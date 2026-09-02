# Hazards invalid regulatory-labeled-observed fixtures

`fixtures/domains/hazards/invalid/regulatory_labeled_observed/`

Status: draft / invalid fixture lane / source-role anti-collapse examples.

This directory is for small synthetic negative-path Hazards fixtures where regulatory, administrative-regulatory, or designation-style context is incorrectly labeled, queried, or displayed as observed event evidence. These examples are meant to verify that source-role collapse fails closed with `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation-failure outcomes rather than producing a valid observed Hazards claim.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, or published artifacts.

## Invalid-case posture

The Hazards source-role matrix says `regulatory` means an authoritative determination by a governing body and must be cited as regulatory context, not as an observed event or modeled estimate. The same matrix marks `regulatory` as forbidden for `HazardEvent` and `HazardObservation`, while `FloodContext` such as NFHL is regulatory context.

The deny-condition register names “regulatory zone labeled as an observed flood / event” as a denied collapse pattern. It requires separate regulatory-layer and observed-event lanes, visible UI labeling, and `not_authoritative_for` guardrails so a regulatory source family cannot support observed-event claims by label change, UI styling, Focus Mode wording, or promotion.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, API behavior, UI behavior, policy enforcement, release integration, schema enforcement, or source-descriptor enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../identity/` | Identity fixtures should preserve object family, source role, temporal scope, and digest instead of relabeling regulatory context as observed evidence. |
| `../../feature_resolver/` | Resolver fixtures should emit finite fail-closed outcomes for regulatory-as-observed requests. |
| `../../drawer/` | Drawer fixtures should display regulatory context and caveats rather than observed-event labels. |
| `../../focus/` | Focus fixtures must not summarize regulatory context as observed event evidence. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../modeled_labeled_observed/` | Related negative case for modeled context labeled as observed. |
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
- toy regulatory designations mislabeled as observed Hazards records;
- toy payloads where regulatory context is incorrectly projected into `HazardEvent`, `HazardObservation`, or observed-event wording;
- toy source-descriptor examples missing or ignoring `not_authoritative_for` guardrails;
- toy drawer, feature-resolver, Focus Mode, identity, and golden-output examples that exercise source-role anti-collapse behavior;
- toy `DENY`, `ABSTAIN`, `ERROR`, review-required, validation-failure, or blocked-render expected outputs;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy source refs, toy object-family refs, toy regulatory refs, toy `not_authoritative_for` refs, toy evidence refs, toy citation refs, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: regulatory labeled observed, regulatory zone treated as event evidence, designation displayed as direct observation, missing guardrail, ignored guardrail, observed-style drawer badge, observed-style resolver answer, or observed wording in Focus Mode.
- Make expected outcome explicit: `DENY`, `ABSTAIN`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, source-role validity, source-descriptor guardrails, evidence support, citation validation, policy filtering, release posture, drawer display, Focus Mode wording, and resolver context separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Regulatory flood-zone context labeled as an observed flood event | `DENY` or validation failure | Regulatory context must not become event evidence. |
| Regulatory designation projected into `HazardObservation` | `DENY` or validation failure | Observed records require observed source role. |
| Source descriptor lacks `not_authoritative_for` guardrail | `ERROR` or review-required output | Guardrails must be inspectable. |
| Source descriptor guardrail exists but is ignored | `DENY` or validation failure | Machine-checkable refusal must be honored. |
| Focus Mode describes regulatory context as observed evidence | `ABSTAIN` or validation failure | Generated language cannot collapse source roles. |
| Drawer displays regulatory context with observed badge | `DENY` or validation failure | Public UI must preserve source-role state. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the source-role check, source-descriptor check, `not_authoritative_for` check, identity check, feature-resolver check, drawer check, Focus Mode check, schema check, policy-filter check, release-readiness check, correction check, rollback check, or governed-API dry-run that consumes it.
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
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, source-role checks, source-descriptor checks, `not_authoritative_for` checks, identity checks, feature-resolver checks, drawer checks, Focus Mode checks, governed-API tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
