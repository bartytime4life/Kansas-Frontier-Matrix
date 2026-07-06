<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-source-readme
title: Archaeology Source Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; archaeology-source-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Archaeology domain steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; archaeology; source-fixtures; source-admission; synthetic-only; no-network; deny-by-default; source-role-fixed; rights-aware; evidence-bound; policy-gated; review-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, archaeology, source-fixtures, source-admission, SourceDescriptor, SourceActivationDecision, source-role, rights-status, steward-authority, watcher-non-publisher, EvidenceBundle, EvidenceRef, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../api/README.md
  - ../promotion/README.md
  - ../review/README.md
  - ../sensitive_geometry/README.md
  - ../sites/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../domains/archaeology/fixtures/source_admission/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_candidate_feature/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_archaeological_site/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../../fixtures/domains/archaeology/valid/README.md
  - ../../../../../fixtures/domains/archaeology/invalid/README.md
  - ../../../../../docs/domains/archaeology/SOURCES.md
  - ../../../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../contracts/domains/archaeology/
  - ../../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../../schemas/contracts/v1/source/
  - ../../../../../data/registry/sources/archaeology/
  - ../../../../../policy/domains/archaeology/
  - ../../../../../release/candidates/archaeology/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/archaeology/source/README.md."
  - "This lane documents test-local expectations for archaeology source-shaped fixtures. Canonical reusable archaeology fixtures live under fixtures/domains/archaeology/ unless an ADR or parent README says otherwise."
  - "The confirmed source-admission test lane observed during authoring is tests/domains/archaeology/fixtures/source_admission/README.md. This requested tests/fixtures/.../source/ path must remain test-local and must not create parallel source-admission authority."
  - "No parent README was found at tests/fixtures/domains/archaeology/README.md during authoring. This lane is self-contained until that parent index is authored."
  - "Source-shaped fixtures are not SourceDescriptor authority, SourceActivationDecision authority, source registry records, source exports, EvidenceBundles, PolicyDecisions, ReviewRecords, ReleaseManifests, watcher outputs, public data, or publication approval."
  - "Executable tests, source fixture payload inventory, source schema bindings, harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology source test fixtures

> Test-lane documentation for Archaeology source-shaped fixtures referenced from `tests/fixtures/domains/archaeology/source/`. This path describes safe synthetic SourceDescriptor, SourceActivationDecision, source-role, rights, steward, watcher, quarantine, evidence, policy, review, and release-gate expectations without turning examples into source authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: source test fixtures" src="https://img.shields.io/badge/lane-source__test__fixtures-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not sources" src="https://img.shields.io/badge/boundary-fixtures__not__sources-success">
</p>

