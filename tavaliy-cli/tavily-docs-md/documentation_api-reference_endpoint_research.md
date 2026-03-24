Title: Create Research Task - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/endpoint/research
Description: Tavily Research performs comprehensive research on a given topic by conducting multiple searches, analyzing sources, and generating a detailed research report.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/endpoint/research#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Research

Create Research Task

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
response = tavily_client.research("What are the latest developments in AI?")

print(response)
```

201

400

401

429

432

433

500

Copy

Ask AI

```
{
  "request_id": "123e4567-e89b-12d3-a456-426614174111",
  "created_at": "2025-01-15T10:30:00Z",
  "status": "pending",
  "input": "What are the latest developments in AI?",
  "model": "mini",
  "response_time": 1.23
}
```

POST

/

research

Python SDK

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.research("What are the latest developments in AI?")

print(response)
```

201

400

401

429

432

433

500

Copy

Ask AI

```
{
  "request_id": "123e4567-e89b-12d3-a456-426614174111",
  "created_at": "2025-01-15T10:30:00Z",
  "status": "pending",
  "input": "What are the latest developments in AI?",
  "model": "mini",
  "response_time": 1.23
}
```

#### Authorizations

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#authorization-authorization)

Authorization

string

header

required

Bearer authentication header in the form Bearer , where  is your Tavily API key (e.g., Bearer tvly-YOUR\_API\_KEY).

#### Body

application/json

Parameters for the Tavily Research request.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#body-input)

input

string

required

The research task or question to investigate.

Example:

`"What are the latest developments in AI?"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#body-model)

model

enum<string>

default:auto

The model used by the research agent. "mini" is optimized for targeted, efficient research and works best for narrow or well-scoped questions. "pro" provides comprehensive, multi-angle research and is suited for complex topics that span multiple subtopics or domains

Available options:

`mini`,

`pro`,

`auto`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#body-stream)

stream

boolean

default:false

Whether to stream the research results as they are generated. When 'true', returns a Server-Sent Events (SSE) stream. See [Streaming documentation](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming) for details.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#body-output-schema)

output\_schema

object

A JSON Schema object that defines the structure of the research output. When provided, the research response will be structured to match this schema, ensuring a predictable and validated output shape. Must include a 'properties' field, and may optionally include 'required' field.

Showchild attributes

Example:

```
{
  "properties": {
    "company": {
      "type": "string",
      "description": "The name of the company"
    },
    "key_metrics": {
      "type": "array",
      "description": "List of key performance metrics",
      "items": { "type": "string" }
    },
    "financial_details": {
      "type": "object",
      "description": "Detailed financial breakdown",
      "properties": {
        "operating_income": {
          "type": "number",
          "description": "Operating income for the period"
        }
      }
    }
  },
  "required": ["company"]
}
```

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#body-citation-format)

citation\_format

enum<string>

default:numbered

The format for citations in the research report.

Available options:

`numbered`,

`mla`,

`apa`,

`chicago`

#### Response

201

application/json

Research task queued successfully (when not streaming)

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#response-request-id)

request\_id

string

required

A unique identifier for the research task.

Example:

`"123e4567-e89b-12d3-a456-426614174111"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#response-created-at)

created\_at

string

required

Timestamp when the research task was created.

Example:

`"2025-01-15T10:30:00Z"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#response-status)

status

string

required

The current status of the research task.

Example:

`"pending"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#response-input)

input

string

required

The research task or question investigated.

Example:

`"What are the latest developments in AI?"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#response-model)

model

string

required

The model used by the research agent.

Example:

`"mini"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/research#response-response-time)

response\_time

integer

required

Time in seconds it took to complete the request.

Example:

`1.23`

[Tavily Map\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/map) [Get Research Task Status\\
\\
Next](https://docs.tavily.com/documentation/api-reference/endpoint/research-get)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.