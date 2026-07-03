# Generated receipt fixtures

`fixtures/generated_receipt/`

Status: draft / fixture parent index / generated-receipt synthetic examples.

This directory is the parent lane for small synthetic generated-receipt fixtures. Use it to organize positive-path and fail-closed toy examples for receipt shape, finite outcomes, evidence refs, citation refs, policy refs, replay refs, integrity refs, persistence refs, public-summary refs, correction refs, rollback refs, and expected outputs.

These files are examples only. They are not actual receipts, EvidenceBundles, SourceDescriptors, policy decisions, promotion decisions, release manifests, proof packs, signed envelopes, public API material, public map material, public tiles, release state, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Fixture parent posture

Generated-receipt fixtures support bounded checking and documentation for receipt-like runtime accountability objects. A fixture may imitate a receipt shape or expected validation result, but it must remain synthetic and must not be treated as sealed process memory, proof material, release evidence, or public truth.

KFM receipt doctrine treats an AIReceipt as a runtime accountability record, not the answer and not a substitute for EvidenceBundle. Valid fixtures may demonstrate complete toy receipts; invalid fixtures should demonstrate fail-closed behavior. Neither path proves validator implementation, policy enforcement, persistence, signing, replay, public projection, release integration, or CI coverage by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, governed-AI runtime root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, governed API routes, persistence checks, signing checks, policy bundles, release manifests, proof stores, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `valid/` | Synthetic positive-path generated-receipt examples with complete toy receipt fields and expected pass posture. | Validation pass, policy pass, replay pass, persistence pass, projection pass, release-ready, `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or expected output. |
| `invalid/` | Synthetic fail-closed generated-receipt examples for bad receipt shape, bad outcome logic, citation gaps, policy drift, replay drift, receipt-family collapse, or unsafe projection. | `DENY`, `ERROR`, validation failure, policy failure, replay failure, blocked persistence, blocked projection, release-readiness failure, or expected output. |

## Relationship to receipt governance

| Lane or document | Relationship |
|---|---|
| `../README.md` | Root fixture rules; this lane must remain synthetic and non-authoritative. |
| `valid/README.md` | Positive-path sibling lane. |
| `invalid/README.md` | Fail-closed sibling lane. |
| `../../docs/architecture/governed-ai/AI_RECEIPTS.md` | Governs AIReceipt meaning, finite outcomes, lifecycle, validator expectations, receipt-family boundaries, and replay posture. |
| `../../contracts/runtime/ai_receipt.md` | Expected canonical contract home if present; fixtures do not define contracts. |
| `../../schemas/contracts/v1/runtime/ai_receipt.schema.json` | Expected machine-shape home if present; fixtures do not define schemas. |
| `../../policy/runtime/ai_receipts.rego` | Expected runtime receipt policy home if present; fixtures do not decide policy. |
| `../../tools/validators/ai/` | Expected validator home if present; fixtures do not implement validators. |
| `../../data/receipts/ai/` | Proposed actual AIReceipt persistence home; fixtures do not store sealed receipts. |
| `../../data/proofs/` | Proof home; fixtures do not create proof authority. |
| `../../release/signatures/` | Signature home if present; fixtures do not create signing authority. |
| `../../release/manifests/` | Release home; fixtures do not publish. |

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.positive.json`, `*.negative.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy generated-receipt examples for complete receipt shapes, incomplete receipt shapes, finite outcomes, evidence refs, citation refs, policy refs, replay refs, integrity refs, signing refs, persistence refs, public-summary refs, correction refs, rollback refs, and expected outputs;
- positive-path examples in `valid/`;
- fail-closed examples in `invalid/`;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for actual receipts, signed envelopes, EvidenceBundles, SourceDescriptors, CitationValidationReports, PolicyDecisions, PromotionDecisions, ReleaseManifests, proof packs, lifecycle data, source exports, implementation code, public API material, public map material, public tiles, direct runtime output, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy refs, toy digests, toy timestamps, toy model IDs, toy policy refs, toy evidence refs, toy citation refs, toy output refs, toy error refs, and toy signature refs.
- Make fixture posture explicit: valid, invalid, positive, negative, expected output, evidence-resolved, evidence-missing, citation-ready, citation-failed, policy-pass, policy-fail, replay-pass, replay-fail, persistence-pass, persistence-blocked, projection-pass, projection-blocked, release-ready, release-blocked, correction-visible, rollback-ready, or review-required.
- Make expected outcome explicit when known: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, policy pass, policy failure, replay pass, replay failure, blocked persistence, blocked projection, release-readiness failure, or expected output.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, outcome validity, reason-code validity, evidence state, citation state, policy state, replay state, signature state, persistence state, public-projection state, release state, correction state, rollback state, and expected-output state separate.
- Do not treat fixture success or failure as receipt storage proof, proof authority, policy approval, validator implementation proof, API implementation proof, release state, public-map authority, public-summary authority, or published output.

## Expected fixture families

| Scenario family | Preferred child lane | Expected posture |
|---|---|---|
| Minimal complete `ABSTAIN`, `DENY`, or `ERROR` receipt | `valid/` | Validation pass or policy pass. |
| Complete `ANSWER` receipt with evidence and citation refs | `valid/` | Validation pass, policy pass, or replay-ready. |
| Deterministic replay example | `valid/` | Replay pass or expected output. |
| Missing outcome or invalid outcome enum | `invalid/` | Schema failure or `ERROR`. |
| `ANSWER` without evidence refs or passing citation validation | `invalid/` | Policy failure or `DENY`. |
| Stale policy bundle hash | `invalid/` | `ERROR`. |
| Receipt-family collapse | `invalid/` | Validation failure or review-required. |
| Raw receipt exposed as public surface | `invalid/` | Blocked projection. |
| Stable expected output is ready to compare | Documented pair or future expected-output lane | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact schema check, policy check, replay check, governed-API test, public-projection check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual receipts, proof material, release material, source exports, or lifecycle data, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated `valid/README.md` and `invalid/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Valid fixture alignment: PARTIALLY VERIFIED against `valid/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `invalid/README.md`.
- AI receipt doctrine alignment: PARTIALLY VERIFIED against `docs/architecture/governed-ai/AI_RECEIPTS.md` from recent preceding updates.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Contract/schema/policy alignment: NEEDS VERIFICATION against live `contracts/runtime/`, `schemas/contracts/v1/runtime/`, and `policy/runtime/` files.
- Consumer alignment: NEEDS VERIFICATION against validators, policy checks, replay checks, signing checks, persistence checks, public-projection checks, governed-API tests, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, and CI implementation.
- Tests and validators: NOT RUN.
