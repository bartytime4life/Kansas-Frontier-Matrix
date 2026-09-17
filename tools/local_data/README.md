<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-local-data-readme
title: Local PC data tools
type: readme
version: v1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-09-17
updated: 2026-09-17
policy_label: public
owning_root: tools/
responsibility: Describe bounded workstation inspection and offline quarantine capture tools.
truth_posture: Branch-local implementation; hosted validation and native host acceptance remain separate.
[/KFM_META_BLOCK_V2] -->

# Local PC data tools

These Python 3 standard-library tools prepare a local checkout and preserve
explicitly selected, already downloaded files in a private external QUARANTINE
store. They do not download, interpret, extract, normalize, activate, promote,
publish, or serve data. See the [local-PC runbook](../../docs/runbooks/local-pc-data-store.md)
for the complete setup and update sequence.

`tools/` owns the operator interface and checks. The existing
`connectors/local_upload/src/local_upload/fetch.py` owns bounded local-byte
capture. Placement follows accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and [Directory Rules](../../docs/doctrine/directory-rules.md), especially
DIR-EXEC-007, DIR-STORAGE-001 and source-first DIR-SOURCE-001. This helper does
not implement the connector's still-unimplemented source-admission gate.

## Commands

Run from the repository root. `--root` may be omitted when `KFM_DATA_ROOT` is set;
the store must be an absolute path outside and separate from the checkout.

```bash
python3 tools/local_data/doctor.py
python3 tools/local_data/manage.py init --root "$HOME/KFM-Data"
python3 tools/local_data/manage.py plan --root "$HOME/KFM-Data" --manifest configs/local/capture.json --downloads "$HOME/Downloads"
python3 tools/local_data/manage.py sync --root "$HOME/KFM-Data" --manifest configs/local/capture.json --downloads "$HOME/Downloads"
python3 tools/local_data/manage.py verify --root "$HOME/KFM-Data" --manifest configs/local/capture.json
```

`doctor` only inspects the checkout and local tool availability. It does not
install dependencies, start services, or fetch anything. `plan` also writes
nothing: it hashes explicit inputs and any existing destination objects, checks
metadata, and reports required space and proposed actions. `sync` does the same
preflight under an exclusive store lock before capturing missing objects.
`verify` checks stored bytes, immutable revision bindings, complete and
per-source manifest snapshots, and success receipts; it does not need downloads.

To calculate a checksum and size without manually transcribing them, describe
one explicit file and redirect the resulting manifest to a local config file:

```bash
python3 tools/local_data/manage.py describe \
  --downloads "$HOME/Downloads" --file maps/county.zip \
  --source-id provider --dataset-id county-boundaries --domain settlements-infrastructure \
  --version 2026-09-17 --source-uri https://example.org/county.zip \
  --media-type application/zip > configs/local/capture.json
```

Replace the illustrative source metadata with the actual provider. `describe`
reads one file without directory discovery. Its stdout is a complete manifest,
with unknown rights and sensitivity. `captured_at` defaults to the current UTC
time; `--captured-at` accepts an explicit whole-second UTC timestamp. This is
local capture time, not provider publication or observation time. The media type
defaults to `application/octet-stream` and remains a declaration, not validation.
`describe` errors go to stderr with a nonzero exit status; other commands return
their status JSON on stdout. Check the exit status before using redirected output.

## Storage and identity

`init` creates private directories for `data/raw`, `work`, `quarantine`,
`processed`, `catalog`, `triplets`, `receipts`, `proofs`, `registry`, and
`published`. Only QUARANTINE capture and process receipts are written by `sync`.
Maps, photographs, PDFs, archives and other files share the same byte-preserving
mechanism; domain and media type remain metadata.

| Relative path beneath the external root | Meaning |
|---|---|
| `data/quarantine/<source>/objects/sha256/<digest>/payload` | Opaque content-addressed bytes, shared by that source's dataset versions |
| `data/quarantine/<source>/versions/<dataset>/<version>/<path-hash>.json` | Immutable local capture binding for one declared relative input path |
| `data/quarantine/<source>/runs/<run>/manifest.json` | Canonical source-filtered manifest snapshot |
| `data/receipts/ingest/local-upload/<run>/manifest.json` | Full replayable canonical manifest |
| `data/receipts/ingest/local-upload/<source>/<run>/ingest-receipt.json` | Existing IngestReceipt shape, successful local capture only |
| `data/receipts/ingest/local-upload/<source>/<run>/attempts/<id>.json` | Partial attempt record when at least one verified object was available |

`run` is `local-` plus SHA-256 of canonical full-manifest bytes, including a final
newline. Items sort by source, dataset, version and relative path; object members
sort by key. The full snapshot can be passed directly to `verify` after a backup
restore. The per-source snapshot alone does not identify a multi-source run.

Revision bindings reject a changed declaration at the same source, dataset,
version and relative path. Use a new version for corrected bytes or metadata.
These bindings are local capture indexes, not source registry entries or
scientific facts. A version can contain multiple explicitly named files.

## Limits, safety and recovery

Defaults: 1,000 items, 8 GiB per file, 64 GiB per batch, 4 MiB manifest JSON, and
256 MiB free-space reserve. Use `--max-items`, `--max-file-bytes`,
`--max-total-bytes`, or `--min-free-bytes` to reduce the envelope. File and batch
limits may be explicitly raised to at most 1 TiB and 16 TiB; 1,000 items and
4 MiB input JSON remain hard caps. Payload streaming uses at most a 1 MiB chunk.
Disk checks conservatively reserve payload and metadata space; they cannot
prevent another process filling the disk during a capture.

Static symlinks, special files, traversal, Windows device/stream names,
duplicate JSON keys, nonfinite/fractional numbers, invalid identifiers and
undeclared fields fail closed. Input size and digest are checked again during
capture. New files use private temporary files, `fsync`, and an atomic hard-link
commit that never replaces an existing object. Filesystems lacking hard-link
support fail closed. POSIX-created directories use mode `0700` and files use
`0600`; a nonprivate store root is denied for initialization or synchronization.
Windows ACL equivalence and crash durability need native-host acceptance.

The operator must control the destination tree. Checks are not a sandbox against
another process replacing checked ancestors, changing files concurrently, or
maliciously modifying the store. The lock serializes cooperating `sync` writers;
it is not a host access-control mechanism. `init` should be run once before
starting writers. A killed writer can leave `.local-data.lock` and uncommitted
`.capture-*` temporary files: confirm that no writer remains, preserve any
material needed for diagnosis, and remove only those stale operational files
before retrying. The tool never steals a lock or deletes retained payloads.

Rerunning the same manifest rehashes existing objects and completes missing
snapshots/receipts without recopying valid bytes. Previous partial attempts stay
available. Existing corrupted payloads, revision bindings, snapshots or success
receipts are refused; they are never overwritten. A zero-capture failure prints
error JSON without inventing an IngestReceipt digest. A receipt's SUCCESS means
local capture processing only. Rights assertions, checksums and successful
copies do not establish source admission or public permission.

```bash
make local-data-check
```

The local tests exercise corruption, safe retry, multi-source backup restore,
resource limits, explicit-file selection and filesystem boundaries. They do not
prove a production downloader, governed map integration, or Windows acceptance.
