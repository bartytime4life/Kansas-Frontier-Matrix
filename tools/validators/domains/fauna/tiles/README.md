<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools/validators/domains/fauna/tiles/readme
title: Fauna Tile Validator Lane
type: validator-lane-readme
version: v1.0.0
status: proposed-inactive; one bounded executable
owners: OWNER_TBD — Fauna steward · Map/UI steward · Policy steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: tools/
policy_label: internal; fauna; tiles; validation; no-network
responsibility: Document the bounded inactive Fauna tile field-name validator lane without creating tile, evidence, policy-decision, review, release, or publication authority.
truth_posture: "CONFIRMED validator, synthetic fixtures, focused tests, and workflow definition; PROPOSED inactive field vocabulary; UNKNOWN production integration; NEEDS VERIFICATION human review and hosted CI"
[/KFM_META_BLOCK_V2] -->

# Fauna Tile Validator Lane

This lane contains repository validators for Fauna-specific tile candidates. It does not contain tile builders, tile bytes, renderer code, policy authority, release decisions, or published carriers.

## Confirmed executable

`validate_tile_field_allowlist.py` checks the inactive fixture profile at `policy/domains/fauna/tile_field_allowlist.yaml` and replays synthetic field-name cases from `fixtures/domains/fauna/layers/tile_field_allowlist_cases.json`.

It checks only closed policy shape, canonical field-name collections, required fixture fields, deny patterns, the relation between encoded properties and a candidate `LayerManifest` allowlist, and fixed-false authority declarations. It does not decode actual PMTiles/MVT/MLT artifacts, inspect values or geometry, verify tile size/accessibility/evidence resolution, or grant evidence, policy-decision, review, release, publication, or public-use authority.

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/fauna/tiles/validate_tile_field_allowlist.py \
  --fixtures
```

Production build-gate integration remains `HOLD` pending an approved production vocabulary, real manifest/build bindings, byte-level inspection, accessibility requirements, evidence resolution, and release/correction/rollback controls.
