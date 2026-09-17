# OMEGA Ω — Browser Media Tools

OMEGA is a static browser-based media toolkit deployed at:

**https://x-five-kappa-98.vercel.app/**

The repository contains local WebP conversion and PDF compression tools, a procedural Canvas/MediaRecorder video workflow, YouTube thumbnail resolution, and optional public TikTok URL processing through external providers.

## Important implementation notes

- WebP conversion and PDF processing run in the browser. Files are not uploaded to an OMEGA server for those workflows.
- The video workflow requests a still image from an external image service, applies procedural Canvas motion, and records a WebM file with `MediaRecorder`. It is not a native Veo-3 rendering API.
- TikTok URL processing depends on third-party providers. Private, removed, restricted, or unsupported URLs may fail.
- YouTube functions resolve thumbnail images only; they do not download YouTube videos.
- Users are responsible for copyright, creator permission, platform terms, and lawful use of downloaded or generated media.
- Monetization scripts from the repository are intentionally retained. On the main page, the real download href remains active and the Smartlink opens separately after the user clicks a completed download action.

## SEO build policy

The repository does not automatically manufacture keyword pages by changing only a title or description. Each indexable landing page must have a reviewed purpose, unique explanatory content, accurate metadata, a self-referencing canonical URL, and a matching sitemap entry.

Run the local quality gate with:

```bash
python3 generate_pages.py
```

The quality gate checks that HTML pages contain titles, descriptions, canonicals, the official domain, and consistent robots and sitemap files.

The one-time repair and normalization script is:

```bash
python3 apply_fixes.py
```

Review the generated diff before committing. Do not run it against a different production domain without changing `SITE_URL` in both scripts and updating the deployment smoke tests.

## Deployment

The current canonical origin is the Vercel URL above. If you later move to a custom domain, update all of these together:

- `SITE_URL` in `apply_fixes.py` and `generate_pages.py`.
- `robots.txt`.
- `sitemap.xml`.
- HTML `canonical`, `og:url`, and structured-data URLs.
- `.github/workflows/ping.yml`, `programmatic-seo.yml`, and `seo-crawler.yml`.
- The Vercel project domain and any redirect from the old origin.

Deploy the repository as a static Vercel project. After deployment, verify:

```bash
curl -I https://x-five-kappa-98.vercel.app/
curl -I https://x-five-kappa-98.vercel.app/robots.txt
curl -I https://x-five-kappa-98.vercel.app/sitemap.xml
```

Then inspect the official origin in Google Search Console and submit the sitemap there. Search Console is the source of truth for indexing and Core Web Vitals; GitHub Actions only performs consistency and availability checks.

## Directory overview

- `index.html`: main multi-tool interface.
- `*-to-webp.html`: focused WebP landing pages.
- `*youtube*.html`: focused YouTube thumbnail pages.
- `*tiktok*.html`: public TikTok URL processing pages.
- `*veo*` and `*cinematic*`: transparent procedural video pages.
- `apply_fixes.py`: metadata, canonical, structured-data, content, robots, and sitemap normalizer.
- `generate_pages.py`: SEO quality gate; it intentionally does not auto-generate thin pages.
- `vercel.json`: caching and security headers.
- `sw.js`: same-origin static-asset cache only; HTML is always fetched from the network.
