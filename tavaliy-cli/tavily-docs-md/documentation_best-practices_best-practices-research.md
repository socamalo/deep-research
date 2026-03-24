Title: Best Practices for Research - Tavily Docs
URL: https://docs.tavily.com/documentation/best-practices/best-practices-research
Description: Learn how to write effective prompts, choose the right model, and configure output formats for better research results.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/best-practices/best-practices-research#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Best Practices

Best Practices for Research

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### API Reference

- [Introduction](https://docs.tavily.com/documentation/api-reference/introduction)
- [POST\\
\\
Search](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [POST\\
\\
Extract](https://docs.tavily.com/documentation/api-reference/endpoint/extract)
- [POST\\
\\
Crawl](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)
- [POST\\
\\
Map](https://docs.tavily.com/documentation/api-reference/endpoint/map)
- Research

- [GET\\
\\
Usage](https://docs.tavily.com/documentation/api-reference/endpoint/usage)

##### Python SDK

- [Quickstart](https://docs.tavily.com/sdk/python/quick-start)
- [SDK Reference](https://docs.tavily.com/sdk/python/reference)

##### JavaScript SDK

- [Quickstart](https://docs.tavily.com/sdk/javascript/quick-start)
- [SDK Reference](https://docs.tavily.com/sdk/javascript/reference)

##### Best Practices

- [Search](https://docs.tavily.com/documentation/best-practices/best-practices-search)
- [Extract](https://docs.tavily.com/documentation/best-practices/best-practices-extract)
- [Crawl](https://docs.tavily.com/documentation/best-practices/best-practices-crawl)
- [Research](https://docs.tavily.com/documentation/best-practices/best-practices-research)
- [API Key Management](https://docs.tavily.com/documentation/best-practices/api-key-management)

On this page

- [Prompting](https://docs.tavily.com/documentation/best-practices/best-practices-research#prompting)
- [Example Queries](https://docs.tavily.com/documentation/best-practices/best-practices-research#example-queries)
- [Model](https://docs.tavily.com/documentation/best-practices/best-practices-research#model)
- [Pro](https://docs.tavily.com/documentation/best-practices/best-practices-research#pro)
- [Mini](https://docs.tavily.com/documentation/best-practices/best-practices-research#mini)
- [Structured Output vs. Report](https://docs.tavily.com/documentation/best-practices/best-practices-research#structured-output-vs-report)
- [Formatting Your Schema](https://docs.tavily.com/documentation/best-practices/best-practices-research#formatting-your-schema)
- [Streaming vs. Polling](https://docs.tavily.com/documentation/best-practices/best-practices-research#streaming-vs-polling)

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#prompting)  Prompting

Define a **clear goal** with all **details** and **direction**.

- **Be specific when you can.** If you already know important details, include them.


(E.g. Target market or industry, key competitors, customer segments, geography, or constraints)
- **Only stay open-ended if you don’t know details and want discovery.** If you’re exploring broadly, make that explicit (e.g., “tell me about the most impactful AI innovations in healthcare in 2025”).
- **Avoid contradictions.** Don’t include conflicting information, constraints, or goals in your prompt.
- **Share what’s already known.** Include prior assumptions, existing decisions, or baseline knowledge—so the research doesn’t repeat what you already have.
- **Keep the prompt clean and directed.** Use a clear task statement + essential context + desired output format. Avoid messy background dumps.

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#example-queries)  Example Queries

Copy

Ask AI

```
"Research the company ____ and it's 2026 outlook. Provide a brief
overview of the company, its products, services, and market position."
```

Copy

Ask AI

```
"Conduct a competitive analysis of ____ in 2026. Identify their main competitors,
compare market positioning, and analyze key differentiators."
```

Copy

Ask AI

```
"We're evaluating Notion as a potential partner. We already know they primarily
serve SMB and mid-market teams, expanded their AI features significantly in 2025,
and most often compete with Confluence and ClickUp. Research Notion's 2026 outlook,
including market position, growth risks, and where a partnership could be most
valuable. Include citations."
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#model)  Model

| Model | Best For |
| --- | --- |
| `pro` | Comprehensive, multi-agent research for complex, multi-domain topics |
| `mini` | Targeted, efficient research for narrow or well-scoped questions |
| `auto` | When you’re unsure how complex research will be |

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#pro)  Pro

Provides comprehensive, multi-agent research suited for complex topics that span multiple subtopics or domains. Use when you want deeper analysis, more thorough reports, or maximum accuracy.

Copy

Ask AI

```
{
  "input": "Analyze the competitive landscape for ____ in the SMB market, including key competitors, positioning, pricing models, customer segments, recent product moves, and where ____ has defensible advantages or risks over the next 2–3 years.",
  "model": "pro"
}
```

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#mini)  Mini

Optimized for targeted, efficient research. Works best for narrow or well-scoped questions where you still benefit from agentic searching and synthesis, but don’t need extensive depth.

Copy

Ask AI

```
{
  "input": "What are the top 5 competitors to ____ in the SMB market, and how do they differentiate?",
  "model": "mini"
}
```

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#structured-output-vs-report)  Structured Output vs. Report

- **Structured Output** \- Best for data enrichment, pipelines, or powering UIs with specific fields.
- **Report** — Best for reading, sharing, or displaying verbatim (e.g., chat interfaces, briefs, newsletters).

### [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#formatting-your-schema)  Formatting Your Schema

- **Write clear field descriptions.** In 1–3 sentences, say exactly what the field should contain and what to look for. This makes it easier for our models to interpret what you’re looking for.
- **Match the structure you actually need.** Use the right types (arrays, objects, enums) instead of packing multiple values into one string (e.g., `competitors: string[]`, not `"A, B, C"`).
- **Avoid duplicate or overlapping fields.** Keep each field unique and specific - contradictions or redundancy can confuse our models.

## [​](https://docs.tavily.com/documentation/best-practices/best-practices-research\#streaming-vs-polling)  Streaming vs. Polling

[**Streaming** \\
\\
Best for user interfaces where you want real-time updates.](https://github.com/tavily-ai/tavily-cookbook/blob/main/cookbooks/research/streaming.ipynb) [**Polling** \\
\\
Best for background processes where you check status periodically.](https://github.com/tavily-ai/tavily-cookbook/blob/main/cookbooks/research/polling.ipynb)

See streaming in action with the [live demo](https://chat-research.tavily.com/).

[Best Practices for Crawl\\
\\
Previous](https://docs.tavily.com/documentation/best-practices/best-practices-crawl) [API Key Management\\
\\
Next](https://docs.tavily.com/documentation/best-practices/api-key-management)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.