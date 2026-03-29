<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-NEEDS-UUID
title: KFM STAC Profile
type: standard
version: v1
status: draft
owners: TODO-NEEDS-VERIFICATION
created: TODO-NEEDS-VERIFICATION
updated: TODO-NEEDS-VERIFICATION
policy_label: TODO-NEEDS-VERIFICATION
related: [TODO-NEEDS-VERIFICATION]
tags: [kfm, stac, standards, catalog, interoperability]
notes: [Mounted workspace evidence for this drafting session was PDF-only; repo links, owners, dates, mounted schema inventory, endpoint names, and CI enforcement require direct verification.]
[/KFM_META_BLOCK_V2] -->

# KFM STAC Profile

KFM’s outward STAC profile for **published spatiotemporal discovery metadata**, release-linked assets, and governed catalog closure.

> [!IMPORTANT]
> This draft is **doctrine-grounded** and **implementation-bounded**. In the current drafting session, visible workspace evidence was PDF-only. Exact repo paths, schema files, endpoint names, fixtures, validators, CI jobs, and neighboring Markdown links remain **UNKNOWN** until directly reverified from the mounted repository.

[![Status: draft](https://img.shields.io/badge/status-draft-lightgrey)](#status-and-verification-boundary)
[![Type: standard](https://img.shields.io/badge/type-standard-2f6fdb)](#status-and-verification-boundary)
[![STAC: 1.1.0](https://img.shields.io/badge/STAC-1.1.0-0b7285)](#baseline-profile-line)
[![Closure: STAC%2FDCAT%2FPROV](https://img.shields.io/badge/closure-STAC%2FDCAT%2FPROV-6f42c1)](#kfm-positioning)
[![Verification: PDF-only](https://img.shields.io/badge/verification-PDF--only_review-f0ad4e)](#status-and-verification-boundary)

**Quick jump:** [Role](#role-in-kfm) · [Scope](#scope) · [Positioning](#kfm-positioning) · [Rules](#profile-rules) · [Requirements](#minimum-profile-requirements) · [Control-plane prerequisites](#control-plane-prerequisites) · [Proposed KFM fields](#proposed-kfm-fields) · [Validation](#validation-and-gates) · [Examples](#illustrative-examples) · [Verification backlog](#verification-backlog)

## Status and verification boundary

| Field | Value |
| --- | --- |
| Status | `draft` |
| Posture | `CONFIRMED doctrine` / `PROPOSED profile realization` / `UNKNOWN mounted implementation` |
| Intended role | Standard for **published discovery metadata**, not canonical storage |
| Baseline profile line | `STAC 1.1.0` |
| Discovery closure | `STAC + DCAT + PROV` |
| Current evidence boundary | PDF corpus only |
| Not directly verified in this session | repo tree, file paths, schemas, tests, workflows, manifests, live routes, runtime outputs |

## Role in KFM

KFM treats STAC as a **release-facing catalog and discovery carrier**.

That means this standard is about:

- outward discoverability of released spatiotemporal assets
- stable item/collection/catalog semantics for public-safe or otherwise policy-permitted release scope
- linkage from discovery metadata into release, provenance, rights, sensitivity, and correction state

It is **not** a replacement for KFM’s canonical truth plane, policy plane, review plane, or runtime evidence-resolution contracts.

## KFM positioning

KFM is strongest when STAC, DCAT, and PROV are linked as one outward closure instead of treated as competing metadata worlds:

- **STAC** carries spatiotemporal item and asset discovery
- **DCAT** carries outward dataset and distribution discovery
- **PROV** carries lineage, agents, and activities
- **KFM-specific policy and review artifacts** remain first-class beside them

```mermaid
flowchart LR
    A[Source edge] --> B[RAW]
    B --> C[WORK / QUARANTINE]
    C --> D[PROCESSED]
    D --> E[DatasetVersion]
    E --> F[CatalogClosure]
    F --> G[STAC]
    F --> H[DCAT]
    F --> I[PROV]
    F --> J[DecisionEnvelope / ReviewRecord]
    F --> K[ReleaseManifest]
    K --> L[ProjectionBuildReceipt]
    G --> M[Catalog & discovery]
    H --> M
    I --> M
    M --> N[Public-safe discovery surface]

    style E fill:#eef7ff,stroke:#2f6fdb
    style F fill:#f5f0ff,stroke:#6f42c1
    style G fill:#eaf7f7,stroke:#0b7285
    style K fill:#fff6e8,stroke:#b26b00
```

## Scope

This profile governs STAC emitted at the **published discovery boundary**.

It covers:

- STAC catalogs, collections, items, and release-safe asset links
- outward metadata emitted from governed catalog closure
- discovery metadata for released data products, portrayals, and derivative packages that remain tied to release scope
- visibility of rights, sensitivity, freshness, and correction state where those change meaning

## Out of scope

This standard does **not** govern the following:

| Out of scope | Where it belongs instead |
| --- | --- |
| `RAW`, `WORK`, `QUARANTINE`, and unpublished candidate artifacts | intake, validation, and review lanes |
| canonical entity storage and internal truth modeling | canonical data architecture and internal schemas |
| `EvidenceBundle` payload shape | evidence-resolution contracts |
| `RuntimeResponseEnvelope` shape | runtime and Focus contracts |
| internal moderation, approval, rollback, or rights-handling workflows | policy/review plane |
| portrayal-specific renderer internals | portrayal, style, and renderer standards |
| direct feature-edit semantics | governed feature APIs and authoring contracts |

## Baseline profile line

### Baseline profile line

| Concern | Rule | Status |
| --- | --- | --- |
| STAC core/profile line | Use `STAC 1.1.0` as the baseline outward profile line | `CONFIRMED` |
| Closure model | Treat STAC as part of a linked `STAC / DCAT / PROV` outward closure | `CONFIRMED doctrine` |
| Discovery boundary | Align discovery with catalog/discovery route families rather than canonical storage | `CONFIRMED doctrine` |
| Mounted conformance claim | Do **not** claim live conformance until actual schemas, fixtures, validators, and emitted examples are reverified | `UNKNOWN` |

> [!NOTE]
> This document defines the **required shape of the standard boundary**. It does not claim that the currently mounted project already emits this profile.

## Profile rules

### Rule 1 — published scope only

STAC is emitted only for **published** or otherwise explicitly release-safe scope. No public STAC document should point into `RAW`, `WORK`, `QUARANTINE`, or unpublished candidate material.

### Rule 2 — STAC is downstream of release governance

STAC is not a publication act by itself. A valid STAC object without release linkage, policy state, or review closure is still insufficient KFM output.

### Rule 3 — release linkage is mandatory

Every emitted STAC object must remain tied to release-bearing scope, not merely to a storage location or convenience export.

### Rule 4 — rights and sensitivity are first-class

Public discovery metadata must not hide unresolved rights, redistribution limits, precision controls, geoprivacy limits, or cultural/sensitivity posture.

### Rule 5 — discovery and authority remain separate

STAC is a discovery layer, not KFM’s sovereign internal truth layer.

### Rule 6 — correction lineage stays visible

Superseded, narrowed, generalized, withdrawn, or replaced material must preserve visible lineage rather than silently disappearing.

### Rule 7 — derived delivery stays downstream

Tiles, portrayals, search views, graph projections, scene packages, and other discovery-adjacent derivatives must inherit release linkage, freshness basis, and correction state from promoted scope.

### Rule 8 — fail closed

Where release, evidence, rights, sensitivity, schema validity, or correction integrity fail, publication must fail closed.

## Minimum profile requirements

### Minimum profile requirements

| Element | Expectation | KFM posture |
| --- | --- | --- |
| `stac_version` | Required and pinned to the approved baseline line | `REQUIRED` |
| Stable `id` | Release-safe, stable, and non-recycled across materially distinct released objects | `REQUIRED` |
| `type` | Standard STAC object typing | `REQUIRED` |
| `geometry` / `bbox` | Present when the object carries spatial scope; generalized shape must be visibly treated as such | `REQUIRED when spatially meaningful` |
| Temporal metadata | Enough to support discovery, filtering, and support-time interpretation | `REQUIRED` |
| `links` | Resolvable navigation and closure linkage | `REQUIRED` |
| `assets` | Release-safe outward distributions only | `REQUIRED when retrievable data exists` |
| Asset `type` / media type | Explicit content typing | `REQUIRED` |
| Asset `roles` | Stable, predictable discovery semantics | `REQUIRED` |
| Rights / license posture | Visible and machine-carried where possible | `REQUIRED` |
| Provenance linkage | Linked PROV closure or equivalent outward lineage pointer | `REQUIRED` |
| Release linkage | Direct or resolvable linkage to release-bearing scope | `REQUIRED` |
| Freshness basis | Declared where staleness changes meaning | `REQUIRED when applicable` |
| Correction / supersession visibility | Successor, withdrawal, narrowing, or replacement state must stay visible | `REQUIRED when applicable` |
| Content digests / checksums | Strong practical closure requirement for promotion-ready assets | `PROPOSED KFM closure requirement` |

### Strong recommendations

| Recommendation | Why it matters |
| --- | --- |
| Keep collection and item identifiers deterministic where practical | simplifies correction, audit, and rebuild |
| Make geometry generalization explicit | prevents false precision |
| Distinguish observed, modeled, assimilated, and source-dependent outputs | prevents interpretive flattening |
| Keep authoritative subject identity separate from projection/build identity | avoids derivative drift |
| Use predictable asset keys and roles | reduces client special-casing |
| Make collections useful without opening assets | improves triage and federation behavior |

## Control-plane prerequisites

A STAC object may be outwardly visible only after the relevant control-plane prerequisites exist.

| KFM object | Why it matters for STAC publication | Status |
| --- | --- | --- |
| `SourceDescriptor` | Declares source identity, support, cadence, rights posture, validation plan, and publication intent | `CONFIRMED doctrine` |
| `IngestReceipt` | Proves fetch/landing and integrity context occurred | `CONFIRMED doctrine` |
| `ValidationReport` | Proves checks passed, failed, or quarantined | `CONFIRMED doctrine` |
| `DatasetVersion` | Provides authoritative candidate or promoted subject set with support/time semantics and provenance | `CONFIRMED doctrine` |
| `CatalogClosure` | Publishes outward metadata closure and STAC/DCAT/PROV linkage | `CONFIRMED doctrine` |
| `DecisionEnvelope` | Records machine-readable policy result and obligations | `CONFIRMED doctrine` |
| `ReviewRecord` | Captures required human approval/denial/escalation where review is needed | `CONFIRMED doctrine` |
| `ReleaseManifest` / `ReleaseProofPack` | Assembles public-safe release and proof | `CONFIRMED doctrine` |
| `ProjectionBuildReceipt` | Proves a derived layer was built from a known release scope | `CONFIRMED doctrine` |
| `CorrectionNotice` | Preserves visible lineage when published meaning changes | `CONFIRMED doctrine` |

> [!CAUTION]
> In KFM, **discoverability is a governed outcome**. If control-plane proof is missing, STAC should not be treated as releasable.

## Required control-plane consequences

1. A `CatalogClosure` must exist before outward discoverability is considered valid.
2. A `DecisionEnvelope` must capture the rights/sensitivity/release result machine-readably.
3. A `ReviewRecord` is required when the publication burden for the lane or artifact class demands review.
4. A `ReleaseManifest` or equivalent release proof must anchor what the catalog is allowed to expose.
5. Any derived portrayal or tile-facing STAC asset should carry or resolve to a `ProjectionBuildReceipt`.
6. Any post-release narrowing, replacement, or withdrawal must emit a `CorrectionNotice`.

## Route fit

| Route family | Fit with this profile | Notes |
| --- | --- | --- |
| Catalog and discovery | **Primary fit** | STAC belongs here most directly |
| Feature or subject read | Adjacent | subject-read contracts remain distinct |
| Map / tile / portrayal | Related | should inherit release linkage, freshness, and correction state |
| Evidence resolution | Related but separate | STAC may point toward evidence, but it is not the evidence contract |
| Story / dossier / compare | Consumer of STAC, not defined by it | shell surfaces must still drill through to evidence |
| Export and report | Related | exports may expose STAC-linked assets but remain governed separately |
| Focus / governed assistance | Consumer of STAC-linked released scope | runtime contracts remain separate |

## Rights, sensitivity, freshness, and correction

### Rights and redistribution

A STAC document must not imply broader reuse than KFM has actually cleared. Unresolved or ambiguous rights posture is a fail-closed condition.

### Sensitive location handling

If exact location is not safe for the intended audience, the profile expects one of the following:

1. do not publish
2. publish a visibly generalized spatial representation
3. publish metadata-only discovery without precise coordinates

### Source-dependent and modeled material

Where a published asset is source-dependent, modeled, generalized, assimilated, or otherwise interpretively burdened, that state should be visible rather than implied away.

### Freshness and stale-visible behavior

If a derived portrayal, projection, or linked asset becomes stale beyond its declared tolerance, the surface should move into a visible stale state rather than silently presenting itself as current.

### Correction propagation

Correction must remain visible across discovery, map, story, export, and Focus-adjacent surfaces. A replacement should not erase the fact that replacement occurred.

## Proposed KFM fields

> [!NOTE]
> The following `kfm:*` fields are **PROPOSED starter fields**. They are not asserted as mounted schemas, extension URIs, or already-deployed property names.

| Field | Purpose | Status |
| --- | --- | --- |
| `kfm:dataset_version_id` | Tie STAC output back to the authoritative dataset version | `PROPOSED` |
| `kfm:release_id` | Tie STAC output to release scope | `PROPOSED` |
| `kfm:decision_ref` | Point to the publication decision or decision envelope | `PROPOSED` |
| `kfm:review_ref` | Point to a review record when one governs publication | `PROPOSED` |
| `kfm:evidence_state` | Surface source-stated / extracted / inferred / reviewed / generalized style state | `PROPOSED` |
| `kfm:rights_class` | Surface rights posture in a machine-readable way | `PROPOSED` |
| `kfm:sensitivity_class` | Surface sensitivity class without leaking protected detail | `PROPOSED` |
| `kfm:source_mode` | Distinguish observed / modeled / assimilated / source-dependent material | `PROPOSED` |
| `kfm:correction_state` | Make superseded / withdrawn / narrowed / replaced status visible | `PROPOSED` |
| `kfm:profile_version` | Pin the KFM STAC profile revision used to emit the object | `PROPOSED` |
| `kfm:generalization_note` | Explain why geometry or timing has been coarsened | `PROPOSED` |
| `kfm:checksum_ref` | Point to asset digest or closure-integrity material | `PROPOSED` |

## KFM object mapping

| KFM family | STAC role | KFM expectation |
| --- | --- | --- |
| `DatasetVersion` | Authoritative version anchor | STAC must not invent competing version truth |
| `CatalogClosure` | Governs emitted catalog / collection / item set | STAC is downstream of closure |
| `ReleaseManifest` | Governs public-safe release linkage | STAC inherits release scope from here |
| `ProjectionBuildReceipt` | Governs lineage for derived assets | tile/scene/portrayal derivatives must stay linked |
| `EvidenceBundle` | Related support object, not a STAC object | link out through governed evidence routes when appropriate |
| `DecisionEnvelope` | Policy proof | usually linked indirectly or through resolvable review/release context |
| `CorrectionNotice` | Correction lineage | successor / withdrawal / replacement state should remain discoverable |

## Validation and gates

### Minimum validation stack

| Gate | What it proves | Status |
| --- | --- | --- |
| STAC schema validation | Core object shape and baseline validity | `CONFIRMED requirement` |
| Closure integrity checks | STAC / DCAT / PROV resolve cleanly together | `CONFIRMED requirement` |
| Identifier consistency checks | IDs resolve consistently across closure and release | `CONFIRMED requirement` |
| Rights / sensitivity gate | publication is public-safe for the intended audience | `CONFIRMED requirement` |
| Freshness / stale-projection checks | derived discovery layers do not silently impersonate current truth | `CONFIRMED requirement` |
| Correction propagation checks | supersession / narrowing / withdrawal stay visible | `CONFIRMED requirement` |
| Link integrity checks | outward links and relations resolve | `CONFIRMED requirement` |
| KFM profile validation | KFM-specific rules beyond STAC core | `PROPOSED starter gate` |
| Digest / integrity checks | content digests are present and coherent for promotion-ready assets | `PROPOSED starter gate` |

### Release gate reminder

A publishable STAC surface should not be treated as complete without:

- dataset version reference
- catalog closure
- policy result
- review record where required
- release receipt or proof pack
- evidence-resolution pass or equivalent support proof
- rollback / correction posture
- updated docs or runbooks where behavior changed

> [!WARNING]
> A syntactically valid STAC object is **not** automatically acceptable KFM output.

## Forbidden or fail-closed conditions

| Condition | Required behavior |
| --- | --- |
| Missing reconstructible evidence path for an outward claim | fail closed |
| Unknown rights or redistribution posture | fail closed |
| Exact-location risk not covered by a safe representation | withhold or generalize visibly |
| Schema / identity / unit / support failure | fail validation |
| Missing catalog closure or required review artifact | no releasable discoverability |
| Runtime citation failure on a trust-bearing outward surface | no confident outward answer path |
| Stale derived projection beyond declared tolerance | stale-visible, rebuilt, or withheld |
| Unlinked or orphaned derived assets | do not publish as current |

<details>
<summary><strong>Anti-patterns this profile rejects</strong></summary>

- treating STAC as KFM’s canonical truth store
- publishing directly from ingest or candidate lanes
- allowing tiles, caches, graphs, or summaries to quietly become authoritative
- shipping discovery metadata with no visible rights or provenance posture
- dropping correction lineage when assets are replaced
- claiming mounted validators or endpoints that have not been directly reverified

</details>

## Illustrative examples

> [!NOTE]
> The examples below are illustrative only. They show profile intent, not confirmed mounted payloads.

### Illustrative STAC Item

```json
{
  "stac_version": "1.1.0",
  "type": "Feature",
  "id": "TODO-ILLUSTRATIVE-KFM-ITEM-ID",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]]
  },
  "bbox": [0, 0, 1, 1],
  "properties": {
    "datetime": "2026-03-01T00:00:00Z",
    "license": "TODO-ILLUSTRATIVE",
    "kfm:dataset_version_id": "TODO-ILLUSTRATIVE",
    "kfm:release_id": "TODO-ILLUSTRATIVE",
    "kfm:evidence_state": "reviewed",
    "kfm:rights_class": "public",
    "kfm:sensitivity_class": "generalized",
    "kfm:source_mode": "observed",
    "kfm:profile_version": "v1"
  },
  "assets": {
    "data": {
      "href": "TODO-ILLUSTRATIVE",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "links": [
    { "rel": "root", "href": "TODO-ILLUSTRATIVE" },
    { "rel": "collection", "href": "TODO-ILLUSTRATIVE" },
    { "rel": "describedby", "href": "TODO-ILLUSTRATIVE" },
    { "rel": "via", "href": "TODO-ILLUSTRATIVE" },
    { "rel": "related", "href": "TODO-ILLUSTRATIVE" }
  ]
}
```

<details>
<summary><strong>Illustrative link expectations</strong></summary>

A review-ready STAC object will usually make room for:

- root / parent / collection navigation
- profile or schema description
- release-manifest or release-context linkage
- provenance linkage
- correction or successor linkage where applicable

</details>

## Verification backlog

| Unknown | Why it matters |
| --- | --- |
| Actual target repo path for this file | keeps links and adjacent docs correct |
| Mounted schema registry path | required before claiming extension or validator wiring |
| Mounted STAC fixtures and examples | needed for conformance claims |
| Mounted CI/workflow coverage | needed before claiming enforced release gates |
| Mounted endpoint names and route trees | needed before naming real public discovery surfaces |
| Mounted owners, dates, and policy label | required to finalize the meta block |
| Mounted KFM extension namespace / schema URI | required before hardening `kfm:*` properties beyond draft |
| Actual checksum / integrity requirements in code | needed before turning closure-digest expectations into confirmed enforcement |

## Definition of done for this standard

- [ ] Reverify whether this file already exists in the repo and merge with any stronger neighboring material
- [ ] Replace all `TODO-NEEDS-VERIFICATION` placeholders in the meta block
- [ ] Confirm the mounted schema home, fixture layout, and validator entrypoints
- [ ] Confirm the mounted STAC version line and any extension allowlist
- [ ] Add relative links to adjacent standards, route, runbook, and API docs
- [ ] Verify one positive and one negative closure example for `STAC / DCAT / PROV`
- [ ] Verify one release-linked item with visible rights/sensitivity posture
- [ ] Verify one correction example with successor or withdrawal behavior
- [ ] Verify one stale-projection or freshness-control example
- [ ] Confirm whether checksums/digests are already enforced or remain starter doctrine

<details>
<summary><strong>Appendix — drafting posture</strong></summary>

This draft intentionally keeps three things separate:

1. **CONFIRMED doctrine**  
   What the attached KFM manuals establish clearly.

2. **PROPOSED starter realization**  
   A usable first profile shape for later schema, fixture, and validator work.

3. **UNKNOWN mounted implementation**  
   Anything that would require direct repo, schema, workflow, or runtime inspection.

That separation is part of the standard, not a temporary embarrassment.

</details>
