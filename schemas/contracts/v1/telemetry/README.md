# Telemetry schemas

**Status:** PROPOSED machine-shape lane  
**Owning root:** `schemas/`  
**Semantic owner:** `contracts/telemetry/`  
**Policy authority:** unchanged

This directory contains machine-checkable shapes for admitted telemetry contract profiles. A schema pass establishes shape only; it does not establish evidence truth, policy admissibility, review, promotion, release, publication, or runtime maturity.

## Current profiles

| Schema | Semantic contract | Scope |
|---|---|---|
| `trace_receipt_link.schema.json` | `contracts/telemetry/trace_receipt_link.md` | Positive, fixture-first trace-to-receipt-to-evidence linkage assertion. |
| `openlineage_run_event_projection.schema.json` | `contracts/telemetry/openlineage_run_event_projection.md` | Deterministic, fixture-only terminal OpenLineage RunEvent-shaped projection from a canonical RunReceipt and EvidenceBundle-resolution summaries. |
| `remote_sensing_lineage_activity.schema.json` | `contracts/telemetry/remote_sensing_lineage_activity.md` | Deterministic, fixture-only remote-sensing metrics and PROV companion composed with the existing OpenLineage projection. |

## Boundary

- Telemetry remains a carrier and process-memory surface, not sovereign truth.
- Runtime receipt schemas remain in their accepted receipt/source/runtime families.
- Policy rules remain under `policy/`.
- Instances, traces, logs, metrics, and exported lineage events do not belong in this schema directory.
- New telemetry schemas require paired contracts, fixtures, validators, tests, and rollback notes.
