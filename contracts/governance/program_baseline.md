<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/program-baseline/v2
title: M01 Program Baseline Contract
version: v2.0.0
type: semantic-contract
status: proposed; repository-grounded; implementation-partial; non-authoritative
owners: "@bartytime4life via CODEOWNERS; accountable human review pending"
created: 2026-08-22
updated: 2026-10-14
responsibility_root: contracts/
owning_root: contracts/
responsibility: define a pinned and reversible M01 repository program-baseline projection without creating authority accepting decisions mutating issue state waiving failures activating sources changing lifecycle state or authorizing release deployment promotion or publication
policy_label: internal-governance; cite-or-abstain; no-self-authority; no-network-validation
truth_posture: CONFIRMED main@514b2367638778a0a0b6e45a6451aea70c762909 accepted ADR inventory derived from the pinned index Directory Rules digest CODEOWNERS route root and alias projections open-review queue tracker state local validation results and exact-main hosted check-runs at observation time / PROPOSED this contract schema profile v2 instance validator fixtures workflow and receipt / CARRIED FORWARD Drive lineage from the 2026-08-22 baseline without re-observation / UNKNOWN independent review branch-protection enforcement deployed consumers and production behavior
related:
  - ../../control_plane/program_baseline.json
  - ../../schemas/contracts/v1/governance/program_baseline.schema.json
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/INDEX.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0048-external-mirror-names-are-externally-fixed.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/path_alias_register.yaml
  - ../../control_plane/external_mirror_register.yaml
  - ../../control_plane/repository_governance_parity.yaml
  - ../../control_plane/README.md
  - ../../tools/validators/control_plane/validate_program_baseline.py
  - ../../tests/validators/test_validate_program_baseline.py
  - ../../.github/workflows/program-baseline.yml
tags: [kfm, m01, program-baseline, authority, directory-rules, control-plane, governance, rollback]
notes:
  - "This packet implements a bounded slice for GitHub milestone 2 issue #3365."
  - "v2 is a same-path forward fix of the v1 baseline pinned to main@6aa1ce50dfc4e818e5f33d47fff24b6d06a1c91e; the instance records that baseline under supersedes, and the v1 bytes remain in Git history."
  - "v2 removes every snapshot-specific constant from the schema and validator; counts, base-path status, and required unresolved items are derived from pinned evidence."
  - "Google Drive documents are recorded as advisory lineage, were not modified, and were not re-observed for v2."
  - "A failing, held, or unrun check remains FAIL, HOLD, or NOT_RUN; this packet cannot convert it to PASS."
[/KFM_META_BLOCK_V2] -->

# M01 Program Baseline Contract

## Purpose

`ProgramBaseline` is the pinned, machine-readable coordination checkpoint for **M01 — Authority, Directory Rules & Program Baseline**. It records the repository state inspected at one exact main commit and makes later drift, correction, and review decisions reproducible.

The canonical instance is [`control_plane/program_baseline.json`](../../control_plane/program_baseline.json). It is a governance projection, not governance authority. Profile `kfm.program-baseline.m01.v2` pins it to `main@514b2367638778a0a0b6e45a6451aea70c762909`. It names the baseline it replaces in `supersedes`: `kfm-program-baseline-main-6aa1ce50dfc4` at `main@6aa1ce50dfc4e818e5f33d47fff24b6d06a1c91e`.

## What changed from v1

The v1 baseline was correct for its base. It went stale as main advanced, as its correction section predicted. Its schema and validator also hard-coded facts of that one snapshot, so a refresh could not pass without rewriting the rules. Profile v2 keeps the v1 shape and replaces those constants with checks derived from evidence:

| v1 constant | v2 rule |
|---|---|
| 36 numbered ADRs and 12 scaffolds | Accepted IDs, the proposed count, and the scaffold count must equal what the pinned `docs/adr/INDEX.md` bytes yield (see below). |
| `base_path_status` is always `ABSENT` | `ABSENT` or `PRESENT`, and it must agree with whether the canonical path exists in the base tree. |
| Topology `FAIL`/9, workflow-watch `FAIL`/9, hosted `NOT_RUN` | The `exact_main_hosted_checks`, `object_family_workflow_watch_tests`, and `repository_topology` observations must be present. Their outcomes are whatever was observed. |
| Three fixed unresolved tokens | One unresolved token per non-`PASS` observation, plus `human_review_pending` (see below). |
| No lineage field | An optional `supersedes` object names the prior baseline. Its commit must be a strict Git ancestor of `base.sha`. |

