# ADR-0002: Governed API path canonicalization (`governed_api` vs `governed-api`)

- **Status:** accepted
- **Date:** 2026-04-25
- **Decision area:** repository structure / import boundaries / compatibility

## Context

The repository currently contains both:

- `apps/governed_api/...` (Python-importable canonical path), and
- `apps/governed-api/...` (legacy path used in docs and historical references).

This dual-path state creates maintenance risk unless one path is declared authoritative.

## Decision

1. **Canonical implementation path:** `apps/governed_api/...`
2. **Legacy compatibility path:** `apps/governed-api/...` remains shim-only.
3. Legacy shim files may only re-export canonical modules and must not hold primary logic.
4. CI enforces this policy via `tools/ci/check_governed_api_path_policy.py`.

## Consequences

### Positive

- Python import behavior is deterministic.
- Implementation ownership is clear.
- Legacy path references continue to resolve without immediate broad docs breakage.

### Negative / tradeoffs

- Temporary duplication of file paths remains visible.
- Additional CI check must be maintained.

## Implementation notes

- Canonical files currently enforced:
  - `apps/governed_api/ecology/evidencebundle_resolver.py`
  - `apps/governed_api/ecology/routes.py`
  - `apps/governed_api/ecology/fastapi_routes.py`
- Legacy shim files currently enforced:
  - `apps/governed-api/ecology/evidencebundle_resolver.py`
  - `apps/governed-api/ecology/routes.py`
  - `apps/governed-api/ecology/fastapi_routes.py`

## Verification

A change violates this ADR if:

- canonical files are missing, or
- legacy files contain non-shim logic.

CI must fail for such changes.
