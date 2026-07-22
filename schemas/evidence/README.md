# `schemas/evidence/` — Evidence Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-evidence-readme
title: schemas/evidence/ README
type: readme; compatibility-index; schema-boundary; migration-guardrail
version: v0.2
status: draft; root-level-evidence-compatibility-path; non-authoritative; CONFLICTED; NEEDS VERIFICATION before retirement
updated: 2026-07-22
policy_label: public
tags: [kfm, schemas, evidence, compatibility, migration, spec-normalization, no-parallel-authority]
related:
  - ../README.md
  - ../contracts/v1/evidence/README.md
  - ../contracts/v1/evidence/spec_normalization.md
  - ../../contracts/evidence/README.md
  - ../../policy/evidence/README.md
  - ../../fixtures/contracts/v1/evidence/README.md
  - ../../.github/workflows/contracts-validate.yml
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/validator-suite.yml
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
notes:
  - "This README is a compatibility and migration guardrail; it is not the canonical v1 evidence schema-family index."
  - "Current machine-checkable evidence schemas and the richer evidence-family normalization note are under schemas/contracts/v1/evidence/."
  - "The directly verified local spec_normalization.md remains a PROPOSED scaffold and must not evolve as a parallel authority."
  - "No schema, contract, fixture, validator, policy, release state, evidence record, proof, receipt, or publication behavior is changed by this README."
[/KFM_META_BLOCK_V2] -->

`schemas/evidence/` preserves a legacy root-level reference without allowing it to become a second evidence schema authority.

**Path:** `schemas/evidence/README.md`  
**Audience:** schema, evidence, contract, validation, policy, release, and documentation maintainers  
**Authority posture:** compatibility and migration guidance only  
**Canonical v1 family:** [`schemas/contracts/v1/evidence/`](../contracts/v1/evidence/README.md)  
**Truth posture:** CONFIRMED target and adjacent files at the reviewed repository snapshot; CONFLICTED duplicate normalization-note placement; NEEDS VERIFICATION for retirement ownership, migration state, and downstream references.

> [!IMPORTANT]
> Do not add new canonical evidence schemas here. The repository's schema root, Directory Rules, and schema-home decision record route versioned evidence machine shape to `schemas/contracts/v1/evidence/`. An object validating against a schema is not thereby true, admissible, reviewed, released, or safe to publish.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Repository fit](#authority-and-repository-fit) · [Inventory](#directly-verified-inventory) · [Routing](#canonical-routing) · [Boundaries](#responsibility-boundaries) · [Normalization](#spec-normalization-compatibility) · [Validation](#validation-tests-and-ci) · [Maintenance](#maintenance-and-change-rules) · [Retirement](#migration-and-retirement-gates) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#correction-and-rollback)

## Status and evidence boundary

| Surface | Current repository evidence | Safe conclusion |
|---|---|---|
| `schemas/evidence/README.md` | CONFIRMED existing compatibility README | This path can explain routing and guard against duplicate authority. |
| `schemas/evidence/spec_normalization.md` | CONFIRMED short `PROPOSED` scaffold sourced from domain identity-model documents | It is lineage and planning context, not an accepted normalization profile or executable implementation. |
| `schemas/contracts/v1/evidence/README.md` | CONFIRMED evidence schema-family index | This is the active v1 family index for evidence machine shape. |
| `schemas/contracts/v1/evidence/spec_normalization.md` | CONFIRMED richer `PROPOSED`, conflict-aware family note | New normalization guidance belongs with the versioned evidence family, subject to steward review and accepted ADRs. |
| EvidenceRef and EvidenceBundle schemas | CONFIRMED fielded JSON Schema 2020-12 documents with `x-kfm.status: PROPOSED` | Bounded machine shape exists; acceptance, resolution, policy, release, and production enforcement remain separate. |
| EvidenceBundle naming | CONFIRMED underscore and hyphen variants with materially different shapes | Canonical filename/profile remains CONFLICTED and must not be silently normalized. |
| Fixtures and validators | CONFIRMED valid/invalid fixture families and dedicated shape-validator wrappers for EvidenceRef and EvidenceBundle | Shape testing exists for a bounded slice; evidence resolution and claim closure are not proven. |
| Schema CI | CONFIRMED read-only `schema-validation` workflow definition | Pull requests run repository-owned schema and contract checks; a green check proves only its tested shape boundary. |
| Retirement of this lane | No accepted retirement record or completed migration was established in the bounded inspection | Keep the guardrail until references, ownership, compatibility needs, and rollback are verified. |

