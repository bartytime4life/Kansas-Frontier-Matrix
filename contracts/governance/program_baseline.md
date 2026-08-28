<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/program-baseline/v1
title: M01 Program Baseline Contract
version: v1.0.0
type: semantic-contract
status: proposed; repository-grounded; implementation-partial; non-authoritative
owners: "@bartytime4life via CODEOWNERS; accountable human review pending"
created: 2026-08-22
updated: 2026-08-22
responsibility_root: contracts/
owning_root: contracts/
responsibility: define a pinned and reversible M01 repository program-baseline projection without creating authority accepting decisions mutating issue state waiving failures activating sources changing lifecycle state or authorizing release deployment promotion or publication
policy_label: internal-governance; cite-or-abstain; no-self-authority; no-network-validation
truth_posture: CONFIRMED main@6aa1ce50dfc4e818e5f33d47fff24b6d06a1c91e accepted ADR inventory Directory Rules digest CODEOWNERS route root and alias projections current open-review queue tracker state local focused results and absent exact-main hosted runs / PROPOSED this contract schema instance validator fixtures workflow and receipt / UNKNOWN independent review branch-protection enforcement deployed consumers and production behavior
related:
  - ../../control_plane/program_baseline.json
  - ../../schemas/contracts/v1/governance/program_baseline.schema.json
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/INDEX.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/path_alias_register.yaml
  - ../../control_plane/README.md
  - ../../tools/validators/control_plane/validate_program_baseline.py
  - ../../tests/validators/test_validate_program_baseline.py
  - ../../.github/workflows/program-baseline.yml
tags: [kfm, m01, program-baseline, authority, directory-rules, control-plane, governance, rollback]
notes:
  - "This packet implements the first bounded slice for GitHub milestone 2 issue #3365."
  - "Google Drive documents are recorded as advisory lineage and were not modified."
  - "A failing or unrun check remains FAIL or NOT_RUN; this packet cannot convert it to PASS."
[/KFM_META_BLOCK_V2] -->

# M01 Program Baseline Contract

## Purpose

`ProgramBaseline` is the pinned, machine-readable coordination checkpoint for **M01 — Authority, Directory Rules & Program Baseline**. It records the repository state inspected before implementation and makes later drift, correction, and review decisions reproducible.

The canonical instance is [`control_plane/program_baseline.json`](../../control_plane/program_baseline.json). It is a governance projection, not governance authority. Its base is the exact pre-change commit `main@6aa1ce50dfc4e818e5f33d47fff24b6d06a1c91e`.

## Evidence and authority order

The packet applies this order:

1. accepted ADRs and adopted Directory Rules;
2. current repository contracts, schemas, policies, registries, validators, tests, workflows, manifests, and executable behavior;
3. current authoritative repository documentation;
4. connected Drive documents as advisory lineage only.

The repository inventory at the pinned base records three accepted numbered ADRs: `ADR-0006`, `ADR-0007`, and `ADR-0029`. The other 33 numbered records remain proposed, and 12 unassigned scaffolds remain non-decisions. The Directory Rules authority remains [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) at SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`, accepted through `ADR-0029`.

An accepted ADR does not prove its implementation. The packet therefore keeps decision status separate from `IMPLEMENTED`, `PARTIAL`, `ABSENT`, `SUPERSEDED`, `CONFLICTED`, `DEPRECATED`, and `NOT_INSPECTED` implementation classifications.

## Placement, ownership, consumers, and aliases

| Question | Verified answer | Boundary |
|---|---|---|
| Primary responsibility | `control_plane/` governance projection | Cannot contain policy source, domain truth, or release decisions. |
| Canonical path | `control_plane/program_baseline.json` | The path was absent at the pinned base; this slice proposes it. |
| Adjacent contract | `control_plane/README.md` | The README explains the root; it does not authorize the projection. |
| Review route | `@bartytime4life` through `.github/CODEOWNERS` | Routing is not proof that accountable or independent review occurred. |
| Machine consumers | Dedicated validator, focused tests, Make target, and read-only workflow | No runtime or public client is admitted. |
| Aliases | none | A future alias requires explicit registration and migration evidence. |

The validator requires the new slice paths to exist in the review worktree, but it replays authority and tracked-surface bytes from the pinned Git tree. A later edit cannot rewrite what the pre-change baseline observed.

## Repository and tracker snapshot

At the observation time:

- GitHub Milestone 2 was represented by issue `#3365`;
- overlap issues `#2768` and `#2874` were open and pinned to older baselines;
- the connected GitHub open-pull-request search returned no open PRs;
- no hosted workflow runs were observed for the exact merge commit SHA;
- the prior `trust_spine_baseline.yaml` remained a valid historical snapshot but no longer described the current program checkpoint.

