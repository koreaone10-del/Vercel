"""Safe SEO build step.

This project intentionally does not create keyword pages by changing only a title.
Create a page from a reviewed, unique content brief, then run apply_fixes.py.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).parent
SITE_URL = "https://x-five-kappa-98.vercel.app"

REQUIRED_FILES = ["index.html", "robots.txt", "sitemap.xml", "manifest.json"]


def validate():
    errors = []
    for name in REQUIRED_FILES:
        if not (ROOT / name).exists():
            errors.append(f"missing required file: {name}")
    for path in ROOT.glob("*.html"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "ultra-compressor-three.vercel.app" in text:
            errors.append(f"old domain reference: {path.name}")
        if not re.search(r'<title[^>]*>[^<]{20,}</title>', text, re.I|re.S):
            errors.append(f"missing or short title: {path.name}")
        if not re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'][^"\']{80,}', text, re.I|re.S):
            errors.append(f"missing or short description: {path.name}")
        if not re.search(r'<link[^>]+rel=["\']canonical["\']', text, re.I):
            errors.append(f"missing canonical: {path.name}")
    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {SITE_URL}/sitemap.xml" not in robots:
        errors.append("robots.txt does not point to the official sitemap")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if SITE_URL not in sitemap or "ultra-compressor-three" in sitemap:
        errors.append("sitemap contains an invalid domain")
    if errors:
        print("SEO validation failed:")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print("SEO validation passed: domain, metadata, canonicals, robots, and sitemap are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
