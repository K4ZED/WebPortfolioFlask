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

  function qs(selector, parent = document) { return parent.querySelector(selector); }
  function qsAll(selector, parent = document) { return parent.querySelectorAll(selector); }

  /* ── Smooth scroll ── */
  function initSmoothScroll() {
    const links  = qsAll('a.nav-link[href^="#"]');
    const navbar = qs('nav');
    if (!links.length) return;

    links.forEach(link => {
      link.addEventListener('click', function (e) {
        const href   = this.getAttribute('href');
        const target = href && href !== '#' ? qs(href) : null;
        if (!target) return;
        e.preventDefault();
        const offset = (navbar ? navbar.offsetHeight : 0) + 8;
        window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - offset, behavior: 'smooth' });
        links.forEach(l => l.classList.toggle('active', l.getAttribute('href') === href));
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
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    els.forEach(el => observer.observe(el));
  }

  /* ── Staggered card animations ── */
  function initCardStagger() {
    const grids = qsAll('.card-grid');
    grids.forEach(grid => {
      const cards = qsAll('.card', grid);
      cards.forEach((card, i) => {
        card.style.opacity   = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.45s ease ${i * 0.07}s, transform 0.45s ease ${i * 0.07}s`;
      });

      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            qsAll('.card', entry.target).forEach(card => {
              card.style.opacity   = '1';
              card.style.transform = 'translateY(0)';
            });
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.06 });

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
    const bar = qs('#scroll-progress-bar');
    if (!bar) return;
    const update = throttle(() => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      bar.style.width = docHeight > 0 ? Math.min((scrollTop / docHeight) * 100, 100) + '%' : '0%';
    }, 50);
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', debounce(update, 100), { passive: true });
    update();
  }

  /* ── Language toggle (handles both desktop + mobile toggles) ── */
  function initLanguageToggle() {
    const toggles = qsAll('#langToggle, #langToggleMobile');
    const body    = document.body;
    if (!toggles.length) return;

    const langBtns = () => {
      const btns = [];
      toggles.forEach(t => t.querySelectorAll('.lang-btn[data-lang]').forEach(b => btns.push(b)));
      return btns;
    };

    const saved = localStorage.getItem('preferredLanguage') || 'id';
    body.setAttribute('data-lang', saved);
    langBtns().forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === saved);
    });

    toggles.forEach(toggle => {
      toggle.addEventListener('click', e => {
        const btn  = e.target.closest('.lang-btn[data-lang]');
        if (!btn) return;
        const lang = btn.getAttribute('data-lang') || 'id';
        body.setAttribute('data-lang', lang);
        langBtns().forEach(b => b.classList.toggle('active', b.getAttribute('data-lang') === lang));
        try { localStorage.setItem('preferredLanguage', lang); } catch (_) {}
      });
    });
  }

  /* ── Active nav highlight on scroll ── */
  function initActiveSectionHighlight() {
    const sections = qsAll('section[id]');
    const navLinks = qsAll('a.nav-link[href^="#"]');
    if (!sections.length || !navLinks.length) return;

    const navbar = qs('nav');

    const update = throttle(() => {
      const offset = (navbar ? navbar.offsetHeight : 0) + 32;
      const scrollY = window.scrollY + offset;

      let current = sections[0].id;
      sections.forEach(section => {
        if (section.offsetTop <= scrollY) current = section.id;
      });

      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
      });
    }, 50);

    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ── Keyboard nav ── */
  function initKeyboardNav() {
    document.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const first = qs('a.nav-link');
        if (first) first.focus();
      }
    });
  }

  /* ── Reduced motion ── */
  function initReducedMotion() {
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    document.documentElement.style.scrollBehavior = 'auto';
    const style = document.createElement('style');
    style.textContent = `*, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }`;
    document.head.appendChild(style);
  }

  /* ── Mobile hamburger menu ── */
  function initMobileMenu() {
    const hamburger = qs('#navHamburger');
    const menu      = qs('#navMobile');
    if (!hamburger || !menu) return;

    const close = () => {
      menu.classList.remove('open');
      hamburger.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
    };

    hamburger.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('open');
      hamburger.classList.toggle('open', isOpen);
      hamburger.setAttribute('aria-expanded', String(isOpen));
    });

    qsAll('.nav-link, .btn-hire', menu).forEach(el => {
      el.addEventListener('click', close);
    });
  }

  /* ── Certificate modal ── */
  function initCertModal() {
    const modal    = qs('#certModal');
    const body     = qs('#certModalBody');
    const backdrop = qs('.cert-modal-backdrop');
    const closeBtn = qs('.cert-modal-close');
    if (!modal) return;

    document.addEventListener('click', e => {
      const trigger = e.target.closest('[data-cert]');
      if (!trigger) return;
      e.preventDefault();
      const src = trigger.dataset.cert;
      body.innerHTML = /\.(png|jpe?g|gif|webp)$/i.test(src)
        ? `<img src="${src}" alt="Certificate" />`
        : `<embed src="${src}#toolbar=0&navpanes=0" type="application/pdf" />`;
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });

    const close = () => {
      modal.classList.remove('open');
      document.body.style.overflow = '';
      setTimeout(() => { body.innerHTML = ''; }, 250);
    };

    backdrop.addEventListener('click', close);
    closeBtn.addEventListener('click', close);
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  /* ── Theme toggle (dark / light) ── */
  function initThemeToggle() {
    const toggles = qsAll('#themeToggle, #themeToggleMobile');
    const allBtns = qsAll('[data-theme-btn]');
    if (!toggles.length) return;

    const apply = theme => {
      document.documentElement.setAttribute('data-theme', theme);
      allBtns.forEach(b => b.classList.toggle('active', b.getAttribute('data-theme-btn') === theme));
      try { localStorage.setItem('preferredTheme', theme); } catch (_) {}
    };

    const saved = localStorage.getItem('preferredTheme') ||
      (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    apply(saved);

    toggles.forEach(toggle => {
      toggle.addEventListener('click', e => {
        const btn = e.target.closest('[data-theme-btn]');
        if (!btn) return;
        apply(btn.getAttribute('data-theme-btn'));
      });
    });
  }

  /* ── Hire Me button → scroll to #contact + activate Kontak nav ── */
  function initHireBtn() {
    const btn = qs('.btn-hire');
    if (!btn) return;
    const navbar = qs('nav');
    btn.addEventListener('click', function (e) {
      const target = qs('#contact');
      if (!target) return;
      e.preventDefault();
      const offset = (navbar ? navbar.offsetHeight : 0) + 8;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - offset, behavior: 'smooth' });
      qsAll('a.nav-link[href^="#"]').forEach(l =>
        l.classList.toggle('active', l.getAttribute('href') === '#contact')
      );
    });
  }

  /* ── Boot ── */
  function init() {
    initSmoothScroll();
    initScrollAnimations();
    initCardStagger();
    initCursorGlow();
    initScrollProgress();
    initLanguageToggle();
    initActiveSectionHighlight();
    initKeyboardNav();
    initReducedMotion();
    initMobileMenu();
    initThemeToggle();
    initHireBtn();
    initCertModal();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
