# Hydrology runtime fixtures

`fixtures/hydrology/`

Status: draft / top-level runtime fixture lane / Hydrology public-safe examples.

This directory is for small synthetic Hydrology runtime fixtures used by renderer smoke tests, performance-governance checks, map runtime examples, public-safe generalized geospatial examples, documentation examples, and cross-lane runtime checks when the fixture is not yet routed to the domain-owned Hydrology fixture root.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, Hydrology truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, emergency authority, or published artifacts.

## Fixture root posture

Use this top-level lane as a runtime/staging fixture surface for public-safe synthetic Hydrology examples. The domain-owned fixture root is `fixtures/domains/hydrology/`, which already carries the detailed Hydrology fixture families for decision envelopes, evidence bundles, run receipts, sources, valid examples, invalid examples, negative examples, and golden expected outputs.

This top-level lane does not override the domain-owned lane and does not create a new Hydrology authority root. If a fixture has a clear Hydrology object family, contract, schema, source-role, EvidenceBundle, RunReceipt, decision-envelope, valid/invalid, or golden expected-output purpose, prefer `fixtures/domains/hydrology/`.

A fixture may describe intended runtime behavior before the corresponding validator, route, policy bundle, UI surface, release gate, renderer check, or CI check exists. When implementation is not verified, the README must say so.

## Placement basis

This lane belongs under `fixtures/` because the root fixture README identifies `fixtures/` as runtime/benchmark fixture corpora for renderer smoke tests and performance governance. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, emergency-alert root, or publication root.

The root fixture README separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to Hydrology domain fixtures

| Lane | Relationship |
|---|---|
| `../domains/hydrology/` | Preferred domain-owned Hydrology fixture root for object-family, evidence, receipt, source, valid, invalid, negative, and golden examples. |
| `../domains/hydrology/decision_envelope/` | Preferred lane for Hydrology runtime `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` envelope examples. |
| `../domains/hydrology/evidence_bundle/` | Preferred lane for synthetic claim-scope evidence-support examples. |
| `../domains/hydrology/run_receipt/` | Preferred lane for synthetic governed-run provenance examples. |
| `../domains/hydrology/sources/` | Preferred lane for source-like refs, source role, cadence, source-head, rights, and sensitivity examples. |
| `../domains/hydrology/valid/` | Preferred lane for broad positive-path Hydrology examples. |
| `../domains/hydrology/invalid/` | Preferred lane for broad stable fail-closed Hydrology examples. |
| `../domains/hydrology/negative/` | Preferred lane for draft negative-path Hydrology scenarios. |
| `../domains/hydrology/golden/` | Preferred lane for stable expected Hydrology outputs. |

## Relationship to sibling top-level fixture lanes

| Lane | Relationship |
|---|---|
| `../slim/` | Preferred home for small renderer/runtime fixtures when Hydrology ownership is not material. |
| `../heavy/` | Heavy runtime stress lane; use it only when a Hydrology runtime fixture is intentionally stress-sized and public-safe. |
| `../golden/` | Top-level expected-output lane for cross-domain or runtime-wide expected outputs. Prefer Hydrology domain `golden/` for domain-owned expected outputs. |
| `../ecology/` | Cross-domain ecology fixture root; Hydrology may lend watershed, reach, flood-context, or wetland context without owning ecology truth. |
| `../domains/` | Domain-specific fixture homes should be preferred when the object family has a clear owner. |
| `../../tests/fixtures/` | Test-only fixture home; use it for deterministic test fixtures that are not runtime/benchmark corpora. |
| `../../artifacts/` | Generated CI output home; do not treat generated artifacts as fixture authority. |
| `../../data/` | Governed lifecycle data root; real data belongs there, not here. |

## Hydrology boundary reminders

Hydrology owns synthetic examples that imitate watersheds, HUC units, hydro features, reach identity, gauge sites, flow observations, water-level observations, water-quality observations, groundwater wells, NFHL/flood context, observed flood events, hydrographs, and upstream traces. These examples remain toy fixtures and do not become canonical claims.

