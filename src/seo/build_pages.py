import sys
sys.path.insert(0, sys.argv[1] + '/seo')
from parts import *

OUT = sys.argv[2]
BOOK = 'index.html#book'


def aside(points):
    lis = ''.join(f'<li>{p}</li>' for p in points)
    return f'''<aside class="aside">
        <p class="eyebrow">Book a service</p>
        <h3>Seaford workshop</h3>
        <p>11 Stephenson Road, Seaford VIC 3198<br>Mon–Fri 8:00–5:00 · Sat 8:30–2:00</p>
        <p class="tel"><a href="{TEL}">{PHONE}</a></p>
        <ul class="chips-static">{lis}</ul>
        <a class="btn btn-solid" href="{BOOK}">Book online</a>
      </aside>'''


def cta(h):
    return f'''  <section class="cta-band on-light">
    <div class="wrap">
      <p class="eyebrow">Bookings</p>
      <h2>{h}</h2>
      <p>Pick your car, what it needs and a drop-off time online. We call to confirm and quote before any work starts.</p>
      <div class="actions"><a class="btn btn-solid" href="{BOOK}">Book online</a><a class="btn" href="{TEL}">Call {PHONE}</a></div>
    </div>
  </section>
'''


def more(exclude):
    links = [(u, {'audi': 'Audi mechanic Seaford', 'vw': 'Volkswagen mechanic Seaford', 'euro': 'European car mechanic Seaford', 'frankston': 'Mechanic near Frankston'}[k]) for k, (u, n) in PAGES.items() if u != exclude]
    links += [(u, t) for u, t in GUIDES.values() if u != exclude]
    lis = ''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in links[:6])
    return f'''  <section class="more-links">
    <div class="wrap">
      <p class="eyebrow">Keep reading</p>
      <ul>{lis}</ul>
    </div>
  </section>
'''


def page(path, title, desc, h1, kicker, intro, img, img_alt, prose, points, qas, cta_h, crumb, extra_schema=None, og=None):
    url = SITE + '/' + path
    graph = [BUSINESS, breadcrumb([('Home', SITE + '/'), (crumb, url)])]
    if qas:
        graph.append(faq_schema(qas))
    if extra_schema:
        graph.append(extra_schema)
    html = head(title, desc, path, {'@graph': graph})
    html += header(False)
    from PIL import Image
    w, hgt = Image.open(f'{OUT}/images/{img}.jpg').size
    html += f'''
<main id="top">
  <section class="page-hero">
    <img src="images/{img}.jpg" srcset="images/{img}-800.jpg 800w, images/{img}.jpg {w}w" sizes="100vw" alt="{img_alt}" width="{w}" height="{hgt}" fetchpriority="high">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span aria-current="page">{crumb}</span></nav>
      <p class="eyebrow">{kicker}</p>
      <h1>{h1}</h1>
      <p>{intro}</p>
      <div class="actions"><a class="btn btn-solid" href="{BOOK}">Book a service</a><a class="btn" href="{TEL}">Call {PHONE}</a></div>
    </div>
  </section>

  <section class="content">
    <div class="wrap">
      <article class="prose">
{prose}
      </article>
      {aside(points)}
    </div>
  </section>

{faq_html(qas, 'Common questions') if qas else ''}{cta(cta_h)}{more(path)}</main>

'''
    html += footer(False) + '\n' + FOOT_JS
    open(OUT + '/' + path, 'w').write(html)


def article(path, title, desc, h1, tag, intro, img, img_alt, prose, cta_h):
    url = SITE + '/' + path
    art = {'@type': 'Article', 'headline': h1, 'description': desc, 'image': SITE + f'/images/{img}.jpg', 'author': {'@id': SITE + '/#business'},
           'publisher': {'@id': SITE + '/#business'}, 'datePublished': '2026-10-25', 'dateModified': '2026-10-25', 'mainEntityOfPage': url, 'inLanguage': 'en-AU'}
    page(path, title, desc, h1, tag, intro, img, img_alt, prose, ['Audi', 'Volkswagen', 'Skoda', 'Cupra', 'Porsche'], None, cta_h, 'Owner guides', art)


