<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-well-log-reference
title: WellLogReference Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Boreholes/wells steward
  - OWNER_TBD — Subsurface data steward
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
policy_label: restricted-by-default; semantic-contract; geology; well-log-reference; borehole-attached; LAS-rights-controlled; source-role-aware; release-gated; references-only-public
tags: [kfm, contracts, geology, WellLogReference, WellLog, well-log, LAS, borehole-reference, subsurface, log-curves, interpreted-tops, depth-interval, evidence, source-role, sensitivity, rights, policy, release, correction, rollback]
related:
  - ./README.md
  - ./BoreholeReference.md
  - ./CoreSample.md
  - ./StratigraphicInterval.md
  - ./Lithology.md
  - ./GeologicUnit.md
  - ./HydrostratigraphicUnit.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/well_log_reference.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology WellLogReference semantic contract."
  - "A lower-case schema scaffold exists at schemas/contracts/v1/domains/geology/well_log_reference.schema.json, while this requested contract path uses PascalCase. The schema's x-kfm.contract_doc points to contracts/domains/geology/well_log_reference.md, creating a casing/path drift that remains CONFLICTED / NEEDS VERIFICATION."
  - "WellLogReference means a LAS, digital, wireline, driller, tops, or related log artifact reference attached to a BoreholeReference. It does not replace BoreholeReference, CoreSample, Lithology, StratigraphicInterval, GeologicUnit, Hydrology measurement, ownership/title, or public release state."
  - "LAS payloads and exact source geometries are excluded from public release by default; public outputs should expose references, summaries, generalized/aggregated products, and receipts only when rights, sensitivity, validation, policy, release, correction, and rollback support are present."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# WellLogReference — Geology

> Semantic contract for Geology `WellLogReference`: the evidence-bound object for well-log artifacts, LAS/digital log references, log curves, interpreted tops, depth-indexed subsurface observations, source rights, public-safe references, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: WellLogReference" src="https://img.shields.io/badge/object-WellLogReference-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: reference not payload release" src="https://img.shields.io/badge/boundary-reference__not__payload__release-critical">
</p>

`contracts/domains/geology/WellLogReference.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Log classes](#log-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/WellLogReference.md`  
> **Schema posture:** a lower-case scaffold exists at `schemas/contracts/v1/domains/geology/well_log_reference.schema.json`; its `x-kfm.contract_doc` points to lower-case `contracts/domains/geology/well_log_reference.md`, while the current requested contract path is PascalCase  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Well Log` / `WellLogReference` as an owned subsurface object family for log artifacts attached to boreholes. Field-level schema shape, casing, fixtures, validators, source registry records, rights enforcement, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `WellLogReference` is a reference to a subsurface log artifact or interpreted log-derived evidence. It does **not** prove `BoreholeReference` identity, `CoreSample` identity, `Lithology`, `StratigraphicInterval`, `GeologicUnit`, `HydrostratigraphicUnit`, Hydrology measurement, ownership/title, lease/permit status, public layer release, or AI/UI truth by itself.

---

## Meaning

`WellLogReference` is the Geology semantic object for a well-log artifact or log-derived reference attached to a `BoreholeReference` or source-native borehole/well record.

It may reference LAS files, digital curve sets, wireline logs, driller logs, gamma-ray/resistivity/neutron/density logs, interpreted tops, depth-indexed picks, scanned log images, source-native log tables, or public-safe metadata summaries.

It answers:

- Which well-log artifact, curve set, interpreted tops set, source-native log, or public-safe reference is being asserted?
- Which borehole, source record, source role, artifact digest, log type, depth interval, rights posture, and evidence support apply?
- Which StratigraphicInterval, Lithology, GeologicUnit, CoreSample, GeochemistrySample, GeophysicalObservation, or HydrostratigraphicUnit may cite the log without collapsing identity?
- Is the record observed, modeled/interpreted, administrative, aggregate, candidate, synthetic, or public derivative?
- What can be shown publicly: reference metadata, generalized availability, derived summary, or nothing?
- Which validation report, policy decision, redaction/aggregation receipt, release manifest, correction notice, and rollback target govern downstream use?

A well log is evidence attached to a subsurface reference. It is not the borehole itself, not the raw payload release, not a public-safe map layer by default, and not a hydrology measurement unless the Hydrology lane owns and releases that measurement separately.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Well-log reference meaning | `contracts/domains/geology/WellLogReference.md` | Owned here by request; casing drift remains open |
| Machine schema shape | `schemas/contracts/v1/domains/geology/well_log_reference.schema.json` | CONFIRMED scaffold; field shape still empty / PROPOSED |
| Schema/contract casing drift | `WellLogReference.md` vs `well_log_reference.schema.json` and lower-case `x-kfm.contract_doc` | CONFLICTED / NEEDS VERIFICATION |
| Object-family naming drift | `Well Log` vs `Well LogReference` vs `WellLogReference` | CONFLICTED / ADR-class; do not treat as separate identities without ADR/schema decision |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms Well Log as a Geology-owned subsurface log series tied to a borehole and rights-controlled |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, proposed keys, material times, sensitivity posture, and source roles |
| Boreholes/wells sublane | `docs/domains/geology/sublanes/boreholes-wells.md` | Confirms deny-by-default exact point/payload posture and public generalized/aggregated derivatives |
| Borehole support | `contracts/domains/geology/BoreholeReference.md` | Well logs attach to borehole references; they do not replace borehole identity |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, rights, sensitive-geometry, payload-deny, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

A paired schema exists only as a lower-case scaffold and does not yet enforce fields.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/WellLogReference.md` |
| Confirmed schema path | `schemas/contracts/v1/domains/geology/well_log_reference.schema.json` |
| Schema status | `PROPOSED` scaffold with empty `properties` and `additionalProperties: true` |
| Schema title | `Well Log Reference` |
| Schema contract pointer | `contracts/domains/geology/well_log_reference.md` |
| Casing/path posture | CONFLICTED / NEEDS VERIFICATION; requested PascalCase contract exists, schema points lower-case contract path |
| Family-name posture | §10.B uses `Well Log`; §E/schema use `Well LogReference`; current contract path uses `WellLogReference` |
| Field-level enforcement | NEEDS VERIFICATION |

