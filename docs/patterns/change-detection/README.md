---
title: "🧭 KFM — Change Detection Patterns (Low‑Noise Upstream Δ · Idempotent Handling · Manifest Diff)"
path: "docs/patterns/change-detection/README.md"

version: "v11.2.6"
last_updated: "2025-12-17"

release_stage: "Stable / Governed"
lifecycle: "Long‑Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-change-detection-patterns"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Reliability & FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM-MDP v12"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../releases/v11.2.6/change-detect-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/change-detect-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/governance/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../../docs/standards/governance/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../../docs/security/SECURITY.md"

semantic_document_id: "kfm-pattern-change-detection-index-v11.2.6"
doc_uuid: "urn:kfm:doc:pattern:change-detection:index:v11.2.6"
immutability_status: "mutable-plan"
---

# 🧭 KFM — Change Detection Patterns

## 📘 Overview

**Purpose:** Provide a **low-noise, governance-friendly** way to detect upstream object changes and safely process them with an **idempotent handler** so that:
- duplicates/retries are harmless,
- promotions are auditable (PROV/OpenLineage),
- rollbacks are deterministic (manifest/delta-based).

**Audience:** Data Engineering · Reliability · Pipeline Maintainers · Domain Stewards · Governance reviewers.

**Scope:** Detection + handling patterns for pipeline stages:
**ETL ingest → STAC/DCAT/PROV catalogs → graph load → API exposure → UI/Story Nodes**.

**Non-goals:**
- UI-side polling or browser-based change detection.
- Frontend access to the graph (all UI change status flows through APIs).
- “Magic” freshness claims without provenance and timestamps.

**What this folder covers**
- Choosing a detector (ETag vs events vs manifest diff) with realistic noise expectations.
- A single idempotent “do work once” handler contract used behind *every* detector.
- Minimal lineage artifacts emitted per detected change.
- Deterministic rollback semantics (manifest/delta apply + revert).

**Canonical patterns in this area**
- **Low‑Noise Change Detection & Idempotent Handler Pattern**  
  See: `./idempotent-handler/README.md`

**Related KFM patterns**
- Provenance graph diffing for ETL-run deltas: `../provenance/graph-diff/README.md`
- Golden-record tests for drift control: `../../testing/golden-record/README.md`

---

## 🗂️ Directory Layout

~~~text
docs/patterns/change-detection/
├── README.md
└── idempotent-handler/
    └── README.md
~~~

**Where implementations usually live (code)**
- Detector implementations: `src/pipelines/**` or `tools/**` (depending on whether the detector is runtime or CI-only).
- Deterministic test suites: `tests/**` (top-level integration) and/or `src/**/tests/**` (module-local).
- Incremental payloads / deltas (data): `data/updates/**` (for dataset update payloads) and `data/stac/**` (catalogs), as applicable.

> Note: This index documents **patterns and contracts**. It does not grant permission to bypass governance review.

---

## 🧭 Context

### Why “low-noise” matters

Change detection is a reliability feature *and* a governance feature. High-noise detectors create:
- unnecessary promotions,
- confusing lineage,
- reviewer fatigue,
- “false freshness” in Story Nodes.

KFM prefers detection that is:
- **cheap to evaluate**, and
- **stable under retries**, and
- **explainable in lineage**.

### Detector selection (what to use when)

| Detector | Best for | Noise profile | What you trust | What you must not assume |
|---|---|---|---|---|
| **Object-store events** (S3/GCS/Azure) | First-party buckets you control | Very low (push) | Provider event_id + object versioning | Delivery is exactly-once (it is not) |
| **HTTP ETag / If-None-Match** | Public HTTP(S) sources | Low–Medium | Server-supplied token; cache semantics | That ETag is a strong content hash (often not) |
| **Manifest/listing diff** | Batch drops, folder-based releases | Medium | Your manifest hashing + stable listing rules | That listing order is stable without canonicalization |

### The invariant: detector ≠ handler

Detectors only answer: **“Should I attempt processing?”**

The idempotent handler answers: **“Have I already produced the effects for this exact object identity?”**  
This separation prevents duplicate promotions when:
- events are delivered twice,
- polling overlaps,
- a retry happens after a partial failure.

### Idempotency key guidance

Use an idempotency identity that is stable and auditable:

**Recommended (strong):**
- `(source_uri, checksum_sha256)` once bytes are fetched, or
- `(source_uri, object_version_id)` when the store guarantees version immutability.

