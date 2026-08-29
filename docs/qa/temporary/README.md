<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-qa-temporary-readme
title: docs/qa/temporary/ — Reserved QA Documentation Hold
type: documentation-lane-readme
version: v0.1.0
status: repository-grounded; routing-and-hold boundary; placement-unresolved; inactive; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes repository changes, but no accepted steward or consumer for this child lane is established
created: 2026-08-28
updated: 2026-08-28
current_path: docs/qa/temporary/README.md
owning_root: docs/
policy_label: repository-facing; qa; temporary; hold; non-authoritative
responsibility: Prevent the unresolved docs/qa/temporary path from being used as tracked scratch space, generated QA output, evidence, executable validation, release proof, or publication authority while routing each responsibility to its established repository surface.
base_commit: 332a371f0be1aae68690853fba368a6289d2dab4
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
truth_posture: CONFIRMED this directory contained only a one-newline README at the pinned base, its parent explicitly withholds authorization for scratch or generated-output use, and no executable producer, consumer, retention rule, required check, release binding, or publication path is established / PROPOSED this same-path routing-and-hold boundary / HOLD long-term placement and qa-versus-quality classification / UNKNOWN legitimate future responsibility, steward, retention, migration, and retirement outcome
related:
  - ../README.md
  - ../../README.md
  - ../../quality/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../artifacts/qa/README.md
  - ../../../tests/README.md
  - ../../../tools/validators/README.md
  - ../../../tools/validators/docs/README.md
  - ../../../.github/workflows/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Reserved QA documentation hold

> **One-line purpose.** `docs/qa/temporary/` is a documented hold around an
> unresolved tracked path. It is not a scratch directory, generated-report
> destination, evidence store, validator, workflow, release gate, or public
> interface.

> [!IMPORTANT]
> **Safe current conclusion at `main@332a371f0be1`:** before this
> same-path documentation replacement, the directory contained only a one-newline
> README. No repository evidence establishes a producer, consumer, format,
> retention period, cleanup process, required check, release dependency, or
> publication path for this lane.

## Purpose and authority

The parent [human QA guidance boundary](../README.md) explicitly states that this
child must not become generated-output storage, scratch space, or a canonical
evidence lane merely because it exists. This README makes that negative boundary
visible without inventing a use for the path.

The canonical [documentation root](../../README.md), accepted
[Directory Rules](../../doctrine/directory-rules.md), and
[ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) govern
documentation placement. The adopted direct-child map does not establish
`docs/qa/` or this child as a canonical category. The nearby
[quality-guidance lane](../../quality/README.md) is current implementation
evidence, not authority to infer that `qa/temporary/` has the same
responsibility.

| Question | Current answer |
|---|---|
| Is this an admitted documentation category? | **No.** Long-term placement and the `qa/` versus `quality/` relationship remain on hold. |
| May tools write reports here? | **No.** No producer, format, retention rule, cleanup contract, or generated relationship is established. |
| May contributors use it for tracked scratch notes? | **No.** Temporary local work must remain outside the tracked canonical tree. |
| Does this README prove a QA result? | **No.** It records routing and uncertainty only. |
| Can presence of this directory approve review, release, deployment, or publication? | **No.** Those are distinct governed states. |

## Current inventory

Verified from the pinned repository tree:

```text
docs/qa/temporary/
└── README.md
```

This inventory proves only that the path is tracked. It does not prove active
use, accepted placement, implementation maturity, or authority.

## Routing matrix

Route work by responsibility instead of by the word “temporary.”

