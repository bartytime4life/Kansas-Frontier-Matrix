<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-critical-structure-readme
title: tools/validators/docs/critical-structure README
type: README
version: v0.1
status: draft; bounded-executable; local-only; no-network; non-authoritative
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-09-10
updated: 2026-09-10
policy_label: repository-facing; docs-validator; structural-integrity; non-authoritative
owning_root: tools/
responsibility: deterministic structural-integrity validation for an explicit bounded set of critical Markdown documents without interpreting claims or granting governance, review, release, or publication authority
truth_posture: CONFIRMED standard-library checker and synthetic no-network tests / NEEDS VERIFICATION hosted exact-head execution, steward acceptance, additional critical-document enrollment, and required-check coupling
related:
  - ../README.md
  - ../../../../CONTRIBUTING.md
  - ../../../../tests/validators/docs/critical-structure/README.md
  - ../../../../.github/workflows/validator-suite.yml
notes:
  - "The initial enrolled document is CONTRIBUTING.md because current-main inspection found a full self-insertion that existing link checks did not reject."
  - "The checker is intentionally separate from link target resolution, metadata validation, and document-graph construction."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/docs/critical-structure/`

> **Purpose.** Fail closed on a small set of high-signal Markdown corruption
> shapes in explicitly enrolled critical documents, without making network
> requests or changing repository state.

## Repository fit

This is a `PLACE` outcome under accepted ADR-0029 and the adopted Directory
Rules: reusable validation logic belongs under `tools/`, executable proof under
`tests/`, CI orchestration under `.github/`, and generated-work provenance under
`data/receipts/generated/`. It creates no new authority root or document copy.

## Initial scope

`CONTRIBUTING.md` is the only default input. The validator checks:

- normalized repository-relative, non-symlink UTF-8 input read through a 2 MB
  byte bound;
- a final newline;
- closed fenced-code and HTML-comment boundaries;
- no visible unresolved merge-conflict markers;
- exactly one visible ATX H1 and the expected contributor-contract title;
- exactly one visible occurrence of that title token, including mid-line text
  but excluding inline code;
- unique source-normalized, case-folded ATX H2 bodies; and
- the interrupted-link/embedded-heading shape `]# Heading` outside code and
  comments.

Headings inside valid fenced examples or HTML comments are inert. Well-formed
same-line inline-code spans are inert for raw-token checks. Multiline code spans
and full CommonMark block interpretation are outside this narrow profile and
may fail conservatively. Findings contain only path, line, stable reason code,
and bounded structural detail; document content is never echoed.

## Outcome grammar

| Outcome | Exit | Meaning |
|---|---:|---|
| `DOC_CRITICAL_STRUCTURE_PASS` | `0` | No enrolled structural invariant failed. |
| `DOC_CRITICAL_STRUCTURE_FAIL` | `1` | One or more deterministic structural findings were emitted. |
| `ERROR` | `2` | Input path, type, encoding, size, or filesystem safety prevented inspection. |

Failure reason codes are `FINAL_NEWLINE_MISSING`, `UNCLOSED_FENCE`,
`UNCLOSED_HTML_COMMENT`, `MERGE_CONFLICT_MARKER`,
`INTERRUPTED_LINK_OR_HEADING`, `H1_COUNT`, `H1_TITLE_MISMATCH`,
`TITLE_OCCURRENCE_COUNT`, and `DUPLICATE_H2`.

## Boundaries

This checker does not validate local or external links, interpret truth or
authority, rewrite documentation, approve review, or authorize release,
deployment, promotion, publication, source admission, or settings changes. It
does not establish a repository-wide Markdown style or require unique lower
level headings.

## Run

```bash
python tools/validators/docs/critical-structure/check_critical_structure.py \
  --repo-root . \
  --format text \
  CONTRIBUTING.md
```

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/critical-structure \
  --pattern 'test_*.py' \
  --verbose
```

The existing `validator-suite` workflow composes this distinct sentinel as a
separately attributable, fail-closed step. The stable workflow and job names
remain unchanged; a green run is bounded QA evidence only.

## Rollback

Before merge, close the draft PR and retain or delete the branch according to
the incident-control boundary. After an authorized merge, revert the repair,
validator, tests, workflow wiring, navigation update, and paired generated
receipt together through reviewed Git history. Reversion creates no authority
to restore known corrupted bytes.

[Back to top](#top)
