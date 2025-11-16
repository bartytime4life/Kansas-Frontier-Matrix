```markdown
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

```

web/src/pipelines/geospatial/tests/fixtures/**

````

Integration tests must be deterministic, governance-safe, and operate strictly on **synthetic** geospatial test data.

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/integration/
├── storyPipeline.integration.test.ts        # StoryNode → footprint → map-layer + temporal sync
├── stacPipeline.integration.test.ts         # STAC item extents → footprints → layers
├── focusPipeline.integration.test.ts        # Focus Mode geometry highlight orchestration
├── timelinePipeline.integration.test.ts     # Temporal alignment across Story/Map layers
├── masking.integration.test.ts              # Full H3 sovereignty masking pipeline E2E
├── layerGeneration.integration.test.ts      # Multi-source data → MapView layer synthesis
├── provenance.integration.test.ts           # Provenance consistency across pipeline outputs
└── README.md                                # This document
~~~

> You may rename or reorganize tests depending on your actual pipeline structure.  
> This reflects the **official KFM recommended structure**.

---

# 🧩 Integration Test Scenarios

Integration tests must validate the following:

---

## 🗺️ **1. Story Node → Geospatial Pipeline → Map Layers**
Validates:

- Story Node v3 footprints  
- temporal extents  
- generalization  
- masking  
- provenance stitching  
- MapView layer correctness  

Ensures cross-component consistency between:

- StoryNode → focus pipeline → map pipeline → timeline pipeline

---

## 📦 **2. STAC/DCAT → Footprint Normalization → Map Layers**
Tests:

- STAC item extent extraction  
- multi-item footprint merging  
- H3 masking for sensitive datasets  
- map layer rendering metadata  
- dataset provenance correctness  

---

## 🎯 **3. Focus Mode → Highlight Geometry Rendering**
Tests:

- focus payload geometry  
- highlight conversion  
- masked geometry path  
- provenance thread-through  
- map highlight + timeline highlight sync  

---

## 🕰️ **4. Temporal Alignment (Timeline Pipeline Integration)**
Ensures:

- start/end normalization  
- fuzzy temporal interpretation  
- alignment of Story Node & STAC temporal extents  
- timeline highlight → map highlight → focus narrative triad  

---

## 🛡️ **5. Masking & Sovereignty Enforcement (H3)**
Validates:

- multi-resolution masking  
- nested sovereignty zones  
- masking → layer conversion  
- generalization fallback  
- negative-path behavior (malformed masking geometries)  

---

## 🔗 **6. Provenance Consistency**
Ensures:

- provenance metadata thread-through remains intact  
- provenance chains are correctly associated with geometry + time  
- no provenance loss across transformation layers  

---

## 🔄 **7. Multi-Footprint & Multi-Region Scenarios**
Validates:

- Story Nodes with multiple polygons  
- STAC Items containing multiple geometries  
- geography with discontinuous regions  
- spatial merging, dissolve, and extent union  

---

# 🔐 FAIR+CARE Governance Requirements

Integration tests must confirm that:

- sovereignty masking is ALWAYS applied where required  
- masked geometries never leak precise coordinates  
- Story Nodes with `"care": "restricted"` or `"care": "sovereignty"` behave correctly  
- provenance metadata must remain attached through every pipeline  
- temporal masks must not obscure governance metadata  
- a failure to propagate CARE metadata results in a **test failure**  

Integration tests **must never** include:

- real geographic polygons  
- real tribal boundaries  
- archaeological coordinates  
- cultural heritage extents  
- treaty borders  

All spatial+temporal data must be **synthetic**.

---

# ♿ Accessibility Integration Requirements

Tests should ensure that:

- map layers generated by pipelines maintain A11y-friendly contrast  
- masking layers do not hide focus rings or interactive overlays  
- timeline highlights generated from spatial data remain WCAG AA visible  
- features marked as sensitive generate appropriate accessibility notices  

---

# 🧪 Example Integration Test

```ts
import node from "../fixtures/storynodes/storynode-multi-footprint.json";
import { runStoryPipeline } from "../../../storyPipeline";

describe("Story Pipeline Integration", () => {
  it("produces valid map layers, temporal extents, and provenance", async () => {
    const result = await runStoryPipeline(node);

    expect(result.layers.length).toBeGreaterThan(0);
    expect(result.temporal.start).toBeDefined();
    expect(result.provenance.length).toBeGreaterThan(0);
    expect(result.layers.every(l => l.maskingApplied)).toBe(true);
  });
});
````

---

# 🕰 Version History

| Version | Date       | Summary                                                              |
| ------: | ---------- | -------------------------------------------------------------------- |
| v10.4.0 | 2025-11-15 | Full geospatial integration test suite specification for KFM v10.4.1 |
| v10.3.2 | 2025-11-14 | Added sovereign masking + temporal alignment integration checks      |
| v10.3.1 | 2025-11-13 | Established initial integration test scaffolding                     |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
FAIR+CARE Certified · Synthetic Integration Suite · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
```
