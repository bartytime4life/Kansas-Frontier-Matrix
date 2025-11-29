---
title: "🧭 Kansas Frontier Matrix — General Utilities Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/general/README.md"
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
telemetry_schema: "../../../../schemas/telemetry/web-utils-general-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-general-utilities"
role: "frontend-foundation"
category: "Web · Utilities · Core Logic"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (logic-only)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/utils/general/README.md@v10.4.1"
  - "web/src/utils/general/README.md@v10.3.2"
  - "web/src/utils/general/README.md@v10.3.1"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../schemas/json/web-utils-general-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-utils-general-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-utils-general-readme:v11.2.2"
semantic_document_id: "kfm-doc-web-utils-general-readme"
event_source_id: "ledger:web/src/utils/general/README.md"
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

# 🧭 **Kansas Frontier Matrix — General Utility Modules (v11.2.2)**  
`web/src/utils/general/README.md`

**Purpose:**  
Provide a unified reference and architectural description for **general-purpose helper utilities** used across the KFM Web Platform (React + MapLibre + Timeline + Focus Mode).  
These utilities are **pure, deterministic, MCP-compliant, FAIR+CARE-safe**, and reused across all major UI subsystems including:  
– Timeline engine  
– Focus Mode v3  
– Story Node v3 rendering  
– Graph & API adapters  
– Map rendering layers  
– STAC/DCAT explorers  

</div>

---

## 🧩 1. Overview

The `general` utilities comprise the **lowest-level foundation** for the KFM frontend logic.

They provide:

- 🧠 **Deterministic memoization**  
- 📦 **Deep structural cloning (cycle-safe)**  
- 🧮 **Robust equality checking**  
- 🧹 **Value normalization & emptiness detection**  
- 🛡️ **Type guards & invariants**  
- 🔗 **FAIR+CARE-aware merge functions**  

Core rules:

- **No side effects** (no global mutation, no I/O, no DOM)  
- **No dependencies** on React, browser APIs, or MapLibre/Cesium  
- **No speculative behavior** (no invented data, no guessed semantics)  
- All outputs must be **safe to pass into higher-level utilities** (`graph`, `bbox`, `temporal`, etc.)  

They are required by:

- `web/src/utils/api`  
- `web/src/utils/temporal`  
- `web/src/utils/graph`  
- `web/src/utils/bbox`  
- Focus Mode v3 narrative assembly layers  
- Timeline event bucketing, deduplication & grouping  
- Story Node v3 field normalization & diffing  

---

## 🧱 2. Directory Structure (Emoji-Rich · v11.2.2)

~~~text
web/src/utils/general/
│
├── 🧠 memo.ts           # Deterministic + TTL-aware memoization utilities
├── 🧬 deepClone.ts      # Cycle-safe, metadata-preserving deep cloning
├── ⚖️ equals.ts         # Deep equality comparisons for value graphs
├── ❗ invariant.ts      # Runtime assertions & invariants (MCP-style errors)
├── 🕳️ isEmpty.ts       # Robust emptiness checks (arrays, objects, sets, maps, GeoJSON)
├── 🧾 typeGuards.ts     # Strong TypeScript runtime type guards
└── 🔀 objectMerge.ts    # FAIR+CARE-aware deterministic deep merge
~~~

These general utilities are deliberately small, sharp, and **zero-UI**.

---

## 🧠 3. Design Requirements & Constraints

### 3.1 Deterministic Behavior (MCP Rule 2.4)

- No usage of `Date.now`, `Math.random`, or non-deterministic APIs  
- Same input → same output across runs, CI nodes, and environments  
- Pure functions only (no side effects, no shared mutable state)  

### 3.2 FAIR+CARE Safety

- No silent deletion of provenance or CARE metadata  
- No silent overwrites of sensitive flags (e.g., `sensitivity`, `sovereignty`, `careLabel`)  
- Deep clone & merge functions MUST retain `__meta` / governance blocks unless explicitly configured otherwise  

### 3.3 Cross-Pipeline Consistency

Results from these functions must behave **identically** across:

- GraphQL + REST responses  
- Timeline Engine sort/group operations  
- Story Node v3 normalization (CIDOC/OWL-Time alignment)  
- MapLibre layer configuration merging  
- Focus Mode v3 state merges  

### 3.4 Zero React / Browser Imports

- **No React**  
- **No DOM** or `window` usage  
- **No MapLibre/Cesium** imports  

Modules in this directory are safe to reuse in Node, browser, tests, and tools.

---

## 📂 4. Module Details

### 🧠 `memo.ts` — Deterministic Memoization

Provides argument-hash–based memoization with optional TTL.

Used by:

- Focus Mode v3 summarization caching  
- Graph → Map layer transformation caching  
- Timeline quantization & bucketing helpers  

Features:

- Stable argument hashing (e.g., via JSON-safe deterministic hash)  
- Optional TTL expiry for caches  
- Orphan cleanup: discard unused entries over time  
- Compatible with unit tests & SSR  

---

### 🧬 `deepClone.ts` — Structural, Cycle-Safe Clone

Guaranteed deep clone for:

