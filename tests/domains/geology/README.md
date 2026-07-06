<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-readme
title: Geology Domain Tests README
type: test-readme
version: v0.1
status: draft; stub-expanded; domain-test-index; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — QA steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; geology; no-network; deny-by-default; cite-or-abstain; release-gated
tags: [kfm, tests, geology, natural-resources, evidence, policy, source-role, catalog-closure, public-safe-geometry, well-rights, FocusMode, EvidenceBundle, PolicyDecision, ReleaseManifest]
related:
  - ../../README.md
  - ../../../fixtures/domains/geology/README.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../docs/focus-mode/state/payload-state.md
  - ../../../contracts/domains/geology/
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../data/catalog/domain/geology/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This file replaces the prior greenfield stub at tests/domains/geology/README.md."
  - "This is a domain-test index and boundary README only. It does not define schemas, contracts, policy rules, source descriptors, fixtures, evidence bundles, receipts, proofs, release decisions, production code, or published artifacts."
  - "The default Geology test posture is deterministic, no-network, synthetic/public-safe fixtures only, and fail-closed for missing evidence, source role, policy, review, release, or rights context."
  - "README-backed child lanes currently documented in this session include catalog closure, evidence before AI, public-safe geometry, source-role anti-collapse, and well-rights. Actual test modules, runners, fixtures, CI wiring, and pass rates remain NEEDS VERIFICATION."
  - "Rollback target for this replacement is previous stub blob SHA 1942e419bb84a7de7b8834cfe8b7a93747777849."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology domain tests

> Governed, deterministic, no-network test documentation for the KFM Geology and Natural Resources domain lane. These tests should prove that geology evidence, source roles, sensitive geometry, catalog closure, governed AI boundaries, well-rights boundaries, review state, release state, correction paths, and rollback targets remain enforceable.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology%2Fnatural__resources-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-success">
  <img alt="Exposure: deny by default" src="https://img.shields.io/badge/exposure-deny__by__default-success">
</p>

