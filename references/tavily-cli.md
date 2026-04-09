# Tavily CLI Reference

## Overview

Tavily CLI is a Python CLI tool (`tavily-cli/`) bundled with the deep-research skill. It provides web search, content extraction, crawling, mapping, and deep research capabilities using the Tavily API.

**Key Features:**
- Multi-key support with automatic rotation
- Quota tracking per key (1000 points, 2 points per search)
- Multiple output formats (table, json, markdown)
- Rich, formatted output with usage statistics

## Installation

```bash
# Install from local skill path
uv tool install ~/.claude/skills/deep-research/tavily-cli

# Force reinstall (after updates)
uv tool install ~/.claude/skills/deep-research/tavily-cli --force

# Uninstall
uv tool uninstall tavily
```

## Configuration

### 1. Initialize Config

After first install, run:

```bash
tavily init
```

This creates `~/.config/tavily/keys.json` from the bundled template.

### 2. Edit API Keys

```bash
# Edit the config file
nano ~/.config/tavily/keys.json

# Or use your preferred editor
code ~/.config/tavily/keys.json
```

**Config format:**

```json
{
  "version": 1,
  "last_reset_date": "2026-04-01",
  "keys": [
    {
      "key": "tvly-YOUR-ACTUAL-KEY",
      "name": "key1",
      "usage": 0,
      "errors": [],
      "disabled": false
    }
  ]
}
```

### Config Location

- **Windows**: `C:\Users\<username>\.config\tavily\keys.json`
- **macOS/Linux**: `~/.config/tavily/keys.json`

## Commands

### `tavily search`

Web search with optional filters.

```bash
tavily search "query" [OPTIONS]

# Advanced search with AI answer
tavily search "query" --depth advanced --include-answer true --max-results 10

# News search with time range
tavily search "query" --topic news --time-range week --max-results 15

# Save to JSON
tavily search "query" -o json > results.json
```

**Options:**

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--depth` | choice | basic | Search depth: basic, advanced, fast, ultra-fast |
| `--max-results` | int | 10 | Max results (0-20) |
| `--topic` | choice | general | Topic: general, news, finance |
| `--time-range` | choice | - | Time range: day, week, month, year |
| `--include-answer` | bool | true | Include AI-generated answer |
| `--include-images` | flag | - | Include images |
| `--include-raw-content` | choice | false | Include raw content: true/false/markdown/text |
| `--output`, `-o` | choice | table | Output format: table, json, markdown |

### `tavily extract`

Extract content from specific URLs.

```bash
tavily extract "https://example.com/article" "https://example.com/page2"

# Advanced extraction
tavily extract "https://example.com" --depth advanced --format markdown
```

### `tavily crawl`

Crawl a website with instructions.

```bash
tavily crawl "https://example.com" --instructions "find all blog posts"

# With depth limits
tavily crawl "https://example.com" --max-depth 2 --max-breadth 50
```

### `tavily map`

Map website structure.

```bash
tavily map "https://example.com" --instructions "find documentation pages"
```

### `tavily research`

Start a deep research task (async).

```bash
# Start research
tavily research "comprehensive analysis of AI trends 2026" -o json

# Check status
tavily research-status <job_id> -o json
```

### `tavily usage`

Show API usage and sync keys.

```bash
tavily usage
```

### `tavily config`

Show current key configuration and status.

```bash
tavily config
```

### `tavily init`

Initialize config file in `~/.config/tavily/keys.json`.

```bash
tavily init
```

**Output:**

```
Created config at ~/.config/tavily/keys.json

Next steps:
  1. Edit ~/.config/tavily/keys.json
  2. Replace YOUR_API_KEY_HERE with your actual Tavily API key
```

### `tavily version`

Show version info.

```bash
tavily version
```

## Quota System

- **Per-key limit**: 1000 points
- **Cost per search**: 2 points
- **Automatic disable**: When usage >= 1000 points
- **Monthly reset**: Usage resets on the 1st of each month

## Directory Structure

```
~/.config/tavily/
└── keys.json          # API keys and usage tracking

~/.claude/skills/deep-research/tavily-cli/
├── pyproject.toml     # Package configuration
├── src/local_tavily/
│   ├── cli.py         # CLI commands
│   ├── key_manager.py # Key rotation & quota
│   ├── search.py      # Search module
│   ├── extract.py     # Extract module
│   ├── crawl.py       # Crawl module
│   ├── map.py         # Map module
│   ├── research.py    # Research module
│   ├── usage.py       # Usage module
│   ├── keys.json      # Bundled template (NOT user config)
│   └── ...
└── keys.json          # User config template
```

## Error Handling

**Missing config:**

```
ValueError: Config file not found at ~/.config/tavily/keys.json
```

**Fix:** Run `tavily init`

**No available keys:**

```
NoAvailableKeyError: All API keys are exhausted or disabled
```

**Fix:** Edit `~/.config/tavily/keys.json` to add more keys or wait for monthly reset

## Troubleshooting

### Config not found

```bash
# Check if config exists
ls ~/.config/tavily/

# Re-initialize if needed
tavily init
```

### Keys not working

```bash
# Check key status
tavily config

# Verify API key is correct
cat ~/.config/tavily/keys.json | grep key
```

### Update to latest version

```bash
# Uninstall and reinstall
uv tool uninstall tavily
uv tool install ~/.claude/skills/deep-research/tavily-cli
```

## Quick Reference

```bash
# Install
uv tool install ~/.claude/skills/deep-research/tavily-cli

# First-time setup
tavily init
nano ~/.config/tavily/keys.json  # Add your API key

# Basic usage
tavily search "query"
tavily search "query" -o json
tavily extract "https://example.com"
tavily research "topic"

# Info
tavily version
tavily config
tavily usage
```
