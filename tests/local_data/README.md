<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-local-data-readme
title: Local PC readiness and data capture tests
type: readme
version: v1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-09-17
updated: 2026-09-17
policy_label: public
owning_root: tests/
responsibility: Record the local readiness and quarantine capture test boundary.
truth_posture: Branch-local deterministic tests; production and native-host acceptance are not established.
[/KFM_META_BLOCK_V2] -->

# Local PC readiness and data capture tests

This existing `tests/` responsibility root owns executable regressions for
`tools/local_data/` and the bounded local-byte capture helper in
`connectors/local_upload/`. Tests use temporary external stores and synthetic
opaque payloads; nothing is downloaded or promoted.

```bash
python3 -m pytest -q tests/local_data
```

Coverage includes manifest shape, explicit-file selection, checksums, resource
limits, path/symlink rejection, storage corruption, interruption and retry,
no-overwrite commit, immutable capture revisions, multi-source backup restore,
read-only doctor output and independent boundary regressions. Tests do not prove
network acquisition, source admission, map rendering integration or native
Windows ACL/crash behavior. The operator tools use the Python standard library;
these tests additionally use the repository's declared test dependencies.
