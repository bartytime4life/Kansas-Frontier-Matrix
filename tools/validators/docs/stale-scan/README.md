<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-stale-scan-readme
title: Documentation Freshness and Review-Posture Validator
type: README
version: v0.2
status: draft; bounded-executable; local-only; no-network; non-authoritative
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-08-07
policy_label: repository-facing; docs-validator; stale-scan; freshness-qa; non-authoritative
owning_root: tools/
responsibility: deterministic documentation freshness, review-age, placeholder-owner, temporal-marker, verification-debt, and implementation-claim review signals without deciding truth, doctrine, source admissibility, policy, review, release, publication, or Directory Rules exceptions
truth_posture: CONFIRMED bounded executable and synthetic tests / PROPOSED freshness thresholds pending steward adoption / NEEDS VERIFICATION hosted exact-head results, whole-repository classification, and required-check coupling
related:
  - ../README.md
  - ../link-check/README.md
  - ../document-graph/README.md
  - ../meta-block/README.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../tests/validators/docs/stale-scan/README.md
notes:
  - "Freshness is a review signal, not proof that content is true, false, current, authoritative, reviewed, or public-safe."
  - "The workflow uses the advisory profile and an explicit UTC as-of date; warnings are not promoted to failures by default."
  - "Full metadata conformance remains delegated to meta-block, and exact link resolution remains delegated to link-check."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/docs/stale-scan/` — Documentation Freshness QA

> **Purpose.** Produce a deterministic, no-network review workbench for
> explicitly scoped Markdown by comparing bounded metadata dates and review
> signals with an explicit as-of date. The scanner routes findings to steward
> review; it never edits documentation or asserts the correct truth state.

## Status and authority boundary

| Surface | State | Limit |
|---|---|---|
| `check_stale_docs.py` | **CONFIRMED bounded executable** | Standard-library only; explicit scope and explicit as-of date. |
| Synthetic tests | **CONFIRMED** | Positive, negative, replay, ratchet, CLI, path-boundary, and no-mutation coverage. |
| Pull-request workflow | **CONFIRMED definition / NEEDS VERIFICATION execution** | Advisory changed-file ratchet; hosted exact-head result is separate evidence. |
| Freshness thresholds | **PROPOSED executable defaults** | `365` review days and `90` placeholder-grace days are review signals, not adopted doctrine. |
| Whole-repository health | **NEEDS VERIFICATION** | Historical findings require classification before stricter enforcement. |

Accepted ADR-0029 makes Directory Rules v2 the effective placement authority.
Reusable validation stays under `tools/`, executable evidence under `tests/`,
read-only orchestration under `.github/`, exploratory adaptation notes under
`docs/intake/exploratory/`, and AI authoring accountability under
`data/receipts/generated/`. This lane creates no parallel documentation,
contract, schema, policy, registry, receipt, proof, release, or publication
home.

## Why the as-of date is explicit

Freshness is time-dependent. The executable therefore requires `--as-of
YYYY-MM-DD` or `KFM_DOCS_AS_OF`; it does not hide the current clock inside a
report. Tests and replay use a fixed date. CI supplies the current UTC date as a
visible input. The as-of date, thresholds, documents, findings, and limitations
all participate in the report digest.

## Profiles

| Profile | Missing metadata/review date | Intended use |
|---|---|---|
| `advisory` | Missing review date is a warning; a document without a meta block is counted but not failed. | Initial repository changed-file ratchet. |
| `bounded-required` | Missing meta block delegates as a failure; missing review date fails. | A specifically adopted documentation lane after steward review. |

The initial workflow uses `advisory` and does **not** pass
`--warnings-as-errors`. This avoids turning an unclassified historical corpus
into an accidental repository-wide freshness policy.

## Signals

The bounded profile can emit:

| Code | Default severity | Meaning |
|---|---:|---|
| `REVIEW_DATE_MISSING` | warning, or failure in `bounded-required` | No `last_reviewed`, `reviewed`, or `updated` date is available. |
| `REVIEW_DATE_INVALID` | failure | Review date is not a real ISO calendar date. |
| `CREATED_DATE_INVALID` | failure | Created date is not a real ISO calendar date. |
| `DATE_ORDER_INVALID` | failure | `created` is later than the review date. |
| `FUTURE_REVIEW_DATE` | failure | Review date is after the explicit as-of date. |
| `REVIE]}WINDOW_EXPIRED` | warning | Review age exceeds the configured window. |
| `OWNER_PLACEHOLDER_STALE` | warning | A TODO/TBD/placeholder owner outlives the configured grace window. |
| `TEMPORARY_MARKER_EXPIRED` | warning | `review_due`, `expires`, `expiry`, `temporary_until`, or `sunset_date` has passed. |
| `TEMPORARY_MARKER_DATE_INVALID` | failure | A temporal marker is not a real ISO date. |
| `IMPLEMENTATION_CLAIM_REVIEW_DUE` | warning | Implementation/current-state language appears in a document whose review window expired. This requests verification; it does not infer actual behavior. |
| `VERIFICATION_DEBT_REVIEW_DUE` | warning | `UNKNOWN` or `NEEDS VERIFICATION` posture remains beyond the review window. |
| `DELEGATE_TO_META_BLOCK` | warning/failure by profile | Full metadata structure belongs to the meta-block validator. |
| `SCAN_ERROR` | operational error | The bounded operation could not complete safely. |

The scanner does not attempt to prove `STATUS_OVERCLAIM`, because that requires
implementation or evidence beyond dates and metadata. It emits a narrower
review-due signal instead.

## Changed-file ratchet

`--git-diff <base>...HEAD` separates current regressions from inherited debt:

- findings touching changed Markdown retain configured severity;
- unchanged failures are downgraded to visible historical warnings;
- unchanged warnings and informational findings are omitted from the pull-request gate;
- `--warnings-as-errors` promotes current warnings only; and
- document rows still record whether each path is current.

Historical downgrade is visibility, not acceptance. A whole-repository baseline
and steward disposition remain separate work.

## Finite outcomes

| Outcome | Exit | Meaning |
|---|---:|---|
| `DOC_STALE_SCAN_PASS` | `0` | No configured finding was emitted. |
| `DOC_STALE_SCAN_WARN` | `0` | Reviewable freshness findings exist. |
| `DOC_STALE_SCAN_FAIL` | `1` | A current fail-closed date/profile finding exists. |
| `ERROR` | `2` | The bounded operation could not complete safely. |

## Run

Fixture replay:

```bash
python tools/validators/docs/stale-scan/check_stale_docs.py \
  --repo-root tests/validators/docs/stale-scan/fixtures/valid_repo \
  --as-of 2026-08-07 \
  --format markdown \
  README.md docs
