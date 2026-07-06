<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-connectors-readme
title: People DNA Land Connector Tests README
type: test-index-readme
version: v0.1
status: draft; directory-created-in-scratch; connector-test-index; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People DNA Land domain steward
  - OWNER_TBD - Connector steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people-dna-land; connectors; parent-index; living-person-sensitive; dna-sensitive; no-network; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, people-dna-land, connectors, source-intake, genealogy, gedcom, living-person, dna, consent, source-role, EvidenceBundle, PolicyDecision, SourceIntakeRecord, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - gedcom/README.md
  - ../../../../docs/domains/people-dna-land/
  - ../../../../docs/domains/people-dna-land/land-ownership/
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../policy/domains/people-dna-land/
  - ../../../../fixtures/domains/people-dna-land/connectors/
  - ../../../../connectors/people-dna-land/
  - ../../../../data/registry/sources/people-dna-land/
  - ../../../../release/manifests/people-dna-land/
notes:
  - "This README creates the local connector-test parent index requested at tests/domains/people-dna-land/connectors/README.md."
  - "Directory Rules place enforceability proof under tests/, source-specific fetcher/admitter implementation under connectors/, and people-dna-land as a domain lane pattern."
  - "This is a connector test index only. It does not define connector implementation, People DNA Land doctrine, contracts, schemas, fixtures, source descriptors, genealogy records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested parent invariant is that People DNA Land connectors produce candidate intake and finite outcomes only; connector success is not truth, source admission, consent clearance, living-person clearance, DNA clearance, release approval, or publication."
  - "Default posture is deterministic and no-network. Live genealogy providers, GEDCOM exports, DNA services, deed/title/assessor systems, people-search services, source exports, credentials, and public release artifacts do not belong in default connector tests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People DNA Land connector tests

> Parent index for no-network connector behavior tests in the People DNA Land domain. These tests should prove source-intake guardrails without becoming connector implementation, source truth, release authority, or public surface.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: connector tests" src="https://img.shields.io/badge/lane-connector__tests-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not connectors" src="https://img.shields.io/badge/boundary-tests__not__connectors-success">
</p>

**Path:** `tests/domains/people-dna-land/connectors/README.md`  
**Status:** draft / directory-created-in-scratch / connector test parent index / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane family:** `connectors`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof, `connectors/` is the canonical root for source-specific fetcher/admitter implementation, and `people-dna-land` is a domain lane pattern; CONFIRMED by attached doctrine that people/genealogy/DNA/land carries living-person, DNA/genomic, relationship-hypothesis, rights, source-role, and release risks; CONFIRMED current local child lane exists at `tests/domains/people-dna-land/connectors/gedcom/README.md`; NEEDS VERIFICATION for executable connector tests, accepted fixture shape, parser behavior, connector implementation, source descriptors, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/connectors/` is the parent test index for People DNA Land connector behavior.

This subtree should prove that source intake remains bounded and governable. A connector parse, fetch, import, scrape, adapter result, or local file read may produce candidate records, validation reports, receipts, denials, abstentions, or errors. It must not by itself produce canonical person truth, relationship truth, land-title truth, living-person exposure, DNA-derived exposure, public map labels, released artifacts, or publication.

A passing connector test should **not** mean that a source is admitted, a provider's terms are safe, a person assertion is true, a relationship is proven, a title chain is closed, or a public carrier is approved. It should mean only that the scoped connector guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable and `connectors/` as the root for source-specific fetchers or admitters. This directory is therefore a test lane family for connector behavior only. Reusable connector implementation belongs under the canonical `connectors/` root, not here.

| Responsibility | Correct home | This lane family's relationship |
|---|---|---|
| Connector behavior tests | `tests/domains/people-dna-land/connectors/` | This directory. |
| Source-specific connector implementation | `connectors/people-dna-land/` or accepted connector home | Referenced by tests if implementation exists; not owned here. |
| Reusable synthetic fixtures | `fixtures/domains/people-dna-land/connectors/` | Preferred fixture home if populated. |
| Semantic contracts | `contracts/domains/people-dna-land/` | Defines object meaning, not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` | Defines shape checks where accepted. |
| Policy rules | `policy/domains/people-dna-land/` | Decides allow, deny, restrict, and abstain. |
| Source descriptors | `data/registry/sources/people-dna-land/` | Source identity, rights, role, caveats, and permitted claim types. |
| Intake candidates | `data/raw/`, `data/work/`, or `data/quarantine/` after accepted pipeline rules | Not stored in this test lane family. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

