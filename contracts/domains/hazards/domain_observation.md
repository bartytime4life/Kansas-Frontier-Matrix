<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hazards-domain-observation
title: Domain Observation Contract — Hazards
type: semantic-contract
version: v0.2
status: draft; PROPOSED; CONFLICTED schema-home/path form; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Observation steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hazards; observation-envelope; source-role-aware; time-aware; not-for-life-safety; evidence-bound; release-gated; rollback-aware
tags: [kfm, contracts, hazards, domain_observation, observation-envelope, HazardObservation, HazardEvent, WildfireDetection, SmokeContext, EarthquakeEvent, source-role, observed, candidate, modeled, regulatory, aggregate, administrative, synthetic, evidence-bundle, not-for-life-safety, correction, rollback]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./hazards_decision_envelope.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/IDENTITY_MODEL.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/API_CONTRACTS.md
  - ../../../docs/architecture/hazards-trust-membrane.md
  - ../../../schemas/contracts/v1/domains/hazards/domain_observation.schema.json
  - ../../../policy/domains/hazards/
  - ../../../fixtures/domains/hazards/domain_observation/
  - ../../../tests/domains/hazards/test_domain_observation.*
  - ../../../data/registry/sources/hazards/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold at contracts/domains/hazards/domain_observation.md."
  - "The paired schema exists at schemas/contracts/v1/domains/hazards/domain_observation.schema.json, but remains a PROPOSED scaffold with only spec_hash, id, and version fields plus additionalProperties=true."
  - "CONFLICTED path form: current mounted repo evidence uses contracts/domains/hazards/ and schemas/contracts/v1/domains/hazards/, while parts of Hazards canonical-path doctrine argue for flat contracts/hazards/ and schemas/contracts/v1/hazards/. This file follows the mounted target path and paired schema pointer."
  - "DomainObservation is a source-role-aware observation envelope. It is not a regulatory zone, not a model, not an aggregate, not an administrative declaration, not a candidate promotion, not a synthetic narrative, not a public layer, not EvidenceBundle proof, and not life-safety guidance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Observation Contract — Hazards

> Semantic contract for `domain_observation`: the Hazards observation envelope used to normalize source-role-aware, evidence-bound observed records and observation candidates before they become specialized Hazards object families, catalog/triplet claims, released public layers, Evidence Drawer payloads, or governed API responses.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hazards" src="https://img.shields.io/badge/domain-Hazards%20%5BDOM--HAZ%5D-orange">
  <img alt="Object: domain_observation" src="https://img.shields.io/badge/object-domain__observation-blue">
  <img alt="Boundary: observed only when observed" src="https://img.shields.io/badge/boundary-observed__only__when__observed-critical">
  <img alt="Alert authority: never" src="https://img.shields.io/badge/alert__authority-never-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
</p>

`contracts/domains/hazards/domain_observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Path conflict](#path-conflict) · [Observation envelope vs object families](#observation-envelope-vs-object-families) · [Observation vs non-observation roles](#observation-vs-non-observation-roles) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Observation classes](#observation-classes) · [Temporal rules](#temporal-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/hazards/domain_observation.md`  
> **Schema path:** `schemas/contracts/v1/domains/hazards/domain_observation.schema.json`  
> **Schema posture:** paired schema exists, but remains a `PROPOSED` scaffold with only `spec_hash`, `id`, and `version` visible and `additionalProperties: true`.  
> **Truth posture:** Hazards doctrine confirms `HazardObservation` and observation-like source roles, but field-level schema shape, validator enforcement, fixtures, policy runtime, release artifacts, public API/UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `domain_observation` is an observation envelope. It must not upgrade regulatory, modeled, aggregate, administrative, candidate, or synthetic material into observation truth. It also must not present KFM as an emergency alert or life-safety instruction surface.

---

## Meaning

`domain_observation` represents a Hazards-domain observation envelope: a normalized, source-role-preserving record of something observed, reported, detected, measured, or submitted for review.

It may route or support:

