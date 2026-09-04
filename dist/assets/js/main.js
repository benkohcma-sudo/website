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

  /* ---------- marquee: duplicate track content for seamless loop ---------- */
  doc.querySelectorAll('.marquee__track').forEach(function (t) { t.innerHTML += t.innerHTML; });

  if (reduce || !hasGsap) {
    doc.querySelectorAll('[data-reveal]').forEach(function (el) { el.style.opacity = 1; el.style.transform = 'none'; });
    doc.querySelectorAll('[data-count]').forEach(function (el) { el.textContent = parseFloat(el.dataset.count).toLocaleString() + (el.dataset.suffix || ''); });
    initFaculty(); initGlobe(true); initJourney(true); initHeroVideo(true); return;
  }

  /* ---------- split headline into rising words ---------- */
  doc.querySelectorAll('[data-split]').forEach(function (el) {
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
  win.addEventListener('load', function () { ScrollTrigger.refresh(); });
  // safety net: anything still hidden 4s after load is shown (e.g. if ScrollTrigger never fires)
  setTimeout(function () { doc.querySelectorAll('[data-reveal]').forEach(function (el) { if (getComputedStyle(el).opacity === '0' && el.getBoundingClientRect().top < win.innerHeight) gsap.to(el, { opacity: 1, x: 0, y: 0, scale: 1, duration: .6 }); }); }, 4000);

  /* ============================================================
     Faculty carousel — tabs + horizontal snap track + counter
     ============================================================ */
  function initFaculty() {
    doc.querySelectorAll('.faculty').forEach(function (root) {
      var tabs = root.querySelectorAll('.tabs button');
      var groups = root.querySelectorAll('.faculty__track');
      var prev = root.querySelector('[data-prev]'), next = root.querySelector('[data-next]');
      var counter = root.querySelector('.counter'), bar = root.querySelector('.bar i');
      var active = null;
      function show(i) {
        tabs.forEach(function (b, j) { b.classList.toggle('is-active', j === i); });
        groups.forEach(function (g, j) { g.hidden = j !== i; });
        active = groups[i]; active.scrollTo({ left: 0 }); update();
        if (hasGsap && !reduce) gsap.from(active.children, { opacity: 0, y: 24, duration: .7, stagger: .06, ease: 'power3.out', clearProps: 'all' });
      }
      function cardW() { var c = active.children[1] || active.children[0]; return c ? c.getBoundingClientRect().width + 24 : 300; }
      function update() {
        if (!active) return;
        var n = active.children.length;
        var idx = Math.min(n, Math.round(active.scrollLeft / cardW()) + 1);
        if (counter) counter.innerHTML = String(idx).padStart(2, '0') + ' <span>/ ' + String(n).padStart(2, '0') + '</span>';
        if (bar) { bar.style.width = (100 / n) + '%'; bar.style.left = ((idx - 1) * 100 / n) + '%'; }
      }
      tabs.forEach(function (b, i) { b.addEventListener('click', function () { show(i); }); });
      groups.forEach(function (g) { g.addEventListener('scroll', update, { passive: true }); });
      if (prev) prev.addEventListener('click', function () { active.scrollBy({ left: -cardW(), behavior: 'smooth' }); });
      if (next) next.addEventListener('click', function () { active.scrollBy({ left: cardW(), behavior: 'smooth' }); });
      if (groups.length) show(0);
      // dotted world map behind the stage
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
    if (staticOnly || win.matchMedia('(max-width: 960px)').matches) { video.loop = true; video.autoplay = true; video.play().catch(function () {}); return; }
    var state = { t: 0 }, dur = 0;
    function seek() { if (dur) video.currentTime = Math.min(dur - 0.05, state.t * dur); }
    function ready() { dur = video.duration || 6; seek(); }
    if (video.readyState >= 1) ready(); else video.addEventListener('loadedmetadata', ready);
    video.load();
    gsap.to(state, {
      t: 1, ease: 'none', onUpdate: seek,
      scrollTrigger: { trigger: hero, start: 'top top', end: '+=120%', scrub: 0.5, pin: true, anticipatePin: 1 }
    });
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
