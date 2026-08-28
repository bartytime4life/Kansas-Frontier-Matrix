<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-test-catalog-closure-readme
title: Geology Catalog Closure Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Catalog steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; geology; catalog-closure; no-network; release-gated; source-role-aware
tags: [kfm, tests, geology, catalog-closure, CATALOG, TRIPLET, STAC, DCAT, PROV, EvidenceBundle, SourceDescriptor, PolicyDecision, ReleaseManifest, CatalogBuildReceipt]
related:
  - ../../../../tests/README.md
  - ../../../../fixtures/domains/geology/README.md
  - ../../../../data/catalog/domain/geology/README.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/DATA_LIFECYCLE.md
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
  - "This file replaces a blank placeholder at tests/domains/geology/test_catalog_closure/README.md."
  - "This is a test-lane README only. It does not define catalog schemas, source descriptors, policy rules, proof objects, receipts, release decisions, or published artifacts."
  - "The default posture is deterministic and no-network. Live source checks, real source exports, credentials, or exact sensitive geology/resource locations do not belong in this test lane."
  - "Catalog closure means agreement across catalog records, evidence/source references, policy/review/release state, and any emitted STAC/DCAT/PROV/triplet projections; it is not mere file presence."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology catalog closure tests

> Deterministic, no-network test documentation for proving that Geology and Natural Resources catalog records are closed enough to support review, release preparation, correction, and rollback without becoming public truth by accident.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology%2Fnatural__resources-brown">
  <img alt="Test lane: catalog closure" src="https://img.shields.io/badge/test-catalog__closure-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Exposure: no publication" src="https://img.shields.io/badge/exposure-no__publication-lightgrey">
</p>

**Path:** `tests/domains/geology/test_catalog_closure/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `geology`  
**Test lane:** `test_catalog_closure`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED KFM testing doctrine places domain-specific tests under `tests/domains/<domain>/` · CONFIRMED Geology catalog and fixture READMEs define separate catalog and fixture boundaries · NEEDS VERIFICATION for actual test modules, fixtures, schemas, validators, policy engine wiring, CI coverage, receipt emission, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [What catalog closure means](#what-catalog-closure-means) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/geology/test_catalog_closure/` is the intended home for tests that prove a Geology catalog candidate has enough governed closure to move toward review or release preparation.

This lane should test whether Geology catalog records correctly bind:

- source identity and source-role posture;
- evidence references and proof pointers;
- schema and contract expectations;
- policy and sensitivity decisions;
- catalog projection consistency;
- release references, correction paths, and rollback targets where public exposure is proposed.

A passing test here should **not** mean that a Geology record is true, public, policy-admitted, reviewed, released, or published. It should mean only that the tested catalog-closure rules behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Geology appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Domain-test documentation and checks | `tests/domains/geology/` | Parent domain test lane. |
| Catalog-closure checks | `tests/domains/geology/test_catalog_closure/` | This directory. |
| Synthetic inputs and expected outputs | `fixtures/domains/geology/` | Preferred fixture source. |
| Geology catalog records | `data/catalog/domain/geology/` | System under test; not duplicated here. |
| Semantic object meaning | `contracts/domains/geology/` | Referenced by tests, not redefined here. |
| Machine shape | `schemas/contracts/v1/domains/geology/` | Referenced by tests, not duplicated here. |
| Policy decisions | `policy/domains/geology/`, `policy/sensitivity/geology/` | Referenced by tests, not bypassed here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Expected references; not authored as test truth here. |
| Release decisions | `release/` | Public promotion authority; tests cannot replace it. |

---

## What catalog closure means

Catalog closure is a governed completeness and consistency property. For this test lane, closure means a candidate catalog record does not stand alone as a loose summary. It is tied to the required upstream and downstream trust objects.

Minimum closure dimensions:

| Dimension | Closure question | Expected failure mode |
|---|---|---|
| Identity | Does the record have a stable catalog identity and domain lane? | `ERROR` or validation failure. |
| Source | Does it point to a SourceDescriptor or equivalent registry reference? | `ABSTAIN` / fail closed. |
| Source role | Is the record clearly occurrence, deposit, estimate, permit, production, reserve, model, observation, or interpretation? | `DENY` / fail closed for ambiguous public use. |
| Evidence | Does every claim-bearing field resolve to an EvidenceRef / EvidenceBundle or approved absence reason? | `ABSTAIN`. |
| Schema | Does the record satisfy the accepted schema/profile for its catalog type? | validation failure. |
| Policy | Does sensitivity, rights, geometry exposure, and review posture resolve to a PolicyDecision? | `DENY` or `RESTRICT`. |
| Projection | Do domain catalog, STAC, DCAT, PROV, and triplet projections agree where those projections exist? | closure failure. |
| Release | If public exposure is proposed, is there release-state linkage plus correction and rollback path? | promotion-blocking failure. |
| Stale state | Are source vintage, supersession, and correction status explicit where material? | `ABSTAIN`, `STALE`, or closure failure. |

---

## Expected test scope

Tests in this lane should be small and deterministic. They may validate:

- Geology domain catalog records under `data/catalog/domain/geology/` against synthetic or fixture-backed examples.
- Agreement between Geology catalog records and STAC/DCAT/PROV/triplet projections where those files exist.
- Closure between catalog entries and SourceDescriptor records.
- Closure between catalog entries and EvidenceBundle/proof references.
- Closure between catalog entries and PolicyDecision or sensitivity posture.
- Closure between release-candidate catalog entries and ReleaseManifest, CorrectionNotice, or RollbackCard references.
- Negative outcomes for missing evidence, missing source role, ambiguous resource-claim type, unresolved sensitivity, missing review, stale source, or public exposure without release state.

