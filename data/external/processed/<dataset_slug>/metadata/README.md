---
kfm:
  # 🧩 Replace all {{placeholders}} before considering this dataset "published"
  dataset_slug: "{{dataset_slug}}"            # folder name (kebab-case recommended)
  dataset_title: "{{dataset_title}}"          # human-friendly title
  domain: "external"
  stage: "processed"
  status: "draft"                            # draft | published | deprecated

  versioning:
    dataset_version: "0.1.0"                 # bump on breaking changes
    upstream_version_or_date: "{{upstream_version_or_date}}"
    last_updated: "YYYY-MM-DD"

  source:
    name: "{{upstream_source_name}}"
    url: "{{upstream_source_url}}"
    accessed_at: "YYYY-MM-DD"
    citation: "{{upstream_citation}}"        # preferred citation text (if available)

  license:
    spdx: "{{license_spdx_id}}"              # e.g., CC-BY-4.0, ODbL-1.0, etc.
    url: "{{license_url}}"
    attribution: "{{attribution_text}}"

  sensitivity:
    classification: "public"                 # public | restricted | sensitive
    pii_present: false
    sovereignty_review_required: false       # CARE / community governance trigger

  ownership:
    steward: "{{data_steward}}"
    maintainer: "{{maintainer}}"
    contact: "{{contact_email_or_issue_link}}"

  catalogs:                                  # canonical “boundary artifacts”
    stac_collection: "../../../../stac/collections/{{dataset_slug}}.collection.json"
    stac_items_dir: "../../../../stac/items/{{dataset_slug}}/"
    dcat_dataset: "../../../../catalog/dcat/{{dataset_slug}}.dcat.jsonld"
    prov_bundle: "../../../../prov/{{dataset_slug}}__v{{dataset_version}}.prov.json"

  local_artifacts:                           # optional: dataset-local convenience copies
    checksums: "checksums.sha256"
    manifest: "manifest.json"
    data_dictionary: "data_dictionary.md"
    schema: "schema.json"
    qa_report: "qa_report.md"
---

# 🧾 Dataset Metadata — {{dataset_title}} (`{{dataset_slug}}`)

