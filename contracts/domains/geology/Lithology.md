<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-lithology
title: Lithology Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Lithology steward
  - OWNER_TBD — Stratigraphy steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; lithology; material-character; vocabulary-versioned; source-role-aware; release-gated
tags: [kfm, contracts, geology, Lithology, material-character, rock, sediment, descriptor-set, vocabulary, geologic-unit, stratigraphic-interval, core-sample, evidence, source-role, policy, release, correction, rollback]
related:
  - ./README.md
  - ./GeologicUnit.md
  - ./GeologicAge.md
  - ./StratigraphicInterval.md
  - ./CoreSample.md
  - ./GeochemistrySample.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../docs/domains/geology/sublanes/stratigraphy.md
  - ../../../docs/domains/geology/sublanes/bedrock_geology.md
  - ../../../schemas/contracts/v1/domains/geology/Lithology.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology Lithology semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/Lithology.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "Lithology is a material-character descriptor for units, samples, and intervals. It does not replace GeologicUnit, StratigraphicInterval, CoreSample, GeochemistrySample, GeologicAge, Soil objects, resource claims, or public release state."
  - "Public use is usually safe at unit/descriptor scale when rights allow, but source role, vocabulary version, evidence, validation, release, correction, and rollback still govern publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Lithology — Geology

> Semantic contract for Geology `Lithology`: the evidence-bound object for rock and sediment material-character descriptions, lithology vocabularies, descriptor sets, unit/sample/interval links, public-safe derivatives, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: Lithology" src="https://img.shields.io/badge/object-Lithology-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: descriptor not unit or sample truth" src="https://img.shields.io/badge/boundary-descriptor__not__unit__or__sample__truth-critical">
</p>

`contracts/domains/geology/Lithology.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Lithology classes](#lithology-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/Lithology.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/Lithology.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Lithology` as an owned foundational object family for the material character of a unit or sample. Field-level schema shape, fixtures, validators, source registry records, vocabulary registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `Lithology` is a material-character descriptor. It does **not** replace `GeologicUnit`, `StratigraphicInterval`, `CoreSample`, `GeochemistrySample`, `GeologicAge`, `HydrostratigraphicUnit`, Soil objects, mineral/resource claims, Hazards risk, public layer release, or AI/UI truth by itself.

---

## Meaning

`Lithology` is the Geology semantic object for rock, sediment, or unconsolidated-material character as described by a source, vocabulary, sample, unit, interval, or interpretation.

It answers:

- Which material character is being asserted?
- Which vocabulary, descriptor set, source record, source role, source time, and evidence support the lithology?
- Which GeologicUnit, SurficialUnit, StratigraphicInterval, CoreSample, BoreholeReference, Well LogReference, GeochemistrySample, CrossSection, or HydrostratigraphicUnit may cite the descriptor without collapsing identity?
- What uncertainty, descriptor granularity, source-native terminology, normalization state, and correction state govern downstream use?
- What public-safe label or derivative may be shown, and which caveats must travel with it?

