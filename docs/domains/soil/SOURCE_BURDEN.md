<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/soil/source-burden
title: Soil Source Burden
type: standard
version: v1
status: draft
owners: TODO-VERIFY
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO-VERIFY
related: [kfm://doc/TODO-VERIFY-uuid]
tags: [kfm, soil, source-registry, burden, validation]
notes: [Companion to soil domain README.]
[/KFM_META_BLOCK_V2] -->

# Soil Source Burden

Defines what each admitted soil source family must preserve before a candidate can move from RAW/WORK into governed review.

## Shared minimum burden (all soil sources)

Every source family should provide:

1. **Source identity**: source name, publisher, citation text, version/release marker.
2. **Rights posture**: usage terms URL or embedded terms text, plus redistribution posture.
3. **Acquisition context**: endpoint/package path, retrieval timestamp (UTC), and transport metadata.
4. **Normalization contract**: transform version and schema/contract version.
5. **Identity keys**: stable keys sufficient to join/trace records without heuristic guessing.
6. **Quality signals**: source QC/status fields preserved without silent coercion.
7. **Deterministic evidence linkage**: `content_spec_hash`, `run_hash`, and `EvidenceRef` joinability.

## Source-family specifics

| Source family | Required keys | Required context | Deny/quarantine triggers |
|---|---|---|---|
| `ssurgo` | `mukey`; where present `cokey`, `chkey`, `areasymbol`, `musym` | survey/package version, CRS, geometry lineage | missing `mukey`; invalid geometry; unknown CRS |
| `soil_data_access` | `query_hash` + returned row keys (`mukey`/`cokey`/`chkey`) | full SQL/template identity, API/service version | missing query identity; unbounded query; column drift |
| `gssurgo` | raster/grid identity + MUKEY mapping metadata | resolution, package checksum/version | published as if equal to raw SSURGO table truth |
| `gnatsgo` | product version + grid identity | refresh cadence and derivative caveats | provenance omitted; stale version unmarked |
| `kansas_mesonet` | station ID, variable, `depth_cm`, timestamp | station metadata and timezone handling | depth missing; station join fails; stale/unknown QC |
| `scan` | station ID, element, depth, timestamp | access method, QC fields, timezone basis | ambiguous timezone; unit mismatch without conversion |
| `uscrn` | station ID, product ID, timestamp, depth | product version and QC semantics | unknown product variant; dropped QC flags |
| `smap` | product/version, grid cell identity, temporal window | QA mask fields, resolution, latency class | presented as station truth; QA ignored |

## Publication guardrails

A soil candidate is **not publishable** by source presence alone. At minimum:

- validator outputs must be finite (`pass`, `quarantine`, `deny`, `error`),
- evidence must resolve to an `EvidenceBundle`,
- policy checks must pass,
- catalog/proof/release requirements must be satisfied in their dedicated lanes.

## Notes for implementers

- Preserve source-native units in raw fields; add normalized fields explicitly.
- Never infer missing identity keys when a source omits them; quarantine instead.
- Treat source-to-source joins (e.g., SSURGO↔SDA) as explicit, testable transforms.
