<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-contracts-person-assertion-readme
title: People DNA Land Person Assertion Contract Tests README
type: test-lane-readme
version: v0.1
status: draft; directory-created-in-scratch; contract-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People DNA Land domain steward
  - OWNER_TBD - Contract steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people-dna-land; contracts; person-assertion; living-person-sensitive; dna-sensitive; no-network; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, people-dna-land, contracts, person-assertion, person-record, identity, genealogy, living-person, dna, consent, source-role, EvidenceBundle, PolicyDecision, ConsentRecord, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../consent/README.md
  - ../../connectors/README.md
  - ../../assessor_as_title_denial_test/README.md
  - ../../chain_of_title_gap_test/README.md
  - ../../../../../docs/domains/people-dna-land/
  - ../../../../../docs/domains/people-dna-land/land-ownership/
  - ../../../../../contracts/domains/people-dna-land/
  - ../../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../../policy/domains/people-dna-land/
  - ../../../../../fixtures/domains/people-dna-land/contracts/person-assertion/
  - ../../../../../data/registry/sources/people-dna-land/
  - ../../../../../release/manifests/people-dna-land/
notes:
  - "This README replaces the placeholder content at tests/domains/people-dna-land/contracts/person-assertion/README.md."
  - "Directory Rules place enforceability proof under tests/, semantic meaning under contracts/, machine shape under schemas/, policy decisions under policy/, and people-dna-land as a domain lane pattern."
  - "This is a contract test-lane README only. It does not define the PersonAssertion contract, schema, policy, consent record, source descriptor, EvidenceBundle, person registry, release decision, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that a person assertion remains a source-scoped, evidence-bound, policy-gated assertion; it is not canonical person truth, relationship truth, living-person clearance, DNA clearance, release approval, or publication."
  - "Default posture is deterministic and no-network. Real people records, living-person records, DNA data, genealogy provider exports, consent records, source exports, credentials, and public release artifacts do not belong in this lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Person assertion contract tests

> Deterministic, no-network test documentation for proving that People DNA Land person assertions stay source-scoped, evidence-bound, time-aware, consent-aware, policy-gated, and release-gated instead of becoming canonical person truth or public exposure by contract shape alone.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: contract tests" src="https://img.shields.io/badge/lane-contract__tests-purple">
  <img alt="Object: person assertion" src="https://img.shields.io/badge/object-person__assertion-informational">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/domains/people-dna-land/contracts/person-assertion/README.md`  
**Status:** draft / directory-created-in-scratch / person-assertion contract test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane:** `contracts/person-assertion`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof, `contracts/` is the semantic contract root, `schemas/` is the machine-shape root, `policy/` decides allow/deny/restrict/abstain, and `people-dna-land` is a domain lane pattern; CONFIRMED by attached doctrine that person assertions, genealogy, family relationships, DNA/genomics, living-person posture, source roles, evidence closure, and release state are high-risk People DNA Land concerns; NEEDS VERIFICATION for the accepted PersonAssertion contract, schema fields, executable tests, fixtures, validators, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/contracts/person-assertion/` is the requested test lane for PersonAssertion contract behavior.

This lane should prove that a PersonAssertion-like object expresses **who or what source asserts something about a person-like subject**, under what evidence, source role, temporal scope, confidence posture, sensitivity posture, consent posture, review state, and release relationship. The object shape must not flatten source-scoped assertions into canonical person identity, family relationship truth, DNA-derived truth, living-person clearance, land relationship truth, or public labels.

A passing test here should **not** mean that a real person exists, a living-person record is publishable, a family relationship is true, a DNA-derived relationship is allowed, a source is admitted, a consent record is valid, or a release is approved. It should mean only that the scoped contract guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable. They place semantic meaning under `contracts/`, machine-checkable shape under `schemas/`, policy decisions under `policy/`, and domain-specific material under a responsibility-root lane such as `tests/domains/<domain>/`.

