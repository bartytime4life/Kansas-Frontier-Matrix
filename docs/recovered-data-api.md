# Recovered public record API

The owner authorized use of all recovered public datasets on 2026-11-03. This
extends the existing signed, read-only local-data service with
`recovered-observations` and `recovered-bulk`. It does not create arbitrary SQL,
table-name, filesystem or database-write endpoints.

The committed `scripts/local-data/recovered-catalog.json` allowlist covers all
189 domain tables in the inventoried observations and bulk databases. Each
collection fixes its database, table, selected columns and primary-key order.
Operational paths/build state and duplicate full-text-index implementation
tables are excluded. Public supporting tables, including storm fatalities and
institution/facility reference records, are included.

## Reading records

Send GET `/api/local-data/recovered-observations` or
`/api/local-data/recovered-bulk` with an allowlisted `collection`, `limit` (1–50,
default 20) and optional `after` copied unchanged from the previous response's
`nextCursor`. Unknown parameters and malformed cursors return 400.

Pages seek through the primary key. They do not count whole tables or apply
growing OFFSET scans. `total: null` means the full count was not requested;
`hasMore` and `nextCursor` describe continuation. Rows retain original values,
codes, nulls, dates, units and quality flags. File-backed records include their
source ID, URL and SHA-256. Import IDs are not observation dates, and overlapping
editions are not silently aggregated.

The existing signed request/reply, 1 MB response, read-only database and loopback
gateway boundaries are retained. Clients can retry oversized pages with a
smaller limit. A single unusually large record explicitly replaces long cells
with a `longField` marker. Read the exact text using the same endpoint with
`collection`, `record` (the row's ID), `field` and `start` (initially 0). The
`fieldChunk` response gives Unicode character offsets, `characters` and
`nextStart`; chunks are at most 32,768 characters. Page exports containing a
marker are not complete exports of that cell.

## Installation and rollback

Ship the matching hosted app, gateway and relay-worker route modules together.
Include `recovered.mjs` and `recovered-catalog.json` wherever `datasets.mjs` is
installed. Preserve existing keys and settings. Add optional gateway setting
`KFM_LOCAL_DATA_BULK_DB` pointing to the existing recovered `kfm-bulk.sqlite`.
The bulk endpoint reports unavailable when that database is not configured.
No migration, index creation, credential rotation or feed activation is needed.
The companion data-library interface consumes these endpoints; do not publish
that interface against an older gateway/worker allowlist.

After coordinated activation, verify signed responses from both stores,
continuation, empty collections, original provenance and outage behavior.
Rollback restores the paired previous app/gateway/worker code and environment;
it does not restore or delete database rows. This PR does not perform activation.

## Evidence and scope

Read-only first/next-page checks exercised all 189 collections: zero query
errors, overlapping identities or null cursor keys; 180 tables had rows and nine
were empty. These are bounded access checks, not full scientific qualification
or a claim that every raw file on the recovery volume has been imported.

The schema-only allowlist can be rebuilt with
`python3 scripts/local-data/build-recovered-catalog.py INVENTORY_JSON`, using a
fresh read-only inventory. Review changes before shipping: schema growth must
not silently expand the public query contract. Raw archives and audit artifacts
remain outside this app repository.
