<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-mineral-occurrence
title: MineralOccurrence Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Natural-resources steward
  - OWNER_TBD — Mineral-occurrence steward
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
policy_label: restricted-by-default; semantic-contract; geology; mineral-occurrence; natural-resources; anti-collapse; source-role-aware; release-gated; public-aggregate-or-generalized
tags: [kfm, contracts, geology, MineralOccurrence, mineral-occurrence, natural-resources, commodity, reported-presence, observation, aggregate, resource-context, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./GeochemistrySample.md
  - ./GeophysicalObservation.md
  - ./ResourceDeposit.md
  - ./ExtractionSite.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../docs/domains/geology/sublanes/geochemistry.md
  - ../../../docs/domains/geology/sublanes/geophysics.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology MineralOccurrence semantic contract."
  - "A lower-case schema scaffold exists at schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json, while this requested contract path uses PascalCase. The schema's x-kfm.contract_doc points to contracts/domains/geology/mineral_occurrence.md, creating a casing/path drift that remains CONFLICTED / NEEDS VERIFICATION."
  - "MineralOccurrence means reported mineral presence. It does not prove economic value, deposit identity, resource/reserve estimate, extraction, ownership, permit authority, production, or hazards risk."
  - "Sensitive/detail occurrence geometry is restricted or generalized by default; public outputs require evidence, rights, validation, policy/review where material, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MineralOccurrence — Geology

> Semantic contract for Geology `MineralOccurrence`: the evidence-bound object for a reported mineral presence, commodity context, source role, public-safe geometry, sensitivity posture, correction, and rollback — explicitly distinct from deposits, estimates, extraction, ownership, permits, production, reserves, and hazards risk.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: MineralOccurrence" src="https://img.shields.io/badge/object-MineralOccurrence-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: occurrence not deposit or estimate" src="https://img.shields.io/badge/boundary-occurrence__not__deposit__or__estimate-critical">
</p>

`contracts/domains/geology/MineralOccurrence.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Occurrence classes](#occurrence-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/MineralOccurrence.md`  
> **Schema posture:** a lower-case scaffold exists at `schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json`; its `x-kfm.contract_doc` points to lower-case `contracts/domains/geology/mineral_occurrence.md`, while the current requested contract path is PascalCase  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Mineral Occurrence` as an owned object family: a documented/reported mineral presence, **not** a deposit and **not** an estimate. Field-level schema shape, casing, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `MineralOccurrence` is an occurrence/presence evidence object. It does **not** prove `ResourceDeposit`, `ResourceEstimate`, economic viability, reserve quantity, extraction, ownership/title, lease, permit authority, production, reclamation state, hazards risk, public alert, or AI/UI truth by itself.

---

## Meaning

`MineralOccurrence` is the Geology semantic object for a reported presence of a mineral, commodity, material, or resource-relevant observation at a source-supported place or area.

It answers:

- Which mineral, commodity, material, or occurrence record was reported?
- Which source, source role, source record, evidence, observation/compilation time, geometry posture, and rights/sensitivity state apply?
- Which geochemistry, geophysics, lithology, geologic unit, extraction-site, or resource-context records may support or cite this occurrence without collapsing identity?
- What public-safe geometry, aggregate summary, or generalized occurrence derivative may be shown?
- Which policy decision, review record, redaction/aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

A mineral occurrence means material was reported, observed, compiled, or otherwise source-supported as present. It does not mean the material is economic, measured, mined, owned, permitted, producible, safe, hazardous, or quantified.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Mineral-occurrence meaning | `contracts/domains/geology/MineralOccurrence.md` | Owned here by request; casing drift remains open |
| Machine schema shape | `schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json` | CONFIRMED scaffold; field shape still empty / PROPOSED |
| Schema/contract casing drift | `MineralOccurrence.md` vs `mineral_occurrence.schema.json` and lower-case `x-kfm.contract_doc` | CONFLICTED / NEEDS VERIFICATION |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms occurrence is documented presence, not deposit/estimate |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed keys, material times, sensitivity posture, and source roles |
| Natural-resources doctrine | `docs/domains/geology/sublanes/natural_resources.md` | Confirms natural-resource sublane scope and anti-collapse posture |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, aggregate, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

A paired schema exists only as a lower-case scaffold and does not yet enforce fields.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/MineralOccurrence.md` |
| Confirmed schema path | `schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json` |
| Schema status | `PROPOSED` scaffold with empty `properties` and `additionalProperties: true` |
| Schema title | `Mineral Occurrence` |
| Schema contract pointer | `contracts/domains/geology/mineral_occurrence.md` |
| Casing/path posture | CONFLICTED / NEEDS VERIFICATION; requested PascalCase contract exists, schema points lower-case contract path |
| Field-level enforcement | NEEDS VERIFICATION |

Until the casing and schema-field decision is resolved, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `MineralOccurrence` should semantically assert:

1. **Occurrence identity** — deterministic identity for the occurrence record, source, commodity set, public-safe geometry fingerprint, temporal scope, and normalized digest.
2. **Reported presence** — a source-supported mineral/material/commodity presence claim with observation or compilation caveats.
3. **Source identity** — SourceDescriptor, source record ID, source role, source time, observed time where material, rights, cadence, and attribution.
4. **Commodity/material support** — commodity set, mineral/material labels, source-native terms, normalized vocabulary, and uncertainty/caveats.
5. **Geometry posture** — exact/internal geometry, source geometry, generalized public geometry, aggregate geography, withheld geometry, or unknown geometry.
6. **Evidence linkage** — field report, sample, geochemistry, geophysics, geologic map, literature record, source database, EvidenceRef, or EvidenceBundle.
7. **Anti-collapse posture** — explicit separation from ResourceDeposit, ResourceEstimate, ExtractionSite, permit, production, ownership/title, reserve, and hazards identities.
8. **Sensitivity posture** — aggregate-public, generalized-public, restricted detail, rights-limited, active-sensitive, public-safe, withheld, or unknown state.
9. **Temporal discipline** — source, observed, valid where applicable, retrieval, release, and correction times remain distinct.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating an occurrence as a deposit | A reported presence is not a delineated resource body. |
| Treating an occurrence as an estimate or reserve | Quantified estimates require assumptions, classification, and separate modeled/aggregate governance. |
| Treating occurrence as economic viability | Economic interpretation is not implied by presence. |
| Treating occurrence as extraction proof | ExtractionSite and production records remain separate. |
| Treating occurrence as ownership, lease, permit, or title proof | People/Land or regulatory/legal sources own those claims. |
| Treating occurrence as hazards risk | Hazards owns risk. Geology may supply context only. |
| Treating high geochemistry values as an occurrence without review | GeochemistrySample is evidence; occurrence identity requires source-role and evidence review. |
| Treating exact occurrence coordinates as public by default | Sensitive/detail geometry requires redaction/generalization or denial. |
| Treating public aggregate summary as exact occurrence truth | Public summaries are derivatives with caveats. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM mineral-occurrence identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `MineralOccurrence` or accepted canonical spelling after casing/path reconciliation. |
| `occurrence_id` | Source-native or KFM occurrence identifier. |
| `occurrence_class` | Field occurrence, compiled occurrence, sample-supported occurrence, geophysical anomaly-supported occurrence, historical occurrence, candidate, aggregate, or public derivative. |
| `commodity_set` | Commodity/mineral/material set as normalized and source-native terms. |
| `commodity_vocabulary_ref` | Vocabulary, code list, source classification, or commodity scheme ref. |
| `source_commodity_labels` | Source-native labels retained for audit. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, aggregate, administrative, modeled, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native occurrence, report, database, sample, map, literature, or inventory record. |
| `location_ref_internal` | Access-controlled exact/source geometry ref. |
| `public_geometry_ref` | Generalized or aggregate public-safe geometry ref, if released. |
| `public_safe_geometry_fingerprint` | Stable fingerprint of released/generalized/aggregate geometry. |
| `geometry_precision` | Exact, source precision, generalized, aggregate, withheld, unknown. |
| `coordinate_uncertainty` | Source/native/georeferenced uncertainty. |
| `evidence_summary` | Public-safe summary of evidence basis. |
| `geochemistry_sample_refs` | Linked GeochemistrySample evidence. |
| `geophysical_observation_refs` | Linked GeophysicalObservation evidence. |
| `lithology_refs` | Linked Lithology/material-character evidence. |
| `geologic_unit_refs` | Linked GeologicUnit or SurficialUnit context. |
| `resource_deposit_refs` | Linked ResourceDeposit refs only where evidence supports relationship; not identity equality. |
| `resource_estimate_refs` | Linked ResourceEstimate refs only where evidence supports relationship; not identity equality. |
| `extraction_site_refs` | Linked ExtractionSite refs only where evidence supports relationship; not extraction proof. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Field observation, sample collection, or original report observation time where material; often unknown for legacy compilations. |
| `valid_time` | Time interval the occurrence claim is considered valid, where applicable. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Aggregate-public, generalized-public, restricted-detail, resource-sensitive, rights-limited, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release where material. |
| `review_record_ref` | Source, geology, natural-resources, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when occurrence detail/geometry is generalized or withheld. |
| `aggregation_receipt_ref` | Required when occurrences become aggregate public products. |
| `validation_report_ref` | Validation report for schema, source role, geometry, commodity vocabulary, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, commodity correction, geometry correction, sensitivity update, identity merge/split, and rollback lineage. |
| `quality_flags` | Source-role conflict, identity collision, commodity conflict, geometry uncertainty, rights unknown, sensitivity unknown, occurrence/deposit collapse, estimate collapse, stale source, or incomplete evidence. |

---

## Occurrence classes

| Class | Meaning | Default posture |
|---|---|---|
| `field_reported_occurrence` | Occurrence reported from field observation or survey. | Observed when source/evidence resolve; detail may restrict. |
| `sample_supported_occurrence` | Occurrence supported by geochemistry/core/sample evidence. | Evidence-bound; sample does not become occurrence by itself. |
| `geophysical_context_occurrence` | Occurrence supported or suggested by geophysical context. | Usually interpreted; source role and uncertainty required. |
| `compiled_occurrence` | Occurrence from compiled database or literature rollup. | Aggregate/compiled; preserve source caveats. |
| `historical_occurrence` | Legacy or historical occurrence with old/uncertain geometry. | Source time and uncertainty are material. |
| `aggregate_public_summary` | Aggregate geography/count/commodity summary. | Public-safe only with release support. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical occurrence. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released generalized or aggregate representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | MineralOccurrence posture |
|---|---|---|
| Field report, mapped occurrence, observed mineralization | `observed` | Supports reported presence when source/evidence resolve. |
| Compiled mineral database, regional inventory, literature rollup | `aggregate` | Compiled support; preserve source, geometry, and completeness caveats. |
| Administrative inventory or agency record | `administrative` | Identifies record/status context; not necessarily observed mineralization by itself. |
| Modeled prospectivity or inferred anomaly | `modeled` | Interpretation/model output; not observed occurrence unless independently supported. |
| Regulatory or permit context | `regulatory` | Context only; not occurrence proof without occurrence evidence. |
| Unreviewed import, fuzzy match, unresolved commodity, geometry conflict | `candidate` | Quarantine until identity, source role, commodity, rights, and geometry resolve. |
| AI-generated or hypothetical occurrence | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`MineralOccurrence` is one of the load-bearing Natural Resources anti-collapse objects.

```text
MineralOccurrence != ResourceDeposit
MineralOccurrence != ResourceEstimate
MineralOccurrence != ReserveClaim
MineralOccurrence != ExtractionSite
MineralOccurrence != ProductionRecord
MineralOccurrence != PermitRecord
MineralOccurrence != ownership / lease / title proof
MineralOccurrence != Hazards risk
MineralOccurrence != AI summary
```

Any join to a deposit, estimate, extraction site, permit, production record, reclamation record, or ownership/title context must be explicit, evidence-bound, source-role-aware, time-aware, policy-reviewed where material, and non-identifying unless a future ADR/schema explicitly defines a relationship type.

Joining occurrence/deposit/estimate as identity equality is a validation `DENY` and an AI/public-surface `ABSTAIN`.

---

## Sensitivity and release

Mineral occurrences can expose resource-sensitive, land/title-adjacent, extraction-adjacent, culturally sensitive, proprietary, or operationally sensitive information. The safe default is to publish only aggregate or generalized public-safe derivatives unless evidence, rights, sensitivity review, and release support allow more detail.

Rules:

- Exact/detail occurrence geometry is not automatically public.
- Public derivatives should use aggregate regions, generalized points/polygons, public-safe commodity classes, or suppression where needed.
- Public outputs must preserve source role, source time, observed time where material, geometry precision, commodity caveats, rights posture, and anti-collapse caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, stale, or evidence-incomplete records must not enter public outputs as authoritative occurrence facts.
- Occurrence detail must not be used to imply economic viability, reserve quantity, deposit identity, extraction, ownership, permit authority, or hazards risk.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision where material, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native occurrence rows, reports, coordinates, commodity labels, maps, database IDs, and source notes remain source-bound. |
| WORK / QUARANTINE | Candidate occurrences are normalized, source-role checked, commodity-mapped, identity-crosswalked, rights/sensitivity-screened, geometry-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, source support, commodity support, geometry posture, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, evidence, geometry precision, commodity vocabulary, access state, and anti-collapse caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision/review where material, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released aggregate or generalized public-safe occurrence derivatives appear in public clients. |
| CORRECTION | Source update, occurrence identity merge/split, commodity correction, geometry correction, sensitivity change, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve casing/path drift between `MineralOccurrence.md`, lower-case schema file, and lower-case schema `contract_doc` pointer.
- [ ] Expand `mineral_occurrence.schema.json` from scaffold into field-level validation, or record the accepted schema path via ADR/schema PR.
- [ ] Add valid fixtures for field-reported occurrence, sample-supported occurrence, compiled occurrence, historical occurrence, aggregate public summary, candidate import, synthetic example, and public generalized derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, missing commodity set, identity collision, occurrence treated as deposit, occurrence treated as estimate/reserve, occurrence treated as extraction/permit/ownership/title proof, exact sensitive public geometry, missing policy decision where material, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, occurrence ID, commodity set, source ID, public-safe geometry fingerprint, source role, temporal support, evidence refs, sensitivity state, policy refs, release refs, correction refs, and anti-collapse constraints.
- [ ] Add policy/access tests proving public clients consume released aggregate/generalized derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, commodity remap, identity merge/split, geometry correction, sensitivity update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, source role is clear, geometry is public-safe or released, derivative is released | `ANSWER` / public-safe occurrence derivative may be shown |
| Evidence, rights, source role, commodity, identity, geometry, or sensitivity support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, release is absent, or occurrence is collapsed into deposit/estimate/title/risk | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Confirmed schema scaffold | Confirms lower-case schema file exists, is PROPOSED, and currently has empty properties. | Does not prove field validation; also exposes casing/path drift. |
| Geology scope doc | Confirms Geology owns Mineral Occurrence and defines it as documented presence, not deposit/estimate. | Does not prove schema or implementation enforcement. |
| Geology object-family doc | Confirms purpose, proposed key fields, material times, sensitivity posture, source roles, and anti-collapse invariant. | Field realization remains PROPOSED. |
| Natural Resources sublane doc | Confirms resource-focused scope, restricted sensitivity posture, and exact-location/role anti-collapse discipline. | Sublane placement remains PROPOSED in that doc. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized MineralOccurrence weakens source integrity, misstates source role, exposes restricted detail, or collapses occurrence into deposit, estimate, extraction, permit, production, title, ownership, or risk truth.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source occurrence record corrected, withdrawn, merged, or split;
- commodity vocabulary, commodity set, or source label corrected;
- occurrence geometry or public-safe derivative corrected;
- occurrence was presented as economic, measured, owned, mined, permitted, estimated, producing, reserved, or hazardous;
- public derivative exposes restricted detail or lacks redaction/aggregation receipt where needed;
- release manifest lacks policy decision where material, correction path, or rollback target;
- public API/UI/AI reads RAW/WORK/QUARANTINE or candidate records as public truth.

Rollback artifacts should include affected MineralOccurrence IDs, source record IDs, commodity refs, geometry refs, public derivative refs, linked deposit/estimate/extraction/context refs, release IDs, evidence refs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should the contract file be PascalCase `MineralOccurrence.md` or lower-case `mineral_occurrence.md` to match the schema scaffold pointer? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted schema path and casing for `MineralOccurrence`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which commodity vocabulary is canonical for KFM occurrence records? | NEEDS VERIFICATION | Source registry, schema, and natural-resources steward review. |
| Which occurrence-detail geometries are public-safe by source family and commodity? | NEEDS VERIFICATION | Policy, sensitivity, and release fixture review. |
| What relationship predicates connect occurrence to deposit, estimate, extraction site, and reclamation without identity collapse? | NEEDS VERIFICATION | Natural-resources ADR and anti-collapse tests. |
| How should AI/MapLibre surfaces phrase occurrence evidence without implying economic value? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/GeochemistrySample.md` — sample/analyte evidence that may support occurrence review.
- `contracts/domains/geology/GeophysicalObservation.md` — geophysical evidence or anomaly context.
- `contracts/domains/geology/ResourceDeposit.md` — distinct deposit body, not occurrence identity.
- `contracts/domains/geology/ExtractionSite.md` — extraction site context, not occurrence proof.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference and anti-collapse invariant.
- `docs/domains/geology/sublanes/natural_resources.md` — Natural Resources sublane doctrine.
- `schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve PascalCase vs lower-case contract/schema path drift.
- [ ] Expand paired schema and fixtures.
- [ ] Add anti-collapse tests for occurrence/deposit/estimate/extraction/permit/production/title/risk distinctions.
- [ ] Add commodity vocabulary and source-role validation fixtures.
- [ ] Add policy tests for restricted/detail vs aggregate/generalized public derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released aggregate/generalized occurrence derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved casing/path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
