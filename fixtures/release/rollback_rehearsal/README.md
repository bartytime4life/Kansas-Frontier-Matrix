# Synthetic rollback rehearsal fixtures

This lane documents the no-network fixture contract exercised by
`tests/release/test_synthetic_rollback_rehearsal.py`.

The test creates two immutable synthetic release directories, one current alias, fixed
manifest and artifact digests, a synthetic correction record, and the complete cache/index
invalidation set inside a temporary directory. The reusable helper refuses every workspace
that does not contain `.kfm-synthetic-rollback-rehearsal` with the exact value
`synthetic-only` and refuses scenarios that do not declare `synthetic: true`.

The fixture proves only deterministic rehearsal semantics. It does not validate a production
RollbackCard signature, authenticate a reviewer, evaluate policy, mutate `release/`, change a
real alias, publish, withdraw a public product, or create release authority.
