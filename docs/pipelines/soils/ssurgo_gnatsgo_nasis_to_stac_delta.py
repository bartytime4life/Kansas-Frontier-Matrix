---
title: "🧩 KFM — SSURGO/gNATSGO/NASIS → STAC/DCAT Delta (One‑File Recipe)"
path: "docs/pipelines/soils/ssurgo_gnatsgo_nasis_to_stac_delta.md"
script_path: "src/pipelines/soils/ssurgo_gnatsgo_nasis_to_stac_delta.py"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long‑Term Support (LTS)"
review_cycle: "Semiannual · FAIR+CARE Council · Data Architecture Board"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Runnable Recipe (Single‑File Script)"
header_profile: "standard"
footer_profile: "standard"
intent: "etl-soils-ssurgo-gnatsgo-nasis-stac-dcat-delta"

license: "CC-BY 4.0 (docs) · MIT (code)"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

semantic_document_id: "kfm-soils-ssurgo-gnatsgo-nasis-stac-delta"
doc_uuid: "urn:kfm:recipe:ssurgo-gnatsgo-nasis-stac-delta:v11.2.6"
event_source_id: "urn:kfm:event:recipe:ssurgo-gnatsgo-nasis-stac-delta"
immutability_status: "mutable-plan"

classification: "Public"
sensitivity: "Low"
fair_category: "Open Metadata"
care_label: "CARE-N/A"

owner: "KFM Core · Data Engineering"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"
telemetry_ref: "releases/v11.2.6/system-telemetry.json"
telemetry_schema: "schemas/telemetry/etl-soils-stac-delta-v1.json"

commit_sha: "<set-by-ci>"
signature_ref: "<set-by-release>"
attestation_ref: "<set-by-release>"

ai_transform_permissions:
  - "summarize"
  - "reformat"
  - "extract_metadata"
  - "generate_checklists"
ai_transform_prohibited:
  - "change normative requirements"
  - "remove governance links"
  - "introduce new external sources without review"
---

# 🧩 KFM — SSURGO/gNATSGO/NASIS → STAC/DCAT Delta (One‑File Recipe)

> **Purpose**  
> Pull SSURGO / gNATSGO / NASIS signals (SDA API + local packages), run a deterministic “LLM‑style”
> field→STAC/DCAT mapping step, apply minimal QA, and write governed **metadata‑only** outputs.  
> Commit happens **only** when the persisted **input fingerprint** changes. Rollback is a **single command**.

## 📘 Overview

### What this is (and isn’t)

- ✅ **Is:** a tiny metadata delta step that emits:
  - a **STAC Item** (coverage + lineage hints)
  - a **DCAT Dataset bundle** (catalog registration fields)
  - a persisted **fingerprint** (delta gate)
- ❌ **Is not:** CRS/H3 tiling/indexing, raster processing, or graph mutation

### Quickstart

~~~bash
# 1) Create a venv
python -m venv .venv && source .venv/bin/activate

# 2) Install deps (no GDAL; wheels available for compiled deps like shapely/xxhash)
pip install click==8.* requests==2.* python-dateutil==2.* jsonschema==4.* \
            shapely==2.* xxhash==3.* rich==13.*

# 3) Run (example AOI bbox shown; replace with an authoritative boundary)
python src/pipelines/soils/ssurgo_gnatsgo_nasis_to_stac_delta.py \
  --item-id kfm-soils-ssurgo-gnatsgo-nasis-ks \
  --sda-where "l.areaname = 'Kansas'" \
  --ssurgo-zip ./data/raw/soils/ssurgo/SSURGO_KS_bulk.zip \
  --gnatsgo-zip ./data/raw/soils/gnatsgo/gNATSGO_CONUS_v24.zip \
  --nasis-sqlite ./data/raw/soils/nasis/nasis_local.sqlite \
  --aoi-bbox "-102.05,36.99,-94.59,40.00" \
  --out-dir ./data/stac/soils/items \
  --catalog ./data/stac/catalog.json \
  --dcat-out ./docs/data/dcat/soils_datasets.jsonld \
  --state-dir ./data/checksums/soils/stac_delta \
  --commit \
  --commit-message "soils: delta metadata update (auto-mapped STAC/DCAT)" \
  --rollback-token-path ./.kfm_last_delta_token
~~~

Rollback one command (safe revert):

~~~bash
python src/pipelines/soils/ssurgo_gnatsgo_nasis_to_stac_delta.py --rollback \
  --rollback-token-path ./.kfm_last_delta_token
~~~

## 🗂️ Directory Layout

~~~text
📂 docs/pipelines/soils/
└── 📄 ssurgo_gnatsgo_nasis_to_stac_delta.md      # This doc (KFM-MDP)

📂 src/pipelines/soils/
└── 🐍 ssurgo_gnatsgo_nasis_to_stac_delta.py           # Runnable script (one file)

📂 data/raw/soils/
├── 📂 ssurgo/                                          # SSURGO bulk packages (often DVC-managed)
├── 📂 gnatsgo/                                         # gNATSGO packages (often DVC-managed)
└── 📂 nasis/                                           # NASIS SQLite extracts (often DVC-managed)

