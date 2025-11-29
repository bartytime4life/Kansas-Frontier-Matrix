---
title: "🔗 NASA SMAP — Provenance Builder (PROV-O Lineage Construction) · ETL Stage 7"
path: "docs/data/satellites/smap/transforms/provenance/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Provenance Board · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public ETL Documentation"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2 (Extended)"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-PROVJSONLD v11"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R5"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Medium"
redaction_required: false

data_steward: "KFM Provenance Board · FAIR+CARE Council · Earth Systems Working Group"

ontology_alignment:
  cidoc: "E7 Activity"
  prov_o: "prov:Activity"
  schema_org: "Dataset"
  geo: "FeatureCollection"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../schemas/json/transform-smap-provenance-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/transform-smap-provenance-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:provenance-readme:v11.2.2"
semantic_document_id: "kfm-doc-smap-provenance-layer"
event_source_id: "ledger:docs/data/satellites/smap/transforms/provenance/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next PROV-O profile update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **NASA SMAP — Provenance Builder (ETL Stage 7)**  
`docs/data/satellites/smap/transforms/provenance/README.md`

**Purpose**  
Construct complete, machine-verifiable **PROV-O lineage graphs** for every SMAP-derived  
dataset in KFM.  
This stage encodes *what data was used*, *what transformations occurred*,  
*who/what performed them*, and *what governance rules were enforced*, producing  
PROV-O JSON-LD used by STAC Writer, Story Node v3, and Focus Mode v3.

</div>

---

## 📘 1. Overview

The **Provenance Builder** is ETL **Stage 7**, executed after:

```
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → provenance building  (this stage)
 → STAC Writer (final stage)
```

Its responsibilities:

- 🔗 Build **PROV-O Activity graphs** for each ETL step  
- 🧩 Encode **Entities** (raster assets, masks, QA, uncertainty, metadata)  
- 🚦 Encode **Activities** (decode, reprojection, calibration, QA integration, uncertainty, governance)  
- 👤 Encode **Agents** (pipelines, tools, governance boards, AI components)  
- 🛡 Apply FAIR+CARE & sovereignty provenance descriptors  
- 📄 Produce **JSON-LD** ready for STAC items  
- 📑 Maintain cross-stage dependency chains  
- 🧾 Write lineage to `prov:wasDerivedFrom`, `prov:used`, `prov:generatedAtTime`, etc.  
- 📤 Export final provenance documents into STAC items via STAC Writer  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/provenance/
├── 📄 README.md                           # This file
│
├── 🔗 build_provenance.py                 # Core PROV-O builder engine
├── 🧩 prov_skeleton.jsonld                # Base JSON-LD provenance template
├── 🧾 agent_registry.json                 # Registered Agents (pipelines, orgs, tools)
├── 🗃️ entity_types.json                   # Entity categories (rasters, masks, metadata, etc.)
├── 🎛 activity_map.json                   # Ordered ETL activity definitions
│
├── 🧪 tests/
│   ├── test_prov_entities.py
│   ├── test_prov_activities.py
│   ├── test_prov_agents.py
│   ├── test_prov_lineage_chain.py
│   ├── test_jsonld_validity.py
│   └── fixtures/
│       ├── sample_etl_inputs.json
│       ├── sample_prov_expected.json
│       ├── synthetic_agent_defs.json
│       ├── synthetic_entity_defs.json
│       └── schema_expected.json
~~~

---

## 🧩 3. Provenance Model (KFM-PROV-O v11.2)

### ✔ Entities (`prov:Entity`)
Represent:
- decode outputs  
- reprojected rasters  
- calibrated rasters  
- QA masks  
- uncertainty grids  
- governance masks  
- metadata & STAC components  

### ✔ Activities (`prov:Activity`)
Represent:
- decode  
- reprojection  
- calibration  
- QA/RFI integration  
- uncertainty propagation  
- governance masking  
- STAC writing  

### ✔ Agents (`prov:Agent`)
Represent:
- KFM pipelines  
- FAIR+CARE Council  
- Sovereignty Working Group  
- STAC Review Board  
- NASA algorithm teams  
- Automated jobs (CI)  
 
### ✔ Relationships
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasDerivedFrom`  
- `prov:wasAttributedTo`  
- `prov:wasAssociatedWith`  
- `prov:actedOnBehalfOf`  

This produces a **complete lineage chain**, finalizing data trustability.

---

## 🧠 4. Responsibilities of This Stage

### 🔗 Build Full ETL Lineage Graphs
Output includes:

- Each ETL stage as an Activity  
- Each intermediate raster as an Entity  
- Each process and governance review board as an Agent  

### 🧭 FAIR+CARE & Sovereignty Provenance
The builder MUST document:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:care_label_reason"`  
- `"kfm:governance_notes"`  

### 📑 JSON-LD & STAC Integration
Builds JSON-LD structured provenance for STAC Items under:

```
assets.<x>.kfm:provenance
item.properties.provenance
```

### 📤 Exports Provenance Docs
Into:

```
data/releases/<version>/provenance/
data/satellites/smap/stac/*/provenance/*.jsonld
```

---

## 🔐 5. Governance, FAIR+CARE, and Sovereignty Integration

Provenance MUST:

- document all sovereignty-driven decisions  
- include evidence for masking/generalization steps  
- document uncertainty-floor reasoning  
- record CARE label origins  
- ensure transparency for communities impacted by the data  
- preserve lineage through all transforms  

CI ensures:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`  

Any missing governance field = **pipeline block**.

---

## 🧪 6. QA & Validation Requirements

Tests verify:

- Valid JSON-LD  
- Valid PROV-O  
- Complete entity/activity/agent sets  
- Matching lineage chains across ETL steps  
- No missing governance fields  
- Stability + determinism  
- Correct STAC integration  
- No circular lineage  
- No invented metadata  

Fixtures ensure CI stability.

---

## 🔁 7. Provenance in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking
 → provenance building (THIS STAGE)
 → STAC Writer (final public output)
~~~

Without provenance, **no STAC Item may be emitted**.

---

## 🔮 8. Applications Inside KFM

### Hydrology  
Source-aware soil-moisture pipelines.

### Climate  
Traceable FT/VWC anomaly production.

### Archaeology  
Transparent environmental evidence for cultural narratives.

### Story Node v3  
Environmental narratives cite precise ETL lineage.

### Focus Mode v3  
Lineage curves power “Why am I seeing this?” explainability.

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First full provenance-layer README; emoji-rich; PROV-O v11.2; sovereignty/CARE compliant; CI-safe.    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🔗 Provenance Tests](../README.md) · [🛡 Governance Standards](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