### Truth labels used here

- **CONFIRMED** — directly verified from the pinned repository snapshot used for this revision.
- **PROPOSED** — documented design or future state not established as accepted implementation.
- **CONFLICTED** — inspected paths or representations disagree and must not be collapsed silently.
- **UNKNOWN** — available evidence is insufficient for a current-state claim.
- **NEEDS VERIFICATION** — a specific repository, steward, migration, validator, or runtime check remains open.

## Purpose

This directory has one safe purpose: preserve and explain a root-level evidence-schema reference while KFM converges on one versioned machine-shape authority.

Use this README to:

- direct maintainers and older references to the active v1 evidence schema family;
- stop new schema or normalization work from landing in a parallel root-level topic lane;
- keep the legacy `spec_normalization.md` scaffold visible as lineage without promoting it;
- record the checks required before this compatibility path can be migrated, frozen, redirected, or retired;
- preserve the separation among evidence meaning, machine shape, policy, fixtures, validators, lifecycle records, proofs, receipts, and release decisions.

This README does not define evidence object semantics or schema fields. It does not resolve an EvidenceRef, close an EvidenceBundle, validate a citation, decide policy, emit a receipt, approve a release, or publish an artifact.

## Authority and repository fit

Directory Rules assign machine-checkable shape to `schemas/`. The schema root README separates that responsibility from contract meaning, policy, fixtures, validator implementation, lifecycle data, and release authority. The repository's proposed ADR-0001 further identifies `schemas/contracts/v1/<family>/` as the default versioned schema home and warns against permanent `schemas/<topic>/` subtrees.

The resulting placement posture is:

| Path | Responsibility | Status |
|---|---|---|
| `schemas/evidence/` | Root-level compatibility, lineage, and migration guardrail | CONFIRMED path / non-authoritative / retirement NEEDS VERIFICATION |
| `schemas/contracts/v1/evidence/` | Versioned evidence machine-shape family | CONFIRMED active repository lane / schema objects remain individually maturity-labeled |
| `contracts/evidence/` | EvidenceRef, EvidenceBundle, citation-report, and evidence-payload meaning | CONFIRMED semantic-contract lane |
| `policy/evidence/` | Evidence admissibility, rights, sensitivity, and finite decision posture | CONFIRMED policy-documentation lane / executable policy maturity separately bounded |
| `fixtures/contracts/v1/evidence/` | Deterministic valid and invalid schema inputs | CONFIRMED bounded fixture lane |
| `tools/validators/` | Executable validator implementation | CONFIRMED dedicated wrappers for the inspected EvidenceRef and EvidenceBundle slice |
| `tests/schemas/` and `tests/contracts/` | Enforceability checks for configured schema/contract behavior | CONFIRMED repository-owned test lanes |
| `data/`, `data/proofs/`, and `data/receipts/` | Lifecycle records, governed proof support, and process memory | Separate authorities; not schema homes |
| `release/` | Release, correction, withdrawal, and rollback decisions | Separate authority; schema validity is not publication permission |

> [!CAUTION]
> ADR-0001 is still marked `proposed`. This README follows the current Directory Rules, schema-root routing, and repository convention without claiming the ADR has been accepted. Any authority-changing migration or retirement must preserve that distinction.

## Directly verified inventory

The bounded inspection directly verified these files in or immediately governing this lane. It is not a recursive tree manifest.

| Path | Role | Current posture |
|---|---|---|
| [`README.md`](README.md) | This compatibility and migration guardrail | CONFIRMED |
| [`spec_normalization.md`](spec_normalization.md) | Legacy root-level normalization scaffold referenced by domain identity documents | PROPOSED lineage / CONFLICTED placement |
| [`../contracts/v1/evidence/README.md`](../contracts/v1/evidence/README.md) | Canonical-routing v1 evidence schema-family index | CONFIRMED |
| [`../contracts/v1/evidence/spec_normalization.md`](../contracts/v1/evidence/spec_normalization.md) | Richer evidence-family normalization profile | PROPOSED / conflict-aware / active authoring lane |
| [`../contracts/v1/evidence/evidence_ref.schema.json`](../contracts/v1/evidence/evidence_ref.schema.json) | EvidenceRef machine shape | CONFIRMED file / `PROPOSED` schema status |
| [`../contracts/v1/evidence/evidence_bundle.schema.json`](../contracts/v1/evidence/evidence_bundle.schema.json) | Strict EvidenceBundle machine shape used by the inspected validator/fixture slice | CONFIRMED file / `PROPOSED` schema status |
| [`../contracts/v1/evidence/evidence-bundle.schema.json`](../contracts/v1/evidence/evidence-bundle.schema.json) | Permissive hyphenated scaffold | CONFIRMED file / duplicate-authority risk |
| [`../contracts/v1/evidence/evidence-bundle.json`](../contracts/v1/evidence/evidence-bundle.json) | Placeholder adjacent JSON record | CONFIRMED file / purpose NEEDS VERIFICATION |

