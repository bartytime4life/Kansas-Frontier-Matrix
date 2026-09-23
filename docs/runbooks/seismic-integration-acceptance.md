<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/seismic-integration-acceptance
title: Seismic integration implementation and acceptance handoff
type: runbook
version: v0.1.0
status: branch-implementation; source-and-hosted-acceptance-held
owners: ["@bartytime4life"]
created: 2026-09-23
updated: 2026-09-23
owning_root: docs/
responsibility: Operate and verify the bounded history driver, local catalog preview and workbook preflight without treating them as admitted or deployed data.
truth_posture: CONFIRMED scoped local implementation tests; PROPOSED operational integration; NEEDS VERIFICATION exact-head hosted and independent acceptance
policy_label: public; context-only; local-preview; no-source-admission; no-release
[/KFM_META_BLOCK_V2] -->

# Seismic integration implementation and acceptance handoff

## Delivery and evidence

Base: `bartytime4life/Kansas-Frontier-Matrix@21eee8dab4637da4771267078fe963f6525b045f`.
Branch: `agent/kfm-seismic-integration-20260923`. Delivery is **VALIDATED_BRANCH_ONLY**
under the current #4024 PR-state incident. No ready transition, PR creation,
owner bypass, merge, release, deployment, audience change or source activation is
performed. #4228 Stage 1A accepted / Stage 1B HOLD / Stage 2 unauthorized remains.

This follows the [existing USGS helpers](usgs-earthquake-live-history.md), the
[KGS/Berkeley source qualification](../intake/exploratory/kgs-berkeley-seismic-source-map.md)
and [context-feed repair](explorer-context-feed-repair.md). Those dated records
remain valid for their original slices. This companion supersedes only their
statement that no supplied-reader history pagination/reconciliation driver exists;
it does not clear their HTTP, custody, source, active-caller or hosted-map gates.

**Implemented here:** an executable source-specific history driver with an injected
reader; a browser-local USGS-format file inspector connected to the existing
Import utility; and a read-only OOXML workbook preflight. These are distinct
boundaries, not an end-to-end released earthquake service. The history driver does
not feed its internal captures directly to the public client.

No full checkout was available: container GitHub DNS failed. The unchanged parser
and bounded JSON dependency were reconstructed and matched to their Git blob SHAs.
The existing waveform panel matched its base blob before the composition-only edit.
Local results cover this partial source projection, not the entire application.

## Run the history driver

Implementation: [`earthquake_history.py`](../../connectors/usgs/src/usgs/earthquake_history.py).
Its `acquire_history(start, end, reader, ...)` orchestrates actual calls to the
supplied reader; it does not create an HTTP client or discover credentials.

`HistoryReader` receives a fixed HTTPS USGS `HistoryRequest` with URL, byte limit,
per-call timeout and redirects disabled. It returns `HistoryResponse` containing
exact body bytes, status, media type, final URL and actual retrieval time. Use the
[existing connectors-core transport boundary](../../packages/connectors-core/src/connectors_core/TRANSPORT.md)
and artifact handoff for any separately authorized network adapter. Do not add a
second generic HTTP stack or interpret a reader callback as source activation.
Hard stream/deadline limits and authentication must be enforced **inside the reader**;
the driver's before/after cooperative deadline cannot interrupt a blocking callback.

For each finite interval the driver requests a plain-text count, bounded GeoJSON
pages and a second count. Overfull intervals split at millisecond precision. Each
page must have the expected cardinality, ascending event times, unique identities
and aliases, and correct event type, bounds and inclusive query-time membership.
Ownership remains `[start, end)`, avoiding duplicate boundary events. A zero count
still requires a genuine empty query response. Query 204, provider errors and count
204 are not interchangeable.

The whole selection is acquired twice. `TWO_PASS_MATCH` means the same selected
IDs and normalized feature digests were observed in both passes. It **does not**
prove an atomic provider snapshot, complete detection, magnitude completeness,
historical knowledge at the original event date, deletion handling or independent
corroboration. Both `coverage=NOT_ESTABLISHED` and `admission=NOT_ADMITTED` remain.
Stable count plus matching pages cannot rule out every intervening provider change.

