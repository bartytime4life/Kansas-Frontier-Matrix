# Compare approved imagery years

The Earth Engine layer controls now open **Compare imagery years**. Choose one
product and two different approved, installed years. The comparison uses the
existing owner-checked, manifest/hash-checked tile routes. It does not run Earth
Engine, download an archive, activate a snapshot, or claim measured change.

Swipe uses two synchronized flat Mercator maps. Its divider is a keyboard range
control: arrow keys adjust the split, Home shows B, and End shows A. **Side by
side** provides the same camera and scale without occlusion. Each side retains
its own observation period, attribution, grid resolution, legend, limits, and
immutable snapshot identity. Pan/zoom controls affect both maps. Closing the
dialog preserves the main map, its terrain/globe view, and its layer choices.

The pair requires the same annual product, source, display resolution, legend,
and at least one common prepared tile zoom. Mixed-date elevation, held products,
ambiguous duplicate years, missing years, and incompatible pairs are unavailable.
PRISM monthly history can begin in 1895 and daily history in 1981, selected by
provider calendar labels. Landsat 4, 5, 7, 8 and 9 remain separate products; the
viewer never silently compares one mission with another. Partial mission years,
Landsat 7 gaps, PRISM source revisions and differing observation conditions
remain review limitations. New recipes do not imply that any year is installed.
These checks support visual comparison; they do not prove scientific
comparability of acquisition conditions, masks, processing, or historical crop
class meanings. Those limits remain visible. No difference statistics, crop
transitions, or causal findings are calculated from display colors.

No current basemap fills imagery gaps. The checkerboard denotes transparency or
unavailable imagery. Tile failures are visible and retryable. Every request has
a 15-second deadline, a 512 KiB PNG limit, same-origin credentials, no browser
cache, and no redirects. Pair changes, renderer switches, and closing abort
outstanding reads. Removed renderers cannot deliver status or pixels to the next
pair. Server admission, owner identity, and byte-integrity checks are unchanged.

**Use 2D images** offers a synchronized tile mosaic without WebGL; it is also the
automatic fallback when WebGL2 cannot initialize. It chooses a common prepared
zoom no higher than 8 with no more than 96 rectangular tile positions per side,
loads at most four tiles concurrently, and revokes temporary image URLs on close.
The image viewer's zoom enlarges the overview; it does not add source detail.
If no bounded overview exists, source details remain readable and the viewer
reports that the overview is unavailable. Historical holes never reuse another
year's pixels.

## Ownership, validation, and rollback

The deployable UI and its pure comparison/transport helpers remain under this
Site's `app/`; regressions under `tests/`; this explanation under `docs/`. The
monorepo mirror preserves those responsibilities under `apps/site/source/`,
consistent with adopted Directory Rules v2 and ADR-0029. No canonical schema,
registry, policy, data, or release home is introduced. The Site-local comparison
types are display adapters, not source-admission contracts.

Run `node --test tests/earth-engine-comparison.test.mjs`, TypeScript, production
build, full Site tests, and lint. The focused suite covers approved/held/ambiguous
years, incompatible pairs, missing zooms, bounded overviews, exact tile paths,
same-origin access, PNG/size refusal, whole-request timeouts, cancellation and
late results. Browser acceptance separately covers real approved pairs, swipe
and side-by-side pan/zoom, keyboard divider, mobile layout, missing tiles,
WebGL fallback, dialog focus/Escape, and unchanged main-map state.

Rollback removes the additive comparison launch/component/helpers/styles and
restores the prior Site source. No private records, display sets, active pointers,
main-map storage, or Earth Engine exports need to be changed.

## Main-map year selection repair · 2026-10-06

Browser acceptance found that the main-map Landsat 4 and 5 selectors visually
fell back to their last option while their preparation links still used 2024.
The controls now prefer the latest approved installed year of that same product
within its source bounds. Without installed imagery, the 2024 default is bounded
by the product's supported years: 1993 for Landsat 4 and 2012 for Landsat 5.
The selection, source-period explanation, renderer state and preparation link
use the same year. These source bounds do not establish usable Kansas imagery.

Invalid or fractional selection events retain the previous valid choice. A
deliberately selected supported year without installed imagery stays unavailable;
the viewer removes the previous year's source rather than substituting pixels.
Defaults do not activate layers. Mixed-date elevation is unchanged. The source
recipe link uses count-free wording so adding recipes cannot stale its label.

`tests/earth-engine-display-years.test.mjs` exercises rendered controls, actual
selection handlers, renderer year projection and removal of the previous map
source. It covers the two expired mission defaults, approved installed defaults,
invalid input and supported missing years. This is a bounded display correction;
it does not alter source approval, installation, tile authorization or admission.

The bounded repair passed production builds, TypeScript and all 545 Node tests
in both the standalone Site candidate and repository mirror. Full lint reported
0 errors and the same 46 inherited warnings in each. The five new regression
tests are included in that total. This record describes code validation;
post-repair browser acceptance and deployment remain separate checks.
