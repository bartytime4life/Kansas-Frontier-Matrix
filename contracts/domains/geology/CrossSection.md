<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-cross-section
title: CrossSection Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Cross-section steward
  - OWNER_TBD — Stratigraphy steward
  - OWNER_TBD — Bedrock geology steward
  - OWNER_TBD — Surficial geology steward
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
policy_label: public-with-gates; semantic-contract; geology; cross-section; interpretation-versioned; source-role-aware; release-gated; reality-boundary-required
tags: [kfm, contracts, geology, CrossSection, cross-section, subsurface, stratigraphy, bedrock, surficial, borehole, well-log, geophysics, interpretation, evidence, source-role, policy, release, correction, rollback]
related:
  - ./README.md
  - ./BoreholeReference.md
  - ./CoreSample.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/stratigraphy.md
  - ../../../docs/domains/geology/sublanes/bedrock_geology.md
  - ../../../docs/domains/geology/sublanes/surficial.md
  - ../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../pipelines/domains/geology/cross_sections/README.md
  - ../../../schemas/contracts/v1/domains/geology/CrossSection.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology CrossSection semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/CrossSection.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "CrossSection is a 2D/2.5D interpretive subsurface section with explicit interpretation version, line geometry, evidence basis, vertical exaggeration disclosure, and reality-boundary requirements."
  - "A CrossSection does not replace GeologicUnit, SurficialUnit, StratigraphicInterval, BoreholeReference, Well LogReference, CoreSample, GeophysicalObservation, HydrostratigraphicUnit, or public-safe released derivatives."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CrossSection — Geology

> Semantic contract for Geology `CrossSection`: the evidence-bound object for 2D / 2.5D interpretive subsurface sections, section traces, panels, vertical scales, correlation surfaces, uncertainty bands, evidence inputs, public-safe derivatives, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: CrossSection" src="https://img.shields.io/badge/object-CrossSection-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: interpretation not direct observation" src="https://img.shields.io/badge/boundary-interpretation__not__direct__observation-critical">
</p>

`contracts/domains/geology/CrossSection.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Section classes](#section-classes) · [Source-role rules](#source-role-rules) · [Reality boundary](#reality-boundary) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/CrossSection.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/CrossSection.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `CrossSection` as an owned object family for 2D interpretive sections with explicit interpretation version. Field-level schema shape, fixtures, validators, policy runtime, source registry records, release workflow, API behavior, UI behavior, rendering behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `CrossSection` is an interpretation carrier. It does **not** certify a direct observation, does **not** replace mapped `GeologicUnit` or `SurficialUnit` truth, does **not** replace `StratigraphicInterval`, `BoreholeReference`, `Well LogReference`, `CoreSample`, or `GeophysicalObservation`, and does **not** authorize public release of exact or sensitive subsurface context by itself.

---

## Meaning

`CrossSection` is the Geology semantic object for a section trace and interpretive panel that depicts subsurface relationships along a line or corridor. It can use admitted evidence from mapped units, boreholes, well logs, cores, measured sections, geophysical observations, stratigraphic intervals, structure features, and hydrostratigraphic context.

It answers:

- Which section line, panel, interpretation version, vertical datum, vertical scale, and display envelope are being referenced?
- Which evidence inputs support the section, and which parts are directly observed, inferred, modeled, generalized, or schematic?
- Which units, intervals, contacts, faults, folds, horizons, tops, picks, correlation lines, and uncertainty bands appear in the panel?
- What is the public-safe derivative, if any, and what caveats must travel with it?
- Which policy decision, review record, representation receipt, release manifest, correction notice, and rollback target govern downstream use?

A cross section can communicate geology. It cannot become the root truth source for the evidence it summarizes.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Cross-section meaning | `contracts/domains/geology/CrossSection.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/CrossSection.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms CrossSection purpose and interpretation-version posture |
| Scope boundary | `docs/domains/geology/SCOPE.md` | Confirms Geology owns CrossSection but not adjacent-domain truth |
| Pipeline logic | `pipelines/domains/geology/cross_sections/README.md` | Executable processing/handoff support only |
| Evidence inputs | `BoreholeReference.md`, `CoreSample.md`, well-log/stratigraphy/unit/geophysics contracts | Referenced evidence families; do not collapse identities |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, interpretive, restricted, and public-safe proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/CrossSection.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/CrossSection.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `CrossSection` preserved because the user requested this path and Geology docs use this spelling |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `CrossSection` should semantically assert:

