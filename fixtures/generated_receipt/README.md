# Generated receipt fixtures

`fixtures/generated_receipt/`

Status: repository-grounded / executable synthetic fixture family.

This directory is the parent lane for small synthetic `GENERATED_RECEIPT` fixtures. It exercises repository-artifact provenance shape and local integrity without storing actual receipts.

These files are examples only. They are not actual receipts, EvidenceBundles, SourceDescriptors, policy decisions, promotion decisions, release manifests, proof packs, signed envelopes, public API material, public map material, public tiles, release state, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Fixture parent posture

Generated-receipt fixtures support bounded schema, cross-field, repository-path, and artifact-hash checks. A fixture may imitate a receipt and bind a synthetic local artifact, but it must not be treated as sealed process memory, proof material, review approval, release evidence, or public truth.

`GENERATED_RECEIPT` is the AI-assisted repository-authoring provenance family. It is separate from runtime `AIReceipt`. Valid fixtures demonstrate bounded acceptance; invalid fixtures demonstrate fail-closed rejection. Neither result establishes factual truth, policy permission, human review, merge approval, release, or publication.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, governed-AI runtime root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes and synthetic artifact are consumed by `tools/validators/validate_generated_receipt.py` and its focused tests.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `artifacts/minimal.txt` | Local synthetic artifact used to prove SHA-256 binding. | Fixture input only. |
| `valid/` | Positive `GENERATED_RECEIPT` candidates with complete shape and resolvable SHA-256 bindings. | Validator exit `0`. |
| `invalid/` | One-defect fail-closed candidates. | Validator nonzero for the named defect. |

## Relationship to receipt governance

| Lane or document | Relationship |
|---|---|
| `../README.md` | Root fixture rules; this lane must remain synthetic and non-authoritative. |
| `valid/README.md` | Positive-path sibling lane. |
| `invalid/README.md` | Fail-closed sibling lane. |
| `../../schemas/contracts/v1/receipts/generated_receipt.schema.json` | Machine shape for this fixture family. |
| `../../docs/doctrine/ai-build-operating-contract.md` | Repository-authoring receipt and integrity requirements. |
| `../../policy/ai_builder/operating_contract.rego` | Separate AI-builder policy surface; fixture validation does not replace policy evaluation. |
| `../../tools/validators/validate_generated_receipt.py` | No-network shape, cross-field, path, SHA-256-prefix, citation-presence, and optional declared-review-claim checker; it authenticates no authority. |
| `../../tests/validators/test_validate_generated_receipt.py` | Focused synthetic behavior and CLI proof. |
| `../../data/receipts/generated/` | Actual generated-work process-memory lane; fixtures never belong there. |
| `../contracts/v1/runtime/ai_receipt/` | Separate runtime `AIReceipt` fixture family. |
| `../../data/proofs/` | Proof home; fixtures do not create proof authority. |
| `../../release/signatures/` | Signature home if present; fixtures do not create signing authority. |
| `../../release/manifests/` | Release home; fixtures do not publish. |

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.positive.json`, `*.negative.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy generated-receipt examples for complete or deliberately incomplete shape, artifact-map parity, local paths, SHA-256 integrity, review posture, and receipt-family separation;
- positive-path examples in `valid/`;
- fail-closed examples in `invalid/`;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for actual receipts, signed envelopes, EvidenceBundles, SourceDescriptors, CitationValidationReports, PolicyDecisions, PromotionDecisions, ReleaseManifests, proof packs, lifecycle data, source exports, implementation code, public API material, public map material, public tiles, direct runtime output, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy refs, toy digests, toy timestamps, toy model IDs, toy policy refs, toy evidence refs, toy citation refs, toy output refs, toy error refs, and toy signature refs.
- Make fixture posture explicit: valid, invalid, schema failure, integrity failure, non-mergeable, or review-required.
- Keep every negative payload focused on one primary defect when practical.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, outcome validity, reason-code validity, evidence state, citation state, policy state, replay state, signature state, persistence state, public-projection state, release state, correction state, rollback state, and expected-output state separate.
- Do not treat fixture success or failure as receipt storage proof, proof authority, policy approval, validator implementation proof, API implementation proof, release state, public-map authority, public-summary authority, or published output.

## Expected fixture families

| Scenario family | Preferred child lane | Expected posture |
|---|---|---|
| Complete pending-review receipt with a matching local SHA-256 | `valid/` | Integrity-valid but not merge-authorizing. |
| Approved-review or override declaration | `valid/` or focused test | Optional review-claim gate passes without authenticating authority. |
| Missing required schema field | `invalid/` | Schema failure. |
| Artifact path/hash/truth-label key mismatch | `invalid/` or focused test | Cross-field failure. |
| Missing, escaping, symlinked, self-referential, or hash-mismatched artifact | `invalid/` or focused test | Integrity failure. |
| BLAKE3 without an admitted implementation dependency | focused test | Fail closed as unsupported. |
| Receipt-family collapse | `invalid/` | Validation failure or review-required. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact validator and focused test that consume it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes actual receipts, proof material, release material, source exports, or lifecycle data, move it out of this lane, quarantine it through the governed lifecycle or security process, and record the correction path.

## Verification status

- Payload inventory: one valid JSON candidate, one one-defect invalid JSON candidate, and one bound synthetic artifact.
- Schema alignment: confirmed against `schemas/contracts/v1/receipts/generated_receipt.schema.json`.
- Consumer alignment: confirmed for the bounded no-network validator, focused `unittest` suite, and `validator-suite` workflow wiring.
- Integrity posture: SHA-256 is implemented; BLAKE3 fails closed until an explicit dependency decision is made.
- Remaining non-scope: policy evaluation, evidence/citation resolution, automatic review-state updates, merge enforcement, persistence, release, and publication remain separate or `NEEDS VERIFICATION`.