Issue bodies and comments are coordination evidence. They do not create source, policy, review, merge, release, deployment, or publication authority.

## Material classifications

The current packet records:

- Directory Rules, the canonical ADR index, root registry, path-alias projection, and CODEOWNERS route as `IMPLEMENTED` only for their bounded repository surfaces;
- the control-plane README, historical repository-control snapshot, and object-family catalog as `PARTIAL` for current-state use;
- the earlier trust-spine snapshot as `IMPLEMENTED` for its immutable historical scope;
- the new program-baseline path as `ABSENT` at the pinned base and `PARTIAL` in this proposed slice.

The 19 object-family entries cover the 16 milestone-required families plus three other registered families. The structural validator passes, while the focused workflow-watch test remains red for nine declared paths. Catalog membership and orchestration closure are therefore not collapsed into one success claim.

## Deterministic validation

Run:

```bash
make program-baseline
```

The profile performs:

1. Draft 2020-12 schema and format validation;
2. duplicate-key and non-finite-number rejection;
3. canonical ordering, uniqueness, count, issue-set, and state/outcome checks;
4. pinned Git commit and authority-byte digest replay;
5. worktree existence checks for the proposed consumer slice;
6. exact positive and negative fixture polarity;
7. focused no-network unit tests; and
8. generated authoring-receipt integrity validation.

Validation findings expose stable codes and JSON-pointer fields only. Untrusted candidate values are not echoed.

### Inherited and unrun results

The baseline records two inherited failures without waiving them:

- repository topology: `FAIL`, nine unbaselined findings and 13 stale fingerprints;
- object-family workflow-watch tests: `FAIL`, nine missing path-filter bindings.

The exact-main hosted-check observation is `NOT_RUN`, not `PASS`. The focused program-baseline workflow can validate the proposed PR head later, but that result will not retroactively certify the pinned base or prove human review.

## Drive lineage

The packet records the connected **AI Build Operating Contract**, **Connected-Dots Architecture Brief**, and **Repository Structure Guiding Document** by Drive file ID, title, URL, and observed modification time. They remain advisory lineage. No Drive file was edited, copied, accepted, published, or converted into repository authority.

## Correction and rollback

The baseline becomes stale when the main branch advances, accepted ADR status or authority digests change, issue state/body changes, the open-PR queue changes, or a recorded validator/workflow outcome changes.

Before merge, rollback is closing the draft PR or deleting the review branch. After an authorized merge, use a same-path forward correction or a reviewed Git revert to `6aa1ce50dfc4e818e5f33d47fff24b6d06a1c91e`. Correct GitHub tracker claims with an append-only corrective comment; do not rewrite or erase historical evidence. Generated receipts remain append-only process memory.

## Non-effects

This packet does not:

- accept, reject, or supersede an ADR;
- activate or admit a source;
- approve policy or human review;
- change repository settings;
- expand or waive a drift baseline;
- mutate lifecycle, release, deployment, promotion, or publication state;
- make Drive guidance authoritative;
- authorize itself; or
- treat `NOT_RUN` or `SKIPPED` as success.

## Completion boundary

This slice is implementation-complete only when its local profile passes and its draft PR has exact-head hosted evidence. Milestone and issue closure remain human review actions. Open inherited failures and stale trackers remain explicit until separately corrected through their owning paths.
