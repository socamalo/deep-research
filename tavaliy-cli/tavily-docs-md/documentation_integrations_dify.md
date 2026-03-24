Title: Dify - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/dify
Description: Tavily is now available for no-code integration through Dify.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/dify#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Dify

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### Tavily MCP Server

- [Tavily MCP Server](https://docs.tavily.com/documentation/mcp)

##### Tavily Agent Skills

- [Tavily Agent Skills](https://docs.tavily.com/documentation/agent-skills)

##### Partnerships

- [Databricks](https://docs.tavily.com/documentation/partnerships/databricks)
- [Amazon Bedrock AgentCore](https://docs.tavily.com/documentation/partnerships/amazon)
- [Microsoft Azure](https://docs.tavily.com/documentation/partnerships/azure)
- [IBM watsonx Orchestrate](https://docs.tavily.com/documentation/partnerships/ibm)
- [Snowflake](https://docs.tavily.com/documentation/partnerships/snowflake)

##### Integrations

- [LangChain](https://docs.tavily.com/documentation/integrations/langchain)
- [Vercel AI SDK](https://docs.tavily.com/documentation/integrations/vercel)
- [LlamaIndex](https://docs.tavily.com/documentation/integrations/llamaindex)
- [OpenAI](https://docs.tavily.com/documentation/integrations/openai)
- [Google ADK](https://docs.tavily.com/documentation/integrations/google-adk)
- [Anthropic](https://docs.tavily.com/documentation/integrations/anthropic)
- [n8n](https://docs.tavily.com/documentation/integrations/n8n)
- [Make](https://docs.tavily.com/documentation/integrations/make)
- [OpenAI Agent Builder](https://docs.tavily.com/documentation/integrations/agent-builder)
- [Langflow](https://docs.tavily.com/documentation/integrations/langflow)
- [Zapier](https://docs.tavily.com/documentation/integrations/zapier)
- [Tines](https://docs.tavily.com/documentation/integrations/tines)
- [Dify](https://docs.tavily.com/documentation/integrations/dify)
- [Composio](https://docs.tavily.com/documentation/integrations/composio)
- [Agno](https://docs.tavily.com/documentation/integrations/agno)
- [Pydantic AI](https://docs.tavily.com/documentation/integrations/pydantic-ai)
- [FlowiseAI](https://docs.tavily.com/documentation/integrations/flowise)
- [CrewAI](https://docs.tavily.com/documentation/integrations/crewai)
- [StackAI](https://docs.tavily.com/documentation/integrations/stackai)

On this page

- [Introduction](https://docs.tavily.com/documentation/integrations/dify#introduction)
- [How to set up Tavily with Dify](https://docs.tavily.com/documentation/integrations/dify#how-to-set-up-tavily-with-dify)
- [Using the Tavily tool in Dify](https://docs.tavily.com/documentation/integrations/dify#using-the-tavily-tool-in-dify)
- [Chatflow / Workflow Applications](https://docs.tavily.com/documentation/integrations/dify#chatflow-%2F-workflow-applications)
- [Agent Applications](https://docs.tavily.com/documentation/integrations/dify#agent-applications)
- [Example use case: automated deep research](https://docs.tavily.com/documentation/integrations/dify#example-use-case-automated-deep-research)
- [Best practices for using Tavily in Dify](https://docs.tavily.com/documentation/integrations/dify#best-practices-for-using-tavily-in-dify)

## [​](https://docs.tavily.com/documentation/integrations/dify\#introduction)  Introduction

Integrate Tavily with Dify to enhance your AI workflows without writing any code. Dify is a no-code platform that allows you to build and deploy AI applications using various tools, including the **Tavily Search API** and **Tavily Extract API**. This integration enables access to real-time web data, improving the capabilities of your AI applications.

## [​](https://docs.tavily.com/documentation/integrations/dify\#how-to-set-up-tavily-with-dify)  How to set up Tavily with Dify

Follow these steps to integrate Tavily with Dify:

Step 1: Log in to Dify

Go to [Dify](https://dify.ai/) and log in to your account.

Step 2: Obtain Your Tavily API Key

Go to the [Tavily Dashboard](https://app.tavily.com/home) to obtain your **API key**.

Step 3: Install the Tavily Tool

Install the **Tavily tool** from the [Plugin Marketplace](https://marketplace.dify.ai/plugins/langgenius/tavily) to enable integration with your Dify workflows.

Step 4: Authorize Tavily in Dify

In **Dify**, navigate to **Tools > Tavily > To Authorize** and enter your **Tavily API key** to connect your Dify instance to Tavily.

## [​](https://docs.tavily.com/documentation/integrations/dify\#using-the-tavily-tool-in-dify)  Using the Tavily tool in Dify

Tavily can be utilized in various Dify application types:

### [​](https://docs.tavily.com/documentation/integrations/dify\#chatflow-/-workflow-applications)  Chatflow / Workflow Applications

Dify’s Chatflow and Workflow applications support Tavily tool nodes, which include:

- **Tavily Search API** – Perform dynamic web searches and retrieve up-to-date information.
- **Tavily Extract API** – Extract raw content from web pages.

These nodes allow you to automate tasks such as research, content curation, and real-time data integration into your workflows.

### [​](https://docs.tavily.com/documentation/integrations/dify\#agent-applications)  Agent Applications

In Agent applications, you can integrate the Tavily tool to access web data in real time. Use this to:

- Retrieve structured and relevant search results.
- Extract raw content for further processing.
- Provide accurate, context-aware answers to user queries.

![defy](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/defy-tavily.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=661597a8a309ab38870e3600fa07fbc5)

## [​](https://docs.tavily.com/documentation/integrations/dify\#example-use-case-automated-deep-research)  Example use case: automated deep research

Use **Tavily Search API** within **Dify** to conduct automated, multi-step searches, iterating through multiple queries to gather, refine, and summarize insights for comprehensive reports.For a detailed walkthrough, check out this blog post:
[DeepResearch: Building a Research Automation App with Dify](https://dify.ai/blog/deepresearch-building-a-research-automation-app-with-dify)

## [​](https://docs.tavily.com/documentation/integrations/dify\#best-practices-for-using-tavily-in-dify)  Best practices for using Tavily in Dify

- **Design Concise Queries** – Use focused queries to maximize the relevance of search results.
- **Utilize Domain Filtering** – Use the `include_domains` parameter to narrow search results to specific domains.
- **Enable an Agentic Workflow** – Leverage an LLM to dynamically generate and refine queries for Tavily.

* * *

[Tines\\
\\
Previous](https://docs.tavily.com/documentation/integrations/tines) [Composio\\
\\
Next](https://docs.tavily.com/documentation/integrations/composio)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![defy](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/defy-tavily.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=62b0b80ca392a2517847c1ab69255ed2)