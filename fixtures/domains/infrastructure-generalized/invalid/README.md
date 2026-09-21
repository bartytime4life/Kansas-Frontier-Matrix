# Infrastructure-generalized — invalid fixtures

`fixtures/domains/infrastructure-generalized/invalid/`

Status: draft / fixture lane, first payloads added per the parent README's
[Accepted material](../README.md#accepted-material) list.

Safe negative examples that exercise the deny-by-default invariants in
[`docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md)
§7.2. None of these files contain real infrastructure detail; each models a
request or payload that a policy helper is expected to reject.

| File pair | Scenario | Expected outcome |
|---|---|---|
| `critical_asset_detail_request.input.json` / `.expected.json` | A request asks for T4 critical-asset/condition detail at public (T0) exposure. | `DENY` — no critical-asset or condition fields returned. |
| `condition_observation_missing_transform.json` / `.expected_error.txt` | A `ConditionObservation` payload claims T1 public exposure with no aggregation/temporal-bucket transform applied. | `ERROR` — release precheck fails closed on the missing `AggregationReceipt`. |

Shared posture:

- Every file here is synthetic and safe to store; none contain the critical-asset, dependency, or condition/vulnerability detail the checks are designed to reject.
- A passing negative test proves only that the declared denial/error was produced for this fixture, not that any infrastructure claim, policy decision, or release was made.

See also: [`../README.md`](../README.md) · [`../valid/README.md`](../valid/README.md)
