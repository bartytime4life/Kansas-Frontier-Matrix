# M17 supply-chain evidence slice

This directory holds the first bounded evidence slice for issue #3382.

## Snapshot

- Current main pinned at `db23a8bfa9fa126e87009a41240576619ccaac02`
- Overlapping open PR at execution start: `#4079`
- Current-main hosted evidence:
  - `dependency-scan` run `33543430134` — success
  - `codeql` run `33543430164` — success
  - `security` run `33543430108` — success
  - `scorecard` run `33543430062` — success

## Inventory

Relevant current surfaces are recorded in
[`dependency_supply_chain_evidence.json`](./dependency_supply_chain_evidence.json):

- dependency review / audit workflow
- CodeQL companion workflow
- repository / container / scorecard security workflow
- lockfiles and package manifests
- pnpm audit readiness validator and tests
- Dockerfile scan surfaces

## First slice

The selected reproducible slice is the dependency-audit lane:

- path: `.github/workflows/dependency-scan.yml`
- validator: `tools/validators/dependencies/pnpm_audit_readiness.py`
- tests: `tests/validators/test_pnpm_audit_readiness.py`
- rollback: revert the workflow/report slice and re-run the no-network validator plus hosted audit

## Explicitly unresolved

- SBOM generation
- attestations and signatures
- license review
- OpenSSF beyond the current Scorecard signal
- any future PR overlap beyond `#4079`

This folder is inspection evidence only. It does not authorize release, publication, promotion, or dependency admission.
