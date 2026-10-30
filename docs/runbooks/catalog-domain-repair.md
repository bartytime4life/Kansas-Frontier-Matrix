# Bounded catalog domain correction

Intake domains are discovery hints, not verified topic, provenance or Kansas
coverage. A short keyword inside a station identifier or place name can mislead
the catalog: `US1SCDL0004` previously matched agriculture (`cdl`), `KGSO`
matched geology (`kgs`), and `Wellington` matched geology (`well`).

The classifier bounds the affected acronyms and ordinary geological terms to
tokens (underscores count as separators). Recognized NOAA GHCNDEX and ASOS
archive path families provide an atmosphere hint; a declared domain still wins.
Classifier version 2 is independent of the payload analyzer version. Normal
intake refreshes old cached hints without rereading payloads, then recomputes
placement recommendations through the existing routing rules.

## Repair an existing catalog copy

Use `tools.local_data.catalog_reclassify` on the private catalog **copy**, never
the original imported archive index. Select explicit IDs using a bounded indexed
query. Planning is read only, limited to 1,000 unique IDs and 24 MiB of metadata.
It refuses changes that would resolve/unresolve a domain, cross a sensitive
domain boundary, or change review flags; those require separate analysis.

```sh
python3 -m tools.local_data.catalog_reclassify --database /absolute/catalog.sqlite \
  plan --ids /absolute/selected-ids.json --output /absolute/repair-plan.json
```

Inspect the complete before/after rows and retain the reported plan SHA-256.
Before applying, pause scheduled writers, acquire the PC's shared pipeline lock,
and stop the catalog service (its summary is cached). Save runtime-file preimages
before installing the classifier. Keep the service/timer restart in an exit trap.

```sh
python3 -m tools.local_data.catalog_reclassify --database /absolute/catalog.sqlite \
  apply --plan /absolute/repair-plan.json --sha256 EXACT_PLAN_SHA256 \
  --recovery /absolute/private-recovery/repair-journal.json
```

The helper replays the plan against its classifier and compares every current
row with its complete preimage inside a SQLite write transaction. Only `domain`,
`profile_json` and `decision_json` change. The profile changes only classification
hints; the decision changes only its domain and recommended staging path. Holds,
authority, status, dates, byte hashes, spatial metadata, analysis version/time,
RTree entries, source declarations and applied-placement history stay intact.
No files are staged and no raw payloads are opened.

An exclusive, fsynced recovery journal is written before commit. A conflict or
journal failure rolls back the entire transaction. The journal contains exact
before/after rows, not a full database backup. It may exist after an interrupted
or rolled-back attempt; verify row state before retrying. Restoration also
requires exact current postimages, so it cannot erase later changes:

```sh
python3 -m tools.local_data.catalog_reclassify --database /absolute/catalog.sqlite \
  restore --plan /absolute/private-recovery/repair-journal.json \
  --sha256 EXACT_PLAN_SHA256 --recovery /absolute/private-recovery/restore-journal.json
```

Keep the same helper/classifier version for recovery. Restart the catalog, verify
affected IDs through its authenticated API, and compare preserved review holds.
Resume timers. Record selection counts separately from changed counts; this
bounded repair does not certify or reclassify the rest of the archive.
