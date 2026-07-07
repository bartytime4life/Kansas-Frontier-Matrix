<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-diff-readme
title: tools/diff README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner
created: 2026-07-07
updated: 2026-07-07
policy_label: public
owning_root: tools/
responsibility: repo-wide diff helpers for deterministic reviewer and CI comparisons
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../tests/diff/README.md
  - ../../tools/ci/README.md
notes:
  - "This README defines the governed boundary for diff helpers. It does not claim that every named helper already exists."
  - "Diff tooling compares artifacts and emits machine-readable reports; it does not own policy, promotion, release, proof, receipt, or review authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/diff

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![scope](https://img.shields.io/badge/scope-comparator--only-informational)
![publication](https://img.shields.io/badge/publication-not--an--authority-lightgrey)

> **One-line purpose.** `tools/diff/` owns deterministic, machine-readable comparison helpers for KFM artifacts so reviewers, tests, CI jobs, and promotion gates can see what changed without letting a diff tool become a policy engine, proof store, receipt store, release authority, or truth source.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Current thin-slice target](#current-thin-slice-target)
- [Expected report envelope](#expected-report-envelope)
- [Inputs and outputs](#inputs-and-outputs)
- [Suggested commands](#suggested-commands)
- [Validation](#validation)
- [Roadmap](#roadmap)
- [Review checklist](#review-checklist)

---

## Purpose

`tools/diff/` is a repo-wide tooling lane under `tools/`. Its job is to compare two local artifacts in a deterministic way and emit a small report that humans and machines can inspect.

The first useful target is a stable JSON diff helper for KFM trust-adjacent artifacts such as receipt-like objects, EvidenceBundle-like payloads, release-manifest-like files, source-descriptor snapshots, fixture outputs, and reviewer-facing CI payloads.

The lane is intentionally narrow:

1. Normalize comparison behavior.
2. Report stable added, removed, and changed fields.
3. Keep output machine-readable.
4. Preserve deterministic ordering.
5. Leave policy and publication decisions to their owning roots.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/diff/README.md` | **CONFIRMED** | This file documents the lane boundary and expected thin-slice contract. |
| `tools/diff/stable_diff.py` | **PROPOSED-to-create / NEEDS VERIFICATION** | Name used for the first executable target. Confirm branch state before invoking. |
| `tests/diff/test_stable_diff.py` | **PROPOSED-to-create / NEEDS VERIFICATION** | Expected proof surface for the first executable helper. |
| `tests/diff/fixtures/...` | **PROPOSED-to-create / NEEDS VERIFICATION** | Suggested fixture home for test-only inputs. |
| Nested semantic diff | **OUT OF SCOPE for first slice** | The first contract should compare top-level JSON keys only unless an ADR or test expands it. |
| Policy interpretation | **DENY here** | Policy meaning belongs in `policy/` and promotion/release validators, not this helper. |
| Promotion authority | **DENY here** | Promotion remains a governed state transition, not a diff output. |

> [!IMPORTANT]
> Treat this README as a lane contract, not runtime proof. Any claim that a helper exists, runs in CI, or gates promotion must be verified against the current branch, tests, workflow logs, emitted reports, or release receipts.

[Back to top](#top)

---

## Governance boundary

KFM's trust membrane remains intact:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

`tools/diff/` may compare artifacts produced along that path, but it does not move data between lifecycle phases. It does not publish, promote, approve, redact, sign, release, or rollback anything.

Use this lane to answer questions like:

- What top-level fields changed between two JSON reports?
- Did a generated manifest change deterministically?
- Did a receipt-like object drift between two runs?
- Can CI display a stable summary of a candidate artifact delta?

Do **not** use this lane to answer questions like:

- Is this source admissible?
- Is this evidence sufficient?
- Is this artifact safe to publish?
- Is this release approved?
- Is this claim true?

Those questions belong to source descriptors, EvidenceBundle resolution, policy checks, validators, promotion decisions, review state, release manifests, receipts, proofs, and rollback controls.

[Back to top](#top)

---

## What belongs here

`tools/diff/` may contain small executable helpers whose primary responsibility is deterministic comparison.

Good fits:

- JSON comparison helpers.
- Manifest comparison helpers.
- Receipt-like object diff helpers.
- Stable report emitters for CI handoff.
- Shared comparison utilities used by `tests/diff/` and CI rendering tools.

A helper belongs here only when it is:

- repo-wide rather than domain-owned;
- deterministic;
- safe to run without network access;
- explicit about its input and output contract;
- free of publication side effects;
- tested through `tests/diff/` or adjacent CI tests.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/diff/` | Correct home | Reason |
|---|---|---|
| Policy bundles or Rego rules | `policy/` | Policy meaning is not owned by diff tooling. |
| JSON Schema definitions | `schemas/contracts/v1/...` | Field-level shape belongs in the schema authority root. |
| Contract definitions | `contracts/` | Object-family meaning belongs in contracts. |
| Promotion decisions | `release/` | Diff reports can inform review, but they do not approve release. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust objects are stored in lifecycle roots, not tool folders. |
| Test files | `tests/diff/` | Tests prove this lane; they are not part of the executable tool lane. |
| Test fixtures | `tests/diff/fixtures/` or `fixtures/` | Fixtures are data for tests, not tools. |
| Reviewer prose rendering | `tools/ci/` or `tools/qa/` | Rendering summaries is adjacent but separate from computing diffs. |
| Source fetching | `connectors/` or `pipelines/` | Diff tools compare local artifacts; they do not harvest sources. |

[Back to top](#top)

---

## Current thin-slice target

The recommended first executable is:

```text
tools/diff/stable_diff.py
```

### Proposed first behavior

`stable_diff.py` should:

1. accept two local JSON file paths;
2. parse both files as JSON objects;
3. normalize object key ordering for deterministic comparison;
4. compare top-level keys only in the first slice;
5. emit a stable JSON report;
6. optionally return a non-zero exit code when differences are found and `--fail-on-change` is passed;
7. fail closed on missing, unreadable, or malformed input.

### Non-goals for the first behavior

The first helper should not attempt:

- nested semantic diff;
- geospatial topology comparison;
- EvidenceBundle sufficiency analysis;
- policy interpretation;
- release approval;
- reviewer Markdown rendering;
- automatic writes into `data/receipts/`, `data/proofs/`, `release/`, or `artifacts/`.

[Back to top](#top)

---

## Expected report envelope

The first stable JSON report should stay small and deterministic.

```json
{
  "tool": "stable-diff",
  "status": "changed",
  "blocking": false,
  "left": "tests/diff/fixtures/changed/left.json",
  "right": "tests/diff/fixtures/changed/right.json",
  "summary": {
    "added": ["new_key"],
    "removed": ["old_key"],
    "changed": ["shared_key"]
  }
}
```

Recommended finite statuses:

| Status | Meaning | Blocking default |
|---|---|---:|
| `same` | Inputs are equivalent under the helper's documented comparison rules. | `false` |
| `changed` | Inputs are valid and comparable, with deterministic differences. | `false` unless `--fail-on-change` is used |
| `error` | At least one input could not be read, parsed, or compared safely. | `true` |

Recommended exit codes:

| Exit code | Meaning |
|---:|---|
| `0` | Same, or changed without `--fail-on-change`. |
| `1` | Changed with `--fail-on-change`. |
| `2` | Input, parse, usage, or comparison error. |

[Back to top](#top)

---

## Inputs and outputs

### Inputs

Input files should be local, explicit, and reviewable.

Suitable inputs include:

- test fixtures;
- generated validation reports;
- candidate release manifests;
- receipt-like JSON objects;
- source descriptor snapshots;
- catalog or layer manifest snapshots;
- EvidenceBundle-like payload fixtures.

Inputs should not include:

- secrets;
- credentials;
- raw private source dumps;
- unrestricted living-person data;
- exact sensitive archaeology or ecology coordinates;
- unpublished public-client payloads that have not passed their policy gates.

### Outputs

Diff output is a derived QA artifact. It may be written to a temporary path, CI artifact path, or reviewer handoff path.

If a diff report becomes promotion-significant, the owning promotion or release workflow must decide how it is represented in receipts, proofs, manifests, or rollback records. `tools/diff/` does not make that decision.

[Back to top](#top)

---

## Suggested commands

> [!NOTE]
> These commands are the intended first-slice interface once `tools/diff/stable_diff.py` and its tests exist on the active branch. Confirm file presence before running them.

```bash
pytest -q tests/diff/test_stable_diff.py
```

```bash
python tools/diff/stable_diff.py \
  --left tests/diff/fixtures/changed/left.json \
  --right tests/diff/fixtures/changed/right.json \
  --output tests/diff/fixtures/_tmp.diff-report.json
```

```bash
python tools/diff/stable_diff.py \
  --left tests/diff/fixtures/changed/left.json \
  --right tests/diff/fixtures/changed/right.json \
  --fail-on-change
```

[Back to top](#top)

---

## Validation

The first proof surface should be narrow and fixture-driven.

Recommended files:

```text
tests/diff/
├── README.md
├── test_stable_diff.py
└── fixtures/
    ├── same/
    │   ├── left.json
    │   └── right.json
    ├── changed/
    │   ├── left.json
    │   └── right.json
    └── trust_chain/
        ├── receipt_prior.json
        └── receipt_current.json
```

Recommended first assertions:

- equivalent JSON under different key order returns `status == "same"`;
- one added, one removed, and one changed top-level key returns deterministic sorted arrays;
- `--fail-on-change` returns a non-zero exit while still emitting machine-readable output when configured to write output;
- malformed JSON fails closed with `status == "error"` or a documented non-zero error path;
- missing files fail closed;
- receipt-like fixture drift is reported as ordinary JSON object drift, not interpreted as policy or promotion state.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace README stub with lane contract | **DONE in this README** | Documents scope, boundaries, and first-slice behavior. |
| Add `stable_diff.py` | **PROPOSED** | First executable comparator. |
| Add `tests/diff/` proof pack | **PROPOSED** | Locks deterministic comparison behavior. |
| Add CI renderer handoff | **PROPOSED** | Convert machine report into reviewer-facing summary without changing diff semantics. |
| Wire selected reports into promotion review | **PROPOSED / later** | Promotion validators may consume diff reports, but diff remains non-authoritative. |
| Expand beyond top-level keys | **NEEDS ADR or explicit test-backed decision** | Avoid silent semantic expansion. |

[Back to top](#top)

---

## Review checklist

Before merging a new diff helper or changing this lane's behavior, reviewers should confirm:

- [ ] The helper is deterministic.
- [ ] The helper runs without network access.
- [ ] The helper has no publication, promotion, policy, proof-storage, or receipt-storage side effects.
- [ ] The output envelope is documented.
- [ ] Exit codes are documented.
- [ ] Tests cover same, changed, malformed, and missing-input cases.
- [ ] Fixture data is public-safe.
- [ ] Sensitive, private, or exact-location data is not embedded in fixtures.
- [ ] Any promotion-significant use is owned by promotion/release tooling, not by the diff helper itself.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement; executable helper still needs branch verification. |
| Next smallest safe change | Add `tools/diff/stable_diff.py` plus `tests/diff/test_stable_diff.py` and minimal public-safe fixtures. |
