# USDA NASS Nested Connector Lane

`connectors/usda/nass/` is a draft nested connector lane for USDA National Agricultural Statistics Service source admission.

Status: draft / NEEDS VERIFICATION.

This lane does not supersede `connectors/nass/` or `connectors/usda-nass/`. Canonical placement remains unresolved until an ADR, migration note, or Directory Rules update chooses the accepted home.

Connector output is limited to `data/raw/` or `data/quarantine/`. This folder must not own source-family doctrine, domain doctrine, SourceDescriptor authority, policy, schemas, catalog/triplet records, release decisions, public API behavior, or public UI behavior.

QuickStats is aggregate data in KFM posture. Aggregate cells must preserve aggregation scope and must not be used as finer-grain truth.
