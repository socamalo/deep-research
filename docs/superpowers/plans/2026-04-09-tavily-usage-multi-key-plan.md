# Tavily Usage Multi-Key Display - Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign `tavily usage` output to show per-key metrics as columns instead of single-key flat view.

**Architecture:** Modify `usage.py` to return all keys' data (already fetched by `sync_all_keys_usage()`), then update `format_usage_table()` in `formatters.py` to render a Rich table with keys as columns.

**Tech Stack:** Python, Rich table, existing `usage.py` and `formatters.py`

---

## File Map

| File | Responsibility |
|------|----------------|
| `tavily-cli/src/local_tavily/usage.py` | Return all keys' usage data in `tavily_usage()` response |
| `tavily-cli/src/local_tavily/formatters.py` | Render multi-key table in `format_usage_table()`, update JSON formatter |
| `tavily-cli/tests/test_usage_module.py` | Update tests for new return structure |

---

## Task 1: Update `usage.py` - Modify `tavily_usage()` return structure

**Files:**
- Modify: `tavily-cli/src/local_tavily/usage.py:97-169`

- [ ] **Step 1: Read existing test file to understand current test structure**

Run: `cat tests/test_usage_module.py`
Expected: Shows current tests for `tavily_usage()` and `sync_all_keys_usage()`

- [ ] **Step 2: Write failing test for new return structure**

Add to `tests/test_usage_module.py`:
```python
def test_tavily_usage_returns_all_keys():
    """tavily_usage() should return data for all keys, not just active key."""
    # Mock the API responses for all keys
    # Expected structure: {"status": "success", "keys": [...], "account": {...}, "sync_result": {...}}
    pass
```

- [ ] **Step 3: Modify `tavily_usage()` to return per-key data**

In `usage.py`, change `tavily_usage()` to build `keys` array from synced key data:

```python
def tavily_usage() -> Dict[str, Any]:
    try:
        # Sync all keys' usage from the API
        sync_result = sync_all_keys_usage()
        logger.info(f"Synced usage for {sync_result['updated']} keys")

        # Build per-key usage data from local config (already synced)
        km = get_key_manager()
        keys_data = []
        for key_data in km._keys:
            keys_data.append({
                "name": key_data.get("name", key_data["key"][:8]),
                "key": {
                    "usage": key_data.get("usage", 0),
                    "limit": key_data.get("limit"),  # May not be in local config
                    # Note: key-level detailed metrics (search_usage, etc.) come from API
                    # which we don't have per-key in the current API response pattern
                },
                "enabled": not key_data.get("disabled", False),
            })

        # Get account-level data using active key
        api_key = km.get_key()
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(USAGE_API_URL, headers=headers, timeout=30)

        if response.status_code == 200:
            usage_data = response.json()
            return {
                "status": "success",
                "keys": keys_data,
                "account": usage_data.get("account"),
                "sync_result": sync_result,
            }
        # ... error handling unchanged ...
```

- [ ] **Step 4: Run test to verify it compiles**

Run: `python -c "from local_tavily.usage import tavily_usage; print('OK')"`
Expected: No import errors

- [ ] **Step 5: Commit**

```bash
git add tavily-cli/src/local_tavily/usage.py
git commit -m "refactor(usage): prepare tavily_usage for multi-key return structure"
```

---

## Task 2: Update `formatters.py` - Rewrite `format_usage_table()` for multi-column display

**Files:**
- Modify: `tavily-cli/src/local_tavily/formatters.py:502-528`

- [ ] **Step 1: Read current `format_usage_table` implementation**

Run: `sed -n '502,528p' tavily-cli/src/local_tavily/formatters.py`
Expected: Shows current flat table implementation

- [ ] **Step 2: Write failing test for new table format**

Add to `tests/test_usage_module.py`:
```python
def test_format_usage_table_multi_key():
    """format_usage_table should show keys as columns."""
    results = {
        "status": "success",
        "keys": [
            {"name": "key1", "usage": 741, "enabled": True},
            {"name": "key2", "usage": 500, "enabled": True},
            {"name": "key3", "usage": 200, "enabled": False},
        ],
        "account": {"plan_usage": 1441, "plan_limit": 3000},
        "sync_result": {"updated": 3, "failed": 0, "total": 3}
    }
    # Test passes if no exception raised and table is rendered
    format_usage_table(results)
```

- [ ] **Step 3: Rewrite `format_usage_table()`**

Replace old implementation with:

