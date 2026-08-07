<!--
KFM_WIKI_SOURCE
page_id: Project-Status
title: Project Status
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Project-Status.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Project Status

> **Evidence checkpoint:** this page was authored from repository reads at `main@391e05b13600bda01b243bb97a0156002d73f0b7` on 2026-08-07. Re-check current `main`, open pull requests, workflow runs, and emitted artifacts before using any statement as current behavior.

KFM has a broad implementation and governance surface, but maturity is mixed. The safest status language is precise: a path may be present, a fixture may pass, a workflow may exist, and a public service may still be unimplemented or undeployed.

## Confirmed at the authoring checkpoint

| Surface | Confirmed repository state | What that does not prove |
|---|---|---|
| Repository | Public `bartytime4life/Kansas-Frontier-Matrix`, default branch `main` | Fitness, release, or deployment |
| Directory governance | [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the pinned [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md) bytes | That every existing path already conforms |
| Responsibility roots | Applications, packages, connectors, pipelines, schemas, policy, tests, data, release, docs, and other governed roots are present | Equal maturity across roots |
| Python surface | `pyproject.toml`, a Python 3.11+ scaffold, tests, and Make targets are present | A stable public Python API |
| Explorer Web | A Vite/TypeScript app, fixture-only Evidence Drawer projection behavior, and bounded UI tests are documented | A live map, live API integration, or production deployment |
| Governed API | Application structure and trust-membrane documentation are present | Every proposed route, middleware, policy integration, or deployed endpoint |
| Domain docs | The domain index records thirteen lanes and current lane documentation | End-to-end domain publication |
| Workflows | A substantial GitHub Actions tree and workflow governance README are present | Recent success, required-check enforcement, or release authority |
| Native GitHub Wiki | Repository metadata reports the wiki feature enabled | A populated `Home` page or synchronized source set |

## Native wiki status

At this checkpoint, the native wiki had no readable `Home` page and the special `.wiki.git` repository was not available through the connected GitHub tool. The reviewable source pages live in `docs/wiki/` and require a separate synchronization step after review. See [Wiki Maintenance](Wiki-Maintenance.md).

## Current bounded UI baseline

The [Explorer Web README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/explorer-web/README.md) describes an intentionally small fail-closed baseline:

- a static Vite entry point;
- fixed finite negative responses when no governed response is available;
- fixture-only Evidence Drawer projection validation;
- keyboard focus entry, Escape close, and focus restoration;
- synthetic positive and no-leak browser tests;
- no claim of live governed API, map, model, data-store, release, or deployment behavior.

This is valuable implementation evidence, but it is not the completed KFM user experience.

## Current bounded API posture

The [Governed API README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/governed-api/README.md) defines the intended trust membrane and finite outcomes. Candidate route families remain explicitly proposed unless verified by current route files, tests, policy integration, and runtime evidence.

## Status vocabulary

| Label | Use |
|---|---|
| `CONFIRMED` | Verified in the current investigation from repository evidence or an accepted decision |
| `PROPOSED` | Designed or requested, but not verified as current implementation |
| `UNKNOWN` | Evidence is insufficient |
| `NEEDS VERIFICATION` | A specific check can resolve the question |
| `CONFLICTED` | Relevant sources or authority surfaces disagree |
| `LINEAGE` | Historical or design context, not current authority by itself |

## High-value verification questions

- Which current workflows are required by repository rules and what are their exact-head conclusions?
- Which proposed ADRs have been accepted, rejected, superseded, or remain pending?
- Which source descriptors have current rights, terms, sensitivity, and activation decisions?
- Which `EvidenceRef` records resolve end to end to released `EvidenceBundle` support?
- Which domain lanes have proof-bearing processed, catalog, and published outputs?
- Which public services are deployed, where, and under what access policy?
- Which release, correction, withdrawal, and rollback drills have current evidence?
- When was the native wiki last synchronized to the reviewed source set?

## Where to verify

- [Main repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix)
- [Current pull requests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pulls)
- [GitHub Actions](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions)
- [ADRs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/adr)
- [Verification backlog](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/registers/VERIFICATION_BACKLOG.md)
- [Drift register](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/registers/DRIFT_REGISTER.md)
- [Generated work receipts](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/receipts/generated)