Any mismatch, duplicate identity, saturation, transport/HTTP/media/JSON problem,
cancellation or exhausted budget returns `HELD` with no candidate event projection.
Do not replace a prior snapshot with that empty tuple. Bounded returned captures
remain available internally, including failed HTTP/media responses; oversized or
malformed response containers are refused rather than retained beyond the budget.
Captures and raw features must not be printed in public diagnostics.

Defaults: 1,000 events/page, 128 requests total across both passes, 20,000 selected
events, 32 MiB retained response bytes and a 120-second cooperative run deadline.
No scheduler, retry loop, persistence, publish pointer, tombstone processor or
source registry entry is installed.

## Inspect a catalog file in the existing Explorer

The existing Import utility's `WaveformPreviewPanel` now composes the independent
[`SeismicSnapshotPanel`](../../apps/kansas-frontier-matrix-explorer/app/seismic-snapshot-panel.tsx)
as a closed disclosure before its unchanged waveform controls. The old component
name/path is retained for caller compatibility, not made a new seismic authority.
No third app, dashboard or renderer is introduced. Component composition is
source-verified; real React/browser and hosted acceptance remain unperformed.

Open **Import**, expand **Earthquake catalog file inspection**, enter a start date
and an excluded end date in UTC, then choose a permitted local USGS-format GeoJSON
file. The file must be at most 8 MiB and 10,000 supplied records. The Kansas context
envelope is fixed and visible, not a legal state/county boundary. No provider is
contacted; no URL input, upload, cache, clipboard export or automatic startup data
exists in this utility.

The [preview parser and session](../../apps/kansas-frontier-matrix-explorer/app/seismic-snapshot-preview.ts)
retain IDs, separate origin/update/generation/inspection clocks, zero or negative
magnitudes, null optional values, magnitude method and depth in km. Depth is not
passed as a surface altitude. The exact-file digest is calculated from a defensive
copy. Unknown properties do not enter the displayed projection. Supplied, matching
and excluded counts remain separate; only the first 200 matching rows are listed.

All results say **UNVERIFIED_LOCAL_FILE / NOT_ADMITTED**. USGS-shaped fields and a
hash do not authenticate provider origin or establish scientific/schema conformance.
This uses the existing bounded JSON decoder; it is not a canonical JSON validator
or a KGS workbook parser. It creates neither map geometry nor EvidenceBundle/report
evidence. Original files remain the operator's responsibility; the preview retains
only transient inspected state, not a custody archive.

Successful replacement clears prior selection, including populated -> empty ->
populated. A failed import may retain the previous **same-window** preview with
`STALE_PREVIEW` wording. A changed window, clear action or unmount invalidates old
work. Late results and replayed completion tokens cannot restore cleared state.
These are local-import recovery semantics, not a claim that existing live feeds or
durable snapshot caches were repaired. Cached real observations must never be
reclassified as synthetic; no synthetic fallback is added.

## Inspect the KGS workbooks without inventing their schema

