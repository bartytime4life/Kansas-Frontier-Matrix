<!--
KFM_WIKI_SOURCE
page_id: Engineering-Case-Studies
title: Engineering case studies — decisions you can inspect
status: source-grounded showcase; independent review pending
updated: 2026-10-09
authority: orientation-only; repository evidence and adopted authority outrank this page
source_path: docs/wiki/Engineering-Case-Studies.md
publication_effect: native wiki documentation only; no data admission or release
evidence_checkpoint: main@459ffbe892929cbe994add8665805549694740b6
-->

# Engineering case studies

**Three problems. Concrete decisions. Code you can inspect.**

Evidence snapshot: [`459ffbe892929cbe994add8665805549694740b6`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/README.md), inspected October 9, 2026. The links below identify implementation and regression-test source. Test presence is not a claim that this wiki refresh reran the application suite or established hosted acceptance.

[Builder profile](Builder-Profile.md) · [Visual tour](Visual-Tour.md)

## 01 · Make the underground readable

**The challenge.** A compelling 3D scene can accidentally imply continuous strata, surveyed elevation, or measured material properties that individual source logs do not establish.

**The implementation.** The cutaway models recorded intervals, converts source depth units, excludes invalid ranges, and bounds the rendered record/interval set. Camera fitting accounts for projected corners and readable labels. The feature guide preserves the difference between original descriptions, interpretations, inventory envelopes, and illustrative display geometry.

**The product decision.** Keep the scene useful while maintaining access to the original record and its uncertainty. A regional aquifer depth envelope is not a statement that its entire volume contains water. A gap remains a gap.

**Inspect:** [cutaway geometry and camera fitting](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/app/cutaway-model.ts) · [regression tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/tests/cutaway-model.test.mjs) · [feature and source limitations](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/docs/underground-explorer.md).

**What this demonstrates:** translating a domain constraint into geometry, interaction, performance bounds, and readable explanation. Continuous geological reconstruction and full device acceptance remain separate qualification work.

## 02 · Compare time without substituting history

**The challenge.** Two attractive map images can be incompatible, incomplete, or mislabeled. Rapid switching also creates a state-management risk: an old tile or completion callback can arrive after the selected pair has changed.

**The implementation.** Pair selection requires distinct installed years of the same compatible product, matching display properties, and a common prepared zoom. Tile reads preserve same-origin access, reject redirects and invalid payloads, impose byte/time limits, and support cancellation. The non-WebGL overview has explicit tile and concurrency bounds.

**The product decision.** Missing data gets an honest unavailable state. A fallback may change the renderer, but it must preserve the source identity. Visual comparison does not automatically compute land-cover change or prove scientific comparability.

**Inspect:** [pair selection and tile transport](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/app/earth-engine-comparison.ts) · [compatibility, invalid payload, timeout, and cancellation tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/tests/earth-engine-comparison.test.mjs) · [comparison guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/docs/history-comparison.md).

**What this demonstrates:** coordinated UX, asynchronous programming, network boundaries, and failure-state design. Historical catalog coverage does not imply that all those years are installed.

## 03 · Protect the meaning of a downloaded result

**The challenge.** An observation, a review decision, and an active release are different things. An export can also become misleading if the selected station changes while its requests are in flight—even if the user returns to the original station.

**The implementation.** The reviewed-water server reads immutable package bytes separately from trusted activation metadata. It accepts a fixed station set, validates package identity and size, and returns closed negative envelopes when an eligible result cannot be established. The browser revalidates station/package/release identity and uses selection generation to prevent stale A → B → A exports.

**The product decision.** Withhold a result whose identity or release status cannot be established. Keep provider context distinguishable from governed evidence, and communicate why the result is withheld.

**Inspect:** [read-only server boundary](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/app/governed-water-server.ts) · [water conformance tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/tests/governed-water.test.mjs) · [browser availability tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/tests/governed-water-availability.test.mjs) · [delivery and export contract](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/docs/governed-water.md).

**What this demonstrates:** security-minded product engineering that connects backend validation to user-visible state. This case does not claim a currently active real-water release, completed hosted administration, or full security certification.

## Follow the decisions one layer deeper

[Architecture](Architecture.md) explains the component handoffs. [Map, UI, and AI](Map-UI-and-AI.md) follows the user state. [Security and Sensitivity](Security-and-Sensitivity.md) pairs controls with concrete counterexamples. [Development and Validation](Development-and-Validation.md) shows how to evaluate each claim.

## Inspect the work

| Review layer | Evidence | What it establishes |
|---|---|---|
| Product behavior | Feature guides linked above | Intended interaction and documented limits |
| Implementation | Commit-pinned source links | Exact code available for review |
| Regression intent | Adjacent test modules | Scenarios encoded as automated checks |
| Delivery history | [Site delivery checkpoints](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/README.md) | Dated, scoped records; historical results retain their original limits |
| Security expectations | [Security reporting and boundaries](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/SECURITY.md) | Public reporting procedure and project posture, not a certificate |
| Review and integration | [Pull-request history](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pulls?q=is%3Apr) | GitHub's recorded state for each individual change |

The wider [governed API](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/governed-api/README.md) still describes a bounded `ABSTAIN / NOT_IMPLEMENTED` scaffold. These specific application slices should not be mistaken for completion of that broader service.

**The portfolio takeaway:** the interesting work is the connection between design choices, source semantics, implementation details, and the checks that keep them aligned. [Return to the builder profile](Builder-Profile.md).
