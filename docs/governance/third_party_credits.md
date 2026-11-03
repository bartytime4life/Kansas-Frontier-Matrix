<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/governance-third-party-credits
title: Third-party credits and license references
type: attribution-notice
version: v1.0
status: informational; source-grounded inventory; human review pending
owners: ["@bartytime4life"]
created: 2026-11-03
updated: 2026-11-03
policy_label: public-doc
owning_root: docs/
responsibility: "Recognize external data, software, services and media without changing their licenses or source-admission status."
truth_posture: "CONFIRMED repository and upstream references; deployment compliance and exhaustive dependency coverage NEEDS VERIFICATION."
related:
  - ../../LICENSE
  - ../../AUTHORS.md
  - data_license.md
[/KFM_META_BLOCK_V2] -->

# Third-party credits and license references

Kansas Frontier Matrix thanks the people, agencies, research groups, archives
and open-source communities whose work supports this project. Credit belongs to
the original creators and contributors as well as the services carrying it.

This inventory was checked on **November 3, 2026**, against repository
[`main@f5bf5d04`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/f5bf5d04a89fa13c3207efb9ec5844b77461b9c5).
The separately maintained Node Explorer was inspected at
[`4a9ef78`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/4a9ef7871003964f8be802c3435b2f86f2fbcd43).
These are different source compositions; neither identifies the deployed build.
Cataloged or optional integrations below are not claims that every dataset is
installed, active, approved or redistributed.

## Which license applies

| Material | Governing terms |
|---|---|
| KFM source code, schemas, policy, workflows and tests | [Apache License 2.0](../../LICENSE). The standard license text is retained. |
| KFM-authored documentation and datasets | [CC BY 4.0](data_license.md), as already selected by the owner. |
| External data, imagery, maps, media, fonts, software and model weights | Their own licenses, copyright notices, attribution requirements and applicable service terms. |
| Derived or combined material | KFM can license only the rights it holds; upstream conditions continue to apply. |

This is an acknowledgment and navigation document, not a new license or a legal
clearance of existing uses. It does not replace full upstream license texts,
required on-screen attribution, source-specific permissions or usage limits.
Names and marks identify sources; no affiliation, sponsorship or endorsement
is claimed.

## Maps, environmental data and research sources

