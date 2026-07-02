# Habitat land-cover change-summary fixtures

`fixtures/domains/habitat/land_cover/change_summary/`

Status: draft / fixture lane / `LandCoverChangeSummary` examples.

This directory is for small synthetic, public-safe Habitat land-cover change-summary fixture examples. These examples support bounded semantic-contract reviews, future schema checks, threshold checks, class-scheme checks, source-vintage checks, renderer checks, governed API examples, Evidence Drawer examples, Focus Mode examples, pipeline dry-runs, policy dry-runs, and documentation dry-runs.

These files are examples only. They are not source rasters, source records, lifecycle data, EvidenceBundles, source descriptors, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, habitat quality proof, occurrence proof, regulatory proof, or published artifacts.

## Contract posture

The `LandCoverChangeSummary` semantic contract defines this object as a governed, public-safe comparison between two versioned `LandCoverObservation` records over a declared analysis unit. It records source vintages, class schemes, valid-pixel footprint, materiality thresholds, change values, evidence closure, policy/review posture, release posture, correction, and rollback support.

The same contract states that the paired schema path exists, but the schema is still a proposed scaffold with empty properties and permissive additional properties. Field-level validation, fixture payloads, validators, threshold policy files, source registry records, release artifacts, API behavior, UI behavior, and CI/test coverage remain `NEEDS VERIFICATION`.

This fixture lane can support those future checks, but fixture examples do not prove schema enforcement, threshold policy maturity, pipeline implementation, or release readiness by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples and runtime/checking inputs, not governed lifecycle data. It is not a `data/`, `policy/`, `schemas/`, `contracts/`, `pipelines/`, `pipeline_specs/`, `connectors/`, `release/`, proof, source-registry, catalog, triplet, tile, or publication root.

The root fixture README states that `fixtures/` is for operational rendering inputs, not validator-only test data. It also states that RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Habitat fixture README is still a greenfield stub during this update, so this README keeps its own boundaries explicit.

## Relationship to adjacent lanes

Use this lane for change-summary examples where land-cover change semantics are the main purpose.

| Adjacent lane | Relationship |
|---|---|
| `../../golden/` | Stable expected outputs for change-summary inputs may be paired there. |
| `../../invalid/` | Negative-path change-summary inputs may move there when the failure posture is the main purpose. |
| `../../../habitat/land_cover/` | Parent land-cover fixture area; this lane is the change-summary object slice. |
| `../../../../contracts/domains/habitat/land_cover/change_summary.md` | Semantic meaning; this fixture lane supplies examples only. |
| `../../../../schemas/contracts/v1/domains/habitat/land_cover/change_summary.schema.json` | Expected machine-shape home; current enforcement remains bounded by contract status. |
| `../../../../pipelines/domains/habitat/land_cover/` | Executable processing home; this lane is not pipeline code. |
| `../../../../pipeline_specs/habitat/land_cover/` | Declarative run/spec home; this lane is not a pipeline spec. |
| `../../../../policy/domains/habitat/land_cover/` | Expected threshold/policy home; fixtures do not decide policy. |
| `../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../../README.md`
- `../../../README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../ecoregions/README.md`
- `../../habitat_fauna_thin_slice/README.md`
- `../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`
- `../../../../docs/domains/habitat/SOURCE_FAMILIES.md`
- `../../../../docs/domains/habitat/API_CONTRACTS.md`
- `../../../../contracts/domains/habitat/land_cover/change_summary.md`
- `../../../../contracts/domains/habitat/land_cover/observation.md`
- `../../../../contracts/domains/habitat/land_cover/crosswalk.md`
- `../../../../contracts/domains/habitat/land_cover/uncertainty.md`
- `../../../../contracts/domains/habitat/land_cover/model_run_receipt.md`
- `../../../../schemas/contracts/v1/domains/habitat/land_cover/`
- `../../../../policy/domains/habitat/land_cover/`
- `../../../../policy/sensitivity/habitat/`
- `../../../../pipelines/domains/habitat/land_cover/`
- `../../../../pipeline_specs/habitat/land_cover/`
- `../../../../data/registry/sources/habitat/`
- `../../../../release/manifests/habitat/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy `LandCoverChangeSummary` examples for positive-path and negative-path checks;
- toy observation-pair, source-vintage, class-scheme, crosswalk, valid-pixel-footprint, threshold-profile, class-delta, transition-matrix, and uncertainty examples;
- toy source-role, evidence-ref, rights-state, sensitivity-state, review-state, release-state, correction-state, and rollback-state examples;
- toy renderer, Evidence Drawer, Focus Mode, governed API, threshold, topology, policy, and pipeline dry-run examples;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real Habitat records, real source exports, live upstream fetch results, credentials, lifecycle data, real EvidenceBundles, proof packs, run receipts, release manifests, correction notices, review records, implementation code, public API material, public map material, public tiles, source raster data, habitat quality claims, occurrence claims, regulatory designation truth, hydrology truth, soil truth, hazards truth, land/title truth, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy observation IDs, toy source IDs, toy analysis-unit IDs, toy class-scheme refs, toy threshold-profile IDs, toy evidence references, toy timestamps, toy hashes, and toy geometries unless a bounded check explicitly requires a more realistic shape.
- Make summary posture explicit: observation pair, analysis unit, source-vintage comparison, class-scheme posture, crosswalk posture, threshold posture, public-safe derivative, candidate, invalid, or expected output.
- Keep source role, evidence state, source vintage, rights state, sensitivity state, valid-pixel support, threshold state, class-scheme state, topology state, policy state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Prefer public-safe generalized geometry. Do not include geometry that could reasonably be mistaken for sensitive real-world data.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `observation-pair-valid`, `source-vintage-valid`, `class-scheme-valid`, `crosswalk-valid`, `threshold-valid`, `evidence-resolved`, `rights-cleared`, `policy-admissible`, `citation-safe`, `release-safe`, and `renderer-safe` as separate checks.
- Do not treat change-summary fixtures as source authority, evidence authority, threshold policy authority, schema authority, implementation proof, release state, public-map authority, tile authority, habitat quality proof, occurrence proof, or published output.

## Expected change-summary fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic change summary with two toy observations, matching class scheme, and toy threshold profile | Valid input or `ANSWER` output | Demonstrates positive path without becoming source truth. |
| Missing baseline or comparison observation ID | Validation failure or `ERROR` | Observation pair must be explicit. |
| Source vintages collapsed or missing | `ABSTAIN` or validation failure | Time and source-vintage discipline remain visible. |
| Different class schemes without reviewed crosswalk | `ABSTAIN` or validation failure | Recode/crosswalk must be explicit. |
| Change summary presented as source raster or observation | `ABSTAIN` or validation failure | Summary does not replace source artifacts or observations. |
| Change summary presented as habitat quality or occurrence proof | `ABSTAIN` | Downstream claims require their own owning contracts and evidence. |
| Public derivative missing release/correction/rollback posture | Validation failure or review-required output | Public use requires governed release posture. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the semantic-contract review, future schema check, threshold check, class-scheme check, source-vintage check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, policy check, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/land_cover/change_summary.md`.
- Land-cover sublane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Schema alignment: NEEDS VERIFICATION because the contract reports the paired schema is still a permissive scaffold.
- Parent habitat fixture README: present but still a greenfield stub during this update.
- Sibling fixture alignment: NEEDS VERIFICATION against populated `golden/`, `invalid/`, `ecoregions/`, and `habitat_fauna_thin_slice/` READMEs.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, threshold checks, class-scheme checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.
