<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/soil/support-types
title: Soil Support Types
type: standard
version: v1
status: draft
owners: TODO-VERIFY
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO-VERIFY
related: [kfm://doc/TODO-VERIFY-uuid]
tags: [kfm, soil, support-type, evidence]
notes: [Companion taxonomy for docs/domains/soil/README.md.]
[/KFM_META_BLOCK_V2] -->

# Soil Support Types

This file defines the support-type taxonomy referenced by the soil domain README.

## Normative intent

A `support_type` identifies **how a claim is supported**, not just where data came from.

## Types and boundaries

| support_type | Primary use | Must include | Must not imply |
|---|---|---|---|
| `authoritative_static_soil` | static survey-backed map/component/horizon facts | source/version + stable soil keys | near-real-time moisture state |
| `authoritative_static_soil_query` | query-derived tabular soil facts | reproducible query identity (`query_hash`) | untracked ad hoc SQL |
| `gridded_derivative_soil` | gridded convenience/derivative surfaces | derivative lineage and resolution | replacement for canonical survey lineage |
| `station_soil_moisture` | in-situ moisture observations | station identity, depth, timestamp, units | statewide static soil classification |
| `reference_station_soil_climate` | climate/reference-network station context | network/source and QC behavior | same semantics as all other station feeds |
| `satellite_soil_moisture_grid` | satellite/grid moisture context | product version, grid/time window, QA fields | point-level station precision |
| `profile_soil_evidence` | pedon/profile/horizon analytical support | profile keys and method context | generalized map-wide truth |
| `soil_interpretation` | interpreted classes/ratings | explicit interpretation method/basis | raw source table row |
| `governed_change_evidence` | change-detection and promotion support | prior/current identity and reason codes | direct publication guarantee |

## Finite outcomes guidance

When support is insufficient or unsafe:

- **ABSTAIN** when evidence is missing,
- **DENY** when policy/provenance constraints are violated,
- **ERROR** for invalid request/runtime failures.

## Modeling guidance

- Keep `support_type` explicit in every published payload.
- Do not collapse multiple support types into one layer without visible provenance.
- If a value blends sources, declare the blend rule and preserve contributing references.
