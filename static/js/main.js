(function () {
  'use strict';

  const isTouchDevice =
    'ontouchstart' in window ||
    navigator.maxTouchPoints > 0 ||
    navigator.msMaxTouchPoints > 0;

  function debounce(func, wait = 15) {
    let timeout;
    return function (...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func(...args), wait);
    };
  }

  function throttle(func, limit = 100) {
    let inThrottle;
    return function (...args) {
      if (!inThrottle) {
        func.apply(this, args);
        inThrottle = true;
        setTimeout(() => (inThrottle = false), limit);
      }
    };
  }

  function qs(selector, parent = document) {
    return parent.querySelector(selector);
  }

  function qsAll(selector, parent = document) {
    return parent.querySelectorAll(selector);
  }

  /* ── Smooth scroll ── */
  function initSmoothScroll() {
    const navLinks = qsAll('.nav-links a[href^="#"]');
    const navbar   = qs('.navbar');
    if (!navLinks.length) return;

    navLinks.forEach(link => {
      link.addEventListener('click', function (e) {
        const href   = this.getAttribute('href');
        const target = href && href !== '#' ? qs(href) : null;
        if (!target) return;

        e.preventDefault();

        const offset = (navbar ? navbar.offsetHeight : 0) + (window.innerWidth <= 768 ? 12 : 4);
        const top    = target.getBoundingClientRect().top + window.scrollY - offset;

        window.scrollTo({ top, behavior: 'smooth' });

        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
      });
    });
  }

  /* ── Section fade-in ── */
  function initScrollAnimations() {
    const els = qsAll('.section-animate');
    if (!els.length) return;

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    els.forEach(el => observer.observe(el));
  }

  /* ── Staggered card animations ── */
  function initCardStagger() {
    const SELECTORS = '.skills-grid, .projects-grid, .clients-grid, .cert-grid';
    const grids = qsAll(SELECTORS);

    grids.forEach(grid => {
      const cards = qsAll('.card, .client-card, .cert-card', grid);

      cards.forEach((card, i) => {
        card.style.opacity   = '0';
        card.style.transform = 'translateY(22px)';
        card.style.transition = `opacity 0.48s ease ${i * 0.07}s, transform 0.48s ease ${i * 0.07}s`;
      });

      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            qsAll('.card, .client-card, .cert-card', entry.target).forEach(card => {
              card.style.opacity   = '1';
              card.style.transform = 'translateY(0)';
            });
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.08 });

      observer.observe(grid);
    });
  }

  /* ── Cursor glow ── */
  function initCursorGlow() {
    if (isTouchDevice) return;

    const glow = document.createElement('div');
    glow.className = 'cursor-glow';
    document.body.appendChild(glow);

    document.addEventListener('mousemove', throttle(e => {
      glow.style.left = e.clientX + 'px';
      glow.style.top  = e.clientY + 'px';
    }, 16), { passive: true });
  }

  /* ── Scroll progress bar ── */
  function initScrollProgress() {
    const bar = document.createElement('div');
    bar.id = 'scroll-progress-bar';
    Object.assign(bar.style, {
      position:       'fixed',
      top:            '0',
      left:           '0',
      height:         '2px',
      width:          '0%',
      background:     'linear-gradient(90deg, #4f7fff, #8b7cf8)',
      zIndex:         '60',
      pointerEvents:  'none',
      transition:     'width 0.1s ease-out',
    });
    document.body.appendChild(bar);

    const update = throttle(() => {
      const scrollTop  = window.scrollY;
      const docHeight  = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      bar.style.width  = docHeight > 0 ? Math.min((scrollTop / docHeight) * 100, 100) + '%' : '0%';
    }, 50);

    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', debounce(update, 100), { passive: true });
    update();
  }

  /* ── Language toggle ── */
  function initLanguageToggle() {
    const langToggle = qs('#langToggle');
    const langBtns   = qsAll('.lang-btn');
    const body       = document.body;
    if (!langToggle || !langBtns.length) return;

    const saved = localStorage.getItem('preferredLanguage') || 'id';
    body.setAttribute('data-lang', saved);
    langBtns.forEach(btn => {
      if (btn.getAttribute('data-lang') === saved) btn.classList.add('active');
    });

    langToggle.addEventListener('click', e => {
      const btn  = e.target.closest('.lang-btn');
      if (!btn) return;
      const lang = btn.getAttribute('data-lang') || 'id';
      body.setAttribute('data-lang', lang);
      langBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      try { localStorage.setItem('preferredLanguage', lang); } catch (_) {}
    });
  }

  /* ── Active nav highlight on scroll ── */
  function initActiveSectionHighlight() {
    const sections = qsAll('section[id]');
    const navLinks = qsAll('.nav-links a[href^="#"]');
    if (!sections.length || !navLinks.length) return;

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          navLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
          });
        }
      });
    }, { threshold: 0.25, rootMargin: '-20% 0px -70% 0px' });

    sections.forEach(s => observer.observe(s));
  }

  /* ── Parallax hero avatar ── */
  function initParallax() {
    const heroAvatar = qs('.hero-avatar');
    if (!heroAvatar || isTouchDevice) return;

    window.addEventListener('scroll', debounce(() => {
      heroAvatar.style.transform = `translateY(${window.scrollY * 0.04}px)`;
    }, 10), { passive: true });
  }

  /* ── 3D tilt on avatar card ── */
  function init3DTilt() {
    const frame = qs('.avatar-frame');
    if (!frame || isTouchDevice) return;

    let hovering = false;

    frame.addEventListener('mouseenter', () => { hovering = true; });

    frame.addEventListener('mousemove', e => {
      if (!hovering) return;
      const rect   = frame.getBoundingClientRect();
      const x      = (e.clientX - rect.left) / rect.width;
      const y      = (e.clientY - rect.top)  / rect.height;
      const rotX   = ((y - 0.5) *  10).toFixed(2);
      const rotY   = ((x - 0.5) * -10).toFixed(2);
      frame.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale3d(1.015,1.015,1.015)`;
    });

    frame.addEventListener('mouseleave', () => {
      hovering = false;
      frame.style.transition = 'transform 0.5s ease';
      frame.style.transform  = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)';
      setTimeout(() => { frame.style.transition = ''; }, 500);
    });
  }

  /* ── Keyboard nav ── */
  function initKeyboardNav() {
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') document.body.classList.remove('nav-open');
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const first = qs('.nav-links a');
        if (first) first.focus();
      }
    });
  }

  /* ── Reduced motion ── */
  function initReducedMotion() {
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    document.documentElement.style.scrollBehavior = 'auto';
    const style = document.createElement('style');
    style.textContent = `
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    `;
    document.head.appendChild(style);
  }

  /* ── Boot ── */
  function init() {
    initSmoothScroll();
    initScrollAnimations();
    initCardStagger();
    initCursorGlow();
    initScrollProgress();
    initLanguageToggle();
    initParallax();
    init3DTilt();
    initActiveSectionHighlight();
    initKeyboardNav();
    initReducedMotion();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
