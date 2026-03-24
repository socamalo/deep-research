Title: Rate Limits - Tavily Docs
URL: https://docs.tavily.com/documentation/rate-limits
Description: Learn about Tavily's API rate limits for both development and production environments.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/rate-limits#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Getting Started

Rate Limits

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### Getting Started

- [About](https://docs.tavily.com/documentation/about)
- [Quickstart](https://docs.tavily.com/documentation/quickstart)
- [Credits & Pricing](https://docs.tavily.com/documentation/api-credits)
- [Rate Limits](https://docs.tavily.com/documentation/rate-limits)

##### FAQ

- [Frequently Asked Questions](https://docs.tavily.com/faq/faq)

On this page

- [Crawl Endpoint Rate Limits](https://docs.tavily.com/documentation/rate-limits#crawl-endpoint-rate-limits)
- [Research Endpoint Rate Limits](https://docs.tavily.com/documentation/rate-limits#research-endpoint-rate-limits)
- [Usage Endpoint Rate Limits](https://docs.tavily.com/documentation/rate-limits#usage-endpoint-rate-limits)

We offer two types of rate limits based on the environment associated with your API key. [**Get your API key** \\
\\
Create your Development or Production API keys.](https://app.tavily.com/)

| Environment | Requests per minute (RPM) |
| --- | --- |
| `Development` | 100 |
| `Production` | 1,000 |

## [​](https://docs.tavily.com/documentation/rate-limits\#crawl-endpoint-rate-limits)  Crawl Endpoint Rate Limits

The crawl endpoint has a separate rate limit that applies to both development and production keys:

| Environment | Requests per minute (RPM) |
| --- | --- |
| `Development` | 100 |
| `Production` | 100 |

## [​](https://docs.tavily.com/documentation/rate-limits\#research-endpoint-rate-limits)  Research Endpoint Rate Limits

The research endpoint has a separate rate limit that applies to both development and production keys for creating research tasks. Note that polling requests to retrieve the status of ongoing research tasks follow the default rate limits as decribed above.

| Environment | Requests per minute (RPM) |
| --- | --- |
| `Development` | 20 |
| `Production` | 20 |

## [​](https://docs.tavily.com/documentation/rate-limits\#usage-endpoint-rate-limits)  Usage Endpoint Rate Limits

The usage endpoint has a separate rate limit that applies to both development and production keys:

| Environment | Requests per 10 minutes |
| --- | --- |
| `Development` | 10 |
| `Production` | 10 |

1. Access to production keys requires either an active **Paid Plan** or **PAYGO** enabled. More information can be found [here](https://docs.tavily.com/guides/api-credits).
2. When using the REST API, ensure you include your API key in the header to apply the correct rate limits.

[Credits & Pricing\\
\\
Previous](https://docs.tavily.com/documentation/api-credits) [Frequently Asked Questions\\
\\
Next](https://docs.tavily.com/faq/faq)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.