.
├── README.md
├── LICENSE
├── package.json
├── package-lock.json
├── pyproject.toml
├── Makefile
├── requirements.txt
├── .gitignore
├── .gitattributes
├── .editorconfig
├── .pre-commit-config.yaml
├── .github/
│   ├── workflows/
│   │   ├── site.yml
│   │   ├── roadmap.yml                  # ⟵ Roadmap → Issues/Milestones sync (Actions)
│   │   └── stac-validate.yml            # ⟵ STAC validation job (reproducibility)
│   ├── roadmap/
│   │   └── roadmap.yaml                 # ⟵ Declarative roadmap (Milestones/Issues)
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── data_addition.md
│   │   └── experiment_report.md
│   └── PULL_REQUEST_TEMPLATE.md
├── scripts/
│   ├── sync-roadmap.js                  # ⟵ GitHub sync script (uses js-yaml, actions/*)
│   ├── fetch.py
│   ├── make_cog.py
│   ├── make_hillshade.py
│   ├── write_meta.py
│   ├── make_stac.py
│   ├── validate_sources.py
│   └── validate_stac.py
├── src/
│   └── kansas_geo_timeline/
│       ├── __init__.py
│       ├── cli.py
│       ├── utils.py
│       ├── templates/
│       │   └── app.config.json.j2
│       └── schemas/
│           └── stac_item.schema.json
├── data/
│   ├── README.md
│   ├── .gitignore
│   ├── .gitattributes
│   ├── sources/
│   │   ├── ks_dem.json
│   │   ├── usgs_historic_topo.json
│   │   ├── ks_treaties.json
│   │   ├── ks_railroads.json
│   │   └── schema.source.json
│   ├── cogs/
│   │   ├── dem/
│   │   │   ├── ks_1m_dem_2018_2020.tif
│   │   │   ├── ks_1m_dem_2018_2020.meta.json
│   │   │   └── ks_1m_dem_2018_2020.sha256
│   │   ├── hillshade/
│   │   │   ├── ks_hillshade_2018_2020.tif
│   │   │   └── ks_hillshade_2018_2020.meta.json
│   │   ├── overlays/
│   │   │   ├── usgs_topo_larned_1894.tif
│   │   │   └── usgs_topo_larned_1894.meta.json
│   │   └── landcover/
│   │       └── ks_landcover_1936_dustbowl.tif
│   ├── processed/
│   │   ├── dem/
│   │   │   ├── ks_1m_dem.tif
│   │   │   ├── ks_1m_hillshade.tif
│   │   │   └── _meta.json
│   │   ├── overlays/
│   │   │   ├── usgs_1894_larned.tif
│   │   │   └── _meta.json
│   │   └── vectors/
│   │       ├── treaties.geojson
│   │       ├── railroads_1900.geojson
│   │       └── _meta.json
│   └── stac/
│       ├── collections/
│       │   ├── elevation.json
│       │   ├── historic_topo.json
│       │   └── vectors.json
│       └── items/
│           ├── ks_1m_dem.json
│           ├── ks_1m_hillshade.json
│           ├── usgs_1894_larned.json
│           ├── treaties_1854.json
│           └── railroads_1900.json
├── earth/
│   ├── Kansas_Terrain.kmz
│   ├── doc.kml
│   └── networklinks/
│       ├── ks_1m_hillshade.kml
│       └── usgs_topo_1894.kml
├── web/
│   ├── index.html
│   ├── app.js
│   ├── app.css
│   ├── app.config.json
│   ├── layers.json
│   └── assets/
│       ├── favicon.svg
│       └── logo.png
├── docker/
│   ├── Dockerfile
│   └── compose.yaml
├── mcp/
│   ├── experiments/
│   │   └── EXP-0001_dem_hillshade.md
│   ├── sops/
│   │   ├── georeference_map.md
│   │   ├── add_dataset.md
│   │   └── publish_pages.md
│   ├── model_cards/
│   │   └── nlp_geoparse.md
│   └── glossary.md
└── tests/
    ├── test_stac.py
    ├── test_sources.py
    └── test_cli.py
