Title: Crawl to RAG - Tavily Docs
URL: https://docs.tavily.com/examples/use-cases/crawl-to-rag
Description: Turn Any Website into a Searchable Knowledge Base using Tavily and MongoDB.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/examples/use-cases/crawl-to-rag#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Use Cases

Crawl to RAG

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

- [The system operates through a two-step process:](https://docs.tavily.com/examples/use-cases/crawl-to-rag#the-system-operates-through-a-two-step-process)
- [1\. Website Crawling & Vectorization:](https://docs.tavily.com/examples/use-cases/crawl-to-rag#1-website-crawling-%26-vectorization)
- [2\. Intelligent Q&A Interface:](https://docs.tavily.com/examples/use-cases/crawl-to-rag#2-intelligent-q%26a-interface)
- [Try Our Crawl to RAG Use Case](https://docs.tavily.com/examples/use-cases/crawl-to-rag#try-our-crawl-to-rag-use-case)
- [Step 1: Get Your API Key](https://docs.tavily.com/examples/use-cases/crawl-to-rag#step-1-get-your-api-key)
- [Step 2: Chat with Tavily](https://docs.tavily.com/examples/use-cases/crawl-to-rag#step-2-chat-with-tavily)
- [Step 3: Read The Open Source Code](https://docs.tavily.com/examples/use-cases/crawl-to-rag#step-3-read-the-open-source-code)
- [Features](https://docs.tavily.com/examples/use-cases/crawl-to-rag#features)

## [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#the-system-operates-through-a-two-step-process)  The system operates through a two-step process:

### [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#1-website-crawling-&-vectorization)  1\. Website Crawling & Vectorization:

Use Tavily’s crawling endpoint to extract and sitemap content from a webpage URL, then embed it into a MongoDB Atlas vector index for retrieval.![Vectorize](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/crawl2rag.gif?s=d33fd9c90043d6a3b03da8a9b7f9d174)

### [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#2-intelligent-q&a-interface)  2\. Intelligent Q&A Interface:

Query your crawled data through a conversational agent that provides citation-backed answers while maintaining conversation history and context. The agent intelligently distinguishes between informational questions (requiring vector search) and conversational queries (using general knowledge).![Chat with vector](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/crawl2rag-pt2.gif?s=931fbe7a417fb684b47b26c1467d9824)

## [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#try-our-crawl-to-rag-use-case)  Try Our Crawl to RAG Use Case

### [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#step-1-get-your-api-key)  Step 1: Get Your API Key

[**Get your Tavily API key**](https://app.tavily.com/)

### [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#step-2-chat-with-tavily)  Step 2: Chat with Tavily

[**Launch the application**](https://crawl-to-rag.tavily.com/)

### [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#step-3-read-the-open-source-code)  Step 3: Read The Open Source Code

[**View Github Repository**](https://github.com/tavily-ai/crawl2rag)

## [​](https://docs.tavily.com/examples/use-cases/crawl-to-rag\#features)  Features

1. **Advanced Web Crawling**: Deep website content extraction using Tavily’s crawling API
2. **Vector Search**: MongoDB Atlas vector search with OpenAI embeddings for semantic content retrieval
3. **Smart Question Routing**: Automatic detection of informational vs. conversational queries
4. **Persistent Memory**: Conversation history and context preservation using LangGraph-MongoDB checkpointing
5. **Session Management**: Thread-based conversational persistance and vector store management

[Company Research\\
\\
Previous](https://docs.tavily.com/examples/use-cases/company-research) [Meeting Prep\\
\\
Next](https://docs.tavily.com/examples/use-cases/meeting-prep)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Vectorize](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/crawl2rag.gif?s=d33fd9c90043d6a3b03da8a9b7f9d174)

![Chat with vector](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/crawl2rag-pt2.gif?s=931fbe7a417fb684b47b26c1467d9824)