**Path:** `tests/fixtures/domains/archaeology/source/README.md`  
**Status:** draft / empty placeholder replaced / Archaeology source test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/archaeology/source`  
**Canonical reusable fixture root:** `fixtures/domains/archaeology/`  
**Confirmed related source-admission test lane:** `tests/domains/archaeology/fixtures/source_admission/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixture envelopes only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED `tests/fixtures/domains/archaeology/README.md` was not found during authoring; CONFIRMED sibling `api/`, `promotion/`, `review/`, `sensitive_geometry/`, and `sites/` README lanes exist as test-local fixture lanes; CONFIRMED `tests/domains/archaeology/fixtures/source_admission/README.md` exists and defines source-admission fixture-test boundaries; CONFIRMED `docs/domains/archaeology/SOURCES.md` and `SOURCE_REGISTRY.md` document source families, SourceDescriptor posture, role-fixed-at-admission discipline, deny-by-default sensitivity, watcher non-publisher posture, and SourceActivationDecision gating; NEEDS VERIFICATION for executable source-fixture tests, fixture payload inventory, accepted schemas, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/archaeology/source/` is a test-local documentation lane for Archaeology source-shaped fixture expectations.

This lane should describe how tests may use synthetic source-admission examples for SourceDescriptor-like envelopes, SourceActivationDecision-like envelopes, source-role preservation, rights posture, steward authority, sensitivity classification, access-method posture, watcher metadata, quarantine decisions, stale-source decisions, supersession decisions, correction refs, withdrawal refs, and rollback refs.

A passing fixture check here should not mean that a source is admitted, a source export is present, rights are resolved, a steward approved use, a candidate is confirmed, a protected detail is releasable, evidence is proven, policy allows release, a release manifest is valid, a public layer is published, or an AI answer is authoritative. It should mean only that a bounded synthetic source-shaped fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement Basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. Source registries and SourceDescriptors belong in their accepted registry/source homes, not in test fixture lanes. This requested path sits under `tests/fixtures/`, so it must remain test-scoped and subordinate to source, fixture, registry, schema, contract, policy, evidence, receipt, release, map, API, and public artifact roots.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Source-shaped fixture-test expectations | `tests/fixtures/domains/archaeology/source/` | This directory. |
| Parent test-fixture lane | `tests/fixtures/domains/archaeology/` | Parent README missing at authoring time; NEEDS VERIFICATION. |
| Source-admission fixture tests | `tests/domains/archaeology/fixtures/source_admission/` | Confirmed related test lane; not replaced here. |
| Reusable archaeology fixtures | `fixtures/domains/archaeology/` | Canonical fixture root; referenced, not replaced. |
| Source registry and descriptors | `data/registry/sources/archaeology/` and accepted source catalog homes | Authority lives there; not here. |
| Archaeology source-family doctrine | `docs/domains/archaeology/SOURCES.md`, `SOURCE_REGISTRY.md` | Explains posture; not authored here. |
| Source schemas | `schemas/contracts/v1/source/` or ADR-selected equivalent | Define machine shape; not owned here. |
| Archaeology object contracts | `contracts/domains/archaeology/` | Define object meaning; not owned here. |
| Policy authority | `policy/domains/archaeology/` or accepted policy roots | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a source registry, source export cache, SourceDescriptor store, watcher output store, provenance ledger, review queue, policy decision store, release candidate folder, map-layer source, or public artifact home. It is a documentation and test-fixture expectation lane only.

---

## Invariant Under Test

> **Source-shaped fixtures are synthetic admission examples, not source authority.** Test fixture success proves only that the source-admission guardrail behaved as expected for a bounded example.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/archaeology/`; test-local wrappers require a documented reason. | validation failure. |
| Source-authority boundary | SourceDescriptor, SourceActivationDecision, source registry records, source descriptors, and watcher receipts are not authored or stored here. | promotion block. |
| Synthetic-only boundary | Source fixtures use fake IDs, mock markers, fake access metadata, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source systems, restricted APIs, web harvesters, geocoders, map services, release services, public APIs, or AI runtimes. | `ERROR`. |
| Source-role boundary | Source role is explicit and cannot be upcast by fixtures, validators, catalog helpers, maps, API wording, or generated text. | `DENY` / `ABSTAIN`. |
| Rights boundary | Rights, license, attribution, redistribution, embargo, and use constraints are explicit or the fixture fails closed. | `DENY` / `ABSTAIN`. |
| Sensitivity boundary | Sensitive source families and protected details fail closed unless synthetic policy, review, redaction, and release refs are present. | `DENY` / `ABSTAIN`. |
| Watcher boundary | Watcher-shaped fixture data is non-publisher metadata and cannot admit, promote, release, or publish source material. | validation failure. |
| Evidence boundary | Source-shaped fixtures can reference evidence expectations but do not become EvidenceBundles or proof closure. | `ABSTAIN`. |
| Release boundary | Fixture success does not become source admission, release approval, map publication, correction approval, or rollback approval. | promotion block. |

---

## Expected Source Fixture Families

| Family | Purpose | Boundary |
|---|---|---|
| SourceDescriptor-shaped fixtures | Verify source identity, role, rights, cadence, steward, sensitivity, and access fields are present where expected. | Fixture is not a real SourceDescriptor. |
| SourceActivationDecision-shaped fixtures | Verify admit, quarantine, restrict, deny, abstain, stale, supersede, and error-like decisions are finite and reasoned. | Fixture is not admission authority. |
| Source-role fixtures | Verify candidate, administrative, observed, modeled, aggregate, regulatory, context, and synthetic roles do not collapse. | Role cannot be upgraded by tests. |
| Rights and access fixtures | Verify unresolved rights, license, embargo, or access terms deny or abstain. | Fixture is not legal clearance. |
| Steward authority fixtures | Verify steward refs and reviewer roles are explicit where material. | Ref is synthetic, not approval. |
| Sensitivity fixtures | Verify exact location, restricted context, and protected-detail examples fail closed. | Negative examples must still be synthetic. |
| Watcher metadata fixtures | Verify ETag, Last-Modified, checksum, content length, cadence, and stale-state markers are treated as metadata. | Watcher is not publisher. |
| Quarantine fixtures | Verify incomplete or conflicting source posture routes to quarantine or abstention. | Quarantine is not deletion. |
| Supersession and rollback fixtures | Verify stale, superseded, withdrawn, corrected, and rollback refs remain auditable. | No silent edit. |
| No-network fixtures | Verify local deterministic loading and no live source calls. | Integration tests require separate gates. |

