<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-people-dna-land-connectors-gedcom-readme
title: People DNA Land GEDCOM Connector Tests README
type: test-lane-readme
version: v0.1
status: draft; directory-created-in-scratch; connector-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - People DNA Land domain steward
  - OWNER_TBD - Genealogy steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Privacy steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - QA steward
created: 2026-07-05
updated: 2026-07-05
policy_label: public-doc; tests; people-dna-land; connectors; gedcom; genealogy; living-person-sensitive; dna-sensitive; no-network; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, people-dna-land, connectors, gedcom, genealogy, person-assertion, family-relationship, living-person, dna, consent, source-role, EvidenceBundle, PolicyDecision, SourceIntakeRecord, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../../README.md
  - ../../../README.md
  - ../../README.md
  - ../../assessor_as_title_denial_test/README.md
  - ../../chain_of_title_gap_test/README.md
  - ../../../../../docs/domains/people-dna-land/
  - ../../../../../docs/domains/people-dna-land/land-ownership/
  - ../../../../../contracts/domains/people-dna-land/
  - ../../../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../../../policy/domains/people-dna-land/
  - ../../../../../fixtures/domains/people-dna-land/connectors/gedcom/
  - ../../../../../connectors/people-dna-land/gedcom/
  - ../../../../../data/registry/sources/people-dna-land/
  - ../../../../../release/manifests/people-dna-land/
notes:
  - "This README creates the local lane requested at tests/domains/people-dna-land/connectors/gedcom/README.md."
  - "Directory Rules place enforceability proof under tests/, source-specific fetcher/admitter implementation under connectors/, and people-dna-land as a domain lane pattern."
  - "This is a connector test-lane README only. It does not define GEDCOM connector implementation, People DNA Land doctrine, contracts, schemas, fixtures, source descriptors, genealogy records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that GEDCOM intake remains a candidate source-admission path: parse success is not truth, source admission, consent clearance, living-person clearance, DNA clearance, release approval, or publication."
  - "Default posture is deterministic and no-network. Live genealogy providers, real GEDCOM exports, real people records, living-person records, DNA data, source exports, credentials, and public release artifacts do not belong in this lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GEDCOM connector tests

> Deterministic, no-network test documentation for GEDCOM-style genealogy connector behavior, source admission, privacy gates, evidence closure, policy outcomes, release boundaries, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-blue">
  <img alt="Lane: GEDCOM connector tests" src="https://img.shields.io/badge/lane-gedcom__connector__tests-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not connector" src="https://img.shields.io/badge/boundary-tests__not__connector-success">
</p>

**Path:** `tests/domains/people-dna-land/connectors/gedcom/README.md`  
**Status:** draft / directory-created-in-scratch / connector test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `people-dna-land`  
**Test lane:** `connectors/gedcom`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED by Directory Rules that `tests/` is the canonical root for enforceability proof, `connectors/` is the canonical root for source-specific fetcher/admitter implementation, and `people-dna-land` is a domain lane pattern; CONFIRMED by attached doctrine that people/genealogy/DNA/land carries living-person, DNA/genomic, relationship-hypothesis, rights, source-role, and release risks; NEEDS VERIFICATION for executable GEDCOM tests, accepted fixture shape, schemas, parser behavior, connector implementation, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/people-dna-land/connectors/gedcom/` is the requested test lane for GEDCOM-style genealogy connector behavior.

This lane should prove that a GEDCOM parse or import candidate does not become KFM truth by parsing successfully. Imported person assertions, family relationships, dates, places, notes, sources, submitter metadata, and derived relationship claims must pass source admission, rights review, living-person and DNA sensitivity checks, evidence closure, policy review, release gates, correction posture, and rollback requirements before any public carrier can use them.

A passing test here should **not** mean that a GEDCOM source is admitted, a family relationship is true, a living-person assertion is publishable, a DNA-derived relationship is allowed, a public genealogy graph is approved, or a connector is production-ready. It should mean only that the scoped guardrail behaved as expected against bounded fixtures and local files.

---

## Placement Basis

Directory Rules classify `tests/` as the root that proves rules are enforceable and `connectors/` as the root for source-specific fetchers or admitters. This path is acceptable only as a **test lane** for connector behavior. Reusable connector implementation belongs under the canonical `connectors/` root, not here.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| GEDCOM connector tests | `tests/domains/people-dna-land/connectors/gedcom/` | This directory. |
| GEDCOM connector implementation | `connectors/people-dna-land/gedcom/` or accepted connector home | Referenced by tests if implementation exists; not owned here. |
| Reusable synthetic fixtures | `fixtures/domains/people-dna-land/connectors/gedcom/` | Preferred fixture home if populated. |
| Semantic contracts | `contracts/domains/people-dna-land/` | Defines object meaning, not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` | Defines shape checks where accepted. |
| Policy rules | `policy/domains/people-dna-land/` | Decides allow, deny, restrict, and abstain. |
| Source descriptors | `data/registry/sources/people-dna-land/` | Source identity, rights, role, caveats, and permitted claim types. |
| Intake candidates | `data/raw/`, `data/work/`, or `data/quarantine/` after accepted pipeline rules | Not stored in this test lane. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

