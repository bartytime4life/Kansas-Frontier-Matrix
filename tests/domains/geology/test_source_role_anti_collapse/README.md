<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-test-source-role-anti-collapse-readme
title: Geology Source-Role Anti-Collapse Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; geology; source-role; anti-collapse; no-network; cite-or-abstain; release-gated
tags: [kfm, tests, geology, source-role, anti-collapse, occurrence, deposit, estimate, permit, production, reserve, SourceDescriptor, EvidenceBundle, PolicyDecision, DENY, ABSTAIN]
related:
  - ../../../../tests/README.md
  - ../../../../fixtures/domains/geology/README.md
  - ../../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../contracts/domains/geology/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../policy/domains/geology/
  - ../../../../data/registry/sources/geology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This file replaces a blank placeholder at tests/domains/geology/test_source_role_anti_collapse/README.md."
  - "This is a test-lane README only. It does not define source-role doctrine, SourceDescriptor schemas, policy rules, semantic contracts, evidence bundles, receipts, release decisions, or published artifacts."
  - "The tested invariant is that Geology source roles and claim classes must not collapse: Occurrence, Deposit, Estimate, Permit, Production, Reserve, model, observation, interpretation, administrative, aggregate, candidate, and synthetic records are not interchangeable."
  - "The default posture is deterministic and no-network. Live source checks, credentials, and real source exports do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology source-role anti-collapse tests

> Deterministic, no-network test documentation for proving that Geology and Natural Resources records preserve source role and claim-class boundaries before catalog, release, API, map, Evidence Drawer, Focus Mode, or AI surfaces can use them.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology%2Fnatural__resources-brown">
  <img alt="Invariant: source role anti collapse" src="https://img.shields.io/badge/invariant-source__role__anti__collapse-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Outcome: fail closed" src="https://img.shields.io/badge/outcome-fail__closed-success">
</p>

**Path:** `tests/domains/geology/test_source_role_anti_collapse/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `geology`  
**Test lane:** `test_source_role_anti_collapse`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED KFM cross-domain doctrine treats source role as a first-class identity attribute fixed at admission · CONFIRMED Geology domain doctrine requires `Occurrence`, `Deposit`, `Estimate`, `Permit`, `Production`, and `Reserve` claims to remain distinct · NEEDS VERIFICATION for actual test modules, fixtures, source descriptors, validators, policy engine wiring, CI coverage, receipt emission, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/geology/test_source_role_anti_collapse/` is the intended home for tests that prove Geology source-role and claim-class distinctions survive admission, transformation, cataloging, release preparation, governed API shaping, map display, Evidence Drawer use, Focus Mode, and AI interpretation.

This lane should test that a Geology record cannot be promoted, published, joined, summarized, rendered, or answered as a stronger or different kind of claim than its evidence and source role support.

