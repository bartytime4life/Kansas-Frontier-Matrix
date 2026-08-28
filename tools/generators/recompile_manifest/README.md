# Fixture-only RecompileManifest compiler

This lane implements the inactive `kfm.governance.recompile-manifest.v1` profile.

It reads one explicit local `QueryRunRecord`, one `AIChangeProposal`, and one JSON subject preimage. When every upstream fixture projection is valid and ready, it applies the proposal in memory, emits canonical JSON candidate bytes and a `RecompileManifest` to stdout, and exits without writing any file.

## Boundary

- `FIXTURE_ONLY_NO_WRITE`
- no network imports or calls
- target stage fixed to `WORK`
- no overwrite or output-path option
- no evidence, policy, review, promotion, release, deployment, publication, or public-use authority

## Commands

```bash
python tools/generators/recompile_manifest/compile_recompile_manifest.py --fixtures

python tools/generators/recompile_manifest/compile_recompile_manifest.py \
  --query-run fixtures/contracts/v1/governance/recompile_manifest/query_ready.json \
  --proposal fixtures/contracts/v1/governance/ai_change_proposal/valid/valid_ready.json \
  --subject fixtures/contracts/v1/governance/ai_change_proposal/subjects/base.json \
  --compiled-at 2026-08-06T23:05:00Z
```

The second command prints the candidate and manifest. It creates no output file.
