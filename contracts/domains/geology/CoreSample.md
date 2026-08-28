<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-core-sample
title: CoreSample Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Boreholes and wells steward
  - OWNER_TBD — Core/sample steward
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
policy_label: restricted-by-default; semantic-contract; geology; core-sample; subsurface-sample-evidence; custody-aware; source-role-aware; release-gated; metadata-public-only
tags: [kfm, contracts, geology, CoreSample, core, cuttings, sample, borehole, subsurface, custody, depth-interval, lithology, geochemistry, evidence, source-role, sensitivity, policy, release, correction, rollback]
related:
  - ./README.md
  - ./BoreholeReference.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../../docs/domains/geology/sublanes/README.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../pipelines/domains/geology/boreholes/README.md
  - ../../../schemas/contracts/v1/domains/geology/CoreSample.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology CoreSample semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/CoreSample.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "CoreSample appears in the Geology owns-list and object-family reference, while a CoreSampleReference reference-form is explicitly marked NEEDS VERIFICATION in boreholes-wells doctrine. This contract preserves the requested CoreSample path and surfaces the reference-form question."
  - "CoreSample is physical subsurface sample evidence. It does not replace BoreholeReference, Well LogReference, Lithology, GeochemistrySampleReference, StratigraphicInterval, custody records, or public-safe released derivatives."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CoreSample — Geology

> Semantic contract for Geology `CoreSample`: the evidence-bound object for physical core, cuttings, sample intervals, custody/context records, and derived descriptions used to support geology claims without becoming borehole truth, well-log truth, ownership proof, resource proof, or public exact-location truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: CoreSample" src="https://img.shields.io/badge/object-CoreSample-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: sample evidence not release approval" src="https://img.shields.io/badge/boundary-sample__evidence__not__release__approval-critical">
</p>

`contracts/domains/geology/CoreSample.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Sample classes](#sample-classes) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/CoreSample.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/CoreSample.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Core Sample` / `CoreSample` as a Geology object family, while reference-form naming remains **NEEDS VERIFICATION**. Field-level schema shape, fixtures, validators, policy runtime, source registry records, release workflow, API behavior, UI behavior, custody handling, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `CoreSample` is physical sample evidence. It does **not** certify the borehole identity, does **not** replace `BoreholeReference`, does **not** replace `Well LogReference`, does **not** prove a resource estimate, does **not** create Hydrology measurements, and does **not** authorize public exposure of restricted location, depth, custody, proprietary, or source-limited material by itself.

---

## Meaning

`CoreSample` is the Geology semantic object for physical or documented subsurface material associated with a borehole-like source record. It may represent core, cuttings, chips, sidewall core, split sample, archived sample, lab subsample, cataloged sample, interval description, image-backed sample, or custody-linked sample record.

It answers:

- Which physical or documented sample is being referenced?
- Which borehole, interval, source, custody context, collection time, description, image, analysis, and evidence support apply?
- Which lithology, stratigraphic interval, geochemistry, or cross-section claims may cite this sample as evidence?
- What rights, sensitivity, location/depth precision, custody, and public-safe representation govern use?
- Which policy decision, review record, receipt, release manifest, correction notice, and rollback target govern downstream use?

