<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-local_data-intake_studio-readme
title: Local intake studio operator
type: readme
version: v1.1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-11-06
updated: 2026-11-20
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
the established capture and intake primitives. `intake_server.py` is the protected
entrypoint; `intake_backend.py` retains storage and review; `large_upload.py` keeps
resumable, chunk-verified upload sessions for files over 25 MiB (up to 2 GiB);
`intake_worker.py` performs
sandboxed extraction, and `local-web/` supplies the local client. The launcher is
on demand; it does not install packages, services or public routes.
`workspace.py` mounts the existing Working Data and read-only Library desks
inside the same sidebar and loopback origin when their roots are configured.

Owning root: `tools/`, following the adjacent local-data operators and desk.
No registry, contract, policy or proof authority lives here. Originals and state
remain outside Git. Tests live in `tests/local_data/test_intake_studio.py`.

## Acceptance & evidence

The same workspace now includes a private receipt-and-observation desk at
`/api/workspace/acceptance/page`. It imports the saved PR #5856 receipt without
changing original bytes or treating historical claims as new verification.
Its separate append-only ledger cannot change intake review, sensitivity,
source admission or publication. See the [local acceptance runbook](../../../docs/runbooks/local-acceptance-evidence.md)
for limits, evidence export, remaining acceptance checks and rollback.

## Private accounts and recovery evidence

The supported server and launcher now require local Studio accounts. A one-time
local setup code creates the first owner; owner-managed admin/operator/viewer
roles protect both pages and APIs. The same navigation adds Backup & recovery
with recorded storage identities, seven evidence stages and display-only command
plans. No disk operations or public deployment are performed.

See the [accounts and recovery runbook](../../../docs/runbooks/private-studio-accounts-recovery.md)
for setup, threat boundary, backup requirements, remaining validation and safe
rollback. `intake_backend.py` is the preserved internal implementation, not a
supported anonymous server entrypoint. Do not launch it directly. The existing
hosted Sites and installed machines are not changed by this source candidate.

## Local administration and data workspace

`studio-admin.sh` (implemented by `studio_admin.py`) is the owner's local program
for passwords, accounts, sign-in lockouts and stopping Studio. It also records the
Working Data and Library roots in `~/.config/kfm-intake-studio/workspace.json`;
`workspace_config.py` validates that file and the launcher passes it to the server,
so held reviews can be sent to Working Data. See the
[administrator quick start](../../../docs/runbooks/private-studio-accounts-recovery.md#administrator-quick-start--local-admin-program).
Tests live in `tests/local_data/test_studio_admin.py`.

## Regression checks

The Studio, handoff and Workspace tests use temporary local accounts and real
cookie/CSRF validation. Fixtures lower only the password KDF cost; the supported
server, account gateway and production KDF configuration stay unchanged. The
strict no-network target exercises in-memory requests; separately run the
loopback cases in `test_intake_studio.py`, `test_intake_studio_integrity.py` and
`test_intake_studio_security.py` to cover the actual protected server, original
integrity and HTTP serialization. These synthetic checks do not qualify native
extraction, an installed service, a browser journey or private production data.

Fingerprint tests patch the owning `intake_backend` module while calling through
the supported `intake_server` facade, so changes to copied authentication,
recovery, workspace and Qwen files must alter the observed identity. Matching
launcher health must also declare `local-accounts-required`; an older or
unauthenticated process is preserved and refused.
