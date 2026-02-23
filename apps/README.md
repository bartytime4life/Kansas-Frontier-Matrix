<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8a4a8e59-7a6f-4d60-9c56-9f6d5f8b1f3d
title: apps/ — Runnable application surfaces
type: standard
version: v3
status: draft
owners: TBD (resolve via CODEOWNERS / repo maintainers)
created: 2026-02-22
updated: 2026-02-23
policy_label: public
related:
  - kfm://doc/kfm-definitive-design-governance-guide-vnext
  - kfm://doc/UNKNOWN_SYSTEM_OVERVIEW
  - ../docs/
tags: [kfm, apps, ui, trust-membrane, contracts, evidence-first, receiptviewer, trust-badges]
notes:
  - This README is intentionally fail-closed: it does not assume a specific tech stack or app list until confirmed in-repo.
  - First follow-up: populate the App Registry + Current layout blocks from the actual apps tree (either `apps/` or `web/apps/`, depending on repo convention).
  - v3 upgrades: add a repo-layout crosswalk (`apps/` vs `web/apps/`), incorporate ReceiptViewer + trust badges expectations, and enumerate adjacent “drop-in” governance directories (schemas/policy/ops/.github) without claiming they exist.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# apps/ — Runnable application surfaces
**Purpose:** Home for user-facing and operator-facing application surfaces (Map / Globe / Story / Catalog / Focus / Admin / CLI) that consume **governed APIs** and expose **evidence-first** UX.

