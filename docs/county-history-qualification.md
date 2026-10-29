# Kansas county history: source qualification

Checked **2026-10-29**. **HOLD for public integration; offline structural qualification passed.** This is a development qualification record, not source admission, a release receipt, or a legal determination about KFM's intended use.

The next useful civic slice is a dated county-history layer. The actual Newberry Kansas archive was acquired and checked. Public redistribution rights, topology, interpretation and the modern continuation remain open. This change supplies an offline checker and tests; it adds no route, map layer, download endpoint, source approval or runtime dependency.

## Evidence and exact source

The [Newberry Kansas landing page](https://publications.newberry.org/ahcb/pages/Kansas.html) links the [Kansas archive](https://publications.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip), [FGDC metadata](https://publications.newberry.org/ahcb/documents/KS_Metadata2.htm), [county chronology](https://publications.newberry.org/ahcb/documents/KS_Individual_County_Chronologies.htm) and [bibliography](https://publications.newberry.org/ahcb/documents/KS_Bibliography.htm). The [Kansas Historical Society](https://www.kansashistory.gov/p/kansas-counties/11304) independently directs researchers to Newberry's map.

The archive was downloaded through the landing page in Chrome after the research fetcher returned HTTP 403. Browser download succeeded normally; no authentication, security warning or access control was bypassed. The original ZIP remains outside this Git tree. It is **2,131,373 bytes**, SHA-256:

```text
a233b4b3bcf3f3d7a52a4c18de76017f0d4f1f421086f95312df4c59a0aa5f02
```

The URL is mutable; the checker accepts only these exact bytes. A later revision must be separately qualified, never accepted by silently replacing the digest. Its JSON output inventories every member's size and SHA-256 without exporting geometry or source prose.

| Archive member, relative to `KS_AtlasHCB/` | SHA-256 |
| --- | --- |
| `KS_Historical_Counties/KS_Historical_Counties.shp` | `43026f03b3d1d5a8020c64aa5a17d765687277311e792208c78d3620e98c35b4` |
| `KS_Historical_Counties/KS_Historical_Counties.dbf` | `25730b7c0ed9bb300f6dd80e833e3c82f95e23b4e8e639fe263f7eeaaefa13ed` |
| `KS_Historical_Counties/KS_Historical_Counties.shx` | `ee4c1d945d526da5952e35170cbcfd639ae60ac259529d0e04aca34c01111619` |
| `KS_Historical_Counties/KS_Historical_Counties.prj` | `84cf5b9a3c1a444f83ac30ff76f8c5035990223027ba69b2f4d628388adcbd65` |
| `KS_Comprehensive_Database/KS_Comprehensive_Database.txt` | `1be56325d28ea82f512d09b8c005e09a20296b0cde6d5f478f9ed1e38bf832e6` |
| `zCreativeCommonsLicense/CreativeCommonsDeed.htm` | `720b2c4d33e2956392f15276468f179d7f24eebb9f8ab5d616680245d5448159` |

## Results on the acquired bytes

| Check | Observed result |
| --- | --- |
| Boundary versions / source institutional IDs | **341 / 143** |
| Geometry interval | **1804-10-01 through 2000-12-31**, inclusive |
| Comprehensive database | **945 rows:** 341 mapped versions, 588 event-only records, 16 undated name cross-references |
| Earliest chronology-only event | **1803-04-30**; this does not extend polygon coverage |
| Join from geometry to chronology | All 341 version keys match exactly, including dates |
| Date representations | DBF dates/numeric dates and chronology text/numeric dates agree |
| Versions without FIPS | **52**; no fabricated code was assigned |
| Source geometry | **343 parts / 186,807 vertices**; largest feature 35,052 vertices |
| Structure | Polygon types, finite geographic coordinates, closed nondegenerate rings, version uniqueness and same-institution non-overlap pass |
| Gaps between versions of the same institution | **8**, retained; no interpolation or forward fill |
| Source classification | All 341 `CNTY_TYPE` values are `County`, including records whose names/IDs describe non-county areas |
| Source projection | NAD83 geographic coordinates per bundled `.prj`; no WGS84 transformation performed |

The 16 undated rows are name cross-references such as an old spelling or renamed county, not missing-date boundary events. All 929 dated chronology rows have citations and change descriptions. Three event-only rows lack an institutional ID; any future event identity must therefore include the exact member digest and row locator rather than inventing a county.

Frame counts below are **features in the whole source**, not counts of organized Kansas counties, seats, legal authorities or modern Kansas-clipped polygons:

| Selected day | Features |
| --- | ---: |
| 1804-10-01 | 4 |
| 1854-05-30 | 2 |
| 1855-08-25 | 39 |
| 1861-01-29 | 50 |
| 1880-01-01 | 105 |
| 1900-01-01 | 106 |
| 2000-12-31 | 105 |

The extent is approximately **113.938°W–89.099°W, 33.004°N–48.151°N**. Historical predecessor jurisdictions extend well beyond present Kansas. Reusing the congressional adapter's modern-Kansas coordinate limits would incorrectly reject these records. Any display clipping must retain the original source geometry and record the transform.

| Institution ID | Gap start, included | Gap end, excluded |
| --- | --- | --- |
| `kss_clark` | 1883-02-22 | 1885-03-13 |
| `kss_grant` | 1883-02-22 | 1887-03-23 |
| `kss_gray` | 1883-02-22 | 1887-03-23 |
| `kss_kearny` | 1883-02-22 | 1887-03-23 |
| `kss_kiowa` | 1875-03-05 | 1886-02-11 |
| `kss_meade` | 1883-02-22 | 1885-03-13 |
| `kss_stanton` | 1883-02-22 | 1887-03-23 |
| `kss_stevens` | 1883-02-22 | 1886-02-20 |

These are observed version gaps, not automatically data defects. The next interpretation check must reconcile dissolution/re-creation and name history against the cited chronology. An empty interval for one institution does not mean the place had no other jurisdiction or inhabitants.

## Rights decision remains open

**CONFIRMED:** both the Kansas download page and bundled deed specify [CC BY-NC-SA 2.5](https://creativecommons.org/licenses/by-nc-sa/2.5/). The site's general footer refers to broader use without permission fees. Newberry's [current policy](https://www.newberry.org/policies) retains the user's responsibility to determine copyright and other restrictions. The general footer does not establish that the source-specific license was replaced.

**NEEDS VERIFICATION:** a recorded determination that KFM's intended display, transformations and downloadable derivatives comply with the applicable terms, or source-specific permission covering that use. Free access to KFM does not by itself settle that question. Keep the source separate from permissively licensed application code; do not relabel it MIT, CC0 or unrestricted government data. Mirroring or reformatting cannot remove the original terms.

The offline checker always returns `status: HOLD` and `releaseEligible: false`, even when its structural checks succeed. This is a bounded development safeguard, not a new policy authority. It has no approval flag. The existing governance process owns any future rights and release decision.

Prepared clarification text, **not sent**:

> We are evaluating the Kansas Atlas of Historical County Boundaries archive for Kansas Frontier Matrix, a public historical map. The Kansas page and ZIP contain CC BY-NC-SA 2.5, while the general footer links an open-access policy. Please confirm the current terms for this exact dataset, including public map display, reprojection/generalization and downloadable derived geometry, and whether commercial use has separately been authorized. Please identify required attribution, license notices and any scope limits. Archive SHA-256: a233b4b3bcf3f3d7a52a4c18de76017f0d4f1f421086f95312df4c59a0aa5f02.

## Proposed implementation after qualification

1. Preserve the raw ZIP and member identities through the existing RAW → WORK/QUARANTINE lifecycle. Use the existing source-registry and evidence responsibilities after an exact-tree placement review; this hosted checker creates neither.
2. Keep institutional identity (`ID`) separate from version identity (source digest plus ID/version/date interval). FIPS is optional. Give event-only and alias rows distinct roles; neither becomes an inferred polygon.
3. Convert each source interval to `[start, end + one day)`. Preserve the original dates. A day outside 1804-10-01–2000-12-31 must abstain for this geometry source. Treat post-2000 official vintages as a separately qualified continuation, not a carry-forward.
4. Resolve territory, non-county area, proposed/unrecognized jurisdiction and renamed/re-created county semantics from evidence. Do not use the catch-all `County` field alone. State/county administrative claims do not establish Indigenous sovereignty, land ownership or absence of communities.
5. Qualify datum conversion, topology and any display simplification before rendering. Preserve correction lineage and unmapped chronology events. Reuse the existing map/calendar/source drawer only after a bounded adapter exists and the rights/review gates are met.
6. Start the future UI with a selected date, explicit reconstruction attribution, source details and a keyboard list. Then-versus-now comparison needs a separately dated modern source. No officeholder, election-result or population crosswalk is inferred by this slice.

## Reproduce the checks

Use a separate development Python environment with **pyshp 2.3.1**. This is an offline-tool dependency, not a hosted application dependency. The unit tests use only the Python standard library. The acquisition step is intentional and external to the checker.

```sh
python3 -m unittest discover -s tests -p test_county_history_qualification.py -v
python3 scripts/qualify-county-history.py /absolute/path/to/KS_AtlasHCB.zip
```

In this session the package installer could not resolve pyshp. The exact [official 2.3.1 source module](https://github.com/GeospatialPython/pyshp/blob/2.3.1/shapefile.py) was retrieved through GitHub into a temporary dependency directory, outside the repository. Its SHA-256 is `9c749d73e31cc332e4683130a808258b407d2ba8cf33a5e1d5ea190c0eaae73f`. Running the checker with that directory on `PYTHONPATH` passed on the acquired ZIP. No third-party module is vendored by this change.

**Passed:** 13 synthetic regression tests and the real-archive structural qualification. Tests cover inclusive end dates, gaps, earlier event-only history, aliases, missing FIPS, overlapping identity, malformed dates/geometry, digest rejection, symlink rejection and bounded ZIP handling. An initial run correctly exposed a distinction missed by the first draft: the chronology begins in 1803 while polygon coverage begins in 1804. The checker now keeps those scopes separate and tests the distinction.

**Not established:** polygon topology or overlap between different institutions, independent verification of every legal boundary, provider-declared text encoding (CP1252 was used successfully), datum-transform accuracy, publication rights, full application tests, independent security review, browser map performance, or release readiness. The JSON output is deterministic qualification evidence, not a governed release proof. Exit zero means checks ran successfully; it does not change HOLD.

## Congressional and hosted status

[PR #5553](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5553) is **merged**, verified this session. The hosted branch subsequently reached `cdbe5d7b66ba431f1bb373201c316fe7048a4509` (tree `fe0a3c737704cae4fad46bcf3949906fc90128cf`). Its source tree was reconstructed and checked before this patch.

A read-only Chrome visit to [the public site](https://kansasfrontiermatrix.com/) still showed the earlier “Civic map” category and its county-oriented full-map controls, rather than the congressional-history selector. This establishes a visible acceptance gap, not the exact deployed commit. No live build identity, historical request, mobile acceptance or publication of #5553 is claimed. Deployment remains a separate authorized action.

## Placement and rollback

Directory Rules v2, adopted by ADR-0029, governs placement by responsibility. Its accepted Markdown authority was inspected (`docs/doctrine/directory-rules.md`, SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`); ADR-0029 identifies the older Directory Rules PDF as a lineage predecessor. This session did not re-extract that PDF.

Within the existing standalone hosted composition, `scripts/qualify-county-history.py` follows the offline-verifier responsibility, `tests/test_county_history_qualification.py` owns synthetic checks, and this document belongs to the existing human documentation root. The link in `docs/civic-districts.md` makes the next slice discoverable. These placements do not establish new monorepo schema, source-registry, policy or release homes. DIR-PLACE-001/002/003/005, DIR-DATA-004 and DIR-SOURCE-003 remain intact.

Raw source bytes, generated qualifications and temporary dependencies are not committed or copied into public assets. There is no public route to candidate data. No signed recipe, source approval, database, worker, deployment or second PC is changed. Rollback is a revert of these four authoring files; no persistent-data migration or released artifact cleanup is needed.
