<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/kaas-document-graph-source-map
title: KaaS Documentation Graph Source Adaptation
type: source-map
version: v0.1
status: exploratory; implementation-source-map
owner: TODO-docs-steward-plus-tooling-qa-owner
created: 2026-08-06
updated: 2026-08-06
policy_label: public; repository-facing; non-authoritative
owning_root: docs/
responsibility: record the bounded adaptation of jimbrig/KaaS knowledge-navigation patterns into KFM documentation graph QA without copying KaaS content, repository structure, workflows, or publication authority
truth_posture: CONFIRMED inspected source patterns and current KFM repository lanes / PROPOSED KFM adaptation / NEEDS VERIFICATION hosted exact-head validation
related:
  - docs/doctrine/directory-rules.md
  - tools/validators/docs/document-graph/README.md
  - tests/validators/docs/document-graph/README.md
  - control_plane/document_registry.yaml
notes:
  - "Source repository inspected at jimbrig/KaaS main commit 028fcf40521403c1b8a9fa6b28c3b9b2cd8cebbc."
  - "No KaaS knowledge content, Obsidian configuration, workflow code, or repository root structure is copied by this adaptation."
[/KFM_META_BLOCK_V2] -->

# KaaS documentation-graph source adaptation

## Status

- **Source repository:** `jimbrig/KaaS`
- **Inspected source revision:** `028fcf40521403c1b8a9fa6b28c3b9b2cd8cebbc`
- **KFM assay base:** `main@89fef7fec1d744df5269d19380a7f7a2a91b5c57`
- **Selected increment:** deterministic documentation graph, backlinks, generated Maps of Content, steward workbench, and documentation-health findings
- **Implementation state:** `PROPOSED` until reviewed and merged
- **Network, source activation, lifecycle promotion, release, deployment, and publication effects:** none

## Source patterns retained

The KaaS repository presents a personal knowledge base as interlinked Markdown
rather than isolated files. Its useful transferable patterns are:

- atomic notes connected through Maps of Content;
- backlinks as a discovery and maintenance surface;
- explicit reports for unlinked, unresolved, and metadata-poor files;
- a workbench that gathers current work and review candidates;
- repeatable note templates and stable source-native identifiers; and
- separation between an authoring representation and downstream public renderings.

These patterns are design evidence only. KaaS's PARA/Zettelkasten root tree,
Obsidian plugin state, force-push conversion workflow, mutable action references,
and direct site deployment are not admitted into KFM.

## Repository adaptation

| KaaS pattern | KFM adaptation in this slice |
|---|---|
| Maps of Content | Generate a deterministic, non-authoritative MOC section by KFM documentation lane. |
| Backlinks | Emit a stable inbound-link index from Markdown and bounded metadata relationships. |
| Unlinked/unresolved reports | Report orphaned, unreachable, duplicate-ID, missing-declared-relation, and registry-parity findings. |
| Workbench | Emit one Markdown Documentation Graph Workbench into the GitHub Actions step summary. |
| Note metadata | Consume only stable identity and relationship fields; full conformance stays with the separate meta-block validator lane. |
| Authoring/public projection split | Keep graph output as QA-only and prohibit direct publication or authority effects. |

The validator intentionally delegates exact local target, fragment, case, and
path validation to the existing link-check lane rather than building a competing
checker.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 the effective placement authority.
This increment uses existing responsibility roots:

| Responsibility | Placement |
|---|---|
| deterministic documentation QA | `tools/validators/docs/document-graph/` |
| executable conformance evidence | `tests/validators/docs/document-graph/` |
| pull-request orchestration | `.github/workflows/docs-document-graph.yml` |
| source adaptation and limitations | this file under `docs/intake/exploratory/` |
| authoring accountability | `data/receipts/generated/` |
| existing optional machine input | `control_plane/document_registry.yaml` |

No new root or parallel documentation, contract, schema, policy, source,
registry, receipt, proof, release, or publication authority is created.

## Finite implementation boundary

The slice may:

- read explicit repository Markdown and the current machine registry;
- construct deterministic graph nodes and typed edges;
- identify entrypoint reachability and backlinks;
- emit reviewable QA findings and a graph digest;
- ratchet historical debt so changed-path regressions remain blocking; and
- provide synthetic no-network tests.

The slice may not:

- edit Markdown or registry entries;
- decide that a document is true, adopted, canonical, rights-cleared, reviewed,
  released, public-safe, or published;
- use graph centrality or link frequency as evidence authority;
- fetch external URLs;
- install or depend on Obsidian; or
- publish a documentation site.

## Deferred candidates

The remaining KaaS-derived ideas require separate dependency and authority
checks:

1. executable `KFM_META_BLOCK_V2` and document-registry closure;
2. accepted freshness thresholds and stale-document validation;
3. governed document template generators;
4. a pinned documentation preview build and immutable build manifest;
5. a candidate-to-adopted idea lifecycle; and
6. source-native identifier intake with receipts and duplicate resolution.

## Rollback

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the bounded implementation commit. No external source,
lifecycle data, deployment, release, cache, or public artifact requires
withdrawal or correction.
