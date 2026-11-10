import re, sys
sys.path.insert(0, sys.argv[1] + '/seo')
from parts import *

SRC, OUT = sys.argv[2], sys.argv[3]
s = open(SRC).read()

# 1. Pull the stylesheet out so every page shares it
css = re.search(r'<style>\n(.*?)</style>', s, re.S).group(1)
css = css.replace('/* Booking pitch */\n.pitch .wrap { padding-block: 110px; display: grid; gap: 28px; justify-items: center; text-align: center; }\n.pitch p { color: var(--muted); max-width: 54ch; }\n.pitch .note { font-size: 0.86rem; color: #7A7A7A; }\n', '')
css += open(sys.argv[1] + '/seo/extra.css').read()
open(OUT + '/css/site.css', 'w').write(css)

body = s[s.index('<main id="top">'):s.index('<footer>')]
script = s[s.index('<script>\n(function () {'):]


def rep(a, b, n=1):
    global body
    assert body.count(a) == n, (a[:80], body.count(a))
    body = body.replace(a, b)


# 2. Hero: keyword-bearing H1, visible
rep('''      <p class="eyebrow">VAG Euro Automotive · Seaford</p>
      <h1>Experience<br><span style="color:var(--accent)">precision.</span></h1>''',
    '''      <h1><span class="eyebrow h1-kicker">Audi &amp; VW mechanic · Seaford</span>Experience<br><span style="color:var(--accent)">precision.</span></h1>
      <p class="hero-sub">Specialist car servicing and repairs for Audi, Volkswagen and European cars in Seaford, minutes from Frankston.</p>''')
rep('<img src="images/three-hoists.jpg" alt="Three cars raised on hoists across the VAG Euro Automotive workshop" width="1200" height="1600" style="object-position:50% 58%">',
    '<img src="images/three-hoists.jpg" srcset="images/three-hoists-800.jpg 800w, images/three-hoists.jpg 1200w" sizes="100vw" alt="Cars on hoists in the VAG Euro Automotive mechanic workshop in Seaford" width="1200" height="1600" fetchpriority="high" style="object-position:50% 58%">')

# 3. Intro copy with the target words used naturally
rep('<h2>Audi, Volkswagen and European vehicle service specialist.</h2>', '<h2>Your Audi and Volkswagen mechanic in Seaford.</h2>')
rep("<p>VAG Euro Automotive has been looking after Volkswagen Group cars in Melbourne's south-east for more than five years. Workshop manager Vic and a team of qualified technicians service and repair everything from a daily Golf to an RS 3. We also look after Porsche, Mercedes-Benz, BMW and other European cars.</p>",
    "<p>VAG Euro Automotive is an independent car mechanic on Stephenson Road in Seaford, a few minutes from Frankston. For more than five years we've serviced and repaired Volkswagen Group cars for drivers across Melbourne's south-east. Workshop manager Vic and a team of qualified mechanics look after everything from a daily Golf to an Audi RS 3. We also service Skoda, Cupra, Porsche, Mercedes-Benz, BMW and other European cars.</p>")

# 4. Marques link to the make pages
rep('<a href="#services">Audi</a><a href="#services">Volkswagen</a><a href="#services">Skoda</a><a href="#services">Porsche</a><a href="#services">Mercedes-Benz</a><a href="#services">BMW</a>',
    f'<a href="{PAGES["audi"][0]}">Audi</a><a href="{PAGES["vw"][0]}">Volkswagen</a><a href="{PAGES["euro"][0]}">Skoda</a><a href="{PAGES["euro"][0]}">Porsche</a><a href="{PAGES["euro"][0]}">Mercedes-Benz</a><a href="{PAGES["euro"][0]}">BMW</a>')

# 5. Feature
rep('<img src="images/porsche-718-cayman.jpg" alt="White Porsche 718 Cayman in the workshop"', '<img src="images/porsche-718-cayman.jpg" srcset="images/porsche-718-cayman-800.jpg 800w, images/porsche-718-cayman.jpg 1600w" sizes="100vw" alt="Porsche 718 Cayman in for a service at our Seaford car mechanic workshop"')
rep('<h2>European vehicle specialists</h2>', '<h2>European car specialists</h2>')
rep('<a class="btn" href="#services">More about our services</a>', f'<a class="btn" href="{PAGES["euro"][0]}">European car servicing</a>')

