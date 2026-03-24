---
name: content-quality-validator
description: Evaluate the quality of Firecrawl scraped content to ensure it meets research standards before synthesis
---

# Content Quality Validator

## Purpose

Evaluate Firecrawl scraped markdown files to determine if they contain high-quality, relevant content suitable for research synthesis. This validator prevents 404 pages, error pages, and low-quality content from polluting the research pipeline.

## When to Use

- After EVERY Firecrawl scrape operation
- Before adding content to synthesis phase
- When deciding whether to keep or discard a scraped file
- During quality gate checks in research phases

## Evaluation Dimensions

### 1. Availability (Critical)

Check if the page was successfully scraped:
- NOT a 404/403/500 error page
- NOT an nginx/Apache error page
- NOT a "Page Not Found" or "Access Denied" page
- NOT a CAPTCHA or login wall
- NOT empty or corrupted content

**Failure indicators:**
- "404 Not Found"
- "403 Forbidden"
- "nginx/1.x.x" error headers
- "Apache Server" error pages
- "This page is no longer available"
- Content < 100 characters
- Only navigation elements, no main content

### 2. Content Relevance (High)

Assess relevance to the research topic:
- Content directly addresses the research topic
- Contains substantive information, not just mentions
- Information is on-topic and useful

**Relevance Scoring (0-10):**
- 9-10: Directly addresses core research questions
- 7-8: Highly relevant with specific information
- 5-6: Moderately relevant, some useful context
- 3-4: Tangentially related
- 1-2: Barely relevant
- 0: Completely unrelated

### 3. Content Depth (High)

Evaluate information density:
- Contains substantial text (>500 words of meaningful content)
- Includes specific data, facts, or insights
- Not just navigation menus, ads, or template text
- Has actual paragraphs of content

**Depth indicators:**
- Detailed explanations
- Data/statistics included
- Multiple sections with substance
- Authoritative analysis or reporting
- Specific examples or case studies

### 4. Source Authority (Medium)

Consider source credibility:
- Academic/institutional domains (.edu, .ac.uk, etc.)
- Recognized publications (major news, journals)
- Official documentation
- Expert blogs with credentials
- Government sources

## Quality Classifications

### High Quality
- **Criteria**: relevance_score >= 8, usable = true, word_count >= 800
- **Action**: Keep and prioritize for synthesis
- **Characteristics**: Authoritative, detailed, directly relevant

### Medium Quality
- **Criteria**: relevance_score 5-7, usable = true, word_count >= 400
- **Action**: Keep for synthesis
- **Characteristics**: Relevant with useful information, may be shorter or less comprehensive

### Low Quality
- **Criteria**: relevance_score < 5 OR word_count < 400
- **Action**: Discard unless no alternatives exist
- **Characteristics**: Thin content, off-topic, or too brief

### Failed
- **Criteria**: usable = false (404, error page, CAPTCHA, etc.)
- **Action**: Discard and trigger retry mechanism
- **Characteristics**: Not usable for research

## Output Format

```json
{
  "file": "raw-content/example-source.md",
  "url": "https://example.com/article",
  "quality": "high|medium|low|failed",
  "usable": true|false,
  "reason": "Detailed explanation of quality assessment",
  "relevance_score": 8,
  "content_type": "article|paper|blog|error_page|login_wall|other",
  "word_count": 1500,
  "is_error_page": false,
  "error_indicators": [],
  "key_insights": [
    "Key finding 1 relevant to research",
    "Key finding 2 relevant to research"
  ],
  "recommendation": "keep|discard|retry_alternative"
}
```

## Usage Instructions

### Step 1: Read the Scraped File
```bash
# Read the file that was just scraped
cat raw-content/example-source.md
```

### Step 2: Evaluate Against Criteria

Check each dimension systematically:
1. Is it an error page? (Yes → quality: failed)
2. Is it relevant to the topic? (Score 0-10)
3. Does it have enough content? (Count words)
4. Is the source credible?

### Step 3: Generate Assessment

Produce the JSON output with all fields populated.

### Step 4: Make Recommendation

- **keep**: High or medium quality content
- **discard**: Low quality that won't help synthesis
- **retry_alternative**: Failed content - needs replacement source

## Example Evaluations

### Example 1: 404 Error Page

**Input:**
```markdown
# Scraped Content

**Source**: https://example.com/deleted-article
**Scraped Date**: 2026-03-18

---

404 Not Found
The requested URL was not found on this server.
Apache/2.4.41 Server at example.com Port 80
```

**Assessment:**
```json
{
  "file": "raw-content/example-source.md",
  "url": "https://example.com/deleted-article",
  "quality": "failed",
  "usable": false,
  "reason": "Page returns 404 Not Found. Server is Apache. No usable content.",
  "relevance_score": 0,
  "content_type": "error_page",
  "word_count": 15,
  "is_error_page": true,
  "error_indicators": ["404 Not Found", "Apache Server"],
  "key_insights": [],
  "recommendation": "retry_alternative"
}
```

### Example 2: High Quality Article

**Input:**
```markdown
# Scraped Content

**Source**: https://journal.example.com/guzheng-history
**Scraped Date**: 2026-03-18

---

The History and Evolution of Guzheng Music

The guzheng, a Chinese plucked zither, has a history spanning over 2,500 years...
[1500+ words of detailed content about guzheng history, techniques, and evolution]
```

