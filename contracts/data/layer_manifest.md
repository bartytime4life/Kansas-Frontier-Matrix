<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/layer-manifest
title: LayerManifest Contract
type: contract
version: v0.3
status: draft; proposed-inactive; dual-profile; fixture-only-strict-profile
owners: OWNER_TBD — Contract steward · Data steward · Layer steward · UI steward · Evidence steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-08-08
policy_label: public; contracts; data; layer-manifest; semantic-contract; release-aware; map-aware; evidence-aware; fixture-only
related:
  - ./README.md
  - ./layer_catalog_item.md
  - ./layer_descriptor.md
  - ./dataset_version.md
  - ./catalog_matrix.md
  - ../common/spec_hash.md
  - ../common/temporal_window.md
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../fixtures/data/layer_manifest/
  - ../../tools/validators/data/validate_layer_manifest.py
  - ../../tests/validators/test_validate_layer_manifest.py
  - ../../tools/validators/validator_registry.json
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
tags: [kfm, contracts, data, layer-manifest, maplibre, evidence, policy, release, rollback, deterministic, no-network]
notes:
  - "The existing permissive id-only profile remains valid for backward compatibility."
  - "A closed PROPOSED_INACTIVE / FIXTURE_ONLY profile now provides deterministic candidate validation."
  - "This change does not resolve the broader data-vs-layers schema-home question and does not modify the map, layers, runtime, or release compatibility schemas."
  - "A passing fixture proves shape and local deterministic invariants only; references remain unresolved and no policy, review, release, publication, signing, or public-use authority is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# LayerManifest Contract

> `LayerManifest` is the governed, version-specific manifest for one map layer representation. It binds a layer candidate to catalog, source, evidence, policy, review, release, artifact, temporal, rights, sensitivity, runtime, correction, and rollback references without collapsing those authorities.

## Status and boundary

| Field | Value |
|---|---|
| Semantic contract | `contracts/data/layer_manifest.md` |
| Paired machine schema | `schemas/contracts/v1/data/layer_manifest.schema.json` |
| Validator | `tools/validators/data/validate_layer_manifest.py` |
| Fixtures | `fixtures/data/layer_manifest/` |
| Strict profile | `PROPOSED_INACTIVE` / `FIXTURE_ONLY` |
| Legacy profile | Existing permissive `id`-required shape retained |
| Live catalog or registry integration | None |
| Runtime loader | None |
| Reference resolution | None |
| Policy or review execution | None |
| Signing or attestation verification | None |
| Release, publication, or public-use effect | None |

A validator `PASS` establishes only that the local JSON carrier conforms to the selected profile and reproduces the declared deterministic identity and semantic checks. It does **not** prove that referenced objects exist, that artifact bytes are valid, that a layer is safe, reviewed, signed, released, published, or available to a public client.

## Source-derived design

Pass 7 card `KFM-P7-PROG-0006` describes the layer manifest as the catalog-to-UI runtime contract. Related Pass 7 cards require first-class trust states, Evidence Drawer support, a UI-to-STAC bridge, and per-layer performance budgets. This implementation admits only the deterministic carrier and validation portion. It does not implement the client loader, signature verification, catalog resolver, Evidence Drawer, MapLibre adapter, or public activation.

## Directory Rules basis

ADR-0029 adopts Directory Governance Standard v2. The selected paths follow existing responsibility roots:

| Responsibility | Path family |
|---|---|
| Human-readable object meaning | `contracts/data/` |
| Machine-checkable shape | `schemas/contracts/v1/data/` |
| Synthetic positive and negative examples | `fixtures/data/` |
| Executable validation | `tools/validators/data/` |
| Behavior proof | `tests/validators/` |
| Read-only hosted orchestration | `.github/workflows/` |
| AI-authoring accountability | `data/receipts/generated/` |

The paired `data` schema already exists and names this contract, fixture root, and validator. This slice hardens that existing pair without moving files or declaring the unresolved `data/` versus `layers/` placement question settled. The placeholder schemas under `map/`, `layers/`, `runtime/`, and the release relationship contract remain unchanged.

