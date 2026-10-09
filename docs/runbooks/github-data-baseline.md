<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/github-data-baseline
title: Download the curated source-context baseline
type: runbook
version: v1
status: source-context-distribution; not-source-admission
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: public
current_path: docs/runbooks/github-data-baseline.md
owning_root: docs/
responsibility: Explicit, bounded download of curated GitHub Release assets into a new local directory
truth_posture: Manifest quantities describe a dated source snapshot; download verification does not establish source admission, map activation, or scientific acceptance
related:
  - ../installation.md
  - ../../tools/local_data/github_baseline.py
  - ../../tools/local_data/catalogs/github-baseline/baseline-manifest.json
  - ../../apps/site/source/scripts/earth-engine/restore-local-display.mjs
[/KFM_META_BLOCK_V2] -->

# Download the curated source-context baseline

The [curated-data-20261008 release](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases/tag/curated-data-20261008)
distributes selected provider data and prepared source context from the server.
The release's **Source code** archive contains the matching downloader and
manifest. The larger `.tar.gz` data assets are separate downloads; GitHub's
ordinary **Code → Download ZIP** does not include them. Use the source archive
attached to this release when the accompanying changes have not reached `main`.

The [baseline manifest](../../tools/local_data/catalogs/github-baseline/baseline-manifest.json)
records each dataset's source URLs, license and attribution, description, file
count, expanded bytes, archive bytes, SHA-256 and exact download URL. Its
`snapshot_utc` identifies the snapshot, not a promise of live provider freshness.
Each collection retains its own observation periods, revisions and limitations.
The exclusion inventory identifies holdings omitted from this distribution.
Backups, credentials, private application databases and runtime recovery state
are outside this baseline.

The distribution budget is **80,000,000,000 bytes (80 GB, about 74.51 GiB)**.
The publishing receipt accounts for existing GitHub storage and the transferred
assets. This is a ceiling, not a request to download that volume. Release assets
are each smaller than 1.8 GB. GitHub documents a limit of 1,000 assets per release,
each under 2 GiB; large binaries stay outside ordinary Git history. See
[GitHub release limits](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).

## Inspect before downloading

Python 3.11 or newer is sufficient. Run from the extracted source or repository
root. The default operation reads only the supplied local manifest: no network,
directory creation or data changes.

```bash
python3 tools/local_data/github_baseline.py \
  --manifest tools/local_data/catalogs/github-baseline/baseline-manifest.json
```

The JSON plan lists dataset IDs and provenance, compressed `download_bytes`,
`expanded_bytes`, file counts and `minimum_free_bytes`. The space estimate
includes downloaded archives, extracted files, the largest temporary reassembled
file and a small metadata allowance. Filesystem overhead can require more space.
Filter the plan with `--dataset DATASET_ID`; repeat the option for several IDs.

## Download selected collections

Choose a **new** output directory below an existing directory you own. The
POSIX installer rejects existing output paths, symlinked parents, and a parent
writable by other users. It requires an explicit selection (`--dataset` or
`--all`) and an explicit compressed-byte budget (`--max-bytes`). Replace the
example dataset ID and budget with the values you choose from the plan:

```bash
python3 tools/local_data/github_baseline.py download \
  --manifest tools/local_data/catalogs/github-baseline/baseline-manifest.json \
  --dataset DATASET_ID \
  --max-bytes 1000000000 \
  --directory "$HOME/KFM-baseline-20261008"
```

To select every packaged collection, use `--all` in place of `--dataset` and
choose a budget at least as large as the plan's `download_bytes`. The helper
rejects budgets above 80 GB. A budget is a maximum; only the declared selected
archive bytes are requested. Source URLs are retained for provenance and are
never contacted by this downloader.

Every archive must come from this repository's exact release URL. Only GitHub's
release-assets CDN redirects are accepted. The helper checks compressed sizes
and SHA-256, then inspects every archive before creating the output directory.
It rejects absolute paths, traversal, links, special files, duplicate file
paths, cross-dataset paths, unexpected expanded sizes and conflicting names.
Extraction uses exclusive file creation with private permissions.

Some original files exceed GitHub's per-asset size limit. Their `reassemble`
records specify ordered part paths and the complete original's size and SHA-256.
The helper rejoins them, verifies the original, and then removes only the part
copies it just extracted. Archive counts describe members before this step;
`installed_files` in the receipt describes the final payload count.

A successful run writes `baseline-install-receipt.json`, reports exact
downloaded and expanded bytes, and removes its temporary archive copies. If a
failure occurs after output creation, `.baseline-incomplete` remains. Preserve
that directory for inspection and use a new path for a later attempt. A failed
download or installation is not reported as complete, and there is no automatic
overwrite, resume, cleanup of existing data, or service restart.

## Use the downloaded data

GeoTIFFs, tables and source catalogues can be inspected with appropriate GIS,
database and analysis tools. The existing Explorer does not automatically read
an arbitrary baseline directory. The download does not initialize a governed
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

Read the exact set ID from the downloaded
`earth-engine-display/earth-engine-context/v1/active.json`; do not invent or
replace it. The tool requires the reviewed 2024 identity and verifies its
manifest, indexes and every tile. To deliberately restore into a **stopped**
local preview, add `--persist-to /absolute/path/to/local-state/v3/r2` after
reviewing the destination. It refuses a different existing active pointer and
conflicting immutable objects. Dependency setup is documented in
[installation](../installation.md). This is a separate local action and is never
run by the baseline downloader; hosted DB/R2 bindings and existing previews are
not modified by downloading the package.

## Verify the downloader

```bash
python3 -m unittest discover -s tests/local_data -p test_github_baseline.py -v
```

These tests use synthetic local archives and network responses. They cover
budget/selection holds, download integrity, unsafe paths and links, preservation
of existing output, and reconstruction of a split original. Passing tests do not
establish the scientific quality, completeness or provider-currentness of the
distributed source collections.
