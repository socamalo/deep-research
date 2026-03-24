Title: Best Practices for Extract - Tavily Docs
URL: https://docs.tavily.com/documentation/best-practices/best-practices-extract
Description: Learn how to optimize content extraction, choose the right approach, and configure parameters for better performance.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/best-practices/best-practices-extract#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Best Practices

Best Practices for Extract

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

- [Extract Parameters](https://docs.tavily.com/documentation/best-practices/best-practices-extract#extract-parameters)
- [Query](https://docs.tavily.com/documentation/best-practices/best-practices-extract#query)
- [Chunks Per Source](https://docs.tavily.com/documentation/best-practices/best-practices-extract#chunks-per-source)
- [Extraction Approaches](https://docs.tavily.com/documentation/best-practices/best-practices-extract#extraction-approaches)
- [Search with include\_raw\_content](https://docs.tavily.com/documentation/best-practices/best-practices-extract#search-with-include_raw_content)
- [Direct Extract API](https://docs.tavily.com/documentation/best-practices/best-practices-extract#direct-extract-api)
- [Extract Depth](https://docs.tavily.com/documentation/best-practices/best-practices-extract#extract-depth)
- [Using extract\_depth=advanced](https://docs.tavily.com/documentation/best-practices/best-practices-extract#using-extract_depth%3Dadvanced)
- [Advanced Filtering Strategies](https://docs.tavily.com/documentation/best-practices/best-practices-extract#advanced-filtering-strategies)
- [Example: Score-based filtering](https://docs.tavily.com/documentation/best-practices/best-practices-extract#example-score-based-filtering)
- [Integration with Search](https://docs.tavily.com/documentation/best-practices/best-practices-extract#integration-with-search)
- [Optimal workflow](https://docs.tavily.com/documentation/best-practices/best-practices-extract#optimal-workflow)
- [Example end-to-end pipeline](https://docs.tavily.com/documentation/best-practices/best-practices-extract#example-end-to-end-pipeline)
- [Summary](https://docs.tavily.com/documentation/best-practices/best-practices-extract#summary)

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#extract-parameters)  Extract Parameters

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#query)  Query

Use query to rerank extracted content chunks based on relevance:

Copy

Ask AI

```
await tavily_client.extract(
    urls=["https://example.com/article"],
    query="machine learning applications in healthcare"
)
```

**When to use query:**

- To extract only relevant portions of long documents
- When you need focused content instead of full page extraction
- For targeted information retrieval from specific URLs

> When `query` is provided, chunks are reranked based on relevance to the query.

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#chunks-per-source)  Chunks Per Source

Control the amount of content returned per URL to prevent context window explosion:

Copy

Ask AI

```
await tavily_client.extract(
    urls=["https://example.com/article"],
    query="machine learning applications in healthcare",
    chunks_per_source=3
)
```

**Key benefits:**

- Returns only relevant content snippets (max 500 characters each) instead of full page content
- Prevents context window from exploding
- Chunks appear in `raw_content` as: `<chunk 1> [...] <chunk 2> [...] <chunk 3>`
- Must be between 1 and 5 chunks per source

> `chunks_per_source` is only available when `query` is provided.

**Example with multiple URLs:**

Copy

Ask AI

```
await tavily_client.extract(
    urls=[\
        "https://example.com/ml-healthcare",\
        "https://example.com/ai-diagnostics",\
        "https://example.com/medical-ai"\
    ],
    query="AI diagnostic tools accuracy",
    chunks_per_source=2
)
```

This returns the 2 most relevant chunks from each URL, giving you focused, relevant content without overwhelming your context window.

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#extraction-approaches)  Extraction Approaches

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#search-with-include_raw_content)  Search with include\_raw\_content

Enable include\_raw\_content=true in Search API calls to retrieve both search results and extracted content simultaneously.

Copy

Ask AI

```
response = await tavily_client.search(
    query="AI healthcare applications",
    include_raw_content=True,
    max_results=5
)
```

**When to use:**

- Quick prototyping
- Simple queries where search results are likely relevant
- Single API call convenience

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#direct-extract-api)  Direct Extract API

Use the Extract API when you want control over which specific URLs to extract from.

Copy

Ask AI

```
await tavily_client.extract(
    urls=["https://example.com/article1", "https://example.com/article2"],
    query="machine learning applications",
    chunks_per_source=3
)
```

**When to use:**

- You already have specific URLs to extract from
- You want to filter or curate URLs before extraction
- You need targeted extraction with query and chunks\_per\_source

**Key difference:** The main distinction is control, with Extract you choose exactly which URLs to extract from, while Search with `include_raw_content` extracts from all search results.

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#extract-depth)  Extract Depth

The `extract_depth` parameter controls extraction comprehensiveness:

| Depth | Use case |
| --- | --- |
| `basic` (default) | Simple text extraction, faster processing |
| `advanced` | Complex pages, tables, structured data, media |

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#using-extract_depth=advanced)  Using `extract_depth=advanced`

Best for content requiring detailed extraction:

Copy

Ask AI

```
await tavily_client.extract(
    url="https://example.com/complex-page",
    extract_depth="advanced"
)
```

**When to use advanced:**

- Dynamic content or JavaScript-rendered pages
- Tables and structured information
- Embedded media and rich content
- Higher extraction success rates needed

`extract_depth=advanced` provides better accuracy but increases latency and
cost. Use `basic` for simple content.

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#advanced-filtering-strategies)  Advanced Filtering Strategies

Beyond query-based filtering, consider these approaches for curating URLs before extraction:

| Strategy | When to use |
| --- | --- |
| Re-ranking | Use dedicated re-ranking models for precision |
| LLM-based | Let an LLM assess relevance before extraction |
| Clustering | Group similar documents, extract from clusters |
| Domain-based | Filter by trusted domains before extracting |
| Score-based | Filter search results by relevance score |

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#example-score-based-filtering)  Example: Score-based filtering

Copy

Ask AI

```
import asyncio
from tavily import AsyncTavilyClient

tavily_client = AsyncTavilyClient(api_key="tvly-YOUR_API_KEY")

async def filtered_extraction():
    # Search first
    response = await tavily_client.search(
        query="AI healthcare applications",
        search_depth="advanced",
        max_results=20
    )

    # Filter by relevance score (>0.5)
    relevant_urls = [\
        result['url'] for result in response.get('results', [])\
        if result.get('score', 0) > 0.5\
    ]

    # Extract from filtered URLs with targeted query
    extracted_data = await tavily_client.extract(
        urls=relevant_urls,
        query="machine learning diagnostic tools",
        chunks_per_source=3,
        extract_depth="advanced"
    )

    return extracted_data

asyncio.run(filtered_extraction())
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#integration-with-search)  Integration with Search

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#optimal-workflow)  Optimal workflow

- **Search** to discover relevant URLs
- **Filter** by relevance score, domain, or content snippet
- **Re-rank** if needed using specialized models
- **Extract** from top-ranked sources with query and chunks\_per\_source
- **Validate** extracted content quality
- **Process** for your RAG or AI application

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#example-end-to-end-pipeline)  Example end-to-end pipeline

Copy

Ask AI

```
async def content_pipeline(topic):
    # 1. Search with sub-queries
    queries = generate_subqueries(topic)
    responses = await asyncio.gather(
        *[tavily_client.search(**q) for q in queries]
    )

    # 2. Filter and aggregate
    urls = []
    for response in responses:
        urls.extend([\
            r['url'] for r in response['results']\
            if r['score'] > 0.5\
        ])

    # 3. Deduplicate
    urls = list(set(urls))[:20]  # Top 20 unique URLs

    # 4. Extract with error handling
    extracted = await asyncio.gather(
        *(tavily_client.extract(url, extract_depth="advanced") for url in urls),
        return_exceptions=True
    )

    # 5. Filter successful extractions
    return [e for e in extracted if not isinstance(e, Exception)]
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-extract\#summary)  Summary

1. **Use query and chunks\_per\_source** for targeted, focused extraction
2. **Choose Extract API** when you need control over which URLs to extract from
3. **Filter URLs** before extraction using scores, re-ranking, or domain trust
4. **Choose appropriate extract\_depth** based on content complexity
5. **Process URLs concurrently** with async operations for better performance
6. **Implement error handling** to manage failed extractions gracefully
7. **Validate extracted content** before downstream processing
8. **Optimize costs** by extracting only necessary content with chunks\_per\_source

> Start with query and chunks\_per\_source for targeted extraction. Filter URLs strategically, extract with appropriate depth, and handle errors gracefully for production-ready pipelines.

[Best Practices for Search\\
\\
Previous](https://docs.tavily.com/documentation/best-practices/best-practices-search) [Best Practices for Crawl\\
\\
Next](https://docs.tavily.com/documentation/best-practices/best-practices-crawl)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.