<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ksgs-tests-readme
title: connectors/ksgs/tests/ — KSGS Greenfield Connector Test Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Test steward · KGS source steward · Geology steward · Hydrology steward · Hazards steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-local-tests; greenfield-scaffold; noncanonical-path; path-and-slug-conflict; no-network; synthetic-fixtures; fail-closed; no-activation; no-publication
current_path: connectors/ksgs/tests/README.md
truth_posture: CONFIRMED README-only inspected test lane, named conventional test paths absent, 0.0.0 package scaffold, placeholder descriptors, and TODO-only connector workflows / CONFLICTED KGS connector path, kgs-versus-ksgs identity, SourceDescriptor schema authority, registry migration, and final test routing / PROPOSED fail-closed connector-local test contract / UNKNOWN differently named tests, package runtime, source access, activation, rights clearance, sensitive-location handling, and substantive CI coverage
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d462f52e9a3b16ea19ad8512895505f0b15d1e27
  prior_blob: 5e4c87a12e91a87b4148691840a41f1bd3513201
  readme_introduction_commit: 1ffda65bd58cae71a60443e87da2e792de68f29f
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/ksgs/README.md
  - ../src/ksgs/descriptor.yaml
  - ../../kgs/README.md
  - ../../geology/kgs/README.md
  - ../../kansas/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../docs/sources/catalog/kansas/ksgs.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/geology/sources/ksgs_bedrock.yaml
  - ../../../data/registry/geology/sources/ksgs_oil_and_gas.yaml
  - ../../../data/registry/geology/sources/ksgs_natural_resources.yaml
  - ../../../data/registry/hazards/sources/ksgs_seismic.yaml
  - ../../../tests/README.md
  - ../../../tests/domains/geology/README.md
  - ../../../fixtures/README.md
  - ../../../fixtures/domains/geology/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../release/
tags: [kfm, connectors, ksgs, kgs, tests, greenfield, compatibility, path-conflict, geology, hydrology, hazards, source-admission, source-role, rights, sensitivity, wells, no-network, fixtures, fail-closed, raw, quarantine, governance]
notes:
  - "The inspected connector-local test directory contains this README; indexed search and exact probes did not find test_fetch.py, test_admit.py, test_descriptor.py, conftest.py, __init__.py, or tests/fixtures/README.md."
  - "Absence claims are bounded to the pinned base, indexed search, and exact named probes. Differently named or unindexed files remain UNKNOWN."
  - "The parent package is a 0.0.0 greenfield scaffold: __init__.py is empty, fetch.py and admit.py are comment-only placeholders, and descriptor.yaml is a four-field nonconforming placeholder."
  - "The local descriptor and domain registry templates contain unresolved or TBD fields and must be negative test inputs, not source authority or activation evidence."
  - "The connector-gate and source-descriptor-validate workflows currently execute TODO echo steps; a green workflow run does not establish KSGS test coverage."
  - "Only this Markdown file is in scope. No test, fixture, code, package metadata, schema, contract, policy, descriptor, registry entry, workflow, receipt, source activation, path move, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KSGS Greenfield Connector Test Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Current test maturity:** README-only inspected lane; executable tests not found at the named conventional paths  
> **Package maturity:** `0.0.0` greenfield scaffold; fetch and admission behavior not implemented  
> **Path posture:** current `connectors/ksgs/` path exists, but the final KGS connector, distribution, import, source-ID, and test homes are `CONFLICTED`  
> **Boundary:** this folder may eventually hold narrow connector-package tests. It does not activate KGS, prove source access, establish descriptor authority, validate a real KGS record, approve exact well locations, or authorize release.

