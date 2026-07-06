<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-contracts-readme
title: People DNA Land Contract Tests README
type: test-index-readme
version: v0.1
status: draft; directory-created-in-scratch; contract-test-index; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People DNA Land domain steward
  - OWNER_TBD - Contract steward
  - OWNER_TBD - Schema steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people-dna-land; contracts; parent-index; living-person-sensitive; dna-sensitive; no-network; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, people-dna-land, contracts, schemas, person-assertion, relationship-assertion, land-relationship, living-person, dna, consent, source-role, EvidenceBundle, PolicyDecision, ConsentRecord, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - person-assertion/README.md
  - ../consent/README.md
  - ../connectors/README.md
  - ../assessor_as_title_denial_test/README.md
  - ../chain_of_title_gap_test/README.md
  - ../../../../docs/domains/people-dna-land/
  - ../../../../docs/domains/people-dna-land/land-ownership/
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../policy/domains/people-dna-land/
  - ../../../../fixtures/domains/people-dna-land/contracts/
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../release/manifests/people-dna-land/
notes:
  - "This README replaces the placeholder content at tests/domains/people-dna-land/contracts/README.md."
  - "Directory Rules place enforceability proof under tests/, semantic meaning under contracts/, machine shape under schemas/, policy decisions under policy/, and people-dna-land as a domain lane pattern."
  - "This is a contract test index only. It does not define People DNA Land contracts, schemas, policies, consent records, source descriptors, EvidenceBundles, person registries, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested parent invariant is that contract-shaped objects remain governed assertions or envelopes until evidence, policy, consent, review, release, correction, withdrawal, and rollback requirements are satisfied."
  - "Default posture is deterministic and no-network. Real people records, living-person records, DNA data, genealogy provider exports, consent records, source exports, credentials, and public release artifacts do not belong in default contract tests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People DNA Land contract tests

> Parent index for deterministic, no-network contract-enforceability tests in the People DNA Land domain. These tests should prove that contract-shaped objects preserve evidence, source role, temporal scope, consent, sensitivity, policy, release, correction, withdrawal, and rollback boundaries without becoming contract authority themselves.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: contract tests" src="https://img.shields.io/badge/lane-contract__tests-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not contracts" src="https://img.shields.io/badge/boundary-tests__not__contracts-success">
</p>

**Path:** `tests/domains/people-dna-land/contracts/README.md`  
**Status:** draft / directory-created-in-scratch / contract test parent index / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane family:** `contracts`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof, `contracts/` owns object meaning, `schemas/` owns machine-checkable shape, `policy/` owns allow/deny/restrict/abstain behavior, and `people-dna-land` is a domain lane pattern; CONFIRMED current child lane exists at `tests/domains/people-dna-land/contracts/person-assertion/README.md`; CONFIRMED by attached doctrine that People DNA Land contract-shaped objects must preserve source role, evidence, living-person/DNA sensitivity, consent, temporal scope, review state, release state, correction, and rollback boundaries; NEEDS VERIFICATION for executable contract tests, accepted contracts, schema fields, validators, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/contracts/` is the parent test index for contract-enforceability tests in the People DNA Land domain.

This subtree should prove that People DNA Land contract-shaped objects behave like governed assertions and envelopes, not like public truth. Person assertions, relationship assertions, consent-bearing objects, land-relationship assertions, source-role bindings, evidence references, and release-aware payloads must remain bounded by source role, evidence, time, consent, sensitivity, review, policy, and release state.

A passing contract test should **not** mean that a semantic contract is complete, a schema is authoritative, a person assertion is true, a relationship is proven, a consent record is valid, a living-person assertion is publishable, a DNA-derived assertion is allowed, or a release is approved. It should mean only that the scoped contract guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules separate responsibility roots:

| Responsibility | Canonical root |
|---|---|
| Semantic object meaning | `contracts/` |
| Machine-checkable shape | `schemas/` |
| Allow, deny, restrict, abstain, and release policy | `policy/` |
| Enforceability proof | `tests/` |
| Golden, valid, invalid, or synthetic test data | `fixtures/` or accepted test fixture home |

This directory is therefore a **test lane family** for contract behavior only. It may test the behavior expected of contracts and schemas, but it must not become the source of contract meaning, schema shape, policy behavior, source admission, consent storage, evidence closure, release approval, public API behavior, public map behavior, or publication.

| Responsibility | Correct home | This lane family's relationship |
|---|---|---|
| People DNA Land contract behavior tests | `tests/domains/people-dna-land/contracts/` | This directory. |
| Semantic contracts | `contracts/domains/people-dna-land/` | Defines object meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` | Defines accepted shape where available. |
| Policy rules | `policy/domains/people-dna-land/` | Decides allow, deny, restrict, abstain, redact, withdraw, and release behavior. |
| Reusable synthetic fixtures | `fixtures/domains/people-dna-land/contracts/` | Preferred fixture home if populated. |
| Source descriptors | `data/registry/sources/people-dna-land/` | Source identity, rights, role, caveats, consent obligations, and permitted claim types. |
| Evidence and proofs | `data/proofs/` or accepted proof home | EvidenceBundle support, not stored here. |
| Release decisions | `release/` | Publication, correction, withdrawal, rollback, and cache invalidation authority. |

