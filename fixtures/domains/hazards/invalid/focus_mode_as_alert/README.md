# Hazards invalid focus-mode-as-alert fixtures

`fixtures/domains/hazards/invalid/focus_mode_as_alert/`

Status: draft / invalid fixture lane / blocked Focus Mode request examples.

This directory is for small synthetic negative-path Hazards fixtures where a Focus Mode request tries to use the answer surface as a current-action or alert-like authority. These examples verify that Focus Mode returns `DENY`, `ABSTAIN`, `ERROR`, review-required, or validation-failure outcomes instead of producing a normal `ANSWER`.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, AI authority, or published artifacts.

## Invalid-case posture

The Hazards API contract describes Focus Mode as evidence-bounded synthesis over released Hazards evidence bundles. Its response shape is `RuntimeResponseEnvelope` plus `AIReceipt`, and its finite outcomes are `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`.

The API contract also says blocked public-use requests, uncited authoritative claims, direct access to internal lifecycle material, and raw model text without `AIReceipt` are not valid Focus Mode answers.

The Hazards map/UI contract says Focus Mode is bounded and citation-validated. Policy prechecks can return `DENY` when the request attempts a blocked current-action use or references expired operational context.

This fixture lane can support future validation and UI checks, but examples here do not prove validator implementation, AI runtime behavior, route behavior, policy enforcement, release integration, or schema enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic invalid examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../../focus/` | Positive-path Focus Mode fixture lane; this lane covers blocked current-action cases. |
| `../../feature_resolver/` | Resolver context may feed Focus requests but does not authorize blocked answers. |
| `../../drawer/` | Drawer handoff must not convert a denied Focus output into a valid drawer answer. |
| `../../golden/` | Expected failure outputs may be paired there when stable. |
| `../expired_warning_as_current/` | Related negative case for expired operational context shown as current. |
| `../drawer_missing_disclaimer/` | Related negative case for missing public-facing label state. |
| `../` | Parent invalid lane; not verified as populated during this update. |
| `../../../../docs/domains/hazards/API_CONTRACTS.md` | Focus Mode outcome doctrine; this lane supplies examples only. |
| `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md` | Focus Mode policy-gate doctrine; this lane supplies examples only. |

## Related references

- `../../focus/README.md`
- `../../feature_resolver/README.md`
- `../../drawer/README.md`
- `../../golden/README.md`
- `../expired_warning_as_current/README.md`
- `../drawer_missing_disclaimer/README.md`
- `../../../README.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../schemas/contracts/v1/focus/`
- `../../../../schemas/contracts/v1/runtime/`
- `../../../../schemas/contracts/v1/ai/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Focus Mode requests with current-action framing, missing evidence, failed citations, expired operational context, or blocked public-use intent;
- toy `RuntimeResponseEnvelope` and `AIReceipt` negative outputs using `DENY`, `ABSTAIN`, `ERROR`, review-required, validation-failure, or blocked-render posture;
- toy policy-gate, citation-validation, visible-limitation, correction, and rollback examples;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, AI authority, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy map-context refs, toy feature refs, toy evidence refs, toy citation refs, toy prompt refs, toy timestamps, toy digests, and toy hashes.
- Make the defect explicit: blocked current-action Focus request, current-state inference, missing citations, failed citation validation, unsupported inference, expired context, or request for internal lifecycle material.
- Make expected outcome explicit: `DENY`, `ABSTAIN`, `ERROR`, review-required, validation failure, blocked render, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence support, citation validation, policy filtering, release posture, freshness posture, source-role validity, AI receipt completeness, drawer handoff, resolver context, and trust-membrane safety separate.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, AI runtime proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Focus request asks for blocked current-action guidance from Hazards context | `DENY` | Focus must not become the authority surface. |
| Focus request asks for current interpretation of expired operational context | `DENY` or `ABSTAIN` | Freshness limits must remain visible. |
| Focus request asks for an uncited authoritative claim | `DENY` or validation failure | Cite-or-abstain remains visible. |
| Focus request has insufficient evidence refs | `ABSTAIN` | Missing evidence cannot be filled by generated language. |
| Focus response lacks `AIReceipt` | `ERROR` or validation failure | Raw model text is not a valid surface. |
| Focus response drops visible limitations | Review-required output | Limitation state must remain inspectable. |

## Verification status

- Target README: replaced one-character placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Hazards Focus Mode API alignment: PARTIALLY VERIFIED against `docs/domains/hazards/API_CONTRACTS.md`.
- Hazards map/UI Focus alignment: PARTIALLY VERIFIED against `docs/domains/hazards/MAP_UI_CONTRACTS.md`.
- Hazards Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/golden/README.md`.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Parent invalid lane alignment: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, Focus Mode checks, policy-gate checks, citation-validation checks, AIReceipt checks, drawer handoff checks, feature-resolver checks, governed-API tests, release-readiness checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
