<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/temporal/src/temporal
title: Temporal module boundary
type: module-readme
version: v0.4.0
status: proposed; fixture-first; no-network
updated: 2026-09-05
responsibility_root: packages/
[/KFM_META_BLOCK_V2] -->

# temporal module

This module is the implementation companion for kfm.temporal.view-state.v1. It provides deterministic local operations only:

- typed boundary normalization that preserves raw values and rejects unknown zones/deep-time profiles as bounded outcomes;
- query/mode validation without turning presentation settings into evidence semantics;
- state/query identity derivation over canonical JSON;
- frame-context checks that prevent withheld metadata leaks;
- request, commit, and failure transitions guarded by a monotonically increasing generation.

It does not fetch sources, resolve EvidenceBundles, make policy or release decisions, write databases, or publish. Callers must bind results to the existing governed query/evidence/release objects.
