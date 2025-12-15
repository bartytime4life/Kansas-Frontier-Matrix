---
title: "🧰 Kansas Frontier Matrix — Web Utilities Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/utils/README.md"
version: "v11.2.3"
last_updated: "2025-12-15"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-utils-overview"
role: "overview"
category: "Web · Utilities · Architecture"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../releases/v11.2.2/system-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/system-telemetry-v11.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/utils/README.md@v11.2.2"
  - "web/src/utils/README.md@v10.4.0"
  - "web/src/utils/README.md@v10.3.2"
  - "web/src/utils/README.md@v10.3.1"
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

doc_uuid: "urn:kfm:doc:web-utils-readme:v11.2.3"
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

# 🧰 **Kansas Frontier Matrix — Web Utilities Overview (v11.2.3)**
`web/src/utils/README.md`

**Purpose**
Describe the **web utility layer** for the Kansas Frontier Matrix (KFM): small, deterministic functions and type guards used across the web app to keep Focus Mode, maps, timelines, and dataset views **governance-safe**, **accessible**, and **reproducible**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Public%20Low--Risk-orange" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

Utilities under `web/src/utils/` exist to make the web layer:

- **Deterministic**: same input → same output; stable ordering; no hidden state
- **Side-effect-free**: no network, no storage, no DOM writes, no logging by default
- **Governance-safe**: never reconstruct restricted precision (coords/IDs); honor CARE labels
- **A11y-forward**: help components meet WCAG 2.1 AA+ consistently
- **Contract-aware**: validate and normalize payloads before rendering (Story Node v3, Focus Mode v3, STAC/DCAT views, telemetry events)

Utilities are used by hooks, services, and components to prevent a common failure mode:
“UI renders something that violates governance or breaks accessibility because input data was malformed or over-precise.”

---

## 🗂️ Directory Layout

The directory trees below are the **governed taxonomy** for `web/src/utils/`.
If the actual tree differs, treat this README as the canonical contract and update it alongside the change.

### Recommended grouping (scales well)

~~~text
web/src/utils/
├── 📄 formatters.ts                   # ✨ Numbers, units, dates, captions (CARE-aware)
├── 📄 guards.ts                       # 🛡️ Runtime guards for payloads (Story Node, STAC, DCAT, telemetry)
├── 📄 jsonld.ts                       # 🧬 JSON-LD builders for doc/dataset/narrative linking
├── 📄 provenance.ts                   # 🧾 PROV-O helpers + manifest/SBOM linkage
│
├── 📁 a11y/                            # ♿ Accessibility helpers
│   ├── 📄 a11y.ts                      # Focus management, SR helpers, reduced motion
│   └── 📄 contrast.ts                  # WCAG contrast helpers (and test helpers)
│
├── 📁 geo/                             # 🗺️ Spatial math and safety utilities
│   ├── 📄 bbox.ts                      # BBox merge/pad/clamp + safe extents
│   └── 📄 h3.ts                        # H3 masking/generalization helpers (optional)
│
├── 📁 links/                           # 🔗 URL + deep-link helpers
│   └── 📄 url.ts                       # Governance-safe query encoding (no restricted precision)
│
├── 📁 temporal/                        # ⏳ Time utilities
│   └── 📄 temporal.ts                  # OWL-Time aligned ranges + timeline mapping
│
├── 📁 theme/                           # 🎨 Color and token helpers
│   └── 📄 color.ts                     # Contrast-aware color utilities + CARE status colors
│
└── 📁 collections/                     # 🔢 Deterministic collection helpers
    └── 📄 array.ts                     # Unique, groupBy, stableSort (no locale drift)
~~~

### Minimal “flat” layout (acceptable for small surfaces)

~~~text
web/src/utils/
├── 📄 formatters.ts                   # ✨ Formatting helpers
├── 📄 jsonld.ts                       # 🧬 JSON-LD helpers
├── 📄 guards.ts                       # 🛡️ Runtime guards
├── 📄 bbox.ts                         # 🗺️ Spatial helpers
├── 📄 a11y.ts                         # ♿ A11y helpers
├── 📄 provenance.ts                   # 🧾 Provenance helpers
├── 📄 url.ts                          # 🔗 URL helpers (governance-safe)
├── 📄 color.ts                        # 🎨 Theme/contrast helpers
├── 📄 temporal.ts                     # ⏳ Time helpers
└── 📄 array.ts                        # 🔢 Deterministic array helpers
~~~

### Naming conventions (recommended)

- `guards.ts` is for runtime validation and type predicates (not “domain logic”)
- Avoid `helpers.ts` / `misc.ts` (too vague → becomes a junk drawer)
- Prefer `stableSort*` over `sort*` when the stability guarantee matters
- Prefer `format*` for user-visible strings, and `to*` / `from*` for structural transforms

---

## 🧭 Context

Where these utilities sit in the web stack (conceptual):

- **API layer** returns data (graph → API → web)
- `web/src/services/**` fetches and parses
- `web/src/utils/**` validates/normalizes/encodes safely
- UI components render only **post-guard** data

Common call paths:

- **Story Nodes / Focus Mode**: guards → formatters → provenance/jsonld → UI
- **Map**: bbox/geo safety → url deep-link encoding → UI
- **Timeline**: temporal mapping → formatters → stable sorting/grouping → UI

---

## 🗺️ Diagrams

This diagram shows a typical safe rendering flow that prevents governance and A11y regressions.

