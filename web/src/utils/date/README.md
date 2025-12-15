---
title: "📅 Kansas Frontier Matrix — Date & Timeline Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/date/README.md"
version: "v11.2.3"
last_updated: "2025-12-15"
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
markdown_protocol_version: "KFM-MDP v11.2.6"
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
  - "web/src/utils/date/README.md@v11.2.2"
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

doc_uuid: "urn:kfm:doc:web-utils-date-readme:v11.2.3"
semantic_document_id: "kfm-doc-web-utils-date-readme"
event_source_id: "ledger:web/src/utils/date/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded on next temporal-logic revision"
jurisdiction: "Kansas / United States"
---

# 📅 Kansas Frontier Matrix — Date & Timeline Utilities (v11.2.3)

`web/src/utils/date/README.md`

Define and govern the temporal utilities powering KFM’s timeline, OWL-Time–aligned intervals,
Story Node v3 temporal reasoning, Focus Mode v3 context windows, and timeline–map synchronization.
All utilities are pure, deterministic, FAIR+CARE-governed, and implemented under strict TypeScript safety.

## 📘 Overview

The `utils/date/` module implements core temporal logic required by major web subsystems in KFM v11:

- 🕒 Timeline Engine (multi-scale zoom + brushing)
- ✨ Story Node v3 (temporal footprints, fuzzy ranges)
- 🎯 Focus Mode v3 (temporal expansion & relevance windows)
- 🔗 Map & timeline synchronization
- 🧠 Graph-derived event normalization
- 📦 STAC/DCAT temporal extent normalization

All functions:

- are side-effect-free
- obey OWL-Time semantics
- propagate FAIR/CARE metadata when temporal transformation occurs
- never “sharpen” uncertain dates into more precise ones
- produce deterministic output across all environments

## 🗂️ Directory Layout

~~~text
web/src/utils/date/
├── 📄 parseDate.ts        # ISO/OWL-Time parser w/ fuzzy & uncertain-date support
├── 📄 formatDate.ts       # UI-safe, deterministic temporal formatting
├── 📄 timelineRange.ts    # Visible-window computation & padding logic
├── 📄 precision.ts        # Granularity evaluator (year → month → day → decade → century)
├── 📄 compareDates.ts     # Stable comparator for events, Story Nodes, STAC items
└── 📄 normalizeDate.ts    # Canonicalization + FAIR/CARE metadata retention
~~~

## 🧭 Context

Where these utilities sit in the web stack:

- API/services fetch data and pass it to temporal utilities for validation/normalization.
- Timeline/map components consume normalized ranges and formatted labels.
- Focus Mode and Story Nodes rely on “fuzzy-safe” transformations (no invented precision).

Typical call paths:

- Story Nodes: `parseDate` → `normalizeDate` → `formatDate` → render
- Timeline: `normalizeDate` → `precision` → `timelineRange` → render
- Sorting/grouping: `parseDate`/`normalizeDate` → `compareDates` → stable ordering

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Raw temporal fields\n(STAC/DCAT, Story Node, graph events)"] --> B["parseDate.ts"]
  B --> C["normalizeDate.ts\ncanonical + metadata retention"]
  C --> D["precision.ts\nrendering granularity"]
  C --> E["compareDates.ts\nstable ordering"]
  C --> F["timelineRange.ts\nwindow + padding"]
  C --> G["formatDate.ts\nUI labels (a11y-safe)"]
~~~

## 🧱 Architecture

### 📅 `parseDate.ts` — Temporal Parsing Engine

Parses:

- ISO 8601 (`1854-03-21`, `1870`, `1870-05`)
- OWL-Time Story Node fields (`when.start`, `when.end`, `precision`)
- approximate expressions:
  - `ca. 1850`, `~1860`, `early 1800s`, `late 19th century`
- OCR-derived or ambiguous fields from archives
- graph events with mixed precision

Returns:

~~~ts
interface DateMeta {
  date: Date | null;
  original: string;
  precision: "year" | "month" | "day" | "decade" | "century" | "unknown";
  approx: boolean;
  provenance?: string;
}
~~~

FAIR rule:
- never discard original input; always preserve `original` and `approx`

### 🗓 `formatDate.ts` — UI Temporal Formatting

- localized yet deterministic
- handles approximate dates (`c. 1850`)
- generates accessible labels for timeline bands
- used by Story Node cards, Focus Mode summaries, dataset previews

Examples:

| Input | Output |
|---|---|
| `1854-03-21` | `Mar 21, 1854` |
| `ca. 1850` | `c. 1850` |
| `{ decade: 1870 }` | `1870s` |
| `century: 19` | `19th century` |

### 🕒 `timelineRange.ts` — Range Expansion & Visible Window Logic

Used by:

- Focus Mode v3 context expansion
- timeline zoom logic
- map ↔ timeline synchronization

Capabilities:

- expands ranges by padding (years, months, days)
- clips reversed or invalid ranges
- merges overlapping intervals
- guarantees deterministic window selection

