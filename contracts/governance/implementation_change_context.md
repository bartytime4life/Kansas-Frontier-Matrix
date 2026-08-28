<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/implementation-change-context
title: ImplementationChangeContext Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Governance steward · Review steward · Contract steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; review-support; non-authoritative
related:
  - ../../schemas/contracts/v1/governance/implementation_change_context.schema.json
  - ../../fixtures/contracts/v1/governance/implementation_change_context/cases.json
  - ../../tools/validators/governance/validate_implementation_change_context.py
  - ../../tools/validators/governance/implementation_change_context_model.py
  - ../../tools/validators/governance/implementation_change_context_git.py
  - ../../tests/validators/governance/test_implementation_change_context.py
  - ./implementation_decision_record.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, implementation-change, review-context, git, deterministic, ai]
notes:
  - "Adapted from FluencyLoop's changed-slice and mechanical-context concepts without copying its scripts, private calibration profile, session transcript, or branch-management behavior."
  - "This contract contains Git path/status/count metadata only. It never stores raw diff hunks, file contents, prompts, private reasoning, or person profiles."
  - "A decision-capture recommendation is a deterministic attention signal, not a correctness, approval, merge, release, or publication gate."
[/KFM_META_BLOCK_V2] -->

# ImplementationChangeContext

> A deterministic, value-minimized review-support record for one committed Git change range: which paths changed, how Git classified them, how many text lines changed, which responsibility roots are involved, and which mechanical signals suggest that one or more `ImplementationDecisionRecord`s would help a reviewer.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `LOCAL_GIT_METADATA_ONLY` |
| Authority created | `NONE` |
| Schema | `schemas/contracts/v1/governance/implementation_change_context.schema.json` |
| Builder and validator | `tools/validators/governance/validate_implementation_change_context.py` |
| Public-use posture | Denied; internal review-support input only |

A conforming context proves only that a local committed Git range was represented consistently under this profile. It does **not** prove that the change is correct, complete, secure, policy-compliant, reviewed, mergeable, releasable, published, or supported by admissible evidence.

## Why this object exists

The repository already has a complete pull-request template and now has `ImplementationDecisionRecord` for the few non-obvious choices that shaped a change. The remaining gap is mechanical scope collection. Reviewers and AI tools otherwise spend context repeatedly reading whole files or reconstructing changed-path facts from prose.

`ImplementationChangeContext` fills only that gap. It separates two responsibilities:

1. **Mechanical collection** — Git paths, statuses, text-line counts, binary markers, responsibility roots, and deterministic signal codes.
2. **Irreducible explanation** — chosen mechanism, rationale, rejected or deferred alternatives, evidence, validation, reviewer questions, and rollback in `ImplementationDecisionRecord`.

The context never infers why code was written. It never writes a decision record automatically. A reviewer may use the context to decide that no durable rationale record is needed.

## Source adaptation

FluencyLoop's `slice-context.sh` collects changed hunks and metadata so an agent can focus on a bounded slice rather than reread whole files. It also applies cheap heuristics to suggest where a real decision may exist. KFM adopts the mechanical-efficiency idea while narrowing the data and authority surface:

| Upstream idea | KFM adaptation |
|---|---|
| Work from the changed slice | Bind one full base SHA and one full head SHA. |
| Let scripts do mechanical work | A deterministic Python tool reads local Git metadata only. |
| Surface likely decision areas | Closed signal codes and a documented score produce `decision_capture_recommended`. |
| Include raw changed hunks | Rejected. KFM stores no raw diff or file contents in this object. |
| Reconstruct skipped work | Build a `DRAFT` context from the committed range; any rationale remains separately authored and reviewable. |
| Branch supplies feature scope | Adapted to an explicit repository plus immutable commit range; no branch naming authority is created. |

No FluencyLoop script, template, hook, plugin manifest, or runtime is vendored.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. Semantic meaning belongs under `contracts/governance/`; machine shape belongs under `schemas/contracts/v1/governance/`; synthetic examples belong under `fixtures/contracts/v1/governance/`; deterministic repository tooling and validation belong under `tools/validators/governance/` and `tests/validators/governance/`; CI belongs under `.github/workflows/`; source adaptation belongs under `docs/intake/exploratory/`; AI authoring provenance belongs under `data/receipts/generated/`.

No new responsibility root or parallel decision, review, receipt, proof, policy, release, catalog, source-registry, or publication home is created.

## Object meaning

An `ImplementationChangeContext` binds:

- repository identity in `owner/name` form;
- immutable base and head commit SHAs;
- the head commit time normalized to UTC seconds;
- sorted changed-file entries;
- recomputed totals, responsibility roots, signal codes, score, and recommendation;
- optional references to separately authored `ImplementationDecisionRecord`s;
- explicit value-minimization, all-false permissions, and non-effects.

### File entries

Each file entry carries:

| Field | Meaning |
|---|---|
| `path` | Destination or current repository-relative POSIX path. |
| `previous_path` | Source path for a Git rename or copy; otherwise `null`. |
| `status` | `ADDED`, `MODIFIED`, `DELETED`, `RENAMED`, `COPIED`, or `TYPE_CHANGED`. |
| `additions` / `deletions` | Git numstat counts for text; `null` for binary files. |
| `binary` | Whether Git numstat reported binary content. |