Until the casing, naming, and schema-field decision is resolved, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `WellLogReference` should semantically assert:

1. **Log-reference identity** — deterministic identity for the log artifact/reference, borehole ref, log type, artifact digest, source, role, temporal scope, and normalized digest.
2. **Borehole attachment** — linked `BoreholeReference` or source-native well/borehole ref, while preserving borehole identity as separate.
3. **Artifact support** — log artifact digest, source URI/ref, file/media type, curve set, scanned image, tops table, or source-native log record.
4. **Log type and depth support** — log class, depth interval, depth datum, measured-depth/true-vertical-depth posture, units, and uncertainty/caveats where supported.
5. **Observed vs interpreted posture** — observed log curves and interpreted tops/picks remain clearly separated.
6. **Source identity** — SourceDescriptor, source record ID, source role, source time, observed/acquisition time where known, rights, cadence, and attribution.
7. **Evidence linkage** — LAS file, digital log, source table, image, report, well top, cross-section, EvidenceRef, or EvidenceBundle.
8. **Sensitivity and rights posture** — exact geometry, private/proprietary well context, LAS payload access, public reference metadata, generalized availability, or withheld state.
9. **Temporal discipline** — source time, observed/log acquisition time, valid time where material, retrieval time, release time, and correction time remain distinct.
10. **Governance state** — validation, policy, review, redaction/aggregation, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a well log as borehole identity | BoreholeReference owns the drilled-location identity. The log attaches to it. |
| Treating a LAS payload as public by default | LAS/digital payloads are excluded from public release by default unless rights/release prove otherwise. |
| Treating interpreted tops as observed curves | Interpreted picks/tops are modeled/interpretive evidence and must be labeled. |
| Treating well logs as Hydrology measurements | Hydrology owns measurements such as levels, flow, water quality, or pumping data. |
| Treating log-derived lithology as Lithology truth without review | Lithology owns material-character descriptors; logs may support them. |
| Treating depth picks as StratigraphicInterval truth without review | Intervals own interval/bound semantics; logs may support them. |
| Treating exact well/log geometry as public by default | Exact subsurface point geometry is restricted or generalized by default. |
| Treating log availability as ownership/title/permit proof | People/Land or regulatory/legal roots own those claims. |
| Treating public aggregate availability as exact log access | Public summaries are derivatives with caveats. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM well-log-reference identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `WellLogReference` or accepted canonical spelling after casing/path reconciliation. |
| `log_reference_id` | Source-native or KFM log reference identifier. |
| `borehole_ref` | Linked BoreholeReference or source-native borehole/well ref. |
| `log_class` | LAS, wireline, driller, image, tops table, curve set, interpreted tops, source-native, candidate, or public derivative. |
| `log_type` | Gamma ray, resistivity, neutron, density, sonic, spontaneous potential, caliper, temperature, driller log, tops, or source-native type. |
| `source_log_type` | Source-native log type retained for audit. |
| `log_artifact_digest` | Stable digest for the referenced artifact or payload metadata. |
| `artifact_ref_internal` | Access-controlled source artifact ref, if retained. |
| `public_reference_ref` | Public-safe reference metadata, if released. |
| `payload_release_state` | Withheld, reference-only, rights-cleared-public, restricted, embargoed, proprietary, unknown. |
| `depth_interval` | Source-supported measured-depth / true-vertical-depth / interval range. |
| `depth_datum_ref` | Datum or reference elevation/depth system. |
| `depth_units_ref` | Units vocabulary/ref for depth values. |
| `curve_set_ref` | Curve inventory or curve metadata ref, not necessarily public payload. |
| `interpreted_top_refs` | Linked interpreted tops/picks when source-supported and labeled as interpreted. |
| `stratigraphic_interval_refs` | Linked StratigraphicInterval refs supported by the log. |
| `lithology_refs` | Linked Lithology refs supported by interpretation or description. |
| `geologic_unit_refs` | Linked GeologicUnit refs supported by interpretation. |
| `core_sample_refs` | Linked CoreSample refs for the same borehole/interval. |
| `geochemistry_sample_refs` | Linked GeochemistrySample refs for the same borehole/interval. |
| `cross_section_refs` | Linked CrossSection refs that use the log. |
| `hydrostratigraphic_refs` | Linked HydrostratigraphicUnit refs where log supports context. |
| `location_ref_internal` | Access-controlled exact/source point geometry ref inherited/linked through borehole. |
| `public_geometry_ref` | Generalized or aggregate public-safe geometry ref, if released. |
| `public_safe_geometry_fingerprint` | Stable fingerprint of released/generalized/aggregate geometry. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, administrative, aggregate, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native well-log, LAS, tops, image, table, report, or database record. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Log acquisition, drilling, recording, or observation time, where material. |
| `valid_time` | Time interval for interpreted log-derived claims, where applicable. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe reference/derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, embargo, proprietary, or source-term posture. |
| `sensitivity_state` | Reference-only, generalized-public, aggregate-public, restricted-detail, private/proprietary, withheld, or unknown. |
| `policy_decision_ref` | Policy result governing use or release where material. |
| `review_record_ref` | Source, geology, borehole/well, sensitivity, rights, interpretation, or release review. |
| `redaction_receipt_ref` | Required when exact geometry or detail is generalized or withheld. |
| `aggregation_receipt_ref` | Required when log availability becomes an aggregate public product. |
| `validation_report_ref` | Validation report for schema, source role, rights, artifact digest, depth interval, geometry posture, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, artifact replacement, digest correction, borehole-link correction, tops correction, rights update, and rollback lineage. |
| `quality_flags` | Missing borehole ref, missing artifact digest, source-role conflict, observed/modelled collapse, rights unknown, exact geometry exposure risk, depth datum missing, stale source, or incomplete evidence. |

