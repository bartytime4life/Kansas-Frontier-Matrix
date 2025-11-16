---
title: "⏳ Kansas Frontier Matrix — Temporal Fixtures for Geospatial Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/tests/fixtures/temporal/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/geospatial-temporal-fixtures-v1.json"
governance_ref: "../../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Test Fixtures"
intent: "geospatial-temporal-fixtures"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Temporal-Dependent"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/pipelines/geospatial/tests/fixtures/temporal/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E52 Time-Span"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
json_schema_ref: "../../../../../../../../schemas/json/geospatial-temporal-fixtures.schema.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/geospatial-temporal-fixtures-shape.ttl"
doc_uuid: "urn:kfm:doc:geospatial-temporal-fixtures-v10.4.0"
semantic_document_id: "kfm-doc-geospatial-temporal-fixtures"
event_source_id: "ledger:web/src/pipelines/geospatial/tests/fixtures/temporal/README.md"
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
  - "temporal inference"
  - "synthetic chronology generation"
machine_extractable: true
accessibility_compliance: "N/A (test data)"
jurisdiction: "United States / Kansas"
classification: "Internal Test Fixture"
role: "test-fixture"
lifecycle_stage: "stable"
ttl_policy: "Persistent"
sunset_policy: "Updated only when temporal schema changes"
---

<div align="center">

# ⏳ **Kansas Frontier Matrix — Temporal Test Fixtures for Geospatial Pipelines**  
`web/src/pipelines/geospatial/tests/fixtures/temporal/README.md`

**Purpose:**  
Provide **synthetic, deterministic, governance-safe temporal fixtures** used to test  
geospatial pipelines that must combine **spatial geometry** with **temporal ranges**,  
including Story Node v3, STAC/DCAT metadata, Focus Mode highlights,  
and TimelineView synchronization.

These fixtures model **complex temporal behaviors** without containing any real historical  
or culturally sensitive dates.

</div>

---

# 📘 Overview

Temporal fixtures exist to validate the following cross-system geospatial behaviors:

- Merging spatial footprints with temporal intervals  
- Normalizing incomplete or fuzzy temporal data  
- Ensuring OWL-Time–compatible interval structures  
- Handling temporal uncertainty for narrative nodes  
- Aligning Story Node and STAC footprints with timeline ranges  
- Ensuring consistency between:
  - `timelinePipeline.ts`
  - `storyPipeline.ts`
  - `geospatial/footprint.ts`  
  - `geospatial/bounds.ts`  
  - `geospatial/layers.ts`

All fixtures in this directory MUST be:

- **Synthetic** (no real-world historical data)  
- **Governance-neutral**  
- **Schema-valid**  
- **Small and deterministic**  
- **Representative of real temporal patterns** (but not using real dates)  

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/tests/fixtures/temporal/
├── sample-interval.json            # Simple valid interval (start + end)
├── sample-open-start.json          # Interval missing a start date
├── sample-open-end.json            # Interval missing an end date
├── sample-instant.json             # Instant in time (start = end)
├── sample-fuzzy.json               # Fuzzy or uncertain interval
├── sample-story-interval.json      # Story Node–style temporal span
├── sample-stac-extent.json         # STAC-style temporal extent object
├── malformed-interval.json         # Invalid or broken temporal structure (negative-path testing)
└── README.md                       # This document
~~~

> Replace with the exact filenames your project will use — these names follow KFM’s recommended fixture naming.

---

# 🧩 Fixture Types & Requirements

### ✔ `sample-interval.json`  
A normal time span:

- `"start": "1900-01-01"`  
- `"end": "1950-01-01"`

Used to test standard normalization.

---

### ✔ `sample-open-start.json`  
Used to validate handling of:

- `"start": null`  
- `"end": "1940-01-01"`

Ensures timeline + story pipelines gracefully handle open intervals.

---

### ✔ `sample-open-end.json`  
Validates:

- `"start": "1800-01-01"`  
- `"end": null"`

Ensures upper-bounded open ranges render correctly in TimelineView.

---

### ✔ `sample-instant.json`  
An instant event:

- `"start": "2001-03-15"`  
- `"end": "2001-03-15"`

Tests instant events in Story Nodes + event markers.

---

### ✔ `sample-fuzzy.json`  
Tests timelines with uncertainty:

- `"start": "1800"`  
- `"end": "1800"`  
- `"certainty": "low"`

Or:

```json
{
  "start": "1850-01-01",
  "end": "1875-12-31",
  "fuzzy": true
}
````

---

### ✔ `sample-story-interval.json`

Used to validate Story Node v3 → Timeline integration.

Includes:

* narrative time spans
* uncertain offsets
* optional date metadata

---

### ✔ `sample-stac-extent.json`

Tests STAC/DCAT temporal extent parsing:

* `"interval": [ ["1970-01-01", "1980-01-01"] ]`

Ensures `stacPipeline` and `timelinePipeline` handle STAC time ranges.

---

### ✔ `malformed-interval.json`

Used for negative-path tests:

* out-of-order dates
* invalid strings
* malformed interval structures

The geospatial pipeline must:

* gracefully reject
* surface a governance-safe error
* avoid crashing

---

# 🔐 Governance & FAIR+CARE Rules

Even though these fixtures contain **synthetic time values**, they MUST:

* Not embed culturally sensitive real-world time periods
* Not encode real treaty dates, cessions, conflicts, massacres, etc.
* Not imply Indigenous or sovereignty-related timelines
* Not reference actual historical figures or nations

Temporal fixtures should represent **structure**, not **history**.

---

# ♿ Accessibility Requirements

Indirect requirements (applied through TimelineView):

* Must allow components to render alt-text for temporal uncertainty
* Must allow timeline to compute accessible SR-only descriptions
* Fuzzy dates should clearly mark uncertainty for A11y

---

# 🧪 Testing Workflows Powered by These Fixtures

Temporal fixtures are used in:

### 🟩 **Timeline Pipeline Tests**

* range merging
* uncertainty propagation
* open interval handling

### 🟦 **Story Pipeline Tests**

* Story Node → temporal extents
* fuzzy narrative timelines

### 🟧 **Focus Pipeline Tests**

* focus highlight → timeline highlight mapping

### 🟥 **Geospatial Pipeline Tests**

* footprint + temporal alignment
* timeline slicing for layers

---

# 🧪 Example Test

```ts
import interval from "./fixtures/temporal/sample-interval.json";
import { normalizeTemporal } from "../../../temporal";

describe("normalizeTemporal", () => {
  it("produces a valid OWL-Time interval", () => {
    const normalized = normalizeTemporal(interval);
    expect(normalized.start).toBeDefined();
    expect(normalized.end).toBeDefined();
  });
});
```

---

# 🕰 Version History

| Version | Date       | Summary                                                                |
| ------: | ---------- | ---------------------------------------------------------------------- |
| v10.4.0 | 2025-11-15 | Added complete temporal fixture specification for geospatial pipelines |
| v10.3.2 | 2025-11-14 | Introduced fuzzy and STAC-temporal test cases                          |
| v10.3.1 | 2025-11-13 | Initial synthetic temporal assets                                      |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
FAIR+CARE Certified · Test Fixtures · Version-Pinned
Validated under MCP-DL v6.3 & KFM-MDP v10.4.1

</div>
