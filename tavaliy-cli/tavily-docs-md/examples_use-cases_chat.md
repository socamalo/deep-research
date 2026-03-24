Title: Chat - Tavily Docs
URL: https://docs.tavily.com/examples/use-cases/chat
Description: Build a conversational chat agent with real-time web search, crawl, and extract capabilities using Tavily's API

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/examples/use-cases/chat#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Use Cases

Chat

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### Use Cases

- [Chat](https://docs.tavily.com/examples/use-cases/chat)
- [Data Enrichment](https://docs.tavily.com/examples/use-cases/data-enrichment)
- [Company Research](https://docs.tavily.com/examples/use-cases/company-research)
- [Crawl to RAG](https://docs.tavily.com/examples/use-cases/crawl-to-rag)
- [Meeting Prep](https://docs.tavily.com/examples/use-cases/meeting-prep)
- [RAG evaluation](https://docs.tavily.com/examples/use-cases/web-eval)
- [Market Researcher](https://docs.tavily.com/examples/use-cases/market-researcher)

##### Quick Tutorials

- [Cookbook](https://docs.tavily.com/examples/quick-tutorials/cookbook)

##### Open Source

- [Projects](https://docs.tavily.com/examples/open-sources/projects)

On this page

- [Try Our Chatbot](https://docs.tavily.com/examples/use-cases/chat#try-our-chatbot)
- [Step 1: Get Your API Key](https://docs.tavily.com/examples/use-cases/chat#step-1-get-your-api-key)
- [Step 2: Chat with Tavily](https://docs.tavily.com/examples/use-cases/chat#step-2-chat-with-tavily)
- [Step 3: Read The Open Source Code](https://docs.tavily.com/examples/use-cases/chat#step-3-read-the-open-source-code)
- [Features](https://docs.tavily.com/examples/use-cases/chat#features)
- [How Does It Work?](https://docs.tavily.com/examples/use-cases/chat#how-does-it-work)

![Tavily Chatbot Demo](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/chatbotgif.gif?s=34574620e82d48fe93965035840fca9f)

## [​](https://docs.tavily.com/examples/use-cases/chat\#try-our-chatbot)  Try Our Chatbot

### [​](https://docs.tavily.com/examples/use-cases/chat\#step-1-get-your-api-key)  Step 1: Get Your API Key

[**Get your Tavily API key**](https://app.tavily.com/)

### [​](https://docs.tavily.com/examples/use-cases/chat\#step-2-chat-with-tavily)  Step 2: Chat with Tavily

[**Launch the application**](https://chat.tavily.com/)

### [​](https://docs.tavily.com/examples/use-cases/chat\#step-3-read-the-open-source-code)  Step 3: Read The Open Source Code

[**View Github Repository**](https://github.com/tavily-ai/tavily-chat)

## [​](https://docs.tavily.com/examples/use-cases/chat\#features)  Features

1. **Fast Results**: Tavily’s API delivers quick responses essential for real-time chat experiences.
2. **Intelligent Parameter Selection**: Dynamically select API parameters based on conversation context using LangChain integration. Specifically designed for agentic systems. All you need is a natural language input, no need to configure structured JSON for our API.
3. **Content Snippets**: Tavily provides compact summaries of search results in the `content` field, best for maintaining small context sizes in low latency, multi-turn applications.
4. **Source Attribution**: All search, extract, and crawl results include URLs, enabling easy implementation of citations for transparency and credibility in responses.

## [​](https://docs.tavily.com/examples/use-cases/chat\#how-does-it-work)  How Does It Work?

The chatbot uses a simple ReAct architecture to manage conversation flow and decision-making. Here’s how the core components work together:![](https://mintcdn.com/tavilyai/Kondu-1Gs9IHpAYd/images/web-agent.png?fit=max&auto=format&n=Kondu-1Gs9IHpAYd&q=85&s=ab86ef264a4cc606f955be338c03429f)The workflow consists of several key components:

1\. Code Snippet: Graph Structure

The chatbot uses LangGraph MemorySaver to manage conversation flow. The graph structure conrtols how messages are processed and routed.

This code snippet is not meant to run standalone. View the full implementation in our [github repository](https://github.com/tavily-ai/tavily-chat).

Copy

Ask AI

```
class WebAgent:
    def __init__(
        self,
    ):
        self.llm = ChatOpenAI(
            model="gpt-4.1-nano", api_key=os.getenv("OPENAI_API_KEY")
        ).with_config({"tags": ["streaming"]})

        # Define the LangChain search tool
        self.search = TavilySearch(
            max_results=10, topic="general", api_key=os.getenv("TAVILY_API_KEY")
        )

        # Define the LangChain extract tool
        self.extract = TavilyExtract(
            extract_depth="advanced", api_key=os.getenv("TAVILY_API_KEY")
        )
        # Define the LangChain crawl tool
        self.crawl = TavilyCrawl(api_key=os.getenv("TAVILY_API_KEY"))
        self.prompt = PROMPT
        self.checkpointer = MemorySaver()

    def build_graph(self):
        """
        Build and compile the LangGraph workflow.
        """
        return create_react_agent(
            prompt=self.prompt,
            model=self.llm,
            tools=[self.search, self.extract, self.crawl],
            checkpointer=self.checkpointer,
        )
```

2\. Routing Logic

The router decides whether to use base knowledge or perform a Tavily web search, extract, or crawl based on:

- Question complexity
- Need for current information
- Available conversation context

3\. Memory Management

The chatbot maintains conversation history using a memory system that:

- Preserves context across multiple exchanges
- Stores relevant search results for future reference
- Manages system prompts and initialization

4\. Real-time Search Integration

When Tavily access is needed, the chatbot:

- Performs targeted web search, extract, or crawl using the LangChain integration
- Includes source citations

5\. Streaming Updates

Users receive real-time updates on:

- Search progress
- Response generation
- Source processing

[Data Enrichment\\
\\
Next](https://docs.tavily.com/examples/use-cases/data-enrichment)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Tavily Chatbot Demo](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/chatbotgif.gif?s=34574620e82d48fe93965035840fca9f)

![](https://mintcdn.com/tavilyai/Kondu-1Gs9IHpAYd/images/web-agent.png?w=840&fit=max&auto=format&n=Kondu-1Gs9IHpAYd&q=85&s=a75700b229e95844d71df3aa4f5ddec7)