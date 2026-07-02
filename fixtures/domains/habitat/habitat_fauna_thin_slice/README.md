# Habitat × Fauna thin-slice fixtures

`fixtures/domains/habitat/habitat_fauna_thin_slice/`

Status: draft / fixture lane / cross-domain proof support.

This directory is for small synthetic, public-safe fixture examples supporting the Habitat × Fauna thin-slice proof. It supplies toy inputs, expected shapes, and dry-run examples for domain-boundary checks, source-role checks, EvidenceBundle closure checks, policy checks, public-safe derivative checks, release-blocker checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, Habitat truth, Fauna truth, or published artifacts.

## Proof posture

The proof-pipeline README defines `pipelines/proofs/habitat_fauna_thin_slice/` as the executable proof harness for demonstrating that Habitat context and Fauna evidence can move through a governed thin slice without collapsing domain authority, bypassing EvidenceBundle closure, or letting public clients read internal lifecycle stores.

The proof harness also states that Habitat and Fauna object families retain their owning domain lanes, and that proof results do not become release approval, EvidenceBundle truth, public artifacts, or live-data truth. This fixture lane supports that proof with synthetic examples only. It does not execute the proof harness, create proof receipts, create EvidenceBundles, decide policy, or publish anything.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic proof-support examples. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The Habitat file-system plan lists `fixtures/domains/habitat/habitat_fauna_thin_slice/` as a proposed joint fixture lane. The same plan marks concrete paths as proposed until verified and warns that cross-domain Habitat × Fauna files must preserve cross-domain placement discipline. This README documents the verified fixture placeholder without treating the lane as implementation proof.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, exact restricted geometry, and canonical-truth treatment do not belong here.

## Relationship to adjacent lanes

Use this lane for synthetic proof inputs where the main purpose is the Habitat × Fauna boundary and trust-membrane check.

| Adjacent lane | Relationship |
|---|---|
| `../golden/` | Stable expected outputs for thin-slice inputs may be paired there. |
| `../ecoregions/` | Ecoregion context examples may be referenced as Habitat-side regionalization context. |
| `../../../pipelines/proofs/habitat_fauna_thin_slice/` | Executable proof harness home; this lane only supplies fixture support. |
| `../../../pipelines/domains/habitat/` | Habitat domain processing home; this fixture lane does not own Habitat pipeline logic. |
| `../../../pipelines/domains/fauna/` | Fauna domain processing home; this fixture lane does not own Fauna pipeline logic. |
| `../../../data/proofs/evidence_bundle/` | EvidenceBundle/proof-data home; fixtures do not create evidence authority. |
| `../../../release/candidates/habitat/` and `../../../release/candidates/fauna/` | Release-candidate homes; fixtures do not approve publication. |

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../ecoregions/README.md`
- `../../../pipelines/proofs/habitat_fauna_thin_slice/README.md`
- `../../../pipelines/proofs/README.md`
- `../../../docs/domains/habitat/FILE_SYSTEM_PLAN.md`
- `../../../docs/domains/habitat/ARCHITECTURE.md`
- `../../../docs/domains/fauna/FILE_SYSTEM_PLAN.md`
- `../../../docs/domains/fauna/ARCHITECTURE.md`
- `../../../docs/domains/fauna/CROSS_LANE_RELATIONS.md`
- `../../../contracts/domains/habitat/`
- `../../../contracts/domains/fauna/`
- `../../../schemas/contracts/v1/domains/habitat/`
- `../../../schemas/contracts/v1/domains/fauna/`
- `../../../policy/domains/habitat/`
- `../../../policy/domains/fauna/`
- `../../../data/registry/sources/habitat/`
- `../../../data/registry/sources/fauna/`
- `../../../data/proofs/evidence_bundle/`
- `../../../data/receipts/pipeline/`
- `../../../release/candidates/habitat/`
- `../../../release/candidates/fauna/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Habitat context refs and toy Fauna refs that preserve owning-domain identity;
- toy join inputs for Habitat context plus Fauna-side references;
- toy source-role, evidence-ref, policy-state, review-state, public-safe derivative, release-blocker, correction, and rollback examples;
- toy trust-membrane examples showing that public clients consume governed APIs or released artifacts, not lifecycle stores;
- toy finite-outcome examples such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, or `SOURCE_STALE`;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real Habitat records, real Fauna records, live upstream fetch results, credentials, lifecycle data, source registry authority, evidence authority, proof receipts, proof packs, policy rules, executable proof code, connector code, pipeline implementation code, public API payloads, public map data, public tiles, release manifests, Habitat truth, Fauna truth, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy habitat IDs, toy fauna IDs, toy source IDs, toy evidence references, toy feature IDs, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make the proof intent explicit: domain-boundary check, source-role check, EvidenceBundle gate, policy gate, public-safe derivative gate, release-blocker gate, trust-membrane gate, or no-direct-publish gate.
- Keep Habitat-owned and Fauna-owned objects separate in every fixture.
- Keep source role, evidence state, policy state, rights state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `domain-boundary-valid`, `source-role-valid`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `public-safe`, `catalog-safe`, `release-safe`, `trust-membrane-safe`, and `renderer-safe` as separate checks.
- Do not treat fixture success as evidence closure, proof receipt, source authority, schema authority, implementation proof, approval, release state, public-map authority, tile authority, or published output.

## Expected thin-slice fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Habitat context joined to toy Fauna reference with resolved toy support | Valid input or `ANSWER` output | Demonstrates boundary-preserving join without becoming release approval. |
| Habitat context used as Fauna truth | `ABSTAIN` or validation failure | Habitat context does not replace Fauna authority. |
| Fauna reference used as Habitat object truth | `ABSTAIN` or validation failure | Fauna evidence does not replace Habitat authority. |
| Missing EvidenceBundle support | `ABSTAIN` or `HOLD` | Cite-or-abstain remains visible. |
| Public output requested from internal lifecycle refs | `DENY` or validation failure | Trust membrane remains intact. |
| Missing release/correction/rollback posture | release-blocker expected output | Proof outputs blockers, not publication. |
| Unsupported policy posture | `DENY`, `HOLD`, or generalized derivative expectation | Most-restrictive applicable policy remains visible. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, proof-runner contracts, or consumer contracts are added.
- Link each fixture to the proof-harness check, domain-boundary check, source-role check, EvidenceBundle check, policy check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, release-blocker check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Proof-pipeline alignment: PARTIALLY VERIFIED against `pipelines/proofs/habitat_fauna_thin_slice/README.md`.
- Habitat file-system alignment: PARTIALLY VERIFIED against `docs/domains/habitat/FILE_SYSTEM_PLAN.md`.
- Sibling fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/golden/README.md` and `fixtures/domains/habitat/ecoregions/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against proof-harness checks, validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, source-role checks, schema checks, and policy checks.
- Tests and validators: NOT RUN.
