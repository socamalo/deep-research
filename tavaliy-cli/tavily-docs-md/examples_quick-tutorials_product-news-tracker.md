Title: Product News Tracker - Tavily Docs
URL: https://docs.tavily.com/examples/quick-tutorials/product-news-tracker
Description: Stay informed with real-time product news using Tavily's APIs.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Product News Tracker

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### Use Cases

- [Chat](https://docs.tavily.com/examples/use-cases/chat)
- [Data Enrichment](https://docs.tavily.com/examples/use-cases/data-enrichment)
- [Company Research](https://docs.tavily.com/examples/use-cases/company-research)
- [Crawl to RAG](https://docs.tavily.com/examples/use-cases/crawl-to-rag)
- [Meeting Prep](https://docs.tavily.com/examples/use-cases/meeting-prep)
- [RAG evaluation](https://docs.tavily.com/examples/use-cases/web-eval)
- [Market Researcher](https://docs.tavily.com/examples/use-cases/market-researcher)

##### Quick Tutorials

- [Cookbook](https://docs.tavily.com/examples/quick-tutorials/cookbook)

##### Open Source

- [Projects](https://docs.tavily.com/examples/open-sources/projects)

On this page

- [What will you learn?](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#what-will-you-learn)
- [How does it work?](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#how-does-it-work)
- [Self-Reported News](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#self-reported-news)
- [Third-Party Coverage](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#third-party-coverage)
- [Getting Started](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#getting-started)

## [​](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker\#what-will-you-learn)  What will you learn?

In this use case, you’ll discover how to gather a company’s product news and updates using Tavily’s Search API. This tutorial outlines how to get started with the Tavily Python SDK, how to properly configure search parameters for optimal results, and how to effectively interact with Tavily’s Search API to retrieve the latest product updates for a specified company.

## [​](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker\#how-does-it-work)  How does it work?

### [​](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker\#self-reported-news)  Self-Reported News

Our system gathers official updates including **blog posts**, **product announcements**, and **company news** by utilizing the `include_domain` parameter. This allows us to focus specifically on content from:

- A company’s official website

This domain-filtered approach ensures efficient credit usage while maintaining search accuracy.

### [​](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker\#third-party-coverage)  Third-Party Coverage

To capture external perspectives, we employ specialized news search parameters:

- Set `topic = news` to focus on reputable news sources
- Utilize `time_range = month` for current coverage

For the functionality discussed in this tutorial, `search_depth = basic` will
be sufficient to acheive the intended results.

## [​](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker\#getting-started)  Getting Started

> We have prepared a [Jupyter Notebook](https://github.com/tavily-ai/tavily-cookbook/blob/main/search/product_news_tracker.ipynb) outlining the contents of this tutorial

First create an account and get your free API key. [**Get your Tavily API key**](https://app.tavily.com/) Next, use the Tavily Python SDK to create the workflow.

1

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#)

Install the Tavily Python SDK

Shell

Copy

Ask AI

```
pip install -q tavily-python python-dotenv ipykernel
```

2

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#)

Import the necessary libraries

Python

Copy

Ask AI

```
import getpass
import os

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("TAVILY_API_KEY:\n")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
```

3

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#)

Instantiate the Tavily Client

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient()
```

4

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#)

Define the search parameters

Python

Copy

Ask AI

```
def search_product_updates(company_name: str, domains: list):
    all_results = []

    # Search for self-reported news
    company_results = tavily_client.search(
        query=f"{company_name} product news, updates, releases, and announcements",
        search_depth="basic",
        max_results=10,
        include_domains=domains
    )

    for result in company_results["results"]:
        result["search_type"] = "Self-reported News"
        all_results.append(result)

    # Search for third-party coverage
    news_results = tavily_client.search(
        query=f"{company_name} product news, updates, releases, and announcements",
        search_depth="basic",
        max_results=10,
        time_range="month",
        topic="news"
    )

    for result in news_results["results"]:
        result["search_type"] = "Third-party Coverage"
        all_results.append(result)

    return all_results
```

5

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#)

Execute the search

Python

Copy

Ask AI

```
    product_updates = search_product_updates(
        "OpenAI", ["openai.com"]
    )

    product_updates
```

6

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/product-news-tracker#)

Output

Shell

Copy

Ask AI

```
 [\
     {\
         "title": "OpenAI launches new tools to help businesses build AI agents - TechCrunch",\
         "url": "https://techcrunch.com/2025/03/11/openai-launches-new-tools-to-help-businesses-build-ai-agents/",\
         "score": 0.70847535,\
         "published_date": "Tue, 11 Mar 2025 17:00:00 GMT",\
         "content": "OpenAI launches new tools to help businesses build AI agents | TechCrunch OpenAI launches new tools to help businesses build AI agents | TechCrunch On Tuesday, OpenAI released new tools designed to help developers and enterprises build AI agents – automated systems that can independently accomplish tasks – using the company’s own AI models and frameworks. The tools are part of OpenAI’s new Responses API, which lets businesses develop custom AI agents that can perform web searches, scan through company files, and navigate websites, much like OpenAI’s Operator product. Using the Responses API, developers can tap the same AI models (in preview) under the hood of OpenAI’s ChatGPT Search web search tool: GPT-4o search and GPT-4o mini search.",\
         "search_type": "Third-party Coverage"\
     },\
     {\
         "title": "New embedding models and API updates - Announcements - OpenAI Developer ...",\
         "url": "https://community.openai.com/t/new-embedding-models-and-api-updates/610540",\
         "score": 0.752468,\
         "content": "We are releasing new models, reducing prices for GPT-3.5 Turbo, and introducing new ways for developers to manage API keys and understand API usage. The new models include: Two new embedding models An updated GPT-4 Turbo preview model An updated GPT-3.5 Turbo model An updated text moderation model By default, data sent to the OpenAI API will not be used to train or improve OpenAI models. All",\
         "search_type": "Self-reported News"\
     },\
     ...\
 ]
```

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.