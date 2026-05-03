# Authority Conflicts
- CONFLICTED: schema authority split across `contracts/`, `schemas/`, and `jsonschema/`; ADR-0001 exists and ADR-0012/0013 indicate compatibility mode; no machine-file moves were made.
- CONFLICTED: policy authority split across `policy/` and `policies/`; ADR-0013 exists; no rego/json policy moves were made.
- CONFIRMED: lifecycle directories under `data/` were preserved in place.
