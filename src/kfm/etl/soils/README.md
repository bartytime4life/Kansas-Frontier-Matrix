---
title: "🧱 Kansas Frontier Matrix — Soils ETL Module (SSURGO/gNATSGO · CDC · STAC/DCAT/PROV)"
path: "src/kfm/etl/soils/README.md"
version: "v11.2.6"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Data Engineering & Soils Domain Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Module README"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles: []

intent: "etl-module-overview"
audience:
  - "Data Engineering"
  - "Soils Domain"
  - "Catalog + Provenance Engineering"
  - "Reliability + Governance"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Data Engineering & Soils Domain Board · FAIR+CARE Council"

doc_uuid: "urn:kfm:doc:src:kfm:etl:soils:v11.2.6"
semantic_document_id: "kfm-soils-etl-module-v11.2.6"
event_source_id: "ledger:kfm:doc:src:kfm:etl:soils:v11.2.6"
commit_sha: "<latest-commit-hash>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_schema_ref: "../../../schemas/telemetry/etl-soils-v11.json"
openlineage_profile_ref: "../../../docs/standards/provenance/openlineage-profile-v11.md"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"

tags:
  - "soils"
  - "ssurgo"
  - "gnatsgo"
  - "nrcs"
  - "cdc"
  - "etl"
  - "stac"
  - "dcat"
  - "prov"
  - "openlineage"
---

<div align="center">

# 🧱 **Kansas Frontier Matrix — Soils ETL Module (SSURGO/gNATSGO · CDC · STAC/DCAT/PROV)**  
`src/kfm/etl/soils/README.md`

**Purpose**  
Implement **deterministic, replayable change-data-capture (CDC)** ingestion for NRCS soils (SDA tabular; SSURGO/gNATSGO patterns), producing **normalized partitions**, plus **STAC/DCAT/PROV** and **OpenLineage** artifacts for governed discovery and lineage.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC%2FDCAT%2FPROV-Aligned-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This module implements **deterministic, replayable CDC ingestion** for NRCS soils (SDA tabular; SSURGO/gNATSGO patterns), producing:

- **Normalized tabular outputs** (canonical units, stable partitions)
- **STAC Collections/Items** linking to emitted data assets
- **DCAT Dataset/Distributions** for catalog interoperability
- **PROV-O + OpenLineage** provenance for lineage governance

Design goal: **idempotent runs**.

> Same inputs + same config ⇒ same partitions + same checksums + same catalog records.

---

## 🗂️ Directory Layout

~~~text
📁 src/kfm/etl/soils/
├── 📄 README.md                         — This file (governed module README)
├── 🧾 cdc_config.yaml                   — Since/until, chunk keys, tables, unit rules, paths
├── 🐍 sda_postrest.py                   — SDA post.rest client (retry, paging)
├── 🐍 cdc_extract.py                    — Date-bounded extraction + incremental semantics
├── 🐍 deterministic_chunk.py            — Stable partition iterator (areasymbol → mukey)
├── 🐍 normalize_units.py                — Canonical units (BD, SOC, depth, textures)
├── 🐍 stac_emit.py                      — STAC emit + validation hooks
├── 🐍 dcat_emit.py                      — DCAT JSON-LD emit
├── 🐍 semver_policy.py                  — Delta-aware version bump logic (advisory)
├── 🐍 main.py                           — Orchestrator (idempotent entrypoint)
└── 📁 validators/
    ├── 🐍 schema_validator.py           — Required columns & table expectations
    ├── 🐍 unit_validator.py             — Dimensional sanity & ranges
    └── 🐍 prov_validator.py             — Required PROV fields & linkage checks
~~~

Related data products (default house paths; config may override):

~~~text
📁 data/soils/
├── 📁 raw/ssurgo/                        — Raw pulls (JSONL/CSV) per table/window
└── 📁 processed/ssurgo/                  — Normalized Parquet partitions (area=.../mukey=...)
📁 data/stac/soils/ssurgo/                — STAC Collection + Items
📁 data/dcat/soils/ssurgo/                — DCAT dataset.jsonld (and distributions)
📁 reports/soils/ssurgo/                  — Validation logs, delta reports, audit bundles
~~~

---

## 🧭 Context

### What “CDC” means here

CDC is implemented as:

- a **date-bounded pull** on an appropriate last-updated field (table dependent),
- followed by **deterministic chunking** and **stable partition replacement**.

Supported CDC modes by policy/config (implementation may select one):

- **Replace-by-partition** (default): rewrite `area=.../mukey=.../table.parquet` for affected partitions.
- **Append-with-ledger** (optional): append new rows and maintain a supersession ledger (**requires governance approval**).

### Determinism contract (non-negotiable)

Determinism is enforced by:

- stable ordering before partitioning (`areasymbol`, `mukey`, then deterministic sort),
- fixed partition paths and naming,
- canonical unit conversions applied consistently,
- idempotent re-runs over the same window (no duplicate partitions; stable checksums).

---

## 📦 Data & Metadata

### Inputs

