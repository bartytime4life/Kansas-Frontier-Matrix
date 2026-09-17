<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/local-pc-data-store
title: Prepare a local PC and maintain its data store
type: runbook
version: v0.1
status: proposed; branch-review; quarantine-only
owners: ["@bartytime4life"]
created: 2026-09-17
updated: 2026-09-17
policy_label: public-documentation
owning_root: docs/
truth_posture: implementation and tests are branch evidence; independent acceptance pending
notes: ["Directory Rules ADR-0029 applies. No source admission, release, deployment, or publication authority."]
[/KFM_META_BLOCK_V2] -->

# Prepare a local PC and maintain its data store

This workflow prepares an Ubuntu/Linux checkout and a private external data
store for already downloaded maps, photos, documents, archives, and other files.
The local tools require Python 3.11 or newer and use only its standard library.
They perform offline quarantine capture and integrity checks. This is not a
complete offline Explorer installation or a production source-admission service.

## Download the code and check the PC

For a new checkout:

```bash
mkdir -p "$HOME/Projects"
git clone --branch agent/local-pc-data-store-20260917 --single-branch \
  https://github.com/bartytime4life/Kansas-Frontier-Matrix.git \
  "$HOME/Projects/Kansas-Frontier-Matrix"
cd "$HOME/Projects/Kansas-Frontier-Matrix"
python3 tools/local_data/doctor.py
```

This branch is the review candidate; use `main` after this change is separately
accepted and integrated. For an existing checkout, inspect `git status` and fetch
the candidate branch without discarding local work. A GitHub source ZIP also
works: extract the whole archive and run the same doctor from its root. A Python
wheel alone does not contain the repository tools, apps, or datasets.

The doctor's JSON reports essential interpreter/source checks and optional tool
locations. It does not install software, start services, access the network, or
claim that JavaScript dependencies or your storage are ready. Windows users can
use these Linux commands inside WSL; native Windows and WSL acceptance have not
been established by the Linux tests.

## Initialize storage outside Git

```bash
export KFM_DATA_ROOT="$HOME/KFM-data"
python3 tools/local_data/manage.py init
```

Choose an operator-controlled disk with enough free space. `--root /absolute/path`
overrides `KFM_DATA_ROOT`. The tools do not automatically load `.env`. Export the
variable again in new terminals or add that export to your own shell setup.
Do not point the root at a web directory, shared writable directory, or the Git
checkout. The tool rejects a root inside the checkout and unsafe path components.

All paths below are relative to `KFM_DATA_ROOT`:

| Physical path | Purpose and write boundary |
|---|---|
| `data/quarantine/<source_id>/objects/sha256/<digest>/payload` | Exact captured bytes; shared by captures from the same source with the same digest. |
| `data/quarantine/<source_id>/runs/<run_id>/manifest.json` | Immutable manifest snapshot for that source and run. |
| `data/quarantine/<source_id>/versions/<dataset_id>/<version>/` | Immutable per-file capture revision bindings; not a source registry. |
| `data/receipts/ingest/local-upload/<run_id>/manifest.json` | Complete canonical multi-source input; use this manifest for backup replay and verification. |
| `data/receipts/ingest/local-upload/<source_id>/<run_id>/ingest-receipt.json` | Local capture process record in the existing IngestReceipt shape. |
| `data/raw/`, `data/work/`, `data/processed/` | Prepared lifecycle destinations; this importer does not promote files into them. |
| `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/registry/`, `data/published/` | Prepared logical destinations for later governed consumers. Empty directories grant no authority. |

Maps, photos, and PDFs use the same source-first capture store. Their original
paths and media types remain in the manifest. Opaque `payload` filenames prevent
file extensions from implying safe execution or parsing. Never serve this whole
store with an HTTP file server or copy it into an app's public assets.

## Try one small synthetic capture

This example deliberately uses a 24-byte test file, not Kansas data. It proves
the local workflow before you point it at real downloads.

```bash
python3 tools/local_data/manage.py plan \
  --manifest configs/examples/local-data-manifest.json \
  --downloads fixtures/source/local_data
python3 tools/local_data/manage.py sync \
  --manifest configs/examples/local-data-manifest.json \
  --downloads fixtures/source/local_data
python3 tools/local_data/manage.py verify \
  --manifest configs/examples/local-data-manifest.json
```

`plan` is read-only. `sync` writes only selected, verified quarantine objects and
their metadata/receipts. `verify` checks those stored objects without needing the
downloads directory. Repeat `sync` with the same input to confirm reuse. A
nonzero exit means the operation failed; inspect its JSON reason before retrying.

## Add downloaded maps, pictures, and documents

Download only files you are entitled to possess using the provider's reviewed
download method, or copy your existing Drive/archive downloads to a private
directory such as `$HOME/Downloads/KFM`. The importer never signs in to a service,
follows a source URL, downloads a remote file, recursively crawls a folder,
extracts a ZIP, or executes imported content.

Use `python3 tools/local_data/manage.py describe --help` to make a one-file
manifest from an explicitly selected local file. The command computes size and
SHA-256, records the supplied source/dataset/version/reference/media metadata,
and leaves rights and sensitivity unknown. Save its JSON in ignored
`configs/local/` or another private location. Review those assertions before
capture. For several files, combine their item objects into one manifest with
`schema_version: "1"`; do not use a directory glob as an implicit import list.

For example, replace the names below with one real downloaded file and its
provider reference. The output file must be a new private manifest:

