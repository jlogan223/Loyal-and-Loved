#!/usr/bin/env python3
"""
After images are generated, swap [IMAGE: ...] placeholders in HTML files
for actual <img> tags pointing at the generated files.

Only swaps placeholders for which the image file actually exists on disk —
so it's safe to run after a partial generation, then again later.

Usage:
    python3 scripts/replace_placeholders.py             # dry-run (default)
    python3 scripts/replace_placeholders.py --apply     # write changes
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def make_img_tag(entry: dict) -> str:
    # Path is relative to the HTML file's directory.
    # index.html is at root, so just use the filename as-is.
    # articles/foo.html and category/foo.html are one level deep,
    # so they need ../ prefix.
    file_dir = Path(entry["file"]).parent
    img_path = entry["filename"]
    if str(file_dir) == ".":
        rel = img_path
    else:
        # Walk up the right number of levels
        depth = len(file_dir.parts)
        rel = ("../" * depth) + img_path
    alt = entry["description"].replace('"', "'")
    return (
        f'<img src="{rel}" alt="{alt}" '
        f'loading="lazy" decoding="async" '
        f'style="width:100%;height:100%;object-fit:cover;display:block;">'
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true",
                        help="Write changes to disk (default is dry-run)")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "scripts" / "image_manifest.json").read_text())

    # Group entries by source file for efficient editing
    by_file: dict[str, list[dict]] = {}
    for e in manifest:
        if (ROOT / e["filename"]).exists():
            by_file.setdefault(e["file"], []).append(e)

    if not by_file:
        print("No generated images found yet. Run generate_images.py first.")
        return

    total_swaps = 0
    for file_rel, entries in sorted(by_file.items()):
        path = ROOT / file_rel
        text = path.read_text(encoding="utf-8")
        original = text
        local_swaps = 0
        for e in entries:
            placeholder = e["placeholder"]
            img_tag = make_img_tag(e)
            if placeholder in text:
                text = text.replace(placeholder, img_tag, 1)
                local_swaps += 1
        if local_swaps == 0:
            continue
        total_swaps += local_swaps
        print(f"  {file_rel}: {local_swaps} swap(s)")
        if args.apply:
            path.write_text(text, encoding="utf-8")

    if args.apply:
        print(f"\nApplied {total_swaps} replacements.")
    else:
        print(f"\nDry run — would apply {total_swaps} replacements. Re-run with --apply.")


if __name__ == "__main__":
    main()