- **NRCS Soil Data Access (SDA)** tabular endpoint via `post.rest`
- CDC window: `since` (inclusive, UTC), `until` (exclusive, UTC)
- Target tables (e.g., `mapunit`, `component`, `chorizon`)
- Stable chunk key strategy (default: `areasymbol` then `mukey`)

### Outputs

- Raw snapshots (traceability): `data/soils/raw/ssurgo/*`
- Normalized Parquet partitions: `data/soils/processed/ssurgo/area=.../mukey=...`
- STAC Collection/Items referencing emitted assets
- DCAT JSON-LD dataset and distributions
- PROV payload embedded in STAC + exported alongside OpenLineage events
- Reports (validators + delta summaries): `reports/soils/ssurgo/`

### Configuration (minimum viable)

`cdc_config.yaml` SHOULD include:

- `since` / `until`
- `tables`
- `keys` (e.g., `areasymbol`, `mukey`)
- `page_size`
- `unit_rules` (table/column conversions and validation ranges)
- `paths` (raw/processed/stac/dcat/reports)

---

## 🧱 Architecture

### Execution

Local run:

~~~bash
python -m pip install -r requirements.txt
python src/kfm/etl/soils/main.py
~~~

CI run:

- Invoked via governed pipeline workflow with **contract + catalog + provenance** validation gates.
- Expected artifacts:
  - STAC validation report
  - DCAT JSON-LD validation report
  - PROV/OpenLineage emission + schema validation report
  - Delta report + advisory semver bump decision

### Unit normalization

Canonical conversions (defaults; extend per-table as needed):

- Depths: **cm → m**
- Bulk density: **g/cm³ → kg/m³**
- Soil organic carbon / OM: **% → fraction (0–1)**

Post-normalization checks:

- non-negative depths; monotonic horizon depths where applicable,
- plausible density bounds (domain-configurable),
- fraction bounds for SOC/OM and textures.

### Semantic versioning policy (advisory)

The module emits a recommended bump based on delta magnitude:

- **MAJOR**: breaking schema/unit/provenance changes, or large corpus change (policy threshold)
- **MINOR**: moderate deltas/new partitions/new tables (non-breaking)
- **PATCH**: small deltas/bugfixes/metadata-only changes

Authoritative release version remains governed by KFM release policy.

### Troubleshooting

- **Empty extract**: verify `since/until` and the selected last-updated field for that table.
- **Validation failures**: inspect `reports/soils/ssurgo/*`; update `cdc_config.yaml` unit rules only under governance.
- **Non-deterministic outputs**: confirm stable sorting before grouping and stable partition naming.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- One **Collection** per dataset family (e.g., `kfm-soils-ssurgo`)
- One **Item** per table per CDC window (or optionally per chunk)
- Assets include:
  - `normalized` Parquet directory reference (or per-partition hrefs)
  - `raw` JSONL/CSV snapshot reference
- Extra fields:
  - `exported_at` (UTC ISO8601)
  - `kfm:profile` (KFM-STAC v11)
  - embedded `prov` payload

### DCAT

- `dcat:Dataset` with `dcat:distribution` entries per Item asset
- `dct:provenance` links to PROV activity summary (JSON-LD)

### PROV-O + OpenLineage

Minimum required:

- `prov:activity` identifier (e.g., `kfm:ssurgo:cdc`)
- `prov:exported_at` timestamp
- `prov:agent` and runtime version
- CDC window (`since`, `until`)
- source identifiers where available (e.g., SDA table refs, NASIS ids if present)

---

## 🧪 Validation & CI/CD

Validators under `validators/` are mandatory in governed runs:

- **Schema**: required columns per table (fail-fast)
- **Units**: dimensional correctness + range sanity (fail-fast)
- **Provenance**: required PROV fields + STAC/DCAT linkage (fail-fast)
- **STAC**: collection/item validation (fail-fast)

Validation outputs MUST be written to:

- `reports/soils/ssurgo/` (JSON summaries + human-readable logs)

---

## ⚖ FAIR+CARE & Governance

### Security, privacy, and sovereignty

- Do not ingest restricted/protected cultural site data into public soils products.
- Respect NHPA §304 and Indigenous sovereignty policies when soils layers intersect sensitive site contexts.
- Prefer minimal, auditable transforms; record all transformations in PROV/OpenLineage.
- No secrets committed: endpoint access must rely on CI-managed secrets where applicable.

### Ownership and change control

Changes to any of the following MUST be reviewed under the **FAIR+CARE Council** and the **Soils Domain Board**, with updated validation reports:

- unit conversions,
- schema requirements,
- provenance fields,
- partition strategy,
- STAC/DCAT profiles,
- CDC mode selection (especially append-with-ledger).

---

## 🕰️ Version History

- v11.2.6 — Governed module README aligned to KFM-MDP v11.2.6; documents CDC, normalization, and catalog/provenance outputs.

---

<div align="center">

🧱 **KFM — Soils ETL Module (SSURGO/gNATSGO · CDC · STAC/DCAT/PROV)**  
Deterministic Pipelines · Open Provenance · FAIR+CARE Governance

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[📘 Docs Root](../../../docs/README.md) ·
[🧭 Data Architecture](../../../docs/architecture/data/README.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

