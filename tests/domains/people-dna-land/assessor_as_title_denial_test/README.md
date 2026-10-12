<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-assessor-as-title-denial-test-readme
title: People DNA Land Assessor-as-Title Denial Test README
type: test-lane-readme
version: v0.1
status: draft; directory-created-in-scratch; negative-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People DNA Land domain steward
  - OWNER_TBD - Land ownership steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people-dna-land; assessor; tax-records; title-denial; parcel-boundary-denial; no-network; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, people-dna-land, assessor, tax-record, land-ownership, title, parcel, deed, source-role, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - ../../../../docs/domains/people-dna-land/
  - ../../../../docs/domains/people-dna-land/land-ownership/
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../policy/domains/people-dna-land/
  - ../../../../fixtures/domains/people-dna-land/assessor_as_title_denial_test/
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../release/manifests/people-dna-land/
notes:
  - "This README creates the local lane requested at tests/domains/people-dna-land/assessor_as_title_denial_test/README.md."
  - "Directory Rules place enforceability proof under tests/ and identify people-dna-land as a domain lane pattern."
  - "This is a negative test-lane README only. It does not define People DNA Land doctrine, land-title doctrine, contracts, schemas, fixtures, source descriptors, deeds, assessor data, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that assessor/tax records are not title truth and parcel geometry is not legal boundary proof unless source role, evidence, policy, review, and release explicitly support the narrower claim."
  - "Default posture is deterministic and no-network. Live assessor systems, tax rolls, parcel services, deed systems, title records, living-person records, source exports, and public release artifacts do not belong in this lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Assessor-as-title denial tests

> Negative test documentation for proving that assessor rows, tax records, parcel labels, and parcel geometry are not silently promoted into land-title truth or legal-boundary proof.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: assessor denial" src="https://img.shields.io/badge/lane-assessor__denial-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Posture: deny title overclaim" src="https://img.shields.io/badge/posture-deny__title__overclaim-critical">
</p>

**Path:** `tests/domains/people-dna-land/assessor_as_title_denial_test/README.md`  
**Status:** draft / directory-created-in-scratch / negative test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane:** `assessor_as_title_denial_test`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof and that `people-dna-land` is a domain lane pattern; CONFIRMED by attached doctrine that assessor/tax rows are not title truth, parcel geometry is not legal boundary proof, and land ownership is a temporal evidence-bound assertion rather than a map label alone; NEEDS VERIFICATION for executable tests, fixtures, schemas, validators, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/assessor_as_title_denial_test/` is a negative test lane for one high-risk overclaim:

> An assessor record, tax row, parcel owner label, or parcel polygon must not be treated as legal title truth or legal boundary proof by itself.

Tests in this lane should prove that KFM returns a finite non-answer, denial, validation failure, or promotion-blocking result when a workflow tries to convert assessor/tax context into title truth without the required source role, evidence, review, policy, release, correction, and rollback support.

A passing test here should **not** mean that a land-title claim is true, that an assessor source is admitted, that a parcel boundary is legally authoritative, that a deed chain is closed, or that a public land-ownership layer is approved. It should mean only that the scoped denial guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable. They also require domain-specific material to appear as a segment inside the responsibility root, such as `tests/domains/<domain>/`, and list `people-dna-land` in the domain lane pattern.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Assessor-as-title denial tests | `tests/domains/people-dna-land/assessor_as_title_denial_test/` | This directory. |
| Reusable synthetic fixtures | `fixtures/domains/people-dna-land/assessor_as_title_denial_test/` | Preferred fixture home if populated. |
| Semantic contracts | `contracts/domains/people-dna-land/` | Defines object meaning, not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` | Defines shape checks where accepted. |
| Policy rules | `policy/domains/people-dna-land/` | Decides allow, deny, restrict, and abstain. |
| Source descriptors | `data/registry/sources/people-dna-land/` | Source identity, rights, role, caveats, and permitted claim types. |
| Evidence and proofs | `data/proofs/` or accepted proof home | EvidenceBundle support, not stored here. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

---

## Invariant Under Test

> **Assessor evidence is not title authority.** Assessor/tax records may provide administrative or contextual evidence, but they do not prove legal title, complete ownership, deed-chain closure, current ownership, or legal parcel boundaries unless admitted under a narrower evidence role with supporting title-source evidence and release controls.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source-role separation | Assessor, tax, deed, title, survey, court, and parcel sources remain distinct. | validation failure / `ABSTAIN`. |
| Title overclaim denial | A claim that treats assessor/tax data as title truth is denied or abstained. | `DENY` / `ABSTAIN`. |
| Boundary overclaim denial | Parcel geometry is not treated as legal boundary proof by itself. | `DENY` / `ABSTAIN`. |
| Evidence closure | Title-like claims require admissible EvidenceBundle support with appropriate source roles. | `ABSTAIN`. |
| Temporal posture | Assessment year, tax year, deed date, valid time, retrieval time, and release time remain distinct. | validation failure. |
| Living-person and privacy posture | Current owner-like assertions involving living persons fail closed without policy support. | `DENY` / `ABSTAIN`. |
| UI/API wording | Public labels do not say "owner" or "title holder" when the support is only assessor/tax context. | validation failure / `DENY`. |
| Release boundary | Test success never becomes release approval or public exposure. | promotion block. |
| No network | Default tests do not call assessor, parcel, tax, deed, title, or people-search systems. | validation failure / `ERROR`. |

