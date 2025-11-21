---
title: "🏷️ Kansas Frontier Matrix — Canonicality Tests for Entity Graph-Resolution (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/tests/plans/semantic/temporal/narratives/sovereignty/masking/propagation/ai/embeddings/anomaly/clustering/governance/remediation/governance/documentation/clearance/completeness/cross_references/entities/graph_resolution/existence/canonicality/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Sovereignty Board · FAIR+CARE Council · Documentation Governance Unit"
backward_compatibility: "Full v11.x-compatible (Validation Contract v11.0)"

commit_sha: "<latest-commit-hash>"
signature_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/signature.sig"
attestation_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/slsa-attestation.json"

sbom_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../../../../../../schemas/telemetry/tests-validation-temporal-narratives-entity-canonicality-v11.json"
energy_schema: "../../../../../../../../../../../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "Critical Governance · Canonical Entity Verification · Sovereignty Sensitive"

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
intent: "temporal-narrative-clearance-crossref-entity-existence-canonicality-tests"
category: "Testing · Governance · Documentation Integrity · Entity Canonicality · Sovereignty"
sensitivity: "High"
classification: "Public Document"
jurisdiction: "Kansas / United States"

prov_profile: "PROV-O Core + KFM Documentation CrossRef Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Governance Extensions"

ontology_ref:
  - "../../../../../../../../../../../graph/ontology/core-entities.md"
  - "../../../../../../../../../../../graph/ontology/cidoc-crm-mapping.md"
  - "../../../../../../../../../../../graph/ontology/spatial-temporal-patterns.md"
  - "../../../../../../../../../../../graph/ontology/temporal/README.md"
  - "../../../../../../../../../../../graph/ontology/storynode-v3.md"
  - "../../../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

metadata_profiles:
  - "../../../../../../../../../../../../../../../../../../../../schemas/stac/kfm-stac-v11.json"
  - "../../../../../../../../../../../../../../../../../../../../schemas/dcat/kfm-dcat-v11.json"
  - "../../../../../../../../../../../../../../../../../../../../schemas/jsonld/kfm-context-v11.json"

validation_profiles:
  - "tests-lint-v11"
  - "entity-existence-audit-v11"
  - "canonicality-audit-v11"
  - "crossref-audit-v11"
  - "sovereignty-audit-v11"
  - "faircare-governance-audit-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

runtime:
  compute: "KFM Multi-Cloud Mesh"
  test_engine: "PyTest + KFM Canonicality Test Harness v11"
  reasoning_engine: "CIDOC-CRM + GeoSPARQL + OWL-Time Resolution Stack"
  governance_engine: "GovHooks v4 + Sovereignty Enforcement Engine v11"
  documentation_engine: "Documentation Integrity Verifier v11"
  observability_stack: "OpenLineage · Grafana · Prometheus · Loki"
  agents: "LangGraph Canonicality Verification Agent v11"
  graph_engine: "Neo4j Enterprise v5.x Cluster"

fair_category: "F1-A1-I1-R1"
sensitivity_level: "High (Sovereignty + Entity Identity Integrity)"
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

json_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/json/tests-temporal-narratives-remediation-clearance-crossref-entity-existence-canonicality-v11.json"
shape_schema_ref: "../../../../../../../../../../../../../../../../../../../../schemas/shacl/tests-temporal-narratives-remediation-clearance-crossref-entity-existence-canonicality-v11.shacl"

doc_uuid: "urn:kfm:docs:pipelines:validation-observability:tests:plans:semantic:temporal:narratives:sovereignty:masking:propagation:ai:embeddings:anomaly:clustering:governance:remediation:governance:documentation:clearance:completeness:cross_references:entities:graph_resolution:existence:canonicality:v11.0.0"
semantic_document_id: "kfm-validation-temporal-narratives-clearance-crossref-entity-existence-canonicality-tests"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 🏷️ **KFM — Canonicality Tests for Graph-Resolved Entities in Clearance Documentation (v11.0.0)**  
`docs/pipelines/.../existence/canonicality/README.md`

**Purpose:**  
Ensure that every entity referenced in clearance documentation is the **canonical**, sovereign-approved, ontology-aligned version in the KFM Neo4j knowledge graph.  
Canonicality failures imply incorrect entity lineage, broken documentation chains, or sovereignty violations.

</div>

---

# 📘 Overview

Canonicality verification ensures:

