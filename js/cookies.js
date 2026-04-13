/**
 * Cookie Consent Bar
 * Slides up from bottom, non-blocking
 * Stores preference in localStorage
 */

(function() {
  const CONSENT_KEY = 'lnl-cookie-consent';
  const CONSENT_VERSION = '1.0';

  function hasConsent() {
    const stored = localStorage.getItem(CONSENT_KEY);
    return stored === CONSENT_VERSION;
  }

  function setConsent() {
    localStorage.setItem(CONSENT_KEY, CONSENT_VERSION);

    // Load GA4 if ID is configured
    if (window.SITE_CONFIG && window.SITE_CONFIG.ga4Id) {
      loadGA4(window.SITE_CONFIG.ga4Id);
    }
  }

  function loadGA4(propertyId) {
    if (!propertyId) return;

    // Google Analytics 4 snippet
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${propertyId}`;
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', propertyId);
  }

  function hideCookieBar() {
    const bar = document.querySelector('.cookie-consent-bar');
    if (bar) {
      bar.classList.add('hidden');
      // Remove from DOM after animation
      setTimeout(() => {
        bar.style.display = 'none';
      }, 300);
    }
  }

  function initCookieBar() {
    // If user already consented, don't show bar
    if (hasConsent()) {
      hideCookieBar();
      setConsent(); // Re-load GA4 on subsequent pages
      return;
    }

    const bar = document.querySelector('.cookie-consent-bar');
    if (!bar) return;

    // Accept button
    const acceptBtn = bar.querySelector('.cookie-accept-btn');
    if (acceptBtn) {
      acceptBtn.addEventListener('click', () => {
        setConsent();
        hideCookieBar();
      });
    }

    // Dismiss/close button
    const dismissBtn = bar.querySelector('.cookie-dismiss-btn');
    if (dismissBtn) {
      dismissBtn.addEventListener('click', () => {
        hideCookieBar();
      });
    }

    // Make bar visible with slide-up animation
    bar.classList.add('visible');
  }

  // Initialize on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCookieBar);
  } else {
    initCookieBar();
  }

  // Expose for testing
  window.cookieConsent = {
    hasConsent,
    setConsent,
    reset: () => localStorage.removeItem(CONSENT_KEY)
  };
})();
