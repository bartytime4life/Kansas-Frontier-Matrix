<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/receipts/representation-receipt
title: RepresentationReceipt Contract
type: semantic-contract; process-memory; representation-boundary
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Receipt steward · Representation steward · Evidence steward · Validation steward
created: 2026-08-04
updated: 2026-08-04
policy_label: public; representation; process-memory; evidence-bound; non-publisher
related:
  - ./README.md
  - ../../schemas/contracts/v1/receipts/representation_receipt.schema.json
  - ../../fixtures/contracts/v1/receipts/representation_receipt/
  - ../../tools/validators/validate_representation_receipt.py
  - ../../tests/validators/test_validate_representation_receipt.py
tags: [kfm, representation-receipt, tiles, 3d, generalization, evidence, reality-boundary]
[/KFM_META_BLOCK_V2] -->

# RepresentationReceipt

> `RepresentationReceipt` records a deterministic transformation from evidence-bound
> input artifacts into a downstream representation. It makes information loss,
> generalization, aggregation, modeling, or synthetic reconstruction visible without
> allowing the representation to become evidence, policy, review, release, or
> publication authority.

## Purpose

KFM maps, tiles, raster overviews, generalized vectors, 3D scenes, synthetic surfaces,
and export snapshots are carriers. They may differ materially from the evidence they
depict. This receipt binds one representation to:

- one subject and at least one `EvidenceBundle` reference;
- exact input and output artifact digests;
- a versioned method and method-spec digest;
- declared evidence and representation fidelity;
- explicit information-loss posture;
- a `RealityBoundaryNote` when output is modeled, synthetic, or a 3D scene;
- represented and input-as-of times;
- correction/supersession lineage;
- a fixed no-authority governance boundary.

## Finite representation types

| Type | Intended use |
|---|---|
| `MAP_TILE` | Vector/raster tile or PMTiles carrier. |
| `RASTER_OVERVIEW` | Downsampled or pyramided raster overview. |
| `VECTOR_GENERALIZATION` | Simplified, snapped, aggregated, or public-safe geometry. |
| `THREE_D_SCENE` | Terrain, extrusion, point cloud, glTF, or 3D Tiles scene. |
| `SYNTHETIC_SURFACE` | Reconstructed, modeled, interpolated, or simulated surface. |
| `EXPORT_SNAPSHOT` | Time-bound report, story, image, or data export. |

## Fidelity vocabulary

`EXACT`, `GENERALIZED`, `AGGREGATED`, `MODELED`, and `SYNTHETIC` describe how
closely the carrier follows its supporting evidence. `EXACT` does not mean the evidence
itself is true or release-ready; it means the representation claims no additional fidelity
loss beyond the declared encoding.

The validator requires:

1. `EXACT` output to declare `information_loss=false`;
2. `GENERALIZED`, `AGGREGATED`, and `SYNTHETIC` output to declare
   `information_loss=true`;
3. `THREE_D_SCENE`, `SYNTHETIC_SURFACE`, `MODELED`, or `SYNTHETIC`
   output to reference a `RealityBoundaryNote`;
4. input-as-of time not to follow represented time;
5. canonical, unique arrays and non-placeholder SHA-256 digests;
6. no self-supersession;
7. all governance authority flags to remain false and `release_ref` to remain null.

## Responsibility boundary

| This receipt records | It does not establish |
|---|---|
| Input/output byte identity | Source truth or evidence admissibility |
| Method identity and parameters | Policy approval |
| Fidelity and information loss | Human review |
| Reality-boundary linkage | Promotion or release |
| Replay and supersession context | Public-use permission |
| Process memory | Publication or rollback execution |

## Lifecycle

```text
governed evidence / processed artifact
  -> representation transform
  -> RepresentationReceipt + candidate carrier
  -> validation / policy / review / release gates
  -> released public-safe carrier
```

A passing receipt can accompany WORK, PROCESSED, or release-candidate material. It
cannot write `PUBLISHED` or make an unreleased carrier public.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_representation_receipt.py' \
  --verbose

python tools/validators/validate_representation_receipt.py --fixtures
```

The validator performs no network access. Diagnostics contain finding codes and JSON
pointers, not candidate values.

## Rollback and correction

Reverting this contract removes the proposed validation profile but does not erase emitted
process memory. A corrected representation emits a new receipt and links it through
`supersedes`/`superseded_by`; downstream release correction and rollback remain owned
by their governing object families.
