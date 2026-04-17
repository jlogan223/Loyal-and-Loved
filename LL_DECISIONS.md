# LL_DECISIONS.md — Loyal & Loved Locked Decisions

> Confirmed decisions. Do NOT deviate without explicit instruction from
> Justin. These are rules, not notes.
>
> **Note:** Separate from the AffiliateStudio `DECISIONS.md` in this same
> folder. This file governs the Loyal & Loved website only.

_Last updated: 2026-04-16_

---

## Editorial & brand

- **British English always.** Spellings, date formats (DD/MM/YYYY in prose,
  ISO in filenames/memory), £ currency, UK-specific terminology
  (e.g. "vet", not "veterinarian"; "fortnight", not "two weeks"; "pavement",
  not "sidewalk").
- **Honest editorial tone.** No clickbait, no coupon-site tactics, no
  trademark bidding on brand PPC terms, no fake urgency.
- **Transparent disclosure.** Every article that contains an affiliate
  link has a disclosure above the fold explaining how the site earns.
- **No PPC or paid traffic.** Organic-only (SEO, content, email later).
- **Long-form buyer guides only.** Commercial intent at point of purchase —
  comparison tables, cost breakdowns, use-case recommendations. Not news
  filler, not thin listicles.

## Affiliate link hygiene

- **Every affiliate link must carry `rel="sponsored nofollow"`.** No
  exceptions. Also add `target="_blank" rel="sponsored nofollow noopener"`
  for external opens.
- **Charities (PDSA, Blue Cross, Battersea) get unaffiliated links** when
  cited for charitable services. Exception: PDSA Pet Insurance is a
  **commercial** Awin programme — if linked, frame explicitly as "buying
  an insurance product that funds their charitable vet work," not as a
  donation.
- **"Link Coming Soon" placeholder spans** stay in place until Awin /
  Impact / direct programme is approved for that brand, then swap in the
  deep link.
- **Verify every target URL before wiring.** Before adding any affiliate
  link to an article, confirm via WebFetch that the target page actually
  exists and returns 200. No guessing URLs from brand site structure.

## Ethics flags (hard rules)

- **DO NOT wire Purina affiliate links** (Awin ID 24465) even if the
  application is approved. Keep the approval (zero cost to hold) but
  don't place any buy buttons. If Purina must be mentioned editorially
  for comparison context, link to Zooplus or Amazon instead. **Why:** FDA
  has 1,705 consumer adverse-event reports and 206 pet-death reports;
  active class-action lawsuit; $550M sales drop 2025. Revisit only if
  the picture changes cleanly over 6–12 months.
- **DISCLOSE the Nestlé Purina ownership of Tails.com** in any article
  that recommends Tails.com. One line is sufficient (e.g. "owned by
  Nestlé Purina since 2018"). Never recommend Tails.com in the same
  article that criticises Purina without acknowledging the link.
- **Frame PDSA Pet Insurance as commercial**, not charitable. Readers
  must not believe they are "donating" by clicking the affiliate link —
  they are buying an insurance policy that happens to fund PDSA's vet
  work.
- **Barking Heads & Meowing Heads amber flag.** Do not promote them as
  "certified cruelty-free" without per-product verification — PETA
  listing is partial and FEDIAF compliance is not explicit.

## Tech stack (fixed)

- **Static site.** Vanilla HTML/CSS/JS. No framework, no build step,
  no bundler.
- **Hosted on GitHub Pages** from `main` branch root of
  `https://github.com/jlogan223/Loyal-and-Loved`.
- **Cloudflare** for DNS, CDN, bulk redirects, and cache. Apex domain
  `loyalandloved.co.uk`.
- **Client-side article registry** in `js/articles.js` as the
  `LNL_ARTICLES` array. Adding an article = edit this file + create the
  HTML under `articles/`.
- **Images 1024×1024** generated via OpenAI `gpt-image-1`. Use
  aspect-ratio containers so they render responsively.
- **Canonical URLs always set** in `<head>` of every page.
- **Site verification meta tags** (e.g. Impact.com
  `impact-site-verification`) go inside the `<head>` of `index.html`
  only, between the canonical link and the stylesheets.

## Git workflow (mandatory)

- **Local mount has a jammed `.git/index.lock`** due to FUSE bindfs
  blocking `unlink`. Do not attempt to commit from
  `/sessions/elegant-intelligent-mayer/mnt/Loyal and Loved/` directly.
- **Use the fresh clone at `/sessions/elegant-intelligent-mayer/push-clone/`.**
  PAT is embedded in the remote URL, so pushes from the sandbox work.
- **Sequence for every change:**
  1. Edit the file in `mnt/Loyal and Loved/` (canonical source).
  2. `cp` the file to the matching path in `push-clone/`.
  3. `git add`, `git commit`, `git push` from `push-clone/`.
  4. Ask Justin to **purge the Cloudflare cache** so the change goes
     live on the CDN.
- **Never force-push, never rewrite history, never bypass hooks.**

## Cloudflare cache

- **After every git push that affects site output**, Justin purges cache
  via `dash.cloudflare.com → loyalandloved.co.uk → Caching → Configuration
  → Purge Everything`. Without this, CDN-cached HTML may lag the deploy
  by hours.

## Accounts & handles (single source of truth)

- **PB Eng Ltd** is the UK Ltd company that owns the site and all
  affiliate accounts.
- **Amazon Associates UK:** tag `pinaffacc-21`.
- **Awin publisher account** active as of 2026-04-16.
- **Impact.com publisher account** active as of 2026-04-16 (verification
  tag deployed commit `b26bb0f`).
- **Primary contact email for applications:** `pbengukltd@gmail.com`.
- **Site contact mailbox `contact@loyalandloved.co.uk`** — to be created
  (backlog).
