---
title: "👤 Kansas Frontier Matrix — User Feature Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/user/README.md"
version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "web-feature-user-overview"
role: "overview"
category: "Web · Features · User"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/web-features-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-features-readme-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (preferences-only; no PII)"
sensitivity: "General (no PII; no secrets; no sensitive entity content)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public Document"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "web/src/features/user/README.md@v11.2.6"

json_schema_ref: "../../../../schemas/json/web-features-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-features-readme-v11-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:web:features:user:readme:v11.2.6"
semantic_document_id: "kfm-doc-web-features-user-readme-v11"
event_source_id: "ledger:web/src/features/user/README.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon User Feature v12 refactor"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🗺️ Diagrams"
    - "📦 Data & Metadata"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🧪 Validation & CI/CD"
    - "🕰️ Version History"
---

<div align="center">

# 👤 **Kansas Frontier Matrix — User Feature Overview (v11.2.6)**  
`web/src/features/user/README.md`

**Purpose**  
Define the **User feature** inside `web/src/features/user/` — a governed, deterministic layer for  
**user-facing preferences, consent surfaces (where enabled), and non-PII session-local UX state**.  
This feature exists to keep preference logic **auditable, testable, and governance-safe**, while  
integrating cleanly with Contexts (`Theme`, `A11y`, `UI`, `Map`, `Time`) and telemetry controls.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../mcp/MCP-README.md)
· [![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)](../../../../docs/standards/kfm_markdown_protocol_v11.2.6.md)
· [![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-orange)](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md)
· [![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)

</div>

---

## 📘 Overview

The **User feature** is a *frontend-only* capability layer responsible for:

- **Preference orchestration**
  - Theme selection defaults (light/dark/high-contrast) as *presentation* state.
  - Accessibility preferences (reduced motion, font scaling, contrast preferences).
  - UI shell defaults (panels/drawers open state, density toggles) *where governance allows*.

- **Consent + safety toggles (optional, governed)**
  - UX surfaces that let users choose among **pre-approved** privacy/telemetry behaviors.
  - Preferences must never override governance requirements or remove mandated warnings.

- **Session-local UX continuity (non-PII)**
  - “Remember my last view” patterns for map/timeline/navigation *without* creating a stable user identity.

**Non-goals (explicit):**

- Authentication and authorization are **out of scope** unless there is an explicitly governed auth subsystem elsewhere.
- This feature must **not** introduce user identifiers, profiles, emails, names, or other PII.
- This feature must **not** personalize factual content, narratives, or governance classifications.

---

## 🗂️ Directory Layout

The tree below is the **governed target layout** for `web/src/features/user/`.  
If the implementation differs, update this README to reflect the real structure.

~~~text
📁 web/src/features/user/
├── 📄 README.md                              — This document
│
├── 📁 hooks/                                 — React hooks that bind contexts ↔ user prefs (no UI)
│   ├── 📄 useUserPreferences.ts              — Read/write preferences (typed + validated)
│   ├── 📄 useTelemetryConsent.ts             — Consent state binding (if supported)
│   └── 📄 useUserSession.ts                  — Session-local, non-PII UX continuity helpers
│
├── 📁 state/                                 — Reducers/slices/selectors (pure, deterministic)
│   ├── 📄 userState.ts                       — State + actions/events
│   ├── 📄 userSelectors.ts                   — Pure selectors for feature consumers
│   └── 📄 userMigrations.ts                  — Schema migrations for persisted prefs
│
├── 📁 pipelines/                             — Orchestration (load → validate → migrate → apply)
│   ├── 📄 userPreferencesPipeline.ts         — Load/save/migrate preferences
│   └── 📄 userConsentPipeline.ts             — Consent changes → safe propagation
│
├── 📁 storage/                               — Storage adapters (no governance bypass)
│   ├── 📄 storageAdapter.ts                  — Adapter interface (localStorage/memory)
│   ├── 📄 localStorageAdapter.ts             — Default browser adapter
│   └── 📄 memoryAdapter.ts                   — Test/SSR adapter
│
├── 📁 types/                                 — Types + schema-bound contracts
│   ├── 📄 userPreferences.ts                 — Preferences DTO (versioned)
│   ├── 📄 userConsent.ts                     — Consent DTO (versioned)
│   └── 📄 index.ts                           — Barrel exports
│
├── 📁 validators/                            — Runtime guards / schema validation
│   ├── 📄 userPreferences.guard.ts           — isUserPreferences / validateUserPreferences
│   └── 📄 userConsent.guard.ts               — isUserConsent / validateUserConsent
│
└── 📁 __tests__/                             — Unit tests for storage + migration + guards
    ├── 📄 userPreferencesPipeline.test.ts
    ├── 📄 userMigrations.test.ts
    └── 📄 localStorageAdapter.test.ts
~~~

---

## 🧭 Context

This feature is designed to be the **single place** where “user preference intent” is translated into
safe, typed updates of platform state.

Expected context touchpoints:

- `ThemeContext` — theme selection and high-contrast mode mapping.
- `A11yContext` — reduced motion, font scaling, keyboard-oriented preferences.
- `UIContext` — panel/drawer defaults that do not conflict with governance overlays.
- `MapContext` / `TimeContext` — optional “start where I left off” behaviors (must never unmask sensitive data).
- `GovernanceContext` — *read-only* dependency to ensure preferences can’t suppress mandated warnings.

**Hard rule:** the User feature may *suggest* UI defaults, but governance remains **authoritative**.

---

## 🧱 Architecture

### Layer contract

- **No UI rendering** in `web/src/features/user/**`.
- **No direct network calls** (no REST/GraphQL/STAC/DCAT from here).
- **Deterministic state**: same inputs → same derived preference state.
- **Schema + guard first**: persisted preferences are treated as untrusted input.

### Public surface (recommended)

A minimal, stable import surface for the rest of the app:

- `initUserPreferences()` — bootstrap hydration (load → validate → migrate → apply contexts)
- `useUserPreferences()` — hook for reading/updating preference state
- `useTelemetryConsent()` — hook for consent state (if enabled)
- `UserPreferences` / `UserConsent` types + validators

### Side effects policy

Allowed side effects:

- Reading/writing to a **local** storage adapter (e.g., `localStorage`), with bounded key-space.
- Emitting **non-PII** telemetry events via approved telemetry hooks/services.

Prohibited side effects:

- Persisting anything that could identify a person.
- Writing raw entity IDs or sensitive dataset identifiers into user settings *if that could recreate restricted views*.

---

## 🗺️ Diagrams

### Preference hydration flow (bootstrap)

~~~mermaid
flowchart TD
  BOOT[App bootstrap] --> LOAD[Load persisted preferences]
  LOAD --> VALIDATE[Validate + migrate (guards)]
  VALIDATE --> APPLY[Apply to Contexts (Theme/A11y/UI)]
  APPLY --> UI[Components render with updated contexts]
~~~

### Consent gating flow (if supported)

~~~mermaid
flowchart TD
  USER[User toggles consent] --> UPDATE[Update consent state]
  UPDATE --> PROPAGATE[Propagate to telemetry boundary]
  PROPAGATE --> EMIT[Telemetry allowed?]
  EMIT -->|Yes| SEND[Emit schema-valid, non-PII event]
  EMIT -->|No| DROP[Do not emit (or emit aggregated baseline allowed by governance)]
~~~

---

## 📦 Data & Metadata

### Preference payloads (recommended contract)

Persisted preference records SHOULD be:

- **Versioned** (`schemaVersion`)
- **Minimal**
- **Non-sensitive**
- **Forward-migratable**

Example (illustrative):

~~~json
{
  "schemaVersion": "11.2.6",
  "updatedAt": "2025-12-16T00:00:00Z",
  "theme": { "mode": "system", "highContrast": false },
  "a11y": { "reducedMotion": true, "fontScale": 1.0 },
  "ui": { "density": "comfortable" },
  "telemetry": { "consent": "default" }
}
~~~

### Storage keys

Storage keys MUST be:

- namespaced
- version-scoped
- collision-safe

Recommended pattern:

- `kfm.user.preferences.v11`
- `kfm.user.consent.v11`

### Migration strategy

- Prefer **additive** schema evolution.
- When breaking changes occur, provide explicit migration steps in `userMigrations.ts`.
- Never silently “reinterpret” old fields into new meanings.

---

## 🧠 Story Node & Focus Mode Integration

If the platform supports per-user **presentation defaults** for Focus Mode or Story reading:

Allowed (presentation-only):

- Remember which panel was last expanded/collapsed.
- Remember “dense vs comfortable” reading layout.
- Remember preferred citation/provenance display density.

Not allowed:

- Any personalization that changes factual narratives or ranking logic without explicit governance approval.
- Any preference that hides provenance, CARE labels, sovereignty notices, or masking indicators.

This feature may store **UI preferences** for Focus/Story components, but cannot alter content semantics.

---

## ⚖ FAIR+CARE & Governance

Because this feature is adjacent to “user data,” it has strict constraints:

- **No PII** in:
  - persisted preferences,
  - telemetry events,
  - debug logs.
- **No stable identifiers** that allow cross-session tracking without explicit governance approval.
- **No governance override**:
  - preferences cannot disable masking,
  - preferences cannot hide sovereignty notices,
  - preferences cannot suppress provenance access.
- **Safety-first defaults**:
  - if validation fails, fall back to safe defaults (do not crash, do not leak).

Governance violations are treated as **security and ethics defects**.

---

## 🧪 Validation & CI/CD

Minimum expectations for this feature:

- **Type safety**
  - strict TypeScript compilation
  - no `any`-typed preference payloads

- **Runtime validation**
  - guards for all persisted records
  - explicit migration coverage tests

- **CI checks**
  - `pii-scan` must pass (no user identifiers)
  - telemetry events must remain schema-valid
  - feature must not introduce secrets (secret-scan)

Recommended test locations:

~~~text
tests/unit/web/features/user/**
tests/integration/web/features/user/**
~~~

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-16 | Initial User feature README; aligned to KFM-MDP v11.2.6 and web feature-layer governance constraints. |

---

<div align="center">

👤 **KFM Web — User Feature**  
Deterministic Preferences · Non‑PII by Design · Governance‑Safe Defaults

[← Features Layer](../README.md) ·
[🧭 Web Source Overview](../../README.md) ·
[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

