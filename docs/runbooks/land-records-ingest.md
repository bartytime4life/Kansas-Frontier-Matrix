<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/land-records-ingest
title: Kansas land-record intake and private review
type: runbook
version: v1.2
status: draft
owners: ["@bartytime4life"]
created: 2026-10-13
updated: 2026-10-14
policy_label: public
owning_root: docs/
responsibility: Operating instructions for explicit land-instrument acquisition, quarantine intake, private review and rollback; no source admission or release authority.
truth_posture: "CONFIRMED private intake implementation; source admission, rights, sensitivity, independent review and publication remain PENDING."
related:
  - contracts/domains/people-dna-land/land_instrument_candidate.md
  - apps/land-records/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [land-records, private-intake, blm, archive, evidence, rollback]
[/KFM_META_BLOCK_V2] -->

# Kansas land-record intake and private review

Import individual official land-record exports into a private, evidence-bound
review store. The intake retains instruments and their source assertions. It
does not decide current ownership, complete a chain of title, infer market
prices, geocode legal descriptions or release person-bearing records.

## Source access verified during implementation

| Source | Supported intake | Authority and remaining limits |
|---|---|---|
| [BLM GLO](https://glorecords.blm.gov/s/) | Captured rendered Kansas result-card text; explicit mapped CSV | Federal instrument/index evidence. July 2026 portal replacement means old ASP.NET/SOAP instructions are not a verified bulk interface. The expanded capture includes 294 instrument candidates across three 100-card keyword pages, spanning 1858–1951. Six survey cards remain excluded. Patent accessions are retained where supplied; original patent images are not acquired. |
| [BLM MLRS public reports](https://reports.blm.gov/reports/MLRS) | Explicit lawfully exported CSV, mapped by the operator | Public reports retain Privacy Act redactions. Land-tenure cases and proposed sales are separate from completed conveyances and mineral leases. Actual MLRS export columns and live ingestion require source-specific verification; this pilot contains no MLRS rows. |
| [Kansas State Archives](https://www.kansashistory.gov/p/land-records-at-the-state-archives/11083) | Explicit ledger/tract-book transcription CSV plus original image/document | Historical individual land transfers and railroad sales. Original bytes and row locators are attached; transcription remains pending independent review. Archive access does not settle redistribution rights. |
| [Sedgwick Register of Deeds](https://www.sedgwickcounty.org/register-of-deeds/online-land-record-search/) | Lawful county CSV with explicit column map | Free in-person computers; online Laredo/Tapestry access uses subscriptions or per-search charges. No purchase, account creation, credentialed search or county download occurred. |
| [Johnson County](https://www.jocogov.org/department/treasury-taxation-and-vehicles) | Lawful county CSV with explicit column map | Bulk export fields, permission and coverage need verification. Assessor/AIMS parcel data does not prove title or substitute for an instrument. No county records acquired. |

Kansas sales-validation questionnaires are **excluded**. Their access is
restricted by [K.S.A. 79-1437f](https://www.ksrevenue.gov/pdf/PVDRSStatutes.pdf).
The county adapters are for lawful deed exports; a supplied file or source URL
does not establish lawful access, authenticity, rights or review acceptance.
Add another county/state only with a verified source profile, host identity,
field mapping, source-role bounds and tests. Kansas is the current enforced
scope; no nationwide completeness is asserted.

## Quick start

Use Python 3.11 or newer. The operational CLI and runtime use the standard
library and bundled source modules; no host service, account, database server,
model runtime or global package installation is required.

From the repository root, choose a **fresh private directory outside Git**:

```bash
python3 tools/local_data/land_records.py --root /absolute/private/land-store init
python3 tools/local_data/land_records.py --root /absolute/private/land-store import \
  --source blm-glo --format glo-text --file /absolute/captured-glo-page.txt \
  --url 'https://glorecords.blm.gov/s/advanced-search?searchTerm=%2Fsearch%3Fq%3DKansas%26page%3D1%26pageSize%3D25' \
  --retrieved-at 2026-10-13T20:00:00Z
python3 tools/local_data/land_records.py --root /absolute/private/land-store audit
python3 tools/local_data/land_records.py --root /absolute/private/land-store status
python3 apps/land-records/server.py --root /absolute/private/land-store --port 5271
```

The timestamp above is an example: use the actual UTC capture/export time.
The runtime creates a private `.review-token` file inside the store and binds
only to `127.0.0.1`. Open its printed `/review` URL and paste that key into the
password field. The key stays in tab memory, never a URL, cookie or browser
storage. Do not put it in Git, logs or shared screenshots. Close the runtime
with Ctrl+C; stop the process before removing its token file to rotate access.

For a mapped export, provide a JSON object mapping KFM fields to exact source
column names. The required fields are `source_record_id`, `instrument_type`,
`event_date`, `state` and `transaction_status`. Dates use ISO calendar dates;
Kansas uses `KS`. Amounts are decimal strings with an explicit amount role and
`USD`, with no automatic currency-symbol removal or inferred sale price.
See [the instrument contract](../../contracts/domains/people-dna-land/land_instrument_candidate.md).
Mapping is an operator interpretation and always awaits review.

```json
{
  "source_record_id": "DocumentNumber",
  "instrument_type": "ReviewedInstrumentType",
  "event_date": "ISOInstrumentDate",
  "state": "StateCode",
  "transaction_status": "ReviewedRecordStatus",
  "county": "County",
  "grantor": "Grantor",
  "grantee": "Grantee"
}
```

These column names illustrate the mapping interface; they are **not** a claim
about a county or BLM export format. Preprocess an actual permitted export into
reviewable, explicitly typed columns when the original uses different codes.
Retain the original as an attached document, and record the transformation in
notes. Do not guess missing prices, dates, types or identities.

```bash
python3 tools/local_data/land_records.py --root /absolute/private/land-store import \
  --source kshs-land-sales --file /absolute/transcription.csv \
  --mapping /absolute/columns.json --url 'https://www.kansashistory.gov/p/land-records-at-the-state-archives/11083' \
  --document /absolute/original-image.jpg --document-url 'https://www.kansashistory.gov/path/from-the-official-source.jpg' \
  --retrieved-at 2026-10-13T20:00:00Z
```

Use an actual official document URL. The archive adapter requires original
document bytes; it does not run OCR or automatically approve a transcription.
`connectors/kshs/land_records.py::fetch_document` provides an optional bounded,
HTTPS host-locked download with no redirects. No GLO bot-block workaround or
authenticated MLRS export is implemented.

## Limits and performance

The default import allows **100 records and 2 MiB total input**, including
attached documents. An explicit `--max-records` or `--max-bytes` can raise those
limits up to **1,000 records and 10 MiB**. The whole import is refused if it
exceeds its budget; it never silently truncates records. A captured GLO page
must agree with the observed 10/25/50/100-result page scope and consistent visible card/range counts. It
retains the upstream match count and whether extra legal-description rows were
hidden. Keyword results are not a verified Kansas state-boundary query.

Exact replay is idempotent. Changed record content creates another immutable
version for the same source record ID. GLO CDI lacks a captured globally unique
document ID, so its composite identity is explicitly flagged; it is not a
verified document identity or cross-source person/parcel match.

SQLite has date, source, county and instrument indexes. Filters use bound
parameters; pagination uses `(event_date, record_digest)` with a 25-row default
and a 100-row ceiling. No bulk candidate payload, geometries or parties are
loaded by an ordinary public map client. The existing Explorer rendering and
provider caches are outside this change.

## Runtime boundaries

| Route | Behavior |
|---|---|
| `/healthz` | Liveness only; no candidate data |
| `/review` | Static administrative review shell |
| `/review/v1/status` | Authenticated intake counts and date ranges |
| `/review/v1/records` | Authenticated filtered record-version pages |
| `/review/v1/evidence?digest=sha256:...` | Authenticated active capture evidence candidates |
| `/v1/land/records` | `403 DENY`, zero records; no release writer |

The private endpoints require the bearer key, reject external Host/Origin,
do not enable CORS, are read-only and return `private, no-store`. Request logs
omit URL filters, record content and credentials. Runtime startup performs
an integrity audit. The UI makes no external map/geocoder calls and uses safe
text rendering; precise parcel coordinates remain absent.

## Evidence, lifecycle and placement

`connectors/` owns source capture; reusable parsers, identifiers and private
store operations belong to `packages/domains/people-dna-land/`;
`pipelines/ingest/people-dna-land/land_records.py` orchestrates the stage;
`tools/local_data/land_records.py` operates it; `apps/land-records/` owns the
loopback review process. Machine contracts live under
`schemas/contracts/v1/domains/people-dna-land/`; human semantics under
`contracts/domains/people-dna-land/`; inactive SourceDescriptor candidates under
`data/registry/sources/people-dna-land/`.

This follows Directory Rules `DIR-EXEC-001..005`, `DIR-AUTHROOT-001`,
`DIR-SOURCE-003..004` and [accepted ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md).
The new stage-first implementation does not add a second implementation under
the existing `pipelines/domains/people-dna-land/land-ownership/` scaffold or move
that compatibility material. Existing legacy ownership schemas and proposed
domain source views remain unchanged; these adapters bind to the new inactive
canonical source profiles through the local keys `blm-glo`, `blm-mlrs`,
`kshs-land-sales`, `sedgwick-deeds`, `johnson-deeds`,
`shawnee-tax-sales` and `leavenworth-tax-sales`.

Source admission is pending, so original objects, capture manifests, normalized
instrument candidates and EvidenceBundle candidates remain in
`data/quarantine/land-records/` in the **external private store**. The disposable
SQLite index is under `data/work/people-dna-land/land-records/`. Ingest and
withdrawal receipts use `data/receipts/ingest/land-records/` and
`data/receipts/pipeline/land-records/`. These are physical projections of the
existing responsibility/lifecycle homes, never deployment assets or fixtures.

Each record resolves to candidate EvidenceBundles containing source URL,
capture method/time, original byte hashes/sizes, card/CSV-row locators and
attached original-document identities. The audit recomputes object, capture,
candidate, record, bundle and receipt hashes and replays normalization against
the preserved bytes. These are **candidates**, not approved standard released
EvidenceBundles. No catalog, triplet or PUBLISHED transition occurs.

## Corrections and rollback

Correct bad capture metadata/content with a new import. Withdraw the previous
capture from the active review listing while retaining its bytes and receipts:

```bash
python3 tools/local_data/land_records.py --root /absolute/private/land-store withdraw-capture \
  --capture-id sha256:ACTUAL_CAPTURE_DIGEST --reason 'Explain the correction and replacement capture.'
```

Withdrawal is irreversible in this bounded private intake implementation;
import a corrected capture instead of toggling an old receipt back to active.
It changes no rights, approval or release state. Replaying an existing withdrawn
capture does not reactivate it. SQLite/file writes are ordered: an interrupted
transaction can leave unindexed immutable quarantine objects; exact replay
repairs the index. Preserve the whole store before operational recovery.
The audit verifies indexed runs, not a claim that every orphan is indexed.

To roll back the application, stop its process and revert the scoped code PR.
Keep external captures/receipts intact. The main Site integration adds private quarantine submissions to its existing
D1/R2 bindings; source synchronization performs no migration, reset or reseed.
No system service, DNS, hosting audience, model binding or public data release
is changed. No timed
acquisition schedule is created; explicit imports are the current job runtime.

## Verification and next gates

Run the synthetic regression suite with repository test dependencies:

```bash
python -m pytest -q tests/domains/people-dna-land/test_land_records.py
```

The dedicated CI job runs the same source, integrity and runtime guards with
the existing hash-locked dependency installer. The retained expansion has 337 unique candidate versions: 294 BLM instrument
entries, 42 Shawnee auction sale units from 2025–2026 and one KSHS railroad-sale
transcription. The 2026 Shawnee capture has 26 sale units covering 108 tracts;
their purchase prices reconcile to the printed $690,200 total. The 2025
capture is only 16 selected page-one sale units. Coverage is partial, and
auction reporting does not establish recording, court confirmation or title. Source admission, person/cultural sensitivity, rights,
independent review, released EvidenceBundle/citation validation, correction,
rollback and a separate exact-content release decision remain required before
any ordinary public API/map publication.

## Main KFM workspace and transfer

Open `/data/land-records` on the existing owner-private Explorer. Data commons,
Land topics and the map Data menu link to it. The application reuses existing
sign-in, owner/steward authorization, submissions, review history and quarantine
storage. It imports and checks a bounded evidence transfer, then filters and
paginates individual candidate versions and resolves original documents. It
does not call a workstation path or retain the local companion token.

```sh
python tools/local_data/land_records.py --root /absolute/private/land-store \
  export-review --output /absolute/private/land-review.json
```

Export selects active captures and deterministically replays their originals.
Repeated `--capture-id` flags select specific captures. The transfer remains
private, pending and unreleased, with a 10 MiB encoded limit, 20 captures and
1,000 candidate occurrences. Duplicate occurrences display once per record
digest; changed versions stay distinct. The Site checks hashes and closure,
while normalization, source authenticity, rights and sensitivity review remain
pending. No original payload, exact party/parcel records or tokens belong in
Git, static assets or deployment archives.

Shawnee's [official prior-sale page](https://snco.gov/counselor/prior_tax_sales.php)
links result PDFs with separate tax-liens, costs, purchaser/deed labels and
purchase prices. Only the purchase-price column is transcribed; multi-tract
sale prices are not allocated across parcels. `tax_foreclosure_sale` uses
`AUCTION_REPORTED` and `auction_purchase_price`, with original documents
mandatory. The inactive Leavenworth profile records a current TLS retrieval
failure; no Leavenworth original or records are claimed. Sedgwick and Johnson
remain lawful-export adapters without live acquisition.

The existing submission review states track administrative disposition only.
Restricted land bundles cannot be accepted merely by supplying a source URL.
Ordinary `/api/governed/land-records/v1/[view]` clients always receive a denial
and zero candidates. App rollback reverts the additive routes/navigation and
redeploys the preceding same-Site version while retaining private submissions
and receipts. The existing loopback runtime remains available independently.

## Complete Shawnee Exhibit B transcription

`transcribe-shawnee --file /absolute/operator-transcript.json` validates an
explicit operator transcription before import. It retains the input JSON,
mapped CSV and column map immutably in the existing private WORK lane. Its
output says `TRANSCRIBED_NOT_IMPORTED`; it neither downloads nor parses PDFs,
imports candidates, approves source admission, nor releases data. Import the
returned CSV and mapping with the official original PDF using the existing
`import` command. The operator transcription is WORK evidence; the PDF is the
original document. No operator JSON is misrepresented as a downloaded PDF.

The JSON has exactly `case_number`, `event_date`, `expected_tracts`, `totals`
and `units`. Totals contain `total_lien`, `court_costs`, `taxes` and
`purchase_price` as decimal strings with two places. Each unit contains
`unit_id`, `purchaser`, `deed_name`, `parcels`, `purchase_price`, `result`
and `pages`. Each parcel row contains `tract`, `parcel_id` (a list of printed
16-digit IDs), `total_lien`, `court_costs` and `taxes`. A combined printed
tract row uses a comma-separated tract string and its combined financial
values once. Explicit source result values are `PURCHASE_REPORTED` and
`INVALIDATED_SALE`; absent printed amounts are null, never invented zeros.

Every tract must be unique; parcel counts, lien = costs + taxes, tract totals
and all four printed document totals must reconcile. Purchaser and printed
Deed labels remain distinct. The source's Deed label maps to the existing
grantee assertion, with its exact label also retained in notes. This does not
establish a recorded deed, current ownership or court confirmation. Parcel
references are labeled as printed references, never surveyed geometry.
Financial fields and purchaser labels appear in notes without redaction.
Grouped purchase prices are retained once per sale unit and never allocated.
Unknown fields, duplicate JSON keys, incomplete rows and over-budget content
fail before any output; output is never silently truncated.

The October 14 full-column checkpoint represents all five pages of the
September 24, 2025 PDF: 73 units, including two invalidated rows, and 79 tracts.
Its purchase prices total USD 996440.00. All seven pages of the June 10, 2026
PDF contain 26 units and 108 tracts, totaling USD 690200.00. Both original PDFs
are retained without redaction. In the combined main-app bundle, 99 county
units plus 294 BLM candidates and one archive record yield 394 unique versions.
The bundle is 4351222 encoded bytes; statewide coverage remains partial.

Free access is an acquisition fact. [BLM's rights policy](https://www.blm.gov/info/notices/drctp-policy)
says most of its content is in the public domain and identifies exceptions.
It does not certify every source or clear person, cultural or location review.
The existing private workspace displays retained source fields and originals;
review gates do not redact those fields. Public-source status does not replace
the independent source, rights, sensitivity and release checks.
