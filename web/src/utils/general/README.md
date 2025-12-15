---
title: "🧭 Kansas Frontier Matrix — General Utilities Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/general/README.md"
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
system_telemetry_ref: "<optional-if-published: ../../../../releases/v11.2.2/system-telemetry.json>"
telemetry_schema: "../../../../schemas/telemetry/web-utils-general-v11.json"

signature_ref: "<optional-if-published: ../../../../releases/v11.2.2/signature.sig>"
attestation_ref: "<optional-if-published: ../../../../releases/v11.2.2/slsa-attestation.json>"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

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
  - "web/src/utils/general/README.md@v11.2.2"
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

doc_uuid: "urn:kfm:doc:web-utils-general-readme:v11.2.3"
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

# 🧭 **Kansas Frontier Matrix — General Utilities Overview (v11.2.3)**
`web/src/utils/general/README.md`

**Purpose**  
Provide a unified reference and architectural description for **general-purpose helper utilities** used across the KFM Web Platform (React + MapLibre + Timeline + Focus Mode).  
These utilities are **pure, deterministic, MCP-compliant, FAIR+CARE-safe**, and reused across all major UI subsystems including:  
– Timeline engine  
– Focus Mode v3  
– Story Node v3 rendering  
– Graph & API adapters  
– Map rendering layers  
– STAC/DCAT explorers  

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

The `general` utilities comprise the lowest-level foundation for KFM frontend logic.

They provide:

- 🧠 Deterministic memoization
- 📦 Deep structural cloning (cycle-safe)
- 🧮 Robust equality checking
- 🧹 Value normalization & emptiness detection
- 🛡️ Type guards & invariants
- 🔗 FAIR+CARE-aware merge functions

Core rules:

- No side effects (no global mutation, no I/O, no DOM)
- No dependencies on React, browser APIs, or MapLibre/Cesium
- No speculative behavior (no invented data, no guessed semantics)
- All outputs must be safe to pass into higher-level utilities (`api`, `bbox`, `temporal`, `graph`, etc.)

They are required by:

- `web/src/utils/api`
- `web/src/utils/temporal`
- `web/src/utils/graph`
- `web/src/utils/bbox`
- Focus Mode v3 narrative assembly layers
- Timeline event bucketing, deduplication & grouping
- Story Node v3 field normalization & diffing

---

## 🗂️ Directory Layout

Directory layouts follow the KFM-MDP v11.2.6 box-safe tree format.

~~~text
web/src/utils/general/
├── 📄 memo.ts           — 🧠 Deterministic + TTL-aware memoization utilities
├── 📄 deepClone.ts      — 🧬 Cycle-safe, metadata-preserving deep cloning
├── 📄 equals.ts         — ⚖️ Deep equality comparisons for value graphs
├── 📄 invariant.ts      — ❗ Runtime assertions & invariants (MCP-style errors)
├── 📄 isEmpty.ts        — 🕳️ Robust emptiness checks (arrays, objects, sets, maps, GeoJSON)
├── 📄 typeGuards.ts     — 🧾 Strong runtime type guards for TypeScript narrowing
└── 📄 objectMerge.ts    — 🔀 FAIR+CARE-aware deterministic deep merge
~~~

These general utilities are deliberately small, sharp, and zero-UI.

---

## 🧭 Context

These utilities sit upstream of all other frontend logic layers.

Typical dependency direction (conceptual):

- `utils/general/*` → supports `utils/api/*`, `utils/temporal/*`, `utils/geo/*`, `utils/provenance/*`
- those layers → support services/hooks
- services/hooks → support UI components

Upstream responsibility:

- provide predictable ordering, comparison, cloning, merging, and guard semantics
- avoid introducing non-determinism that would destabilize:
  - timeline grouping and sorting
  - Focus Mode windowing/cache behavior
  - map layer configuration merging
  - Story Node v3 diffing and rendering behavior

### Accessibility expectations

General utilities do not render UI, but they must not undermine accessible flows:

- do not randomize ordering that screen-reader and keyboard navigation depends on
- do not silently strip fields required for accessible labeling downstream
- keep deterministic behavior so focus/ARIA-dependent components behave consistently

### Telemetry interaction

General utilities should not emit telemetry directly. However, they influence telemetry quality by:

- enabling stable hashing and memo semantics (reduces noisy event duplication)
- ensuring deterministic equality semantics (prevents flicker/re-render loops)
- producing stable grouping/sorting (improves “same action” aggregation)