# ---------- Audi ----------
page(PAGES['audi'][0],
     'Audi Mechanic Seaford &amp; Frankston | Audi Service | VAG Euro Automotive'.replace('&amp;', '&'),
     f'Independent Audi mechanic in Seaford, near Frankston. Audi logbook servicing, S tronic, timing chains, brakes and diagnostics without dealer prices. Call {PHONE}.',
     'Audi mechanic in Seaford', 'Audi service &amp; repairs',
     'Specialist Audi servicing and repairs from an independent workshop that works on Volkswagen Group cars every day. A few minutes from Frankston.',
     'audi-rs3-hoist', 'Audi RS 3 on a hoist at our Audi mechanic workshop in Seaford',
     f'''        <p class="lede">VAG Euro Automotive is an independent Audi mechanic in Seaford. Audi shares its engines, gearboxes and electronics with the rest of the Volkswagen Group, and that family of cars is what we work on every day.</p>
        <h2>Audi logbook servicing</h2>
        <p>We service your Audi to the manufacturer's logbook schedule, use oils and parts that meet Audi's specifications, and stamp your service book. Servicing with an independent mechanic doesn't void your new-car warranty, so you can keep your Audi under warranty and still deal directly with the people working on it. <a href="{GUIDES['warranty'][0]}">Read more about logbook servicing and warranty</a>.</p>
        <h2>Audi repairs we do</h2>
        <ul>
          <li><strong>S tronic and DSG gearboxes:</strong> gearbox oil services and clutch faults</li>
          <li><strong>Mechatronic unit repair:</strong> diagnosis and repair of S tronic and DSG mechatronic units, the gearbox's control unit</li>
          <li><strong>Timing belts and chains:</strong> TFSI timing chains and tensioners, TDI timing belt kits and water pumps</li>
          <li><strong>quattro and Haldex:</strong> Haldex coupling services, differential oil services and all-wheel-drive faults</li>
          <li><strong>TDI diesels and DPF:</strong> diesel particulate filter (DPF) repairs, EGR faults and timing belts</li>
          <li><strong>Brakes:</strong> pads, rotors, fluid and electronic park brakes</li>
          <li><strong>Diagnostics:</strong> warning lights, fault codes, battery replacement and coding</li>
          <li><strong>Suspension and steering:</strong> control arms, bushes, shocks and wheel bearings</li>
          <li><strong>Air conditioning:</strong> re-gas, leak tests and repairs</li>
        </ul>
        <h2>Audi models we service</h2>
        <p>A1, A3, S3, RS 3, A4, S4, A5, S5, A6, Q2, Q3, Q5, SQ5, Q7, Q8 and TT, from older models through to cars still under new-car warranty.</p>
        <h2>Why Seaford and Frankston Audi owners choose us</h2>
        <p>You talk directly to the mechanic working on your car, and we quote before any work starts. Loan cars are available on request. You can also wait in our lounge, or drop your keys in the key drop box early or after hours. Pay by card, Afterpay, Zip or humm.</p>''',
     ['Logbook servicing', 'S tronic', 'quattro &amp; Haldex', 'DPF', 'Timing chains', 'Diagnostics'],
     [('Can you service my Audi while it is under warranty?', "Yes. Using an independent mechanic doesn't void your Audi's new-car warranty as long as the servicing follows the manufacturer's specifications. We follow the logbook schedule and stamp your book."),
      ('Do you service Audi RS and S models?', 'Yes. We service and repair S and RS models such as the S3, RS 3, S4 and SQ5, as well as the standard range.'),
      ('Is your workshop close to Frankston?', 'Yes. We are at 11 Stephenson Road in Seaford, a short drive from Frankston, Carrum Downs and Chelsea.')],
     'Book your Audi in', 'Audi mechanic')

