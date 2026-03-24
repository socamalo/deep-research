Title: RAG evaluation - Tavily Docs
URL: https://docs.tavily.com/examples/use-cases/web-eval
Description: Effortless Web-Based RAG Evaluation Using Tavily and LangGraph

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/examples/use-cases/web-eval#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Use Cases

RAG evaluation

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

- [Introduction](https://docs.tavily.com/examples/use-cases/web-eval#introduction)
- [How does it work?](https://docs.tavily.com/examples/use-cases/web-eval#how-does-it-work)
- [Learn More](https://docs.tavily.com/examples/use-cases/web-eval#learn-more)

# [​](https://docs.tavily.com/examples/use-cases/web-eval\#introduction)  Introduction

Every data science enthusiast knows that a vital first step to building a successful model or algorithm is having a reliable evaluation set to aspire to. In the rapidly evolving landscape of **Retrieval-Augmented Generation (RAG)** and AI-driven search systems, the importance of high-quality eval datasets is crucial.In this article, we introduce an agentic workflow designed to **generate** subject-specific dynamic **evaluation datasets**, enabling precise validation of web search augmented agents’ performance.**Known RAG evaluation datasets**, such as [HotPotQA](https://hotpotqa.github.io/), [CRAG](https://github.com/facebookresearch/CRAG), and [MultiHop-RAG](https://github.com/yixuantt/MultiHop-RAG), have been pivotal in benchmarking and fine-tuning models. However, these datasets primarily focus on evaluating performance with **static, pre-defined document sets**. As a result, they fall short when it comes to evaluating **web-based RAG systems**, where data is dynamic, contextual, and ever-changing.This gap presents a significant challenge: how do we effectively test and refine RAG systems designed for real-world web search scenarios? **Enter the Real-Time Dataset Generator for RAG Evals** — an agentic tool leveraging [Tavily’s Search Layer](https://tavily.com/) and the **LangGraph framework** to create diverse, relevant, and dynamic datasets tailored specifically for web based RAG agents.

# [​](https://docs.tavily.com/examples/use-cases/web-eval\#how-does-it-work)  How does it work?

![Web Evaluation Graph](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/web-eval-graph.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=4a1f16a5632ea3abeb5f0dad21aa49cb)

The Real-Time Dataset Generator follows a systematic workflow to create high-quality evaluation datasets:

1

[Navigate to header](https://docs.tavily.com/examples/use-cases/web-eval#)

Input

The workflow begins with user-provided inputs.

2

[Navigate to header](https://docs.tavily.com/examples/use-cases/web-eval#)

Domain-Specific Search Query Generation

If a subject is provided (e.g., “NBA Basketball”), the system **generates a**
**set of search queries**. This ensures queries are tailored to gather
high-quality, recent, and subject-specific information.

3

[Navigate to header](https://docs.tavily.com/examples/use-cases/web-eval#)

Web Search with Tavily

This step guarantees that the dataset reflects **current and relevant**
**information**, particularly for web search RAG evaluation, where up-to-date
data is crucial.This is the **heart of the RAG Dataset Generator**,
transforming queries into actionable, high-quality data that forms the
foundation of the evaluation set.

4

[Navigate to header](https://docs.tavily.com/examples/use-cases/web-eval#)

Q&A Pair Generation

For each website returned by Tavily, the system generates question-answer pair
using a **map-reduce paradigm** to ensure efficient processing across multiple
sources. This step is implemented using LangGraph’s Send API.

5

[Navigate to header](https://docs.tavily.com/examples/use-cases/web-eval#)

Saving the Evaluation Set

Finally, the generated dataset is saved either **locally** or to
**Langsmith**, based on the input configuration.

6

[Navigate to header](https://docs.tavily.com/examples/use-cases/web-eval#)

Output

The result is a well-structured, subject-specific evaluation dataset, ready for use in advanced evaluation methods like **LLM-as-a-Judge**.

# [​](https://docs.tavily.com/examples/use-cases/web-eval\#learn-more)  Learn More

Want to dive deeper into web-based RAG evaluation? Check out these resources:

[**Blog Post** \\
\\
Read our detailed blog post about generating dynamic RAG evaluation datasets](https://blog.tavily.com/effortless-web-based-rag-evaluation-using-tavily-and-langgraph/) [**GitHub**\\
\\
`/Eyalbenba/tavily-web-eval-generator`![GitHub Repo stars](https://img.shields.io/github/stars/Eyalbenba/tavily-web-eval-generator?style=social)](https://github.com/Eyalbenba/tavily-web-eval-generator)

[Meeting Prep\\
\\
Previous](https://docs.tavily.com/examples/use-cases/meeting-prep) [Market Researcher\\
\\
Next](https://docs.tavily.com/examples/use-cases/market-researcher)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Web Evaluation Graph](https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/web-eval-graph.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=a7d31aa205cbd1b2000f73de8dc7d1bf)