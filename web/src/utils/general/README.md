---
title: "🧭 Kansas Frontier Matrix — General Utilities Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/general/README.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-utils-general-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-general-utilities"
fair_category: "F1-A1-I1-R1"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — General Utility Modules**  
`web/src/utils/general/README.md`

**Purpose:**  
Provide a unified reference and architectural description for **general-purpose helper utilities** used across the KFM Web Platform (React + MapLibre + Timeline Engine).  
These utilities are **pure, deterministic, MCP-compliant, FAIR-safe**, and reused across all major UI subsystems including:  
– Timeline engine  
– Focus Mode v2  
– Story Node rendering  
– Graph API adapters  
– Map rendering layers  

</div>

---

## 🧩 Overview

The `general` utilities comprise the lowest-level foundation for the KFM frontend.  
They provide:

- **Deterministic memoization**
- **Deep structural cloning (cycle-safe)**
- **Robust equality checking**
- **Value normalization**
- **Type guards**
- **Invariant enforcement**
- **General-purpose merge functions that are FAIR+/CARE-aware**

These utilities *must* remain completely **side-effect free**, **dependency-free**, and **React-agnostic**, making them safe to use throughout the monorepo.

They are required by:

- `web/src/utils/api`
- `web/src/utils/date`
- `web/src/utils/map`
- `web/src/utils/graph`
- Focus Mode v2 narrative assembly
- Timeline event bucketing + deduplication
- Story Node field normalization

General utilities live here:

```

web/src/utils/general/
│
├── memo.ts
├── deepClone.ts
├── equals.ts
├── invariant.ts
├── isEmpty.ts
├── typeGuards.ts
└── objectMerge.ts

```

---

## 🧠 Design Requirements & Constraints

All utilities in this directory must follow:

### **1. Deterministic Behavior (MCP Rule 2.4)**
- Zero reliance on system time, locale, or global state
- Pure functions only
- Same input → same output, guaranteed

### **2. FAIR+CARE Safety**
- No silent deletion of metadata fields  
- Merges must preserve provenance & CARE-related labels unless explicitly overridden
- All deepClone functions retain `__meta` blocks

### **3. Cross-Pipeline Consistency**
Results from these functions must behave identically across:

- GraphQL + REST API responses  
- Timeline Engine sort/group operations  
- Story Nodes (CIDOC/OWL-Time)  
- MapLibre layer adapters  

### **4. Zero React Imports**
No React, no hooks, no DOM access, no browser globals.

---

## 📂 Module Details

### 🧱 `memo.ts` — Deterministic + TTL-Aware Memoization  
Provides argument-hash–based memoization with optional expiration.

Used by:
- Focus Mode v2 summarizer
- Graph → MapLayer transformation cache
- Timeline step quantization

Features:
- TTL support  
- Stable JSON hashing  
- Automatic orphan cleanup  

---

### 🧱 `deepClone.ts` — Structural, Cycle-Safe Clone  
Guaranteed deep clone for:

- Arrays
- Objects
- Nested graph fragments
- Story Node narrative blocks
- GeoJSON structures

Includes:
- Cycle detection  
- `__meta` retention  
- GeoJSON-safe numerical normalization  

---

### 🧱 `equals.ts` — Deep Equality  
Used heavily for:

- Memo caches  
- Story Node diffing  
- Focus Mode v2 "semantic window" comparisons  
- Map layer rerender pruning  

Supports:
- Arrays  
- Objects  
- GeoJSON  
- Primitive unions  

---

### 🧱 `invariant.ts`  
Strict runtime assertions with MCP-format errors.

Example:
```

invariant(typeof id === "string", "Expected string id in entity resolver");

```

This enforces correctness boundaries between modules.

---

### 🧱 `isEmpty.ts`  
Robust emptiness detection for:

- Arrays  
- Objects  
- Sets/Maps  
- Nullish values  
- GeoJSON geometries  

Used for preflight validation in API + Timeline layers.

---

### 🧱 `typeGuards.ts`  
Provides strong TypeScript guards for:

- `isString`, `isNumber`, `isBoolean`
- `isArray`, `isObject`
- `isPlainObject`
- `isDate`
- `isGeoJSONGeometry`

These are foundational for runtime validation of API responses.

---

### 🧱 `objectMerge.ts` — FAIR+CARE–Aware Merge  
A deterministic deep merge function with:

- No silent drops of provenance  
- Controlled overwrite rules  
- Metadata priority safety features  
- Support for Story Node property merging  
- GeoJSON property + bbox precedence logic  

---

## 🧪 Testing

All utilities must have tests located at:

```

tests/web/utils/general/*.test.ts

```

Test classes must cover:

- Value stability across repeated calls  
- Cross-object equality logic  
- Metadata retention rules  
- Extreme structural clones  
- FAIR+CARE contract enforcement  

---

## 🧭 Future Enhancements (v10.5+)

- Deterministic hashing module (for GraphQL optimistic updates)
- Object diff engine (Story Node delta compression)
- Immutable patch utility (React state optimizer)
- WASM-backed structural clone for large datasets

---

## 🏁 Version History

| Version | Date       | Notes |
|---------|------------|-------|
| v10.4.1 | 2025-11-15 | Initial file creation using KFM-MDP v10.4 standards |

---
