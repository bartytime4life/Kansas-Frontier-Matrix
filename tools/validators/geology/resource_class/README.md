<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geology-resource-class-readme
title: tools/validators/geology/resource_class README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geology-steward-plus-natural-resources-steward-plus-claim-class-steward-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geology-validator; resource-class; claim-class; natural-resources; occurrence-deposit-estimate-permit-production-reserve; anti-collapse; source-role-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Geology resource-class validator lane for checking MineralOccurrence, ResourceDeposit, ResourceEstimate, permit, production, reserve, extraction-site, reclamation, ownership, lease, title, hazard, and public-summary anti-collapse, source-role separation, classification-scheme posture, assumption posture, rights/sensitivity posture, public-safe geometry posture, EvidenceRef/EvidenceBundle linkage, source registry linkage, policy/review/release linkage, correction and rollback linkage, and public-surface denial checks while deferring Geology meaning, source registry authority, resource/reserve decisions, policy decisions, evidence records, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../../domains/geology/README.md
  - ../borehole_rights/README.md
  - ../public_safe_geometry/README.md
  - ../../cross-domain-joins/README.md
  - ../../evidence/README.md
  - ../../citation/README.md
  - ../../evidence_bundle/README.md
  - ../../../../contracts/domains/geology/MineralOccurrence.md
  - ../../../../contracts/domains/geology/ResourceDeposit.md
  - ../../../../contracts/domains/geology/ResourceEstimate.md
  - ../../../../contracts/domains/geology/ExtractionSite.md
  - ../../../../contracts/domains/geology/ReclamationRecord.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/domains/geology/
  - ../../../../policy/sensitivity/geology/
  - ../../../../data/registry/sources/geology/
  - ../../../../data/registry/sensitivity/geology/
  - ../../../../data/proofs/geology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
  - ../../../../tests/domains/geology/claim-class/README.md
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "MineralOccurrence contract evidence says an occurrence is reported mineral presence and does not prove economic value, deposit identity, resource/reserve estimate, extraction, ownership, permit authority, production, or hazards risk."
  - "ResourceDeposit contract evidence says a deposit is a named/delineated body with characterization and does not prove quantified resource/reserve estimate, economic viability, production, extraction, ownership, permit authority, or hazards risk."
  - "ResourceEstimate contract evidence says an estimate is a modeled or compiled quantity/classification claim with assumptions and is not direct measurement, deposit, occurrence, or reserve unless source classification and policy support that narrow status."
  - "Claim-class test evidence says claim class is not source role and that public summaries, catalog projections, graph edges, AI answers, and map labels must not collapse one claim class into another."
  - "This validator lane must not certify resource value, reserve status, economic viability, extraction feasibility, ownership/title, lease, permit status, production status, public safety, policy approval, release approval, or public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geology/resource_class

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-resource--class--validator-informational)
![posture](https://img.shields.io/badge/posture-anti--collapse-critical)
![release](https://img.shields.io/badge/release-gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geology/resource_class/` is the proposed validator lane for checking that Geology/Natural Resources claims preserve their resource claim class instead of collapsing occurrence, deposit, estimate, permit, production, reserve, extraction, reclamation, ownership, lease, title, or hazard statements into one another.

---

## Purpose

`tools/validators/geology/resource_class/` exists for Geology resource-class and claim-class checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a Geology/Natural Resources candidate preserve its exact claim class, source role, source authority limit, classification scheme, assumptions, rights/sensitivity posture, public-safe geometry posture, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Geology truth, resource truth, reserve truth, permit truth, production truth, ownership/title truth, extraction guidance, economic viability, hazard truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geology/resource_class/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Per-domain Geology validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Geology validator index names occurrence/deposit/estimate/permit/production/reserve distinctions, natural-resource sensitivity, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| MineralOccurrence contract | **CONFIRMED in repo evidence / draft** | `MineralOccurrence` is reported presence and is explicitly not deposit, estimate, economic viability, reserve, extraction, ownership, permit, production, reclamation, hazards risk, or AI/UI truth by itself. |
| ResourceDeposit contract | **CONFIRMED in repo evidence / draft** | `ResourceDeposit` is a named/delineated deposit body with characterization and is explicitly distinct from occurrences, estimates, reserves, extraction, ownership, permits, production, and hazards risk. |
| ResourceEstimate contract | **CONFIRMED in repo evidence / draft** | `ResourceEstimate` is a modeled or compiled quantity/classification claim with assumptions and is distinct from direct measurement, occurrence, deposit, reserve, economic viability, extraction, production, ownership, lease, permit, and public safety. |
| Claim-class test lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tests/domains/geology/claim-class/README.md` states claim class is not source role and documents proposed anti-collapse test coverage. |
| Resource-class executable, accepted schemas, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Claim class is not source role

This validator must keep two separate questions separate:

| Question | Example values | Validator posture |
|---|---|---|
| **Source role** — what kind of source support is being used? | `observed`, `modeled`, `aggregate`, `administrative`, `regulatory`, `candidate`, `synthetic` | Source role can constrain trust, but it does not relabel the claim. |
| **Resource claim class** — what kind of Geology/Natural Resources assertion is being made? | `mineral_occurrence`, `resource_deposit`, `resource_estimate`, `permit`, `production`, `reserve`, `extraction_site`, `reclamation_record` | Claim class must remain visible through catalog, graph, map, report, export, and AI surfaces. |

A modeled source can support a resource estimate. An administrative source can support a permit. An observed source can support a mineral occurrence. None of those facts allow KFM to relabel the claim class or source role for convenience.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Mineral occurrence | Is the candidate only a reported/observed/compiled presence claim? | Deposit, estimate, reserve, permit, production, extraction, ownership, or hazard truth. |
| Resource deposit | Is the candidate a named/delineated deposit body with characterization? | Quantified estimate, reserve, economic viability, production, extraction, ownership, or permit authority. |
| Resource estimate | Is the candidate a modeled/compiled quantity or classification claim with assumptions? | Observation, deposit, occurrence, reserve, direct measurement, economic viability, or production truth. |
| Permit/regulatory record | Is the candidate an administrative/regulatory claim scoped to the permit? | Occurrence, deposit, extraction, production, ownership, or reserve proof. |
| Production record | Is the candidate a time-bounded production statement with source and caveats? | Current reserve, future availability, ownership, or active extraction proof. |
| Reserve language | Does reserve terminology have explicit classification scheme, source, assumptions, rights, policy, and release support? | Generic resource or deposit label. |
| Extraction/reclamation context | Is operational or reclamation context bounded and caveated? | Resource estimate, absence/presence proof, hazard clearance, or release safety. |
| Public summary/AI/map label | Does the displayed wording preserve claim class and caveats? | A stronger simplified claim. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Resource-class validator lane | `tools/validators/geology/resource_class/` |
| Per-domain Geology validator index | `tools/validators/domains/geology/` |
| Borehole rights and exact subsurface rights gate | `tools/validators/geology/borehole_rights/` |
| Public-safe geometry gate | `tools/validators/geology/public_safe_geometry/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Claim-class tests | `tests/domains/geology/claim-class/` |
| MineralOccurrence / ResourceDeposit / ResourceEstimate contracts | `contracts/domains/geology/` |
| Geology doctrine and natural-resources scope | `docs/domains/geology/` |
| Geology and source schemas | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/source/` |
| Source descriptors | `data/registry/sources/geology/` |
| Sensitivity registry and policy | `data/registry/sensitivity/geology/`, `policy/domains/geology/`, `policy/sensitivity/geology/` |
| Proofs, receipts, release | `data/proofs/geology/`, `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where resource-class validation may be documented or implemented after verification.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Resource-class validator lane | `tools/validators/geology/resource_class/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Geology validator index | `tools/validators/domains/geology/` |
| Resource-class contracts | `contracts/domains/geology/MineralOccurrence.md`, `contracts/domains/geology/ResourceDeposit.md`, `contracts/domains/geology/ResourceEstimate.md`, and related contracts |
| Geology doctrine | `docs/domains/geology/` |
| Source descriptors and source admission records | `data/registry/sources/geology/` or accepted source-registry home |
| Sensitivity registry and policy | `data/registry/sensitivity/geology/`, `policy/domains/geology/`, `policy/sensitivity/geology/` |
| Source and geology schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/geology/` |
| Evidence/proof support | `data/proofs/geology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geology/resource_class/`, `tests/domains/geology/claim-class/`, `fixtures/domains/geology/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared resource-class, source-role, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, claim-class vocabulary, reserve-classification vocabulary, fixture shape, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Geology doctrine, resource/reserve authority, source registry, source payload storage, schema home, proof storage, receipt storage, policy home, release record store, mineral-rights authority, title authority, lease authority, permit authority, production authority, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geology/resource_class/` include checks that:

- verify each natural-resource candidate carries an explicit resource claim class;
- verify `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, permit, production, reserve, extraction-site, and reclamation claims remain distinct;
- verify source role, source family, source descriptor, classification scheme, assumptions, rights, sensitivity tier, public-safe geometry, EvidenceRef/EvidenceBundle, policy, release, correction, and rollback posture are present where required;
- verify public summaries, catalog records, graph edges, map labels, export rows, Focus Mode cards, Evidence Drawer language, and AI responses do not strengthen the claim class;
- verify reserve terminology is blocked unless source classification, assumptions, rights, evidence, policy, release, correction, and rollback support authorize that narrow statement;
- emit deterministic findings for downstream review without storing source payloads, proof artifacts, receipts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geology/resource_class/` | Correct home |
|---|---|
| Geology doctrine, object-family meaning, or natural-resources scope | `docs/domains/geology/`, `contracts/domains/geology/` |
| Resource/reserve classification schemes and schemas | `schemas/contracts/v1/domains/geology/`, contract docs, or accepted schema homes |
| SourceDescriptor records or source registry records | `data/registry/sources/geology/` |
| Geology source payloads or resource datasets | dedicated `data/` lifecycle roots with quarantine/review as needed |
| Rights decisions, sensitivity decisions, policy bundles | `policy/`, `data/registry/sensitivity/geology/`, or accepted policy/sensitivity homes |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Connectors, parsers, ETL, source refreshers, model runners, estimate calculators | `connectors/`, `pipelines/`, `packages/`, or accepted implementation roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, extraction guidance, legal/title/lease/permit determinations, engineering recommendations, investment advice, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Resource-class validator posture

Resource-class validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, claim class, classification scheme, assumptions, sensitivity tier, public-safe geometry posture, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- treats mineral occurrence as deposit, estimate, reserve, permit, production, ownership, extraction, reclamation, or hazard truth;
- treats deposit body or deposit characterization as quantified estimate, reserve, economic viability, production, ownership, extraction, or permit authority;
- treats resource estimate as observed field truth, direct measurement, deposit, occurrence, reserve, production, economic viability, public safety, or legal statement;
- treats permit or administrative records as occurrence, deposit, extraction, production, ownership, reserve, or public-access proof;
- treats production totals as current reserve, future availability, ownership, active operation, or extraction feasibility;
- uses reserve/resource language without explicit source classification, assumptions, evidence, rights, policy, release, correction, and rollback support;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on resource-class-collapsed candidates;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, exact sensitive geometry, unsupported reserve language, or incomplete proof closure;
- treats resource-class validation as SourceDescriptor creation, EvidenceBundle creation, PolicyDecision creation, reserve certification, economic assessment, release approval, publication, public API behavior, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `RESOURCE_CLASS_PASS` | Configured resource-class checks passed. |
| `RESOURCE_CLASS_FAIL` | One or more configured resource-class checks failed. |
| `RESOURCE_CLASS_MISSING` | Required resource claim class is absent. |
| `RESOURCE_CLASS_UNKNOWN` | Claim class is not accepted by configured contract/schema/policy. |
| `SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `MINERAL_OCCURRENCE_COLLAPSE` | Mineral occurrence is treated as a stronger or different claim class. |
| `RESOURCE_DEPOSIT_COLLAPSE` | Deposit body/characterization is treated as estimate, reserve, production, or ownership truth. |
| `RESOURCE_ESTIMATE_COLLAPSE` | Estimate is treated as observation, deposit, occurrence, reserve, production, or economic/legal truth. |
| `UNSUPPORTED_RESERVE_CLAIM` | Reserve terminology lacks required classification, assumptions, source, rights, evidence, policy, and release support. |
| `PERMIT_AS_RESOURCE_TRUTH` | Permit/regulatory/administrative record is treated as occurrence, deposit, extraction, production, ownership, or reserve proof. |
| `PRODUCTION_AS_RESERVE` | Production record is treated as current reserve, future availability, or ownership proof. |
| `EXTRACTION_AS_ESTIMATE` | Extraction site/context is treated as resource estimate or active production proof. |
| `RECLAMATION_OVERCLAIM` | Reclamation status is treated as absence/presence/resource/hazard/release proof. |
| `SUMMARY_OVERCLAIM` | Public summary, label, graph edge, export, or AI answer strengthens or collapses claim class. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, source admission, evidence closure, classification review, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/geology/resource_class/
├── README.md
├── test_resource_class_validator.py
└── fixtures/
    ├── valid_mineral_occurrence/
    ├── valid_resource_deposit/
    ├── valid_resource_estimate_aggregate/
    ├── missing_resource_class/
    ├── mineral_occurrence_collapse/
    ├── resource_deposit_collapse/
    ├── resource_estimate_collapse/
    ├── unsupported_reserve_claim/
    ├── permit_as_resource_truth/
    ├── production_as_reserve/
    └── summary_overclaim/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geology/resource_class
```

```bash
python tools/validators/geology/resource_class/validate_resource_class.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_resource_class.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Geology contracts, schemas, source descriptors, source-role rules, sensitivity posture, policy, evidence records, release records, and correction/rollback records rather than defining meaning locally.
- [ ] Claim class and source role remain distinct.
- [ ] MineralOccurrence, ResourceDeposit, ResourceEstimate, permit, production, reserve, extraction-site, and reclamation claims remain distinct.
- [ ] Reserve/resource/economic/legal wording requires explicit source classification, assumptions, evidence, rights, policy, release, correction, and rollback support.
- [ ] Public summaries, catalog projections, graph edges, map labels, export rows, Evidence Drawer text, and AI answers do not strengthen the claim class.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, exact sensitive geometry, unsupported reserve language, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, resource/reserve certification, economic assessment, policy approval, release, publication, source admission, mineral-rights authority, title authority, lease authority, permit authority, production authority, extraction guidance, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Geology resource-class validator file. |
| Next smallest safe change | Verify actual resource-class validator script path, accepted Geology/source schemas, claim-class vocabulary, reserve-classification vocabulary, fixtures, report destination, receipt emission, policy enforcement, release linkage, public summary/AI wording behavior, and CI/runtime wiring before promoting this lane beyond draft. |
