<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/brand/readme-artwork
title: docs/brand/readme — README artwork
type: readme
version: v1.1
status: draft
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: "Human-facing record of the illustrative SVG artwork used by the root README and docs landing page; not map product, evidence, policy, review, release, or publication authority."
truth_posture: CONFIRMED asset inventory, counted figures and accessibility treatment in this directory / PROPOSED palette tokens inherited from docs/brand/visual-language.md
related:
  - README.md
  - docs/README.md
  - apps/site/README.md
  - connectors/README.md
  - CONTRIBUTING.md
  - docs/brand/README.md
  - docs/brand/visual-language.md
[/KFM_META_BLOCK_V2] -->

# README artwork

Illustrative, animated SVG artwork for the repository's front doors: the [root README](../../../README.md), the [docs landing page](../../README.md), the [Explorer README](../../../apps/site/README.md), the [connectors README](../../../connectors/README.md) and the [contribution guide](../../../CONTRIBUTING.md).

> [!IMPORTANT]
> **These images are artwork, not data.** They depict the *kind* of experience an Explorer workspace offers. They are not screenshots, map products, data displays, acceptance evidence, or released KFM layers. Kansas outlines and rivers are hand-simplified; grids, echoes, columns and curves are invented for illustration. Numbers that appear (for example the Underground record counts) are quoted from the linked Site guides at the README's evidence commit and are labelled there.

## Assets

| File | Used for | What it depicts |
|---|---|---|
| [`kfm-hero.svg`](kfm-hero.svg) | Root README banner | Kansas outline, major rivers, observation points and a west-to-east time sweep through eras |
| [`kfm-feature-river-pulse.svg`](kfm-feature-river-pulse.svg) | Feature tour | Pulsing gauges and a discharge chart with a visible gap |
| [`kfm-feature-observatory.svg`](kfm-feature-observatory.svg) | Feature tour | Radar echoes crossing Kansas while an archive playhead advances |
| [`kfm-feature-underground.svg`](kfm-feature-underground.svg) | Feature tour | Isometric strata block with recorded columns on the cut faces |
| [`kfm-feature-evidence-drawer.svg`](kfm-feature-evidence-drawer.svg) | Feature tour | A selected point opening a drawer of source, clocks, role and limits (example values) |
| [`kfm-feature-history.svg`](kfm-feature-history.svg) | Feature tour | A swipe comparison between two years |
| [`kfm-feature-atmosphere.svg`](kfm-feature-atmosphere.svg) | Feature tour | Crossfading soil-moisture cells with drifting, labelled-illustrative wind |
| [`kfm-time-depth.svg`](kfm-time-depth.svg) | Time-depth section | Timeline from 1800 to today with source milestones (piecewise scale) |
| [`kfm-source-lanes.svg`](kfm-source-lanes.svg) | Data-sources section | Seven source themes feeding a single evidence gate |
| [`kfm-trust-path.svg`](kfm-trust-path.svg) | Trust-path section | Lifecycle stages and gates, with publish, hold and abstain/deny outcomes |
| [`kfm-explorer-walkthrough.svg`](kfm-explorer-walkthrough.svg) | “See it in action”; Explorer README | 36-second loop of the eight-step journey: map, area, layers, time, inspect, evidence, report, share |
| [`kfm-by-the-numbers.svg`](kfm-by-the-numbers.svg) | Root README | Odometer digits that roll once to counted figures (see below) |
| [`kfm-layer-stack.svg`](kfm-layer-stack.svg) | “One place, many layers” | Six layer plates separating and settling beside a shared clock |
| [`kfm-focus-mode.svg`](kfm-focus-mode.svg) | “Ask, and see why” | Intents, an example six-gate trace and the four finite outcomes, using names and codes from `app/focus-mode.ts` |
| [`kfm-capability-board.svg`](kfm-capability-board.svg) | Build status; Explorer README | All 23 entries of `app/site-features.ts` grouped by declared status |
| [`kfm-trust-membrane.svg`](kfm-trust-membrane.svg) | Trust section | Public clients, Governed API and internal stores; a refused direct read |
| [`kfm-feature-roads-rail.svg`](kfm-feature-roads-rail.svg) | Feature tour | 1918-style roads drawing over today's grid; a moving train; bridges |
| [`kfm-feature-hazards.svg`](kfm-feature-hazards.svg) | Feature tour | Declared counties, flood-zone bands and lightning-density cells |
| [`kfm-feature-survey.svg`](kfm-feature-survey.svg) | Feature tour | One PLSS township with sections numbered from the northeast |
| [`kfm-feature-reports.svg`](kfm-feature-reports.svg) | Feature tour | A map view fanning out into report, story and workspace drafts |
| [`kfm-contributor-paths.svg`](kfm-contributor-paths.svg) | Contributing; `CONTRIBUTING.md` | Six contributor paths flowing into one draft pull request |
| [`kfm-divider.svg`](kfm-divider.svg) | Section breaks | A sunflower (the Kansas state flower) on a gold rule with a travelling glint; transparent, works in both themes |
| [`kfm-footer.svg`](kfm-footer.svg) | Page footer | Prairie at dusk with stars, a grain elevator, a turning windmill and swaying grass |
| [`kfm-social-preview.png`](kfm-social-preview.png) | Repository social card | 1280 × 640 still built from the hero plus four counted figures. To use it, a repository admin uploads it under **Settings → General → Social preview**; nothing in this repository applies it automatically |

