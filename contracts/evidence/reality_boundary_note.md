# RealityBoundaryNote Contract

Status: PROPOSED implementation contract.

A `RealityBoundaryNote` makes the representation-to-reality boundary explicit for synthetic, reconstructed, modeled, interpolated, generalized, or otherwise mediated spatial carriers. It is required when a 3D or synthetic surface could reasonably be mistaken for direct observation.

Required semantics:
- finite `representation_kind`: `OBSERVED`, `MODELED`, `SYNTHETIC`, `RECONSTRUCTED`, `INTERPOLATED`, `GENERALIZED`;
- finite `reality_posture`: `DIRECT_EVIDENCE`, `DERIVED_WITH_LIMITS`, `ILLUSTRATIVE_ONLY`, `UNSUPPORTED`;
- explicit `evidence_refs`, `source_roles`, `transforms`, limitations, spatial/temporal scope, and correction lineage;
- `OBSERVED` cannot be paired with synthetic/reconstruction transforms;
- synthetic or reconstructed carriers cannot claim `DIRECT_EVIDENCE`;
- `ILLUSTRATIVE_ONLY` and `UNSUPPORTED` cannot be used as evidence authority for a consequential public claim.

This object is a trust-visible annotation and validation boundary. It does not authorize 3D admission, policy, release, or publication.