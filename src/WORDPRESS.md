# Putting this site into WordPress

This guide is for building the **whole site** as a WordPress theme.

> If only `/blog/` is moving to WordPress and the main site stays Laravel, use
> `HANDOFF.md` instead — that one assumes Laravel for everything else.

The deliverable is plain HTML, CSS and JavaScript: no React, no build step, no npm.
Every page in `dist/` is a finished page. The job is to turn repeated page shapes
into theme templates and hand the changing parts to the WordPress editor.

---

## 1. What you are converting

620 pages. They group like this:

| Group | Count | What it becomes in WordPress |
|---|---|---|
| `blog/…` | 269 | **Posts** (the existing blog) + year archives 2016–2026 |
| `webinar/…` | 174 | **Custom post type** `webinar` |
| `events/…`, `event/…` | 117 | **Custom post type** `event` (news, gallery, calendar) |
| `pages/…` + top-level articles | ~60 | **Pages** |
| Everything else | — | **Pages** |

Twelve pages are hand-designed and each needs its own page template:

```
/                                             home
/about-us                                     globe hero
/pages/our-story                              curved journey line
/our-faculty                                  carousel
/icf-master-certified-coach-mcc               founder
/icf-coaching-training-program                certification pathway
/pages/why-cma                                chapters + labs on a curve
/pages/coaching-education                     interactive globe of offices
/pages/mentor-coaching                        packages + lightbox
/pages/our-unique-approach                    layered sections
/pages/business-development                   photo hero
/executive-leadership-coaching-service-…      flip cards
/faq                                          open accordion list
/events/calendar                              schedule, two views + filters
```

Everything else fits one of two generic templates: a **landing** template (sections
of logo lanes, stat rings, icon cards) and a **content** template (title, breadcrumb,
sub-nav, prose column).

---

## 2. Theme skeleton

```
wp-content/themes/cma/
  style.css            theme header comment only
  functions.php        enqueues, menus, CPTs, form handlers
  header.php           everything above <main>  (identical on all 620 pages)
  footer.php           everything below </main> (identical on all 620 pages)
  index.php            fallback
  front-page.php       the home page
  page.php             generic content page
  page-templates/      one file per hand-designed page (above)
  single.php           blog post
  archive.php          blog listing (card grid)
  single-webinar.php   archive-webinar.php
  single-event.php     archive-event.php
  search.php           the search form already posts to `?s=` — WordPress native
  assets/              copy the delivered assets/ folder here
```

**The header and footer are byte-identical on every page** (header ~1.2 KB, footer
~4.3 KB), so lift them once from any `dist/*/index.html`. Only `<title>` and the
meta description change per page — use `wp_head()` and a SEO plugin for those.

---

## 3. Assets

Copy the delivered `assets/` folder into the theme, then enqueue it. Do **not**
hardcode the paths — the HTML uses absolute `/assets/…` paths that must become
`get_template_directory_uri()`:

```php
function cma_assets() {
    wp_enqueue_style( 'cma', get_template_directory_uri() . '/assets/css/main.css', [], '1.0' );
    wp_enqueue_script( 'gsap', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js', [], '3.12.5', true );
    wp_enqueue_script( 'gsap-st', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js', ['gsap'], '3.12.5', true );
    wp_enqueue_script( 'cma', get_template_directory_uri() . '/assets/js/main.js', ['gsap-st'], '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'cma_assets' );
```

`assets/js/globe-data.js` is only needed on `/pages/coaching-education` — enqueue it
on that template alone.

Keep the load order: GSAP, then ScrollTrigger, then `main.js`. `main.js` degrades
gracefully if GSAP is missing, but animations will not run.

Also remove the old theme's CSS (Bootstrap 3, Revolution, `style.css`) from these
pages — the accordions and tabs are native `<details>` now and need no Bootstrap JS.

---

## 4. Images still pointing at the live site

Many images still load from the current site rather than from this build:

| Prefix | Links |
|---|---|
| `/siteimages/…` | 925 |
| `/cmaassets/…` | 529 |
| `/ckFiles/…` | 227 |
| `/public/…` | 150 |

They are written as full URLs (`https://www.coachmastersacademy.com/siteimages/…`),
so **they keep working on day one** without touching them. Two options:

* **Leave them** — fine while the old site stays up, but you are hotlinking.
* **Migrate** — pull those four folders into the Media Library and rewrite the
  prefix. One find-and-replace per prefix across the templates.

