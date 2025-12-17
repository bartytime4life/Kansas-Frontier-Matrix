---
title: "🧭 KFM — Low‑Noise Change Detection & Idempotent Handler Pattern (ETag · Events · Manifest Diff)"
path: "docs/patterns/change-detection/idempotent-handler/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long‑Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-change-detection-idempotent-handler"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
classification: "Public"
jurisdiction: "Kansas / United States"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "Reliability & FAIR+CARE Council"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

semantic_document_id: "kfm-pattern-change-detect-idempotent-handler"
doc_uuid: "urn:kfm:doc:pattern-change-detect-idempotent-handler:v11.2.6"
event_source_id: "ledger:kfm:doc:pattern:change-detect-idempotent-handler:v11.2.6"
immutability_status: "mutable-plan"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/change-detect-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/change-detect-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../../../docs/security/SECURITY.md"

provenance_chain: []

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

# 🧭 KFM — Low‑Noise Change Detection & Idempotent Handler Pattern (ETag · Events · Manifest Diff)

> **Purpose:** Provide a low-noise, deterministic pattern for detecting upstream change and applying *exactly-once effects* (promotion + catalog updates) under *at-least-once triggers* (polling/events/listing diffs).
>
> **Audience:** ETL / Data Engineering, Reliability, Catalog & Provenance maintainers.
>
> **Scope:** Change detection + idempotent processing for publishing into KFM’s tiered data store, STAC/DCAT catalogs, and lineage (OpenLineage + PROV), with downstream visibility via APIs (no direct graph access from the UI).

---

## 📘 Overview

This pattern gives KFM pipelines a **practical, low‑noise way to detect new/changed upstream objects** and a **single, copy‑paste idempotent handler** that:

- **Validates** a new object deterministically (contract-first, order-invariant checks).
- **Emits** a minimal, auditable provenance bundle (OpenLineage + PROV‑JSONLD).
- **Applies** one clear **rollback** action on failure.
- **Plays nicely** with retries, reorders, and duplicates by ensuring **exactly‑once effects**.

Use this when promoting STAC/DCAT assets into lineage‑enforced storage tiers and you need **deterministic diffing** and **auditable promotions**.

### Non-goals

- Designing your entire ETL orchestration system (use existing KFM pipeline orchestration).
- Implementing a custom message bus, queue, or event router.
- Allowing frontend components to bypass APIs and query the graph or object store directly.

---

## 🗂 Directory Layout

This pattern is documentation-first. The layout below shows **recommended** placements for a reference implementation and tests in the KFM monorepo structure.

~~~text
docs/
  patterns/
    change-detection/
      idempotent-handler/
        README.md

schemas/
  telemetry/
    change-detect-v1.json
  events/
    object-change-event-v1.schema.json

tools/
  change_detection/
    handler.py
    manifest_diff.py
    etag_normalize.py
    wal_store.py
    provenance_emit.py

tests/
  change_detection/
    test_idempotent_handler.py
    test_manifest_diff.py
    fixtures/
      event_samples.json
      manifests/
        manifest_a.json
        manifest_b.json

mcp/
  runs/
    change-detection/
      <run-id>/
        wal/
        provenance/
        qa/
        logs/
~~~

---

## 🧭 Context

KFM workflows routinely ingest upstream objects via:

- Public HTTP(S) endpoints
- First‑party object stores (bucket events)
- Batch drops / catalog listings

These upstreams are **not reliable** in the ways we need:
- events may be **duplicated** or **reordered**
- polling may miss intermediate changes
- listings may be large, paginated, and partially inconsistent

So the detector MUST be treated as a **trigger** (at-least-once) and the handler MUST implement **idempotent effects**.

### Change Detectors — what to use when

