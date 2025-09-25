#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
regionate_kml.py — Build a quadtree of KML Folders with Regions + NetworkLinks.

Goal
----
Given many features (Points, Polylines, Polygons) this script produces a
regionated KML tree (z/x/y.kml) so Google Earth loads details progressively.

Inputs
------
- GeoJSON FeatureCollection (preferred)  → --geojson input.geojson
- Flat/simple KML with Placemarks (optional) → --kml input.kml
  (Limited parser: extracts Placemark name + Point/LineString/Polygon coords.)

Output
------
- A folder with:
  doc.kml                (root)
  nodes/0.kml            (root node)
  nodes/1.kml, 2.kml...  (children)
  nodes/z/x_y.kml        (quadtree nodes)
- Optional: a KMZ (zip) if --kmz out.kmz is given.

Regionation
-----------
- Quadtree over the dataset bbox.
- Nodes subdivide until (count <= --leaf-features) or depth == --max-depth.
- Each node .kml has a <Region> (LatLonAltBox) + <Lod> (min/max LOD pixels).
- Each node contains only the features intersecting its bbox.
- Each child is referenced via <NetworkLink> from its parent.

Practical notes
---------------
- Works best if features have 2D bbox. We compute from geometry coordinates.
- For very large polylines/polygons, consider simplifying beforehand.
- For rasters/overlays, emit as GroundOverlay items into nodes similarly.

Usage
-----
python scripts/regionate_kml.py --geojson data/features.geojson \
  --out build/kml/my_layer --name "Kansas Geo Timeline — Layers" \
  --leaf-features 250 --max-depth 8 --lod-min 128 --lod-max -1

python scripts/regionate_kml.py --kml data/flat.kml \
  --out build/kml/flat --kmz build/kml/flat.kmz

"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

# ----------------------------
# Geometry / bbox utilities
# ----------------------------

def bbox_union(a: Tuple[float, float, float, float],
               b: Tuple[float, float, float, float]) -> Tuple[float, float, float, float]:
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))

def bbox_intersects(a: Tuple[float, float, float, float],
                    b: Tuple[float, float, float, float]) -> bool:
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return (ax1 <= bx2) and (ax2 >= bx1) and (ay1 <= by2) and (ay2 >= by1)

def bbox_from_coords(coords: Iterable[Tuple[float, float]]) -> Tuple[float, float, float, float]:
    xs, ys = zip(*coords)
    return (min(xs), min(ys), max(xs), max(ys))

def geom_bbox(geom: Dict) -> Tuple[float, float, float, float]:
    t = geom.get("type")
    c = geom.get("coordinates")
    if t == "Point":
        x, y = c[:2]
        return (x, y, x, y)
    if t in ("LineString", "MultiPoint"):
        return bbox_from_coords(c)
    if t == "Polygon":
        ring = c[0] if c else []
        return bbox_from_coords(ring)
    if t == "MultiLineString":
        flat = [pt for line in c for pt in line]
        return bbox_from_coords(flat)
    if t == "MultiPolygon":
        flat = [pt for poly in c for ring in (poly[0] if poly else []) for pt in ring]
        return bbox_from_coords(flat)
    if t == "GeometryCollection":
        bb = None
        for g in geom.get("geometries", []):
            b = geom_bbox(g)
            bb = b if bb is None else bbox_union(bb, b)
        return bb or (0, 0, 0, 0)
    raise ValueError(f"Unsupported geometry type: {t}")

def kml_coords_for_geom(geom: Dict) -> str:
    """Return KML <coordinates> string; supports Point/LineString/Polygon (+Multi*)."""
    t = geom.get("type")
    c = geom.get("coordinates")
    if t == "Point":
        x, y = c[:2]
        return f"{x:.8f},{y:.8f},0"
    if t == "LineString":
        return " ".join(f"{x:.8f},{y:.8f},0" for x, y in c)
    if t == "Polygon":
        outer = c[0] if c else []
        return " ".join(f"{x:.8f},{y:.8f},0" for x, y in outer)
    if t == "MultiPoint":
        return " ".join(f"{x:.8f},{y:.8f},0" for x, y in c)
    if t == "MultiLineString":
        # Concatenate parts; GE renders them as one line if in one placemark.
        return " ".join(f"{x:.8f},{y:.8f},0" for line in c for x, y in line)
    if t == "MultiPolygon":
        outer_rings = [poly[0] for poly in c if poly]
        return " ".join(f"{x:.8f},{y:.8f},0" for ring in outer_rings for x, y in ring)
    if t == "GeometryCollection":
        # Fallback: flatten to multi-line string of coordinates
        parts = []
        for g in geom.get("geometries", []):
            parts.append(kml_coords_for_geom(g))
        return " ".join(parts)
    raise ValueError(f"Unsupported geometry type for KML coordinates: {t}")

