<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-settlements-infrastructure-readme
title: Settlements Infrastructure Domain Package README
type: standard
version: v1
status: draft
owners: OWNER_TBD
created: 2026-06-14
updated: 2026-06-14
policy_label: public
related:
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - docs/domains/settlements-infrastructure/SOURCE_ROLES.md
  - docs/domains/settlements-infrastructure/TIME_SEMANTICS.md
  - docs/domains/settlements-infrastructure/PROMOTION.md
  - docs/domains/settlements-infrastructure/UI_AND_EVIDENCE_DRAWER.md
  - contracts/domains/settlements-infrastructure/
  - schemas/contracts/v1/domains/settlements-infrastructure/
  - policy/domains/settlements-infrastructure/
  - tests/domains/settlements-infrastructure/
  - fixtures/domains/settlements-infrastructure/
  - data/registry/settlements-infrastructure/
  - data/receipts/settlements-infrastructure/
  - data/proofs/settlements-infrastructure/
  - data/catalog/domain/settlements-infrastructure/
  - data/published/layers/settlements-infrastructure/
  - release/settlements-infrastructure/
tags:
  - kfm
  - packages
  - domains
  - settlements-infrastructure
  - settlements
  - cities
  - infrastructure
  - public-safe-geometry
  - evidence
  - release
  - rollback
notes:
  - "README-like package entrypoint for shared settlements/cities/infrastructure implementation helpers."
  - "Directory Rules support packages/domains/<domain>/ as the responsibility-rooted package lane; this document treats implementation depth as UNKNOWN until current repo files, tests, schemas, policy, and workflows are inspected."
  - "This package may contain reusable implementation helpers only; it must not become schema, contract, policy, source-registry, lifecycle-data, release, receipt, proof, or public API authority."
[/KFM_META_BLOCK_V2] -->

# Settlements Infrastructure Domain Package

Shared implementation package for KFM settlements, cities, place-boundaries, infrastructure assets, public-safe infrastructure context, dependency summaries, governed layer payload helpers, and evidence-bound domain normalization.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: proposed" src="https://img.shields.io/badge/implementation-PROPOSED-orange">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Root: packages" src="https://img.shields.io/badge/root-packages-blue">
  <img alt="Domain: settlements infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-2f6f4e">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
  <img alt="Public path: governed only" src="https://img.shields.io/badge/public__path-governed__only-informational">
</p>

> [!IMPORTANT]
> **Status:** PROPOSED package README  
> **Path:** `packages/domains/settlements-infrastructure/README.md`  
> **Owning responsibility root:** `packages/`  
> **Domain lane:** `settlements-infrastructure`  
> **Truth posture:** CONFIRMED doctrine / PROPOSED implementation / UNKNOWN repo depth  
> **Repo implementation depth:** NEEDS VERIFICATION — package metadata, source files, tests, schemas, policies, registries, CI workflows, API routes, UI bindings, emitted receipts, proof objects, release manifests, and runtime behavior were not inspected in this file-generation pass.

> [!NOTE]
> This README is a package contract, not an implementation proof. It states where reusable code may live and what it may do. It does not prove that the package currently exists in the repository or that any specific function, route, schema, test, release, or workflow has been implemented.

## Quick links

