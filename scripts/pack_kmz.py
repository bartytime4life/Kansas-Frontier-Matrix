#!/usr/bin/env python3
"""
post_pack_kmz.py — KML→KMZ post-processor & fixer

Use cases
---------
• You already produced a KML + local rasters/icons (e.g. from a regionation step).
  This script zips them into a clean KMZ, fixing hrefs and bundling assets.

• You have a KML directory (with doc.kml and subfiles). It will validate doc.kml,
  rewrite local paths to "files/<basename>", add the files/ payload to the KMZ,
  (optionally) strip remote <href> that point to http(s) if you want a fully self-contained KMZ.

What it does
------------
• Validates & parses doc.kml (or a given .kml file).
• Locates <Icon><href> and <Link><href> elements (GroundOverlay, ScreenOverlay, NetworkLink…).
• For local paths: copies into KMZ under "files/" and rewrites href to relative.
• For remote URLs: keeps them *by default* (Google Earth can stream them);
  pass --strip-remote to remove those nodes (for fully offline KMZ).
• Writes SHA256 and a tiny _meta.json next to the KMZ.

No external deps. Python 3.10+ only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import zipfile
from pathlib import Path
from typing import Iterable, Tuple
from xml.etree import ElementTree as ET

KML_NS = {"kml": "http://www.opengis.net/kml/2.2"}
HREF_XPATHS = [
    ".//kml:GroundOverlay/kml:Icon/kml:href",
    ".//kml:ScreenOverlay/kml:Icon/kml:href",
    ".//kml:NetworkLink/kml:Link/kml:href",
    ".//kml:Model/kml:Link/kml:href",
    ".//kml:Model/kml:ResourceMap/kml:Alias/kml:targetHref",
]

def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def _is_remote(s: str) -> bool:
    return bool(re.match(r"^(https?|s3|gs)://", s, re.IGNORECASE))

def _is_kmz(path: Path) -> bool:
    return path.suffix.lower() == ".kmz"

def _collect_hrefs(root: ET.Element) -> Iterable[ET.Element]:
    for xp in HREF_XPATHS:
        yield from root.findall(xp, KML_NS)

def _rewrite_local_hrefs(doc_dir: Path, root: ET.Element, assets: set[Path], strip_remote: bool) -> None:
    # Ensure <Document> exists
    if root.tag.endswith("kml"):
        doc = root.find("./kml:Document", KML_NS)
        if doc is None:
            raise ValueError("No <Document> element found in KML")
    # Rewrite hrefs
    nodes_to_remove: list[ET.Element] = []
    for href_node in _collect_hrefs(root):
        text = (href_node.text or "").strip()
        if not text:
            continue
        if _is_remote(text):
            if strip_remote:
                # remove the top overlay/networklink element that owns this href
                parent = href_node
                # climb a couple of levels to the named container
                for _ in range(3):
                    if parent is None or parent.getparent if hasattr(parent, "getparent") else None:
                        break
                # xml.etree has no getparent; fall back to removing the immediate parent of href's parent if known schema
                # Instead mark the parent of href_node to be pruned by calling code. Simpler: blank the href.
                href_node.text = ""
            # keep remote by default
            continue

        # Local path: resolve relative to doc_dir
        src = (doc_dir / text).resolve() if not os.path.isabs(text) else Path(text)
        if not src.exists():
            # Try also basename only from doc_dir
            candidate = (doc_dir / Path(text).name).resolve()
            if candidate.exists():
                src = candidate
            else:
                print(f"[WARN] missing asset referenced in href: {text}", file=sys.stderr)
                continue

        assets.add(src)
        href_node.text = f"files/{src.name}"

def _load_kml(kml_path: Path) -> ET.ElementTree:
    try:
        tree = ET.parse(kml_path)
        return tree
    except ET.ParseError as e:
        raise ValueError(f"KML parse error: {e}") from e

def _find_doc_kml(kml_input: Path) -> Tuple[Path, Path]:
    """
    Returns (doc_dir, kml_file).
    If --kml is a file, doc_dir = parent, kml_file = file.
    If --kml is a dir, tries doc.kml inside it.
    """
    if kml_input.is_file():
        return kml_input.parent.resolve(), kml_input.resolve()
    if kml_input.is_dir():
        k = kml_input / "doc.kml"
        if not k.exists():
            # fallback: single .kml in dir
            ks = list(kml_input.glob("*.kml"))
            if len(ks) == 1:
                k = ks[0]
            else:
                raise FileNotFoundError("No doc.kml (or unique .kml) found in directory")
        return kml_input.resolve(), k.resolve()
    raise FileNotFoundError(f"--kml path not found: {kml_input}")

def _write_kmz(out_dir: Path, kmz_name: str, kml_text: str, assets: Iterable[Path]) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    kmz_name = kmz_name if kmz_name.lower().endswith(".kmz") else f"{kmz_name}.kmz"
    kmz_path = out_dir / kmz_name
    with zipfile.ZipFile(kmz_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("doc.kml", kml_text)
        for a in assets:
            z.write(a, arcname=f"files/{a.name}")
    return kmz_path

def _write_sidecars(kmz_path: Path) -> None:
    (kmz_path.with_suffix(kmz_path.suffix + ".sha256")).write_text(_sha256(kmz_path))
    meta = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kmz": kmz_path.name,
        "size": kmz_path.stat().st_size,
        "command": " ".join(sys.argv),
    }
    (kmz_path.with_suffix(".meta.json")).write_text(json.dumps(meta, indent=2))

def main() -> int:
    ap = argparse.ArgumentParser(description="Package KML + local assets into a KMZ.")
    ap.add_argument("--kml", required=True, type=Path, help="KML file or directory containing doc.kml")
    ap.add_argument("--out", required=True, type=Path, help="Output directory for KMZ and sidecars")
    ap.add_argument("--kmz", default="overlay.kmz", help="Output KMZ filename")
    ap.add_argument("--strip-remote", action="store_true",
                    help="Strip remote http(s) hrefs (remove/blank them) to make fully offline KMZ")
    args = ap.parse_args()

    # If input is already a KMZ, just copy + sidecars
    if _is_kmz(args.kml):
        out_dir = args.out
        out_dir.mkdir(parents=True, exist_ok=True)
        kmz_path = out_dir / (args.kmz if args.kmz.endswith(".kmz") else f"{args.kmz}.kmz")
        kmz_path.write_bytes(Path(args.kml).read_bytes())
        _write_sidecars(kmz_path)
        print(f"[OK] Copied KMZ → {kmz_path}")
        return 0

    doc_dir, kml_file = _find_doc_kml(args.kml)
    tree = _load_kml(kml_file)
    root = tree.getroot()

    assets: set[Path] = set()
    _rewrite_local_hrefs(doc_dir, root, assets, strip_remote=args.strip_remote)

    # Pretty print (xml.etree doesn't pretty by default; keep compact)
    kml_text = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")

    kmz_path = _write_kmz(args.out, args.kmz, kml_text, sorted(assets))
    _write_sidecars(kmz_path)
    print(f"[OK] KMZ → {kmz_path} (assets: {len(assets)})")
    if args.strip_remote:
        print("[INFO] remote http(s) hrefs stripped")
    return 0

if __name__ == "__main__":
    sys.exit(main())
