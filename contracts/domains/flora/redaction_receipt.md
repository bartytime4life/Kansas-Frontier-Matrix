<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-redaction-receipt
title: Redaction Receipt Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Redaction steward · Sensitivity reviewer · Privacy steward · Contract steward · Source steward · Schema steward · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: restricted; semantic-contract; flora; redaction-receipt; geoprivacy; transform-proof; sensitivity-aware; release-gated; audit-required; rollback-critical
tags: [kfm, contracts, flora, redaction-receipt, geoprivacy, generalization, suppression, withholding, transform-proof, sensitivity, evidence, policy, release, correction, rollback]
related:
  - ./README.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./specimen_record.md
  - ./flora_occurrence.md
  - ./occurrence_public.md
  - ./occurrence_restricted.md
  - ./rare_plant_record.md
  - ./phenology_observation.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./domain_validation_report.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/redaction_receipt.schema.json
  - ../../../fixtures/domains/flora/redaction_receipt/
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold into a Flora redaction/transform receipt semantic contract."
  - "The paired schema is a PROPOSED scaffold with no declared fields and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "RedactionReceipt records how, why, when, and under which policy/review decision a Flora record or geometry was generalized, suppressed, delayed, withheld, binned, masked, or otherwise transformed."
  - "A receipt proves a transform event; it does not itself authorize publication, override policy, replace EvidenceBundle, or make the transformed output canonical truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Redaction Receipt — Flora

> Semantic contract for Flora `RedactionReceipt`: the auditable proof object for privacy, sensitivity, and geoprivacy transforms applied to Flora records before public or semi-public use.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: receipt not release approval" src="https://img.shields.io/badge/boundary-receipt__not__release__approval-critical">
</p>

`contracts/domains/flora/redaction_receipt.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Transform classes](#transform-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/redaction_receipt.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/redaction_receipt.schema.json`  
> **Truth posture:** the target contract path exists as a scaffold, the paired schema path exists as a PROPOSED scaffold, and the Flora canonical path register identifies `RedactionReceipt` as the transform receipt for any redaction or generalization. Field-level schema shape, fixtures, validators, policy runtime, source registry terms, release workflow, API behavior, UI behavior, receipt integrity checks, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `RedactionReceipt` documents a protective transform. It does **not** authorize publication by itself, does **not** replace a `PolicyDecision`, `ReviewRecord`, `DomainValidationReport`, `ReleaseManifest`, `CorrectionNotice`, or rollback target, and does **not** make a public derivative canonical exact truth.

---

## Meaning

`RedactionReceipt` is the Flora semantic object that records a protective transformation applied to sensitive or policy-significant Flora data. It captures what was transformed, why it was transformed, what method was used, what policy/review basis allowed or required the transform, what public-safe result was created, and what rollback/correction path remains available.

It answers:

- Which source object, record, field, geometry, time, label, evidence projection, or layer was transformed?
- Was the transform redaction, generalization, aggregation, grid/binning, masking, suppression, withholding, delay, clipping, simplification, precision reduction, label filtering, or citation projection?
- Which sensitivity, rights, source-role, policy, review, or release reason required the transform?
- What exact internal support remains restricted, and what public-safe derivative was produced?
- Which integrity hash, transform version, validation report, policy decision, release manifest, correction notice, and rollback target make the transform auditable?
- Which public clients may consume the result, and what caveats must follow the released derivative?

