---
title: "📚 Kansas Frontier Matrix — Story Node Fixtures for Geospatial Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/fixtures/storynodes/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/geospatial-storynode-fixtures-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Test Fixtures"
intent: "geospatial-storynode-fixtures"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Narrative-Dependent"
sensitivity_level: "Low–Medium (all synthetic)"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true
provenance_chain:
  - "web/src/pipelines/geospatial/tests/fixtures/storynodes/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../../../schemas/json/geospatial-storynode-fixtures.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/geospatial-storynode-fixtures-shape.ttl"
doc_uuid: "urn:kfm:doc:geospatial-storynode-fixtures-v10.4.0"
semantic_document_id: "kfm-doc-geospatial-storynode-fixtures"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/fixtures/storynodes/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (test fixtures only)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative expansions"
  - "invented historical claims"
  - "coordinate inference"
machine_extractable: true
accessibility_compliance: "N/A (test fixtures)"
jurisdiction: "United States / Kansas"
classification: "Internal Test Fixture"
role: "test-fixture"
lifecycle_stage: "stable"
ttl_policy: "Persistent"
sunset_policy: "Updated only when Story Node schema changes"
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Story Node Test Fixtures for Geospatial Pipelines**  
`web/src/pipelines/geospatial/tests/fixtures/storynodes/README.md`

**Purpose:**  
Provide **synthetic Story Node v3 datasets** used to test all cross-system geospatial + temporal pipelines  
involving Story Nodes, including:

- spatial footprint normalization  
- temporal range alignment  
- provenance metadata handling  
- integration with masking / sovereignty systems  
- timeline → map → focus synchronization  
- Story Node layer generation for MapView  

All Story Node fixtures are **synthetic** and **never use real historical data**.

</div>

---

# 📘 Overview

Story Node fixtures simulate how real Story Node v3 payloads behave in KFM, allowing safe, precise testing of:

- Narrative metadata → geospatial footprints  
- OWL-Time temporal intervals  
- Fuzzy/uncertain ranges  
- Provenance chain structuring  
- Multi-footprint scenarios  
- Governance + CARE restrictions  
- Spatial → timeline → focus interactions  

These fixtures test the interplay between:

- `storyPipeline.ts`
- `timelinePipeline.ts`
- `focusPipeline.ts`
- `geospatial/footprint.ts`
- `geospatial/masking.ts`
- `geospatial/bounds.ts`
- `geospatial/layers.ts`

They must be:

- **synthetic**  
- **deterministic**  
- **small**  
- **schema-valid Story Node v3 JSON**  
- **governance-neutral**

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/fixtures/storynodes/
├── storynode-simple.json             # Minimal Story Node w/ 1 footprint + clean dates
├── storynode-multipolygon.json       # MultiPolygon footprint case
├── storynode-fuzzy-temporal.json     # Fuzzy/uncertain temporal span
├── storynode-open-interval.json      # Missing start OR end date
├── storynode-masked.json             # Story Node requiring spatial masking
├── storynode-provenance.json         # Synthetic provenance chain for testing UI/graph joins
├── storynode-multi-footprint.json    # Multiple spatial footprints (complex case)
├── storynode-no-geometry.json        # Story Node without a footprint (narrative-only)
├── malformed-storynode.json          # Invalid Story Node (negative-path test)
└── README.md                         # This document
~~~

---

# 🧩 Fixture Descriptions

---

## ✔ `storynode-simple.json`
A basic valid Story Node containing:

- one clean Polygon footprint  
- clear start & end temporal bounds  
- minimal narrative string  
- simple provenance metadata  

Used to verify baseline pipeline behavior.

---

## ✔ `storynode-multipolygon.json`
Tests handling of:

- MultiPolygon geometry  
- flattening or normalization  
- correct centroid and bounding box resolution  
- rendering in MapView  

---

## ✔ `storynode-fuzzy-temporal.json`
Includes:

- `"fuzzy": true`  
- approximate or uncertain date ranges  
- Story Node narrative that references broad eras  

Validates:

