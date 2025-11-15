---
title: "🧩 Kansas Frontier Matrix — Web Utility Modules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-utils-v3.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-utilities"
fair_category: "F1-A1-I1-R1"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Web Utility Modules**  
`web/src/utils/README.md`

**Purpose:**  
Document the **core JavaScript/TypeScript utility modules** used across the KFM React + MapLibre web client.  
These utilities provide **state management helpers**, **STAC/DCAT parsing**, **MapLibre layer transforms**,  
**API wrappers**, and **frontend-safe data normalization** that keep the UI predictable, stable, and FAIR+CARE aligned.

</div>

---

## 🧭 Overview

The `web/src/utils/` directory contains **pure, side-effect-free utility functions** that support the UI’s  
timeline, map rendering, Focus Mode v2, and semantic search. These utilities follow KFM’s front-end standards:

- Deterministic outputs  
- Fully typed (TypeScript)  
- No direct DOM manipulation  
- No external network calls (handled in `web/src/api/`)  
- MCP-compliant documentation  
- FAIR+CARE metadata propagation when handling dataset descriptors  

All utilities are designed to be **tree-shakeable**, **unit-testable**, and **frontend-performant**.

---

## 📂 Directory Layout

```

web/src/utils/
│
├── date/
│   ├── parseDate.ts
│   ├── formatDate.ts
│   └── timelineRange.ts
│
├── map/
│   ├── stacToMaplibre.ts
│   ├── layerStyles.ts
│   ├── bboxUtils.ts
│   └── featureSelectors.ts
│
├── graph/
│   ├── entityNormalize.ts
│   ├── relationFlatten.ts
│   └── focusBindings.ts
│
├── api/
│   └── validateResponse.ts
│
└── general/
├── memo.ts
├── deepClone.ts
├── isEmpty.ts
└── invariant.ts

```

---

## 🗂 Module Classes

### 📅 Date & Timeline Utilities (`utils/date/`)

These functions ensure **OWL-Time-aligned**, ISO-normalized temporal handling.

| Utility | Description |
|--------|-------------|
| `parseDate` | Converts API/graph timestamps → JS `Date` objects (with precision tracking). |
| `formatDate` | Human-readable date formatting following KFM display rules. |
| `timelineRange` | Expands time ranges (start/end) for timeline window calculations. |

All functions support **approximate date labels** (e.g., “circa 1854”) mapped from the CIDOC/Story Node time model.

---

### 🗺 Map Utilities (`utils/map/`)

MapLibre-safe geospatial helpers.

| Utility | Description |
|--------|-------------|
| `stacToMaplibre` | Converts STAC Items → MapLibre layer descriptors. Preserves bbox, geometry, projections. |
| `layerStyles` | Shared styling tokens for map layers (opacity, filter rules, highlight modes). |
| `bboxUtils` | Fit-to-extent helpers, buffer calculations, timeline-synced zooming. |
| `featureSelectors` | Extracts features from GeoJSON sources using stable ID patterns. |

These utilities form the backbone of **3D map synchronization**, **Focus Mode map centering**, and **layer overlays**.

---

### 🧠 Knowledge Graph Helpers (`utils/graph/`)

| Utility | Description |
|--------|-------------|
| `entityNormalize` | Normalizes API-returned graph objects for React state. |
| `relationFlatten` | Converts nested graph structures into UI-ready flat lists. |
| `focusBindings` | Binds Focus Mode v2 outputs to map & timeline selections. |

These utilities decouple the **Neo4j graph schema** from the UI layer.

---

### 🌐 API Utilities (`utils/api/`)

| Utility | Description |
|--------|-------------|
| `validateResponse` | Ensures API responses conform to JSON Schema + telemetry expectations. |

---

### 🧩 General Utilities (`utils/general/`)

| Utility | Description |
|--------|-------------|
| `memo` | Lightweight memoization with TTL, used for expensive derived computations. |
| `deepClone` | Pure structural clone (avoids React state mutation issues). |
| `isEmpty` | Universal emptiness checker (objects, arrays, strings). |
| `invariant` | Internal assertion helper for safety-critical conditions. |

---

## 🧪 Testing

All utilities must include **unit tests** located at:

```

tests/web/utils/<module>.test.ts

```

Tests must validate:

- Deterministic outputs  
- Type correctness  
- No side effects  
- MCP documentation references  
- FAIR+CARE propagation for metadata-handling functions  

---

## ⚙️ Development Standards

All utility modules must:

- Be written in **TypeScript**  
- Contain **JSDoc docstrings**  
- Avoid hidden global state  
- Include **edge-case handling**  
- Pass ESLint + Prettier  
- Pass KFM Docs Lint (metadata in comments when applicable)  

---

## 🧭 Future Extensions (v10.5+)

Planned enhancements:

- STAC v1.1 projection utilities (`proj:` extension)  
- MapLibre 3D terrain integration helpers  
- Predictive-layer transforms (for 2030–2100 climate scenarios)  
- Multi-graph federation utilities for cross-region knowledge graphs  

---

## 🏁 Version History

| Version | Date | Changes |
|---------|-------|---------|
| v10.4.1 | 2025-11-15 | Initial creation using KFM-MDP v10.4 rules. |

---
