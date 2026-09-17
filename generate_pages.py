import os
import re

# الكلمات المفتاحية وسيناريوهات الاستهداف الشائعة
USE_CASES = [
    {"slug": "compress-shopify-images-to-webp", "title": "Compress Shopify Images to WebP (Boost Speed)", "target": "Shopify Store Owners"},
    {"slug": "convert-discord-stickers-to-webp", "title": "Convert Discord Custom Stickers to WebP", "target": "Discord Creators & Gamers"},
    {"slug": "optimize-wordpress-images-webp", "title": "Optimize WordPress Images to WebP Format", "target": "WordPress Bloggers & Developers"},
    {"slug": "etsy-product-photo-compressor", "title": "Etsy Product Photo Optimizer (WebP)", "target": "Etsy Sellers"},
    {"slug": "compress-woocommerce-product-photos", "title": "WooCommerce Image Compression Engine", "target": "E-Commerce Managers"},
    {"slug": "convert-png-banner-to-webp", "title": "Convert High-Res PNG Banners to WebP", "target": "Graphic Designers"},
    {"slug": "shrink-blog-images-lossless-webp", "title": "Lossless WebP Compression for Blogs", "target": "Content Creators"},
    {"slug": "midjourney-png-to-webp-converter", "title": "Compress Midjourney AI Images to WebP", "target": "AI Artists & Prompt Engineers"},
    {"slug": "youtube-thumbnail-webp-optimizer", "title": "Optimize YouTube Thumbnails to WebP", "target": "YouTubers & Video Editors"},
    {"slug": "veo-3-ai-video-prompt-generator", "title": "Veo-3 AI Video Studio & Cinematic Renderer", "target": "Shorts & TikTok Creators"}
]

DOMAIN = "https://ultra-compressor-three.vercel.app"

# قراءة الصفحة الرئيسية لاستخدام هيكلها كقالب
with open("index.html", "r", encoding="utf-8") as f:
    template = f.read()

new_urls = []

for case in USE_CASES:
    filename = f"{case['slug']}.html"
    new_urls.append(f"{DOMAIN}/{case['slug']}.html")
    
    # تخصيص العناوين وبيانات السيو لكل صفحة هبوط
    page_content = template
    page_content = re.sub(r"<title>.*?</title>", f"<title>{case['title']} // OMEGA Ω</title>", page_content)
    page_content = re.sub(r'<meta name="description".*?>', f'<meta name="description" content="Free instant tool to {case["title"].lower()}. Optimized specifically for {case["target"]} with zero server latency.">', page_content)
    
    with open(filename, "w", encoding="utf-8") as out:
        out.write(page_content)
    print(f"Generated: {filename}")

# تحديث ملف sitemap.xml تلقائياً
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
    print("Updated: sitemap.xml with programmatic URLs.")

