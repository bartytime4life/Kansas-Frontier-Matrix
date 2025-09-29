#!/usr/bin/env python3
"""
Generate Shields.io JSON endpoints for data coverage badges.

Reads STAC + data/sources to infer status per domain, then writes
JSON files under public/badges/status/*.json (for GitHub Pages).

No external dependencies; pure stdlib.
"""
import json
import os
import glob
from pathlib import Path

# ----------------------------
# Config
# ----------------------------
ROOT = Path(__file__).resolve().parents[1]
STAC_CATALOG = ROOT / "stac" / "catalog.json"
SOURCES_DIR = ROOT / "data" / "sources"
OUT_DIR = ROOT / "public" / "badges" / "status"  # Published via GH Pages

# Badge schema helpers (Shields endpoint format)
def badge(label: str, message: str, color: str) -> dict:
    return {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "color": color
    }

def write_badge(filename: str, payload: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

# ----------------------------
# Heuristics for coverage
# ----------------------------
def load_stac():
    if STAC_CATALOG.exists():
        try:
            return json.loads(STAC_CATALOG.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def list_source_jsons():
    return [Path(p) for p in glob.glob(str(SOURCES_DIR / "**" / "*.json"), recursive=True)]

def text_join(*parts):
    return " ".join([str(p).lower() for p in parts if p])

def any_match(haystack: str, needles):
    return any(n in haystack for n in needles)

def status_from_presence(has_all: bool, has_some: bool, planned: bool = False, pilot: bool = False, in_dev: bool = False):
    # Map to standard messages/colors (consistent with README)
    if has_all:
        return ("✔️ ready", "brightgreen")
    if pilot:
        return ("⚠️ pilot", "orange")
    if in_dev:
        return ("⚠️ in dev", "orange")
    if has_some:
        return ("⚠️ partial", "orange")
    if planned:
        return ("❌ planned", "lightgrey")
    # default fallback
    return ("⚠️ in progress", "orange")

def infer_presence():
    """
    Build a simple presence index from filenames & item hrefs.
    This relies on consistent naming in data/sources and STAC items.
    """
    stac = load_stac()
    items_txt = json.dumps(stac).lower() if stac else ""
    src_files = list_source_jsons()
    src_txt = " ".join([text_join(p.name, p.parent) for p in src_files])

    def check(needles, in_dev_needles=None, pilot_needles=None, planned=False):
        in_dev_needles = in_dev_needles or []
        pilot_needles = pilot_needles or []
        # presence in sources or stac
        has_some = any_match(src_txt, needles) or any_match(items_txt, needles)
        # "all" is hard to know; treat as same for now, can refine later
        has_all = has_some
        in_dev = any_match(src_txt, in_dev_needles) or any_match(items_txt, in_dev_needles)
        pilot = any_match(src_txt, pilot_needles) or any_match(items_txt, pilot_needles)
        return status_from_presence(has_all, has_some, planned=planned, pilot=pilot, in_dev=in_dev)

    status = {}

    # Domains and keyword heuristics (adjust as your repo evolves)
    status["dem"]         = check(["dem", "lidar", "elevation", "raster-dem"])
    status["hillshade"]   = check(["hillshade", "slope", "aspect"], in_dev_needles=["terrain"])
    status["hydro"]       = check(["nhd", "hydro", "river", "flood", "flowdir"], in_dev_needles=["floodplain", "hec-ras"])
    status["landcover"]   = check(["nlcd", "landcover", "land_cover"])
    status["soils"]       = check(["ssurgo", "soils", "plss", "parcel", "parcels"])
    status["treaties"]    = check(["treaties", "tribal", "cession", "reservation"])
    status["railroads"]   = check(["railroad", "rail", "trails"], in_dev_needles=["anim", "timeline-rail"])
    status["topo"]        = check(["topo", "usgs", "pcl", "historic topo", "drg"])
    status["climate"]     = check(["climate normals", "1991-2020", "daymet", "ncei", "ghcn"])
    status["tornado"]     = check(["tornado", "spc", "svrgis"])
    status["drought"]     = check(["drought monitor", "usdm"])
    status["floods"]      = check(["fema", "flood", "declaration"], in_dev_needles=["extent", "inundation"])
    status["wildfire"]    = check(["wildfire", "nifc", "fire perimeter"])
    status["paleo"]       = check(["paleo", "charcoal", "core", "speleo", "holocene"], planned=True)
    status["oral"]        = check(["oral", "archaeology", "excavation", "site"], pilot_needles=["pilot"])
    status["geology"]     = check(["core library", "drill core", "kgs"], in_dev_needles=["logger"])

    return status

def main():
    presence = infer_presence()

    labels = {
        "dem":        "DEM / Terrain",
        "hillshade":  "Hillshade / Derivatives",
        "hydro":      "Hydrology",
        "landcover":  "Land Cover",
        "soils":      "Soils / PLSS / Parcels",
        "treaties":   "Treaties & Tribal Lands",
        "railroads":  "Railroads & Trails",
        "topo":       "Topographic Maps",
        "climate":    "Climate Normals",
        "tornado":    "Hazards — Tornado",
        "drought":    "Hazards — Drought",
        "floods":     "Hazards — Floods",
        "wildfire":   "Hazards — Wildfire",
        "paleo":      "Paleoclimate / Fire Regimes",
        "oral":       "Oral Histories & Archaeology",
        "geology":    "Geology / Core Samples",
    }

    for key, (message, color) in presence.items():
        label = labels.get(key, key)
        write_badge(f"{key}.json", badge(label, message, color))

    # Optional: also write an index file
    write_badge("index.json", badge("coverage", "updated", "blue"))
    print(f"Wrote {len(presence)} badges to {OUT_DIR}")

if __name__ == "__main__":
    main()