| Material or activity | Current owning surface | Boundary |
|---|---|---|
| Human QA interpretation and review guidance | [`docs/qa/`](../README.md) or an accepted responsibility-specific documentation lane | Prose explains bounded evidence; it does not execute or approve. |
| Broader quality guidance | [`docs/quality/`](../../quality/README.md) | Existing lane with its own placement caveat; not an alias for this path. |
| Executable tests | [`tests/`](../../../tests/README.md) | Test results prove only their declared assertions and revision. |
| Reusable validators | [`tools/validators/`](../../../tools/validators/README.md) | Executable checking belongs with the validator responsibility. |
| Documentation validators | [`tools/validators/docs/`](../../../tools/validators/docs/README.md) | Bounded link, graph, metadata, freshness, and assessment checks; not release authority. |
| Workflow orchestration and hosted logs | [`.github/workflows/`](../../../.github/workflows/README.md) and external CI storage | A workflow conclusion is orchestration evidence, not a retained governed record by itself. |
| Non-authoritative generated QA output | [`artifacts/qa/`](../../../artifacts/qa/README.md) or declared external CI storage | Use only when the producer and retention boundary explicitly select that destination. |
| Evidence, receipts, proofs, decisions, and releases | Their accepted `data/`, contract, policy, and `release/` responsibilities | Do not collapse authority into documentation or transient output. |
| Local experiments, editor notes, caches, downloads, and scratch files | An ignored or external ephemeral workspace selected by the owning tool | Do not commit them under this directory. |

A file does not become safe, canonical, retained, or reviewable merely because it
is Markdown or because a pull request contains it.

## What may change here

Until an accepted placement decision establishes another outcome, changes should
be limited to:

- corrections to this routing-and-hold boundary;
- evidence-backed documentation of a newly observed dependency or conflict;
- an accepted decision that classifies, migrates, or retires the path; and
- directly required navigation updates for that accepted outcome.

Do not add child reports, screenshots, recordings, logs, fixtures, generated
summaries, reviewer notes, benchmark results, evidence packets, receipts, or
release artifacts here. Do not create an automated writer or cleanup job merely
to populate the directory.

## Inputs, outputs, and failure posture

This boundary consumes current repository evidence and adopted placement
doctrine. Its only output is contributor routing plus an explicit hold. It emits
no test result, validation report, evidence claim, approval, policy decision,
receipt, release record, deployment state, or public artifact.

When a proposed file has no accepted owner or destination, stop and classify the
responsibility. Preserve `UNKNOWN`, `NEEDS VERIFICATION`, or `HOLD` rather
than using this directory as a convenient fallback.

## Validation

Run the bounded documentation checks from the repository root:

```bash
python tools/validators/docs/link-check/check_links.py \
  docs/qa/temporary/README.md docs/qa/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required docs/qa/temporary/README.md docs/qa/README.md
```

The link checker covers repository-local files, directories, images, and
fragments. The metadata checker covers the bounded metadata envelope. Passing
either command confirms only its exercised documentation QA scope at that
revision. It does not resolve placement, create a producer or retention policy,
approve review, or authorize release or publication.

Review the complete base-to-head diff for one H1, balanced fences, resolvable
relative links, truthful labels, final newline, no sensitive payload, and no
unrelated changed path.

## Maintenance, correction, and rollback

Recheck this boundary if the parent lane, `docs/quality/`, adopted Directory
Rules, a QA producer, retention requirements, required checks, artifact routing,
or the direct directory contents change.

For an unmerged documentation change, rollback is closing the draft pull request
or reverting its focused branch commits. After merge, prefer a visible
forward-correction that preserves the hold. Reverting to the prior one-newline
blob `8b137891791fe96927ad78e64b0aad7bded08bdc` removes guidance only; it must not be treated as deleting a QA
result, undoing a workflow, withdrawing evidence, or reversing release,
deployment, or publication.

## Open verification register

| ID | Open item | Current posture |
|---|---|---|
| `QA-TEMP-001` | Legitimate responsibility, if any, for this child lane | **UNKNOWN** |
| `QA-TEMP-002` | Relationship among `docs/qa/`, `docs/quality/`, and generated QA output | **HOLD / NEEDS DIRECTORY REVIEW** |
| `QA-TEMP-003` | Accepted steward, writers, readers, format, retention, and cleanup behavior | **NOT ESTABLISHED** |
| `QA-TEMP-004` | Migration or retirement plan if no responsibility is accepted | **NEEDS DECISION** |
| `QA-TEMP-005` | Required checks and independent review for a future placement change | **NEEDS VERIFICATION** |

## Changelog

| Version | Date | Change | Runtime effect |
|---|---|---|---|
| v0.1.0 | 2026-08-28 | Replaced the one-newline placeholder with a repository-grounded routing-and-hold boundary; prohibited scratch, generated-output, evidence, release, and publication misuse. | None; documentation only. |

[Back to top](#top)
