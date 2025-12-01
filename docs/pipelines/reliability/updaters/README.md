---
title: "🧬 KFM v11.2.3 — Deterministic Updaters, WAL & Lineage-Safe Writes (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/reliability/updaters/README.md"
version: "v11.2.3"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x updater-contract compatible"

status: "Active / Enforced"
doc_kind: "Reliability Pattern · Pipeline Contract"
intent: "deterministic-updaters-wal-lineage"

classification: "Internal Reliability Document"
sensitivity: "Low"
fair_category: "F1-A1-I2-R2 · FAIR: Findable, Accessible, Interoperable, Reusable"
care_label: "CARE: Collective Benefit, Authority to Control, Responsibility, Ethics"
care_label_detail: "CARE-Level 2 — Responsible Operational Data Handling"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded by next updater-contract revision"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../releases/v11.2.3/reliability-updaters-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/reliability/updaters-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-doc-reliability-updaters"
doc_uuid: "urn:kfm:pipeline:reliability:updaters:v11.2.3"

machine_extractable: true

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "OpenLineage"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/reliability/updaters/README.md@v11.2.2"
  - "docs/pipelines/reliability/updaters/README.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false
---

<div align="center">

# 🧬 KFM v11.2.3 — Deterministic Updaters, WAL & Lineage-Safe Writes  

**Triggers → Pure Plans → WAL-backed Execution → Idempotent Upserts → Neo4j Lineage → SLO Telemetry**

<br/>

<img alt="Docs-MCP" src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blueviolet"/>
<img alt="Markdown" src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.2-4444aa"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Active-green"/>
<img alt="License" src="https://img.shields.io/badge/License-CC--BY_4.0-ffcc00"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active_/_Enforced-brightgreen"/>

</div>

---

## 📘 1. Purpose & Scope

This document standardizes **deterministic, WAL-backed updater pipelines** used across the Kansas Frontier Matrix (KFM):

- Same inputs → same outputs (**determinism**).  
- Every side-effect is preceded by a **Write-Ahead Log (WAL)** event.  
- All writes are **idempotent** and safe to **retry** or **replay**.  
- Each run emits **Neo4j lineage** (DCAT / PROV-O compatible).  
- Each run emits **OpenTelemetry + energy/carbon** metrics for SLOs.  
- Focus Mode can reconstruct **reproducible narratives** from lineage.

This is a **pattern + contract** doc, not an implementation manual for a single language.  
Individual services (Python, Rust, Node, etc.) MUST implement the behaviors defined here.

---

## 🗂 2. Directory Layout

~~~text
docs/pipelines/reliability/updaters/
│
├── 📄 README.md                                  # This file — deterministic updaters contract
│
├── 🧬 patterns/                                  # Pattern deep-dives & specialization notes
│   ├── 📄 wal-replay-strategies.md               # WAL replay, crash recovery, partial re-runs
│   ├── 📄 idempotent-upserts.md                  # Business-key + content-hash patterns
│   ├── 📄 concurrency-locks.md                   # Advisory locks, leases, shard keys
│   └── 📄 focus-mode-integration.md              # Story Node & Focus Mode fabric integration
│
├── 📐 specs/                                     # Formal contracts & schemas
│   ├── 📄 updater-interface.md                   # Language-agnostic Updater interface
│   ├── 📄 wal-record-schema.md                   # WAL event schema (JSON / Avro / Parquet)
│   ├── 📄 lineage-cypher-templates.md            # Neo4j Cypher snippets (PROV-O / DCAT)
│   └── 📄 telemetry-schema.md                    # Metric/event schema (OpenTelemetry, energy)
│
├── 🧪 examples/                                  # Worked examples
│   ├── 📄 sentinel1-coherence-daily.md           # Daily SAR coherence tiles updater
│   ├── 📄 climate-downscaling-hrrr.md            # HRRR → downscaled climate tiles updater
│   └── 📄 stratigraphy-profiles.md               # Archaeology stratigraphy ingest & lineage
│
└── ✅ checklists/                                # Operational readiness & change safety
    ├── 📄 rollout-readiness.md                   # Pre-deploy checks for new/changed updaters
    ├── 📄 canary-playbook.md                     # Canary, kill-switch, rollback patterns
    └── 📄 governance-review.md                   # FAIR+CARE & data-governance approvals
