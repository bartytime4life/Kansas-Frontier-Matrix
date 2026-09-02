<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-soil-mukey-properties
title: MukeyProperties Contract — deterministic SSURGO/SDA map-unit aggregate candidate
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only; no-source-activation; no-publication-authority
owners:
  - OWNER_TBD — Soil domain steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; soil; ssurgo; sda; derived-candidate; support-type-aware; no-network; release-gated
related:
  - ./README.md
  - ./soil_map_unit.md
  - ./soil_component.md
  - ./horizon.md
  - ./component_horizon_join.md
  - ./soil_property.md
  - ../../../schemas/contracts/v1/domains/soil/mukey_properties.schema.json
  - ../../../fixtures/domains/soil/mukey_properties/README.md
  - ../../../tools/validators/domains/soil/mukey_properties/validate_mukey_properties.py
  - ../../../tests/validators/domains/soil/mukey_properties/test_mukey_properties.py
  - ../../../pipeline_specs/soil/support_type_profile.v1.json
notes:
  - "Derived from the supplied New Ideas 3-31-26 soil-baseline proposal and current Soil support-type doctrine."
  - "This is a fixture-only derived-candidate profile. It does not activate NRCS access, resolve EvidenceBundles, execute policy, promote, release, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MukeyProperties Contract

> `MukeyProperties` is a deterministic, MUKEY-scoped **derived candidate** that preserves the source hierarchy `SoilMapUnit → SoilComponent → Horizon` while exposing a bounded set of reproducible map-unit metrics. It is not raw SSURGO truth, a current field condition, an interpretation, a release decision, or a public layer.

**Status:** `PROPOSED_INACTIVE` / fixture-only  
**Profile:** `kfm.soil.mukey-properties.v1`  
**Machine shape:** `schemas/contracts/v1/domains/soil/mukey_properties.schema.json`  
**Validator:** `tools/validators/domains/soil/mukey_properties/validate_mukey_properties.py`

## Evidence-led rationale

The supplied `New Ideas 3-31-26.pdf` recommends a governed Kansas SSURGO/SDA baseline that:

- keeps `MUKEY`, `COKEY`, and `CHKEY` lineage intact;
- treats `Map Unit → Component → Horizon` as a truth-preserving hierarchy;
- computes depth-weighted and component-weighted properties rather than using only the dominant component;
- validates component-percent closure, horizon continuity, physical plausibility, and reproducible hashes;
- keeps authoritative source evidence distinct from derived aggregates; and
- fails closed when critical support or hydric-classification currency is unresolved.

Current repository evidence already defines `authoritative_static_soil` for NRCS SSURGO/SDA support and keeps derived projections subordinate. This contract implements the smallest missing machine-enforceable slice: one synthetic aggregate shape, fixtures, deterministic validator, tests, and read-only CI.

## Responsibility and placement

| Concern | Owning root | Rule |
|---|---|---|
| Object meaning | `contracts/domains/soil/` | This contract defines semantics and limits. |
| Machine shape | `schemas/contracts/v1/domains/soil/` | Closed Draft 2020-12 schema. |
| Synthetic examples | `fixtures/domains/soil/mukey_properties/` | No-network, non-authoritative test inputs. |
| Validator | `tools/validators/domains/soil/mukey_properties/` | Deterministic local checks only. |
| Tests | `tests/validators/domains/soil/mukey_properties/` | Positive, negative, and no-network proof. |
| CI orchestration | `.github/workflows/` | Read-only exact-fixture validation. |
| Source activation, lifecycle bytes, evidence, policy, release, publication | Their existing responsibility roots | Explicitly outside this object family. |

ADR-0029 adopts Directory Rules v2. These paths reuse existing responsibility roots and create no parallel schema, contract, policy, source, registry, proof, release, or publication authority.

## Meaning and boundaries

A conforming candidate binds:

- one `mukey` and exact `record_id`;
- one NRCS source family (`nrcs_ssurgo` or `nrcs_sda`) with the matching source role;
- a non-placeholder source version, query hash, retrieval time, and evidence references;
- one or more uniquely keyed components with component percentages;
- uniquely keyed, ordered, contiguous horizons carrying depth and physical-property context;
- explicit aggregation windows and method;
- recomputable map-unit metrics;
- hydric classification status and criteria reference posture;
- an exact canonical SHA-256 over the candidate content; and
- explicit non-effects that deny public use and all authority-bearing transitions.

It must not be used as:

- a replacement for SSURGO/SDA source evidence or relational tables;
- proof that a source query, package, geometry, or EvidenceBundle was resolved;
- a current station, field, parcel, producer, or management condition;
- legal, engineering, conservation-compliance, hazard, agronomic, or operational advice;
- a gridded gSSURGO/gNATSGO product;
- a PolicyDecision, ReviewRecord, PromotionDecision, ReleaseManifest, proof, or published artifact; or
- a public API, MapLibre layer, Focus Mode answer, or AI authority.

## Aggregation profile v1

The fixture profile fixes its method rather than allowing each record to loosen validation:

```text
root zone: 0–100 cm
surface organic-matter window: 0–5 cm
component closure: 99–101 percent
comparison tolerance: 0.000001
method: arithmetic depth weighting, then component-percent weighting
```

For numeric property `p`, component `c`, and depth interval `[a,b)`:

```text
depth_average(c, p, a, b)
  = Σ(p_horizon × overlap_cm) / Σ(overlap_cm)

map_unit_average(p)
  = Σ(depth_average_component × component_pct) / Σ(component_pct)
```

This arithmetic method is a **PROPOSED fixture profile**, not a claim that it is the correct scientific transfer function for every SSURGO property. In particular, the validator does not invent a Ksat-to-hydrologic-group threshold. `hydrologic_group` remains source-carried from `muaggatt` under the declared basis `source_muaggatt`.

## Required derived metrics

| Field | Scope | Unit / scheme |
|---|---|---|
| `root_zone_clay_pct` | 0–100 cm, depth then component weighted | percent |
| `root_zone_ksat_um_s` | 0–100 cm, depth then component weighted | micrometres per second |
| `root_zone_available_water_capacity_fraction` | 0–100 cm, depth then component weighted | fraction 0–1 |
| `surface_organic_matter_pct` | 0–5 cm, depth then component weighted | percent |
| `hydrologic_group` | source-carried map-unit interpretation | A, B, C, D, or dual group |
| `component_pct_total` | sum of component percentages | percent |

## Hydric currency rule

The source packet warns that hydric classification criteria may change. This contract avoids encoding an unverified date as timeless truth:

- `CURRENT` requires a non-null `criteria_ref` identifying the criteria or source version used;
- without such a reference, the candidate must use `NEEDS_VERIFICATION`;
- the field does not authorize wetland delineation, jurisdictional determination, compliance evidence, or public release.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed shape, identity, lineage, continuity, ranges, recomputation, and hash checks passed for the synthetic candidate. |
| `ABSTAIN` | Critical property or root/surface coverage is incomplete; the validator cannot recompute the claimed metric. |
| `DENY` | The candidate is contradictory, non-canonical, physically implausible, hash-mismatched, authority-seeking, or otherwise invalid. |
| `ERROR` | The validator could not read or safely evaluate the input or schema. |

A passing result proves only fixture-profile conformance. It does not prove source truth, evidence closure, policy approval, review, release, publication, or fitness for a real-world decision.

## Validation invariants

- `record_id` must equal `soil-mukey-properties:<mukey>`.
- SSURGO and SDA source-family/source-role pairs must match.
- `COKEY` and `CHKEY` values are unique in one candidate.
- component percentages total 99–101 percent and match `derived.component_pct_total`.
- horizons are sorted, non-overlapping, gap-free, and cover the required windows.
- sand and clay remain within 0–100 percent and their sum does not exceed 100 percent.
- organic matter remains within 0–20 percent; Ksat is positive; available-water capacity is 0–1.
- every declared derived metric matches deterministic recomputation within tolerance.
- evidence references are sorted and unique.
- the canonical content hash is non-placeholder and exact.
- public-use and authority-bearing flags remain false.

## Rollout and rollback

This slice is inactive and fixture-only. It introduces no source credentials, network calls, live query, database migration, lifecycle transition, catalog item, release candidate, API route, tile, or published output.

Rollback is one commit revert. Removing the additive contract, schema, fixtures, validator, tests, workflow, and generated receipt restores the prior repository state. No source deactivation, data reprocessing, release withdrawal, cache invalidation, or public correction is required.

## Open verification

- Current NRCS endpoints, fields, package versions, source terms, and hydric criteria.
- Accepted real-data aggregation rules, especially Ksat and categorical interpretations.
- Whether partial components or incomplete horizons should produce `ABSTAIN`, `QUARANTINE`, or a distinct candidate state in a future live pipeline.
- EvidenceBundle resolution, geometry binding, source-version pinning, policy, review, promotion, release, correction, and rollback for operational records.
- Parent index updates and broader Soil schema closure beyond this bounded object family.
