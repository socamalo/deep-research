Title: n8n - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/n8n
Description: Tavily is now available for no-code integration through n8n.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/n8n#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

n8n

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

- [Introduction](https://docs.tavily.com/documentation/integrations/n8n#introduction)
- [How to set up Tavily with n8n](https://docs.tavily.com/documentation/integrations/n8n#how-to-set-up-tavily-with-n8n)
- [Use cases for Tavily in n8n](https://docs.tavily.com/documentation/integrations/n8n#use-cases-for-tavily-in-n8n)
- [Detailed example – Automated job search](https://docs.tavily.com/documentation/integrations/n8n#detailed-example-%E2%80%93-automated-job-search)
- [Best practices](https://docs.tavily.com/documentation/integrations/n8n#best-practices)

## [​](https://docs.tavily.com/documentation/integrations/n8n\#introduction)  Introduction

Integrate Tavily with n8n to enhance your workflows with real-time web search and content extraction—without writing code. With Tavily’s powerful search and extraction capabilities, you can seamlessly integrate up-to-date online information into your n8n automations.

![n8n](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/n8n.gif?s=bb9a9ca58010f04981df615e09d52971)

## [​](https://docs.tavily.com/documentation/integrations/n8n\#how-to-set-up-tavily-with-n8n)  How to set up Tavily with n8n

Step 1: Log in to n8n

[Log in](https://n8n.io/) to your n8n account or self-hosted instance.

Step 2: Create a New Workflow

Create a new workflow and select a trigger node to start your automation.

Step 3: Add Tavily to Your Workflow

**Option 1: Add Tavily as a Node**

In the node library, search for **Tavily**. Add it to your workflow and choose between **Search** or **Extract** actions.

**Option 2: Add Tavily as a Tool to an AI Agent**

If you are building an AI agent workflow, you can add Tavily as a tool to your agent. This allows your agent to use Tavily for web search or content extraction as part of its reasoning process.

**Connection:** Connect your Tavily account by entering your [Tavily API key](https://app.tavily.com/home).

**Configuration:** Set up your parameters:

**For Search:**

- Enter your search `query` (can be manually entered or populated from another node’s output)
- Select a `topic` (“general” or “news”)
- Choose whether to include raw content or generate an answer
- Specify domains to include or exclude
- Set search depth and other optional parameters

**For Extract:**

- Enter the URL(s) to extract content from (can be a single URL or multiple URLs from another node’s output)
- Choose extraction type (“basic” or “advanced”)

**Test:** Run a test to verify your configuration.

Step 4: Process and Use Tavily Results

Utilize the search or extraction results in your workflow:

- Process data through additional nodes
- Send information to your CRM, database, or email
- Generate reports or notifications
- Feed data into AI models for further processing

## [​](https://docs.tavily.com/documentation/integrations/n8n\#use-cases-for-tavily-in-n8n)  Use cases for Tavily in n8n

Leverage Tavily’s capabilities to create powerful automated workflows:

- **Job Search Automation**: Find and summarize new job postings, then send results to your inbox
- **Competitive Intelligence**: Automatically gather and analyze competitor information
- **Market Research**: Track industry trends and market developments
- **Content Curation**: Collect and organize relevant content for your business
- **Lead Enrichment**: Enhance lead data with real-time information
- **News Monitoring**: Stay updated with the latest developments in your field

## [​](https://docs.tavily.com/documentation/integrations/n8n\#detailed-example-%E2%80%93-automated-job-search)  Detailed example – Automated job search

Create an automated workflow that uses an AI agent with Tavily as a tool for web search to find new “Software Engineering Intern Roles” on the web, summarizes the results, and sends them to your email.

Workflow Steps

1. **Trigger:** Schedule the workflow to run daily or weekly
2. **AI Agent:** Add an AI agent node to your workflow
3. **Add Tavily as a Tool:** In the AI agent configuration, add Tavily as a tool for web search
4. **Search:** The AI agent uses Tavily to find new “Software Engineering Intern Roles”
5. **Summarize:** The AI agent summarizes the search results using its LLM capabilities
6. **Email:** Use the Email node to send the summarized results to your inbox

## [​](https://docs.tavily.com/documentation/integrations/n8n\#best-practices)  Best practices

To optimize your Tavily integration in n8n:

- Use the SplitInBatches node to process multiple search results efficiently
- Use filters to process only relevant results
- Use the Merge node to combine multiple search results

[Anthropic\\
\\
Previous](https://docs.tavily.com/documentation/integrations/anthropic) [Make\\
\\
Next](https://docs.tavily.com/documentation/integrations/make)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![n8n](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/n8n.gif?s=bb9a9ca58010f04981df615e09d52971)