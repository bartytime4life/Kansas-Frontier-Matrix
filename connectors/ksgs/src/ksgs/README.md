<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksgs-src-package-readme
title: connectors/ksgs/src/ksgs/ — KSGS Greenfield Package Scaffold
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · KGS source steward · Geology steward · Hydrology steward · Rights reviewer · Sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; greenfield-scaffold; noncanonical-path; path-and-slug-conflict; source-admission; no-network; no-activation; no-publication
proposed_path: connectors/ksgs/src/ksgs/README.md
truth_posture: CONFIRMED 0.0.0 greenfield scaffold and placeholder package files / KGS connector path CONFLICTED / connector-local descriptor NONCONFORMING and non-authoritative / executable fetch, admission, validation, lifecycle handoff, tests, and CI ABSENT or UNKNOWN
related:
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../tests/README.md
  - ../../../kgs/README.md
  - ../../../geology/kgs/README.md
  - ../../../kansas/README.md
  - ../../../../docs/sources/catalog/kansas/ksgs.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../data/registry/sources/README.md
  - ../../../../policy/rights/README.md
  - ../../../../policy/sensitivity/README.md
tags: [kfm, connectors, ksgs, kgs, package, python, greenfield, compatibility, path-conflict, geology, hydrology, source-admission, rights, sensitivity, no-network, no-publication]
notes:
  - "Direct reads at base commit 52f90317a1d3cc54010ae862d6f7f92ff2d18105 confirm package version 0.0.0, an empty __init__.py, one-line fetch.py and admit.py placeholders, and a four-field descriptor.yaml placeholder."
  - "The proposed connectors/kansas/kgs/ child is absent at the inspected base; repository documents conflict among connectors/kgs/, connectors/ksgs/, connectors/geology/kgs/, proposed connectors/kansas/kgs/, and product-specific top-level KGS lanes."
  - "The connector-local descriptor uses legacy/minimal fields and does not satisfy the richer SourceDescriptor v1 schema; it is not a registry record or activation decision."
  - "No live KGS source, current terms, credentials, payload, fixture, executable test, runtime log, lifecycle artifact, or deployment state was inspected for this revision."
  - "This package performs no fetch, admission decision, lifecycle write, release, or publication in its current state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSGS Greenfield Package Scaffold

> Repository-grounded boundary for the import namespace at `connectors/ksgs/src/ksgs/`. The package exists, but it is a non-operational `0.0.0` scaffold inside an unresolved KGS connector topology. It is not an active connector, a SourceDescriptor authority, a lifecycle writer, or a publication surface.

**Status:** `draft` · `CONFIRMED greenfield scaffold` · `CONFLICTED connector placement` · `no supported command` · `no live-network behavior` · `no activation` · `no publication`

> [!IMPORTANT]
> At the pinned evidence base, `fetch.py` and `admit.py` contain comments only, `__init__.py` is empty, and `descriptor.yaml` is a nonconforming placeholder. Nothing in this package fetches KGS material, makes an admission decision, emits a candidate envelope, or writes to a KFM lifecycle root.

> [!CAUTION]
> Do not add operational code here merely because the import package exists. The repository has not settled the canonical KGS connector path or the `kgs` versus `ksgs` identity. Resolve placement, descriptor authority, product boundaries, ownership, and migration before this package gains behavior.

## Quick links

