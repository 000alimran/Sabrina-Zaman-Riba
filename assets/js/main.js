/* Sabrina Zaman Riba — site behaviour & interactions
   Open-source stack: GSAP + ScrollTrigger + Flip (gsap.com, free),
   Lenis (darkroom.engineering), SplitType, GLightbox — all vendored. */

(function () {
  'use strict';

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasGsap = typeof gsap !== 'undefined';
  if (hasGsap && typeof ScrollTrigger !== 'undefined') gsap.registerPlugin(ScrollTrigger, typeof Flip !== 'undefined' ? Flip : undefined);

  /* ── Year ─────────────────────────────────────────────── */
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ── Mobile nav ───────────────────────────────────────── */
  const navToggle = document.getElementById('navToggle');
  const siteNav = document.getElementById('siteNav');
  if (navToggle && siteNav) {
    navToggle.addEventListener('click', () => {
      const open = siteNav.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(open));
    });
    siteNav.addEventListener('click', (e) => {
      if (e.target.tagName === 'A') {
        siteNav.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ── Smooth scroll (Lenis) ────────────────────────────── */
  let lenis = null;
  if (!reduced && typeof Lenis !== 'undefined') {
    lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    function raf(t) { lenis.raf(t); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
    if (hasGsap) lenis.on('scroll', ScrollTrigger.update);
    // in-page anchors through lenis
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
      a.addEventListener('click', (e) => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) { e.preventDefault(); lenis.scrollTo(target, { offset: -70 }); }
      });
    });
  }

  /* ── Hide-on-scroll pill nav ──────────────────────────── */
  const navWrap = document.querySelector('.nav-wrap');
  if (navWrap && hasGsap && !reduced) {
    let lastY = 0;
    ScrollTrigger.create({
      start: 0, end: 'max',
      onUpdate(self) {
        const y = self.scroll();
        const goingDown = y > lastY && y > 300;
        gsap.to(navWrap, { yPercent: goingDown ? -130 : 0, duration: 0.35, ease: 'power2.out', overwrite: 'auto' });
        lastY = y;
      }
    });
  }

  /* ── Headline split & rise ────────────────────────────── */
  if (hasGsap && !reduced && typeof SplitType !== 'undefined') {
    document.querySelectorAll('[data-split]').forEach((el) => {
      const split = new SplitType(el, { types: 'lines,words' });
      gsap.from(split.words, {
        yPercent: 115, duration: 0.9, ease: 'power4.out',
        stagger: 0.045, delay: 0.1
      });
    });
  }

  /* ── Scroll reveals (auto-tagged) ─────────────────────── */
  if (hasGsap && !reduced) {
    const targets = document.querySelectorAll(
      '.section-head, .section-intro, .work-item, .svc-grid li, .steps li, ' +
      '.camp-list li, .press-list li, .story, .pull-quote, .cta-band, ' +
      '.about-copy, .about-portrait, .fact-list, .comp-toggle, .comp-grid > div, ' +
      '.num-grid > div, .platform-rows li, .faq-list details, .timeline li, ' +
      '.booking-copy, .booking-form, .hero-stats > div, .tile-row a'
    );
    targets.forEach((el) => {
      gsap.fromTo(el, { y: 26, opacity: 0 }, {
        y: 0, opacity: 1, duration: 0.8, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 88%', once: true }
      });
    });

    /* subtle parallax on tagged figures & hero cards */
    document.querySelectorAll('[data-parallax], .hero-card').forEach((el, i) => {
      gsap.to(el, {
        yPercent: (i % 2 ? -6 : 6), ease: 'none',
        scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: 0.6 }
      });
    });
  }

  /* ── Stat counters ────────────────────────────────────── */
  if (hasGsap && !reduced) {
    document.querySelectorAll('[data-count]').forEach((el) => {
      const target = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      const decimals = (el.dataset.count.split('.')[1] || '').length;
      const obj = { v: 0 };
      gsap.to(obj, {
        v: target, duration: 1.6, ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 88%', once: true },
        onUpdate() {
          el.textContent = obj.v.toLocaleString('en-US', {
            minimumFractionDigits: decimals, maximumFractionDigits: decimals
          }) + suffix;
        }
      });
    });
  }

  /* ── Magnetic buttons ─────────────────────────────────── */
  if (hasGsap && !reduced && matchMedia('(hover:hover) and (pointer:fine)').matches) {
    document.querySelectorAll('.btn').forEach((btn) => {
      const strength = 18;
      btn.addEventListener('mousemove', (e) => {
        const r = btn.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width / 2) / (r.width / 2);
        const y = (e.clientY - r.top - r.height / 2) / (r.height / 2);
        gsap.to(btn, { x: x * strength, y: y * strength * 0.6, duration: 0.3, ease: 'power2.out' });
      });
      btn.addEventListener('mouseleave', () => {
        gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1,0.4)' });
      });
    });
  }

  /* ── Work filters (FLIP transitions) ──────────────────── */
  const filters = document.querySelectorAll('.filter');
  const grid = document.getElementById('workGrid');
  const empty = document.getElementById('workEmpty');
  function applyFilter(cat) {
    if (!grid) return;
    const items = grid.querySelectorAll('.work-item');
    filters.forEach((b) => b.classList.toggle('is-active', b.dataset.filter === cat));
    const doFlip = hasGsap && !reduced && typeof Flip !== 'undefined';
    const state = doFlip ? Flip.getState(items) : null;
    let shown = 0;
    items.forEach((item) => {
      const show = cat === 'all' || item.dataset.cat === cat;
      item.hidden = !show;
      if (show) shown++;
    });
    if (empty) empty.hidden = shown > 0;
    if (doFlip) {
      Flip.from(state, {
        duration: 0.55, ease: 'power3.inOut', stagger: 0.02,
        absolute: true, onEnter: (els) => gsap.fromTo(els, { opacity: 0, scale: 0.92 }, { opacity: 1, scale: 1, duration: 0.4 }),
        onLeave: (els) => gsap.to(els, { opacity: 0, scale: 0.92, duration: 0.3 })
      });
      ScrollTrigger.refresh();
    }
  }
  filters.forEach((btn) => btn.addEventListener('click', () => applyFilter(btn.dataset.filter)));
  document.querySelectorAll('[data-cat-link]').forEach((tile) => {
    tile.addEventListener('click', () => applyFilter(tile.dataset.catLink));
  });

  /* ── Lightbox ─────────────────────────────────────────── */
  if (typeof GLightbox !== 'undefined') {
    // work.html: anchor-based gallery
    if (document.querySelector('.glightbox')) {
      GLightbox({ selector: '.glightbox', touchNavigation: true, loop: true });
    }
    // home: open grid images in a lightbox without anchors
    const homeFrames = document.querySelectorAll('.gl-home img');
    if (homeFrames.length) {
      const elements = [...homeFrames].map((img) => ({ href: img.src, type: 'image' }));
      const gl = GLightbox({ elements, touchNavigation: true, loop: true });
      homeFrames.forEach((img, i) => {
        img.closest('.work-frame').style.cursor = 'zoom-in';
        img.addEventListener('click', () => gl.openAt(i));
      });
    }
  }

  /* ── Booking form → mail app ──────────────────────────── */
  const form = document.getElementById('bookingForm');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const subject = encodeURIComponent(
        'Booking enquiry — ' + data.get('type') + ' (' + (data.get('brand') || data.get('name')) + ')'
      );
      const body = encodeURIComponent(
        'Name: ' + data.get('name') + '\nBrand: ' + (data.get('brand') || '—') +
        '\nWork type: ' + data.get('type') + '\n\n' + data.get('message')
      );
      // TODO: replace with Riba's real booking address
      window.location.href = 'mailto:booking@sabrinazamanriba.com?subject=' + subject + '&body=' + body;
    });
  }
})();
