<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-crosswalk
title: Land Cover Crosswalk Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Crosswalk steward
  - OWNER_TBD — Classification-scheme steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; habitat; land-cover; crosswalk; CoverClassCrosswalk; class-scheme-aware; source-vintage-aware; evidence-bound; no-silent-recode; release-gated
tags: [kfm, contracts, habitat, land_cover, crosswalk, CoverClassCrosswalk, ClassSchemeProfile, class-scheme, land-cover-legend, nlcd, landfire, gap, nwi, cdl-adjacency, crosswalk-version, reviewer-state, evidence, source-role, policy, release, correction, rollback]
related:
  - ../../README.md
  - ./class_scheme.md
  - ./change_summary.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../fixtures/domains/habitat/land_cover/crosswalk/
  - ../../../../tests/domains/habitat/land_cover/crosswalk/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold into a Habitat land-cover CoverClassCrosswalk semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "The land-cover sublane names the object family CoverClassCrosswalk, while this requested file path and paired schema title use crosswalk/Crosswalk. This contract treats crosswalk.md as the current semantic contract for CoverClassCrosswalk unless a later ADR/schema decision says otherwise."
  - "A crosswalk is a reviewed, versioned, citable mapping between two ClassSchemeProfile records. It is not a class scheme, observation, source raster, renderer transform, change summary, public layer, or release authority by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Cover Crosswalk — Habitat

> Semantic contract for `CoverClassCrosswalk`: the Habitat land-cover object that records a reviewed, versioned, citable mapping between two `ClassSchemeProfile` records so observations, summaries, layers, and downstream Habitat products never rely on silent recodes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: CoverClassCrosswalk" src="https://img.shields.io/badge/object-CoverClassCrosswalk-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: crosswalk not renderer" src="https://img.shields.io/badge/boundary-crosswalk__not__renderer-critical">
</p>

`contracts/domains/habitat/land_cover/crosswalk.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Crosswalk classes](#crosswalk-classes) · [Mapping rules](#mapping-rules) · [Source-role rules](#source-role-rules) · [Change-summary and layer boundaries](#change-summary-and-layer-boundaries) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/land_cover/crosswalk.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Naming posture:** the land-cover sublane names the object family `CoverClassCrosswalk`; the requested path and schema title use `Crosswalk`. This file treats `crosswalk.md` as the current semantic contract for `CoverClassCrosswalk`, pending schema/ADR confirmation.  
> **Truth posture:** Habitat land-cover doctrine defines cover-class crosswalks as reviewed, citable mappings between class schemes, emitted as evidence and never as silent renderer transformations. Field-level schema shape, fixtures, validators, source registry records, policy files, release artifacts, API behavior, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `CoverClassCrosswalk` maps classes between schemes. It is **not** a `ClassSchemeProfile`, not a `LandCoverObservation`, not a `LandCoverChangeSummary`, not an ecological-system synthesis, not a source raster, not a renderer style, not a public layer, not a policy decision, and not a release manifest by itself.

---

## Meaning

`CoverClassCrosswalk` records an explicit, reviewed mapping between two versioned land-cover classification schemes.

It answers:

- Which source and target `ClassSchemeProfile` records are being mapped?
- Which class codes, labels, hierarchy levels, nodata/unknown values, and aggregate classes are involved?
- Is the mapping one-to-one, one-to-many, many-to-one, partial, lossy, probabilistic, conditional, aggregate, or advisory?
- Which evidence, reviewer state, method, source role, rights posture, uncertainty, and caveats support the mapping?
- Which `LandCoverObservation`, `LandCoverChangeSummary`, generalized layer, ecological-system synthesis, or downstream Habitat object may use the crosswalk?
- Which validation report, policy decision where material, release manifest, correction notice, and rollback target govern downstream use?

A crosswalk is an evidence-bearing transform descriptor. It does not change source truth. It only declares how a reviewed workflow may interpret one scheme in relation to another.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Crosswalk meaning | `contracts/domains/habitat/land_cover/crosswalk.md` | Owned here by request; object-family naming needs verification |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Source/target schemes | `contracts/domains/habitat/land_cover/class_scheme.md` | Crosswalk depends on reviewed class schemes; it does not replace them |
| Change summaries | `contracts/domains/habitat/land_cover/change_summary.md` | Summaries may cite crosswalks; they do not define them |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Defines class schemes, crosswalks, identity, lifecycle, and renderer/release boundaries |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, activation |
| Crosswalk policy | `policy/domains/habitat/land_cover/` | Expected review, allowed-use, threshold, and public-safety policy home; contents NEEDS VERIFICATION |
| Fixtures and tests | `fixtures/domains/habitat/land_cover/crosswalk/`, `tests/domains/habitat/land_cover/crosswalk/` | PROPOSED / NEEDS VERIFICATION |
| Executable logic | `pipelines/domains/habitat/land_cover/` | Expected transform/check implementation home; not this contract |
| Declarative specs | `pipeline_specs/habitat/land_cover/` | Expected config home; not this contract |
| Release | `release/manifests/habitat/` | Expected release/correction/rollback home; release instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Crosswalk` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/sublanes/land_cover.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `CoverClassCrosswalk` should semantically assert:

