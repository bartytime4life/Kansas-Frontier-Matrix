<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-stratigraphic-interval
title: StratigraphicInterval Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Stratigraphy steward
  - OWNER_TBD — Geologic-time steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; stratigraphic-interval; bounded-contacts; age-model; vocabulary-versioned; source-role-aware; release-gated
tags: [kfm, contracts, geology, StratigraphicInterval, stratigraphic-interval, stratigraphy, chronostratigraphy, lithostratigraphy, interval-bounds, contacts, age-model, geologic-age, geologic-unit, lithology, evidence, source-role, policy, release, correction, rollback]
related:
  - ./README.md
  - ./GeologicUnit.md
  - ./GeologicAge.md
  - ./Lithology.md
  - ./CrossSection.md
  - ./BoreholeReference.md
  - ./CoreSample.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../docs/domains/geology/sublanes/stratigraphy.md
  - ../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../../schemas/contracts/v1/domains/geology/stratigraphic_interval.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology StratigraphicInterval semantic contract."
  - "A lower-case schema scaffold exists at schemas/contracts/v1/domains/geology/stratigraphic_interval.schema.json, while this requested contract path uses PascalCase. The schema's x-kfm.contract_doc points to contracts/domains/geology/stratigraphic_interval.md, creating a casing/path drift that remains CONFLICTED / NEEDS VERIFICATION."
  - "StratigraphicInterval means a named chronostratigraphic or lithostratigraphic interval with bounded contacts and age-model support. It does not replace GeologicUnit, GeologicAge, Lithology, CoreSample, BoreholeReference, CrossSection, boundary lineage, or public release state."
  - "Public use is usually safe at interval/label scale when rights allow, but source role, vocabulary version, bounds, age-model support, validation, release, correction, and rollback still govern publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# StratigraphicInterval — Geology

> Semantic contract for Geology `StratigraphicInterval`: the evidence-bound object for named chronostratigraphic or lithostratigraphic intervals, lower/upper bound references, age-model support, vocabulary versioning, source role, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: StratigraphicInterval" src="https://img.shields.io/badge/object-StratigraphicInterval-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: interval not unit or age truth" src="https://img.shields.io/badge/boundary-interval__not__unit__or__age__truth-critical">
</p>