~~~mermaid
flowchart LR
  A["API response"] --> B["services parse"]
  B --> C["utils guards + normalization"]
  C --> D["formatters + a11y helpers"]
  D --> E["components render"]
~~~

---

## 🧱 Architecture

### Design rules (non-negotiable)

1. **No side effects**
   - No `fetch`, no `localStorage`, no `window` mutation, no DOM writes, no analytics calls.

2. **Deterministic output**
   - Avoid locale-sensitive formatting unless explicitly parameterized.
   - Prefer stable ordering utilities for lists that feed UI diffing or accessibility flows.

3. **Governance-safe by construction**
   - Do not generate URLs or strings that expose restricted precision (micro-coordinates, sensitive IDs).
   - Utilities must support masking/generalization and must not “undo” it.

4. **Boundary-friendly**
   - Utilities should accept primitives and plain objects, return primitives/plain objects.
   - Avoid importing UI-only code, components, or styles.

### Module map (what goes where)

- `guards.ts`: schema/type guards for inbound and inter-layer payloads
- `formatters.ts`: user-visible strings (dates, ranges, units, labels)
- `geo/*`: bbox math, safe extents, (optional) H3 generalization helpers
- `temporal/*`: timeline range normalization, OWL-Time aligned intervals
- `a11y/*`: focus and reduced-motion helpers; contrast math
- `provenance.ts` + `jsonld.ts`: linking evidence and lineage into UI-friendly forms
- `url.ts`: deep links and query encoding with governance guardrails
- `array.ts`: stable collection transforms used across views

---

## 📦 Data & Metadata

### Runtime validation and “defensive rendering”

Utilities should make it easy to do:

- “Reject invalid payload early” (fail fast before it reaches UI)
- “Normalize on ingest” (e.g., empty arrays → empty arrays, optional fields → defaults)
- “Never infer precision” (do not create coordinates, timestamps, or IDs that weren’t present)

### Suggested type surfaces (optional, if not provided elsewhere)

If the project does not centralize types in another directory, `web/src/utils/types/` can host thin types for:

- STAC views (`stac.ts`)
- DCAT views (`dcat.ts`)
- Story Node v3 (`story_node.ts`)
- Telemetry events (`telemetry.ts`)
- Focus Mode payload contracts (`focus_mode.ts`)

---

## 🌐 STAC, DCAT & PROV Alignment

Utilities may be used to:

- Map STAC/GeoJSON geometry and bbox into safe UI extents (never increasing precision)
- Produce DCAT-style identifiers and distribution references for “dataset-like” UI entities
- Build PROV-O-friendly traces for “what evidence produced this view” via:
  - `prov:used` (inputs)
  - `prov:wasGeneratedBy` (activity)
  - `prov:wasDerivedFrom` (lineage)

Practical guidance:

- Treat README/docs as `prov:Plan`-adjacent metadata surfaces (via front-matter IDs)
- Keep JSON-LD generation deterministic and minimal (avoid speculative relationship generation)

---

## 🧠 Story Node & Focus Mode Integration

Utilities directly support Focus Mode’s “safe transform” posture:

- Stable sectioning + deterministic formatting makes summarization predictable
- `ai_transform_permissions` / `ai_transform_prohibited` in front-matter constrain automation
- Provenance utilities ensure “why/where did this come from” is renderable without leaking restricted detail

Focus Mode-safe patterns:

- Prefer “generalized location” language when sovereignty policy requires masking
- Provide provenance links to manifests/SBOM instead of repeating sensitive identifiers in UI

---

## 🧪 Validation & CI/CD

Utilities must be easy to validate and hard to misuse.

### Required checks (typical)

- Unit tests for:
  - stable sorting/grouping
  - bbox clamping and safe extents
  - temporal conversions and labeling
  - URL encoding constraints (no restricted precision)
  - contrast computations / WCAG thresholds
- Type-level checks (TS) for public utility APIs
- Schema-lint for this README front-matter (`metadata-check` / `schema-lint`)

### Test placement (preferred)

~~~text
tests/
├── unit/
│   └── web/
│       └── utils/                    # Pure unit tests for utils
└── integration/
    └── web/
        └── utils/                    # Integration tests with service parsing / key views
~~~

---

## ⚖ FAIR+CARE & Governance

Utilities must enforce “least harm by default”:

- Never expose secrets, tokens, or internal-only IDs in generated strings/URLs
- Never reconstruct restricted locations or increase coordinate precision
- Support CARE labeling and sovereignty policy enforcement in UI-facing transforms
- Prefer explicit “restricted” states over silent failure

If a utility function affects governance-sensitive output, it must:

- be covered by a test that asserts masking/generalization behavior
- be reviewed with the relevant governance references in this doc’s front-matter

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-12-15 | Aligned README to KFM-MDP v11.2.6 headings and fencing; clarified governance-safe patterns; expanded directory taxonomy while keeping utils deterministic and side-effect-free. |
| v11.2.2 | 2025-11-28 | Prior baseline referenced by provenance chain. |
| v10.4.0 | 2025-11-15 | Full rewrite to KFM-MDP v10.4; added governance, A11y, spatial, temporal, JSON-LD modules. |
| v10.3.2 | 2025-11-14 | Added temporal + provenance utilities. |
| v10.3.1 | 2025-11-13 | Initial utilities overview. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../README.md) · [🌐 Web Platform Overview](../../README.md) · [🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>