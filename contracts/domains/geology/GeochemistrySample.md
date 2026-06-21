<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-geochemistry-sample
title: GeochemistrySample Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Geochemistry steward
  - OWNER_TBD — Natural-resources steward
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
policy_label: restricted-by-default; semantic-contract; geology; geochemistry-sample; analyte-evidence; custody-aware; source-role-aware; release-gated; public-generalized-only
tags: [kfm, contracts, geology, GeochemistrySample, geochemistry, sample, analyte, assay, analytical-method, sample-medium, custody, resource-context, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./CoreSample.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/geochemistry.md
  - ../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/GeochemistrySample.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology GeochemistrySample semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/GeochemistrySample.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "Geology doctrine contains naming drift between Geochemistry Sample and GeochemistrySampleReference. This contract preserves the requested GeochemistrySample path while surfacing the drift."
  - "GeochemistrySample is sample/analyte evidence. It does not prove a mineral occurrence, resource deposit, resource estimate, extraction site, hazards risk, hydrology measurement, or public release by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GeochemistrySample — Geology

> Semantic contract for Geology `GeochemistrySample`: the evidence-bound object for geochemical sample and analysis references, analyte sets, sample media, analytical methods, custody/time separation, public-safe derivatives, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: GeochemistrySample" src="https://img.shields.io/badge/object-GeochemistrySample-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: assay not resource proof" src="https://img.shields.io/badge/boundary-assay__not__resource__proof-critical">
</p>

`contracts/domains/geology/GeochemistrySample.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Sample classes](#sample-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/GeochemistrySample.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/GeochemistrySample.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Geochemistry Sample` as an owned object family, while `GeochemistrySampleReference` appears as a reference-form spelling in the conflicted object roster. Field-level schema shape, fixtures, validators, policy runtime, source registry records, release workflow, API behavior, UI behavior, analyte vocabulary, method vocabulary, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `GeochemistrySample` is sample/analysis evidence. It does **not** prove a `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, `ExtractionSite`, production claim, reserve claim, hydrology measurement, hazards risk, or public release by itself.

---

## Meaning

`GeochemistrySample` is the Geology semantic object for a geochemical sample, analysis reference, assay row, lab result, sample-medium observation, analyte set, analytical method, or public-safe derivative used as evidence in KFM geology and natural-resources workflows.

It answers:

- Which sample or analysis record is being referenced?
- Which sample medium, collection event, analytical method, lab/report, analyte set, unit, detection limit, uncertainty, and custody context apply?
- Which source record, source role, rights posture, collection time, analytical-report time, retrieval time, and correction time apply?
- Which mineral occurrence, resource deposit, resource estimate, extraction site, lithology, core sample, or map context may cite this evidence without collapsing identity?
- What public-safe geometry, analyte summary, or generalized derivative may be shown?
- Which policy decision, review record, redaction/aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

A geochemistry sample can support interpretation. It is not itself an economic finding, a resource estimate, a deposit boundary, a mine/extraction site, or a public artifact.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Geochemistry sample meaning | `contracts/domains/geology/GeochemistrySample.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/GeochemistrySample.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms owned family and adjacent-lane exclusions |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, keys, material times, sensitivity, and source role |
| Natural-resources doctrine | `docs/domains/geology/sublanes/natural_resources.md` | Confirms resource-context use and anti-collapse posture |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, and public-safe proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/GeochemistrySample.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/GeochemistrySample.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `GeochemistrySample` preserved because the user requested this path while Geology docs show both `Geochemistry Sample` and `GeochemistrySampleReference` forms |
| Naming drift | `Geochemistry Sample` / `GeochemistrySampleReference` remains CONFLICTED until ADR/schema decision |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `GeochemistrySample` should semantically assert:

1. **Sample identity** — deterministic identity for the sample, analysis record, assay row, lab result, or public derivative.
2. **Source identity** — SourceDescriptor, source record ID, source role, source vintage, rights, cadence, and attribution.
3. **Sample medium** — rock, soil/sediment, stream sediment, core/cuttings, water-associated material, concentrate, tailings, ore, mine waste, or source-native medium.
4. **Collection support** — collection event, observed/collection time, geometry, collector/program, and source-native sample ID where supported.
5. **Analytical support** — analytical method, lab/report, analyte set, units, detection limits, QA/QC, uncertainty, and analytical-report time.
6. **Custody/time separation** — collection time and analytical-report/source time remain distinct because collapsing them weakens chain-of-custody.
7. **Evidence linkage** — reports, tables, lab sheets, source datasets, sample catalogs, EvidenceRefs, and EvidenceBundles.
8. **Derived-use posture** — mineral occurrence, deposit, estimate, lithology, extraction, environmental context, or public-map uses with caveats.
9. **Sensitivity posture** — exact sample geometry, resource-sensitive detail, proprietary/right-limited data, cultural/environmental context, or public-safe derivative state.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating an assay as a resource estimate | Estimates require modeled/compiled assumptions and separate governance. |
| Treating a sample as a mineral occurrence | A sample can support occurrence evidence; it is not occurrence identity by itself. |
| Treating high analyte values as a deposit | Deposit identity remains separate and evidence-bound. |
| Treating a sample as an extraction site | Sites are physical/operational context, not chemical analysis rows. |
| Treating geochemistry as hydrology measurement | Hydrology owns water measurements; Geology may only hold geology-context sample evidence. |
| Treating source_time as collection time | Collection and analytical report times must remain separate. |
| Publishing exact sensitive coordinates by default | Public derivatives require review, redaction/generalization, and release. |
| Treating a lab report as public release approval | Publication requires release manifest, policy outcome, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM geochemistry sample identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `GeochemistrySample` or accepted canonical/reference-form synonym after naming reconciliation. |
| `sample_class` | Field sample, core/cuttings sample, stream-sediment sample, rock sample, soil/sediment sample, tailings/mine-waste sample, lab subsample, candidate, or source-native class. |
| `sample_id` | Source-native or KFM sample identifier. |
| `sample_medium` | Medium/material sampled. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native sample, analysis, assay, table, lab, or report record. |
| `collection_event_ref` | Collection event or field program ref, where available. |
| `location_ref_internal` | Access-controlled sample geometry ref. |
| `public_geometry_ref` | Generalized/aggregated public-safe geometry ref, if released. |
| `geometry_precision` | Exact, source precision, generalized, aggregate, withheld, unknown. |
| `coordinate_uncertainty` | Source/native/georeferenced uncertainty. |
| `collection_time` | Observed collection time. |
| `analysis_time` | Lab analysis time, if available. |
| `source_time` | Source report/publication/assertion time. |
| `retrieval_time` | Time KFM retrieved the record. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `analytical_method_ref` | Analytical method, lab method, instrument, or method vocabulary ref. |
| `lab_or_program_ref` | Lab/program/source organization ref, where available. |
| `analyte_set_ref` | Ref to analyte set or result table. |
| `analyte_results_summary` | Public-safe analyte summary, if permitted. |
| `units_ref` | Unit vocabulary/ref for reported values. |
| `detection_limit_refs` | Detection limit, censoring, or reporting limit refs. |
| `quality_control_refs` | QA/QC flags, blanks, duplicates, standard refs, or source-native quality flags. |
| `uncertainty_summary` | Analytical uncertainty, field uncertainty, source caveats, or method limitations. |
| `core_sample_refs` | Linked CoreSample refs where analysis uses core/cuttings. |
| `lithology_refs` | Linked Lithology refs where material characterization is supported. |
| `mineral_occurrence_refs` | Linked occurrence refs, if evidence supports relationship. |
| `resource_deposit_refs` | Linked deposit refs, if evidence supports relationship. |
| `resource_estimate_refs` | Linked estimate refs, if evidence supports relationship and caveats. |
| `extraction_site_refs` | Linked extraction-site refs, if evidence supports relationship. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Restricted, generalized-public, aggregate-public, rights-limited, resource-sensitive, public-safe, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release. |
| `review_record_ref` | Source, geology, geochemistry, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when sample geometry/fields/results are generalized or withheld for public output. |
| `aggregation_receipt_ref` | Required when samples become aggregate public products. |
| `validation_report_ref` | Validation report for schema, analyte units, method refs, source-role, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, analyte correction, unit correction, method correction, rights update, supersession, and rollback lineage. |
| `quality_flags` | Source-role conflict, identity collision, missing method, unit conflict, detection-limit issue, rights unknown, sensitivity unknown, custody gap, stale source, or incomplete evidence. |

---

## Sample classes

| Class | Meaning | Default posture |
|---|---|---|
| `field_sample` | Field-collected geochemistry sample. | Observed evidence when source, method, and time resolve. |
| `core_or_cuttings_sample` | Analysis of core/cuttings or subsurface material. | Link to CoreSample; exact location/depth reviewed. |
| `rock_sample` | Rock or outcrop sample. | Public posture depends on location and source rights. |
| `stream_sediment_sample` | Stream-sediment or related surficial sample. | Generalize where needed and preserve method. |
| `soil_or_sediment_sample` | Soil/sediment-context geochemistry sample. | Geology context only; Soil lane owns soil objects. |
| `tailings_or_mine_waste_sample` | Mine waste/tailings/contextual sample. | Sensitivity and public communication reviewed carefully. |
| `lab_subsample` | Lab-derived subsample/aliquot. | Link to parent sample and method. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `public_derivative` | Released generalized or aggregated representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | GeochemistrySample posture |
|---|---|---|
| Field sample with lab result and method | `observed` | Evidence-bearing record; preserve collection time, analysis time, method, units, and uncertainty. |
| Compiled geochemistry dataset, regional summary, public report table | `aggregate` | Aggregate/compiled support unless source sample row resolves. |
| Lab/catalog/sample inventory | `administrative` | Identifies sample/status context; not analysis truth by itself. |
| Interpolated geochemical surface or modeled anomaly | `modeled` | Derived interpretation; do not relabel as observed sample. |
| Permit/regulatory monitoring table | `regulatory` | Regulatory context; not necessarily geology observation unless supported. |
| Unreviewed import, unmatched assay row, unit conflict | `candidate` | Quarantine until identity, method, units, and rights resolve. |
| AI-generated or hypothetical geochemistry note | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`GeochemistrySample` is evidence, not the downstream conclusion.

```text
GeochemistrySample != MineralOccurrence
GeochemistrySample != ResourceDeposit
GeochemistrySample != ResourceEstimate
GeochemistrySample != ExtractionSite
GeochemistrySample != ProductionRecord
GeochemistrySample != ReserveClaim
GeochemistrySample != Hydrology measurement
GeochemistrySample != hazards risk
```

Any linkage must preserve source role, method, time, uncertainty, rights, sensitivity, evidence, and release state. High or anomalous analyte values can support review; they do not become an occurrence, deposit, estimate, reserve, or risk claim by identity equality.

---

## Sensitivity and release

Geochemistry sample records can expose exact sample coordinates, subsurface/depth context, resource-sensitive patterns, proprietary reports, environmental/cultural context, or rights-limited analytical data. The safe default is controlled internal use with reviewed public-safe derivatives.

Rules:

- Exact sample geometry is not automatically public.
- Public derivatives should use generalized points, aggregate summaries, analyte ranges/classes, or suppression where needed.
- Public outputs must preserve sample medium, method, units, collection time, analysis/source time, uncertainty, source role, rights posture, and caveats.
- Public evidence/citation projections must not leak restricted source details.
- Candidate, synthetic, rights-unknown, sensitivity-unknown, method-unknown, unit-conflicted, or evidence-incomplete records must not enter public outputs as authoritative sample facts.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native sample rows, analyte tables, units, methods, coordinates, lab reports, QA/QC fields, and source notes remain source-bound. |
| WORK / QUARANTINE | Candidate samples are normalized, method/unit checked, source-role checked, rights/sensitivity-screened, geometry-checked, analyte-mapped, and evidence-linked. |
| PROCESSED | Reviewed samples receive deterministic identity, source support, method/analyte support, temporal separation, geometry posture, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, collection/source/retrieval times, method, units, uncertainty, evidence, geometry precision, access state, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision, review record, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released generalized or aggregated public-safe derivatives appear in public clients. |
| CORRECTION | Source update, sample identity merge/split, unit conversion error, analyte correction, method correction, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve `Geochemistry Sample` vs `GeochemistrySampleReference` vs `GeochemistrySample` naming through ADR, schema PR, or drift-register decision.
- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for field sample, core/cuttings sample, rock sample, stream-sediment sample, soil/sediment sample, tailings/mine-waste sample, lab subsample, candidate import, and public aggregate derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, missing method, unit conflict, missing analyte set, collection/source time collapse, sample treated as occurrence/deposit/estimate, exact sensitive public geometry, missing policy decision, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source keys, sample medium, analyte units, method refs, detection limits, QA/QC, temporal separation, source role, evidence refs, policy refs, release refs, correction refs, and anti-collapse constraints.
- [ ] Add policy/access tests proving public clients consume released derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, identity merge/split, unit conversion correction, analyte correction, method correction, rights update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, method/units validate, source role is clear, policy allows, derivative is released | `ANSWER` / public-safe derivative may be shown |
| Evidence, rights, source role, sample identity, method, units, or geometry support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, or release is absent | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns Geochemistry Sample and excludes hydrology, hazards, title, and UI/AI truth. | Records broader naming drift and field realization remains PROPOSED. |
| Geology object-family doc | Confirms GeochemistrySampleReference / Geochemistry Sample purpose, proposed key fields, material-time separation, sensitivity posture, and source role. | Does not prove schema or validator enforcement. |
| Natural Resources sublane doc | Confirms geochemistry can support resource characterization when source role and use are declared, while anti-collapse boundaries remain required. | Docs-side sublane placement is itself PROPOSED. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized GeochemistrySample weakens source integrity, misstates source role, collapses sample evidence into resource claims, exposes restricted detail, or depends on superseded source, method, unit, analyte, rights, or release evidence.

Rollback triggers include:

- object-family name/casing is superseded by ADR or schema decision;
- source sample/analysis record corrected, withdrawn, merged, or split;
- analyte value, unit, detection limit, method, or QA/QC flag corrected;
- collection time, analysis time, source time, or retrieval time collapsed or corrected;
- sample treated as occurrence, deposit, estimate, extraction, reserve, hydrology measurement, or risk claim;
- public derivative exposes restricted detail or lacks a redaction/aggregation receipt;
- release manifest lacks policy decision, correction path, or rollback target;
- public API/UI/AI reads RAW/WORK/QUARANTINE or internal records as public truth.

Rollback artifacts should include affected GeochemistrySample IDs, source record IDs, analyte/result refs, method refs, unit refs, geometry refs, linked occurrence/deposit/estimate/extraction/context refs, public derivative refs, release IDs, evidence refs, policy decisions, receipts, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `GeochemistrySample` or `GeochemistrySampleReference` the accepted contract name? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted paired schema path and casing? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which analyte/unit/method vocabularies are canonical for KFM? | NEEDS VERIFICATION | Schema, source, and geochemistry steward review. |
| Which public analyte summaries are safe for resource-sensitive areas? | NEEDS VERIFICATION | Policy and release fixture review. |
| How should geochemistry results attach to CoreSample without duplicating custody or depth semantics? | NEEDS VERIFICATION | Cross-contract schema and fixture review. |
| How should GeochemistrySample support Natural Resources without becoming ResourceEstimate? | NEEDS VERIFICATION | Natural-resources ADR and anti-collapse tests. |

---

## Related contracts and docs

- `contracts/domains/geology/CoreSample.md` — core/cuttings/sample evidence that may carry geochemistry analysis.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and naming drift.
- `docs/domains/geology/sublanes/natural_resources.md` — Natural Resources sublane doctrine.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve `GeochemistrySample` / `GeochemistrySampleReference` naming and schema path.
- [ ] Create or verify paired schema and fixtures.
- [ ] Add anti-collapse tests for sample/occurrence/deposit/estimate/extraction/hydrology/risk distinctions.
- [ ] Add method, unit, detection-limit, and QA/QC validation fixtures.
- [ ] Add policy tests for restricted/internal vs public-safe derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released generalized or aggregated derivatives.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved naming/path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
