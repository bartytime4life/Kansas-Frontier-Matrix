# Habitat land-cover class-scheme fixtures

`fixtures/domains/habitat/land_cover/class_scheme/`

Status: draft / fixture lane / `ClassSchemeProfile` examples.

This directory is for small synthetic, public-safe Habitat land-cover class-scheme fixture examples. These examples support bounded semantic-contract reviews, future schema checks, class inventory checks, source-vintage checks, crosswalk checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, pipeline dry-runs, policy dry-runs, and documentation dry-runs.

These files are examples only. They are not source rasters, source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, habitat quality proof, occurrence proof, regulatory proof, or published artifacts.

## Contract posture

The `ClassSchemeProfile` semantic contract defines this object as the Habitat land-cover object that names, versions, and governs a source classification scheme or legend before `LandCoverObservation`, crosswalk, change-summary, public layer, or downstream Habitat reasoning can use its classes.

The same contract states that the paired schema path exists, but the schema is still a proposed scaffold with empty properties and permissive additional properties. Field-level validation, fixture payloads, validators, source registry records, policy files, release artifacts, API behavior, UI behavior, and CI/test coverage remain `NEEDS VERIFICATION`.

This fixture lane can support those future checks, but fixture examples do not prove schema enforcement, source activation, class-scheme authority, crosswalk maturity, pipeline implementation, or release readiness by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples and runtime/checking inputs, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The Habitat land-cover sublane doctrine lists `fixtures/domains/habitat/land_cover/` as the proposed fixture home for land-cover examples, while warning that specific land-cover paths require repo confirmation. This README documents the verified fixture placeholder without treating the lane as implementation proof.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Habitat fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to adjacent lanes

Use this lane for class-scheme examples where classification vocabulary, source legend, version pinning, class inventory, nodata/unknown handling, or allowed-use posture is the main purpose.

| Adjacent lane | Relationship |
|---|---|
| `../change_summary/` | Change summaries may reference class-scheme fixtures but do not define class-scheme authority. |
| `../../golden/` | Stable expected outputs for class-scheme inputs may be paired there. |
| `../../invalid/` | Negative-path class-scheme inputs may move there when the failure posture is the main purpose. |
| `../../ecoregions/` | Ecoregion examples may reference class schemes only as governed context; they do not own land-cover vocabulary. |
| `../../../../../contracts/domains/habitat/land_cover/class_scheme.md` | Semantic meaning; this fixture lane supplies examples only. |
| `../../../../../schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json` | Expected machine-shape home; current enforcement remains bounded by contract status. |
| `../../../../../pipelines/domains/habitat/land_cover/` | Executable processing home; this lane is not pipeline code. |
| `../../../../../pipeline_specs/habitat/land_cover/` | Declarative run/spec home; this lane is not a pipeline spec. |
| `../../../../../policy/domains/habitat/land_cover/` | Expected class-scheme and crosswalk policy home; fixtures do not decide policy. |
| `../../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../../README.md`
- `../../../README.md`
- `../change_summary/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../ecoregions/README.md`
- `../../habitat_fauna_thin_slice/README.md`
- `../../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`
- `../../../../../docs/domains/habitat/SOURCE_FAMILIES.md`
- `../../../../../docs/domains/habitat/API_CONTRACTS.md`
- `../../../../../contracts/domains/habitat/land_cover/class_scheme.md`
- `../../../../../contracts/domains/habitat/land_cover/observation.md`
- `../../../../../contracts/domains/habitat/land_cover/crosswalk.md`
- `../../../../../contracts/domains/habitat/land_cover/change_summary.md`
- `../../../../../contracts/domains/habitat/land_cover/uncertainty.md`
- `../../../../../schemas/contracts/v1/domains/habitat/land_cover/`
- `../../../../../policy/domains/habitat/land_cover/`
- `../../../../../policy/sensitivity/habitat/`
- `../../../../../pipelines/domains/habitat/land_cover/`
- `../../../../../pipeline_specs/habitat/land_cover/`
- `../../../../../data/registry/sources/habitat/`
- `../../../../../release/manifests/habitat/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy `ClassSchemeProfile` examples for positive-path and negative-path checks;
- toy scheme namespace, scheme ID, scheme version, class code, class label, class hierarchy, nodata-code, unknown-code, reserved-code, deprecated-code, and color-table examples;
- toy source-role, source-vintage, evidence-ref, rights-state, review-state, release-state, correction-state, and rollback-state examples;
- toy crosswalk-admissibility, change-summary-dependency, renderer-legend, Evidence Drawer, Focus Mode, governed API, policy, and pipeline dry-run examples;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real Habitat records, real source exports, live upstream fetch results, credentials, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, source raster data, class-scheme source authority, habitat quality claims, occurrence claims, regulatory designation truth, hydrology truth, soil truth, hazards truth, land/title truth, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy scheme namespaces, toy scheme IDs, toy version labels, toy class codes, toy class labels, toy source IDs, toy evidence references, toy timestamps, toy hashes, and toy style refs unless a bounded check explicitly requires a more realistic shape.
- Make scheme posture explicit: classification vocabulary, source legend, source version, class inventory, hierarchy, nodata/unknown handling, deprecated class, crosswalk dependency, observation dependency, public legend derivative, candidate, invalid, or expected output.
- Keep source role, evidence state, source vintage, rights state, class inventory state, hierarchy state, crosswalk state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Do not include real source properties, direct model-runtime output, unpublished candidate content, or geometry that could reasonably be mistaken for real sensitive data.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `scheme-version-valid`, `class-inventory-valid`, `hierarchy-valid`, `nodata-valid`, `crosswalk-admissible`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat class-scheme fixtures as source authority, evidence authority, crosswalk authority, observation truth, threshold policy authority, schema authority, implementation proof, release state, public-map authority, tile authority, habitat quality proof, occurrence proof, or published output.

## Expected class-scheme fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic class scheme with toy classes, version, source role, and evidence refs | Valid input or `ANSWER` output | Demonstrates vocabulary anchor without becoming observation truth. |
| Missing scheme version | Validation failure or `ERROR` | Published scheme versions must be explicit. |
| Duplicate class code with conflicting label | Validation failure | Class inventory must be deterministic. |
| Unknown/nodata code not declared | Validation failure or review-required output | Nodata/unknown semantics must be inspectable. |
| Class scheme used as land-cover observation | `ABSTAIN` or validation failure | Schemes define labels; observations apply them to space/time. |
| Class scheme used as crosswalk | `ABSTAIN` or validation failure | Crosswalks require separate reviewed mapping. |
| Source legend treated as release approval | `ABSTAIN` or validation failure | Release posture remains governed separately. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the semantic-contract review, future schema check, class-inventory check, source-vintage check, crosswalk check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, policy check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/land_cover/class_scheme.md`.
- Land-cover sublane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Schema alignment: NEEDS VERIFICATION because the contract reports the paired schema is still a permissive scaffold.
- Change-summary sibling alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/land_cover/change_summary/README.md`.
- Parent habitat fixture README: present but still a greenfield stub during this update.
- Sibling fixture alignment: NEEDS VERIFICATION against populated `golden/`, `invalid/`, `ecoregions/`, and `habitat_fauna_thin_slice/` READMEs.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, class-inventory checks, source-vintage checks, crosswalk checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.
