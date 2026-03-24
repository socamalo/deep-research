Title: Tavily Map - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/endpoint/map
Description: Tavily Map traverses websites like a graph and can explore hundreds of paths in parallel with intelligent discovery to generate comprehensive site maps.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/endpoint/map#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

API Reference

Tavily Map

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

Python SDK

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.map("https://docs.tavily.com")

print(response)
```

200

400

401

403

429

432

433

500

Copy

Ask AI

```
{
  "base_url": "docs.tavily.com",
  "results": [\
    "https://docs.tavily.com/welcome",\
    "https://docs.tavily.com/documentation/api-credits",\
    "https://docs.tavily.com/documentation/about"\
  ],
  "response_time": 1.23,
  "usage": {
    "credits": 1
  },
  "request_id": "123e4567-e89b-12d3-a456-426614174111"
}
```

POST

/

map

Python SDK

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.map("https://docs.tavily.com")

print(response)
```

200

400

401

403

429

432

433

500

Copy

Ask AI

```
{
  "base_url": "docs.tavily.com",
  "results": [\
    "https://docs.tavily.com/welcome",\
    "https://docs.tavily.com/documentation/api-credits",\
    "https://docs.tavily.com/documentation/about"\
  ],
  "response_time": 1.23,
  "usage": {
    "credits": 1
  },
  "request_id": "123e4567-e89b-12d3-a456-426614174111"
}
```

#### Authorizations

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#authorization-authorization)

Authorization

string

header

required

Bearer authentication header in the form Bearer , where  is your Tavily API key (e.g., Bearer tvly-YOUR\_API\_KEY).

#### Body

application/json

Parameters for the Tavily Map request.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-url)

url

string

required

The root URL to begin the mapping.

Example:

`"docs.tavily.com"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-instructions)

instructions

string

Natural language instructions for the crawler. When specified, the cost increases to 2 API credits per 10 successful pages instead of 1 API credit per 10 pages.

Example:

`"Find all pages about the Python SDK"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-max-depth)

max\_depth

integer

default:1

Max depth of the mapping. Defines how far from the base URL the crawler can explore.

Required range: `1 <= x <= 5`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-max-breadth)

max\_breadth

integer

default:20

Max number of links to follow per level of the tree (i.e., per page).

Required range: `1 <= x <= 500`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-limit)

limit

integer

default:50

Total number of links the crawler will process before stopping.

Required range: `x >= 1`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-select-paths)

select\_paths

string\[\]

Regex patterns to select only URLs with specific path patterns (e.g., `/docs/.*`, `/api/v1.*`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-select-domains)

select\_domains

string\[\]

Regex patterns to select crawling to specific domains or subdomains (e.g., `^docs\.example\.com$`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-exclude-paths)

exclude\_paths

string\[\]

Regex patterns to exclude URLs with specific path patterns (e.g., `/private/.*`, `/admin/.*`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-exclude-domains)

exclude\_domains

string\[\]

Regex patterns to exclude specific domains or subdomains from crawling (e.g., `^private\.example\.com$`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-allow-external)

allow\_external

boolean

default:true

Whether to include external domain links in the final results list.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-timeout)

timeout

number<float>

default:150

Maximum time in seconds to wait for the map operation before timing out. Must be between 10 and 150 seconds.

Required range: `10 <= x <= 150`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#body-include-usage)

include\_usage

boolean

default:false

Whether to include credit usage information in the response.`NOTE:`The value may be 0 if the total successful pages mapped has not yet reached 10 calls. See our [Credits & Pricing documentation](https://docs.tavily.com/documentation/api-credits) for details.

#### Response

200

application/json

Map results returned successfully

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#response-base-url)

base\_url

string

The base URL that was mapped.

Example:

`"docs.tavily.com"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#response-results)

results

string\[\]

A list of URLs that were discovered during the mapping.

Example:

```
[\
  "https://docs.tavily.com/welcome",\
  "https://docs.tavily.com/documentation/api-credits",\
  "https://docs.tavily.com/documentation/about"\
]
```

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#response-response-time)

response\_time

number<float>

Time in seconds it took to complete the request.

Example:

`1.23`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#response-usage)

usage

object

Credit usage details for the request.

Example:

```
{ "credits": 1 }
```

[​](https://docs.tavily.com/documentation/api-reference/endpoint/map#response-request-id)

request\_id

string

A unique request identifier you can share with customer support to help resolve issues with specific requests.

Example:

`"123e4567-e89b-12d3-a456-426614174111"`

[Tavily Crawl\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/crawl) [Create Research Task\\
\\
Next](https://docs.tavily.com/documentation/api-reference/endpoint/research)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.