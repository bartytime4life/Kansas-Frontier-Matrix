# Hydrology run-receipt fixtures

`fixtures/domains/hydrology/run_receipt/`

Status: draft / fixture parent index / Hydrology RunReceipt examples.

This directory is the parent lane for small synthetic Hydrology `run_receipt` fixture examples. These fixtures are used to exercise governed-run provenance for Hydrology source intake, no-network fixture processing, HUC/watershed processing, reach identity validation, gauge observation transforms, regulatory-context processing, hydrograph generation, EvidenceBundle proof steps, LayerManifest proof steps, Focus Mode proof steps, release dry runs, rollback drills, correction workflows, and downstream decision-envelope consumption.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, actual RunReceipts, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## RunReceipt posture

The Hydrology run-receipt contract defines a domain-lane alias of the shared runtime `RunReceipt` shape. It records that a Hydrology operation ran with declared inputs, outputs, code reference, source descriptor references, validation references, deterministic hash, and finite outcome.

A Hydrology `run_receipt` does not make an output true, safe, publishable, rights-cleared, or public. It proves a governed run record exists. Evidence closure, policy decisions, validation results, release manifests, rollback targets, and source-role discipline still decide whether a claim can move forward.

The current Hydrology schema aliases the common runtime schema with `allOf/$ref` and does not add Hydrology-specific top-level fields. The current common runtime schema requires `run_id`, `stage`, `inputs`, `outputs`, `code_ref`, `spec_hash`, `source_descriptor_refs`, `validation_refs`, and `outcome`; the finite outcome enum is `SUCCESS`, `PARTIAL`, or `FAIL`; the current runtime `spec_hash` pattern is `sha256:<64 hex>`. Broader `RunReceipt` standard alignment remains conflicted / needs verification.

This fixture parent can support future validation and governed-run checks, but examples here do not prove validator implementation, receipt storage, route behavior, policy enforcement, schema enforcement, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, receipt storage, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `valid/` | Positive-path Hydrology RunReceipt examples with complete required runtime fields and finite outcomes. | Validation pass, review-ready, provenance-resolved, replay-reviewable, or downstream governed-surface use. |
| `invalid/` | Fail-closed Hydrology RunReceipt examples with missing, malformed, unresolved, mismatched, or semantically insufficient run provenance. | Validation failure, review-required, `ABSTAIN`, `DENY`, `ERROR`, blocked render, release-readiness failure, or rollback-readiness failure. |

## Relationship between fixture lanes

| Lane | Use |
|---|---|
| `valid/` | Synthetic RunReceipt examples intended to pass bounded shape and semantic checks. |
| `invalid/` | Synthetic RunReceipt examples intended to fail closed without supporting promotion, release, rollback, or public output. |
| `../negative/` | Draft negative Hydrology scenarios may move into `invalid/` when the run-receipt defect family stabilizes. |
| `../invalid/` | Broader Hydrology invalid index; this lane supplies the run-receipt-specific family. |
| `../golden/` | Stable expected outputs for valid and invalid run-receipt fixtures may be paired there. |
| `../decision_envelope/` | Runtime envelopes may consume valid or invalid run provenance and return finite outcomes. |
| `../evidence_bundle/` | Evidence support may reference valid run provenance or fail when run provenance is missing. |
| Parent Hydrology fixture lane | Broader Hydrology fixture family; not inspected during this update. |

## Related references

