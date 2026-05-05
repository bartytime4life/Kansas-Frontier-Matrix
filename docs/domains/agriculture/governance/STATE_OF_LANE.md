# Agriculture Lane State of Lane

Last reviewed: 2026-04-27.

## Snapshot

The agriculture lane now has a full documentation control set in `docs/domains/agriculture/` for governance, source admission, contracts, validation, evidence, and operations.

## Present in this lane

- README landing page and lane scope.
- Source coverage and source registry documentation.
- Data contract overview and validation plan.
- Evidence/provenance and pipeline runbook guidance.
- Changelog, file index, and supersession map.

## Gaps still marked for verification

- Canonical schema home (`schemas/contracts/...` vs `contracts/...`).
- Existing policy-as-code locations and command names.
- Concrete validator script and CI workflow paths.
- CODEOWNERS/steward confirmation for agriculture lane ownership.

## Next actions

1. Confirm schema home via ADR and update `DATA_CONTRACTS.md`.
2. Add machine-readable source descriptors under the canonical registry path.
3. Land fixture-first validators and wire CI checks.
4. Record first release manifest and rollback card references.
