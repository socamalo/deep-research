Title: Quickstart - Tavily Docs
URL: https://docs.tavily.com/sdk/python/quick-start
Description: Integrate Tavily's powerful APIs natively in your Python apps.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/sdk/python/quick-start#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Python SDK

Quickstart

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

- [Introduction](https://docs.tavily.com/sdk/python/quick-start#introduction)
- [Quickstart](https://docs.tavily.com/sdk/python/quick-start#quickstart)
- [Installation](https://docs.tavily.com/sdk/python/quick-start#installation)
- [Usage](https://docs.tavily.com/sdk/python/quick-start#usage)
- [Features](https://docs.tavily.com/sdk/python/quick-start#features)

Looking for the Python SDK Reference? Head to our [Python SDK Reference](https://docs.tavily.com/sdk/python/reference) and learn how to use `tavily-python`.

## [​](https://docs.tavily.com/sdk/python/quick-start\#introduction)  Introduction

The Python SDK allows for easy interaction with the Tavily API, offering the full range of our search functionality directly from your Python programs. Easily integrate smart search capabilities into your applications, harnessing Tavily’s powerful search features.

[**GitHub**\\
\\
`/tavily-ai/tavily-python`![GitHub Repo stars](https://img.shields.io/github/stars/tavily-ai/tavily-python?style=social)](https://github.com/tavily-ai/tavily-python) [**PyPI** \\
\\
`tavily-python`![PyPI downloads](https://img.shields.io/pypi/dm/tavily-python)](https://pypi.org/project/tavily-python)

## [​](https://docs.tavily.com/sdk/python/quick-start\#quickstart)  Quickstart

Get started with our Python SDK in less than 5 minutes! [**Get your free API key** \\
\\
You get 1,000 free API Credits every month. **No credit card required.**](https://app.tavily.com/)

### [​](https://docs.tavily.com/sdk/python/quick-start\#installation)  Installation

You can install the Tavily Python SDK using the following:

Copy

Ask AI

```
pip install tavily-python
```

### [​](https://docs.tavily.com/sdk/python/quick-start\#usage)  Usage

With Tavily’s Python SDK, you can search the web in only 4 lines of code:

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.search("Who is Leo Messi?")

print(response)
```

You can also easily extract content from URLs:

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.extract("https://en.wikipedia.org/wiki/Lionel_Messi")

print(response)
```

Tavily also allows you to perform a smart crawl starting at a given URL.

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.crawl("https://docs.tavily.com", instructions="Find all pages on the Python SDK")

print(response)
```

These examples are very simple, and you can do so much more with Tavily!

## [​](https://docs.tavily.com/sdk/python/quick-start\#features)  Features

Our Python SDK supports the full feature range of our [REST API](https://docs.tavily.com/documentation/api-reference/introduction), and more. We offer both a synchronous and an asynchronous client, for increased flexibility.

- The `search` function lets you harness the full power of Tavily Search.
- The `extract` function allows you to easily retrieve web content with Tavily Extract.
- The `crawl` and `map`functions allow you to intelligently traverse websites and extract content.

For more details, head to the [Python SDK Reference](https://docs.tavily.com/sdk/python/reference).

[Usage\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/usage) [SDK Reference\\
\\
Next](https://docs.tavily.com/sdk/python/reference)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.