<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-agriculture-readme
title: Agriculture Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; agriculture-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Agriculture domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; agriculture; synthetic-only; no-network; aggregate-only; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, agriculture, synthetic-fixtures, no-network, aggregate-only, SourceDescriptor, EvidenceRef, EvidenceBundle, AggregationReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/agriculture/README.md
  - ../../../e2e/agriculture/README.md
  - ../../../../fixtures/domains/agriculture/README.md
  - ../../../../fixtures/domains/agriculture/catalog/README.md
  - ../../../../fixtures/domains/agriculture/field_level_attempt/README.md
  - ../../../../fixtures/domains/agriculture/golden/README.md
  - ../../../../fixtures/domains/agriculture/hls_vi/README.md
  - ../../../../fixtures/domains/agriculture/invalid/README.md
  - ../../../../fixtures/domains/agriculture/nass_quickstats/README.md
  - ../../../../fixtures/domains/agriculture/no_network/README.md
  - ../../../../fixtures/domains/agriculture/release/README.md
  - ../../../../fixtures/domains/agriculture/soil_moisture/README.md
  - ../../../../fixtures/domains/agriculture/ssurgo/README.md
  - ../../../../fixtures/domains/agriculture/valid/README.md
  - ../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/API_CONTRACTS.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../release/candidates/agriculture/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/agriculture/README.md."
  - "This lane documents test-local expectations for Agriculture fixtures. Canonical reusable Agriculture fixtures live under fixtures/domains/agriculture/ unless an ADR or parent README says otherwise."
  - "No parent README was found at tests/fixtures/README.md or tests/fixtures/domains/README.md during authoring. This lane is self-contained until those parent indexes are authored."
  - "Executable tests, fixture payload inventory, test harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture test fixtures

> Test-lane documentation for Agriculture fixtures referenced from `tests/fixtures/domains/agriculture/`. This path describes how tests may use synthetic fixture material without turning fixture examples into source truth, catalog truth, policy approval, release approval, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: test fixtures" src="https://img.shields.io/badge/lane-test__fixtures-purple">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-green">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not truth" src="https://img.shields.io/badge/boundary-fixtures__not__truth-success">
</p>

**Path:** `tests/fixtures/domains/agriculture/README.md`  
**Status:** draft / empty placeholder replaced / Agriculture test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/agriculture`  
**Canonical reusable fixture root:** `fixtures/domains/agriculture/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED no parent README was found at `tests/fixtures/README.md` or `tests/fixtures/domains/README.md`; CONFIRMED canonical Agriculture fixture README exists under `fixtures/domains/agriculture/`; CONFIRMED Agriculture test, E2E, no-network, lifecycle, and API docs describe synthetic, no-network, aggregate-only, evidence-bound, fail-closed, and release-gated behavior; NEEDS VERIFICATION for executable tests, fixture payload inventory, fixture schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/agriculture/` is a test-local documentation lane for Agriculture fixture expectations.

This lane should explain how test code may reference, mirror, stub, or locally constrain Agriculture fixture material while preserving the authority of the canonical fixture root. It can describe test-only fixture behavior, expected fixture families, validation expectations, negative cases, no-network posture, and safe-output rules.

A fixture used from this lane should not mean that an Agriculture claim is true, a field condition is known, a source record is admitted, a catalog record is closed, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement Basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Test-local Agriculture fixture expectations | `tests/fixtures/domains/agriculture/` | This directory. |
| Reusable Agriculture fixtures | `fixtures/domains/agriculture/` | Canonical fixture root; referenced, not replaced. |
| Agriculture domain tests | `tests/domains/agriculture/` | Consumers and validators; not fixture authority. |
| Agriculture E2E tests | `tests/e2e/agriculture/` | Composed-flow consumers; not fixture authority. |
| Semantic contracts | `contracts/domains/agriculture/` | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/agriculture/` | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/agriculture/` or accepted policy roots | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a second fixture root unless a parent README or ADR explicitly allows test-local copies. Prefer references to `fixtures/domains/agriculture/` for reusable fixture payloads.

---

## Invariant Under Test

> **Agriculture fixtures are synthetic bounded examples, not Agriculture truth.** Test fixture success proves only the fixture expectation it was designed to exercise.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/agriculture/`; test-local copies require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixtures use fake identifiers, mock markers, minimized geometry, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source APIs, map services, release services, public APIs, or AI runtimes. | `ERROR`. |
| Aggregate-only boundary | Aggregate products stay aggregate and cannot become field, operator, parcel, or person-level truth. | `DENY` / `ABSTAIN`. |
| Source-role boundary | Source roles remain fixed and cannot be upcast by fixtures, validators, catalog helpers, API envelopes, or generated text. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Claim-like fixtures include EvidenceRef expectations or explicitly mark evidence as out of scope. | `ABSTAIN`. |
| Receipt boundary | Aggregation, validation, redaction, correction, withdrawal, and rollback refs are explicit where material. | validation failure. |
| Policy boundary | Rights, privacy, precision, source-license, and release blockers fail closed in negative fixtures. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected Fixture-Test Families

