<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/land-full-county-records-20261014
title: Complete county land-result transcription and current source alignment
type: report
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-10-14
updated: 2026-10-14
policy_label: public
owning_root: docs/
responsibility: Record full-column private source transcription, provenance, validation and bounded GitHub source alignment.
truth_posture: "CONFIRMED private intake and browser observations; independent review, source admission and release remain PENDING."
related:
  - docs/runbooks/land-records-ingest.md
  - contracts/domains/people-dna-land/land_instrument_candidate.md
  - data/receipts/generated/site-v267-land-full-records-20261014.json
tags: [land, county, source-integrity, private-review, github]
[/KFM_META_BLOCK_V2] -->

# Complete county land-result transcription

The signed-in main KFM app accepted a new unredacted bundle with **394 unique
candidate versions**: 294 retained BLM instrument entries, 99 Shawnee County
result units, and one archive record. The county transcription includes all
printed purchaser labels, separate Deed labels, tract/parcel references, liens,
court costs, taxes and purchase prices in the two selected official PDFs.
The original PDFs and all preceding partial captures remain retained. No source
fields were redacted. Missing legal descriptions, acreage, court confirmation
and current ownership are not invented.

[Shawnee County's official result page](https://snco.gov/counselor/prior_tax_sales.php)
links both originals. All five pages of the September 24, 2025 result table
contain 73 result units covering 79 tracts, including two explicitly invalidated
rows. Its printed totals reconcile exactly: liens USD 1309426.45, court costs
USD 38500.00, taxes USD 1270926.45, and purchase prices USD 996440.00.
All seven pages of the June 10, 2026 table contain 26 units covering 108 tracts:
liens USD 8115747.81, court costs USD 54000.00, taxes USD 8061747.81, and
purchase prices USD 690200.00. Prices remain once per sale unit. Combined tract
financial rows remain combined; no group price is allocated to individual parcels.
Purchasers and printed Deed labels remain distinct source assertions.

The new `transcribe-shawnee` operation retains an explicit operator JSON
transcription, CSV and mapping in the existing private WORK lane. It checks
unique units/tracts, parcel counts, all financial identities, printed document
totals, types and text budgets before output. It does not infer PDF fields.
The ordinary bounded capture/normalize/stage/import pipeline still supplies the
original-document closure, deterministic identities and immutable receipts.
Operator JSON is never labeled as an original downloaded document.

The copied private ledger passes replay/integrity audit for 436 historical
versions and ten runs. Two superseded partial county captures were withdrawn
only in this working copy; their original bytes, receipts and the preceding
hosted submission remain available for correction and rollback. Seven active
captures export 419 occurrences, deduplicated to 394 versions, in **4351222
encoded bytes**. The main app's authenticated import and read verify object
hashes and graph closure. Focused browser observations verify all 99 county
units, distinct purchaser and Deed labels, printed parcel/financial fields,
and original-document download links. Independent transcription review remains
pending; financial reconciliation is not independent approval.

## GitHub and saved source identity

Authoring starts at current GitHub main
`b71d52766707b2676492df72c9551d8fcda73f17`, after owner merge of PR #5165.
The newest same-Site saved source is v267,
`8b4c03a5ba2c803d1f323460a23778adc8e4c76b`, project
`appgprj_6aa0b1c41bc08191bfd86003920f1631`. The native version readback returned
no deployment ID for v267. This change aligns that saved source without
claiming it is the live deployed version or deploying unrelated connection work.
The land bundle was imported through the existing live application.
Owner-only access, storage bindings, recent performance work and saved source
history remain preserved.

The new append-only content receipt binds 865 comparison paths: 858 identical,
five inherited repository security overlays and two repository-only tests.
Canonical tool/document aliases and 258 previously withheld location carriers
remain intact. Those pre-existing holds are outside this land-source request.
The selector checks content parity only; receipt review and human acceptance
remain pending. No data bytes or real-party fixtures are committed to GitHub.

Saved source v267 adds two connection API routes and migration 0010. The local
launcher initially rejected that published non-idempotent CREATE syntax. A
hash-bound temporary local replay adds only IF NOT EXISTS, following the existing
daily-archive mechanism. Original migration bytes remain unchanged. Changed
source hashes and unknown nonadditive migrations are still refused. Verification
uses disposable local D1/R2; no hosted storage migration or provider activation
is performed.

## Authority, placement and rollback

Accepted ADR-0029 and Directory Rules sections 10, 11 and 14 place source
transcription in the existing county connector, operational commands in the
existing local-data tool, tests in the established domain/QA lanes, and the
deployable source projection in the existing Site mirror. This report owns
implementation evidence only. No parallel schema, source registry, normalization,
policy or release authority is created.

Free access does not automatically certify source-specific copyright or
sensitivity. [BLM's policy](https://www.blm.gov/info/notices/drctp-policy) states
that most of its content is public domain and identifies exceptions. The private
workspace shows the retained fields and originals without redaction. Rights,
source admission, sensitivity assessment, independent review and public release
remain separate required checks. No public map/API release or source activation
is implemented; Kansas and BLM keyword coverage remain partial.

Rollback selects the retained preceding hosted bundle, keeps all originals and
reviews, and reverts this source/CLI/mirror/launcher change. The earlier local
ledger is preserved separately. Do not delete source bytes, rewrite historical
receipts, reset persisted storage or deploy an older Site as a data correction.

## Changed-area validation

The aligned app passes TypeScript, production build and all 1345 Node tests.
Required lint has zero errors and 76 warnings. The source/ingest/ledger/transfer
suite passes 65 tests; mirror integrity passes 38; local startup and source-bound
migration replay pass six. The full backend smoke passes 112 checks across 79
routes, with nine provider-only routes explicitly excluded. Topology passes with
zero invariants, zero new drift and 93 inherited warnings; no waiver was broadened.
The original failed startup was attributable to source migration 0010 and is
resolved by the hash-bound local replay. Hosted exact-head GitHub checks remain
pending until the new review branch is pushed. No unrun source-only or broad
browser/device checks are represented as passing.