- `valid/README.md`
- `invalid/README.md`
- `../negative/README.md`
- `../invalid/README.md`
- `../golden/README.md`
- `../decision_envelope/README.md`
- `../decision_envelope/valid/README.md`
- `../decision_envelope/invalid/README.md`
- `../evidence_bundle/README.md`
- `../evidence_bundle/valid/README.md`
- `../evidence_bundle/invalid/README.md`
- `../README.md`
- `../../../README.md`
- `../../../../contracts/domains/hydrology/run_receipt.md`
- `../../../../contracts/runtime/run_receipt.md`
- `../../../../docs/standards/RUN_RECEIPT.md`
- `../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../schemas/contracts/v1/domains/hydrology/run_receipt.schema.json`
- `../../../../schemas/contracts/v1/runtime/run_receipt.schema.json`
- `../../../../policy/domains/hydrology/`
- `../../../../data/registry/sources/hydrology/`
- `../../../../data/proofs/hydrology/`
- `../../../../release/candidates/hydrology/`
- `../../../../release/manifests/hydrology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Hydrology RunReceipt payloads with `run_id`, `stage`, `inputs`, `outputs`, `code_ref`, `spec_hash`, `source_descriptor_refs`, `validation_refs`, and `outcome` examples;
- toy examples for source intake, no-network fixture processing, HUC/watershed processing, reach identity validation, gauge observation transform, regulatory-context processing, hydrograph generation, EvidenceBundle proof steps, LayerManifest proof steps, Focus Mode proof steps, release dry runs, rollback drills, and correction workflows;
- toy failure examples for missing required fields, malformed `spec_hash`, unsupported outcome, unresolved source descriptor refs, missing validation refs, source-role drift, input/output mismatch, schema/standard drift, undeclared Hydrology-only fields, proof-vs-truth confusion, proof-vs-release confusion, and proof-vs-rollback confusion;
- contrast examples showing the difference between a valid governed-run receipt and an invalid variant;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual RunReceipts, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy run IDs, toy stages, toy input refs, toy output refs, toy code refs, toy source descriptor refs, toy validation refs, toy spec hashes, toy timestamps, toy digests, and toy outcomes.
- Make the receipt posture explicit: valid, invalid, complete required fields, missing required field, stable run identity, unclear run identity, clear stage, missing stage, input/output closure, input/output mismatch, code-ref present, code-ref missing, `sha256:<64 hex>` spec hash, malformed spec hash, source descriptor refs present, validation refs present, finite outcome, unsupported outcome, source-role preserved, source-role drift, replay-reviewable, or expected output.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, source descriptor resolution, validation ref resolution, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, transform lineage, checksum integrity, policy filtering, release posture, trust-membrane safety, decision-envelope outcome, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level RunReceipt fields as implemented unless the schema is extended; the current contract says Hydrology adds meaning through the alias contract, companion refs, validation refs, EvidenceBundles, PolicyDecisions, ReleaseManifests, or later schema revisions.
- Do not treat fixture success or failure as receipt storage proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Preferred child lane | Expected posture |
|---|---|---|
| Complete toy source-intake or fixture-admission receipt | `valid/` | Validation pass or review-ready. |
| Complete toy transform, validation, release dry-run, rollback drill, or correction receipt | `valid/` | Validation pass, review-ready, or replay-reviewable. |
| Missing required runtime field | `invalid/` | Validation failure. |
| Malformed `spec_hash` or unsupported outcome | `invalid/` | Validation failure. |
| Source descriptor refs or validation refs cannot be resolved | `invalid/` | Review-required, `ABSTAIN`, `DENY`, or validation failure when consumed. |
| Receipt is treated as truth, policy, release, or rollback authority | `invalid/` | `DENY` or readiness failure. |
| Stable expected output is ready to compare | `../golden/` | Deterministic expected output. |

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or run-receipt consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior changes, update the paired input, expected output, consumer notes, child README, `../golden/README.md`, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated `valid/README.md` and `invalid/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Valid fixture alignment: PARTIALLY VERIFIED against `valid/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `invalid/README.md`.
- Hydrology RunReceipt contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/run_receipt.md`.
- RunReceipt standard alignment: PARTIALLY VERIFIED against `docs/standards/RUN_RECEIPT.md`; standard/schema drift remains documented as conflicted / needs verification.
- Hydrology invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/invalid/README.md`.
- Hydrology negative fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/negative/README.md`.
- Hydrology golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/golden/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Parent Hydrology fixture alignment: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, run-receipt checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, source-descriptor checks, validation-ref checks, spec-hash checks, source-role checks, trust-membrane checks, release-readiness checks, rollback-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
