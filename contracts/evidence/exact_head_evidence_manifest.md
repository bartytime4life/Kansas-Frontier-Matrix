# Exact-head evidence manifest v1

The `kfm.exact-head-evidence/v1` manifest binds an observation to a full commit,
tree, commands, exit codes, collector, retained artifact digests, and explicit
lifecycle disposition.

It exists to prevent an older-head check, review, or artifact from being
presented as current evidence after `main` or a pull-request head advances.

## Validation

```bash
python tools/validators/evidence/validate_exact_head_evidence.py \
  path/to/manifest.json \
  --current-head "$(git rev-parse HEAD)"
```

A manifest marked `current` fails unless its full subject commit equals the
explicitly supplied observed head. A `superseded` manifest must name its
successor. Command and exit-code arrays must have equal length. GitHub Actions
evidence must name its workflow run, and retained artifacts must carry SHA-256
digests.

Independent acceptance can be recorded only when the collector is identified
as `independent`. The contract fixes `release_authority` to `false`; evidence
validity never implies source admission, release, deployment, publication, or
repository authority.