- Arrays & objects  
- Nested graph fragments  
- Story Node narrative structures  
- GeoJSON objects  
- Metadata-bearing objects (`__meta`, `provenance`, etc.)

Features:

- Cycle detection and safe cloning  
- Retains governance metadata (`careLabel`, `sovereignty`, `license`, `source`)  
- Does NOT attempt to interpret or rewrite fields (no semantic guessing)  

---

### ⚖️ `equals.ts` — Deep Equality

Used heavily for:

- Memo caches  
- Story Node diffing and delta detection  
- Focus Mode v3 semantic window comparisons  
- Map layer re-render pruning (compare config objects)  

Supports:

- Primitives & primitive unions  
- Arrays & objects  
- GeoJSON objects  
- Governance metadata comparison  

Guarantees:

- Deterministic equality semantics  
- No reliance on object identity or reference equality alone  

---

### ❗ `invariant.ts` — Invariant Enforcement

Runtime assertion helper, used for:

- Enforcing preconditions in pipelines  
- Early failure in unexpected states  
- Making MCP-style error messages (clear, actionable)  

Example:

```ts
invariant(typeof id === "string", "Expected string id in entity resolver");
```

Failure behavior:

- Throws typed error suitable for logging + telemetry  
- Should never leak sensitive details in messages  

---

### 🕳️ `isEmpty.ts` — Robust Emptiness Detection

Determines “emptiness” for:

- Arrays (`[]`)  
- Objects (`{}` without own enumerable props)  
- Sets/Maps  
- Null/undefined  
- String variants (configurable)  
- GeoJSON geometries (e.g., empty MultiPolygons)  

Used by:

- API preflight validation  
- Timeline & Focus Mode data guards  
- Graph adapters checking for “no data” conditions  

---

### 🧾 `typeGuards.ts` — Strong TypeScript Guards

Provides runtime type guards:

- `isString`, `isNumber`, `isBoolean`  
- `isArray`, `isObject`, `isPlainObject`  
- `isDate`  
- `isGeoJSONGeometry`  

Used by:

- API & graph response validators  
- utils in `graph`, `bbox`, `temporal`  
- defensive checks in Focus/Story pipelines  

Guarantees:

- Tight TypeScript narrowing for safer code paths  
- Consistent semantics across the entire web codebase  

---

### 🔀 `objectMerge.ts` — FAIR+CARE–Aware Merge

Deterministic, deep merge function for configuration and data objects.

Features:

- No silent discarding of metadata fields  
- Configurable precedence (e.g., `source` vs `target`)  
- Special handling for governance keys (`careLabel`, `sensitivity`, `sovereignty`)  
- Compatible with:
  - Story Node property merge  
  - Map layer style merges  
  - Timeline config merges  
  - STAC/DCAT-derived configs  

Guarantees:

- No invented fields  
- No silent masking override  
- Deterministic output  

---

## 🔐 5. Governance & FAIR+CARE Behavior

These general utilities sit **upstream** of more specialized governance layers (e.g., `bbox.ts`, `graph/`, `url.ts`). They **must not**:

- Strip or corrupt governance metadata  
- Invent missing CARE labels or sovereignty values  
- Sharpen masked/generalized values into more precise ones  

They **should**:

- Provide a solid base for more domain-specific enforcement (graph, spatial, temporal)  
- Support easy composition into Story Node v3 and Focus Mode v3 logic  

---

## ♿ 6. Accessibility Expectations

Although these utilities do not emit UI themselves, they:

- May be used by A11y-related utilities (`a11y.ts`)  
- Must not impede accessible flows (e.g., by randomizing order or hiding required metadata)  
- Must remain predictable so ARIA- and order-dependent components behave consistently  

---

## 📈 7. Telemetry Interaction

While general utilities do not emit telemetry directly, they:

- Influence telemetry quality (e.g., via stable equality and memoization behavior)  
- Must not introduce non-determinism in telemetry flows  
- Are expected to support consistent hashing, diffing, and grouping semantics upstream  

Telemetry schemas referenced in `telemetry_schema` capture error categories and governance metrics impacted by general utils indirectly.

---

## 🧪 8. Testing Requirements

All utilities MUST be tested under:

~~~text
tests/unit/web/utils/general/**
tests/integration/web/utils/general/**
~~~

Tests must verify:

- Deterministic behavior across repeated calls  
- Structural cloning corner cases (including cycles)  
- Equality semantics for complex graphs & GeoJSON  
- Metadata retention (FAIR+CARE fields) in deepClone/objectMerge  
- Correct assertion behavior (`invariant`)  
- Guard correctness in `typeGuards.ts`  

CI will block merges that reduce coverage or violate these invariants.

---

## 🕰 9. Version History

| Version | Date       | Notes                                                                                             |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; emoji-rich directory; enhanced governance/A11y/test expectations.    |
| v10.4.1 | 2025-11-15 | Initial v10.4 file creation using KFM-MDP v10.4 standards.                                        |
| v10.3.2 | 2025-11-14 | Added general-purpose structural utilities; stabilized behaviors.                                  |
| v10.3.1 | 2025-11-13 | Initial general utilities overview for early web platform.                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../../README.md) · [🌐 Web Platform Overview](../../../README.md) · [🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>