A lithology can support unit, interval, sample, and hydrostratigraphic interpretation. It is not itself the mapped unit, sampled object, geochemical result, resource claim, or published layer.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Lithology meaning | `contracts/domains/geology/Lithology.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/Lithology.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms owned family and adjacent-lane exclusions |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed keys, material time, sensitivity posture, and roster placement |
| Geologic unit support | `contracts/domains/geology/GeologicUnit.md` | Unit identity may cite Lithology; lithology does not replace unit truth |
| Stratigraphy support | `contracts/domains/geology/StratigraphicInterval.md` | Intervals may cite Lithology; interval identity stays separate |
| Sample support | `contracts/domains/geology/CoreSample.md`, `contracts/domains/geology/GeochemistrySample.md` | Samples may carry material evidence; Lithology does not replace sample identity |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy | `policy/domains/geology/` | Allow/deny/abstain and public projection decisions where material |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, vocabulary, descriptor-set, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/Lithology.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/Lithology.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `Lithology` preserved because the user requested this path and Geology docs use this owned-family spelling |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `Lithology` should semantically assert:

1. **Descriptor identity** — deterministic identity for the lithology descriptor, vocabulary/version, source, temporal scope, and normalized digest.
2. **Material character** — rock/sediment/material label, source-native descriptor, normalized vocabulary label, descriptor set, and composition/texture/fabric qualifiers where supported.
3. **Vocabulary support** — vocabulary, classification system, source legend, code list, or source-native terminology with version/source state.
4. **Bound-object support** — linked unit, interval, sample, borehole, well log, cross-section, or hydrostratigraphic context that uses the descriptor.
5. **Source identity** — SourceDescriptor, source record ID, source role, source time, rights, cadence, and attribution.
6. **Evidence linkage** — map legend, report, sample description, core description, geochemistry, photo/media, well log, EvidenceRef, or EvidenceBundle.
7. **Uncertainty support** — source confidence, mixed lithology proportion, descriptor granularity, conflicting labels, approximate classification, or vocabulary drift.
8. **Temporal discipline** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
9. **Public projection** — public-safe label, descriptor class, simplified legend entry, or graph claim must carry vocabulary/source caveats where material.
10. **Governance state** — validation, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating lithology as unit identity | A GeologicUnit may cite lithology, but unit identity belongs to GeologicUnit. |
| Treating lithology as sample identity | CoreSample / GeochemistrySample own sample identity and custody/context. |
| Treating lithology as age or interval truth | GeologicAge and StratigraphicInterval own age/interval claims. |
| Treating lithology as soil mapunit | Soil owns soil horizons, pedons, mapunits, and soil classifications. |
| Treating lithology as resource proof | MineralOccurrence, ResourceDeposit, and ResourceEstimate remain separate object families. |
| Treating lithology as hazards risk | Hazards owns risk; Geology may supply material context only. |
| Treating source-native descriptor as normalized vocabulary without review | Vocabulary mapping and version must be explicit. |
| Treating public label as release approval | Publication requires release manifest, validation, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM lithology identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `Lithology`. |
| `lithology_class` | Igneous, sedimentary, metamorphic, unconsolidated, mixed, source-native, candidate, synthetic, or public derivative. |
| `lithology_code` | Normalized lithology code or source-native code. |
| `lithology_label` | Normalized public-safe material label. |
| `source_lithology_label` | Source-native descriptor retained for audit. |
| `vocabulary_ref` | Vocabulary, legend, classification system, or source-native code-list ref. |
| `vocabulary_version` | Version/date/edition of the vocabulary or source classification. |
| `descriptor_set_hash` | Stable hash of normalized descriptor set. |
| `descriptor_set` | Grain size, composition, color, texture, fabric, cement, sorting, bedding, alteration, metamorphic grade, or other source-supported descriptors. |
| `modifier_refs` | Optional normalized modifier refs or source-native modifier refs. |
| `proportion_summary` | Dominant/minor/interbedded/proportional composition, if supported. |
| `bound_object_type` | GeologicUnit, SurficialUnit, StratigraphicInterval, CoreSample, BoreholeReference, Well LogReference, GeochemistrySample, CrossSection, HydrostratigraphicUnit, or source legend. |
| `bound_object_ref` | Object ref this lithology applies to. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native legend, sample, report, interval, core description, log, table, or figure record. |
| `geologic_unit_refs` | Linked GeologicUnit refs. |
| `surficial_unit_refs` | Linked SurficialUnit refs, if applicable. |
| `stratigraphic_interval_refs` | Linked StratigraphicInterval refs. |
| `core_sample_refs` | Linked CoreSample refs. |
| `geochemistry_sample_refs` | Linked GeochemistrySample refs. |
| `borehole_refs` | Linked BoreholeReference refs. |
| `well_log_refs` | Linked well-log refs. |
| `cross_section_refs` | Linked CrossSection refs where descriptor appears. |
| `hydrostratigraphic_refs` | Linked HydrostratigraphicUnit refs where material character supports context. |
| `observed_time` | Observation/description/sample time, if known and material. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the descriptor/binding claims to represent, where material. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `policy_decision_ref` | Policy result governing use or public projection where material. |
| `review_record_ref` | Source, geology, vocabulary, sample, or release review. |
| `validation_report_ref` | Validation report for schema, vocabulary, descriptor mapping, source-role, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, vocabulary update, source correction, descriptor remap, bound-object correction, rights update, and rollback lineage. |
| `quality_flags` | Vocabulary missing, descriptor conflict, bound-object missing, source-role conflict, mixed lithology unresolved, rights unknown, stale source, or incomplete evidence. |

---

## Lithology classes

| Class | Meaning | Default posture |
|---|---|---|
| `sedimentary` | Sedimentary rock or sediment descriptor. | Public-safe when source rights allow. |
| `igneous` | Intrusive/extrusive igneous material descriptor. | Public-safe when source rights allow. |
| `metamorphic` | Metamorphic material descriptor. | Public-safe when source rights allow. |
| `unconsolidated` | Surficial or unconsolidated material descriptor. | Public-safe as geology context; Soil objects remain Soil-owned. |
| `mixed_or_interbedded` | Composite, interbedded, mixed, or proportional descriptor. | Requires proportion/caveat where source supports it. |
| `source_native_label` | Source descriptor not yet normalized. | Preserve source label and mark normalization state. |
| `candidate_record` | Unreviewed import or unresolved descriptor. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical descriptor. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released public-safe label or simplified descriptor. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | Lithology posture |
|---|---|---|
| Field/map legend lithology assigned to unit | `observed` with interpretation caveat | Evidence-bearing unit attribute; preserve source map/version. |
| Core/sample description | `observed` | Evidence-bearing sample/interval descriptor; preserve sample context and time. |
| Regional compiled lithology class | `aggregate` | Compiled support; preserve scale/source version and caveats. |
| Log-derived or model-derived lithology | `modeled` | Interpretation/model output; never label as direct observation. |
| Source vocabulary/code-list row | `administrative` | Defines labels/codes; not material observation by itself. |
| Unreviewed import, unmatched descriptor, conflicting vocabulary | `candidate` | Quarantine until vocabulary and bound-object support resolve. |
| AI-generated or hypothetical descriptor | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`Lithology` is material characterization, not the object it describes.

```text
Lithology != GeologicUnit
Lithology != StratigraphicInterval
Lithology != GeologicAge
Lithology != CoreSample
Lithology != GeochemistrySample
Lithology != HydrostratigraphicUnit
Lithology != Soil mapunit / horizon / pedon
Lithology != MineralOccurrence
Lithology != ResourceDeposit / ResourceEstimate
Lithology != Hazards risk
Lithology != public release approval
Lithology != AI summary
```

Any linkage must preserve source role, vocabulary/version, bound-object identity, evidence, uncertainty, rights, validation, release, and correction state.

---

## Sensitivity and release

Lithology is usually public-safe at unit, interval, or sample-description scale when source rights allow. It can still become sensitive or misleading when exact sample location, proprietary core descriptions, private subsurface records, resource-adjacent detail, or weak vocabulary mapping is exposed without caveats.

Rules:

- A lithology descriptor is not automatically a released public attribute.
- Public derivatives require validation, rights review where material, release manifest, correction path, and rollback target.
- Public outputs must preserve source role, vocabulary/version, bound-object context, source time, descriptor uncertainty, and caveats.
- Source-native labels must not be silently normalized without review.
- Candidate, synthetic, vocabulary-unresolved, bound-object-missing, rights-unknown, stale, or evidence-incomplete descriptors must not enter public outputs as authoritative lithology facts.
- Cross-lane use must not harden geology material context into Soil, Hazards, Hydrology, resource, or UI/AI truth.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native lithology labels, legends, sample descriptions, core descriptions, logs, code lists, and reports remain source-bound. |
| WORK / QUARANTINE | Candidate descriptors are normalized, vocabulary-mapped, bound-object checked, source-role checked, rights/sensitivity-screened, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, vocabulary/version support, descriptor-set hash, bound-object refs, evidence refs, rights state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, source time, vocabulary version, bound-object context, evidence, uncertainty, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, review where material, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe lithology labels, graph claims, or API/UI payloads appear in public clients. |
| CORRECTION | Source update, vocabulary update, descriptor remap, bound-object correction, sample correction, rights update, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for sedimentary, igneous, metamorphic, unconsolidated, mixed/interbedded, source-native label, candidate record, synthetic display descriptor, and public derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing vocabulary ref, missing descriptor-set hash, missing bound object, source-native label silently normalized, lithology treated as unit/sample/age/soil/resource/risk truth, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, lithology code, vocabulary refs, descriptor-set hash, bound-object refs, source role, evidence refs, release refs, and correction refs.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for vocabulary update, source correction, descriptor remap, unit/sample binding correction, public label rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, vocabulary/version is clear, bound object is valid, derivative is released | `ANSWER` / public-safe lithology claim may be shown |
| Evidence, vocabulary, source role, bound object, rights, or descriptor support is incomplete | `ABSTAIN` |
| Claim would misstate source role, collapse adjacent-domain truth, hide uncertainty, or bypass release | `DENY` |
| Schema, validator, source-read, vocabulary-map, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns Lithology as material character of a unit or sample and preserves adjacent-domain ownership boundaries. | Does not prove schema or implementation enforcement. |
| Geology object-family doc | Confirms Lithology purpose, proposed key fields, material time, sensitivity posture, and foundational placement. | Field realization remains PROPOSED. |
| Object-family quick reference | Confirms `Lithology` appears in the §B + §E roster with source as most-material time and T0 public-safe posture. | Schema filename is PROPOSED and exact current schema path was not found. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized Lithology weakens source integrity, misstates vocabulary/version, collapses material description into unit/sample/resource/soil/risk truth, hides uncertainty, or depends on superseded source, vocabulary, bound object, rights, or release evidence.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source lithology label corrected or withdrawn;
- vocabulary/code-list version updated;
- descriptor set, modifier, or proportion corrected;
- bound GeologicUnit, StratigraphicInterval, CoreSample, GeochemistrySample, or HydrostratigraphicUnit corrected;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate descriptors as public truth;
- public derivative lacks release manifest, correction path, or rollback target.

Rollback artifacts should include affected Lithology IDs, vocabulary refs, descriptor-set hashes, bound-object refs, source record refs, public derivative refs, release IDs, evidence refs, validation reports, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| What is the accepted paired schema path and casing for `Lithology`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which lithology vocabulary or vocabulary-stack is canonical for KFM? | NEEDS VERIFICATION | Schema, source, and geology steward review. |
| How should mixed/interbedded descriptors be normalized without losing source meaning? | NEEDS VERIFICATION | Fixture and validator design. |
| How should Lithology attach to CoreSample and GeochemistrySample without duplicating custody or analyte semantics? | NEEDS VERIFICATION | Cross-contract schema review. |
| How should surficial/unconsolidated lithology support Soil without becoming Soil truth? | NEEDS VERIFICATION | Soil/Geology cross-lane policy review. |
| How should public UI display vocabulary/source caveats without clutter? | NEEDS VERIFICATION | API/UI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/GeologicUnit.md` — mapped unit identity that may cite Lithology.
- `contracts/domains/geology/GeologicAge.md` — age binding and vocabulary-versioned geologic-time claims.
- `contracts/domains/geology/CoreSample.md` — physical sample evidence that may carry lithology descriptions.
- `contracts/domains/geology/GeochemistrySample.md` — analytical sample evidence that may support material characterization.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and Lithology semantics.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Create or verify paired schema and fixtures.
- [ ] Add validation for lithology code, vocabulary ref/version, descriptor-set hash, source role, bound object, and evidence refs.
- [ ] Add anti-collapse tests for lithology/unit/sample/age/soil/resource/risk/UI-summary distinctions.
- [ ] Add source profiles or vocabulary registry records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe lithology labels and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved path/schema/vocabulary drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
