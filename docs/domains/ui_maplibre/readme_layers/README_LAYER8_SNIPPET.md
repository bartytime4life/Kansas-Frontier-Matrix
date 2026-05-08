## Layer 8 Static Viewer Bundle

### CLI (link-existing-tile-package)
`python tools/soilgrids/soilgrids_viewer_bundle.py --tile-package-manifest ... --tile-package-receipt ... --tile-validation-report ... --tilejson ... --maplibre-style ... --release-manifest ... --publish-receipt ... --stac-item ... --viewer-root viewer_bundles --viewer-mode link-existing-tile-package --maplibre-js vendor/maplibre-gl.js --maplibre-css vendor/maplibre-gl.css`

### CLI (copy-pmtiles)
Add: `--viewer-mode copy-pmtiles --pmtiles-js vendor/pmtiles.js --pmtiles-path tile_packages/<id>/tiles.pmtiles`

### Note
This viewer is static and does not mutate authoritative COG, STAC, release, or tile package artifacts.