# ----------------------------
# Feature + parsing
# ----------------------------

@dataclass
class Feature:
    id: str
    name: str
    geom: Dict
    bbox: Tuple[float, float, float, float]
    props: Dict

def parse_geojson(p: Path) -> Tuple[List[Feature], Tuple[float, float, float, float]]:
    data = json.loads(p.read_text(encoding="utf-8"))
    if data.get("type") != "FeatureCollection":
        raise ValueError("GeoJSON must be a FeatureCollection")
    feats: List[Feature] = []
    bb = None
    for i, f in enumerate(data.get("features", [])):
        geom = f.get("geometry") or {}
        if not geom:
            continue
        b = tuple(f.get("bbox")) if f.get("bbox") else geom_bbox(geom)
        props = f.get("properties") or {}
        nm = props.get("name") or props.get("title") or f"feat_{i}"
        fid = str(f.get("id") or i)
        feats.append(Feature(id=fid, name=str(nm), geom=geom, bbox=b, props=props))
        bb = b if bb is None else bbox_union(bb, b)
    if bb is None:
        raise ValueError("No features found in GeoJSON")
    return feats, bb

# Very small KML reader (Placemark only), good enough for flat/simple sources
_PLACEMARK_RE = re.compile(r"<Placemark(?:\s[^>]*)?>(.*?)</Placemark>", re.DOTALL)
_NAME_RE = re.compile(r"<name>(.*?)</name>", re.DOTALL)
_POINT_RE = re.compile(r"<Point>.*?<coordinates>(.*?)</coordinates>.*?</Point>", re.DOTALL)
_LINE_RE = re.compile(r"<LineString>.*?<coordinates>(.*?)</coordinates>.*?</LineString>", re.DOTALL)
_POLY_RE = re.compile(r"<Polygon>.*?<outerBoundaryIs>.*?<coordinates>(.*?)</coordinates>.*?</outerBoundaryIs>.*?</Polygon>", re.DOTALL)

def _parse_coord_text(txt: str) -> List[Tuple[float, float]]:
    pts = []
    for token in txt.strip().replace("\n", " ").split():
        if not token:
            continue
        parts = token.split(",")
        if len(parts) >= 2:
            x, y = float(parts[0]), float(parts[1])
            pts.append((x, y))
    return pts

def parse_flat_kml(p: Path) -> Tuple[List[Feature], Tuple[float, float, float, float]]:
    text = p.read_text(encoding="utf-8")
    feats: List[Feature] = []
    bb = None
    idx = 0
    for block in _PLACEMARK_RE.findall(text):
        name_m = _NAME_RE.search(block)
        name = name_m.group(1).strip() if name_m else f"placemark_{idx}"
        geom: Optional[Dict] = None

        if (m := _POINT_RE.search(block)):
            pts = _parse_coord_text(m.group(1))
            if pts:
                x, y = pts[0]
                geom = {"type": "Point", "coordinates": [x, y]}
        elif (m := _LINE_RE.search(block)):
            pts = _parse_coord_text(m.group(1))
            if pts:
                geom = {"type": "LineString", "coordinates": [[x, y] for x, y in pts]}
        elif (m := _POLY_RE.search(block)):
            pts = _parse_coord_text(m.group(1))
            if pts:
                geom = {"type": "Polygon", "coordinates": [[[x, y] for x, y in pts]]}

        if geom:
            b = geom_bbox(geom)
            feats.append(Feature(id=str(idx), name=name, geom=geom, bbox=b, props={}))
            bb = b if bb is None else bbox_union(bb, b)
            idx += 1
    if not feats:
        raise ValueError("No Placemarks found in KML (Point/LineString/Polygon)")
    return feats, bb

# ----------------------------
# Quadtree
# ----------------------------

@dataclass
class Node:
    id: int
    depth: int
    bbox: Tuple[float, float, float, float]
    features: List[int]  # indices into features array
    children: List['Node']

def subdivide(b: Tuple[float, float, float, float]) -> List[Tuple[float, float, float, float]]:
    x1, y1, x2, y2 = b
    xm = (x1 + x2) / 2.0
    ym = (y1 + y2) / 2.0
    # NW, NE, SW, SE (lat grows north → y2 higher)
    return [
        (x1, ym, xm, y2),  # NW
        (xm, ym, x2, y2),  # NE
        (x1, y1, xm, ym),  # SW
        (xm, y1, x2, ym),  # SE
    ]