| Detector | Best For | Noise Profile | Guarantees | Caveats |
|---|---|---|---|---|
| **HTTP ETag / If‑None‑Match** | Public HTTP(S) sources, object fetches | **Low** (server computes content hash/opaque token) | Cache‑friendly; cheap polling; no body download on no‑change | Some servers use *weak* ETags (`W/`) → treat as advisory; always compute strong digest after fetch |
| **Object‑store events** (S3 `PutObject`, GCS `finalize`, Azure Blob) | First‑party buckets, internal feeds | **Very low** (push) | Near‑real‑time; dedup by event ID + object version | Reorders/duplicates possible → handler MUST be idempotent |
| **Manifest/listing diffs** (list → compare keys + checksums) | Bulk drops, folder-based catalogs, “release drops” | **Medium** (depends on cadence) | Fully deterministic if manifest includes checksums | Listings can be large; page consistently; write manifests with stable ordering |

**Guideline**
- Prefer **Events** if you own the bucket.
- Fall back to **ETag** for HTTP sources.
- Use **Manifest Diff** for batch/collection workflows.
- Always couple detectors with the **same idempotent handler** so duplicates/reorders are harmless.

### Where this lives in the KFM pipeline

This pattern primarily concerns:

1. **ETL ingest & staging** (change detection, content hashing, validation)
2. **STAC/DCAT/PROV generation** (metadata + lineage)
3. **Graph ingest** (via ETL loaders, not frontend)
4. **API exposure** (frontend consumes change status only through APIs)

---

## 🗺 Diagrams

~~~mermaid
flowchart TD
  subgraph Detectors
    ETag[HTTP ETag Poller]
    Ev[Object-Store Events]
    Man[Manifest Diff]
  end

  ETag --> Env[Event Envelope]
  Ev --> Env
  Man --> Env

  Env --> WAL[WAL / Idempotency Gate]
  WAL -->|duplicate| Noop[No-op]
  WAL -->|new| Fetch[Fetch + Strong Hash]

  Fetch --> Validate[Deterministic Validation]
  Validate -->|fail| RB[Rollback Action]
  Validate -->|pass| Stage[Content-addressed Stage]

  Stage --> Prov[Emit OpenLineage + PROV]
  Prov --> Promote[Atomic Promotion]

  Promote --> STAC[STAC/DCAT Update]
  Promote --> Graph[Graph Ingest (ETL)]
  STAC --> API[APIs]
  Graph --> API
  API --> UI[Story Nodes / Focus Mode]
~~~

---

## 🧠 Story Node & Focus Mode Integration

This pattern supports Story Nodes and Focus Mode by ensuring change is:

- **Explainable:** provenance ties “what changed” to an upstream object and a run.
- **Reviewable:** promotions are gated by deterministic checks and policy.
- **Rollbackable:** catalogs and assets can be reverted safely.

### UI contract

Frontend MUST NOT query the graph or raw object store directly. It should rely on APIs that expose:

- “New/updated assets available” indicators (by Collection / layer)
- Provenance trace links (“derived from”, “generated by”)
- QA/policy outcomes (pass/fail + reason codes)
- Version / release metadata (manifest pointers)

If a Story Node references a dataset version, it SHOULD reference:
- STAC Item `id`
- Collection `id`
- and a version property or checksum (when applicable)

This supports stable citations and avoids silently changing narratives.

---

## 🧪 Validation & CI/CD

### Determinism rules (MUST)

- Validation checks MUST be **pure** (no network calls, no time-of-day dependence).
- Ordering MUST be stable (sort inputs before hashing/serializing).
- Any sampling MUST be seeded and recorded (if used).
- The handler MUST remain idempotent under:
  - duplicate events
  - reordered events
  - concurrent delivery of the same `(uri, version)`

### Policy gates (recommended)

Use OPA/Conftest (or equivalent) to enforce:

- required metadata fields present
- license + access constraints consistent
- provenance artifacts attached
- checksum fields match payload digests
- sovereignty rules applied for sensitive locations/materials

Example policy sketch (illustrative):

~~~rego
package kfm.change_detect

deny[msg] {
  input.stac_item.properties["checksum:sha256"] == ""
  msg := "missing checksum:sha256"
}

deny[msg] {
  not input.provenance.prov_jsonld_emitted
  msg := "missing PROV JSON-LD"
}

