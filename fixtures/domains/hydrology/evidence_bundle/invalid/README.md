# Hydrology evidence-bundle invalid fixtures

`fixtures/domains/hydrology/evidence_bundle/invalid/`

Status: draft / invalid fixture lane / Hydrology EvidenceBundle negative-path examples.

This directory is for small synthetic Hydrology `EvidenceBundle` fixtures that should fail validation, review, citation closure, policy checks, release-readiness checks, or governed API use. These examples are meant to exercise fail-closed behavior for missing evidence support, mismatched claim scope, unresolved EvidenceRefs, missing source records, missing citations, rights gaps, sensitivity gaps, transform gaps, checksum gaps, source-role collapse, cross-lane evidence mismatch, and proof-vs-release confusion.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, source descriptors, review approvals, policy decisions, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## Invalid fixture posture

The Hydrology EvidenceBundle contract defines the Hydrology alias of KFM's shared `evidence_bundle`: the closure artifact that packages source records, evidence refs, citations, rights, sensitivity, transforms, checksums, and spec linkage for a Hydrology claim scope. It also states that an EvidenceBundle is support for a claim scope; it is not source truth, a policy decision, a release manifest, validation report, public layer, runtime answer, or generated explanation.

The shared EvidenceBundle schema requires `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, and `spec_hash`. Invalid fixtures in this lane should make one or more of those requirements absent, malformed, unresolved, mismatched, or semantically insufficient.

Hydrology-specific meaning must remain in common fields such as `claim_scope`, `evidence_refs`, `source_records`, `citations`, `transforms`, `sensitivity`, policy, fixtures, validation reports, and docs. Do not add Hydrology-specific top-level EvidenceBundle fields as implemented unless the shared schema or domain alias schema is extended.

This lane can support future validation and governed-API checks, but examples here do not prove validator implementation, EvidenceBundle storage, route behavior, policy enforcement, schema enforcement, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent `fixtures/domains/hydrology/evidence_bundle/README.md` is blank during this update.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../` | Parent Hydrology evidence-bundle fixture lane; blank during this update. |
| `../../decision_envelope/invalid/` | Decision-envelope invalid fixtures may consume invalid EvidenceBundle cases as `ABSTAIN`, `DENY`, or `ERROR` scenarios. |
| `../../decision_envelope/valid/` | Valid decision-envelope fixtures may provide contrast cases with resolvable evidence support. |
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
- `../../decision_envelope/invalid/README.md`
- `../../decision_envelope/valid/README.md`
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

- small synthetic `*.input.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy invalid Hydrology EvidenceBundle payloads with absent, malformed, unresolved, mismatched, or semantically insufficient required fields;
- toy examples for missing `claim_scope`, empty `evidence_refs`, empty `source_records`, missing citations, missing rights/license posture, missing sensitivity label, missing transforms, missing checksums, missing `spec_hash`, unresolved EvidenceRefs, wrong-domain evidence refs, source-role collapse, or unsupported cross-lane links;
- toy expected outputs such as validation failure, review-required, `ABSTAIN`, `DENY`, or `ERROR` when consumed by a decision envelope, drawer, Focus Mode surface, layer resolver, or release-readiness check;
- contrast examples paired with future valid examples when useful.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy bundle IDs, toy claim scopes, toy evidence refs, toy source-record refs, toy citation refs, toy rights refs, toy sensitivity labels, toy transform refs, toy checksums, toy spec hashes, toy timestamps, and toy digests.
- Make the defect explicit: missing required field, empty required array, unresolved EvidenceRef, wrong-domain EvidenceRef, mismatched claim scope, source-role collapse, missing rights, missing sensitivity, missing transform, missing checksum, or proof treated as release authority.
- Make expected outcome explicit: validation failure, review-required, `ABSTAIN`, `DENY`, `ERROR`, blocked render, release-readiness failure, or expected output.
- Pair each invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, transform lineage, checksum integrity, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, decision-envelope outcome, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level EvidenceBundle fields as implemented unless the schema is extended; the current contract says Hydrology-specific obligations are semantic, policy, fixture, and validation expectations layered on top of the shared schema.
- Do not treat fixture failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected invalid examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Missing `claim_scope` | Validation failure | Reviewers cannot tell what claim the bundle supports. |
| Empty `evidence_refs` | Validation failure or `ABSTAIN` | Bundle without evidence refs cannot support a claim. |
| Empty `source_records` | Validation failure | Provenance reconstruction is not possible. |
| Missing citations | Validation failure or `ABSTAIN` | Public answer surfaces need citation closure. |
| Missing rights/license posture | Validation failure or review-required output | Rights must be inspectable before release. |
| Missing sensitivity label | Validation failure or review-required output | Sensitivity cannot be inferred silently. |
| Missing transforms | Validation failure | Claim support must show how source evidence became support. |
| Missing checksums or `spec_hash` | Validation failure | Integrity and deterministic linkage must be present. |
| EvidenceRef points to the wrong domain or object family | `ABSTAIN` or validation failure | Evidence identity must match claim scope. |
| Proof object treated as release approval | `DENY` or release-readiness failure | Evidence support is not publication authority. |

## Maintenance notes

- Update this README when invalid payload files, validators, tests, helper scripts, expected-output names, or evidence-bundle consumer contracts are added.
- Link each invalid fixture to the EvidenceBundle schema check, Hydrology evidence-bundle contract check, evidence-resolution check, citation-validation check, rights check, sensitivity check, transform-lineage check, checksum check, source-role check, policy-filter check, release-readiness check, decision-envelope check, drawer check, Focus Mode check, correction check, rollback check, or governed-API dry-run that consumes it.
- If expected invalid behavior changes, update the paired input, expected output, consumer notes, and verification status together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Parent evidence-bundle fixture README: present but blank during this update.
- Hydrology EvidenceBundle contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/evidence_bundle.md`.
- Hydrology proof-lane alignment: PARTIALLY VERIFIED against `data/proofs/hydrology/README.md`.
- EvidenceBundle standard alignment: PARTIALLY VERIFIED against `docs/standards/EVIDENCE_BUNDLE.md`.
- Hydrology decision-envelope fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/README.md` and child lanes.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, evidence-bundle checks, Hydrology governed-API tests, decision-envelope checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, transform-lineage checks, checksum checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.