~~~

---

## 🧩 3. Deterministic Updater Interface (Abstract Contract)

All KFM updater implementations MUST conform to the following **logical interface**  
(names can differ per language, but behavior MUST match).

~~~text
interface Updater {
  /// Stable logical name for this updater
  id: string

  /// Semantic version of transform logic (changing behavior ⇒ bump)
  version: string  // e.g. "1.4.0"

  /// Discover or receive inputs (URIs, hashes, partition keys, etc.)
  inputs(): SourceRef[]

  /// Pure function: same inputs ⇒ same Plan object (no I/O, no randomness)
  plan(inputs: SourceRef[]) -> Plan

  /// Execute the Plan with WAL; may be retried/replayed
  execute(plan: Plan, wal: WalHandle) -> Outputs

  /// Idempotent upsert into sinks; guarded by idempotency keys + locks
  upsert(outputs: Outputs, lock: AdvisoryLock) -> UpsertResult

  /// Emit lineage graph mutations for Neo4j (PROV-O / DCAT)
  lineage(outputs: Outputs, run_meta: RunMeta) -> CypherBatch

  /// Emit telemetry points/metrics/events (OpenTelemetry + energy/carbon)
  telemetry(run_meta: RunMeta, stats: RunStats) -> TelemetryBatch
}
~~~

### 3.1 Inputs

- **SourceRef** MUST include at least:
  - `uri`: canonical source URI (S3, lakeFS, HTTP, STAC Item ID, etc.).  
  - `content_hash`: stable hash of input payload (e.g., SHA-256).  
  - Optional partitioning keys (date, tile, H3 index, station, etc.).

### 3.2 Plan

- **Plan** is a **pure, fully derived DAG** from inputs:
  - Lists **steps**, **dependencies**, and **target keys**.  
  - Contains no external randomness or wall-clock time.  
  - Is serializable (JSON/YAML/MsgPack) and stored in WAL for replay.

- Any change in Plan for the same inputs **requires** a version bump (`version` field).

---

## 🧾 4. WAL (Write-Ahead Log) Contract

All side-effecting stages MUST be **WAL-backed**.

### 4.1 WAL Record Schema (Conceptual)

~~~text
WalRecord {
  wal_id: string            // stable per run
  seq: int                  // strictly increasing sequence number
  phase: string             // e.g. "PLAN", "EXECUTE", "UPSERT", "LINEAGE"
  step_id: string           // logical step in Plan
  updater_id: string
  updater_version: string
  input_hash: string        // hash of inputs (or sub-partition)
  payload: bytes|json       // plan fragment, step result metadata, etc.
  status: string            // "PENDING" | "IN_PROGRESS" | "DONE" | "FAILED"
  ts: string                // RFC 3339 timestamp
}
~~~

### 4.2 WAL Rules

1. **No side-effects without WAL**  
   Before any irreversible action (e.g., sink write, lineage insert), append a **WalRecord** describing the intention.

2. **Atomic WAL append**  
   WAL writes MUST be atomic (at-least-once).  
   Duplicates are acceptable if they are **idempotent** by `(wal_id, seq)`.

3. **Replay semantics**  
   On resume:
   - Read WAL for `wal_id`.  
   - Reconstruct last known Plan and step statuses.  
   - Resume from first step that is not `DONE`.

4. **Commit protocol**  
   - Perform side-effect (e.g., write to sink).  
   - Verify or read-after-write as needed.  
   - Mark corresponding WAL step `DONE`.  
   - Only after all sinks & lineage are `DONE` is the run considered **committed**.

---

