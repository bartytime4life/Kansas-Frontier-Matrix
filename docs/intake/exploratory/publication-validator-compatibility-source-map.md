<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/publication-validator-compatibility-source-map
title: Publication Validator Compatibility Source Map
type: source-map; exploratory-intake; implementation-lineage
version: v1.0.0
status: proposed; repository-grounded; compatibility-only; fixture-only; no-network
owners: OWNER_TBD — Validator steward · Data steward · Release steward · Correction and rollback steward
authority_class: non-authoritative lineage and review context
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; validators; release; rollback; no-publication-authority
owning_root: docs/
responsibility: Record the evidence, placement, bounded compatibility decision, validation, and rollback for replacing three obsolete root validator stubs with delegation-only entrypoints.
truth_posture: CONFIRMED repository and source evidence / PROPOSED compatibility change pending review / NEEDS VERIFICATION hosted checks and consumer inventory
related:
  - ../../../tools/validators/validate_layer_manifest.py
  - ../../../tools/validators/data/validate_layer_manifest.py
  - ../../../tools/validators/validate_release_manifest.py
  - ../../../tools/validators/release/validate_release_manifest.py
  - ../../../tools/validators/validate_rollback_card.py
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_publication_validator_compatibility.py
  - ../../../.github/workflows/publication-validator-compatibility.yml
notes:
  - "Compatibility wrappers delegate to existing canonical implementations and add no semantic, policy, review, release, rollback-execution, or publication logic."
  - "The change preserves existing root paths for callers while eliminating guaranteed NotImplementedError failures."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Publication Validator Compatibility Source Map

## Goal

Replace three obsolete root-level greenfield validator stubs with thin, tested compatibility entrypoints that delegate to the already-implemented canonical validator lanes for `LayerManifest`, `ReleaseManifest`, and `RollbackCard`.

## Source basis

| Source | Status | Contribution | Limit |
|---|---|---|---|
| Google Drive `New Ideas 5-19-26` | `CONFIRMED` discovery source | Repeated pressure for manifest-bound publication, PMTiles/sidecar integrity, explicit release objects, correction, and rollback. | Proposal pressure; not proof that a specific validator path is current. |
| KFM MapLibre Operating Architecture | `CONFIRMED` doctrine / `PROPOSED` realization | Map artifacts remain downstream carriers and require manifest, evidence, policy, release, correction, and rollback context. | Does not authorize release or a public layer. |
| KFM Definitive Greenfield Building Plan v1.1 | `CONFIRMED` doctrine / `PROPOSED` realization | Publication is a governed transition; manifests and rollback are separate trust objects. | Greenfield path examples do not outrank current repository evidence. |
| Current repository root entrypoints | `CONFIRMED` implementation evidence | All three root files exist but raise `NotImplementedError("Greenfield placeholder")`. | File presence proves only a broken compatibility surface. |
| Current canonical validator lanes | `CONFIRMED` implementation evidence | Implemented deterministic fixture-only validators exist under `tools/validators/data/` and `tools/validators/release/`. | A passing fixture profile does not approve release or publication. |
| Existing citation compatibility entrypoint | `CONFIRMED` repository pattern | `tools/validators/validate_citation_validation.py` delegates to one canonical implementation without duplicating semantics. | Pattern evidence only; each target still needs exact-path verification. |

## Pinned repository finding

Baseline: `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a`.

| Object | Root entrypoint | Canonical implementation | Finding |
|---|---|---|---|
| `LayerManifest` | `tools/validators/validate_layer_manifest.py` blob `6f4b2593122db6b1774bdbd79bad9d8b0f7d7aba` | `tools/validators/data/validate_layer_manifest.py` blob `577d31795caaf6712132e73189af18d318ac0e8a` | Root path is a guaranteed failure; canonical fixture validator is implemented. |
| `ReleaseManifest` | `tools/validators/validate_release_manifest.py` blob `8af7a463d9776793ce6d0ec56a09282023845192` | `tools/validators/release/validate_release_manifest.py` blob `00307dc0d5e2c3867a229076e3702f8111455425` | Root path is a guaranteed failure; canonical fixture validator is implemented. |
| `RollbackCard` | `tools/validators/validate_rollback_card.py` blob `b80dd40e93733c7fa76f8f9a78e9ec55b6090b4b` | `tools/validators/release/validate_rollback_card.py` blob `9e9ed5a92851935b41a36698e4bead13ef4edf57` | Root path is a guaranteed failure; canonical fixture validator is implemented. |
| Open overlap | none found | — | No open pull request matched the exact root entrypoints or compatibility task at preflight. |

## Bounded implementation decision

Each root file becomes a compatibility shim that:

1. adds the repository root to `sys.path` when executed directly;
2. imports `main` from the verified canonical module;
3. exposes that exact function without wrapping, changing arguments, findings, outcomes, output, or exit codes; and
4. exits through the canonical function when invoked as a script.

The slice also adds:

- tests proving object identity between each compatibility `main` and canonical `main`;
- tests replaying the canonical fixture profile through each root entrypoint;
- a read-only, no-network workflow; and
- a generated authoring receipt.

The slice does not:

- change any manifest, rollback, or release schema;
- edit canonical validator semantics or fixtures;
- execute a rollback or lifecycle transition;
- approve evidence, policy, review, promotion, release, or publication;
- create a new validator authority or parallel implementation;
- remove, move, or deprecate a public path without consumer inventory and review.

## Directory Rules basis

The existing root files receive same-path `PLACE` treatment as compatibility entrypoints under `tools/`. Canonical semantics remain in their current responsibility sub-lanes:

```text
tools/validators/data/validate_layer_manifest.py
tools/validators/release/validate_release_manifest.py
tools/validators/release/validate_rollback_card.py
```

The wrappers contain no validation logic and therefore do not create parallel authority. Tests remain under `tests/`, hosted orchestration under `.github/`, lineage under `docs/`, and generated-work provenance under `data/receipts/generated/`.

## Acceptance and validation

- each root module exports the exact canonical `main` object;
- each root `--fixtures` command returns the canonical success code;
- no compatibility file contains contract, schema, policy, release, or rollback logic;
- workflow permissions remain `contents: read`, with no secrets, OIDC, artifacts, comments, releases, deployments, or writes;
- generated receipt hashes bind all AI-authored files except the receipt itself;
- hosted exact-head results and a full consumer inventory remain `NEEDS VERIFICATION`.

## Rollback
Before merge, close the draft pull request and abandon the branch. After an authorized merge, restore the three prior stub blobs and remove the additive test, workflow, source map, and generated receipt through a reviewed correction. No manifest, lifecycle state, release, deployment, cache, rollback execution, or public artifact requires restoration.

[Back to top](#top)
