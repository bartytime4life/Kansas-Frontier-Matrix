<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Governed API
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS-VERIFICATION
updated: 2026-04-15
policy_label: NEEDS-VERIFICATION
related: [
  ../README.md,
  ./app.py,
  ./routes/__init__.py,
  ./routes/soil_moisture.py,
  ./runtime/soil_moisture_runtime.py,
  ../api/src/api/README.md,
  ../explorer-web/README.md,
  ../review-console/README.md,
  ../workers/README.md,
  ../../contracts/README.md,
  ../../contracts/source/kansas_mesonet_source_descriptor.md,
  ../../contracts/soil_moisture/reading.schema.json,
  ../../schemas/README.md,
  ../../schemas/contracts/README.md,
  ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json,
  ../../schemas/soil_moisture/README.md,
  ../../policy/README.md,
  ../../packages/README.md,
  ../../tests/README.md,
  ../../tests/e2e/runtime_proof/soil_moisture/README.md,
  ../../tests/e2e/runtime_proof/soil_moisture/test_runtime_soil_moisture_proof.py,
  ../../tests/e2e/runtime_proof/soil_moisture/test_runtime_route_soil_moisture.py,
  ../../tests/e2e/runtime_proof/test_governed_api_app.py,
  ../../tools/ci/render_runtime_proof_summary.py,
  ../../.github/workflows/README.md
]
tags: [kfm, governed-api, api, trust-membrane, runtime, soil-moisture]
notes: [
  This revision preserves the stronger old boundary-first README while aligning it to the current thin-slice governed runtime implementation added in-session.
  The older surfaced draft used the path apps/governed-api/ while the current thin-slice code examples use apps/governed_api/. That path split remains NEEDS VERIFICATION and is kept explicit here instead of being silently flattened.
  Mounted repository inspection was not available in this session; repo-fit details below preserve the strongest supplied signals and should be rechecked against repository-authoritative sources before publication.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed API

Trust-bearing API boundary for KFM reads, evidence resolution, bounded assistance, exports, and steward-only actions.

> [!NOTE]
> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `apps/governed_api/README.md` *(older surfaced draft used `apps/governed-api/README.md`; exact mounted path remains NEEDS VERIFICATION)*  
> ![Status](https://img.shields.io/badge/status-experimental-orange) ![Trust](https://img.shields.io/badge/trust-membrane-1f4d78) ![Boundary](https://img.shields.io/badge/boundary-governed%20API-blue) ![Runtime](https://img.shields.io/badge/runtime-finite%20outcomes-6f42c1) ![Repo fit](https://img.shields.io/badge/repo--fit-needs%20mounted%20recheck-lightgrey)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> In KFM, the API boundary is part of the trust model. Public and steward-facing shells consume governed responses; they do **not** bypass policy evaluation, evidence resolution, release state, correction visibility, or runtime proof obligations.

> [!TIP]
> This README is intentionally **boundary-first**. It explains trust obligations, mounted app fit, accepted request families, and proof expectations. Route-by-route handler mechanics belong in the deeper route or runtime modules, not here.

---

## Scope

This directory documents the edge-facing contract boundary between KFM clients and released, policy-shaped, evidence-resolvable outputs.

The point of this README is not to describe transport plumbing in the abstract. Its job is to explain how KFM keeps the trust membrane intact at the public and steward edge: requests enter through governed surfaces, narrow to admissible released scope, resolve support-bearing objects, and leave through bounded runtime outcomes rather than uncited improvisation.

### Boundary doctrine in one view

The supplied KFM material consistently frames the governed API as the **runtime trust-surface boundary**. In that posture, the API and evidence resolver serve approved discovery, read, evidence-resolution, dossier, story, export, and Focus interactions; public or external surfaces may read only through this boundary and only within promoted scope; and the boundary may not bypass catalog, policy, review, or correction control planes.

### What this README must answer

1. What belongs in the governed API boundary?
2. What must stay outside it?
3. How does this boundary fit the current repo?
4. What is doctrinally confirmed today versus still unresolved at mounted-repo level?

### Current thin-slice reality

The in-session thin slice now clearly supports:

- a governed app assembly surface
- a mounted soil-moisture runtime route
- a runtime builder that emits finite outward envelopes
- fixture-driven runtime proof
- app-level and route-level tests
- schema-validated runtime responses

That means this README should now describe **both** doctrine and the thin-slice governed runtime that actually exists in the current work, without overstating broader app maturity.

[Back to top](#top)

---

## Repo fit

| Item | Value |
|---|---|
| File | `apps/governed_api/README.md` *(older surfaced draft used `apps/governed-api/README.md`)* |
| Directory role | Boundary-level README for the governed API surface |
| Boundary role from corpus | Governed API and evidence resolver for approved discovery, read, evidence-resolution, dossier, story, export, and Focus interactions |
| Current thin-slice mounted-style surfaces created in-session | `apps/governed_api/app.py`, `apps/governed_api/routes/__init__.py`, `apps/governed_api/routes/soil_moisture.py`, `apps/governed_api/runtime/soil_moisture_runtime.py` |
| Parallel deeper API doc surface | `apps/api/src/api/README.md` remains the likeliest deeper API-module README based on the supplied draft and project notes |
| Upstream neighbors | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md), [`../../policy/README.md`](../../policy/README.md), [`../../packages/README.md`](../../packages/README.md), [`../../tests/README.md`](../../tests/README.md) |
| Downstream / sibling consumers | [`../explorer-web/README.md`](../explorer-web/README.md), [`../review-console/README.md`](../review-console/README.md), [`../workers/README.md`](../workers/README.md) |
| Trust rule | Public or external surfaces should read only through governed API layers and only within promoted scope |
| Verification posture | Boundary doctrine is **CONFIRMED** from the supplied corpus; exact mounted repo-tree specifics remain **NEEDS VERIFICATION** in this session |

### Current surfaced repo-fit signals

> [!CAUTION]
> The table below preserves the strongest repo-fit signals available in the supplied old draft and the in-session thin-slice code work. It should not be upgraded into a mounted implementation claim until repository-authoritative inspection is performed.

| Surface | Current signal in supplied material | Safe reading |
|---|---|---|
| `apps/governed_api/` | Thin-slice app assembly, route, and runtime files were generated in-session | Treat as the current preferred app path for this slice, pending mounted recheck |
| `apps/governed-api/` | Older surfaced README draft used a hyphenated path | Treat as a path-tension / reconciliation item, not a hidden typo |
| `apps/api/src/api/` | Identified as a deeper API-shaped doc surface with `README.md`, `middleware/`, and `routes/` adjacency | Treat as the likeliest home for route/module detail beyond this boundary README |
| `contracts/` | Named as neighboring human-readable contract law | Safe to reference as adjacent doctrinal ownership |
| `schemas/contracts/` | Named as neighboring machine-file contract lane | Safe to reference as adjacent schema ownership |
| `policy/` | Named as adjacent policy-runtime / bundle lane | Safe to reference as enforcement dependency, not sovereign home of this app |
| `tests/` | Named as adjacent verification family | Safe to reference as the proof lane, not as proof of broader app maturity |
| `.github/workflows/` | Mentioned as neighboring workflow surface | Keep workflow depth explicitly bounded until direct file inspection happens |

### Boundary-first reading

This file should describe:

- the API as a trust-bearing boundary
- the repo neighbors it depends on
- the runtime and proof objects it touches
- the open reconciliation work between `apps/governed_api/` and `apps/api/src/api/`

It should **not** duplicate route-by-route implementation notes better housed in [`../api/src/api/README.md`](../api/src/api/README.md) or the local runtime / route modules.

[Back to top](#top)

---

## Accepted inputs

This area should accept or orchestrate the following request classes.

| Request family | Belongs here? | Notes |
|---|---:|---|
| Catalog and discovery requests | Yes | Release-scoped discovery, catalog closure reads, outward metadata resolution |
| Feature / subject / place reads | Yes | Released authoritative reads only |
| Map / tile / style / legend / portrayal reads | Yes | Public-safe delivery over released scope |
| `EvidenceRef` resolution | Yes | Request-time drill-through to `EvidenceBundle` |
| Story / dossier / compare reads | Yes | Must stay anchored to the same geography/time/release shell |
| Export / report requests | Yes | Public-safe outward artifacts that inherit release, policy, and correction state |
| Focus / governed assistance requests | Yes | Bounded synthesis over admissible released evidence only |
| Soil-moisture runtime requests | Yes | Thin-slice mounted governed runtime path in current work |
| Review / stewardship actions | Yes, internal only | Approval, denial, rollback, quarantine inspection, rights/sensitivity handling |
| Ops / status endpoints | Yes, internal only | Health, traces, audit joins, runtime status; never a shadow truth surface |
| Raw store paths, DB credentials, unpublished candidate artifacts | No | Trust-membrane violation |
| Free-form uncited assistant behavior | No | Prohibited by KFM doctrine |

### Thin-slice soil-moisture request posture

The current governed runtime slice supports requests shaped like:

- request metadata (`request_id`)
- query context (`kind=soil_moisture`, interval, station hints, quantity hints)
- canonical candidate object for the bounded runtime evaluation

This is intentionally narrow. The route is not yet a general ingestion or retrieval API; it is a governed request-time envelope builder over already-bounded candidate support.

---

## Exclusions

| Out of scope | Why it stays out | Where it goes instead |
|---|---|---|
| Direct browser/client access to RAW, WORK, QUARANTINE, canonical stores, or artifact trees | Collapses the trust membrane | Intake, canonical, catalog/review, and projection planes behind governed services |
| Canonical writes from ordinary clients | Public clients are not authority writers | Steward-only review / repair / promotion lanes |
| Shared domain model ownership | Prevents app-local drift and duplicated contract semantics | [`../../packages/README.md`](../../packages/README.md) |
| Policy bundle authorship | This boundary enforces policy; it should not become policy’s sovereign home | [`../../policy/README.md`](../../policy/README.md) |
| Schema / standards-profile source of truth | This boundary consumes and validates against them | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md) |
| Hidden correction or rollback behavior | KFM requires visible correction lineage | release / correction runbooks and proof objects |
| “Secret” second truth in telemetry or ops | Status endpoints must not become a bypass database | shaped governed ops surfaces only |
| Route-detail duplication already maintained elsewhere | Creates drift between boundary docs and handler/module docs | [`../api/src/api/README.md`](../api/src/api/README.md) |
| Fetching or normalizing source data inside the runtime route | Breaks the thin-slice trust split | source descriptor, watcher, normalization, and validator lanes |

> [!WARNING]
> Do not let this directory become a convenience bypass. In KFM, undocumented edge behavior is usually governance debt in disguise.

[Back to top](#top)

---

## Directory tree

### Current thin-slice governed API sketch

```text
apps/
├── governed_api/
│   ├── README.md
│   ├── app.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── soil_moisture.py
│   └── runtime/
│       └── soil_moisture_runtime.py
└── api/
    └── src/
        └── api/
            └── README.md
```

### Older surfaced path sketch

```text
apps/
└── governed-api/
    └── README.md
```

### Adjacent contract / policy / verification surfaces

```text
contracts/
├── README.md
├── source/
│   └── kansas_mesonet_source_descriptor.md
└── soil_moisture/
    └── reading.schema.json

schemas/
├── README.md
├── soil_moisture/
│   └── README.md
└── contracts/
    ├── README.md
    └── v1/
        ├── runtime/
        │   └── runtime_response_envelope.schema.json
        └── source/
            └── source_descriptor.schema.json

tests/
├── README.md
└── e2e/
    └── runtime_proof/
        ├── soil_moisture/
        │   ├── README.md
        │   ├── fixtures/
        │   ├── test_runtime_soil_moisture_proof.py
        │   └── test_runtime_route_soil_moisture.py
        └── test_governed_api_app.py
```

### Working implication

The strongest current signal is that the repo now has **at least two API-facing documentation surfaces** to reconcile explicitly:

1. `apps/governed_api/README.md` — boundary-facing, trust-first README for the current thin slice  
2. `apps/api/src/api/README.md` — deeper API-module surface for broader route and middleware detail

That is a documentation split to reconcile, not a fact to hide.

[Back to top](#top)

---

## Quickstart

### Verification-first review loop

1. Read this file as the **boundary README** for the governed API surface.
2. Read [`../api/src/api/README.md`](../api/src/api/README.md) as the deeper API-module surface.
3. Check [`../../contracts/README.md`](../../contracts/README.md), [`../../contracts/source/kansas_mesonet_source_descriptor.md`](../../contracts/source/kansas_mesonet_source_descriptor.md), and [`../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) before making contract claims here.
4. Check [`../../policy/README.md`](../../policy/README.md) and [`../../tests/README.md`](../../tests/README.md) before claiming enforcement depth.
5. Promote or downgrade wording in this README only after those neighbors agree.

### Useful local inspection commands

Use these when the repository is mounted and you need to recheck boundary claims directly:

```bash
find apps/governed_api -maxdepth 3 -type f | sort
find apps/governed-api -maxdepth 3 -type f | sort 2>/dev/null || true
find apps/api/src/api -maxdepth 3 -type f | sort
find contracts -maxdepth 3 -type f | sort
find schemas/contracts -maxdepth 4 -type f | sort
find tests/e2e/runtime_proof -maxdepth 4 -type f | sort
find .github/workflows -maxdepth 2 -type f | sort
```

### Minimal review pass before editing boundary claims

```bash
sed -n '1,260p' apps/governed_api/README.md 2>/dev/null || true
sed -n '1,260p' apps/api/src/api/README.md 2>/dev/null || true
sed -n '1,220p' apps/governed_api/app.py 2>/dev/null || true
sed -n '1,240p' apps/governed_api/routes/soil_moisture.py 2>/dev/null || true
sed -n '1,240p' apps/governed_api/runtime/soil_moisture_runtime.py 2>/dev/null || true
sed -n '1,240p' contracts/README.md 2>/dev/null || true
sed -n '1,240p' policy/README.md 2>/dev/null || true
sed -n '1,240p' tests/e2e/runtime_proof/soil_moisture/README.md 2>/dev/null || true
```

> [!TIP]
> The supplied KFM corpus proves more doctrine than mounted implementation. Keep broader route names, DTOs, workflow enforcement, and live runtime depth visibly bounded unless the repo, tests, manifests, or emitted proof objects are directly rechecked.

[Back to top](#top)

---

## Usage

### Boundary responsibilities

The governed API should expose request families by responsibility, not by framework fashion.

| Route family | Public or internal | What it owes callers |
|---|---:|---|
| Catalog and discovery | Public governed | release scope, stable identifiers, outward metadata closure |
| Feature / subject / place reads | Public governed | support/time semantics, rights posture, release linkage, correction visibility |
| Map / tile / portrayal | Public governed | release linkage, freshness basis, policy posture |
| Evidence resolution | Public governed | `EvidenceRef → EvidenceBundle`, preview policy, rights/sensitivity state, audit linkage |
| Story / dossier / compare | Public governed | anchored geography/time shell, drill-through to evidence |
| Export / report | Public governed | no export outruns release, policy, or correction state |
| Focus / governed assistance | Public governed | finite outcome, citation checks, policy-visible reasoning boundary, audit linkage |
| Soil-moisture runtime | Public governed (thin slice) | finite runtime envelope, explicit source role, depth/unit/freshness visibility, fail-closed outcomes |
| Review / stewardship | Internal governed | explicit decision artifacts, no hidden approvals |
| Ops / status | Internal governed | health and explainability without raw-store exposure |

### Boundary request rule of thumb

1. Establish request context, audience, and allowed surface.
2. Apply policy pre-checks and scope narrowing.
3. Resolve only to release-scoped admissible material.
4. Resolve evidence, catalog, or outward portrayal objects.
5. Shape the result into a bounded runtime outcome.
6. Attach decision, audit, and correction linkage where required.
7. Preserve visible stale-state, narrowing, or denial cues instead of bluffing.

### Thin-slice runtime route posture

The current soil-moisture route:

- accepts a thin request envelope
- rejects malformed request shape early
- denies unsupported query kinds
- delegates candidate trust logic to the runtime module
- returns finite outward outcomes:
  - `ANSWER`
  - `ABSTAIN`
  - `DENY`
  - `ERROR`

It does **not**:

- fetch Mesonet directly
- normalize raw provider payloads
- issue promotion decisions
- sign proofs
- publish catalogs

### Public-safe outcomes

| Outcome | Allowed? | Minimum burden |
|---|---:|---|
| Evidence-linked read | Yes | resolvable support, policy-allowed scope, release linkage |
| `ANSWER` | Yes | evidence resolution + citation / source checks + bounded support |
| `ABSTAIN` | Yes | explicit bounded reason, calm failure language |
| `DENY` | Yes | policy or trust reason + obligation visibility where applicable |
| `ERROR` | Yes | machine-meaningful failure without bluffing |
| Silent fallback to uncited prose | No | prohibited |
| Direct DB / object-store pass-through | No | prohibited |

### Boundary README vs module README

| Surface | Best use |
|---|---|
| `apps/governed_api/README.md` | explain trust obligations, repo fit, accepted inputs, exclusions, proof expectations, adjacent ownership |
| `apps/api/src/api/README.md` | explain middleware, broader route groups, `/api/v1` shaping, implementation-facing handler organization |
| `apps/governed_api/runtime/soil_moisture_runtime.py` | explain runtime envelope assembly for the current thin slice |
| `apps/governed_api/routes/soil_moisture.py` | explain request handling and route behavior for the thin slice |
| `contracts/README.md` | explain human-readable contract law and contract families |
| `schemas/contracts/README.md` | explain machine-file contract scaffolding and vocabulary adjacency |
| `policy/README.md` | explain policy-runtime, bundle, and fixture lanes |
| `tests/README.md` | explain verification families and proof expectations |

### Repo-facing guidance

This README should remain the calm, high-signal answer to:

- “What is the governed API surface for?”
- “What does it protect?”
- “What does it consume?”
- “What must not bypass it?”

It should not become the place where route-by-route handler mechanics drift away from the actual API module docs.

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    subgraph Clients["Client and operator surfaces"]
        Explorer["apps/explorer-web"]
        Review["apps/review-console"]
        CLI["apps/cli"]
        Workers["apps/workers"]
    end

    subgraph Boundary["Governed API boundary"]
        BoundaryReadme["apps/governed_api/README.md"]
        App["app.py"]
        Route["routes/soil_moisture.py"]
        Runtime["runtime/soil_moisture_runtime.py"]
        Envelope["Runtime outcomes\nANSWER / ABSTAIN / DENY / ERROR"]
    end

    subgraph Control["Control-plane dependencies"]
        Contracts["contracts + schemas"]
        Policy["Policy / review / decisions"]
        Validator["Soil-moisture validator"]
        Release["Release / correction / rollback"]
    end

    subgraph Published["Published outward scope"]
        Closure["STAC / DCAT / PROV closure"]
        Releases["Promoted datasets, portrayals,\nexports, and release refs"]
    end

    subgraph NonPublic["Non-public planes"]
        Raw["RAW / WORK / QUARANTINE"]
        Canon["Canonical truth"]
    end

    Explorer --> BoundaryReadme
    Review --> BoundaryReadme
    CLI --> BoundaryReadme
    Workers --> BoundaryReadme

    BoundaryReadme --> App
    App --> Route
    Route --> Runtime
    Runtime --> Envelope
    Runtime --> Validator
    Route --> Contracts
    Route --> Policy
    Route --> Release

    Release --> Closure
    Release --> Releases

    Explorer -. no direct client path .-> Raw
    Explorer -. no direct client path .-> Canon
    Route -. may not bypass control planes .-> Canon
    Review -. no hidden approval bypass .-> Canon
```

### Reading the diagram

The API does not “own” the whole system. It owns the public and steward edge where request context, policy evaluation, evidence resolution, and bounded runtime results meet. In the current thin slice, that edge is now represented by a boundary README, an app assembly, a route handler, and a runtime module.

[Back to top](#top)

---

## Tables

### Core proof-bearing objects this boundary is expected to touch

| Object family | Why it matters here | Current posture |
|---|---|---|
| `SourceDescriptor` | keeps source role, cadence, and rights posture explicit at runtime | strong thin-slice alignment |
| canonical soil-moisture candidate | bounded support object for governed runtime responses | strong thin-slice alignment |
| validator result | keeps subject-level validation separate from outward runtime behavior | strong thin-slice alignment |
| `RuntimeResponseEnvelope` | keeps runtime outcomes finite, inspectable, and auditable | now schema-backed in thin slice |
| `run_receipt` | provides machine-checkable audit linkage for support-bearing work | visible seam, not equivalent to runtime response |
| `EvidenceBundle` | makes broader drill-through operational at point of use | doctrinally strong; broader mounted examples still need verification |
| `DecisionEnvelope` | makes policy results machine-readable | strong corpus support; broader mounted shape still needs verification |
| `ReleaseManifest` / proof pack | ties outward payloads to release state | corpus-supported; broader emitted examples still need verification |

### Boundary-adjacent proof quartet

| Artifact | Why the boundary cares | Ownership note |
|---|---|---|
| `spec_hash` | joins visible runtime or release behavior back to exact input / contract state | cross-cutting proof object; not boundary-exclusive |
| `run_receipt` | provides machine-checkable audit linkage for fetch/build/publish work that shapes outward scope | usually emitted in ingest/build/release lanes, consumed at the boundary |
| `ai_receipt` | required wherever model-mediated proposal or bounded assistance participates | subordinate to evidence and policy; not a replacement for `EvidenceBundle` |
| Attestation ref / bundle | connects releases or run artifacts to signed proof | strongest as release/proof-lane object; boundary should link, not reinvent |

### Boundary ownership matrix

| Concern | This app owns it | This app consumes it | This app must not replace it |
|---|---:|---:|---:|
| Request authentication / policy edge | ✓ |  |  |
| Evidence resolution orchestration | ✓ |  |  |
| Runtime envelope emission | ✓ |  |  |
| Shared domain model ownership |  | ✓ | ✓ |
| Policy bundle authoring |  | ✓ | ✓ |
| Catalog closure authoring |  | ✓ | ✓ |
| Canonical source-of-truth writes |  |  | ✓ |
| Derived map/search/scene rebuild logic |  | ✓ | ✓ |
| Route/middleware implementation detail |  | ✓ | ✓ |

### Evidence and freshness posture

| Statement type | What to surface |
|---|---|
| Released, public-safe read | release linkage, provenance, freshness basis, correction state |
| Modeled / derived content | modeled status, limits, and release linkage |
| Partial coverage | explicit partial-state cue, not silent omission |
| Stale projection | visible stale cue or fail-closed denial depending on policy |
| Rights / sensitivity constrained read | denial or generalized output with stated obligation |

### Thin-slice runtime surface

| Surface | Current role | Notes |
|---|---|---|
| `app.py` | app assembly | mounts current governed routes |
| `routes/soil_moisture.py` | request handling | finite HTTP behavior for the soil-moisture route |
| `runtime/soil_moisture_runtime.py` | envelope builder | converts validated candidate state into outward runtime responses |
| `tests/e2e/runtime_proof/...` | proof of outward behavior | fixture-driven and schema-aware |
| `tools/ci/render_runtime_proof_summary.py` | reviewer summary | presentation-only, not authority |

### Current verification posture

| Area | Safe reading now |
|---|---|
| Route families and trust obligations | **CONFIRMED** doctrine from supplied KFM materials |
| Runtime proof for the soil-moisture slice | **CONFIRMED in-session thin slice** |
| Runtime envelope schema | **CONFIRMED in-session thin slice** |
| Broader EvidenceBundle / DecisionEnvelope / release-proof family | **CONFIRMED doctrine**, broader mounted examples still **NEEDS VERIFICATION** |
| Repo tree shape under `apps/`, `contracts/`, `schemas/`, `policy/`, `tests/` | **NEEDS VERIFICATION** in this session because the mounted repo was not surfaced |
| CI / workflow enforcement depth | **UNKNOWN** beyond what neighboring docs may later prove |

[Back to top](#top)

---

## Task list

### Definition of done for this directory

- [ ] Canonical relationship between `apps/governed_api/README.md` and `apps/api/src/api/README.md` is explicitly documented in both places.
- [ ] Owners, created date, doc UUID, and policy label in the meta block are filled from repo-authoritative sources.
- [ ] The current mounted path (`governed_api` vs `governed-api`) is resolved explicitly.
- [ ] One public governed-read contract surface is linked from this README.
- [ ] One internal / steward contract surface is linked from this README.
- [ ] One positive runtime trace is linked.
- [ ] One negative runtime trace is linked for each of `ABSTAIN`, `DENY`, and `ERROR`.
- [ ] One correction / rollback example is linked.
- [ ] Boundary-adjacent proof quartet references are linked where relevant: `spec_hash`, `run_receipt`, `ai_receipt`, attestation ref / bundle.
- [ ] Public claims about CI gates are kept aligned with actual workflow files, not just README intent.
- [ ] Route-level duplication between this file and deeper route/module docs is reduced or explicitly partitioned.

### First high-value gates

- [ ] **contracts gate** — schema compile + valid/invalid fixtures + non-zero CI failure
- [ ] **policy gate** — deny-by-default reason / obligation grammar
- [ ] **resolver gate** — positive and negative evidence traces
- [ ] **runtime gate** — finite envelope validation for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`
- [ ] **correction gate** — visible supersession / withdrawal / rollback behavior
- [ ] **docs gate** — boundary README, module README, runbooks, and actual route/contract behavior stay aligned

### Immediate repo-fit follow-ups

- [ ] Decide whether `apps/governed_api/` remains the durable app shell path.
- [ ] Confirm whether `schemas/contracts/` or another path is the durable machine-file authority for runtime and evidence contracts.
- [ ] Replace scaffold-state or placeholder representative files before claiming broader implemented contract-family depth in prose.
- [ ] Confirm whether `.github/workflows/README.md` reflects hidden/private enforcement, public enforcement, or intended future structure only.
- [ ] Add narrower `CODEOWNERS` coverage if `apps/governed_api/` needs review routing more specific than `/apps/`.

[Back to top](#top)

---

## FAQ

### Why “governed API” instead of just “backend”?

Because KFM treats the API boundary as part of the trust model. It is where public or steward requests inherit release state, evidence drill-through, policy posture, and fail-closed runtime behavior.

### Why can’t the UI call the database or object store directly?

Because that would collapse the trust membrane. Browser shells are supposed to inherit governed evidence, policy, and correction behavior — not bypass them.

### Why are there two API-facing documentation surfaces right now?

Because the strongest surfaced repo-fit signal points to both `apps/governed_api/README.md` and `apps/api/src/api/README.md`. The first reads best as a boundary README for the current thin slice. The second still reads best as a deeper API module surface. The split is real and should be documented rather than blurred.

### Is `apps/governed_api/` currently code-bearing?

In the current thin slice produced in-session, yes. Broader branch-level inventory still needs direct verification.

### Where should endpoint-level details live?

Today, the least-drifty place is the local route/runtime modules plus `apps/api/src/api/README.md` for broader API-module structure, unless the repo later consolidates that ownership.

### Are runtime contracts already enforcement-grade?

For the current soil-moisture thin slice, the runtime envelope and runtime-proof tests are now concrete. Broader contract-family depth still needs direct recheck.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Status legend, vocabulary, and path note</strong></summary>

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | directly supported by the supplied KFM corpus or by in-session thin-slice files |
| **INFERRED** | strongly implied by repeated project patterns, but not directly proven as mounted broader behavior |
| **PROPOSED** | recommended starter shape or reconciliation move |
| **UNKNOWN** | not verified strongly enough to claim as live repo or runtime fact |
| **NEEDS VERIFICATION** | a field, repo path, or authority source that should be rechecked before publication |

### Working vocabulary

| Term | Meaning in this README |
|---|---|
| **Trust membrane** | the boundary that prevents public or ordinary UI paths from bypassing governed services |
| **SourceDescriptor** | source-admission object for role, rights, cadence, and access posture |
| **RuntimeResponseEnvelope** | bounded runtime result object carrying outcome, reason, and trust cues |
| **run_receipt** | compact machine-readable process memory |
| **EvidenceBundle** | broader request-time package of support, lineage hints, rights/sensitivity state, and preview policy |
| **DecisionEnvelope** | machine-readable policy result with reason and obligation codes |

### Path note

Treat `apps/governed_api/README.md` as the preferred current target path for this README.

Treat `apps/governed-api/README.md` as an older surfaced path signal that still needs reconciliation.

Treat `apps/api/src/api/README.md` as the likeliest parallel deeper API module documentation surface until direct repository inspection either confirms or revises that relationship.

</details>

<details>
<summary><strong>Current direct-recheck checklist</strong></summary>

```bash
# app surfaces
find apps -maxdepth 3 -type f | sort

# governed app thin slice
find apps/governed_api -maxdepth 3 -type f | sort

# older path signal
find apps/governed-api -maxdepth 3 -type f | sort 2>/dev/null || true

# deeper API surface
find apps/api/src/api -maxdepth 3 -type f | sort

# contracts and schemas
find contracts -maxdepth 3 -type f | sort
find schemas/contracts -maxdepth 4 -type f | sort

# policy and tests
find policy -maxdepth 3 -type f | sort
find tests/e2e/runtime_proof -maxdepth 4 -type f | sort

# workflow visibility
find .github/workflows -maxdepth 3 -type f | sort
```

</details>

[Back to top](#top)