## Object meaning

The strict fixture profile keeps these authority roles visible:

1. **Identity** — content-derived manifest identity, stable layer identity, and explicit layer version.
2. **Catalog and release relations** — catalog, release-manifest, promotion-decision, policy-decision, review, rollback, and correction references remain distinct.
3. **Evidence and source support** — sorted unique `SourceDescriptor` and `EvidenceBundle` references.
4. **Representation** — renderer, delivery protocol, immutable artifact reference, source-layer name, zoom envelope, bounds, and attribution.
5. **Time** — valid-time interval, source-update time, and evaluation time are explicit.
6. **Exposure** — audience, rights, sensitivity, field allowlist, geometry-generalization declaration, and transform-receipt references.
7. **Runtime contract** — trust state, stale behavior, Evidence Drawer/Focus Mode enablement, and bounded performance budgets.
8. **Lineage** — previous manifest, correction records, and rollback reference.
9. **Provenance** — run-receipt reference and validator implementation identity.
10. **Non-effects** — every authority-bearing governance flag is fixed to `false`.

## Strict profile fields

| Field | Meaning |
|---|---|
| `object_type` | Constant `LayerManifest`. |
| `schema_version` | Strict profile version `1.0.0`. |
| `profile_status` | Constant `PROPOSED_INACTIVE`. |
| `execution_mode` | Constant `FIXTURE_ONLY`. |
| `id` | `layer-manifest:` plus the first 24 hexadecimal characters of the semantic digest. |
| `spec_hash` | RFC 8785 JCS plus SHA-256 over all strict-profile fields except `id` and `spec_hash`. |
| `layer_id`, `layer_version`, `title` | Stable layer family, explicit version, and human label. |
| `lifecycle_state` | Constant `CANDIDATE`; this profile cannot represent publication. |
| `trust_state` | `CANDIDATE`, `DEGRADED`, `STALE`, or `HELD`. |
| `catalog_ref` | Candidate catalog record or STAC/DCAT projection reference. |
| `release_manifest_ref` | Unresolved candidate release-manifest reference; not release approval. |
| `promotion_decision_ref` | Unresolved promotion-decision reference. |
| `style_manifest_ref` | Optional style-manifest reference. |
| `source_descriptor_refs` | Canonical source-role references. |
| `evidence_bundle_refs` | Canonical evidence-support references. |
| `policy_decision_refs` | Canonical policy-decision references. |
| `review_record_refs` | Canonical review-record references; no authentication claim. |
| `representation` | MapLibre renderer, protocol, artifact ref, source layer, zooms, bounds, attribution. |
| `temporal` | Valid interval plus source-update and evaluation times. |
| `exposure` | Audience, rights, sensitivity, public fields, geometry transform, transform receipts. |
| `runtime` | Drawer/Focus flags, stale behavior, and performance budget. |
| `lineage` | Previous manifest, correction refs, rollback ref. |
| `provenance` | Run receipt and validator implementation. |
| `governance` | Explicit false-valued non-effects. |

## Canonical and semantic rules

A strict candidate is conformant only when:

- all reference and allowlist arrays are sorted and unique;
- catalog, release, promotion, run-receipt, rollback, and artifact references do not collapse into one identity;
- no authority-bearing reference uses a floating `latest` locator;
- `PMTILES` and `XYZ` representations name a non-empty `source_layer`;
- `COG` and `GEOJSON_FIXTURE` representations use `source_layer: null`;
- `min_zoom <= max_zoom`;
- bounds are ordered and within longitude/latitude limits;
- valid time does not end before it begins;
- a `PUBLIC` audience has `rights_status: APPROVED`;
- a `PUBLIC` audience uses `PUBLIC_SAFE` or `TRANSFORM_REQUIRED` sensitivity;
- `TRANSFORM_REQUIRED` carries a transform receipt and declares generalized geometry;
- the stored digest and content-derived ID reproduce exactly;
- governance flags remain false.

