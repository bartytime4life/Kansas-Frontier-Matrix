<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/publication-validator-compatibility-source-map
title: Publication Manifest Validator Compatibility Source Map
type: source-map; exploratory-intake; implementation-lineage
version: v1.1.0
status: proposed; repository-grounded; compatibility-only; fixture-only; no-network
owners: OWNER_TBD — Validator steward · Data steward · Release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; validators; release; no-publication-authority
owning_root: docs/
responsibility: Record the evidence, bounded compatibility decision, exact-head correction, validation, and rollback for replacing two obsolete root manifest-validator stubs with delegation-only entrypoints.
truth_posture: CONFIRMED repository and source evidence / PROPOSED compatibility change pending review / NEEDS VERIFICATION hosted checks and consumer inventory
[/KFM_META_BLOCK_V2] -->

# Publication Manifest Validator Compatibility Source Map

## Goal

Replace the obsolete root `LayerManifest` and `ReleaseManifest` validator stubs with thin compatibility entrypoints that delegate to the already-implemented canonical fixture validators. Preserve one semantic implementation per concern and create no release or publication authority.

## Source and repository basis

Google Drive `New Ideas 5-19-26` repeatedly emphasizes manifest-bound map artifacts, explicit release objects, correction, and rollback. KFM MapLibre and greenfield doctrine keep those objects downstream of evidence, policy, review, release, correction, and rollback gates. At `main@ef1ba46a19e4de7c176e9d093c1285e73a0af75a`, the root paths below existed as `NotImplementedError("Greenfield placeholder")` stubs while canonical fixture validators already existed:

| Object | Compatibility path | Canonical implementation |
|---|---|---|
| `LayerManifest` | `tools/validators/validate_layer_manifest.py` | `tools/validators/data/validate_layer_manifest.py` |
| `ReleaseManifest` | `tools/validators/validate_release_manifest.py` | `tools/validators/release/validate_release_manifest.py` |

The repository's citation-validation compatibility entrypoint establishes the same delegation-only pattern.

## Exact-head narrowing

The first branch head also delegated the root `RollbackCard` path. Hosted `rollback-drill` failed because current repository control deliberately requires `tools/validators/validate_rollback_card.py` to remain an explicit stub/hold until separate rollback adoption criteria are met. The repair restores that file byte-for-byte and removes it from this packet. This PR therefore fixes only the two manifest entrypoints whose canonical validators are already admitted by current workflows.

## Bounded implementation

Each compatibility module imports and exposes the exact canonical `main` function, adds no wrapper semantics, and exits through that function when invoked directly. Tests prove function-object identity and fixture replay. The read-only workflow runs only repository-owned fixtures and validates the generated authoring receipt.

This packet does **not** change schemas, contracts, policies, canonical validator semantics, fixtures, release state, correction state, rollback execution, or publication state. It does not remove or deprecate any path.

## Directory Rules basis

Existing root files receive same-path `PLACE` treatment as compatibility entrypoints under `tools/`. Canonical semantics remain in their current responsibility sub-lanes. Tests remain under `tests/`, hosted orchestration under `.github/`, lineage under `docs/`, and generated authoring provenance under `data/receipts/generated/`. No parallel authority is created.

## Acceptance

- each root module exports the exact canonical `main` object;
- each root `--fixtures` command returns the canonical success code;
- the root wrappers contain no validation, policy, review, release, or publication logic;
- workflow permissions remain `contents: read`, no-network, and SHA-pinned;
- generated-receipt hashes bind every AI-authored artifact except the receipt itself;
- hosted exact-head checks and a complete consumer inventory remain separate verification items.

## Rollback

Before merge, close the draft PR and abandon the branch. After an authorized merge, restore prior root stubs `6f4b2593122db6b1774bdbd79bad9d8b0f7d7aba` and `8af7a463d9776793ce6d0ec56a09282023845192`, then remove the additive test, workflow, source map, and generated receipt. No manifest, lifecycle, release, deployment, cache, rollback execution, or public artifact requires restoration.
