#!/usr/bin/env python3
# scripts/pack_kmz.py
"""
pack_kmz.py — KML→KMZ post-processor & fixer (no external deps; Python 3.9+)

Use cases
---------
• You already produced a KML + local rasters/icons (e.g., from regionation).
  This script zips them into a clean KMZ, fixing hrefs and bundling assets.

• You have a KML directory (with doc.kml and subfiles). It will validate doc.kml,
  rewrite local paths to "files/<basename>" (or --prefix), add the files/ payload
  to the KMZ, and (optionally) strip remote http(s) hrefs for fully offline use.

What it does
------------
• Validates & parses doc.kml (or a given .kml file).
• Locates hrefs in common places (Overlays, NetworkLinks, Models/ResourceMap,
  PhotoOverlay, and IconStyles; including legacy <Url> and gx: elements).
• For LOCAL paths: copies into KMZ under prefix/ and rewrites href to relative.
• For REMOTE URLs: keeps by default (Google Earth can stream them);
  pass --strip-remote to REMOVE the owning feature (Overlay/NetworkLink/Model/PhotoOverlay),
  or --blank-remote to blank the href but keep the node.
• Optionally bundle extra files via --extra 'glob'.

Outputs
-------
• KMZ (doc.kml at root + assets under <prefix>/).
• <kmz>.sha256 and <kmz>.meta.json (size, timestamp, argv).

Examples
--------
  # Directory with doc.kml + local assets → my_overlay.kmz
  python scripts/pack_kmz.py --kml out/regionated --out dist --kmz my_overlay.kmz

  # Single KML file with relative pngs → KMZ with prefix 'files'
  python scripts/pack_kmz.py --kml out/doc.kml --out dist --prefix files

  # Fully offline: strip remote hrefs and keep only local
  python scripts/pack_kmz.py --kml out/regionated --out dist --strip-remote

  # Include additional files not referenced by hrefs
  python scripts/pack_kmz.py --kml out/regionated --out dist --extra "out/regionated/**/*.dae"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import zipfile
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

# Namespaces
KML_NS_URI = "http://www.opengis.net/kml/2.2"
GX_NS_URI = "http://www.google.com/kml/ext/2.2"
KML_NS = {"kml": KML_NS_URI, "gx": GX_NS_URI}

# Common href locations we care about
HREF_XPATHS = (
    # Overlays
    ".//kml:GroundOverlay/kml:Icon/kml:href",
    ".//kml:ScreenOverlay/kml:Icon/kml:href",
    ".//kml:PhotoOverlay/kml:Icon/kml:href",
    # NetworkLink (KML 2.2 and legacy)
    ".//kml:NetworkLink/kml:Link/kml:href",
    ".//kml:NetworkLink/kml:Url/kml:href",
    # Model/ResourceMap
    ".//kml:Model/kml:Link/kml:href",
    ".//kml:Model/kml:ResourceMap/kml:Alias/kml:targetHref",
    # Styles that point to icons
    ".//kml:Style/kml:IconStyle/kml:Icon/kml:href",
)

# Owning feature tags we may remove if strip-remote is set
OWNER_TAGS = (
    f"{{{KML_NS_URI}}}GroundOverlay",
    f"{{{KML_NS_URI}}}ScreenOverlay",
    f"{{{KML_NS_URI}}}PhotoOverlay",
    f"{{{KML_NS_URI}}}NetworkLink",
    f"{{{KML_NS_URI}}}Model",
)

REMOTE_SCHEMES = ("http", "https", "s3", "gs")


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def _sha256(p: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def _is_remote(s: str) -> bool:
    try:
        pr = urlparse(s.strip())
        return pr.scheme.lower() in REMOTE_SCHEMES
    except Exception:
        return False


def _is_kmz(path: Path) -> bool:
    return path.suffix.lower() == ".kmz"


def _build_parent_map(root: ET.Element) -> Dict[ET.Element, ET.Element]:
    """xml.etree doesn’t expose getparent(); build a parent map."""
    return {child: parent for parent in root.iter() for child in parent}


def _collect_href_nodes(root: ET.Element) -> List[ET.Element]:
    out: List[ET.Element] = []
    for xp in HREF_XPATHS:
        out.extend(root.findall(xp, KML_NS))
    # Try gx Icon hrefs if present
    try:
        out.extend(root.findall(".//kml:Style/gx:IconStyle/kml:Icon/kml:href", KML_NS))
    except Exception:
        pass
    return out


def _find_owner(node: ET.Element, parents: Dict[ET.Element, ET.Element]) -> Optional[ET.Element]:
    """Walk upward to the nearest known owner feature (Overlay/NetworkLink/Model)."""
    cur = node
    for _ in range(12):  # deep enough for most trees
        parent = parents.get(cur)
        if parent is None:
            return None
        if parent.tag in OWNER_TAGS:
            return parent
        cur = parent
    return None


def _project_root_from(kml_path: Path) -> Path:
    # Heuristic: 2 levels up for stac/items/… style; else nearest dir with a repo marker if present
    for parent in [kml_path.parent] + list(kml_path.parents):
        for marker in (".git", "pyproject.toml", "README.md"):
            if (parent / marker).exists():
                return parent
    return kml_path.parents[2] if len(kml_path.parents) >= 2 else kml_path.parent


def _resolve_local_asset(base_dir: Path, href_text: str, item_path: Path) -> Optional[Path]:
    """
    Try to resolve a local file:
      - file:// path → use
      - absolute path → use if exists
      - relative path → base_dir / href
      - "data/..." → repo-root / href
      - last resort → base_dir / basename(href)
    """
    s = (href_text or "").strip()
    if not s:
        return None
    pr = urlparse(s)
    if pr.scheme.lower() == "file":
        p = Path(pr.path)
        return p if p.exists() else None
    p = Path(s)
    if p.is_absolute():
        return p if p.exists() else None
    if s.startswith("data/"):
        root = _project_root_from(item_path)
        cand = (root / s).resolve()
        return cand if cand.exists() else None
    cand = (base_dir / s).resolve()
    if cand.exists():
        return cand
    alt = (base_dir / p.name).resolve()
    return alt if alt.exists() else None


# ---------------------------------------------------------------------------
# KML processing
# ---------------------------------------------------------------------------

def _read_kml_name(root: ET.Element) -> Optional[str]:
    # Prefer Document/name, fallback to root name
    nm = root.find("./kml:Document/kml:name", KML_NS)
    if nm is not None and (nm.text or "").strip():
        return nm.text.strip()
    nm = root.find("./kml:name", KML_NS)
    if nm is not None and (nm.text or "").strip():
        return nm.text.strip()
    return None


def rewrite_hrefs(
    item_path: Path,
    doc_dir: Path,
    root: ET.Element,
    *,
    prefix: str,
    strip_remote: bool,
    blank_remote: bool,
) -> List[Path]:
    """
    Rewrite local hrefs to <prefix>/<basename>; collect assets to include.
    Handle remote hrefs per flags.
    """
    assets: List[Path] = []
    parents = _build_parent_map(root)
    href_nodes = _collect_href_nodes(root)

    # Validate top-level document presence
    if root.tag.endswith("kml"):
        doc = root.find("./kml:Document", KML_NS)
        if doc is None:
            raise ValueError("No <Document> element found in KML")

    owners_to_remove: List[ET.Element] = []
    owners_seen: set[ET.Element] = set()

    for href_node in href_nodes:
        text = (href_node.text or "").strip()
        if not text:
            continue

        if _is_remote(text):
            if strip_remote:
                owner = _find_owner(href_node, parents)
                if owner is not None and owner not in owners_seen:
                    owners_to_remove.append(owner)
                    owners_seen.add(owner)
                else:
                    # No known owner – safest fallback: blank
                    href_node.text = ""
            elif blank_remote:
                href_node.text = ""
            # else keep as-is
            continue

        # Local asset
        src = _resolve_local_asset(doc_dir, text, item_path)
        if not src:
            sys.stderr.write(f"[WARN] missing local asset referenced in href: {text}\n")
            continue

        # record + rewrite
        if src not in assets:
            assets.append(src)
        href_node.text = f"{prefix}/{src.name}"

    # Remove owners of stripped remotes (with the original parent map)
    for owner in owners_to_remove:
        parent = parents.get(owner)
        if parent is not None:
            parent.remove(owner)

    return assets


# ---------------------------------------------------------------------------
# IO / ZIP
# ---------------------------------------------------------------------------

def find_doc_kml(kml_input: Path) -> Tuple[Path, Path]:
    """
    Returns (doc_dir, kml_file).
    If --kml is a file, doc_dir = parent, kml_file = file.
    If --kml is a dir, tries doc.kml inside it (or unique *.kml).
    """
    if kml_input.is_file():
        return kml_input.parent.resolve(), kml_input.resolve()
    if kml_input.is_dir():
        k = kml_input / "doc.kml"
        if not k.exists():
            ks = list(kml_input.glob("*.kml"))
            if len(ks) == 1:
                k = ks[0]
            elif len(ks) == 0:
                raise FileNotFoundError(f"No doc.kml (or any .kml) found in {kml_input}")
            else:
                raise FileNotFoundError(f"Multiple .kml files in {kml_input}; please specify --kml <file.kml>")
        return kml_input.resolve(), k.resolve()
    raise FileNotFoundError(f"--kml path not found: {kml_input}")


def load_kml(kml_path: Path) -> ET.ElementTree:
    try:
        return ET.parse(kml_path)
    except ET.ParseError as e:
        raise ValueError(f"KML parse error in {kml_path}: {e}") from e


def write_kmz(out_dir: Path, kmz_name: str, kml_text: str, assets: Sequence[Path], *, prefix: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    kmz_name = kmz_name if kmz_name.lower().endswith(".kmz") else f"{kmz_name}.kmz"
    kmz_path = out_dir / kmz_name
    with zipfile.ZipFile(kmz_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("doc.kml", kml_text)
        for a in assets:
            z.write(a, arcname=f"{prefix}/{a.name}")
    return kmz_path


def write_sidecars(kmz_path: Path) -> None:
    kmz_path.with_suffix(kmz_path.suffix + ".sha256").write_text(_sha256(kmz_path) + "\n", encoding="utf-8")
    meta = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kmz": kmz_path.name,
        "size": kmz_path.stat().st_size,
        "argv": sys.argv,
    }
    kmz_path.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Package KML + local assets into a KMZ.")
    ap.add_argument("--kml", required=True, type=Path, help="KML file or directory containing doc.kml (or an existing .kmz)")
    ap.add_argument("--out", required=True, type=Path, help="Output directory for KMZ + sidecars")
    ap.add_argument("--kmz", default="overlay.kmz", help="Output KMZ filename (default: overlay.kmz)")
    ap.add_argument("--prefix", default="files", help="Subfolder name inside KMZ for assets (default: files)")
    ap.add_argument("--strip-remote", action="store_true",
                    help="Remove features whose <href> points to http(s), making KMZ fully offline")
    ap.add_argument("--blank-remote", action="store_true",
                    help="Blank http(s) hrefs instead of removing owning feature")
    ap.add_argument("--extra", action="append", default=[],
                    help="Glob(s) of additional local files to include under prefix/ (repeatable)")
    ap.add_argument("--name-from-kml", action="store_true",
                    help="Derive KMZ name from <Document><name> (fallback to --kmz)")
    return ap.parse_args()


def main() -> int:
    args = parse_args()

    # If input is already a KMZ, copy + sidecars
    if _is_kmz(args.kml):
        args.out.mkdir(parents=True, exist_ok=True)
        dst = args.out / (args.kmz if args.kmz.lower().endswith(".kmz") else f"{args.kmz}.kmz")
        dst.write_bytes(args.kml.read_bytes())
        write_sidecars(dst)
        print(f"[OK] Copied KMZ → {dst}")
        return 0

    # Find and parse KML
    doc_dir, kml_file = find_doc_kml(args.kml)
    tree = load_kml(kml_file)
    root = tree.getroot()

    # KMZ name from KML if asked
    kmz_name = args.kmz
    if args.name_from_kml:
        nm = _read_kml_name(root)
        if nm:
            # sanitize minimal: spaces to underscores; drop path-hostiles
            safe = re.sub(r"\s+", "_", nm.strip())
            safe = "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "_" for ch in safe)
            if safe:
                kmz_name = safe if safe.lower().endswith(".kmz") else f"{safe}.kmz"

    # Rewrite hrefs and collect assets
    assets = rewrite_hrefs(
        item_path=kml_file,
        doc_dir=doc_dir,
        root=root,
        prefix=args.prefix,
        strip_remote=bool(args.strip_remote),
        blank_remote=bool(args.blank_remote),
    )

    # Include extra globs if requested
    extras: List[Path] = []
    for pat in (args.extra or []):
        for m in sorted(Path().glob(pat)):
            if m.is_file() and m not in assets and m not in extras:
                extras.append(m)
    if extras:
        assets.extend(extras)

    # Emit KMZ
    kml_text = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")
    kmz_path = write_kmz(args.out, kmz_name, kml_text, assets, prefix=args.prefix)
    write_sidecars(kmz_path)
    print(f"[OK] KMZ → {kmz_path} (assets: {len(assets)})")
    if args.strip_remote:
        print("[INFO] remote http(s) href owners removed")
    if args.blank_remote:
        print("[INFO] remote http(s) hrefs blanked (nodes kept)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
