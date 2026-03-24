Title: OpenAI Agent Builder - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/agent-builder
Description: Integrate OpenAI’s Agent Builder with Tavily’s MCP server to empower your AI agents with real-time web access.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/agent-builder#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

OpenAI Agent Builder

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

- [Getting Started](https://docs.tavily.com/documentation/integrations/agent-builder#getting-started)
- [Real-World Applications](https://docs.tavily.com/documentation/integrations/agent-builder#real-world-applications)
- [Market Research Agents](https://docs.tavily.com/documentation/integrations/agent-builder#market-research-agents)
- [Content Curation Systems](https://docs.tavily.com/documentation/integrations/agent-builder#content-curation-systems)
- [Competitive Intelligence](https://docs.tavily.com/documentation/integrations/agent-builder#competitive-intelligence)
- [News & Event Monitors](https://docs.tavily.com/documentation/integrations/agent-builder#news-%26-event-monitors)

## [​](https://docs.tavily.com/documentation/integrations/agent-builder\#getting-started)  Getting Started

Before you begin, make sure you have:

- A [Tavily API key](https://app.tavily.com/home) (sign up for free if you don’t have one)
- An OpenAI account with [organization verification](https://help.openai.com/en/articles/10910291-api-organization-verification)

1

[Navigate to header](https://docs.tavily.com/documentation/integrations/agent-builder#)

Create a new workflow in Agent Builder

Navigate to [Agent Builder](https://platform.openai.com/agent-builder) and click **Create New Workflow** to begin building your AI agent.![Create New Workflow](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=d032fb19494be5ccd0c516de7bfc1b4d)

2

[Navigate to header](https://docs.tavily.com/documentation/integrations/agent-builder#)

Select the agent node in your workflow

Click on the agent node in your workflow canvas to open the configuration panel.![Agent Block](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=5b1b592b5b703df7f85a26626c05dc4d)

3

[Navigate to header](https://docs.tavily.com/documentation/integrations/agent-builder#)

Open the Tools configuration

In the configuration panel, locate and click on **Tools** in the sidebar to add external capabilities to your agent.![Tools Panel](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=18bf6ac9a2dda471ef124ef7f21216fc)

4

[Navigate to header](https://docs.tavily.com/documentation/integrations/agent-builder#)

Connect Tavily's MCP server

In the MCP configuration section, paste the Tavily MCP server URL:

Copy

Ask AI

```
https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_API_KEY
```

Remember to replace `YOUR_API_KEY` with your actual Tavily API key.

Need an API key? Get one instantly from your [Tavily\\
dashboard](https://app.tavily.com/home)

Click **Connect** to establish the connection to Tavily.![Tavily MCP Configuration](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=2f39df29a22f845ed5d2f9bf7883d0fd)

5

[Navigate to header](https://docs.tavily.com/documentation/integrations/agent-builder#)

Enable Tavily capabilities for your agent

Once connected, you’ll see Tavily’s suite of tools available:

- **tavily\_search** \- Execute a search query.
- **tavily\_extract** \- Extract web page content from one or more specified URLs.
- **tavily\_map** \- Traverses websites like a graph and can explore hundreds of paths in parallel with intelligent discovery to generate comprehensive site maps.
- **tavily\_crawl** \- Traversal tool that can explore hundreds of paths in parallel with built-in extraction and intelligent discovery.

Select the tools you want to activate for this agent, then click **Add** to integrate them.![Tavily Tools Available](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=d9e0d214e5b6c0d9c0ab3943289d6729)

6

[Navigate to header](https://docs.tavily.com/documentation/integrations/agent-builder#)

Customize your agent's behavior

Now configure your agent:

- **Name**: Choose a descriptive name for your agent
- **Instructions**: Define the agent’s role and how it should use Tavily’s tools
- **Reasoning**: Set the appropriate reasoning effort level
- Click **Preview** to test the configuration

**Sample instructions:**

Copy

Ask AI

```
You are a research assistant that uses Tavily to search the web for up-to-date information.
When the user asks questions that require current information, use Tavily to find relevant and recent sources.
```

![Agent Configuration Panel](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=899b9db4ad2c6f8e785ef24dcdf17bbc)

7

[Navigate to header](https://docs.tavily.com/documentation/integrations/agent-builder#)

Verify your agent works correctly

Test your agent with queries that require real-time information to verify everything is working as expected.![Agent Testing Interface](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=6b2dca8e3bb276e711fd5e09b5fa5e63)

## [​](https://docs.tavily.com/documentation/integrations/agent-builder\#real-world-applications)  Real-World Applications

### [​](https://docs.tavily.com/documentation/integrations/agent-builder\#market-research-agents)  Market Research Agents

Build agents that continuously monitor industry trends, competitor activities, and market sentiment by searching for and analyzing relevant business information.

### [​](https://docs.tavily.com/documentation/integrations/agent-builder\#content-curation-systems)  Content Curation Systems

Create agents that automatically find, extract, and summarize content from multiple sources based on your specific criteria and preferences.

### [​](https://docs.tavily.com/documentation/integrations/agent-builder\#competitive-intelligence)  Competitive Intelligence

Develop agents that crawl competitor websites, map their content strategies, and extract pricing, features, and positioning information.

### [​](https://docs.tavily.com/documentation/integrations/agent-builder\#news-&-event-monitors)  News & Event Monitors

Build agents that track breaking news on specific topics by leveraging Tavily’s news search mode, providing real-time updates with citations.

[Make\\
\\
Previous](https://docs.tavily.com/documentation/integrations/make) [Langflow\\
\\
Next](https://docs.tavily.com/documentation/integrations/langflow)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Create New Workflow](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/create-workflow.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=ba9864ddc063f9ef3f58d9c77b170d84)

![Agent Block](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-node.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=5bd15c7f863307d449fc53ce49f28be6)

![Tools Panel](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-tool.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=e0d2bd554ddb3a34f9803af07844868b)

![Tavily MCP Configuration](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=1fd82ede8766b583ac66386545cfb5f3)

![Tavily Tools Available](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/tavily-mcp-tools.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=8a7085f7335e901d1186c5dffdee1089)

![Agent Configuration Panel](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/agent-config.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=10364283f2a50fe29fee45df5c89447b)

![Agent Testing Interface](https://mintcdn.com/tavilyai/L1kzPmnTqAHnyyDl/images/test-agent.png?w=840&fit=max&auto=format&n=L1kzPmnTqAHnyyDl&q=85&s=20d40de348c4941ef95ad9c97f6531ad)