A redaction receipt is evidence of a governed transform. It is not the transform policy itself and not a release decision.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Redaction receipt meaning | `contracts/domains/flora/redaction_receipt.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/redaction_receipt.schema.json` | Linked only; currently scaffolded |
| Restricted source records | `rare_plant_record.md`, `occurrence_restricted.md`, `specimen_record.md`, `botanical_survey.md` | Common upstream sensitive inputs |
| Public derivatives | `occurrence_public.md`, `range_polygon.md`, public-safe summaries/layers | Common downstream outputs |
| Taxon/status context | `plant_taxon.md`, `flora_taxon_crosswalk.md`, `invasive_plant_record.md` | Labels/statuses that may require caveats or suppression |
| Timing/context surfaces | `phenology_observation.md`, `habitat_association.md`, `vegetation_community.md` | Context that can amplify sensitive inference |
| Validation report | `domain_validation_report.md` | Validates transform, fixtures, policy, and release readiness |
| Policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/` | Owns allow/deny/abstain rules; receipt records result/application |
| Source registry | `data/registry/sources/flora/` | Source rights, redistribution, attribution, and access limits |
| Release artifacts | `release/candidates/`, `release/manifests/` | Publication decision and rollback target live here, not in this receipt alone |
| Published layers | `data/published/layers/flora/` | Consume released public-safe derivatives only |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/redaction_receipt.schema.json` |
| Schema title | `Redaction Receipt` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Source document | `docs/domains/flora/CANONICAL_PATHS.md` |
| Contract document | `contracts/domains/flora/redaction_receipt.md` |

Because the schema is empty and permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validators, integrity checks, policy checks, transform logs, public derivative links, release manifests, correction flows, and rollback handling. It does not claim current machine enforcement.

---

## Assertions

A reviewed `RedactionReceipt` should semantically assert:

