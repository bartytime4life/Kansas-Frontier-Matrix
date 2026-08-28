<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-ingest-cdl-watch-readme
title: tests/ingest/cdl_watch README
type: README
version: v0.1
status: draft; bounded executable coverage
owners: OWNER_TBD - tooling QA; Agriculture source steward
created: 2026-08-02
updated: 2026-08-02
policy_label: repository-facing; fixture-only; no-network; watcher-non-publisher
owning_root: tests/
responsibility: Prove the frozen synthetic CDL watcher comparison profile, exact finite outcomes, parser bounds, deterministic reports, safe output handling, and no-network posture.
related:
  - ../README.md
  - ../../../tools/ingest/cdl_watch/README.md
  - ../../../docs/sources/catalog/usda/usda-nass-cdl.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CDL watcher fixture proof

The suite compares seven closed synthetic sidecar pairs:

| Case | Expected result |
|---|---|
| `no_material_change` | `NO_MATERIAL_CHANGE` |
| `metadata_change` | `NO_MATERIAL_CHANGE` with a source-metadata diagnostic |
| `below_threshold` | `NO_MATERIAL_CHANGE` with a below-threshold diagnostic |
| `relative_threshold` | `PROPOSED_WORK_RECORD` at the inclusive relative boundary |
| `absolute_threshold` | `PROPOSED_WORK_RECORD` at the inclusive absolute boundary |
| `classmap_drift` | blocking `CLASSMAP_DRIFT` |
| `geometry_drift` | blocking `GEOMETRY_DRIFT` |

All payloads use the non-real county sentinel `99999`, fixture-only source
references, integer square metres, and integer parts-per-million thresholds.
The profile deliberately does not choose a live CDL descriptor, county,
classmap, geometry release, or policy threshold.

Metadata and CDL-year changes remain diagnostics. Only a relative or absolute
histogram threshold reached under the unchanged caller-supplied profile returns
`PROPOSED_WORK_RECORD`. Sidecars with zero covered area, noncanonical class IDs,
or future-relative chronology fail validation.

Run with:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest tests.ingest.cdl_watch.test_cdl_watch --verbose
```

A pass proves only the frozen helper profile. It does not admit, download,
reprocess, promote, sign, release, or publish CDL material.

[Back to top](#top)
