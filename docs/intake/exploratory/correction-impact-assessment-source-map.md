# Correction Impact Assessment — Source Map

Status: **PROPOSED**, exploratory adaptation only.

This slice adapts the KFM correction doctrine that corrections, withdrawals, supersessions, cache invalidation, and rollback must propagate through downstream public and interpretive surfaces. The Briefing-to-System blueprint explicitly requires correction behavior to reach manifests, caches, maps, search, and AI surfaces before a public product is considered mature. The connected KFM doctrine likewise treats maps, tiles, graphs, exports, and AI answers as downstream carriers rather than sovereign truth.

`CorrectionImpactAssessment` turns that propagation burden into a fixture-first validation object. It does not replace `CorrectionNotice`, `PolicyDecision`, `ReleaseManifest`, review evidence, or rollback authority, and it does not execute a correction.

Placement follows accepted Directory Rules v2 and ADR-0029: meaning under `contracts/`, shape under `schemas/`, fixtures under `fixtures/`, validation under `tools/`, tests under `tests/`, and generated authoring provenance under `data/receipts/generated/`.
