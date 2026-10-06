<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/free-data-acquisition
title: Free data discovery, selection and bounded acquisition
type: runbook
version: v0.1
status: branch implementation; candidate-only
owners: ["@bartytime4life"]
created: 2026-10-06
updated: 2026-10-06
policy_label: repository-facing; candidate-only; no-release
owning_root: docs/
responsibility: Explain free-source metadata discovery, explicit payload selection, bounded local capture, and receipt limits.
truth_posture: CONFIRMED scoped local tests and captured metadata / NEEDS VERIFICATION source admission, independent review, and public acceptance.
[/KFM_META_BLOCK_V2] -->

# Free data discovery, selection and bounded acquisition

The owner-selected local temporary/replaceable cache limit is **500 GB =
500,000,000,000 bytes (about 465.7 GiB)**. Selected Kansas data is retained on the
local PC under `KFM_DATA_ROOT`; provider originals remain available remotely.
Earth Engine or Drive is used only for processing or temporary transfer when
needed. Reuse existing local holdings before selecting missing dates or reviewed
provider revisions. Source-hosted access, generated exports and captured local
bytes have separate provenance. The cache limit does not cap provider-hosted
data or authorize paying for storage. The operator chooses individual payloads
and amounts. No paid
subscription, requester-pays endpoint, paid fallback, account change, export
charge, or billing activation is performed by these commands.

## Ownership and boundaries

Placement follows accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and [Directory Rules](../doctrine/directory-rules.md) §§10.1, 11.4 and 12.3:
`tools/local_data/` owns operator commands; `configs/examples/` owns an example
read by `candidate_queue.py`; `tests/local_data/` owns focused checks; `docs/`
owns this runbook. The catalog example is a dated selection aid, not another
source registry. Existing `data/registry/sources/` records retain authority.

Use the already initialized, owner-private external `KFM_DATA_ROOT` described by
the [local store runbook](local-pc-data-store.md). Files under
`data/work/acquisition-cache/<job_id>/` are explicitly replaceable transport
working copies, not admitted originals. Provider metadata captures go to new
immutable candidate folders under `data/raw/`. Process receipts go under
`data/receipts/ingest/acquisition/`. None is a released public data interface.
The tools never scan or evict the rest of the local data store. The existing
offline local-upload manifest remains the separately reviewed path for verified
bytes to enter immutable QUARANTINE; acquisition does not promote them.

The generic acquisition worker requires an expected checksum before transfer.
A generated Earth Engine download without a provider-issued digest therefore
uses a separate protected candidate capture and review. Its post-download
SHA-256 and stored-byte readback prove capture integrity; they must not be
labeled verification against an upstream checksum. Do not weaken the generic
transport allowlist to accommodate temporary authenticated download URLs.

## Discover metadata and review all historical choices

Run from the repository root, with the existing physical data root selected:

```bash
export KFM_DATA_ROOT=/home/bartytime/Projects/KFM-data
python3 tools/local_data/candidate_queue.py
python3 tools/local_data/discover_3dep.py \
  --output-directory "$KFM_DATA_ROOT/data/raw/usgs-3dep-discovery-NEW-CAPTURE"
python3 tools/local_data/discover_water.py \
  --output-directory "$KFM_DATA_ROOT/data/raw/usgs-water-history-NEW-CAPTURE"
```

The offline queue contains Kansas and broader provider-extent options from
`configs/examples/acquisition-candidates.json`. Every entry stays blocked until
specific assets, byte limits and checksums are selected. Catalog temporal bounds
are not a claim that a query, download or gap analysis has occurred. `null` dates
remain unknown; do not fill them from filenames or station IDs.

3DEP discovery captures only the public `KS_` bucket prefix listing and each
selected EPT metadata document, with an aggregate 8 MiB metadata response limit.
It records whether that prefix listing was truncated. It does not establish that
all Kansas-overlapping projects use the `KS_` naming convention. EPT bounds are
in the provider's native CRS; never render them directly as longitude/latitude.
Year-like name tokens do not establish acquisition dates, and CRS codes alone
are not verified human-readable vertical-datum descriptions.

Water discovery captures only time-series metadata in the explicit Kansas
bounding rectangle. Border locations require separate state-membership checks.
It follows only same-endpoint, same-bounds pagination, bounded to four pages by
default and 8 MiB overall. `complete_for_query` is true only when no next page
remains. `begin`/`end` are period envelopes; `gaps_verified` remains false because
the observations were not downloaded. A retained provider `data_gap_interval`
does not prove an absence of actual gaps.

## Select exact bytes, plan offline, then acquire

A payload manifest is a private operator input with this shape:

```json
{
  "schema_version": "kfm-acquisition-plan-v1",
  "jobs": [{
    "source_id": "usgs-3dep",
    "dataset_id": "selected-object",
    "label": "Selected public object",
    "source_url": "https://usgs-lidar-public.s3.amazonaws.com/SELECTED-PROJECT/SELECTED-OBJECT",
    "scope": "kansas",
    "expected_bytes": null,
    "approved_max_bytes": null,
    "sha256": null,
    "temporal_start": null,
    "temporal_end": null,
    "estimate_basis": "unknown",
    "rights_url": null
  }]
}
```