1. **Crosswalk identity** — deterministic identity from `from_scheme_id + to_scheme_id + crosswalk_version + reviewer_state`.
2. **Directionality** — source scheme and target scheme are explicit; reverse use is not implied unless separately reviewed.
3. **Version pinning** — both schemes and the crosswalk version are immutable once published; corrections create lineage.
4. **Mapping inventory** — every source class is mapped, held, denied, unknown, nodata, partial, aggregate, or explicitly unmapped.
5. **Mapping confidence** — one-to-one, one-to-many, many-to-one, partial, lossy, probabilistic, conditional, or advisory posture is explicit.
6. **Source-role preservation** — mapping a class does not upgrade a source product from modeled to observed, observation to regulation, or adjacency to Habitat truth.
7. **Evidence binding** — source legends, reviewer notes, method refs, source docs, EvidenceRef/EvidenceBundle refs, and artifact digests support the mapping.
8. **Use constraints** — allowed use in observations, change summaries, ecological-system synthesis, public layers, Focus Mode, or exports is explicit.
9. **Sensitivity and rights posture** — controlled-distribution labels, rare/sensitive habitat joins, or rights-limited schemes are not exposed without review.
10. **Governance state** — validation report, policy decision where material, review record, release/correction/rollback refs.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating crosswalk as class scheme | Schemes define vocabularies; crosswalks map between them. |
| Treating crosswalk as observation truth | Observations apply schemes to space/time; crosswalks only translate class semantics. |
| Treating crosswalk as silent renderer transform | Crosswalks must be reviewed, citable, and evidence-bound. |
| Treating reverse mapping as automatic | Direction matters; reverse crosswalk needs its own review or explicit bidirectional state. |
| Treating many-to-one mapping as lossless | Aggregation must carry loss/uncertainty caveats. |
| Treating CDL adjacency as Habitat cover | CDL remains Agriculture-owned unless governed adjacency says otherwise. |
| Treating ecological-system synthesis as crosswalk | Synthesis is downstream Habitat work and may need model receipts. |
| Treating public release as implied | ReleaseManifest, policy/review, correction, and rollback support are required. |
| Treating UI legend/color table as crosswalk | UI is downstream display, not transform authority. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM crosswalk ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized crosswalk digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `CoverClassCrosswalk`, pending naming confirmation. |
| `crosswalk_id` | Source/KFM crosswalk identifier. |
| `crosswalk_version` | Immutable crosswalk version. |
| `from_scheme_id` | Source/input ClassSchemeProfile ID. |
| `to_scheme_id` | Target/output ClassSchemeProfile ID. |
| `from_scheme_version` | Source/input scheme version. |
| `to_scheme_version` | Target/output scheme version. |
| `directionality` | Forward-only, bidirectional-reviewed, symmetric, inverse-derived, or unknown. |
| `reviewer_state` | Draft, reviewed, accepted, rejected, superseded, withdrawn, or accepted enum. |
| `mapping_table_ref` | Structured class-mapping table. |
| `mapping_table_digest` | Digest of mapping table. |
| `mapping_method_ref` | Method, rule, model, expert review, source guidance, or literature ref. |
| `mapping_kind` | One-to-one, one-to-many, many-to-one, aggregate, partial, probabilistic, conditional, advisory, denied, or unknown. |
| `lossiness_summary` | Public-safe statement of information loss or ambiguity. |
| `uncertainty_refs` | Crosswalk uncertainty or reviewer confidence refs. |
| `nodata_handling` | Nodata, unknown, unclassified, reserved, and deprecated class handling. |
| `class_coverage_summary` | Count/percent of mapped, unmapped, denied, partial, or ambiguous classes. |
| `allowed_use_cases` | Observations, summaries, layer legends, ecological-system input, research-only, steward-only, or accepted enum. |
| `denied_use_cases` | Use cases explicitly denied. |
| `source_descriptor_refs` | SourceDescriptor refs for schemes and review evidence. |
| `source_role_summary` | Source roles preserved through the mapping. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the mapping. |
| `validation_report_ref` | Validation report for schema, class coverage, directionality, evidence, and public safety. |
| `policy_decision_ref` | Policy decision where material. |
| `review_record_ref` | Steward/reviewer approval record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref where publicly surfaced. |
| `source_time` | Source publication/assertion time for scheme evidence. |
| `valid_time` | Valid interval for the crosswalk. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `correction_refs` | CorrectionNotice, supersession, replacement crosswalk refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing scheme, scheme-version mismatch, unmapped class, lossy mapping, direction conflict, source-role collapse, rights unknown, evidence incomplete, release missing. |