[Purpose](#purpose) · [Current package](#current-package) · [Repository fit](#repository-fit) · [Descriptor conflict](#descriptor-conflict) · [Product boundaries](#product-boundaries) · [Inputs and outputs](#inputs-and-outputs) · [Implementation boundary](#implementation-boundary) · [Validation](#validation) · [Evidence](#evidence) · [Review and rollback](#review-and-rollback) · [Definition of done](#definition-of-done)

---

## Purpose

This README describes what the current Python namespace is, what it demonstrably does not do, and which gates must close before implementation can begin.

Today the package is useful only as:

- a visible marker for the live `ksgs` scaffold;
- a place to document the unresolved connector-path and slug conflict;
- a fail-closed boundary around placeholder code and metadata;
- a migration input for a future KGS connector decision.

It does not prove that the `ksgs` package name should survive, that this directory is canonical, or that any KGS product is approved for access or admission.

---

## Current package

Direct file reads at base commit `52f90317a1d3cc54010ae862d6f7f92ff2d18105` confirm this inspected surface:

```text
connectors/ksgs/
├── pyproject.toml                  # project kfm-connector-ksgs, version 0.0.0
├── src/
│   ├── README.md                   # source-layout documentation
│   └── ksgs/
│       ├── README.md               # this package boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # one-line greenfield comment
│       ├── admit.py                # one-line greenfield comment
│       └── descriptor.yaml         # four-field greenfield placeholder
└── tests/
    └── README.md                   # test-boundary documentation
```

| Surface | Confirmed state | Consequence |
|---|---|---|
| [`pyproject.toml`](../../pyproject.toml) | Declares `kfm-connector-ksgs` at `0.0.0`; no build system, dependencies, Python constraint, package-discovery rule, or command is declared. | Buildability, installability, supported runtime, and public API are `UNKNOWN`. |
| [`__init__.py`](./__init__.py) | Empty file. | No package API or import-time behavior is implemented. |
| [`fetch.py`](./fetch.py) | Comment-only placeholder. | No transport, endpoint, authentication, retry, timeout, rate-limit, pagination, caching, or source-head behavior exists. |
| [`admit.py`](./admit.py) | Comment-only placeholder. | No validation, quarantine, admission, receipt, or handoff behavior exists. |
| [`descriptor.yaml`](./descriptor.yaml) | `name: ksgs`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Placeholder is incomplete, internally unsafe as an activation basis, and not authoritative. |
| [`tests/README.md`](../../tests/README.md) | Documentation contract only in the directly inspected path. | Executable package tests and package-specific CI remain absent or `UNKNOWN`. |

The inspected file set is not a substitute for a recursive tree receipt. Any additional inventory claim must be regenerated from the repository at the commit under review.

---

## Repository fit

KFM's connector root owns source-specific fetch, probe, packaging, and admission support. Source doctrine, registry records, schemas, policy decisions, evidence closure, release decisions, and public-client behavior live elsewhere.

The KGS connector topology is currently conflicted:

| Surface | Observed posture | Package implication |
|---|---|---|
| `connectors/ksgs/` | Live `0.0.0` greenfield scaffold; its existing READMEs call it noncanonical. | Presence does not grant canonical status or permission to implement. |
| `connectors/kgs/` | Top-level compatibility README. | Competing source-first name; no package behavior was established by this review. |
| `connectors/geology/kgs/` | Newer README-only compatibility pointer; rejects domain-scoped implementation and marks canonical placement conflicted. | Useful conflict evidence, not an implementation home. |
| `connectors/kansas/kgs/` | Proposed by the KGS source catalog, but an exact read returned `404` at the pinned base. | Do not describe it as a present or confirmed canonical child. |
| `connectors/kgs_surficial/`, `connectors/kgs_bedrock/`, `connectors/kgs_oil_gas_wells/`, `connectors/kgs_kdhe_wwc5/`, `connectors/kgs_las/` | Product-specific compatibility README paths are indexed. | Their existence adds migration scope; it does not activate products or settle packaging. |
| `docs/sources/catalog/kansas/ksgs.md` | Draft catalog entry retains the `ksgs` document slug and proposes a `kgs` connector child. | Human-facing doctrine input; not source registry or activation authority. |

> [!NOTE]
> Directory-level documentation is inconsistent in age and certainty. The newer repository-grounded `connectors/geology/kgs/README.md` and direct path probes outrank stale claims that `connectors/kansas/kgs/` already exists or is conclusively canonical.

Choosing, renaming, consolidating, or deleting a KGS connector lane affects imports, source IDs, descriptors, fixtures, receipts, and lineage. That decision requires an accepted ADR or explicit migration plan; this README does not make it.

---

## Descriptor conflict

`descriptor.yaml` is not a usable `SourceDescriptor`.

| Connector-local field | Current value | Current contract posture |
|---|---|---|
| `name` | `ksgs` | Not the canonical required `source_id`; the publisher abbreviation and package slug are themselves conflicted. |
| `role` | `TBD` | Legacy alias; `TBD` is not an accepted source role. KGS products require independent role decisions. |
| `rights` | `TBD` | Unresolved rights must fail closed. |
| `sensitivity_floor` | `public` | Legacy alias and unsafe as a permissive default while rights, product, geometry, and review state are unresolved. |

The inspected SourceDescriptor v1 schema requires a much richer, closed object including identity, descriptor version, source type and role, authority rank, publisher, steward, rights, sensitivity, cadence, access, citation, source head, admissibility limits, public-release posture, review state, release state, and lifecycle state.

The same schema declares connector-local minimal fields as deprecated migration aliases. It also requires public release to remain false when rights are unknown, unasserted, or denied, and requires review for restricted or unknown sensitivity.

Therefore:

- do not load `descriptor.yaml` as activation authority;
- do not infer that `sensitivity_floor: public` makes any KGS record public-safe;
- do not fill `role` once at publisher level for every KGS product;
- do not place the authoritative registry instance in this package;
- do not activate a connector until a conforming product-specific descriptor, review state, and activation decision exist in accepted authority surfaces.

The machine-readable source authority register is currently `PROPOSED` with `entries: []`. The rights and sensitivity policy READMEs are greenfield stubs. Those facts reinforce a default-deny posture; they do not authorize local substitutes.

---

## Product boundaries

KGS is a publisher family, not one interchangeable payload. A future accepted connector must preserve product identity and independently govern at least these documented families:

| Product family | Required distinctions | Denied collapse |
|---|---|---|
| Surficial and bedrock geologic maps | Map/unit identity, compilation role, scale, vintage, CRS/datum, geometry, source URI. | Map compilation presented as direct observation or current site condition. |
| Oil-and-gas wells and production | Well, lease/field, reporting period, record type, source role, geometry and uncertainty. | KGS observation or aggregate presented as KCC regulatory determination, reserve, forecast, or per-place truth. |
| WWC5 water-well records | Joint-program identity, well/completion identity, PLSS derivation, coordinate precision, disclaimer, vintage. | Completion record presented as current water quality, aquifer condition, safe supply, or exact public location by default. |
| LAS logs and well tops | Well/log/curve/top identity, units, depth reference and datum, interpretation lineage, vintage. | Interpreted top presented as measured curve, canonical geology, or engineering/drilling advice. |
| Geoportal resources | Resource-specific identity, access method, schema, role, rights, cadence, and geometry. | Mixed portal resources admitted under one publisher-wide role or descriptor. |

One governed capture may serve multiple downstream domains, but Geology, Hydrology, and Environment consumers must not independently recapture the same source product or erase shared provenance.

Exact wells, boreholes, samples, logs, private locations, and harmful cross-source joins must fail closed. PLSS-derived coordinates must retain derivation level and uncertainty. Public availability upstream is not equivalent to KFM rights clearance, sensitivity clearance, or release approval.

---

## Inputs and outputs

### Current inputs

None. The package declares no supported function, class, command, configuration contract, endpoint, credential variable, or fixture format.

### Current outputs

None. The package emits no payload, candidate envelope, receipt, validation report, RAW record, QUARANTINE record, or public artifact.

### Future admissible inputs

Only after placement and activation gates are accepted, a narrow package contract may accept:

- a conforming, reviewed, product-specific SourceDescriptor reference;
- an explicit activation decision and approved access configuration;
- caller-supplied bytes, files, or approved transport results;
- synthetic or rights-cleared fixtures for offline tests;
- explicit run identity, retrieval time, source-head evidence, and destination intent.

### Future admissible outputs

A future package may return deterministic parse results, validation failures, or RAW/QUARANTINE **candidate envelopes** to governed orchestration. It must not select public release, persist directly into lifecycle roots, or convert connector success into evidence or truth.

---

## Implementation boundary

### Allowed only after the path decision

- narrow, product-dispatched parsing and source-head helpers;
- explicit opt-in transport behind reviewed configuration;
- deterministic normalization that preserves source-native values and uncertainty;
- product, role, rights, sensitivity, geometry, datum, scale, depth, vintage, and disclaimer checks;
- structured errors suitable for abstention, denial, hold, or quarantine;
- side-effect-free candidate-envelope construction;
- offline, synthetic, negative-first fixtures and tests;
- a migration shim if the accepted ADR retains `ksgs` as a compatibility import.

### Forbidden

- network calls on import or by default;
- credentials, tokens, cookies, account data, or private endpoints in source, fixtures, docs, logs, or exceptions;
- publisher-wide default roles or permissive rights/sensitivity assumptions;
- authoritative SourceDescriptor instances or activation decisions inside the package;
- direct writes to RAW, QUARANTINE, receipts, processed, catalog, triplet, proof, release, or published roots;
- silent aliasing among `kgs`, `ksgs`, or product-specific paths;
- duplicate capture for separate consumer domains;
- reconstruction or exposure of withheld geometry;
- operational engineering, drilling, water-supply, hazard, reserve, investment, legal, or safety conclusions;
- claims of implementation, coverage, validation, activation, or CI maturity without current evidence.

There is intentionally no quickstart. A runnable example would imply an API and behavior that do not exist.

---

## Failure contract

A future implementation must fail deterministically and without sensitive payload echo. Minimum reason families include:

- unresolved connector path or source identity;
- missing, nonconforming, unreviewed, or inactive descriptor;
- unknown product or unsupported source shape;
- unresolved role, rights, attribution, disclaimer, or sensitivity;
- missing well/log/map/unit identity or source vintage;
- lost PLSS derivation, coordinate uncertainty, scale, CRS/datum, units, or depth reference;
- role collapse among observation, aggregate, regulatory, modeled, administrative, candidate, or interpreted material;
- denied network posture or unapproved host;
- attempted lifecycle persistence or public-release target.

Unknowns route to `DENY`, `ABSTAIN`, `HOLD`, or a QUARANTINE candidate. They never receive permissive defaults.

---

## Validation

No package build or test command is documented because none is supported by the inspected project metadata.

Before implementation maturity can be claimed, evidence must cover:

1. accepted KGS connector path, package/import name, source-ID convention, and losing-path migration;
2. complete recursive package and backlink inventory;
3. build backend, package discovery, supported Python versions, dependency policy, and clean install/import;
4. product-specific conforming descriptors and explicit activation decisions;
5. reviewed access methods, current terms, attribution, redistribution, cadence, and source schemas;
6. no-network default and host/credential controls for opt-in transport;
7. synthetic or rights-cleared fixtures with negative-path coverage;
8. source-role, product-identity, KGS/KCC, geometry, PLSS, datum, scale, depth, disclaimer, rights, and sensitivity tests;
9. deterministic candidate-envelope and lifecycle-boundary tests;
10. CI discovery and passing package-specific evidence.

Documentation checks for this revision should include one H1, balanced fences, working repository-relative links, no remote badge images, no credential-like strings, a final newline, and an exact one-file diff.

---

## Evidence

Evidence for this revision is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at commit `52f90317a1d3cc54010ae862d6f7f92ff2d18105`.

| Evidence | Status | Supports | Does not support |
|---|---|---|---|
| [`connectors/ksgs/pyproject.toml`](../../pyproject.toml) | `CONFIRMED` | Project name and version `0.0.0`. | Buildability, dependencies, installability, API, or command. |
| Package files under this path | `CONFIRMED` for exact reads | Empty initializer; comment-only fetch/admit placeholders; four-field descriptor placeholder. | Executable behavior, exhaustive recursive inventory, validation, or activation. |
| [`connectors/ksgs/tests/README.md`](../../tests/README.md) | `CONFIRMED` | Intended offline compatibility-test posture. | Executable tests or CI success. |
| [`connectors/geology/kgs/README.md`](../../../geology/kgs/README.md) | `CONFIRMED` | Newer repository-grounded path-conflict and source-first compatibility analysis. | Accepted canonical path or migration. |
| [`docs/sources/catalog/kansas/ksgs.md`](../../../../docs/sources/catalog/kansas/ksgs.md) | `CONFIRMED draft` | KGS product-family and slug/path proposal context. | Registry authority, current upstream behavior, rights clearance, or activation. |
| [`contracts/source/source_descriptor.md`](../../../../contracts/source/source_descriptor.md) and [paired singular-path schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) | `CONFIRMED draft/PROPOSED` | Richer descriptor contract, legacy-field migration, and fail-closed constraints. | Accepted plural-path migration, persisted KGS descriptor, or runtime enforcement. |
| [`control_plane/source_authority_register.yaml`](../../../../control_plane/source_authority_register.yaml) | `CONFIRMED` | Register is `PROPOSED` and contains `entries: []`. | Any KGS activation decision. |
| [Rights](../../../../policy/rights/README.md) and [sensitivity](../../../../policy/sensitivity/README.md) README files | `CONFIRMED` | Both are greenfield stubs. | Executable or reviewed KGS policy. |
| Exact `connectors/kansas/kgs/README.md` probe | `CONFIRMED absent at base` | Proposed child README was not present at the pinned commit. | Permanent nonexistence or final path decision. |

Not inspected: live KGS services, current terms, credentials, source payloads, private locations, runtime logs, deployed configuration, emitted receipts, or public clients. Treat all associated claims as `UNKNOWN` or `NEEDS VERIFICATION`.

---

## Review and rollback

Review changes here as connector-placement, source-identity, packaging, source-role, rights, sensitivity, subsurface-location, geometry, and lifecycle-boundary changes—even when the diff is documentation-only.

Rollback this README revision if it is used to:

- treat this package or any competing path as canonical without an accepted decision;
- activate the placeholder descriptor;
- infer public safety from `sensitivity_floor: public`;
- claim working fetch, admission, tests, fixtures, CI, or lifecycle output;
- collapse KGS products or KGS observations into regulatory or generated truth;
- bypass rights, sensitivity, descriptor, activation, evidence, release, correction, or rollback gates.

Before merge, close the draft change and abandon its scoped branch. After merge, create a transparent revert of the documentation commit; do not rewrite shared history. The baseline target blob is `e5f0501777f22ccaf3003d628b1f225e2b1a251d` at base commit `52f90317a1d3cc54010ae862d6f7f92ff2d18105`.

---

## Definition of done

### Documentation boundary

- [x] Current package files and `0.0.0` maturity are explicit.
- [x] Placeholder fetch, admit, and descriptor behavior is not overstated.
- [x] Path and slug conflicts are visible.
- [x] Descriptor/schema conflict and default-deny result are explicit.
- [x] Product, role, geometry, rights, sensitivity, and KGS/KCC anti-collapse rules are explicit.
- [x] Current inputs, outputs, API, commands, tests, activation, and publication are stated as absent or unknown.
- [x] Evidence limits and rollback target are recorded.

### Implementation readiness

- [ ] Connector-path and slug ADR or migration plan is accepted.
- [ ] One package/import/source-ID strategy is accepted and losing paths are dispositioned.
- [ ] Owners and reviewers are assigned.
- [ ] Product-specific conforming descriptors and activation decisions exist.
- [ ] Current source access, schemas, terms, rights, attribution, disclaimers, cadence, and corrections are reviewed.
- [ ] Sensitive-location, PLSS, geometry, datum, scale, depth, and cross-source join policy is executable.
- [ ] Build, install, import, fixture, test, candidate-envelope, and lifecycle-boundary contracts are implemented.
- [ ] Default tests are offline, deterministic, negative-first, and CI-discovered.
- [ ] Correction, invalidation, migration, and rollback are tested.

Until every applicable implementation-readiness item closes, keep this package inert and fail closed.

<p align="right"><a href="#top">Back to top</a></p>
