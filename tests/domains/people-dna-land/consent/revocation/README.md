<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-consent-revocation-readme
title: People DNA Land Consent Revocation Tests README
type: test-lane-readme
version: v0.1
status: draft; directory-created-in-scratch; consent-revocation-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
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
policy_label: public-doc; tests; people-dna-land; consent; revocation; living-person-sensitive; dna-sensitive; no-network; evidence-bound; policy-gated; release-gated; correction-aware; withdrawal-aware; rollback-aware
tags: [kfm, tests, people-dna-land, consent, revocation, withdrawal, living-person, dna, genealogy, land-relationship, EvidenceBundle, PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../README.md
  - ../../../README.md
  - ../../assessor_as_title_denial_test/README.md
  - ../../chain_of_title_gap_test/README.md
  - ../../connectors/README.md
  - ../../../../../docs/domains/people-dna-land/
  - ../../../../../docs/domains/people-dna-land/land-ownership/
  - ../../../../../contracts/domains/people-dna-land/
  - ../../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../../policy/domains/people-dna-land/
  - ../../../../../fixtures/domains/people-dna-land/consent/revocation/
  - ../../../../../data/registry/sources/people-dna-land/
  - ../../../../../release/manifests/people-dna-land/
notes:
  - "This README replaces the placeholder content at tests/domains/people-dna-land/consent/revocation/README.md."
  - "Directory Rules place enforceability proof under tests/ and identify people-dna-land as a domain lane pattern."
  - "This is a consent-revocation test-lane README only. It does not define People DNA Land doctrine, consent policy, consent-record storage, contracts, schemas, fixtures, source descriptors, EvidenceBundles, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that consent revocation blocks or withdraws affected People/DNA/Land public exposure without deleting audit history, evidence lineage, review records, receipts, release records, correction notices, withdrawal notices, or rollback targets."
  - "Default posture is deterministic and no-network. Live consent databases, genealogy providers, DNA services, people-search services, deed/title/assessor systems, source exports, credentials, and public release artifacts do not belong in this lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Consent revocation tests

> Deterministic, no-network test documentation for proving that revoked consent blocks, withdraws, or re-scopes People DNA Land exposure without erasing the audit trail that makes the action inspectable.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: consent revocation" src="https://img.shields.io/badge/lane-consent__revocation-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Posture: revoke blocks exposure" src="https://img.shields.io/badge/posture-revoke__blocks__exposure-critical">
</p>

**Path:** `tests/domains/people-dna-land/consent/revocation/README.md`  
**Status:** draft / directory-created-in-scratch / consent revocation test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane:** `consent/revocation`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof and that `people-dna-land` is a domain lane pattern; CONFIRMED by attached doctrine that living-person and DNA-derived outputs are denied or restricted by default, that rights/consent affect admissibility, and that releases need correction, withdrawal, rollback, and cache invalidation paths; NEEDS VERIFICATION for executable consent-revocation tests, fixture shape, consent schemas, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/consent/revocation/` is the requested test lane for consent-revocation guardrails in the People DNA Land domain.

This lane should prove that a revoked, expired, narrowed, disputed, or superseded consent signal changes what KFM may expose. If a fixture says that consent for a living-person, DNA-linked, genealogy, relationship, private-land, or owner-like assertion has been revoked, public carriers should return a finite `DENY`, `ABSTAIN`, withdrawal, redaction, or promotion-blocking outcome rather than continuing to publish stale consent assumptions.

A passing test here should **not** mean that a real consent record is valid, that a revocation request is legally complete, that a source is admitted, that a person assertion is true, that DNA-derived relationship exposure is allowed, or that a public layer is approved. It should mean only that the scoped revocation guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable. They also require domain-specific material to appear as a segment inside the responsibility root, such as `tests/domains/<domain>/`, and list `people-dna-land` in the domain lane pattern.

This path is therefore a **test lane** for revocation behavior only. It is not the consent policy root, consent database, source registry, evidence store, release root, public API, public map surface, or production workflow implementation.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Consent revocation tests | `tests/domains/people-dna-land/consent/revocation/` | This directory. |
| Consent parent test index | `tests/domains/people-dna-land/consent/README.md` | SHOULD exist or be created to index consent lanes. |
| Reusable synthetic fixtures | `fixtures/domains/people-dna-land/consent/revocation/` | Preferred fixture home if populated. |
| Semantic contracts | `contracts/domains/people-dna-land/` | Defines object meaning, not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` | Defines shape checks where accepted. |
| Policy rules | `policy/domains/people-dna-land/` | Decides allow, deny, restrict, abstain, withdraw, and re-scope behavior. |
| Source descriptors | `data/registry/sources/people-dna-land/` | Source identity, rights, role, caveats, and permitted claim types. |
| Consent records | Accepted consent-record home after repo inspection | NEEDS VERIFICATION; not stored in this test lane. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

---

## Invariant Under Test

> **Revocation changes exposure, not history.** Consent revocation must block, withdraw, redact, or re-scope affected public and semi-public outputs. It must not delete evidence history, erase source lineage, mutate canonical records without receipts, or turn a test result into a release decision.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Revocation precedence | A revoked consent signal overrides earlier allow-like consent for affected exposure. | `DENY` / withdrawal-required failure. |
| Scope matching | Subject, purpose, data class, access role, audience, time, and exposure class are checked before deciding impact. | `ABSTAIN` / validation failure. |
| Living-person posture | Living-person assertions fail closed after revocation unless a separate accepted policy basis exists. | `DENY` / `ABSTAIN`. |
| DNA/genomic posture | DNA-linked or DNA-derived assertions deny or withdraw by default when consent is revoked or unclear. | `DENY`. |
| Derived exposure | Downstream labels, summaries, graphs, Focus answers, tiles, exports, and cached carriers are blocked or invalidated where affected. | promotion-blocking failure. |
| Evidence preservation | EvidenceBundle lineage, source refs, review records, receipts, correction notices, withdrawal notices, and rollback cards remain auditable. | validation failure. |
| Temporal posture | Consent grant time, revocation time, retrieval time, release time, correction time, and transaction time remain distinct. | validation failure. |
| Public wording | Public outputs do not imply consent remains valid after revocation. | `DENY` / validation failure. |
| Release boundary | Test success never becomes release approval, withdrawal execution, or public exposure. | promotion block. |
| No network | Default tests do not call consent services, identity providers, genealogy providers, DNA services, people-search services, or land systems. | validation failure / `ERROR`. |

---

## Expected Scope

Tests in this lane may validate:

- denial when a public People/DNA/Land carrier tries to use a revoked consent record;
- abstention when the system cannot determine whether a revocation applies to the requested subject, purpose, data class, time window, or exposure class;
- withdrawal-required behavior when a previously released public carrier depends on now-revoked consent;
- cache invalidation or derivative-output blocking for public labels, Focus Mode answers, graph projections, tiles, exports, and summaries;
- preservation of EvidenceBundle lineage, source refs, receipts, review records, release manifests, correction notices, withdrawal notices, and rollback targets;
- distinction between consent revocation and source deletion, evidence deletion, source-admission denial, title correction, or identity correction;
- living-person and DNA/genomic fail-closed behavior after revocation;
- no-network behavior for the default suite.

Out of scope for the default suite:

- real consent requests, real revocation records, real people records, living-person data, real DNA/genomic data, private family trees, provider exports, deed/title records, assessor records, parcel data, credentials, external API calls, production consent systems, public tiles, public layers, and published artifacts.

---

## Fixture Posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- small enough for PR review;
- clearly labeled as synthetic;
- no real names, real consent forms, real revocation requests, real family trees, real DNA data, real living-person relationships, real parcel numbers, real addresses, credentials, or production identifiers;
- explicit expected outcome: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or withdrawal-required validation failure;
- explicit consent subject, grant scope, revocation scope, purpose, audience, data class, access role, temporal scope, evidence posture, living-person posture, DNA/genomic posture, policy state, release relationship, correction path, withdrawal path, cache-invalidation posture, and rollback target where material.

---

## Finite Outcomes

| Condition | Expected outcome |
|---|---|
| Revocation clearly applies to requested public exposure | `DENY` or withdrawal-required failure. |
| Revocation scope is unclear or cannot be matched safely | `ABSTAIN`. |
| Consent was narrowed from public to restricted access | `DENY` for public exposure; restricted-path behavior NEEDS VERIFICATION. |
| Consent expired before release time | `DENY` / `ABSTAIN`. |
| Consent is revoked after a public release | withdrawal, correction, cache invalidation, and rollback checks are required. |
| EvidenceRef cannot resolve to EvidenceBundle for the affected claim | `ABSTAIN`. |
| Revocation is treated as evidence deletion | validation failure. |
| Revocation is ignored by Focus Mode, graph, tile, export, or summary output | validation failure / `DENY`. |
| Consent validator or policy engine is unavailable | `ERROR` / fail closed. |
| Test attempts live consent, genealogy, DNA, people-search, assessor, parcel, deed, or title access | validation failure / `ERROR`. |

---

## Suggested Layout

```text
tests/domains/people-dna-land/consent/revocation/
|-- README.md
|-- test_revoked_consent_denies_public_exposure.py
|-- test_scope_mismatch_abstains.py
|-- test_expired_consent_denies.py
|-- test_revocation_requires_withdrawal_for_released_carrier.py
|-- test_revocation_preserves_evidence_lineage.py
|-- test_dna_linked_revocation_denies.py
|-- test_living_person_revocation_denies.py
|-- test_derived_outputs_invalidate_after_revocation.py
|-- test_release_correction_withdrawal_rollback_required.py
`-- test_no_network_consent_provider_access.py
```

---

## Run Posture

```bash
pytest tests/domains/people-dna-land/consent/revocation
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; domain-specific material belongs under `tests/domains/<domain>/`; `people-dna-land` is listed in the domain lane pattern. | Does not prove executable consent-revocation test coverage. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | Public clients use governed APIs and released artifacts; `DENY` applies where rights, sensitivity, living-person data, DNA, or source terms are unsafe or unclear; sensitivity review includes living-person and DNA; correction/withdrawal and rollback are release-significant paths. | Does not prove consent schemas, consent runtime, executable tests, fixtures, validators, or CI exist in this workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | Public-safe defaults fail closed when rights, sensitivity, source authority, review state, release state, or evidence closure is unclear; source rights, source licenses, contacts, attribution, and written consent should be checked before ingest or release; living-person and DNA data require special protection. | Does not define jurisdiction-specific consent law, revocation mechanics, production policy, or storage location for consent records. |
| Adjacent `people-dna-land` test README files | CONFIRMED upstream pattern | Existing sibling lanes use KFM Meta Block v2, impact badges, placement basis, no-network posture, finite outcomes, validation checklist, and rollback sections. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| GitHub target file before this update | CONFIRMED | Existing `tests/domains/people-dna-land/consent/revocation/README.md` contained only `y`, so no substantive content was available to preserve. | Placeholder content did not prove implementation or doctrine. |

---

## Validation Checklist

- [ ] Parent `tests/domains/people-dna-land/consent/README.md` exists or is created to index consent test lanes.
- [ ] Executable tests exist under this lane.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic fixtures exist in the accepted fixture home.
- [ ] ConsentRecord, revocation event, consent scope, public-exposure class, living-person posture, DNA/genomic derivation, source role, evidence posture, release state, correction path, withdrawal path, cache-invalidation posture, and rollback fields are accepted by schemas or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] Revocation behavior distinguishes exposure blocking from audit-history deletion.
- [ ] CI runs this no-network consent-revocation lane or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live consent database, live provider connector, lifecycle data store, person registry, genealogy graph authority, land-title registry, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback is also required if tests or documentation treat consent revocation as deletion of evidence history, ignore revocation for derived public carriers, expose living-person or DNA-linked material after revocation without accepted policy support, or publish any People DNA Land output without explicit evidence, policy, review, release, correction, withdrawal, and rollback support.

<p align="right"><a href="#top">Back to top</a></p>
