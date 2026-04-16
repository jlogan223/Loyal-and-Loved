# Loyal & Loved — Session Memory

## Backlog (not urgent)

- [ ] **Create `contact@loyalandloved.co.uk` mailbox** (or swap the address on
      privacy-policy.html to something real). Currently the line reads
      "contact@loyalandloved.co.uk (placeholder)". Low priority — tidy up
      before any press / partnerships outreach.
- [ ] Swap "Link Coming Soon" spans for real affiliate deep-links once
      each Awin/Impact application is approved. Full programme-by-programme
      guide lives in `AFFILIATE_APPLICATIONS.md`.
- [ ] Rewrite pet-insurance-cost-uk's custom sidebar ("Money Saving Tips"
      widget currently has three dead `#save-money` / `#age-pricing` /
      `#lifetime-vs-annual` anchors). Separate from the Quick Links fix
      shipped in d249826.
- [ ] Clean up stale `heroImage` / `thumbnailImage` / empty `affiliateLinks`
      fields in `js/articles.js`. Dormant (nothing currently reads them) but
      noisy. Low priority.

## Session 2026-04-16 (placeholder audit + affiliate list)

### What user asked for
1. Go through every page — audit every remaining placeholder on the site and report back.
2. Provide a list of affiliates to apply to now that the site is live.

### Placeholder audit findings (LIVE files only, excluding Loyal-and-Loved-FIXED archive)

**Category A: Related-articles cards at the bottom of every article (45 broken images)**
- 15 articles × 3 cards = 45 `<img>` tags pointing at non-existent `../images/placeholder*.jpg` paths
- Paths used: `placeholder.jpg`, `placeholder-insurance.jpg`, `placeholder-cost.jpg`, `placeholder-vet.jpg`, `placeholder-policy.jpg`, `placeholder-puppy.jpg`, `placeholder-lifetime.jpg`, `placeholder-indoor.jpg`
- Links inside the cards (`<a href=...>`) DO resolve correctly — only the images are broken
- Alt text literally reads "Placeholder: ..." on several

**Category B: Sidebar Table of Contents dead anchors (30 bad links across 14 articles)**
- Every article sidebar has hardcoded `<a href="#section1">Main Content</a>` / `<a href="#section2">More Info</a>`
- Neither anchor exists in the HTML — they jump to top of page
- Real section IDs exist in each article (`#intro`, `#routine-costs`, `#takeaway`, etc.) and aren't linked
- Count by article: most have 2, best-pet-insurance-uk + best-dog-gps-tracker-uk + best-cat-insurance-uk have extra

**Category C: "Link Coming Soon" affiliate placeholders (15 across 5 articles)**
- best-pet-insurance-uk: 4 (Petplan, Animal Friends, Bought By Many, ManyPets — all "Get Quote")
- best-cat-insurance-uk: 4 (Petplan Cat, Bought By Many Cat, ManyPets Cat, Animal Friends Cat)
- best-dog-gps-tracker-uk: 4 (PitPat Activity Tracker, Tractive GPS Tracker ×2, PitPat at Pets at Home)
- flea-tick-worm-protection: 2 (Vet-UK Parasite Treatments, Pets at Home Flea & Tick Range)
- cockapoo-cost-uk: 1 (Compare Pet Insurance for Cockapoos)

**Category D: Registry `heroImage` / `thumbnailImage` fields in js/articles.js (30 stale paths)**
- All 15 entries have placeholder paths like `images/placeholder-insurance-comparison.jpg`
- NOT CURRENTLY RENDERED — no consumer reads these fields
- Dead weight in the registry; can be left or cleaned up
- `getRelatedArticles()` helper exists but is never called — related-articles sections are hardcoded per-article

**Category E: Registry `affiliateLinks` fields (all empty strings)**
- Every article has an `affiliateLinks: { "Brand": "" }` block with URLs left blank
- Not rendered anywhere either — dormant

**Category F: Privacy policy**
- privacy-policy.html line 192: `contact@loyalandloved.co.uk (placeholder)` — address not yet created