Paths are metadata. A sensitive-looking path is not proof that a secret or restricted value exists, and a normal-looking path is not proof that content is safe.

## Deterministic identity

The context identifier covers only the immutable mechanical range and file projection:

```text
context_id = "kfm:implementation-change-context:" +
  SHA-256(RFC8785-JCS({
    profile,
    repository,
    base_sha,
    head_sha,
    files
  }))
```

`generated_at`, review status, summary, and `implementation_decision_refs` are excluded. A later review transition or addition of decision references therefore does not create a second identity for the same Git change range.

The validator recomputes the entire summary and the context ID. Declared values cannot override the mechanical projection.

## Mechanical signal profile

Signals are deterministic review-attention hints. They are not policy decisions, risk ratings, reviewer assignments, or proof that a change contains a design decision.

| Signal | Condition | Score |
|---|---|---:|
| `AUTHORITY_SURFACE` | Paths touch contracts, schemas, policy, control plane, release, doctrine/ADR, or trust-bearing data lanes. | 2 |
| `BINARY_CONTENT` | At least one binary file is present. | 1 |
| `CROSS_ROOT` | More than one top-level responsibility root is touched. | 1 |
| `DELETION_OR_RENAME` | At least one deletion or rename is present. | 2 |
| `DEPENDENCY_SURFACE` | A recognized dependency manifest or lockfile changes. | 2 |
| `DOCUMENTATION_ONLY` | Every changed path has a documentation suffix. | 0 |
| `LARGE_CHANGE` | At least 20 files or 500 changed text lines. | 1 |
| `PUBLIC_SURFACE` | Paths touch deployable/public-facing app, runtime, UI, web, API, or MapLibre package surfaces. | 2 |
| `SENSITIVE_PATH_NAME` | A narrow path-name pattern such as `.env`, `secrets`, `credentials`, or `private_keys` appears. | 3 |
| `TEST_OR_FIXTURE_ONLY` | Every top-level root is `tests` or `fixtures`. | 0 |
| `WORKFLOW_SURFACE` | A path under `.github/workflows/` changes. | 2 |

`decision_capture_recommended` is true when the score is at least 2. The threshold exists only to conserve review attention. It does not waive KFM review when false and does not force a decision record when true.

## Finite outcomes

The validator returns one outcome:

- `READY` — internally consistent and marked `READY_FOR_REVIEW`; when decision capture is recommended, at least one separate decision-record reference is declared;
- `HOLD` — well formed but still `DRAFT`, or marked review-ready without a decision-record reference despite the mechanical recommendation;
- `ERROR` — malformed, unsafe, noncanonical, hash-inconsistent, summary-inconsistent, or otherwise contradictory.

CLI exit codes are `0` for `READY`, `3` for `HOLD`, and `2` for `ERROR`. A `HOLD` does not block Git or merge by itself; it is the finite state of this review-support profile.

## Local Git builder

The implementation is split into a closed model/validation module, a local-Git adapter, and the public CLI wrapper so schema semantics remain independent from Git process execution.

The builder:

- requires the repository top-level directory;
- resolves supplied refs to full commit SHAs;
- requires the base to be an ancestor of the head;
- reads `git diff --name-status` and `git diff --numstat` with rename detection;
- records no raw patch text or file bytes;
- derives `generated_at` from the head commit time and normalizes it to UTC;
- bounds the range to 1,000 changed files;
- emits a closed JSON document and validates it before returning its finite outcome.

It does not fetch, pull, contact GitHub, inspect issues or pull requests, stage files, modify the index, create commits, push, or write repository state unless an explicit `--output` file is supplied by the caller.

## Backfill posture

For already merged work, build a `DRAFT` context from the original base and merged head. Then inspect contemporaneous evidence such as the PR body, ADRs, tests, and review comments. Any reconstructed rationale belongs in a separate `ImplementationDecisionRecord` and remains `DRAFT` or `NEEDS_VERIFICATION` until a human confirms it. Unknown alternatives stay unknown; the context must not invent them.

## Validation

```bash
python -m pytest -q \
  tests/validators/governance/test_implementation_change_context.py

python tools/validators/governance/validate_implementation_change_context.py \
  --cases
```

Build a local context without network access:

```bash
python tools/validators/governance/validate_implementation_change_context.py \
  --build-from-git \
  --repo-root . \
  --repository bartytime4life/Kansas-Frontier-Matrix \
  --base <full-or-resolvable-base-ref> \
  --head <full-or-resolvable-head-ref> \
  --status DRAFT \
  --output /tmp/kfm-implementation-change-context.json
```

The expected exit code for a newly built `DRAFT` context is `3` (`HOLD`).

## Trust boundary

This object is a review aid. It does not:

- create or resolve evidence;
- authenticate GitHub state, branch protection, review, or repository permissions;
- read or preserve raw diff text or file content in the output;
- infer rationale, alternatives, correctness, or implementation completeness;
- decide policy, sensitivity, rights, approval, merge, promotion, release, deployment, or publication;
- create a person profile, competence score, private calibration record, prompt transcript, or hidden-reasoning record.

## Rollback

Revert the feature commit or close the draft pull request. No migration, reprocessing, source activation, external state, release artifact, deployment, cache invalidation, or publication rollback is required because this slice creates only an inactive contract, schema, synthetic fixtures, deterministic local tooling, tests, documentation, workflow validation, and authoring provenance.
