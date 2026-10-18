# Kansas land records in Data commons

The signed-in `/data/land-records` workspace imports bounded private-review
transfers produced by the KFM repository land pipeline. It reuses existing
`data_submissions`, `data_submission_reviews`, dispatch identity and R2
quarantine storage. This change requires no database migration, reseed or
additional privilege. Owners see their own submissions; assigned stewards can
inspect the review queue and append existing version-checked review notes.

The application checks canonical JSON, closed transfer and record shapes,
source hosts, byte budgets, original-object hashes, capture/candidate/record
identities and EvidenceBundle membership. Every imported bundle is pending,
restricted and unreleased. Hash integrity does not establish source
authenticity, normalization correctness, rights, sensitivity or source
admission. The Python exporter deterministically replays the private ledger;
hosted normalization review remains explicitly pending. Neither endpoint
can promote records or issue a release decision.

`/api/land-records` lists 20 owner-visible bundles with a bounded continuation
cursor. `/api/land-records/[id]` checks owner/steward access and the retained
R2 bytes before returning at most 50 filtered records, individual evidence or
an authenticated original-object attachment. A transfer is limited to 10 MiB,
20 captures and 1,000 candidate occurrences; repeated occurrences display
once per immutable record digest. Source, county, instrument, record search
and event-date filters retain separate recording dates and amount roles.
Candidate versions remain distinct from unique instruments or complete
Kansas coverage. Original downloads are attachment-only, private/no-store
and sandboxed. The ordinary `/api/governed/land-records/v1/[view]` route
always denies with zero candidate records.

BLM keyword captures can contain surveys. Known survey cards are retained in
original bytes and counted as exclusions, not converted into purchases or
sales. State-volume and serial patent metadata use supplied accessions;
CDI entries retain their composite identity warning. County tax-foreclosure
results use `AUCTION_REPORTED` and `auction_purchase_price`. Bundled tracts
remain one sale unit without allocating prices to parcels. Neither auction
results nor deed-name labels prove court confirmation, recording or title.
Sales questionnaires, paid record scraping and automatic acquisitions are
outside this workflow. Modern party/parcel joins remain restricted.

Generate a transfer outside Git with the repository CLI:

```sh
python tools/local_data/land_records.py --root /absolute/private/store \
  export-review --output /absolute/private/land-review.json
```

Use repeated `--capture-id sha256:...` flags to select active captures. Withdrawn
captures are excluded; originals and local withdrawal receipts remain retained.
Upload permission is explicitly confirmed in the private form. The Site cannot
read a workstation path or a companion token. Private evidence does not enter
source control, static assets, deployment archives or the public map.

App files reuse the existing deployable Site responsibility. Canonical
normalization and transfer implementation remain in the domain package,
source adapters in connectors, orchestration in the ingest pipeline, contracts
and schemas in their existing roots, and physical candidate bytes outside Git.
This follows Directory Rules v2 sections 10.1, 11.4 and 14 with ADR-0029;
application validation is a bounded integrity projection, not a second source
registry, normalization or release authority.

Rollback reverts the additive application routes/navigation and redeploys the
previous same-Site version. Existing private submissions, originals and review
history remain retained. No deletion, data promotion or storage reset is part
of rollback. Source validation, GitHub mirror parity, review acceptance,
private deployment and browser acceptance are separate evidence.
