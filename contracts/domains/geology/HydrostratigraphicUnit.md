<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-hydrostratigraphic-unit
title: HydrostratigraphicUnit Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Hydrostratigraphy steward
  - OWNER_TBD — Hydrology liaison
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; hydrostratigraphic-unit; geology-hydrology-bridge; context-only; source-role-aware; release-gated
tags: [kfm, contracts, geology, HydrostratigraphicUnit, hydrostratigraphy, hydrology-bridge, aquifer-context, geologic-unit, stratigraphic-interval, lithology, evidence, source-role, policy, release, correction, rollback]
related:
  - ./README.md
  - ./GeologicUnit.md
  - ./StratigraphicInterval.md
  - ./Lithology.md
  - ./BoreholeReference.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/HydrostratigraphicUnit.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology HydrostratigraphicUnit semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/HydrostratigraphicUnit.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "Object-family docs explicitly leave the schema home open: geology lane vs a neutral hydrostratigraphy home requires Hydrology co-signoff."
  - "HydrostratigraphicUnit is a geology↔hydrology bridge/context object. It cites Hydrology where appropriate, but it owns no Hydrology measurements, gauges, flows, water levels, or water-quality truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# HydrostratigraphicUnit — Geology

> Semantic contract for Geology `HydrostratigraphicUnit`: the evidence-bound bridge object for geology-controlled hydrostratigraphic context, lithologic/stratigraphic controls on aquifer behavior, public-safe derivatives, correction, and rollback — without absorbing Hydrology measurement truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: HydrostratigraphicUnit" src="https://img.shields.io/badge/object-HydrostratigraphicUnit-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: context not measurement" src="https://img.shields.io/badge/boundary-context__not__measurement-critical">
</p>

`contracts/domains/geology/HydrostratigraphicUnit.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Unit classes](#unit-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/HydrostratigraphicUnit.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/HydrostratigraphicUnit.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Hydrostratigraphic Unit` as the geology↔hydrology bridge object and states that it is context, not measurement. The object-family reference places `HydrostratigraphicUnit` in the lineage/cross-lane group and explicitly marks its schema home as open: geology lane vs neutral `hydrostratigraphy/`. Field-level schema shape, fixtures, validators, source registry records, Hydrology co-signoff, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `HydrostratigraphicUnit` supplies geology-controlled hydrostratigraphic context. It does **not** own Hydrology measurements, gauges, flow, water levels, water quality, aquifer-test results, water rights, hazards risk, public health advice, or AI/UI truth.

---

## Meaning

`HydrostratigraphicUnit` is the Geology semantic object for a geologic unit, interval, assemblage, or interpreted body described by its hydrostratigraphic role — for example, an aquifer, aquitard, confining unit, permeable interval, leaky unit, or source-native hydrostratigraphic label.

It answers:

- Which geology-controlled hydrostratigraphic unit or context is being asserted?
- Which geologic units, surficial units, lithology, stratigraphic intervals, boreholes, well logs, core samples, geophysics, and source records support it?
- Which Hydrology objects may be cited as related evidence or downstream context without becoming Geology-owned measurements?
- What source role, source time, valid time, retrieval time, release time, and correction time govern the claim?
- What public-safe unit label, geometry, or summary may be shown?
- Which validation report, policy decision where material, review record, release manifest, correction notice, and rollback target govern downstream use?