---

## Crosswalk classes

| Class | Meaning | Default posture |
|---|---|---|
| `scheme_to_scheme` | General mapping between two `ClassSchemeProfile`s. | Requires reviewed mapping table. |
| `legend_harmonization` | Harmonizes source legends for comparison or display. | Must preserve source labels and lossiness. |
| `summary_support` | Crosswalk used by `LandCoverChangeSummary`. | Must be versioned and cited in summary. |
| `ecological_system_input` | Crosswalk used to feed ecological-system synthesis. | Synthesis remains downstream owner; review/model receipt may be needed. |
| `public_layer_legend` | Crosswalk used to simplify a public layer legend. | Public-safe only after release and warnings. |
| `adjacency_context` | Crosswalk-like use of Agriculture/CDL or other adjacent-domain classes as context. | Must not re-own adjacent truth. |
| `sensitive_join_guard` | Mapping used in joins to sensitive Fauna/Flora context. | Fails closed unless policy/geoprivacy/release support exists. |
| `candidate_record` | Unreviewed/imported mapping. | WORK/QUARANTINE; no public edge. |
| `deprecated_or_superseded` | Older mapping retained for lineage. | No new public use unless explicitly allowed. |

---

## Mapping rules

- Crosswalks are directional unless `directionality` explicitly says otherwise and evidence/review supports it.
- Every source class must have an explicit mapping state: mapped, aggregated, split, partial, ambiguous, denied, nodata, unknown, unclassified, reserved, deprecated, or unmapped.
- Many-to-one mappings must carry lossiness and uncertainty caveats.
- One-to-many mappings must define allocation, conditional rules, or abstain from automated use.
- Nodata and unknown classes must not be silently treated as land cover.
- Crosswalks between source vintages must pin both scheme versions and source vintages where material.
- Crosswalks used in change summaries must be cited by `crosswalk_ref` and included in validation reports.
- Crosswalks used in public layers must be tied to release, artifact, legend, warning, correction, and rollback support.

