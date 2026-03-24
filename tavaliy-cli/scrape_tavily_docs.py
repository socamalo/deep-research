"""Scrape all Tavily docs URLs to markdown files."""
import re
import subprocess
from pathlib import Path

URLS_FILE = Path(__file__).parent / "tavily-docs-urls.txt"
OUT_DIR = Path(__file__).parent / "tavily-docs-md"


def url_to_filename(url: str) -> str:
    """Convert URL to safe filename."""
    # Remove protocol and domain
    path = url.replace("https://docs.tavily.com/", "").strip("/")
    # Replace slashes with underscores, remove .md if present
    path = path.replace(".md", "").replace("/", "_")
    # Sanitize
    path = re.sub(r"[^\w\-.]", "_", path) or "index"
    return f"{path}.md"


def main():
    urls = [
        line.strip()
        for line in URLS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and line.strip().startswith("http")
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    success = 0
    failed = []
    for i, url in enumerate(urls, 1):
        out_file = OUT_DIR / url_to_filename(url)
        print(f"[{i}/{len(urls)}] {url} -> {out_file.name}")
        try:
            result = subprocess.run(
                ["firecrawl", "scrape", url, "-o", str(out_file)],
                capture_output=True,
                text=True,
                timeout=60,
            )
            if result.returncode == 0:
                success += 1
            else:
                failed.append((url, result.stderr or result.stdout))
        except Exception as e:
            failed.append((url, str(e)))
    print(f"\nDone: {success} succeeded, {len(failed)} failed")
    if failed:
        for url, err in failed:
            print(f"  FAILED: {url}\n    {err[:200]}")


if __name__ == "__main__":
    main()