`contracts/domains/geology/StratigraphicInterval.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Interval classes](#interval-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/StratigraphicInterval.md`  
> **Schema posture:** a lower-case scaffold exists at `schemas/contracts/v1/domains/geology/stratigraphic_interval.schema.json`; its `x-kfm.contract_doc` points to lower-case `contracts/domains/geology/stratigraphic_interval.md`, while the current requested contract path is PascalCase  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Stratigraphic Interval` as an owned object family for named intervals with bounded contacts and age model. Field-level schema shape, casing, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `StratigraphicInterval` is an interval/bounds/age-model object. It does **not** prove `GeologicUnit`, `GeologicAge`, `Lithology`, `BoreholeReference`, `CoreSample`, `GeochemistrySample`, `CrossSection`, `GeologyBoundaryVersion`, Hydrology measurement, Hazards risk, public layer release, or AI/UI truth by itself.

---

## Meaning

`StratigraphicInterval` is the Geology semantic object for a named stratigraphic interval, such as a group, formation, member, bed, series, stage, local interval, measured-section interval, borehole interval, source-native interval, or normalized KFM interval.

It answers:

- Which interval name, source-native label, vocabulary, or normalized stratigraphic identity is being asserted?
- Which lower and upper contacts, bounds, boundaries, depths/elevations, age refs, lithology refs, unit refs, source records, and evidence support apply?
- Which GeologicUnit, GeologicAge, Lithology, BoreholeReference, Well LogReference, CoreSample, CrossSection, or HydrostratigraphicUnit may cite the interval without collapsing identity?
- What source role, source time, valid time, retrieval time, release time, and correction time govern the interval claim?
- What public-safe label, interval range, section label, or graph/triplet derivative may be shown?
- Which validation report, policy decision where material, review record, release manifest, correction notice, and rollback target govern downstream use?

A stratigraphic interval can bind units, ages, lithologies, and subsurface evidence into a named or bounded interval. It is not the same thing as the unit, the age label, the lithology descriptor, the sample, or the public map layer.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Stratigraphic-interval meaning | `contracts/domains/geology/StratigraphicInterval.md` | Owned here by request; casing drift remains open |
| Machine schema shape | `schemas/contracts/v1/domains/geology/stratigraphic_interval.schema.json` | CONFIRMED scaffold; field shape still empty / PROPOSED |
| Schema/contract casing drift | `StratigraphicInterval.md` vs `stratigraphic_interval.schema.json` and lower-case `x-kfm.contract_doc` | CONFLICTED / NEEDS VERIFICATION |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms Stratigraphic Interval as owned for named intervals with bounded contacts and age model |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed keys, material times, sensitivity posture, and source-role context |
| Geologic unit support | `contracts/domains/geology/GeologicUnit.md` | Units may cite intervals; interval identity remains separate |
| Geologic age support | `contracts/domains/geology/GeologicAge.md` | Age bindings may support interval time scope; age identity remains separate |
| Lithology support | `contracts/domains/geology/Lithology.md` | Material descriptions may support interval characterization; lithology remains separate |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy | `policy/domains/geology/` | Allow/deny/abstain and public projection decisions where material |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, vocabulary, bounds, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

A paired schema exists only as a lower-case scaffold and does not yet enforce fields.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/StratigraphicInterval.md` |
| Confirmed schema path | `schemas/contracts/v1/domains/geology/stratigraphic_interval.schema.json` |
| Schema status | `PROPOSED` scaffold with empty `properties` and `additionalProperties: true` |
| Schema title | `Stratigraphic Interval` |
| Schema contract pointer | `contracts/domains/geology/stratigraphic_interval.md` |
| Casing/path posture | CONFLICTED / NEEDS VERIFICATION; requested PascalCase contract exists, schema points lower-case contract path |
| Field-level enforcement | NEEDS VERIFICATION |

Until the casing and schema-field decision is resolved, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `StratigraphicInterval` should semantically assert:

1. **Interval identity** — deterministic identity for the interval name, source, vocabulary/version, bound refs, temporal scope, and normalized digest.
2. **Interval name and rank** — interval name, rank/class, source-native label, normalized label, alias/correlation caveats, and vocabulary refs.
3. **Bound support** — lower and upper bound refs, contacts, depths/elevations, boundary versions, measured-section positions, or source-native bound descriptors.
4. **Age-model support** — GeologicAge refs, source age labels, age model/version, uncertainty, and time-scale caveats where material.
5. **Material and unit support** — linked GeologicUnit, SurficialUnit, Lithology, CoreSample, BoreholeReference, Well LogReference, GeochemistrySample, CrossSection, or HydrostratigraphicUnit refs.
6. **Source identity** — SourceDescriptor, source record ID, source role, source time, rights, cadence, and attribution.
7. **Evidence linkage** — map legend, measured section, core description, well log, borehole, report, geologic chart, cross-section, EvidenceRef, or EvidenceBundle.
8. **Temporal discipline** — source time, valid time, observed time where material, retrieval time, release time, and correction time remain distinct.
9. **Public projection** — public-safe interval label, section label, graph claim, or API/UI field must carry source/vocabulary/bounds caveats where material.
10. **Governance state** — validation, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating interval as geologic unit identity | GeologicUnit owns mapped unit identity; intervals are named/bounded stratigraphic contexts. |
| Treating interval as geologic age itself | GeologicAge owns age binding and vocabulary version; intervals may cite ages. |
| Treating interval as lithology itself | Lithology owns material-character descriptors; intervals may include lithology support. |
| Treating measured depth interval as a borehole | BoreholeReference owns drilled-location identity; interval may cite borehole evidence. |
| Treating core interval as a sample | CoreSample owns physical sample identity and custody. |
| Treating interval bounds as boundary lineage | GeologyBoundaryVersion owns mapped boundary replacement history. |
| Treating interval as Hydrology measurement | Hydrology owns gauges, flow, water levels, water quality; geology may supply context only. |
| Treating interval as hazards risk | Hazards owns risk. Geology may supply structural/stratigraphic context only. |
| Treating source-native interval as normalized without review | Vocabulary mapping and version must be explicit. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM stratigraphic-interval identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `StratigraphicInterval` or accepted canonical spelling after casing/path reconciliation. |
| `interval_id` | Source-native or KFM interval identifier. |
| `interval_name` | Normalized public-safe interval name. |
| `source_interval_name` | Source-native name/label retained for audit. |
| `interval_rank` | Group, formation, member, bed, series, stage, local interval, measured-section interval, borehole interval, or source-native rank. |
| `interval_class` | Lithostratigraphic, chronostratigraphic, biostratigraphic, magnetostratigraphic, informal, measured-section, borehole/log, candidate, or public derivative. |
| `vocabulary_ref` | Stratigraphic vocabulary, source legend, nomenclature authority, chart, or source-native code-list ref. |
| `vocabulary_version` | Version/date/edition of vocabulary or source nomenclature. |
| `lower_bound_ref` | Lower contact, depth, horizon, boundary version, sample/log marker, or source-native lower bound ref. |
| `upper_bound_ref` | Upper contact, depth, horizon, boundary version, sample/log marker, or source-native upper bound ref. |
| `bound_uncertainty_summary` | Bound confidence, open/approximate limits, disputed contact, measurement uncertainty, or source caveat. |
| `age_refs` | Linked GeologicAge refs. |
| `age_model_ref` | Age model/chart/version/source ref. |
| `age_uncertainty_summary` | Public-safe age/interval uncertainty. |
| `geologic_unit_refs` | Linked GeologicUnit or SurficialUnit refs. |
| `lithology_refs` | Linked Lithology/material descriptors. |
| `borehole_refs` | Linked BoreholeReference evidence. |
| `well_log_refs` | Linked Well LogReference evidence. |
| `core_sample_refs` | Linked CoreSample evidence. |
| `geochemistry_sample_refs` | Linked GeochemistrySample evidence. |
| `cross_section_refs` | Linked CrossSection refs where the interval appears. |
| `hydrostratigraphic_refs` | Linked HydrostratigraphicUnit refs where interval contributes context. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native interval, legend, chart, report, table, measured section, core, log, or figure record. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Field/section/sample/log observation time, where known and material. |
| `valid_time` | Time interval the interval nomenclature/bounds are considered valid. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `policy_decision_ref` | Policy result governing use or public projection where material. |
| `review_record_ref` | Source, stratigraphy, vocabulary, sample/log, or release review. |
| `validation_report_ref` | Validation report for schema, vocabulary, bounds, source-role, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, nomenclature correction, bound correction, age-model update, bound-object correction, rights update, and rollback lineage. |
| `quality_flags` | Vocabulary missing, interval conflict, lower/upper bound missing, invalid bound order, age conflict, source-role conflict, bound-object missing, rights unknown, stale source, or incomplete evidence. |

---

## Interval classes

