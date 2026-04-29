# Ecology Source Role Matrix

Defines admissible source roles and claim boundaries for ecology registry descriptors.

| Source role | Allowed support | Must not be used as |
|---|---|---|
| `TAXONOMIC_AUTHORITY` | Taxonomic naming, synonym reconciliation, and canonical species references. | Direct proof of current local occurrence. |
| `OBSERVATION_SYSTEM` | Observed records with time, place, and method context. | Standalone public release when rights, precision, or sensitivity are unresolved. |
| `AGGREGATOR` | Federated occurrence access and broad discovery context. | Unreviewed canonical truth for sensitive/public claims. |
| `DERIVED_MODEL_LAYER` | Contextual surfaces (e.g., vegetation indices, modeled habitat context). | Confirmed field observation evidence by itself. |
| `SENSITIVE_OCCURRENCE` | Restricted stewardship records requiring geoprivacy controls. | Exact public geometry without explicit review and transform receipts. |

## Admission checks

A descriptor should be accepted only if it explicitly states:

1. source role
2. rights posture
3. sensitivity class
4. publication requirements
5. quarantine triggers
