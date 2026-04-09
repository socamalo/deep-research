# Tavily Usage Display - Multi-Key Columns Design

## Overview

Redesign `tavily usage` command output to display per-key metrics as separate columns instead of a flat single-key view.

## Current Behavior

- Shows only the active (first available) key's usage data
- Displays metrics in a flat key=value table
- No visibility into other keys' usage

## Desired Behavior

- Show all keys' usage data in a single table
- Each key gets its own column
- Same metrics as rows (plus `enabled` status row)
- Consistent with existing rich-based UI

## Design

### Output Format

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Metric                      ┃ key1        ┃ key2        ┃ key3        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ usage                       ┃ 741         │ 500         │ 200         │
│ limit                       ┃ 1000        │ 1000        │ 1000        │
│ search_usage                ┃ 737         │ 498         │ 195         │
│ crawl_usage                 │ 0           │ 0           │ 0           │
│ extract_usage               │ 4           │ 2           │ 5           │
│ map_usage                   │ 0           │ 0           │ 0           │
│ research_usage              │ 0           │ 0           │ 0           │
│ enabled                     │ true        │ true        │ false       │
└─────────────────────────────┴─────────────┴─────────────┴─────────────┘
```

### Metrics Rows (per key)

From `key.*` API response:
- `usage` - Current usage count
- `limit` - Usage limit (null if no limit)
- `search_usage` - Search endpoint usage
- `crawl_usage` - Crawl endpoint usage
- `extract_usage` - Extract endpoint usage
- `map_usage` - Map endpoint usage
- `research_usage` - Research endpoint usage
- `enabled` - Key enabled status (from local config, not API)

### Account-level Summary (optional footer section)

Keep existing account-level info as a secondary Panel/Table below the per-key table for context.

### Implementation

**Files to modify:**
1. `usage.py` - `tavily_usage()` needs to return data for ALL keys, not just active key
2. `formatters.py` - `format_usage_table()` needs to render multi-column table

**Changes:**

### 1. `usage.py` - `tavily_usage()`

Modify to return per-key usage data for all keys:
```python
{
    "status": "success",
    "keys": [
        {"name": "key1", "usage": {...}, "enabled": true},
        {"name": "key2", "usage": {...}, "enabled": true},
        {"name": "key3", "usage": {...}, "enabled": false},
    ],
    "account": {...},  # Keep for reference
    "sync_result": {...}
}
```

`fetch_key_usage()` already exists and fetches per-key data. `sync_all_keys_usage()` already syncs all keys. The main change is in `tavily_usage()` to return all keys' data instead of just calling API with active key.

### 2. `formatters.py` - `format_usage_table()`

Rewrite to create a table where:
- First column = Metric name
- Subsequent columns = One per key
- Use `Table` with `show_header=True` and key names as header
- Add rows for each metric + enabled status

### 3. `format_usage_json()`

Update to return the new multi-key structure.

## Backward Compatibility

- CLI interface unchanged (`tavily usage`)
- JSON output format changed (now includes `keys` array) - acceptable as this is a display improvement
- No breaking changes to other commands
