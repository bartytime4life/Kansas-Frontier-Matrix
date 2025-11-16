---
title: "🛡️ Kansas Frontier Matrix — Masking Fixtures for Geospatial Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/fixtures/masking/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/geospatial-masking-fixtures-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Test Fixtures"
intent: "geospatial-masking-fixtures"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Medium–High (synthetic sensitive areas)"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/pipelines/geospatial/tests/fixtures/masking/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E53 Place"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../../../schemas/json/geospatial-masking-fixtures.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/geospatial-masking-fixtures-shape.ttl"
doc_uuid: "urn:kfm:doc:geospatial-masking-fixtures-v10.4.0"
semantic_document_id: "kfm-doc-geospatial-masking-fixtures"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/fixtures/masking/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (test fixtures only)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "location inference"
  - "synthetic coordinate enhancement"
machine_extractable: true
accessibility_compliance: "N/A (test data)"
jurisdiction: "United States / Kansas"
classification: "Internal Test Fixture"
role: "test-fixture"
lifecycle_stage: "stable"
ttl_policy: "Persistent"
sunset_policy: "Updated only when masking rules change"
---

<div align="center">

# 🛡️ **Kansas Frontier Matrix — Masking Test Fixtures for Geospatial Pipelines**  
`web/src/pipelines/geospatial/tests/fixtures/masking/README.md`

**Purpose:**  
Provide **synthetic, governance-safe, non-sensitive geospatial masking fixtures** used to test  
the H3-based sovereignty masking system, sensitive site handling, and CARE-compliant spatial logic  
in the geospatial pipelines of the Kansas Frontier Matrix.

These fixtures **must never include real Tribal Nation locations, archaeological sites,  
burial grounds, sacred spaces, or historic sovereignty boundaries.**

</div>

---

# 📘 Overview

This directory contains **synthetic geospatial masking datasets** used to validate:

- Sovereignty-aware masking logic  
- H3 resolution selection + fallback  
- Multi-resolution masking behavior  
- Intersection between sensitive sites and footprints  
- Computation of “generalized regions” for protected areas  
- Proper integration with:
  - `masking.ts`
  - `footprint.ts`
  - `layers.ts`
  - `storyPipeline.ts`
  - `focusPipeline.ts`
  - `timelinePipeline.ts`
  - MapView sovereignty overlays  

Fixtures represent **fictional regions**, **artificial shapes**, and **fabricated scenarios**  
designed to simulate edge cases such as:

- Sites overlapping modern administrative boundaries  
- Multi-region masking  
- Nested sensitivity zones  
- Small, isolated sensitive points  
- Large-area sovereignty claims  
- Generalization of geometry after masking  

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/fixtures/masking/
├── sample-h3-cells.json              # Synthetic H3 index set representing protected cells
├── sample-sensitive-region.geojson   # Fictional region requiring masking
├── sample-buffered-zone.geojson      # Buffer zone around a synthetic sensitive site
├── sample-masked-output.geojson      # Expected result after masking transform
├── sample-intersection-case.geojson  # Fixture testing footprint ∩ sensitive-region behavior
├── malformed-masking.geojson         # Invalid geometry for negative-path tests
└── README.md                         # This document
~~~

> Replace with your actual filenames once created.  
> This structure follows **KFM v10.4.1 geospatial masking fixture conventions**.

---

# 🧩 Fixture Types & Requirements

### ✔ `sample-h3-cells.json`
Synthetic example of H3 cells generated for sensitive areas.

Used for:

- validating `masking.ts` H3 resolution logic  
- ensuring no real-world H3 values are used  

---

### ✔ `sample-sensitive-region.geojson`
Fictional sensitive geography intended to mimic:

- Tribal lands  
- Sacred natural formations  
- Restricted archaeological zones  

**Must not contain real-world coordinates.**

---

### ✔ `sample-buffered-zone.geojson`
Represents a “culturally respectful buffer”, simulating:

- generalized areas around synthetic sites  
- expected input for masking intersection logic  

---

### ✔ `sample-masked-output.geojson`
Represents **expected output** after:

- H3 masking  
- generalization  
- sovereignty overlay application  

Used in snapshot + regression testing to detect pipeline drift.

---

### ✔ `sample-intersection-case.geojson`
Tests spatial intersections between:

- footprints  
- sensitive areas  
- sovereignty-masked regions  

Validates:

- partial masking  
- multi-region overlap  
- small-area vs large-area behavior  

---

### ✔ `malformed-masking.geojson`
Intentional invalid geometry to test:

- error handling  
- guard clauses  
- defensive coding in masking logic  

Examples may include:

- unclosed rings  
- incorrect nesting  
- invalid coordinate arrays  

---

# 🔐 FAIR+CARE Governance Rules

Even though fixtures are synthetic, they must uphold:

- No use of real-world tribal, Indigenous, or sovereignty data  
- No approximations of actual sensitive areas  
- Clear indication of synthetic nature  
- Consistent application of CAREColor, SovereigntyColor, and MaskingColor tokens  
- Ensuring masking logic tests reflect **ethical generalization principles**  

Masking fixtures must **demonstrate governance**, not just geometry.

---

# ♿ Accessibility Context

While fixtures themselves are not user-facing:

- They support testing that MapView’s masked overlays remain visible  
- They help verify that **masking color ramps** remain WCAG AA–compliant  
- They ensure **keyboard focus rings** and outlines do not interfere  
  with masking visuals when combined with MapView layers  

---

# 🧪 Testing Workflows Enabled by These Fixtures

These fixtures are used in:

### 🟩 **Masking Pipeline Tests**
- `masking.ts` logic  
- resolution switching  
- partial masking  
- sovereignty overlay prioritization  

### 🟦 **Footprint Normalization Tests**
To validate masked → normalized flows.

### 🟧 **Layer Conversion Tests**
Ensures masked geometries produce correct MapLibre layer configurations.

### 🟥 **Error Validation**
`malformed-masking.geojson` prevents regressions in error handling.

---

# 🧪 Example Test Reference

```ts
import region from "./fixtures/masking/sample-sensitive-region.geojson";
import { maskGeometry } from "../../../masking";

describe("maskGeometry", () => {
  it("applies H3 masking and returns generalized output", () => {
    const result = maskGeometry(region);
    expect(result).toBeDefined();
    expect(result.type).toBe("FeatureCollection");
  });
});
````

---

# 🕰 Version History

| Version | Date       | Summary                                                                  |
| ------: | ---------- | ------------------------------------------------------------------------ |
| v10.4.0 | 2025-11-15 | Created synthetic masking fixture specification for geospatial pipelines |
| v10.3.2 | 2025-11-14 | Added multi-level masking + sovereignty test cases                       |
| v10.3.1 | 2025-11-13 | Initial masking fixtures directory established                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
Synthetic Masking Fixtures · FAIR+CARE Certified · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