| Class | Meaning | Default posture |
|---|---|---|
| `lithostratigraphic` | Rock-unit interval such as group, formation, member, bed, or informal unit interval. | Public-safe when source rights allow. |
| `chronostratigraphic` | Time-rock interval such as system, series, stage, or source-native equivalent. | Vocabulary/version required. |
| `measured_section_interval` | Interval from measured section or field column. | Evidence-bound; location/detail may require review. |
| `borehole_or_log_interval` | Interval in borehole, well log, core, or subsurface section. | Rights and exact-location posture material. |
| `correlated_interval` | Interval correlated across sources, sections, wells, or map editions. | Requires evidence, method, and uncertainty caveats. |
| `source_native_label` | Source interval label not yet normalized. | Preserve source label and mark normalization state. |
| `candidate_record` | Unreviewed import or unresolved interval. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical interval. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released public-safe label or simplified interval representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | StratigraphicInterval posture |
|---|---|---|
| Published stratigraphic chart, map legend, nomenclature table | `administrative` or `aggregate` | Defines interval naming/context; preserve version/source time. |
| Measured section, core description, borehole log interval | `observed` | Evidence-bearing interval support; preserve observation/custody/location caveats. |
| Correlation panel, cross-section interpretation, inferred contact | `modeled` | Interpretation/model output; never relabel as observed interval truth. |
| Regional framework or compiled stratigraphic synthesis | `aggregate` | Compiled support; preserve source scale/version and caveats. |
| Source vocabulary/code-list row | `administrative` | Defines labels/codes; not interval observation by itself. |
| Unreviewed import, unmatched interval name, conflicting bounds | `candidate` | Quarantine until vocabulary, source role, bounds, and bound-object support resolve. |
| AI-generated or hypothetical interval | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`StratigraphicInterval` is interval identity and bound support, not the object it binds.

```text
StratigraphicInterval != GeologicUnit
StratigraphicInterval != GeologicAge
StratigraphicInterval != Lithology
StratigraphicInterval != GeologyBoundaryVersion
StratigraphicInterval != BoreholeReference
StratigraphicInterval != Well LogReference
StratigraphicInterval != CoreSample
StratigraphicInterval != GeochemistrySample
StratigraphicInterval != CrossSection
StratigraphicInterval != HydrostratigraphicUnit
StratigraphicInterval != Hydrology measurement
StratigraphicInterval != Hazards risk
StratigraphicInterval != public release approval
StratigraphicInterval != AI summary
```

Any linkage must preserve source role, vocabulary/version, bounds, bound-object identity, evidence, uncertainty, rights, validation, release, and correction state.

---

## Sensitivity and release

Stratigraphic interval names and broad bounds are usually public-safe when source rights allow, but exact subsurface intervals, borehole/log-derived intervals, proprietary measured sections, and interpreted correlations can require review, generalization, or suppression.

Rules:

- An interval label is not automatically a released public claim.
- Public derivatives require validation, rights review where material, release manifest, correction path, and rollback target.
- Public outputs must preserve source role, vocabulary/version, bounds caveats, source time, valid time, age-model caveats, and correction state.
- Source-native labels must not be silently normalized without review.
- Candidate, synthetic, vocabulary-unresolved, bound-conflicted, rights-unknown, stale, or evidence-incomplete intervals must not enter public outputs as authoritative interval facts.
- Cross-lane use must not harden stratigraphic context into Soil, Hydrology, Hazards, resource, or UI/AI truth.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native interval names, legends, charts, contacts, measured-section rows, borehole/log/core intervals, reports, and tables remain source-bound. |
| WORK / QUARANTINE | Candidate intervals are normalized, vocabulary-mapped, bounds-checked, bound-object checked, source-role checked, rights/sensitivity-screened, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, vocabulary/version support, lower/upper bound refs, age refs, bound-object refs, evidence refs, rights state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, source time, valid time, vocabulary version, bound support, evidence, uncertainty, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, review where material, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe interval labels, graph claims, or API/UI payloads appear in public clients. |
| CORRECTION | Source update, vocabulary update, bound correction, age-model update, interval rename, bound-object correction, rights update, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve casing/path drift between `StratigraphicInterval.md`, lower-case schema file, and lower-case schema `contract_doc` pointer.
- [ ] Expand `stratigraphic_interval.schema.json` from scaffold into field-level validation, or record the accepted schema path via ADR/schema PR.
- [ ] Add valid fixtures for lithostratigraphic interval, chronostratigraphic interval, measured-section interval, borehole/log interval, correlated interval, source-native label, candidate record, synthetic example, and public derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing vocabulary ref, missing lower/upper bounds where required, invalid bound order, missing age ref where required, source-native label silently normalized, interval treated as unit/age/lithology/sample/boundary truth, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, interval name/rank/class, vocabulary refs, lower and upper bound refs, age refs, bound-object refs, source role, evidence refs, release refs, and correction refs.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for vocabulary update, source correction, bound correction, interval rename, age-model update, unit/sample binding correction, public label rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, vocabulary/version is clear, bounds are valid, derivative is released | `ANSWER` / public-safe interval claim may be shown |
| Evidence, vocabulary, source role, bounds, bound object, rights, or release support is incomplete | `ABSTAIN` |
| Claim would misstate source role, collapse adjacent-domain truth, hide uncertainty, or bypass release | `DENY` |
| Schema, validator, source-read, vocabulary-map, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Confirmed schema scaffold | Confirms lower-case schema file exists, is PROPOSED, and currently has empty properties. | Does not prove field validation; also exposes casing/path drift. |
| Geology scope doc | Confirms Geology owns Stratigraphic Interval for named intervals with bounded contacts and age model. | Does not prove schema or implementation enforcement. |
| Geology object-family doc | Confirms StratigraphicInterval purpose, proposed key fields, material times, sensitivity posture, and foundational placement. | Field realization remains PROPOSED. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized StratigraphicInterval weakens source integrity, misstates vocabulary/version, collapses interval into unit/age/lithology/sample/boundary truth, hides bound uncertainty, or depends on superseded source, vocabulary, bound object, rights, or release evidence.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source interval name, rank, or bounds corrected or withdrawn;
- stratigraphic vocabulary, chart, or nomenclature version updated;
- lower/upper bound, bound object, or age-model support corrected;
- interval was presented as GeologicUnit, GeologicAge, Lithology, CoreSample, BoreholeReference, or CrossSection identity;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate intervals as public truth;
- public derivative lacks release manifest, correction path, or rollback target.

