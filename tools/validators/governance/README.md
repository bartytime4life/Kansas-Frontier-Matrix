# Governance validators

`tools/validators/governance/` contains deterministic governance validators and
dry-run analysis tools. They do not create evidence, make policy or review
decisions, authorize repository operations, release artifacts, or publish.

## BriefingSignal executables

### `validate_briefing_signal.py`

Validates the proposed non-authoritative `1.2.0` profile:

- bounded duplicate-key-safe JSON and closed schema shape;
- evidence references for confirmed claims;
- reproducible signal digest, daily ID, cluster ID, and issue idempotency key;
- exact materiality formula, thresholds, reason codes, and override consistency;
- exact finite routing precedence and reasons;
- duplicate issue-creation denial and declared existing-issue target shape;
- false consequential permissions;
- no inline geometry, secret-like fields, or true trust-bearing states; and
- deterministic no-network, value-minimized output.

### `deduplicate_briefing_signals.py`

Groups validated signals by event cluster, counts replay, detects collisions,
requires primary references, rejects duplicate issue creation, and emits dry-run
operations only.

### `validate_issue_inventory_projection.py`

Validates the read-only
`kfm.briefing.issue-inventory.fixture.v1` projection:

- closed, bounded, duplicate-key-safe JSON;
- sorted unique issue numbers with `OPEN` or `CLOSED` state only;
- canonical UTC-second generation and update times;
- issue-count closure;
- canonical SHA-256 digest and derived projection ID;
- fixed false live-state, authority, and mutation flags; and
- deterministic value-minimized findings.

The projection is synthetic local fixture state, not a live GitHub read or a
repository authorization record.

### `route_briefing_signals.py`

Recomputes materiality and declared routing for multiple local signals. With
`--issue-inventory`, it binds a declared `UPDATE_EXISTING_ISSUE` route to
exactly one open projected target. Missing, closed, absent-inventory, or
ambiguous targets become `HOLD_FOR_DEPENDENCY`. The report contains only IDs,
scores, priorities, finite reasons, proposed dispositions, idempotency keys, and
value-minimized issue-state metadata.

It always reports `authority_created=false` and
`repository_mutation_allowed=false`.

## Implementation-decision review

### `validate_implementation_decision_record.py`

Validates and mechanically renders the proposed non-authoritative
`ImplementationDecisionRecord` profile:

- closed duplicate-key-safe JSON with exact false permission and non-effect boundaries;
- stable relative repository paths and canonical ordering of path, object-family, evidence, and validation arrays;
- a chosen mechanism, rationale, at least one rejected or deferred alternative, and reviewer questions;
- finite `READY`, `HOLD`, and `ERROR` outcomes with exit codes `0`, `3`, and `2`;
- ADR escalation for authority-significant records and multi-root closure for cross-component records;
- deterministic Markdown assembly from declared fields only; and
- denial of hidden-reasoning or person-profile content.

`READY` means only that the record is internally ready to present to a reviewer.
The tool does not inspect a diff, infer a decision, authenticate a reference,
create review approval, or replace the KFM pull-request template.

## Implementation-change context

### `validate_implementation_change_context.py`

Builds and validates the proposed non-authoritative
`ImplementationChangeContext` profile:

- binds a local committed Git range to full base and head SHAs;
- records sorted path, status, rename/copy source, text-line count, and binary metadata only;
- excludes raw diff hunks, file contents, prompts, private reasoning, and person profiles;
- recomputes responsibility roots, finite signal codes, score, and the decision-capture recommendation;
- derives content identity with the repository RFC 8785 + SHA-256 helper;
- supports deterministic `DRAFT` backfill from an existing committed range without inventing rationale;
- returns finite `READY`, `HOLD`, and `ERROR` outcomes with exit codes `0`, `3`, and `2`; and
- retains exact false permission and non-effect boundaries.

The recommendation only says that durable implementation rationale may help a
reviewer. It is not a policy decision, risk rating, approval, merge gate, or
claim that a design decision exists. Rationale belongs in a separately authored
and validated `ImplementationDecisionRecord`.

## Verification backlog records

### `validate_verification_backlog_item.py`

Validates the proposed, inactive `VerificationBacklogItem` profile through small private I/O, semantic-model, and fixture-expansion modules plus one public CLI:

- the Agenda-derived required record for question, bounded scope, evidence, currentness, constraints, impacts, recommendation, acceptance, residue, and next check;
- exact `EXT`, `REPO`, `DEC`, `STW`, and `TST` research modes without cross-mode substitution;
- deterministic item identity and full-record spec hash;
- canonical ordering and duplicate denial;
- finite `READY`, `HOLD`, and `ERROR` outcomes with exits `0`, `3`, and `2`;
- fail-closed rights, sensitivity, sovereignty, security, and public-use constraints;
- resolved and superseded-state coherence; and
- exact false permissions and non-effects.

`READY` means only that a closed backlog record is internally consistent.
The validator does not conduct research, authenticate evidence, update the human
verification register, create a control-plane projection, make a steward or
architecture decision, activate a source, or authorize public use.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_briefing_signal.py \
  examples/briefing_integration/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_issue_inventory_projection.py \
  fixtures/contracts/v1/governance/issue_inventory_projection/valid/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/route_briefing_signals.py \
  --issue-inventory \
  fixtures/contracts/v1/governance/issue_inventory_projection/valid/open-target.json \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json \
  examples/briefing_integration/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_implementation_decision_record.py \
  --cases

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_implementation_change_context.py \
  --cases

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_verification_backlog_item.py \
  --cases
```

None of these tools fetches sources, reads live GitHub state, writes GitHub
issues or control-plane registers, activates policy, or validates real-world truth.
The change-context builder may read local committed Git metadata only when
explicitly invoked.
