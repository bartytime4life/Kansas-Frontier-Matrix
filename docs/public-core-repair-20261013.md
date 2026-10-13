# Public core-sample delivery repair candidate

## Scope and identity

The reported failure is on `https://www.kansasfrontiermatrix.com/`, the separate
GoDaddy Node composition. The owner-private Sites application is a different
runtime and is not replaced or republished by this change.

This candidate starts at `708183b09cd265b1f1ccd98c44765b2620b75d02` on
`a0-godaddy-free-reports`, preserving the merged camera and river-pacing changes.
The inspected local v259 source is
`441c3e29581ffb0293d8e643e5c37eed50319032`. The hosting branch and the exact
currently deployed GoDaddy revision remain separate facts; branch HEAD alone
does not establish deployment. The candidate branch is
`codex/godaddy-underground-availability-20261013`.

Placement follows the existing standalone application responsibilities:
`app/` owns rendering and bounded reads; `vendor/` and the npm lock own the
runtime repair; `tests/` owns synthetic checks; `docs/` records behavior and
verification. The monorepo's adopted Directory Rules and ADR-0029 continue to
govern its separate `apps/site/source` mirror. No new source, contract, policy,
release or proof authority root is created.

## Confirmed causes and changes

The public High Plains journey showed zero records and zero of four requested
tiles loaded. A normal HTTP read of an existing `.json.gz` source URL returned
404. The Node static cache skipped every `.gz`, `.br` and `.zst` file as a
transport-compression variant, including standalone compressed datasets.

`vinext-0.0.50-kfm.2.tgz` excludes a compressed URL only when its uncompressed
sibling exists. Standalone gzip data is served at its original URL with
`application/gzip` and no `Content-Encoding`, preserving the bytes that the
browser checks and decompresses. JavaScript/CSS transport negotiation remains
unchanged. No missing uncompressed alias is invented. Archive SHA-256:
`276f257130d285d8478403148737ae27f69fd5ee1ea86fdc8ce777cebe768b15`.
Only package metadata, the static-cache implementation and its regenerated
embedded source map differ among the 740 archive file members. The prior tar,
upstream license and other archive members are retained.

Once delivery worked, a core whose inventory range was 4,094–4,893 ft loaded
but drew no column: the aquifer's shallow depth cap hid the entire range.
The cutaway now includes valid selected record depths in its fit, bounded by
the existing 12,000 m ceiling. Original intervals, units, coordinates and
references are unchanged. The 50-record/400-interval budgets remain intact.
Core inventory spans remain envelopes with possible recovery gaps, not
continuous lithology or measured vertical trajectories beneath terrain.

If every requested source tile fails, the worker reports a source-delivery
failure rather than implying geological absence. The empty view separately
explains when loaded records have no valid intervals in the displayed range.

## Public locations and source terms

The owner explicitly clarified: "we can have precise locations as long as it
is public data". This candidate retains the existing locations from official
public KGS archives; it does not add private records or restore excluded fields.

