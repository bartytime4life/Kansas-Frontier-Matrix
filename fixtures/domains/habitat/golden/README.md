# Habitat golden fixtures

`fixtures/domains/habitat/golden/`

Status: draft / fixture lane / expected-output examples.

This directory is for small synthetic Habitat expected-output fixtures. Golden fixtures describe the expected result for known synthetic Habitat inputs used by bounded checks, renderer examples, governed API examples, Focus Mode examples, Evidence Drawer examples, pipeline dry-runs, source-role checks, context-join checks, policy dry-runs, and documentation examples.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, species occurrence truth, plant occurrence truth, habitat quality proof, regulatory proof, or published artifacts.

## Placement basis

This lane belongs under `fixtures/` because it contains expected-output examples for synthetic fixtures. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Habitat fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to input lanes

Use this lane for stable expected outputs paired with synthetic Habitat inputs from sibling fixture lanes.

| Input lane | Expected-output use | Status |
|---|---|---|
| `../ecoregions/` | Expected ecoregion, regionalization, hierarchy, context-join, renderer, policy, governed API, Evidence Drawer, or Focus Mode outputs. | Present README populated. |

Future sibling lanes may add valid, invalid, land-cover, ecological-system, habitat-patch, suitability, connectivity, restoration, stewardship, source-role, map-ui, tier-transition, evidence-bundle, runtime-envelope, or other Habitat fixture inputs. Expected outputs may be stored here when they are stable, deterministic, and documented.

## Related references

- `../README.md`
- `../../README.md`
- `../ecoregions/README.md`
- `../../../docs/domains/habitat/sublanes/ecoregions.md`
- `../../../docs/domains/habitat/README.md`
- `../../../docs/domains/habitat/API_CONTRACTS.md`
- `../../../docs/domains/habitat/SOURCE_FAMILIES.md`
- `../../../contracts/domains/habitat/`
- `../../../contracts/domains/habitat/ecoregions/README.md`
- `../../../schemas/contracts/v1/domains/habitat/`
- `../../../policy/domains/habitat/`
- `../../../policy/sensitivity/habitat/`
- `../../../pipelines/domains/habitat/`
- `../../../data/registry/sources/habitat/`
- `../../../release/manifests/habitat/`
- `../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.expected.json`, `*.expected.geojson`, `*.expected.jsonl`, `*.expected.yaml`, `*.expected.yml`, `*.expected.svg`, or `*.md` expected-output examples;
- expected positive-path outputs for valid public-safe Habitat fixture inputs;
- expected bounded non-answer, validation-failure, stale-source, unsupported-join, source-role-failure, hierarchy-failure, topology-failure, renderer-failure, policy-failure, or review-required outputs for negative-path fixture inputs;
- expected ecoregion, ecological-system, land-cover, habitat-patch, suitability, connectivity, restoration, stewardship, source-admission, Evidence Drawer, Focus Mode, governed API, renderer, topology, context-join, or pipeline dry-run outputs;
- paired expected outputs for inputs stored in sibling fixture lanes such as `../ecoregions/` and future Habitat fixture lanes;
- README files explaining fixture intent and boundaries.

## Exclusions

Do not use this lane for real Habitat records, real source exports, live upstream fetch results, credentials, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, species occurrence data, plant occurrence data, habitat quality claims, regulatory designation truth, hydrology truth, soil truth, hazards truth, land/title truth, or published artifacts.

## Fixture design rules

- Keep expected outputs synthetic, compact, deterministic, and reviewable.
- Pair golden outputs with a clearly named input fixture whenever practical.
- Use naming that makes the relationship obvious, such as `<scenario>.input.json` in a sibling lane and `<scenario>.expected.json` in this lane, or an equivalent documented pair.
- Keep expected outcomes explicit, such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, `SOURCE_STALE`, validation failure, renderer-safe output, topology-safe output, hierarchy-safe output, join-safe output, or another documented finite posture.
- Keep source role, evidence state, freshness state, sensitivity state, rights state, context-join state, hierarchy state, review state, release state, correction state, and expected output state explicit where material.
- Do not include real source properties, direct model-runtime output, unpublished candidate content, or geometry that could reasonably be mistaken for real sensitive data.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `topology-valid`, `hierarchy-valid`, `context-join-valid`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat golden fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, occurrence truth, habitat quality proof, public-map authority, tile authority, or published output.

## Expected golden fixture examples

| Input lane | Example expected output | Notes |
|---|---|---|
| `../ecoregions/` | Public-safe ecoregion snapshot `ANSWER` output | Demonstrates regionalization context without becoming occurrence truth. |
| `../ecoregions/` | Ecoregion `ABSTAIN` output for missing EvidenceBundle support | Cite-or-abstain remains visible. |
| `../ecoregions/` | Validation failure for missing framework or hierarchy level | Framework and level must be explicit. |
| `../ecoregions/` | Context-join `ABSTAIN` output when used as species or plant occurrence proof | Occurrence truth remains in Fauna or Flora. |
| Future `valid/` | Positive governed API or renderer output | Must remain synthetic and public-safe. |
| Future `invalid/` | Bounded non-answer or validation output | Failure intent must remain explicit. |
| Future source fixture lane | Source-admission or source-role expected output | Registry authority remains separate. |

## Maintenance notes

- Update this README when payload files, input fixture lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each golden fixture to the input fixture and the test, renderer check, governed-API contract, Focus Mode test, Evidence Drawer test, pipeline dry-run, topology check, hierarchy check, context-join check, evidence resolver, policy check, or documentation example that consumes it.
- Keep payloads small enough for normal code review.
- If an expected output becomes broad enough to be a release artifact, move that concern to the governed release lane instead of expanding this fixture lane.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Parent habitat fixture README: present but still a greenfield stub during this update.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Sibling input alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/ecoregions/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, topology checks, hierarchy checks, context-join checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.
