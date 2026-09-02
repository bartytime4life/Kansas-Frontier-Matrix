# Hydrology golden fixtures

`fixtures/domains/hydrology/golden/`

Status: draft / fixture lane / expected-output examples.

This directory is for small synthetic Hydrology expected-output fixtures. Golden fixtures describe the expected result for known synthetic Hydrology inputs used by bounded checks, decision-envelope examples, EvidenceBundle examples, Evidence Drawer examples, Focus Mode examples, layer resolver examples, export examples, source-role checks, evidence-resolution checks, citation-validation checks, policy dry-runs, release-readiness checks, and documentation examples.

These files are examples only. They are not source records, lifecycle data, actual EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, Hydrology truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Golden fixture posture

Use this lane for stable expected outputs paired with synthetic Hydrology inputs from sibling fixture lanes. A golden fixture should make the expected finite posture explicit, such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-required, evidence-resolved, citation-ready, citation-failed, release-ready, release-blocked, source-role-preserved, source-role-conflicted, correction-visible, rollback-visible, or blocked render.

A golden fixture is not proof that implementation exists. It does not prove validator behavior, governed API route behavior, UI behavior, policy enforcement, schema enforcement, EvidenceBundle storage, release integration, or CI coverage by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains expected-output examples for synthetic fixtures. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hydrology fixture README was not inspected during this update.

## Relationship to input lanes

Use this lane for stable expected outputs paired with synthetic Hydrology inputs from sibling fixture lanes.

| Input lane | Expected-output use | Status |
|---|---|---|
| `../decision_envelope/` | Expected runtime envelopes for valid and invalid Hydrology decision-envelope inputs. | Present README populated. |
| `../decision_envelope/valid/` | Expected `ANSWER`, valid `ABSTAIN`, valid `DENY`, valid `ERROR`, or validation-pass outputs. | Present README populated. |
| `../decision_envelope/invalid/` | Expected fail-closed `ABSTAIN`, `DENY`, `ERROR`, validation-failure, review-required, or blocked-render outputs. | Present README populated. |
| `../evidence_bundle/` | Expected evidence-support outcomes for valid and invalid Hydrology EvidenceBundle inputs. | Present README populated. |
| `../evidence_bundle/valid/` | Expected validation pass, review-ready, evidence-resolved, citation-ready, or decision-envelope `ANSWER` outputs. | Present README populated. |
| `../evidence_bundle/invalid/` | Expected validation failure, review-required, `ABSTAIN`, `DENY`, `ERROR`, or release-readiness failure outputs. | Present README populated. |

Future sibling lanes may add feature-resolver, drawer, Focus Mode, layer-manifest, observation, gauge, HUC/WBD, reach, water-quality, groundwater, regulatory-context, modeled-context, source-role, map-ui, or other Hydrology fixture inputs. Expected outputs may be stored here when they are stable, deterministic, and documented.

## Related references

- `../decision_envelope/README.md`
- `../decision_envelope/valid/README.md`
- `../decision_envelope/invalid/README.md`
- `../evidence_bundle/README.md`
- `../evidence_bundle/valid/README.md`
- `../evidence_bundle/invalid/README.md`
- `../README.md`
- `../../README.md`
- `../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../contracts/domains/hydrology/decision_envelope.md`
- `../../../contracts/domains/hydrology/evidence_bundle.md`
- `../../../contracts/runtime/decision_envelope.md`
- `../../../contracts/evidence/evidence_bundle.md`
- `../../../schemas/contracts/v1/domains/hydrology/`
- `../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`
- `../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`
- `../../../policy/domains/hydrology/`
- `../../../data/registry/sources/hydrology/`
- `../../../data/proofs/hydrology/`
- `../../../release/candidates/hydrology/`
- `../../../release/manifests/hydrology/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.expected.json`, `*.expected.geojson`, `*.expected.jsonl`, `*.expected.yaml`, `*.expected.yml`, `*.expected.svg`, `*.golden.json`, or `*.md` expected-output examples;
- expected positive-path outputs for valid public-safe Hydrology fixture inputs;
- expected bounded non-answer, validation-failure, stale-state, unsupported-join, source-role-failure, citation-failure, evidence-resolution-failure, release-blocked, policy-blocked, review-required, or runtime-error outputs for negative-path fixture inputs;
- expected decision-envelope, EvidenceBundle, Evidence Drawer, Focus Mode, layer resolver, export, source-role, evidence-resolution, citation-validation, policy, release-readiness, correction, rollback, or documentation-example outputs;
- paired expected outputs for inputs stored in sibling fixture lanes such as `../decision_envelope/` and `../evidence_bundle/`;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for real Hydrology records, real source exports, live upstream fetch results, credentials, lifecycle data, actual EvidenceBundles, proof packs, source descriptors, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture design rules

