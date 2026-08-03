<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ingest-readme
title: tests/ingest README
type: README
version: v0.1
status: draft; bounded executable coverage
owners: OWNER_TBD - tooling QA; source stewards
created: 2026-08-02
updated: 2026-08-02
policy_label: repository-facing; synthetic-fixtures; no-network; no-publication
owning_root: tests/
responsibility: Test ingest-adjacent watcher and preflight helpers without performing source access, lifecycle mutation, promotion, release, or publication.
related:
  - ../../tools/ingest/README.md
  - ./cdl_watch/README.md
notes:
  - "The first executable child is the frozen synthetic CDL material-change watcher profile."
  - "Passing tests prove only local helper behavior; they do not admit a source or create evidence, receipt, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Ingest-adjacent helper tests

This lane proves deterministic watcher and preflight helpers under synthetic,
bounded, no-network inputs. It does not test a live source, connector, pipeline,
catalog, proof, release, or public surface.

## Current executable coverage

| Child | Status | Boundary |
|---|---|---|
| [`cdl_watch/`](cdl_watch/README.md) | **CONFIRMED bounded executable** | Synthetic sidecar comparison and review-only outcomes; no USDA access or lifecycle writes. |

Every admitted fixture must be obviously synthetic, contain no credential or
private record, declare its expected outcome, and remain unable to trigger
network or governed lifecycle mutations.

[Back to top](#top)