```

Repository changed-file profile:

```bash
python tools/validators/docs/stale-scan/check_stale_docs.py \
  --repo-root . \
  --as-of "$(date -u +%F)" \
  --profile advisory \
  --review-window-days 365 \
  --placeholder-grace-days 90 \
  --git-diff <BASE_SHA>...HEAD \
  --format markdown \
  README.md docs tools/validators/docs
```

Type-specific windows are explicit and repeatable:

```bash
--type-window adr=180 --type-window runbook=90
```

Tests:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/stale-scan \
  --pattern 'test_*.py' \
  --verbose
```

## Explicit limits

- A recent date does not establish material currentness or human review.
- An old date does not establish that content is false.
- Owner placeholders are reported; the tool never invents an owner.
- Implementation-claim review signals do not inspect runtime behavior.
- Full metadata validity belongs to `meta-block/`.
- Exact link and anchor resolution belongs to `link-check/`.
- Graph connectivity and reachability belong to `document-graph/`.
- The tool never edits Markdown, registries, doctrine, policy, review records,
  release state, or publication state.

## Rollback

Before merge, close the draft pull request and remove its feature branch. After
an authorized merge, revert the implementation commit or merge commit. No
source, lifecycle data, release, deployment, cache, or public artifact requires
migration or withdrawal.

[Back to top](#top)
