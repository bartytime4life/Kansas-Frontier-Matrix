<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-document-graph-readme
title: Documentation Graph Validator
type: README
version: v0.1
status: draft; bounded-executable; local-only; no-network; non-authoritative
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; docs-validator; graph-qa; non-authoritative
owning_root: tools/
responsibility: deterministic documentation graph, backlink, reachability, generated-MOC, workbench, and optional machine document-registry QA without deciding doctrine, evidence sufficiency, source admissibility, policy, review, release, publication, or Directory Rules exceptions
truth_posture: CONFIRMED bounded executable and synthetic fixture tests / NEEDS VERIFICATION hosted exact-head results and whole-repository historical classification
related:
  - ../README.md
  - ../link-check/README.md
  - ../meta-block/README.md
  - ../../../../docs/README.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../control_plane/document_registry.yaml
  - ../../../../docs/intake/exploratory/kaas-document-graph-source-map.md
  - ../../../../tests/validators/docs/document-graph/README.md
notes:
  - "The graph is a rebuildable QA projection, never a documentation, evidence, policy, release, or publication authority."
  - "The parser consumes only bounded top-level identity and relationship metadata; the meta-block lane remains responsible for full metadata conformance."
  - "The existing link-check lane remains responsible for exact local target, fragment, case, and path validation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/docs/document-graph/` — Documentation Graph QA

> **Purpose.** Build a deterministic, no-network projection of repository
> Markdown nodes, local navigation, bounded metadata relationships, backlinks,
> entrypoint reachability, generated Maps of Content, and optional machine
> document-registry parity.

## Status and authority boundary

| Surface | State | Limit |
|---|---|---|
| `check_document_graph.py` | **CONFIRMED bounded executable** | Standard library only; explicit Markdown scope; no network. |
| Synthetic tests | **CONFIRMED** | Public-safe fixture repository with positive and negative cases. |
| Pull-request workflow | **CONFIRMED definition / NEEDS VERIFICATION execution** | Changed-file ratchet; hosted exact-head result remains separate evidence. |
| Generated graph/workbench | **Non-authoritative QA projection** | It may guide review; it cannot create or change doctrine, registry authority, release, or publication state. |
| Whole-repository health | **NEEDS VERIFICATION** | Historical findings require classification before a stricter baseline is adopted. |

The accepted Directory Rules place reusable repository validators under
`tools/`, proof under `tests/`, orchestration under `.github/`, and generated QA
summaries under a non-authoritative output lane. This implementation extends the
existing documentation-validator family without creating a root or parallel
contract, schema, policy, source, registry, receipt, proof, release, or
publication authority.

## What the validator reads

- explicit UTF-8 `.md` and `.markdown` files or directories;
- local inline and bounded reference-style Markdown links;
- top-level `KFM_META_BLOCK_V2` or `KFM_DOCUMENT_CONTROL` fields needed for
  identity and relationships;
- configured entrypoints; and
- optionally, `doc_id` and `path` fields from the existing machine document
  registry.

The metadata parser is intentionally narrow. It consumes `doc_id` or
`document_id`, title, type, status, owner/owners, policy label, `related`,
`supersedes`, and `superseded_by`. It does not claim full YAML or meta-block
validation.

## Outputs

The tool emits stable text, compact JSON, or a Markdown **Documentation Graph
Workbench**. The projection includes:

- deterministic nodes and typed edges;
- stable document identities when declared;
- inbound/outbound counts and backlink lists;
- reachability from explicit entrypoints;
- orphan and unreachable-document findings;
- duplicate identity and missing declared-relation failures;
- optional registry path/identity parity;
- generated Maps of Content grouped by documentation lane; and
- a SHA-256 graph digest over canonical graph material.

## Finite outcomes

| Outcome | Exit | Meaning |
|---|---:|---|
| `DOC_GRAPH_PASS` | `0` | No configured finding was emitted. |
| `DOC_GRAPH_WARN` | `0` | Reviewable QA findings exist, but no fail finding is current. |
| `DOC_GRAPH_FAIL` | `1` | At least one current fail-closed graph or registry finding exists. |
| `ERROR` | `2` | The bounded operation could not complete safely. |

Important finding families include `DUPLICATE_DOC_ID`,
`RELATED_TARGET_MISSING`, `RELATED_DOC_ID_MISSING`, `PATH_ESCAPE`,
`REGISTRY_TARGET_MISSING`, `REGISTRY_DOC_ID_MISMATCH`, `DOC_ORPHANED`,
`DOC_UNREACHABLE`, and `DOC_ID_MISSING`.

## Changed-file ratchet

`--git-diff <base-sha>...HEAD` makes historical debt visible without letting a
new or changed document introduce the same failure silently:

- findings touching a changed path retain their configured severity;
- unchanged fail findings are reported as historical warnings;
- unchanged orphan, unreachable, and missing-ID warnings are omitted from the
  pull-request gate; and
- `--warnings-as-errors` promotes only current warnings.

The ratchet does not declare historical findings acceptable. It keeps the first
implementation reviewable while a steward-owned baseline is classified.

## Run

Fixture profile:

```bash
python tools/validators/docs/document-graph/check_document_graph.py \
  --repo-root tests/validators/docs/document-graph/fixtures/valid_repo \
  --entrypoint README.md \
  --registry control_plane/document_registry.yaml \
  --format markdown \
  README.md docs
```

Repository changed-file profile:

```bash
python tools/validators/docs/document-graph/check_document_graph.py \
  --repo-root . \
  --entrypoint README.md \
  --entrypoint docs/README.md \
  --registry control_plane/document_registry.yaml \
  --git-diff <BASE_SHA>...HEAD \
  --format markdown \
  README.md docs tools/validators/docs
```

Tests:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/document-graph \
  --pattern 'test_*.py' \
  --verbose
```

## Explicit limits

- The graph covers only the supplied Markdown scope and configured entrypoints.
- The existing link checker remains the target/anchor/case/path authority for
  Markdown QA; this graph does not duplicate that implementation.
- External URLs are counted as unverified and never requested.
- Cycles are ordinary graph structure and are not failures by themselves.
- A graph edge, backlink, centrality signal, MOC, or workbench entry is not
  evidence and does not upgrade a document's authority.
- The optional registry comparison does not add entries or make the registry
  complete.
- The tool never edits documentation, registries, doctrine, or publication
  state.

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert the implementation commit. No source, lifecycle data,
release, deployment, cache, or public artifact requires migration or withdrawal.

[Back to top](#top)