## 🔒 5. Idempotent Upserts & Concurrency

### 5.1 Idempotency Keys

Each logical output MUST be uniquely identified by an **idempotency key**:

~~~text
idempotency_key = HASH(
  updater_id,
  updater_version,
  business_key,     // e.g., (dataset_id, date, tile, band)
  content_hash      // of produced payload
)
~~~

**Rules:**

- Upserts MUST be **idempotent** with respect to `idempotency_key`.  
- Retrying the same `idempotency_key` MUST NOT create duplicates or conflicting rows/documents/objects.  
- If content changes for the same `business_key`, the content hash (and thus key) changes, and **lineage and versioning** MUST reflect it.

### 5.2 Advisory Locks / Leases

For hotspots (same `business_key` being updated by concurrent workers):

- Use **advisory locks** (DB, Redis, etc.) or **short leases** on key ranges.  
- Lock scope: `(updater_id, business_key)`.  
- Locks MUST:
  - Be short-lived.  
  - Handle worker death (expiry).  
  - Be **best-effort** (idempotent upsert still protects correctness).

---

## 🧬 6. Neo4j Lineage (PROV-O / DCAT-Oriented)

### 6.1 Core Nodes & Relationships

Each run MUST create/merge:

- `(:Run)` — one per updater execution.  
- `(:Asset)` — for each input source (raw or upstream product).  
- `(:Dataset)` — for each produced artifact (STAC Item, tile, table partition, file).

Minimal pattern (simplified Cypher snippet):

~~~text
MERGE (r:Run {
  id: $run_id,
  updater_id: $updater_id,
  version: $updater_version
})
ON CREATE SET
  r.started_at = $started_at,
  r.trigger_type = $trigger_type,
  r.wal_id = $wal_id

WITH r
UNWIND $input_assets AS a
  MERGE (s:Asset { uri: a.uri, hash: a.hash })
  ON CREATE SET s.first_seen_at = $now
  MERGE (s)-[:USED_IN]->(r)

WITH r
UNWIND $outputs AS o
  MERGE (d:Dataset { key: o.key })
  ON CREATE SET d.created_at = $now
  SET d.hash = o.hash,
      d.stac_id = o.stac_id,
      d.version = o.version
  MERGE (r)-[:GENERATED]->(d)
~~~

### 6.2 FAIR+CARE Considerations

- For **sensitive archaeological or Indigenous data**, lineage writes MUST:
  - Respect **H3 generalization** policies.  
  - Attach CARE labels in metadata (e.g., `d.care_label = "Restricted / By Request"`).

- Lineage MUST NEVER expose coordinates or site identifiers that violate governance policies or sovereignty agreements.

---

## 📡 7. Telemetry & SLOs (OpenTelemetry + Energy/Carbon)

Each updater run MUST emit a minimal telemetry envelope:

~~~text
UpdatersRunTelemetry {
  run_id: string
  updater_id: string
  version: string

  status: string              // "SUCCESS" | "FAILED" | "PARTIAL" | "SKIPPED"
  failure_stage: string|null  // "PLAN" | "EXECUTE" | "UPSERT" | "LINEAGE" | null

  latency_ms: int
  retries: int
  wal_replay_count: int

  inputs_count: int
  outputs_count: int
  bytes_in: int
  bytes_out: int

  energy_kwh: float|null
  co2e_g: float|null

  slo_target_latency_ms: int
  slo_ok: bool
  error_budget_burn: float    // 0.0–1.0 for period
}
~~~

Guidance:

- Telemetry SHOULD be exportable as **OpenTelemetry metrics + logs**.  
- Energy/carbon values MAY be derived from:
  - Node/cluster metrics (CPU, GPU, memory).  
  - Region- and time-specific carbon intensity factors.

- Failed runs MUST still emit telemetry with `status = "FAILED"`.

---

## 🔀 8. End-to-End Flow (Conceptual DAG)