![stage](https://img.shields.io/badge/stage-processed-blue)
![domain](https://img.shields.io/badge/domain-external-6f42c1)
![status](https://img.shields.io/badge/status-draft-lightgrey)
![metadata](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT%20%2B%20PROV-brightgreen)
![governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-informational)

📍 **Location:** `data/external/processed/{{dataset_slug}}/metadata/README.md` (you are here)

> [!IMPORTANT]
> **No hand-edits to processed data.** Changes to `data/external/processed/{{dataset_slug}}/` should come from deterministic pipelines (config-driven, idempotent).  
> Raw inputs should remain read-only and traceable. If something is wrong, fix the pipeline + bump the dataset version.

---

## 🔎 Quick Links

- 🧊 **STAC Collection:** `{{kfm.catalogs.stac_collection}}`
- 🧊 **STAC Items dir:** `{{kfm.catalogs.stac_items_dir}}`
- 🗃️ **DCAT Dataset:** `{{kfm.catalogs.dcat_dataset}}`
- 🧬 **PROV Bundle:** `{{kfm.catalogs.prov_bundle}}`
- 🧾 **Local checksums:** `checksums.sha256`
- 🧾 **Local manifest:** `manifest.json`

> [!NOTE]
> “Canonical catalogs” live under `data/stac/`, `data/catalog/dcat/`, and `data/prov/` (or `data/provenance/` in older layouts).  
> This folder is the **human-facing runbook** + dataset-local integrity artifacts.

---

## 📌 Dataset Snapshot

| Field | Value |
|---|---|
| **Dataset slug** | `{{dataset_slug}}` |
| **Title** | {{dataset_title}} |
| **Domain** | `external` |
| **Stage** | `processed` |
| **Dataset version** | `{{dataset_version}}` |
| **Upstream source** | {{upstream_source_name}} |
| **Upstream version/date** | {{upstream_version_or_date}} |
| **License (SPDX)** | `{{license_spdx_id}}` |
| **Sensitivity** | `{{classification}}` |
| **Spatial coverage** | `{{bbox_or_region}}` |
| **Temporal coverage** | `{{start_date}} → {{end_date}}` |
| **Primary formats** | {{formats}} |
| **Primary CRS** | {{crs}} |

---

## 📁 What’s in this folder

```text
📁 data/external/processed/{{dataset_slug}}/
├── 📁 metadata/                          👈 this directory
│   ├── 📄 README.md                      👈 you are here
│   ├── 📄 manifest.json                  ✅ required (recommended)
│   ├── 📄 checksums.sha256               ✅ required (recommended)
│   ├── 📄 data_dictionary.md             ⭐ recommended
│   ├── 📄 schema.json                    ⭐ recommended (or /schemas/)
│   ├── 📄 qa_report.md                   ⭐ recommended
│   └── 📁 notes/                         📝 optional (edge cases, caveats)
└── 📁 assets/                            (optional) dataset-local asset bundle
```

### ✅ Minimum expectation (dataset-local)
- [ ] `manifest.json` lists every asset in `../` (and/or `../assets/`) with **path, media_type, size_bytes, sha256**
- [ ] `checksums.sha256` includes a sha256 for every asset referenced in the manifest
- [ ] This `README.md` is filled in (no placeholder fields remain)

---

## 🌐 Canonical “Boundary Artifacts” (Required)

These are the records downstream systems rely on (catalogs → graph → API → UI).

### ✅ Required records
- [ ] **STAC Collection** exists and validates ✅
- [ ] **STAC Item(s)** exist (one per asset or logical item) and validate ✅
- [ ] **DCAT Dataset entry** exists and validates ✅
- [ ] **PROV bundle** exists and validates ✅

### 📎 Where they live
| Artifact | Canonical path (expected) | Purpose |
|---|---|---|
| 🧊 STAC Collection | `data/stac/collections/{{dataset_slug}}.collection.json` | dataset-level discoverability (spatial/temporal summary) |
| 🧊 STAC Items | `data/stac/items/{{dataset_slug}}/*.item.json` | asset-level metadata + links to data files |
| 🗃️ DCAT Dataset | `data/catalog/dcat/{{dataset_slug}}.dcat.jsonld` | high-level catalog record (title/desc/license/distributions) |
| 🧬 PROV Bundle | `data/prov/{{dataset_slug}}__v{{dataset_version}}.prov.json` | lineage: raw → work → processed + agents + parameters |

> [!TIP]
> If this dataset is **non-spatial**, still create a STAC Collection for consistency, and use STAC links/distributions to point at the assets.

---

## 🔗 Cross‑Layer Linkage Rules (Non‑negotiable)

### STAC → Data (assets)
- STAC Items must link to the actual files (or stable URLs) for the processed outputs.
- STAC must also carry **source attribution** + **license** for the asset.

### DCAT → STAC / Distributions
- DCAT should point to STAC and/or direct downloads (distributions).
- DCAT is the “front door” for discovery; STAC is the “deep details.”

### PROV end‑to‑end
- PROV must represent **raw inputs → intermediate work → processed outputs**.
- Include pipeline run identifiers (run ID and/or git commit hash), timestamps, and configuration references.

### Graph references catalogs (no duplication)
- Graph nodes should reference catalog IDs (e.g., STAC Item IDs) rather than embedding full payloads.

---

## 🧬 Provenance & Reproducibility

### 📥 Inputs (raw sources)
- **Raw location:** `data/external/raw/{{dataset_slug}}/`
- **Notes:** {{raw_input_notes}}

### 🧪 Transformations (pipeline)
Fill these in so anyone can reproduce the dataset.

- **Pipeline name:** `{{pipeline_name}}`
- **Pipeline entrypoint:** `src/pipelines/{{pipeline_path}}`
- **Config used:** `{{config_path}}`
- **Run command (example):**
  ```bash
  # example only — replace with your real pipeline command
  python -m src.pipelines.{{pipeline_module}} --config {{config_path}} --dataset {{dataset_slug}}
  ```
- **Run ID:** `{{run_id}}`
- **Git commit:** `{{git_commit}}`
- **Runtime environment:** `{{docker_image_or_conda_env}}`

### 🧾 Parameters & assumptions
- {{parameter_1}}
- {{parameter_2}}
- {{assumption_1}}

> [!WARNING]
> If your processing includes redaction/generalization (sensitivity), **document it here and in PROV**, and ensure downstream layers only serve the redacted outputs.

---

## ✅ Validation & QA

### Required checks
- [ ] ✅ **Checksum verification** passes (`checksums.sha256`)
- [ ] ✅ **Schema validation** passes (`schema.json` or referenced schema)
- [ ] ✅ **Geometry validity** (if vector): no self-intersections; consistent winding; valid polygons
- [ ] ✅ **CRS sanity**: clearly declared + consistent across files
- [ ] ✅ **Attribute hygiene**: documented units; no cryptic codes without dictionary
- [ ] ✅ **Sensitivity scan** (if applicable): no PII / protected locations leaked

### QA Outputs
- **QA report:** `qa_report.md` (or link to CI artifact)  
- **Known issues:** {{known_issues}}

<details>
<summary>📋 Suggested QA checklist (expand)</summary>

- File integrity: counts, sizes, hashes
- Schema: required fields present; allowed enums; null handling
- Spatial: bbox within expected region; invalid geometry count = 0
- Temporal: expected date ranges; timezone normalized
- Statistics: row counts, min/max ranges, missingness
- Sampling: spot-check N records against raw sources
- Metadata: STAC/DCAT/PROV validate and cross-link correctly

</details>

---

## 🧾 Data Dictionary & Schema

### Data dictionary
- **Local:** `data_dictionary.md`
- **Required fields documented:** {{required_fields_documented}}

### Schema
- **Local:** `schema.json` (or `schemas/*.json`)
- **Validation tool:** {{schema_validator_tool}}

---

## 🗜️ Large Assets & Storage Notes

If assets are too large for git:
- ✅ Prefer **Git LFS** for binaries (GeoTIFFs, large Parquet, etc.), **or**
- ✅ Store a **pointer + checksum** and provide a fetch script (documented & deterministic)

Document the strategy:
- **Strategy used:** {{lfs_or_fetch_strategy}}
- **Fetch command (if applicable):**
  ```bash
  # example only
  ./tools/fetch_assets.sh --dataset {{dataset_slug}} --manifest metadata/manifest.json
  ```

---

## 🧭 Update Policy & Versioning

### What requires a version bump?
- **Breaking changes** (schema changes, units changes, different geometry meaning, removed fields) → bump **minor/major**.
- **New data points** with same schema meaning → bump **patch** (or minor if substantive).
- **Upstream refresh** → record upstream version/date and bump as appropriate.

### Changelog (keep it short)
- `{{dataset_version}}` — {{change_summary}}

> [!NOTE]
> Dataset versioning is separate from overall system releases. Don’t ship breaking dataset changes “silently.”

---

## ⚖️ Governance, FAIR + CARE, & Sovereignty

### Governance checklist
- [ ] License confirmed and compatible with redistribution
- [ ] Source attribution included (STAC + DCAT + README)
- [ ] Sensitivity classification assigned and justified
- [ ] No PII leaked OR approved redaction documented
- [ ] Sovereignty review completed (if applicable)
- [ ] “AI/evidence artifact” clearly labeled (if applicable)

### CARE notes (if relevant)
- **Authority to Control:** {{authority_to_control_notes}}
- **Collective Benefit:** {{collective_benefit_notes}}
- **Responsibility & Ethics:** {{ethics_notes}}

---

## 🧩 Downstream Integration Notes (Optional but helpful)

- **Graph ingest status:** {{graph_ingest_status}}
- **Graph IDs / node keys:** {{graph_ids_or_keys}}
- **API exposure:** {{api_endpoints_or_dataset_route}}
- **UI layer name(s):** {{ui_layer_names}}

---

## 👥 Maintainer Notes

- **Primary maintainer:** {{maintainer}}
- **How to report issues:** {{contact_email_or_issue_link}}
- **Next TODOs:**
  - [ ] {{todo_1}}
  - [ ] {{todo_2}}

