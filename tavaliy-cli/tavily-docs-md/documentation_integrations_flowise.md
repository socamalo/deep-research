Title: FlowiseAI - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/flowise
Description: Tavily is now available for integration through Flowise.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/flowise#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

FlowiseAI

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

- [Introduction](https://docs.tavily.com/documentation/integrations/flowise#introduction)
- [How to set up Tavily with Flowise](https://docs.tavily.com/documentation/integrations/flowise#how-to-set-up-tavily-with-flowise)
- [Using Tavily in Flowise](https://docs.tavily.com/documentation/integrations/flowise#using-tavily-in-flowise)
- [Chatflow Applications](https://docs.tavily.com/documentation/integrations/flowise#chatflow-applications)
- [Agent Applications](https://docs.tavily.com/documentation/integrations/flowise#agent-applications)

## [​](https://docs.tavily.com/documentation/integrations/flowise\#introduction)  Introduction

Integrate [Tavily with FlowiseAI](https://docs.flowiseai.com/integrations/langchain/tools/tavily-ai) to enhance your AI workflows with powerful web search capabilities. Flowise provides a no-code platform for building AI applications, and the Tavily integration offers real-time, accurate search results tailored for LLMs and RAG (Retrieval-Augmented Generation) systems.Set up Tavily in Flowise to create chatflows or agent flows that can automate research, track news, or feed relevant data into your connected applications.

## [​](https://docs.tavily.com/documentation/integrations/flowise\#how-to-set-up-tavily-with-flowise)  How to set up Tavily with Flowise

Follow these steps to integrate Tavily with Flowise:

Step 1: Log in to Flowise

[Login](https://flowiseai.com/) to your Flowise account.

Step 2: Create a New Flow

Create a new flow in Flowise:

1. Click “Create New Flow”
2. Select either “Chat Flow” or “Agent Flow” as the type
3. Name your flow (e.g., “Research Assistant”)

Step 3: Add Tavily Node

Add the Tavily node to your flow:

**For Chat Flow:**

1. Click on the (+) button
2. Navigate to **LangChain > Tools > Tavily API**
3. Drag the Tavily node into your flow

**For Agent Flow:**

1. Click on the (+) button
2. Navigate to **Tools > Tavily API**
3. Drag the Tavily node into your flow

Step 4: Configure Tavily Node

Configure the Tavily node with your credentials and parameters:

1. Enter your Tavily API key in the credentials section
2. Configure additional parameters, for example:
   - **Search Depth:** Choose between ‘basic’ or ‘advanced’
   - **Max Results:** Set the number of results to return
   - **Include Domains:** Specify domains to include in search
   - **Exclude Domains:** Specify domains to exclude from search

Step 5: Connect Nodes

Connect the Tavily node to other nodes in your flow:

1. Connect to any node that accepts tool inputs
2. Connect to an LLM node for query processing
3. Connect to a Response node to format results

## [​](https://docs.tavily.com/documentation/integrations/flowise\#using-tavily-in-flowise)  Using Tavily in Flowise

Tavily can be utilized in various Flowise application types:

### [​](https://docs.tavily.com/documentation/integrations/flowise\#chatflow-applications)  Chatflow Applications

Flowise’s Chatflow applications support Tavily tool node. This node allows you to automate tasks such as research, content curation, and real-time data integration into your workflows.

### [​](https://docs.tavily.com/documentation/integrations/flowise\#agent-applications)  Agent Applications

In Agent applications, you can integrate the Tavily tool to access web data in real time. Use this to:

- Retrieve structured and relevant search results
- Extract raw content for further processing
- Provide accurate, context-aware answers to user queries

![Flowise Tavily Integration](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=25e21b93e92b99d765eb7c0c4aba06c5)

[Pydantic AI\\
\\
Previous](https://docs.tavily.com/documentation/integrations/pydantic-ai) [CrewAI\\
\\
Next](https://docs.tavily.com/documentation/integrations/crewai)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Flowise Tavily Integration](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/flowise-tavily.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=9f6f8a85bac404c02610bd789fdfc20f)