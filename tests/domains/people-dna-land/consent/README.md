<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-consent-readme
title: People DNA Land Consent Tests README
type: test-index-readme
version: v0.1
status: draft; directory-created-in-scratch; consent-test-index; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People DNA Land domain steward
  - OWNER_TBD - Consent steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people-dna-land; consent; parent-index; living-person-sensitive; dna-sensitive; no-network; evidence-bound; policy-gated; release-gated; correction-aware; withdrawal-aware; rollback-aware
tags: [kfm, tests, people-dna-land, consent, revocation, expiry, scope, living-person, dna, genealogy, land-relationship, EvidenceBundle, PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - revocation/README.md
  - ../assessor_as_title_denial_test/README.md
  - ../chain_of_title_gap_test/README.md
  - ../connectors/README.md
  - ../../../../docs/domains/people-dna-land/
  - ../../../../docs/domains/people-dna-land/land-ownership/
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../policy/domains/people-dna-land/
  - ../../../../fixtures/domains/people-dna-land/consent/
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../release/manifests/people-dna-land/
notes:
  - "This README replaces the placeholder content at tests/domains/people-dna-land/consent/README.md."
  - "Directory Rules place enforceability proof under tests/ and identify people-dna-land as a domain lane pattern."
  - "This is a consent test index only. It does not define People DNA Land doctrine, consent policy, consent-record storage, contracts, schemas, fixtures, source descriptors, EvidenceBundles, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested parent invariant is that consent is an exposure gate, not truth, evidence closure, source admission, release approval, or publication."
  - "Default posture is deterministic and no-network. Live consent databases, genealogy providers, DNA services, deed/title/assessor systems, people-search services, source exports, credentials, and public release artifacts do not belong in default consent tests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People DNA Land consent tests

> Parent index for deterministic, no-network consent guardrail tests in the People DNA Land domain. These tests should prove consent scope, denial, revocation, expiry, redaction, release, correction, withdrawal, and rollback behavior without becoming consent policy, consent storage, or public release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: consent tests" src="https://img.shields.io/badge/lane-consent__tests-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not consent authority" src="https://img.shields.io/badge/boundary-tests__not__consent__authority-success">
</p>

**Path:** `tests/domains/people-dna-land/consent/README.md`  
**Status:** draft / directory-created-in-scratch / consent test parent index / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane family:** `consent`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof and that `people-dna-land` is a domain lane pattern; CONFIRMED by attached doctrine that rights, source terms, consent, living-person data, DNA, review state, release state, correction, withdrawal, and rollback can block public exposure; CONFIRMED current child lane exists at `tests/domains/people-dna-land/consent/revocation/README.md`; NEEDS VERIFICATION for executable consent tests, accepted consent-record shape, policy runtime, fixtures, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/consent/` is the parent test index for consent-related guardrails in the People DNA Land domain.

This subtree should prove that consent scope is explicit before sensitive People/DNA/Land material can be exposed. Consent-sensitive assertions may involve living-person identity, DNA-derived relationships, genealogy claims, family links, private-land associations, owner-like labels, source exports, or derived public carriers. The test family should exercise the finite outcomes KFM needs when consent is missing, expired, revoked, narrowed, disputed, mismatched, or insufficient for the requested exposure.

A passing consent test should **not** mean that a real consent record is valid, a person assertion is true, DNA-derived exposure is allowed, a land relationship is publishable, a source is admitted, or a release is approved. It should mean only that the scoped consent guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable. They also require domain-specific material to appear as a segment inside the responsibility root, such as `tests/domains/<domain>/`, and list `people-dna-land` in the domain lane pattern.

This directory is therefore a test lane family for consent behavior only. Consent policy belongs under `policy/`; semantic meaning belongs under `contracts/`; machine shape belongs under `schemas/`; release authority belongs under `release/`; source descriptors belong under `data/registry/sources/`; and reusable synthetic fixtures belong under the accepted fixture home.

| Responsibility | Correct home | This lane family's relationship |
|---|---|---|
| Consent behavior tests | `tests/domains/people-dna-land/consent/` | This directory. |
| Reusable synthetic fixtures | `fixtures/domains/people-dna-land/consent/` | Preferred fixture home if populated. |
| Semantic contracts | `contracts/domains/people-dna-land/` | Defines object meaning, not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` | Defines shape checks where accepted. |
| Policy rules | `policy/domains/people-dna-land/` | Decides allow, deny, restrict, abstain, withdraw, and re-scope behavior. |
| Source descriptors | `data/registry/sources/people-dna-land/` | Source identity, rights, role, caveats, consent obligations, and permitted claim types. |
| Consent records | Accepted consent-record home after repo inspection | NEEDS VERIFICATION; not stored in this test lane family. |
| Evidence and proofs | `data/proofs/` or accepted proof home | EvidenceBundle support, not stored here. |
| Release decisions | `release/` | Publication, correction, withdrawal, rollback, and cache invalidation authority. |

---

## Parent Invariant

> **Consent is an exposure gate, not a truth source.** Consent can help decide whether a bounded People/DNA/Land assertion may be exposed to a specific audience for a specific purpose. It cannot by itself create evidence, prove relationships, admit a source, validate land ownership, authorize public release, or erase audit history.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Explicit scope | Subject, purpose, audience, access role, data class, derivation, geography, time, and exposure class remain explicit where material. | validation failure / `ABSTAIN`. |
| Missing consent | Missing required consent blocks public or semi-public exposure. | `DENY` / `ABSTAIN`. |
| Scope mismatch | Consent for one purpose, audience, role, data class, or time window cannot silently authorize another. | `DENY` / `ABSTAIN`. |
| Expiry and supersession | Expired, superseded, disputed, or stale consent fails closed. | `DENY` / `ABSTAIN`. |
| Revocation | Revocation blocks or withdraws affected exposure without deleting evidence lineage. | `DENY` / withdrawal-required failure. |
| Living-person posture | Living-person assertions fail closed without accepted policy and consent support where required. | `DENY` / `ABSTAIN`. |
| DNA/genomic posture | DNA-linked or DNA-derived assertions deny or restrict by default unless policy and consent support a narrower exposure. | `DENY`. |
| Evidence boundary | Consent does not replace EvidenceBundle support or source-role review. | `ABSTAIN` / validation failure. |
| Release boundary | Test success never becomes release approval, release manifest, public exposure, correction, withdrawal, or rollback. | promotion block. |
| No network | Default consent tests use synthetic local fixtures only. | validation failure / `ERROR`. |

---

## Lane Index

| Lane | Primary responsibility | Boundary |
|---|---|---|
| [`revocation/`](revocation/README.md) | Revoked, narrowed, expired, disputed, or superseded consent behavior; withdrawal/correction/rollback posture for affected public carriers. | Revocation tests do not execute real revocations, delete evidence, mutate consent stores, or approve publication. |

Additional consent lanes may be added only when their fixture posture, consent object assumptions, policy expectations, sensitive-data posture, release relationship, correction path, withdrawal path, and rollback target are explicit.

Potential future lanes:

| Lane | Proposed responsibility | Status |
|---|---|---|
| `scope/` | Subject, purpose, role, audience, time, geography, data class, and exposure-class matching. | PROPOSED / NEEDS VERIFICATION. |
| `expiry/` | Expired, stale, superseded, or review-due consent behavior. | PROPOSED / NEEDS VERIFICATION. |
| `grant/` | Positive consent fixture behavior that still requires evidence, policy, review, and release. | PROPOSED / NEEDS VERIFICATION. |
| `derived_data/` | Consent behavior for DNA-derived, relationship-derived, graph-derived, AI-derived, and map-derived carriers. | PROPOSED / NEEDS VERIFICATION. |
| `access_roles/` | Role-bounded access tests for steward-only, restricted, staged, public, or denied exposure classes. | PROPOSED / NEEDS VERIFICATION. |
| `audit_trail/` | Consent-change receipts, transaction time, correction notices, withdrawal notices, and rollback card checks. | PROPOSED / NEEDS VERIFICATION. |

---

## Expected Test Families

The consent test family should eventually cover:

| Family | Expected proof point |
|---|---|
| Consent scope | Consent is matched by subject, purpose, audience, role, data class, derivation, geography, and time. |
| Missing consent | Required consent absence produces finite `DENY`, `ABSTAIN`, or fail-closed `ERROR`. |
| Scope mismatch | Consent for one use cannot authorize broader, public, derivative, or unrelated exposure. |
| Expiry and staleness | Expired, stale, superseded, or review-due consent blocks exposure until reviewed. |
| Revocation and withdrawal | Revoked consent blocks new exposure and requires withdrawal/correction/rollback checks for released carriers. |
| Living-person protection | Living-person outputs fail closed unless policy, evidence, consent, review, and release support a bounded path. |
| DNA/genomic restriction | DNA-linked and DNA-derived outputs remain restricted or denied by default. |
| Source rights and terms | Provider terms, source rights, and consent obligations remain visible and non-interchangeable. |
| Evidence closure | Consent never substitutes for EvidenceRef-to-EvidenceBundle resolution. |
| Release/correction/rollback | Public exposure requires release state, correction path, withdrawal path, rollback target, and cache invalidation posture. |
| No-network discipline | Default tests run from local synthetic fixtures, local schemas/contracts where available, and stubs only. |

---

## What Belongs Here

Appropriate contents include:

- deterministic no-network consent behavior tests;
- parent and child-lane README files;
- compact synthetic fixture pointers;
- consent-scope, expiry, revocation, and mismatch checks;
- living-person, DNA/genomic, relationship, private-land, and owner-like exposure denial tests;
- evidence, policy, release, correction, withdrawal, cache-invalidation, and rollback gate checks;
- tests proving that consent changes exposure while preserving audit lineage.

---

## Forbidden Shortcuts

Do not use this subtree to:

- store real consent records, real revocation requests, real people records, real DNA/genomic data, real match lists, private family trees, provider exports, deed/title records, assessor records, parcel data, credentials, source payloads, public tiles, proof artifacts, or release artifacts;
- call live consent databases, identity providers, genealogy providers, DNA services, people-search services, deed/title systems, assessor systems, parcel services, geocoders, or source systems by default;
- define consent policy, consent schemas, consent contracts, source registries, People DNA Land doctrine, EvidenceBundle contracts, release decisions, public API behavior, public map behavior, renderer code, or production pipeline code;
- treat consent as proof of a person assertion, relationship assertion, DNA-derived inference, title claim, source admission, EvidenceBundle closure, or release approval;
- publish, promote, approve, release, correct, withdraw, roll back, or cache-invalidate anything.

Any test that needs live provider access, production source data, real consent systems, real subject requests, or public output belongs in a gated integration tier with explicit source admission, rights review, sensitivity review, policy decision, receipts, release controls, correction path, withdrawal path, and rollback targets.

---

## Run Posture

Parent consent test command:

```bash
pytest tests/domains/people-dna-land/consent
```

Selected child-lane example:

```bash
pytest tests/domains/people-dna-land/consent/revocation
```

Status of these commands: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted runner and that executable test modules exist. This README does not claim any command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; domain-specific material belongs under `tests/domains/<domain>/`; `people-dna-land` is listed in the domain lane pattern; fixtures belong under the accepted fixture home. | Does not prove executable consent test coverage or consent runtime implementation. |
| `revocation/README.md` | CONFIRMED upstream child lane | Existing child lane for consent revocation behavior under this consent test family. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | Public clients use governed APIs and released artifacts; `DENY` applies where rights, sensitivity, living-person data, DNA, or source terms are unsafe or unclear; release-significant material requires correction, withdrawal, rollback, and cache invalidation paths. | Does not prove consent schemas, consent runtime, executable tests, fixtures, validators, CI, or pass rates exist in this workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | Public-safe defaults fail closed when rights, sensitivity, source authority, review state, release state, or evidence closure is unclear; source rights, source licenses, contacts, attribution, and written consent should be checked before ingest or release; living-person and DNA data require special protection. | Does not define jurisdiction-specific consent law, production policy, or storage location for consent records. |
| Adjacent `people-dna-land` test README files | CONFIRMED upstream pattern | Existing sibling lanes use KFM Meta Block v2, impact badges, placement basis, no-network posture, lane index, finite outcomes, validation checklist, and rollback sections. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| GitHub target file before this update | CONFIRMED | Existing `tests/domains/people-dna-land/consent/README.md` contained only `y`, so no substantive content was available to preserve. | Placeholder content did not prove implementation or doctrine. |

---

## Validation Checklist

- [ ] Executable consent tests exist under documented child lanes.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic consent fixtures exist in the accepted fixture home.
- [ ] ConsentRecord, consent scope, revocation event, expiry state, public-exposure class, living-person posture, DNA/genomic derivation, source role, evidence posture, release state, correction path, withdrawal path, cache-invalidation posture, and rollback fields are accepted by schemas or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] Consent tests distinguish exposure authorization from truth, evidence closure, source admission, release approval, and audit-history deletion.
- [ ] CI runs this no-network consent test family or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this consent test family becomes a live consent database, live provider connector, lifecycle data store, person registry, genealogy graph authority, land-title registry, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback is also required if tests or documentation treat consent as evidence, truth, source admission, release approval, or deletion authority; ignore missing, mismatched, expired, or revoked consent; expose living-person or DNA-linked material without accepted policy support; or publish any People DNA Land output without explicit evidence, policy, review, release, correction, withdrawal, and rollback support.

<p align="right"><a href="#top">Back to top</a></p>
