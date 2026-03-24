Title: Tavily Agent Skills - Tavily Docs
URL: https://docs.tavily.com/documentation/agent-skills
Description: Official skills that define best practices for working with the Tavily API. Useful for AI agents like Claude Code, Codex, or Cursor.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/agent-skills#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Tavily Agent Skills

Tavily Agent Skills

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

- [Why Use These Skills?](https://docs.tavily.com/documentation/agent-skills#why-use-these-skills)
- [What You Can Build](https://docs.tavily.com/documentation/agent-skills#what-you-can-build)
- [Installation](https://docs.tavily.com/documentation/agent-skills#installation)
- [Prerequisites](https://docs.tavily.com/documentation/agent-skills#prerequisites)
- [Step 1: Configure Your API Key](https://docs.tavily.com/documentation/agent-skills#step-1-configure-your-api-key)
- [Step 2: Install the Skills](https://docs.tavily.com/documentation/agent-skills#step-2-install-the-skills)
- [Step 3: Restart Your Agent](https://docs.tavily.com/documentation/agent-skills#step-3-restart-your-agent)
- [Available Skills](https://docs.tavily.com/documentation/agent-skills#available-skills)
- [Usage Examples](https://docs.tavily.com/documentation/agent-skills#usage-examples)
- [Automatic Skill Invocation](https://docs.tavily.com/documentation/agent-skills#automatic-skill-invocation)
- [Explicit Skill Invocation](https://docs.tavily.com/documentation/agent-skills#explicit-skill-invocation)
- [Claude Code Plugin](https://docs.tavily.com/documentation/agent-skills#claude-code-plugin)
- [Step 1: Configure Your API Key](https://docs.tavily.com/documentation/agent-skills#step-1-configure-your-api-key-2)
- [Step 2: Install the Skills](https://docs.tavily.com/documentation/agent-skills#step-2-install-the-skills-2)
- [Step 3: Restart Claude Code](https://docs.tavily.com/documentation/agent-skills#step-3-restart-claude-code)

[**GitHub**\\
\\
`/tavily-ai/skills`](https://github.com/tavily-ai/skills) [**Get API Key** \\
\\
Sign up at tavily.com](https://app.tavily.com/)

## [​](https://docs.tavily.com/documentation/agent-skills\#why-use-these-skills)  Why Use These Skills?

These official skills define best practices for working with the Tavily API, going beyond just using the endpoints. They give AI agents low-level control to build custom web tooling directly in your development environment.These skills bring Tavily’s services (search, extract, crawl, research) right where you work. The real-time context these tools provide significantly enhances your agent’s capabilities for development tasks.Most importantly, the **tavily-best-practices** skill turns your AI agent into a true Tavily expert. Instead of reading API docs, just ask your agent how to integrate Tavily into your project. All API best practices are baked in, dramatically accelerating your build process.

## [​](https://docs.tavily.com/documentation/agent-skills\#what-you-can-build)  What You Can Build

Copy-paste these prompts into your AI agent and start building:

AI Chatbot with Real-Time Search

Build a chatbot that can answer questions about current events and up-to-date information.**Try these prompts:**

Copy

Ask AI

```
/tavily-best-practices Build a chatbot that integrates Tavily search to answer questions with up-to-date web information
```

Copy

Ask AI

```
/tavily-best-practices Add Tavily search to my internal company chatbot so it can answer questions about our competitors
```

News Dashboard with Sentiment Analysis

Create a live news dashboard that tracks topics and analyzes sentiment.**Try these prompts:**

Copy

Ask AI

```
/tavily-best-practices Build a website that refreshes daily with Tesla news and gives a sentiment score on each article
```

Copy

Ask AI

```
/tavily-best-practices Create a news monitoring dashboard that tracks AI industry news and sends daily Slack summaries
```

Lead Enrichment Tool

Build tools that automatically enrich leads with company data from the web.**Try these prompts:**

Copy

Ask AI

```
/tavily-best-practices Build a lead enrichment tool that uses Tavily to find company information from their website
```

Copy

Ask AI

```
/tavily-best-practices Create a script that takes a list of company URLs and extracts key business information
```

Competitive Intelligence Agent

Build an autonomous agent that monitors competitors and surfaces insights.**Try these prompts:**

Copy

Ask AI

```
/tavily-best-practices Build a market research tool that crawls competitor documentation and pricing pages
```

Copy

Ask AI

```
/tavily-best-practices Create an agent that monitors competitor product launches and generates weekly reports
```

The `/tavily-best-practices` skill is your fastest path to production. Describe what you want to build and your agent generates working code with best practices baked in.

## [​](https://docs.tavily.com/documentation/agent-skills\#installation)  Installation

### [​](https://docs.tavily.com/documentation/agent-skills\#prerequisites)  Prerequisites

Required

- [Tavily API key](https://app.tavily.com/home) \- Sign up for free
- An AI agent that supports skills (Claude Code, Codex, Cursor, etc.)

### [​](https://docs.tavily.com/documentation/agent-skills\#step-1-configure-your-api-key)  Step 1: Configure Your API Key

Add your Tavily API key to your agent’s environment. For Claude Code, add it to your settings file:

macOS

Linux

Windows

Copy

Ask AI

```
# Open your Claude settings file
open -e "$HOME/.claude/settings.json"

# Or with VS Code
code "$HOME/.claude/settings.json"
```

Add the following configuration:

Copy

Ask AI

```
{
  "env": {
    "TAVILY_API_KEY": "tvly-YOUR_API_KEY"
  }
}
```

Replace `tvly-YOUR_API_KEY` with your actual Tavily API key from [app.tavily.com](https://app.tavily.com/home)

### [​](https://docs.tavily.com/documentation/agent-skills\#step-2-install-the-skills)  Step 2: Install the Skills

Run this command in your terminal:

Copy

Ask AI

```
npx skills add tavily-ai/skills
```

### [​](https://docs.tavily.com/documentation/agent-skills\#step-3-restart-your-agent)  Step 3: Restart Your Agent

After installation, restart your AI agent to load the skills.

## [​](https://docs.tavily.com/documentation/agent-skills\#available-skills)  Available Skills

Tavily Best Practices

Build production-ready Tavily integrations with best practices baked in. Reference documentation for implementing web search, content extraction, crawling, and research in agentic workflows, RAG systems, or autonomous agents.**Invoke explicitly:**

Copy

Ask AI

```
/tavily-best-practices
```

**Example prompts:**

- “Add Tavily search to my internal company chatbot so it can answer questions about our competitors”
- “Build a lead enrichment tool that uses Tavily to find company information from their website”
- “Create a news monitoring agent that tracks mentions of our brand using Tavily search”
- “Implement a RAG pipeline that uses Tavily extract to pull content from industry reports”

Search

Search the web using Tavily’s LLM-optimized search API. Returns relevant results with content snippets, scores, and metadata.**Invoke explicitly:**

Copy

Ask AI

```
/search
```

**Example prompts:**

- “Search for the latest news on AI regulations”
- “/search current React best practices”
- “Search for Python async patterns”

Research

Get AI-synthesized research on any topic with citations. Supports structured JSON output for integration into pipelines.**Invoke explicitly:**

Copy

Ask AI

```
/research
```

**Example prompts:**

- “Research the latest developments in quantum computing”
- “/research AI agent frameworks and save to report.json”
- “Research the competitive landscape for AI coding assistants”

Crawl

Crawl any website and save pages as local markdown files. Ideal for downloading documentation, knowledge bases, or web content for offline access or analysis.**Invoke explicitly:**

Copy

Ask AI

```
/crawl
```

**Example prompts:**

- “Crawl the Stripe API docs and save them locally”
- “/crawl [https://docs.example.com](https://docs.example.com/)”
- “Download the Next.js documentation for offline reference”

Extract

Extract content from specific URLs using Tavily’s extraction API. Returns clean markdown/text from web pages.**Invoke explicitly:**

Copy

Ask AI

```
/extract
```

**Example prompts:**

- “Extract the content from this article URL”
- “/extract [https://example.com/blog/post](https://example.com/blog/post)”
- “Extract content from these three documentation pages”

## [​](https://docs.tavily.com/documentation/agent-skills\#usage-examples)  Usage Examples

### [​](https://docs.tavily.com/documentation/agent-skills\#automatic-skill-invocation)  Automatic Skill Invocation

Your AI agent will automatically use Tavily skills when appropriate. Simply describe what you need:

Copy

Ask AI

```
Research the latest developments in AI agents and summarize the key trends
```

Copy

Ask AI

```
Search for the latest news on AI regulations
```

Copy

Ask AI

```
Crawl the Stripe API docs and save them locally
```

### [​](https://docs.tavily.com/documentation/agent-skills\#explicit-skill-invocation)  Explicit Skill Invocation

You can also invoke skills directly using slash commands:

Copy

Ask AI

```
/research AI agent frameworks and save to report.json
```

Copy

Ask AI

```
/search current React best practices
```

Copy

Ask AI

```
/crawl https://docs.example.com
```

Copy

Ask AI

```
/extract https://example.com/blog/post
```

Copy

Ask AI

```
/tavily-best-practices
```

## [​](https://docs.tavily.com/documentation/agent-skills\#claude-code-plugin)  Claude Code Plugin

If you’re using Claude Code specifically, you can also install the skills as a plugin.

### [​](https://docs.tavily.com/documentation/agent-skills\#step-1-configure-your-api-key-2)  Step 1: Configure Your API Key

Add your Tavily API key to your Claude Code settings file:

Copy

Ask AI

```
code ~/.claude/settings.json
```

Add the following configuration:

Copy

Ask AI

```
{
  "env": {
    "TAVILY_API_KEY": "tvly-YOUR_API_KEY"
  }
}
```

### [​](https://docs.tavily.com/documentation/agent-skills\#step-2-install-the-skills-2)  Step 2: Install the Skills

Run these commands inside Claude Code:

Copy

Ask AI

```
/plugin marketplace add tavily-ai/skills
```

Copy

Ask AI

```
/plugin install tavily@skills
```

### [​](https://docs.tavily.com/documentation/agent-skills\#step-3-restart-claude-code)  Step 3: Restart Claude Code

Clear your session and restart to load the plugin:

Copy

Ask AI

```
/clear
```

Then press `Ctrl+C` to restart.

[Tavily MCP Server\\
\\
Previous](https://docs.tavily.com/documentation/mcp) [Databricks\\
\\
Next](https://docs.tavily.com/documentation/partnerships/databricks)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.