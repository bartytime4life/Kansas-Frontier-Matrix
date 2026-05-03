# Authority Conflicts

- CONFLICTED: `contracts/` vs `schemas/` both contain machine-shape adjacent artifacts; ADR-0001 exists but coexistence persists.
- CONFLICTED: `policy/` vs `policies/` both active homes; ADR-0013 documents boundary but split remains.
- PROPOSED: keep machine files in-place; only index/control docs updated in this sprint.