The validator rejects an instance that still declares the v1 profile with the single finding `PROFILE_VERSION_UNSUPPORTED` at `/profile`. It does not apply v2 rules to it. The v1 instance stays readable in Git history and is bound by its own generated receipt.

## Evidence and authority order

The packet applies this order:

1. accepted ADRs and adopted Directory Rules;
2. current repository contracts, schemas, policies, registries, validators, tests, workflows, manifests, and executable behavior;
3. current authoritative repository documentation;
4. connected Drive documents as advisory lineage only.

At the pinned base the ADR index marks 11 numbered records `accepted`: `ADR-0006`, `ADR-0007`, `ADR-0029`, `ADR-0038`, `ADR-0040`, `ADR-0044`, `ADR-0045`, `ADR-0046`, `ADR-0047`, `ADR-0048`, and `ADR-0049`. The other 38 numbered records are `proposed`, and 11 unassigned scaffolds remain non-decisions. The Directory Rules authority remains [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) at SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`, accepted through `ADR-0029` and unchanged since v1.

The index's status badge still reports five accepted records, while its table and prose report eleven. The baseline counts the table and records the badge as an unresolved item. It does not edit the index.

### ADR counting rule

The validator replays the index bytes from the pinned tree. It reads only the two marker-delimited tables, using the same rule as `tools/validators/validate_adr_index.py`:

- **Numbered records:** the rows between `<!-- ADR_INDEX_TABLE_START -->` and `<!-- ADR_INDEX_TABLE_END -->`. The first row must be the exact six-column header, followed by a separator row. Each later table row is one record. Its effective status is the third cell, with backticks removed and lower-cased. `accepted_ids` must equal the set of `accepted` rows, and `proposed_count` must equal the number of `proposed` rows. `superseded` and `rejected` rows are valid, but neither count includes them.
- **Unassigned scaffolds:** every data row between `<!-- ADR_SCAFFOLD_TABLE_START -->` and `<!-- ADR_SCAFFOLD_TABLE_END -->` under the exact three-column header.

Text outside the tables does not count, including badges, notes, and prose. A missing marker, a wrong header, a row with the wrong cell count, an unknown status, or a repeated ID makes the index `ADR_INDEX_UNPARSEABLE`. The validator does not guess a count. Applied to the v1 base, the rule reproduces the v1 hand-recorded values: three accepted, 33 proposed, and 12 scaffolds.

An accepted ADR does not prove its implementation. The packet keeps decision status separate from the `IMPLEMENTED`, `PARTIAL`, `ABSENT`, `SUPERSEDED`, `CONFLICTED`, `DEPRECATED`, and `NOT_INSPECTED` implementation classifications.

## Placement, ownership, consumers, and aliases

| Question | Verified answer | Boundary |
|---|---|---|
| Primary responsibility | `control_plane/` governance projection | Cannot contain policy source, domain truth, or release decisions. |
| Canonical path | `control_plane/program_baseline.json` | The path is `PRESENT` at the v2 base: it held the v1 instance. v2 replaces those bytes at the same path. |
| Adjacent contract | `control_plane/README.md` | The README explains the root; it does not authorize the projection. |
| Review route | `@bartytime4life` through `.github/CODEOWNERS` | Routing is not proof that accountable or independent review occurred. |
| Machine consumers | Dedicated validator, focused tests, Make target, and read-only workflow | No runtime or public client is admitted. |
| Aliases | none | A future alias requires explicit registration and migration evidence. |

The validator requires the slice paths to exist in the review worktree. It replays authority and tracked-surface bytes from the pinned Git tree, so a later edit cannot rewrite what the baseline observed.

## Repository and tracker snapshot

At the observation time:

- GitHub Milestone 2 was represented by issue `#3365`.
- All three tracked issues (`#2768`, `#2874`, `#3365`) were open. Each one's latest checkpoint cites an older main commit, so each is `stale_at_base`. `#2768` and `#3365` cite `main@2d6808a9edc99c1850aca375afb5f0894772e723` in their 2026-10-13 comments. `#2874` cites `fd03c91c88a06fc7d4e097775ec62ede6d3b498c` in its 2026-09-16 handoff.
- The open pull requests were the ones listed in `base.open_pull_requests`. Main advanced past the base while the evidence was being gathered, so this queue is the queue at `observed_at`, not the queue at the base commit. The instance records `main_advanced_past_base_before_observation_completed` as unresolved.
- Hosted check-runs for the exact base commit were read after they had all completed: 109 runs, 107 `success`, 2 `skipped` (`Trigger_APIsec_scan` and `dependency-review`), and none failed. `exact_main_hosted_checks` records `PASS` with those counts in its scope. The two skips stay explicit as an unresolved item and are not counted as passes.

