---
title: "🧪 Kansas Frontier Matrix — GX Validate → Promote Pipeline Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/gx-validate-promote.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-gx-promote-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "gx-validate-promote"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Great Expectations Validate → Promote Pipeline Guide**  
`docs/guides/pipelines/gx-validate-promote.md`

**Purpose**  
Define the **canonical KFM v10.4.2 Validate → Promote pipeline pattern** based on  
**Great Expectations (GX)**, **FAIR+CARE v2**, **Telemetry v2**, and  
**Lineage v2**, ensuring every dataset moves safely from  
**Raw → Staging → Processed → Published → Graph/RDF/STAC/DCAT**  
with **deterministic**, **auditable**, and **reproducible** steps.

This pattern is used across:

- STAC ingestion pipelines  
- Remote sensing pipelines (Landsat, Sentinel-1/2/3, NAIP, MODIS, VIIRS)  
- Historical/tabular ETL pipelines  
- Hazard, drought, climate, temporal analysis pipelines  
- AI/agent-assisted pipelines (post-GX)

</div>

---

# 📘 Overview

The **Validate → Promote** pattern ensures that:

- Incoming data is rigorously validated before being allowed into KFM storage  
- CARE v2 governance rules are applied immediately  
- Telemetry v2 (energy, CO₂e, care_violations, errors, metrics) is recorded  
- Lineage v2 (PROV-O + CIDOC + GeoSPARQL + CARE v2) is produced  
- All promotions follow the **Publishing Gate v10.4.x**  
- Dataset failures consistently enter **Quarantine**  
- STAC/DCAT, Neo4j, RDF, and Focus Mode integrations only reference **validated assets**

This guide defines the:

1. Directory model  
2. GX suite structure  
3. Validation-to-promotion state machine  
4. CARE v2 rules at validation  
5. Telemetry + lineage requirements  
6. Promotion contract (Processed Layer)  
7. Publishing integration (optional)  
8. CI/CD blocking logic  

---

# 🗂️ Directory Layout (Authoritative KFM v10.4.2)

~~~text
data/
├── raw/                               # Incoming unverified data
├── work/
│   ├── tmp/                           # Ephemeral / intermediate transforms
│   ├── staging/                       # GX-validated, schema-aligned, CARE-labeled data
│   ├── quarantine/                    # Failed validation batches
│   └── validated/                     # Optional domain-specific review layer
├── processed/                         # Certified FAIR+CARE datasets (post-promotion)
├── stac/                              # Published STAC Items/Collections
├── dcat/                              # Published DCAT JSON-LD
├── rdf/                               # GeoSPARQL/RDF exports
├── lineage/                           # Lineage v2 bundles (PROV-O, CIDOC CRM, CARE v2)
├── telemetry/                         # NDJSON telemetry logs per stage
└── reports/
    ├── validation/                    # GX reports
    ├── fair/                          # CARE audits
    └── audit/                         # Governance ledger entries
~~~

---

# 🔄 Validate → Promote Lifecycle (GitHub-Safe Mermaid)

