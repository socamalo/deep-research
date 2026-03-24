Title: Vercel AI SDK - Tavily Docs
URL: https://docs.tavily.com/documentation/integrations/vercel
Description: Integrate Tavily with Vercel AI SDK to enhance your AI agents with powerful web search, content extraction, crawling, and site mapping capabilities.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/integrations/vercel#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Integrations

Vercel AI SDK

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

- [Introduction](https://docs.tavily.com/documentation/integrations/vercel#introduction)
- [Step-by-Step Integration Guide](https://docs.tavily.com/documentation/integrations/vercel#step-by-step-integration-guide)
- [Step 1: Install Required Packages](https://docs.tavily.com/documentation/integrations/vercel#step-1-install-required-packages)
- [Step 2: Set Up API Keys](https://docs.tavily.com/documentation/integrations/vercel#step-2-set-up-api-keys)
- [Step 3: Basic Usage](https://docs.tavily.com/documentation/integrations/vercel#step-3-basic-usage)
- [Available Tools](https://docs.tavily.com/documentation/integrations/vercel#available-tools)
- [Tavily Search](https://docs.tavily.com/documentation/integrations/vercel#tavily-search)
- [Tavily Extract](https://docs.tavily.com/documentation/integrations/vercel#tavily-extract)
- [Tavily Crawl](https://docs.tavily.com/documentation/integrations/vercel#tavily-crawl)
- [Tavily Map](https://docs.tavily.com/documentation/integrations/vercel#tavily-map)
- [Using Multiple Tools Together](https://docs.tavily.com/documentation/integrations/vercel#using-multiple-tools-together)
- [Advanced Examples](https://docs.tavily.com/documentation/integrations/vercel#advanced-examples)
- [News Research with Time Range](https://docs.tavily.com/documentation/integrations/vercel#news-research-with-time-range)
- [Market Analysis with Advanced Search](https://docs.tavily.com/documentation/integrations/vercel#market-analysis-with-advanced-search)
- [Benefits of Tavily + Vercel AI SDK](https://docs.tavily.com/documentation/integrations/vercel#benefits-of-tavily-%2B-vercel-ai-sdk)

## [​](https://docs.tavily.com/documentation/integrations/vercel\#introduction)  Introduction

The `@tavily/ai-sdk` package provides pre-built AI SDK tools for Vercel’s AI SDK v5, making it easy to add real-time web search, content extraction, intelligent crawling, and site mapping to your AI applications.

## [​](https://docs.tavily.com/documentation/integrations/vercel\#step-by-step-integration-guide)  Step-by-Step Integration Guide

### [​](https://docs.tavily.com/documentation/integrations/vercel\#step-1-install-required-packages)  Step 1: Install Required Packages

Install the necessary packages:

Copy

Ask AI

```
npm install ai @ai-sdk/openai @tavily/ai-sdk
```

### [​](https://docs.tavily.com/documentation/integrations/vercel\#step-2-set-up-api-keys)  Step 2: Set Up API Keys

- **Tavily API Key:** [Get your Tavily API key here](https://app.tavily.com/home)
- **OpenAI API Key:** [Get your OpenAI API key here](https://platform.openai.com/account/api-keys)

Set these as environment variables:

Copy

Ask AI

```
export TAVILY_API_KEY=tvly-your-api-key
export OPENAI_API_KEY=your-openai-api-key
```

### [​](https://docs.tavily.com/documentation/integrations/vercel\#step-3-basic-usage)  Step 3: Basic Usage

The simplest way to get started with Tavily Search:

Copy

Ask AI

```
import { tavilySearch } from "@tavily/ai-sdk";
import { generateText, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";

const result = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "What are the latest developments in quantum computing?",
  tools: {
    tavilySearch: tavilySearch(),
  },
  stopWhen: stepCountIs(3),
});

console.log(result.text);
```

## [​](https://docs.tavily.com/documentation/integrations/vercel\#available-tools)  Available Tools

### [​](https://docs.tavily.com/documentation/integrations/vercel\#tavily-search)  Tavily Search

Real-time web search optimized for AI applications:

Copy

Ask AI

```
import { tavilySearch } from "@tavily/ai-sdk";
import { generateText, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";

const result = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "Research the latest trends in renewable energy technology",
  tools: {
    tavilySearch: tavilySearch({
      searchDepth: "advanced",
      includeAnswer: true,
      maxResults: 5,
      topic: "general",
    }),
  },
  stopWhen: stepCountIs(3),
});
```

**Key Configuration Options:**

- `searchDepth?: "basic" | "advanced"` \- Search depth (default: “basic”)
- `topic?: "general" | "news" | "finance"` \- Search category
- `includeAnswer?: boolean` \- Include AI-generated answer
- `maxResults?: number` \- Maximum results to return (default: 5)
- `includeImages?: boolean` \- Include images in results
- `timeRange?: "year" | "month" | "week" | "day"` \- Time range for results
- `includeDomains?: string[]` \- Domains to include
- `excludeDomains?: string[]` \- Domains to exclude

### [​](https://docs.tavily.com/documentation/integrations/vercel\#tavily-extract)  Tavily Extract

Clean, structured content extraction from URLs:

Copy

Ask AI

```
import { tavilyExtract } from "@tavily/ai-sdk";
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

const result = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "Extract and summarize the content from https://tavily.com",
  tools: {
    tavilyExtract: tavilyExtract(),
  },
});
```

**Key Configuration Options:**

- `extractDepth?: "basic" | "advanced"` \- Extraction depth
- `format?: "markdown" | "text"` \- Output format (default: “markdown”)
- `includeImages?: boolean` \- Include images in extracted content

### [​](https://docs.tavily.com/documentation/integrations/vercel\#tavily-crawl)  Tavily Crawl

Intelligent website crawling at scale:

Copy

Ask AI

```
import { tavilyCrawl } from "@tavily/ai-sdk";
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

const result = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "Crawl tavily.com and tell me about their integrations",
  tools: {
    tavilyCrawl: tavilyCrawl({
      maxDepth: 2,
      limit: 50,
    }),
  },
});
```

**Key Configuration Options:**

- `maxDepth?: number` \- Maximum crawl depth (1-5, default: 1)
- `maxBreadth?: number` \- Maximum pages per depth level (1-100, default: 20)
- `limit?: number` \- Maximum total pages to crawl (default: 50)
- `extractDepth?: "basic" | "advanced"` \- Content extraction depth
- `instructions?: string` \- Natural language crawling instructions
- `selectPaths?: string[]` \- Path patterns to include
- `excludePaths?: string[]` \- Path patterns to exclude
- `allowExternal?: boolean` \- Allow crawling external domains

### [​](https://docs.tavily.com/documentation/integrations/vercel\#tavily-map)  Tavily Map

Website structure discovery and mapping:

Copy

Ask AI

```
import { tavilyMap } from "@tavily/ai-sdk";
import { generateText, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";

const result = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "Map the structure of tavily.com",
  tools: {
    tavilyMap: tavilyMap(),
  },
  stopWhen: stepCountIs(3),
});
```

**Key Configuration Options:**

- `maxDepth?: number` \- Maximum mapping depth (1-5, default: 1)
- `maxBreadth?: number` \- Maximum pages per depth level (1-100, default: 20)
- `limit?: number` \- Maximum total pages to map (default: 50)
- `instructions?: string` \- Natural language mapping instructions
- `selectPaths?: string[]` \- Path patterns to include
- `excludePaths?: string[]` \- Path patterns to exclude
- `allowExternal?: boolean` \- Allow mapping external domains

## [​](https://docs.tavily.com/documentation/integrations/vercel\#using-multiple-tools-together)  Using Multiple Tools Together

You can combine multiple Tavily tools in a single AI agent for comprehensive research capabilities:

Copy

Ask AI

```
import {
  tavilySearch,
  tavilyExtract,
  tavilyCrawl,
  tavilyMap
} from "@tavily/ai-sdk";
import { generateText, stepCountIs } from "ai";
import { openai } from "@ai-sdk/openai";

const result = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "Research the company at tavily.com - search for news, map their site, and extract key pages",
  tools: {
    tavilySearch: tavilySearch({ searchDepth: "advanced" }),
    tavilyExtract: tavilyExtract(),
    tavilyCrawl: tavilyCrawl(),
    tavilyMap: tavilyMap(),
  },
  stopWhen: stepCountIs(5),
});
```

## [​](https://docs.tavily.com/documentation/integrations/vercel\#advanced-examples)  Advanced Examples

### [​](https://docs.tavily.com/documentation/integrations/vercel\#news-research-with-time-range)  News Research with Time Range

Copy

Ask AI

```
const newsResult = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "What are the top technology news stories from this week?",
  tools: {
    tavilySearch: tavilySearch({
      topic: "news",
      timeRange: "week",
      maxResults: 10,
    }),
  },
  stopWhen: stepCountIs(3),
});
```

### [​](https://docs.tavily.com/documentation/integrations/vercel\#market-analysis-with-advanced-search)  Market Analysis with Advanced Search

Copy

Ask AI

```
const marketResult = await generateText({
  model: openai("gpt-5-mini"),
  prompt: "Analyze the current state of the electric vehicle market",
  tools: {
    tavilySearch: tavilySearch({
      searchDepth: "advanced",
      topic: "finance",
      includeAnswer: true,
      maxResults: 10,
    }),
  },
  stopWhen: stepCountIs(5),
});
```

## [​](https://docs.tavily.com/documentation/integrations/vercel\#benefits-of-tavily-+-vercel-ai-sdk)  Benefits of Tavily + Vercel AI SDK

- **Pre-built Tools:** No need to manually create tool definitions - just import and use
- **Type-Safe:** Full TypeScript support with proper type definitions
- **Real-time Information:** Access up-to-date web content for your AI agents
- **Optimized for LLMs:** Search results are specifically formatted for language models
- **Multiple Capabilities:** Search, extract, crawl, and map websites - all in one package
- **Easy Integration:** Works seamlessly with Vercel AI SDK v5
- **Flexible Configuration:** Extensive configuration options for all tools
- **Production-Ready:** Built on the reliable Tavily API infrastructure

[LangChain\\
\\
Previous](https://docs.tavily.com/documentation/integrations/langchain) [LlamaIndex\\
\\
Next](https://docs.tavily.com/documentation/integrations/llamaindex)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.