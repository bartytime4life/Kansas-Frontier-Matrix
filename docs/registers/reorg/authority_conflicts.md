# Authority Conflicts

- **CONFLICTED**: `contracts/` vs `schemas/` both contain machine-shape material; ADR-0001 exists and must remain governing for any machine-file migration.
- **CONFLICTED**: `policy/` vs `policies/` both exist; ADR-0013 defines policy-home authority and blocks direct machine policy migration without explicit follow-up.
- **CONFIRMED**: this sprint only moved domain documentation paths; no machine schema/policy files moved.