A hydrostratigraphic unit can bridge geology and hydrology. The bridge is not a license to collapse the two domains.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Hydrostratigraphic meaning | `contracts/domains/geology/HydrostratigraphicUnit.md` | Owned here as a draft Geology bridge contract |
| Machine schema shape | `schemas/contracts/v1/domains/geology/HydrostratigraphicUnit.schema.json` or accepted neutral home | NEEDS VERIFICATION; exact geology path not found |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms bridge object and Hydrology boundary |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Places object in lineage/cross-lane group and flags schema-home question |
| Geologic-unit support | `contracts/domains/geology/GeologicUnit.md` | Unit identity and mapped geology support |
| Stratigraphy/lithology support | `contracts/domains/geology/StratigraphicInterval.md`, `contracts/domains/geology/Lithology.md` | Geological controls and material context; companion files may need verification |
| Borehole/log/sample support | `contracts/domains/geology/BoreholeReference.md`, well-log/core-sample contracts | Subsurface evidence; restricted details remain governed |
| Hydrology references | Hydrology-owned roots, paths NEED VERIFICATION | Measurements and water-system truth remain Hydrology-owned |
| Source registry | `data/registry/sources/geology/` and Hydrology source registries where applicable | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, Hydrology policy as applicable | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, cross-lane, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/HydrostratigraphicUnit.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/HydrostratigraphicUnit.schema.json` |
| Exact schema result | Not found in this session |
| Object-family posture | `HydrostratigraphicUnit` appears in §B and object-family quick reference |
| Schema-home drift | Object-family backlog asks whether schema home is Geology or neutral `hydrostratigraphy/` co-signed with Hydrology |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema-home decision is resolved, this contract is semantic guidance only.

---

## Assertions

A reviewed `HydrostratigraphicUnit` should semantically assert:

1. **Unit identity** — deterministic identity for the hydrostratigraphic unit, source, object role, temporal scope, and normalized digest.
2. **Geology support** — linked GeologicUnit, SurficialUnit, Lithology, StratigraphicInterval, GeologicAge, boundary version, borehole, well-log, core-sample, or geophysical evidence.
3. **Hydrology relationship** — related Hydrology objects may be cited, but measurement ownership remains Hydrology.
4. **Hydrostratigraphic role** — aquifer, aquitard, confining unit, leaky unit, permeable interval, recharge-relevant unit, discharge-relevant unit, source-native class, or model-context class.
5. **Geometry and scale** — polygon/volume/interval/extent/footprint, geometry precision, CRS, scale, and public-safe representation.
6. **Interpretation basis** — source map, report, borehole/log evidence, measured section, geophysics, hydrologic context, method, confidence, and caveats.
7. **Temporal discipline** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
8. **Sensitivity posture** — exact subsurface, private-well-adjacent, infrastructure-adjacent, rights-limited, generalized, public-safe, or withheld state.
9. **Release posture** — public derivative, validation report, policy decision where material, review record, release manifest, correction path, and rollback target.
10. **Cross-lane boundary** — Hydrology, Hazards, Soil, People/Land, and UI/AI claims remain separate authority classes.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating hydrostratigraphy as water-level measurement | Hydrology owns measurements. Geology supplies context only. |
| Treating hydrostratigraphy as water-quality truth | Hydrology owns water-quality observations and claims. |
| Treating hydrostratigraphy as aquifer-test result | Aquifer tests and hydraulic measurements remain Hydrology-owned unless a cross-lane ADR says otherwise. |
| Treating a hydrostratigraphic unit as a mapped geologic unit | It may reference GeologicUnit/SurficialUnit, but it is a bridge interpretation. |
| Treating a hydrostratigraphic unit as hazards risk | Hazards owns risk; Geology may supply context. |
| Treating it as ownership or water-right proof | People/Land or water-right/legal systems own those claims. |
| Treating public generalized geometry as exact subsurface geometry | Public-safe geometry is a derivative with caveats. |
| Treating AI/UI summary as domain truth | Generated language and UI views are downstream carriers only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM hydrostratigraphic-unit identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology` unless an ADR creates a neutral hydrostratigraphy home. |
| `object_family` | `HydrostratigraphicUnit`. |
| `unit_class` | Aquifer, aquitard, confining unit, leaky unit, permeable interval, source-native class, modeled class, candidate, or public derivative. |
| `unit_name` | Public-safe hydrostratigraphic unit label. |
| `source_unit_name` | Source-native label retained for audit. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native map, report, unit, interval, table, or dataset record. |
| `geologic_unit_refs` | Linked GeologicUnit refs. |
| `surficial_unit_refs` | Linked SurficialUnit refs where applicable. |
| `lithology_refs` | Linked lithology/material descriptors. |
| `stratigraphic_interval_refs` | Linked StratigraphicInterval refs. |
| `geologic_age_refs` | Linked GeologicAge refs. |
| `boundary_version_refs` | Linked GeologyBoundaryVersion refs. |
| `borehole_refs` | Linked BoreholeReference evidence, with sensitivity posture preserved. |
| `well_log_refs` | Linked well-log evidence, with rights/source restrictions preserved. |
| `core_sample_refs` | Linked CoreSample evidence. |
| `geophysical_observation_refs` | Linked GeophysicalObservation evidence. |
| `hydrology_context_refs` | Hydrology-owned measurement/model/context refs cited without taking ownership. |
| `geometry_ref` | Internal geometry/extent/volume/interval reference. |
| `public_geometry_ref` | Public-safe generalized or aggregate geometry ref, if released. |
| `geometry_fingerprint` | Stable geometry fingerprint for identity and drift detection. |
| `crs` | Coordinate reference system / projection metadata. |
| `vertical_extent` | Depth/elevation/stratigraphic interval support, where available. |
| `hydraulic_role_summary` | Public-safe summary of hydrostratigraphic role, not a measurement. |
| `interpretation_version` | Source or KFM interpretation/model version. |
| `uncertainty_summary` | Confidence, gaps, disagreement, scale limits, and interpretation caveats. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Observation/acquisition time for supporting evidence, where material. |
| `valid_time` | Time interval the hydrostratigraphic interpretation claims to represent. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, or unknown. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Public-safe, generalized, restricted, subsurface-sensitive, rights-limited, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release where material. |
| `review_record_ref` | Source, geology, hydrology-liaison, sensitivity, interpretation, or release review. |
| `validation_report_ref` | Validation report for schema, source-role, geometry, cross-lane references, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, unit rename, boundary correction, interpretation supersession, rights update, and rollback lineage. |
| `quality_flags` | Source-role conflict, Hydrology ownership ambiguity, geometry missing, vertical extent missing, rights unknown, sensitivity unknown, stale source, or incomplete evidence. |