# ---------- Volkswagen ----------
page(PAGES['vw'][0],
     'Volkswagen Mechanic Seaford & Frankston | VW Service | VAG Euro Automotive',
     f'VW mechanic in Seaford, near Frankston. Volkswagen logbook servicing, DSG services and mechatronic repair, TSI timing chains, Amarok and Transporter repairs. Book online or call {PHONE}.',
     'Volkswagen mechanic in Seaford', 'VW service &amp; repairs',
     'Logbook servicing and repairs for every Volkswagen, from a Polo to an Amarok, by mechanics who specialise in VW. Close to Frankston.',
     'golf-gti-pair', 'Volkswagen Golf GTIs at our VW mechanic workshop in Seaford',
     f'''        <p class="lede">Volkswagen is where VAG Euro Automotive started, and VWs are the cars we see most. Whether it's a daily Golf, a family Tiguan or a work Amarok, we know the common faults and the right parts.</p>
        <h2>Volkswagen logbook servicing</h2>
        <p>We service your VW to the logbook schedule with oils and parts that meet Volkswagen's specifications, and stamp your service book. Your new-car warranty stays intact. <a href="{GUIDES['warranty'][0]}">Here's how that works</a>.</p>
        <h2>VW repairs we do</h2>
        <ul>
          <li><strong>DSG gearboxes:</strong> DSG oil and filter services and clutch faults. <a href="{GUIDES['dsg'][0]}">Read our DSG guide</a></li>
          <li><strong>DSG mechatronic unit repair:</strong> diagnosis and repair of the mechatronic unit that controls the gearbox</li>
          <li><strong>TSI timing chains:</strong> chain, tensioner and guide replacement. <a href="{GUIDES['chain'][0]}">What a chain rattle sounds like</a></li>
          <li><strong>TDI diesels and DPF:</strong> diesel particulate filter (DPF) repairs, EGR faults, timing belt kits and water pumps</li>
          <li><strong>4MOTION and Haldex:</strong> Haldex coupling services and all-wheel-drive faults on Tiguan, Golf R, Passat and Arteon</li>
          <li><strong>Brakes:</strong> pads, rotors, fluid and electronic park brakes</li>
          <li><strong>Diagnostics:</strong> warning lights, fault codes, battery replacement and coding</li>
          <li><strong>Cooling and leaks:</strong> water pumps, thermostat housings, coolant leaks and oil leaks</li>
          <li><strong>Suspension, steering and air conditioning</strong></li>
        </ul>
        <h2>VW models we service</h2>
        <p>Polo, Golf, Golf GTI, Golf R, Jetta, Passat, Arteon, T-Cross, T-Roc, Tiguan, Touareg, Amarok, Caddy, Transporter and Multivan.</p>
        <h2>A local VW mechanic for Seaford and Frankston</h2>
        <p>We are on Stephenson Road in Seaford, a few minutes from Frankston. You deal directly with your mechanic and get a quote before any work starts. Loan cars are available on request, and there's a key drop box for early drop-off.</p>''',
     ['Logbook servicing', 'DSG', 'TSI chains', 'DPF', 'Haldex', 'Amarok'],
     [('Do you service the Volkswagen Amarok and Transporter?', 'Yes. We service and repair Amarok, Transporter, Caddy and Multivan, as well as VW passenger cars.'),
      ('How often does my VW need a DSG service?', "It depends on the gearbox. Wet-clutch DSGs generally need an oil and filter change at set intervals, while the 7-speed dry-clutch DQ200 doesn't have a regular gearbox oil change. Check your logbook or ask us."),
      ('Will a VW service with you affect my warranty?', 'No. We service to the logbook schedule with parts and oils that meet the specifications, so your warranty stays intact.')],
     'Book your Volkswagen in', 'Volkswagen mechanic')