---

## Parent Invariant

> **Contract tests prove enforceability; they do not define authority.** A test can prove that a PersonAssertion-like object refuses to become canonical person truth, but the semantic contract still belongs under `contracts/`, the machine shape under `schemas/`, admissibility under `policy/`, and publication under `release/`.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Contract/schema split | Semantic meaning and machine shape remain separate. | validation failure / drift note. |
| Test/contract split | Tests do not become the only source of contract meaning. | validation failure / review block. |
| Source-role support | Contract-shaped fixtures preserve source identity, source role, rights, caveats, and permitted claim type. | validation failure / `ABSTAIN`. |
| Evidence closure | Evidence-dependent assertions require EvidenceRef-to-EvidenceBundle support before answer-like output. | `ABSTAIN`. |
| Living-person posture | Living-person or possibly-living assertions fail closed without accepted policy and consent support. | `DENY` / `ABSTAIN`. |
| DNA/genomic posture | DNA-linked or DNA-derived assertions deny or restrict by default unless policy supports a narrower outcome. | `DENY`. |
| Assertion boundary | Assertion-shaped objects do not become canonical identity, relationship truth, title truth, or public labels by shape alone. | validation failure / `ABSTAIN`. |
| Release boundary | Test success never becomes release approval, release manifest, public exposure, correction, withdrawal, or rollback. | promotion block. |
| No network | Default contract tests use synthetic local fixtures only. | validation failure / `ERROR`. |

---

## Lane Index

| Lane | Primary responsibility | Boundary |
|---|---|---|
| [`person-assertion/`](person-assertion/README.md) | PersonAssertion-like contract guardrails: source-scoped person assertions, identity separation, evidence closure, living-person/DNA posture, consent posture, release relationship, correction, withdrawal, and rollback. | Person assertion contract tests do not define the semantic contract, schema, person registry, consent store, or release decision. |

Additional contract test lanes may be added only when their semantic contract home, schema home, fixture posture, policy expectations, evidence expectations, release relationship, correction path, withdrawal path, and rollback target are explicit.

Potential future lanes:

| Lane | Proposed responsibility | Status |
|---|---|---|
| `relationship-assertion/` | Family, household, genetic, social, and land-linked relationship assertion boundaries. | PROPOSED / NEEDS VERIFICATION. |
| `land-relationship-assertion/` | Person-to-land assertions that prevent owner/title overclaim and parcel-boundary collapse. | PROPOSED / NEEDS VERIFICATION. |
| `consent-record/` | ConsentRecord-like contract behavior for scope, expiry, revocation, access role, and exposure class. | PROPOSED / NEEDS VERIFICATION. |
| `evidence-binding/` | EvidenceRef, EvidenceBundle, source-role, and citation closure expectations for People DNA Land assertions. | PROPOSED / NEEDS VERIFICATION. |
| `release-state/` | Release, correction, withdrawal, rollback, and cache-invalidation fields for public carrier eligibility. | PROPOSED / NEEDS VERIFICATION. |
| `temporal-posture/` | Valid time, source time, retrieval time, transaction time, review time, release time, and correction time requirements. | PROPOSED / NEEDS VERIFICATION. |

---

## Expected Test Families

The contract test family should eventually cover:

| Family | Expected proof point |
|---|---|
| Contract/schema split | Contract meaning does not drift into schema-only or test-only authority. |
| Assertion-first modeling | Person, relationship, consent, and land-linked records remain assertions with evidence and policy context. |
| Source-role integrity | Source roles, rights, caveats, and permitted claim types are explicit and non-interchangeable. |
| Evidence closure | EvidenceRef resolves to EvidenceBundle before answer-like or public carrier output. |
| Living-person protection | Living-person outputs fail closed unless policy, evidence, consent, review, and release support a bounded path. |
| DNA/genomic restriction | DNA-linked and DNA-derived outputs remain restricted or denied by default. |
| Consent posture | Consent scope, expiry, revocation, subject, purpose, role, and exposure class remain visible where material. |
| Temporal posture | Time fields remain distinct instead of collapsing into a single date label. |
| Release/correction/rollback | Public exposure requires release state, correction path, withdrawal path, rollback target, and cache invalidation posture. |
| No-network discipline | Default tests run from local synthetic fixtures, local schemas/contracts where available, and stubs only. |

