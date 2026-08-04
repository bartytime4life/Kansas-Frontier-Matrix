# BriefingSignal fixtures

Synthetic, public-safe fixtures for the proposed `BriefingSignal` `1.1.0` profile.

They exercise deterministic daily signal identity, durable event clustering, issue-routing idempotency, duplicate classification, non-authoritative permissions, evidence references, and inline-geometry denial. They are test inputs only—not real briefings, official-source snapshots, evidence, issue instructions, review decisions, or public records.

## Inventory

- `valid/valid_1.json`: first synthetic signal in a new event cluster.
- `valid/valid_duplicate_followup.json`: later briefing revision with changed wording, the same event cluster, an explicit primary-signal match, and `NO_ACTION`.
- `invalid/invalid_public_use.json`: false public, publication, and repository-mutation authority.
- `invalid/invalid_missing_evidence.json`: confirmed claim without evidence.
- `invalid/invalid_inline_geometry.json`: inline coordinate material.
- `invalid/invalid_duplicate_issue_create.json`: duplicate signal attempting to open parallel work.

## Run

```bash
python tools/validators/governance/validate_briefing_signal.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json

python tools/validators/governance/deduplicate_briefing_signals.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json
```

Known-invalid fixtures must return a nonzero result. A pass creates no source, evidence, issue, review, policy, release, deployment, publication, or public-use authority.
