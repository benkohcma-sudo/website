/* ============================================================
   Coach Masters Academy — front-end behaviour
   Dependencies (loaded before this file): GSAP 3 + ScrollTrigger.
   Everything degrades gracefully if GSAP is missing.
   ============================================================ */
(function () {
  'use strict';
  var doc = document, win = window;
  var reduce = win.matchMedia('(prefers-reduced-motion: reduce)').matches || /nomotion/.test(location.search);
  var hasGsap = !!win.gsap;
  doc.documentElement.classList.remove('no-js');
  if (reduce) doc.documentElement.classList.add('reduce-motion');
  if (hasGsap && win.ScrollTrigger) gsap.registerPlugin(ScrollTrigger);
  if (hasGsap && win.MotionPathPlugin) gsap.registerPlugin(MotionPathPlugin);

  /* ---------- preloader: logo on green, then an orange staircase lifts away ---------- */
  var pre = doc.querySelector('.preloader'), preDone = false, preQueue = [];
  function afterPreloader(fn) { if (preDone) fn(); else preQueue.push(fn); }
  function finishPreloader() {
    if (preDone) return; preDone = true;
    doc.documentElement.classList.remove('is-preloading');
    if (pre && pre.parentNode) pre.parentNode.removeChild(pre);
    try { sessionStorage.setItem('cmaPre', '1'); } catch (e) {}
    preQueue.splice(0).forEach(function (fn) { fn(); });
    if (win.ScrollTrigger) ScrollTrigger.refresh();
  }
  ['wheel', 'touchmove', 'keydown'].forEach(function (type) {   // nothing behind the curtain reacts until it opens
    win.addEventListener(type, function (e) {
      if (preDone) return;
      if (type === 'keydown' && !/^(ArrowDown|ArrowUp|PageDown|PageUp|Space| |Home|End)$/.test(e.key)) return;
      e.preventDefault(); e.stopImmediatePropagation();
    }, { capture: true, passive: false });
  });
  function runPreloader() {
    if (!pre || reduce || !hasGsap || !doc.documentElement.classList.contains('is-preloading')) { finishPreloader(); return; }
    var logo = pre.querySelector('.preloader__logo'), line = pre.querySelector('.preloader__line');
    var steps = pre.querySelectorAll('.preloader__step'), n = steps.length;
    gsap.timeline({ onComplete: finishPreloader })
      .from(logo, { opacity: 0, y: 18, scale: .97, duration: .7, ease: 'power3.out' })
      .to(line, { scaleX: 1, duration: .8, ease: 'power2.inOut' }, '-=.35')
      .fromTo(steps, { scaleY: 0 }, { scaleY: function (i) { return (i + 1) / n; }, duration: .5, ease: 'power3.out', stagger: .055 }, '+=.1')   // the staircase
      .to(steps, { scaleY: 1, duration: .38, ease: 'power2.in', stagger: .035 }, '+=.08')                                                     // fills the screen
      .set([pre.querySelector('.preloader__bg'), logo], { opacity: 0 })
      .to(steps, { yPercent: -100, duration: .62, ease: 'power3.inOut', stagger: .055 }, '+=.04');                                          // lifts away step by step
  }
  runPreloader();

  /* ---------- header: shrink + hide on scroll down ---------- */
  var header = doc.querySelector('.site-header');
  var lastY = 0;
  function onScroll() {
    var y = win.scrollY;
    if (!header) return;
    if (doc.documentElement.classList.contains('keep-header')) { header.classList.add('is-scrolled'); header.classList.remove('is-hidden'); lastY = y; return; }   // a pinned section sits under the compact header
    header.classList.toggle('is-scrolled', y > 10);
    if (y > 320 && y > lastY + 4) header.classList.add('is-hidden');
    else if (y < lastY - 4) header.classList.remove('is-hidden');
    lastY = y;
  }
  win.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- mobile nav ---------- */
  var burger = doc.querySelector('.burger'), mnav = doc.querySelector('.mobile-nav');
  if (burger && mnav) burger.addEventListener('click', function () {
    var open = mnav.classList.toggle('is-open');
    burger.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', open);
    doc.body.style.overflow = open ? 'hidden' : '';
  });

  /* ---------- active nav link ---------- */
  var path = location.pathname.replace(/\/$/, '') || '/';
  doc.querySelectorAll('.nav a, .mobile-nav a, .subnav a, .aside-links a').forEach(function (a) {
    var href = (a.getAttribute('href') || '').replace(/\/$/, '') || '/';
    if (href === path || (href !== '/' && a.dataset.section && path.indexOf(a.dataset.section) === 0)) a.classList.add('is-active');
  });

  /* ---------- prose: wrap tables, auto reveal blocks ---------- */
  doc.querySelectorAll('.prose table').forEach(function (t) {
    if (t.parentElement.classList.contains('table-wrap')) return;
    var w = doc.createElement('div'); w.className = 'table-wrap'; t.parentNode.insertBefore(w, t); w.appendChild(t);
  });
  doc.querySelectorAll('.prose[data-auto-reveal] > *').forEach(function (el) { if (!el.hasAttribute('data-reveal')) el.setAttribute('data-reveal', ''); });

  /* ---------- step-by-step forms, open/close cards ---------- */
  initSteps();
  initAccordions();
  initTabs();
  initOffices();
  initVideoModal();
  initLightbox();

  /* ---------- marquee: duplicate track content for seamless loop ---------- */
  doc.querySelectorAll('.marquee__track').forEach(function (t) {
    var once = t.innerHTML, box = t.parentElement ? t.parentElement.clientWidth : win.innerWidth, n = 0;
    while (t.scrollWidth < box * 2 && n < 6) { t.innerHTML += once; n++; }   // enough copies for a seamless loop
    if (n === 0) t.innerHTML += once;
  });
  initElastic();

  if (reduce || !hasGsap) {
    doc.querySelectorAll('[data-reveal]').forEach(function (el) { el.style.opacity = 1; el.style.transform = 'none'; });
    doc.querySelectorAll('[data-count]').forEach(function (el) { el.textContent = parseFloat(el.dataset.count).toLocaleString() + (el.dataset.suffix || ''); });
    initFaculty(); initGlobe(true); initJourney(true); initHeroVideo(true); initHomeHero(true); return;
  }

  /* ============================================================
     Section entrances. Everything that carries [data-reveal] (and
     the hero headline) comes in the way the reference does:
       - headings and short text arrive word by word, soft and quick
       - cards land as an empty shell first, then their contents fill in
       - images scale gently into place, buttons follow last
     Elements that enter the viewport together are sequenced in DOM
     order, so a section reads: heading -> copy -> cards left to right.
     ============================================================ */
  var CARD_SEL = '.card, .icon-card, .photo-card, .service, .acc-card, .stand__card, .do-card, .stat, .quote-card, .pull, .proof__item, .news-card, .person, .feature-card, .office, .step-card, .track-card, .badge-float, .tab-panel__grid > *, .cta-full__inner';
  var PART_SEL = 'h1, h2, h3, h4, p, li, .lead, .btn, .link, img, video, figure, .eyebrow, .stat__num, .stat__label, .acc-card__head, .card__media, .do-card__media, .icon-card__img, .actions';
  var TEXT_SEL = 'p, li, .lead, .eyebrow, .stat__label, .acc-card__title, .acc-card__sub, blockquote';
  var mobileMotion = win.matchMedia('(max-width: 760px)').matches;
  var BLUR = mobileMotion ? 'blur(0px)' : 'blur(7px)';

  function wrapWords(node) {                                         // wrap every word in the text nodes below `node`
    if (node.nodeType === 3) {
      if (!/\S/.test(node.nodeValue)) return;
      var frag = doc.createDocumentFragment();
      node.nodeValue.split(/(\s+)/).forEach(function (w) {
        if (!w) return;
        if (/^\s+$/.test(w)) { frag.appendChild(doc.createTextNode(' ')); return; }
        var sp = doc.createElement('span'); sp.className = 'w'; sp.textContent = w; frag.appendChild(sp);
      });
      node.parentNode.replaceChild(frag, node);
      return;
    }
    if (node.nodeType !== 1) return;
    if (/^(SVG|IMG|VIDEO|INPUT|SELECT|TEXTAREA|BUTTON|CODE|PRE|BR)$/.test(node.tagName)) return;
    if (node.hasAttribute('data-count') || node.classList.contains('w')) return;
    Array.prototype.slice.call(node.childNodes).forEach(wrapWords);
  }
  function words(el) {
    if (!el.dataset.split) { wrapWords(el); el.dataset.split = '1'; }
    return el.querySelectorAll('.w');
  }
  function wordCount(el) { return (el.textContent.match(/\S+/g) || []).length; }

  function kindOf(el) {
    if (el.matches('.marquee, .marquee__track, .logo-section, .logo-row, .partners')) return 'plain';   // moving bands come in whole
    if (el.matches(CARD_SEL)) return 'card';
    if (/^H[1-4]$/.test(el.tagName)) return 'head';
    if (el.matches('img, video, figure, picture, .media, .media-stack, .card__media, .do-card__media, .icon-card__img, .globe-wrap, .split__media, iframe')) return 'media';
    if (el.matches('.btn, .link, .actions, .cta-full__actions, .hero__actions, .subnav, .badge-strip')) return 'action';
    if (el.matches('ul, ol')) return 'list';
    if (el.matches(TEXT_SEL)) return 'text';
    return 'block';
  }

  function addPart(tl, el, pos) {                                    // one element's own entrance, placed at `pos`
    var k = kindOf(el);
    if (el.querySelector('[data-count]') && k !== 'card' && k !== 'block') k = 'plain';
    if ((k === 'head' || k === 'text') && !words(el).length) k = 'plain';
    if (k === 'head') {
      tl.from(words(el), { opacity: 0, y: '.35em', filter: BLUR, duration: .75, ease: 'power3.out', stagger: .055, clearProps: 'filter,transform' }, pos);
    } else if (k === 'text' && wordCount(el) <= 48) {
      tl.from(words(el), { opacity: 0, y: '.25em', filter: mobileMotion ? 'blur(0px)' : 'blur(4px)', duration: .55, ease: 'power2.out', stagger: .014, clearProps: 'filter,transform' }, pos);
    } else if (k === 'media') {
      tl.from(el, { opacity: 0, scale: 1.06, duration: 1, ease: 'power3.out', clearProps: 'transform' }, pos);
    } else if (k === 'action') {
      var kids = el.children.length > 1 && el.matches('.actions, .cta-full__actions, .hero__actions, .badge-strip') ? el.children : el;
      tl.from(kids, { opacity: 0, y: 12, scale: .97, duration: .55, ease: 'power3.out', stagger: .08, clearProps: 'transform' }, pos);
    } else if (k === 'list' && el.children.length) {
      tl.from(el.children, { opacity: 0, x: -14, duration: .55, ease: 'power3.out', stagger: .07, clearProps: 'transform' }, pos);
    } else if (k === 'card') {
      tl.from(el, { opacity: 0, y: 24, scale: .96, duration: .6, ease: 'power3.out', clearProps: 'transform' }, pos);
      parts(el).forEach(function (c, i) { addPart(tl, c, i === 0 ? '<.16' : '<.1'); });
    } else if (k === 'block') {
      var ps = parts(el);
      if (ps.length && ps.length <= 14) {
        ps.forEach(function (c, i) { addPart(tl, c, i === 0 ? '<' : '<.1'); });
      } else tl.from(el, { opacity: 0, y: 22, duration: .8, ease: 'power3.out', clearProps: 'transform' }, pos);
    } else {
      tl.from(el, { opacity: 0, y: 16, duration: .7, ease: 'power3.out', clearProps: 'transform' }, pos);
    }
  }
  function parts(root) {                                             // the pieces inside a card / block, outermost first
    var all = Array.prototype.slice.call(root.querySelectorAll(PART_SEL + ', ' + CARD_SEL)), out = [];
    all.forEach(function (el) {
      if (el === root) return;
      var p = el.parentElement, nested = false;
      while (p && p !== root) { if (p.hasAttribute('data-reveal') || p.matches(CARD_SEL) || (p !== root && p.matches(PART_SEL))) { nested = true; break; } p = p.parentElement; }
      if (!nested) out.push(el);
    });
    return out;
  }
  function enter(el, delay) {
    if (el.dataset.entered) return; el.dataset.entered = '1';       // CSS now holds it visible; tweens below draw it in
    var tl = gsap.timeline({ delay: delay || 0 });
    addPart(tl, el, 0);
    return tl;
  }

  afterPreloader(function () {
    /* ---------- hero headline: in view on load, so it just plays ---------- */
    doc.querySelectorAll('[data-split], .hv__title').forEach(function (el) {
      gsap.from(words(el), { opacity: 0, y: '.35em', filter: BLUR, duration: .9, ease: 'power3.out', stagger: .06, delay: .15, clearProps: 'filter,transform' });
    });

    /* ---------- scroll reveals ---------- */
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 92%',
      once: true,
      onEnter: function (els) {
      els.forEach(function (el, i) {
        var seq = el.parentElement && el.parentElement.closest('[data-seq]');   // [data-seq]: children land one after another, 1-2-3-4
        if (seq) {
          var idx = Array.prototype.indexOf.call(seq.querySelectorAll(':scope > [data-reveal]'), el);
          enter(el, .1 + Math.max(0, idx) * .42);
        } else enter(el, Math.min(i, 6) * .11);
      });
    }
    });
  });

  /* ---------- drawn lines: [data-draw="x"|"y"] grow in as they scroll into view ---------- */
  doc.documentElement.classList.add('js-motion');
  doc.querySelectorAll('[data-draw]').forEach(function (el) {
    var axis = el.dataset.draw === 'y' ? 'scaleY' : 'scaleX';
    var from = {}; from[axis] = 0;
    gsap.fromTo(el, from, { scaleX: 1, scaleY: 1, duration: 1.1, ease: 'power3.inOut', scrollTrigger: { trigger: el, start: 'top 85%', once: true } });
  });

  /* ---------- counters ---------- */
  doc.querySelectorAll('[data-count]').forEach(function (el) {
    if (el.closest('.globe-stats--reveal')) return;
    var target = parseFloat(el.dataset.count), suffix = el.dataset.suffix || '';
    var obj = { v: 0 };
    var ring = el.closest('.ring-stat'), bar = ring ? ring.querySelector('.ring-stat__bar') : null;   // orange ring fills in step with the number
    ScrollTrigger.create({
      trigger: el, start: 'top 88%', once: true,
      onEnter: function () {
        gsap.to(obj, { v: target, duration: 1.8, ease: 'power2.out', onUpdate: function () { el.textContent = Math.round(obj.v).toLocaleString() + suffix; if (bar) bar.style.strokeDashoffset = 100 - 100 * (target ? obj.v / target : 1); } });
      }
    });
  });

  /* ---------- parallax images ---------- */
  doc.querySelectorAll('[data-parallax]').forEach(function (el) {
    var amt = parseFloat(el.dataset.parallax) || 40;
    gsap.fromTo(el, { y: -amt }, { y: amt, ease: 'none', scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* ---------- hero gallery float ---------- */
  doc.querySelectorAll('.hero__gallery .media').forEach(function (m, i) {
    gsap.from(m, { opacity: 0, y: 40, scale: .96, duration: 1.2, delay: .25 + i * .12, ease: 'power3.out' });
    gsap.to(m, { y: (i % 2 ? -1 : 1) * 10, duration: 3.2 + i * .6, yoyo: true, repeat: -1, ease: 'sine.inOut', delay: 1.5 });
  });


  initFaculty();
  initGlobe(false);
  initJourney();
  initHeroVideo();
  initHomeHero(false);
  initStrips();
  initFlowSide();
  win.addEventListener('load', function () { ScrollTrigger.refresh(); });
  // safety net: anything still hidden 4s after load is shown (e.g. if ScrollTrigger never fires)
  afterPreloader(function () { setTimeout(function () { doc.querySelectorAll('[data-reveal]').forEach(function (el) { if (el.closest('.globe-hero')) return; if (getComputedStyle(el).opacity === '0' && el.getBoundingClientRect().top < win.innerHeight) enter(el, 0); }); }, 4000); });

  /* ============================================================
     Step-by-step form: groups the existing fields into panels.
     Nothing is renamed, removed or reworded; data-steps="2,2,5,3"
     says how many questions go on each step.
     ============================================================ */
  function initSteps() {
    doc.querySelectorAll('form.js-steps').forEach(function (form) {
      var counts = (form.dataset.steps || '').split(',').map(Number).filter(Boolean);
      var nodes = Array.prototype.slice.call(form.children);
      var head = [], hidden = [], fields = [], cur = null;
      nodes.forEach(function (n) {
        var tag = n.tagName.toLowerCase();
        if (tag === 'input' && n.type === 'hidden') { hidden.push(n); return; }
        if ((tag === 'h4' || tag === 'p') && !fields.length) { head.push(n); return; }
        if (tag === 'label' && !n.querySelector('input,select,textarea')) { cur = { title: n, items: [] }; fields.push(cur); return; }
        if (cur) cur.items.push(n); else { cur = { title: null, items: [n] }; fields.push(cur); }
      });
      if (fields.length < 2) return;
      var steps = [], i = 0;
      counts.forEach(function (n) { if (i < fields.length) { steps.push(fields.slice(i, i + n)); i += n; } });
      if (i < fields.length) steps.push(fields.slice(i));

      form.innerHTML = '';
      head.forEach(function (h) { form.appendChild(h); });
      hidden.forEach(function (h) { form.appendChild(h); });

      var progress = doc.createElement('div'); progress.className = 'stepper__progress';
      progress.innerHTML = '<span class="stepper__count"></span><div class="stepper__bar"><i></i></div>';
      form.appendChild(progress);
      var count = progress.querySelector('.stepper__count'), bar = progress.querySelector('.stepper__bar i');

      var panels = steps.map(function (fs) {
        var panel = doc.createElement('div'); panel.className = 'stepper__panel';
        var isText = fs.some(function (f) { return f.items.length === 1 && !f.items[0].querySelector('input[type=checkbox],input[type=radio]'); });
        var host = panel;
        if (isText) { host = doc.createElement('div'); host.className = 'stepper__grid'; panel.appendChild(host); }
        fs.forEach(function (f) {
          var field = doc.createElement('div'); field.className = 'field';
          if (f.title) { f.title.classList.add('field__title'); field.appendChild(f.title); }
          var options = f.items.filter(function (el) { return el.tagName === 'LABEL' && el.querySelector('input[type=checkbox],input[type=radio]'); });
          if (options.length) {
            var grid = doc.createElement('div'); grid.className = 'field__options';
            var long = options.some(function (o) { return o.textContent.trim().length > 60; });
            if (long) grid.classList.add('field__options--wide');
            options.forEach(function (o) { o.classList.add('choice'); grid.appendChild(o); });
            field.appendChild(grid);
            if (isText) field.classList.add('field--full');
          }
          f.items.forEach(function (el) {
            if (options.indexOf(el) >= 0) return;
            var box = doc.createElement('div'); box.className = 'field__input'; box.appendChild(el); field.appendChild(box);
            if (el.tagName === 'TEXTAREA') field.classList.add('field--full');
          });
          host.appendChild(field);
        });
        form.appendChild(panel);
        return panel;
      });

      var nav = doc.createElement('div'); nav.className = 'stepper__nav';
      nav.innerHTML = '<button type="button" class="btn btn--ghost" data-back>Back</button><p class="stepper__error" aria-live="polite"></p>' +
        '<button type="button" class="btn" data-next>Next</button><button type="submit" class="btn" data-submit hidden>Submit</button>';
      form.appendChild(nav);
      var back = nav.querySelector('[data-back]'), next = nav.querySelector('[data-next]'), submit = nav.querySelector('[data-submit]'), err = nav.querySelector('.stepper__error');
      var at = 0;

      function valid(panel) {
        var ok = true;
        panel.querySelectorAll('input,select,textarea').forEach(function (el) {
          if (el.type === 'checkbox' || el.type === 'radio') {
            if (!el.required) return;
            var same = panel.querySelectorAll('[name="' + el.name.replace(/"/g, '\\"') + '"]');
            var any = Array.prototype.some.call(same, function (x) { return x.checked; });
            if (!any) ok = false;
          } else if (el.required && !el.checkValidity()) { if (ok) el.reportValidity(); ok = false; }
        });
        err.textContent = ok ? '' : 'Please answer the required questions marked * before continuing.';
        return ok;
      }
      function show(n, dir) {
        at = Math.max(0, Math.min(panels.length - 1, n));
        panels.forEach(function (p, j) { p.hidden = j !== at; });
        count.textContent = 'Step ' + (at + 1) + ' of ' + panels.length;
        bar.style.width = ((at + 1) / panels.length * 100) + '%';
        back.hidden = at === 0;
        next.hidden = at === panels.length - 1;
        submit.hidden = at !== panels.length - 1;
        err.textContent = '';
        if (hasGsap && !reduce && dir) gsap.from(panels[at], { opacity: 0, x: 24 * dir, duration: .45, ease: 'power3.out', clearProps: 'all' });
        if (dir) { var top = form.getBoundingClientRect().top + win.scrollY - 120; if (win.scrollY > top) win.scrollTo({ top: top, behavior: 'smooth' }); }
      }
      back.addEventListener('click', function () { show(at - 1, -1); });
      next.addEventListener('click', function () { if (valid(panels[at])) show(at + 1, 1); });
      form.addEventListener('submit', function (e) { if (!valid(panels[at])) e.preventDefault(); });
      form.addEventListener('keydown', function (e) { if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA' && at < panels.length - 1) { e.preventDefault(); next.click(); } });
      show(0, 0);
    });
  }

  /* ============================================================
     Badge strip: items start far above and below the row, alternating,
     and slide into line as the strip scrolls up the screen; then the
     whole row drifts sideways a little as you keep scrolling.
     ============================================================ */
  /* orange ribbon in a side margin that pours down as its section scrolls past */
  function initFlowSide() {
    doc.querySelectorAll('.flow-side__svg').forEach(function (svg) {
      if (getComputedStyle(svg).display === 'none') return;
      gsap.fromTo(svg, { clipPath: 'inset(0% 0% 100% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', ease: 'none',
        scrollTrigger: { trigger: svg.parentElement, start: 'top 75%', end: 'bottom 65%', scrub: 0.8 } });
    });
  }

  /* [data-video] links open their video in a popup: YouTube in an embedded player, files in a native player */
  function initVideoModal() {
    doc.addEventListener('click', function (e) {
      var a = e.target.closest ? e.target.closest('[data-video]') : null;
      if (!a) return;
      var src = a.getAttribute('href') || a.getAttribute('data-video');
      if (!src) return;
      e.preventDefault();
      openVideo(src, a);
    });
  }
  function openVideo(src, opener) {
    var yt = src.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([\w-]{6,})/);
    var wrap = doc.createElement('div');
    wrap.className = 'video-modal';
    wrap.setAttribute('role', 'dialog'); wrap.setAttribute('aria-modal', 'true'); wrap.setAttribute('aria-label', 'Video');
    var media = yt
      ? '<iframe src="https://www.youtube.com/embed/' + yt[1] + '?autoplay=1&rel=0" title="Video" allow="autoplay; encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe>'
      : '<video controls autoplay playsinline preload="metadata"></video>';
    wrap.innerHTML = '<div class="video-modal__box">' + media + '</div><button class="video-modal__close" type="button" aria-label="Close video"></button>';
    if (!yt) wrap.querySelector('video').src = src;
    doc.body.appendChild(wrap);
    doc.documentElement.classList.add('modal-open');
    var close = wrap.querySelector('.video-modal__close');
    function shut() {
      var v = wrap.querySelector('video'); if (v) { v.pause(); v.removeAttribute('src'); v.load(); }
      wrap.classList.remove('is-open');
      doc.documentElement.classList.remove('modal-open');
      doc.removeEventListener('keydown', onKey);
      setTimeout(function () { if (wrap.parentNode) wrap.parentNode.removeChild(wrap); }, 320);
      if (opener && opener.focus) opener.focus();
    }
    function onKey(ev) { if (ev.key === 'Escape') shut(); }
    close.addEventListener('click', shut);
    wrap.addEventListener('click', function (ev) { if (ev.target === wrap) shut(); });
    doc.addEventListener('keydown', onKey);
    requestAnimationFrame(function () { wrap.classList.add('is-open'); close.focus(); });
  }

  /* [data-lightbox="group"] links open their image large, with previous / next through the group */
  function initLightbox() {
    doc.addEventListener('click', function (e) {
      var a = e.target.closest ? e.target.closest('[data-lightbox]') : null;
      if (!a) return;
      e.preventDefault();
      var group = Array.prototype.slice.call(doc.querySelectorAll('[data-lightbox="' + a.getAttribute('data-lightbox') + '"]'));
      openLightbox(group, group.indexOf(a), a);
    });
  }
  function openLightbox(items, at, opener) {
    var wrap = doc.createElement('div');
    wrap.className = 'video-modal lightbox';
    wrap.setAttribute('role', 'dialog'); wrap.setAttribute('aria-modal', 'true'); wrap.setAttribute('aria-label', 'Image viewer');
    wrap.innerHTML = '<figure class="lightbox__stage"><img alt=""><figcaption class="lightbox__count"></figcaption></figure>' +
      '<button class="lightbox__nav lightbox__nav--prev" type="button" aria-label="Previous image"></button>' +
      '<button class="lightbox__nav lightbox__nav--next" type="button" aria-label="Next image"></button>' +
      '<button class="video-modal__close" type="button" aria-label="Close"></button>';
    var img = wrap.querySelector('img'), count = wrap.querySelector('.lightbox__count');
    if (items.length < 2) wrap.classList.add('lightbox--single');
    function show(i) {
      at = (i + items.length) % items.length;
      img.src = items[at].getAttribute('href');
      var t = items[at].querySelector('img'); img.alt = t ? t.alt : '';
      count.textContent = (at + 1) + ' / ' + items.length;
    }
    function shut() {
      wrap.classList.remove('is-open');
      doc.documentElement.classList.remove('modal-open');
      doc.removeEventListener('keydown', onKey);
      setTimeout(function () { if (wrap.parentNode) wrap.parentNode.removeChild(wrap); }, 320);
      if (opener && opener.focus) opener.focus();
    }
    function onKey(ev) {
      if (ev.key === 'Escape') shut();
      else if (ev.key === 'ArrowRight') show(at + 1);
      else if (ev.key === 'ArrowLeft') show(at - 1);
    }
    wrap.querySelector('.video-modal__close').addEventListener('click', shut);
    wrap.querySelector('.lightbox__nav--prev').addEventListener('click', function () { show(at - 1); });
    wrap.querySelector('.lightbox__nav--next').addEventListener('click', function () { show(at + 1); });
    wrap.addEventListener('click', function (ev) { if (ev.target === wrap || ev.target.classList.contains('lightbox__stage')) shut(); });
    doc.addEventListener('keydown', onKey);
    show(at);
    doc.body.appendChild(wrap);
    doc.documentElement.classList.add('modal-open');
    requestAnimationFrame(function () { wrap.classList.add('is-open'); wrap.querySelector('.video-modal__close').focus(); });
  }

  function initStrips() {
    doc.querySelectorAll('[data-strip]').forEach(function (strip) {
      var items = Array.prototype.slice.call(strip.children);
      var offsets = [-190, 210, -150, 190, -220, 170, -170, 200];
      items.forEach(function (el, i) {
        gsap.fromTo(el, { y: offsets[i % offsets.length], opacity: 0, scale: .82, rotate: (i % 2 ? 4 : -4) },
          { y: 0, opacity: 1, scale: 1, rotate: 0, ease: 'none',
            scrollTrigger: { trigger: strip, start: 'top bottom', end: 'center 60%', scrub: 0.6 } });
      });
      gsap.fromTo(strip.children, { x: 22 }, { x: -22, ease: 'none', scrollTrigger: { trigger: strip, start: 'top bottom', end: 'bottom top', scrub: true } });
    });
  }

  /* ============================================================
     Home hero: the first frame waits with a "scroll to begin" hint.
     One scroll plays the staircase video through; as it arrives the
     header slides down and the words rise into place.
     ============================================================ */
  function initHomeHero(staticOnly) {
    var hero = doc.querySelector('[data-home-hero]');
    if (!hero) return;
    var video = hero.querySelector('.hv__video'), scrim = hero.querySelector('.hv__scrim:not(.hv__scrim--end)'), endScrim = hero.querySelector('.hv__scrim--end');
    var copy = hero.querySelector('.hv__copy'), endBlock = hero.querySelector('[data-hero-end]');
    var endItems = endBlock ? Array.prototype.slice.call(endBlock.querySelectorAll('.hv__end-inner > *')) : [];
    var html = doc.documentElement;
    var RATE = 2;                                                    // the climb runs at double speed
    var mobile = win.matchMedia('(max-width: 760px)').matches;
    // every arrival at the home page starts at the foot of the stairs, refresh included,
    // so the browser must not drop us back at a remembered scroll position
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';

    function landInstantly() {                                       // already been through the door: classroom + welcome
      var toEnd = function () { try { video.currentTime = Math.max(0, (video.duration || 6) - 0.05); } catch (e) {} };
      if (video.readyState >= 1) toEnd(); else video.addEventListener('loadedmetadata', toEnd);
      if (copy) copy.style.display = 'none';
      if (scrim) scrim.style.opacity = 0;
      if (endScrim) endScrim.style.opacity = 1;
      if (endBlock) { endBlock.style.opacity = 1; endBlock.classList.add('is-on'); }
      endItems.forEach(function (el) { el.style.opacity = 1; });
    }
    if (staticOnly || location.hash) { landInstantly(); return; }
    html.classList.add('js-motion');

    var started = false;
    function release() {
      html.classList.remove('hv-locked');
      ScrollTrigger.refresh();
    }
    function land() {                                                // the welcome rises in over the classroom
      if (endBlock) endBlock.classList.add('is-on');
      var tl = gsap.timeline({ defaults: { ease: 'power3.out' }, onComplete: release });
      tl.to(endScrim, { opacity: 1, duration: 1.0 }, 0)
        .to(endBlock, { opacity: 1, duration: .3 }, 0)
        .fromTo(endItems, { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: .8, stagger: .12 }, .15);
    }
    function start() {
      if (started) return; started = true;
      video.playbackRate = RATE;
      video.currentTime = 0;
      var p = video.play(); if (p && p.catch) p.catch(land);
      gsap.to(copy.children, { opacity: 0, y: -28, duration: .55, ease: 'power2.in', stagger: .05 });   // the words step aside as we climb
      gsap.to(scrim, { opacity: 0, duration: 1.2, ease: 'power2.inOut' });
      var done = false;
      var finish = function () { if (done) return; done = true; if (copy) copy.style.display = 'none'; land(); };
      video.addEventListener('timeupdate', function () { if (!done && video.duration && video.currentTime > video.duration - 0.35) finish(); });
      video.addEventListener('ended', finish);
      setTimeout(finish, ((video.duration || 6) / RATE + 1.5) * 1000);   // safety net
    }
    if (mobile) { start(); return; }                                 // phones: climb on arrival, no lock
    html.classList.add('hv-locked'); win.scrollTo(0, 0);
    function onWheel(e) { if (html.classList.contains('hv-locked')) { e.preventDefault(); if (e.deltaY > 0) start(); } }
    function onKey(e) { if (html.classList.contains('hv-locked') && /^(ArrowDown|PageDown|Space| )$/.test(e.key)) { e.preventDefault(); start(); } }
    var touchY = null;
    win.addEventListener('wheel', onWheel, { passive: false });
    win.addEventListener('keydown', onKey);
    win.addEventListener('touchstart', function (e) { touchY = e.touches[0].clientY; }, { passive: true });
    win.addEventListener('touchmove', function (e) { if (html.classList.contains('hv-locked')) { e.preventDefault(); if (touchY !== null && touchY - e.touches[0].clientY > 8) start(); } }, { passive: false });
    video.load();
  }

  /* ============================================================
     Open/close cards: one open at a time, height animates via CSS grid
     ============================================================ */
  function initAccordions() {
    doc.querySelectorAll('[data-accordion]').forEach(function (group) {
      var cards = Array.prototype.slice.call(group.querySelectorAll('.acc-card'));
      cards.forEach(function (card) {
        var head = card.querySelector('.acc-card__head');
        if (!head) return;
        head.addEventListener('click', function () {
          var open = card.classList.contains('is-open');
          cards.forEach(function (c) { c.classList.remove('is-open'); var h = c.querySelector('.acc-card__head'); if (h) h.setAttribute('aria-expanded', 'false'); });
          if (!open) { card.classList.add('is-open'); head.setAttribute('aria-expanded', 'true'); }
          if (win.ScrollTrigger) setTimeout(function () { ScrollTrigger.refresh(); }, 600);
        });
      });
    });
  }

  /* ============================================================
     Regional offices: region tabs switch the list; picking an office
     moves the map to it.
     ============================================================ */
  function initOffices() {
    doc.querySelectorAll('[data-offices]').forEach(function (root) {
      var canvas = root.querySelector('.offices__canvas');
      var cards = Array.prototype.slice.call(root.querySelectorAll('.office--globe'));
      var regions = Array.prototype.slice.call(root.querySelectorAll('.offices__regions .chip'));
      var placeSets = Array.prototype.slice.call(root.querySelectorAll('.offices__places'));
      var places = Array.prototype.slice.call(root.querySelectorAll('.chip--place'));
      var count = root.querySelector('.offices__count b');
      if (!cards.length) return;
      var land = win.CMA_LAND || new Float32Array(0), dpr = Math.min(2, win.devicePixelRatio || 1);
      var ctx = canvas ? canvas.getContext('2d') : null;
      var motion = hasGsap && !reduce;
      var rot = { y: 0, x: 0.3 }, size = 0, R = 0, auto = true, resumeAt = 0, active = 0, drag = null, inView = true;
      var pts = new Float32Array(land.length / 2 * 3);
      function toXYZ(lat, lon) { var la = lat * Math.PI / 180, lo = lon * Math.PI / 180; return [Math.cos(la) * Math.cos(lo), Math.sin(la), Math.cos(la) * Math.sin(lo)]; }
      for (var i = 0; i < land.length; i += 2) { var q = toXYZ(land[i], land[i + 1]); pts[i / 2 * 3] = q[0]; pts[i / 2 * 3 + 1] = q[1]; pts[i / 2 * 3 + 2] = q[2]; }
      var pins = cards.map(function (c) { var lat = +c.dataset.lat, lon = +c.dataset.lon; return { lat: lat, lon: lon, xyz: toXYZ(lat, lon), sx: 0, sy: 0, z: -1 }; });
      var home = 0;
      cards.forEach(function (c, i) { if (/singapore/i.test(c.querySelector('.office__name').textContent)) home = i; });
      function resize() { if (!canvas) return; size = canvas.clientWidth; canvas.width = size * dpr; canvas.height = size * dpr; R = size * 0.44; }
      function project(v) {
        var cy = Math.cos(rot.y), sy = Math.sin(rot.y), x1 = v[0] * cy - v[2] * sy, z1 = v[0] * sy + v[2] * cy;
        var cx = Math.cos(rot.x), sx = Math.sin(rot.x), y1 = v[1] * cx - z1 * sx, z2 = v[1] * sx + z1 * cx;
        return [size / 2 + x1 * R, size / 2 - y1 * R, z2];
      }
      function draw() {
        if (!ctx || !size) return;
        var k = size / 640;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, size, size);
        ctx.fillStyle = '#F4EFE7'; ctx.beginPath(); ctx.arc(size / 2, size / 2, R, 0, 6.283); ctx.fill();
        ctx.strokeStyle = 'rgba(23,56,14,0.12)'; ctx.lineWidth = 1; ctx.stroke();
        ctx.strokeStyle = 'rgba(23,56,14,0.07)';
        for (var lat = -60; lat <= 60; lat += 30) {
          ctx.beginPath(); var first = true;
          for (var lon = -180; lon <= 180; lon += 6) { var s = project(toXYZ(lat, lon)); if (s[2] < 0) { first = true; continue; } if (first) { ctx.moveTo(s[0], s[1]); first = false; } else ctx.lineTo(s[0], s[1]); }
          ctx.stroke();
        }
        for (var i = 0; i < pts.length; i += 3) {
          var s2 = project([pts[i], pts[i + 1], pts[i + 2]]); if (s2[2] < -0.02) continue;
          ctx.fillStyle = 'rgba(23,56,14,' + ((0.25 + 0.75 * Math.max(0, s2[2])) * 0.85).toFixed(3) + ')';
          ctx.beginPath(); ctx.arc(s2[0], s2[1], (1.1 + 1.3 * s2[2]) * k, 0, 6.283); ctx.fill();
        }
        var t = performance.now() / 1000, a = pins[active], h = pins[home];
        var pa = project(a.xyz), ph = project(h.xyz);
        if (pa[2] > 0 && ph[2] > 0 && active !== home) {                                   // arc from the Global Office to the chosen office
          var mx = (a.xyz[0] + h.xyz[0]) / 2, my = (a.xyz[1] + h.xyz[1]) / 2, mz = (a.xyz[2] + h.xyz[2]) / 2, ml = Math.sqrt(mx * mx + my * my + mz * mz) || 1;
          var m = project([mx / ml * 1.3, my / ml * 1.3, mz / ml * 1.3]);
          ctx.strokeStyle = 'rgba(235,100,34,0.55)'; ctx.lineWidth = 1.4 * k; ctx.beginPath(); ctx.moveTo(ph[0], ph[1]); ctx.quadraticCurveTo(m[0], m[1], pa[0], pa[1]); ctx.stroke();
        }
        pins.forEach(function (p, i) {
          var s3 = project(p.xyz); p.sx = s3[0]; p.sy = s3[1]; p.z = s3[2];
          if (s3[2] < 0.05) return;
          var on = i === active;
          if (on) { var pulse = (Math.sin(t * 2.4) + 1) / 2; ctx.strokeStyle = 'rgba(235,100,34,' + (0.9 - 0.6 * pulse) + ')'; ctx.lineWidth = 2 * k; ctx.beginPath(); ctx.arc(s3[0], s3[1], (9 + 12 * pulse) * k, 0, 6.283); ctx.stroke(); }
          ctx.fillStyle = on ? '#eb6422' : 'rgba(235,100,34,' + (0.45 + 0.55 * s3[2]).toFixed(2) + ')';
          ctx.beginPath(); ctx.arc(s3[0], s3[1], (on ? 6 : 3.6) * k, 0, 6.283); ctx.fill();
          if (on) { ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(s3[0], s3[1], 2.2 * k, 0, 6.283); ctx.fill(); }
        });
      }
      function targetFor(i) {
        var p = pins[i], ty = Math.PI / 2 - p.lon * Math.PI / 180, tx = Math.max(-1, Math.min(1, p.lat * Math.PI / 180 * 0.9));
        var twoPi = Math.PI * 2; ty = rot.y + ((ty - rot.y + Math.PI) % twoPi + twoPi) % twoPi - Math.PI;   // shortest way round
        return { y: ty, x: tx };
      }
      function select(i, opts) {
        opts = opts || {};
        active = (i + cards.length) % cards.length;
        var region = cards[active].dataset.region;
        cards.forEach(function (c, k) { c.hidden = k !== active; });
        places.forEach(function (b) { b.classList.toggle('is-active', +b.dataset.office === active); });
        regions.forEach(function (b) { b.classList.toggle('is-active', b.dataset.region === region); b.setAttribute('aria-selected', b.dataset.region === region); });
        placeSets.forEach(function (p) { p.hidden = p.dataset.region !== region; });
        if (count) count.textContent = active + 1;
        var tg = targetFor(active);
        if (motion) {
          gsap.killTweensOf(rot); gsap.to(rot, { y: tg.y, x: tg.x, duration: opts.instant ? 0 : 1.1, ease: 'power3.inOut' });
          if (!opts.quiet) gsap.from(cards[active], { opacity: 0, y: 14, duration: .45, ease: 'power3.out', clearProps: 'all' });
        } else { rot.y = tg.y; rot.x = tg.x; draw(); }
        auto = false; resumeAt = performance.now() + 7000;
      }
      regions.forEach(function (b) { b.addEventListener('click', function () { for (var k = 0; k < cards.length; k++) if (cards[k].dataset.region === b.dataset.region) { select(k); break; } }); });
      places.forEach(function (b) { b.addEventListener('click', function () { select(+b.dataset.office); }); });
      root.querySelectorAll('.offices__arrow').forEach(function (b) { b.addEventListener('click', function () { select(active + (+b.dataset.dir)); }); });
      if (canvas) {                                                                                     // drag to spin, tap a pin to choose it
        canvas.addEventListener('pointerdown', function (e) { drag = { x: e.clientX, y: e.clientY, ry: rot.y, rx: rot.x, moved: false }; try { canvas.setPointerCapture(e.pointerId); } catch (err) {} if (motion) gsap.killTweensOf(rot); });
        canvas.addEventListener('pointermove', function (e) {
          if (!drag) return; var dx = e.clientX - drag.x, dy = e.clientY - drag.y;
          if (Math.abs(dx) + Math.abs(dy) > 4) drag.moved = true;
          rot.y = drag.ry + dx * 0.006; rot.x = Math.max(-1.1, Math.min(1.1, drag.rx + dy * 0.006)); auto = false; resumeAt = performance.now() + 7000;
          if (!motion) draw();
        });
        function up(e) {
          if (!drag) return;
          if (!drag.moved) {
            var r = canvas.getBoundingClientRect(), x = (e.clientX - r.left) * (size / r.width), y = (e.clientY - r.top) * (size / r.height), best = -1, bd = 18 * (size / 640) * 1.4;
            pins.forEach(function (p, i) { if (p.z < 0.05) return; var d = Math.hypot(p.sx - x, p.sy - y); if (d < bd) { bd = d; best = i; } });
            if (best >= 0) select(best);
          }
          drag = null;
        }
        canvas.addEventListener('pointerup', up); canvas.addEventListener('pointercancel', function () { drag = null; });
        canvas.style.touchAction = 'none';
      }
      resize(); win.addEventListener('resize', function () { resize(); draw(); });
      select(0, { instant: true, quiet: true });
      draw();
      root.__globe = { select: select, get active() { return active; }, pins: pins, rot: rot };   // hook for tests
      if (!motion) return;
      if ('IntersectionObserver' in win) new IntersectionObserver(function (es) { inView = es[0].isIntersecting; }, { rootMargin: '120px' }).observe(root);
      gsap.ticker.add(function (time, dt) {
        if (!inView) return;
        if (!auto && !drag && performance.now() > resumeAt && !gsap.isTweening(rot)) auto = true;
        if (auto && !drag) rot.y += dt * 0.00012;
        draw();
      });
    });
  }

  /* ============================================================
     Elastic expanding gallery: the hovered or tapped panel springs open
     ============================================================ */
  function initElastic() {
    doc.querySelectorAll('[data-elastic]').forEach(function (g) {
      var panels = Array.prototype.slice.call(g.querySelectorAll('.elastic__panel'));
      var activate = function (p) { panels.forEach(function (x) { x.classList.toggle('is-active', x === p); }); };
      panels.forEach(function (p) {
        p.addEventListener('click', function () { activate(p); });
        if (win.matchMedia('(pointer:fine)').matches) p.addEventListener('mouseenter', function () { activate(p); });
      });
    });
  }

  /* ============================================================
     Simple tabs: [data-tabs] buttons switch the .tab-panel siblings that follow
     ============================================================ */
  function initTabs() {
    doc.querySelectorAll('[data-tabs]').forEach(function (bar) {
      var btns = Array.prototype.slice.call(bar.querySelectorAll('button'));
      var wrap = bar.nextElementSibling; if (!wrap) return;
      var panels = Array.prototype.slice.call(wrap.querySelectorAll('.tab-panel'));
      btns.forEach(function (b, i) {
        b.addEventListener('click', function () {
          btns.forEach(function (x, j) { x.classList.toggle('is-active', j === i); x.setAttribute('aria-selected', j === i ? 'true' : 'false'); });
          panels.forEach(function (p, j) { p.hidden = j !== i; p.classList.toggle('is-active', j === i); });
          if (hasGsap && !reduce && panels[i]) gsap.from(panels[i].children, { opacity: 0, y: 16, duration: .55, ease: 'power3.out', clearProps: 'all' });
          if (win.ScrollTrigger) setTimeout(function () { ScrollTrigger.refresh(); }, 400);
        });
      });
    });
  }

  /* ============================================================
     Faculty carousel — tabs + horizontal snap track + counter
     ============================================================ */
  function initFaculty() {
    doc.querySelectorAll('.faculty').forEach(function (root) {
      var tabs = root.querySelectorAll('.tabs button');
      var groups = root.querySelectorAll('.faculty__track');
      var feature = root.querySelector('[data-feature]');
      var prev = root.querySelector('[data-prev]'), next = root.querySelector('[data-next]');
      var counter = root.querySelector('.counter'), bar = root.querySelector('.bar i');
      var track = null, index = 0;

      function cards() { return track ? track.querySelectorAll('.person--sm') : []; }

      function paint(card) {
        if (!feature || !card) return;
        var img = feature.querySelector('[data-f-img]');
        var set = function (sel, val) {
          var el = feature.querySelector(sel); if (!el) return;
          el.textContent = val || '';
        };
        var apply = function () {
          if (img && img.getAttribute('src') !== card.dataset.img) { img.src = card.dataset.img; img.alt = card.dataset.name; }
          set('[data-f-name]', card.dataset.name);
          set('[data-f-cred]', card.dataset.cred);
          set('[data-f-role]', card.dataset.role);
          set('[data-f-loc]', card.dataset.loc);
          var lw = feature.querySelector('[data-f-locwrap]'); if (lw) lw.hidden = !card.dataset.loc;
        };
        if (!hasGsap || reduce) { apply(); return; }
        var body = feature.querySelector('.person__body');
        gsap.timeline()
          .to([body, img], { opacity: 0, duration: .18, ease: 'power2.in', onComplete: apply })
          .fromTo(img, { scale: 1.04 }, { scale: 1, opacity: 1, duration: .5, ease: 'power3.out' })
          .fromTo(body, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: .45, ease: 'power3.out' }, '<');
      }

      function select(i, scroll) {
        var list = cards(); if (!list.length) return;
        index = Math.max(0, Math.min(list.length - 1, i));
        list.forEach(function (c, j) { c.classList.toggle('is-active', j === index); c.setAttribute('aria-current', j === index ? 'true' : 'false'); });
        paint(list[index]);
        if (counter) counter.innerHTML = String(index + 1).padStart(2, '0') + ' <span>/ ' + String(list.length).padStart(2, '0') + '</span>';
        if (bar) { bar.style.width = (100 / list.length) + '%'; bar.style.left = (index * 100 / list.length) + '%'; }
        if (prev) prev.disabled = index === 0;
        if (next) next.disabled = index === list.length - 1;
        if (scroll !== false) {
          var c = list[index], t = track;
          var left = c.offsetLeft - (t.clientWidth - c.offsetWidth) / 2;
          t.scrollTo({ left: Math.max(0, left), behavior: 'smooth' });
        }
      }

      function showGroup(g) {
        tabs.forEach(function (b, j) { b.classList.toggle('is-active', j === g); });
        groups.forEach(function (t, j) { t.hidden = j !== g; });
        track = groups[g];
        track.scrollTo({ left: 0 });
        select(0, false);
        if (hasGsap && !reduce) gsap.from(track.children, { opacity: 0, y: 20, duration: .6, stagger: .04, ease: 'power3.out', clearProps: 'all' });
      }

      groups.forEach(function (t) {
        t.querySelectorAll('.person--sm').forEach(function (card, i) {
          card.addEventListener('click', function () { if (t === track) select(i); });
        });
      });
      tabs.forEach(function (b, i) { b.addEventListener('click', function () { showGroup(i); }); });
      if (prev) prev.addEventListener('click', function () { select(index - 1); });
      if (next) next.addEventListener('click', function () { select(index + 1); });
      root.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { select(index + 1); }
        else if (e.key === 'ArrowLeft') { select(index - 1); }
      });
      if (groups.length) showGroup(0);

      var map = root.querySelector('canvas.faculty__map');
      if (map && win.CMA_LAND) drawFlatMap(map);
    });
  }

  function drawFlatMap(canvas) {
    var dpr = Math.min(2, win.devicePixelRatio || 1);
    function paint() {
      var w = canvas.clientWidth, h = canvas.clientHeight;
      canvas.width = w * dpr; canvas.height = h * dpr;
      var ctx = canvas.getContext('2d'); ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, w, h);
      var d = win.CMA_LAND;
      for (var i = 0; i < d.length; i += 2) {
        var lat = d[i], lon = d[i + 1];
        var x = (lon + 180) / 360 * w, y = (90 - lat) / 180 * h;
        ctx.fillStyle = 'rgba(23,56,14,' + (0.10 + 0.08 * Math.random()) + ')';
        ctx.beginPath(); ctx.arc(x, y, 1.6, 0, 6.283); ctx.fill();
      }
    }
    paint(); win.addEventListener('resize', paint);
  }

  /* ============================================================
     Globe — canvas dot sphere; spins one full turn over one scroll
     ============================================================ */
  function initGlobe(staticOnly) {
    var canvas = doc.querySelector('canvas.globe');
    if (!canvas || !win.CMA_LAND) return;
    var dpr = Math.min(2, win.devicePixelRatio || 1);
    var ctx = canvas.getContext('2d');
    var land = win.CMA_LAND;
    // regional offices (from the site copy): Global Office Singapore + regions
    var pins = [
      [1.35, 103.8, 'Singapore · Global Office'], [3.1, 101.7, 'Malaysia'], [13.7, 100.5, 'Thailand'], [21.0, 105.8, 'Vietnam'],
      [14.6, 121.0, 'Philippines'], [19.1, 72.9, 'India'], [6.9, 79.9, 'Sri Lanka'], [-33.9, 151.2, 'Australia'],
      [-36.8, 174.8, 'New Zealand'], [25.2, 55.3, 'UAE'], [33.9, 35.5, 'Lebanon'], [0.3, 32.6, 'Uganda'],
      [6.5, 3.4, 'Nigeria'], [-1.3, 36.8, 'Kenya'], [44.4, 26.1, 'Romania'], [51.5, -0.1, 'United Kingdom'],
      [50.1, 8.7, 'Germany'], [43.7, -79.4, 'Canada'], [40.7, -74.0, 'United States'], [-23.5, -46.6, 'Brazil'], [48.0, 66.9, 'Kazakhstan']
    ];
    var rot = { y: -0.9, x: 0.35 }, idle = 0, size = 0, R = 0;
    var pts = new Float32Array(land.length / 2 * 3), pinsXYZ = [];
    function toXYZ(lat, lon) {
      var la = lat * Math.PI / 180, lo = lon * Math.PI / 180;
      return [Math.cos(la) * Math.cos(lo), Math.sin(la), Math.cos(la) * Math.sin(lo)];
    }
    for (var i = 0; i < land.length; i += 2) { var p = toXYZ(land[i], land[i + 1]); pts[i / 2 * 3] = p[0]; pts[i / 2 * 3 + 1] = p[1]; pts[i / 2 * 3 + 2] = p[2]; }
    pins.forEach(function (pin) { pinsXYZ.push(toXYZ(pin[0], pin[1]).concat([pin[2]])); });
    function resize() {
      size = canvas.clientWidth; canvas.width = size * dpr; canvas.height = size * dpr; R = size * 0.42;
    }
    function project(x, y, z) {
      // rotate around Y then X
      var cy = Math.cos(rot.y + idle), sy = Math.sin(rot.y + idle);
      var x1 = x * cy - z * sy, z1 = x * sy + z * cy;
      var cx = Math.cos(rot.x), sx = Math.sin(rot.x);
      var y1 = y * cx - z1 * sx, z2 = y * sx + z1 * cx;
      return [size / 2 + x1 * R, size / 2 - y1 * R, z2];
    }
    function draw() {
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, size, size);
      // sphere body
      ctx.fillStyle = 'rgba(244,239,231,0.95)';   // flat fill: the site uses no colour blends ctx.beginPath(); ctx.arc(size / 2, size / 2, R, 0, 6.283); ctx.fill();
      ctx.strokeStyle = 'rgba(23,56,14,0.10)'; ctx.lineWidth = 1; ctx.stroke();
      // graticule (a few latitude rings)
      ctx.strokeStyle = 'rgba(23,56,14,0.06)';
      for (var lat = -60; lat <= 60; lat += 30) {
        ctx.beginPath(); var first = true;
        for (var lon = -180; lon <= 180; lon += 6) {
          var q = toXYZ(lat, lon), s = project(q[0], q[1], q[2]);
          if (s[2] < 0) { first = true; continue; }
          if (first) { ctx.moveTo(s[0], s[1]); first = false; } else ctx.lineTo(s[0], s[1]);
        }
        ctx.stroke();
      }
      // land dots
      for (var i = 0; i < pts.length; i += 3) {
        var s2 = project(pts[i], pts[i + 1], pts[i + 2]);
        if (s2[2] < -0.02) continue;
        var a = 0.25 + 0.75 * Math.max(0, s2[2]);
        ctx.fillStyle = 'rgba(23,56,14,' + (a * 0.85).toFixed(3) + ')';
        ctx.beginPath(); ctx.arc(s2[0], s2[1], (1.1 + 1.3 * s2[2]) * (size / 640), 0, 6.283); ctx.fill();
      }
      // pins
      var t = performance.now() / 1000;
      pinsXYZ.forEach(function (p, k) {
        var s3 = project(p[0], p[1], p[2]);
        if (s3[2] < 0.05) return;
        var pulse = (Math.sin(t * 2 + k) + 1) / 2;
        ctx.fillStyle = 'rgba(235,100,34,' + (0.12 + 0.18 * pulse) + ')';
        ctx.beginPath(); ctx.arc(s3[0], s3[1], (6 + 8 * pulse) * (size / 640), 0, 6.283); ctx.fill();
        ctx.fillStyle = '#eb6422';
        ctx.beginPath(); ctx.arc(s3[0], s3[1], 3.2 * (size / 640), 0, 6.283); ctx.fill();
      });
      // arcs from Singapore (global office) to a few regions
      var sg = pinsXYZ[0];
      [4, 9, 11, 14, 17, 7].forEach(function (k) {
        var to = pinsXYZ[k]; if (!to) return;
        var a = project(sg[0], sg[1], sg[2]), b = project(to[0], to[1], to[2]);
        if (a[2] < 0 || b[2] < 0) return;
        var mx = (sg[0] + to[0]) / 2, my = (sg[1] + to[1]) / 2, mz = (sg[2] + to[2]) / 2;
        var ml = Math.sqrt(mx * mx + my * my + mz * mz) || 1; var lift = 1.25;
        var m = project(mx / ml * lift, my / ml * lift, mz / ml * lift);
        ctx.strokeStyle = 'rgba(235,100,34,0.45)'; ctx.lineWidth = 1.2 * (size / 640);
        ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.quadraticCurveTo(m[0], m[1], b[0], b[1]); ctx.stroke();
      });
    }
    resize(); win.addEventListener('resize', function () { resize(); draw(); });
    draw();
    if (staticOnly) return;
    // idle spin + scroll-driven full rotation over the hero
    var hero = canvas.closest('.globe-hero') || canvas.parentElement;
    gsap.to(rot, { y: rot.y + Math.PI * 2, ease: 'none', scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: 0.6 } });
    gsap.from(canvas, { scale: .8, opacity: 0, duration: 1.4, ease: 'power3.out' });
    gsap.ticker.add(function (time, dt) { idle += dt * 0.00008; draw(); });
  }

  /* ============================================================
     About hero video — the globe turns once over a single scroll.
     The hero is pinned for one viewport of scrolling and the video's
     currentTime is tied to scroll progress (video is encoded with a
     keyframe on every frame so seeking is instant).
     ============================================================ */
  function initHeroVideo(staticOnly) {
    var video = doc.querySelector('.globe-video__el');
    if (!video) return;
    var hero = video.closest('.globe-hero');
    var lead = hero.querySelector('.globe-hero__lead');
    var stats = hero.querySelectorAll('.globe-stats--reveal .stat');
    var hint = hero.querySelector('.globe-hint');
    function showStatsNow() {
      stats.forEach(function (st) { st.style.opacity = 1; st.style.transform = 'none'; var n = st.querySelector('[data-count]'); if (n) n.textContent = parseFloat(n.dataset.count).toLocaleString(); });
    }
    if (staticOnly || win.matchMedia('(max-width: 960px)').matches) {
      video.loop = true; video.autoplay = true; video.play().catch(function () {}); showStatsNow(); return;
    }
    doc.documentElement.classList.add('js-motion');

    // The hero stays put while the page is scrolled through it: the scroll position drives the globe's
    // spin frame by frame, the subheading gives way to the counters, then the page carries on down.
    // Scrolling back up runs it all in reverse.
    var dur = 6, last = -1;
    video.pause(); video.currentTime = 0;
    var vs = { t: 0 };
    function seek() {
      var t = Math.min(dur - 0.03, vs.t * dur);
      if (Math.abs(t - last) < 1 / 30) return;
      last = t; try { video.currentTime = t; } catch (e) {}
    }
    video.addEventListener('loadedmetadata', function () { dur = video.duration || 6; seek(); });

    doc.documentElement.classList.add('hero-pinned');   // the next section rides up over the held hero
    var tl = gsap.timeline({ paused: true });
    tl.to(vs, { t: 1, duration: 1, ease: 'none', onUpdate: seek }, 0);
    tl.to({}, { duration: .625 }, 1);                       // hold the last frame while the page covers it
    if (hint) tl.to(hint, { opacity: 0, duration: .08 }, 0);
    tl.to(lead, { opacity: 0, y: -14, duration: .18, ease: 'power2.in' }, 0.02);
    stats.forEach(function (st, i) {
      var num = st.querySelector('[data-count]'); var target = num ? parseFloat(num.dataset.count) : 0; var obj = { v: 0 };
      var at = 0.3 + i * 0.1;
      tl.to(st, { opacity: 1, y: 0, duration: .22, ease: 'power3.out' }, at);
      if (num) tl.to(obj, { v: target, duration: .3, ease: 'power2.out', onUpdate: function () { num.textContent = Math.round(obj.v).toLocaleString(); } }, at);
    });

    var cover = doc.querySelector('.about-cover');
    ScrollTrigger.create({
      trigger: hero, start: 'top top', end: '+=260%', pin: true, pinSpacing: false, scrub: 0.6, animation: tl, anticipatePin: 1
    });
    if (cover && header) {                                           // once it has risen, the Vision / Mission / Approach section holds under the compact header
      var hdrH = function () { var had = header.classList.contains('is-scrolled'); header.classList.add('is-scrolled'); var h = header.offsetHeight; if (!had) header.classList.remove('is-scrolled'); return h; };
      ScrollTrigger.create({
        trigger: cover, start: function () { return 'top ' + hdrH(); }, end: '+=90%', pin: true, pinSpacing: true, anticipatePin: 1,
        onToggle: function (st) { doc.documentElement.classList.toggle('keep-header', st.isActive); if (st.isActive) { header.classList.add('is-scrolled'); header.classList.remove('is-hidden'); } }
      });
    }
    video.load();
  }

  function initJourney(staticOnly) {
    doc.querySelectorAll('.journey').forEach(function (root) {
      var svg = root.querySelector('svg.journey__svg'), list = root.querySelector('.journey__list');
      if (!svg || !list) return;
      var items = list.querySelectorAll('.milestone');
      var track = svg.querySelector('.track'), draw = svg.querySelector('.draw'), dot = svg.querySelector('.dot'), halo = svg.querySelector('.halo');
      function build() {
        var H = root.getBoundingClientRect().height, W = root.getBoundingClientRect().width;
        var mobile = win.matchMedia('(max-width: 860px)').matches;
        svg.setAttribute('viewBox', '0 0 ' + (mobile ? 40 : W) + ' ' + H);
        svg.setAttribute('preserveAspectRatio', 'none');
        var d = '';
        if (mobile) {
          d = 'M20 0 V' + H;
        } else {
          // winding curve through each milestone card's centre, alternating sides
          var cx = W / 2, amp = Math.min(W * 0.22, 260);
          d = 'M' + cx + ' 0';
          var prevY = 0, prevX = cx;
          items.forEach(function (it, i) {
            var r = it.getBoundingClientRect(), rr = root.getBoundingClientRect();
            var y = r.top - rr.top + r.height / 2;
            var x = cx + (i % 2 === 0 ? -amp : amp);
            var c1y = prevY + (y - prevY) * 0.5, c2y = y - (y - prevY) * 0.5;
            d += ' C' + prevX + ' ' + c1y + ', ' + x + ' ' + c2y + ', ' + x + ' ' + y;
            prevY = y; prevX = x;
          });
          d += ' C' + prevX + ' ' + (prevY + (H - prevY) * 0.5) + ', ' + cx + ' ' + (H - (H - prevY) * 0.5) + ', ' + cx + ' ' + H;
        }
        track.setAttribute('d', d); draw.setAttribute('d', d);
        var len = draw.getTotalLength();
        draw.style.strokeDasharray = len; draw.style.strokeDashoffset = len;
        return len;
      }
      var len = build();
      var state = { p: staticOnly ? 1 : 0 };
      function place() {
        var pt = draw.getPointAtLength(state.p * len);
        dot.setAttribute('cx', pt.x); dot.setAttribute('cy', pt.y); halo.setAttribute('cx', pt.x); halo.setAttribute('cy', pt.y);
        draw.style.strokeDashoffset = len * (1 - state.p);
      }
      place();
      if (staticOnly) return;
      gsap.to(state, { p: 1, ease: 'none', onUpdate: place, scrollTrigger: { trigger: root, start: 'top 70%', end: 'bottom 60%', scrub: 0.8 } });
      items.forEach(function (it, i) {
        gsap.from(it.querySelector('.milestone__card'), { opacity: 0, x: i % 2 === 0 ? -40 : 40, duration: .9, ease: 'power3.out', scrollTrigger: { trigger: it, start: 'top 80%', once: true } });
      });
      ScrollTrigger.addEventListener('refreshInit', function () { len = build(); place(); });
      win.addEventListener('load', function () { ScrollTrigger.refresh(); });
    });
  }
})();