```mermaid
flowchart TD

A["Incoming Data (raw)"] --> B["GX Checkpoint<br/>Schema · Ranges · Integrity"]
B -->|PASS| C["Staging Layer<br/>Schema-aligned · CARE-tagged"]
B -->|FAIL| Q["Quarantine<br/>Issue Creation · CARE Flags · Telemetry v2"]
C --> D["Promotion Gate<br/>FAIR+CARE v2 · Lineage v2 · Provenance Checks"]
D -->|PASS| E["Processed Layer<br/>Certified FAIR+CARE v2 Dataset"]
E --> F["Optional Publish<br/>STAC · DCAT · Neo4j · RDF"]
F --> G["Governance Ledger + Telemetry v2"]
````

---

# 1️⃣ Great Expectations (GX) Validation

GX Checkpoints MUST verify:

## 1.1 Structural Schema

* Required fields present
* Field types correct
* Nullability constraints
* Unique keys (if required)
* Temporal coverage sanity (OWL-Time alignment for time-series datasets)
* Geometry validity (if spatial)

## 1.2 Ranges & Integrity

* Value ranges
* Geo-boundary checks (Kansas AOI, bounding boxes)
* CRS correctness
* Sentinel/Landsat QA bitmask parity
* File size & row-count sanity checks

## 1.3 CARE v2 Pre-Checks

Although full governance happens at “Promotion Gate”, GX performs:

* PII detection warnings
* Sensitive attribute warnings
* Sovereignty overlap hints
* Indigenous data hints
* License + consent fields (if provided)

These generate **warnings**, not **hard errors**, unless configured otherwise.

---

# 2️⃣ Validation Outcomes

## 2.1 PASS → Enter Staging Layer

Validation PASS moves dataset to:

```text
data/work/staging/<dataset>/<run_id>/
```

A `staging_manifest.json` is created with:

* `validated_at`
* `gx_suites_passed[]`
* `careHints[]`
* `checksum_sha256`
* `record_count`
* `provenance_input_hash`
* `telemetryRef`

This layer contains:
**verified structure → not yet published → awaiting Promotion Gate**.

## 2.2 FAIL → Quarantine

Validation FAIL sends dataset to:

```text
data/work/quarantine/<run_id>/
```

Files written:

* `failure_report.json`
* `gx_errors.json`
* `care_flags.json`
* Offending rows (optional)
* Telemetry v2 for the failed run

A GitHub Issue is automatically created via:

`peter-evans/create-issue-from-file`

---

# 3️⃣ Staging Layer Rules

Data in **Staging** must be:

* 100% GX validated
* CARE-labeled (`careLabel`, `maskingStrategy`, `sovereigntyFlags`)
* Lineage-ready
* Checksum-locked
* Semantic versioning determined (patch/minor/major)

Staging metadata injected:

```json
{
  "kfm:validated_at": "...",
  "kfm:validation_version": "v10.4.2",
  "kfm:careLabel": "public",
  "kfm:checksum_sha256": "...",
  "kfm:record_count": 123456,
  "kfm:provenance_input_hash": "...",
  "kfm:telemetryRef": "telemetry/validate-<run>.ndjson"
}
```

---

# 4️⃣ FAIR+CARE v2 Promotion Gate

This is the **hard gate** controlling entry into the `processed/` layer.

Promotion MUST fail if ANY of the following checks fail:

## 4.1 FAIR Requirements

| Requirement      | Description                                       |
| ---------------- | ------------------------------------------------- |
| Accessibility    | Open format, accessible metadata, non-proprietary |
| Interoperability | STAC/DCAT fields complete, CRS correct            |
| Reusability      | License present, provenance links complete        |
| Findability      | Identifiers stable, versioned                     |

## 4.2 CARE v2 Requirements

| Rule              | Description                                 |
| ----------------- | ------------------------------------------- |
| Consent & Context | Required consent metadata present if needed |
| Sovereignty       | Tribal/heritage AOIs masked/generalized     |
| Equity            | Sensitive attributes controlled             |
| Responsibility    | Governance metadata complete                |

Governance validation uses:

```text
docs/standards/governance/ROOT-GOVERNANCE.md
```

All CARE v2 fields are re-checked before promotion:

* `careLabel`
* `maskingStrategy`
* `sovereigntyFlags[]`
* `careReason`

## 4.3 Provenance Requirements

* Input → output relations recorded
* Provenance input hash matches Staging manifest
* Lineage v2 bundle produced and validated
* SBOM + manifest created

## 4.4 Telemetry v2 Requirements

* Telemetry emitted for validation + promotion stages
* Required fields must exist:

  * `duration_ms`
  * `rows_processed` / `pixels_processed`
  * `energy_wh`
  * `co2_g`
  * `care_violations`
  * `errors[]`

Promotion is blocked if telemetry is incomplete.

---

# 5️⃣ Promotion → Processed Layer

Promotion writes:

```text
data/processed/<dataset>/<version>/
```

Artifacts:

* `processed_manifest.json`
* `data.json` or `data.parquet`
* `lineage.jsonld` (Lineage v2)
* `telemetry.ndjson`
* `checksums.txt`
* Optional domain rasters/vectors (processed)

`processed_manifest.json` includes:

* SemVer
* CARE v2 values
* Provenance refs
* Telemetry summary
* STAC/DCAT IDs (post-stage)

This dataset is now **certified** and ready for publishing.

---

# 6️⃣ Publish Phase (Optional but Common)

Publishing writes:

* **STAC Items**
* **STAC Collections** (if needed)
* **DCAT Dataset JSON-LD**
* **Neo4j graph nodes/relationships**
* **RDF/GeoSPARQL triples**

Requires:

* Hash-locking every asset
* Telemetry linking
* Governance ledger update

Publishing follows the **Publishing Gate v10.4.2** standard.

---

# 7️⃣ Telemetry v2 Requirements

Telemetry for GX Validate → Promote MUST include:

* `stage` (`validate`, `promote`)
* `status`
* `record_count`
* `schema_checks`
* `faircare_checks`
* `duration_ms`
* `http_codes` (if applicable)
* `energy_wh`, `co2_g`
* `care_violations`
* `errors`

Written to:

```text
data/telemetry/gx-validate-promote.ndjson
```

Aggregated to:

```text
releases/v10.4.2/pipeline-telemetry.json
```

---

# 8️⃣ Lineage v2 Requirements

Every promotion must produce a lineage bundle:

```text
data/processed/lineage/<dataset>/<version>.jsonld
```

Bundle includes:

* PROV-O Activity
* PROV-O Entity chain
* GeoSPARQL geometry (if spatial)
* CARE v2 metadata
* STAC/DCAT references
* Telemetry summary
* Transformation chain

Validated against:

```text
src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
```

---

# 🧪 Local Developer Flow

```bash
# 1. Validate
great_expectations checkpoint run <checkpoint>

