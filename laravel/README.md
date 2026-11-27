# Our Social Foundation — Laravel handover (3 pages)

The front end for these three pages is finished. This folder holds them as Blade
views with their routes, so they can be dropped into the Laravel site.

> **Laravel or WordPress?** Both versions are in this repo and show the same pages.
> Use this folder if the pages go into the Laravel site. Use [`wordpress/README.md`](../wordpress/README.md)
> if they go into WordPress. You only need one of them.

| Page | URL | Blade view | Preview |
|---|---|---|---|
| Our Social Foundation | `/pages/our-social-foundation` | `social-foundation/index.blade.php` | https://website-one-dun-67.vercel.app/pages/our-social-foundation |
| I Am NOT Afraid (Cambodia, Feb 2025) | `/pages/our-social-foundation/i-am-not-afraid` | `social-foundation/i-am-not-afraid.blade.php` | https://website-one-dun-67.vercel.app/pages/our-social-foundation/i-am-not-afraid |
| Dare to Dream (Colombo, Feb 2026) | `/pages/our-social-foundation/dare-to-dream` | `social-foundation/dare-to-dream.blade.php` | https://website-one-dun-67.vercel.app/pages/our-social-foundation/dare-to-dream |

The static HTML of the same pages is in `dist/pages/our-social-foundation/`.

## Before you start

These pages use the **new design's** stylesheet, script and header/footer. They will
not look right inside the old `twenty25` layout. If the new layout is not in the
Laravel project yet, do steps 1–2 of `src/HANDOFF.md` first (copy `assets/`, build
the layout from any `dist/*/index.html`).

## Steps

1. **Assets.** Copy the repo's `assets/` folder to `public/assets/`. If you already
   copied it earlier, these files are new or changed and must be copied again:

   ```
   assets/css/main.css                       (changed)
   assets/js/main.js                         (changed)
   assets/img/logo.png                       (changed: now 1000x280, sharp on retina)
   assets/img/hero/social-foundation.jpg     (new)
   assets/img/sf-coaches.jpg                 (new)
   assets/img/sf-mentor.jpg                  (new)
   assets/img/sf-forward.jpg                 (new)
   assets/img/hero/sf-i-am-not-afraid.jpg    (new)
   assets/img/hero/sf-dare-to-dream.jpg      (new)
   assets/img/sf-i-am-not-afraid-video.jpg   (new: cover of the video card)
   ```

   The views call `asset('assets/...')`. If your assets live elsewhere
   (for example `public/twenty26/`), change that prefix in the three views.

2. **Views.** Copy `laravel/resources/views/social-foundation/` into the project's
   `resources/views/`.

3. **Layout.** Each view starts with `@extends('layouts.app')` and fills three
   sections: `title`, `meta_description`, `content`. Change those names to the ones
   your layout uses. If your layout already opens `<main>`, delete the `<main>`
   wrapper inside the view (a comment marks it).

4. **Routes.** Paste the three lines from `laravel/routes/social-foundation.php`
   into `routes/web.php`. Put them **above** any catch-all page route such as
   `Route::get('/pages/{slug}', ...)`, or that route will answer first.

5. **Menu.** In the About Us sub-menu, "Our Social Foundation" has no link on the
   current site (`href="#"`). Point it at `/pages/our-social-foundation`.

6. **Check.**
   * The three URLs open and the About sub-menu shows on each.
   * On Our Social Foundation, the two cards under "Personal Development Boot Camps"
     open the two event pages.
   * On I Am NOT Afraid, the play button opens the YouTube video in a popup
     (`https://www.youtube.com/watch?v=194TgmaGq60`).
   * On Dare to Dream, "What our participants say" shows six testimony cards drifting in two
     columns (they pause on hover, and sit still on phones), and "View the post on LinkedIn"
     opens the original post in a new tab.

## Nothing else is needed from the back end

* No form, no database table and no API call on these pages. The only form is the
  footer newsletter that every page shares.
* The scroll entrances, the video popup and the numbered cards are driven by
  `main.js` through the `data-reveal`, `data-seq` and `data-video` attributes already
  in the views. Leave those attributes where they are.

## If the client needs to edit these pages in the admin

The views are static on purpose, to get the pages live quickly. To make them
editable later, store the texts as page records and print them into the same markup.
The fields per page:

* **Our Social Foundation:** hero image; three chapters (heading, paragraphs, photo);
  two quotes between them (text, name); three card lines; closing quote (text, name).
* **Each event:** title, place, date; four facts (label, value); subtitle; body text;
  the video URL or the testimony link; closing line.

Keep the class names and the `data-*` attributes exactly as they are.

## Things to know

* **Wording.** The text is exactly what the client sent ("Social Foundation.docx"
  and "CMA Social Works.docx"). Please do not edit it.
* **Photos.** Every photograph on these three pages was generated to match the site.
  None is a photo of a real CMA event. On Our Social Foundation they show a global group
  of people and no identifiable city, at the client's request. On the two event pages the
  hero photo and the video cover are illustrations of that kind of camp, set in Cambodia
  and Sri Lanka. When the client sends real photos from the camps, send them to the
  designer and the views will be regenerated with them.
* **URLs.** If nested URLs are awkward in your routing, tell the designer the URLs
  you prefer and the links inside the pages will be regenerated to match.
* **Regenerating.** These views are produced by `src/tools/blade_export.py` from the
  built pages. After any design change the designer re-runs it and pushes; copy the
  three views again.
