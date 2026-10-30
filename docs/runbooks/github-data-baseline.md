<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/github-data-baseline
title: Curated source-context baseline (retired GitHub archives)
type: runbook
version: v1
status: archive-retired; not-source-admission
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-30
policy_label: public
current_path: docs/runbooks/github-data-baseline.md
owning_root: docs/
responsibility: Preserve provenance and explain retirement of curated GitHub Release archives
truth_posture: Manifest quantities describe a historical source snapshot; release archives are retired; existing install receipts do not establish source admission, map activation, or scientific acceptance
related:
  - ../installation.md
  - ../../tools/local_data/github_baseline.py
  - ../../tools/local_data/catalogs/github-baseline/baseline-manifest.json
  - ../../apps/site/source/scripts/earth-engine/restore-local-display.mjs
[/KFM_META_BLOCK_V2] -->

# Curated source-context baseline (retired GitHub archives)

The data archives for the [curated-data-20261008 release](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases/tag/curated-data-20261008) have been retired from GitHub. The release retains its manifest, checksums and transfer report for historical provenance. The URLs and archive sizes in these documents describe the original release and do not indicate that the archives remain downloadable. A private local copy may exist for its operator; it is not a public distribution endpoint.

The [baseline manifest](../../tools/local_data/catalogs/github-baseline/baseline-manifest.json) records each dataset's original source URLs, license and attribution, file count, sizes and checksums. Its snapshot date is not a promise of current provider data. Backups, credentials, private application databases and runtime recovery state were outside this baseline.

The downloader's offline plan remains available to inspect the historical inventory. It reports `archive_availability: retired` for this release and refuses a download before accessing the network or creating a directory:

```bash
python3 tools/local_data/github_baseline.py \
  --manifest tools/local_data/catalogs/github-baseline/baseline-manifest.json
```

The recorded `download_bytes` and space estimates are historical quantities, not a current download offer. To obtain data independently, review the original provider sources and their terms; the release metadata alone does not restore the data.

## Use an existing local copy

GeoTIFFs, tables and source catalogues can be inspected with appropriate GIS,
database and analysis tools. The existing Explorer does not automatically read
an arbitrary baseline directory. An existing local copy does not initialize a governed
store, import a database, alter a source registry, or activate map layers.
Distribution status remains `source-context-unadmitted`.

The Earth Engine display collection preserves the existing
`earth-engine-context/v1/` layout. Its separately reviewed 2024 package has an
existing local-preview restoration tool. From `apps/site/source`, first verify
the package without writing runtime state:

```bash
node scripts/earth-engine/restore-local-display.mjs \
  --package "$HOME/KFM-baseline-20261008/earth-engine-display" \
  --reviewed-set EXACT_SET_ID_FROM_ACTIVE_JSON
```

Read the exact set ID from the local
`earth-engine-display/earth-engine-context/v1/active.json`; do not invent or
replace it. The tool requires the reviewed 2024 identity and verifies its
manifest, indexes and every tile. To deliberately restore into a **stopped**
local preview, add `--persist-to /absolute/path/to/local-state/v3/r2` after
reviewing the destination. It refuses a different existing active pointer and
conflicting immutable objects. Dependency setup is documented in
[installation](../installation.md). This is a separate local action and is never
run by the baseline downloader; hosted DB/R2 bindings and existing previews are
not modified by storing the package.

## Verify the downloader

```bash
python3 -m unittest discover -s tests/local_data -p test_github_baseline.py -v
```

These tests use synthetic local archives and network responses. They cover
budget/selection holds, download integrity, unsafe paths and links, preservation
of existing output, and reconstruction of a split original. Passing tests do not
establish the scientific quality, completeness or provider-currentness of the
historical source collections.
