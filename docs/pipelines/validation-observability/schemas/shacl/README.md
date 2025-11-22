---
title: "🧩 KFM Validation & Observability — SHACL Shape Constraint Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/schemas/shacl/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Semi-Annual / FAIR+CARE Council & Knowledge Graph Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/shacl-shapes-index-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Reference"
doc_kind: "SHACL-Index"
intent: "validation-observability-shacl-index"
semantic_document_id: "kfm-validation-observability-shacl-index"
doc_uuid: "urn:kfm:schemas:validation-observability:shacl:index:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧩 **Validation & Observability — SHACL Shape Constraint Index**  
`docs/pipelines/validation-observability/schemas/shacl/README.md`

**Purpose:**  
Provide the **authoritative index** for all **SHACL Shape Constraints** used across the Kansas Frontier Matrix (KFM) v11 to validate graph structure, ontology alignment, provenance correctness, FAIR+CARE compliance, and Story Node v3 integrity.

</div>

---

# 📘 Overview

KFM v11 uses **SHACL (Shapes Constraint Language)** for:

- Knowledge Graph structural validation  
- Enforcing CIDOC-CRM, OWL-Time, GeoSPARQL, PROV-O alignment  
- Story Node v3 schema conformance (graph-level)  
- Narrative grounding constraints (Focus Mode v3)  
- FAIR+CARE + CARE-S compliance at the RDF/graph layer  
- Validating STAC/DCAT → Graph mappings  
- Ensuring reproducibility lineage (PROV-O linkage correctness)  
- Semantic drift and bias-drift prevention at KG boundaries  

This directory hosts **all SHACL shape graphs** responsible for graph-level rule enforcement across:

- ETL pipelines  
- AI-generated content (Story Nodes, Focus Mode v3 narratives)  
- Dataset ingestion  
- Observability dashboards  
- Governance & promotion gates  

All shapes are **CI-enforced**.

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/schemas/shacl/
│
├── README.md                                  # This file — SHACL Index
│
├── shapes/                                    # Official SHACL shapes (Turtle/RDF)
│   ├── storynode-v3.shacl.ttl                 # Story Node v3 structural & semantic constraints
│   ├── provenance.shacl.ttl                   # PROV-O lineage constraints
│   ├── temporal.shacl.ttl                     # OWL-Time interval validity
│   ├── spatial.shacl.ttl                      # GeoSPARQL spatial constraints
│   ├── stac-dcat-mapping.shacl.ttl            # STAC/DCAT → Graph shape alignment
│   ├── faircare.shacl.ttl                     # FAIR + CARE-S governance constraints
│   ├── ai-anomaly.shacl.ttl                   # Shapes for anomaly reports linked to KG entities
│   └── narrative.shacl.ttl                    # Logical/narrative reasoning constraints
│
└── validators/                                # SHACL validation executables
    ├── validate_all_shapes.sh                 # Batch validator
    ├── validate_storynodes.py                 # Story Node v3-specific validator
    ├── validate_graph_structure.py            # General KG structural checker
    └── validate_provenance.py                 # PROV-O checker
```

---

# 🧩 What SHACL Validates in KFM v11

## 1. 🧭 Graph Topology & Class Integrity  
Validates:

- CIDOC-CRM class membership  
- Node typing rules  
- Legal relationship ranges / domains  
- Multi-hop graph consistency  
- No dangling or orphaned entities  

---

## 2. 🕰 Temporal Validity (OWL-Time)  
Includes constraints on:

- Start/end date correctness  
- Valid time intervals (no negative spans)  
- Event ordering alignment  
- Story Node chronology consistency  

---

## 3. 🌍 Spatial Validity (GeoSPARQL)  
Shapes enforce:

- Geometry validity  
- CRS alignment  
- Bounding-box correctness  
- Spatial relationships (`within`, `intersects`, `touches`)  

---

## 4. 🧬 Provenance Completeness (PROV-O)  
Required SHACL constraints ensure:

- Every entity has a generating activity  
- Every activity has an associated agent  
- `prov:used` and `prov:generated` edges follow valid patterns  
- Reproducibility rules match KFM governance requirements  

---

## 5. 🧡 CARE-S Cultural Safety  
Shapes encode **Sovereignty-safe constraints**, preventing:

- Unauthorized cultural inference  
- Tribal identity leaps  
- Misrepresentation of heritage  
- Sensitive site exposure  
- Violations of Indigenous data sovereignty  

All CARE-S violations → governance alerts.

---

## 6. 📚 Story Node v3 Structural Integrity  
Validates:

- Required fields: spacetime, relationships, citations  
- Node-to-entity graph links  
- Narrative alignment with graph ontology  
- JSON-LD → RDF coherence  

---

## 7. 🛰 STAC/DCAT → Graph Mappings  
Ensures:

- Spatial extents map correctly  
- Temporal extents align with OWL-Time  
- License / rights / provenance fields are consistent  
- Assets & metadata generate valid graph structures  

---

# 🛠 Example SHACL Execution Command

```bash
shaclvalidate.sh \
  -datafile graph-export.ttl \
  -shapesfile shapes/storynode-v3.shacl.ttl \
  -reportfile reports/storynode_v3_report.ttl
```

---

# 🔍 CI Integration

CI workflows using these shapes include:

- `kg-shacl-validate.yml`  
- `storynode-v3-integrity.yml`  
- `prov-lineage-audit.yml`  
- `faircare-graph-governance.yml`  

All merges **blocked** if SHACL validation fails.

---

# 🧪 How Contributors Should Use This Directory

- Add new SHACL shapes **only when necessary**  
- Always accompany with a small **example KG snippet** in `schemas/examples`  
- Update this index if adding or reorganizing shapes  
- Ensure shapes are deterministic and version-pinned  
- Use Turtle (`ttl`) format following W3C conventions  

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of SHACL Shape Constraint Index for Validation & Observability v11. |

---

<div align="center">

**Kansas Frontier Matrix — SHACL Shape Constraint Index**  
*Semantic Precision · Graph Safety · Provenance Integrity · CARE-S Sovereignty Governance*

[Back to JSON Schema Index](../json/README.md) ·  
[Back to Schema Examples](../examples/README.md) ·  
[Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>