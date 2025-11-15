---
title: "🧠 Kansas Frontier Matrix — Graph & Entity Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/graph/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-graph-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-graph-utilities"
fair_category: "F1-A1-I1-R1"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Graph & Entity Utilities**  
`web/src/utils/graph/README.md`

**Purpose:**  
Define the **frontend-side normalization, relationship flattening, subgraph extraction, and  
Focus Mode v2 binding utilities** used by the KFM React client to convert Neo4j API responses  
into stable UI-ready structures.  
These utilities are deterministic, typed, FAIR+CARE-compliant, and central to timeline–map–Focus  
synchronization.

</div>

---

## 🧭 Overview

The `web/src/utils/graph/` directory contains **pure TypeScript utilities** that:

- Normalize entities and relationships from Neo4j/FastAPI  
- Convert nested graph subgraphs → flattened UI structures  
- Bind graph entities to map/timeline highlighting (Focus Mode v2)  
- Apply FAIR+CARE provenance metadata to all graph-derived fields  
- Ensure consistent ordering, grouping, and ID resolution  
- Provide deterministic data transforms across the entire React tree  

These modules **never** call the network, mutate global state, or manipulate the DOM.

---

## 📂 Directory Layout

```

web/src/utils/graph/
│
├── entityNormalize.ts     # Normalizes graph entities to UI-safe formats
├── relationFlatten.ts     # Converts nested Neo4j-style subgraphs → flat relationships
├── focusBindings.ts       # Binds Focus Mode v2 results to map/timeline selections
├── idUtils.ts             # Stable ID creation, hashing, deduplication
└── groupByType.ts         # Groups graph nodes by logical type (Place, Person, Event, Document)

````

---

## 🧱 Module Descriptions

### 🧩 `entityNormalize.ts`

Normalizes graph nodes returned by the API into a consistent shape used across the UI.

Handles:

- Node type canonicalization (`Place`, `Person`, `Event`, `Document`, `StoryNode`)  
- Metadata merging from STAC/DCAT + graph properties  
- FAIR provenance (`source`, `license`, `confidence`, `corroborationCount`)  
- Temporal normalization (`when.start`, `when.end`, precision) via `utils/date`  
- Geometry extraction for Places & Story Nodes  

Example output:

```ts
interface NormalizedEntity {
  id: string;
  type: "Place" | "Event" | "Person" | "Document" | "StoryNode";
  label: string;
  description?: string;
  temporal?: { start: string; end?: string; precision: string };
  spatial?: GeoJSON.Geometry;
  provenance: { source: string; license: string; confidence?: number };
}
````

This is used by all entity cards, tooltips, Focus Mode, and search results.

---

### 🧩 `relationFlatten.ts`

Neo4j subgraphs are nested.
The frontend requires clean arrays.

This utility:

* Converts `{ nodes: [...], relationships: [...] }` → flat structures
* Creates `edges: Array<{ from, to, type }>`
* Deduplicates repeated nodes/edges
* Sorts edges by relationship type (semantic ordering)
* Applies CARE flags (e.g., hides restricted relationships in the UI)

This is essential for:

* Graph-based event summaries
* Story Node narrative linking
* Focus Mode v2 reasoning traces
* Relationship graphs shown in detail sidebar

---

### 🧩 `focusBindings.ts`

The glue layer between **graph results** and **map/timeline selections**.

Functionality:

* Determines which Places, Events, Documents, and Story Nodes should be
  highlighted for a selected entity
* Computes **temporal windows** for Focus Mode
* Computes **map extents** based on locations of related nodes
* Outputs a stable `FocusContext` object:

```ts
interface FocusContext {
  focusId: string;
  relatedPlaces: string[];
  relatedEvents: string[];
  relatedDocuments: string[];
  timelineWindow: { start: string; end: string };
  bbox: [number, number, number, number] | null;
}
```

This powers the synchronized UI experience for Focus Mode v2.

---

### 🧩 `idUtils.ts`

Ensures stable, deterministic identification:

* Hashes raw graph IDs into safe frontend IDs if needed
* Deduplicates IDs across nested subgraph structures
* Performs stable sorting for deterministic UIs
* Encodes composite IDs for Story Node relationships

Used everywhere IDs appear — search, highlighting, keying React lists.

---

### 🧩 `groupByType.ts`

Groups mixed node arrays into:

```
{
  places: [...],
  events: [...],
  people: [...],
  documents: [...],
  storyNodes: [...]
}
```

Used by:

* Focus Mode v2 summaries
* Entity panels
* Relationship graph visualization
* Search results

---

## 🧪 Testing Requirements

All tests are located under:

```
tests/web/utils/graph/*.test.ts
```

Tests MUST verify:

* Deterministic normalization across all node types
* Correct flattening of nested subgraphs
* ID stability across runs
* CARE-compliant concealment of sensitive relationships
* FAIR provenance propagation
* Correct FocusContext generation across edge cases

---

## ⚙️ Development Standards

All modules in this directory MUST:

* Be written strictly in TypeScript
* Export pure, side-effect-free functions
* Pass ESLint + Prettier + KFM Docs Lint
* Retain all FAIR metadata and CARE sensitivity flags
* Include complete JSDoc docstrings
* Avoid MapLibre/DOM/React imports (data only)
* Ensure compatibility with Story Node schema & Focus Mode v2

---

## 🧭 Future Extensions (v10.5+)

* Graph federation adapters (multi-region knowledge graphs)
* Temporal relationship density metrics for timeline heatmaps
* Story Node merge/resolution helpers
* Cross-entity confidence scoring matrices
* AI narrative provenance trace integration

---

## 🏁 Version History

| Version | Date       | Changes                                         |
| ------- | ---------- | ----------------------------------------------- |
| v10.4.1 | 2025-11-15 | Initial creation using KFM-MDP v10.4 standards. |

---