# ---------- European ----------
page(PAGES['euro'][0],
     'European Car Mechanic Seaford & Frankston | Skoda, Porsche, Mercedes, BMW',
     f'European car mechanic in Seaford, near Frankston. Servicing and repairs for Skoda, Cupra, Porsche, Mercedes-Benz, BMW and Mini. Call {PHONE}.',
     'European car mechanic in Seaford', 'European car servicing',
     'Skoda, Cupra, Porsche, Mercedes-Benz, BMW and Mini servicing and repairs from a Volkswagen Group specialist close to Frankston.',
     'porsche-718-cayman', 'Porsche 718 Cayman at our European car mechanic workshop in Seaford',
     f'''        <p class="lede">Our speciality is Audi and Volkswagen, and the same expertise carries across to other European cars. Skoda and Cupra share VW's engines and gearboxes, and Porsche shares much of its technology with Audi.</p>
        <h2>Skoda and Cupra</h2>
        <p>Octavia, Superb, Kodiaq, Karoq, Fabia and Kamiq, and the Cupra Formentor, Leon and Ateca. These cars use the same TSI and TDI engines and DSG gearboxes as Volkswagen, so they get the same specialist care. <a href="{PAGES['vw'][0]}">See our Volkswagen services</a>.</p>
        <h2>Porsche</h2>
        <p>Servicing and repairs for the Macan, Cayenne, Panamera and 718 Cayman and Boxster.</p>
        <h2>Mercedes-Benz, BMW and Mini</h2>
        <p>Logbook servicing, brakes, diagnostics, suspension and general repairs for Mercedes-Benz, BMW and Mini.</p>
        <h2>What we do for every European car</h2>
        <ul>
          <li>Logbook servicing that keeps your new-car warranty intact</li>
          <li>Warning light diagnostics and fault finding</li>
          <li>Brakes, suspension and steering</li>
          <li>Timing belts, chains and cooling system repairs</li>
          <li>Air conditioning service</li>
          <li>Pre-purchase inspections with a written report</li>
        </ul>''',
     ['Skoda', 'Cupra', 'Porsche', 'Mercedes-Benz', 'BMW', 'Mini'],
     [('Do you service Mercedes-Benz and BMW?', 'Yes. Audi and Volkswagen are our speciality, and we also service and repair Mercedes-Benz, BMW and Mini.'),
      ('Can you do a pre-purchase inspection on a European car?', "Yes. We inspect the car before you buy and give you a written report on what we find.")],
     'Book your European car in', 'European car mechanic')

# ---------- Frankston ----------
page(PAGES['frankston'][0],
     'Mechanic near Frankston | Audi & VW Car Mechanic | VAG Euro Automotive',
     f'Looking for a mechanic near Frankston? VAG Euro Automotive in Seaford services Audi, Volkswagen and European cars, a short drive from Frankston. Call {PHONE}.',
     'Car mechanic near Frankston', 'Frankston &amp; surrounds',
     'Our Seaford workshop is a short drive from Frankston. Bring us your Audi, Volkswagen or European car for servicing and repairs.',
     'three-hoists', 'Cars on hoists at the VAG Euro Automotive workshop near Frankston',
     f'''        <p class="lede">If you live or work in Frankston, VAG Euro Automotive is close by at 11 Stephenson Road, Seaford. We're an independent car mechanic that specialises in Audi and Volkswagen and services other European cars too.</p>
        <h2>Why Frankston drivers come to Seaford</h2>
        <p>A specialist knows the common faults on your car and has the right parts, so jobs are done properly the first time. You talk to the mechanic doing the work and get a quote before anything starts.</p>
        <h2>Services for Frankston customers</h2>
        <ul>
          <li><a href="{PAGES['audi'][0]}">Audi servicing and repairs</a></li>
          <li><a href="{PAGES['vw'][0]}">Volkswagen servicing and repairs</a></li>
          <li><a href="{PAGES['euro'][0]}">Skoda, Cupra, Porsche, Mercedes-Benz and BMW</a></li>
          <li>Logbook servicing without affecting your new-car warranty</li>
          <li>DSG and S tronic servicing, timing chains, brakes and diagnostics</li>
        </ul>
        <h2>Easy drop-off</h2>
        <p>Loan cars are available on request, subject to availability. You can also wait in our lounge for shorter jobs, or leave your keys in the key drop box before work. We're open Monday to Friday 8:00 to 5:00 and Saturday 8:30 to 2:00.</p>
        <h2>Suburbs we service</h2>
        <p>{', '.join(AREAS)}.</p>''',
     ['Frankston', 'Frankston North', 'Seaford', 'Carrum Downs', 'Langwarrin', 'Kananook'],
     [('How far is your workshop from Frankston?', 'We are at 11 Stephenson Road, Seaford, a short drive from Frankston.'),
      ('Do you only work on European cars?', 'Audi and Volkswagen are our speciality, and we also service Skoda, Cupra, Porsche, Mercedes-Benz, BMW and Mini.')],
     'Book your car in from Frankston', 'Mechanic near Frankston')

