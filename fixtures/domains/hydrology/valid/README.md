# Hydrology valid fixtures

`fixtures/domains/hydrology/valid/`

Status: draft / valid fixture parent index / Hydrology positive-path examples.

This directory is the broad parent lane for small synthetic Hydrology valid fixture examples. Use it to index and stage Hydrology positive-path cases that are intended to pass bounded shape, semantic, evidence, citation, source-role, rights, sensitivity, receipt, policy, release-readiness, drawer, Focus Mode, layer resolver, export, renderer, or governed-API checks.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, Hydrology truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Valid fixture posture

Use this lane for synthetic inputs that should produce a normal bounded positive posture, usually validation pass, review-ready, evidence-resolved, citation-ready, provenance-resolved, public-safe-context, or a governed `ANSWER` when consumed by a decision envelope. Valid Hydrology fixtures must still preserve KFM trust boundaries: evidence support remains separate from source admission, receipts remain separate from evidence closure, policy remains separate from proof, release remains separate from fixtures, and generated language remains downstream of evidence.

A valid fixture is not implementation proof. It does not prove validator behavior, governed API route behavior, UI behavior, policy enforcement, schema enforcement, EvidenceBundle storage, RunReceipt storage, source admission, release integration, or CI coverage. It only provides reviewable synthetic material for future checks.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hydrology fixture README is still a greenfield stub during this update.

## Current valid fixture families

The following Hydrology fixture lanes currently carry more specific valid or positive-path README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, source-registry records, or CI coverage exist.

| Child or sibling lane | Valid case family | Expected posture |
|---|---|---|
| `../decision_envelope/valid/` | Valid Hydrology runtime envelopes and bounded finite outcomes. | `ANSWER`, or valid `ABSTAIN` / `DENY` / `ERROR` when the finite outcome is correct. |
| `../evidence_bundle/valid/` | Valid Hydrology EvidenceBundle claim-support examples. | Validation pass, review-ready, evidence-resolved, citation-ready, or decision-envelope `ANSWER` when consumed. |
| `../run_receipt/valid/` | Valid Hydrology governed-run provenance examples. | Validation pass, review-ready, provenance-resolved, replay-reviewable, or downstream governed-surface use. |
| `../sources/` | Synthetic source-reference and source-role examples, including valid and invalid source fixture families. | Validation pass, review-ready, source-role-preserved, or fail-closed where appropriate. |
| `../golden/` | Expected outputs for stable valid inputs. | Deterministic expected positive or valid finite output, once paired with an input fixture. |

Future child lanes under this `valid/` parent may be added when broader Hydrology positive-path families are stable enough to deserve their own directory, such as drawer, Focus Mode, layer manifest, feature resolver, HUC/WBD, reach identity, gauge observation, water-quality observation, groundwater observation, regulatory context, modeled hydrograph, map UI, release-readiness, correction, or rollback examples.

## Relationship to sibling fixture lanes

| Sibling lane | Relationship |
|---|---|
| `../decision_envelope/` | Runtime envelope fixture family; valid envelope cases currently live under its `valid/` child. |
| `../evidence_bundle/` | Evidence-support fixture family; valid bundle cases currently live under its `valid/` child. |
| `../run_receipt/` | Governed-run receipt fixture family; valid receipt cases currently live under its `valid/` child. |
| `../sources/` | Source-like and source-role fixture family; may contain valid source posture examples. |
| `../negative/` | Draft negative cases that are not yet sorted into stable invalid families. |
| `../invalid/` | Stable fail-closed cases with known defect families. |
| `../golden/` | Stable expected positive outputs should be paired there. |
| `../README.md` | Parent Hydrology fixture lane; still a greenfield stub during this update. |

## When to use this lane vs specific valid children

| Use case | Preferred lane | Reason |
|---|---|---|
| Valid runtime decision envelope | `../decision_envelope/valid/` | The object family is already known and specific. |
| Valid claim-scope evidence support | `../evidence_bundle/valid/` | Evidence support belongs to the EvidenceBundle fixture family. |
| Valid governed-run provenance | `../run_receipt/valid/` | Run provenance belongs to the RunReceipt fixture family. |
| Valid source-role or descriptor-like toy input | `../sources/` | Source-like examples need source-registry/source-role boundaries. |
| Stable expected output for a valid input | `../golden/` | Golden files anchor deterministic expectations. |
| Broad positive scenario not yet sorted | `./` | This parent can stage or document the family without creating premature taxonomy. |
| Real source material appears in a fixture | Neither | Move it out of fixtures and route through the governed lifecycle or registry/quarantine path. |

## Related references

