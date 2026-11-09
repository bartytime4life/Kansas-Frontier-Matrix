<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-local_data-intake_studio-readme
title: Local intake studio operator
type: readme
version: v1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-11-06
updated: 2026-11-06
policy_label: public
owning_root: tools/
responsibility: Describe local photo and PDF preparation implementation.
truth_posture: CONFIRMED targeted local regressions; NEEDS VERIFICATION camera and browser acceptance; no admission or publication.
[/KFM_META_BLOCK_V2] -->

# Local photo and PDF preparation operator

Run `./tools/local_data/intake_studio/start-local.sh` from the repository root.
See the [setup, review and handoff runbook](../../../docs/runbooks/local-intake-studio.md).

This Linux loopback operator prepares private held proposals and can explicitly
send a saved ready review into private Working Data capture and indexing.
`handoff.py` preserves original bytes, review history and sharing holds using
the established capture and intake primitives. `intake_server.py` owns storage
and review, `intake_worker.py` performs
sandboxed extraction, and `local-web/` supplies the local client. The launcher is
on demand; it does not install packages, services or public routes.
`workspace.py` mounts the existing Working Data and read-only Library desks
inside the same sidebar and loopback origin when their roots are configured.

Owning root: `tools/`, following the adjacent local-data operators and desk.
No registry, contract, policy or proof authority lives here. Originals and state
remain outside Git. Tests live in `tests/local_data/test_intake_studio.py`.
