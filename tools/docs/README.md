<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-docs-readme
title: tools/docs README
type: README
version: v0.1
status: draft
owner: TODO-docs-steward-plus-tooling-qa-owner
created: 2026-07-07
updated: 2026-07-07
policy_label: public
owning_root: tools/
responsibility: repo-wide documentation tooling, hygiene checks, render helpers, and docs QA handoff
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../docs/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../tools/qa/README.md
  - ../../tools/ci/README.md
notes:
  - "This README defines the governed boundary for documentation tooling under tools/docs/."
  - "Documentation content belongs under docs/ or the relevant responsibility root; tools/docs/ only owns executable helpers for checking, rendering, normalizing, or summarizing docs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/docs

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--tooling-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![authority](https://img.shields.io/badge/content--authority-docs%2F-lightgrey)

> **One-line purpose.** `tools/docs/` owns repo-wide executable helpers for documentation hygiene, rendering, normalization, metadata checks, link checks, and reviewer handoff reports. It does **not** own KFM doctrine, documentation authority, policy meaning, schema shape, contracts, or publication decisions.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Documentation tooling contract](#documentation-tooling-contract)
- [Inputs and outputs](#inputs-and-outputs)
- [Suggested helper families](#suggested-helper-families)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/docs/` is a tooling lane for documentation operations that need executable support across the repository.

It exists because KFM documentation is part of the governed system. Good documentation helps maintainers understand evidence boundaries, responsibility roots, policy posture, source roles, validation gates, release state, correction paths, rollback targets, and implementation uncertainty.

This lane may help produce or check documentation, but it must not blur the authority boundary:

- `docs/` owns human-facing doctrine, architecture, runbooks, ADRs, source documentation, and public-facing documentation content.
- `tools/docs/` owns executable support used to check, normalize, render, summarize, or inspect those documents.
- `policy/`, `contracts/`, and `schemas/` remain the sources of policy meaning, object-family meaning, and field-level shape.
- `release/`, `data/receipts/`, and `data/proofs/` remain the homes for release decisions and trust artifacts.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/docs/README.md` | **CONFIRMED** | This README defines the lane boundary. |
| Documentation helper scripts | **NEEDS VERIFICATION** | Confirm current branch contents before naming specific executables as implemented. |
| Docs linting behavior | **PROPOSED** | Should be fixture-backed before being treated as CI behavior. |
| Markdown metadata checks | **PROPOSED** | Recommended first-slice helper family. |
| Link / citation checks | **PROPOSED** | Must distinguish broken links from unsupported claims. |
| Render helpers | **PROPOSED** | May produce previews or artifacts; they do not publish docs. |
| Doctrine authority | **DENY here** | Doctrine lives in `docs/doctrine/` and accepted ADRs, not tool code. |

> [!IMPORTANT]
> Do not treat a documentation tool output as doctrine. A tool can detect missing metadata, unresolved links, bad anchors, broken tables, or mismatched front matter. It cannot decide that a claim is true, a source is admissible, a release is approved, or a directory-rule exception is valid.

[Back to top](#top)

---

## Governance boundary

KFM's documentation tooling must preserve the same trust membrane as the rest of the system:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Documentation helpers can support review and release readiness, but they do not move data or documents across lifecycle states. Publication remains a governed state transition.

### Allowed questions

`tools/docs/` may help answer:

- Does a README contain the expected KFM metadata block?
- Do intra-repo links resolve?
- Are Markdown anchors stable?
- Does a document include required truth-posture warnings?
- Does a generated documentation report differ from the prior report?
- Does a documentation page accidentally claim implementation maturity without evidence labels?
- Does a docs table or badge set follow the expected house pattern?

### Disallowed questions

`tools/docs/` must not decide:

- Is this doctrine accepted?
- Does this claim have sufficient evidence?
- Is this source legally or ethically admissible?
- Is this artifact safe for public release?
- Should this path override Directory Rules?
- Should this release be promoted?

Those decisions require the owning docs steward, ADRs, source stewards, policy checks, review state, release state, evidence closure, and rollback controls.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/docs/` include:

- Markdown metadata checkers.
- KFM meta-block validators.
- README shape checkers.
- Anchor and mini-TOC checkers.
- Link checking wrappers for local repository paths.
- Markdown normalization helpers that preserve meaning.
- Generated docs index builders.
- Docs report generators for CI handoff.
- Documentation drift scanners.
- Tools that compare stated path placement against Directory Rules references and flag items for review.
- Tools that find unlabelled implementation claims and suggest `CONFIRMED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` review.

Every helper should be:

- deterministic;
- safe to run locally and in CI;
- network-free by default;
- explicit about inputs and outputs;
- conservative about rewriting content;
- tested with public-safe fixtures;
- clear about whether it checks format, links, metadata, evidence labels, or prose hygiene.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/docs/` | Correct home | Reason |
|---|---|---|
| Doctrine documents | `docs/doctrine/` | Tooling checks doctrine; it does not own doctrine. |
| ADRs | `docs/adr/` | ADRs are governance records, not executable helpers. |
| Architecture prose | `docs/architecture/` | Human-facing architecture belongs in docs. |
| Source catalog pages | `docs/sources/` or `data/registry/sources/` depending on responsibility | Source documentation and source registry records are not docs tooling. |
| Generated release manifests | `release/` | Release authority does not live in tooling. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts belong in lifecycle roots. |
| Policy files | `policy/` | Policy meaning must not be embedded in docs helpers. |
| JSON Schemas | `schemas/contracts/v1/...` | Field shape belongs in schema home. |
| Contract definitions | `contracts/` | Object-family meaning belongs in contract home. |
| Tests | `tests/docs/` or existing test root convention | Tests prove helpers; helpers do not own tests. |
| Fixtures | `fixtures/` or `tests/docs/fixtures/` | Fixture data is not executable tooling. |
| One-off manual cleanup snippets | `scripts/maintenance/` or `scripts/one_off/` | Promote only durable, repo-wide tooling into `tools/docs/`. |

[Back to top](#top)

---

## Documentation tooling contract

A helper under `tools/docs/` should document its contract before being used in CI or review gates.

Minimum contract:

| Field | Requirement |
|---|---|
| Inputs | Explicit files, directories, or manifests. Avoid implicit whole-repo mutation. |
| Output | Stable JSON, Markdown report, or console summary. |
| Side effects | None by default. Any write mode must require an explicit flag. |
| Network | Off by default. Network checks require explicit opt-in and source rationale. |
| Determinism | Stable ordering and repeatable output. |
| Failure mode | Fail closed on malformed files, missing required metadata, or unsafe write target. |
| Evidence posture | Flag unsupported claims; do not invent evidence. |
| Rewrite posture | Preserve meaning; never silently rewrite doctrine, ADRs, rights statements, sensitivity notes, or release decisions. |

Recommended finite statuses:

| Status | Meaning |
|---|---|
| `pass` | The checked documentation surface satisfies the documented rule. |
| `warn` | A reviewable issue exists, but the helper cannot determine whether it is blocking. |
| `fail` | The checked surface violates a documented rule. |
| `error` | The helper could not safely complete. |
| `abstain` | The helper cannot decide because evidence, path authority, or configured scope is insufficient. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- Markdown files under `docs/`.
- README files under responsibility roots.
- ADR templates and ADR index files.
- Documentation inventories.
- Source catalog documentation pages.
- Generated docs reports from previous CI runs.
- Public-safe test fixtures.

### Unsuitable inputs

- private credentials;
- raw source dumps;
- living-person records;
- DNA/genomic data;
- exact sensitive archaeology or rare-species locations;
- unpublished release payloads outside their review workflow;
- unredacted policy-sensitive material.

### Suitable outputs

- CI-friendly JSON reports;
- Markdown review summaries;
- local normalized copies when explicitly requested;
- anchor/link inventories;
- metadata coverage reports;
- verification backlog suggestions.

Generated outputs should go to a caller-selected output path. The helper should not silently write into `docs/`, `release/`, `data/receipts/`, `data/proofs/`, or `artifacts/` without an explicit workflow decision.

[Back to top](#top)

---

## Suggested helper families

| Helper family | Proposed path | Purpose | Status |
|---|---|---|---|
| Metadata checker | `tools/docs/check_meta_block.py` | Verify KFM meta-block presence and required fields. | **PROPOSED** |
| README shape checker | `tools/docs/check_readme_shape.py` | Check expected README sections, badges, and governance warnings. | **PROPOSED** |
| Local link checker | `tools/docs/check_links.py` | Verify relative links and anchors within the repo. | **PROPOSED** |
| Truth-label scanner | `tools/docs/check_truth_labels.py` | Flag strong implementation claims without support labels. | **PROPOSED** |
| Docs index builder | `tools/docs/build_docs_index.py` | Emit a deterministic docs inventory for review. | **PROPOSED** |
| Markdown normalizer | `tools/docs/normalize_markdown.py` | Optional explicit-write hygiene pass that preserves meaning. | **PROPOSED** |
| Drift note helper | `tools/docs/find_directory_drift_notes.py` | Find path claims that should be compared against Directory Rules. | **PROPOSED** |

> [!NOTE]
> These names are recommended first-slice targets, not proof of current implementation. Confirm file presence on the active branch before invoking them.

[Back to top](#top)

---

## Validation

The first useful proof surface should be a small fixture-backed test suite.

Recommended structure:

```text
tests/docs/
├── README.md
├── test_check_meta_block.py
├── test_check_readme_shape.py
└── fixtures/
    ├── valid_readme.md
    ├── missing_meta_block.md
    ├── unresolved_link.md
    └── unsupported_implementation_claim.md
```

Recommended assertions:

- valid KFM meta block returns `pass`;
- missing required metadata returns `fail`;
- unresolved local links return `fail` or `warn` according to documented rule;
- unsupported implementation claims are flagged for review, not auto-rewritten;
- exact sensitive placeholders in fixtures are synthetic and public-safe;
- write mode is disabled unless explicitly requested;
- output order is deterministic.

Suggested future command pattern:

```bash
pytest -q tests/docs
```

```bash
python tools/docs/check_meta_block.py --path docs --output .tmp/docs-meta-report.json
```

[Back to top](#top)

---

## Review checklist

Before adding or changing a `tools/docs/` helper, reviewers should confirm:

- [ ] The helper has a narrow documented purpose.
- [ ] The helper does not redefine doctrine, policy, schema, contract, release, receipt, or proof authority.
- [ ] The helper is deterministic.
- [ ] Network access is off by default.
- [ ] Write mode is opt-in and safe.
- [ ] Public-safe fixtures cover pass, warn, fail, error, and abstain where relevant.
- [ ] The helper preserves KFM truth labels and uncertainty boundaries.
- [ ] The helper does not silently rewrite ADRs, doctrine, rights statements, or sensitivity notes.
- [ ] CI use is documented before a helper becomes blocking.
- [ ] Any generated report has a clear owner and retention location.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with lane contract | **DONE in this README** | Establishes boundary for documentation tooling. |
| Add metadata checker | **PROPOSED** | First executable helper for KFM meta-block coverage. |
| Add README shape fixtures | **PROPOSED** | Prevents root README drift. |
| Add local link checker | **PROPOSED** | Improves docs reliability without web dependency. |
| Add truth-label scanner | **PROPOSED** | Helps reviewers catch unsupported implementation claims. |
| Add CI report handoff | **PROPOSED / later** | Emits reviewer summaries without making doctrine decisions. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add `tools/docs/check_meta_block.py` plus public-safe `tests/docs/` fixtures. |
