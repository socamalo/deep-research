Title: Get Research Task Status - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/endpoint/research-get
Description: Retrieve the status and results of a research task using its request ID.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Research

Get Research Task Status

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

  - [POST\\
    \\
    Create Research Task](https://docs.tavily.com/documentation/api-reference/endpoint/research)
  - [GET\\
    \\
    Get Research Task Status](https://docs.tavily.com/documentation/api-reference/endpoint/research-get)
  - [Streaming](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming)
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

Python SDK

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.get_research("123e4567-e89b-12d3-a456-426614174111")

print(response)
```

200

202

401

404

500

Copy

Ask AI

```
{
  "request_id": "123e4567-e89b-12d3-a456-426614174111",
  "created_at": "2025-01-15T10:30:00Z",
  "status": "completed",
  "content": "Research Report: Latest Developments in AI\n\n## Executive Summary\n\nArtificial Intelligence has seen significant advancements in recent months, with major breakthroughs in large language models, multimodal AI systems, and real-world applications...",
  "sources": [\
    {\
      "title": "Latest AI Developments",\
      "url": "https://example.com/ai-news",\
      "favicon": "https://example.com/favicon.ico"\
    },\
    {\
      "title": "AI Research Breakthroughs",\
      "url": "https://example.com/ai-research",\
      "favicon": "https://example.com/favicon.ico"\
    }\
  ],
  "response_time": 1.23
}
```

GET

/

research

/

{request\_id}

Python SDK

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.get_research("123e4567-e89b-12d3-a456-426614174111")

print(response)
```

200

202

401

404

500

Copy

Ask AI

```
{
  "request_id": "123e4567-e89b-12d3-a456-426614174111",
  "created_at": "2025-01-15T10:30:00Z",
  "status": "completed",
  "content": "Research Report: Latest Developments in AI\n\n## Executive Summary\n\nArtificial Intelligence has seen significant advancements in recent months, with major breakthroughs in large language models, multimodal AI systems, and real-world applications...",
  "sources": [\
    {\
      "title": "Latest AI Developments",\
      "url": "https://example.com/ai-news",\
      "favicon": "https://example.com/favicon.ico"\
    },\
    {\
      "title": "AI Research Breakthroughs",\
      "url": "https://example.com/ai-research",\
      "favicon": "https://example.com/favicon.ico"\
    }\
  ],
  "response_time": 1.23
}
```

#### Authorizations

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#authorization-authorization)

Authorization

string

header

required

Bearer authentication header in the form Bearer , where  is your Tavily API key (e.g., Bearer tvly-YOUR\_API\_KEY).

#### Path Parameters

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#parameter-request-id)

request\_id

string

required

The unique identifier of the research task.

#### Response

200

application/json

Research task is completed or failed.

- Completed

- Failed


[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#response-one-of-0-request-id)

request\_id

string

required

The unique identifier of the research task.

Example:

`"123e4567-e89b-12d3-a456-426614174111"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#response-one-of-0-created-at)

created\_at

string

required

Timestamp when the research task was created.

Example:

`"2025-01-15T10:30:00Z"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#response-one-of-0-status)

status

enum<string>

required

The current status of the research task.

Available options:

`completed`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#response-one-of-0-content-one-of-0)

content

stringobjectstringobject

required

The research report content. Can be a string or a structured object if output\_schema was provided.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#response-one-of-0-sources)

sources

object\[\]

required

List of sources used in the research.

Showchild attributes

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research-get#response-one-of-0-response-time)

response\_time

integer

required

Time in seconds it took to complete the request.

Example:

`1.23`

[Create Research Task\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/research) [Streaming\\
\\
Next](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.