def build_quadtree(all_features: List[Feature],
                   root_bbox: Tuple[float, float, float, float],
                   leaf_features: int,
                   max_depth: int) -> Node:
    node_id = 0
    def mk_node(depth: int, bbox: Tuple[float, float, float, float], idxs: List[int]) -> Node:
        nonlocal node_id
        me = Node(id=node_id, depth=depth, bbox=bbox, features=idxs, children=[])
        node_id += 1
        if depth >= max_depth or len(idxs) <= leaf_features:
            return me
        # assign to children (feature goes to any child whose bbox intersects)
        for child_bbox in subdivide(bbox):
            child_idxs = [i for i in idxs if bbox_intersects(all_features[i].bbox, child_bbox)]
            if child_idxs:
                me.children.append(mk_node(depth + 1, child_bbox, child_idxs))
        return me

    # initial features (all)
    idxs = list(range(len(all_features)))
    return mk_node(0, root_bbox, idxs)

# ----------------------------
# KML writers
# ----------------------------

def kml_header(name: str) -> str:
    return (
f'<?xml version="1.0" encoding="UTF-8"?>\n'
f'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
f'  <Document>\n'
f'    <name>{escape_xml(name)}</name>\n'
    )

def kml_footer() -> str:
    return "  </Document>\n</kml>\n"

def kml_region(b: Tuple[float, float, float, float], lod_min: int, lod_max: int) -> str:
    x1, y1, x2, y2 = b
    return (
f'    <Region>\n'
f'      <LatLonAltBox>\n'
f'        <north>{y2:.8f}</north>\n'
f'        <south>{y1:.8f}</south>\n'
f'        <east>{x2:.8f}</east>\n'
f'        <west>{x1:.8f}</west>\n'
f'      </LatLonAltBox>\n'
f'      <Lod>\n'
f'        <minLodPixels>{lod_min}</minLodPixels>\n'
f'        <maxLodPixels>{lod_max}</maxLodPixels>\n'
f'      </Lod>\n'
f'    </Region>\n'
    )

def kml_network_link(name: str, href: str, b: Tuple[float, float, float, float],
                     lod_min: int, lod_max: int) -> str:
    return (
f'    <NetworkLink>\n'
f'      <name>{escape_xml(name)}</name>\n'
f'{kml_region(b, lod_min, lod_max)}'
f'      <Link>\n'
f'        <href>{escape_xml(href)}</href>\n'
f'        <viewRefreshMode>onRegion</viewRefreshMode>\n'
f'      </Link>\n'
f'    </NetworkLink>\n'
    )

def kml_placemark(feat: Feature, style_url: Optional[str]=None) -> str:
    nm = escape_xml(feat.name)
    coords = kml_coords_for_geom(feat.geom)
    t = feat.geom["type"]
    style = f"      <styleUrl>{escape_xml(style_url)}</styleUrl>\n" if style_url else ""
    if t == "Point":
        return (
f'    <Placemark>\n'
f'      <name>{nm}</name>\n'
f'{style}'
f'      <Point><coordinates>{coords}</coordinates></Point>\n'
f'    </Placemark>\n'
        )
    if t in ("LineString", "MultiLineString"):
        return (
f'    <Placemark>\n'
f'      <name>{nm}</name>\n'
f'{style}'
f'      <LineString><tessellate>1</tessellate><coordinates>{coords}</coordinates></LineString>\n'
f'    </Placemark>\n'
        )
    if t in ("Polygon", "MultiPolygon"):
        return (
f'    <Placemark>\n'
f'      <name>{nm}</name>\n'
f'{style}'
f'      <Polygon><tessellate>1</tessellate><outerBoundaryIs><LinearRing>'
f'<coordinates>{coords}</coordinates></LinearRing></outerBoundaryIs></Polygon>\n'
f'    </Placemark>\n'
        )
    # Fallback as point at bbox center
    x1, y1, x2, y2 = feat.bbox
    xc, yc = (x1+x2)/2.0, (y1+y2)/2.0
    return (
f'    <Placemark>\n'
f'      <name>{nm}</name>\n'
f'{style}'
f'      <Point><coordinates>{xc:.8f},{yc:.8f},0</coordinates></Point>\n'
f'    </Placemark>\n'
    )

def escape_xml(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&apos;"))

def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)

# ----------------------------
# Regionation writer
# ----------------------------