**Assessment:**
```json
{
  "file": "raw-content/journal-guzheng-history.md",
  "url": "https://journal.example.com/guzheng-history",
  "quality": "high",
  "usable": true,
  "reason": "Comprehensive historical article from academic journal. Directly addresses research topic with detailed analysis.",
  "relevance_score": 9,
  "content_type": "article",
  "word_count": 1850,
  "is_error_page": false,
  "error_indicators": [],
  "key_insights": [
    "Guzheng dates back 2,500 years to Warring States period",
    "Modern guzheng has 21 strings, evolved from 12-string version",
    "Major schools include Shandong, Henan, and Chaozhou styles"
  ],
  "recommendation": "keep"
}
```

### Example 3: Low Quality - Thin Content

**Input:**
```markdown
# Scraped Content

**Source**: https://blog.example.com/guzheng-post
**Scraped Date**: 2026-03-18

---

Home | About | Contact | Guzheng | Music | Blog

The Guzheng

The guzheng is a Chinese instrument. It sounds nice. Many people play it.

Related Posts:
- Piano for Beginners
- Guitar Chords
- Music Theory

Copyright 2026 Example Blog
```

**Assessment:**
```json
{
  "file": "raw-content/blog-guzheng-post.md",
  "url": "https://blog.example.com/guzheng-post",
  "quality": "low",
  "usable": true,
  "reason": "Content is extremely thin - only generic description with no depth. Mostly navigation and template elements.",
  "relevance_score": 4,
  "content_type": "blog",
  "word_count": 25,
  "is_error_page": false,
  "error_indicators": [],
  "key_insights": [],
  "recommendation": "discard"
}
```

## Common Error Patterns to Detect

### HTTP Error Pages
```
404 Not Found
403 Forbidden
500 Internal Server Error
502 Bad Gateway
```

### Server Software Indicators
```
nginx/1.x.x
Apache/2.x.x Server
Microsoft-IIS/10.0
```

### Generic Error Messages
```
Page Not Found
This page is unavailable
The requested URL was not found
Access Denied
You don't have permission
```

### CAPTCHA/Login Walls
```
Please verify you are human
Complete the security check
Sign in to continue
Login required
Subscribe to read
```

### Placeholder/Empty Content
```
Coming soon
Under construction
Content removed
This page intentionally left blank
```

## Integration with Research Workflow

### Phase Quality Gates

**Phase 1 (Initial Discovery):**
- Minimum: 5 high/medium quality sources
- Target: 8 sources with quality >= medium
- Ideal: 10+ diverse sources

**Phase 2 (Breadth Expansion):**
- Minimum: 8 high/medium quality sources
- Target: 12 sources with quality >= medium
- Ideal: 15+ sources covering multiple angles

**Phase 3 (Depth Exploration):**
- Minimum: 10 high/medium quality sources
- Target: 15+ authoritative sources
- Ideal: 20+ comprehensive sources across domains

**Note:** More high-quality sources lead to better synthesis. Continue searching until quality targets are met or source exhaustion is confirmed.

### Retry Trigger Conditions

Retry search if:
- Any scraped file gets "failed" quality rating
- < 50% of scraped files achieve medium+ quality
- Average word_count < 500 across all files
- Multiple files show error_indicators

### Retry Strategy

When content fails validation:

1. **Analyze failure patterns:**
   - Are URLs consistently returning 404s?
   - Are sources behind paywalls?
   - Is the search query finding wrong type of content?

2. **Design new search:**
   - Remove failed URLs from consideration
   - Adjust search terms for better specificity
   - Try different content types (add "pdf", "paper", "guide")
   - Include site restrictions for known good sources

3. **Execute retry:**
   - Run new Tavily search
   - Scrape new URLs
   - Validate new content
   - Repeat until quality gate is met

## Quality Gate Checklist

Before proceeding to synthesis, verify:

- [ ] All files evaluated with quality validator
- [ ] No "failed" quality files (either removed or replaced)
- [ ] Minimum high/medium count met for phase
- [ ] Average content depth is sufficient
- [ ] Key insights extracted from each kept file
- [ ] Failed sources have retry plan if needed

## Reporting

Document validation results in phase directory:

```markdown
# Content Quality Report - Phase X

## Summary
- Total scraped: 5
- High quality: 2
- Medium quality: 2
- Low quality: 0
- Failed: 1

## Quality Gate Status: PASSED / FAILED

## Details

### source-01-domain-com.md
- Quality: high
- Relevance: 9/10
- Word count: 1850
- Status: Kept

### source-02-broken-url.md
- Quality: failed
- Reason: 404 Not Found
- Status: Discarded, retry triggered

## Retry Actions
- Searched alternative sources for [topic]
- Found replacement: source-02-alt-domain.md (high quality)
```

## Error Log Format

Track failed URLs for pattern analysis:

```json
{
  "phase": "01-initial-discovery",
  "failed_scrapes": [
    {
      "url": "https://example.com/broken",
      "file": "source-03-broken.md",
      "error_type": "404",
      "timestamp": "2026-03-18T10:30:00Z"
    }
  ],
  "retry_attempts": 2,
  "final_quality_count": {
    "high": 3,
    "medium": 2,
    "low": 0,
    "failed": 0
  }
}
```