### Light and dark themes

Every graphic on a paper background has a `-dark.svg` twin. Pages use `<picture>` with `prefers-color-scheme` so the image matches the reader's GitHub theme. The hero, footer and divider carry their own backgrounds or are transparent, so they have no twin. Text drawn on navy uses the reserved colours `#FFFFFE` and `#DCE6F3` so theme conversion leaves it legible.

### Counted figures

| Figure | Counted from |
|---|---|
| 23 Explorer features (7 LIVE UI · 12 ACTIVE CONTEXT · 2 BOUNDED PROOF · 2 HELD) | `apps/site/source/app/site-features.ts` |
| 104 connector lanes | direct child directories of `connectors/` |
| 314,844 water-well records · 6,598 core locations | `apps/site/source/docs/underground-explorer.md` |
| 105 Kansas counties | 2020 Census county baseline used by the Explorer |
| 1800, first year on the map clock | `apps/site/source/README.md` (temporal sweep) |
| Focus Mode gates, intents, outcomes and codes | `apps/site/source/app/focus-mode.ts` |

Re-count these when their sources change, and update the images and the README text together.

## Design rules applied

- **Palette** — the PROPOSED tokens in [`visual-language.md` §6.2](../visual-language.md#62-proposed-palette) plus the logo navy and gold from [`logo/tokens/colors.tokens.json`](../logo/tokens/colors.tokens.json). Each image carries its own background so it reads in GitHub light and dark themes.
- **Motion** — CSS-only, slow, linear or single ease-out curves, no bounce. Looping animations start mid-cycle so the first frame is never empty; the walkthrough holds its finished state before it resets; the number odometer and capability board animate once, then rest. Every file includes `@media (prefers-reduced-motion: reduce)`, which stops motion and shows a complete still frame.
- **Trust signals are never decorated** — outcome labels (`ABSTAIN`, `DENY`) are static text; no badge morphs between states, per [`trust-state-visuals.md`](../trust-state-visuals.md).
- **Accessibility** — every SVG has `role="img"`, a `<title>` and a `<desc>`; the README `<img>` tags carry matching `alt` text. Text inside images duplicates content that also appears in the README.
- **Self-contained** — no scripts, external fonts, `foreignObject` or remote references, so GitHub's image proxy renders them unchanged.

## Changing an asset

Keep claims inside an image in step with the README text and the linked source guides. If a feature's behavior or a quoted count changes, update both. Re-check each file still parses as XML and still honors reduced motion. These images may be reused in talks or posts with the caption “Illustration — not a data product”.
