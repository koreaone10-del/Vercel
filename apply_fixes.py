from pathlib import Path
import re
from html import escape

ROOT = Path(__file__).parent
SITE_URL = "https://x-five-kappa-98.vercel.app"
OLD_URL = "https://ultra-compressor-three.vercel.app"

PAGES = {
    "download-tiktok-without-watermark-hd": {
        "title": "Download TikTok Videos for Personal Use | OMEGA",
        "description": "Process a public TikTok URL for personal use. Learn what the browser tool can retrieve, its external-service limits, and your responsibility to respect creator rights.",
        "heading": "TikTok video link processor",
        "intro": "Use this page to process a public TikTok link for content you own or have permission to download. The browser requests metadata from an external provider, so availability depends on the provider and the source video.",
        "steps": ["Paste a public TikTok URL.", "Review the returned creator and video information.", "Download only content you are allowed to use."],
        "faq": [("Does the tool work for every TikTok URL?", "No. Private, removed, region-restricted, or unsupported URLs may fail because the tool depends on an external provider."), ("Can I reuse downloaded videos?", "Only when you have permission or a legal right to reuse them. Removing a watermark does not transfer copyright."), ("Is my TikTok URL uploaded to OMEGA?", "The browser sends the URL to the configured third-party processing providers so they can resolve the media." )]
    },
    "extract-tiktok-audio-mp3-free": {
        "title": "Extract Audio from a TikTok Link for Personal Use | OMEGA",
        "description": "Extract available audio metadata from a public TikTok link for personal use, with clear provider, copyright, and browser limitations.",
        "heading": "TikTok audio processor",
        "intro": "This page provides a browser interface for processing audio associated with a public TikTok URL. It is not a license to redistribute music, and the result depends on the external provider and the source video.",
        "steps": ["Paste a public TikTok URL.", "Wait for the provider response.", "Save or use the result only where you have permission."],
        "faq": [("Is every TikTok audio track available?", "No. Provider availability, privacy settings, regional restrictions, and source changes can prevent retrieval."), ("Can I publish the extracted audio?", "Only if you have the necessary copyright or licensing permission."), ("Does OMEGA host the audio?", "The browser receives a URL from an external provider; OMEGA does not promise permanent hosting or availability.")]
    },
    "tiktok-story-video-saver-hd": {
        "title": "Save Public TikTok Stories for Personal Use | OMEGA",
        "description": "Process a public TikTok story link for personal use while explaining availability, third-party provider limits, and creator rights.",
        "heading": "Public TikTok story processor",
        "intro": "Use this page for public content that you own or are authorized to save. Stories can expire or be unavailable, and the external processing provider may change its response.",
        "steps": ["Paste a public story URL.", "Check that the returned item is the intended content.", "Use the file only under applicable rights and permissions."],
        "faq": [("Why might a story fail?", "Stories may expire, be private, be region restricted, or be unsupported by the external provider."), ("Does saving a story grant reuse rights?", "No. You remain responsible for permission, attribution, and copyright compliance."), ("Does this page bypass private accounts?", "No. It is intended for public URLs and does not provide access to private content.")]
    },
    "youtube-thumbnail-downloader-4k": {
        "title": "Download a YouTube Thumbnail in the Highest Available Resolution | OMEGA",
        "description": "Extract the highest available YouTube thumbnail image from a video or Shorts URL in your browser, with a fallback when the largest image is unavailable.",
        "heading": "YouTube thumbnail extractor",
        "intro": "Paste a YouTube video or Shorts URL to resolve its thumbnail image. The tool checks the highest available standard thumbnail and falls back when that image does not exist. Actual resolution is controlled by YouTube source availability.",
        "steps": ["Paste a YouTube watch or Shorts URL.", "Preview the resolved thumbnail.", "Download it only when your intended use is permitted."],
        "faq": [("Is every thumbnail really 4K?", "No. The tool requests the highest available YouTube thumbnail, but YouTube may provide a lower resolution for a particular video."), ("Does it download the video?", "No. It extracts a thumbnail image URL only."), ("Can I use a creator's thumbnail commercially?", "Check the creator's permission and applicable copyright rules before reuse.")]
    },
    "extract-youtube-shorts-cover-image": {
        "title": "Extract a YouTube Shorts Thumbnail | OMEGA",
        "description": "Extract the available thumbnail image from a YouTube Shorts URL in your browser, with clear resolution and reuse limitations.",
        "heading": "YouTube Shorts thumbnail extractor",
        "intro": "This focused tool accepts a YouTube Shorts link and resolves the associated thumbnail image. It does not download the Shorts video and cannot create a thumbnail that YouTube has not provided.",
        "steps": ["Paste a YouTube Shorts URL.", "Preview the available cover image.", "Download and reuse it only with appropriate permission."],
        "faq": [("What if the Shorts thumbnail is missing?", "The source may not provide the requested image, so the tool uses the available fallback or reports an error."), ("Does this tool download Shorts?", "No. It retrieves a thumbnail image only."), ("Can I edit the thumbnail?", "You may edit it only when your intended use and the copyright holder's terms allow it.")]
    },
    "youtube-video-cover-grabber-online": {
        "title": "Get a YouTube Video Cover Image Online | OMEGA",
        "description": "Resolve a YouTube video's available cover image from a valid URL, preview it in the browser, and download the image when permitted.",
        "heading": "YouTube cover image tool",
        "intro": "This page extracts a cover image from a YouTube URL rather than downloading the underlying video. Resolution varies by the source video and YouTube's available thumbnail endpoints.",
        "steps": ["Paste a valid YouTube URL.", "Confirm the preview and resolution.", "Download the image only for an allowed use."],
        "faq": [("What URLs are accepted?", "The interface supports common YouTube watch and Shorts URL formats."), ("Why is the image not maximum resolution?", "Some videos do not have a maximum-resolution thumbnail, so the browser uses a fallback."), ("Does OMEGA store the image?", "The page displays an image returned by YouTube's image endpoint; storage and reuse remain your responsibility.")]
    },
    "free-ai-video-generator-veo-3": {
        "title": "Browser-Based Procedural AI Video Studio | OMEGA",
        "description": "Create a short procedural motion video in the browser using a generated still image, Canvas animation, and MediaRecorder. No promise of native Veo-3 access.",
        "heading": "Procedural AI video studio",
        "intro": "The current implementation requests a generated still image from an external image service, animates it with Canvas camera motion, and records a short WebM video locally. It is a procedural browser workflow, not a direct native Veo-3 rendering API.",
        "steps": ["Enter a visual prompt and choose a motion style.", "Wait for the still image and Canvas animation.", "Preview and download the recorded WebM file."],
        "faq": [("Does this page call the official Veo-3 model?", "No. The repository implementation uses an external image endpoint and local Canvas/MediaRecorder animation."), ("Is the generated video stored on OMEGA?", "The recording is created in the browser, while the source still image is requested from the configured external image service."), ("Why can generation fail?", "The external image service, browser codec support, network, or device memory can cause failure.")]
    },
    "generate-cinematic-ai-shorts-free": {
        "title": "Create Short Cinematic Browser Videos | OMEGA",
        "description": "Generate a short cinematic browser video from a prompt using an external still-image service and local Canvas motion recording.",
        "heading": "Cinematic short video maker",
        "intro": "Create a short motion clip from a prompt. The implementation combines an externally generated image with local camera movement and WebM recording, so output and availability depend on the browser and provider.",
        "steps": ["Write a concise visual prompt.", "Choose the camera motion and style.", "Preview the short WebM result before saving it."],
        "faq": [("Is this a full text-to-video model?", "No. It generates a still image and applies procedural motion locally."), ("Which format is downloaded?", "The browser records a WebM video when MediaRecorder supports the required codec."), ("Can I use the generated result commercially?", "Check the terms of the external image service and any third-party assets before commercial use.")]
    },
    "flux-text-to-video-ai-cinema": {
        "title": "Flux-Style Prompt to Cinematic Browser Video | OMEGA",
        "description": "Turn a visual prompt into a short cinematic browser recording using an external still-image generation endpoint and local Canvas motion.",
        "heading": "Prompt-to-cinematic browser tool",
        "intro": "This page provides a transparent browser workflow: a still image is requested from an external image endpoint, then the page adds procedural pan, zoom, and lighting effects before recording a WebM clip.",
        "steps": ["Enter a prompt without sensitive personal data.", "Let the browser load the still image.", "Preview and save the local WebM recording."],
        "faq": [("Does Flux run inside the browser?", "No. The browser requests an image from the configured external service and performs the motion stage locally."), ("Will every browser support the export?", "Support depends on Canvas capture and MediaRecorder codec availability."), ("Can I control the source image license?", "Review the external service terms and use prompts and outputs lawfully.")]
    },
    "compress-shopify-images-to-webp": {
        "title": "Compress Shopify Product Images to WebP in Your Browser | OMEGA",
        "description": "Compress Shopify product images to WebP locally in your browser, compare file sizes, and download an optimized copy without server upload.",
        "heading": "Shopify image to WebP optimizer",
        "intro": "Prepare a product image for a Shopify workflow by converting it to WebP locally. The tool does not upload your file to OMEGA. Check the result in your store theme and keep the original before replacing production assets.",
        "steps": ["Choose a product image.", "Adjust the compression level.", "Compare the original and WebP sizes, then download the result."],
        "faq": [("Does this upload my Shopify image?", "The WebP conversion is performed in the browser with Canvas; the page does not need an OMEGA upload."), ("Will WebP always be smaller?", "Not always. The result depends on the source image, dimensions, and quality setting."), ("Can I replace Shopify files automatically?", "No. Download the result and upload it through your normal Shopify workflow.")]
    },
    "convert-discord-stickers-to-webp": {
        "title": "Convert Discord Stickers to WebP Locally | OMEGA",
        "description": "Convert an image or sticker asset to WebP in your browser, compare the output size, and download the converted file locally.",
        "heading": "Discord sticker WebP converter",
        "intro": "Convert a sticker asset to WebP without sending the image to an OMEGA server. Discord's own dimensions, file-size, and usage requirements still apply, so validate the downloaded file before upload.",
        "steps": ["Select a sticker image supported by the browser.", "Choose a quality level.", "Download the WebP and validate it against Discord requirements."],
        "faq": [("Does the tool upload my sticker?", "No. The conversion is performed locally with the browser Canvas API."), ("Does it preserve animation?", "The current image workflow is intended for still images; animated assets may not be preserved as animation."), ("Is every WebP accepted by Discord?", "You must check Discord's current asset requirements after conversion.")]
    },
    "optimize-wordpress-images-webp": {
        "title": "Optimize WordPress Images as WebP Locally | OMEGA",
        "description": "Convert a WordPress image to WebP locally in your browser, measure the output size, and download the optimized copy for your media workflow.",
        "heading": "WordPress WebP image optimizer",
        "intro": "Create a WebP copy before uploading it to WordPress. Local processing helps keep the source image in your browser, but WordPress themes, caching, and image dimensions still determine the final page performance.",
        "steps": ["Select a source image.", "Tune the quality slider for the visual result you need.", "Download and upload the WebP through your WordPress media workflow."],
        "faq": [("Does WebP alone guarantee better SEO?", "No. Image dimensions, responsive delivery, accessibility, content quality, and page performance also matter."), ("Does the conversion require an upload?", "No. The current WebP conversion uses Canvas in the browser."), ("Should I keep the original?", "Yes. Keep the original source so you can create another quality or format later.")]
    },
    "etsy-product-photo-compressor": {
        "title": "Compress Etsy Product Photos to WebP Locally | OMEGA",
        "description": "Create a smaller WebP copy of a product photo in your browser, compare the size, and download it for a permitted Etsy workflow.",
        "heading": "Etsy product photo optimizer",
        "intro": "Optimize a product photo locally before using it in your commerce workflow. Always verify Etsy's current accepted formats and visual quality requirements, and keep the original file.",
        "steps": ["Select a product photo.", "Adjust quality while checking the preview metrics.", "Download the WebP and validate it before publishing."],
        "faq": [("Will the tool preserve every photo detail?", "WebP quality is adjustable, but lossy compression can remove detail. Compare the result before publishing."), ("Is my product photo uploaded?", "The conversion itself runs locally in the browser."), ("Does this upload to Etsy?", "No. It only creates a downloadable local copy.")]
    },
}


