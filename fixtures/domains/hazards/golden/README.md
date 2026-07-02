# Hazards golden fixtures

`fixtures/domains/hazards/golden/`

Status: draft / fixture lane / expected-output examples.

This directory is for small synthetic Hazards expected-output fixtures. Golden fixtures describe the expected result for known synthetic Hazards inputs used by bounded resolver checks, drawer projection checks, Focus Mode checks, renderer examples, governed API examples, policy dry-runs, release-readiness dry-runs, correction/rollback dry-runs, and documentation examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, domain truth, official-source authority, AI authority, or published artifacts.

## Golden posture

Use this lane for stable expected outputs paired with synthetic Hazards inputs from sibling fixture lanes. A golden fixture may describe expected finite outcomes, normalized envelopes, rendered drawer states, Focus Mode response envelopes, citation-check results, policy-filter results, release-state results, stale-state results, correction visibility, rollback visibility, or public-safe UI states.

Golden fixtures are regression anchors only after their producer and consumer are documented. They do not prove EvidenceBundle closure, policy enforcement, route behavior, UI implementation, AI runtime behavior, release integration, schema enforcement, or public publication by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains expected outputs for synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is still a greenfield stub during this update.

## Relationship to input lanes

| Input lane | Expected-output use | Current posture |
|---|---|---|
| `../feature_resolver/` | Expected `HazardsDecisionEnvelope` outputs for synthetic feature/detail requests. | Draft fixture lane. |
| `../drawer/` | Expected `EvidenceDrawerPayload` / drawer projection outputs for synthetic Hazards context. | Draft fixture lane. |
| `../focus/` | Expected `RuntimeResponseEnvelope` and `AIReceipt` outputs for synthetic Focus Mode requests. | Draft fixture lane. |
| `../invalid/` | Future negative-path inputs may pair with golden outputs if a Hazards invalid lane is created. | Not verified during this update. |
| `../README.md` | Parent Hazards fixture lane. | Present but greenfield stub during this update. |

## Related references

- `../README.md`
- `../feature_resolver/README.md`
- `../drawer/README.md`
- `../focus/README.md`
- `../../../README.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../schemas/contracts/v1/domains/hazards/`
- `../../../../schemas/contracts/v1/evidence/`
- `../../../../schemas/contracts/v1/focus/`
- `../../../../schemas/contracts/v1/runtime/`
- `../../../../schemas/contracts/v1/ai/`
- `../../../../policy/domains/hazards/`
- `../../../../data/registry/sources/hazards/`
- `../../../../release/manifests/hazards/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.expected.json`, `*.golden.json`, `*.expected.yaml`, `*.expected.yml`, `*.expected.md`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- expected `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` outputs for paired synthetic inputs;
- expected resolver envelopes, drawer payloads, Focus Mode responses, AI receipts, citation-validation results, policy-filter results, stale-state results, correction-state results, and rollback-state results;
- expected normalized IDs, source-role labels, evidence refs, release refs, policy refs, citation refs, freshness refs, visible limitations, and public-safe display labels;
- documentation examples that identify their paired input lane and expected consumer.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, AI authority, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep expected outputs synthetic, compact, deterministic, reviewable, and public-safe.
- Name files so the paired input and expected outcome are obvious.
- Use toy IDs, toy feature refs, toy layer refs, toy evidence refs, toy citation refs, toy prompt refs, toy timestamps, toy digests, and toy hashes.
- Make outcome posture explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, stale, expired, missing evidence, failed citation validation, conflicting source roles, release-blocked, correction-visible, rollback-visible, or boundary-labeled.
- Keep schema validity, semantic validity, evidence support, citation validation, policy filtering, release posture, freshness posture, source-role validity, AI receipt completeness, drawer projection, resolver context, and Focus Mode behavior separate.
- Do not treat a golden output as EvidenceBundle closure, source authority, policy approval, release state, API implementation proof, UI implementation proof, AI correctness proof, public-map authority, or published output.

## Expected golden examples

| Paired input type | Expected output type | Notes |
|---|---|---|
| Synthetic feature resolver request | `HazardsDecisionEnvelope` expected output | Finite resolver outcome and reason state. |
| Synthetic drawer input | `EvidenceDrawerPayload` expected output | Trust-visible drawer projection. |
| Synthetic Focus Mode request | `RuntimeResponseEnvelope` + `AIReceipt` expected output | Evidence-bounded answer, abstain, deny, or error. |
| Synthetic missing-evidence case | `ABSTAIN` expected output | Cite-or-abstain remains inspectable. |
| Synthetic blocked public-use case | `DENY` expected output | Boundary posture remains inspectable. |
| Synthetic malformed request | `ERROR` expected output | Error remains finite and reviewable. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each golden fixture to the exact input fixture, check, and consumer that uses it.
- If expected behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: replaced one-character placeholder content.
- Parent Hazards fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Focus fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/focus/README.md`.
- Hazards API alignment: PARTIALLY VERIFIED against `docs/domains/hazards/API_CONTRACTS.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, golden-file checks, feature-resolver checks, drawer checks, Focus Mode checks, governed-API tests, release-readiness checks, schema checks, policy checks, AIReceipt checks, citation-validation checks, and UI implementation.
- Tests and validators: NOT RUN.