1. **Section identity** — deterministic identity for the section trace, panel, interpretation version, source, and normalized digest.
2. **Section geometry** — line geometry, corridor, endpoints, orientation, map context, and geometry precision.
3. **Panel geometry** — horizontal scale, vertical datum, vertical scale, vertical exaggeration, display envelope, and units.
4. **Interpretation version** — explicit version, author/source, method, basis, review state, and supersession lineage.
5. **Evidence basis** — linked boreholes, well logs, cores, measured sections, geophysics, mapped units, structures, intervals, and EvidenceBundles.
6. **Observed vs inferred posture** — clear distinction among observed contacts, interpreted contacts, modeled surfaces, schematic features, and generalized display features.
7. **Uncertainty support** — confidence, uncertainty bands, correlation uncertainty, unsupported gaps, and caveats.
8. **Sensitivity posture** — exact subsurface, private/source-restricted evidence, proprietary data, resource-adjacent detail, or public-safe state.
9. **Release posture** — public derivative, representation/redaction receipt, review, validation, release manifest, correction path, and rollback target.
10. **Cross-lane boundary** — Hydrostratigraphy, Hazards, People/Land, resource, permit, and UI/AI claims remain separate authority classes.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a section panel as direct observation | A cross section is interpretive unless the specific feature is tied to observed evidence. |
| Treating a cross section as canonical map-unit truth | It may reference units; it does not replace GeologicUnit or SurficialUnit. |
| Treating inferred contacts as observed contacts | Interpretation class and confidence must be explicit. |
| Treating vertical exaggeration as physical geometry | Vertical exaggeration must be disclosed. |
| Treating a section as reserve/resource proof | Resource objects and estimates remain separate governed identities. |
| Treating hydrostratigraphic context as Hydrology measurement | Hydrology owns measurement truth; Geology supplies context only. |
| Treating a rendered panel as release approval | Publication requires release manifest, policy outcome, correction path, and rollback target. |
| Treating generated diagrams as EvidenceBundle | Rendered images and AI summaries are downstream carriers only. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM cross-section identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `CrossSection`. |
| `section_class` | Published section, source section, interpreted panel, schematic panel, measured section, model-derived section, candidate, or public derivative. |
| `section_id` | Source-native or KFM section identifier. |
| `section_trace_ref` | Section line/corridor geometry reference. |
| `line_geometry_fingerprint` | Stable fingerprint for trace geometry. |
| `panel_geometry_ref` | Panel/display geometry reference, if modeled separately. |
| `horizontal_units` | Distance units for panel or trace. |
| `vertical_units` | Elevation/depth units. |
| `vertical_datum` | NAVD88, sea level, source-native datum, ground surface, or unknown. |
| `vertical_exaggeration` | Numeric or source-native vertical exaggeration disclosure. |
| `interpretation_version` | Explicit interpretation version or source edition. |
| `interpretation_basis_ref` | Evidence/method basis for the section. |
| `method_summary` | Source-native or normalized method description. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, candidate, regulatory, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native section record, publication, figure, plate, dataset, or panel ID. |
| `geologic_unit_refs` | Linked GeologicUnit or SurficialUnit refs appearing in the panel. |
| `stratigraphic_interval_refs` | Linked interval refs used in correlation. |
| `structure_feature_refs` | Fault/fold/contact/structure refs used in panel. |
| `borehole_refs` | Linked BoreholeReference evidence. |
| `well_log_refs` | Linked Well LogReference or log/pick evidence. |
| `core_sample_refs` | Linked CoreSample evidence. |
| `geophysical_observation_refs` | Linked geophysical horizons or survey evidence. |
| `hydrostratigraphic_refs` | Hydrostratigraphic context refs, not Hydrology measurements. |
| `uncertainty_summary` | Confidence, uncertainty bands, correlation caveats, and unsupported gaps. |
| `reality_boundary_note` | Required note explaining observed/inferred/modeled/schematic status. |
| `representation_receipt_ref` | Receipt for synthetic/reconstructed panel, rendering, exaggeration, or transformation where required. |
| `redaction_receipt_ref` | Required when exact/sensitive inputs are generalized or withheld. |
| `observed_time` | Observation time for source evidence where material. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the interpretation claims to represent. |
| `retrieval_time` | Time KFM retrieved the source record. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Public-safe, generalized, restricted, source-limited, proprietary, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release. |
| `review_record_ref` | Source, geology, interpretation, sensitivity, or release review. |
| `validation_report_ref` | Validation report for schema, evidence closure, uncertainty, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, interpretation supersession, source update, geometry correction, rights update, and rollback lineage. |
| `quality_flags` | Missing evidence, unsupported correlation, missing vertical datum, undisclosed exaggeration, source-role conflict, rights unknown, sensitivity unknown, stale interpretation, or incomplete release refs. |

