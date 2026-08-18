<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://runbook/github-milestone-sync-m13-m24
title: GitHub Milestone Sync — M13 through M24
type: runbook
version: v1
status: draft; repository-grounded; explicit-operator-apply; no-scheduled-mutation
owner: "@bartytime4life — verified repository review route; independent program/quality/security stewardship remains NEEDS VERIFICATION"
created: 2026-08-18
updated: 2026-08-18
policy_label: repository-facing; program-planning; github-metadata; token-required-for-apply; no-release-authority
owning_root: docs/
responsibility: explain how an authorized maintainer validates, previews, creates, and verifies the evidence-backed M13-M24 GitHub milestone packet without overwriting existing milestone decisions
truth_posture: cite-or-abstain; GitHub milestone metadata is planning state only and never evidence, policy, promotion, release, deployment, or publication authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: e5a5aa69de564601fe3dd5e8cce2fb7c109e6306
  open_pull_requests: []
  open_issues: [2768, 2874, 2898, 2899, 2906, 2907, 2957, 2975, 2990, 3022]
related:
  - ../../scripts/maintenance/sync_github_milestones.py
  - ../../scripts/maintenance/github_milestones_m13_m24.json
  - ../../tests/governance/test_sync_github_milestones.py
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../quality/README.md
  - ../security/README.md
  - ../../SECURITY.md
  - ../../tools/validators/governance/validate_workflow_security.py
notes:
  - "No workflow is added. Mutation remains an explicit operator action using an environment-supplied GitHub token."
  - "No due dates are declared because the inspected evidence does not support a defensible schedule."
  - "The tool never deletes milestones, reopens closed milestones, overwrites descriptions, or replaces an issue's existing milestone."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GitHub Milestone Sync — M13 through M24

> **Purpose.** Apply the next twelve KFM planning milestones from one validated, reviewable manifest while preserving existing GitHub decisions and keeping security, quality, evidence, correction, and rollback boundaries visible.

> [!IMPORTANT]
> A GitHub milestone is a planning and coordination surface. Creating a milestone, assigning an issue, closing a milestone, merging a pull request, or showing a green check does **not** admit a source, establish an EvidenceBundle, approve policy, promote lifecycle state, release, deploy, or publish KFM material.

## Status and boundary

The packet is pinned to `main@e5a5aa69de564601fe3dd5e8cce2fb7c109e6306` and the ten open issues listed in the meta block. No open pull requests were returned at the checkpoint, so no active review branch owned this runbook, maintenance command, manifest, or governance-test path.

The manifest covers every open issue observed at the checkpoint. M14, M15, M16, and M24 intentionally have no issue assignment because the evidence supports strategic milestones but does not support inventing speculative issue records. No due date is supplied.

## Directory Rules basis

Accepted ADR-0029 adopts `docs/doctrine/directory-rules.md` as placement authority.

- `scripts/maintenance/` holds the bounded, explicit operator command and its command-specific manifest.
- `tests/governance/` holds executable conformance for the planning-metadata guardrails.
- `docs/runbooks/` explains the authorized operator procedure.
- No new root, control-plane authority, release object, workflow, or public route is created.

The script is a maintenance command, not a policy engine, evidence store, release tool, or publisher. Repeated broader GitHub-program automation would require a separate graduation and ownership review rather than silently expanding this packet.

## Milestone packet

| ID | Milestone | Mapped open issues |
|---|---|---|
| M13 | Security Operations & Fail-Closed Exposure Assurance | #3022 |
| M14 | Quality Engineering, Regression Ratchets & Test Governance | — |
| M15 | Hosted CI, Branch Protection & Workflow Convergence | — |
| M16 | Supply Chain, Containers, SBOMs & Artifact Attestation | — |
| M17 | Program Reconciliation & Repository Conformance | #2768, #2874 |
| M18 | Evidence Resolver & Inspectable Claim Closure | #2975 |
| M19 | Temporal Authority Compatibility & Historical Replay | #2990 |
| M20 | Kansas Transportation Geometry & Source Admission | #2898 |
| M21 | Western Kansas Drought & Hydrology Evidence Envelope | #2899 |
| M22 | MapLibre Architecture Decision & 6.4 Runtime Readiness | #2957, #2906 |
| M23 | GeoParquet 2.0 RC Carrier Interoperability | #2907 |
| M24 | Observability, Resilience, Correction & Recovery Readiness | — |

