# Hazards invalid modeled-labeled-observed fixtures

`fixtures/domains/hazards/invalid/modeled_labeled_observed/`

Status: draft / invalid fixture lane / source-role anti-collapse examples.

This directory is for small synthetic negative-path Hazards fixtures where modeled, derived, aggregate-like, or reconstruction-style context is incorrectly labeled, queried, or displayed as observed evidence. These examples are meant to verify that source-role collapse fails closed with `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation-failure outcomes rather than producing a valid observed Hazards claim.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Invalid-case posture

The Hazards source-role matrix says source role is a first-class identity attribute. An observed reading is not interchangeable with a modeled estimate, and governed API or lifecycle surfaces fail closed when those roles are conflated.

The same matrix names “modeled product labeled or queried as observed” as a denied collapse pattern. Modeled material must preserve its model identity, run receipt, uncertainty, provenance, and bounds. A modeled smoke trajectory, drought surface, exposure surface, reconstructed swath, or other derived product cannot become an observed record by label change, UI styling, Focus Mode wording, or promotion.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, API behavior, UI behavior, policy enforcement, release integration, schema enforcement, or model-run receipt enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../identity/` | Identity fixtures should preserve object family, source role, temporal scope, and digest instead of relabeling modeled as observed. |
| `../../feature_resolver/` | Resolver fixtures should emit finite fail-closed outcomes for modeled-as-observed requests. |
| `../../drawer/` | Drawer fixtures should display modeled role and caveats rather than observed labels. |
| `../../focus/` | Focus fixtures must not summarize modeled context as observed evidence. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../expired_warning_as_current/` | Related negative case for freshness/state collapse. |
| `../focus_mode_as_alert/` | Related negative case for public-use boundary collapse. |
| `../` | Parent invalid lane; not verified as populated during this update. |
| `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md` | Source-role anti-collapse doctrine; this lane supplies examples only. |
| `../../../../docs/atlas/source-role-anti-collapse.md` | Cross-domain anti-collapse doctrine; this lane supplies examples only. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../../identity/README.md`
- `../../feature_resolver/README.md`
- `../../drawer/README.md`
- `../../focus/README.md`
- `../../golden/README.md`
- `../expired_warning_as_current/README.md`
- `../focus_mode_as_alert/README.md`
- `../drawer_missing_disclaimer/README.md`
- `../../../README.md`
- `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/domains/hazards/domain_observation.md`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy modeled products mislabeled as observed Hazards records;
- toy payloads where model metadata, run receipt refs, uncertainty refs, input provenance, or bounds are missing;
- toy drawer, feature-resolver, Focus Mode, identity, and golden-output examples that exercise source-role anti-collapse behavior;
- toy `DENY`, `ABSTAIN`, `ERROR`, review-required, validation-failure, or blocked-render expected outputs;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy source refs, toy object-family refs, toy model-run refs, toy uncertainty refs, toy evidence refs, toy citation refs, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: modeled labeled observed, derived labeled observed, reconstructed labeled observed, missing model-run ref, missing uncertainty, missing provenance, observed-style drawer badge, observed-style resolver answer, or observed wording in Focus Mode.
- Make expected outcome explicit: `DENY`, `ABSTAIN`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, source-role validity, model-run support, uncertainty support, evidence support, citation validation, policy filtering, release posture, drawer display, Focus Mode wording, and resolver context separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Modeled smoke trajectory labeled as observed smoke | `DENY` or validation failure | Model role must remain visible. |
| Drought surface labeled as direct observation | `DENY` or validation failure | Derived/aggregate context cannot become observed truth. |
| Reconstructed swath displayed as observed path | `DENY` or review-required output | Reconstruction must preserve modeled/reconstructed caveat. |
| Model output missing run receipt ref | `ERROR` or validation failure | Modeled outputs need process support. |
| Model output missing uncertainty or bounds | `ABSTAIN`, `DENY`, or review-required output | Limits must remain inspectable. |
| Focus Mode describes modeled context as observed evidence | `ABSTAIN` or validation failure | Generated language cannot collapse source roles. |
| Drawer displays modeled context with observed badge | `DENY` or validation failure | Public UI must preserve source-role state. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the source-role check, model-run check, uncertainty check, identity check, feature-resolver check, drawer check, Focus Mode check, schema check, policy-filter check, release-readiness check, correction check, rollback check, or governed-API dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Hazards source-role matrix alignment: PARTIALLY VERIFIED against `docs/domains/hazards/SOURCE_ROLE_MATRIX.md`.
- Hazards identity fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/identity/README.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, source-role checks, model-run checks, uncertainty checks, identity checks, feature-resolver checks, drawer checks, Focus Mode checks, governed-API tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
