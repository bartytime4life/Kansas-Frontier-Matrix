# NHDPlus HR Network Revision Fixture Comparator

This child lane compares two frozen synthetic NHDPlus HR network snapshots and emits a deterministic review signal for COMID inventory, linear-reference, HUC12-assignment, and geometry-summary changes.

```bash
python tools/ingest/hydrology_watch/nhdplus_network_revision.py \
  tests/ingest/hydrology_watch/fixtures/nhdplus_network_revision/prior.json \
  tests/ingest/hydrology_watch/fixtures/nhdplus_network_revision/current_unchanged.json
```

The comparator is no-network and read-only. It does not fetch USGS data, recompute a crosswalk, write lifecycle state, issue hydrologic guidance, create evidence or policy authority, promote, release, or publish.
