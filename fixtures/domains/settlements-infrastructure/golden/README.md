# Settlements/Infrastructure golden fixtures

`fixtures/domains/settlements-infrastructure/golden/`

Status: draft / fixture lane, first payload added. `PLACEHOLDER.md` is
retained because
[`.github/workflows/domain-settlements-infrastructure.yml`](../../../../.github/workflows/domain-settlements-infrastructure.yml)
checks for its presence.

| File pair | Scenario | Expected outcome |
|---|---|---|
| `settlement_identity_lookup.input.json` / `.expected.json` | Lookup of the synthetic `Settlement` identity in `../valid/valid_1_settlement.json`. | `ANSWER` — returns the generalized-point identity envelope with `sensitivity_tier: T1`. |

See also: [`../README.md`](../README.md) · [`../valid/README.md`](../valid/README.md) · [`../domain_feature_identity/README.md`](../domain_feature_identity/README.md)
