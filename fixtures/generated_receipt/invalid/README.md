# Generated receipt invalid fixtures

`fixtures/generated_receipt/invalid/`

Status: draft / invalid fixture lane / generated-receipt fail-closed examples.

This directory is for small synthetic invalid generated-receipt examples. Use it for toy receipt cases that should fail schema validation, policy validation, replay checks, receipt-family checks, citation-closure checks, integrity checks, persistence checks, public-projection checks, or release-readiness checks.

These files are examples only. They are not actual receipts, EvidenceBundles, SourceDescriptors, policy decisions, promotion decisions, release manifests, proof packs, signed envelopes, public API material, public map material, public tiles, release state, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Invalid fixture posture

Generated-receipt invalid fixtures exist to prove that bad receipt shapes and unsafe receipt semantics fail closed. They should produce `ERROR`, `DENY`, validation failure, replay failure, policy failure, blocked persistence, blocked projection, release-readiness failure, or another documented fail-closed outcome.

KFM receipt doctrine treats an AIReceipt as a runtime accountability record, not the answer and not a substitute for EvidenceBundle. A generated receipt with missing evidence support, missing citation closure, disallowed content, bad outcome logic, bad replay keys, or stale policy state must not become an `ANSWER`, proof authority, release authority, or public truth surface.

A fixture can describe a desired invalid case before validators, policies, schema checks, replay checks, signing checks, persistence checks, public-projection checks, release integration, or CI coverage exist. Fixture failure is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, governed-AI runtime root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to receipt governance

| Lane or document | Relationship |
|---|---|
| `../../docs/architecture/governed-ai/AI_RECEIPTS.md` | Governs AIReceipt meaning, finite outcomes, lifecycle, validator expectations, and negative-path coverage. |
| `../README.md` | Parent generated-receipt fixture root; currently blank at the time this invalid README is authored. |
| `../../contracts/runtime/ai_receipt.md` | Expected canonical contract home if present; fixtures do not define contracts. |
| `../../schemas/contracts/v1/runtime/ai_receipt.schema.json` | Expected machine-shape home if present; fixtures do not define schemas. |
| `../../policy/runtime/ai_receipts.rego` | Expected runtime receipt policy home if present; fixtures do not decide policy. |
| `../../tools/validators/ai/` | Expected validator home if present; fixtures do not implement validators. |
| `../../data/receipts/ai/` | Proposed actual AIReceipt persistence home; fixtures do not store sealed receipts. |
| `../../data/proofs/` | Proof home; fixtures do not create proof authority. |
| `../../release/signatures/` | Signature home if present; fixtures do not create signing authority. |
| `../../release/manifests/` | Release home; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.invalid.json`, `*.negative.json`, `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy generated-receipt examples with missing required fields, bad field types, invalid outcome enums, outcome/reason mismatch, missing evidence refs, missing citation validation, stale policy bundle hash, unapproved model ID, replay drift, duplicate receipt ID, bad digest form, bad schema URI, missing domain constraints, or missing outcome-specific refs;
- toy receipt-family-collapse examples where one receipt family is confused with another;
- toy public-projection failures where a raw receipt is exposed instead of a bounded receipt summary;
- paired expected fail-closed outputs when behavior becomes stable.

## Exclusions

Do not use this lane for actual receipts, signed envelopes, EvidenceBundles, SourceDescriptors, CitationValidationReports, PolicyDecisions, PromotionDecisions, ReleaseManifests, proof packs, lifecycle data, source exports, implementation code, public API material, public map material, public tiles, direct runtime output, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy refs, toy digests, toy timestamps, toy model IDs, toy policy refs, toy evidence refs, toy citation refs, toy output refs, toy error refs, and toy signature refs.
- Make the invalid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `DENY`, `ERROR`, validation failure, policy failure, replay failure, blocked persistence, blocked projection, release-readiness failure, or expected output.
- Pair each stable invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, outcome validity, reason-code validity, evidence state, citation state, policy state, replay state, signature state, persistence state, public-projection state, release state, correction state, rollback state, and expected-output state separate.
- Do not treat fixture failure as receipt storage proof, proof authority, policy approval, validator implementation proof, API implementation proof, release state, public-map authority, public-summary authority, or published output.

## Expected invalid fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Missing outcome or invalid outcome enum | Schema failure or `ERROR` | Receipt outcomes are finite. |
| `ANSWER` without evidence refs or passing citation validation | Policy failure or `DENY` | Cite-or-abstain remains visible. |
| Unapproved model ID | `DENY` or `ERROR` | Model allowlist must be enforced. |
| Stale policy bundle hash | `ERROR` | Replay drift must not silently publish. |
| Receipt-family collapse | Validation failure or review-required | Receipt families must not collapse. |
| Raw receipt exposed as public surface | Blocked projection | Public surfaces use summaries, not raw receipts. |

## Maintenance notes

- Update this README when generated-receipt child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the exact schema check, policy check, replay check, governed-API test, public-projection check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- If expected invalid behavior stabilizes, update the paired input, expected output, consumer notes, parent README, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual receipts, proof material, release material, source exports, or lifecycle data, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Parent generated-receipt README: fetched and found blank during this update.
- Fixture payload inventory: no payload files verified under this invalid lane during this update.
- Generated-receipt child inventory: NOT VERIFIED during this update.
- AI receipt doctrine alignment: PARTIALLY VERIFIED against `docs/architecture/governed-ai/AI_RECEIPTS.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Contract/schema/policy alignment: NEEDS VERIFICATION against live `contracts/runtime/`, `schemas/contracts/v1/runtime/`, and `policy/runtime/` files.
- Consumer alignment: NEEDS VERIFICATION against validators, policy checks, replay checks, signing checks, persistence checks, public-projection checks, governed-API tests, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, and CI implementation.
- Tests and validators: NOT RUN.