Issue bodies and comments are coordination evidence. They do not create source, policy, review, merge, release, deployment, or publication authority.

## Material classifications

The current packet records:

- Directory Rules, the canonical ADR index, the root registry, the path-alias projection, and the CODEOWNERS route as `IMPLEMENTED`, only for their bounded repository surfaces;
- the external-mirror register as `IMPLEMENTED` for its bounded scope. It projects accepted `ADR-0048`, the topology validator reads it, and its parity check passes. Content parity is not hosted equivalence or human acceptance;
- the control-plane README and object-family catalog as `PARTIAL` for current-state use. The workflow-watch tests now pass, but ten required families remain conflicted;
- the repository-governance parity projection as `PARTIAL`. Its expected topology matches the observed result, but its conformance outcome remains `HOLD_INHERITED`;
- the repository-control state projection as `SUPERSEDED`, as the projection itself declares;
- the earlier trust-spine snapshot as `IMPLEMENTED` for its immutable historical scope.

## Unresolved-item rule

For every validation observation whose `outcome` is not `PASS`, `unresolved_items` must contain the token `<observation id>_<outcome in lower case>`. Examples are `repository_governance_parity_hold` and `exact_main_hosted_checks_not_run`. `human_review_pending` is always required.

The rule also runs in reverse. An unresolved token of that form whose observation now has a different outcome is reported as `UNRESOLVED_ITEM_STALE`. A refreshed baseline cannot keep a stale failure claim, and it cannot drop a live one. Other unresolved tokens are free-form and are not checked against observations.

## Deterministic validation

Run:

```bash
make program-baseline
```

The profile performs:

1. Draft 2020-12 schema and format validation;
2. duplicate-key and non-finite-number rejection;
3. retired-profile rejection;
4. canonical ordering, uniqueness, count, issue-set, and state/outcome checks;
5. pinned Git commit and authority-byte digest replay;
6. ADR count derivation from the pinned index bytes;
7. base-path status agreement and `supersedes` ancestry against Git;
8. the unresolved-item rule;
9. worktree existence checks for the consumer slice;
10. exact positive and negative fixture polarity, with Git checks enabled;
11. focused no-network unit tests; and
12. generated authoring-receipt integrity validation for each baseline receipt, each replayed from its own artifact commit.

Validation findings expose stable codes and JSON-pointer fields only. Untrusted candidate values are not echoed.

### Recorded results

The v2 instance records each command it lists as it was actually run against the base tree. A held or failed result stays `HOLD` or `FAIL` with its failure class. A hosted state that was not observed stays `NOT_RUN`, never `PASS`. The focused program-baseline workflow can validate a later PR head, but that result does not certify the pinned base or prove human review.

## Drive lineage

The packet carries forward the three Drive entries from the v1 baseline unchanged: the **AI Build Operating Contract**, the **Connected-Dots Architecture Brief**, and the **Repository Structure Guiding Document**. They were not re-observed for v2, so their recorded modification times are the 2026-08-22 observations, and `drive_lineage_not_reobserved_since_prior_baseline` remains unresolved. They remain advisory lineage. No Drive file was edited, copied, accepted, published, or converted into repository authority.

## Correction and rollback

The baseline goes stale when main advances, an accepted ADR's status changes, an authority or tracked-surface digest changes, an issue's state or body changes, the open-PR queue changes, or a recorded validator or workflow outcome changes. The correction is a same-path forward fix: refresh the instance at a new base, record the replaced baseline in `supersedes`, and add a new generated receipt.

Before merge, rollback is closing the draft PR or deleting the review branch. After an authorized merge, use a same-path forward correction, or a reviewed Git revert to `514b2367638778a0a0b6e45a6451aea70c762909`, which restores the v1 packet. Correct GitHub tracker claims with an append-only corrective comment; do not rewrite or erase historical evidence. Generated receipts remain append-only process memory, and the 2026-08-22 receipt is kept unchanged.

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
- treat `NOT_RUN`, `SKIPPED`, or `HOLD` as success.

## Completion boundary

This slice is implementation-complete only when its local profile passes and its draft PR has exact-head hosted evidence. Milestone and issue closure remain human review actions. Open holds, stale trackers, and carried-forward lineage remain explicit until separately corrected through their owning paths.
