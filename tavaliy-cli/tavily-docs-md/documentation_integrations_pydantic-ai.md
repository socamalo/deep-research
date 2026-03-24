Title: Pydantic AI - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/pydantic-ai
Description: Tavily is now available for integration through Pydantic AI.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/pydantic-ai#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Pydantic AI

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

- [Introduction](https://docs.tavily.com/documentation/integrations/pydantic-ai#introduction)
- [Step-by-Step Integration Guide](https://docs.tavily.com/documentation/integrations/pydantic-ai#step-by-step-integration-guide)
- [Step 1: Install Required Packages](https://docs.tavily.com/documentation/integrations/pydantic-ai#step-1-install-required-packages)
- [Step 2: Set Up API Keys](https://docs.tavily.com/documentation/integrations/pydantic-ai#step-2-set-up-api-keys)
- [Step 3: Initialize Pydantic AI Agent with Tavily Tools](https://docs.tavily.com/documentation/integrations/pydantic-ai#step-3-initialize-pydantic-ai-agent-with-tavily-tools)
- [Step 4: Example Use Cases](https://docs.tavily.com/documentation/integrations/pydantic-ai#step-4-example-use-cases)
- [Additional Use Cases](https://docs.tavily.com/documentation/integrations/pydantic-ai#additional-use-cases)

## [​](https://docs.tavily.com/documentation/integrations/pydantic-ai\#introduction)  Introduction

Integrate [Tavily with Pydantic AI](https://ai.pydantic.dev/common-tools/#tavily-search-tool) to enhance your AI agents with powerful web search capabilities. Pydantic AI provides a framework for building AI agents with tools, making it easy to incorporate real-time web search and data extraction into your applications.

## [​](https://docs.tavily.com/documentation/integrations/pydantic-ai\#step-by-step-integration-guide)  Step-by-Step Integration Guide

### [​](https://docs.tavily.com/documentation/integrations/pydantic-ai\#step-1-install-required-packages)  Step 1: Install Required Packages

Install the necessary Python packages:

Copy

Ask AI

```
pip install "pydantic-ai-slim[tavily]"
```

### [​](https://docs.tavily.com/documentation/integrations/pydantic-ai\#step-2-set-up-api-keys)  Step 2: Set Up API Keys

- **Tavily API Key:** [Get your Tavily API key here](https://app.tavily.com/home)

Set this as an environment variable in your terminal or add it to your environment configuration file:

Copy

Ask AI

```
export TAVILY_API_KEY=your_tavily_api_key
```

### [​](https://docs.tavily.com/documentation/integrations/pydantic-ai\#step-3-initialize-pydantic-ai-agent-with-tavily-tools)  Step 3: Initialize Pydantic AI Agent with Tavily Tools

Copy

Ask AI

```
import os
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

# Get API key from environment
api_key = os.getenv('TAVILY_API_KEY')
assert api_key is not None

# Initialize the agent with Tavily tools
agent = Agent(
    'openai:o3-mini',
    tools=[tavily_search_tool(api_key)],
    system_prompt='Search Tavily for the given query and return the results.'
)
```

### [​](https://docs.tavily.com/documentation/integrations/pydantic-ai\#step-4-example-use-cases)  Step 4: Example Use Cases

Copy

Ask AI

```
# Example 1: Basic search for news
result = agent.run_sync('Tell me the top news in the GenAI world, give me links.')
print(result.output)
```

Example Response:

Copy

Ask AI

```
Here are some of the top recent news articles related to GenAI:

1. How CLEAR users can improve risk analysis with GenAI – Thomson Reuters
   Read more: https://legal.thomsonreuters.com/blog/how-clear-users-can-improve-risk-analysis-with-genai/
   (This article discusses how CLEAR's new GenAI-powered tool streamlines risk analysis by quickly summarizing key information from various public data sources.)

2. TELUS Digital Survey Reveals Enterprise Employees Are Entering Sensitive Data Into AI Assistants More Than You Think – FT.com
   Read more: https://markets.ft.com/data/announce/detail?dockey=600-202502260645BIZWIRE_USPRX____20250226_BW490609-1
   (This news piece highlights findings from a TELUS Digital survey showing that many enterprise employees use public GenAI tools and sometimes even enter sensitive data.)

3. The Essential Guide to Generative AI – Virtualization Review
   Read more: https://virtualizationreview.com/Whitepapers/2025/02/SNOWFLAKE-The-Essential-Guide-to-Generative-AI.aspx
   (This guide provides insights into how GenAI is revolutionizing enterprise strategies and productivity, with input from industry leaders.)
```

## [​](https://docs.tavily.com/documentation/integrations/pydantic-ai\#additional-use-cases)  Additional Use Cases

1. **Content Curation**: Gather and organize information from multiple sources
2. **Real-time Data Integration**: Keep your AI agents up-to-date with the latest information
3. **Technical Documentation**: Search and analyze technical documentation
4. **Market Analysis**: Conduct comprehensive market research and analysis

[Agno\\
\\
Previous](https://docs.tavily.com/documentation/integrations/agno) [FlowiseAI\\
\\
Next](https://docs.tavily.com/documentation/integrations/flowise)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.