# Hazards invalid temporal-role-swap fixtures

`fixtures/domains/hazards/invalid/temporal_role_swap/`

Status: draft / invalid fixture lane / temporal source-role anti-collapse examples.

This directory is for small synthetic negative-path Hazards fixtures where source role changes incorrectly across event time, issue time, retrieval time, review time, correction time, or release time. These examples are meant to verify that temporal role swaps fail closed with `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation-failure outcomes rather than producing a valid Hazards claim.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Invalid-case posture

The Hazards source-role matrix says source role is set at admission and preserved through every promotion. Promotion does not upgrade one role into another; those are separate governed transitions with their own evidence and review requirements.

The same matrix says promotion is a governed state transition, not a role upgrade. A modeled surface stays modeled from RAW to PUBLISHED; a candidate record becomes verified only through a separate governed transition; correcting a role creates a new `SourceDescriptor` plus correction notice rather than an in-place edit.

The Hazards identity fixture lane also treats source role and temporal scope as identity-bearing context. This lane tests the failure mode where a record changes role merely because the current time, retrieval time, review time, or release time changed.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, API behavior, UI behavior, policy enforcement, release integration, schema enforcement, or source-descriptor enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../identity/` | Identity fixtures should preserve source role and temporal scope instead of allowing role swaps by time label. |
| `../../feature_resolver/` | Resolver fixtures should emit finite fail-closed outcomes for temporal role-swap requests. |
| `../../drawer/` | Drawer fixtures should display source role and freshness state without converting role. |
| `../../focus/` | Focus fixtures must not explain a time change as a source-role upgrade. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../modeled_labeled_observed/` | Related negative case for modeled context labeled as observed. |
| `../regulatory_labeled_observed/` | Related negative case for regulatory context labeled as observed. |
| `../expired_warning_as_current/` | Related negative case for freshness/state collapse. |
| `../focus_mode_as_alert/` | Related negative case for public-use boundary collapse. |
| `../` | Parent invalid lane; not verified as populated during this update. |
| `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md` | Source-role anti-collapse doctrine; this lane supplies examples only. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/hazards/` | Release home; fixtures do not approve publication. |

## Related references

- `../../identity/README.md`
- `../../feature_resolver/README.md`
- `../../drawer/README.md`
- `../../focus/README.md`
- `../../golden/README.md`
- `../modeled_labeled_observed/README.md`
- `../regulatory_labeled_observed/README.md`
- `../expired_warning_as_current/README.md`
- `../focus_mode_as_alert/README.md`
- `../drawer_missing_disclaimer/README.md`
- `../../../README.md`
- `../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy records whose source role changes incorrectly across event, issue, valid-through, retrieval, review, correction, or release times;
- toy source descriptors that try to update `source_role` in place instead of creating a governed correction/supersession path;
- toy drawer, feature-resolver, Focus Mode, identity, and golden-output examples that exercise temporal role-swap checks;
- toy `DENY`, `ABSTAIN`, `ERROR`, review-required, validation-failure, or blocked-render expected outputs;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy source refs, toy object-family refs, toy source-role refs, toy temporal scopes, toy issue times, toy retrieval times, toy release times, toy correction refs, toy evidence refs, toy citation refs, toy digests, and toy hashes.
- Make the defect explicit: role changed by retrieval time, role changed by release time, candidate changed to observed without governed transition, modeled changed to observed at publication, administrative changed to observed in a timeline, or in-place source-role edit.
- Make expected outcome explicit: `DENY`, `ABSTAIN`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, source-role validity, temporal-scope validity, identity determinism, correction linkage, supersession linkage, evidence support, citation validation, policy filtering, release posture, drawer display, Focus Mode wording, and resolver context separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Candidate record becomes observed only because release time arrived | `DENY` or validation failure | Candidate needs a governed transition. |
| Modeled payload becomes observed at publication | `DENY` or validation failure | Promotion is not a role upgrade. |
| Administrative compilation becomes observed event in a timeline | `DENY` or validation failure | Administrative context must keep its role. |
| Retrieval time changes but source role changes too | `ERROR` or validation failure | Fetch timing should not rotate role. |
| In-place edit changes source role without correction/supersession | Review-required or validation failure | Role correction needs auditable path. |
| Focus Mode explains role change as time-based upgrade | `ABSTAIN` or validation failure | Generated language cannot create role transitions. |
| Drawer displays old role in header and new role in detail body | `DENY` or review-required output | Public UI role state must be coherent. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the source-role check, temporal-scope check, identity check, correction check, supersession check, feature-resolver check, drawer check, Focus Mode check, schema check, policy-filter check, release-readiness check, rollback check, or governed-API dry-run that consumes it.
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
- Hazards modeled-labeled-observed fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/invalid/modeled_labeled_observed/README.md`.
- Hazards regulatory-labeled-observed fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/invalid/regulatory_labeled_observed/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, source-role checks, temporal-scope checks, identity checks, correction checks, supersession checks, feature-resolver checks, drawer checks, Focus Mode checks, governed-API tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
