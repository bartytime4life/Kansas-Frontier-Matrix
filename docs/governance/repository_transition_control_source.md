<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance/repository-transition-control-source
title: Repository transition check retirement
type: governance-binding-retirement-note
version: v1.5.0
status: retired by owner; workflow disabled; required status rule removed
owner: OWNER_TBD — governance steward and repository-control steward
created: 2026-09-03
updated: 2026-09-25
policy_label: repository-facing; governance; non-authoritative
owning_root: docs/
responsibility: Record retirement of the repository transition check while preserving historical evidence and offline validation semantics.
truth_posture: CONFIRMED platform readback; no independent containment or incident-closure claim
related:
  - ../../CONTRIBUTING.md
  - ../../contracts/governance/repository_control_state.md
  - ../../tools/validators/repository_control/validate_transition_authorization.py
  - ../../tests/validators/test_repository_control_source.py
  - ../../.github/workflows/repository-control.yml
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/rules/15484585
[/KFM_META_BLOCK_V2] -->

# Repository transition check retirement

## Current disposition

On 2026-09-25 the owner explicitly requested removal of the transition check
and its current Markdown requirements. This supersedes the check-specific
branch-only delivery hold. Authorized branch work and draft pull requests follow
[CONTRIBUTING](../../CONTRIBUTING.md); no issue-comment authorization record or
independent draft creator is required by this retired gate.

Platform readback confirmed:

- Ruleset `15484585` no longer requires `authorize-ready-and-merge`. It was the
  sole status context in that rule, so the empty required-status rule was removed.
- GitHub workflow `324077182`, `repository-control`, is `disabled_manually`.
- Deletion, non-fast-forward, pull-request and review-thread-resolution
  protections remain unchanged. The existing zero required approvals and owner
  always-bypass entry also remain unchanged.

This deliberately removes the automated exact-owner-record merge prerequisite;
it is not a repair to the validator and does not claim stronger containment.
No other required check is removed. No ready, approval, merge, release,
deployment, publication, source-admission or topology transition is authorized
by this document. Issue #4024 remains open as incident history; retirement does
not resolve the initiating-client attribution or prove independent acceptance.

## Retained implementation and historical evidence

The disabled workflow source, bounded capture helpers, strict authorization
parser, schemas and negative tests remain available for historical replay.
Their validation semantics are unchanged: invalid records still fail when the
retained tools are explicitly invoked. They are not active contributor gates.
The workflow was disabled through GitHub settings, not replaced with a green
no-op job. A checkout alone cannot establish its platform enablement state.

The [previous binding at the inspected base](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/7e25a287eaeb080bf18a743ae2518147b08b7e2a/docs/governance/repository_transition_control_source.md)
retains the former issue #4024 lookup, exact-record format, input limits,
required-check snapshot and proof plan. Deleted issue #1675 and historical
fixtures retain their original identity. Historical evidence for PR #4234,
PR #4235, PR #4622 and the
[PR #4675 incident](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024#issuecomment-5788994213)
is not erased or relabeled as authorized by this retirement.

## Verification and rollback

Verify the workflow's current platform state and effective default-branch rules
before claiming that the retirement is still applied. Offline parser tests
prove retained parsing behavior, not platform configuration or merge prevention.

A later owner-authorized restoration would enable the retained workflow, verify
its exact check identity and behavior, then reinstate the required status rule.
Restore only the retired rule against a fresh settings readback; do not overwrite
concurrent settings. Do not silently restore enforcement through a documentation
revert or invent a replacement gate. Historical records remain unchanged.
