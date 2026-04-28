# Runtime Proof: Evidence Ref

`tests/e2e/runtime_proof/evidence_ref/` validates the runtime evidence-ref chain used by
claim rendering.

## Coverage focus

- promoted evidence refs render (`decision == cite`)
- missing/invalid/unapproved evidence refs abstain
- digest mismatch fails closed
- composed-claim refs must fully resolve to render
- file-based evidence-ref loading preserves the same fail-closed guarantees

## Key invariant

A runtime path may render only when required evidence and composed-claim references are
fully valid and approved. Any resolver error path must return abstain/fail-closed.

## Run

```bash
pytest -q tests/e2e/runtime_proof/evidence_ref
```
