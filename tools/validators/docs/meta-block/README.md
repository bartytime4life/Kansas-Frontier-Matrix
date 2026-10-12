<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-meta-block-readme
title: Documentation Metadata-Block Validator
type: README
version: v0.2
status: draft; bounded-executable; local-only; no-network; non-authoritative
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-08-06
policy_label: repository-facing; docs-validator; meta-block; registry-delta; non-authoritative
owning_root: tools/
responsibility: deterministic KFM_META_BLOCK_V2 structural validation and review-only machine document-registry delta generation without deciding doctrine, evidence sufficiency, source admissibility, policy, review, release, publication, or Directory Rules exceptions
truth_posture: CONFIRMED bounded executable and synthetic tests / PROPOSED metadata profile pending steward adoption / NEEDS VERIFICATION hosted exact-head results and whole-repository historical classification
related:
  - ../README.md
  - ../link-check/README.md
  - ../document-graph/README.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../control_plane/document_registry.yaml
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../tests/validators/docs/meta-block/README.md
notes:
  - "The validator checks a bounded top-level metadata subset and does not claim general YAML conformance."
  - "The registry delta is a deterministic review candidate only; the executable never writes or authorizes the machine register."
  - "Exact local target, fragment, case, and path validation remains delegated to link-check."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/docs/meta-block/` — Documentation Metadata QA

> **Purpose.** Validate the structural integrity of `KFM_META_BLOCK_V2`
> envelopes in explicitly scoped Markdown and optionally compare valid document
> identities with `control_plane/document_registry.yaml` without mutating either
> surface.

## Status and authority boundary

| Surface | State | Limit |
|---|---|---|
| `check_meta_blocks.py` | **CONFIRMED bounded executable** | Standard-library only; explicit Markdown scope; no network. |
| Synthetic tests | **CONFIRMED** | Positive, negative, replay, ratchet, CLI, and no-mutation coverage. |
| Pull-request workflow | **CONFIRMED definition / NEEDS VERIFICATION execution** | Read-only changed-file ratchet; hosted result remains separate evidence. |
| Metadata field profile | **PROPOSED executable profile** | It is structural QA, not adopted metadata doctrine. |
| Registry delta | **Review-only QA projection** | It cannot create, update, authorize, or approve a register entry. |
| Whole-repository health | **NEEDS VERIFICATION** | Existing historical findings require classification before stricter enforcement. |

Accepted ADR-0029 makes Directory Rules v2 the placement authority. Reusable
repository validation belongs under `tools/`; executable evidence belongs under
`tests/`; orchestration belongs under `.github/`; generated authoring
accountability belongs under `data/receipts/generated/`. This lane does not
create a parallel documentation, schema, policy, registry, receipt, proof,
release, or publication authority.

## What the validator reads

- explicitly supplied UTF-8 `.md` and `.markdown` files or directories;
- one bounded top-level `KFM_META_BLOCK_V2` envelope per document;
- optional changed-file scope from `<base-sha>...HEAD`; and
- optional `doc_id` and `path` entries from the existing machine document
  registry.

The parser intentionally supports only top-level scalar fields and simple
sequences. Nested mappings are reported as outside the bounded profile. No
metadata value is executed.

## Profiles

| Profile | Missing block | Existing block |
|---|---|---|
| `present` | Counted but not failed | Validated fully when present. This is the initial repository ratchet. |
| `required` | `META_BLOCK_MISSING` failure | Validated fully. Intended for bounded lanes after steward adoption. |

The first workflow uses `present` so the new validator does not convert
historical metadata coverage debt into an unreviewed repository-wide gate.

## Structural checks

The first executable profile validates:

- complete, non-duplicated metadata delimiters;
- unique top-level field names;
- required fields: `doc_id`, `title`, `type`, `version`, `status`, `created`,
  `updated`, `policy_label`, `owning_root`, `responsibility`, and
  `truth_posture`;
- exactly one of `owner` or `owners`, with at least one non-empty owner value;
- bounded `kfm://` identity syntax;
- ISO calendar dates and non-reversing `created`/`updated` order;
- top-level responsibility-root agreement between `owning_root` and path;
- bounded type and field lengths;
- recognized evidence-posture markers;
- basic `related` entry hygiene and path-escape denial;
- duplicate `doc_id` values across the scan scope; and
- optional registry identity/path parity.