---

## Log classes

| Class | Meaning | Default posture |
|---|---|---|
| `las_reference` | LAS file or digital log payload reference. | Reference-only public by default; payload withheld unless rights/release allow. |
| `wireline_log` | Wireline/geophysical log reference or curve set. | Rights-controlled; exact borehole geometry restricted/generalized. |
| `driller_log` | Driller's log, descriptive interval table, or source-native drilling record. | Evidence-bearing; owner/privacy/source rights material. |
| `scanned_image_log` | Scanned log image or plate. | Rights and payload review required. |
| `interpreted_tops` | Tops/picks interpreted from logs. | Modeled/interpreted; not observed curves. |
| `curve_set_metadata` | Metadata-only public-safe curve inventory. | Public-safe only after rights/release review. |
| `aggregate_public_summary` | County/region/log-availability summary. | Public-safe only with aggregation release. |
| `candidate_record` | Unreviewed import or unresolved source row. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical log reference or interpreted trace. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released generalized/reference-only representation. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | WellLogReference posture |
|---|---|---|
| LAS/digital log curves from source repository | `observed` | Evidence-bearing log curves; payload access governed by rights and release. |
| Driller log or descriptive interval table | `observed` with source caveats | Evidence-bearing, often owner/privacy/right-sensitive. |
| Interpreted tops/picks from logs | `modeled` | Interpretation; never label as observed curve data. |
| Log catalog row or availability index | `administrative` | Identifies artifact/status; not curve/payload truth by itself. |
| Regional log availability summary | `aggregate` | Public-safe only with aggregation receipt/release support. |
| Unreviewed import, missing borehole ref, missing digest, rights unknown | `candidate` | Quarantine until identity, source role, rights, and attachment resolve. |
| AI-generated or hypothetical log/pick | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`WellLogReference` is a log artifact/reference, not the surrounding truth system.

