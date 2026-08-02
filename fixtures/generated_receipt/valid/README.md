# Generated receipt valid fixtures

`fixtures/generated_receipt/valid/`

Status: repository-grounded / executable positive fixture lane.

This directory contains small synthetic `GENERATED_RECEIPT` candidates that should pass the bounded repository-authoring provenance validator.

These files are examples only. They are not actual receipts, EvidenceBundles, SourceDescriptors, policy decisions, promotion decisions, release manifests, proof packs, signed envelopes, public API material, public map material, public tiles, release state, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Valid fixture posture

Generated-receipt valid fixtures demonstrate complete schema shape, exact artifact-map parity, canonical repository-relative paths, and matching local SHA-256 bytes.

`GENERATED_RECEIPT` records AI-assisted repository-artifact provenance. It is separate from runtime `AIReceipt`. A valid fixture does not prove factual truth, evidence closure, policy permission, human review, merge approval, release state, or publication.

The current `minimal.json` binds `../artifacts/minimal.txt` through SHA-256 and keeps human review pending. Its success proves only the validator behaviors exercised by the fixture and focused tests.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, governed-AI runtime root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to receipt governance

| Lane or document | Relationship |
|---|---|
| `../../../schemas/contracts/v1/receipts/generated_receipt.schema.json` | Machine shape for `GENERATED_RECEIPT`. |
| `../../../docs/doctrine/ai-build-operating-contract.md` | Repository-authoring receipt and integrity requirements. |
| `../invalid/README.md` | Sibling fail-closed lane for generated-receipt cases that must be rejected or blocked. |
| `../README.md` | Parent generated-receipt fixture root and family boundary. |
| `../../../tools/validators/validate_generated_receipt.py` | Bounded no-network fixture consumer. |
| `../../../tests/validators/test_validate_generated_receipt.py` | Focused validator proof. |
| `../../../data/receipts/generated/` | Actual provenance process-memory lane; fixtures are never emitted records. |
| `../../../data/proofs/` | Proof home; valid generated-receipt fixtures do not create proof authority. |
| `../../../release/signatures/` | Signature home if present; fixtures do not create signing authority. |
| `../../../release/manifests/` | Release home; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.valid.json`, `*.positive.json`, `*.input.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy generated-receipt examples with complete required fields, exact path/hash/truth-label maps, canonical paths, digest fields, validation-gate records, and truthful review state;
- small synthetic artifacts whose bytes can be recomputed locally;
- toy correction or supersession examples that preserve append-only receipt posture;
- paired expected positive outputs when behavior becomes stable.

## Exclusions

Do not use this lane for actual receipts, signed envelopes, EvidenceBundles, SourceDescriptors, CitationValidationReports, PolicyDecisions, PromotionDecisions, ReleaseManifests, proof packs, lifecycle data, source exports, implementation code, public API material, public map material, public tiles, direct runtime output, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy digests, toy timestamps, model identities, policy refs, evidence refs, citations, and reviewer IDs.
- Make the valid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected validator outcome, review state, and declared-review-claim posture explicit.
- Pair each stable valid input with an expected positive output when practical.
- Keep schema validity, semantic validity, outcome validity, reason-code validity, evidence state, citation state, policy state, replay state, signature state, persistence state, public-projection state, release state, correction state, rollback state, and expected-output state separate.
- Do not treat fixture success as receipt storage proof, proof authority, policy approval, validator implementation proof, API implementation proof, release state, public-map authority, public-summary authority, or published output.

## Expected valid fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Pending review with matching local SHA-256 | Validation pass, non-mergeable | Current `minimal.json` case. |
| Approved-review declaration | Validation and optional review-claim-gate pass | Covered by focused synthetic tests; reviewer authority is not authenticated. |
| Schema-valid override declaration | Validation and optional review-claim-gate pass | Covered by focused synthetic tests; approver authority, scope, expiry, policy, and merge authority remain separate. |
| Multiple canonical artifacts | Validation pass | Future fixture when a stable need exists. |

## Maintenance notes

- Update this README when generated-receipt child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each valid fixture to the exact validator/test behavior it exercises.
- If expected valid behavior stabilizes, update the paired input, expected output, consumer notes, parent README, sibling invalid README, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual receipts, proof material, release material, source exports, or lifecycle data, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Direct payload: `minimal.json` plus `../artifacts/minimal.txt`.
- Schema family: `schemas/contracts/v1/receipts/generated_receipt.schema.json`; runtime `AIReceipt` remains separate.
- Consumer: `tools/validators/validate_generated_receipt.py` in default integrity mode and `--fixtures` mode.
- Focused proof: `tests/validators/test_validate_generated_receipt.py` and `validator-suite` workflow wiring.
- Boundary: policy evaluation, evidence/citation resolution, approval, merge, persistence, release, and publication remain outside fixture success.
