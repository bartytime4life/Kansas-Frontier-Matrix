<!-- kfm-showcase:start -->
<p align="center">
  <a href="README.md#see-it-in-action"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/brand/readme/kfm-banner-changelog-dark.svg" /><img src="docs/brand/readme/kfm-banner-changelog.svg" alt="Changelog banner: what changed, and where to prove it." width="100%" /></picture></a>
</p>
<!-- kfm-showcase:end -->

# Changelog

<!-- kfm-showcase:start -->
<p>
  <a href="#changelog"><img src="https://img.shields.io/badge/history-changelog-4a6fa5?style=flat-square" alt="history page" /></a>
  <a href="#changelog"><img src="https://img.shields.io/badge/read-~3%20min-6b6b6b?style=flat-square" alt="About 3 minutes to read" /></a>
  <a href="README.md"><img src="https://img.shields.io/badge/%E2%86%A9-project%20home-0b1f3a?style=flat-square" alt="Back to the project home" /></a>
  <a href="README.md#take-the-tour"><img src="https://img.shields.io/badge/tour-10%20workspaces-2f6f4e?style=flat-square" alt="Take the Explorer tour" /></a>
</p>
<!-- kfm-showcase:end -->

KFM records notable repository changes in this file. It is a human-readable repository history, not a release manifest, promotion decision, proof pack, correction notice, rollback card, or publication record.

> [!IMPORTANT]
> A changelog entry, commit, pull request, merge, tag, GitHub release, badge, or passing workflow does not by itself establish a governed KFM release or publish KFM knowledge. Governed release, correction, withdrawal, and rollback decisions belong under [`release/`](release/); released public-safe carriers belong under [`data/published/`](data/published/).

## Record boundaries

| Record | Responsibility |
|---|---|
| `CHANGELOG.md` | Concise, reviewable summary of notable repository changes. |
| Git commits and pull requests | Exact byte-level and review history for repository work. |
| [`release/`](release/) | Append-only release, promotion, correction, withdrawal, and rollback decisions. |
| [`data/published/`](data/published/) | Released public-safe carriers after the applicable evidence, policy, validation, review, correction, and rollback gates. |

## Entry contract