The [KGS historical page](https://www.kgs.ku.edu/Geophysics/Earthquakes/historic.html)
again exposed separate recorded-earthquake and felt-report downloads. The web
reads and attempted download did not yield workbook bytes. No source header, row
count, date range, coordinate meaning, workbook digest or rights clearance is
claimed. No catalog form or email request was submitted.

The new [read-only inspector](../../tools/ingest/inspect_seismic_workbook.py) can be
run on a legitimately obtained file outside the checkout:

```bash
python tools/ingest/inspect_seismic_workbook.py /absolute/path/to/recorded.xlsx \
  --kind recorded-earthquakes --header-row 1
python tools/ingest/inspect_seismic_workbook.py /absolute/path/to/felt.xlsx \
  --kind felt-reports --header-row 1
```

These paths are command examples, not repository placement or downloaded files.
The supplied kind and candidate header-row choice are labels for review, not
source-derived facts. The tool reports the exact-byte digest, sheet names, actual
XML row/cell counts, candidate header literals/types, formula-cell counts and
external-relationship counts. XML row counts are **not event counts**. Numeric/date
cells are not converted to UTC, coordinates or earthquake measurements.

The inspector never extracts ZIP members, evaluates formulas, follows external
relationships, executes macros or normalizes domain observations. It refuses
active embedded content, unsafe/duplicate member names, leaf symlinks in the CLI,
oversized/overexpanded archives, unsupported XML declarations and malformed cells.
Parent-path security, full OOXML conformance and custody-store admission are not
proven by this CLI. Do not expose it as a public upload endpoint. Header literals
can contain source text: keep the report internal until disclosure review.

Exit 0 means inspection ran and returns **REVIEW_REQUIRED**, not an admission PASS.
An error exits 1 without echoing a private input path. Real files may legitimately
require a separately reviewed expansion of this narrow OOXML profile; never loosen
limits merely to turn a held file into accepted data.

## Placement and compatibility

Basis: [adopted Directory Rules](../doctrine/directory-rules.md) and
[accepted ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md).
The older Directory Rules PDF is lineage; current adopted ownership governs.

| Artifact | Owning root and scope |
|---|---|
| USGS driver and adjacent tests | Existing `connectors/usgs/` importable helper/test lane; no competing earthquake connector root. |
| Preview parser, panel, composition and test | Existing `apps/kansas-frontier-matrix-explorer/`; browser-local inspection only. |
| Workbook preflight | Existing `tools/ingest/`; no fetch, normalization or disputed KGS connector placement. |
| Workbook tests | Existing `tests/ingest/`; generated-in-memory synthetic OOXML only. |
| Python check wiring | Existing `.github/workflows/usgs-earthquake-offline.yml`; read-only and no provider access. |
| Handoff | Existing `docs/runbooks/`; behavior-linked operation and acceptance guidance. |
| Authoring provenance | Existing `data/receipts/generated/`; append-only process record, not source/evidence/release authority. |

The Python workflow includes this exact feature branch to support branch-only
checks without creating a PR. The existing Explorer `npm test` wildcard collects
the new `.test.mjs` file after its normal locked application build. No dependency,
lockfile, package manifest, required check, ruleset, source schema, policy,
registry, catalog baseline or historical receipt is changed.

## Validation and remaining acceptance

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover \
  -s connectors/usgs/tests -p 'test_earthquake_history.py' -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover \
  -s tests/ingest -p 'test_seismic_workbook.py' -v
# With the existing Explorer locked dependencies installed:
node --test apps/kansas-frontier-matrix-explorer/tests/seismic-snapshot-preview.test.mjs
```

Local candidate: **31 history tests + 17 workbook tests + 36 preview tests passed**,
with zero skips. Python 3.13.5, Node 22.16.0 and available TypeScript 5.8.3 were used.
Strict TypeScript checking passed for the new non-React preview module and its
unchanged bounded JSON dependency. The panel was syntax-transpiled and its source
composition checked; this is not React type/build, DOM, accessibility or WebGL proof.
The declared Explorer TypeScript 6.0.2 toolchain was not installed. The original 25
USGS tests and full-repository suites were not rerun locally. Read exact-head hosted
results independently; configured workflows are not passing checks.

Remaining dependencies, in order:

1. Obtain current native Sites source, archive/bindings/audience identity and saved
   predecessor. Old v40/v53 coordination checkpoints are not current runtime proof.
   Reconcile the monorepo and active source without importing a standalone tree
   over `main` or replacing the existing Site.
2. Bind a reviewed SourceDescriptor/activation/rights decision to the existing
   connectors-core transport and custody handoff. Verify real provider requests,
   finite deadlines, raw retention, revisions/deletions and correction behavior.
3. Obtain and inspect the real KGS files, then implement separate exact-schema
   recorded-event and felt-report adapters. Treat stations/seismogram links and
   NCEDC comparison/waveforms as separately qualified source products.
4. Close normalized records -> EvidenceBundle -> policy/review/release -> governed
   API -> map/list/Evidence Drawer. Preserve the intended 30-day Present versus
   explicit historical window; do not substitute this preview or a one-day helper
   default. Public clients still do not read RAW or unreleased captures.
5. Prove same-candidate populated/empty/error/stale/retry rendering, selection,
   keyboard/narrow-screen behavior and rollback with the actual hosted source.
   Only then extend county profiles, stories, cross-catalog associations and
   contextual geology/infrastructure comparisons. Proximity is not causation.

## Rollback

Before integration, abandon the isolated branch. After a separately approved
merge, use a reviewed inverse of the eight added implementation/test/doc files and
two existing-file edits; retain the generated receipt as historical process evidence.
Removing the panel composition restores the prior Import utility without changing
waveform parsing or stored data. There is no database migration, persistent browser
state, admitted source or hosted deployment to undo from this candidate. A saved
Site predecessor is still only a recovery candidate until rehearsed.
