# Pet & Proud UK — Build Memory

## Project Overview
- **Client**: Justin Logan / PB Eng Ltd
- **Site Name**: Pet & Proud UK (abbreviation: PNP, short name: Pet & Proud)
- **Platform**: Pure HTML/CSS/JS, hosted on GitHub Pages + Cloudflare
- **Dev Server**: Node.js on port 3002
- **Domain**: petandproud.uk (placeholder)
- **Launch Articles**: 15 full articles (800-1500 words each)

## Design System
- **Light default** (opposite of TSI-UK which is dark-first)
- **Colours**: Warm off-white (#FAF7F2), sage green (#5B7C5B), soft terracotta (#C4745A), charcoal (#2D2D2D), cream (#FFF8F0)
- **Fonts**: Fraunces (headings, Google Fonts), Nunito (body, Google Fonts)
- **Mood**: Warm, friendly, lifestyle magazine + trusted vet advice

## File Structure Created
```
pet-site/
  index.html
  about.html
  privacy-policy.html
  robots.txt
  sitemap.xml
  start-website.bat
  js/
    site-config.js (brand config, colors, GA4 placeholder)
    theme.js (light/dark switcher, default: light)
    articles.js (central article registry)
    carousel.js (4-card hero carousel, 6s auto-advance)
    cookies.js (consent bar, slides up)
    main.js (scroll animations, mobile menu)
  css/
    style.css (globals + CSS variables)
    article.css
    category.css
    carousel.css
  category/
    pet-insurance.html
    food-nutrition.html
    health-vet-care.html
    training-behaviour.html
    gear-tech.html
    breed-guides.html
  articles/
    (15 HTML files, one per article)
  images/
    (placeholder folder)
```

## Article List & Status
1. best-pet-insurance-uk.html — [TODO]
2. pet-insurance-cost-uk.html — [TODO]
3. lifetime-vs-annual-pet-insurance.html — [TODO]
4. vet-bills-uk.html — [TODO]
5. best-fresh-dog-food-uk.html — [TODO]
6. flea-tick-worm-protection.html — [TODO]
7. best-dog-gps-tracker-uk.html — [TODO]
8. cost-of-owning-dog-uk.html — [TODO]
9. pet-dental-care.html — [TODO]
10. senior-dog-care.html — [TODO]
11. puppy-first-year-checklist.html — [TODO]
12. best-cat-insurance-uk.html — [TODO]
13. indoor-vs-outdoor-cats.html — [TODO]
14. cockapoo-cost-uk.html — [TODO]
15. emergency-vet-costs-uk.html — [TODO]

## Key Requirements
- Real, useful content (not thin SEO filler)
- UK spelling (colour, behaviour, organisation)
- Every article: breadcrumbs, hero image placeholder, TOC, sections with h2/h3, image placeholders every 2-3 sections, affiliate link placeholders, related articles, desktop sidebar
- Affiliate disclosure on every page
- FCA disclaimer on all insurance articles
- Responsive design: 3-col desktop, 2-col tablet, 1-col mobile
- Sitemap + robots.txt
- Cookie consent bar (non-blocking)
- GA4 placeholder

## Build Progress — COMPLETE
- [x] Folder structure
- [x] site-config.js
- [x] theme.js
- [x] articles.js (15 articles registered)
- [x] All CSS files (style.css, article.css, carousel.css, category.css)
- [x] HTML infrastructure (index.html, about.html, privacy-policy.html)
- [x] Category pages (6 complete: pet-insurance, health-vet-care, food-nutrition, training-behaviour, gear-tech, breed-guides)
- [x] 15 Article pages (all created with full structure and content)
- [x] carousel.js, cookies.js, main.js
- [x] sitemap.xml, robots.txt, start-website.bat

## Final Statistics
- Total Files: 38
- HTML Files: 24 (1 index + 2 core pages + 6 categories + 15 articles)
- CSS Files: 4 (global + article-specific + carousel + category)
- JS Files: 6 (config, theme, articles registry, carousel, cookies, main)
- Images Directory: Created (ready for images)
- Meta Files: robots.txt, sitemap.xml, start-website.bat

## Article Details
All 15 articles created with:
- Full HTML structure with breadcrumbs, meta tags, hero images
- Table of contents auto-generated from h2 headings
- Article metadata (date, author, read time)
- Multiple content sections with h2/h3 hierarchy
- Image placeholders throughout (every 2-3 sections)
- Key takeaway callout boxes
- Related articles section at bottom
- Desktop sidebar with quick links and newsletter signup
- FCA disclaimers on insurance articles
- Affiliate link placeholders

## Categories
All 6 category pages with:
- Category hero section
- Articles grid (will auto-populate from articles.js registry)
- Affiliate CTA box
- Newsletter signup
- Full footer and navigation

## Technology Features
- Pure HTML/CSS/JS (no frameworks/build tools)
- Light-first theme with dark mode toggle (default: light)
- Cookie consent bar (slides up, non-blocking)
- GA4 placeholder in config
- Responsive design (3-col desktop, 2-col tablet, 1-col mobile)
- Semantic HTML throughout
- CSS custom properties for easy theme switching
- Mobile hamburger menu
- Smooth scroll navigation
- Lazy load support for images

## Next Steps
1. Add real images to /images folder
2. Get GA4 property ID and update site-config.js
3. Update affiliate links when approved
4. Set up GitHub Pages deployment
5. Configure Cloudflare DNS
6. Update domain in site-config.js (currently: petandproud.uk placeholder)
7. Add actual newsletter backend
8. Get contact email configured (currently: contact@petandproud.uk placeholder)
