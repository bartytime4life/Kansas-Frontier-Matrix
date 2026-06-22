<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-resource-estimate
title: ResourceEstimate Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Natural-resources steward
  - OWNER_TBD — Resource-estimate steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: restricted-by-default; semantic-contract; geology; resource-estimate; natural-resources; modeled-aggregate; anti-collapse; source-role-aware; release-gated; public-aggregate-only
tags: [kfm, contracts, geology, ResourceEstimate, resource-estimate, natural-resources, reserve, resource, modeled, aggregate, classification-scheme, assumptions, commodity, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./MineralOccurrence.md
  - ./ResourceDeposit.md
  - ./GeochemistrySample.md
  - ./GeophysicalObservation.md
  - ./ExtractionSite.md
  - ./ReclamationRecord.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../docs/domains/geology/sublanes/geochemistry.md
  - ../../../docs/domains/geology/sublanes/geophysics.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/resource_estimate.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology ResourceEstimate semantic contract."
  - "A lower-case schema scaffold exists at schemas/contracts/v1/domains/geology/resource_estimate.schema.json, while this requested contract path uses PascalCase. The schema's x-kfm.contract_doc points to contracts/domains/geology/resource_estimate.md, creating a casing/path drift that remains CONFLICTED / NEEDS VERIFICATION."
  - "ResourceEstimate means a modeled or compiled quantity/classification claim with assumptions. It is not a direct measurement, not a deposit, not an occurrence, not a reserve claim unless source classification and policy explicitly support that narrow status."
  - "ResourceEstimate is typically T3/restricted; aggregate public derivatives may be released only with evidence, rights, validation, policy/review where material, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ResourceEstimate — Geology

> Semantic contract for Geology `ResourceEstimate`: the evidence-bound object for modeled or compiled resource/reserve estimate claims, classification schemes, assumptions, aggregation units, source roles, sensitivity posture, correction, and rollback — explicitly distinct from occurrences, deposits, extraction, ownership, permits, production, and public release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: ResourceEstimate" src="https://img.shields.io/badge/object-ResourceEstimate-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: estimate not observation" src="https://img.shields.io/badge/boundary-estimate__not__observation-critical">
</p>

`contracts/domains/geology/ResourceEstimate.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Estimate classes](#estimate-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/ResourceEstimate.md`  
> **Schema posture:** a lower-case scaffold exists at `schemas/contracts/v1/domains/geology/resource_estimate.schema.json`; its `x-kfm.contract_doc` points to lower-case `contracts/domains/geology/resource_estimate.md`, while the current requested contract path is PascalCase  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology object-family doctrine identifies `ResourceEstimate` as a modeled or compiled reserve/resource estimate distinct from deposits and occurrences. The scope document also notes naming drift because §10.C uses `ResourceEstimate` where §10.B says `Resource Deposit`. Field-level schema shape, casing, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `ResourceEstimate` is a modeled or compiled quantity/classification claim with assumptions. It does **not** prove `MineralOccurrence`, `ResourceDeposit`, direct measurement, reserve claim, economic viability, extraction, production, ownership/title, lease, permit authority, operator liability, hazards risk, public alert, or AI/UI truth by itself.

---

## Meaning

`ResourceEstimate` is the Geology semantic object for a source-supported modeled, compiled, classified, aggregated, or reported resource/reserve estimate claim.

It answers:

- Which estimate, classification, quantity, aggregation unit, commodity set, or source-native estimate record is being referenced?
- Which source, source role, source record, classification scheme, assumption set, model/version, geometry/aggregation posture, and rights/sensitivity state apply?
- Which mineral occurrences, resource deposits, geochemistry samples, geophysical observations, extraction sites, production records, reserve claims, or regulatory/legal records may be linked as context without collapsing identity?
- What public-safe aggregate, generalized, redacted, or suppressed derivative may be shown?
- Which policy decision, review record, redaction/aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

A resource estimate can describe a quantity or class under an explicit source scheme and assumption set. It is not the deposit itself, not observed presence, not a direct measurement, not automatically a reserve, not proof of production, and not an economic, legal, or public-safety statement.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Resource-estimate meaning | `contracts/domains/geology/ResourceEstimate.md` | Owned here by request; casing/membership drift remains open |
| Machine schema shape | `schemas/contracts/v1/domains/geology/resource_estimate.schema.json` | CONFIRMED scaffold; field shape still empty / PROPOSED |
| Schema/contract casing drift | `ResourceEstimate.md` vs `resource_estimate.schema.json` and lower-case `x-kfm.contract_doc` | CONFLICTED / NEEDS VERIFICATION |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms broader naming drift: §10.C uses `ResourceEstimate` where §10.B says `Resource Deposit` |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed keys, material times, sensitivity posture, source roles, and anti-collapse invariant |
| Natural-resources doctrine | `docs/domains/geology/sublanes/natural_resources.md` | Confirms `ResourceEstimate` documents are in the resource-focused sublane |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, aggregate, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

A paired schema exists only as a lower-case scaffold and does not yet enforce fields.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/ResourceEstimate.md` |
| Confirmed schema path | `schemas/contracts/v1/domains/geology/resource_estimate.schema.json` |
| Schema status | `PROPOSED` scaffold with empty `properties` and `additionalProperties: true` |
| Schema title | `Resource Estimate` |
| Schema contract pointer | `contracts/domains/geology/resource_estimate.md` |
| Casing/path posture | CONFLICTED / NEEDS VERIFICATION; requested PascalCase contract exists, schema points lower-case contract path |
| Membership posture | §E/§INDEX-18 + §C member, not in §B verbatim; §10.C uses `ResourceEstimate` where §10.B says `Resource Deposit` |
| Field-level enforcement | NEEDS VERIFICATION |

Until the casing, membership, and schema-field decisions are resolved, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `ResourceEstimate` should semantically assert:

1. **Estimate identity** — deterministic identity for the estimate record, source, classification scheme, aggregation unit, commodity set, temporal scope, and normalized digest.
2. **Modeled/compiled quantity posture** — explicit quantity/classification/aggregation claim with assumptions, not observation or deposit identity.
3. **Source identity** — SourceDescriptor, source record ID, source role, source time, valid time, rights, cadence, and attribution.
4. **Classification support** — classification scheme, reserve/resource category, confidence class, source-native terminology, and caveats.
5. **Assumption support** — method, model version, cutoff, commodity prices if source-used, aggregation basis, reporting standard, or source-native assumptions where available.
6. **Geometry/aggregation posture** — aggregation unit, deposit ref, project area, district, county, source geometry, generalized public geometry, withheld geometry, or unknown geometry.
7. **Evidence linkage** — source estimate table, report, model, dataset, deposit/occurrence context, samples, geophysics, production history context, EvidenceRef, or EvidenceBundle.
8. **Anti-collapse posture** — explicit separation from MineralOccurrence, ResourceDeposit, ReserveClaim, ExtractionSite, PermitRecord, ProductionRecord, ownership/title, and hazards identities.
9. **Temporal discipline** — source, valid, retrieval, release, and correction times remain distinct; observed time applies only to supporting evidence, not to the estimate as a direct observation.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating estimate as a mineral occurrence | Occurrence is reported presence; estimate is modeled/compiled quantity/classification. |
| Treating estimate as a resource deposit | Deposit is a named/delineated body; estimate is a quantity/classification claim. |
| Treating estimate as direct measurement | Estimates are modeled or compiled and must never be relabeled `observed`. |
| Treating estimate as reserve claim by default | Reserve status requires explicit classification scheme, assumptions, source role, and policy support. |
| Treating estimate as economic viability | Economic interpretation is not implied unless source/classification supports that narrow claim and KFM policy allows it. |
| Treating estimate as extraction or production proof | ExtractionSite and ProductionRecord remain separate. |
| Treating estimate as permit/title/ownership proof | People/Land or regulatory/legal roots own those claims. |
| Treating estimate as hazards risk | Hazards owns risk. Geology may supply context only. |
| Treating exact estimate geometry as public by default | Estimates are often restricted; aggregate/generalized outputs are safer. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM resource-estimate identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology` unless a future ADR creates a neutral resource-classification home. |
| `object_family` | `ResourceEstimate` or accepted canonical spelling after casing/path reconciliation. |
| `estimate_id` | Source-native or KFM estimate identifier. |
| `estimate_class` | Resource estimate, reserve estimate, prospective resource, inferred/indicated/measured class, aggregate estimate, model-derived estimate, candidate, or public derivative. |
| `commodity_set` | Commodity/mineral/material set as normalized and source-native terms. |
| `commodity_vocabulary_ref` | Vocabulary, code list, source classification, or commodity scheme ref. |
| `source_commodity_labels` | Source-native labels retained for audit. |
| `classification_scheme_ref` | Classification scheme, reporting standard, agency category, or source-native scheme. |
| `classification_label` | Normalized classification label. |
| `source_classification_label` | Source-native classification text retained for audit. |
| `aggregation_unit` | Deposit, district, field, county, project area, source geometry, commodity group, time period, or source-native unit. |
| `quantity_summary` | Public-safe summary of source quantity; include units/caveats or suppress if sensitive. |
| `quantity_units_ref` | Units vocabulary/ref for quantity values. |
| `assumption_set_ref` | Model assumptions, cutoff, method, price basis, recovery factor, or source-native assumption record. |
| `model_or_method_ref` | Model, method, estimation workflow, compiler, or reporting method. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules; never relabeled observed. |
| `source_record_ref` | Source-native estimate, report, table, map, inventory, model, literature, project, or dataset record. |
| `location_ref_internal` | Access-controlled exact/source geometry ref, if any. |
| `public_geometry_ref` | Generalized or aggregate public-safe geometry ref, if released. |
| `public_safe_geometry_fingerprint` | Stable fingerprint of released/generalized/aggregate geometry. |
| `geometry_precision` | Exact, source precision, generalized, aggregate, withheld, unknown. |
| `mineral_occurrence_refs` | Linked MineralOccurrence refs only where evidence supports relationship; not identity equality. |
| `resource_deposit_refs` | Linked ResourceDeposit refs only where evidence supports relationship; not identity equality. |
| `geochemistry_sample_refs` | Linked GeochemistrySample evidence. |
| `geophysical_observation_refs` | Linked GeophysicalObservation evidence. |
| `extraction_site_refs` | Linked ExtractionSite refs only where evidence supports relationship; not extraction proof. |
| `production_context_refs` | Production context refs only where source supports relationship; not estimate identity. |
| `reserve_claim_refs` | ReserveClaim refs where source/policy supports explicit relationship; ownership/home NEEDS VERIFICATION. |
| `permit_context_refs` | Permit/regulatory context refs, not title or legal proof by themselves. |
| `operator_context_refs` | Operator/source context refs with time and role caveats. |
| `land_context_refs` | Land/parcel/ownership/title context refs only as non-authoritative context unless owning lane confirms. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the estimate claim is considered valid, where applicable. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Restricted-detail, aggregate-public, generalized-public, source-limited, rights-limited, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release where material. |
| `review_record_ref` | Source, geology, natural-resources, sensitivity, estimate-method, or release review. |
| `redaction_receipt_ref` | Required when estimate detail/geometry/quantity is generalized or withheld. |
| `aggregation_receipt_ref` | Required when estimates become aggregate public products. |
| `validation_report_ref` | Validation report for schema, source role, classification, quantities, assumptions, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, quantity correction, classification correction, assumption correction, geometry correction, sensitivity update, and rollback lineage. |
| `quality_flags` | Source-role conflict, estimate/deposit collapse, estimate/occurrence collapse, missing classification scheme, missing assumptions, unit conflict, rights unknown, sensitivity unknown, stale source, or incomplete evidence. |

---

## Estimate classes

| Class | Meaning | Default posture |
|---|---|---|
| `resource_estimate` | Source-supported resource quantity/classification estimate. | Modeled/aggregate; restricted detail by default. |
| `reserve_estimate` | Estimate explicitly classified as reserve by source scheme. | Highly sensitive; classification and assumptions required. |
| `prospective_resource` | Prospective or hypothetical source-estimate class. | Modeled; not observed; caveats mandatory. |
| `classification_record` | Source-native classification without full quantity exposure. | Administrative/aggregate context. |
| `aggregate_estimate` | County/district/field/commodity aggregate estimate. | Public-safe only after aggregation release. |
| `model_derived_estimate` | Model-derived quantity or potential. | Modeled; never observed. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical estimate. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released generalized, redacted, or aggregate representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | ResourceEstimate posture |
|---|---|---|
| Published resource/reserve estimate report | `modeled` or `aggregate` | Estimate claim with assumptions; never direct observation. |
| Agency/industry compilation table | `aggregate` | Compiled estimate support; preserve source/completeness caveats. |
| Model output, potential map, inferred quantity | `modeled` | Model output; not observed, not deposit identity. |
| Classification scheme/code-list row | `administrative` | Defines categories/labels, not quantity truth by itself. |
| Regulatory or permit-linked estimate record | `regulatory` or `administrative` | Context only; not title/permit/extraction proof. |
| Unreviewed import, missing assumptions, unit conflict, fuzzy deposit link | `candidate` | Quarantine until source role, classification, assumptions, units, rights, and geometry resolve. |
| AI-generated or hypothetical estimate | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`ResourceEstimate` is one of the load-bearing Natural Resources anti-collapse objects.

```text
ResourceEstimate != MineralOccurrence
ResourceEstimate != ResourceDeposit
ResourceEstimate != ReserveClaim by default
ResourceEstimate != ExtractionSite
ResourceEstimate != ProductionRecord
ResourceEstimate != PermitRecord
ResourceEstimate != direct measurement
ResourceEstimate != ownership / lease / title proof
ResourceEstimate != Hazards risk
ResourceEstimate != AI summary
```

Any join to occurrence, deposit, extraction site, permit, production record, reclamation record, reserve claim, or ownership/title context must be explicit, evidence-bound, source-role-aware, time-aware, policy-reviewed where material, and non-identifying unless a future ADR/schema explicitly defines a relationship type.

Joining occurrence/deposit/estimate as identity equality is a validation `DENY` and an AI/public-surface `ABSTAIN`.

---

## Sensitivity and release

Resource estimates are sensitive by default because they can imply economic value, reserves, production potential, operational interest, or land/title-adjacent significance. Public release should prefer aggregate, redacted, generalized, or qualitative derivatives unless evidence, rights, sensitivity review, classification review, and release support allow more detail.

Rules:

- Resource estimates must never be published as observed truth.
- Exact/detail estimate geometry, quantities, assumptions, or source-sensitive classes are not automatically public.
- Public derivatives should use aggregate regions, generalized geometry, redacted quantities, classification-only summaries, or suppression where needed.
- Public outputs must preserve source role, source time, valid time, classification scheme, aggregation unit, assumptions, quantity caveats, rights posture, and anti-collapse caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, classification-unknown, assumption-missing, stale, or evidence-incomplete records must not enter public outputs as authoritative estimate facts.
- Estimate detail must not be used to imply deposit identity, occurrence presence, reserve status, economic viability, extraction, ownership, permit authority, production, public safety, or hazards risk.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision where material, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native estimate rows, reports, tables, quantities, units, classifications, assumptions, model outputs, maps, and notes remain source-bound. |
| WORK / QUARANTINE | Candidate estimates are normalized, source-role checked, classification-mapped, assumption-linked, unit-checked, identity-crosswalked, rights/sensitivity-screened, geometry-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, source support, commodity support, classification scheme, aggregation unit, assumption refs, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, evidence, classification scheme, assumptions, units, aggregation posture, access state, and anti-collapse caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision/review where material, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released aggregate, redacted, generalized, or classification-safe estimate derivatives appear in public clients. |
| CORRECTION | Source update, quantity correction, unit correction, classification remap, assumption update, identity merge/split, sensitivity change, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve casing/path drift between `ResourceEstimate.md`, lower-case schema file, and lower-case schema `contract_doc` pointer.
- [ ] Resolve membership drift: §E/§C `ResourceEstimate` vs §B `Resource Deposit` naming overlap.
- [ ] Expand `resource_estimate.schema.json` from scaffold into field-level validation, or record the accepted schema path via ADR/schema PR.
- [ ] Add valid fixtures for resource estimate, reserve estimate, prospective resource, classification record, aggregate estimate, model-derived estimate, candidate import, synthetic example, and public aggregate/redacted derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, missing estimate ID, missing commodity set, missing classification scheme, missing assumptions, unit conflict, estimate relabeled observed, estimate treated as deposit, estimate treated as occurrence, estimate treated as extraction/permit/ownership/title proof, sensitive quantity public without release, missing policy decision where material, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, estimate ID, commodity set, classification scheme, aggregation unit, source ID, source role, quantities/units, assumption refs, temporal support, evidence refs, sensitivity state, policy refs, release refs, correction refs, and anti-collapse constraints.
- [ ] Add policy/access tests proving public clients consume released aggregate/generalized/redacted derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, quantity correction, unit correction, classification remap, assumption update, identity merge/split, sensitivity update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, classification/assumptions are clear, source role is modeled/aggregate, derivative is released | `ANSWER` / public-safe estimate derivative may be shown |
| Evidence, rights, source role, classification, assumptions, units, identity, geometry, or sensitivity support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, release is absent, estimate is relabeled observed, or estimate is collapsed into occurrence/deposit/title/risk | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Confirmed schema scaffold | Confirms lower-case schema file exists, is PROPOSED, and currently has empty properties. | Does not prove field validation; also exposes casing/path drift. |
| Geology scope doc | Confirms naming drift: §10.C uses `ResourceEstimate` where §10.B says `Resource Deposit`; it also confirms Resource Deposit is not an estimate. | Does not prove schema or implementation enforcement. |
| Geology object-family doc | Confirms ResourceEstimate purpose, proposed key fields, material times, sensitivity posture, source roles, and anti-collapse invariant. | Field realization remains PROPOSED. |
| Natural Resources sublane doc | Confirms `ResourceEstimate` documents are in Natural Resources scope and that truth lives in EvidenceBundle, not UI/AI narrative. | Sublane placement remains PROPOSED in that doc. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized ResourceEstimate weakens source integrity, misstates source role, exposes restricted detail, hides assumptions, or collapses estimate into occurrence, deposit, reserve, extraction, permit, production, title, ownership, or risk truth.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source estimate record corrected, withdrawn, merged, or split;
- quantity, units, commodity vocabulary, classification scheme, aggregation unit, assumption set, or source label corrected;
- estimate geometry or public-safe derivative corrected;
- estimate was presented as observed, direct measurement, deposit identity, occurrence presence, reserve claim without support, economic viability, owned, mined, permitted, producing, or hazardous;
- public derivative exposes restricted detail or lacks redaction/aggregation receipt where needed;
- release manifest lacks policy decision where material, correction path, or rollback target;
- public API/UI/AI reads RAW/WORK/QUARANTINE or candidate records as public truth.

Rollback artifacts should include affected ResourceEstimate IDs, source record IDs, commodity refs, classification scheme refs, assumption refs, quantity/unit refs, aggregation refs, geometry refs, public derivative refs, linked occurrence/deposit/extraction/production/context refs, release IDs, evidence refs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should the contract file be PascalCase `ResourceEstimate.md` or lower-case `resource_estimate.md` to match the schema scaffold pointer? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted schema path and casing for `ResourceEstimate`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| How should §10.C/§E `ResourceEstimate` relate to §10.B `Resource Deposit` without collapsing identities? | CONFLICTED / NEEDS VERIFICATION | Natural-resources ADR and anti-collapse tests. |
| Which resource/reserve classification schemes are canonical or allowed? | NEEDS VERIFICATION | Source registry, schema, and natural-resources steward review. |
| Which estimate quantities/classes are public-safe by source family and commodity? | NEEDS VERIFICATION | Policy, sensitivity, and release fixture review. |
| What relationship predicates connect estimate to occurrence, deposit, extraction site, production, reserve claim, and reclamation without identity collapse? | NEEDS VERIFICATION | Natural-resources ADR and graph/triplet contract review. |
| How should AI/MapLibre surfaces phrase estimate evidence without implying observed truth or economic certainty? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/MineralOccurrence.md` — reported mineral presence, not estimate identity.
- `contracts/domains/geology/ResourceDeposit.md` — named/delineated deposit body, not estimate identity.
- `contracts/domains/geology/GeochemistrySample.md` — sample/analyte evidence that may support resource review.
- `contracts/domains/geology/GeophysicalObservation.md` — geophysical evidence or anomaly context.
- `contracts/domains/geology/ExtractionSite.md` — extraction site context, not estimate proof.
- `contracts/domains/geology/ReclamationRecord.md` — reclamation status/context, not estimate proof.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary and naming drift.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference and anti-collapse invariant.
- `docs/domains/geology/sublanes/natural_resources.md` — Natural Resources sublane doctrine.
- `schemas/contracts/v1/domains/geology/resource_estimate.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve PascalCase vs lower-case contract/schema path drift.
- [ ] Resolve ResourceEstimate vs ResourceDeposit membership drift.
- [ ] Expand paired schema and fixtures.
- [ ] Add anti-collapse tests for estimate/occurrence/deposit/reserve/extraction/permit/production/title/risk distinctions.
- [ ] Add classification-scheme, assumption, quantity/unit, and source-role validation fixtures.
- [ ] Add policy tests for restricted/detail vs aggregate/generalized/redacted public derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released aggregate/generalized/redacted estimate derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved casing/path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
