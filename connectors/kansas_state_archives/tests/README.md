<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kansas-state-archives-tests-readme
title: connectors/kansas_state_archives/tests/ — Kansas State Archives Greenfield Connector Test Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Test steward · Kansas source steward · Archives steward · Rights reviewer · Sensitivity/privacy reviewer · CARE/cultural/sovereignty reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-local-tests; greenfield-scaffold; compatibility-path; path-and-surface-conflict; no-network; synthetic-fixtures; rights-fail-closed; sensitivity-fail-closed; care-review; no-activation; no-publication
current_path: connectors/kansas_state_archives/tests/README.md
truth_posture: CONFIRMED README-only inspected test lane, named conventional test paths absent, 0.0.0 package scaffold, placeholder descriptor, and TODO-only connector workflows / CONFLICTED compatibility class, final connector and test paths, KSHS umbrella-versus-surface scope, SourceDescriptor authority, and fixture routing / PROPOSED fail-closed connector-local test contract / UNKNOWN differently named tests, package runtime, source access, activation, rights clearance, sensitive-record handling, substantive CI coverage, and deployment
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 40deb4a3cab0972f0c7d38930e30c3b497408b0a
  prior_blob: c44d6abbc84e8870c25a242d417c3c6f30fdaf09
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/kansas_state_archives/README.md
  - ../src/kansas_state_archives/descriptor.yaml
  - ../../kansas/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/README.md
  - ../../../docs/sources/catalog/kansas/kansas-state-archives.md
  - ../../../docs/sources/catalog/kansas_state_archives.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../tests/README.md
  - ../../../tests/fixtures/README.md
  - ../../../fixtures/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
tags: [kfm, connectors, kansas-state-archives, kshs, archives, tests, python, greenfield, compatibility, source-admission, source-role, rights, privacy, sensitivity, care, fixtures, no-network, fail-closed, raw, quarantine, governance]
notes:
  - 'The inspected connector-local test directory contains this README; exact probes did not find __init__.py, conftest.py, test_import.py, test_fetch.py, test_admit.py, test_descriptor.py, test_surface_identity.py, test_no_network.py, or tests/fixtures/README.md.'
  - 'Absence claims are bounded to the pinned base, exact named probes, and the available indexed search. Differently named or unindexed files remain UNKNOWN.'
  - 'The package is a 0.0.0 greenfield scaffold: __init__.py is empty, fetch.py and admit.py are comment-only placeholders, and descriptor.yaml is a four-field nonconforming placeholder.'
  - 'The local descriptor must be treated as a negative test input, not as SourceDescriptor authority, source activation, rights clearance, sensitivity clearance, or public-release evidence.'
  - 'The connector-gate and source-descriptor-validate workflows execute TODO echo steps; a green workflow result does not establish connector-local test coverage.'
  - 'Only this Markdown file is in scope. No test, fixture, code, package metadata, schema, contract, policy, descriptor, registry entry, workflow, receipt, source activation, path move, release object, or public artifact is created or changed.'
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas State Archives Greenfield Connector Test Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Current test maturity:** README-only inspected lane; executable tests were not found at the named conventional paths  
> **Package maturity:** `0.0.0` greenfield scaffold; fetch and admission behavior are not implemented  
> **Path posture:** the current top-level connector exists, but its compatibility class, final connector path, package scope, and long-term test home are `CONFLICTED / NEEDS VERIFICATION`  
> **Boundary:** this folder may eventually hold narrow package-local tests. It does not activate a KSHS source, prove source access, establish descriptor authority, approve sensitive records, write lifecycle state, authorize release, or publish archive content.

