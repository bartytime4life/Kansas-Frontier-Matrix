# Geology & Natural Resources Schema Index

Documentation index for machine contracts that should eventually support this lane.

## Contract families

| Family | Purpose | Minimum fixture expectation |
| --- | --- | --- |
| `source_descriptor` | Captures publisher, source role, rights, cadence, and scope for source admission. | 1 valid + 1 invalid source descriptor fixture. |
| `geologic_unit` | Represents map units, nomenclature, rank, age, and interpreted boundaries. | 1 interpreted-unit valid fixture + 1 invalid role/scale fixture. |
| `structure_feature` | Fault/fold/fracture/landform features with certainty and method context. | 1 observed/inferred split fixture pair. |
| `borehole_or_subsurface_reference` | Well/borehole/core references with geometry sensitivity controls. | 1 public-safe fixture + 1 exact-public leakage invalid fixture. |
| `resource_claim` | Occurrence/resource/reserve/extraction/reclamation semantics without collapsing categories. | 1 classification-complete valid fixture + 1 under-specified invalid fixture. |
| `layer_descriptor` | Public map layer metadata and trust cues linking layer to release/evidence/policy states. | 1 publishable layer fixture + 1 missing evidence reference invalid fixture. |
| `evidence_bundle_ref` | Runtime lookup object that ties rendered assertions to supporting evidence. | 1 resolvable fixture + 1 unresolved fixture expecting fail-closed behavior. |

## Proposed schema homes

- Primary candidate: `schemas/contracts/v1/geology/`.
- Compatibility note: if a different repo-native home is authoritative, document migration/supersession in an ADR before dual-writing.

## Validation expectations

- Schema validation must fail closed on missing source role, unknown rights, ambiguous geometry role, or absent evidence references for publishable surfaces.
- Fixtures should remain no-network and deterministic.
- Contract changes should trigger policy and runtime-proof tests in addition to schema tests.
