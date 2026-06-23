<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-domain-observation
title: Domain Observation Contract — Hydrology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Observation steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hydrology; observation-envelope; source-role-aware; observed-role; time-aware; evidence-bound; release-gated; rollback-aware; not-for-life-safety
tags: [kfm, contracts, hydrology, domain-observation, GaugeSite, FlowObservation, WaterLevelObservation, WaterQualityObservation, GroundwaterWell, AquiferObservation, ObservedFloodEvent, source-role, observed, candidate, regulatory, modeled, aggregate, administrative, synthetic, EvidenceBundle, CitationValidationReport, ReleaseManifest, rollback]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./flow_observation.md
  - ./water_level_observation.md
  - ./water_quality_observation.md
  - ./groundwater_well.md
  - ./aquifer_observation.md
  - ./observed_flood_event.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../schemas/contracts/v1/domains/hydrology/domain_observation.schema.json
  - ../../../policy/domains/hydrology/
  - ../../../fixtures/domains/hydrology/domain_observation/
  - ../../../tests/domains/hydrology/test_domain_observation.*
  - ../../../data/registry/sources/hydrology/
  - ../../../release/candidates/hydrology/
notes:
  - "Expanded from a greenfield scaffold at contracts/domains/hydrology/domain_observation.md."
  - "The paired schema exists at schemas/contracts/v1/domains/hydrology/domain_observation.schema.json, but it remains a PROPOSED stub with only spec_hash, id, and version properties; only id is required and additionalProperties=true."
  - "Hydrology observation doctrine confirms direct, time-stamped, in-situ readings are observed-role objects and that provisional/final status must be preserved."
  - "This contract intentionally keeps observation separate from regulatory NFHL context, modeled hydrographs, aggregate HUC rollups, administrative records, candidates, synthetic/AI content, public layers, and emergency guidance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Observation Contract — Hydrology

> Semantic contract for `domain_observation`: the Hydrology observation envelope that normalizes observed readings, candidate observations, and observation-derived public-safe records while preserving source role, time, unit, qualifier, evidence, policy, release, correction, and rollback boundaries.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hydrology" src="https://img.shields.io/badge/domain-Hydrology%20%5BDOM--HYD%5D-1f9eda">
  <img alt="Object: domain_observation" src="https://img.shields.io/badge/object-domain__observation-blue">
  <img alt="Source role: observed" src="https://img.shields.io/badge/source__role-observed-success">
  <img alt="Boundary: NFHL not observed" src="https://img.shields.io/badge/NFHL-not__observed-critical">
  <img alt="Schema: stub" src="https://img.shields.io/badge/schema-stub%20%2F%20NEEDS__VERIFICATION-orange">
</p>

`contracts/domains/hydrology/domain_observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Observation envelope vs object families](#observation-envelope-vs-object-families) · [Observation vs non-observation roles](#observation-vs-non-observation-roles) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Observation classes](#observation-classes) · [Temporal rules](#temporal-rules) · [Sensitivity and publication](#sensitivity-and-publication) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/hydrology/domain_observation.md`  
> **Schema path:** `schemas/contracts/v1/domains/hydrology/domain_observation.schema.json`  
> **Schema posture:** paired schema exists, but remains a `PROPOSED` stub with only `spec_hash`, `id`, and `version` visible. Only `id` is required and `additionalProperties: true` is still allowed.  
> **Truth posture:** Hydrology observation doctrine is defined in the domain docs, but field-level schema shape, validators, fixtures, policy enforcement, runtime route behavior, emitted EvidenceBundles, release manifests, and UI behavior remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `domain_observation` is not NFHL regulatory context, not a modeled hydrograph, not an aggregate rollup, not an administrative roster, not a candidate promotion, not a synthetic/AI summary, not a public layer, and not emergency or life-safety guidance.

---

## Meaning

`domain_observation` is the Hydrology observation envelope. It defines how KFM records and carries observed Hydrology facts before they become specialized object families, catalog/triplet claims, Evidence Drawer payloads, public-safe layers, exports, or Focus Mode context.

