# Flora PLANTS source fixtures

`fixtures/domains/flora/sources/plants/`

Status: draft / fixture lane / PLANTS-source example support.

This directory is for small synthetic USDA PLANTS-style Flora source fixture examples used by source-admission checks, source-role checks, taxonomy/crosswalk checks, watcher dry-runs, governed API examples, Evidence Drawer examples, Focus Mode examples, and documentation dry-runs. These fixtures may represent toy PLANTS-like source descriptors, source snapshots, source-head metadata, taxonomy-symbol examples, state/county distribution examples, or refusal cases, but they are not real USDA PLANTS records and must not be treated as source truth, catalog truth, release proof, or publication state.

These files are examples only. They are not authoritative project records, source records, live upstream payloads, EvidenceBundles, registry entries, policy decisions, review approvals, release state, public API material, public map material, public tiles, or published artifacts.

## Source posture

Repository evidence includes a proposed Flora source-registry placeholder at `data/registry/sources/flora/usda_plants.yaml`. That file is marked `PROPOSED` and notes that it was created from the current docs/domain inventory.

Repository evidence also includes the USDA PLANTS catalog page. That page describes USDA PLANTS as a Flora source and states that the authoritative `SourceDescriptor` belongs in `data/registry/sources/`, not in the catalog page. It also marks endpoint and cadence specifics as `NEEDS VERIFICATION`.

This fixture lane is not the authoritative descriptor. It is only for synthetic source examples that can exercise PLANTS-like behavior before real registry records, source payloads, EvidenceBundles, policy decisions, or release artifacts are involved.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fixture examples, not governed lifecycle data. It is not a `data/registry/`, `data/raw/`, `data/work/`, `data/quarantine/`, `policy/`, `schemas/`, `contracts/`, `connectors/`, `release/`, proof, or publication root.

The root fixture README states that fixtures are operational/runtime examples, not canonical truth, and that RAW, WORK, or QUARANTINE data does not belong here. The Flora source-descriptor fixture README also limits source-descriptor fixtures to synthetic examples that are not registry authority, source data, proof, policy, release authority, public API material, or published output. This README inherits those boundaries.

## Related references

- `../../README.md`
- `../../source_descriptors/README.md`
- `../../plants_drift/README.md`
- `../../plant_taxon/README.md`
- `../../evidence_bundles/README.md`
- `../../golden/README.md`
- `../../invalid/README.md`
- `../../../../README.md`
- `../../../../../data/registry/sources/flora/usda_plants.yaml`
- `../../../../../data/registry/sources/flora/README.md`
- `../../../../../docs/sources/catalog/usda/usda-plants.md`
- `../../../../../docs/domains/flora/SOURCE_REGISTRY.md`
- `../../../../../docs/domains/flora/SOURCE_ROLES.md`
- `../../../../../docs/domains/flora/CROSSWALKS.md`
- `../../../../../docs/domains/flora/DATA_LIFECYCLE.md`
- `../../../../../connectors/usda/plants/README.md`
- `../../../../../connectors/usda-plants/README.md`
- `../../../../../pipeline_specs/flora/plants_drift_watcher.yaml`
- `../../../../../pipeline_specs/watchers/plants_drift.yaml`
- `../../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.json`, `*.yaml`, `*.yml`, `*.jsonl`, or `*.md` examples;
- toy PLANTS-like source descriptor examples for positive-path and negative-path checks;
- toy source-head metadata examples such as version, digest, retrieval time, ETag, Last-Modified, content-length, or snapshot label;
- toy taxon-symbol, scientific-name, family, native-status, growth-habit, wetland-status, state-distribution, or county-distribution examples;
- examples that keep source identity, source role, rights posture, cadence, attribution, source version, freshness, taxonomy identity, distribution support, evidence state, review state, and release state separate;
- examples that prove source data is not silently upgraded into occurrence proof, public-release approval, or management authority;
- paired expected outputs in `../../golden/` when behavior becomes a stable regression anchor.

## Exclusions

Do not use this lane for real USDA PLANTS payloads, live endpoint samples, credentials, lifecycle data, source registry authority, release artifacts, proof packs, policy rules, implementation code, public API payloads, public map data, public tiles, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, and reviewable.
- Use toy source IDs, toy PLANTS symbols, toy taxon names, toy URLs, toy licenses, toy timestamps, toy hashes, and toy evidence references unless a bounded check explicitly requires a more realistic shape.
- Make source posture explicit: candidate, active, inactive, stale, superseded, restricted, denied, synthetic, or review-required.
- Keep taxonomy identity, distribution support, source role, rights state, cadence state, freshness state, review state, release state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `taxonomy-resolved`, `crosswalk-resolved`, `freshness-known`, `registry-admissible`, and `release-safe` as separate checks.
- Do not treat PLANTS source fixtures as taxonomic authority, evidence, source authority, registry authority, implementation proof, release approval, or published output.

## Expected fixture examples

| Scenario | Expected posture | Notes |
|---|---|---|
| Complete synthetic PLANTS source descriptor | Valid descriptor-style output | Demonstrates positive path without becoming registry authority. |
| Missing source version or source ID | Validation failure or `ERROR` | Source identity and version must be stable before use. |
| Toy taxonomy symbol renamed | `MaterialChangeReport` or review-required output | Rename handling remains auditable. |
| County distribution example without occurrence support | Contextual or `ABSTAIN` output | Distribution scaffold must not become occurrence proof. |
| Source freshness unknown or stale | `SOURCE_STALE` or review-required output | Freshness state remains visible. |
| Source role unclear | `ABSTAIN` or review-required output | Source-role anti-collapse remains visible. |
| Fixture asks for direct publication | Validation failure or deny output | Fixtures and registry examples do not publish. |

## Maintenance notes

- Update this README when payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each fixture to the source-admission check, taxonomy/crosswalk check, source-role test, watcher dry-run, governed-API test, Evidence Drawer test, Focus Mode test, or documentation example that consumes it.
- If a fixture becomes stable enough to anchor a regression check, pair it with an expected output and document the consumer.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, move it out of this lane, quarantine it through the governed lifecycle, and record the correction path.

## Verification status

- Target README: populated from empty placeholder content.
- Fixture payload inventory: no payloads verified in this directory during this update.
- PLANTS registry alignment: PARTIALLY VERIFIED against the proposed `data/registry/sources/flora/usda_plants.yaml` placeholder.
- Catalog alignment: PARTIALLY VERIFIED against `docs/sources/catalog/usda/usda-plants.md`.
- Fixture boundary alignment: PARTIALLY VERIFIED against `fixtures/README.md` and `fixtures/domains/flora/source_descriptors/README.md`.
- Consumer alignment: NEEDS VERIFICATION against source-admission checks, source-role checks, taxonomy/crosswalk checks, watcher dry-runs, governed-API tests, Evidence Drawer tests, Focus Mode tests, schema checks, and policy checks.
- Tests and validators: NOT RUN.
