---
title: "Kansas Frontier Matrix — DetailDrawer Component Overview"
path: "web/src/components/DetailDrawer/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Component Overview"
license: "MIT"

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

doc_uuid: "urn:kfm:doc:web:components:detaildrawer:readme:v12.0.0-draft"
semantic_document_id: "kfm-doc-web-components-detaildrawer-readme-v12.0.0-draft"
event_source_id: "ledger:web/src/components/DetailDrawer/README.md"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "structure_extract"
ai_transform_prohibited:
  - "summarize"
  - "generate_policy"
  - "infer_sensitive_locations"
  - "speculative-additions"
  - "unverified-historical-claims"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Kansas Frontier Matrix — DetailDrawer Component Overview

## 📘 Overview

### Purpose
The **DetailDrawer** is a governed, accessible “stay-on-page” UI pattern used in the KFM Web UI to present
contextual detail (metadata, provenance, and CARE/sovereignty context) without navigating away from maps,
Story Nodes, or Focus Mode surfaces.

This document governs:
- expected responsibilities of the DetailDrawer UI surface
- contract expectations for **governance-aware** rendering (masking/generalization)
- accessibility and telemetry expectations for a governance-critical component

### Scope
| In Scope | Out of Scope |
|---|---|
| DetailDrawer UX contract (open/close lifecycle, focus rules, sectioning) | Backend redaction logic implementation |
| Governance-aware display behaviors (masking/generalization indicators) | Generating STAC/DCAT/PROV catalogs |
| Data/metadata expectations for the drawer payload | Neo4j schema design or direct graph querying from UI |
| Telemetry expectations (non-PII, schema-conformant) | Defining organization-wide telemetry policy |

### Audience
- Primary: KFM Web engineers; a11y QA
- Secondary: Governance reviewers; API engineers (payload contracts); Story/Focus Mode owners

### Definitions (link to glossary)
- Link: `../../../../docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **DetailDrawer**: a slide-out panel for contextual detail, designed to preserve the user’s current map/story context.
  - **Focus Mode**: an immersive narrative exploration view that must remain provenance-led.
  - **Story Node**: a narrative artifact that must be evidence-led and source-citable.
  - **Redaction / generalization**: the contracted replacement of sensitive fields (e.g., exact coordinates) with safer representations.
  - **STAC / DCAT / PROV**: metadata and provenance standards used as upstream evidence pointers.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This document | `web/src/components/DetailDrawer/README.md` | Web | Governed component overview |
| DetailDrawer component directory | `web/src/components/DetailDrawer/` | Web | Verify actual contents |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Path is per v12 docs; verify if repo still uses `docs/standards/...` |
| Ethics guide | `docs/governance/ETHICS.md` | Governance |  |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance |  |
| Telemetry schema (component) | `schemas/telemetry/web-components-detaildrawer-v2.json` | Observability | not confirmed in repo (inherited from prior doc) |
| Telemetry schema (energy) | `schemas/telemetry/energy-v2.json` | Observability | not confirmed in repo (inherited from prior doc) |
| Telemetry schema (carbon) | `schemas/telemetry/carbon-v2.json` | Observability | not confirmed in repo (inherited from prior doc) |
| Release SBOM | `releases/<ver>/sbom.spdx.json` | Release Eng | not confirmed in repo (placeholder) |
| Release manifest | `releases/<ver>/manifest.zip` | Release Eng | not confirmed in repo (placeholder) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory layout matches actual repo contents (no invented filenames)
- [ ] All governance-sensitive behaviors are described as **contracts**, not assumptions
- [ ] Validation steps listed and repeatable
- [ ] API-boundary invariant stated (UI never reads Neo4j directly)
- [ ] Version history updated with date + summary

## 🗂️ Directory Layout

### This document
- `path`: `web/src/components/DetailDrawer/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Web UI | `web/` | React/Map UI (components, pages, app shell) |
| Web components | `web/src/components/` | Reusable UI components (including DetailDrawer) |
| API layer | `src/server/` | Contracted access layer (REST/GraphQL) |
| Schemas | `schemas/` | JSON schemas, SHACL, telemetry schemas |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV outputs consumed by graph/API |

### Expected component directory (verify in repo)
The following file list is **not confirmed in repo** and must be updated to match the working branch:

~~~text
📁 web/
└── 📁 src/
    └── 📁 components/
        └── 📁 DetailDrawer/
            ├── 📄 README.md
            ├── 📄 DetailDrawer.tsx
            ├── 📄 DrawerHeader.tsx
            ├── 📄 DrawerSection.tsx
            ├── 📄 DrawerMetadata.tsx
            ├── 📄 DrawerProvenance.tsx
            ├── 📄 DrawerCAREBlock.tsx
            ├── 📄 DrawerFooter.tsx
            └── 📄 DrawerA11yHelpers.tsx
~~~

## 🧭 Context

### Where DetailDrawer is used
DetailDrawer is intended for situations where the user needs deeper context without losing their place:
- map feature selection (entity inspect)
- search results “inspect” / “preview” actions
- Story Node supporting panels
- Focus Mode supporting panes (evidence pointers, provenance, governance context)

### API boundary and canonical pipeline
DetailDrawer must be fed by **contracted outputs** (API payloads and/or published catalogs), not by direct
graph access in the browser.

Canonical ordering (non-negotiable):
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Neo4j graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[DetailDrawer]
  E --> G[Story Nodes]
  G --> H[Focus Mode]
~~~

~~~mermaid
sequenceDiagram
  participant User
  participant UI as React/Map UI
  participant API as API Layer
  participant Drawer as DetailDrawer

  User->>UI: Select entity / open details
  UI->>API: Request detail bundle (id + context)
  API-->>UI: Contracted payload + governance flags + provenance refs
  UI->>Drawer: Render drawer with payload
  Drawer-->>UI: Emit telemetry (non-PII)
  User->>Drawer: Close / toggle section
  Drawer-->>UI: Restore focus to invoking element
~~~

## 📦 Data & Metadata

### Data expected by the drawer (conceptual)
The DetailDrawer should be treated as a **pure renderer** of a contracted “detail bundle”.

| Field | Source | Sensitivity | Notes |
|---|---|---|---|
| `id` | API | public | Stable entity identifier |
| `entity_type` | API | public | e.g., Place / Person / Event / Document / Organization / Artifact |
| `title` | API | public | Display label |
| `summary` | API | public | Optional; should be sanitized for display |
| `stac_item_id` | API/catalog | public | Optional pointer to STAC Item |
| `dcat_dataset_id` | API/catalog | public | Optional pointer to DCAT dataset |
| `prov_activity_id` | API/catalog | public | Optional pointer to PROV run/activity |
| `temporal_extent` | API | variable | Must support generalization |
| `spatial_extent` | API | variable | Must support generalization (avoid exact coords if gated) |
| `governance` | API | variable | CARE label, classification, redaction flags, display rules |
| `actions` | UI policy | variable | Must be filtered by governance rules |

### Redaction and generalization contract
If the payload indicates masking/generalization is required:
- do **not** render raw sensitive values (including in hidden DOM attributes)
- prefer “show that something exists” with a clear indicator (e.g., “Location generalized for sovereignty”)
- avoid enabling copy/export actions that would bypass masking
- ensure the reason shown is **policy-based**, not speculative

### Telemetry expectations (non-PII)
Recommended event names (schema-conformant):
- `drawer:open`
- `drawer:close`
- `drawer:section-toggle`
- `drawer:care-warning-shown`
- `drawer:provenance-visible`
- `drawer:action`

Telemetry must:
- exclude raw user-entered queries and sensitive identifiers
- be version-tagged (component version + environment)
- avoid embedding raw coordinates or unredacted text fragments

## 🌐 STAC

### How STAC relates to the drawer
DetailDrawer may surface STAC pointers as read-only evidence anchors:
- STAC Item ID and/or Collection ID
- a safe list of assets (links/previews) only when allowed by governance flags
- license/rights fields as display-safe metadata

The drawer must not:
- fabricate STAC fields
- infer missing geometry/time fields
- “reconstruct” redacted STAC values client-side

## 🧾 DCAT & PROV Alignment

### DCAT
DetailDrawer may show DCAT-derived fields when provided by the payload:
- dataset title/publisher/rights/license identifiers
- distribution links (if allowed)

### PROV
DetailDrawer may show provenance pointers when available:
- `prov:Activity` identifiers (run IDs)
- upstream input entity IDs (where disclosure is allowed)
- links to provenance artifacts (e.g., JSON-LD export) if published