A core sample can support geology interpretation. It is not itself a unit boundary, a well log, a reserve/production claim, or a public artifact.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Core/sample meaning | `contracts/domains/geology/CoreSample.md` | Owned here |
| Borehole identity | `contracts/domains/geology/BoreholeReference.md` | Parent or related borehole reference; distinct identity |
| Machine schema shape | `schemas/contracts/v1/domains/geology/CoreSample.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Human-facing sublane doctrine | `docs/domains/geology/sublanes/boreholes-wells.md` | Governs boreholes/wells/core sample posture |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Records CoreSample purpose and sensitivity posture |
| Scope boundary | `docs/domains/geology/SCOPE.md` | Confirms Geology owns core samples but not adjacent-domain truth |
| Pipeline logic | `pipelines/domains/geology/boreholes/README.md` | Executable processing/handoff support only |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, restricted, and public-safe proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/CoreSample.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/CoreSample.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `CoreSample` preserved because the user requested this path and Geology docs use this object-family spelling |
| Reference-form posture | `CoreSampleReference` is not yet confirmed as an accepted object family |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `CoreSample` should semantically assert:

1. **Sample identity** — deterministic identity for the physical core, cutting, chip, sidewall core, interval, subsample, image, or source sample record.
2. **Source identity** — SourceDescriptor, source record ID, source role, source vintage, rights, cadence, and attribution.
3. **Borehole linkage** — `BoreholeReference` or source-native borehole/well reference without collapsing sample and borehole identity.
4. **Interval support** — depth interval, depth datum, units, measured depth / true vertical depth posture, and uncertainty where source-supported.
5. **Material support** — lithology, stratigraphic, geochemistry, fossil, physical-property, or descriptive support with method and uncertainty.
6. **Custody posture** — repository, accession, box/tray, archive, lab, chain-of-custody, image/media, or source-native custody context where available.
7. **Sensitivity posture** — location/depth precision, source rights, proprietary analysis, private context, restricted repository notes, or public-safe status.
8. **Evidence linkage** — links to images, labels, logs, descriptions, analyses, field notes, EvidenceRefs, and EvidenceBundles.
9. **Derived-use posture** — lithology, stratigraphy, geochemistry, cross-section, resource, or public-map uses with caveats.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a sample as the borehole identity | A sample references a borehole; it does not replace the borehole reference. |
| Treating a sample as a well log | Logs, curves, and interpreted tops are separate evidence classes. |
| Treating one sample as a mapped unit boundary | A sample can support interpretation; it does not by itself redraw a unit. |
| Treating an assay or description as a resource estimate | Resource estimates require separate modeled/estimate governance. |
| Publishing restricted location or depth context by default | Public derivatives require governed review and public-safe representation. |
| Treating a lab result as Hydrology measurement truth | Hydrology owns water measurements; CoreSample may provide geology context. |
| Removing custody/provenance | Sample utility depends on source, repository, interval, and custody context. |
| Treating a pipeline candidate as catalog truth | Candidates require validation, evidence, policy, review, and promotion. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM core/sample identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `CoreSample` or accepted canonical synonym after naming reconciliation. |
| `sample_class` | Core, cuttings, chips, sidewall core, archived sample, lab subsample, image record, candidate, or source-native class. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Administrative, observed, aggregate, modeled, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native sample, accession, catalog, interval, or analysis ID. |
| `borehole_ref` | Linked `BoreholeReference` or source-native borehole reference. |
| `well_log_refs` | Linked well log references, when applicable. |
| `depth_interval` | Top/base interval and units. |
| `depth_datum` | Ground surface, Kelly bushing, sea level, source-native datum, or unknown. |
| `interval_uncertainty` | Depth/interval uncertainty and method caveat. |
| `sample_material` | Core, cutting, chip, sediment, rock, fossiliferous material, fluid-bearing material, or source-native descriptor. |
| `lithology_refs` | Linked lithology descriptions or vocabulary refs. |
| `stratigraphic_interval_refs` | Linked intervals or picks supported by this sample. |
| `geochemistry_sample_refs` | Linked geochemistry analysis references, when applicable. |
| `image_refs` | Public-safe or restricted images/media refs. |
| `custody_ref` | Repository, accession, archive, lab, box/tray, or custody record ref. |
| `collection_time` | Collection, drilling, recovery, or sample time when known. |
| `source_time` | Source assertion or publication time. |
| `retrieval_time` | Time KFM retrieved the record. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `location_ref_internal` | Access-controlled related borehole/sample location ref, if modeled separately. |
| `public_geometry_ref` | Generalized/aggregated public-safe geometry reference, if released. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `sensitivity_state` | Restricted, metadata-public, generalized-public, withheld, rights-limited, public-safe, or unknown. |
| `policy_decision_ref` | Policy result governing use or release. |
| `review_record_ref` | Source, geology, custody, sensitivity, or release review. |
| `redaction_receipt_ref` | Required when sample location/fields/media are generalized or withheld for public output. |
| `validation_report_ref` | Validation report for schema, custody, interval, source-role, sensitivity, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, interval correction, custody correction, rights update, and rollback lineage. |
| `quality_flags` | Source-role conflict, identity collision, missing borehole ref, depth/datum missing, custody unknown, rights unknown, sensitivity unknown, stale source, or incomplete evidence. |

---

## Sample classes

| Class | Meaning | Default posture |
|---|---|---|
| `whole_core` | Continuous or partial core interval. | Evidence-bearing; exact location/depth context reviewed before public use. |
| `cuttings` | Drilling cuttings or chips tied to interval/depth. | Evidence-bearing with interval/mixing caveats. |
| `sidewall_core` | Sidewall sample tied to borehole interval. | Evidence-bearing; interval precision must be explicit. |
| `archived_sample` | Repository or catalog sample record. | Custody and rights posture are material. |
| `lab_subsample` | Subsample used for analysis. | Links to parent sample and method. |
| `image_record` | Image/media of core/sample/box/label. | Media rights and public projection reviewed separately. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `public_derivative` | Released metadata/generalized sample representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | CoreSample posture |
|---|---|---|
| Repository catalog, accession table, box inventory | `administrative` | Identifies custody/status context; not a geology interpretation by itself. |
| Core description, cuttings description, measured interval, lab observation | `observed` | Evidence-bearing record; preserve method, time, interval, and uncertainty. |
| Compiled sample index, county inventory, public rollup | `aggregate` | Aggregate support only; not exact sample detail unless source row resolves. |
| Interpreted facies, modeled interval, inferred correlation | `modeled` | Must remain interpretation/model output with method and uncertainty. |
| Unreviewed import, fuzzy match, unmatched catalog row | `candidate` | Quarantine until identity, borehole link, and rights resolve. |
| AI-generated or reconstructed sample description | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Sensitivity and release

Core samples can expose subsurface location, depth, custody, source-rights, interpretation, or adjacent-domain risk. The safe default is controlled internal use with reviewed public-safe metadata only where release permits.

Rules:

- Exact/internal point and interval context is not a normal public artifact.
- Public derivatives should use metadata-only, generalized, or aggregated views with clear caveats, where approved.
- Public evidence/citation projections must not reveal restricted source details.
- Rights, custody, source terms, and source-role ambiguity trigger quarantine, abstain, deny, or review rather than publication.
- Public outputs must preserve source role, sample class, interval uncertainty, method, rights, and interpretation caveats.
- Any derivative used by map/API/UI/AI surfaces needs EvidenceBundle support, policy decision, review, release manifest, correction path, and rollback target.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native sample rows, images, labels, interval descriptions, custody records, lab records, and media remain source-bound. |
| WORK / QUARANTINE | Candidate records are normalized, source-role checked, borehole-linked, rights/custody-screened, interval/datum-checked, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, source support, borehole/interval support, custody posture, evidence refs, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, temporal support, interval precision, custody, evidence, access state, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy decision, review record, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released metadata/generalized/aggregated public-safe derivatives appear in public clients. |
| CORRECTION | Source update, identity merge/split, interval correction, borehole link correction, custody correction, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve whether `CoreSample` remains the canonical contract name or needs a reference-form companion.
- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for whole core, cuttings, sidewall core, archived sample, lab subsample, image record, candidate import, and public metadata/generalized derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing source role, missing borehole ref, missing depth interval, unresolved datum, custody unknown, rights unknown, restricted detail in public output, missing policy decision, missing receipt, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source keys, borehole refs, interval/datum, custody refs, media rights, temporal support, source role, evidence refs, policy refs, release refs, and correction refs.
- [ ] Add policy/access tests proving public clients consume released derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, schema rename, identity merge/split, interval correction, custody correction, rights update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, source role is clear, policy allows, derivative is released | `ANSWER` / public-safe derivative may be shown |
| Evidence, rights, source role, identity, interval, custody, or interpretation support is incomplete | `ABSTAIN` |
| Restricted detail would be exposed, rights deny use, or release is absent | `DENY` |
| Schema, validator, source-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns core samples and does not own adjacent-domain truth. | Records broader naming drift. |
| Geology object-family doc | Confirms CoreSample purpose, intrinsic-key proposals, sensitivity posture, and relationship to boreholes. | Field realization remains PROPOSED. |
| Boreholes-wells sublane doc | Confirms core/cuttings are part of borehole/well evidence and that reference-form naming needs verification. | Human-facing doctrine, not schema enforcement. |
| Boreholes pipeline README | Confirms pipeline separation and that core/cuttings descriptions are linked evidence, not borehole-owned truth. | Does not prove runtime behavior. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized CoreSample claim weakens source integrity, misstates source role, crosses adjacent-domain ownership, exposes restricted detail, or depends on superseded identity, interval, custody, rights, or release evidence.

Rollback triggers include:

- object-family name/casing is superseded by ADR or schema decision;
- source sample record is corrected, withdrawn, merged, or split;
- borehole linkage is corrected;
- depth interval or datum is corrected;
- custody, repository, accession, or media rights are corrected;
- linked log, lithology, stratigraphy, or geochemistry evidence is withdrawn or corrected;
- public layer/API/UI uses an unreleased internal record;
- release manifest lacks receipt, policy decision, correction path, or rollback target.

Rollback artifacts should include affected CoreSample IDs, source record IDs, borehole refs, interval refs, custody refs, media refs, public derivative refs, linked BoreholeReference / Well LogReference / Lithology / StratigraphicInterval / Geochemistry refs, evidence refs, policy decisions, receipts, release IDs, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `CoreSample` the canonical contract name, or should a `CoreSampleReference` contract also exist? | NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted paired schema path and casing? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which sample/custody keys are safe and stable enough for deterministic identity? | NEEDS VERIFICATION | Source registry and fixture review. |
| How should core/cuttings intervals reference boreholes without collapsing identities? | NEEDS VERIFICATION | Companion contract and schema references. |
| Which media/image/custody fields may be public? | NEEDS VERIFICATION | Source rights, policy, and release fixture review. |
| How should geochemistry and lithology analysis refs attach without duplicating those object families? | NEEDS VERIFICATION | Cross-contract schema and validation review. |

---

## Related contracts and docs

- `contracts/domains/geology/BoreholeReference.md` — borehole/well reference identity and location posture.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and naming drift.
- `docs/domains/geology/sublanes/boreholes-wells.md` — human-facing boreholes/wells/core-sample sublane doctrine.
- `pipelines/domains/geology/boreholes/README.md` — executable processing orientation; not semantic authority.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.

---

## Maintainer checklist

- [ ] Resolve `CoreSample` / `CoreSampleReference` naming and schema path.
- [ ] Create or verify paired schema and fixtures.
- [ ] Add policy tests for restricted/internal vs public-safe derivative access.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released metadata/generalized/aggregated derivatives.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved naming/path/schema drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
