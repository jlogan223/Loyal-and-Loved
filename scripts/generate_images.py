#!/usr/bin/env python3
"""
Generate images for the Loyal & Loved site using OpenAI's gpt-image-1.

Usage:
    python3 scripts/generate_images.py --tiers 1,2          # first wave
    python3 scripts/generate_images.py --tiers 1,2,3,4      # everything
    python3 scripts/generate_images.py --dry-run            # show prompts only
    python3 scripts/generate_images.py --limit 3            # only first 3 (sanity check)

Reads OPENAI_API_KEY from .env in the project root.
Skips any file already on disk so reruns are safe (unless --force is used).
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Run: pip install openai python-dotenv --break-system-packages")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("Run: pip install python-dotenv --break-system-packages")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

# Curated per-article prompts (optional). When a slug is in ARTICLE_PROMPTS
# we use that scene verbatim instead of the generic style template.
try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from prompts import ARTICLE_PROMPTS, BODY_PROMPTS, GLOBAL_RULES  # type: ignore
except Exception:
    ARTICLE_PROMPTS = {}
    BODY_PROMPTS = {}
    GLOBAL_RULES = ""

# Brand-aligned style prompts. These get prepended to each description.
_NO_TEXT = (
    " ABSOLUTELY NO TEXT, no lettering, no words, no captions, no signs, "
    "no labels, no logos, no watermarks, no writing of any kind anywhere "
    "in the image. Pure visual composition only."
)

STYLE_PROMPTS = {
    "photo": (
        "A high-quality, warm, natural-light photograph for a UK pet care website. "
        "Realistic, soft lighting, shallow depth of field, lifestyle photography. "
        "Friendly and trustworthy mood." + _NO_TEXT + " Subject: "
    ),
    "illustration": (
        "A soft, modern flat illustration for a UK pet care website. "
        "Cosy hand-drawn feel, gentle pastel colour palette featuring teal (#189181) "
        "and soft purple (#8A44F3), warm beige background, clean simple shapes, "
        "approachable and friendly." + _NO_TEXT + " Subject: "
    ),
}

# Image generation settings
MODEL = "gpt-image-1"
SIZE = "1024x1024"  # square — fits both card and hero crops well
QUALITY = "high"    # "low" ~$0.011/img, "medium" ~$0.04, "high" ~$0.17
                    # High is worth it for photorealism and to minimise
                    # garbled lettering — fallback to "medium" via --quality
                    # on reruns.


def build_prompt(entry: dict) -> str:
    """Build the final image prompt.

    Priority:
      1. Curated scene from prompts.ARTICLE_PROMPTS (keyed by article slug)
         — used whenever we have a bespoke brief for that article.
      2. Generic style template + placeholder description + global rules.
    """
    slug = entry.get("article_slug", "")
    position = entry.get("position", 0)
    # Hero images (tier 1/2 and category heroes tier 4) get the curated
    # treatment when available — all keyed by slug with position == 1.
    if position == 1 and slug in ARTICLE_PROMPTS:
        return ARTICLE_PROMPTS[slug]

    # Body images (tier 3, position >= 2) may have a bespoke scene keyed
    # by "{slug}-pos{position}" for high-risk compositions (brand logos,
    # documents, charts, packaging) — anywhere garbled text would betray
    # AI generation. Fall back to the generic template otherwise.
    body_key = f"{slug}-pos{position}"
    if body_key in BODY_PROMPTS:
        return BODY_PROMPTS[body_key]

    style = entry["style"]
    desc = entry["description"]
    if desc.lower().startswith("hero image"):
        slug_human = slug.replace("-", " ").title()
        desc = f"editorial-style image representing the topic '{slug_human}'"
    return STYLE_PROMPTS[style] + desc + GLOBAL_RULES


def generate_one(client: OpenAI, prompt: str, out_path: Path) -> bool:
    """Generate a single image. Returns True on success."""
    try:
        result = client.images.generate(
            model=MODEL,
            prompt=prompt,
            size=SIZE,
            quality=QUALITY,
            n=1,
        )
        b64 = result.data[0].b64_json
        if not b64:
            print(f"  ! No image data returned for {out_path.name}")
            return False
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(base64.b64decode(b64))
        return True
    except Exception as e:
        print(f"  ! Error for {out_path.name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tiers", default="1,2",
                        help="Comma-separated tiers to generate (1=home, 2=article hero, 3=body, 4=category)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Stop after N images (sanity-check runs)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print prompts without calling the API")
    parser.add_argument("--force", action="store_true",
                        help="Re-generate images that already exist on disk")
    parser.add_argument("--quality", choices=["low", "medium", "high"], default=QUALITY)
    args = parser.parse_args()

    tiers = {int(t.strip()) for t in args.tiers.split(",")}
    manifest_path = ROOT / "scripts" / "image_manifest.json"
    if not manifest_path.exists():
        print(f"Run extract_placeholders.py first.")
        sys.exit(1)

    manifest = json.loads(manifest_path.read_text())

    # Deduplicate: one entry per unique filename. Many cards across the homepage
    # and category pages share the same hero image. Prefer the article's own
    # hero entry (tier 2) over a card reference (tier 1/4) so we use the best
    # description for the prompt.
    tier_priority = {2: 0, 3: 1, 1: 2, 4: 3}
    seen: dict[str, dict] = {}
    for e in manifest:
        key = e["filename"]
        if key not in seen:
            seen[key] = e
        else:
            if tier_priority.get(e["tier"], 99) < tier_priority.get(seen[key]["tier"], 99):
                seen[key] = e
    unique = list(seen.values())

    # Keep only entries whose ORIGINATING tier is requested. An article hero
    # referenced from the homepage should still be generated when tier=2 is
    # selected, so we check against the full manifest's tiers per filename.
    requested_filenames = {
        e["filename"] for e in manifest if e["tier"] in tiers
    }
    todo = [e for e in unique if e["filename"] in requested_filenames]
    if args.limit:
        todo = todo[: args.limit]

    print(f"Plan: {len(todo)} images, tiers={sorted(tiers)}, quality={args.quality}")
    if args.dry_run:
        for e in todo:
            print(f"  → {e['filename']} [{e['style']}]: {build_prompt(e)[:120]}…")
        return

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not found. Add it to .env in the project root.")
        sys.exit(1)
    client = OpenAI(api_key=api_key)

    succeeded = 0
    skipped = 0
    failed = 0
    start = time.time()
    for i, entry in enumerate(todo, 1):
        out_path = ROOT / entry["filename"]
        if out_path.exists() and not args.force:
            print(f"[{i}/{len(todo)}] SKIP {entry['filename']} (exists)")
            skipped += 1
            continue
        prompt = build_prompt(entry)
        print(f"[{i}/{len(todo)}] GEN  {entry['filename']} [{entry['style']}]")
        if generate_one(client, prompt, out_path):
            succeeded += 1
        else:
            failed += 1

    elapsed = time.time() - start
    print(f"\nDone in {elapsed:.0f}s — {succeeded} generated, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