deny[msg] {
  input.security.secret_scan.passed == false
  msg := "secret scan failed"
}
~~~

### Test cases (minimum)

- **Idempotency:** same event delivered twice → second run is a no-op.
- **Concurrency:** two workers race → one wins; the other exits safely.
- **Rollback:** validation fail → staged artifacts removed AND WAL marked failed.
- **Manifest diff stability:** manifest ordering changes only → diff is empty.
- **ETag weakness:** weak ETag changes without content change → digest gate prevents false promotion.

---

## 📦 Data & Metadata

### Minimal event envelope (recommended)

Detectors should normalize into a single envelope to reduce special cases:

~~~json
{
  "source": "s3|gcs|azure|http",
  "uri": "s3://bucket/key|https://example/data.tif",
  "version": "object-version-or-etag",
  "event_id": "provider-unique-id",
  "detector": "event|etag|manifest",
  "received_at": "2025-12-16T00:00:00Z",
  "metadata": {
    "content_length": 123456,
    "content_type": "image/tiff"
  }
}
~~~

### Idempotency key (MUST)

The handler MUST derive a stable idempotency key. Recommended:

- `idempotency_key = sha256(uri + "\n" + version)`

If `version` is missing or unreliable, the handler MUST compute a strong digest and treat:

- `(uri, sha256(content_bytes))` as the dedup key

### WAL record (minimum)

The WAL is the authoritative state machine for “exactly-once effects”:

- `PENDING` → `FETCHED` → `VALIDATED` → `STAGED` → `PROMOTED` → `FINALIZED`
- On failure: `FAILED` + `ROLLBACK_APPLIED`

WAL MUST be append-only or at least audit-loggable (so reviewers can reconstruct events).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Handler SHOULD create/update a STAC Item (or Item version) with:

- `checksum:sha256` (strong digest computed by handler)
- `lineage:detector`, `lineage:version_hint`
- assets with roles such as:
  - `data`
  - `metadata`
  - `provenance`
  - `qa`
  - `sbom` (when applicable)

Example (illustrative) asset roles:

~~~json
{
  "assets": {
    "data": {
      "href": "s3://kfm-processed/.../sha256/<digest>/asset.tif",
      "roles": ["data"],
      "type": "image/tiff"
    },
    "provenance": {
      "href": "s3://kfm-provenance/.../<run-id>.prov.jsonld",
      "roles": ["provenance"],
      "type": "application/ld+json"
    }
  }
}
~~~

### DCAT

DCAT SHOULD represent promoted outputs as `dcat:Distribution` entries, each with:

- stable identifier
- media type
- checksum
- access constraints (if any)

### PROV + OpenLineage (minimal)

The handler MUST emit minimal lineage sufficient to answer:

- What inputs were used?
- What outputs were produced?
- What validations/policies were applied?
- Which run/job produced the output?

At minimum record:
- `prov:Entity` for input object reference (uri + version)
- `prov:Entity` for output promoted asset (uri + sha256)
- `prov:Activity` for the handler run (run_id, tool version, commit sha, seed if any)
- `prov:wasDerivedFrom` / `prov:used` / `prov:wasGeneratedBy` links

---

## 🧱 Architecture

### Invariants (MUST)

- **At-least-once triggers; exactly-once effects.**
- Content-addressed staging ensures the same bytes do not create multiple “different” artifacts.
- Catalog writes (STAC/DCAT) MUST be atomic with WAL finalize.
- Rollback MUST be a single, deterministic action (don’t “half rollback”).

### Minimal idempotent handler (copy‑paste skeleton)

> One function. Exactly‑once *effects* with at‑least‑once *triggers*.

