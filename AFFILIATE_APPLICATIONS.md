# Loyal & Loved — Affiliate Application Pack

_Last updated: 2026-04-16_

Justin already has an **Awin** publisher account and an **Amazon Associates UK** account, so most of the work below is applying to advertisers **inside Awin** (no new account signup needed). A few brands sit outside Awin — those get direct links.

---

## Master copy-paste block (reuse in every application)

Most Awin advertisers have a short "Tell us about your site / promotional methods" field. Paste this in:

### Website description
> **Loyal & Loved (https://loyalandloved.co.uk)** is an independent UK pet content site covering pet insurance, vet care, food and nutrition, training and behaviour, gear and tech, and breed ownership costs. We publish long-form buyer guides and cost breakdowns aimed at first-time and experienced UK pet owners making purchase decisions. All editorial is written in-house, in British English, with a transparent affiliate-disclosure policy (see https://loyalandloved.co.uk/about.html#affiliate-disclosure). The site is registered to PB Eng Ltd, a UK Ltd company.

### Promotional methods
> Contextual in-content links and comparison tables within buyer guides. Sidebar recommendations on category pages. Occasional newsletter mentions to opt-in subscribers. We do not use PPC bidding on brand terms, trademark bidding, coupon-site tactics, incentivised traffic, or cashback. All links are tagged `rel="sponsored nofollow"`.

### Traffic sources
> Organic search (primary), direct, referral. No paid traffic.

### Expected monthly clicks (to be conservative while ramping up)
> 500–2,000 clicks/month in first 6 months, growing as search rankings build. Happy to provide updated figures after each quarter.

### Company details
> **Company:** PB Eng Ltd
> **Country:** United Kingdom
> **Contact:** Justin (pbengukltd@gmail.com)

---

## Tier 1 — Insurance (highest-priority, referenced in 5 articles)

### 1. Petplan
- **Network:** Awin
- **Application:** Awin dashboard → Advertisers → search "Petplan"
- **Direct link:** https://www.awin1.com/awclk.php?mid=2677 _(if missing, search within Awin)_
- **Notes:** Largest UK pet insurer. Usually accepts content-site publishers within 2–5 working days. They often ask for sample article URLs — give them `best-pet-insurance-uk.html` and `pet-insurance-cost-uk.html`.

### 2. Animal Friends Pet Insurance
- **Network:** Awin
- **Application:** Awin dashboard → search "Animal Friends"
- **Notes:** Often advertises charity-linked angle. Paste the master block above, add: "We cover charity-aligned providers in our ethical-insurance comparisons."

### 3. ManyPets (and Bought By Many)
- **Network:** Awin (also Impact.com)
- **Application:** Awin dashboard → search "ManyPets". The ManyPets application typically covers Bought By Many since they merged — confirm during application.
- **Fallback:** If not on Awin, apply via Impact.com → https://manypets.com/uk/affiliates (requires separate Impact publisher signup).

---

## Tier 2 — Food & nutrition (referenced in best-fresh-dog-food-uk + puppy-first-year-checklist)

### 4. Butternut Box
- **Network:** Impact.com (primary), sometimes Awin
- **Direct:** https://butternutbox.com/affiliates
- **Application:** Sign up at impact.com as a publisher (free, separate from Awin), then apply to the Butternut Box programme.
- **Notes:** Has a customer-referral scheme in addition to affiliate — don't confuse the two. You want the **affiliate** programme (recurring commissions on new customer orders).

### 5. Tails.com
- **Network:** Awin
- **Application:** Awin dashboard → search "Tails.com"
- **Notes:** Pay-per-acquisition on first paid box. Good fit for the dog-food comparison guide.

### 6. Pure Pet Food (optional add-on, not currently linked from articles)
- **Network:** Awin
- **Application:** Awin dashboard → search "Pure Pet Food"
- **Notes:** Worth adding as a third comparator in the fresh-food article. Freeze-dried angle is different from Butternut/Tails.

---

## Tier 3 — Gear & tech (referenced in best-dog-gps-tracker-uk + puppy-first-year-checklist)

### 7. PitPat
- **Network:** Awin
- **Application:** Awin dashboard → search "PitPat"
- **Notes:** UK-made activity + location tracker. Strong UK-owner fit.

### 8. Tractive
- **Network:** Awin (EU-wide programme)
- **Application:** Awin dashboard → search "Tractive"
- **Notes:** If not listed under Awin UK, check Awin EU/international. They also run a direct programme via their own portal (https://tractive.com/en/affiliate) as a fallback.

### 9. Pets at Home
- **Network:** Awin
- **Application:** Awin dashboard → search "Pets at Home"
- **Notes:** Covers GPS trackers, flea/tick products, food, accessories, grooming. Mentioned in 5+ articles — worth having approved early. Lower commission rate (~3–5%) but huge product range.

---

## Tier 4 — Vet pharmacy / consumables (referenced in flea-tick-worm-protection, pet-dental-care)

### 10. Vet-UK
- **Network:** Awin
- **Application:** Awin dashboard → search "Vet-UK"
- **Notes:** Online pet pharmacy, parasitic treatments, prescription meds. High basket value, decent commission.

### 11. Pet Drugs Online (backup to Vet-UK)
- **Network:** Awin
- **Application:** Awin dashboard → search "Pet Drugs Online"
- **Notes:** Alternative supplier — useful to have both so articles can cite "available from X or Y" for credibility.

---

## Tier 5 — General catch-all (already set up)

### 12. Amazon Associates UK ✅
- **Status:** Already approved.
- **Store ID:** Use the existing tag.
- **Notes:** Use for anything not covered above (toothbrushes, dental chews, crates, cones, gates, toys, books). Low commission (~1–3% in the pet category) but universal coverage.

### 13. PDSA / Blue Cross
- **Not affiliate programmes** — charities. Leave links unaffiliated; they're useful for editorial credibility.

---

## Application order (suggested sequence)

1. **This week:** Petplan, Animal Friends, ManyPets, Pets at Home — these unblock 8+ article affiliate slots.
2. **Next week:** Butternut Box (Impact.com account first), Tails.com, Vet-UK, PitPat.
3. **Week 3:** Tractive, Pure Pet Food, Pet Drugs Online — round out the coverage.

Most Awin advertisers approve within 2–5 working days. Butternut/Impact typically takes ~7 days. If rejected, the rejection email usually says why — most rejections for new sites are resolved by re-applying after the first 10 indexed articles (you're there) and a month of organic traffic.

---

## After approval — what to do with the links

Each Awin advertiser gives you a deep-link generator. Inside the site:

1. Open the relevant article (e.g. `articles/best-pet-insurance-uk.html`).
2. Find the `<span class="affiliate-btn affiliate-btn--pending">Petplan — Get Quote — Link Coming Soon</span>` span.
3. Replace it with the real deep link, for example:

```html
<a class="affiliate-btn" href="https://www.awin1.com/awclk.php?mid=XXXX&id=YYYY" rel="sponsored nofollow" target="_blank">Petplan — Get Quote</a>
```

Once all four insurance articles' buttons are live, push to GitHub + purge Cloudflare, and the revenue path is active.
