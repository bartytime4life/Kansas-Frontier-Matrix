---
title: "🔗📐 Kansas Frontier Matrix — Lineage Observability Dashboard Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/lineage/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable · Reference"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Lineage Governance Board · FAIR+CARE Council · Sovereignty Review Panel"
backward_compatibility: "Full v11.x-compatible"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/dashboards-schemas-lineage-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High — Provenance, Promotion, Sovereignty-Sensitive"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active · Reference"
doc_kind: "Schemas · Lineage Observability"
intent: "dashboard-schema-lineage"
category: "Lineage · PROV-O · OpenLineage · Governance"
sensitivity: "High"
classification: "Public Examples (Governance-Safe)"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM Lineage Schema Extensions"
openlineage_profile: "Supported for read-only event alignment"

metadata_profiles:
  - "../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "lineage-schema-check-v11"
  - "faircare-schema-audit-v11"
  - "sovereignty-schema-audit-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

runtime:
  compute: "Client-Side Schema Validation & Dashboard Rendering"
  dashboard_engine: "Grafana · KFM Observability Lineage Layer"
  agents: "N/A"

fair_category: "F1-A1-I1-R1"
indigenous_rights_flag: true
redaction_required: true

ontology_alignment:
  cidoc: "E7 Activity · E5 Event · E73 Information Object"
  schema_org: "Dataset"
  owl_time: "ProperInterval"
  geosparql: "N/A"

json_schema_ref: "../../../../../schemas/json/dashboards-schemas-lineage-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/dashboards-schemas-lineage-v11.shacl"

doc_uuid: "urn:kfm:docs:pipelines:validation-observability:dashboards:schemas:lineage:v11.0.0"
semantic_document_id: "kfm-dashboard-schemas-lineage"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🔗📐 **Lineage Observability Dashboard Schema Library (v11.0.0)**  
`docs/pipelines/validation-observability/dashboards/schemas/lineage/README.md`

**Purpose:**  
Define the authoritative v11 schema specifications for **lineage-focused observability dashboards**, covering PROV-O, OpenLineage, masking/redaction lineage, AI lineage, temporal/spatial lineage, and promotion-gate lineage requirements.

These schemas enforce **provenance correctness**, sovereign protection, FAIR+CARE compliance, and promotion-gate lineage integrity.

</div>

---

# 📘 Overview

Lineage schemas ensure all dashboards that display provenance:

- Use strict PROV-O structures (`prov:Entity`, `prov:Activity`, `prov:Agent`)  
- Integrate OpenLineage event structures (runs, tasks, linkages)  
- Enforce masking/redaction lineage correctness  
- Enforce temporal (OWL-Time) lineage and precision reduction  
- Validate spatial lineage (H3-masked GeoSPARQL relationships)  
- Capture AI inference lineage (model → config → seed → inference path)  
- Ensure complete lineage closure before dataset promotion  
- Provide governance-usable audit surfaces  
- Block promotion when lineage is incomplete, contradictory, or unsafe  

These schemas define the **CI/CD guards** for lineage dashboards.

---

# 🗂 Directory Layout

```text
lineage/
│
├── prov_o/                  # PROV-O structured lineage schemas
├── openlineage/             # OpenLineage run/task/event schemas
├── masking/                 # Masking lineage schema (spatial/temporal/cultural)
├── redaction/               # Redaction lineage schema (suppression provenance)
├── ai/                      # AI inference lineage schemas
├── temporal/                # OWL-Time lineage alignment schemas
├── spatial/                 # H3-masked spatial lineage schemas
└── promotion/               # Promotion-gate lineage validation schemas
```

---

# 📑 Mandatory Schema Components (v11)

### **1. Lineage Metadata Block**
Each schema MUST define:

- `lineage_schema_version`  
- `requires_provenance: true`  
- `sovereignty_protection` (H3/temporal/CARE rules)  
- `masking_obligations`  
- `redaction_obligations`  
- `promotion_blocking_conditions`  

### **2. PROV-O Structural Contract**
All lineage dashboards must reflect:

- `prov:Entity` objects with identifiers + metadata  
- `prov:Activity` transformations with timestamps (coarsened if needed)  
- `prov:Agent` attributions (human or autonomous pipeline agents)  
- Derivation, generation, usage, invalidation relations  
- CARE + sovereignty lineage expansion  

### **3. OpenLineage Compatibility**
Where applicable:

- `run`, `job`, `facet`, `eventTime`, `parentRunId`  
- I/O dataset lineage (input/output facets)  
- Sovereignty-masked outputs  
- Temporal-spatial lineage merging  

### **4. Masking & Redaction Blocks**
Schemas MUST include obligations for:

- H3 r7+ spatial generalization  
- Temporal precision reduction  
- Cultural-site redaction lineage  
- Narrative suppression lineage  
- AI inference masking alignment  

### **5. Lineage Closure Requirements**
Schemas define:

- Lineage completeness conditions  
- Dangling-node detection  
- Derivation-chain closure expectations  
- Promotion gating logic  

### **6. Accessibility & Governance Requirements**
Schemas must enforce:

- WCAG 2.1 AA compliance  
- FAIR+CARE labeling  
- Sovereignty-policy tagging  
- Explainability attachments for governance panels  

---

# 🧪 Example Schema Snippet

```json
{
  "lineage_schema_version": "1.0.0",
  "requires_provenance": true,
  "prov": {
    "entities_required": true,
    "activities_required": true,
    "agents_required": true
  },
  "masking": {
    "requires_h3": true,
    "temporal_coarsening": "decade",
    "cultural_redaction_required": true
  },
  "promotion": {
    "block_if_lineage_incomplete": true,
    "requires_governance_signoff": true
  }
}
```

---

# 🎨 Schema Design Requirements (v11)

All lineage observability schemas MUST:

- Use strict JSON Schema + SHACL validation  
- Enforce masking and redaction lineage correctness  
- Integrate FAIR+CARE + sovereignty constraints  
- Forbid unmasked sensitive spatial/temporal details  
- Include provenance-linked UI semantics  
- Conform to the KFM Observability Style Guide v11  
- Block promotion if lineage is incomplete or unsafe  
- Integrate AI lineage & narrative lineage where applicable  
- Pass `lineage-schema-check-v11` in CI  

---

# 🕰 Version History

| Version | Date       | Notes                                                         |
|--------:|-----------:|---------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial Lineage Observability Dashboard Schema Library (v11). |

---

# 🔗 Footer

**Back to Root:** `../../../../../README.md`  
**Back to Dashboard Schemas:** `../README.md`  
**Back to Dashboard Examples:** `../../examples/README.md`  
**Back to Validation & Observability:** `../../../README.md`  
**Back to Standards:** `../../../../standards/README.md`