If a utility is added that outputs any telemetry-adjacent structure, it must conform to `telemetry_schema` referenced in front-matter.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  GEN["utils/general/*\n(memo, clone, equals, guards, merge)"] --> API["utils/api/*"]
  GEN --> TEMP["utils/temporal/*"]
  GEN --> GEO["utils/geo/* (bbox, masking helpers)"]
  API --> SVC["services/hooks"]
  TEMP --> SVC
  GEO --> SVC
  SVC --> UI["UI components\n(Timeline, Focus Mode, Story Nodes, Maps)"]
~~~

---

## 📦 Data & Metadata

These utilities must preserve the meaning and governance context of objects they handle.

Minimum expectations:

- no silent deletion of provenance or CARE metadata
- no silent overwrite of sensitive flags (for example: `sensitivity`, `sovereignty`, `careLabel`, `license`, `rights`)
- deep cloning and merging must retain metadata blocks (for example: `__meta`, `provenance`) unless explicitly configured

Recommended patterns for metadata-safe operations:

- treat metadata keys as first-class fields (clone/merge them like any other key)
- when merging, do not “upgrade” or “downgrade” governance labels by default
- prefer explicit merge policy options (if supported) over implicit precedence

---

## 🌐 STAC, DCAT & PROV Alignment

General utilities are schema-agnostic, but they must not break STAC/DCAT/PROV objects.

Guidelines:

- `deepClone.ts` must preserve JSON-LD keys and contexts (for example: `@context`, `@id`, `@type`) as plain fields
- `equals.ts` must treat STAC/DCAT/PROV objects deterministically (no special-case guessing)
- `objectMerge.ts` must not discard distribution/license/provenance fields in DCAT objects
- stable sorting/grouping helpers must not reorder objects in ways that imply meaning changes (sorting should be explicit and documented)

Practical examples where this matters:

- STAC `assets` dictionaries are often consumed by UI layers; do not rewrite keys
- DCAT dataset/distribution fields should remain intact for licensing and reuse
- PROV-like fields (`wasDerivedFrom`, run IDs, agent refs) must not be stripped or “simplified away”

---

## 🧱 Architecture

### Deterministic behavior (MCP rule alignment)

- no usage of `Date.now`, `Math.random`, or other non-deterministic APIs
- same input → same output across runs, CI nodes, and environments
- pure functions only (no side effects, no shared mutable state)

### FAIR+CARE safety

- no silent deletion of provenance or CARE metadata
- no silent overwrites of sensitive flags
- deep clone & merge functions must retain governance blocks unless explicitly configured

### Cross-pipeline consistency

Results from these functions must behave identically across:

- GraphQL + REST responses
- timeline engine sort/group operations
- Story Node v3 normalization (CIDOC/OWL-Time alignment)
- MapLibre layer configuration merging
- Focus Mode v3 state merges

### Zero React / browser imports

- no React
- no DOM or `window` usage
- no MapLibre/Cesium imports

Modules in this directory must be safe to reuse in Node, browser, tests, and tools.

### Module details

#### `memo.ts` — deterministic memoization

Provides argument-hash–based memoization with optional TTL.

Used by:

- Focus Mode v3 summarization caching
- graph → map layer transformation caching
- timeline quantization & bucketing helpers

Features:

- stable argument hashing (for example: deterministic JSON-safe hashing)
- optional TTL expiry for caches
- orphan cleanup: discard unused entries over time
- compatible with unit tests and SSR

#### `deepClone.ts` — structural, cycle-safe clone

Guaranteed deep clone for:

- arrays and objects
- nested graph fragments
- Story Node narrative structures
- GeoJSON objects
- metadata-bearing objects (`__meta`, `provenance`, etc.)

Features:

- cycle detection and safe cloning
- retains governance metadata (`careLabel`, `sovereignty`, `license`, `source`)
- does not interpret or rewrite fields (no semantic guessing)

#### `equals.ts` — deep equality

Used heavily for:

- memo caches
- Story Node diffing and delta detection
- Focus Mode v3 semantic window comparisons
- map layer re-render pruning (compare config objects)

Supports:

- primitives and primitive unions
- arrays and objects
- GeoJSON objects
- governance metadata comparison

Guarantees:

- deterministic equality semantics
- no reliance on object identity alone

#### `invariant.ts` — invariant enforcement

Runtime assertion helper, used for:

- enforcing preconditions in pipelines
- early failure in unexpected states
- MCP-style error messages (clear, actionable)

Example:

~~~ts
invariant(typeof id === "string", "Expected string id in entity resolver");
~~~