# ---------- Guides ----------
article(GUIDES['warranty'][0],
        'Logbook Servicing & New-Car Warranty | Audi & VW Mechanic Seaford',
        "Can an independent mechanic service your new Audi or Volkswagen without voiding the warranty? What Australian owners need to know, from our Seaford workshop.",
        GUIDES['warranty'][1], 'Owner guide · Servicing',
        "Why an independent specialist can service your new Audi or VW without affecting the warranty, and what to check in your logbook.",
        'golf-gti-pair', 'Volkswagen Golf GTIs waiting for logbook servicing',
        f'''        <p class="lede">Many new-car owners believe they have to go back to the dealer for every service to keep their warranty. In Australia, that isn't the case.</p>
        <h2>You can choose your mechanic</h2>
        <p>The ACCC has made it clear that a manufacturer can't refuse a warranty claim just because your car was serviced by an independent mechanic. What matters is that the servicing is done properly, following the manufacturer's specifications and logbook schedule, using parts and oils that are fit for purpose.</p>
        <h2>What a proper logbook service includes</h2>
        <ul>
          <li>The checks and replacements listed for that interval in your car's service schedule</li>
          <li>Engine oil that meets the manufacturer's approval for your engine, such as VW 504 00 or 508 00 on many recent VW Group cars</li>
          <li>Filters and parts that meet the original specification</li>
          <li>A stamped and dated entry in your logbook or digital service record</li>
          <li>Records of the work and parts used, which you should keep</li>
        </ul>
        <h2>What to check after every service</h2>
        <p>Make sure the logbook is stamped with the date, odometer reading and workshop details, and keep your invoice. If you ever need to make a warranty claim, these records show the car was serviced on time and to specification.</p>
        <h2>Fixed or flexible service intervals</h2>
        <p>Many Audi and Volkswagen models in Australia use a fixed interval, commonly every 12 months or 15,000 km, whichever comes first. Some have different schedules. Your logbook or service display tells you what applies to your car, and we can check it for you.</p>
        <h2>Book your logbook service in Seaford</h2>
        <p>We service Audi, Volkswagen, Skoda and Cupra to the logbook schedule at our workshop in Seaford, close to Frankston. <a href="{BOOK}">Book online</a> or call <a href="{TEL}">{PHONE}</a>.</p>
        <p style="font-size:0.85rem;color:var(--muted)">This guide is general information, not legal advice. For details, see the ACCC's guidance on new-car warranties.</p>''',
        'Book a logbook service')

article(GUIDES['dsg'][0],
        'DSG Service Guide: When Your VW or Audi Needs One | Seaford Mechanic',
        "What a DSG service is, the difference between wet and dry clutch DSG gearboxes, and the signs your VW or Audi gearbox needs attention.",
        GUIDES['dsg'][1], 'Owner guide · Transmission',
        "Wet-clutch and dry-clutch gearboxes have different needs. Here's how to tell which one you have.",
        'audi-s3-bay', 'Audi in the service bay ready for a DSG gearbox service',
        f'''        <p class="lede">DSG (called S tronic by Audi) is Volkswagen Group's dual-clutch automatic gearbox. It shifts quickly and is efficient, but it needs the right maintenance.</p>
        <h2>Wet clutch or dry clutch?</h2>
        <p>DSG gearboxes come in two broad types:</p>
        <ul>
          <li><strong>Wet-clutch DSG</strong> (for example the 6-speed DQ250 and 7-speed DQ381 and DQ500) runs its clutches in oil. This oil and its filter need changing at set intervals, often around every 60,000 km. Your logbook gives the exact interval.</li>
          <li><strong>Dry-clutch DSG</strong> (the 7-speed DQ200, common in smaller engines such as the 1.4 TSI) has dry clutches. Its gearbox oil is usually not part of the regular service schedule.</li>
        </ul>
        <p>Not sure which you have? Give us your rego or model and engine, and we'll tell you.</p>
        <h2>What a DSG service involves</h2>
        <p>On wet-clutch gearboxes we drain the old oil, replace the filter, refill with oil that meets VW's specification at the correct temperature, and check for fault codes. Some gearboxes also need their clutch settings re-learned with a diagnostic tool afterwards.</p>
        <h2>Signs your DSG needs attention</h2>
        <ul>
          <li>Jerky or shuddering take-off from a standstill</li>
          <li>Hesitation or clunking when changing gear</li>
          <li>A flashing gear indicator or a gearbox warning on the dash</li>
          <li>The car going into limp mode</li>
        </ul>
        <p>Catching these early is usually far cheaper than repairing a failed clutch pack or mechatronic unit.</p>
        <h2>Mechatronic unit repair</h2>
        <p>The mechatronic unit is the gearbox's built-in control unit, combining its electronics and hydraulics. Faults often show up as a flashing gear indicator, harsh or missed shifts, or limp mode. We diagnose the fault, then repair the mechatronic unit rather than defaulting to a full gearbox replacement.</p>
        <h2>DSG servicing in Seaford</h2>
        <p>We service and repair DSG and S tronic gearboxes on Volkswagen, Audi, Skoda and Cupra at our workshop in Seaford, near Frankston. <a href="{BOOK}">Book online</a> or call <a href="{TEL}">{PHONE}</a>.</p>''',
        'Book a DSG service')