Absence of another file is not asserted from this bounded inventory. Use a complete tree or generated schema manifest before making deletion, rename, or retirement decisions.

## Canonical routing

Use the following mapping when a document, test, tool, or maintainer reaches this lane:

| Need | Route | Do not do here |
|---|---|---|
| Evidence schema-family overview | [`schemas/contracts/v1/evidence/README.md`](../contracts/v1/evidence/README.md) | Do not create a competing family index. |
| EvidenceRef schema | [`evidence_ref.schema.json`](../contracts/v1/evidence/evidence_ref.schema.json) | Do not copy or fork the schema. |
| EvidenceBundle schema | [`evidence_bundle.schema.json`](../contracts/v1/evidence/evidence_bundle.schema.json), pending duplicate-profile resolution | Do not promote the hyphenated scaffold or invent a third profile. |
| Evidence-family normalization guidance | [`schemas/contracts/v1/evidence/spec_normalization.md`](../contracts/v1/evidence/spec_normalization.md) | Do not expand the root-level scaffold independently. |
| Evidence semantics | [`contracts/evidence/README.md`](../../contracts/evidence/README.md) | Do not encode semantic authority in a compatibility README. |
| Evidence policy | [`policy/evidence/README.md`](../../policy/evidence/README.md) | Do not turn schema constraints into allow/deny/restrict/abstain decisions. |
| Evidence fixtures | [`fixtures/contracts/v1/evidence/README.md`](../../fixtures/contracts/v1/evidence/README.md) | Do not store example instances beside schemas. |
| Validator implementation | [`tools/validators/`](../../tools/validators/) | Do not place executable validation code under `schemas/`. |
| Schema and contract tests | [`tests/schemas/`](../../tests/schemas/) and [`tests/contracts/`](../../tests/contracts/) | Do not treat documentation examples as passing tests. |
| Drift and migration tracking | [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) and [`VERIFICATION_BACKLOG.md`](../../docs/registers/VERIFICATION_BACKLOG.md) | Do not resolve authority conflicts by prose alone. |

## Responsibility boundaries

### What belongs here

- This README.
- A minimal, explicit compatibility notice while verified references still target this path.
- A migration or deprecation pointer approved by the owning schema/evidence stewards.
- Historical lineage needed to explain why the root-level path exists.

### What does not belong here

- New or revised canonical `*.schema.json`, `*.schema.yaml`, JSON-LD context, or equivalent machine-shape files.
- A second EvidenceRef, EvidenceBundle, CitationValidationReport, RedactionReceipt, EvidenceDrawerPayload, or geospatial-manifest schema family.
- Independent normalization, canonicalization, `$id`, `$ref`, `spec_hash`, or hashing rules.
- Semantic contracts, policy rules, fixtures, validator/test code, source records, EvidenceBundle instances, proof objects, receipts, catalog records, lifecycle data, release manifests, corrections, or rollback cards.
- Public API, UI, map, search, graph, export, or AI payloads.
- Claims that schema validation proves evidence truth, source authority, citation sufficiency, rights clearance, sensitivity clearance, review, release, or publication.

## Spec-normalization compatibility

The root-level [`spec_normalization.md`](spec_normalization.md) and versioned [`schemas/contracts/v1/evidence/spec_normalization.md`](../contracts/v1/evidence/spec_normalization.md) are not equivalent authorities.

| Concern | Root-level scaffold | Versioned evidence-family note |
|---|---|---|
| Placement | `schemas/evidence/spec_normalization.md` | `schemas/contracts/v1/evidence/spec_normalization.md` |
| Content depth | Short domain-inventory scaffold | Detailed, conflict-aware normalization profile |
| Status | PROPOSED lineage | PROPOSED active family note |
| Safe maintenance | Freeze except for an approved compatibility pointer or migration correction | Review substantive normalization guidance here |
| Promotion authority | None | Still requires accepted decisions, schemas, fixtures, validators, tests, and steward review |