---

## Relationship to Source-Admission Tests

The confirmed `tests/domains/archaeology/fixtures/source_admission/README.md` lane describes tests that verify archaeology source-admission fixtures are safe, synthetic, reviewable, and bounded before default test runs. This `tests/fixtures/.../source/` lane is narrower: it documents test-local source-shaped fixture wrappers and expectation manifests.

| Question | Preferred answer |
|---|---|
| Need executable source-admission guardrail tests? | Use `tests/domains/archaeology/fixtures/source_admission/`. |
| Need reusable fixture payloads? | Use `fixtures/domains/archaeology/` or an accepted canonical fixture child lane. |
| Need a test-only source wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need a real source descriptor or registry record? | Do not put it here. Use accepted source registry/catalog roots. |
| Need source data or a source export? | Do not put it here. Use governed lifecycle roots with rights, sensitivity, and quarantine handling. |
| Need policy, schema, evidence, receipt, or release authority? | Do not put it here. Use the owning root. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Archaeology fixtures under `fixtures/domains/archaeology/`
- test-local source fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic SourceDescriptor-shaped and SourceActivationDecision-shaped envelopes
- synthetic source-family cases such as state inventory, public listing, field survey, excavation packet, collection record, lab report, historic map, and oral-history/cultural-knowledge placeholders
- synthetic source-role, rights-status, access-method, steward-authority, sensitivity, sovereignty-label, watcher-metadata, stale-state, supersession, quarantine, correction, withdrawal, and rollback refs
- synthetic EvidenceRef, EvidenceBundle-stub, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard refs
- canary values that make source-role upcast, source-admission bypass, rights overclaiming, steward-approval leakage, protected-detail exposure, watcher-publisher collapse, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, source family, source role, rights posture, sensitivity posture, access posture, steward ref, watcher metadata ref, evidence ref, policy decision ID, review record ID, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source records, source descriptors, source registry YAML, source-system exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, or runtime outputs | Bypasses the trust membrane. |
| Real coordinates, protected site details, restricted source terms, reviewer notes, consultation records, rights-holder communications, or collection-security details | Sensitive material requires governed policy, review, redaction, and release controls. |
| Secrets, credentials, private endpoints, production logs, or telemetry | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, API implementation, map implementation, pipeline implementation, watcher implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested Layout

```text
tests/fixtures/domains/archaeology/source/
|-- README.md
|-- manifest_expectations.json
|-- test_source_fixture_manifest_shape.py
|-- test_source_fixture_no_network.py
|-- test_source_descriptor_fixture_not_source_authority.py
|-- test_source_role_fixture_no_upcast.py
|-- test_rights_and_sensitivity_fixture_fail_closed.py
|-- test_watcher_metadata_fixture_not_publisher.py
|-- test_quarantine_supersession_rollback_refs.py
`-- test_source_fixture_canaries.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/archaeology/source
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no geocoding, no real secrets, no production logs, no production trust artifacts, no protected location detail, no source exports, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal Source Fixture Manifest

Synthetic test-local manifests should describe source fixture expectations without carrying real source data or source authority.

