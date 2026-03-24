Title: Introduction - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/introduction
Description: Easily integrate our APIs with your services.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/introduction#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

API Reference

Introduction

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

- [Base URL](https://docs.tavily.com/documentation/api-reference/introduction#base-url)
- [Authentication](https://docs.tavily.com/documentation/api-reference/introduction#authentication)
- [Endpoints](https://docs.tavily.com/documentation/api-reference/introduction#endpoints)
- [Project Tracking](https://docs.tavily.com/documentation/api-reference/introduction#project-tracking)

## [​](https://docs.tavily.com/documentation/api-reference/introduction\#base-url)  Base URL

The base URL for all requests to the Tavily API is:

Copy

Ask AI

```
https://api.tavily.com
```

## [​](https://docs.tavily.com/documentation/api-reference/introduction\#authentication)  Authentication

All Tavily endpoints are authenticated using API keys.
[Get your free API key](https://app.tavily.com/).

Copy

Ask AI

```
curl -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer tvly-YOUR_API_KEY" \
  -d '{"query": "Who is Leo Messi?"}'
```

## [​](https://docs.tavily.com/documentation/api-reference/introduction\#endpoints)  Endpoints

[**`/search`**Tavily’s powerful web search API.](https://docs.tavily.com/documentation/api-reference/endpoint/search) [**`/extract`**Tavily’s powerful content extraction API.](https://docs.tavily.com/documentation/api-reference/endpoint/extract) [`/crawl` , `/map`Tavily’s intelligent sitegraph navigation and extraction tools.](https://docs.tavily.com/documentation/api-reference/endpoint/crawl) [**`/research`**Tavily’s comprehensive research API for in-depth analysis.](https://docs.tavily.com/documentation/api-reference/endpoint/research)

## [​](https://docs.tavily.com/documentation/api-reference/introduction\#project-tracking)  Project Tracking

You can optionally attach a Project ID to your API requests to organize and track usage by project. This is useful when a single API key is used across multiple projects or applications.To attach a project to your request, add the `X-Project-ID` header:

Copy

Ask AI

```
curl -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer tvly-YOUR_API_KEY" \
  -H "X-Project-ID: your-project-id" \
  -d '{"query": "Who is Leo Messi?"}'
```

**Key features:**

- An API key can be associated with multiple projects
- Filter requests by project in the [/logs endpoint](https://docs.tavily.com/documentation/api-reference/endpoint/usage) and platform usage dashboard
- Helps organize and track where requests originate from

When using the SDKs, you can specify a project using the `project_id`
parameter when instantiating the client, or by setting the `TAVILY_PROJECT`
environment variable.

[Tavily Search\\
\\
Next](https://docs.tavily.com/documentation/api-reference/endpoint/search)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.