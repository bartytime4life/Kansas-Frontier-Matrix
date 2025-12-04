---
title: "🧠 KFM v11.2.3 — NOAA NODD SNS → SQS Operator Contracts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed contracts for the core operators in the NOAA NODD SNS → SQS ingestion pipeline: message parse, integrity check, metadata extract, STAC register, and provenance emit."
path: "docs/pipelines/atmo/nodd-sns-sqs/operators/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x operator-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Operator Specification"
intent: "nodd-sns-sqs-operators"
category: "Pipelines · Atmospheric · Operators"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD operator standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🧠 NOAA NODD SNS → SQS Operator Contracts  

`docs/pipelines/atmo/nodd-sns-sqs/operators/README.md`

**Governed contracts for the core operators in the NOAA NODD SNS → SQS ingestion pipeline: message parse, integrity check, metadata extract, STAC register, and provenance emit.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Pipeline-NODD_SNS_%E2%86%92_SQS-skyblue" />
<img src="https://img.shields.io/badge/Operators-Deterministic-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This document defines the **governed contracts** for the core operators that make up the NOAA NODD SNS → SQS ingestion pipeline:

- `message-parse`  
- `integrity-check`  
- `metadata-extract`  
- `stac-register`  
- `provenance-emit`  

Each operator:

- Has a **strict, typed input/output contract**.  
- Is **deterministic and idempotent** given the same inputs and configuration.  
- Integrates with **telemetry, WAL, and governance gates** documented elsewhere in the NODD pipeline.

Operators MUST be composable in any order consistent with these contracts, without hidden side-effects.

---

## 🗂 2. Directory Layout (Emoji-Prefix Standard)

Operators documentation under `docs/pipelines/atmo/nodd-sns-sqs/operators/`:

    docs/pipelines/atmo/nodd-sns-sqs/operators/
    │
    ├── 📄 README.md                        # This file (operator contracts index)
    │
    ├── 🧾 message-parse.md                 # SNS/SQS → canonical NODD event envelope
    ├── 🛡️ integrity-check.md               # Size, checksum, headers, basic QC
    ├── 🧬 metadata-extract.md              # Spatial/temporal/product metadata extraction
    ├── 🗺️ stac-register.md                 # Deterministic STAC Item/Collection registration
    └── 📚 provenance-emit.md               # PROV-O / OpenLineage event generation contracts

Implementation code (e.g., Python modules) lives in the code tree, but MUST conform to the contracts in these documents.

---

## 🧾 3. Canonical Operator Graph

Conceptual operator graph for a single ingest unit:

    [SNS/SQS Message]
          |
          v
    (message-parse)
          |
          v
    (integrity-check)
          |
          v
    (metadata-extract)
          |
          v
    (stac-register)
          |
          v
    (provenance-emit)

All operators are pure functions with respect to their inputs and configuration, except for:

- External I/O (object fetch, STAC write, provenance write).  
- Telemetry emission (spans/metrics/logs).  

Any side effects must be observable and logged.

---

## ✉️ 4. Message Parse Operator

**File:** `message-parse.md`  
**Role:** Convert raw SNS/SQS payloads into a **canonical NODD event envelope** used by downstream operators.

### 4.1 Input

- Raw SQS message body + attributes.  
- Includes SNS envelope (subject, message, attributes).

### 4.2 Output (Canonical Envelope)

Required fields (conceptual):

- `event_time` (RFC3339).  
- `dataset` (canonical dataset ID, e.g., `goes-abi`, `nexrad-l2`).  
- `object_uri` (e.g., S3/Blob/GCS URI).  
- `provider` (`aws`, `azure`, `gcp`).  
- `content_etag` / checksum.  
- `time_range` (start/end timestamps).  
- `priority`.  
- `schema_version`.

### 4.3 Guarantees

- Drops or quarantines malformed messages (never passes partial or ambiguous envelopes).  
- Enforces **schema_version** compatibility.  
- Emits telemetry on parsing errors and dataset/priority classifications.

---

## 🛡️ 5. Integrity Check Operator

**File:** `integrity-check.md`  
**Role:** Ensure object integrity and basic QC before further processing.

### 5.1 Input

- Canonical event envelope from `message-parse`.  
- Optional WAL reference (if already recorded).

### 5.2 Processing

- Fetches the referenced object (if not already cached).  
- Validates:
  - Size against expected thresholds.  
  - ETag or checksum consistency.  
  - Basic header consistency (e.g., content-type).

### 5.3 Output

- Envelope enriched with:
  - `integrity_status` (`ok`, `failed`, `suspect`).  
  - `content_length` and normalized checksum.  
  - Any repair attempts (if applicable).

### 5.4 Guarantees

- No downstream operator is invoked for `integrity_status = failed`.  
- Hard failures push message into DLQ/quarantine; soft anomalies are annotated for downstream QA.

