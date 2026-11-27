# Our Social Foundation — WordPress handover (3 pages)

The front end for these three pages is finished. This folder holds them as WordPress
page templates, so they can be added to a WordPress theme.

> **Laravel or WordPress?** Both versions are in this repo and show the same pages.
> Use this folder if the pages go into WordPress. Use [`laravel/README.md`](../laravel/README.md)
> if they go into the Laravel site. You only need one of them.

| Page | WordPress slug | Template to choose | Preview |
|---|---|---|---|
| Our Social Foundation | `our-social-foundation` | Our Social Foundation | https://website-one-dun-67.vercel.app/pages/our-social-foundation |
| I Am NOT Afraid (Cambodia, Feb 2025) | `i-am-not-afraid` (child of Our Social Foundation) | Social Foundation - I Am NOT Afraid | https://website-one-dun-67.vercel.app/pages/our-social-foundation/i-am-not-afraid |
| Dare to Dream (Colombo, Feb 2026) | `dare-to-dream` (child of Our Social Foundation) | Social Foundation - Dare to Dream | https://website-one-dun-67.vercel.app/pages/our-social-foundation/dare-to-dream |

## What is in this folder

```
wordpress/theme-files/
  page-templates/template-social-foundation.php     the main page
  page-templates/template-sf-i-am-not-afraid.php    the Cambodia camp
  page-templates/template-sf-dare-to-dream.php      the Colombo camp
  functions-social-foundation.php                   loads the CSS and JS on those three pages only
```

## Steps

1. **Assets.** Copy the repo's `assets/` folder into the active theme, so you have
   `wp-content/themes/<your-theme>/assets/`. The templates find their files with
   `get_theme_file_uri( 'assets/...' )`.

2. **Templates.** Copy `theme-files/page-templates/` into the same theme folder, and
   `theme-files/functions-social-foundation.php` next to the theme's `functions.php`.

3. **Load the CSS and JS.** Add this line to the theme's `functions.php`:

   ```php
   require get_theme_file_path( 'functions-social-foundation.php' );
   ```

   It loads `main.css`, the Google fonts, GSAP and `main.js` on these three page
   templates only, so the rest of the site is not affected.

4. **Create the pages** (Pages → Add New):
   * "Our Social Foundation", slug `our-social-foundation`, template **Our Social Foundation**.
   * "I Am NOT Afraid", slug `i-am-not-afraid`, parent **Our Social Foundation**,
     template **Social Foundation - I Am NOT Afraid**.
   * "Dare to Dream", slug `dare-to-dream`, parent **Our Social Foundation**,
     template **Social Foundation - Dare to Dream**.

   Leave the page content empty: everything comes from the template.
   Settings → Permalinks must be set to "Post name", so the URLs become
   `/our-social-foundation/`, `/our-social-foundation/i-am-not-afraid/` and
   `/our-social-foundation/dare-to-dream/`.

5. **Menu.** In the About Us sub-menu, point "Our Social Foundation" at the new page.
   It is `#` on the current site.

6. **Check.**
   * The three pages open with the photo heroes and the About sub-menu.
   * On Our Social Foundation, the two cards under "Personal Development Boot Camps"
     open the two camp pages.
   * On I Am NOT Afraid, the play button opens the YouTube video in a popup.
   * On Dare to Dream, "What our participants say" shows six testimony cards drifting in two
     columns (they pause on hover, and sit still on phones), and "View the post on LinkedIn"
     opens the original post in a new tab.

## Things to know

* **Header and footer.** The templates call `get_header()` and `get_footer()`, so they use
  the theme's own header and footer. The page body is designed for the new header and
  footer; if the theme still has the old ones, the body will look right but the top and
  bottom of the page will not match until the theme's header and footer are updated
  (see "WordPress blog" in `src/HANDOFF.md`).
* **Old theme CSS.** `main.css` styles the whole page. If the old theme's CSS
  (Bootstrap 3, `style.css`) also loads on these pages, the two can clash. Dequeue the
  old stylesheets for these three templates if anything looks off.
* **Links to other pages.** Links to About Us, Our Story, Our Faculty and so on point at
  the main site's own addresses (`/about-us` etc.) and are left as they are. Only the
  links between the three Social Foundation pages go through `home_url()`.
* **No forms or data.** Nothing on these pages posts anywhere; the only form is the
  footer newsletter that every page shares.
* **Wording.** The text is exactly what the client sent. Please do not edit it.
* **Photos.** Every photograph on these pages was generated to match the site; none is a
  photo of a real CMA event. When the client sends real photos from the camps, send them
  to the designer and the templates will be regenerated with them.
* **Regenerating.** These templates are produced by `src/tools/wp_export.py` from the built
  pages. After any design change the designer re-runs it and pushes; copy the three
  templates again.