> [!WARNING]
> A README, directory, package name, local `descriptor.yaml`, source-catalog statement, pull request, merge, or green TODO-only workflow is not test coverage. Until executable tests, safe fixtures, an accepted runner, and observed results exist, package behavior remains `UNKNOWN` and source activation remains denied.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence](#evidence-basis) · [Fixture contract](#fixture-contract) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kansas_state_archives/tests/` is the repository-present test-documentation lane beside the non-operational [`kansas_state_archives`](../src/kansas_state_archives/README.md) Python package scaffold.

Its narrow purpose is to define what **connector-local** tests must prove if this package is retained, delegated, or migrated:

- importing or inspecting the package causes no network, credential, filesystem, lifecycle, registration, activation, logging, thread, or global-state side effect;
- the placeholder descriptor and any missing, stale, malformed, unreviewed, or inactive descriptor fail closed;
- Kansas State Archives proper, Kansas Memory, KHRI, publication indexes, and adjacent KSHS surfaces retain distinct identities and source roles;
- original records, digital surrogates, OCR, transcriptions, annotations, entity links, indexes, and generated summaries remain distinct derivatives;
- metadata, provenance, rights statements, sensitivity flags, cultural/CARE posture, and uncertainty are preserved rather than upgraded;
- package helpers return bounded candidates to caller-owned orchestration instead of writing lifecycle, receipt, proof, release, or publication state;
- compatibility behavior does not silently settle the package name, connector path, source-ID strategy, or KSHS umbrella-versus-surface design.

This folder is not the canonical home for all archive, source, policy, release, migration, or cross-system tests. Canonical enforceability belongs under the root [`tests/`](../../../tests/README.md) responsibility root; shared fixture ownership belongs under [`fixtures/`](../../../fixtures/README.md) or [`tests/fixtures/`](../../../tests/fixtures/README.md) according to the documented split.

[Back to top](#top)

---

## Authority level

**Connector-local test lane inside a repository-present compatibility scaffold. It has no source, schema, policy, lifecycle, evidence, release, or publication authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility | **CONFIRMED** | Tests prove behavior. Source-specific code belongs under `connectors/`; canonical cross-system enforceability belongs under root `tests/`. |
| Current path | **CONFIRMED** | `connectors/kansas_state_archives/tests/README.md` exists at the pinned base. |
| Current executable tests | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | Direct reads found the README but not the conventional modules listed in the current snapshot. |
| Current package behavior | **GREENFIELD PLACEHOLDER** | Empty initializer, comment-only fetch/admit modules, and minimal package metadata establish no runnable connector behavior. |
| Connector path and compatibility class | **CONFLICTED** | The top-level path exists; the Kansas-family child is proposed but unverified, and no accepted path-specific `legacy`, `mirror`, `deprecated`, or `transitional` decision was verified. |
| Package scope | **CONFLICTED** | Current documentation mixes a KSHS umbrella with independently governed surfaces. One package must not silently become one publisher-wide descriptor, role, rights profile, or activation state. |
| Descriptor and registry authority | **NOT ESTABLISHED** | The local YAML is nonconforming, the machine source-authority register has no entries, and policy READMEs are greenfield stubs. |
| Fixture authority | **OUTSIDE THIS README** | Test-local fixtures may belong under `tests/fixtures/`; shared fixtures may belong under root `fixtures/`. This connector-local README does not create a third fixture authority. |
| Source activation | **DENIED / NOT VERIFIED** | No conforming per-surface descriptor, rights/sensitivity review, source head, activation decision, or executable gate was verified. |
| Public release | **NONE** | Connector-local tests cannot approve a public layer, map, API response, archive claim, receipt, proof, release, correction, or rollback. |

Editing this README does not ratify the directory or select a future test home. A move, rename, consolidation, compatibility import, or new canonical child requires the applicable ADR or explicit migration discipline.

[Back to top](#top)

---

## Status

### Current bounded repository snapshot

The following map is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `40deb4a3cab0972f0c7d38930e30c3b497408b0a` and exact path reads:

```text
connectors/kansas_state_archives/
├── README.md
├── pyproject.toml                  # kfm-connector-kansas_state_archives, version 0.0.0
├── src/
│   ├── README.md
│   └── kansas_state_archives/
│       ├── README.md               # repository-grounded package boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field nonconforming placeholder
└── tests/
    └── README.md                   # this documentation contract
```

Exact probes returned `Not Found` for:

```text
connectors/kansas_state_archives/tests/__init__.py
connectors/kansas_state_archives/tests/conftest.py
connectors/kansas_state_archives/tests/test_import.py
connectors/kansas_state_archives/tests/test_fetch.py
connectors/kansas_state_archives/tests/test_admit.py
connectors/kansas_state_archives/tests/test_descriptor.py
connectors/kansas_state_archives/tests/test_surface_identity.py
connectors/kansas_state_archives/tests/test_no_network.py
connectors/kansas_state_archives/tests/fixtures/README.md
```

These absence statements are bounded to the pinned commit and named paths. Differently named, generated, external, ignored, or unindexed files remain `UNKNOWN`.

### Current maturity table

| Item | Current state | Safe conclusion |
|---|---|---|
| This README | **DRAFT v0.2** | Reviewable boundary documentation only. |
| Test runner | **NOT DECLARED** | [`pyproject.toml`](../pyproject.toml) declares no build backend, dependency, Python version, package discovery, test framework, or command. |
| Import-safety test | **NOT FOUND** | No no-side-effect import behavior is proven. |
| Fetch/no-network test | **NOT FOUND** | No transport, endpoint, retry, timeout, rate-limit, pagination, caching, source-head, or egress behavior is proven. |
| Admission/descriptor test | **NOT FOUND** | No descriptor gate, activation gate, finite outcome, quarantine candidate, or receipt-candidate behavior is proven. |
| Surface/derivative identity test | **NOT FOUND** | No preservation of KSHS surface identity or original-versus-derived record identity is proven. |
| Connector-local fixtures | **NOT FOUND AT NAMED PATH** | No fixture safety, rights review, generation note, or expected-output pairing is proven. |
| Repository-wide connector workflows | **TODO-ONLY STUBS** | [`connector-gate`](../../../.github/workflows/connector-gate.yml) and [`source-descriptor-validate`](../../../.github/workflows/source-descriptor-validate.yml) run `echo TODO ...`; green completion is not substantive coverage. |
| Source activation | **NOT CONFIRMED** | The directory, package, descriptor placeholder, source brief, or test README does not activate a source. |
| Current test outputs | **NONE CONFIRMED** | No test result, coverage report, validation report, candidate envelope, or CI evidence is emitted by the inspected lane. |

[Back to top](#top)

---

## What belongs here

While the lane remains README-only and its long-term placement remains unresolved, accepted material is limited to the smallest package-local test surface needed to keep the scaffold safe and reviewable.

### Documentation that belongs now

- this test-boundary README;
- migration-bound notes that explain delegation, deprecation, or compatibility behavior after an accepted decision;
- links to canonical test, fixture, contract, schema, policy, registry, and release authorities;
- evidence-bounded inventories of what was actually inspected and what remains unknown.

### Executable tests that may belong later

Only after the connector path, package scope, runner, descriptor authority, and fixture plan are accepted, narrow package-local tests may cover:

- import and package-discovery safety;
- no-network default and explicit transport injection;
- host allowlisting, timeout, retry, rate-limit, byte-limit, cancellation, and credential-boundary behavior;
- descriptor rejection and activation preconditions;
- source, surface, collection, item, record-class, and source-URI identity preservation;
- original record versus surrogate, OCR, transcription, annotation, index, entity-resolution, and generated-summary separation;
- title, creator, date, description, collection, retrieval-time, source-head, checksum, and provenance preservation where present;
- source-role anti-collapse across administrative, observational, discovery/index, inventory, candidate, and derived material;
- rights, attribution, redistribution, privacy, sensitivity, cultural, sovereignty, CARE, archaeology, private-land, and infrastructure fail-closed behavior;
- deterministic parsing and normalization that do not upgrade truth, confidence, authority, or release state;
- side-effect-free RAW/QUARANTINE **candidate** construction for caller-owned orchestration;
- deterministic deny, abstain, hold, error, and quarantine-candidate behavior without sensitive payload echo;
- migration/delegation behavior if the compatibility import survives.

Package-local tests must call accepted contracts, schemas, policies, validators, and registries rather than copy those rules into a parallel local authority.

[Back to top](#top)

---

## What does NOT belong here

Do not add or establish:

- live KSHS network calls in default tests;
- credentials, tokens, cookies, account data, private endpoints, access agreements, or production configuration;
- bulk archive downloads, media corpora, OCR dumps, or source payload caches;
- real living-person records, donor-restricted material, exact archaeological or sacred-place coordinates, culturally restricted records, private-land detail, or sensitive infrastructure information;
- fixtures with unknown rights, missing generation notes, or unclear sensitivity posture;
- a connector-local SourceDescriptor, activation decision, source-authority register, schema, contract, policy bundle, or release decision;
- a third fixture authority beside root `fixtures/` and `tests/fixtures/`;
- direct writes to RAW, QUARANTINE, receipts, proofs, WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, correction, rollback, or release roots;
- public API, map, tile, timeline, search-index, graph, embedding, summary, screenshot, export, or AI-answer assertions;
- generated language, OCR, transcription, index metadata, or entity links presented as verified historical truth;
- tests that silently treat the top-level package as canonical or collapse all KSHS surfaces into one source identity;
- claims of coverage, source activation, rights clearance, sensitivity clearance, public safety, CI maturity, or production readiness without executable evidence.

[Back to top](#top)

---

## Inputs

### Current inputs

No executable test-input contract is implemented or confirmed. The current lane contains documentation only, and the package metadata declares no runner or command.

### Permitted future inputs

After the applicable placement and activation decisions are accepted, package-local tests may receive only explicit, synthetic, public-safe, caller-controlled inputs such as:

- the package modules under test;
- a conforming per-surface descriptor fixture and deliberately invalid, missing, stale, unreviewed, restricted, and inactive variants;
- explicit activation-state fixtures that never activate a live source;
- injected fake transport, clock, retry policy, rate limiter, byte limiter, cancellation signal, and temporary destination;
- synthetic KSHS surface, collection, item, index, surrogate, OCR, transcription, annotation, and generated-summary metadata;
- toy source-head, checksum, retrieval-time, provenance, rights, sensitivity, cultural/CARE, privacy, and review values;
- caller-owned candidate sinks and expected finite outcomes;
- an accepted migration or delegation map if the compatibility path survives.

Missing, stale, malformed, conflicted, or unsafe trust-bearing inputs must fail before network access, persistence, or public exposure.

[Back to top](#top)

---

## Outputs

### Current outputs

**None confirmed.** The README-only lane emits no test result, coverage report, validation report, candidate envelope, receipt, lifecycle record, release object, or public artifact.

### Permitted future outputs

A separately approved test implementation may emit or assert only non-authoritative test evidence such as:

- test-run pass/fail results;
- deterministic expected-output comparisons;
- coverage or mutation-test reports, when an accepted runner defines them;
- no-network and no-side-effect assertions;
- structured expected failures and bounded reason codes;
- candidate-envelope shape assertions against accepted contracts;
- migration/delegation parity results;
- CI annotations or QA artifacts that remain outside source, evidence, policy, lifecycle, and release authority.

A test result is not a SourceDescriptor, EvidenceBundle, PolicyDecision, ReviewRecord, receipt, proof, ReleaseManifest, correction, rollback decision, published layer, or historical claim.

[Back to top](#top)

---

## Validation

### Documentation validation applicable now

- preserve one H1 and a logical heading hierarchy;
- preserve the KFM Meta Block v2 wrapper with current path, pinned base, prior blob, and bounded truth posture;
- follow the required folder-README section order from Directory Rules;
- keep all current-state claims bounded to inspected files, exact probes, and named workflow bytes;
- label future interfaces, tests, fixtures, outcomes, paths, and migration behavior as `PROPOSED` or `NEEDS VERIFICATION`;
- resolve repository-relative links to owning surfaces;
- include no remote badges, tracking images, credentials, source payloads, private data, restricted record details, or exact sensitive locations;
- end with a final newline, balanced fences, readable tables, and valid GitHub callouts;
- keep the change to this one requested Markdown path.

There is intentionally no quickstart or test command. Publishing one would imply a runner and behavior that the inspected project metadata does not define.

### Required future behavioral test matrix

| Test family | Required positive proof | Required fail-closed proof |
|---|---|---|
| Import and package discovery | Import succeeds without side effects. | Import attempts network, persistence, registration, logging secrets, or global mutation and the test fails. |
| Descriptor gate | A conforming reviewed per-surface fixture is accepted for local validation. | Missing, local-placeholder, malformed, stale, unreviewed, inactive, unknown-rights, or unsafe-sensitivity descriptor is rejected before transport. |
| Activation gate | Explicit fixture state permits only a synthetic operation. | Missing, denied, review-required, withdrawn, or conflicted activation blocks the operation. |
| No-network default | Fake transport is used and no egress occurs. | Any unexpected socket, HTTP, DNS, tile, image, IIIF, OAI-PMH, scrape, or vendor access fails the test. |
| Surface identity | State Archives proper, Kansas Memory, KHRI, and indexes retain distinct identifiers and roles. | Umbrella-wide default identity, role, rights, or sensitivity collapses are rejected. |
| Derivative identity | Original, surrogate, OCR, transcription, annotation, index, entity link, and generated summary remain distinct. | A derivative silently replaces or upgrades the original record and the test fails. |
| Metadata fidelity | Source URI, collection/item IDs, title/creator/date, retrieval time, source head, checksum, and provenance survive where supplied. | Required identity or provenance is dropped, guessed, rewritten, or made more precise without evidence. |
| Rights and attribution | Verified fixture terms and attribution are preserved. | Unknown, restricted, denied, noassertion, missing-attribution, or nonredistributable posture blocks public-track behavior. |
| Privacy, sensitivity, cultural, and CARE | Public-safe synthetic or transformed fixtures remain bounded. | Living-person, archaeology, sacred/cultural, sovereignty, private-land, or infrastructure concerns route to deny, hold, abstain, or quarantine candidate. |
| Parser and normalizer determinism | Repeated input yields the same bounded result. | Nondeterministic identity, field upgrade, hidden enrichment, or source-role mutation fails. |
| Candidate handoff | Side-effect-free RAW/QUARANTINE candidate shape is returned to caller-owned orchestration. | Direct write to any lifecycle, receipt, proof, release, correction, rollback, or public root fails. |
| Error hygiene | Structured error omits sensitive payload and credentials. | Raw record text, private details, tokens, or exact protected geometry appear in logs or exceptions and the test fails. |
| Fixture safety | Fixture is synthetic, compact, public-safe, deterministic, and paired with expected posture. | Live, bulk, unclear-rights, sensitive, credential-bearing, or unreviewed material is rejected. |
| Migration/delegation | Accepted compatibility shim delegates once with stable identity and no duplicate capture. | Duplicate fetch, duplicate activation, divergent behavior, silent aliasing, or missing rollback fails. |
| Publication denial | Package-local tests assert that connector success remains non-public. | Any test creates or approves a public map, layer, API answer, release, proof, or historical claim and fails. |

Outcome names and object shapes must come from accepted contracts. This README does not create a new enum, schema, or validator.

### Current workflow limit

The repository-present connector workflows are greenfield stubs. They check out the repository and run `echo TODO ...`; therefore their success can prove workflow execution only, not package import, test discovery, descriptor conformance, source-role preservation, rights/sensitivity enforcement, no-network behavior, candidate handoff, or public-release denial.

[Back to top](#top)

---

## Review burden

Changes here should be reviewed according to what they claim to prove, not merely by file extension.

| Change | Required review posture |
|---|---|
| README clarification only | Docs steward plus connector/package or test steward. |
| Import, parser, transport, or admission test | Connector/package maintainer plus test/validation steward. |
| Source identity, role, or descriptor test | Kansas source and archives steward plus contract/schema or source-registry reviewer as applicable. |
| Rights or attribution fixture/test | Rights reviewer. |
| Living-person, archaeology, cultural, sovereignty, CARE, private-land, or infrastructure case | Sensitivity/privacy reviewer, CARE/cultural/sovereignty reviewer, and security reviewer as applicable. |
| Fixture-home or shared-fixture change | Test and fixture stewards; document the `tests/fixtures/` versus root `fixtures/` split. |
| Path, package, source-ID, compatibility, or migration test | Architecture/migration reviewer and ADR review when the decision is ADR-class. |
| Release, correction, rollback, or public-output assertion | Release steward; these tests normally belong under the canonical root test lanes, not here. |

Current [CODEOWNERS](../../../.github/CODEOWNERS) provides a repository-wide fallback for this path but no Kansas State Archives connector-specific owner. Ownership remains `UNKNOWN` until a path-specific rule or accepted steward assignment exists.

[Back to top](#top)

---

## Related folders

| Surface | Relationship to this lane | Boundary |
|---|---|---|
| [`connectors/kansas_state_archives/`](../README.md) | Parent compatibility connector documentation. | Older draft posture; does not prove runtime or accepted migration. |
| [`src/`](../src/README.md) | Source-layout documentation. | Organizes package code; not test authority. |
| [`src/kansas_state_archives/`](../src/kansas_state_archives/README.md) | Repository-grounded `0.0.0` package boundary. | Confirms placeholder bytes and current no-runtime posture. |
| [`connectors/kansas/`](../../kansas/README.md) | Current Kansas source-family coordination lane. | Family context; does not prove a KSHS archive child exists. |
| [`tests/`](../../../tests/README.md) | Canonical cross-system enforceability root. | Source, schema, policy, lifecycle, release, and domain integration tests belong there when scope exceeds the package. |
| [`tests/fixtures/`](../../../tests/fixtures/README.md) | Unit-test-scoped synthetic fixtures. | Use for fixtures local to accepted tests; not a cross-cutting fixture authority. |
| [`fixtures/`](../../../fixtures/README.md) | Shared synthetic/runtime/golden fixture root. | Use for cross-cutting reusable fixtures; not lifecycle or source data. |
| [Nested KSHS source-family brief](../../../docs/sources/catalog/kansas/kansas-state-archives.md) | Documents KSHS umbrella and per-surface distinctions. | Human-facing draft; not descriptor or activation authority. |
| [Legacy flat catalog stub](../../../docs/sources/catalog/kansas_state_archives.md) | Conflicting older path and connector pointer. | Migration/supersession evidence; not canonicality. |
| [`SourceDescriptor` contract](../../../contracts/source/source_descriptor.md) | Defines source-admission meaning. | Contract is not executable validation. |
| [Paired singular-path schema](../../../schemas/contracts/v1/source/source_descriptor.schema.json) | Defines the currently populated machine shape and deprecated aliases. | Schema reports its own path migration conflict; no package-local copy. |
| [Source registry](../../../data/registry/sources/README.md) and [authority register](../../../control_plane/source_authority_register.yaml) | Own source identity/admission records and machine governance maps. | Current authority register has no entries; tests do not create authority. |
| [Rights](../../../policy/rights/README.md) and [sensitivity](../../../policy/sensitivity/README.md) | Own admissibility decisions. | Current READMEs are greenfield stubs; tests must not substitute local policy. |
| [Connector workflow](../../../.github/workflows/connector-gate.yml) and [descriptor workflow](../../../.github/workflows/source-descriptor-validate.yml) | Potential CI entry points. | Current jobs are TODO-only and do not establish substantive coverage. |

[Back to top](#top)

---

## ADRs

No ADR is triggered by this documentation-only revision: it changes no root, path, schema home, lifecycle phase, authority surface, source identity, compatibility class, sensitive-location posture, release gate, or publication path.

A future change requires an accepted ADR or explicit migration plan when it:

- chooses, renames, moves, merges, deprecates, or deletes a connector/package/test path;
- changes `kansas_state_archives` from a compatibility import into canonical implementation authority;
- settles KSHS umbrella-versus-per-surface packaging in a way that changes source identity or descriptor ownership;
- creates a new fixture, schema, contract, policy, registry, receipt, proof, release, or public-output authority;
- changes the SourceDescriptor schema-home decision or lifecycle boundaries;
- changes sensitive-record or exact-location posture;
- makes a compatibility shim responsible for duplicate capture, activation, persistence, or publication.

The current [`docs/adr/`](../../../docs/adr/README.md) lane explains ADR discipline. The populated SourceDescriptor schema currently declares a different canonical path than its own location; this README records that conflict but does not resolve it.

[Back to top](#top)

---

## Last reviewed

**2026-07-13** against repository `bartytime4life/Kansas-Frontier-Matrix`, immutable base commit `40deb4a3cab0972f0c7d38930e30c3b497408b0a`, and prior target blob `c44d6abbc84e8870c25a242d417c3c6f30fdaf09`.

This date records the documentation evidence pass. It is not a source-terms review, rights clearance, sensitivity review, activation decision, test run, CI certification, deployment review, release review, or publication date.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not support |
|---|---|---|---|
| This target README at prior blob `c44d6abb…` | `CONFIRMED` | Existing v0.1 test-boundary prose and rollback baseline. | Executable tests, fixtures, or CI coverage. |
| [`pyproject.toml`](../pyproject.toml) | `CONFIRMED` | Project name and version `0.0.0`. | Buildability, dependencies, supported Python, test runner, command, or package discovery. |
| Package files under [`src/kansas_state_archives/`](../src/kansas_state_archives/README.md) | `CONFIRMED` for exact reads | Empty initializer, comment-only fetch/admit files, and four-field placeholder descriptor. | Executable behavior, exhaustive recursive inventory, activation, or public safety. |
| Exact conventional test-path probes | `CONFIRMED absent at base` | The nine named files were not present at the pinned commit. | Universal absence of differently named, ignored, generated, external, or unindexed tests. |
| Root [`tests/`](../../../tests/README.md) README | `CONFIRMED draft` | Canonical enforceability responsibility and domain/source/policy/release test boundaries. | Actual runner, current pass rates, or coverage. |
| [`tests/fixtures/`](../../../tests/fixtures/README.md) and root [`fixtures/`](../../../fixtures/README.md) | `CONFIRMED draft` | Fixture-home split, synthetic/public-safe posture, and anti-authority boundary. | Archive fixture inventory or current consumer tests. |
| [Nested KSHS brief](../../../docs/sources/catalog/kansas/kansas-state-archives.md) | `CONFIRMED draft` | Umbrella/per-surface distinctions, rights and sensitivity concerns, and anti-collapse posture. | Current source access, terms, descriptors, activation, or release. |
| [`SourceDescriptor` contract](../../../contracts/source/source_descriptor.md) and [schema](../../../schemas/contracts/v1/source/source_descriptor.schema.json) | `CONFIRMED draft / PROPOSED schema` | Richer descriptor surface, deprecated aliases, and fail-closed requirements. | Accepted schema-path migration, persisted KSHS descriptors, or runtime enforcement. |
| [Source-authority register](../../../control_plane/source_authority_register.yaml) | `CONFIRMED` | Register is `PROPOSED` with `entries: []`. | Any KSHS source activation or authority decision. |
| [Rights](../../../policy/rights/README.md) and [sensitivity](../../../policy/sensitivity/README.md) READMEs | `CONFIRMED` | Both are greenfield stubs. | Executable or reviewed archive policy. |
| [Connector](../../../.github/workflows/connector-gate.yml) and [descriptor](../../../.github/workflows/source-descriptor-validate.yml) workflows | `CONFIRMED` | Pull-request-triggered workflow stubs exist. | Test discovery, descriptor validation, rights enforcement, connector behavior, or coverage; jobs only echo TODO messages. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md), [CONTRIBUTING](../../../CONTRIBUTING.md), [CODEOWNERS](../../../.github/CODEOWNERS), and [ADR guidance](../../../docs/adr/README.md) | `CONFIRMED` | Placement, smallest reversible change, review fallback, migration discipline, and authority separation. | Branch protection, required reviewers, or merge policy beyond inspected files. |

Not inspected: live KSHS services, current terms, credentials, source payloads, private or sensitive records, archive-media rights, deployed configuration, runtime logs, emitted receipts, release objects, public clients, or an exhaustive recursive tree. Treat all associated claims as `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Fixture contract

This README creates no fixture folder or payload. If executable tests are later approved, fixture placement must follow the existing split rather than growing a connector-local third authority.

| Fixture need | Preferred home | Required posture |
|---|---|---|
| Small fixture owned by one accepted package-local test | `tests/fixtures/` under an accepted child lane, or test-adjacent only if repository convention explicitly permits it | Synthetic, compact, deterministic, no-network, public-safe, expected outcome recorded. |
| Shared archive-source, parser, policy, or lifecycle example used by multiple test areas | Root `fixtures/` under an accepted domain/source lane | Synthetic or rights-cleared, reusable, source/generation note, public-safe, no authority claim. |
| Real archive payload or unresolved-rights material | Neither fixture home | Governed source/lifecycle intake or quarantine; never committed as a convenience fixture. |

Minimum future fixture families:

- valid minimal per-surface descriptor reference;
- missing, malformed, stale, inactive, denied, unknown-rights, and unsafe-sensitivity descriptor cases;
- separate State Archives proper, Kansas Memory, KHRI, and index identities;
- original record, surrogate, OCR, transcription, annotation, index, entity-link, and generated-summary distinctions;
- missing collection/item/source-URI/provenance cases;
- living-person, archaeology, cultural/CARE, private-land, and infrastructure canaries using synthetic or transformed values only;
- no-network transport canary;
- direct-write/publication denial canary;
- migration/delegation parity and duplicate-capture canary if a compatibility shim is accepted.

Each stable fixture should name its expected posture—such as validation pass, validation failure, deny, abstain, hold, quarantine candidate, no-op, or deterministic error—without claiming that this README defines the canonical outcome enum.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Current README-only test inventory is explicit and bounded.
- [x] `0.0.0` package maturity and placeholder bytes are explicit.
- [x] Named absent conventional test paths are recorded without claiming exhaustive absence.
- [x] Connector-path, compatibility-class, package-scope, descriptor, fixture-home, and source-catalog conflicts are visible.
- [x] Current inputs, outputs, runner, commands, tests, fixtures, activation, and publication are stated as absent or unknown.
- [x] Package-local versus root test responsibility is explicit.
- [x] Rights, privacy, sensitivity, cultural/CARE, derivative identity, and precise-location boundaries are fail closed.
- [x] TODO-only workflows are not represented as coverage.
- [x] Evidence limits and immutable rollback target are recorded.
- [x] Remote badge images and the prior unresolved rollback placeholder are removed.

### Implementation readiness

- [ ] Connector path, compatibility class, package/import name, source-ID strategy, and losing-path migration are accepted.
- [ ] KSHS umbrella versus per-surface adapter and descriptor strategy is accepted.
- [ ] Package build backend, supported Python versions, dependency policy, package discovery, test runner, and commands are defined.
- [ ] Owners and required reviewers are assigned.
- [ ] Per-surface conforming descriptors and explicit activation decisions exist in accepted authority surfaces.
- [ ] Current source access methods, terms, attribution, redistribution, cadence, source-head strategy, and correction behavior are reviewed.
- [ ] Synthetic or rights-cleared fixtures exist in an accepted fixture home with expected outcomes and generation notes.
- [ ] Import, no-network, descriptor, activation, surface, derivative, metadata, rights, sensitivity/CARE, candidate-handoff, error-hygiene, and publication-denial tests are executable.
- [ ] Cross-system policy, source, lifecycle, release, correction, and rollback tests are routed to canonical root test lanes.
- [ ] CI discovers the tests and emits substantive results rather than TODO-only success.
- [ ] Migration/delegation, duplicate-capture prevention, invalidation, correction, and rollback are tested.

Until every applicable implementation-readiness item closes, keep this test lane documentation-only, the package inert, and source access fail closed.

[Back to top](#top)

---

## Rollback

Rollback this README revision if it is used to:

- claim that executable tests, fixtures, coverage, or substantive CI exist;
- activate the package or local descriptor;
- infer public safety from `sensitivity_floor: public`;
- treat the current path as canonical or assign an unsupported compatibility class;
- collapse KSHS surfaces, record classes, or derivatives into one identity or source role;
- justify live-network default tests, credential storage, bulk payload commits, or sensitive-record fixtures;
- create package-local schema, policy, source-registry, release, proof, receipt, or fixture authority;
- bypass rights, privacy, sensitivity, cultural/CARE, descriptor, activation, evidence, review, release, correction, or rollback gates.

Before merge, close the draft change and abandon its scoped branch. After merge, create a transparent revert of the documentation commit; do not rewrite shared history. The baseline target blob is `c44d6abbc84e8870c25a242d417c3c6f30fdaf09` at base commit `40deb4a3cab0972f0c7d38930e30c3b497408b0a`.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Final connector, package, import, source-ID, and test path | **CONFLICTED / NEEDS VERIFICATION** | Accepted ADR or explicit migration plan with old-to-new mapping, callers, deprecation, and rollback. |
| Exact compatibility class of `connectors/kansas_state_archives/` | **CONFLICTED** | Path history plus accepted `legacy`, `mirror`, `deprecated`, or `transitional` decision. |
| KSHS umbrella versus per-surface adapter strategy | **NEEDS VERIFICATION** | Accepted architecture/source decision and per-surface descriptor plan. |
| Complete recursive package and test inventory | **UNKNOWN** | Commit-pinned recursive tree and indexed/unindexed file review. |
| Build, install, runner, dependency, and command contract | **UNKNOWN** | Complete `pyproject.toml` or accepted package metadata plus clean install/import/test logs. |
| Per-surface descriptors and activation | **NOT ESTABLISHED** | Registry records, reviews, source heads, and explicit activation decisions. |
| Current source access and terms | **UNKNOWN** | Source-steward review of APIs/exports/IIIF/OAI-PMH/manual access, terms, cadence, and correction behavior. |
| Rights, privacy, sensitivity, cultural/CARE, and precise-location policy | **NEEDS VERIFICATION** | Reviewed policy, synthetic fixtures, executable tests, and review records. |
| Fixture home and fixture receipts/generation notes | **NEEDS VERIFICATION** | Accepted lane choice, payload inventory, rights/sensitivity review, and consuming tests. |
| RAW/QUARANTINE candidate-envelope contract | **NEEDS VERIFICATION** | Accepted contract/schema, validator, fixtures, and tests. |
| Import and no-network safety | **UNKNOWN** | Executable tests with egress blocking and side-effect detection. |
| Surface and derivative identity preservation | **UNKNOWN** | Executable positive/negative fixtures and assertions. |
| CI discovery and substantive pass status | **UNKNOWN** | Workflow steps that invoke an accepted runner plus logs showing collected tests and results. |
| Legacy flat catalog-stub supersession | **NEEDS VERIFICATION** | Documentation migration, backlink inventory, correction/deprecation record, and rollback. |
| Path-specific owners | **UNKNOWN** | Accepted CODEOWNERS or steward assignment. |

[Back to top](#top)
