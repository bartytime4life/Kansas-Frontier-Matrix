# Site files on an Ubuntu PC

Use separate homes for application source, incoming files, governed data, and
recovery copies. The standalone Explorer Site is a different Git project from
Kansas Frontier Matrix (KFM). This guide prepares local folders; it does not
move, upload, import, or publish your existing PC files.

| Local path | Owner and purpose |
| --- | --- |
| `~/Projects/Kansas-Frontier-Matrix` | KFM monorepo, code and documentation. Keep private datasets out of Git. |
| `~/Projects/KFM-Explorer-Site-<version>` | A new, separate checkout or extracted source archive of **this** Site. Never extract over an existing checkout. |
| `~/Downloads/KFM/<source-id>/<dataset-id>/` | Incoming provider files and their original filenames. Select individual files for private capture. |
| `~/KFM-references` | Private study books, architecture reports, and design references. Keep their original author/title and usage terms; they are not provider data or public Site assets. |
| `~/KFM-data` | Private quarantine objects, manifest snapshots, and receipts managed by KFM's `tools/local_data/manage.py`. This is not a web root. |
| `~/KFM-site-recovery` | Private source/version recovery copies outside either Git tree and outside deployed assets. |

## Prepare the folders

From a fresh extracted copy of this Site, with Node.js 22.13 or newer:

```bash
cd "$HOME/Projects/KFM-Explorer-Site-<version>"
node scripts/prepare-local-pc.mjs
node scripts/prepare-local-pc.mjs --apply
```

The first command inspects without writing. The second creates only
`~/Downloads/KFM`, `~/KFM-references`, and `~/KFM-site-recovery` with private permissions. It refuses
symlinked/non-directory path components, an existing target open to group or
other users, or a checkout bound to another Site project. For an existing
permissive target, inspect its contents and ownership, then use `chmod 700`
on that target before retrying. The command does not scan, move, or delete
files, or create `~/KFM-data`. Keep any archived Site sources in the recovery
folder, and record their version and digest separately.

The supplied *KFM MapLibre Operating Architecture (Revised)*,
*Pipeline Living Implementation Manual v0.3*, and
*Data Placement and Site Realization Decision (2026-09-10)* are architecture
references suitable for `~/KFM-references`, subject to their usage terms.
Their proposed implementation sequences and older repository pins are not
proof of the current Site's behavior; compare them against this checkout and
the current KFM repository before implementation. GIS books and API/design
books also belong in references. A
provider map, imagery file, observation, or historical scan is a candidate
source item for `~/Downloads/KFM/<source-id>/<dataset-id>/` instead. A PDF
extension alone cannot decide the role: a book and a scanned map may both be
PDFs. Record publisher, edition, acquisition time, and rights alongside each
item. Moving a file between these homes never admits or releases it.

Prepare KFM's independent data store from the **KFM monorepo** checkout:

```bash
cd "$HOME/Projects/Kansas-Frontier-Matrix"
python3 tools/local_data/doctor.py
export KFM_DATA_ROOT="$HOME/KFM-data"
python3 tools/local_data/manage.py init
```

Follow [KFM's local PC data-store runbook](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/runbooks/local-pc-data-store.md)
for private manifests and explicit `describe`, `plan`, `sync`, and `verify`
commands. Keep provider references, rights records, digests, and capture times;
do not infer release status from a successful copy. Back up the manifests,
receipts, and store together as described there. The download inbox and the
quarantine store are separate: removing an original downloaded file must be a
deliberate decision after verification and backup.

## What a Site source archive contains

The source archive contains application code, tests, documentation, static
assets, and `.openai/hosting.json`, which identifies this one Site project.
It does not contain your browser's device-local workspaces, downloaded data,
runtime credentials, D1 database rows, or R2 objects. The DB and BUCKET
bindings remain hosted with the Site; no local folder is a replacement for
them. Never copy `~/KFM-data`, downloaded raw files, or recovery archives into
the Site's `public/`, build output, or source tree. Only separately governed
and released artifacts belong in a public Site data path.
