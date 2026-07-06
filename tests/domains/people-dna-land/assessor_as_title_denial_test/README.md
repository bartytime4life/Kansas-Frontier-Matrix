<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-readme
title: People Domain Tests README
type: test-index-readme
version: v0.1
status: draft; directory-created-in-scratch; parent-index; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People domain steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Identity steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people; parent-index; living-person-sensitive; dna-sensitive; default-deny; no-network; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, people, genealogy, dna, genomics, living-person, identity, privacy, consent, relationship-hypothesis, land-relationship, EvidenceBundle, PolicyDecision, RedactionReceipt, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../README.md
  - dna/README.md
  - ../../../docs/domains/people/
  - ../../../docs/domains/people-dna-land/
  - ../../../contracts/domains/people/
  - ../../../contracts/domains/people-dna-land/
  - ../../../schemas/contracts/v1/domains/people/
  - ../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../policy/domains/people/
  - ../../../policy/domains/people-dna-land/
  - ../../../fixtures/domains/people/
  - ../../../fixtures/domains/people-dna-land/
  - ../../../data/registry/sources/people/
  - ../../../data/registry/sources/people-dna-land/
  - ../../../release/manifests/people/
  - ../../../release/manifests/people-dna-land/
notes:
  - "This README creates the local parent index requested at tests/domains/people/README.md."
  - "Directory Rules place enforceability proof under tests/ and domain-specific material under tests/domains/<domain>/."
  - "The exact canonical domain naming for people, DNA, genealogy, and land-relationship tests is NEEDS VERIFICATION because attached doctrine also names people-dna-land as a domain pattern."
  - "This is a parent test index only. It does not define People doctrine, contracts, schemas, fixtures, source descriptors, consent records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "Default posture is deterministic and no-network. Live genealogy providers, DNA services, people-search services, real living-person records, consent databases, source exports, and public release artifacts do not belong in default People tests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People domain tests

> Parent index for People-domain test lanes. These tests should prove enforceable privacy, identity, consent, evidence, policy, redaction, release, correction, and rollback boundaries without turning tests into a person registry, source feed, consent authority, release authority, public surface, or generated truth source.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people" src="https://img.shields.io/badge/domain-people-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Posture: default deny" src="https://img.shields.io/badge/posture-default__deny-critical">
  <img alt="Boundary: tests not release" src="https://img.shields.io/badge/boundary-tests__not__release-success">
</p>

