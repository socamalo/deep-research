# Deep Research Skill

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-purple)](https://claude.ai/)

A skill for conducting multi-phase deep research using Tavily CLI for search and **Firecrawl CLI (REQUIRED)** for content scraping, with **content quality validation (REQUIRED)** and human judgment at each step.

## Overview

This skill provides a structured 3-phase research methodology:

1. **Initial Discovery** - Map the landscape, identify themes, scrape and validate high-value sources
2. **Breadth Expansion** - Explore multiple angles, scrape and validate content systematically
3. **Depth Exploration** - Deep dive into priority domains, comprehensive scraping with validation

**Key principles:**
1. **Human judgment guides the research** at every phase, not automation
2. **Raw content MUST be preserved** using Firecrawl on high-value sources
3. **Content quality MUST be validated** - every scraped file is evaluated for errors and relevance
4. **Quality gates MUST be met** - sufficient high-quality sources required before synthesis
5. **Source attribution is mandatory** in every synthesis

**🔬 Autoresearch Optimized:** All quality evaluation parameters (risk thresholds, scoring weights, content requirements) have been systematically optimized through autoresearch iterations for maximum research accuracy and minimal false positives.

**🐍 Includes Python Package:** This skill bundles a custom Tavily CLI (`tavaliy-cli/`) - a Python CLI tool with API key rotation, multi-format output, and comprehensive test suite. Install with `uv tool install`.

## Installation

### Method 1: Install via npx (Recommended - when published)

```bash
npx skills add https://github.com/socamalo/deep-research.git
```

### Method 2: Clone via Git

```bash
git clone https://github.com/socamalo/deep-research.git ~/.claude/skills/deep-research
```

### Method 3: Manual Installation

1. Download or clone this repository
2. Copy the `deep-research` folder to your Claude Code skills directory:
   - macOS/Linux: `~/.claude/skills/`
   - Windows: `%USERPROFILE%\.claude\skills\`

### Prerequisites

After installation, install the required CLI tools:

#### Tavily CLI

```bash
# Check if already installed
which tavily && tavily --help

# Install from local path (bundled with this skill)
uv tool install ~/.claude/skills/deep-research/tavaliy-cli

# Update (if needed)
uv tool uninstall tavily
uv tool install ~/.claude/skills/deep-research/tavaliy-cli
```

**Configure Tavily API Keys:**

```bash
cd ~/.claude/skills/deep-research/tavaliy-cli
cp .env.example .env
# Edit .env and add your Tavily API key(s)
```

Supports multiple keys for automatic rotation (TAVILY_API_KEY_1, TAVILY_API_KEY_2, etc.)

#### Firecrawl CLI (REQUIRED)

```bash
npm install -g firecrawl
```

**Configure Firecrawl API Key:**

```bash
export FIRECRAWL_API_KEY="your-firecrawl-api-key"
```

Get your API keys:
- Tavily: https://tavily.com
- Firecrawl: https://firecrawl.dev

## Source Evaluation (Pre-Scraping)

**BEFORE scraping, use Quality Evaluator (Pre-Scrape Mode) to filter Tavily results.**

### Why Pre-Evaluation Matters

- Tavily Score ≠ content quality (many 1.00 scores lead to 404 pages)
- Portal sites have high link rot
- Some sites block direct article access but allow homepage + crawl
- Pre-filtering saves time and reduces failed scrapes

### Source Evaluation Process

First, read `references/quality-evaluator.md` (Mode 1: Pre-Scrape Assessment) for detailed evaluation guidelines.

Then invoke:

```markdown
Evaluate sources (Pre-Scrape Mode):
- Research topic: {topic}
- Results file: ./01-initial-discovery/raw-results/search-01.json

Use skill: quality-evaluator

Output: JSON with recommended/excluded URLs and risk assessment
```

### Domain Risk Awareness

**High Risk (frequent 404/invalid URLs):**
- News portals: sina.com.cn, sohu.com, 163.com, ifeng.com
- Regional news subdomains
- Temporary event pages

**Strategy for high-risk domains:**
1. Try direct scrape first (quick fail check)
2. If 404 → extract homepage URL
3. Use `firecrawl map "https://homepage.com"` to discover valid content
4. Or skip and find alternative sources

---

## Content Quality Validation (Post-Scraping)

**Every scraped file MUST be validated using Quality Evaluator (Post-Scrape Mode) before entering synthesis.**

### Why Deep Validation is Required

Without validation, your research pipeline may include:
- 404/403 error pages (even 5-line nginx errors)
- CAPTCHA/login walls
- Marketing pages with high word count but low substance
- Thin content with mostly navigation/ads

**Simple word-counting FAILS:**
- A 404 error page can have 20+ lines of nginx HTML
- A marketing page can have 400+ lines of specs without real insight

### Quality Ratings

| Rating | Criteria | Action |
|--------|----------|--------|
| **high** | Weighted score >= 7.7, passed validity | Keep and prioritize |
| **medium** | Weighted score 5.0-7.6, passed validity | Keep for synthesis |
| **low** | Weighted score 3.0-4.9, passed validity | Discard |
| **poor** | Weighted score < 3.0, passed validity | Discard immediately |
| **failed** | Failed validity (404/error/CAPTCHA) | Discard + retry |

### Quality Gate Thresholds (Autoresearch Optimized)

Based on systematic optimization (targeting 50 total sources with authority-weighted scoring):

**Phase 1 (Initial Discovery):**
- **Queries**: 7 broad queries
- **Max results**: 15 per query
- **Min quality score**: 0.52
- Minimum: 5 high/medium quality sources
- Target: 8 sources
- Ideal: 10+ diverse sources

**Phase 2 (Breadth Expansion):**
- **Queries**: 9 targeted queries
- **Max results**: 12 per query
- **Min quality score**: 0.62
- Minimum: 8 high/medium quality sources
- Target: 12 sources
- Ideal: 15+ sources

**Phase 3 (Depth Exploration):**
- **Queries**: 8 deep queries
- **Max results**: 10 per query
- **Min quality score**: 0.67
- Minimum: 10 high/medium quality sources
- Target: 15+ sources
- Ideal: 20+ authoritative sources

**Overall Strategy:**
- **max_total_sources**: 50 (across all phases)
- **Scoring priority**: Authority (0.32) > Density (0.25) > Relevance (0.25) > Timeliness (0.10) > Uniqueness (0.08)

**Rule: Do NOT proceed to synthesis until quality gate is met.**

### Validation Process

1. Scrape URL with Firecrawl
2. Read scraped file
3. Invoke Quality Evaluator (Post-Scrape Mode)
4. Get quality rating
5. Keep high/medium, discard low/poor/failed
6. Retry with new searches if quality gate not met

## Firecrawl Usage (REQUIRED)

**Every research phase MUST use Firecrawl to scrape high-value sources.**

### When to Scrape

- URLs with Tavily score > 0.75
- Authoritative sources (universities, official docs, recognized experts)
- In-depth articles or guides
- Content you need to quote or reference

### How to Scrape

```bash
# Always save to raw-content directory
firecrawl scrape "https://example.com/article" markdown \
  -o ./01-initial-discovery/raw-content/example-com-article.md

# Scrape with only main content
firecrawl scrape "https://example.com/article" markdown \
  --only-main-content \
  -o ./raw-content/example-com-article.md
```

## Quick Start

```bash
# Start Claude
claude

# Ask Claude to research using the skill:
# "Research AI agent frameworks using the deep-research skill"
```

## How It Works

The skill guides Claude through structured research:

1. **Phase 1**: Claude designs broad searches, scrapes 5-8 URLs, validates content quality, ensures 5+ high-quality sources
2. **User Checkpoint**: Review synthesis with quality ratings, set research direction
3. **Phase 2**: Claude explores multiple angles, scrapes 8-12 sources, validates, ensures 8+ high-quality sources
4. **User Checkpoint**: Identify priority domains for deep dive
5. **Phase 3**: Claude conducts targeted deep research, scrapes 10-15 sources, validates, ensures 10+ high-quality sources
6. **Final Report**: Comprehensive synthesis with full source attribution

## Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  User provides research topic                                     │
└──────────────────┬──────────────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: Initial Discovery                                       │
│  - Claude designs 3-5 broad Tavily searches                       │
│  - Identifies 5-8 high-value URLs (score > 0.75)                  │
│  - Scrapes each URL with Firecrawl                                │
│  - Quality Evaluator evaluates each scrape                  │
│  - Quality Gate: Minimum 5 high/medium sources                    │
│  - If not met: retry with new searches                            │
│  - Reviews validated content, synthesizes findings                │
└──────────────────┬──────────────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  User Checkpoint 1                                                │
│  - Review synthesis & quality report                              │
│  - Discuss and set direction                                      │
└──────────────────┬──────────────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 2: Breadth Expansion                                       │
│  - Claude designs targeted searches per angle                     │
│  - Identifies 8-12 high-value sources                             │
│  - Scrapes all sources with Firecrawl                             │
│  - Quality Evaluator evaluates each scrape                  │
│  - Quality Gate: Minimum 8 high/medium sources                    │
│  - If not met: retry with new searches                            │
│  - Identifies 3-5 core domains                                    │
└──────────────────┬──────────────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  User Checkpoint 2                                                │
│  - Review breadth findings with quality report                    │
│  - Prioritize domains for deep dive                               │
└──────────────────┬──────────────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 3: Depth Exploration                                       │
│  - Targeted searches on priority domains                          │
│  - Identifies 10-15 authoritative sources                         │
│  - Comprehensive Firecrawl scraping                               │
│  - Quality Evaluator evaluates each scrape                  │
│  - Quality Gate: Minimum 10 high/medium sources                   │
│  - If not met: retry with new searches                            │
│  - Domain synthesis with cross-domain analysis                    │
└──────────────────┬──────────────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────────────┐
│  Final Report                                                     │
│  - Comprehensive synthesis                                        │
│  - Clear arguments with source references                         │
│  - Appendix listing all raw content files with quality ratings    │
└─────────────────────────────────────────────────────────────────┘
```

## Quality Validation Workflow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Firecrawl      │────▶│  Quality        │────▶│  Quality Gate   │
│  Scrape URL     │     │  Validator      │     │  Check          │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                              ┌──────────────────────────┼──────────┐
                              │                          │          │
                              ▼                          ▼          ▼
                        ┌─────────┐               ┌──────────┐ ┌────────┐
                        │  high   │               │  medium  │ │  low/  │
                        │ quality │               │  quality │ │ failed │
                        └────┬────┘               └─────┬────┘ └───┬────┘
                             │                          │          │
                             ▼                          ▼          ▼
                        ┌─────────┐               ┌──────────┐ ┌────────┐
                        │  Keep   │               │   Keep   │ │ Discard│
                        │& Prioritize             │          │ │ + Retry│
                        └─────────┘               └──────────┘ └────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                         Quality Gate Logic                          │
├─────────────────────────────────────────────────────────────────────┤
│  Count high + medium quality sources                                │
│       │                                                             │
│       ▼                                                             │
│  >= Minimum required? ──YES──▶ Proceed to synthesis                 │
│       │                                                             │
│       NO                                                            │
│       │                                                             │
│       ▼                                                             │
│  Document failed URLs                                               │
│  Design new search queries                                          │
│  Execute new Tavily search                                          │
│  Scrape new URLs                                                    │
│  Validate new content                                               │
│       │                                                             │
│       └────────────────────────▶ Loop until gate met                │
└─────────────────────────────────────────────────────────────────────┘
```

## CLI Reference

### Tavily Search

```bash
# Basic search
tavily search "query"

# Advanced search with more results
tavily search --depth advanced --max-results 10 "query"

# Extract content from URL
tavily extract "https://example.com"
```

### Firecrawl Scrape (REQUIRED)

```bash
# Scrape to markdown (always use -o flag)
firecrawl scrape "https://example.com" markdown \
  -o ./raw-content/example-com.md

# Scrape only main content
firecrawl scrape "https://example.com" markdown \
  --only-main-content \
  -o ./raw-content/example-com.md

# Scrape multiple formats
firecrawl scrape "https://example.com" \
  --format markdown,links,summary \
  -o ./raw-content/example-com.json

# Crawl website
firecrawl crawl "https://example.com"
```

## Output Structure

All research outputs are saved in `research-output/`:

```
research-output/
├── 01-initial-discovery/
│   ├── raw-results/          # Tavily search results (JSON)
│   ├── raw-content/          # Firecrawl outputs - REQUIRED
│   │   ├── source-01-domain-com.md
│   │   └── source-02-authority-org.md
│   ├── synthesis.md          # Phase findings & proposed directions
│   ├── user-discussion.md    # Direction decisions
│   └── quality-report.md     # Quality validation results
├── 02-breadth-expansion/
│   ├── raw-results/
│   ├── raw-content/          # Phase 2 scraped sources
│   │   ├── source-01.md
│   │   ├── source-02.md
│   │   └── source-03.md
│   ├── synthesis.md          # Breadth findings & domains
│   ├── user-discussion.md    # Domain prioritization
│   └── quality-report.md     # Quality validation results
├── 03-depth-exploration/
│   ├── raw-results/
│   ├── raw-content/          # Phase 3 deep scraped sources
│   │   ├── source-01.md
│   │   ├── source-02.md
│   │   └── source-03.md
│   ├── synthesis.md          # Deep domain insights
│   ├── user-discussion.md
│   └── quality-report.md     # Quality validation results
├── 04-final-report/
│   └── comprehensive-report.md  # Full synthesis with source refs
└── meta/
    ├── research-log.md       # Complete search history
    └── iteration-notes.md    # Feedback for improvement
```

### File Naming Convention

Use descriptive names based on source:
```
huain-com-guzheng-article.md
guzheng-cn-composer-interview.md
people-cn-culture-report.md
nature-com-ai-research-paper.md
github-com-project-readme.md
```

### File Header Template

Each scraped file includes metadata:

```markdown
# Scraped Content

**Source**: https://example.com/article-path
**Scraped Date**: 2026-03-18
**Tavily Score**: 0.95
**Relevance**: High - authoritative source on topic
**Quality**: high (validated)

---

[Original content follows...]
```

### Quality Report Template

Each phase includes a quality report:

```markdown
# Content Quality Report - Phase X

## Summary
- Total scraped: 12
- High quality: 5
- Medium quality: 4
- Low quality: 1
- Failed: 2

## Quality Gate Status: PASSED
- Required: 5 high/medium
- Achieved: 9 high/medium

## Failed Sources (Retried)
- source-05-broken.md: 404 Not Found
- source-09-paywall.md: Login required

## Retry Actions
- Searched alternative sources for [topic]
- Found replacements: source-05-alt.md, source-09-alt.md
- All replacements passed quality validation
```

### Source Attribution in Synthesis

Every synthesis.md includes source references:

```markdown
## Source References
- [source-01-domain-com.md](./raw-content/source-01-domain-com.md) - Key findings on X (quality: high)
- [source-02-authority-org.md](./raw-content/source-02-authority-org.md) - Data on Y (quality: medium)
- [source-03-github-com.md](./raw-content/source-03-github-com.md) - Implementation details (quality: high)
```

## Tips for Best Results

1. **Engage at checkpoints** - Your input shapes the research direction
2. **Ask for rationale** - Have Claude explain why certain sources were selected
3. **Challenge assumptions** - If synthesis seems off, push back and refine
4. **Verify Firecrawl usage** - Ensure high-value sources are being scraped
5. **Check quality validation** - Ensure every scraped file is validated
6. **Monitor quality gates** - Confirm sufficient sources before synthesis
7. **Check source attribution** - Every synthesis should reference raw-content files
8. **Iterate if needed** - Don't hesitate to revisit a phase

## Examples

### Example 1: Technology Research

**Topic:** "Compare React server components vs traditional SSR"

**Phase 1:** Map the landscape - RSC architecture, SSR patterns, comparison articles
- Scraped: React docs, Vercel blog posts, comparison articles
- Validated: 6 high/medium quality sources (target: 5)
- Checkpoint 1: User wants focus on performance and developer experience

**Phase 2:** Explore performance benchmarks, DX feedback, adoption patterns
- Scraped: Benchmark studies, GitHub discussions, case studies
- Validated: 10 high/medium quality sources (target: 8)
- Checkpoint 2: User prioritizes: performance data and migration stories

**Phase 3:** Deep dive into benchmark studies and case studies
- Scraped: Detailed benchmark reports, migration guides, official docs
- Validated: 12 high/medium quality sources (target: 10)

**Report:** Data-backed comparison with recommendations and full source attribution

### Example 2: Market Research

**Topic:** "AI coding assistant market landscape 2024"

**Phase 1:** Identify key players, segments, recent developments
- Scraped: Market reports, company blogs, analyst reviews
- Validated: 8 high/medium quality sources (target: 5)
- Checkpoint 1: User wants focus on enterprise adoption

**Phase 2:** Explore enterprise case studies, pricing, ROI analyses
- Scraped: Enterprise case studies, pricing pages, ROI calculators
- Validated: 12 high/medium quality sources (target: 8)
- Checkpoint 2: User prioritizes: security and integration challenges

**Phase 3:** Deep research on security audits and integration patterns
- Scraped: Security whitepapers, integration docs, compliance reports
- Validated: 15 high/medium quality sources (target: 10)

**Report:** Market analysis with security-focused recommendations

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| **Only using Tavily, not Firecrawl** | **MUST scrape high-value URLs with Firecrawl after every search phase** |
| **Not saving raw content** | **ALWAYS save scraped markdown to `raw-content/` directory** |
| **Skipping content validation** | **ALWAYS validate with Quality Evaluator after scraping** |
| **Not meeting quality gates** | **Loop with new searches until minimum sources achieved** |
| **Immediate synthesis without review** | **Review scraped AND validated content before synthesizing** |
| **Losing source attribution** | **Reference specific scraped files in synthesis.md** |
| **Scoring threshold too low** | **Only scrape sources with score > 0.75 or clear authority** |
| **Not creating raw-content directory** | **Create directory structure BEFORE starting research** |
| **Skipping user checkpoints** | Always pause for direction - user's input shapes quality |
| **Too many searches without synthesis** | Stop to analyze patterns every 3-5 searches |
| **Rushing to final report** | Depth exploration often reveals critical insights |

## License

MIT - Feel free to adapt for your own use.