```bash
python3 tools/local_data/manage.py describe \
  --downloads "$HOME/Downloads/KFM" --file "maps/county-map.tif" \
  --source-id my-provider --dataset-id county-map --domain geology \
  --version capture-v1 --source-uri "file-ref:provider-download-record" \
  --media-type image/tiff > configs/local/county-map-v1.json
```

Without `--captured-at`, `describe` records its current execution time. Supply
the original download time explicitly when known. Check the command's exit
status; error JSON is not a usable manifest. A shell redirection writes the
selected output file even when the command fails, so keep older manifests intact.

The [manifest contract](../../contracts/source/local_data_manifest.md) explains
every field. Keep stable provider and dataset IDs. Keep license/rights evidence
and original download time; `captured_at` is not the map's historical date or a
sensor observation timestamp. A locally computed digest establishes byte identity
only. Compare against independently obtained provider checksums when available.
Signed URLs, credentials, personal paths, and private identifiers must stay out
of Git. Unknown rights or sensitivity never become public by default.

For a private manifest saved as `configs/local/my-downloads.json`:

```bash
python3 tools/local_data/manage.py plan \
  --manifest configs/local/my-downloads.json --downloads "$HOME/Downloads/KFM"
python3 tools/local_data/manage.py sync \
  --manifest configs/local/my-downloads.json --downloads "$HOME/Downloads/KFM"
python3 tools/local_data/manage.py verify --manifest configs/local/my-downloads.json
```

Default limits are 1,000 items, 8 GiB per file, 64 GiB per batch, a 4 MiB
manifest, and a 256 MiB free-space reserve. The command help exposes explicit
finite limits. Split large acquisitions into manageable manifests; reserve
extra space for normalization, tiles, database imports, and backups. The file
copy streams chunks, so memory use does not scale with the whole raster or ZIP.
The store filesystem must support same-directory hard links for atomic,
no-overwrite commits. Unsupported filesystems fail closed; do not assume a
FAT/exFAT removable drive can be used as the active store.

## Keep updates and historical backfill repeatable

1. Retain each reviewed manifest and its canonical stored snapshot. Record a new
   `version` when bytes or capture metadata change. Reusing a bound version/file
   identity with changed declarations is rejected.
2. Preview the new manifest. Synchronization reuses valid content hashes and
   preserves old versions. An upstream file disappearing never deletes local
   history. Existing corrupt objects are reported and never silently overwritten.
3. Sync, verify, and retain the process receipts. An interrupted batch can leave
   already verified quarantined captures; retry the same manifest to finish
   missing outputs. Never treat partial output as completed source admission.
4. For backfill, make one bounded manifest per provider/dataset/time partition.
   Keep source observation/valid-time coverage in the provider metadata. The
   existing `scripts/plan_backfill_window.py` separately validates time-window
   requests of at most 366 days; it is a no-write planner, not a downloader or
   scheduler. This change does not connect its processed-artifact locator to the
   quarantine store or imply a published version exists.
5. Re-download and compare revised provider artifacts explicitly. There is no
   implicit remote monitoring, deletion, source activation, or scheduling.

Update code separately from bytes. On a clean checkout of the accepted branch,
`git pull --ff-only` preserves history and refuses divergent source updates.
Inspect the changes, run the doctor and changed-area checks, then verify a saved
manifest. Do not use `git reset --hard` or `git clean` to repair a data problem.
The external data root stays in place through code updates or a replacement ZIP.

## Backup, restore, and recovery

Back up the complete external root, including quarantined bytes, manifest
snapshots, version bindings, and receipts, while capture is idle. Keep another
copy on a separate device. Configure private filesystem access and encryption
appropriate to the source; this tool does not provide encryption, ACL policy,
malware scanning, or multi-user isolation.

Restore into a separate private root and run `verify --root <restored-root>` with
each retained manifest before adopting the restored store. A source deletion or
corrected dataset does not authorize garbage collection: check retention,
rights, and legal holds first. Do not delete a stale lock until you have
established that no writer is active. Prefer local disks; network filesystems
and hostile concurrent modification are outside the accepted operating scope.

Rollback of unintegrated code means abandoning the branch. After separately
approved integration, revert the focused change without deleting captured data.
An older program may not understand a newer manifest version; keep exact source
revision and manifest together. Recovery is not a release or publication action.

## What remains before the local map is production-ready

The GitHub source checkout and the hosted Explorer have separate histories.
Session readback found Explorer v44 at source `b893683c33ef1a85d75f88db58e27e361c7e01a0`;
this local-store change does not establish byte parity, replace the Site, or
connect its browser to your PC's filesystem. Compose remains a placeholder.

The next integration work is source-by-source: registered descriptor and rights
review; admitted RAW capture; normalization and spatial/temporal validation;
catalog/layer entries; evidence/proof and release closure; governed API and
MapLibre loading; correction/rollback verification. PMTiles, COG, GeoParquet,
imagery, and photos require their respective reviewed adapters. Sensitive exact
locations and unclear rights stay held. No store path alone makes a layer visible.

## Validation and placement

Run `make local-data-check` after installing the repository's declared test
dependencies. The dedicated `local-data-store` workflow runs the same target on
relevant pull requests, main changes, and the exact candidate branch. It has a
read-only token, uses temporary test directories, and transfers no provider data.
Hosted results and independent acceptance remain separate from local test output.

Accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and
[Directory Rules](../doctrine/directory-rules.md) §§10.1, 11.4, and 12.3 place
operators in `tools/`, source capture in `connectors/`, examples in `configs/`,
meaning in `contracts/`, shape in `schemas/`, tests/fixtures in their own roots,
and this guide in `docs/runbooks/`. Physical disk separation preserves logical
lifecycle ownership; it creates no new registry or release authority.
