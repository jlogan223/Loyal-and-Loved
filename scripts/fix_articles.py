#!/usr/bin/env python3
"""
Article page fix-ups:

  1. Rewrite the related-articles block at the bottom of every article
     to use real hero images from `images/articles/{slug}/hero.png`
     plus real titles / excerpts / links from LNL_ARTICLES. Picks
     related articles via same-category match, padded with other
     featured articles if the category has fewer than 3 siblings.

  2. Rewrite the sidebar Quick Links ToC in every article to point at
     the actual `<section id="...">` anchors, using the first `<h2>`
     inside each section as the label.

Dry-run by default — pass --apply to write.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# ---------- registry ----------

def parse_articles_registry() -> list[dict]:
    src = (ROOT / "js" / "articles.js").read_text(encoding="utf-8")
    m = re.search(r"window\.LNL_ARTICLES\s*=\s*(\[.*?\n\]);", src, re.DOTALL)
    if not m:
        raise SystemExit("Could not find LNL_ARTICLES array in js/articles.js")
    arr_src = m.group(1)
    arr_src = re.sub(r"//[^\n]*", "", arr_src)
    arr_src = re.sub(r"([\{,\[]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:", r'\1"\2":', arr_src)
    arr_src = re.sub(r",(\s*[\]}])", r"\1", arr_src)
    return json.loads(arr_src)


def related_for(slug: str, articles: list[dict], limit: int = 3) -> list[dict]:
    current = next((a for a in articles if a["slug"] == slug), None)
    if not current:
        return []
    same_cat = [a for a in articles if a["category"] == current["category"] and a["slug"] != slug]
    picks = same_cat[:limit]
    if len(picks) < limit:
        # Pad with featured articles from other categories
        featured_others = [
            a for a in articles
            if a.get("featured") and a["slug"] != slug and a not in picks
        ]
        picks.extend(featured_others[: limit - len(picks)])
    return picks[:limit]


# ---------- related-articles block ----------

# Matches the existing <section class="related-articles">...</section>
RELATED_RE = re.compile(
    r'<section class="related-articles">.*?</section>',
    re.DOTALL,
)


def build_related_block(picks: list[dict]) -> str:
    cards = []
    for a in picks:
        slug = a["slug"]
        cards.append(
            '      <article class="related-article-card">\n'
            f'        <a href="./{slug}.html" style="text-decoration: none; color: inherit; display: block;">\n'
            f'          <img src="../images/articles/{slug}/hero.png" alt="{a["title"]}" loading="lazy" decoding="async">\n'
            '          <div class="card-content">\n'
            f'            <h3>{a["title"]}</h3>\n'
            f'            <p>{a["excerpt"]}</p>\n'
            '            <span class="card-cta">Read <span class="arrow" aria-hidden="true">→</span></span>\n'
            '          </div>\n'
            '        </a>\n'
            '      </article>'
        )
    cards_html = "\n".join(cards)
    return (
        '<section class="related-articles">\n'
        '          <h2>Related Guides</h2>\n'
        '          <div class="related-articles-grid">\n'
        f'{cards_html}\n'
        '          </div>\n'
        '        </section>'
    )


# ---------- sidebar ToC ----------

# Matches the <div class="sidebar-widget"> that contains <h3>Quick Links</h3>
SIDEBAR_QUICKLINKS_RE = re.compile(
    r'(<div class="sidebar-widget">\s*<h3>Quick Links</h3>\s*<ul>)(.*?)(</ul>\s*</div>)',
    re.DOTALL,
)

# Extracts the body of each <section id="xxx"> ... </section>. We then
# find the first heading (h2, then h3, then h4) inside to use as the
# sidebar label. Matching contents *within* the section avoids leaking
# into the next section's <h2> when a section only has an <h3>.
SECTION_RE = re.compile(
    r'<section\s+id="([^"]+)"[^>]*>(.*?)</section>',
    re.DOTALL,
)
HEADING_RE = re.compile(r'<h[234][^>]*>(.*?)</h[234]>', re.DOTALL)


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).strip()


def extract_toc(text: str) -> list[tuple[str, str]]:
    """Return [(id, label), ...] for each <section id="..."> in the article.

    The label is the first <h2>/<h3>/<h4> inside that section's body."""
    items: list[tuple[str, str]] = []
    for m in SECTION_RE.finditer(text):
        sec_id = m.group(1)
        body = m.group(2)
        # Skip "related" sections — they're not content
        if "related" in sec_id.lower():
            continue
        h = HEADING_RE.search(body)
        if not h:
            continue
        label = strip_tags(h.group(1))
        if not label:
            continue
        items.append((sec_id, label))
    return items


def build_sidebar_toc(items: list[tuple[str, str]]) -> str:
    lis = "\n".join(f'          <li><a href="#{sid}">{label}</a></li>' for sid, label in items)
    return (
        '<div class="sidebar-widget">\n'
        '        <h3>Quick Links</h3>\n'
        '        <ul>\n'
        f'{lis}\n'
        '        </ul>\n'
        '      </div>'
    )


# ---------- main pass ----------

def rewrite_article(path: Path, articles: list[dict]) -> tuple[str, int, list[str]]:
    original = path.read_text(encoding="utf-8")
    text = original
    changes = 0
    notes: list[str] = []
    slug = path.stem

    # 1. Related-articles block
    picks = related_for(slug, articles, limit=3)
    if picks:
        new_block = build_related_block(picks)
        new_text, n = RELATED_RE.subn(new_block, text, count=1)
        if n == 0:
            notes.append("related-articles block not matched")
        else:
            text = new_text
            changes += 1

    # 2. Sidebar ToC
    toc_items = extract_toc(text)
    if toc_items:
        new_sidebar = build_sidebar_toc(toc_items)
        new_text, n = SIDEBAR_QUICKLINKS_RE.subn(
            # Replace the WHOLE widget div (opening + ul + closing div)
            new_sidebar,
            text,
            count=1,
        )
        if n == 0:
            notes.append("sidebar Quick Links widget not matched")
        else:
            text = new_text
            changes += 1
    else:
        notes.append("no <section id=...> anchors found — ToC not rewritten")

    return text, changes, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="Write changes to disk (default: dry-run)")
    args = ap.parse_args()

    articles = parse_articles_registry()
    print(f"Loaded {len(articles)} articles from registry.\n")

    total_changes = 0
    for art_file in sorted((ROOT / "articles").glob("*.html")):
        slug = art_file.stem
        new_text, changes, notes = rewrite_article(art_file, articles)
        if changes or notes:
            print(f"  {art_file.relative_to(ROOT)}: {changes} change(s)")
            for n in notes:
                print(f"    ! {n}")
            if args.apply and changes:
                art_file.write_text(new_text, encoding="utf-8")
            total_changes += changes

    print(f"\n{'Applied' if args.apply else 'Would apply'} {total_changes} change(s).")


if __name__ == "__main__":
    main()
