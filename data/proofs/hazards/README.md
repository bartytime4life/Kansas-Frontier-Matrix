<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/proofs/hazards/readme
title: Hazards Proofs README
type: data-lifecycle-readme
version: v0.1
status: draft
owners: <PLACEHOLDER — Data steward · Hazards lane steward · Proof/release steward · Safety/policy reviewer>
created: 2026-06-25
updated: 2026-06-25
policy_label: internal-planning
intended_path: data/proofs/hazards/README.md
owning_root: data/
lifecycle_area: proofs
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/domains/hazards/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/settlements-infrastructure/README.md
  - data/receipts/hazards/README.md
  - data/catalog/README.md
  - data/published/hazards/README.md
  - release/manifests/hazards/README.md
  - schemas/contracts/v1/domains/hazards/
  - policy/domains/hazards/
  - policy/release/hazards/
tags: [kfm, data, proofs, hazards, evidence, validation, policy, release, rollback, not-for-life-safety, freshness, source-role]
notes:
  - "This README governs the hazards proof lane only; it is not itself a proof object, release decision, emergency alert, or publication manifest."
  - "Hazards outputs are planning and evidence context only. KFM must not operate as an emergency alerting, warning, regulatory determination, or life-safety instruction system."
  - "Implementation depth remains UNKNOWN until verified against the mounted repository, schemas, validators, fixtures, CI, emitted receipts, emitted proofs, and release manifests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Proofs

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success?style=flat-square)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-orange?style=flat-square)
![area](https://img.shields.io/badge/data%20area-proofs-blue?style=flat-square)
![domain](https://img.shields.io/badge/domain-hazards-red?style=flat-square)
![safety](https://img.shields.io/badge/not%20for-life--safety-critical?style=flat-square)
![publication](https://img.shields.io/badge/publication-not%20by%20file%20move-critical?style=flat-square)

> **One-line purpose.** `data/proofs/hazards/` stores machine-checkable proof objects that support hazards-domain evidence closure, source-role separation, freshness/expiry checks, policy decisions, catalog closure, release review, correction, and rollback — without turning KFM into an emergency alerting or life-safety instruction system.

---

## Mini table of contents

- [1. Scope](#1-scope)
- [2. Directory contract](#2-directory-contract)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Hazards proof responsibilities](#5-hazards-proof-responsibilities)
- [6. Expected object families](#6-expected-object-families)
- [7. Naming and identity](#7-naming-and-identity)
- [8. Minimum proof closure checklist](#8-minimum-proof-closure-checklist)
- [9. Hazards thin-slice proof pattern](#9-hazards-thin-slice-proof-pattern)
- [10. Safety, policy, and sensitivity posture](#10-safety-policy-and-sensitivity-posture)
- [11. Validation expectations](#11-validation-expectations)
- [12. Promotion, publication, and rollback](#12-promotion-publication-and-rollback)
- [13. Maintenance checklist](#13-maintenance-checklist)
- [14. Open verification backlog](#14-open-verification-backlog)

---

## 1. Scope

This directory is the hazards-domain lane under the KFM proof lifecycle area.

It exists to hold proof artifacts for claims and derived outputs involving historical hazard events, severe weather, flood context, wildfire and smoke context, drought indicators, earthquake events, heat/cold context, hail/wind/tornado records, disaster declarations, advisory and warning context, regulatory hazard areas, exposure summaries, resilience summaries, impact areas, and role-aware hazard timelines.

The proof lane supports review and publication decisions. It does **not** publish anything by itself.

### Life-safety boundary

KFM hazards outputs are evidence-backed context for planning, history, resilience, review, and explanation. They are **not** emergency alerts, warnings, evacuation instructions, rescue guidance, regulatory determinations, or authoritative life-safety instructions.

Any proof artifact that touches operational warning or advisory material must preserve this boundary by recording freshness, expiry, source authority, retrieval time, release time, official-source referral behavior, and a `not_for_life_safety` policy/disclaimer check.

### Truth posture

| Statement | Status |
|---|---:|
| `data/proofs/hazards/` is the intended home for hazards proof artifacts. | **PROPOSED** until verified against the mounted repo and Directory Rules version in force. |
| Hazards proofs must remain downstream of source descriptors, evidence records, validation, policy, review state, and release state. | **CONFIRMED doctrine / PROPOSED lane application**. |
| Hazards public surfaces must keep planning/context outputs distinct from emergency alerting and regulatory authority. | **CONFIRMED doctrine / PROPOSED implementation control**. |
| Existing hazards proof schemas, validators, CI jobs, fixtures, and emitted proof packs are present. | **UNKNOWN** until inspected in a mounted checkout. |

---

## 2. Directory contract

`data/proofs/hazards/` is a responsibility-rooted lane, not a topic bucket.

It answers to:

- the `data/` lifecycle root;
- the `proofs/` lifecycle area;
- the hazards domain lane;
- evidence, validation, policy, release, correction, and rollback governance;
- the KFM rule that promotion is a governed state transition, not a file move;
- the hazards rule that operational context is not a life-safety alert.

### Contract summary

| Field | Value |
|---|---|
| Root owner | `data/` lifecycle stewardship |
| Area owner | Proof / release support stewardship |
| Domain lane | Hazards |
| Public exposure | None by direct file path |
| Normal public path | Governed API → released artifact / catalog / EvidenceBundle projection / policy-filtered hazards view |
| Adjacent lifecycle roots | `data/receipts/`, `data/catalog/`, `data/published/`, `release/` |
| Required public label | Planning/context only; not emergency alerting; not regulatory determination unless a released regulatory source explicitly supports that limited context |
| Forbidden shortcut | Direct UI, API, model, or map access to this folder as public truth |

---

## 3. What belongs here

Store proof objects that can be independently inspected, validated, hashed, compared, cited by a release decision, and used for correction or rollback review.

Examples include:

| Proof artifact | Purpose | Status |
|---|---|---:|
| `proofpack.<hazards_object_id>.<run_id>.json` | Bundled proof closure for one hazard object, candidate layer, analytical summary, or release candidate. | **PROPOSED** |
| `validation-proof.<run_id>.json` | Shows schema, geometry, CRS, temporal, freshness, expiry, and source-reference validation outcomes. | **PROPOSED** |
| `policy-proof.<run_id>.json` | Records rights, sensitivity, source-role, release-state, access, and not-for-life-safety checks. | **PROPOSED** |
| `source-role-proof.<object_id>.json` | Confirms observation, model, regulatory, operational context, report, and summary roles are not collapsed. | **PROPOSED** |
| `freshness-expiry-proof.<object_id>.json` | Confirms issue time, valid time, expiry time, retrieval time, stale-state behavior, and release-time interpretation. | **PROPOSED** |
| `evidence-closure-proof.<evidence_bundle_id>.json` | Confirms every material hazard claim has resolvable evidence support. | **PROPOSED** |
| `life-safety-boundary-proof.<artifact_id>.json` | Confirms the artifact cannot be represented as an emergency alert or instruction surface. | **PROPOSED** |
| `official-referral-proof.<artifact_id>.json` | Confirms public hazard surfaces route urgent needs to official emergency/weather authorities instead of KFM advice. | **PROPOSED** |
| `catalog-closure-proof.<catalog_record_id>.json` | Confirms catalog, provenance, citation, digest, and source-role closure before release review. | **PROPOSED** |
| `public-safe-geometry-proof.<artifact_id>.json` | Documents generalization, suppression, precision degradation, or withheld infrastructure/sensitive geometry. | **PROPOSED** |
| `exposure-summary-proof.<summary_id>.json` | Confirms exposure/resilience summaries preserve underlying source roles and avoid exact sensitive asset leakage. | **PROPOSED** |
| `rollback-proof.<release_candidate_id>.json` | Confirms a rollback target exists and is sufficient before release. | **PROPOSED** |

Proof objects should be small, structured, deterministic where practical, and reproducible from the referenced inputs.

---

## 4. What does not belong here

Do **not** store these in `data/proofs/hazards/`:

| Do not store | Correct home | Reason |
|---|---|---|
| Raw NOAA, NWS, FEMA, USGS, wildfire, smoke, drought, state/local emergency, or source API payloads | `data/raw/hazards/` or `data/raw/<source-family>/` | Raw material must remain in the RAW lifecycle area. |
| Live warning feeds, alert streams, or operational dashboards | Connector/runtime/source-specific areas, with no public path unless separately governed | Proofs may snapshot and prove context; they are not live alert feeds. |
| Work-in-progress transforms or failed normalization outputs | `data/work/hazards/` or `data/quarantine/hazards/` | Proofs cite work; they are not the work surface. |
| Validated processed hazard objects | `data/processed/hazards/` | Processed objects are source-derived records, not proof records. |
| STAC, DCAT, PROV, or other catalog records | `data/catalog/` | Catalog records have their own lifecycle responsibility. |
| Runtime receipts | `data/receipts/hazards/` | Receipts record runs/actions; proofs support closure and decisions. |
| Release manifests, promotion decisions, rollback cards, or correction notices | `release/` | Release authority belongs to the release responsibility root. |
| Public PMTiles, GeoParquet, GeoJSON, COG, raster, vector, or API payload exports | `data/published/hazards/` | Published artifacts are the released delivery surface. |
| Policy rules | `policy/domains/hazards/`, `policy/release/hazards/`, or related policy roots | Policy authority does not live inside proof data. |
| Schemas | `schemas/contracts/v1/domains/hazards/` or applicable cross-cutting schema roots | Schema authority belongs under the schema root. |
| Tests or fixtures | `tests/` and `fixtures/` | Test evidence belongs in test/fixture roots, not in lifecycle data. |
| Public instructions such as “take shelter now” or “evacuate here” | Not a KFM artifact | KFM must refer life-safety action to official authorities. |

---

## 5. Hazards proof responsibilities

Hazards proofs should answer these questions before a hazard artifact can support a public or semi-public claim:

1. **Source support:** Which source descriptors support this hazard object or derived artifact?
2. **Source-role support:** Is the artifact an observation, model field, regulatory archive, warning/advisory context, historical event, public report, remote-sensing detection, resilience summary, or exposure summary?
3. **Evidence closure:** Which EvidenceBundle supports each material claim?
4. **Spatial support:** What geometry, CRS, scale, resolution, uncertainty, and generalization rules apply?
5. **Temporal support:** What event, issue, valid, expiry, source, retrieval, release, correction, and stale-state times matter?
6. **Policy support:** Are rights, terms, sensitivity, source role, operational context, official-referral, and review requirements satisfied?
7. **Life-safety boundary:** Does the artifact clearly refuse alerting, warning, evacuation, emergency-response, or real-time instruction behavior?
8. **Validation support:** Which validators passed, failed, abstained, denied, or require review?
9. **Release support:** Which release candidate or manifest cites this proof?
10. **Correction support:** What stale-state, correction, supersession, and rollback path exists?

A proof object should be rejected if it cannot identify the source, evidence, role, time basis, policy, validation, and release context it is meant to support.

---

## 6. Expected object families

Hazards proof objects may support, but do not replace, these hazards-domain object families:

| Hazards object family | Proof concern |
|---|---|
| `HazardEvent` | Event identity, source support, geometry/time basis, severity vocabulary, citation, uncertainty. |
| `HazardObservation` | Observed vs modeled distinction, station/sensor/source role, retrieval time, quality flags. |
| `WarningContext` | Issue/valid/expiry times, official source, not-for-life-safety label, stale-state handling. |
| `AdvisoryContext` | Advisory role, source authority, time window, disclaimer, official-referral behavior. |
| `DisasterDeclaration` | Declaration authority, jurisdiction, date scope, regulatory/legal context, non-collapse with event truth. |
| `FloodContext` | NFHL/regulatory context, hydrology relation, flood-event distinction, scale and effective date. |
| `WildfireDetection` | Remote-sensing detection role, confidence, temporal lag, smoke/fire distinction, public-safe geometry. |
| `SmokeContext` | Observation/model/source role, air-lane dependency, freshness, health-advice boundary. |
| `DroughtIndicator` | Indicator source, class/version, time window, aggregation scale, agriculture/hydrology relation. |
| `EarthquakeEvent` | Event source, magnitude/depth uncertainty, time basis, geometry precision, source update state. |
| `HeatColdEvent` | Observation/model/advisory role, atmospheric relation, time scope, public guidance boundary. |
| `ExposureSummary` | Cross-lane joins, infrastructure sensitivity, aggregation/generalization, no exact sensitive leakage. |
| `ResilienceSummary` | Assumption surface, scenario limits, source role preservation, planning-not-authority label. |
| `HazardTimeline` | Role-aware time ordering, event/update/stale/release separation, supersession handling. |
| `ImpactArea` | Geometry derivation, confidence, source role, public-safe transforms, rollback/correction path. |
| `RegulatoryHazardArea` | Source authority, effective date, legal context, update cadence, not a KFM determination. |
| `RemoteSensingDetection` | Product lineage, processing level, confidence, false-positive limits, temporal lag. |

When a proof references hydrology, atmosphere/air, roads/rail, settlements/infrastructure, agriculture, geology, or other evidence, it must preserve the owning lane and should not collapse those claims into hazards authority.

---

## 7. Naming and identity

Use names that are deterministic enough to diff and inspect.

Recommended pattern:

```text
<proof_family>.<domain>.<stable_object_or_candidate_id>.<run_id>.json
```

Examples:

```text
proofpack.hazards.hazard_event_noaa_storm_demo.run_20260625T000000Z.json
validation-proof.hazards.flood_context_nfhl_demo.run_20260625T000000Z.json
source-role-proof.hazards.warning_context_demo_expired.run_20260625T000000Z.json
freshness-expiry-proof.hazards.warning_context_demo_expired.run_20260625T000000Z.json
life-safety-boundary-proof.hazards.hazard_layer_demo.run_20260625T000000Z.json
official-referral-proof.hazards.hazard_layer_demo.run_20260625T000000Z.json
catalog-closure-proof.hazards.layer_candidate_demo.run_20260625T000000Z.json
public-safe-geometry-proof.hazards.exposure_summary_demo.run_20260625T000000Z.json
rollback-proof.hazards.release_candidate_demo.run_20260625T000000Z.json
```

### Identity guidance

A proof record should carry, at minimum:

- `proof_id`
- `proof_family`
- `domain`
- `object_id` or `release_candidate_id`
- `run_id`
- `source_descriptor_ids`
- `source_roles`
- `evidence_bundle_ids`
- `policy_decision_ids`
- `validation_report_ids`
- `receipt_ids`
- `catalog_record_ids`
- `release_manifest_ids` when applicable
- `input_digests`
- `output_digests`
- `spec_hash`
- `created_at`
- `event_time`, `valid_time`, `issue_time`, `expiry_time`, `retrieval_time`, `release_time`, and `correction_time` where material
- `freshness_state`
- `not_for_life_safety`
- `official_source_referral`
- `review_state`
- `status`

Use stable IDs and digests instead of human names wherever the proof must be reproducible.

---

## 8. Minimum proof closure checklist

A hazards proof is not ready to support release review unless all applicable checks are satisfied or explicitly recorded as blocked.

| Check | Required evidence | Failure posture |
|---|---|---:|
| Source descriptor exists | `SourceDescriptor` with role, rights, cadence, sensitivity, time basis, and source authority. | **DENY / QUARANTINE** |
| Evidence resolves | EvidenceRef resolves to EvidenceBundle for every material claim. | **ABSTAIN / DENY** |
| Source roles are distinct | Observation/model/regulatory/warning/advisory/report/summary roles are explicitly labeled. | **DENY** |
| Temporal support exists | Event, valid, issue, expiry, source, retrieval, release, stale, and correction times are recorded where material. | **ABSTAIN / DENY** |
| Operational context is bounded | Warning/advisory context has expiry, freshness, official-source link, and not-for-life-safety label. | **DENY** |
| Geometry is valid | Geometry, CRS, scale, uncertainty, and transform digest validate. | **ABSTAIN / DENY** |
| Sensitive joins are safe | Infrastructure, roads, settlements, health, or other sensitive joins have access class, transform receipt, and review state. | **DENY** |
| Policy decision exists | Rights, sensitivity, source role, release state, access role, and official-referral policy checks passed. | **DENY** |
| Catalog closure exists | Catalog/provenance/citation/digest closure is complete before release review. | **ABSTAIN / DENY** |
| Release reference exists | Release candidate or manifest cites the proof before public exposure. | **DENY** |
| Rollback path exists | Rollback target and stale/correction path are identified. | **DENY** |

---

## 9. Hazards thin-slice proof pattern

Recommended first proof slice:

> Historical flood or severe-weather event fixture plus NFHL or official hazard-area context and an exposure summary, with live warning feeds disabled or represented only as contextual, expired, fixture-bound examples.

### Thin-slice files this directory may eventually cite

| Artifact | Likely home | Proof role |
|---|---|---|
| Synthetic or public-safe source descriptor | `data/registry/` or source registry lane | Identifies source role, rights, cadence, authority, and sensitivity. |
| Raw source snapshot | `data/raw/hazards/` | Immutable source payload or source reference. |
| Normalized hazard fixture | `data/processed/hazards/` | Validated event/context object. |
| Evidence bundle | `data/catalog/` or evidence lifecycle lane as adopted by repo rules | Supports inspectable claims. |
| Layer manifest | `data/catalog/` / release-adjacent manifest lane | Defines map delivery and trust state. |
| Runtime receipt | `data/receipts/hazards/` | Records validator, compiler, or release dry-run execution. |
| Proof pack | `data/proofs/hazards/` | Proves closure for release review. |
| Release manifest | `release/` | Publishes or denies release through governed state transition. |
| Published artifact | `data/published/hazards/` | Released public-safe delivery artifact only after promotion. |

### Thin-slice acceptance criteria

- No live emergency alerts are exposed as current KFM instructions.
- Every feature click can resolve to evidence, source role, time scope, policy state, and release state.
- Expired or stale operational context is labeled as expired/stale, not current.
- The Evidence Drawer states planning/context posture and official-source referral behavior.
- Focus Mode can only answer through finite outcomes: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
- Public geometry is generalized or withheld where sensitivity, infrastructure exposure, or misuse risk requires it.
- Release can be dry-run and rolled back.

---

## 10. Safety, policy, and sensitivity posture

Hazards proofs are high-consequence even when source data is public.

### Required safety rules

| Rule | Meaning |
|---|---|
| Not emergency alerting | KFM hazards outputs do not warn, dispatch, evacuate, shelter, rescue, or instruct. |
| Official referral | Public surfaces should point urgent life-safety users to official emergency/weather authorities. |
| Source-role anti-collapse | Historical, regulatory, observational, modeled, advisory, warning, report, and summary records are not interchangeable. |
| Freshness and expiry | Operational context must record issue, valid, expiry, retrieval, release, stale, and correction times where material. |
| Public-safe geometry | Sensitive infrastructure, facility, response, or precise exposure details require review, redaction, aggregation, or denial. |
| Default-deny release | Missing rights, missing evidence, unresolved source role, unresolved sensitivity, or absent release state blocks public promotion. |
| AI is downstream | AI may summarize released EvidenceBundles and limitations; it may not create hazard truth or life-safety instructions. |

### Sensitivity notes

Historical hazard events may be low sensitivity when already public and properly cited. Sensitivity increases when hazards are joined to precise infrastructure, critical facilities, health, private property, emergency operations, response capability, or living-person information.

Where sensitivity is unclear, use `DENY`, `ABSTAIN`, `QUARANTINE`, redaction, aggregation, staged access, or steward review. Do not publish first and repair later.

---

## 11. Validation expectations

Hazards proof validators should include both generic KFM proof checks and hazards-specific safety checks.

| Validator family | Required behavior | Status |
|---|---|---:|
| Schema validation | Proof object conforms to the adopted proof schema. | **PROPOSED** |
| Source descriptor validation | Every source has identity, role, rights, cadence, and sensitivity metadata. | **PROPOSED** |
| Evidence closure validation | Every material claim resolves to EvidenceBundle support. | **PROPOSED** |
| Source-role anti-collapse validation | Observation, model, regulatory, warning/advisory context, and summary roles remain distinct. | **PROPOSED** |
| Temporal validation | Event, issue, valid, expiry, retrieval, release, correction, and stale-state times are coherent. | **PROPOSED** |
| Freshness/expiry validation | Operational context cannot appear as current after expiry or stale threshold. | **PROPOSED** |
| Life-safety boundary validation | Hazard output cannot be interpreted as emergency instruction, active warning authority, or regulatory determination. | **PROPOSED** |
| Official-referral validation | Urgent/public hazard contexts provide official-source referral behavior where applicable. | **PROPOSED** |
| Geometry validation | Geometry validity, CRS, scale, transform digest, and uncertainty validate. | **PROPOSED** |
| Public-safe exposure validation | Sensitive joins and infrastructure exposure require access class, transform receipt, reviewer, and release gate. | **PROPOSED** |
| Catalog closure validation | Catalog/provenance/citation/digest closure is complete before release review. | **PROPOSED** |
| UI disclaimer validation | Evidence Drawer and layer summaries carry planning/context-not-alerting labels. | **PROPOSED** |
| Rollback validation | Release candidate has rollback target and correction path. | **PROPOSED** |
| No-direct-source validation | Public UI/API/AI cannot read from RAW, WORK, QUARANTINE, or proof files directly. | **PROPOSED** |

### Finite validator outcomes

Validators should emit finite outcomes:

```text
PASS
WARN
ABSTAIN
DENY
ERROR
```

A proof with `DENY` or unresolved `ERROR` must not support public release.

---

## 12. Promotion, publication, and rollback

A proof file in this directory is never publication.

Publication requires a governed state transition through the release process. A release decision must cite the relevant proof IDs, EvidenceBundles, validation reports, policy decisions, receipts, catalog records, and rollback target.

### Promotion guardrails

| Guardrail | Requirement |
|---|---|
| Proof before release | Release manifests cite proof objects; proof objects do not self-publish. |
| Catalog before public artifact | Public artifacts require catalog/provenance/citation/digest closure. |
| Policy before exposure | Rights, sensitivity, source role, release state, access role, and safety policy pass before public access. |
| Rollback before release | Rollback target exists before public release. |
| Stale-state before current display | Hazard layers with time-sensitive operational context expose freshness/stale/expiry state. |
| Review before sensitive joins | Infrastructure, health, emergency operations, property, or living-person joins require explicit review state. |
| Correction after discovery | Corrections create new records, receipts, proofs, and release decisions; do not silently overwrite prior proof lineage. |

### Rollback triggers

Rollback or withdrawal is required when:

- evidence is found to be wrong, missing, or mis-cited;
- source rights or redistribution terms are unresolved;
- source role was collapsed or mislabeled;
- an expired warning/advisory context was displayed as current;
- a public surface implied emergency-alert authority or life-safety instruction;
- sensitive infrastructure or precise exposure detail leaked;
- release manifest, catalog closure, or proof digest fails validation;
- a correction notice supersedes the published artifact.

---

## 13. Maintenance checklist

Use this checklist when adding or reviewing files in `data/proofs/hazards/`.

- [ ] File is a proof object, not a raw payload, receipt, catalog, release manifest, policy, schema, fixture, or public artifact.
- [ ] File name includes proof family, hazards domain, stable object or candidate ID, and run ID.
- [ ] Proof references source descriptors and EvidenceBundles.
- [ ] Proof records source role and knowledge character.
- [ ] Proof records all material times, including freshness and expiry where applicable.
- [ ] Proof records `not_for_life_safety` behavior where operational context is involved.
- [ ] Proof records official-source referral behavior when public hazard context could be confused with current guidance.
- [ ] Proof records policy decisions and validation reports.
- [ ] Proof records input and output digests.
- [ ] Proof records review state and release candidate references where applicable.
- [ ] Proof records rollback and correction path where applicable.
- [ ] Sensitive or cross-lane joins include public-safe geometry or aggregation proof.
- [ ] No public UI/API/AI path reads this file directly as truth.

---

## 14. Open verification backlog

| Item | Status | Evidence needed to close |
|---|---:|---|
| Verify `data/proofs/hazards/` exists in the mounted repo. | **NEEDS VERIFICATION** | Mounted checkout, tree listing, or accepted PR. |
| Verify hazards proof schema home. | **NEEDS VERIFICATION** | Adopted schema path under `schemas/contracts/v1/...` and ADR/schema-home evidence. |
| Verify hazards source-role taxonomy. | **NEEDS VERIFICATION** | Contract/schema/policy docs defining observation/model/regulatory/warning/advisory/report/summary roles. |
| Verify freshness and expiry policy. | **NEEDS VERIFICATION** | Policy files, fixtures, and validator reports for operational context. |
| Verify not-for-life-safety enforcement. | **NEEDS VERIFICATION** | Policy tests, UI tests, Evidence Drawer tests, Focus Mode runtime fixtures. |
| Verify official-source referral behavior. | **NEEDS VERIFICATION** | UI/API/runtime fixtures and review guidance. |
| Verify sensitive exposure classes for infrastructure and critical assets. | **NEEDS VERIFICATION** | Sensitivity policy, access roles, transform receipts, reviewer signoff. |
| Verify proof/receipt/catalog/release separation. | **NEEDS VERIFICATION** | Directory scan, validators, CI checks, and release dry-run artifacts. |
| Verify rollback drill. | **NEEDS VERIFICATION** | ReleaseManifest, RollbackCard, rollback-proof, correction fixture, and CI/report output. |

---

## Closing rule

Hazards proofs help KFM say what is supported, current, stale, contextual, restricted, denied, or corrected. They must never make a hazard surface look more authoritative, current, precise, or operational than the evidence, source role, policy, review state, and release state allow.
