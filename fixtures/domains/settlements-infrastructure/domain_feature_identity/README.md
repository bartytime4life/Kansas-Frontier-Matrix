# Settlements/Infrastructure — `domain_feature_identity` fixtures

`fixtures/domains/settlements-infrastructure/domain_feature_identity/`

Status: draft / fixture lane, first payloads added at the `fixtures_root` path
named by
[`schemas/contracts/v1/domains/settlements-infrastructure/domain_feature_identity.schema.json`](../../../../schemas/contracts/v1/domains/settlements-infrastructure/domain_feature_identity.schema.json).

The paired schema is currently a **PROPOSED stub** that requires only `id`
and allows additional properties. The bounded candidate validator at
`tools/validators/domains/settlements-infrastructure/validate_domain_feature_identity.py`
checks family/role separation, source and evidence pointers, a source-native
or normalized name key, temporal scope, and SHA-256 digest syntax. It does not
resolve referenced objects or make sensitivity, policy, or release decisions.
Run it with `python tools/validators/domains/settlements-infrastructure/validate_domain_feature_identity.py fixtures/domains/settlements-infrastructure/domain_feature_identity/*.json`;
the mixed fixture set intentionally exits 1. These fixtures follow the fuller
**Recommended semantics** field list in
[`contracts/domains/settlements-infrastructure/domain_feature_identity.md`](../../../../contracts/domains/settlements-infrastructure/domain_feature_identity.md#recommended-semantics)
so the fixture shape is ready ahead of schema hardening; they do not claim the
schema currently enforces these fields.

| File | Object family | Scenario | Expected outcome |
|---|---|---|---|
| `valid_settlement.json` | `Settlement` (GhostTown role) | Minimal identity envelope carrying source, temporal scope, and digest per the identity recipe. | Passes the bounded validator; SHA-256 fixture values have full 64-digit syntax. |
| `valid_infrastructure_asset.json` | `InfrastructureAsset` | Identity envelope for a generalized-footprint asset at sensitivity tier T1. | Passes the bounded validator; this is not public-release approval. |
| `invalid_collapsed_object_family.json` | — | Identity omits `object_family` and `feature_role`, so a `Settlement` and an `InfrastructureAsset` cannot be distinguished. | Fails the bounded validator with `OBJECT_FAMILY_NOT_DISTINGUISHABLE`; **passes today's permissive stub schema**. |
| `invalid_collapsed_object_family.expected_error.txt` | — | Expected diagnostic for the bounded validator. | Documents the identity-collapse failure; the schema gap remains. |

Shared posture:

- All `id`, `source_id`, `evidence_ref`, and digest values are synthetic placeholders.
- These fixtures name an identity envelope only; they are not the object payload, a policy decision, or a release manifest.
- `invalid_collapsed_object_family.json` intentionally still passes today's stub schema; the bounded validator rejects it. Schema hardening remains a separate proposal.

See also: [`../README.md`](../README.md) · [`../valid/README.md`](../valid/README.md) · [`../invalid/README.md`](../invalid/README.md)