# 6. Tiles go to the make pages
rep('<a class="tile" href="#services"><img src="images/golf-gti-pair.jpg" alt="Two Volkswagen Golf GTIs in the workshop"', f'<a class="tile" href="{PAGES["vw"][0]}"><img src="images/golf-gti-pair.jpg" srcset="images/golf-gti-pair-800.jpg 800w, images/golf-gti-pair.jpg 1600w" sizes="(min-width: 860px) 33vw, 100vw" alt="Two Volkswagen Golf GTIs in for logbook servicing in Seaford"')
rep('<a class="tile" href="#services"><img src="images/technician-718-hoist.jpg"', f'<a class="tile" href="{PAGES["euro"][0]}"><img src="images/technician-718-hoist.jpg" srcset="images/technician-718-hoist-800.jpg 800w, images/technician-718-hoist.jpg 1200w" sizes="(min-width: 860px) 33vw, 100vw"')
rep('<a class="tile" href="#services"><img src="images/under-car-exhaust.jpg" alt="Technician working under a raised Porsche"', f'<a class="tile" href="{PAGES["audi"][0]}"><img src="images/under-car-exhaust.jpg" srcset="images/under-car-exhaust-800.jpg 800w, images/under-car-exhaust.jpg 1200w" sizes="(min-width: 860px) 33vw, 100vw" alt="Mechanic inspecting brakes and suspension under a raised car"')

# 7. Services intro
rep('<li><b>DSG &amp; S tronic</b><span>Oil services, mechatronic and clutch faults</span></li>', f'<li><b><a href="{PAGES["dsg"][0]}">DSG &amp; transmission</a></b><span>DSG, S tronic and automatic gearbox repairs</span></li>\n        <li><b><a href="{PAGES["mech"][0]}">Mechatronic unit repair</a></b><span>DSG and S tronic mechatronic faults and repairs</span></li>')
rep('<li><b>Engine &amp; cooling</b><span>Leaks, coil packs, pumps, thermostats</span></li>', f'<li><b><a href="{PAGES["pump"][0]}">Water pumps &amp; cooling</a></b><span>VW water pumps, thermostat housings and coolant leaks</span></li>')
rep('<li><b>Clutch &amp; differential</b><span>Manual clutches, Haldex and quattro</span></li>', '<li><b>quattro &amp; Haldex</b><span>Haldex services, quattro, 4MOTION and differentials</span></li>\n        <li><b>Diesel &amp; DPF</b><span>DPF repairs, EGR faults and TDI diesels</span></li>')
rep('<h2>What we look after</h2>', '<h2>Car servicing &amp; repairs</h2>')

# 8. Gallery: srcset, honest button
body = re.sub(r'(<img src="images/([\w-]+)\.jpg")( alt="[^"]*" width="(\d+)" height="\d+" loading="lazy")',
              lambda m: m.group(1) + f' srcset="images/{m.group(2)}-800.jpg 800w, images/{m.group(2)}.jpg {m.group(4)}w" sizes="(min-width: 860px) 25vw, 50vw"' + m.group(3)
              if 'srcset' not in m.group(0) else m.group(0), body)
rep('<a class="btn" href="#visit">Follow us on Instagram</a>', '<a class="btn" href="#book">Book a service</a>')
rep('<h2>In the workshop</h2>', '<h2>Inside our Seaford workshop</h2>')

# 9. Guides link to real articles
for k, (u, t) in GUIDES.items():
    rep(f'<h3>{t}</h3>', f'<h3><a href="{u}">{t}</a></h3>')
body = body.replace('<a class="more" href="#guides">Read article</a>', '§')
for u, t in GUIDES.values():
    body = body.replace('§', f'<a class="more" href="{u}" aria-label="Read: {t}">Read article</a>', 1)