```text
WellLogReference != BoreholeReference
WellLogReference != CoreSample
WellLogReference != GeochemistrySample
WellLogReference != Lithology
WellLogReference != StratigraphicInterval
WellLogReference != GeologicUnit
WellLogReference != HydrostratigraphicUnit
WellLogReference != Hydrology measurement
WellLogReference != ownership / lease / title proof
WellLogReference != public payload release
WellLogReference != AI summary
```

Any linkage must preserve source role, artifact digest, borehole attachment, depth semantics, rights, sensitivity, evidence, validation, release state, and correction lineage.

---

## Sensitivity and release

Well logs are restricted by default because they attach to exact subsurface locations and often carry rights-controlled LAS/digital payloads. Public release should prefer reference metadata, generalized/aggregated availability, or public-safe summaries unless rights, sensitivity review, validation, and release support prove a narrower release is allowed.

Rules:

- LAS/digital payloads are excluded from public release by default.
- Exact borehole/well/log geometry is restricted or generalized by default.
- Public derivatives require rights review, policy decision where material, redaction or aggregation receipt where needed, validation report, release manifest, correction path, and rollback target.
- Public outputs must preserve source role, source time, observed time where material, depth/datum caveats, artifact digest posture, rights posture, geometry precision, and public-payload caveats.
- Candidate, synthetic, rights-unknown, private/proprietary, stale, missing-borehole, missing-digest, or evidence-incomplete records must not enter public outputs as authoritative log facts.
- Log-derived tops, intervals, lithology, and hydrostratigraphy must not be displayed as direct observation unless the source-role and evidence support that narrow claim.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native LAS files, log images, log tables, tops, catalog rows, depth intervals, curve metadata, source notes, and rights terms remain source-bound. |
| WORK / QUARANTINE | Candidate log refs are normalized, borehole-linked, artifact-digested, source-role checked, depth/datum checked, rights/sensitivity-screened, geometry-generalization planned, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, borehole ref, artifact digest, log type, depth posture, evidence refs, rights state, sensitivity state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, source/observed/retrieval times, borehole attachment, artifact digest, depth/datum caveats, evidence, rights, and public-access posture preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, policy/review where material, redaction/aggregation receipt where needed, release manifest, and rollback target. |
| PUBLISHED | Only released reference metadata, generalized/aggregated availability, or rights-cleared derivatives appear in public clients. |
| CORRECTION | Source update, artifact replacement, digest correction, borehole-link correction, depth/datum correction, tops reinterpretation, rights change, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve naming drift between `Well Log`, `Well LogReference`, and `WellLogReference`.
- [ ] Resolve casing/path drift between `WellLogReference.md`, lower-case schema file, and lower-case schema `contract_doc` pointer.
- [ ] Expand `well_log_reference.schema.json` from scaffold into field-level validation, or record the accepted schema path via ADR/schema PR.
- [ ] Add valid fixtures for LAS reference, wireline log, driller log, scanned image log, interpreted tops, curve-set metadata, aggregate public summary, candidate import, synthetic example, and public reference derivative.
- [ ] Add invalid fixtures for missing borehole ref, missing source descriptor, missing artifact digest, observed/modelled collapse, interpreted tops labeled observed, exact geometry public without receipt, LAS payload public without rights/release, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, borehole ref, log type, artifact digest, source role, depth interval, datum, rights state, geometry posture, evidence refs, release refs, correction refs, and anti-collapse constraints.
- [ ] Add policy/access tests proving public clients consume reference-only or aggregate/generalized derivatives unless payload release is explicitly rights-cleared.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, artifact replacement, digest correction, borehole-link correction, depth/datum correction, tops correction, rights update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, borehole ref and artifact digest validate, rights/release allow public reference | `ANSWER` / public-safe log reference derivative may be shown |
| Evidence, source role, borehole ref, digest, rights, geometry, or release support is incomplete | `ABSTAIN` |
| Restricted payload/detail would be exposed, rights deny use, exact geometry would leak, or interpreted data is relabeled observed | `DENY` |
| Schema, validator, source-read, artifact-read, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Confirmed schema scaffold | Confirms lower-case schema file exists, is PROPOSED, and currently has empty properties. | Does not prove field validation; also exposes casing/path drift. |
| Geology object-family doc | Confirms WellLogReference/Well Log purpose, proposed keys, material times, sensitivity posture, source roles, and LAS public-release exclusion. | Field realization remains PROPOSED. |
| Geology scope doc | Confirms Well Log is Geology-owned for subsurface log series tied to a borehole, and rights-controlled. | Does not prove schema or implementation enforcement. |
| Boreholes/wells sublane doc | Confirms exact borehole/log/sample/private-well locations fail closed and public derivatives are generalized/aggregated only with receipts/review/policy. | The sublane path is itself marked PROPOSED and has naming drift notes. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized WellLogReference weakens source integrity, misstates source role, leaks restricted payload or exact geometry, hides rights state, or collapses log evidence into borehole/sample/lithology/interval/unit/Hydrology truth.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source log record corrected, withdrawn, replaced, or superseded;
- artifact digest, borehole ref, log type, depth interval, datum, or interpreted tops corrected;
- LAS/digital payload was exposed without rights/release support;
- exact well/log geometry was published without redaction/generalization support;
- interpreted tops/picks were labeled as observed curves;
- log was presented as Hydrology measurement, ownership/title proof, public release approval, or AI truth;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate records as public truth;
- public derivative lacks release manifest, correction path, or rollback target.

