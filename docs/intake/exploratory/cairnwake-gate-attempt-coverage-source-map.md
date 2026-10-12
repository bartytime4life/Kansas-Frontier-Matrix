<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/cairnwake-gate-attempt-coverage-source-map
title: Cairnwake Gate Attempt Coverage Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; read-only-source-adaptation
owners: OWNER_TBD — Intake steward · Validation steward
created: 2026-08-28
updated: 2026-08-28
policy_label: internal; exploratory; no-authority
owning_root: docs/
responsibility: source-grounded mapping from an external gate-accounting correction to a bounded KFM validation candidate without treating an autonomous-agent report or its operational data as repository evidence or authority
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/validation/gate_attempt_coverage_assessment.md
  - ../../../control_plane/object_family_register.yaml
tags: [kfm, cairnwake, gate, refusals, attempts, denominators, source-map]
[/KFM_META_BLOCK_V2] -->

# Cairnwake Gate Attempt Coverage Source Map

## Read-only source

- Cairn, Wake 186, retrieved 2026-08-28: https://cairnwake.com/wake-186.html

The external report describes a mail gate that retained successful-send records while refusal records were discarded. Its correction records refusals separately under a distinct signature domain, counts them beside successful sends, and excludes refusal records from the gate's behavioral feedback. This is an external operational report, not a KFM fact or authority.

## KFM comparison

Current KFM controls include individual operation receipts, denied source-admission states, negative-state distinctions, and reconciliation profiles. The repository's object-family register also records the `run_receipt` family as `CONFLICTED` across multiple candidate contract and schema surfaces. No inspected generic validation profile reconciles `ATTEMPTED = ADMITTED + REFUSED + ERROR + UNOBSERVED`, declares denominator inclusion for every class, and prohibits refusal records from acting as occurrence evidence or same-gate feedback.

## Bounded adaptation

The candidate keeps only the accounting mechanism:

- classify every synthetic attempt exactly once;
- keep admitted, refused, error, and unobserved rows in distinct signature domains;
- carry opaque references and counts, never submitted or rejected payloads;
- reproduce count reconciliation and explicit metric denominators;
- prevent refusal records from proving the guarded action occurred or entering same-gate feedback;
- preserve incomplete terminal coverage as a visible state.

It does not send a message, configure a gate, ingest a live receipt, select among the conflicted KFM run-receipt carriers, retain rejected content, update behavioral feedback, admit a source, or create release, deployment, publication, or public-use authority. The source is an idea input; KFM semantics and any future integration remain governed by repository doctrine and steward review.
