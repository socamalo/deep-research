Title: Best Practices for Search - Tavily Docs
URL: https://docs.tavily.com/documentation/best-practices/best-practices-search
Description: Learn how to optimize your queries, refine search filters, and leverage advanced parameters for better performance.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/best-practices/best-practices-search#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Best Practices

Best Practices for Search

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

- [Query Optimization](https://docs.tavily.com/documentation/best-practices/best-practices-search#query-optimization)
- [Keep your query under 400 characters](https://docs.tavily.com/documentation/best-practices/best-practices-search#keep-your-query-under-400-characters)
- [Break complex queries into sub-queries](https://docs.tavily.com/documentation/best-practices/best-practices-search#break-complex-queries-into-sub-queries)
- [Search Depth](https://docs.tavily.com/documentation/best-practices/best-practices-search#search-depth)
- [Content types](https://docs.tavily.com/documentation/best-practices/best-practices-search#content-types)
- [Fast + Ultra-Fast](https://docs.tavily.com/documentation/best-practices/best-practices-search#fast-%2B-ultra-fast)
- [Using search\_depth=advanced](https://docs.tavily.com/documentation/best-practices/best-practices-search#using-search_depth%3Dadvanced)
- [Filtering Results](https://docs.tavily.com/documentation/best-practices/best-practices-search#filtering-results)
- [By date](https://docs.tavily.com/documentation/best-practices/best-practices-search#by-date)
- [By topic](https://docs.tavily.com/documentation/best-practices/best-practices-search#by-topic)
- [By domain](https://docs.tavily.com/documentation/best-practices/best-practices-search#by-domain)
- [Response Content](https://docs.tavily.com/documentation/best-practices/best-practices-search#response-content)
- [max\_results](https://docs.tavily.com/documentation/best-practices/best-practices-search#max_results)
- [include\_raw\_content](https://docs.tavily.com/documentation/best-practices/best-practices-search#include_raw_content)
- [auto\_parameters](https://docs.tavily.com/documentation/best-practices/best-practices-search#auto_parameters)
- [Exact Match](https://docs.tavily.com/documentation/best-practices/best-practices-search#exact-match)
- [Async & Performance](https://docs.tavily.com/documentation/best-practices/best-practices-search#async-%26-performance)
- [Post-Processing](https://docs.tavily.com/documentation/best-practices/best-practices-search#post-processing)
- [Using metadata](https://docs.tavily.com/documentation/best-practices/best-practices-search#using-metadata)
- [Score-based filtering](https://docs.tavily.com/documentation/best-practices/best-practices-search#score-based-filtering)
- [Regex extraction](https://docs.tavily.com/documentation/best-practices/best-practices-search#regex-extraction)

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#query-optimization)  Query Optimization

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#keep-your-query-under-400-characters)  Keep your query under 400 characters

Keep queries concise—under **400 characters**. Think of it as a query for an agent performing web search, not long-form prompts.

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#break-complex-queries-into-sub-queries)  Break complex queries into sub-queries

For complex or multi-topic queries, send separate focused requests:

Copy

Ask AI

```
// Instead of one massive query, break it down:
{ "query": "Competitors of company ABC." }
{ "query": "Financial performance of company ABC." }
{ "query": "Recent developments of company ABC." }
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#search-depth)  Search Depth

The `search_depth` parameter controls the tradeoff between latency and relevance:

Show Latency vs relevance chart

![Latency vs Relevance by Search Depth](https://mintcdn.com/tavilyai/-85Rr9EfVqo8fXvO/images/search-depth.png?fit=max&auto=format&n=-85Rr9EfVqo8fXvO&q=85&s=c57f2074dda171a1e3e9f96afbec8f10)_This chart is a heuristic and is not to scale._

| Depth | Latency | Relevance | Content Type |
| --- | --- | --- | --- |
| `ultra-fast` | Lowest | Lower | Content |
| `fast` | Low | Good | Chunks |
| `basic` | Medium | High | Content |
| `advanced` | Higher | Highest | Chunks |

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#content-types)  Content types

| Type | Description |
| --- | --- |
| **Content** | NLP-based summary of the page, providing general context |
| **Chunks** | Short snippets reranked by relevance to your search query |

Use **chunks** when you need highly targeted information aligned with your query. Use **content** when a general page summary is sufficient.

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#fast-+-ultra-fast)  Fast + Ultra-Fast

| Depth | When to use |
| --- | --- |
| `ultra-fast` | When latency is absolutely crucial. Delivers near-instant results, prioritizing speed over relevance. Ideal for real-time applications where response time is critical. |
| `fast` | When latency is more important than relevance, but you want results in reranked chunks format. Good for applications that need quick, targeted snippets. |
| `basic` | A solid balance between relevance and latency. Best for general-purpose searches where you need quality results without the overhead of advanced processing. |
| `advanced` | When you need the highest relevance and are willing to trade off latency. Best for queries seeking specific, detailed information. |

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#using-search_depth=advanced)  Using `search_depth=advanced`

Best for queries seeking specific information:

Copy

Ask AI

```
{
  "query": "How many countries use Monday.com?",
  "search_depth": "advanced",
  "chunks_per_source": 3,
  "include_raw_content": true
}
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#filtering-results)  Filtering Results

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#by-date)  By date

| Parameter | Description |
| --- | --- |
| `time_range` | Filter by relative time: `day`, `week`, `month`, `year` |
| `start_date` / `end_date` | Filter by specific date range (format: `YYYY-MM-DD`) |

Copy

Ask AI

```
{ "query": "latest ML trends", "time_range": "month" }
{ "query": "AI news", "start_date": "2025-01-01", "end_date": "2025-02-01" }
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#by-topic)  By topic

Use `topic` to filter by content type. Set to `news` for news sources (includes `published_date` metadata):

Copy

Ask AI

```
{ "query": "What happened today in NY?", "topic": "news" }
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#by-domain)  By domain

| Parameter | Description |
| --- | --- |
| `include_domains` | Limit to specific domains |
| `exclude_domains` | Filter out specific domains |
| `country` | Boost results from a specific country |

Copy

Ask AI

```
// Restrict to LinkedIn profiles
{ "query": "CEO background at Google", "include_domains": ["linkedin.com/in"] }

// Exclude irrelevant domains
{ "query": "US economy trends", "exclude_domains": ["espn.com", "vogue.com"] }

// Boost results from a country
{ "query": "tech startup funding", "country": "united states" }

// Wildcard: limit to .com, exclude specific site
{ "query": "AI news", "include_domains": ["*.com"], "exclude_domains": ["example.com"] }
```

Keep domain lists short and relevant for best results.

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#response-content)  Response Content

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#max_results)  `max_results`

Limits results returned (default: `5`). Setting too high may return lower-quality results.

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#include_raw_content)  `include_raw_content`

Returns full extracted page content. For comprehensive extraction, consider a two-step process:

1. Search to retrieve relevant URLs
2. Use [Extract API](https://docs.tavily.com/documentation/best-practices/best-practices-extract#2-two-step-process-search-then-extract) to get content

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#auto_parameters)  `auto_parameters`

Tavily automatically configures parameters based on query intent. Your explicit values override automatic ones.

Copy

Ask AI

```
{
  "query": "impact of AI in education policy",
  "auto_parameters": true,
  "search_depth": "basic" // Override to control cost
}
```

`auto_parameters` may set `search_depth` to `advanced` (2 credits). Set it
manually to control cost.

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#exact-match)  Exact Match

Use `exact_match` only when searching for a specific name or phrase that must appear verbatim in the source content. Wrap the phrase in quotes within your query:

Copy

Ask AI

```
{
  "query": "\"John Smith\" CEO Acme Corp",
  "exact_match": true
}
```

Because this narrows retrieval, it may return fewer results or empty result fields when no exact matches are found. Best suited for:

- **Due diligence** — finding information on a specific person or entity
- **Data enrichment** — retrieving details about a known company or individual
- **Legal/compliance** — locating exact names or phrases in public records

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#async-&-performance)  Async & Performance

Use async calls for concurrent requests:

Copy

Ask AI

```
import asyncio
from tavily import AsyncTavilyClient

tavily_client = AsyncTavilyClient("tvly-YOUR_API_KEY")

async def fetch_and_gather():
    queries = ["latest AI trends", "future of quantum computing"]
    responses = await asyncio.gather(
        *(tavily_client.search(q) for q in queries),
        return_exceptions=True
    )
    for response in responses:
        if isinstance(response, Exception):
            print(f"Failed: {response}")
        else:
            print(response)

asyncio.run(fetch_and_gather())
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#post-processing)  Post-Processing

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#using-metadata)  Using metadata

Leverage response metadata to refine results:

| Field | Use case |
| --- | --- |
| `score` | Filter/rank by relevance score |
| `title` | Keyword filtering on headlines |
| `content` | Quick relevance check |
| `raw_content` | Deep analysis and regex extraction |

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#score-based-filtering)  Score-based filtering

The `score` indicates relevance between query and content. Higher is better, but the ideal threshold depends on your use case.

Copy

Ask AI

```
# Filter results with score > 0.7
filtered = [r for r in results if r['score'] > 0.7]
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-search\#regex-extraction)  Regex extraction

Extract structured data from `raw_content`:

Copy

Ask AI

```
import re

# Extract location
text = "Company: Tavily, Location: New York"
match = re.search(r"Location: (\w+)", text)
location = match.group(1) if match else None  # "New York"

# Extract all emails
text = "Contact: john@example.com, support@tavily.com"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
```

[SDK Reference\\
\\
Previous](https://docs.tavily.com/sdk/javascript/reference) [Best Practices for Extract\\
\\
Next](https://docs.tavily.com/documentation/best-practices/best-practices-extract)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Latency vs Relevance by Search Depth](https://mintcdn.com/tavilyai/-85Rr9EfVqo8fXvO/images/search-depth.png?w=840&fit=max&auto=format&n=-85Rr9EfVqo8fXvO&q=85&s=138868083b0737aaa5b00f3064e7d5a8)