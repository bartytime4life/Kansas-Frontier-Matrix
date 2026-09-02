# Hydrology run-receipt invalid fixtures

`fixtures/domains/hydrology/run_receipt/invalid/`

Status: draft / invalid fixture lane / Hydrology RunReceipt negative-path examples.

This directory is for small synthetic Hydrology `run_receipt` fixtures that should fail validation, review, promotion-readiness, rollback-readiness, release-readiness, or governed API use. These examples are meant to exercise fail-closed behavior for missing required fields, malformed spec hashes, undeclared Hydrology-only fields, unresolved source descriptor refs, missing validation refs, input/output mismatch, source-role drift, ambiguous outcomes, proof-vs-truth confusion, proof-vs-release confusion, and schema/standard drift.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, actual RunReceipts, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## Invalid fixture posture

The Hydrology run-receipt contract defines a domain-lane alias of the shared runtime `RunReceipt` shape. It records that a Hydrology operation ran with declared inputs, outputs, code reference, source descriptor references, validation references, deterministic hash, and finite outcome.

A Hydrology `run_receipt` does not make an output true, safe, publishable, rights-cleared, or public. It proves a governed run record exists. Evidence closure, policy decisions, validation results, release manifests, rollback targets, and source-role discipline still decide whether a claim can move forward.

The current common runtime schema requires `run_id`, `stage`, `inputs`, `outputs`, `code_ref`, `spec_hash`, `source_descriptor_refs`, `validation_refs`, and `outcome`. The current outcome enum is `SUCCESS`, `PARTIAL`, or `FAIL`, and `spec_hash` follows `sha256:<64 hex>` in the current runtime schema. Broader `RunReceipt` standard alignment remains conflicted / needs verification.

Invalid fixtures in this lane should make one or more of those requirements absent, malformed, unresolved, mismatched, or semantically insufficient. They should also test that a run receipt is not treated as evidence closure, source truth, policy approval, release approval, rollback approval, public-map authority, or generated explanation.

