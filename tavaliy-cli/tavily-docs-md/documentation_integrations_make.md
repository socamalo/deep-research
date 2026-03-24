Title: Make - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/make
Description: Tavily is now available for no-code integration through Make.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/make#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Make

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

- [Introduction](https://docs.tavily.com/documentation/integrations/make#introduction)
- [How to set up Tavily with Make](https://docs.tavily.com/documentation/integrations/make#how-to-set-up-tavily-with-make)
- [Use cases for Tavily in Make](https://docs.tavily.com/documentation/integrations/make#use-cases-for-tavily-in-make)
- [Detailed example - automated market research](https://docs.tavily.com/documentation/integrations/make#detailed-example-automated-market-research)
- [Best practices](https://docs.tavily.com/documentation/integrations/make#best-practices)

## [​](https://docs.tavily.com/documentation/integrations/make\#introduction)  Introduction

Integrate [Tavily with Make](https://www.make.com/en/integrations/tavily) to enhance your business processes without writing a single line of code. With Tavily’s powerful search and content extraction capabilities, you can seamlessly integrate real-time online information into your Make workflows and automations.

![Make-Tavily](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/make-tavily.gif?s=8c21f3b24b94f8648447746c67f92be6)

## [​](https://docs.tavily.com/documentation/integrations/make\#how-to-set-up-tavily-with-make)  How to set up Tavily with Make

Step 1: Log in to Make

[Log in](https://www.make.com/en/login) to your Make account.

Step 2: Create a New Scenario

Create a new scenario and select a trigger module that will start your workflow.

Step 3: Add Tavily as an Action Module

Add Tavily as an action module in your scenario and choose between **Perform a Search** or **Extract Raw Content**:

**Connection:** Connect your Tavily account by entering your [Tavily API key](https://app.tavily.com/home).

**Configuration:** Set up your parameters:

**For Search:**

- Enter your search `query` (can be manually entered or populated from another module’s output)
- Select a `topic` (`general` or `news`)
- Choose whether to include raw content or generate an answer
- Specify domains to include or exclude
- Set search depth and other optional parameters

**For Extract:**

- Enter the URL(s) to extract content from (can be a single URL or multiple URLs from another module’s output)
- Choose extraction type (`basic` or `advanced`)

**Test:** Run a test to verify your configuration.

Step 4: Process and Use Tavily Results

Utilize the search results in your workflow:

- Process data through additional modules
- Send information to your CRM or database
- Generate reports or notifications
- Feed data into AI models for further processing

## [​](https://docs.tavily.com/documentation/integrations/make\#use-cases-for-tavily-in-make)  Use cases for Tavily in Make

Leverage Tavily’s capabilities to create powerful automated workflows:

- **Competitive Intelligence**: Automatically gather and analyze competitor information
- **Market Research**: Track industry trends and market developments
- **Content Curation**: Collect and organize relevant content for your business
- **Lead Enrichment**: Enhance lead data with real-time information
- **News Monitoring**: Stay updated with the latest developments in your field

## [​](https://docs.tavily.com/documentation/integrations/make\#detailed-example-automated-market-research)  Detailed example - automated market research

Create an automated workflow that performs market research and delivers insights to your team.

Workflow Steps

1. **Trigger:** Schedule the scenario to run daily or weekly
2. **Generate Search Queries:** Use an AI module to create relevant search queries
3. **Execute Searches:** Use Tavily to perform multiple searches with the generated queries
4. **Process Results:** Filter and organize the search results
5. **Generate Report:** Use an AI module to create a comprehensive report
6. **Deliver Insights:** Send the report via email or to your team’s communication platform

## [​](https://docs.tavily.com/documentation/integrations/make\#best-practices)  Best practices

To optimize your Tavily integration in Make:

- Use the Iterator module to process multiple search results efficiently
- Use filters to process only relevant results
- Use the Aggregator module to combine multiple search results

[n8n\\
\\
Previous](https://docs.tavily.com/documentation/integrations/n8n) [OpenAI Agent Builder\\
\\
Next](https://docs.tavily.com/documentation/integrations/agent-builder)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Make-Tavily](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/make-tavily.gif?s=8c21f3b24b94f8648447746c67f92be6)