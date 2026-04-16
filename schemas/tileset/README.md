<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: schemas/tileset
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <NEEDS_VERIFICATION_DATE>
updated: <NEEDS_VERIFICATION_DATE>
policy_label: public
related: [../README.md, ../tiler/README.md, ../../contracts/tiler/README.md, ../../tools/tiler/README.md, ../../data/catalog/README.md, ../../data/receipts/README.md, ../../tools/validators/README.md, ../../tests/contracts/README.md, ../../docs/standards/KFM_STAC_PROFILE.md]
tags: [kfm, schemas, tileset, tiler, 3d-tiles, scene-manifest]
notes: [Current public-main view shows this lane as README-only, narrower path ownership and canonical metadata values still need verification, tileset-facing schema wave is proposed but not repo-verified]
[/KFM_META_BLOCK_V2] -->

# `schemas/tileset`

Boundary README for tileset- and scene-manifest-shaped schemas in KFM’s conditional 3D delivery path.

> Status: experimental · Doc status: draft  
> Owners: `@bartytime4life` *(public-main global fallback; narrower `/schemas/tileset/` ownership still needs verification)*  
> ![Status: Experimental](https://img.shields.io/badge/status-experimental-1f6feb) ![Doc: Draft](https://img.shields.io/badge/doc-draft-f59e0b) ![Lane: Tileset](https://img.shields.io/badge/lane-tileset-7c3aed) ![3D: Conditional](https://img.shields.io/badge/3D-conditional-6b7280) ![Posture: Fail Closed](https://img.shields.io/badge/posture-fail--closed-b91c1c)  
> Quick jumps: [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)  
> Repo fit: path `schemas/tileset/README.md` · upstream [`../README.md`](../README.md) · sibling schema lane [`../tiler/README.md`](../tiler/README.md) · contract home [`../../contracts/tiler/README.md`](../../contracts/tiler/README.md) · implementation lane [`../../tools/tiler/README.md`](../../tools/tiler/README.md) · downstream [`../../data/catalog/README.md`](../../data/catalog/README.md), [`../../data/receipts/README.md`](../../data/receipts/README.md), [`../../tools/validators/README.md`](../../tools/validators/README.md), [`../../tests/contracts/README.md`](../../tests/contracts/README.md), [`../../docs/standards/KFM_STAC_PROFILE.md`](../../docs/standards/KFM_STAC_PROFILE.md)  
> Accepted inputs: emitted tileset object schemas, asset-inventory schemas, scene-manifest-adjacent schemas, tiny illustrative examples  
> Exclusions: run specs, invocations, receipts, policy decisions, release proofs, renderer code, catalog standards, canonical data

> [!IMPORTANT]
> Current public `main` shows `schemas/tileset/` as a real directory, but only this README is visible in the evidence supplied for this revision. Treat this file as a boundary and placement guide first, not as proof that a settled schema wave already exists.

> [!WARNING]
> In KFM, tilesets are derived delivery artifacts, not sovereign truth objects. Any schema landed here must stay subordinate to released assets, evidence links, catalog closure, and the same trust-visible shell rules that govern 2D.

## Scope

`schemas/tileset/` is the narrow place where KFM can eventually formalize **emitted tileset objects** without collapsing four different concerns into one directory:

- semantic meaning and invariants
- concrete field shape and serialization
- adapter and runtime behavior
- publication, proof, and policy outcomes

That split matters. The repo evidence supplied for this revision already gives:

- `contracts/tiler/` the contract-home role for deterministic tiling runs
- `schemas/tiler/` the schema-home role for run, receipt, and summary objects
- `tools/tiler/` the implementation role
- `data/catalog/` the outward discovery role

This directory should therefore remain **boundary-first** unless and until the repo explicitly decides that *emitted tileset-* and *scene-manifest-shaped* objects deserve their own schema lane.

### Truth labels used here

| Label | Meaning in this README |
|---|---|
| **CONFIRMED** | Directly visible in the supplied repo-facing Markdown or strongly stated in the attached KFM corpus |
| **INFERRED** | Strongly implied by the supplied corpus, but not yet surfaced as checked-in local schema files |
| **PROPOSED** | Recommended next shape for this lane, not yet verified as implemented |
| **UNKNOWN** | Not established by the supplied evidence |
| **NEEDS VERIFICATION** | Current supplied evidence is not enough to settle the claim |

[Back to top](#schemastileset)

## Repo fit

### Where this lane sits

| Neighbor | Role | Why it matters here |
|---|---|---|
| [`../README.md`](../README.md) | parent `schemas/` boundary | establishes subtree posture and the current schema-home ambiguity |
| [`../tiler/README.md`](../tiler/README.md) | existing tiling schema lane | already owns run specs, invocations, receipts, summaries, and related machine objects |
| [`../../contracts/tiler/README.md`](../../contracts/tiler/README.md) | contract home | owns meaning, invariants, and lifecycle semantics for tiling objects |
| [`../../tools/tiler/README.md`](../../tools/tiler/README.md) | implementation lane | emits derived tile artifacts and run memory, not release truth |
| [`../../data/receipts/README.md`](../../data/receipts/README.md) | process memory | receives run receipts; should not be conflated with tileset schemas |
| [`../../data/catalog/README.md`](../../data/catalog/README.md) | STAC / DCAT / PROV closure | carries outward discovery and lineage closure for released artifacts |
| [`../../tools/validators/README.md`](../../tools/validators/README.md) | fail-closed checks | validates shape, linkage, and readiness without owning semantics |
| [`../../tests/contracts/README.md`](../../tests/contracts/README.md) | contract / schema verification | should carry valid / invalid example coverage once schemas land |

### Placement rule

Use `schemas/tileset/` only when the object being described is **about the released tileset or 3D-scene handoff itself**.

Do **not** use it for:

- author-authored run requests
- normalized invocations
- process-memory receipts
- release proofs or attestations
- STAC / DCAT / PROV profiles
- renderer-specific bootstrap or worker code

### First-wave direction

The strongest **PROPOSED** first-wave objects, based on the supplied README baseline and the surrounding lane logic it cites, are:

| Candidate object | Status | Why this is the likely fit |
|---|---|---|
| `tileset_manifest.schema.json` | **PROPOSED** | best single anchor for a released tileset descriptor |
| `tileset_asset_inventory.schema.json` | **PROPOSED** | explicit file list, digests, bounds, hierarchy, and emitted artifact inventory fit this lane better than run-control lanes |
| `scene_manifest.schema.json` | **INFERRED / PROPOSED** | coherent 3D handoff unit is repeatedly implied, but no checked-in schema was verified in the supplied evidence |

> [!NOTE]
> This README now names the likely first-wave schema objects more directly than the prior draft, but still does **not** claim those files already exist.

## Inputs

### What belongs here

| Candidate object | Status | Belongs here? | Why |
|---|---|---:|---|
| `tileset_manifest.schema.json` | **PROPOSED** | Yes, if adopted | a release-facing emitted tileset descriptor is narrower than run control and broader than raw file inventory |
| `tileset_asset_inventory.schema.json` | **PROPOSED** | Yes, if adopted | file list, digests, bounds, hierarchy, and emitted artifact inventory are tileset-shaped, not run-shaped |
| `scene_manifest.schema.json` | **INFERRED / PROPOSED** | Maybe | the supplied corpus repeatedly points to scene manifests as the coherent 3D handoff unit, but no checked-in schema was verified |
| `bounding_volume_summary.schema.json` | **PROPOSED** | Maybe | useful if the repo wants a compact validator-friendly surface for bounds, LOD, or hierarchy review |
| tiny `examples/*.json` | **PROPOSED** | Yes | reviewer-readable examples can help schema adoption, as long as full valid / invalid fixtures live in test lanes |

### Minimal field families any future schema here should expect

A safe first-wave tileset object is likely to need some combination of the following. These are **PROPOSED design families**, not confirmed implemented fields:

- **identity**: object id, version, `spec_hash`, created or updated timestamps
- **artifact linkage**: emitted asset paths, digests, media types, byte sizes
- **spatial interpretation**: CRS or coordinate metadata, bounds, geometric-error or hierarchy summaries
- **release linkage**: release refs, catalog refs, or promoted-subject identifiers
- **evidence continuity**: evidence refs or drawer-parity refs when the object participates in a 3D story handoff
- **status grammar**: bounded machine states when applicable

### Validator-first expectations for a first schema wave

The baseline README already points to validators, tests, receipts, and catalog closure as adjacent lanes. A conservative **PROPOSED** first schema wave should therefore favor objects whose fields are:

- explicit rather than inferred
- diff-friendly
- digest-bearing
- small enough for fail-closed validation
- easy to link downstream without duplicating catalog or proof objects

> [!TIP]
> Keep author-friendly inputs and adapter-facing execution shapes in `schemas/tiler/`. Keep emitted tileset-facing shapes here only if the repo deliberately separates them.

## Exclusions

This directory should **not** become a catch-all 3D bucket.

| Does **not** belong here | Better home |
|---|---|
| `tiling_run_spec`, `tiling_invocation`, `tiling_receipt`, `tile_summary` | [`../tiler/README.md`](../tiler/README.md) + [`../../contracts/tiler/README.md`](../../contracts/tiler/README.md) |
| policy allow or deny logic, sensitivity rules, promotion outcomes | [`../../policy/README.md`](../../policy/README.md) |
| release manifests, attestations, proof packs | release, proof, or validator lanes rather than schema-only placement |
| STAC / DCAT / PROV outward profiles | [`../../docs/standards/KFM_STAC_PROFILE.md`](../../docs/standards/KFM_STAC_PROFILE.md) and `data/catalog/` |
| renderer or bootstrap behavior for Cesium, MapLibre, three.js, workers, or viewers | [`../../tools/tiler/README.md`](../../tools/tiler/README.md) and app or runtime lanes |
| canonical terrain, imagery, or source datasets | upstream data lanes |

## Directory tree

### Current public snapshot

```text
schemas/
└── tileset/
    └── README.md
```

### Safe next expansion if this lane becomes real

```text
schemas/
└── tileset/
    ├── README.md
    ├── tileset_manifest.schema.json           # PROPOSED
    ├── tileset_asset_inventory.schema.json    # PROPOSED
    ├── scene_manifest.schema.json             # PROPOSED / conditional 3D only
    └── examples/                              # PROPOSED, tiny illustrative payloads only
```

> [!NOTE]
> Full valid and invalid fixtures should stay in test lanes rather than turning this directory into an ungoverned example dump.

[Back to top](#schemastileset)

## Quickstart

1. **Decide the object family first.**  
   If the object describes a run, a receipt, or a summary emitted by the tiler lane, stop and place it in `schemas/tiler/` instead.

2. **Land semantic meaning before field shape.**  
   Add or confirm contract meaning in `../../contracts/tiler/` or another explicit contract home before writing a schema file here.

3. **Keep the first schema small.**  
   Prefer one object—most likely `tileset_manifest` or `tileset_asset_inventory`—before splitting into many variants.

4. **Wire fail-closed coverage immediately.**  
   Add at least one valid example and one invalid example to the contract or schema test surface, then wire validator checks.

5. **Link downstream; do not duplicate downstream.**  
   Reference catalog closure, receipts, and proof lanes instead of copying their fields wholesale.

### Starter review checklist

- [ ] Is this object emitted-tileset-shaped rather than run-shaped?
- [ ] Does a contract home already define its meaning?
- [ ] Are digests, bounds, and linkage fields explicit rather than inferred?
- [ ] Does the object stay subordinate to release-backed truth?
- [ ] If it participates in 3D story mode, does it preserve Evidence Drawer parity?

### Illustrative validator-facing sketch

The following is **illustrative only**. It is included to make the first-wave direction concrete without claiming implementation.

```json
{
  "kind": "tileset_manifest",
  "version": "v1",
  "spec_hash": "sha256:...",
  "artifacts": [
    {
      "href": "relative/or/oci/ref",
      "digest": "sha256:...",
      "media_type": "application/json"
    }
  ],
  "bounds": {
    "kind": "region-or-box",
    "summary_ref": "kfm://..."
  },
  "catalog_refs": {
    "stac": "relative-or-kfm-ref",
    "dcat": "relative-or-kfm-ref",
    "prov": "relative-or-kfm-ref"
  },
  "status": "draft"
}
```

## Usage

### A practical placement matrix

| Question | Put it in | Reason |
|---|---|---|
| “What should be tiled, with which adapter, and how?” | `contracts/tiler/` + `schemas/tiler/` | run-control semantics already live there |
| “What happened during the run?” | `schemas/tiler/` + `data/receipts/` | process memory and run results are already defined as receipt or summary territory |
| “Which files, digests, bounds, and hierarchy describe this emitted tileset?” | `schemas/tileset/` | emitted artifact shape fits this lane if the repo formalizes it |
| “How does a conditional 3D scene hand off from the governed 2D shell?” | `schemas/tileset/` **only if** the repo adopts a renderer-neutral scene manifest | the supplied doctrine points to a scene manifest, but this remains partly **INFERRED / PROPOSED** |
| “How is the released asset discoverable and cross-linkable?” | `data/catalog/` + standards docs | catalog closure is downstream of schema shape |
| “Can this object be trusted, promoted, or published?” | validators, policy, and proof lanes | trust decisions do not belong to schema placement alone |

### Conditional 3D rule

The supplied doctrine is clear on one point: 3D is **conditional**, 2D remains primary, and a 3D story mode is coherent only when it stays downstream of the same released assets, evidence links, decision grammar, and Evidence Drawer payload logic as the 2D shell.

That makes `schemas/tileset/` a possible home for **scene-manifest-shaped** objects—but only if they are:

- renderer-neutral enough to survive beyond one engine
- downstream of released assets rather than ambient runtime state
- explicit about evidence, release, and correction linkage
- small enough to validate and review fail-closed

### Validator and test handoff

This README does **not** claim current implementation, but the neighboring lanes it cites imply a clean division of responsibilities once a schema lands:

| Neighbor lane | Expected role once schema files exist | Status |
|---|---|---|
| `tools/validators/` | shape checks, required-field checks, linkage checks | **INFERRED** |
| `tests/contracts/` | valid / invalid fixtures and reviewable failure cases | **INFERRED** |
| `data/catalog/` | outward discovery and closure, not schema authority | **CONFIRMED** in doctrine framing |
| `data/receipts/` | process memory linkage, not release truth | **CONFIRMED** in doctrine framing |

## Diagram

```mermaid
flowchart LR
    A[contracts/tiler<br/>meaning + invariants]
    B[schemas/tiler<br/>run / invocation / receipt / summary]
    C[schemas/tileset<br/>emitted tileset + scene-manifest shapes<br/>(boundary-first today)]
    D[tools/tiler<br/>adapter execution]
    E[data/receipts<br/>process memory]
    F[data/catalog<br/>STAC / DCAT / PROV closure]
    G[tools/validators<br/>fail-closed checks]
    H[governed shell<br/>2D default, 3D conditional]

    A --> B
    A -. semantic prerequisite .-> C
    D --> B
    D --> E
    D --> C
    B --> G
    C --> G
    C --> F
    E --> F
    F --> H
```

## Tables

### Schema design goals for this lane

| Goal | Why it matters |
|---|---|
| Deterministic serialization | tileset descriptors must diff cleanly and validate predictably |
| Explicit linkage | digests, bounds, release refs, and evidence refs should be present, not guessed |
| Reviewer readability | machine objects here should still be inspectable during review |
| Derived-artifact posture | nothing in this lane should pretend to be canonical truth |
| Downstream compatibility | validators, catalog closure, and shell handoff should consume these objects without hidden adapters |

### Candidate first-wave objects

| Object | Recommended first-wave priority | Notes |
|---|---:|---|
| `tileset_manifest` | High | best candidate if the repo wants a single emitted-object anchor |
| `tileset_asset_inventory` | High | pairs well with validator checks for digests, bounds, and hierarchy |
| `scene_manifest` | Medium | doctrine supports it, but exact minimal parity fields are still unsettled |
| `bounding_volume_summary` | Low | useful later if review surfaces need a compact abstraction |
| renderer-specific config blobs | Do not land here | keep implementation detail out of schema authority |

### Truth boundary matrix

| Concern | Sovereign home | Why `schemas/tileset/` is not the sovereign home |
|---|---|---|
| semantics | contracts | schema shape should not replace contract meaning |
| process memory | receipts | receipts capture run memory, replay clues, and operational trace |
| release discovery | catalog | catalog carries outward discovery and provenance closure |
| trust decision | policy / proof / validators | schema presence alone is not authorization, promotion, or release proof |
| viewer behavior | runtime / tools | engines and viewers consume outputs; they do not define schema authority |

[Back to top](#schemastileset)

## Task list

### Definition of done for turning this from boundary to real lane

- [ ] Confirm whether `schemas/tileset/` should stay boundary-only or become a distinct schema-home for emitted tileset objects.
- [ ] Publish one contract-backed object meaning for a tileset-facing schema.
- [ ] Add one JSON Schema file plus one valid and one invalid example.
- [ ] Wire a validator check and a contract-facing test.
- [ ] Document downstream linkage expectations to `data/catalog/`, `data/receipts/`, and validation lanes.
- [ ] If `scene_manifest` lands here, define a minimal drawer-parity checklist before broader 3D rollout.

### Explicit gates before broader 3D adoption

- [ ] one terrain-bearing story node only
- [ ] same released-asset refs as the 2D shell
- [ ] same Evidence Drawer payload family, or an explicitly justified subset
- [ ] clear correction path
- [ ] validator-visible parity fixture

### Review questions for the first schema PR

- [ ] Does the object reduce ambiguity, or just create a second naming system?
- [ ] Is every trust-bearing link explicit?
- [ ] Could a reviewer understand the object without reading runtime code?
- [ ] Would the object still make sense if the renderer changed?
- [ ] Does the placement keep `receipt ≠ proof ≠ catalog ≠ publication` visible?

## FAQ

### Is `schemas/tileset/` already a settled schema home?

No. **CONFIRMED**: the supplied repo-facing draft shows the directory exists. **NEEDS VERIFICATION**: no checked-in schema files were visible in the supplied evidence set for this revision.

### Why not just put everything in `schemas/tiler/`?

Because emitted tileset objects may deserve a narrower lane than run-control objects. But that split should happen only when it improves clarity rather than multiplying dialects.

### Does this directory authorize Cesium-specific or MapLibre-specific runtime behavior?

No. Runtime behavior belongs in implementation lanes. This directory, if expanded, should stay at the level of machine-readable shape for emitted artifacts or renderer-neutral scene handoff objects.

### Are scene manifests already implemented in the repo?

Not from the evidence supplied here. They are **INFERRED / PROPOSED** from the attached corpus as the coherent unit for conditional 3D handoff, but no mounted or checked-in schema file was directly verified in this path.

## Appendix

<details>
<summary><strong>Illustrative starter sketch — <code>scene_manifest</code> (PROPOSED)</strong></summary>

This is an illustrative shape sketch, not a confirmed repo contract.

```json
{
  "scene_id": "hydrology-story-node-001",
  "spec_hash": "sha256:...",
  "released_assets": [
    {
      "href": "oci://... or relative asset ref",
      "digest": "sha256:...",
      "media_type": "application/json"
    }
  ],
  "camera": {
    "entry": "named pose or path ref",
    "exit": "named pose or path ref"
  },
  "layers": [
    {
      "id": "terrain",
      "kind": "terrain_3dtiles_1_1",
      "required": true
    }
  ],
  "evidence_refs": [
    "kfm://evidence/..."
  ],
  "drawer_payload_ref": "kfm://drawer/...",
  "catalog_refs": {
    "stac": "relative-or-kfm-ref",
    "dcat": "relative-or-kfm-ref",
    "prov": "relative-or-kfm-ref"
  },
  "status": "draft"
}
```

A safe first implementation would keep this object small, explicit, and downstream of released assets.

</details>

<details>
<summary><strong>Open verification items</strong></summary>

- Whether `schemas/tileset/` should become a real schema-home or remain boundary-only
- Whether path-specific ownership exists beyond the public fallback owner shown in the supplied draft
- Whether a scene-manifest contract already exists elsewhere in the repo
- Whether `tileset_manifest` or `tileset_asset_inventory` is the preferred first landed object
- Whether adjacent validator and test lanes already have conventions specific to emitted tileset artifacts

</details>