The full descriptions and evidence pointers live in `scripts/maintenance/github_milestones_m13_m24.json` so review and execution use the same bytes.

## Safety model

The command has three finite modes:

| Mode | Network | GitHub mutation | Intended result |
|---|---:|---:|---|
| `validate` | No | No | Strict local manifest validation. This is the default. |
| `plan` | Yes | No | Read milestones and optionally mapped issues, then print exact intended actions. |
| `apply` | Yes | Yes | Create missing exact-title milestones and optionally assign unassigned open issues. |

`apply` requires both:

1. `GITHUB_TOKEN` or `GH_TOKEN` supplied through the environment; and
2. `--confirm-repository bartytime4life/Kansas-Frontier-Matrix`.

The tool fails closed when:

- an M13-M24 prefix already exists under a different title;
- an exact-title milestone exists but is closed;
- a mapped issue is closed, resolves to a pull request, or already belongs to another milestone;
- manifest IDs, titles, descriptions, issue mappings, evidence pointers, checkpoint, or mutation policy are malformed;
- GitHub returns an unexpected or oversized response; or
- post-write verification does not match the manifest.

The tool does not delete milestones, reopen milestones, replace descriptions, set due dates, clear milestones, reassign conflicting issues, or change repository settings.

## Procedure

Run from the repository root.

### 1. Validate locally

```bash
python scripts/maintenance/sync_github_milestones.py validate
python -m unittest tests/governance/test_sync_github_milestones.py -v
```

Expected local result: twelve ordered records (`M13` through `M24`), ten uniquely mapped open issues, no due dates, and no network or mutation.

### 2. Preview current GitHub state

Supply a GitHub token through the environment using the approved local secret-handling method. Do not place it in the manifest, command arguments, shell history, logs, issue bodies, or committed files.

```bash
python scripts/maintenance/sync_github_milestones.py plan --assign-issues
```

Review every `CREATE_MILESTONE`, `KEEP_MILESTONE`, `ASSIGN_ISSUE`, and `KEEP_ISSUE` result. A `HOLD` requires a maintainer decision; do not edit the script to bypass it.

### 3. Apply explicitly

```bash
python scripts/maintenance/sync_github_milestones.py apply \
  --confirm-repository bartytime4life/Kansas-Frontier-Matrix \
  --assign-issues
```

The command preflights the full packet before its first write, creates only missing exact-title milestones, assigns only open unassigned issues, and then rereads GitHub to verify titles and assignments.

### 4. Record the bounded result

Record the exact command, source commit, created/kept milestone counts, assigned/kept issue counts, any `HOLD`, and the operator/reviewer route in the applicable GitHub review surface. Do not convert the console output into a receipt, proof, release record, or publication claim merely by copying it into the repository.

## Finite outcomes and exits

| Exit | Outcome | Meaning |
|---:|---|---|
| `0` | `VALIDATED`, planned, or `APPLIED` | The selected command completed its declared bounded checks. |
| `1` | `HOLD` | Existing GitHub state requires a maintainer decision before mutation. |
| `2` | `ERROR` | Manifest, environment, I/O, network, API, or verification failure. |

A zero exit proves only this milestone-maintenance contract for the inspected state. It does not prove issue completion, milestone completion, CI health, branch protection, security posture, release readiness, or production behavior.

## Correction and rollback

Repository rollback is a normal reviewed revert of the script, manifest, tests, and runbook. That revert does not automatically undo GitHub metadata already created.

For an incorrect applied milestone:

1. stop additional assignments;
2. preserve the command output and affected milestone/issue identifiers for audit;
3. compare the applied state with the reviewed manifest;
4. correct the GitHub metadata through an explicit maintainer action rather than an automatic delete or overwrite;
5. update the manifest and tests when the intended plan changes;
6. rerun `validate` and `plan`; and
7. record the correction and any issue reassignment decision in the appropriate GitHub review surface.

Do not delete milestones or silently move issues merely to make the manifest appear green.

## Open verification

- Existing M01-M12 milestone titles and descriptions remain outside this packet's mutation scope.
- Independent program, quality, security, and release stewardship assignments remain `NEEDS VERIFICATION`.
- Direct Projects V2 field/view automation remains outside scope.
- A future recurring automation lane requires separate security, permission, workflow, ownership, and rollback review.
