<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-reclamation-record
title: ReclamationRecord Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Natural-resources steward
  - OWNER_TBD — Reclamation steward
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
policy_label: public-with-gates; semantic-contract; geology; reclamation-record; natural-resources; regulatory-context; source-role-aware; release-gated; correction-ready
tags: [kfm, contracts, geology, ReclamationRecord, reclamation-record, natural-resources, extraction-site, status, plan, observation, program-authority, regulatory-context, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./ExtractionSite.md
  - ./MineralOccurrence.md
  - ./ResourceDeposit.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/reclamation_record.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology ReclamationRecord semantic contract."
  - "A lower-case schema scaffold exists at schemas/contracts/v1/domains/geology/reclamation_record.schema.json, while this requested contract path uses PascalCase. The schema's x-kfm.contract_doc points to contracts/domains/geology/reclamation_record.md, creating a casing/path drift that remains CONFLICTED / NEEDS VERIFICATION."
  - "ReclamationRecord means reclamation status, plan, program authority, and observations. It does not prove extraction-site identity, ownership/title, lease, permit authority, hazards risk, public safety, or environmental compliance by itself."
  - "Public use requires evidence, source role, rights, sensitivity review where material, validation, release, correction path, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ReclamationRecord — Geology

> Semantic contract for Geology `ReclamationRecord`: the evidence-bound object for reclamation status, plan, program authority, observations, source role, public-safe posture, correction, and rollback — explicitly distinct from extraction-site identity, permits, ownership/title, hazards risk, and public release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: ReclamationRecord" src="https://img.shields.io/badge/object-ReclamationRecord-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: reclamation not title or risk" src="https://img.shields.io/badge/boundary-reclamation__not__title__or__risk-critical">
</p>

`contracts/domains/geology/ReclamationRecord.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Record classes](#record-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/ReclamationRecord.md`  
> **Schema posture:** a lower-case scaffold exists at `schemas/contracts/v1/domains/geology/reclamation_record.schema.json`; its `x-kfm.contract_doc` points to lower-case `contracts/domains/geology/reclamation_record.md`, while the current requested contract path is PascalCase  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Reclamation Record` as an owned object family for reclamation status, plan, and observations. Field-level schema shape, casing, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `ReclamationRecord` is a reclamation status / plan / observation reference. It does **not** prove `ExtractionSite` identity, ownership/title, lease, permit authority, operator authority, environmental compliance, hazards risk, public safety, production, reserve status, or AI/UI truth by itself.

---

## Meaning

`ReclamationRecord` is the Geology semantic object for a source-supported reclamation record connected to resource extraction, disturbed land, mining/quarrying/oil-gas context, closure, remediation, restoration, inspection, or post-extraction land-use status.

It answers:

- Which reclamation status, plan, program authority, observation, inspection, or source record is being referenced?
- Which extraction site, source record, program, authority, status code, temporal scope, evidence, geometry posture, and rights/sensitivity state apply?
- Which extraction-site, resource, permit/regulatory, land/title, hazards, or restoration records may be linked as context without collapsing identity?
- What public-safe status, geometry, summary, or derivative may be shown?
- Which policy decision, review record, redaction/aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

A reclamation record can describe reclamation context. It is not automatically proof of legal compliance, title, permit validity, operator responsibility, public safety, environmental condition, hazards risk, or site identity.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Reclamation meaning | `contracts/domains/geology/ReclamationRecord.md` | Owned here by request; casing drift remains open |
| Machine schema shape | `schemas/contracts/v1/domains/geology/reclamation_record.schema.json` | CONFIRMED scaffold; field shape still empty / PROPOSED |
| Schema/contract casing drift | `ReclamationRecord.md` vs `reclamation_record.schema.json` and lower-case `x-kfm.contract_doc` | CONFLICTED / NEEDS VERIFICATION |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms Reclamation Record is owned for status, plan, and observations |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed keys, material times, sensitivity posture, and source roles |
| Natural-resources doctrine | `docs/domains/geology/sublanes/natural_resources.md` | Confirms reclamation context belongs in the resource-focused Geology sublane |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, aggregate, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

A paired schema exists only as a lower-case scaffold and does not yet enforce fields.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/ReclamationRecord.md` |
| Confirmed schema path | `schemas/contracts/v1/domains/geology/reclamation_record.schema.json` |
| Schema status | `PROPOSED` scaffold with empty `properties` and `additionalProperties: true` |
| Schema title | `Reclamation Record` |
| Schema contract pointer | `contracts/domains/geology/reclamation_record.md` |
| Casing/path posture | CONFLICTED / NEEDS VERIFICATION; requested PascalCase contract exists, schema points lower-case contract path |
| Field-level enforcement | NEEDS VERIFICATION |

Until the casing and schema-field decision is resolved, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `ReclamationRecord` should semantically assert:

1. **Record identity** — deterministic identity for the reclamation record, source, program authority, status code, temporal scope, and normalized digest.
2. **Reclamation status/plan/observation** — source-supported status, plan, inspection, observation, milestone, closure, or program record.
3. **Source identity** — SourceDescriptor, source record ID, source role, source time, valid time, correction time, rights, cadence, and attribution.
4. **Program authority context** — administering program, agency, regulatory context, or source-native authority label, without converting it into title/permit proof.
5. **Linked site context** — extraction site, disturbed area, lease/permit context, operation context, or public-safe geometry where supported, without identity equality.
6. **Temporal discipline** — source time, valid time, retrieval time, release time, and correction time remain distinct; observed/inspection time is retained where material.
7. **Evidence linkage** — program record, inspection report, plan document, status database, map, photo, source table, EvidenceRef, or EvidenceBundle.
8. **Sensitivity posture** — public-safe, generalized, rights-limited, active-sensitive, site-sensitive, restricted, withheld, or unknown state.
9. **Anti-collapse posture** — explicit separation from ExtractionSite, permit, ownership/title, operator authority, hazards risk, and legal/environmental compliance claims.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating reclamation record as extraction-site identity | ExtractionSite owns physical site context. Reclamation can link to it, not replace it. |
| Treating status as legal compliance proof | Reclamation status may be administrative/regulatory context, not a legal conclusion unless the source explicitly supports it and owning policy allows use. |
| Treating program authority as title or permit authority | Ownership/title/lease/permit claims remain outside Geology canonical truth. |
| Treating reclamation record as hazards risk | Hazards owns risk. Geology may supply reclamation context only. |
| Treating reclamation plan as completed reclamation | Plans, milestones, inspections, and completion status are distinct source-role/time-bound claims. |
| Treating operator name as responsibility proof | Operator context requires source role and time; it is not title or liability proof. |
| Treating public generalized geometry as exact site footprint | Public-safe geometry is a derivative with caveats. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM reclamation-record identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `ReclamationRecord` or accepted canonical spelling after casing/path reconciliation. |
| `record_class` | Status record, plan record, inspection observation, milestone, closure record, candidate, aggregate, or public derivative. |
| `site_ref` | Linked ExtractionSite or source-native site ref where supported; not identity equality. |
| `program_authority` | Agency/program/source-native authority label or ref. |
| `reclamation_status_code` | Normalized or source-native status/milestone code. |
| `source_status_label` | Source-native reclamation status text retained for audit. |
| `plan_ref` | Reclamation plan, program plan, closure plan, or source-native plan document ref. |
| `observation_refs` | Inspection/observation/photo/report refs, where available. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Administrative, regulatory, observed, aggregate, modeled, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native status, plan, inspection, program, site, table, or report record. |
| `location_ref_internal` | Access-controlled exact/source geometry ref. |
| `public_geometry_ref` | Generalized or aggregate public-safe geometry ref, if released. |
| `public_safe_geometry_fingerprint` | Stable fingerprint of released/generalized/aggregate geometry. |
| `geometry_precision` | Exact, source precision, generalized, aggregate, withheld, unknown. |
| `activity_state` | Planned, active, under reclamation, completed, monitored, closed, abandoned, unknown, or source-native status. |
| `status_effective_time` | Time the reclamation status became effective, where supported. |
| `inspection_time` | Observation/inspection time, where material. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the status/plan/observation claim is valid for. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `extraction_site_refs` | Linked ExtractionSite refs. |
| `mineral_occurrence_refs` | Linked occurrence refs only where evidence supports relationship; not identity equality. |
| `resource_deposit_refs` | Linked deposit refs only where evidence supports relationship; not status proof. |
| `permit_context_refs` | Permit/regulatory context refs, not title or legal proof by themselves. |
| `operator_context_refs` | Operator/source context refs with time and role caveats. |
| `land_context_refs` | Land/parcel/ownership/title context refs only as non-authoritative context unless owning lane confirms. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Public-safe, generalized-public, aggregate-public, rights-limited, active-sensitive, restricted, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release where material. |
| `review_record_ref` | Source, geology, natural-resources, reclamation, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when record detail/geometry is generalized or withheld. |
| `aggregation_receipt_ref` | Required when records become aggregate public products. |
| `validation_report_ref` | Validation report for schema, source role, status code, geometry, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, status correction, geometry correction, sensitivity update, identity merge/split, and rollback lineage. |
| `quality_flags` | Source-role conflict, status ambiguity, plan/status collapse, site identity ambiguity, rights unknown, sensitivity unknown, stale source, or incomplete evidence. |

---

## Record classes

| Class | Meaning | Default posture |
|---|---|---|
| `status_record` | Administrative/regulatory status record for reclamation state. | Administrative/regulatory; not compliance proof by itself. |
| `plan_record` | Reclamation, closure, remediation, or post-extraction plan. | Planned intent; not completed reclamation. |
| `inspection_observation` | Inspection, observation, report, or source-supported field status. | Observed or regulatory depending on source. |
| `milestone_record` | Milestone such as started, seeded, monitored, released, closed, or source-native equivalent. | Time-bound; valid/source/correction times material. |
| `closure_record` | Closure/completion/release-from-program context. | Requires source-role caveat; not title/public safety proof. |
| `aggregate_public_summary` | Aggregate status counts or county/region summary. | Public-safe only with release support. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical reclamation note. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released generalized or aggregate representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | ReclamationRecord posture |
|---|---|---|
| Agency reclamation database or program record | `administrative` or `regulatory` | Status/program context; not automatically legal conclusion. |
| Inspection report, field observation, photo-supported review | `observed` or `regulatory` | Evidence-bearing observation if source and time resolve. |
| Regional summary, annual report, aggregate rollup | `aggregate` | Aggregate status only; preserve source scale and caveats. |
| Modeled restoration/recovery condition | `modeled` | Model output; not observed reclamation status. |
| Permit/lease/operator record | `regulatory` or `administrative` | Context only; not reclamation proof without reclamation evidence. |
| Unreviewed import, stale status, fuzzy site link, unresolved program code | `candidate` | Quarantine until identity, source, status, rights, and site refs resolve. |
| AI-generated or hypothetical reclamation note | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`ReclamationRecord` is status/plan/observation context, not the upstream site or downstream legal/risk conclusion.

```text
ReclamationRecord != ExtractionSite
ReclamationRecord != PermitRecord
ReclamationRecord != ProductionRecord
ReclamationRecord != ReserveClaim
ReclamationRecord != ownership / lease / title proof
ReclamationRecord != operator liability proof
ReclamationRecord != environmental compliance proof by default
ReclamationRecord != Hazards risk
ReclamationRecord != public safety statement
ReclamationRecord != AI summary
```

Any join to extraction sites, permits, leases, operators, land/title context, hazards, restoration, or public UI must preserve object identity, source role, time, evidence, rights, sensitivity, release state, and correction lineage.

---

## Sensitivity and release

Reclamation records are often public-safe as administrative status summaries when source rights allow, but exact active-site detail, operator-sensitive context, private land/title context, unresolved status, and stale program records can require review, generalization, or denial.

Rules:

- A reclamation record is not automatically a released public layer or compliance statement.
- Public derivatives require validation, source rights, policy/review where material, release manifest, correction path, and rollback target.
- Public outputs must preserve source role, source time, valid time, correction time, status code, geometry precision, and caveats.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, stale, site-ambiguous, or evidence-incomplete records must not enter public outputs as authoritative reclamation facts.
- Reclamation status must not be used to imply public safety, hazards risk, title, permit validity, operator liability, environmental compliance, or completed restoration unless the owning source and policy explicitly support that narrow claim.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision where material, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native reclamation status rows, plans, inspections, coordinates, program codes, reports, photos, maps, and source notes remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, source-role checked, status-code mapped, site-linked, rights/sensitivity-screened, geometry-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, source support, status/plan/observation support, geometry posture, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, evidence, geometry precision, program authority, status caveats, and anti-collapse caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision/review where material, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released aggregate, generalized, or public-safe reclamation derivatives appear in public clients. |
| CORRECTION | Source update, status correction, plan update, site-link correction, geometry correction, sensitivity change, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve casing/path drift between `ReclamationRecord.md`, lower-case schema file, and lower-case schema `contract_doc` pointer.
- [ ] Expand `reclamation_record.schema.json` from scaffold into field-level validation, or record the accepted schema path via ADR/schema PR.
- [ ] Add valid fixtures for status record, plan record, inspection observation, milestone record, closure record, aggregate public summary, candidate import, synthetic example, and public generalized derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, missing site ref, missing program authority, status/plan collapse, reclamation treated as extraction-site identity, reclamation treated as title/permit/compliance/hazards proof, exact sensitive public geometry, missing policy decision where material, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, site ref, program authority, reclamation status code, source role, temporal support, evidence refs, sensitivity state, policy refs, release refs, correction refs, and anti-collapse constraints.
- [ ] Add policy/access tests proving public clients consume released aggregate/generalized derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, status-code remap, site-link correction, identity merge/split, geometry correction, sensitivity update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, source role is clear, status context is bounded, derivative is released | `ANSWER` / public-safe reclamation derivative may be shown |
| Evidence, rights, source role, status, site identity, geometry, or sensitivity support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, release is absent, or reclamation is collapsed into title/permit/compliance/risk | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Confirmed schema scaffold | Confirms lower-case schema file exists, is PROPOSED, and currently has empty properties. | Does not prove field validation; also exposes casing/path drift. |
| Geology scope doc | Confirms Geology owns Reclamation Record for status, plan, and observations. | Does not prove schema or implementation enforcement. |
| Geology object-family doc | Confirms purpose, proposed key fields, material times, sensitivity posture, source roles, and §B-only / §E drift. | Field realization remains PROPOSED. |
| Natural Resources sublane doc | Confirms reclamation context belongs in the resource-focused Geology sublane and inherits deny-by-default/resource anti-collapse governance. | Sublane placement remains PROPOSED in that doc. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized ReclamationRecord weakens source integrity, misstates source role, exposes restricted detail, or collapses reclamation status into extraction-site identity, permit/title authority, compliance proof, hazards risk, or public safety truth.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source reclamation record corrected, withdrawn, merged, or split;
- status code, program authority, plan, milestone, or inspection observation corrected;
- source-time, valid-time, or correction-time semantics were collapsed;
- reclamation was presented as title, lease, permit, legal compliance, environmental compliance, hazards risk, public safety, or operator liability proof;
- public derivative exposes restricted detail or lacks redaction/aggregation receipt where needed;
- release manifest lacks policy decision where material, correction path, or rollback target;
- public API/UI/AI reads RAW/WORK/QUARANTINE or candidate records as public truth.

Rollback artifacts should include affected ReclamationRecord IDs, source record IDs, site refs, program authority refs, status refs, geometry refs, linked extraction/permit/operator/land/hazards context refs, public derivative refs, release IDs, evidence refs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should the contract file be PascalCase `ReclamationRecord.md` or lower-case `reclamation_record.md` to match the schema scaffold pointer? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted schema path and casing for `ReclamationRecord`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which reclamation status-code vocabulary is canonical for KFM? | NEEDS VERIFICATION | Source registry, schema, and natural-resources steward review. |
| Which public reclamation statuses are safe to show at site/detail scale? | NEEDS VERIFICATION | Policy, sensitivity, and release fixture review. |
| What relationship predicates connect reclamation to extraction site, permit context, operator context, and land context without identity collapse? | NEEDS VERIFICATION | Natural-resources ADR and anti-collapse tests. |
| How should AI/MapLibre surfaces phrase reclamation status without implying legal compliance or public safety? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/ExtractionSite.md` — physical extraction-site context, not reclamation status proof.
- `contracts/domains/geology/MineralOccurrence.md` — reported mineral presence, not reclamation status.
- `contracts/domains/geology/ResourceDeposit.md` — resource-deposit body, if/when verified.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference and operational-object semantics.
- `docs/domains/geology/sublanes/natural_resources.md` — Natural Resources sublane doctrine.
- `schemas/contracts/v1/domains/geology/reclamation_record.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve PascalCase vs lower-case contract/schema path drift.
- [ ] Expand paired schema and fixtures.
- [ ] Add anti-collapse tests for reclamation/extraction-site/permit/operator/title/compliance/hazards/public-safety distinctions.
- [ ] Add status-code vocabulary and source-role validation fixtures.
- [ ] Add policy tests for restricted/detail vs aggregate/generalized public derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released aggregate/generalized reclamation derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved casing/path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
