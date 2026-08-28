# Hazards identity fixtures

`fixtures/domains/hazards/identity/`

Status: draft / fixture lane / domain feature identity examples.

This directory is for small synthetic Hazards identity fixture examples. These fixtures describe toy stable feature IDs, source IDs, object families, source roles, temporal scopes, geography versions, normalized digests, spec hashes, correction links, rollback links, and feature-reference cases for Hazards objects.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, Hazards truth, or published artifacts.

## Identity posture

The `domain_feature_identity` contract defines how a Hazards record becomes the same object or a different object across source systems, roles, time windows, geography versions, corrections, and releases. It says identity is not a source-native ID alone.

The contract gives the governing identity tuple as:

```text
source_id + object_role + temporal_scope + normalized_digest
```

It also reports that the paired schema exists, but remains a proposed scaffold with only `spec_hash`, `id`, and `version` visible and `additionalProperties: true`. Field-level schema shape, validator enforcement, fixtures, policy runtime, release artifacts, and public API behavior remain `NEEDS VERIFICATION`.

This fixture lane can support future identity checks, but fixture examples do not prove schema enforcement, ID canonicalization, source activation, validator behavior, policy approval, release integration, or public API behavior by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../README.md` | Parent Hazards fixture lane; still a greenfield stub during this update. |
| `../feature_resolver/` | Resolver fixtures may reference toy identity fixtures as feature refs. |
| `../drawer/` | Drawer fixtures may display toy identity and citation context. |
| `../focus/` | Focus fixtures may use toy identity refs in map context. |
| `../golden/` | Stable expected outputs for identity inputs may be paired there. |
| `../invalid/` | Future negative-path examples may be paired there if a Hazards invalid lane is created. |
| `../../../../contracts/domains/hazards/domain_feature_identity.md` | Identity semantics; this lane supplies examples only. |
| `../../../../schemas/contracts/v1/domains/hazards/domain_feature_identity.schema.json` | Expected machine-shape home; current enforcement remains bounded by contract status. |
| `../../../../data/registry/sources/hazards/` | Source descriptor home; fixtures do not activate sources. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../README.md`
- `../feature_resolver/README.md`
- `../drawer/README.md`
- `../focus/README.md`
- `../golden/README.md`
- `../../../README.md`
- `../../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/domains/hazards/domain_observation.md`
- `../../../../contracts/domains/hazards/domain_layer_descriptor.md`
- `../../../../contracts/domains/hazards/domain_validation_report.md`
- `../../../../docs/domains/hazards/IDENTITY_MODEL.md`
- `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../schemas/contracts/v1/domains/hazards/domain_feature_identity.schema.json`
- `../../../../policy/domains/hazards/`
- `../../../../data/registry/sources/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy `domain_feature_identity` examples for positive-path and negative-path checks;
- toy source IDs, object families, object roles, temporal scopes, geography versions, normalized digests, spec hashes, and feature refs;
- toy correction, supersession, rollback, duplicate-detection, source-role-change, time-window-change, and geography-version-change examples;
- toy resolver, drawer, Focus Mode, golden-output, and documentation examples that reference identity objects;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy source refs, toy object families, toy time windows, toy geography refs, toy digests, toy spec hashes, toy correction refs, toy rollback refs, and toy hashes.
- Make identity posture explicit: same object, different object, duplicate candidate, correction, supersession, role change, time-window change, geography-version change, invalid, or expected output.
- Keep source ID, object family, object role, temporal scope, geography version, normalized digest, spec hash, evidence refs, correction state, rollback state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, ID determinism, source-role validity, temporal identity, geography-version identity, duplicate detection, correction linkage, rollback linkage, resolver-readiness, and drawer-readiness separate.
- Do not treat fixture success as EvidenceBundle closure, source authority, schema authority, identity algorithm proof, implementation proof, release state, public-map authority, or published output.

## Expected identity fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic record with toy source ID, object role, temporal scope, and normalized digest | Valid input | Demonstrates identity tuple shape. |
| Same source-native ID but changed object role | Different identity or correction-required output | Role is identity-bearing. |
| Same source-native ID with changed event/observed time | Different identity or correction-required output | Time may participate in identity. |
| Retrieval time changes only | Same identity | Fetch timing should not rotate identity. |
| Release time changes only | Same identity | Release scheduling is not object identity. |
| Missing source ID or object role | Validation failure | Identity cannot be grounded. |
| Duplicate digest across two toy records | Duplicate-candidate output | Review decides merge/correction posture. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, identity contracts, or consumer contracts are added.
- Link each fixture to the identity contract review, schema check, ID canonicalization check, duplicate-detection check, source-role check, temporal-scope check, geography-version check, correction check, rollback check, feature-resolver check, drawer check, Focus Mode check, or governed-API dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Domain feature identity contract alignment: PARTIALLY VERIFIED against `contracts/domains/hazards/domain_feature_identity.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, identity checks, duplicate-detection checks, feature-resolver checks, drawer checks, Focus Mode checks, golden-file checks, governed-API tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
