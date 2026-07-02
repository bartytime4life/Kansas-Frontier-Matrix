# Hazards negative fixtures

`fixtures/domains/hazards/negative/`

Status: draft / negative fixture lane / fail-closed scenario staging.

This directory is for small synthetic Hazards negative-path fixture examples that are being drafted, grouped, or staged before they are promoted into a more specific invalid fixture lane. Use this lane for negative cases that should not produce a normal public `ANSWER`, but whose exact consumer, defect family, expected envelope, or child-lane placement is still being worked out.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, AI authority, or published artifacts.

## Negative fixture posture

The populated `../invalid/` lane is the more specific fail-closed index for known invalid Hazards cases. It already covers missing drawer disclaimer state, expired operational context shown as current, blocked Focus Mode requests, modeled/regulatory source-role collapse, temporal role swaps, direct UI reads of internal material, and unresolved evidence references.

Use this `negative/` lane when a negative case is useful but not yet sorted into a stable invalid child lane. Once the defect family and expected outcome stabilize, move or cross-link the case into `../invalid/` or a specific child lane there.

This lane can support future validation and UI checks, but examples here do not prove validator implementation, governed API behavior, UI behavior, policy enforcement, release integration, schema enforcement, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../invalid/` | Canonical populated fail-closed index for stable invalid Hazards fixture families. |
| `../golden/` | Stable expected outputs for negative/invalid inputs may be paired there. |
| `../feature_resolver/` | Negative resolver examples may be staged here before becoming invalid resolver cases. |
| `../drawer/` | Negative drawer examples may be staged here before becoming invalid drawer cases. |
| `../focus/` | Negative Focus Mode examples may be staged here before becoming invalid Focus cases. |
| `../identity/` | Negative identity/source-role examples may be staged here before becoming invalid identity cases. |
| `../layer_manifest/` | Negative layer-manifest examples may be staged here before becoming invalid layer-manifest cases. |
| `../README.md` | Parent Hazards fixture lane; still a greenfield stub during this update. |

## When to use `negative/` vs `invalid/`

| Use case | Preferred lane | Reason |
|---|---|---|
| The defect family and expected failure are already known | `../invalid/<case>/` | Specific invalid lanes are easier to validate and pair with golden outputs. |
| The case is exploratory or not yet categorized | `./` | This lane can stage the scenario without creating a premature child taxonomy. |
| The example is a malformed payload with stable expected output | `../invalid/<case>/` plus `../golden/` | Stable regression cases should live in a precise lane. |
| The example is a broad negative scenario sketch | `./` | Narrative or design-stage examples can live here until narrowed. |
| The example accidentally contains real source material | Neither | Move it out of fixtures and route through the governed lifecycle/quarantine path. |

## Current known invalid families

These families are currently indexed under `../invalid/` rather than here:

- missing required drawer disclaimer or boundary label state;
- expired warning/advisory context displayed as current;
- Focus Mode used as an alert-like or current-action authority;
- modeled or derived context labeled as observed evidence;
- regulatory/designation context labeled as observed event evidence;
- source role swapped across event, retrieval, review, correction, or release time;
- public UI reading RAW, WORK, QUARANTINE, unpublished, or internal material directly;
- unresolved or invalid evidence references.

## Related references

- `../invalid/README.md`
- `../golden/README.md`
- `../feature_resolver/README.md`
- `../drawer/README.md`
- `../focus/README.md`
- `../identity/README.md`
- `../layer_manifest/README.md`
- `../../README.md`
- `../../../../docs/architecture/governed-api.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/focus/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.negative.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- draft negative examples for resolver, drawer, Focus Mode, identity, evidence, policy, release, correction, rollback, source-role, freshness, layer-manifest, and trust-membrane behavior;
- toy `ABSTAIN`, `DENY`, `ERROR`, review-required, validation-failure, blocked-render, stale-state, missing-evidence, or expected-output examples;
- design-stage scenario notes that need later sorting into a specific invalid child lane;
- contrast examples showing the difference between a negative input and a valid governed envelope;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the negative condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `ABSTAIN`, `DENY`, `ERROR`, review-required, validation failure, blocked render, stale-state, missing-evidence, or expected output.
- Pair each stable negative input with an expected failure output when practical.
- Move stable negative cases to `../invalid/<case>/` when the defect family becomes clear.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, resolver context, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Maintenance notes

- Update this README when new negative child lanes, negative payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable negative fixture to the exact invalid lane, check, and consumer that uses it.
- If expected negative behavior stabilizes, update the paired input, expected output, consumer notes, child README, `../invalid/README.md`, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced one-character placeholder content.
- Negative fixture payload inventory: no payload files verified under this parent during this update.
- Invalid lane relationship: PARTIALLY VERIFIED against `fixtures/domains/hazards/invalid/README.md`.
- Hazards layer-manifest fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/layer_manifest/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards identity fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/identity/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, negative-fixture checks, invalid-fixture checks, governed-API tests, feature-resolver checks, drawer checks, Focus Mode checks, identity checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, source-role checks, freshness checks, UI tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
