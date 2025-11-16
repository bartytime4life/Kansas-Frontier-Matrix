---
title: "🧰 Kansas Frontier Matrix — Web Utilities Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-utils-readme-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-utils-overview"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (logic-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/utils/README.md@v10.3.2"
  - "web/src/utils/README.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/web-utils-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-utils-readme-shape.ttl"
doc_uuid: "urn:kfm:doc:web-utils-readme-v10.4.0"
semantic_document_id: "kfm-doc-web-utils-readme"
event_source_id: "ledger:web/src/utils/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "overview"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded on next utils-layer revision"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — Web Utilities Overview**  
`web/src/utils/README.md`

**Purpose:**  
Document the **utility modules** used across the Kansas Frontier Matrix (KFM) Web Platform — providing  
pure, deterministic helper functions for formatting, schema guards, spatial math, JSON-LD generation,  
accessibility utilities, URL building, and type validation.  
Utilities ensure repeatable logic that supports all features, components, and pipelines.

</div>

---

# 📘 Overview

Utilities in `web/src/utils/**`:

- Provide **stateless, deterministic** functions  
- Contain **no UI logic**  
- Contain **no side effects**  
- Can be used anywhere (features, hooks, components, pipelines)  
- Must be **heavily tested** with unit and integration tests  
- Are required to be **FAIR+CARE-safe**, especially for spatial utilities  
- Must follow **WCAG 2.1 AA** rules where A11y is involved  
- Must correctly propagate **governance metadata** when appropriate  
- Must avoid speculative or unverified transformations  

Utilities support:

- Focus Mode v2.5  
- Story Node v3  
- STAC/DCAT payload handling  
- Timeline + Map synchronization  
- Telemetry  
- Governance display  
- Accessibility-first UI  
- JSON-LD semantics  
- Spatial/temporal calculations  

---

# 🧱 Directory Structure

~~~text
web/src/utils/
├── formatters.ts             # Formatting: numbers, units, dates, captions
├── jsonld.ts                 # JSON-LD builders for entities, datasets, story nodes
├── guards.ts                 # Schema + type guards (Story Node, STAC, Focus Mode)
├── bbox.ts                   # Spatial bounding box utilities (merge, pad, validate)
├── a11y.ts                   # Accessibility helpers (contrast, reduced-motion)
├── provenance.ts             # Provenance-building utilities (PROV-O aligned)
├── url.ts                    # URL-safe builders for routes/query params
├── color.ts                  # WCAG-compliant color utilities
├── temporal.ts               # OWL-Time aligned temporal math
└── array.ts                  # Deterministic array helpers (unique, group, sort)
~~~

---

# 🧩 Module Responsibilities

## 📏 `formatters.ts`
Provides formatting helpers:

- Dates (UTC, historical, fuzzy intervals)  
- Narrative captions  
- Temporal ranges  
- Scientific units  
- Accessibility-friendly number formatting  
- CARE-sensitive wording (“generalized location”, “restricted”)  

Guarantees:

- No misleading or overly precise representations  
- Consistency across pages and features  

---

## 🧬 `jsonld.ts`
Generates JSON-LD blocks for:

- Story Node v3  
- Focus Mode targets  
- STAC/DCAT datasets  
- Governance metadata  
- Page-level semantic descriptors  

Guarantees:

- Schema.org + CIDOC-CRM alignment  
- No speculative semantic relationships  
- Valid machine-extractable metadata  

---

## 🛡️ `guards.ts`
Provides strict runtime validation:

- Story Node schema  
- Focus Mode v2.5 payloads  
- STAC Items & Collections  
- Provenance objects  
- Telemetry events  

Guarantees:

- Malformed data never reaches UI components  
- Governance + CARE metadata is present before rendering  

---

## 📦 `bbox.ts`
Spatial utilities for:

- BBox merging  
- Expansion/padding  
- Point-in-bounds checks  
- GeoJSON validity checks  
- Geodesic-safe calculations  

Used in:

- MapLibre layers  
- Story Node footprints  
- STAC preview extents  

Governance:

- Must enforce rules preventing exposure of restricted coordinates  

---

## ♿ `a11y.ts`
Accessibility utilities including:

- Reduced-motion helpers  
- Contrast ratio checks  
- Color token selection  
- Screen-reader safe text formatting  

Guarantees:

- WCAG 2.1 AA compliance  
- No inaccessible color ramps  

---

## 🧾 `provenance.ts`
Builds explicit provenance chains:

- Rights-holder → source → tool → transformation  
- Links to SBOM + manifest metadata  
- Supports PROV-O graph creation  
- Used by Story Nodes, datasets, Focus Mode  

Guarantees:

- Clear, non-invented provenance  
- Ethical + transparent lineage  

---

## 🔗 `url.ts`
Generates route-safe URLs:

- Avoids leakage of sensitive IDs  
- Encodes query params safely  
- Supports timeline/map/focus deep links  
- Used by Share buttons and navigation  

Governance:

- Must ensure masked datasets never expose raw coordinates in URLs  

---

## 🎨 `color.ts`
Contains WCAG AA color utilities:

- Accessible palettes  
- CARE label color mapping  
- Focus/Story Node highlight colors  
- Light/dark token selection  

Must meet:

- 4.5:1 contrast ratio minimum  
- Accessible theming in light/dark modes  

---

## ⏳ `temporal.ts`
Temporal math helpers:

- OWL-Time alignment  
- Fuzzy intervals  
- Range merging  
- Story Node timeline calculations  
- STAC/DCAT extent normalization  

Guarantees:

- Accurate, non-speculative temporal logic  
- Governance-compliant text for uncertain dates  

---

## 🔢 `array.ts`
Provides deterministic array utilities:

- Sorted uniqueness  
- Stable grouping  
- Map/filter/reduce helpers  
- Sequence utilities for timeline aggregation  

Guarantees:

- No random/non-deterministic ordering  
- Stable repeated renders  

---

# 🔐 Governance Considerations

All utilities MUST:

- Respect CARE labels  
- Avoid generating sensitive or precise coordinate values  
- Avoid speculative interpretations of cultural/historical data  
- Include provenance-building support where data is transformed  
- Ensure masking/aggregation rules are not bypassed  
- Follow `ai_transform_prohibited` constraints  

---

# ♿ Accessibility Requirements

Utilities must:

- Apply accessible color rules  
- Never return inaccessible tokens  
- Support reduced-motion flows  
- Support screen-reader-friendly outputs  

A11y regressions block CI.

---

# 📈 Telemetry Responsibilities

Utilities that produce telemetry signals must:

- Use schema-valid event structures  
- Include governance metadata where appropriate  
- Avoid PII  
- Support sustainability metrics  

Telemetry flows into:

`releases/<version>/focus-telemetry.json`

---

# 🧪 Testing Requirements

Each utility MUST have:

- Unit tests  
- Integration tests where applicable  
- Schema tests (guards)  
- A11y color contrast tests (color + a11y utils)  
- Governance tests (provenance + masking)  

Tests located at:

~~~text
tests/unit/web/utils/**
tests/integration/web/utils/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full rewrite to KFM-MDP v10.4; added governance, A11y, spatial, temporal, and JSON-LD modules |
| v10.3.2 | 2025-11-14 | Added temporal + provenance utilities |
| v10.3.1 | 2025-11-13 | Initial utilities overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>