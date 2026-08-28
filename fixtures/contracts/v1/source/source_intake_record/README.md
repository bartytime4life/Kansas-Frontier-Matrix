# SourceIntakeRecord fixture suite

Synthetic, no-network fixtures for the proposed `SourceIntakeRecord` and `DriftSummary` contracts.

- `valid/` proves no-change, bounded work-candidate, and blocking-quarantine postures.
- `invalid/` proves closed-schema rejection of direct publication and unsupported evidence-resolution claims.
- `semantic_invalid/` proves the CandidateDelta relationship and quarantine/materiality invariants.
- `expected_findings_manifest.json` binds every case to one finite expected outcome.

The fixtures contain no live source payload, sensitive location, credential, release decision, or publication authority.
