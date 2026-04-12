# hydrology thin slice bundle

This example bundle shows one governed hydrology path:

1. Source edge admitted (`source_descriptor`) -> RAW.
2. Fetch proof (`ingest_receipt`) -> WORK.
3. `dataset_version` emitted at PROCESSED.
4. `release_manifest` links dataset to PUBLISHED-ready evidence refs.
5. `evidence_bundle` ties decision/release/proof objects.
6. Runtime emits explicit outcomes (`ANSWER` and `DENY`).

This is a non-authoritative example pack.
