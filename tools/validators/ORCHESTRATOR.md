<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-orchestrator
title: KFM validator orchestrator
type: operational-validator-contract
version: v0.1.0
status: draft; executable; no-network; non-authoritative
owners: OWNER_TBD — Validation steward · Schema steward · CI steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; validation; fail-closed; no-publication-authority
related:
  - ../validate_all.py
  - ./_common/run_all.py
  - ../../tests/validators/test_validate_all.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, validators, orchestration, deterministic, report, exit-codes, no-network]
[/KFM_META_BLOCK_V2] -->

# KFM validator orchestrator

`tools/validate_all.py` is the canonical repository entry point for the bounded
core validator set. It runs the existing validators in a stable registry order
and emits one text, JSON, or JUnit report.

`tools/validators/_common/run_all.py` is a compatibility delegate for existing
callers. It contains no independent registry.

## Interface

```bash
python tools/validate_all.py --list
python tools/validate_all.py --profile core
python tools/validate_all.py --only evidence-bundle,runtime-response-envelope \
  --format json --report /tmp/kfm-validation.json
python tools/validate_all.py --profile core --format junit \
  --report /tmp/kfm-validation.xml
```

## Stable process outcomes

| Exit | Meaning |
|---:|---|
| `0` | All selected validators passed, or only emitted non-blocking warnings. |
| `1` | A selected validator failed, or `--fail-on-warning` made a warning blocking. |
| `2` | Registry, process-launch, missing-validator, or report-write error. |

Child validator exits are normalized as `PASS`, `WARNING`, `FAIL`, or `ERROR`.
The orchestrator never reinterprets domain truth, evidence sufficiency, policy,
review, promotion, release, or publication state.

## Determinism and safety

- Registry order determines execution and report order.
- Reports contain no run timestamp or duration.
- JSON keys and arrays are emitted in stable order.
- Child diagnostics are bounded and line-normalized.
- Child processes receive `KFM_NO_NETWORK=1`, `PYTHONHASHSEED=0`, and `TZ=UTC`.
- Report writes are atomic.
- The runner does not install dependencies, fetch sources, mutate lifecycle
  storage, approve reviews, promote, release, deploy, or publish.

## Current core registry

1. `dataset-version`
2. `layer-manifest`
3. `release-manifest`
4. `evidence-bundle`
5. `runtime-response-envelope`
6. `release-decision`
7. `promotion-decision`

Changing the registry is a reviewable behavioral change. Add or remove a
validator only with its direct fixture/test/documentation closure.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After
an authorized merge, revert the orchestrator packet and restore the prior
placeholder and compatibility runner. No source, lifecycle object, release, or
public artifact requires rollback.