---

## Expected Scope

Tests in this lane may validate:

- denial when an assessor row is used as the sole support for "legal owner";
- denial when a tax mailing name is used as title holder truth;
- abstention when a parcel polygon is used as legal boundary proof without survey/title evidence;
- rejection of public UI/API wording that upgrades "assessor-listed party" into "owner";
- source-role mismatch handling for assessor, deed, title, parcel, tax, and survey fixtures;
- temporal separation between assessment year, tax year, deed date, retrieval time, release time, and correction time;
- living-person and privacy fail-closed behavior for current owner-like assertions;
- release, correction, withdrawal, and rollback preconditions for any public land-relationship carrier;
- no-network behavior for the default suite.

Out of scope for the default suite:

- real assessor exports, tax rolls, parcel datasets, deed images, title records, survey records, living-person records, people-search data, credentials, API calls, public tiles, public layers, and published artifacts.

---

## Fixture Posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- small enough for PR review;
- clearly labeled as synthetic;
- no real names, real parcel numbers, real addresses, real ownership records, real deed chains, real tax records, real title records, credentials, or production identifiers;
- explicit expected outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- explicit source role, claim type, assessment/tax/deed/valid/retrieval/release/correction time, evidence posture, living-person/privacy posture, policy state, release relationship, correction path, and rollback target where material.

---

## Finite Outcomes

| Condition | Expected outcome |
|---|---|
| Assessor fixture is described only as administrative/tax context | accepted context support only. |
| Assessor row is used as sole proof of legal title | `DENY` / `ABSTAIN`. |
| Tax mailing name is used as current title holder truth | `DENY` / `ABSTAIN`. |
| Parcel polygon is used as legal boundary proof without survey/title evidence | `DENY` / `ABSTAIN`. |
| Deed/title/source role evidence is missing for a title-like claim | `ABSTAIN`. |
| Current owner-like assertion involves living-person risk without policy support | `DENY`. |
| UI/API label upgrades context into "owner" or "title holder" | validation failure / `DENY`. |
| Release state, correction path, or rollback target is missing for public exposure | promotion-blocking failure. |
| Test attempts live assessor, parcel, deed, tax, title, or people-search access | validation failure / `ERROR`. |

---

## Suggested Layout

```text
tests/domains/people-dna-land/assessor_as_title_denial_test/
|-- README.md
|-- test_assessor_row_not_title_truth.py
|-- test_tax_mailing_name_not_title_holder.py
|-- test_parcel_geometry_not_legal_boundary.py
|-- test_source_role_mismatch_denies.py
|-- test_title_claim_requires_evidence_bundle.py
|-- test_living_person_owner_like_claim_denies.py
|-- test_public_label_does_not_upgrade_assessor_context.py
|-- test_release_correction_rollback_required.py
`-- test_no_network_land_provider_access.py
```

---

## Run Posture

```bash
pytest tests/domains/people-dna-land/assessor_as_title_denial_test
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; domain-specific material belongs under `tests/domains/<domain>/`; `people-dna-land` is listed in the domain lane pattern. | Does not prove executable test coverage. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | People/genealogy/DNA/land includes land ownership assertions, parcels, deeds, assessor/tax context, and temporal land tenure; assessor/tax rows are a risk when treated as title truth; parcel geometry is a risk when treated as legal boundary proof; land ownership is evidence-bound and temporal. | Does not prove runtime implementation in this sparse workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | Assessor and tax records are not title truth; parcel geometry is not title boundary proof; assertion-first modeling should keep source role, evidence, temporal scope, confidence, and policy posture visible. | Does not define jurisdiction-specific land-title law or production policy. |
| Current workspace | CONFIRMED | This README was created locally at the requested path. | Workspace is sparse and not a full verified repository checkout; CI and pass rates are UNKNOWN. |

---

## Validation Checklist

- [ ] Parent `tests/domains/people-dna-land/README.md` exists or this lane is linked from the accepted parent index.
- [ ] Executable tests exist under this lane.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic fixtures exist in the accepted fixture home.
- [ ] Source role, claim type, title-claim support, parcel-boundary support, living-person posture, rights, temporal fields, public label, release state, correction path, and rollback fields are accepted by schemas or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs this no-network denial lane or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live assessor, parcel, tax, deed, title, survey, genealogy, people-search, or DNA connector; lifecycle data store; person registry; land-title registry; source registry; contract root; schema authority; policy authority; proof store; release-decision root; public map/API/tile surface; AI surface; renderer implementation; pipeline implementation; or publication shortcut.

Rollback is also required if tests or documentation use assessor rows, tax mailing names, parcel polygons, map labels, or generated summaries as title truth without explicit source role, evidence, policy, review, release, correction, and rollback support.

<p align="right"><a href="#top">Back to top</a></p>
