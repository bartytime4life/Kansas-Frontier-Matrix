<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-domain-observation
title: Domain Observation Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Observation steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; domain-observation; observation-envelope; source-role-aware; evidence-bound; sensitivity-aware; no-release-authority
tags: [kfm, contracts, geology, domain_observation, observation-envelope, source-role, observed-time, source-time, evidence-ref, evidence-bundle, geophysical-observation, geochemistry-sample, borehole, well-log, core-sample, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./GeophysicalObservation.md
  - ./GeochemistrySample.md
  - ./BoreholeReference.md
  - ./WellLogReference.md
  - ./CoreSample.md
  - ./Lithology.md
  - ./StratigraphicInterval.md
  - ./GeologicUnit.md
  - ./HydrostratigraphicUnit.md
  - ./MineralOccurrence.md
  - ../../../docs/domains/geology/IDENTITY_MODEL.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/domain_observation.schema.json
  - ../../../fixtures/domains/geology/domain_observation/
  - ../../../tools/validators/domains/geology/validate_domain_observation.py
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a greenfield scaffold into a Geology domain_observation semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/geology/domain_observation.schema.json, but it is still a PROPOSED stub with only id, version, and spec_hash fields; field-level enforcement remains NEEDS VERIFICATION."
  - "DomainObservation is an observation envelope and normalization/routing contract. It is not a source descriptor, EvidenceBundle, public layer, policy decision, release manifest, AI answer, or specialized Geology object-family contract."
  - "Geology observations must preserve source role and the distinct KFM time dimensions, especially observed_time versus source_time, retrieval_time, release_time, and correction_time."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Observation — Geology

> Semantic contract for `domain_observation`: the Geology observation envelope used to normalize source-role-aware, evidence-bound observations before they become specialized Geology records, catalog/triplet claims, public-safe layer features, governed API payloads, or release artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: domain_observation" src="https://img.shields.io/badge/object-domain__observation-blue">
  <img alt="Schema: stub" src="https://img.shields.io/badge/schema-stub%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Truth: evidence bound" src="https://img.shields.io/badge/truth-evidence__bound-informational">
  <img alt="Boundary: observation not release authority" src="https://img.shields.io/badge/boundary-observation__not__release__authority-critical">
</p>

`contracts/domains/geology/domain_observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Observation envelope vs object families](#observation-envelope-vs-object-families) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Observation classes](#observation-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Anti-collapse rules](#anti-collapse-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/domain_observation.md`  
> **Schema path:** `schemas/contracts/v1/domains/geology/domain_observation.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` stub. It currently defines only `spec_hash`, `id`, and `version`, requires only `id`, and permits additional properties.  
> **Truth posture:** Geology doctrine supports observation/source-role/time distinctions and the owned observation families, especially geophysical observations, geochemistry samples, boreholes, well logs, and core samples. Field-level schema enforcement, fixtures, validator behavior, policy runtime, release workflow, API behavior, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `domain_observation` is a normalization envelope. It does **not** prove a public Geology claim by itself, does not replace specialized object-family contracts, does not publish exact coordinates or payloads, does not authorize map/API/UI/AI use, and does not bypass EvidenceBundle, policy, review, release, correction, or rollback controls.

---

## Meaning

`domain_observation` is the Geology lane's generic semantic envelope for a bounded observation, source-provided observation candidate, observed record, interpreted observation support, or normalized observation unit before that unit is specialized into one or more Geology object families.

It can carry source-provided or normalized context for:

- field or remote-sensed geophysical observations;
- geochemistry samples and analytical results;
- borehole, well-log, and core/cuttings observations;
- field notes, mapped contacts, lithology descriptions, structural observations, measured sections, or source-native geologic observation rows;
- candidate observations awaiting review;
- restricted internal observations that may later yield public-safe derivatives;
- public-safe observation derivatives that have already passed redaction, policy, review, and release gates.

A `domain_observation` answers:

- What was observed, measured, logged, sampled, surveyed, modeled, aggregated, administered, or proposed?
- Which source supplied it, under which source role, rights posture, cadence, and attribution rules?
- What spatial, temporal, material, analytical, evidentiary, uncertainty, sensitivity, and custody support does it carry?
- Which specific Geology object family should own downstream meaning?
- Which EvidenceRef/EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, AggregationReceipt, ReleaseManifest, CorrectionNotice, and rollback references must resolve before the observation contributes to public claims?

It is a normalization and routing contract, not sovereign truth.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Observation-envelope meaning | `contracts/domains/geology/domain_observation.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/domain_observation.schema.json` | CONFIRMED stub; field-level enforcement NEEDS VERIFICATION |
| Feature identity | `contracts/domains/geology/domain_feature_identity.md` | Identity companion; not replaced |
| Layer descriptor | `contracts/domains/geology/domain_layer_descriptor.md` | Public/release-layer descriptor; not observation truth |
| Specialized observation families | `GeophysicalObservation.md`, `GeochemistrySample.md`, `BoreholeReference.md`, `WellLogReference.md`, `CoreSample.md` | Downstream/sibling contracts that own specialized meaning |
| Context families | `Lithology.md`, `StratigraphicInterval.md`, `GeologicUnit.md`, `StructureFeature.md`, `HydrostratigraphicUnit.md` | May cite observations as evidence; not replaced |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, role, cadence, activation |
| Evidence/proofs/catalog | EvidenceBundle, ValidationReport, catalog/triplet homes — accepted paths NEED VERIFICATION | Claim support and discoverability |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Admission/release decisions and fail-closed geometry/payload behavior |
| Fixtures/tests | `fixtures/domains/geology/domain_observation/`, `tests/domains/geology/` | Validation and non-regression proof |
| Release and rollback | `release/manifests/geology/`, accepted release homes | ReleaseManifest, CorrectionNotice, RollbackCard, withdrawal support |

---

## Schema posture

The paired schema exists but is intentionally thin.

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/geology/domain_observation.schema.json` |
| Schema status | `PROPOSED` |
| Schema description | Greenfield placeholder; fields to be defined per contract document and ADR |
| Defined properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Schema-linked fixtures root | `fixtures/domains/geology/domain_observation/` |
| Schema-linked validator | `tools/validators/domains/geology/validate_domain_observation.py` |
| Validator implementation | NEEDS VERIFICATION; schema references the path, but runtime/file behavior was not verified here |

Until the schema is expanded, this contract is the semantic authority for review and fixture design, but not proof of field-level validation.

---

## Observation envelope vs object families

`domain_observation` helps route evidence. It does not erase object-family boundaries.

| Observation support | Possible downstream owner | Boundary rule |
|---|---|---|
| Field or remote-sensed survey reading | `GeophysicalObservation` | Derived surfaces must remain modeled and labeled. |
| Sample collection / assay / analytical result | `GeochemistrySample` | Collection time and analytical report time must not collapse. |
| Borehole/well source row | `BoreholeReference` | Exact point geometry restricted/generalized by default. |
| LAS/well-log curve or interpreted top | `WellLogReference` | Curves may be observed; interpreted tops are modeled. |
| Core/cuttings/sample interval | `CoreSample` | Physical sample/custody context remains specialized. |
| Material-character note | `Lithology` | Observation can support lithology; it is not the lithology descriptor itself. |
| Named interval/top/bound | `StratigraphicInterval` | Observation can support interval bounds; interval identity remains separate. |
| Mapped unit/contact observation | `GeologicUnit` / `StructureFeature` / `GeologyBoundaryVersion` | Observation can support map/structure/boundary truth; it is not the published layer. |
| Occurrence report | `MineralOccurrence` | Presence report is not deposit, estimate, ownership, or extraction proof. |
| Hydrostratigraphic context support | `HydrostratigraphicUnit` | Geology context only; Hydrology measurements remain outside Geology. |

---

## Assertions

A reviewed `domain_observation` should semantically assert:

1. **Observation identity** — stable observation-envelope ID and `spec_hash`.
2. **Observation class** — field observation, survey observation, sample observation, log observation, core observation, source-native observation, modeled/interpreted observation support, aggregate observation, candidate, synthetic, or public derivative.
3. **Observed subject** — what the observation concerns: geologic material, structure, interval, geophysical signal, sample, log curve, borehole context, occurrence report, or source-native object.
4. **Source identity** — SourceDescriptor ref, source record ref, source role, source time, rights, cadence, and attribution.
5. **Temporal support** — observed time, source time, valid time, retrieval time, release time, and correction time remain distinct where material.
6. **Spatial support** — geometry ref, geometry fingerprint, public-safe geometry fingerprint, precision state, coordinate uncertainty, scale, or withheld geometry posture.
7. **Evidence support** — EvidenceRef/EvidenceBundle refs, supporting artifact digests, analytical method refs, survey refs, log artifact refs, sample refs, or report refs.
8. **Uncertainty and quality** — confidence, method, instrument, detection limit, interval uncertainty, source caveat, or quality flag.
9. **Sensitivity and rights** — exact/detail exposure posture, redaction/aggregation receipt refs, rights limitations, access tier, or withheld state.
10. **Routing decision** — which specialized object-family contract receives downstream meaning.
11. **Governance state** — validation, policy, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating observation envelope as final object-family truth | Specialized contracts own final meaning. |
| Treating observation as public release approval | ReleaseManifest / PromotionDecision owns publication. |
| Treating observation as policy decision | Policy owns allow/restrict/deny/abstain. |
| Treating observation as EvidenceBundle | Observations cite evidence; EvidenceBundle carries support. |
| Treating observed and modeled as interchangeable | Role change rotates meaning and can require a separate identity. |
| Treating collection time as analytical report time | Collapsing observed/source time can break chain-of-custody and provenance. |
| Treating exact subsurface/sample/resource geometry as public by default | Sensitive location and rights controls fail closed. |
| Treating administrative or regulatory record as observed geology | Source-role anti-collapse applies. |
| Treating aggregate observation as per-place truth | Aggregate loses per-record fidelity. |
| Treating AI text as observation | AI is interpretive and cannot supply source evidence. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. Only `id`, `version`, and `spec_hash` are currently visible in the confirmed schema stub.

| Field | Meaning |
|---|---|
| `id` | Canonical domain observation ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized observation-envelope digest. |
| `domain` | Must resolve to `geology`. |
| `observation_id` | Source-native or KFM observation ID. |
| `observation_class` | Field, survey, sample, log, core, source-native, modeled, aggregate, candidate, synthetic, or public derivative. |
| `target_object_family` | Intended specialized Geology object-family owner. |
| `target_object_ref` | Downstream object ref if already minted. |
| `domain_feature_identity_ref` | Identity envelope ref where available. |
| `observed_subject` | What was observed/measured/logged/sampled/surveyed. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_id` | Stable SourceDescriptor handle. |
| `source_role` | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, or accepted enum. |
| `source_record_ref` | Source-native row, map feature, report, log, sample, survey, table, or artifact. |
| `source_time` | Source publication/assertion/report time. |
| `observed_time` | Field/sample/log/survey/measurement/acquisition time. |
| `valid_time` | Time interval for the claim, where applicable. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if any. |
| `correction_time` | Correction/supersession time. |
| `geometry_ref_internal` | Access-controlled exact/source geometry ref. |
| `public_geometry_ref` | Generalized, aggregate, centroid, or withheld public geometry ref where released. |
| `geometry_fingerprint` | Stable geometry fingerprint where geometry is identity-bearing. |
| `public_safe_geometry_fingerprint` | Public-safe derivative geometry fingerprint where needed. |
| `geometry_precision` | Exact, source precision, generalized, aggregate, withheld, unknown. |
| `method_ref` | Instrument, analytical method, survey method, logging method, or source-native method ref. |
| `artifact_digest` | Digest for source artifact, log file, image, report, table, or survey product. |
| `measurement_units_ref` | Units vocabulary/ref where numeric observations are present. |
| `value_summary` | Public-safe observation value summary; detailed payload may be withheld. |
| `uncertainty_summary` | Public-safe uncertainty/confidence summary. |
| `quality_flags` | Missing source, role conflict, time collapse, geometry uncertainty, rights unknown, sensitivity unknown, method missing, evidence incomplete, stale source. |
| `evidence_refs` | EvidenceRef links that must resolve before claims. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the observation. |
| `rights_state` | Rights, license, attribution, embargo, proprietary, redistribution, or unknown state. |
| `sensitivity_state` | Public, generalized, restricted, withheld, source-limited, rights-limited, sensitive, or unknown. |
| `policy_decision_ref` | Policy decision governing admission/use/release where material. |
| `review_record_ref` | Source, steward, sensitivity, method, or release review. |
| `redaction_receipt_ref` | Required when detail or geometry is generalized/redacted/withheld. |
| `aggregation_receipt_ref` | Required when observations become aggregate public products. |
| `representation_receipt_ref` | Required when synthetic/reconstructed representation is material. |
| `validation_report_ref` | Validation report for schema, source role, time, evidence, geometry, sensitivity, or release candidate. |
| `release_ref` | ReleaseManifest / PromotionDecision / release candidate ref where public use is requested. |
| `correction_refs` | Correction notices, supersession refs, rollback refs, merge/split refs, replacement records. |

---

## Observation classes

| Class | Meaning | Default posture |
|---|---|---|
| `field_observation` | Field-mapped or field-described geology observation. | Observed if source/time/support resolve. |
| `survey_observation` | Geophysical or remote-sensed survey observation. | Observed for acquisition/product; derived surfaces modeled. |
| `sample_observation` | Sample collection, geochemistry, core, or cuttings observation. | Observed with collection/report-time distinction. |
| `log_observation` | Well-log curve, log artifact, or logging observation. | Curves may be observed; interpreted tops modeled. |
| `source_native_observation` | Source row whose native type does not yet map cleanly. | Candidate until mapped and reviewed. |
| `modeled_observation_support` | Model/interpreted derivative based on observations. | Modeled; never observed. |
| `aggregate_observation` | Rollup over a spatial/temporal/category unit. | Aggregate; never per-place truth. |
| `administrative_observation` | Program/registry/admin observation context. | Administrative; never observed geology by default. |
| `candidate_record` | Unreviewed or unresolved observation. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical observation-like record. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released generalized/aggregate/reference-only observation derivative. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source role | Observation meaning | Required behavior |
|---|---|---|
| `observed` | Direct reading, sample, log curve, survey product, or mapped field record. | May support object-family claims if evidence/time/geometry resolve. |
| `regulatory` | Regulatory determination or controlled administrative context. | Keep regulatory label; never relabel as observed geology. |
| `modeled` | Derived/interpreted/model output. | Carry method/run/assumption refs; never relabel observed. |
| `aggregate` | Published summary over an aggregation unit. | Carry aggregation unit/receipt; never join to per-place truth. |
| `administrative` | Program, registry, catalog, permit, or accounting context. | Context only unless independent observed evidence supports geology claim. |
| `candidate` | Detected but unpromoted/unreviewed. | No PUBLISHED edge. |
| `synthetic` | Generated or reconstructed observation-like content. | Reality-boundary/representation receipt; never source observation. |

---

## Sensitivity and release

Geology observations can be public, generalized, restricted, or withheld depending on object family, source rights, precision, payload type, and downstream use.

Rules:

- Exact borehole, well-log, core, private-well, sample, sensitive occurrence, resource-detail, and rights-restricted observation geometry fails closed until policy/review proves public exposure is allowed.
- LAS/log payloads, source artifacts, proprietary survey data, private well details, and exact sample coordinates are not public by default.
- Public derivatives require evidence closure, rights review, policy decision, validation, redaction/aggregation/representation receipts where material, release manifest, correction path, and rollback target.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, stale, time-collapsed, source-role-conflicted, or evidence-incomplete observations must not enter public outputs as authoritative facts.
- Public clients must consume released public-safe derivatives through governed APIs and released artifacts, not RAW/WORK/QUARANTINE or internal stores.

---

## Anti-collapse rules

```text
domain_observation != EvidenceBundle
domain_observation != SourceDescriptor
domain_observation != PolicyDecision
domain_observation != ReleaseManifest
domain_observation != DomainLayerDescriptor
domain_observation != AI summary
```

Geology-specific denials:

```text
Observed != modeled
Aggregate != per-place observation
Administrative != observed geology
Regulatory != field measurement
Synthetic != observed reality
GeophysicalObservation != modeled surface unless labeled modeled
Geochemistry collection time != analytical report time
Borehole/WellLog/Core observations != public exact point release
MineralOccurrence observation != ResourceDeposit != ResourceEstimate
Structure observation != Hazards risk or alert
Hydrostratigraphic context != Hydrology measurement
```

Any observation envelope that would cause one of these collapses must return `DENY`, `ABSTAIN`, or `ERROR` instead of producing a public-ready claim.

---

## Lifecycle

| Phase | Observation handling |
|---|---|
| RAW | Source-native observation rows, logs, samples, reports, surveys, payloads, coordinates, and source terms remain source-bound. |
| WORK / QUARANTINE | Candidate observation is normalized, source-role checked, time-separated, geometry/sensitivity screened, method/artifact refs linked, and evidence-linked. |
| PROCESSED | Reviewed observation receives deterministic identity support, source refs, observed/source/valid/retrieval times, geometry posture, evidence refs, rights state, and correction posture. |
| CATALOG / TRIPLET | Claims may be projected only with source role, temporal support, EvidenceBundle refs, source caveats, and anti-collapse caveats preserved. |
| RELEASE CANDIDATE | Public derivative requires validation report, policy decision/review where material, redaction/aggregation/representation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released public-safe observation derivatives appear in public clients. |
| CORRECTED / WITHDRAWN / SUPERSEDED | Source update, evidence correction, method correction, time correction, geometry correction, sensitivity change, or identity merge/split triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `domain_observation.schema.json` beyond `id`, `version`, and `spec_hash`.
- [ ] Decide exact required fields for source role, target object family, observed/source/valid/retrieval/release/correction times, geometry posture, evidence refs, and sensitivity state.
- [ ] Verify or create `tools/validators/domains/geology/validate_domain_observation.py`.
- [ ] Add valid fixtures for field observation, geophysical observation, geochemistry sample observation, borehole observation, well-log observation, core observation, modeled observation support, aggregate observation, candidate record, synthetic record, and public derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, observed/modeled collapse, aggregate/per-place collapse, time collapse, missing EvidenceBundle, exact sensitive geometry public without receipt, LAS payload public without rights/release, candidate published, AI text used as evidence, and missing rollback target.
- [ ] Add tests proving public clients never consume RAW/WORK/QUARANTINE observation envelopes as public truth.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source correction, observation time correction, analytical report correction, geometry generalization, sensitivity update, evidence hash mismatch, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, role, evidence, time, geometry, policy, release, and rollback support all resolve | `ANSWER` / public-safe derivative may be shown |
| Evidence, source role, time, geometry, rights, sensitivity, or release support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, source role is collapsed, AI is used as evidence, or release is bypassed | `DENY` |
| Schema, validator, source-read, artifact-read, evidence lookup, hash, policy, or release failure occurs | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms this target file existed as a greenfield scaffold before replacement. | Does not prove contract maturity. |
| Confirmed paired schema stub | Confirms schema path, `$id`, `x-kfm` pointers, and current minimal fields. | Does not prove field-level validation or validator implementation. |
| Geology Identity Model | Confirms source-role meanings, six time dimensions, `spec_hash`, identity basis, and failure posture. | Field realizations remain PROPOSED / NEEDS VERIFICATION in that source. |
| Geology Object Families | Confirms observation-family purposes and sensitivity/source-role posture for geophysical observations and geochemistry samples, plus subsurface restrictions and resource anti-collapse. | Field realization remains PROPOSED. |
| Geology Scope | Confirms owned Geology object families and explicit non-ownership of Hydrology, Soil, Hazards, title/permit, and UI/AI truth. | Does not prove runtime enforcement. |
| Cross-domain Flora DomainObservation contract | Useful repo-local style/reference precedent for a domain observation envelope. | Flora semantics do not control Geology object meaning. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized `domain_observation` weakens source integrity, hides evidence gaps, collapses source roles or time dimensions, leaks restricted geometry/payloads, or makes an observation look more authoritative than its evidence/release state allows.

Rollback triggers include:

- schema field names or observation-envelope relationship are superseded by ADR/schema PR;
- source observation corrected, withdrawn, superseded, merged, or split;
- `observed_time`, `source_time`, `valid_time`, `retrieval_time`, `release_time`, or `correction_time` was collapsed or corrected;
- observed record was relabeled modeled, aggregate, regulatory, administrative, candidate, or synthetic without correction lineage;
- EvidenceRef cannot resolve to EvidenceBundle or hash mismatch occurs;
- exact sensitive geometry or rights-restricted payload entered a public derivative without receipt/release support;
- aggregate observation was joined as per-place truth;
- resource occurrence/deposit/estimate identities were collapsed;
- structure observation was treated as Hazards risk or alert;
- Hydrology, Soil, ownership/title, or UI/AI truth was absorbed into Geology observation truth;
- public API/UI/AI consumed RAW/WORK/QUARANTINE/candidate observation as authoritative truth.

Rollback artifacts should include affected observation IDs, source record IDs, target object-family refs, evidence refs, bundle refs, method refs, artifact digests, geometry refs, public derivative refs, policy decisions, receipts, validation reports, release refs, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `domain_observation.schema.json` beyond `id`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Should `domain_observation` be a generic support envelope only, or should it be materialized as a catalog/triplet object family? | NEEDS VERIFICATION | Domain/steward ADR. |
| What exact enum should be used for `observation_class` and `source_role`? | NEEDS VERIFICATION | Source-role schema and validator alignment. |
| Which observation types require separate custody/method/detection-limit fields? | NEEDS VERIFICATION | Geochemistry, core, well-log, and geophysics steward review. |
| What public-safe geometry roles are allowed by observation class? | NEEDS VERIFICATION | Policy/sensitivity fixture design. |
| How should observation envelopes route to multiple downstream objects without duplicating evidence or rotating identity incorrectly? | NEEDS VERIFICATION | Identity, graph/triplet, and EvidenceBundle design review. |
| How should MapLibre/Evidence Drawer/Focus Mode show observation support without implying release, policy, or AI truth? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/domain_feature_identity.md` — identity envelope and `spec_hash` support.
- `contracts/domains/geology/domain_layer_descriptor.md` — public/released layer profile; not observation truth.
- `contracts/domains/geology/GeophysicalObservation.md` — specialized geophysical observation contract.
- `contracts/domains/geology/GeochemistrySample.md` — specialized sample/analysis contract.
- `contracts/domains/geology/BoreholeReference.md` — subsurface point reference with restricted/generalized geometry posture.
- `contracts/domains/geology/WellLogReference.md` — well-log/LAS artifact reference.
- `contracts/domains/geology/CoreSample.md` — physical core/cuttings sample reference.
- `docs/domains/geology/IDENTITY_MODEL.md` — source-role, time, and identity doctrine.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference and observation-family semantics.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `schemas/contracts/v1/domains/geology/domain_observation.schema.json` — confirmed schema stub, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Expand paired schema with required observation-envelope fields.
- [ ] Verify or create validator and fixtures referenced by the schema `x-kfm` block.
- [ ] Add anti-collapse tests for observed/modeled, aggregate/per-place, administrative/observed, regulatory/observed, synthetic/observed, occurrence/deposit/estimate, structure/hazards, hydrostratigraphy/hydrology, and AI/evidence failures.
- [ ] Confirm EvidenceRef/EvidenceBundle lookup before catalog/triplet/public claims.
- [ ] Confirm public map/API/UI surfaces use only released public-safe observation derivatives through governed interfaces.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved observation/schema/source-role/geometry-policy drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
