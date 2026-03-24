Title: Agno - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/agno
Description: Tavily is now available for integration through Agno.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/agno#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Agno

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

- [Introduction](https://docs.tavily.com/documentation/integrations/agno#introduction)
- [Step-by-Step Integration Guide](https://docs.tavily.com/documentation/integrations/agno#step-by-step-integration-guide)
- [Step 1: Install Required Packages](https://docs.tavily.com/documentation/integrations/agno#step-1-install-required-packages)
- [Step 2: Set Up API Keys](https://docs.tavily.com/documentation/integrations/agno#step-2-set-up-api-keys)
- [Step 3: Initialize Agno Agent with Tavily Tools](https://docs.tavily.com/documentation/integrations/agno#step-3-initialize-agno-agent-with-tavily-tools)
- [Step 4: Example Use Cases](https://docs.tavily.com/documentation/integrations/agno#step-4-example-use-cases)
- [Additional Use Cases](https://docs.tavily.com/documentation/integrations/agno#additional-use-cases)

## [​](https://docs.tavily.com/documentation/integrations/agno\#introduction)  Introduction

Integrate [Tavily with Agno](https://docs.agno.com/tools/toolkits/search/tavily#tavily) to enhance your AI agents with powerful web search capabilities. Agno provides a lightweight library for building agents with memory, knowledge, tools, and reasoning, making it easy to incorporate real-time web search and data extraction into your AI applications.

## [​](https://docs.tavily.com/documentation/integrations/agno\#step-by-step-integration-guide)  Step-by-Step Integration Guide

### [​](https://docs.tavily.com/documentation/integrations/agno\#step-1-install-required-packages)  Step 1: Install Required Packages

Install the necessary Python packages:

Copy

Ask AI

```
pip install agno tavily-python
```

### [​](https://docs.tavily.com/documentation/integrations/agno\#step-2-set-up-api-keys)  Step 2: Set Up API Keys

- **Tavily API Key:** [Get your Tavily API key here](https://app.tavily.com/home)
- **OpenAI API Key:** [Get your OpenAI API key here](https://platform.openai.com/account/api-keys)

Set these as environment variables in your terminal or add them to your environment configuration file:

Copy

Ask AI

```
export TAVILY_API_KEY=your_tavily_api_key
export OPENAI_API_KEY=your_openai_api_key
```

### [​](https://docs.tavily.com/documentation/integrations/agno\#step-3-initialize-agno-agent-with-tavily-tools)  Step 3: Initialize Agno Agent with Tavily Tools

Copy

Ask AI

```
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
import os

# Initialize the agent with Tavily tools
agent = Agent(
    tools=[TavilyTools(\
        search=True,                    # Enable search functionality\
        max_tokens=8000,                # Increase max tokens for more detailed results\
        search_depth="advanced",        # Use advanced search for comprehensive results\
        format="markdown"               # Format results as markdown\
    )],
    show_tool_calls=True
)
```

### [​](https://docs.tavily.com/documentation/integrations/agno\#step-4-example-use-cases)  Step 4: Example Use Cases

Copy

Ask AI

```
# Example 1: Basic search with default parameters
agent.print_response("Latest developments in quantum computing", markdown=True)

# Example 2: Market research with multiple parameters
agent.print_response(
    "Analyze the competitive landscape of AI-powered customer service solutions in 2024, "
    "focusing on market leaders and emerging trends",
    markdown=True
)

# Example 3: Technical documentation search
agent.print_response(
    "Find the latest documentation and tutorials about Python async programming, "
    "focusing on asyncio and FastAPI",
    markdown=True
)

# Example 4: News aggregation
agent.print_response(
    "Gather the latest news about artificial intelligence from tech news websites "
    "published in the last week",
    markdown=True
)
```

## [​](https://docs.tavily.com/documentation/integrations/agno\#additional-use-cases)  Additional Use Cases

1. **Content Curation**: Gather and organize information from multiple sources
2. **Real-time Data Integration**: Keep your AI agents up-to-date with the latest information
3. **Technical Documentation**: Search and analyze technical documentation
4. **Market Analysis**: Conduct comprehensive market research and analysis

[Composio\\
\\
Previous](https://docs.tavily.com/documentation/integrations/composio) [Pydantic AI\\
\\
Next](https://docs.tavily.com/documentation/integrations/pydantic-ai)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.