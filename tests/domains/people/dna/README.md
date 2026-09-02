<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-readme
title: People DNA Test Lane README
type: test-lane-readme
version: v0.1
status: draft; directory-created-in-scratch; dna-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People domain steward
  - OWNER_TBD - DNA / genomic policy steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people; dna; genomic; living-person-sensitive; default-deny; no-network; evidence-bound; release-gated; rollback-aware
tags: [kfm, tests, people, dna, genomics, genealogy, living-person, privacy, consent, relationship-hypothesis, EvidenceBundle, PolicyDecision, RedactionReceipt, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../../README.md
  - ../../../../docs/domains/people/
  - ../../../../docs/domains/people-dna-land/
  - ../../../../contracts/domains/people/
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/domains/people/
  - ../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../policy/domains/people/
  - ../../../../policy/domains/people-dna-land/
  - ../../../../fixtures/domains/people/dna/
  - ../../../../fixtures/domains/people-dna-land/dna/
  - ../../../../data/registry/sources/people/
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../release/manifests/people/
  - ../../../../release/manifests/people-dna-land/
notes:
  - "This README creates the local lane requested at tests/domains/people/dna/README.md."
  - "Directory Rules place enforceability proof under tests/ and domain-specific material under tests/domains/<domain>/."
  - "The exact canonical domain naming for this lane is NEEDS VERIFICATION because attached doctrine also names people-dna-land as a domain pattern."
  - "This is a test-lane README only. It does not define People doctrine, DNA policy, privacy policy, contracts, schemas, fixtures, consent records, EvidenceBundles, release decisions, public API material, public map material, public tiles, or published artifacts."
  - "Default posture is deterministic and no-network. Live genealogy providers, DNA services, real genomic data, living-person records, consent databases, source exports, and public release artifacts do not belong in this lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People DNA tests

> Deterministic, no-network test documentation for proving that living-person, DNA, genomic, relationship, identity, consent, evidence, policy, redaction, release, correction, and rollback guardrails fail closed before any public carrier.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people" src="https://img.shields.io/badge/domain-people-blue">
  <img alt="Lane: dna" src="https://img.shields.io/badge/lane-dna-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Posture: default deny" src="https://img.shields.io/badge/posture-default__deny-critical">
</p>

**Path:** `tests/domains/people/dna/README.md`  
**Status:** draft / directory-created-in-scratch / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people`  
**Test lane:** `dna`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof and that domain-specific files belong under `tests/domains/<domain>/`; CONFIRMED by attached doctrine that living-person and DNA-derived outputs are denied or restricted by default; NEEDS VERIFICATION for the canonical domain naming choice between `people/dna` and `people-dna-land/dna`, executable tests, fixtures, schemas, validators, policy runtime, consent records, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people/dna/` is the requested test lane for People-domain DNA and genomic guardrails.

This lane should prove that KFM does not treat DNA, genomic, DNA-derived relationship hypotheses, living-person identity assertions, or consent-sensitive person assertions as ordinary public knowledge. Tests here should verify finite outcomes such as `DENY`, `ABSTAIN`, or fail-closed `ERROR` when evidence, consent, rights, sensitivity review, policy clearance, release state, correction path, or rollback target is missing.

A passing test here should **not** mean that DNA data is admitted, a person relationship is true, a living-person assertion is publishable, a genealogy provider is authorized, a consent record is valid, or a public layer/API answer is approved. It should mean only that the scoped guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable. They also require domain-specific material to appear as a segment inside the responsibility root, such as `tests/domains/<domain>/`.

This file therefore belongs to the test responsibility root, with `people` as the requested domain segment and `dna` as the child test lane.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| DNA / genomic enforceability tests | `tests/domains/people/dna/` | This directory. |
| Reusable synthetic fixtures | `fixtures/domains/people/dna/` or accepted repo fixture home | Referenced by tests, not duplicated as authority. |
| Semantic contracts | `contracts/domains/people/` or accepted people/DNA domain home | Meaning source, not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/people/` or accepted people/DNA domain home | Shape checks where accepted. |
| Policy rules | `policy/domains/people/` or accepted people/DNA domain home | Allow, deny, restrict, abstain source of truth. |
| Source descriptors | `data/registry/sources/people/` or accepted people/DNA source registry home | Source identity, rights, cadence, consent, caveats. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

**Naming note:** attached KFM doctrine also identifies `people-dna-land` as a domain pattern. If the canonical domain is later resolved to `people-dna-land`, migrate this lane to `tests/domains/people-dna-land/dna/` with a drift note, redirect README, or ADR-backed path decision.

---

## Invariant Under Test

> **DNA and living-person assertions are high-sensitivity, policy-gated assertions.** Evidence is necessary but not sufficient for public exposure. Consent, source role, living-person posture, relationship confidence, rights, sensitivity review, policy decision, release state, correction path, and rollback target must remain explicit.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Living-person default deny | Living-person DNA-derived identity or relationship output is denied unless an accepted policy path permits it. | `DENY`. |
| DNA/genomic sensitivity | DNA or genomic derivation is visible as a sensitivity label and not collapsed into ordinary genealogy. | validation failure / `DENY`. |
| Consent posture | Missing, expired, insufficient, or scope-mismatched consent blocks public exposure. | `DENY` / `ABSTAIN`. |
| Evidence closure | EvidenceRef must resolve to an admissible EvidenceBundle before answer-like output. | `ABSTAIN`. |
| Relationship confidence | Hypotheses remain hypotheses and are not promoted to canonical person truth by wording, UI, or schema pass. | validation failure / `ABSTAIN`. |
| Source role | Test fixtures preserve source role, rights posture, terms, caveats, and permitted claim types. | validation failure. |
| Redaction/generalization | Public-safe derivatives use named transforms and receipts, not improvised UI or AI masking. | validation failure / `DENY`. |
| Release boundary | Test success never becomes release approval or public exposure. | promotion block. |
| No network | Default tests do not call genealogy providers, DNA services, people search services, or consent systems. | validation failure / `ERROR`. |

---

## Expected Scope

Tests in this lane may validate:

- denial of living-person DNA-derived identity assertions without explicit authorized policy support;
- abstention when EvidenceRef cannot resolve to an admissible EvidenceBundle;
- rejection of fixtures that convert DNA match strength into certain family relationship truth;
- consent-scope checks for purpose, subject, time, access role, and public exposure class;
- rights and source-terms checks for DNA or genealogy provider material;
- redaction receipt requirements for any public-safe derivative;
- release, correction, withdrawal, and rollback preconditions for sensitive assertions;
- no-network behavior for the default suite.

Out of scope for the default suite:

- real DNA files, raw genotype files, genome sequences, match lists, living-person records, private family trees, provider exports, scraped people-search data, production consent systems, credentials, API calls, public tiles, public layers, or published artifacts.

---

## Fixture Posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- small enough for PR review;
- clearly labeled as synthetic;
- no real names, real DNA data, real living-person relationships, real private family trees, real provider exports, credentials, or production identifiers;
- explicit expected outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- explicit source role, evidence posture, living-person status posture, DNA/genomic derivation posture, consent posture, policy state, redaction posture, release relationship, correction path, and rollback target where material.

---

## Finite Outcomes

| Condition | Expected outcome |
|---|---|
| Synthetic historical person assertion has released evidence and no living-person/DNA sensitivity | possible `ANSWER`, only if policy and release are satisfied. |
| Living-person DNA-derived identity assertion lacks authorized policy support | `DENY`. |
| DNA relationship hypothesis lacks admissible evidence or confidence support | `ABSTAIN`. |
| Consent is missing, expired, mismatched, or not public-exposure scoped | `DENY` / `ABSTAIN`. |
| Source terms or redistribution rights are unknown | `DENY` / `ABSTAIN`. |
| EvidenceRef cannot resolve to EvidenceBundle | `ABSTAIN`. |
| Policy engine or consent validator is unavailable | `ERROR` / fail closed. |
| Test attempts live provider access in default lane | validation failure / `ERROR`. |
| Release state, correction path, or rollback target is missing for public exposure | promotion-blocking failure. |

---

## Suggested Layout

```text
tests/domains/people/dna/
|-- README.md
|-- test_living_person_dna_default_denies.py
|-- test_dna_derivation_label_required.py
|-- test_consent_scope_required.py
|-- test_relationship_hypothesis_not_canonical_truth.py
|-- test_evidence_bundle_required.py
|-- test_source_rights_and_terms_fail_closed.py
|-- test_redaction_receipt_required.py
|-- test_release_correction_rollback_required.py
`-- test_no_network_provider_access.py
```

---

## Run Posture

```bash
pytest tests/domains/people/dna
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; domain-specific material belongs under `tests/domains/<domain>/`; domains must not become root folders. | Does not settle whether the canonical domain segment should be `people`, `people-dna-land`, or another accepted lane name. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | Public clients use governed APIs and released artifacts; living-person and DNA-derived outputs are denied/restricted by default; sensitivity gates include living-person and DNA. | Does not prove executable tests, fixtures, validators, or policy runtime exist in this workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | DNA/genomic/living-person outputs should be restricted by default; first fixture should show `ABSTAIN` or `DENY` for unauthorized living-person DNA-derived identity or relationship assertions. | Does not define jurisdiction-specific privacy law or production policy. |
| `maplibre3d.md` | CONFIRMED doctrine / PROPOSED realization | Living-person data and DNA-linked locations do not enter terrain-anchored or true-3D scenes by default. | 3D-specific; not a full People/DNA test contract. |
| Current workspace | CONFIRMED | This README was created locally at the requested path. | Workspace is sparse and not a full verified repository checkout; CI and pass rates are UNKNOWN. |

---

## Validation Checklist

- [ ] Canonical domain path is resolved: `tests/domains/people/dna/` versus `tests/domains/people-dna-land/dna/`.
- [ ] Executable tests exist under the accepted lane.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic fixtures exist in the accepted fixture home.
- [ ] DNA/genomic derivation, living-person posture, consent posture, source role, and public-exposure class fields are accepted by schemas or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network People DNA suite or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live DNA/genealogy connector, provider export store, consent database, person registry, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

If canonical naming resolves to `people-dna-land`, move this README and any tests under the accepted path with an ADR, migration note, or redirect README so the repo does not split People/DNA governance across parallel authorities.

<p align="right"><a href="#top">Back to top</a></p>
