#!/usr/bin/env python3
"""Fetch and extract main content from Wikipedia AI page."""

import urllib.request
import re
from html.parser import HTMLParser

class WikipediaContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.in_script = False
        self.in_style = False
        self.skip_tag = 0
        self.content = []
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Skip script and style tags
        if tag in ('script', 'style'):
            self.in_script = True
            return

        # Skip navigation, infobox, references, etc.
        skip_classes = ['navbox', 'infobox', 'reflist', 'mw-jump-link', 'toc',
                       'mw-editsection', 'external', 'thumbinner', 'thumb',
                       'mw-parser-output']

        class_attr = attrs_dict.get('class', '')
        if any(skip in class_attr for skip in skip_classes):
            self.skip_tag += 1
            return

        # Start collecting content from main content area
        if tag == 'div' and 'mw-parser-output' in class_attr:
            self.in_content = True

        # Handle links - keep the text
        if tag == 'a':
            href = attrs_dict.get('href', '')
            if href.startswith('#'):
                return  # Skip anchor links

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.in_script = False
            return

        if self.skip_tag > 0:
            self.skip_tag -= 1
            return

        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'li'):
            if self.current_text and self.in_content and not self.skip_tag:
                text = ' '.join(self.current_text).strip()
                if text:
                    self.content.append(text)
            self.current_text = []

    def handle_data(self, data):
        if self.in_script or self.skip_tag > 0:
            return
        if self.in_content:
            self.current_text.append(data)

    def get_text(self):
        return '\n\n'.join(self.content)


def fetch_and_extract():
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; ResearchBot/0.1)'}

    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req, timeout=30) as response:
        html = response.read().decode('utf-8')

    print(f"Downloaded {len(html)} characters")

    # Extract main content
    # Wikipedia's main content is in #mw-content-text > .mw-parser-output

    # Simple regex-based extraction for main paragraphs
    # Remove script and style tags first
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)

    # Find the main content
    content_match = re.search(
        r'<div id="mw-content-text"[^>]*>.*?<div class="mw-parser-output"[^>]*>(.*?)</div>\s*</div>',
        html, re.DOTALL
    )

    if content_match:
        content_html = content_match.group(1)

        # Remove unwanted sections
        # Remove references section
        content_html = re.split(r'<h2[^>]*>.*?(References|Notes|See also|External links)',
                                content_html, flags=re.IGNORECASE)[0]

        # Remove infobox
        content_html = re.sub(r'<table class="infobox[^"]*"[^>]*>.*?</table>', '',
                             content_html, flags=re.DOTALL)

        # Extract text from paragraphs and headers
        parser = WikipediaContentExtractor()
        parser.feed('<div class="mw-parser-output">' + content_html + '</div>')

        text = parser.get_text()

        # Clean up the text
        text = re.sub(r'\[\d+\]', '', text)  # Remove citation markers
        text = re.sub(r'\[edit\]', '', text)  # Remove edit links
        text = re.sub(r'\n{3,}', '\n\n', text)  # Normalize newlines
        text = text.strip()

        return text, html
    else:
        return "Could not extract content", html


if __name__ == "__main__":
    text, raw_html = fetch_and_extract()

    # Save results
    output_dir = "/Users/d_d/.claude/skills/tavily-workspace/iteration-1/extract-content/without_skill"

    with open(f"{output_dir}/extracted_content.txt", "w", encoding="utf-8") as f:
        f.write(text)

    with open(f"{output_dir}/raw_html.html", "w", encoding="utf-8") as f:
        f.write(raw_html)

    print(f"\nExtracted {len(text)} characters of main content")
    print(f"Content saved to {output_dir}/extracted_content.txt")
    print(f"Raw HTML saved to {output_dir}/raw_html.html")
    print("\n--- First 2000 characters of extracted content ---")
    print(text[:2000])
