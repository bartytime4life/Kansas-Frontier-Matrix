# Kansas county history: source qualification and dated queries

Checked **2026-10-29**. **Source reuse notice confirmed; offline structural qualification and dated queries passed. Public map integration is not implemented.** This is a development qualification record, not source admission or a release receipt.

The next useful civic slice is a dated county-history layer. The actual Newberry Kansas archive was acquired and checked. The offline checker now selects mapped versions for an exact day, with citations and record-level source locators. Topology, datum conversion, interpretation and the modern continuation remain open. This change adds no route, map layer, download endpoint, source approval or runtime dependency.

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

## Rights evidence and correction

**CONFIRMED:** the [Atlas state download page](https://publications.newberry.org/ahcb/downloads/states.html), which links this exact Kansas ZIP, permits lawful commercial and noncommercial reuse without library permission fees. It explicitly identifies the old bundled licenses as outdated and says they can be ignored. The [Atlas download overview](https://publications.newberry.org/ahcb/downloads/index.html) carries the same dataset-specific notice. The [Library of Congress catalog record 2018487899](https://www.loc.gov/item/2018487899/) separately identifies the Atlas collection, including state GIS packages, with a **CC0** Rights Advisory.

Both the provider's state download notice and the Library of Congress Rights Advisory were directly inspected in Chrome on **2026-10-29**, after research fetches returned 403. The catalog's initial automatic verification page resolved normally; no challenge was solved or bypassed. These are recorded observations as of that date, not network checks performed each time the offline script runs.

**Correction to the initial qualification in [PR #5557](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5557):** its rights hold relied on the bundled [CC BY-NC-SA 2.5](https://creativecommons.org/licenses/by-nc-sa/2.5/) deed and older state page, while overlooking the explicit supersession notice. The earlier conclusion was incomplete. This follow-up removes that rights blocker. It does not claim the notice changed on the verification date. The original deed and its digest remain part of the preserved archive; the current provider notice and catalog advisory are recorded alongside it. The draft clarification message is superseded and was never sent.

Reuse permission does not turn this scholarly reconstruction into government-issued or legally authoritative boundary data. This finding applies to the Atlas dataset, not all third-party material cited in its bibliography, and does not make a KFM candidate a released artifact.

The offline checker continues to return `status: HOLD` and `releaseEligible: false`: those fields describe the absent release decision, not an unresolved provider license. It has no approval flag. The existing governance process owns source admission and any future release.

## Exact-day query implemented

`--date YYYY-MM-DD` adds a deterministic `snapshot` to the qualification output. It first checks the complete pinned archive. The query accepts only a calendar day inside the mapped coverage, 1804-10-01–2000-12-31. It rejects compact dates, timestamps, malformed days and unsupported years before opening the archive. It never carries a version across a source gap or beyond 2000.

The snapshot separates three kinds of information:

- `boundaryVersions`: source versions covering the selected day using inclusive source ends normalized to exclusive KFM ends. Source names, FIPS when present, state/type labels, change descriptions and citations are retained. The type remains an unreviewed source label; it is not promoted into a legal county classification.
- `eventOnlyRecordsOnDay`: chronology-only events occurring on that exact day. An absent institutional ID remains null. Events do not create open-ended polygons or imply that every event of the selected day is listed here; mapped changes remain in the boundary records.
- `undatedNameCrossReferences`: all 16 source cross-references, explicitly marked with unknown temporal applicability. These are dataset context, not a list of names valid on the selected day.

Each record carries `evidenceRefs` resolving to a local WORK `evidenceBundle`: the exact source URL/archive digest, member digest and one-based member record number. TSV record numbers exclude the header and mean parsed data records, not physical text lines. Boundary references identify the matching SHP, DBF and chronology records. Identities include the archive revision; version identities also include the institutional ID, version and date interval. Event and cross-reference identities use the member digest and source record locator, so missing institutional IDs are not fabricated.

This is a bounded offline query format, not a new canonical contract, source registry, public DTO or release proof. Its only output is JSON on stdout; it performs no writes, acquisition or publication. Coordinates are deliberately absent while datum conversion and topology remain unchecked. The cited geometry locators enable that next processing step without mislabeling NAD83 coordinates as WGS84. The 1803 chronology evidence remains in the qualification and source; the geometry date query does not claim to cover it.

## Proposed implementation after qualification

1. Preserve the raw ZIP and member identities through the existing RAW → WORK/QUARANTINE lifecycle. Use the existing source-registry and evidence responsibilities after an exact-tree placement review; this hosted checker creates neither.
2. Reuse the tested temporal identities, evidence references and distinct event/cross-reference roles when building the geometry adapter. FIPS remains optional. Reconcile the WORK format with the existing canonical evidence contracts at source admission.
3. Preserve the tested `[start, end + one day)` semantics and original dates. Treat post-2000 official vintages as a separately qualified continuation, not a carry-forward.
4. Resolve territory, non-county area, proposed/unrecognized jurisdiction and renamed/re-created county semantics from evidence. Do not use the catch-all `County` field alone. State/county administrative claims do not establish Indigenous sovereignty, land ownership or absence of communities.
5. Qualify datum conversion, topology and any display simplification before rendering. Preserve correction lineage and unmapped chronology events. Reuse the existing map/calendar/source drawer after a bounded adapter and source/release review exist; the old bundled license is no longer a blocker.
6. Start the future UI with a selected date, explicit reconstruction attribution, source details and a keyboard list. Then-versus-now comparison needs a separately dated modern source. No officeholder, election-result or population crosswalk is inferred by this slice.

## Reproduce the checks

Use a separate development Python environment with **pyshp 2.3.1**. This is an offline-tool dependency, not a hosted application dependency. The 18 synthetic tests use only the Python standard library. Three additional tests are opt-in real-archive checks and need pyshp. The acquisition step is intentional and external to the checker.

```sh
python3 -m unittest discover -s tests -p test_county_history_qualification.py -v
python3 scripts/qualify-county-history.py /absolute/path/to/KS_AtlasHCB.zip
python3 scripts/qualify-county-history.py /absolute/path/to/KS_AtlasHCB.zip --date 1861-01-29
KFM_COUNTY_ARCHIVE=/absolute/path/to/KS_AtlasHCB.zip python3 -m unittest discover -s tests -p test_county_history_qualification.py -v
```

In this session the package installer could not resolve pyshp. The exact [official 2.3.1 source module](https://github.com/GeospatialPython/pyshp/blob/2.3.1/shapefile.py) was retrieved through GitHub into a temporary dependency directory, outside the repository. Its SHA-256 is `9c749d73e31cc332e4683130a808258b407d2ba8cf33a5e1d5ea190c0eaae73f`. Running the checker with that directory on `PYTHONPATH` passed on the acquired ZIP. No third-party module is vendored by this change.

**Passed:** 21 tests with the exact source archive supplied: 18 synthetic regression tests and three real-source checks. They cover inclusive ends, gaps, event-only history, aliases, missing FIPS/IDs, overlapping identity, strict dates, malformed geometry, digest/symlink rejection, bounded ZIP handling, evidence-reference resolution and stable identities. The real-source transition check compares every version start/end and its adjacent days against the original numeric source intervals; no historical counts are inferred from today's counties. It also verifies the seven frame counts above, Clark County's 1883 disappearance/1885 return and deterministic repeated full qualification. Without `KFM_COUNTY_ARCHIVE`, the three real-source tests are explicitly skipped, not counted as passing.

The exact CLI query for **1861-01-29** produced **50 mapped versions, 52 event-only records and 16 undated cross-references**, 122,118 JSON bytes with SHA-256 `3a58068a837a1dd53e455e931ff9c1648785c1c5d83c117e127d9fff7df558ab`. A CLI smoke check caught a development defect where the report's frame loop overwrote the requested day. The loop variable is now separate, and the real-source regression checks the requested date, expected count, CLI/API equality and absence of a snapshot when no date is supplied. The final 21-test run passed after that correction.

**Not established:** polygon topology or overlap between different institutions, independent verification of every legal boundary, provider-declared text encoding (CP1252 was used successfully), datum-transform accuracy, full application tests, independent security review, browser map performance, or release readiness. The JSON output is deterministic qualification evidence, not a governed release proof. Exit zero means checks ran successfully; it does not change HOLD.

## Congressional and hosted status

[PR #5553](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5553) is **merged**, verified this session. The hosted branch subsequently reached `cdbe5d7b66ba431f1bb373201c316fe7048a4509` (tree `fe0a3c737704cae4fad46bcf3949906fc90128cf`). Its source tree was reconstructed and checked before this patch.

The initial county qualification [PR #5557](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5557) was subsequently merged at `8f5407fcfb5a258b1c0c56e9aaa7c71676109049` (tree `4ecbc6aa26affcc874919b1ff2ebae4c2e6f0ac2`). This rights/query follow-up is based on that exact tree. Twelve intervening drought-related files were reconciled without overlap with the four county qualification files. These merge observations are not deployment evidence.

A later read-only Chrome check on **2026-10-29** supersedes the earlier deployment observation: [the public site](https://kansasfrontiermatrix.com/) now shows “Kansas representation” and Congress 36–119 controls. Selecting Congress 36 loaded the **1861-01-29 statewide at-large plan**, with visible geometry, a selected-plan download link and source record revision `a72f5836d0de4ad5aa94a18b6b725b46bf71b39e` / SHA-256 `8953c719b3f71c374e6dfc797d9740b70b593a52932b1cbb5fa18beac4f6eea3`. This confirms that desktop path, not every Congress, mobile acceptance or the exact deployed application commit. No deployment was performed in this follow-up.

The same inspection exposed inherited drawer inconsistencies: a scholarly source appears under “OFFICIAL SOURCE”, and the loaded 1861 record also receives a current-2026 time warning and hidden-layer warning. The source details correctly identify the scholarly reconstruction and absence of a KFM EvidenceBundle. These conflicting drawer labels remain a follow-up defect; this offline query patch does not silently claim to fix them.

## Placement and rollback

Directory Rules v2, adopted by ADR-0029, governs placement by responsibility. Its accepted Markdown authority was inspected (`docs/doctrine/directory-rules.md`, SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`); ADR-0029 identifies the older Directory Rules PDF as a lineage predecessor. This session did not re-extract that PDF.

Within the existing standalone hosted composition, `scripts/qualify-county-history.py` follows the offline-verifier responsibility, `tests/test_county_history_qualification.py` owns synthetic checks, and this document belongs to the existing human documentation root. The link in `docs/civic-districts.md` makes the next slice discoverable. These placements do not establish new monorepo schema, source-registry, policy or release homes. DIR-PLACE-001/002/003/005, DIR-DATA-004 and DIR-SOURCE-003 remain intact.

Raw source bytes, generated qualifications and temporary dependencies are not committed or copied into public assets. There is no public route to candidate data. No signed recipe, source approval, database, worker, deployment or second PC is changed. Rollback is a revert of these four authoring files; no persistent-data migration or released artifact cleanup is needed.
