<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/source-intake-steward-summary-source-map
title: SourceIntake steward summary source map
type: exploratory-source-map
version: 1.0.0
status: proposed
owning_root: docs/
truth_posture: source-derived proposal; current repository behavior verified separately
related:
  - ../../../contracts/source/source_intake_steward_summary.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# SourceIntake steward summary source map

## Goal

Close the source-review presentation seam without creating another diff, review, or lifecycle object: render one already-valid `SourceIntakeRecord` into deterministic, redaction-aware Markdown a steward can act on.

## Source-derived requirements

The supplied `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` states in `KFM-IDX-UIX-003` that steward surfaces should present what changed, the materiality reason, policy implications, a rollback target, and explicit next-action options rather than raw diffs or free-text logs. The same source connects CDL drift specifically to `DriftSummary`, a human-readable Markdown steward summary, and a `SourceIntakeRecord` candidate.

Repository Flora source guidance independently says `steward_summary_ref` is a Markdown payload for human review and that a machine diff without a human-readable explanation is incomplete.

## Repository evidence and reuse decision

At the implementation base:

- `SourceIntakeRecord` and `DriftSummary` already have closed schemas, fixtures, semantic validation, and no-network CI;
- `tools/ci/render_stable_diff_summary.py` already establishes the repository pattern for deterministic reviewer-facing Markdown; and
- `tools/ci/build_stable_diff_review_handoff.py` already owns generic exact-input review handoff behavior.

The smallest non-duplicative increment is therefore a source-specific presentation adapter. It calls the existing source validator, derives only source-intake posture, emits Markdown, and leaves review handoff and authority to the existing governance lane.

## Translation choices

- Exact input bytes are bound by SHA-256 in the rendered summary.
- Sensitive or non-public drift suppresses narrative, changed fields, metrics, and identity details.
- Policy implications are derived from declared evidence, review, sensitivity, public-detail, and promotion posture.
- A work proposal is `READY_FOR_REVIEW` only when a prior identity is declared as rollback evidence; otherwise it is held.
- Next actions are finite display options. The renderer never invokes them.
- Invalid input produces a value-free error and no Markdown.

## Non-effects

This packet does not fetch a source, create or modify a SourceIntakeRecord, write lifecycle data, resolve evidence, execute policy, authenticate or approve review, create a review record, open an issue, send a notification, promote, release, deploy, publish, or authorize public use.

## Directory Rules basis

Accepted ADR-0029 makes the adopted Directory Governance Standard the placement authority. The packet uses existing source-contract, CI-tool, test, workflow, exploratory-doc, and generated-receipt roots and creates no parallel schema or authority home.