It applies to source-role-aware Hydrology observations such as:

- `GaugeSite` observations and site-linked measurement context;
- `FlowObservation` discharge/streamflow readings;
- `WaterLevelObservation` stage/gage-height readings;
- `WaterQualityObservation` parameter measurements;
- `GroundwaterWell` and `AquiferObservation` measurement-linked context;
- `ObservedFloodEvent` records grounded in observed evidence;
- candidate observations that remain in WORK/QUARANTINE until governed promotion resolves source role, evidence, rights, sensitivity, identity, and review state.

The envelope must preserve:

- source identity and source role;
- observed/source/valid/retrieval/release/correction times;
- value, unit, qualifier, no-data/provisional status, and method where material;
- geometry and public geometry posture;
- EvidenceRefs/EvidenceBundles, PolicyDecisions, ReviewRecords, ReleaseManifests, CorrectionNotices, and RollbackCards.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable observation meaning | `contracts/domains/hydrology/domain_observation.md` | This file; semantic contract for Hydrology observation envelopes. |
| Machine schema | `schemas/contracts/v1/domains/hydrology/domain_observation.schema.json` | Confirmed stub; full observation shape is not enforced yet. |
| Hydrology object catalog | `docs/domains/hydrology/OBJECT_FAMILIES.md` | Defines observation families and flood-family separation. |
| Source-role doctrine | `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | Defines observed/regulatory/modeled/aggregate/admin/candidate/synthetic roles and deny conditions. |
| Contract root | `contracts/domains/hydrology/README.md` | Directory root and object-family boundaries. |
| Feature identity | `contracts/domains/hydrology/domain_feature_identity.md` | Stable identity, source role, time, geography/version, digest companion. |
| Layer descriptor | `contracts/domains/hydrology/domain_layer_descriptor.md` | Public/release layer delivery descriptor, not observation truth. |
| Decision envelope | `contracts/domains/hydrology/decision_envelope.md` | Runtime finite-outcome wrapper. |
| Source registry | `data/registry/sources/hydrology/` | Expected SourceDescriptor instances and role/rights/cadence. |
| Policy | `policy/domains/hydrology/` | Expected source-role, rights, sensitivity, release, and public-exposure gates. |
| Release | `release/candidates/hydrology/` and release roots | ReleaseManifest, CorrectionNotice, RollbackCard, and promotion decisions. |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/hydrology/domain_observation.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `domain_observation` |
| Visible properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Contract pointer | `contracts/domains/hydrology/domain_observation.md` |
| Fixtures pointer | `fixtures/domains/hydrology/domain_observation/` |
| Validator pointer | `tools/validators/domains/hydrology/validate_domain_observation.py` |
| Policy pointer | `policy/domains/hydrology/` |
| Full observation enforcement | NEEDS VERIFICATION |

The schema currently does not prove enforcement of source role, source descriptor, observed time, unit, qualifier, value, no-data semantics, provisional/final status, geometry role, evidence refs, policy refs, release refs, correction refs, or rollback refs.

---

## Observation envelope vs object families

`domain_observation` is a shared envelope. It routes to specialized Hydrology object families without erasing their boundaries.

| Observation support | Specialized family | Boundary rule |
|---|---|---|
| Monitoring site record | `GaugeSite` | Site identity is not the measurement itself. |
| Discharge / streamflow reading | `FlowObservation` | Observed reading; never a forecast or modeled series. |
| Gage height / stage reading | `WaterLevelObservation` | Observed reading with unit/qualifier/provisional state. |
| Water-quality parameter measurement | `WaterQualityObservation` | Parameter/method/detection limits and program rights matter. |
| Groundwater/aquifer-state reading | `GroundwaterWell` / `AquiferObservation` | Private-property/well-owner and Geology cross-lane context require review. |
| Observed inundation evidence | `ObservedFloodEvent` | Must not be derived from NFHL alone. |
| Hydrograph series | `Hydrograph` | May include observed or modeled series, but role flag and receipt/uncertainty are required where modeled. |
| Unverified mark/report/source row | Candidate observation | WORK/QUARANTINE only until governed transition. |

---

## Observation vs non-observation roles

| Source role | Can this envelope carry it? | Required handling |
|---|---:|---|
| `observed` | Yes | Preserve source, time, unit, qualifier, no-data/provisional state, geometry, and evidence. |
| `candidate` | Yes, pre-publication only | WORK/QUARANTINE until review/admission/promotion resolves. |
| `regulatory` | Context only, not observation | Route to `NFHLZone` / `FloodContext`; deny observed-flood claims. |
| `modeled` | Context only, not observation | Require model/run/uncertainty; deny observed-reading framing. |
| `aggregate` | Context only, not per-record observation | Preserve aggregation unit/window; deny per-place truth. |
| `administrative` | Context/site/registry only unless separately evidenced | A roster or registry is not an observation by itself. |
| `synthetic` | No observed claim | AI/simulation/reconstruction is not observed reality. |

---

## Assertions

A reviewed `domain_observation` should assert:

1. **Observation identity** — stable ID and `spec_hash` over source, role, temporal scope, geometry/source record, value/unit/qualifier where material, and normalized digest.
2. **SourceDescriptor linkage** — source identity, source role, rights, cadence, authority limits, and citation posture are resolvable.
3. **Source-role integrity** — observed/candidate status remains visible; regulatory/modeled/aggregate/admin/synthetic material is not relabeled.
4. **Object-family routing** — downstream specialized family is explicit and auditable.
5. **Temporal separation** — source, observed, valid, retrieval, release, and correction times remain distinct.
6. **Measurement semantics** — value, unit, method, parameter code/characteristic, qualifier, no-data, provisional/final status, and datum/reference point are preserved where material.
7. **Geometry posture** — source geometry, public geometry, generalized geometry, restricted geometry, and aggregation scope are distinct.
8. **Evidence binding** — EvidenceRefs resolve to EvidenceBundles before public/consequential claims.
9. **Policy/review support** — rights, sensitivity, private-property, infrastructure, and cross-lane joins route through PolicyDecision/ReviewRecord.
10. **Release/rollback support** — ReleaseManifest, CorrectionNotice path, and RollbackCard are required for public derivatives.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| NFHL regulatory polygon as observed flood event | Regulatory context is not observed inundation. |
| Modeled hydrograph as observed reading | Modeled output requires run receipt/uncertainty and role flag. |
| HUC/watershed aggregate as point observation | Aggregate scope cannot prove per-place fact. |
| Water-right or well registry row as observation | Administrative record is not a measurement unless separately evidenced. |
| Candidate source row as public observation | Candidate remains WORK/QUARANTINE until governed transition. |
| AI summary as evidence | AI is interpretive; EvidenceBundle is the admissible support. |
| Retrieval/release time as observed time | KFM fetch/publication time is not source observation time. |
| Public direct read of RAW/WORK/QUARANTINE | Public clients use governed APIs and released artifacts only. |
| Public layer as observation truth | Layer descriptors and tiles are delivery surfaces, not canonical truth. |
| Emergency flood-warning or life-safety instruction | Hydrology is not an alert authority. |

---

## Recommended fields

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current schema stub.

| Field | Meaning |
|---|---|
| `id` | Canonical Hydrology observation envelope ID. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic digest over normalized observation semantics. |
| `domain` | Must resolve to `hydrology`. |
| `object_type` | `DomainObservation` or accepted enum. |
| `downstream_object_family` | `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `WaterQualityObservation`, `AquiferObservation`, `ObservedFloodEvent`, etc. |
| `source_descriptor_ref` | SourceDescriptor identity, role, rights, cadence, attribution, authority limits. |
| `source_record_ref` | Source-native ID, site/series/sample/event row, URL, or measurement ID where allowed. |
| `source_role` | Canonical role: observed, regulatory, modeled, aggregate, administrative, candidate, synthetic. |
| `candidate_disposition` | candidate, admitted, merged, rejected, quarantined, superseded, or accepted enum. |
| `parameter_ref` | Parameter code, characteristic, method, or source measurement type. |
| `measurement_value` | Numeric or coded observed value where applicable. |
| `unit` | Source and normalized unit, with conversion receipt where converted. |
| `qualifier` | Provisional/final, estimated, no-data, censored, QA flag, detection limit, or source caveat. |
| `observed_time` | Time of measurement/observation. |
| `source_time` | Source assertion/publication/update time. |
| `valid_time` | Validity window where source provides one. |
| `retrieval_time` | KFM fetch time; not observation truth. |
| `release_time` | KFM public release time; not observation truth. |
| `correction_time` | Correction/supersession time; never silent mutation. |
| `spatial_scope_ref` | Site, point, line, polygon, grid, or area reference. |
| `geometry_role` | source_exact, exact_internal, generalized_public, aggregate_public, withheld, restricted, or accepted enum. |
| `evidence_ref_ids` | EvidenceRefs supporting the observation. |
| `evidence_bundle_ids` | EvidenceBundles supporting public claims. |
| `policy_decision_refs` | Policy decisions controlling exposure/release. |
| `review_record_refs` | Steward/sensitivity review decisions. |
| `release_refs` | ReleaseManifest/PromotionDecision refs if public. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | RollbackCard/rollback target refs. |
| `quality_flags` | missing_source_role, missing_unit, missing_observed_time, provisional_only, no_data, source_stale, role_conflict, sensitive_join, nfhl_observed_collapse, modeled_as_observed, aggregate_as_per_place, schema_stub. |