Decide before launch: if the old site is switched off, hotlinked images die with it.

---

## 5. Forms

Every page carries the newsletter form, and `<!-- CMS: … -->` comments mark each
spot the editor must keep control of:

| Marker | Where |
|---|---|
| `newsletter form posts to backend; country select supplied by backend` | all 620 pages (footer) |
| `full option list supplied by backend` | 84 places (country/timezone lists) |
| `brochure form posts to backend (download_programpack)` | home brochure form |

**Important:** the markup still contains Laravel's `<input name="_token">` in 145
places. WordPress does not use that — **delete it** and add `wp_nonce_field()`
instead.

Field names are unchanged from the live site, so whatever receives them must accept:

* newsletter — `email`
* brochure download — `down_username`, `down_number`, `down_email`, `country`
* interest forms — `name`, `email`, `country`, `inspire_positive_change`,
  `how_to_know_cma[]`, `how_serve_best[]`, `coahing_education_intrest`
  (note: `coahing_` is the live site's own spelling — keep it or change it in both places)

Handle them with `admin_post_*` / `admin_post_nopriv_*` actions, or drop in a form
plugin (WPForms, CF7) and map the field names across. The certification interest form
is shown as a 4-step wizard by `main.js` (`form.js-steps`, `data-steps="2,2,5,3"`) but
still submits as one form — keep the classes and it keeps working.

The search form uses `name="s"`, which is WordPress's own search parameter — it works
as-is once pointed at the site root.

---

## 6. The Schedule page is the real work

`/events/calendar` is the one page that needs a backend, not just a template. On the
current site the rows, the country list and the timezone list come from the server.

* Store sessions as a CPT (`session`) or a custom table: event type, event name,
  date, month, time, detail link.
* Render them into the same `<table>` markup — the in-page filter script works on
  whatever rows you output, so it needs no changes.
* The timezone dropdown called a Laravel route (`/get-timezones`) when a country was
  picked. Rebuild it as `admin-ajax.php` or a REST route returning the same shape.
* The page has two views behind a sliding toggle (Training Schedule / Complimentary
  Enrichment Learning). The toggle keeps the live `?type=` URLs so old deep links
  still land correctly — preserve that query string.
* The enrichment rows in this build were copied from the live site into
  `src/content/calendar_enrichment.json`; treat them as sample data.

---

## 7. Dynamic lists

These are rendered as static examples of content you already have. Each maps to a
`WP_Query` loop over the markup that is already there:

faculty cards · calendar rows · news · gallery · webinars · blog cards · program tabs

Keep the surrounding classes exactly — the animations and layouts key off them.

---

## 8. Things that must not change

* **Copy is verbatim.** Nothing was reworded, added or removed — the client asked for
  the original wording to stay. Keep it when moving text into the editor.
* **No gradients anywhere** (client's rule). Flat `#eb6422` orange, flat tints only.
* **Colours:** `#eb6422` orange, `#17380E` deep green, `#E55C00` dark orange — all in
  `:root` in `main.css`.
* **Fonts:** Instrument Sans (headings) + Inter (body), from Google Fonts.
* Links, nav and footer text are the live site's own — leave them pointing where they
  point.

---

## 9. Animation hooks (for new content added in WordPress)

The editor can use these on any new block and the motion comes for free:

| Attribute | Effect |
|---|---|
| `data-reveal` | the block rises in when scrolled to |
| `data-split` | heading arrives word by word |
| `data-count="1234"` | number counts up |
| `data-video` | link opens in a video popup |
| `data-lightbox` | image opens in a viewer |

Add `?nomotion` to any URL to see a page with all motion switched off — the same thing
users with "reduce motion" enabled get automatically.

The preloader (green screen, logo, orange staircase) runs on the first page of a visit
only, keyed on `sessionStorage` `cmaPre`. It is the `PRELOADER` block right after
`<body>` — delete that block to switch it off.

---

## 10. Suggested order of work

1. `header.php` + `footer.php` + `functions.php` with assets enqueued — check a page renders styled.
2. `page.php` (generic) — covers the long tail immediately.
3. The blog: `single.php`, `archive.php` — 269 pages handled.
4. CPTs for `webinar` and `event` + their templates — another 291.
5. The twelve hand-designed page templates.
6. Forms and the Schedule backend last, once the shapes are all in place.
