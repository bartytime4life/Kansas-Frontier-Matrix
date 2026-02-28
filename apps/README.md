<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8a4a8e59-7a6f-4d60-9c56-9f6d5f8b1f3d
title: apps/ — Runnable application surfaces
type: standard
version: v3.3
status: draft
owners: TBD (resolve via CODEOWNERS / repo maintainers)
created: 2026-02-22
updated: 2026-02-27
policy_label: public
related:
  - kfm://doc/kfm-definitive-design-governance-guide-vnext
  - kfm://doc/UNKNOWN_SYSTEM_OVERVIEW
  - ../README.md
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../CHANGELOG.md
  - ../.github/README.md
  - ../docs/
tags: [kfm, apps, ui, trust-membrane, contracts, evidence-first, receiptviewer, trust-badges, promotion-contract, threat-model, app-registry, view-state]
notes:
  - This README is intentionally fail-closed: it does not assume a specific tech stack or app list until confirmed in-repo.
  - First follow-up: populate the App Registry + Current layout blocks from the actual apps tree (either `apps/` or `web/apps/`, depending on repo convention).
  - v3.3 upgrade: add a machine-readable App Registry file recommendation + registry DoD.
  - v3.3 upgrade: align “Testing and gates” language with fail-closed required checks posture (anti-skip gate summary).
  - v3.3 upgrade: add trust-surface requirements matrix by app type (map/story/catalog/focus/admin/cli).
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# apps/ — Runnable application surfaces

**Purpose:** Home for user-facing and operator-facing application surfaces (Map / Globe / Story / Catalog / Focus / Admin / CLI) that consume **governed APIs** and expose **evidence-first** UX with **cite-or-abstain** guarantees.

**Owners:** TBD (resolve via CODEOWNERS / repo maintainers)  
**Status:** draft — **fail-closed** (repo-specific facts remain **UNKNOWN** until verified)  
**Policy label:** public (documentation only; individual apps may be `restricted|internal|secret`)

<!-- TODO(kfm): replace placeholder badges with real workflow badges once repo wiring is confirmed. -->

