<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/quarantine/soil/readme
name: Soil Quarantine README
path: data/quarantine/soil/README.md
type: data-quarantine-index-readme
version: v0.1.0
status: draft
owners:
  - <soil-lane-steward>
  - <data-steward>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: quarantine
responsibility_root: data/
domain: soil
artifact_family: held-soil-material
sensitivity_posture: fail-closed; no-public-path; support-type-separation-required; source-role-preservation-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../processed/soil/README.md
  - ../../published/layers/soil/README.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../contracts/domains/soil/README.md
  - ../../../release/manifests/README.md
tags: [kfm, data, quarantine, soil, ssurgo, gssurgo, soil-moisture, pedon, support-type, source-role, evidence-first]
notes:
  - "This README replaces the greenfield stub and documents the parent Soil quarantine lane."
  - "No Soil quarantine child README lanes were confirmed during this edit."
  - "Support-type separation is mandatory: static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface."
  - "Actual held payload presence, policy automation, validator wiring, CI enforcement, and review completion remain UNKNOWN unless verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Quarantine

Parent hold lane for Soil material that is not safe or sufficiently governed for normal processing, cataloging, publication, reporting, map rendering, story playback, graph/vector indexing, or generated-answer use.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: quarantine" src="https://img.shields.io/badge/lifecycle-quarantine-critical">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-795548">
  <img alt="Support types: separated" src="https://img.shields.io/badge/support%20types-separated-6e40c9">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Proposed quarantine classes](#proposed-quarantine-classes) · [Exclusions](#exclusions) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/quarantine/soil/` is a no-public-path hold lane. Material here is not public, not processed truth, not catalog truth, not proof, not release authority, not policy authority, not survey truth, not gridded-derivative truth, not observation truth, not pedon truth, and not interpretation truth. Nothing in this subtree may be consumed by public clients or normal UI surfaces until a governed exit transition leaves inspectable evidence.

---

## Scope

This directory holds Soil material when source role, source activation, rights, support type, survey lineage, map-unit identity, component identity, horizon identity, pedon/profile identity, soil-property meaning, units, depth, QC, gridded derivative support, satellite grid caveats, interpretation caveats, geometry/CRS, temporal state, sensitivity, evidence support, validation, review record, policy decision, receipt closure, correction path, or rollback target is unresolved.

Soil owns static soil-survey evidence, gridded soil derivatives, components, horizons, pedons, soil-moisture observations, interpretations, suitability, erosion context, and public-safe soil map/API products. It cites but does not own crop/yield, streamflow, groundwater, flood context, lithology, boreholes, stratigraphy, habitat patches, or ecological occurrence truth.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/quarantine/soil/` |
| Responsibility root | `data/` |
| Lifecycle phase | `quarantine/` |
| Domain lane | `soil` |
| Artifact role | Parent hold lane for Soil quarantine material and quarantine-local review sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Exit posture | Only by explicit policy decision, source-role/evidence/rights/sensitivity/support-type closure, required receipt closure, corrected lifecycle placement, and release-state closure |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/` and `data/receipts/`, not this directory |
| Catalog authority | `data/catalog/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `DENY`, `RESTRICT`, or `ABSTAIN` when source role, rights, evidence, support type, sensitivity, identity, lineage, geometry, caveat, review, correction, or rollback support is insufficient |

---

## Confirmed child lanes

No `data/quarantine/soil/` child-lane README paths were confirmed during this edit.

| Child lane | Status | Notes |
|---|---|---|
| `<none confirmed>` | **UNKNOWN** | Do not infer payloads, validators, source descriptors, release gates, or CI coverage from this parent README. |

---

## Proposed quarantine classes

| Class | Status | Typical handling |
|---|---|---|
| Source activation unresolved | **PROPOSED / NEEDS VERIFICATION** | Hold until source descriptor and activation decision are resolved. |
| Rights unknown | **PROPOSED / NEEDS VERIFICATION** | Hold until terms, attribution, cadence, and permitted claims are recorded. |
| Support type missing or collapsed | **PROPOSED / NEEDS VERIFICATION** | Hold when static survey, gridded derivative, station, satellite, pedon, or interpretation support is not explicit. |
| Survey lineage defect | **PROPOSED / NEEDS VERIFICATION** | Hold map-unit, component, and horizon joins until lineage and identity closure are restored. |
| Observation unit/depth/QC defect | **PROPOSED / NEEDS VERIFICATION** | Hold observations until units, depth, QC, time, support type, and source caveats are explicit. |
| Cross-support aggregation unreviewed | **PROPOSED / NEEDS VERIFICATION** | Require explicit derivation, validation, caveats, and receipt closure before aggregation. |
| Evidence open | **PROPOSED / NEEDS VERIFICATION** | Build EvidenceBundle or deny/abstain. |
| Temporal / scale / caveat defect | **PROPOSED / NEEDS VERIFICATION** | Separate source, observed, valid, retrieval, release, and correction time; record time/scale caveats. |

---

## Inputs

Accepted content is limited to held review material and quarantine-local sidecars: source references, source-role notes, rights notes, support-type notes, lineage notes, geometry notes, observation caveats, validation notes, quarantine reason notes, candidate receipt drafts, digest sidecars, and local README/index files.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Clean RAW source mirrors that have not triggered quarantine | `data/raw/soil/` or source-specific intake |
| Ordinary WORK material that is safe to process under normal review | `data/work/soil/` |
| Validated processed Soil objects | `data/processed/soil/` only after quarantine resolution |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, triplet lanes, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Final validation, redaction, aggregation, source-role-review, support-type derivation, or release receipts | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, or signatures | `release/` |
| Source descriptors, activation records, source registries, or registry truth | `data/registry/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Crop/yield, streamflow, flood, lithology, borehole, habitat, species occurrence, or rare-location truth | Owning domain lane, not Soil quarantine |
| Semantic contracts, schemas, validators, or policy rules | `contracts/`, `schemas/`, `tools/`, `policy/` |

---

## Directory map

```text
data/quarantine/soil/
├── README.md
├── <future-risk-sublane>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain quarantine-local. It is not a public index, catalog record, release manifest, registry, graph edge source, layer/story/report pointer, search index, vector index, map source, soil truth index, or support-type authority.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay held | Any unresolved source-role, source-activation, rights, support-type, identity, lineage, units, depth, QC, sensitivity, evidence, temporal, validation, review, policy, or release question remains. |
| Deny | PolicyDecision says `DENY`; public/UI surfaces abstain or deny. |
| Restrict | PolicyDecision and ReviewRecord identify allowed audience, purpose, terms, caveat state, correction path, and rollback target. |
| Return to work | Hold reason is resolved, but normal validation, attribution, temporal handling, source-role review, support-type derivation, or EvidenceBundle work still remains. |
| Promote to processed/catalog/published | Only after required receipts, source descriptors, source-role closure, support-type closure, validation closure, EvidenceBundle closure, ReleaseManifest, correction path, rollback path, and approved public-safe transform exist. |

---

## Forbidden shortcuts

```text
data/quarantine/soil/
→ data/processed/soil/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless the appropriate governed transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the material is Soil-domain material and belongs under `data/quarantine/soil/`.
- [ ] Confirm the hold reason is recorded using a governed reason code.
- [ ] Confirm source descriptors, source activation decisions, source roles, rights posture, cadence, and current terms.
- [ ] Confirm support type is explicit and preserved.
- [ ] Confirm survey lineage, units, depths, QC flags, geometry/CRS, source vintage, temporal scope, caveats, and digest closure where material.
- [ ] Confirm cross-lane joins follow the owning lane's policy.
- [ ] Confirm required receipts are present or explicitly marked missing.
- [ ] Confirm PolicyDecision, ValidationReport, ReviewRecord where required, correction path, rollback target, and release-state handling before any exit.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses quarantined material.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/quarantine/soil/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No `data/quarantine/soil/` child-lane README path was confirmed during this edit. | **CONFIRMED by GitHub search/fetch during this edit** |
| Soil architecture says the lane owns static soil-survey evidence, gridded derivatives, components, horizons, pedons, soil-moisture observations, interpretations, suitability, erosion context, and public-safe soil products. | **CONFIRMED by GitHub contents API during this edit** |
| Soil architecture says support-type separation is mandatory and mixed/untagged support surfaces deny, abstain, or quarantine. | **CONFIRMED by GitHub contents API during this edit** |
| Soil architecture says unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion. | **CONFIRMED by GitHub contents API during this edit** |
| `data/processed/soil/README.md` exists as the downstream processed-stage parent lane. | **CONFIRMED by GitHub contents API during this edit** |
| `data/published/layers/soil/README.md` exists as the released public-safe layer parent lane. | **CONFIRMED by GitHub contents API during this edit** |
| Actual quarantined payloads exist under this subtree. | **UNKNOWN** |
| Policy automation, validators, and CI checks enforce every listed Soil quarantine class. | **NEEDS VERIFICATION** |
| This README is proof, release, catalog, registry, policy, soil truth, survey truth, gridded-derivative truth, station observation truth, satellite observation truth, interpretation truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../processed/soil/README.md`](../../processed/soil/README.md)
- [`../../published/layers/soil/README.md`](../../published/layers/soil/README.md)
- [`../../../docs/domains/soil/ARCHITECTURE.md`](../../../docs/domains/soil/ARCHITECTURE.md)
- [`../../../contracts/domains/soil/README.md`](../../../contracts/domains/soil/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Soil quarantine hold index only. It is not source authority, proof authority, receipt authority, release authority, catalog authority, registry authority, policy authority, soil truth, survey truth, gridded-derivative truth, station observation truth, satellite observation truth, pedon truth, interpretation truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
