import json

SITE = 'https://vageuroautomotive.com.au'   # assumed domain, change in one place
NAME = 'VAG Euro Automotive'
PHONE, PHONE_INTL, TEL = '(03) 8795 7699', '+61 3 8795 7699', 'tel:+61387957699'
EMAIL = 'Hiproservicecentre@gmail.com'
AREAS = ['Seaford', 'Frankston', 'Carrum Downs', 'Kananook', 'Frankston North', 'Chelsea', 'Carrum', 'Patterson Lakes', 'Langwarrin', 'Skye', 'Aspendale', 'Mornington Peninsula']

PAGES = {
    'audi': ('audi-mechanic-seaford.html', 'Audi'),
    'vw': ('volkswagen-mechanic-seaford.html', 'Volkswagen'),
    'euro': ('european-car-mechanic-seaford.html', 'European cars'),
    'frankston': ('mechanic-frankston.html', 'Frankston'),
}
GUIDES = {
    'warranty': ('logbook-servicing-new-car-warranty.html', 'Logbook servicing and your new-car warranty'),
    'dsg': ('dsg-service-guide.html', 'DSG service: what it is and when your VW needs one'),
    'chain': ('tsi-timing-chain-noise.html', 'Timing chain noise on TSI engines: what to listen for'),
}

BUSINESS = {
    '@type': 'AutoRepair',
    '@id': SITE + '/#business',
    'name': NAME,
    'alternateName': 'Hi Pro Service Centre',
    'description': 'Audi, Volkswagen and European car mechanic in Seaford, near Frankston, Victoria. Logbook servicing, DSG and S tronic, timing belts and chains, brakes, diagnostics and repairs.',
    'url': SITE + '/',
    'logo': SITE + '/brand/logo-colour-on-light.png',
    'image': [SITE + '/images/three-hoists.jpg', SITE + '/images/porsche-718-cayman.jpg', SITE + '/images/golf-gti-pair.jpg'],
    'telephone': PHONE_INTL,
    'email': EMAIL,
    'taxID': '81 677 521 854',
    'priceRange': '$$',
    'address': {'@type': 'PostalAddress', 'streetAddress': '11 Stephenson Road', 'addressLocality': 'Seaford', 'addressRegion': 'VIC', 'postalCode': '3198', 'addressCountry': 'AU'},
    'hasMap': 'https://www.google.com/maps/search/?api=1&query=11+Stephenson+Road+Seaford+VIC+3198',
    'openingHoursSpecification': [
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '08:00', 'closes': '17:00'},
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Saturday', 'opens': '08:30', 'closes': '14:00'},
    ],
    'areaServed': [{'@type': 'City', 'name': a + ', VIC'} if a != 'Mornington Peninsula' else {'@type': 'AdministrativeArea', 'name': a} for a in AREAS],
    'brand': [{'@type': 'Brand', 'name': b} for b in ['Audi', 'Volkswagen', 'Skoda', 'Cupra', 'Porsche', 'Mercedes-Benz', 'BMW', 'Mini']],
    'paymentAccepted': 'Cash, EFTPOS, Visa, Mastercard, Afterpay, Zip, humm',
    'currenciesAccepted': 'AUD',
    'amenityFeature': [{'@type': 'LocationFeatureSpecification', 'name': n, 'value': True} for n in ['Loan cars', 'Customer waiting lounge', 'Key drop box', 'Service warranty']],
    'sameAs': ['https://www.autoguru.com.au/s/vag-euro-automotive-hi-pro-service-vw-audi'],
    'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Car servicing and repairs', 'itemListElement': [
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s}} for s in [
            'Logbook servicing', 'Audi servicing', 'Volkswagen servicing', 'DSG and S tronic servicing', 'Timing belt and timing chain replacement',
            'Brake repairs', 'Diagnostics and warning lights', 'Suspension and steering', 'Air conditioning service', 'Pre-purchase car inspections', 'quattro and Haldex servicing', 'DPF repairs', 'DSG and S tronic mechatronic unit repair']]},
}


def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps({'@context': 'https://schema.org', **obj} if '@graph' not in obj else {'@context': 'https://schema.org', **obj}, indent=1, ensure_ascii=False) + '\n</script>'


def breadcrumb(items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)]}


def faq_schema(qas):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qas]}


def faq_html(qas, heading='Questions we get asked', eyebrow='FAQ'):
    items = ''.join(f'<details class="qa"><summary>{q}</summary><p>{a}</p></details>' for q, a in qas)
    return f'''  <section class="faq" id="faq">
    <div class="wrap">
      <div style="display:grid;gap:14px;align-content:start"><p class="eyebrow">{eyebrow}</p><h2>{heading}</h2></div>
      <div class="qa-list">{items}</div>
    </div>
  </section>
'''