# 2. Promote
python scripts/promote.py \
  --input data/work/staging/<dataset> \
  --version vYYYYMMDD

# 3. Publish (optional)
python scripts/publish_stac.py
python scripts/publish_graph.py
python scripts/publish_rdf.py
```

---

# 🛠 CI/CD Integration

Promotion MUST be blocked unless ALL pass:

| Workflow                   | Purpose                      |
| -------------------------- | ---------------------------- |
| `gx-validate.yml`          | GX checkpoint validation     |
| `faircare-validate.yml`    | CARE v2 governance           |
| `lineage-validate.yml`     | Lineage v2 bundle validation |
| `stac-validate.yml`        | STAC correctness             |
| `dcat-validate.yml`        | DCAT JSON-LD validation      |
| `linked-data-validate.yml` | RDF/GeoSPARQL correctness    |
| `telemetry-export.yml`     | Telemetry v2 correctness     |
| `docs-lint.yml`            | KFM-MDP v10.4.2 compliance   |
| `sbom-validate.yml`        | SBOM + supply chain checks   |

Quarantine / issue creation must be triggered on failure.

---

# 🕰 Version History

| Version | Date       | Summary                                                                                                                                     |
| ------: | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Complete KFM v10.4.2 upgrade: CARE v2, Lineage v2, Telemetry v2, governance-gated promotion, GitHub-safe Mermaid, SBOM+Manifest integration |
| v10.3.1 | 2025-11-14 | Initial Validate→Promote workflow guide                                                                                                     |

---

<div align="center">

**Kansas Frontier Matrix — GX Validate → Promote Pattern (v10.4.2)**
Deterministic Validation × FAIR+CARE v2 × Provenance Integrity × Publishing Gate Compliance
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
