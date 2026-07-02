# Habitat invalid fixtures

`fixtures/domains/habitat/invalid/`

Status: draft / fixture lane / negative-path synthetic inputs.

This directory is for small synthetic Habitat examples that are intentionally rejected by bounded checks or expected to produce a bounded non-answer. Invalid fixtures support review of semantic-contract behavior, future schema checks, renderer checks, governed API behavior, Evidence Drawer behavior, Focus Mode behavior, source-role checks, context-join checks, policy dry-runs, pipeline dry-runs, topology checks, hierarchy checks, and documentation examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, species occurrence truth, plant occurrence truth, habitat quality proof, regulatory proof, or published artifacts.

## Negative-path posture

An invalid Habitat fixture demonstrates a bounded failure or non-answer. It does not prove that real Habitat data, real source rights, real policy decisions, real release manifests, or real public artifacts are present.

Invalid fixtures may represent missing identifiers, missing source descriptors, missing EvidenceBundle support, source-role mismatch, unsupported context joins, model/observation collapse, hierarchy failure, topology failure, policy failure, renderer-unsafe payloads, missing release posture, or missing rollback posture. Stable expected outputs should usually be paired in `../golden/`.

## Placement basis

This lane belongs under `fixtures/` because it contains negative-path synthetic examples, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Habitat fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to sibling lanes

Use this lane for invalid or negative-path synthetic inputs. Expected outputs should usually live in `../golden/` once behavior is stable.

| Sibling lane | Relationship |
|---|---|
| `../golden/` | Stores stable expected outputs for invalid inputs. |
| `../ecoregions/` | May contain ecoregion-specific positive or negative examples; move stable invalid examples here when a dedicated negative lane is clearer. |
| `../habitat_fauna_thin_slice/` | May contain proof-specific negative examples; move cross-cutting invalid inputs here when the failure posture is the main purpose. |

Future sibling lanes may add valid, land-cover, ecological-system, habitat-patch, suitability, connectivity, restoration, stewardship, source-role, map-ui, tier-transition, evidence-bundle, runtime-envelope, or other Habitat fixture inputs. Invalid examples may live here when they are cross-cutting or when the object-specific lane does not yet exist.

## Related references

- `../README.md`
- `../../README.md`
- `../golden/README.md`
- `../ecoregions/README.md`
- `../habitat_fauna_thin_slice/README.md`
- `../../../docs/domains/habitat/README.md`
- `../../../docs/domains/habitat/FILE_SYSTEM_PLAN.md`
- `../../../docs/domains/habitat/API_CONTRACTS.md`
- `../../../docs/domains/habitat/SOURCE_FAMILIES.md`
- `../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`
- `../../../docs/domains/habitat/sublanes/ecoregions.md`
- `../../../contracts/domains/habitat/`
- `../../../schemas/contracts/v1/domains/habitat/`
- `../../../policy/domains/habitat/`
- `../../../policy/sensitivity/habitat/`
- `../../../pipelines/domains/habitat/`
- `../../../pipelines/proofs/habitat_fauna_thin_slice/README.md`
- `../../../data/registry/sources/habitat/`
- `../../../release/manifests/habitat/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.invalid.json`, `*.input.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- intentionally incomplete Habitat examples;
- intentionally mismatched Habitat examples;
- examples with missing identity, missing source role, missing evidence support, missing rights state, missing policy state, missing review state, missing release state, or missing expected outcome;
- examples that attempt to use Habitat context as Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Spatial Foundation, People/Land, or UI/AI truth;
- examples that collapse model output, candidate output, observation, context, public derivative, proof result, EvidenceBundle, and release state;
- examples used to confirm a bounded non-answer, validation failure, topology failure, hierarchy failure, source-role failure, renderer failure, policy failure, or review-required result;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real Habitat records, real source exports, live upstream fetch results, credentials, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, species occurrence data, plant occurrence data, habitat quality claims, regulatory designation truth, hydrology truth, soil truth, hazards truth, land/title truth, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Make the intended failure explicit in the file name, fixture metadata, or paired expected output.
- Prefer one failure reason per fixture unless a test intentionally checks precedence.
- Pair invalid inputs with expected outputs in `../golden/` when practical.
- Use toy source IDs, toy object IDs, toy layer IDs, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Keep source role, evidence state, freshness state, sensitivity state, rights state, context-join state, hierarchy state, topology state, review state, release state, correction state, rollback state, and expected output state explicit where material.
- Do not include real source properties, direct model-runtime output, unpublished candidate content, or geometry that could reasonably be mistaken for real sensitive data.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `topology-valid`, `hierarchy-valid`, `context-join-valid`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat invalid fixtures as evidence, approval, release state, source authority, schema authority, implementation proof, occurrence truth, habitat quality proof, public-map authority, tile authority, or published output.

## Expected invalid fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Missing required identity | Validation failure | Identity must be stable before use. |
| Missing EvidenceBundle support | `ABSTAIN` | No claim is emitted without support. |
| Source role unclear or collapsed | `ABSTAIN` or review-required output | Source-role anti-collapse remains visible. |
| Ecoregion used as species or plant occurrence proof | `ABSTAIN` or validation failure | Occurrence truth remains in the owning domain. |
| Habitat context used as regulatory truth | `ABSTAIN` or validation failure | Regulatory posture requires its own admitted source role and evidence. |
| Model output presented as observation | `DENY`, `ABSTAIN`, or validation failure | Model-vs-observation posture remains explicit. |
| Public derivative missing release, correction, or rollback posture | Validation failure or review-required output | Public use requires governed release posture. |
| Renderer-unsafe geometry or hierarchy | Validation failure or bounded error | Renderer safety remains separate from semantic validity. |

## Maintenance notes

- Update this README when payload files, sibling valid/golden lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the semantic-contract review, future schema check, pipeline dry-run, renderer check, topology check, hierarchy check, context-join check, source-role check, governed-API test, Evidence Drawer test, Focus Mode test, evidence resolver, policy check, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Parent habitat fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Golden fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/golden/README.md`.
- Ecoregions fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/ecoregions/README.md` from the prior verified fetch in this session.
- Habitat × Fauna fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/habitat_fauna_thin_slice/README.md` from the prior verified fetch in this session.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, topology checks, hierarchy checks, context-join checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.
