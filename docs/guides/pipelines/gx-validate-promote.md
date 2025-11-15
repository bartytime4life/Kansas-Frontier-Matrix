---
title: "🧪 Kansas Frontier Matrix — Great Expectations Validate → Promote Pipeline Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/gx-validate-promote.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-gx-promote-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Great Expectations Validate → Promote Pipeline Guide**  
`docs/guides/pipelines/gx-validate-promote.md`

**Purpose:**  
Define the **canonical KFM workflow** for validating datasets with **Great Expectations (GX)** and then **promoting** validated assets to the **Processed**, **Published**, and **Graph** layers with complete **FAIR+CARE**, **lineage**, **provenance**, and **telemetry** commitments.

This guide standardizes the Validate→Promote pattern used by:  
- STAC ingestion pipelines  
- Remote sensing pipelines (LandsatLook, Sentinel-2, Sentinel-1)  
- Historical / tabular ETL pipelines  
- Hazard, drought, climate, and multi-temporal analysis pipelines  

</div>

---

## 📘 Overview

The **GX Validate → Promote pattern** ensures:

- Input data is fully validated before entering KFM storage  
- All promotions respect FAIR+CARE governance  
- Lineage and telemetry are bound at each step  
- Neo4j + STAC indexes + RDF exports only reference validated assets  
- All failures follow a standard quarantine + issue creation workflow

This guide defines:
1. **Directory model**  
2. **Validation → promotion states**  
3. **GX check suite structure**  
4. **Governance and CARE forcing functions**  
5. **CI/CD triggers and blocking rules**  

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
data/
├── raw/                            # Incoming unverified data
├── work/
│   ├── tmp/                        # Intermediate transforms
│   ├── staging/                    # GX-validated, schema-aligned data
│   └── processed/                  # Pre-publication outputs
├── processed/                      # Certified FAIR+CARE datasets
├── stac/                           # STAC Items/Collections (published)
├── reports/
│   ├── validation/                 # GX summaries
│   ├── fair/                       # CARE audits
│   └── audit/                      # Governance ledgers
└── telemetry/
    └── *.ndjson                    # Stage-by-stage telemetry
~~~~~

---

## 🔄 Validate → Promote Lifecycle

~~~~~mermaid
flowchart TD
  A["Raw / Incoming Data"] --> B["GX Checkpoint<br/>Schema · Ranges · Integrity"]
  B -->|PASS| C["Staging Layer<br/>Schema-Aligned · CARE-tagged"]
  B -->|FAIL| Q["Quarantine<br/>Issue Creation · Telemetry"]
  C --> D["Promotion Gate<br/>FAIR+CARE + Provenance Checks"]
  D -->|PASS| E["Processed Layer"]
  E --> F["Publish<br/>STAC · DCAT · Neo4j · RDF"]
  F --> G["Telemetry + Lineage<br/>Governance Ledger"]
~~~~~

---

## 🧪 1. Great Expectations Checkpoints

KFM standardizes GX checkpoints:

- **Schema Validation**  
- **Uniqueness Rules**  
- **Value Ranges**  
- **Required Fields**  
- **Geo-boundary checks** (if spatial)
- **Temporal rule checks** (OWL-Time alignment)
- **CARE rule checks** (combined with governance pipeline)
- **Link integrity** (STAC, DCAT, references)

### File structure:

~~~~~text
great_expectations/
├── great_expectations.yml
├── checkpoints/
│   ├── <pipeline>_schema.yml
│   └── <pipeline>_integrity.yml
└── expectations/
    ├── schema_<name>.json
    ├── ranges_<name>.json
    └── integrity_<name>.json
~~~~~

### Promotion Condition  
A dataset **CANNOT** be promoted unless:

- All GX suites = **PASS**  
- No warnings exist  
- CARE rules pass  
- Provenance hashes recorded  

---

## 🛡️ 2. Quarantine Workflow

If validation fails:

- Dataset batch is moved to:

~~~~~text
data/work/quarantine/<timestamp>/
~~~~~

- Generated files:
  - `failure_report.json`
  - `last_failure_summary.md`
  - Raw offending data files (optional)
- CI automatically opens a GitHub Issue (peter-evans/create-issue-from-file)
- Telemetry entry added (stage=validate, status=failure)

Quarantined data **must not** be used downstream.

