# next-repo-scan

## Scan metadata
- **CONFIRMED** Branch: `work`.
- **CONFIRMED** Dirty state from `git status --short`: clean (no output).
- **CONFIRMED** Latest commit: `3ef70f46f42a6e02500e4675af73c836700d6e6d`.

## Top-level directories (active checkout)
- **CONFIRMED** `.github`, `apps`, `artifacts`, `configs`, `connectors`, `contracts`, `control_plane`, `data`, `docs`, `examples`, `fixtures`, `infra`, `migrations`, `packages`, `pipeline_specs`, `pipelines`, `policy`, `release`, `runtime`, `schemas`, `scripts`, `tests`, `tools`.

## Package markers and repo README markers
- **CONFIRMED** `README.md` files discovered at root and key subtrees, including package and module markers:
  - `README.md`
  - `packages/README.md`
  - `packages/kfm_core/README.md`
  - `apps/api/README.md`
  - `apps/web/README.md`
  - `schemas/README.md`
  - `tests/README.md`
  - `tools/README.md`
- **NEEDS VERIFICATION** Python packaging/build-system depth beyond visible `pyproject.toml` conventions was not re-audited in this scan.

## Workflow files
- **CONFIRMED** `.github/workflows/baseline.yml`.
- **CONFIRMED** `.github/workflows/synthetic-release-dry-run.yml`.
- **PROPOSED** Keep synthetic dry-run workflow optional for branch policy while baseline remains required.

## Schema homes
- **CONFIRMED** Primary schema root exists at `schemas/contracts` with versioned subtree `schemas/contracts/v1`.
- **CONFIRMED** Shared schema subtree exists at `schemas/contracts/v1/shared`.
- **NEEDS VERIFICATION** Enforcement breadth for shared schemas vs domain schemas across all validators should be periodically reviewed.

## Tests
- **CONFIRMED** Test roots include `tests/`, `tests/public_surface/`, and `tests/domains/`.
- **CONFIRMED** `scripts/validate_all.sh` executed and completed with passing checks plus expected dry-run ABSTAIN outputs for network-disabled probes.

## Validators
- **CONFIRMED** Validator scripts present under `tools/validators/` including:
  - `validate_activation_decisions.py`
  - `validate_evidence_closure.py`
  - `validate_fixture_validation.py`
  - `validate_public_path_guards.py`
  - `validate_source_terms.py`
- **CONFIRMED** Gate-style validation tools under `tools/` executed via `scripts/validate_all.sh` and passed.

## Transitional roots
- **CONFIRMED** Lifecycle/transitional directories present under `data/`:
  - `data/raw`
  - `data/work`
  - `data/quarantine`
  - `data/processed`
- **CONFIRMED** Publication/serving-adjacent roots present:
  - `data/catalog`
  - `data/triplets`
  - `data/published`
  - `release/dry_runs`

## Open UNKNOWNs
- **UNKNOWN** Whether any downstream consumers require stricter JSON schema constraints for newly added shared schemas beyond minimal `id`-based structure.
- **UNKNOWN** Whether synthetic mock payloads should be formally linked into contract-schema validation mapping (outside current checks).
- **UNKNOWN** Whether CI branch protection currently treats `synthetic-release-dry-run.yml` as required or informational.

## Commands run (as requested)
- **CONFIRMED** `git status --short`
- **CONFIRMED** `git branch --show-current`
- **CONFIRMED** `git rev-parse HEAD`
- **CONFIRMED** `find . -maxdepth 2 -type d | sort`
- **CONFIRMED** `find . -maxdepth 3 -name README.md | sort`
- **CONFIRMED** `bash scripts/validate_all.sh` (available and executed)
