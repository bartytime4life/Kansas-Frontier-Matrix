---
title: "📂 Kansas Frontier Matrix — Governance Components Overview"
path: "web/src/components/Governance/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Component Overview"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "Public / Medium (content-dependent)"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web-components-governance-readme:v12.0.0-draft"
semantic_document_id: "kfm-doc-web-components-governance-readme-v12.0.0-draft"
event_source_id: "ledger:web/src/components/Governance/README.md"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "summarize"
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 📂 Kansas Frontier Matrix — Governance Components Overview

## 📘 Overview

### Purpose
- Define the **UI component contract** for how KFM’s Web frontend **displays governance** (FAIR+CARE context, sovereignty constraints, sensitivity labels, redaction/generalization explanations) in a consistent, accessible way.
- This document governs **presentation and UI behavior** only. **Policy decisions** (what is restricted, how redaction is computed, who can see what) must be enforced **upstream** (catalog/graph/API), not invented or overridden in the browser.

### Scope
| In Scope | Out of Scope |
|---|---|
| UI primitives for governance: badges, notices, “why masked” explanations, safe-action gating, provenance/audit affordances | Defining governance policy; approving releases; implementing server-side redaction/auth; rewriting provenance; creating new rules outside `governance_ref` |
| A11y expectations for governance messaging (screen-reader clarity, non-color-only signaling) | Security architecture details beyond what the UI must assume/avoid |
| Integration patterns for Map panels, Detail drawers, Story Nodes, and Focus Mode surfaces | API contract changes (use `TEMPLATE__API_CONTRACT_EXTENSION.md` if contracts change) |

### Audience
- Primary: Web UI engineers working in `web/src/components/`
- Secondary: Governance reviewers (FAIR+CARE), QA, security reviewers, doc maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo — create if missing)
- Terms used in this doc:
  - **Governance bundle**: API-provided flags/labels describing sensitivity, CARE/sovereignty constraints, and any redaction/generalization requirements.
  - **Redaction vs generalization**: removal vs controlled imprecision (e.g., bounding box vs exact coordinate).
  - **Safe actions**: UI actions that remain permitted under the current governance state.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering; Focus Mode constraints |
| Governance charter | `docs/governance/ROOT_GOVERNANCE.md` | FAIR+CARE Council | Source of truth for governance rules and review gates |
| Ethics guidance | `docs/governance/ETHICS.md` | FAIR+CARE Council | UI must not encourage policy bypass |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | FAIR+CARE Council | Indigenous data protection & sovereignty constraints |
| Component consumer example | `web/src/components/DetailDrawer/README.md` | Web UI | Not confirmed in repo — common consumer surface |
| Telemetry schemas | `schemas/telemetry/` | Telemetry | Not confirmed in repo — where governance UI events should be defined/validated |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All behavior described as **UI contract**, not policy invention
- [ ] All paths referenced are repo-real or marked **not confirmed in repo**
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No instructions that bypass review/approval processes

## 🗂️ Directory Layout