**Avoid (weak):**
- `Last-Modified` alone,
- weak ETags (`W/`),
- timestamps as identifiers.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Upstream Objects\nHTTP / Object Store / Batch Drop] --> B[Detector\nETag | Events | Manifest Diff]
  B --> C[Idempotency Gate\nWAL / Ledger / State Store]
  C -->|new| D[Fetch + Strong Digest\nSHA-256]
  D --> E[Deterministic Validation\nSchema | Geo | QA | Security]
  E -->|pass| F[Stage + Normalize\nContent-addressed]
  F --> G[Catalog Update\nSTAC/DCAT]
  G --> H[Minimal Provenance\nOpenLineage + PROV]
  H --> I[Promotion\nTiered store / release]
  E -->|fail| R[Rollback Action\nSingle, deterministic]
  C -->|already processed| N[No-op\nsafe exit]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Goal

Story Nodes and Focus Mode must be able to answer:
- **What changed?**
- **When did it change?**
- **Why should I trust this update?**
- **Can I roll back?**

### Required UI-facing contract

Do **not** push graph internals to the frontend. Instead:
- publish change outcomes through **API endpoints** backed by catalog/provenance artifacts, and
- make every “freshness” claim traceable to:
  - a run timestamp,
  - an input identifier,
  - a delta/manifest reference.

### Recommended fields to expose via API responses

- `change_event_id` (detector-provided or KFM-generated)
- `detected_at`
- `source_uri`
- `object_identity` (e.g., version id and/or sha256)
- `delta_manifest_ref` (points to the reversible delta)
- `qa_summary` (high-level, non-sensitive)
- `prov_ref` and `openlineage_ref` (links, not embedded blobs)

### Story Node guidance

- If a Story Node references a dataset layer affected by a delta:
  - Show **“Updated on <date>”** with a link to provenance.
  - Show a **QA disclaimer** when anomalies or incomplete coverage are flagged.
  - For sensitive topics/places: apply masking/aggregation rules and avoid precise coordinates unless permitted.

---

## 🧪 Validation & CI/CD

### Minimum CI expectations (pattern-level)

A change-detection implementation should be considered “promotion-safe” only if it has:

1. **Deterministic tests**
   - fixed seeds (when randomness exists),
   - stable ordering for manifests,
   - reproducible hashes.

2. **Idempotency tests**
   - same event delivered twice → same final state,
   - crash between “stage” and “commit” → safe retry,
   - partial manifest pages → no missing/duplicate items after reconciliation.

3. **Policy gates (OPA/Conftest)**
   - required catalog fields present,
   - checksums attached,
   - provenance emitted or explicitly waived (waivers must be reviewed).

4. **Drift guards**
   - golden-record tests for key datasets where regression risk is high,
   - schema invariants (JSON Schema / Pandera / GX) enforced.

### CI artifacts to persist (recommended)

- `artifacts/change-detect/<run-id>/detector.json`
- `artifacts/change-detect/<run-id>/manifest.json`
- `artifacts/change-detect/<run-id>/stac-delta/`
- `artifacts/change-detect/<run-id>/provenance.prov.jsonld`
- `artifacts/change-detect/<run-id>/openlineage.json`

> Store human-readable summaries as well as machine payloads. Reviewers should not need to parse raw logs.

---

## 📦 Data & Metadata

### Change event payload (recommended shape)

~~~json
{
  "change_event_id": "evt_2025-12-17T01:23:45Z_abc123",
  "detector": "etag|event|manifest",
  "source": "http|s3|gcs|azure|filesystem",
  "source_uri": "https://example.org/data/file.tif",
  "version_hint": "etag-or-object-version",
  "detected_at": "2025-12-17T01:23:45Z",
  "received_at": "2025-12-17T01:23:47Z",
  "content_digest": {
    "algorithm": "sha256",
    "value": "<computed-after-fetch>"
  },
  "content_length_bytes": 1234567,
  "notes": "Optional, non-sensitive"
}
~~~

### Manifest diff record (recommended)

A manifest diff should be **order-independent** and **hash-stable**:

~~~json
{
  "manifest_id": "man_2025-12-17_kfm-aq-pm25",
  "generated_at": "2025-12-17T01:30:00Z",
  "listing_basis": "bucket-listing|api-list|git-tree",
  "canonical_sort": "uri_asc",
  "entries": [
    {
      "uri": "s3://bucket/key1",
      "version": "v123",
      "checksum_sha256": "<optional-if-known>",
      "size_bytes": 111
    }
  ],
  "manifest_checksum_sha256": "<sha256-of-canonical-json>"
}
~~~

### Deterministic rollback target