Replace the placeholder URL with the exact selected object; supply its expected
SHA-256 and either exact `expected_bytes` or an explicitly approved bounded
`approved_max_bytes`. Unknown-size jobs stay blocked before any transfer unless
the latter is set. A locally calculated checksum establishes byte identity, not
provider authenticity or scientific validity. If a provider does not supply an
independent checksum, document the origin of the expected digest; do not invent
one to unlock a job. Catalog queue URLs are metadata references, not automatically
downloadable payload manifests.

```bash
python3 tools/local_data/acquisition.py plan --manifest /absolute/private/selected.json
python3 tools/local_data/acquisition.py acquire \
  --manifest /absolute/private/selected.json --select EXACT_JOB_ID_FROM_PLAN
python3 tools/local_data/acquisition.py inventory
```

`plan` is offline and performs no writes. `acquire` requires one exact job ID;
it never downloads every candidate by default. Its fixed HTTPS host/path
allowlist contains public USGS EPT, National Map delivery, NOAA GHCN and USDA CDL
delivery routes. It denies credentials, queries, alternate ports, redirects,
encoded traversal and requester-pays buckets. It sends no API keys. Cloud
processing through Earth Engine or Copernicus is a separate operation.

The worker checks aggregate cache usage and free disk space before transfer and
enforces the selected bound while streaming. It counts all regular cache bytes,
including partial downloads, protected cache files, metadata and unknown files.
`temporary_bytes` and `replaceable_bytes` are subsets of `used_bytes`; do not add
them to that total. Protected cache bytes remain in aggregate usage but are not
in `replaceable_bytes`. `cache.inspected: false` means a catalog/plan projection,
not a measured empty cache.

Rerun the same selected job to resume. A nonempty partial requires an unchanged
strong ETag, conditional Range request and exact Content-Range validation. A
changed/weak/missing validator, ignored Range, altered size, quota response or
checksum failure blocks completion without overwriting existing payloads. No
automatic retry can switch providers, restart altered bytes or incur a charge.
The full retained file is SHA-256 checked before an atomic no-overwrite commit.
Concurrent workers are excluded by a process lock. A crash may leave a partial;
inventory reports the actual retained length and an interrupted state. A crash
in the no-overwrite hard-link commit can leave two links: the worker fails closed
and requires operator inspection instead of deleting either link automatically.

## Inspect, preserve and explicitly evict

```bash
python3 tools/local_data/acquisition.py protect --select EXACT_JOB_ID
python3 tools/local_data/acquisition.py evict --select EXACT_JOB_ID
```

There is no automatic eviction. `protect` prevents subsequent tool eviction;
there is deliberately no unattended unprotect command. `evict` accepts only the
two worker-owned payload filenames of the selected registered job. Any unknown
cache file, symlink, hard link, unsafe permission, or protected job blocks it.
It preserves job metadata and prior immutable receipts. Original/raw/quarantine
files are outside its destination allowlist and cannot be eviction targets.

Receipts use `kfm-acquisition-inventory-v1`; `complete` means verified cached
bytes only. It grants no rights, source admission, review, release, promotion or
publication. An owner-only dashboard may explicitly import a saved receipt and
must show its capture time and saved-state nature. It is not a live worker feed;
the dashboard cannot execute arbitrary download URLs or browse internal paths.

## Costs, historical interpretation and validation

[Earth Engine](https://developers.google.com/earth-engine/guides/noncommercial_tiers)
requires verified noncommercial eligibility; Community currently provides 150
EECU-hours/month. Contributor needs a billing account, and other Google Cloud
services may charge even when Earth Engine access is unpaid. Do not assume KFM
entitlement or unlimited free storage. [Copernicus openEO](https://documentation.dataspace.copernicus.eu/APIs/openEO/credit_usage.html)
currently provides 10,000 monthly free credits; paid extensions are excluded.

[PRISM](https://developers.google.com/earth-engine/datasets/catalog/OREGONSTATE_PRISM_ANm)
offers 1895+ monthly context but warns against century-long trend calculations.
[JRC v1.5](https://global-surface-water.appspot.com/download) requires history
version joins and documents alignment/recurrence limitations.
[USGS EPT](https://registry.opendata.aws/usgs-lidar/) is a public, unsigned route;
the neighboring raw LAZ bucket is requester-pays and not selected.
[USGS water metadata](https://api.waterdata.usgs.gov/) supplies site-specific
periods; [legacy WaterServices retirement](https://waterdata.usgs.gov/blog/api-waterservices-decom)
is expected in early 2027. Catalog options retain their checked dates, scope and
limitations so future revisions can supersede them without rewriting history.

Run `python3 -m unittest tests.local_data.test_acquisition -v` for offline
resume, validator changes, checksum rejection, byte caps, quotas, lock exclusion,
protected originals, unsafe paths, metadata pagination and queue-state tests.
Run the existing local-data suite for compatibility. Tests use synthetic opaque
bytes, not live bulk downloads. Revert these operator additions to roll back
code; retain external metadata snapshots and receipts. Do not delete or relocate
the existing data store as part of code rollback.