### Scope totals
- 45 broken related-articles images
- ~30 dead sidebar ToC anchors
- 15 "Link Coming Soon" affiliate buttons visible to users
- 30 stale registry image paths (not rendered)
- 15 empty affiliate URL slots (not rendered)
- 1 placeholder contact email

### Decision for fix approach
1. Rewrite related-articles sections via fix_site.py to use hero images from `images/articles/{slug}/hero.png` and real title/excerpt from LNL_ARTICLES registry
2. Rewrite sidebar ToCs to reflect actual `<section id="...">` anchors in each article
3. Leave "Link Coming Soon" buttons alone until Justin has real affiliate URLs — will swap once applications approved
4. Decide whether to clean up registry fields later (dormant, low priority)
5. Create contact@loyalandloved.co.uk mailbox (Justin's task)

### Affiliate application list delivered separately — see response text

## Session 2026-04-15 (continued — site-wide cleanup)

### Issues the user flagged
1. health-vet-care, food-nutrition, training-behaviour, gear-tech all
   had `TITLE_PLACEHOLDER` in the `<title>`, breadcrumb, and `<h1>`.
2. Home page carousel cards were being clipped on the sides and bottom
   (hover-lift + box-shadow cut by `.carousel-viewport { overflow: hidden }`).
3. Every category page had a single hardcoded `<h3>Article Title</h3>` /
   `<p>Article excerpt...</p>` placeholder card with `href="#"`. Real
   articles existed under `articles/` (all 15) but weren't listed.
4. Old 'Pet & Proud' brand still in category and article footers /
   bylines / copyright lines.

### Fix approach (scripts/fix_site.py, idempotent, dry-run by default)
- Parses `window.LNL_ARTICLES` out of `js/articles.js` (strips // comments,
  quotes bare keys, drops trailing commas, then `json.loads`).
- For each `category/*.html`:
    - Swaps `TITLE_PLACEHOLDER` → `&amp;`.
    - Rebuilds `<div class="article-grid category-articles">...</div>`
      with real `<a class="article-card fade-in">` for every article in
      that category, reusing the homepage card pattern (hero image from
      `images/articles/{slug}/hero.png`, title, excerpt, read time,
      `Read →` CTA).
    - Replaces stale `Pet & Proud` branding.
- For each `articles/*.html`:
    - Just the branding fix.
- For `css/style.css`:
    - `.carousel-viewport` now uses `overflow-x: clip; overflow-y: visible;`
      plus `padding: 8px 4px 24px; margin: -8px -4px -24px;` so the
      hover-lift (translateY -4px) and `box-shadow` on the cards have
      room to bleed without being clipped. Horizontal clipping is
      preserved so transform-based slide transitions still work.

### Article distribution (from LNL_ARTICLES)
- pet-insurance: 4 (best-pet-insurance-uk, pet-insurance-cost-uk, lifetime-vs-annual-pet-insurance, best-cat-insurance-uk)
- health-vet-care: 6 (vet-bills-uk, flea-tick-worm-protection, pet-dental-care, senior-dog-care, emergency-vet-costs-uk, indoor-vs-outdoor-cats)
- food-nutrition: 1 (best-fresh-dog-food-uk)
- gear-tech: 1 (best-dog-gps-tracker-uk)
- training-behaviour: 1 (puppy-first-year-checklist)
- breed-guides: 2 (cost-of-owning-dog-uk, cockapoo-cost-uk)

### Verification
- 0 `TITLE_PLACEHOLDER` remaining
- 0 `Pet & Proud` strings remaining in live files
- Every category-page `href` and every homepage `href` resolves to an
  existing `articles/<slug>.html` file

### Pushed
- **0a3a451** — 22 files touched (13 articles, 6 category pages,
  style.css, fix_site.py, memory.md). 563 insertions / 130 deletions.

### Outstanding
- Justin purges Cloudflare cache so the changes go live
- Visual QA on the home carousel (does the hover-lift now show cleanly?)
- Visual QA on each category page

## Session 2026-04-15 (tier 3 + tier 4 image generation)

### Plan for this round
- User confirmed the 15 new high-quality hero images are much better. Greenlit tier 3 (34 body images) + tier 4 (6 category heroes).
- Added 6 curated category hero prompts (pet-insurance, health-vet-care, food-nutrition, training-behaviour, gear-tech, breed-guides) as flat pastel illustrations in the brand palette.
- Added BODY_PROMPTS dict with 34 curated body-image scenes keyed by `{slug}-pos{position}`. Every one rewritten to avoid garbled text: brand-logo comparisons → abstract pastel panels; documents → blank cream paper; charts → abstract bars; packaging → unlabelled cream containers; phone screens → angled away.
- Extended build_prompt() to check BODY_PROMPTS for body images.
- Dry-run confirmed all 40 entries resolve to curated prompts.

### Generation run — DONE
- 31 new images generated at high quality (9 body shots had been written
  in the earlier aborted run and were skipped on resume)
- Total round-3 cost ≈ 40 × $0.167 = ~$6.68
- Full run took 1387s (~23 min) — about 45s per image on average
- 0 failures

### Pushed to GitHub
- **262fc5e** — all 40 generated images + updated prompts.py +
  generate_images.py (BODY_PROMPTS wiring)
- **bf646b9** — replace_placeholders.py --apply: 55 [IMAGE: …]
  placeholders swapped for real <img> tags across 15 article pages
  and 6 category pages

### Cost tally (cumulative)
- Round 1 (deleted): 16 medium ≈ $0.64
- Round 2 (deleted): 15 medium ≈ $0.60
- Round 3 heroes:    15 high   ≈ $2.50
- Round 4 bodies+categories: 40 high ≈ $6.68 (9 were resumed skips, so actual spend closer to 31 × $0.167 = $5.17 — $1.51 already counted earlier)
- **Running total: ~$10.90**

### Outstanding / next steps
1. Justin purges Cloudflare cache so the new body images and category
   heroes go live immediately (https://dash.cloudflare.com → caching →
   purge everything)
2. Review the 40 new images for composition / text glitches — any
   individual image can be regenerated by editing its prompt in
   scripts/prompts.py (ARTICLE_PROMPTS or BODY_PROMPTS), deleting the
   file, and rerunning generate_images.py (slug+position-specific
   rerun would need a --filter flag — not wired yet)
3. Category pages still show a single hardcoded placeholder article
   card — need dynamic article listings using LNL_ARTICLES registry
   with the clickable card pattern
4. Review published site end-to-end once cache is purged



## Session 2026-04-14 (continued — card CTA + character roster)

### What changed this round (commit 583048a)
1. **Card CTA is now text, not a circle**: replaced `.card-arrow` (teal circle with arrow inside) with `.card-cta` — "Read →" in teal plain text, same colour as the old circle. Arrow animates a few px right on hover; text shifts to accent purple on hover. Same treatment on every carousel and article card.
2. **Character roster in scripts/prompts.py**: 20 pets (Luna Golden, Milo Cockapoo, Bear Bernese, Willow Border Collie, Finn Frenchie, Poppy Dachshund, Rufus Lab, Daisy Springer, Max JRT, Rosie Cavalier, plus Oscar/Bella/Whiskers/Luna-Rose/Tigger/Pepper cats, Kiwi budgie, Thumper rabbit, Shadow horse, Sunny gpig) and 10 UK owners (Sarah 30s, James 40s, Emma late 20s, Michael 60s, Priya 30s, Daniel late 20s, Lucy 40s, Oliver 50s, Chloe early 20s, Hannah vet). Each character has a tight distinctive description so gpt-image-1 can reliably render the same character twice.
3. **Curated per-article scene prompts**: every one of the 15 article heroes now has a hand-written scene in `ARTICLE_PROMPTS`. vet-bills-uk = Bear the Bernese puppy with bandaged paw and soft recovery cone in a warm vet room. pet-insurance-cost-uk = Sarah at kitchen table with Luna resting her chin on the edge. best-dog-gps-tracker-uk = Bear mid-stride through a British meadow with a featureless tracker on his collar. emergency-vet-costs-uk = Daisy lying calmly on exam table with bandaged front leg and Hannah the vet's hand resting on her. etc. Registry is in `/scripts/prompts.py`.
4. **Default quality raised medium → high** in generate_images.py. At 1024x1024, gpt-image-1 "high" is ~$0.167/img (~$2.50 per 15 heroes). `--quality medium` still available for cheaper reruns.
5. **Text rules tightened** in GLOBAL_RULES: explicitly covers packaging, screens, collars, and signage. If any text would naturally appear, render as blank/abstract with no letters.
6. **Regenerated all 15 article heroes** at high quality using curated scenes. ~13 minutes to generate (762s for the batch).

### Confirmation on image model
- We are using **gpt-image-1** (OpenAI's current multimodal image model, launched April 2025, the one that powers ChatGPT's native image generation).
- NOT DALL·E 3 (which remains available as a separate endpoint but is older and worse at photorealism, character consistency, and text rendering).

### What's deployed on GitHub main (commit 583048a)
- Homepage cards use "Read →" text CTA instead of arrow circle
- 15 fresh high-quality article hero images under images/articles/<slug>/hero.png
- scripts/prompts.py with full character roster + article prompt library
- generate_images.py wired to prefer curated prompts with medium/high/low CLI toggle

### Cost tally
- Round 1 (deleted): 16 images medium ≈ $0.64
- Round 2 (deleted): 15 images medium ≈ $0.60
- Round 3 (current): 15 images high ≈ $2.50
- **Running total: ~$3.75**

### Outstanding / next steps
1. **Justin purges Cloudflare cache** so the new index + heroes go live immediately
2. Evaluate the 15 new heroes — any still with garbled lettering or wrong composition can be regenerated individually by editing that scene in `scripts/prompts.py` then running `python3 scripts/generate_images.py --tiers 2 --force` (or use `--limit 1` plus a slug filter if we add one)
3. **Category pages** still show a single hardcoded placeholder card — need dynamic article listings using LNL_ARTICLES registry with the new clickable card pattern
4. **Article pages (15 files)** still have `[IMAGE: ...]` body-image placeholders (34 tier-3 images, ~$5.70 at high, ~$1.30 at medium)
5. **Tier 4 category heroes** still pending (6 images)
6. Run `replace_placeholders.py --apply` on article pages once body images are ready

### Decisions locked this session
- Card CTA: "Read →" teal text, not a circle
- Image model: gpt-image-1 (confirmed)
- Default quality: high
- Character roster lives in scripts/prompts.py — reuse across articles
- Per-article prompts must match emotional register (bandaged puppy for vet bills, content pet on sofa for insurance, etc.)
- Global no-text rule applies to packaging/screens/collars/signage too

### Pitfalls
- gpt-image-1 can still produce slightly-off text at high quality — the "no text" clause is doubled up (in STYLE_PROMPTS and GLOBAL_RULES) because belt-and-braces is needed
- Generation at high quality is slower: ~50s per image vs ~20s at medium

## Prior session context (from earlier memory)

### Repo structure
All site files at repo root (main branch). GitHub Pages + Cloudflare. Previously stuck in `Loyal-and-Loved-FIXED/` subfolder; fixed earlier.

### Git workflow
- Local mount has jammed `.git/index.lock` (FUSE bindfs blocks unlink)
- Workaround: fresh clone at `/sessions/elegant-intelligent-mayer/push-clone/` — copy files in, commit, push from there. PAT embedded in remote URL so pushes work from sandbox.

### API key
OpenAI project key lives in `.env` in repo root. Current key ends `...Jhf6gA`. `.env` is gitignored.

### Carousel
5 slides, 3 visible desktop / 2 tablet / 1 mobile, auto-advance 5s.

### Hero banner
`linear-gradient(135deg, rgba(24,145,129,0.3), rgba(138,68,243,0.3))` — pastel teal → purple at 30% opacity.
