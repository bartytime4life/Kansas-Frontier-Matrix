# Hazards invalid expired-warning-as-current fixtures

`fixtures/domains/hazards/invalid/expired_warning_as_current/`

Status: draft / invalid fixture lane / expired operational-context examples.

This directory is for small synthetic negative-path Hazards fixtures where an expired `WarningContext` or `AdvisoryContext` is incorrectly presented as current. These examples are meant to verify that stale operational context fails closed with `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation-failure outcomes rather than rendering as a valid current public state.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Invalid-case posture

The Hazards API contract says a `WarningContext` or `AdvisoryContext` whose `valid_through` or `expiry` time has passed must be returned as `ABSTAIN` or `DENY`, with an explicit `freshness: expired` marker and official-source referral, never as a current warning payload.

The Hazards map/UI contract also states that a drawer should not render expired operational context as current. This lane tests the failure mode where a payload has an expired issue/validity window but still tries to use a current-state label, current-state badge, current layer style, or current drawer posture.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, UI behavior, policy enforcement, route behavior, release integration, or schema enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../feature_resolver/` | Resolver fixtures should emit finite fail-closed outcomes for expired-current cases. |
| `../../drawer/` | Drawer fixtures should show expired-state handling rather than current-state display. |
| `../../focus/` | Focus fixtures must not treat expired operational context as current. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../drawer_missing_disclaimer/` | Related negative drawer case for missing public-facing label state. |
| `../` | Parent invalid lane; not verified as populated during this update. |
| `../../../../docs/domains/hazards/API_CONTRACTS.md` | API outcome and freshness doctrine; this lane supplies examples only. |
| `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md` | Map/drawer freshness doctrine; this lane supplies examples only. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../../feature_resolver/README.md`
- `../../drawer/README.md`
- `../../focus/README.md`
- `../../golden/README.md`
- `../drawer_missing_disclaimer/README.md`
- `../../../README.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/ui/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy warning/advisory context payloads with issue, expiry, valid-through, retrieval, release, and current-time fields;
- toy payloads where `expiry_time < now` but the payload tries to render as current;
- toy `DENY`, `ABSTAIN`, `ERROR`, review-required, validation-failure, or blocked-render expected outputs;
- toy examples showing the difference between historical context display and invalid current-state display;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy feature refs, toy layer refs, toy evidence refs, toy citation refs, toy issue times, toy expiry times, toy retrieval times, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: expired warning as current, expired advisory as current, stale state hidden, stale state contradicted, missing expiry, invalid freshness badge, or current-style rendering after expiry.
- Make expected outcome explicit: `DENY`, `ABSTAIN`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence support, policy filtering, release posture, freshness posture, source-role validity, UI label visibility, accessibility state, and trust-membrane safety separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Expired `WarningContext` rendered with current-state label | `DENY` or validation failure | Current-state presentation is not allowed after expiry. |
| Expired `AdvisoryContext` rendered as current | `DENY` or validation failure | Expiry must control display posture. |
| Missing expiry field on operational-context payload | `ERROR` or validation failure | Required time bounds must be inspectable. |
| Expiry is past but freshness state says current | `DENY` or review-required output | Freshness must be coherent. |
| Expired context shown as historical context with clear stale state | Valid historical expected output | This is the safe contrast case. |
| Expired context used by Focus Mode as current evidence | `DENY` or `ABSTAIN` | Focus must preserve freshness limits. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the API outcome check, freshness check, expiry check, drawer check, Focus Mode check, schema check, policy-filter check, UI label check, accessibility check, release-readiness check, correction check, rollback check, or governed-API dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Hazards API freshness alignment: PARTIALLY VERIFIED against `docs/domains/hazards/API_CONTRACTS.md`.
- Hazards map/UI freshness alignment: PARTIALLY VERIFIED against `docs/domains/hazards/MAP_UI_CONTRACTS.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, expiry checks, freshness checks, drawer checks, Focus Mode checks, UI label checks, accessibility checks, governed-API tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