- direct hazard observations from official or scientific sources;
- historical hazard event records that include observed facts;
- remote-sensing detections such as active fire or smoke detections;
- earthquake readings or measured event attributes;
- storm reports or source-provided event observations;
- warning/advisory/watch issuance records when handled as source-context records with issue/expiry and not-for-life-safety posture;
- candidate observations that remain in WORK/QUARANTINE until governed promotion resolves evidence, deduplication, source role, and review state.

It answers:

- What was observed, reported, detected, or submitted?
- Which source supplied it, under which source role, rights posture, cadence, attribution, and authority limits?
- What event/observed/source/issue/expiry/valid/retrieval/release/correction times are attached?
- Which specialized Hazards object family should own downstream meaning?
- Which EvidenceRefs/EvidenceBundles, PolicyDecisions, ReviewRecords, ReleaseManifests, CorrectionNotices, and RollbackCards must resolve before public claims or maps can use it?

`domain_observation` is a normalization and routing contract, not sovereign truth and not release authority.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable observation meaning | `contracts/domains/hazards/domain_observation.md` | This file; semantic contract for Hazards observation envelopes. |
| Machine schema | `schemas/contracts/v1/domains/hazards/domain_observation.schema.json` | CONFIRMED scaffold; field-level shape still thin. |
| Feature identity | `contracts/domains/hazards/domain_feature_identity.md` | Stable ID, role, time, geography, digest companion. |
| Layer descriptor | `contracts/domains/hazards/domain_layer_descriptor.md` | Public/release layer descriptor; not observation truth. |
| Validation report | `contracts/domains/hazards/domain_validation_report.md` | Planned validation-report semantics; still scaffold unless expanded. |
| Decision envelope | `contracts/domains/hazards/hazards_decision_envelope.md` | Planned bounded runtime envelope; still scaffold unless expanded. |
| Source-role doctrine | `docs/domains/hazards/SOURCE_ROLE_MATRIX.md` | Defines seven roles, observation-producing families, deny conditions, and promotion rule. |
| Domain doctrine | `docs/domains/hazards/README.md` | Defines Hazards object families, non-ownership, trust membrane, validators, AI, release/rollback posture. |
| Publication doctrine | `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` | Defines publishable families, gates, UI/API boundary, operational expiry, deny register. |
| Source registry | `data/registry/sources/hazards/` | Expected SourceDescriptor and activation records. |
| Policy | `policy/domains/hazards/` and possibly `policy/release/hazards/` | Expected role, expiry, alert-boundary, source-rights, sensitivity, and release gates. |
| Release | `release/` | ReleaseManifest, CorrectionNotice, RollbackCard, PromotionDecision. |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/hazards/domain_observation.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `domain_observation` |
| Visible properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Contract pointer | `contracts/domains/hazards/domain_observation.md` |
| Fixtures root | `fixtures/domains/hazards/domain_observation/` |
| Validator pointer | `tools/validators/domains/hazards/validate_domain_observation.py` |
| Policy pointer | `policy/domains/hazards/` |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is expanded, this contract defines intended semantics for review and fixture design, but does not prove field-level validation.

---

## Path conflict

> [!WARNING]
> **CONFLICTED / NEEDS VERIFICATION:** current mounted repo evidence uses `contracts/domains/hazards/` and `schemas/contracts/v1/domains/hazards/`. Hazards path doctrine contains unresolved tension with a flat `contracts/hazards/` and `schemas/contracts/v1/hazards/` crosswalk. This file follows the requested mounted path and paired schema pointer. It does not resolve the ADR.

Do not create a second `contracts/hazards/domain_observation.md` without an ADR, redirect, or migration note. Parallel contract homes would weaken contract/schema authority.

---

## Observation envelope vs object families

`domain_observation` helps route evidence. It does not erase Hazards object-family boundaries.

