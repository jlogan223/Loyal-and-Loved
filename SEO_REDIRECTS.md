# Loyal & Loved — SEO Step 4 (Old URL Redirects)

_Last updated: 2026-04-16_

## What I found when I ran the audit

1. **Live site on the root is healthy.** `https://loyalandloved.co.uk/` returns
   HTTP 200 and the canonical tag is set correctly
   (`<link rel="canonical" href="https://loyalandloved.co.uk/">`).

2. **Old URLs already 404.** Every path that used to live under
   `/Loyal-and-Loved-FIXED/...` now returns a proper HTTP 404, e.g.
   `/Loyal-and-Loved-FIXED/`, `/Loyal-and-Loved-FIXED/index.html`,
   `/Loyal-and-Loved-FIXED/articles/best-pet-insurance-uk.html`, and every
   category path. These are being served by Cloudflare/GitHub Pages as
   genuine not-found responses — they are **not** being served as duplicate
   content.

3. **The local `Loyal-and-Loved-FIXED/` folder in your working copy is cruft.**
   It exists on your NAS but it is NOT in the `main` branch on GitHub. The
   remote is clean. Safe to delete locally when you want to.

4. **No references to `Loyal-and-Loved-FIXED` in the live `sitemap.xml` or
   `robots.txt`.** Clean.

5. **Sitemap at `/sitemap.xml` returns 200** and lists the correct root URLs.

### Verdict
You do not have a duplicate-content problem. You have a "Google might still
have a few of the old URLs in its index from before the rebuild" problem.
That is much smaller — Google will drop them organically within a few weeks
of repeated 404s — but we can speed it up with 301 redirects so any link
equity pointing at the old paths carries over to the new ones.

---

## The fix — one Cloudflare Bulk Redirect rule

Cloudflare Bulk Redirects with **subpath matching** lets a single rule
redirect every `/Loyal-and-Loved-FIXED/*` URL to its new root equivalent.

### Step-by-step (updated for Cloudflare 2026 dashboard)

**Part A — Create the redirect list**

1. Log in to **dash.cloudflare.com**.
2. Click the **loyalandloved.co.uk** zone to enter it.
3. In the left sidebar: **Rules → Settings**.
4. Click the **Bulk Redirects** tab at the top of the Settings page.
5. Under **Bulk Redirect Lists**, click **Create Bulk Redirect List**.
6. Fill in:
   - **List name:** `loyalandloved-old-paths`
   - **Description:** `Redirect legacy /Loyal-and-Loved-FIXED/* paths
     to root equivalents (301).`
7. Click **Next**.
8. Choose **"Or, manually add URL redirects"** (don't use CSV import
   for a single entry).
9. Enter the redirect:

   | Field | Value |
   | --- | --- |
   | **Source URL** | `https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/` |
   | **Target URL** | `https://loyalandloved.co.uk/` |
   | **Status** | `301` |

10. Click **Edit parameters** (small text below the fields) to expand
    the advanced options. Tick these:

    | Parameter | Setting |
    | --- | --- |
    | **Subpath matching** | ✅ On |
    | **Preserve path suffix** | ✅ On (should be on by default) |
    | **Preserve query string** | ✅ On |
    | **Include subdomains** | ❌ Off |

11. Click **Next** to review, then click **Continue to Redirect Rules**.

**Part B — Create the rule that activates the list**

12. You'll land on the **Create Bulk Redirect Rule** screen.
13. Fill in:
    - **Rule name:** `Apply old-paths redirects`
    - **Bulk Redirect List:** select `loyalandloved-old-paths` from
      the dropdown.
14. Leave the expression editor and rule key at their defaults.
15. Click **Save and Deploy**.

Within ~30 seconds, every `/Loyal-and-Loved-FIXED/...` URL on the live
site will return **HTTP 301** with a `Location:` header pointing to the
matching root path.

**Note:** Bulk Redirect Lists and Rules exist at the account level, so
they appear the same regardless of which zone you navigate from. If step
3 doesn't show a "Settings" option under Rules, try: click your account
name in the top-left → look for **Bulk Redirects** at the account level
instead.

### Verify after deploying
Paste these into a terminal (or a browser with DevTools → Network tab):

```
curl -I https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/best-pet-insurance-uk.html
# Expect: HTTP/2 301   location: https://loyalandloved.co.uk/articles/best-pet-insurance-uk.html

curl -I https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/
# Expect: HTTP/2 301   location: https://loyalandloved.co.uk/
```

---

## Fallback — per-URL list