- `../decision_envelope/README.md`
- `../decision_envelope/valid/README.md`
- `../decision_envelope/invalid/README.md`
- `../evidence_bundle/README.md`
- `../evidence_bundle/valid/README.md`
- `../evidence_bundle/invalid/README.md`
- `../run_receipt/README.md`
- `../run_receipt/valid/README.md`
- `../run_receipt/invalid/README.md`
- `../sources/README.md`
- `../negative/README.md`
- `../invalid/README.md`
- `../golden/README.md`
- `../README.md`
- `../../README.md`
- `../../../README.md`
- `../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/domains/hydrology/SOURCE_REGISTRY.md`
- `../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`
- `../../../../contracts/domains/hydrology/decision_envelope.md`
- `../../../../contracts/domains/hydrology/evidence_bundle.md`
- `../../../../contracts/domains/hydrology/run_receipt.md`
- `../../../../contracts/runtime/decision_envelope.md`
- `../../../../contracts/evidence/evidence_bundle.md`
- `../../../../contracts/runtime/run_receipt.md`
- `../../../../schemas/contracts/v1/domains/hydrology/`
- `../../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`
- `../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`
- `../../../../schemas/contracts/v1/runtime/run_receipt.schema.json`
- `../../../../schemas/contracts/v1/source/`
- `../../../../policy/domains/hydrology/`
- `../../../../policy/sensitivity/hydrology/`
- `../../../../data/registry/sources/hydrology/`
- `../../../../data/proofs/hydrology/`
- `../../../../release/candidates/hydrology/`
- `../../../../release/manifests/hydrology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- draft valid examples for decision envelopes, EvidenceBundles, RunReceipts, source-role checks, drawer outputs, Focus Mode outputs, layer resolver outputs, exports, evidence-resolution checks, citation-validation checks, rights/sensitivity checks, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ANSWER`, validation-pass, review-ready, evidence-resolved, citation-ready, rights-visible, sensitivity-visible, source-role-preserved, provenance-resolved, replay-reviewable, public-safe-context, release-ready, correction-visible, rollback-visible, or expected-output examples;
- contrast examples showing the difference between a valid governed envelope/support/receipt/source-like object and an invalid variant;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, source activation decisions, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the valid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: validation pass, review-ready, `ANSWER`, valid `ABSTAIN`, valid `DENY`, valid `ERROR`, evidence-resolved, citation-ready, source-role-preserved, provenance-resolved, release-ready, or expected output.
- Pair each stable valid input with an expected output in `../golden/` when practical.
- Move stable family-specific cases to a specific valid child lane when the object family becomes clear.
- Keep schema validity, semantic validity, source admission, source role, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, temporal validity, receipt provenance, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture success as source admission, SourceDescriptor authority, EvidenceBundle closure, RunReceipt storage proof, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected valid fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Released, evidence-backed Hydrology runtime answer | `../decision_envelope/valid/` | `ANSWER`. |
| Valid finite no-answer envelope for a structurally valid request | `../decision_envelope/valid/` | `ABSTAIN`, `DENY`, or `ERROR` by design. |
| Complete claim-scope EvidenceBundle fixture | `../evidence_bundle/valid/` | Validation pass, review-ready, evidence-resolved, or citation-ready. |
| Complete governed-run receipt fixture | `../run_receipt/valid/` | Validation pass, review-ready, provenance-resolved, or replay-reviewable. |
| Source-like toy input with explicit role, rights, sensitivity, cadence, and source-head posture | `../sources/` | Validation pass or review-ready. |
| Broad positive scenario not yet sorted | `./` | Review-ready staging until object family is clear. |
| Stable positive output is ready to compare | `../golden/` | Deterministic expected output. |

## Maintenance notes

- Update this README when new valid child lanes, valid payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each valid fixture to the exact check and consumer that uses it.
- If expected valid behavior stabilizes, update the paired input, expected output, consumer notes, child README, `../golden/README.md`, and this index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, a real SourceDescriptor, an actual EvidenceBundle, or an actual RunReceipt, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Decision-envelope valid alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/valid/README.md`.
- EvidenceBundle valid alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/evidence_bundle/valid/README.md`.
- RunReceipt valid alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/run_receipt/valid/README.md`.
- Source fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/sources/README.md`.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/golden/README.md`.
- Negative and invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/negative/README.md` and `fixtures/domains/hydrology/invalid/README.md` from prior updates.
- Parent Hydrology fixture README: present but still a greenfield stub during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, valid-fixture checks, golden-file checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, run-receipt checks, source-descriptor checks, source-role checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, source-head checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