---

## Source-role rules

| Source or mapping pattern | Required handling |
|---|---|
| NLCD ↔ GAP / LANDFIRE / NWI | Preserve both source schemes and source roles; no silent harmonization. |
| LANDFIRE EVT / BPS use | Keep vegetation/fuel/ecological context separate from species occurrence or fire-behavior prediction. |
| NWI wetland-class mapping | Treat as wetland observation/context, not regulatory delineation. |
| CDL adjacency mapping | CDL remains Agriculture-owned crop observation; no Habitat reclassification by convenience. |
| NatureServe ecological-system reference | Rights and sensitive joins fail closed until reviewed. |
| State inventory mapping | Authority/rights vary; review and source role required. |
| Model-derived mapping | Carries model/run/assumption receipt; not observed. |
| AI-proposed mapping | Synthetic/candidate only; cannot be evidence or released mapping without review. |

---

## Change-summary and layer boundaries

Crosswalks often support change summaries and public layers, but they remain separate objects.

```text
CoverClassCrosswalk != ClassSchemeProfile
CoverClassCrosswalk != LandCoverObservation
CoverClassCrosswalk != LandCoverChangeSummary
CoverClassCrosswalk != LayerManifest
CoverClassCrosswalk != ReleaseManifest
CoverClassCrosswalk != EvidenceBundle
CoverClassCrosswalk != renderer style
```

`LandCoverChangeSummary` must cite any crosswalk used to compare two observations. Public layer legends may cite crosswalks for simplification or harmonization, but the renderer must not become the transform authority.

---

## Sensitivity and release

Crosswalks are usually public-safe when they map public schemes, but rights and sensitivity can change that.

Rules:

- Controlled-distribution or rights-restricted source schemes must not be copied into public crosswalk artifacts without rights review.
- Crosswalks that support sensitive Fauna/Flora joins fail closed until geoprivacy, policy, review, release, correction, and rollback support exist.
- Public crosswalk display must include source schemes, versions, directionality, lossiness, reviewer state, and caveats.
- Public map/UI/AI surfaces must not infer crosswalks from similar class labels.
- Generated summaries cannot promote candidate mappings or fill missing reviewer/evidence fields.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source legends, class tables, source guidance, prior crosswalks, literature, reviewer notes, and candidate mapping tables remain source-bound. |
| WORK / QUARANTINE | Candidate crosswalks are normalized, class coverage checked, source roles preserved, rights reviewed, directionality stated, ambiguity/lossiness recorded, and evidence-linked. |
| PROCESSED | Reviewed crosswalks receive deterministic identity, mapping table digest, source scheme refs, evidence refs, validation report refs, and correction posture. |
| CATALOG / TRIPLET | Mapping claims may be cataloged with scheme refs, source role, reviewer state, EvidenceBundle refs, and anti-collapse caveats. |
| RELEASE CANDIDATE | Public crosswalk tables, summary support, or layer-legend use require validation, policy/review where material, release refs, correction path, and rollback target. |
| PUBLISHED | Only released public-safe crosswalk references/tables appear in public clients. |
| CORRECTED / SUPERSEDED | Source scheme update, class label correction, mapping correction, reviewer-state change, rights change, or crosswalk deprecation triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand the paired schema beyond an empty scaffold.
- [ ] Decide whether `CoverClassCrosswalk` or `Crosswalk` is the accepted object-family name.
- [ ] Add valid fixtures for scheme-to-scheme, legend-harmonization, summary-support, ecological-system-input, public-layer-legend, adjacency-context, sensitive-join-guard, candidate, and superseded crosswalks.
- [ ] Add invalid fixtures for missing source scheme, missing target scheme, missing crosswalk version, duplicate mapping rows, unmapped classes without state, nodata treated as class, reverse use without review, many-to-one lossiness omitted, CDL re-owned as Habitat, source-role collapse, rights-unknown public release, and missing rollback target.
- [ ] Add validator checks for class coverage, directionality, version pinning, mapping-kind consistency, lossiness, nodata/unknown handling, evidence refs, reviewer state, release refs, and correction lineage.
- [ ] Add tests proving renderers, notebooks, summaries, and AI cannot silently recode class schemes.
- [ ] Add release tests proving public clients consume released crosswalk metadata only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source/target schemes, mapping table, directionality, evidence, review, policy, release, and rollback all resolve | `ANSWER` / public-safe crosswalk may be used |
| Evidence, scheme version, class coverage, reviewer state, rights, policy, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Silent recode, source-role collapse, unauthorized reverse mapping, sensitive/right-restricted leak, or release bypass would occur | `DENY` |
| Schema, validator, source read, mapping table parse, evidence lookup, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current contract scaffold | Confirms the target file existed as a scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current empty schema posture. | Does not prove field-level validation. |
| Habitat land-cover sublane doc | Defines class schemes, cover-class crosswalks, object-family identity, source-role boundaries, lifecycle, thresholds, map products, cross-lane relations, and no-silent-renderer-transform discipline. | Many field realizations and paths remain PROPOSED. |
| ClassScheme contract | Repo-local adjacent contract defining scheme/vocabulary boundary. | Recent contract content is semantic documentation, not schema enforcement. |
| ChangeSummary contract | Repo-local adjacent contract defining how summaries should cite crosswalks. | Recent contract content is semantic documentation, not schema enforcement. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | It is an authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized crosswalk weakens source integrity, silently changes class meaning, collapses source roles, or lets summaries/layers compare incompatible schemes.