---

## Parent Invariant

> **Connector output is candidate intake, not People DNA Land truth.** Connector success can support intake candidates, validation reports, or finite outcomes. It cannot by itself create source admission, evidence closure, consent clearance, living-person clearance, DNA clearance, title closure, release approval, public API output, public map output, or publication.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| No-network default | Default connector tests use synthetic local fixtures only. | validation failure / `ERROR`. |
| Source admission | SourceDescriptor-like metadata is required before connector output can progress. | `ABSTAIN` / `DENY`. |
| Rights and terms | Unknown, missing, or incompatible rights block public progression. | `DENY` / `ABSTAIN`. |
| Living-person posture | Living-person assertions fail closed without accepted policy support. | `DENY` / `ABSTAIN`. |
| DNA/genomic posture | DNA-derived or DNA-linked output is denied/restricted by default. | `DENY`. |
| Relationship hypotheses | Genealogy relationships remain assertions with evidence, confidence, source role, and review state. | validation failure / `ABSTAIN`. |
| Land/title overclaim | Connector output cannot settle title, ownership continuity, or legal boundary proof by itself. | `DENY` / `ABSTAIN`. |
| Evidence closure | Evidence-dependent claims resolve support before answer-like output. | `ABSTAIN`. |
| Lifecycle boundary | Connector output remains candidate/lifecycle material until governed promotion. | promotion block. |
| Release boundary | Test success never becomes release approval or public exposure. | promotion block. |

---

## Lane Index

| Lane | Primary responsibility | Boundary |
|---|---|---|
| [`gedcom/`](gedcom/README.md) | GEDCOM-style genealogy connector behavior, parser boundaries, source admission, living-person/DNA gates, relationship-hypothesis handling, evidence closure, lifecycle, release, correction, and rollback. | GEDCOM parse/import success creates candidate assertions only; it does not prove people, relationships, consent, DNA clearance, release approval, or connector production readiness. |

Additional connector test lanes may be added only when their source family, fixture posture, rights posture, privacy posture, source-role expectations, policy outcomes, release relationship, correction path, and rollback target are explicit.

Potential future lanes:

| Lane | Proposed responsibility | Status |
|---|---|---|
| `deeds/` | Local deed/title-record parser or adapter tests using synthetic fixtures. | PROPOSED / NEEDS VERIFICATION. |
| `assessor/` | Assessor/tax source intake tests that prevent title overclaim. | PROPOSED / NEEDS VERIFICATION. |
| `parcel/` | Parcel source intake tests that prevent legal-boundary overclaim. | PROPOSED / NEEDS VERIFICATION. |
| `genealogy_provider/` | Provider export/API behavior tests with rights, terms, consent, and living-person denial gates. | PROPOSED / NEEDS VERIFICATION. |
| `geocoder/` | Place-string handling tests that prevent authoritative geometry or land-claim overreach. | PROPOSED / NEEDS VERIFICATION. |

---

## Expected Test Families

The connector test family should eventually cover:

| Family | Expected proof point |
|---|---|
| Parse/fetch boundary | Parser or adapter success creates candidates only, not domain truth. |
| Source admission | Source identity, source role, rights, terms, caveats, and permitted claim types are explicit. |
| Candidate lifecycle | Connector output does not skip RAW, WORK, QUARANTINE, validation, catalog closure, or release gates. |
| Living-person and DNA gates | Sensitive People/DNA content denies, abstains, or restricts by default. |
| Relationship assertions | Imported family relationships remain evidence-bound hypotheses unless governed support allows more. |
| Land/title assertions | Connector output cannot settle legal title, ownership continuity, or legal boundary truth by itself. |
| Evidence closure | Imported citations or source notes do not become EvidenceBundles automatically. |
| Policy outcomes | Missing rights, consent, evidence, sensitivity review, or release state produces finite outcomes. |
| Redaction/generalization | Public-safe derivatives require named transforms and receipts where material. |
| Release/correction/rollback | Public exposure requires release state, correction path, withdrawal path, rollback target, and cache invalidation posture. |

