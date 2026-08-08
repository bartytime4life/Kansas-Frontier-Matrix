<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-validator-orchestrator
title: Validator Orchestrator Runbook
type: runbook
version: v1.0
status: draft
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal
owning_root: docs/
responsibility: Operate the bounded registry-driven validator orchestrator without treating a validation result as evidence, policy, review, release, or publication authority.
truth_posture: CONFIRMED current command and registry contract on this branch; hosted CI remains NEEDS VERIFICATION until the pull-request checks complete.
related:
  - ../../tools/validate_all.py
  - ../../tools/validators/validate_all.py
  - ../../tools/validators/validator_registry.json
  - ../../tools/validators/_common/run_all.py
  - ../../tests/validators/test_validator_orchestrator.py
  - ../doctrine/directory-rules.md
  - ../dashboards/observability/validator-orchestrator-health.md
notes:
  - "Directory Rules v2 DIR-EXEC-006 permits tools/validate_all.py as a thin repository entrypoint while implementation remains under tools/validators/."
  - "This runbook implements the bounded orchestrator direction associated with KFM-P5-PROG-0009 and the Pass 6 validator-report expansions."
  - "The orchestrator runs repository-owned validators without a shell, forces no-network test posture, and emits finite machine-readable outcomes."
  - "A green orchestrator report proves only the selected checks completed successfully for the declared profile."
[/KFM_META_BLOCK_V2] -->

# Validator Orchestrator Runbook

`tools/validate_all.py` is the canonical thin entrypoint. The implementation and executable registry live under `tools/validators/`, consistent with Directory Rules v2 `DIR-EXEC-006`.

> [!IMPORTANT]
> The orchestrator is a checker coordinator. It does not resolve evidence, evaluate policy, authenticate review, approve promotion, assemble a release, publish data, or certify that every repository invariant is covered.

## Commands

Validate the registry without running child validators:

```bash
python tools/validate_all.py --validate-registry
```

List profiles and registered validator IDs:

```bash
python tools/validate_all.py --list
```

Run the complete bounded registry:

```bash
python tools/validate_all.py --profile full
```

Run the smaller trust-spine profile:

```bash
python tools/validate_all.py --profile focused
```

Run the release-adjacent fixture profile:

```bash
python tools/validate_all.py --profile release-dry-run
```

Select validators from changed repository paths:

```bash
python tools/validate_all.py \
  --profile changed-area \
  --changed-path contracts/runtime/decision_envelope.md \
  --changed-path schemas/contracts/v1/runtime/decision_envelope.schema.json
```

Select exact registered IDs:

```bash
python tools/validate_all.py \
  --profile focused \
  --validator evidence-bundle \
  --validator decision-envelope
```

Write the deterministic report to a file:

```bash
python tools/validate_all.py \
  --profile full \
  --output artifacts/qa/validator-orchestrator.json \
  --quiet
```

Timing is excluded by default so identical validator outputs yield identical reports. Add timing only for operational inspection:

```bash
python tools/validate_all.py --profile full --include-timing
```

## Profiles

| Profile | Selection law | Empty selection |
|---|---|---|
| `focused` | Small trust-spine subset declared in the registry. | Configuration error. |
| `changed-area` | Every validator whose registered path glob matches at least one supplied changed path. | `ABSTAIN` with `NO_MATCHING_VALIDATORS`, exit `0`; this is not represented as a validator pass. |
| `release-dry-run` | Release-adjacent evidence, decision, and receipt fixture validators. | Configuration error. |
| `full` | Every registered validator exactly once, in registry order. | Configuration error. |

The `full` profile means every validator in `validator_registry.json`; it does not claim every executable checker in the repository has been registered.

## Finite outcomes and process exit codes

| Outcome | Exit | Meaning |
|---|---:|---|
| `PASS` | `0` | Every selected child validator exited `0`. |
| `ABSTAIN` | `0` | The `changed-area` profile matched no registered validator. No pass claim is made. |
| `FAIL` | `1` | The orchestrator completed and at least one child validator exited `1`. |
| `ERROR` | `2` | Registry, path, I/O, timeout, or child-system failure occurred; or a child exited outside `0`/`1`. |

Downstream callers must preserve the distinction between exit `1` and exit `2`. An arbitrary nonzero exit is not proof of a reviewed validation rejection.

## Report contract

The default JSON report includes:

- registry identity and SHA-256 digest;
- named profile and selection mode;
- normalized changed paths or explicit validator IDs;
- aggregate finite outcome and reason code;
- registered and selected counts;
- one stable result per selected validator;
- child return code;
- SHA-256 digests and line counts for captured stdout/stderr;
- declared artifact references, when the registry supplies them;
- no timestamp and no duration unless `--include-timing` is requested.

Raw child output is not copied into the JSON report. `--verbose` prints bounded captured output to stderr for a local operator and should not be enabled on a public surface.

## Registry maintenance

`tools/validators/validator_registry.json` is executable selection metadata, not policy or release authority. For each new entry:

1. use a stable lowercase validator ID;
2. point only to a repository-relative Python file under `tools/validators/`;
3. use bounded arguments and timeout;
4. register nonempty path globs for changed-area selection;
5. add the ID to one or more named profiles;
6. keep `profiles.full` equal to the complete validator list, in the same order;
7. add focused positive and negative orchestrator tests when registry semantics change;
8. verify the child validator already has its own fixtures, tests, and authority boundary.

Do not register placeholder validators that intentionally raise `NotImplementedError`.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validator_orchestrator.py' \
  --verbose

python tools/validate_all.py --validate-registry
python tools/validate_all.py --profile full
```

The existing compatibility surface remains available:

```bash
python tools/validators/_common/run_all.py
```

It delegates to the canonical full profile and retains `RUNNER_VALIDATORS` for the existing `validator-suite` workflow. New callers should use `tools/validate_all.py`.

## Failure handling

- Registry parse, duplicate key, nonfinite number, path escape, missing script, symlink, profile drift, or unsafe output path: exit `2`.
- Child timeout: child result `ERROR`, aggregate exit `2`.
- Child exit `1`: child result `FAIL`, aggregate exit `1` unless another child errors.
- Child exit `2` or any other code: child result `ERROR`, aggregate exit `2`.
- Changed-area no match: `ABSTAIN`, exit `0`, with no false all-pass statement.

## Rollback

Revert the campaign commit to restore the previous `Makefile` aggregate runner and placeholder entrypoints. Do not delete historical CI logs or reports. The compatibility wrapper makes rollback independent of consumers that still import `RUNNER_VALIDATORS`.
