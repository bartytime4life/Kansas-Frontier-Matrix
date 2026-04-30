<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-NEEDS-VERIFICATION
title: Tile Delta Update Model
type: standard
version: v1
status: draft
owners: TODO-NEEDS-VERIFICATION
created: TODO-NEEDS-VERIFICATION
updated: 2026-04-30
policy_label: TODO-NEEDS-VERIFICATION
related: [docs/architecture/tiles/README.md, docs/architecture/tiles/TILE_MANIFEST_SPEC.md, docs/architecture/tiles/VERIFIABLE_TILE_RENDERING.md]
tags: [kfm, tiles, delta-update, tile-manifest, map-release]
notes: [Target file was an empty placeholder during remote inspection; owners, created date, policy label, and doc UUID need maintainer verification.]
[/KFM_META_BLOCK_V2] -->

# Tile Delta Update Model

Purpose: define how KFM updates tile-backed map surfaces without letting incremental delivery bypass evidence, policy, release state, or rollback.

![Status: draft](https://img.shields.io/badge/status-draft-yellow)
![Surface: tiles](https://img.shields.io/badge/surface-tiles-blue)
![Truth: evidence first](https://img.shields.io/badge/truth-evidence--first-blue)
![Implementation: needs verification](https://img.shields.io/badge/implementation-needs%20verification-orange)

**Quick navigation:** [Core rule](#core-rule) · [Truth posture](#truth-posture) · [Scope](#scope) · [Repo fit](#repo-fit) · [Delta model](#delta-model) · [State machine](#state-machine) · [Update decisions](#update-decisions) · [Records](#records) · [Validation gates](#validation-gates) · [Runtime behavior](#runtime-behavior) · [Rollback](#rollback-and-correction) · [Examples](#illustrative-examples) · [Done](#definition-of-done) · [Backlog](#open-verification-backlog)

---

## Core rule

> [!IMPORTANT]
> A tile delta is an update proposal, not publication. Public users may see only release-bound tile artifacts, styles, layers, and governed API responses whose evidence, policy, integrity, cache, and rollback state can be inspected.

Delta delivery can reduce rebuild or transfer cost. It must not reduce KFM’s burden to prove:

- what changed;
- why it changed;
- which sources and processed artifacts support the change;
- whether rights, sensitivity, review, and source role still permit the intended audience;
- which map release now owns the visible result;
- how stale, denied, missing-evidence, generalized, superseded, or withdrawn states appear;
- how the prior public release can be restored without erasing correction history.

---

## Truth posture

| Claim area | Status | Meaning for this file |
|---|---:|---|
| Target path | `CONFIRMED` | Public repository inspection found `docs/architecture/tiles/DELTA_UPDATE_MODEL.md` as an empty placeholder; this document supplies the missing architecture content. |
| Local checkout evidence | `UNKNOWN` | No mounted KFM repository was available in the visible workspace during authoring. |
| KFM tile doctrine | `CONFIRMED` | Adjacent tile docs require manifest-bound rendering, release identity, EvidenceBundle resolution, policy closure, and rollback. |
| Delta object names | `PROPOSED` | `TileDeltaUpdateRecord`, `DeltaEvaluationReport`, and `CacheInvalidationPlan` are proposed names until schema conventions are verified. |
| Runtime implementation | `NEEDS VERIFICATION` | No route handlers, CI jobs, validator scripts, emitted delta receipts, cache rules, or release automation are claimed here. |
| Public release posture | `CONFIRMED doctrine / PROPOSED implementation` | Delta updates must fail closed when evidence, rights, sensitivity, integrity, release, or rollback cannot be proven. |

This document uses `MUST`, `SHOULD`, and `MAY` as architecture requirement keywords.

[Back to top](#tile-delta-update-model)

---

## Scope

This file defines the KFM architecture model for incremental updates to tile-backed map surfaces.

It covers:

- source-change signals that affect tile releases;
- delta candidates for `PMTiles`, `MVT`, raster tiles, COG-backed tile views, small `GeoJSON`, and server-mediated tile services;
- release identity, cache invalidation, rollback, and correction lineage;
- how deltas interact with `TileManifest`, `TileArtifactManifest`, `LayerManifest`, `StyleManifest`, `MapReleaseManifest`, `EvidenceBundle`, `PolicyDecision`, and runtime receipts;
- validation gates that decide whether an update may publish, abstain, deny, or remain quarantined.

It does **not** define:

| Excluded item | Why excluded | Home |
|---|---|---|
| Canonical domain truth | Tiles and deltas are derived artifacts. | Domain stores, source registries, dataset versions, and EvidenceBundle-producing pipelines. |
| Raw source polling logic | Source activation needs rights, cadence, source-role, and connector discipline. | Source registry, connectors, pipelines, and domain runbooks. |
| Tiler-specific implementation | Tooling must not define truth or publication. | Repo-native tools, validators, and pipeline scripts after verification. |
| Style semantics alone | A visual edit can change meaning but cannot approve itself. | `StyleManifest`, release review, and accessibility checks. |
| AI-generated explanations | Model output is downstream of governed evidence. | Governed AI / Focus Mode contracts. |
| Emergency alerting | KFM is contextual evidence, not life-safety alerting. | Official emergency and alerting systems. |
| Exact restricted geometry | Sensitive public precision fails closed. | Restricted/steward paths with policy, transform receipts, and withheld accounting. |

---

## Repo fit

| Relationship | Path or target | Status | Notes |
|---|---:|---|---|
| This document | `docs/architecture/tiles/DELTA_UPDATE_MODEL.md` | `CONFIRMED placeholder / draft content` | Standard architecture doc for delta update semantics. |
| Directory landing page | [`./README.md`](./README.md) | `CONFIRMED adjacent doc` | Defines tile delivery scope, accepted inputs, exclusions, lifecycle, gates, and delivery posture. |
| Manifest spec | [`./TILE_MANIFEST_SPEC.md`](./TILE_MANIFEST_SPEC.md) | `CONFIRMED adjacent doc` | Defines the governed sidecar contract for tile delivery artifacts. |
| Verifiable rendering | [`./VERIFIABLE_TILE_RENDERING.md`](./VERIFIABLE_TILE_RENDERING.md) | `CONFIRMED adjacent doc` | Defines renderability, trust flow, object families, gates, runtime rules, and failure states. |
| Schema home | `schemas/contracts/v1/tiles/` or repo-native equivalent | `NEEDS VERIFICATION` | Do not create a parallel schema dialect without ADR review. |
| Fixtures | `tests/fixtures/tiles/delta_update/` or repo-native equivalent | `PROPOSED` | Should include valid, stale, denied, rollback, and digest-mismatch examples. |
| Validators | `tools/validators/tiles/` or repo-native equivalent | `PROPOSED` | Should validate delta records, manifest closure, release identity, and cache invalidation plans. |
| Release artifacts | `data/published/`, `data/proofs/`, `data/receipts/`, `release/`, or repo-native equivalent | `NEEDS VERIFICATION` | Published homes must never expose RAW, WORK, QUARANTINE, canonical, review-only, or model-runtime paths. |

> [!WARNING]
> If the mounted repository proves different homes for schemas, contracts, fixtures, receipts, proofs, or release bundles, preserve the semantics here and adapt the paths through an ADR. Do not create duplicate tile-delta object families.

---

## Delta model

KFM treats delta updates as release-aware changes between known map states.

| Term | Meaning |
|---|---|
| **Base release** | The last known release state used as the starting point for comparison, rollback, and cache decisions. |
| **Delta signal** | A source, pipeline, review, correction, style, policy, or release event that may require a tile update. |
| **Delta candidate** | A proposed change set that has not yet passed integrity, evidence, policy, catalog, UI, and rollback gates. |
| **Tile delta update record** | PROPOSED record describing what changed, which releases/artifacts are affected, and what evidence/policy checks are required. |
| **Delta evaluation report** | PROPOSED validation output that classifies the update as `PASS`, `ABSTAIN`, `DENY`, or `ERROR`. |
| **Materialized release** | A complete release-visible state after update. Even when internal build work is incremental, public state must be release-addressable. |
| **Cache invalidation plan** | Explicit plan for removing or bypassing stale tile/style/layer bytes without hiding correction lineage. |

```mermaid
flowchart LR
  SD["SourceDescriptor<br/>role · rights · cadence · sensitivity"] --> DS["Delta signal"]
  DS --> DC["Delta candidate<br/>what changed?"]
  DC --> DER["DeltaEvaluationReport<br/>integrity · evidence · policy"]
  DER -->|PASS| BUILD["Build or materialize<br/>new tile/style/layer state"]
  DER -->|ABSTAIN| HOLD["Hold / visible no-publication state"]
  DER -->|DENY| Q["QUARANTINE or denied candidate"]
  DER -->|ERROR| FIX["Implementation fix required"]

  BUILD --> TAM["TileManifest / TileArtifactManifest"]
  TAM --> MRM["MapReleaseManifest<br/>release id · prior release · rollback"]
  MRM --> CIP["CacheInvalidationPlan"]
  MRM --> PUB["PUBLISHED map state"]
  PUB --> ML["MapLibre shell<br/>released artifacts only"]
  ML --> API["Governed API<br/>feature candidate resolution"]
  API --> EB["EvidenceBundle"]
  API --> PD["PolicyDecision"]
  EB --> ED["Evidence Drawer"]
  PD --> ED
```

### Operating interpretation

A delta may be efficient internally, but the public map must still behave as a coherent release. The browser should not need hidden knowledge of unpublished diffs to decide what is true, public, safe, current, or cited.

[Back to top](#tile-delta-update-model)

---

## State machine

Delta handling is a governed state transition. It is not a silent file overwrite.

```mermaid
stateDiagram-v2
  [*] --> DETECTED
  DETECTED --> PROPOSED: source/policy/style/review/correction signal
  PROPOSED --> QUARANTINED: unresolved rights, sensitivity, evidence, or integrity
  PROPOSED --> CANDIDATE: minimum descriptor and base release present
  QUARANTINED --> PROPOSED: issue resolved with receipt
  CANDIDATE --> VALIDATED: gates pass for requested access class
  CANDIDATE --> ABSTAINED: support incomplete or stale
  CANDIDATE --> DENIED: policy/integrity/right/sensitivity failure
  CANDIDATE --> ERROR: validator/runtime defect
  VALIDATED --> PROMOTED: PromotionDecision approved
  PROMOTED --> PUBLISHED: MapReleaseManifest closed
  PUBLISHED --> SUPERSEDED: later release promoted
  PUBLISHED --> WITHDRAWN: release unsafe or invalid
  WITHDRAWN --> ROLLED_BACK: prior release restored
  ROLLED_BACK --> [*]
  SUPERSEDED --> [*]
  ABSTAINED --> [*]
  DENIED --> [*]
  ERROR --> PROPOSED: implementation fixed
```

| State | Public behavior |
|---|---|
| `DETECTED` | No public effect. |
| `PROPOSED` | No public effect; reviewers may inspect proposal. |
| `QUARANTINED` | No public rendering; reason must be recorded. |
| `CANDIDATE` | May be tested in controlled fixture/review contexts only. |
| `VALIDATED` | Eligible for promotion, not yet published. |
| `PROMOTED` | Approved transition, awaiting release/materialization closure. |
| `PUBLISHED` | Public/steward surfaces load release-bound artifacts. |
| `ABSTAINED` | UI may show visible no-answer/no-publication state. |
| `DENIED` | UI may show denial reason without leaking restricted details. |
| `WITHDRAWN` | Active use stops; correction or withdrawal state remains visible. |
| `ROLLED_BACK` | Prior release restored; history remains inspectable. |
| `SUPERSEDED` | Older release remains traceable as lineage. |

---

## Update decisions

KFM prefers complete, digest-addressed release state for public surfaces. Incremental deltas are allowed only when they improve delivery without weakening verification or rollback.

| Update type | Preferred public posture | Delta may be used when… | Must not happen |
|---|---|---|---|
| `PMTiles` snapshot | Publish a new immutable artifact and release ID. | Internal build can update only affected inputs, then materialize a full release artifact. | In-place mutation of a public PMTiles URI without new digest and release state. |
| `MVT` service | Serve versioned release scope or snapshot descriptor. | Per-tile invalidation and service snapshot identity are manifest-bound. | Browser fetches unmanifested or unreleased tile URLs. |
| Martin/PostGIS-style serving | Server-mediated, release-aware, policy-aware serving. | Freshness, steward access, or dynamic slicing needs backend control. | Dynamic tile output becomes undocumented canonical truth. |
| COG-backed raster view | Keep COG/source artifact stronger than derived tiles. | Tile facade points to verified COG/version and render profile. | Pixel interpretation is upgraded to claim truth without evidence. |
| Raster tile bundle | Publish new release-bound tile set or clear invalidation plan. | Low-latency display needs precomputed pixels. | Style/colormap changes alter meaning without `StyleManifest` and review. |
| Small GeoJSON overlay | Use for fixtures, review overlays, or low-risk debug surfaces. | Stable feature IDs and evidence refs are present. | Large public cartography or sensitive geometry bypasses tile governance. |
| Style-only change | Release-aware `StyleManifest` update. | Change does not alter claim meaning, or meaning impact is reviewed. | Hand-edited style becomes publication approval. |
| Layer metadata change | Release-aware `LayerManifest` update. | Evidence/policy/display contract remains coherent. | Layer toggle silently changes what the public may infer. |
| Correction update | Correction notice plus release transition. | Prior release needs visible correction, withdrawal, supersession, or rollback. | Correction history is hidden by replacing assets. |

> [!TIP]
> Treat “delta” as an optimization inside the governed release process. Treat “release” as the public unit of tile visibility.

---

## Records

Object names below are PROPOSED until schema and contract homes are verified.

| Record | Purpose | Minimum fields |
|---|---|---|
| `TileDeltaUpdateRecord` | Describes a proposed tile-visible change against a base release. | `update_id`, `base_release_id`, `target_release_id`, `update_reason`, `update_kind`, `affected_layers`, `affected_artifacts`, `source_descriptor_refs`, `dataset_version_refs`, `evidence_bundle_refs`, `policy_scope`, `created_at`, `created_by_or_process`, `rollback_target_ref` |
| `DeltaEvaluationReport` | Records gate results and final validator outcome. | `report_id`, `update_id`, `base_release_id`, `candidate_release_id`, `checks`, `outcome`, `reason_codes`, `evidence_resolution_summary`, `policy_decision_refs`, `integrity_results`, `review_requirements` |
| `TileDeltaPackage` | Optional internal package of changed tile/style/layer assets. | `package_id`, `base_artifact_refs`, `changed_artifact_refs`, `tile_coordinate_scope`, `artifact_digests`, `manifest_digest`, `media_types`, `stale_after`, `generated_by`, `receipt_refs` |
| `CacheInvalidationPlan` | Describes how stale public bytes are bypassed, purged, or retired. | `plan_id`, `release_id`, `previous_release_id`, `changed_urls_or_keys`, `immutable_url_strategy`, `purge_required`, `fallback_release_id`, `expected_public_state`, `verification_steps` |
| `MapRuntimeReceipt` | Records runtime interaction with the updated release. | `session_or_trace_id`, `active_release_id`, `layer_ids`, `artifact_ids`, `interaction_type`, `resolution_outcome`, `errors`, `timing`, `policy_badges_shown` |
| `CorrectionNotice` | Explains correction, withdrawal, or public-facing update significance. | `notice_id`, `affected_release_ids`, `affected_claims_or_layers`, `correction_reason`, `public_summary`, `review_state`, `rollback_or_supersession_refs` |

### Identity rules

1. `base_release_id` and `target_release_id` MUST be explicit.
2. Public artifacts SHOULD use immutable or digest-addressed URLs where feasible.
3. Mutable public URLs MUST carry release-aware cache behavior and a verifiable invalidation plan.
4. A delta candidate MUST NOT publish if it lacks a rollback target.
5. A changed feature identity MUST either preserve a stable evidence route or emit a visible supersession/correction path.
6. Per-tile changes SHOULD be recorded at the smallest reliable unit the repo can validate. If per-tile integrity is not validated, the release-level artifact digest remains the authority.

[Back to top](#tile-delta-update-model)

---

## Validation gates

| Gate | Purpose | Blocks when… | Outcome |
|---|---|---|---|
| `D0_REPO_CONTEXT` | Avoid false implementation claims. | Schema home, validator, release storage, or package runner is unknown. | `ABSTAIN` for implementation claim; continue as design only. |
| `D1_BASE_RELEASE` | Prove starting state. | Base release, prior manifest, or rollback target is missing. | `DENY` publication. |
| `D2_SOURCE_DELTA` | Prove why update exists. | Source descriptors, update signal, dataset version, or receipt is missing. | `ABSTAIN` or `DENY`. |
| `D3_ARTIFACT_INTEGRITY` | Prove changed bytes. | Artifact digest, manifest digest, media type, or package digest mismatches. | `DENY` and quarantine candidate. |
| `D4_EVIDENCE_IMPACT` | Preserve claim support. | Consequential feature cannot resolve to `EvidenceBundle` or visible failure state. | `ABSTAIN`. |
| `D5_POLICY_SENSITIVITY` | Fail closed before exposure. | Rights unknown, exact restricted geometry, stale source, denied role, or unsupported access class. | `DENY` or forced generalization. |
| `D6_LAYER_STYLE_BINDING` | Keep visual meaning governed. | Layer/style changes are unhashed, ad hoc, inaccessible, or detached from release identity. | `ERROR` or `DENY`. |
| `D7_RELEASE_CLOSURE` | Make update publishable. | `MapReleaseManifest`, proof pack, prior release, cache plan, or promotion decision is missing. | No publication. |
| `D8_RUNTIME_BOUNDARY` | Keep browser downstream. | Public client can fetch raw/work/quarantine/canonical/model-runtime/review-only paths. | `DENY`. |
| `D9_ROLLBACK_CORRECTION` | Preserve reversibility. | Rollback cannot restore prior release or correction lineage is erased. | `DENY`. |
| `D10_ACCESSIBILITY_TRUST` | Keep trust visible. | Stale, denied, generalized, missing-evidence, or correction state is color-only, hidden, or keyboard-inaccessible. | Block public release. |

Finite validator outcomes:

| Outcome | Meaning |
|---|---|
| `PASS` | Checks prove the update is safe for the requested access class. |
| `ABSTAIN` | The system cannot prove support, freshness, completeness, or release eligibility. |
| `DENY` | Integrity, policy, rights, sensitivity, or boundary rule blocks the update. |
| `ERROR` | Validator, schema, runtime, environment, or artifact access failed. |

---

## Runtime behavior

### Renderer permissions

MapLibre, or any future renderer, may:

- load released tile, style, sprite, glyph, and layer artifacts;
- expose `release_id`, `layer_id`, `feature_id`, viewport, active time, and interaction state;
- highlight features using safe UI state;
- send candidate selections to governed APIs;
- emit runtime receipts and diagnostics.

It must not:

- fetch RAW, WORK, QUARANTINE, canonical, review-only, steward-only, proof-pack, or model-runtime paths directly;
- decide whether a delta is true, public, reviewed, cited, corrected, or safe;
- hide restricted geometry with client-side filters;
- treat feature properties, pixels, popups, or style visibility as evidence authority;
- silently suppress stale, denied, withdrawn, generalized, digest-mismatch, or citation-failed states.

### Delta-visible failure states

| State | Meaning | Required behavior |
|---|---|---|
| `BASE_RELEASE_MISSING` | Delta cannot identify its starting release. | Block publication; show release diagnostic to maintainers. |
| `DELTA_SIGNAL_UNRESOLVED` | Reason for update cannot be tied to source, review, policy, or correction. | Hold candidate; require receipt or review. |
| `DELTA_DIGEST_MISMATCH` | Changed artifact does not match declared digest. | Block rendering; create incident/review record. |
| `CACHE_STALE_AFTER_UPDATE` | User may still receive prior bytes after update. | Use immutable release URL or execute invalidation plan before public switch. |
| `EVIDENCE_ROUTE_CHANGED` | Feature ID or evidence route changed. | Require supersession mapping or visible missing-evidence state. |
| `POLICY_DENIED_DELTA` | Update would expose denied/right-restricted/sensitive material. | Deny or generalize server-side; do not send exact detail. |
| `GENERALIZED_DELTA` | Public update changed precision for safety. | Show transform badge and withheld accounting. |
| `RELEASE_WITHDRAWN` | Active release is no longer allowed. | Fall back to prior release or show withdrawn state. |
| `ROLLBACK_REQUIRED` | New release is unsafe or broken. | Restore rollback target without deleting correction notice. |

[Back to top](#tile-delta-update-model)

---

## Rollback and correction

Rollback is a governed state transition, not a cache trick.

| Preserve | Why it matters |
|---|---|
| Prior `MapReleaseManifest` | Defines the exact release state to restore. |
| Withdrawn or superseded manifest | Explains what changed and why it is no longer active. |
| `CacheInvalidationPlan` and execution receipt | Shows how stale bytes were removed or bypassed. |
| `CorrectionNotice` | Prevents history erasure. |
| `DeltaEvaluationReport` | Keeps failed or denied update reasoning inspectable. |
| Evidence and policy refs | Allows future reviewers to audit the release decision. |

### Rollback rule

A delta update cannot be considered release-ready unless the previous public map state can be restored without deleting evidence, receipts, proof objects, release records, or correction lineage.

### Correction rule

A correction delta differs from a routine source delta. It must identify the public-facing claim, layer, artifact, or release state being corrected and must preserve user-visible correction context where the prior state could have affected interpretation.

---

## Illustrative examples

The examples below are contract sketches, not production schemas.

<details>
<summary>Example: TileDeltaUpdateRecord</summary>

```json
{
  "schema": "kfm.map.tile_delta_update_record.v1",
  "update_id": "tile_delta_huc12_2026_04_demo_001",
  "status": "candidate",
  "base_release_id": "maprelease_hydrology_huc12_demo_v1",
  "target_release_id": "maprelease_hydrology_huc12_demo_v2",
  "update_kind": "source_refresh",
  "update_reason": "Source descriptor reports new public-safe HUC12 boundary snapshot.",
  "affected_layers": ["hydrology.huc12.public.v1"],
  "affected_artifacts": ["tileartifact_huc12_pmtiles_v1"],
  "source_descriptor_refs": ["source_usgs_wbd_huc12_kansas_v1"],
  "dataset_version_refs": ["dataset_huc12_kansas_snapshot_REVIEW_REQUIRED"],
  "evidence_bundle_refs": ["bundle_huc12_fixture_001"],
  "policy_scope": {
    "access_class": "public",
    "sensitive_exact_geometry_allowed": false,
    "rights_state": "REVIEW_REQUIRED"
  },
  "delta_scope": {
    "geometry_changed": true,
    "style_changed": false,
    "evidence_route_changed": "REVIEW_REQUIRED",
    "tile_coordinate_scope": ["z/x/y REVIEW_REQUIRED"]
  },
  "evaluation_ref": "data/receipts/REVIEW_REQUIRED_delta_evaluation.json",
  "rollback_target_ref": "maprelease_hydrology_huc12_demo_v1",
  "created_at": "REVIEW_REQUIRED",
  "created_by_or_process": "REVIEW_REQUIRED"
}
```

</details>

<details>
<summary>Example: CacheInvalidationPlan</summary>

```json
{
  "schema": "kfm.map.cache_invalidation_plan.v1",
  "plan_id": "cache_plan_huc12_demo_v2",
  "release_id": "maprelease_hydrology_huc12_demo_v2",
  "previous_release_id": "maprelease_hydrology_huc12_demo_v1",
  "strategy": "immutable_release_urls_preferred",
  "changed_cache_keys": [
    "release_id+artifact_id+content_hash REVIEW_REQUIRED"
  ],
  "purge_required": false,
  "fallback_release_id": "maprelease_hydrology_huc12_demo_v1",
  "verification_steps": [
    "Verify new TileManifest digest.",
    "Verify MapReleaseManifest points to target artifact.",
    "Verify old release remains addressable for rollback.",
    "Verify public shell cannot request unmanifested tile URLs."
  ],
  "executed_at": "REVIEW_REQUIRED",
  "execution_receipt_ref": "data/receipts/REVIEW_REQUIRED_cache_invalidation_receipt.json"
}
```

</details>

<details>
<summary>Example: proposed validation commands</summary>

```bash
# PROPOSED — adapt to repo-native task runner after checkout inspection.

make validate-tile-delta-records
make validate-delta-evaluation-reports
make validate-cache-invalidation-plans
make validate-map-release-manifests
make policy-tiles-delta-public-boundary
make test-tile-delta-rollback
make test-tile-delta-evidence-resolution
make test-no-unreleased-tile-load
```

</details>

---

## Definition of done

A tile delta update model change is not done until every applicable item passes.

- [ ] Target repo checkout, branch, schema home, validator home, release storage, package runner, and adjacent docs have been inspected.
- [ ] Delta object names are reconciled with repo schema conventions or documented through an ADR.
- [ ] `base_release_id`, `target_release_id`, rollback target, and cache invalidation posture are explicit.
- [ ] Every affected source has a `SourceDescriptor` with role, rights, cadence, citation posture, and sensitivity handling.
- [ ] Every changed tile artifact has digest, bounds, zoom range, media type, source refs, build/transform receipts, and stale policy.
- [ ] Every changed layer has a `LayerManifest` that states what it may show and withhold.
- [ ] Every changed style has a `StyleManifest` when visual meaning, accessibility, sprites, glyphs, or layer bindings change.
- [ ] Every consequential selected feature resolves to `EvidenceBundle` or a visible negative state.
- [ ] Unknown rights, unknown sensitivity, missing evidence, digest mismatch, unmanifested URL, or missing rollback blocks public release.
- [ ] Browser access to raw/work/quarantine/canonical/review-only/model-runtime paths is blocked and tested.
- [ ] Delta release can be withdrawn or rolled back without deleting correction history.
- [ ] Trust states are keyboard-accessible and not color-only.
- [ ] Documentation, fixtures, validators, policy tests, and release notes update in the same PR as behavior changes.

---

## Open verification backlog

| Item | Label | Why it matters |
|---|---|---|
| Confirm owners / CODEOWNERS for `docs/architecture/tiles/*` | `NEEDS VERIFICATION` | Required for review routing. |
| Confirm schema home for tile delta objects | `NEEDS VERIFICATION` | Avoids parallel schema dialects. |
| Confirm whether `TileArtifactManifest` and `TileManifest` naming is already standardized | `NEEDS VERIFICATION` | Prevents object-family drift. |
| Confirm release storage and proof/receipt directories | `UNKNOWN` | Delta rollback and cache records depend on repo convention. |
| Confirm current package manager and validator runner | `UNKNOWN` | Commands must be repo-native. |
| Confirm whether PMTiles, Martin/PostGIS, COG, MVT, or MLT tools are installed or planned | `UNKNOWN` | Affects implementation strategy but not governance law. |
| Confirm cache hosting model | `UNKNOWN` | Immutable URLs, purge APIs, and rollback procedures depend on deployment. |
| Confirm source-rights vocabulary | `NEEDS VERIFICATION` | Unknown rights must block public release. |
| Confirm sensitive geometry categories and transform receipts | `NEEDS VERIFICATION` | Public deltas must not leak restricted locations. |
| Confirm runtime receipt vocabulary | `UNKNOWN` | Click/render delta behavior should be observable without becoming truth. |
| Confirm accessibility test convention | `UNKNOWN` | Trust-state visibility must be testable. |

---

<details>
<summary>Appendix A — Glossary</summary>

| Term | KFM meaning |
|---|---|
| **Delta signal** | A change event that may require a map release update. |
| **Delta candidate** | Proposed update that has not yet passed gates. |
| **Tile delta update record** | Proposed sidecar describing changed scope, base release, target release, source refs, policy scope, and rollback target. |
| **Delta evaluation report** | Validation result for an update candidate. |
| **Tile delta package** | Optional internal package of changed delivery bytes; not automatically public. |
| **Materialized release** | Complete release-visible map state after update. |
| **Cache invalidation plan** | Reviewable plan for stale public bytes after release transition. |
| **Rollback target** | Prior known-good release state. |
| **Correction delta** | Update that fixes or withdraws prior public meaning and must preserve correction context. |
| **Release-bound rendering** | Browser loads only artifacts referenced by the active map release. |
| **Evidence route** | Path from selected feature/layer/release to governed `EvidenceBundle`. |

</details>

<details>
<summary>Appendix B — Anti-patterns to reject</summary>

- Updating public tile bytes in place without a new digest, release ID, and rollback target.
- Treating a tile diff as proof that the underlying claim changed.
- Publishing a delta because it is small, fast, or visually harmless.
- Using client-side filters to hide restricted geometry after the browser has already received it.
- Letting `feature_id` changes break Evidence Drawer or Focus Mode resolution silently.
- Letting cache freshness hide release withdrawal or correction status.
- Allowing a style-only change to alter meaning without `StyleManifest` and release review.
- Using Focus Mode to summarize changed tile properties before EvidenceBundle resolution.
- Deleting old manifests to “clean up” rollback history.
- Creating a new delta schema home without checking existing repo convention.

</details>

[Back to top](#tile-delta-update-model)