article(GUIDES['chain'][0],
        'TSI Timing Chain Noise: What to Listen For | VW & Audi Mechanic Seaford',
        "A rattle on cold start can be a sign of timing chain wear on VW and Audi TSI and TFSI engines. What to listen for and when to book a check in Seaford.",
        GUIDES['chain'][1], 'Owner guide · Engine',
        "A rattle on cold start can be an early warning sign. Here's when to book a check.",
        '718-bonnet-up', 'Car on a hoist with the bonnet up for an engine inspection',
        f'''        <p class="lede">Many Volkswagen Group petrol engines use a timing chain instead of a belt. Chains are designed to last, but on some TSI and TFSI engines the chain, tensioner or guides can wear early.</p>
        <h2>Which engines are affected?</h2>
        <p>Timing chain problems are best known on some earlier engines, including certain 1.2 and 1.4 TSI engines and the first generations of the 1.8 and 2.0 TSI/TFSI (EA888) used from about 2008. Later versions brought improved parts, but any high-mileage chain engine can wear.</p>
        <h2>What to listen for</h2>
        <ul>
          <li>A rattle or grinding noise for a few seconds after a cold start</li>
          <li>Rattling at idle that gets worse as the engine warms</li>
          <li>An engine warning light with camshaft or crankshaft timing fault codes</li>
          <li>Rough running or difficulty starting</li>
        </ul>
        <h2>Why it matters</h2>
        <p>A stretched chain or failed tensioner can let the chain skip a tooth. On these engines that can cause serious damage to valves and pistons. Checking a noise early costs far less than an engine repair.</p>
        <h2>How we check it</h2>
        <p>We listen to the engine from cold, read the fault codes and check the live camshaft timing data with a diagnostic tool. On some engines we also inspect the tensioner. If the chain needs replacing, we quote for a kit with the updated parts.</p>
        <h2>Timing chain checks in Seaford</h2>
        <p>Hear a rattle on cold start? <a href="{BOOK}">Book a check</a> at our Seaford workshop near Frankston, or call <a href="{TEL}">{PHONE}</a>.</p>''',
        'Book a timing chain check')
print('pages ok')

# ---------- 404 ----------
html = head('Page not found | VAG Euro Automotive', 'This page could not be found.', '404.html', {'@graph': [BUSINESS]}).replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
html += header(False) + f'''
<main id="top">
  <section class="cta-band on-light" style="min-height:60vh;display:grid;align-items:center">
    <div class="wrap">
      <p class="eyebrow">404</p>
      <h1 style="font-size:clamp(1.6rem,3vw,2.4rem)">That page has moved</h1>
      <p>The page you're after isn't here. Head back to the homepage, or book your Audi or Volkswagen in with our Seaford mechanics.</p>
      <div class="actions"><a class="btn btn-solid" href="index.html">Go to homepage</a><a class="btn" href="{BOOK}">Book a service</a></div>
    </div>
  </section>
</main>

''' + footer(False) + '\n' + FOOT_JS
open(OUT + '/404.html', 'w').write(html)