| Observation support | Possible downstream owner | Boundary rule |
|---|---|---|
| Storm report or historical event observation | `HazardEvent` / `HazardObservation` | Historical observed record; not live safety instruction. |
| FIRMS/HMS detection | `WildfireDetection` / `SmokeContext` | Detection is not confirmed fire/perimeter; confidence and source role required. |
| USGS earthquake reading | `EarthquakeEvent` | Event is observed; magnitude/location estimates may carry modeled uncertainty. |
| Warning/advisory/watch issuance fact | `WarningContext` / `AdvisoryContext` | Issuance may be recorded as context; KFM never becomes alert authority. |
| FEMA/agency declaration used as observation | `DisasterDeclaration` | Administrative context; not observed damage/event unless separately evidenced. |
| NFHL or regulatory flood area | `FloodContext` | Regulatory context; not observed inundation. |
| Smoke/flood/drought model output | `SmokeContext`, `DroughtIndicator`, `ImpactArea`, etc. | Modeled output; not observation. |
| Aggregate hazard summary | `ExposureSummary`, `ResilienceSummary`, `DroughtIndicator` | Aggregate scope; not per-place observation. |
| Candidate source row | Candidate object in WORK/QUARANTINE | Not public; promotion requires governed transition. |
| AI-generated summary or reconstruction | Synthetic support, if allowed | Never observed reality. |

---

## Observation vs non-observation roles

A Hazards observation envelope may carry an observed source role, or it may carry candidate-observation support before promotion. It must not relabel other roles as observations.

| Source role | Can this contract carry it? | Required handling |
|---|---:|---|
| `observed` | Yes | Preserve observed/source time, source identity, evidence refs, and uncertainty where material. |
| `candidate` | Yes, pre-publication only | WORK/QUARANTINE until dedup, review, evidence, role, and policy resolve. |
| `regulatory` | Context only, not observation | Route to regulatory-context object; deny observed-event claims. |
| `modeled` | Context only, not observation | Require model identity, run receipt, uncertainty; deny observed claims. |
| `aggregate` | Context only, not observation | Preserve aggregation unit/window; deny per-place observation claims. |
| `administrative` | Context only unless source explicitly records observed facts | Do not cite declaration/proclamation as observed event evidence. |
| `synthetic` | No observed claim | Requires reality-boundary/AIReceipt posture; never observation truth. |

---

## Assertions

A reviewed `domain_observation` should assert:

1. **Observation identity** — stable observation-envelope ID and `spec_hash` tied to source, role, time, geography/version, and normalized digest.
2. **Source identity** — SourceDescriptor ref, source-native record ref, rights/cadence/authority posture, and citation support.
3. **Source-role integrity** — observed/candidate status remains visible; other roles are routed as context, not relabeled.
4. **Object-family routing** — downstream owner family is explicit: `HazardEvent`, `HazardObservation`, `WildfireDetection`, `EarthquakeEvent`, etc.
5. **Temporal scope** — event/observed/source/issue/expiry/valid/retrieval/release/correction times are distinct where material.
6. **Spatial scope** — source geometry, point/area/line support, uncertainty, resolution, geocoding, generalized/public geometry, and sensitivity posture are explicit.
7. **Evidence binding** — EvidenceRefs/EvidenceBundles are resolvable before consequential claims or public use.
8. **Policy/review support** — PolicyDecision and ReviewRecord refs are visible where rights, sensitivity, operational context, or publication risk matters.
9. **Release separation** — observation envelope may support release but never authorizes it.
10. **Correction/rollback lineage** — source updates, role corrections, stale state, supersession, and rollback targets are auditable.
11. **Not-for-life-safety posture** — operational-context observations carry disclaimers and official-source referrals.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Regulatory context as observed event | NFHL/regulatory sources are not observed flood events. |
| Modeled output as observation | Model assumptions, run receipt, and uncertainty must remain visible. |
| Aggregate as per-place truth | Aggregation loses per-record fidelity. |
| Administrative declaration as observed damage | Declaration is administrative unless separately evidenced. |
| Detection as confirmed fire/perimeter | Remote-sensing detection is not legal/ground confirmation by itself. |
| Candidate as public observation | Candidate records remain WORK/QUARANTINE until governed transition. |
| Synthetic/AI summary as observed reality | Generated language is interpretive, not root truth. |
| Observation envelope as EvidenceBundle | EvidenceBundle/proof support remains separate. |
| Observation envelope as public layer | Layer descriptor and release artifacts govern public serving. |
| Observation envelope as life-safety alert | KFM is never an emergency alert authority. |
| Retrieval time as observation time | Fetch cadence must not rewrite the observation. |
| Release time as event time | Publication scheduling is not source/event truth. |