---

## Invariant Under Test

> **GEDCOM import is candidate intake, not genealogy truth.** Parse success can produce source-intake candidates, validation reports, or abstention/denial outcomes. It cannot by itself create canonical person truth, public relationship truth, living-person exposure, DNA-derived exposure, public map labels, or release approval.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Parser boundary | Well-formed synthetic GEDCOM-like input becomes candidate assertions only. | validation failure if treated as truth. |
| Malformed input | Invalid structure fails closed with no partial public payload. | `ERROR` / validation failure. |
| Source admission | SourceDescriptor-like metadata is required before connector output can progress. | `ABSTAIN` / `DENY`. |
| Living-person posture | Living-person assertions fail closed without accepted policy support. | `DENY` / `ABSTAIN`. |
| DNA/genomic posture | DNA-derived or DNA-linked relationship output is denied/restricted by default. | `DENY`. |
| Relationship hypotheses | Family relationships remain assertions with evidence, confidence, source role, and review state. | validation failure / `ABSTAIN`. |
| Evidence closure | Evidence-dependent person or relationship claims resolve support before answer-like output. | `ABSTAIN`. |
| Notes and free text | Notes are not promoted to claims without parsing, policy, evidence, and review support. | validation failure / `ABSTAIN`. |
| Place extraction | Places from GEDCOM-like input do not become authoritative geocodes or land claims. | validation failure / `ABSTAIN`. |
| Release boundary | Test success never becomes release approval or public exposure. | promotion block. |
| No network | Default tests do not call genealogy providers, geocoders, DNA services, people-search services, or live source systems. | validation failure / `ERROR`. |

---

## Expected Scope

Tests in this lane may validate:

- parse success produces candidate person and relationship assertions, not canonical truth;
- malformed input returns finite `ERROR` or validation failure without leaking partial sensitive payloads;
- living-person records are denied or abstained without policy support;
- DNA-linked or DNA-derived relationship assertions are denied or restricted by default;
- imported relationships remain hypotheses unless evidence, confidence, review, and release support a stronger claim;
- GEDCOM-like source citations are preserved as source references but do not become EvidenceBundles by themselves;
- notes, submitter metadata, free text, and places are treated as high-risk input requiring parsing, policy, evidence, and review;
- GEDCOM place strings do not create authoritative geometry, title claims, or parcel links;
- connector output remains `RAW`, `WORK`, `QUARANTINE`, or candidate-like material until governed promotion;
- no-network behavior for the default suite.

Out of scope for the default suite:

- real GEDCOM exports, private family trees, real living-person records, real DNA records, provider downloads, credentials, geocoding calls, people-search calls, genealogy-provider APIs, public tiles, public layers, published genealogy graphs, and production connector runs.

---

## Fixture Posture

Use synthetic, public-safe GEDCOM-like fixtures only.

Fixture requirements:

- deterministic and no-network;
- small enough for PR review;
- clearly labeled as synthetic;
- no real names, real family trees, real living-person records, real DNA references, real submitter metadata, real addresses, real provider IDs, credentials, or production identifiers;
- explicit expected outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- explicit source role, parse posture, person/living-status posture, relationship-assertion posture, DNA/genomic posture, consent posture, evidence posture, policy state, release relationship, correction path, and rollback target where material.

---

## Finite Outcomes

