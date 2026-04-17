# LL_CURRENT_STATE.md — Loyal & Loved Live Status

> Separate from `CURRENT_STATE.md` in this folder (which is for
> AffiliateStudio). This file reflects the live status of the Loyal &
> Loved website only.

_Last updated: 2026-04-17_

---

## Phase
**Live site operating, affiliate monetisation in progress.** 15
articles published at `https://loyalandloved.co.uk`. Affiliate link
automation scaffold is live (affiliates.json + js/affiliate-links.js).
Three Awin brands approved and wired. 25 affiliate placements across
9 articles. IndexNow deployed. Cloudflare Bulk Redirects deployed.

## Last completed
- **2026-04-17** Commit `5f64760` pushed — affiliate link UX fix
  (pending links no longer jump to top), broken Omlet/AATU URLs fixed,
  puppy-first-year-checklist enhanced with expandable cost table +
  Amazon product links, SEO_REDIRECTS.md updated for 2026 Cloudflare UI.
- **2026-04-16** IndexNow deployed — verification file, bulk submission
  script, 24 URLs submitted (HTTP 202).
- **2026-04-16** Favicon regenerated — darkened ampersand, 15% padding,
  48/96/192px sizes for Google's circular crop.
- **2026-04-16** Affiliate link automation scaffold built — affiliates.json
  (brand brain, 27 entries) + js/affiliate-links.js (DOM rewriter).
  Wired into all 24 pages. 25 placements across 9 articles.
- **2026-04-16** Cloudflare Bulk Redirects deployed by Justin per
  SEO_REDIRECTS.md — `/Loyal-and-Loved-FIXED/*` → root equivalents (301).
- **2026-04-16** Impact.com publisher site verification meta tag deployed.
- **2026-04-16** Affiliate research delivered, Awin applications submitted.

## In progress (awaiting response)
- **Awin applications — approved:** Barking Heads (15852), AATU (17135),
  Omlet (76702, 5% ex. VAT, 60-day cookie).
- **Awin applications — pending:** ~21 brands (see affiliates.json for
  full list). Animal Friends applied 2026-04-16.
- **Impact.com:** publisher account active, site verification pending.

## Next task (in order)
1. **Build inline brand name links** throughout article body text — user
   approved this UX approach. Clickable brand names in prose, not just
   CTA buttons at bottom.
2. **Build "Quick Compare" summary box** near top of comparison articles
   (e.g. best-pet-insurance-uk.html). Template one, roll out to others.
3. **Justin: update Awin publisher profile** website from
   jlogan223.github.io/affiliatestudio-app to loyalandloved.co.uk
   (fixes utm_campaign in tracking URLs).
4. **Justin: purge Cloudflare cache** after latest push.
5. **Apply to ManyPets on Impact.com** once verification completes.
6. **Apply to Tractive on Impact.com** (same session).
7. **Petplan UK — alternative routes.** Programme 3058 unreachable.
8. **Contact mailbox:** create `contact@loyalandloved.co.uk` (backlog).
9. **Save Awin API token** into local affiliate-secrets.json (Justin).
10. **Impact.com:** fetch Account SID + Auth Token once approved.

## Open questions
- **Does Petplan UK still run a working affiliate programme in 2026?**
- **Is Christies Direct aligned?** May be too niche for home-groomer audience.

## Blocked on
- **Impact.com verification** blocked on Cloudflare cache purge.
- **Petplan 3058 outreach** blocked on finding working contact route.

## Recent decisions (pointer)
Full list in `LL_DECISIONS.md`. Session-level decisions recorded this
round:
- DO NOT wire Purina affiliate links even if approved.
- DISCLOSE Tails.com's Nestlé Purina ownership in any recommendation.
- FRAME PDSA Pet Insurance as commercial (not charitable).
- British English across all new content and applications.
- Use LL_ prefix on Loyal & Loved memory files to avoid clashing with
  AffiliateStudio files in the same workspace folder.
