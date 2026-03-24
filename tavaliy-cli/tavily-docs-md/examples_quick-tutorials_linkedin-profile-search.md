Title: LinkedIn Profile Search - Tavily Docs
URL: https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search
Description: Discover and analyze LinkedIn profiles with Tavily's APIs

--- MARKDOWN ---
[Skip to main content](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/light.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=7df00865e87a791d3152072e23161d63)![dark logo](https://mintcdn.com/tavilyai/3bRbNpTHEFkRcfMH/logo/dark.svg?fit=max&auto=format&n=3bRbNpTHEFkRcfMH&q=85&s=bbd8aed61d89c892eafdcb7d9473f104)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

LinkedIn Profile Search

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

- [What will you learn?](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#what-will-you-learn)
- [How does it work?](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#how-does-it-work)
- [Include Raw Content](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#include-raw-content)
- [Include Answer](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#include-answer)
- [Getting Started](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#getting-started)

## [​](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search\#what-will-you-learn)  What will you learn?

In this use case, you’ll learn how to gather information from LinkedIn profiles using Tavily’s Search and Extract functionality.We’ll teach you how to structure your search parameters to generate concise and readable answers to your provided query, and how to properly use the Tavily Python SDK to retrieve the desired information effectively and efficiently.Once the search, extract, and answer process have been completed, we’ll demonstrate how to parse the raw extracted content into usable profile data.

## [​](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search\#how-does-it-work)  How does it work?

Through use of the `include_domains` and `include_raw_content` parameters, our system searches for **LinkedIn profiles** that match the provided query and extracts the profile content to provide complete insights into professional experiences, information and skills.

### [​](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search\#include-raw-content)  Include Raw Content

By including the `include_raw_content` parameter, Tavily’s **Search** and **Extract** functionality are used in tandem to provide the most accurate and complete result.

### [​](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search\#include-answer)  Include Answer

Utilizing the `include_answer` parameter provides an **LLM-generated** response to the provided query, making it easy to access and parse concise and relevant information quickly with detailed sources.

To get achieve the proper functionality when searching LinkedIn URLs, be sure
to specify `search_depth = advanced` in your use of Tavily Search.

## [​](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search\#getting-started)  Getting Started

> We have prepared a [Jupyter Notebook](https://github.com/tavily-ai/tavily-tutorials/blob/main/linkedin-profile-search.ipynb) outlining the contents of this tutorial

First create an account and get your free API key. [**Get your Tavily API key**](https://app.tavily.com/) Next, use the Tavily Python SDK to create the workflow.

1

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#)

Install the Tavily Python SDK

Shell

Copy

Ask AI

```
pip install -q tavily-python python-dotenv ipykernel
```

2

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#)

Import the necessary libraries

Python

Copy

Ask AI

```
import getpass
import os

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("TAVILY_API_KEY:\n")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
```

3

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#)

Instantiate the Tavily Client

Python

Copy

Ask AI

```
from tavily import TavilyClient

tavily_client = TavilyClient()
```

4

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#)

Execute the candidate leads search and extract

Python

Copy

Ask AI

```
response = tavily_client.search(
    query="Who are the C-Suite employees at OpenAI?",
    search_depth="advanced",
    include_answer="advanced",
    include_raw_content=True,
    include_domains=["linkedin.com/in"],
    max_results=10,
)
```

5

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#)

Function to parse LinkedIn profile raw content into key info

Python

Copy

Ask AI

```
import re

def extract_profile_data(raw_content):
    profile_data = {
        "location": None,
        "education": [],
        "skills": [],
        "work_experience": []
    }

    # Check if raw_content is None or empty
    if raw_content is None or raw_content.strip() == "":
        return profile_data

    # Extract Location
    location_match = re.search(r'\n(.*?)\n\d+ connections', raw_content)
    if location_match:
        profile_data["location"] = location_match.group(1).strip()

    # Extract Work Experience Section
    experience_match = re.search(r'Experience:\n(.*?)\n\nEducation:', raw_content, re.DOTALL)
    if experience_match:
        experience_text = experience_match.group(1)

        # Extract Company Names and Date Ranges
        experience_entries = re.findall(r'(.+?) \(https://www\.linkedin\.com/company/.*?\)\n(.*?)\n', experience_text)

        for company, date_range in experience_entries:
            profile_data["work_experience"].append({
                "company": company.strip(),
                "date_range": date_range.strip()
            })

    # Extract Education
    education_match = re.search(r'Education:\n(.*?)\n\nSkills:', raw_content, re.DOTALL)
    if education_match:
        education_text = education_match.group(1)
        education_entries = re.findall(r'(.+?)\n(.*?)\n(\w+ \d{4} - \w+ \d{4}|N/A - Present|\w+ \d{4} - \w+ \d{4})\nGrade: (.*?)\nActivities and societies: (.*?)\n', education_text)

        for institution, program, date_range, grade, activities in education_entries:
            profile_data["education"].append({
                "institution": institution.strip(),
                "program": program.strip(),
                "date_range": date_range.strip(),
                "grade": grade.strip(),
                "activities": activities.strip()
            })

    # Extract Skills
    skills_match = re.search(r'Skills:\n(.*?)\n\n', raw_content, re.DOTALL)
    if skills_match:
        skills_text = skills_match.group(1)
        profile_data["skills"] = [skill.strip() for skill in skills_text.split('\n') if skill.strip()]

    return profile_data
```

6

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#)

Execute the candidate leads search and extract

Python

Copy

Ask AI

```
profiles = []

for profile in response["results"]:
    profile_data = extract_profile_data(profile["raw_content"])
    profile_data["name"] = profile["title"]
    profile_data["url"] = profile["url"]
    profiles.append(profile_data)

print(response["answer"])
print(profiles)
```

7

[Navigate to header](https://docs.tavily.com/examples/quick-tutorials/linkedin-profile-search#)

Output

Shell

Copy

Ask AI

```
 # LLM-generated answer
 OpenAI's C-Suite includes several key executives. Sam Altman serves as the CEO, while Mira Murati holds the position of Chief Technology Officer (CTO). Brad Lightcap is the Chief Operating Officer (COO) of the company. Greg Brockman, one of the co-founders, holds the roles of President and Chairman. While not explicitly mentioned as C-Suite, Wojciech Zaremba is another co-founder who plays a significant role in the organization. The leadership team also includes Srinivas Narayanan as a Vice President, though his specific C-Suite title is not clear. These individuals collectively form the core executive team responsible for steering OpenAI's strategic direction and operations.

 # Profile data
 [\
     {\
         "name": "Hannah Wong - OpenAI"\
         "url": "https://www.linkedin.com/in/hannah-wong-66b78612",\
         "location": "San Francisco Bay Area, United States",\
         "education": [\
             {\
             "institution": "University of Washington",\
             "program": "Bachelor of Arts, Communications, Women Studies",\
             "date_range": "N/A - Present",\
             "grade": "Cum Laude",\
             "activities": "Association of Women in Communication, University Chorale"\
             }\
         ],\
         "skills": [\
             "Media Relations; Product Launch; Crisis Communications; Corporate Communications; Event Planning; Creative Writing; Reputation Management; Social Media Communications; Project Management; Team Leadership; Teamwork; Mentoring; Executive Communications; Product Reviews; Influencers; Global Communications; Management"\
         ],\
         "work_experience": [\
             {\
             "company": "Chief Communications Officer at OpenAI",\
             "date_range": "Aug 2024 - Present"\
             },\
             {\
             "company": "VP, Communications at OpenAI",\
             "date_range": "Jun 2023 - Aug 2024"\
             },\
             {\
             "company": "Director, Head of Public Relations at OpenAI",\
             "date_range": "Feb 2021 - Jun 2023"\
             },\
             {\
             "company": "Senior PR Manager, Apple Pay, Apple Card, iCloud at Apple",\
             "date_range": "Jan 2019 - Nov 2020"\
             },\
             {\
             "company": "PR Manager, iPad at Apple",\
             "date_range": "Nov 2014 - Dec 2018"\
             },\
             {\
             "company": "PR Manager, Consumer Momentum at Apple",\
             "date_range": "Oct 2013 - Oct 2014"\
             },\
             {\
             "company": "Corporate Communications at Gap Inc.",\
             "date_range": "Dec 2012 - May 2013"\
             },\
             {\
             "company": "Account Supervisor, Xbox LIVE, Charles Schwab, Twitter at Edelman",\
             "date_range": "Jun 2009 - Oct 2011"\
             },\
             {\
             "company": "Senior Account Executive, Xbox LIVE at Edelman",\
             "date_range": "Apr 2008 - Jun 2009"\
             },\
             {\
             "company": "Account Executive, Xbox at Edelman",\
             "date_range": "Apr 2007 - Mar 2008"\
             },\
             {\
             "company": "Assistant Account Executive at Edelman",\
             "date_range": "Apr 2006 - Mar 2007"\
             }\
         ]\
     },\
     ...\
 ]
```

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.