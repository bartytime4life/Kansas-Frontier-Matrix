# Hazards feature-resolver fixtures

`fixtures/domains/hazards/feature_resolver/`

Status: draft / fixture lane / Hazards feature-detail resolver examples.

This directory is for small synthetic Hazards feature-resolver fixture examples. These fixtures describe toy feature requests, layer-feature refs, canonical feature refs, temporal scopes, caller posture, `HazardsDecisionEnvelope` outputs, finite outcomes, source-role state, evidence state, policy state, release state, freshness state, correction state, rollback state, and boundary labels for Hazards feature/detail interactions.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, policy decisions, review approvals, release state, public API material, public map material, public tiles, official-source authority, Hazards truth, or published artifacts.

## Resolver posture

The `HazardsDecisionEnvelope` contract defines the feature/detail resolver envelope returned when KFM answers, abstains, denies, or errors on a Hazards feature/detail request while preserving the Hazards boundary.

The Hazards API contract identifies the feature/detail resolver as the surface that resolves a clicked or queried Hazards feature to a governed claim envelope. The surface uses finite outcomes: `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. Route names, DTO field-level enforcement, validators, policy runtime, fixtures, release artifacts, UI behavior, and CI/test coverage remain `NEEDS VERIFICATION`.

This fixture lane can support future resolver checks, but fixture examples do not prove governed API route behavior, policy enforcement, EvidenceBundle closure, release integration, UI implementation, or schema enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../README.md` | Parent Hazards fixture lane; currently a greenfield stub during this update. |
| `../drawer/` | Drawer fixtures may consume resolver outputs and project them into Evidence Drawer payloads. |
| `../../golden/` | Future expected-output examples may be paired there if a Hazards golden lane is created. |
| `../../invalid/` | Future negative-path examples may be paired there if a Hazards invalid lane is created. |
| `../../../../contracts/domains/hazards/hazards_decision_envelope.md` | Resolver envelope semantics; this lane supplies examples only. |
| `../../../../docs/domains/hazards/API_CONTRACTS.md` | Hazards governed API surface doctrine; this lane supplies examples only. |
| `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md` | Map/UI flow; resolver output feeds public UI through governed surfaces. |
| `../../../../schemas/contracts/v1/domains/hazards/` | Hazards schema home; current enforcement remains bounded by contract status. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../README.md`
- `../drawer/README.md`
- `../../../README.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../../contracts/domains/hazards/domain_layer_descriptor.md`
- `../../../../contracts/domains/hazards/domain_observation.md`
- `../../../../contracts/domains/hazards/domain_validation_report.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../docs/domains/hazards/SOURCE_REGISTRY.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../policy/domains/hazards/`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../data/registry/sources/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy feature/detail resolver requests with feature refs, layer refs, canonical ids, temporal scopes, caller contexts, and normalized request digests;
- toy `HazardsDecisionEnvelope` outputs using `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- toy Hazards object-family refs, source-role refs, evidence refs, policy refs, release refs, freshness refs, correction refs, and rollback refs;
- paired expected outputs in a future Hazards `golden/` lane when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy feature refs, toy layer refs, toy request refs, toy evidence refs, toy citation refs, toy timestamps, toy digests, and toy hashes.
- Make resolver posture explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, stale, expired, unknown source role, no-data, failed verification, release-blocked, correction-visible, rollback-visible, or boundary-labeled.
- Keep source role, object family, evidence state, citation state, policy state, release state, freshness state, temporal scope, correction state, rollback state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, evidence support, policy filtering, release posture, freshness posture, source-role validity, trust-membrane safety, and drawer projection readiness separate.
- Do not treat fixture success as EvidenceBundle closure, source authority, policy approval, release state, API implementation proof, public-map authority, or published output.

## Expected resolver fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic released historical hazard feature with evidence refs and valid release state | `ANSWER` | Bounded context only. |
| Synthetic feature with missing EvidenceBundle support | `ABSTAIN` | Cite-or-abstain remains visible. |
| Synthetic feature with unresolved source role | `ABSTAIN` or `DENY` | Source-role collapse is not allowed. |
| Synthetic expired operational context presented as current | `DENY` or validation failure | Freshness state must remain explicit. |
| Synthetic blocked public-use request | `DENY` | Boundary and referral posture remain visible where material. |
| Synthetic request for unreleased candidate or internal lifecycle material | `DENY` | Resolver reads governed released surfaces, not internal stores. |
| Malformed feature ref or unsupported object family | `ERROR` | Error remains finite and does not fall through to a generic answer. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, resolver contracts, or consumer contracts are added.
- Link each fixture to the Hazards decision-envelope contract review, API contract check, schema check, source-role check, evidence-resolution check, citation check, freshness check, policy-filter check, release-readiness check, drawer projection check, Focus Mode test, correction check, rollback check, or governed-API dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Hazards decision-envelope alignment: PARTIALLY VERIFIED against `contracts/domains/hazards/hazards_decision_envelope.md`.
- Hazards API-contract alignment: PARTIALLY VERIFIED against `docs/domains/hazards/API_CONTRACTS.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, feature-resolver checks, governed-API tests, drawer projection checks, Focus Mode tests, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.
