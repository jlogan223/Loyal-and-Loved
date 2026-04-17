# LL_CURRENT_STATE.md — Loyal & Loved Live Status

> Separate from `CURRENT_STATE.md` in this folder (which is for
> AffiliateStudio). This file reflects the live status of the Loyal &
> Loved website only.

_Last updated: 2026-04-16_

---

## Phase
**Live site operating, affiliate monetisation wave underway.** 15
articles published at `https://loyalandloved.co.uk`. Focus right now:
securing the affiliate programme approvals needed to swap out "Link
Coming Soon" placeholders with real deep links.

## Last completed
- **2026-04-16** Impact.com publisher site verification meta tag
  deployed to homepage (`<meta name="impact-site-verification"
  value="bfdd3a59-469f-4dd6-aa3a-9934d34db2f0">`) — commit `b26bb0f`
  pushed to `origin/main` via `push-clone/`.
- **2026-04-16** `AFFILIATE_RESEARCH_2026-04-16.md` delivered — three
  parts: direct programmes for 8 non-Awin brands, ethics red flags on
  current pending list, full Awin advertiser sweep with 25+ new
  applications recommended in priority order.
- **2026-04-16** `SEO_REDIRECTS.md` delivered — single-rule Cloudflare
  Bulk Redirect plan for legacy `/Loyal-and-Loved-FIXED/*` paths. Not
  yet deployed by Justin.
- **2026-04-16** Butternut Box Ambassador application copy finalised
  (both under 1000 chars, revised to remove personal-use claim).
- **2026-04-16** Awin 255-char introduction message delivered.
- **2026-04-16** Impact.com site description delivered (~750-char long
  and ~400-char compressed versions).

## In progress (awaiting response)
- **Awin applications — pending approval:** Butternut Box (6074? tails),
  Tails.com (6074), Pure Pet Food (28012), PitPat (43513), Your Pet
  Nutrition UK (123532), Scruffs (23375), PDSA (7028), Purina (24465 —
  DO NOT wire even if approved), YuMOVE (17141), Wisdom Panel UK
  (16376), Itch Pet (18115), Zooplus (2940), Edgard & Cooper (100729),
  KatKin (21501), Lily's Kitchen (7262), Bella & Duke (111046), Omlet
  (76702), Christies Direct (3379 — alignment questionable), VetBox
  (34905), The Pharm Pet Co. (109526), Everypaw (19162), Co-op Pet
  Insurance (86195), Viovet (6960).
- **Awin applications — approved:** Barking Heads & Meowing Heads
  (15852), AATU (17135), **Omlet (76702) — approved 2026-04-16, 5%
  commission ex. VAT, 60-day cookie**.
- **Impact.com:** publisher account active; meta tag deployed but
  verification crawler awaits Cloudflare cache purge.

## Next task (in order)
0. **Paste Awin Publisher ID** so I can fill in
   `affiliates.json` → `publisher.awin_publisher_id` and switch on link
   generation for Omlet, AATU, Barking Heads (and every future Awin
   approval). Publisher ID is public (appears in every tracking URL) —
   safe to share in chat. The API token, by contrast, goes into
   `affiliate-secrets.json` (gitignored) locally.
1. **Purge Cloudflare cache** so Impact.com's verification crawler picks
   up the new meta tag on `index.html`. (`dash.cloudflare.com →
   loyalandloved.co.uk → Caching → Configuration → Purge Everything`.)
2. **Deploy the Cloudflare Bulk Redirect** per `SEO_REDIRECTS.md` to
   convert `/Loyal-and-Loved-FIXED/*` 404s into 301s.
3. **Apply to Animal Friends Pet Insurance** via
   `animalfriends.co.uk/partner-up-with-us/` — relationship-driven, uses
   the Butternut/Impact-style pitch copy.
4. **Petplan UK — alternative routes.** Programme 3058 unreachable via
   Awin search, website doesn't load, email addresses bounced. Options:
   (a) LinkedIn outreach to Petplan/Allianz UK partnerships lead, (b)
   switchboard 0345 077 1936 to ask for affiliate team, (c) social DM,
   (d) accept the miss and lean on Everypaw + Co-op + Animal Friends +
   ManyPets as insurance comparators.
5. **Apply to ManyPets on Impact.com** (search "ManyPets" in Impact
   publisher dashboard) once Impact verification completes.
6. **Apply to Tractive on Impact.com** (same session).
7. **Contact mailbox:** create `contact@loyalandloved.co.uk` for
   business correspondence (backlog).
8. **Rewrite custom sidebar on `pet-insurance-cost-uk`** — flagged in
   memory as needing work, exact details in `memory.md`.
9. **Swap "Link Coming Soon" placeholder spans** in articles as each
   Awin/Impact approval lands.

## Open questions
- **Does Petplan UK still run a working affiliate programme in 2026?**
  Awin listing exists (ID 3058) but appears unreachable. May be
  invitation-only / suspended. Needs direct human contact.
- **Is Christies Direct aligned?** Professional grooming equipment — may
  be too niche for the home-groomer audience. Keep the approval if
  offered; revisit editorial fit.
- **Pets at Home** — direct partnerships enquiry or skip? Low priority
  given Zooplus + Viovet + Amazon overlap.

## Blocked on
- **Impact.com verification** blocked on Cloudflare cache purge
  (Justin's action).
- **Pet Plan 3058 outreach** blocked on finding a working Petplan UK
  contact route (website down, emails bouncing).
- **`/Loyal-and-Loved-FIXED/*` 301s** blocked on Justin deploying the
  Cloudflare Bulk Redirect rule per `SEO_REDIRECTS.md`.

## Recent decisions (pointer)
Full list in `LL_DECISIONS.md`. Session-level decisions recorded this
round:
- DO NOT wire Purina affiliate links even if approved.
- DISCLOSE Tails.com's Nestlé Purina ownership in any recommendation.
- FRAME PDSA Pet Insurance as commercial (not charitable).
- British English across all new content and applications.
- Use LL_ prefix on Loyal & Loved memory files to avoid clashing with
  AffiliateStudio files in the same workspace folder.