A passing test here should **not** mean that a source record is true, complete, released, or authoritative. It should mean only that anti-collapse guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Geology appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Source-role anti-collapse tests | `tests/domains/geology/test_source_role_anti_collapse/` | This directory. |
| Synthetic source-role fixtures | `fixtures/domains/geology/source_role/` if present, otherwise `fixtures/domains/geology/` | Preferred toy inputs and expected outcomes. |
| Cross-domain source-role doctrine | `docs/architecture/cross-domain/source-role-anti-collapse.md` | Referenced doctrine, not redefined here. |
| Geology domain doctrine | `docs/domains/geology/` | Domain-specific occurrence/deposit/estimate/permit/production/reserve anti-collapse boundary. |
| Source descriptors and source registry | `data/registry/sources/geology/` | Source identity, role, rights, cadence, caveats, and activation state. |
| Semantic contracts | `contracts/domains/geology/` | Object meaning and claim-class distinctions. |
| Machine shape | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/sources/` if accepted | Referenced by tests, not duplicated here. |
| Policy decisions | `policy/domains/geology/`, `policy/sources/` if accepted | Referenced by tests, not bypassed here. |
| Receipts, proofs, release | `data/receipts/`, `data/proofs/`, `release/` | Expected references; tests cannot replace them. |

---

## Invariant under test

> **Source role does not collapse.** Admission, promotion, aggregation, interpretation, public display, and AI wording must preserve the source role and claim class. Publication state does not upgrade a source role.

For Geology, the high-risk collapse set includes:

| Distinction | Must remain separate because... | Unsafe collapse example |
|---|---|---|
| `Occurrence` vs `Deposit` | Presence is not a delineated or economically meaningful deposit. | A reported mineral occurrence is displayed as a deposit body. |
| `Deposit` vs `Estimate` | A physical deposit is not a quantity/classification estimate. | A deposit polygon is described as proven reserve without estimate evidence. |
| `Estimate` vs `Reserve` | Modeled/compiled quantity is not legal/economic reserve status by itself. | A resource estimate is summarized as a reserve. |
| `Permit` vs `ExtractionSite` | Administrative permission is not physical extraction evidence. | A permit record becomes an active mine/quarry/well site. |
| `Production` vs `Occurrence` | Production/accounting records do not prove all physical geology details. | Production history is used as proof of current deposit extent. |
| `Reclamation` vs `Closure` | Reclamation status is not the same as absence of hazard, resource, or disturbance. | Reclaimed site is treated as non-sensitive/public-safe without policy review. |
| `Modeled` vs `Observed` | Interpretive or modeled products carry assumptions and uncertainty. | A model output is queried as direct observation. |
| `Aggregate` vs `Per-place` | Aggregates lose individual-place fidelity. | County-level resource summary is used as a precise local claim. |
| `Administrative` vs `Physical geology` | Agency records support administration, not necessarily geology truth. | Lease/title/permit data becomes physical deposit evidence. |
| `Synthetic` or `AI text` vs `Evidence` | Generated content is interpretive, not root truth. | AI summary becomes citation or evidence for a geology claim. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- source-role presence on admitted or fixture SourceDescriptor-like records;
- preservation of `source_role` through transform output, catalog record, runtime envelope, or release-candidate payload;
- failure when `source_role` is dropped, rewritten, upgraded, or inferred from publication state;
- failure when a permit, lease, title, production record, or reserve estimate is used as direct physical-geology proof;
- failure when occurrence, deposit, estimate, production, reserve, extraction, reclamation, model, aggregate, candidate, synthetic, and AI-text records are treated as interchangeable;
- finite outcomes at public surfaces when source role does not support the requested claim;
- clear role badges or reader-facing role metadata in public-ready payloads where applicable;
- receipt-ready metadata for role-preservation and collapse-denial decisions.

Live source systems and real exports are out of scope for the default suite.

---

## Fixture posture

Use fixture material from `fixtures/domains/geology/` when possible.

Fixture requirements:

- synthetic and public-safe;
- no live source calls;
- no real source exports;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source role;
- explicit claim class;
- explicit evidence-resolution state where a claim is tested;
- explicit policy/release state where public exposure is tested;
- no exact sensitive geometry or real resource-location detail.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid occurrence claim | `fixtures/domains/geology/source_role/` or `valid/` | Occurrence remains occurrence; not deposit. |
| Deposit with no estimate | `fixtures/domains/geology/source_role/` | Deposit cannot imply reserve or quantity estimate. |
| Administrative permit | `fixtures/domains/geology/source_role/` | Permit cannot imply physical extraction or deposit proof. |
| Production summary | `fixtures/domains/geology/source_role/` | Production remains administrative/accounting context. |
| Modeled layer | `fixtures/domains/geology/source_role/` | Model cannot be labeled observed. |
| Aggregate summary | `fixtures/domains/geology/source_role/` | Aggregate cannot satisfy per-place claim. |
| Candidate record | `fixtures/domains/geology/invalid/` | Candidate cannot appear on public surface. |
| AI-generated summary | `fixtures/domains/geology/invalid/` | AI text cannot become evidence. |

---

## Assertions

A good source-role anti-collapse test should make both the claimed role and the forbidden upgrade obvious.

### Positive path

- `source_role` is present and from the accepted source-role vocabulary.
- claim class is explicit and separate from source role.
- object family is explicit: occurrence, deposit, estimate, permit, production, reserve, extraction, reclamation, model, aggregate, candidate, synthetic, or other accepted class.
- transforms and joins preserve source role and claim class.
- catalog/API/UI/AI payloads expose or carry role metadata where material.
- release-linked outputs preserve role distribution and do not imply stronger claims.

### Negative path

- missing `source_role` fails closed.
- `candidate` records cannot cross the public trust membrane.
- `modeled` output cannot be labeled `observed`.
- `aggregate` output cannot satisfy a per-place claim.
- `administrative` source cannot become physical geology proof by wording.
- `synthetic` or AI text cannot become evidence.
- `permit`, `production`, `reserve`, `estimate`, `deposit`, and `occurrence` cannot substitute for each other.
- publication state does not upgrade role.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Role and claim class are present, supported, evidence-bound, and policy/release-admitted | allow downstream carrier / answer only with citations. |
| Source role missing | validation failure / `ABSTAIN`. |
| Source role dropped during transform or DTO shaping | validation failure. |
| Source role rewritten without correction event and re-promotion | validation failure / `DENY`. |
| Candidate record requested for public exposure | `DENY`. |
| Modeled, aggregate, administrative, synthetic, or AI content queried as observed evidence | `ABSTAIN` or `DENY`. |
| Claim class unsupported by source role | `ABSTAIN`, `DENY`, or `RESTRICT`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real source exports;
- redefine source-role doctrine;
- create a parallel SourceDescriptor schema, policy bundle, contract, source registry, receipt, proof, or release decision;
- bypass source-role checks with a fixture flag;
- infer role from file path, source name, publication state, map layer name, or AI wording;
- treat permit, lease, title, production, reserve, estimate, occurrence, deposit, model, aggregate, candidate, synthetic, or AI-text records as interchangeable;
- publish, promote, or release anything.

Any test that requires real source data belongs in a gated integration tier with quarantine, source admission, policy, receipts, and rollback controls.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/geology/test_source_role_anti_collapse/
├── README.md
├── test_source_role_required.py            # missing role fails closed
├── test_role_preserved_through_payload.py  # transform/catalog/API/AI payload preserves role
├── test_occurrence_deposit_estimate.py     # occurrence/deposit/estimate/reserve boundaries
├── test_admin_records_not_physical_proof.py # permit/production/title/lease anti-collapse
└── test_ai_text_not_evidence.py            # generated summaries cannot create evidence or role upgrade
```