📂 data/stac/soils/items/
└── 🗺️ <item_id>.geojson                                # Emitted STAC Item

📂 docs/data/dcat/
└── 📄 soils_datasets.jsonld                            # Emitted DCAT dataset bundle

📂 data/checksums/soils/stac_delta/
└── 🔒 <item_id>.fingerprint                            # Persisted fingerprint (delta gate)
~~~

## 🧭 Context

This step is designed to slot into KFM’s “Standardization & Metadata Annotation” stage: it produces STAC/DCAT metadata artifacts and makes **no tiling/indexing changes**.

**Material difference from CRS/H3 cards:**  
The novelty is deterministic *field inventory → STAC/DCAT* mapping + persisted input fingerprint delta gating for safe, tiny metadata-only updates.

## 📦 Data & Metadata

### Inputs

- **SDA** tabular rows (public; optional; skipped with `--offline`)
  - Note: `--sda-where` expects a **SQL WHERE fragment** (not the SDA “key:value” style).
- **SSURGO** bulk zip (local path)
- **gNATSGO** zip (local path)
- **NASIS** SQLite (local path)
- **AOI geometry**:
  - `--aoi-geojson <path>` OR
  - `--aoi-bbox "minx,miny,maxx,maxy"` (fallback)

### Outputs

- STAC Item: `--out-dir/<item_id>.geojson`
- DCAT bundle: `--dcat-out`
- Fingerprint state: `--state-dir/<item_id>.fingerprint`
- Optional STAC catalog link append: `--catalog`

### The Script (single file)

Save the following as `src/pipelines/soils/ssurgo_gnatsgo_nasis_to_stac_delta.py`:

~~~python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
KFM — SSURGO/gNATSGO/NASIS → STAC/DCAT Delta (metadata-only)

- Pulls sources: SDA tabular rows (optional), SSURGO bulk zip, gNATSGO zip, NASIS SQLite
- Deterministic inventory+heuristics mapping -> STAC Item + DCAT Dataset
- Minimal QA: geometry/bbox sanity + temporal coverage
- Delta gate: write outputs only when input fingerprint changes (persisted state file)
- Optional: git commit + single-command rollback (git revert) via token file
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import click
import requests
import xxhash
from dateutil.parser import isoparse
from rich.console import Console
from rich.table import Table
from shapely.geometry import Polygon, box, mapping, shape
from shapely.ops import unary_union

console = Console()