Conceptual updater DAG used across KFM (safe text rendering here; in-repo you MAY include a `flowchart TD`
Mermaid block directly as ```mermaid``` per KFM-MDP):

~~~text
flowchart TD
  T[Trigger: new/changed sources] --> Q[Quarantine: hash, schema, governance checks]
  Q --> P[Planner: pure Plan(inputs)]
  P --> W[Write Plan to WAL (PLAN)]
  W --> X[Executor: deterministic steps]
  X -->|WAL per step| U[Upsert: idempotent writes]
  U --> L[Lineage: Neo4j mutations]
  U --> M[Telemetry: SLO + energy/carbon]
  L --> F[Focus Mode Fabric: narrative + reproducible view]
  M --> F
~~~

---

## 🧠 9. Focus Mode & Story Nodes Integration

Deterministic updaters are first-class citizens in the **Story Node** and **Focus Mode** ecosystem.

### 9.1 Story Node Hooks

Story Nodes SHOULD be able to:

- Resolve which updaters produced a given **Dataset** (`GENERATED` edge).  
- Enumerate **inputs** and show provenance chains (raw → harmonized → derived).  
- Highlight **governance context**:
  - CARE labels.  
  - H3 generalization level.  
  - Data ownership / tribal or agency custodianship.

### 9.2 Reproducible Narratives

Focus Mode can use updater metadata to:

- Show “**How this layer was produced**”:
  - Updater ID + version.  
  - Trigger type (schedule / on-demand / anomaly).  
  - Time of last successful run.

- Offer a “**Re-run explanation**” view:
  - Not necessarily re-execute, but reconstruct explanation from WAL, Plan, and lineage.

---

## ✅ 10. Test & Operational Checklists (Condensed)

### 10.1 Determinism

- [ ] Same inputs, same version ⇒ identical Plan serialization.  
- [ ] Random seeds and wall-clock access removed or fixed in `plan()`.  
- [ ] Version bump whenever Plan semantics change.

### 10.2 WAL & Replay

- [ ] WAL records written before each side-effect.  
- [ ] Crash-injection tests between steps prove **safe replay**.  
- [ ] WAL can be compacted/archived without losing provenance.

### 10.3 Idempotent Upserts

- [ ] Idempotency keys implemented as specified.  
- [ ] N retries result in **one** materialized output.  
- [ ] Conflicts (e.g., changed content for same business key) handled by:
  - Clear versioning.  
  - Correct lineage updates.  
  - Optional soft-deletion or supersession marks.

### 10.4 Lineage & Telemetry

- [ ] Runs, assets, and datasets appear in Neo4j as expected.  
- [ ] No duplication of `Asset` nodes for same `(uri, hash)`.  
- [ ] Telemetry emitted on success **and** failure.  
- [ ] SLO dashboards wired to updater metrics.

---

## 🕰️ 11. Version History (Human Summary)

- **v11.2.3**
  - Formalized **Updater interface** and WAL/Plan semantics.  
  - Added explicit **idempotency key** formula and lock guidance.  
  - Expanded **Neo4j lineage templates** and FAIR+CARE notes.  
  - Documented **telemetry envelope** with energy/carbon fields.

- **v11.2.2**
  - Initial consolidation of updater patterns under reliability pipelines.

- **v11.0.0–v11.2.1**
  - Updater behaviors distributed across HRRR, climate, and Sentinel-1 pipeline docs.

---

## 📚 12. References & Related Documents

- Reliability root: `docs/pipelines/reliability/README.md`  
- Markdown protocol: `docs/standards/kfm_markdown_protocol_v11.2.2.md`  
- Governance root: `docs/standards/governance/ROOT-GOVERNANCE.md`  
- FAIR+CARE: `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- Sovereignty: `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`  

---

<div align="center">

🧬 **Kansas Frontier Matrix — Deterministic Updaters (v11.2.3)**  
Deterministic · WAL-Backed · Lineage-Safe · FAIR+CARE-Governed  

[📘 Docs Root](../../..) · [🧱 Reliability Root](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>