<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-qa-readme
title: tools/qa README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-docs-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; qa-tooling
owning_root: tools/
responsibility: QA tooling boundary for coverage checks, link checks, drift scans, and reviewer summaries
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../validators/README.md
  - ../docs/README.md
  - ../diff/README.md
  - ../proof_pack/README.md
  - ../../tests/
notes:
  - "This README documents the QA tooling lane. It does not confirm executable files."
  - "QA reports support review and do not replace validators, tests, source records, proof records, or release review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/qa

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-QA--tooling-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/qa/` is the tooling lane for KFM quality-assurance helpers: coverage analyzers, link checks, drift scans, CI reviewer summaries, and related repo-quality reports.

---

## Purpose

`tools/qa/` holds deterministic helpers that make repository quality issues visible to maintainers.

A QA helper may check README coverage, metadata blocks, links, stale references, orphaned folders, parent index drift, badge/status consistency, TODOs, or CI summary formatting.

A QA report is a review aid. It is not final acceptance by itself.

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/qa/README.md` | **CONFIRMED** | This README replaces the previous stub. |
| QA executables | **PROPOSED / NEEDS VERIFICATION** | No script is claimed here. |
| `tools/` root authority | **CONFIRMED in repo evidence** | Parent README names `tools/qa/` as QA tooling. |

---

## Authority boundary

| Responsibility | Home |
|---|---|
| QA helper tooling | `tools/qa/` |
| Validators | `tools/validators/` |
| Documentation hygiene helpers | `tools/docs/` |
| Diff helpers | `tools/diff/` |
| Tests | `tests/` |
| Contracts, schemas, and policy | `contracts/`, `schemas/`, `policy/` |
| Receipts, proofs, catalog, and release records | dedicated `data/` and `release/` roots |

---

## What belongs here

- README coverage checks.
- Metadata block checks.
- Local link checks.
- Parent index drift scans.
- Placeholder and TODO scans.
- Last-reviewed scans.
- CI reviewer-summary renderers.
- QA report formatters.

---

## What does not belong here

| Do not put in `tools/qa/` | Correct home |
|---|---|
| Validators of record | `tools/validators/` |
| Contracts | `contracts/` |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release records | `release/` |
| Tests | `tests/qa/` or accepted test convention |

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `QA_PASS` | Configured checks passed. |
| `QA_WARN` | Review issues were found. |
| `QA_FAIL` | Configured checks failed. |
| `MISSING_README` | Expected README is absent. |
| `MISSING_METADATA` | Required metadata is absent. |
| `BROKEN_LINK` | A referenced path failed the configured check. |
| `INDEX_DRIFT` | Parent index and child folders appear out of sync. |
| `ABSTAIN` | Helper cannot decide with available context. |
| `ERROR` | Helper could not safely complete. |

---

## Validation

Suggested future test surface:

```text
tests/qa/
├── README.md
├── test_qa_checker.py
└── fixtures/
```

Suggested future command pattern:

```bash
pytest -q tests/qa
```

> [!NOTE]
> This is a proposed validation surface, not proof that `tests/qa/` exists.

---

## Review checklist

- [ ] Helper is deterministic.
- [ ] Helper is explicit about scan scope.
- [ ] Output is a review aid.
- [ ] Output is machine-readable where practical.
- [ ] Tests use safe fixtures.
- [ ] Executable claims are backed by repo evidence.

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub. |
| Next smallest safe change | Add `tests/qa/README.md` and fixture conventions. |
