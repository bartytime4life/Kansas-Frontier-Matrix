---
title: "📅 Kansas Frontier Matrix — Date & Timeline Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/date/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-date-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-date-utilities"
role: "timeline-temporal-logic"
category: "Web · Utilities · Temporal"

classification: "Public Document"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "None"
indigenous_rights_flag: false
public_exposure_risk: "Low"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/utils/date/README.md@v10.4.1"
  - "web/src/utils/date/README.md@v10.3.2"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E52 Time-Span"
  schema_org: "Date"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-utils-date-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-utils-date-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-utils-date-readme:v11.2.2"
semantic_document_id: "kfm-doc-web-utils-date-readme"
event_source_id: "ledger:web/src/utils/date/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded on next temporal-logic revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📅 **Kansas Frontier Matrix — Date & Timeline Utilities (v11.2.2)**  
`web/src/utils/date/README.md`

**Purpose:**  
Define and govern the **temporal utilities** powering KFM’s timeline,  
OWL-Time–aligned intervals, Story Node v3 temporal reasoning,  
Focus Mode v3 context windows, and timeline–map synchronization.  
All utilities are **pure**, **deterministic**, **FAIR+CARE-governed**,  
and implemented under strict TypeScript safety.

</div>

---

# 🧭 1. Overview

The `utils/date/` module implements **core temporal logic** required by all major  
web subsystems in KFM v11:

- 🕒 **Timeline Engine** (multi-scale zoom + brushing)  
- ✨ **Story Node v3** (temporal footprints, fuzzy ranges)  
- 🎯 **Focus Mode v3** (temporal expansion & relevance windows)  
- 🔗 **Map & timeline synchronization**  
- 🧠 **Graph-derived event normalization**  
- 📦 **STAC/DCAT temporal extent normalization**  

All functions:

- Are **side-effect-free**  
- Obey **OWL-Time** semantics  
- Propagate FAIR/CARE metadata when temporal transformation occurs  
- Never “sharpen” uncertain dates into more precise ones  
- Produce deterministic output across all environments  

---

# 🗂 2. Directory Layout (Emoji-Rich · v11.2.2)

~~~text
web/src/utils/date/
│
├── 📅 parseDate.ts        # ISO/OWL-Time parser w/ fuzzy & uncertain-date support
├── 🗓 formatDate.ts       # UI-safe, deterministic temporal formatting
├── 🕒 timelineRange.ts    # Visible-window computation & padding logic
├── 🎚 precision.ts        # Granularity evaluator (year → month → day → decade → century)
├── 🔢 compareDates.ts     # Stable comparator for events, Story Nodes, STAC items
└── 🔧 normalizeDate.ts    # Canonicalization + FAIR/CARE metadata retention
~~~

---

# 🧱 3. Module Descriptions

## 📅 `parseDate.ts` — Temporal Parsing Engine

Parses:

- ISO 8601 (`1854-03-21`, `1870`, `1870-05`)  
- OWL-Time Story Node fields (`when.start`, `when.end`, `precision`)  
- Approximate expressions:  
  - `"ca. 1850"`, `"~1860"`, `"early 1800s"`, `"late 19th century"`  
- OCR-derived or ambiguous fields from archives  
- Graph events with mixed precision  

Returns:

```ts
interface DateMeta {
  date: Date | null;
  original: string;
  precision: "year" | "month" | "day" | "decade" | "century" | "unknown";
  approx: boolean;
  provenance?: string;
}
```

**FAIR rule:**  
Never discard original input; always store `original` & `approx`.

---

## 🗓 `formatDate.ts` — UI Temporal Formatting

- Localized yet deterministic  
- Handles approximate dates (`"c. 1850"`)  
- Generates accessible labels for timeline bands  
- Used by Story Node cards, Focus Mode summaries, dataset previews  

Examples:

| Input             | Output         |
|-------------------|----------------|
| `1854-03-21`      | `Mar 21, 1854` |
| `ca. 1850`        | `c. 1850`      |
| `{ decade: 1870 }`| `1870s`        |
| `century: 19`     | `19th century` |

---

## 🕒 `timelineRange.ts` — Range Expansion & Visible Window Logic

Used by:

- Focus Mode v3 context expansion  
- Timeline zoom logic  
- Map ↔ timeline synchronization  

Capabilities:

- Expands ranges by padding (years, months, days)  
- Clips reversed or invalid ranges  
- Merges overlapping intervals  
- Guarantees deterministic window selection  

Example:

```ts
computeTimelineWindow({ start: 1850, end: 1870 }, { padYears: 5 })
→ { start: 1845, end: 1875 }
```

**Governance requirement:**  
Timeline expansions for sensitive Story Nodes must NOT suggest false precision.

---

## 🎚 `precision.ts` — Granularity Evaluation

Determines how the UI renders a date:

- Year-only → wide block  
- Month → moderate block  
- Day → point highlight  
- Decade/century → abstract interval blocks  

Supports Story Node v3 mixed-precision overlays and timeline aggregation.

---

## 🔢 `compareDates.ts` — Stable Comparator

Provides consistent ordering for:

- Story Node events  
- Graph Events  
- STAC date ranges  
- Approximate and partial dates  
- BCE/CE alignment  

Ensures:

- No sorting jumps for BCE → CE transitions  
- Comparators do not exaggerate precision  
- Deterministic results across sessions  

---

## 🔧 `normalizeDate.ts` — Canonical Temporal Normalization

Creates a **FAIR, canonical** representation of any parsed date.

Adds metadata:

```ts
{
  value: "1854-03-21",
  canonical: "1854-03-21",
  precision: "day",
  approx: false,
  provenance: "graph-event"
}
```

Also ensures:

- APPROX flags are preserved  
- CIDOC `time:hasTime` compatibility  
- STAC/DCAT temporal extents are normalized without modification of meaning  

---

# 🧪 4. Testing Requirements

All utilities must include tests under:

~~~text
tests/web/utils/date/**
~~~

Tests MUST verify:

- Deterministic results for identical inputs  
- Preservation of approximate/fuzzy dates  
- OWL-Time alignment  
- FAIR temporal metadata retention  
- BCE/CE edge-case handling  
- Correct grouping & ordering via `compareDates.ts`  
- Timeline-range correctness (`timelineRange.ts`)  

---

# 🧭 5. Development Standards

Every module MUST:

- Be pure TypeScript (`.ts`)  
- Export pure functions  
- Include JSDoc docstrings  
- Avoid all side effects  
- Pass ESLint + Prettier + Docs Lint  
- Validate against telemetry schemas for any date-derived metrics  
- Comply with FAIR+CARE & sovereignty rules  

---

# 🔮 6. Future Extensions (v11.3+)

- BCE support across all rendering engines  
- Hybrid calendar support (Julian ↔ Gregorian)  
- Prehistoric/paleoclimate fuzzy ranges  
- Temporal-density heatmap generation  
- Sub-daily precision for modern sensor data  

---

# 🕰 7. Version History

| Version | Date       | Changes                                                                                      |
|--------:|------------|----------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Full v11.2.2 upgrade; emoji directory; Focus Mode v3 + Story Node v3 alignment; FAIR/CARE update. |
| v10.4.1 | 2025-11-15 | Initial KFM-MDP v10.4 version.                                                               |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Utils](../README.md) · [🧭 Web Source Overview](../../README.md) · [🌐 Web Platform Overview](../../../README.md)

</div>