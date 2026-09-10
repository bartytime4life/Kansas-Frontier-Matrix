# Sites v15 official-context alignment checkpoint

Status: **SAVED / NOT DEPLOYED**

This record captures the review boundary for ChatGPT Sites project `appgprj_6aa0b1c41bc08191bfd86003920f1631` without asserting GitHub source parity, source admission, release, publication, or deployment.

## Immutable checkpoint

- Site: https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site
- Saved Site version: `15`
- Current production Site version: `14`
- Sites source commit: `459916cb3622385b2b0d19b83e7fb666966d9ab3`
- Saved archive hash: `sha256:ca1ae92ada5ea03191094224131bc06fcd820e3185db383bd61482d65887ba76`
- GitHub alignment base: `f0b1c0acd44fb64192abd77fb19e068277c3db34`

## Saved capability slice

- Enrich Census 2026 TIGERweb county geometry with 2024 ACS 5-year total population (`DP05_0001E`) through a GEOID join.
- Add an opt-in USGS 30-day Kansas earthquake context feed, bounded by rectangle, event type, and result count.
- Make official sources searchable alongside places, layers, and features.
- Add a Data command, official-data pulse, connection/retrieval visibility, refresh-visible, and hide-all controls.
- Show source-aware selection summaries for county, streamflow, earthquake, and alert context.
- Preserve evidence boundaries: every official feed remains `EXTERNAL_CONTEXT_ONLY`; no feed is admitted to KFM EvidenceBundles, reports, exports, release, or source authority.

Official API references:

- Census ACS DP05 variables: https://api.census.gov/data/2024/acs/acs5/profile/groups/DP05.html
- USGS Earthquake Catalog API: https://earthquake.usgs.gov/fdsnws/event/1/

## Verification

- Production build: passed.
- Focused rendered/API tests: `34/34` passed.
- Tests cover the mocked Census population join, bounded earthquake query, and rejection of unknown adapter feeds without network access.
- Only a non-blocking client-chunk size warning remains.

## Connected design records

- Notion Real-Data hub: https://app.notion.com/p/3d6a92021bf6816cae0ec1ccbd15e21e?pvs=204
- Google Drive Living Atlas design doc: https://docs.google.com/document/d/1aivNyfMjQ8urQO6vjt4YvkT1ltF1t7fxCahEcnGV4Dw/edit?usp=drivesdk

## Review boundary

The GitHub app and the Sites source have materially diverged. This checkpoint intentionally does not overwrite the repository app with the Sites tree. A later source-parity change should re-pin `main`, identify overlapping ownership, reconcile the exact official-context files, run repository-native validation, and obtain review before any merge or deployment.

Deployment remains a separate, explicit action.
