<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-domains-hazards-readme
title: Hazards Fixture Parent README
type: fixture-parent-readme
version: v0.3
status: repository-grounded draft; reusable synthetic fixture index; non-authoritative; non-publisher
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Fixture steward
  - OWNER_TBD — Validation steward
created: 2026-05-08
updated: 2026-08-31
policy_label: public-doc; fixtures; hazards; synthetic-only; no-network; finite-outcomes; not-for-life-safety; release-gated
owning_root: fixtures/
responsibility: Index the reusable Hazards fixture families, their exact tracked inventory, their bounded consumers, and their non-authority limits without creating source, lifecycle, policy, release, alerting, or publication state.
truth_posture: "CONFIRMED sixteen direct fixture families and forty fixture-material files at main@5d835798e09a4dd14735779cb44206a8a3e8b2d3; CONFIRMED seven payload-bearing direct families and nine documentation-only or placeholder direct families; PROPOSED profiles remain inactive where their governing contract says so; NEEDS VERIFICATION exhaustive consumer coverage, stewardship, CI/ruleset binding, runtime coupling, promotion enforcement, and public effects"
tags: [kfm, fixtures, hazards, synthetic, valid, invalid, golden, advisory, drought, USDM, rollback, no-network, not-for-life-safety, ANSWER, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - drawer/README.md
  - drinking_water_advisory/README.md
  - feature_resolver/README.md
  - focus/README.md
  - golden/README.md
  - identity/README.md
  - invalid/README.md
  - layer_manifest/README.md
  - negative/README.md
  - synthetic_rollback_rehearsal/README.md
  - valid/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../tools/validators/domains/hazards/README.md
  - ../../../tools/validators/hazards/validate_drought_families.py
  - ../../../tests/domains/hazards/README.md
  - ../../../tests/schemas/test_drought_separation_contracts.py
  - ../../../tests/schemas/test_kdhe_hab_advisory_snapshot_contracts.py
  - ../../../.github/workflows/domain-hazards.yml
  - ../../../.github/workflows/drinking-water-advisory.yml
  - ../../../release/manifests/README.md
notes:
  - "Inventory counts exclude README.md, .gitkeep, and PLACEHOLDER.md; the forty fixture-material files are thirty-nine JSON files and one marker file."
  - "Executable fixture replay establishes only bounded deterministic behavior at the tested ref; it does not establish factual truth, source admission, rights, policy approval, release, alerting, or publication."
  - "The test-local Hazards fixture routing README retains a stale nine-child snapshot and remains a separate follow-up candidate."
[/KFM_META_BLOCK_V2] -->

# Hazards fixtures

`fixtures/domains/hazards/`

Status: repository-grounded draft / fixture parent index / synthetic Hazards examples / non-publisher.

This directory is the parent lane for small synthetic Hazards fixture examples. Hazards fixtures are used to exercise bounded feature resolution, Evidence Drawer projection, Focus Mode, identity handling, layer manifests, valid/negative/invalid cases, golden expected outputs, source-role preservation, evidence resolution, citation validation, freshness state, policy state, release posture, correction posture, rollback posture, and public-safe UI handoff examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, source authority, policy authority, release authority, Hazards truth, AI authority, or published artifacts.

## Fixture posture

Use this parent lane to navigate Hazards fixture families and keep their boundaries consistent. Current `main` contains 16 direct child families: 11 have README coverage, five are payload-first machine fixture families, and two combine README coverage with machine material. After excluding `README.md`, `.gitkeep`, and `PLACEHOLDER.md`, the subtree contains 40 fixture-material files: 39 JSON files and one marker file.

A fixture is not factual or operational proof. When a fixture is replayed by an identified validator and test, it can prove only that bounded deterministic behavior at the tested ref. It does not prove governed API or UI behavior, policy enforcement, release integration, source activation, EvidenceBundle closure, current conditions, alert authority, or publication.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Direct child inventory

This is the complete direct-child inventory at the pinned ref. Material counts exclude `README.md`, `.gitkeep`, and `PLACEHOLDER.md`. A payload-bearing row means only that tracked material and a bounded repository consumer exist; it does not activate a source, accept a policy profile, or establish current hazard conditions.

| Direct family | Tracked fixture material | Repository-grounded posture |
|---|---:|---|
| `drawer/` | 0 | `DOCUMENTATION_ONLY / NO_FIXTURE_PAYLOADS`; the separate general EvidenceDrawerPayload fixture profile remains `PROPOSED`. |
| `drinking_water_advisory/` | 1 JSON | Bounded synthetic advisory cases consumed by the drinking-water validator and tests; no official advisory authority. |
| `drought_declaration/` | 8 JSON | One valid and seven invalid declaration cases for the drought separation contract. |
| `drought_obs_decl_relationship/` | 2 JSON | One valid and one invalid observation/declaration relationship case. |
| `drought_observation/` | 8 JSON | One valid and seven invalid observation cases for the drought separation contract. |
| `feature_resolver/` | 0 | `DOCUMENTATION_ONLY / NO_FIXTURE_PAYLOADS`; proposed resolver scaffolds are not executable Hazards proof. |
| `focus/` | 0 | `DOCUMENTATION_ONLY / NO_FIXTURE_PAYLOADS`; the separate general Focus proof remains `PROPOSED`. |
| `golden/` | 0 | `DOCUMENTATION_ONLY / PLACEHOLDER_ONLY`; no paired expected-output payload is tracked. |
| `identity/` | 0 | `DOCUMENTATION_ONLY / NO_FIXTURE_PAYLOADS`. |
| `invalid/` | 0 | `DOCUMENTATION_ONLY / PLACEHOLDER_ONLY`; its eight nested defect lanes also contain no payloads. |
| `kdhe_hab_advisory_snapshot/` | 13 JSON | Eight valid and five invalid synthetic snapshot cases for the bounded schema contract; publication remains disabled. |
| `layer_manifest/` | 0 | `DOCUMENTATION_ONLY / NO_FIXTURE_PAYLOADS`; the separate general data LayerManifest profile remains `PROPOSED_INACTIVE`. |
| `negative/` | 0 | `DOCUMENTATION_ONLY / NO_FIXTURE_PAYLOADS`. |
| `synthetic_rollback_rehearsal/` | 6 JSON + 1 marker | Marker-protected, no-sensitive-data rollback rehearsal consumed by bounded helper and release tests; not operational rollback authority. |
| `usdm_materiality/` | 1 JSON | Synthetic materiality cases consumed by the bounded USDM validator and tests. |
| `valid/` | 0 | `DOCUMENTATION_ONLY / PLACEHOLDER_ONLY`. |

## Proof map

The current machine-material families map to these narrow proof surfaces:

- drinking-water advisory: `tools/validators/domains/hazards/validate_drinking_water_advisory.py`, its domain tests, and `.github/workflows/drinking-water-advisory.yml`;
- drought observation, declaration, and relationship: `tools/validators/hazards/validate_drought_families.py` and `tests/schemas/test_drought_separation_contracts.py`;
- KDHE HAB advisory snapshot: `tests/schemas/test_kdhe_hab_advisory_snapshot_contracts.py`;
- synthetic rollback rehearsal: the domain helper tests, release tests, and `.github/workflows/rollback-drill.yml`;
- USDM materiality: `tools/validators/domains/hazards/validate_usdm_materiality.py` and its domain tests.

These mappings are deterministic test evidence only. They do not establish exhaustive consumer coverage, runtime coupling, accepted stewardship, required-check enforcement, source admission, EvidenceBundle closure, life-safety suitability, or release and publication authority.

## Related references

- `valid/README.md`
- `negative/README.md`
- `invalid/README.md`
- `golden/README.md`
- `feature_resolver/README.md`
- `drawer/README.md`
- `focus/README.md`
- `identity/README.md`
- `layer_manifest/README.md`
- `synthetic_rollback_rehearsal/README.md`
- `drinking_water_advisory/cases.json`
- `drought_declaration/`
- `drought_obs_decl_relationship/`
- `drought_observation/`
- `kdhe_hab_advisory_snapshot/`
- `usdm_materiality/cases.json`
- `../../README.md`
- `../../../docs/architecture/governed-api/README.md`
- `../../../docs/architecture/hazards-trust-membrane.md`
- `../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`
- `../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`
- `../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../contracts/domains/hazards/domain_feature_identity.md`
- `../../../contracts/domains/hazards/domain_layer_descriptor.md`
- `../../../contracts/data/layer_manifest.md`
- `../../../schemas/contracts/v1/domains/hazards/`
- `../../../schemas/contracts/v1/evidence/`
- `../../../schemas/contracts/v1/focus/`
- `../../../schemas/contracts/v1/data/layer_manifest.schema.json`
- `../../../policy/domains/hazards/`
- `../../../data/registry/sources/hazards/`
- `../../../data/proofs/hazards/`
- `../../../release/manifests/README.md`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This parent lane and its children may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.negative.json`, `*.invalid.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy feature, layer, drawer, Focus, identity, evidence, policy, release, correction, rollback, source-role, freshness, disclaimer, and trust-membrane examples;
- toy `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, review-required, validation-failure, blocked-render, stale-state, missing-evidence, correction-visible, rollback-visible, or expected-output examples;
- contrast examples showing the difference between valid governed envelopes and negative/invalid variants;
- paired expected outputs in `golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, tile bytes, renderer implementations, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Make the lane purpose, file purpose, expected outcome, and consumer notes explicit.
- Use toy IDs, toy source refs, toy feature refs, toy layer refs, toy evidence refs, toy citation refs, toy policy refs, toy release refs, toy timestamps, toy digests, and toy hashes.
- Make expected posture explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, bounded context, evidence-resolved, missing-evidence, citation-validated, policy-allowed, release-permitted, release-blocked, source-role-preserved, source-role-conflicted, freshness-visible, stale, expired, correction-visible, rollback-visible, disclaimer-visible, or expected output.
- Pair each stable input with an expected output in `golden/` when practical.
- Keep schema validity, semantic validity, evidence resolution, citation validation, policy filtering, source-role validity, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, resolver context, layer-manifest state, UI behavior, correction posture, and rollback posture separate.
- Do not treat fixture success or failure as EvidenceBundle closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Maintenance notes

- Update this README when new child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior changes, update the paired input, expected output, consumer notes, child README, and `golden/README.md` together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- `CONFIRMED`: 16 direct child families and 40 fixture-material files at `main@5d835798e09a4dd14735779cb44206a8a3e8b2d3`.
- `CONFIRMED`: seven direct families carry machine material; nine are documentation-only or placeholder-only.
- `CONFIRMED`: all 11 direct child READMEs and all five payload-first direct families are represented above.
- `CONFIRMED`: the parent lane is reusable synthetic fixture material under the accepted `fixtures/` responsibility root, not test-local wrappers under `tests/fixtures/`.
- `PROPOSED`: profiles described as proposed or inactive by their governing contracts remain proposed or inactive; this index does not change them.
- `NEEDS_VERIFICATION`: the test-local routing README at `tests/fixtures/domains/hazards/README.md` retains an older nine-child snapshot and is intentionally outside this one-file review boundary.
- `NEEDS_VERIFICATION`: accepted stewardship, exhaustive two-way consumer backlinks, CI/ruleset binding, runtime/UI coupling, promotion enforcement, and any public effect.
- `UNKNOWN / HELD`: source admission, rights, sensitivity, freshness, EvidenceRef or EvidenceBundle closure, life-safety conclusions, lifecycle promotion, release, deployment, promotion, and publication.