### This document
- `path`: `web/src/components/Governance/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs; catalogs emitted to STAC/DCAT/PROV |
| Documentation | `docs/` | Canonical governed docs (including governance + templates) |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map/narrative clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 src/
    └── 📁 components/
        └── 📁 Governance/
            ├── 📄 README.md
            ├── 📄 index.ts                         — (not confirmed in repo)
            ├── 📄 GovernanceBadge.tsx              — (not confirmed in repo)
            ├── 📄 GovernanceNotice.tsx             — (not confirmed in repo)
            ├── 📄 RedactionNotice.tsx              — (not confirmed in repo)
            ├── 📄 GovernanceGate.tsx               — (not confirmed in repo)
            └── 📄 GovernanceHelpLink.tsx           — (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM’s UI surfaces (maps, entity inspectors, Story Nodes, Focus Mode) present information that may be:
- governed by FAIR+CARE requirements,
- subject to Indigenous data sovereignty constraints,
- redacted/generalized based on sensitivity rules,
- provenance-linked (STAC/DCAT/PROV pointers) and therefore audit-relevant.

Without a central Governance component suite, teams tend to re-implement inconsistent:
- badge/label mapping,
- “why is this hidden?” messaging,
- safe-action gating (export/copy/open),
- accessibility semantics for warnings.

### Assumptions
- Governance decisions (sensitivity, redaction/generalization requirements) are produced upstream and delivered via **API contracts**.
- The frontend is a client: it **renders** governance state; it does **not** compute or override governance policy.
- Focus Mode and Story Nodes require evidence-led presentation (no unsourced narrative).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Governance UI must not leak restricted values via DOM attributes, logs, or telemetry.
- If AI-derived content is shown anywhere in governed surfaces, it must be opt-in and clearly labeled with uncertainty (policy lives in upstream governance docs; UI must reflect it).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical shape of the “governance bundle” in API responses? | API + Governance | TBD |
| Are there standardized “redaction reason codes” that the UI should map to copy? | Governance | TBD |
| What telemetry events are required for governance UI visibility (non-PII)? | Telemetry | TBD |

### Future extensions
- Localization of governance explanations (multi-language)
- “Reason-code → explanation” registry (versioned, testable)
- Stronger telemetry governance signals (e.g., counts of redaction-triggered renders, without leaking content)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as Contracted API
  participant GOV as Governance UI Components

  UI->>API: Request entity/context bundle (id, mode)
  API-->>UI: Payload + governance bundle + provenance refs
  UI->>GOV: Render(governance bundle, content)
  GOV-->>UI: Badges/notices + gated actions + redaction explanations
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Governance bundle (labels, flags, reasons) | JSON | API response | Contract/schema validation (not confirmed in repo) |
| Entity/dataset/story payload | JSON | API response | Contract/schema validation |
| Auth context (role/claims) | JWT/headers → app state | Auth layer | Must never be logged in telemetry |
| UI config (copy strings, mappings) | TS/JSON | `web/src/...` | Unit tests for mapping completeness |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Governance badges/notices in UI | DOM | Web runtime | A11y checks + snapshot tests |
| “Why masked” explanations | DOM text | Web runtime | Must not include raw restricted values |
| Telemetry (non-PII) | JSON events | Web telemetry pipeline | `schemas/telemetry/…` (not confirmed in repo) |

### Sensitivity & redaction
- Do not render restricted values (exact coordinates, names/IDs, timestamps) when governance indicates redaction/generalization.
- Avoid “accidental disclosure” vectors:
  - `data-*` DOM attributes
  - hidden copy-to-clipboard targets
  - console logs / error logs
  - telemetry payloads
- Prefer “presence with explanation” over silent omission:
  - “Location generalized due to sovereignty constraints.”
  - “Exact timestamp withheld due to sensitivity.”

### Quality signals
- Mapping coverage: every governance state has a user-facing badge and explanation copy.
- A11y: warnings/notices are screen-reader discoverable and do not rely on color alone.
- Consistency: same governance state yields same UX across map panels, drawers, and Focus Mode.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If a payload includes STAC identifiers, Governance components may display:
  - Collection/Item IDs (display-safe)
  - License/rights (display-safe)
  - Generalized spatial/temporal extents when required
- Do not infer missing STAC fields client-side.

### DCAT
- If a payload includes DCAT dataset identifiers, Governance components may display:
  - Dataset ID/title/publisher (when permitted)
  - License mapping (display-safe)
- License and rights text should be presented as received (no UI “policy rewriting”).

### PROV-O
- Governance UI may provide affordances to:
  - view provenance references (run IDs, activity IDs)
  - open audit/provenance panels (if allowed)
- Must not “fill in gaps” in provenance.

### Versioning
- Governance-related copy/mappings should be versioned with the UI release.
- If governance meaning changes, treat as a contract change and route through review (and API contract template where applicable).

## 🧱 Architecture

### Recommended component responsibilities (update to match actual implementation)
> Note: filenames/components below are a recommended decomposition and are **not confirmed in repo**.

- **GovernanceBadge**
  - Render classification + CARE label chips in a compact, non-color-only way.
- **GovernanceNotice**
  - Render a short, plain-language summary of constraints (e.g., “Some fields are generalized.”).
- **RedactionNotice**
  - Render “why masked” explanations tied to reason codes/flags (no sensitive values).
- **GovernanceGate**
  - Wrapper that conditionally renders children or disables actions based on governance flags.
- **GovernanceHelpLink**
  - Links to the relevant governance policy pages (`governance_ref`, `ethics_ref`, `sovereignty_policy`).

### Recommended UI contract shape (illustrative)
~~~ts
export type GovernanceBundle = {
  classification: "open" | "restricted" | "internal" | string;
  sensitivity: "public" | "variable" | "restricted" | string;

  care_label?: string;               // e.g., "Public / Medium (content-dependent)"
  indigenous_rights_flag?: boolean;  // if present in contract
  redaction_required?: boolean;

  reasons?: Array<{
    code: string;                    // e.g., "SOVEREIGNTY_LOCATION_GENERALIZED"
    summary: string;                 // short display-safe explanation
    affects?: string[];              // fields/sections affected (display-safe names)
  }>;

  allow_export?: boolean;
  allow_copy?: boolean;
};
~~~

## 🧠 Story Node & Focus Mode Integration

- Governance UI components should be used anywhere Story Nodes / Focus Mode render:
  - citations and sources,
  - “audit” or provenance panels,
  - AI-assisted content blocks (if enabled).
- Non-negotiables:
  - No unsourced narrative is introduced by the UI.
  - Governance UI never reframes redaction as “missing data”; it must be explicit and plain-language.
  - AI-assisted content (if present) must be clearly labeled as such and must not be presented as provenance.

## 🧪 Validation & CI/CD

### Automated checks (recommended)
- Unit tests:
  - badge mapping coverage (every classification maps to a chip)
  - gating behavior (allowed/blocked actions)
  - redaction notice rendering (no sensitive values)
- A11y checks:
  - notices announced to screen readers
  - icons/badges have accessible labels
  - no color-only signaling
- Integration / e2e flows:
  - entity select → panel open → governance badges visible
  - restricted layer/entity → hidden from UI or shown generalized with explanation (contract dependent)

### Security and privacy checks
- Verify no restricted fields appear in:
  - DOM attributes
  - client logs
  - telemetry events
- Telemetry (if present) must remain non-PII and schema-conformant.

## ⚖ FAIR+CARE & Governance

Governance components must:
- reflect upstream governance decisions faithfully
- provide “why masked/generalized” explanations without revealing restricted details
- ensure UI actions (export/copy/open) are gated to prevent accidental disclosure
- route policy questions to governance docs (do not embed new policy in UI copy)

Governance components must not:
- invent sensitivity classifications, redaction rules, or approvals
- provide hidden toggles that bypass redaction/generalization
- claim that an item is “cleared” or “approved” unless the contract explicitly carries that signal

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0-draft | 2025-12-21 | Initial Governance component overview using v12 universal doc format. | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`