<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/watcher-registry
title: Governed Watcher Registry Contract
type: semantic-contract; control-plane-register; watcher-boundary; fixture-first
version: v0.1.0
status: proposed; inactive; no-network; non-publisher
owners: OWNER_TBD — Watcher steward · Source steward · Pipeline-spec steward · Validation steward · Policy steward · Release steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; source; watcher; registry; non-publisher; no-live-activation
related:
  - ../../pipeline_specs/watchers/README.md
  - ../../control_plane/watcher_registry.json
  - ../../schemas/contracts/v1/source/watcher_registry.schema.json
  - ../../tools/validators/validate_watcher_registry.py
  - ../../fixtures/contracts/v1/source/watcher_registry/
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, watcher, registry, source, control-plane, deterministic, fixture-first]
[/KFM_META_BLOCK_V2] -->

# Governed Watcher Registry Contract

> The `WatcherRegistry` is a machine-readable control-plane index of watcher identities, declarative specification paths, source/activation references, comparison capabilities, expected outputs, and explicit non-authority state. It does not activate, schedule, execute, admit, promote, release, publish, or notify.

## Source-derived requirement

Pass 31 proposes a watcher registry with stable watcher identity, canonical identity, endpoint/poll/policy/output references, schema identity, version, `spec_hash`, and signature reference. The repository already has a shared watcher specification boundary but no active shared registry. This contract introduces a fixture-first registry projection without converting the existing `plants_drift.yaml` placeholder into an active watcher.

## Responsibility split

| Responsibility | Home |
|---|---|
| Registry semantics | `contracts/source/watcher_registry.md` |
| Machine shape | `schemas/contracts/v1/source/watcher_registry.schema.json` |
| Machine projection | `control_plane/watcher_registry.json` |
| Declarative watcher intent | `pipeline_specs/watchers/` or a verified domain watcher lane |
| Executable validation | `tools/validators/validate_watcher_registry.py` |
| Synthetic evidence | `fixtures/contracts/v1/source/watcher_registry/` |
| Focused tests | `tests/validators/test_validate_watcher_registry.py` |

The placement follows adopted Directory Rules v2: semantic meaning belongs to `contracts/`, machine shape to `schemas/`, cross-system governance indexes to `control_plane/`, and executable checking to `tools/validators/`.

## Entry states

| State | Meaning | Mandatory boundary |
|---|---|---|
| `PLACEHOLDER` | An inventory path exists, but stable activation, source, policy, schema, consumer, and output bindings do not. | All authority refs remain null; capabilities and outputs are empty; every governance flag is false. |
| `INACTIVE` | A reviewed identity may exist, but activation is not effective. | No source activation or lifecycle/public authority. |
| `ACTIVE` | An external accepted activation record is referenced. | Source descriptor, activation, endpoint, policy, schema, signature, and outputs must be present; the registry still grants no RAW, promotion, release, or publication authority. |
| `SUSPENDED` | Execution is held pending correction, source, security, rights, or policy review. | No execution/public authority; reasons must be visible to reviewers. |
| `RETIRED` | The watcher identity is preserved for lineage but must not execute. | No activation or public authority. |

## Deterministic identity and integrity

- `watcher_id`, `canonical_id`, and `spec_path` are unique.
- Entries are sorted by `watcher_id`.
- `spec_path` is a canonical repository-relative path under `pipeline_specs/`.
- `spec_sha256` binds the entry to exact declarative bytes.
- The registry `spec_hash` is RFC 8785 JCS plus SHA-256 over the registry object with `spec_hash` omitted.
- Capability and output arrays use canonical ordering.

## Non-effects

A valid registry proves only deterministic shape, ordering, reference syntax, and exact declarative-byte binding. It does not prove that a source is authoritative, rights-cleared, current, reachable, sensitive-safe, or activated. It does not prove that a watcher implementation, scheduler, receipt writer, review path, release gate, or public product exists.

Watchers remain candidate-signal emitters and non-publishers. A changed ETag, timestamp, checksum, manifest, or endpoint response does not by itself establish material domain change.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive registry packet. The existing watcher placeholder remains unchanged, and no live source, schedule, lifecycle record, release, cache, or public artifact is modified.
