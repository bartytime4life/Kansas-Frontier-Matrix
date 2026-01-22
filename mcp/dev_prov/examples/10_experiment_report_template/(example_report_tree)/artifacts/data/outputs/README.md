# 📦 Experiment Outputs (Data Artifacts)

![Status](https://img.shields.io/badge/status-template-2ea44f)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%2B%20DCAT%20%2B%20PROV-6f42c1)
![Rigor](https://img.shields.io/badge/ethos-no%20black%20boxes-111111)
![KFM](https://img.shields.io/badge/aligned%20with-KFM%20docs-0b7285)

> [!IMPORTANT]
> This directory contains **machine-generated outputs** for an experiment run (datasets, tiles, reports, manifests, audits).  
> **Treat outputs as immutable artifacts**: if you need to change something, rerun the pipeline and emit a new output version.

---

## 🎯 Purpose

This folder is the **artifact store** for the experiment report template:

- ✅ **Publishable results** (processed datasets, tilesets, exports, figures)
- ✅ **Provenance & audit companions** (run manifests, checksums, evidence manifests, lineage)
- ✅ **UI-ready exports** (Story Nodes, snapshots, offline packs, simulation results)
- ✅ **AI-ready exports** (Focus Mode transcripts + citations + audit panels)

KFM alignment in one sentence: **everything here must be traceable to evidence, processing steps, and governance decisions** — no “black box” outputs.

---

## ✅ What belongs here

- 🧾 **Manifests**: `run_manifest.json`, `source.json`, `checksums.sha256`, `telemetry.ndjson`
- 🧬 **Catalog triplet**: STAC + DCAT + PROV (stored under `meta/`)
- 🗺️ **Geospatial outputs**: GeoParquet, COGs, vector tiles (PMTiles), 3D Tiles
- 🧠 **Models & analytics artifacts**: model cards, evaluation metrics, drift reports
- 🤖 **AI artifacts**: evidence-backed answers, retrieved context, governance flags
- 📖 **Narrative artifacts**: Story Nodes (markdown + JSON config), narrative playback bundles
- 🧪 **QA artifacts**: validation reports, schema checks, graph health checks, policy pack results
- 🔐 **Governance artifacts**: sensitivity labels, access tier manifests, obfuscation logs
- 📦 **Distribution artifacts**: OCI-style packaging metadata, signatures/attestations (optional)

---

## 🚫 What does *not* belong here

- ❌ Raw “as-received” evidence (keep in raw evidence folders / receipts; do not overwrite originals)
- ❌ One-off manual edits to derived data (edit pipeline code/config instead; regenerate deterministically)
- ❌ Secrets (tokens, private keys, credentials)
- ❌ Unattributed exports (if it can’t be traced, it can’t ship)

---

## 🧭 “No Skipping Stages” (KFM pipeline mindset)

> [!TIP]
> If your workflow resembles **Raw → Processed → UI** without a lineage/citation trail, it’s incomplete.

A KFM-style path is typically:

**Raw ➜ Work ➜ Processed ➜ Catalogs (STAC/DCAT/PROV) ➜ Graph ➜ API ➜ UI ➜ Story/Focus**

This `outputs/` folder is where the experiment’s **final, shareable “Processed ➜ UI/Story/AI” products** land — *with their metadata and proof*.

---

## 🗂️ Recommended layout

```text
outputs/
├─ README.md
├─ meta/ 🧾
│  ├─ run_manifest.json
│  ├─ source.json
│  ├─ checksums.sha256
│  ├─ telemetry.ndjson
│  ├─ evidence_manifest.json
│  ├─ stac/ 🛰️
│  │  ├─ collection.json
│  │  └─ items/
│  ├─ dcat/ 🏷️
│  │  └─ dataset.json
│  ├─ prov/ 🧬
│  │  └─ lineage.json
│  └─ qa/ ✅
│     ├─ validation_report.md
│     ├─ schema_checks.json
│     └─ policy_pack_results.json
├─ datasets/ 🗄️
│  ├─ geoparquet/
│  ├─ raster_cogs/
│  └─ tables/
├─ tiles/ 🧱
│  ├─ pmtiles/
│  └─ tiles3d/
├─ graphs/ 🕸️
│  ├─ exports/
│  └─ queries/
├─ ai/ 🤖
│  ├─ focus_mode/
│  └─ audit_panels/
├─ ui/ 🧩
│  ├─ story_nodes/
│  ├─ screenshots/
│  └─ offline_packs/
└─ packages/ 📦
   ├─ oci/
   └─ attestations/
```

> [!NOTE]
> You can simplify this for smaller experiments (e.g., only `meta/` + `datasets/`).  
> The key is: **outputs are discoverable, verifiable, and reproducible**.

---

## 🧾 Required “artifact contract” (minimum per run)

| Artifact | Why it exists | Where |
|---|---|---|
| `run_manifest.json` | Reproducibility anchor: who/what/when/how | `meta/` |
| `checksums.sha256` | Integrity + tamper detection | `meta/` |
| `source.json` | Raw evidence references + retrieval notes | `meta/` |
| `telemetry.ndjson` | Append-only run log (events, counts, warnings) | `meta/` |
| `evidence_manifest.json` | “Evidence-first” map from claims ➜ sources | `meta/` |
| STAC + DCAT + PROV | Findable + standardized metadata + lineage | `meta/stac`, `meta/dcat`, `meta/prov` |
| `validation_report.md` | Human-readable QA snapshot | `meta/qa` |

> [!IMPORTANT]
> If the run can’t produce provenance (STAC/DCAT/PROV) and checksums, **it isn’t a publishable output**.

---

## 🏷️ Naming & versioning rules (recommended)

### 🔑 Identifiers
- `run_id`: unique run identifier (UUID, timestamped slug, or CI run number)
- `artifact_id`: stable logical ID for the output (e.g., `ks_river_gauge_daily_observations`)
- `version`: semver-ish or date-based (e.g., `v0.1.0` or `2026-01-22`)

### 📌 Filename pattern
```
<artifact_id>__<run_id>__<timestamp>__<version>.<ext>
```

### ✅ Good examples
- `ks_county_drought_index__run_7c3b...__20260122T031500Z__v0.3.0.parquet`
- `ks_river_gauges__run_7c3b...__20260122T031500Z__v0.3.0.pmtiles`
- `focus_mode_answer__run_7c3b...__20260122T031500Z__v0.3.0.md`

---

## 🧬 Provenance & metadata (STAC + DCAT + PROV)

### The “catalog triplet” idea
Every publishable dataset output should be paired with:

- 🛰️ **STAC**: footprint + temporal extent + assets + geometry
- 🏷️ **DCAT**: publication metadata, licensing, distribution info
- 🧬 **PROV**: lineage — inputs, transformations, agents, timestamps

### What “evidence-first” means in outputs
A run should produce a machine-readable mapping between:

- **claims/insights** (what the run concluded)
- **supporting data assets** (files in `datasets/`, `tiles/`, `graphs/`)
- **source evidence** (raw receipts, upstream datasets, citations)
- **transformations** (code/config versions)

> [!TIP]
> Think of `evidence_manifest.json` as the “proof ledger” that lets anyone say:  
> “Show me the chain from this map layer all the way back to original sources.”

---

## 🗺️ Geospatial output formats (KFM-friendly)

### 🧱 Vector
- ✅ **GeoParquet** (preferred for analytics + modern pipelines)
- ✅ GeoPackage (portable, GIS-friendly)
- ✅ FlatGeobuf (fast streaming for some workflows)
- ⚠️ GeoJSON (OK for small outputs; avoid for big datasets)

### 🌄 Raster
- ✅ **COG** (Cloud-Optimized GeoTIFF) for rasters that will be served or cached

### 🗺️ Tiles & web delivery
- ✅ **PMTiles** for vector tile packaging + offline packs
- ✅ Cesium/3D workflows: **3D Tiles** (+ glTF assets where applicable)

### 🧭 CRS + spatial rules
- Record CRS on every output (even if you standardize to WGS84 for interchange).
- If you reproject, **it must be a declared transform** in provenance, not a silent step.

---

## 🤖 AI outputs (Focus Mode / evidence-backed assistants)

If this experiment produces AI-generated narrative or Q&A artifacts, store them in `ai/` with:

- 🧾 the **question/prompt**
- 🧠 the **retrieved context** (graph nodes, datasets, documents)
- 🧬 the **citation list** (dataset IDs, STAC assets, document references)
- 🧪 the **audit panel** (influences, governance flags, uncertainty)
- ✅ the **final answer** (human-readable)

Suggested structure:

```text
ai/focus_mode/
├─ session_<run_id>/
│  ├─ question.md
│  ├─ answer.md
│  ├─ citations.json
│  ├─ retrieval_context.json
│  ├─ audit_panel.json
│  └─ governance_flags.json
```

> [!IMPORTANT]
> If an AI output cannot be derived from available evidence, it should explicitly record uncertainty/refusal — never fabricate.

---

## 📖 Narrative outputs (Story Nodes + playback-ready bundles)

Story/Narrative outputs make results **explainable and shareable**:

- 📝 `story.md` (human narrative)
- ⚙️ `story.json` (configuration: chapters, map extents, time ranges, layers)
- 🖼️ assets (figures, images, short clips, thumbnails)

Suggested structure:

```text
ui/story_nodes/
├─ <story_slug>/
│  ├─ story.md
│  ├─ story.json
│  ├─ assets/
│  └─ exports/
```

> [!TIP]
> Keep narratives “citation-aware”: every major claim should point back to a dataset asset or source reference included in `meta/`.

---

## 🧪 QA, governance, and sensitivity outputs

### ✅ QA / validation
Place structured QA artifacts in `meta/qa/`:

- schema validation results
- geospatial sanity checks (bounds, CRS, geometry validity)
- completeness checks (null rates, required columns)
- performance notes (tile generation time, indexing notes)

### 🔐 Sensitivity-aware handling
If the run uses or produces sensitive data:

- include a `sensitivity_manifest.json` describing:
  - classification tier (public / restricted / admin)
  - allowed distributions
  - obfuscation methods (e.g., rounding, generalization)
  - audit trail for what was withheld or blurred

> [!IMPORTANT]
> For public-facing outputs, consider producing **two variants**:
> - `public/` (safe, obfuscated if needed)
> - `restricted/` (full fidelity, access-controlled)
>
> Both variants should be cataloged and prov-linked so the reason for differences is explicit.

---

## 📦 Packaging & distribution (optional but powerful)

For “ship it anywhere” reproducibility, you can package outputs as **content-addressed artifacts**:

- store export bundles under `packages/oci/`
- store signatures/attestations under `packages/attestations/`
- ensure digests match `checksums.sha256`

> [!TIP]
> This mirrors “data treated with the same rigor as code”: versioned, reviewable, signed, rollbackable.

---

## 🧰 Reference & methodology packs (project libraries)

These project files are intentionally broad: they support experiments that span:
- geospatial WebGL + virtual worlds 🗺️🌐
- AI/LLMs + explainability 🤖🔎
- data architecture + Bayesian methods 🧠📈
- multi-language implementation notes 🧑‍💻🧰

<details>
<summary><strong>📚 Resource bundles included in the project (high-level)</strong></summary>

- 🧠 **AI Concepts & more**: curated AI/ML references (PDF portfolio)
- 🗄️ **Data Management / Bayesian**: data architecture + statistical learning references (PDF portfolio)
- 🧑‍💻 **Programming languages & resources**: implementation resources across languages (PDF portfolio)
- 🗺️ **Maps / Google Maps / Virtual Worlds / WebGL / Archaeology**: mapping + rendering + virtual world references (PDF portfolio)

These packs inform how you design experiments and what kinds of outputs you may emit (tiles, scenes, notebooks, evaluation reports, etc.).
</details>

---

## 🔗 Related KFM design docs (alignment targets)

This README is designed to align experiment outputs with the broader KFM system:

- 🧭 **KFM Architecture & Design** (modules, services, standards, growth strategy)
- 🧾 **KFM Data Intake Guide** (immutability, deterministic ETL, catalog triplet, evidence-first publishing)
- 🧩 **KFM UI System Overview** (2D/3D maps, timeline, Story Nodes, offline packs, AR)
- 🤖 **KFM AI System Overview** (Focus Mode, citations, explainability/audit panels)
- ✨ **Latest Ideas & Future Proposals** (new domains, federation, governance maturity)
- 💡 **Additional Project Ideas** (Pulse Threads, conceptual attention nodes, narrative pattern detection, OCI packaging)
- 🚀 **Innovative Concepts** (4D digital twins, AR storytelling, natural-language GIS co-pilots, cultural protocols)

---

## ✅ Reproducibility checklist (printable)

- [ ] Outputs are generated (not hand-edited)
- [ ] `meta/run_manifest.json` present
- [ ] `meta/checksums.sha256` present and matches files
- [ ] `meta/source.json` points to raw evidence / upstream inputs
- [ ] `meta/telemetry.ndjson` captured
- [ ] `meta/evidence_manifest.json` maps claims ➜ assets ➜ sources
- [ ] STAC + DCAT + PROV present and consistent
- [ ] QA artifacts present (at least a `validation_report.md`)
- [ ] Sensitive data handled (manifest + public/restricted split if needed)
- [ ] Optional: packaged + signed for distribution

---

## 🧷 Conventions for contributors

> [!NOTE]
> If you’re adding a new kind of output, also add:
> - a short description in this README
> - a directory under `outputs/` with a clear name
> - a schema or example snippet under `meta/qa/` (so others can validate it)

Happy experimenting 🌾🧪
