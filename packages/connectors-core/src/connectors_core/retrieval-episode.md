# connectors_core retrieval-to-SourceRetrievalEpisode recording

## Status

**PROPOSED internal implementation; fixture-only; no live transport, storage, receipt emitter, lifecycle writer, or public export.**

`retrieval_episode.py` records one injected-transport `RetrievalResult` as a `SourceRetrievalEpisode` shaped for `schemas/contracts/v1/source/source_retrieval_episode.schema.json`. It is the source-agnostic companion to `artifact_handoff.py`, and it was extracted once a second connector needed it: `connectors/usgs` (earthquake feeds) and `connectors/fema` (OpenFEMA declarations pages).

## API

```python
from connectors_core.retrieval_episode import build_retrieval_episode, RetrievalEpisode

record = build_retrieval_episode(
    result, source_url=url, source_id="usgs.earthquake",
    retrieval_profile_ref="kfm:source-profile:usgs-earthquake-geojson-v1",
    attempted_at=attempted, completed_at=completed, spec_hash=compute_spec_hash)
record.episode    # fresh dict copy; the stored episode is canonical JSON
record.body       # exact bytes only when captured, otherwise None
```

`spec_hash` must be the repository's canonical `hashing.compute_spec_hash` (RFC 8785). It is injected so this package stays standard-library-only.

## Mapping

- Category, final HTTP status, retries (attempts after the first), and elapsed time come from the result.
- ETag, Last-Modified, and Content-Length come from the source head; digest, byte length, and media type come from the captured payload.
- The locator is `RetrievalResult.safe_locator` (no userinfo, query, or fragment).
- Result status and reason come from a table that mirrors the contract validator's `recompute_result()`. `tests/packages/connectors_core/test_retrieval_episode.py` fails if the two drift.
- Governance flags are fixed to the contract's fixture-only constants.

Outcomes the current contract cannot represent are refused rather than re-labelled:
- HTTP 204 raises `EMPTY_SUCCESS_UNREPRESENTABLE`, because a captured GET needs a non-empty body.
- A 304 to a request this boundary never makes conditional is recorded as `INVALID_RESPONSE_METADATA`.

## Construction integrity

`RetrievalEpisode` re-validates itself on construction, including direct construction. It rejects:
- an `episode_id` that does not agree with `spec_hash`;
- governance that differs from the fixed constants;
- a locator that is not the redaction of `source_url`;
- a body present on an uncaptured episode, or missing from a captured one;
- a captured body whose length or SHA-256 differs from the recorded values.

It cannot recompute `spec_hash`, because that needs the injected canonical hasher. The contract validator does recompute it.

## Directory Rules basis

The code is reusable, source-agnostic implementation, so it lives in `packages/connectors-core/src/connectors_core/`. Source-specific profiles, allowlists and routing stay under `connectors/<source>/`, and the semantic contract stays under `schemas/` and `tools/validators/source/`.

## Validation

```bash
python tools/ci/install_python_ci.py project-test
python -m pytest tests/packages/connectors_core/test_retrieval_episode.py -q --strict-config --strict-markers
```

The suite runs every reachable category through the repository validator and covers the direct-construction integrity cases. A green result proves only this mapping and integrity boundary. It does not prove a live source, admission, storage, receipt correspondence, evidence, release, or publication.

## Rollback

Revert the module, and the connector `fetch.py` modules that import it, together.
