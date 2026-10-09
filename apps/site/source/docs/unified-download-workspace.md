# Unified local download workspace

Design follow-up, 2026-10-08. Local implementation; hosted publication is outside
this request. Human review remains pending.

## Observed problem

The original `/downloads` page exposed useful capabilities but arranged them as
separate systems. At a 1440 × 1000 desktop viewport, its content was 5,416 pixels
high. Mine-map/geology discovery began at y=1,765, public-map transfer history at
y=4,775, and Earth Engine history at y=5,119. A twelve-row storage inventory came
first, both services had connection controls, source coverage was expanded, and
six filters competed with map results. File actions followed a long metadata
block. These measurements describe the browser state observed on 2026-10-08,
not fixed layout dimensions.

## Design decisions

- Put **Find data**, **My library**, and **Activity** in one workspace. Discovery
  leads; current transfers remain accessible while browsing or inspecting files.
- Keep maps/geology and satellite/climate as recognizable source categories.
  Basic dataset/year/file selection belongs here; advanced Earth Engine recipes
  and comparisons retain their existing workspace.
- Make a file's format, size and download action easy to find. Keep original
  documents, provider records, source terms and map previews nearby. Detailed
  metadata and advanced filters use disclosures instead of disappearing.
- Present one connection area and one activity history while retaining each
  provider's real request, authentication, cancellation and progress semantics.
- Show bounded background operations truthfully: bytes for document transfers,
  completed files for Earth Engine tiles, indeterminate progress when totals are
  unknown. A selected maximum is a stop limit, never a completion denominator.
- Automate local connection, status updates, foreground recovery and library
  refresh after a newly observed completed or stopped capture. Payload selection,
  maximum size and the final download action remain explicit. No automatic retry,
  review approval, imagery activation, scheduled transfer or resumable queue is
  implied.
- Retain the KFM pine, sage and sand palette, readable controls and restrained
  typography. Desktop activity can remain beside discovery; a compact mobile
  task strip must leave content and focused controls unobstructed.

## Preserved contracts

The local origin, D1/R2 state, credentials, RAW/WORK store and 500 GB replaceable
cache policy are independent of this presentation change. All 596 archive
identities, Allen preparation hashes, supplied source URLs and rights states
remain intact. Ordinary scans stay documents until verified preparation. A
completed download remains a stored candidate; it does not establish source
admission or approved map display.

Existing `/downloads#public-maps`, `/earth-engine`, source-document links and
manual recipe workflows remain reachable. Hosted origins require explicit local
service connection. The loopback backend continues to enforce one active
transfer across provider types.

## Background behavior

The workspace owns one controller per native download protocol. Switching
between views keeps those controllers and the user's selected source mounted.
Status checks run every 2.5 seconds during active work and every 15 seconds when
idle. Hidden tabs abort their outstanding reads and resume on return; each
controller allows only one request round at a time. Catalog payloads are read on
connection or completed discovery instead of on every progress tick.

An accepted start stays reserved until a status request issued after its
acknowledgement returns. An uncertain start retains its request ID for the same
selection. Native job IDs, byte/file units, stop limits and cancellation requests
remain separate. A terminal transition triggers a library refresh, with one
trailing refresh if a scan is already running. Pre-acknowledgement library reads
cannot replace the newly acknowledged scan or consume that trailing request.

## Acceptance evidence

Final checks on 2026-10-08:

| Check | Observed result |
|---|---|
| TypeScript, production build | Passed |
| Full Site suite | 732 tests passed, no failures or skips |
| Full ESLint | No errors; 45 existing warnings remain |
| Local API smoke | 57 checks across 47 routes passed; nine provider-only routes listed |
| Independent runtime review | 28 focused tests passed; no remaining actionable findings |
| Independent visual review | PASS with mobile-focus refinement; separate same-provider evaluator because no other provider was available |
| Responsive browser | Actual 1440×1000, 768×1024, 390×844 and 375×812 viewports; no horizontal page overflow |

Desktop discovery now begins around y=494 and the activity panel at y=392, within
the initial viewport. Default desktop content measured 1,574 pixels, compared
with 5,416 before this change. On the final 390×844 mobile page, the heading was
at y=375, search at y=452 and first result at y=634. At 375×812, choosing JPEG
then PDF focused the maximum field around y=296–341, above the fixed activity
strip at y=751–802. The focus helper also has a deterministic keyboard-viewport
regression; physical phone/OS keyboard testing was not performed.

Actual local interactions verified: connection and 1,695-record catalog loading;
search and publisher filtering/reset; retained map/file selection across views;
Earth Engine dataset/year selection with its existing unconfigured sign-in
boundary; source details, dates and rights; opening the publisher JPEG; loading
five KGS features, selecting Marmaton Group and reading its description;
attribution and legend; keyboard Enter/Tab access and focus return to the result
heading; combined history and the stopped-transfer filter.

