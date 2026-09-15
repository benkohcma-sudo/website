# Coach Masters Academy — front-end handoff

This folder is the complete redesigned front end of **www.coachmastersacademy.com**:
one folder per URL (for example `about-us/index.html`), plus `assets/`. Every page's
copy is exactly what is on the live site today; only the layout, styling and motion
are new. It is plain HTML, CSS and JavaScript with no framework, so it drops into
the existing back end.

## What the live site runs on

* The main site is a **Laravel** application (AdminLTE admin at `/admin`, Blade
  templates, theme assets under `/public/twenty25/`). It is not WordPress.
* The blog at `/blog/` **is WordPress**.

So the job is: convert these pages into Blade views for the main site, and into a
theme for the WordPress blog. Both use the same `assets/` folder.

## Step by step (Laravel main site)

1. **Assets.** Copy `assets/` to `public/twenty26/` (any folder name is fine) and
   change the `/assets/...` paths in the templates to match. Everything the pages
   need is in there: `css/main.css`, `js/main.js`, `js/globe-data.js`, `img/`
   (logo and the ICF/CMA badges), `video/` (home staircase film, About globe film,
   poster frames).
2. **Layout.** Every page shares the same head, top bar, header, footer and
   script tags. Take those from any `index.html` once and make them the Blade
   layout. The header nav and footer links are the live site's own.
3. **Page templates.** Open each `index.html`, take the `<main>` block, and make it
   a Blade view. The pages fall into three kinds:
   * **Hand-designed pages** (build them as their own views): home `/`, `about-us`,
     `pages/our-story`, `our-faculty`, `icf-master-certified-coach-mcc` (founder),
     `icf-coaching-training-program` (certification), `events/calendar`, `webinar`,
     `registration`, `events/news`, `events/gallery`, `workshops`, `blog/coaching`.
   * **Landing pages** (`pages/our-services`, `coaching-skill-training-course-and-workshop`,
     `mentor-coaching`, and about 20 more): the CMS content is laid out as sections
     (logo lanes, stat cards, icon cards, chips). One view with these section
     patterns covers them all.
   * **Everything else** (articles, webinar and event detail, news detail, blog
     posts): one generic view — page title, breadcrumb, sub-navigation, then the
     content column.
4. **CMS regions.** Wherever the admin should keep editing content, the HTML is
   marked with `<!-- CMS: ... -->` comments. Replace the static text there with
   the Blade variables you already have. Do not change the wording; the client
   asked for the copy to stay as it is.
5. **Dynamic lists.** Faculty cards, calendar rows, news, gallery, webinars and
   blog cards are rendered from the same data the current site uses. Loop your
   existing collections into the card markup you see in those pages.
6. **Forms.** Field names, values and options are unchanged from the live site,
   so they post to the same controllers. Put back `action` and the `_token` field.
   Two things to note: long country lists were shortened to a placeholder (`<!-- CMS:
   full option list supplied by backend -->`), and the certification interest form
   is shown as a 4-step wizard by `main.js` (`form.js-steps`, `data-steps="2,2,5,3"`);
   it still submits as one form.
7. **Pagination.** Static preview uses `/page-2/` folders; keep your `?page=2`
   query strings and point the links at them.

## WordPress blog

Build a small theme from the same layout: `header.php` and `footer.php` from the
shared chrome, `index.php`/`archive.php` from `blog/coaching/index.html` (the card
grid), `single.php` from any post under `blog/…/index.html`. Enqueue `main.css`,
GSAP 3 (cdnjs), ScrollTrigger and `main.js`.

## Behaviour that lives in `assets/js/main.js`

| Where | What happens |
|---|---|
| Home hero | Staircase film. Page holds on the first frame with the headline; the first scroll plays the climb at 2× speed, then the welcome block rises in centred over the classroom and the page releases. Replays on every load. Phones play on arrival without the hold. |
| About Us hero | Globe film, driven by the scroll bar. The hero pins for about one and a half screens: the scroll position sets the film frame (so the earth spins as you scroll), the subheading fades out, then four centred counters count up. Scrolling back up runs it in reverse. Below 960px the film simply loops and the counters show. |
| Our Story, Certification | Curved orange journey line drawn by scroll, milestone cards slide in. |
| Our Faculty | Featured large card driven by the small cards and arrows; tabs per group. |
| Certification badges, Our Services badges | Badges fly into line from above and below as the row scrolls in (`[data-strip]`). |
| Client logos | Two endless lanes drifting in opposite directions (`.logo-lanes`). |
| Every page | Preloader: deep green screen with the white CMA logo and a thin orange line, then orange steps climb in left to right, fill the screen and lift away to open the page (about 3.5s). It runs on the first page of a visit only (sessionStorage key `cmaPre`), and never with `?nomotion` or reduced motion. Page entrances and scroll input wait until it opens. Markup is the `PRELOADER` block right after `<body>`; remove that block to switch it off. |
| Our Services, Team Coaching | Stat groups render as orange rings (`.ring-stat`): the ring fills in step with the number as it counts. Two rings per row on phones. The heading and intro above a stat group are centred (`.lp-block--center`). The card row after the stats is a centred open/close list (`.acc-cards--center`). |
| About Us | What We Stand For cards land one after another (`[data-seq]` on the grid: each child waits ~0.4s after the previous). Phones: the globe film sits behind the hero, centred in the upper middle, with the headline and counters below. |
| Forms (workshop interest, registration, webinars, calendar, certification) | Flat label + field runs are grouped at build time into `.field` wrappers; radio/checkbox options sit under their question in `.field--choices`. Field names, values and wording are unchanged. |
| Home brochure form | Orange staircase shape climbs into the form's lower-left corner (`.form-stage::before`, pure CSS clip-path), with a thin orange ring at the top-left. |
| Everywhere | Section entrances on `[data-reveal]`: headings and short copy arrive word by word with a soft blur, cards land as a shell first and then fill in, images scale in, buttons come last; items entering together are sequenced in DOM order. Hero headlines use `[data-split]`. Counters (`[data-count]`), marquees (`.marquee`). Add `?nomotion` to any URL to see the page without animation. |

Add `?nomotion` to any URL to see a page with all motion switched off. Users with
"reduce motion" turned on get that automatically.

## Keeping it up to date

Once the templates exist, most later changes from the designer are **asset swaps**:
replace `assets/css/main.css`, `assets/js/main.js` or files in `assets/img` and
`assets/video`. Layout changes to a specific page come as a fresh `index.html` for
that page plus a note of what moved. The designer keeps the source in git, so a
list of exactly what changed between two deliveries is always available.
