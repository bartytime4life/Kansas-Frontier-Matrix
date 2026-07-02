# Flora source-family fixtures

`fixtures/domains/flora/sources/`

Status: draft / fixture lane / source-family coordination.

This directory coordinates small synthetic Flora source-family fixture examples. Child directories may hold toy source-family examples for source admission, source-role checks, taxonomy and crosswalk checks, watcher dry-runs, governed API examples, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs.

These files are examples only. They are not authoritative project records, source records, live upstream payloads, EvidenceBundles, registry entries, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Relationship to child lanes

Use this parent directory to group source-specific fixture lanes, such as:

| Child lane | Purpose | Status |
|---|---|---|
| `plants/` | Synthetic USDA PLANTS-style Flora source fixtures. | Present README populated. |

Future child lanes may be added for GBIF, iNaturalist, herbarium, NatureServe, ECOS, restoration, vegetation, invasive-plant, phenology, or other Flora source families only when they remain synthetic and fixture-scoped.

## Source posture

The source-specific fixture lanes under this directory are not the authoritative Flora source registry. Authoritative source-admission records belong under governed registry roots such as `data/registry/sources/flora/`, and source documentation belongs under `docs/sources/` or `docs/domains/flora/` as appropriate.

The existing `plants/` child lane is grounded in a proposed `usda_plants` source-registry placeholder and the USDA PLANTS catalog page, but it remains only a synthetic fixture lane. It does not activate a source, prove endpoint behavior, approve a live descriptor, or create publication authority.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/registry/`, `data/raw/`, `data/work/`, `data/quarantine/`, `policy/`, `schemas/`, `contracts/`, `connectors/`, `release/`, proof, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Flora source-descriptor fixture README limits source-descriptor fixtures to synthetic examples that are not registry authority, source data, proof, policy, release authority, public API material, or published output. This README inherits those boundaries.

## Related references

- `../README.md`
- `../source_descriptors/README.md`
- `../plants_drift/README.md`
- `../plant_taxon/README.md`
- `../flora_occurrence/README.md`
- `../evidence_bundles/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `plants/README.md`
- `../../../README.md`
- `../../../../data/registry/sources/flora/README.md`
- `../../../../data/registry/sources/flora/usda_plants.yaml`
- `../../../../docs/sources/catalog/usda/usda-plants.md`
- `../../../../docs/domains/flora/SOURCE_REGISTRY.md`
- `../../../../docs/domains/flora/SOURCE_ROLES.md`
- `../../../../docs/domains/flora/SOURCE_FAMILIES.md`
- `../../../../docs/domains/flora/CROSSWALKS.md`
- `../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../connectors/`
- `../../../../pipeline_specs/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- source-family subdirectories with README files and small synthetic fixture payloads;
- small synthetic `*.json`, `*.yaml`, `*.yml`, `*.jsonl`, or `*.md` examples;
- toy source-descriptor, source-head, source-version, source-role, source-family, cadence, attribution, rights posture, freshness, and material-change examples;
- toy taxonomy, occurrence, specimen, vegetation, invasive-plant, phenology, restoration, or watcher-oriented source examples;
- examples that prove source metadata is not silently upgraded into occurrence proof, taxonomic authority, management authority, public-release approval, or published map output;
- paired expected outputs in `../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real upstream source payloads, live endpoint samples, credentials, lifecycle data, source registry authority, release artifacts, proof packs, policy rules, connector implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Place source-specific examples in a named child lane, not loose at this parent unless a fixture truly spans source families.
- Use toy source IDs, toy source names, toy URLs, toy licenses, toy timestamps, toy hashes, toy taxa, toy geographies, and toy evidence references unless a bounded check explicitly requires a more realistic shape.
- Keep source identity, source role, source family, rights state, sensitivity state, cadence state, freshness state, review state, release state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `taxonomy-resolved`, `crosswalk-resolved`, `freshness-known`, `registry-admissible`, and `release-safe` as separate checks.
- Do not treat source-family fixtures as source authority, registry authority, evidence, implementation proof, release approval, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Complete synthetic source-family descriptor | Valid descriptor-style output | Demonstrates positive path without becoming registry authority. |
| Missing source identity | Validation failure or `ERROR` | Source identity must be stable before use. |
| Source role unclear | `ABSTAIN` or review-required output | Source-role anti-collapse remains visible. |
| Freshness state unknown or stale | `SOURCE_STALE` or review-required output | Freshness remains visible and stage-bound. |
| Source metadata used as occurrence proof | `ABSTAIN` | Source metadata does not become a biological claim by itself. |
| Fixture asks for direct publication | Validation failure or deny output | Fixtures and registry examples do not publish. |

## Maintenance notes

- Update this README when child source-family lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each child lane to the source-admission check, source-role test, taxonomy/crosswalk check, watcher dry-run, governed-API test, Evidence Drawer test, Focus Mode test, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Child lane inventory: `plants/README.md` verified as present during this update; other child lanes were not inventoried as present.
- Fixture payload inventory: no payloads verified in this directory during this update.
- Fixture boundary alignment: PARTIALLY VERIFIED against `fixtures/README.md`, `fixtures/domains/flora/source_descriptors/README.md`, and `fixtures/domains/flora/sources/plants/README.md`.
- Consumer alignment: NEEDS VERIFICATION against source-admission checks, source-role checks, taxonomy/crosswalk checks, watcher dry-runs, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, and policy checks.
- Tests and validators: NOT RUN.