---

## Section classes

| Class | Meaning | Default posture |
|---|---|---|
| `source_section` | Section copied or referenced from source publication/dataset. | Preserve source edition, rights, and figure/panel identity. |
| `interpreted_panel` | KFM-assembled or steward-reviewed interpretation. | Requires interpretation version and evidence refs. |
| `schematic_panel` | Simplified/teaching/public diagram. | Requires reality-boundary note and caveats. |
| `measured_section` | Field-measured section or log-like vertical profile. | Observed evidence where method/date/source resolve. |
| `model_derived_section` | Slice through model or interpolated surface. | Modeled, not observed; uncertainty and version required. |
| `public_derivative` | Released public-safe section view. | Requires release manifest and rollback target. |
| `candidate_record` | Unreviewed import or unresolved section row. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated or hypothetical section panel. | Reality-boundary disclosure; not source evidence. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | CrossSection posture |
|---|---|---|
| Published map plate, report figure, KGS/USGS section | `aggregate` or `administrative` with source evidence | Source-authored interpretation; preserve edition and caveats. |
| Measured section, borehole tie, core interval, observed contact | `observed` | Evidence input, not automatically the entire panel truth. |
| Correlated horizons, interpolated contacts, model slices | `modeled` | Interpretation/model output with method/version/uncertainty. |
| Generalized educational/display panel | `synthetic` or `aggregate` | Public-friendly carrier, not canonical observed truth. |
| Unreviewed digitized section, OCR figure extraction, unresolved source plate | `candidate` | Quarantine until source, geometry, and rights resolve. |

Source role applies to the section and to each evidence family it cites. A modeled surface cannot be worded into an observed contact.

---

## Reality boundary

A `CrossSection` must make its interpretation boundary visible.

Required disclosures when applicable:

- vertical exaggeration;
- datum and units;
- section trace and corridor width;
- which features are observed, interpreted, modeled, generalized, or schematic;
- evidence inputs and missing evidence gaps;
- interpretation version and supersession state;
- public-safe generalization or redaction;
- whether the rendered panel is source-authored, KFM-assembled, or synthetic.

A public or AI-facing explanation should cite evidence and state the boundary instead of presenting the panel as direct subsurface truth.

---

## Sensitivity and release

Cross sections may combine many lower-risk inputs into a higher-risk subsurface interpretation. The safe default is release gating with explicit public-safe projection.

Rules:

