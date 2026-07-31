<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-link-check-readme
title: tools/validators/docs/link-check README
type: README
version: v0.2
status: draft; bounded-executable; local-only; no-network; non-authoritative
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-07-30
policy_label: repository-facing; docs-validator; link-check; markdown-qa; non-authoritative
owning_root: tools/
responsibility: deterministic local Markdown target and fragment validation without deciding doctrine, evidence sufficiency, source admissibility, policy, review, release, or publication
truth_posture: CONFIRMED standard-library local target checker, synthetic tests, and changed-Markdown CI wiring / NEEDS VERIFICATION broader Markdown dialect coverage, historical repository backlog, hosted exact-head results, and required-check coupling
related:
  - ../README.md
  - ../../README.md
  - ../../../../tests/validators/docs/link-check/README.md
  - ../../../../.github/workflows/link-check.yml
  - ../../../../docs/doctrine/directory-rules.md
notes:
  - "External targets are classified as EXTERNAL_TARGET_UNVERIFIED and are never requested."
  - "A passing result proves local target resolution only within the supplied Markdown scope."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/docs/link-check/` — Bounded Local Markdown Link Check

![status](https://img.shields.io/badge/status-bounded--executable-success)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![network](https://img.shields.io/badge/network-denied-critical)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)

> **Purpose.** Validate repository-local inline Markdown file, directory,
> image, and fragment targets deterministically while abstaining from all
> external URL availability claims.

**Quick navigation:** [Status](#status) · [Repository fit](#repository-fit) ·
[Inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Behavior](#behavior-contract) ·
[Run](#run) · [CI](#ci-integration) · [Rollback](#rollback)

## Status

| Surface | Current evidence | Limit |
|---|---|---|
| `check_links.py` | **CONFIRMED executable** | Standard-library, local inline Markdown targets only. |
| Focused tests | **CONFIRMED executable** | Synthetic temporary fixtures; no production documents or external requests. |
| `link-check.yml` | **CONFIRMED command-bearing definition** | Hosted exact-head result and required-check coupling remain **NEEDS VERIFICATION**. |
| External URLs | **EXTERNAL_TARGET_UNVERIFIED** | Classified and reported; never requested. |
| Whole repository | **NOT CLAIMED** | CI checks changed Markdown, not every historical document. |

## Repository fit

The accepted Directory Rules place reusable validator implementation under
`tools/`, conformance proof under `tests/`, and GitHub orchestration under
`.github/`. This existing lane is therefore a `PLACE` outcome: no new authority
root or parallel documentation store is created.

| Responsibility | Owning surface |
|---|---|
| Local link-check implementation | This directory |
| Synthetic behavior proof | [`tests/validators/docs/link-check/`](../../../../tests/validators/docs/link-check/README.md) |
| Pull-request and main-push orchestration | [`.github/workflows/link-check.yml`](../../../../.github/workflows/link-check.yml) |
| Documentation content and meaning | Each document's responsibility root |
| Evidence, policy, review, and release | Their existing governed roots; never this checker |

## Accepted inputs

- explicit UTF-8 `.md` or `.markdown` files;
- directories, recursively limited to Markdown files;
- a strict `<base-sha>...HEAD` changed-file selector;
- repository-relative links, root-relative links, images, directories, heading
  fragments, and explicit HTML `id` or `name` anchors.

Every input must resolve within the declared repository root with exact path
casing. Symbolic-link inputs and links inside recursively scanned input
directories are denied. Inputs larger than 5 MB fail closed.

## Exclusions

This bounded version does not:

- request external URLs, follow redirects, or claim external availability;
- parse reference-style Markdown links or inline HTML `href`/`src` attributes;
- validate citations, reference semantics, link text, or document authority;
- support ignores, allowlists, suppressions, or generated report files;
- edit documentation;
- validate source admission, evidence closure, policy, review, proof, release,
  deployment, or publication.

Unsupported features remain visible scope limits. They are not silently treated
as passing coverage.

## Behavior contract

| Outcome | Exit | Meaning |
|---|---:|---|
| `DOC_LINK_CHECK_PASS` | `0` | No failing local target was found in the supplied scope. |
| `DOC_LINK_CHECK_FAIL` | `1` | At least one local target, fragment, case, or root-boundary check failed. |
| `ERROR` | `2` | Input, encoding, size, repository, or changed-file discovery could not complete safely. |
| `LOCAL_TARGET_MISSING` | contributes to `1` | File, directory, or image is absent or case-mismatched. |
| `ANCHOR_MISSING` | contributes to `1` | Target exists, but the fragment does not match a heading or explicit anchor. |
| `PATH_ESCAPE` | contributes to `1` | A local target resolves outside the repository root. |
| `EXTERNAL_TARGET_UNVERIFIED` | informational | External target was classified but not requested. |

Findings are sorted by repository-relative source path, line, outcome, and
target. External findings retain only scheme and hostname; path, query,
fragment, and credentials are omitted from logs. JSON output uses stable key
ordering and compact encoding.

## Run

Check explicit files or directories:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  README.md docs/
```

Check Markdown changed from an immutable base:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --git-diff <BASE_SHA>...HEAD \
  --format json
```

Run the synthetic no-network suite:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/link-check \
  --pattern 'test_*.py' \
  --verbose
```

## CI integration

The stable workflow name `link-check` and job id `docs-link-check` are retained.
The job uses read-only contents permission, a GitHub-hosted runner, no secrets,
no OIDC, and no write or artifact-upload step. It runs the focused tests and
then checks local targets in Markdown files changed by the triggering revision.

When a triggering revision changes no Markdown, the command reports
`changed_markdown_empty` with zero checked documents. That is an explicit empty
scope, not whole-repository link coverage.

## Review checklist

- [x] Local paths and anchors are checked deterministically.
- [x] Path escape and exact-case mismatch fail closed.
- [x] Symbolic-link inputs fail closed.
- [x] External URLs remain unrequested and visibly unverified.
- [x] Tests use synthetic fixtures and standard-library runners.
- [x] Workflow permissions remain read-only and names remain stable.
- [ ] Reference-style and inline-HTML link parsing — **DEFERRED**.
- [ ] Historical whole-repository remediation — **DEFERRED**.
- [ ] Hosted exact-head result and ruleset coupling — **NEEDS VERIFICATION**.

## Rollback

Before merge, close the draft PR and abandon its branch. After an authorized
merge, revert the focused commit. The workflow and job names are unchanged, so
rollback does not require a check-name migration; separately verify any ruleset
coupling before removing an active check.

## Last reviewed

| Field | Value |
|---|---|
| Review date | 2026-07-30 |
| Evidence base | `main@3c4f01cf5133d57a8522df0c30d83681702dd179` |
| Human review | Pending |

[Back to top](#top)
