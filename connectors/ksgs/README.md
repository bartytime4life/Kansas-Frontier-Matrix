<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksgs-readme
title: connectors/ksgs/ — KSGS Greenfield Connector Scaffold Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · KGS source steward · Geology steward · Hydrology steward · Hazards steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-root; greenfield-scaffold; noncanonical-path; path-and-slug-conflict; source-admission; no-network; fail-closed; no-activation; no-publication
current_path: connectors/ksgs/README.md
truth_posture: CONFIRMED repository-present 0.0.0 scaffold, exact placeholder package bytes, README-only named test lane, absent proposed Kansas child, empty source-authority register, unresolved registry templates, and TODO-only connector workflows / CONFLICTED final KGS connector, distribution, import, source-ID, schema, registry, fixture, and test placement / PROPOSED fail-closed parent boundary / UNKNOWN package runtime, source access, activation, rights clearance, sensitive-location transforms, substantive CI, deployment, and owners
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb
  prior_blob: f43b040bcc2b08cba0492cb6ef3bfeb7bbd392b9
  readme_introduction_commit: aef2b175d52d8429dfd295b9face39ae00b77a08
related:
  - ../README.md
  - ./pyproject.toml
  - ./src/README.md
  - ./src/ksgs/README.md
  - ./src/ksgs/descriptor.yaml
  - ./tests/README.md
  - ../kgs/README.md
  - ../geology/kgs/README.md
  - ../kansas/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/sources/catalog/kansas/ksgs.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../control_plane/source_authority_register.yaml
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../tests/README.md
  - ../../release/
tags: [kfm, connectors, ksgs, kgs, kansas, python, greenfield, compatibility, path-conflict, geology, hydrology, hazards, wells, oil-gas, wwc5, las, geoportal, source-admission, rights, sensitivity, no-network, raw, quarantine, governance]
notes:
  - "The current connector root contains this README, pyproject.toml declaring kfm-connector-ksgs version 0.0.0, one src/ksgs package scaffold, and a tests README."
  - "The import package is non-operational: __init__.py is empty; fetch.py and admit.py are comment-only placeholders; descriptor.yaml contains name: ksgs, role: TBD, rights: TBD, and sensitivity_floor: public."
  - "Exact probes at the pinned base returned Not Found for conventional connector-local test modules, a connector-local fixture README, and connectors/kansas/kgs/README.md."
  - "The machine source-authority register has entries: []; KSGS registry files are PROPOSED templates with unresolved fields; SourceDescriptor schema authority is conflicted; rights and sensitivity READMEs are greenfield stubs."
  - "The connector-gate and source-descriptor-validate workflows execute TODO echo steps; green completion does not prove package import, test discovery, descriptor validity, rights clearance, activation, or connector behavior."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry record, schema, contract, policy, fixture, test, workflow, receipt, source activation, path move, release object, or public artifact is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSGS Greenfield Connector Scaffold Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Component maturity:** repository-present `0.0.0` scaffold; no supported command, fetcher, parser, admission decision, lifecycle handoff, or public output  
> **Path posture:** `connectors/ksgs/` exists, but final KGS connector, distribution, import, source-ID, descriptor, registry, fixture, and test homes are `CONFLICTED`  
> **Authority:** connector-package documentation only; no source, schema, policy, lifecycle, evidence, release, or publication authority.

> [!WARNING]
> A directory, package name, catalog statement, local `descriptor.yaml`, proposed registry template, or green TODO-only workflow is not implementation evidence. KGS source access and activation remain denied until an accepted path decision, product-specific descriptors, reviews, safe fixtures, executable tests, substantive CI, and observed behavior exist.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#current-status) · [Placement](#placement-package-and-slug-conflict) · [Descriptor boundary](#descriptor-registry-and-policy-boundary) · [Product boundaries](#product-and-source-role-boundaries) · [Lifecycle](#lifecycle-and-publication-boundary) · [Validation](#validation) · [Evidence](#evidence-basis) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/ksgs/` is the repository-present parent for a non-operational Python scaffold using the `ksgs` distribution and import name.

Its present responsibility is to:

- record the exact scaffold that exists;
- keep placeholder code and metadata fail closed;
- preserve KGS product, source-role, rights, sensitivity, geometry, time, uncertainty, disclaimer, and provenance boundaries;
- expose the unresolved relationship among `KGS`, `kgs`, `ksgs`, competing connector paths, product compatibility paths, and source-registry templates;
- define what must be proved before implementation or activation;
- remain reversible while the repository chooses one accepted KGS connector and migration topology.

