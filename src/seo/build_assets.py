import sys, glob, os
sys.path.insert(0, sys.argv[1] + '/seo')
from parts import *
from PIL import Image

OUT = sys.argv[2]

# Re-encode photos as progressive JPEGs, and add 800px versions for srcset
for f in sorted(glob.glob(OUT + '/images/*.jpg')):
    if f.endswith('-800.jpg') or f.endswith('og-image.jpg'):
        continue
    im = Image.open(f).convert('RGB')
    im.save(f, quality=80, optimize=True, progressive=True)
    s = im.copy(); s.thumbnail((800, 800))
    s.save(f[:-4] + '-800.jpg', quality=78, optimize=True, progressive=True)

pages = ['index.html'] + [u for u, _ in PAGES.values()] + [u for u, _ in GUIDES.values()]
urls = ''.join(f'  <url><loc>{SITE}/{"" if p == "index.html" else p}</loc><lastmod>2026-10-25</lastmod></url>\n' for p in pages)
open(OUT + '/sitemap.xml', 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(OUT + '/robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /print/\n\nSitemap: {SITE}/sitemap.xml\n')
open(OUT + '/site.webmanifest', 'w').write('{"name":"VAG Euro Automotive","short_name":"VAG Euro","icons":[{"src":"apple-touch-icon.png","sizes":"180x180","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#0A0A0A","background_color":"#0A0A0A","display":"browser"}\n')
open(OUT + '/netlify.toml', 'w').write('''[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/images/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000"

[[headers]]
  for = "/brand/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000"

[[redirects]]
  from = "https://www.vageuroautomotive.com.au/*"
  to = "https://vageuroautomotive.com.au/:splat"
  status = 301
  force = true
''')
print('assets ok')
