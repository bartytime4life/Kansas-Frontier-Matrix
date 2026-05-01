# Governed Tile Release Publisher

This slice publishes **render artifacts only** from an approved candidate while keeping governance objects separate.

- Deterministic identity: `kfm:spec_hash`.
- Generated outputs: TileJSON, ReleaseManifest, STAC catalog record, and public registry entry.
- Outcome enum: `PUBLISHABLE | BLOCKED | NEEDS_RECEIPT | ERROR`.
- Blocking checks enforce public policy/sensitivity, approved+released states, role/path bans, receipt linkage, and PMTiles metadata `spec_hash` match.
- No-network operation: local fixture candidate + local PMTiles metadata fixture.

CLI:

```bash
node scripts/publish_kfm_tile_layer.ts \
  tests/fixtures/tile_release/valid/candidate.json \
  tests/fixtures/tile_release/valid/pmtiles_metadata.json \
  .tmp/tile_release
```
