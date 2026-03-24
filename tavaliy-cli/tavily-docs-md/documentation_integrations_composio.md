Title: Composio - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/composio
Description: Tavily is now available for integration through Composio.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/composio#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Composio

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

- [Introduction](https://docs.tavily.com/documentation/integrations/composio#introduction)
- [Step-by-Step Integration Guide](https://docs.tavily.com/documentation/integrations/composio#step-by-step-integration-guide)
- [Step 1: Install Required Packages](https://docs.tavily.com/documentation/integrations/composio#step-1-install-required-packages)
- [Step 2: Set Up API Keys](https://docs.tavily.com/documentation/integrations/composio#step-2-set-up-api-keys)
- [Step 3: Connect Tavily to Composio](https://docs.tavily.com/documentation/integrations/composio#step-3-connect-tavily-to-composio)
- [Step 4: Example Use Case](https://docs.tavily.com/documentation/integrations/composio#step-4-example-use-case)
- [Additional Use Cases](https://docs.tavily.com/documentation/integrations/composio#additional-use-cases)

## [​](https://docs.tavily.com/documentation/integrations/composio\#introduction)  Introduction

Integrate Tavily with Composio to enhance your AI workflows with powerful web search capabilities. Composio provides a platform to connect your AI agents to external tools like Tavily, making it easy to incorporate real-time web search and data extraction into your applications.

## [​](https://docs.tavily.com/documentation/integrations/composio\#step-by-step-integration-guide)  Step-by-Step Integration Guide

### [​](https://docs.tavily.com/documentation/integrations/composio\#step-1-install-required-packages)  Step 1: Install Required Packages

Install the necessary Python packages:

Copy

Ask AI

```
pip install composio composio-openai openai python-dotenv
```

### [​](https://docs.tavily.com/documentation/integrations/composio\#step-2-set-up-api-keys)  Step 2: Set Up API Keys

- **OpenAI API Key:** [Get your OpenAI API key here](https://platform.openai.com/account/api-keys)
- **Composio API Key:** [Get your Composio API key here](https://app.composio.dev/dashboard)

Set these as environment variables in your terminal or add them to your environment configuration file:

Copy

Ask AI

```
export OPENAI_API_KEY=your_openai_api_key
export COMPOSIO_API_KEY=your_composio_api_key
```

### [​](https://docs.tavily.com/documentation/integrations/composio\#step-3-connect-tavily-to-composio)  Step 3: Connect Tavily to Composio

Copy

Ask AI

```
from composio import Composio
from dotenv import load_dotenv

load_dotenv()

composio = Composio()

# Use composio managed auth
auth_config = composio.auth_configs.create(
    toolkit="tavily",
    options={
        "type": "use_custom_auth",
        "auth_scheme": "API_KEY",
        "credentials": {}
    }
)
print(auth_config)
auth_config_id = auth_config.id

user_id = "your-user-id"
connection_request = composio.connected_accounts.link(user_id, auth_config_id)
print(connection_request.redirect_url)
```

### [​](https://docs.tavily.com/documentation/integrations/composio\#step-4-example-use-case)  Step 4: Example Use Case

Copy

Ask AI

```
from composio import Composio
from composio_openai import OpenAIProvider
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize OpenAI client with API key
client = OpenAI()

# Initialize Composio toolset
composio = Composio(
    api_key=os.getenv("COMPOSIO_API_KEY"),
    provider=OpenAIProvider()
)

user_id = "your-user-id"

# Get the Tavily tool with all available parameters
tools = composio.tools.get(user_id,
    toolkits=['TAVILY']
)

# Define the market research task with specific parameters
task = {
    "query": "Analyze the competitive landscape of AI-powered customer service solutions in 2024",
    "search_depth": "advanced",
    "include_answer": True,
    "max_results": 10,
    # Focus on relevant industry sources
    "include_domains": [\
        "techcrunch.com",\
        "venturebeat.com",\
        "forbes.com",\
        "gartner.com",\
        "marketsandmarkets.com"\
    ],
}

# Send request to LLM
messages = [{"role": "user", "content": str(task)}]

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# Handle tool call via Composio
execution_result = None
response_message = response.choices[0].message

if response_message.tool_calls:
    execution_result = composio.provider.handle_tool_calls(user_id,response)
    print("Execution Result:", execution_result)
    messages.append(response_message)

    # Add tool response messages
    for tool_call, result in zip(response_message.tool_calls, execution_result):
        messages.append({
            "role": "tool",
            "content": str(result["data"]),
            "tool_call_id": tool_call.id
        })

    # Get final response from LLM
    final_response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )
    print("\nMarket Research Summary:")
    print(final_response.choices[0].message.content)
else:
    print("LLM responded directly (no tool used):", response_message.content)
```

## [​](https://docs.tavily.com/documentation/integrations/composio\#additional-use-cases)  Additional Use Cases

1. **Research Automation**: Automate the collection and summarization of research data
2. **Content Curation**: Gather and organize information from multiple sources
3. **Real-time Data Integration**: Keeping your AI models up-to-date with the latest information.

[Dify\\
\\
Previous](https://docs.tavily.com/documentation/integrations/dify) [Agno\\
\\
Next](https://docs.tavily.com/documentation/integrations/agno)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.