1. **Receipt identity** — deterministic identity for the transform receipt.
2. **Input identity** — internal source object, record, field, geometry, layer, or evidence projection transformed.
3. **Output identity** — public-safe derivative, withheld result, suppressed geometry, aggregated summary, delayed release, or label-only output produced.
4. **Transform class** — generalization, aggregation, suppression, withholding, delay, masking, binning, precision reduction, clipping, simplification, citation projection, or other governed method.
5. **Reason and policy basis** — sensitivity, rights, source-role, review, source-term, public-risk, or publication requirement that required the transform.
6. **Method details** — transform version, parameters, thresholds, cell size, precision level, delay interval, clipping boundary, suppression reason, and safe-output caveats.
7. **Evidence support** — internal and public-safe EvidenceRef/EvidenceBundle projections sufficient for cite-or-abstain behavior without leaking restricted content.
8. **Integrity support** — input hash, output hash, transform hash, spec hash, code/version ref, reviewer signature/ref, or audit trail where applicable.
9. **Governance state** — validation, policy, review, release, correction, supersession, and rollback references.
10. **Reversibility posture** — which exact source remains protected, which public output can be withdrawn/rebuilt, and what rollback path exists.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a receipt as publication approval | Release still requires validation, policy, review, release manifest, and rollback target. |
| Treating redacted output as canonical exact truth | Public-safe derivatives are carriers, not internal exact records. |
| Omitting the reason for a transform | A transform without reason is not auditable. |
| Hiding a denial as an empty result | Withholding/suppression should produce visible reason metadata where safe. |
| Publishing exact sensitive input alongside the receipt | The receipt must not leak the protected value it documents. |
| Generalizing without parameters or version | Reproducibility and rollback require transform details. |
| Using redaction to launder weak evidence | Source role, evidence, uncertainty, and caveats must survive transformation. |
| Allowing public clients to infer restricted details from receipt metadata | Receipt public projection must itself be redacted when needed. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical redaction receipt identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic receipt content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `receipt_class` | `geometry_generalization`, `geometry_suppression`, `geometry_aggregation`, `grid_binning`, `precision_reduction`, `temporal_delay`, `label_filter`, `evidence_projection`, `field_redaction`, `withholding`, `public_derivative`, or `rollback_redaction`. |
| `input_object_type` | Source object class, such as RarePlantRecord, OccurrenceRestricted, SpecimenRecord, RangePolygon, PhenologyObservation, or HabitatAssociation. |
| `input_object_ref` | Access-controlled ref to the internal source object. |
| `input_field_refs` | Fields transformed, if field-level redaction applies. |
| `input_geometry_ref` | Exact/restricted geometry ref, if applicable. |
| `input_evidence_refs` | Internal evidence refs protected by access rules. |
| `output_object_type` | Output derivative class, such as OccurrencePublic, public RangePolygon, summary, layer feature, withheld result, or suppressed geometry. |
| `output_object_ref` | Public-safe derivative or withheld/suppressed result ref. |
| `output_geometry_ref` | Public-safe geometry ref, if produced. |
| `public_evidence_projection_ref` | Public-safe evidence/citation projection, if produced. |
| `transform_method` | Generalization, aggregation, binning, masking, clipping, delay, suppression, withholding, label filtering, or citation projection method. |
| `transform_parameters` | Cell size, county/grid/region, precision, delay interval, clipping boundary, suppression threshold, or other parameter summary. |
| `transform_version` | Version of transform rule, script, policy, or process. |
| `transform_time` | Time the transform was applied. |
| `actor_ref` | Service, steward, reviewer, or process that applied the transform. |
| `reason_codes` | Rare-plant, private-land, cultural, source-restricted, rights-limited, precision-risk, habitat-inference, stale-risk, public-safe-projection, or policy-blocked reasons. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, and authority limits that influenced the transform. |
| `source_role` | Source role preserved through the transform. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state_before` | Sensitivity/access state before transform. |
| `sensitivity_state_after` | Sensitivity/public-safe state after transform. |
| `policy_decision_ref` | Policy decision requiring or allowing transform. |
| `review_record_ref` | Source/steward/sensitivity/release review supporting transform. |
| `validation_report_ref` | Validation report for transform correctness and release readiness. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage, if the derivative is released. |
| `input_hash` | Integrity hash of protected input or canonical input envelope. |
| `output_hash` | Integrity hash of derivative output. |
| `transform_hash` | Integrity hash of transform spec/code/config, where available. |
| `public_caveats` | Public-safe caveats that must accompany output. |
| `withholding_explanation_public` | Public-safe explanation when output is suppressed or withheld. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, stale-state, transform bug, and rollback lineage. |
| `rollback_ref` | RollbackCard or rollback target. |
| `quality_flags` | Missing-policy, missing-review, missing-output, parameter-unknown, sensitivity-unknown, rights-unknown, transform-not-reproducible, or leak-risk flags. |

---

## Transform classes

| Class | Meaning | Default posture |
|---|---|---|
| `geometry_generalization` | Exact geometry moved/rounded/coarsened to safer support. | Requires method, scale, reason, and receipt. |
| `geometry_suppression` | Geometry removed from public output. | Requires safe withholding explanation where possible. |
| `geometry_aggregation` | Records summarized by county/grid/range/region. | Must preserve support scale and count/caveat rules. |
| `grid_binning` | Points/features binned into grid or hex cells. | Requires cell size, threshold, and inference-risk review. |
| `precision_reduction` | Coordinate/date/label precision reduced. | Must record before/after precision and reason. |
| `temporal_delay` | Release delayed to reduce exposure risk. | Requires delay interval and release-time caveat. |
| `label_filter` | Sensitive label/source context removed or generalized. | Must preserve enough caveat for honest public interpretation. |
| `evidence_projection` | Internal EvidenceBundle projected to public-safe citation/evidence. | Must not leak restricted rows, notes, or exact geometry. |
| `field_redaction` | Specific fields removed, masked, or replaced. | Requires field refs and reason codes. |
| `withholding` | No public derivative emitted. | Record reason; avoid silent empty results where safe. |
| `public_derivative` | Receipt for a released public-safe object. | Requires validation, release linkage, and rollback target. |
| `rollback_redaction` | Transform applied during rollback/suppression. | Requires correction/rollback refs. |

---

## Source-role rules

| Source pattern | Canonical `source_role` | Receipt posture |
|---|---|---|
| Observed exact occurrence, specimen locality, survey route, steward note | `observed` | Receipt must preserve observation support while protecting exact detail. |
| Rare/protected list, policy boundary, restriction rule | `regulatory` | Receipt can document status-driven restriction; not occurrence proof. |
| Model output or risk surface | `modeled` | Receipt must keep model identity/version/uncertainty caveats. |
| Atlas/grid/county/literature summary | `aggregate` | Receipt must not imply exact occurrence after transformation. |
| Program/site/project management record | `administrative` | Receipt protects administrative or private context without upgrading biological truth. |
| Unreviewed import or unresolved candidate | `candidate` | Usually no public derivative; receipt may record quarantine/suppression. |
| AI-generated or reconstructed sensitive material | `synthetic` | Receipt must preserve reality-boundary disclosure; never observed fact. |

Redaction can reduce exposure. It cannot upgrade source authority.

---

## Sensitivity and release

Flora redaction receipts exist because sensitive plant information should be useful without being reckless. They make protective choices visible and auditable.

Rules:

- Exact rare/protected/culturally sensitive locations remain withheld from public surfaces by default.
- The safest accurate representation wins: generalized region, grid cell, range, aggregate, delayed release, label-only, or withholding where needed.
- Source quality is not a license to expose sensitive detail.
- Every protective transform should be recorded with reason, method, before/after posture, review, and rollback support.
- A receipt must not expose the sensitive detail it protects through metadata, hashes that are reversible in practice, labels, evidence projections, or public caveats.
- Public release requires validation, policy decision, review state, release manifest, correction path, and rollback target in addition to the receipt.
- If a safe public derivative cannot be produced, the receipt should support `DENY` or `ABSTAIN` rather than silent omission.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Exact source values, source-native geometry, steward notes, sensitive labels, and restricted evidence remain source-bound. |
| WORK / QUARANTINE | Candidate transforms are proposed, policy-checked, reviewed, parameterized, and tested. Unsafe or unresolved transforms remain quarantined. |
| PROCESSED | Reviewed receipts receive deterministic identity, input/output refs, method/version, reason codes, sensitivity before/after, integrity support, and correction posture. |
| CATALOG / TRIPLET | Transform claims may be cataloged only with protected input refs, public-safe output refs, source role, policy basis, and caveats preserved. |
| RELEASE CANDIDATE | Public derivative packages include receipt refs plus validation report, policy decision, review record, release manifest, and rollback target. |
| PUBLISHED | Public API/UI/map layers consume released derivatives and may expose only public-safe receipt projections. |
| CORRECTION | Transform bug, policy change, rights change, source withdrawal, sensitivity upgrade, leak, or stale-state change triggers correction and possible rollback/suppression. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/redaction_receipt.schema.json` beyond the empty scaffold.
- [ ] Add valid fixtures for exact-to-county generalization, grid binning, geometry suppression, temporal delay, label filtering, public evidence projection, withholding, and rollback redaction.
- [ ] Add invalid fixtures for missing input ref, missing output/withholding reason, missing policy decision, missing transform method, unknown transform parameters, missing before/after sensitivity state, public receipt leaking exact geometry, public citation leaking restricted evidence, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, input/output separation, transform method/version, reason codes, sensitivity before/after, policy decision, review record, validation report, integrity hashes, release linkage, correction refs, and rollback refs.
- [ ] Add policy/access tests proving public clients cannot reconstruct restricted geometry or source-private fields from receipt metadata.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add non-regression tests for redaction bugs, source withdrawal, rights change, sensitivity upgrade, transform-version update, public evidence leak, and rollback of released derivatives.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Transform is validated, policy-supported, reviewed, release-linked, and rollback-ready | `ANSWER` / public-safe derivative may cite receipt |
| Evidence, policy, source role, transform parameters, or review are incomplete | `ABSTAIN` |
| Receipt or derivative leaks sensitive details, violates rights, or bypasses release | `DENY` |
| Schema/validator/runtime/transform failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and scaffold status before replacement. |
| Schema metadata | Confirms the paired schema path, title, empty properties, permissive additional properties, PROPOSED status, source doc, and contract doc link. |
| Directory Rules / canonical path register | Confirms `contracts/` owns object meaning, schemas own machine shape, and `RedactionReceipt` is the Flora transform receipt for redaction/generalization. |
| Flora object-family register | Confirms `RedactionReceipt` is an expected Flora object family and that field-level shape remains outside the register. |
| Flora sensitivity posture | Confirms exact sensitive plant locations are withheld from public surfaces by default, generalized safe representations are preferred, protective transforms require receipts, and policy/rules outrank the public stance statement. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |
| KFM trust posture | Confirms evidence, source role, policy, review, release, correction, and rollback must outrank generated summaries, public map layers, or receipt text. |