# ----------------------------
# Helpers: JSON + hashing
# ----------------------------
def _canonical_json_bytes(obj: Any) -> bytes:
    """Deterministic JSON encoding for hashing."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _xxh64_hexdigest(obj: Any) -> str:
    h = xxhash.xxh64()
    h.update(_canonical_json_bytes(obj))
    return h.hexdigest()


def _file_xxh64(path: Optional[Path], *, mode: str = "fast", fast_bytes: int = 2_000_000) -> Dict[str, Any]:
    """
    Compute a lightweight file fingerprint.
    mode:
      - "fast": hash first `fast_bytes` bytes + size + mtime
      - "full": hash full file bytes + size + mtime
    """
    if not path:
        return {"exists": False, "path": None}
    if not path.exists():
        return {"exists": False, "path": str(path)}

    st = path.stat()
    h = xxhash.xxh64()
    h.update(str(st.st_size).encode("utf-8"))
    h.update(str(int(st.st_mtime)).encode("utf-8"))

    n = 0
    with path.open("rb") as f:
        if mode == "full":
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
                n += len(chunk)
        else:
            data = f.read(fast_bytes)
            h.update(data)
            n = len(data)

    return {
        "exists": True,
        "path": str(path),
        "size": st.st_size,
        "mtime_epoch_s": int(st.st_mtime),
        "hash_mode": mode,
        "hashed_bytes": n,
        "xxh64": h.hexdigest(),
    }


# ----------------------------
# Helpers: git (CLI, no GitPython dependency)
# ----------------------------
def _run(cmd: Sequence[str], cwd: Optional[Path] = None, *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(cmd),
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=True,
        check=check,
    )


def _git_root(start: Path) -> Optional[Path]:
    try:
        cp = _run(["git", "rev-parse", "--show-toplevel"], cwd=start, check=True)
        root = cp.stdout.strip()
        return Path(root) if root else None
    except Exception:
        return None


def _git_is_clean(repo_root: Path) -> bool:
    cp = _run(["git", "status", "--porcelain"], cwd=repo_root, check=True)
    return cp.stdout.strip() == ""


def _repo_relative(repo_root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except Exception:
        return path.as_posix()


def _git_commit_files(
    repo_root: Path,
    files: List[Path],
    message: str,
    token_path: Path,
    *,
    allow_dirty: bool = False,
) -> Optional[str]:
    if not allow_dirty and not _git_is_clean(repo_root):
        raise RuntimeError("Refusing to commit: working tree is dirty (use --allow-dirty to override).")

    rel_files = [str(f) for f in files]
    _run(["git", "add", "--"] + rel_files, cwd=repo_root, check=True)

    # Bail if nothing staged.
    diff_cp = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=str(repo_root))
    if diff_cp.returncode == 0:
        return None

    _run(["git", "commit", "-m", message], cwd=repo_root, check=True)
    sha = _run(["git", "rev-parse", "HEAD"], cwd=repo_root, check=True).stdout.strip()

    token_path.parent.mkdir(parents=True, exist_ok=True)
    token_path.write_text(sha, encoding="utf-8")
    return sha


def _git_rollback_revert(repo_root: Path, token_path: Path, *, allow_dirty: bool = False) -> str:
    if not token_path.exists():
        raise RuntimeError(f"No rollback token found at: {token_path}")

    if not allow_dirty and not _git_is_clean(repo_root):
        raise RuntimeError("Refusing to rollback: working tree is dirty (use --allow-dirty to override).")

    sha = token_path.read_text(encoding="utf-8").strip()
    if not sha:
        raise RuntimeError("Rollback token was empty")

    _run(["git", "revert", "--no-edit", sha], cwd=repo_root, check=True)

    token_path.unlink(missing_ok=True)
    return sha


# ----------------------------
# Helpers: atomic writes
# ----------------------------
def _atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def _atomic_write_json(path: Path, obj: Any) -> None:
    _atomic_write_text(path, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


# ----------------------------
# Source readers
# ----------------------------
SDA_URL = "https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest"


def fetch_sda_rows(where_sql: str, *, limit: int = 5000, timeout_s: int = 30, offline: bool = False) -> List[Dict[str, Any]]:
    """
    Minimal SDA API call. Returns [] on error/offline.
    `where_sql` should be a SQL WHERE clause fragment.
    """
    if offline:
        return []

    sql = f"SELECT TOP {int(limit)} * FROM legend l INNER JOIN mapunit mu ON l.lkey=mu.lkey WHERE {where_sql}"
    payload = {"format": "JSON", "query": sql}

    try:
        resp = requests.post(SDA_URL, json=payload, timeout=timeout_s)
        resp.raise_for_status()
        data = resp.json()
    except Exception:
        return []

    # SDA responses vary; handle common shapes.
    if isinstance(data, dict):
        if isinstance(data.get("Table"), list):
            return [r for r in data["Table"] if isinstance(r, dict)]
        if isinstance(data.get("rows"), list):
            return [r for r in data["rows"] if isinstance(r, dict)]
        # Sometimes nested.
        for v in data.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                return v
    return []


def read_sqlite_rows(sqlite_path: Path, query: str, *, limit: int = 5000) -> List[Dict[str, Any]]:
    if not sqlite_path or not sqlite_path.exists():
        return []
    try:
        con = sqlite3.connect(str(sqlite_path))
        cur = con.cursor()
        cur.execute(query)
        cols = [c[0] for c in cur.description]
        rows = []
        for row in cur.fetchmany(limit):
            rows.append(dict(zip(cols, row)))
        con.close()
        return rows
    except Exception:
        return []


def _local_name(tag: str) -> str:
    return tag.split("}", 1)[1] if "}" in tag else tag


def _parse_number(s: Optional[str]) -> Optional[float]:
    if s is None:
        return None
    s = s.strip()
    try:
        return float(s)
    except Exception:
        return None


def _xml_extract_bbox_and_dates(xml_text: str) -> Tuple[Optional[List[float]], List[str]]:
    """
    Try to extract bbox and date strings from FGDC/ISO-ish XML.
    Returns (bbox, date_strings).
    """
    date_strings: List[str] = []
    bbox: Optional[List[float]] = None

    try:
        import xml.etree.ElementTree as ET

        root = ET.fromstring(xml_text)
        values: Dict[str, List[str]] = {}
        for elem in root.iter():
            tag = _local_name(str(elem.tag))
            txts: List[str] = []
            if elem.text and elem.text.strip():
                txts.append(elem.text.strip())
            # Sometimes values are in child nodes.
            for child in list(elem):
                if child.text and child.text.strip():
                    txts.append(child.text.strip())
            if txts:
                values.setdefault(tag, []).extend(txts)

        def first_num(keys: Iterable[str]) -> Optional[float]:
            for k in keys:
                for v in values.get(k, []):
                    n = _parse_number(v)
                    if n is not None:
                        return n
            return None

        west = first_num(["westbc", "westBoundLongitude", "westLong"])
        east = first_num(["eastbc", "eastBoundLongitude", "eastLong"])
        north = first_num(["northbc", "northBoundLatitude", "northLat"])
        south = first_num(["southbc", "southBoundLatitude", "southLat"])

        if None not in (west, south, east, north):
            bbox = [float(west), float(south), float(east), float(north)]

        # Date candidates (FGDC + ISO variants)
        date_keys = [
            "begdate", "enddate", "begdt", "enddt",
            "beginPosition", "endPosition",
            "dateStamp",
        ]
        for k in date_keys:
            for v in values.get(k, []):
                date_strings.append(v)

    except Exception:
        # As a fallback, try regex on known tags (very permissive)
        def re_tag(t: str) -> Optional[float]:
            m = re.search(rf"<{t}>\s*([-+]?\d+(?:\.\d+)?)\s*</{t}>", xml_text, re.IGNORECASE)
            return float(m.group(1)) if m else None

        west = re_tag("westbc") or re_tag("westBoundLongitude")
        east = re_tag("eastbc") or re_tag("eastBoundLongitude")
        north = re_tag("northbc") or re_tag("northBoundLatitude")
        south = re_tag("southbc") or re_tag("southBoundLatitude")
        if None not in (west, south, east, north):
            bbox = [west, south, east, north]

    return bbox, date_strings


def scan_zip_for_signals(zpath: Path, *, max_xml_files: int = 20, max_bytes_per_xml: int = 2_000_000) -> Dict[str, Any]:
    """
    Extract lightweight signals from a zip without GDAL:
    - bbox from metadata XML (FGDC/ISO)
    - temporal hints from metadata XML
    - optional GeoJSON polygon union if present (best-effort)
    """
    out: Dict[str, Any] = {
        "path": str(zpath),
        "exists": bool(zpath and zpath.exists()),
        "bbox_candidates": [],
        "date_candidates": [],
        "geojson_polygons": 0,
    }
    if not zpath or not zpath.exists():
        return out

    try:
        with zipfile.ZipFile(zpath, "r") as zf:
            names = zf.namelist()

            # 1) XML metadata bbox/date extraction
            xml_names = [n for n in names if n.lower().endswith(".xml")]
            for n in xml_names[:max_xml_files]:
                try:
                    with zf.open(n) as f:
                        raw = f.read(max_bytes_per_xml)
                    bbox, dates = _xml_extract_bbox_and_dates(raw.decode("utf-8", errors="ignore"))
                    if bbox:
                        out["bbox_candidates"].append({"file": n, "bbox": bbox})
                    for d in dates:
                        out["date_candidates"].append({"file": n, "value": d})
                except Exception:
                    continue

            # 2) Optional: GeoJSON polygons union (best-effort)
            polys = []
            for n in names:
                if not (n.lower().endswith(".geojson") or n.lower().endswith(".json")):
                    continue
                # Avoid huge reads; metadata-only
                try:
                    with zf.open(n) as f:
                        raw = f.read(2_000_000)
                    obj = json.loads(raw.decode("utf-8", errors="ignore"))
                except Exception:
                    continue

                feats = obj.get("features") if isinstance(obj, dict) else None
                if not isinstance(feats, list):
                    continue

                for feat in feats[:200]:
                    try:
                        g = shape(feat.get("geometry"))
                        polys.append(g)
                    except Exception:
                        continue

            if polys:
                out["geojson_polygons"] = len(polys)
                try:
                    unioned = unary_union(polys).buffer(0)
                    out["geojson_union_bbox"] = list(map(float, unioned.bounds))
                except Exception:
                    pass

    except Exception:
        return out

    return out


# ----------------------------
# Deterministic “AI-style” mapping
# ----------------------------
def _parse_date_candidates(values: Iterable[str]) -> List["datetime.date"]:
    import datetime as _dt

    out: List[_dt.date] = []
    for v in values:
        if not v:
            continue
        s = str(v).strip()
        # Support YYYYMMDD
        try:
            if re.fullmatch(r"\d{8}", s):
                out.append(_dt.date(int(s[0:4]), int(s[4:6]), int(s[6:8])))
                continue
        except Exception:
            pass
        try:
            out.append(isoparse(s).date())
        except Exception:
            continue
    return out


def _coalesce_temporal(*date_lists: Iterable[str]) -> Tuple[Optional[str], Optional[str], Dict[str, Any]]:
    """Return (start_iso, end_iso, debug) based on any candidate date strings."""
    all_dates: List["datetime.date"] = []
    debug: Dict[str, Any] = {"candidates": []}
    for dl in date_lists:
        dl_list = list(dl)
        debug["candidates"].extend([str(x) for x in dl_list][:200])
        all_dates.extend(_parse_date_candidates(dl_list))
    if not all_dates:
        return None, None, debug
    start = min(all_dates).isoformat()
    end = max(all_dates).isoformat()
    return start, end, debug


def _bbox_union(bboxes: Iterable[Optional[List[float]]]) -> Optional[List[float]]:
    xs: List[float] = []
    ys: List[float] = []
    xe: List[float] = []
    ye: List[float] = []
    for b in bboxes:
        if not (isinstance(b, list) and len(b) == 4):
            continue
        try:
            xs.append(float(b[0])); ys.append(float(b[1])); xe.append(float(b[2])); ye.append(float(b[3]))
        except Exception:
            continue
    if not xs:
        return None
    return [min(xs), min(ys), max(xe), max(ye)]


def _aoi_geometry(aoi_geojson: Optional[Path], aoi_bbox: Optional[str]) -> Tuple[Optional[Dict[str, Any]], Optional[List[float]], str]:
    """
    Determine AOI geometry and bbox.
    Priority:
      1) --aoi-geojson (Feature/Geometry/FeatureCollection)
      2) --aoi-bbox minx,miny,maxx,maxy
    """
    if aoi_geojson:
        obj = json.loads(aoi_geojson.read_text(encoding="utf-8"))
        geom = None
        if isinstance(obj, dict) and obj.get("type") == "Feature":
            geom = obj.get("geometry")
        elif isinstance(obj, dict) and obj.get("type") in ("Polygon", "MultiPolygon"):
            geom = obj
        elif isinstance(obj, dict) and obj.get("type") == "FeatureCollection":
            feats = obj.get("features") or []
            polys = []
            for feat in feats[:500]:
                try:
                    g = shape(feat.get("geometry"))
                    polys.append(g)
                except Exception:
                    continue
            if polys:
                geom = mapping(unary_union(polys).buffer(0))
        if geom:
            shp = shape(geom)
            return geom, list(map(float, shp.bounds)), "aoi_geojson"
        return None, None, "aoi_geojson_invalid"

    if aoi_bbox:
        parts = [p.strip() for p in aoi_bbox.split(",")]
        if len(parts) == 4:
            try:
                minx, miny, maxx, maxy = map(float, parts)
                geom = mapping(box(minx, miny, maxx, maxy))
                return geom, [minx, miny, maxx, maxy], "aoi_bbox"
            except Exception:
                return None, None, "aoi_bbox_invalid"
        return None, None, "aoi_bbox_invalid"

    return None, None, "no_aoi"


def build_stac_item_and_dcat(
    *,
    item_id: str,
    title: str,
    description: str,
    aoi_geom: Optional[Dict[str, Any]],
    bbox: Optional[List[float]],
    temporal_start: Optional[str],
    temporal_end: Optional[str],
    input_fingerprint: str,
    source_summaries: Dict[str, Any],
    stac_item_href: str,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    # STAC Item (deterministic fields only; no runtime timestamps)
    props: Dict[str, Any] = {
        "title": title,
        "description": description,
        "start_datetime": f"{temporal_start}T00:00:00Z" if temporal_start else None,
        "end_datetime": f"{temporal_end}T23:59:59Z" if temporal_end else None,
        "datetime": f"{temporal_end}T00:00:00Z" if temporal_end else None,
        "kfm:input_fingerprint": input_fingerprint,
        "kfm:mapping_hints": {
            "method": "deterministic inventory+heuristics (offline)",
            "sources": source_summaries.get("sources", []),
            "signals": source_summaries.get("signals", {}),
        },
    }

    # Remove Nones for cleaner output
    props = {k: v for k, v in props.items() if v is not None}

    assets: Dict[str, Any] = {}
    for src in source_summaries.get("sources", []):
        if not isinstance(src, dict):
            continue
        name = str(src.get("name") or "source").lower().replace(" ", "_")
        href = src.get("url") or src.get("path")
        if not href:
            continue
        assets[name] = {
            "href": str(href),
            "roles": ["source", "metadata"],
            "title": src.get("name"),
        }
        # Keep any stable hints.
        extra = {k: v for k, v in src.items() if k not in {"name", "url", "path"} and v is not None}
        if extra:
            assets[name]["kfm:source_hints"] = extra

    stac_item: Dict[str, Any] = {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": item_id,
        "bbox": bbox if bbox else None,
        "geometry": aoi_geom if aoi_geom else None,
        "properties": props,
        "assets": assets,
        "links": [],
    }

    # Minimal JSON-LD DCAT bundle (inline @context; no remote fetch needed)
    dcat: Dict[str, Any] = {
        "@context": {
            "dcat": "http://www.w3.org/ns/dcat#",
            "dct": "http://purl.org/dc/terms/",
            "prov": "http://www.w3.org/ns/prov#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "locn": "http://www.w3.org/ns/locn#",
            "spdx": "http://spdx.org/rdf/terms#",
            "kfm": "urn:kfm:",
        },
        "@graph": [
            {
                "@id": f"urn:kfm:dataset:{item_id}",
                "@type": "dcat:Dataset",
                "dct:title": title,
                "dct:description": description,
                "dct:spatial": {
                    "@type": "dct:Location",
                    "locn:bbox": ",".join(str(x) for x in (bbox or [])),
                } if bbox else {},
                "dct:temporal": {
                    "@type": "dct:PeriodOfTime",
                    "dcat:startDate": temporal_start,
                    "dcat:endDate": temporal_end,
                } if (temporal_start and temporal_end) else {},
                "dcat:distribution": [
                    {
                        "@id": f"urn:kfm:distribution:{item_id}:stac-item",
                        "@type": "dcat:Distribution",
                        "dcat:downloadURL": stac_item_href,
                        "dct:format": "application/geo+json",
                        "dct:title": "STAC Item (GeoJSON)",
                    }
                ],
                "prov:wasGeneratedBy": {
                    "@id": f"urn:kfm:activity:ssurgo-gnatsgo-nasis-stac-delta:{input_fingerprint}",
                    "@type": "prov:Activity",
                },
            }
        ],
    }

    return stac_item, dcat


# ----------------------------
# Minimal QA
# ----------------------------
def minimal_qa(
    stac_item: Dict[str, Any],
    *,
    require_geometry: bool = True,
    require_temporal: bool = True,
    assume_wgs84: bool = True,
) -> List[str]:
    errs: List[str] = []

    geom = stac_item.get("geometry")
    bbox = stac_item.get("bbox")
    props = stac_item.get("properties") or {}

    if require_geometry and not geom:
        errs.append("missing geometry")

    if not bbox or not (isinstance(bbox, list) and len(bbox) == 4):
        errs.append("missing or invalid bbox")
    else:
        try:
            minx, miny, maxx, maxy = map(float, bbox)
            if not (minx < maxx and miny < maxy):
                errs.append("bbox min/max invalid")
            if assume_wgs84:
                if not (-180 <= minx <= 180 and -180 <= maxx <= 180 and -90 <= miny <= 90 and -90 <= maxy <= 90):
                    errs.append("bbox out of WGS84 range (disable with --no-assume-wgs84)")
        except Exception:
            errs.append("bbox not numeric")

    if require_temporal and not (props.get("start_datetime") and props.get("end_datetime")):
        errs.append("missing temporal coverage")

    if geom:
        try:
            g = shape(geom)
            if not g.is_valid:
                errs.append("geometry invalid")
        except Exception:
            errs.append("geometry unparsable")

    return errs


# ----------------------------
# STAC catalog update (optional)
# ----------------------------
def update_catalog_with_item(catalog_path: Path, *, item_href: str) -> bool:
    """
    Adds an `item` link to a STAC catalog/collection JSON if not already present.
    Returns True if catalog changed.
    """
    if not catalog_path.exists():
        return False
    try:
        cat = json.loads(catalog_path.read_text(encoding="utf-8"))
    except Exception:
        return False

    links = cat.get("links")
    if not isinstance(links, list):
        links = []
        cat["links"] = links

    for lnk in links:
        if isinstance(lnk, dict) and lnk.get("rel") == "item" and lnk.get("href") == item_href:
            return False

    links.append({"rel": "item", "href": item_href, "type": "application/geo+json"})
    _atomic_write_json(catalog_path, cat)
    return True


# ----------------------------
# CLI
# ----------------------------
@dataclass
class RunOutputs:
    stac_path: Path
    dcat_path: Path
    fingerprint_path: Path
    catalog_path: Optional[Path] = None


@click.command()
@click.option("--item-id", required=True, help="Stable STAC Item id to emit (e.g., kfm-soils-ssurgo-gnatsgo-nasis-ks).")
@click.option("--title", default="Kansas Soils (SSURGO/gNATSGO/NASIS) — Metadata", show_default=True)
@click.option("--description", default="Auto-derived STAC/DCAT metadata for SSURGO/gNATSGO/NASIS inputs.", show_default=True)
@click.option("--sda-where", default="1=1", show_default=True, help="SQL WHERE fragment for SDA tabular query.")
@click.option("--sda-limit", default=5000, show_default=True, type=int)
@click.option("--offline", is_flag=True, help="Disable network calls (skip SDA).")
@click.option("--ssurgo-zip", type=click.Path(exists=True, dir_okay=False, path_type=Path), required=False)
@click.option("--gnatsgo-zip", type=click.Path(exists=True, dir_okay=False, path_type=Path), required=False)
@click.option("--nasis-sqlite", type=click.Path(exists=True, dir_okay=False, path_type=Path), required=False)
@click.option("--nasis-sql", default="SELECT * FROM legend", show_default=True, help="SQL query executed against NASIS sqlite.")
@click.option("--aoi-geojson", type=click.Path(exists=True, dir_okay=False, path_type=Path), required=False)
@click.option("--aoi-bbox", type=str, required=False, help='AOI bbox as "minx,miny,maxx,maxy" (WGS84).')
@click.option("--out-dir", type=click.Path(file_okay=False, path_type=Path), required=True)
@click.option("--catalog", type=click.Path(dir_okay=False, path_type=Path), required=False, help="Optional STAC root catalog to append an item link.")
@click.option("--dcat-out", type=click.Path(dir_okay=False, path_type=Path), required=True)
@click.option("--state-dir", type=click.Path(file_okay=False, path_type=Path), required=True, help="Directory for fingerprint state files.")
@click.option("--hash-mode", type=click.Choice(["fast", "full"]), default="fast", show_default=True)
@click.option("--commit", is_flag=True, help="Git commit emitted metadata files (only if fingerprint changed).")
@click.option("--commit-message", default="kfm: soils stac/dcat delta metadata update", show_default=True)
@click.option("--rollback", is_flag=True, help="Rollback last delta commit using the rollback token.")
@click.option("--rollback-token-path", type=click.Path(dir_okay=False, path_type=Path), default=Path("./.kfm_last_delta_token"))
@click.option("--allow-dirty", is_flag=True, help="Allow git commit/rollback even if working tree is dirty (not recommended).")
@click.option("--require-temporal/--allow-missing-temporal", default=True, show_default=True)
@click.option("--require-geometry/--allow-missing-geometry", default=True, show_default=True)
@click.option("--assume-wgs84/--no-assume-wgs84", default=True, show_default=True)
def main(
    item_id: str,
    title: str,
    description: str,
    sda_where: str,
    sda_limit: int,
    offline: bool,
    ssurgo_zip: Optional[Path],
    gnatsgo_zip: Optional[Path],
    nasis_sqlite: Optional[Path],
    nasis_sql: str,
    aoi_geojson: Optional[Path],
    aoi_bbox: Optional[str],
    out_dir: Path,
    catalog: Optional[Path],
    dcat_out: Path,
    state_dir: Path,
    hash_mode: str,
    commit: bool,
    commit_message: str,
    rollback: bool,
    rollback_token_path: Path,
    allow_dirty: bool,
    require_temporal: bool,
    require_geometry: bool,
    assume_wgs84: bool,
) -> None:
    """
    Main entrypoint.
    """
    start = Path.cwd()
    repo_root = _git_root(start) or start

    if rollback:
        sha = _git_rollback_revert(repo_root, rollback_token_path, allow_dirty=allow_dirty)
        console.print(f"[bold yellow]Rolled back (reverted) commit:[/bold yellow] {sha}")
        return

    # 1) Read sources + extract signals
    sda_rows = fetch_sda_rows(sda_where, limit=sda_limit, offline=offline)
    nasis_rows = read_sqlite_rows(nasis_sqlite, nasis_sql, limit=5000) if nasis_sqlite else []

    ssurgo_signals = scan_zip_for_signals(ssurgo_zip) if ssurgo_zip else {"exists": False}
    gnatsgo_signals = scan_zip_for_signals(gnatsgo_zip) if gnatsgo_zip else {"exists": False}

    aoi_geom, aoi_bbox_list, aoi_src = _aoi_geometry(aoi_geojson, aoi_bbox)

    # bbox precedence: AOI > zip union bbox > zip bbox candidates
    bbox_candidates: List[Optional[List[float]]] = []
    bbox_candidates.append(aoi_bbox_list)
    bbox_candidates.append(ssurgo_signals.get("geojson_union_bbox"))
    bbox_candidates.append(gnatsgo_signals.get("geojson_union_bbox"))
    # Pull xml bbox candidates too
    bbox_candidates.append(_bbox_union([c.get("bbox") for c in ssurgo_signals.get("bbox_candidates", []) if isinstance(c, dict)]))
    bbox_candidates.append(_bbox_union([c.get("bbox") for c in gnatsgo_signals.get("bbox_candidates", []) if isinstance(c, dict)]))

    bbox = _bbox_union(bbox_candidates)

    # Temporal candidates from SDA + NASIS + zip metadata
    sda_date_fields = ("lrevise", "saverest", "recdate", "effectivedate", "surveydate")
    sda_dates: List[str] = []
    for r in sda_rows[:5000]:
        for k in sda_date_fields:
            if r.get(k):
                sda_dates.append(str(r[k]))

    nasis_dates: List[str] = []
    for r in nasis_rows[:5000]:
        for k in sda_date_fields:
            if r.get(k):
                nasis_dates.append(str(r[k]))

    zip_dates: List[str] = []
    for sig in (ssurgo_signals, gnatsgo_signals):
        for d in sig.get("date_candidates", []):
            if isinstance(d, dict) and d.get("value"):
                zip_dates.append(str(d["value"]))

    temporal_start, temporal_end, temporal_dbg = _coalesce_temporal(sda_dates, nasis_dates, zip_dates)

    ssurgo_fp = _file_xxh64(ssurgo_zip, mode=hash_mode)
    gnatsgo_fp = _file_xxh64(gnatsgo_zip, mode=hash_mode)
    nasis_fp = _file_xxh64(nasis_sqlite, mode=hash_mode)

    # 2) Fingerprint inputs
    input_fp_payload = {
        "item_id": item_id,
        "sda": {
            "where": sda_where,
            "limit": sda_limit,
            "offline": offline,
            "rows_hash": _xxh64_hexdigest(sda_rows[:200]),
            "row_count": len(sda_rows),
        },
        "ssurgo_zip": ssurgo_fp,
        "gnatsgo_zip": gnatsgo_fp,
        "nasis_sqlite": nasis_fp,
        "nasis_sql": nasis_sql,
        "aoi": {"source": aoi_src, "bbox": aoi_bbox_list},
        "signals": {
            "bbox": bbox,
            "temporal": temporal_dbg,
        },
    }
    fingerprint = _xxh64_hexdigest(input_fp_payload)

    state_dir.mkdir(parents=True, exist_ok=True)
    fingerprint_path = state_dir / f"{item_id}.fingerprint"
    old_fp = fingerprint_path.read_text(encoding="utf-8").strip() if fingerprint_path.exists() else ""

    if fingerprint == old_fp:
        console.print(f"[bold cyan]No delta[/bold cyan] — fingerprint unchanged: {fingerprint}")
        return

    # 3) Build outputs (deterministic)
    out_dir.mkdir(parents=True, exist_ok=True)
    stac_path = out_dir / f"{item_id}.geojson"
    stac_href = _repo_relative(repo_root, stac_path)

    # If AOI geometry missing but bbox exists, derive geometry from bbox (deterministic)
    if not aoi_geom and bbox:
        aoi_geom = mapping(box(*bbox))

    # Include source fingerprints where available
    source_summaries = {
        "sources": [
            {"name": "SDA", "url": SDA_URL, "enabled": (not offline), "where": sda_where},
            {"name": "SSURGO zip", "path": _repo_relative(repo_root, ssurgo_zip) if ssurgo_zip else None},
            {"name": "gNATSGO zip", "path": _repo_relative(repo_root, gnatsgo_zip) if gnatsgo_zip else None},
            {"name": "NASIS sqlite", "path": _repo_relative(repo_root, nasis_sqlite) if nasis_sqlite else None, "query": nasis_sql},
        ],
        "signals": {
            "aoi_source": aoi_src,
            "bbox": bbox,
            "temporal_start": temporal_start,
            "temporal_end": temporal_end,
        },
        "input_fingerprints": {
            "ssurgo_zip": ssurgo_fp.get("xxh64"),
            "gnatsgo_zip": gnatsgo_fp.get("xxh64"),
            "nasis_sqlite": nasis_fp.get("xxh64"),
        },
    }

    stac_item, dcat = build_stac_item_and_dcat(
        item_id=item_id,
        title=title,
        description=description,
        aoi_geom=aoi_geom,
        bbox=bbox,
        temporal_start=temporal_start,
        temporal_end=temporal_end,
        input_fingerprint=fingerprint,
        source_summaries=source_summaries,
        stac_item_href=stac_href,
    )

    # 4) QA
    errors = minimal_qa(
        stac_item,
        require_geometry=require_geometry,
        require_temporal=require_temporal,
        assume_wgs84=assume_wgs84,
    )
    if errors:
        console.print(f"[bold red]QA failed[/bold red]: {errors}")
        sys.exit(2)

    # 5) Write outputs + state
    _atomic_write_json(stac_path, stac_item)
    _atomic_write_json(dcat_out, dcat)
    _atomic_write_text(fingerprint_path, fingerprint + "\n")

    catalog_changed = False
    if catalog:
        try:
            catalog_changed = update_catalog_with_item(catalog, item_href=stac_href)
        except Exception:
            catalog_changed = False

    # 6) Report
    table = Table(title="KFM soils STAC/DCAT delta")
    table.add_column("Artifact")
    table.add_column("Path")
    table.add_row("STAC Item", str(stac_path))
    table.add_row("DCAT JSON-LD", str(dcat_out))
    table.add_row("Fingerprint", str(fingerprint_path))
    if catalog:
        table.add_row("Catalog updated?", str(bool(catalog_changed)))
    console.print(table)
    console.print(f"[bold green]New fingerprint[/bold green]: {fingerprint}")
    console.print(f"[bold yellow]Old fingerprint[/bold yellow]: {old_fp or '∅'}")

    # 7) Optional commit
    if commit:
        files = [stac_path, dcat_out, fingerprint_path]
        if catalog and catalog_changed:
            files.append(catalog)

        sha = _git_commit_files(repo_root, files, commit_message, rollback_token_path, allow_dirty=allow_dirty)
        if sha:
            console.print(f"[bold green]Committed[/bold green] {sha} — rollback token saved at {rollback_token_path}")
        else:
            console.print("[yellow]No staged changes to commit[/yellow]")
    else:
        console.print("[yellow]Commit skipped[/yellow] (use --commit to enable)")


if __name__ == "__main__":
    main()
~~~

## 🌐 STAC, DCAT & PROV Alignment

- **STAC**
  - `geometry` + `bbox` (AOI-derived; zip metadata-derived; or bbox-derived geometry)
  - `properties.start_datetime` / `properties.end_datetime` (best-effort from SDA/NASIS + zip XML)
  - `kfm:input_fingerprint` and `kfm:mapping_hints` for lineage and determinism
- **DCAT (JSON-LD)**
  - Inline `@context` (no remote context fetch)
  - Dataset node with spatial bbox + temporal range
  - Distribution linking to the emitted STAC Item

PROV is represented as embedded lineage hints (upgradeable to full PROV/OpenLineage emission later).

## 🧪 Validation & CI/CD

Minimal QA gates:
- Geometry is present and valid (or derived from bbox)
- BBox is sane (min < max; WGS84 range checks when enabled)
- Temporal coverage is parseable and start <= end

Delta behavior:
- If the current fingerprint matches the last recorded fingerprint, the script exits **without writing outputs**.
- With `--commit`, the script stages and commits only the emitted files and writes a rollback token.

Rollback behavior:
- `--rollback` uses `git revert` on the stored SHA (safer than hard reset for governed history).

## ⚖ FAIR+CARE & Governance

- No embedded credentials (SDA is public; local file paths are user-provided)
- Treat raw packages as governed inputs (use DVC/external pointers for large binaries)
- Apply CARE/sovereignty guidance if extending beyond public soils metadata

## 🕰️ Version History

- v11.2.6 (2025-12-16): Initial governed recipe with deterministic mapping + fingerprint delta gate + rollback

---

<div align="center">

**KFM v11.2.6 · STAC/DCAT/PROV Profiles v11 · Governed ETL Recipe**  
Standards: `docs/standards/` · Pipelines: `docs/pipelines/` · Validation: `tools/validation/`

</div>