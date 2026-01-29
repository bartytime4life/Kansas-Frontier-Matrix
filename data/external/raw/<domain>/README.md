# 🧱 External Raw Data — `<domain>`  

![Stage](https://img.shields.io/badge/stage-raw-blue)
![Scope](https://img.shields.io/badge/scope-external-purple)
![Governance](https://img.shields.io/badge/provenance-first-success)
![Principles](https://img.shields.io/badge/principles-FAIR%20%2B%20CARE-informational)

📍 **Folder:** `data/external/raw/<domain>/`  
🎯 **Mission:** Store **immutable, byte-for-byte snapshots** of externally sourced data for the **`<domain>`** domain — the “map behind the map” 🗺️🔎 (provenance-first, evidence-backed).:contentReference[oaicite:0]{index=0}

---

## ⚡ Quick Rules (Read This First)

> [!IMPORTANT]
> **Raw means raw.** This directory holds **original source artifacts** (or pointers to them) with **no transformations**.  
> Any conversion, cleaning, georeferencing, OCR, tiling, reprojection, etc. happens **after** raw — in work/processed stages.:contentReference[oaicite:1]{index=1}

✅ **DO**
- Keep **original downloads** intact (same bytes as source).:contentReference[oaicite:2]{index=2}
- Record **where it came from** (URL/archive ref), **what license applies**, and **when/how it was retrieved**.
- Add **checksums** so we can prove integrity over time.
- Treat each new pull as a **new version** (don’t overwrite history).

🚫 **DON’T**
- Don’t “fix” files here (even “minor” edits).
- Don’t commit secrets/keys.
- Don’t shortcut the pipeline (Raw → Processed → Catalog/Prov → Database → API → UI).:contentReference[oaicite:3]{index=3}

---

## 🧭 Domain Profile (Fill This In)

| Field | Value |
|---|---|
| **Domain slug** | `<domain>` |
| **What it covers** | _e.g., historical topo maps, land parcels, hydrology, census, remote sensing, etc._ |
| **Primary upstream sources** | _e.g., USGS, NOAA, Kansas Historical Society, etc._ |
| **Update cadence** | _one-time / monthly / quarterly / ad-hoc_ |
| **Steward / Maintainer** | `@handle` |
| **Default license expectation** | _Public domain / CC / ODbL / custom TOU_ |
| **Sensitive data?** | _None / restricted / review required_ |

> [!NOTE]
> KFM governance emphasizes **traceability, reproducibility, and auditability** — every dataset and derived artifact should link back to original sources.:contentReference[oaicite:4]{index=4}

---

## 🗂️ Recommended Folder Layout

Here’s a **domain-friendly** structure that keeps raw immutable while still being organized:

```text
📁 data/
  📁 external/
    📁 raw/
      📁 <domain>/
        📄 README.md                👈 you are here
        📄 sources.json             🧾 source registry (per-domain)
        📄 CHECKSUMS.sha256         🔐 integrity proofs
        📁 licenses/                ⚖️ downloaded license/ToS texts (when available)
        📁 provider_a/              🛰️ group by upstream provider
          📁 dataset_x/
            📁 vYYYYMMDD/           🧊 versioned snapshots (never overwrite)
              🗄️ original_file.ext
              🗄️ original_file.ext.aux.xml   (if source includes it)
```

Why this shape:
- A **catalog of inputs** is foundational (URLs, extents, coverage, notes).:contentReference[oaicite:5]{index=5}
- Versioning preserves reproducibility and avoids “silent drift.”

---

## 🧾 `sources.json` (Per-Domain Source Registry)

A lightweight “source-of-truth” inventory for **inputs**. Inspired by the project’s catalog-first approach (STAC-like metadata + source info).:contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}

### ✅ Suggested schema (example)

```json
{
  "domain": "<domain>",
  "datasets": [
    {
      "id": "provider_a.dataset_x",
      "title": "Dataset X (Provider A)",
      "upstream_url": "https://example.org/datasets/x",
      "retrieved_at": "YYYY-MM-DD",
      "retrieval_method": "download|api|bulk",
      "license": {
        "name": "Public Domain|CC-BY-4.0|ODbL|Custom",
        "url": "https://example.org/license",
        "notes": "Any attribution / restrictions / redistribution limits"
      },
      "coverage": {
        "spatial": "Kansas (statewide) OR bbox/geometry ref",
        "temporal": "YYYY-YYYY OR YYYY-MM-DD..YYYY-MM-DD"
      },
      "files": [
        {
          "path": "provider_a/dataset_x/vYYYYMMDD/original_file.ext",
          "sha256": "<computed>",
          "size_bytes": 123456789
        }
      ],
      "notes": "Any upstream quirks, missing metadata, known issues"
    }
  ]
}
```

> [!TIP]
> If your downstream processing builds a STAC collection/item later, keep that **out** of raw. Raw only holds the **inputs** and their acquisition metadata.

---

## 🔐 Checksums & Integrity

Store checksums at the domain root (or per dataset/version):

- `CHECKSUMS.sha256` should be reproducible and stable.
- Compute against the **exact bytes** stored in raw.

Example:

```bash
# from data/external/raw/<domain>/
find . -type f ! -name "CHECKSUMS.sha256" -print0 \
  | sort -z \
  | xargs -0 sha256sum > CHECKSUMS.sha256
```

Why: this supports provable integrity and audit trails, aligning with KFM’s provenance-first design.:contentReference[oaicite:8]{index=8}

---

## ⚖️ Licensing, Attribution, and “Fail Closed”

> [!CAUTION]
> If we don’t know the license/terms, we treat it as **blocked** until clarified.

KFM policy prefers **fail-closed** governance: CI should prevent data ingestion when license/metadata requirements aren’t met.:contentReference[oaicite:9]{index=9}

### Minimum requirements for each dataset
- License name + link (or archived license text in `licenses/`)
- Attribution requirements (if any)
- Redistribution constraints (if any)
- Any privacy/community restrictions (CARE)

---

## 🧊 Large Files (Git vs. DVC vs. Object Storage)

Raw datasets can be huge (rasters, imagery, LiDAR, etc.). Prefer:
- **DVC** pointers in Git + data in remote storage
- Or **object storage** (S3-compatible) with stable URIs
- Or Git LFS (if you already standardized on it)

The project explicitly anticipates large/binary data needing external storage + reference pointers rather than stuffing Git with massive files.:contentReference[oaicite:10]{index=10}

> [!NOTE]
> Even if the bytes live elsewhere, **raw still needs the evidence trail**: `sources.json` + checksums (for pointer manifests) + license docs.

---

## 🔁 Canonical Handoff to Next Stages

Raw is only step 1. The canonical order is:

```text
Raw → Processed → Catalog/Prov → Database → API → UI
```

Any shortcut is considered flawed unless explicitly justified.:contentReference[oaicite:11]{index=11}

### After raw is committed, the next moves typically are:
- `data/external/work/<domain>/` — scratch/intermediate (unzips, staging, temporary outputs)
- `data/external/processed/<domain>/` — cleaned, standardized outputs (COGs, GeoJSON, etc.)
- `data/catalog/` or `data/stac/` — STAC/DCAT metadata for discovery and reproducibility:contentReference[oaicite:12]{index=12}

---

## ✅ “Adding a New Raw Source” Checklist

Use this checklist to keep contributions consistent:

- [ ] Create provider/dataset/version folder: `provider_x/dataset_y/vYYYYMMDD/`
- [ ] Download **original files** (no edits)
- [ ] Add/update `sources.json`
- [ ] Save license/ToS text under `licenses/` (if applicable)
- [ ] Generate `CHECKSUMS.sha256`
- [ ] Ensure no secrets / tokens / PII are included
- [ ] Commit with message: `data(raw/<domain>): add <dataset> vYYYYMMDD`

---

## 📚 Project Alignment & References

This README follows KFM’s **provenance-first** + **pipeline-driven** architecture and the repo’s staged data lifecycle design (raw/work/processed + catalog/prov).:contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}

### Key project documents (for deeper context)
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint** :contentReference[oaicite:15]{index=15}  
  - Provenance-first framing + FAIR/CARE:contentReference[oaicite:16]{index=16}  
  - Canonical pipeline order:contentReference[oaicite:17]{index=17}

- **MARKDOWN_GUIDE_v13 (Repo + Data Lifecycle conventions)** :contentReference[oaicite:18]{index=18}  
  - Staged data lifecycle (raw/work/processed):contentReference[oaicite:19]{index=19}  
  - Raw is immutable snapshot storage:contentReference[oaicite:20]{index=20}  
  - Governance “fail closed” philosophy:contentReference[oaicite:21]{index=21}  
  - Handling large/binary data via DVC/object storage:contentReference[oaicite:22]{index=22}  
  - Citation metadata patterns (`CITATION.cff`):contentReference[oaicite:23]{index=23}

- **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** :contentReference[oaicite:24]{index=24}  
  - Repository/data catalog layout (sources/raw/processed/stac):contentReference[oaicite:25]{index=25}  
  - STAC-like catalog emphasis for source traceability:contentReference[oaicite:26]{index=26}

---

## 🧩 Template Notes (Replace These)

- Replace `<domain>` everywhere with your domain slug.
- Update the **Domain Profile** table.
- Add `sources.json`, `CHECKSUMS.sha256`, and a `licenses/` folder once you ingest your first dataset.

