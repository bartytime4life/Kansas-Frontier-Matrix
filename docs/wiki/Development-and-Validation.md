<!--
KFM_WIKI_SOURCE
page_id: Development-and-Validation
title: Development and Validation
status: source-grounded documentation candidate; independent review pending
updated: 2026-11-11
authority: orientation-only; repository evidence and adopted authority outrank this page
source_path: docs/wiki/Development-and-Validation.md
evidence_checkpoint: main@d4d84171653a2f2582b48ece511dc010857fde15; historical-hosted@bbcec824fe57e6be0409ba1e35d737fa99581560
publication_effect: none until reviewed source is separately synchronized
-->

# Development and Validation

**Run the component you intend to evaluate. Report the result it actually produced.**

## Verify the repository Explorer

Use the Site's exact-lock installer and built Worker workflow in
[Installation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/installation.md#explorer-site-mirror).
Build before tests that import generated server output. At PR #5822 head
`8a532b34eb691c06a53325ef553ea248ebbb11d5`, recorded checks passed the build,
types, 1,804 Site tests, 380 conformance checks and 110 local route smoke checks;
lint had zero errors and 77 inherited warnings. Its CI readback has 52 successes
and one skip. These are separate from pending browser acceptance and deployment.
[Source and documentation review](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/reports/documentation-currentness-review-20261111.md).

## Reproduce the historical public application check

At hosted composition [`bbcec824fe57`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/bbcec824fe57e6be0409ba1e35d737fa99581560), after `npm ci`:

```bash
npm test
node_modules/.bin/tsc --noEmit
```

`npm test` runs the production build and the Node test suite. The October 27 qualification observed
exit zero, **1,934 passing and 19 skipped tests**, with no failures. TypeScript exited
zero separately. These counts include nested tests and are the runner's totals,
not a hand count of test files. [Detailed qualification](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a27c45354b461cd2fd5978efe7a7aacfc5f064ac/docs/reports/documentation-showcase-qualification-20261027.md).

## Match the check to the claim

| Check | Supports | Does not establish |
|---|---|---|
| Production build | The declared source compiles/packages in this environment | Successful deployment or provider operation |
| Node tests | Existing isolated assertions pass for their inputs | Exhaustive correctness, real data completeness or security certification |
| TypeScript | The configured type checks complete | All runtime behavior |
| Media validation | The selected source and derivative bytes match their record; decoded motion is finite | Real-time FPS, live observations or scientific validity |
| Chrome observation | The inspected welcome/category states appeared in this session | A full browser/device/accessibility matrix |
| Markdown/link/wiki checks | Navigation, source structure and projection behavior | Truth, policy authority or native publication |

## Scientific qualification

Software tests and scientific evaluation answer different questions. A schema
can validate shape while a model remains uncalibrated or unsuitable for its
intended population, support, and prediction horizon.

For a proposed [scientific investigation](scientific-methods.md), declare the
target quantity, units, support, baseline, evaluation split, metrics, and rejection
criteria before final scoring. Keep spatial neighbors, repeated stations, and
future information from leaking into a holdout in ways incompatible with the
intended prediction task. Fit preprocessing and tuning within the training
process; keep the final evaluation separate from model selection.

Inspect error and bias, interval behavior where applicable, coverage gaps, and
sensitivity to assumptions and aggregation. Include negative results and
deviations from the plan. A declaration validator, one attractive score, or
reproducible code does not establish scientific validity, qualified review,
source admission, or release eligibility. The
[detailed guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/496a97280e72b22a5c83d48725e51828ab9c7237/docs/architecture/scientific-analysis.md)
maps existing repository candidates to their narrower responsibilities.

## Documentation checks

The [documentation maintenance runbook](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/runbooks/documentation-maintenance.md)
gives explicit changed-file commands and a tracked-file inventory scan. Local
link resolution, metadata, freshness and document-graph results retain separate
coverage and inherited-debt boundaries. Do not advance historical dates to
manufacture freshness.


Use the repository's existing documentation validators under
[tools/validators/docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/17f106d558674ec92a11809bcf3a06c82453777e/tools/validators/docs), the generated-work
receipt validator and the finite wiki-sync contract tests. Record failures and skips
without converting them to passes. Native wiki projection is dry-run first and
requires the reviewed immutable source; see [Wiki Maintenance](Wiki-Maintenance.md).

## Local operation and recovery

Keep source, browser origin and stored data identities distinct. Consult the
[preserved local-operation guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/17f106d558674ec92a11809bcf3a06c82453777e/apps/site/source/docs/local-pc-consolidation.md)
before replacing a local source folder. Historical workstation paths are examples;
a documentation refresh must not select an empty store or reset private records.

## Other components

`main` root npm scripts intentionally report `WORKFLOW_HOLD`. The preserved Sites
mirror, governed API, local-data tools and pipeline/contract validators own their own
commands and acceptance. [Installation guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/17f106d558674ec92a11809bcf3a06c82453777e/docs/installation.md)
provides those separate routes.

[Getting Started](Getting-Started.md) · [Project Status](Project-Status.md) · [Contributing](Contributing.md)