A real M-118 PDF completed with 37,386,469 stored bytes. That first check exposed
a native browser timer receiver error missed by injected timer mocks. The final
code uses explicit Window timer calls, and a strict-receiver regression prevents
recurrence. After rebuilding and reinstalling, a second bounded transfer showed
5,242,880 bytes of live progress while navigating the workspace. Cancellation
from the mobile strip retained 36,700,160 bytes under the selected 37,748,736-byte
maximum. Job `8cad856290314a2c97b1c0b63b71ed1a` became `cancelled`; its stored-byte
SHA-256 is `ba6f165ac97ec74ca15ee0203557fc31676fb2b268871337753527b15e8b1ba6`.
The library refreshed automatically and completed at `2026-10-08T19:18:31Z`.
No new browser errors were observed after the corrected installation. Captures
remain private candidates with rights review held.

Deterministic tests cover source failures, native progress units, unknown totals,
pending acknowledgements, uncertain-start IDs, cross-provider busy state,
cancellation, hidden/resumed polling, obsolete responses, and one coalesced
trailing library scan. Those tests do not claim a real Earth Engine download:
its project remains unconfigured. Comprehensive accessibility, touch-device,
provider availability and geological acceptance remain separate reviews.

## Local delivery and rollback

The implementation starts at repository main
`5874802f4f4be4968a68a96ed526d7fb4d68cd8d`, after mine-map PR #4944 merged. Its
765 Site source files matched the existing local checkout before editing.
The final local application is installed under
`/home/bartytime/Projects/KFM-Explorer-Site-download-workspace-20261008-r2` and
served through the existing `KFM-Explorer-Site-current` alias on port 4173.
The original Git remote `/tmp/kfm-authoritative-site-20261008` and persistent
`KFM-Explorer-Site-v109/.wrangler/local-state` remain in use. The loopback
operator, credentials, store configuration and provider endpoints were not
changed. The new application has 776 source files; final source parity is
checked independently of built assets and private data.

Rollback can restore the alias to the preserved
`KFM-Explorer-Site-mine-geology-20261008-r4` checkout and restart only
`kfm-explorer-local.service`. Existing captures and D1/R2 state require no
migration. Revert this UI/controller diff for repository rollback.

The prior merged Site workflow failed on three lint errors in the old download
components; this change fixes those errors and verifies the full lint/build/test
sequence locally. Unrelated repository gap, water mirror-review, People marker
and soil-index checks are not waived. Exact-head hosted CI and human review are
reported on the draft PR separately. No hosted Site publication, source
admission, map-review approval or audience change is included.


## Google account and local library update — 2026-10-09

Sign in with Google before choosing a project. The local operator exchanges a
one-time PKCE code, refreshes the grant and reports the account when Google
provides a verified email. Project discovery uses the read-only Cloud project
list scope; it does not create projects, enable APIs or billing, or grant IAM
roles. Choose a project (or enter its ID if listing is unavailable) and use
**Check download access**. A real Earth Engine scalar computation must succeed
before the download control becomes ready. Saved credentials are rechecked on
operator restart; a credential file alone does not establish access.

OAuth additionally requests email/OpenID and read-only project listing alongside
the existing Earth Engine scope. Tokens remain in private local credential
storage and never appear in status responses or Site storage. Legacy grants can
still be checked with a manually entered project; missing email/project-list
permissions have an explicit fallback. Browser Google cookies alone are not an
Earth Engine grant. Google consent and live account/project acceptance require
the owner to complete sign-in.

**View downloaded data** opens My library directly. It lists recent completed
and partial transfers by source, with bytes and destination, plus the bounded
filesystem metadata scan of all existing collections. Earth Engine raw files
are grouped by dataset and period; empty directories are not downloaded data.
Transfer history does not prove a file still exists, and stored bytes do not
approve a dataset for map display. The existing refresh, stale-state, partial
capture, size-cap and source-review protections remain in effect.

References: [Google authentication](https://developers.google.com/earth-engine/guides/auth)
and [read-only project discovery](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/list).


### No-login Kansas catalog preference — 2026-10-09

Satellite & climate defaults to public publisher files. Google sign-in is an
optional Earth Engine export path. The initial public collection contains 20
USDA NASS national CDL ZIPs (2008–2025, including the 2024/2025 10 m and
resampled 30 m alternatives) and 44 CHIRPS v2 annual GeoTIFFs (1981–2024).
Every offered URL was found in the publisher's listing and checked anonymously
with a bounded byte-range read: file signature and total byte length matched.
No full datasets were fetched as part of curation. The exact URLs are pinned in
the local operator; redirect/query variants and arbitrary future URLs remain
denied. Publisher originals include Kansas but are national/global files, not
Kansas clips or byte-identical Earth Engine recipe outputs. Size and scope are
visible before an explicit download. They use the existing local transfer,
cancellation, history and library paths without Google credentials. The source
coverage remains a curated subset; geology refreshes retain its separate check
date and never mark it as a complete live Earth Engine catalog.

Public sources: [USDA files](https://www.nass.usda.gov/Research_and_Science/Cropland/Release/),
[CHIRPS annual files](https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/),
and [Earth Engine catalog](https://developers.google.com/earth-engine/datasets).
