# Reviewed source requests and exports

Repository candidate reviewed against main
`d58bd53a33bbe83a0f77dd98bc1b74a3d594aa7f` on November 11, 2026.
This guide applies to the water, daily weather, soil, earthquake and storm-event
map controls. Local controlled-transport checks establish component behavior;
they do not establish browser acceptance, provider availability, hosted release
activation or data admission.

## Response and release checks

Evidence reads and both export reads require successful HTTP responses before
parsing JSON. A failed response's body is canceled, even if it contains an
otherwise matching released package. This closes the missing HTTP check in the
soil, earthquake and storm-event controls and shares the existing water/weather
rule. Initial layer and bootstrap reads still interpret negative envelopes to
explain an unavailable or withheld release; they cannot enable an export.

Every successful export must still bind the selected station or month to the
same package, release, approval expiry and measurement evidence. Station exports
exclude other stations; monthly exports exclude other months and years. Existing
source times, trace/zero/null distinctions, quality flags and byte limits remain
part of the source contract.

| Read | Water / weather | Soil | Earthquakes / storm events |
|---|---|---|---|
| Layers, including export | 2 MiB | 2 MiB | 8 MiB |
| Evidence, including export | 512 KiB | 1 MiB | 8 MiB |
| Monthly bootstrap | Not used by these controls | Not used by this control | 256 KiB |

## Export ownership and recovery

An explicit export owns one 15-second deadline across the fresh layer request,
the evidence request and both response bodies. Abort signals reach the bounded
body readers, so a stalled stream cannot retain the checking state while waiting
for transport cleanup. A failed current export reports that it was withheld and
can be retried.

The pending export is canceled when the station or month changes, a release
recheck starts (manual or scheduled), the displayed approval expires, evidence is
withheld, or the control unmounts. Returning A→B→A does not revive the old export.
Starting another export cancels the previous one. A late completion cannot create
a download or replace the current view's export status, including after a newer
export succeeds. Valid current exports retain their existing filenames and full
source/evidence payloads.

## Verification

From `apps/site/source`:

```sh
node --test tests/governed-*-control.test.mjs tests/governed-water-export-selection.test.mjs tests/reviewed-control-request-integrity.test.mjs
npm run build
node --test tests/*.test.mjs
npx tsc --noEmit --incremental false
npm run lint
```

The request-integrity matrix covers all five actual components and model helpers,
successful payload preservation, failed HTTP responses at each export stage,
failed initial evidence, unmount/recheck/supersession at each stage, stalled body
cancellation without awaiting cleanup, and approval expiry. It uses copied
synthetic fixtures, controlled timers and transports, real response streams and
Blob downloads. It does not start a provider acquisition or use an actual browser
or map renderer. The family-specific tests retain package, measurement, year,
month and withheld-value conformance checks.

Visual review remains pending: the available browser automation failed before a
page or screenshot could be observed. No current visual or accessibility
acceptance is claimed. No Site synchronization, deployment, publication, release
activation, persisted data migration or source admission is included. To roll
back this candidate, revert the control/helper changes, tests, guidance and mirror
successor selector together while preserving historical receipts.
