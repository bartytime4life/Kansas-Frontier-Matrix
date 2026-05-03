# Authority conflicts

- CONFLICTED: `contracts/` and `schemas/` both contain machine-shape and semantic materials; ADR-0001 and ADR-0012 require explicit compatibility mapping before any machine-file migration.
- CONFLICTED: `policy/` and `policies/` both exist; ADR-0013 marks `policy/` as primary authority with `policies/` as compatibility lane pending consolidation.
