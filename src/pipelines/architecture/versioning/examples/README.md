---
title: "🧬 Kansas Frontier Matrix — Pipeline Versioning Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/examples/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-versioning-examples-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Pipeline Versioning Examples**  
`src/pipelines/architecture/versioning/examples/README.md`

**Purpose:**  
Provide canonical examples of **dataset versioning**, **artifact immutability**, **schema upgrades**, **STAC/DCAT version alignment**, and **FAIR+CARE-aware version lifecycle** within Kansas Frontier Matrix (KFM) pipelines.  
These examples illustrate **true semantic versioning (SemVer)** and **pipeline–artifact coupling** required by MCP v6.3.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Examples-success"/>

</div>

---

## 📘 Overview

Versioning in KFM ensures:

- **Immutability** of historical artifacts  
- **Deterministic lineage lookup**  
- **Auditable scientific reproducibility**  
- **Compatibility across STAC/DCAT catalogs**  
- **FAIR+CARE governance stability**  
- **Cross-pipeline consistency**  

This document provides **validated example records** for:

- Versioned artifacts  
- Versioned STAC Items  
- Versioned metadata  
- Schema migrations  
- Semantic version increment decisions  
- Governance-aware version approval  

---

## 📁 Directory Layout

~~~~~text
src/pipelines/architecture/versioning/examples/
├── README.md                     # This file
├── artifact_version.json         # Example versioned artifact entry
├── stac_item_version.json        # Example versioned STAC Item
├── schema_migration.json         # Example schema migration event
└── governance_version_record.json # Governance approval for version changes
~~~~~

---

## 📦 Example — Versioned Artifact Entry

~~~~~json
{
  "artifact_id": "hydrology_flow_ks",
  "version": "v10.3.1",
  "artifact_uri": "s3://kfm/artifacts/hydrology_flow_ks/v10.3.1/output.parquet",
  "checksum": "sha256:c7bbf233a12fbb5e32aa...",
  "created_at": "2025-11-13T20:14:00Z",
  "care_label": "public",
  "lineage_ref": "data/lineage/hydrology_flow_ks/v10.3.1/lineage.json",
  "telemetry_ref": "releases/v10.3.0/focus-telemetry.json",
  "governance_ref": "docs/reports/audit/versioning_ledger.json"
}
~~~~~

---

## 🗺️ Example — Versioned STAC Item (STAC 1.0 + Versioning Extension)

~~~~~json
{
  "id": "hydrology_flow_ks_v10.3.1",
  "type": "Feature",
  "stac_version": "1.0.0",
  "properties": {
    "title": "Hydrology Flow (Kansas)",
    "version": "v10.3.1",
    "datetime": "2025-11-13T20:14:00Z",
    "kfm:care_label": "public",
    "kfm:provenance": "data/lineage/hydrology_flow_ks/v10.3.1/lineage.json",
    "kfm:checksum": "sha256:c7bbf233a12fbb5e32aa..."
  },
  "geometry": null,
  "links": [
    {
      "rel": "version",
      "href": "hydrology_flow_ks_v10.3.0.json"
    },
    {
      "rel": "version",
      "href": "hydrology_flow_ks_v10.2.2.json"
    }
  ],
  "assets": {
    "data": {
      "href": "s3://kfm/artifacts/hydrology_flow_ks/v10.3.1/output.parquet",
      "type": "application/x-parquet"
    }
  }
}
~~~~~

---

## 🔧 Example — Schema Migration Event

~~~~~json
{
  "migration_id": "schema_migration_2025_11_13_v10.3.1",
  "pipeline_id": "hydrology_flow_ks",
  "old_schema": "v10.2.2",
  "new_schema": "v10.3.1",
  "changes": [
    "Added kfm:care_label to STAC properties",
    "Updated temporal coverage metadata",
    "Updated checksum extension to SHA-256 only"
  ],
  "breaking_change": false,
  "requires_reprocessing": false,
  "governance_ref": "docs/reports/audit/schema_migrations_ledger.json"
}
~~~~~

---

## ⚖️ Governance Example — Version Approval Record

~~~~~json
{
  "governance_decision_id": "gov_version_approval_2025_11_13_hydro4",
  "dataset_id": "hydrology_flow_ks",
  "old_version": "v10.3.0",
  "new_version": "v10.3.1",
  "reviewer": "FAIR+CARE Council",
  "care_impact": "none",
  "approval_status": "approved",
  "notes": "Minor pipeline updating; no heritage or sovereignty impact.",
  "timestamp": "2025-11-13T20:44:00Z"
}
~~~~~

---

## 📡 Telemetry Requirements

Versioning-related telemetry MUST capture:

- version transitions  
- governance decision references  
- lineage linkage  
- checksum stability  
- CARE label consistency  
- energy/CO₂ deltas between versions  

Telemetry appended to:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🚫 Forbidden Versioning Behaviors

- Overwriting artifacts for past versions  
- Changing checksums of past releases  
- Republishing assets with identical version tags but different content  
- Publishing new versions without governance approval for sensitive data  
- Omitting lineage links in STAC Items  

Any violation must be treated as a governance defect.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Added canonical versioning examples for artifacts, STAC Items, schema migrations, and governance approvals. |

---

<div align="center">

**Kansas Frontier Matrix — Versioning Architecture Examples**  
Immutable History × FAIR+CARE Governance × Verifiable Provenance  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Architecture](../README.md)

</div>
