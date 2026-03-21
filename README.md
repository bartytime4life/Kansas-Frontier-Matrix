<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TBD-VERIFY-root-readme-uuid
title: Kansas Frontier Matrix
type: standard
version: v1
status: review
owners: TBD-VERIFY-.github-CODEOWNERS
created: TBD-VERIFY-first-commit-date
updated: 2026-03-21
policy_label: TBD-VERIFY-public-or-restricted
related: [./docs/, ./contracts/, ./policy/, ./data/, ./apps/, ./packages/, ./tests/, ./infra/, ./tools/, TBD-VERIFY-./CONTRIBUTING.md, TBD-VERIFY-./SECURITY.md, TBD-VERIFY-./.github/CODEOWNERS]
tags: [kfm, root-doc, governance, evidence-first, map-first, trust-system]
notes: [Root README revision candidate grounded in the attached March 2026 KFM corpus and source-mediated repo inventories; active-branch tree, owners, CODEOWNERS, commit history, and adjacent root files still require direct verification.]
[/KFM_META_BLOCK_V2] -->

# Kansas Frontier Matrix

Governed, evidence-first, map-first, time-aware repository for Kansas spatial evidence, publication, and trust-visible product surfaces.

> **Status:** Experimental  
> **Owners:** TBD-VERIFY — `.github/CODEOWNERS` was not directly inspected in this session  
> ![Status: Experimental](https://img.shields.io/badge/status-experimental-orange) ![Owners: TBD](https://img.shields.io/badge/owners-TBD-lightgrey) ![Surface: Root README](https://img.shields.io/badge/surface-root%20README-6f42c1) ![Posture: Evidence-first](https://img.shields.io/badge/posture-evidence--first-success) ![Trust: Governed](https://img.shields.io/badge/trust-governed-blue) ![Evidence: Source-bounded](https://img.shields.io/badge/evidence-source--bounded-yellow)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Operating tables](#operating-tables) · [Task list](#task-list-and-definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `/README.md` *(documented root role; active-branch verification still required)*

> [!IMPORTANT]
> This README is intentionally **verification-first**. It is grounded in the attached March 2026 KFM doctrine, architecture, delivery, UI, and atlas manuals, plus source-mediated repository inventories preserved inside those manuals. The current session did **not** expose a mounted branch checkout, workflow YAML, runtime manifests, CODEOWNERS, or live test results. Treat path-level and implementation-shaped statements here as bounded until the active branch is inspected directly.

| At a glance | Working rule |
|---|---|
| System identity | Governed spatial evidence system |
| Value unit | The inspectable claim, not the layer, dashboard, or fluent answer |
| Truth path | `Source edge → RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` |
| Trust boundary | Governed APIs and evidence resolution, not direct client access to stores |
| Runtime answer rule | Cite or abstain |
| Publication rule | Promotion changes trust state; deployment should apply already approved intent |
| Surface rule | One map-first, time-aware shell with trust-visible evidence and negative states |
| 3D rule | 2D default; 3D is conditional and burden-bearing |

## Scope

This README covers the **repo-root identity and operating posture** of Kansas Frontier Matrix.

Use it for:

- root-level mission, boundaries, and non-negotiable invariants
- verification-first navigation across doctrine, contracts, policy, data, testing, apps, packages, and operations
- a source-bounded map of the documented repo shape
- the minimum path from clone to trustworthy local inspection

Do not use it for:

- full contract text that belongs in `./contracts/`
- full policy rules that belong in `./policy/`
- detailed source-domain coverage that belongs in `./docs/` and the domain/source atlas
- implementation certainty that has not been re-verified on the active branch

### Evidence posture used in this README

| Label | Meaning in this README |
|---|---|
| **CONFIRMED** | Supported by the attached March 2026 KFM corpus or by directly visible session evidence. |
| **INFERRED** | Strongly implied by repeated corpus patterns or source-mediated repo inventories, but not directly branch-inspected in this session. |
| **PROPOSED** | A recommended realization or repo pattern that fits doctrine but is not proven as current implementation reality. |
| **NEEDS VERIFICATION** | A likely repo-local fact, path, or control point that should be checked on the active branch before being treated as current reality. |
| **UNKNOWN** | Not supported strongly enough in this session to state as a live repo or runtime fact. |

> [!NOTE]
> The most authoritative attached KFM manuals repeatedly preserve this boundary on purpose: doctrine can be stated confidently, but live repo topology, CI gates, route inventories, manifests, and implementation depth should remain visible as **UNKNOWN** until directly inspected.

[Back to top](#kansas-frontier-matrix)

## Repo fit

**Path:** `/README.md` *(documented root role; active branch NEEDS VERIFICATION)*  
**Role:** Root orientation document and verification-first operating index for Kansas Frontier Matrix.

The attached corpus documents a root-level repository shape and a public repository name, but this session did **not** include a mounted checkout. The links below therefore follow the **documented root inventory** while keeping branch-local certainty visibly bounded.

| Direction | Documented path | Status | Why it matters |
|---|---|---|---|
| Root | `./README.md` | **INFERRED** | Root identity, navigation, and doctrine summary surface. |
| Upstream | [`./docs/`](./docs/) | **INFERRED** | Architecture, governance, ADRs, runbooks, and domain depth. |
| Upstream | [`./contracts/`](./contracts/) | **INFERRED** | OpenAPI, schemas, vocabularies, and shared contract surfaces. |
| Upstream | [`./policy/`](./policy/) | **INFERRED** | Policy bundles, fixtures, and policy tests. |
| Upstream | [`./data/`](./data/) | **INFERRED** | Registry, lifecycle zones, catalog artifacts, and receipts. |
| Downstream | [`./apps/`](./apps/) | **INFERRED** | Deployable runtime surfaces such as API, UI, workers, and related apps. |
| Downstream | [`./packages/`](./packages/) | **INFERRED** | Shared reusable law: ingest, evidence, catalog, policy, delivery, and domain logic. |
| Downstream | [`./tests/`](./tests/) | **INFERRED** | Unit, contract, policy, integration, and end-to-end verification. |
| Downstream | [`./infra/`](./infra/) | **INFERRED** | Deployment, environment wiring, observability, and delivery mechanics. |
| Downstream | [`./tools/`](./tools/) | **INFERRED** | Validators, link checkers, and supporting CLI utilities. |
| Adjacent | [`./.github/`](./.github/) | **INFERRED** | CI/CD, templates, CODEOWNERS, and review-routing signals. |
| Adjacent | `./CONTRIBUTING.md` | **NEEDS VERIFICATION** | Contributor contract and workflow expectations were not directly inspected. |
| Adjacent | `./SECURITY.md` | **NEEDS VERIFICATION** | Security policy presence and exact path were not directly inspected. |

KFM is easiest to understand as a **truth path → catalog / evidence → governed API → trust-visible surface** system. The root README exists to keep that order clear before contributors descend into domain-, app-, or contract-specific depth.

[Back to top](#kansas-frontier-matrix)

## Accepted inputs

At repo root, this README should summarize the input families KFM is built to admit and govern, while pushing detailed schemas, source registers, and ingestion rules into their owning docs.

| Input family | What belongs in KFM | Expected governed lane | Where detailed treatment should live |
|---|---|---|---|
| Historical tabular data | census extracts, registries, land records, archival tables | `RAW/` → `WORK/` → `PROCESSED/` | `./data/`, `./contracts/`, `./docs/` |
| Vector geodata | boundaries, parcels, routes, service areas, sites | `RAW/` → `PROCESSED/` | `./data/`, `./contracts/`, `./docs/` |
| Raster geodata | land cover, DEMs, climate grids, scenes, hazard rasters | `RAW/` → `PROCESSED/` → `CATALOG/` | `./data/`, `./contracts/`, `./docs/` |
| Documentary evidence | archives, newspapers, oral histories, scans, narrative support material | source intake → evidence flow | `./docs/`, `./data/`, evidence-related packages |
| Metadata and lineage | STAC, DCAT, PROV, manifests, receipts, run records | `CATALOG/` and proof surfaces | `./contracts/`, `./data/`, `./docs/` |
| Derived analytical artifacts | summaries, projections, tiles, exports, scenes, indexes | derived lanes only, always release-linked | `./packages/`, `./apps/`, `./infra/` |
| Validation and review artifacts | QA reports, fixtures, review notes, correction notices | `WORK/`, `tests/`, docs/runbooks | `./tests/`, `./docs/`, `./data/receipts/` |
| Policy-safe civic and environmental context | hydrology, hazards, land use, infrastructure context | governed domain lanes | `./docs/`, `./data/`, `./policy/` |

## Exclusions

These do **not** belong in the governed publication path, and this root README should not present them as acceptable shortcuts.

| Exclusion | Why it stays out | Where it goes instead |
|---|---|---|
| Secrets, tokens, credentials | Never commit secrets into the repo or artifact path. | Secret manager / environment provisioning |
| Direct client-to-store or client-to-model paths | Breaks the trust membrane. | Governed APIs and protected adapters |
| Publishable artifacts without receipts, digests, or catalog closure | Cannot be audited, reproduced, or corrected safely. | `WORK/QUARANTINE` until complete |
| Rights-unclear or sensitivity-unresolved material | Ambiguity must fail closed. | Quarantine, metadata-only handling, redaction, or generalized public-safe derivatives |
| Uncited Story or Focus claims | Violates cite-or-abstain. | Draft or internal review states only |
| Fine-grained restricted location exposure | Risks policy leakage and unsafe precision. | Restricted lanes or generalized public-safe outputs |
| Docs that imply live behavior without proof | Weakens trust through overclaiming. | Keep the statement `INFERRED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` |
| Detached reviewer/admin tools that sever geography, time, or evidence context | Breaks the governed shell model. | Review and stewardship as shell variation, not separate truth systems |

[Back to top](#kansas-frontier-matrix)

## Directory tree

### Documented root shape *(source-mediated; active branch NEEDS VERIFICATION)*

```text
<repo-root>/
├── README.md
├── .github/
├── docs/
├── contracts/
├── policy/
├── data/
├── apps/
├── packages/
├── tests/
├── infra/
├── tools/
└── ... additional root files and directories require branch verification
```

### Top-level role map

| Path target | Status | Expected repo role |
|---|---|---|
| `./.github/` | **INFERRED** | Workflow, templates, review routing, and merge discipline |
| `./docs/` | **INFERRED** | Architecture, governance, domain, ADR, diagram, and runbook documentation |
| `./contracts/` | **INFERRED** | API contracts, schemas, vocabularies, and shared object definitions |
| `./policy/` | **INFERRED** | Policy bundles, fixtures, deny-by-default rules, and policy tests |
| `./data/` | **INFERRED** | Registry entries, lifecycle zones, catalog artifacts, and receipts |
| `./apps/` | **INFERRED** | Deployable user- and operator-facing surfaces |
| `./packages/` | **INFERRED** | Shared reusable law and supporting libraries |
| `./tests/` | **INFERRED** | Unit, contract, policy, integration, and end-to-end verification |
| `./infra/` | **INFERRED** | Environment wiring, deployment, dashboards, and release mechanics |
| `./tools/` | **INFERRED** | Validators, link checkers, and supporting CLI/tooling |
| `./scripts/`, `./configs/`, `./migrations/`, `./examples/` | **NEEDS VERIFICATION** | Mentioned in some source-mediated inventories, but not directly confirmed in this session |

### What remains `UNKNOWN` or `NEEDS VERIFICATION`

- exact active-branch root file set
- exact `.github` inventory, including `CODEOWNERS`
- current workflow catalog and merge-blocking checks
- exact schema and fixture inventory
- actual deployment overlays and observability stack
- exact mounted route tree, DTO set, and proof-object emission coverage

[Back to top](#kansas-frontier-matrix)

## Quickstart

The safest root-level quickstart is **verification-first**, not assumption-first.

```bash
# identify the exact revision you are reviewing
git rev-parse HEAD 2>/dev/null || echo "Not inside a Git checkout"

# inspect the repo root and near-root shape
find . -maxdepth 2 -type d 2>/dev/null | sort | sed -n '1,160p'

# inspect GitHub control-plane files if present
find .github -maxdepth 3 -type f 2>/dev/null | sort
ls -la .github/workflows 2>/dev/null || true

# inspect likely contract, policy, data, and test surfaces
find contracts policy data tests tools -maxdepth 3 -type f 2>/dev/null | sort | sed -n '1,220p'

# inspect documentation, apps, packages, and infra
find docs apps packages infra -maxdepth 3 -type f 2>/dev/null | sort | sed -n '1,260p'

# pressure-test evidence, policy, and trust vocabulary
grep -RIn "EvidenceBundle\|EvidenceRef\|RuntimeResponseEnvelope\|truth membrane\|cite-or-abstain" docs contracts policy apps packages tests 2>/dev/null || true
grep -RIn "Map Explorer\|Evidence Drawer\|Focus Mode\|Story\|Dossier\|Review" docs apps packages 2>/dev/null || true
```

> [!TIP]
> Run the inspection loop above before upgrading any statement from `INFERRED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` to `CONFIRMED`.

<details>
<summary>Illustrative local-first contributor flow (use only where analogous targets actually exist)</summary>

```bash
make bootstrap
make validate-schemas
make test
make dev-up
make sample-ingest SOURCE=example_fixture
make catalog-validate
```

</details>

### Before documenting branch behavior as fact

1. Confirm what exists on this branch now.
2. Confirm which checks actually block merges.
3. Confirm which contracts, policies, and validations are enforced today.
4. Confirm that at least one end-to-end governed slice exists from source admission to evidence-backed public read.
5. Confirm whether public surfaces expose evidence, freshness, and policy-visible negative states rather than hiding them.
6. Confirm whether rollback, correction, and supersession are visible and evidenced rather than implied.
7. Confirm whether `.github/CODEOWNERS`, root doc neighbors, and README links match the active branch.

[Back to top](#kansas-frontier-matrix)

## Usage

### What KFM is

KFM is:

- a governed spatial evidence system
- a provenance-preserving publication program
- a map-first, time-aware shell over place, chronology, evidence, review state, and policy state
- a coordinated family of product surfaces that remain behind one trust membrane
- a Kansas-first operating environment for history, land, hydrology, hazards, environment, services, and public knowledge
- a platform that can grow into bounded retrieval and AI assistance **without** weakening the evidence contract

### What KFM is not

KFM is **not**:

- a free-form chatbot
- a dashboard-only GIS stack
- a direct browser-to-database mapping surface
- a graph-first or vector-first authority engine
- a publication path that can skip rights, provenance, review, or release evidence
- a spectacle-first 3D product
- a detached admin console that severs review from geography, time, and evidence

### Non-negotiable invariants

| Invariant | Status | Practical meaning | What must never happen |
|---|---|---|---|
| Truth path | **CONFIRMED doctrine** | Data moves through `Source edge → RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. | Ad hoc publication from analyst notebooks, transient transforms, or unpublished working states |
| Trust membrane | **CONFIRMED doctrine** | Public and role-limited access crosses governed APIs, policy, and evidence resolution. | Direct UI or external access to canonical stores, raw buckets, or model runtimes |
| Cite-or-abstain | **CONFIRMED doctrine** | Story, map, dossier, export, and Focus claims resolve to evidence or abstain. | Plausible uncited output presented as fact |
| Fail-closed posture | **CONFIRMED doctrine** | Unclear rights, unresolved sensitivity, or broken evidence blocks release. | “Best effort” publication under ambiguity |
| Deterministic identity | **CONFIRMED / INFERRED doctrine** | Comparable inputs and the same spec produce stable identities and digests. | Unstable versions or ambiguous lineage |
| Evidence as interface | **CONFIRMED doctrine** | Evidence must be operationally reachable through resolvable support objects. | Provenance trapped in notes that surfaces cannot reach |
| Documentation as production surface | **CONFIRMED doctrine** | Behavior-significant changes update docs, contracts, examples, diagrams, and runbooks together. | Silent drift between behavior and procedure |
| 2D default, 3D conditional | **CONFIRMED doctrine** | 2D remains the default operating surface; 3D carries extra governance burden. | Spectacle-first 3D becoming a parallel truth surface |

### Product surfaces and operating promise

| Surface | Status | What it should answer |
|---|---|---|
| Map Explorer | **CONFIRMED doctrine** | **Where?** |
| Timeline | **CONFIRMED doctrine** | **When?** |
| Dossier | **CONFIRMED doctrine / PROPOSED packaging** | **What matters about this place, feature, or subject?** |
| Story | **CONFIRMED doctrine** | **Why does the evidence matter?** |
| Evidence Drawer | **CONFIRMED doctrine** | **What does a visible claim rest on?** |
| Focus Mode | **CONFIRMED doctrine** | Natural-language investigation **without bypassing evidence or policy** |
| Review / Stewardship | **CONFIRMED doctrine / PROPOSED packaging** | Inspect, approve, restrict, correct, supersede, or withdraw within the same governed shell |
| Compare / Export | **PROPOSED shell family members** | Compare release contexts and preview what leaves the system without dropping trust cues |

### Kansas operating lanes at a glance

| Lane | Typical grain | Why it matters early |
|---|---|---|
| Historical and demographic | county-version, county-year, event-time | Establishes time-aware joins and stable place/time scaffolding |
| Hydrology and water | station-time, watershed, raster | Strong public-safe thin-slice candidate |
| Hazards and environment | event-time, county, polygon, raster | High public value with visible governance needs |
| Land and cadastral history | parcel, tract, legal description, PLSS section | Supports land-tenure, settlement, and archival interpretation |
| Archives and heritage | document, place, event-time | Critical for story publication and evidence depth |
| Services and infrastructure context | place, corridor, service area | Useful early, but precision and rights posture must stay explicit |

### Preferred first governed slice

A strong first slice is **hydrology-first**:

1. one released hydrology dataset family with stable source descriptors
2. one map + timeline surface that opens directly into an Evidence Drawer
3. one public-safe dossier or detail path
4. one Focus path that either cites correctly or abstains
5. one visible correction or supersession drill

[Back to top](#kansas-frontier-matrix)

## Diagram

```mermaid
flowchart LR
    A[Source edge] --> B[RAW]
    B --> C[WORK / QUARANTINE]
    C --> D[PROCESSED]
    D --> E[CATALOG / TRIPLET]
    E --> F[PUBLISHED]
    F --> G[GOVERNED API / EVIDENCE RESOLVER]
    G --> H[Map Explorer]
    G --> I[Timeline / Dossier / Story]
    G --> J[Evidence Drawer]
    G --> K[Focus Mode]
    G --> L[Review / Stewardship]
```

This is the core promise of the repo: every public or role-limited surface remains downstream of acquisition, policy checks, provenance capture, review state, and evidence resolution.

[Back to top](#kansas-frontier-matrix)

## Operating tables

### Truth path and promotion contract

Promotion is not a file copy. It is a governed state transition.

| Gate | Minimum proof | Fail-closed behavior |
|---|---|---|
| Identity and versioning | stable IDs, deterministic digests, immutable version references | Block on missing, duplicated, or unstable identity |
| Rights and license | rights snapshot, attribution basis, reuse posture | Hold or quarantine when rights are unclear |
| Sensitivity and generalization | policy label, obligations, generalization or redaction plan | Restrict, generalize, or block publication |
| Schema and QA | schema validity, spatial/time/unit checks, domain QC | Route to `WORK/QUARANTINE` on blocking failure |
| Catalog closure | linked catalog, lineage, and release linkage | Block if metadata and lineage do not resolve coherently |
| Receipt and review | run receipt, decision/review evidence, release inventory | Block if required review or proof objects are absent |
| Release and correction readiness | release manifest / proof pack, rollback and correction hooks | Block promotion until public-safe scope is inspectable and reversible |

### Release taxonomy

| Term | Meaning in KFM |
|---|---|
| Continuous integration | Proves a candidate change is buildable, testable, schema-valid, provenance-aware, and policy-checkable before trust widens |
| Continuous delivery | Assembles a releasable, immutable unit whose integrity, inventory, and provenance are explicit |
| Deployment | Applies already-approved desired state to a runtime surface |
| Promotion | Governs the transition from one trust state to another |
| Rollback / correction | Reverses or supersedes a prior decision **without erasing evidence** |

### Canonical vs rebuildable rule

| Class | Examples |
|---|---|
| **Canonical / authoritative** | `RAW`, `PROCESSED`, catalog-closure objects, review/decision artifacts, release manifests, correction notices |
| **Rebuildable / derived** | tiles, search indexes, graphs, caches, summaries, scenes, denormalized projections, embeddings |

### Documented first implementation wave *(plan documented, branch completion UNKNOWN)*

| Work package | Documented intent | What it proves |
|---|---|---|
| WP-01 | Spec hashing + controlled vocab validation | Stable identity and drift blocking |
| WP-02 | Catalog validators + link checker | Catalog closure and broken-link gating |
| WP-03 | Policy pack + fixture tests | Default-deny policy enforcement |
| WP-04 | Evidence resolver service | `EvidenceRef → EvidenceBundle` resolution |
| WP-05 | Dataset registry + discovery endpoints | Policy-filtered dataset discovery |
| WP-06 | Map Explorer baseline UI | Evidence Drawer, license/version visibility, keyboard navigation |
| WP-07 | Story Node publish workflow | Review state + resolvable citation gates |
| WP-08 | Focus Mode MVP + evaluation harness | Cite-or-abstain synthesis with regression control |

[Back to top](#kansas-frontier-matrix)

## Task list and definition of done

Use this as the minimum repo-root gate list for substantial work.

- [ ] active-branch evidence baseline exists: repo tree, manifests, schema inventory, workflow inventory, and sample proof objects
- [ ] `.github/CODEOWNERS` and root-doc neighbors are inspected and README placeholders retired where possible
- [ ] first-wave schemas plus valid and invalid fixtures validate in CI
- [ ] deny-by-default policy bundle and policy tests exist for integrity, provenance, rights/sensitivity, and runtime negative states
- [ ] release candidates emit validation, catalog-closure, manifest, and proof-pack artifacts
- [ ] `EvidenceBundle` drill-through works from consequential visible claims
- [ ] `RuntimeResponseEnvelope`-style negative-state grammar is visible and testable
- [ ] Map Explorer, Timeline, Dossier, Story, Focus, and Review surfaces expose trust-visible state where relevant
- [ ] Evidence Drawer drill-through works from the same governed shell
- [ ] Focus either cites with audit linkage or abstains cleanly
- [ ] derived freshness, correction, supersession, withdrawal, and stale-visible states remain explicit
- [ ] behavior-significant changes update docs, contracts, examples, diagrams, and runbooks in the same governed stream
- [ ] one hydrology-first slice proves descriptor → ingest → validation → dataset version → catalog closure → decision/review → release → map/read surface → correction
- [ ] one rollback or correction drill is rehearsed and leaves evidence-bearing output behind

## FAQ

### Why is KFM stricter than a normal map portal?

Because KFM is designed as a **trust system**, not just a presentation layer. Provenance, policy, review, and evidence resolution are runtime obligations, not decoration.

### Why does this README keep saying `UNKNOWN` or `NEEDS VERIFICATION`?

Because repo size and documentation density do not prove runtime governance. Branch-local facts should be verified from the active repo and live artifacts, not inferred from persuasive prose.

### Why are Evidence Bundles, catalogs, and receipts treated as first-class?

Because discoverability, reproducibility, review, and public trust depend on resolvable metadata and lineage, not just attractive maps or fluent answers.

### Why keep observed, documentary, derived, modeled, and AI-synthesized outputs distinct?

Because KFM must preserve the difference between what was observed, what was recorded, what was derived, what was modeled, and what was synthesized for explanation.

### Why start with a narrow slice?

Because one fully governed slice proves the architecture honestly. Many half-governed features only prove that governance was bypassed.

### Why is 2D the default operating surface?

Because 2D keeps geography, chronology, evidence, and state easier to govern. 3D is allowed only when it adds real explanatory value and still returns users to the same evidence flow.

### Why are some repo paths still marked `TBD-VERIFY` or `NEEDS VERIFICATION`?

Because the current session exposed doctrine and source-mediated repo inventories, not a mounted branch checkout. Root-doc adjacency should be verified against the active repository, not inferred from polished prose alone.

[Back to top](#kansas-frontier-matrix)

## Appendix

<details>
<summary>Open the root-doc verification appendix</summary>

### Working basis for this README candidate

This README is aligned to the attached March 2026 KFM authority layer, with the strongest weighting given to the replacement-grade KFM manuals, the unified geospatial architecture manual, the MapLibre UI architecture report, the components/pass dossiers, the master design manual, the evidence-first delivery compendium, and the domains/source atlas.

### Why placeholders remain in the meta block

The following values still require direct repo or history verification before publication:

- `doc_id`
- owners / `.github/CODEOWNERS`
- created date
- policy label
- exact adjacent root-doc links such as `CONTRIBUTING.md` and `SECURITY.md`

### First verification targets after repo mount

- root repo tree and package/workspace inventory
- `.github` inventory, especially `CODEOWNERS` and merge-blocking workflows
- schema directories, fixtures, and registry versions
- route inventory, DTO inventory, and runtime negative-path coverage
- `EvidenceBundle` resolver contracts and traces
- correction / rollback evidence and surface behavior

### Root README maintenance rule

Keep this file focused on:

- repo identity
- top-level navigation and boundaries
- non-negotiable invariants
- documented repo shape plus verification boundary
- the minimum governed quickstart
- root-level gates that help reviewers reject overclaiming early

Push deep schema catalogs, route trees, lane-by-lane source atlases, and environment-specific runbooks into their owning docs once those files are verified.

[Back to top](#kansas-frontier-matrix)

</details>
