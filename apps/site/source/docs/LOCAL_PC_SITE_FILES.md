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
| `~/Projects/KFM-data` | Existing private lifecycle store: quarantine objects, source collections, manifest snapshots, and receipts. KFM's `tools/local_data/manage.py` owns its offline quarantine capture. This is not a web root. |
| `~/Projects/KFM-data/data/work/earth-engine` | Existing Earth Engine exports and display packages, relocated together with their identities and review labels preserved. A mixed working collection, not an admitted source or public assets. |
| `~/KFM-site-recovery` | Private source/version recovery copies outside either Git tree and outside deployed assets. |

## Prepare the folders

From a fresh extracted copy of this Site, use Node.js 22.13 or a later 22.x
release for the direct local Worker launcher:

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
files, or initialize `~/Projects/KFM-data`. Keep any archived Site sources in the recovery
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

Before preparing a new store, inspect the existing configuration and physical
data locations. The owner's workstation inventory on 2026-10-05 found an
existing lifecycle store at `~/Projects/KFM-data`; the 2026-10-06 organization
reused that home. Choose the tool and existing store described in its runbook.
Do not initialize a second empty store and treat it as a replacement for
existing data.

From the **KFM monorepo**, select the verified store. Run `init` only when
creating a genuinely new store:

```bash
cd "$HOME/Projects/Kansas-Frontier-Matrix"
python3 tools/local_data/doctor.py
export KFM_DATA_ROOT="$HOME/Projects/KFM-data"
# New stores only: python3 tools/local_data/manage.py init
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
them. Never copy `~/Projects/KFM-data`, downloaded raw files, or recovery archives into
the Site's `public/`, build output, or source tree. Only separately governed
and released artifacts belong in a public Site data path.

## Verified workstation organization — 2026-10-06

Eighteen Desktop reference folders now live below `~/KFM-references`; one
Desktop `KFM References` shortcut opens that home. Six inactive build/state/sync
recovery packages now live below `~/KFM-site-recovery`, retaining their original
names. The pre-v153 state backup is therefore
`~/KFM-site-recovery/KFM-Explorer-local-state-pre-v153-20261005`.

Earth Engine moved from `~/KFM-data/earth-engine` to the existing private store's
`data/work/earth-engine` subtree. The emptied `~/KFM-data` container was removed.
Preparation/assembly commands use the new location with `--data-root`; package
inspection/restoration uses its explicit `--package` path. Existing metadata,
manifests, and historical receipt bytes are unchanged. Live local R2 imagery,
actual D1/R2 state, the current Site alias/source, and active PRISM acquisition
were not moved. No service restart was needed.

The private catalog at
`~/Projects/KFM-data/data/catalog/KFM-LOCAL-DATA-CATALOG.md` links the full
SHA-256 inventories and reversible old-to-new mappings under
`data/receipts/local-organization/20261006T163401Z/`. All 49,749 files in the
25 moved directories were verified before and after. Check the receipt before
rollback; never overwrite newer files or infer cleanup permission from a clean
Git status. Unresolved checkouts and other chats' worktrees remain preserved.