| Family | Purpose | Boundary |
|---|---|---|
| Valid fixture smoke checks | Prove known-good synthetic fixture envelopes satisfy expected shape. | Valid fixture is not true data. |
| Invalid fixture checks | Prove malformed or unsafe examples fail for finite reasons. | Negative examples are not production incidents. |
| No-network fixture checks | Prove fixture loading is local and deterministic. | No live connectors by default. |
| Aggregate fixture checks | Prove aggregate Agriculture examples retain aggregation posture and receipts. | Aggregate is not field truth. |
| Field-level denial checks | Prove unsafe exact or private-like requests deny or abstain. | Denial test does not store real private data. |
| Source-role checks | Prove source-role metadata is not silently changed. | Fixture labels do not confer authority. |
| Evidence and receipt checks | Prove EvidenceRef and receipt expectations are present where material. | Fixture refs are synthetic. |
| Release-shaped checks | Prove release fixtures remain release-shaped examples and do not approve publication. | Release authority remains in `release/`. |
| Cross-lane context checks | Prove Soil, Hydrology, Atmosphere, Habitat, Flora, Fauna, Geology, Hazards, and People/Land refs remain external authority. | Context is not ownership transfer. |

---

## Relationship to Canonical Agriculture Fixtures

The canonical Agriculture fixture root already documents multiple README-backed fixture lanes, including catalog-shaped, field-level-denial, golden, invalid, NASS-like, no-network, release-shaped, soil-moisture, SSURGO-like, and valid examples.

This `tests/fixtures/...` lane should therefore avoid duplicating those payloads. It should instead document how tests consume them, what local wrappers may exist, and what safety checks must run before fixture material is accepted by test code.

| Question | Preferred answer |
|---|---|
| Need a reusable fixture payload? | Put it under `fixtures/domains/agriculture/`. |
| Need a test-only wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need source data? | Do not put it here. Use governed source/lifecycle roots. |
| Need policy or schema authority? | Do not put it here. Use policy or schema roots. |
| Need release authority? | Do not put it here. Use release roots. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Agriculture fixtures under `fixtures/domains/agriculture/`
- test-local fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic SourceDescriptor, EvidenceRef, EvidenceBundle stub, AggregationReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard refs
- synthetic valid, invalid, denied, abstention, correction, withdrawal, and rollback cases
- canary values that make source-role collapse, aggregate-to-field collapse, private-detail leakage, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, source role, aggregation receipt ref, evidence ref, policy decision ID, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Direct reads from pre-public lifecycle stores, internal stores, unpublished candidates, or runtime outputs | Bypasses the trust membrane. |
| Real field/operator/parcel identifiers, proprietary records, farm operation detail, or person-land joins | Sensitive and rights-limited material must fail closed. |
| Secrets, credentials, private endpoints, production logs, or telemetry | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested Layout

