# Hydrology run-receipt valid fixtures

`fixtures/domains/hydrology/run_receipt/valid/`

Status: draft / valid fixture lane / Hydrology RunReceipt positive-path examples.

This directory is for small synthetic Hydrology `run_receipt` fixtures that represent valid bounded governed-run records. These examples are meant to exercise positive-path RunReceipt shapes with declared run identity, lifecycle stage, inputs, outputs, code reference, deterministic spec hash, source descriptor refs, validation refs, and finite outcome.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, actual RunReceipts, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## Valid fixture posture

The Hydrology run-receipt contract defines a domain-lane alias of the shared runtime `RunReceipt` shape. It records that a Hydrology operation ran with declared inputs, outputs, code reference, source descriptor references, validation references, deterministic hash, and finite outcome.

A valid Hydrology run-receipt fixture should satisfy the current common runtime required fields: `run_id`, `stage`, `inputs`, `outputs`, `code_ref`, `spec_hash`, `source_descriptor_refs`, `validation_refs`, and `outcome`. The current outcome enum is `SUCCESS`, `PARTIAL`, or `FAIL`, and the current runtime `spec_hash` pattern is `sha256:<64 hex>`.

A valid receipt still does not make an output true, public, policy-approved, release-approved, or rollback-approved. It proves a governed run record exists and supports later review by EvidenceBundles, decision envelopes, validation reports, policy decisions, release manifests, correction notices, and rollback cards.

Hydrology-specific meaning must remain inside the current alias boundary. Do not add Hydrology-specific top-level RunReceipt fields as implemented unless the schema is extended; use companion refs, validation refs, EvidenceBundles, PolicyDecisions, ReleaseManifests, or later schema revisions for domain-specific meaning.

