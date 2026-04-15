#!/usr/bin/env python3
"""
End-to-end site fix-up pass for Loyal & Loved.

1. Parse js/articles.js to get the LNL_ARTICLES registry.
2. For every category page under category/*.html:
    - Replace TITLE_PLACEHOLDER with the correct ampersand.
    - Replace the hardcoded placeholder article card with real cards
      for every article in that category (clickable <a class="article-card">).
3. Fix stale "Pet & Proud" branding to "Loyal & Loved" across every
   HTML file at the site root + articles/ + category/.
4. Fix carousel viewport clipping in css/style.css.

Dry-run by default (no --apply).
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CATEGORY_LABELS = {
    "pet-insurance": "Pet Insurance",
    "health-vet-care": "Health &amp; Vet Care",
    "food-nutrition": "Food &amp; Nutrition",
    "training-behaviour": "Training &amp; Behaviour",
    "gear-tech": "Gear &amp; Tech",
    "breed-guides": "Breed Guides",
}

# Plain (non-entity) ampersand version — used in <h1> and breadcrumb where
# a literal '&' is fine in HTML text content (the browser parses it as an
# ampersand character). Using the entity is still valid but less readable.
CATEGORY_LABELS_PLAIN = {
    k: v.replace("&amp;", "&") for k, v in CATEGORY_LABELS.items()
}

# Short badge label that sits on each article card. Keeps cards compact.
CATEGORY_BADGE = {
    "pet-insurance": "Pet Insurance",
    "health-vet-care": "Vet Care",
    "food-nutrition": "Food",
    "training-behaviour": "Training",
    "gear-tech": "Gear",
    "breed-guides": "Breed Guide",
}


def parse_articles_registry() -> list[dict]:
    """Extract LNL_ARTICLES from js/articles.js without needing a JS runtime."""
    src = (ROOT / "js" / "articles.js").read_text(encoding="utf-8")
    m = re.search(r"window\.LNL_ARTICLES\s*=\s*(\[.*?\n\]);", src, re.DOTALL)
    if not m:
        raise SystemExit("Could not find LNL_ARTICLES array in js/articles.js")
    arr_src = m.group(1)
    # Convert JS object literal to JSON:
    #   - Strip // line comments
    #   - Quote bare keys: key: → "key":
    #   - Strip trailing commas before } or ]
    arr_src = re.sub(r"//[^\n]*", "", arr_src)
    arr_src = re.sub(r"([\{,\[]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:", r'\1"\2":', arr_src)
    arr_src = re.sub(r",(\s*[\]}])", r"\1", arr_src)
    # "Petplan": "" etc already uses double-quoted strings.
    # The JS file uses HTML entities like "Loyal &amp; Loved" which JSON
    # accepts as plain strings.
    try:
        return json.loads(arr_src)
    except json.JSONDecodeError as e:
        snippet = arr_src[max(0, e.pos - 60):e.pos + 60]
        raise SystemExit(f"JSON parse failed: {e}\n---\n{snippet}\n---")


def build_article_card(article: dict) -> str:
    """Render a single article card <a> matching the homepage pattern."""
    slug = article["slug"]
    title = article["title"]
    excerpt = article["excerpt"]
    read_time = article["readTime"]
    category = article["category"]
    badge = CATEGORY_BADGE.get(category, category.title())
    hero = f"../images/articles/{slug}/hero.png"
    # Escape any stray angle brackets in title / excerpt — our registry
    # entries don't contain them, but be defensive.
    title_html = title
    excerpt_html = excerpt
    return (
        f'      <a class="article-card fade-in" href="../articles/{slug}.html">\n'
        f'        <div class="article-card-image">\n'
        f'          <img src="{hero}" alt="{title_html}" loading="lazy" decoding="async">\n'
        f'        </div>\n'
        f'        <div class="article-card-content">\n'
        f'          <span class="article-badge">{badge}</span>\n'
        f'          <h3>{title_html}</h3>\n'
        f'          <p>{excerpt_html}</p>\n'
        f'          <div class="article-meta">\n'
        f'            <span class="read-time">{read_time}</span>\n'
        f'            <span class="card-cta">Read <span class="arrow" aria-hidden="true">→</span></span>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'      </a>'
    )


ARTICLE_GRID_RE = re.compile(
    r'(<div class="article-grid category-articles">)(.*?)(</div>\s*<div class="category-affiliate-cta">)',
    re.DOTALL,
)


def rewrite_category_page(path: Path, articles: list[dict]) -> tuple[str, int]:
    """Return the (new_content, change_count) for a category HTML file."""
    original = path.read_text(encoding="utf-8")
    text = original
    changes = 0
    slug = path.stem  # e.g. "health-vet-care"

    # 1. TITLE_PLACEHOLDER → & / &amp;
    # The three occurrences are all inside text content: <title>, breadcrumb
    # <span>, and <h1>. HTML allows & as a character only when unambiguous,
    # so use &amp; everywhere to be safe.
    if "TITLE_PLACEHOLDER" in text:
        text = text.replace("TITLE_PLACEHOLDER", "&amp;")
        changes += 1

    # 2. Rebuild the article grid for this category.
    cat_articles = [a for a in articles if a["category"] == slug]
    if cat_articles:
        cards_html = "\n\n".join(build_article_card(a) for a in cat_articles)
        new_block = (
            '<div class="article-grid category-articles">\n'
            f'{cards_html}\n'
            '    </div>\n\n    <div class="category-affiliate-cta">'
        )
        new_text, n = ARTICLE_GRID_RE.subn(
            new_block, text, count=1
        )
        if n == 0:
            # Pattern didn't match — log it, don't silently skip.
            print(f"    ! {path.relative_to(ROOT)}: article-grid block not matched")
        else:
            text = new_text
            changes += len(cat_articles)

    # 3. Fix "Pet & Proud" stale branding. "Pet & Proud UK" → "Loyal & Loved
    #    UK", "Pet & Proud Team" → "Loyal & Loved Team", "About Pet & Proud"
    #    → "About Loyal & Loved".
    for old, new in [
        ("Pet & Proud UK", "Loyal &amp; Loved UK"),
        ("About Pet & Proud", "About Loyal &amp; Loved"),
        ("Pet & Proud Team", "Loyal &amp; Loved Team"),
        ("Pet & Proud", "Loyal &amp; Loved"),
    ]:
        if old in text:
            text = text.replace(old, new)
            changes += 1

    return text, changes


def rewrite_article_page(path: Path) -> tuple[str, int]:
    """Lighter pass for articles/*.html — just fix stale branding."""
    original = path.read_text(encoding="utf-8")
    text = original
    changes = 0
    for old, new in [
        ("Pet & Proud UK", "Loyal &amp; Loved UK"),
        ("About Pet & Proud", "About Loyal &amp; Loved"),
        ("Pet & Proud Team", "Loyal &amp; Loved Team"),
        ("Pet & Proud", "Loyal &amp; Loved"),
    ]:
        if old in text:
            text = text.replace(old, new)
            changes += 1
    return text, changes


def fix_carousel_css(css_path: Path) -> tuple[str, int]:
    """Adjust the carousel viewport so the hover-lift and box-shadow on
    carousel cards aren't clipped at top/bottom or along the horizontal
    edges. We switch overflow to overflow-x: clip / overflow-y: visible and
    add vertical padding so the shadow has room to render."""
    original = css_path.read_text(encoding="utf-8")
    new = original
    # Find the .carousel-viewport block.
    pattern = re.compile(
        r"\.carousel-viewport\s*\{\s*overflow:\s*hidden;\s*position:\s*relative;\s*\}",
        re.DOTALL,
    )
    replacement = (
        ".carousel-viewport {\n"
        "  /* Clip slides horizontally as they transform, but leave vertical\n"
        "     overflow visible so the card hover-lift and box-shadow aren't\n"
        "     cut off at the top or bottom edge. */\n"
        "  overflow-x: clip;\n"
        "  overflow-y: visible;\n"
        "  position: relative;\n"
        "  padding: 8px 4px 24px;\n"
        "  margin: -8px -4px -24px;\n"
        "}"
    )
    new, n = pattern.subn(replacement, new, count=1)
    return new, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="Write changes to disk (default is dry-run)")
    args = ap.parse_args()

    articles = parse_articles_registry()
    print(f"Loaded {len(articles)} articles from registry.")
    by_cat: dict[str, int] = {}
    for a in articles:
        by_cat[a["category"]] = by_cat.get(a["category"], 0) + 1
    for k, v in sorted(by_cat.items()):
        print(f"  {k}: {v}")

    total_changes = 0

    # Category pages
    print("\n--- Category pages ---")
    for cat_file in sorted((ROOT / "category").glob("*.html")):
        new_text, changes = rewrite_category_page(cat_file, articles)
        if changes:
            print(f"  {cat_file.relative_to(ROOT)}: {changes} change(s)")
            if args.apply:
                cat_file.write_text(new_text, encoding="utf-8")
            total_changes += changes

    # Article pages
    print("\n--- Article pages (branding only) ---")
    for art_file in sorted((ROOT / "articles").glob("*.html")):
        new_text, changes = rewrite_article_page(art_file)
        if changes:
            print(f"  {art_file.relative_to(ROOT)}: {changes} change(s)")
            if args.apply:
                art_file.write_text(new_text, encoding="utf-8")
            total_changes += changes

    # Carousel CSS
    print("\n--- CSS ---")
    css_path = ROOT / "css" / "style.css"
    new_css, n = fix_carousel_css(css_path)
    if n:
        print(f"  {css_path.relative_to(ROOT)}: carousel-viewport block updated")
        if args.apply:
            css_path.write_text(new_css, encoding="utf-8")
        total_changes += 1
    else:
        print(f"  {css_path.relative_to(ROOT)}: carousel-viewport pattern not matched (already updated?)")

    print(f"\n{'Applied' if args.apply else 'Would apply'} {total_changes} change(s).")


if __name__ == "__main__":
    main()
