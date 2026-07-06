<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-claim-class-readme
title: Tests — Geology Claim Class
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <natural-resources-steward> + <evidence-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/domains/geology/README.md
  - docs/domains/geology/OBJECT_FAMILIES.md
  - docs/domains/geology/IDENTITY_MODEL.md
  - docs/domains/geology/SOURCE_REGISTRY.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - contracts/domains/geology/ResourceEstimate.md
  - contracts/domains/geology/MineralOccurrence.md
  - contracts/domains/geology/ResourceDeposit.md
  - contracts/domains/geology/ExtractionSite.md
  - contracts/domains/geology/ReclamationRecord.md
  - data/catalog/domain/geology/README.md
  - data/proofs/geology/README.md
  - tests/domains/geology/catalog-closure/README.md
  - fixtures/domains/geology/
tags:
  - kfm
  - tests
  - geology
  - natural-resources
  - claim-class
  - resource-class
  - anti-collapse
  - mineral-occurrence
  - resource-deposit
  - resource-estimate
  - permit
  - production
  - reserve
  - source-role
  - fail-closed
notes:
  - "This README governs the claim-class test lane under tests/domains/geology/claim-class/."
  - "It documents intended Geology claim-class test coverage; it does not claim that all tests already exist."
  - "Claim class is not source role. This lane tests the class of Geology/Natural Resources claim being asserted, especially occurrence/deposit/estimate/permit/production/reserve distinctions."
  - "Do not let public summaries, catalog projections, graph edges, AI answers, or map labels collapse one claim class into another."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Claim Class

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fgeology%2Fclaim--class-blue?style=flat-square)
![posture](https://img.shields.io/badge/posture-anti--collapse-critical?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the Geology-domain test lane for claim-class discipline. It proves that Geology/Natural Resources claims do not collapse `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, permit, production, reserve, extraction, reclamation, observation, model, and interpretation statements into one another.

---

## 1. Placement and authority

`tests/domains/geology/claim-class/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove Geology claim-class rules are enforceable.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/geology/` |
| Test lane | `claim-class/` |
| Primary doctrine | `docs/domains/geology/OBJECT_FAMILIES.md` |
| Primary runbook | `docs/runbooks/geology/PROMOTION_RUNBOOK.md` |
| Related semantic contracts | `contracts/domains/geology/` |
| Fixture counterpart | `fixtures/domains/geology/` |
| Adjacent proof lane | `tests/domains/geology/catalog-closure/` |
| Current implementation status | README path exists; executable tests, fixtures, validators, and CI wiring remain `UNKNOWN` until verified. |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific proof lanes under `tests/domains/<domain>/`. This lane tests classification behavior; it must not become a contract, schema, source registry, catalog, proof, policy, release, or fixture home.

---

## 2. Claim class vs. source role

This lane intentionally separates **claim class** from **source role**.

| Concept | Meaning | Example |
|---|---|---|
| Source role | What kind of source support is being used. | `observed`, `modeled`, `aggregate`, `administrative`, `regulatory`, `candidate`, `synthetic`. |
| Claim class | What kind of Geology/Natural Resources assertion is being made. | `mineral_occurrence`, `resource_deposit`, `resource_estimate`, `permit`, `production`, `reserve`, `extraction_site`, `reclamation_record`. |

A modeled source can support a resource estimate. An administrative source can support a permit record. An observed source can support a mineral occurrence. None of those facts allow the system to relabel the claim class or source role for convenience.

---

## 3. What this lane must prove

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| Mineral occurrence | Reported or observed presence remains an occurrence, not a deposit, estimate, reserve, permit, production record, or extraction site. | `CLAIM_CLASS_COLLAPSE` or hold. |
| Resource deposit | Named/delineated deposit remains distinct from occurrence and estimate. | `DEPOSIT_OCCURRENCE_COLLAPSE` or hold. |
| Resource estimate | Modeled/compiled quantity/classification claim remains estimate; not observation, deposit, reserve, or economic viability. | `ESTIMATE_CLASS_COLLAPSE` or hold. |
| Reserve claim | Reserve language requires explicit classification scheme, assumptions, source role, rights, and policy support. | `UNSUPPORTED_RESERVE_CLAIM` or hold. |
| Permit record | Permit/regulatory/administrative records do not prove occurrence, deposit, extraction, production, ownership, or reserve. | `PERMIT_AS_RESOURCE_TRUTH` or hold. |
| Production record | Production totals do not prove current deposit, reserve, ownership, or future availability. | `PRODUCTION_AS_RESERVE` or hold. |
| Extraction site | Extraction site is operational/historical context, not automatic proof of resource estimate or active production. | `EXTRACTION_AS_ESTIMATE` or hold. |
| Reclamation record | Reclamation status does not prove absence of resource, hazard, ownership, or release safety. | `RECLAMATION_OVERCLAIM` or hold. |
| Model/interpreted product | Modeled or interpreted geology cannot be presented as observed field truth. | `ROLE_UPCAST_FORBIDDEN` or hold. |
| Public/AI summary | Summaries, labels, graph edges, and AI answers preserve claim class and do not simplify into a stronger claim. | `SUMMARY_OVERCLAIM` or abstain/hold. |

---

## 4. Expected test families

This folder should eventually contain narrow tests for claim-class behavior.

```text
tests/domains/geology/claim-class/
├── README.md
├── test_mineral_occurrence_class.py         # PROPOSED
├── test_resource_deposit_class.py           # PROPOSED
├── test_resource_estimate_class.py          # PROPOSED
├── test_reserve_claim_support.py            # PROPOSED
├── test_permit_not_resource_truth.py        # PROPOSED
├── test_production_not_reserve.py           # PROPOSED
├── test_extraction_site_class.py            # PROPOSED
├── test_reclamation_record_class.py         # PROPOSED
├── test_model_interpretation_boundaries.py  # PROPOSED
├── test_public_summary_claim_class.py       # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

If executable module names use underscores, keep Python filenames with underscores while preserving this requested `claim-class/` directory path unless a repository-wide naming migration says otherwise.

---

## 5. Fixture expectations

Tests in this lane should be no-network by default. They should use small synthetic or public-safe examples that isolate one claim-class boundary at a time.

Recommended fixture groups:

```text
fixtures/domains/geology/claim-class/
├── valid/
│   ├── mineral_occurrence_observed.json
│   ├── resource_deposit_named.json
│   ├── resource_estimate_modeled.json
│   ├── permit_administrative.json
│   ├── production_aggregate.json
│   ├── extraction_site_operational.json
│   └── reclamation_record_context.json
├── invalid/
│   ├── occurrence_labeled_as_deposit.json
│   ├── deposit_labeled_as_reserve.json
│   ├── estimate_labeled_as_observation.json
│   ├── permit_labeled_as_resource_truth.json
│   ├── production_labeled_as_current_reserve.json
│   ├── extraction_site_labeled_as_estimate.json
│   ├── reclamation_record_labeled_as_no_hazard.json
│   └── ai_summary_collapses_claim_class.json
└── golden/
    ├── geology_claim_class_minimal.json
    └── geology_resource_claim_anti_collapse_matrix.json
```

Fixture rules:

- Use synthetic examples unless a public-safe, rights-reviewed fixture is intentionally included.
- Do not include precise sensitive borehole, sample, private-well, operator, parcel, mineral-rights, lease, proprietary, or infrastructure-risk details.
- Invalid fixtures should fail for one primary claim-class reason where practical.
- Golden fixtures should make claim class, source role, evidence reference, sensitivity posture, and public summary text easy to inspect.

---

## 6. Claim-class vocabulary under test

The vocabulary below is a proposed testing vocabulary, not a new schema authority.

| Claim class | Safe meaning | Must not be treated as |
|---|---|---|
| `mineral_occurrence` | Reported/observed/compiled presence of a mineral/material. | Deposit, reserve, estimate, production, ownership, permit. |
| `resource_deposit` | Named or delineated deposit/body/resource context. | Occurrence-only, reserve, production, legal title, extraction permit. |
| `resource_estimate` | Modeled/compiled quantity or classification claim with assumptions. | Direct observation, deposit, reserve by default, economic viability. |
| `reserve_claim` | Reserve classification under explicit scheme, assumptions, and source support. | Generic estimate, occurrence, production, ownership. |
| `permit_record` | Regulatory/administrative authorization or record. | Resource truth, production proof, ownership/title. |
| `production_record` | Reported production amount or operational history. | Current reserve, current deposit extent, future availability. |
| `extraction_site` | Site or facility context for extraction activity. | Estimate, reserve, ownership, safety condition. |
| `reclamation_record` | Reclamation/remediation status or context. | Hazard absence, resource absence, unrestricted release. |
| `model_interpretation` | Modeled or interpreted geology product. | Field observation unless evidence and source role support that narrower claim. |
| `public_derivative` | Public-safe summary/generalized carrier. | Canonical truth, internal exact record, legal/resource conclusion. |

---

## 7. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `GEOL-CLAIM-001` | Valid occurrence class passes. | A MineralOccurrence with observed/compiled presence support and no stronger claim. | Validation passes. |
| `GEOL-CLAIM-002` | Occurrence cannot become deposit. | A MineralOccurrence labeled or summarized as ResourceDeposit. | Validation fails closed. |
| `GEOL-CLAIM-003` | Estimate cannot become observation. | A ResourceEstimate with modeled/compiled support labeled observed. | Validation fails closed. |
| `GEOL-CLAIM-004` | Estimate cannot become reserve by default. | A ResourceEstimate without classification scheme/assumptions labeled reserve. | Held or denied. |
| `GEOL-CLAIM-005` | Permit cannot prove resource truth. | A permit record used as deposit/occurrence/reserve evidence without supporting geology evidence. | Held or denied. |
| `GEOL-CLAIM-006` | Production cannot prove current reserve. | A production total summarized as current reserve or future availability. | Held or denied. |
| `GEOL-CLAIM-007` | Extraction site cannot become estimate. | An ExtractionSite record used as a ResourceEstimate. | Validation fails closed. |
| `GEOL-CLAIM-008` | Public summary preserves class. | A public layer label or AI summary simplifies estimate/deposit/occurrence into one stronger claim. | Summary fails, holds, or abstains. |
| `GEOL-CLAIM-009` | Graph edge preserves class. | A triplet edge converts occurrence -> reserve or permit -> production. | Graph projection fails. |
| `GEOL-CLAIM-010` | Catalog closure preserves class. | A catalog record and EvidenceBundle disagree on claim class. | Hold at PROCESSED/CATALOG gate. |

---

## 8. Non-goals

This folder must not:

- decide mineral value, economic viability, reserve status, legal ownership, leasing, title, operator liability, or investment meaning;
- call live KGS, USGS, KCC, mineral-resource, permit, production, borehole, or proprietary services;
- store fixtures, contracts, schemas, catalog records, proofs, receipts, releases, source records, or raw data;
- treat AI-generated summaries as claim-class authority;
- infer claim class from a folder name, layer name, map color, or common-language label alone;
- expose precise sensitive subsurface, resource, borehole, sample, private-well, parcel, operator, or infrastructure-risk details; or
- silently convert `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, or unresolved claim class into a passing result.

---

## 9. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] The expected result preserves claim class and source role separately.
- [ ] Occurrence, deposit, estimate, permit, production, reserve, extraction, and reclamation are not collapsed.
- [ ] Any public summary or AI answer fixture retains qualifiers and does not strengthen the claim.
- [ ] Any graph/triplet fixture preserves EvidenceBundle and claim-class references.
- [ ] Sensitive geometry, private/proprietary detail, or rights uncertainty holds or denies.
- [ ] Failure emits a finite reason code rather than a silent pass.
- [ ] Any naming or schema drift is recorded as drift or verification backlog, not silently normalized.

---

## 10. Current implementation note

This lane is documentation-first. The target README existed as an empty placeholder before this update. The Geology promotion runbook identifies a proposed resource-class anti-collapse test, and the object-family doctrine records the occurrence/deposit/estimate distinctions. This README does not prove that executable claim-class tests, fixtures, validators, or CI wiring already exist.

---

## 11. Definition of done

This README becomes implementation-backed when:

- at least the `GEOL-CLAIM-001` through `GEOL-CLAIM-010` scenarios exist as executable tests;
- fixtures exist under the repository's approved Geology fixture home and contain no sensitive real locations or proprietary details;
- contracts/schemas carry claim-class fields or equivalent validated structures;
- source-role and claim-class checks are separate and both enforced;
- graph, catalog, public summary, and AI-answer fixtures prove anti-collapse behavior; and
- CI runs this lane without network access.
