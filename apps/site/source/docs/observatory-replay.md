# Replay and inspect a dated interval

This guide describes repository source at main
`d4d84171653a2f2582b48ece511dc010857fde15` on November 11, 2026. Provider coverage,
browser acceptance, installed copies and hosted deployments have separate checks.

## Load a day

1. Open **Observatory** (`/observatory`). Choose an exact UTC start and a one-,
   six- or twenty-four-hour window, then choose **Load exact interval**.
2. Use **Calendar**, **Load full 24 hours**, or the adjacent-day controls to
   inspect another UTC day. Dates since 1800 are accepted by the interval model;
   that does not imply that every source has records for them.
3. Enable the layers you need. Use **Sources & quality** to inspect their clocks,
   coverage and limitations. Modern reference maps remain modern backgrounds.
4. For selected-station discharge, enter a supported `USGS-` station identifier.
   **Continuous samples** and **Daily means · older archive** describe different
   temporal support. A daily mean does not create hourly observations.

**Follow today / latest** returns to the current UTC day and safe latest cursor.
Automatic follow refresh checks five-minute elapsed time while the page is visible
and idle; choosing another interval stops following today. This is a refresh rule,
not a guarantee of provider observation freshness.

## Read the current record

Select a map feature, then move the replay cursor. The inspector resolves that
selection against records committed for the current frame. It shows an updating,
hidden or unavailable state while the corresponding record is not usable; old
clicked values are not substituted. Missing or ambiguous records stay unresolved.

Weather daily summaries remain bound to their date. Trace precipitation, presumed
zero and missing or quality-withheld values retain their qualifiers. River values
retain their own observation time, units and quality; a reported numeric zero is
distinct from a missing sample. County editions, station operating epochs and
individual storm-scan identities keep their separate clocks.

## Recover a load

| Visible state | What to do | What it means |
|---|---|---|
| **Reading archives…** | Allow the source check to finish | Each manifest or station read has a thirty-second deadline covering headers and body completion |
| Archive check took too long | Choose **Load exact interval** again | Coverage was not confirmed; a full-day check is failed rather than empty |
| River observations took too long | Reload the interval to retry the selected station | Other loaded replay sources remain usable; river observations are withheld and full-day coverage is partial |
| Reading saved radar frames took too long | Retry the interval or inspect the private cache separately | The local-index wait is bounded to fifteen seconds; it is not proof that saved coverage is empty |
| Selected record updating or unavailable | Wait for a committed frame, check the layer, or choose another record | A selection does not authorize stale displayed readings |

These budgets apply to separate reads, rather than one thirty-second total load.
When radar replay cannot read a provider listing, an exact verified private cache
may supply the interval. Its status states that other sources were not checked.
Superseded responses and late file reads cannot publish into the new load.

## Share and retain context

**Share replay** uses the committed replay position. A replay link identifies
requested context; it does not capture or release provider bytes. Main-map saved
investigations and share links have their own [research workflow](map-research-tools.md).
Private captures, local cache files and reviewed downloads retain their separate
identity and rights/review boundaries.

## Implementation and evidence

- [Interval model](../app/event-atlas.ts), [workspace](../app/observatory/workspace.tsx),
  [read deadline](../app/observatory/load-deadline.ts) and
  [committed inspection](../app/observatory/inspection.ts).
- [Replay-record correction](explorer-replay-record-integrity-2026-11-10.md) and
  [interval recovery correction](observatory-interval-recovery-20261111.md).
- [Actual load regressions](../tests/observatory-load-recovery.test.mjs) and
  [frame/inspector regressions](../tests/observatory-inspection-frame.test.mjs).

The recorded build, test and loopback HTTP results do not establish live-provider
coverage, scientific accuracy, complete browser/device acceptance or publication.
[All Explorer documentation](README.md).