This lane can support future validation and governed-run checks, but examples here do not prove validator implementation, receipt storage, route behavior, policy enforcement, schema enforcement, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent `fixtures/domains/hydrology/run_receipt/README.md` was not inspected during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../` | Parent Hydrology run-receipt fixture lane; not inspected during this update. |
| `../../invalid/` | Broader Hydrology invalid fixture index; this lane supplies a specific invalid family. |
| `../../negative/` | Draft negative scenarios may move here when run-receipt defects stabilize. |
| `../../golden/` | Stable expected invalid outputs may be paired there. |
| `../../decision_envelope/invalid/` | Invalid decision-envelope cases may consume run-receipt failures as `DENY`, `ABSTAIN`, or `ERROR` scenarios. |
| `../../evidence_bundle/invalid/` | Invalid EvidenceBundle cases may depend on missing or mismatched run provenance. |
| `../../` | Parent Hydrology fixture lane; not inspected during this update. |
| `../../../../README.md` | Root fixture rules; this lane follows the synthetic/public-safe fixture boundary. |
| `../../../../../contracts/domains/hydrology/run_receipt.md` | Hydrology RunReceipt semantic contract; this lane supplies examples only. |
| `../../../../../docs/standards/RUN_RECEIPT.md` | Broader RunReceipt standard; current schema alignment is conflicted / needs verification. |
| `../../../../../policy/domains/hydrology/` | Policy home; fixtures do not decide policy. |
| `../../../../../release/candidates/hydrology/` | Candidate release home; fixtures do not approve release. |
| `../../../../../release/manifests/hydrology/` | Release-manifest home if present; fixtures do not publish. |

## Related references

- `../README.md`
- `../../invalid/README.md`
- `../../negative/README.md`
- `../../golden/README.md`
- `../../decision_envelope/invalid/README.md`
- `../../decision_envelope/README.md`
- `../../evidence_bundle/invalid/README.md`
- `../../evidence_bundle/README.md`
- `../../README.md`
- `../../../../README.md`
- `../../../../../contracts/domains/hydrology/run_receipt.md`
- `../../../../../contracts/runtime/run_receipt.md`
- `../../../../../docs/standards/RUN_RECEIPT.md`
- `../../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../../schemas/contracts/v1/domains/hydrology/run_receipt.schema.json`
- `../../../../../schemas/contracts/v1/runtime/run_receipt.schema.json`
- `../../../../../policy/domains/hydrology/`
- `../../../../../data/registry/sources/hydrology/`
- `../../../../../data/proofs/hydrology/`
- `../../../../../release/candidates/hydrology/`
- `../../../../../release/manifests/hydrology/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy invalid Hydrology RunReceipt payloads with absent, malformed, unresolved, mismatched, or semantically insufficient required fields;
- toy examples for missing `run_id`, missing `stage`, empty `inputs`, empty `outputs`, missing `code_ref`, malformed `spec_hash`, unresolved `source_descriptor_refs`, missing `validation_refs`, unsupported `outcome`, undeclared Hydrology-only fields, input/output mismatch, source-role drift, or receipt treated as release approval;
- toy expected outputs such as validation failure, review-required, `ABSTAIN`, `DENY`, or `ERROR` when consumed by a decision envelope, evidence bundle, release-readiness check, rollback check, drawer, Focus Mode surface, or governed API dry-run;
- contrast examples paired with future valid examples when useful.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual RunReceipts, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy run IDs, toy stages, toy input refs, toy output refs, toy code refs, toy source descriptor refs, toy validation refs, toy spec hashes, toy timestamps, toy digests, and toy outcomes.
- Make the defect explicit: missing required field, empty required array, malformed `spec_hash`, unsupported outcome, unresolved source descriptor ref, unresolved validation ref, source-role drift, input/output mismatch, schema/standard drift, undeclared Hydrology-only field, or receipt treated as truth/release authority.
- Make expected outcome explicit: validation failure, review-required, `ABSTAIN`, `DENY`, `ERROR`, blocked render, release-readiness failure, rollback-readiness failure, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, source descriptor resolution, validation ref resolution, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, transform lineage, checksum integrity, policy filtering, release posture, trust-membrane safety, decision-envelope outcome, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level RunReceipt fields as implemented unless the schema is extended; the current contract says Hydrology adds meaning through the alias contract, companion refs, validation refs, EvidenceBundles, PolicyDecisions, ReleaseManifests, or later schema revisions.
- Do not treat fixture failure as receipt storage proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Missing `run_id` | Validation failure | Run identity must be stable and citeable. |
| Missing or unclear `stage` | Validation failure or review-required output | Lifecycle placement must be explicit. |
| Empty `inputs` or `outputs` | Validation failure | Input/output closure is required. |
| Missing `code_ref` | Validation failure | The run cannot be replay-reviewed without code/tool reference. |
| Malformed `spec_hash` | Validation failure | Current runtime schema expects `sha256:<64 hex>`. |
| Missing `source_descriptor_refs` | Validation failure or review-required output | Source role and authority limits must be traceable. |
| Missing `validation_refs` | Validation failure or review-required output | Promotion/denial gates need validation linkage. |
| Unsupported outcome outside `SUCCESS`, `PARTIAL`, or `FAIL` | Validation failure | Outcome must stay finite. |
| Hydrology-only top-level field added without schema support | Validation failure | Alias schema does not currently add domain-specific fields. |
| Receipt treated as release approval | `DENY` or release-readiness failure | Receipt supports review; release still requires release/policy gates. |
| Receipt treated as evidence truth | `ABSTAIN` or validation failure | EvidenceBundle and citation closure still own claim support. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or run-receipt consumer contracts are added.
- Link each invalid fixture to the RunReceipt schema check, Hydrology run-receipt contract check, source-descriptor resolution check, validation-ref check, spec-hash check, source-role check, evidence-bundle check, decision-envelope check, policy-filter check, release-readiness check, rollback-readiness check, correction check, drawer check, Focus Mode check, or governed-API dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, sibling valid/contrast notes, and verification status together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Parent run-receipt fixture README: NEEDS VERIFICATION.
- Hydrology RunReceipt contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/run_receipt.md`.
- RunReceipt standard alignment: PARTIALLY VERIFIED against `docs/standards/RUN_RECEIPT.md`; standard/schema drift remains documented as conflicted / needs verification.
- Hydrology invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/invalid/README.md`.
- Hydrology negative fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/negative/README.md`.
- Hydrology golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/golden/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, run-receipt checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, source-descriptor checks, validation-ref checks, spec-hash checks, source-role checks, trust-membrane checks, release-readiness checks, rollback-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
