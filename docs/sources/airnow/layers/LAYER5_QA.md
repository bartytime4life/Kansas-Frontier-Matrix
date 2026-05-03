# AirNow Layer 5 QA

Layer 5 performs **offline internal QA summaries** over Layer 4 reconciliation artifacts. It does not ingest live data, call web services, download files, publish outputs, create dashboards, tiles, UI, or public APIs.

AirNow data are preliminary and subject to change. Official regulatory air-quality data must come from EPA AQS/AirData.

## Inputs
Local Layer 4 JSON/JSONL indexes, conflicts, quarantine, and reconciliation receipt.

## Outputs
coverage_summary, freshness_summary, source_completeness_summary, parameter_coverage_summary, geography_coverage_summary, relationship_graph_summary, conflict_summary, orphan_summary, quarantine_summary, governance_summary, qa_findings, qa_report, qa_receipt.

## Next Layer
Layer 6 should add offline internal bundle assembly (manifest/receipt/schema bundle and optional archive) without live ingestion or publication.
