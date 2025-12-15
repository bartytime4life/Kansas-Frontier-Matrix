---
title: "🧾 Kansas Frontier Matrix — Web Types Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/types/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"
review_cycle: "Quarterly · FAIR+CARE Council & Web Architecture Board"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-types-readme-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-types-overview"
role: "type-system"
category: "Web · Types · Architecture"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (unless typing redacted CARE fields)"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/types/README.md@v11.2.2"
  - "web/src/types/README.md@v10.4.0"
  - "web/src/types/README.md@v10.3.2"
provenance_requirements:
  versions_required: true
  newest_first: true

ontology_alignment:
  cidoc: "E28 Conceptual Object"
  schema_org: "DefinedTerm"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"

json_schema_ref: "../../../schemas/json/web-types-readme.schema.json"
shape_schema_ref: "../../../schemas/shacl/web-types-readme-shape.ttl"

doc_uuid: "urn:kfm:doc:web-types-readme:v11.2.6"
semantic_document_id: "kfm-doc-web-types-readme"
event_source_id: "ledger:web/src/types/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative typing"
  - "synthetic type inference"
  - "unverified historical claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next type-system revision"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Web Types Overview (v11)**  
`web/src/types/README.md`

**Purpose**  
Define the **governed TypeScript type surface** for the Kansas Frontier Matrix Web Platform  
(`web/src/types/**`). Types enforce **deterministic, schema-aligned, FAIR+CARE-safe** modeling of:

- UI ↔ API DTOs (REST / GraphQL / JSON-LD)
- Focus Mode payloads and explainability envelopes
- Story Node v3 narrative + spatial/temporal bundles
- STAC / DCAT catalog artifacts
- Governance overlays (CARE, sovereignty, redaction/masking)
- Telemetry events (non-PII; schema-validated)

</div>

---

## 📘 Overview

`web/src/types/**` is the **single, shared type contract** for the entire frontend. It exists to prevent:
- schema drift (backend vs. UI expectations),
- accidental leakage of sensitive governed fields,
- non-deterministic rendering behavior caused by loose typing.

### Core invariants

- **No direct graph typing**: the web models only **API surfaces**, not Neo4j internals.
- **No `any` on external payloads**: inbound data is treated as `unknown` until validated.
- **DTOs are not domain objects**: DTOs mirror API shapes; domain types represent UI-safe normalized forms.
- **Governance metadata is first-class**: “redaction/masking/CARE/sovereignty” is not a footnote—types must carry it.
- **Determinism**: given identical responses, the UI must render the same results (no speculative enrichment).

### Where these types are consumed

- `web/src/services/**` — API clients and adapters (typed input/output)
- `web/src/hooks/**` and `web/src/pipelines/**` — orchestration and state machines
- `web/src/context/**` — shared state contracts
- `web/src/components/**` — component props + render-safe domain models
- `web/src/utils/**` — guards and normalizers that convert DTO → domain models

### Source-of-truth references

- JSON Schemas and telemetry schemas under `schemas/**` are authoritative for shape validation.
- Validators and contract checks under `tools/validation/**` are authoritative for schema conformance.

---

## 🗂️ Directory Layout

This directory is intentionally small and stable. New modules must be justified by:
- an upstream schema contract (JSON Schema / telemetry schema / API change), and
- a clear ownership boundary (DTO vs domain vs UI state).

~~~text
web/src/types/
├── 🌐 api.ts          # API-layer DTOs (REST/GraphQL/JSON-LD/STAC/DCAT responses)
├── 🧬 domain.ts       # UI-safe domain entities (normalized, render-ready)
├── 🛡 governance.ts   # CARE/sovereignty/redaction/provenance envelopes
├── 🌍 spatial.ts      # GeoJSON/BBox/H3/CRS primitives + governed spatial wrappers
├── ⏳ temporal.ts     # OWL-Time-aligned temporal primitives + fuzzy/approx intervals
├── 🖥 ui.ts           # UI state types (panels, layouts, A11y flags, interaction contracts)
├── 📈 telemetry.ts    # Non-PII telemetry event + attribute shapes (schema-derived)
├── 🎯 focus.ts        # Focus Mode payloads (targets, context windows, evidence refs)
├── 📖 story.ts        # Story Node v3 structures (narrative + time + space + provenance)
├── 📦 stac.ts         # STAC v1.x Collection/Item/Asset/Link subsets used by UI
├── 🗂 dcat.ts         # DCAT v3 Dataset/Distribution/Catalog subsets used by UI
└── 🔗 index.ts        # Barrel exports (the only stable import surface for app code)
~~~

**Import rule (enforced by review):** app code should import from `web/src/types` (via `index.ts`) rather than deep-linking into individual files, except within this directory.

---

## 🧱 Architecture

### Layer boundary: DTO → Domain → UI

The type system is intentionally layered:

~~~mermaid
flowchart LR
  DTO["API DTOs (api.ts, stac.ts, dcat.ts)"] --> NORM["Normalize + Validate (utils/guards + adapters)"]
  NORM --> DOM["Domain Models (domain.ts, story.ts, focus.ts)"]
  DOM --> UI["UI Contracts (ui.ts, component props, contexts)"]
  GOV["Governance Envelope (governance.ts)"] --> DTO
  GOV --> DOM
  GOV --> UI
~~~

### DTO principles (`api.ts`, `stac.ts`, `dcat.ts`)

- DTOs mirror the backend **exactly**.
- DTOs may contain:
  - `null` / redacted values,
  - optional fields,
  - versioned payload envelopes.
- DTOs must be treated as `unknown` at the boundary and promoted to typed DTOs only via validation.

**Recommended naming convention**
- `Api*` prefixes for DTOs: `ApiStoryNodeResponse`, `ApiFocusSummary`, etc.
- `Dcat*` and `Stac*` prefixes for catalog types.