On 2026-10-13 the official [Core Library](https://www.kgs.ku.edu/Magellan/CoreLibrary/)
offered its complete inventory download, and the official
[WWC5 page](https://www.kgs.ku.edu/Magellan/WaterWell/) offered statewide location
and log archives for public access. The
[KGS terms](https://www.kgs.ku.edu/General/copyright.html) explicitly permit free
reuse and redistribution with attribution and retained copyright notices.
Required attribution already present in the view and geological CSV/SVG exports:

> The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved.

A bounded, unauthenticated read of the
[official example core record](https://chasm.kgs.ku.edu/ords/qualified.well_page.DisplayWell?f_kid=1001251474)
confirmed public NAD27/NAD83 coordinates and inventory intervals within the
displayed 4,094–4,893 ft envelope. This is a provider record check, not survey
verification. [WWC5 metadata](https://www.kgs.ku.edu/Magellan/WaterWell/wwc5_fgdc.html)
warns that submitted records can be inaccurate or incomplete, and many positions
are calculated from PLSS descriptions. Display precision does not establish
location accuracy. Core trajectory and usable vertical datum remain unknown.

This source-specific confirmation replaces the assumption that all precise
public KGS locations must be hidden. It does not grant unrestricted treatment
of other sources, source admission, release activation, or permission to expose
private fields. Monorepo PR #5110 and its build guard are not modified or waived
by this application candidate. Cross-runtime reconciliation remains a separate
review. Unknown or nonpublic source assets remain ineligible for this rollout.

## Preservation and local verification

All 257 existing tiles were found locally, totaling 19,349,349 compressed bytes,
with every manifest digest matching. The locator adds 3,550,680 bytes. The
projection contains 6,598 mapped core identities and 314,844 well records.
These are counts of the October 6 capture, not a current provider census.
All 273 public asset files remain byte-identical to the candidate base.
No dataset was regenerated, imported, reseeded, migrated or activated.

| Executed check | Result |
| --- | --- |
| Locked installation, Node production build and TypeScript | Passed |
| Final HTTP gzip, worker, cutaway, runtime and access-boundary checks | 28 passed |
| Additional subsurface/aquifer/view-session checks | 71 passed |
| Existing area UI harness with corrected empty-state assertions | 19 passed |
| Full candidate suite | 1,144 tests: 1,127 passed, 17 failed |
| Exact-base suite after its own Node build | 1,139 tests: 1,122 passed, the same 17 failed |
| Public asset comparison and diff whitespace | No changes/errors |

The 17 inherited failures are Cloudflare Worker-composition assumptions
(`worker.fetch`/Wrangler) in this Node composition. They remain reported rather
than removed or described as passing. This branch has no GitHub workflow tree;
local execution does not imply hosted CI acceptance.

Real HTTP regression tests verify original compressed bytes and digest, gzip
MIME without transport decoding, ordinary compressed JS negotiation, HEAD/ETag
304, missing aliases, and private/traversal paths. Worker tests retain integrity,
Kansas bounds, request limits, date filters and cancellation checks. A deep-core
regression uses synthetic identity and asserts source objects are not mutated.

Fresh loopback browser checks on the built Node candidate showed 50 records,
28 plotted columns, one aquifer region and a complete 2048×1718 surface in the
High Plains view. A core-only probe found five nearby core identities. Selecting
one and showing its map area produced one loaded record and one plotted core
column, retaining the original feet range and approximately 1,491 m diagram
depth. At 1× vertical scale the column was visible below the surface plate;
unknown gaps stayed empty. Captured warning/error logs were empty. An unrelated
counties/population provider warning means this is not all-source readiness.
These are bounded local observations, not final hosted acceptance or a
performance benchmark. The original local service and preferences were retained.

## Dependency disposition and remaining gates

Both exact-base and candidate audits report eight affected packages at HIGH
and no CRITICAL findings, with the same underlying
[braces stack-exhaustion advisory](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm).
It lists no patched version. The installed chains run through fast-glob,
micromatch, ESLint and Vite build plugins. Inspection found no references to
these packages in the application handlers, Node production-server sources or
generated server code; no remotely controlled brace-pattern path was identified
in this bounded review. That does not prove exhaustive unreachability or
remediation. Dependencies are unchanged apart from the bounded vendored repair.
Do not suppress the audit or call the full application security-reviewed.

Merge, public GoDaddy deployment, exact deployed-revision readback and hosted
sample/opacity/selection checks remain separate owner-authorized operations.
No private Sites audience, D1/R2 binding, DNS/email, account or paid service is
changed. Repository-wide source admission and release review remain independent.

Rollback: restore the prior reviewed application revision and lock containing
`vinext-0.0.50-kfm.1.tgz` in an isolated build, verify the build, then use the
hosting app's reviewed rollback operation. Retain the datasets and local v259
copy; never revert by deleting source tiles or changing geological values.
The previous missing-file behavior would return, so rollback is a service
recovery option and not a data correction.
