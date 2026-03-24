# Content Quality Evaluator

Unified quality assessment framework for research content. Provides two evaluation modes: pre-scrape source assessment and post-scrape content validation.

## Overview

| Mode | When to Use | Input | Output |
|------|-------------|-------|--------|
| **Pre-Scrape** | After Tavily search, before Firecrawl | Tavily JSON results | Recommended/excluded URLs with risk analysis |
| **Post-Scrape** | After Firecrawl scrape, before synthesis | Scraped markdown file | Quality rating and validation report |

## Mode 1: Pre-Scrape Assessment

Evaluates Tavily search results to identify high-value sources and filter out problematic URLs before committing to scraping.

### Why It Matters

- Tavily relevance score does not correlate with scrape success
- Scores of 0.95+ frequently lead to 404 pages
- Portal sites have high link rot
- Some sites block direct URLs but allow homepage crawling

### Evaluation Dimensions

| Dimension | Assessment Criteria |
|-----------|---------------------|
| **Content Type** | Academic / News / Blog / Product / Forum |
| **Source Credibility** | .edu/.gov > Established media > Personal blog > Unknown |
| **Domain Risk** | Historical 404 rate, URL stability |
| **URL Validity** | Direct access likely to succeed? |
| **Content Depth** | Does snippet suggest substantive content? |

### Domain Risk Classification

| Risk Level | Score | Characteristics |
|------------|-------|-----------------|
| **LOW** | 0.0 - 0.3 | Academic (.edu), Government (.gov), Official docs, Established orgs |
| **MEDIUM** | 0.3 - 0.6 | Archive sites, Community platforms, Older news content |
| **HIGH** | 0.6 - 1.0 | News portals (sina, sohu, 163), Temp pages, URL shorteners |

**Quantitative Risk Factors:**
- Domain in known problematic list: +0.4 risk
- URL contains date pattern > 2 years old: +0.2 risk
- URL has excessive parameters (> 3): +0.2 risk
- Domain TLD is .cn (news portal): +0.3 risk
- Subdomain indicates regional/local: +0.2 risk

**Tavily Score Adjustments:**
- If risk score > 0.5 AND Tavily score < 0.90: **EXCLUDE**
- If risk score > 0.7: **EXCLUDE** regardless of Tavily score
- If risk score < 0.3 AND Tavily score > 0.75: **RECOMMEND**

### Input Format

```json
{
  "research_topic": "topic name",
  "search_query": "actual query used",
  "tavily_results": [
    {
      "url": "https://example.com/article",
      "title": "Article Title",
      "score": 0.95,
      "snippet": "Content preview...",
      "published_date": "2024-01-15"
    }
  ]
}
```

### Output Format

```json
{
  "evaluation_summary": {
    "total_results": 10,
    "recommended_count": 5,
    "excluded_count": 3,
    "needs_alternative": 2
  },
  "recommended_urls": [
    {
      "url": "https://example.org/article",
      "tavily_score": 0.89,
      "source_type": "academic_paper",
      "credibility": "high",
      "domain_risk": "low",
      "reasoning": "University repository, stable URL pattern"
    }
  ],
  "excluded_urls": [
    {
      "url": "https://news-portal.com/2024/xxxx",
      "tavily_score": 1.00,
      "domain_risk": "high",
      "risk_reason": "News portal with high historical 404 rate",
      "alternative_suggestion": "Search for alternative sources"
    }
  ],
  "alternative_strategy": [
    {
      "original_url": "https://portal.com/article/123",
      "suggested_action": "crawl_homepage",
      "homepage": "https://portal.com",
      "reasoning": "Direct URL likely expired, try discovery from homepage"
    }
  ]
}
```

### Decision Rules

**INCLUDE when:**
- Credible source with stable URL pattern
- Content type matches research needs
- No known domain risk
- Snippet indicates substantive content

**EXCLUDE when:**
- High-risk domain AND Tavily score < 0.90
- URL format problems (excessive parameters, session tokens)
- Content type irrelevant (shopping, video-only pages)
- Historical pattern of failures

**ALTERNATIVE STRATEGY when:**
- Source has value but URL is risky
- Homepage may yield discoverable content
- Worth quick validation before deep crawl

### Usage Prompt (Pre-Scrape)

```markdown
Evaluate sources (Pre-Scrape Mode):
- Research topic: {topic}
- Search query: {query}
- Results file: ./raw-results/search-01.json

Apply quality assessment and output JSON with:
- Recommended URLs for scraping
- Excluded URLs with risk rationale
- Alternative strategies where applicable
```

---

## Mode 2: Post-Scrape Validation

Validates scraped content to ensure quality before synthesis. Replaces simplistic word counting with multi-dimensional assessment.

### Why It Matters

Firecrawl may return content that appears valid but has quality issues:
- Error pages (404, 403) with sufficient length to pass word-count checks
- CAPTCHA walls or login requirements
- Marketing pages with high volume but low information density
- Navigation-heavy pages with minimal substantive content