---

## 🧬 6. Metadata Extract Operator

**File:** `metadata-extract.md`  
**Role:** Derive **domain-specific metadata** needed for STAC registration and graph integration.

### 6.1 Input

- Envelope with integrity results and object reference.

### 6.2 Processing

- Reads object metadata (headers, sidecar metadata, filename patterns).  
- Populates:
  - Spatial footprint (geometry, bbox).  
  - Temporal attributes (acquisition time, validity time, model run time).  
  - Product identifiers (e.g., channel/band, radar product code).  
  - Dataset-specific extensions (e.g., scanning mode, elevation angle).

### 6.3 Output

- Envelope enriched with:
  - `stac_properties` (ready to map into STAC Item properties).  
  - `geometry` and `bbox`.  
  - Derived keys needed for STAC ID construction and collection mapping.

### 6.4 Guarantees

- All derived fields are deterministic functions of object content + configuration.  
- Missing critical metadata results in a hard failure or quarantine, not silent defaults.

---

## 🗺️ 7. STAC Register Operator

**File:** `stac-register.md`  
**Role:** Write or update STAC Items/Collections in a **deterministic, atomic** fashion.

### 7.1 Input

- Envelope with metadata and integrity results.

### 7.2 Processing

- Derives STAC Item ID (deterministic).  
- Constructs STAC Item JSON:
  - `id`, `geometry`, `bbox`, `datetime`.  
  - `properties` (including NODD-specific extensions).  
  - `assets` (primary data + sidecars).

- Validates against:
  - STAC core.  
  - KFM STAC profile (extensions, required fields).  

- Atomically writes:
  - Candidate Item to temporary store.  
  - Promotes to canonical catalog only after validation passes.

### 7.3 Output

- Envelope enriched with:
  - `stac_item_id`.  
  - `stac_collection_id`.  
  - `stac_write_status` (`created`, `updated`, `no-op`, `failed`).

### 7.4 Guarantees

- No partial or invalid Items appear in the canonical catalog.  
- Idempotent: same envelope with unchanged object does not create duplicates.

---

## 📚 8. Provenance Emit Operator

**File:** `provenance-emit.md`  
**Role:** Emit **PROV-O and/or OpenLineage** records that document the ingest.

### 8.1 Input

- Envelope with STAC write results and identifiers.  
- WAL reference if available.

### 8.2 Processing

- Creates or updates:
  - `prov:Activity` representing the ingest run.  
  - `prov:Entity` for the NODD object and resulting STAC Item.  
  - `prov:Agent` representing the pipeline or service.

- For OpenLineage:
  - Emits `Job`, `Run`, and `Dataset` events.

### 8.3 Output

- Envelope enriched with:
  - `prov_activity_id`.  
  - `openlineage_run_id`.  
  - Any governance tags associated with this ingest.

### 8.4 Guarantees

- Provenance is emitted **once** per ingest unit (idempotent using WAL / idempotency keys).  
- Failures in provenance emission are visible via telemetry and can be replayed using WAL.

---

## 🧱 9. Reliability & Idempotency Across Operators

Cross-cutting reliability guarantees:

- Every operator is **side-effect free** with respect to its input envelope, except where explicitly documented (STAC writes, provenance writes, telemetry).  
- Idempotency is enforced at:
  - Message level (SNS/SQS dedupe keys, where applicable).  
  - Ingest job level (idempotency keys based on dataset + object + checksum).  
- WAL-backed semantics:
  - Operators that mutate external state only proceed once WAL entries exist.  
  - Replays drive the same operator chain with the same contracts.

Operators MUST be testable in isolation with mock dependencies.

---

## 🧪 10. Testing & CI Requirements

For each operator, CI must include:

- **Contract tests**:
  - Valid input → expected output envelope.  
  - Invalid input → deterministic failure modes.

- **Round-trip tests**:
  - Full operator chain on a sample event:
    - message-parse → integrity-check → metadata-extract → stac-register → provenance-emit.  

- **Negative tests**:
  - Corrupt objects.  
  - Missing metadata.  
  - Schema version mismatches.

- **Determinism tests**:
  - Same inputs + config → identical outputs (modulo timestamps where applicable).

No change to operator behavior can merge without updating corresponding tests and, if needed, this specification.

---

## 🕰 11. Version History

| Version  | Date       | Notes                                                                                         |
|---------:|------------|-----------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial operator contracts for NODD SNS → SQS; defined parse, integrity, metadata, STAC, PROV. |

---

<div align="center">

### 🧠 NOAA NODD SNS → SQS Operators · KFM v11.2.3

Deterministic · Composable · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Pipeline](../README.md) ·  
[📊 Telemetry & SLOs](../telemetry/README.md) ·  
[🔁 Replay & WAL](../replay/README.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>