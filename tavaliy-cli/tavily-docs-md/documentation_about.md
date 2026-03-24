Title: About - Tavily Docs
URL: https://docs.tavily.com/documentation/about
Description: Welcome to Tavily!

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/about#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Getting Started

About

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### Getting Started

- [About](https://docs.tavily.com/documentation/about)
- [Quickstart](https://docs.tavily.com/documentation/quickstart)
- [Credits & Pricing](https://docs.tavily.com/documentation/api-credits)
- [Rate Limits](https://docs.tavily.com/documentation/rate-limits)

##### FAQ

- [Frequently Asked Questions](https://docs.tavily.com/faq/faq)

On this page

- [Who are we?](https://docs.tavily.com/documentation/about#who-are-we)
- [What is the Tavily Search Engine?](https://docs.tavily.com/documentation/about#what-is-the-tavily-search-engine)
- [Why choose Tavily?](https://docs.tavily.com/documentation/about#why-choose-tavily)
- [How does the Search API work?](https://docs.tavily.com/documentation/about#how-does-the-search-api-work)
- [Getting started](https://docs.tavily.com/documentation/about#getting-started)

Looking for a step-by-step tutorial to get started in under 5 minutes? Head to our [Quickstart guide](https://docs.tavily.com/guides/quickstart) and start coding!

## [​](https://docs.tavily.com/documentation/about\#who-are-we)  Who are we?

We’re a team of AI researchers and developers passionate about helping you build the next generation of AI assistants.
Our mission is to empower individuals and organizations with accurate, unbiased, and factual information.

## [​](https://docs.tavily.com/documentation/about\#what-is-the-tavily-search-engine)  What is the Tavily Search Engine?

Building an AI agent that leverages realtime online information is not a simple task. Scraping doesn’t scale and requires expertise to refine, current search engine APIs don’t provide explicit information to queries but simply potential related articles (which are not always related), and are not very customziable for AI agent needs. This is why we’re excited to introduce the first search engine for AI agents - [Tavily](https://app.tavily.com/).Tavily is a search engine optimized for LLMs, aimed at efficient, quick and persistent search results. Unlike other search APIs such as Serp or Google, Tavily focuses on optimizing search for AI developers and autonomous AI agents. We take care of all the burden of searching, scraping, filtering and extracting the most relevant information from online sources. All in a single API call!To try the API in action, you can now use our hosted version on our [API Playground](https://app.tavily.com/playground).

If you’re an AI developer looking to integrate your application with our API, or seek increased API limits, [please reach out!](mailto:support@tavily.com)

## [​](https://docs.tavily.com/documentation/about\#why-choose-tavily)  Why choose Tavily?

Tavily shines where others fail, with a Search API optimized for LLMs.

Purpose-Built

Tailored just for LLM Agents, we ensure the search results are optimized for [RAG](https://towardsdatascience.com/retrieval-augmented-generation-intuitively-and-exhaustively-explain-6a39d6fe6fc9). We take care of all the burden in searching, scraping, filtering and extracting information from online sources. All in a single API call! Simply pass the returned search results as context to your LLM.

Versatility

Beyond just fetching results, the Tavily Search API offers precision. With customizable search depths, domain management, and parsing HTML content controls, you’re in the driver’s seat.

Performance

Committed to speed and efficiency, our API guarantees real-time and trusted information. Our team works hard to improve Tavily’s performance over time.

Integration-friendly

We appreciate the essence of adaptability. That’s why integrating our API with your existing setup is a breeze. You can choose our [Python library](https://pypi.org/project/tavily-python/), [JavaScript package](https://www.npmjs.com/package/@tavily/core) or a simple API call. You can also use Tavily through any of our supported partners such as [LangChain](https://docs.tavily.com/integrations/langchain) and [LlamaIndex](https://docs.tavily.com/integrations/llamaindex).

Transparent & Informative

Our detailed documentation ensures you’re never left in the dark. From setup basics to nuanced features, we’ve got you covered.

## [​](https://docs.tavily.com/documentation/about\#how-does-the-search-api-work)  How does the Search API work?

Traditional search APIs such as Google, Serp and Bing retrieve search results based on a user query. However, the results are sometimes irrelevant to the goal of the search, and return simple URLs and snippets of content which are not always relevant. Because of this, any developer would need to then scrape the sites to extract relevant content, filter irrelevant information, optimize the content to fit LLM context limits, and more. This task is a burden and requires a lot of time and effort to complete. The Tavily Search API takes care of all of this for you in a single API call.The Tavily Search API aggregates up to 20 sites per a single API call, and uses proprietary AI to score, filter and rank the top most relevant sources and content to your task, query or goal.
In addition, Tavily allows developers to add custom fields such as context and limit response tokens to enable the optimal search experience for LLMs.Tavily can also help your AI agent make better decisions by including a short answer for cross-agent communication.

With LLM hallucinations, it’s crucial to optimize for RAG with the right context and information. This is where Tavily comes in, delivering accurate and precise information for your RAG applications.

## [​](https://docs.tavily.com/documentation/about\#getting-started)  Getting started

[Sign up](https://app.tavily.com/) for Tavily to get your API key. You get **1,000 free API Credits every month**. No credit card required. [**Get your free API key** \\
\\
You get 1,000 free API Credits every month. **No credit card required.**](https://app.tavily.com/) Head to our [API Playground](https://app.tavily.com/playground) to familiarize yourself with our API.To get started with Tavily’s APIs and SDKs using code, head to our [Quickstart Guide](https://docs.tavily.com/guides/quickstart) and follow the steps.

Got questions? Stumbled upon an issue? Simply intrigued? Don’t hesitate! Our support team is always on standby, eager to assist. Join us, dive deep, and redefine your search experience! [Contact us!](mailto:support@tavily.com)

[Quickstart\\
\\
Next](https://docs.tavily.com/documentation/quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.