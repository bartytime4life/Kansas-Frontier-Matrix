# Hydrology evidence-bundle fixtures

`fixtures/domains/hydrology/evidence_bundle/`

Status: draft / fixture parent index / Hydrology EvidenceBundle examples.

This directory is the parent lane for small synthetic Hydrology `EvidenceBundle` fixture examples. These fixtures are used to exercise claim-scope evidence support, evidence refs, source-record handles, citations, rights posture, sensitivity labels, transforms, checksums, deterministic spec linkage, source-role preservation, decision-envelope consumption, drawer handoff, Focus Mode handoff, release-readiness checks, correction posture, rollback posture, and trust-membrane behavior.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, source descriptors, review approvals, policy decisions, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hydrology truth, AI authority, or published artifacts.

## EvidenceBundle posture

The Hydrology EvidenceBundle contract defines the Hydrology alias of KFM's shared `evidence_bundle`: the closure artifact that packages source records, evidence refs, citations, rights, sensitivity, transforms, checksums, and spec linkage for a Hydrology claim scope. EvidenceBundles answer what evidence supports an exact claim scope; they do not decide whether that claim is public-safe or should be rendered.

The current Hydrology schema is an alias of the shared EvidenceBundle schema and does not add Hydrology-specific top-level fields. Hydrology-specific meaning must therefore be carried through common fields such as `claim_scope`, `evidence_refs`, `source_records`, `citations`, `transforms`, `sensitivity`, policy, fixtures, validation reports, and docs until the schema is revised.

This fixture parent can support future validation and governed-API checks, but examples here do not prove validator implementation, EvidenceBundle storage, route behavior, policy enforcement, schema enforcement, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `valid/` | Positive-path Hydrology EvidenceBundle examples with complete required common fields. | Validation pass, review-ready, evidence-resolved, citation-ready, or decision-envelope `ANSWER` when consumed by a governed surface. |
| `invalid/` | Fail-closed EvidenceBundle examples with missing, malformed, unresolved, mismatched, or semantically insufficient support. | Validation failure, review-required, `ABSTAIN`, `DENY`, `ERROR`, blocked render, or release-readiness failure. |

## Relationship between fixture lanes

| Lane | Use |
|---|---|
| `valid/` | Synthetic EvidenceBundle examples intended to pass bounded semantic and shape checks. |
| `invalid/` | Synthetic EvidenceBundle examples intended to fail closed without supporting a claim. |
| Future `golden/` or expected-output lane | Stable expected outputs for valid and invalid inputs, if added. |
| `../decision_envelope/` | Runtime envelopes may consume valid or invalid evidence support and return finite outcomes. |
| Parent Hydrology fixture lane | Broader Hydrology fixture family; not inspected during this update. |

## Related references

- `valid/README.md`
- `invalid/README.md`
- `../decision_envelope/README.md`
- `../decision_envelope/valid/README.md`
- `../decision_envelope/invalid/README.md`
- `../README.md`
- `../../../README.md`
- `../../../../contracts/domains/hydrology/evidence_bundle.md`
- `../../../../contracts/evidence/evidence_bundle.md`
- `../../../../docs/standards/EVIDENCE_BUNDLE.md`
- `../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json`
- `../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`
- `../../../../policy/domains/hydrology/`
- `../../../../data/registry/sources/hydrology/`
- `../../../../data/proofs/hydrology/`
- `../../../../release/candidates/hydrology/`
- `../../../../release/manifests/hydrology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Hydrology EvidenceBundle payloads with `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, and `spec_hash` examples;
- toy examples for HUC/WBD boundary support, reach identity support, observed flow or stage support, water-quality sample support, groundwater or aquifer support, regulatory-context support, modeled hydrograph support, and cross-lane link support;
- toy failure examples for missing evidence support, unresolved refs, mismatched claim scope, missing source records, missing citations, rights gaps, sensitivity gaps, transform gaps, checksum gaps, source-role conflicts, cross-lane evidence mismatch, and proof-vs-release confusion;
- contrast examples showing the difference between a valid evidence-support fixture and an invalid variant;
- paired expected outputs when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy bundle IDs, toy claim scopes, toy evidence refs, toy source-record refs, toy citation refs, toy rights refs, toy sensitivity labels, toy transform refs, toy checksums, toy spec hashes, toy timestamps, and toy digests.
- Make the bundle posture explicit: valid, invalid, complete required fields, missing required field, narrow claim scope, mismatched claim scope, evidence-resolved, unresolved EvidenceRef, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, transform-visible, transform-missing, checksum-present, checksum-missing, spec-hash-present, source-role-preserved, source-role-conflicted, or expected output.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, rights posture, sensitivity posture, source-role validity, transform lineage, checksum integrity, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, decision-envelope outcome, correction posture, and rollback posture separate.
- Do not document Hydrology-specific top-level EvidenceBundle fields as implemented unless the schema is extended; the current contract says Hydrology-specific obligations are semantic, policy, fixture, and validation expectations layered on top of the shared schema.
- Do not treat fixture success or failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Preferred child lane | Expected posture |
|---|---|---|
| Complete toy bundle for a narrow Hydrology claim scope | `valid/` | Validation pass or review-ready. |
| Complete toy bundle consumed by a valid decision envelope | `valid/` | `ANSWER` from the envelope, not from the bundle itself. |
| Missing required field or empty required array | `invalid/` | Validation failure. |
| EvidenceRef is unresolved or points to the wrong scope | `invalid/` | `ABSTAIN` or validation failure when consumed. |
| Missing rights, sensitivity, transform, checksum, or spec linkage | `invalid/` | Validation failure or review-required output. |
| Proof object treated as policy or release approval | `invalid/` | `DENY` or release-readiness failure. |

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or evidence-bundle consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior changes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated `valid/README.md` and `invalid/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this parent during this update.
- Valid fixture alignment: PARTIALLY VERIFIED against `valid/README.md`.
- Invalid fixture alignment: PARTIALLY VERIFIED against `invalid/README.md`.
- Hydrology EvidenceBundle contract alignment: PARTIALLY VERIFIED against `contracts/domains/hydrology/evidence_bundle.md`.
- Hydrology decision-envelope fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/README.md` and child lanes.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Parent Hydrology fixture alignment: NEEDS VERIFICATION.
- Consumer alignment: NEEDS VERIFICATION against validators, evidence-bundle checks, Hydrology governed-API tests, decision-envelope checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, transform-lineage checks, checksum checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, and UI implementation.
- Tests and validators: NOT RUN.