# 10. FAQ + areas before Contact
QA = [
    ('Will servicing my new Audi or Volkswagen with you void the warranty?', 'No. In Australia, using an independent mechanic does not void your new-car warranty as long as the servicing follows the manufacturer\'s specifications. We follow the manufacturer\'s logbook schedule, use parts and oils that meet the right specifications, and stamp your logbook.'),
    ('Do you only work on Audi and Volkswagen?', 'Audi and Volkswagen are our speciality, and we also service Skoda, Cupra, Porsche, Mercedes-Benz, BMW, Mini and other European cars.'),
    ('Where is your workshop?', 'We are at 11 Stephenson Road, Seaford VIC 3198, a short drive from Frankston, Carrum Downs and Chelsea. We are open Monday to Friday 8:00 to 5:00 and Saturday 8:30 to 2:00.'),
    ('How do I book my car in?', f'Use the booking form on this page to choose your car, what it needs and a drop-off time, or call us on {PHONE}. We call you to confirm and give you a quote before any work starts.'),
    ('Do you have loan cars?', 'Yes, loan cars are available on request, subject to availability. You can also wait in our lounge for shorter jobs, or use the key drop box to drop off early or after hours.'),
    ('Do you repair DSG gearboxes and mechatronic units?', 'Yes. We service and repair DSG and S tronic transmissions, including mechatronic unit diagnosis and repair, often without replacing the whole gearbox.'),
    ('Do you do quattro, Haldex and DPF repairs?', 'Yes. We service Haldex all-wheel-drive systems on Audi quattro and Volkswagen 4MOTION cars, and diagnose and repair diesel particulate filter (DPF) and EGR faults on TDI diesels.'),
    ('Can I pay with Afterpay or Zip?', 'Yes. We accept EFTPOS, Visa, Mastercard, Afterpay, Zip and humm.'),
]
areas = ''.join(f'<li>{a}</li>' for a in AREAS)
rep('  <section class="visit-sec on-light" id="visit">', faq_html(QA) + f'''  <section class="areas">
    <div class="wrap">
      <div style="display:grid;gap:14px;align-content:start"><p class="eyebrow">Areas we service</p><h2>Car mechanic for Seaford, Frankston and surrounds</h2></div>
      <div style="display:grid;gap:22px"><p>Our workshop is in the Seaford industrial area off Stephenson Road, easy to reach from Frankston, Patterson Lakes, Carrum Downs and Chelsea. Customers bring their Audi, Volkswagen and European cars to us from:</p><ul class="area-list">{areas}</ul><p style="display:flex;gap:24px;flex-wrap:wrap"><a class="more" href="{PAGES['seaford'][0]}">Mechanic Seaford</a><a class="more" href="{PAGES['frankston'][0]}">Frankston mechanic</a><a class="more" href="{PAGES['patterson'][0]}">Mechanic near Patterson Lakes</a></p></div>
    </div>
  </section>

  <section class="visit-sec on-light" id="visit">''')
rep('<h2>Visit our workshop</h2>', '<h2>Visit our Seaford workshop</h2>')

# 11. Script: drop the footer-only bits now handled by FOOT_JS? Keep the original page script (hours, booking, signup).
schema = {'@graph': [BUSINESS,
                     {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': NAME, 'publisher': {'@id': SITE + '/#business'}, 'inLanguage': 'en-AU'},
                     {'@type': 'WebPage', '@id': SITE + '/#webpage', 'url': SITE + '/', 'name': 'Audi & VW Mechanic Seaford | VAG Euro Automotive', 'about': {'@id': SITE + '/#business'}, 'isPartOf': {'@id': SITE + '/#website'}},
                     faq_schema(QA)]}
title = 'Audi &amp; VW Mechanic Seaford, near Frankston | VAG Euro Automotive'
desc = f'Audi & Volkswagen mechanic in Seaford, near Frankston & Patterson Lakes. DSG & transmission repair, mechatronics, VW water pumps and logbook servicing. Call {PHONE}.'
pre = '<link rel="preload" as="image" href="images/three-hoists.jpg" imagesrcset="images/three-hoists-800.jpg 800w, images/three-hoists.jpg 1200w" imagesizes="100vw" fetchpriority="high">\n'
html = head(title, desc, 'index.html', schema, extra=pre).replace('<title>' + title + '</title>', '<title>Audi & VW Mechanic Seaford, near Frankston | VAG Euro Automotive</title>')
html = html.replace(f'content="{title}"', 'content="Audi & VW Mechanic Seaford, near Frankston | VAG Euro Automotive"')
html += header(True) + '\n' + body + footer(True) + '\n' + script
open(OUT + '/index.html', 'w').write(html)
print('ok', len(html))