---

## Observation classes

| Class | Example | Required posture |
|---|---|---|
| `gauge_site_context` | USGS/NWIS site metadata. | Site identity; readings separate. |
| `flow_observation` | Streamflow/discharge reading. | Observed time, unit, qualifier/provisional status. |
| `water_level_observation` | Stage/gage-height reading. | Observed time, unit, qualifier/provisional status. |
| `water_quality_observation` | Characteristic/sample measurement. | Method, unit, detection/reporting limit, program rights. |
| `groundwater_observation` | Groundwater/aquifer-state reading. | Private-property/sensitivity review where joins expose risk. |
| `observed_flood_event` | High-water mark, imagery footprint, historical inundation source. | Observed evidence; never NFHL-derived alone. |
| `candidate_observation` | Unverified flood mark or watcher result. | WORK/QUARANTINE only. |
| `corrected_observation` | Source correction or superseded measurement. | CorrectionNotice/supersession and rollback linkage. |

---

## Temporal rules

| Time field | Rule |
|---|---|
| `observed_time` | Required for observation claims where source supplies measurement/event time. |
| `source_time` | Required where source publication/update time matters. |
| `valid_time` | Required when source supplies an effective/valid interval. |
| `retrieval_time` | KFM fetch time; never substitutes for observed/source time. |
| `release_time` | KFM release time; never substitutes for source/observed time. |
| `correction_time` | Correction lineage; never silent overwrite. |

