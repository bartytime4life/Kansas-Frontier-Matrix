# Changelog

## 0.1.1 - 2026-05-04
- Hardened baseline validation gates:
  - added explicit API contract validator integration,
  - added fixture-to-schema mapping validation,
  - added promotion receipt determinism tool and idempotence checks,
  - expanded directory rules enforcement,
  - composed `validate_repo` with directory-rules gate.
- Reduced test log noise by silencing mock API HTTP handler access logs.

## 0.1.0 - 2026-05-03
- Initial governance-first, synthetic hydrology baseline scaffold with docs, schemas, fixtures, policies, tooling, tests, and CI.