Example:

~~~ts
computeTimelineWindow({ start: 1850, end: 1870 }, { padYears: 5 })
→ { start: 1845, end: 1875 }
~~~

Governance requirement:
- timeline expansions for sensitive Story Nodes must not suggest false precision

### 🎚 `precision.ts` — Granularity Evaluation

Determines how the UI renders a date:

- year-only → wide block
- month → moderate block
- day → point highlight
- decade/century → abstract interval blocks

Supports Story Node v3 mixed-precision overlays and timeline aggregation.

### 🔢 `compareDates.ts` — Stable Comparator

Provides consistent ordering for:

- Story Node events
- graph events
- STAC date ranges
- approximate and partial dates
- BCE/CE alignment

Ensures:

- no sorting jumps for BCE → CE transitions
- comparators do not exaggerate precision
- deterministic results across sessions

### 🔧 `normalizeDate.ts` — Canonical Temporal Normalization

Creates a FAIR, canonical representation of any parsed date.

Adds metadata:

~~~ts
{
  value: "1854-03-21",
  canonical: "1854-03-21",
  precision: "day",
  approx: false,
  provenance: "graph-event"
}
~~~

Also ensures:

- approx flags are preserved
- CIDOC time-span compatibility patterns are supported in downstream JSON-LD
- STAC/DCAT temporal extents are normalized without modification of meaning

## 📦 Data & Metadata

Temporal transforms must retain meaning and context:

- preserve the original source string and declared precision
- retain approximate/uncertain markers end-to-end
- avoid converting partial dates into implied full dates (e.g., `1870` must not become `1870-01-01` without explicit labeling)

Recommended normalized fields for downstream UI:

- `original` (string)
- `canonical` (string or null)
- `precision` (enum)
- `approx` (boolean)
- `range` (start/end where known)
- `provenance` (optional string tag)

## ⚖ FAIR+CARE & Governance

Non-negotiables:

- never “sharpen” a fuzzy/approximate time into a specific day/month
- never infer a precise range when only a coarse range exists
- always preserve uncertainty markers for user-facing transparency
- when content is governance-sensitive, prefer generalized labels and stable, non-leaky ordering

Governance failures are treated as blocking defects when they change meaning or imply false precision.

## 🧪 Validation & CI/CD

All utilities must include tests under:

~~~text
tests/web/utils/date/**
~~~

Tests must verify:

- deterministic results for identical inputs
- preservation of approximate/fuzzy dates
- OWL-Time alignment behavior in parsing/normalization
- FAIR temporal metadata retention
- BCE/CE edge-case handling
- correct grouping and ordering via `compareDates.ts`
- timeline-range correctness (`timelineRange.ts`)

## 🧠 Story Node & Focus Mode Integration

Temporal utilities must support narrative safety:

- Story Node temporal footprints must render without inventing certainty
- Focus Mode context windows must expand without implying the story “started earlier” than evidence supports
- Timeline labels must remain accessible and explicit about fuzziness (e.g., “c. 1850”, “late 19th century”)

Recommended patterns:

- surface `approx` markers in UI labels
- keep “unknown” explicit rather than silently dropping time
- keep sorting stable even when precision differs (coarse dates should not bounce in ordering)

## 🧭 Context

Development standards for this module:

- pure TypeScript (`.ts`)
- export pure functions only
- include JSDoc docstrings for public functions
- avoid all side effects
- pass ESLint + Prettier + docs lint
- comply with FAIR+CARE and sovereignty rules

## 🧪 Validation & CI/CD

If any date-derived telemetry is emitted by callers, it must conform to `telemetry_schema` referenced in front-matter.

## 🧭 Context

## 🧭 Context
(Reserved for future cross-links to web timeline engine architecture and map/time synchronization docs.)

## 🧭 Context

## 🔮 Future Extensions (v11.3+)

- BCE support across all rendering engines
- hybrid calendar support (Julian ↔ Gregorian)
- prehistoric/paleoclimate fuzzy ranges
- temporal-density heatmap generation
- sub-daily precision for modern sensor data

## 🕰️ Version History

| Version | Date | Changes |
|---:|---:|---|
| v11.2.3 | 2025-12-15 | Reformatted to KFM-MDP v11.2.6 headings/fences; preserved all v11.2.2 content; clarified governance-safe normalization and added diagram + integration notes. |
| v11.2.2 | 2025-11-28 | Full v11.2.2 upgrade; emoji directory; Focus Mode v3 + Story Node v3 alignment; FAIR/CARE update. |
| v10.4.1 | 2025-11-15 | Initial KFM-MDP v10.4 version. |
| v10.3.2 | 2025-11-14 | Added temporal + provenance utilities. |

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned

[⬅️ Back to Web Utils](../README.md) · [🧭 Web Source Overview](../../README.md) · [🌐 Web Platform Overview](../../../README.md)

</div>