def head(title, desc, path, schema, og_image='images/og-image.jpg', extra=''):
    url = SITE + '/' + ('' if path == 'index.html' else path)
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0A0A0A">
<meta name="geo.region" content="AU-VIC">
<meta name="geo.placename" content="Seaford">
<link rel="icon" href="brand/favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_AU">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&display=swap">
<link rel="stylesheet" href="css/site.css">
{extra}{ld(schema)}
</head>
'''


def header(home):
    h = '' if home else 'index.html'
    return f'''<body>

<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{h or '#top'}" aria-label="{NAME} home"><img src="brand/logo-colour-on-dark.svg" alt="{NAME}, Audi and Volkswagen mechanic Seaford" width="200" height="46"></a>
    <nav class="nav" aria-label="Main">
      <a href="{h or '#top'}">Home</a>
      <a href="{h}#story">Our story</a>
      <div class="dd">
        <span tabindex="0">Service</span>
        <div class="dd-menu">
          <a href="{PAGES['audi'][0]}">Audi</a><a href="{PAGES['vw'][0]}">Volkswagen</a><a href="{PAGES['euro'][0]}">Skoda &amp; Cupra</a><a href="{PAGES['euro'][0]}">Porsche</a><a href="{PAGES['euro'][0]}">Mercedes-Benz</a><a href="{PAGES['euro'][0]}">BMW &amp; Mini</a><a href="{h}#services">All services</a>
        </div>
      </div>
      <a href="{h}#guides">Guides</a>
      <a href="{h}#visit">Contact</a>
    </nav>
    <div class="head-right">
      <a class="phone" href="{TEL}" aria-label="Call {PHONE}"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M3.5 1.5h2.5l1.2 3-1.6 1.1a8 8 0 0 0 4.8 4.8l1.1-1.6 3 1.2v2.5A1.5 1.5 0 0 1 13 14 11.5 11.5 0 0 1 2 3a1.5 1.5 0 0 1 1.5-1.5z"/></svg></a>
      <a class="btn btn-solid" href="{h}#book">Book now</a>
    </div>
  </div>
</header>
'''


def footer(home):
    h = '' if home else 'index.html'
    svc = ''.join(f'<li><a href="{u}">{n} mechanic</a></li>' for u, n in [PAGES['audi'], PAGES['vw'], (PAGES['euro'][0], 'European car')]) + f'<li><a href="{PAGES["frankston"][0]}">Mechanic near Frankston</a></li><li><a href="{h}#book">Book a service</a></li>'
    gd = ''.join(f'<li><a href="{u}">{t}</a></li>' for u, t in GUIDES.values())
    return f'''<footer>
  <div class="wrap">
    <div style="display:grid;gap:18px;align-content:start">
      <img src="brand/logo-colour-on-dark.svg" alt="{NAME}" width="218" height="50" loading="lazy">
      <address>Audi, Volkswagen and European car mechanic<br>11 Stephenson Road, Seaford VIC 3198<br>Mon–Fri 8:00–5:00 · Sat 8:30–2:00<br><a href="{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></address>
    </div>
    <div><h3>Services</h3><ul>{svc}</ul></div>
    <div><h3>Owner guides</h3><ul class="plain">{gd}</ul></div>
    <div>
      <h3>Service reminders</h3>
      <p>Sign up to receive service reminders and offers.</p>
      <form class="signup" id="signup" novalidate>
        <label for="s-email" style="position:absolute;left:-9999px">Email</label>
        <input id="s-email" type="email" placeholder="Email address" autocomplete="email">
        <button class="btn" type="submit">Sign up</button>
      </form>
      <p class="form-note" id="s-note" aria-live="polite" style="color:var(--muted);margin-top:10px"></p>
    </div>
    <p class="legal">&copy; <span id="yr">2026</span> {NAME}. ABN 81 677 521 854. Mechanic in Seaford serving Frankston, Carrum Downs, Chelsea and the Mornington Peninsula. Audi, Volkswagen and other marque names are trademarks of their owners. We are an independent workshop, not affiliated with any manufacturer.</p>
  </div>
</footer>
'''


FOOT_JS = '''<script>
(function () {
  var d = new Date();
  document.getElementById('yr').textContent = d.getFullYear();
  document.getElementById('signup').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('s-note').textContent = 'Sign-ups will work once the site is live. Nothing was saved.';
  });
})();
</script>
</body>
</html>
'''
