<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksgs-src-readme
title: connectors/ksgs/src/ — KSGS Greenfield Source Layout
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · KGS source steward · Geology steward · Hydrology steward · Rights reviewer · Sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-12
policy_label: public-doctrine; source-layout; greenfield-scaffold; noncanonical-path; path-and-slug-conflict; no-network; no-activation; no-publication
current_path: connectors/ksgs/src/README.md
truth_posture: CONFIRMED source layout and 0.0.0 package scaffold / KGS connector and import path CONFLICTED / connector-local descriptor NONCONFORMING and non-authoritative / executable fetch, admission, validation, lifecycle handoff, tests, and deployment ABSENT or UNKNOWN
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d8d246bcd21b574c7691c396965b61d4548b30c3
  prior_blob: 45cb0900fc14bef569b69f972a4a8041c56f8cec
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - ../tests/README.md
  - ./ksgs/README.md
  - ../../kgs/README.md
  - ../../geology/kgs/README.md
  - ../../kansas/README.md
  - ../../../docs/sources/catalog/kansas/ksgs.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
tags: [kfm, connectors, ksgs, kgs, src, python, package-layout, greenfield, compatibility, path-conflict, geology, hydrology, source-admission, rights, sensitivity, no-network, no-publication]
notes:
  - "The inspected src layout contains this README and one ksgs package directory."
  - "The package directory contains README.md, an empty __init__.py, one-line fetch.py and admit.py placeholders, and a four-field descriptor.yaml placeholder."
  - "The parent pyproject.toml declares project name kfm-connector-ksgs and version 0.0.0 only; it does not prove a buildable, installable, or runnable package."
  - "The package-local descriptor is not a governed SourceDescriptor, registry record, activation decision, rights decision, sensitivity decision, or release authority."
  - "The proposed connectors/kansas/kgs/README.md path is absent at the pinned base; competing KGS connector and product paths remain unresolved."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry record, fixture, test, policy, schema, workflow, receipt, source activation, path move, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSGS Greenfield Source Layout

> Source-layout boundary for the repository-present Python scaffold at `connectors/ksgs/src/`. This directory organizes one non-operational `ksgs` package inside an unresolved KGS connector topology. It is not a connector authority, runtime, registry, policy engine, lifecycle store, or publication surface.

**Status:** `draft v0.2` · `CONFIRMED one-package scaffold` · `CONFLICTED connector/import placement` · `no supported command` · `no activation` · `no publication`

> [!IMPORTANT]
> The current source layout contains real placeholder files, not merely two READMEs. The `ksgs` initializer is empty, `fetch.py` and `admit.py` contain comments only, and `descriptor.yaml` is a four-field nonconforming placeholder. No executable source-admission behavior is established.

> [!WARNING]
> Do not add a second import package, operational client, or migration shim under this `src/` directory until the repository accepts one KGS connector path, package name, source-ID convention, and losing-path disposition. Directory presence does not settle `kgs` versus `ksgs`.

## Quick links

[Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Current layout](#current-layout) · [Inputs and outputs](#inputs-and-outputs) · [Allowed contents](#allowed-contents) · [Exclusions](#exclusions) · [Descriptor boundary](#descriptor-boundary) · [Runtime boundary](#runtime-and-admission-boundary) · [Validation](#validation) · [Related surfaces](#related-surfaces) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/ksgs/src/` is a Python source-layout container. Its only current child package is `ksgs/`, and that package is a `0.0.0` greenfield scaffold.

The layout may eventually organize narrow, source-specific code that:

- consumes caller-supplied, approved KGS source material or an explicitly reviewed transport result;
- preserves product identity, source role, rights, sensitivity, provenance, geometry, scale, datum, depth, units, uncertainty, disclaimer, and vintage;
- returns deterministic parse, validation, denial, abstention, hold, or RAW/QUARANTINE candidate results to caller-owned orchestration;
- supports an explicit compatibility import only if an accepted migration retains `ksgs`.

This directory cannot decide which competing KGS path is canonical, activate a source, make the package descriptor authoritative, write lifecycle state, close evidence, approve release, or publish KGS-derived claims.

---

## Authority level

**Implementation source layout inside a live but noncanonical greenfield scaffold. Final connector, distribution, import, and source-ID placement remain unresolved.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | `CONFIRMED` | Source-specific fetch and admission implementation belongs under `connectors/`; registry, contract, schema, policy, evidence, release, and publication authority remain elsewhere. |
| Current `src/` path | `CONFIRMED` | The target README and `ksgs/` package child exist at the pinned base. |
| Current package name | `CONFIRMED scaffold / CONFLICTED final` | The live import directory is `ksgs` and project metadata is `kfm-connector-ksgs`; neither is ratified as the final identity. |
| KGS connector path | `CONFLICTED` | Live and documented candidates include `connectors/ksgs/`, `connectors/kgs/`, `connectors/geology/kgs/`, proposed `connectors/kansas/kgs/`, and product-specific top-level paths. |
| Proposed Kansas child | `CONFIRMED absent at base` | An exact read of `connectors/kansas/kgs/README.md` returned `404`; catalog prose does not make the path present. |
| Package implementation | `GREENFIELD PLACEHOLDER` | Empty initializer and comment-only fetch/admit modules establish no supported behavior. |
| Package-local descriptor | `NONCONFORMING / DENY FOR AUTHORITY USE` | Four legacy/minimal fields do not satisfy the richer SourceDescriptor contract and cannot activate a source. |
| Tests and fixtures | `ABSENT AT NAMED PROBES / OTHERWISE UNKNOWN` | The test README exists; conventional `test_fetch.py`, `test_admit.py`, `conftest.py`, and `tests/fixtures/README.md` paths were absent. |
| Source access and activation | `UNKNOWN / DISABLED BY DEFAULT` | No approved endpoint, transport, credential mode, terms review, source head, product descriptor, or activation decision was verified. |
| Public output | `NONE` | The layout creates no public map, API response, well record, geology claim, hydrology claim, release artifact, or operational guidance. |

This README records repository state and safe layout constraints. It does not ratify the current slug, create the proposed Kansas child, or authorize implementation.

---

## Status

| Item | Current state | What that means |
|---|---|---|
| This README | `DRAFT v0.2` | Reviewable layout boundary, not runtime evidence. |
| Source-layout directory | `CONFIRMED` | One package child was directly inspected. |
| Project metadata | `0.0.0 PLACEHOLDER` | Name and version only; build backend, dependencies, supported Python, package discovery, and entry points are not declared. |
| Package initializer | `EMPTY` | No import surface, version export, registration, or initialization behavior. |
| Fetch and admit modules | `COMMENT-ONLY` | No endpoint access, parser, validator, finite outcome, receipt, or handoff. |
| Local descriptor | `UNSAFE PLACEHOLDER` | Unresolved role and rights plus `sensitivity_floor: public`; must fail closed. |
| Source authority register | `PROPOSED / EMPTY` | Inspected `entries: []`; no KGS activation record. |
| Rights and sensitivity policy | `GREENFIELD STUBS` | No executable KGS-specific clearance or public-release policy was established. |
| Runtime, tests, CI, deployment | `ABSENT or UNKNOWN` | Repository-wide CI success would not prove this package is implemented or activated. |

---

## Current layout

The following map is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `d8d246bcd21b574c7691c396965b61d4548b30c3` and the exact paths read for this revision:

```text
connectors/ksgs/
├── pyproject.toml                  # project kfm-connector-ksgs, version 0.0.0
├── src/
│   ├── README.md                   # this source-layout boundary
│   └── ksgs/
│       ├── README.md               # v0.2 package scaffold boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # one-line greenfield placeholder
│       ├── admit.py                # one-line greenfield placeholder
│       └── descriptor.yaml         # four-field unsafe placeholder
└── tests/
    └── README.md                   # documentation contract; executable tests unverified
```

The parent package metadata contains only:

```toml
[project]
name = "kfm-connector-ksgs"
version = "0.0.0"
```

| File | Confirmed bytes/posture | Does not prove |
|---|---|---|
| `README.md` | This source-layout document. | Runtime behavior or canonical placement. |
| `ksgs/README.md` | Repository-grounded package boundary merged before this revision. | Executable modules, activation, or deployment. |
| `ksgs/__init__.py` | Empty. | Stable import API or side-effect contract. |
| `ksgs/fetch.py` | One comment. | Network behavior, endpoint support, authentication, retries, pagination, caching, or source-head logic. |
| `ksgs/admit.py` | One comment. | Validation, admission, quarantine, receipt, or candidate-envelope behavior. |
| `ksgs/descriptor.yaml` | `name: ksgs`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Schema validity, registry authority, activation, rights clearance, sensitivity clearance, or public safety. |

This is a bounded inspected map, not a recursive tree receipt. Differently named or unindexed files remain possible until a complete inventory is generated.

---

## Inputs and outputs

### Current inputs

None. A source-layout directory has no callable contract, and the child package declares no supported function, class, command, endpoint, configuration, credential variable, or fixture shape.

### Current outputs

None. The child placeholder modules emit no payload, parsed record, validation report, candidate envelope, receipt, lifecycle write, or public artifact.

### Future permitted package inputs

Only after placement, contracts, review, and activation are accepted, the child package may consume:

- a conforming, reviewed, product-specific SourceDescriptor reference;
- an explicit activation state and approved access configuration;
- caller-supplied bytes, files, metadata, or approved transport results;
- source and product identity, source-head evidence, retrieval time, and run identity;
- rights, attribution, disclaimer, redistribution, sensitivity, and review context;
- synthetic or rights-cleared fixtures for offline validation.

### Future permitted package outputs

Future code may return in-memory, caller-owned parse results, finite failures, and RAW/QUARANTINE or receipt **candidates**. It must not select a lifecycle sink, persist directly to repository data roots, close evidence, or approve public release.

---

## Allowed contents

Subject to an accepted path and package decision, this `src/` layout may contain:

- one Python import package;
- package-local boundary documentation;
- narrow product-dispatch, parse, normalize, validation, and source-head helpers;
- an explicit opt-in source client with import-time and default-network denial;
- deterministic errors and stable reason codes;
- side-effect-free candidate-envelope builders;
- a compatibility shim only when a migration plan defines ownership, warnings, sunset criteria, tests, and rollback.

Every new executable module requires corresponding offline tests. A new sibling import package is a migration decision, not a convenience refactor.

---

## Exclusions

Do not place or authorize the following under this layout:

- canonical SourceDescriptor instances or activation decisions;
- contracts, schemas, registry authority, rights policy, sensitivity policy, evidence closure, or release authority;
- source payload archives, LAS files, maps, bulk tables, database extracts, or fixture corpora;
- credentials, tokens, cookies, session state, private endpoints, or account data;
- network calls triggered by import, installation, or default test execution;
- direct writes to RAW, QUARANTINE, receipts, processed, catalog, triplet, proof, release, or published roots;
- public APIs, maps, tiles, well locations, geology/hydrology claims, production summaries, or generated narratives;
- a second KGS package or silent `kgs`/`ksgs` alias;
- publisher-wide role, rights, sensitivity, or public-release defaults;
- operational engineering, drilling, water-supply, hazard, reserve, investment, legal, or safety conclusions.

Fixtures belong in an accepted fixture/test lane and require rights and sensitivity review. Exact wells, boreholes, samples, logs, private locations, and harmful joins must not be bundled as package data.

---

## Descriptor boundary

The package-local `ksgs/descriptor.yaml` is not a governed SourceDescriptor.

| Local field | Current value | Required disposition |
|---|---|---|
| `name` | `ksgs` | Do not convert into a stable source ID until the slug and product identity are accepted. |
| `role` | `TBD` | Reject as unresolved; source role is product-specific and must use an accepted vocabulary. |
| `rights` | `TBD` | Fail closed; no transport, admission, redistribution, or release authority. |
| `sensitivity_floor` | `public` | Ignore as authority; unresolved rights, product, geometry, and review state prohibit a permissive default. |

The populated singular-path SourceDescriptor schema requires a rich closed object and labels minimal legacy fields as migration aliases. The nominal plural-path schema is a permissive proposed scaffold with no properties. This schema-home conflict does not authorize the package to choose or create a third authority.

The source authority register is `PROPOSED` with no entries, and rights/sensitivity READMEs are greenfield stubs. Until the relevant authorities are accepted and populated:

- no local YAML field activates the connector;
- no KGS product receives a publisher-wide role;
- unknown rights or sensitivity routes to `DENY`, `ABSTAIN`, `HOLD`, or a QUARANTINE candidate;
- `public` in the placeholder never implies public-release safety.

---

## Runtime and admission boundary

The `src/` directory itself performs no runtime action. Any future child implementation must complete this sequence before source access:

1. Accept one connector path, distribution name, import name, and source-ID strategy.
2. Inventory and disposition losing KGS and product-specific paths.
3. Accept one SourceDescriptor contract, schema, registry, validator, and activation authority.
4. Approve product-specific identity, role, rights, attribution, disclaimer, sensitivity, cadence, source head, and access method.
5. Require explicit opt-in transport with bounded hosts, timeouts, retries, pagination, rate limits, credential handling, and audit behavior.
6. Preserve map, unit, well, lease/field, completion, log, curve/top, Geoportal resource, geometry, PLSS, scale, datum, depth, units, uncertainty, and vintage context as applicable.
7. Return a finite, side-effect-free outcome to caller-owned orchestration.
8. Leave lifecycle persistence, evidence closure, cataloging, release, correction, withdrawal, and public delivery to their owning systems.

| Condition | Required outcome |
|---|---|
| Path, package identity, descriptor, or activation unresolved | `DENY` or `ABSTAIN`; no network. |
| Product, role, rights, disclaimer, or sensitivity unresolved | `HOLD`, `DENY`, or QUARANTINE candidate. |
| Source shape, source head, or product identity drifted | QUARANTINE candidate or structured error; preserve bounded diagnostics. |
| PLSS derivation, geometry uncertainty, scale, datum, units, or depth context lost | Hard validation failure. |
| KGS observation collapsed into KCC regulatory truth | Hard source-role failure. |
| Aggregate, model, interpretation, or compilation presented as direct observation | Hard semantic failure. |
| Valid approved material | Caller-owned RAW candidate only. |
| Downstream persistence or public release requested | Refuse; outside this layout. |

There is intentionally no quickstart. A runnable example would invent an API and behavior not present in the repository.

---

## Validation

### Documentation checks for this revision

- preserve the document ID and creation date;
- record the pinned base and prior target blob;
- use one H1, logical heading order, balanced fences, and a final newline;
- make all repository-relative links resolve from `connectors/ksgs/src/`;
- remove remote badges and tracking images;
- contain no credentials, source payloads, private records, or exact sensitive locations;
- change only `connectors/ksgs/src/README.md`.

### Required future package checks

Before implementation maturity is claimed, tests must prove:

- clean build, install, and import for accepted Python versions;
- imports perform no network, filesystem write, registration, secret logging, or activation;
- the package-local descriptor is rejected as authority;
- missing or conflicted path, descriptor, activation, product, role, rights, disclaimer, and sensitivity state fail closed;
- product identity and KGS/KCC authority separation are preserved;
- geometry, PLSS derivation, uncertainty, scale, CRS/datum, depth, units, and vintage survive parsing;
- malformed inputs, schema drift, stale source heads, and unsupported products return finite outcomes;
- outputs remain caller-owned RAW, QUARANTINE, or receipt candidates;
- no direct lifecycle, evidence, release, correction, withdrawal, or public writes occur;
- live-source tests, if ever approved, are opt-in, isolated, credential-safe, terms-reviewed, rate-limited, and excluded from default CI;
- migration shims carry warnings, tests, owners, sunset criteria, and rollback coverage.

The exact conventional test probes `test_fetch.py`, `test_admit.py`, `conftest.py`, and `tests/fixtures/README.md` were absent at the pinned base. That bounded result does not rule out every differently named or unindexed test.

---

## Related surfaces

| Surface | Relationship | Status at the pinned base |
|---|---|---:|
| [Connector root](../../README.md) | Source-admission implementation and lifecycle boundary. | `CONFIRMED` |
| [Parent KSGS lane](../README.md) | Live compatibility connector scaffold. | `CONFIRMED path / stale canonicality claims` |
| [Child package](ksgs/README.md) | Package-level scaffold, product, descriptor, and runtime boundary. | `CONFIRMED v0.2` |
| [Project metadata](../pyproject.toml) | Distribution name and version. | `CONFIRMED 0.0.0 placeholder` |
| [Test boundary](../tests/README.md) | Intended offline compatibility tests. | `CONFIRMED README / executable tests unverified` |
| [Top-level KGS pointer](../../kgs/README.md) | Competing source-first compatibility path. | `CONFIRMED README` |
| [Geology KGS pointer](../../geology/kgs/README.md) | Newer documentation-only path-conflict analysis. | `CONFIRMED README-only pointer` |
| [Kansas family](../../kansas/README.md) | Kansas source-family coordination lane. | `CONFIRMED / child topology provisional` |
| `../../kansas/kgs/README.md` | Catalog-proposed KGS child. | `CONFIRMED exact path absent` |
| [KGS source catalog](../../../docs/sources/catalog/kansas/ksgs.md) | Human-facing product-family and slug/path proposal. | `CONFIRMED draft / not registry authority` |
| [SourceDescriptor contract](../../../contracts/source/source_descriptor.md) | Rich descriptor meaning and fail-closed rules. | `CONFIRMED draft / PROPOSED` |
| [Singular schema](../../../schemas/contracts/v1/source/source_descriptor.schema.json) | Populated rich machine shape that calls itself legacy. | `CONFIRMED / path conflict` |
| [Plural schema](../../../schemas/contracts/v1/sources/source_descriptor.schema.json) | Nominal canonical path with permissive empty scaffold. | `CONFIRMED PROPOSED scaffold` |
| [Source registry](../../../data/registry/sources/README.md) | Governed source-instance responsibility. | `CONFIRMED README / KGS entry unverified` |
| [Source authority register](../../../control_plane/source_authority_register.yaml) | Machine authority/activation register. | `CONFIRMED PROPOSED / entries empty` |
| [Rights policy](../../../policy/rights/README.md) and [sensitivity policy](../../../policy/sensitivity/README.md) | External fail-closed policy authority. | `CONFIRMED greenfield stubs` |

Product-specific compatibility paths such as `connectors/kgs_surficial/`, `connectors/kgs_bedrock/`, `connectors/kgs_oil_gas_wells/`, `connectors/kgs_kdhe_wwc5/`, and `connectors/kgs_las/` remain migration inputs, not authority granted to this layout.

---

## Evidence basis

Evidence is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at commit `d8d246bcd21b574c7691c396965b61d4548b30c3`.

| Evidence | Supports | Does not support |
|---|---|---|
| Target blob `45cb0900fc14bef569b69f972a4a8041c56f8cec` | Exact v0.1 baseline, stale two-README map, remote badges, and unresolved rollback placeholder. | Runtime or source readiness. |
| Direct reads of child package files | Empty initializer, comment-only code placeholders, and four-field local descriptor. | Executable behavior, recursive inventory, or safe configuration. |
| Parent `pyproject.toml` | Project name and version `0.0.0`. | Buildability, dependencies, supported runtime, or entry points. |
| Merged child package README | Package-level state, path conflict, descriptor conflict, product boundaries, and implementation gates. | Runtime behavior or accepted canonicality. |
| Parent, test, competing KGS, Kansas-family, and catalog READMEs | Current documentation topology and conflicts. | Accepted migration, activation, current upstream behavior, or rights clearance. |
| Populated singular and scaffold plural descriptor schemas | Schema-home and machine-shape conflict. | One accepted schema authority or KGS descriptor. |
| Authority register and policy stubs | Empty proposed source authority and missing executable rights/sensitivity policy. | Permission to implement local substitutes. |
| Exact absent-path probes and indexed searches | Named conventional tests and proposed Kansas child were absent at the pinned base. | Absence of every differently named or unindexed file. |
| Directory Rules, contribution guidance, and PR template inspected in this documentation pass | Responsibility boundaries, truth labels, reversible change, review, and rollback expectations. | Product approval or package maturity. |

Not inspected: live KGS services, current terms, credentials, source payloads, private locations, runtime logs, deployed configuration, emitted receipts, or public clients. Associated claims remain `UNKNOWN` or `NEEDS VERIFICATION`.

---

## Rollback

Rollback is required if this README is used to justify canonical placement, a second import package, live source access, local-descriptor authority, source activation, direct lifecycle writes, public KGS claims, rights/sensitivity bypass, or implementation maturity without code and tests.

Before merge, leave the draft PR unmerged and abandon the scoped branch. Closing the PR or deleting the branch requires separate authorization.

After merge, restore prior README blob `45cb0900fc14bef569b69f972a4a8041c56f8cec` from base `d8d246bcd21b574c7691c396965b61d4548b30c3` through a transparent revert commit or revert PR, then rerun documentation and connector-boundary validation. Do not reset, force-push, or rewrite shared history.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve canonical KGS connector, distribution, import, and source-ID paths. | `CONFLICTED` | Accepted ADR or migration record, backlink/import inventory, losing-path disposition, tests, and rollback. |
| Decide whether `ksgs` survives as a compatibility import. | `OPEN DECISION` | Explicit alias semantics, ownership, warnings, sunset criteria, and migration tests. |
| Reconcile parent and product-specific compatibility paths. | `CONFLICTED` | Migration manifest covering `kgs`, `ksgs`, domain-scoped, Kansas-family, and product paths. |
| Decide disposition of package-local `descriptor.yaml`. | `NEEDS VERIFICATION` | Registry, contract, schema, policy, package, and migration review. |
| Resolve SourceDescriptor schema, registry, validator, and activation authority. | `CONFLICTED` | Accepted contract/ADR, one enforceable schema, fixtures, validator, and registry workflow. |
| Create product-specific descriptors and activation decisions. | `BLOCKED` | Source identity, role, rights, sensitivity, access, cadence, source head, and steward review. |
| Confirm current KGS source surfaces and schemas. | `NEEDS VERIFICATION` | Current official documentation, source steward review, and approved fixtures. |
| Confirm rights, attribution, redistribution, disclaimers, and restrictions per product. | `NEEDS VERIFICATION / DEFAULT DENY` | Rights review, terms snapshot, and negative tests. |
| Confirm sensitive well, borehole, sample, log, and private-location handling. | `NEEDS VERIFICATION / DEFAULT DENY` | Sensitivity policy, transformations, negative fixtures, and release tests. |
| Confirm PLSS, geometry, CRS/datum, scale, depth, unit, and uncertainty handling. | `NEEDS VERIFICATION` | Product docs, contracts, fixtures, and validation tests. |
| Define build, import, dependency, configuration, and transport behavior. | `ABSENT` | Package implementation plus clean build/install/import evidence. |
| Define candidate envelopes, outcomes, reason codes, receipts, retries, replay, idempotency, and drift behavior. | `NEEDS VERIFICATION` | Accepted contracts, schemas, fixtures, and runtime tests. |
| Add safe offline fixtures and negative-first executable tests. | `ABSENT AT NAMED PROBES` | Fixture review, package tests, CI discovery, and logs. |
| Assign package and connector owners and required reviewers. | `UNKNOWN` | CODEOWNERS or accepted ownership record. |

---

## Maintainer note

Keep `src/` boring: one explicit package, no hidden side effects, no bundled source payloads, and no authority encoded by convenience. Until governance resolves the final KGS package home and descriptor controls, preserve this directory as a small, visible, inert scaffold.

When implementation begins, start with an offline proof-bearing slice: a synthetic or explicitly approved fixture, deterministic product identity, local-placeholder rejection, KGS/KCC anti-collapse, fail-closed rights and sensitivity behavior, geometry/uncertainty preservation, and a caller-owned quarantine candidate. Add reviewed source access only after that foundation passes.

<p align="right"><a href="#top">Back to top</a></p>
