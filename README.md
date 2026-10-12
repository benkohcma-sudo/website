# Coach Masters Academy — website redesign (front-end handoff)

A redesigned front end for **www.coachmastersacademy.com**: same pages, same links,
same wording — new layout, styling and motion. Built to be dropped into the
existing Laravel back end.

**Live preview:** https://website-one-dun-67.vercel.app

---

## Read this first

**This is plain HTML, CSS and JavaScript. There is no React.**

| | |
|---|---|
| **Is it React / Vue / Next?** | No. There is not a single `.jsx`/`.tsx` file, no `package.json`, no `node_modules`. |
| **Is there a build step?** | No. No npm install, no bundler, no compile. The files in `dist/` are the finished website. |
| **What JavaScript is there?** | One file — `assets/js/main.js`, written in plain browser JavaScript (no imports, no framework). Plus `globe-data.js`, which is only map coordinates. |
| **Any third-party library?** | One: **GSAP 3.12** for the scroll animations, loaded from a CDN with a `<script>` tag. Nothing to install. |
| **How do I view it?** | Open any `dist/.../index.html` in a browser, or use the live preview link above. |
| **Does this suit Blade?** | Yes — directly. Static HTML is the easiest possible input for Blade templates. See below. |

If someone told you this was React, they were looking at something else.

---

## Converting to Laravel Blade

The full step-by-step is in **[`src/HANDOFF.md`](src/HANDOFF.md)** — read that next.
The short version:

1. **Assets** — copy `assets/` into `public/` (e.g. `public/twenty26/`). Every path in
   the HTML is absolute (`/assets/css/main.css`), so update the prefix once if you
   move it.
2. **Layout** — the `<head>`, top bar, header and footer are **byte-identical on all
   620 pages**. Lift them once from any `index.html` into `layouts/app.blade.php`.
   Only `<title>` and the meta description change per page, so make those
   `@section` variables.
3. **Views** — everything inside `<main>` becomes one view's `@section('content')`.
   Pages fall into three groups (hand-designed, landing, generic) — `HANDOFF.md`
   lists exactly which is which.
4. **CMS regions** — `<!-- CMS: ... -->` comments mark every spot where the admin
   should keep editing content. Swap the static text there for your Blade variables.
5. **Dynamic lists** — faculty, calendar rows, news, gallery, webinars and blog
   cards are static examples of your existing collections. Each one maps 1:1 to a
   `@foreach` over the markup already there.
6. **Forms** — field names, values and options are unchanged from the live site, so
   they post to your existing controllers. Put back `action` and `@csrf`.

The one page needing real backend work is **`/events/calendar`** (Schedule): the rows,
country list and timezone list come from the server, and the `/get-timezones` route
stays. The in-page filter script works on whatever rows you render, so it can stay
as it is. Details in `HANDOFF.md`.

The blog at `/blog/` is **WordPress**, not Laravel — build a small theme from the
same chrome (`header.php` / `footer.php`). Also covered in `HANDOFF.md`.

---

## What is in this repo

```
dist/                        THE DELIVERABLE — 620 pages, one folder per URL
  about-us/index.html          (so /about-us is dist/about-us/index.html)
  assets/css/main.css          the whole design system, one file
  assets/js/main.js            all behaviour and animation, plain JS
  assets/js/globe-data.js      land-dot coordinates for the globe
  assets/img/ assets/video/    images and film

assets/                      source of dist/assets (edit here, then rebuild)
src/HANDOFF.md               >> the developer guide: read this <<
src/content/pages.json       every page's copy, crawled verbatim from the live site
src/build.py                 pages.json -> dist/
src/pages_custom.py          the hand-designed page templates
src/verify.py                proves no original wording was lost
vercel.json                  tells the preview host the site lives in dist/
```

You only need `dist/` to build the templates. The `src/` folder is how the pages
were generated, kept so the design can be regenerated later.

## House rules the build follows

* **Copy is verbatim.** Nothing was reworded, added or removed — the client asked
  for the original wording to stay. `python3 src/verify.py` checks this and must
  report `0 with missing copy`.
* **No gradients anywhere** (client's rule). Flat `#eb6422` orange, flat tints.
* **Colours**: `#eb6422` orange, `#17380E` deep green, `#E55C00` dark orange —
  all defined in `:root` in `main.css`.
* **Fonts**: Instrument Sans (headings) + Inter (body), from Google Fonts.
* Old Bootstrap accordions/tabs became native `<details>` — do **not** load the old
  theme CSS (Bootstrap 3, Revolution, style.css) on these pages.

## Previewing locally

```bash
npx -y serve dist          # then open http://localhost:3000
```

Add `?nomotion` to any URL to see a page with all animation switched off — the same
thing users with "reduce motion" enabled get automatically.
