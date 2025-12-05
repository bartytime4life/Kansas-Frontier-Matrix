---
title: "🛡️ KFM v11.2.4 — FAIR+CARE Validation Gates for SNS→SQS Auto-Updates (Self-Verifying Promotion)"
description: "Deterministic validation gates wired into event-driven ingestion. Each SNS→SQS message enforces FAIR+CARE, provenance, and schema fitness before promotion to stable."
path: "docs/pipelines/atmo/nodd-sns-sqs/validation/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Data Governance Board"
content_stability: "stable"
backward_compatibility: "v11.x ingestion-contract compatible"
status: "Active / Enforced"

doc_kind: "Pipeline Validation Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/atmo/nodd-sns-sqs/validation"
  applies_to:
    - "atmo"
    - "sns-sqs"
    - "validation-gates"
    - "ingest"
    - "stac"
    - "dcat"
    - "prov"
    - "fair-care"
    - "geoethics"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/validation-gates-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipeline-validation-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:pipelines:atmo:nodd-sns-sqs:validation:v11.2.4"
semantic_document_id: "kfm-pipeline-atmo-nodd-sns-sqs-validation-gates-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:atmo:nodd-sns-sqs:validation:v11.2.4"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🛡️ FAIR+CARE Validation Gates for SNS→SQS Auto-Updates (Self-Verifying Promotion)  
`docs/pipelines/atmo/nodd-sns-sqs/validation/README.md`

**Purpose:**  
Integrate **metadata validation gates** directly into event-driven auto-updates so every **SNS→SQS** ingestion message **self-verifies FAIR+CARE, STAC/DCAT, security, and PROV-O lineage** before any object can move from `work` → `processed` → `stable`.

</div>

---

## 📘 Overview

This standard defines the **validation-gate layer** for the atmospheric NODD SNS→SQS ingestion path in KFM:

- Each SQS message is treated as a **deterministic validation envelope**.  
- Gate functions (A..E) enforce:
  - **Schema fitness** (STAC 1.x, DCAT 3.0, KFM extensions).  
  - **FAIR fitness** (findable, accessible, interoperable, reusable).  
  - **CARE & sovereignty** constraints (masking, H3 generalization, tribal review).  
  - **PROV-O lineage fitness** (wasGeneratedBy, inputs, config, energy).  
  - **Security & supply chain** (SLSA, SBOM, signatures).  
- Only envelopes that pass all gates within a configured watermark window are **promoted** to `stable` and indexed in STAC/DCAT and the KFM graph.

This is a **pipeline-level enforcement standard**: implementations may vary by language or infra, but gate semantics and ordering are normative.

---

## 🗂️ Directory Layout

```text
📂 docs/pipelines/atmo/nodd-sns-sqs/validation/
├── 📄 README.md                      # 🛡️ FAIR+CARE Validation Gates (this file)
├── 📂 policies/                      # YAML policy sets referenced by envelopes
│   └── 📄 default.yaml               # Default validation policy for NODD SNS→SQS
└── 📂 runbooks/                      # Operational playbooks for gate failures
    ├── 📄 gate-failure-triage.md
    └── 📄 replay-procedures.md

📂 src/pipelines/common/validation/
└── 📄 gates.py                       # Shared deterministic gate library (A..E)

📂 docs/policies/validation/
└── 📄 *.yaml                         # Project-wide validation policies

📂 schemas/validation/
└── 📄 pipeline-validation-v1.json    # Normalized envelope & gate-result schema

📂 data/tests/fixtures/validation/
└── 📄 *.json                         # Fixtures for Great Expectations & CI tests
```

Any new validation gate or policy profile must be reflected in this layout and documented here.

---

## 🧭 Context

The NODD SNS→SQS ingestion flow sits early in the atmospheric pipeline:

> SNS (source events) → SQS (ingest queue) → WAL + Validation Gates (A..E) → Promotion → STAC/DCAT index → Graph upsert → Story Nodes & Focus Mode