Rollback artifacts should include affected WellLogReference IDs, borehole refs, source record IDs, artifact digests, log-type refs, depth intervals, geometry refs, public derivative refs, linked interval/lithology/unit/hydrostratigraphy refs, release IDs, evidence refs, policy decisions, receipts, validation reports, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the canonical family name `Well Log`, `Well LogReference`, or `WellLogReference`? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| Should the contract file be PascalCase `WellLogReference.md` or lower-case `well_log_reference.md` to match the schema scaffold pointer? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| Which log-type vocabulary is canonical for LAS, wireline, driller, scanned, and tops records? | NEEDS VERIFICATION | Schema, source registry, and boreholes/wells steward review. |
| What rights classes allow public payload release versus reference-only public metadata? | NEEDS VERIFICATION | Policy, source registry, rights review, and fixture design. |
| How should log-derived tops attach to StratigraphicInterval without becoming interval truth? | NEEDS VERIFICATION | Cross-contract schema review. |
| How should MapLibre/AI surfaces show log availability without exposing exact coordinates or proprietary payloads? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/BoreholeReference.md` — drilled-location identity to which well logs attach.
- `contracts/domains/geology/CoreSample.md` — physical sample evidence from borehole/core context.
- `contracts/domains/geology/StratigraphicInterval.md` — interval/bounds claims supported by logs/tops.
- `contracts/domains/geology/Lithology.md` — material-character descriptors supported by log interpretation.
- `contracts/domains/geology/HydrostratigraphicUnit.md` — geology↔hydrology bridge context, not measurement ownership.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference, naming drift, and WellLogReference semantics.
- `docs/domains/geology/sublanes/boreholes-wells.md` — restricted borehole/well/log sublane posture.
- `schemas/contracts/v1/domains/geology/well_log_reference.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `policy/sensitivity/geology/` — expected sensitivity policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve Well Log / Well LogReference / WellLogReference naming drift.
- [ ] Resolve PascalCase vs lower-case contract/schema path drift.
- [ ] Expand paired schema and fixtures.
- [ ] Add validation for borehole ref, log type, artifact digest, source role, depth interval, rights state, geometry posture, and evidence refs.
- [ ] Add anti-collapse tests for well-log/borehole/core-sample/lithology/interval/geologic-unit/hydrology-measurement/public-payload/UI-summary distinctions.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released reference-only or aggregate/generalized derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved casing/path/schema/source-role/rights drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
