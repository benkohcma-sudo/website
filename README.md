# Coach Masters Academy — website redesign (front-end handoff)

Static HTML/CSS/JS rebuild of **www.coachmastersacademy.com** with a new look,
animations and the same pages, links and copy. Built to be dropped into the
existing back-end by a developer.

## What the live site actually runs on

* The main site is a **Laravel** application (AdminLTE admin at `/admin`,
  Blade templates, theme assets under `/public/twenty25/`). It is **not** WordPress.
* The blog at `/blog/` **is WordPress** (`wp-content/uploads`, WP permalinks).

So the developer converts the pages here into Blade views (main site) and a
WordPress theme (blog). The HTML is framework-free on purpose.

## What is in this repo

```
dist/                     THE DELIVERABLE. 553 pages, one folder per URL (about-us/index.html …)
dist/assets/css/main.css  design system (colours, type, components, animation primitives)
dist/assets/js/main.js    animations: GSAP + ScrollTrigger (reveals, split headlines,
                          counters, parallax, globe, curved journey line, faculty carousel)
dist/assets/js/globe-data.js  land-dot data for the globe (Natural Earth, public domain)

src/content/pages.json    every page's copy, crawled verbatim from the live site
src/extract.py            crawl -> pages.json
src/build.py              pages.json -> dist/ (layout, header, footer, generic page)
src/pages_custom.py       hand-designed pages: home, about-us (globe), our-story (journey),
                          our-faculty (carousel), coaching certification (pathway), listings
src/verify.py             proves every sentence of the original copy is still on each page
assets/                   source of dist/assets
```

## Rules the build follows

* **Copy is verbatim.** Nothing was rewritten, added or removed. Run
  `python3 src/verify.py` after any change; it must report `0 with missing copy`
  (the one accepted exception is `/our-faculty`, where "Name I Credential" is
  laid out on two lines).
* **Images and files** point at the live site (`https://www.coachmastersacademy.com/...`)
  so nothing needs re-uploading. Swap the prefix when moving assets.
* **Colours**: `#eb6422` orange, `#17380E` deep green, `#E55C00` dark orange (see `:root` in main.css).
* **Fonts**: Instrument Sans (headings) + Inter (body) from Google Fonts.
* `<!-- CMS: ... -->` comments mark things the back-end must supply
  (country lists, form actions, CSRF tokens, pagination, newsletter).

## Key pages

| URL | What is special |
|---|---|
| `/` | floating hero gallery, service tiles, feature rows, partner + testimonial marquees, brochure form |
| `/about-us` | **globe hero** – canvas dot-globe with regional office pins; spins one full turn as you scroll the hero, plus a slow idle spin; counters; faculty carousel |
| `/pages/our-story` | **curved orange journey line** – SVG S-curve drawn on scroll with a travelling dot; milestone cards alternate sides |
| `/our-faculty` | carousel like the reference design: tabs per group, featured large card + small cards, prev/next, counter, dotted world map behind |
| `/icf-coaching-training-program` | stats counters, the four "Advantages" on a curved journey line, track feature rows |
| listings (`/blog/…`, `/events/news`, `/events/gallery`, `/workshops`) | card grids / masonry gallery, original pagination kept |
| everything else | generic template: hero + prose + sticky contact aside + section links |

## Integration notes for the developer

1. Shared chrome (`header`, `footer`, sub-navigation) is identical on every page —
   lift it once into the layout Blade file. Nav links and footer text are the live ones.
2. Page body = everything inside `<main>`. Generic pages use `.prose` for CMS
   HTML; keep that wrapper so headings, lists, accordions (`<details>`), tables
   and forms pick up the styling.
3. Accordions/tabs from the old Bootstrap markup were converted to native
   `<details>`; no Bootstrap JS needed. Do not load the old theme CSS
   (Bootstrap 3, Revolution, style.css) on the new pages.
4. Pagination links were rewritten to `/page-N/` folders for the static preview;
   Laravel keeps its `?page=N` — one regex in `build.py` (`rewrite_pagination`).
5. Animations: only dependency is GSAP 3.12 (cdnjs). Append `?nomotion` to any
   URL to see a page without animation (also what `prefers-reduced-motion` gets).
6. Add `data-reveal` to any new block to get the scroll reveal; `data-split` on a
   heading for the word-by-word rise; `data-count="1234"` on a number to count up.
7. Faculty and Story sections are generated from the CMS lists (see
   `parse_faculty`, `story` in `pages_custom.py`) — the loop maps 1:1 to a Blade `@foreach`.

## Preview / rebuild

```
npx -y serve dist            # preview at http://localhost:3000
python3 src/build.py         # regenerate dist/ from pages.json + templates
python3 src/verify.py        # copy-preservation check
```

Re-crawling (only if the live copy changes): `pip3 install --user beautifulsoup4 lxml`,
fetch each URL in `src/sitemap_urls.txt` into a folder, then `python3 src/extract.py <folder>`.
