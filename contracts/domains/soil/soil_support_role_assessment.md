<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domain/soil/support-role-assessment/v1
title: SoilSupportRoleAssessment candidate profile
type: semantic-contract
version: 1.0.0
status: proposed-inactive
owning_root: contracts/
responsibility: Distinguish static survey, gridded derivative, station observation, and satellite-grid soil support without allowing one support class to masquerade as another.
truth_posture: cite-or-abstain; PASS proves fixture coherence only
related:
  - ../../../../schemas/contracts/v1/domains/soil/soil_support_role_assessment.schema.json
  - ../../../../fixtures/contracts/v1/domains/soil/soil_support_role_assessment/README.md
  - ../../../../tools/validators/domains/soil/validate_soil_support_role_assessment.py
  - ../../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# `SoilSupportRoleAssessment` candidate profile

> **Status:** `PROPOSED_INACTIVE` · **Decision:** `HOLD` · **Source activation:** none · **Public-use authority:** none

## Purpose

The soil planning source requires KFM to preserve the different knowledge character of static SSURGO/SDA survey support, gridded derivatives, in-situ station observations, and satellite soil-moisture grids. `SoilSupportRoleAssessment` turns that anti-collapse rule into a deterministic, fixture-only candidate profile.

The profile checks whether a synthetic soil support record declares a coherent source family, authority role, geometry support, temporal support, depth interval, measurement, and claim class. It does not contact a source, normalize real soil data, resolve evidence, evaluate policy, activate a connector, write lifecycle data, build a catalog or tile, promote, release, deploy, or publish.

## Support classes

| Support type | Source families | Authority role | Geometry | Permitted claim character |
|---|---|---|---|---|
| `STATIC_SURVEY` | `SSURGO_SDA` | `AUTHORITATIVE_SURVEY` | map-unit polygon | map-unit identity and bounded property estimates |
| `GRIDDED_DERIVATIVE` | `GSSURGO_GNATSGO` | `DERIVED_SURFACE` | grid cell | derived property estimates, never canonical survey identity |
| `STATION_OBSERVATION` | `KANSAS_MESONET`, `NRCS_SCAN`, `NOAA_USCRN` | `IN_SITU_OBSERVATION` | station point | point soil-moisture observation at declared time and depth |
| `SATELLITE_GRID` | `NASA_SMAP` | `REMOTE_SENSING_OBSERVATION` | grid cell | grid soil-moisture estimate at declared time, resolution, and depth |

## Deterministic identity

The validator computes RFC 8785 JCS + SHA-256 over the complete candidate except `assessment_id` and `spec_hash`:

```text
spec_hash = sha256(JCS(identity_subject))
assessment_id = "soil-support-role:" + first_24_hex(spec_hash)
```

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The inactive synthetic candidate is locally coherent and retains every authority hold. |
| `ABSTAIN` | The support class is coherent but freshness remains unresolved. |
| `DENY` | Source role, support class, geometry, time, depth, claim, or authority invariants fail. |
| `ERROR` | Input, schema, hashing, identity, or fixture execution fails. |

## Authority boundary

Every candidate remains `review_state: HOLD`, `public_use_allowed: false`, and all effect flags `false`. A passing result is not a `SourceDescriptor`, `EvidenceBundle`, policy decision, promotion decision, release manifest, catalog item, PMTiles artifact, source activation, or publication authorization.
