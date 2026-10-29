# DeFlock community-reported ALPR areas

## Scope and status

This standalone hosted Explorer addition provides an optional layer in **Transportation & movement**. It reads OpenStreetMap nodes using the ALPR tagging convention documented by DeFlock. It is not a DeFlock-hosted API, a complete camera inventory, a feed of plate reads, or a KFM released dataset. The layer is off by default and is not a category starter.

**Implemented:** generalized report cells, per-cell counts, source details, opacity, selection, attribution, a current-only time posture, and fail-closed source errors. **Needs verification:** actual deployed-provider access, Kansas coverage, desktop/mobile WebGL acceptance and physical-device performance. Source code and synthetic tests do not establish publication, source admission or independent sensitivity approval.

## Data meaning, rights and sensitivity

- Fixed source: `https://overpass-api.de/api/interpreter`; exact query is exported as `DEFLOCK_QUERY` in the existing live-context adapter directory. It selects the Kansas administrative area (`ISO3166-2=US-KS`, admin level 4), then nodes tagged `man_made=surveillance` and `surveillance:type=ALPR`. The area object must also be returned; missing/ambiguous areas fail instead of becoming a false empty result. Ways and relations are outside this first node-only profile.
- Data: © OpenStreetMap contributors, [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/). [OSM attribution and copyright](https://www.openstreetmap.org/copyright) are linked on the map. DeFlock's software license does not replace OSM's data license. The generalized data response remains available through the same route with explicit ODbL attribution.
- Reports can be incomplete, stale, misclassified or duplicated in the real world. Deduplication rejects repeated OSM node identities; distinct nodes can still refer to one device. Counts are mapped reports, not verified devices, operational coverage, or a safety/routing assessment. No reports never means no cameras.
- KFM's exact-infrastructure sensitivity posture is unresolved for this source. The server reduces positions to deterministic 0.05° grid cells (approximately 4.3 × 5.6 km in Kansas), withholds exact points, OSM node IDs, operators, directions, images, notes and all other tags, and caches only that projection. Cells can extend across the state boundary and are not administrative outlines or field-of-view polygons. Exact-point display requires a separately reviewed policy change.
- The OSM database timestamp and KFM retrieval timestamp remain distinct. Neither proves a camera's installation date, observation date, current presence or operating state. Historical frames hold this layer; the implementation does not fabricate time series.
- This context is not claim-bearing evidence. AI, admission, EvidenceBundle construction, source approvals, signed publication recipes, releases, the second-PC worker and persistent data stores are unchanged.

## Request and display bounds

The browser uses `/api/live-context?feed=deflock-alpr`. Extra query parameters, duplicate parameters and historical dates are rejected before source access. The source URL, geography and query are fixed; no visitor coordinates or arbitrary upstream URL are accepted. Redirects are not followed. The response budget is 2 MiB, the node budget is 5,000, and the deadline is 25 seconds. Querying one extra node makes cap overflow fail rather than silently truncating.

One in-flight request is shared per server process; only normalized cells are cached for up to one hour. Errors clear expired content and apply a one-minute retry cooldown. No expired result is served after a failed refresh. The HTTP response is `no-store` to avoid an extra stale cache beyond the explicit process cache. This is per-process deduplication, not a distributed quota guarantee. Replica-wide load remains an operational qualification item.

The existing browser request lifecycle owns queueing, hiding and obsolete-result cancellation. Turning off the layer cancels its browser consumer. A shared bounded server read may finish for other consumers. No polling is added. The map receives at most 5,000 cells, draws fills/outlines, and shows counts from zoom 8. Source failure clears displayed cells through the existing context lifecycle. Basemap changes restore the selected layer. No new renderer dependency is introduced.

## Placement and authority

The base is hosted branch `a0-hosted-ai-web-20261017` at `b09a9b5fa2c62999d4c228573a69fcfbdbbecbb1`, tree `57e40a5e24844bc8ba726598523a1cb12a8cc0b9`. This is the existing separate GoDaddy application composition, not a new monorepo root. Local reconstruction from the prior checkout was verified against that exact tree before editing. Main and the standalone branch have different layouts.

Directory Rules v2, adopted by [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/2782f3e2793f125b192e7f238b8a406acc4ad44c/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), owns placement. Applying §§5, 10–12: app-local source normalization belongs with the existing deployable's context implementation (`app/deflock.ts`); bounded request code extends its existing `app/api/live-context/` boundary; navigation, keys, drawer fields and source/action traces extend their existing owners; regression checks belong in `tests/`; behavior and source limits belong in `docs/`. Outcome: **PLACE within the existing hosted composition**. No new canonical source, policy, contract, registry, evidence or release home is created. `DIR-PLACE-002`, `DIR-PLACE-007`, `DIR-DATA-004` and `DIR-SOURCE-003` preserve the separate admission/publication boundary.

## Verification and rollback

`tests/deflock.test.mjs` uses synthetic records, including malformed, inactive, duplicate, over-cap, unsafe-tag and upstream-error cases. It exercises generalization, deterministic cell identities, concurrent reads, cache age, failure cooldown, response limits, route parameter rejection, default-off selection and MapLibre style restoration/visibility. Existing transport, context lifecycle, source registry, drawer and temporal tests provide adjacent coverage. Record actual run results in the PR; this document is not a passing receipt.

Rollback is a focused inverse of this addition before any separately authorized publication. The default-off source can be disabled immediately; no database migration, persisted source payload, signed source approval or lifecycle rollback is needed. Keep any future deployment/correction record separate from this source PR.

## Source evidence inspected

- [DeFlock](https://deflock.org/) and [project README](https://github.com/FoggedLens/deflock/blob/master/README.md): OSM-backed community mapping. DeFlock is a project reference, not an official government assertion.
- [DeFlock node query](https://github.com/FoggedLens/deflock/blob/master/serverless/alpr_cache/src/alpr_cache.py), inspected blob `f4f62358c25941c0e28073c6c6041bd08fa057ec`: the two node tags used above. This older cache producer establishes tagging, not current DeFlock infrastructure or refresh guarantees.
- [OSM license](https://www.openstreetmap.org/copyright): attribution and ODbL data terms.
- [DeFlock data pipeline](https://github.com/flockhopper3/deflock-data/blob/main/README.md): downstream tile alternatives exist, including frozen legacy tiles. They are not used in this change; direct public tiles would bypass KFM's chosen generalization boundary.

Research checked October 28, 2026 (America/Chicago). Upstream references may change; no current Kansas camera count is claimed.