Tests should prefer tiny synthetic fixtures over real source material. Real KGS, USGS, KCC, MRDS, borehole, well-log, or resource-production data belongs in the governed lifecycle and source registry, not in this test directory.

---

## Fixture posture

Use fixture material from `fixtures/domains/geology/` when possible.

Fixture requirements:

- synthetic and public-safe;
- compact enough for review in a PR;
- deterministic and no-network;
- explicit expected outcome;
- explicit source-role and sensitivity posture;
- explicit toy evidence/source/release references where the tested closure rule requires them;
- no real exact borehole, well-log, private-well, mineral, extraction, reclamation, infrastructure-sensitive, or resource-location detail.

Preferred fixture families:

| Fixture kind | Preferred lane | Example role |
|---|---|---|
| Positive closure example | `fixtures/domains/geology/valid/` or `golden/` | A toy catalog record with all required references. |
| Missing evidence example | `fixtures/domains/geology/invalid/` | Expected `ABSTAIN` or closure failure. |
| Source-role ambiguity example | `fixtures/domains/geology/source_role/` | Occurrence/deposit/estimate anti-collapse check. |
| Sensitivity example | `fixtures/domains/geology/tier-transitions/` | Expected `DENY`, `RESTRICT`, or public-safe transform requirement. |
| Map/UI closure example | `fixtures/domains/geology/map-ui/` | Downstream envelope must not bypass release state. |

---

## Assertions

A good catalog-closure test should make the expected invariant obvious.

Suggested assertion groups:

### Positive closure

- `catalog_id` is stable and domain-scoped.
- catalog record type is explicit.
- source reference resolves or is intentionally stubbed with a declared fixture record.
- evidence reference resolves or produces the expected finite non-answer.
- source role is preserved and not upgraded by prose.
- policy posture is explicit.
- projection references agree where STAC/DCAT/PROV/triplet projections are present.
- release-linked records include correction and rollback references.

### Negative closure

- missing EvidenceRef causes `ABSTAIN`, not a guessed claim.
- missing or ambiguous source role causes failure or `DENY` for public exposure.
- exact sensitive geometry without an accepted public-safe transform fails closed.
- a permit, lease, production record, or reserve estimate cannot satisfy a physical geology occurrence/deposit claim by itself.
- a catalog record under `data/catalog/domain/geology/` is not public merely because it exists.
- no test reads `data/raw`, `data/work`, or `data/quarantine` as a public truth shortcut.

---

## Forbidden shortcuts

Do not use this test lane to:

- perform live network calls;
- fetch live upstream source systems;
- store credentials or tokens;
- store real source exports;
- store exact sensitive geology/resource locations;
- redefine schemas, policies, contracts, source descriptors, receipts, proofs, or release decisions;
- bypass `EvidenceRef → EvidenceBundle` resolution;
- bypass policy with a fixture flag;
- treat generated text, AI output, map tiles, STAC/DCAT/PROV records, graph edges, or README summaries as sovereign truth;
- publish, promote, or release anything.

Any test that requires live source behavior belongs in a gated integration tier with an explicit runbook, not in the default closure suite.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/geology/test_catalog_closure/
├── README.md
├── test_domain_catalog_closure.py          # domain catalog record completeness
├── test_catalog_projection_alignment.py    # STAC/DCAT/PROV/triplet consistency where present
├── test_evidence_policy_release_links.py   # EvidenceBundle, PolicyDecision, ReleaseManifest links
└── test_catalog_closure_negative.py        # missing evidence/source-role/sensitivity/release failures
```

Keep helpers local only when they are test-specific. Shared validator behavior belongs under the accepted validator/tool root, not duplicated here.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/geology/test_catalog_closure
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that the test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on unresolved evidence, unresolved source role, missing policy, missing release reference, or sensitive public exposure;
- live-source checks: separate gated job only, never required for deterministic closure tests;
- release gate: closure failures should block promotion where catalog outputs are release candidates.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/geology/test_catalog_closure/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default suite should avoid sensitive data and live network calls. | Does not prove this lane's modules or pass rate. |
| `docs/domains/geology/README.md` | CONFIRMED doctrine / PROPOSED implementation | Geology scope, anti-collapse rules, lifecycle invariant, public trust path, and test/fixture placement. | Does not prove catalog-closure tests exist. |
| `fixtures/domains/geology/README.md` | CONFIRMED | Synthetic, public-safe fixture posture and child fixture lanes for Geology. | Does not prove all fixture payloads or consumers. |
| `data/catalog/domain/geology/README.md` | CONFIRMED | Geology catalog lane boundary, source-role requirements, sensitivity guardrails, and catalog validation checklist. | Does not prove catalog inventory, validators, or release state. |
| `contracts/domains/geology/README.md` | CONFIRMED | Semantic contracts are separate from tests, schemas, policy, fixtures, source registry, lifecycle data, release, maps, APIs, and AI surfaces. | Does not settle schema naming drift or runtime behavior. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for positive closure, missing evidence, ambiguous source role, sensitivity denial, stale state, and release linkage.
- [ ] Geology catalog schema/profile path is accepted.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision behavior is available to tests or safely stubbed.
- [ ] STAC/DCAT/PROV/triplet projection alignment rules are defined before enforcing them.
- [ ] ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing release-linked closure.
- [ ] CI runs the no-network closure suite.
- [ ] Failures block promotion where catalog artifacts are release candidates.

---

## Rollback

Rollback is required if this lane becomes a source registry, fixture root, lifecycle data store, proof store, receipt store, release-decision root, schema authority, policy authority, validator implementation root, public map/API surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
