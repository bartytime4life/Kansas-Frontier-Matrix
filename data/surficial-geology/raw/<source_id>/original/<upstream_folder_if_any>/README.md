---
title: "🧱 Surficial Geology — Raw / Original / Upstream Folder"
path: "data/surficial-geology/raw/<source_id>/original/<upstream_folder_if_any>/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / Scaffold"
lifecycle: "Evolving"
review_cycle: "Quarterly · Data Stewardship"
content_stability: "evolving"

status: "Active"
doc_kind: "README"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "data"
  applies_to:
    - "data/surficial-geology/raw/<source_id>/original/<upstream_folder_if_any>/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded when source is retired"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "data/surficial-geology/raw/<source_id>/original/README.md@v0.1.0"
  - "data/surficial-geology/raw/<source_id>/README.md@v0.1.0"
  - "data/surficial-geology/raw/README.md@v0.1.0"

story_node_refs: []
immutability_status: "immutable"

doc_uuid: "urn:kfm:doc:data:surficial-geology:raw:<source_id>:original:<upstream_folder_if_any>:readme:v0.1.0"
semantic_document_id: "surficial-geology-raw-<source_id>-original-<upstream_folder_if_any>-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:raw:<source_id>:original:<upstream_folder_if_any>:readme:v0.1.0"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧱 **Surficial Geology — Raw / Original / Upstream Folder**
`data/surficial-geology/raw/<source_id>/original/<upstream_folder_if_any>/`

**Purpose**  
Preserve the upstream provider’s folder **exactly as received** (after download and any
decompression/extraction) as the **immutable evidence layer** for deterministic ETL, checksums,
and provenance.

</div>

---

## 📘 Overview

This directory holds **verbatim upstream files**. Treat everything under this folder as **read-only**
source evidence.

### What belongs here

- Upstream files in their original formats (e.g., `.zip`, `.tif`, `.gpkg`, `.shp`, `.dbf`, `.prj`, `.csv`,
  `.pdf`, `.xml`, `.txt`, etc.)
- The upstream folder hierarchy (if the provider ships a nested structure)

### What must NOT happen here

- Do **not** edit, “clean”, reproject, simplify, normalize, or otherwise transform files in-place.
- Do **not** rename files to “make them nicer”. Preserve upstream naming.
- Do **not** add derived artifacts (tiles, vectors, intermediate outputs). Put derivatives in:
  - `data/surficial-geology/outputs/**`
  - `data/processed/**` (if certified canonical processed outputs exist)

### How updates are handled

- Upstream updates should be introduced as **new** payloads (new folder, new retrieval, or new
  source version strategy), never by overwriting prior evidence.
- Checksums and lineage must be recorded outside this folder (see “📦 Data & Metadata”).

---

## 🗂️ Directory Layout

~~~text
📁 original/                                           — Verbatim upstream payloads (immutable)
└── 📁 <upstream_folder_if_any>/                        — Upstream folder name (provider-defined)
    ├── 📄 README.md                                    — This file (rules + pointers)
    ├── 📄 <upstream_file_1>                             — Upstream asset (unchanged)
    ├── 📄 <upstream_file_2>                             — Upstream asset (unchanged)
    └── 📁 <subfolders_if_any>/                          — Upstream subfolders (unchanged)
~~~

---

## 📦 Data & Metadata

### Where to record “about” information (do NOT put it in the upstream files)

- License and rights context:
  - `../../license/`
- Provider metadata (landing page snapshots, FGDC/ISO XML, etc.):
  - `../../metadata/`
- Curator notes (interpretation, assumptions, hazards, known issues):
  - `../../notes/`

### Where to record file integrity and lineage

- File manifests and checksums (expected):
  - `../../../../lineage/manifests/`
- Provenance exports (expected):
  - `../../../../lineage/prov/`
- OpenLineage event exports (if used):
  - `../../../../lineage/openlineage/events/`

---

## 🌐 STAC, DCAT & PROV Alignment

- Files in this folder are treated as **PROV Entities** (`prov:Entity`) that ETL activities
  (`prov:Activity`) **use** (`prov:used`) when producing outputs.
- STAC/DCAT metadata should reference these assets via stable repo paths, but publication and
  access are constrained by recorded rights in `../../license/`.
- Never add STAC/DCAT/PROV JSON outputs into this folder; store them in their dedicated
  locations (e.g., STAC under `data/stac/**`, provenance under `data/surficial-geology/lineage/**`).

---

## ⚖ FAIR+CARE & Governance

- Before committing upstream payloads, ensure the license/rights basis is recorded in
  `../../license/` (and keep any required attribution text intact).
- If any content is sensitive or restricted, apply the repository’s classification and handling rules.
  If in doubt, treat as restricted until reviewed by data stewardship.
- Indigenous sovereignty considerations apply by default when there is any potential linkage to
  sensitive locations, culturally sensitive materials, or restricted site knowledge (see policy links in
  footer).

---

## 🕰️ Version History

| Date       | Version  | Change |
|------------|----------|--------|
| 2025-12-14 | v0.1.0   | Initial scaffold README for raw upstream folder preservation rules. |

---

**Governance:** [ROOT-GOVERNANCE](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)  
**FAIR+CARE:** [FAIRCARE-GUIDE](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md)  
**Sovereignty:** [INDIGENOUS-DATA-PROTECTION](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