This path is therefore a **test lane** for a contract family, not the semantic contract itself.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| PersonAssertion contract tests | `tests/domains/people-dna-land/contracts/person-assertion/` | This directory. |
| PersonAssertion semantic contract | `contracts/domains/people-dna-land/` | Defines meaning and invariants; not owned here. |
| PersonAssertion machine schema | `schemas/contracts/v1/domains/people-dna-land/` | Defines accepted shape where available. |
| Policy rules | `policy/domains/people-dna-land/` | Decides allow, deny, restrict, abstain, redact, and release behavior. |
| Reusable synthetic fixtures | `fixtures/domains/people-dna-land/contracts/person-assertion/` | Preferred fixture home if populated. |
| Source descriptors | `data/registry/sources/people-dna-land/` | Source identity, rights, role, caveats, consent obligations, and permitted claim types. |
| Consent records | Accepted consent-record home after repo inspection | NEEDS VERIFICATION; not stored in this test lane. |
| Evidence and proofs | `data/proofs/` or accepted proof home | EvidenceBundle support, not stored here. |
| Release decisions | `release/` | Publication, correction, withdrawal, rollback, and cache invalidation authority. |

---

## Invariant Under Test

> **A person assertion is not a canonical person.** It is a bounded assertion with source role, evidence posture, temporal scope, confidence, review state, consent posture, sensitivity posture, and release relationship. Contract success cannot publish it, collapse it into identity truth, or bypass living-person and DNA policy.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Assertion/object separation | PersonAssertion-like fixtures remain separate from canonical person identity or display labels. | validation failure / `ABSTAIN`. |
| Source-role support | Source identity, source role, rights posture, caveats, and permitted claim type remain explicit. | validation failure / `ABSTAIN`. |
| Evidence closure | Evidence-dependent person claims require EvidenceRef-to-EvidenceBundle support before answer-like output. | `ABSTAIN`. |
| Living-person posture | Living-person or possibly-living assertions fail closed without accepted policy and consent support. | `DENY` / `ABSTAIN`. |
| DNA/genomic posture | DNA-linked or DNA-derived assertions remain restricted or denied by default unless policy supports a narrower outcome. | `DENY`. |
| Relationship boundary | Parent, spouse, child, household, genetic, or land relationship assertions are not promoted to relationship truth by person assertion shape. | validation failure / `ABSTAIN`. |
| Temporal posture | asserted time, source time, retrieval time, valid time, review time, release time, and correction time remain distinct where material. | validation failure. |
| Public wording | Public labels do not upgrade "asserted person" into "confirmed person", "owner", "ancestor", or "DNA match" without release support. | `DENY` / validation failure. |
| Release boundary | Test success never becomes release approval, release manifest, public exposure, correction, withdrawal, or rollback. | promotion block. |
| No network | Default tests do not call genealogy providers, DNA services, consent systems, identity providers, people-search services, or land systems. | validation failure / `ERROR`. |

---

## Expected Scope

Tests in this lane may validate:

- valid synthetic PersonAssertion-like fixtures carry source role, evidence posture, temporal scope, confidence, review state, sensitivity posture, consent posture, and release relationship;
- invalid fixtures fail when person assertion objects omit source role, evidence refs, temporal scope, living-person posture, DNA/genomic posture, consent posture, or release state where material;
- assertion objects do not become canonical person records, relationship truth, genealogy truth, land-title truth, public labels, graph truth, or Focus Mode answer text by shape alone;
- living-person and DNA-linked assertions deny or abstain by default without accepted policy support;
- source citations or connector outputs do not become EvidenceBundles automatically;
- consent scope and revocation states block public exposure where applicable;
- release, correction, withdrawal, cache invalidation, and rollback preconditions remain visible before public carrier use;
- no-network behavior for the default suite.

Out of scope for the default suite:

- real people records, real living-person records, real DNA/genomic data, real family trees, real genealogy provider exports, real consent records, real relationship graphs, real deed/title records, assessor records, parcel data, credentials, external API calls, public tiles, public layers, and published artifacts.

---

## Fixture Posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- small enough for PR review;
- clearly labeled as synthetic;
- no real names, real people, real family trees, real DNA data, real provider IDs, real living-person relationships, real addresses, real parcel numbers, credentials, or production identifiers;
- explicit expected outcome: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or validation failure;
- explicit source role, assertion type, evidence posture, temporal posture, living-person posture, DNA/genomic posture, relationship posture, consent posture, sensitivity posture, review state, release relationship, correction path, withdrawal path, and rollback target where material.

---

## Finite Outcomes

