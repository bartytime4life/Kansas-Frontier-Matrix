<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/land-workflow-integration-20261014
title: Kansas land workflow integration and bounded coverage expansion
type: report
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-10-14
updated: 2026-10-14
policy_label: public
owning_root: docs/
responsibility: Record bounded implementation, private intake, source alignment and remaining review gates.
truth_posture: "CONFIRMED implementation and bounded private browser observations; independent review, source admission and release remain PENDING."
related:
  - docs/runbooks/land-records-ingest.md
  - contracts/domains/people-dna-land/land_instrument_candidate.md
  - data/receipts/generated/site-v264-land-workflow-20261014.json
tags: [land, blm, county, site, evidence, quarantine]
[/KFM_META_BLOCK_V2] -->

# Kansas land workflow integration

The main owner-private Explorer now provides `/data/land-records`, linked from
Data commons, Land topics and the map Data menu. It imports an audited private
transfer, filters individual candidate versions, paginates results, resolves
original objects and retains the existing steward review history. Existing
D1/R2 quarantine bindings and authenticated owner/steward boundaries are reused;
no database migration, storage reset, reseed or additional access is introduced.
Ordinary governed land clients always receive zero candidates and a denial.

## Verified scope and source limitations

The private intake and live bundle contain **337 unique candidate versions**:
294 BLM instrument entries, 42 Shawnee tax-foreclosure sale units and one retained
Kansas State Archives railroad-sale transcription. The BLM expansion preserves
three 100-card keyword pages and excludes six known survey cards. Instrument
dates span **1858-10-01 through 1951-03-17**. These are partial keyword results,
not a complete Kansas inventory; patent/index metadata does not establish
present ownership or a sale price.

[Shawnee County's official result page](https://snco.gov/counselor/prior_tax_sales.php)
links the two retained original PDFs. The June 10, 2026 capture has 26 sale units
covering 108 tracts; purchase prices reconcile to the county's $690,200 total.
The September 24, 2025 capture includes 16 selected page-one sale units, so its
remaining pages are not represented. Multi-tract units retain their whole-unit
price. Purchasers, deed-name labels, legal descriptions and court confirmation
were not independently transcribed or established. `AUCTION_REPORTED` and
`auction_purchase_price` keep those bounds explicit.

The [BLM GLO portal](https://glorecords.blm.gov/s/) was verified in the browser;
provider access was not bypassed. Leavenworth's indexed official sale-results
source failed TLS retrieval in both the downloader and browser: its inactive
profile records that limit, with no original capture or record ingestion claim.
Sedgwick and Johnson remain lawful-export adapters without live acquisition.
Confidential Kansas sales-validation questionnaires and paid scraping remain
excluded. Rights, person/cultural/location sensitivity, source authenticity,
normalization review and source admission remain pending for every candidate.

## Source identity and validation

The application starts at same-Site v263 source
`902c1f5c60bb90ed215fc94fdeda6c1c0784834d`, retains its river-startup restoration
and recent rendering/cache work, and is privately deployed as v264 from
`2ad58f0a6a82e2a99aca4f9bf1d3faae2b154246`. Project identity is
`appgprj_6aa0b1c41bc08191bfd86003920f1631`; owner-only audience revision 1 and
environment revision 6 remain preserved. Private publication of app code does
not release imported land data.

The GitHub branch starts at `934be0688b41ebdc8d7aac5e5fcbeedde96863c1`.
Mirror content checks bind 831 paths: 824 exact paths, five inherited GitHub
security overlays and two repository-only overlay tests. Both canonical tool
aliases and two lowercase document mappings remain explicit. All 258 historical
precise-location carriers remain absent. The new append-only mirror receipt
retains `REVIEW_ONLY`, pending source/overlay review and human acceptance; passing
content checks do not evaluate those approvals. Historical receipts are retained.

Validation: production Site build, TypeScript and 1,246 Site tests pass; the
GitHub mirror passes TypeScript and 1,257 tests; 54 pipeline/source/transfer tests
and 38 mirror-validator tests pass. Topology reports zero invariant failures,
zero new drift and 93 inherited warnings. The private ledger audit verifies 337
versions across eight retained runs, including a previously withdrawn capture.
The live import retains seven active captures, 362 occurrences and **4,098,119
encoded bytes**; immutable record digests deduplicate 25 repeated occurrences.
The hosted boundary verifies integrity and closure, while normalization review
remains pending. Focused browser observations confirm signed-in persistence,
county filtering, grouped-price roles and original evidence. Broad device,
accessibility, provider and independent review acceptance remain separate.

## Placement and rollback

Directory Rules sections 10.1, 11.4 and 14 with accepted ADR-0029 place deployable
UI/adapters under the existing Site, canonical reusable normalization/transfer
logic in the domain package, source acquisition in county connectors, orchestration
in the existing ingest pipeline, shapes/semantics in schema/contract roots, and
inactive source profiles in the canonical registry. Private physical bytes remain
outside Git. The application projection is integrity-only and cannot become a
second normalization or release authority.

Rollback reverts this bounded code/mirror/selector change and redeploys the
preceding same-Site v263. Retain private originals, submissions, withdrawal receipts
and review history. No deletion, data promotion, source activation, merge, public
publication or storage reset is authorized by this report. A separately reviewed
released carrier and rights, sensitivity, provenance, policy, correction and
rollback closure are still required before any map/API release.
