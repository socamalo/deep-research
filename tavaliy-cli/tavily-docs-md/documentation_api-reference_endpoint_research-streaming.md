Title: Streaming - Tavily Docs
URL: https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming
Description: Stream real-time research progress and results from Tavily Research API

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Research

Streaming

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

  - [POST\\
    \\
    Create Research Task](https://docs.tavily.com/documentation/api-reference/endpoint/research)
  - [GET\\
    \\
    Get Research Task Status](https://docs.tavily.com/documentation/api-reference/endpoint/research-get)
  - [Streaming](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming)
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

- [Overview](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#overview)
- [Enabling Streaming](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#enabling-streaming)
- [Event Structure](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#event-structure)
- [Core Fields](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#core-fields)
- [Event Types](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#event-types)
- [1\. Tool Call Events](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#1-tool-call-events)
- [2\. Tool Response Events](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#2-tool-response-events)
- [3\. Content Events](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#3-content-events)
- [4\. Sources Event](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#4-sources-event)
- [5\. Done Event](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#5-done-event)
- [Tool Types](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#tool-types)
- [Research Flow Example](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#research-flow-example)
- [Handling Streaming Responses](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#handling-streaming-responses)
- [Python Example](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#python-example)
- [JavaScript Example](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#javascript-example)
- [Structured Output with Streaming](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#structured-output-with-streaming)
- [Error Handling](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#error-handling)
- [Non-Streaming Alternative](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#non-streaming-alternative)

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#overview)  Overview

When using the Tavily Research API, you can stream responses in real-time by setting `stream: true` in your request. This allows you to receive research progress updates, tool calls, and final results as they’re generated, providing a better user experience for long-running research tasks.Streaming is particularly useful for:

- Displaying research progress to users in real-time
- Monitoring tool calls and search queries as they execute
- Receiving incremental updates during lengthy research operations
- Building interactive research interfaces

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#enabling-streaming)  Enabling Streaming

To enable streaming, set the `stream` parameter to `true` when making a request to the Research endpoint:

Copy

Ask AI

```
{
  "input": "What are the latest developments in AI?",
  "stream": true
}
```

The API will respond with a `text/event-stream` content type, sending Server-Sent Events (SSE) as the research progresses.

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#event-structure)  Event Structure

Each streaming event follows a consistent structure compatible with the OpenAI chat completions format:

Copy

Ask AI

```
{
  "id": "123e4567-e89b-12d3-a456-426614174111",
  "object": "chat.completion.chunk",
  "model": "mini",
  "created": 1705329000,
  "choices": [\
    {\
      "delta": {\
        // Event-specific data here\
      }\
    }\
  ]
}
```

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#core-fields)  Core Fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the stream event |
| `object` | string | Always `"chat.completion.chunk"` for streaming events |
| `model` | string | The research model being used (`"mini"` or `"pro"`) |
| `created` | integer | Unix timestamp when the event was created |
| `choices` | array | Array containing the delta with event details |

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#event-types)  Event Types

The streaming response includes different types of events in the `delta` object. Here are the main event types you’ll encounter:

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#1-tool-call-events)  1\. Tool Call Events

When the research agent performs actions like web searches, you’ll receive tool call events:

Copy

Ask AI

```
{
  "id": "evt_002",
  "object": "chat.completion.chunk",
  "model": "mini",
  "created": 1705329005,
  "choices": [\
    {\
      "delta": {\
        "role": "assistant",\
        "tool_calls": {\
          "type": "tool_call",\
          "tool_call": [\
            {\
              "name": "WebSearch",\
              "id": "fc_633b5932-e66c-4523-931a-04a7b79f2578",\
              "arguments": "Executing 5 search queries",\
              "queries": ["latest AI developments 2024", "machine learning breakthroughs", "..."]\
            }\
          ]\
        }\
      }\
    }\
  ]
}
```

**Tool Call Delta Fields:**

| Field | Type | Description |
| --- | --- | --- |
| `type` | string | Either `"tool_call"` or `"tool_response"` |
| `tool_call` | array | Details about the tool being invoked |
| `name` | string | Name of the tool (see [Tool Types](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming#tool-types) below) |
| `id` | string | Unique identifier for the tool call |
| `arguments` | string | Description of the action being performed |
| `queries` | array | _(WebSearch only)_ The search queries being executed |
| `parent_tool_call_id` | string | _(Pro mode only)_ ID of the parent tool call for nested operations |

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#2-tool-response-events)  2\. Tool Response Events

After a tool executes, you’ll receive response events with discovered sources:

Copy

Ask AI

```
{
  "id": "evt_003",
  "object": "chat.completion.chunk",
  "model": "mini",
  "created": 1705329010,
  "choices": [\
    {\
      "delta": {\
        "role": "assistant",\
        "tool_calls": {\
          "type": "tool_response",\
          "tool_response": [\
            {\
              "name": "WebSearch",\
              "id": "fc_633b5932-e66c-4523-931a-04a7b79f2578",\
              "arguments": "Completed executing search tool call",\
              "sources": [\
                {\
                  "url": "https://example.com/article",\
                  "title": "Example Article",\
                  "favicon": "https://example.com/favicon.ico"\
                }\
              ]\
            }\
          ]\
        }\
      }\
    }\
  ]
}
```

**Tool Response Fields:**

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Name of the tool that completed |
| `id` | string | Unique identifier matching the original tool call |
| `arguments` | string | Completion status message |
| `sources` | array | Sources discovered by the tool (with `url`, `title`, `favicon`) |
| `parent_tool_call_id` | string | _(Pro mode only)_ ID of the parent tool call |

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#3-content-events)  3\. Content Events

The final research report is streamed as content chunks:

Copy

Ask AI

```
{
  "id": "evt_004",
  "object": "chat.completion.chunk",
  "model": "mini",
  "created": 1705329015,
  "choices": [\
    {\
      "delta": {\
        "role": "assistant",\
        "content": "# Research Report\n\nBased on the latest sources..."\
      }\
    }\
  ]
}
```

**Content Field:**

- Can be a **string** (markdown-formatted report chunks) when no `output_schema` is provided
- Can be an **object** (structured data) when an `output_schema` is specified

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#4-sources-event)  4\. Sources Event

After the content is streamed, a sources event is emitted containing all sources used in the research:

Copy

Ask AI

```
{
  "id": "evt_005",
  "object": "chat.completion.chunk",
  "model": "mini",
  "created": 1705329020,
  "choices": [\
    {\
      "delta": {\
        "role": "assistant",\
        "sources": [\
          {\
            "url": "https://example.com/article",\
            "title": "Example Article Title",\
            "favicon": "https://example.com/favicon.ico"\
          }\
        ]\
      }\
    }\
  ]
}
```

**Source Object Fields:**

| Field | Type | Description |
| --- | --- | --- |
| `url` | string | The URL of the source |
| `title` | string | The title of the source page |
| `favicon` | string | URL to the source’s favicon |

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#5-done-event)  5\. Done Event

Signals the completion of the streaming response:

Copy

Ask AI

```
event: done
```

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#tool-types)  Tool Types

During research, you’ll encounter the following tool types in streaming events:

| Tool Name | Description | Model |
| --- | --- | --- |
| `Planning` | Initializes the research plan based on the input query | Both |
| `Generating` | Generates the final research report from collected information | Both |
| `WebSearch` | Executes web searches to gather information | Both |
| `ResearchSubtopic` | Conducts deep research on specific subtopics | Pro only |

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#research-flow-example)  Research Flow Example

A typical streaming session follows this sequence:

01. **Planning** tool\_call → Initializing research plan
02. **Planning** tool\_response → Research plan initialized
03. **WebSearch** tool\_call → Executing search queries (with `queries` array)
04. **WebSearch** tool\_response → Search completed (with `sources` array)
05. _(Pro mode)_ **ResearchSubtopic** tool\_call/response cycles for deeper research
06. **Generating** tool\_call → Generating final report
07. **Generating** tool\_response → Report generated
08. **Content** events → Streamed report chunks
09. **Sources** event → Complete list of all sources used
10. **Done** event → Stream complete

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#handling-streaming-responses)  Handling Streaming Responses

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#python-example)  Python Example

Copy

Ask AI

```
from tavily import TavilyClient

# Step 1. Instantiating your TavilyClient
tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")

# Step 2. Creating a streaming research task
stream = tavily_client.research(
    input="Research the latest developments in AI",
    model="pro",
    stream=True
)

for chunk in stream:
    print(chunk.decode('utf-8'))
```

### [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#javascript-example)  JavaScript Example

Copy

Ask AI

```
const { tavily } = require("@tavily/core");

const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });

const stream = await tvly.research("Research the latest developments in AI", {
  model: "pro",
  stream: true,
});

for await (const chunk of result as AsyncGenerator<Buffer, void, unknown>) {
    console.log(chunk.toString('utf-8'));
}
```

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#structured-output-with-streaming)  Structured Output with Streaming

When using `output_schema` to request structured data, the `content` field will contain an object instead of a string:

Copy

Ask AI

```
{
  "delta": {
    "role": "assistant",
    "content": {
      "company": "Acme Corp",
      "key_metrics": ["Revenue: $1M", "Growth: 50%"],
      "summary": "Company showing strong growth..."
    }
  }
}
```

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#error-handling)  Error Handling

If an error occurs during streaming, you may receive an error event:

Copy

Ask AI

```
{
  "id": "1d77bdf5-38a4-46c1-87a6-663dbc4528ec",
  "object": "error",
  "error": "An error occurred while streaming the research task"
}
```

Always implement proper error handling in your streaming client to gracefully handle these cases.

## [​](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming\#non-streaming-alternative)  Non-Streaming Alternative

If you don’t need real-time updates, set `stream: false` (or omit the parameter) to receive a single complete response:

Copy

Ask AI

```
{
  "request_id": "123e4567-e89b-12d3-a456-426614174111",
  "created_at": "2025-01-15T10:30:00Z",
  "status": "pending",
  "input": "What are the latest developments in AI?",
  "model": "mini",
  "response_time": 1.23
}
```

You can then poll the status endpoint to check when the research is complete.

[Get Research Task Status\\
\\
Previous](https://docs.tavily.com/documentation/api-reference/endpoint/research-get) [Usage\\
\\
Next](https://docs.tavily.com/documentation/api-reference/endpoint/usage)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.