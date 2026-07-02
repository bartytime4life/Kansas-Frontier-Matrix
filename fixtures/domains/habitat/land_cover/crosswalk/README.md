# Habitat land-cover crosswalk fixtures

`fixtures/domains/habitat/land_cover/crosswalk/`

Status: draft / fixture lane / `CoverClassCrosswalk` examples.

This directory is for small synthetic Habitat land-cover crosswalk fixtures. A crosswalk fixture describes a toy, reviewed mapping between two toy `ClassSchemeProfile` records. Its purpose is to prove that class recoding is explicit, versioned, citable, and checked rather than hidden in a renderer, notebook, or downstream summary.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, Habitat truth, or published artifacts.

## Contract posture

The `CoverClassCrosswalk` contract defines a crosswalk as a reviewed, versioned, citable mapping between two class schemes. It is not a class scheme, observation, change summary, renderer style, public layer, policy decision, release manifest, or source truth by itself.

The paired schema is still a permissive scaffold. This fixture lane can support future checks, but it does not prove schema enforcement, crosswalk authority, pipeline implementation, or release readiness.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The Habitat land-cover sublane lists `fixtures/domains/habitat/land_cover/` as the proposed fixture home for land-cover examples. The root fixture README says fixture corpora are not canonical truth and RAW, WORK, and QUARANTINE data do not belong here.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../class_scheme/` | Crosswalk fixtures depend on source and target class-scheme fixtures. |
| `../change_summary/` | Change-summary fixtures may cite crosswalk fixtures. |
| `../../golden/` | Stable expected outputs for crosswalk inputs may be paired there. |
| `../../invalid/` | Negative-path crosswalk inputs may be paired there when useful. |
| `../../../../../contracts/domains/habitat/land_cover/crosswalk.md` | Semantic meaning; this lane supplies examples only. |
| `../../../../../schemas/contracts/v1/domains/habitat/land_cover/crosswalk.schema.json` | Expected machine-shape home; enforcement remains bounded by contract status. |
| `../../../../../pipelines/domains/habitat/land_cover/` | Executable processing home; this lane is not pipeline code. |
| `../../../../../release/manifests/habitat/` | Release home; fixtures do not approve publication. |

## Related references

- `../class_scheme/README.md`
- `../change_summary/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../../../../docs/domains/habitat/sublanes/land_cover.md`
- `../../../../../contracts/domains/habitat/land_cover/crosswalk.md`
- `../../../../../contracts/domains/habitat/land_cover/class_scheme.md`
- `../../../../../contracts/domains/habitat/land_cover/change_summary.md`
- `../../../../../schemas/contracts/v1/domains/habitat/land_cover/`
- `../../../../../pipelines/domains/habitat/land_cover/`
- `../../../../../release/manifests/habitat/`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy source-scheme and target-scheme references;
- toy mapping tables and mapping digests;
- toy directionality, reviewer state, mapping kind, lossiness, confidence, coverage, allowed-use, and denied-use examples;
- toy evidence-ref, rights-state, review-state, release-state, correction-state, and rollback-state examples;
- paired expected outputs in `../../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, run receipts, release manifests, implementation code, public API material, public map material, public tiles, source authority, class-scheme authority, observation truth, change-summary truth, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy IDs, toy version labels, toy class codes, toy mapping rows, toy evidence references, toy timestamps, and toy hashes.
- Make mapping posture explicit: source scheme, target scheme, directionality, mapping version, class coverage, lossiness, allowed use, denied use, candidate, invalid, or expected output.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, source-scheme validity, target-scheme validity, directionality, coverage, lossiness, evidence, citation, release, and renderer checks separate.
- Do not treat fixture success as evidence closure, source authority, schema authority, implementation proof, release state, public-map authority, tile authority, or published output.

## Expected crosswalk fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Synthetic reviewed crosswalk between two toy class schemes | Valid input | Demonstrates explicit mapping without silent recode. |
| Missing source or target scheme ID | Validation failure | Both schemes must be explicit. |
| Directionality missing | Review-required output | Reverse mapping is not automatic. |
| Many-to-one mapping presented as lossless | Validation failure | Lossiness must be visible. |
| Crosswalk used as class scheme | Validation failure | Schemes define vocabularies; crosswalks map between them. |
| Crosswalk used as land-cover observation | Validation failure | Observations apply schemes to space/time. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the contract review, schema check, class-scheme check, mapping-coverage check, directionality check, lossiness check, renderer check, governed-API test, Evidence Drawer test, Focus Mode test, or pipeline dry-run that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Contract alignment: PARTIALLY VERIFIED against `contracts/domains/habitat/land_cover/crosswalk.md`.
- Land-cover sublane alignment: PARTIALLY VERIFIED against `docs/domains/habitat/sublanes/land_cover.md`.
- Schema alignment: NEEDS VERIFICATION because the contract reports the paired schema is still a permissive scaffold.
- Class-scheme sibling alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/land_cover/class_scheme/README.md`.
- Change-summary sibling alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/land_cover/change_summary/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, class-scheme checks, mapping checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, pipeline dry-runs, schema checks, and policy checks.
- Tests and validators: NOT RUN.
