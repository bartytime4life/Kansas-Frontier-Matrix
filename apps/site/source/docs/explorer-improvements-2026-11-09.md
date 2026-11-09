# Explorer reliability and recovery improvements — 2026-11-09

This bounded application change is proposed for repository review from
`main@f7166031e5d5aa92e1ea73762e841675cffb1406`. It is not a complete project
audit, a hosted release, or source-admission evidence. Implementation, tests
and this note stay in their established Site application homes under ADR-0029.

## Resulting behavior

| Area | Demonstrated problem | Result |
| --- | --- | --- |
| Provider requests | Rejected responses retained unread bodies; stalled reads could outlive cancellation. | Cancel unusable streams, enforce cancellation during body reads, release readers, and reject partial success after abort. |
| Earthquake context | A response capped at 250 events could appear complete; withheld invalid records did not make the envelope partial. | Request one lookahead event, publish at most 250, disclose capped/withheld results as partial, and safely handle invalid timestamps. |
| Source downloads | Download metadata omitted the displayed feature count and truncation flag. | Carry those limitations into downloaded GeoJSON beside the source and clock metadata. |
| Error recovery | Persistent failures offered only another retry; route-wide copy described every failure as a map error. | Offer full-navigation exits to Data & downloads and the sources/evidence guide, with accurate retry guidance. |
| Source connections | Initial failure looked like ongoing checking; a stalled request could strand retry. | Show errors and retry, bound catalog/capture-list refresh to 15 seconds, retain earlier results, and cancel obsolete requests. |
| Navigation | Connections linked to a nonexistent source-operations route. | Open the existing Daily capture & archive workspace. |

The [USGS event API documentation](https://earthquake.usgs.gov/fdsnws/event/1/)
defines the source result limit and inclusive end-time behavior. The application
retains its end-exclusive selected-day filter and makes withheld records explicit.
No synthetic response is treated as admitted provider data.

## Regression coverage

Coverage includes HTTP rejection, byte caps, stalled reads after headers,
caller cancellation, deadlines, successful stream completion, earthquake
boundaries at 0/249/250/251 events, invalid/outside-window records, exported
provenance, recovery links, blocked browser storage, initial status failure and
retry, unmount/late-response handling, and retention of earlier capture results.

Two existing harnesses also need the browser/map context now required on main:
the map-click test supplies the geology layer dependency and verifies local,
geology and aviation click ownership; the standalone Intake Desk test supplies
its document/workspace context while retaining session-authentication checks.
No application guard or test expectation is relaxed.

## Repository candidate verification

The candidate uses a separate checkout from the pinned main and its own
frozen-lock installation. Hosted CI and human review remain separate from local results.

| Candidate check | Result |
| --- | --- |
| `npm run install:ci` | PASS; existing manifest and lock unchanged |
| `npm run build` | PASS; public containment checks pass |
| `tsc --noEmit` | PASS |
| `node --test tests/*.test.mjs` | 1,473 passed; zero failed, skipped or cancelled |
| `git diff --check` | PASS |
| Independent bounded source/diff review | No blocking issue found |

The first fresh-main suite exposed one inherited test setup failure:
`document is not defined` in the unchanged standalone Desk test. Its source and
test were identical to the pinned base. Providing the required document context
and covering the operator session handshake repairs the harness without changing
Intake Desk production code or relaxing session checks. The complete candidate
suite above passed after this correction.

The build retains warnings for large client chunks and runtime deprecation /
experimental APIs. No bundle-performance improvement is claimed. Dependency
manifests and the lockfile are unchanged.

## Earlier browser evidence and its limits

A preceding owner-checkout build passed its production build, TypeScript and
1,472 Site tests. Its browser flow was checked at 1440 × 900 and 390 × 844:

1. **Status failure — PASS:** a temporary catalog-request block produced an
   explicit error and an enabled retry button instead of indefinite checking.
2. **Retry and restored catalog — PASS:** removing the block and choosing retry
   restored the catalog. Capture remained held in disposable empty storage.
   The phone document had no horizontal overflow.
3. **Archive navigation — PASS:** Daily capture & archive opened its real page
   and owner-access boundary. No capture or settings change was performed.

These are bounded screenshots and interaction checks of that owner-checkout
build, not exact-candidate rendered/WebGL proof. Temporary network blocking and
viewport overrides were removed and the preview stopped. The error components
have executable behavior tests; an actual rendered application crash was not
induced. Full accessibility, every-source, long-session and hosted acceptance
remain unverified.

## Delivery and rollback

The six pre-existing edited files in the owner checkout remain byte-identical
and are not copied into this change. Main already contains the geology marker
integration used by the revised map test. The original owner checkout is not
reset, synchronized or replaced to prepare this candidate.

No merge, deployment, source admission, governed-data activation, production-data
change or installed-service replacement is performed. The configured Sites
project returned `NOT_FOUND` to this session; GitHub review and hosted delivery
remain separate.

Revert this focused repository change or apply an equivalent forward fix to undo
these source changes. Preserve separately held owner work and existing data.
No database migration or dependency-input rollback is required.

Before a hosted release, reconcile with the latest accessible source for the
same preserved Site, run release-acceptance scenarios, and record deployed and
public behavior independently from local results.
