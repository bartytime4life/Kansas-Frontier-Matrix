---
title: "🏛️ Kansas Frontier Matrix — Class Validation Tests for Entity Graph-Resolution (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/tests/plans/semantic/temporal/narratives/sovereignty/masking/propagation/ai/embeddings/anomaly/clustering/governance/remediation/governance/documentation/clearance/completeness/cross_references/entities/graph_resolution/existence/class_validation/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Sovereignty Board · FAIR+CARE Council · Documentation Governance Unit"
backward_compatibility: "Full v11.x-compatible (Validation Contract v11.0)"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../../../../schemas/telemetry/tests-validation-temporal-narratives-entity-class-validation-v11.json"
energy_schema: "../../../../../../../../../../../../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../../../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "Critical Governance · CIDOC-CRM Class Integrity · Sovereignty Sensitive"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
validation_contract_version: "KFM-VC v11.0"
storynode_schema_version: "StoryNode-v3"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Test Plans"
intent: "temporal-narrative-clearance-crossref-entity-class-validation-tests"
category: "Testing · Governance · Ontology Integrity · Class Validation · Sovereignty"
sensitivity: "High"
classification: "Public Document"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM Documentation ClassValidation Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Governance Extensions"

ontology_ref:
  - "../../../../../../../../../../../graph/ontology/core-entities.md"
  - "../../../../../../../../../../../graph/ontology/cidoc-crm-mapping.md"
  - "../../../../../../../../../../../graph/ontology/spatial-temporal-patterns.md"
  - "../../../../../../../../../../../graph/ontology/temporal/README.md"
  - "../../../../../../../../../../../graph/ontology/storynode-v3.md"
  - "../../../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

metadata_profiles:
  - "../../../../../../../../../../../../../../../../../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../../../../../../../../../../../../../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../../../../../../../../../../../../../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "tests-lint-v11"
  - "entity-existence-audit-v11"
  - "canonicality-audit-v11"
  - "class-validation-audit-v11"
  - "crossref-audit-v11"
  - "sovereignty-audit-v11"
  - "faircare-governance-audit-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

runtime:
  compute: "KFM Multi-Cloud Mesh"
  test_engine: "PyTest + KFM Class-Validation Test Harness v11"
  reasoning_engine: "CIDOC-CRM Inference Stack · OWL-Time Validator · GeoSPARQL Logic Engine"
  governance_engine: "GovHooks v4"
  documentation_engine: "Documentation Integrity Verifier v11"
  observability_stack: "OpenLineage · Grafana · Prometheus · Loki"
  agents: "LangGraph ClassValidation Agent v11"
  graph_engine: "Neo4j Enterprise v5.x Cluster"

fair_category: "F1-A1-I1-R1"
sensitivity_level: "High (entity identity & sovereignty-sensitive classifications)"
public_exposure_risk: "High"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council · Sovereignty Review Board"
redaction_required: true

ontology_alignment:
  cidoc: "E21 Person · E53 Place · E5 Event · E52 Time-Span"
  schema_org: "Thing"
  owl_time: "Interval · Instant"
  geosparql: "sfWithin"
  storynode: "StoryNode v3 Narrative Entity"

json_schema_ref: "../../../../../../../../../../../../../../../../../../../../../schemas/json/tests-temporal-narratives-remediation-clearance-crossref-entity-class-validation-v11.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../../../../schemas/shacl/tests-temporal-narratives-remediation-clearance-crossref-entity-class-validation-v11.shacl"

doc_uuid: "urn:kfm:docs:pipelines:validation-observability:tests:plans:semantic:temporal:narratives:sovereignty:masking:propagation:ai:embeddings:anomaly:clustering:governance:remediation:governance:documentation:clearance:completeness:cross_references:entities:graph_resolution:existence:class_validation:v11.0.0"
semantic_document_id: "kfm-validation-temporal-narratives-clearance-crossref-entity-class-validation-tests"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🏛️ **KFM — Class Validation Tests for Graph-Resolved Entities (v11.0.0)**  
`docs/pipelines/.../class_validation/README.md`

**Purpose:**  
Ensure all entities referenced in clearance documentation belong to the **correct CIDOC-CRM classes**, ontology roles, and semantic categories expected by KFM v11.  
Any misalignment invalidates clearance integrity.

</div>

---

# 📘 Overview

