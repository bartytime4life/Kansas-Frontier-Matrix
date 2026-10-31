# Local library coverage review — 2026-10-31

This records a private PC review. It does not establish the contents of the
GoDaddy database, deploy map layers, or transfer local data to the website.
The hosted application uses its own database. GitHub code deployment does not
import the PC's SQLite records or source files. See
[database and intake status](database-intake-status.md) for measurement scope.

## Verified scope

| Check | Result | Limit |
| --- | --- | --- |
| Imported catalog metadata | 2,711,226 present file records across 27 source groups | One record is an indexed file, not an observation; this is not a fresh read of every payload. |
| Receipted NOAA/IEM climate payloads | 2,685 files passed fresh SHA-256, gzip CRC and row-count checks | Detailed measurement flags come from the matching capture receipts; source quality flags and missing values remain significant. |
| PRISM acquisition catalog | All 457,815 grid records examined; completed raster paths checked for existence and nonzero regular-file size | Raster decoding was not repeated for the full collection. |
| TIGER selection | Component sets found and basic DBF/SHP/SHX consistency checked for 1,082 of 1,083 selected package names | The remaining name requires reconciliation; this is not a full topology or positional-accuracy check. |

All original imported catalog records remain unchanged. New assessment receipts
record the review separately. A catalog status of `review` therefore does not
mean that no later review evidence exists, and a source-policy lookup alone does
not approve every file from that source.

## TIGER address-feature reconciliation

The September 12 manifest and its 104-county ADDRFEAT bundle describe an earlier
McPherson County gap. The September 25 completion record reports recovery of
`tl_2025_20113_addrfeat.zip`; the imported archive contains its unpacked files.
All seven components exactly match the fresh October 31 Census download.

The new local bundle consolidates all 105 Kansas counties and contains 382,868
potential address-range features. It adds **zero new geographic coverage** to
the already-completed imported collection. These ranges are not verified
individual addresses. Retain Census attribution, the 2025 vintage and NAD83 CRS.

| Local artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `tl_2025_20113_addrfeat.zip` | 413,332 | `b66e48b9c867306d55066abdd7297075a53f933fcf692fa768d689bf32aa23d5` |
| `kfm_tiger2025_Kansas_105_counties_ADDRFEAT_verified_components.zip` | 35,685,486 | `4741823655ebe3d876732ea8f842d31e7b35b66a75ccd8825f97dfe25e6c9ddd` |

The bundle contains 735 verified components. The recovered county's 4,929
features and 16,543 vertices passed full structural checks. The other 104
counties passed component-hash and SHX/DBF count checks. The bundle packages
unpacked components; it is not the original delivery of nested source ZIPs.

Source: [Census 2025 ADDRFEAT archive](https://www2.census.gov/geo/tiger/TIGER2025/ADDRFEAT/).
Bulk source files and recovery artifacts remain outside the public repository.

## Open findings

- **Three empty PRISM rasters:** the 800 m `tdmean` daily rasters for April
  27–29, 1987 are zero bytes, although the source catalog marks their grids
  complete and retains source ZIP hashes and county statistics. Recovery and
  comparison with the saved source versions are pending. Do not infer raster
  availability from `status='complete'` alone.
- **PRISM acquisition backlog:** 96,498 grid records are only indexed and 136
  have error status. Two additional complete grids lack units. These categories
  explain the 96,636 grids excluded from the earlier SQL import. They are not
  all corrupt files, nor proof that the current provider lacks those dates.
- **TIGER AREAWATER reconciliation:** the component inventory did not find
  `tl_2025_20055_areawater` for Finney County. Check alternate names and the
  acquisition receipts before declaring a source-coverage gap or re-downloading.
- **Wind coverage:** the captured annual observation files stop at 2002.
  Daily summaries extend through September 23, 2026, with three legitimately
  empty year files. Later individual snapshots do not fill the entire missing
  observation history. Do not count summaries and detailed observations as
  independent coverage.
- **Backup scope:** the earlier SQL/export backup and restore passed. A backup
  covering the new bundle and these review receipts has not yet been verified.

No unresolved gap should be silently filled with zeros, inferred geometry, a
different model version, or an older snapshot relabeled as current.

## Repeatable checks and evidence

The private review run retains `audit-catalog.py`,
`verify-receipted-climate.py`, `check-coverage.py`, and their JSON receipts.
The catalog metadata stream has SHA-256
`a56263e3ed198fc3710f56eba2668cb1da3d21298f22eaece9f3a274d2d4f0cc`.
That digest identifies the reviewed metadata stream, not the SQLite file bytes.

Reproduce the PRISM status split on a checkpointed read-only snapshot:

```sh
sqlite3 -readonly /path/to/PRISM/Kansas/catalog.sqlite \
  'SELECT status, count(*) FROM grids GROUP BY status;'
sqlite3 -readonly /path/to/PRISM/Kansas/catalog.sqlite \
  "SELECT path, tif_path FROM grids WHERE status='complete' AND (unit IS NULL OR unit='');"
```

Resolve every completed `tif_path` against that same PRISM root and check the
actual file; the status query alone cannot detect empty rasters. For TIGER,
reconcile `source_manifest.json` with `local_completion_2026-09-25.json` and the
current unpacked components rather than treating the old bundle filename as
the final coverage inventory. Check each DBF record count against SHX entries
and the SHP/SHX declared file lengths.

For the locally generated bundle, verify the recorded digest and archive CRC:

```sh
sha256sum /path/to/kfm_tiger2025_Kansas_105_counties_ADDRFEAT_verified_components.zip
python3 -m zipfile -t /path/to/kfm_tiger2025_Kansas_105_counties_ADDRFEAT_verified_components.zip
```

Fresh recovery results must be added as dated evidence. This record deliberately
does not claim that every source file was approved, every gap was resolved, or
the local data now powers the hosted website.