This lane can support future validation and governed-run checks, but examples here do not prove validator implementation, receipt storage, route behavior, policy enforcement, schema enforcement, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent `fixtures/domains/hydrology/run_receipt/README.md` was not inspected during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../` | Parent Hydrology run-receipt fixture lane; not inspected during this update. |
| `../invalid/` | Sibling fail-closed lane for invalid RunReceipt cases and contrast examples. |
| `../../invalid/` | Broader Hydrology invalid fixture index; this lane supplies valid contrast cases. |
| `../../negative/` | Draft negative scenarios may move to `../invalid/` when run-receipt defects stabilize. |
| `../../golden/` | Stable expected valid outputs may be paired there. |
| `../../decision_envelope/valid/` | Valid decision-envelope examples may reference valid run provenance. |
| `../../evidence_bundle/valid/` | Valid EvidenceBundle examples may reference valid run provenance. |
| `../../` | Parent Hydrology fixture lane; not inspected during this update. |
| `../../../../README.md` | Root fixture rules; this lane follows the synthetic/public-safe fixture boundary. |
| `../../../../../contracts/domains/hydrology/run_receipt.md` | Hydrology RunReceipt semantic contract; this lane supplies examples only. |
| `../../../../../docs/standards/RUN_RECEIPT.md` | Broader RunReceipt standard; current schema alignment is conflicted / needs verification. |
| `../../../../../policy/domains/hydrology/` | Policy home; fixtures do not decide policy. |
| `../../../../../release/candidates/hydrology/` | Candidate release home; fixtures do not approve release. |
| `../../../../../release/manifests/hydrology/` | Release-manifest home if present; fixtures do not publish. |

## Related references

- `../README.md`
- `../invalid/README.md`
- `../../invalid/README.md`
- `../../negative/README.md`
- `../../golden/README.md`
- `../../decision_envelope/valid/README.md`
- `../../decision_envelope/README.md`
- `../../evidence_bundle/valid/README.md`
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

- small synthetic `*.input.json`, `*.valid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy valid Hydrology RunReceipt payloads with complete required runtime fields;
- toy examples for source intake, no-network fixture processing, HUC/watershed processing, reach identity validation, gauge observation transform, regulatory-context processing, hydrograph generation, EvidenceBundle proof steps, LayerManifest proof steps, Focus Mode proof steps, release dry runs, rollback drills, and correction workflows;
- toy `run_id`, `stage`, `inputs`, `outputs`, `code_ref`, `spec_hash`, `source_descriptor_refs`, `validation_refs`, and `outcome` examples;
- toy expected outputs such as validation pass, review-ready, provenance-resolved, replay-reviewable, or decision-envelope `ANSWER` when consumed by a governed surface;
- contrast examples paired with `../invalid/` when useful.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual RunReceipts, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy run IDs, toy stages, toy input refs, toy output refs, toy code refs, toy source descriptor refs, toy validation refs, toy spec hashes, toy timestamps, toy digests, and toy outcomes.
- Make the valid condition explicit: complete required fields, stable run identity, clear stage, input/output closure, code ref present, `sha256:<64 hex>` spec hash, source descriptor refs present, validation refs present, finite outcome, source-role preserved, replay-reviewable, or release-review-ready.
- Make expected outcome explicit: validation pass, review-ready, provenance-resolved, replay-reviewable, `SUCCESS`, `PARTIAL`, `FAIL`, expected output, or downstream decision-envelope use.
- Pair each valid input with an expected output when practical.
- Keep schema validity, semantic validity, source descriptor resolution, validation ref resolution, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, transform lineage, checksum integrity, policy filtering, release posture, trust-membrane safety, decision-envelope outcome, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level RunReceipt fields as implemented unless the schema is extended; the current contract says Hydrology adds meaning through the alias contract, companion refs, validation refs, EvidenceBundles, PolicyDecisions, ReleaseManifests, or later schema revisions.
- Do not treat fixture success as receipt storage proof, EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected valid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Complete toy source-intake receipt | Validation pass | Declared inputs, source descriptor refs, validation refs, and outcome are present. |
| Complete toy HUC/watershed processing receipt | Validation pass | Run provenance is inspectable; geometry truth/release remains separate. |
| Complete toy reach identity validation receipt | Validation pass | Ambiguity handling still belongs to validation and decision envelopes. |
| Complete toy gauge observation transform receipt | Validation pass | Receipt records run provenance, not final observation truth. |
| Complete toy regulatory-context processing receipt | Validation pass | Regulatory context remains regulatory context. |
| Complete toy modeled hydrograph generation receipt | Validation pass | Receipt records model/transform execution, not observed truth. |
| Complete toy release dry-run receipt | Review-ready | Release still requires policy and release gates. |
| Complete toy rollback drill receipt | Review-ready | Rollback still requires rollback target and governance. |
| Valid receipt consumed by a decision envelope | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` as governed | Decision envelope owns runtime outcome. |

## Maintenance notes

- Update this README when valid payload files, validators, tests, helper scripts, expected-output names, or run-receipt consumer contracts are added.
- Link each valid fixture to the RunReceipt schema check, Hydrology run-receipt contract check, source-descriptor resolution check, validation-ref check, spec-hash check, source-role check, evidence-bundle check, decision-envelope check, policy-filter check, release-readiness check, rollback-readiness check, correction check, drawer check, Focus Mode check, or governed-API dry-run that consumes it.
- If expected valid behavior changes, update the paired input, expected output, consumer notes, sibling invalid/contrast notes, and verification status together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Parent run-receipt fixture README: NEEDS VERIFICATION.
- Sibling invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/run_receipt/invalid/README.md`.
- Hydrology RunReceipt contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/run_receipt.md`.
- RunReceipt standard alignment: PARTIALLY VERIFIED against `docs/standards/RUN_RECEIPT.md`; standard/schema drift remains documented as conflicted / needs verification.
- Hydrology invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/invalid/README.md`.
- Hydrology negative fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/negative/README.md`.
- Hydrology golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/golden/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, run-receipt checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, source-descriptor checks, validation-ref checks, spec-hash checks, source-role checks, trust-membrane checks, release-readiness checks, rollback-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
