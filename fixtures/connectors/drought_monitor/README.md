<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-connectors-drought-monitor-readme
title: fixtures/connectors/drought_monitor/ — USDM No-Network Fixtures
type: README
version: v0.1
status: draft
created: 2026-07-28
updated: 2026-07-28
policy_label: public
related:
  - ../../../docs/sources/catalog/drought_monitor/drought-monitor.md
  - ../../../connectors/drought-monitor/README.md
  - ../../contracts/v1/source/source_descriptor/valid/valid_usdm_inactive.json
tags: [kfm, fixtures, drought-monitor, usdm, no-network, synthetic]
notes:
  - "No-network fixtures for the USDM connector lane. Values are synthetic and do not represent real conditions."
  - "These fixtures exist before any live-fetch implementation, as required by the USDM ingestion profile."
[/KFM_META_BLOCK_V2] -->

# `fixtures/connectors/drought_monitor/` — USDM No-Network Fixtures

No-network, synthetic, public-safe fixtures for the U.S. Drought Monitor (USDM) connector lane.

## Contents

| File | Purpose |
|---|---|
| `gis_metadata_response.json` | Representative GIS metadata and polygon feature structure for one USDM weekly release. |
| `statistics_response.json` | Representative aggregate statistics REST service response for one USDM weekly release. |

## Posture

- **No network required.** These fixtures do not require any live connection and must not fetch from external endpoints.
- **Synthetic values.** All field values are synthetic and illustrative. They do not represent real drought conditions.
- **Not source authority.** These fixtures support boundary tests and connector development only. They are not evidence, validated catalog records, policy decisions, or release objects.
- **Public-safe.** No sensitive, restricted, or person-level data is present.

## Artifact separation

GIS polygon products and aggregate statistics are **separate artifacts** even when they share a release week identity. Do not collapse them into one record type. See `connectors/drought-monitor/README.md` for boundary rules.

## Related

- `docs/sources/catalog/drought_monitor/drought-monitor.md` — product documentation
- `connectors/drought-monitor/README.md` — connector boundary and admission contract
- `fixtures/contracts/v1/source/source_descriptor/valid/valid_usdm_inactive.json` — inactive SourceDescriptor candidate
- `tests/schemas/test_usdm_source_descriptor_contracts.py` — boundary tests
