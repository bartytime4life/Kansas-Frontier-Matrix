<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0041
title: Proportional Handling of Inherited Repository Holds
type: architecture-decision-record
version: v1.0-draft
status: proposed
effective_decision_status: proposed
owners: ["@bartytime4life"]
created: 2026-09-18
updated: 2026-09-18
policy_label: public; governance; fail-closed
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0041-proportional-handling-of-inherited-repository-holds.md
responsibility: "Propose a deterministic, non-authorizing classification for unchanged inherited repository holds without weakening changed-area validation, topology authority, release, or publication controls."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  source_commit: 97be53c4bafe44bb78e6df6b29e0273350d75744
  source_blob: 3e7030ebc9e8949a4b59dd791ce5a1c46f75a700
  source_path: "docs/adr/ADR-0041 — Proportional handling of inherited repository holds"
  source_path_had_markdown_extension: false
related:
  - ADR-0038-trusted-base-topology-correction-transitions.md
  - ADR-0040-catalog-redirect-metadata-corrections.md
  - ../../tools/validators/directory_governance/validate_repository_topology.py
  - ../../tools/validators/directory_governance/repository_topology_baseline.json
tags: [kfm, governance, topology, inherited-hold, changed-area, fail-closed]
notes:
  - "PR #4632 added the proposal without a Markdown extension, metadata block, or canonical-index entry; this transition normalizes its identity without accepting the decision."
  - "The proposal cannot classify PRs that modify the held subject or any governing validator, baseline, register, schema, contract, workflow, authority document, or decision record."
  - "No implementation, required-check change, merge authority, release, deployment, promotion, publication, or repository-setting change is authorized."
[/KFM_META_BLOCK_V2] -->

# ADR-0041 — Proportional handling of inherited repository holds

**Status:** PROPOSED  
**Supersedes:** no existing decision  
**Amends if accepted:** ADR-0038 operational handling only  
**Does not amend:** ADR-0004, ADR-0029, public trust boundaries, release or publication authority

## Context

A pull request can reproduce a failure already present at its trusted base even
when the pull request does not change the failed subject or its governing
control. Treating every inherited failure as newly introduced drift blocks safe,
reversible authoring without improving attribution.

The repository still needs to fail closed for new drift, worsened drift,
ambiguous comparisons, governance-control edits, and any change touching the
held subject.

## Decision

Introduce `EXPECTED_INHERITED_HOLD` as a non-authorizing check outcome. It may
be emitted only when all of the following are proved from repository-owned,
deterministic evidence:

1. The trusted-base and candidate findings have identical rule ID, subject,
   fingerprint, evidence digest, severity, and baseline disposition.
2. The candidate does not add, remove, or mutate any finding for that subject.
3. The pull request does not modify the held subject tree.
4. The pull request does not modify the applicable validator, baseline,
   correction register, schema, contract, workflow, authority document, or
   decision record.
5. The trusted-base comparison is available, exact, and bound to the pull
   request base SHA. Missing or ambiguous evidence remains blocking.
6. Every changed-area validator still passes.

`EXPECTED_INHERITED_HOLD` permits ordinary review and merge consideration for
an unrelated, reversible change. It does not mark the inherited condition
resolved and does not authorize source admission, lifecycle movement, release,
deployment, promotion, publication, or repository-setting changes.

Any pull request touching the failed subject or a governing control remains on
the existing strict path. New or changed drift remains a failure.

## Required implementation

- Add a deterministic base-versus-candidate classifier with a closed output
  vocabulary.
- Keep the existing strict validator unchanged as the source of each finding.
- Emit both trusted-base and candidate identities without exposing private
  evidence members.
- Add positive coverage for byte-identical inherited findings.
- Add negative coverage for changed fingerprints, evidence, severity,
  baselines, subjects, validators, registers, workflows, authority documents,
  unavailable bases, and partial comparisons.
- Document which required check consumes the classifier and preserve a stable
  blocking result for every nonmatching case.

## Rollback

Remove the classifier and restore unconditional blocking for inherited holds.
No source, lifecycle, release, or publication state is changed by rollback.

## Acceptance boundary

Merging this proposal does not accept it. Acceptance requires an explicit owner
decision recorded through the repository authority process. Implementation must
start from a later trusted base containing the accepted decision.
