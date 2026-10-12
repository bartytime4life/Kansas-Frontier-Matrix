# GeoParquet 2.0 RC Compatibility Assessment

Status: `PROPOSED_INACTIVE`

Profile: `kfm.geoparquet-2-rc-compatibility-assessment.v2`

This profile implements the bounded `DUAL_EVALUATE` route described by proposed ADR-0033. It evaluates whether a declared, synthetic, exact-toolchain packet is complete enough to proceed to separately reviewed GeoParquet-byte probes for `2.0.0-rc.1`.

It does **not** change KFM's declared GeoParquet `1.1.0` default, open or generate Parquet bytes, install any tool, authenticate a package artifact, migrate data, accept ADR-0033, or authorize release or publication.

## Upstream checkpoint

The candidate remains fixed to GeoParquet `2.0.0-rc.1` at upstream commit `0c7fab74cf1177e2fe61df8eb7fcd1813b73e4aa`.

The assessment records the 2.0 storage boundary without treating the release candidate as final:

- root geometry columns use Parquet `GEOMETRY` or `GEOGRAPHY` logical types;
- the physical representation remains `BYTE_ARRAY` with `WKB` encoding;
- the native Parquet logical-type CRS property is authoritative;
- optional GeoParquet metadata may restate that CRS as inline PROJJSON but must be semantically equivalent;
- Parquet-native row-group spatial statistics replace a universal GeoParquet 1.1 covering-column requirement; and
- existing 1.1 fixtures and receipts remain historical compatibility evidence.

## Exact proposed toolchain matrix

The profile declares four distinct execution surfaces and one footer inspector. Version recognition is not support evidence, and a Git tag is not a package-integrity proof.

1. **GDAL `3.13.2`** — source tag commit `b40672525acf3f5c4f29d8541aa7dcff1e18eb92`; producer, consumer, native-type, CRS, row-group-statistics, metadata, and 1.1 checks.
2. **DuckDB `1.5.5`** — source tag commit `d8cdaa33fda8df955cc76ef58a280f68f4cd43fa`; exact `spatial@1.5.5` artifact and digest; read, query, pruning, CRS, metadata, and 1.1 checks.
3. **SedonaSpark `1.9.0`** — source tag commit `34098262086a6137d105cd8d9e0b366e4a8246c0`; Spark `3.5.9` at `7c14a3c28b141cc97a330c4d0f5d2a6da7267f85`, Java `11`, Scala `2.12.18`, and Spark-resolved parquet-java `1.13.1`. SedonaSpark's documented GeoParquet 1.1 and CRS behavior is a baseline only; it does not prove 2.0-RC support.
4. **SedonaDB `0.4.0`** — a separate single-node execution surface. Its release documentation describes draft GeoParquet 2.0 geometry/geography writing and statistics; this declaration still requires actual carrier-byte proof.
5. **PyArrow `25.0.0` inspector** — footer logical-type and row-group-statistics inspection only. It is not a substitute for producer/consumer behavior.

Every lane requires an exact version, exact source reference, artifact digest, unique evidence reference, finite probe statuses, and explicit rejection of unsupported assumptions. DuckDB's extension and SedonaSpark's Spark distribution require separate digests.

## Finite outcomes

- `READY` — the exact declared packet is structurally complete and all synthetic statuses are `PASS`; this means **ready to execute byte probes**, not cross-engine compatible.
- `HOLD` — the packet is well formed but probes are pending or failed, a tool is intentionally unpinned, or unsupported assumptions do not fail closed.
- `ERROR` — the packet is malformed, selects a different version/source/transitive dependency, uses an invalid artifact digest, collapses the Sedona surfaces, reuses evidence identity, misstates the RC/default boundary, carries a 1.x-only covering assumption into 2.0, contains contradictory CRS declarations, changes governance state, or declares an outcome different from the computed result.

## Required next evidence after READY

A later dependency-closed execution PR must generate or capture deterministic 1.1 and 2.0-RC carrier bytes and run the exact pinned artifacts. It must inspect native logical types, round-trip CRS, demonstrate correct row-group pruning or an explicit unsupported result, preserve unknown metadata, retain 1.1 read coverage, reject malformed carriers, and bind every command, log, result, package, extension, container, and carrier to immutable digests.

## Authority boundary

This profile is a readiness classifier only. It is not a `ValidationReport`, `EvidenceBundle`, `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, migration receipt, correction notice, rollback card, signature, or publication proof. No result changes lifecycle state or permits public use.

## Rollback

Before merge, close the draft PR. After an authorized merge, revert this bounded profile revision, workflow, tests, fixtures, and successor receipt. No data or external-system cleanup is required because the profile is synthetic and no-network.