---

## What Belongs Here

Appropriate contents include:

- no-network connector behavior tests;
- parser/adapter smoke tests against synthetic fixtures;
- source-admission and source-role tests;
- rights, terms, consent, living-person, DNA, and privacy fail-closed tests;
- lifecycle, evidence, policy, release, correction, and rollback gate tests;
- child-lane README files that explain scope, limits, validation posture, and rollback.

---

## Forbidden Shortcuts

Do not use this subtree to:

- implement live connectors, scrapers, fetchers, admitters, parsers, provider clients, geocoders, or pipeline logic;
- call live genealogy providers, DNA services, assessor systems, parcel services, deed/title systems, court systems, geocoders, or people-search services by default;
- store real GEDCOM exports, real people records, living-person records, DNA records, provider exports, deed/title records, assessor records, parcel data, credentials, public tiles, proof artifacts, or release artifacts;
- redefine People DNA Land doctrine, contracts, schemas, fixtures, source registries, policy rules, release decisions, renderer code, or production pipeline code;
- infer publication from connector success, parser success, source labels, test success, schema pass, map rendering, tile availability, Focus answer text, or AI wording;
- publish, promote, approve, release, correct, withdraw, or roll back anything.

Any test that needs live provider access, production source data, real consent systems, connector execution against external systems, or public output belongs in a gated integration tier with explicit source admission, rights review, sensitivity review, policy decision, receipts, release controls, correction path, and rollback targets.

---

## Run Posture

Parent connector test command:

```bash
pytest tests/domains/people-dna-land/connectors
```

Selected child-lane example:

```bash
pytest tests/domains/people-dna-land/connectors/gedcom
```

Status of these commands: **PROPOSED / NEEDS VERIFICATION**. They assume `pytest` is the accepted runner and that executable test modules exist. This README does not claim any command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; `connectors/` owns source-specific fetcher/admitter implementation; domain-specific material belongs under `tests/domains/<domain>/`; `people-dna-land` is listed in the domain lane pattern. | Does not prove executable connector test coverage or connector implementation. |
| `gedcom/README.md` | CONFIRMED local file | Existing child lane for GEDCOM connector behavior tests under this connector test family. | README-only; does not prove executable tests, fixtures, validators, CI, or pass rates. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | People/genealogy/DNA/land carries living-person/DNA restrictions; connectors require rights/source/security verification; no-network proof slices precede live activation. | Does not prove runtime implementation in this sparse workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | Connectors emit candidate records rather than public truth; source roles matter; People/DNA/land is assertion-first, evidence-bound, privacy-aware, and denied/restricted by default where exposure is unsafe. | Does not define parser behavior, jurisdiction-specific privacy law, source-specific terms, or production policy. |
| Current workspace | CONFIRMED | This README was created locally at the requested path. | Workspace is sparse and not a full verified repository checkout; CI and pass rates are UNKNOWN. |

---

## Validation Checklist

- [ ] Parent `tests/domains/people-dna-land/README.md` exists or this connector index is linked from the accepted parent index.
- [ ] Executable connector tests exist under documented child lanes.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic connector fixtures exist in the accepted fixture home.
- [ ] SourceDescriptor, SourceIntakeRecord, EvidenceRef / EvidenceBundle, PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] Living-person, DNA/genomic, consent, relationship-confidence, land/title, source-role, place, note/free-text, lifecycle, public-label, release, correction, and rollback fields are accepted by schemas or safely stubbed.
- [ ] CI runs this no-network connector test family or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this connector test family becomes live connector implementation, lifecycle data store, person registry, genealogy graph authority, consent database, land-title registry, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback is also required if parse success, fetch success, imported notes, imported source citations, relationship links, place strings, provider metadata, assessor/tax/parcel context, or generated summaries are treated as public truth without explicit source admission, evidence, policy, review, release, correction, and rollback support.

<p align="right"><a href="#top">Back to top</a></p>
