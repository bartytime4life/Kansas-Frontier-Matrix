<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-geologic-age
title: GeologicAge Contract — Geology
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
policy_label: public-with-gates; semantic-contract; geology; geologic-age; chronostratigraphy; geochronology; vocabulary-versioned; source-role-aware; release-gated
tags: [kfm, contracts, geology, GeologicAge, geologic-age, geochronology, chronostratigraphy, time-scale, age-model, interval, unit, evidence, source-role, policy, release, correction, rollback]
related:
  - ./README.md
  - ./CrossSection.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/stratigraphy.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/GeologicAge.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology GeologicAge semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/GeologicAge.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "GeologicAge appears in the §10.B owns-list and is absent from the §E object-family table; this membership drift remains CONFLICTED / NEEDS VERIFICATION until ADR or schema decision."
  - "GeologicAge binds units or intervals to a geologic-time vocabulary/version with uncertainty; it does not replace GeologicUnit, StratigraphicInterval, sample dating evidence, CrossSection interpretation, or public release state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GeologicAge — Geology

> Semantic contract for Geology `GeologicAge`: the evidence-bound object for geochronologic and chronostratigraphic age bindings, time-scale vocabulary references, age-model uncertainty, unit/interval links, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: GeologicAge" src="https://img.shields.io/badge/object-GeologicAge-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: age binding not unit truth" src="https://img.shields.io/badge/boundary-age__binding__not__unit__truth-critical">
</p>

`contracts/domains/geology/GeologicAge.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Age classes](#age-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/GeologicAge.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/GeologicAge.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Geologic Age` as an owned object family in the §10.B owns-list, while the object-family roster notes that it is not present in the §E table. Field-level schema shape, fixtures, validators, source registry records, vocabulary registry records, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `GeologicAge` is an age-binding object. It does **not** replace `GeologicUnit`, `StratigraphicInterval`, `Lithology`, fossil/sample evidence, radiometric/geochemistry evidence, `CrossSection`, source map truth, or public release approval by itself.

---

## Meaning

`GeologicAge` is the Geology semantic object for binding a unit, interval, section, sample-derived interpretation, or source-native geology record to a geologic-time vocabulary or age model.

It answers:

- Which geologic age, age range, period, epoch, stage, chron, numerical age, or source-native age label is being asserted?
- Which vocabulary, chart, time scale, source edition, or model version defines the age label?
- Which unit, interval, sample, section, boundary, or source record uses the age binding?
- What source role, evidence, uncertainty, temporal scope, and correction state govern the age claim?
- What public-safe label or derivative may be shown, and which caveats must travel with it?
- Which policy decision, validation report, release manifest, correction notice, and rollback target govern downstream use?

