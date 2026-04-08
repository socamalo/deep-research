#!/usr/bin/env python3
"""
Crawl Python documentation tutorial site and get the first 5 pages.
"""

import urllib.request
import re
from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.in_a = False
        self.current_href = None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs_dict = dict(attrs)
            if 'href' in attrs_dict:
                self.current_href = attrs_dict['href']
                self.in_a = True

    def handle_data(self, data):
        if self.in_a and self.current_href:
            self.links.append((self.current_href, data.strip()))

    def handle_endtag(self, tag):
        if tag == 'a':
            self.in_a = False
            self.current_href = None

def main():
    base_url = 'https://docs.python.org/3/tutorial/'
    print(f'Fetching: {base_url}')
    print('=' * 60)

    try:
        req = urllib.request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8')
            print(f'Successfully fetched {len(html)} bytes')

            # Extract links
            parser = LinkExtractor()
            parser.feed(html)

            # Find tutorial page links
            tutorial_links = []
            for href, text in parser.links:
                if href.endswith('.html') and not href.startswith('http'):
                    full_url = base_url + href if not href.startswith('/') else 'https://docs.python.org' + href
                    if full_url not in [l[0] for l in tutorial_links]:
                        tutorial_links.append((full_url, text))

            print(f'\nFound {len(tutorial_links)} tutorial pages')
            print('\nFirst 5 pages:')
            print('-' * 60)
            for i, (url, title) in enumerate(tutorial_links[:5], 1):
                print(f'{i}. {title}')
                print(f'   URL: {url}')
                print()

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
