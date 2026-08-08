# TemporalAuthorityEnvelope

Status: PROPOSED implementation contract.

`TemporalAuthorityEnvelope` is a shared evidence-support envelope for keeping identity, source role, authority, geography, lineage, and materially distinct times explicit. It does not replace domain contracts and grants no release authority.

Required time roles are `observed_at`, `valid_from`, `valid_to`, `source_updated_at`, `retrieved_at`, `released_at`, and `corrected_at`; nullable roles must remain explicit. The validator rejects inverted validity, source updates after retrieval, release before retrieval, correction before release, generic unlabeled timestamps, unknown source role, and a `CURRENT` posture whose freshness deadline has elapsed.

Finite temporal posture: `CURRENT`, `STALE`, `SUPERSEDED`, `WITHDRAWN`, `UNKNOWN`.

A published or public-safe carrier may cite this envelope only with an independent EvidenceBundle, policy/review state, and ReleaseManifest. This object never turns briefing prose, forecasts, models, or aggregates into observations.