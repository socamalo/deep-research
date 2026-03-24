Title: Best Practices for Crawl - Tavily Docs
URL: https://docs.tavily.com/documentation/best-practices/best-practices-crawl
Description: Learn how to optimize crawl parameters, focus your crawls, and efficiently extract content from websites.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Best Practices

Best Practices for Crawl

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### API Reference

- [Introduction](https://docs.tavily.com/documentation/api-reference/introduction)
- [POST\\
\\
Search](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [POST\\
\\
Extract](https://docs.tavily.com/documentation/api-reference/endpoint/extract)
- [POST\\
\\
Crawl](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)
- [POST\\
\\
Map](https://docs.tavily.com/documentation/api-reference/endpoint/map)
- Research

- [GET\\
\\
Usage](https://docs.tavily.com/documentation/api-reference/endpoint/usage)

##### Python SDK

- [Quickstart](https://docs.tavily.com/sdk/python/quick-start)
- [SDK Reference](https://docs.tavily.com/sdk/python/reference)

##### JavaScript SDK

- [Quickstart](https://docs.tavily.com/sdk/javascript/quick-start)
- [SDK Reference](https://docs.tavily.com/sdk/javascript/reference)

##### Best Practices

- [Search](https://docs.tavily.com/documentation/best-practices/best-practices-search)
- [Extract](https://docs.tavily.com/documentation/best-practices/best-practices-extract)
- [Crawl](https://docs.tavily.com/documentation/best-practices/best-practices-crawl)
- [Research](https://docs.tavily.com/documentation/best-practices/best-practices-research)
- [API Key Management](https://docs.tavily.com/documentation/best-practices/api-key-management)

On this page

- [Crawl vs Map](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#crawl-vs-map)
- [Use Crawl when you need:](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#use-crawl-when-you-need)
- [Use Map when you need:](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#use-map-when-you-need)
- [Crawl Parameters](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#crawl-parameters)
- [Instructions](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#instructions)
- [Chunks per Source](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#chunks-per-source)
- [Depth and breadth](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#depth-and-breadth)
- [Filtering and Focusing](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#filtering-and-focusing)
- [Path patterns](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#path-patterns)
- [Domain filtering](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#domain-filtering)
- [Extract depth](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#extract-depth)
- [Use Cases](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#use-cases)
- [1\. Deep or Unlinked Content](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#1-deep-or-unlinked-content)
- [2\. Structured but Nonstandard Layouts](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#2-structured-but-nonstandard-layouts)
- [3\. Multi-modal Information Needs](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#3-multi-modal-information-needs)
- [4\. Rapidly Changing Content](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#4-rapidly-changing-content)
- [5\. Behind Auth / Paywalls](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#5-behind-auth-%2F-paywalls)
- [6\. Complete Coverage / Auditing](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#6-complete-coverage-%2F-auditing)
- [7\. Semantic Search or RAG Integration](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#7-semantic-search-or-rag-integration)
- [8\. Known URL Patterns](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#8-known-url-patterns)
- [Performance Optimization](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#performance-optimization)
- [Depth vs. Performance](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#depth-vs-performance)
- [Rate Limiting](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#rate-limiting)
- [Integration with Map](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#integration-with-map)
- [Common Pitfalls](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#common-pitfalls)
- [Excessive depth](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#excessive-depth)
- [Unfocused crawling](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#unfocused-crawling)
- [Missing limits](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#missing-limits)
- [Ignoring failed results](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#ignoring-failed-results)
- [Summary](https://docs.tavily.com/documentation/best-practices/best-practices-crawl#summary)

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#crawl-vs-map)  Crawl vs Map

Understanding when to use each API:

| Feature | Crawl | Map |
| --- | --- | --- |
| **Content extraction** | Full content | URLs only |
| **Use case** | Deep content analysis | Site structure discovery |
| **Speed** | Slower (extracts content) | Faster (URLs only) |
| **Best for** | RAG, analysis, documentation | Sitemap generation |

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#use-crawl-when-you-need)  Use Crawl when you need:

- Full content extraction from pages
- Deep content analysis
- Processing of paginated or nested content
- Extraction of specific content patterns
- Integration with RAG systems

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#use-map-when-you-need)  Use Map when you need:

- Quick site structure discovery
- URL collection without content extraction
- Sitemap generation
- Path pattern matching
- Domain structure analysis

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#crawl-parameters)  Crawl Parameters

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#instructions)  Instructions

Guide the crawl with natural language to focus on relevant content:

Copy

Ask AI

```
{
  "url": "example.com",
  "max_depth": 2,
  "instructions": "Find all documentation pages about Python"
}
```

**When to use instructions:**

- To focus crawling on specific topics or content types
- When you need semantic filtering of pages
- For agentic use cases where relevance is critical

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#chunks-per-source)  Chunks per Source

Control the amount of content returned per page to prevent context window explosion:

Copy

Ask AI

```
{
  "url": "example.com",
  "instructions": "Find all documentation about authentication",
  "chunks_per_source": 3
}
```

**Key benefits:**

- Returns only relevant content snippets (max 500 characters each) instead of full page content
- Prevents context window from exploding in agentic use cases
- Chunks appear in `raw_content` as: `<chunk 1> [...] <chunk 2> [...] <chunk 3>`

> `chunks_per_source` is only available when instructions are provided.

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#depth-and-breadth)  Depth and breadth

| Parameter | Description | Impact |
| --- | --- | --- |
| `max_depth` | How many levels deep to crawl from starting URL | Exponential latency growth |
| `max_breadth` | Maximum links to follow per page | Horizontal spread |
| `limit` | Total maximum pages to crawl | Hard cap on pages |

**Performance tip:** Each level of depth increases crawl time exponentially. Start with `max_depth=1` and increase as needed.

Copy

Ask AI

```
// Conservative crawl
{
  "url": "example.com",
  "max_depth": 1,
  "max_breadth": 20,
  "limit": 20
}

// Comprehensive crawl
{
  "url": "example.com",
  "max_depth": 3,
  "max_breadth": 100,
  "limit": 500
}
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#filtering-and-focusing)  Filtering and Focusing

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#path-patterns)  Path patterns

Use regex patterns to include or exclude specific paths:

Copy

Ask AI

```
// Target specific sections
{
  "url": "example.com",
  "select_paths": ["/blog/.*", "/docs/.*", "/guides/.*"],
  "exclude_paths": ["/private/.*", "/admin/.*", "/test/.*"]
}

// Paginated content
{
  "url": "example.com/blog",
  "max_depth": 2,
  "select_paths": ["/blog/.*", "/blog/page/.*"],
  "exclude_paths": ["/blog/tag/.*"]
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#domain-filtering)  Domain filtering

Control which domains to crawl:

Copy

Ask AI

```
// Stay within subdomain
{
  "url": "docs.example.com",
  "select_domains": ["^docs.example.com$"],
  "max_depth": 2
}

// Exclude specific domains
{
  "url": "example.com",
  "exclude_domains": ["^ads.example.com$", "^tracking.example.com$"],
  "max_depth": 2
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#extract-depth)  Extract depth

Controls extraction quality vs. speed.

| Depth | When to use |
| --- | --- |
| `basic` (default) | Simple content, faster processing |
| `advanced` | Complex pages, tables, structured data |

Copy

Ask AI

```
{
  "url": "docs.example.com",
  "max_depth": 2,
  "extract_depth": "advanced",
  "select_paths": ["/docs/.*"]
}
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#use-cases)  Use Cases

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#1-deep-or-unlinked-content)  1\. Deep or Unlinked Content

Many sites have content that’s difficult to access through standard means:

- Deeply nested pages not in main navigation
- Paginated archives (old blog posts, changelogs)
- Internal search-only content

**Best Practice:**

Copy

Ask AI

```
{
  "url": "example.com",
  "max_depth": 3,
  "max_breadth": 50,
  "limit": 200,
  "select_paths": ["/blog/.*", "/changelog/.*"],
  "exclude_paths": ["/private/.*", "/admin/.*"]
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#2-structured-but-nonstandard-layouts)  2\. Structured but Nonstandard Layouts

For content that’s structured but not marked up in schema.org:

- Documentation
- Changelogs
- FAQs

**Best Practice:**

Copy

Ask AI

```
{
  "url": "docs.example.com",
  "max_depth": 2,
  "extract_depth": "advanced",
  "select_paths": ["/docs/.*"]
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#3-multi-modal-information-needs)  3\. Multi-modal Information Needs

When you need to combine information from multiple sections:

- Cross-referencing content
- Finding related information
- Building comprehensive knowledge bases

**Best Practice:**

Copy

Ask AI

```
{
  "url": "example.com",
  "max_depth": 2,
  "instructions": "Find all documentation pages that link to API reference docs",
  "extract_depth": "advanced"
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#4-rapidly-changing-content)  4\. Rapidly Changing Content

For content that updates frequently:

- API documentation
- Product announcements
- News sections

**Best Practice:**

Copy

Ask AI

```
{
  "url": "api.example.com",
  "max_depth": 1,
  "max_breadth": 100
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#5-behind-auth-/-paywalls)  5\. Behind Auth / Paywalls

For content requiring authentication:

- Internal knowledge bases
- Customer help centers
- Gated documentation

**Best Practice:**

Copy

Ask AI

```
{
  "url": "help.example.com",
  "max_depth": 2,
  "select_domains": ["^help.example.com$"],
  "exclude_domains": ["^public.example.com$"]
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#6-complete-coverage-/-auditing)  6\. Complete Coverage / Auditing

For comprehensive content analysis:

- Legal compliance checks
- Security audits
- Policy verification

**Best Practice:**

Copy

Ask AI

```
{
  "url": "example.com",
  "max_depth": 3,
  "max_breadth": 100,
  "limit": 1000,
  "extract_depth": "advanced",
  "instructions": "Find all mentions of GDPR and data protection policies"
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#7-semantic-search-or-rag-integration)  7\. Semantic Search or RAG Integration

For feeding content into LLMs or search systems:

- RAG systems
- Enterprise search
- Knowledge bases

**Best Practice:**

Copy

Ask AI

```
{
  "url": "docs.example.com",
  "max_depth": 2,
  "extract_depth": "advanced",
  "include_images": true
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#8-known-url-patterns)  8\. Known URL Patterns

When you have specific paths to crawl:

- Sitemap-based crawling
- Section-specific extraction
- Pattern-based content collection

**Best Practice:**

Copy

Ask AI

```
{
  "url": "example.com",
  "max_depth": 1,
  "select_paths": ["/docs/.*", "/api/.*", "/guides/.*"],
  "exclude_paths": ["/private/.*", "/admin/.*"]
}
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#performance-optimization)  Performance Optimization

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#depth-vs-performance)  Depth vs. Performance

- Each level of depth increases crawl time exponentially
- Start with max\_depth: 1 and increase as needed
- Use max\_breadth to control horizontal expansion
- Set appropriate limit to prevent excessive crawling

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#rate-limiting)  Rate Limiting

- Respect site’s robots.txt
- Implement appropriate delays between requests
- Monitor API usage and limits
- Use appropriate error handling for rate limits

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#integration-with-map)  Integration with Map

Consider using Map before Crawl to:

1. Discover site structure
2. Identify relevant paths
3. Plan crawl strategy
4. Validate URL patterns

**Example workflow:**

1. Use Map to get site structure
2. Analyze paths and patterns
3. Configure Crawl with discovered paths
4. Execute focused crawl

**Benefits:**

- Discover site structure before crawling
- Identify relevant path patterns
- Avoid unnecessary crawling
- Validate URL patterns work correctly

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#common-pitfalls)  Common Pitfalls

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#excessive-depth)  Excessive depth

- **Problem:** Setting `max_depth=4` or higher
- **Impact:** Exponential crawl time, unnecessary pages
- **Solution:** Start with 1-2 levels, increase only if needed

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#unfocused-crawling)  Unfocused crawling

- **Problem:** No `instructions` provided, crawling entire site
- **Impact:** Wasted resources, irrelevant content, context explosion
- **Solution:** Use instructions to focus the crawl semantically

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#missing-limits)  Missing limits

- **Problem:** No `limit` parameter set
- **Impact:** Runaway crawls, unexpected costs
- **Solution:** Always set a reasonable `limit` value

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#ignoring-failed-results)  Ignoring failed results

- **Problem:** Not checking which pages failed extraction
- **Impact:** Incomplete data, missed content
- **Solution:** Monitor failed results and adjust parameters

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-crawl\#summary)  Summary

- Use instructions and chunks\_per\_source for focused, relevant results in agentic use cases
- Start with conservative parameters (`max_depth=1, max_breadth=20`)
- Use path patterns to focus crawling on relevant content
- Choose appropriate extract\_depth based on content complexity
- Set reasonable limits to prevent excessive crawling
- Monitor failed results and adjust patterns accordingly
- Use Map first to understand site structure
- Implement error handling for rate limits and failures
- Respect robots.txt and site policies
- Optimize for your use case (speed vs. completeness)
- Process results incrementally rather than waiting for full crawl

> Crawling is powerful but resource-intensive. Focus your crawls, start small, monitor results, and scale gradually based on actual needs.

[Best Practices for Extract\\
\\
Previous](https://docs.tavily.com/documentation/best-practices/best-practices-extract) [Best Practices for Research\\
\\
Next](https://docs.tavily.com/documentation/best-practices/best-practices-research)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.