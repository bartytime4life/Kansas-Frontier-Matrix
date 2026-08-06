# Telemetry schemas

**Status:** PROPOSED machine-shape lane  
**Owning root:** `schemas/`  
**Semantic owner:** `contracts/telemetry/`  
**Policy authority:** unchanged

This directory contains machine-checkable shapes for admitted telemetry contract profiles. A schema pass establishes shape only; it does not establish evidence truth, policy admissibility, review, promotion, release, publication, or runtime maturity.

## Current profile

| Schema | Semantic contract | Scope |
|---|---|---|
| `trace_receipt_link.schema.json` | `contracts/telemetry/trace_receipt_link.md` | Positive, fixture-first trace-to-receipt-to-evidence linkage assertion. |

## Boundary

- Telemetry remains a carrier and process-memory surface, not sovereign truth.
- Runtime receipt schemas remain in their accepted receipt/source/runtime families.
- Policy rules remain under `policy/`.
- Instances, traces, logs, and metrics do not belong in this schema directory.
- New telemetry schemas require paired contracts, fixtures, validators, tests, and rollback notes.
