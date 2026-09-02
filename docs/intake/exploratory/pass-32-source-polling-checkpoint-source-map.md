<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-source-polling-checkpoint
title: Pass 32 source polling checkpoint adaptation
status: proposed adaptation; fixture-only
type: exploratory-intake; source-map
created: 2026-08-08
updated: 2026-08-08
[/KFM_META_BLOCK_V2] -->

# Pass 32 source polling checkpoint adaptation

Pass 32 carries `KFM-P18-PROG-0009`: persist ETag, Last-Modified, source locator, and validator state per source so no-change and changed-source paths are explicit. Current repository evidence already contains source health, source availability watchlist, and STAC asset HEAD prefilter families. This packet adds only the missing generic checkpoint projection and does not replace those objects.

The implementation is fixture-only, uses opaque endpoint references, makes no network request, downloads no payload, and treats `FETCH_CANDIDATE` as review metadata rather than RAW admission.
