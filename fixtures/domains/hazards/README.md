# Hazards fixtures

`fixtures/domains/hazards/`

Status: draft / fixture parent index / synthetic Hazards examples.

This directory is the parent lane for small synthetic Hazards fixture examples. Hazards fixtures are used to exercise bounded feature resolution, Evidence Drawer projection, Focus Mode, identity handling, layer manifests, valid/negative/invalid cases, golden expected outputs, source-role preservation, evidence resolution, citation validation, freshness state, policy state, release posture, correction posture, rollback posture, and public-safe UI handoff examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, AI authority, or published artifacts.

## Fixture posture

Use this parent lane to navigate Hazards fixture families and keep their boundaries consistent. The populated child READMEs define synthetic examples for resolver, drawer, Focus, identity, layer-manifest, valid, negative, invalid, and golden-output scenarios.

A fixture is not implementation proof. It does not prove validator behavior, governed API route behavior, UI behavior, policy enforcement, release integration, schema enforcement, source activation, EvidenceBundle closure, or CI coverage. It only provides reviewable synthetic material for future checks.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `valid/` | Positive-path synthetic Hazards inputs. | Bounded `ANSWER` or other finite valid envelope by design. |
| `negative/` | Draft negative-path scenarios not yet sorted into stable invalid child lanes. | Staging for fail-closed scenarios. |
| `invalid/` | Stable fail-closed negative cases with known defect families. | `ABSTAIN`, `DENY`, `ERROR`, review-required, validation failure, or blocked render. |
| `golden/` | Expected outputs for stable synthetic inputs. | Regression anchors once producer and consumer are documented. |
| `feature_resolver/` | Synthetic Hazards feature/detail resolver examples. | `HazardsDecisionEnvelope` with finite outcomes. |
| `drawer/` | Synthetic Evidence Drawer and trust-visible UI examples. | Governed drawer projection; not source truth or proof closure. |
| `focus/` | Synthetic Hazards Focus Mode examples. | `RuntimeResponseEnvelope` plus `AIReceipt` where AI is involved. |
| `identity/` | Synthetic stable-ID and feature-reference examples. | Source role and temporal scope remain identity-bearing. |
| `layer_manifest/` | Synthetic Hazards-scoped `LayerManifest` examples. | Released/public-safe layer metadata examples, not layer bytes or release authority. |

## Relationship between fixture lanes

| Lane | Use |
|---|---|
| `valid/` | Positive-path synthetic inputs expected to pass bounded checks. |
| `negative/` | Draft negative cases that are not yet sorted into stable invalid child lanes. |
| `invalid/` | Stable fail-closed negative cases with known defect families. |
| `golden/` | Expected outputs for stable valid, negative, and invalid inputs. |
| `feature_resolver/` | Bounded feature/detail resolver request and envelope examples. |
| `drawer/` | Evidence Drawer payload and trust-visible projection examples. |
| `focus/` | Focus Mode request, response, receipt, citation, and limitation examples. |
| `identity/` | Stable identity, duplicate, correction, supersession, and temporal-scope examples. |
| `layer_manifest/` | Layer identity, artifact, release, policy, evidence, stale-state, and rollback examples. |

## Related references

- `valid/README.md`
- `negative/README.md`
- `invalid/README.md`
- `golden/README.md`
- `feature_resolver/README.md`
- `drawer/README.md`
- `focus/README.md`
- `identity/README.md`
- `layer_manifest/README.md`
- `../../README.md`
- `../../../docs/architecture/governed-api.md`
- `../../../docs/architecture/hazards-trust-membrane.md`
- `../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../contracts/domains/hazards/domain_layer_descriptor.md`
- `../../../contracts/data/layer_manifest.md`
- `../../../schemas/contracts/v1/domains/hazards/`
- `../../../schemas/contracts/v1/evidence/`
- `../../../schemas/contracts/v1/focus/`
- `../../../schemas/contracts/v1/data/layer_manifest.schema.json`
- `../../../policy/domains/hazards/`
- `../../../data/registry/sources/hazards/`
- `../../../data/proofs/hazards/`
- `../../../release/manifests/hazards/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.negative.json`, `*.invalid.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy feature, layer, drawer, Focus, identity, evidence, policy, release, correction, rollback, source-role, freshness, disclaimer, and trust-membrane examples;
- toy `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, review-required, validation-failure, blocked-render, stale-state, missing-evidence, correction-visible, rollback-visible, or expected-output examples;
- contrast examples showing the difference between valid governed envelopes and negative/invalid variants;
- paired expected outputs in `golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, tile bytes, renderer implementations, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the lane purpose, file purpose, expected outcome, and consumer notes explicit.
- Use toy IDs, toy source refs, toy feature refs, toy layer refs, toy evidence refs, toy citation refs, toy policy refs, toy release refs, toy timestamps, toy digests, and toy hashes.
- Make expected posture explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, bounded context, evidence-resolved, missing-evidence, citation-validated, policy-allowed, release-permitted, release-blocked, source-role-preserved, source-role-conflicted, freshness-visible, stale, expired, correction-visible, rollback-visible, disclaimer-visible, or expected output.
- Pair each stable input with an expected output in `golden/` when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, resolver context, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture success or failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior changes, update the paired input, expected output, consumer notes, child README, and `golden/README.md` together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced greenfield stub content.
- Child README inventory: PARTIALLY VERIFIED against populated child READMEs fetched during this update sequence.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Valid fixture alignment: PARTIALLY VERIFIED against `valid/README.md`.
- Negative fixture alignment: PARTIALLY VERIFIED against `negative/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `invalid/README.md`.
- Golden fixture alignment: PARTIALLY VERIFIED against `golden/README.md`.
- Feature-resolver fixture alignment: PARTIALLY VERIFIED against `feature_resolver/README.md`.
- Drawer fixture alignment: PARTIALLY VERIFIED against `drawer/README.md`.
- Focus fixture alignment: PARTIALLY VERIFIED against `focus/README.md`.
- Identity fixture alignment: PARTIALLY VERIFIED against `identity/README.md`.
- Layer-manifest fixture alignment: PARTIALLY VERIFIED against `layer_manifest/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, valid-fixture checks, negative-fixture checks, invalid-fixture checks, golden-file checks, governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, identity checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, source-role checks, freshness checks, UI tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
