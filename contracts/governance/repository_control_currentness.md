# Repository-control projection currentness

`control_plane/repository_control_state.yaml` is a signed-by-review,
observation-time projection. It is not a self-refreshing pointer to live GitHub
state and cannot authorize itself.

Check it only against a separately observed full head:

```bash
python tools/validators/repository_control/check_currentness.py \
  --observed-main-sha "$(git rev-parse origin/main)"
```

An optional `--max-age-days N` adds a bounded age gate. The command fails closed
when the projection is `SUPERSEDED`, the recorded main SHA differs, the
observation is too old, or a SHA/timestamp is malformed.

The current checked-in projection is deliberately marked `SUPERSEDED` because
its August 3, 2026 main checkpoint predates the current repository head and its
July 29 settings snapshot predates the live required-check configuration. The
historical record is preserved rather than rewritten as if it were a fresh
observation.

A successor projection must be built from a new read-only GitHub observation,
carry its own recomputed state digest, and undergo normal repository review.
Passing this currentness check does not grant merge, source-admission, release,
deployment, or publication authority.
