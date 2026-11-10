# VAG Euro Automotive website

Static website for VAG Euro Automotive, Audi, Volkswagen and European car mechanic at 11 Stephenson Road, Seaford VIC 3198.

- `site/` is the live website. Netlify publishes this folder (see `netlify.toml`). There is no build step.
- `src/` holds the scripts that generated the pages: `src/seo/parts.py` (shared header, footer, business details, schema), `build_index.py` (homepage, from `src/homepage-template.html`), `build_pages.py` (service pages and guides) and `build_assets.py` (sitemap, robots, image sizes). Small text changes can be made directly in `site/`.

Booking requests are sent through Netlify Forms (form name `booking`). Turn on form detection in Netlify and add a notification email.
