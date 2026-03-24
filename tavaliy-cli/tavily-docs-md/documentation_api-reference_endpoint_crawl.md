Title: Tavily Crawl - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/endpoint/crawl
Description: Tavily Crawl is a graph-based website traversal tool that can explore hundreds of paths in parallel with built-in extraction and intelligent discovery.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

API Reference

Tavily Crawl

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
response = tavily_client.crawl("https://docs.tavily.com", instructions="Find all pages on the Python SDK")

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
    {\
      "url": "https://docs.tavily.com/welcome",\
      "raw_content": "Welcome - Tavily Docs\n\n[Tavily Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/dark.svg)](https://tavily.com/)\n\nSearch or ask...\n\nCtrl K\n\n- [Support](mailto:support@tavily.com)\n- [Get an API key](https://app.tavily.com)\n- [Get an API key](https://app.tavily.com)\n\nSearch...\n\nNavigation\n\n[Home](/welcome)[Documentation](/documentation/about)[SDKs](/sdk/python/quick-start)[Examples](/examples/use-cases/data-enrichment)[FAQ](/faq/faq)\n\nExplore our docs\n\nYour journey to state-of-the-art web search starts right here.\n\n[## Quickstart\n\nStart searching with Tavily in minutes](documentation/quickstart)[## API Reference\n\nStart using Tavily's powerful APIs](documentation/api-reference/endpoint/search)[## API Credits Overview\n\nLearn how to get and manage your Tavily API Credits](documentation/api-credits)[## Rate Limits\n\nLearn about Tavily's API rate limits for both development and production environments](documentation/rate-limits)[## Python\n\nGet started with our Python SDK, `tavily-python`](sdk/python/quick-start)[## Playground\n\nExplore Tavily's APIs with our interactive playground](https://app.tavily.com/playground)",\
      "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
    },\
    {\
      "url": "https://docs.tavily.com/documentation/api-credits",\
      "raw_content": "Credits & Pricing - Tavily Docs\n\n[Tavily Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/dark.svg)](https://tavily.com/)\n\nSearch or ask...\n\nCtrl K\n\n- [Support](mailto:support@tavily.com)\n- [Get an API key](https://app.tavily.com)\n- [Get an API key](https://app.tavily.com)\n\nSearch...\n\nNavigation\n\nOverview\n\nCredits & Pricing\n\n[Home](/welcome)[Documentation](/documentation/about)[SDKs](/sdk/python/quick-start)[Examples](/examples/use-cases/data-enrichment)[FAQ](/faq/faq)\n\n- [API Playground](https://app.tavily.com/playground)\n- [Community](https://community.tavily.com)\n- [Blog](https://blog.tavily.com)\n\n##### Overview\n\n- [About](/documentation/about)\n- [Quickstart](/documentation/quickstart)\n- [Credits & Pricing](/documentation/api-credits)\n- [Rate Limits](/documentation/rate-limits)\n\n##### API Reference\n\n- [Introduction](/documentation/api-reference/introduction)\n- [POST\n\n  Tavily Search](/documentation/api-reference/endpoint/search)\n- [POST\n\n  Tavily Extract](/documentation/api-reference/endpoint/extract)\n- [POST\n\n  Tavily Crawl](/documentation/api-reference/endpoint/crawl)\n- [POST\n\n  Tavily Map](/documentation/api-reference/endpoint/map)\n\n##### Best Practices\n\n- [Best Practices for Search](/documentation/best-practices/best-practices-search)\n- [Best Practices for Extract](/documentation/best-practices/best-practices-extract)\n\n##### Tavily MCP Server\n\n- [Tavily MCP Server](/documentation/mcp)\n\n##### Integrations\n\n- [LangChain](/documentation/integrations/langchain)\n- [LlamaIndex](/documentation/integrations/llamaindex)\n- [Zapier](/documentation/integrations/zapier)\n- [Dify](/documentation/integrations/dify)\n- [Composio](/documentation/integrations/composio)\n- [Make](/documentation/integrations/make)\n- [Agno](/documentation/integrations/agno)\n- [Pydantic AI](/documentation/integrations/pydantic-ai)\n- [FlowiseAI](/documentation/integrations/flowise)\n\n##### Legal\n\n- [Security & Compliance](https://trust.tavily.com)\n- [Privacy Policy](https://tavily.com/privacy)\n\n##### Help\n\n- [Help Center](https://help.tavily.com)\n\n##### Tavily Search Crawler\n\n- [Tavily Search Crawler](/documentation/search-crawler)\n\nOverview\n\n# Credits & Pricing\n\nLearn how to get and manage your Tavily API Credits.\n\n## [​](#free-api-credits) Free API Credits\n\n[## Get your free API key\n\nYou get 1,000 free API Credits every month.\n**No credit card required.**](https://app.tavily.com)\n\n## [​](#pricing-overview) Pricing Overview\n\nTavily operates on a simple, credit-based model:\n\n- **Free**: 1,000 credits/month\n- **Pay-as-you-go**: $0.008 per credit (allows you to be charged per credit once your plan's credit limit is reached).\n- **Monthly plans**: $0.0075 - $0.005 per credit\n- **Enterprise**: Custom pricing and volume\n\n| **Plan** | **Credits per month** | **Monthly price** | **Price per credit** |\n| --- | --- | --- | --- |\n| **Researcher** | 1,000 | Free | - |\n| **Project** | 4,000 | $30 | $0.0075 |\n| **Bootstrap** | 15,000 | $100 | $0.0067 |\n| **Startup** | 38,000 | $220 | $0.0058 |\n| **Growth** | 100,000 | $500 | $0.005 |\n| **Pay as you go** | Per usage | $0.008 / Credit | $0.008 |\n| **Enterprise** | Custom | Custom | Custom |\n\nHead to [my plan](https://app.tavily.com/account/plan) to explore our different options and manage your plan.\n\n## [​](#api-credits-costs) API Credits Costs\n\n### [​](#tavily-search) Tavily Search\n\nYour [search depth](/api-reference/endpoint/search#body-search-depth) determines the cost of your request.\n\n- **Basic Search (`basic`):**\n  Each request costs **1 API credit**.\n- **Advanced Search (`advanced`):**\n  Each request costs **2 API credits**.\n\n### [​](#tavily-extract) Tavily Extract\n\nThe number of successful URL extractions and your [extraction depth](/api-reference/endpoint/extract#body-extract-depth) determines the cost of your request. You never get charged if a URL extraction fails.\n\n- **Basic Extract (`basic`):**\n  Every 5 successful URL extractions cost **1 API credit**\n- **Advanced Extract (`advanced`):**\n  Every 5 successful URL extractions cost **2 API credits**\n\n[Quickstart](/documentation/quickstart)[Rate Limits](/documentation/rate-limits)\n\n[x](https://x.com/tavilyai)[github](https://github.com/tavily-ai)[linkedin](https://linkedin.com/company/tavily)[website](https://tavily.com)\n\n[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.tavily.com)\n\nOn this page\n\n- [Free API Credits](#free-api-credits)\n- [Pricing Overview](#pricing-overview)\n- [API Credits Costs](#api-credits-costs)\n- [Tavily Search](#tavily-search)\n- [Tavily Extract](#tavily-extract)",\
      "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
    },\
    {\
      "url": "https://docs.tavily.com/documentation/about",\
      "raw_content": "Who are we?\n-----------\n\nWe're a team of AI researchers and developers passionate about helping you build the next generation of AI assistants. Our mission is to empower individuals and organizations with accurate, unbiased, and factual information.\n\nWhat is the Tavily Search Engine?\n---------------------------------\n\nBuilding an AI agent that leverages realtime online information is not a simple task. Scraping doesn't scale and requires expertise to refine, current search engine APIs don't provide explicit information to queries but simply potential related articles (which are not always related), and are not very customziable for AI agent needs. This is why we're excited to introduce the first search engine for AI agents - [Tavily](https://app.tavily.com/).\n\nTavily is a search engine optimized for LLMs, aimed at efficient, quick and persistent search results. Unlike other search APIs such as Serp or Google, Tavily focuses on optimizing search for AI developers and autonomous AI agents. We take care of all the burden of searching, scraping, filtering and extracting the most relevant information from online sources. All in a single API call!\n\nTo try the API in action, you can now use our hosted version on our [API Playground](https://app.tavily.com/playground).\n\nWhy choose Tavily?\n------------------\n\nTavily shines where others fail, with a Search API optimized for LLMs.\n\nHow does the Search API work?\n-----------------------------\n\nTraditional search APIs such as Google, Serp and Bing retrieve search results based on a user query. However, the results are sometimes irrelevant to the goal of the search, and return simple URLs and snippets of content which are not always relevant. Because of this, any developer would need to then scrape the sites to extract relevant content, filter irrelevant information, optimize the content to fit LLM context limits, and more. This task is a burden and requires a lot of time and effort to complete. The Tavily Search API takes care of all of this for you in a single API call.\n\nThe Tavily Search API aggregates up to 20 sites per a single API call, and uses proprietary AI to score, filter and rank the top most relevant sources and content to your task, query or goal. In addition, Tavily allows developers to add custom fields such as context and limit response tokens to enable the optimal search experience for LLMs.\n\nTavily can also help your AI agent make better decisions by including a short answer for cross-agent communication.\n\nGetting started\n---------------\n\n[Sign up](https://app.tavily.com/) for Tavily to get your API key. You get **1,000 free API Credits every month**. No credit card required.\n\n[Get your free API key --------------------- You get 1,000 free API Credits every month. **No credit card required.**](https://app.tavily.com/)Head to our [API Playground](https://app.tavily.com/playground) to familiarize yourself with our API.\n\nTo get started with Tavily's APIs and SDKs using code, head to our [Quickstart Guide](https://docs.tavily.com/guides/quickstart) and follow the steps.",\
      "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
    }\
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

