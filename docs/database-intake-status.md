# Database and intake status

Open `/data-status` from the Explorer's Sources panel or `/pipelines`.

The hosted SQL card makes one fixed, read-only metadata query through the app's
existing database connection policy. Concurrent checks share the result and it
is cached for 60 seconds. No table names, records, connection addresses or
credentials are returned. Missing configuration, denied metadata access and
malformed measurements remain unknown.

Table/index allocation and row totals are estimates for tables visible to the
configured account. They exclude shared tablespace free space, logs, backups and
other hosting files. MySQL documents those limits in its
[TABLES metadata reference](https://dev.mysql.com/doc/refman/8.4/en/information-schema-tables-table.html).
The 85 GB decimal planning ceiling does not establish provider quota, enforce a
write limit, or authorize another import. The capture archive retains its
separate 80 GB configured limit; its bytes overlap the database and must not be
added to the SQL estimate.

The hosted intake section explains source review, validation and retry holds.
Retry eligibility is not a promise that a worker is running. Three failed
attempts exhaust the same capture; publication still requires approved release.

## Private PC report

The website does not contact visitor loopback services or expose the operator PC.
Generate a small status report on that PC, then use **Open local status report**:

```sh
node scripts/pc-pipeline/data-status.mjs \
  --intake /path/to/data/work/intake/index.sqlite \
  --catalog /path/to/data/work/intake/index.sqlite \
  --catalog /path/to/observations.sqlite \
  --output /private/path/data-status.json
```

List each catalog to be measured, up to 32. The tool reads SQLite file sizes and
existing journal/shared-memory sidecars, deduplicates catalog files by filesystem
identity, and queries the intake index read-only. It does not load source rows,
modify databases, scan unlisted directories, or publish anything. A missing or
invalid selected catalog makes the whole SQL total unknown instead of presenting
a partial sum as complete. Exports, backups and unselected databases are excluded.
Live files may change after measurement; quiesce writers for a stable inventory.

Reports contain timestamps, totals and fixed review categories. File paths,
dataset records and arbitrary decision text are excluded. Unknown hold details
are grouped under “Other”; one file can have several holds. Local review does
not imply public-release approval. The output path must be new and is created
with owner-only permissions. Keep real reports out of Git.

Opening a report checks its format and internal totals, with a 64 KiB file limit.
The browser retains it only in page memory and sends no upload. The displayed
date belongs to the supplied report; opening it does not refresh the PC or
authenticate its contents. Reloading or clearing the report removes it.

The [October 31 local library review](library-coverage-review-20261031.md)
records the scope of completed checks, the TIGER bundle reconciliation, and
remaining coverage gaps. Those local findings do not describe the hosted
database's contents or establish a live connection between the two stores.