These checks do not resolve the carried references or inspect remote/source/artifact bytes.

## Legacy compatibility profile

Objects without `object_type` continue to use the previous compatibility shape:

- root JSON object;
- `id` required;
- optional string `version` and `spec_hash`;
- additional properties allowed.

The validator intentionally skips strict semantic checks for the legacy profile. This preserves existing consumers while making the stricter profile opt-in and visibly inactive.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape and applicable local deterministic checks succeeded. |
| `FAIL` | The input was readable, but schema or semantic invariants failed. |
| `ERROR` | The file, parser, schema, or hashing dependency could not be evaluated safely. |

Reports use stable finding codes and JSON pointers and do not echo untrusted values.

## Trust-state and runtime posture

`trust_state` is metadata, not a release decision. A client implementation may eventually map it to visible badges, but this fixture profile does not authorize that client behavior.

`runtime.performance_budget` records candidate limits for tile size, feature count, property count, and render time. The validator checks only bounded numeric shape; real device measurements and release gating require a separate runtime-probe component and release decision.

`evidence_drawer_enabled` and `focus_mode_enabled` are candidate declarations. A future governed loader must still resolve released evidence and finite policy/runtime outcomes before exposing those surfaces.

## Lifecycle relationship

```text
DatasetVersion / processed candidate
  -> artifact build
  -> LayerManifest candidate
  -> schema + deterministic validation
  -> evidence/source resolution
  -> policy + rights + sensitivity
  -> review
  -> PromotionDecision / ReleaseManifest
  -> governed catalog, API, MapLibre, Evidence Drawer, Focus Mode
  -> correction / withdrawal / rollback
```

This slice implements only the boxed candidate-validation step.

## Validation

```bash
python -m unittest tests.validators.test_validate_layer_manifest --verbose
python tools/validators/data/validate_layer_manifest.py --fixtures
python tools/validate_all.py --validate-registry
python tools/validate_all.py --profile release-dry-run --validator layer-manifest
```

The dedicated workflow also validates the generated authoring receipt against repository bytes.

## Security and privacy posture

- Fixtures are synthetic and contain no precise sensitive location.
- The validator performs no network access.
- Diagnostics contain finding codes and JSON pointers only.
- Client-side style filtering is not treated as redaction.
- Unknown rights or sensitivity fail the strict public-candidate checks.
- The profile cannot set release, publication, public-use, signature-verification, policy-evaluation, review-authentication, artifact-verification, or reference-resolution authority to true.

## Compatibility and unresolved seams

- The existing permissive schema behavior is retained.
- The strict profile is additive and inactive.
- Other LayerManifest schema stubs are not changed or declared canonical.
- No data migration, runtime route, MapLibre source registration, layer registry, policy bundle, proof pack, release record, or public artifact is introduced.
- The data-versus-layers schema-home seam remains `NEEDS VERIFICATION` pending an accepted decision or migration note.
- Future signing work must bind the manifest bytes or semantic digest through a separately governed attestation object.

## Rollback

Before merge, close the draft pull request and delete the feature branch.

After an authorized merge, revert the implementation commit or merge commit. The legacy schema branch remains intact, and the strict profile is fixture-only and inactive, so rollback requires no source deactivation, artifact withdrawal, cache invalidation, data migration, public correction, or runtime rollback.

## Open verification

- Which schema home will be canonical after ADR-0001 is resolved?
- Which accepted LayerManifest vocabulary should be shared with `LayerDescriptor`, `LayerCatalogItem`, and `MapReleaseManifest`?
- Which component resolves and authenticates catalog, evidence, policy, review, release, and rollback references?
- Which signature/attestation profile binds a future active manifest?
- Which public field allowlist and geometry-transform rules vary by domain?
- Which runtime probe establishes real performance-budget compliance?
- Which loader prevents unreleased or inactive manifests from reaching MapLibre?

<p align="right"><a href="#top">Back to top</a></p>
