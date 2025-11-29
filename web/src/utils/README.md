---
title: "🧰 Kansas Frontier Matrix — Web Utilities Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-utils-readme-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-utils-overview"
role: "overview"
category: "Web · Utilities · Architecture"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/utils/README.md@v10.3.1"
  - "web/src/utils/README.md@v10.3.2"
  - "web/src/utils/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/web-utils-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-utils-readme-shape.ttl"

doc_uuid: "urn:kfm:doc:web-utils-readme:v11.2.2"
semantic_document_id: "kfm-doc-web-utils-readme"
event_source_id: "ledger:web/src/utils/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
ttl_policy: "Annual review"
sunset_policy: "Superseded on next utils-layer revision"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — Web Utilities Overview (v11.2.2)**  
`web/src/utils/README.md`

**Purpose**  
Document the **utility modules** used across the Kansas Frontier Matrix (KFM) Web Platform — providing  
pure, deterministic helper functions for formatting, schema guards, spatial math, JSON-LD generation,  
accessibility utilities, URL building, temporal logic, and type validation.  
Utilities ensure repeatable, FAIR+CARE-safe logic supporting every component, pipeline, and feature in the web application.

</div>

---

# 📘 Overview

Utilities in `web/src/utils/**`:

- Provide **state-less, deterministic**, pure functions  
- Contain **no UI logic** and **no side effects**  
- Are imported everywhere (hooks, pipelines, components, services)  
- Must be **FAIR+CARE-safe**, sovereign-safe, and governance-aware  
- Must uphold **WCAG 2.1 AA+** accessibility patterns  
- Must avoid speculative or unverified logic  
- Must include **unit, integration, A11y, and governance tests**  
- Must align with:
  - KFM-OP v11 ontology expectations  
  - KFM-PDC v11 data contracts  
  - KFM-MDP v11.2.2 documentation rules  

Utilities form the **shared logic layer** that powers Focus Mode v3, Story Node v3, STAC/DCAT explorers, timeline interactions, and map synchronization.

---

# 🧱 Directory Structure (Emoji-Rich · Box-Safe · v11.2.2)

~~~text
web/src/utils/
├── ✨ formatters.ts             # Formatting: numbers, units, dates, captions, CARE-aware text
├── 🧬 jsonld.ts                 # JSON-LD builders (Story Nodes, Datasets, Focus Mode governance)
├── 🛡️ guards.ts                 # Type/schema guards (Story Node v3, STAC/DCAT, Focus, telemetry)
├── 🗺️ bbox.ts                   # Spatial math (BBox merge, clamp, pad, safe extents, no leaks)
├── ♿ a11y.ts                    # Accessibility helpers (contrast, motion, SR text, focus control)
├── 🧾 provenance.ts             # Provenance-building utilities (PROV-O, SBOM/manifest linking)
├── 🔗 url.ts                    # Governance-safe URL builders (no PK leaks, no raw coords)
├── 🎨 color.ts                  # WCAG AA+ color utilities (contrast, tokens, CARE state colors)
├── ⏳ temporal.ts               # OWL-Time aligned temporal logic (fuzzy ranges, intervals)
└── 🔢 array.ts                  # Deterministic array helpers (unique, group, stable sort)
~~~

All modules must remain **side-effect-free, deterministic, and safe across governance contexts**.

---

# 🧩 Module Responsibilities

## ✨ `formatters.ts`
- Dates, ranges, time labels  
- Accessible number formatting  
- CARE-safe wording (“generalized location”, “restricted dataset”)  
- Scientific units  
- Narrative microcopy  

**Never:**  
- invent precision  
- override CARE/sovereignty wording  
- produce inaccessible text  

---

## 🧬 `jsonld.ts`
- Build JSON-LD for:
  - Story Node v3  
  - Focus Mode v3 focal entities  
  - STAC/DCAT datasets  
  - Governance metadata  

Aligned with:
- schema.org  
- CIDOC-CRM  
- PROV-O  
- KFM-OP v11  

**Never:**  
- create speculative relationships  
- output unverifiable provenance  

---

## 🛡️ `guards.ts`
- Validate:
  - Story Nodes  
  - STAC Items  
  - DCAT datasets  
  - Governance metadata  
  - Telemetry events  
  - Focus Mode payloads  

Guarantee:
- invalid data is rejected before rendering  
- governance metadata exists before sensitive output  

---

## 🗺️ `bbox.ts`
Spatial helpers for:
- merging & padding  
- safe extent calculation  
- preventing map over-zoom of masked sites  
- normalizing STAC bounding boxes  

**Must never:**
- recreate precise coordinates for masked/generalized data  

---

## ♿ `a11y.ts`
- Contrast utilities  
- Screen-reader helpers  
- Reduced-motion flows  
- Keyboard focus utilities  
- Label/ARIA helpers  

Must satisfy:
- WCAG 2.1 AA+  
- high-contrast mapping  

---

## 🧾 `provenance.ts`
- Build PROV-O aligned traces  
- Connect UI provenance to manifest/SBOM/lineage  
- Provide UI-readable provenance descriptors  

---

## 🔗 `url.ts`
- URL generation for deep links (timeline, map, focus)  
- Query encoding  
- **Governance-safe**: no restricted IDs, no micro-coords  
- Normalizes H3 masking and generalization  

---

## 🎨 `color.ts`
- WCAG AA+ color contrast  
- CARE-status mapping  
- Light/dark/high-contrast themes  
- Returns safe palettes only  

---

## ⏳ `temporal.ts`
- OWL-Time aligned temporal ranges  
- Fuzzy interval labeling  
- STAC/DCAT → timeline conversions  
- Timeline highlight intervals  

---

## 🔢 `array.ts`
- Stable uniqueness  
- Deterministic grouping  
- Predictable sorting for Story Nodes, events, datasets  
- Build timeline summary rows  

---

# 🔐 Governance Requirements

All utilities must:

- Respect CARE labels & sovereignty rules  
- Honor masking/generalization constraints  
- Include provenance features where applicable  
- Avoid generating:
  - speculative historical interpretations  
  - overprecise coordinates  
  - unverifiable narratives  

Governance failures → CI failure (faircare_validate.yml).

---

# ♿ Accessibility Requirements

Utilities must always:

- Maintain WCAG AA+ contrast  
- Support keyboard navigation patterns  
- Provide safe token combinations  
- Be compatible with reduced-motion modes  

A11y regressions → CI block.

---

# 📈 Telemetry Responsibilities

Utilities must:

- Produce schema-valid telemetry structures  
- Support event classification  
- Exclude PII  
- Attach governance metadata where relevant  
- Flow into `focus-telemetry.json`  

---

# 🧪 Testing Requirements

Must include:

- Unit tests  
- Integration tests (pipelines/UI interactions)  
- Schema/type guard tests  
- A11y contrast tests  
- Governance tests (masking, sovereignty, provenance)  

All under:

~~~text
tests/unit/web/utils/**
tests/integration/web/utils/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-28 | Complete emoji-restoration, governance alignment, MDP v11.2.2 upgrade, A11y/CARE overhaul |
| v10.4.0 | 2025-11-15 | Full rewrite to KFM-MDP v10.4; added governance, A11y, spatial, temporal, JSON-LD modules |
| v10.3.2 | 2025-11-14 | Added temporal + provenance utilities |
| v10.3.1 | 2025-11-13 | Initial utilities overview |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../README.md) · [🌐 Web Platform Overview](../../README.md) · [🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>