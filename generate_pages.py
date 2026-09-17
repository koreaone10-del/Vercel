import os
import re

# بنك الكلمات المفتاحية عالي الاستهداف (Multi-Engine Cluster)
USE_CASES = [
    # 1. TikTok Viral Cluster
    {"slug": "download-tiktok-without-watermark-hd", "title": "Download TikTok Video Without Watermark HD", "target": "TikTok Creators & Video Editors", "default_tab": "tiktok"},
    {"slug": "extract-tiktok-audio-mp3-free", "title": "Extract TikTok Audio to MP3 Online", "target": "Music Producers & Creators", "default_tab": "tiktok"},
    {"slug": "tiktok-story-video-saver-hd", "title": "Save TikTok Stories & Videos in HD", "target": "Social Media Managers", "default_tab": "tiktok"},

    # 2. YouTube Thumbnail 4K Cluster
    {"slug": "youtube-thumbnail-downloader-4k", "title": "Download YouTube Video Thumbnails in 4K Ultra HD", "target": "YouTubers & Graphic Designers", "default_tab": "yt"},
    {"slug": "extract-youtube-shorts-cover-image", "title": "Extract YouTube Shorts Thumbnail HD", "target": "Shorts Creators", "default_tab": "yt"},
    {"slug": "youtube-video-cover-grabber-online", "title": "Instant YouTube Video Cover Grabber", "target": "Digital Marketers", "default_tab": "yt"},

    # 3. Veo-3 AI Cinema Cluster
    {"slug": "free-ai-video-generator-veo-3", "title": "Free Veo-3 AI Video Studio (Procedural Rendering)", "target": "AI Artists & Filmmakers", "default_tab": "veo"},
    {"slug": "generate-cinematic-ai-shorts-free", "title": "Generate Cinematic AI Videos for Reels & Shorts", "target": "Content Creators", "default_tab": "veo"},

    # 4. WebP Image Compression Cluster
    {"slug": "compress-shopify-images-to-webp", "title": "Compress Shopify Images to WebP (Boost Speed)", "target": "Shopify Store Owners", "default_tab": "webp"},
    {"slug": "convert-discord-stickers-to-webp", "title": "Convert Discord Custom Stickers to WebP", "target": "Discord Creators & Gamers", "default_tab": "webp"},
    {"slug": "optimize-wordpress-images-webp", "title": "Optimize WordPress Images to WebP Format", "target": "WordPress Bloggers & Developers", "default_tab": "webp"},
    {"slug": "etsy-product-photo-compressor", "title": "Etsy Product Photo Optimizer (WebP)", "target": "Etsy Sellers", "default_tab": "webp"}
]

DOMAIN = "https://ultra-compressor-three.vercel.app"

with open("index.html", "r", encoding="utf-8") as f:
    template = f.read()

new_urls = []

for case in USE_CASES:
    filename = f"{case['slug']}.html"
    new_urls.append(f"{DOMAIN}/{case['slug']}.html")
    
    page_content = template
    # تخصيص العناوين والوصف لكل صفحة
    page_content = re.sub(r"<title id=\"pageTitle\">.*?</title>", f"<title id=\"pageTitle\">{case['title']} // OMEGA Ω</title>", page_content)
    page_content = re.sub(r'<meta name="description" id="pageDesc".*?>', f'<meta name="description" id="pageDesc" content="Free instant tool to {case["title"].lower()}. Optimized specifically for {case["target"]} with zero latency.">', page_content)
    
    # جعل التبويب المناسب يفتح تلقائياً في الصفحة المخصصة
    tab_script = f"""
    <script>
      window.addEventListener('DOMContentLoaded', () => {{
        if (typeof switchEngine === 'function') {{
          switchEngine('{case["default_tab"]}');
        }}
      }});
    </script>
    </body>
    """
    page_content = page_content.replace("</body>", tab_script)

    with open(filename, "w", encoding="utf-8") as out:
        out.write(page_content)
    print(f"Generated Landing Page: {filename}")

# تحديث sitemap.xml تلقائياً
sitemap_file = "sitemap.xml"
if os.path.exists(sitemap_file):
    with open(sitemap_file, "r", encoding="utf-8") as f:
        sitemap_content = f.read()
    
    for url in new_urls:
        if url not in sitemap_content:
            entry = f"  <url>\n    <loc>{url}</loc>\n    <priority>0.9</priority>\n  </url>\n</urlset>"
            sitemap_content = sitemap_content.replace("</urlset>", entry)
            
    with open(sitemap_file, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Sitemap.xml updated with full programmatic cluster.")
