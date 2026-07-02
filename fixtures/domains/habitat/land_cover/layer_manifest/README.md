# Habitat land-cover layer-manifest fixtures

`fixtures/domains/habitat/land_cover/layer_manifest/`

Status: draft / fixture lane / land-cover layer-manifest examples.

This directory is for small synthetic Habitat land-cover layer-manifest fixture examples. These fixtures describe toy layer-version metadata, artifact pointers, source-role badges, evidence pointers, integrity checks, freshness state, release-facing checks, correction state, and rollback posture for land-cover viewing products.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, Habitat truth, or published artifacts.

## Contract posture

The generic `LayerManifest` contract defines a governed manifest for a versioned layer payload. It binds layer identity, product lineage, evidence posture, integrity references, time, freshness, source roles, rights, policy posture, review state, release relationship, correction, supersession, and rollback context.

The Habitat `DomainLayerDescriptor` contract is the closest Habitat-specific support surface verified for layer semantics. It describes how a Habitat object family may appear as a governed, released, public-safe map/API/UI layer without turning tiles, render styles, popups, graph projections, or generated text into source truth.

Both contracts keep release authority separate from descriptors and manifests. This fixture lane can support future checks, but fixture examples do not prove schema enforcement, public route behavior, release integration, or renderer implementation.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The Habitat land-cover sublane lists `fixtures/domains/habitat/land_cover/` as the proposed fixture home for land-cover examples. The root fixture README says fixture corpora are not canonical truth and RAW, WORK, and QUARANTINE data do not belong here.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../class_scheme/` | Layer-manifest fixtures may reference toy class-scheme fixtures for legends. |
| `../crosswalk/` | Layer-manifest fixtures may reference toy crosswalk fixtures when a displayed layer depends on recoding. |
| `../change_summary/` | Layer-manifest fixtures may reference toy change-summary fixtures for change products. |
| `../../golden/` | Stable expected outputs for layer-manifest inputs may be paired there. |
| `../../invalid/` | Negative-path layer-manifest inputs may be paired there when useful. |
| `../../../../../contracts/data/layer_manifest.md` | Generic layer-manifest semantics; this lane supplies examples only. |
| `../../../../../contracts/domains/habitat/domain_layer_descriptor.md` | Habitat layer-support semantics; this lane supplies examples only. |
| `../../../../../data/registry/layers/habitat/` | Layer-registry control records; fixtures do not create registry authority. |
| `../../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../class_scheme/README.md`
- `../crosswalk/README.md`
- `../change_summary/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../../contracts/data/layer_manifest.md`
- `../../../../../contracts/data/layer_descriptor.md`
- `../../../../../contracts/data/layer_catalog_item.md`
- `../../../../../contracts/domains/habitat/domain_layer_descriptor.md`
- `../../../../../data/registry/layers/habitat/README.md`
- `../../../../../schemas/contracts/v1/data/layer_manifest.schema.json`
- `../../../../../schemas/contracts/v1/domains/habitat/domain_layer_descriptor.schema.json`
- `../../../../../pipelines/domains/habitat/land_cover/`
- `../../../../../release/manifests/habitat/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy layer IDs, layer versions, artifact refs, artifact digests, tile/vector/raster pointer examples, and display-family metadata;
- toy source-role badges, evidence refs, policy refs, review refs, release refs, freshness states, correction refs, and rollback refs;
- toy layer-manifest inputs for governed API, Evidence Drawer, Focus Mode, renderer, catalog, registry, release-readiness, and documentation checks;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, run receipts, release manifests, implementation code, public API material, public map material, public tiles, source authority, registry authority, layer authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy IDs, toy layer keys, toy versions, toy artifact refs, toy digests, toy evidence references, and toy timestamps.
- Make layer posture explicit: candidate, fixture-only, released-like example, stale, superseded, withdrawn, corrected, rollback-ready, invalid, or expected output.
- Keep layer identity, data lineage, source role, evidence state, rights state, policy state, review state, release state, correction state, rollback state, freshness state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, artifact integrity, source-role display, evidence closure, release posture, correction posture, rollback posture, catalog safety, and renderer safety separate.
- Do not treat fixture success as evidence closure, source authority, schema authority, implementation proof, release state, public-map authority, tile authority, or published output.

## Expected layer-manifest fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic land-cover layer manifest with toy artifact refs and evidence refs | Valid input | Demonstrates layer-version metadata without becoming a release artifact. |
| Missing layer ID or version | Validation failure | Layer identity must be stable. |
| Missing artifact digest | Validation failure or review-required output | Integrity refs must be explicit. |
| Missing evidence support for a displayed claim | `ABSTAIN` or hold output | Cite-or-abstain remains visible. |
| Descriptor treated as release approval | Validation failure | Release authority remains separate. |
| Tile/style treated as truth | Validation failure | Rendering is downstream display. |
| Missing correction or rollback posture for a public-facing example | Review-required output | Public-use posture must be inspectable. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the contract review, schema check, artifact-integrity check, registry check, governed-API test, Evidence Drawer test, Focus Mode test, renderer check, release-readiness check, correction check, rollback check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Generic LayerManifest contract alignment: PARTIALLY VERIFIED against `contracts/data/layer_manifest.md`.
- Habitat layer-descriptor alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/domain_layer_descriptor.md`.
- Habitat layer-registry alignment: PARTIALLY VERIFIED against `data/registry/layers/habitat/README.md`.
- Land-cover sublane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Schema alignment: NEEDS VERIFICATION because the generic layer-manifest contract reports schema-home conflict and placeholder schema posture.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, registry checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
