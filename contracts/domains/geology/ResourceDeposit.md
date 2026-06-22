<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-resource-deposit
title: ResourceDeposit Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Natural-resources steward
  - OWNER_TBD — Resource-deposit steward
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
policy_label: restricted-by-default; semantic-contract; geology; resource-deposit; natural-resources; anti-collapse; source-role-aware; release-gated; public-aggregate-or-generalized
tags: [kfm, contracts, geology, ResourceDeposit, resource-deposit, natural-resources, commodity, deposit-body, characterization, administrative-context, aggregate, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./MineralOccurrence.md
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
  - ../../../schemas/contracts/v1/domains/geology/resource_deposit.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology ResourceDeposit semantic contract."
  - "A lower-case schema scaffold exists at schemas/contracts/v1/domains/geology/resource_deposit.schema.json, while this requested contract path uses PascalCase. The schema's x-kfm.contract_doc points to contracts/domains/geology/resource_deposit.md, creating a casing/path drift that remains CONFLICTED / NEEDS VERIFICATION."
  - "ResourceDeposit means a named or delineated body of material with characterization. It does not prove quantified resource/reserve estimate, economic viability, production, extraction, ownership, permit authority, or hazards risk."
  - "Sensitive/detail deposit geometry is restricted or generalized by default; public outputs require evidence, rights, validation, policy/review where material, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ResourceDeposit — Geology

> Semantic contract for Geology `ResourceDeposit`: the evidence-bound object for a named or delineated deposit body, commodity context, source role, public-safe geometry, sensitivity posture, correction, and rollback — explicitly distinct from occurrences, estimates, reserves, extraction, ownership, permits, production, and hazards risk.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: ResourceDeposit" src="https://img.shields.io/badge/object-ResourceDeposit-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: deposit not estimate or reserve" src="https://img.shields.io/badge/boundary-deposit__not__estimate__or__reserve-critical">
</p>

`contracts/domains/geology/ResourceDeposit.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Deposit classes](#deposit-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/ResourceDeposit.md`  
> **Schema posture:** a lower-case scaffold exists at `schemas/contracts/v1/domains/geology/resource_deposit.schema.json`; its `x-kfm.contract_doc` points to lower-case `contracts/domains/geology/resource_deposit.md`, while the current requested contract path is PascalCase  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Resource Deposit` as an owned object family: a delineated or named body with characterization, **not** an estimate. Field-level schema shape, casing, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `ResourceDeposit` is deposit-body / characterization evidence. It does **not** prove `MineralOccurrence`, `ResourceEstimate`, economic viability, reserve quantity, extraction, production, ownership/title, lease, permit authority, operator liability, reclamation state, hazards risk, public alert, or AI/UI truth by itself.

---

## Meaning

`ResourceDeposit` is the Geology semantic object for a named, delineated, or source-characterized body of material treated as a resource deposit in a source system, map, report, inventory, or compiled dataset.

It answers:

- Which deposit body or source-native deposit record is being referenced?
- Which commodity/material set, source, source role, source record, characterization basis, geometry posture, and rights/sensitivity state apply?
- Which mineral occurrences, geochemistry samples, geophysical observations, lithology records, geologic units, extraction sites, estimates, reclamation records, or regulatory/legal records may be linked as context without collapsing identity?
- What public-safe geometry, aggregate summary, or generalized deposit derivative may be shown?
- Which policy decision, review record, redaction/aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

A resource deposit means a source-supported deposit body or characterized resource body exists as a named/delineated object. It does not mean the body is quantified, economic, permitted, owned, producing, reserved, safe, hazardous, or legally actionable.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Resource-deposit meaning | `contracts/domains/geology/ResourceDeposit.md` | Owned here by request; casing drift remains open |
| Machine schema shape | `schemas/contracts/v1/domains/geology/resource_deposit.schema.json` | CONFIRMED scaffold; field shape still empty / PROPOSED |
| Schema/contract casing drift | `ResourceDeposit.md` vs `resource_deposit.schema.json` and lower-case `x-kfm.contract_doc` | CONFLICTED / NEEDS VERIFICATION |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms Resource Deposit as delineated body with characterization, not estimate |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed keys, material times, sensitivity posture, and source roles |
| Natural-resources doctrine | `docs/domains/geology/sublanes/natural_resources.md` | Confirms resource-focused scope and anti-collapse posture |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, aggregate, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

A paired schema exists only as a lower-case scaffold and does not yet enforce fields.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/ResourceDeposit.md` |
| Confirmed schema path | `schemas/contracts/v1/domains/geology/resource_deposit.schema.json` |
| Schema status | `PROPOSED` scaffold with empty `properties` and `additionalProperties: true` |
| Schema title | `Resource Deposit` |
| Schema contract pointer | `contracts/domains/geology/resource_deposit.md` |
| Casing/path posture | CONFLICTED / NEEDS VERIFICATION; requested PascalCase contract exists, schema points lower-case contract path |
| Field-level enforcement | NEEDS VERIFICATION |

Until the casing and schema-field decision is resolved, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `ResourceDeposit` should semantically assert:

1. **Deposit identity** — deterministic identity for the deposit record, source, commodity set, public-safe geometry fingerprint, temporal scope, and normalized digest.
2. **Deposit-body characterization** — source-supported named/delineated body with characterization, not a quantity estimate.
3. **Source identity** — SourceDescriptor, source record ID, source role, source time, valid time, rights, cadence, and attribution.
4. **Commodity/material support** — commodity set, mineral/material labels, source-native terms, normalized vocabulary, and caveats.
5. **Geometry posture** — exact/internal geometry, source geometry, generalized public geometry, aggregate geography, withheld geometry, or unknown geometry.
6. **Evidence linkage** — map, report, inventory, geologic unit, occurrence set, geochemistry/geophysics, literature record, source database, EvidenceRef, or EvidenceBundle.
7. **Anti-collapse posture** — explicit separation from MineralOccurrence, ResourceEstimate, ReserveClaim, ExtractionSite, PermitRecord, ProductionRecord, ownership/title, and hazards identities.
8. **Sensitivity posture** — aggregate-public, generalized-public, restricted detail, rights-limited, active-sensitive, public-safe, withheld, or unknown state.
9. **Temporal discipline** — source, valid, retrieval, release, and correction times remain distinct; observed time is used only when a source actually supports observed deposit-characterization events.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a deposit as a mineral occurrence | Occurrence is reported presence; deposit is a named/delineated body. The identities remain distinct. |
| Treating a deposit as a resource estimate | Estimates quantify/classify assumptions and quantities; deposits do not by identity carry estimates. |
| Treating deposit as reserve or economic viability | Reserve/economic claims require separate classification, assumptions, and authority. |
| Treating deposit as extraction proof | ExtractionSite and ProductionRecord remain separate. |
| Treating deposit as permit/title/ownership proof | People/Land or regulatory/legal roots own those claims. |
| Treating deposit as hazards risk | Hazards owns risk. Geology may supply context only. |
| Treating geochemistry/geophysics as deposit identity without review | Samples/observations are evidence, not deposit identity by themselves. |
| Treating exact deposit coordinates as public by default | Sensitive/detail geometry requires redaction/generalization or denial. |
| Treating public aggregate summary as exact deposit truth | Public summaries are derivatives with caveats. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM resource-deposit identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `ResourceDeposit` or accepted canonical spelling after casing/path reconciliation. |
| `deposit_id` | Source-native or KFM deposit identifier. |
| `deposit_class` | Named deposit, delineated deposit, district/field deposit, compiled deposit, candidate, aggregate, or public derivative. |
| `deposit_name` | Public-safe deposit name or source-native name after review. |
| `source_deposit_name` | Source-native label retained for audit. |
| `commodity_set` | Commodity/mineral/material set as normalized and source-native terms. |
| `commodity_vocabulary_ref` | Vocabulary, code list, source classification, or commodity scheme ref. |
| `source_commodity_labels` | Source-native labels retained for audit. |
| `characterization_summary` | Public-safe characterization summary; not quantity/economic proof. |
| `classification_context_ref` | Optional source classification context; not a ResourceEstimate unless estimate evidence exists. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Administrative, aggregate, observed, modeled, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native deposit, report, database, map, literature, inventory, district, or field record. |
| `location_ref_internal` | Access-controlled exact/source geometry ref. |
| `public_geometry_ref` | Generalized or aggregate public-safe geometry ref, if released. |
| `public_safe_geometry_fingerprint` | Stable fingerprint of released/generalized/aggregate geometry. |
| `geometry_precision` | Exact, source precision, generalized, aggregate, withheld, unknown. |
| `coordinate_uncertainty` | Source/native/georeferenced uncertainty. |
| `evidence_summary` | Public-safe summary of evidence basis. |
| `mineral_occurrence_refs` | Linked MineralOccurrence refs, not identity equality. |
| `geochemistry_sample_refs` | Linked GeochemistrySample evidence. |
| `geophysical_observation_refs` | Linked GeophysicalObservation evidence. |
| `lithology_refs` | Linked Lithology/material-character evidence. |
| `geologic_unit_refs` | Linked GeologicUnit or SurficialUnit context. |
| `resource_estimate_refs` | Linked ResourceEstimate refs only where evidence supports relationship; not identity equality. |
| `extraction_site_refs` | Linked ExtractionSite refs only where evidence supports relationship; not extraction proof. |
| `reclamation_record_refs` | Linked ReclamationRecord refs only where evidence supports relationship; not status/compliance proof. |
| `permit_context_refs` | Permit/regulatory context refs, not title or legal proof by themselves. |
| `operator_context_refs` | Operator/source context refs with time and role caveats. |
| `land_context_refs` | Land/parcel/ownership/title context refs only as non-authoritative context unless owning lane confirms. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the deposit characterization is considered valid, where applicable. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Aggregate-public, generalized-public, restricted-detail, resource-sensitive, rights-limited, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release where material. |
| `review_record_ref` | Source, geology, natural-resources, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when deposit detail/geometry is generalized or withheld. |
| `aggregation_receipt_ref` | Required when deposits become aggregate public products. |
| `validation_report_ref` | Validation report for schema, source role, geometry, commodity vocabulary, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, commodity correction, geometry correction, sensitivity update, identity merge/split, and rollback lineage. |
| `quality_flags` | Source-role conflict, identity collision, commodity conflict, geometry uncertainty, rights unknown, sensitivity unknown, occurrence/deposit collapse, estimate collapse, stale source, or incomplete evidence. |

---

## Deposit classes

| Class | Meaning | Default posture |
|---|---|---|
| `named_deposit` | Source-supported named deposit or body. | Administrative/aggregate unless direct observation evidence resolves. |
| `delineated_deposit` | Source-supported mapped/delineated deposit extent. | Detail may restrict; public geometry usually generalized/aggregate. |
| `district_or_field` | Deposit district, field, trend, or grouped source-native resource body. | Aggregate/administrative; caveats required. |
| `compiled_deposit` | Deposit compiled from literature/database rollups. | Aggregate; source and completeness caveats material. |
| `sample_supported_context` | Deposit relationship supported by sample/assay evidence. | Evidence-bound; samples do not become deposit identity. |
| `geophysical_context` | Deposit relationship supported by geophysical interpretation. | Modeled/interpreted unless source says otherwise. |
| `aggregate_public_summary` | Aggregate geography/count/commodity summary. | Public-safe only with release support. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical deposit. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released generalized or aggregate representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | ResourceDeposit posture |
|---|---|---|
| Agency/mining database deposit record | `administrative` or `aggregate` | Deposit context; not economic/reserve proof by itself. |
| Published resource map or deposit inventory | `aggregate` | Compiled deposit support; preserve source scale/completeness caveats. |
| Field/literature report describing deposit body | `observed` with interpretation caveat | Evidence-bearing only if source supports deposit-body characterization. |
| Modeled prospectivity, inferred deposit extent, or exploration target | `modeled` | Model output; not observed deposit unless independently supported. |
| Permit/lease/production/operator record | `regulatory` or `administrative` | Context only; not deposit proof without deposit evidence. |
| Unreviewed import, fuzzy match, unresolved commodity, geometry conflict | `candidate` | Quarantine until identity, source role, commodity, rights, and geometry resolve. |
| AI-generated or hypothetical deposit | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`ResourceDeposit` is one of the load-bearing Natural Resources anti-collapse objects.

```text
ResourceDeposit != MineralOccurrence
ResourceDeposit != ResourceEstimate
ResourceDeposit != ReserveClaim
ResourceDeposit != ExtractionSite
ResourceDeposit != ProductionRecord
ResourceDeposit != PermitRecord
ResourceDeposit != ownership / lease / title proof
ResourceDeposit != Hazards risk
ResourceDeposit != AI summary
```

Any join to occurrence, estimate, extraction site, permit, production record, reclamation record, reserve claim, or ownership/title context must be explicit, evidence-bound, source-role-aware, time-aware, policy-reviewed where material, and non-identifying unless a future ADR/schema explicitly defines a relationship type.

Joining occurrence/deposit/estimate as identity equality is a validation `DENY` and an AI/public-surface `ABSTAIN`.

---

## Sensitivity and release

Resource deposits can expose resource-sensitive, land/title-adjacent, extraction-adjacent, proprietary, or operationally sensitive information. The safe default is to publish only aggregate or generalized public-safe derivatives unless evidence, rights, sensitivity review, and release support allow more detail.

Rules:

- Exact/detail deposit geometry is not automatically public.
- Public derivatives should use aggregate regions, generalized points/polygons, public-safe commodity classes, or suppression where needed.
- Public outputs must preserve source role, source time, valid time, geometry precision, commodity caveats, rights posture, and anti-collapse caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, stale, or evidence-incomplete records must not enter public outputs as authoritative deposit facts.
- Deposit detail must not be used to imply quantified resource, reserve quantity, economic viability, extraction, ownership, permit authority, production, public safety, or hazards risk.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision where material, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native deposit rows, maps, reports, coordinates, commodity labels, database IDs, and source notes remain source-bound. |
| WORK / QUARANTINE | Candidate deposits are normalized, source-role checked, commodity-mapped, identity-crosswalked, rights/sensitivity-screened, geometry-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, source support, commodity support, characterization posture, geometry posture, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, evidence, geometry precision, commodity vocabulary, access state, and anti-collapse caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision/review where material, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released aggregate or generalized public-safe deposit derivatives appear in public clients. |
| CORRECTION | Source update, deposit identity merge/split, commodity correction, geometry correction, sensitivity change, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve casing/path drift between `ResourceDeposit.md`, lower-case schema file, and lower-case schema `contract_doc` pointer.
- [ ] Expand `resource_deposit.schema.json` from scaffold into field-level validation, or record the accepted schema path via ADR/schema PR.
- [ ] Add valid fixtures for named deposit, delineated deposit, district/field deposit, compiled deposit, sample-supported context, geophysical context, aggregate public summary, candidate import, synthetic example, and public generalized derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, missing deposit ID, missing commodity set, identity collision, deposit treated as occurrence, deposit treated as estimate/reserve, deposit treated as extraction/permit/ownership/title proof, exact sensitive public geometry, missing policy decision where material, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, deposit ID, commodity set, source ID, public-safe geometry fingerprint, source role, temporal support, evidence refs, sensitivity state, policy refs, release refs, correction refs, and anti-collapse constraints.
- [ ] Add policy/access tests proving public clients consume released aggregate/generalized derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, commodity remap, identity merge/split, geometry correction, sensitivity update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, source role is clear, geometry is public-safe or released, derivative is released | `ANSWER` / public-safe deposit derivative may be shown |
| Evidence, rights, source role, commodity, identity, geometry, or sensitivity support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, release is absent, or deposit is collapsed into occurrence/estimate/title/risk | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Confirmed schema scaffold | Confirms lower-case schema file exists, is PROPOSED, and currently has empty properties. | Does not prove field validation; also exposes casing/path drift. |
| Geology scope doc | Confirms Geology owns Resource Deposit and defines it as a delineated body with characterization, not an estimate. | Does not prove schema or implementation enforcement. |
| Geology object-family doc | Confirms purpose, proposed key fields, material times, sensitivity posture, source roles, and anti-collapse invariant. | Field realization remains PROPOSED. |
| Natural Resources sublane doc | Confirms resource-focused scope and that Resource Deposit belongs with mineral evidence and resource characterization. | Sublane placement remains PROPOSED in that doc. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized ResourceDeposit weakens source integrity, misstates source role, exposes restricted detail, or collapses deposit into occurrence, estimate, reserve, extraction, permit, production, title, ownership, or risk truth.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source deposit record corrected, withdrawn, merged, or split;
- commodity vocabulary, commodity set, deposit name, or source label corrected;
- deposit geometry or public-safe derivative corrected;
- deposit was presented as quantified, economic, measured, owned, mined, permitted, producing, reserved, or hazardous;
- public derivative exposes restricted detail or lacks redaction/aggregation receipt where needed;
- release manifest lacks policy decision where material, correction path, or rollback target;
- public API/UI/AI reads RAW/WORK/QUARANTINE or candidate records as public truth.

Rollback artifacts should include affected ResourceDeposit IDs, source record IDs, commodity refs, geometry refs, public derivative refs, linked occurrence/estimate/extraction/reclamation/context refs, release IDs, evidence refs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should the contract file be PascalCase `ResourceDeposit.md` or lower-case `resource_deposit.md` to match the schema scaffold pointer? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted schema path and casing for `ResourceDeposit`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which commodity/deposit classification vocabulary is canonical for KFM deposit records? | NEEDS VERIFICATION | Source registry, schema, and natural-resources steward review. |
| Which deposit-detail geometries are public-safe by source family and commodity? | NEEDS VERIFICATION | Policy, sensitivity, and release fixture review. |
| What relationship predicates connect deposit to occurrence, estimate, extraction site, and reclamation without identity collapse? | NEEDS VERIFICATION | Natural-resources ADR and anti-collapse tests. |
| How should AI/MapLibre surfaces phrase deposit evidence without implying quantified resource or economic value? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/MineralOccurrence.md` — reported mineral presence, not deposit identity.
- `contracts/domains/geology/GeochemistrySample.md` — sample/analyte evidence that may support deposit review.
- `contracts/domains/geology/GeophysicalObservation.md` — geophysical evidence or anomaly context.
- `contracts/domains/geology/ExtractionSite.md` — extraction site context, not deposit proof.
- `contracts/domains/geology/ReclamationRecord.md` — reclamation status/context, not deposit proof.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference and anti-collapse invariant.
- `docs/domains/geology/sublanes/natural_resources.md` — Natural Resources sublane doctrine.
- `schemas/contracts/v1/domains/geology/resource_deposit.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve PascalCase vs lower-case contract/schema path drift.
- [ ] Expand paired schema and fixtures.
- [ ] Add anti-collapse tests for deposit/occurrence/estimate/extraction/permit/production/title/risk distinctions.
- [ ] Add commodity/deposit classification vocabulary and source-role validation fixtures.
- [ ] Add policy tests for restricted/detail vs aggregate/generalized public derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released aggregate/generalized deposit derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved casing/path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