### Domain principles (`domain.ts`, `focus.ts`, `story.ts`)

Domain models are:
- render-safe (no raw HTML injection shapes),
- normalized (IDs and label fields are predictable),
- governance-aware (domain objects carry “what is allowed to show”).

Domain types should:
- preserve stable IDs (URNs/UUIDs) unchanged,
- avoid embedding transport details (pagination metadata, HTTP status, etc.).

### Governance envelope (`governance.ts`)

Governance types define the “UI visibility contract”:
- CARE labels and license/rights hints
- sovereignty and heritage flags
- masking/redaction indicators (including geometry generalization)
- provenance hooks (PROV-aligned structures and references)

**Rule:** if a feature, dataset, story node, or focus narrative is governed, its type must include governance metadata (or explicitly model its absence).

### Spatial (`spatial.ts`)

Spatial types must support:
- GeoJSON geometry and Feature/FeatureCollection
- bounding boxes and spatial extents
- coordinate reference descriptors (when exposed)
- **masking/generalization** signals for protected places

**Governance-friendly spatial modeling**
- Represent “redacted geometry” explicitly (e.g., generalized geometry + masking reason) rather than silently dropping geometry.

### Temporal (`temporal.ts`)

Temporal types must support:
- OWL-Time aligned intervals/instants
- fuzzy/approximate ranges (precision metadata)
- story-node and catalog temporal coverage

**Rule:** never silently coerce fuzzy ranges into precise instants.

### Telemetry (`telemetry.ts`)

Telemetry types must:
- match the telemetry schemas under `schemas/telemetry/**`,
- be non-PII by construction,
- encode event names and attribute keys as constrained unions.

**Event taxonomy (typical)**
- `ui:*`, `map:*`, `timeline:*`, `story:*`, `focus:*`, `stac:*`, `dcat:*`
- error classes (typed): rendering, schema validation, governance denial, network failures

### Barrel export (`index.ts`)

`index.ts` is the **public type API** for the web codebase.
- Keep exports intentional.
- Avoid re-exporting types that are internal-only or experimental.

---

## 🌐 STAC, DCAT & PROV Alignment

Types in this folder must support KFM’s catalog and provenance strategy:

- **STAC** (`stac.ts`) represents UI-consumed subsets of STAC Collections/Items/Assets.
- **DCAT** (`dcat.ts`) represents UI-consumed subsets of DCAT Dataset/Distribution/Catalog views.
- **PROV** alignment is expressed through governance/provenance envelopes and reference IDs (not raw RDF graphs in the UI).

### Practical alignment rules for the type system

- Keep catalog types **structurally compatible** with schema validators in `tools/validation/**`.
- Maintain **lossless references**:
  - dataset IDs, item IDs, distribution IDs,
  - provenance IDs and source references,
  - time coverage and spatial extents.

### UI-safe catalog previews

Types must allow catalog previews to be:
- license-aware,
- provenance-linked,
- masking-aware (sensitive tiles/geometries generalized and flagged),
- stable for caching and deterministic rendering.

---

## ⚖ FAIR+CARE & Governance

Types are part of governance enforcement:

- If the backend signals **masking/redaction**, types must provide a place to carry:
  - what was masked,
  - why it was masked,
  - what level of generalization is permitted.

### AI behavior constraints reflected in typing

Frontend types must not enable:
- speculative additions to narratives,
- client-side “invented” provenance,
- governance overrides via UI state.

AI-related payload shapes should:
- distinguish archival/curated text vs. AI-generated segments,
- link AI segments to evidence references and governance context,
- carry flags needed for “Why am I seeing this?” UX affordances.

**All governance display/behavior must remain consistent with:**
- `../../../docs/standards/governance/ROOT-GOVERNANCE.md`
- `../../../docs/standards/faircare/FAIRCARE-GUIDE.md`
- `../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🧪 Validation & CI/CD

Types are validated in CI through a combination of compile-time and runtime checks.

### Required checks

- **TypeScript strict** compilation must pass (no ignored errors).
- **Runtime guards** must exist for any external payload shape used by the UI.
- **Telemetry event types** must conform to telemetry schemas (`telemetry_schema`, energy/carbon schemas).
- **Schema drift prevention**:
  - when upstream JSON Schemas change, DTOs and guards must be updated together.

### Change checklist (when modifying types)

1. Update DTO types (and any adapters) for the changed API shape.
2. Update guards/normalizers that promote `unknown` → typed DTO/domain.
3. Update dependent services/hooks/pipelines.
4. Update telemetry types if event shapes changed.
5. Add/adjust tests (type-level and runtime guard coverage).

**Note:** script names vary by workspace; reference `web/package.json` for the exact typecheck/lint/test commands used in CI.

---

## 🕰️ Version History

| Version  | Date       | Summary |
|---------:|------------|---------|
| v11.2.6  | 2025-12-15 | Aligned to KFM-MDP v11.2.6 (approved H2 registry + required section order); added missing ethics/sovereignty refs; clarified DTO→Domain→UI boundaries; strengthened governance- and validator-linked typing guidance. |
| v11.2.2  | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; emoji directory; added Focus v3, Story v3, STAC/DCAT v11 alignment; strengthened governance typing. |
| v10.4.0  | 2025-11-15 | KFM-MDP v10.4.1 types overview; labeled modules; governance-aligned typing rules. |
| v10.3.2  | 2025-11-14 | Added STAC/DCAT + Focus Mode v2.5 types. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  

[⬅️ Back to Web Source Overview](../README.md) · [🧱 Web Source Architecture](../ARCHITECTURE.md) · [🌐 Web Platform Overview](../../README.md) · [🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>