If observed/source/valid support is incomplete, the claim should be narrowed, held, or abstained rather than completed by inference.

---

## Sensitivity and publication

Hydrology observations are often public-safe, but sensitivity increases when observations join to:

- private wells or owner/parcel inference;
- infrastructure assets, dams, bridges, levees, intakes, utilities, or critical facilities;
- exact coordinates tied to sensitive cross-lane ecology, archaeology, land/title, or living-person data;
- drought, irrigation, or water-use claims that imply per-parcel certainty;
- unpublished candidate records, raw sensor feeds, or uncertain rights/cadence sources.

Public release should prefer public-safe geometry and explicit caveats. Exact internal geometry, sensitive joins, restricted source terms, and private-property-adjacent contexts require PolicyDecision, ReviewRecord, and recorded redaction/generalization/aggregation posture before publication.

---

## Lifecycle

| Phase | Observation handling |
|---|---|
| RAW | Source payload/reference, source role, source-native ID, time fields, values/units/qualifiers, geometry, and rights/sensitivity metadata are captured. |
| WORK / QUARANTINE | Normalize observation, unit, time, identity, geometry, evidence refs, and source role; quarantine missing role/time/unit/evidence, rights gaps, sensitivity risk, or role collapse. |
| PROCESSED | Emit validated observation candidate with EvidenceRef, ValidationReport, source-role posture, and quality flags. |
| CATALOG / TRIPLET | Catalog/triplet projections cite the observation by identity and evidence; projections do not become truth. |
| RELEASE CANDIDATE | Public-safe derivative resolves EvidenceBundle, PolicyDecision, ReviewRecord where needed, ReleaseManifest, CorrectionNotice path, and RollbackCard. |
| PUBLISHED | Governed API/UI may serve released public-safe observation or derivative; public clients do not read RAW/WORK/QUARANTINE directly. |
| CORRECTED / SUPERSEDED | Source correction, value/unit/time correction, geometry redaction, role correction, or policy change creates correction/supersession lineage and invalidates affected derivatives. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/hydrology/domain_observation.schema.json` beyond `spec_hash`, `id`, and `version`.
- [ ] Decide whether this envelope is a shared base schema for all observation families or only a semantic contract.
- [ ] Define canonical values for `downstream_object_family`, `source_role`, `candidate_disposition`, `geometry_role`, `qualifier`, and `quality_flags`.
- [ ] Add positive fixtures for `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `WaterQualityObservation`, `GroundwaterWell` / `AquiferObservation`, `ObservedFloodEvent`, candidate observation, and corrected observation.
- [ ] Add negative fixtures for NFHL-as-observed-flood, modeled-hydrograph-as-observed, aggregate-as-per-place, administrative-registry-as-observation, candidate-as-public, AI-summary-as-evidence, retrieval-time-as-observed-time, missing unit, missing observed time, missing EvidenceBundle, and RAW/WORK public exposure.
- [ ] Add validator coverage for source role, SourceDescriptor, value/unit/qualifier, temporal fields, geometry role, evidence refs, policy refs, release refs, correction refs, and rollback refs.
- [ ] Confirm public API/UI uses `decision_envelope` outcomes and never silently falls through to raw source or generic AI answer.
- [ ] Confirm sensitivity policy denies or restricts private-property, infrastructure, and sensitive cross-lane joins.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Observation, source role, value/unit/qualifier, time, geometry, evidence, policy, release, correction, and rollback resolve | `ANSWER` or release-eligible reference |
| Evidence, time, unit, source role, geometry, rights, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, candidate public exposure, sensitive join, synthetic-as-observed, life-safety framing, or direct RAW/WORK read would occur | `DENY` |
| Schema, validator, evidence lookup, source read, policy lookup, release lookup, or canonicalization fails | `ERROR` |