def clean_external_ads(text: str) -> str:
    text = re.sub(r'\s*<!--\s*(?:Adsterra|إعلان Adsterra).*?-->\s*<script[^>]+profitableratecpmnetwork\.com[^>]*></script>', '', text, flags=re.I|re.S)
    text = re.sub(r'\s*<script[^>]+profitableratecpmnetwork\.com[^>]*></script>', '', text, flags=re.I)
    text = re.sub(r'\s+onclick="triggerSmartlinkMonetization\(\)"', '', text)
    text = text.replace('rel="dofollow noopener"', 'rel="sponsored nofollow noopener"')
    text = re.sub(r'\s*// رابط Adsterra Smartlink المباشر عالي العائد المعتمد\s*const SMARTLINK_URL\s*=.*?function triggerSmartlinkMonetization\(\)\s*\{.*?\}\s*', '\n', text, flags=re.S)
    return text


AD_HEAD = '<script defer src="https://pl31380433.profitableratecpmnetwork.com/ff/5f/83/ff5f8391dca0db6a910d6256c4e3ae4c.js"></script>'
AD_SOCIAL = '<script defer src="https://pl31380434.profitableratecpmnetwork.com/a7/ef/35/a7ef35450a993db38aa0a0996b5c4da6.js"></script>'


def restore_ads(text: str, is_index: bool = False) -> str:
    """Keep monetization while leaving the actual download href untouched."""
    text = text.replace('\n}\n\n    const translations', '\n    const translations', 1)
    text = re.sub(r'\s*<script[^>]+profitableratecpmnetwork\.com[^>]*></script>', '', text, flags=re.I)
    text = text.replace('</head>', f'  {AD_HEAD}\n</head>', 1)
    text = text.replace('</body>', f'  {AD_SOCIAL}\n</body>', 1)
    if is_index:
        monetization = '''
    const SMARTLINK_URL = "https://www.profitableratecpmnetwork.com/ns71n37a0?key=d496ca279caa580cdfddebcb2aff24a6";
    function triggerSmartlinkMonetization(event) {
      if (event) event.stopPropagation();
      if (SMARTLINK_URL) window.open(SMARTLINK_URL, '_blank', 'noopener,noreferrer');
    }
    window.addEventListener('DOMContentLoaded', () => {
      ['downloadTrigger', 'veoDownloadBtn', 'tiktokDownloadNoWatermark', 'tiktokDownloadAudio', 'ytDownloadBtn', 'pdfDownloadBtn']
        .map((id) => document.getElementById(id)).filter(Boolean)
        .forEach((button) => button.addEventListener('click', (event) => {
          setTimeout(() => triggerSmartlinkMonetization(event), 50);
        }));
    });
'''
        text = text.replace('\n}\n\n    const translations', '\n' + monetization + '\n    const translations', 1)
        text = text.replace('  <script>\n    const translations', '  <script>\n' + monetization + '\n    const translations', 1)
    return text