- timeline fuzzy logic  
- appropriate visual fading in TimelineView  
- proper labeling for A11y  

---

## ✔ `storynode-open-interval.json`
Contains missing upper or lower bounds:

- `"start": "1700-01-01", "end": null`  
- OR `"start": null, "end": "1850-01-01"`  

Tests UI rendering for open intervals.

---

## ✔ `storynode-masked.json`
Contains:

- valid footprint  
- `"care": "sovereignty"` or `"care": "restricted"` tag  
- requires H3 masking  

Ensures pipelines properly apply:

- sovereignty masking  
- masked layer color schemes  
- sensitivity warnings  

---

## ✔ `storynode-provenance.json`
Synthetic Story Node containing:

- long provenance chain  
- nested transformations  
- derived-from relationships  

Used to validate:

- ProvenancePanel  
- ProvenanceChip  
- PROV-O alignment in converters  

---

## ✔ `storynode-multi-footprint.json`
Tests:

- multiple footprints  
- varying geometry shapes  
- potentially conflicting bounding boxes  
- temporal alignment per footprint  

A stress test for `footprint.ts`.

---

## ✔ `storynode-no-geometry.json`
Represents:

- narrative-only Story Nodes  
- no spatial component  
- purely temporal or semantic content  

Used to test fallback map behavior.

---

## ✔ `malformed-storynode.json`
Used for:

- schema guard tests  
- Story Node schema mismatch  
- missing required fields  
- invalid coordinate arrays  
- narrative missing required metadata  

Pipeline must:

- throw a clear governance-safe error  
- never crash  
- never display invalid geometry  
- log telemetry  

---

# 🔐 FAIR+CARE Governance Rules

Even synthetic Story Node fixtures must:

- Never reference real historical events  
- Never encode actual Indigenous or sovereignty-sensitive footprints  
- Never reproduce treaty lines or culturally restricted areas  
- Use ONLY fictional narratives and coordinates  
- Mark masked cases with `"care": "sovereignty"` or `"care": "restricted"`  

Every Story Node introduced must be:

- governance-neutral  
- synthetic  
- completely safe for public test exposure  

---

# ♿ Accessibility Requirements

Story Node fixture testing must ensure:

- temporal ranges produce A11y-consistent timeline text  
- masking + narrative warnings are readable in high-contrast mode  
- missing or fuzzy dates receive proper alt-text messaging  
- provenance chain remains screen-reader accessible  

---

# 🧪 Testing Workflows Supported by These Fixtures

### 🟩 Story Pipeline Tests
- narrative → timeline → map sync  
- provenance propagation  
- mapping Story Node → timeline items  

### 🟦 Geospatial Pipeline Tests
- footprint normalization  
- masking + sovereignty overlay  

### 🟧 Focus Pipeline Tests
- Story Node suggestions from Focus Mode  
- narrative highlight generation  

### 🟫 Timeline Pipeline Tests
- interval normalization  
- fuzzy-range visualization  
- open-interval handling  

### 🟥 Negative-path Tests
- malformed nodes  
- missing geometry  
- missing temporal metadata  

---

# 🧪 Example Test

```ts
import node from "./fixtures/storynodes/storynode-simple.json";
import { normalizeStoryNode } from "../../../storyPipeline";

describe("normalizeStoryNode", () => {
  it("produces a valid domain Story Node", () => {
    const out = normalizeStoryNode(node);
    expect(out.id).toBeDefined();
    expect(out.spatial).toBeDefined();
    expect(out.temporal).toBeDefined();
  });
});
````

---

# 🕰 Version History

| Version | Date       | Summary                                                          |
| ------: | ---------- | ---------------------------------------------------------------- |
| v10.4.0 | 2025-11-15 | Added full synthetic Story Node test fixture specification       |
| v10.3.2 | 2025-11-14 | Added fuzzy + multi-footprint Story Node fixture recommendations |
| v10.3.1 | 2025-11-13 | Established baseline Story Node fixture directory                |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
Synthetic Story Node Fixtures · FAIR+CARE Certified · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