| Condition | Expected outcome |
|---|---|
| Synthetic historical assertion has released evidence and no living-person/DNA sensitivity | possible accepted support only, if policy and release are satisfied. |
| PersonAssertion lacks source role or permitted claim type | validation failure / `ABSTAIN`. |
| EvidenceRef cannot resolve to EvidenceBundle | `ABSTAIN`. |
| Living-person assertion lacks authorized policy and consent support | `DENY` / `ABSTAIN`. |
| DNA-linked assertion lacks authorized policy support | `DENY`. |
| Assertion is used as canonical person identity | validation failure / `ABSTAIN`. |
| Assertion is used as confirmed relationship truth | validation failure / `ABSTAIN`. |
| Assertion is used as owner/title truth | `DENY` / `ABSTAIN`. |
| Public label upgrades asserted identity into confirmed identity | validation failure / `DENY`. |
| Release state, correction path, withdrawal path, or rollback target is missing for public exposure | promotion-blocking failure. |
| Test attempts live provider, consent, DNA, people-search, assessor, parcel, deed, or title access | validation failure / `ERROR`. |

---

## Suggested Layout

```text
tests/domains/people-dna-land/contracts/person-assertion/
|-- README.md
|-- test_person_assertion_requires_source_role.py
|-- test_person_assertion_requires_evidence_ref.py
|-- test_person_assertion_not_canonical_person.py
|-- test_living_person_assertion_denies_by_default.py
|-- test_dna_linked_assertion_denies.py
|-- test_relationship_claim_not_confirmed_by_person_assertion.py
|-- test_land_owner_like_label_not_confirmed_by_person_assertion.py
|-- test_consent_and_revocation_posture_required.py
|-- test_release_correction_withdrawal_rollback_required.py
`-- test_no_network_person_assertion_contract.py
```

---

## Run Posture

```bash
pytest tests/domains/people-dna-land/contracts/person-assertion
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; `contracts/` owns semantic meaning; `schemas/` owns machine-checkable shape; `policy/` owns allow/deny/restrict/abstain; domain-specific material belongs under `tests/domains/<domain>/`; `people-dna-land` is listed in the domain lane pattern. | Does not prove executable PersonAssertion tests, accepted schema fields, or contract implementation. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | People/genealogy/DNA/land includes person assertions, genealogy, family relationships, DNA/genomics, land ownership assertions, and living-person/DNA restrictions; DNA/living-person data published by default is denied. | Does not prove runtime implementation, executable tests, fixtures, validators, CI, or pass rates exist in this workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | People/DNA/land should use assertion-first modeling with evidence, source role, temporal scope, confidence, review state, and policy posture rather than flattened labels; public-safe defaults fail closed for living-person/DNA and unclear evidence or rights. | Does not define the final PersonAssertion schema, jurisdiction-specific privacy law, production policy, or storage location for consent records. |
| Adjacent `people-dna-land` test README files | CONFIRMED upstream pattern | Existing sibling lanes use KFM Meta Block v2, impact badges, placement basis, no-network posture, finite outcomes, validation checklist, and rollback sections. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| GitHub target file before this update | CONFIRMED | Existing `tests/domains/people-dna-land/contracts/person-assertion/README.md` contained only `y`, so no substantive content was available to preserve. | Placeholder content did not prove implementation or doctrine. |

---

## Validation Checklist

- [ ] Parent `tests/domains/people-dna-land/contracts/README.md` exists as a real index or is replaced from placeholder content.
- [ ] Executable tests exist under this lane.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic PersonAssertion fixtures exist in the accepted fixture home.
- [ ] PersonAssertion semantic contract exists in the accepted contract home or test expectations are safely stubbed.
- [ ] PersonAssertion machine schema exists in the accepted schema home or schema checks are safely stubbed.
- [ ] Source role, evidence posture, temporal posture, living-person posture, DNA/genomic posture, relationship posture, consent posture, sensitivity posture, review state, release state, correction path, withdrawal path, and rollback fields are accepted by schemas or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs this no-network PersonAssertion contract test lane or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a semantic contract root, schema authority, policy authority, live provider connector, lifecycle data store, person registry, genealogy graph authority, consent database, land-title registry, source registry, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback is also required if tests or documentation treat PersonAssertion shape as canonical person truth, relationship truth, DNA-derived truth, living-person clearance, land/title truth, source admission, evidence closure, release approval, or deletion authority without explicit evidence, policy, review, release, correction, withdrawal, and rollback support.

<p align="right"><a href="#top">Back to top</a></p>