If Cloudflare's subpath matching is disabled on your plan (it's on Free +
Pro + higher, so should be fine), or you'd rather be explicit, upload
this as a CSV under **Edit → Upload URLs**:

```
Source URL,Target URL,Status
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/,https://loyalandloved.co.uk/,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/index.html,https://loyalandloved.co.uk/,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/about.html,https://loyalandloved.co.uk/about.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/privacy-policy.html,https://loyalandloved.co.uk/privacy-policy.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/category/pet-insurance.html,https://loyalandloved.co.uk/category/pet-insurance.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/category/health-vet-care.html,https://loyalandloved.co.uk/category/health-vet-care.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/category/food-nutrition.html,https://loyalandloved.co.uk/category/food-nutrition.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/category/training-behaviour.html,https://loyalandloved.co.uk/category/training-behaviour.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/category/gear-tech.html,https://loyalandloved.co.uk/category/gear-tech.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/category/breed-guides.html,https://loyalandloved.co.uk/category/breed-guides.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/best-pet-insurance-uk.html,https://loyalandloved.co.uk/articles/best-pet-insurance-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/pet-insurance-cost-uk.html,https://loyalandloved.co.uk/articles/pet-insurance-cost-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/lifetime-vs-annual-pet-insurance.html,https://loyalandloved.co.uk/articles/lifetime-vs-annual-pet-insurance.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/best-cat-insurance-uk.html,https://loyalandloved.co.uk/articles/best-cat-insurance-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/vet-bills-uk.html,https://loyalandloved.co.uk/articles/vet-bills-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/flea-tick-worm-protection.html,https://loyalandloved.co.uk/articles/flea-tick-worm-protection.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/pet-dental-care.html,https://loyalandloved.co.uk/articles/pet-dental-care.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/senior-dog-care.html,https://loyalandloved.co.uk/articles/senior-dog-care.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/emergency-vet-costs-uk.html,https://loyalandloved.co.uk/articles/emergency-vet-costs-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/indoor-vs-outdoor-cats.html,https://loyalandloved.co.uk/articles/indoor-vs-outdoor-cats.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/best-fresh-dog-food-uk.html,https://loyalandloved.co.uk/articles/best-fresh-dog-food-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/best-dog-gps-tracker-uk.html,https://loyalandloved.co.uk/articles/best-dog-gps-tracker-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/puppy-first-year-checklist.html,https://loyalandloved.co.uk/articles/puppy-first-year-checklist.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/cost-of-owning-dog-uk.html,https://loyalandloved.co.uk/articles/cost-of-owning-dog-uk.html,301
https://loyalandloved.co.uk/Loyal-and-Loved-FIXED/articles/cockapoo-cost-uk.html,https://loyalandloved.co.uk/articles/cockapoo-cost-uk.html,301
```

This covers every page that ever existed inside the old subfolder.

---

## In Google Search Console

After the redirects are live, give Google a nudge:

1. Go to **Google Search Console → Pages** report.
2. If the "Not indexed" or "Not found (404)" bucket lists any
   `/Loyal-and-Loved-FIXED/...` URLs, select them and click **Validate
   Fix**. Google will recrawl; because they now return 301 → existing
   URLs, Search Console will consolidate them.
3. **URL Inspection → Request indexing** on the 5 most important pages
   (homepage, `/category/pet-insurance.html`,
   `/articles/best-pet-insurance-uk.html`,
   `/articles/pet-insurance-cost-uk.html`,
   `/articles/vet-bills-uk.html`). This pushes Google to re-crawl them
   with the new content.
4. **Sitemaps → Submit sitemap** (if not already): paste
   `https://loyalandloved.co.uk/sitemap.xml` and click Submit. If it's
   already submitted with a previous error, click the sitemap row and
   Submit again to force a recrawl.

---

## Local cleanup (optional, safe)

Your working folder at `C:\Users\Justin\Documents\Cloud\...\Loyal and Loved\`
still contains a `Loyal-and-Loved-FIXED/` archive subfolder (45 files).
It's not on the remote, not being served, and has no effect on the live
site. Safe to delete whenever you want to tidy up — nothing depends on it.

---

## Summary

**Step 4 status:** Old paths already 404 (the critical fail-safe). The
right permanent fix is a single Cloudflare Bulk Redirect with subpath
matching, which will convert those 404s to 301s for any search engine
or external link still pointing at the old `/Loyal-and-Loved-FIXED/`
paths. Instructions above; one rule, 30 seconds to deploy.
