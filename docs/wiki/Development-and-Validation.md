<!--
KFM_WIKI_SOURCE
page_id: Development-and-Validation
title: Development and Validation
status: source-grounded documentation candidate; independent review pending
updated: 2026-10-27
authority: orientation-only; repository evidence and adopted authority outrank this page
source_path: docs/wiki/Development-and-Validation.md
evidence_checkpoint: main@17f106d558674ec92a11809bcf3a06c82453777e; hosted@bbcec824fe57e6be0409ba1e35d737fa99581560
publication_effect: none until reviewed source is separately synchronized
-->

# Development and Validation

**Run the component you intend to evaluate. Report the result it actually produced.**

## Reproduce this application check

At hosted composition [`bbcec824fe57`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/bbcec824fe57e6be0409ba1e35d737fa99581560), after `npm ci`:

```bash
npm test
node_modules/.bin/tsc --noEmit
```

`npm test` runs the production build and the Node test suite. This session observed
exit zero, **1,934 passing and 19 skipped tests**, with no failures. TypeScript exited
zero separately. These counts include nested tests and are the runner's totals,
not a hand count of test files. [Detailed qualification](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/codex/docs-living-showcase-20261027/docs/reports/documentation-showcase-qualification-20261027.md).

## Match the check to the claim

| Check | Supports | Does not establish |
|---|---|---|
| Production build | The declared source compiles/packages in this environment | Successful deployment or provider operation |
| Node tests | Existing isolated assertions pass for their inputs | Exhaustive correctness, real data completeness or security certification |
| TypeScript | The configured type checks complete | All runtime behavior |
| Media validation | The selected source and derivative bytes match their record; decoded motion is finite | Real-time FPS, live observations or scientific validity |
| Chrome observation | The inspected welcome/category states appeared in this session | A full browser/device/accessibility matrix |
| Markdown/link/wiki checks | Navigation, source structure and projection behavior | Truth, policy authority or native publication |

## Documentation checks

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