Current conflicts that must remain visible include:

- the proposed `jcs:sha256:<hex>` grammar versus the currently referenced bare `sha256:<hex>` schema pattern;
- underscore versus hyphen EvidenceBundle filenames and materially different shapes;
- incomplete verification of canonicalization fixtures, duplicate-key rejection, transient-field rules, and runtime hash parity;
- domain documents that still cite the root-level path as a planned validator or normalization surface.

Do not copy content in both files. A substantive correction belongs in the versioned evidence-family note, followed by a separately reviewed migration or compatibility update here if downstream references require one.

## Evidence object and trust boundaries

This lane must preserve these separations:

| Object or decision | What schema validation can establish | What remains outside schema authority |
|---|---|---|
| EvidenceRef | Required fields, enum values, and closed object shape for the inspected profile | Resolution, bundle membership, current-head status, or claim closure |
| EvidenceBundle | Required top-level claim-support fields and value shapes for the inspected profile | Claim truth, citation sufficiency, rights/sensitivity permission, review, or release |
| CitationValidationReport | Shape when an accepted schema and fixtures are present | Whether the cited material actually supports the claim |
| RedactionReceipt | Shape when an accepted schema and fixtures are present | Whether the transform was policy-authorized or safe to expose |
| EvidenceDrawerPayload | Display-projection shape | Canonical evidence truth or permission to bypass governed APIs |
| Geo/layer manifest | Artifact and evidence-reference shape | EvidenceBundle, PolicyDecision, ReviewRecord, or ReleaseManifest authority |

EvidenceBundle outranks generated language, but an EvidenceBundle is still not a PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, or RollbackCard. Public clients and AI surfaces must use governed interfaces and finite outcomes; they must not read this schema lane as publication authority.

## Validation, tests, and CI

### Confirmed repository surfaces