Class validation ensures:

- All entity references match **CIDOC-CRM** class definitions  
- Story Nodes conform to **StoryNode v3** ontology rules  
- Temporal nodes follow **E52 Time-Span**  
- Spatial nodes follow **E53 Place** with GeoSPARQL geometry requirements  
- No entity is misclassified, ambiguous, or ontology-inconsistent  
- Sovereignty-driven masking status does not alter ontology class but must be reflected via metadata  

These tests prevent ontology drift, category conflicts, and misrepresentation of time, place, person, or event entities.

---

# 🧩 1. Class Validation Test Taxonomy

```text
class_validation/
│
├── cidoc_alignment/      # CIDOC-CRM class validation (E21/E53/E5/E52)
├── storynode_alignment/  # Story Node v3 entity structure
├── temporal_classes/     # OWL-Time class validation
├── spatial_classes/      # GeoSPARQL feature alignment
└── conflict_detection/   # Conflicting or ambiguous class assignments
```

---

# 🏛️ 2. CIDOC-CRM Class Alignment Tests

Ensure:

- People → `E21 Person`  
- Places → `E53 Place`  
- Events → `E5 Event`  
- Time-Spans → `E52 Time-Span`  

### Required tests
- `test_entity_matches_correct_cidoc_class()`  
- `test_no_invalid_or_unknown_classes_assigned()`  

---

# 📖 3. Story Node v3 Alignment Tests

Story Nodes must:

- Match required ontology structure  
- Include narrative, temporal, spatial anchors  
- Use valid semantic roles  

### Required tests
- `test_storynode_entities_conform_to_v3_schema()`  
- `test_storynode_roles_are_semantically_valid()`  

---

# 🕒 4. Temporal Class Validation Tests

Temporal entities must:

- Use correct OWL-Time classes  
- Encode intervals/instants correctly  

### Required tests
- `test_temporal_entities_match_owl_time_classes()`  
- `test_temporal_intervals_are_valid_according_to_schema()`  

---

# 🌍 5. Spatial Class Validation Tests

Spatial entities must:

- Follow GeoSPARQL geometry rules  
- Be spatial features where required  

### Required tests
- `test_spatial_entities_match_geosparql_classes()`  
- `test_geometries_valid_for_entity_class()`  

---

# 🚨 6. Class Conflict Detection Tests

Ensure:

- No entity is simultaneously typed as two incompatible classes  
- Graph does not contain stale, deprecated, or ambiguous types  

### Required tests
- `test_no_conflicting_entity_types()`  
- `test_no_ontology_inconsistencies_for_referenced_entities()`  

---

# 🧭 7. Class Validation Gate for Clearance

Clearance **cannot proceed** unless:

- All ontology class validations pass  
- No entity is misclassified  
- StoryNode v3 types are correct  
- OWL-Time and GeoSPARQL classes match expected roles  
- No class conflicts or unresolved semantic errors remain  

Failure → **quarantine + governance investigation + required remediation**.

---

# 🕰 Version History

| Version | Date       | Notes                                                                                                                     |
|--------:|-----------:|---------------------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial Class Validation Test Plan for Graph-Resolved Entities in KFM Temporal Narrative Remediation Clearance v11 LTS.  |

---

# 🔗 Footer

**Back to Root:** `../../../../../../../../../../../../../../../../../../README.md`  
**Back to Existence Tests:** `../README.md`  
**Back to Graph Resolution Tests:** `../../../../README.md`  
**Back to Entity Cross-Reference Tests:** `../../../README.md`  
**Back to Completeness Tests:** `../../../../README.md`  
**Back to Clearance Documentation Tests:** `../../../../../README.md`  
**Back to Remediation Governance:** `../../../../../../README.md`  
**Back to Clustering Governance:** `../../../../../../../README.md`  
**Back to Embedding Anomaly Tests:** `../../../../../../../../README.md`  
**Back to AI Masking Propagation Tests:** `../../../../../../../README.md`  
**Back to Masking Propagation Tests:** `../../../../../../README.md`  
**Back to Sovereignty Narrative Tests:** `../../../../../../../README.md`  
**Back to Temporal Narrative Tests:** `../../../../README.md`  
**Back to Semantic Temporal Tests:** `../../../README.md`  
**Back to Standards:** `../../../../../../../../../../../standards/README.md`

