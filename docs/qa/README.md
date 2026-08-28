<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-qa-readme
title: docs/qa/ - Human QA Guidance Boundary
type: documentation-lane-readme
version: v1.0
status: "repository-grounded; placement-hold; non-authoritative"
owners:
  - "@bartytime4life"
created: 2026-05-24
updated: 2026-08-14
policy_label: repository-facing
owning_root: docs/
responsibility: "Explain bounded QA review without taking authority from tests, validators, workflows, evidence, policy, or release."
truth_posture: cite-or-abstain
current_path: docs/qa/README.md
evidence_base_commit: c61309b69f3754345db38e6bd2560834d5c3b5e9
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/qa/temporary/README.md
  - docs/quality/maplibre-perf-governance.md
  - tests/README.md
  - tools/validators/README.md
  - .github/workflows/README.md
  - artifacts/qa/README.md
tags: [kfm, docs, qa, review, validation]
notes:
  - "Replaces a one-byte placeholder with a BOUNDARY_COMPACT lane contract."
  - "Placement remains HOLD; this update does not resolve qa/ versus quality/ or authorize temporary/."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/qa/` - Human QA Guidance Boundary

> `docs/qa/` explains how reviewers inspect and interpret bounded KFM quality-assurance evidence. It does not execute tests, own validators, store generated reports, approve policy, or authorize release.

> [!IMPORTANT]
> A green test, workflow conclusion, validator pass, report, badge, or review note proves only its declared scope and revision. It does not create an `EvidenceBundle`, human approval, promotion, release, deployment, publication, correction closure, or rollback authority.

## Purpose and placement

At `main@c61309b69f3754345db38e6bd2560834d5c3b5e9`, this README and `temporary/README.md` were one-newline placeholders. The repository also contains [`docs/quality/`](../quality/), whose relationship to this lane is unresolved.

Accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../doctrine/directory-rules.md). The parent [`docs/`](../README.md) root is canonical, but `qa/` is absent from the adopted direct-child map. Therefore:

- **CONFIRMED:** the path exists and this is a same-path placeholder replacement.
- **HOLD:** long-term placement and the `qa/` versus `quality/` distinction.
- **NEEDS VERIFICATION:** stewardship, consumers, required-check coupling, and the purpose of `temporary/`.
- **UNKNOWN:** any deployed QA service, full-suite coverage, production parity, or release authority associated with this path.

## Boundary contract

Appropriate content is human-readable review guidance: scoped checklists, result interpretation, manual inspection procedures, introduced-versus-inherited triage, limitations, escalation, correction, and rollback guidance.

| Responsibility | Owning surface |
|---|---|
| Executable conformance | [`tests/`](../../tests/README.md) |
| Reusable validators and checkers | [`tools/validators/`](../../tools/validators/README.md) |
| Workflow orchestration | [`.github/workflows/`](../../.github/workflows/README.md) |
| Generated QA output | [`artifacts/qa/`](../../artifacts/qa/README.md) or external CI storage |
| Contracts, schemas, and policy | `contracts/`, `schemas/`, and `policy/` |
| Evidence, receipts, proofs, and catalogs | governed `data/` lanes |
| Release, correction, withdrawal, and rollback decisions | `release/` |

`docs/qa/temporary/` must not become generated-output storage, scratch space, or a canonical evidence lane merely because it exists.

## Review interpretation

Preserve the exact vocabulary of the owning contract. `PASS` supports only the tested assertion; `FAIL` identifies an unmet expectation; `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, `SKIPPED`, and `PENDING` must remain visible and must not be translated into success.

A QA note should identify the revision, scope, acceptance criteria, evidence, commands or hosted checks, positive and negative cases, introduced and inherited findings, sensitive-domain limitations, correction owner, rollback implication, and reviewer disposition.

## Validation

Current bounded documentation checks include `docs-meta-block`, `link-check`, `docs-document-graph`, `docs-stale-scan`, and `docs-build`. Review this change for one valid metadata block, one H1, valid local links and anchors, honest placement status, no authority collapse, public-safe content, final newline, generated-receipt integrity, and exact-head hosted results.

```bash
python tools/validators/validate_generated_receipt.py   data/receipts/generated/<receipt>.json

git diff --check
```

## Open verification

- Decide whether to admit `docs/qa/`, migrate its guidance, split it by responsibility, or retire it after reference migration.
- Compare `docs/qa/` and `docs/quality/` identities and consumers before any rename or move.
- Determine whether [`temporary/README.md`](temporary/README.md) has a legitimate documentation responsibility.
- Inventory existing QA guidance and generated-output retention before adding child documents.
- Identify or explicitly decline a root-wide full-suite contract.

## Correction and rollback
Correct inaccurate statements in place, preserve stable anchors, update the generated receipt, and keep unresolved placement conflicts visible. After an authorized merge, revert the focused README and receipt commit to restore the prior placeholder blob `8b137891791fe96927ad78e64b0aad7bded08bdc`.

---

**Current edition:** v1.0 | **Placement:** `HOLD` | **Authority:** human guidance only

[Back to top](#top)
