---
title: "🏷️ Kansas Frontier Matrix — Pipeline Versioning Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-versioning-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏷️ **Kansas Frontier Matrix — Pipeline Versioning Architecture**  
`src/pipelines/architecture/versioning/README.md`

**Purpose:**  
Define the **semantic versioning, artifact immutability rules, rollbacks, compatibility constraints, and lineage guarantees** that apply to every KFM pipeline.  
Ensures **deterministic replays**, **time-travel debugging**, **unbroken provenance**, and **FAIR+CARE-governed dataset evolution** for all ETL, AI, geospatial, metadata, and graph pipelines.

</div>

---

## 📘 Overview

The KFM versioning system covers:

- Pipeline code versions  
- Dataset & artifact versions  
- STAC/DCAT metadata versions  
- Model versions (Focus Transformer family)  
- Graph schema versions  
- Governance record versions  
- Telemetry schema versions  

**Versioned artifacts must be immutable.**  
All rollbacks must be **pointer-based**, never destructive.

This file defines the *full versioning contract* for KFM v10.3+.

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/architecture/versioning/
├── README.md                     # This document
├── patterns/                     # Versioning & release pattern examples
├── schemas/                      # JSON Schemas for version metadata
├── rules/                        # Constraints & compatibility rules
└── examples/                     # Sample version manifests
~~~~~

---

## 🧩 Versioning Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Pipeline Code Version<br/>Git SHA · SemVer"] --> B["Artifact Version<br/>Dataset · STAC · Parquet · COG"]
  B --> C["Metadata Version<br/>DCAT · PROV-O · lineage"]
  C --> D["Release Bundle<br/>manifest.zip · sbom.spdx.json"]
  D --> E["Telemetry Version<br/>runtime · energy · CO₂e"]
  E --> F["Governance Ledger<br/>Append-only"]
~~~~~

---

## 🏷️ 1. Semantic Versioning Rules (SemVer)

All pipelines and artifacts must use strict **x.y.z** versioning:

- **MAJOR (x)** – Breaking schema or structural changes  
- **MINOR (y)** – Backward-compatible new features  
- **PATCH (z)** – Fixes, updates, or non-breaking improvements  

Examples:

- `hydrology_flow_v10.3.1`  
- `focus-transformer-v2.4.3`  
- `historic_maps_v5.1.0`  

**Never reuse a version number.**

---

## 📦 2. Artifact Versioning Rules

All output artifacts MUST be stored using **immutable version directories**:

~~~~~text
s3://kfm/artifacts/{dataset}/{version}/<payload>
~~~~~

Every artifact must include:

- `version`  
- `checksum (sha256)`  
- `provenance`  
- `care_label`  
- `date_published`  
- `stac_item` link

Artifacts are immutable forever.

---

## 🔁 3. Rollback Protocol (Pointer-Based)

Rollbacks MUST NOT regenerate old artifacts.

Instead, update the pointer:

~~~~~text
s3://kfm/artifacts/{dataset}/latest.json
~~~~~

`latest.json` contains:

```json
{
  "version": "v10.3.1",
  "uri": "s3://kfm/artifacts/dataset/v10.3.1/",
  "checksum": "sha256:...",
  "telemetry_ref": "releases/v10.3.0/focus-telemetry.json"
}
```

**Never delete, overwrite, or mutate** an old version.

---

## 🧮 4. STAC / DCAT Versioning

### STAC Items
Must include:

- `version`  
- `deprecated` (optional flag)  
- `previous_version`  
- `next_version`  

### DCAT Datasets  
Must maintain:

- `dct:hasVersion`  
- `dct:isVersionOf`  
- `dct:provenance` chain  

All version updates must be published to:

```
data/stac/
data/reports/dcat_exports/
```

---

## 🧬 5. Model Versioning (AI / Focus Mode)

Every model must:

- Use semantic versioning  
- Publish a model card  
- Include training provenance  
- Emit checksum + hyperparameters  
- Log drift against prior versions  

Model artifacts stored in:

```
src/ai/models/{model_name}/{version}/
```

Example:

```
focus-transformer-v2/2.4.1/
```

---

## 🧱 6. Graph Schema Versioning

Graph migrations MUST be versioned:

~~~~~text
src/graph/migrations/
├── v10.3.0/
├── v10.3.1/
└── v10.4.0/
~~~~~

Migration files must include:

- Up/Down scripts  
- CIDOC class alignment  
- GeoSPARQL/WKT consistency  

Each migration stored in governance ledger.

---

## 🔐 7. Governance Metadata Versioning

Governance entries must include:

- `governance_schema_version`  
- `reviewer_id`  
- `conditions`  
- `sovereignty_notes`  
- `care_label_version`  
- `provenance_model_version`

All governance metadata is **append-only**.

---

## 📡 8. Telemetry Schema Versioning

Telemetry schemas live in:

```
schemas/telemetry/
```

Every pipeline MUST emit telemetry matching the current version:

- v2.x for UI  
- v3.x for pipelines  
- v1.x for governance summaries  

If mismatched → CI fails.

---

## 📘 9. Version Manifest Specification

Each release must include a manifest:

```
releases/<version>/manifest.zip
```

Manifest MUST contain:

- STAC index  
- Neo4j export metadata  
- Telemetry snapshot  
- Version compatibility matrix  
- SBOM (SPDX)  
- Pipeline lineage logs  
- CARE review entries  

Example snippet:

~~~~~json
{
  "release": "v10.3.0",
  "artifacts": [
    "hydrology_flow_v10.3.0",
    "focus-transformer-v2.4.0"
  ],
  "sbom": "sbom.spdx.json",
  "manifest_checksum": "sha256:...",
  "governance_reviewed": true
}
~~~~~

---

## 📊 10. Version Compatibility Matrix (Required)

| Component | Compatible Versions |
|-----------|---------------------|
| Pipelines | v10.2.x → v10.3.x |
| STAC | 1.0.x only |
| DCAT | 3.x only |
| Neo4j Schema | v10.x |
| Focus Transformer | ≥ v2.3.0 |
| Telemetry Schema | v3.x |

If incompatible versions are detected → pipeline blocked.

---

## 🧾 Example Version Metadata Record

~~~~~json
{
  "dataset_id": "usgs_streamflow_ks",
  "version": "v10.3.1",
  "previous_version": "v10.3.0",
  "checksum": "sha256:48af...",
  "care_label": "public",
  "stac_item": "streamflow_ks_v10.3.1",
  "dcat_dataset": "streamflow-hydrology",
  "lineage": ["prov:Entity", "prov:Activity", "prov:wasGeneratedBy"],
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Full v10.3 pipeline versioning rules; added governance & telemetry schema integration. |
| v10.2.2 | 2025-11-12 | Pipeline Team | Initial versioning architecture for KFM v10 pipelines. |

---

<div align="center">

**Kansas Frontier Matrix — Versioning Architecture**  
Immutable Artifacts × Deterministic Replays × Ethical Governance × Provenance Integrity  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Pipeline Architecture](../README.md)

</div>