Rollback artifacts should include affected StratigraphicInterval IDs, vocabulary refs, lower/upper bound refs, age refs, bound-object refs, source record refs, public derivative refs, release IDs, evidence refs, validation reports, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should the contract file be PascalCase `StratigraphicInterval.md` or lower-case `stratigraphic_interval.md` to match the schema scaffold pointer? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted schema path and casing for `StratigraphicInterval`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which stratigraphic vocabulary or authority stack is canonical for KFM? | NEEDS VERIFICATION | Schema, source, and stratigraphy steward review. |
| How should lower/upper bound refs attach to GeologyBoundaryVersion, contacts, boreholes/logs, samples, or cross-sections without duplicating their identity? | NEEDS VERIFICATION | Cross-contract schema review. |
| How should interval names be correlated across source map editions without over-normalizing source meaning? | NEEDS VERIFICATION | Fixture and validator design. |
| How should public UI display source/vocabulary/bounds/age-model caveats without clutter? | NEEDS VERIFICATION | API/UI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/GeologicUnit.md` — mapped unit identity that may cite intervals.
- `contracts/domains/geology/GeologicAge.md` — age binding and vocabulary-versioned geologic-time claims.
- `contracts/domains/geology/Lithology.md` — material-character descriptors for interval characterization.
- `contracts/domains/geology/CrossSection.md` — interpretive panels that may display intervals.
- `contracts/domains/geology/BoreholeReference.md` — subsurface point evidence for borehole/log intervals.
- `contracts/domains/geology/CoreSample.md` — physical sample evidence that may cite interval context.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and StratigraphicInterval semantics.
- `schemas/contracts/v1/domains/geology/stratigraphic_interval.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve PascalCase vs lower-case contract/schema path drift.
- [ ] Expand paired schema and fixtures.
- [ ] Add validation for interval name, rank/class, vocabulary ref/version, lower/upper bound refs, age refs, source role, bound objects, and evidence refs.
- [ ] Add anti-collapse tests for interval/unit/age/lithology/sample/boundary/hydrology/hazards/UI-summary distinctions.
- [ ] Add source profiles or vocabulary registry records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe interval labels and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved path/schema/vocabulary drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
