<!--
KFM_WIKI_SOURCE
page_id: Home
title: Kansas Frontier Matrix Wiki
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Home.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
<p align="center">
  <img src="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/docs/brand/logo/The-Kansas-Frontier-Matrix-Seal-transparent-cropped.png" alt="Kansas Frontier Matrix seal" width="220" />
</p>

# Kansas Frontier Matrix

> A governed, evidence-first, map-first, time-aware spatial knowledge system for Kansas and the surrounding frontier.

Kansas Frontier Matrix (KFM) is designed to make spatial and historical knowledge useful **without hiding where it came from, what it means, what may be shown, or how it can be corrected**. It brings together domain data, maps, time, evidence, policy, review, and release controls around a common goal: the **inspectable claim**.

> [!IMPORTANT]
> This wiki is an orientation surface. Canonical repository evidence, adopted KFM doctrine and ADRs, contracts, schemas, policy, tests, lifecycle records, and release decisions outrank wiki prose. A wiki page is not implementation, approval, release, or data-publication evidence.

## Start here

| Reader goal | Wiki page | Canonical repository entry point |
|---|---|---|
| Understand KFM in ten minutes | [Architecture](Architecture.md) | [Repository README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md) |
| Set up a development environment | [Getting Started](Getting-Started.md) | [Contributing guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md) |
| See what is actually present now | [Project Status](Project-Status.md) | Current `main` tree and current checks |
| Learn where files belong | [Repository Map](Repository-Map.md) | [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md) |
| Understand evidence and trust | [Governance and Evidence](Governance-and-Evidence.md) | [Doctrine index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/README.md) |
| Browse Kansas knowledge lanes | [Domains](Domains.md) | [Domain index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/domains/README.md) |
| Understand maps and AI | [Map, UI, and AI](Map-UI-and-AI.md) | [Explorer Web](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/explorer-web/README.md) and [Governed API](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/governed-api/README.md) |
| Contribute safely | [Contributing](Contributing.md) | [CONTRIBUTING.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md) |
| Maintain this wiki | [Wiki Maintenance](Wiki-Maintenance.md) | [`docs/wiki/README.md`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/wiki/README.md) |

## KFM operating law

KFM connects source material to public-safe products through an explicit lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Promotion is a governed state transition, not a file move. Public clients use governed APIs and released public-safe artifacts rather than canonical or internal stores. Consequential claims resolve `EvidenceRef -> EvidenceBundle`; when support is missing or unsafe, the system abstains, denies, holds, or reports an error.

Maps, tiles, graph projections, indexes, dashboards, screenshots, stories, 3D scenes, and AI responses are **downstream carriers**. They do not become sovereign truth merely because they render successfully.

## What KFM brings together

- **Place:** a map-first operating surface centered on Kansas.
- **Time:** observations, source versions, valid periods, releases, corrections, and supersession.
- **Evidence:** resolvable source and support chains for consequential claims.
- **Domains:** hydrology, soil, ecology, geology, atmosphere, infrastructure, history, archaeology, agriculture, people, and more.
- **Governance:** source roles, rights, sensitivity, policy, review, promotion, correction, and rollback.
- **Delivery:** governed APIs, public-safe geospatial artifacts, Evidence Drawer views, and bounded Focus Mode interpretation.
- **Reversibility:** auditable changes, deterministic identity where practical, correction lineage, and rollback targets.

## Finite public outcomes

Trust-bearing runtime surfaces converge on four outward states:

| Outcome | Meaning |
|---|---|
| `ANSWER` | Released, policy-safe, evidence-supported response |
| `ABSTAIN` | Evidence is missing, stale, conflicting, or outside the supported scope |
| `DENY` | Rights, sensitivity, role, release state, or exposure risk blocks the response |
| `ERROR` | A validator, resolver, adapter, policy service, or runtime failed safely |

Negative states are first-class behavior. The system should never turn uncertainty into a confident answer merely to keep the interface moving.

## Project posture

KFM is a large, actively evolving repository with real documentation, application, schema, policy, test, pipeline, data-lifecycle, and release-supporting surfaces. Maturity is uneven and must be assessed claim by claim. File presence does not prove deployment, full validation, rights clearance, release readiness, or publication.

The source set for this wiki was authored against `main@391e05b13600bda01b243bb97a0156002d73f0b7`. Always inspect the current branch, files, tests, workflow runs, and emitted artifacts before relying on a current-behavior claim.

## Important links

- [Main repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix)
- [Repository README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md)
- [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md)
- [Accepted ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Security policy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/SECURITY.md)
- [Contribution guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md)
- [Documentation root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs)
- [Applications](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/apps)
- [Schemas](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/schemas)
- [Policy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/policy)
- [Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/tests)
