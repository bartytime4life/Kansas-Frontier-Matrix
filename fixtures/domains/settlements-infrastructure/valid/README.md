# Settlements/Infrastructure — valid fixtures

`fixtures/domains/settlements-infrastructure/valid/`

Status: draft / fixture lane. `PLACEHOLDER.md` is retained because
[`.github/workflows/domain-settlements-infrastructure.yml`](../../../../.github/workflows/domain-settlements-infrastructure.yml)
checks for its presence; the payloads below are the first real content in
this lane.

| File | Object family | Scenario | Expected outcome |
|---|---|---|---|
| `valid_1_settlement.json` | `Settlement` (GhostTown role) | Same synthetic settlement identity as `../domain_feature_identity/valid_settlement.json`, restated as a domain-level positive case. | Passes shape check (`id` present, PROPOSED-schema stub); matches contract-recommended semantics. |
| `valid_2_service_area.json` | `ServiceArea` | Aggregate public-safe service-area footprint at sensitivity tier T0–T1. | Passes shape check; no facility-level detail present. |

Shared posture: all identifiers and geometry references are synthetic. A
passing check proves only the declared shape expectation for that fixture,
not settlement/infrastructure truth, evidence closure, or release readiness.

See also: [`../README.md`](../README.md) · [`../invalid/README.md`](../invalid/README.md) · [`../domain_feature_identity/README.md`](../domain_feature_identity/README.md)