---

## Recommended fields

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical Hazards observation-envelope ID. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic digest over normalized observation semantics. |
| `domain` | Must resolve to `hazards`. |
| `object_family` | Usually `domain_observation`; downstream owner family listed separately. |
| `downstream_object_family` | `HazardObservation`, `HazardEvent`, `WildfireDetection`, `EarthquakeEvent`, etc. |
| `source_descriptor_ref` | SourceDescriptor identity, role, rights, cadence, attribution, authority limits. |
| `source_record_ref` | Source-native ID/table/URL/ref where allowed. |
| `source_role` | Canonical seven-class source role. |
| `knowledge_character` | Hazards-specific label such as `scientific_observation`, `remote_sensing_detection`, `historical_event_record`, `operational_warning`, etc. |
| `candidate_disposition` | candidate, merged, rejected, superseded, quarantined, or accepted enum. |
| `event_time` | Time of event where applicable. |
| `observed_time` | Time the observation/measurement/detection was made. |
| `source_time` | Source assertion/publication/update time. |
| `issue_time` / `expiry_time` | Required for warning/advisory/watch context. |
| `valid_time` | Validity window where source asserts a time span. |
| `retrieval_time` | KFM fetch time; not identity/event truth. |
| `spatial_scope_ref` | Point/line/polygon/grid/area/ref geometry. |
| `geometry_role` | exact_internal, source_scale, generalized_public, aggregate_public, withheld, restricted, synthetic_representation, or accepted enum. |
| `uncertainty_refs` | Location, detection, magnitude, model, confidence, or classification uncertainty refs. |
| `evidence_ref_ids` | EvidenceRefs available for proof/evidence lookup. |
| `evidence_bundle_ids` | EvidenceBundles supporting public claims. |
| `policy_decision_refs` | Policy decisions controlling exposure/release. |
| `review_record_refs` | Steward or reviewer decisions. |
| `release_refs` | ReleaseManifest/PromotionDecision refs if public. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | RollbackCard/rollback target refs. |
| `not_for_life_safety` | Required where operational or public hazards context may be mistaken for alerting. |
| `official_source_referral` | Official-source referral required for operational/safety-adjacent contexts. |
| `quality_flags` | Missing source role, missing evidence, unresolved rights, stale source, expired operational context, candidate state, sensitive geometry, role conflict, release missing. |

---

## Observation classes

| Class | Example | Default posture |
|---|---|---|
| `scientific_observation` | USGS earthquake reading; stream/atmospheric observation cited as Hazards context. | Evidence-bound; source-role visible. |
| `historical_event_record` | NOAA Storm Events row; archival hazard report. | Historical only; not current operational guidance. |
| `remote_sensing_detection` | FIRMS hot pixel; HMS detection/plume. | Detection not confirmation; confidence/vintage visible. |
| `operational_issuance_context` | NWS warning/advisory/watch issuance fact. | Context only; issue/expiry, official referral, not-for-life-safety. |
| `candidate_observation` | Unmerged source row or connector output. | WORK/QUARANTINE only. |
| `corrected_observation` | Source revision or corrected record. | CorrectionNotice/supersession required. |
| `public_safe_observation_derivative` | Released generalized point/area or summarized observation. | ReleaseManifest, EvidenceBundle, policy/review, rollback required. |

---

## Temporal rules