![status](https://img.shields.io/badge/status-draft-lightgrey)
![layer](https://img.shields.io/badge/layer-application%20surfaces-blue)
![northstars](https://img.shields.io/badge/north%20stars-map--first%20%7C%20time--aware%20%7C%20governed-informational)
![trust-membrane](https://img.shields.io/badge/governance-trust%20membrane-critical)
![promotion](https://img.shields.io/badge/promotion%20contract-fail--closed-critical)
![ux](https://img.shields.io/badge/UX-evidence--first-success)
![contracts](https://img.shields.io/badge/contracts-contract--first-important)
![ai](https://img.shields.io/badge/AI-focus%20mode%20cite--or--abstain-informational)
![anti-skip](https://img.shields.io/badge/gates-anti--skip%20summary-important)

> [!WARNING]
> This document is **fail-closed**. Anything repo-specific (actual app list, tooling, owners, contract paths, whether apps live in `apps/` or `web/apps/`) is **UNKNOWN** until verified in-repo.
> Do not “fill in the blanks” from memory.

---

## Navigation

- [Directory contract](#directory-contract)
- [Truth status legend](#truth-status-legend)
- [First follow-up checklist](#first-follow-up-checklist)
- [Where this fits in the repo](#where-this-fits-in-the-repo)
- [Repo layout crosswalk](#repo-layout-crosswalk)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Promotion Contract awareness](#promotion-contract-awareness)
- [Trust surfaces required](#trust-surfaces-required)
- [Evidence resolver expectations](#evidence-resolver-expectations)
- [Focus Mode UX contract](#focus-mode-ux-contract)
- [Threat model checklist](#threat-model-checklist)
- [Architecture sketch](#architecture-sketch)
- [App registry](#app-registry)
- [Directory layout](#directory-layout)
- [App manifest contract](#app-manifest-contract)
- [Per-app README minimum](#per-app-readme-minimum)
- [Local development](#local-development)
- [Testing and gates](#testing-and-gates)
- [Security, privacy, and sensitivity](#security-privacy-and-sensitivity)
- [Add a new app](#add-a-new-app)
- [Glossary](#glossary)

---

## Directory contract

This section is the directory-level “README contract” for `apps/`.

### Where it fits

`apps/` is a **surface-layer** directory. It sits at the end of the KFM layering model:

- **Domain** → concepts and invariants (no UI)
- **Use cases** → workflows (map/story/focus/admin)
- **Interfaces** → contracts + policy boundary (governed API, schemas)
- **Infrastructure** → storage/index, pipelines, CI
- **Apps** → UX that consumes governed APIs and makes trust + evidence visible

### Acceptable inputs

This folder is for **runnable applications**—anything a human launches (browser UI, operator console, desktop wrapper, CLI) whose job is **presenting governed KFM knowledge**.

Typical app categories (examples; verify actual apps in this repo):
- Map Explorer UI (2D map + timeline + evidence drawer + policy badges)
- Globe UI (optional 3D; same evidence constraints)
- Story UI (narrative + claim citations + view-state replay)
- Catalog UI (dataset discovery + version browsing)
- Focus Mode UI (governed Q&A with cite-or-abstain)
- Admin/Steward UI (intake review, promotion dashboards, policy fixtures review; usually restricted)
- CLI (operator workflows via governed APIs)

### Exclusions

The following do **not** belong in `apps/`:

- shared domain libraries used by multiple apps (move to the workspace’s shared packages area)
- shared UI components used by multiple apps (move to shared UI component space)
- data pipelines or long-running jobs (move to pipeline/workflow area)
- any direct storage/index access adapters
  - no DB drivers in browser code
  - no object-store clients in browser code
  - no “search index client in the UI” patterns
- policy engines or redaction logic
  - policy enforcement belongs in governed APIs and CI, not in clients
- receipt/attestation verification logic
  - clients may *display* verification results; verification occurs behind the trust membrane
- long-lived secrets or embedded credentials

> [!IMPORTANT]
> Shared libraries should **not** live here. Put shared code in the repo’s shared workspace (e.g., `packages/`, `web/packages/`, etc.) to prevent copy/paste drift.

---

## Truth status legend

This README uses explicit claim labels so it stays **evidence-first** and **fail-closed**:

- **CONFIRMED (design)**: a KFM north star / invariant / contract posture (treat as required)
- **UNKNOWN (repo)**: not yet verified in this repository (treat as TODO; do not assume)
- **PROPOSED**: a template/pattern you can adopt (validate before standardizing)

> [!NOTE]
> Repo-specific facts should graduate from **UNKNOWN → CONFIRMED (repo)** by attaching paths/snippets in PRs.

---

## First follow-up checklist

These steps convert this README from **UNKNOWN-heavy** to **repo-confirmed** without guessing.

### Repo facts to confirm

- [ ] Confirm where runnable UI surfaces live:
  - `ls -la apps/` **and** `ls -la web/apps/` (one may not exist)
- [ ] Capture at-a-glance trees:
  - `tree -L 3 apps/` (or `find apps -maxdepth 3 -type d`)
  - `tree -L 3 web/apps/` (or `find web/apps -maxdepth 3 -type d`)
- [ ] Identify the workspace/tooling boundary:
  - look for `package.json`, `pnpm-workspace.yaml`, `yarn.lock`, `turbo.json`, `nx.json`, `Cargo.toml`, `go.work`, etc.
- [ ] Resolve ownership:
  - inspect `CODEOWNERS` and any governance owners registry (if present)
- [ ] Locate contract surfaces consumed by apps:
  - search for `openapi`, `graphql`, `schema`, `contracts`, `sdk`, `client`, `generated`, `proto`
  - search for DCAT/STAC/PROV profile artifacts if stored in-repo (`dcat`, `stac`, `prov`)
- [ ] Locate trust UX components and their contract sources:
  - search for `EvidenceDrawer`, `ReceiptViewer`, `EvidenceRef`, `EvidenceBundle`, `run_receipt`, `promotion_manifest`
- [ ] Confirm policy labels and deny/abstain patterns in UI:
  - search for `policy_label`, `obligations`, `classification`, `redaction`, `abstain`, `deny`, `policy_safe`
- [ ] Confirm “policy-safe errors” posture:
  - search for `hide_restricted`, `not_found_forbidden`, `indistinguishable`, `policy_safe_error`

> [!TIP]
> Once verified, update only two sections first:
> 1) [App registry](#app-registry)  2) [Directory layout](#directory-layout)

---

## Where this fits in the repo

Some KFM repo layouts place runnable apps under `web/apps/` (with `web/` as the frontend workspace). If that’s true in your repo, treat this README as describing that subtree and consider either:

- moving this README to `web/apps/README.md` and leaving a short stub here, or
- keeping both copies with a single source-of-truth generator (preferred).

> [!PROPOSED]
> If you adopt “single source of truth,” store the canonical markdown in `docs/standards/apps.README.md` and generate `apps/README.md` and/or `web/apps/README.md` in CI.

---

## Repo layout crosswalk

This prevents “directory drift” when the repo uses `web/` as the frontend root.

> [!IMPORTANT]
> These are *layout patterns* (PROPOSED), not confirmations of your current repo state.

| Concept | Common location (root apps layout) | Common location (web layout) | What this means for this README |
|---|---|---|---|
| Runnable UI surfaces | `apps/<app>/` | `web/apps/<app>/` | Update “Current layout” + App Registry from whichever exists. |
| Shared UI packages | `packages/` | `web/packages/` | Keep shared code out of app folders. |
| Shared UI components | `packages/ui*/` | `web/src/components/` | Trust components should not be duplicated per app. |
| Contract schemas | `contracts/` or `schemas/` | `contracts/` or `schemas/` | Apps are contract consumers. |
| Governed API | `apps/api/` or `services/api/` | `apps/api/` or `services/api/` | Apps must not implement policy enforcement. |
| Governance policy | `policy/` | `policy/` | Policy is enforced by API + CI; apps display results. |
| CI gates | `.github/workflows/` | `.github/workflows/` | Apps are safety-critical: trust flows should be required checks. |

---

## Non-negotiable invariants

Apps are the most visible trust surface; breaking invariants breaks credibility. These invariants are **system-level** and apply to every app.

### 1) Truth path lifecycle (KFM north star)

- Apps sit at the end of the truth path:
  - upstream → RAW → WORK / QUARANTINE → PROCESSED → CATALOG/TRIPLET (DCAT + STAC + PROV + receipts) → projections → governed API → apps
- Apps **MUST** assume only *promoted* DatasetVersions are admissible for public surfaces.
- Apps **MUST NOT** use “floating latest” as a substitute for versioned IDs in share links, exports, or Story Nodes.

### 2) Trust membrane (KFM north star)

- Apps **MUST NOT** access object storage, databases, or internal indexes directly.
- Apps **MUST** consume data only through **governed APIs** that enforce policy, obligations/redactions, and logging.
- Apps **MUST NOT** embed credentials that could bypass governance.

### 3) Evidence-first UX (KFM north star)

Every layer, story claim, chart, or AI output **MUST** open into an **evidence view**:

- DatasetVersion ID and human name
- License and rights holder attribution (copyable)
- Policy label and obligations/redactions applied
- Provenance chain and run receipt reference
- Validation and freshness indicators (policy-safe)
- Evidence bundle digest/checksum (when policy allows)

### 4) Cite-or-abstain Focus Mode (KFM north star)

If Focus Mode exists, it **MUST** implement cite-or-abstain:

- If citations can’t be verified, the UI **MUST** abstain or reduce scope and show why (policy-safe).
- If policy denies, the UI **MUST** deny and explain in policy-safe terms.
- Every Focus response **MUST** link to an `audit_ref` (run id) for review.

### 5) Canonical vs rebuildable stores (KFM north star)

- Canonical truth lives in: artifacts + catalogs + run receipts + audit ledger.
- Apps **MUST** treat DB/search/tiles/graph as rebuildable projections, not source-of-truth.
- Apps **MUST** display DatasetVersion identity and evidence links that tie projections back to canonical artifacts.

### 6) Deterministic identity and hashing (KFM north star)

- DatasetVersion identity is stable and derived deterministically (spec-hash posture).
- Apps **MUST** use stable IDs in URLs/share links/view_state and avoid “version drift.”
- Apps **SHOULD** surface spec-hash/digest identifiers where policy allows.

---

## Promotion Contract awareness

> [!IMPORTANT]
> Promotion gates are enforced in pipelines/CI and the governed API — but apps must not become a bypass.

UI implications:

- Apps **MUST** show only promoted DatasetVersions on public surfaces.
- Apps **MUST** render “untrusted / not promotable” states safely:
  - missing receipt
  - missing catalogs
  - unresolvable evidence
  - policy engine degraded
- Apps **MUST** treat missing/invalid evidence as a reason to **degrade**, not as permission to render anyway.
- Any export/download UX **MUST** be checked against policy label + license/rights, and must be policy-safe (no restricted existence inference).

---

## Trust surfaces required

These are not optional polish. They are the user-visible governance contract.

### Trust-surface requirements by app type

> [!NOTE]
> This is **CONFIRMED (design)** as a target posture. Confirm exact implementations in-repo.

| App type | Evidence Drawer | DatasetVersion + Policy badges | ReceiptViewer | Provenance panel | What-changed (versions) | Exports gated by policy/rights |
|---|---:|---:|---:|---:|---:|---:|
| Map Explorer | ✅ MUST | ✅ MUST | ✅ SHOULD | ✅ SHOULD | ✅ SHOULD | ✅ MUST |
| Story | ✅ MUST (claim-level) | ✅ MUST | ✅ SHOULD | ✅ SHOULD | ✅ SHOULD | ✅ MUST |
| Catalog | ✅ SHOULD | ✅ MUST | ✅ SHOULD | ✅ SHOULD | ✅ MAY | ✅ MUST (if exports exist) |
| Focus | ✅ MUST (citations) | ✅ MUST | ✅ SHOULD | ✅ MUST (audit_ref/receipt) | ✅ MAY | ✅ MUST (if exports exist) |
| Admin/Steward | ✅ MUST | ✅ MUST | ✅ MUST | ✅ MUST | ✅ SHOULD | ✅ MUST |
| CLI | N/A | N/A | ✅ SHOULD (read) | ✅ SHOULD | ✅ MAY | ✅ MUST (server-side) |

### Evidence drawer minimum fields

- Evidence bundle ID and digest
- DatasetVersion ID and dataset name
- License and rights holder attribution
- Validation status + QA summary (policy-safe)
- Provenance chain link to run receipt
- Obligations/redactions applied
- Policy-safe access messaging (deny/abstain states)

> [!WARNING]
> Evidence UX must never become a data exfiltration path. “Evidence exists” must not leak restricted existence unless policy allows acknowledging existence.

---

## Evidence resolver expectations

Evidence resolution is a **contract surface** (not a best-effort UI feature).

- Apps **MUST** treat the evidence resolver as authoritative for citations/evidence bundles.
- Apps **SHOULD** be able to fetch/render an EvidenceBundle in **≤ 2 calls** (e.g., resolve → fetch bundle), otherwise degrade safely.
- Apps **MUST** fail closed:
  - if evidence is unresolvable → show “untrusted” / abstain
  - if policy denies → show deny UX (policy-safe)

> [!NOTE]
> Do not build DIY citations in clients. EvidenceRefs must resolve to EvidenceBundles.

---

## Focus Mode UX contract

If Focus Mode exists, it must behave like a governed run, not chat.

**Inputs**
- user query
- optional view_state (map bbox, time window, active layers)
- user role + policy context

**Outputs**
- answer text
- citations (EvidenceRefs) resolvable to EvidenceBundles
- audit_ref (run id) for review

### Control loop (required posture)

1) Policy pre-check  
2) Retrieval plan (based on view_state + intent)  
3) Retrieve admissible evidence (catalog/search/graph/projections)  
4) Build EvidenceBundles via evidence resolver (apply obligations)  
5) Synthesize answer referencing bundles  
6) **Citation verification (HARD GATE)** — if any citation fails or is denied, revise or abstain  
7) Emit run receipt (query + bundle digests + decisions + output hash)

### Evaluation harness (release posture)

For broad release, Focus Mode **SHOULD** be gated by an evaluation harness:

- citation coverage (claims supported)
- citation resolvability (100% for allowed users)
- refusal correctness (restricted prompts denied safely)
- sensitivity leakage tests (no restricted coordinates/metadata)
- golden queries across DatasetVersions (regression gate)

---

## Threat model checklist

Use this checklist when reviewing new app features (especially exports, sharing, search, and AI).

- TM-001 **Trust membrane:** Does the frontend ever fetch directly from object storage or databases? **Expected: NO**
- TM-002 **Restricted inference:** Can a public user infer restricted dataset existence via errors, timing, caching, or empty states? **Expected: NO**
- TM-003 **Exports:** Are downloads/exports checked against policy labels and rights? **Expected: YES**
- TM-004 **Caching:** Can tiles/search results leak across roles due to shared caches? **Expected: NO**
- TM-005 **Focus injection:** Can retrieved content prompt-inject the system into policy bypass? **Expected: mitigated**
- TM-006 **Audit data safety:** Are audit logs redacted and access-controlled (PII safety)? **Expected: YES**
- TM-007 **Credential scope:** Are tokens short-lived and least-privilege? **Expected: YES**
- TM-008 **Artifact immutability:** Are rendered artifacts immutable-by-digest where applicable? **Expected: YES**
- TM-009 **UI trust flows tested:** Are evidence/deny/abstain flows covered by E2E tests? **Expected: YES**

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

  Apps --> API["Governed API"]
  API --> Policy["Policy engine"]
  API --> Evidence["Evidence resolver"]
  API --> CatalogTriplet["Catalog triplet DCAT STAC PROV"]
  API --> Projections["Rebuildable projections (DB/search/tiles/graph)"]
  CatalogTriplet --> Canonical["Canonical artifacts + receipts + audit"]
  Projections --> Canonical
```

### Evidence-first interaction sketch

```mermaid
sequenceDiagram
  participant U as User
  participant A as App
  participant G as Governed API
  participant P as Policy
  participant E as Evidence Resolver

  U->>A: Toggle layer / open claim / ask Focus
  A->>G: Request data + EvidenceRefs
  G->>P: Evaluate policy + obligations
  G->>E: Resolve EvidenceBundles (policy-applied)
  E-->>G: Bundles + digests + audit refs
  G-->>A: Payload + citations + policy labels
  A-->>U: Render + EvidenceDrawer + deny/abstain when needed
```

---

## App registry

> [!IMPORTANT]
> Populate this from the **actual** apps tree:
> - either `apps/*` **or** `web/apps/*`
> - do not assume both exist

### App registry table (human)

| App path | Type | Primary surface | Policy label | Primary contract references | Owner | Status |
|---|---|---|---|---|---|---|
| `TBD` | web / desktop / cli / other | map / globe / story / catalog / focus / admin / ops | public / restricted / internal | `TBD` | `TBD` | draft |
| `TBD` |  |  |  |  |  |  |

### Machine-readable App Registry (PROPOSED)

Keep the canonical registry in a small JSON file that CI can validate:

- `apps/registry/apps.v1.json` **or** `web/apps/registry/apps.v1.json` (choose one based on repo convention)

Template:

```json
{
  "kfm_app_registry_version": "v1",
  "updated": "2026-02-27",
  "apps": [
    {
      "app_id": "kfm.app.map",
      "path": "apps/map",
      "surface": "map",
      "policy_label": "public",
      "owners": ["@kfm-engineering"],
      "contracts": ["contracts/openapi/api.yaml#tag=tiles", "contracts/openapi/api.yaml#tag=evidence"],
      "trust_surfaces": ["evidence_drawer", "receipt_viewer", "provenance_panel"],
      "capabilities": { "view_state": true, "exports": ["png"], "focus_mode": false }
    }
  ]
}
```

### Registry definition of done

- [ ] Every app has a one-line purpose (README).
- [ ] Every app declares `policy_label` (and any restrictions).
- [ ] Every app lists governed API contract references (OpenAPI/GraphQL/schema URIs/paths).
- [ ] Every public surface declares its trust surfaces (EvidenceDrawer/ReceiptViewer/provenance/what-changed).
- [ ] Every map/story/focus surface declares whether it supports reproducible `view_state`.
- [ ] Owners resolved via `CODEOWNERS` and/or registry.

---

## Directory layout

### Current layout (UNKNOWN until verified)

Replace the block below with the real tree output (choose the directory that exists).

```text
apps/ or web/apps/
├─ README.md
└─ TBD
```

### Recommended layout template (apps-at-root)

Use only if the repo does not already enforce a different convention.

```text
apps/                                                            | # App surfaces (UI + services) + governed registry
├─ README.md                                                     | # Directory contract + App Registry index (human-readable)
│
├─ registry/                                                     | # Machine-readable app inventory + CI validation fixtures
│  ├─ README.md                                                  | # Registry purpose + DoD + CI validation rules
│  ├─ apps.v1.json                                               | # Canonical App Registry (names, owners, policy labels, capabilities)
│  ├─ fixtures/                                                  | # CI fixtures (no secrets; policy-safe)
│  │  ├─ apps.v1.minimal.json                                    | # Smallest valid registry example
│  │  └─ apps.v1.invalid.examples.json                           | # Intentionally invalid cases for fail-closed validation
│  └─ _generated/                                                | # ⚠️ Generated snapshots (gitignored or policy-committed)
│     └─ manifests.index.json                                    | # Optional flattened index from per-app manifests
│
├─ api/                                                          | # ✅ Governed API (runtime trust membrane / PEP)
│  ├─ README.md                                                  | # Service overview, run/dev, contracts, policy, observability
│  ├─ kfm.app.json                                               | # ✅ App manifest (policy_label, contracts, capabilities)
│  ├─ Dockerfile                                                 | # ⚠️ If deploying as a container
│  ├─ src/                                                       | # API source
│  │  ├─ server.ts                                               | # Service bootstrap (HTTP server wiring)
│  │  ├─ api/                                                    | # HTTP boundary (routes + middleware)
│  │  │  ├─ routes/                                              | # Route modules (thin handlers)
│  │  │  │  ├─ catalog.ts                                        | # /api/v1/datasets + registry endpoints (WP-05)
│  │  │  │  ├─ evidence.ts                                       | # EvidenceRef -> EvidenceBundle (WP-04)
│  │  │  │  ├─ stories.ts                                        | # Story publish/read (WP-07)
│  │  │  │  ├─ tiles.ts                                          | # Policy-safe tiles (rendering-safe map tiles)
│  │  │  │  └─ focus.ts                                          | # Focus Mode ask orchestration boundary (WP-08)
│  │  │  └─ middleware/                                          | # Cross-cutting HTTP concerns (auth/policy/audit/errors)
│  │  │     ├─ auth.ts                                           | # Authentication + session extraction
│  │  │     ├─ policy.ts                                         | # PEP policy checks (allow/deny + obligations)
│  │  │     ├─ audit.ts                                          | # Audit event emission hooks (request/decision receipts)
│  │  │     └─ errors.ts                                         | # Policy-safe error mapping (no leakage)
│  │  ├─ services/                                               | # Usecase implementations (business logic; policy-aware)
│  │  │  ├─ evidence_resolver.ts                                 | # Evidence resolution + bundle assembly
│  │  │  ├─ catalog_registry.ts                                  | # Dataset discovery + registry-backed listings
│  │  │  ├─ story_publisher.ts                                   | # Story publish flow with citation resolution
│  │  │  └─ focus_orchestrator.ts                                | # Focus ask flow (cite-or-abstain handshake)
│  │  └─ adapters/                                               | # IO + external systems (stores, databases, PDP)
│  │     ├─ object_store.ts                                      | # Object storage adapter (S3/GCS/FS; policy-safe paths)
│  │     ├─ postgis.ts                                           | # PostGIS adapter (spatial storage/query)
│  │     ├─ search.ts                                            | # Search adapter (index/query)
│  │     ├─ graph.ts                                             | # Graph adapter (lineage/provenance queries)
│  │     └─ opa.ts                                               | # OPA/PDP adapter (decision + obligations)
│  └─ tests/                                                     | # Service tests (policy + contracts + integration)
│     ├─ integration/                                            | # API/service integration tests (adapters + policy)
│     └─ contract/                                               | # OpenAPI/DTO compatibility tests (backward-compat gates)
│
├─ map/                                                          | # Map Explorer UI (map-first browse + inspect + export)
│  ├─ README.md                                                  | # ✅ App README (purpose, contracts, trust surfaces, run, tests)
│  ├─ kfm.app.json                                               | # ✅ App manifest (policy_label, contracts, capabilities)
│  ├─ Dockerfile                                                 | # ⚠️ If containerized
│  ├─ public/                                                    | # ⚠️ Static assets (icons, fonts). No secrets.
│  │  ├─ icons/                                                  | # App icons (safe to publish)
│  │  └─ branding/                                               | # Brand assets (safe to publish)
│  └─ src/                                                       | # UI source
│     ├─ main.*                                                  | # ✅ App entrypoint (framework-specific)
│     ├─ app.*                                                   | # ✅ Root shell (routing/layout)
│     ├─ routes/                                                 | # Route-level screens + error boundaries
│     │  ├─ index.*                                              | # Landing / default map view
│     │  ├─ layer.*                                              | # Layer browsing/config routes
│     │  ├─ dataset.*                                            | # Dataset details / open-in-map routes
│     │  └─ error.*                                              | # Policy-safe error boundary (no leakage)
│     ├─ config/                                                 | # Runtime config (read-only env + build metadata)
│     │  ├─ env.*                                                | # Reads KFM_API_BASE_URL, KFM_ENV, etc.
│     │  ├─ featureFlags.*                                       | # UI toggles only (no policy bypass)
│     │  └─ buildInfo.*                                          | # Version/build metadata for trust badges
│     ├─ adapters/                                               | # ✅ Governed API clients + DTO mapping (no direct DB)
│     │  ├─ apiClient.*                                          | # Base HTTP client (headers, retries, tracing)
│     │  ├─ catalogApi.*                                         | # Catalog endpoints client
│     │  ├─ tilesApi.*                                           | # Tiles endpoints client
│     │  ├─ queryApi.*                                           | # Query/search endpoints client
│     │  ├─ evidenceApi.*                                        | # Evidence resolve endpoints client
│     │  └─ auditApi.*                                           | # Audit endpoints client (write-only where appropriate)
│     ├─ trust/                                                  | # ✅ Trust membrane UX components (evidence, receipts, deny/abstain)
│     │  ├─ EvidenceDrawer/                                      | # Evidence Drawer UI + bundle presentation
│     │  │  ├─ EvidenceDrawer.*                                  | # Drawer container + state orchestration
│     │  │  ├─ EvidenceBundleCard.*                              | # Bundle summary card (hashes, sources, completeness)
│     │  │  ├─ LicenseAttribution.*                              | # License + attribution rendering (policy-safe)
│     │  │  ├─ PolicyBadge.*                                     | # Policy label + obligations badge rendering
│     │  │  └─ UntrustedEvidence.*                               | # Untrusted/missing evidence UX (abstain posture)
│     │  ├─ ReceiptViewer/                                       | # Run receipt + audit receipt viewing
│     │  │  ├─ ReceiptViewer.*                                   | # Receipt renderer
│     │  │  ├─ ReceiptSchemaValidate.*                           | # Client-side validation of receipt shape (defensive)
│     │  │  └─ UnverifiedReceipt.*                               | # UX for invalid/unverified receipts
│     │  ├─ TrustBadges/                                         | # Inline trust signals (freshness/validation/version)
│     │  │  ├─ DatasetVersionBadge.*                             | # Dataset/version identifiers
│     │  │  ├─ ValidationBadge.*                                 | # Validation status (schema/profile)
│     │  │  └─ FreshnessBadge.*                                  | # Freshness/updated-at surfaces
│     │  └─ DenyAbstain/                                         | # Allow/deny/abstain UX flows + access requests
│     │     ├─ PolicyDenyPanel.*                                 | # Deny reason + obligations display
│     │     ├─ AbstainPanel.*                                    | # Abstain reason + next steps
│     │     └─ RequestAccessPanel.*                              | # Access request UX (policy-compliant)
│     ├─ map/                                                    | # 🧩 Map-specific modules (engine/layers/timeline/inspect/exports)
│     │  ├─ engine/                                              | # Map engine primitives (canvas, camera, interaction)
│     │  │  ├─ MapCanvas.*                                       | # Map rendering surface
│     │  │  ├─ CameraState.*                                     | # Camera state + transitions
│     │  │  └─ Interaction.*                                     | # Input handling (click/drag/hover)
│     │  ├─ layers/                                              | # Layer registry + styling + state
│     │  │  ├─ layerRegistry.*                                   | # Catalog → layer mapping (governed)
│     │  │  ├─ styleAdapters.*                                   | # Style mapping (tokenized, policy-safe)
│     │  │  └─ layerState.*                                      | # Layer visibility/opacity/order state
│     │  ├─ timeline/                                            | # Time-aware exploration (valid vs transaction time)
│     │  │  ├─ TimeSlider.*                                      | # Timeline UI control
│     │  │  ├─ ValidVsTransactionTime.*                          | # Semantics + UI toggles
│     │  │  └─ TimeWindowState.*                                 | # State model for time windows
│     │  ├─ inspect/                                             | # Inspect flows → evidence flows
│     │  │  ├─ FeatureInspectPanel.*                             | # Inspect UI for selected features
│     │  │  ├─ OnClickEvidenceRef.*                              | # Click → EvidenceRef creation
│     │  │  └─ InspectToEvidenceFlow.*                           | # Inspect → drawer orchestration
│     │  └─ exports/                                             | # Export workflows (policy notices + requests)
│     │     ├─ ExportPanel.*                                     | # Export UI (format/extent options)
│     │     ├─ ExportPolicyNotice.*                              | # Policy + obligations notice for exports
│     │     └─ ExportRequests.*                                  | # Export request submission + status
│     ├─ view_state/                                             | # Shareable view state (encode/decode/normalize)
│     │  ├─ ViewStateSchema.*                                    | # View state schema/typing
│     │  ├─ encodeViewState.*                                    | # State → URL/token
│     │  ├─ decodeViewState.*                                    | # URL/token → state
│     │  └─ normalizeViewState.*                                 | # Canonicalization + drift protection
│     ├─ components/                                             | # App-shell components (layout + nav + panels)
│     │  ├─ Layout.*                                             | # Global layout container
│     │  ├─ TopNav.*                                             | # Top navigation bar
│     │  ├─ SidePanel.*                                          | # Side panel scaffolding
│     │  └─ LoadingErrorStates.*                                 | # Standard loading/error surfaces (policy-safe)
│     ├─ state/                                                  | # Client state management (store/selectors/persistence)
│     │  ├─ store.*                                              | # Store setup
│     │  ├─ selectors.*                                          | # Derived selectors (stable, tested)
│     │  └─ persistence.*                                        | # Persisted state (policy-safe keys only)
│     ├─ telemetry/                                              | # Client telemetry (otel + analytics + redaction)
│     │  ├─ otel.*                                               | # OpenTelemetry wiring (if used)
│     │  ├─ analytics.*                                          | # Product analytics (policy-safe)
│     │  └─ redaction.*                                          | # Client-side redaction hooks/guards
│     └─ tests/                                                  | # App tests (fast + integration + e2e)
│        ├─ unit/                                                | # Pure UI/unit tests (deterministic)
│        ├─ integration/                                         | # UI+API client integration tests (mocked boundaries)
│        └─ e2e/                                                 | # End-to-end tests (runner-dependent)
│
├─ story/                                                        | # Story Mode UI (publish/read narratives with citations)
│  ├─ README.md                                                  | # App overview + run + trust surfaces
│  ├─ kfm.app.json                                               | # App manifest (policy label, capabilities)
│  ├─ Dockerfile                                                 | # ⚠️ If containerized
│  ├─ public/                                                    | # ⚠️ Static assets (safe)
│  └─ src/                                                       | # UI source
│     ├─ main.*                                                  | # App entrypoint
│     ├─ app.*                                                   | # Root shell (routing/layout)
│     ├─ routes/                                                 | # Pages/routes (policy-safe errors)
│     │  ├─ index.*                                              | # Landing / story list
│     │  ├─ story.*                                              | # Story reader
│     │  ├─ claim.*                                              | # Claim view / citation drilldown
│     │  └─ error.*                                              | # Error boundary (no leakage)
│     ├─ adapters/                                               | # Governed API clients
│     │  ├─ apiClient.*                                          | # Base client
│     │  ├─ storiesApi.*                                         | # Story endpoints client
│     │  ├─ evidenceApi.*                                        | # Evidence resolve client
│     │  └─ auditApi.*                                           | # Audit events client
│     ├─ trust/                                                  | # Trust membrane UX (same structure as map)
│     ├─ stories/                                                | # Story rendering + review tooling
│     │  ├─ renderer/                                            | # Markdown rendering (safe mode)
│     │  ├─ citations/                                           | # Citation components + linking
│     │  ├─ sidecar/                                             | # Sidecar metadata + evidence refs
│     │  ├─ playback/                                            | # Playback controls (timeline/steps)
│     │  └─ review/                                              | # Review UI (policy, citation completeness)
│     ├─ view_state/                                             | # View state encoding/decoding (shareable)
│     └─ tests/                                                  | # Tests
│        ├─ unit/                                                | # Unit tests
│        ├─ integration/                                         | # Integration tests
│        └─ e2e/                                                 | # End-to-end tests
│
├─ catalog/                                                      | # Catalog UI (browse datasets, versions, lineage; evidence-backed)
│  ├─ README.md                                                  | # App overview + run + contracts + evidence UX
│  ├─ kfm.app.json                                               | # App manifest
│  ├─ Dockerfile                                                 | # ⚠️ If containerized
│  ├─ public/                                                    | # ⚠️ Static assets (safe)
│  └─ src/                                                       | # UI source
│     ├─ main.*                                                  | # App entrypoint
│     ├─ app.*                                                   | # Root shell
│     ├─ routes/                                                 | # Pages/routes
│     │  ├─ index.*                                              | # Dataset list/search
│     │  ├─ dataset.*                                            | # Dataset details
│     │  ├─ version.*                                            | # Dataset version view/compare
│     │  ├─ lineage.*                                            | # Lineage view (policy-gated)
│     │  └─ error.*                                              | # Error boundary (no leakage)
│     ├─ adapters/                                               | # Governed API clients + DTO mapping
│     │  ├─ apiClient.*                                          | # Base client
│     │  ├─ catalogApi.*                                         | # Catalog endpoints
│     │  ├─ evidenceApi.*                                        | # Evidence endpoints
│     │  └─ auditApi.*                                           | # Audit endpoints
│     ├─ trust/                                                  | # Trust membrane UX components
│     ├─ catalog_ui/                                             | # Catalog-specific UI modules
│     │  ├─ search/                                              | # Search UI + filters
│     │  ├─ datasetCards/                                        | # Dataset cards/listing tiles
│     │  ├─ versionCompare/                                      | # Version diff/compare UI
│     │  └─ licenseRights/                                       | # License/rights display modules
│     └─ tests/                                                  | # Tests
│        ├─ unit/                                                | # Unit tests
│        ├─ integration/                                         | # Integration tests
│        └─ e2e/                                                 | # End-to-end tests
│
├─ focus/                                                        | # Focus Mode UI (ask → cite-or-abstain answers + audit)
│  ├─ README.md                                                  | # App overview + run + safety + citations
│  ├─ kfm.app.json                                               | # App manifest
│  ├─ Dockerfile                                                 | # ⚠️ If containerized
│  ├─ public/                                                    | # ⚠️ Static assets (safe)
│  └─ src/                                                       | # UI source
│     ├─ main.*                                                  | # App entrypoint
│     ├─ app.*                                                   | # Root shell
│     ├─ routes/                                                 | # Pages/routes
│     │  ├─ index.*                                              | # Composer landing
│     │  ├─ session.*                                            | # Session view (question/answer/citations)
│     │  └─ error.*                                              | # Error boundary (no leakage)
│     ├─ adapters/                                               | # Governed API clients
│     │  ├─ apiClient.*                                          | # Base client
│     │  ├─ focusApi.*                                           | # Focus ask endpoints
│     │  ├─ evidenceApi.*                                        | # Evidence resolve endpoints
│     │  └─ auditApi.*                                           | # Audit endpoints
│     ├─ trust/                                                  | # Trust membrane UX components
│     ├─ focus_ui/                                               | # Focus-specific UI modules
│     │  ├─ composer/                                            | # Prompt composer
│     │  ├─ answer/                                              | # Answer view (abstain/allow)
│     │  ├─ citations/                                           | # Citation list + drilldowns
│     │  ├─ abstain/                                             | # Abstain UX + next steps
│     │  ├─ audit/                                               | # Audit/receipt surfaces
│     │  └─ safety/                                              | # Safety notices + policy badge surfaces
│     ├─ view_state/                                             | # Shareable state for sessions
│     └─ tests/                                                  | # Tests
│        ├─ unit/                                                | # Unit tests
│        ├─ integration/                                         | # Integration tests
│        └─ e2e/                                                 | # End-to-end tests
│
├─ admin/                                                        | # Admin/Steward UI (review, promote, audit, policy fixtures)
│  ├─ README.md                                                  | # App overview + governance + run + tests
│  ├─ kfm.app.json                                               | # App manifest
│  ├─ Dockerfile                                                 | # ⚠️ If containerized
│  ├─ public/                                                    | # ⚠️ Static assets (safe)
│  └─ src/                                                       | # UI source
│     ├─ main.*                                                  | # App entrypoint
│     ├─ app.*                                                   | # Root shell
│     ├─ routes/                                                 | # Admin screens
│     │  ├─ index.*                                              | # Admin landing/dashboard
│     │  ├─ reviewQueue.*                                        | # Review queue workflows
│     │  ├─ promotion.*                                          | # Promotion workflows + gates
│     │  ├─ policyFixtures.*                                     | # Policy fixture views/tools (governed)
│     │  ├─ receipts.*                                           | # Receipt browsing/validation
│     │  └─ error.*                                              | # Error boundary (no leakage)
│     ├─ adapters/                                               | # Governed API clients
│     │  ├─ apiClient.*                                          | # Base client
│     │  ├─ adminApi.*                                           | # Admin endpoints
│     │  ├─ policyApi.*                                          | # Policy/PDP endpoints (fixtures/decisions)
│     │  ├─ auditApi.*                                           | # Audit endpoints
│     │  └─ evidenceApi.*                                        | # Evidence endpoints
│     ├─ trust/                                                  | # Trust membrane UX components
│     ├─ admin_ui/                                               | # Admin-specific UI modules
│     │  ├─ approvals/                                           | # Approval UX + reviewers
│     │  ├─ gateStatus/                                          | # Gate status dashboards
│     │  ├─ quarantine/                                          | # Quarantine workflows
│     │  ├─ lineage/                                             | # Lineage tools/surfaces
│     │  └─ audit/                                               | # Audit views (events/receipts)
│     └─ tests/                                                  | # Tests
│        ├─ unit/                                                | # Unit tests
│        ├─ integration/                                         | # Integration tests
│        └─ e2e/                                                 | # End-to-end tests
│
└─ cli/                                                          | # CLI surface (operator tooling; policy-aware)
   ├─ README.md                                                  | # CLI usage + commands + examples
   ├─ kfm.app.json                                               | # CLI manifest (capabilities, contracts)
   ├─ bin/                                                       | # Launchers/wrappers
   │  └─ kfm                                                     | # Wrapper script/binary launcher
   ├─ completions/                                               | # Shell completions
   │  ├─ kfm.bash                                                | # Bash completion
   │  └─ _kfm                                                    | # Zsh completion
   └─ src/                                                       | # CLI source
      ├─ main.*                                                  | # CLI entrypoint
      ├─ config/                                                 | # Config + profiles
      │  ├─ env.*                                                | # Env parsing (KFM_API_BASE_URL, auth, etc.)
      │  └─ profiles.*                                           | # Named profiles (safe defaults; no secrets committed)
      ├─ adapters/                                               | # Governed API clients (no direct DB)
      │  ├─ apiClient.*                                          | # Base client
      │  ├─ evidenceApi.*                                        | # Evidence endpoints
      │  ├─ catalogApi.*                                         | # Catalog endpoints
      │  ├─ promoteApi.*                                         | # Promotion endpoints
      │  ├─ auditApi.*                                           | # Audit endpoints
      │  └─ exportApi.*                                          | # Export endpoints
      ├─ commands/                                               | # Command groups (subcommands)
      │  ├─ catalog/                                             | # Catalog-related commands
      │  ├─ evidence/                                            | # Evidence-related commands
      │  ├─ receipts/                                            | # Receipt/audit commands
      │  ├─ promote/                                             | # Promotion commands
      │  ├─ validate/                                            | # Validation commands (schemas/profiles)
      │  └─ focus/                                               | # Focus ask commands
      ├─ output/                                                 | # Output formats + redaction helpers
      │  ├─ json.*                                               | # JSON output
      │  ├─ table.*                                              | # Table output
      │  └─ redact.*                                             | # Redaction helpers (policy-safe)
      ├─ telemetry/                                              | # CLI telemetry (optional; policy-safe)
      └─ tests/                                                  | # CLI tests
         ├─ unit/                                                | # Unit tests
         └─ integration/                                         | # Integration tests (mocked boundaries)
```

### Recommended layout template (web/apps)

If your repo uses a `web/` workspace root:

```text
web/
├─ apps/
│  ├─ README.md
│  ├─ registry/
│  │  └─ apps.v1.json
│  ├─ map/
│  ├─ story/
│  ├─ catalog/
│  ├─ focus/
│  └─ admin/
└─ packages/                                   # Shared UI packages (do not duplicate per-app)
```

---

## App manifest contract

Each app directory **SHOULD** include an app manifest file (example: `kfm.app.json`) so governance intent is machine-readable.

> [!NOTE]
> If the repo already has a standard manifest, use that instead. This is a PROPOSED contract.

### Example kfm.app.json

```json
{
  "app_id": "kfm.app.map",
  "name": "KFM Map Explorer",
  "surface": "map",
  "policy_label": "public",
  "capabilities": {
    "view_state": true,
    "exports": ["png"],
    "focus_mode": false
  },
  "governed_api": {
    "base_url_env": "KFM_API_BASE_URL",
    "contracts": [
      "openapi://contracts/openapi/api.yaml#tag=catalog",
      "openapi://contracts/openapi/api.yaml#tag=tiles",
      "openapi://contracts/openapi/api.yaml#tag=evidence"
    ]
  },
  "trust_surfaces": ["evidence_drawer", "receipt_viewer", "provenance_panel", "what_changed"],
  "telemetry": {
    "otel": true,
    "pii": "none"
  }
}
```

### Minimal manifest rules (PROPOSED)

- `policy_label` is mandatory.
- `governed_api.contracts` is mandatory for any app that makes API calls.
- `trust_surfaces` is mandatory for any public-facing surface that renders layers or claims.
- `capabilities.view_state = true` SHOULD be set for Map/Story/Focus surfaces that emit share links.

---

## Per-app README minimum

Each app under `apps/<app>/` or `web/apps/<app>/` SHOULD include a README that answers:

- title and one-line purpose
- where it fits in the system
- acceptable inputs
- exclusions
- governed API contracts used
- trust surfaces (EvidenceDrawer, ReceiptViewer, provenance, what-changed)
- view_state expectations (if applicable)
- how to run locally
- tests and CI gates
- threat model notes for exports/share/search/AI features

### Template header snippet

```md
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: apps/<app>/ — <purpose>
type: standard
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - ../README.md
tags: [kfm, apps]
notes:
  - Keep repo-unknowns explicit until verified.
[/KFM_META_BLOCK_V2] -->
```

---

## Local development

> [!IMPORTANT]
> This section is intentionally generic until the repo’s tooling is verified.

### Quick start pattern

1. Identify the workspace toolchain from repo root (and whether frontend is rooted at `web/`).
2. Install dependencies using the repo’s chosen package manager.
3. Run the app’s dev target from its directory.
4. Confirm it points to a **governed API** instance (not direct storage/DB).

### Proposed environment variables

- `KFM_API_BASE_URL` — base URL for the governed API gateway
- `KFM_ENV` — `local|dev|stage|prod`

> [!WARNING]
> Apps must be safe under policy deny. Even if UI misconfigures itself, restricted content must not render because enforcement occurs in the API.

---

## Testing and gates

Apps are safety-critical surfaces. Treat app changes like production changes.

### Minimum CI gates (recommended baseline)

- [ ] unit tests for UI + adapters
- [ ] contract checks for governed API compatibility (OpenAPI/GraphQL/schema)
- [ ] evidence resolution smoke test (EvidenceRef → EvidenceBundle) in CI
- [ ] ReceiptViewer safe-render tests (schema validate + “untrusted” fallback)
- [ ] E2E tests for critical trust flows (below)
- [ ] accessibility checks (EvidenceDrawer keyboard navigation at minimum)
- [ ] dependency and supply chain checks
- [ ] static guardrail: **no direct storage/DB access** from apps
- [ ] policy-safe errors guardrail (no restricted existence inference)

### Anti-skip requirement (merge posture)

> [!WARNING]
> A required app gate must not be skippable via `paths:` filters, `if:` conditions, or job fanout.
> Prefer a single always-runs **gate-summary** job as the required check (see `../.github/README.md` if present).

### Recommended E2E trust flows

- load app → toggle a layer → open EvidenceDrawer → verify policy label + DatasetVersion shown
- change time window → verify results change → evidence remains version-pinned
- open a story claim → open citations → resolver success or policy-safe deny
- open receipt viewer → verified/untrusted renders safely
- ask a Focus question → citations present or abstain with reasons + audit_ref
- attempt export → policy + rights enforced; policy-safe errors; no restricted inference

### Static guardrail examples (PROPOSED)

Because tech stacks vary, the implementation varies. The invariant does not: **apps cannot bypass governed APIs**.

Possible approaches:
- dependency allow/deny list in CI (fail if an app depends on DB/object-store/index client SDKs)
- linter rules blocking direct calls to non-governed origins (where applicable)
- egress policy in dev/stage to prevent direct access to internal stores from UI origins
- targeted grep checks for known bypass libraries (tune to avoid false positives)

---

## Security, privacy, and sensitivity

### Secrets and credentials
- Never ship secrets in clients.
- Prefer short-lived tokens scoped to least privilege.
- Do not log tokens or sensitive request payloads.

### Evidence UI guardrails

- validate evidence bundle shape before rendering derived UI
- ReceiptViewer must be safe by construction:
  - validate schema before derived views
  - never render untrusted HTML
  - treat external links as hostile by default
- if evidence cannot be verified or resolved, render as **untrusted** and block publish flows

### Sensitive locations and culturally restricted material

- do not render exact coordinates in public UIs for vulnerable/restricted sites
- prefer generalization and show a governance note explaining why
- never allow share links to “accidentally” encode restricted geometry

### Abstention and restriction UX

Abstention is a feature. The UI must:
- show policy-safe reasons
- suggest safe alternatives
- provide `audit_ref` for steward review
- avoid leaking restricted existence

---

## Add a new app

### Checklist

1. Create app directory (choose the repo convention):
   - `apps/<new-app>/README.md` **or** `web/apps/<new-app>/README.md`
   - add `kfm.app.json` (or repo-standard manifest)
2. Define or extend contracts first:
   - update OpenAPI/GraphQL/JSON Schema
   - add fixtures and contract tests
3. Implement UI against governed APIs only:
   - no direct storage or DB access
   - evidence UX for every public layer/claim
4. Add tests:
   - unit, contract, E2E, accessibility, evidence resolution
   - receipt viewer safe-render tests if rendering receipts/manifests
5. Threat-model the change:
   - run [Threat model checklist](#threat-model-checklist)
6. Register the app:
   - add to [App registry](#app-registry) (human + machine registry if used)
7. Update this README:
   - regenerate “Current layout”
   - ensure the crosswalk reflects the chosen convention

---

## Glossary

- **Truth path lifecycle:** upstream → RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → projections → governed API → apps
- **Trust membrane:** enforced boundary where policy and provenance are applied; clients never access storage directly
- **Promotion Contract:** fail-closed gates that block serving any dataset version until identity, rights, sensitivity, catalogs, receipts, and policy tests validate
- **Evidence-first UX:** every visible claim opens into provenance, rights, and validation details
- **EvidenceRef:** resolvable reference used as a citation pointer
- **EvidenceBundle:** resolved evidence card (human + machine fields, digests, policy decision, audit refs)
- **ReceiptViewer:** safe read-only viewer for run receipts / promotion manifests; schema-validates and surfaces verification status
- **Trust badges:** compact UI indicators summarizing provenance/quality without leaking restricted details
- **Cite-or-abstain:** answer only when citations can be verified; otherwise abstain or reduce scope
- **Canonical vs rebuildable:** catalogs/provenance/artifacts are canonical; DB/search/graph/tiles are rebuildable projections

---

<details>
<summary><strong>Appendix: Updating this README without guessing</strong></summary>

- Determine whether runnable apps live under `apps/` or `web/apps/`.
- Regenerate the Current layout block from the actual repo tree.
- Populate the App Registry table from real app directories/manifests.
- If adopting the machine registry, ensure CI validates it (schema + owner paths) and CODEOWNERS covers it.
- For each app, link to:
  - contract references
  - trust surface entry points
  - CI gates and test commands
- Resolve owners via CODEOWNERS and replace `TBD`.

</details>

<p align="right"><a href="#top">Back to top ↑</a></p>
