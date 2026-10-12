<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-borehole-reference
title: BoreholeReference Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Boreholes and wells steward
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
policy_label: restricted-by-default; semantic-contract; geology; borehole-reference; subsurface-point-evidence; source-role-aware; release-gated; public-generalized-only
tags: [kfm, contracts, geology, BoreholeReference, borehole, well, subsurface, point-evidence, well-log, core-sample, hydrostratigraphy, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../../docs/domains/geology/sublanes/README.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../pipelines/domains/geology/boreholes/README.md
  - ../../../schemas/contracts/v1/domains/geology/BoreholeReference.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology BoreholeReference semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/BoreholeReference.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "Object-family naming is CONFLICTED in doctrine: Borehole / BoreholeReference and Well Log / Well LogReference variants appear across Geology docs. This contract preserves the requested path and casing while surfacing the drift."
  - "BoreholeReference is a subsurface point-evidence carrier. It does not prove resource estimates, permits, ownership, hydrology measurements, hazards risk, stratigraphic interpretations, or public release by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BoreholeReference — Geology

> Semantic contract for Geology `BoreholeReference`: the evidence-bound reference object for drilled-hole, well, boring, stratigraphic-test, and related subsurface point records used to support geology claims without becoming public exact-location truth or adjacent-domain authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: BoreholeReference" src="https://img.shields.io/badge/object-BoreholeReference-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: point evidence not public truth" src="https://img.shields.io/badge/boundary-point__evidence__not__public__truth-critical">
</p>

`contracts/domains/geology/BoreholeReference.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Reference classes](#reference-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/BoreholeReference.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/BoreholeReference.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine confirms a borehole-owned object family but records naming drift between `Borehole` and `BoreholeReference`. Field-level schema shape, fixtures, validators, policy runtime, source registry records, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `BoreholeReference` is a location-sensitive evidence carrier. It does **not** publish exact point records, does **not** certify hydrology measurements, does **not** prove ownership, permits, production, reserves, hazards risk, or resource estimates, and does **not** replace `Well LogReference`, `CoreSample`, `StratigraphicInterval`, `GeologicUnit`, `HydrostratigraphicUnit`, or public-safe released derivatives.

---

## Meaning

`BoreholeReference` is the Geology semantic object for a drilled-hole or well-like source reference used as subsurface evidence. It may represent a water well, oil/gas well, stratigraphic test, geotechnical boring, monitoring well, core hole, or source-native borehole record when admitted into KFM.

It answers:

- Which borehole-like source record is being referenced?
- Which source, source role, rights posture, time, geometry precision, depth/datum support, and evidence support apply?
- Which well logs, core/cuttings descriptions, stratigraphic picks, hydrostratigraphic context, or cross-sections may cite this reference?
- What public-safe representation, if any, may be shown without exposing restricted detail?
- Which policy decision, review record, redaction or aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

A borehole reference can support geology interpretation. It is not itself a unit boundary, aquifer measurement, reserve estimate, permit/title fact, or public artifact.

---

## Repo fit

The Geology lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, policy gates admissibility/release, fixtures/tests prove behavior, and data/release roots carry lifecycle and publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Borehole reference meaning | `contracts/domains/geology/BoreholeReference.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/BoreholeReference.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Human-facing sublane doctrine | `docs/domains/geology/sublanes/boreholes-wells.md` | Governs boreholes/wells sublane posture |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Records Borehole / BoreholeReference meaning and sensitivity posture |
| Scope boundary | `docs/domains/geology/SCOPE.md` | Confirms Geology owns boreholes/logs/cores but not adjacent-domain truth |
| Pipeline logic | `pipelines/domains/geology/boreholes/README.md` | Executable processing/handoff support only |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, and public-safe proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |
| Published surfaces | `data/published/layers/geology/` and governed APIs/UI | Released generalized or aggregated derivatives only |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/BoreholeReference.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/BoreholeReference.schema.json` |
| Exact schema result | Not found in this session |
| Casing posture | `BoreholeReference` preserved because the user requested this path and Geology docs use this spelling in the reference-form roster |
| Naming drift | `Borehole` / `BoreholeReference` is CONFLICTED until ADR/schema decision |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `BoreholeReference` should semantically assert:

1. **Reference identity** — deterministic identity for the source borehole/well/boring record or public-safe derivative reference.
2. **Source identity** — SourceDescriptor, source record ID, source role, source vintage, rights, cadence, and attribution.
3. **Borehole class** — water well, oil/gas well, stratigraphic test, geotechnical boring, monitoring well, core hole, candidate, or source-native class.
4. **Location posture** — exact, source-precision, generalized, aggregated, withheld, public-safe, or unknown geometry support.
5. **Depth/datum support** — total depth, depth interval, datum, elevation, units, completion/drilling context, and uncertainty where source-supported.
6. **Evidence linkage** — references to well logs, core/cuttings, driller records, source documents, stratigraphic picks, cross-sections, or EvidenceBundles.
7. **Temporal support** — source, observed/drilled, valid, retrieval, release, correction, and stale-state times where material.
8. **Access and release posture** — internal access, public derivative, review, redaction/aggregation receipt, release manifest, and rollback target.
9. **Cross-lane boundaries** — Hydrology, People/Land, Hazards, and resource claims remain separate authority classes.
10. **Correction posture** — source revision, identity merge/split, location correction, depth/datum correction, rights change, and release rollback lineage.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a borehole point as a public exact-location layer | Public derivatives require governed generalization or aggregation and release support. |
| Treating a borehole as a geologic unit boundary | A borehole is evidence; unit interpretation belongs to the relevant unit/stratigraphy contract. |
| Treating a borehole as a hydrology measurement | Hydrology owns water levels, flows, water quality, and measurement truth. |
| Treating a borehole as ownership, lease, permit, or title proof | People/Land or source-specific regulatory records own those claims. |
| Treating a well log as owned by this object | Well logs are linked evidence or separate references, not collapsed into BoreholeReference. |
| Treating depth picks as accepted stratigraphy without review | Picks and tops require evidence, method, uncertainty, and interpretation version. |
| Treating a public generalized point as exact | Public-safe geometry is a derivative with caveats, not the internal exact geometry. |
| Treating a pipeline run as release approval | Publication requires release manifest, policy outcome, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM borehole reference identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `BoreholeReference` or accepted canonical synonym after naming reconciliation. |
| `borehole_class` | Water well, oil/gas well, stratigraphic test, geotechnical boring, monitoring well, core hole, candidate, or source-native type. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Administrative, observed, aggregate, modeled, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native borehole/well/boring ID. |
| `source_record_keys` | API number, water-well ID, permit ID, local ID, catalog ID, or other source-native keys where allowed. |
| `borehole_name` | Public-safe name/label, when allowed. |
| `location_ref_internal` | Access-controlled internal geometry reference. |
| `public_geometry_ref` | Generalized/aggregated public-safe geometry reference, if released. |
| `geometry_precision` | Exact, source precision, generalized, aggregated, withheld, unknown. |
| `coordinate_uncertainty` | Source/native/georeferenced uncertainty. |
| `total_depth` | Total depth and units, if source-supported. |
| `depth_datum` | Ground surface, Kelly bushing, sea level, source-native datum, or unknown. |
| `elevation_ref` | Elevation and datum reference, if available. |
| `drill_or_completion_time` | Drilling/completion/observation time, if material. |
| `source_time` | Source assertion or publication time. |
| `retrieval_time` | Time KFM retrieved the record. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `well_log_refs` | Linked `Well LogReference` objects, when applicable. |
| `core_sample_refs` | Linked core/cuttings/sample references, when applicable. |
| `stratigraphic_pick_refs` | Linked picks/tops/interpretations, with method/version caveats. |
| `hydrostratigraphic_refs` | Context refs to `HydrostratigraphicUnit`, not Hydrology measurement ownership. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Restricted, generalized-public, aggregated-public, withheld, rights-limited, public-safe, or unknown. |
| `policy_decision_ref` | Policy result governing use or release. |
| `review_record_ref` | Source, geology, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when geometry/fields are generalized or withheld for public output. |
| `aggregation_receipt_ref` | Required when records become aggregate public products. |
| `validation_report_ref` | Validation report for schema, geometry, source-role, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, merge/split, source update, location/depth correction, rights update, and rollback lineage. |
| `quality_flags` | Source-role conflict, identity collision, geometry uncertainty, rights unknown, sensitivity unknown, depth/datum missing, stale source, or incomplete evidence. |

---

## Reference classes

| Class | Meaning | Default posture |
|---|---|---|
| `water_well` | Water-well or related source record. | Context only for Geology unless Hydrology owns measurement refs. |
| `oil_gas_well` | Oil/gas well or regulatory source record. | Geology point evidence; permits/production/ownership are separate claims. |
| `stratigraphic_test` | Stratigraphic or scientific test hole. | May support stratigraphic interpretation with review. |
| `geotechnical_boring` | Engineering/geotechnical boring. | Context/evidence only; source rights may constrain use. |
| `monitoring_well` | Monitoring well reference. | Geology context only; measurements belong to Hydrology/other owning lane. |
| `core_hole` | Borehole tied to core/cuttings. | Link to core/sample refs; do not collapse identities. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `public_derivative` | Released generalized or aggregated representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | BoreholeReference posture |
|---|---|---|
| Well registry, permit table, catalog, inventory | `administrative` or `regulatory` | Identifies records and status context; does not prove geology interpretation by itself. |
| Driller log, well completion, measured depth, core description | `observed` | Evidence-bearing record; must preserve method, time, depth/datum, and uncertainty. |
| Compiled map, portal rollup, county summary, density product | `aggregate` | Aggregate support only; not exact record identity unless source row resolves. |
| Interpreted tops, predicted depth, inferred lithology, modeled surfaces | `modeled` | Must remain interpretation/model output with method and uncertainty. |
| Unreviewed import, fuzzy crosswalk, unmatched source row | `candidate` | Quarantine until identity, source, and rights resolve. |
| AI-generated or reconstructed well note | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Sensitivity and release

Borehole references carry location, subsurface, source-rights, and adjacent-domain risk. The safe default is to keep exact/internal detail behind governed access and expose only reviewed public-safe derivatives where release permits.

Rules:

- Exact/internal point geometry is not a normal public artifact.
- Public derivatives should use generalized or aggregated geometry with clear caveats, where approved.
- Public evidence/citation projections must not reveal restricted source details.
- Rights, source terms, and source-role ambiguity trigger quarantine, abstain, deny, or review rather than publication.
- Public outputs must preserve source role, source vintage, geometry precision, depth/datum caveats, and interpretation caveats.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native well/borehole rows, coordinates, logs, permits, depths, completion fields, and metadata remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, source-role checked, identity-crosswalked, rights/sensitivity-screened, geometry-checked, depth/datum-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, source support, geometry posture, depth/datum posture, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, evidence, geometry precision, access state, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision, review record, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released generalized or aggregated public-safe derivatives appear in public clients. |
| CORRECTION | Source update, identity collision, merge/split, geometry correction, depth/datum correction, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve `Borehole` vs `BoreholeReference` naming through ADR, schema PR, or drift-register decision.
- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for water well, oil/gas well, stratigraphic test, geotechnical boring, core hole, candidate import, and public generalized/aggregated derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, identity collision, unresolved geometry precision, missing depth/datum where material, rights unknown, direct public exact point, missing policy decision, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source keys, geometry precision, CRS, depth/datum, temporal support, source role, evidence refs, policy refs, release refs, and correction refs.
- [ ] Add policy/access tests proving public clients consume released derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, schema rename, identity merge/split, geometry correction, rights update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, source role is clear, policy allows, derivative is released | `ANSWER` / public-safe derivative may be shown |
| Evidence, rights, source role, identity, geometry, or interpretation support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, or release is absent | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns borehole/log/core families and does not own Hydrology, People/Land, Hazards, UI/AI truth. | Records naming drift. |
| Geology object-family doc | Confirms BoreholeReference / Borehole purpose, intrinsic-key proposals, sensitivity posture, source roles, and roster drift. | Field realization remains PROPOSED. |
| Boreholes-wells sublane doc | Confirms sublane scope, reference-form naming, restricted/default-generalized posture, and sublane path caveats. | Human-facing doctrine, not schema enforcement. |
| Boreholes pipeline README | Confirms pipeline orientation and separation of executable processing from contracts/policy/release. | Does not prove runtime behavior. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized BoreholeReference claim weakens source integrity, misstates source role, crosses adjacent-domain ownership, exposes restricted detail, or depends on superseded identity, geometry, rights, or release evidence.

Rollback triggers include:

- object-family name/casing is superseded by ADR or schema decision;
- source record is corrected, withdrawn, merged, or split;
- location precision or public derivative is corrected;
- depth/datum or well identity is corrected;
- linked log/core/pick evidence is withdrawn or corrected;
- public layer/API/UI uses an unreleased internal record;
- release manifest lacks receipt, policy decision, correction path, or rollback target.

Rollback artifacts should include affected BoreholeReference IDs, source record IDs, geometry refs, public derivative refs, linked Well LogReference/CoreSample/StratigraphicInterval refs, evidence refs, policy decisions, receipts, release IDs, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `BoreholeReference` the canonical contract name, or should it normalize to `Borehole`? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted paired schema path and casing? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which source keys are safe and stable enough for deterministic identity? | NEEDS VERIFICATION | Source registry and fixture review. |
| What public generalization/aggregation forms are acceptable for each source family? | NEEDS VERIFICATION | Policy and release fixtures. |
| How should well logs and core samples reference the borehole without collapsing identities? | NEEDS VERIFICATION | Companion contracts and schema references. |
| Which hydrology handoffs are context-only and which require Hydrology-owned objects? | NEEDS VERIFICATION | Cross-lane policy and Hydrology steward review. |

---

## Related contracts and docs

- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and naming drift.
- `docs/domains/geology/sublanes/boreholes-wells.md` — human-facing boreholes/wells sublane doctrine.
- `pipelines/domains/geology/boreholes/README.md` — executable processing orientation; not semantic authority.
- `contracts/domains/geology/README.md` — parent contract lane scaffold.
- `contracts/domains/geology/sublanes/README.md` — contract sublane orientation.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.

---

## Maintainer checklist

- [ ] Resolve `Borehole` / `BoreholeReference` naming drift.
- [ ] Create or verify paired schema and fixtures.
- [ ] Add policy tests for restricted/internal vs public-safe derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released generalized or aggregated derivatives.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved naming/path/schema drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