- Documentation references point to **current, valid, canonical graph entities**  
- Superseded entities are not used unless explicitly referenced with lineage justification  
- Entities derived from sensitive or restricted datasets reflect **sovereignty-mandated masking**  
- No deprecated, archived, or phantom IDs are included in clearance bundles  

It is one of the most essential gates in documentation cross-reference validation.

---

# 🧩 1. Canonicality Test Taxonomy

```text
canonicality/
│
├── active_entity/       # Ensures entity is the current, canonical version
├── supersession/        # Proper superseded ↔ supersededBy lineage
├── sovereignty_status/  # Ensures entity canonicality respects sovereignty rules
├── metadata/            # Canonical metadata required for validated entities
└── versioning/          # Ensures entity version, timestamps, and flags are correct
```

---

# 🏅 2. Active Entity Tests

Determine whether referenced entities:

- Are the **latest active versions**  
- Carry `kfm:canonical=true`  
- Are not deprecated or archived  

### Required tests

- `test_entity_is_active_canonical_version()`  
- `test_no_deprecated_entities_used_in_clearance_docs()`  

---

# 🔄 3. Supersession Lineage Tests

If an entity was superseded:

- Documentation must reference the *correct* canonical successor  
- Lineage must be preserved (`prov:supersededBy`, `prov:wasRevisionOf`)  
- No “zombie” superseded nodes may appear in clearance bundles  

### Required tests

- `test_superseded_entities_link_to_canonical_successor()`  
- `test_clearance_docs_do_not_reference_superseded_nodes()`  

---

# 🛡️ 4. Sovereignty Canonicality Tests

Canonicality must reflect:

- Precision masking (temporal)  
- Spatial generalization (H3 r7+)  
- Sovereignty policies from original datasets  
- CARE obligations for sensitive entities  

### Required tests

- `test_canonical_entity_reflects_sovereignty_masking()`  
- `test_sovereignty_metadata_matches_policies()`  

---

# 📑 5. Metadata Completeness Tests

Canonical entities must include:

- `kfm:id`  
- `kfm:canonical=true`  
- `kfm:source` and data license  
- `prov:wasGeneratedBy` with full lineage  
- StoryNode v3 temporal & spatial bindings (if applicable)

### Required tests

- `test_canonical_entities_have_required_metadata_fields()`  
- `test_entity_version_and_timestamps_present()`  

---

# 🧭 6. Versioning Tests

Version identifiers must:

- Match the canonical entity’s state  
- Be stable and immutable  
- Reflect correct lineage versions  

### Required tests

- `test_entity_version_matches_canonical_state()`  
- `test_version_changes_reflect_lineage_updates()`  

---

# 🚧 7. Canonicality Gate for Clearance

**No clearance may proceed unless:**

- All canonicality tests pass  
- No superseded or ambiguous IDs remain  
- All sovereignty rules are enforced  
- Canonical metadata is complete  
- Documentation references the correct canonical graph node  

Failure → **quarantine**, governance review, and required remediation.

---

# 🕰 Version History

| Version | Date       | Notes                                                                                                                           |
|--------:|-----------:|---------------------------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial Canonicality Test Plan for Entity Existence Validation in KFM Temporal Narrative Remediation Clearance v11 LTS.         |

---

# 🔗 Footer

**Back to Root:** `../../../../../../../../../../../../../../../../../../README.md`  
**Back to Existence Tests:** `../README.md`  
**Back to Graph Resolution Tests:** `../../README.md`  
**Back to Entity Cross-Reference Tests:** `../../../README.md`  
**Back to Completeness Tests:** `../../../../README.md`  
**Back to Clearance Documentation Tests:** `../../../../../README.md`  
**Back to Remediation Governance:** `../../../../../../README.md`  
**Back to Clustering Governance:** `../../../../../../../README.md`  
**Back to Embedding Anomaly Tests:** `../../../../../../../../README.md`  
**Back to AI Masking Propagation Tests:** `../../../../../../../../../README.md`  
**Back to Masking Propagation Tests:** `../../../../../../../../../../README.md`  
**Back to Sovereignty Narrative Tests:** `../../../../../../../../../../../README.md`  
**Back to Temporal Narrative Tests:** `../../../../../../../../../../README.md`  
**Back to Semantic Temporal Tests:** `../../../../../../../../../README.md`  
**Back to Standards:** `../../../../../../../../../../../standards/README.md`
````

