# Kansas county history: source qualification and dated queries

Checked **2026-10-29**. **Source reuse notice confirmed; offline structural queries and geometry checks passed for the 1861-01-29 WORK candidate. The 1873–1874 disputed coverage is withheld. Public map integration is not implemented.** This is a development qualification record, not source admission or a release receipt.

The next useful civic slice is a dated county-history layer. The actual Newberry Kansas archive was acquired and checked. The original offline checker selects mapped versions for an exact day, with citations and record-level source locators. A separate offline geometry investigation now checks all versions and dated coverage epochs, applies a named NAD83-to-WGS84 display operation, and emits a WORK candidate only for a passing selected date. Historical interpretation and the modern continuation remain open. The private Node handoff below now carries those checked records into calendar and source-drawer rehearsals. This work adds no public route, map layer, download endpoint, source approval or hosted runtime dependency.

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
| Source projection | NAD83 geographic coordinates per bundled `.prj`; the original structural checker does not transform coordinates. The geometry follow-up below records its explicit display operation. |

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

## Offline geometry candidate implemented

`python3 scripts/qualify-county-geometry.py /absolute/path/to/KS_AtlasHCB.zip --date 1861-01-29` reuses the complete pinned-archive qualification and adds `geometryQualification` and `geometryCandidate`. The existing coordinate-free `snapshot` remains unchanged. Output is JSON on stdout; there is no acquisition, file write, publication flag or public consumer. Exit **0** means a WORK geometry candidate was produced, **2** means the selected coverage was quarantined without a geometry candidate, and **1** means input, dependency or processing failure. None means release approval.