```text
tests/fixtures/domains/agriculture/
|-- README.md
|-- manifest_expectations.json
|-- test_fixture_manifest_shape.py
|-- test_no_network_fixture_loading.py
|-- test_aggregate_fixture_receipt_refs.py
|-- test_field_level_denial_fixture_canaries.py
|-- test_source_role_fixture_no_upcast.py
`-- test_release_fixture_refs_do_not_authorize_publication.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/agriculture
```

Required run posture: no network access, no live service calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no private field/operator/parcel data, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal Fixture Manifest

Synthetic test-local manifests should describe fixture expectations without carrying real Agriculture data.

```json
{
  "fixture_manifest_id": "agriculture-test-fixture-manifest-example",
  "domain": "agriculture",
  "canonical_fixture_ref": "fixtures/domains/agriculture/valid/example-fixture.json",
  "fixture_family": "aggregate_public_safe",
  "source_role": "aggregate",
  "mock_marker": true,
  "evidence_ref": "evidence-ref-fixture-ag-test-fixture-001",
  "aggregation_receipt_ref": "aggregation-receipt-fixture-ag-test-fixture-001",
  "policy_decision_ref": "policy-decision-fixture-ag-test-fixture-001",
  "release_manifest_ref": null,
  "expected_outcome": "ABSTAIN",
  "reason_code": "FIXTURE_TEST_DOES_NOT_AUTHORIZE_PUBLICATION",
  "must_not_claim": [
    "FIELD_LEVEL_TRUTH_CANARY",
    "OPERATOR_IDENTITY_CANARY",
    "PARCEL_JOIN_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, fixture homes, reason codes, and CI wiring remain NEEDS VERIFICATION.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; `fixtures/` is the fixture responsibility root; authority roots remain separate. | Does not prove executable tests, fixture inventory, CI, or pass rates. |
| `fixtures/domains/agriculture/README.md` | CONFIRMED repo evidence | Defines the canonical Agriculture fixture root, fixture-only authority, observed child lanes, common fixture rules, and separation from source, catalog, policy, release, public-client, and lifecycle authority. | Payload inventory and test wiring remain NEEDS VERIFICATION. |
| `tests/domains/agriculture/README.md` | CONFIRMED repo evidence | Defines Agriculture domain tests and child lanes for aggregate-only, catalog closure, policy deny, rollback, schema, soil moisture, SSURGO lineage, and vegetation index behavior. | Does not prove executable tests or fixture payload presence. |
| `tests/e2e/agriculture/README.md` | CONFIRMED repo evidence | Defines Agriculture E2E fixture usage through governed envelopes and no-network public-safe posture. | Does not prove executable E2E tests. |
| `docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md` | CONFIRMED repo evidence | Defines no-network first posture and synthetic fixture expectations for Agriculture. | Many paths are PROPOSED until implementation verification. |
| `docs/domains/agriculture/DATA_LIFECYCLE.md` | CONFIRMED repo evidence | Defines Agriculture lifecycle, aggregate discipline, cross-lane boundaries, correction, and rollback posture. | It marks path-shaped claims and implementation details as PROPOSED where not inspected. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/fixtures/domains/agriculture/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |
| `tests/fixtures/README.md` and `tests/fixtures/domains/README.md` | CONFIRMED not found in GitHub fetch | Parent indexes were missing during authoring. | Missing parent indexes should be created before treating this subtree as mature. |

---

## Validation Checklist

- [ ] Confirm whether `tests/fixtures/` is intended as a supported test-local fixture lane or only a compatibility surface.
- [ ] Create or confirm parent indexes at `tests/fixtures/README.md` and `tests/fixtures/domains/README.md`.
- [ ] Confirm accepted rules for when test-local fixture wrappers may live here instead of `fixtures/domains/agriculture/`.
- [ ] Confirm fixture manifest schema, reason-code vocabulary, mock-marker requirements, and canary conventions.
- [ ] Confirm fixture payload inventory under `fixtures/domains/agriculture/` before linking tests to payloads.
- [ ] Add executable checks for manifest shape, no-network fixture loading, source-role preservation, aggregation receipt refs, field-level denial canaries, release refs, correction refs, and rollback refs.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, private details, direct lifecycle-store reads, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to store real source data, production fixture payloads, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, map implementation, API implementation, pipeline implementation, or AI runtime behavior.

Rollback is also required if this lane treats a fixture pass as source truth, catalog closure, policy approval, release approval, publication approval, map truth, AI truth, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent fixture-test indexes, fixture homes, manifest schema, source-role handling, aggregation handling, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)