- Exact restricted subsurface inputs remain behind governed access.
- Public derivatives should remove, generalize, or summarize source-limited details while preserving caveats.
- Source rights and figure/media permissions must be checked before public reproduction.
- Public evidence/citation projections must not reveal restricted source details.
- Public outputs must preserve interpretation version, evidence basis, uncertainty, vertical exaggeration, source role, and caveats.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source figures, panels, coordinates, trace lines, digitized linework, well ties, logs, cores, geophysics, and metadata remain source-bound. |
| WORK / QUARANTINE | Candidate sections are normalized, source-role checked, rights/sensitivity-screened, geometry/datum checked, evidence-linked, and quarantined on ambiguity. |
| PROCESSED | Reviewed sections receive deterministic identity, interpretation version, trace/panel refs, evidence refs, uncertainty posture, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, evidence, interpretation version, reality boundary, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision, review record, representation/redaction receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released public-safe section derivatives appear in public clients. |
| CORRECTION | Source update, interpretation supersession, datum correction, evidence withdrawal, rights change, or rendering error triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for source section, interpreted panel, schematic panel, measured section, model-derived section, candidate record, and public-safe derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing interpretation version, missing section trace, missing vertical datum, undisclosed vertical exaggeration, unsupported correlation, direct public restricted inputs, missing reality-boundary note, missing policy decision, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, section trace, panel geometry, vertical datum, exaggeration, source role, interpretation version, evidence refs, uncertainty, rights state, sensitivity state, policy refs, release refs, and correction refs.
- [ ] Add policy/access tests proving public clients consume released derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for interpretation supersession, datum correction, evidence withdrawal, rights update, figure redaction, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, interpretation boundary is clear, policy allows, derivative is released | `ANSWER` / public-safe derivative may be shown |
| Evidence, rights, source role, geometry, datum, interpretation, or uncertainty support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, or release is absent | `DENY` |
| Schema, validator, source-read, rendering, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns CrossSection and preserves adjacent-domain ownership boundaries. | Records broader naming drift. |
| Geology object-family doc | Confirms CrossSection purpose, proposed key fields, time posture, and vertical-exaggeration / reality-boundary requirements. | Field realization remains PROPOSED. |
| Cross-sections pipeline README | Confirms cross-section processing is interpretive, release-gated, evidence-bound, and executable support only. | Does not prove runtime behavior. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized CrossSection weakens source integrity, hides interpretation status, misstates source role, crosses adjacent-domain ownership, exposes restricted detail, or depends on superseded evidence, geometry, rights, or release decisions.

Rollback triggers include:

- interpretation version superseded or withdrawn;
- section trace, vertical datum, vertical exaggeration, or panel geometry corrected;
- borehole, well log, core, geophysics, unit, interval, or structure evidence withdrawn or corrected;
- public derivative lacks reality-boundary note, receipt, policy decision, release manifest, or rollback target;
- rendered panel or AI explanation presents modeled/inferred contacts as observed fact;
- source rights change or source figure reproduction is no longer allowed;
- release manifest points to RAW/WORK/QUARANTINE or restricted source instead of public-safe derivative.

Rollback artifacts should include affected CrossSection IDs, section trace refs, panel refs, interpretation version refs, evidence refs, linked unit/interval/borehole/log/core/geophysics refs, public derivative IDs, release IDs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| What is the accepted paired schema path and casing for `CrossSection`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Should section trace and panel geometry be one object or linked companion objects? | PROPOSED / NEEDS VERIFICATION | Schema and fixture review. |
| What is the canonical receipt family for rendered/schematic/vertical-exaggerated sections? | NEEDS VERIFICATION | RepresentationReceipt / RedactionReceipt policy review. |
| Which source figures or section panels may be reproduced publicly? | NEEDS VERIFICATION | Source registry, rights review, and release fixtures. |
| How should uncertainty bands and unsupported gaps be represented in public UI? | NEEDS VERIFICATION | UI/API projection and validation review. |
| How should Hydrology context appear without becoming Hydrology measurement truth? | NEEDS VERIFICATION | Cross-lane policy and Hydrology steward review. |

---

## Related contracts and docs

- `contracts/domains/geology/BoreholeReference.md` — borehole/well evidence and location posture.
- `contracts/domains/geology/CoreSample.md` — core/cuttings/sample evidence.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and CrossSection semantics.
- `pipelines/domains/geology/cross_sections/README.md` — executable processing orientation; not semantic authority.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.

---

## Maintainer checklist

- [ ] Create or verify paired schema and fixtures.
- [ ] Add validation for interpretation version, reality boundary, vertical datum, vertical exaggeration, and evidence closure.
- [ ] Add policy tests for restricted/internal vs public-safe derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe section derivatives.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved path/schema/receipt drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