def replace_schema(text: str, page_url: str, name: str, description: str, faqs=None) -> str:
    text = re.sub(r'\s*<!-- FAQ Schema.*?</script>\s*', '\n', text, flags=re.S|re.I)
    text = re.sub(r'\s*<!-- Structured Data JSON-LD -->.*?</script>\s*', '\n', text, flags=re.S|re.I)
    text = re.sub(r'\s*<script[^>]+type=["\']application/ld\+json["\'][^>]*>.*?</script>\s*', '\n', text, flags=re.S|re.I)
    app = {
        "@context": "https://schema.org", "@type": "WebApplication", "name": name,
        "url": page_url, "description": description, "applicationCategory": "MultimediaApplication",
        "operatingSystem": "All", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }
    import json
    blocks = [f'<script type="application/ld+json">\n{json.dumps(app, ensure_ascii=False, indent=2)}\n  </script>']
    if faqs:
        faq = {"@context":"https://schema.org", "@type":"FAQPage", "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
        blocks.append(f'<script type="application/ld+json">\n{json.dumps(faq, ensure_ascii=False, indent=2)}\n  </script>')
    marker = '<meta name="google-site-verification"'
    pos = text.find(marker)
    if pos >= 0:
        end = text.find('>', pos) + 1
        text = text[:end] + '\n  ' + '\n  '.join(blocks) + text[end:]
    return text


def add_page_content(text: str, data: dict) -> str:
    if 'id="seoPageContent"' in text:
        return text
    steps = ''.join(f'<li>{escape(x)}</li>' for x in data['steps'])
    faq = ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q,a in data['faq'])
    section = f'''\n  <section id="seoPageContent" class="w-full max-w-xl mx-auto px-4 pb-6 z-10" aria-labelledby="seoPageHeading">\n    <div class="bg-slate-950/80 border border-cyan-500/20 rounded-2xl p-5 text-slate-300 text-sm leading-7">\n      <h2 id="seoPageHeading" class="text-lg font-bold text-cyan-300 mb-2">{escape(data['heading'])}</h2>\n      <p>{escape(data['intro'])}</p>\n      <h3 class="text-base font-bold text-white mt-4 mb-2">How to use this tool</h3>\n      <ol class="list-decimal list-inside space-y-1">{steps}</ol>\n      <h3 class="text-base font-bold text-white mt-4 mb-2">Frequently asked questions</h3>\n      <div class="space-y-2">{faq}</div>\n    </div>\n  </section>\n'''
    text = text.replace('\n  <footer', section + '\n  <footer', 1)
    return text


