---
title: "🛠️ Kansas Frontier Matrix — General Utility Modules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
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

# 🛠️ **Kansas Frontier Matrix — General Utility Modules**  
`web/src/utils/general/README.md`

**Purpose:**  
Document the **foundational utility helpers** used across the KFM React + MapLibre web client,  
including memoization, cloning, validation guards, object/array helpers, and other building blocks  
shared across map, graph, API, timeline, and Focus Mode v2 systems.  
All modules are pure, deterministic, TypeScript-strict, and KFM-MDP v10.4 compliant.

</div>

---

## 🧭 Overview

The `web/src/utils/general/` directory contains cross-cutting utilities that:

- Provide **safe, predictable low-level behaviors**  
- Enable **performance optimizations** (memoization, structural cloning)  
- Supply **runtime assertions & invariant guards**  
- Offer **universal emptiness and type-check helpers**  
- Are imported by *every other* utils module (date, graph, map, api)  
- Ensure FAIR+CARE-compliant handling of metadata when used in data transforms  
- Support MCP documentation-first reproducibility via deterministic operations  

These helpers form the *standard library* for the KFM frontend.

All utilities here are **pure functions**, export-safe, test-covered, and never reference DOM or network.

---

## 📂 Directory Layout

```

web/src/utils/general/
│
├── memo.ts           # Deterministic memoization with TTL + argument hashing
├── deepClone.ts      # Fast structural deep clone with cycle detection
├── isEmpty.ts        # Robust emptiness checker for all serializable types
├── invariant.ts      # Assertion utility with MCP-compliant error messages
├── equals.ts         # Deep equality checker for objects/arrays
├── typeGuards.ts     # Handy TS predicate fns: isString, isNumber, isObject, etc.
└── objectMerge.ts    # Safe deep merge respecting FAIR/CARE metadata retention

````

---

## 🧱 Module Descriptions

### 🧩 `memo.ts`
Deterministic memoization layer used throughout the KFM frontend.

Features:

- Argument hashing (stable, collision-safe)  
- Optional TTL expiration  
- Prevents recomputation in Focus Mode v2, timeline ranges, expensive STAC transforms  
- Purely functional — no global caches  

Example:

```ts
const heavy = memo(fn, { ttl: 5000 });
````

---

### 🧩 `deepClone.ts`

Pure structural cloning with:

* Cycle detection
* FAIR/CARE metadata preservation
* Support for arrays, objects, primitives
* Immutable output guaranteed

Used to protect React state from accidental mutation.

---

### 🧩 `isEmpty.ts`

Universal emptiness checker for:

* `null`, `undefined`
* Arrays (length 0)
* Objects (no enumerable keys)
* Strings (trimmed)
* Maps/Sets (size 0)

Used before timeline/map calculations to ensure safe fallbacks.

---

### 🧩 `invariant.ts`

Assertion helper used across utility modules.

* Throws deterministic error with MCP-aligned diagnostics
* Guards impossible branches
* Avoids obscure runtime bugs

Example:

```ts
invariant(Array.isArray(nodes), "Expected array of graph nodes");
```

---

### 🧩 `equals.ts`

Deep equality comparison:

* Handles nested objects, arrays
* Stable sorting for unordered structures
* Type-aware comparisons
* Used in memoization hashing + Focus Mode v2 dedupe logic

---

### 🧩 `typeGuards.ts`

A collection of TS-level type guards:

* `isString`, `isNumber`, `isBoolean`
* `isObject`, `isArray`, `isPlainObject`
* `isDate`, `isJson`
* `isGeoJSONGeometry`

These dramatically reduce React component conditional clutter.

---

### 🧩 `objectMerge.ts`

Safe structural merge:

* Deep merges without mutating source objects
* Never overwrites FAIR/CARE metadata automatically
* Performs deterministic resolution of conflicts
* Used heavily in normalized graph + STAC metadata merging

---

## 🧪 Testing Requirements

All modules must be covered by corresponding tests in:

```
tests/web/utils/general/*.test.ts
```

Tests MUST verify:

* Deterministic memoization under varied argument lists
* Correct deepClone behavior (cycles, metadata, nested types)
* equivalence + non-equivalence in equals.ts
* Proper failures + MCP-style diagnostics in invariant.ts
* Strict type guard correctness
* objectMerge respecting metadata + non-destructive behavior

---

## ⚙️ Development Standards

All utilities MUST:

* Be written in **TypeScript**
* Export only pure functions
* Pass ESLint + Prettier + KFM Docs Lint
* Avoid DOM, MapLibre, network, or global state
* Preserve FAIR/CARE metadata when merging or cloning
* Include complete JSDoc docstrings

---

## 🧭 Future Extensions (v10.5+)

* Deterministic hash module for reproducible caching
* Structural diffing (`diffObjects`) used in telemetry & debug overlays
* Pattern matching helpers for Story Node narrative objects
* RFC 8785–compliant canonicalization helpers for JSON serialization
* High-performance “immutable patch” utilities for React state transitions

---

## 🏁 Version History

| Version | Date       | Changes                                         |
| ------- | ---------- | ----------------------------------------------- |
| v10.4.1 | 2025-11-15 | Initial creation following KFM-MDP v10.4 rules. |

---
