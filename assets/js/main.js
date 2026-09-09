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

  /* ---------- header: shrink + hide on scroll down ---------- */
  var header = doc.querySelector('.site-header');
  var lastY = 0;
  function onScroll() {
    var y = win.scrollY;
    if (!header) return;
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

  /* ---------- marquee: duplicate track content for seamless loop ---------- */
  doc.querySelectorAll('.marquee__track').forEach(function (t) { t.innerHTML += t.innerHTML; });

  if (reduce || !hasGsap) {
    doc.querySelectorAll('[data-reveal]').forEach(function (el) { el.style.opacity = 1; el.style.transform = 'none'; });
    doc.querySelectorAll('[data-count]').forEach(function (el) { el.textContent = parseFloat(el.dataset.count).toLocaleString() + (el.dataset.suffix || ''); });
    initFaculty(); initGlobe(true); initJourney(true); initHeroVideo(true); initHomeHero(true); return;
  }

  /* ---------- split headline into rising words ---------- */
  doc.querySelectorAll('[data-split], .hv__title').forEach(function (el) {
    var nodes = Array.prototype.slice.call(el.childNodes), out = '';
    nodes.forEach(function (n) {
      if (n.nodeType === 3) {
        out += n.textContent.split(/(\s+)/).map(function (w) {
          return /^\s+$/.test(w) ? ' ' : (w ? '<span class="split-word"><span>' + w + '</span></span>' : '');
        }).join('');
      } else if (n.nodeType === 1) {
        var tag = n.tagName.toLowerCase();
        out += '<' + tag + (n.className ? ' class="' + n.className + '"' : '') + '>' +
          n.textContent.split(/(\s+)/).map(function (w) { return /^\s+$/.test(w) ? ' ' : (w ? '<span class="split-word"><span>' + w + '</span></span>' : ''); }).join('') + '</' + tag + '>';
      }
    });
    el.innerHTML = out;
    gsap.from(el.querySelectorAll('.split-word > span'), { yPercent: 115, duration: 1.1, ease: 'power4.out', stagger: 0.045, delay: 0.1 });
  });

  /* ---------- scroll reveals ---------- */
  ScrollTrigger.batch('[data-reveal]', {
    start: 'top 90%',
    once: true,
    onEnter: function (els) {
      gsap.to(els, { opacity: 1, x: 0, y: 0, scale: 1, duration: 0.9, ease: 'power3.out', stagger: 0.08, overwrite: true, clearProps: 'transform' });
    }
  });

  /* ---------- counters ---------- */
  doc.querySelectorAll('[data-count]').forEach(function (el) {
    if (el.closest('.globe-stats--reveal')) return;
    var target = parseFloat(el.dataset.count), suffix = el.dataset.suffix || '';
    var obj = { v: 0 };
    ScrollTrigger.create({
      trigger: el, start: 'top 88%', once: true,
      onEnter: function () {
        gsap.to(obj, { v: target, duration: 1.8, ease: 'power2.out', onUpdate: function () { el.textContent = Math.round(obj.v).toLocaleString() + suffix; } });
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

  /* ---------- cursor glow (desktop) ---------- */
  if (win.matchMedia('(pointer:fine)').matches) {
    var glow = doc.createElement('div'); glow.className = 'cursor-glow'; doc.body.appendChild(glow);
    var qx = gsap.quickTo(glow, 'x', { duration: .6, ease: 'power3' }), qy = gsap.quickTo(glow, 'y', { duration: .6, ease: 'power3' });
    win.addEventListener('mousemove', function (e) { glow.style.opacity = 1; qx(e.clientX); qy(e.clientY); }, { passive: true });
  }

  initFaculty();
  initGlobe(false);
  initJourney();
  initHeroVideo();
  initHomeHero(false);
  initStrips();
  win.addEventListener('load', function () { ScrollTrigger.refresh(); });
  // safety net: anything still hidden 4s after load is shown (e.g. if ScrollTrigger never fires)
  setTimeout(function () { doc.querySelectorAll('[data-reveal]').forEach(function (el) { if (el.closest('.globe-hero')) return; if (getComputedStyle(el).opacity === '0' && el.getBoundingClientRect().top < win.innerHeight) gsap.to(el, { opacity: 1, x: 0, y: 0, scale: 1, duration: .6 }); }); }, 4000);

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
      var g = ctx.createRadialGradient(size * 0.38, size * 0.36, R * 0.1, size / 2, size / 2, R);
      g.addColorStop(0, 'rgba(255,255,255,0.9)'); g.addColorStop(1, 'rgba(244,239,231,0.95)');
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(size / 2, size / 2, R, 0, 6.283); ctx.fill();
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
    if (staticOnly || win.matchMedia('(max-width: 960px)').matches || win.scrollY > 40 || location.hash) {
      video.loop = true; video.autoplay = true; video.play().catch(function () {}); showStatsNow(); return;
    }
    doc.documentElement.classList.add('js-motion');

    // Enter on the first frame with only the headline. One scroll runs the globe to the end in ~3s
    // while the headline gives way to the counters. Scrolling back up runs the whole thing in reverse.
    var html = doc.documentElement, locked = true, dur = 6, TOTAL = 3;
    html.classList.add('is-locked');
    win.scrollTo(0, 0);
    video.pause(); video.currentTime = 0;
    var vs = { t: 0 };
    function seek() { if (dur) video.currentTime = Math.min(dur - 0.03, vs.t * dur); }
    video.addEventListener('loadedmetadata', function () { dur = video.duration || 6; seek(); });

    function release() { locked = false; html.classList.remove('is-locked'); if (hint) hint.classList.add('is-done'); ScrollTrigger.refresh(); }
    function relock() { locked = true; html.classList.add('is-locked'); win.scrollTo(0, 0); if (hint) hint.classList.remove('is-done', 'is-playing'); }

    var tl = gsap.timeline({ paused: true, onComplete: release, onReverseComplete: relock });
    tl.to(vs, { t: 1, duration: TOTAL, ease: 'none', onUpdate: seek }, 0)
      .to(lead, { opacity: 0, y: -16, duration: .4, ease: 'power2.in' }, 0);
    stats.forEach(function (st, i) {
      var num = st.querySelector('[data-count]'); var target = num ? parseFloat(num.dataset.count) : 0; var obj = { v: 0 };
      var at = 0.7 + i * ((TOTAL - 0.7 - 0.8) / stats.length);
      tl.to(st, { opacity: 1, y: 0, duration: .6, ease: 'power3.out' }, at);
      if (num) tl.to(obj, { v: target, duration: .8, ease: 'power2.out', onUpdate: function () { num.textContent = Math.round(obj.v).toLocaleString(); } }, at);
    });

    function forward() { if (hint) hint.classList.add('is-playing'); tl.play(); }
    function backward() { if (hint) hint.classList.remove('is-playing'); tl.reverse(); }
    function onWheel(e) {
      if (locked) { e.preventDefault(); if (e.deltaY > 0) forward(); else if (e.deltaY < 0) backward(); return; }
      if (win.scrollY <= 0 && e.deltaY < 0) { e.preventDefault(); relock(); backward(); }
    }
    function onKey(e) {
      if (locked && /^(ArrowDown|PageDown|Space| )$/.test(e.key)) { e.preventDefault(); forward(); }
      else if (locked && /^(ArrowUp|PageUp)$/.test(e.key)) { e.preventDefault(); backward(); }
      else if (!locked && win.scrollY <= 0 && /^(ArrowUp|PageUp)$/.test(e.key)) { e.preventDefault(); relock(); backward(); }
    }
    var touchY = null;
    function onTouchStart(e) { touchY = e.touches[0].clientY; }
    function onTouchMove(e) {
      if (touchY === null) return;
      var dy = touchY - e.touches[0].clientY;
      if (locked) { e.preventDefault(); if (dy > 8) forward(); else if (dy < -8) backward(); }
      else if (win.scrollY <= 0 && dy < -8) { e.preventDefault(); relock(); backward(); }
    }
    win.addEventListener('wheel', onWheel, { passive: false });
    win.addEventListener('keydown', onKey);
    win.addEventListener('touchstart', onTouchStart, { passive: true });
    win.addEventListener('touchmove', onTouchMove, { passive: false });
    video.load();
  }

  /* ============================================================
     Journey — S-curve path drawn as you scroll, dot travels along
     ============================================================ */
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
