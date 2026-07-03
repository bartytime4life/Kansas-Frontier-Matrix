# Infrastructure-generalized runtime fixtures

`fixtures/infrastructure-generalized/`

Status: draft / top-level runtime fixture lane / public-safe generalized infrastructure examples.

This directory is for small synthetic, public-safe, generalized infrastructure runtime fixtures used by renderer smoke tests, performance-governance checks, map runtime examples, public-safe generalized geospatial examples, documentation examples, and cross-lane runtime checks when the fixture is not yet routed to the domain-owned generalized-infrastructure fixture root.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, infrastructure truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, emergency authority, operational authority, or published artifacts.

## Fixture root posture

Use this top-level lane as a runtime/staging surface for public-safe generalized infrastructure examples. The domain-owned fixture root is `fixtures/domains/infrastructure-generalized/`, which already carries detailed generalized-infrastructure fixture boundaries for infrastructure rendering, sensitivity handling, cross-lane references, release-readiness checks, EvidenceBundle references, RunReceipt references, decision envelopes, layer manifests, map/UI behavior, correction posture, rollback posture, and expected outputs.

This top-level lane does not override the domain-owned lane and does not create a new infrastructure authority root. If a fixture has a clear infrastructure object-family, source-role, evidence, receipt, decision-envelope, layer-manifest, sensitivity, valid/invalid, or golden expected-output purpose, prefer `fixtures/domains/infrastructure-generalized/`.

A fixture may describe intended runtime behavior before the corresponding validator, route, policy bundle, UI surface, release gate, renderer check, or CI check exists. When implementation is not verified, the README must say so.

## Placement basis

This lane belongs under `fixtures/` because the root fixture README identifies `fixtures/` as runtime/benchmark fixture corpora for renderer smoke tests and performance governance, and includes `infrastructure-generalized/` in its suggested layout. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, emergency-alert root, operational root, or publication root.

The root fixture README separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to domain infrastructure fixtures

| Lane | Relationship |
|---|---|
| `../domains/infrastructure-generalized/` | Preferred domain-owned generalized-infrastructure fixture root for object-family, sensitivity, source-role, evidence, receipt, decision-envelope, layer-manifest, map/UI, correction, rollback, and expected-output examples. |
| `../domains/settlements-infrastructure/` | Expected domain fixture home for Settlements/Infrastructure examples if present. Use domain-owned lanes when object-family ownership is clear. |
| `../domains/roads-rail-trade/` | Expected transport fixture home for road, rail, trade, corridor, and crossing examples if present. Do not duplicate transport truth here. |
| `../domains/hydrology/` | Hydrology-owned water, flood context, and drainage examples belong there. Infrastructure examples may reference Hydrology only as context. |
| `../domains/hazards/` | Hazard exposure, declarations, and warning context belong there. This lane does not issue alerts. |
| `../domains/people-dna-land/` | Parcel, owner, consent, living-person, and land-title constraints belong there. This lane does not publish private joins. |

## Relationship to sibling top-level fixture lanes

| Lane | Relationship |
|---|---|
| `../slim/` | Preferred home for small renderer/runtime fixtures when infrastructure ownership is not material. |
| `../heavy/` | Heavy runtime stress lane; use it only when an infrastructure fixture is intentionally stress-sized and public-safe. |
| `../golden/` | Top-level expected-output lane for cross-domain or runtime-wide expected outputs. Prefer a domain/object-family expected-output lane when ownership is clear. |
| `../ecology/` | Cross-domain ecology fixture root; infrastructure context may appear there only as generalized context. |
| `../hydrology/` | Top-level Hydrology runtime fixture lane; use it for water-context runtime examples not owned by infrastructure. |
| `../domains/` | Domain-specific fixture homes should be preferred when the object family has a clear owner. |
| `../../tests/fixtures/` | Test-only fixture home; use it for deterministic test fixtures that are not runtime/benchmark corpora. |
| `../../artifacts/` | Generated CI output home; do not treat generated artifacts as fixture authority. |
| `../../data/` | Governed lifecycle data root; real data belongs there, not here. |

## Infrastructure boundary reminders

Settlements/Infrastructure owns infrastructure-side object families such as infrastructure assets, network nodes, network segments, facilities, service areas, operators, condition observations, and dependency relations. These examples remain toy fixtures and do not become canonical claims, operational records, public infrastructure datasets, or release state.