| Time field | Required distinction |
|---|---|
| `event_time` | When the hazard event occurred, if applicable. |
| `observed_time` | When the source observed/measured/detected it. |
| `source_time` | When the source asserted, published, or updated the record. |
| `issue_time` | When an operational warning/advisory/watch was issued. |
| `expiry_time` | When operational context stops being even source-current. |
| `valid_time` | When the source says the assertion applies. |
| `retrieval_time` | When KFM fetched it; never observation truth by itself. |
| `release_time` | When KFM released a public-safe artifact; never event truth. |
| `correction_time` | When a correction/supersession was made; never silent mutation. |

Expired operational context remains auditable as history, but must not be displayed as current.

---

## Lifecycle

| Phase | Observation handling |
|---|---|
| RAW | Source payload/ref, source role, source-native ID, rights, source/observed/issue/expiry/valid times, geometry, and hash are captured. |
| WORK / QUARANTINE | Candidate observation is normalized; missing source role, rights gap, unresolved evidence, missing expiry, stale state, geometry/sensitivity risk, or role conflict quarantines it. |
| PROCESSED | Observation envelope binds identity, source refs, normalized geometry/time, evidence refs, validation results, and policy posture. |
| CATALOG / TRIPLET | Observation may support catalog/triplet claims only with EvidenceBundle closure and role/time caveats. |
| RELEASE CANDIDATE | Public-safe observation derivative must resolve ReleaseManifest, PolicyDecision, ReviewRecord where required, correction path, and rollback target. |
| PUBLISHED | Governed API/UI may serve released public-safe observation derivatives; public clients do not read RAW/WORK/QUARANTINE/source endpoints directly. |
| CORRECTED / SUPERSEDED | Source correction, role correction, stale-state change, dedup result, geometry correction, or release withdrawal creates correction/supersession lineage and rollback support. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/hazards/domain_observation.schema.json` beyond the three visible scaffold fields.
- [ ] Resolve the flat-vs-`domains/` path conflict or record an accepted compatibility rule.
- [ ] Define canonical `downstream_object_family`, `knowledge_character`, `candidate_disposition`, `geometry_role`, `quality_flags`, and temporal field names.
- [ ] Add positive fixtures for NOAA Storm Events observation, USGS earthquake observation, FIRMS/HMS detection, operational issuance context with issue/expiry, candidate observation, corrected observation, and released public-safe derivative.
- [ ] Add negative fixtures for NFHL-as-observed-flood, modeled-smoke-as-observed-smoke, aggregate-as-per-place, declaration-as-damage-observation, detection-as-confirmed-fire, candidate-as-published, synthetic-as-observed, expired-warning-as-current, missing source role, and missing EvidenceBundle.
- [ ] Add validator coverage for source role, downstream family, source descriptor, event/observed/source/issue/expiry/valid times, geometry role, evidence refs, policy refs, release refs, correction refs, rollback refs, and not-for-life-safety markers.
- [ ] Confirm Focus Mode and Evidence Drawer deny/abstain when observation evidence, source role, temporal scope, or release state is incomplete.
- [ ] Confirm public UI/API does not read source endpoints, RAW, WORK, QUARANTINE, or unreleased observation objects directly.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Observation role, time, geometry, evidence, policy, release, correction, and rollback resolve | `ANSWER` or allow public-safe reference |
| Evidence, source role, time, rights, geometry, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, candidate public exposure, synthetic-as-observed, live-alert framing, stale-as-current, or direct-source public read would occur | `DENY` |
| Schema, validator, source read, canonicalization, hash, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Rollback

Rollback is required when observation handling weakens source integrity, source-role separation, temporal truth, evidence closure, sensitivity posture, release governance, or the not-for-life-safety boundary.

Rollback triggers include regulatory context published as observed event; modeled product published as observation; aggregate summary joined as per-place observation; administrative declaration used as damage/event observation without separate evidence; remote-sensing detection rendered as confirmed incident/perimeter; candidate observation reaches public surface; synthetic/AI summary becomes observed reality; expired operational issuance shown as current; missing not-for-life-safety marker or official-source referral; public API/UI reads source endpoint or RAW/WORK/QUARANTINE directly; source correction changes observation semantics; artifact/geometry digest mismatch; or release lacks EvidenceBundle, ReleaseManifest, CorrectionNotice path, and rollback target.

Rollback artifacts should include affected observation IDs, source descriptors, source-native refs, source-role refs, temporal scope, geometry refs, evidence refs/bundles, validation reports, policy decisions, release refs, correction notices, supersession links, rollback cards, invalidated downstream layers/descriptors, and public-cache/style invalidation instructions.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hazards/domain_observation.md` scaffold | CONFIRMED | Target existed as a greenfield scaffold. | Did not contain authoritative observation semantics. |
| `schemas/contracts/v1/domains/hazards/domain_observation.schema.json` | CONFIRMED | Schema pointer, current scaffold fields, fixtures/validator/policy pointers. | Does not enforce full observation semantics. |
| `docs/domains/hazards/SOURCE_ROLE_MATRIX.md` | CONFIRMED | Seven canonical source roles, role/object-family matrix, DENY conditions, promotion-never-upgrades rule. | Some matrix cells remain proposed applications pending fixtures/schema enforcement. |
| `docs/domains/hazards/README.md` | CONFIRMED | Hazards object families, explicit non-ownership, proposed lane layout, anti-collapse patterns, validators, AI, release/rollback posture. | Some implementation claims remain verification-bound. |
| `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` | CONFIRMED | Not-for-life-safety rule, publishable object families, promotion gates, UI/API boundary, stale/expiry/correction/rollback requirements. | It states many route/policy paths as PROPOSED where implementation was not proven. |
| `contracts/domains/hazards/domain_feature_identity.md` | CONFIRMED | Identity tuple and role/time/digest companion semantics. | It is semantic documentation, not validator proof. |
| `contracts/domains/hazards/domain_layer_descriptor.md` | CONFIRMED | Layer descriptor boundary: delivery support, not source truth. | It does not define observations. |
| `contracts/domains/geology/domain_observation.md` | CONFIRMED | Adjacent expanded contract pattern for observation-envelope structure. | Geology-specific object families do not transfer directly to Hazards. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which exact field set should `domain_observation.schema.json` require? | NEEDS VERIFICATION | Schema PR with positive and negative fixtures. |
| Should operational warning/advisory issuance facts be represented as observed, administrative, or separate context posture? | CONFLICTED / NEEDS VERIFICATION | ADR-S-04 / source-role schema review. |
| Which Hazards object families require separate observation contracts after this envelope? | NEEDS VERIFICATION | Contract inventory and schema expansion review. |
| Which validator proves a regulatory FloodContext cannot be routed as HazardObservation? | NEEDS VERIFICATION | Negative fixture and policy/validator implementation. |
| Which public geometry roles are allowed for observations with sensitive or infrastructure-adjacent context? | NEEDS VERIFICATION | Sensitivity policy and release fixture review. |
| Which policy file enforces not-for-life-safety and expired-operational-context denial for observations? | NEEDS VERIFICATION | Policy root inspection and tests. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hazards contract-root README.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — Hazards feature identity contract.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — Hazards layer descriptor contract.
- [`./domain_validation_report.md`](./domain_validation_report.md) — planned validation-report contract scaffold.
- [`./hazards_decision_envelope.md`](./hazards_decision_envelope.md) — planned bounded runtime envelope scaffold.
- [`../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md) — source-role anti-collapse matrix.
- [`../../../docs/domains/hazards/README.md`](../../../docs/domains/hazards/README.md) — Hazards domain operating doctrine.
- [`../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`](../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md) — publication and not-for-life-safety boundary.
- [`../../../docs/architecture/hazards-trust-membrane.md`](../../../docs/architecture/hazards-trust-membrane.md) — hazards trust-membrane architecture note.
- [`../../../schemas/contracts/v1/domains/hazards/domain_observation.schema.json`](../../../schemas/contracts/v1/domains/hazards/domain_observation.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