Rollback triggers include:

- source or target class scheme is corrected, withdrawn, or superseded;
- crosswalk version changed in place instead of creating correction lineage;
- mapping table digest changes unexpectedly;
- unmapped, nodata, unknown, reserved, or deprecated classes were mishandled;
- reverse mapping was used without review;
- many-to-one or one-to-many lossiness was hidden;
- CDL or another adjacent-domain scheme was re-owned as Habitat truth;
- crosswalk was embedded in renderer/notebook/AI text without evidence/review record;
- public layer, change summary, or Focus Mode card used the wrong crosswalk version;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate crosswalk as public truth.

Rollback artifacts should include affected crosswalk IDs, from/to scheme IDs, mapping table refs/digests, source descriptor refs, observation refs, change-summary refs, layer refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement crosswalks, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the canonical object name `CoverClassCrosswalk` or `Crosswalk`? | NEEDS VERIFICATION | Habitat contract/schema naming review. |
| Which fields must be required in `crosswalk.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which source-scheme pairs should be activated first? | NEEDS VERIFICATION | SourceDescriptor and land-cover steward review. |
| Which crosswalks can be public, and which inherit controlled-distribution restrictions? | NEEDS VERIFICATION | Source rights and release review. |
| How should probabilistic or one-to-many mappings be represented in public summaries? | NEEDS VERIFICATION | Schema/UX/policy review. |
| How should crosswalks feed ecological-system synthesis without becoming model output by themselves? | NEEDS VERIFICATION | Land-cover + ecological-systems steward review. |

---

## Related contracts and docs

- `contracts/domains/habitat/land_cover/class_scheme.md` — source/target class schemes that crosswalks map.
- `contracts/domains/habitat/land_cover/change_summary.md` — summaries that must cite reviewed crosswalks.
- `docs/domains/habitat/sublanes/land_cover.md` — land-cover sublane doctrine and object-family context.
- `docs/domains/habitat/SOURCE_FAMILIES.md` — Habitat source-family role, rights, and sensitivity posture.
- `schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/habitat/land_cover/` — expected source-role/materiality/crosswalk policy home, pending verification.
- `release/manifests/habitat/` — expected release/rollback home, pending verification.

[Back to top](#top)