- [Scope](#scope)
- [Repo fit](#repo-fit)
- [What this package may own](#what-this-package-may-own)
- [What this package must not own](#what-this-package-must-not-own)
- [Accepted inputs](#accepted-inputs)
- [Excluded inputs and outputs](#excluded-inputs-and-outputs)
- [Domain model boundaries](#domain-model-boundaries)
- [Settlement and infrastructure source-role rules](#settlement-and-infrastructure-source-role-rules)
- [Identity, time, and digest rules](#identity-time-and-digest-rules)
- [Public-safe geometry and exposure controls](#public-safe-geometry-and-exposure-controls)
- [Trust-boundary flow](#trust-boundary-flow)
- [Proposed directory map](#proposed-directory-map)
- [Finite outcomes](#finite-outcomes)
- [Validation and quality gates](#validation-and-quality-gates)
- [Development rules](#development-rules)
- [Definition of done](#definition-of-done)
- [Evidence basis](#evidence-basis)
- [Verification checklist](#verification-checklist)
- [Rollback](#rollback)

---

## Scope

`packages/domains/settlements-infrastructure/` is the PROPOSED shared implementation package lane for reusable code supporting KFM settlements, cities, infrastructure, public-safe built-environment context, domain identity helpers, normalization helpers, graph-projection preparation, Evidence Drawer support fragments, Focus Mode support fragments, validation-prep utilities, and release-aware layer payload preparation.

It may support these object families as implementation helpers, not as authority:

- settlement;
- legal municipality;
- census place;
- historic townsite;
- ghost town;
- fort;
- depot or transport facility when handled as settlement/infrastructure context;
- mission;
- reservation community;
- neighborhood;
- unincorporated place;
- infrastructure asset;
- infrastructure facility;
- infrastructure network;
- network node;
- service area;
- dependency summary;
- condition observation when policy permits internal handling;
- public-safe layer descriptor fragments;
- Evidence Drawer and Focus Mode payload fragments after evidence, policy, review, catalog, release, and sensitivity filtering.

The package exists to keep reusable domain logic out of apps, one-off scripts, raw data folders, schemas, policy roots, release roots, and public UI shells. It should be boring, deterministic, testable, and reversible.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package may help prepare candidate objects moving through the lifecycle, but it must not collapse lifecycle phases. Promotion remains a governed state transition, not a package function that publishes data by itself.

## Repo fit

Directory ownership is by responsibility root, not by topic. This README belongs under `packages/` because the requested artifact is a reusable implementation package README. It is not a schema, contract, policy document, data lifecycle object, release decision, proof, receipt, registry, app, connector, or pipeline.

| Concern | Canonical owner | This package role |
|---|---|---|
| Human domain doctrine | `docs/domains/settlements-infrastructure/` | Link to docs; do not replace them. |
| Object meaning | `contracts/domains/settlements-infrastructure/` | Consume semantic contracts after confirmed; do not define canonical meaning here. |
| Machine shape | `schemas/contracts/v1/domains/settlements-infrastructure/` | Validate against schemas; do not become schema authority. |
| Allow / deny / restrict / abstain | `policy/domains/settlements-infrastructure/`, `policy/sensitivity/`, `policy/release/` | Consume policy decisions; do not decide public release alone. |
| Source identity, rights, cadence, sensitivity | `data/registry/settlements-infrastructure/` or source registry lanes | Reference descriptors through governed interfaces; do not become the source registry. |
| Test fixtures | `fixtures/domains/settlements-infrastructure/` | Read fixtures; do not hide test truth in package internals. |
| Tests | `tests/domains/settlements-infrastructure/` | Provide code under test; tests live in test roots unless repo convention says otherwise. |
| Lifecycle records | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` | Prepare payloads; do not store lifecycle data here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Emit payload candidates only through governed pipeline writers. |
| Release decisions and rollback | `release/settlements-infrastructure/` | Consume release state; do not publish. |
| Public UI | `apps/explorer-web/`, `packages/ui/`, `packages/maplibre/` | Provide safe DTO helpers only after evidence/policy/release filtering. |

## What this package may own

The package may own reusable implementation logic such as:

- settlement candidate normalization;
- infrastructure candidate normalization;
- domain-specific identity material builders;
- stable digest material preparation;
- source-role preserving record adapters;
- legal municipality versus census-place distinction helpers;
- historic settlement uncertainty helpers;
- public-safe geometry transform helpers after a policy decision is supplied;
- infrastructure exposure-class helpers after policy terms are supplied;
- condition-observation metadata shaping for restricted review contexts;
- graph-projection input preparation;
- layer-manifest payload helper functions;
- Evidence Drawer projection helpers that require EvidenceBundle references;
- Focus Mode context-fragment helpers that cannot answer without evidence and policy state;
- finite outcome wrappers for package-local validation results;
- deterministic fixture utilities.

The package should be library-like: functions should be deterministic where practical, side effects should be explicit, and every public helper should make evidence, policy, time, release, and sensitivity requirements visible in its name, type signature, validation result, or returned envelope.

## What this package must not own

This package must not own or become authority for:

- raw source downloads;
- live source fetchers;
- source credentials;
- source descriptors;
- rights decisions;
- canonical contracts;
- canonical schemas;
- release policy;
- sensitivity policy;
- review decisions;
- lifecycle data stores;
- public tiles;
- release manifests;
- rollback cards;
- proof packs;
- receipt records;
- catalog records;
- public API routes;
- direct database connections for public clients;
- direct model-runtime outputs;
- infrastructure exact-location publication decisions;
- legal municipality truth without evidence;
- critical infrastructure condition or operator-sensitive public outputs.

> [!WARNING]
> A helper that produces a map label, graph node, DTO fragment, AI context block, layer descriptor, or normalized candidate does not publish truth. Public truth requires EvidenceBundle support, policy state, validation, review where required, release state, correction path, and rollback target.

## Accepted inputs

The package may accept already-admitted, already-fetched, or synthetic fixture inputs. Production callers should pass source and policy context explicitly rather than allowing package functions to read from raw folders or source APIs.

| Input family | Minimum expectation | Package treatment |
|---|---|---|
| Settlement candidate records | Source descriptor reference, evidence refs, place type, time fields, rights and sensitivity metadata. | Normalize into validation-ready structures; never treat as released truth. |
| Legal municipality records | Legal-status source role, legal-status event refs, time scope, evidence refs. | Preserve legal status as evidence-bound; do not infer from a name, map label, or census record alone. |
| Census place records | Census source role, vintage, geometry or summary geography, evidence refs. | Preserve census semantics; do not imply incorporation or local legal authority. |
| Historic townsite / ghost town records | Evidence refs, time span, uncertainty, source role, interpretive posture. | Preserve uncertainty; avoid over-precise public display. |
| Fort / mission / reservation community records | Evidence refs, source role, stewardship/sensitivity metadata, cultural review state if applicable. | Preserve review and sensitivity requirements; do not expose restricted exact geometry. |
| Infrastructure asset records | Asset/facility/network role, source role, evidence refs, sensitivity, exposure class, time, condition metadata. | Prepare restricted or public-safe candidates based on supplied policy state. |
| Boundary geometry candidates | CRS, precision, source geometry hash, valid time, retrieval time, source role. | Normalize for validation; never publish exact restricted geometry by default. |
| Service area / dependency candidates | Evidence refs, method, uncertainty, aggregation level, sensitivity. | Preserve as derived context; do not transform into canonical facility truth. |
| Public-safe layer fragments | Release ID, layer manifest ref, public geometry or aggregate, evidence hooks. | Prepare DTO fragments only when release/policy state is supplied. |
| Synthetic fixtures | Fixture marker, test purpose, expected outcome, no live personal or sensitive source data. | Support tests and documentation only; never mingle with production evidence. |

## Excluded inputs and outputs

Do not pass these directly into package helpers unless a test explicitly verifies denial or quarantine behavior:

- unreviewed raw source payloads;
- source credentials or API tokens;
- undocumented source exports;
- records with missing source role;
- records with unknown rights;
- records with missing EvidenceRefs;
- exact critical infrastructure geometry without exposure class and review state;
- operator-sensitive details without access context;
- bridge/utility/facility condition observations without observed time and policy context;
- living-person residence or ownership assertions without the People/DNA/Land policy path;
- emergency alert or life-safety instruction payloads;
- generated summaries that pretend to be evidence.

Package outputs must remain one of these safe forms:

- normalized candidate;
- validation input;
- policy input;
- EvidenceBundle projection request;
- public-safe DTO fragment after policy/release context is supplied;
- graph-projection input;
- transform receipt payload candidate;
- deterministic test fixture result;
- finite outcome envelope.

## Domain model boundaries

Settlements and infrastructure are visually close on a map, but KFM must not collapse their meanings.

| Object or concept | Keep separate from | Reason |
|---|---|---|
| Legal municipality | Census place, map label, settlement name, historic townsite | Legal status needs source-specific evidence and time scope. |
| Census place | Legal municipality or incorporated city | Census geography is an administrative/statistical construct. |
| Settlement | Infrastructure asset or service area | A place context is not automatically an asset or network. |
| Historic townsite | Current municipality or land parcel | Historic interpretation requires time and evidence boundaries. |
| Ghost town | Abandoned property status or folklore | Existence and abandonment claims need evidence and uncertainty. |
| Fort | Archaeological site, military site, tourist site, settlement | Role and time scope determine meaning and sensitivity. |
| Depot | Rail/roads facility, settlement nucleus, historic place | Cross-lane relation must preserve source role and EvidenceBundle support. |
| Infrastructure asset | Facility, network node, service area, operator | Each has different sensitivity and evidence requirements. |
| Condition observation | Asset identity or public instruction | Observations require observed time and exposure controls. |
| Dependency summary | Canonical network edge | Derived dependencies must not become root truth. |
| Public-safe geometry | Canonical/internal geometry | Public geometry may be generalized, redacted, aggregated, or delayed. |

## Settlement and infrastructure source-role rules

Source role must travel with every consequential candidate. A package helper that strips source role is unsafe.

| Source role family | Example use | Package rule |
|---|---|---|
| Legal / administrative | Incorporation, annexation, boundary, ordinance, legal status event | Preserve as legal-status evidence, with time scope and citation. |
| Census / statistical | Census place, population summary, vintage boundary | Preserve vintage and statistical semantics; do not imply local legal authority. |
| Historic / archival | Historic townsite, ghost town, fort, mission, depot context | Preserve uncertainty, date range, interpretive status, and rights. |
| Infrastructure operator / administrative | Utility, facility, network, asset, service area | Preserve operator-sensitive fields and access class; public output defaults to review. |
| Condition / inspection / observation | Bridge/facility/condition records, observed status | Preserve observed_at and source role; public release requires policy and review state. |
| Derived / modeled | Dependency summary, graph projection, service-area aggregate | Mark as derivative; never replace canonical evidence. |
| Generated / AI | Summary, explanation, draft steward note | Keep evidence-subordinate; must not become source evidence. |

## Identity, time, and digest rules

Identity must be deterministic where practical and must not depend on unstable display labels alone.

Recommended package-local identity material:

```text
source_id + object_role + temporal_scope + normalized_geometry_or_place_digest + normalized_attribute_digest
```

The package should preserve these time concepts when available:

| Time field | Meaning | Package expectation |
|---|---|---|
| `source_time` | Time asserted or used by the source. | Preserve when present; do not replace with retrieval time. |
| `observed_at` | Time a condition or observation was observed. | Required for condition-like infrastructure observations. |
| `valid_time` | Time interval when a statement is valid. | Required for legal status, historic status, boundary, and condition claims where material. |
| `retrieved_at` | Time KFM obtained or checked the source. | Important for source freshness, but not proof of historical validity. |
| `release_time` | Time a public artifact was released. | Release metadata belongs to release roots; package may consume it. |
| `corrected_at` | Time a correction/supersession was recorded. | Package may preserve references; correction authority is outside the package. |

Digest rules:

- normalize before hashing;
- exclude volatile timestamps from semantic hashes unless the timestamp is part of the claim;
- hash geometry after CRS and precision normalization;
- include time scope where it changes meaning;
- include object role to avoid cross-type collisions;
- retain source ID and evidence reference in digest material;
- return digest material and computed hash separately when practical for inspectability.

## Public-safe geometry and exposure controls

Public geometry must be treated as a released derivative, not as canonical geometry.

| Geometry or exposure class | Public behavior | Required support |
|---|---|---|
| Public exact allowed | May be shown exactly after release. | Evidence, rights, source role, validation, release, and no sensitivity block. |
| Public generalized | Show generalized, buffered, aggregated, gridded, or simplified geometry. | Transform receipt with method, reason, source geometry hash, public geometry hash, and policy reference. |
| Restricted exact | Exact geometry not public. | Access profile, reviewer state, audit path, and denial/generalization for public path. |
| Steward-only | Only authorized review/steward workflows. | Auth, role, audit, no public leakage. |
| Denied | Do not expose. | Policy reason and finite outcome. |
| Quarantine | Hold pending rights/sensitivity/evidence resolution. | Quarantine reason and review path. |

For settlements and infrastructure, public-safe behavior must especially protect:

- critical infrastructure exact geometry;
- utility networks and dependencies;
- sensitive facility locations;
- operator-sensitive details;
- condition/inspection observations;
- security-relevant dependencies;
- private-property-sensitive or living-person-adjacent details;
- culturally sensitive historic or reservation-community context;
- unsupported legal-status claims;
- emergency or life-safety interpretation.

## Trust-boundary flow

```mermaid
flowchart LR
  Raw[RAW source payload or reference] --> Work[WORK candidate normalization]
  Work --> Gate1{Schema, source role, rights, evidence, time, sensitivity}
  Gate1 -->|fail| Quarantine[QUARANTINE with reason]
  Gate1 -->|pass| Processed[PROCESSED normalized candidate]
  Processed --> Bundle[EvidenceBundle / catalog / graph candidate]
  Bundle --> Gate2{Policy, validation, proof, review, release}
  Gate2 -->|deny| Deny[DENY / restricted / withheld]
  Gate2 -->|abstain| Abstain[ABSTAIN insufficient support]
  Gate2 -->|pass| Published[PUBLISHED governed artifact]
  Published --> API[Governed API]
  Published --> Map[MapLibre public-safe layer]
  Published --> Drawer[Evidence Drawer]
  Published --> Focus[Focus Mode]

  Package[packages/domains/settlements-infrastructure] -. helper code only .-> Work
  Package -. helper code only .-> Processed
  Package -. payload helpers .-> Bundle
  Package -. released DTO helpers .-> API

  Raw -. no direct public access .x API
  Work -. no direct public access .x Map
  Quarantine -. no direct public access .x Focus
```

## Proposed directory map

> [!NOTE]
> This is a PROPOSED package-local map. Confirm against package manager, import style, repo conventions, and existing files before merging.

```text
packages/domains/settlements-infrastructure/
├── README.md
├── pyproject.toml                  # NEEDS VERIFICATION if Python package is used
├── package.json                    # NEEDS VERIFICATION if JS/TS package is used
├── src/
│   ├── README.md
│   └── settlements_infrastructure/
│       ├── README.md
│       ├── __init__.py
│       ├── identity.py
│       ├── time_semantics.py
│       ├── normalization.py
│       ├── settlement_types.py
│       ├── infrastructure_types.py
│       ├── source_roles.py
│       ├── public_geometry.py
│       ├── exposure.py
│       ├── graph_projection.py
│       ├── evidence_payloads.py
│       ├── layer_payloads.py
│       ├── focus_mode_context.py
│       └── outcomes.py
├── settlement/
│   └── README.md                   # optional narrow helpers; avoid parallel authority
├── infrastructure/
│   └── README.md                   # optional narrow helpers; avoid parallel authority
├── identity/
│   └── README.md
├── normalizers/
│   └── README.md
├── public_geometry/
│   └── README.md
├── exposure/
│   └── README.md
├── graph_projection/
│   └── README.md
├── layer_manifests/
│   └── README.md
└── fixtures/
    └── README.md                   # only lightweight package-local examples if repo convention allows
```

Package-local examples are allowed only when they are clearly synthetic and do not compete with `fixtures/domains/settlements-infrastructure/`.

## Finite outcomes

Package functions that validate, transform, classify, or prepare public-safe outputs should return finite, inspectable outcomes rather than raising ambiguous success/failure states.

| Outcome | Meaning | Typical package use |
|---|---|---|
| `ANSWER` | Enough evidence, policy, validation, and release context exists for the requested package operation. | Build public-safe DTO fragment or normalized validated result. |
| `ABSTAIN` | The package cannot support the operation from available evidence or context. | Missing evidence, missing time scope, ambiguous source role. |
| `DENY` | Policy, sensitivity, rights, release state, or exposure class blocks the operation. | Restricted exact geometry, infrastructure exposure risk, absent release state. |
| `ERROR` | Input is malformed, unsupported, or package execution failed. | Schema mismatch, invalid CRS, invalid enum, impossible geometry. |
| `QUARANTINE` | Candidate should be held for steward or validator review. | Rights unknown, sensitivity unresolved, source role unclear. |

Every non-`ANSWER` outcome should carry a stable reason code and enough diagnostic context for tests, receipts, review, or rollback.

## Validation and quality gates

Minimum package-level gates before treating this README as merge-ready:

| Gate | Expected check | Status |
|---|---|---|
| Path conformance | Confirm `packages/domains/settlements-infrastructure/` is accepted by Directory Rules and current repo conventions. | NEEDS VERIFICATION |
| Naming | Confirm canonical package lane is plural `settlements-infrastructure`, not singular `settlement` or split package names. | NEEDS VERIFICATION |
| Import namespace | Confirm import namespace such as `settlements_infrastructure` and avoid hyphenated import names. | PROPOSED |
| Schema alignment | Confirm package helpers validate against `schemas/contracts/v1/domains/settlements-infrastructure/`. | NEEDS VERIFICATION |
| Contract alignment | Confirm package terms match `contracts/domains/settlements-infrastructure/`. | NEEDS VERIFICATION |
| Policy alignment | Confirm deny/restrict/generalize behavior is delegated to policy roots. | NEEDS VERIFICATION |
| Fixture safety | Confirm no real sensitive infrastructure, operator, condition, private-property, or living-person data appears in fixtures. | NEEDS VERIFICATION |
| Evidence checks | Confirm public outputs require EvidenceRefs / EvidenceBundle support. | NEEDS VERIFICATION |
| Public path checks | Confirm public clients cannot reach RAW, WORK, QUARANTINE, internal stores, direct DBs, source APIs, or model runtime output. | NEEDS VERIFICATION |
| Rollback checks | Confirm released outputs have rollback targets and correction paths. | NEEDS VERIFICATION |

Suggested first tests after implementation exists:

- legal municipality without legal-status evidence returns `DENY` or `ABSTAIN`;
- census place is not treated as legal municipality;
- historic townsite uncertainty is preserved;
- restricted infrastructure exact geometry returns `DENY` for public DTO requests;
- public generalized geometry requires transform receipt inputs;
- condition observation without `observed_at` returns `ERROR` or `ABSTAIN`;
- missing EvidenceRefs block public output;
- missing release state blocks public output;
- graph projection is marked derivative;
- generated Focus Mode context cannot claim root truth.

## Development rules

1. Keep helpers deterministic where practical.
2. Pass source role, evidence refs, rights, sensitivity, time scope, review state, and release state explicitly.
3. Do not fetch live sources from package helpers.
4. Do not read RAW, WORK, QUARANTINE, or internal stores from public-facing helpers.
5. Do not embed policy decisions as constants when policy roots should decide.
6. Do not create package-local schema authority.
7. Do not create package-local release authority.
8. Do not expose exact critical infrastructure geometry by default.
9. Do not generate public DTO fragments without release and policy context.
10. Do not treat graph projections, tiles, labels, summaries, or AI context as sovereign truth.
11. Keep error and denial reason codes stable.
12. Prefer small pure functions with explicit inputs and typed outputs.
13. Keep fixture examples synthetic and clearly marked.
14. Update docs when behavior changes materially.

## Definition of done

This README is ready for a real PR only when maintainers can check all of the following:

- [ ] Target path is confirmed or ADR-backed.
- [ ] Package owner is assigned.
- [ ] Import namespace is confirmed.
- [ ] Adjacent package READMEs exist where needed.
- [ ] Package metadata exists if code exists.
- [ ] Contracts and schemas are referenced from their canonical homes.
- [ ] Policy delegation is explicit and tested.
- [ ] Synthetic fixtures exist for valid and invalid cases.
- [ ] Tests cover settlement legal status, census distinction, infrastructure exposure, public-safe geometry, missing evidence, and release-state denial.
- [ ] Public outputs require EvidenceBundle, validation, policy, review where required, release state, correction path, and rollback target.
- [ ] No public helper reads RAW, WORK, QUARANTINE, source APIs, direct DBs, or direct model outputs.
- [ ] Rollback and correction paths are documented for released derivatives.

## Evidence basis

| Source | Status used here | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED doctrine | Responsibility roots, `packages/` as shared implementation root, domain-as-segment placement, lifecycle split, schema/policy/release separation. | Does not prove this package exists in the repo. |
| `kfm_settlements_infrastructure_extended_pro_plan_2026-04-21.pdf` | Domain blueprint / LINEAGE / PROPOSED implementation | Settlement/infrastructure scope, critical-infrastructure sensitivity, tests, CI ideas, API/UI/Evidence Drawer/Focus Mode patterns, no-repo implementation boundary. | PDF-only plan; does not prove implementation. |
| `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` | Domain atlas / doctrine synthesis | Object-family vocabulary, cross-lane relations, lifecycle, public-safe viewing products, finite outcomes, publication/correction/rollback posture. | Synthesis/atlas; requires repo verification before implementation claims. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | Synthesis / policy and domain boundary guidance | Anti-collapse rules for transport/settlements/infrastructure/geology, critical infrastructure exposure controls, source-role and public-safe geometry emphasis. | Does not settle current source rights, exact schemas, or repo maturity. |

## Verification checklist

- [ ] Confirm `packages/domains/settlements-infrastructure/` exists or create it through a governed PR.
- [ ] Confirm no conflict with `packages/domains/settlement/` or other settlement package aliases.
- [ ] Confirm owning steward and reviewers.
- [ ] Confirm package manager and import namespace.
- [ ] Confirm links to `docs/domains/settlements-infrastructure/` exist or update to actual paths.
- [ ] Confirm schemas live under `schemas/contracts/v1/domains/settlements-infrastructure/` or update by ADR.
- [ ] Confirm contracts live under `contracts/domains/settlements-infrastructure/`.
- [ ] Confirm policy lives under `policy/domains/settlements-infrastructure/` and related sensitivity/release roots.
- [ ] Confirm tests live under `tests/domains/settlements-infrastructure/` or accepted test convention.
- [ ] Confirm fixtures use synthetic or rights-cleared data only.
- [ ] Confirm release and rollback records are not stored in the package.
- [ ] Confirm public clients use governed APIs and released artifacts only.
- [ ] Confirm restricted infrastructure geometry cannot leak through layer helpers, graph projection helpers, Evidence Drawer payloads, or Focus Mode context.
- [ ] Confirm generated language remains evidence-subordinate.

## Rollback

Rollback is required if this package path, README, or later implementation weakens source integrity, creates parallel schema/contract/policy/source/release/proof/receipt authority, bypasses public-governed interfaces, exposes restricted infrastructure details, collapses census/legal/historic distinctions, or claims implementation maturity without proof.

Rollback target:

```text
git rm -r packages/domains/settlements-infrastructure
```

Use `git mv` rather than delete/recreate if the corrective action is a rename into a confirmed package lane. Preserve history, record the drift or ADR decision, and update links from docs, tests, fixtures, schemas, policies, release records, and package manifests.

<details>
<summary>Maintainer notes</summary>

- Treat `packages/domains/settlements-infrastructure/README.md` as a package boundary document.
- Treat `docs/domains/settlements-infrastructure/README.md` as the human domain landing page.
- Treat `schemas/contracts/v1/domains/settlements-infrastructure/` as the default schema home unless an accepted ADR changes it.
- Treat `policy/domains/settlements-infrastructure/` and sensitivity/release policy roots as the public-exposure decision homes.
- Treat `release/settlements-infrastructure/` as the release decision / rollback home, not as package code.
- Treat `data/receipts/` and `data/proofs/` as trust-bearing emitted record homes, not as package examples.
- If a singular `settlement` package remains in parallel, decide whether it is a compatibility alias, a narrow subpackage, or drift.

</details>