---

## Unit classes

| Class | Meaning | Default posture |
|---|---|---|
| `aquifer_context` | Geological body described as aquifer context. | Public-safe when generalized and caveated; measurements remain Hydrology-owned. |
| `aquitard_context` | Low-permeability or confining geology context. | Public-safe when source/scale allow. |
| `confining_unit` | Confining layer/unit context. | Interpretation-bound; uncertainty and source support required. |
| `leaky_unit` | Transitional or partly confining unit. | Method and caveats required. |
| `permeable_interval` | Interval described by permeability or transmissive character. | Context only unless Hydrology owns measured values. |
| `source_native_class` | Source-native hydrostratigraphic label not yet normalized. | Preserve source label and normalization state. |
| `model_context` | Model-derived hydrostratigraphic unit/context. | Modeled, not observed; version and uncertainty required. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `public_derivative` | Released public-safe geometry/label/summary. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | HydrostratigraphicUnit posture |
|---|---|---|
| Geologic map/report assigning aquifer/aquitard context | `observed` or `aggregate` with interpretation caveat | Geology-context evidence; preserve source scale and caveats. |
| Borehole/log/core support for unit role | `observed` | Evidence-bearing support; exact subsurface restrictions preserved. |
| Regional hydrostratigraphic framework or compiled report | `aggregate` | Compiled framework; preserve source version and scale. |
| Groundwater model layer or interpolated hydrostratigraphic surface | `modeled` | Model output; never label as observed measurement. |
| Hydrology gauge/well measurement dataset | Hydrology-owned source role | May be cited only as Hydrology context; Geology does not restate measurements. |
| Unreviewed import, ambiguous aquifer label, unresolved cross-lane ref | `candidate` | Quarantine until identity, role, source, and ownership resolve. |
| AI-generated or hypothetical hydrostratigraphic label | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`HydrostratigraphicUnit` is a bridge object, not a takeover object.

```text
HydrostratigraphicUnit != Hydrology measurement
HydrostratigraphicUnit != water level
HydrostratigraphicUnit != water quality observation
HydrostratigraphicUnit != flow / gauge record
HydrostratigraphicUnit != aquifer-test result
HydrostratigraphicUnit != GeologicUnit
HydrostratigraphicUnit != Hazards risk
HydrostratigraphicUnit != water right / ownership / title proof
HydrostratigraphicUnit != public alert
HydrostratigraphicUnit != AI summary
```

Any linkage to Hydrology must preserve owning lane, source role, evidence, time, uncertainty, policy state, release state, and correction lineage.

---

## Sensitivity and release

Hydrostratigraphic context is often public-safe at generalized unit scale when source rights allow, but exact subsurface evidence, private-well-adjacent records, model layers, rights-limited reports, and water-system interpretations can require review or restriction.

Rules:

- A hydrostratigraphic unit is not automatically a public layer.
- Public derivatives require validation, source rights, policy/review where material, release manifest, correction path, and rollback target.
- Exact subsurface inputs remain governed and may require redaction/generalization.
- Hydrology measurements referenced by this object must stay Hydrology-owned and citation-bound.
- Public outputs must preserve source role, source time, valid time, interpretation/model version, geometry precision, uncertainty, and caveats.
- Candidate, synthetic, rights-unknown, ownership-ambiguous, stale, or evidence-incomplete records must not enter public outputs as authoritative unit facts.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native hydrostratigraphic labels, model layers, maps, borehole/log/core evidence, reports, and Hydrology references remain source-bound. |
| WORK / QUARANTINE | Candidate units are normalized, source-role checked, cross-lane ownership checked, rights/sensitivity-screened, geometry/vertical extent checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, source support, geometry/extent support, Hydrology-context references, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, source time, valid time, evidence, geometry/vertical precision, owning-lane boundaries, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy/review where material, release manifest, and rollback target. |
| PUBLISHED | Only released public-safe hydrostratigraphic context layers, labels, graph claims, or API/UI payloads appear in public clients. |
| CORRECTION | Source update, unit rename, cross-lane ownership correction, model revision, geometry correction, Hydrology reference correction, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve schema home: `schemas/contracts/v1/domains/geology/` vs neutral `hydrostratigraphy/` co-signed by Hydrology.
- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for aquifer context, aquitard context, confining unit, leaky unit, permeable interval, source-native class, model context, candidate record, and public derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, missing geometry/extent, Hydrology measurement copied into Geology, aquifer test treated as Geology-owned, water-quality value embedded as unit truth, public exact private-well-derived geometry, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source keys, source role, bound geology refs, Hydrology context refs, geometry/vertical extent, model version, uncertainty, evidence refs, release refs, and correction refs.
- [ ] Add cross-lane policy tests proving Hydrology measurements remain Hydrology-owned and public clients consume released derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, Hydrology reference correction, model revision, unit rename, geometry repair, rights update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, cross-lane ownership is clear, geometry validates, derivative is released | `ANSWER` / public-safe hydrostratigraphic context may be shown |
| Evidence, source role, geometry, Hydrology ownership, rights, model version, or release state is incomplete | `ABSTAIN` |
| Claim would restate Hydrology measurement as Geology truth, expose restricted detail, bypass release, or imply risk/legal advice | `DENY` |
| Schema, validator, source-read, cross-lane resolution, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Hydrostratigraphic Unit is the geology↔hydrology bridge object and explicitly says Geology does not own Hydrology measurements. | Does not prove schema or implementation enforcement. |
| Geology object-family map | Places `HydrostratigraphicUnit` in lineage/cross-lane group and shows it cites Hydrology while owning nothing there. | Does not prove schema enforcement. |
| Object-family sensitivity/quick reference | Confirms public-safe posture, most-material times, observed source-role default, and the open schema-home question. | Tier mapping and schema home remain NEEDS VERIFICATION. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized HydrostratigraphicUnit weakens source integrity, misstates source role, absorbs Hydrology measurements, hides model/interpretation uncertainty, exposes restricted detail, or depends on superseded source, geometry, Hydrology reference, rights, or release evidence.

Rollback triggers include:

- schema/home placement is superseded by ADR or schema decision;
- Hydrology co-signoff rejects field ownership or source references;
- source framework, model layer, or unit label corrected, withdrawn, or superseded;
- Hydrology measurement values were copied into Geology-owned unit truth;
- geometry, vertical extent, model version, or uncertainty corrected;
- public derivative exposes restricted subsurface/private-well-adjacent detail;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate units as public truth;
- release manifest lacks correction path or rollback target.

Rollback artifacts should include affected HydrostratigraphicUnit IDs, source record IDs, geologic unit refs, Hydrology context refs, geometry refs, model/version refs, public derivative refs, release IDs, evidence refs, policy decisions, validation reports, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should `HydrostratigraphicUnit` schema live under Geology or a neutral `hydrostratigraphy/` home? | OPEN / NEEDS VERIFICATION | ADR or co-signed Geology + Hydrology schema PR. |
| What Hydrology refs may be cited without copying measurements into Geology? | NEEDS VERIFICATION | Cross-lane policy and fixture review. |
| Which public geometry/vertical-generalization forms are acceptable? | NEEDS VERIFICATION | Policy, release, and spatial validation review. |
| How should model-derived hydrostratigraphic layers expose model version and uncertainty? | NEEDS VERIFICATION | Schema and representation receipt review. |
| Which source-role outcomes are allowed for regional frameworks vs model layers? | NEEDS VERIFICATION | Source-role matrix and fixture review. |
| How should MapLibre/AI surfaces communicate bridge context without implying Hydrology measurement truth? | NEEDS VERIFICATION | API/UI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/GeologicUnit.md` — mapped geologic unit support.
- `contracts/domains/geology/StratigraphicInterval.md` — stratigraphic interval support, if/when verified.
- `contracts/domains/geology/Lithology.md` — material-character support, if/when verified.
- `contracts/domains/geology/BoreholeReference.md` — subsurface point evidence and restricted-location posture.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary and Hydrology measurement exclusion.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference, lineage/cross-lane group, and schema-home open question.
- `schemas/contracts/v1/domains/geology/` — expected Geology machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve Geology vs neutral hydrostratigraphy schema home.
- [ ] Create or verify paired schema and fixtures.
- [ ] Add validation for geologic refs, Hydrology context refs, model/version refs, geometry/vertical extent, source role, and evidence refs.
- [ ] Add anti-collapse tests for hydrostratigraphy/Hydrology measurement/aquifer-test/water-quality/hazards/legal/UI-summary distinctions.
- [ ] Add source profiles or SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe hydrostratigraphic derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved schema-home/cross-lane drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
