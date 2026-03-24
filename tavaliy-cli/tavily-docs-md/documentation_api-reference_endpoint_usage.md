Title: Usage - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/endpoint/usage
Description: Get API key and account usage details

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/endpoint/usage#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

API Reference

Usage

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

Get API key and account usage details

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.tavily.com/usage \
  --header 'Authorization: Bearer <token>'
```

200

401

429

Copy

Ask AI

```
{
  "key": {
    "usage": 150,
    "limit": 1000,
    "search_usage": 100,
    "extract_usage": 25,
    "crawl_usage": 15,
    "map_usage": 7,
    "research_usage": 3
  },
  "account": {
    "current_plan": "Bootstrap",
    "plan_usage": 500,
    "plan_limit": 15000,
    "paygo_usage": 25,
    "paygo_limit": 100,
    "search_usage": 350,
    "extract_usage": 75,
    "crawl_usage": 50,
    "map_usage": 15,
    "research_usage": 10
  }
}
```

GET

/

usage

Get API key and account usage details

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://api.tavily.com/usage \
  --header 'Authorization: Bearer <token>'
```

200

401

429

Copy

Ask AI

```
{
  "key": {
    "usage": 150,
    "limit": 1000,
    "search_usage": 100,
    "extract_usage": 25,
    "crawl_usage": 15,
    "map_usage": 7,
    "research_usage": 3
  },
  "account": {
    "current_plan": "Bootstrap",
    "plan_usage": 500,
    "plan_limit": 15000,
    "paygo_usage": 25,
    "paygo_limit": 100,
    "search_usage": 350,
    "extract_usage": 75,
    "crawl_usage": 50,
    "map_usage": 15,
    "research_usage": 10
  }
}
```

#### Authorizations

[​](https://docs.tavily.com/documentation/api-reference/endpoint/usage#authorization-authorization)

Authorization

string

header

required

Bearer authentication header in the form Bearer , where  is your Tavily API key (e.g., Bearer tvly-YOUR\_API\_KEY).

#### Response

200

application/json

Usage details returned successfully

[​](https://docs.tavily.com/documentation/api-reference/endpoint/usage#response-key)

key

object

Showchild attributes

[​](https://docs.tavily.com/documentation/api-reference/endpoint/usage#response-account)

account

object

Account plan and usage information

Showchild attributes

[Streaming\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming) [Quickstart\\
\\
Next](https://docs.tavily.com/sdk/python/quick-start)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.