- Add material work under [`Unreleased`](#unreleased) using `Added`, `Changed`, `Fixed`, `Deprecated`, `Removed`, or `Security` headings as applicable.
- Link the pull request or immutable commit supporting each entry. Name the affected surface and keep implementation, validation, release, deployment, and publication claims separate.
- Create a dated, versioned section only when a governed release record identifies the release, scope, review state, correction path, and rollback target. A merge or tag alone is insufficient.
- Keep `Security` entries public-safe. Do not include credentials, exploit-enabling detail, restricted payloads, living-person or genomic data, private review notes, or harmful-precision locations; follow [`SECURITY.md`](SECURITY.md) for private-first reporting.
- Correct material mistakes with a visible follow-up entry. Do not silently rewrite historical claims or remove lineage without evidence and review.

## Coverage notice

The previous changelog recorded only the initial implementation milestones through 2026-05-09. This modernization preserves those seed entries but does not invent a retrospective backfill for later repository activity. Use the repository's [commit history](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commits/main) and [merged pull requests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pulls?q=is%3Apr+is%3Amerged) to reconstruct repository changes, and use [`release/`](release/) for governed release state.

## Unreleased

### Added

- Illustrated, visitor-first project home with animated, theme-aware SVG artwork under [`docs/brand/readme/`](docs/brand/readme/README.md): Explorer walkthrough, feature tour, time depth, source lanes, Focus Mode gate trace, capability board, trust membrane and trust path ([#4942](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4942), [#4945](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4945)).
- Social preview card, artwork gallery and encyclopedia cover visuals ([#4946](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4946)).
- Page banners, badge rows, topic graphics and footer navigation for documents linked from the project home: doctrine, security, installation, local-data runbook and tools, acquisition runbook, verification backlog, brand, changelog, code of conduct and three encyclopedia chapters. Artwork is illustrative; each page's text remains authoritative, and no release or publication is implied.
- Raw-data intake pipeline for the private local store: content profiling of RAW and QUARANTINE files, placement recommendations across local store, intake database, WORK review lane, Git metadata cards and GitHub release candidates, a GitHub storage guard keeping 20 GB of the 100 GB limit for code and interface work, the loopback Intake Desk on `127.0.0.1:8771`, and a read-only Explorer summary in `apps/site/source` (repository source; not yet deployed). Recommendations only; no admission, upload, release or publication ([#4984](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4984), [runbook](docs/runbooks/raw-data-intake.md)).
- Local Qwen companion evaluation in `apps/site/source` (repository source; not yet deployed): `npm run eval:qwen-local` runs a fixed set of questions through the running loopback bridge against the real model and checks each reply against the governance rules and the expected outcome, including whether the installed knowledge pack is current. It prints IDs and outcomes, not question or answer text, and is a local diagnostic rather than evidence or release.

### Changed

- Local Qwen knowledge pack cross-domain ideas in `apps/site/source` (repository source; not yet deployed): 32 ideas across 30 of the 45 domain pairings (up from 9), every domain in at least three, and the three offered per question now favour pairs that touch the question's domains.
- Local Qwen knowledge pack glossary in `apps/site/source` (repository source; not yet deployed): definitions for source kinds, connection states and the map-context fields the model reads (for example selected versus displayed, and retrieval versus observation time), five more governance terms, and 55 technical terms across all ten domains (discharge versus gage height, NWS warning versus watch, PLSS township and range, wind direction convention and more), sent only for relevant domains.
- Local Qwen knowledge pack in `apps/site/source` (repository source; not yet deployed): six exploration ideas for every source domain (60 in all, up from 26), nine cross-domain ideas offered only when both of their domains are in view, and more project ideas. Ideas stay framed as questions rather than findings, and a test checks they carry no EvidenceRefs or precise locations.
- Local Qwen companion contract v2 in `apps/site/source` (repository source; not yet deployed): the loopback bridge now reaches Ollama for view-level questions and returns a structured interpretation (observations, cautious readings, evidence gaps, follow-up questions) under `ABSTAIN`, never as evidence or an `ANSWER`. The model is grounded in a generated KFM knowledge pack of source metadata (cadence, freshness, what each source is not) plus a curated glossary and exploration ideas. Ollama's tested release is now a floor instead of an exact pin, the context window is explicit, safety and precision-seeking questions skip the model, and every reply carries a redacted receipt. See the [Site README](apps/site/source/README.md#interpretation-and-the-kfm-knowledge-pack-contract-v2).
- Explorer site audit in `apps/site/source` (repository source; not yet deployed): additive D1 indexes and a row-value cursor for the data-submission lists, a branded 404 page, baseline response headers, and fixes for the serious accessibility findings: link contrast, ARIA roles, keyboard access to the Qwen conversation, a `<dl>` structure and a missing `main` landmark. See [audit notes](apps/site/source/docs/explorer-site-audit-2026-10-09.md).
- Explorer interface refresh in `apps/site/source` (repository source; not yet deployed to the Site): navy theme, first-visit quick start, offline Kansas orientation on the local basemaps, a single zoom control set, and removal of a fixed place label and two mobile layout overlaps. See [refresh notes](apps/site/source/docs/explorer-interface-refresh.md).
- Modernized the root changelog into an evidence-bounded repository-history contract with entry categories, source-link expectations, security guidance, a historical coverage notice, and an explicit release/publication boundary.

### Fixed

- Local Qwen companion in `apps/site/source` (repository source; not yet deployed): street addresses, ZIP codes, lat/lon, UTM and PLSS references, "precisely" and "pinpoint" wording, questions about where burials, mounds, archaeological sites, nests, leks, dens or roosts are, "safe to drink" or "can I drink", and more personal places ("my basement", "my neighborhood", "where I'm staying") now abstain before the model as `SENSITIVE_QUESTION_NOT_INTERPRETED`. A probe found 21 of 26 such questions reached the model before; ordinary view questions, including `PUBLIC_SAFE`, highway numbers and county-level questions, are still interpreted.
- Local Qwen knowledge pack cross-domain ideas in `apps/site/source` (repository source; not yet deployed): when three or more domains are on the map, the three ideas offered now go to the pairs the question matches most closely, so a question about flood zones and the alluvial aquifer gets that pair's idea rather than two about the river beside it.
- Local Qwen knowledge pack matching in `apps/site/source` (repository source; not yet deployed): question words now match source metadata and cross-domain idea text across simple plurals ("county" finds "counties"), and each idea's own words count toward its rank, so "How many gauges are active in each county?" gets the gauges-per-county idea. Plural forms of ignored words stay ignored ("What maps are visible?" no longer pulls in unrelated sources).
- Local Qwen companion in `apps/site/source` (repository source; not yet deployed): questions that ask for exact or personal locations in everyday words ("where exactly", "wells near me", "nearest well to my house", "is my property in a flood zone?") now abstain before the model, matching the documented exact-location rule; previously only literal phrases such as "exact location" or "GPS" did.

## Legacy seed milestones — 2026-05-08 to 2026-05-09

These entries preserve the scope and wording of the original changelog as repository lineage. They describe implementation work recorded at the time; they do not establish that the described state remains current or that a governed release or publication occurred.

### Added

- 2026-05-08 — [`66c9ee3`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/66c9ee3b490dec2b2f834d07b316116609f35df8): recorded the initial greenfield scaffolding upload.
- 2026-05-09 — `PR-001` ([`9aa78e4`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/9aa78e40a46673ec9399d4bb508209dea5226c95)): wired the local JSON Schema `$ref` resolver, made `make schemas` and `make test` executable, and activated three CI workflows.

### Changed

- 2026-05-09 — `PR-002` ([`cd27539`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/cd275394f8949ab7cfb61cf63b5b4fa03066aa38)): established the validator/test floor, added governed-API smoke and response-envelope shape coverage to `api-test`, and converted domain-alias schemas to `unevaluatedProperties` for `allOf`/`$ref` composition.

### Fixed

- 2026-05-09 — `PR-003` ([`ccd3fe8`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/ccd3fe8c333b2d11ad5c1a4189f20821f2577e27)): corrected the **CONFIRMED** invalid-fixture/schema floor mismatch by tightening schemas and seeded the **PROPOSED** hydrology `wbd_huc12` source spine with ADR-0026.

<!-- kfm-showcase:start -->
<p align="center">
  <img src="docs/brand/readme/kfm-divider.svg" alt="" width="100%" />
</p>

<p align="center">
  <a href="README.md"><b>↩ Project home</b></a> ·
  <a href="README.md#see-it-in-action">See it in action</a> ·
  <a href="README.md#take-the-tour">Tour</a> ·
  <a href="README.md#things-to-try">Things to try</a> ·
  <a href="README.md#faq">FAQ</a> ·
  <a href="docs/brand/readme/README.md">Artwork</a>
</p>
<!-- kfm-showcase:end -->