This standard ensures that:

- Promotion from `work`/`processed` to `stable` is **not** just a successful ETL run, but a **governed decision** based on FAIR+CARE, security, and provenance.  
- Validation logic is **deterministic and idempotent**, matching the queue-centric architecture standard.  
- Validation outcomes are **observable and replayable**, with telemetry, WAL, and CLI tools wired in.

It directly depends on:

- **Queue-centric architecture** (for WAL, DLQ, replays).  
- **OpenLineage integration** (for PROV-O alignment).  
- **Geoprivacy / geospatial masking** (for H3 and sensitive-site policies).  
- **Energy and security standards** (for energy_span and SLSA/SBOM checks).

---

## 🧱 Architecture

### 1. Gate design (deterministic & idempotent)

#### 1.1 Trigger envelope (SQS message)

The normalized validation envelope includes:

- `event_time`  
- `dataset_id`  
- `source_uri`  
- `checksum`  
- `attestation_ref`  
- `policy_set_ref`  
- `protection_level` (e.g., `public_default`, `heritage_sensitive`, `restricted`)  
- `h3_policy_profile`  
- `watermark`  

**Idempotency / WAL key:**

```text
${dataset_id}:${event_time}:${checksum}
```

This key indexes WAL entries and deduplication; processing the same envelope multiple times must be side-effect safe.

#### 1.2 Gate A — Schema fitness

Gate A validates **schema and metadata fitness**:

- Enforces **STAC 1.x / DCAT 3.0** required fields plus KFM extensions (energy, carbon, sovereignty).  
- Rejects on missing:
  - `license`  
  - `provenance.activity`  
  - `spatial`  
  - `temporal`  
  - `keywords`  
  - `lineage.inputs`  

Failures emit structured reports and never promote to `stable`.

#### 1.3 Gate B — FAIR checks

Gate B enforces FAIR:

- **Findable**  
  - Persistent IDs (URNs or stable URLs).  
  - Search keywords and catalog indexability fields.  
- **Accessible**  
  - Access URL reachable (HTTP 200/206).  
  - Byte-range support where required.  
- **Interoperable**  
  - CRS declared.  
  - Media types and STAC media links correct.  
  - JSON-LD context or equivalent where applicable.  
- **Reusable**  
  - License present and parsable.  
  - Usage notes.  
  - Version and citation information.

#### 1.4 Gate C — CARE & sovereignty

Gate C enforces CARE and sovereignty rules:

- Checks:
  - `care.labels[]`  
  - `indigenous_rights.review_state`  
  - `masking.policy` for sensitive sites.  
- Enforces **dynamic H3 generalization** and redaction when `protection_level != public_default`.  
- Blocks promotion when:
  - `tribal_review_required == true` and `review_state != approved`.  
  - Masking/H3 rules are missing or non-compliant with `h3_policy_profile`.

#### 1.5 Gate D — PROV-O lineage

Gate D validates PROV-O alignment:

- Requires a `wasGeneratedBy` activity with:
  - `softwareAgent`  
  - `config_digest`  
  - `inputs[]` (with hashes or identifiers)  
  - `energy_span` (linking to energy telemetry, per energy standards).  

Incomplete or missing lineage facets fail Gate D.

#### 1.6 Gate E — Security & supply chain

Gate E enforces security and supply-chain rules:

- Requires:
  - SLSA attestation link (`attestation_ref`).  
  - SBOM reference (e.g., via `sbom_ref` in metadata).  
  - Dependency policy pass (no disallowed packages/versions).  
  - Signature verification for relevant artifacts.

Any failure triggers a security-focused `validation_error` event.

#### 1.7 Decision logic

A message is eligible for promotion only when:

- Gates A, B, C, D, E all return **pass**.  
- `event_time` lies within a configured **watermark window** for the dataset (e.g., `t_low <= event_time <= t_high`).