~~~python
def handle_object(event: dict) -> str:
    """
    Inputs:
      event: {
        "source": "s3|gcs|http",
        "uri": "s3://bucket/key|https://example/data.tif",
        "version": "object-version-or-etag",
        "event_id": "provider-unique-id",
        "detector": "event|etag|manifest",
        "received_at": "2025-12-16T00:00:00Z"
      }
    """

    # 1) Idempotency Gate (WAL)
    # Key idea: if (uri, version) already committed OR rollback marker exists, exit.
    if wal.already_finalized(uri=event["uri"], version=event.get("version")):
        return "noop:already_finalized"

    wal.stage(event)  # writes a pending record with monotonic step

    # 2) Fetch (content-addressed)
    obj = fetch(event["uri"], version=event.get("version"))  # honor If-None-Match for HTTP where applicable

    # Always compute a strong digest (ETags may be weak/opaque).
    digest = sha256(obj.bytes)

    # 3) Deterministic Validation (contract-first)
    # All checks must be pure & order-invariant.
    checks = [
        schema.validate(obj),           # JSON Schema / Pandera / Great Expectations
        geospatial.validate_crs(obj),   # CRS, extents, resolution (if spatial)
        content.validate_expected(obj), # domain invariants (bands/columns/keys)
        security.scan(obj),             # AV/allowlist (supply-chain)
    ]
    if not all(checks):
        wal.mark_failed(event, reason="validation_failed")
        return rollback.delete_staged_assets(event)  # single rollback action

    # 4) Normalize + Stage (write-once)
    staged_uri = staging.put(obj, digest=digest)  # path includes digest to ensure immutability
    stac_item = stac.build_item(
        source_uri=event["uri"],
        staged_uri=staged_uri,
        checksum=digest,
        detector=event["detector"],
        version_hint=event.get("version"),
    )

    # 5) Emit Minimal Provenance Bundle (OpenLineage + PROV-JSONLD)
    prov = provenance.minimal_bundle(
        event=event,
        digest=digest,
        inputs=[event["uri"]],
        outputs=[staged_uri],
        validations=["schema", "crs", "content", "security"],
    )
    lineage.emit(prov)

    # 6) Commit (atomic promotion + WAL finalize)
    promoted_uri = promotion.promote(staged_uri, policy="kfm-tiered-store")
    catalog.write(stac_item.with_asset(promoted_uri))
    wal.finalize(event, result={"promoted_uri": promoted_uri, "digest": digest})
    return "ok"
~~~

### Rollback semantics (MUST)

Rollback MUST be deterministic and leave the system in one of two acceptable states:

- **No-op state:** nothing promoted; WAL indicates failure; provenance emitted (append-only).
- **Promoted state:** catalog + WAL finalized; promotion is complete and auditable.

Rollback SHOULD NOT delete provenance logs; provenance is append-only evidence.

---

## ⚖ FAIR+CARE & Governance

### FAIR

- **Findable:** Stable STAC IDs + checksums, cataloged assets.
- **Accessible:** APIs provide controlled access; access constraints are explicit.
- **Interoperable:** STAC/DCAT/PROV standard mapping is enforced.
- **Reusable:** Clear license, provenance, and validation results.

### CARE / Sovereignty

- Apply masking/aggregation where required by `sovereignty_policy`.
- Do not publish sensitive locations at full precision unless explicitly allowed.
- Ensure review cycles are followed for promoted changes in governed tiers.

### Security expectations

- No secrets/tokens in events, logs, or telemetry.
- All promotions pass policy gates before becoming discoverable.
- Supply-chain artifacts (SBOM/signatures/attestations) are referenced when release-pinned.

---

## 🕰 Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.2.6 | 2025-12-16 | Standardized fences (`~~~`), approved heading structure, and canonical footer; clarified detector selection, idempotency invariants, minimal event envelope, and rollback semantics for governed promotions. |

---

<div align="center">
🧭 **KFM — Low‑Noise Change Detection & Idempotent Handler Pattern (ETag · Events · Manifest Diff)**  
Reliable Pipelines · Deterministic Diffs · Auditable Promotions  
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" />

[📘 Docs Root](../../../README.md) ·
[🧭 Patterns Index](../../README.md) ·
[🧱 Data Architecture](../../../architecture/README.md) ·
[⚙ CI/CD Workflows](../../../workflows/README.md) ·
[🏛 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🔐 Security Policy](../../../security/SECURITY.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6
</div>