# Slim runtime fixtures

`fixtures/slim/`

Status: draft / runtime fixture lane / small synthetic smoke examples.

This directory is for small, public-safe, synthetic runtime fixture corpora used to exercise renderer smoke tests, governed API dry-runs, map runtime examples, Evidence Drawer examples, Focus Mode examples, documentation examples, and lightweight performance-governance checks when a heavy fixture is not needed.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, canonical truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Slim fixture posture

Use this lane as the default home for small runtime fixtures when the fixture is not clearly owned by a domain-specific fixture lane. Slim fixtures should be compact enough for normal code review, deterministic enough for repeatable checks, and public-safe enough for documentation or smoke-test use.

The root fixture README identifies `fixtures/` as runtime/benchmark fixture corpora for renderer smoke tests and performance governance. It lists PMTiles benchmark datasets, MLT benchmark datasets, MapLibre runtime fixtures, Cesium runtime fixtures, public-safe generalized geospatial corpora, and slim/heavy renderer stress scenarios as accepted purposes.

The sibling heavy lane says `fixtures/slim/` is preferred unless the test genuinely requires a heavy runtime corpus. Start here first; move to `../heavy/` only when a small fixture cannot exercise the intended behavior.

## Placement basis

This lane belongs under `fixtures/` because it contains runtime benchmark inputs, smoke-test examples, and public-safe synthetic runtime fixtures. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile publication root, artifact root, or public publication root.

The root fixture README separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to sibling fixture lanes

| Lane | Relationship |
|---|---|
| `../heavy/` | Heavy runtime stress lane; use only when a small fixture cannot meet the test purpose. |
| `../golden/` | Expected-output lane for stable synthetic fixture outputs. Slim fixtures may pair with compact golden outputs. |
| `../invalid/` | Top-level fail-closed lane for broad invalid examples. |
| `../public_safe/` | Parent lane for public-safe documentation/runtime examples. |
| `../ecology/` | Cross-domain ecology fixture root; use it for ecology-specific synthetic examples. |
| `../hydrology/` | Top-level Hydrology runtime fixture lane; use it for Hydrology-specific runtime examples. |
| `../infrastructure-generalized/` | Top-level generalized-infrastructure runtime fixture lane; use it for infrastructure-specific public-safe examples. |
| `../release/` | Synthetic release-governance fixture lane; use it for release object examples. |
| `../generated_receipt/` | Generated-receipt fixture root; use it for receipt-shape and receipt-validation examples. |
| `../domains/` | Preferred root for domain-owned fixtures. |
| `../../tests/fixtures/` | Test-only fixture home; use it for deterministic test fixtures that are not runtime/benchmark corpora. |
| `../../artifacts/` | Generated CI output home; do not treat generated artifacts as fixture authority. |
| `../../data/` | Governed lifecycle data root; real data belongs there, not here. |

## Accepted material

This lane may contain:

- small synthetic PMTiles, MLT, MapLibre, Cesium, vector-tile, GeoJSON, JSON, JSONL, SVG, YAML, or Markdown examples;
- toy map layers, layer manifests, feature collections, camera states, style switches, attribution examples, drawer payloads, Focus Mode payloads, governed API envelopes, and bounded runtime-output examples;
- public-safe generalized geospatial examples built for smoke tests, documentation, dry-runs, and lightweight performance checks;
- metadata notes describing generation method, rights posture, source note, generation receipt pointer, expected consumer, and expected runtime envelope;
- expected-output pointers to `../golden/` when stable comparisons are practical.

## Exclusions

Do not use this lane for RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data; real source exports; live upstream payloads; real sensitive geography; exact restricted locations; credentials; lifecycle data; EvidenceBundles; SourceDescriptors; actual receipts; proof packs; release manifests; generated CI artifacts; implementation code; public API material; public map material; public tiles; source authority; evidence authority; policy authority; proof authority; release authority; AI authority; or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, public-safe, and easy to review.
- Prefer this lane over `../heavy/` unless the test genuinely requires a larger corpus.
- Prefer a domain-specific fixture lane when the object family or policy context has a clear owner.
- Document the fixture purpose, expected consumer, generation method, rights posture, and rollback/correction path.
- Use toy IDs, toy refs, toy geometries, toy timestamps, toy hashes, and toy metadata.
- Keep performance-governance expectations separate from truth, evidence, policy, release, and publication claims.
- Pair stable slim inputs with compact expected outputs when practical.
- Do not treat fixture success as implementation proof, benchmark truth, public-map authority, tile authority, release state, source authority, evidence closure, policy approval, or published output.

## Expected slim fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Renderer smoke input | Runtime smoke input | Synthetic and public-safe only. |
| Small MapLibre/Cesium runtime example | Renderer-safe or bounded output | Not a public map product. |
| Small generalized GeoJSON fixture | Public-safe runtime input | No sensitive exact geometry or lifecycle data. |
| Evidence Drawer or Focus Mode smoke fixture | Drawer-safe, Focus-safe, `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` | Generated text remains interpretive and evidence-bound. |
| Governed API dry-run envelope | Validation pass or fail-closed output | Not public API authority. |
| Stable expected output | Expected-output pointer | Route to `../golden/` where practical. |
| Fixture grows too large | Move concern to `../heavy/` or external storage decision | Do not turn slim into a large corpus lane. |

## Maintenance notes

- Update this README when payload files, generation recipes, renderer checks, helper scripts, expected-output names, storage decisions, or consumer contracts are added.
- Link each slim fixture to the renderer check, performance-governance check, benchmark harness, governed-API dry-run, Evidence Drawer check, Focus Mode check, or documentation example that consumes it.
- Keep each corpus small enough for ordinary review. If it becomes large, move the concern to `../heavy/` or require an explicit storage decision.
- Move stable domain-owned examples into the owning domain fixture lane when ownership is clear.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, or sensitive exact geometry, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this slim lane during this update.
- Exact child-lane inventory under `fixtures/slim/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Heavy sibling alignment: PARTIALLY VERIFIED against `fixtures/heavy/README.md`.
- Consumer alignment: NEEDS VERIFICATION against renderer checks, performance-governance checks, benchmark harnesses, MapLibre checks, Cesium checks, governed-API dry-runs, Evidence Drawer checks, Focus Mode checks, expected-output checks, storage decisions, and CI implementation.
- Tests and validators: NOT RUN.
