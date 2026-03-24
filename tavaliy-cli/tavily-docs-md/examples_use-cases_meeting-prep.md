Title: Meeting Prep - Tavily Docs
URL: https://docs.tavily.com/examples/use-cases/meeting-prep
Description: Build an intelligent meeting preparation agent with real-time web research capabilities using Tavily's API and Google Calendar integration

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/examples/use-cases/meeting-prep#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Use Cases

Meeting Prep

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

- [Introduction](https://docs.tavily.com/examples/use-cases/meeting-prep#introduction)
- [Try Our Meeting Prep Agent](https://docs.tavily.com/examples/use-cases/meeting-prep#try-our-meeting-prep-agent)
- [Step 1: Get Your API Key](https://docs.tavily.com/examples/use-cases/meeting-prep#step-1-get-your-api-key)
- [Step 2: Read The Open Source Code and Clone the App](https://docs.tavily.com/examples/use-cases/meeting-prep#step-2-read-the-open-source-code-and-clone-the-app)
- [System Diagram](https://docs.tavily.com/examples/use-cases/meeting-prep#system-diagram)
- [Features](https://docs.tavily.com/examples/use-cases/meeting-prep#features)

## [​](https://docs.tavily.com/examples/use-cases/meeting-prep\#introduction)  Introduction

This repository demonstrates how to build a meeting preparation agent with real-time web access, leveraging Tavily’s advanced search capabilities. This agent will connect to your Google Calendar via MCP, extract meeting information, and use Tavily search for profile research on the meeting attendees and general information on the companies you are meeting with.![Meeting Prep Agent Demo](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-agent.gif?s=58004f96bc27a202f3994033fb2c1308)

## [​](https://docs.tavily.com/examples/use-cases/meeting-prep\#try-our-meeting-prep-agent)  Try Our Meeting Prep Agent

### [​](https://docs.tavily.com/examples/use-cases/meeting-prep\#step-1-get-your-api-key)  Step 1: Get Your API Key

[**Get your Tavily API key**](https://app.tavily.com/)

### [​](https://docs.tavily.com/examples/use-cases/meeting-prep\#step-2-read-the-open-source-code-and-clone-the-app)  Step 2: Read The Open Source Code and Clone the App

[**View Github Repository**](https://github.com/tavily-ai/meeting-prep-agent)

## [​](https://docs.tavily.com/examples/use-cases/meeting-prep\#system-diagram)  System Diagram

![Meeting Prep Agent Diagram](https://mintcdn.com/tavilyai/1psaZWEtqkbgGquR/images/meeting-prep-diagram.svg?fit=max&auto=format&n=1psaZWEtqkbgGquR&q=85&s=9d6ce9043329048eacf81ead6814bb33)

## [​](https://docs.tavily.com/examples/use-cases/meeting-prep\#features)  Features

1. **Real-time Web Search**: Instantly fetches up-to-date information using Tavily’s search API.
2. **Agentic Reasoning**: Combines MCP and ReAct agent flows for smarter, context-aware responses.
3. **Streaming Substeps**: See agentic reasoning and substeps streamed live for transparency.
4. **Citations**: All web search results are cited for easy verification.
5. **Google Calendar Integration**: (via mcp-use) Access and analyze your meeting data.
6. **Async FastAPI Backend**: High-performance, async-ready backend for fast responses.
7. **Modern React Frontend**: Interactive UI for dynamic user interactions.

[Crawl to RAG\\
\\
Previous](https://docs.tavily.com/examples/use-cases/crawl-to-rag) [RAG evaluation\\
\\
Next](https://docs.tavily.com/examples/use-cases/web-eval)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Meeting Prep Agent Diagram](https://mintcdn.com/tavilyai/1psaZWEtqkbgGquR/images/meeting-prep-diagram.svg?w=840&fit=max&auto=format&n=1psaZWEtqkbgGquR&q=85&s=19b2509a60f170361f992c49a8e57cac)

![Meeting Prep Agent Demo](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-agent.gif?s=58004f96bc27a202f3994033fb2c1308)