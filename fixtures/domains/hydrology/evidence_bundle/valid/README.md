# Hydrology evidence-bundle valid fixtures

`fixtures/domains/hydrology/evidence_bundle/valid/`

Status: draft / valid fixture lane / Hydrology EvidenceBundle positive-path examples.

This directory is for small synthetic Hydrology `EvidenceBundle` fixtures that represent valid claim-scope evidence support. These examples are meant to exercise positive-path EvidenceBundle shapes with narrow claim scopes, non-empty evidence refs, source-record handles, publication-ready citations, rights posture, sensitivity labels, transforms, checksums, and deterministic spec linkage.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, source descriptors, review approvals, policy decisions, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## Valid fixture posture

The Hydrology EvidenceBundle contract defines the Hydrology alias of KFM's shared `evidence_bundle`: the closure artifact that packages source records, evidence refs, citations, rights, sensitivity, transforms, checksums, and spec linkage for a Hydrology claim scope. EvidenceBundles answer what evidence supports an exact claim scope; they do not decide whether that claim is public-safe or should be rendered.

A valid positive fixture should include the shared required fields: `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, and `spec_hash`. Hydrology-specific meaning should remain in common fields and semantic obligations until the shared schema or domain alias schema is extended.

A valid fixture is not implementation proof. It does not prove validator behavior, EvidenceBundle storage, governed API route behavior, policy enforcement, schema enforcement, release integration, UI rendering, or CI coverage by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent `fixtures/domains/hydrology/evidence_bundle/README.md` is blank during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../` | Parent Hydrology evidence-bundle fixture lane; blank during this update. |
| `../invalid/` | Sibling fail-closed lane for invalid EvidenceBundle cases and contrast examples. |
| `../../decision_envelope/valid/` | Valid decision-envelope fixtures may consume valid evidence support as bounded `ANSWER` examples. |
| `../../decision_envelope/invalid/` | Invalid decision-envelope fixtures may consume missing or invalid evidence support as `ABSTAIN`, `DENY`, or `ERROR` examples. |
| `../../` | Parent Hydrology fixture lane; not inspected during this update. |
| `../../../../README.md` | Root fixture rules; this lane follows the synthetic/public-safe fixture boundary. |
| `../../../../../contracts/domains/hydrology/evidence_bundle.md` | Hydrology EvidenceBundle semantic contract; this lane supplies examples only. |
| `../../../../../data/proofs/hydrology/` | Proof storage home; fixtures do not create proof authority. |
| `../../../../../docs/standards/EVIDENCE_BUNDLE.md` | External-conformance standard; this lane does not redefine object meaning or shape. |
| `../../../../../policy/domains/hydrology/` | Policy home; fixtures do not decide policy. |
| `../../../../../release/candidates/hydrology/` | Candidate release home; fixtures do not approve release. |
| `../../../../../release/manifests/hydrology/` | Release-manifest home if present; fixtures do not publish. |

## Related references

- `../README.md`
- `../invalid/README.md`
- `../../decision_envelope/valid/README.md`
- `../../decision_envelope/invalid/README.md`
- `../../decision_envelope/README.md`
- `../../README.md`
- `../../../../README.md`
- `../../../../../contracts/domains/hydrology/evidence_bundle.md`
- `../../../../../contracts/evidence/evidence_bundle.md`
- `../../../../../docs/standards/EVIDENCE_BUNDLE.md`
- `../../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../../schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json`
- `../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`
- `../../../../../policy/domains/hydrology/`
- `../../../../../data/registry/sources/hydrology/`
- `../../../../../data/proofs/hydrology/`
- `../../../../../release/candidates/hydrology/`
- `../../../../../release/manifests/hydrology/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy valid Hydrology EvidenceBundle payloads with complete required common fields;
- toy examples for HUC/WBD boundary support, reach identity support, observed flow or stage support, water-quality sample support, groundwater or aquifer support, regulatory-context support, modeled hydrograph support, and cross-lane link support;
- toy `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, and `spec_hash` examples;
- toy expected outputs such as validation pass, review-ready, evidence-resolved, citation-ready, or decision-envelope `ANSWER` when consumed by a governed surface;
- contrast examples paired with `../invalid/` when useful.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy bundle IDs, toy claim scopes, toy evidence refs, toy source-record refs, toy citation refs, toy rights refs, toy sensitivity labels, toy transform refs, toy checksums, toy spec hashes, toy timestamps, and toy digests.
- Make the valid condition explicit: complete required fields, narrow claim scope, evidence-resolved, citation-ready, rights-visible, sensitivity-visible, transform-visible, checksum-present, spec-hash-present, source-role-preserved, or cross-lane ownership-preserved.
- Make expected outcome explicit: validation pass, review-ready, evidence-resolved, citation-ready, `ANSWER` when consumed by a valid decision envelope, or expected output.
- Pair each valid input with an expected output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, transform lineage, checksum integrity, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, decision-envelope outcome, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level EvidenceBundle fields as implemented unless the schema is extended; the current contract says Hydrology-specific obligations are semantic, policy, fixture, and validation expectations layered on top of the shared schema.
- Do not treat fixture success as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected valid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Complete toy bundle for a HUC/WBD boundary claim | Validation pass | Claim scope and snapshot/vintage must be visible. |
| Complete toy bundle for a reach identity claim | Validation pass | Evidence must support the exact reach identity scope. |
| Complete toy bundle for an observed flow or stage claim | Validation pass | Source role and time window remain explicit. |
| Complete toy bundle for a water-quality sample claim | Validation pass | Method and program limits remain reviewable through citations/transforms. |
| Complete toy bundle for a regulatory-context claim | Validation pass | Regulatory context remains regulatory context. |
| Complete toy bundle for a modeled hydrograph claim | Validation pass | Model lineage and transform posture remain visible. |
| Complete toy bundle for a cross-lane link | Review-ready or validation pass | Both sides preserve ownership, source role, sensitivity, and evidence. |
| Valid bundle consumed by a decision envelope | `ANSWER` | The decision envelope still owns runtime outcome. |

## Maintenance notes

- Update this README when valid payload files, validators, tests, helper scripts, expected-output names, or evidence-bundle consumer contracts are added.
- Link each valid fixture to the EvidenceBundle schema check, Hydrology evidence-bundle contract check, evidence-resolution check, citation-validation check, rights check, sensitivity check, transform-lineage check, checksum check, source-role check, policy-filter check, release-readiness check, decision-envelope check, drawer check, Focus Mode check, correction check, rollback check, or governed-API dry-run that consumes it.
- If expected valid behavior changes, update the paired input, expected output, consumer notes, sibling invalid/contrast notes, and verification status together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Parent evidence-bundle fixture README: present but blank during this update.
- Sibling invalid fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/evidence_bundle/invalid/README.md`.
- Hydrology EvidenceBundle contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/evidence_bundle.md`.
- Hydrology decision-envelope fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/README.md` and child lanes.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, evidence-bundle checks, Hydrology governed-API tests, decision-envelope checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, transform-lineage checks, checksum checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.