crawl

Python SDK

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.crawl("https://docs.tavily.com", instructions="Find all pages on the Python SDK")

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
    {\
      "url": "https://docs.tavily.com/welcome",\
      "raw_content": "Welcome - Tavily Docs\n\n[Tavily Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/dark.svg)](https://tavily.com/)\n\nSearch or ask...\n\nCtrl K\n\n- [Support](mailto:support@tavily.com)\n- [Get an API key](https://app.tavily.com)\n- [Get an API key](https://app.tavily.com)\n\nSearch...\n\nNavigation\n\n[Home](/welcome)[Documentation](/documentation/about)[SDKs](/sdk/python/quick-start)[Examples](/examples/use-cases/data-enrichment)[FAQ](/faq/faq)\n\nExplore our docs\n\nYour journey to state-of-the-art web search starts right here.\n\n[## Quickstart\n\nStart searching with Tavily in minutes](documentation/quickstart)[## API Reference\n\nStart using Tavily's powerful APIs](documentation/api-reference/endpoint/search)[## API Credits Overview\n\nLearn how to get and manage your Tavily API Credits](documentation/api-credits)[## Rate Limits\n\nLearn about Tavily's API rate limits for both development and production environments](documentation/rate-limits)[## Python\n\nGet started with our Python SDK, `tavily-python`](sdk/python/quick-start)[## Playground\n\nExplore Tavily's APIs with our interactive playground](https://app.tavily.com/playground)",\
      "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
    },\
    {\
      "url": "https://docs.tavily.com/documentation/api-credits",\
      "raw_content": "Credits & Pricing - Tavily Docs\n\n[Tavily Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/dark.svg)](https://tavily.com/)\n\nSearch or ask...\n\nCtrl K\n\n- [Support](mailto:support@tavily.com)\n- [Get an API key](https://app.tavily.com)\n- [Get an API key](https://app.tavily.com)\n\nSearch...\n\nNavigation\n\nOverview\n\nCredits & Pricing\n\n[Home](/welcome)[Documentation](/documentation/about)[SDKs](/sdk/python/quick-start)[Examples](/examples/use-cases/data-enrichment)[FAQ](/faq/faq)\n\n- [API Playground](https://app.tavily.com/playground)\n- [Community](https://community.tavily.com)\n- [Blog](https://blog.tavily.com)\n\n##### Overview\n\n- [About](/documentation/about)\n- [Quickstart](/documentation/quickstart)\n- [Credits & Pricing](/documentation/api-credits)\n- [Rate Limits](/documentation/rate-limits)\n\n##### API Reference\n\n- [Introduction](/documentation/api-reference/introduction)\n- [POST\n\n  Tavily Search](/documentation/api-reference/endpoint/search)\n- [POST\n\n  Tavily Extract](/documentation/api-reference/endpoint/extract)\n- [POST\n\n  Tavily Crawl](/documentation/api-reference/endpoint/crawl)\n- [POST\n\n  Tavily Map](/documentation/api-reference/endpoint/map)\n\n##### Best Practices\n\n- [Best Practices for Search](/documentation/best-practices/best-practices-search)\n- [Best Practices for Extract](/documentation/best-practices/best-practices-extract)\n\n##### Tavily MCP Server\n\n- [Tavily MCP Server](/documentation/mcp)\n\n##### Integrations\n\n- [LangChain](/documentation/integrations/langchain)\n- [LlamaIndex](/documentation/integrations/llamaindex)\n- [Zapier](/documentation/integrations/zapier)\n- [Dify](/documentation/integrations/dify)\n- [Composio](/documentation/integrations/composio)\n- [Make](/documentation/integrations/make)\n- [Agno](/documentation/integrations/agno)\n- [Pydantic AI](/documentation/integrations/pydantic-ai)\n- [FlowiseAI](/documentation/integrations/flowise)\n\n##### Legal\n\n- [Security & Compliance](https://trust.tavily.com)\n- [Privacy Policy](https://tavily.com/privacy)\n\n##### Help\n\n- [Help Center](https://help.tavily.com)\n\n##### Tavily Search Crawler\n\n- [Tavily Search Crawler](/documentation/search-crawler)\n\nOverview\n\n# Credits & Pricing\n\nLearn how to get and manage your Tavily API Credits.\n\n## [​](#free-api-credits) Free API Credits\n\n[## Get your free API key\n\nYou get 1,000 free API Credits every month.\n**No credit card required.**](https://app.tavily.com)\n\n## [​](#pricing-overview) Pricing Overview\n\nTavily operates on a simple, credit-based model:\n\n- **Free**: 1,000 credits/month\n- **Pay-as-you-go**: $0.008 per credit (allows you to be charged per credit once your plan's credit limit is reached).\n- **Monthly plans**: $0.0075 - $0.005 per credit\n- **Enterprise**: Custom pricing and volume\n\n| **Plan** | **Credits per month** | **Monthly price** | **Price per credit** |\n| --- | --- | --- | --- |\n| **Researcher** | 1,000 | Free | - |\n| **Project** | 4,000 | $30 | $0.0075 |\n| **Bootstrap** | 15,000 | $100 | $0.0067 |\n| **Startup** | 38,000 | $220 | $0.0058 |\n| **Growth** | 100,000 | $500 | $0.005 |\n| **Pay as you go** | Per usage | $0.008 / Credit | $0.008 |\n| **Enterprise** | Custom | Custom | Custom |\n\nHead to [my plan](https://app.tavily.com/account/plan) to explore our different options and manage your plan.\n\n## [​](#api-credits-costs) API Credits Costs\n\n### [​](#tavily-search) Tavily Search\n\nYour [search depth](/api-reference/endpoint/search#body-search-depth) determines the cost of your request.\n\n- **Basic Search (`basic`):**\n  Each request costs **1 API credit**.\n- **Advanced Search (`advanced`):**\n  Each request costs **2 API credits**.\n\n### [​](#tavily-extract) Tavily Extract\n\nThe number of successful URL extractions and your [extraction depth](/api-reference/endpoint/extract#body-extract-depth) determines the cost of your request. You never get charged if a URL extraction fails.\n\n- **Basic Extract (`basic`):**\n  Every 5 successful URL extractions cost **1 API credit**\n- **Advanced Extract (`advanced`):**\n  Every 5 successful URL extractions cost **2 API credits**\n\n[Quickstart](/documentation/quickstart)[Rate Limits](/documentation/rate-limits)\n\n[x](https://x.com/tavilyai)[github](https://github.com/tavily-ai)[linkedin](https://linkedin.com/company/tavily)[website](https://tavily.com)\n\n[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.tavily.com)\n\nOn this page\n\n- [Free API Credits](#free-api-credits)\n- [Pricing Overview](#pricing-overview)\n- [API Credits Costs](#api-credits-costs)\n- [Tavily Search](#tavily-search)\n- [Tavily Extract](#tavily-extract)",\
      "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
    },\
    {\
      "url": "https://docs.tavily.com/documentation/about",\
      "raw_content": "Who are we?\n-----------\n\nWe're a team of AI researchers and developers passionate about helping you build the next generation of AI assistants. Our mission is to empower individuals and organizations with accurate, unbiased, and factual information.\n\nWhat is the Tavily Search Engine?\n---------------------------------\n\nBuilding an AI agent that leverages realtime online information is not a simple task. Scraping doesn't scale and requires expertise to refine, current search engine APIs don't provide explicit information to queries but simply potential related articles (which are not always related), and are not very customziable for AI agent needs. This is why we're excited to introduce the first search engine for AI agents - [Tavily](https://app.tavily.com/).\n\nTavily is a search engine optimized for LLMs, aimed at efficient, quick and persistent search results. Unlike other search APIs such as Serp or Google, Tavily focuses on optimizing search for AI developers and autonomous AI agents. We take care of all the burden of searching, scraping, filtering and extracting the most relevant information from online sources. All in a single API call!\n\nTo try the API in action, you can now use our hosted version on our [API Playground](https://app.tavily.com/playground).\n\nWhy choose Tavily?\n------------------\n\nTavily shines where others fail, with a Search API optimized for LLMs.\n\nHow does the Search API work?\n-----------------------------\n\nTraditional search APIs such as Google, Serp and Bing retrieve search results based on a user query. However, the results are sometimes irrelevant to the goal of the search, and return simple URLs and snippets of content which are not always relevant. Because of this, any developer would need to then scrape the sites to extract relevant content, filter irrelevant information, optimize the content to fit LLM context limits, and more. This task is a burden and requires a lot of time and effort to complete. The Tavily Search API takes care of all of this for you in a single API call.\n\nThe Tavily Search API aggregates up to 20 sites per a single API call, and uses proprietary AI to score, filter and rank the top most relevant sources and content to your task, query or goal. In addition, Tavily allows developers to add custom fields such as context and limit response tokens to enable the optimal search experience for LLMs.\n\nTavily can also help your AI agent make better decisions by including a short answer for cross-agent communication.\n\nGetting started\n---------------\n\n[Sign up](https://app.tavily.com/) for Tavily to get your API key. You get **1,000 free API Credits every month**. No credit card required.\n\n[Get your free API key --------------------- You get 1,000 free API Credits every month. **No credit card required.**](https://app.tavily.com/)Head to our [API Playground](https://app.tavily.com/playground) to familiarize yourself with our API.\n\nTo get started with Tavily's APIs and SDKs using code, head to our [Quickstart Guide](https://docs.tavily.com/guides/quickstart) and follow the steps.",\
      "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
    }\
  ],
  "response_time": 1.23,
  "usage": {
    "credits": 1
  },
  "request_id": "123e4567-e89b-12d3-a456-426614174111"
}
```

#### Authorizations

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#authorization-authorization)

Authorization

string

header

required

Bearer authentication header in the form Bearer , where  is your Tavily API key (e.g., Bearer tvly-YOUR\_API\_KEY).

#### Body

application/json

Parameters for the Tavily Crawl request.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-url)

url

string

required

The root URL to begin the crawl.

Example:

`"docs.tavily.com"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-instructions)