Hydrology does not own emergency alerts, life-safety instructions, observed inundation derived from NFHL, soil/agriculture/geology/infrastructure canonical truth, ownership, parcels, title, CRS definitions, or base-layer definitions. Cross-lane examples must preserve ownership, source role, sensitivity, and EvidenceBundle support.

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy public-safe watershed, HUC, reach, gauge, flow, water-level, water-quality, groundwater, NFHL-context, flood-context, observed-flood, hydrograph, upstream-trace, renderer, map, drawer, Focus Mode, or runtime-envelope examples;
- public-safe generalized geometries and toy attributes for renderer smoke tests, map UI checks, and performance-governance examples;
- top-level runtime examples before a more specific Hydrology domain fixture lane is chosen;
- expected-output pointers to `../domains/hydrology/golden/` or `../golden/` when stable comparisons are practical.

## Exclusions

Do not use this lane for RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data; real source exports; live upstream payloads; real sensitive geography; exact infrastructure or private-well exposure; emergency alerts; life-safety instructions; lifecycle data; SourceDescriptors; actual EvidenceBundles; actual RunReceipts; proof packs; release manifests; generated CI artifacts; implementation code; public API material; public map material; public tiles; source authority; evidence authority; policy authority; proof authority; release authority; AI authority; emergency authority; or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer `fixtures/domains/hydrology/` when the fixture has a clear Hydrology object-family, evidence, receipt, source, decision-envelope, valid/invalid, or golden purpose.
- Use toy IDs, toy refs, toy timestamps, toy digests, toy source refs, toy evidence refs, toy policy refs, toy release refs, toy reviewer refs, and toy geometries.
- Make fixture posture explicit: runtime, valid, invalid, negative, golden, expected output, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, public-safe, release-blocked, correction-visible, rollback-visible, or blocked render.
- Keep source admission, source role, evidence support, receipt provenance, citation validation, rights posture, sensitivity posture, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as source admission, SourceDescriptor authority, EvidenceBundle closure, RunReceipt storage proof, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, emergency authority, or published output.

## Expected top-level Hydrology fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Domain-owned Hydrology object fixture | `../domains/hydrology/` or child lane | Synthetic domain fixture, not truth. |
| Runtime map smoke example with Hydrology context | `./` until ownership is clear | Renderer-safe or bounded output. |
| Hydrology decision envelope | `../domains/hydrology/decision_envelope/` | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass/failure, or blocked render. |
| Hydrology EvidenceBundle-like example | `../domains/hydrology/evidence_bundle/` | Evidence-resolved, citation-ready, `ABSTAIN`, `DENY`, or validation failure. |
| Hydrology RunReceipt-like example | `../domains/hydrology/run_receipt/` | Provenance-resolved, replay-reviewable, or validation failure. |
| Hydrology source-role example | `../domains/hydrology/sources/` | Source-role-preserved or fail-closed. |
| Cross-domain ecology or habitat-hydrology context | `../ecology/` or domain lane depending on owner | Context-only, evidence-resolved, or review-required. |
| Stable Hydrology expected output | `../domains/hydrology/golden/` | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when payload files, child lanes, validators, tests, helper scripts, renderer checks, expected-output names, storage decisions, or consumer contracts are added.
- Link each stable fixture to the renderer check, governed-API dry-run, Evidence Drawer check, Focus Mode check, source-role check, evidence-resolution check, citation-validation check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- Move stable domain-owned examples into the owning `fixtures/domains/hydrology/` child lane once ownership is clear.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this top-level index together.
- Keep payloads small enough for normal code review unless an explicit large-corpus storage decision exists.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, exact private-well detail, exact infrastructure-exposure detail, or emergency-authority content, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this top-level Hydrology lane during this update.
- Exact child-lane inventory under `fixtures/hydrology/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Domain Hydrology fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/README.md`.
- Hydrology boundary alignment: PARTIALLY VERIFIED against `docs/domains/hydrology/BOUNDARY.md`.
- Consumer alignment: NEEDS VERIFICATION against renderer checks, performance-governance checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, run-receipt checks, source-descriptor checks, source-role checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, source-head checks, trust-membrane checks, release-readiness checks, rollback-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.
