# Outdoor access and soil survey layers — November 13, 2026

Three off-by-default, `EXTERNAL_CONTEXT_ONLY` layers fill gaps that the
composition's own pipeline catalogue lists (`outdoor-access` for Ecology and
Fauna, `soil-survey` for Agriculture and Land). They are display context, not
the governed admission lanes those catalogue entries describe.

| Layer | Provider | Kind | Clock |
|---|---|---|---|
| Wildlife areas · KDWP | Kansas Department of Wildlife and Parks | Clickable polygons (`feed=kdwp-wildlife-areas`) | Current public layer |
| Walk-in hunting access | KDWP (layer in the public 2026–2027 WIHA map) | Clickable polygons (`feed=kdwp-wiha-access`) | Current season layer |
| Soil survey · map units | USDA NRCS SSURGO (SDM WMS) | Provider image, zoom 12+ | Current SSURGO edition |

A live check on 2026-11-13 returned 266 wildlife-area polygons and 3,591 WIHA
tracts (two provider pages, about 2 MB after provider-side simplification).

**Boundaries.** KDWP outlines are simplified display geometry, not legal
boundaries, regulations or hunting permission; seasons, refuges and closures
change. WIHA tracts are private land open to public hunting only under program
rules. The November 13 implementation excluded `CONTRACTID` and `NOTES` as a
conservative project choice, not an established provider confidentiality rule.
The [public-record correction](public-record-context-policy-20261114.md)
supersedes that exclusion: public administrative references, payment rates and
contract expiries are eligible; targeted personal-data safeguards remain. Only
`ksoutdoors.com`/`ksoutdoors.gov` links are kept. SSURGO outlines are map units
(often several soil components), not site-specific soil tests or engineering,
septic or building suitability.

**Not done.** Animal-occurrence layers remain off for the Fauna map, as its own
description states. Tribal context remains with its jurisdiction and
sensitivity review lane.

**Rollback.** Revert the commit; no data, settings or provider change.
