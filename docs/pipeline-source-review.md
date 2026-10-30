# USGS / NWS source review packet

Status: REVIEW REQUIRED. No signed approval, credential, source admission or hosted publication is created by this packet.

Reconciled application recipe digest: `5fde439189e6cc813401d84d6a3f6036ecaedcfd666f87b66ab2de37fb098055`

Review the exact product below, then supply existing accepted source, rights, review and release-profile references using `cli.mjs profile-template SOURCE`. Keep every placeholder unsigned. Approval must bind this recipe digest and expire within the existing 30-day maximum.

## USGS streamflow

Source ID: `usgs-streamflow`

Example bounded query (dated illustration): https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous/items?f=json&limit=1000&state_code=20&agency_code=USGS&site_type_code=ST&parameter_code=00060&datetime=2026-10-28T00%3A00%3A00.000Z%2F2026-10-29T00%3A00%3A00.000Z

Provider rights reference: https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits

Capture interval: 1 hour(s). Maximum entity bytes: 8388608.

Rolling 24-hour Kansas streamflow query, at most 1,000 rows. Provisional values, original units, missing values and paging remain in the source. No automatic flood or evidence interpretation.

## NWS Kansas alerts

Source ID: `nws-alerts`

Example bounded query (dated illustration): https://api.weather.gov/alerts/active?area=KS

Provider rights reference: https://www.weather.gov/disclaimer

Capture interval: 1 hour(s). Maximum entity bytes: 8388608.

Active Kansas alert payload at retrieval time; no zone geometry expansion. Expired or missing alerts are not an all-clear. Not an emergency notification service.

## Acceptance still required

- Confirm applicable rights and public sensitivity against the exact source descriptors; a working API is not approval.
- Review one real bounded capture per source, including partial/empty and observation-clock behavior.
- Verify the intended GoDaddy app and deployed source before any upload.
- Establish verified MySQL TLS, private artifact storage, dedicated transfer credentials and reviewed profile references.
- Run staging, hash readback, activation conflict, withdrawal and rollback acceptance before enabling routine publication.

The broader domain queue remains disabled until each product passes its own review. The preserved archive still needs a full-size independent backup.


## Historical private capture checkpoint

These candidates were produced by the installed two-source worker before reconciliation with newer earthquake/county code. They are not acceptance evidence for the reconciled recipe above. Re-normalize exact preserved bytes with the candidate recipe and review fresh hashes before signing any replacement profiles.

Read back on 2026-10-30T02:53:56.575Z. These are unsigned external-context candidates, not approved hosted releases. Original source bytes and receipts remain private.

| Source | Retrieved | Records | Partial | Product SHA-256 |
|---|---|---|---|---|
| usgs-streamflow | 2026-10-30T02:00:18.736Z | 181 | false | 95419667f40a0f1ab74620b3beb2723b1243d8d40f9e2df45f852d9b63ea6b6a |
| nws-alerts | 2026-10-30T02:00:19.564Z | 6 | false | b57aa082a74f2dbb550e656f69a1cd642da26727130dddd6c4ab477fe307bcee |

Offline revalidation corrected 156 private USGS candidates from preserved raw bytes and matching receipts; the subsequent audit found all 312 candidates valid. Originals, previous candidate bytes and source retrieval clocks were preserved. Correction receipts do not grant admission or publication. Inspect the corresponding source items in KFM Working Data before approving any profile.