instructions

string

Natural language instructions for the crawler. When specified, the mapping cost increases to 2 API credits per 10 successful pages instead of 1 API credit per 10 pages.

Example:

`"Find all pages about the Python SDK"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-chunks-per-source)

chunks\_per\_source

integer

default:3

Chunks are short content snippets (maximum 500 characters each) pulled directly from the source. Use `chunks_per_source` to define the maximum number of relevant chunks returned per source and to control the `raw_content` length. Chunks will appear in the `raw_content` field as: `<chunk 1> [...] <chunk 2> [...] <chunk 3>`. Available only when `instructions` are provided. Must be between 1 and 5.

Required range: `1 <= x <= 5`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-max-depth)

max\_depth

integer

default:1

Max depth of the crawl. Defines how far from the base URL the crawler can explore.

Required range: `1 <= x <= 5`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-max-breadth)

max\_breadth

integer

default:20

Max number of links to follow per level of the tree (i.e., per page).

Required range: `1 <= x <= 500`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-limit)

limit

integer

default:50

Total number of links the crawler will process before stopping.

Required range: `x >= 1`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-select-paths)

select\_paths

string\[\]

Regex patterns to select only URLs with specific path patterns (e.g., `/docs/.*`, `/api/v1.*`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-select-domains)

select\_domains

string\[\]

Regex patterns to select crawling to specific domains or subdomains (e.g., `^docs\.example\.com$`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-exclude-paths)

exclude\_paths

string\[\]

Regex patterns to exclude URLs with specific path patterns (e.g., `/private/.*`, `/admin/.*`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-exclude-domains)

exclude\_domains

string\[\]

Regex patterns to exclude specific domains or subdomains from crawling (e.g., `^private\.example\.com$`).

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-allow-external)

allow\_external

boolean

default:true

Whether to include external domain links in the final results list.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-include-images)

include\_images

boolean

default:false

Whether to include images in the crawl results.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-extract-depth)

extract\_depth

enum<string>

default:basic

Advanced extraction retrieves more data, including tables and embedded content, with higher success but may increase latency. `basic` extraction costs 1 credit per 5 successful extractions, while `advanced` extraction costs 2 credits per 5 successful extractions.

Available options:

`basic`,

`advanced`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-format)

format

enum<string>

default:markdown

The format of the extracted web page content. `markdown` returns content in markdown format. `text` returns plain text and may increase latency.

Available options:

`markdown`,

`text`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-include-favicon)

include\_favicon

boolean

default:false

Whether to include the favicon URL for each result.

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-timeout)

timeout

number<float>

default:150

Maximum time in seconds to wait for the crawl operation before timing out. Must be between 10 and 150 seconds.

Required range: `10 <= x <= 150`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#body-include-usage)

include\_usage

boolean

default:false

Whether to include credit usage information in the response. `NOTE:`The value may be 0 if the total use of /extract and /map have not yet reached minimum requirements. See our [Credits & Pricing documentation](https://docs.tavily.com/documentation/api-credits) for details.

#### Response

200

application/json

Crawl results returned successfully

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#response-base-url)

base\_url

string

The base URL that was crawled.

Example:

`"docs.tavily.com"`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#response-results)

results

object\[\]

A list of extracted content from the crawled URLs.

Showchild attributes

Example:

```
[\
  {\
    "url": "https://docs.tavily.com/welcome",\
    "raw_content": "Welcome - Tavily Docs\n\n[Tavily Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/dark.svg)](https://tavily.com/)\n\nSearch or ask...\n\nCtrl K\n\n- [Support](mailto:support@tavily.com)\n- [Get an API key](https://app.tavily.com)\n- [Get an API key](https://app.tavily.com)\n\nSearch...\n\nNavigation\n\n[Home](/welcome)[Documentation](/documentation/about)[SDKs](/sdk/python/quick-start)[Examples](/examples/use-cases/data-enrichment)[FAQ](/faq/faq)\n\nExplore our docs\n\nYour journey to state-of-the-art web search starts right here.\n\n[## Quickstart\n\nStart searching with Tavily in minutes](documentation/quickstart)[## API Reference\n\nStart using Tavily's powerful APIs](documentation/api-reference/endpoint/search)[## API Credits Overview\n\nLearn how to get and manage your Tavily API Credits](documentation/api-credits)[## Rate Limits\n\nLearn about Tavily's API rate limits for both development and production environments](documentation/rate-limits)[## Python\n\nGet started with our Python SDK, `tavily-python`](sdk/python/quick-start)[## Playground\n\nExplore Tavily's APIs with our interactive playground](https://app.tavily.com/playground)",\
    "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
  },\
  {\
    "url": "https://docs.tavily.com/documentation/api-credits",\
    "raw_content": "Credits & Pricing - Tavily Docs\n\n[Tavily Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/dark.svg)](https://tavily.com/)\n\nSearch or ask...\n\nCtrl K\n\n- [Support](mailto:support@tavily.com)\n- [Get an API key](https://app.tavily.com)\n- [Get an API key](https://app.tavily.com)\n\nSearch...\n\nNavigation\n\nOverview\n\nCredits & Pricing\n\n[Home](/welcome)[Documentation](/documentation/about)[SDKs](/sdk/python/quick-start)[Examples](/examples/use-cases/data-enrichment)[FAQ](/faq/faq)\n\n- [API Playground](https://app.tavily.com/playground)\n- [Community](https://community.tavily.com)\n- [Blog](https://blog.tavily.com)\n\n##### Overview\n\n- [About](/documentation/about)\n- [Quickstart](/documentation/quickstart)\n- [Credits & Pricing](/documentation/api-credits)\n- [Rate Limits](/documentation/rate-limits)\n\n##### API Reference\n\n- [Introduction](/documentation/api-reference/introduction)\n- [POST\n\n  Tavily Search](/documentation/api-reference/endpoint/search)\n- [POST\n\n  Tavily Extract](/documentation/api-reference/endpoint/extract)\n- [POST\n\n  Tavily Crawl](/documentation/api-reference/endpoint/crawl)\n- [POST\n\n  Tavily Map](/documentation/api-reference/endpoint/map)\n\n##### Best Practices\n\n- [Best Practices for Search](/documentation/best-practices/best-practices-search)\n- [Best Practices for Extract](/documentation/best-practices/best-practices-extract)\n\n##### Tavily MCP Server\n\n- [Tavily MCP Server](/documentation/mcp)\n\n##### Integrations\n\n- [LangChain](/documentation/integrations/langchain)\n- [LlamaIndex](/documentation/integrations/llamaindex)\n- [Zapier](/documentation/integrations/zapier)\n- [Dify](/documentation/integrations/dify)\n- [Composio](/documentation/integrations/composio)\n- [Make](/documentation/integrations/make)\n- [Agno](/documentation/integrations/agno)\n- [Pydantic AI](/documentation/integrations/pydantic-ai)\n- [FlowiseAI](/documentation/integrations/flowise)\n\n##### Legal\n\n- [Security & Compliance](https://trust.tavily.com)\n- [Privacy Policy](https://tavily.com/privacy)\n\n##### Help\n\n- [Help Center](https://help.tavily.com)\n\n##### Tavily Search Crawler\n\n- [Tavily Search Crawler](/documentation/search-crawler)\n\nOverview\n\n# Credits & Pricing\n\nLearn how to get and manage your Tavily API Credits.\n\n## [​](#free-api-credits) Free API Credits\n\n[## Get your free API key\n\nYou get 1,000 free API Credits every month.\n**No credit card required.**](https://app.tavily.com)\n\n## [​](#pricing-overview) Pricing Overview\n\nTavily operates on a simple, credit-based model:\n\n- **Free**: 1,000 credits/month\n- **Pay-as-you-go**: $0.008 per credit (allows you to be charged per credit once your plan's credit limit is reached).\n- **Monthly plans**: $0.0075 - $0.005 per credit\n- **Enterprise**: Custom pricing and volume\n\n| **Plan** | **Credits per month** | **Monthly price** | **Price per credit** |\n| --- | --- | --- | --- |\n| **Researcher** | 1,000 | Free | - |\n| **Project** | 4,000 | $30 | $0.0075 |\n| **Bootstrap** | 15,000 | $100 | $0.0067 |\n| **Startup** | 38,000 | $220 | $0.0058 |\n| **Growth** | 100,000 | $500 | $0.005 |\n| **Pay as you go** | Per usage | $0.008 / Credit | $0.008 |\n| **Enterprise** | Custom | Custom | Custom |\n\nHead to [my plan](https://app.tavily.com/account/plan) to explore our different options and manage your plan.\n\n## [​](#api-credits-costs) API Credits Costs\n\n### [​](#tavily-search) Tavily Search\n\nYour [search depth](/api-reference/endpoint/search#body-search-depth) determines the cost of your request.\n\n- **Basic Search (`basic`):**\n  Each request costs **1 API credit**.\n- **Advanced Search (`advanced`):**\n  Each request costs **2 API credits**.\n\n### [​](#tavily-extract) Tavily Extract\n\nThe number of successful URL extractions and your [extraction depth](/api-reference/endpoint/extract#body-extract-depth) determines the cost of your request. You never get charged if a URL extraction fails.\n\n- **Basic Extract (`basic`):**\n  Every 5 successful URL extractions cost **1 API credit**\n- **Advanced Extract (`advanced`):**\n  Every 5 successful URL extractions cost **2 API credits**\n\n[Quickstart](/documentation/quickstart)[Rate Limits](/documentation/rate-limits)\n\n[x](https://x.com/tavilyai)[github](https://github.com/tavily-ai)[linkedin](https://linkedin.com/company/tavily)[website](https://tavily.com)\n\n[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.tavily.com)\n\nOn this page\n\n- [Free API Credits](#free-api-credits)\n- [Pricing Overview](#pricing-overview)\n- [API Credits Costs](#api-credits-costs)\n- [Tavily Search](#tavily-search)\n- [Tavily Extract](#tavily-extract)",\
    "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
  },\
  {\
    "url": "https://docs.tavily.com/documentation/about",\
    "raw_content": "Who are we?\n-----------\n\nWe're a team of AI researchers and developers passionate about helping you build the next generation of AI assistants. Our mission is to empower individuals and organizations with accurate, unbiased, and factual information.\n\nWhat is the Tavily Search Engine?\n---------------------------------\n\nBuilding an AI agent that leverages realtime online information is not a simple task. Scraping doesn't scale and requires expertise to refine, current search engine APIs don't provide explicit information to queries but simply potential related articles (which are not always related), and are not very customziable for AI agent needs. This is why we're excited to introduce the first search engine for AI agents - [Tavily](https://app.tavily.com/).\n\nTavily is a search engine optimized for LLMs, aimed at efficient, quick and persistent search results. Unlike other search APIs such as Serp or Google, Tavily focuses on optimizing search for AI developers and autonomous AI agents. We take care of all the burden of searching, scraping, filtering and extracting the most relevant information from online sources. All in a single API call!\n\nTo try the API in action, you can now use our hosted version on our [API Playground](https://app.tavily.com/playground).\n\nWhy choose Tavily?\n------------------\n\nTavily shines where others fail, with a Search API optimized for LLMs.\n\nHow does the Search API work?\n-----------------------------\n\nTraditional search APIs such as Google, Serp and Bing retrieve search results based on a user query. However, the results are sometimes irrelevant to the goal of the search, and return simple URLs and snippets of content which are not always relevant. Because of this, any developer would need to then scrape the sites to extract relevant content, filter irrelevant information, optimize the content to fit LLM context limits, and more. This task is a burden and requires a lot of time and effort to complete. The Tavily Search API takes care of all of this for you in a single API call.\n\nThe Tavily Search API aggregates up to 20 sites per a single API call, and uses proprietary AI to score, filter and rank the top most relevant sources and content to your task, query or goal. In addition, Tavily allows developers to add custom fields such as context and limit response tokens to enable the optimal search experience for LLMs.\n\nTavily can also help your AI agent make better decisions by including a short answer for cross-agent communication.\n\nGetting started\n---------------\n\n[Sign up](https://app.tavily.com/) for Tavily to get your API key. You get **1,000 free API Credits every month**. No credit card required.\n\n[Get your free API key --------------------- You get 1,000 free API Credits every month. **No credit card required.**](https://app.tavily.com/)Head to our [API Playground](https://app.tavily.com/playground) to familiarize yourself with our API.\n\nTo get started with Tavily's APIs and SDKs using code, head to our [Quickstart Guide](https://docs.tavily.com/guides/quickstart) and follow the steps.",\
    "favicon": "https://mintlify.s3-us-west-1.amazonaws.com/tavilyai/_generated/favicon/apple-touch-icon.png?v=3"\
  }\
]
```

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#response-response-time)

response\_time

number<float>

Time in seconds it took to complete the request.

Example:

`1.23`

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#response-usage)

usage

object

Credit usage details for the request.

Example:

```
{ "credits": 1 }
```

[​](https://docs.tavily.com/documentation/api-reference/endpoint/crawl#response-request-id)

request\_id

string

A unique request identifier you can share with customer support to help resolve issues with specific requests.

Example:

`"123e4567-e89b-12d3-a456-426614174111"`

[Tavily Extract\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/extract) [Tavily Map\\
\\
Next](https://docs.tavily.com/documentation/api-reference/endpoint/map)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.