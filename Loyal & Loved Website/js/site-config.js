/**
 * Loyal & Loved UK — Global Site Configuration
 * Single source of truth for brand, colours, and GA4 ID
 * Easy to swap entire branding via this object
 */

window.SITE_CONFIG = {
  name: "Loyal &amp; Loved UK",
  shortName: "Loyal &amp; Loved",
  abbreviation: "LNL",
  tagline: "Trusted advice for UK pet owners",
  domain: "loyalandloved.co.uk",
  ga4Id: "", // Add property ID when approved

  colors: {
    primary: "#5B7C5B",        // Sage green
    accent: "#C4745A",         // Soft terracotta
    dark: "#2D2D2D",           // Charcoal
    light: "#FAF7F2",          // Warm off-white
    cream: "#FFF8F0"           // Cream
  },

  fonts: {
    heading: "'Fraunces', serif",
    body: "'Nunito', sans-serif"
  },

  companyInfo: {
    name: "PB Eng Ltd",
    jurisdiction: "UK Ltd"
  },

  affiliateDisclosure: "We are a participant in affiliate programs for various companies mentioned on this website. We only recommend products and services we genuinely believe will help you care for your pets. When you purchase through our affiliate links, we earn a small commission at no extra cost to you."
};

// CSS custom properties will be set by theme.js on page load
// and synced to these values
