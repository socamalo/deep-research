Title: Tavily Extract - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/endpoint/extract
Description: Extract web page content from one or more specified URLs using Tavily Extract.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/endpoint/extract#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

API Reference

Tavily Extract

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
response = tavily_client.extract("https://en.wikipedia.org/wiki/Artificial_intelligence")

print(response)
```

200

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
  "results": [\
    {\
      "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",\
      "raw_content": "\"Jump to content\\nMain menu\\nSearch\\nAppearance\\nDonate\\nCreate account\\nLog in\\nPersonal tools\\n        Photograph your local culture, help Wikipedia and win!\\nToggle the table of contents\\nArtificial intelligence\\n161 languages\\nArticle\\nTalk\\nRead\\nView source\\nView history\\nTools\\nFrom Wikipedia, the free encyclopedia\\n\\\"AI\\\" redirects here. For other uses, see AI (disambiguation) and Artificial intelligence (disambiguation).\\nPart of a series on\\nArtificial intelligence (AI)\\nshow\\nMajor goals\\nshow\\nApproaches\\nshow\\nApplications\\nshow\\nPhilosophy\\nshow\\nHistory\\nshow\\nGlossary\\nvte\\nArtificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, particularly computer systems. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.[1] Such machines may be called AIs.\\nHigh-profile applications of AI include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); virtual assistants (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., ChatGPT and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go)...................",\
      "images": [],\
      "favicon": "https://en.wikipedia.org/static/favicon/wikipedia.ico"\
    }\
  ],
  "failed_results": [],
  "response_time": 0.02,
  "usage": {
    "credits": 1
  },
  "request_id": "123e4567-e89b-12d3-a456-426614174111"
}
```

POST

/

extract

Python SDK

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.extract("https://en.wikipedia.org/wiki/Artificial_intelligence")

print(response)
```

200

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
  "results": [\
    {\
      "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",\
      "raw_content": "\"Jump to content\\nMain menu\\nSearch\\nAppearance\\nDonate\\nCreate account\\nLog in\\nPersonal tools\\n        Photograph your local culture, help Wikipedia and win!\\nToggle the table of contents\\nArtificial intelligence\\n161 languages\\nArticle\\nTalk\\nRead\\nView source\\nView history\\nTools\\nFrom Wikipedia, the free encyclopedia\\n\\\"AI\\\" redirects here. For other uses, see AI (disambiguation) and Artificial intelligence (disambiguation).\\nPart of a series on\\nArtificial intelligence (AI)\\nshow\\nMajor goals\\nshow\\nApproaches\\nshow\\nApplications\\nshow\\nPhilosophy\\nshow\\nHistory\\nshow\\nGlossary\\nvte\\nArtificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, particularly computer systems. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.[1] Such machines may be called AIs.\\nHigh-profile applications of AI include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); virtual assistants (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., ChatGPT and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go)...................",\
      "images": [],\
      "favicon": "https://en.wikipedia.org/static/favicon/wikipedia.ico"\
    }\
  ],
  "failed_results": [],
  "response_time": 0.02,
  "usage": {
    "credits": 1
  },
  "request_id": "123e4567-e89b-12d3-a456-426614174111"
}
```

#### Authorizations

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#authorization-authorization)

Authorization

string

header

required

Bearer authentication header in the form Bearer , where  is your Tavily API key (e.g., Bearer tvly-YOUR\_API\_KEY).

#### Body

application/json

Parameters for the Tavily Extract request.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-urls-one-of-0)

urls

stringstring\[\]stringstring\[\]

required

The URL to extract content from.

Example:

`"https://en.wikipedia.org/wiki/Artificial_intelligence"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-query)

query

string

User intent for reranking extracted content chunks. When provided, chunks are reranked based on relevance to this query.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-chunks-per-source)

chunks\_per\_source

integer

default:3

Chunks are short content snippets (maximum 500 characters each) pulled directly from the source. Use `chunks_per_source` to define the maximum number of relevant chunks returned per source and to control the `raw_content` length. Chunks will appear in the `raw_content` field as: `<chunk 1> [...] <chunk 2> [...] <chunk 3>`. Available only when `query` is provided. Must be between 1 and 5.

Required range: `1 <= x <= 5`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-extract-depth)

extract\_depth

enum<string>

default:basic

The depth of the extraction process. `advanced` extraction retrieves more data, including tables and embedded content, with higher success but may increase latency.`basic` extraction costs 1 credit per 5 successful URL extractions, while `advanced` extraction costs 2 credits per 5 successful URL extractions.

Available options:

`basic`,

`advanced`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-include-images)

include\_images

boolean

default:false

Include a list of images extracted from the URLs in the response. Default is false.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-include-favicon)

include\_favicon

boolean

default:false

Whether to include the favicon URL for each result.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-format)

format

enum<string>

default:markdown

The format of the extracted web page content. `markdown` returns content in markdown format. `text` returns plain text and may increase latency.

Available options:

`markdown`,

`text`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-timeout)

timeout

number<float>

default:None

Maximum time in seconds to wait for the URL extraction before timing out. Must be between 1.0 and 60.0 seconds. If not specified, default timeouts are applied based on extract\_depth: 10 seconds for basic extraction and 30 seconds for advanced extraction.

Required range: `1 <= x <= 60`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#body-include-usage)

include\_usage

boolean

default:false

Whether to include credit usage information in the response. `NOTE:`The value may be 0 if the total successful URL extractions has not yet reached 5 calls. See our [Credits & Pricing documentation](https://docs.tavily.com/documentation/api-credits) for details.

#### Response

200

application/json

Extraction results returned successfully

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#response-results)

results

object\[\]

A list of extracted content from the provided URLs.

Showchild attributes

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#response-failed-results)

failed\_results

object\[\]

A list of URLs that could not be processed.

Showchild attributes

Example:

```
[]
```

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#response-response-time)

response\_time

number<float>

Time in seconds it took to complete the request.

Example:

`0.02`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#response-usage)

usage

object

Credit usage details for the request.

Example:

```
{ "credits": 1 }
```

[​](https://docs.tavily.com/documentation/api-reference/endpoint/extract#response-request-id)

request\_id

string

A unique request identifier you can share with customer support to help resolve issues with specific requests.

Example:

`"123e4567-e89b-12d3-a456-426614174111"`

[Tavily Search\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/search) [Tavily Crawl\\
\\
Next](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.