The drawer must not:
- fill gaps in provenance with assumptions
- present a provenance chain that is not explicitly provided

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| DetailDrawer (UI) | Governed, accessible contextual detail surface | Props: `isOpen`, `onClose`, `payload` |
| API Layer | Returns contracted detail bundle + governance flags + provenance refs | REST/GraphQL (not specified here) |
| Catalog outputs | Provide STAC/DCAT/PROV identifiers and evidence anchors | Read-only published outputs |
| Telemetry pipeline | Collects non-PII UI events for reliability/usage monitoring | JSON schema-conformant events |

### Interfaces / contracts (conceptual TypeScript)
~~~ts
export type GovernanceFlags = {
  care_label?: string;
  classification?: string;
  redaction_required?: boolean;
  // If true, UI must generalize sensitive fields (e.g., location/time) and show an explanation.
  generalize_location?: boolean;
  generalize_time?: boolean;
  // Optional human-readable explanation (must be policy-based; no speculation).
  display_notice?: string;
};

export type ProvenanceRefs = {
  stac_item_id?: string;
  dcat_dataset_id?: string;
  prov_activity_id?: string;
};

export type DetailBundle = {
  id: string;
  entity_type: string;
  title: string;
  summary?: string;
  temporal_extent?: unknown;
  spatial_extent?: unknown;
  governance: GovernanceFlags;
  provenance?: ProvenanceRefs;
  actions?: Array<{ id: string; label: string; kind: "navigate" | "export" | "open_panel" }>;
};
~~~

### Extension points checklist
If adding a new drawer section:
- [ ] Section has stable heading semantics and does not break heading order
- [ ] Section content is gated by governance flags (mask/generalize where required)
- [ ] New telemetry events (if any) are schema-added + tested
- [ ] a11y reviewed (keyboard navigation, focus order, SR labels)
- [ ] Story/Focus Mode owners sign off if the section appears in those contexts

## 🧠 Story Node & Focus Mode Integration

DetailDrawer is a **safe supporting surface** for evidence-led context:
- Story Node excerpts shown in the drawer must be source-citable and must not introduce new claims
- Focus Mode panels must not rewrite governance status or provenance
- If AI-assisted highlighting is present:
  - label it as AI-assisted
  - keep it strictly non-speculative
  - never present it as authoritative record

## 🧪 Validation & CI/CD

### Automated checks (recommended)
- [ ] Type checking + linting for component code
- [ ] Unit tests:
  - masking/generalization behavior given governance flags
  - focus trap + focus restore on close
  - ARIA attributes present and correct
- [ ] Integration/e2e tests (as applicable):
  - map feature select → drawer opens → close restores focus
  - Focus Mode → drawer opens for an entity → no uncited content added
- [ ] Telemetry tests:
  - required events emitted
  - payload conforms to telemetry schema (if present)

### Security + privacy checks
- [ ] No secrets in code/docs
- [ ] No sensitive coordinates in snapshots/tests/fixtures
- [ ] No PII in telemetry payloads

## ⚖ FAIR+CARE & Governance

### Governance posture (inherited; verify)
- Release stage: Stable / Governed (not confirmed in repo)
- Lifecycle: LTS (not confirmed in repo)
- Review cycle: Quarterly (not confirmed in repo)
- Public with CARE/sovereignty exceptions: treated as “open” docs with redaction behavior enforced by payload flags

### Non-negotiables for DetailDrawer
- Must honor CARE and sovereignty flags and display requirements
- Must clearly explain masking/generalization in plain language (policy-based)
- Must avoid exposing sensitive values through:
  - UI text
  - DOM attributes
  - logs or telemetry payloads
  - copy/export affordances

DetailDrawer must not:
- invent provenance links
- claim governance approval where none exists
- bypass redaction rules via hidden toggles or “advanced” routes

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v12.0.0-draft | 2025-12-21 | Rebuilt from scratch using v12 Universal Doc structure; removed v11-only front-matter keys; added contract-first framing and diagrams. | TBD |
| v11.2.2 | 2025-12-16 | Prior governed README revision (v11 format). | TBD |
| v10.4.0 | 2025-11-15 | Earlier full drawer documentation. | TBD |
| v10.3.2 | 2025-11-14 | Added CARE/provenance improvements. | TBD |
| v10.3.1 | 2025-11-13 | Initial DetailDrawer overview. | TBD |