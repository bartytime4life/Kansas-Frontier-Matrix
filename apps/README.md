<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS-UUID>
title: Apps Runtime Surfaces
type: standard
version: v1
status: draft
owners: <NEEDS VERIFICATION>
created: <NEEDS VERIFICATION>
updated: <NEEDS VERIFICATION>
policy_label: <NEEDS VERIFICATION>
related: [../README.md, ../docs/, ../contracts/, ../policy/, ../infra/]
tags: [kfm, apps, runtime, governance]
notes: [Grounded in attached KFM source corpus; live repo tree was not directly verified in the current session, so subdirectories, owners, commands, and links require review before commit.]
[/KFM_META_BLOCK_V2] -->

# Apps

Governed runtime surfaces for KFM’s API, UI, and background application lanes.

> [!IMPORTANT]
> This README is grounded in the attached KFM documentation corpus, not a directly verified `apps/` workspace snapshot. Treat path details, owners, and boot commands marked **INFERRED**, **UNKNOWN**, or **NEEDS VERIFICATION** as review items before merge.

**Status:** experimental  
**Owners:** `<NEEDS VERIFICATION>`  
**Badges:** ![status](https://img.shields.io/badge/status-experimental-lightgrey) ![evidence](https://img.shields.io/badge/evidence-pdf--grounded-blue) ![trust-membrane](https://img.shields.io/badge/trust-membrane_required-brightgreen) ![live-repo](https://img.shields.io/badge/live_repo-needs_verification-orange)

**Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Runtime diagram](#runtime-diagram) · [Reference tables](#reference-tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

---

## Scope

`apps/` is the application-facing runtime layer of KFM.

At the doctrinal level, this directory exists to hold the surfaces that users, reviewers, contributors, and operators actually interact with: the governed API boundary, the map/story/focus experience, and the background application lanes that support governed runtime behavior.

### What this directory is for

- **CONFIRMED:** exposing KFM through governed runtime surfaces rather than direct storage access
- **CONFIRMED:** preserving the trust membrane between clients and canonical/internal stores
- **CONFIRMED:** supporting product surfaces such as Map Explorer, Story, Evidence Drawer, and Focus Mode
- **INFERRED:** grouping those runtime surfaces under an `apps/` top-level boundary
- **PROPOSED:** making this directory the entry point for runtime-specific READMEs, local bring-up instructions, and app-surface ownership

### What this directory is not

- a home for canonical datasets
- a substitute for contracts, schemas, or policy rule packs
- a place to bypass EvidenceRef / EvidenceBundle resolution
- a place to expose raw or quarantined assets directly to clients
- a dumping ground for shared libraries that belong in `packages/` instead

[Back to top](#apps)

---

## Repo fit

| Field | Value |
|---|---|
| Path | `apps/` |
| Role | Runtime application boundary for governed API, UI surfaces, and worker-style application lanes |
| Upstream dependencies | `contracts/`, `policy/`, `data/`, `packages/`, `docs/`, `infra/` **(INFERRED; NEEDS VERIFICATION)** |
| Downstream consumers | public users, contributors, reviewers/stewards, operators |
| Architectural posture | map-first, time-aware, policy-enforced, evidence-first |
| Runtime rule | no direct client-to-storage bypass |
| Release posture | fail-closed; cite-or-abstain where claim-bearing behavior exists |

### Upstream / downstream map

**Upstream into `apps/`:**
- promoted datasets and catalog metadata
- policy decisions and vocabulary
- evidence-resolution contracts
- shared domain and adapter packages
- operational environment wiring

**Downstream from `apps/`:**
- governed API responses
- map/story/focus product surfaces
- evidence drawers and audit references
- reviewer workflows
- bounded runtime jobs and projections

[Back to top](#apps)

---

## Accepted inputs

The following content belongs here when it is runtime-facing and app-scoped:

- application entrypoints
- web clients and app shells
- governed API services
- app-specific worker lanes or orchestrated runtime jobs
- app-surface tests
- app-level configuration and deployment wiring
- app-local documentation that explains how a runtime surface behaves

### Accepted by sub-area

| Sub-area | Accepts | Status |
|---|---|---|
| API app | governed request handling, authz/authn integration, evidence resolution, audit emission | **CONFIRMED concept** |
| UI app | map, story, focus, evidence interaction surfaces | **CONFIRMED concept** |
| Worker app(s) | async jobs, queue consumers, projection builders, bounded runtime workflows | **INFERRED / NEEDS VERIFICATION** |
| App tests | app-level contract, accessibility, integration, and smoke tests | **INFERRED** |
| App docs | local README files, route/feature notes, operator-facing runtime notes | **PROPOSED** |

[Back to top](#apps)

---

## Exclusions

Content that should **not** live in `apps/`:

- canonical truth-path assets under `RAW`, `WORK/QUARANTINE`, `PROCESSED`, `CATALOG/TRIPLET`, or `PUBLISHED`
- source registry entries
- authoritative contract definitions
- policy packs as the system of record
- shared domain logic that should be versioned and reused across apps
- notebooks or ad hoc analysis outputs treated as production runtime surfaces

### Put it somewhere else

| Does not belong here | Put it under | Why |
|---|---|---|
| dataset registry entries | `data/registry/` | source onboarding and promotion posture should not be app-local |
| raw and processed artifacts | `data/` truth-path zones | canonical truth must remain distinct from runtime surfaces |
| schema / API / vocabulary authority | `contracts/` | apps should consume contracts, not silently redefine them |
| policy rules and fixtures | `policy/` | governance must remain explicit and testable |
| shared reusable code | `packages/` | avoids app-to-app duplication and drift |
| architectural doctrine | `docs/` | keeps doctrine visible, reviewable, and versioned |

> [!WARNING]
> If a runtime surface needs a new contract, vocabulary item, or policy rule, add or update it in the authoritative location first, then consume it from the app. Do not let `apps/` become a shadow source of truth.

[Back to top](#apps)

---

## Directory tree

The exact live tree was **not directly verified** in the current session. The structure below is a **doctrinally grounded draft** based on attached KFM materials.

```text
apps/
├─ api/                  # INFERRED: governed API boundary
│  ├─ README.md          # REFERENCED in attached project materials; NEEDS VERIFICATION in workspace
│  ├─ src/               # PROPOSED placeholder
│  ├─ tests/             # PROPOSED placeholder
│  └─ ...
├─ ui/                   # INFERRED: map/story/focus product surface
│  ├─ README.md          # PROPOSED placeholder
│  ├─ src/               # PROPOSED placeholder
│  ├─ tests/             # PROPOSED placeholder
│  └─ ...
├─ workers/              # INFERRED from some attached docs
│  └─ ...                # NEEDS VERIFICATION
└─ worker/               # POSSIBLE naming variant seen in attached docs
   └─ ...                # NEEDS VERIFICATION
```

### Naming note

There is a **naming ambiguity** in the attached corpus between `workers/` and `worker/`. This README intentionally preserves that ambiguity rather than guessing.

### Expected local README coverage

| Path | Expected role | Status |
|---|---|---|
| `apps/README.md` | top-level runtime boundary guide | **this file** |
| `apps/api/README.md` | API trust-membrane and endpoint posture | **INFERRED from attached docs** |
| `apps/ui/README.md` | user-facing surface behavior and UI-specific constraints | **PROPOSED** |
| `apps/worker/README.md` or `apps/workers/README.md` | async/runtime job posture and queue boundaries | **PROPOSED / NEEDS VERIFICATION** |

[Back to top](#apps)

---

## Quickstart

These commands are intentionally **verification-first**. They are meant to help a maintainer confirm the live repo shape before polishing this README further.

```bash
# Inspect what actually exists under apps/
find apps -maxdepth 3 -print | sort
```

```bash
# Find local README coverage and likely runtime entrypoints
find apps -maxdepth 4 \( -name 'README.md' -o -name 'package.json' -o -name 'pyproject.toml' -o -name 'Dockerfile' -o -name 'compose.yaml' -o -name 'docker-compose.yml' \) | sort
```

```bash
# Identify app-local tests and route/handler hints
find apps -maxdepth 5 \( -path '*/test*' -o -path '*/tests/*' -o -name '*route*' -o -name '*handler*' \) | sort
```

```bash
# Review nearby top-level boundaries this directory should align with
find . -maxdepth 2 \( -type d -name 'contracts' -o -name 'policy' -o -name 'packages' -o -name 'docs' -o -name 'infra' \) | sort
```

> [!NOTE]
> Do not add bootstrap or run commands to this file until the app toolchain is confirmed. The attached KFM documentation supports the runtime architecture, but not the exact package manager, framework entrypoints, or task runner present in the live workspace.

[Back to top](#apps)

---

## Usage

`apps/` should be treated as the place where KFM’s governed architecture becomes executable product behavior.

### Runtime rules for every app lane

1. **CONFIRMED:** public and contributor-facing behavior must cross a governed API boundary.
2. **CONFIRMED:** claim-bearing behavior must preserve a route back to evidence.
3. **CONFIRMED:** Focus-like AI behavior must cite or abstain.
4. **CONFIRMED:** policy failure must block or narrow output cleanly.
5. **PROPOSED:** app-local code should import shared contracts and vocabularies rather than redefining them.
6. **PROPOSED:** every app surface should have a local README explaining inputs, exclusions, and review gates.

### What “good” looks like in this directory

- UI surfaces open into evidence rather than hiding provenance
- API surfaces expose only promoted, policy-safe outputs
- app-local background jobs build or consume projections without redefining canonical truth
- runtime errors are policy-safe and auditable
- accessibility is treated as part of the product contract, not a final polish pass

### What to avoid

- direct DB/object-store reads from browser clients
- hidden internal-only routes accidentally promoted as public contract
- app-local one-off schemas that drift from `contracts/`
- AI output shown as authoritative when citation verification failed
- convenience endpoints that bypass policy, publication state, or evidence resolution

[Back to top](#apps)

---

## Runtime diagram

```mermaid
flowchart LR
    U[Public / Contributor / Reviewer] --> UI[apps/ui<br/>Map · Story · Focus · Evidence]
    UI --> API[apps/api<br/>Governed API boundary]

    API --> PDP[Policy enforcement<br/>default-deny / fail-closed]
    API --> ER[Evidence resolution<br/>EvidenceRef → EvidenceBundle]
    API --> PUBLISHED[Promoted published views]
    API --> PROJ[Rebuildable projections<br/>PostGIS · search · vector · tiles]

    W[apps/worker(s)<br/>runtime jobs] --> PROJ
    W --> PUBLISHED

    CANONICAL[RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED]
    CANONICAL -. governs release eligibility .-> API
    ER -. citation path .-> UI
```

### Diagram reading notes

- `apps/` is **downstream** of canonical promotion gates.
- `apps/api` is the executable trust membrane.
- `apps/ui` is where governed product surfaces become visible.
- worker-style app lanes may help build projections, but they do **not** become canonical truth by themselves.

[Back to top](#apps)

---

## Reference tables

### App lanes and their expected responsibilities

| Lane | Primary job | Must never do | Status |
|---|---|---|---|
| API | enforce auth, policy, evidence resolution, publication state, stable runtime contracts | expose raw/quarantined material directly | **CONFIRMED concept** |
| UI | render map/story/focus/evidence interactions | bypass governed API or suppress evidence path | **CONFIRMED concept** |
| Worker(s) | support async runtime jobs and rebuildable projections | silently publish canonical truth outside promotion gates | **INFERRED** |

### Truth posture inside `apps/`

| Topic | Required posture |
|---|---|
| Evidence | cite-or-abstain for claim-bearing runtime behavior |
| Publication state | expose promoted outputs only |
| Policy | default-deny / fail-closed |
| Provenance | preserve audit-friendly route back to evidence |
| Canonical vs rebuildable | treat search/vector/tile-style surfaces as derived unless separately promoted |
| Accessibility | part of the app contract |

### Verification status snapshot

| Item | Current label | Action |
|---|---|---|
| `apps/` as top-level runtime boundary | **INFERRED** | verify repo tree |
| `apps/api/` existence | **INFERRED** | confirm path and local README |
| `apps/ui/` existence | **INFERRED** | confirm path and app stack |
| `apps/worker/` vs `apps/workers/` | **UNKNOWN** | resolve naming in workspace |
| Owners | **UNKNOWN** | populate from CODEOWNERS or adjacent docs |
| Created / updated dates | **UNKNOWN** | fill from repo history |
| Toolchain commands | **UNKNOWN** | inspect package manifests and local scripts |

[Back to top](#apps)

---

## Task list

### Definition of done for this README

- [ ] verify the live `apps/` subtree
- [ ] resolve `worker/` vs `workers/`
- [ ] confirm local README links for each app lane
- [ ] confirm owners from authoritative repo evidence
- [ ] replace placeholder metadata values in the KFM meta block
- [ ] replace verification-first commands with actual bootstrap/run/test commands
- [ ] add direct relative links only after paths are confirmed
- [ ] confirm whether app-level accessibility and API contract checks already exist

### Review gates for app-surface changes

- [ ] no client-side storage bypass introduced
- [ ] no evidence path removed from claim-bearing UI
- [ ] no policy-unsafe endpoint added
- [ ] no uncited Focus-like success path shipped
- [ ] app-local docs updated when runtime behavior changes
- [ ] tests cover public/reviewer critical paths where relevant

[Back to top](#apps)

---

## FAQ

### Does `apps/` own canonical truth?

No. `apps/` should expose governed runtime behavior over promoted truth-path outputs. Canonical truth remains upstream in the governed data and catalog layers.

### Can the UI talk directly to storage or databases?

No. That would violate the trust membrane.

### Should vector or search indexes be treated as canonical here?

No by default. They are runtime accelerators and rebuildable projections unless separately promoted under an explicit governed process.

### Is Focus Mode just another chat surface?

No. It is a governed synthesis surface whose answers must cite correctly or abstain.

### Should contracts or policy rules be copied into app folders for convenience?

No. Apps should consume authoritative contracts and policies from their owning directories.

[Back to top](#apps)

---

## Appendix

<details>
<summary><strong>Glossary and verification notes</strong></summary>

### Compact glossary

- **Truth path** — the governed lifecycle from source capture through publication.
- **Trust membrane** — the rule that clients interact through governed APIs rather than internal stores.
- **EvidenceRef** — stable citation token used by runtime surfaces.
- **EvidenceBundle** — policy-safe resolved evidence payload.
- **Focus Mode** — governed natural-language synthesis over admissible evidence.
- **Audit reference** — stable runtime trace identifier for user-visible action paths.

### Review-first follow-ups

1. Open the live repo tree and confirm actual `apps/` contents.
2. Check whether `apps/api/README.md` exists and align terminology with it.
3. Confirm the frontend stack and test runner before adding concrete commands.
4. Confirm app-local ownership boundaries from CODEOWNERS or adjacent repo docs.
5. Add direct relative links after validation so GitHub navigation stays clean.

### Suggested neighboring docs to audit next

- `README.md`
- `apps/api/README.md`
- `docs/architecture/`
- `docs/governance/`
- `contracts/`
- `policy/`
- `infra/`

</details>

[Back to top](#apps)