def write_tree(root: Node, features: List[Feature], outdir: Path,
               name: str, lod_min: int, lod_max: int, style_url: Optional[str]) -> None:
    """
    Write:
    - doc.kml (links to node 0)
    - nodes/<id>.kml for each node, linking to its children with Regions
    """
    nodes_dir = outdir / "nodes"
    # doc.kml
    doc = []
    doc.append(kml_header(name))
    doc.append("    <Folder>\n")
    doc.append(f'      <name>{escape_xml(name)} — Regionated</name>\n')
    # link to root node (id 0)
    doc.append(kml_network_link("root", "nodes/0.kml", root.bbox, lod_min, lod_max))
    doc.append("    </Folder>\n")
    doc.append(kml_footer())
    write_text_atomic(outdir / "doc.kml", "".join(doc))

    # node files (DFS)
    stack = [root]
    while stack:
        n = stack.pop()
        k = []
        k.append(kml_header(f"node {n.id} (depth {n.depth})"))
        k.append(kml_region(n.bbox, lod_min, lod_max))
        # child links
        for ch in n.children:
            href = f"{ch.id}.kml"
            k.append(kml_network_link(f"node {ch.id}", href, ch.bbox, lod_min, lod_max))
        # features in this node (only when leaf or shallow? — keep simple: always include)
        k.append("    <Folder>\n")
        k.append(f'      <name>features ({len(n.features)})</name>\n')
        for idx in n.features:
            k.append(kml_placemark(features[idx], style_url=style_url))
        k.append("    </Folder>\n")
        k.append(kml_footer())
        write_text_atomic(nodes_dir / f"{n.id}.kml", "".join(k))
        # traverse
        for ch in n.children:
            stack.append(ch)

# ----------------------------
# KMZ
# ----------------------------

def write_kmz_from_folder(src_dir: Path, kmz_path: Path) -> None:
    # KMZ expects doc.kml at root and relative links within folders
    with zipfile.ZipFile(kmz_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in [src_dir / "doc.kml", *sorted((src_dir / "nodes").rglob("*.kml"))]:
            arc = p.relative_to(src_dir).as_posix()
            z.write(p, arcname=arc)

# ----------------------------
# Main CLI
# ----------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Regionate features into a KML quadtree with Regions + NetworkLinks.")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--geojson", type=Path, help="Input GeoJSON FeatureCollection")
    src.add_argument("--kml", type=Path, help="Input flat/simple KML with Placemarks")
    ap.add_argument("--out", type=Path, required=True, help="Output folder for KML tree")
    ap.add_argument("--name", type=str, default="Regionated Layer", help="Root document name")
    ap.add_argument("--leaf-features", type=int, default=200, help="Max features per leaf node")
    ap.add_argument("--max-depth", type=int, default=8, help="Max quadtree depth")
    ap.add_argument("--lod-min", type=int, default=128, help="minLodPixels (e.g., 64–256)")
    ap.add_argument("--lod-max", type=int, default=-1, help="maxLodPixels (-1 = no limit)")
    ap.add_argument("--style-url", type=str, help="Optional shared <styleUrl> for placemarks")
    ap.add_argument("--bbox", type=float, nargs=4, metavar=("MINX","MINY","MAXX","MAXY"),
                    help="Force root bbox; otherwise use dataset bbox")
    ap.add_argument("--kmz", type=Path, help="Also write a KMZ at this path")
    args = ap.parse_args()

    # Load features
    if args.geojson:
        feats, bb = parse_geojson(args.geojson)
    else:
        feats, bb = parse_flat_kml(args.kml)

    if args.bbox:
        bb = tuple(args.bbox)  # type: ignore

    # Build quadtree
    root = build_quadtree(feats, bb, leaf_features=max(1, args.leaf_features), max_depth=max(0, args.max_depth))

    # Write tree
    outdir = args.out
    outdir.mkdir(parents=True, exist_ok=True)
    write_tree(root, feats, outdir, name=args.name, lod_min=args.lod_min, lod_max=args.lod_max,
               style_url=args.style_url)

    # Optional KMZ
    if args.kmz:
        write_kmz_from_folder(outdir, args.kmz)

    # Manifest for CI/debug
    manifest = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": str(args.geojson or args.kml),
        "outdir": str(outdir),
        "kmz": str(args.kmz) if args.kmz else None,
        "name": args.name,
        "features": len(feats),
        "quadtree": {
            "leaf_features": args.leaf_features,
            "max_depth": args.max_depth,
            "bbox": list(bb),
        },
        "lod": {"min": args.lod_min, "max": args.lod_max},
    }
    Path(outdir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"[OK] regionated KML → {outdir/'doc.kml'} "
          f"({manifest['features']} features, depth≤{args.max_depth})")
    if args.kmz:
        print(f"[OK] KMZ → {args.kmz}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
