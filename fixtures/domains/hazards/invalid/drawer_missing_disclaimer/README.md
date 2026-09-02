# Hazards invalid drawer-missing-disclaimer fixtures

`fixtures/domains/hazards/invalid/drawer_missing_disclaimer/`

Status: draft / invalid fixture lane / missing required drawer label examples.

This directory is for small synthetic negative-path Hazards drawer fixtures where a drawer-like payload is missing the required public-facing boundary/disclaimer state. These examples are meant to verify that incomplete drawer payloads fail closed with `DENY`, `ERROR`, review-required, or validation-failure outcomes rather than rendering as a valid public drawer.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Invalid-case posture

The Hazards drawer fixture lane states that drawer examples must preserve finite outcomes, source-role state, freshness/expiry state, official-source referral state, and the required public boundary label where material. It also states that drawer payloads are governed projections and must not read RAW, WORK, QUARANTINE, or internal proof stores directly.

Hazards UI doctrine states that Hazards surfaces must label themselves as planning context rather than alerting context and must preserve redirect/referral behavior for official sources. This lane tests the failure mode where that required label/disclaimer state is missing, blank, hidden, stale, contradictory, or detached from the rendered drawer state.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, UI behavior, policy enforcement, route behavior, release integration, or schema enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../drawer/` | Positive-path drawer fixture lane; this lane covers missing-label negative cases. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../../feature_resolver/` | Resolver outputs may be projected into drawer payloads before this invalid state is detected. |
| `../../focus/` | Focus handoff must not inherit an invalid drawer state. |
| `../` | Parent invalid lane; not verified as populated during this update. |
| `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md` | UI label and drawer doctrine; this lane supplies examples only. |
| `../../../../contracts/evidence/evidence_drawer_payload.md` | Drawer payload semantics; this lane supplies examples only. |
| `../../../../schemas/contracts/v1/evidence/` and `../../../../schemas/contracts/v1/ui/` | Expected schema homes; fixture failure does not prove schema authority. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../../drawer/README.md`
- `../../golden/README.md`
- `../../feature_resolver/README.md`
- `../../focus/README.md`
- `../../../README.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/ui/`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy drawer payloads missing required disclaimer, label, referral, freshness, expiry, citation, policy, review, release, correction, or rollback display state;
- toy `DENY`, `ERROR`, review-required, validation-failure, or blocked-render expected outputs;
- toy examples showing the difference between a valid drawer state and an invalid missing-disclaimer state;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy feature refs, toy layer refs, toy evidence refs, toy citation refs, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: missing label, blank label, hidden label, contradictory label, missing referral state, missing freshness state, missing expiry state, or dropped caveat.
- Make expected outcome explicit: `DENY`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence support, policy filtering, release posture, freshness posture, source-role validity, UI label visibility, accessibility state, and trust-membrane safety separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Drawer payload missing required boundary label | `DENY` or validation failure | The drawer must not render as valid. |
| Drawer payload label is present but blank | `DENY` or validation failure | Empty text does not satisfy the label requirement. |
| Drawer payload label contradicts freshness/expiry state | `DENY` or review-required output | Trust state must remain coherent. |
| Drawer payload drops source-role caveat | `ABSTAIN`, `DENY`, or validation failure | Source-role collapse is not allowed. |
| Drawer payload drops citation or evidence refs | `ABSTAIN` or validation failure | Cite-or-abstain remains visible. |
| Drawer payload drops correction or rollback posture | Review-required output | Public trust state must be inspectable. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the drawer check, schema check, policy-filter check, UI label check, accessibility check, source-role check, freshness check, release-readiness check, correction check, rollback check, or governed-API dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards UI label alignment: PARTIALLY VERIFIED against `docs/domains/hazards/MAP_UI_CONTRACTS.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, drawer checks, UI label checks, accessibility checks, governed-API tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