```json
{
  "fixture_manifest_id": "archaeology-source-test-fixture-manifest-example",
  "domain": "archaeology",
  "fixture_family": "source_admission_guardrail_envelope",
  "source_descriptor_ref": "source-descriptor-fixture-arch-source-001",
  "source_activation_decision_ref": null,
  "source_family": "public_listing_placeholder",
  "source_role": "candidate",
  "rights_status": "needs_verification",
  "access_method": "fixture_only",
  "watcher_metadata_present": true,
  "mock_marker": true,
  "evidence_ref": "evidence-ref-fixture-arch-source-001",
  "policy_decision_ref": "policy-decision-fixture-arch-source-001",
  "review_record_ref": "review-record-fixture-arch-source-001",
  "redaction_receipt_ref": "redaction-receipt-fixture-arch-source-001",
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card-fixture-arch-source-001",
  "expected_outcome": "ABSTAIN",
  "reason_code": "SOURCE_FIXTURE_TEST_DOES_NOT_AUTHORIZE_ADMISSION_OR_PUBLICATION",
  "must_not_claim": [
    "SOURCE_ADMITTED_CANARY",
    "SOURCE_AUTHORITY_CANARY",
    "RIGHTS_RESOLVED_CANARY",
    "STEWARD_APPROVAL_CANARY",
    "CONFIRMED_SITE_CANARY",
    "PROTECTED_DETAIL_CANARY",
    "WATCHER_PUBLISHER_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, fixture homes, source-family vocabulary, source-role vocabulary, reason codes, and CI wiring remain NEEDS VERIFICATION.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; `fixtures/` is the fixture responsibility root; source registry, schemas, policy, evidence, receipts, release, map, API, and public artifacts remain separate. | Does not prove executable tests, fixture inventory, CI, or pass rates. |
| `tests/domains/archaeology/fixtures/source_admission/README.md` | CONFIRMED repo evidence | Defines a source-admission fixture-test lane and states fixtures must be safe, synthetic, reviewable, bounded, and non-authoritative. | Does not prove this `tests/fixtures/.../source/` lane has executable tests. |
| `docs/domains/archaeology/SOURCES.md` | CONFIRMED repo evidence | Defines archaeology source-family catalogue, SourceDescriptor posture, role-fixed-at-admission discipline, deny-by-default admission, watcher non-publisher posture, and source-admission flow. | It marks many path and implementation claims PROPOSED. |
| `docs/domains/archaeology/SOURCE_REGISTRY.md` | CONFIRMED repo evidence | Defines archaeology source registry as admission and authority-control surface, not bibliography; names SourceDescriptor fields, source roles, rights, access, cadence, steward, sensitivity, release class, and SourceActivationDecision posture. | Machine truth lives in registry YAML and schemas; implementation remains NEEDS VERIFICATION where not inspected. |
| `fixtures/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines the canonical Archaeology fixture root, child fixture lanes, accepted synthetic examples, exclusions, and verification status. | Payload inventory and test wiring remain NEEDS VERIFICATION. |
| `tests/fixtures/domains/archaeology/api/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local API fixture posture and notes missing immediate parent index. | Does not prove source-fixture tests exist. |
| `tests/fixtures/domains/archaeology/promotion/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local promotion fixture posture and release-boundary discipline. | Does not prove source-fixture tests exist. |
| `tests/fixtures/domains/archaeology/review/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local review fixture posture and review-approval boundary. | Does not prove source-fixture tests exist. |
| `tests/fixtures/domains/archaeology/sensitive_geometry/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local sensitive-geometry fixture posture and no-protected-coordinate boundary. | Does not prove source-fixture tests exist. |
| `tests/fixtures/domains/archaeology/sites/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local site fixture posture and candidate-not-confirmed boundary. | Does not prove source-fixture tests exist. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/fixtures/domains/archaeology/source/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |
| `tests/fixtures/domains/archaeology/README.md` | CONFIRMED not found in GitHub fetch | Parent index was missing during authoring. | Missing parent should be created before treating this subtree as mature. |

---

## Validation Checklist

- [ ] Confirm whether `tests/fixtures/` is intended as a supported test-local fixture lane or only a compatibility surface.
- [ ] Create or confirm parent indexes at `tests/fixtures/README.md`, `tests/fixtures/domains/README.md`, and `tests/fixtures/domains/archaeology/README.md`.
- [ ] Confirm accepted rules for when source fixture wrappers may live here instead of `fixtures/domains/archaeology/` or `tests/domains/archaeology/fixtures/source_admission/`.
- [ ] Confirm source fixture manifest schema, source-family vocabulary, source-role vocabulary, rights-status vocabulary, reason-code vocabulary, mock-marker requirements, and canary conventions.
- [ ] Confirm fixture payload inventory under `fixtures/domains/archaeology/` before linking tests to payloads.
- [ ] Add executable checks for manifest shape, no-network fixture loading, SourceDescriptor shape, SourceActivationDecision shape, source-role no-upcast, rights fail-closed behavior, sensitivity fail-closed behavior, watcher non-publisher behavior, quarantine refs, supersession refs, correction refs, withdrawal refs, rollback refs, and public-surface canaries.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, restricted details, direct lifecycle-store reads, geocoders, map services, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to store real source records, source descriptors, source registry records, source-system exports, watcher outputs, restricted source terms, protected-location material, production source payloads, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, map implementation, API implementation, pipeline implementation, watcher implementation, or AI runtime behavior.

Rollback is also required if this lane treats a source-shaped fixture pass as source admission, source authority, rights resolution, steward approval, evidence proof, policy approval, review approval, release approval, publication approval, map truth, AI truth, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent fixture-test indexes, fixture homes, manifest schema, source vocabulary, source-role behavior, rights expectations, sensitivity expectations, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)