| Surface | Confirmed bounded behavior | Does not prove |
|---|---|---|
| [`validate_evidence_ref.py`](../../tools/validators/validate_evidence_ref.py) | Delegates to the shared JSON Schema runner with the EvidenceRef schema and fixture root. | Evidence resolution or bundle closure. |
| [`validate_evidence_bundle.py`](../../tools/validators/validate_evidence_bundle.py) | Delegates to the shared runner with the strict underscore-named bundle schema and fixture root. | Claim truth, policy permission, or release readiness. |
| [`test_evidence_ref_validator.py`](../../tests/schemas/test_evidence_ref_validator.py) | Checks one valid EvidenceRef and the missing-`ref` failure path. | Exhaustive EvidenceRef behavior or runtime resolution. |
| [`test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) | Discovers evidence-family fixtures whose directory names match `*.schema.json` stems and tests valid/invalid polarity. | Non-vacuous coverage for every evidence schema or semantic closure. |
| [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) | Parses schema JSON, checks JSON Schema 2020-12 shape, requires canonical v1 `$id` uniqueness, runs configured aggregate fixtures, and executes schema/contract tests with read-only repository permission. | Meaning, evidence truth, source authority, policy, rights, sensitivity, release, or publication. |
| [`contracts-validate.yml`](../../.github/workflows/contracts-validate.yml) | Runs the repository-owned `make test` surface on pull requests with read-only repository permission. | Complete semantic equivalence, release authority, or publication. |
| [`validator-suite.yml`](../../.github/workflows/validator-suite.yml) | Runs `make schemas` and verifies that the reviewed invalid EvidenceBundle canary fails for the expected missing-`bundle_id` reason. | Exhaustive evidence validation, EvidenceBundle closure, policy, or public safety. |

### Repository-native commands

Run from the repository root after installing declared test dependencies:

```bash
python -m pip install -e ".[test]"
make schemas
python -m pytest -q tests/schemas tests/contracts
```

For the directly inspected evidence slice:

```bash
python tools/validators/validate_evidence_ref.py \
  fixtures/contracts/v1/evidence/evidence_ref/valid/valid_1.json

python tools/validators/validate_evidence_bundle.py \
  fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_1.json

python -m pytest -q \
  tests/schemas/test_evidence_ref_validator.py \
  tests/schemas/test_common_contracts.py
```

These commands validate the checked-out revision. Do not describe them as passed without a current run result.

## Maintenance and change rules

Before changing this lane:

- [ ] Pin and inspect the current base commit and target blob.
- [ ] Re-read Directory Rules, the schema-root README, ADR-0001 status, the drift register, and the versioned evidence-family index.
- [ ] Search all tracked references to `schemas/evidence/` and `schemas/evidence/spec_normalization.md`.
- [ ] Determine whether the requested edit is compatibility maintenance, migration, retirement, or an attempted new schema authority.
- [ ] Reject new canonical machine shape or substantive normalization guidance at this root-level path.
- [ ] Preserve the EvidenceBundle filename/profile conflict until a reviewed migration resolves it.
- [ ] Update contracts, schemas, fixtures, validators, tests, policy references, registries, and consumers atomically when a real schema migration requires them.
- [ ] Keep policy, rights, sensitivity, review, release, correction, and rollback separate from schema validity.
- [ ] Run repository-native schema/contract checks and inspect pull-request workflow results.
- [ ] Record correction and rollback targets; do not delete or rewrite shared history to hide the compatibility path.

## Migration and retirement gates

This directory should remain a narrow guardrail until every applicable gate is satisfied.

| Gate | Required evidence | Current status |
|---|---|---|
| Reference inventory | Complete tracked-reference inventory for this directory and its normalization scaffold | NEEDS VERIFICATION |
| Authority decision | Accepted steward/ADR decision identifying the canonical schema and normalization homes | NEEDS VERIFICATION; ADR-0001 remains proposed |
| Duplicate-profile resolution | Canonical EvidenceBundle filename, `$id`, shape, and compatibility strategy | CONFLICTED / NEEDS VERIFICATION |
| Migration record | Reviewed migration/deprecation entry with owner, scope, sunset, downstream updates, and rollback | NOT ESTABLISHED in the bounded inspection |
| Consumer updates | Contracts, schemas, fixtures, validators, tests, domain docs, registries, APIs/UI, and release references updated where applicable | NEEDS VERIFICATION |
| Validation | Schema/contract checks and any normalization/hash parity tests pass on the migration commit | NEEDS VERIFICATION |
| Compatibility decision | Explicit choice to freeze, redirect, retain, or remove the root-level path | NEEDS VERIFICATION |
| Rollback proof | Reversible restoration path and preserved lineage | NEEDS VERIFICATION |

Retirement is a repository migration, not a documentation cleanup. Do not remove this README or `spec_normalization.md` merely because the versioned lane exists.

## Definition of done

### This README revision

- [x] Identifies the lane as non-authoritative compatibility guidance.
- [x] Routes machine shape and normalization guidance to the versioned evidence family.
- [x] Preserves the root-level normalization scaffold as lineage rather than promoting it.
- [x] Documents verified schema, fixture, validator, test, and CI boundaries.
- [x] Keeps evidence truth, policy, review, release, correction, rollback, and publication separate.
- [x] Leaves unresolved migration and duplicate-profile decisions visible.

### Executable or migration maturity

- [ ] ADR/steward authority is accepted.
- [ ] EvidenceBundle profile and filename conflict is resolved.
- [ ] Normalization and `spec_hash` grammar are accepted and tested.
- [ ] All downstream references are inventoried and migrated.
- [ ] Compatibility/deprecation metadata and rollback are implemented.
- [ ] Current CI and consumer evidence support retirement or promotion.

Completing this README does not complete those executable or governance gates.

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Full recursive inventory of `schemas/evidence/` | UNKNOWN beyond directly fetched files | Complete tree or generated schema manifest at the final commit. |
| Current tracked references to the root-level lane | NEEDS VERIFICATION | Repository-wide path/reference scan. |
| Accepted owner for this compatibility path | NEEDS VERIFICATION | Stewardship assignment or reviewed ownership record. |
| ADR-0001 acceptance and implementation state | PROPOSED / NEEDS VERIFICATION | Accepted ADR status plus migration/registry evidence. |
| EvidenceBundle canonical filename and profile | CONFLICTED | Schema-steward decision and non-divergent migration. |
| Root-level `spec_normalization.md` disposition | NEEDS VERIFICATION | Freeze, redirect, migrate, or retire decision with reference inventory. |
| `spec_hash` canonical grammar and canonicalizer | CONFLICTED / NEEDS VERIFICATION | Accepted normalization/hash ADR, schemas, fixtures, validators, and parity tests. |
| Exhaustive evidence-schema fixture coverage | UNKNOWN beyond inspected EvidenceRef/EvidenceBundle families | Non-vacuous inventory and test results for each supported schema. |
| Runtime evidence resolution and policy enforcement | UNKNOWN | Accepted resolver/policy contracts, implementation, tests, and runtime evidence. |
| Required-check and branch-protection significance | UNKNOWN | Repository ruleset or branch-protection evidence. |

## Evidence ledger

Repository evidence for this revision was verified against `bartytime4life/Kansas-Frontier-Matrix@f37a8c8bb77840d1189d731d1043ad1d05ec5fc0`.

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Prior `schemas/evidence/README.md` blob `70ad8c2dc278727619dcb61b43ea693a9b6eae2a` | CONFIRMED | Existing purpose, compatibility classification, inventory baseline, and open placement questions. | Complete tree, accepted migration, or executable behavior. |
| [`schemas/README.md`](../README.md) | CONFIRMED repository root README | Shape/meaning/policy/fixture/validator/data/release separation and current CI boundary. | Acceptance of every child schema. |
| [`Directory Rules`](../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine file | Responsibility-root placement, no-parallel-authority rule, and README/migration discipline. | Acceptance of ADR-0001 or completion of this lane's migration. |
| [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | CONFIRMED file / proposed decision | Intended canonical versioned schema home and prohibition on permanent topic subtrees. | Accepted decision or completed migration. |
| [`schemas/contracts/v1/evidence/README.md`](../contracts/v1/evidence/README.md) | CONFIRMED family index | Versioned evidence-family routing and duplicate-name risk. | Production acceptance or complete coverage. |
| [`spec_normalization.md`](spec_normalization.md) | CONFIRMED root-level scaffold | Legacy path and domain-document lineage. | Accepted normalization behavior. |
| [`versioned spec_normalization.md`](../contracts/v1/evidence/spec_normalization.md) | CONFIRMED detailed family note / PROPOSED | Active conflict-aware normalization guidance and open `spec_hash` mismatch. | Runtime canonicalization or hash parity. |
| EvidenceRef and EvidenceBundle schemas | CONFIRMED files / PROPOSED status | Inspected machine shapes and schema-declared contract/fixture/validator pointers. | Resolution, closure, policy, or release. |
| [`fixtures/contracts/v1/evidence/README.md`](../../fixtures/contracts/v1/evidence/README.md) | CONFIRMED bounded inventory | EvidenceRef and EvidenceBundle valid/invalid fixture families. | Exhaustive evidence-family coverage. |
| Dedicated validators and schema tests | CONFIRMED source files | Bounded shape-validation wiring and polarity checks. | Current run result or production behavior. |
| [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) | CONFIRMED read-only workflow | Pull-request schema/fixture/test command surface and authority boundary. | A current successful run or branch-protection requirement. |
| [`contracts-validate.yml`](../../.github/workflows/contracts-validate.yml) and [`validator-suite.yml`](../../.github/workflows/validator-suite.yml) | CONFIRMED read-only workflows | Repository-owned contract/schema commands and the bounded invalid EvidenceBundle canary. | Complete evidence-family coverage, claim truth, or release authority. |
| [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) and [`VERIFICATION_BACKLOG.md`](../../docs/registers/VERIFICATION_BACKLOG.md) | CONFIRMED register files | Existing repository drift and verification surfaces. | That this compatibility-path conflict has a complete migration entry. |

## Correction and rollback

Correct this README when:

- ADR-0001 changes status or is superseded;
- the canonical evidence schema family moves or changes version;
- the root-level normalization scaffold is frozen, redirected, migrated, or retired;
- EvidenceBundle duplicate profiles are resolved;
- normalization, `spec_hash`, fixtures, validators, tests, CI, policy, resolver, or release evidence changes materially;
- any current-state statement no longer matches the repository.

Before merge, rollback means closing or abandoning the scoped review change. After merge, use a transparent revert of the documentation commit and re-run applicable documentation, schema, contract, and link checks. Do not force-push shared history or delete the compatibility lane without a separately reviewed migration.

Reverting this README changes documentation only. It does not alter schemas, contracts, fixtures, validators, tests, policy, evidence records, proofs, receipts, lifecycle data, releases, public interfaces, deployments, or publication state.