Keep helpers local only when they are test-specific. Shared source-role, policy, source-registry, evidence, runtime-envelope, or release behavior belongs under its accepted implementation root, not duplicated here.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/geology/test_source_role_anti_collapse
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that the test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing source role, role rewrite, role drop, unsupported claim class, candidate public exposure, or AI-text-as-evidence;
- live-source checks: separate gated job only;
- release gate: anti-collapse failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/geology/test_source_role_anti_collapse/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default suite should avoid sensitive data and live network calls. | Does not prove this lane's modules or pass rate. |
| `docs/architecture/cross-domain/source-role-anti-collapse.md` | CONFIRMED doctrine / PROPOSED implementation | Source role is first-class, fixed at admission, preserved through promotion, and fail-closed when roles are conflated. | Notes implementation surfaces and path placement are PROPOSED / NEEDS VERIFICATION. |
| `docs/domains/geology/README.md` | CONFIRMED doctrine / PROPOSED implementation | Geology's first job is anti-collapse: keep occurrence, deposit, estimate, permit, production, and reserve claims distinct. | Does not prove test modules, validators, or policy enforcement. |
| `contracts/domains/geology/README.md` | CONFIRMED | Geology semantic contracts keep object-family meaning separate from tests, schemas, policies, fixtures, source registry, lifecycle data, release, maps, APIs, and AI surfaces. | Does not settle all naming drift or runtime behavior. |
| `fixtures/domains/geology/README.md` | CONFIRMED | Synthetic, public-safe fixture posture and source-role child fixture lane. | Does not prove all fixture payloads or consumers. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for missing role, valid occurrence, occurrence/deposit mismatch, deposit/estimate/reserve mismatch, permit/extraction mismatch, production/physical-proof mismatch, model/observed mismatch, aggregate/per-place mismatch, candidate public exposure, and AI-text-as-evidence rejection.
- [ ] SourceDescriptor/source-role schema path is accepted.
- [ ] Source-role policy behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] Public payload role metadata expectations are defined before enforcing UI/API assertions.
- [ ] Receipt-ready role-preservation metadata expectations are defined before enforcing them.
- [ ] CI runs the no-network source-role anti-collapse suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source registry, SourceDescriptor schema home, policy authority, contract authority, fixture root, lifecycle data store, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
