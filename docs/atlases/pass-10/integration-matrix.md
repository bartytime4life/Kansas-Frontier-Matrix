# Pass 10 idea integration matrix

Status: CONFIRMED as an atlas integration carrier; operationalization remains HOLD.

Every row below is backed by the exact record in `changed-cards-pass-10.jsonl`. Candidate authority families are responsibility-root guidance only; no unverified leaf path is asserted.

| Stable ID | Delta | Category | Title | Proposed track | Operationalization |
|---|---|---|---|---|---|
| KFM-P1-IDEA-0061 | EXPANDED | ANA | Spatial analysis as interpretive derivative | analytics-and-environmental-data | HOLD |
| KFM-P1-PROG-0062 | EXPANDED | ANA | AOD and FRP tile-health gates when policy-bound | analytics-and-environmental-data | HOLD |
| KFM-P10-PROG-0009 | NEW | ANA | Fused PM2.5 surface ETL | analytics-and-environmental-data | HOLD |
| KFM-P10-PROG-0016 | NEW | ANA | TROPOMI NO2 gridding and AQS collocation | analytics-and-environmental-data | HOLD |
| KFM-P10-PROG-0017 | NEW | ANA | EPA AQS hourly O3/NO2 and 8-hour ozone aggregation | analytics-and-environmental-data | HOLD |
| KFM-P10-PROG-0018 | NEW | ANA | Raster-to-point GeoParquet and H3 aggregation | analytics-and-environmental-data | HOLD |
| KFM-P8-PROG-0022 | EXPANDED | ANA | DuckDB + h3 hex coverage / overlap QA | analytics-and-environmental-data | HOLD |
| KFM-P10-FEAT-0003 | NEW | CAT | Discovery-to-draft-PR catalog update flow | discovery-and-catalog | HOLD |
| KFM-P6-PROG-0014 | EXPANDED | CAT | STAC/OGC watcher + webhook boundary | discovery-and-catalog | HOLD |
| KFM-P10-IDEA-0002 | NEW | DAT | Low-blast discovery: one emitter per upstream | event-intake-and-idempotency | HOLD |
| KFM-P10-PROG-0021 | NEW | DAT | Event-first upstream discovery envelope | event-intake-and-idempotency | HOLD |
| KFM-P10-PROG-0022 | NEW | DAT | Idempotency key recipe for discovery events | event-intake-and-idempotency | HOLD |
| KFM-P10-PROG-0003 | NEW | EVD | PROV-O to Neo4j lineage mapping | evidence-and-lineage | HOLD |
| KFM-P10-PROG-0024 | NEW | EVD | PROV receipt for watershed rollups | evidence-and-lineage | HOLD |
| KFM-P8-PROG-0019 | EXPANDED | EVD | DRIFT STAC, Provenance, Embeddings, Graph Queries | evidence-and-lineage | HOLD |
| KFM-P1-FEAT-0038 | EXPANDED | MAP | Governed API as trust membrane | map-delivery-and-governed-services | HOLD |
| KFM-P1-IDEA-0040 | EXPANDED | MAP | Tiles, PMTiles, COGs, GeoParquet, MVT, and MLT as rebuildable artifacts | map-delivery-and-governed-services | HOLD |
| KFM-P1-PROG-0041 | EXPANDED | MAP | Layer, style, tile artifact, and map release manifests | map-delivery-and-governed-services | HOLD |
| KFM-P10-FEAT-0001 | NEW | MAP | Governed routing and isochrone service surface | map-delivery-and-governed-services | HOLD |
| KFM-P4-PROG-0002 | EXPANDED | MAP | COG, GeoParquet, PMTiles, STAC, DCAT, and PROV form an artifact matrix | map-delivery-and-governed-services | HOLD |
| KFM-P1-PROG-0021 | EXPANDED | MDP | STAC, DCAT, and PROV profile mapping | metadata-and-catalog-profiles | HOLD |
| KFM-P10-PROG-0002 | NEW | MDP | GeoParquet metadata contract for Arrow pipelines | metadata-and-catalog-profiles | HOLD |
| KFM-P10-PROG-0007 | NEW | MDP | Attestation discoverability in STAC/DCAT/PROV | metadata-and-catalog-profiles | HOLD |
| KFM-P10-PROG-0020 | NEW | MDP | OpenLandMap STAC and Zenodo DOI soil-layer ingest | metadata-and-catalog-profiles | HOLD |
| KFM-P3-IDEA-0004 | EXPANDED | MDP | KFM Catalog Extensions (kfm:run_receipt_ref, kfm:proof_ref, kfm:trust_class, kfm:source_role) | metadata-and-catalog-profiles | HOLD |
| KFM-P10-PROG-0013 | NEW | MOD | Watershed rollup schema and rollSpecVersion | domain-modeling | HOLD |
| KFM-P1-PROG-0026 | EXPANDED | PIP | CI probes with source heads and run receipts | pipeline-runtime-and-reliability | HOLD |
| KFM-P1-PROG-0029 | EXPANDED | PIP | Schema, contract, policy, and directory drift detection | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0001 | NEW | PIP | Arrow-native geospatial pipeline | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0004 | NEW | PIP | Experiment registry nightly health check | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0008 | NEW | PIP | Valhalla routing graph build pipeline | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0010 | NEW | PIP | SMAP L3/L4 soil moisture raster ETL | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0011 | NEW | PIP | Container-native geospatial ETL orchestration references | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0012 | NEW | PIP | Mini GeoTIFF to COG and STAC automation lab | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0015 | NEW | PIP | WZDx GeoParquet/PMTiles CI pattern | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0019 | NEW | PIP | SCAN/AWDB and USCRN soil-station ingest | pipeline-runtime-and-reliability | HOLD |
| KFM-P10-PROG-0023 | NEW | PIP | Discovery PR merge gates | pipeline-runtime-and-reliability | HOLD |
| KFM-P2-PROG-0003 | EXPANDED | PIP | Soil and air watcher pattern (SoilGrids, SSURGO, EPA AQS, EPA AirNow) | pipeline-runtime-and-reliability | HOLD |
| KFM-P2-PROG-0004 | EXPANDED | PIP | SMAP L4 soil moisture ingest with CI-friendly QA | pipeline-runtime-and-reliability | HOLD |
| KFM-P5-PROG-0009 | EXPANDED | PIP | validate_all.py canonical validator entrypoint | pipeline-runtime-and-reliability | HOLD |
| KFM-P7-PROG-0009 | EXPANDED | PIP | CI workflow skeleton: schema ->policy ->sign ->export ->attest | pipeline-runtime-and-reliability | HOLD |
| KFM-P8-PROG-0001 | EXPANDED | PIP | Trigger and retry decision matrix | pipeline-runtime-and-reliability | HOLD |
| KFM-P8-PROG-0003 | EXPANDED | PIP | Idempotency keys and exponential backoff with jitter | pipeline-runtime-and-reliability | HOLD |
| KFM-P8-PROG-0004 | EXPANDED | PIP | Replay-safe ETL - outbox, WAL, ON CONFLICT, dead-letter requeue | pipeline-runtime-and-reliability | HOLD |
| KFM-P8-PROG-0023 | EXPANDED | PIP | NWIS Kansas streamflow watcher | pipeline-runtime-and-reliability | HOLD |
| KFM-P8-PROG-0025 | EXPANDED | PIP | WZDx v4.x roadworks validator and transformer | pipeline-runtime-and-reliability | HOLD |
| KFM-P1-PROG-0032 | EXPANDED | POL | Rights and source terms gate | rights-and-policy | HOLD |
| KFM-P10-IDEA-0001 | NEW | POL | Citizen air-sensor QA and calibration posture | rights-and-policy | HOLD |
| KFM-P10-PROG-0014 | NEW | POL | SPDX license guard across code and catalogs | rights-and-policy | HOLD |
| KFM-P1-IDEA-0056 | EXPANDED | REL | Promotion as governed state transition | release-and-promotion | HOLD |
| KFM-P1-IDEA-0059 | EXPANDED | REL | Watcher output enters WORK_CANDIDATE, not PUBLISHED | release-and-promotion | HOLD |
| KFM-P1-PROG-0017 | EXPANDED | SEC | Signed attestations and provenance references | security-and-attestation | HOLD |
| KFM-P10-PROG-0005 | NEW | SEC | SBOM plus signing hardening pack | security-and-attestation | HOLD |
| KFM-P10-PROG-0006 | NEW | SEC | DSSE/SLSA attestations for data artifacts | security-and-attestation | HOLD |
| KFM-P5-PROG-0013 | EXPANDED | SEC | Runtime telemetry envelope for verified surfaces | security-and-attestation | HOLD |
| KFM-P6-PROG-0010 | EXPANDED | SEC | SBOM, in-toto provenance, and Rekor inclusion as release prerequisites | security-and-attestation | HOLD |
| KFM-P1-FEAT-0066 | EXPANDED | UIX | Focus Mode stays evidence-bounded | trust-visible-ui | HOLD |
| KFM-P1-FEAT-0068 | EXPANDED | UIX | Story Nodes inherit release state and rights posture | trust-visible-ui | HOLD |
| KFM-P10-FEAT-0002 | NEW | UIX | Watershed summary nodes for Focus Mode | trust-visible-ui | HOLD |

## Coverage

- CONFIRMED: 59 changed stable IDs are listed exactly once.
- CONFIRMED: 29 are NEW and 30 are EXPANDED.
- CONFIRMED: Every row resolves to a full source record and an operationalization backlog record.
- UNKNOWN: None is claimed implemented because implementation evidence is not mounted in this workspace.