Infrastructure is a sensitive boundary. Exact asset locations, condition or vulnerability detail, operational dependency detail, restricted-source fields, private person/parcel joins, and alert-like operational instructions do not belong in this runtime fixture lane. Public examples should be generalized, aggregated, redacted, synthetic, or review-gated.

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy generalized point, line, polygon, tile, layer, drawer, Focus Mode, export, renderer, map, or runtime-envelope examples;
- toy generalized infrastructure asset, facility, service-area, network-node, network-segment, operator, dependency, bridge, crossing, corridor, route-adjacent, or utility-context examples when generalized enough for public-safe fixture use;
- public-safe generalized geometries and toy attributes for renderer smoke tests, map UI checks, and performance-governance examples;
- top-level runtime examples before a more specific infrastructure domain fixture lane is chosen;
- expected-output pointers to `../domains/infrastructure-generalized/`, `../golden/`, or a future object-family golden lane when stable comparisons are practical.

## Exclusions

Do not use this lane for RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data; real source exports; live upstream payloads; real exact infrastructure geometry; restricted attributes; operational dependency detail; condition/vulnerability detail; emergency alerts; life-safety instructions; private parcel/person joins; lifecycle data; SourceDescriptors; actual EvidenceBundles; actual RunReceipts; proof packs; release manifests; generated CI artifacts; implementation code; public API material; public map material; public tiles; source authority; evidence authority; policy authority; proof authority; release authority; AI authority; emergency authority; operational authority; or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, generalized, and public-safe.
- Prefer `fixtures/domains/infrastructure-generalized/` when the fixture has a clear infrastructure object-family, source-role, evidence, receipt, decision-envelope, layer-manifest, sensitivity, valid/invalid, or expected-output purpose.
- Use toy IDs, toy refs, toy timestamps, toy digests, toy source refs, toy evidence refs, toy policy refs, toy release refs, toy reviewer refs, toy geometries, and toy transform refs.
- Prefer generalized, coarse, aggregated, redacted, or toy geometry; never include sensitive exact geometry.
- Make fixture posture explicit: runtime, generalized, redacted, aggregated, public-safe, reviewer-only, restricted, denied, valid, invalid, negative, expected output, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, release-blocked, correction-visible, rollback-visible, or blocked render.
- Keep source admission, source role, evidence support, receipt provenance, citation validation, rights posture, sensitivity posture, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as source admission, SourceDescriptor authority, EvidenceBundle closure, RunReceipt storage proof, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, emergency authority, operational authority, or published output.

## Expected top-level infrastructure fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Domain-owned generalized infrastructure object fixture | `../domains/infrastructure-generalized/` | Synthetic domain fixture, not truth. |
| Runtime map smoke example with generalized infrastructure context | `./` until ownership is clear | Renderer-safe or bounded output. |
| Generalized infrastructure asset marker | `../domains/infrastructure-generalized/` | Public-safe or validation pass. |
| Generalized facility service area | `../domains/infrastructure-generalized/` | Public-safe or review-ready. |
| Transport crossing or route-adjacent context | Domain lane or `../domains/infrastructure-generalized/` depending on owner | Public-safe after source-role and sensitivity review. |
| Dependency sketch | `../domains/infrastructure-generalized/` | Reviewer-only, restricted, denied, or synthetic-only. |
| Sensitive exact geometry appears | Invalid/fail-closed lane or quarantine path | `DENY`, validation failure, or blocked render. |
| Stable expected output | `../golden/` or object-family golden lane | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when payload files, child lanes, validators, tests, helper scripts, renderer checks, expected-output names, storage decisions, or consumer contracts are added.
- Link each stable fixture to the renderer check, governed-API dry-run, Evidence Drawer check, Focus Mode check, source-role check, evidence-resolution check, citation-validation check, release-readiness check, correction check, rollback check, sensitivity check, or documentation example that consumes it.
- Move stable domain-owned examples into the owning `fixtures/domains/infrastructure-generalized/` child lane once ownership is clear.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this top-level index together.
- Keep payloads small enough for normal code review unless an explicit large-corpus storage decision exists.
- If a fixture accidentally includes real infrastructure material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, restricted operational detail, condition/vulnerability detail, private joins, or emergency-authority content, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this top-level infrastructure-generalized lane during this update.
- Exact child-lane inventory under `fixtures/infrastructure-generalized/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Domain infrastructure-generalized fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/infrastructure-generalized/README.md`.
- Settlements/Infrastructure alignment: PARTIALLY VERIFIED against `docs/domains/settlements-infrastructure/sublanes/infrastructure.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, generalized-infrastructure checks, sensitivity checks, source-descriptor checks, source-role checks, evidence-bundle checks, run-receipt checks, decision-envelope checks, layer-manifest checks, drawer checks, Focus Mode checks, map/UI checks, release-readiness checks, schema checks, policy checks, renderer checks, correction checks, rollback checks, and CI implementation.
- Tests and validators: NOT RUN.
