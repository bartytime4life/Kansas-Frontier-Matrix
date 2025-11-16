---
title: "📐 Kansas Frontier Matrix — Geometry Fixtures for Geospatial Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/fixtures/geometry/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/geospatial-geometry-fixtures-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Test Fixtures"
intent: "geospatial-geometry-fixtures"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Low–Medium (synthetic data only)"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/pipelines/geospatial/tests/fixtures/geometry/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E53 Place"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../../../schemas/json/geospatial-geometry-fixtures.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/geospatial-geometry-fixtures-shape.ttl"
doc_uuid: "urn:kfm:doc:geospatial-geometry-fixtures-v10.4.0"
semantic_document_id: "kfm-doc-geospatial-geometry-fixtures"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/fixtures/geometry/README.md"
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
  - "coordinate inference"
  - "synthetic precision enhancement"
machine_extractable: true
accessibility_compliance: "N/A (test data)"
jurisdiction: "United States / Kansas"
classification: "Internal Test Fixture"
role: "test-fixture"
lifecycle_stage: "stable"
ttl_policy: "Persistent"
sunset_policy: "Updated only when geometry schema changes"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Geometry Test Fixtures for Geospatial Pipelines**  
`web/src/pipelines/geospatial/tests/fixtures/geometry/README.md`

**Purpose:**  
Provide **synthetic, deterministic, governance-safe geometry fixtures** used to test all  
low-level geometry handling across the KFM geospatial pipeline, including:

- GeoJSON validity testing  
- Geometry repair logic  
- Polygon/MultiPolygon flattening  
- Geometry simplification/normalization  
- Error-path testing for invalid geometries  
- Spatial edge-case resolution  

These fixtures simulate real geospatial patterns **without containing any real-world sensitive data**.

</div>

---

# 📘 Overview

Geometry fixtures allow the geospatial pipeline to be tested across dozens of real-world edge cases—  
but using **safe synthetic data** that poses **zero sovereignty or cultural risk**.

These fixtures validate:

- Geometry normalization (`geometry.ts`, `footprint.ts`)  
- H3 masking + generalization (when joined with masking fixtures)  
- Bounding-box extraction (`bounds.ts`)  
- Layer conversion reliability (`layers.ts`)  
- Timeline + map synchronization (via combined spatial–temporal tests)  
- Proper error handling and fallback behavior  

Fixtures must be:

- Synthetic (never real lat/lon coordinates)  
- Small + deterministic  
- Schema-validated  
- Designed to break things in useful ways  

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/fixtures/geometry/
├── polygon-simple.geojson          # Basic valid Polygon
├── polygon-hole.geojson            # Polygon with interior ring (hole)
├── multipolygon-complex.geojson    # MultiPolygon with disjoint regions
├── self-intersecting.geojson       # Known-invalid geometry (bowtie/cross)
├── unclosed-ring.geojson           # Invalid polygon ring for error-path testing
├── degenerate.geojson              # Zero-area or collapsed-geometry case
├── mixed-geometry.geojson          # FeatureCollection mixing Points, Lines, Polygons
├── empty-geometry.geojson          # Empty GeoJSON objects for guard testing
├── malformed.geojson               # Incorrect structure or invalid keys
└── README.md                       # This document
~~~

> Replace file names with your real fixture list once created.  
> Names above follow KFM’s recommended fixture taxonomy.

---

# 🧩 Fixture Types & Requirements

---

## 🟩 **polygon-simple.geojson**
A valid Polygon used to ensure the pipeline processes normal cases correctly.

---

## 🟦 **polygon-hole.geojson**
Tests:

- Polygon with an inner hole  
- Ring ordering  
- Correct area calculation  
- No accidental ring inversion  

---

## 🟧 **multipolygon-complex.geojson**
A synthetic example of:

- multiple disjoint regions  
- nested polygons  
- mixed ring counts  

Used to test:

- MultiPolygon → Polygon flattening  
- union/dissolve fallback behavior  
- footprint aggregation  

---

## 🟥 **self-intersecting.geojson**
Intentionally invalid (bowtie/cross shape) for testing:

- error handling  
- geometry repair logic  
- fallback to bounding box or masked region  

---

## 🟪 **unclosed-ring.geojson**
Tests:

- rings not returning to first coordinate  
- guard clauses in geometry normalization  

---

## 🟨 **degenerate.geojson**
Zero-area or nearly-zero-area geometry.

Used to test:

- centroid fallback paths  
- geometry replacement with masked generalization  
- pipeline stability with invalid features  

---

## 🟫 **mixed-geometry.geojson**
Includes:

- Points  
- Linestrings  
- Polygons  

Used to ensure:

- only Polygon/MultiPolygon are accepted  
- Points/Linestrings are rejected or upgraded appropriately  

---

## 🟫 **empty-geometry.geojson**
Tests:

- empty FeatureCollection  
- null geometries  
- missing coordinate arrays  
- safe fallback behavior  

---

## ❌ **malformed.geojson**
Purposely broken:

- missing `type` key  
- misspelled keys  
- wrong nesting  
- non-array coordinates  

Essential for negative-path tests.

---

# 🔐 FAIR+CARE Governance Rules

Even though these fixtures are synthetic, they must comply with:

- No real geographies  
- No real boundaries or culturally sensitive shapes  
- No resemblance to Tribal Nations, archaeological sites, sacred areas  
- Masking tests must not imply real sovereign territories  

Fixtures must emphasize structure, not actual world meaning.

---

# ♿ Accessibility Context

Indirect A11y requirements:

- Geometry → map layer conversion must not obscure accessibility features  
- Fallback states should still render accessible alternative text  
- Legend swatches derived from these fixtures must maintain WCAG contrast  

---

# 🧪 Tests Supported by These Fixtures

Fixtures support:

### 🟩 Geometry normalization tests  
`geometry.ts`, `footprint.ts`

### 🟦 H3 masking + pattern tests  
when combined with masking fixtures

### 🟧 MapView layer conversion tests  
`layers.ts`

### 🟥 Timeline + Map synchronization tests  
temporal + geometry combos

### 🟫 Error-handling tests  
invalid + malformed cases

---

# 🧪 Example Test

```ts
import feature from "./fixtures/geometry/multipolygon-complex.geojson";
import { normalizeGeometry } from "../../../geometry";

describe("normalizeGeometry", () => {
  it("flattens MultiPolygon and returns valid Polygon", () => {
    const output = normalizeGeometry(feature);
    expect(output.type === "Polygon" || output.type === "MultiPolygon").toBe(true);
  });
});
````

---

# 🕰 Version History

| Version | Date       | Summary                                                                    |
| ------: | ---------- | -------------------------------------------------------------------------- |
| v10.4.0 | 2025-11-15 | Added complete geometry fixture specification for KFM geospatial pipelines |
| v10.3.2 | 2025-11-14 | Added negative-path fixtures for geometry repair testing                   |
| v10.3.1 | 2025-11-13 | Initial geometry fixture directory created                                 |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
Synthetic Geometry Fixtures · FAIR+CARE Certified · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