![status](https://img.shields.io/badge/status-draft-lightgrey)
![layer](https://img.shields.io/badge/layer-UI%20surfaces-blue)
![governance](https://img.shields.io/badge/governance-trust%20membrane-critical)
![ux](https://img.shields.io/badge/UX-evidence--first-success)
![contracts](https://img.shields.io/badge/contracts-contract--first-important)
![evidence](https://img.shields.io/badge/evidence-ReceiptViewer%20%2B%20Drawer-informational)
![ai](https://img.shields.io/badge/AI-focus%20mode%20cite--or--abstain-informational)

> [!WARNING]
> This document is **fail-closed**. Anything repo-specific (actual app list, tooling, owners, contract paths, whether apps live in `apps/` or `web/apps/`) is **Unknown** until verified in-repo. Do not “fill in the blanks” from memory.

---

## Navigation
- [First follow-up checklist](#first-follow-up-checklist)
- [Where this fits in the repo](#where-this-fits-in-the-repo)
- [Repo layout crosswalk](#repo-layout-crosswalk)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Trust surfaces required](#trust-surfaces-required)
- [Architecture sketch](#architecture-sketch)
- [App registry](#app-registry)
- [Directory layout](#directory-layout)
- [App manifest contract](#app-manifest-contract)
- [Per-app README minimum](#per-app-readme-minimum)
- [Local development](#local-development)
- [Testing and gates](#testing-and-gates)
- [Security privacy and sensitivity](#security-privacy-and-sensitivity)
- [Add a new app](#add-a-new-app)
- [Glossary](#glossary)

---

## First follow-up checklist

These steps convert this README from **Unknown-heavy** to **Confirmed** without guessing.

### Repo facts to confirm
- [ ] Confirm where runnable UI surfaces live:
  - `ls -la apps/` **and** `ls -la web/apps/` (one may not exist)
- [ ] Capture at-a-glance trees:
  - `tree -L 3 apps/` (or `find apps -maxdepth 3 -type d`)
  - `tree -L 3 web/apps/` (or `find web/apps -maxdepth 3 -type d`)
- [ ] Identify the workspace/tooling boundary:
  - Look for `package.json`, `pnpm-workspace.yaml`, `yarn.lock`, `turbo.json`, `nx.json`, `Cargo.toml`, `go.work`, etc.
- [ ] Resolve ownership:
  - Inspect `CODEOWNERS` and any `/docs/governance/owners` (or equivalent)
- [ ] Locate API contracts consumed by apps:
  - Search for `openapi`, `graphql`, `schema`, `contracts`, `sdk`, `client`, `generated`, `proto`
- [ ] Locate evidence UX components and their contract sources:
  - Search for `EvidenceDrawer`, `ReceiptViewer`, `run_receipt`, `run_manifest`, `automation_badge`
- [ ] Confirm policy labels and deny/abstain UX patterns in use:
  - Search for `policy_label`, `classification`, `sensitivity`, `redaction`, `abstain`, `deny`

> [!TIP]
> Once those are verified, update only two sections first:
> 1) [App registry](#app-registry)  2) [Directory layout](#directory-layout)

---

## Where this fits in the repo

`apps/` is a **surface-layer** directory. It should sit at the very end of the KFM layering model:

- **Domain** → concepts and invariants (no UI)
- **Use cases** → workflows (map/story/focus/admin)
- **Interfaces** → contracts + policy boundary (governed API, schemas)
- **Infrastructure** → storage/index, pipelines, CI
- **Apps** → UX that consumes governed APIs and makes evidence visible

> [!NOTE]
> Some KFM repo layouts place runnable apps under `web/apps/` (with `web/` as the frontend workspace). If that’s true in your repo, treat this README as describing that subtree, and consider either:
> - moving it to `web/apps/README.md` and leaving a short stub here, or
> - keeping both copies with a single source-of-truth generator (preferred).

---

## Repo layout crosswalk

This section prevents “directory drift” when the repo uses `web/` as the frontend root.

> [!IMPORTANT]
> These are *layout patterns* seen in KFM design sources. They are **not** confirmations of your current repo state.

| Concept | Common location (root apps layout) | Common location (web layout) | What this means for this README |
|---|---|---|---|
| Runnable UI surfaces | `apps/<app>/` | `web/apps/<app>/` | Update “Current layout” + App Registry based on whichever exists. |
| Shared UI packages | `packages/` | `web/packages/` | Keep shared code out of apps. |
| Shared UI components | `packages/ui/` | `web/src/components/` | Evidence components (e.g., ReceiptViewer) should live in shared UI space, not per-app copies. |
| UI contract schemas | `schemas/ui/` | `schemas/ui/` | UI event schemas live alongside other contracts. |
| API services | `api/` or `services/` | `api/services/` | Apps depend on governed APIs; do not implement policy/verification in clients. |
| Governance policy | `policy/` | `policy/` | OPA/Rego policies are gates and runtime rules; apps only *display* results. |
| CI gates | `.github/workflows/` | `.github/workflows/` | Apps are safety-critical: treat UI trust flows as required checks. |

---

## What belongs here

This folder is for **runnable applications**—anything a human launches (browser UI, operator console, desktop wrapper, CLI) whose primary job is **presenting governed KFM knowledge**.

Typical app categories (examples; verify actual apps in this repo):
- **Map Explorer UI**: 2D map rendering, timeline/time slider, evidence drawer, layer policies
- **Globe UI** (optional): 3D rendering and camera choreography; same evidence constraints as Map
- **Story UI**: narrative browsing, claim-level citations, map choreography via stored view state, “what changed”
- **Catalog UI**: dataset discovery and version browsing with license + policy summaries
- **Focus Mode UI**: governed Q&A workflow (policy pre-check → evidence retrieval → cite-or-abstain)
- **Admin/Steward UI**: intake review, promotion gates dashboards, policy fixtures review (usually restricted)
- **CLI**: operator workflows (promotion, validation, evidence resolution) via governed APIs

> [!NOTE]
> Shared libraries should **not** live here. Put shared code in `packages/` or `web/packages/` (or repo-standard workspace) to prevent copy/paste drift.

---

## What must not go here

This directory should remain a **surface layer**. The following do not belong in `apps/`:

- **Shared domain libraries** used by multiple apps (move to `packages/` / `web/packages/` / equivalent)
- **Shared UI components** used by multiple apps (move to shared UI component space)
- **Data pipelines** or jobs (move to pipeline/workflow area)
- **Direct storage/index access adapters**
  - no DB drivers in browser code
  - no “S3 client in the UI” patterns
  - no “search index client in the UI” patterns
- **Policy engines or redaction logic**
  - policy enforcement belongs in governed APIs, not in clients
- **Receipt/attestation verification logic**
  - clients may *display* verification results; verification happens behind the trust membrane
- **Long-lived secrets**
  - no embedded credentials
  - no “shared admin token” configuration

---

## Non-negotiable invariants

These are requirements. Apps are the most visible trust surface; breaking invariants breaks credibility.

### 1) Trust membrane
- Apps **MUST NOT** access object storage, databases, or internal indexes directly.
- Apps **MUST** consume data only through **governed APIs** that enforce policy, redactions, and logging.
- Apps **MUST NOT** embed credentials that could bypass governance.

### 2) Truth path awareness
Apps sit at the end of the KFM “truth path”:
- Upstream → RAW → WORK or QUARANTINE → PROCESSED → CATALOG and LINEAGE → projections → **governed API** → **apps**
- Apps **MUST** assume only *promoted* dataset versions are admissible for public surfaces.

### 3) Evidence-first UX
Every layer, claim, chart, or AI output **MUST** open into an **evidence view**:
- DatasetVersion ID and human name
- License and rights holder attribution
- Policy label and redactions applied
- Provenance chain and run receipt reference
- Validation and freshness indicators
- Evidence bundle digest or checksum when policy allows

### 3b) Map view state is a reproducible artifact
If the system supports “share links”, Story Nodes, or Focus Mode answers tied to a map view, the **view state** must be durable and reproducible:
- camera position (2D/3D)
- active layers with DatasetVersion IDs (not floating “latest”)
- time window / timeline selection
- filters and selections (policy-safe)
- evidence references (ids/digests), not embedded restricted payloads

### 4) Focus Mode is not general chat
If this repo contains a Focus Mode surface, it **MUST** implement **cite-or-abstain**:
- If citations can’t be verified, the UI **MUST** abstain or reduce scope and show why
- If policy denies, the UI **MUST** deny and explain in policy-safe terms

### 5) Contract-first changes
- API and schema contracts are first-class artifacts.
- UI changes that rely on new or changed data **MUST** start from a contract change (OpenAPI/GraphQL/JSON Schema), not ad-hoc parsing.

---

## Trust surfaces required

These are not optional polish. They are the user-visible governance contract.

Minimum trust surfaces expected across apps:
- **Evidence drawer** accessible from every layer and story claim
- **ReceiptViewer (read-only)** for run receipts/manifests (schema validate → signature verify → render; otherwise “untrusted”)
- **Automation status badges** (optional but recommended) to show pipeline health, freshness, and provenance linkage without leaking restricted details
- **Data version label** per layer linking to the relevant DatasetVersion record
- **Policy notices** at interaction time
  - example: “Geometry generalized due to policy”
- **What changed** panel comparing dataset versions
  - counts, checksums, QA metrics, and effective dates
- **Degraded mode indicators**
  - evidence resolver degraded
  - contract mismatch
  - stale data

### Evidence drawer minimum fields
- Evidence bundle ID and digest
- DatasetVersion ID and dataset name
- License and rights holder attribution
- Freshness and validation status
- Provenance chain link to run receipt
- Redactions applied and obligations
- Access note for restricted evidence: “exists but you can’t access it”

> [!WARNING]
> Evidence UX must never become a data exfiltration path. “Evidence exists” must not leak restricted existence unless policy allows.

---

## Architecture sketch

```mermaid
flowchart LR
  subgraph Apps["apps/ or web/apps/"]
    Map["Map UI"]
    Globe["Globe UI"]
    Story["Story UI"]
    Catalog["Catalog UI"]
    Focus["Focus Mode UI"]
    Admin["Admin/Steward UI"]
    CLI["Operator CLI"]
  end

  Apps -->|HTTPS| API["Governed API"]
  API --> Policy["Policy Engine"]
  API --> Evidence["Evidence Resolver"]
  API --> Repos["Repository Interfaces"]
  Repos --> Canon["Canonical Stores"]
  Repos --> Proj["Rebuildable Projections"]
```

### Evidence-first interaction sketch
```mermaid
sequenceDiagram
  participant U as User
  participant A as App
  participant G as Governed API
  participant P as Policy
  participant E as Evidence Resolver

  U->>A: Toggle layer / open claim / ask Focus question
  A->>G: Request data + evidence refs
  G->>P: Evaluate policy for requester
  G->>E: Resolve evidence bundle for response
  E-->>G: Evidence bundle + digests + links (scoped)
  G-->>A: Payload + citations + policy labels
  A-->>U: Render + evidence drawer + denial or abstain UI when needed
```

---

## App registry

> [!IMPORTANT]
> Populate this table from the actual apps tree:
> - either `apps/*` **or** `web/apps/*`
> - do not merge them conceptually unless your repo intentionally ships both.

| App path | Type | Primary surface | Policy label | Primary API contract references | Owner | Status |
|---|---|---|---|---|---|---|
| `TBD` | web / desktop / cli / other | map / globe / story / catalog / focus / admin / steward / ops | public / restricted / internal / secret | `TBD` | `TBD` | draft |
| `TBD` |  |  |  |  |  |  |

### Registry definition of done
- [ ] Every app has a one-line purpose.
- [ ] Every app lists governed API dependencies.
- [ ] Every app declares a `policy_label` and constraints.
- [ ] Every app links to its evidence UX entry points (drawer, ReceiptViewer, badges, what-changed).

---

## Directory layout

### Current layout

Replace the block below with the real tree output (choose the directory that exists).

```text
apps/ or web/apps/
├─ README.md
└─ TBD
```

### Design-source drop-ins (adjacent directories)

This is a **proposed** drop-in layout from KFM integration sources. Use it as a scan checklist for “what else might exist” around apps:

```text
repo-root/
|-- schemas/                                    # JSON Schemas: run_receipt, run_manifest, watchers, UI events
|-- policy/                                     # OPA/Rego and policy packs (fail-closed gates)
|-- ops/                                        # Templates + operational playbooks
|-- src/                                        # Pipelines + models (run receipt emitters, validators, etc.)
|-- web/                                        # Frontend workspace (may contain apps, shared components)
`-- .github/workflows/                          # Required status checks, attest, policy gates
```

### Recommended layout template (apps-at-root)

Use only if the repo does not already enforce a different convention.

```text
apps/                                             # Runnable app surfaces (each app ships independently)
├─ map/                                           # Map Explorer (layers + timeline + inspect)
│  ├─ README.md                                   # App purpose, routes, dev/run instructions
│  ├─ kfm.app.json                                # App manifest (id, owner, policy surface, capabilities)
│  └─ src/                                        # App source (UI + app-specific logic)
│
├─ globe/                                         # Optional 3D globe (same evidence surfaces; different renderer)
│  ├─ README.md
│  ├─ kfm.app.json
│  └─ src/
│
├─ story/                                         # Story Mode (narrative reader + map choreography)
│  ├─ README.md
│  ├─ kfm.app.json
│  └─ src/
│
├─ catalog/                                       # Dataset discovery + version browsing
│  ├─ README.md
│  ├─ kfm.app.json
│  └─ src/
│
├─ focus/                                         # Focus Mode (Q&A + citations + audit/explain)
│  ├─ README.md
│  ├─ kfm.app.json
│  └─ src/
│
├─ admin/                                         # Admin/Steward Console (restricted; audit-heavy workflows)
│  ├─ README.md
│  ├─ kfm.app.json
│  └─ src/
│
└─ cli/                                           # CLI tools (operators/devs; automation entrypoints)
   ├─ README.md
   ├─ kfm.app.json
   └─ src/
```

### Recommended layout template (web/apps)

If your repo uses a `web/` workspace root, the equivalent pattern is:

```text
web/                                               # Frontend workspace (multiple apps + shared UI packages)
├─ apps/                                           # App entrypoints (route shells + app-specific composition)
│  ├─ map/                                         # 2D map explorer (layers, timeline, inspect)
│  ├─ globe/                                       # 3D globe explorer (Cesium; optional)
│  ├─ story/                                       # Story reader + map choreography
│  ├─ catalog/                                     # Catalog browser (datasets/layers; policy badges)
│  ├─ focus/                                       # Focus Mode UI (Q&A + citations + audit/explain)
│  └─ admin/                                       # Admin console (governance, ops, approvals; restricted)
│
├─ packages/                                       # Shared UI packages (do not duplicate per-app)
│  └─ …                                            # e.g., ui-kit, contracts, services, map-adapters, telemetry
│
└─ src/components/                                 # Shared components (legacy/global shared)
   └─ …                                            # EvidenceDrawer, ReceiptViewer, CitationList, AuditDrawer, etc.
```

---

## App manifest contract

Each app directory **SHOULD** include an app manifest file (example: `kfm.app.json`) so governance intent is machine-readable.

> [!NOTE]
> If the repo already has a standard manifest, use that instead. This is a proposed contract.

### Example kfm.app.json
```json
{
  "app_id": "kfm.app.map",
  "name": "KFM Map Explorer",
  "surface": "map",
  "policy_label": "public",
  "governed_api": {
    "base_url_env": "KFM_API_BASE_URL",
    "contracts": [
      "openapi://api/openapi.yaml#tag=tiles",
      "openapi://api/openapi.yaml#tag=catalog",
      "openapi://api/openapi.yaml#tag=evidence"
    ]
  },
  "trust_surfaces": ["evidence_drawer", "receipt_viewer", "what_changed"],
  "evidence_ux": {
    "required": true,
    "entry_points": ["layer_details_drawer", "receipt_viewer_modal", "story_claim_citation_popover"]
  },
  "telemetry": {
    "otel": true,
    "pii": "none"
  }
}
```

### Minimal contract rules
- `policy_label` is mandatory.
- `governed_api.contracts` is mandatory for any app that makes API calls.
- `evidence_ux.required = true` for any public-facing surface that shows layers or claims.
- `trust_surfaces` SHOULD be present for public-facing surfaces.

### Proposed JSON Schema
Use this to validate manifests in CI with a fail-closed rule.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "kfm://schema/app-manifest/v1",
  "type": "object",
  "additionalProperties": false,
  "required": ["app_id", "name", "surface", "policy_label", "governed_api", "evidence_ux"],
  "properties": {
    "app_id": { "type": "string", "minLength": 1 },
    "name": { "type": "string", "minLength": 1 },
    "surface": { "type": "string", "enum": ["map", "globe", "story", "catalog", "focus", "admin", "steward", "ops", "cli", "other"] },
    "policy_label": { "type": "string", "enum": ["public", "restricted", "internal", "secret"] },
    "governed_api": {
      "type": "object",
      "additionalProperties": false,
      "required": ["base_url_env", "contracts"],
      "properties": {
        "base_url_env": { "type": "string", "minLength": 1 },
        "contracts": { "type": "array", "minItems": 1, "items": { "type": "string", "minLength": 1 } }
      }
    },
    "trust_surfaces": {
      "type": "array",
      "items": { "type": "string" }
    },
    "evidence_ux": {
      "type": "object",
      "additionalProperties": false,
      "required": ["required", "entry_points"],
      "properties": {
        "required": { "type": "boolean" },
        "entry_points": { "type": "array", "items": { "type": "string" } }
      }
    },
    "telemetry": {
      "type": "object",
      "additionalProperties": true,
      "properties": {
        "otel": { "type": "boolean" },
        "pii": { "type": "string", "enum": ["none", "low", "moderate", "high"] }
      }
    }
  }
}
```

---

## Per-app README minimum

Each app under `apps/<app>/` or `web/apps/<app>/` **SHOULD** include a README that answers:

- title and one-line purpose
- where it fits in the system
- acceptable inputs
- exclusions
- governed API contracts used
- evidence UX entry points (drawer, ReceiptViewer, badges, what-changed)
- map/story/focus view_state expectations (if applicable)
- how to run locally
- tests and CI gates

### Template header snippet
```md
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: apps/<app>/ — <purpose>
type: standard
version: v1
status: draft
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - ../README.md
tags: [kfm, apps]
notes:
  - Keep app-specific unknowns explicit until verified.
[/KFM_META_BLOCK_V2] -->
```

---

## Local development

> [!IMPORTANT]
> This section is intentionally generic until the repo’s tooling is verified.

### Quick start pattern
1. Identify the workspace toolchain from repo root (and whether the frontend is rooted at `web/`).
2. Install dependencies using the repo’s chosen package manager.
3. Run the app’s dev target from its directory.
4. Confirm it points to a **governed API** instance and not direct storage.

### Proposed environment variables
- `KFM_API_BASE_URL` — base URL for the governed API gateway
- `KFM_ENV` — `local|dev|stage|prod`

> [!WARNING]
> Apps must be safe under policy deny. Even if UI misconfigures itself, restricted content must not render because enforcement happens in the API.

---

## Testing and gates

Apps should be treated as safety-critical surfaces.

### Minimum CI gates
- [ ] Unit tests for components and adapters
- [ ] Contract checks for governed API compatibility
- [ ] Evidence and citation resolution smoke test in CI
- [ ] Receipt/manifest rendering safety tests (schema validate + “untrusted” fallback)
- [ ] E2E tests for critical trust flows
- [ ] Accessibility checks
- [ ] Dependency and supply chain checks
- [ ] Static guardrail: no direct storage access

### Recommended E2E trust flows
- Load app → toggle a layer → open evidence drawer → verify policy label shown
- Change time → verify data changes → evidence remains consistent
- Story claim → open citations → verify resolver success or policy-safe deny
- Open dataset → open receipt viewer → verify Valid/Verified state or “untrusted”
- Focus Mode question → citations present or abstain with reasons
- (If badges exist) verify automation status badge updates without leaking restricted details

---

## Security privacy and sensitivity

### Secrets and credentials
- Never ship secrets in the client.
- Prefer short-lived tokens scoped to least privilege.

### Evidence UI guardrails
- Validate evidence bundle shape before rendering derived UI.
- ReceiptViewer must be safe by construction:
  - validate schema before derived views
  - never render untrusted HTML
  - treat external links as hostile by default
- If an evidence object cannot be verified or resolved, render as **untrusted** and block publish paths.

### Sensitive locations and culturally restricted material
- Do not render exact coordinates in public UIs for vulnerable or restricted sites.
- Prefer generalization and show a governance note explaining why.

### Abstention and restriction UX
Abstention is a feature. The UI must:
- show policy-safe reasons
- suggest safe alternatives
- provide `audit_ref` for steward review
- avoid leaking restricted existence

---

## Add a new app

### Checklist
1. Create app directory (pick the repo convention):
   - `apps/<new-app>/README.md` **or** `web/apps/<new-app>/README.md`
   - `kfm.app.json` (or repo-standard manifest)
2. Define or extend API contract:
   - update OpenAPI or GraphQL or JSON Schema first
   - add fixtures and contract tests
3. Implement UI against governed APIs only:
   - no direct storage or DB access
   - evidence UX for every public layer or claim
4. Add tests:
   - unit, contract, E2E, accessibility, evidence resolution
   - receipt viewer safe-render tests if the app renders receipts
5. Register the app:
   - add row to [App registry](#app-registry)
6. Update this README:
   - regenerate “Current layout”
   - ensure the crosswalk reflects the chosen convention

---

## Glossary

- **Trust membrane:** enforced boundary where policy and provenance are applied; clients never access storage directly.
- **Truth path:** upstream → RAW → WORK or QUARANTINE → PROCESSED → catalogs and lineage → projections → governed API → UI.
- **Evidence-first UX:** every visible claim opens into provenance, rights, and validation details.
- **ReceiptViewer:** safe read-only receipt UI component; validates schema and surfaces verification status without executing untrusted content.
- **Trust badges:** compact UI affordances (e.g., automation status) that summarize provenance/quality without leaking restricted details.
- **Cite-or-abstain:** answers only when citations can be verified; otherwise abstain or reduce scope.
- **Canonical vs rebuildable:** artifacts, catalogs, and provenance are canonical; indexes are rebuildable projections.

---

<details>
<summary>Appendix: Updating this README without guessing</summary>

- Determine whether runnable apps live under `apps/` or `web/apps/`.
- Regenerate the Current layout block from the actual repo tree.
- Populate the App Registry table from real app directories.
- For each app, link to:
  - its contract references
  - its evidence UX entry points
  - its CI gates and test commands
- Resolve owners via CODEOWNERS and replace `TBD`.

</details>

<p align="right"><a href="#top">Back to top ↑</a></p>