| Provider or community | Work recognized and terms to retain |
|---|---|
| **U.S. Geological Survey (USGS)** | Water Data, earthquakes, The National Map, 3DEP elevation, Landsat, historical topographic and geologic records. Credit USGS and the specific product, edition and authors; retain identified third-party exceptions. See the [USGS licensing guidance](https://www.usgs.gov/data-management/data-licensing). |
| **NOAA, National Weather Service and NCEI** | Weather alerts, radar, satellite, station histories, GHCN Daily, climate normals, storm events, National Water Model and NADCON5 grids. Credit the originating office and product. See the [NWS disclaimer](https://www.weather.gov/disclaimer); federal hosting does not establish the rights of every contributed item. |
| **USDA NASS and NRCS** | Cropland Data Layer, agricultural and soil information, SSURGO and SCAN references. Preserve agency/product/year credits and the rights recorded by the relevant [connector](../../connectors/README.md) and source descriptor. |
| **U.S. Census Bureau** | TIGER/Line reference geography and Census statistical context. Credit the Census Bureau and the release year. See [TIGER/Line documentation](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html). |
| **PRISM Group, Oregon State University** | Climate grids, normals and derived summaries. Credit the provider, URL and actual access date. Reproduced PRISM map graphics also need the full copyright notice, URL and map creation date. PRISM retains ownership; see its [terms of use](https://prism.oregonstate.edu/terms/). |
| **Iowa Environmental Mesonet, Iowa State University** | Airport wind and station histories, radar/weather archives and summaries. Preserve IEM and originating-network credit; its [disclaimer](https://mesonet.agron.iastate.edu/disclaimer.php) describes lawful public-domain use and requests acknowledgment. |
| **Kansas Geological Survey (KGS), University of Kansas, and Kansas DASC** | Geology, aquifers, wells, map discovery and aerial imagery. Keep KGS's required source citation and existing copyright notices under its [terms](https://www.kgs.ku.edu/General/copyright.html). DASC/Kansas 911/Surdex and other contributor credits remain attached to the relevant imagery. Item-specific holds remain in force. |
| **Kansas Department of Transportation (KDOT)** | Transport and road-history references, maps and source records. Preserve KDOT/product/date credits and the item-specific terms. Existing exclusions of KDOT PDFs and map-derived vectors/OCR from curated redistribution remain in place; credit alone does not remove them. |
| **OpenStreetMap contributors** | Community map data under [ODbL](https://www.openstreetmap.org/copyright). Display **© OpenStreetMap contributors** with a link to its copyright/license page; database reuse may carry share-alike obligations. The [standard tile service policy](https://operations.osmfoundation.org/policies/tiles/) is separate from the data license. |
| **OpenFreeMap and OpenMapTiles** | Vector map delivery, styles and underlying map work. Preserve OpenFreeMap, OpenMapTiles and OpenStreetMap contributor attribution. See the [OpenFreeMap integration guide](https://openfreemap.org/quick_start/); keep upstream font and sprite notices too. |
| **Mapzen / Tilezen and AWS Open Data** | Terrain Tiles / Terrarium elevation mosaics. Keep the source-specific credits listed in the [terrain attribution record](https://github.com/tilezen/joerd/blob/master/docs/attribution.md), and an actual access date for the [AWS dataset](https://registry.opendata.aws/terrain-tiles/). AWS hosting does not replace the underlying data terms. |
| **Esri and World Imagery contributors** | Optional imagery basemap and ArcGIS-hosted source context. Preserve Esri and the layer's contributing-source credits. Follow the [attribution and licensing requirements](https://location.arcgis.com/help/licensing-and-attribution/) and the applicable item/service terms; a reachable tile URL does not itself grant caching or redistribution rights. |
| **Open-Meteo and originating weather-model providers** | Forecast/weather context, including GFS-driven wind displays. Credit Open-Meteo and relevant model providers under [CC BY 4.0](https://open-meteo.com/en/licence). Its [API terms](https://open-meteo.com/en/terms) separately limit free service to noncommercial use and impose request limits. |
| **European Union / ESA / Copernicus and ECMWF** | Sentinel imagery, reanalysis and Copernicus products. Preserve each product's license and attribution; for modified Sentinel imagery use the required notice with the actual source year, such as “Contains modified Copernicus Sentinel data 2024” for the existing 2024 package. See the [Sentinel catalog and terms](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED). |
| **Google and World Resources Institute** | Dynamic World land-cover data. Retain CC BY 4.0 attribution, dataset citation and the associated Sentinel notices from the [dataset catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1). |
| **UCSB Climate Hazards Center** | CHIRPS precipitation. Retain the dataset attribution and Funk et al. (2015) citation recorded in the [Earth Engine source catalog](../../apps/site/source/app/earth-engine-data.ts). |
| **University of Idaho / University of California, Merced** | TerraClimate climate and drought grids. Retain provider and scientific-study credit alongside the CC0 terms recorded in the [Earth Engine source catalog](../../apps/site/source/app/earth-engine-data.ts). |

For KGS material to which its website terms apply, retain this source citation:

> The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved.

For PRISM, record the access date of the actual input; this document's review
date is not a data-access date. The existing curated baseline records local
holdings accessed October 8, 2026, and separately identifies Earth Engine gap
candidates accessed October 6. See the
[curated baseline manifest](../../tools/local_data/catalogs/github-baseline/baseline-manifest.json).

Additional catalog and connector references recognize **NASA/Earthdata; FEMA;
EPA/AirNow; BLM; USFWS; OSMRE; federal transportation agencies; Kansas Mesonet
and Kansas State University; Kansas Historical Society, Kansas Memory and state
archives; Library of Congress; Internet Archive; GBIF; iNaturalist; Cornell
Lab of Ornithology/eBird; iDigBio; Symbiota; NatureServe; and ISRIC**.
Their presence in the [connector inventory](../../connectors/README.md) or
[public-map catalog](../../apps/site/source/app/public-map-catalog.json)
does not confer permission to redistribute individual records, scans, photos,
restricted occurrences, genealogical material or contributed content.

The [source registry](../../data/registry/sources/README.md), source descriptors,
per-item rights and release records remain the detailed record of attribution,
rights and unresolved restrictions. This page does not change their decisions.

## Open-source software

Thanks to these projects and all their upstream contributors. The versions and
license labels below come from the repository's
[Explorer manifest](../../apps/site/source/package.json) and
[lockfile](../../apps/site/source/package-lock.json) at the inspected revision.
Full license and copyright texts shipped by each package remain controlling.

| Software | Recorded license / credit |
|---|---|
| [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js), 6.9.0 | BSD-3-Clause; MapLibre contributors and retained Mapbox/upstream notices. |
| [Mapbox vector-tile-js](https://github.com/mapbox/vector-tile-js), 2.0.4, and [Pbf](https://github.com/mapbox/pbf), 4.0.1 | BSD-3-Clause; retain each package's notices. |
| [h5wasm](https://github.com/usnistgov/h5wasm), 0.10.3 | NIST-developed software with its own complete notice and bundled HDF5 notices; not a blanket MIT license. Explicitly acknowledge the National Institute of Standards and Technology and retain The HDF Group / University of Illinois notices in `LICENSE.txt`. |
| [LERC](https://github.com/Esri/lerc), 2.0.0 | Apache-2.0; Esri and contributors. |
| [React, React DOM and React Server DOM](https://github.com/facebook/react), 19.2.8 | MIT; Meta and contributors, with upstream notices. |
| [Next.js and eslint-config-next](https://github.com/vercel/next.js), 16.4.2 | MIT; Vercel and contributors. |
| [Three.js](https://github.com/mrdoob/three.js), 0.186.1 | MIT; Three.js authors and contributors. |
| [polygon-clipping](https://github.com/mfogel/polygon-clipping), 0.15.7 | MIT. |
| [sunrise-sunset-js](https://github.com/udivankin/sunrise-sunset-js), 3.3.1 | ISC. |
| [Vinext](https://github.com/cloudflare/vinext), 0.0.50 KFM fork | MIT; Cloudflare and contributors. Preserve the bundled license and [KFM modification notice](../../apps/site/source/vendor/vinext-kfm.README.md). |
| [Vite](https://github.com/vitejs/vite), 8.3.4; [React/RSC plugins](https://github.com/vitejs/vite-plugin-react), 6.0.2 / 0.5.26 | MIT. |
| [Cloudflare Vite plugin](https://github.com/cloudflare/workers-sdk), 1.54.2; [Wrangler](https://github.com/cloudflare/workers-sdk), 4.127.1 | MIT for the plugin; MIT OR Apache-2.0 for Wrangler. Included runtimes/dependencies retain their own terms. |
| [Tailwind CSS and its PostCSS plugin](https://github.com/tailwindlabs/tailwindcss), 4.2.1 | MIT. |
| [TypeScript](https://github.com/microsoft/TypeScript), 5.9.3 | Apache-2.0. |
| [ESLint](https://github.com/eslint/eslint), 9.39.4 | MIT. |
| [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) Node / React / React DOM / Three types | MIT; the exact type-package versions are in the lockfile. |

The separately inspected Node composition also uses **mysql2** (MIT) and a
modified **Braces** package (MIT), and has different Vite/Vinext pins. Its
[manifest](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/4a9ef7871003964f8be802c3435b2f86f2fbcd43/package.json)
and [Braces modification record](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/4a9ef7871003964f8be802c3435b2f86f2fbcd43/vendor/braces-kfm.README.md)
identify those differences; the monorepo lockfile does not describe that build.

KFM also thanks the **Node.js, pnpm, Corepack, Python, PyYAML, jsonschema,
referencing, rfc3339-validator, rfc8785, NumPy, Rasterio/GDAL, pyproj/PROJ,
Pillow, earthengine-api, Hydra, Typer, Rich, pytest, Hypothesis, Vitest and
packaging/build-tool communities**. Applicable versions, optional dependencies
and licenses must be taken from each environment's manifests, lockfiles and
installed distributions; this acknowledgment does not assign one license to
all of them. See the [root Python manifest](../../pyproject.toml),
[workspace lockfile](../../pnpm-lock.yaml) and
[Earth Engine raster requirements](../../apps/site/source/scripts/earth-engine/requirements.txt).

## Apps, hosting and AI tools

| Tool or service | Contribution recognized |
|---|---|
| [GitHub](https://github.com/) and GitHub Actions | Repository hosting, contribution history, reviews and CI. |
| [GoDaddy](https://www.godaddy.com/) | Node hosting and domain infrastructure documented in the project runbooks. |
| [Cloudflare](https://www.cloudflare.com/) | Vinext, Workers tooling and the preserved Sites runtime/storage integration. |
| [OpenAI](https://openai.com/), ChatGPT and Codex | AI-assisted implementation, research and authoring, including the current attribution update. |
| [Anthropic](https://www.anthropic.com/), Claude and Claude Code | AI-assisted development and design workflows recorded in repository history. |
| [Google Earth Engine](https://earthengine.google.com/) | Dataset discovery, recipes and separately authorized processing; dataset publishers retain their own rights. |
| [Ollama](https://github.com/ollama/ollama) and [Qwen](https://github.com/QwenLM) | Local inference tooling and candidate model integration. Model weights have model-specific licenses; record the exact publisher, tag and digest before use or redistribution. |

See the [deployment record](../runbooks/deployment-consolidation.md) for dated
tooling evidence. This credit list does not certify current accounts, plans,
service permissions, model admission or deployment. Service agreements and
model licenses are separate from KFM's code license.

## Icons, footage and recorded map tours

The standalone Node composition includes **Phosphor Icons**, copyright
2023 Phosphor Icons, under MIT. Keep its
[full icon license](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/4a9ef7871003964f8be802c3435b2f86f2fbcd43/public/icons/time-sweep/LICENSE)
with redistributed icons.

Its [30-clip motion catalog](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/4a9ef7871003964f8be802c3435b2f86f2fbcd43/app/living-welcome/motion-clips.json)
credits each creator, original source URL, license/version, adaptation and
local file. Those individual credits remain essential: Wikimedia Commons or
another archive hosting a clip is not itself a license for that clip. Retain
the named creators, source and license links, modification notices and any
share-alike obligations. Public-domain entries do not change the terms of
other footage.

The repository's [recorded map tours](../brand/readme/README.md) retain provider
credits and dated limitations. Their
[media manifest](../brand/readme/showcase-media.json) identifies original
captures and derived files. KFM's software license does not relicense provider
pixels shown in videos, screenshots, exported reports or map images.

## Keeping credit attached

- Keep applicable upstream copyright, license, NOTICE, disclaimer and
  modification notices with source and binary distributions, including
  vendored packages, copied browser assets, workers, WASM and fonts.
- Keep map/provider attribution readable in the application and carry the
  applicable credits into screenshots, reports, downloads and offline packages.
  A GitHub acknowledgment alone does not satisfy every display requirement.
- Record product/edition, source URL, creator, actual access date, license
  version and modifications alongside reused data or media. Preserve restrictions
  already recorded in source descriptors and curated-release exclusions.
- Check the exact release's transitive dependency notices, imagery/service
  permissions, footage obligations and model-weight license before distribution.
  This inventory covers identified sources and tools; a complete release and
  deployed-display compliance audit has not been performed.