Outcomes:

- **Pass:**  
  - `PROMOTE → stable`  
  - STAC/DCAT index update  
  - Graph upsert transaction  
- **Fail:**  
  - Object remains in `work`/`processed`.  
  - Emit `validation_error` event.  
  - Record `validation_report.json` and replayable WAL entry.

### 2. Reference flow (SNS→SQS→Gates→Promotion)

```text
SNS (source emits)
  → SQS (ingest queue; FIFO + content-based dedup)
    → WAL Append (idempotency key)
      → Gate A..E (strict deterministic order)
        → [pass] Promote + STAC/DCAT index + Graph upsert
        → [fail] Quarantine + Error Topic + Replay Ticket
```

Gate execution order is strictly **A → B → C → D → E**. No short-circuiting outside of hard failures; all gate results are recorded for observability.

### 3. Implementation notes (KFM)

**Locations**

- Gate library:  
  - `src/pipelines/common/validation/`  

- Policies and schemas:  
  - `docs/policies/validation/*.yaml`  
  - `schemas/validation/pipeline-validation-v1.json`  

- CI hooks:  
  - `.github/workflows/docs-lint.yml`  
  - `.github/workflows/kfm-ci.yml` (pre-merge gate tests)

**Contracts**

- Input:  
  - SQS message → normalized envelope (JSON) conforming to `pipeline-validation-v1.json`.  
- Output on pass:  
  - `promotion_receipt.json` with checksums, watermarks, latency, gates passed.  
- Output on fail:  
  - `validation_report.json` (per-gate results) + `prov_violation.jsonld` where applicable.

---

## 📦 Data & Metadata

### 1. Envelope schema (minimum fields)

The normalized envelope MUST at minimum support:

- `event_time` (RFC 3339).  
- `dataset_id` (URN or stable identifier).  
- `source_uri`.  
- `checksum` (e.g., `sha256:<hash>`).  
- `attestation_ref`.  
- `policy_set_ref`.  
- `protection_level`.  
- `h3_policy_profile`.  
- `watermark`.

### 2. Watermarks

Event-time watermarks are maintained per dataset:

- Promote only when `t_event` satisfies configured bounds (e.g., no promotion of **too late** or **too early** backfill records).  
- Watermark state should be stored in a lineage-aware store (e.g., OpenLineage facet or dedicated config entity).

### 3. Promotion receipt (minimum)

Example promotion receipt:

```json
{
  "dataset_id": "urn:kfm:data:atmo:goes-16:abi-l2",
  "version": "2025.12.05",
  "commit_sha": "<sha>",
  "watermark": "2025-12-05T03:10:00Z",
  "gates_passed": ["schema", "fair", "care", "prov", "supply_chain"],
  "stac_item_ref": "data/stac/collections/goes-16/items/...",
  "graph_upsert_tx": "neo4j:tx:abcd-1234",
  "energy_span_kwh": 0.047
}
```

Receipts MUST:

- Be stored in a queryable location (e.g., `data/processed/atmo/...` or a dedicated receipts store).  
- Include a reference to the corresponding envelope and OpenLineage run.

---

## 🌐 STAC, DCAT & PROV Alignment

This validation standard is explicitly tied to STAC/DCAT/PROV:

- **STAC / DCAT**
  - Gate A checks required fields and KFM extensions (license, spatial, temporal, keywords, lineage).  
  - Promotion updates:
    - STAC Collections/Items in `data/stac/...`.  
    - DCAT Datasets/Distributions in relevant catalogs.  

- **PROV-O**
  - Gate D ensures the presence of:
    - `prov:Activity` for generation (`wasGeneratedBy`).  
    - `prov:Entity` references for inputs and outputs.  
    - `prov:Agent` for software agents and configurations.  
  - Failed PROV checks generate `prov_violation.jsonld` for governance review.