> [!WARNING]
> A README, passing repository-wide workflow, local `descriptor.yaml`, domain registry template, source-catalog statement, or directory name is not test coverage. Until executable tests, safe fixtures, an accepted runner, and observed results exist, package behavior remains `UNKNOWN` and source activation remains denied.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence](#evidence-basis) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/ksgs/tests/` is the repository-present test-documentation lane beside the non-operational `connectors/ksgs/src/ksgs/` Python package scaffold.

Its narrow purpose is to define what **connector-local** tests must prove if this package is retained or migrated:

- importing or inspecting the package causes no network, credential, filesystem, lifecycle, or publication side effect;
- placeholder descriptors and unresolved registry templates fail closed;
- source-product identity, role, rights, sensitivity, geometry, time, uncertainty, and disclaimer fields are preserved rather than upgraded;
- package helpers return bounded candidate outcomes to caller-owned orchestration rather than writing lifecycle or release state;
- compatibility behavior does not silently settle the `kgs` versus `ksgs` path and identity conflict.

This folder is not the canonical home for all KGS, Geology, Hydrology, Hazards, policy, release, or source-admission tests. Cross-system enforceability belongs under the canonical `tests/` responsibility root and its domain/source/policy lanes.

[Back to top](#top)

---

## Authority level

**Connector-local test lane inside a noncanonical greenfield scaffold. It has no source, schema, policy, lifecycle, evidence, release, or publication authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility | **CONFIRMED** | Test code proves behavior; source-fetch and admission implementation belongs under `connectors/`, while canonical cross-system enforceability belongs under root `tests/`. |
| Current path | **CONFIRMED** | `connectors/ksgs/tests/README.md` exists at the pinned base. |
| Current executable tests | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | Indexed search and direct reads found the README but not the conventional modules listed in the current snapshot. |
| Current package behavior | **GREENFIELD PLACEHOLDER** | Empty initializer, comment-only fetch/admit modules, and minimal package metadata establish no runnable behavior. |
| KGS connector path | **CONFLICTED** | Current and documented candidates include `connectors/ksgs/`, `connectors/kgs/`, `connectors/geology/kgs/`, proposed-but-absent `connectors/kansas/kgs/`, and product-specific top-level KGS lanes. |
| Package/import identity | **CONFLICTED** | Distribution and import scaffold use `ksgs`; publisher abbreviation and several proposed connector paths use `kgs`. No accepted migration was verified. |
| Descriptor/schema authority | **CONFLICTED / NOT ESTABLISHED FOR KGS** | The local descriptor is nonconforming; legacy registry templates remain `TBD`; the populated singular schema calls itself legacy; the plural schema is an empty scaffold; the machine authority register has no entries. |
| Source activation | **DENIED / NOT VERIFIED** | No conforming product descriptor, authority entry, rights/sensitivity review, source head, activation decision, or executable gate was verified. |
| Public release | **NONE** | Connector-local tests cannot approve a public layer, API response, map, well record, geology claim, hazard claim, receipt, proof, or release. |

Editing this existing README does not ratify the path. Any move, rename, consolidation, compatibility import, or new canonical KGS test home requires the applicable ADR or migration discipline.

[Back to top](#top)

---

## Status

### Current bounded repository snapshot

The following map is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `d462f52e9a3b16ea19ad8512895505f0b15d1e27`, indexed search, and exact path reads:

```text
connectors/ksgs/
├── README.md
├── pyproject.toml                  # project kfm-connector-ksgs, version 0.0.0
├── src/
│   ├── README.md
│   └── ksgs/
│       ├── README.md
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field nonconforming placeholder
└── tests/
    └── README.md                   # this documentation contract
```

Exact probes returned `Not Found` for:

```text
connectors/ksgs/tests/__init__.py
connectors/ksgs/tests/conftest.py
connectors/ksgs/tests/test_fetch.py
connectors/ksgs/tests/test_admit.py
connectors/ksgs/tests/test_descriptor.py
connectors/ksgs/tests/fixtures/README.md
```

This does not prove that every differently named or unindexed file is absent. It does establish that the prior generic “test inventory needs verification” wording can be narrowed: no executable test was found in the indexed lane or at these conventional paths.

### Current maturity table

| Item | Current state | Safe conclusion |
|---|---|---|
| This README | **DRAFT v0.2** | Reviewable boundary documentation only. |
| Test runner | **NOT DECLARED** | `pyproject.toml` contains no build backend, dependency, test framework, command, or package-discovery configuration. |
| Import tests | **NOT FOUND** | No import-safety behavior is proven. |
| Fetch tests | **NOT FOUND** | No transport, endpoint, retry, timeout, rate-limit, pagination, caching, source-head, or no-network behavior is proven. |
| Admission tests | **NOT FOUND** | No descriptor gate, finite outcome, quarantine, receipt, or candidate-handoff behavior is proven. |
| Descriptor tests | **NOT FOUND** | The local descriptor and legacy registry templates remain unsafe/unvalidated as activation inputs. |
| Fixtures | **NO CONNECTOR-LOCAL FIXTURE README FOUND** | No local fixture rights, sensitivity, provenance, generation, or expected-outcome record was verified. |
| Connector workflows | **TODO-ONLY STUBS** | `connector-gate` and `source-descriptor-validate` currently run `echo TODO ...`; success proves workflow execution only. |
| Package runtime | **ABSENT / UNKNOWN** | No supported command, callable API, source client, parser, output DTO, sink, or runtime log was verified. |
| Source activation and public use | **DENIED BY DEFAULT** | Repository presence does not authorize access, admission, evidence use, or release. |

[Back to top](#top)

---

## What belongs here

Only after the KGS path and test-routing decision is accepted, this connector-local lane may contain small tests for behavior owned by the retained package, such as:

- import and module smoke tests with no network or side effects;
- deterministic tests for package-local pure parsing, source-head, checksum, identity-preservation, and candidate-envelope helpers;
- tests that reject the package-local placeholder descriptor as authority;
- tests that require a caller-supplied, conforming, reviewed, product-specific descriptor reference and activation state;
- no-network transport tests using explicit fakes or approved synthetic responses;
- tests that preserve source-native product, record, geometry, scale, datum, depth, unit, time, uncertainty, rights, sensitivity, attribution, and disclaimer fields;
- tests that return explicit admit-candidate, hold/quarantine-candidate, deny, abstain, no-op, rate-limit, or error outcomes without creating lifecycle state;
- import/path compatibility tests only when an accepted migration retains `ksgs` as a compatibility namespace;
- small test-only expected outputs that are clearly synthetic and do not become registry, receipt, proof, or release authority.

Executable tests must be paired with an accepted runner, documented fixture home, observable CI command, and negative coverage before implementation maturity is claimed.

[Back to top](#top)

---

## What does not belong here

This folder must not contain or become:

- live KGS source payloads, bulk downloads, private exports, or unreviewed upstream samples;
- real exact wells, boreholes, samples, logs, production sites, private-land locations, or other sensitive coordinates;
- credentials, cookies, access tokens, account details, private endpoints, or secrets in source, fixtures, logs, snapshots, or exceptions;
- production connector code, package metadata, runtime configuration, caches, or downloaded source files;
- authoritative `SourceDescriptor` instances, source-authority entries, activation decisions, rights decisions, sensitivity decisions, or policy bundles;
- a second schema, contract, policy, source registry, fixture authority, receipt, proof, catalog, release, or publication home;
- direct writes to `data/raw/`, `data/quarantine/`, `data/receipts/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, or `release/`;
- tests that contact live sources by default or require internet access to pass;
- tests that convert a successful fetch, parse, validation, Git commit, workflow, map, tile, graph edge, AI summary, or README statement into source truth or release approval;
- cross-domain tests that silently make this local lane the owner of Geology, Hydrology, Hazards, KCC regulatory, KDHE environmental, land/privacy, or release semantics;
- evidence of canonical placement merely because the current package, source-catalog slug, or directory exists.

[Back to top](#top)

---

## Inputs

### Current inputs

None. The package exposes no supported function, command, configuration contract, endpoint contract, fixture contract, or test runner.

### Future admissible test inputs

After placement and implementation gates are accepted, tests may consume:

- explicit synthetic or rights-cleared, public-safe fixture material;
- a conforming valid descriptor fixture and deliberately invalid descriptor fixtures;
- an explicit activation-state fixture;
- accepted semantic contracts, schemas, and policy expectations from their owning roots;
- caller-supplied bytes or response doubles—never implicit live-source access;
- deterministic run identity, retrieval time, source-head, checksum, and destination intent fixtures;
- product-specific fixtures that make publisher, product, record type, source role, geometry provenance, uncertainty, rights, sensitivity, and expected outcome explicit;
- correction, withdrawal, supersession, and stale-state fixtures where the source product supports them.

A real upstream payload is not automatically a safe test input. It requires rights, sensitivity, provenance, minimization, and repository-storage review.

[Back to top](#top)

---

## Outputs

### Current outputs

None. The current lane emits no test result because no runner or executable test was verified.

### Future allowed outputs

A future test run may emit ordinary ephemeral test results and clearly non-authoritative expected-output comparisons. When the repository adopts a governed test-report or CI-artifact contract, the runner may emit that contract through the accepted artifact path.

Tests must never emit or mutate:

- actual RAW or QUARANTINE records;
- source-authority or activation records;
- actual receipts or proofs;
- catalog or triplet records;
- release, correction, withdrawal, supersession, or rollback decisions;
- public API, map, tile, export, or AI artifacts.

A synthetic expected receipt or release object remains a fixture. It is not process memory, proof, or release state.

[Back to top](#top)

---

## Validation

### Test ownership and routing

KGS behavior crosses several responsibility boundaries. Keep tests with the owner of the rule they prove.

| Test concern | Correct or current responsibility lane | Local-lane boundary |
|---|---|---|
| Package import, side effects, pure package helpers, retained import compatibility | `connectors/ksgs/tests/` **only if this package/path survives** | May test local behavior; cannot prove system admission, policy, or release. |
| SourceDescriptor shape, source role, activation, cadence, citation, and registry linkage | Canonical root source-admission/source tests under `tests/` plus accepted schema/validator lanes | This folder may call the accepted behavior but must not fork it. |
| Geology semantics, KGS/KCC anti-collapse, borehole rights, public-safe geometry, catalog closure, and evidence-before-AI | `tests/domains/geology/` | Connector tests preserve fields; domain tests decide domain semantic expectations. |
| Hydrology use of WWC5 or groundwater products | Hydrology-owned tests under the canonical domain test lane | KGS package tests must not turn completion records into current groundwater truth. |
| Hazards use of seismic context | Hazards-owned tests under the canonical domain test lane | KGS package tests must not become alert, event, or operational hazard authority. |
| Rights, sensitivity, privacy, access, and release obligations | Canonical policy tests and their accepted fixtures | Connector-local tests assert fail-closed integration; policy remains external. |
| Shared synthetic Geology examples | `fixtures/domains/geology/` | Reuse without copying into a competing fixture authority. |
| Deterministic unit-test-only examples | `tests/fixtures/` or another accepted test-fixture lane | Final KGS-specific subpath remains `NEEDS VERIFICATION`; do not create it from this README alone. |
| Release, correction, withdrawal, supersession, and rollback | Root release tests and `release/` authority surfaces | Connector-local tests must only prove they cannot perform these actions. |

The present connector topology is unresolved, so this routing table describes responsibility—not authorization to create missing paths.

### Required future test families

Before KSGS/KGS implementation maturity can be claimed, the accepted test plan should cover at least these families:

1. **Import and side-effect tests.** Importing any retained package performs no network request, credential lookup, filesystem write, cache mutation, lifecycle write, logging of sensitive values, or source activation.
2. **Greenfield-placeholder denial tests.** Comment-only modules and `0.0.0` metadata cannot be reported as working behavior; missing callables or commands fail clearly.
3. **Path and identity tests.** No test assumes `kgs`, `ksgs`, `connectors/ksgs/`, `connectors/kgs/`, `connectors/geology/kgs/`, or proposed `connectors/kansas/kgs/` is canonical without accepted migration evidence.
4. **Descriptor and activation tests.** The local four-field descriptor, `TBD` domain templates, missing authority entry, missing review, and missing activation all deny or hold access.
5. **Product-dispatch tests.** Bedrock, surficial, oil-and-gas wells, production aggregates, WWC5, LAS logs, interpreted tops, Geoportal resources, natural-resource records, and seismic context remain independently identifiable.
6. **Source-role anti-collapse tests.** Observations, compilations, interpretations, aggregates, regulatory records, modeled surfaces, candidates, and generated text never upgrade one another.
7. **Cross-publisher tests.** KGS material does not become KCC regulatory determination, KDHE environmental decision, KDA-DWR water-right decision, USGS authority, or another publisher's record.
8. **Rights and attribution tests.** Unknown, expired, inconsistent, product-specific, or non-redistributable rights fail closed and preserve attribution/disclaimer obligations.
9. **Sensitivity and privacy tests.** Exact/private wells, boreholes, samples, logs, owners, parcels, sensitive subsurface locations, and harmful joins deny public use unless an accepted policy and transform support exposure.
10. **Geometry and uncertainty tests.** CRS, datum, scale, depth reference, units, coordinate source, PLSS derivation, precision, uncertainty, and generalization state remain explicit.
11. **Temporal and source-head tests.** Source vintage, observation/reporting period, retrieval time, source head, correction time, stale state, and supersession remain distinct where material.
12. **Lifecycle and output-boundary tests.** Package code returns side-effect-free candidates only and cannot write directly to lifecycle, evidence, catalog, proof, release, or publication roots.
13. **Correction and withdrawal tests.** Re-cataloging, source corrections, withdrawn records, replaced maps/logs, rights changes, and superseded descriptors remain traceable.
14. **Carrier-boundary tests.** A map, tile, graph edge, index, search result, AI answer, workflow result, or connector receipt cannot become sovereign truth or release approval.
15. **Fixture-safety tests.** Default fixtures are synthetic, compact, deterministic, public-safe, source-labeled, and expected-outcome-labeled.
16. **CI-truthfulness tests.** The workflow must actually discover and run the accepted KGS tests; a TODO echo or empty discovery result must not pass as substantive coverage.

### KGS product anti-collapse matrix

| Product or record family | Tests must preserve | Tests must deny |
|---|---|---|
| Bedrock and surficial geologic maps | Publication/map identity, unit identity, compilation method, scale, vintage, CRS/datum, geometry, source URI, disclaimer. | Compilation presented as direct observation, current site condition, engineering advice, or scale-free truth. |
| Oil-and-gas wells | Well/API identity, location source, uncertainty, status/vintage, record type, source role. | KGS record presented as KCC permit/compliance finding, current operational status, reserve, forecast, or safe drilling decision. |
| Oil-and-gas production | Lease/field/reporting-period identity, aggregation unit, correction state, source role. | Aggregate production assigned to a well/place without support or treated as a resource estimate/reserve. |
| WWC5 water-well completion | Joint-program identity, completion/well identity, construction fields, coordinate derivation, precision, disclaimer, vintage. | Completion record presented as current water quality, aquifer condition, safe supply, water right, or exact public private-well location by default. |
| LAS logs and curves | Well/log/curve identity, mnemonic, units, depth reference, datum, null values, source/version. | Measured curve silently replaced by interpreted top, modeled surface, canonical stratigraphy, or operational engineering advice. |
| Well tops and interpretations | Interpreter/source, method, confidence, depth/datum, version, correction lineage. | Interpretation presented as raw measurement or universally accepted geology. |
| Geoportal resources | Resource-specific endpoint/distribution, schema, role, rights, cadence, geometry, vintage. | Mixed portal content admitted under one publisher-wide role or one generic descriptor. |
| Natural-resource/mineral records | Occurrence/deposit/estimate/extraction/administrative class, evidence, geometry, uncertainty, vintage. | Occurrence presented as reserve, estimate as observation, extraction record as geology truth, or exact sensitive site exposed. |
| Seismic context | Dataset/product identity, event versus background context, source role, time, uncertainty, official-source links. | KGS context presented as public alert authority, emergency instruction, deterministic cause, or real-time completeness guarantee. |

### Fixture posture

The default is **no network, synthetic, public-safe, and negative-first**.

A stable fixture must record, as applicable:

- synthetic marker and generation note;
- product family and source role;
- fake publisher/source/product/record identifiers that cannot be mistaken for live records;
- geometry source, CRS/datum, precision, uncertainty, and whether coordinates are intentionally generalized;
- temporal fields and source vintage;
- rights, attribution, disclaimer, sensitivity, access, and expected policy outcome;
- expected test outcome and the rule being exercised;
- correction, withdrawal, or supersession state;
- why repository storage is safe.

Do not commit:

- bulk source harvests;
- real restricted media or proprietary logs;
- credentials or authenticated responses;
- real exact private wells, boreholes, samples, owner/parcel joins, extraction sites, or other sensitive locations;
- a fixture whose rights or sensitivity cannot be reviewed;
- a copied registry record mislabeled as a fixture;
- generated AI text presented as source content or expected truth.

When fixture safety is unresolved, write a synthetic shape-only example or test the hold/deny/quarantine path without including the material.

### Placeholder, registry, and schema negative cases

The current repository contains several machine-shaped surfaces that must not be mistaken for readiness.

| Surface | Current evidence | Required test posture |
|---|---|---|
| `src/ksgs/descriptor.yaml` | `name: ksgs`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Reject or ignore for authority; must not activate, fetch, admit, or mark public-safe. |
| `data/registry/geology/sources/ksgs_bedrock.yaml` | `PROPOSED` greenfield template; role, authority, rights, sensitivity, cadence, access, and citation unresolved. | Treat as invalid/incomplete for activation until migrated and reviewed. |
| `data/registry/geology/sources/ksgs_oil_and_gas.yaml` | Same `TBD` template posture. | Hold/deny; require product-specific role, aggregation, rights, sensitivity, and cadence evidence. |
| `data/registry/geology/sources/ksgs_natural_resources.yaml` | Same `TBD` template posture. | Hold/deny; prevent occurrence/deposit/estimate/extraction collapse. |
| `data/registry/hazards/sources/ksgs_seismic.yaml` | Same `TBD` template posture. | Hold/deny; never infer alert or operational hazard authority. |
| `control_plane/source_authority_register.yaml` | Register is `PROPOSED` and `entries: []`. | No KGS machine authority or activation is established. |
| Singular SourceDescriptor schema | Rich required-field schema; metadata identifies the path as legacy and points to the plural path. | Useful as minimum-field and migration-conflict evidence; not unilateral final path authority. |
| Plural SourceDescriptor schema | Empty `PROPOSED` scaffold with unrestricted properties. | Passing it cannot prove meaningful descriptor conformance. |
| ADR-0001 schema-home file | Current filename exists, but status is `proposed`. | Respect its placement direction; do not claim accepted schema-path or field-level resolution. |

Until these conflicts are resolved, a meaningful test must assert fail-closed behavior rather than selecting whichever artifact is easiest to satisfy.

### No-network and side-effect contract

A future accepted package/test runner must prove:

```text
import retained package
  -> no network
  -> no DNS lookup
  -> no credential lookup
  -> no filesystem or cache write
  -> no lifecycle write
  -> no source activation
  -> no receipt, proof, catalog, release, or public artifact
```

Live-source integration tests, if ever approved, must be:

- explicitly opt-in;
- isolated from default CI;
- source-steward and rights-reviewed;
- credential-safe and least-privilege;
- rate-limited, timeout-bounded, and auditable;
- safe against logging or snapshotting private responses;
- incapable of publication;
- paired with a deterministic offline contract test.

This README does not approve such a test.

### Validation matrix

| Condition | Required outcome |
|---|---|
| No executable test module or runner is present | Do not claim test coverage, CI enforcement, package readiness, or source readiness. |
| Import causes network, credential, filesystem, cache, lifecycle, or publication side effect | **FAIL** |
| Local four-field descriptor is accepted as authority | **FAIL / DENY** |
| A domain registry template contains `TBD`, missing review, or unresolved rights/sensitivity | **HOLD / DENY** |
| Empty plural schema is treated as meaningful SourceDescriptor validation | **FAIL** |
| Descriptor, authority entry, or activation decision is missing | **DENY** |
| Path or slug is treated as canonical without accepted migration evidence | **FAIL** |
| Product identity or record class is missing | **HOLD / QUARANTINE** |
| KGS observation/aggregate is upgraded to KCC regulation or another publisher's authority | **FAIL / DENY** |
| Unknown rights, terms, attribution, or redistribution posture | **HOLD / DENY PUBLIC USE** |
| Placeholder `sensitivity_floor: public` overrides stricter or unresolved review | **FAIL / MOST RESTRICTIVE / HOLD** |
| Real exact well, borehole, sample, private-land, owner, parcel, or sensitive site enters a default fixture | **FAIL / REMOVE / REVIEW INCIDENT** |
| PLSS-derived or otherwise approximate coordinate lacks derivation and uncertainty | **HOLD / QUARANTINE** |
| Scale, CRS/datum, depth reference, units, vintage, or source head is materially missing | **HOLD / ABSTAIN** |
| Default test contacts a live source | **FAIL** |
| Package writes beyond an in-memory/caller-owned candidate result | **FAIL** |
| Package creates actual receipt, proof, catalog, release, rollback, or published artifact | **FAIL** |
| Source correction, withdrawal, rights change, or supersession is discarded | **FAIL / HOLD** |
| Map, tile, graph, search, workflow, or AI result is treated as root truth | **FAIL / ABSTAIN** |
| Workflow executes only TODO echo steps | Workflow may be green, but substantive KGS test coverage remains **UNKNOWN** |
| Valid and invalid synthetic fixtures do not cover fail-closed paths | **DO NOT CLAIM IMPLEMENTATION READINESS** |

Exact exception classes, result DTOs, outcome enums, reason codes, report schemas, and runner commands remain `NEEDS VERIFICATION`; this README does not invent them.

### Current CI reality

Two repository workflows are relevant by name but do not currently prove KSGS behavior:

```text
.github/workflows/connector-gate.yml
  -> echo TODO connector-output-gate
  -> echo TODO ingest-receipt-presence

.github/workflows/source-descriptor-validate.yml
  -> echo TODO validate-descriptors
  -> echo TODO rights-presence
```

Therefore:

- a successful run proves that GitHub Actions checked out the repository and executed the stub step;
- it does not prove test discovery, package import, no-network behavior, descriptor validity, rights presence, source activation, output boundaries, fixture safety, or KGS product semantics;
- repository-wide schema, policy, domain, or release checks may provide useful regression evidence, but they do not establish this package's implementation;
- future CI must show the exact command, discovered test count, exit status, and fail-closed negative cases before the README may claim coverage.

[Back to top](#top)

---

## Review burden

Changes require review proportionate to the rule they affect:

- **README-only boundary clarification:** test/validation steward plus connector/package or docs steward.
- **Executable connector-local test:** package maintainer, connector steward, test steward, and owner of the code under test.
- **SourceDescriptor, source ID, role, registry, or activation test:** source-registry, contract/schema, policy, and KGS source stewards.
- **Bedrock, surficial, natural-resource, well-log, or production semantics:** Geology steward.
- **WWC5 or groundwater interpretation:** Geology and Hydrology stewards, plus joint-program/source review.
- **Seismic/hazard interpretation:** Geology and Hazards stewards; no alert-authority assumption.
- **Rights, attribution, redistribution, or source terms:** rights reviewer and source steward.
- **Exact/private wells, owner/parcel joins, sensitive subsurface sites, or public generalization:** privacy/sensitivity reviewer, domain steward, and policy reviewer.
- **Live integration test or credential mode:** security reviewer, source steward, rights reviewer, connector maintainer, and CI owner.
- **Path/slug/import migration:** connector architecture steward, package maintainer, test steward, docs steward, and ADR/migration reviewers.
- **Release-affecting behavior:** separate release authority; connector-local approval is insufficient.

The inspected CODEOWNERS posture does not establish package-specific reviewer accounts here. Exact teams and assignments remain `UNKNOWN`; this README does not invent them.

[Back to top](#top)

---

## Related folders

| Surface | Responsibility | Current relationship |
|---|---|---|
| [`../README.md`](../README.md) | Parent KSGS connector boundary. | Existing path documentation; older canonicality wording must be read against newer conflict evidence. |
| [`../src/README.md`](../src/README.md) | Python source-layout boundary. | Confirms one greenfield package and no operational behavior. |
| [`../src/ksgs/README.md`](../src/ksgs/README.md) | Package scaffold boundary. | Primary package-state evidence for tests. |
| [`../src/ksgs/descriptor.yaml`](../src/ksgs/descriptor.yaml) | Connector-local placeholder metadata. | Negative test input only; not authority. |
| [`../../kgs/README.md`](../../kgs/README.md) | Competing top-level KGS compatibility lane. | Path-conflict evidence; not implementation authority. |
| [`../../geology/kgs/README.md`](../../geology/kgs/README.md) | Domain-scoped compatibility pointer. | Newer repository-grounded evidence that this domain path is not an implementation home and final placement is unresolved. |
| [`../../kansas/README.md`](../../kansas/README.md) | Kansas source-family coordination. | Family-level context; does not create the absent KGS child. |
| [`../../../docs/sources/catalog/kansas/ksgs.md`](../../../docs/sources/catalog/kansas/ksgs.md) | Human-facing KGS source profile. | Product, role, rights, sensitivity, and test requirements; not machine authority. |
| [`../../../tests/README.md`](../../../tests/README.md) | Canonical test responsibility root. | Owns cross-system enforceability proof. |
| [`../../../tests/domains/geology/README.md`](../../../tests/domains/geology/README.md) | Geology domain tests. | Owns domain semantics, public-safe geometry, catalog closure, and evidence-before-AI checks. |
| [`../../../fixtures/README.md`](../../../fixtures/README.md) | Shared runtime/synthetic fixture root. | Distinguishes runtime/shared examples from deterministic test-only fixtures. |
| [`../../../fixtures/domains/geology/README.md`](../../../fixtures/domains/geology/README.md) | Shared Geology fixtures. | Existing synthetic/public-safe examples; avoid duplication. |
| [`../../../contracts/source/source_descriptor.md`](../../../contracts/source/source_descriptor.md) | SourceDescriptor meaning. | Tests consume meaning; they do not redefine it. |
| [`../../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../../schemas/contracts/v1/source/source_descriptor.schema.json) | Rich singular-path schema. | Populated but self-described as legacy. |
| [`../../../schemas/contracts/v1/sources/source_descriptor.schema.json`](../../../schemas/contracts/v1/sources/source_descriptor.schema.json) | Plural-path schema. | Empty `PROPOSED` scaffold; not meaningful conformance proof. |
| [`../../../control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | Machine authority map. | `PROPOSED` with no entries; no KGS authority established. |
| `../../../policy/rights/` and `../../../policy/sensitivity/` | Rights and sensitivity policy. | External authority; connector-local tests must fail closed when unresolved. |
| `../../../release/` | Release, correction, withdrawal, supersession, and rollback authority. | Outside connector-local tests. |

The proposed `connectors/kansas/kgs/` path was not present at the pinned base and is intentionally not linked as a live directory.

[Back to top](#top)

---

## ADRs

### Directory Rules basis

- `connectors/` is the responsibility root for source-specific fetch and admission implementation.
- `tests/` is the canonical responsibility root for enforceability proof.
- `fixtures/` and `tests/fixtures/` must have a documented split and must not become lifecycle or truth stores.
- An existing local test directory may document package-local behavior, but it must not become a parallel schema, source, registry, policy, domain-test, release, proof, or fixture authority.
- A path move or identity change must preserve imports, tests, fixtures, descriptors, source IDs, references, history, deprecation state, correction state, and rollback.
- Promotion remains a governed state transition outside connectors and connector-local tests.

### Current ADR posture

- [`ADR-0001 — Schema Home`](../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) exists under its current long filename and has status `proposed`. It directs machine-checkable shape toward `schemas/contracts/v1/`, but it does not resolve the singular/plural SourceDescriptor conflict or field content by itself.
- No accepted ADR or migration record was verified that selects the final KGS connector path, `kgs` versus `ksgs` identity, package import, source-ID namespace, local test home, losing-path disposition, or compatibility sunset.
- The source profile tracks the slug issue as `OPEN-KSGS-13`; an open question is not an accepted decision.
- This README-only edit creates no new path and changes no authority boundary, so it does not itself require a new ADR.
- Adding executable implementation or moving these tests before the path decision would be premature.

[Back to top](#top)

---

## Last reviewed

**Documentation review date:** `2026-07-13`  
**Evidence base:** `main` at `d462f52e9a3b16ea19ad8512895505f0b15d1e27`  
**Prior README blob:** `5e4c87a12e91a87b4148691840a41f1bd3513201`  
**Review scope:** this Markdown file, directly related package files, named test probes, current KGS path documentation, source-catalog/descriptor/registry surfaces, fixture/test root documentation, and relevant workflow stubs.

This date is not a source-rights review, security approval, test run, package release, source activation, or KFM publication date.

[Back to top](#top)

---

## Evidence basis

| Evidence | Supports | Does not prove |
|---|---|---|
| Target blob `5e4c87a12e91a87b4148691840a41f1bd3513201` | Exact v0.1 baseline, stale generic inventory language, remote badges, and unresolved rollback placeholder. | Executable test behavior. |
| Introduction commit `1ffda65bd58cae71a60443e87da2e792de68f29f` | v0.1 replaced a three-line greenfield stub. | That restoring the stub is the best rollback now. |
| Exact test-path probes and indexed search | Named conventional test modules and local fixture README were not found; target README is indexed. | Complete recursive absence of differently named or unindexed files. |
| `pyproject.toml` | Project name `kfm-connector-ksgs` and version `0.0.0`. | Buildability, runner, dependencies, entry point, or supported Python. |
| Empty `__init__.py`, comment-only `fetch.py` and `admit.py` | Greenfield package intent only. | Fetch, admission, parsing, network, validation, or output behavior. |
| Local `descriptor.yaml` | Minimal placeholder values exist. | Descriptor conformance, source role, rights, sensitivity, activation, or release. |
| Domain registry templates | Several KSGS-named candidate records exist with `TBD` values. | Accepted registry authority or active sources. |
| SourceDescriptor schemas and proposed ADR | Current shape/path conflict and richer required field set. | One accepted executable schema/validator authority. |
| Empty machine source-authority register | No authority entry is established in that surface. | Absence from every differently named or private system. |
| Parent/package/source-layout READMEs | Actual scaffold state and unresolved KGS topology. | Runtime implementation or canonical path. |
| KGS source catalog | Human-facing product distinctions, risks, and proposed tests. | Live path presence, source access, rights clearance, activation, or machine authority. |
| Root tests and Geology tests READMEs | Canonical enforceability and domain-test responsibility. | Actual runner, modules, coverage, or passing results. |
| Root and Geology fixture READMEs | Fixture-home and synthetic/public-safe boundaries. | KGS-specific fixture payload presence or safety review. |
| Connector workflow YAML | Current TODO-only job content. | Substantive connector or SourceDescriptor validation. |
| Directory Rules and KFM doctrine | Responsibility-root placement, fail-closed posture, lifecycle, trust membrane, and reversible change. | Current KGS endpoint, terms, runtime, or release state. |

Absence and maturity statements are bounded to the pinned commit, indexed search, and exact reads. This README does not claim an exhaustive recursive inventory.

[Back to top](#top)

---

## Definition of done

### Documentation-only readiness for this README

- [x] Current path, base commit, prior blob, and introduction commit are recorded.
- [x] The actual `0.0.0` package scaffold is described without runtime overclaiming.
- [x] Named conventional test paths are explicitly recorded as absent at the inspected base.
- [x] Remote badges and unsupported coverage/maturity signals are removed.
- [x] Local and domain registry placeholders are classified as fail-closed negative inputs, not authority.
- [x] Connector-path, package-identity, schema, registry, fixture, and test-routing conflicts remain visible.
- [x] Purpose, authority, status, inclusions, exclusions, inputs, outputs, validation, review burden, related folders, ADRs, last review, evidence, rollback, and backlog are present.
- [x] Product identity, source role, KGS/KCC/KDHE cross-publisher boundaries, rights, sensitivity, geometry, time, correction, lifecycle, AI/map, and publication anti-collapse tests are specified.
- [x] Current CI TODO stubs are distinguished from substantive coverage.

### Implementation readiness still open

- [ ] An accepted ADR or migration record selects the final KGS connector, distribution, import, source-ID, and test homes.
- [ ] One enforceable SourceDescriptor contract/schema/validator path is accepted and migrated.
- [ ] Product-specific descriptors, authority entries, rights reviews, sensitivity reviews, source heads, review states, and activation decisions exist.
- [ ] Current source access methods, terms, attribution, redistribution, cadence, rate limits, disclaimers, correction, and supersession behavior are verified.
- [ ] Package metadata declares an accepted build, dependency, package-discovery, supported-Python, and test-runner contract.
- [ ] Executable package code exists with explicit no-network defaults and bounded outcomes.
- [ ] Safe valid, invalid, denied, abstain, error, stale, corrected, withdrawn, and superseded fixtures exist in accepted homes.
- [ ] Connector-local, source, Geology, Hydrology, Hazards, policy, security, and release tests are routed without duplication.
- [ ] CI runs the exact test command, reports discovered tests, and demonstrates negative/fail-closed behavior.
- [ ] Connector/package/test owners and required reviewers are assigned.
- [ ] Rollback and import/path migration are tested before compatibility paths are retired.

Documentation readiness does not imply test coverage, package readiness, source activation, evidence closure, rights approval, sensitivity clearance, or public release.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to justify:

- executable test coverage or CI enforcement that was not observed;
- canonical status for the current `ksgs` path, package, slug, descriptor, registry template, or test lane;
- live-source access or activation from placeholder code or metadata;
- `role: TBD`, `rights: TBD`, `sensitivity_floor: public`, or other unresolved template fields as accepted decisions;
- use of the empty plural schema as meaningful conformance;
- storage of real, restricted, private, or sensitive KGS material in fixtures;
- bypass of source role, rights, sensitivity, geometry, review, evidence, correction, release, or rollback controls;
- direct connector/test writes to lifecycle, receipt, proof, catalog, release, or publication surfaces;
- a map, tile, workflow, search result, graph edge, AI answer, or generated summary as KGS truth.

Before merge, rollback is to leave the review branch unmerged and abandon the proposed change. Closing a pull request or deleting a branch is a separate repository action.

After merge, restore prior README blob:

```text
5e4c87a12e91a87b4148691840a41f1bd3513201
```

from base:

```text
d462f52e9a3b16ea19ad8512895505f0b15d1e27
```

through a transparent revert commit or revert pull request, then rerun applicable documentation and connector-boundary checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm complete recursive test inventory under `connectors/ksgs/tests/`. | **UNKNOWN** | Git tree receipt or mounted checkout; compare with indexed search. |
| Resolve final KGS connector, distribution, import, source-ID, and test paths. | **CONFLICTED** | Accepted ADR/migration, import/reference inventory, deprecation records, tests, and rollback plan. |
| Reconcile `KGS`, `kgs`, and `ksgs` identities. | **CONFLICTED** | Stable naming/identity decision and compatibility map. |
| Decide whether connector-local tests survive or move entirely to root `tests/`. | **NEEDS VERIFICATION** | Package/path decision plus test-ownership review. |
| Resolve SourceDescriptor singular/plural schema and validator authority. | **CONFLICTED** | Accepted ADR/contract, one meaningful schema, validator, valid/invalid fixtures, and migration. |
| Migrate or retire the package-local descriptor. | **NEEDS VERIFICATION** | Source-registry, package, schema, policy, and migration review. |
| Migrate, validate, or retire the KSGS domain registry templates. | **NEEDS VERIFICATION** | Product descriptors, rights/sensitivity review, authority entries, fixtures, and validation reports. |
| Confirm product-specific access, terms, attribution, redistribution, cadence, source head, and correction behavior. | **NEEDS VERIFICATION** | Current authoritative source documentation and steward review. |
| Define exact package inputs, outputs, finite outcomes, DTOs, reason codes, exceptions, and side-effect boundaries. | **NEEDS VERIFICATION** | Accepted contracts, implementation, and tests. |
| Confirm safe KGS fixture homes and fixture rights. | **UNKNOWN** | Fixture inventory, generation notes, rights/sensitivity review, expected outcomes, and consumer tests. |
| Implement import/no-network/descriptor/activation/product/role/rights/sensitivity/geometry/time/lifecycle/correction tests. | **NOT IMPLEMENTED AT NAMED PATHS** | Test modules and observed runner results. |
| Replace TODO-only workflows with substantive commands and negative coverage. | **NEEDS VERIFICATION** | Workflow patch, exact command, discovery count, logs, and failure demonstration. |
| Confirm cross-domain routing for WWC5 and seismic context. | **NEEDS VERIFICATION** | Geology, Hydrology, Hazards, source, and policy ownership decision. |
| Confirm KGS/KCC/KDHE/KDA-DWR/USGS cross-publisher anti-collapse coverage. | **NEEDS VERIFICATION** | Contracts, fixtures, policy, and tests. |
| Assign package, source, domain, test, security, rights, sensitivity, and release reviewers. | **UNKNOWN** | CODEOWNERS or accepted ownership records. |
| Verify applicable CI and repository-wide promotion prerequisites for the resulting PR. | **NEEDS VERIFICATION** | Pull-request workflow runs and scoped interpretation. |

[Back to top](#top)

---

## Maintainer note

Keep this lane documentation-only until the repository resolves the KGS path and identity conflict and creates one small offline proof-bearing slice.

The safest first executable increment is not a live fetch. It is a synthetic negative-first test that:

1. imports the retained package without side effects;
2. rejects `src/ksgs/descriptor.yaml`;
3. rejects one `TBD` KSGS registry template;
4. preserves product identity and uncertainty;
5. returns a caller-owned hold/quarantine candidate;
6. proves no lifecycle or release write occurred.

Only after that slice, product-specific governance, and observed CI exist should an opt-in source-access test be considered. Evidence closure, domain truth, public-safe transformation, release approval, publication, correction, withdrawal, and rollback remain outside this connector-local test lane.

[Back to top](#top)
