---
title: "📁 Kansas Frontier Matrix — Geospatial Footprint Fixtures (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/fixtures/footprints/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/geospatial-fixtures-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Test Fixtures"
intent: "geospatial-test-fixtures"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Spatial-Dependent"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/pipelines/geospatial/tests/fixtures/footprints/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Geometry"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../../../schemas/json/geospatial-footprints-fixtures.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/geospatial-footprints-fixtures-shape.ttl"
doc_uuid: "urn:kfm:doc:geospatial-footprints-fixtures-v10.4.0"
semantic_document_id: "kfm-doc-geospatial-footprints-fixtures"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/fixtures/footprints/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (test data only)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "coordinate inference"
  - "synthetic feature generation"
machine_extractable: true
accessibility_compliance: "N/A (test data)"
jurisdiction: "United States / Kansas"
classification: "Internal Test Fixture"
role: "test-fixture"
lifecycle_stage: "stable"
ttl_policy: "Persistent"
sunset_policy: "Replaced only when geospatial pipeline schema changes"
---

<div align="center">

# 📁 **Kansas Frontier Matrix — Geospatial Footprint Test Fixtures**  
`web/src/pipelines/geospatial/tests/fixtures/footprints/README.md`

**Purpose:**  
Provide **safe, governance-compliant, non-sensitive, synthetic geospatial fixtures** used for  
testing the geospatial pipeline, including masking, footprint normalization, bounding box  
calculation, spatial generalization, layer conversion, and Story Node/STAC integration logic.

These fixtures **must NOT contain real cultural, archaeological, tribal, or sensitive geographies**.

</div>

---

# 📘 Overview

This directory contains **synthetic or fully anonymized spatial datasets**, used exclusively to validate:

- H3 masking behavior  
- Footprint extraction + normalization logic  
- MultiPolygon → Polygon flattening  
- Bounding-box derivation  
- Geometry validity checks  
- Sovereignty/CARE overlays (mocked)  
- Layer conversion reliability  
- Spatial handling within Focus Mode & Story Node pipelines  

Fixtures must be:

- **Static**  
- **Deterministic**  
- **Non-PII**  
- **Non-sensitive**  
- **Governance-neutral**  
- **Schema-valid GeoJSON**  

They should closely mimic real-world cases without ever risking disclosure of protected locations.

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/fixtures/footprints/
├── sample-polygon.geojson           # Simple polygon footprint
├── sample-multipolygon.geojson      # Complex MultiPolygon case
├── sample-footprint-set.geojson     # Array of multiple footprints for batch tests
├── sample-masked-footprint.geojson  # Already-masked geometry (H3 or obfuscated)
├── sample-stac-footprint.geojson    # STAC Item geometry normalization test
├── sample-sovereignty-region.geojson# Synthetic region requiring masking
├── malformed-geometry.geojson       # Invalid geometry for negative-path tests
└── README.md                        # This document
~~~

> Actual filenames may vary — update the tree above to match your repo’s file names when they are created.

---

# 🧩 Fixture Requirements

Each fixture must satisfy:

### ✔ **1. Must be synthetic / non-sensitive**
No real archaeological sites, tribal boundaries, petroglyphs, or sacred sites.

### ✔ **2. Must pass GeoJSON validity checks**
- Closed rings  
- No self-intersection  
- Correct winding order (or at least repairable)  
- Proper Polygon / MultiPolygon format  

### ✔ **3. Must test both valid & invalid cases**
To validate pipeline resilience.

### ✔ **4. Must include sovereignty-safe examples**
For testing CARE + masking integration:
- `sample-sovereignty-region.geojson` must represent a **synthetic** culturally sensitive region  
- Must be safe for public use  
- Must require masking via `masking.ts`

### ✔ **5. Must include masked geometry**  
For validating inverse logic:
- Already-masked examples  
- Normalization of masked → masked  
- Masked footprint → layer conversion  

### ✔ **6. Must not exceed performance limits**
Fixtures should remain small, clean, and performant.

---

# 🔐 Governance & FAIR+CARE Rules

Fixtures MUST NOT:

- Reveal real-world sensitive geometry  
- Suggest precise locations of cultural/archaeological importance  
- Embed sovereignty information from real nations/tribes  
- Misrepresent CARE labels  
- Encode dataset risk classifications  

Fixtures MUST:

- Include synthetic sovereignty examples  
- Trigger correct masking behavior in tests  
- Preserve the governance workflow for:
  - Masking  
  - Labeling  
  - Metadata enforcement  

---

# 🧪 Testing Scenarios Powered by These Fixtures

These fixtures are used to validate:

### 🟦 **Masking Logic**
- H3 resolution boundaries  
- Sovereignty overlays  
- Generalization behavior

### 🟩 **Footprint Normalization**
- Polygon vs MultiPolygon  
- CRS normalization  
- Degenerate geometry handling  

### 🟧 **Layer Conversion**
- Footprint → MapView layer  
- Sovereignty → overlay  
- Story Node & STAC → merged footprints  

### 🟥 **Error Handling**
- Malformed geometry  
- Incomplete geometry  
- Empty rings  
- Non-standard coordinate arrays  

---

# 🧪 Example Test Reference

Example Jest test using these fixtures:

```ts
import polygon from "./fixtures/footprints/sample-polygon.geojson";
import { normalizeFootprint } from "../../../footprint";

describe("normalizeFootprint", () => {
  it("converts Polygon → normalized structure", () => {
    const result = normalizeFootprint(polygon);
    expect(result.type).toBe("Polygon");
    expect(result.coordinates.length).toBeGreaterThan(0);
  });
});
````

---

# 🕰 Version History

| Version | Date       | Summary                                                            |
| ------: | ---------- | ------------------------------------------------------------------ |
| v10.4.0 | 2025-11-15 | Created synthetic, governance-safe footprint fixture specification |
| v10.3.2 | 2025-11-14 | Added guidance for CARE masking tests                              |
| v10.3.1 | 2025-11-13 | Initial fixture directory established                              |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
Governance-Safe Synthetic Fixtures · FAIR+CARE Certified · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