---

## What Belongs Here

Appropriate contents include:

- deterministic no-network contract behavior tests;
- parent and child-lane README files;
- compact synthetic fixture pointers;
- tests that validate contract/schema/policy boundary expectations;
- source-role, evidence, temporal, consent, living-person, DNA/genomic, assertion, release, correction, withdrawal, and rollback gate checks;
- tests proving that contract-shaped objects do not become public truth by shape, parse success, schema pass, map rendering, graph projection, Focus text, or AI wording.

---

## Forbidden Shortcuts

Do not use this subtree to:

- define semantic contracts, machine schemas, policy rules, source descriptors, consent records, EvidenceBundle contracts, release decisions, public API behavior, public map behavior, renderer code, or production pipeline code;
- store real people records, real living-person records, real DNA/genomic data, real match lists, private family trees, provider exports, real consent records, deed/title records, assessor records, parcel data, credentials, source payloads, public tiles, proof artifacts, or release artifacts;
- call live genealogy providers, DNA services, consent systems, identity providers, people-search services, deed/title systems, assessor systems, parcel services, geocoders, or source systems by default;
- treat schema pass, contract wording, test success, source label, generated text, graph projection, map rendering, or tile availability as publication;
- publish, promote, approve, release, correct, withdraw, roll back, or cache-invalidate anything.

Any test that needs live provider access, production source data, real consent systems, real subject requests, production schemas, or public output belongs in a gated integration tier with explicit source admission, rights review, sensitivity review, policy decision, receipts, release controls, correction path, withdrawal path, and rollback targets.

---

## Run Posture

Parent contract test command:

```bash
pytest tests/domains/people-dna-land/contracts
```

Selected child-lane example:

```bash
pytest tests/domains/people-dna-land/contracts/person-assertion
```

Status of these commands: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted runner and that executable test modules exist. This README does not claim any command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; `contracts/` owns semantic meaning; `schemas/` owns machine-checkable shape; `policy/` owns allow/deny/restrict/abstain; domain-specific material belongs under `tests/domains/<domain>/`; `people-dna-land` is listed in the domain lane pattern. | Does not prove executable contract tests, accepted schema fields, validators, or contract implementation. |
| `person-assertion/README.md` | CONFIRMED upstream child lane | Existing child lane for PersonAssertion contract behavior under this contract test family. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | People/genealogy/DNA/land includes person assertions, genealogy, family relationships, DNA/genomics, land ownership assertions, and living-person/DNA restrictions; validation includes contract checks; DNA/living-person public default is denied. | Does not prove runtime implementation, executable tests, fixtures, validators, CI, or pass rates exist in this workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | People/DNA/land should use assertion-first modeling with evidence, source role, temporal scope, confidence, review state, and policy posture rather than flattened labels; public-safe defaults fail closed for living-person/DNA and unclear evidence or rights. | Does not define final People DNA Land contract schemas, jurisdiction-specific privacy law, production policy, or storage location for consent records. |
| Adjacent `people-dna-land` test README files | CONFIRMED upstream pattern | Existing sibling lanes use KFM Meta Block v2, impact badges, placement basis, no-network posture, lane index, finite outcomes, validation checklist, and rollback sections. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| GitHub target file before this update | CONFIRMED | Existing `tests/domains/people-dna-land/contracts/README.md` contained only `y`, so no substantive content was available to preserve. | Placeholder content did not prove implementation or doctrine. |

---

## Validation Checklist

- [ ] Executable contract tests exist under documented child lanes.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic contract fixtures exist in the accepted fixture home.
- [ ] Semantic contracts exist in the accepted contract home or test expectations are safely stubbed.
- [ ] Machine schemas exist in the accepted schema home or schema checks are safely stubbed.
- [ ] Source role, evidence posture, temporal posture, living-person posture, DNA/genomic posture, relationship posture, consent posture, sensitivity posture, review state, release state, correction path, withdrawal path, and rollback fields are accepted by schemas or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] Contract tests distinguish semantic meaning, machine shape, policy decision, evidence closure, release approval, and publication.
- [ ] CI runs this no-network contract test family or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this contract test family becomes a semantic contract root, schema authority, policy authority, live provider connector, lifecycle data store, person registry, genealogy graph authority, consent database, land-title registry, source registry, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback is also required if tests or documentation treat contract shape, schema pass, test success, generated text, map rendering, graph projection, or tile availability as truth, source admission, evidence closure, living-person clearance, DNA clearance, release approval, or deletion authority without explicit evidence, policy, review, release, correction, withdrawal, and rollback support.

<p align="right"><a href="#top">Back to top</a></p>