---

## Rollback

Redaction-receipt rollback is required when a transform weakens protection, becomes unreproducible, violates policy, leaks restricted detail, misstates source role, breaks release lineage, or cannot support correction.

Rollback triggers include:

- public receipt, derivative, or evidence projection leaks exact sensitive geometry;
- transform parameters were wrong, undocumented, stale, or unreproducible;
- source rights change or source withdrawal invalidates derivative release;
- policy decision, review state, or sensitivity state changes;
- public derivative was released without a valid receipt;
- receipt exists but release manifest or rollback target is missing;
- model/aggregate/candidate source was transformed into a misleading observed/exact public claim;
- metadata, caveats, or labels allow inference of restricted content;
- correction notice invalidates input, output, method, or public caveat.

Rollback artifacts should include receipt IDs, input refs, output derivative refs, release IDs, affected layer/API/UI IDs, evidence refs, policy decisions, review records, validation reports, correction notices, rollback cards, replacement receipts, rebuilt derivatives, and suppression instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| What transform-method enum should be canonical for Flora and shared sensitivity policy? | NEEDS VERIFICATION | Resolve with schema, policy, and redaction stewards. |
| Which receipt fields may be public, and which must remain internal-only? | NEEDS VERIFICATION | Define public receipt projection fixtures and API rules. |
| How should hashes be designed so they prove integrity without enabling sensitive reconstruction? | NEEDS VERIFICATION | Security/privacy review and validator fixtures. |
| Which grid/bin/generalization thresholds are acceptable for rare plants by default? | NEEDS VERIFICATION | Sensitivity policy + redaction fixtures. |
| Should withheld/denied outputs emit a public receipt projection or only a public withholding reason? | PROPOSED / NEEDS VERIFICATION | Resolve with policy, UI, and release stewards. |
| How should receipts compose when multiple transforms are chained? | NEEDS VERIFICATION | Define supersession/lineage model and rollback tests. |

