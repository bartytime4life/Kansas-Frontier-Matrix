---
title: "📐 Kansas Frontier Matrix — Heritage Standards Schemas Index (v11)"
path: "docs/standards/heritage/schemas/README.md"
version: "v11.0.0"
last_updated: "2025-11-20"
review_cycle: "Annual / FAIR+CARE Council & Focus Mode Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/standards-heritage-schemas-v11.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "heritage-schemas-index"
semantic_document_id: "kfm-heritage-schemas-index-v11"
doc_uuid: "urn:kfm:docs:standards:heritage:schemas:index:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Protected / High-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Heritage Standards Schemas Index (v11)**  
`docs/standards/heritage/schemas/README.md`

**Purpose:**  
Serve as the **authoritative, enforceable v11 index** for all JSON Schemas governing cultural-heritage, archaeological, Indigenous, and sensitive-location data within the Kansas Frontier Matrix (KFM).  
Schemas under this directory define **ethical**, **legal**, **FAIR+CARE**, **PROV-O**, **H3-generalization**, and **Diamond⁹ Ω confidentiality** requirements for heritage-sector pipelines.

<img alt="FAIR+CARE Badge" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold" />
<img alt="Heritage Standards Badge" src="https://img.shields.io/badge/Heritage_Standards-Schemas-blue" />
<img alt="Protection Level III" src="https://img.shields.io/badge/Protection_Level-III-red" />

</div>

---

# 📘 Overview

This directory contains the **v11-governed schema definitions** that regulate how heritage-related data is:

- ingested into the ETL pipelines  
- normalized and generalized (H3, masking, obfuscation)  
- validated pre-Neo4j and pre-PGV  
- exported as STAC/DCAT-compliant datasets  
- protected according to **FAIR+CARE** and **NHPA §304**  
- rendered safely in MapLibre + Cesium + Focus Mode v3  
- linked to provenance pathways (PROV-O) and Story Node v3 entities  

**Every heritage dataset MUST validate against these schemas before entering the KFM knowledge graph.**

Schemas enforce:

- Mandatory metadata blocks (FAIR+CARE, lineage, sovereignty, sensitivity)  
- Spatial confidentiality (no raw coordinates; H3-only for protected sites)  
- Indigenous governance fields (CARE sovereignty controls, custodial rights)  
- Dataset invariants, identity, and temporal coverage  
- Provenance lineage logs for reproducible science  
- Story Node & Focus Mode compatibility rules  

---

# 🗂 Directory Layout

```text
schemas/
│
├── README.md                                   # This index file (v11)
│
├── h3-generalization-standard.json              # Spatial masking + resolution constraints
├── heritage-sensitive-location.schema.json      # Metadata schema for protected cultural sites
├── heritage-dataset.schema.json                 # STAC/DCAT/FAIR+CARE-compliant dataset schema
├── heritage-protection-flags.schema.json        # Protection tiers, sensitivity flags, restrictions
├── lineage-provenance.schema.json               # Required lineage, reproducibility, PROV-O links
│
└── examples/                                    # Example valid JSON instances for CI tests
```

---

# 🧱 Schema Descriptions

## 🧩 `h3-generalization-standard.json`

Defines v11-certified spatial masking rules:

- Allowed H3 resolutions for protection tiers  
- Required removal of raw lat/lon  
- Minimum aggregation thresholds  
- NHPA §304 confidentiality flags  
- CARE sovereignty override controls  
- Required PROV-O lineage for any generalization process  

## 🏺 `heritage-sensitive-location.schema.json`

Defines metadata for **protected cultural sites**, including:

- Indigenous/tribal sovereignty fields  
- CARE labels (public / restricted / sacred / private / ancestral)  
- Sensitivity scoring with mandatory protection tier  
- **Explicit prohibition of coordinate export**  
- Required Story Node v3 link fields  
- Required OWL-Time temporal anchors (if known)  

## 📦 `heritage-dataset.schema.json`

STAC/DCAT-aligned dataset-level schema enforcing:

- STAC Item/Collection correctness  
- Required dataset identity, license, spatial/temporal extents  
- FAIR+CARE metadata and governance  
- H3 generalization obligations  
- Dataset lineage (PROV-O `wasDerivedFrom`, `generatedBy`)  
- Machine-extractable Story Node links  

## 🔐 `heritage-protection-flags.schema.json`

Defines protection and confidentiality semantics:

- Protection tiers I–III (automatically enforced by KFM pipelines)  
- Sensitivity flags  
- Export/display/indexing restrictions  
- Masking rules for Focus Mode v3  
- CARE ethics alignment fields  

## 🧬 `lineage-provenance.schema.json`

Governs mandatory provenance and reproducibility metadata:

- Required PROV-O relations  
- “Who/when/what” action logs  
- Activity chains (import → normalize → generalize → publish)  
- SHA-256 diff manifests  
- Multi-version reproducibility guarantees  

---

# 🧪 Validation Rules

All heritage-sector data MUST:

- Validate cleanly against all relevant schemas (CI-enforced)  
- Pass FAIR+CARE ethical validation  
- Include `mcp_protected: true` for sensitive contexts  
- Strip raw coordinates where required  
- Provide H3 generalization metadata (resolution + justification)  
- Include dataset lineage, SHA-256 integrity, and PROV-O activity logs  
- Provide Access + CARE sovereignty fields before publication  
- Validate through Story Node v3 + Focus Mode v3 compatibility tests  

Local validator:

```bash
make validate-heritage-schemas
```

---

# 🛠 Focus Mode v3 Integration

All schemas here supply the metadata required for:

- Focus Mode narrative filtering  
- Confidentiality-aware summarization  
- Story Node linkage  
- Data exclusions for inappropriate contexts  
- Multi-hop graph safety for cultural entities  

No heritage data may enter Focus Mode unless validated through this index.

---

# 🕰 Version History

| Version | Date       | Author          | Notes                                                         |
|--------|------------|-----------------|---------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | KFM Docs AI     | Full upgrade to KFM-MDP v11.0.0; STAC/DCAT/PROV-O aligned.    |
| v10.2.3 | 2025-11-13 | KFM Docs AI     | Initial v10 heritage schemas index.                           |

---

# 🔗 Footer

Return to **Heritage Standards**:  
`docs/standards/heritage/README.md`

Return to **KFM Standards Root**:  
`docs/standards/README.md`

Return to **Repository Root**:  
`README.md`
