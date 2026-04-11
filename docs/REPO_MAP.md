# Repository Map (Evidence-Based)

Last verified: 2026-04-11 (UTC).

## README inventory snapshot

- Total `README.md` files: **396**.
- README-heavy directories (README is the only file in directory): **250**.
- This is currently a **documentation-first scaffold** with a small amount of executable validation code.

## Top-level map (actual files and directories)

- Governance/docs: `.github/`, `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `LICENSE`.
- Domain/structure lanes: `apps/`, `brand/`, `configs/`, `contracts/`, `data/`, `docs/`, `examples/`, `infra/`, `migrations/`, `packages/`, `pipelines/`, `policy/`, `schemas/`, `tests/`, `tools/`, `web/`.
- Executable implementation currently confirmed:
  - `tests/contracts/test_correction_notice_contract.py`
  - `schemas/contracts/v1/correction/correction_notice.schema.json`
  - fixture JSON under `schemas/tests/fixtures/contracts/v1/{valid,invalid}/`
  - utility scripts under `scripts/` and `Makefile` (added in this change set)

## Structural reality

1. Most subtrees are contract/README placeholders, not full implementations.
2. No package manager workspace manifest was found (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml` absent).
3. Build and test entrypoints referenced by root docs now resolve through `Makefile` targets.

## Current entrypoints

- `make bootstrap`
- `make validate-schemas`
- `make test`
- `make dev-up`
- `make sample-ingest SOURCE=<name>`
- `make catalog-validate`