**CONFIRMED on the exact archive:** all **341** source polygons and all 341 transformed polygons pass individual GEOS validity checks. The full **71** membership epochs were checked in source and target coordinates, with identical results: **69** pass coverage validation and **2** contain overlaps. Epoch boundaries include every source start and exclusive end, including an end without an incoming version. Shared edges are permitted; polygon interior intersections, containment and duplicate polygons are detected. The [Shapely coverage check](https://shapely.readthedocs.io/en/2.1.2/reference/shapely.coverage_is_valid.html) uses `gap_width=0`: holes are permitted, so a passing result does **not** establish complete coverage of Kansas or the absence of historical gaps.

| Coverage interval, end excluded | Result |
| --- | --- |
| 1873-03-20 to 1874-02-25 | Withheld: five intersecting record pairs |
| 1874-02-25 to 1874-03-18 | Withheld: the same five pairs |
| 1861-01-29 selected snapshot | WORK candidate: 50 source versions |

The overlapping source records are **268 Disputed Area**, **269 Stafford**, **271 Pawnee** and **276 Barton** (one-based SHP/DBF records). The five pairs are 268/269, 268/271, 268/276, 269/276 and 271/276. Their change descriptions explicitly report conflicting 1873 laws, citing *Kansas Laws 1873*, chapter 57, pages 112–113, and chapter 72, sections 27 and 29, pages 152–154. These are the Atlas's citations; this session did not independently inspect the underlying statutes. The observations support preserving a documented source dispute, not assuming digitization damage or deciding which jurisdiction prevailed.

The report retains those source descriptions, citations and digest-backed record locators. It never dissolves overlaps, snaps edges, fills gaps, clips to modern Kansas, simplifies, or runs automatic polygon repair. All dates from **1873-03-20 through 1874-03-17 inclusive** produce `geometryCandidate: null` and `candidateState: QUARANTINE`. A separately checked 1874-03-18 snapshot passes the geometry gate. **PROPOSED:** a future disputed-claims display can expose the competing source claims after interpretation review; this script does not authorize that display.

### Coordinate operation and provenance

The `.prj` must be equivalent to **EPSG:4269**, allowing the source WKT's different axis declaration. [pyproj TransformerGroup](https://pyproj4.github.io/pyproj/3.7.2/api/transformer.html) runs with network access disabled, `allow_ballpark=False`, and explicit longitude/latitude order. The tool selects only **EPSG:1188, NAD83 to WGS 84 (1)**, checking its method, zero translation parameters, reported 4-metre operation accuracy and area of use against the entire source extent. It refuses a missing or ambiguous named operation rather than accepting another transformation. PROJ's axis-normalized `DERIVED_FROM(EPSG)` representation is accepted only with the same operation code, method and parameters.

This is a documented **zero-translation display approximation**, represented by PROJ as a no-op. The reported 4 metres describe the coordinate operation; they are **not** a measured accuracy for these historical reconstructions, an epoch-specific datum solution, or a survey guarantee. Output is **OGC:CRS84 longitude/latitude**, with RFC 7946 ring orientation. All vertex counts are preserved and coordinates are checked for finite values and geographic ranges. No extra precision is inferred from the number of decimal places.

Each candidate feature retains its existing version identity and source EvidenceRefs. Its geometry has a deterministic SHA-256. The candidate includes the local WORK EvidenceBundle, extended with the exact SHX and PRJ member identities, and a projection EvidenceRef. The processing report records the complete operation PROJJSON, Python/library versions and PROJ database digest. The complete candidate has its own digest. These are inspectable development provenance, not signed release receipts or a replacement for canonical evidence contracts.

### Validation and reproduction

Use an isolated development **Python 3.11+** environment; no hosted Node dependency changes are needed:

```sh
python3 -m pip install pyshp==2.3.1 shapely==2.1.2 pyproj==3.7.2 numpy==2.4.6
KFM_COUNTY_ARCHIVE=/absolute/path/to/KS_AtlasHCB.zip python3 -m unittest discover -s tests -p 'test_county*.py' -v
python3 scripts/qualify-county-geometry.py /absolute/path/to/KS_AtlasHCB.zip --date 1861-01-29
python3 scripts/qualify-county-geometry.py /absolute/path/to/KS_AtlasHCB.zip --date 1873-03-20
```

The current host could not resolve PyPI. The actual checks used already-cached GIS packages and the previously pinned official pyshp module, outside the repository: **Python 3.11.15, pyshp 2.3.1, Shapely 2.1.2 / GEOS 3.13.1, pyproj 3.7.2 / PROJ 9.5.1, NumPy 2.4.6**. PROJ database SHA-256: `a25d85a2ebfc4584eba65186b7c41743b084ce5d391941cbb41c805947b77109`. GEOS 3.12+ is required for coverage checks; the report records the actual engine and database, so another toolchain must be checked rather than assumed byte-identical.

**Passed:** all **34 county tests**, comprising the prior 21 and 13 geometry tests. The new cases cover invalid/empty/non-polygon inputs, shared edges and holes, overlap/containment/duplicates, time-disjoint geometries, end-only transitions, wrong CRS/extent, unavailable operations, strict dates, all real coverage epochs, dispute withholding, ring orientation, source-reference resolution, unchanged temporal identities and CLI/API determinism. Source integration tests require the exact archive; missing dependencies or source bytes produce explicit test skips, not passing evidence. Application build, full repository tests and independent security review were not run for this offline-only change.

The 1861-01-29 candidate includes **50 mapped source versions**, with the separate query retaining **52 event-only records** and **16 undated cross-references**. These are whole-source counts, not counts of organized Kansas counties. The complete JSON report is **1,824,097 bytes**, SHA-256 `3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a`; its compact, sorted-key geometry candidate digest is `17955a7d60e690775b9dc3e90cf7202ce8d216958bfac71973c6e3c926bb5e32`. These measurements describe the tested toolchain above.

**Still open:** interpretation of source labels and disputed claims, independent legal/source accuracy, provider-declared encoding, geographic completeness, post-2000 continuation, canonical source/evidence admission, release review, browser rendering and performance. The parent output remains `status: HOLD` and `releaseEligible: false` even for a passing geometry candidate.

## Private calendar and source-drawer handoff implemented

**CONFIRMED, 2026-10-29:** [PR #5566](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5566) merged at `5204194904fac8df3d550e4890a79429aa5260fd`. Its exact head `7c39c86790fa2c228fb416b83ecc95592ce866c1` has successful `welcome-performance` and `verify-core-delivery` checks. The recorded Codex review summary reports completed code review with no findings; it does not establish an independent security review or source admission.

The next implementation adds the private `server/county-history-candidate.mjs` adapter and the operator command:

```sh
node scripts/pc-pipeline/cli.mjs county-history /absolute/path/to/qualification.json 3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a
```

That digest identifies the **1861-01-29 report above**. For another date, first run the Python geometry investigation and independently record that report's byte digest. Do not reuse this date's digest or treat a digest copied from inside an untrusted report as external validation.

The command reads one explicit absolute regular-file path, rejects symlinks and symlinked parent directories, limits the read to 8 MiB, checks file stability and SHA-256 before JSON parsing, and writes its result only to stdout. It performs no network acquisition, database writes, key access, schedule installation or publication. CLI exit 0 means a checked **research candidate** was adapted; 2 means its coverage is quarantined; 1 means failure. The existing kit copier includes the new adapter and its dependency chain.

| Handoff element | Implemented behavior |
| --- | --- |
| Source binding | Exact archive URL/digest/size, pinned SHP/DBF/SHX/PRJ/chronology identities and WORK lifecycle |
| Version records | Recomputed deterministic identities; original names, optional FIPS/state, source type and unreviewed classification retained |
| Geometry | Bounded Polygon/MultiPolygon structure; matching feature/record identities and SHP/DBF record locators; no clipping, rounding or new transform |
| Chronology | Date-specific events remain distinct from polygons; null institution IDs remain null; all 16 aliases retain unknown temporal applicability |
| Calendar rehearsal | Exact selected day only; absent snapshots and dates outside 1804-10-01–2000-12-31 return empty held views; no carry-forward across an interval |
| Source-drawer rehearsal | Original citation/change, validity dates, institution ID, source labels and resolvable WORK EvidenceRefs; stale-day or unknown-ID selection returns null |
| Disputed coverage | Private source records remain inspectable, but map geometry is empty and the CLI returns 2 |
| Release boundary | `lifecycle: WORK`, `releaseEligible: false`, `publicClientEligible: false`; the public pipeline rejects this packet/source |

These functions are **private rehearsals for the eventual calendar and drawer integration**. The public Explorer does not import this adapter and gains no route, layer, client-side import control, or release capability from this patch. Approval and released-read integration remain required before a public map can consume county history. The adapter neither decides those approvals nor changes the current signed recipe to make this source publishable.

### Cross-language integrity and verification scope

The adapter verifies the original UTF-8 report bytes against the separately supplied digest. Python and JavaScript can encode equivalent JSON numbers differently, for example `-110.0` and `-110`. It therefore preserves the upstream candidate and geometry digests with their Python encoding label instead of making a false comparison against JavaScript reserialization. A separate SHA-256 binds the normalized JavaScript research packet. Byte integrity and a correctly shaped report do **not** prove source approval, truthful upstream computation or legal authority. GEOS topology checks remain evidence in the referenced qualification; this adapter rechecks transport structure and references without pretending to repeat GEOS.

The real statehood report produced **50 unchanged geometries**, **52 dated events**, and **16 undated references**. Every source identity, coordinate array, citation and record-level EvidenceRef was compared with the original Python output. The derived private CLI output is 747,797 bytes (including its final newline), SHA-256 `546f4709cb167396ea861aedafa2b3fba5b7dfbda66ee9d1897dbd670870e7ed`; its adapter-content digest is `620eabd35b971b15dbc015647521ad64d334d4d6000fff4be39a681d381594fc`. A separately generated real **1873-03-20** report was also adapted: its report digest is `469cff70b71135a2cdd9c6667450f147cda019fea9f08bb3bc896e8af36351ef`, and the CLI returned 2 with zero map features.

**Passed:** 17 adapter tests with the real report supplied, including 16 synthetic transport/negative/installation cases and one actual-report integration case. Without the real-report environment variables the integration case is explicitly skipped. Changed-file ESLint passed with no diagnostics. Five focused test files passed: the new adapter, civic intake, PC pipeline, pipeline cutover and pipeline domain. The new tests exercise wrong source and self-asserted release claims, changed digests and members, dangling references, duplicate/missing/substituted records, strict dates, malformed geometry, quarantine, exact-day projections, unsafe paths, mutation checks and isolated kit imports. Synthetic boxes and citations are test data, never historical evidence.

The existing `pipeline-install.test.mjs` subprocess test **fails on both exact base and head** at its first JSON parse because child stdout is empty. A direct child-process probe additionally reported `EPERM`. This is recorded as an environment-limited inherited failure, not a passing installed-worker qualification. The new in-process test successfully loads the CLI and county adapter from a fresh copied kit. Direct CLI smoke checks ran separately on the real reports. Full application build, browser acceptance, full repository suite and independent security review were not run for this private operator-only scope.

Reproduce the actual-report test with the report created above:

```sh
KFM_COUNTY_REPORT=/absolute/path/to/qualification.json KFM_COUNTY_REPORT_SHA256=3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a node tests/county-history-candidate.test.mjs
node --test tests/county-history-candidate.test.mjs tests/civic-intake.test.mjs tests/pc-pipeline.test.mjs tests/pipeline-cutover.test.mjs tests/pipeline-domain.test.mjs
```

### Handoff placement, compatibility and rollback

This patch starts from hosted commit `45df10bf46e5e066f06f1080a2b635894bb2779d`, tree `325d11ed9c45bb7c8109efcc221b5ebc1e09829d`. The earlier geometry work and intervening changes were reconciled to that exact tree. The final five-file drought update was preserved and does not overlap these five handoff files; the focused tests were repeated after reconciliation.

Under accepted Directory Rules v2/ADR-0029, the existing hosted `server/` responsibility owns reusable operator adapter logic, following the private `server/aviation-candidates.mjs` precedent. `scripts/pc-pipeline/cli.mjs` remains a thin invocation wrapper; `bundle.mjs` owns installed-kit assembly; tests and this document retain their existing roots. This carries forward the DIR-EXEC-007 migration boundary: it creates no canonical schema, source registry, policy or release authority. The member pins are bounded compatibility checks for this previously qualified report format. Future canonical source admission must reconcile them with the existing source registry rather than treating this file as a parallel registry.

The three files used by `recipeDigest()` are byte-unchanged. Both base and head compute `e8b85ea8ff6414e9dc46030835d2102ce7439cf7811615512b422b2386d5fab3`; this patch therefore does not itself change the recipe binding of existing source approvals. Their other validity conditions remain independent. No credentials, approvals, database, deployment, public data or second PC were changed. Rollback is a revert of the adapter, test, CLI/kit changes and this documentation update; there is no persistent migration to reverse.

## Proposed implementation after qualification

1. Preserve the raw ZIP and member identities through the existing RAW → WORK/QUARANTINE lifecycle. Use the existing source-registry and evidence responsibilities after an exact-tree placement review; this hosted checker creates neither.
2. Reuse the tested temporal identities, evidence references and distinct event/cross-reference roles when building the geometry adapter. FIPS remains optional. Reconcile the WORK format with the existing canonical evidence contracts at source admission.
3. Preserve the tested `[start, end + one day)` semantics and original dates. Treat post-2000 official vintages as a separately qualified continuation, not a carry-forward.
4. Resolve territory, non-county area, proposed/unrecognized jurisdiction and renamed/re-created county semantics from evidence. Do not use the catch-all `County` field alone. State/county administrative claims do not establish Indigenous sovereignty, land ownership or absence of communities.
5. Use the checked geometry candidate and retain the disputed-coverage hold. Qualify any later simplification separately. Preserve correction lineage and unmapped chronology events. Reuse the existing map/calendar/source drawer after a bounded adapter and source/release review exist; the old bundled license is no longer a blocker.
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

**Limits of the original structural-only checks:** topology and datum conversion were unchecked at that stage; the geometry follow-up above now provides bounded results. Independent verification of every legal boundary, provider-declared text encoding (CP1252 was used successfully), historical positional accuracy, full application tests, independent security review, browser map performance and release readiness remain unestablished. The JSON output is deterministic qualification evidence, not a governed release proof. Exit zero means checks ran successfully; it does not change HOLD.

## Congressional and hosted status

[PR #5553](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5553) is **merged**, verified this session. The hosted branch subsequently reached `cdbe5d7b66ba431f1bb373201c316fe7048a4509` (tree `fe0a3c737704cae4fad46bcf3949906fc90128cf`). Its source tree was reconstructed and checked before this patch.

The initial county qualification [PR #5557](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5557) was subsequently merged at `8f5407fcfb5a258b1c0c56e9aaa7c71676109049` (tree `4ecbc6aa26affcc874919b1ff2ebae4c2e6f0ac2`). This rights/query follow-up is based on that exact tree. Twelve intervening drought-related files were reconciled without overlap with the four county qualification files. These merge observations are not deployment evidence.

A later read-only Chrome check on **2026-10-29** supersedes the earlier deployment observation: [the public site](https://kansasfrontiermatrix.com/) now shows “Kansas representation” and Congress 36–119 controls. Selecting Congress 36 loaded the **1861-01-29 statewide at-large plan**, with visible geometry, a selected-plan download link and source record revision `a72f5836d0de4ad5aa94a18b6b725b46bf71b39e` / SHA-256 `8953c719b3f71c374e6dfc797d9740b70b593a52932b1cbb5fa18beac4f6eea3`. This confirms that desktop path, not every Congress, mobile acceptance or the exact deployed application commit. No deployment was performed in this follow-up.

The same inspection exposed inherited drawer inconsistencies: a scholarly source appears under “OFFICIAL SOURCE”, and the loaded 1861 record also receives a current-2026 time warning and hidden-layer warning. The source details correctly identify the scholarly reconstruction and absence of a KFM EvidenceBundle. The subsequent [selected-record correction](civic-districts.md#selected-record-time-and-visibility) adds exact historical date/Congress matching, shared map/drawer visibility and neutral source-card labels. Its build and focused tests passed, but local browser startup was blocked by `listen EPERM`; deployed acceptance remains pending. A fresh live-site check at approximately **09:29 CDT on 2026-10-29**, after PR #5561 merged, still showed “OFFICIAL SOURCE”, the current-2026 warning and the hidden-layer warning for the loaded Congress 36 record. This is evidence that the corrected behavior was not yet present on that inspected page, not proof of the deployed commit. No deployment was attempted. The county query itself does not publish a map layer.

## Placement and rollback

Directory Rules v2, adopted by ADR-0029, governs placement by responsibility. Its accepted Markdown authority was inspected (`docs/doctrine/directory-rules.md`, SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`); ADR-0029 identifies the older Directory Rules PDF as a lineage predecessor. This session did not re-extract that PDF.

Within the existing standalone hosted composition, `scripts/qualify-county-history.py` follows the offline-verifier responsibility, `tests/test_county_history_qualification.py` owns synthetic checks, and this document belongs to the existing human documentation root. The link in `docs/civic-districts.md` makes the next slice discoverable. These placements do not establish new monorepo schema, source-registry, policy or release homes. DIR-PLACE-001/002/003/005, DIR-DATA-004 and DIR-SOURCE-003 remain intact.

Raw source bytes, generated qualifications and temporary dependencies are not committed or copied into public assets. There is no public route to candidate data. No signed recipe, source approval, database, worker, deployment or second PC is changed. Rollback is a revert of these four authoring files; no persistent-data migration or released artifact cleanup is needed.

### Geometry follow-up placement and migration boundary

The geometry investigation adds `scripts/qualify-county-geometry.py` beside the existing offline checker, `tests/test_county_geometry.py` under existing verification ownership, and this documentation update. These are non-authoritative development investigations in the standalone hosted composition. **DIR-EXEC-007 migration note:** these scripts must not become production imports or unique release/admission authorities. Any reusable production adapter must move through the existing canonical pipeline/tool/package responsibilities after an exact-tree placement and consumer review; a public API must not read these WORK outputs. No new schema, registry, policy, evidence or release root is created.

The supplied *KFM Baseline Geospatial Data and Tile Production Architecture* (pages 1–3, inspected this session) also calls for native-source preservation, normalization of working data and reproducible display derivatives. The raw ZIP, temporary environment and generated JSON stay outside public assets and this Git patch. Rollback of this geometry follow-up is removal/revert of its two authoring files and documentation changes; no database, source admission, released data or deployment is affected.

The geometry patch was prepared against hosted base `466495fb156d47ea5ff614ce778ddbe354697868`, tree `76c61c660438647846aa830775b74ec207b3fbbd`. Intervening drought-map changes were preserved, with no overlap in these three authoring files. The complete county tests were rerun on that reconciled base.
