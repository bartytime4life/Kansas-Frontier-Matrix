<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/brand/readme-artwork
title: docs/brand/readme — README artwork
type: readme
version: v1.0
status: draft
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: "Human-facing record of the illustrative SVG artwork used by the root README and docs landing page; not map product, evidence, policy, review, release, or publication authority."
truth_posture: CONFIRMED asset inventory and accessibility treatment in this directory / PROPOSED palette tokens inherited from docs/brand/visual-language.md
related:
  - README.md
  - docs/README.md
  - docs/brand/README.md
  - docs/brand/visual-language.md
[/KFM_META_BLOCK_V2] -->

# README artwork

Illustrative, animated SVG artwork for the repository's front door: the [root README](../../../README.md) and the [docs landing page](../../README.md).

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

## Design rules applied

- **Palette** — the PROPOSED tokens in [`visual-language.md` §6.2](../visual-language.md#62-proposed-palette) plus the logo navy and gold from [`logo/tokens/colors.tokens.json`](../logo/tokens/colors.tokens.json). Each image carries its own background so it reads in GitHub light and dark themes.
- **Motion** — CSS-only, slow, linear or single ease-out curves, no bounce. Animations start mid-cycle so the first frame is never empty. Every file includes `@media (prefers-reduced-motion: reduce)`, which stops motion and shows a complete still frame.
- **Trust signals are never decorated** — outcome labels (`ABSTAIN`, `DENY`) are static text; no badge morphs between states, per [`trust-state-visuals.md`](../trust-state-visuals.md).
- **Accessibility** — every SVG has `role="img"`, a `<title>` and a `<desc>`; the README `<img>` tags carry matching `alt` text. Text inside images duplicates content that also appears in the README.
- **Self-contained** — no scripts, external fonts, `foreignObject` or remote references, so GitHub's image proxy renders them unchanged.

## Changing an asset

Keep claims inside an image in step with the README text and the linked source guides. If a feature's behavior or a quoted count changes, update both. Re-check each file still parses as XML and still honors reduced motion. These images may be reused in talks or posts with the caption “Illustration — not a data product”.
