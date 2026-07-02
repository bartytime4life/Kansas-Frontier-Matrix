# Hazards layer-manifest fixtures

`fixtures/domains/hazards/layer_manifest/`

Status: draft / fixture lane / Hazards-scoped `LayerManifest` examples.

This directory is for small synthetic Hazards layer-manifest fixture examples. These fixtures describe toy layer identities, artifact refs, source refs, source-role posture, style refs, time extents, evidence refs, policy state, stale state, public-safe flags, disclaimer fields, correction state, rollback state, and finite layer-manifest resolver outcomes.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Layer-manifest posture

The Hazards API contract identifies a Hazards layer manifest resolver that returns a Hazards-scoped `LayerManifest`. It is the governed surface for released Hazards layer metadata and returns only `ANSWER`, `DENY`, or `ERROR`. A layer either has a release-authorized manifest or it is denied; it is not a public layer by fixture presence.

The Hazards domain layer descriptor contract describes the Hazards profile around released or release-candidate map/UI layers: artifact binding, source-role posture, evidence lookup, policy/release state, disclaimer obligations, stale/expiry behavior, correction state, and rollback target. It also states that layer descriptors are downstream delivery-support objects, not source truth, proof, release authority, or safety guidance.

The cross-cutting `LayerManifest` contract records layer identity, data/product lineage, evidence posture, integrity refs, valid time, freshness state, source roles, rights, sensitivity, policy posture, review state, release relationship, and correction/rollback lineage. It remains a semantic contract; schema completeness, fixtures, validators, release integration, public route behavior, and tests remain `NEEDS VERIFICATION`.

This fixture lane can support future layer-manifest checks, but fixture examples do not prove schema enforcement, layer-registry behavior, release integration, route behavior, UI behavior, policy enforcement, or public tile serving by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says RAW, WORK, and QUARANTINE data do not belong in `fixtures/`, sensitive exact geometry does not belong here, and fixture corpora must not be treated as canonical truth. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../feature_resolver/` | Feature resolver fixtures may reference layer IDs and manifest states. |
| `../drawer/` | Drawer fixtures may depend on layer manifest evidence and display obligations. |
| `../focus/` | Focus fixtures may receive layer manifest context through governed envelopes. |
| `../identity/` | Identity fixtures may supply stable layer/feature refs used by manifests. |
| `../golden/` | Stable expected manifest outputs may be paired there. |
| `../invalid/` | Negative layer-manifest cases should be indexed there when they represent blocked public states. |
| `../../../../contracts/data/layer_manifest.md` | Cross-cutting `LayerManifest` semantics; this lane supplies examples only. |
| `../../../../contracts/domains/hazards/domain_layer_descriptor.md` | Hazards layer descriptor semantics; this lane supplies examples only. |
| `../../../../docs/domains/hazards/API_CONTRACTS.md` | Hazards layer-manifest resolver doctrine; this lane supplies examples only. |
| `../../../../data/registry/layers/` | Layer registry home; fixtures do not create registry authority. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../feature_resolver/README.md`
- `../drawer/README.md`
- `../focus/README.md`
- `../identity/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../../README.md`
- `../../../../contracts/data/layer_manifest.md`
- `../../../../contracts/data/layer_descriptor.md`
- `../../../../contracts/data/layer_catalog_item.md`
- `../../../../contracts/domains/hazards/domain_layer_descriptor.md`
- `../../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../data/registry/layers/`
- `../../../../data/registry/sources/hazards/`
- `../../../../data/proofs/hazards/`
- `../../../../schemas/contracts/v1/data/layer_manifest.schema.json`
- `../../../../schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Hazards `LayerManifest` payloads with layer IDs, version IDs, artifact refs, source refs, style refs, time extents, evidence refs, policy refs, release refs, stale-state refs, correction refs, rollback refs, and public-safe flags;
- toy layer-manifest resolver outputs using `ANSWER`, `DENY`, or `ERROR`;
- toy layer-manifest examples for hazard event timelines, flood context, drought maps, wildfire/smoke context, earthquake context, heat/cold context, exposure analysis, resilience summary, and official-link/context-only modes;
- toy positive contrast cases and negative examples paired with `../invalid/` when useful;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, tile bytes, renderer implementations, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy layer IDs, toy version refs, toy artifact refs, toy source refs, toy evidence refs, toy release refs, toy policy refs, toy style refs, toy timestamps, toy digests, and toy hashes.
- Make layer-manifest posture explicit: released, release-candidate, denied, stale, superseded, withdrawn, rollback-ready, correction-visible, public-safe, restricted, missing release, missing evidence, or invalid.
- Make expected outcome explicit: `ANSWER`, `DENY`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, release posture, stale/freshness state, disclaimer state, correction posture, rollback posture, registry linkage, drawer readiness, Focus readiness, and resolver context separate.
- Do not treat fixture success as EvidenceBundle closure, source authority, policy approval, release state, layer-registry authority, API implementation proof, UI implementation proof, tile authority, or published output.

## Expected layer-manifest fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Released synthetic historical hazard layer with resolvable evidence, policy, release, and rollback refs | `ANSWER` | Bounded layer manifest only; not source truth. |
| Synthetic layer missing `ReleaseManifest` ref | `DENY` or validation failure | Public layer serving requires release state. |
| Synthetic layer manifest missing Hazards disclaimer/public-boundary field | `DENY` or validation failure | Display obligations must travel with the manifest. |
| Synthetic layer with unresolved EvidenceRef | `DENY` or `ERROR` | Evidence state must be inspectable. |
| Synthetic expired warning context styled as current layer | `DENY` or validation failure | Freshness state controls public display posture. |
| Synthetic candidate or internal lifecycle layer presented as public | `DENY` or validation failure | Public clients consume released governed surfaces only. |
| Malformed layer ID, artifact digest, or schema version | `ERROR` | Error remains finite and inspectable. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, layer-manifest contracts, or consumer contracts are added.
- Link each fixture to the layer-manifest check, Hazards layer descriptor check, evidence-resolution check, citation-validation check, source-role check, stale/freshness check, disclaimer check, policy-filter check, release-readiness check, registry-link check, drawer check, Focus Mode check, correction check, rollback check, or governed-API dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Hazards layer descriptor alignment: PARTIALLY VERIFIED against `contracts/domains/hazards/domain_layer_descriptor.md`.
- Cross-cutting LayerManifest alignment: PARTIALLY VERIFIED against `contracts/data/layer_manifest.md`.
- Hazards API layer-manifest alignment: PARTIALLY VERIFIED against `docs/domains/hazards/API_CONTRACTS.md`.
- Layer registry alignment: PARTIALLY VERIFIED against `data/registry/layers/README.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Hazards invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/invalid/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, layer-manifest checks, layer-descriptor checks, governed-API tests, drawer checks, Focus Mode checks, registry checks, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.