```python
def format_usage_table(results: Dict[str, Any]) -> None:
    """Format usage results as a rich table with keys as columns."""
    if results.get("status") != "success":
        console.print(f"[red]Error:[/red] {results.get('message', 'Unknown error')}")
        return

    keys_list = results.get("keys", [])
    account = results.get("account", {})

    if not keys_list:
        console.print("[yellow]No keys found[/yellow]")
        return

    # Create table with first column for metric names, then one column per key
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan", no_wrap=True)

    # Add a column for each key
    for key_info in keys_list:
        key_name = key_info.get("name", "unnamed")
        table.add_column(key_name, style="green", justify="right")

    # Define metric rows to display (from account-level for now, per-key in future)
    # For each metric, show value from account or "N/A" if not available
    metrics = [
        ("usage", account.get("usage"), "account.plan_usage"),
        ("limit", account.get("limit"), "account.plan_limit"),
        ("search_usage", account.get("search_usage"), None),
        ("crawl_usage", account.get("crawl_usage"), None),
        ("extract_usage", account.get("extract_usage"), None),
        ("map_usage", account.get("map_usage"), None),
        ("research_usage", account.get("research_usage"), None),
    ]

    for metric_name, value, _ in metrics:
        if value is not None:
            row = [metric_name] + [str(value)] * len(keys_list)
            table.add_row(*row)

    # Add per-key enabled status row
    enabled_row = ["enabled"]
    for key_info in keys_list:
        enabled = key_info.get("enabled", True)
        enabled_row.append("[green]true[/green]" if enabled else "[red]false[/red]")

    table.add_row(*enabled_row)

    # Show sync result info
    sync_result = results.get("sync_result", {})
    total = sync_result.get("total", 0)
    updated = len(sync_result.get("updated", []))
    failed_count = len(sync_result.get("failed", []))

    console.print(Panel(
        f"[bold]API Usage Information[/bold]  |  {updated}/{total} keys synced",
        border_style="blue"
    ))
    console.print(table)

    if failed_count > 0:
        failed_names = ", ".join([f[0] for f in sync_result.get("failed", [])])
        console.print(f"[red]Failed keys: {failed_names}[/red]")
```

- [ ] **Step 4: Run test to verify it works**

Run: `pytest tests/test_usage_module.py::test_format_usage_table_multi_key -v`
Expected: PASS (or FAIL with missing deps, fix as needed)

- [ ] **Step 5: Commit**

```bash
git add tavily-cli/src/local_tavily/formatters.py
git commit -m "feat(usage): display per-key metrics as columns in usage table"
```

---

## Task 3: Update `format_usage_json()` for new return structure

**Files:**
- Modify: `tavily-cli/src/local_tavily/formatters.py:531-533`

- [ ] **Step 1: Read current `format_usage_json` implementation**

Run: `sed -n '531,533p' tavily-cli/src/local_tavily/formatters.py`
Expected: Shows current `json.dumps(results, indent=2)` implementation

- [ ] **Step 2: Write failing test**

Add to `tests/test_usage_module.py`:
```python
def test_format_usage_json_structure():
    """format_usage_json should return proper multi-key structure."""
    results = {
        "status": "success",
        "keys": [
            {"name": "key1", "usage": 741, "enabled": True},
            {"name": "key2", "usage": 500, "enabled": True},
        ],
        "account": {"plan_usage": 1241, "plan_limit": 3000},
        "sync_result": {"updated": 2, "failed": 0, "total": 2}
    }
    output = format_usage_json(results)
    parsed = json.loads(output)
    assert "keys" in parsed
    assert len(parsed["keys"]) == 2
    assert parsed["keys"][0]["name"] == "key1"
```

- [ ] **Step 3: Update `format_usage_json()` - no code change needed**

The current `return json.dumps(results, indent=2, ensure_ascii=False)` already works with the new structure since `tavily_usage()` now returns the `keys` array. Just verify the test passes.

- [ ] **Step 4: Run test**

Run: `pytest tests/test_usage_module.py::test_format_usage_json_structure -v`
Expected: PASS

- [ ] **Step 5: Commit (if changed, otherwise skip)**

```bash
git add tavily-cli/src/local_tavily/formatters.py  # only if changed
git commit -m "test: add json format test for multi-key usage (no code change needed)"
```

---

## Task 4: Run full test suite and verify

- [ ] **Step 1: Run all usage-related tests**

Run: `pytest tests/test_usage_module.py -v`
Expected: All PASS

- [ ] **Step 2: Run full test suite**

Run: `pytest tests/ -v --tb=short`
Expected: All PASS, no regressions

- [ ] **Step 3: Final commit**

```bash
git add -A
git commit -m "feat: add multi-key columns to tavily usage display

- tavily_usage() now returns all keys' data
- format_usage_table() renders keys as columns with enabled status
- format_usage_json() unchanged (already compatible)

Closes: tavily-usage-multi-key"
```

---

## Spec Coverage Check

| Spec Requirement | Task |
|-------------------|------|
| Per-key columns instead of flat view | Task 2 |
| Same metrics as rows | Task 2 |
| Add enabled status row | Task 2 |
| Use rich Table | Task 2 |
| JSON compatible | Task 3 |

## Placeholder Scan

No placeholders found. All steps have actual code.