- Keep expected outputs synthetic, compact, deterministic, and reviewable.
- Pair golden outputs with a clearly named input fixture whenever practical.
- Use naming that makes the relationship obvious, such as `<scenario>.input.json` in a sibling lane and `<scenario>.expected.json` in this lane, or an equivalent documented pair.
- Keep expected outcomes explicit, such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, review-required, evidence-resolved, evidence-missing, citation-ready, citation-failed, policy-allowed, policy-blocked, release-ready, release-blocked, source-role-preserved, source-role-conflicted, correction-visible, rollback-visible, blocked render, or another documented finite posture.
- Keep schema validity, semantic validity, evidence state, citation state, rights state, sensitivity state, source-role state, freshness state, review state, release state, correction state, rollback state, and expected-output state explicit where material.
- Do not include real source properties, direct model-runtime output, unpublished candidate content, or geometry that could reasonably be mistaken for real sensitive data.
- Treat `schema-valid`, `semantic-valid`, `evidence-resolved`, `citation-safe`, `rights-cleared`, `sensitivity-reviewed`, `source-role-valid`, `policy-admissible`, `release-safe`, `trust-membrane-safe`, `renderer-safe`, `focus-safe`, and `drawer-safe` as separate checks.
- Do not treat golden fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected golden fixture examples

| Input lane | Example expected output | Notes |
|---|---|---|
| `../decision_envelope/valid/` | Runtime `ANSWER` envelope for a released, evidence-backed feature/detail response | Envelope owns the runtime outcome. |
| `../decision_envelope/valid/` | Valid `ABSTAIN`, `DENY`, or `ERROR` envelope for a structurally valid non-answer case | Non-answer states can be valid. |
| `../decision_envelope/invalid/` | Validation failure for malformed envelope shape | Failure intent remains explicit. |
| `../evidence_bundle/valid/` | Validation-pass output for a complete toy bundle | Bundle supports a claim scope but does not publish it. |
| `../evidence_bundle/invalid/` | Validation failure for missing required EvidenceBundle fields | Required fields stay explicit. |
| `../evidence_bundle/invalid/` | `ABSTAIN` output for unresolved evidence support when consumed by a decision envelope | Cite-or-abstain remains visible. |
| Future `valid/` | Positive governed API, drawer, Focus, layer, or renderer output | Must remain synthetic and public-safe. |
| Future `invalid/` | Bounded fail-closed output | Failure intent must remain explicit. |

## Maintenance notes

- Update this README when payload files, input fixture lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each golden fixture to the input fixture and the test, governed-API contract, Evidence Drawer test, Focus Mode test, layer resolver check, export check, evidence resolver, citation validator, policy check, release-readiness check, schema check, renderer check, or documentation example that consumes it.
- Keep payloads small enough for normal code review.
- If an expected output becomes broad enough to be a release artifact, move that concern to the governed release lane instead of expanding this fixture lane.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Decision-envelope fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/README.md` and child lanes.
- EvidenceBundle fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/evidence_bundle/README.md` and child lanes.
- Habitat golden fixture precedent: PARTIALLY VERIFIED against `fixtures/domains/habitat/golden/README.md` for expected-output-lane structure only.
- Parent Hydrology fixture README: NEEDS VERIFICATION.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, golden-file checks, Hydrology governed-API tests, decision-envelope checks, evidence-bundle checks, drawer checks, Focus Mode checks, layer-manifest checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, transform-lineage checks, checksum checks, source-role checks, trust-membrane checks, release-readiness checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
