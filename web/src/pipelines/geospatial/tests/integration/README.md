---
title: "🔗 Kansas Frontier Matrix — Geospatial Integration Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/integration/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/geospatial-integration-tests-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Test Suite"
intent: "geospatial-integration-tests"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Low–Medium (all synthetic)"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/pipelines/geospatial/tests/integration/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
  prov_o: "prov:Activity"
json_schema_ref: "../../../../../../../schemas/json/geospatial-integration-tests.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/geospatial-integration-tests-shape.ttl"
doc_uuid: "urn:kfm:doc:geospatial-integration-tests-v10.4.0"
semantic_document_id: "kfm-doc-geospatial-integration-tests"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/integration/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (test logic only)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "coordinate inference"
  - "synthetic geometry enhancement"
machine_extractable: true
accessibility_compliance: "N/A (test content)"
jurisdiction: "United States / Kansas"
classification: "Internal Test Suite"
role: "integration-tests"
lifecycle_stage: "stable"
ttl_policy: "Persistent"
sunset_policy: "Replaced upon geospatial pipeline v11 overhaul"
---

<div align="center">

# 🔗 **Kansas Frontier Matrix — Geospatial Integration Test Suite**  
`web/src/pipelines/geospatial/tests/integration/README.md`

**Purpose:**  
Define the integration-level test architecture for the full geospatial pipeline used in the  
Kansas Frontier Matrix (KFM).  
These tests validate **end-to-end spatial behavior**, ensuring that masking, footprint normalization,  
temporal alignment, provenance propagation, and map-layer generation work correctly together  
— not just in isolation.

</div>

---

# 📘 Overview

Integration tests in this directory verify **multi-step + cross-module** geospatial flows that depend on:

- `footprint.ts`  
- `masking.ts`  
- `bounds.ts`  
- `geometry.ts`  
- `layers.ts`  
- `transforms.ts`  
- STAC/STORY/FOCUS converters  
- Pipeline orchestrators (`storyPipeline`, `stacPipeline`, `timelinePipeline`, `focusPipeline`)  

They confirm the **correct orchestration** of:

- Spatial + temporal normalization  
- Sovereignty masking + H3 workflows  
- Provenance metadata threading  
- Valid MapLibre/Cesium layer definitions  
- Full Story Node → Map → Timeline highlight flows  
- Dataset footprint → map layer → masking interactions  

Fixtures for these tests live in:


