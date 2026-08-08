# SourceHealthAssessment Contract

Status: PROPOSED implementation contract.

`SourceHealthAssessment` records a bounded, non-publishing evaluation of source freshness and retrieval health. It is designed for watcher sidecars and material-change detection without granting source activation, truth, release, or publication authority.

Finite health outcomes: `HEALTHY`, `DEGRADED`, `STALE`, `UNAVAILABLE`, `UNKNOWN`.

The assessment records source identity, probe time, last successful retrieval, freshness deadline, optional ETag/Last-Modified observations, HTTP/result class, material-change signal, and finite reasons. A watcher may emit this object and propose work, but it must never clear a prior condition merely because the current probe is empty or failed.

Fail-closed rules: failed retrieval cannot be `HEALTHY`; elapsed freshness cannot be `HEALTHY`; `UNAVAILABLE` requires a failed result; `material_change=true` requires a change reason; and `UNKNOWN` remains non-authoritative.