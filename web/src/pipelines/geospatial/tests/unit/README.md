---
title: "🧪 Kansas Frontier Matrix — Geospatial Unit Test Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/unit/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/geospatial-unit-tests-v1.json"
governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Test Suite"
intent: "geospatial-unit-tests"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Low–Medium (synthetic test data)"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/pipelines/geospatial/tests/unit/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Activity"
json_schema_ref: "../../../../../../../schemas/json/geospatial-unit-tests.schema.json"
shape_schema_ref: "../../../../../../../schemas/shacl/geospatial-unit-tests-shape.ttl"
doc_uuid: "urn:kfm:doc:geospatial-unit-tests-v10.4.0"
semantic_document_id: "kfm-doc-geospatial-unit-tests"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/unit/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (test code only)"
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
role: "unit-tests"
lifecycle_stage: "stable"
ttl_policy: "Persistent"
sunset_policy: "Replaced when geospatial pipeline v11 lands"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Geospatial Unit Test Suite**  
`web/src/pipelines/geospatial/tests/unit/README.md`

**Purpose:**  
Define the **unit-level test architecture** for the geospatial pipeline within the Kansas Frontier Matrix (KFM).  
Unit tests validate small, isolated, deterministic geospatial functions — guaranteeing correctness, safety,  
and FAIR+CARE compliance before integration with MapView, Focus Mode, Story Nodes, and STAC/DCAT pipelines.

</div>

---

# 📘 Overview

This directory contains **low-level unit tests** covering all internal geospatial functions such as:

- GeoJSON geometry normalization  
- H3 masking + sovereignty handling  
- Footprint extraction + validity tests  
- Bounding box calculations  
- Coordinate sanitization  
- CRS assumptions (EPSG:4326)  
- Layer conversion helpers  
- Geometry repair logic  
- Fuzzy temporal + spatial alignment when applicable  

Each test ensures functions behave correctly in isolation, with **fixtures** provided under:

```

web/src/pipelines/geospatial/tests/fixtures/**

````

These tests are deliberately **small, fast, deterministic, and dependency-free**  
(other than JSON fixtures).

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/unit/
├── masking.test.ts              # H3 masking logic, sovereignty rules, generalization
├── footprint.test.ts            # Footprint normalization & geometry flattening
├── geometry.test.ts             # GeoJSON normalization, repair, invalid cases
├── bounds.test.ts               # Bounding-box & extent calculation tests
├── transforms.test.ts           # Shared spatial transforms (simplify, centroid, dissolve)
├── layers.test.ts               # Footprint → MapView layer conversion integrity
├── temporalAlignment.test.ts    # Combined temporal + spatial normalization
└── README.md                    # This document
~~~

> Note: file names reflect recommended test suite structure.  
> Update to match your actual implementation as tests are added.

---

# 🧩 Unit Test Responsibilities

---

## 🛡️ **`masking.test.ts`**
Validates:

- H3 resolution switching  
- Partial masking  
- Nested sovereignty regions  
- Masked vs. unmasked region behavior  
- Masking error cases (e.g., malformed inputs)  

Ensures:

- No sensitive geometry is rendered  
- Masking aligns with CARE + sovereignty metadata  

---

## 🗺️ **`footprint.test.ts`**
Validates:

- Polygon → normalized footprint  
- MultiPolygon flattening  
- Geometry validation  
- CRS normalization (assume EPSG:4326)  
- Centerpoint extraction  

Ensures:

- Deterministic footprint results  
- No speculative geometry  

---

## 📐 **`geometry.test.ts`**
Covers:

- geometry normalization  
- ring repair  
- invalid coordinate arrays  
- FeatureCollection handling  
- error-path coverage  

Ensures:

- frontend never accepts malformed geometry  

---

## 📦 **`bounds.test.ts`**
Tests:

- bounding box generation  
- min/max value correctness  
- multi-geometry extent merging  
- degenerate cases (zero-area)  

---

## 🔄 **`transforms.test.ts`**
Validates spatial transforms, including:

- centroid  
- simplify  
- dissolve  
- intersect  
- difference  

Ensures:

- deterministic, safe transforms  
- no over-simplification that invalidates geometry  

---

## 🎨 **`layers.test.ts`**
Tests the layer conversion pipeline:

- footprint → MapView polygon layers  
- mask → masking overlays  
- CARE overlays  
- sovereignty overlays  
- rendering-safe metadata  

Ensures:

- all layers use design tokens + theme variables indirectly  
- no disallowed colors or styles leak into MapView  

---

## 🕰️ **`temporalAlignment.test.ts`**
Tests combination of:

- spatial footprint  
- temporal extent  
- fuzzy time  
- open intervals  

Used in timeline + story + map sync logic.

---

# 🔐 FAIR+CARE Governance Rules

Unit tests must validate:

- geometry masking for synthetic sensitive regions  
- sovereignty-aware generalization  
- strict avoidance of precise coordinates in synthetic fixtures  
- deterministic outputs for all transforms  
- that governance-related components receive correct derived metadata  

Unit tests **must never**:

- contain real geography  
- embed real sovereign boundaries  
- replicate real archaeological/cultural footprints  

All sensitive cases must be **synthetic**.

---

# 🧪 Example Unit Test

```ts
import sample from "../fixtures/geometry/polygon-simple.geojson";
import { normalizeGeometry } from "../../../geometry";

describe("normalizeGeometry", () => {
  it("returns valid GeoJSON geometry", () => {
    const out = normalizeGeometry(sample);
    expect(out.type === "Polygon" || out.type === "MultiPolygon").toBe(true);
  });
});
````

---

# 🕰 Version History

| Version | Date       | Summary                                                        |
| ------: | ---------- | -------------------------------------------------------------- |
| v10.4.0 | 2025-11-15 | Complete unit test suite specification for geospatial pipeline |
| v10.3.2 | 2025-11-14 | Added transforms, bounds, and sovereignty masking test cases   |
| v10.3.1 | 2025-11-13 | Initial geospatial unit test scaffold                          |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
Synthetic Test Suite · FAIR+CARE Certified · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
