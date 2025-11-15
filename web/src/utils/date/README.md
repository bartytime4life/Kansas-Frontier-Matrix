---
title: "📅 Kansas Frontier Matrix — Date & Timeline Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/date/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-date-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-date-utilities"
fair_category: "F1-A1-I1-R1"
---

<div align="center">

# 📅 **Kansas Frontier Matrix — Date & Timeline Utilities**  
`web/src/utils/date/README.md`

**Purpose:**  
Document the **temporal utility modules** powering the Kansas Frontier Matrix's timeline,  
OWL-Time–aligned intervals, Story Node temporal reasoning, Focus Mode v2 temporal expansion,  
and timeline–map synchronization.  
All utilities are deterministic, pure, FAIR+CARE-compliant, and TypeScript-strict.

</div>

---

## 🧭 Overview

The `utils/date/` module provides **core temporal logic** for the KFM web client.  
These utilities support:

- Parsing OWL-Time / ISO 8601 / Story Node temporal fields  
- Handling uncertain & approximate dates (“circa”, ranges, BC/AD edge cases)  
- Normalizing temporal precision (year/month/day granularity)  
- Expanding ranges for Focus Mode v2 context windows  
- Computing timeline zoom levels and visible windows  
- Converting graph events → renderable UI intervals  
- Ensuring temporal FAIRness & provenance retention on all values  

The functions are **side-effect-free**, **tree-shakeable**, and centrally tested.

---

## 📂 Directory Layout

```

web/src/utils/date/
│
├── parseDate.ts          # ISO/OWL-Time parser w/ uncertainty support
├── formatDate.ts         # Human-readable formatting (UI-safe)
├── timelineRange.ts      # Time-range expansion + clipping
├── precision.ts          # Granularity evaluator (year→month→day)
├── compareDates.ts       # Stable comparator for event sorting
└── normalizeDate.ts      # Canonicalization & FAIR metadata retention

````

---

## 🧱 Module Descriptions

### 🧩 `parseDate.ts`
Parses any of the following into a stable DateMeta object:

- ISO 8601 (`1854-03-21`, `1870`, `1870-05`)  
- OWL-Time Story Node (`when.start`, `when.end`, `precision`)  
- Approximate historical labels (`"circa 1850"`, `"~1860"`, `"late 1700s"`)  
- Partial dates from historical OCR or Focus Mode v2 summaries  

Returns:

```ts
interface DateMeta {
  date: Date | null;
  original: string;
  precision: "year" | "month" | "day" | "decade" | "century" | "unknown";
  approx: boolean;
}
````

---

### 🧩 `formatDate.ts`

UI-only formatting engine.

* Localized but deterministic output
* Supports approximate rendering (“ca. 1850”)
* Used by timeline labels, Focus Mode cards, Story Nodes
* Ensures WCAG-AAA contrast when rendered in timeline bands

Examples:

| Input        | Output         |
| ------------ | -------------- |
| `1854-03-21` | `Mar 21, 1854` |
| `ca. 1850`   | `c. 1850`      |
| `1870-05`    | `May 1870`     |

---

### 🧩 `timelineRange.ts`

Used by:

* Focus Mode v2 temporal expansion
* Timeline zoom logic
* Map/timeline sync engine

Capabilities:

* Expands range by surrounding “context windows”
* Clips invalid or reversed ranges
* Handles overlapping ranges for merged visual intervals
* Fully deterministic → same inputs always produce same window

Example:

```ts
computeTimelineWindow({ start: 1850, end: 1870 }, { padYears: 5 })
→ { start: 1845, end: 1875 }
```

---

### 🧩 `precision.ts`

Granularity engine to determine how the UI should render a date.

* Year-only → wide block
* Month → mid-size block
* Day → pinpoint highlight
* Decade/century → collapsed abstract interval

Supports mixed-precision Story Node overlays.

---

### 🧩 `compareDates.ts`

Consistent sorting across:

* Raw ISO strings
* Story Node events
* Graph Events
* Approximate or missing dates

Handles:

* Partial dates
* Ties
* BCE/CE normalization (ensuring no jump discontinuity)

---

### 🧩 `normalizeDate.ts`

Canonicalizes a date for internal use.

Adds FAIR metadata:

```ts
{
  value: "1854-03-21",
  canonical: "1854-03-21",
  provenance: "graph-event",
  precision: "day",
  approx: false
}
```

Used by all mapping, timeline, and Focus Mode v2 paths.

---

## 🧪 Testing Requirements

All utilities must include matching tests under:

```
tests/web/utils/date/*.test.ts
```

Tests must verify:

* Deterministic output
* Complete precision coverage
* Correct handling of approximate dates
* Alignment with Story Node schema
* Proper FAIR preservation of metadata

---

## 🧭 Development Standards

All modules in this directory MUST:

* Be TypeScript-only (`.ts`)
* Contain complete JSDoc docstrings
* Avoid side effects & global state
* Pass ESLint + Prettier
* Pass KFM Docs Lint + FAIR/CARE metadata propagation checks
* Integrate with Story Node temporal schema

---

## 🗺️ Future Extensions (v10.5+)

* BCE support across all render engines
* Multi-calendar support (Julian ↔ Gregorian conversions)
* “Historical fuzzy ranges” for deep-time archaeology & paleoclimate overlays
* Temporal heatmap generation for density-of-events analysis

---

## 🏁 Version History

| Version | Date       | Changes                                                    |
| ------- | ---------- | ---------------------------------------------------------- |
| v10.4.1 | 2025-11-15 | Initial creation following KFM-MDP v10.4 formatting rules. |

---
