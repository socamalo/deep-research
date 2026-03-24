Title: CrewAI - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/crewai
Description: Integrate Tavily with CrewAI to build powerful AI agents that can search the web.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/crewai#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

CrewAI

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

- [Introduction](https://docs.tavily.com/documentation/integrations/crewai#introduction)
- [Prerequisites](https://docs.tavily.com/documentation/integrations/crewai#prerequisites)
- [Installation](https://docs.tavily.com/documentation/integrations/crewai#installation)
- [Setup](https://docs.tavily.com/documentation/integrations/crewai#setup)
- [Using Tavily Search with CrewAI](https://docs.tavily.com/documentation/integrations/crewai#using-tavily-search-with-crewai)
- [Customizing search tool parameters](https://docs.tavily.com/documentation/integrations/crewai#customizing-search-tool-parameters)
- [Using Tavily Extract with CrewAI](https://docs.tavily.com/documentation/integrations/crewai#using-tavily-extract-with-crewai)
- [Customizing extract tool parameters](https://docs.tavily.com/documentation/integrations/crewai#customizing-extract-tool-parameters)

## [​](https://docs.tavily.com/documentation/integrations/crewai\#introduction)  Introduction

This guide shows you how to integrate Tavily with CrewAI to create sophisticated AI agents that can search the web and extract content. By combining CrewAI’s multi-agent framework with Tavily’s real-time web search capabilities, you can build AI systems that research, analyze, and process web information autonomously.

## [​](https://docs.tavily.com/documentation/integrations/crewai\#prerequisites)  Prerequisites

Before you begin, make sure you have:

- An OpenAI API key from [OpenAI Platform](https://platform.openai.com/)
- A Tavily API key from [Tavily Dashboard](https://app.tavily.com/sign-in)

## [​](https://docs.tavily.com/documentation/integrations/crewai\#installation)  Installation

Install the required packages:

> **Note:** The stable python versions to use with CrewAI are `Python >=3.10 and Python <3.13` .

Copy

Ask AI

```
pip install 'crewai[tools]'
pip install pydantic
```

## [​](https://docs.tavily.com/documentation/integrations/crewai\#setup)  Setup

Set up your API keys:

Copy

Ask AI

```
import os

# Set your API keys
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["TAVILY_API_KEY"] = "your-tavily-api-key"
```

## [​](https://docs.tavily.com/documentation/integrations/crewai\#using-tavily-search-with-crewai)  Using Tavily Search with CrewAI

CrewAI provides built-in Tavily tools that make it easy to integrate web search capabilities into your AI agents. The `TavilySearchTool` allows your agents to search the web for real-time information.

Copy

Ask AI

```
import os
from crewai import Agent, Task, Crew
from crewai_tools import TavilySearchTool
```

Copy

Ask AI

```
# Initialize the Tavily search tool
tavily_tool = TavilySearchTool()
```

Copy

Ask AI

```
# Create an agent that uses the tool
researcher = Agent(
    role='News Researcher',
    goal='Find trending information about AI agents',
    backstory='An expert News researcher specializing in technology, focused on AI.',
    tools=[tavily_tool],
    verbose=True
)
```

Copy

Ask AI

```
# Create a task for the agent
research_task = Task(
    description='Search for the top 3 Agentic AI trends in 2025.',
    expected_output='A JSON report summarizing the top 3 AI trends found.',
    agent=researcher
)
```

Copy

Ask AI

```
# Form the crew and execute the task
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

result = crew.kickoff()
print(result)
```

### [​](https://docs.tavily.com/documentation/integrations/crewai\#customizing-search-tool-parameters)  Customizing search tool parameters

**Example:**

Copy

Ask AI

```
from crewai_tools import TavilySearchTool

# You can configure the tool with specific parameters
tavily_search_tool = TavilySearchTool(
    search_depth="advanced",
    max_results=10,
    include_answer=True
)
```

You can customize the search tool by passing parameters to configure its behavior.Below are available parameters in crewai integration:**Available Parameters:**

- `query` (str): Required. The search query string.
- `search_depth` (Literal\[“basic”, “advanced”\], optional): The depth of the search. Defaults to “basic”.
- `topic` (Literal\[“general”, “news”, “finance”\], optional): The topic to focus the search on. Defaults to “general”.
- `time_range` (Literal\[“day”, “week”, “month”, “year”\], optional): The time range for the search. Defaults to None.
- `max_results` (int, optional): The maximum number of search results to return. Defaults to 5.
- `include_domains` (Sequence\[str\], optional): A list of domains to prioritize in the search. Defaults to None.
- `exclude_domains` (Sequence\[str\], optional): A list of domains to exclude from the search. Defaults to None.
- `include_answer` (Union\[bool, Literal\[“basic”, “advanced”\]\], optional): Whether to include a direct answer synthesized from the search results. Defaults to False.
- `include_raw_content` (bool, optional): Whether to include the raw HTML content of the searched pages. Defaults to False.
- `include_images` (bool, optional): Whether to include image results. Defaults to False.
- `timeout` (int, optional): The request timeout in seconds. Defaults to 60.

> **Explore More Parameters**: For a complete list of available parameters and their descriptions, visit our [API documentation](https://docs.tavily.com/documentation/api-reference/endpoint/search) to discover all the customization options available for search operations.

Full Code Example - Search

Copy

Ask AI

```
import os
from crewai import Agent, Task, Crew
from crewai_tools import TavilySearchTool

# Set up environment variables
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["TAVILY_API_KEY"] = "your-tavily-api-key"

# Initialize the tool
tavily_tool = TavilySearchTool()

# Create an agent that uses the tool
researcher = Agent(
    role='News Researcher',
    goal='Find trending information about AI agents',
    backstory='An expert News researcher specializing in technology, focused on AI.',
    tools=[tavily_tool],
    verbose=True
)

# Create a task for the agent
research_task = Task(
    description='Search for the top 3 Agentic AI trends in 2025.',
    expected_output='A JSON report summarizing the top 3 AI trends found.',
    agent=researcher
)

# Form the crew and kick it off
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

result = crew.kickoff()
print(result)
```

## [​](https://docs.tavily.com/documentation/integrations/crewai\#using-tavily-extract-with-crewai)  Using Tavily Extract with CrewAI

The `TavilyExtractorTool` allows your CrewAI agents to extract and process content from specific web pages. This is particularly useful for content analysis, data collection, and research tasks.

Copy

Ask AI

```
import os
from crewai import Agent, Task, Crew
from crewai_tools import TavilyExtractorTool
```

Copy

Ask AI

```
# Initialize the Tavily extractor tool
tavily_tool = TavilyExtractorTool()
```

Copy

Ask AI

```
# Create an agent that uses the tool
extractor_agent = Agent(
    role='Web Page Content Extractor',
    goal='Extract key information from the given web pages',
    backstory='You are an expert at extracting relevant content from websites using the Tavily Extract.',
    tools=[tavily_tool],
    verbose=True
)
```

Copy

Ask AI

```
# Define a task for the agent
extract_task = Task(
    description='Extract the main content from the URL https://en.wikipedia.org/wiki/Lionel_Messi .',
    expected_output='A JSON string containing the extracted content from the URL.',
    agent=extractor_agent
)
```

Copy

Ask AI

```
# Create and run the crew
crew = Crew(
    agents=[extractor_agent],
    tasks=[extract_task],
    verbose=False
)

result = crew.kickoff()
print(result)
```

### [​](https://docs.tavily.com/documentation/integrations/crewai\#customizing-extract-tool-parameters)  Customizing extract tool parameters

**Example:**

Copy

Ask AI

```
from crewai_tools import TavilyExtractorTool

# You can configure the tool with specific parameters
tavily_extract_tool = TavilyExtractorTool(
    extract_depth="advanced",
    include_images=True,
    timeout=45
)
```

You can customize the extract tool by passing parameters to configure its behavior. Below are available parameters in crewai integration:**Available Parameters:**

- `urls` (Union\[List\[str\], str\]): Required. A single URL string or a list of URL strings to extract data from.
- `include_images` (Optional\[bool\]): Whether to include images in the extraction results. Defaults to False.
- `extract_depth` (Literal\[“basic”, “advanced”\]): The depth of extraction. Use “basic” for faster, surface-level extraction or “advanced” for more comprehensive extraction. Defaults to “basic”.
- `timeout` (int): The maximum time in seconds to wait for the extraction request to complete. Defaults to 60.

> **Explore More Parameters**: For a complete list of available parameters and their descriptions, visit our [API documentation](https://docs.tavily.com/documentation/api-reference/endpoint/extract) to discover all the customization options available for extract operations.

Full Code Example - Extract

Copy

Ask AI

```
import os
from crewai import Agent, Task, Crew
from crewai_tools import TavilyExtractorTool

# Set up environment variables
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["TAVILY_API_KEY"] = "your-tavily-api-key"

# Initialize the Tavily extractor tool
tavily_tool = TavilyExtractorTool()

# Create an agent that uses the tool
extractor_agent = Agent(
    role='Web Page Content Extractor',
    goal='Extract key information from the given web pages',
    backstory='You are an expert at extracting relevant content from websites using the Tavily Extract.',
    tools=[tavily_tool],
    verbose=True
)

# Define a task for the agent
extract_task = Task(
    description='Extract the main content from the URL https://en.wikipedia.org/wiki/Lionel_Messi .',
    expected_output='A JSON string containing the extracted content from the URL.',
    agent=extractor_agent
)

# Create and execute the crew
crew = Crew(
    agents=[extractor_agent],
    tasks=[extract_task],
    verbose=True
)

# Run the extraction
result = crew.kickoff()
print("Extraction Results:")
print(result)
```

For more information about Tavily’s capabilities, check out our [API documentation](https://docs.tavily.com/documentation/api-reference/introduction) and [best practices](https://docs.tavily.com/documentation/best-practices/best-practices-search).

[FlowiseAI\\
\\
Previous](https://docs.tavily.com/documentation/integrations/flowise) [StackAI\\
\\
Next](https://docs.tavily.com/documentation/integrations/stackai)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.