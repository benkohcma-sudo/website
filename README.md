# Coach Masters Academy – Front-end Handoff

Static HTML/CSS/JS pages for the Coach Masters Academy website. Built to be
dropped into the existing Laravel site (Blade templates + `public/` assets).

## What's in here

```
index.html            one file per page, plain HTML
assets/css/main.css   all styles (self-contained, no dependency on old theme CSS)
assets/js/main.js     animations (GSAP + ScrollTrigger), vanilla JS, no jQuery
assets/img/           images
assets/fonts/         self-hosted fonts (if any)
```

## Integration notes for the developer

1. Copy `assets/` to `public/twenty26/` (or any folder) and update the paths
   in the `<head>`/footer. All paths in the HTML are relative (`assets/...`).
2. Convert each `.html` into a Blade view. Anything the client should edit
   from the admin CMS is marked with `<!-- CMS: ... -->` comments.
3. Do NOT load the old theme's `style.css`, Bootstrap 3, or Revolution
   Slider on these pages. The new pages are self-contained and the old
   global CSS will fight the layout.
4. Only external dependency is GSAP (loaded from cdnjs in the footer). It can
   be self-hosted by downloading `gsap.min.js` and `ScrollTrigger.min.js`
   into `assets/js/vendor/`.
5. Forms are static placeholders. Wire `action`/CSRF `_token` as usual.

## Local preview

Any static server works, e.g.

```
npx serve .
```
