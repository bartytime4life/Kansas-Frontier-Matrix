# 🧬 Dataset Provenance Bundles (PROV) — `data/prov/datasets/`

![W3C PROV](https://img.shields.io/badge/W3C-PROV-blue)
![Evidence-first](https://img.shields.io/badge/evidence--first-traceable-success)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-by%20design-brightgreen)

This folder is the **dataset-level lineage ledger** for KFM ✅  
If a dataset is published, it **must** have a provenance (PROV) bundle here.

> **Goal:** make every layer, chart, API response, and AI-derived output traceable to original sources — *“the map behind the map.”* 🧭

---

## 🧠 What belongs here?

### ✅ Yes (belongs in this folder)
- **One PROV bundle per dataset version** (typically JSON or JSON-LD)
- PROV bundles that capture:
  - **Entities**: raw inputs + processed outputs (plus optional intermediates)
  - **Activities**: ETL/processing steps (script/config + run metadata)
  - **Agents**: human + software agents responsible for creation

### ❌ No (does not belong here)
- Raw source files → go to `data/raw/`
- Processed deliverables → go to `data/processed/`
- STAC/DCAT catalog entries → go to `data/stac/` and `data/catalog/dcat/`
- Free-form notes without structured lineage (put those in `docs/`)

---

## 🧱 Non‑negotiable pipeline alignment 🔗

KFM treats provenance as a **boundary artifact** that enables downstream stages.

**Canonical flow (conceptual):**
```mermaid
flowchart LR
  Raw[data/raw/] --> ETL[pipelines/ (ETL jobs)]
  ETL --> Work[data/work/ (optional)]
  ETL --> Proc[data/processed/]
  Proc --> STAC[data/stac/]
  Proc --> DCAT[data/catalog/dcat/]
  ETL --> PROV[data/prov/datasets/]
  STAC --> Graph[graph (Neo4j)]
  DCAT --> Graph
  PROV --> Graph
  Graph --> API[API layer]
  API --> UI[UI + AI surfaces]
```

**Cross-layer expectations (short version):**
- **STAC → Data**: STAC points to the actual files / endpoints in `data/processed/**`
- **DCAT → STAC/Distribution**: DCAT provides discovery + distribution links
- **PROV (this folder) → End-to-end lineage**: raw → work → processed, plus run/config/commit identifiers

---

## 📁 Directory layout

Recommended organization (dataset-centric, versioned):

```text
data/
  prov/
    datasets/
      README.md
      <dataset_id>/
        v1.prov.jsonld
        v2.prov.jsonld
        latest.prov.jsonld        # optional convenience pointer/copy
        attachments/              # optional: small lineage-related artifacts (NOT raw data)
```

> If the repo is currently using a flat naming style (e.g., `rainfall_1850_2020.prov.json`), you can keep it — but **versioning must remain explicit** (foldered or suffixed filenames).

---

## 🏷️ Naming conventions

### Dataset ID (`<dataset_id>`)
- **lowercase + snake_case**
- stable over time (used in catalogs and APIs)
- examples:
  - `ks_hydrology_1880`
  - `census_1900_county_population`
  - `railroads_1870_1910`

### Versioning
Use **dataset-scoped versioning** (simple + explicit):
- `v1`, `v2`, `v3` … (recommended baseline)
- If you adopt semver later, keep `v<major>` compatibility and map semver → DCAT/PROV consistently.

---

## 🧾 Minimum required PROV content (Definition of Done ✅)

A dataset PROV bundle is “publishable” when it includes:

- **Inputs (Entities)**
  - references to raw source files (path + checksum preferred)
  - source URLs / acquisition date (when applicable)
  - license + attribution pointers
- **Outputs (Entities)**
  - the produced artifact(s) in `data/processed/**`
  - stable identifiers for downstream linking
- **Transformation (Activity)**
  - pipeline/script name
  - config path or parameters
  - runtime timestamp(s)
  - run identifier (run ID and/or git commit hash)
- **Agents**
  - software agent (pipeline script/container/version)
  - human agent (maintainer/contributor) when applicable
- **Revision links (when version > 1)**
  - explicit linkage to the previous version (e.g., `prov:wasRevisionOf`)

---

## 🔁 Dataset updates & revision chaining

When a dataset is updated or reprocessed:
1. **Create a new PROV bundle** (don’t overwrite history)
2. **Link the new version to the old**
   - DCAT: `prov:wasRevisionOf` (or equivalent per KFM profile)
   - PROV: reference the activity that derived `v2` from `v1` (if applicable)
3. Keep the chain unbroken:
   - `v3 → v2 → v1`

---

## 🧩 PROV bundle template (starter)

<details>
<summary><strong>📦 Minimal PROV JSON‑LD skeleton</strong> (click to expand)</summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "kfm": "https://example.org/kfm/id/"
  },
  "@id": "kfm:prov/datasets/<dataset_id>/v2",
  "@type": "prov:Bundle",

  "prov:entity": [
    {
      "@id": "kfm:entity/raw/<source_id>",
      "@type": "prov:Entity",
      "dcterms:title": "Raw source snapshot",
      "dcterms:source": "<source_url_or_archive_ref>",
      "dcterms:license": "<license_id_or_url>",
      "prov:location": "data/raw/<domain>/<file>",
      "kfm:checksumSha256": "<sha256>"
    },
    {
      "@id": "kfm:entity/processed/<dataset_id>/v2",
      "@type": "prov:Entity",
      "dcterms:title": "Processed dataset output",
      "prov:location": "data/processed/<domain>/<dataset_id>/...",
      "kfm:checksumSha256": "<sha256>",
      "prov:wasGeneratedBy": "kfm:activity/<run_id>"
    }
  ],

  "prov:activity": [
    {
      "@id": "kfm:activity/<run_id>",
      "@type": "prov:Activity",
      "dcterms:description": "ETL pipeline run producing <dataset_id> v2",
      "prov:startedAtTime": "2026-02-03T00:00:00Z",
      "prov:endedAtTime": "2026-02-03T00:10:00Z",
      "kfm:pipelineScript": "pipelines/<domain>/<script>.py",
      "kfm:pipelineConfig": "pipelines/<domain>/configs/<config>.yaml",
      "kfm:gitCommit": "<commit_hash>",
      "prov:used": [
        "kfm:entity/raw/<source_id>",
        "kfm:entity/processed/<dataset_id>/v1"
      ],
      "prov:wasAssociatedWith": [
        "kfm:agent/software/<pipeline_agent_id>",
        "kfm:agent/human/<contributor_id>"
      ]
    }
  ],

  "prov:agent": [
    {
      "@id": "kfm:agent/software/<pipeline_agent_id>",
      "@type": "prov:SoftwareAgent",
      "dcterms:title": "KFM pipeline runner",
      "kfm:containerImage": "<image_ref_or_digest>",
      "kfm:version": "<pipeline_version>"
    },
    {
      "@id": "kfm:agent/human/<contributor_id>",
      "@type": "prov:Person",
      "dcterms:title": "<name_or_handle>"
    }
  ]
}
```
</details>

📌 **Important:** This is a starter shape. Always conform to:
- `docs/standards/KFM_PROV_PROFILE.md`
- and any schema validation enforced by CI.

---

## ✅ PR checklist (fast sanity pass)

Before opening a PR that adds/updates a dataset:

- [ ] Processed output exists under `data/processed/**`
- [ ] STAC is updated (`data/stac/**`) to point to processed assets
- [ ] DCAT is updated (`data/catalog/dcat/**`) for discoverability + distributions
- [ ] PROV bundle added here (`data/prov/datasets/**`)
- [ ] Dataset version chain is intact (`prov:wasRevisionOf` when applicable)
- [ ] License + attribution are explicit (fail-closed governance expects this)
- [ ] Validation steps are repeatable (documented in domain runbook)

---

## 🧯 “Red flag” rule

If a dataset is visible in the product but **has no PROV bundle**, treat it as **not publishable** 🚫  
Fix provenance before expanding access or building narratives on top of it.

---

## 🔗 Related folders (quick jumps)

- 📦 Processed data: `../../processed/`
- 🧪 Raw snapshots: `../../raw/`
- 🗺️ STAC catalogs: `../../stac/`
- 🗂️ DCAT catalogs: `../../catalog/dcat/`
- 🧰 Pipelines: `../../../pipelines/`
- 📚 Standards: `../../../docs/standards/`
- 🧭 Master guide / architecture: `../../../docs/`

---

## 📚 Project docs to read next

- `docs/MASTER_GUIDE_v13.md` (canonical pipeline + governance)
- `docs/standards/KFM_PROV_PROFILE.md` (PROV profile + required fields)
- `docs/standards/KFM_DCAT_PROFILE.md` + `docs/standards/KFM_STAC_PROFILE.md` (cross-layer linking rules)
- `docs/data/<domain>/README.md` (domain runbooks and ETL notes)

---