**Path:** `tests/domains/geology/README.md`  
**Status:** draft / stub-expanded / domain-test-index / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `geology`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a greenfield stub before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED KFM doctrine places domain-specific tests under `tests/domains/<domain>/` · CONFIRMED Geology doctrine requires evidence discipline, source-role anti-collapse, deny-by-default exact subsurface/private-well exposure, and governed promotion · NEEDS VERIFICATION for actual test modules, fixtures, runner configuration, imports, CI coverage, receipt emission, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Directory basis](#directory-basis) · [Geology invariants under test](#geology-invariants-under-test) · [README-backed test lanes](#readme-backed-test-lanes) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/geology/` is the domain-specific test home for Geology and Natural Resources enforceability checks.

Its job is to prove that geology-facing behavior does not bypass the KFM trust spine:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A passing geology test suite should demonstrate that controlled, synthetic inputs can move through validation, evidence resolution, policy decision, catalog/proof closure, release decision, governed API/UI payloads, correction, and rollback without crossing forbidden boundaries.

A passing suite should **not** mean that any real geology claim is true, released, public, policy-admitted, or complete. It should mean only that the tested invariant behaved as expected against bounded fixtures.

---

## Directory basis

`tests/` is the canonical root for enforceability proof. `geology` is a domain segment inside that root, not a repo-root domain folder.

| Responsibility | Correct home | This README's relationship |
|---|---|---|
| Geology domain tests | `tests/domains/geology/` | This directory. |
| Geology fixtures | `fixtures/domains/geology/` | Preferred source for deterministic toy inputs and expected outputs. |
| Geology doctrine | `docs/domains/geology/` | Referenced for domain scope and governance posture. |
| Geology semantic contracts | `contracts/domains/geology/` | Referenced by tests, not redefined here. |
| Geology schemas | `schemas/contracts/v1/domains/geology/` or accepted ADR alternative | Referenced by tests, not duplicated here. |
| Geology policy | `policy/domains/geology/`, `policy/sensitivity/geology/`, or accepted ADR alternative | Referenced by tests, not bypassed here. |
| Source registry | `data/registry/sources/geology/` | Source identity, source role, rights, cadence, caveats, and activation state. |
| Catalog records | `data/catalog/domain/geology/` | Catalog system under test, not duplicated here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Expected references; tests do not own trust objects. |
| Release decisions | `release/` | Promotion authority; tests cannot replace it. |

---

## Geology invariants under test

Geology is a high-risk lane because maps, logs, well records, mineral/resource context, and AI summaries can look more authoritative than they are. The domain test suite should keep these invariants visible:

| Invariant | Required behavior | Failure posture |
|---|---|---|
| Evidence before claim | Every claim-bearing public surface resolves `EvidenceRef -> EvidenceBundle` or produces a finite non-answer. | `ABSTAIN` / validation failure. |
| Source-role anti-collapse | Occurrence, deposit, estimate, permit, production, reserve, model, observation, administrative, aggregate, candidate, synthetic, and AI text remain distinct. | `DENY`, `ABSTAIN`, or test failure. |
| Public-safe geometry | Exact/internal borehole, well-log, private-well, sample, mineral/resource, extraction, reclamation, or sensitive subsurface geometry does not publish by default. | `DENY` / `RESTRICT`. |
| Catalog closure | Catalog records bind source, evidence, schema, policy, projection, release, correction, and rollback context before promotion. | closure failure. |
| AI is downstream | Governed AI can interpret released evidence but cannot create root truth, citations, policy clearance, or release authority. | `ABSTAIN` / `ERROR`. |
| Well-rights boundary | Geology well/borehole evidence does not become water-right law, parcel/title ownership, hydrology authority, or public exact private-well exposure. | `DENY`, `RESTRICT`, or `ABSTAIN`. |
| Lifecycle discipline | Public carriers never read `RAW`, `WORK`, `QUARANTINE`, unpublished candidates, canonical/internal stores, or direct model outputs. | test failure. |
| Release discipline | Public output requires review, policy, proof/receipt, release state, correction path, and rollback target where material. | promotion-blocking failure. |

---

## README-backed test lanes

The following child lanes are documented as test lanes. Their README files may exist before executable test modules do; module presence, import paths, CI wiring, and pass rates remain NEEDS VERIFICATION until inspected.

| Lane | Path | Primary invariant |
|---|---|---|
| Catalog closure | `tests/domains/geology/test_catalog_closure/` | Catalog records must close over source, evidence, policy, projection, release, correction, and rollback context. |
| Evidence before AI | `tests/domains/geology/test_evidence_before_ai/` | AI-facing outputs cannot answer before evidence, policy, review, release, and citation closure. |
| Public-safe geometry | `tests/domains/geology/test_public_safe_geometry/` | Exact/internal sensitive geology geometry cannot reach public carriers without public-safe transform and release controls. |
| Source-role anti-collapse | `tests/domains/geology/test_source_role_anti_collapse/` | Geology source roles and claim classes cannot collapse into stronger or different authority. |
| Well-rights boundary | `tests/domains/geology/well-rights/` | Well/borehole evidence, source rights, owner privacy, hydrology groundwater claims, and people/land ownership claims remain separate. |

Future lanes should be added here only after their directory placement and responsibility boundary are checked against Directory Rules and current repo evidence.

---

## Expected test scope

Tests under this directory may validate:

- schema and contract conformance for geology object families;
- source-role presence, preservation, and anti-collapse behavior;
- evidence resolution and finite non-answer behavior;
- sensitivity, rights, geometry, and policy decisions;
- catalog closure and projection consistency;
- public-safe geometry transforms and leakage prevention;
- well/borehole owner-privacy and source-rights boundaries;
- governed AI and Focus Mode answer gates;
- release/correction/rollback linkage;
- no-network fixture-driven behavior.

Tests should be small first and end-to-end only where needed to prove trust-spine behavior.

---

## Fixture posture

Default fixture rule: use `fixtures/domains/geology/` or clearly scoped test-local fixtures only when root fixture material is not appropriate.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit evidence/source/policy/release state where relevant;
- no real exact borehole, private-well, mineral, resource, owner, parcel, production, extraction, reclamation, infrastructure-sensitive, archaeological, or other sensitive location detail;
- no credentials, live source exports, or live model/provider calls.

When fixture behavior touches hydrology, people/land, source rights, or policy, the fixture must make the owning boundary explicit rather than silently importing another lane's authority.

---

## Assertions

A useful geology test should prove one of two things clearly:

### Positive path

- the input is synthetic/public-safe;
- required source role, claim class, evidence, policy, review, release, and rollback context are present;
- geometry is public-safe or intentionally withheld;
- output preserves domain boundaries and cites evidence;
- receipt-ready metadata can explain what was checked.

### Negative path

- missing evidence returns `ABSTAIN`, not a guessed claim;
- missing policy, source rights, or sensitivity posture fails closed;
- source-role or claim-class collapse is denied;
- exact sensitive geometry does not reach public output;
- unreleased or candidate material does not cross the trust membrane;
- AI text, map tiles, graph edges, catalog summaries, or generalized geometry do not become sovereign truth;
- cross-lane ownership is not overwritten.

---

## Forbidden shortcuts

Do not use `tests/domains/geology/` to:

- store production code;
- store real exact sensitive geology/resource/well geometry;
- store real owner, parcel, title, water-right, or proprietary well-log records;
- fetch live upstream source systems in the default suite;
- store credentials or tokens;
- create a second schema, contract, policy, source-registry, receipt, proof, release, fixture, or publication authority;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass policy or sensitivity checks with a fixture flag;
- publish, promote, or release anything;
- treat AI text, MapLibre layers, vector tiles, screenshots, graph edges, generalized geometry, or README text as root truth.

---

## Suggested layout

The exact executable modules remain NEEDS VERIFICATION. A governed parent layout should look like this:

```text
tests/domains/geology/
├── README.md
├── test_catalog_closure/
│   └── README.md
├── test_evidence_before_ai/
│   └── README.md
├── test_public_safe_geometry/
│   └── README.md
├── test_source_role_anti_collapse/
│   └── README.md
└── well-rights/
    └── README.md
```

Executable test module names should follow the repo's accepted runner/import convention once confirmed.

---

## Run posture

Default run expectation:

```bash
pytest tests/domains/geology
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: deterministic, synthetic, no-network;
- fail closed on unresolved evidence, source-role collapse, missing policy, exact sensitive geometry exposure, owner/privacy leakage, unreleased public carrier, or AI/text-as-evidence;
- live-source or provider checks: separate gated jobs only;
- release gate: geology domain failures should block public carrier promotion or release candidate approval.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/geology/README.md` existed as a greenfield stub before this replacement. | Did not define the domain test boundary. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default tests should avoid sensitive data and live network calls. | Does not prove geology module presence, CI wiring, or pass rate. |
| `docs/domains/geology/README.md` | CONFIRMED doctrine / PROPOSED implementation | Geology scope, anti-collapse posture, evidence binding, deny-by-default exact subsurface/private-well exposure, lifecycle invariant, and public trust path. | Does not prove test implementations. |
| `fixtures/domains/geology/README.md` | CONFIRMED | Synthetic, public-safe fixture posture and child fixture lanes. | Does not prove all fixture payloads or consumers. |
| Child lane READMEs | CONFIRMED for documented README files in this session | Catalog closure, evidence-before-AI, public-safe geometry, source-role anti-collapse, and well-rights lane documentation exists or was expanded. | README presence does not prove executable tests, validators, schemas, policies, or CI. |
| Cross-domain source-role, Focus Mode payload, boreholes/wells, hydrology boundary docs | CONFIRMED doctrine / PROPOSED implementation | Provide governing boundaries for geology test lanes. | Do not prove runtime enforcement. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this directory or its child lanes.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for the documented positive and negative geology cases.
- [ ] Geology schema, contract, policy, source-registry, evidence, receipt, proof, and release paths are accepted and not duplicated.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision behavior is available to tests or safely stubbed.
- [ ] Public-safe geometry transform and receipt expectations are defined before enforcing them.
- [ ] Source-role anti-collapse expectations are tied to accepted source-role vocabulary.
- [ ] Hydrology and people/land boundary expectations are tied to accepted contracts before enforcing cross-lane assertions.
- [ ] CI runs the no-network geology domain suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this directory becomes a production implementation root, lifecycle data store, fixture authority, source registry, schema authority, contract authority, policy authority, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous stub blob SHA `1942e419bb84a7de7b8834cfe8b7a93747777849`.

<p align="right"><a href="#top">Back to top</a></p>