| Condition | Expected outcome |
|---|---|
| Synthetic GEDCOM-like file parses and contains only historical public-safe assertions | candidate assertions only; possible accepted support only after policy and release. |
| Parser fails on malformed input | `ERROR` / validation failure; no public payload. |
| SourceDescriptor-like metadata is missing | `ABSTAIN` / `DENY`. |
| Living-person assertion lacks policy support | `DENY` / `ABSTAIN`. |
| DNA-linked relationship is present without authorized policy support | `DENY`. |
| Relationship claim lacks admissible evidence or confidence support | `ABSTAIN`. |
| Imported source citation cannot resolve to EvidenceBundle | `ABSTAIN`. |
| Place string is treated as authoritative geometry or land ownership | validation failure / `DENY`. |
| Connector output skips lifecycle and promotion gates | promotion-blocking failure. |
| Test attempts live provider, geocoder, DNA, or people-search access | validation failure / `ERROR`. |

---

## Suggested Layout

```text
tests/domains/people-dna-land/connectors/gedcom/
|-- README.md
|-- test_parse_success_creates_candidates_only.py
|-- test_malformed_input_fails_closed.py
|-- test_source_descriptor_required.py
|-- test_living_person_records_deny_by_default.py
|-- test_dna_linked_relationship_denies.py
|-- test_relationship_hypothesis_not_canonical_truth.py
|-- test_source_citation_not_evidence_bundle.py
|-- test_place_string_not_authoritative_geometry.py
|-- test_lifecycle_promotion_required.py
`-- test_no_network_gedcom_provider_access.py
```

---

## Run Posture

```bash
pytest tests/domains/people-dna-land/connectors/gedcom
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence Ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` | CONFIRMED | `tests/` is enforceability proof; `connectors/` owns source-specific fetcher/admitter implementation; domain-specific material belongs under `tests/domains/<domain>/`; `people-dna-land` is listed in the domain lane pattern. | Does not prove executable GEDCOM test coverage or connector implementation. |
| `Unified Implementation Architecture Build Manual.md` | CONFIRMED doctrine / PROPOSED realization | People/genealogy/DNA/land includes person assertions, genealogy, family relationships, DNA/genomics, land ownership, and living-person/DNA restrictions; connectors require rights/source/security verification; no-network proof slices precede live activation. | Does not prove runtime implementation in this sparse workspace. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | CONFIRMED corpus synthesis / PROPOSED realization | Connectors emit candidate records rather than public truth; source roles matter; People/DNA/land is assertion-first, evidence-bound, privacy-aware, and denied/restricted by default where exposure is unsafe. | Does not define GEDCOM parser behavior, jurisdiction-specific privacy law, or production policy. |
| Current workspace | CONFIRMED | This README was created locally at the requested path. | Workspace is sparse and not a full verified repository checkout; CI and pass rates are UNKNOWN. |

---

## Validation Checklist

- [ ] Parent `tests/domains/people-dna-land/README.md` exists or this lane is linked from the accepted parent index.
- [ ] Executable tests exist under this lane.
- [ ] Test runner and import paths match repo convention.
- [ ] Synthetic GEDCOM-like fixtures exist in the accepted fixture home.
- [ ] Parser outputs candidate records only and does not create canonical person or relationship truth.
- [ ] SourceDescriptor, SourceIntakeRecord, EvidenceRef / EvidenceBundle, PolicyDecision, ConsentRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard expectations are defined before enforcing them.
- [ ] Living-person, DNA/genomic, consent, relationship-confidence, source-role, place, note/free-text, lifecycle, public-label, release, correction, and rollback fields are accepted by schemas or safely stubbed.
- [ ] CI runs this no-network GEDCOM connector test lane or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live GEDCOM, genealogy-provider, DNA, geocoder, people-search, parcel, assessor, title, or deed connector; lifecycle data store; person registry; genealogy graph authority; consent database; source registry; contract root; schema authority; policy authority; proof store; release-decision root; public map/API/tile surface; AI surface; renderer implementation; pipeline implementation; or publication shortcut.

Rollback is also required if parse success, imported notes, imported source citations, relationship links, place strings, GEDCOM submitter metadata, or generated summaries are treated as public truth without explicit source admission, evidence, policy, review, release, correction, and rollback support.

<p align="right"><a href="#top">Back to top</a></p>