### Evaluation Dimensions

| Dimension | Weight | Assessment |
|-----------|--------|------------|
| **Validity** | Gate | Is this a valid content page? (404/403/CAPTCHA = fail) |
| **Relevance** | 30% | How relevant to research topic? (1-10) |
| **Authority** | 20% | Source credibility and expertise (1-10) |
| **Information Density** | 25% | Signal-to-noise ratio (1-10) |
| **Timeliness** | 15% | Currency of information (1-10) |
| **Uniqueness** | 10% | Originality of content (1-10) |

### Validity Check (Required Gate)

Content MUST pass validity to proceed to scoring.

**Automatic Failure Keywords (case-insensitive):**
```
- "404 Not Found", "403 Forbidden", "410 Gone"
- "nginx/", "Apache/", "Server Error"
- "Page not found", "Content unavailable", "Article deleted"
- "CAPTCHA", "captcha", "I'm not a robot"
- "Please log in", "Login required", "Sign in to continue"
- "Redirecting", "seconds", "Click here if not redirected"
- "Access denied", "Forbidden", "403"
```

**Failure Detection Rules:**
- Title contains error keywords: **FAIL**
- First 200 chars contain 2+ error indicators: **FAIL**
- Content length < 100 chars AND contains error keyword: **FAIL**
- Contains CAPTCHA-related text: **FAIL**

### Scoring Guidelines

#### Relevance (1-10)

| Score | Criteria | Keywords/Indicators |
|-------|----------|---------------------|
| 9-10 | Comprehensive coverage | Topic in title + headings + throughout |
| 7-8 | Strong coverage | Topic appears 5+ times, main subject |
| 5-6 | Moderate relevance | Topic appears 3-5 times, partial coverage |
| 3-4 | Weak relevance | Topic appears 1-2 times, tangential |
| 1-2 | Minimal relevance | Topic mentioned briefly or not at all |

**Auto-calculation:**
- Topic in title: +2 points
- Topic in first 200 chars: +2 points
- Topic frequency: +1 per occurrence (max +4)
- Topic in conclusion: +2 points

#### Authority (1-10)

| Source Type | Base Score | Indicators |
|-------------|------------|------------|
| .edu / .gov | 9 | Educational/government domain |
| Academic journal | 9 | DOI, citations, peer-reviewed |
| Official docs | 8 | docs.*, developer.*, official guide |
| Major media | 7 | Established news orgs, recognized brands |
| Industry blog | 6 | Professional author, date, citations |
| Personal blog | 4 | Individual author, limited credentials |
| Unknown/Untrusted | 2 | No author info, spam indicators |

**Adjustments:**
- Named expert author: +1
- Citations/references: +1
- Publication date within 2 years: +1
- Anonymous/no author: -2

#### Information Density (1-10)

Calculate using:
```
density_score = (unique_content_words / total_words) × 10
```

| Ratio | Score | Characteristics |
|-------|-------|-----------------|
| > 0.8 | 9-10 | Minimal nav/ads/templates, pure content |
| 0.6-0.8 | 7-8 | Some boilerplate but mostly substantive |
| 0.4-0.6 | 5-6 | Mixed content, padded with templates |
| 0.2-0.4 | 3-4 | Heavy nav/ads, low signal-to-noise |
| < 0.2 | 1-2 | Almost entirely noise |

**Noise indicators to exclude:**
- Navigation menus ("Home", "About", "Contact")
- Footer text
- Advertisement labels
- Social media widgets
- Cookie notices

### Quality Ratings

| Rating | Score Range | Action | Threshold for Synthesis |
|--------|-------------|--------|------------------------|
| **high** | >= 7.5 | Keep and prioritize | Required: min 3 per phase |
| **medium** | 5.0 - 7.4 | Keep with caveats | Acceptable: counts toward total |
| **low** | 3.0 - 4.9 | Discard | Exclude from synthesis |
| **poor** | < 3.0 | Discard immediately | Exclude from synthesis |
| **failed** | Validity fail | Discard + retry if critical | Exclude from synthesis |

**Minimum Content Requirements:**
- Word count: > 300 words (after stripping nav/footer)
- Unique content ratio: > 40% (non-template text)
- Keyword density: Research topic appears > 3 times

### Input Format

- Research topic
- Source URL
- Scraped content file (Markdown)

### Output Format

```json
{
  "file": "source-name.md",
  "url": "https://example.com/source",
  "validity": {
    "passed": true,
    "check": "valid content page"
  },
  "scores": {
    "relevance": 9,
    "authority": 8,
    "information_density": 6,
    "timeliness": 7,
    "uniqueness": 8,
    "weighted_total": 7.65
  },
  "quality_rating": "high",
  "issues": [
    "Contains navigation menu and footer content",
    "Image placeholders present but not loaded"
  ],
  "usable_content": {
    "estimated_word_count": 1800,
    "content_type": "expert_interview",
    "key_topics": ["topic A", "topic B", "topic C"],
    "summary": "Brief description of content value"
  },
  "recommendation": "keep - extract key insights",
  "improvement_suggestions": [
    "Extract core interview content",
    "Focus on technical details section"
  ]
}
```

