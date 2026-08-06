# Synthetic SSURGO/SDA Micro-Snapshot Diff Contract

**Status:** PROPOSED fixture-only implementation contract
**Owning responsibilities:** `contracts/` defines meaning; `tools/ingest/ssurgo_watch/` owns the deterministic repository helper
**Release posture:** review signal only; promotion and publication are always false

## Purpose

This contract adapts the supplied SSURGO/gSSURGO watcher idea into a bounded, no-network proof. It validates a tiny synthetic Soil Data Access-style component snapshot, computes stable content and retrieval fingerprints, and produces a field-level diff for steward review.

The helper does not select a live NRCS endpoint, execute an SDA query, download SSURGO/gSSURGO, write RAW or WORK data, emit or sign an operational RunReceipt, evaluate OPA policy, promote, release, or publish.

## Snapshot rules

A snapshot must contain synthetic `mukey` and `cokey` identities, component percentages, representative slope, drainage class, source metadata, retrieval time, and evidence references.

Deterministic validation requires:

- at least one map unit and one row;
- unique `(mukey, cokey)` identity and globally unique synthetic `cokey`;
- component percentages in `[0, 100]` and a per-`mukey` sum within one percentage point of `100`;
- `slope_r` in `[0, 100]`;
- canonical UTC retrieval time;
- fixture-only source identity and evidence references; and
- no unknown fields.

## Hash separation

`content_spec_hash` includes source identity, product version, ETag, and canonical rows. `retrieval_hash` additionally includes retrieval time and evidence references. This intentionally prevents a new retrieval timestamp by itself from being misrepresented as material source change while preserving auditability of each retrieval attempt.

## Diff semantics

- Product-version or ETag change is material metadata change.
- Added or removed component rows are material.
- Changes to `component_pct`, `slope_r`, or `drainage_class` are material and listed as old-to-new field changes.
- Row order and retrieval timestamp alone are non-material.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `NO_MATERIAL_CHANGE` | Both snapshots validate and no source metadata or canonical row content changed. |
| `PROPOSED_WORK_RECORD` | A validated metadata or row change requires governed review. |
| `VALIDATION_HOLD` | One or both snapshots fail deterministic identity, percentage, range, or shape checks. |
| `ERROR` | Input bytes cannot be parsed safely. |

`PROPOSED_WORK_RECORD` is not lifecycle state, proof, policy, promotion, release, or publication authority.

## Rollback

The slice is additive. Removing its helper, tests, fixtures, schema, workflow, contract, and generated authoring receipt restores prior repository behavior without migration.