- **OpenLineage**
  - Gate results can be attached as facets to OpenLineage run events:
    - e.g., `validation.gates_passed`, `validation.gates_failed`, `validation_policy_ref`.

This alignment ensures that promotion decisions are visible and reproducible across catalogs, graphs, and lineage dashboards.

---

## 🧪 Validation & CI/CD

### 1. Telemetry & SLOs

Gate and promotion telemetry:

- Emit OpenTelemetry spans for:
  - `gate.schema` (A), `gate.fair` (B), `gate.care` (C), `gate.prov` (D), `gate.security` (E).  
  - `promotion` and `quarantine`.  

- SLOs (minimum):
  - Gate latency p95 ≤ 800 ms.  
  - False-pass rate = 0 (no known misclassified failures).  
  - Mean time to clear replayable failures ≤ 24 hours.

Metrics should be schema-aligned with `pipeline-validation-v1.json` and aggregated per dataset and gate.

### 2. Test matrix (Great Expectations + fixtures)

Fixtures live in:

```text
data/tests/fixtures/validation/
```

Great Expectations / validation suites include:

- `stac_required_fields.yaml`  
- `fair_care_profile.yaml`  
- `prov_lineage_minimum.yaml`  
- `sovereignty_masking.yaml`  
- `slsa_attestation.yaml`  

CI must:

- Run these suites as part of pre-merge checks.  
- Block changes that break validation policies.

### 3. CLI (deterministic replay)

A CLI must exist to replay validation deterministically:

```bash
kfm-validate run \
  --envelope /path/envelope.json \
  --policy docs/policies/validation/default.yaml \
  --report out/validation_report.json \
  --promote-on-pass
```

CLI behavior:

- Uses the same gate ordering and logic as the SNS→SQS path.  
- Writes `validation_report.json` and (on pass) `promotion_receipt.json`.  
- Does not perform promotion when `--promote-on-pass` is omitted (dry-run mode).

---

## ⚖ FAIR+CARE & Governance

### 1. Sensitive data guardrails

For heritage-sensitive or otherwise restricted layers:

- `protection_level ∈ {heritage_sensitive, restricted}` requires:
  - `care.masking_applied == true`.  
  - `h3_policy_profile` compliance with geoprivacy/geoethics standards.  
- Raw coordinates are **disallowed** in `stable` for such datasets:
  - Only generalized geometries (H3 aggregates, buffered regions, or redacted geometries) are permitted.  

Gate C is responsible for enforcing these constraints before graph upsert or STAC/DCAT promotion.

### 2. Governance hooks

This validation standard integrates with:

- **FAIR+CARE Council**  
  - Reviews and updates CARE and sovereignty policies applied in Gate C.  
- **Data Governance Board**  
  - Owns overall promotion and dataset lifecycle policies.  
- **Security & supply-chain standards**  
  - Gate E must remain in sync with SLSA/SBOM/security bulletins.

Any change to gates, policy structures, or required fields must:

- Be documented in this file and in `docs/policies/validation/*.yaml`.  
- Include CI/CD updates and updated fixtures.  
- Receive approval from relevant governance bodies.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                 |
|--------:|------------|-------------------|-----------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Initial KFM-MDP v11.2.4–aligned FAIR+CARE validation gate standard.  |

Future revisions must:

- Document any changes to gate definitions, ordering, or required fields.  
- Update references to telemetry and validation schemas.  
- Capture governance decisions that materially affect promotion logic.

---

<div align="center">

🛡️ **KFM v11.2.4 — FAIR+CARE Validation Gates for SNS→SQS Auto-Updates**  
Self-Verifying Promotion · Deterministic Validation · FAIR+CARE & Security Enforced  

[📘 Docs Root](../../../../..) · [⚙ Pipelines Index](../../../README.md) · [🔁 Queue Architecture](../../../core/queue-architecture/README.md) · [⚖ Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>