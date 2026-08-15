# GeoParquet 2.0 RC Compatibility Assessment

Status: `PROPOSED_INACTIVE`

Profile: `kfm.geoparquet-2-rc-compatibility-assessment.v1`

This profile implements the bounded `DUAL_EVALUATE` route described by proposed ADR-0033. It evaluates whether a declared, synthetic cross-engine evidence packet is complete enough to proceed to separately reviewed GeoParquet-byte probes for `v2.0.0-rc.1`.

It does **not** change KFM's declared GeoParquet `1.1.0` default, open Parquet bytes, install GDAL, DuckDB, or Sedona, authenticate tool output, migrate data, accept ADR-0033, or authorize release or publication.

## Upstream checkpoint

The candidate is fixed to GeoParquet `v2.0.0-rc.1`. The assessment records the 2.0 storage boundary without treating the release candidate as final:

- root geometry columns use Parquet `GEOMETRY` or `GEOGRAPHY` logical types;
- the physical representation remains `BYTE_ARRAY` with `WKB` encoding;
- the native Parquet logical-type CRS property is the source of truth;
- optional GeoParquet metadata may restate that CRS as inline PROJJSON but must be semantically equivalent;
- Parquet-native row-group spatial statistics replace a universal GeoParquet 1.1 covering-column requirement; and
- existing 1.1 fixtures and receipts remain historical compatibility evidence.

## Required engine matrix

One candidate must declare exactly three bounded lanes:

1. **GDAL** — producer and consumer checks;
2. **DuckDB** — query-consumer checks; and
3. **Sedona** — a Sedona-facing workflow-consumer check.

Every lane records a pinned tool version, a non-authoritative evidence reference, the required native-type/CRS/statistics/legacy-read checks, and finite behavior for unsupported assumptions. The profile reads only these declarations. A synthetic `PASS` fixture proves classifier logic, not actual support in any tool version.

## Finite outcomes

- `READY` — the declared packet is structurally complete and all required synthetic check statuses are `PASS`; this means **ready for byte probes**, not compatible for production.
- `HOLD` — the packet is well formed but checks are pending, failed, unpinned, or do not fail closed on unsupported assumptions.
- `ERROR` — the packet is malformed, misstates the RC/default boundary, carries a 1.x-only covering assumption into 2.0, contains contradictory CRS declarations, changes governance state, or declares an outcome different from the computed result.

## Required next evidence after READY

A later dependency-closed PR must generate or capture deterministic 1.1 and 2.0-RC Parquet fixtures and run pinned tools. It must inspect native logical types, round-trip CRS, demonstrate row-group spatial pruning, preserve unknown metadata, retain 1.1 read coverage, and verify explicit reject-or-warn behavior for unsupported assumptions. Tool logs and carrier digests must be independently reviewable.

## Authority boundary

This profile is a readiness classifier only. It is not a `ValidationReport`, `EvidenceBundle`, `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, migration receipt, correction notice, rollback card, signature, or publication proof. No result changes lifecycle state or permits public use.

## Rollback

Before merge, close the draft PR. After an authorized merge, revert this additive family, workflow, tests, fixtures, and generated receipt. No data or external system cleanup is required because the profile is synthetic and no-network.
