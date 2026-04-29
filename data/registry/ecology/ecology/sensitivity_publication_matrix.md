# Sensitivity Publication Matrix

Fail-closed publication outcomes for ecology records.

| Sensitivity class | Public precision | Default decision | Required controls |
|---|---|---|---|
| `low` | Exact or generalized | `allow` | rights clear, evidence bundle present, citation present |
| `moderate` | Generalized preferred | `review_required` | reviewer approval, precision check, evidence bundle |
| `high` | Not exact in public lanes | `generalize_or_restrict` | geoprivacy transform, redaction receipt, reviewer approval |
| `restricted` | No public geometry | `deny_public` | non-public access controls, DUA confirmation |

## Guardrails

- Exact coordinates for sensitive species are denied for public outputs unless policy says otherwise.
- Missing rights or missing evidence defaults to `hold`.
- Derived layers must retain derived/model labeling in all runtime surfaces.
