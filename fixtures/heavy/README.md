# Heavy runtime fixtures

`fixtures/heavy/`

Status: draft / runtime fixture lane / heavy synthetic stress scenarios.

This directory is for heavy, public-safe, synthetic runtime fixture corpora used to exercise renderer smoke tests, performance governance, memory/throughput checks, map runtime behavior, tile loading, benchmark-style comparisons, and documentation examples when a small fixture is not enough.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, canonical truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Heavy fixture posture

Use this lane for stress-sized runtime inputs only when the fixture purpose cannot be met by `fixtures/slim/`, a domain-specific fixture lane, or `tests/fixtures/`. Heavy fixtures should be deterministic, reproducible, public-safe, and documented with source/generation notes when added.

The root fixture README identifies `fixtures/` as runtime/benchmark fixture corpora for renderer smoke tests and performance governance. It lists PMTiles benchmark datasets, MLT benchmark datasets, MapLibre runtime fixtures, Cesium runtime fixtures, public-safe generalized geospatial corpora, and slim/heavy renderer stress scenarios as accepted purposes.

Large fixture corpora require explicit repo decision, external storage, or Git LFS according to root fixture rules. This README does not authorize adding large binary payloads, real source extracts, sensitive exact geometry, or release-like datasets.

## Placement basis

This lane belongs under `fixtures/` because it contains runtime benchmark inputs and stress-test examples. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile publication root, artifact root, or public publication root.

The root fixture README separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to sibling fixture lanes

| Lane | Relationship |
|---|---|
| `../slim/` | Preferred home for small renderer/runtime fixtures where possible. |
| `../golden/` | Expected-output fixtures for stable synthetic inputs. Heavy fixtures may have golden outputs, but expected outputs should remain compact. |
| `../ecology/` | Cross-domain ecology fixture root; use that lane for ecology-specific synthetic examples. |
| `../fauna/` | Fauna compatibility/staging fixture root; use it for Fauna-specific synthetic examples. |
| `../generated_receipt/` | Generated-receipt fixture root; use it for receipt-shape and receipt-validation examples. |
| `../domains/` | Preferred root for domain-owned fixtures. Heavy domain fixtures should usually live under the owning domain unless they are runtime-wide. |
| `../../tests/fixtures/` | Test-only fixture home; use it for deterministic test fixtures that are not runtime/benchmark corpora. |
| `../../artifacts/` | Generated CI output home; do not treat generated artifacts as fixture authority. |
| `../../data/` | Governed lifecycle data root; real data belongs there, not here. |

## Accepted material

This lane may contain:

- documented synthetic PMTiles, MLT, MapLibre, Cesium, vector-tile, GeoJSON, JSON, JSONL, SVG, YAML, or Markdown stress examples;
- public-safe generalized geospatial corpora built for runtime/load testing;
- toy stress scenarios for layer counts, feature counts, tile count, zoom ranges, attribution display, style-switch behavior, evidence-drawer load, Focus Mode overlay load, map camera behavior, or renderer memory pressure;
- metadata notes describing generation method, rights posture, source note, generation receipt pointer, expected size, expected consumer, and expected runtime envelope;
- expected-output pointers to `../golden/` when stable comparisons are practical.

## Exclusions

Do not use this lane for RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data; real source exports; live upstream payloads; real sensitive geography; exact restricted locations; credentials; lifecycle data; EvidenceBundles; SourceDescriptors; actual receipts; proof packs; release manifests; generated CI artifacts; implementation code; public API material; public map material; public tiles; source authority; evidence authority; policy authority; proof authority; release authority; AI authority; or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, public-safe, reproducible, and reviewable.
- Prefer `fixtures/slim/` unless the test genuinely requires a heavy runtime corpus.
- Document the fixture purpose, expected consumer, generation method, size expectations, rights posture, and rollback/correction path.
- Do not add large binary files without an explicit repo decision, storage decision, or Git LFS/external-storage note.
- Prefer deterministic generation scripts or documented recipes over opaque large checked-in payloads.
- Use toy IDs, toy refs, toy geometries, toy timestamps, toy hashes, and toy metadata.
- Keep performance-governance expectations separate from truth, evidence, policy, release, and publication claims.
- Pair stable heavy inputs with compact expected outputs or summaries when practical.
- Do not treat fixture success as implementation proof, benchmark truth, public-map authority, tile authority, release state, source authority, evidence closure, policy approval, or published output.

## Expected heavy fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Renderer stress corpus | Runtime smoke or benchmark input | Synthetic and public-safe only. |
| PMTiles or MLT benchmark-style fixture | Performance-governance input | Not a published tile product. |
| MapLibre/Cesium runtime load case | Renderer-safe or performance result | Expected metrics should be documented separately. |
| Large generalized geospatial corpus | Public-safe stress input | No sensitive exact geometry or lifecycle data. |
| Heavy fixture with stable expected output | Expected-output pointer | Keep expected output compact and route to `../golden/` where practical. |
| Corpus too large for Git | External storage or Git LFS decision needed | Do not check in without explicit repo decision. |

## Maintenance notes

- Update this README when payload files, generation recipes, benchmark consumers, renderer checks, helper scripts, expected-output names, storage decisions, or consumer contracts are added.
- Link each heavy fixture to the renderer check, performance-governance check, benchmark harness, governed-API dry-run, Evidence Drawer check, Focus Mode check, or documentation example that consumes it.
- Keep large corpus handling visible: storage decision, size, generation method, rights note, and rollback/correction path should be documented before payloads are added.
- Move domain-owned heavy examples into the owning domain fixture lane when ownership is clear.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, or sensitive exact geometry, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this heavy lane during this update.
- Exact child-lane inventory under `fixtures/heavy/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Sibling heavy/slim precedent: NOT FOUND by repository search during this update.
- Consumer alignment: NEEDS VERIFICATION against renderer checks, performance-governance checks, benchmark harnesses, MapLibre checks, Cesium checks, governed-API dry-runs, Evidence Drawer checks, Focus Mode checks, expected-output checks, storage decisions, and CI implementation.
- Tests and validators: NOT RUN.