---

## Rollback

Rollback is required when Hydrology observation handling weakens source-role integrity, measurement/time correctness, sensitivity posture, evidence closure, release governance, or correction lineage.

Rollback triggers include NFHL regulatory context published as observed flood; modeled hydrograph or modeled surface presented as observation; aggregate rollup presented as per-place observation; administrative roster/registry presented as measurement; candidate observation reaches public surface; synthetic/AI summary treated as evidence; retrieval/release time substituted for observed time; public API/UI reads RAW/WORK/QUARANTINE directly; private-property or infrastructure-sensitive join exposed without review; source correction changes value/unit/time/geometry semantics; or release lacks EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice path, and RollbackCard.

Rollback artifacts should include affected observation IDs, downstream object-family refs, SourceDescriptor refs, source-native refs, values/units/qualifiers, temporal scope, geometry refs, EvidenceRefs/EvidenceBundles, ValidationReports, PolicyDecisions, ReviewRecords, ReleaseManifests, CorrectionNotices, RollbackCards, invalidated layer descriptors, invalidated decision envelopes, invalidated exports, and public-cache/style invalidation instructions.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hydrology/domain_observation.md` scaffold | CONFIRMED | Target existed as a greenfield scaffold. | Did not contain Hydrology-specific observation semantics. |
| `schemas/contracts/v1/domains/hydrology/domain_observation.schema.json` | CONFIRMED | Schema pointer, current stub fields, fixtures/validator/policy pointers. | Does not enforce full observation fields. |
| `docs/domains/hydrology/OBJECT_FAMILIES.md` | CONFIRMED | Observation families, shared invariants, NFHL/ObservedFloodEvent separation, Hydrograph role, sensitive groundwater posture, object-home crosswalk. | Some field details remain inferred/proposed. |
| `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | CONFIRMED | Seven role vocabulary, source-family roles, object-family role bases, cannot-prove grid, anti-collapse DENY conditions. | Matrix is navigational; machine enforcement requires SourceDescriptor, EvidenceBundle, policy, fixtures, and validators. |
| `docs/domains/hydrology/README.md` | CONFIRMED | Hydrology owns observation families but does not own emergency alerts, NFHL-as-observed, cross-domain canonical truth, or modeled-as-observed claims. | Some implementation/path claims remain PROPOSED / NEEDS VERIFICATION. |
| `docs/domains/hydrology/API_CONTRACTS.md` | CONFIRMED | Governed API trust membrane, finite outcomes, public-path exclusions, layer/drawer/focus gates, release lifecycle. | Routes/DTOs/policy runtime remain PROPOSED / NEEDS VERIFICATION. |
| `contracts/domains/hydrology/domain_feature_identity.md` | CONFIRMED | Identity/source-role/time/digest companion semantics. | Identity contract, not observation schema enforcement. |
| `contracts/domains/hydrology/domain_layer_descriptor.md` | CONFIRMED | Layer delivery boundary: layer is not source truth. | Layer descriptor, not observation object. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `domain_observation` a base schema inherited by observation families, or only a semantic contract? | NEEDS VERIFICATION | Schema steward + Hydrology steward review. |
| Which fields must be required for all Hydrology observation types? | NEEDS VERIFICATION | Schema PR with positive/negative fixtures. |
| How should `GaugeSite` split site metadata from observation measurements in schema and API DTOs? | NEEDS VERIFICATION | Object contract/schema review. |
| Which qualifier/provisional/no-data vocabulary is canonical for USGS/NWIS and water-quality sources? | NEEDS VERIFICATION | SourceDescriptor + fixture review. |
| Which geometry roles are allowed for groundwater/private-property-adjacent observations? | NEEDS VERIFICATION | Policy/sensitivity review. |
| Which validator proves NFHL/regulatory and modeled/aggregate/admin inputs cannot become observed records? | NEEDS VERIFICATION | Validator + negative fixtures. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hydrology contract-root README.
- [`./decision_envelope.md`](./decision_envelope.md) — Hydrology runtime decision-envelope alias.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — Hydrology feature identity contract.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — Hydrology layer descriptor contract.
- [`./domain_validation_report.md`](./domain_validation_report.md) — Hydrology validation report, if present/expanded.
- [`./flow_observation.md`](./flow_observation.md) — flow observation contract, if present/expanded.
- [`./water_level_observation.md`](./water_level_observation.md) — water-level observation contract, if present/expanded.
- [`./water_quality_observation.md`](./water_quality_observation.md) — water-quality observation contract, if present/expanded.
- [`./aquifer_observation.md`](./aquifer_observation.md) — aquifer observation contract.
- [`../../../docs/domains/hydrology/OBJECT_FAMILIES.md`](../../../docs/domains/hydrology/OBJECT_FAMILIES.md) — object-family catalog.
- [`../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md) — source-role anti-collapse matrix.
- [`../../../docs/domains/hydrology/API_CONTRACTS.md`](../../../docs/domains/hydrology/API_CONTRACTS.md) — governed API and finite-outcome doctrine.
- [`../../../schemas/contracts/v1/domains/hydrology/domain_observation.schema.json`](../../../schemas/contracts/v1/domains/hydrology/domain_observation.schema.json) — current schema stub.

[Back to top](#top)
