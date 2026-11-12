<!--
KFM_WIKI_SOURCE
page_id: Project-Status
title: Project Status
status: source-grounded documentation candidate; independent review pending
updated: 2026-11-11
authority: orientation-only; repository evidence and adopted authority outrank this page
source_path: docs/wiki/Project-Status.md
evidence_checkpoint: main@d4d84171653a2f2582b48ece511dc010857fde15; historical-hosted@bbcec824fe57e6be0409ba1e35d737fa99581560
publication_effect: none until reviewed source is separately synchronized
-->

# Project Status

**November 11, 2026: source identity first, then the claim.**

## Current repository checkpoint

| Surface | Recorded result | Boundary |
|---|---|---|
| Inspected monorepo | main `d4d84171653a2f2582b48ece511dc010857fde15` | Contains externally merged PR #5822; its tree equals that PR's head tree |
| Explorer source | `apps/site/source/` at `8a532b34eb691c06a53325ef553ea248ebbb11d5` | Preserved Sites lineage plus repository overlays |
| Local application validation | Build/types; 1,804 Site tests; lint zero errors and 77 inherited warnings | Node 22.13.1 and clean exact-lock install |
| Conformance and route smoke | 380 checks including 79 mirror checks; 110 smoke checks across 79 routes | Fourteen provider-only routes unexercised |
| PR #5822 CI | 52 successes and one skip at readback | Exact submitted head; merge and deployment are distinct |
| Browser and deployment | Interval-load browser acceptance pending; no new deployment performed | The browser tool could not create a test tab |

[Current review and documentation audit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/reports/documentation-currentness-review-20261111.md) ·
[Explorer guides](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/site/source/docs/README.md).

The following qualification remains historical. Its public Node counts and
media do not describe the current repository mirror or a freshly read deployment.

## Historical public qualification — October 27, 2026

| Surface | Result | Evidence boundary |
|---|---|---|
| Monorepo source | `17f106d558674ec92a11809bcf3a06c82453777e` inspected | The documentation author's base, not a runtime deployment |
| Public Node application | `bbcec824fe57e6be0409ba1e35d737fa99581560`; exact-lock install and production build completed | Separate standalone source tree |
| Node tests | **1,934 pass · 19 skip · 0 fail; 1,953 total** | Full existing application test command on this execution host |
| TypeScript | `node_modules/.bin/tsc --noEmit` exited zero | Same application revision and installation |
| Recorded media | Five complete source captures; input/output hashes, duration, dimensions and finite motion checked | Existing October 20 renderer output, not a production speed recording |
| Browser observation | Public category welcome and water-tour selection inspected in Chrome | Session-limited UI observation; complete tour playback/provider health not certified |
| Native wiki | Source prepared for reviewed synchronization | A draft PR does not publish the separate wiki |

[Detailed commands, skipped coverage and limits](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/a27c45354b461cd2fd5978efe7a7aacfc5f064ac/docs/reports/documentation-showcase-qualification-20261027.md) ·
[Application source](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/bbcec824fe57e6be0409ba1e35d737fa99581560) · [Media provenance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/974d3b340e619effc91d8da98cf9e67d95119df9/docs/brand/readme/showcase-media.json).

## What those checks cannot establish

The 19 skipped tests remain skipped. Test execution is bounded to the test inputs
and host; it does not establish real-provider coverage, owner-host throughput,
whole-site accessibility, other browser engines, sustained GPU/memory behavior,
scientific validity, live inference health or source admission/release closure.
No repository-wide security certification or production performance gain is claimed.

## Keep the source histories distinct

| Responsibility | Source |
|---|---|
| Public Explorer, chat and Node routes | [Hosted composition](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/bbcec824fe57e6be0409ba1e35d737fa99581560) |
| Evidence contracts, schemas, policies, connectors and release support | [Monorepo](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/17f106d558674ec92a11809bcf3a06c82453777e) |
| Preserved Sites application | [apps/site](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/17f106d558674ec92a11809bcf3a06c82453777e/apps/site/README.md) |
| Human orientation | Reviewed `docs/wiki` projected into the native wiki |

Earlier pages in this wiki retain explicitly dated historical checkpoints. In
particular, October 9 owner-private Sites metadata does not describe today's separate
public Node website. Current source selection is explained in [Getting Started](Getting-Started.md).

## Status language

**CONFIRMED** means verified for the named scope. **PROPOSED** means unadopted or
unverified design. **NEEDS VERIFICATION** identifies a remaining check. **UNKNOWN**
means evidence is insufficient. A green test, map display, generated answer or wiki
page cannot perform review, approval, deployment or governed publication.

[Development and Validation](Development-and-Validation.md) · [Governance and Evidence](Governance-and-Evidence.md)
