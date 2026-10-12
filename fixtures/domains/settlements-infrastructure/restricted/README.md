# Settlements/Infrastructure — restricted (T4) fixtures

`fixtures/domains/settlements-infrastructure/restricted/`

Status: draft / fixture lane, first payload added.

This lane exercises the deny-by-default outcome for **T4** infrastructure
material — critical-asset detail, condition/vulnerability records, and
sensitive dependency edges — per
[`docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md)
§7.1–§7.2.

> [!IMPORTANT]
> Nothing in this directory contains real critical-infrastructure detail. Every field holds a synthetic placeholder string. The point of each fixture is to prove that a **request** for T4 content at a public tier is denied, not to store the content itself.

| File | Scenario | Expected outcome |
|---|---|---|
| `restricted_1_dependency_edge_request.json` | A request asks for a full `Dependency` edge (asset-to-asset reliance) at public (T0) exposure. | `DENY` — full dependency edges are T4-only; at most a coarse aggregate summary may reach T1. |

See also: [`../README.md`](../README.md) · [`../invalid/README.md`](../invalid/README.md)
