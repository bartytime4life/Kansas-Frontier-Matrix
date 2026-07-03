# Generated receipt valid fixtures

`fixtures/generated_receipt/valid/`

Status: draft / valid fixture lane / generated-receipt positive-path examples.

This directory is for small synthetic valid generated-receipt examples. Use it for toy receipt cases that should pass schema validation, policy validation, replay checks, receipt-family checks, citation-closure checks, integrity checks, persistence checks, public-projection checks, or release-readiness checks when paired with the appropriate validator and expected output.

These files are examples only. They are not actual receipts, EvidenceBundles, SourceDescriptors, policy decisions, promotion decisions, release manifests, proof packs, signed envelopes, public API material, public map material, public tiles, release state, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Valid fixture posture

Generated-receipt valid fixtures exist to demonstrate the positive path for bounded receipt objects. They may show complete toy receipt shapes, finite outcomes, evidence refs, citation refs, policy refs, replay refs, integrity refs, signature refs, persistence refs, public-summary refs, correction refs, rollback refs, and expected outputs.

KFM receipt doctrine treats an AIReceipt as a runtime accountability record, not the answer and not a substitute for EvidenceBundle. A valid generated-receipt fixture may show that a toy receipt is complete and admissible, but it does not make the answer true, does not close evidence, does not approve policy, does not publish release state, and does not prove runtime implementation.

A fixture can describe a desired valid case before validators, policies, schema checks, replay checks, signing checks, persistence checks, public-projection checks, release integration, or CI coverage exist. Fixture success is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, governed-AI runtime root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to receipt governance

| Lane or document | Relationship |
|---|---|
| `../../docs/architecture/governed-ai/AI_RECEIPTS.md` | Governs AIReceipt meaning, finite outcomes, lifecycle, validator expectations, receipt-family boundaries, and replay posture. |
| `../invalid/README.md` | Sibling fail-closed lane for generated-receipt cases that must be rejected or blocked. |
| `../README.md` | Parent generated-receipt fixture root; currently blank at the time this valid README is authored. |
| `../../contracts/runtime/ai_receipt.md` | Expected canonical contract home if present; fixtures do not define contracts. |
| `../../schemas/contracts/v1/runtime/ai_receipt.schema.json` | Expected machine-shape home if present; fixtures do not define schemas. |
| `../../policy/runtime/ai_receipts.rego` | Expected runtime receipt policy home if present; fixtures do not decide policy. |
| `../../tools/validators/ai/` | Expected validator home if present; fixtures do not implement validators. |
| `../../data/receipts/ai/` | Proposed actual AIReceipt persistence home; fixtures do not store sealed receipts. |
| `../../data/proofs/` | Proof home; valid generated-receipt fixtures do not create proof authority. |
| `../../release/signatures/` | Signature home if present; fixtures do not create signing authority. |
| `../../release/manifests/` | Release home; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.valid.json`, `*.positive.json`, `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy generated-receipt examples with complete required fields, valid finite outcomes, valid reason codes, evidence refs where required, citation-validation refs where required, policy refs, policy bundle hashes, replay keys, model identity refs, output refs, error refs, denial refs, abstention refs, digest fields, schema URI refs, domain constraints, signature refs, or public-summary refs;
- toy examples for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` outcomes when each outcome is complete and policy-admissible for its role;
- toy public-projection examples where a bounded summary is exposed instead of a raw receipt object;
- toy correction or supersession examples that preserve append-only receipt posture;
- paired expected positive outputs when behavior becomes stable.

## Exclusions

Do not use this lane for actual receipts, signed envelopes, EvidenceBundles, SourceDescriptors, CitationValidationReports, PolicyDecisions, PromotionDecisions, ReleaseManifests, proof packs, lifecycle data, source exports, implementation code, public API material, public map material, public tiles, direct runtime output, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy refs, toy digests, toy timestamps, toy model IDs, toy policy refs, toy evidence refs, toy citation refs, toy output refs, toy error refs, and toy signature refs.
- Make the valid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: validation pass, policy pass, replay pass, persistence pass, projection pass, release-ready, `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or expected output.
- Pair each stable valid input with an expected positive output when practical.
- Keep schema validity, semantic validity, outcome validity, reason-code validity, evidence state, citation state, policy state, replay state, signature state, persistence state, public-projection state, release state, correction state, rollback state, and expected-output state separate.
- Do not treat fixture success as receipt storage proof, proof authority, policy approval, validator implementation proof, API implementation proof, release state, public-map authority, public-summary authority, or published output.

## Expected valid fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Minimal complete `ABSTAIN` receipt | Validation pass or policy pass | Evidence may be absent when abstention reason is present. |
| Minimal complete `DENY` receipt | Validation pass or policy pass | Denial reason and policy refs remain visible. |
| Minimal complete `ERROR` receipt | Validation pass or policy pass | Error refs remain structured. |
| Complete `ANSWER` receipt with evidence and citation refs | Validation pass, policy pass, or replay-ready | `ANSWER` remains evidence-subordinate. |
| Deterministic replay example | Replay pass or expected output | Digest identity must remain stable for the toy case. |
| Public receipt summary projection | Projection pass | Summary is bounded and not raw receipt authority. |
| Correction or supersession example | Review-ready | Old receipt posture remains append-only. |
| Stable valid output is ready to compare | Expected output | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when generated-receipt child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each valid fixture to the exact schema check, policy check, replay check, governed-API test, public-projection check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- If expected valid behavior stabilizes, update the paired input, expected output, consumer notes, parent README, sibling invalid README, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual receipts, proof material, release material, source exports, or lifecycle data, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Parent generated-receipt README: fetched and found blank during the recent sibling invalid update.
- Fixture payload inventory: no payload files verified under this valid lane during this update.
- Generated-receipt child inventory: NOT VERIFIED during this update.
- Invalid generated-receipt alignment: PARTIALLY VERIFIED against `fixtures/generated_receipt/invalid/README.md`.
- AI receipt doctrine alignment: PARTIALLY VERIFIED against `docs/architecture/governed-ai/AI_RECEIPTS.md` from recent preceding updates.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md` from recent preceding updates.
- Contract/schema/policy alignment: NEEDS VERIFICATION against live `contracts/runtime/`, `schemas/contracts/v1/runtime/`, and `policy/runtime/` files.
- Consumer alignment: NEEDS VERIFICATION against validators, policy checks, replay checks, signing checks, persistence checks, public-projection checks, governed-API tests, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, and CI implementation.
- Tests and validators: NOT RUN.