A geologic age can be public-safe as a unit/interval attribute when rights allow, but it must stay vocabulary-versioned, evidence-bound, and correctable.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Geologic-age meaning | `contracts/domains/geology/GeologicAge.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/GeologicAge.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms owned family and adjacent-lane exclusions |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed key fields, material time, sensitivity posture, and roster drift |
| Stratigraphy doctrine | `docs/domains/geology/sublanes/stratigraphy.md` | Expected upstream context for interval and age-model use; NEEDS VERIFICATION if missing or stale |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy | `policy/domains/geology/` | Allow/deny/abstain and public projection decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, drift, vocabulary-version, and correction proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/GeologicAge.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/GeologicAge.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `GeologicAge` preserved because the user requested this path while Geology docs use human-readable `Geologic Age` |
| Membership drift | `Geologic Age` appears in §10.B owns-list but not in §E table; CONFLICTED / NEEDS VERIFICATION until ADR/schema decision |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `GeologicAge` should semantically assert:

1. **Age identity** — deterministic identity for the age binding, source label, vocabulary version, and normalized digest.
2. **Vocabulary support** — vocabulary, chart, time-scale edition, age-code system, or source-native model version.
3. **Bound object** — linked GeologicUnit, StratigraphicInterval, Lithology, CrossSection, sample, boundary, or source record that uses the age binding.
4. **Age expression** — named age, interval, minimum/maximum age, absolute age, relative age, source-native text, or mixed expression.
5. **Uncertainty support** — numeric uncertainty, lower/upper bounds, open bounds, disputed age, approximate label, or source caveat.
6. **Source identity** — SourceDescriptor, source record ID, source role, source time, rights, cadence, and attribution.
7. **Evidence linkage** — map legend, stratigraphic chart, publication, sample/dating report, fossil evidence, cross-section, EvidenceRef, or EvidenceBundle.
8. **Temporal discipline** — source time, valid time, retrieval time, release time, and correction time remain distinct where material.
9. **Derived-use posture** — public labels, map symbology, section labels, AI explanations, or graph/triplet claims must carry vocabulary/version and caveats.
10. **Governance state** — validation, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating age as unit identity | A unit may have an age binding, but GeologicUnit owns mapped unit identity. |
| Treating age as interval authority | StratigraphicInterval owns interval boundaries and names. |
| Treating a source age label as accepted vocabulary | Vocabulary/version and review state must be explicit. |
| Treating an absolute date as whole-unit truth | Date evidence must state sample/context, method, uncertainty, and representativeness. |
| Collapsing source time and geologic time | Source publication time is not the age being asserted. |
| Treating an AI explanation as age evidence | AI output is interpretive and subordinate to EvidenceBundle and source-role posture. |
| Publishing unsupported updated time-scale labels | Vocabulary updates require validation, correction, and release review. |
| Treating scaffold presence as release approval | Publication requires release manifest, policy outcome, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM geologic-age identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `GeologicAge` or accepted canonical spelling after naming reconciliation. |
| `age_class` | Chronostratigraphic, geochronologic, numeric date, relative age, source-native label, candidate, synthetic, or public derivative. |
| `age_code` | Stable age code or source-native code. |
| `age_label` | Public-safe age label. |
| `source_age_label` | Source-native age text retained for audit. |
| `vocabulary_ref` | Time-scale, chart, controlled vocabulary, or source legend ref. |
| `vocabulary_version` | Version/date/edition of the age vocabulary. |
| `lower_age_bound` | Lower/older bound where numeric. |
| `upper_age_bound` | Upper/younger bound where numeric. |
| `age_units` | Ma, ka, years BP, source-native units, or vocabulary-native units. |
| `uncertainty_summary` | Numeric uncertainty, approximation, disputed status, open bounds, or source caveat. |
| `bound_object_type` | GeologicUnit, StratigraphicInterval, Lithology, CrossSection, sample, source legend, or other accepted object. |
| `bound_object_ref` | Object ref this age binding applies to. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native map legend, chart, interval, sample, report, or figure record. |
| `dating_method_ref` | Dating method or method family where applicable. |
| `sample_evidence_refs` | Sample, fossil, geochemistry, core, or external dating evidence refs when applicable. |
| `stratigraphic_interval_refs` | Linked StratigraphicInterval refs. |
| `geologic_unit_refs` | Linked GeologicUnit or SurficialUnit refs. |
| `cross_section_refs` | Linked CrossSection refs where the age label appears. |
| `observed_time` | Collection/measurement/observation time where applicable. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the age vocabulary/binding is considered valid. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `policy_decision_ref` | Policy result governing use or public projection. |
| `review_record_ref` | Source, stratigraphy, vocabulary, or release review. |
| `validation_report_ref` | Validation report for schema, vocabulary, bounds, time discipline, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, vocabulary update, age-model update, source correction, supersession, and rollback lineage. |
| `quality_flags` | Vocabulary missing, source-age conflict, bound-object missing, uncertainty missing, range invalid, source-role conflict, stale vocabulary, or incomplete evidence. |

---

## Age classes

| Class | Meaning | Default posture |
|---|---|---|
| `chronostratigraphic` | Rock-time interval label such as system, series, stage, formation-time relation, or source-native equivalent. | Public-safe if vocabulary/version and source allow. |
| `geochronologic` | Time interval label such as period, epoch, age, or chron. | Public-safe if vocabulary/version and source allow. |
| `numeric_date` | Absolute or measured age estimate. | Requires method, sample/context, uncertainty, and representativeness caveat. |
| `relative_age` | Older/younger/superposition/correlation age claim. | Interpretation-bound; evidence and uncertainty required. |
| `source_native_label` | Map legend or report age text not yet normalized. | Preserve source label and mark normalization state. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated or hypothetical age label. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released public-safe label or graph/triplet projection. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | GeologicAge posture |
|---|---|---|
| Published geologic time scale, controlled vocabulary, map legend | `aggregate` or `administrative` | Defines vocabulary/source label; preserve version and source time. |
| Dated sample, fossil evidence, measured age, analytical report | `observed` | Evidence-bearing only for the sampled/contextual claim; representativeness must be reviewed. |
| Correlation, interpreted age model, cross-section label, inferred contact age | `modeled` | Interpretation/model output; preserve method/version/uncertainty. |
| Unreviewed import, unmapped source label, unmatched vocabulary row | `candidate` | Quarantine until source, vocabulary, and bound object resolve. |
| AI-generated or hypothetical age label | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`GeologicAge` is a binding, not the object it binds.

```text
GeologicAge != GeologicUnit
GeologicAge != StratigraphicInterval
GeologicAge != Lithology
GeologicAge != dated sample
GeologicAge != CrossSection interpretation
GeologicAge != source publication time
GeologicAge != public release approval
GeologicAge != AI summary
```

Any linkage must preserve source role, vocabulary/version, uncertainty, bound-object identity, evidence, and correction state.

---

## Sensitivity and release

Most geologic-age labels are public-safe at unit/interval scale when source rights allow, but age claims can still mislead if vocabulary version, uncertainty, or representativeness is hidden.

Rules:

- Public age labels must carry vocabulary/version and source/caveat posture where material.
- Numeric ages require method, uncertainty, sample/context, and representativeness notes before consequential use.
- Candidate, synthetic, vocabulary-unresolved, source-conflicted, stale, or evidence-incomplete records must not enter public outputs as authoritative age facts.
- Public outputs must preserve source role, source time, valid time, vocabulary version, uncertainty, and correction state.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision where material, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native age labels, legends, reports, dating rows, charts, vocabulary rows, and notes remain source-bound. |
| WORK / QUARANTINE | Candidate age labels are normalized, vocabulary-mapped, bound-object checked, source-role checked, rights-checked, uncertainty-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, vocabulary/version support, bound-object support, evidence refs, uncertainty posture, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, vocabulary version, temporal support, evidence, uncertainty, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, review where material, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe age labels, graph claims, or API/UI payloads appear in public clients. |
| CORRECTION | Vocabulary update, source correction, bound-object correction, sample correction, age-model supersession, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve whether `GeologicAge` remains the accepted contract name and schema path.
- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for chronostratigraphic label, geochronologic label, numeric date, relative age, source-native label, candidate record, and public derivative.
- [ ] Add invalid fixtures for missing vocabulary, missing version, invalid age bounds, source time treated as geologic age, missing bound object, sample date treated as whole-unit truth, missing uncertainty for numeric date, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, age code, vocabulary refs, vocabulary version, bound object refs, lower/upper bounds, units, uncertainty, source role, evidence refs, release refs, and correction refs.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for vocabulary update, time-scale revision, source correction, bound-object rename, numeric-age correction, public label rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, vocabulary/version is clear, bound object is valid, derivative is released | `ANSWER` / public-safe age claim may be shown |
| Evidence, vocabulary, source role, bound object, uncertainty, or version support is incomplete | `ABSTAIN` |
| Claim would mislead, hide uncertainty, bypass source rights, or exceed release state | `DENY` |
| Schema, validator, source-read, vocabulary-map, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns Geologic Age and preserves adjacent-domain ownership boundaries. | Records broader naming/membership drift and field realization remains PROPOSED. |
| Geology object-family doc | Confirms GeologicAge purpose, proposed key fields, material time, sensitivity posture, and §B-only roster membership. | Does not prove schema or validator enforcement. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized GeologicAge weakens source integrity, misstates vocabulary/version, collapses age into unit/interval truth, hides uncertainty, or depends on superseded source, vocabulary, bound object, or release evidence.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source age label corrected or withdrawn;
- geologic-time vocabulary version updated;
- age bounds, units, or uncertainty corrected;
- bound GeologicUnit, StratigraphicInterval, sample, or CrossSection corrected;
- source time and geologic age were collapsed;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate age labels as public truth;
- release manifest lacks correction path or rollback target.

Rollback artifacts should include affected GeologicAge IDs, vocabulary refs, bound-object refs, source record refs, public derivative refs, release IDs, evidence refs, validation reports, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `GeologicAge` the accepted contract name even though `Geologic Age` appears only in the §10.B roster? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted paired schema path and casing? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which geologic-time vocabulary/version is canonical for KFM public labels? | NEEDS VERIFICATION | Stratigraphy steward, schema, and source review. |
| How should numeric ages attach to samples without becoming whole-unit truth? | NEEDS VERIFICATION | Cross-contract schema and fixture review. |
| How should public UI display vocabulary version and uncertainty without clutter? | NEEDS VERIFICATION | API/UI projection review. |
| How should age-model updates trigger correction across units, intervals, sections, and maps? | NEEDS VERIFICATION | Validation, release, and rollback fixture design. |

---

## Related contracts and docs

- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and roster drift.
- `contracts/domains/geology/CrossSection.md` — interpretive section panels that may display age labels.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve `GeologicAge` naming and schema path.
- [ ] Create or verify paired schema and fixtures.
- [ ] Add validation for vocabulary/version, age bounds, units, uncertainty, source role, and bound-object refs.
- [ ] Add anti-collapse tests for age/unit/interval/sample/source-time/UI-summary distinctions.
- [ ] Add source profiles or vocabulary registry records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe age labels and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved membership/path/schema drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