**Path:** `tests/domains/people/README.md`  
**Status:** draft / directory-created-in-scratch / parent index / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof and that domain-specific files belong under `tests/domains/<domain>/`; CONFIRMED by attached doctrine that living-person and DNA-derived outputs are denied or restricted by default; CONFIRMED current local child lane exists at `tests/domains/people/dna/README.md`; NEEDS VERIFICATION for canonical domain naming between `people` and `people-dna-land`, executable test modules, fixtures, schemas, validators, policy runtime, consent records, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people/` is the requested People-domain segment of the KFM test tree.

Its job is to prove that People-related assertions remain evidence-bound, source-role-aware, consent-aware, privacy-aware, and policy-gated before public exposure. This includes person identity assertions, genealogy assertions, relationship hypotheses, living-person posture, DNA/genomic derivation, land-relationship context, redaction/generalization, release state, correction path, and rollback targets.

A passing test in this subtree should **not** mean that a real person assertion is true, a living-person record is publishable, a DNA-derived relationship is proven, a consent record is valid, a source is admitted, a public layer is safe, or a release is approved. It should mean only that the scoped guardrail behaved as expected against bounded fixtures and local files.

---

## Parent Invariant

> **People tests prove enforceability; they do not become People authority.** The subtree may validate People contracts, schemas, fixtures, source descriptors, consent posture, relationship-confidence handling, privacy gates, redaction receipts, release readiness, correction, and rollback, but it must not become a person registry, genealogy source, DNA provider adapter, consent database, proof store, policy root, release root, public API/map/tile surface, or generated truth surface.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Living-person posture | Living-person assertions are denied, restricted, or abstained unless an accepted policy path permits exposure. | `DENY` / `ABSTAIN`. |
| DNA/genomic sensitivity | DNA and genomic derivation remain visible and default-deny for public exposure. | `DENY` / validation failure. |
| Identity separation | Person assertions, relationship hypotheses, canonical identity, land records, and generated summaries do not collapse into one truth object. | validation failure / `ABSTAIN`. |
| Consent posture | Consent scope, subject, purpose, access role, time, and public-exposure class are explicit where material. | `DENY` / `ABSTAIN`. |
| Source role and rights | Source identity, source role, rights, terms, caveats, and permitted claims remain visible. | validation failure / `ABSTAIN`. |
| Evidence support | Evidence-dependent People claims resolve support or return a finite non-answer. | `ABSTAIN`. |
| Redaction posture | Public-safe transforms are named, deterministic, receipt-backed, and not improvised at the UI or AI edge. | validation failure / `DENY`. |
| Release boundary | Test success does not become release approval, release manifest, correction notice, or rollback card. | promotion block. |
| No network | Default People tests use local synthetic fixtures only. | validation failure / `ERROR`. |

---

## Lane Index

| Lane | Primary responsibility | Boundary |
|---|---|---|
| [`dna/`](dna/README.md) | DNA, genomic, living-person, consent, relationship-hypothesis, redaction, release, correction, and rollback guardrail tests. | DNA tests do not admit real DNA data, prove relationships, authorize consent, call providers, or approve publication. |

Additional People lanes may be added only when their responsibility is clear and their fixture, policy, evidence, release, correction, and rollback boundaries are explicit.

Potential future lanes:

| Lane | Proposed responsibility | Status |
|---|---|---|
| `identity/` | Person assertion identity, alias, disambiguation, and living-status tests. | PROPOSED / NEEDS VERIFICATION. |
| `genealogy/` | Genealogy relationship assertion tests that keep source role, confidence, and evidence support visible. | PROPOSED / NEEDS VERIFICATION. |
| `consent/` | Consent scope, expiry, subject, purpose, access-role, and public-exposure checks. | PROPOSED / NEEDS VERIFICATION. |
| `policy/` | People-domain policy finite-outcome tests. | PROPOSED / NEEDS VERIFICATION. |
| `redaction/` | People public-safe transform and receipt tests. | PROPOSED / NEEDS VERIFICATION. |
| `sources/` | People/genealogy source descriptor, rights, terms, cadence, and permitted-claims tests. | PROPOSED / NEEDS VERIFICATION. |

---

## Expected Test Families

The People test subtree should eventually cover these trust families:

| Family | Expected proof point |
|---|---|
| Person assertion identity | Identity remains deterministic, source-scoped, time-aware, and separate from generated text or display labels. |
| Living-person privacy | Living-person records fail closed unless policy, consent, rights, evidence, review, and release allow a bounded exposure. |
| DNA/genomic restriction | DNA-derived identity or relationship output is denied or restricted by default. |
| Relationship hypotheses | Relationship confidence, evidence role, uncertainty, and review state remain visible. |
| Consent and access | Consent is scoped to subject, purpose, role, time, derivation, and exposure class. |
| Source rights and terms | SourceDescriptor-like fixtures carry rights, attribution, redistribution, provider terms, caveats, and permitted claim types. |
| Evidence closure | EvidenceRef resolves to EvidenceBundle before answer-like output, otherwise the system abstains. |
| Redaction/generalization | Public-safe transforms emit receipts and preserve withheld-count or residual-risk posture where material. |
| Release/correction/rollback | Public exposure requires release state, correction path, withdrawal path, rollback target, and cache invalidation posture. |
| No-network discipline | Default tests run from local synthetic fixtures, local schema/contract files, and stubs only. |

---

## What Belongs Here

Appropriate contents include:

- deterministic no-network tests;
- compact synthetic fixture pointers;
- import and schema smoke checks;
- source-role and permitted-claims checks;
- living-person, DNA/genomic, consent, privacy, and redaction policy checks;
- evidence, release, correction, withdrawal, and rollback gate checks;
- child-lane README files that explain scope, limits, validation posture, and rollback.

---

## Forbidden Shortcuts

Do not use this subtree to:

- fetch live genealogy, DNA, people-search, assessor, tax, parcel, or identity-provider systems by default;
- store real people records, real DNA/genomic data, real match lists, private family trees, provider exports, consent records, source payloads, public tiles, proof artifacts, or release artifacts;
- redefine People doctrine, contracts, schemas, source registries, policy rules, consent rules, release decisions, renderer code, or production pipeline code;
- infer publication from file existence, source label, test success, schema pass, map rendering, tile availability, Focus answer text, or AI wording;
- publish, promote, approve, release, correct, withdraw, or roll back anything.

Any test that needs live provider access, production source data, real consent systems, connector execution, or public output belongs in a gated integration tier with explicit source admission, rights review, sensitivity review, policy decision, receipts, release controls, correction path, and rollback targets.

---

## Run Posture

Parent subtree smoke command:

```bash
pytest tests/domains/people
```

Selected child-lane example:

```bash
pytest tests/domains/people/dna
```

Status of these commands: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted runner and that executable test modules exist. This README does not claim any command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; domain-specific material belongs under `tests/domains/<domain>/`; domains must not become root folders. | Does not settle whether canonical People/DNA tests should use `people`, `people-dna-land`, or another accepted domain segment. |
| `tests/domains/people/dna/README.md` | CONFIRMED local file | Existing child lane for DNA/genomic/living-person guardrails under the requested People path. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | Public clients use governed APIs and released artifacts; living-person and DNA-derived outputs are denied/restricted by default; sensitivity gates include living-person and DNA. | Does not prove runtime implementation in this sparse workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | People/genealogy/DNA/land lane should restrict living-person, DNA, genomic, and DNA-derived outputs by default and use `ABSTAIN` or `DENY` for unauthorized requests. | Does not define jurisdiction-specific privacy law or production policy. |
| `maplibre3d.md` | CONFIRMED doctrine / PROPOSED realization | Living-person data and DNA-linked locations do not enter terrain-anchored or true-3D scenes by default. | 3D-specific; not a full People test contract. |
| Current workspace | CONFIRMED | This parent README was created locally at the requested path. | Workspace is sparse and not a full verified repository checkout; CI and pass rates are UNKNOWN. |

---

## Validation Checklist

Before treating this parent README as implemented behavior, verify:

- [ ] Canonical domain path is resolved: `tests/domains/people/` versus `tests/domains/people-dna-land/`.
- [ ] Executable tests exist for documented lanes or the lane is explicitly documentation-only.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic fixtures exist in accepted fixture homes and are not source payloads.
- [ ] Person identity, living-person posture, DNA/genomic derivation, consent posture, source role, rights, public-exposure class, redaction posture, release state, correction path, and rollback fields are accepted by schemas or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network People suite or marks incomplete lanes as expected gaps.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this parent lane becomes a live provider fetcher, connector implementation, lifecycle data store, person registry, DNA provider export store, consent database, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

If canonical naming resolves to `people-dna-land`, move this README and child lanes under the accepted path with an ADR, migration note, or redirect README so the repo does not split People/DNA governance across parallel authorities.

<p align="right"><a href="#top">Back to top</a></p>