### Usage Prompt (Post-Scrape)

```markdown
Validate content (Post-Scrape Mode):
- Research topic: {topic}
- File to validate: ./raw-content/example.md
- Source URL: {original_url}

Apply validation framework and output JSON assessment with quality rating.
```

### Weight Formula

```
Weighted Score (Post-Scrape only) =
  (Relevance × 0.30) +
  (Authority × 0.20) +
  (Information Density × 0.25) +
  (Timeliness × 0.15) +
  (Uniqueness × 0.10)
```

Validity is a binary gate - must pass before scoring applies.

---

## Iteration Parameters

These parameters can be adjusted to tune evaluation sensitivity:

### Pre-Scrape Thresholds

| Parameter | Default | Range | Effect |
|-----------|---------|-------|--------|
| `RISK_THRESHOLD_EXCLUDE` | 0.7 | 0.0-1.0 | Risk score above which URLs are excluded |
| `RISK_TAVILY_COMBINED` | 0.5 + 0.90 | - | Exclude if risk > 0.5 AND Tavily < 0.90 |
| `MIN_TAVILY_SCORE` | 0.75 | 0.0-1.0 | Minimum Tavily score for recommendation |

### Post-Scrape Thresholds

| Parameter | Default | Range | Effect |
|-----------|---------|-------|--------|
| `QUALITY_HIGH_THRESHOLD` | 7.5 | 0-10 | Score for "high" rating |
| `QUALITY_MEDIUM_THRESHOLD` | 5.0 | 0-10 | Score for "medium" rating |
| `QUALITY_LOW_THRESHOLD` | 3.0 | 0-10 | Score for "low" rating |
| `MIN_WORD_COUNT` | 300 | 0-10000 | Minimum words for valid content |
| `MIN_UNIQUE_RATIO` | 0.40 | 0.0-1.0 | Minimum unique content ratio |
| `MIN_KEYWORD_FREQUENCY` | 3 | 0-100 | Minimum topic keyword occurrences |

### Weight Adjustments

| Parameter | Default | Range | Effect |
|-----------|---------|-------|--------|
| `WEIGHT_RELEVANCE` | 0.30 | 0.0-1.0 | Relevance dimension weight |
| `WEIGHT_AUTHORITY` | 0.20 | 0.0-1.0 | Authority dimension weight |
| `WEIGHT_DENSITY` | 0.25 | 0.0-1.0 | Information density weight |
| `WEIGHT_TIMELINESS` | 0.15 | 0.0-1.0 | Timeliness dimension weight |
| `WEIGHT_UNIQUENESS` | 0.10 | 0.0-1.0 | Uniqueness dimension weight |

### Iteration Guidelines

1. **Too many false positives (bad content getting through):**
   - Increase `QUALITY_HIGH_THRESHOLD` to 8.0
   - Increase `MIN_WORD_COUNT` to 500
   - Increase `MIN_UNIQUE_RATIO` to 0.50

2. **Too many false negatives (good content rejected):**
   - Decrease `QUALITY_MEDIUM_THRESHOLD` to 4.5
   - Decrease `MIN_WORD_COUNT` to 200
   - Increase `WEIGHT_RELEVANCE` to 0.35

3. **Missing niche/technical content:**
   - Decrease `MIN_KEYWORD_FREQUENCY` to 2
   - Increase `WEIGHT_AUTHORITY` to 0.25
   - Increase `WEIGHT_UNIQUENESS` to 0.15

4. **Too much marketing content:**
   - Increase `WEIGHT_DENSITY` to 0.30
   - Increase `MIN_UNIQUE_RATIO` to 0.60
   - Add marketing keywords to negative filter

---

## Workflow Integration

```
Research Workflow:
1. Execute Tavily searches
2. [PRE-SCRAPE] Assess sources → Get recommended URLs
3. Scrape recommended URLs with Firecrawl
4. [POST-SCRAPE] Validate each scraped file
5. Categorize: high/medium/low/failed
6. Quality Gate Check
7. If insufficient sources → Retry loop
8. Synthesize only validated content
```

## Common Patterns

**404 Error Page Detection:**
- Look for: "404 Not Found", "nginx/", "Apache/" error indicators
- Even short content can be a valid error page
- Discard immediately

**Marketing Content Detection:**
- High word count but low substance
- Product specs without analysis
- Heavy on features, light on insights
- Usually scores low on Information Density

**High-Value Content Indicators:**
- Original research or expert insights
- Comprehensive coverage of topic
- Low noise-to-signal ratio
- Authoritative source