---

## Related contracts

- `rare_plant_record.md` — high-sensitivity source record that commonly requires redaction.
- `occurrence_restricted.md` — exact/internal occurrence surface that should feed public output only through governed derivatives.
- `occurrence_public.md` — public-safe occurrence derivative produced after redaction/generalization when approved.
- `range_polygon.md` — public-safe or generalized range/distribution geometry may require transform receipt.
- `phenology_observation.md` — timing/location combinations may require delay, aggregation, or suppression.
- `habitat_association.md` and `vegetation_community.md` — contextual joins can amplify sensitive inference and may require suppression/generalization.
- `specimen_record.md` and `botanical_survey.md` — source evidence that may contain sensitive locality or route detail.
- `domain_validation_report.md` — validation report for transform correctness, policy checks, fixtures, and releases.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md`, `docs/domains/flora/OBJECT_FAMILIES.md`, and `docs/domains/flora/SENSITIVITY_POSTURE.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any public Flora derivative depends on this receipt contract.
- [ ] Add policy/access-control tests proving receipts cannot leak exact geometry, restricted evidence, or source-private fields.
- [ ] Add transform-method vocabulary and parameters through schema/policy review rather than ad hoc implementation.
- [ ] Confirm every public derivative generated from restricted/sensitive Flora data has receipt, validation report, release manifest, correction path, and rollback target.
- [ ] Confirm public API/UI/map/AI surfaces consume public-safe receipt projections only.
- [ ] Record any contract/schema/path/policy/transform conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
