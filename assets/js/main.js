/* Animations: GSAP + ScrollTrigger. No jQuery. */
(function () {
  if (!window.gsap) return;
  gsap.registerPlugin(ScrollTrigger);

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;

  // Split hero title into words for a staggered rise
  document.querySelectorAll('[data-split]').forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.innerHTML = words.map(function (w) {
      return '<span class="word"><span>' + w + '</span></span>';
    }).join('');
    gsap.from(el.querySelectorAll('.word > span'), {
      yPercent: 110, duration: .9, ease: 'power4.out', stagger: .06, delay: .15
    });
  });

  // Generic reveal on scroll
  gsap.utils.toArray('[data-reveal]').forEach(function (el, i) {
    gsap.to(el, {
      opacity: 1, y: 0, duration: .8, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 88%', once: true },
      delay: (i % 4) * .08
    });
  });
})();
