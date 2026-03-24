Title: API Key Management - Tavily Docs
URL: https://docs.tavily.com/documentation/best-practices/api-key-management
Description: Learn how to handle API key leaks and best practices for key rotation.

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/documentation/best-practices/api-key-management#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

Best Practices

API Key Management

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

- [What to do if your API key leaks](https://docs.tavily.com/documentation/best-practices/api-key-management#what-to-do-if-your-api-key-leaks)
- [Rotating your API keys](https://docs.tavily.com/documentation/best-practices/api-key-management#rotating-your-api-keys)
- [How to rotate your keys safely](https://docs.tavily.com/documentation/best-practices/api-key-management#how-to-rotate-your-keys-safely)

## [​](https://docs.tavily.com/documentation/best-practices/api-key-management\#what-to-do-if-your-api-key-leaks)  What to do if your API key leaks

If you suspect or know that your API key has been leaked (e.g., committed to a public repository, shared in a screenshot, or exposed in client-side code), **immediate action is required** to protect your account and quota.Follow these steps immediately:

1. **Log in to your account**: Go to the [Tavily Dashboard](https://app.tavily.com/).
2. **Revoke the leaked key**: Navigate to the API Keys section. Identify the compromised key and delete or revoke it immediately. This will stop any unauthorized usage.
3. **Generate a new key**: Create a new API key to replace the compromised one.
4. **Update your applications**: Replace the old key with the new one in your environment variables, secrets management systems, and application code.

If you notice any unusual activity or usage spikes associated with the leaked key before you revoked it, please contact [support@tavily.com](mailto:support@tavily.com) for assistance.

## [​](https://docs.tavily.com/documentation/best-practices/api-key-management\#rotating-your-api-keys)  Rotating your API keys

As a general security best practice, we recommend rotating your API keys periodically (e.g., every 90 days). This minimizes the impact if a key is ever compromised without your knowledge.

### [​](https://docs.tavily.com/documentation/best-practices/api-key-management\#how-to-rotate-your-keys-safely)  How to rotate your keys safely

To rotate your keys without downtime:

1. **Generate a new key**: Create a new API key in the [Tavily Dashboard](https://app.tavily.com/) while keeping the old one active.
2. **Update your application**: Deploy your application with the new API key.
3. **Verify functionality**: Ensure your application is working correctly with the new key.
4. **Revoke the old key**: Once you are confirmed that the new key is in use and everything is functioning as expected, delete the old API key from the dashboard.

Never hardcode API keys in your source code. Always use environment variables or a secure secrets manager to store your credentials.

[Best Practices for Research\\
\\
Previous](https://docs.tavily.com/documentation/best-practices/best-practices-research)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.