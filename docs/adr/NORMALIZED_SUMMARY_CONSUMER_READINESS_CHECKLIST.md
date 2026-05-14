# Normalized Summary Consumer Readiness Checklist

Use this checklist before enabling normalized-only preflight summaries by default.

## Scope
- Applies to consumers of doctrine artifact preflight summaries.
- Covers CI checks, operator tooling, and downstream parsers.

## Required checks
- [ ] Consumer reads `artifact_paths.check_receipt` instead of standalone `check_receipt`.
- [ ] Consumer reads `artifact_paths.provenance_sync_receipt` instead of standalone `provenance_sync_receipt`.
- [ ] Consumer handles nullable `artifact_paths.presence_output`.
- [ ] Consumer reads `artifact_digests.*` map for digest lookups.
- [ ] Consumer does not require standalone digest fields.
- [ ] Consumer passes `validate_doctrine_preflight_summary_consistency.py --require-normalized-only` on representative fixtures.
- [ ] Rollback path documented (re-enable compatibility mode output).

## Evidence to attach per consumer
- Consumer name / owner
- Test command(s)
- Date validated (UTC)
- Link to CI run or test artifact
- Notes / follow-ups
