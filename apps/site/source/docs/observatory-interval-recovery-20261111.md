# Observatory interval loading can recover from stalled reads

This follow-up starts at main `b4c07171560e19f8d72690dcaee03876f8b0e70e`,
including the merged replay inspection and Flight/Zod dependency corrections.

## Reproduction and behavior

The actual interval-loading callback waits for manifest headers and JSON, then
optional selected-station headers and JSON. Neither wait had a client deadline.
A stalled read left the primary action at “Reading archives…” with replay
controls disabled and a full-day calendar check still pending. A private radar
fallback could also wait indefinitely for browser file storage.

Each manifest or station read now has a thirty-second deadline through body
completion. This leaves room for the existing parallel eighteen-second archive
and twenty-five-second station upstream budgets. Verified private radar fallback
remains available after a provider failure, with a separate fifteen-second wait
for the local index. Browser file storage cannot be cancelled; its late result
cannot publish status or data after the load is cancelled or times out.

A manifest failure restores “Load exact interval” and marks a full-day check
failed, without claiming empty coverage. An optional station timeout retains the
loaded manifest, withholds river observations, and marks the full-day result
partial. The source message explains retry. Existing exact-frame cache checks,
generation guards and committed-record inspection remain in place. Superseding
an interval cancels its outstanding read; unmount cancellation releases timers
without publishing a failure or fallback.

## Verification boundary

Focused regressions execute the real interval callback and primary-button JSX.
They cover stalled headers and bodies, retry, late success, optional river
failure, exact local fallback, stalled file storage, supersession, unmount,
already-cancelled work, HTTP failure and true zero. Native Node fetch also reads
real loopback HTTP stalls and verifies that cancellation closes each connection.
These are automated lifecycle and local transport checks, not browser or provider
observations. The manifest regressions fail against the unchanged base callback
because it installs no finite read deadline.

Build/containment and nonincremental types pass. Lint has zero errors and 77
inherited warnings. All 1,804 Site tests pass; the bounded conformance suite
passes 380 checks, including 79 mirror checks. Disposable local smoke passes
110 checks across 79 routes; fourteen provider-only routes remain unexercised.
Selected parity passes for 949 files with all 262 withheld carriers absent.
These results use Node 22.13.1 with a clean exact-lock installation.

Browser acceptance remains pending:
the available browser tool could not create a test tab. No screenshot or hosted
acceptance is claimed. Temporary verification servers are stopped after checks.

## Inventory and rollback

The append-only interval-recovery receipt succeeds the exact Zod receipt.
Historical receipts, Site identity, source mappings, all withheld carriers and
pending source/overlay review remain. Current-byte parity is CONTENT_PARITY_ONLY;
human acceptance and hosted equivalence remain false. Application implementation,
regression and documentation stay in the existing Site mirror; receipt, selector
and QA stay in their established roots under ADR-0029 and ADR-0048.

Revert the interval callback/helper, regression, note and successor selector/QA
as one unit, retaining immutable receipt history. This restores the unbounded
loading behavior. No operational store, provider, access, dependency, admission,
activation, merge, deployment or publication change is included.