It deliberately does **not** decide whether a document's status is justified by
evidence. Evidence-based overclaim analysis remains a separate future profile.

## Review-only document-registry delta

When `--registry` is supplied, valid metadata identities are compared with the
machine register:

| Result | Delta action | Effect |
|---|---|---|
| Exact `doc_id` and path match | none | Registry state is reported as `registered`. |
| Valid document absent from registry | `ADD_REVIEW` | Emits proposed `kind`, `status`, and `policy_label`; leaves `authority` unresolved. |
| Same `doc_id`, different path | `HOLD_CONFLICT` | Fails current changes; requires migration or correction authority. |
| Same path, different `doc_id` | `HOLD_CONFLICT` | Fails current changes; requires identity correction authority. |

The delta includes `review_only: true` and `mutates_registry: false`. It is never
applied automatically.

## Changed-file ratchet

`--git-diff <base-sha>...HEAD` keeps current changes strict without silently
ratifying inherited debt:

- findings touching a changed document retain their configured severity;
- unchanged failures become historical warnings;
- unchanged warnings and informational findings are omitted from the PR gate;
- registry additions are emitted only for the current review scope; and
- `--warnings-as-errors` promotes only current warnings.

Historical downgrade is visibility, not acceptance. A separately reviewed
baseline is still required before whole-repository enforcement.

## Finite outcomes

| Outcome | Exit | Meaning |
|---|---:|---|
| `DOC_META_BLOCK_PASS` | `0` | No configured finding was emitted. |
| `DOC_META_BLOCK_WARN` | `0` | Reviewable current or historical findings exist. |
| `DOC_META_BLOCK_FAIL` | `1` | A current fail-closed metadata or registry finding exists. |
| `ERROR` | `2` | The bounded operation could not complete safely. |

Stable finding families include `META_BLOCK_MISSING`,
`META_BLOCK_MALFORMED`, `META_BLOCK_DUPLICATE`,
`META_BLOCK_DUPLICATE_KEY`, `REQUIRED_FIELD_MISSING`, `DOC_ID_INVALID`,
`OWNING_ROOT_PATH_MISMATCH`, `DATE_INVALID`, `DATE_ORDER_INVALID`,
`RELATED_PATH_ESCAPE`, `DUPLICATE_DOC_ID`, `REGISTRY_ENTRY_MISSING`,
`REGISTRY_DOC_ID_PATH_CONFLICT`, and `REGISTRY_PATH_DOC_ID_CONFLICT`.

## Run

Fixture profile:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root tests/validators/docs/meta-block/fixtures/valid_repo \
  --registry control_plane/document_registry.yaml \
  --format markdown \
  README.md docs
```

Repository changed-file profile:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --registry control_plane/document_registry.yaml \
  --git-diff <BASE_SHA>...HEAD \
  --format markdown \
  --output /tmp/docs-meta-block.md \
  --registry-delta-output /tmp/document-registry-delta.json \
  README.md docs tools/validators/docs
```

Tests:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/meta-block \
  --pattern 'test_*.py' \
  --verbose
```

## Explicit limits

- Structural conformance does not establish truth, authority, rights,
  sensitivity, source admissibility, policy, review, release, or publication.
- The parser is not a general YAML implementation.
- Exact local link/anchor/case resolution remains owned by link-check.
- The document graph remains the connectivity, backlink, and reachability
  projection.
- The machine registry remains separately governed; this tool cannot update it.
- The tool never edits Markdown or repository control surfaces.

## Rollback

Before merge, close the draft pull request and remove its feature branch. After
an authorized merge, revert the implementation commit. No source, lifecycle
data, release, deployment, cache, or public artifact requires migration or
withdrawal.

[Back to top](#top)
