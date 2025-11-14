---
title: "🗂️ Kansas Frontier Matrix — STAC/DCAT Alignment Pattern (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/versioning/patterns/stac_dcat_alignment.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/pipelines-versioning-stac-dcat-alignment-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — STAC/DCAT Alignment Pattern**  
`src/pipelines/architecture/versioning/patterns/stac_dcat_alignment.md`

**Purpose:**  
Define the **canonical alignment rules** that ensure STAC 1.0 and DCAT 3.0 metadata remain perfectly synchronized across versions, lineage, governance, and downstream pipelines.  
This alignment pattern guarantees that KFM dataset catalogs remain **FAIR+CARE certified**, **deterministic**, **version-accurate**, and **interoperable across APIs, UI layers, and Focus Mode v2.4**.

<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0-blue"/>
<img alt="DCAT" src="https://img.shields.io/badge/DCAT-3.0-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Required-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Pattern_Active-success"/>

</div>

---

## 📘 Overview

This pattern enforces:

- **1:1 semantic linkage** between STAC Items and DCAT Datasets  
- **Version-consistency** across metadata systems  
- **CARELABEL alignment** (public/sensitive/restricted)  
- **Checksum stability** for artifact integrity  
- **Lineage coherence** (linking STAC → lineage → DCAT)  
- **Governance visibility** across both catalogs  

Both catalogs serve different roles:

- **STAC** → geospatial & temporal discovery  
- **DCAT** → metadata, licensing, provenance, distribution semantics  

They must always describe **the same dataset**, **same version**, **same lineage**, and **same governance status**.

---

## 🗂️ Directory Context

~~~~~text
src/pipelines/architecture/versioning/patterns/
├── README.md
├── artifact_lifecycle.md
├── semver_rules.md
├── stac_dcat_alignment.md          # This file
├── lineage_version_links.md
└── governance_version_contract.md
~~~~~

---

## 🧩 Alignment Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Versioned Artifact<br/>COG · GeoParquet · JSON"] --> B["STAC Item<br/>Spatiotemporal Metadata"]
  A --> C["DCAT Dataset<br/>Semantic Metadata & Licensing"]

  B --> D["Alignment Engine<br/>Version · CARE · Checksums"]
  C --> D

  D --> E["Lineage Bundle<br/>PROV-O · CIDOC CRM"]
  E --> F["Governance Review<br/>CARE · Sovereignty · License"]

  F --> G["Publication<br/>Catalogs · UI · APIs · Focus Mode"]
~~~~~

---

## 🧱 Required Alignment Fields

The following fields MUST match across STAC + DCAT:

| Concept | STAC Field | DCAT Field |
|---------|------------|-------------|
| Version | `properties.version` | `dct:hasVersion` |
| CARE Label | `kfm:care_label` | `kfm:care_label` |
| Checksum | `kfm:checksum` | `dct:identifier` (or checksum extension) |
| Provenance | `kfm:provenance` | `dct:provenance` |
| License | `kfm:license` | `dct:license` |
| Spatial Extent | `geometry` / bbox | `dct:spatial` |
| Temporal Extent | `properties.datetime` | `dct:temporal` |
| Dataset ID | `id` | `dct:identifier` |

All other fields MUST be consistent and non-conflicting.

---

## 📦 STAC Requirements

### STAC Item Naming Pattern

~~~~~text
{dataset_id}_{version}.json
~~~~~

Example:

~~~~~text
historic_floods_ks_v10.3.1.json
~~~~~

### Required STAC Properties

- `properties.version`  
- `properties.kfm:checksum`  
- `properties.kfm:care_label`  
- `properties.kfm:provenance`  
- `links[rel="version"]`  

STAC MUST reflect **exact version path** of artifact and lineage.

---

## 📚 DCAT Requirements

### Required DCAT Fields

- `dct:identifier` (dataset ID)  
- `dct:hasVersion` (SemVer)  
- `dct:provenance` (lineage path)  
- `dct:license` (SPDX)  
- `dct:temporal`  
- `dct:spatial`  
- `dcat:distribution` (versioned asset paths)

DCAT MUST reflect the **same identity** as STAC.

---

## 🔗 Version Chain Alignment Rules

STAC and DCAT must align in:

- Version chain membership  
- Version graph backward links  
- CARE label inheritance  
- Sovereignty metadata propagation  
- Lineage pointer consistency  

Example STAC snippet:

~~~~~json
{
  "id": "historic_floods_ks_v10.3.1",
  "links": [
    { "rel": "version", "href": "historic_floods_ks_v10.3.0.json" }
  ]
}
~~~~~

Matching DCAT snippet:

~~~~~json
{
  "dct:hasVersion": "v10.3.1",
  "dct:isVersionOf": "historic_floods_ks_v10.3.0"
}
~~~~~

---

## ⚖️ CARE & Sovereignty Alignment

CARELABEL must match **exactly**:

- If STAC marks dataset as `sensitive` → DCAT MUST match  
- If STAC includes sovereignty metadata → DCAT MUST include  
- If masking is applied (H3, bbox, fuzzing) → both MUST declare it  

Missing CARE fields → **Critical CI Failure**.

---

## 🧬 Lineage Alignment

Lineage bundle location:

~~~~~text
data/lineage/{dataset_id}/{version}/lineage.json
~~~~~

Both STAC and DCAT MUST reference it.

Mismatch → version is invalid.

---

## 📡 Telemetry Alignment

Every STAC/DCAT pair must produce telemetry containing:

- dataset_id  
- version  
- checksum  
- care_label  
- governance status  
- lineage checksum  
- spatial/temporal alignment indicators  

Telemetry written to:

~~~~~text
../../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🚫 Forbidden Alignment Violations

❌ STAC version ≠ DCAT version  
❌ Missing CARE label in either catalog  
❌ Inconsistent spatial or temporal extents  
❌ Lineage referenced in only one catalog  
❌ STAC asset modified without DCAT update  
❌ Version chain gap (STAC links updated but DCAT not)  
❌ License mismatch between catalogs  

Any violation results in **Critical CI block**.

---

## 🧾 Example — Valid STAC/DCAT Alignment

~~~~~json
{
  "stac": {
    "id": "landcover_ks_v10.3.1",
    "properties": {
      "version": "v10.3.1",
      "kfm:care_label": "public",
      "kfm:checksum": "sha256:ab34...",
      "kfm:provenance": "data/lineage/landcover_ks/v10.3.1/lineage.json"
    }
  },
  "dcat": {
    "dct:identifier": "landcover_ks",
    "dct:hasVersion": "v10.3.1",
    "dct:license": "CC-BY-4.0",
    "dct:provenance": "data/lineage/landcover_ks/v10.3.1/lineage.json"
  }
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Added full STAC/DCAT alignment pattern covering versioning, CARE, lineage, governance, and telemetry. |

---

<div align="center">

**Kansas Frontier Matrix — STAC/DCAT Alignment Pattern**  
Interoperability × Semantic Synchronization × FAIR+CARE Governance  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Versioning Patterns](../README.md)

</div>