---

## 🧭 3. Staging Layer Rules

Data in `data/work/staging/` is:

- Fully GX-validated  
- Schema-harmonized  
- CARE-labeled  
- Provenance-linked  
- Ready for promotion gating

Required metadata injected:

- `kfm:validation_version`
- `kfm:validated_at`
- `kfm:care_label`
- `kfm:checksum_sha256`
- `kfm:source_ids`
- Provenance chain reference

---

## ⚖️ 4. FAIR+CARE Promotion Gate

Promotion from `data/work/staging/` → `data/processed/` requires:

### Mandatory Conditions

| Requirement | Description |
|------------|-------------|
| FAIR | STAC/DCAT fields complete, open format, linked metadata |
| CARE | sovereignty, sensitive AOIs masked, consent metadata present |
| Provenance | lineage record created & validated |
| Integrity | checksums match lineage records |
| Telemetry | validate telemetry exists & required fields present |

Promotion fails if **any** of these conditions are not met.

### Governance Check

Promotion gate uses:

~~~~~text
docs/reports/audit/data_provenance_ledger.json
~~~~~

The ledger receives:

- Dataset ID  
- Validation suite IDs  
- Telemetry summary  
- CARE decisions  
- Transformation log  

---

## 🆙 5. Promotion → Processed Layer

Promotion writes:

~~~~~text
data/processed/<dataset_id>/<version>/
~~~~~

+ a `processed_manifest.json` containing:

- Version  
- Checksums  
- GX suite versions  
- Telemetry reference  
- CARE label  
- Provenance references  
- Linked STAC + DCAT IDs  

After promotion:

- Pre-registered STAC Items are created/updated  
- Neo4j graph nodes/edges built  
- RDF/GeoSPARQL exports constructed  

---

## 🌐 6. Publish Phase (Optional Per Pipeline)

For pipelines that include publication:

- STAC Items written to `data/stac/published/items/**`  
- Collections updated  
- Neo4j nodes merged  
- RDF/JSON-LD published  
- Catalogs synchronized (STAC ↔ DCAT)

All published items must be:

- Hash-locked (sha256)  
- Telemetry-linked  
- Listed in the governance ledger  

---

## 📡 7. Telemetry Requirements

Every stage MUST emit NDJSON:

~~~~~text
data/telemetry/<pipeline>.ndjson
~~~~~

Required fields:

- `stage`  
- `status`  
- `duration_ms`  
- `rows` / `pixels_processed`  
- `energy_wh`, `co2_g`  
- `care_violations`  
- `errors`  
- `stac_items`, `graph_nodes`, etc.  

Aggregated to:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

CI (`telemetry-export.yml`) rejects missing fields.

---

## 🧬 8. Lineage Requirements

Each pipeline stage MUST append lineage info validated by:

~~~~~text
src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
~~~~~

Required elements:

- PROV-O Activity  
- PROV-O Entity (source + outputs)  
- GeoSPARQL geometry (if spatial)  
- CARE attributes  
- STAC parent/child linkages  
- Transformation chain  

Lineage written to:

~~~~~text
data/processed/lineage/<dataset>/<version>.jsonld
~~~~~

---

## 🧪 Local Developer Run (Recommended)

~~~~~bash
# 1. Validate
great_expectations checkpoint run <checkpoint>

# 2. Promote
python scripts/promote.py \
  --input data/work/staging/<dataset> \
  --output data/processed/<dataset>/<version>

# 3. Publish (optional)
python scripts/publish_stac.py
python scripts/publish_graph.py
~~~~~

---

## 🛠️ CI/CD Integration

Promotion is blocked unless all workflows succeed:

- `stac-validate.yml`  
- `faircare-validate.yml`  
- `telemetry-export.yml`  
- `docs-lint.yml`  
- `data-contract-validate.yml`  
- `ai-model-audit.yml` (if AI-enabled)  

Failures automatically generate issues with pointers to quarantined data.

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Pipeline Governance Team | Initial Validate→Promote workflow guide; aligned with GX v1.x, FAIR+CARE, telem. v3, KFM Markdown Protocol. |

---

<div align="center">

**Kansas Frontier Matrix — Validate → Promote Pattern**  
FAIR+CARE ETL × Deterministic Validation × Reproducible Science × Governance by Design  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>