def main():
    html_files = list(ROOT.glob('*.html'))
    for path in html_files:
        text = path.read_text(encoding='utf-8')
        text = text.replace(OLD_URL, SITE_URL)
        text = clean_external_ads(text)
        text = restore_ads(text, path.stem == 'index')
        text = re.sub(r'\s*<meta name="viewport"([^>]+)>', r'\n  <meta name="viewport"\1>', text, count=1)
        if 'name="robots"' not in text:
            text = text.replace('</head>', '  <meta name="robots" content="index,follow,max-image-preview:large">\n</head>', 1)
        slug = path.stem
        if slug == 'index':
            page_url = SITE_URL + '/'
            if re.search(r'<link[^>]+rel="canonical"', text, flags=re.I):
                text = re.sub(r'<link[^>]+rel="canonical"[^>]*>', f'<link rel="canonical" href="{page_url}">', text, count=1, flags=re.I)
            else:
                text = text.replace('</head>', f'  <link rel="canonical" href="{page_url}">\n</head>', 1)
            text = re.sub(r'<meta property="og:url"[^>]*>', f'<meta property="og:url" content="{page_url}">', text, count=1)
            text = re.sub(r'<meta property="og:title"[^>]*>', '<meta property="og:title" content="OMEGA Browser Media Tools">', text, count=1)
            text = re.sub(r'<meta property="og:description"[^>]*>', '<meta property="og:description" content="Browser-based WebP conversion, PDF compression, thumbnail extraction, and procedural video tools.">', text, count=1)
            text = replace_schema(text, page_url, 'OMEGA Browser Media Tools', 'Browser-based WebP conversion, PDF compression, thumbnail extraction, and procedural video tools.')
        else:
            data = PAGES.get(slug)
            if data:
                page_url = SITE_URL + '/' + slug + '.html'
                text = re.sub(r'<title[^>]*>.*?</title>', f'<title>{escape(data["title"])}</title>', text, count=1, flags=re.S|re.I)
                text = re.sub(r'<meta name="description"[^>]*>', f'<meta name="description" content="{escape(data["description"])}">', text, count=1, flags=re.I)
                if re.search(r'<link[^>]+rel="canonical"', text, flags=re.I):
                    text = re.sub(r'<link[^>]+rel="canonical"[^>]*>', f'<link rel="canonical" href="{page_url}">', text, count=1, flags=re.I)
                else:
                    text = text.replace('</head>', f'  <link rel="canonical" href="{page_url}">\n</head>', 1)
                text = re.sub(r'<meta property="og:url"[^>]*>', f'<meta property="og:url" content="{page_url}">', text, count=1)
                text = re.sub(r'<meta property="og:title"[^>]*>', f'<meta property="og:title" content="{escape(data["title"])}">', text, count=1)
                text = re.sub(r'<meta property="og:description"[^>]*>', f'<meta property="og:description" content="{escape(data["description"])}">', text, count=1)
                text = replace_schema(text, page_url, data['title'], data['description'], data['faq'])
                text = add_page_content(text, data)
            else:
                page_url = SITE_URL + '/' + path.name
                if re.search(r'<link[^>]+rel="canonical"', text, flags=re.I):
                    text = re.sub(r'<link[^>]+rel="canonical"[^>]*>', f'<link rel="canonical" href="{page_url}">', text, count=1, flags=re.I)
                else:
                    text = text.replace('</head>', f'  <link rel="canonical" href="{page_url}">\n</head>', 1)
                text = re.sub(r'<meta property="og:url"[^>]*>', f'<meta property="og:url" content="{page_url}">', text, count=1)
        path.write_text(text, encoding='utf-8')

    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n', encoding='utf-8')

    urls = [SITE_URL + '/'] + [SITE_URL + '/' + path.name for path in sorted(ROOT.glob('*.html')) if path.name != 'index.html']
    entries = []
    for url in urls:
        entries.append(f'  <url>\n    <loc>{url}</loc>\n  </url>')
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(entries) + '\n</urlset>\n', encoding='utf-8')
    print(f'Fixed {len(html_files)} HTML files, robots.txt, and sitemap.xml')

if __name__ == '__main__':
    main()