Rollback must reference a **single source of truth**, typically:
- a delta manifest (what was applied), or
- a prior manifest (what should exist).

Never define rollback as “delete everything from last hour.”

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (minimal fields to attach)

Attach change detection + idempotency context in `properties` and in `assets`:

- `properties.kfm:change_detection.detector`
- `properties.kfm:change_detection.detected_at`
- `properties.checksum:sha256`
- `assets.provenance` (PROV JSON-LD)
- `assets.openlineage` (OpenLineage event JSON)
- `links` to delta manifest (apply/revert unit)

### DCAT (distribution updates)

For catalog-level datasets:
- Each promoted artifact is a `dcat:Distribution`
- Each distribution includes checksum and media type
- Distributions are versioned and linked to provenance artifacts

### PROV (minimal lineage expectations)

At minimum, each successful change-handling run should express:

- **Entity**: the upstream object (as observed)
- **Entity**: the normalized/staged artifact (content-addressed)
- **Activity**: the handler run (deterministic, versioned)
- **Agent**: the pipeline identity (service account / runner)

~~~json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "urn:kfm:entity:source:obj": {
      "prov:label": "source_uri",
      "kfm:uri": "https://example.org/data/file.tif"
    },
    "urn:kfm:entity:artifact:sha256:...": {
      "prov:label": "staged_artifact",
      "kfm:checksum_sha256": "..."
    }
  },
  "activity": {
    "urn:kfm:activity:change-detect:run:...": {
      "prov:label": "change-detection-handler",
      "kfm:detector": "etag"
    }
  },
  "wasGeneratedBy": {
    "_:wgb1": {
      "prov:entity": "urn:kfm:entity:artifact:sha256:...",
      "prov:activity": "urn:kfm:activity:change-detect:run:..."
    }
  }
}
~~~

---

## 🧱 Architecture

### Building blocks

1. **Detector**
   - produces a change-event candidate
   - must be cheap and safe to retry

2. **State store (idempotency ledger/WAL)**
   - tracks `(identity → status)`
   - statuses should support: `pending`, `finalized`, `failed`, `rolled_back`

3. **Idempotent handler**
   - validates deterministically
   - stages artifacts content-addressed
   - emits minimal lineage
   - performs an atomic commit (or a single rollback action)

4. **Catalog writer**
   - updates STAC/DCAT through governed contracts
   - never requires frontend to talk directly to the graph

5. **Rollback**
   - one command / one action
   - uses a delta manifest as the reversible unit

### Implementation reference

Use the canonical handler skeleton in:
- `./idempotent-handler/README.md`

This index intentionally does not duplicate the full skeleton to avoid divergence.

### Common failure modes to design for

- Duplicate events (at-least-once delivery)
- Retry storms after transient errors
- Partial listing pages / pagination drift
- Weak ETags or broken Last-Modified headers
- Large manifests (must canonicalize and checksum)

---

## ⚖ FAIR+CARE & Governance

### FAIR

- **Findable:** Change events must link to catalog IDs and stable artifact IDs.
- **Accessible:** Access constraints must be explicit (do not infer).
- **Interoperable:** Use KFM-STAC / KFM-DCAT / KFM-PROV profiles.
- **Reusable:** Provide provenance + QA notes + deterministic rollback.

### CARE / sovereignty

- Avoid leaking sensitive locations, identifiers, or restricted materials via:
  - verbose logs,
  - public delta manifests,
  - “helpful” UI freshness tooltips.

- If a dataset has restrictions:
  - keep deltas in restricted storage tiers,
  - only expose aggregated/non-sensitive summaries to public views,
  - require documented approvals for promotions.

### Governance expectations

- Promotion gates should treat “unexplained change” as a risk signal.
- Required artifacts (or waivers) must be reviewable.
- No governance overrides embedded in code paths.

---

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---:|---|---|
| v11.2.6 | 2025-12-17 | Standardized formatting; added index content and contracts for detectors/handler/rollback alignment | <name/handle> |

---

<div align="center">

**Navigation**  
[⬅️ Docs Index](../../README.md) ·
[📂 Patterns](../README.md) ·
[🧭 Change Detection](./README.md) ·
[🧾 Provenance Graph Diff](../provenance/graph-diff/README.md) ·
[✅ Golden-Record Tests](../../testing/golden-record/README.md)

**Governance & Policy**  
[⚖️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🧭 FAIR+CARE Guide](../../standards/governance/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/governance/INDIGENOUS-DATA-PROTECTION.md) ·
[🛡️ Security](../../security/SECURITY.md)

© 2025 Kansas Frontier Matrix

</div>