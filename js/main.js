/**
 * Main Site JavaScript
 * Scroll animations, mobile menu, smooth interactions
 */

(function() {
  // Mobile menu toggle
  function initMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const nav = document.querySelector('nav');
    const navLinks = document.querySelectorAll('nav a');

    if (!menuBtn) return;

    menuBtn.addEventListener('click', () => {
      nav.classList.toggle('mobile-open');
      menuBtn.setAttribute('aria-expanded', nav.classList.contains('mobile-open'));
    });

    // Close menu when link clicked
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('mobile-open');
        menuBtn.setAttribute('aria-expanded', 'false');
      });
    });

    // Close menu on ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && nav.classList.contains('mobile-open')) {
        nav.classList.remove('mobile-open');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Scroll-triggered animations
  function initScrollAnimations() {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // Observe all elements with fade-in class
    document.querySelectorAll('.fade-in, .slide-up, .scale-in').forEach(el => {
      observer.observe(el);
    });
  }

  // Smooth scroll for anchor links
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(link => {
      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href === '#') return;

        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth' });
        }
      });
    });
  }

  // Table of contents — auto-generate from article h2s
  function initTableOfContents() {
    const toc = document.querySelector('.table-of-contents');
    if (!toc) return;

    const article = document.querySelector('article');
    if (!article) return;

    const headings = article.querySelectorAll('h2');
    if (headings.length === 0) {
      toc.style.display = 'none';
      return;
    }

    const list = document.createElement('ul');
    headings.forEach((heading, index) => {
      const id = heading.id || `section-${index}`;
      heading.id = id;

      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = `#${id}`;
      a.textContent = heading.textContent;
      li.appendChild(a);
      list.appendChild(li);
    });

    const container = toc.querySelector('ul') || toc;
    if (container.parentElement === toc) {
      container.replaceWith(list);
    } else {
      toc.appendChild(list);
    }
  }

  // Lazy load images with intersection observer
  function initLazyLoad() {
    const images = document.querySelectorAll('img[data-src]');
    if (images.length === 0) return;

    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      });
    });

    images.forEach(img => imageObserver.observe(img));
  }

  // Initialize all on DOM ready
  function init() {
    initMobileMenu();
    initScrollAnimations();
    initSmoothScroll();
    initTableOfContents();
    initLazyLoad();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
