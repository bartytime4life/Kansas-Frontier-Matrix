# BriefingSignal fixtures

Synthetic, public-safe fixtures for the proposed `BriefingSignal` `1.2.0` profile.

They exercise deterministic identity, event clustering, idempotency, explainable materiality, mandatory overrides, finite routing, duplicate suppression, false-authority denial, evidence requirements, and inline-geometry denial. They are test inputs only—not real briefings, official-source snapshots, evidence, issue instructions, review decisions, or public records.

## Inventory

### Valid

- `valid/valid_1.json`: new cluster, exact `P2`, `NO_ACTION`.
- `valid/valid_duplicate_followup.json`: same cluster, later wording, duplicate `NO_ACTION`.
- `valid/valid_p0_corrective_override.json`: synthetic repository-integrity override and corrective-issue proposal.
- `valid/valid_p1_source_discovery.json`: exact `P1` threshold and source-discovery proposal.
- `valid/valid_dependency_hold.json`: `P1` candidate held for a dependency.
- `valid/valid_reject_unsafe.json`: `P1` candidate rejected as unsafe for routing.

### Structural invalid

- `invalid/invalid_public_use.json`: false public, publication, and mutation authority.
- `invalid/invalid_missing_evidence.json`: confirmed claim without evidence.
- `invalid/invalid_inline_geometry.json`: inline coordinate material.
- `invalid/invalid_duplicate_issue_create.json`: duplicate cluster opening parallel work.
- `invalid/invalid_priority_without_reasons.json`: priority without required finite reasons.

### Semantic invalid

`semantic_invalid/` contains schema-valid candidates with exact sidecars for score, priority, reason, override-context, disposition, and routing-reason mismatches.

## Run

```bash
python tools/validators/governance/validate_briefing_signal.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json

python tools/validators/governance/deduplicate_briefing_signals.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json

python tools/validators/governance/route_briefing_signals.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json
```

Known-invalid fixtures must return nonzero. A pass creates no source, evidence, issue, review, policy, proof, release, deployment, publication, or public-use authority.
