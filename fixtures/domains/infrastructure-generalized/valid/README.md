# Infrastructure-generalized — valid fixtures

`fixtures/domains/infrastructure-generalized/valid/`

Status: draft / fixture lane, first payloads added per the parent README's
[Accepted material](../README.md#accepted-material) list.

Small, wholly synthetic, public-safe examples of generalized infrastructure
objects at sensitivity tiers T0–T1 only (per
[`docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md)
§7.1). No T3/T4 (restricted/denied) payloads live in this lane — see
[`../invalid/`](../invalid/README.md) for how those are exercised safely.

| File | Object family | Sensitivity tier | Consumer (intended) | Expected outcome |
|---|---|---|---|---|
| `valid_1_generalized_service_area.json` | `ServiceArea` | T0–T1 | Renderer / release-readiness smoke check. | Passes; aggregate footprint only, no facility-level detail. |
| `valid_2_generalized_asset_footprint.json` | `InfrastructureAsset` (generalized footprint) | T1 | Redaction/generalization helper. | Passes; footprint is coarsened and cites a synthetic `RedactionReceipt`. |

Shared posture:

- All identifiers, geometries, operators, and receipt references are synthetic placeholders.
- Geometry is a coarse bounding grid cell, never an exact facility, node, or segment location.
- A passing check proves only the declared shape/tier expectation, not real infrastructure truth, policy approval, or release readiness.

See also: [`../README.md`](../README.md) · [`../invalid/README.md`](../invalid/README.md) · [`../../settlements-infrastructure/README.md`](../../settlements-infrastructure/README.md)