Failure behavior:

- throws typed error suitable for logging + telemetry
- must never leak sensitive details in error messages

#### `isEmpty.ts` — robust emptiness detection

Determines “emptiness” for:

- arrays (`[]`)
- objects (`{}` without own enumerable props)
- sets/maps
- null/undefined
- string variants (configurable)
- GeoJSON geometries (for example: empty MultiPolygons)

Used by:

- API preflight validation
- timeline and Focus Mode data guards
- graph adapters checking for “no data” conditions

#### `typeGuards.ts` — strong runtime guards

Provides runtime type guards:

- `isString`, `isNumber`, `isBoolean`
- `isArray`, `isObject`, `isPlainObject`
- `isDate`
- `isGeoJSONGeometry`

Used by:

- API and graph response validators
- utils in `graph`, `bbox`, `temporal`
- defensive checks in Focus/Story pipelines

Guarantees:

- tight TypeScript narrowing for safer code paths
- consistent semantics across the web codebase

#### `objectMerge.ts` — FAIR+CARE-aware merge

Deterministic deep merge function for configuration and data objects.

Features:

- no silent discarding of metadata fields
- configurable precedence (for example: `source` vs `target`)
- special handling for governance keys (`careLabel`, `sensitivity`, `sovereignty`)
- compatible with:
  - Story Node property merge
  - map layer style merges
  - timeline config merges
  - STAC/DCAT-derived configs

Guarantees:

- no invented fields
- no silent masking override
- deterministic output

---

## 🧠 Story Node & Focus Mode Integration

These utilities support narrative-facing systems indirectly by making the underlying logic stable and safe.

Common integration points:

- Story Node v3:
  - diffing and “changed fields” detection (`equals.ts`)
  - safe copying of narrative structures (`deepClone.ts`)
  - guard rails for expected shapes (`typeGuards.ts`, `invariant.ts`)
  - stable ordering for event lists (via downstream consumers)

- Focus Mode v3:
  - deterministic caching/memoization (`memo.ts`)
  - state merge correctness (`objectMerge.ts`)
  - “no data” detection for safe fallbacks (`isEmpty.ts`)

Narrative safety support:

- stable transforms reduce accidental “meaning drift”
- metadata retention prevents loss of evidence/provenance indicators required by governed UI surfaces

---

## ⚖ FAIR+CARE & Governance

These general utilities sit upstream of more specialized governance layers (for example: `bbox`, `url`, `api`).
They must not:

- strip or corrupt governance metadata
- invent missing CARE labels or sovereignty values
- sharpen masked/generalized values into more precise ones

They should:

- provide a solid base for domain-specific enforcement (graph, spatial, temporal)
- support safe composition into Story Node v3 and Focus Mode v3 logic
- keep governance fields stable under clone/merge and never silently “normalize away” stewardship context

---

## 🧪 Validation & CI/CD

All utilities must have test coverage under:

~~~text
tests/unit/web/utils/general/**
tests/integration/web/utils/general/**
~~~

Tests must verify:

- deterministic behavior across repeated calls
- structural cloning corner cases (including cycles)
- equality semantics for complex graphs and GeoJSON
- metadata retention (FAIR+CARE fields) in `deepClone.ts` and `objectMerge.ts`
- correct assertion behavior (`invariant.ts`)
- guard correctness and narrowing expectations in `typeGuards.ts`

CI policy:

- merges are blocked if changes introduce non-determinism, reduce coverage materially, or cause governance metadata loss
- any governance-sensitive change must include tests that assert “no leakage / no stripping” behavior

---

## 🕰️ Version History

| Version | Date | Notes |
|---:|---:|---|
| v11.2.3 | 2025-12-15 | Reformatted to KFM-MDP v11.2.6 (approved H2 registry + ordering, box-safe directory tree, inner `~~~` fences); preserved all v11.2.2 content and clarified governance/telemetry context. |
| v11.2.2 | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; emoji-rich directory; enhanced governance/A11y/test expectations. |
| v10.4.1 | 2025-11-15 | Initial v10.4 file creation using KFM-MDP v10.4 standards. |
| v10.3.2 | 2025-11-14 | Added general-purpose structural utilities; stabilized behaviors. |
| v10.3.1 | 2025-11-13 | Initial general utilities overview for early web platform. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned

[⬅️ Back to Web Utils](../README.md) ·
[🧭 Web Source Overview](../../README.md) ·
[🌐 Web Platform Overview](../../../README.md) ·
[🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
