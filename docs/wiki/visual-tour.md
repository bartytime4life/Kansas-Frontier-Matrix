<!--
KFM_WIKI_SOURCE
page_id: Visual-Tour
title: Visual tour — place, time, and evidence
status: source-grounded showcase; independent review pending
updated: 2026-10-09
authority: orientation-only; repository evidence and adopted authority outrank this page
source_path: docs/wiki/visual-tour.md
publication_effect: native wiki documentation only; no data admission or release
evidence_checkpoint: main@459ffbe892929cbe994add8665805549694740b6
-->

# Visual tour

**From a place on the map to the records behind it.**

This is an illustrated product walkthrough. The diagrams are original project artwork, not screenshots, live readings, or an assertion that every proposed capability is accepted. Each stop links to source documentation at the inspected repository revision.

[Builder profile](builder-profile.md) · [Engineering case studies](engineering-case-studies.md)

## 01 · Start with a place

<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-explorer-walkthrough-dark.svg" /><img src="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-explorer-walkthrough.svg" alt="Conceptual map workspace with investigation controls, source context, and an evidence panel." width="100%" /></picture>

Choose an area, establish the question, then bring the relevant context into view. The Explorer's [map research tools](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/docs/map-research-tools.md) connect measurement, comparison, saved investigations, and reporting. The design goal is a short path from exploration to an inspectable source.

**Design decision:** Reveal detail as the investigation needs it, while keeping the map and its context legible.

## 02 · Look beneath the surface

<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-feature-underground-dark.svg" /><img src="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-feature-underground.svg" alt="Illustrative subsurface columns with source-specific depths, separated intervals, and a linked surface context." width="100%" /></picture>

The [Underground Explorer](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/docs/underground-explorer.md) connects location selection to recorded wells, cores, and original intervals. Its cutaway makes depth easier to inspect, while source descriptions, gaps, and units remain available.

**Design decision:** Use 3D to explain recorded structure. Preserve unknowns and keep illustrative column width distinct from geographic footprint. Record time filters records; it does not reconstruct changing geology.

## 03 · Put two moments side by side

<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-feature-history-dark.svg" /><img src="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-feature-history.svg" alt="Illustrative Kansas history comparison showing two time views with retained source context." width="100%" /></picture>

[Historical imagery comparison](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/docs/history-comparison.md) supports swipe and side-by-side views for compatible approved, installed years of one product. Each side retains its period, attribution, and limitations; unavailable imagery stays unavailable. A bounded image-mosaic fallback supports inspection without WebGL.

**Design decision:** Make the comparison easy to operate without suggesting that color differences alone establish a measured or causal change.

## 04 · Keep evidence within reach

<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-feature-evidence-drawer-dark.svg" /><img src="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/kfm-feature-evidence-drawer.svg" alt="Conceptual evidence drawer beside a map, presenting source identity, time, and limitations." width="100%" /></picture>

The evidence interface gives the selected result a source and a context. The [reviewed-water implementation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/apps/site/source/docs/governed-water.md) separates source observations from independently trusted review/release metadata and withholds data when an eligible release cannot be established.

**Design decision:** A useful application explains absence, expiry, and uncertainty as carefully as it explains a visible result.

## What to ask in a demonstration

| Try this | Observe this |
|---|---|
| Select a recorded subsurface interval | Original description, unit, depth reference, and source context remain attached |
| Select an imagery year with no installed data | The previous year's image is not silently reused |
| Switch areas or stations during a load | A late response cannot be presented as the newly selected result |
| Inspect a withheld reviewed-water response | The interface distinguishes unavailable release state from absence of a source observation |

These are a review agenda, not a claim that this wiki refresh performed application acceptance. The hosted Explorer remains owner-private; the [installation guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/docs/installation.md) and public source provide a separate route for technical evaluation.

**Next:** [Read the engineering decisions](engineering-case-studies.md). [Artwork inventory and limitations](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/459ffbe892929cbe994add8665805549694740b6/docs/brand/readme/README.md).
