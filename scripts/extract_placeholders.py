#!/usr/bin/env python3
"""
Scan all HTML files in the site, find [IMAGE: ...] placeholders,
and emit a manifest JSON the generator can consume.

Each entry includes:
  - file: source HTML path (relative to repo root)
  - line: line number of the placeholder
  - placeholder: the exact placeholder string (used for find/replace)
  - description: the human description from the placeholder
  - article_slug: slug (filename without .html) — used for naming
  - position: index of placeholder within file (1 = hero, 2+ = body)
  - tier: priority tier
      tier 1 = homepage carousel + Latest Guides cards (highest visibility)
      tier 2 = article hero images (clicked-through pages)
      tier 3 = in-article body images
      tier 4 = category page heroes
  - style: 'photo' for product comparison guides, 'illustration' for advice
  - filename: target filename inside images/articles/
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDER_RE = re.compile(r"\[IMAGE:\s*([^\]]+)\]")

# Articles classified as "product comparison" → photographic style.
# Everything else → illustration style.
PHOTO_ARTICLES = {
    "best-pet-insurance-uk",
    "best-cat-insurance-uk",
    "best-dog-gps-tracker-uk",
    "best-fresh-dog-food-uk",
    "pet-insurance-cost-uk",
    "lifetime-vs-annual-pet-insurance",
    "vet-bills-uk",
    "emergency-vet-costs-uk",
    "cost-of-owning-dog-uk",
    "cockapoo-cost-uk",
}


def style_for(slug: str) -> str:
    return "photo" if slug in PHOTO_ARTICLES else "illustration"


def tier_for(file_rel: str, position: int) -> int:
    if file_rel == "index.html":
        return 1  # homepage = highest visibility
    if file_rel.startswith("category/"):
        return 4
    # Articles
    if position == 1:
        return 2  # hero
    return 3  # in-article body


def safe_filename(file_rel: str, position: int, linked_slug: str | None = None) -> str:
    """Return a deterministic image path. One hero per article, shared across
    every placeholder that references that article (homepage cards, category
    cards, article hero). In-article body images remain unique."""
    if file_rel.startswith("articles/"):
        slug = Path(file_rel).stem
        # First image in an article file is the hero
        if position == 1:
            return f"images/articles/{slug}/hero.png"
        # Subsequent images are body content — unique per placeholder
        return f"images/articles/{slug}/body-{position - 1}.png"
    if file_rel == "index.html":
        # Homepage cards: use the linked article's hero image so the same
        # article always shows the same image everywhere.
        if linked_slug:
            return f"images/articles/{linked_slug}/hero.png"
        return f"images/home/{position}.png"
    if file_rel.startswith("category/"):
        # Category cards: use the linked article's hero if we can find one
        if linked_slug:
            return f"images/articles/{linked_slug}/hero.png"
        slug = Path(file_rel).stem
        return f"images/category/{slug}.png"
    return f"images/misc/{position}.png"


ARTICLE_LINK_RE = re.compile(r'articles/([a-z0-9\-]+)\.html')


def linked_article_slug(lines: list[str], start_idx: int, look_ahead: int = 15) -> str | None:
    """Look for an articles/<slug>.html link within `look_ahead` lines after
    the placeholder. Returns the slug or None."""
    end = min(len(lines), start_idx + look_ahead)
    for ln in lines[start_idx:end]:
        m = ARTICLE_LINK_RE.search(ln)
        if m:
            return m.group(1)
    return None


def main():
    manifest = []
    for html_path in sorted(ROOT.rglob("*.html")):
        # Skip the colour palette playground and any backup folders
        rel = html_path.relative_to(ROOT).as_posix()
        if rel.startswith("Loyal-and-Loved-FIXED/") or rel.startswith("colour-palettes"):
            continue
        lines = html_path.read_text(encoding="utf-8").splitlines()
        position = 0
        for lineno, line in enumerate(lines, start=1):
            m = PLACEHOLDER_RE.search(line)
            if not m:
                continue
            position += 1
            desc = m.group(1).strip()
            # strip leading "Placeholder — " noise if present
            desc = re.sub(r"^Placeholder\s*[—-]\s*", "", desc)
            file_slug = Path(rel).stem
            # For homepage / category placeholders, classify by the linked
            # article so a "Best Pet Insurance" card on the homepage gets
            # photo style even though index.html itself isn't a product page.
            linked = linked_article_slug(lines, lineno) if rel != f"articles/{file_slug}.html" else None
            classify_slug = linked or file_slug
            manifest.append({
                "file": rel,
                "line": lineno,
                "placeholder": m.group(0),
                "description": desc,
                "article_slug": file_slug,
                "linked_article": linked,
                "position": position,
                "tier": tier_for(rel, position),
                "style": style_for(classify_slug),
                "filename": safe_filename(rel, position, linked),
            })

    out = ROOT / "scripts" / "image_manifest.json"
    out.write_text(json.dumps(manifest, indent=2))
    print(f"Wrote {len(manifest)} entries to {out.relative_to(ROOT)}")
    # Tier breakdown
    from collections import Counter
    tier_counts = Counter(e["tier"] for e in manifest)
    style_counts = Counter(e["style"] for e in manifest)
    print(f"  Tier breakdown: {dict(sorted(tier_counts.items()))}")
    print(f"  Style breakdown: {dict(style_counts)}")


if __name__ == "__main__":
    main()
