# Settlements/Infrastructure — `domain_feature_identity` fixtures

`fixtures/domains/settlements-infrastructure/domain_feature_identity/`

Status: draft / fixture lane, first payloads added at the `fixtures_root` path
named by
[`schemas/contracts/v1/domains/settlements-infrastructure/domain_feature_identity.schema.json`](../../../../schemas/contracts/v1/domains/settlements-infrastructure/domain_feature_identity.schema.json).

The paired schema is currently a **PROPOSED stub** that requires only `id`
and allows additional properties. These fixtures follow the fuller
**Recommended semantics** field list in
[`contracts/domains/settlements-infrastructure/domain_feature_identity.md`](../../../../contracts/domains/settlements-infrastructure/domain_feature_identity.md#recommended-semantics)
so the fixture shape is ready ahead of schema hardening; they do not claim the
schema currently enforces these fields.

| File | Object family | Scenario | Expected outcome |
|---|---|---|---|
| `valid_settlement.json` | `Settlement` (GhostTown role) | Minimal identity envelope carrying source, temporal scope, and digest per the identity recipe. | Passes the current permissive schema (`id` present); matches recommended semantics. |
| `valid_infrastructure_asset.json` | `InfrastructureAsset` | Identity envelope for a generalized-footprint asset at sensitivity tier T1. | Passes the current permissive schema; matches recommended semantics. |
| `invalid_collapsed_object_family.json` | — | Identity omits `object_family` and `feature_role`, so a `Settlement` and an `InfrastructureAsset` cannot be distinguished. | Fails invariant 3 ("Object family is identity-significant") once a reviewed schema enforces it; **passes today's permissive stub**, which is itself evidence the stub needs hardening. |
| `invalid_collapsed_object_family.expected_error.txt` | — | Expected diagnostic once the schema/validator named in `x-kfm` is implemented. | Documents the target failure so it is not lost when the validator is written. |

Shared posture:

- All `id`, `source_id`, `evidence_ref`, and digest values are synthetic placeholders.
- These fixtures name an identity envelope only; they are not the object payload, a policy decision, or a release manifest.
- `invalid_collapsed_object_family.json` intentionally still passes today's stub schema — this is documented, not hidden, so the fixture cannot be mistaken for proof that identity collapse is currently rejected.

See also: [`../README.md`](../README.md) · [`../valid/README.md`](../valid/README.md) · [`../invalid/README.md`](../invalid/README.md)
