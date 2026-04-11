# Backlog

## High priority

1. Decide authoritative API lane naming (`apps/api` vs `apps/governed-api`) and collapse duplicates.
2. Add real package manifests for each implemented stack (Python/Node/etc.) once code lands.
3. Replace placeholder README sections containing `NEEDS VERIFICATION` with commit-verified values.
4. Expand tests beyond the single correction notice contract floor test.

## Medium priority

1. Add machine-checked schema validation (e.g., `jsonschema`) once dependency strategy is approved.
2. Add CI workflow YAML that runs the standardized Makefile entrypoints.
3. Add deterministic lint/doc checks for README cross-links.

## Known unknowns

- Intended runtime stack(s) for `apps/`, `packages/`, and `web/` are not yet implemented in this checkout.
- Deployment targets and operational runtime shape remain documentation-level only.
