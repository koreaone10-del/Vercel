import os
import re

# بنك الكلمات المفتاحية الاستراتيجي للمحركات الأربعة
USE_CASES = [
    # 1. باقة أدوات TikTok HD
    {
        "slug": "download-tiktok-without-watermark-hd",
        "title": "Download TikTok Video Without Watermark HD",
        "target": "TikTok Creators & Video Editors",
        "default_tab": "tiktok"
    },
    {
        "slug": "extract-tiktok-audio-mp3-free",
        "title": "Extract TikTok Audio to MP3 Online Free",
        "target": "Music Producers & Audio Editors",
        "default_tab": "tiktok"
    },
    {
        "slug": "tiktok-story-video-saver-hd",
        "title": "Save TikTok Stories and Reels in Full HD",
        "target": "Social Media Managers",
        "default_tab": "tiktok"
    },

    # 2. باقة أدوات YouTube 4K
    {
        "slug": "youtube-thumbnail-downloader-4k",
        "title": "Download YouTube Video Thumbnails in 4K Ultra HD",
        "target": "YouTubers & Graphic Designers",
        "default_tab": "yt"
    },
    {
        "slug": "extract-youtube-shorts-cover-image",
        "title": "Extract YouTube Shorts Thumbnail HD",
        "target": "Shorts Creators & Streamers",
        "default_tab": "yt"
    },
    {
        "slug": "youtube-video-cover-grabber-online",
        "title": "Instant YouTube Video Cover Grabber",
        "target": "Digital Content Publishers",
        "default_tab": "yt"
    },

    # 3. باقة أدوات Veo-3 AI Cinema
    {
        "slug": "free-ai-video-generator-veo-3",
        "title": "Free Veo-3 AI Video Studio (Procedural Rendering)",
        "target": "AI Artists & Filmmakers",
        "default_tab": "veo"
    },
    {
        "slug": "generate-cinematic-ai-shorts-free",
        "title": "Generate Cinematic AI Videos for Reels & Shorts",
        "target": "Content Creators & Marketers",
        "default_tab": "veo"
    },
    {
        "slug": "flux-text-to-video-ai-cinema",
        "title": "Flux Text to Video AI Generator in Browser",
        "target": "Creative Directors & Designers",
        "default_tab": "veo"
    },

    # 4. باقة ضغط وتحويل WebP
    {
        "slug": "compress-shopify-images-to-webp",
        "title": "Compress Shopify Images to WebP (Boost Speed)",
        "target": "Shopify Store Owners",
        "default_tab": "webp"
    },
    {
        "slug": "convert-discord-stickers-to-webp",
        "title": "Convert Discord Custom Stickers to WebP",
        "target": "Discord Creators & Gamers",
        "default_tab": "webp"
    },
    {
        "slug": "optimize-wordpress-images-webp",
        "title": "Optimize WordPress Images to WebP Format",
        "target": "WordPress Bloggers & Developers",
        "default_tab": "webp"
    },
    {
        "slug": "etsy-product-photo-compressor",
        "title": "Etsy Product Photo Optimizer (WebP)",
        "target": "Etsy Sellers & Handcrafters",
        "default_tab": "webp"
    }
]

DOMAIN = "https://ultra-compressor-three.vercel.app"
TEMPLATE_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"

if not os.path.exists(TEMPLATE_FILE):
    raise FileNotFoundError(f"Template file '{TEMPLATE_FILE}' not found.")

with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template_content = f.read()

clean_urls = []

for case in USE_CASES:
    slug = case["slug"]
    title = case["title"]
    target = case["target"]
    tab = case["default_tab"]
    
    clean_url = f"{DOMAIN}/{slug}"
    filename = f"{slug}.html"
    clean_urls.append(clean_url)
    
    page = template_content
    
    # 1. تخصيص العنوان والوصف
    page = re.sub(
        r'<title id="pageTitle">.*?</title>',
        f'<title id="pageTitle">{title} // OMEGA Ω</title>',
        page
    )
    page = re.sub(
        r'<meta name="description" id="pageDesc".*?>',
        f'<meta name="description" id="pageDesc" content="Free instant online tool to {title.lower()}. Optimized for {target} with zero server upload and ultra high-speed processing.">',
        page
    )

    # 2. حقن وسم Canonical لحماية السيو
    canonical_tag = f'<link rel="canonical" href="{clean_url}" />\n  <meta property="og:url" content="{clean_url}">'
    page = re.sub(r'<meta property="og:url".*?>', canonical_tag, page)

    # 3. تخصيص وسوم التواصل الاجتماعي
    page = re.sub(
        r'<meta property="og:title".*?>',
        f'<meta property="og:title" content="{title} // OMEGA Ω">',
        page
    )
    page = re.sub(
        r'<meta name="twitter:title".*?>',
        f'<meta name="twitter:title" content="{title} // OMEGA Ω">',
        page
    )

    # 4. تفعيل التبويب المخصص للزائر تلقائياً
    activation_script = f"""
  <!-- Programmatic Tab Auto-Switcher -->
  <script>
    window.addEventListener('DOMContentLoaded', () => {{
      if (typeof switchEngine === 'function') {{
        switchEngine('{tab}');
      }}
    }});
  </script>
</body>"""
    page = page.replace("</body>", activation_script)

    with open(filename, "w", encoding="utf-8") as out:
        out.write(page)
    print(f"Generated Landing Page: {filename} (Tab: {tab})")

# تحديث sitemap.xml بالروابط النظيفة
if os.path.exists(SITEMAP_FILE):
    with open(SITEMAP_FILE, "r", encoding="utf-8") as sf:
        sitemap_data = sf.read()

    added = 0
    for url in clean_urls:
        if url not in sitemap_data:
            entry = f"  <url>\n    <loc>{url}</loc>\n    <priority>0.9</priority>\n  </url>\n</urlset>"
            sitemap_data = sitemap_data.replace("</urlset>", entry)
            added += 1

    with open(SITEMAP_FILE, "w", encoding="utf-8") as sf:
        sf.write(sitemap_data)
    print(f"Sitemap updated: {added} new canonical URLs injected.")