This directory does not prove that `ksgs` is the final package name, that the path is canonical, that a KGS source may be contacted, or that any source record is safe to publish.

Directory Rules place source-specific fetch and admission mechanics under `connectors/`. Source doctrine, authority records, contracts, schemas, policy, EvidenceBundle closure, lifecycle promotion, release, public APIs, maps, and AI answers remain in their owning roots.

[Back to top](#top)

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | `connectors/` owns source-specific fetch, probe, preservation, and admission mechanics. |
| Current parent path | **CONFIRMED** | README, package metadata, `src/`, and test documentation exist at the pinned base. |
| Distribution/import identity | **CONFIRMED scaffold / CONFLICTED final** | Metadata declares `kfm-connector-ksgs`; import folder is `ksgs`; publisher doctrine uses `KGS`; proposed paths use `kgs`. |
| Final connector path | **CONFLICTED** | Candidates include `connectors/ksgs/`, `connectors/kgs/`, `connectors/geology/kgs/`, proposed-but-absent `connectors/kansas/kgs/`, and product-specific top-level lanes. |
| Current implementation | **GREENFIELD PLACEHOLDER** | Empty initializer, comment-only fetch/admit modules, and minimal metadata establish no runtime behavior. |
| Local descriptor | **NONCONFORMING / DENY FOR AUTHORITY USE** | Four minimal or unresolved fields do not satisfy the richer SourceDescriptor contract. |
| Machine authority | **NOT ESTABLISHED** | Source-authority register is `PROPOSED` with `entries: []`; KSGS registry files are unresolved templates. |
| Executable tests | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | Test README exists; conventional modules and local fixture README were absent at the pinned base. |
| Connector CI | **TODO-ONLY** | Current connector and descriptor workflows execute `echo TODO ...`. |
| Source access and activation | **DENIED / NOT VERIFIED** | No approved product descriptor, source head, rights review, sensitivity review, or activation decision was verified. |
| Public output | **NONE** | This scaffold emits no map, API response, evidence object, proof, release, or publication artifact. |

Editing this README does not ratify the directory, package name, catalog slug, registry templates, product paths, or proposed Kansas child. A migration must preserve imports, source IDs, descriptors, fixtures, tests, receipts, provenance, backlinks, history, deprecation/correction state, and rollback.

[Back to top](#top)

---

## Current status

### Bounded repository snapshot

```text
connectors/ksgs/
├── README.md                           # this boundary
├── pyproject.toml                      # kfm-connector-ksgs, version 0.0.0
├── src/
│   ├── README.md                       # source-layout boundary
│   └── ksgs/
│       ├── README.md                   # package scaffold boundary
│       ├── __init__.py                 # empty
│       ├── fetch.py                    # comment-only placeholder
│       ├── admit.py                    # comment-only placeholder
│       └── descriptor.yaml             # four-field placeholder
└── tests/
    └── README.md                       # documentation contract
```

Package metadata:

```toml
[project]
name = "kfm-connector-ksgs"
version = "0.0.0"
```

Local descriptor:

```yaml
name: ksgs
role: TBD
rights: TBD
sensitivity_floor: public
```

Exact probes returned `Not Found` for:

```text
connectors/ksgs/tests/__init__.py
connectors/ksgs/tests/conftest.py
connectors/ksgs/tests/test_fetch.py
connectors/ksgs/tests/test_admit.py
connectors/ksgs/tests/test_descriptor.py
connectors/ksgs/tests/fixtures/README.md
connectors/kansas/kgs/README.md
```

These absence statements are bounded to the pinned commit and named paths. Differently named or unindexed files remain `UNKNOWN`.

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Metadata | `0.0.0` placeholder | Buildability, supported Python, dependencies, discovery, entry points, and runner are unknown. |
| `__init__.py` | Empty | No public import API or initialization behavior. |
| `fetch.py` / `admit.py` | Comment-only | No transport, parsing, validation, decision, receipt, or handoff behavior. |
| Descriptor | Unsafe placeholder | No conformance, role, rights, sensitivity, activation, or public-safety posture. |
| Tests | README-only at named probes | No import, fetch, admission, descriptor, fixture, replay, security, or lifecycle behavior is proved. |
| Policy | Rights and sensitivity README stubs | No executable KGS-specific decision is established. |
| Registry | Empty authority register plus unresolved templates | Migration evidence and negative inputs only. |
| Schemas | Populated singular path self-declared legacy; empty plural path | Final schema and validator authority remain conflicted. |
| Workflows | TODO-only | A green run cannot establish substantive coverage. |

[Back to top](#top)

---

## What belongs here

Only after an accepted path, package, and migration decision, this directory may contain:

- one distribution boundary and one import package;
- source-fetch, transport, parser, preservation, source-head, checksum, and candidate-envelope helpers;
- explicit opt-in clients whose import and default-test posture is no-network;
- deterministic finite outcomes and stable reason codes;
- product dispatch that preserves source-native identity, role, geometry, scale, datum, depth, units, uncertainty, vintage, rights, sensitivity, attribution, and disclaimers;
- caller-owned RAW, QUARANTINE, or receipt **candidate** builders that do not select lifecycle sinks;
- connector-local tests for retained package behavior;
- migration shims only when ownership, warnings, sunset criteria, tests, and rollback are accepted.

Every executable module requires offline tests and an observable CI command. A second package, silent `kgs`/`ksgs` alias, product root, or local authority record is a migration decision—not a convenience refactor.

## What does not belong here

This directory must not contain or imply authority over:

- source-catalog doctrine, SourceDescriptor authority, activation decisions, contracts, schemas, policy, or release review;
- bulk KGS downloads, LAS archives, database extracts, map caches, production payload corpora, or unreviewed upstream samples;
- credentials, cookies, authorization headers, account details, signed URLs, private endpoints, or secrets;
- real exact private wells, boreholes, samples, proprietary logs, owner/parcel joins, sensitive subsurface sites, or harmful location joins in fixtures, logs, snapshots, or examples;
- network access on import, installation, default tests, or documentation rendering;
- direct writes to lifecycle, catalog, triplet, proof, release, or published roots;
- EvidenceBundle closure, proof generation, promotion, correction, withdrawal, supersession, rollback, or public release;
- public APIs, map layers, drilling or engineering advice, water-supply conclusions, reserve estimates, operational hazard guidance, or AI narratives presented as KGS truth.

Public availability upstream is not equivalent to KFM rights clearance, sensitivity clearance, evidence closure, or release approval.

[Back to top](#top)

---

## Inputs and outputs

### Current

The package declares no supported function, class, command, endpoint, configuration contract, credential variable, descriptor contract, fixture shape, or runner. It emits no response bytes, parsed record, validation result, decision, candidate, receipt, lifecycle write, map artifact, API payload, or public claim.

### Future admissible inputs

After placement and activation gates are accepted, a retained package may consume:

- a conforming, reviewed, product-specific SourceDescriptor reference;
- an explicit activation decision and approved access configuration;
- caller-supplied bytes, files, metadata, or reviewed transport result;
- source/product/record identity, source-head evidence, retrieval time, run identity, and destination intent;
- rights, attribution, disclaimer, redistribution, sensitivity, geometry, scale, datum, depth, units, uncertainty, and review context;
- synthetic or explicitly rights-cleared fixtures.

### Future allowed outputs

A retained package may return in-memory, caller-owned parsed records, validation findings, and explicit `admit-candidate`, `hold/quarantine-candidate`, `deny`, `abstain`, `no-op`, `rate-limit`, or `error` outcomes. Orchestration chooses persistence. The package must not select a lifecycle sink, mint authoritative receipts, close evidence, approve release, or publish.

[Back to top](#top)

---

## Placement, package, and slug conflict

| Surface | Current evidence | Safe posture |
|---|---|---|
| `connectors/ksgs/` | Live package-shaped `0.0.0` scaffold. | **Present / final status CONFLICTED.** Shape does not establish canonicality. |
| `connectors/kgs/` | README-only compatibility lane with older path certainty. | **Present / stale certainty.** Migration evidence, not authority. |
| `connectors/geology/kgs/` | Newer README-only pointer rejecting domain-scoped implementation. | **Present / not an implementation home.** |
| `connectors/kansas/` | Kansas source-family coordination lane. | **Family placement present / child topology provisional.** |
| `connectors/kansas/kgs/` | Proposed by catalog; exact README probe returned `404`. | **PROPOSED / NOT PRESENT.** |
| Product-specific `connectors/kgs_*` lanes | README-only compatibility surfaces for maps, wells/production, WWC5, and LAS. | **Migration scope, not activation or canonicality.** |
| `docs/sources/catalog/kansas/ksgs.md` | Draft human-facing publisher entry preserving `ksgs.md`, proposing `kgs/`, and tracking OPEN-KSGS-13. | **Doctrine input, not machine authority or path-presence proof.** |

A final decision must cover `KGS`/`kgs`/`ksgs` naming, parent path, losing-path disposition, distribution/import name, source-ID namespace, product dispatch, joint-program identity, registry/schema migration, tests/fixtures, credentials, receipt ownership, compatibility warnings, history, deprecation, correction, and rollback.

Until an accepted ADR or migration closes that scope, implementation remains frozen at the documentation-only scaffold.

[Back to top](#top)

---

## Descriptor, registry, and policy boundary

The local descriptor is not a governed SourceDescriptor:

| Field | Value | Required posture |
|---|---|---|
| `name` | `ksgs` | Do not convert into a stable source ID until identity is accepted. |
| `role` | `TBD` | Reject. Role is product-specific, not publisher-wide. |
| `rights` | `TBD` | Reject for activation and public use. |
| `sensitivity_floor` | `public` | Never treat as clearance while rights, product, geometry, policy, and review remain unresolved. |

Other machine-shaped surfaces remain non-authoritative:

- `control_plane/source_authority_register.yaml` is `PROPOSED` with `entries: []`;
- KSGS bedrock, oil-and-gas, natural-resources, and seismic registry files are `PROPOSED` templates with unresolved fields;
- the populated singular SourceDescriptor schema is `PROPOSED` and self-identifies as legacy;
- the plural SourceDescriptor schema is an empty permissive `PROPOSED` scaffold;
- ADR-0001 remains `proposed`;
- rights and sensitivity READMEs are greenfield stubs;
- connector workflows execute TODO echo steps.

The richer SourceDescriptor contract requires identity, version, source type and role, authority rank, publisher, steward, rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, public-release posture, review state, release state, and lifecycle state.

Therefore no placeholder, unresolved template, empty-schema pass, catalog statement, or TODO workflow may activate a source or establish public safety.

[Back to top](#top)

---

## Product and source-role boundaries

KGS is a publisher family, not one interchangeable payload.

| Product family | Preserve | Deny or abstain from |
|---|---|---|
| Bedrock and surficial maps | Map/unit ID, compilation method, scale, vintage, CRS/datum, geometry, uncertainty, source URI, disclaimer. | Compilation as direct observation, current site condition, engineering advice, or scale-free truth. |
| Oil-and-gas wells | Well/API ID, location source, uncertainty, record type, status vintage, role, correction state. | KGS record as KCC permit/compliance finding, current operations, reserve, forecast, or drilling decision. |
| Oil-and-gas production | Lease/field/reporting period, aggregation unit, revision state, role. | Aggregate assigned to a well/place without support or treated as reserve estimate. |
| WWC5 | Joint-program and completion identity, construction fields, coordinate derivation, precision, disclaimer, vintage. | Current water quality, aquifer condition, safe supply, water right, or exact public private-well location by default. |
| LAS logs and tops | Well/log/curve/top identity, units, depth reference, datum, interpretation lineage, source version, rights. | Interpretation as raw measurement, canonical geology, or engineering advice. |
| Geoportal resources | Resource-specific distribution, schema, role, rights, cadence, geometry, source head, vintage. | Mixed content admitted under one publisher-wide role or generic descriptor. |
| Natural resources | Occurrence/deposit/estimate/extraction/administrative class, evidence, geometry, uncertainty, vintage. | Occurrence as reserve, estimate as observation, extraction as geology truth, or exact sensitive site exposure. |
| Seismic context | Product identity, event/background distinction, role, time, uncertainty, official-source links. | Public alert authority, emergency instruction, deterministic cause, or real-time completeness guarantee. |

KGS material is not a KCC regulatory determination, a KDHE environmental decision, a KDA-DWR water-right decision, a USGS observation, or an official alert. Maps, tiles, search results, graph edges, dashboards, workflows, AI answers, and generated summaries cannot upgrade source role.

Exact/private wells, boreholes, samples, logs, owner/parcel joins, resource sites, and harmful combined geometries fail closed. PLSS-derived coordinates retain derivation and uncertainty. Upstream disclaimers remain governance metadata.

[Back to top](#top)

---

## Lifecycle and publication boundary

Current lifecycle behavior is **none**. Future package code may return caller-owned candidates only.

```text
accepted product SourceDescriptor + activation + access + policy context
  -> opt-in fetch or caller-supplied bytes
  -> preserve product identity and source meaning
  -> parse / validate / finite outcome
  -> return caller-owned candidate
  -> orchestration persists RAW, QUARANTINE, or receipt state
  -> downstream pipelines own WORK, PROCESSED, CATALOG/TRIPLET
  -> evidence, policy, review, proof, and release gates
  -> PUBLISHED public-safe artifact
```

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move, package return value, successful request, Git commit, merged PR, workflow completion, map render, or AI explanation.

[Back to top](#top)

---

## Validation

No package build, install, import test, fetch test, parser test, admission test, descriptor validation, fixture run, source probe, or package-specific CI command was verified.

Required future coverage includes:

1. import and collection cause no network, DNS, credential, filesystem, cache, registry, lifecycle, or publication side effect;
2. `0.0.0`, comment-only modules, the local descriptor, and unresolved templates cannot be reported as working or active;
3. path and identity tests do not choose `KGS`/`kgs`/`ksgs` or a competing path without migration evidence;
4. metadata declares supported Python, build backend, dependencies, discovery, entry points, extras, and runner;
5. missing, malformed, conflicted, `TBD`, unreviewed, or unactivated descriptors deny or hold access;
6. default transport tests are no-network; live integration is explicit, isolated, reviewed, rate-limited, and incapable of publication;
7. product identity and source-role anti-collapse are preserved across maps, wells, production, WWC5, LAS, Geoportal, natural resources, and seismic context;
8. rights, attribution, disclaimers, sensitivity, geometry, scale, depth, units, uncertainty, time, source head, correction, and supersession remain explicit;
9. finite outcomes and reason codes are deterministic;
10. package helpers cannot write lifecycle, catalog, evidence, proof, release, or publication state;
11. fixtures are compact, synthetic or rights-cleared, public-safe, source-labeled, and expected-outcome-labeled;
12. secrets, private endpoints, restricted payloads, and sensitive coordinates never appear in logs, errors, snapshots, or committed fixtures;
13. maps, tiles, graphs, indexes, workflows, and AI answers cannot become source truth or release approval;
14. CI runs the accepted command, reports discovered tests, and fails on zero discovery, TODO-only execution, or missing negative coverage.

```text
import retained package
  -> no network or DNS
  -> no credential lookup
  -> no filesystem, cache, registry, or lifecycle write
  -> no activation
  -> no receipt, proof, catalog, release, or public artifact
```

| Condition | Required outcome |
|---|---|
| Local descriptor accepted as authority | **FAIL / DENY** |
| Template has `TBD` or unresolved rights/sensitivity | **HOLD / DENY** |
| Empty plural schema treated as conformance | **FAIL** |
| Descriptor, authority entry, review, or activation missing | **DENY** |
| Path or slug treated as canonical without migration evidence | **FAIL** |
| Product identity or record class missing | **HOLD / QUARANTINE** |
| KGS role upgraded to regulatory or another publisher | **FAIL / DENY** |
| Unknown rights, attribution, redistribution, or disclaimer | **HOLD / DENY PUBLIC USE** |
| Exact sensitive/private location enters default fixture, log, or public candidate | **FAIL / REMOVE / REVIEW INCIDENT** |
| PLSS-derived coordinate lacks derivation and uncertainty | **HOLD / QUARANTINE** |
| Default test or import contacts a live source | **FAIL** |
| Package writes beyond a caller-owned candidate | **FAIL** |
| Workflow only echoes TODO or discovers zero tests | **FAIL AS COVERAGE CLAIM** |
| Connector result treated as publication or evidence closure | **FAIL / DENY** |

[Back to top](#top)

---

## Review burden

README-only clarification needs connector/package or docs review plus validation/test review. Executable code additionally needs package, source, rights, privacy/sensitivity, security, and affected domain review. Source IDs, roles, descriptors, registry, and activation need source-registry, contract/schema, policy, and KGS source review. Live integration or credentials need security and CI review. Path/package/import migration needs architecture, package, test, docs, registry, and ADR/migration review. Release-affecting behavior requires independent release authority.

Named teams and package-specific owners remain `UNKNOWN`; do not invent them.

---

## Related folders

| Surface | Current relationship |
|---|---|
| [`../README.md`](../README.md) | Connector-root authority and RAW/QUARANTINE/receipt boundary. |
| [`./src/README.md`](./src/README.md) | Confirms one `0.0.0` source layout and no runtime behavior. |
| [`./src/ksgs/README.md`](./src/ksgs/README.md) | Package-state and product anti-collapse boundary. |
| [`./src/ksgs/descriptor.yaml`](./src/ksgs/descriptor.yaml) | Negative input only; not authority. |
| [`./tests/README.md`](./tests/README.md) | Future connector-local test contract; named tests absent. |
| [`../kgs/README.md`](../kgs/README.md) | Competing compatibility lane with stale path certainty. |
| [`../geology/kgs/README.md`](../geology/kgs/README.md) | Rejects domain-scoped implementation and records placement conflict. |
| [`../kansas/README.md`](../kansas/README.md) | Kansas family path exists; KGS child remains absent/provisional. |
| [`../../docs/sources/catalog/kansas/ksgs.md`](../../docs/sources/catalog/kansas/ksgs.md) | Human-facing product doctrine; not machine authority. |
| [`../../contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) | Rich SourceDescriptor meaning; proposed status. |
| [`../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) | Rich, populated, self-declared legacy schema path. |
| [`../../schemas/contracts/v1/sources/source_descriptor.schema.json`](../../schemas/contracts/v1/sources/source_descriptor.schema.json) | Empty permissive proposed scaffold. |
| [`../../control_plane/source_authority_register.yaml`](../../control_plane/source_authority_register.yaml) | Proposed, empty source-authority map. |
| [`../../policy/rights/`](../../policy/rights/README.md), [`../../policy/sensitivity/`](../../policy/sensitivity/README.md) | Greenfield policy stubs. |
| [`../../tests/`](../../tests/README.md) | Canonical repository-wide enforceability root. |
| [`../../release/`](../../release/) | Release, correction, withdrawal, supersession, and rollback authority. |

The proposed `connectors/kansas/kgs/` child is intentionally not linked as a live directory.

---

## ADRs

Directory Rules assign source mechanics to `connectors/`, object meaning to `contracts/`, shape to `schemas/`, admissibility to `policy/`, and enforceability to `tests/`. Connectors do not publish or write downstream lifecycle state. Existing paths do not become canonical by presence, and parallel authority is forbidden without an accepted ADR or migration note.

[`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) exists with status `proposed`; it does not resolve the singular/plural SourceDescriptor content conflict. No accepted ADR or migration was verified for final KGS connector, distribution, import, source-ID, product dispatch, descriptor migration, test home, or losing-path disposition. OPEN-KSGS-13 is an open naming item, not an accepted decision.

This one-file documentation edit creates no path or authority boundary and does not itself require a new ADR.

---

## Last reviewed

- **Documentation review:** `2026-07-13`
- **Evidence base:** `main` at `0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb`
- **Prior README blob:** `f43b040bcc2b08cba0492cb6ef3bfeb7bbd392b9`
- **README introduction commit:** `aef2b175d52d8429dfd295b9face39ae00b77a08`

This is not a source-rights review, security approval, activation, runtime proof, release decision, or publication date.

---

## Evidence basis

| Evidence | Supports | Does not prove |
|---|---|---|
| Prior README blob | Exact v0.1 baseline, stale canonical certainty, remote badges, and rollback placeholder. | Runtime or canonical placement. |
| Package metadata and exact module bytes | `0.0.0`, empty initializer, comment-only fetch/admit. | Build, fetch, parse, decision, or handoff behavior. |
| Local descriptor | Minimal unresolved values. | Conformance, role, rights, sensitivity, activation, or release. |
| Current source/package/test READMEs and exact probes | Scaffold state, named absent tests, and path conflict. | Exhaustive recursive absence or executable behavior. |
| KGS catalog and compatibility READMEs | Product distinctions, proposed path, rights/sensitivity posture, and migration scope. | Machine authority, path presence, current terms, or activation. |
| SourceDescriptor contract, schemas, ADR, register, and templates | Rich required surface plus current schema/registry conflict. | Accepted validator authority or valid product descriptors. |
| Policy and workflow files | Greenfield policy stubs and TODO-only jobs. | Executable policy or substantive CI. |
| Directory Rules and connector-root README | Responsibility roots, lifecycle boundary, and reversible migration discipline. | Final KGS path or source runtime. |

Claims are bounded to the pinned commit, exact reads, and named probes.

---

## Definition of done

### This documentation update

- [x] Records current path, base commit, prior blob, and introduction commit.
- [x] Describes exact package, descriptor, and test scaffold without runtime overclaiming.
- [x] Records the absent proposed Kansas child and named absent tests.
- [x] Removes stale canonical-path certainty, remote badges, and rollback placeholder.
- [x] Keeps connector/package/slug/schema/registry/fixture/test conflicts visible.
- [x] Treats placeholders, empty authority register, unresolved templates, empty schema, and TODO workflows as fail-closed evidence.
- [x] Preserves product, source-role, rights, sensitivity, geometry, time, correction, carrier, lifecycle, and publication boundaries.
- [x] Changes only this Markdown file.

### Implementation readiness remains open

- [ ] Accepted path/package/source-ID/schema/registry/fixture/test migration.
- [ ] Product descriptors, authority entries, reviews, source heads, and activation decisions.
- [ ] Current endpoints, access, terms, attribution, redistribution, cadence, rate limits, disclaimers, corrections, and withdrawals.
- [ ] Build metadata, executable code, safe fixtures, negative tests, substantive CI, owners, and rollback-tested migration.

Documentation readiness does not imply package readiness, source access, activation, evidence closure, rights approval, sensitivity clearance, release approval, or publication.

---

## Rollback

Rollback is required if this README is used to claim canonical status, implementation/test/CI behavior, source access, activation, rights/sensitivity clearance, public safety, downstream lifecycle authority, evidence closure, or release.

Before merge, leave the branch unmerged. After merge, restore prior blob:

```text
f43b040bcc2b08cba0492cb6ef3bfeb7bbd392b9
```

from base:

```text
0e0b6bfdc3e1cb6711acd9f495c72b906a2845fb
```

through a transparent revert commit or revert PR, then rerun applicable documentation and connector-boundary checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Complete recursive inventory | **UNKNOWN** | Git tree receipt or mounted checkout. |
| Final connector/distribution/import/source-ID/schema/registry/fixture/test paths | **CONFLICTED** | Accepted ADR/migration, consumer inventory, tests, and rollback plan. |
| `KGS`/`kgs`/`ksgs` identity | **CONFLICTED** | Stable naming and compatibility map. |
| Scaffold survives, migrates, redirects, or retires | **NEEDS VERIFICATION** | Path decision and migration sequence. |
| SourceDescriptor schema/validator authority | **CONFLICTED** | One meaningful accepted schema, validator, fixtures, and migration. |
| Local descriptor and KSGS templates | **NEEDS VERIFICATION** | Migrate, validate, or retire through source-registry review. |
| Product endpoints, terms, cadence, source heads, and corrections | **NEEDS VERIFICATION** | Current authoritative source documentation and steward review. |
| Package APIs, DTOs, finite outcomes, reason codes, and side effects | **NEEDS VERIFICATION** | Accepted contracts, implementation, and tests. |
| Fixture homes and rights | **UNKNOWN** | Fixture inventory, generation notes, reviews, and expected outcomes. |
| Executable negative-first tests and substantive CI | **NOT IMPLEMENTED AT NAMED PATHS** | Test modules, exact command, discovery count, logs, and failure demonstration. |
| Joint-program identity and cross-domain routing | **NEEDS VERIFICATION** | KGS/KDHE/KDA-DWR, Geology, Hydrology, Hazards, and policy decision. |
| Cross-publisher anti-collapse and sensitive-location handling | **NEEDS VERIFICATION** | Contracts, policies, transforms, fixtures, tests, and review records. |
| Owners and PR promotion prerequisites | **UNKNOWN / NEEDS VERIFICATION** | CODEOWNERS/ownership records and workflow evidence. |

[Back to top](#top)

---

## Maintainer note

Keep this scaffold non-operational until path and identity conflicts are resolved and one offline proof-bearing slice exists.

The safest first executable increment is synthetic and negative-first: import without side effects; reject the local descriptor and one unresolved registry template; preserve product identity, role, geometry, uncertainty, time, rights, sensitivity, attribution, and disclaimer fields; return a caller-owned hold/quarantine candidate with deterministic reasons; prove no lifecycle, evidence, catalog, proof, release, or publication write; and fail CI on zero discovery or negative-case regression.

Only after that slice, accepted placement, product-specific governance, and observed CI should an opt-in source-access test be considered.

[Back to top](#top)
