Title: Langflow - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/langflow
Description: Integrate Tavily with Langflow, an open-source visual framework for building multi-agent and RAG applications.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/langflow#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Langflow

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

- [Introduction](https://docs.tavily.com/documentation/integrations/langflow#introduction)
- [Installation](https://docs.tavily.com/documentation/integrations/langflow#installation)
- [Setting Up Tavily Components in Langflow](https://docs.tavily.com/documentation/integrations/langflow#setting-up-tavily-components-in-langflow)
- [Step 1: Launch Langflow](https://docs.tavily.com/documentation/integrations/langflow#step-1-launch-langflow)
- [Step 2: Using Tavily Components](https://docs.tavily.com/documentation/integrations/langflow#step-2-using-tavily-components)
- [Step 3: Configure Your Tavily API Key](https://docs.tavily.com/documentation/integrations/langflow#step-3-configure-your-tavily-api-key)
- [Example Workflows](https://docs.tavily.com/documentation/integrations/langflow#example-workflows)
- [Basic Search Workflow](https://docs.tavily.com/documentation/integrations/langflow#basic-search-workflow)
- [Content Extraction Workflow](https://docs.tavily.com/documentation/integrations/langflow#content-extraction-workflow)
- [Example Use Cases](https://docs.tavily.com/documentation/integrations/langflow#example-use-cases)
- [Additional Resources](https://docs.tavily.com/documentation/integrations/langflow#additional-resources)

## [​](https://docs.tavily.com/documentation/integrations/langflow\#introduction)  Introduction

Integrate [Tavily with Langflow](https://blog.langflow.org/web-search-in-your-ai-agents-a-langflow-tutorial/) to create powerful AI workflows using a visual interface. Langflow is an open-source tool that provides a visual builder for creating AI agents and workflows, making it easy to incorporate Tavily’s search and extraction capabilities into your applications.

## [​](https://docs.tavily.com/documentation/integrations/langflow\#installation)  Installation

Langflow works with Python 3.10 to 3.13. You can install it using either UV (recommended) or pip:

Copy

Ask AI

```
# Using UV (recommended)
uv pip install langflow

# Using pip
pip install langflow
```

## [​](https://docs.tavily.com/documentation/integrations/langflow\#setting-up-tavily-components-in-langflow)  Setting Up Tavily Components in Langflow

### [​](https://docs.tavily.com/documentation/integrations/langflow\#step-1-launch-langflow)  Step 1: Launch Langflow

After installation, start Langflow:

Copy

Ask AI

```
langflow run
```

This will start the Langflow server locally at `http://localhost:7860`.

### [​](https://docs.tavily.com/documentation/integrations/langflow\#step-2-using-tavily-components)  Step 2: Using Tavily Components

Langflow provides two main Tavily components in the **Tools** section of the components library:

1. **Tavily Search API**: Perform web searches and retrieve relevant information   - Located under Tools > Tavily Search API
   - **Configuration Options**: Select the component and go to “Controls” to access all available settings. Here are some key examples:

     - Max Results: Number of results to return
     - Search Depth: “basic” or “advanced”
     - _Note: Additional parameters are available in the Controls panel_
2. **Tavily Extract API**: Extract content from web pages   - Located under Tools > Tavily Extract API
   - **Configuration Options**: Select the component and go to “Controls” to access all available settings. Here are some key examples:

     - Extract Depth: “basic” or “advanced”
     - _Note: Additional parameters are available in the Controls panel_

### [​](https://docs.tavily.com/documentation/integrations/langflow\#step-3-configure-your-tavily-api-key)  Step 3: Configure Your Tavily API Key

To use Tavily components, you need to enter your [Tavily API key](https://app.tavily.com/home) under “Tavily API Key”

## [​](https://docs.tavily.com/documentation/integrations/langflow\#example-workflows)  Example Workflows

### [​](https://docs.tavily.com/documentation/integrations/langflow\#basic-search-workflow)  Basic Search Workflow

1. Add a Tavily Search component to your flow
2. Connect it to a prompt template
3. Configure the search parameters
4. Add an LLM component to process the results
5. Connect to an output component

### [​](https://docs.tavily.com/documentation/integrations/langflow\#content-extraction-workflow)  Content Extraction Workflow

1. Add a Tavily Extract component
2. Connect it to a URL input
3. Configure extraction parameters
4. Add processing components as needed
5. Connect to your desired output

## [​](https://docs.tavily.com/documentation/integrations/langflow\#example-use-cases)  Example Use Cases

1. **Research Assistant**   - Combine Tavily Search with LLMs for comprehensive research
   - Extract and summarize information from multiple sources
2. **Content Aggregation**   - Use Tavily Extract to gather content from specific websites
   - Process and format the extracted content
3. **Market Intelligence**   - Create workflows for competitive analysis
   - Monitor industry trends and news
4. **Documentation Search**   - Build custom documentation search interfaces
   - Extract and format technical documentation

## [​](https://docs.tavily.com/documentation/integrations/langflow\#additional-resources)  Additional Resources

- [Langflow GitHub Repository](https://github.com/langflow-ai/langflow)
- [Langflow Documentation](https://docs.langflow.org/)

[OpenAI Agent Builder\\
\\
Previous](https://docs.tavily.com/documentation/integrations/agent-builder) [Zapier\\
\\
Next](https://docs.tavily.com/documentation/integrations/zapier)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.