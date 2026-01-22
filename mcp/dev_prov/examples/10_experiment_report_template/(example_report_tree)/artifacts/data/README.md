# 📦 `artifacts/data/` — Experiment Data Bundle (Evidence-First) ⛓️🧪

![template](https://img.shields.io/badge/template-10__experiment__report__template-2b6cb0)
![provenance](https://img.shields.io/badge/provenance-required-0ea5e9)
![reproducible](https://img.shields.io/badge/reproducibility-first-22c55e)

This folder is the **data backpack** for this experiment report: the inputs you used, the outputs you produced, and the metadata needed to **re-run + verify** the results—without “mystery files”.

> 💡 Design intent: mirror KFM’s “no black box data” philosophy—**every file is traceable, licensed, checksummed, and explainable**.

---

## 🧭 What belongs here?

✅ Put **everything referenced by the report** here *or* include an **immutable pointer** (hash-addressed) to where it lives.

- **Inputs**: raw sources, downloaded snapshots, curated extracts
- **Intermediates**: scratch outputs, temporary conversions, debug exports
- **Final outputs**: processed data used in results/figures/tables
- **Metadata**: manifests, checksums, provenance lineage, catalog records
- **Governance**: sensitivity labels, redaction notes, access constraints

❌ Don’t put:
- “random_final_v7_REALFINAL.csv” with no context
- data without a license/source
- large binaries without a pointer strategy (OCI/S3/etc.) and integrity proof

---

## 🗂️ Recommended layout (template-friendly)

```text
artifacts/data/
  README.md                         👈 you are here
  manifest.yaml                     🧾 human+machine index of this bundle
  checksums.sha256                  🔐 tamper-evident hashes (all files)

  raw/                              📥 as-acquired inputs (immutable mindset)
    <dataset_or_source_name>/
      source.json                   🔗 where it came from (URL/provider/etc.)
      ...files...

  work/                              🧪 intermediates (NOT publishable by default)
    <pipeline_or_notebook_name>/
      run_config.json               ⚙️ params, seeds, env, versions
      logs/                         🪵 stdout/stderr, QA logs
      ...files...

  processed/                         🗄️ canonical outputs used by this report
    <dataset_or_product_name>/
      ...files...

  catalog/                           🗂️ “evidence triplet” metadata (optional but recommended)
    stac/                           🗺️ STAC Item/Collection JSON
    dcat/                           🧭 DCAT JSON-LD (discovery)
    prov/                           ⛓️ PROV JSON-LD (lineage)

  governance/                        ⚖️ access + sensitivity + redaction notes
    classification.yaml
    redaction_notes.md

  pointers/                          📌 for large assets stored elsewhere
    oci_artifacts.yaml              📦 OCI/ORAS refs + digests + signature notes
    external_uris.yaml              🌐 stable URLs + expected hashes

  samples/                           🧃 tiny subsets for quick tests / CI smoke checks
    ...files...
```

---

## 🧾 `manifest.yaml` (required)

Treat this as the table-of-contents for your data bundle.

### Minimal schema (suggested)
```yaml
bundle:
  id: EXP-000
  title: "Experiment Report Data Bundle"
  created_utc: "2026-01-22T00:00:00Z"
  owner: "team-or-handle"

datasets:
  - id: "raw.usgs.stream_gauges.2026-01-01"
    stage: "raw"
    path: "raw/usgs_stream_gauges/"
    source:
      provider: "USGS"
      uri: "https://example.com/source"
    license:
      spdx: "CC0-1.0"
    integrity:
      checksums_file: "../checksums.sha256"
    notes: "As-acquired snapshot used for ingest test."

  - id: "processed.kfm.hydro.low_flow_clusters.v1"
    stage: "processed"
    path: "processed/low_flow_clusters/"
    derived_from:
      - "raw.usgs.stream_gauges.2026-01-01"
    methods:
      pipeline: "pipelines/hydro/low_flow_detector.py"
      run_config: "../work/low_flow_detector/run_config.json"
    outputs_used_in_report:
      - "../figures/flow_cluster_map.png"
```

---

## 🔐 `checksums.sha256` (required)

A simple tamper-evidence mechanism: every file in this folder tree gets hashed.

**Convention**
- One line per file: `<sha256>  <relative/path>`
- Re-run hashes whenever files change
- CI can verify them to “fail closed”

---

## 🧪 Raw → Work → Processed (promotion rule)

To preserve trust and avoid accidental use of half-baked outputs:

- `raw/` = what you got (minimal transformation)
- `work/` = sandbox outputs (experiments, drafts, debug)
- `processed/` = **what the report actually depends on**

> ✅ If a work result is used in the report, **promote it** to `processed/` and document the promotion in `manifest.yaml`.

---

## 🗺️ Geospatial tips (if relevant)

**Prefer open, analysis-friendly formats:**
- Vector: GeoParquet / GeoJSON (small), Shapefile (legacy)
- Raster: COG (`.tif`) for efficient tiling + partial reads
- Tiles: PMTiles (portable), MBTiles (common)

**Always record**
- CRS / EPSG code
- spatial extent (bbox)
- temporal range (if applicable)

---

## 🤖 AI/ML experiment add-ons (if relevant)

If this experiment involves ML or LLM work, store these alongside the data:

- `work/<run>/run_config.json` (hyperparameters, seeds, split strategy)
- `work/<run>/metrics.json` (evaluation outputs)
- `work/<run>/prompts/` (prompt sets, system prompts, templates)
- `processed/<model_or_output>/model_card.md` (intent, limits, eval summary)

---

## ⚖️ Governance & sensitivity (don’t skip)

Put a simple label on datasets and outputs:

- `public`
- `internal`
- `restricted` (needs review / access controls / redaction)

If you must generalize or obfuscate sensitive locations, document:
- what was altered
- why
- how to reproduce the “unredacted” version (if allowed)

---

## 🧳 Large files: “pointer, don’t panic” 📦

If an asset is too large for the repo:
1. Store it in a registry/bucket **immutably** (digest-addressed)
2. Put the pointer + digest in `pointers/`
3. Keep a tiny `samples/` subset for quick verification

Example `pointers/oci_artifacts.yaml` (pattern)
```yaml
artifacts:
  - id: "processed.kfm.geology.surficial.pmtiles.v2026-01-11"
    oci_ref: "oci://ghcr.io/<org>/<repo>:20260111"
    digest: "sha256:<...>"
    media_type: "application/vnd.pmtiles"
    verification:
      signature: "cosign (keyless or key-based)"
```

---

## ✅ “Definition of Done” checklist 🧰

- [ ] All files are referenced in `manifest.yaml`
- [ ] All files are included in `checksums.sha256`
- [ ] Every dataset has **source + license**
- [ ] Any derived dataset lists **inputs + method**
- [ ] Any sensitive content is labeled + documented
- [ ] Report references datasets by **stable IDs** (not ad-hoc filenames)

---

## 📚 Reference library (project docs used as inspiration) 📖✨

> Some project “mega PDFs” are PDF Portfolios (bundles). If you open them locally, you’ll find additional embedded docs/books for deeper patterns.

- 📘 KFM Data Intake Guide (STAC/DCAT/PROV, promotion workflow, validation)
- 🧭 KFM AI System Overview (governance + citations + drift)
- 🗺️ KFM UI Overview (provenance surfaced in UI + exports)
- 🏗️ KFM Architecture/Design (policy gates, provenance-first)
- 💡 KFM Innovative Concepts + Future Proposals (AR/sims + provenance-carrying layers)
- 🧪 Scientific Method / Experiment Protocol doc (rigor + traceability)
- 🔐 Data Mining privacy/security references (privacy-aware outputs)
- 🧰 Geospatial engineering references (APIs, routing, GIS patterns)
