// Loyal & Loved — affiliate link builder
// ---------------------------------------
// Reads /affiliates.json (the brand brain) and rewrites any anchor tag
// carrying data-aff-brand into a properly-tracked affiliate URL.
//
// Usage inside any article:
//   <a data-aff-brand="omlet"
//      data-aff-target="https://www.omlet.co.uk/shop/chicken-coops/eglu-cube/"
//      data-aff-clickref="best-coops-uk-hero"
//      href="#placeholder"
//      class="aff-link">Buy the Eglu Cube</a>
//
// If the brand is approved, href is replaced with the tracked URL and
// rel="sponsored nofollow noopener" + target="_blank" are set.
// If the brand is pending or flagged do-not-wire, the anchor stays
// as a placeholder (aria-disabled=true, class "aff-link-pending").
//
// Works as plain <script src="/js/affiliate-links.js" defer></script>
// in the <head> or before </body>.

(function () {
  'use strict';

  var SOURCE = '/affiliates.json';

  // Promise cache — fetched once per page load.
  var READY = fetch(SOURCE, { cache: 'no-cache' })
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      window.LL_AFFILIATES = data;
      return data;
    })
    .catch(function (err) {
      console.warn('[affiliate-links] could not load affiliates.json:', err);
      return null;
    });

  // Public API — call directly if you need a URL programmatically.
  window.buildAffiliateLink = function (brandSlug, targetUrl, opts) {
    opts = opts || {};
    return READY.then(function (data) {
      if (!data) return null;
      var brand = data.brands && data.brands[brandSlug];
      if (!brand) {
        console.warn('[affiliate-links] unknown brand:', brandSlug);
        return null;
      }
      if (brand.status !== 'approved') return null;
      if (brand.ethicsFlag === 'red_do_not_wire') {
        console.warn('[affiliate-links] refusing to build link — brand flagged do-not-wire:', brandSlug);
        return null;
      }

      var clickref = opts.clickref || '';
      var publisher = data.publisher || {};

      switch (brand.network) {
        case 'awin': {
          var aid = publisher.awin_publisher_id;
          if (!aid || /REPLACE_WITH/.test(aid)) {
            console.warn('[affiliate-links] Awin publisher ID not set in affiliates.json');
            return null;
          }
          var target = encodeURIComponent(targetUrl || brand.merchantHome || '');
          var cr = clickref ? '&clickref=' + encodeURIComponent(clickref) : '';
          return 'https://www.awin1.com/cread.php?awinmid=' + encodeURIComponent(brand.merchantId)
            + '&awinaffid=' + encodeURIComponent(aid)
            + '&ued=' + target
            + cr;
        }
        case 'amazon': {
          var tag = publisher.amazon_associates_tag;
          if (!tag) return null;
          try {
            var u = new URL(targetUrl || brand.merchantHome);
            u.searchParams.set('tag', tag);
            return u.toString();
          } catch (e) {
            console.warn('[affiliate-links] invalid Amazon target URL:', targetUrl);
            return null;
          }
        }
        case 'impact': {
          if (!brand.impactTrackingBase) return null;
          var sep = brand.impactTrackingBase.indexOf('?') === -1 ? '?' : '&';
          return brand.impactTrackingBase
            + sep + 'u1=' + encodeURIComponent(clickref)
            + '&subid1=' + encodeURIComponent(targetUrl || '');
        }
        case 'direct': {
          if (!brand.directLinkTemplate) return null;
          return brand.directLinkTemplate
            .replace('{{TARGET}}', encodeURIComponent(targetUrl || ''))
            .replace('{{SUBID}}', encodeURIComponent(clickref));
        }
        default:
          return null;
      }
    });
  };

  // DOM rewriter — runs once on DOMContentLoaded.
  function rewire() {
    var anchors = document.querySelectorAll('a[data-aff-brand]');
    if (!anchors.length) return;
    READY.then(function (data) {
      anchors.forEach(function (a) {
        var slug = a.getAttribute('data-aff-brand');
        var target = a.getAttribute('data-aff-target') || '';
        var clickref = a.getAttribute('data-aff-clickref') || '';
        window.buildAffiliateLink(slug, target, { clickref: clickref })
          .then(function (url) {
            if (url) {
              a.setAttribute('href', url);
              a.setAttribute('rel', 'sponsored nofollow noopener');
              a.setAttribute('target', '_blank');
              a.classList.remove('aff-link-pending');
              a.classList.add('aff-link-live');
              a.removeAttribute('aria-disabled');
            } else {
              // Pending, unknown, or do-not-wire — keep as placeholder.
              a.setAttribute('aria-disabled', 'true');
              a.classList.remove('aff-link-live');
              a.classList.add('aff-link-pending');
              a.removeAttribute('href');
              a.style.cursor = 'default';
              a.addEventListener('click', function (e) { e.preventDefault(); });
            }
          });
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', rewire);
  } else {
    rewire();
  }
})();

/* ===========================================================================
 * PB Eng affiliate click tracking — beacons every successful affiliate click
 * to the Cloudflare Worker so the dashboard can count clicks per page/brand.
 * Self-contained IIFE — does not interfere with the rewriter above.
 * Uses event delegation so it works regardless of when the rewriter finishes.
 * navigator.sendBeacon is fire-and-forget, so it never blocks the click.
 * Source of truth: Website Dashboard/cloudflare-worker/tracking-snippet.js
 * =========================================================================== */
(function () {
  'use strict';

  var TRACK_URL = 'https://pb-eng-click-tracker.jlogan223.workers.dev/track';
  var host = (location.host || '').toLowerCase();
  var SITE = host.indexOf('loyalandloved') !== -1 ? 'll'
           : host.indexOf('thesecondincome') !== -1 ? 'tsi'
           : 'unknown';

  function shouldTrack(a) {
    if (!a) return false;
    var hasBrand = a.dataset && a.dataset.affBrand;
    var hasAffClass = a.classList && a.classList.contains('aff-link');
    if (!hasBrand && !hasAffClass) return false;
    var href = a.getAttribute('href');
    if (!href) return false;
    if (href.charAt(0) === '#') return false;
    if (a.getAttribute('aria-disabled') === 'true') return false;
    return true;
  }

  function detectNetwork(a, href) {
    var explicit = a.dataset && (a.dataset.affNetwork || a.dataset.network);
    if (explicit) return explicit;
    if (!href) return 'unknown';
    if (/amzn\.to|amazon\./i.test(href)) return 'amazon';
    if (/awin1\.com|awin\./i.test(href)) return 'awin';
    if (/topcashback/i.test(href)) return 'topcashback';
    if (/quidco/i.test(href)) return 'quidco';
    if (/swagbucks/i.test(href)) return 'swagbucks';
    if (/pxf\.io|partnerstack/i.test(href)) return 'partnerstack';
    return 'unknown';
  }

  function send(a) {
    try {
      var href = a.getAttribute('href') || '';
      var data = {
        site: SITE,
        page: location.pathname,
        brand: (a.dataset && a.dataset.affBrand) || '',
        network: detectNetwork(a, href),
        targetUrl: href,
        referrer: document.referrer || ''
      };
      var blob = new Blob([JSON.stringify(data)], { type: 'application/json' });
      navigator.sendBeacon(TRACK_URL, blob);
    } catch (e) { /* never block navigation */ }
  }

  document.addEventListener('click', function (e) {
    var t = e.target;
    if (!t) return;
    var a = (t.closest ? t.closest('a') : null);
    if (shouldTrack(a)) send(a);
  }, true);
})();
