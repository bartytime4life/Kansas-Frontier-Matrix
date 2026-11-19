# Fire-weather, drought, public-land and historic-place layers — November 13, 2026

Ported from monorepo PR #5829 (`apps/site/source`) into this GoDaddy Node
composition. All additions are off by default and `EXTERNAL_CONTEXT_ONLY`; none
creates a KFM EvidenceBundle, source admission or release.

| Layer | Provider | Kind | Clock |
|---|---|---|---|
| Fire-weather outlook · Day 1 | NOAA SPC | Provider image | Current Day 1 issuance |
| Drought outlook · seasonal | NOAA CPC | Provider image | Current seasonal outlook |
| Public & protected lands | USGS PAD-US 4.0 | Provider image | PAD-US 4.0 compilation |
| Historic places · National Register | National Park Service | Clickable points (`/api/live-context?feed=nps-nrhp-places`) | Current public NPS locations |

The monorepo change also added an SPC severe outlook, MRMS rainfall, a WPC rain
forecast, NLCD land cover and NWS storm reports. This composition already has
richer Storm desk, rainfall and land-cover features for those products, so they
were **not** ported to avoid duplicate toggles.

Also included: inline legend chips, NEW markers, four themed starters
(Drought & water, Fire season, Heritage trail, Open lands & waters) and a
**Surprise me** starter. The local companion official-source cap rises from 50
to 54 so context requests listing every source remain valid.

**Boundaries.** Outlooks are forecasts, not observations, burn bans, warnings or
drought designations. PAD-US inclusion does not grant access or title. National
Register points come only from the NPS public, non-restricted service; sensitive
locations are withheld by NPS and never inferred. Listings marked removed are
omitted, and only `catalog.archives.gov` record links are kept.

**Rollback.** Revert the port commit. No database, settings, model or data change
is involved.
