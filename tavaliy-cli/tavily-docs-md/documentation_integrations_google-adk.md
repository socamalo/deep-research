Title: Google ADK - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/google-adk
Description: Connect your Google ADK agent to Tavily's AI-focused search, extraction, and crawling platform for real-time web intelligence.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/google-adk#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Google ADK

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

- [Introduction](https://docs.tavily.com/documentation/integrations/google-adk#introduction)
- [Prerequisites](https://docs.tavily.com/documentation/integrations/google-adk#prerequisites)
- [Installation](https://docs.tavily.com/documentation/integrations/google-adk#installation)
- [Building Your Agent](https://docs.tavily.com/documentation/integrations/google-adk#building-your-agent)
- [Step 1: Create an Agent Project](https://docs.tavily.com/documentation/integrations/google-adk#step-1-create-an-agent-project)
- [Step 2: Update Your Agent Code](https://docs.tavily.com/documentation/integrations/google-adk#step-2-update-your-agent-code)
- [Step 3: Set Your API Keys](https://docs.tavily.com/documentation/integrations/google-adk#step-3-set-your-api-keys)
- [Step 4: Run Your Agent](https://docs.tavily.com/documentation/integrations/google-adk#step-4-run-your-agent)
- [Run with Command-Line Interface](https://docs.tavily.com/documentation/integrations/google-adk#run-with-command-line-interface)
- [Run with Web Interface](https://docs.tavily.com/documentation/integrations/google-adk#run-with-web-interface)
- [Example Usage](https://docs.tavily.com/documentation/integrations/google-adk#example-usage)
- [Available Tools](https://docs.tavily.com/documentation/integrations/google-adk#available-tools)
- [tavily-search](https://docs.tavily.com/documentation/integrations/google-adk#tavily-search)
- [tavily-extract](https://docs.tavily.com/documentation/integrations/google-adk#tavily-extract)
- [tavily-map](https://docs.tavily.com/documentation/integrations/google-adk#tavily-map)
- [tavily-crawl](https://docs.tavily.com/documentation/integrations/google-adk#tavily-crawl)

## [​](https://docs.tavily.com/documentation/integrations/google-adk\#introduction)  Introduction

The Tavily MCP Server connects your ADK agent to Tavily’s AI-focused search, extraction, and crawling platform. This gives your agent the ability to perform real-time web searches, intelligently extract specific data from web pages, and crawl or create structured maps of websites.

## [​](https://docs.tavily.com/documentation/integrations/google-adk\#prerequisites)  Prerequisites

Before you begin, make sure you have:

- Python 3.9 or later
- pip for installing packages
- A [Tavily API key](https://app.tavily.com/home) (sign up for free if you don’t have one)
- A [Gemini API key](https://aistudio.google.com/app/apikey) for Google AI Studio

## [​](https://docs.tavily.com/documentation/integrations/google-adk\#installation)  Installation

Install ADK by running:

Copy

Ask AI

```
pip install google-adk mcp
```

## [​](https://docs.tavily.com/documentation/integrations/google-adk\#building-your-agent)  Building Your Agent

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#step-1-create-an-agent-project)  Step 1: Create an Agent Project

Run the `adk create` command to start a new agent project:

Copy

Ask AI

```
adk create my_agent
```

This creates a new directory with the following structure:

Copy

Ask AI

```
my_agent/
    agent.py      # main agent code
    .env          # API keys or project IDs
    __init__.py
```

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#step-2-update-your-agent-code)  Step 2: Update Your Agent Code

Edit the `my_agent/agent.py` file to integrate Tavily. Choose either **Remote MCP Server** or **Local MCP Server**:

Remote MCP Server

Local MCP Server

Copy

Ask AI

```
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
import os

# Get API key from environment
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

root_agent = Agent(
    model="gemini-2.5-pro",
    name="tavily_agent",
    instruction="You are a helpful assistant that uses Tavily to search the web, extract content, and explore websites. Use Tavily's tools to provide up-to-date information to users.",
    tools=[\
        MCPToolset(\
            connection_params=StreamableHTTPServerParams(\
                url="https://mcp.tavily.com/mcp/",\
                headers={\
                    "Authorization": f"Bearer {TAVILY_API_KEY}",\
                },\
            ),\
        )\
    ],
)
```

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#step-3-set-your-api-keys)  Step 3: Set Your API Keys

Update the `my_agent/.env` file with your API keys:

Copy

Ask AI

```
echo 'GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"' >> my_agent/.env
echo 'TAVILY_API_KEY="YOUR_TAVILY_API_KEY"' >> my_agent/.env
```

Or manually edit the `.env` file:

Copy

Ask AI

```
GOOGLE_API_KEY="your_gemini_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
```

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#step-4-run-your-agent)  Step 4: Run Your Agent

You can run your ADK agent in two ways:

#### [​](https://docs.tavily.com/documentation/integrations/google-adk\#run-with-command-line-interface)  Run with Command-Line Interface

Run your agent using the `adk run` command:

Copy

Ask AI

```
adk run my_agent
```

This starts an interactive command-line interface where you can chat with your agent and test Tavily’s capabilities.

#### [​](https://docs.tavily.com/documentation/integrations/google-adk\#run-with-web-interface)  Run with Web Interface

Start the ADK web interface for a visual testing experience:

Copy

Ask AI

```
adk web --port 8000
```

**Note:** Run this command from the parent directory that contains your `my_agent/` folder. For example, if your agent is inside `agents/my_agent/`, run `adk web` from the `agents/` directory.This starts a web server with a chat interface. Access it at `http://localhost:8000`, select your agent from the dropdown, and start chatting.

## [​](https://docs.tavily.com/documentation/integrations/google-adk\#example-usage)  Example Usage

Once your agent is set up and running, you can interact with it through the command-line interface or web interface. Here’s a simple example:**User Query:**

Copy

Ask AI

```
Find all documentation pages on tavily.com and provide instructions on how to get started with Tavily
```

The agent automatically combines multiple Tavily tools to provide comprehensive answers, making it easy to explore websites and gather information without manual navigation.![Tavily-ADK](https://mintcdn.com/tavilyai/6_GM_pQOTDBhyG2t/images/google-adk.png?fit=max&auto=format&n=6_GM_pQOTDBhyG2t&q=85&s=32daff4af3598c46f1bedae141666bc9)

## [​](https://docs.tavily.com/documentation/integrations/google-adk\#available-tools)  Available Tools

Once connected, your agent gains access to Tavily’s powerful web intelligence tools:

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#tavily-search)  tavily-search

Execute a search query to find relevant information across the web.

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#tavily-extract)  tavily-extract

Extract structured data from any web page. Extract text, links, and images from single pages or batch process multiple URLs efficiently.

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#tavily-map)  tavily-map

Traverses websites like a graph and can explore hundreds of paths in parallel with intelligent discovery to generate comprehensive site maps.

### [​](https://docs.tavily.com/documentation/integrations/google-adk\#tavily-crawl)  tavily-crawl

Traversal tool that can explore hundreds of paths in parallel with built-in extraction and intelligent discovery.

[OpenAI\\
\\
Previous](https://docs.tavily.com/documentation/integrations/openai) [Anthropic\\
\\
Next](https://docs.tavily.com/documentation/integrations/anthropic)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Tavily-ADK](https://mintcdn.com/tavilyai/6_GM_pQOTDBhyG2t/images/google-adk.png?w=840&fit=max&auto=format&n=6_GM_pQOTDBhyG2t&q=85&s=2ac15ad4b9b3a9708f51a3fafb1cfc60)