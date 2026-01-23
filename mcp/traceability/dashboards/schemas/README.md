<!-- 📍 File: mcp/traceability/dashboards/schemas/README.md -->

# 📊 Traceability Dashboard Schemas (MCP) 🧬

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-2020--12-blue)
![Dashboards](https://img.shields.io/badge/dashboards-📈-informational)
![Traceability](https://img.shields.io/badge/traceability-⛓️-success)
![Policy Gates](https://img.shields.io/badge/policy%20gates-fail--closed-critical)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%2B%20DCAT%20%2B%20PROV-brightgreen)

> [!IMPORTANT]
> This folder is the **schema registry** for the telemetry, manifests, and reports that power **traceability dashboards** across KFM (Kansas Frontier Matrix) and MCP (Master Coder Protocol).  
> If it shows up in a dashboard, it must be **machine-validatable** and **back-traceable** to evidence. 🧾✅

---

## 🧭 Where we are

```text
📦 mcp/
 └─ 🧬 traceability/
     └─ 📊 dashboards/
         └─ 🧾 schemas/   👈 you are here
```

---

## 🎯 Purpose

This directory defines **dashboard-facing data contracts** (JSON Schemas) for:

- 📜 **Telemetry** (append-only NDJSON events)  
- 🧪 **Run manifests** (exact pipeline inputs/outputs + hashes)  
- 🧭 **Provenance & lineage** (STAC + DCAT + PROV cross-links)  
- 🧱 **Graph integrity** (weekly graph health checks, schema drift, orphan/dangling refs)  
- 🔐 **Policy & governance** (OPA/Conftest decisions, fail-closed gates, audit trail)  
- 🧠 **AI traceability** (Focus Mode citations, drift, governance ledger entries)  
- 🧵 **Narrative traceability** (Pulse Threads, evidence manifests, concept activations)

These schemas are the “shape of truth” dashboards rely on—so dashboards can be **reliable**, **comparable**, and **portable** across environments (local/dev/staging/prod). 🧰📦

---

## 🧬 Why schemas matter here

KFM’s architecture is explicitly **contract-first** and **provenance-first**—anything presented in the UI or AI responses must be traceable back to cataloged sources, using open standards like **STAC**, **DCAT**, and **PROV**.[^kfm-contract]  
That same rule applies to dashboards: dashboards are “UI for operations,” so they must also be **provable**.

---

## 🗺️ Traceability → Dashboards: high-level dataflow

```mermaid
flowchart LR
  A[🗂️ Sources] --> B[⚙️ Pipeline Run]
  B --> C[📜 telemetry.ndjson]
  B --> D[🧪 run_manifest.json]
  B --> E[🧭 Evidence Triplet<br/>STAC + DCAT + PROV]

  D --> F[🔐 Policy Gates<br/>(OPA/Conftest)]
  E --> F

  E --> G[🕸️ Neo4j Knowledge Graph]
  G --> H[🧱 Graph Health Check Report]

  F --> I[📘 Governance Ledger]
  C --> J[📊 Dashboards]
  D --> J
  F --> J
  H --> J
  I --> J

  G --> K[🧑‍💻 UI Panels]
  G --> L[🤖 Focus Mode]
  L --> M[🧾 Answer Trace + Citations]
  M --> J
```

---

## 📦 What belongs in this folder

✅ **YES** (dashboard contract schemas)
- `*.schema.json` files for dashboard payloads/events/manifests/reports  
- A “common envelope” schema used by most payloads  
- Minimal example payloads (small + realistic) for CI validation

❌ **NO** (belongs elsewhere)
- Full STAC/DCAT/PROV canonical schemas (we *reference* them; don’t duplicate)  
- Raw telemetry/event logs (those are artifacts produced by runs)  
- UI component code (dashboards consume schemas, not define them)

---

## 📏 Schema conventions

### 1) Schema draft + IDs
- Target: **JSON Schema Draft 2020-12** (unless a specific consumer requires otherwise)
- Every schema should include:
  - `$schema`
  - `$id`
  - `title`
  - `type`
  - `required`
  - `additionalProperties` (prefer `false` for dashboard contracts)

### 2) Versioning rules (SemVer)
- `schema_version`: `"MAJOR.MINOR.PATCH"`
- Breaking change → bump MAJOR
- Additive change → bump MINOR
- Fix/clarify → bump PATCH

### 3) Deterministic & replayable
Subsystem contracts emphasize **deterministic pipelines**, validation gates, and stable “shape rules” for the graph.[^subsystem-contracts]  
Dashboards should be able to replay history by ingesting:
- `telemetry.ndjson` (event stream)
- `run_manifest.json` (exact artifacts + hashes)
- report artifacts (graph health, policy decisions, etc.)

### 4) Cross-link everything
Every dashboard payload must link to at least one of:
- `run_id` (pipeline run identity)
- `dataset_id` / catalog IDs
- `artifact.digest` (content-addressed identity)
- PROV IDs (`prov.activity_id`, `prov.entity_id`, `prov.agent_id`)

---

## 🧱 Common envelope (recommended)

Most dashboard payloads should follow a shared envelope shape (either via `$ref` or copy/paste for early MVP).

**Recommended fields**:

| Field | Type | Why it exists |
|---|---:|---|
| `schema` | string | Canonical schema name (`kfm.trace.telemetry_event`) |
| `schema_version` | string | SemVer for compatibility |
| `ts` | string (date-time) | Event/report timestamp |
| `env` | object | build/release context (`git_sha`, `deployment`, etc.) |
| `run_id` | string | Correlates everything to a pipeline run |
| `correlation_id` | string | Joins across services (API ↔ pipeline ↔ UI) |
| `actor` | object | human/agent/service identity |
| `severity` | string | `DEBUG`/`INFO`/`WARN`/`ERROR` |
| `labels` | object | small, indexed tags for dashboards |

> [!TIP]
> **Dashboards love stable keys.** Prefer stable identifiers (`run_id`, `dataset_id`, `digest`) over human text.

---

## 🧾 Schema inventory

> Status legend: ✅ MVP | 🧪 Experimental | 🧭 Roadmap

| Schema file (proposed) | Status | Producer | Dashboard consumers | Notes |
|---|---:|---|---|---|
| `telemetry_event.schema.json` | ✅ | pipeline/agents | pipeline health, latency, failures | Append-only NDJSON events for run activity[^ndjson] |
| `run_manifest.schema.json` | ✅ | pipeline/agents | reproducibility, lineage | Tracks input/output artifacts + canonical digest + idempotency key[^run-manifest] |
| `evidence_triplet.schema.json` | ✅ | catalog builder | provenance coverage | STAC + DCAT + PROV alignment contract[^evidence-triplet] |
| `policy_decision.schema.json` | ✅ | policy gate | compliance dashboard | OPA/Conftest decisions; fail-closed semantics[^policy-gates] |
| `governance_ledger_entry.schema.json` | ✅ | governance layer | audit dashboard | Immutable ledger for AI outputs + decisions[^gov-ledger] |
| `graph_health_report.schema.json` | ✅ | scheduled job | graph integrity dashboard | Weekly health checks, schema drift, orphan/dangling edges[^graph-health] |
| `graph_schema_contract.schema.json` | ✅ | graph team | drift detection | Expected labels/properties types; used to detect “hand edits”[^graph-health] |
| `focus_answer_trace.schema.json` | ✅ | AI layer | trust dashboard | Answer → citations → datasets → PROV activities[^ai-trace] |
| `model_drift_report.schema.json` | 🧪 | AI eval job | trust dashboard | drift + citation coverage + performance[^focus-telemetry] |
| `pulse_thread.schema.json` | 🧭 | narrative service | narrative dashboard | Mini-stories with provenance & “trust but verify” controls[^pulse] |
| `evidence_manifest.schema.json` | ✅ | narrative service | narrative dashboard | Manifest (often YAML) describing exact evidence & transformations[^evidence-manifest] |
| `concept_activation.schema.json` | 🧪 | AI/narrative | research dashboard | Tracks “conceptual attention nodes” activation for explainability[^concepts] |
| `artifact_attestation.schema.json` | 🧭 | build/release | supply-chain dashboard | OCI/ORAS artifacts + Cosign signatures for reports/manifests[^oci] |

---

## 📊 Dashboard panels mapped to schemas

| Dashboard panel | Key questions it answers | Schemas |
|---|---|---|
| ⚙️ Pipeline Health | What’s running? What failed? How long? | `telemetry_event`, `run_manifest` |
| 🧭 Provenance Coverage | What % of layers have STAC/DCAT/PROV? | `evidence_triplet`, `policy_decision` |
| 🧱 Graph Integrity | Orphans? Dangling edges? Schema drift? | `graph_health_report`, `graph_schema_contract` |
| 🔐 Compliance & Governance | What was blocked? Why? Who approved? | `policy_decision`, `governance_ledger_entry` |
| 🤖 Focus Mode Trust | Are answers cited? Any drift/regressions? | `focus_answer_trace`, `model_drift_report` |
| 🧵 Narrative Integrity | Do Pulse Threads link to evidence manifests? | `pulse_thread`, `evidence_manifest` |
| 🧾 Supply Chain Integrity | Are artifacts signed? Which digest is deployed? | `artifact_attestation`, `run_manifest` |

---

## 🧪 Validation, CI, and “fail closed” behavior

Policy and governance gates are described as automated checks (e.g., Conftest/OPA) that **fail closed**—if rules fail or evidence is missing, the pipeline should block publication.[^policy-gates]

Recommended CI checks for this folder:
1. ✅ JSON Schema validity check (draft 2020-12)
2. ✅ Example payload validation against schemas
3. ✅ Backward compatibility check (for non-breaking changes)
4. ✅ “No unknown fields” enforcement for dashboard contracts
5. ✅ Lint rules (naming, required fields, timestamps)

---

## 🔐 Supply-chain integrity (optional but powerful)

Project proposals include storing and distributing **report artifacts** (run manifests, graph health checks, etc.) as **OCI artifacts**, moved via **ORAS** and signed via **Cosign**.[^oci]

Why dashboards care:
- Dashboards can verify the digest + signature before trusting a report
- Report history becomes content-addressable and tamper-evident
- Makes it easier to share QA artifacts across environments/regions

---

## 🧠 AI + UI traceability: contract expectations

### Focus Mode traceability
AI system plans emphasize that results should be linked to sources, and that AI outputs can be logged to an immutable governance ledger for audit.[^ai-trace][^gov-ledger]

Dashboards should expect:
- `answer_id` (stable)
- `citations[]` with stable IDs/digests
- `datasets[]` referenced by catalog IDs
- `prov.activity_id` linking analysis steps
- `policy_decision_id` (if gated)
- `confidence` fields (and a “verify” affordance)

### UI dashboards & provenance
UI documentation describes “standard schemas” and linking each visualization back to source metadata, plus dashboard integrations for monitoring and administration.[^ui-standard][^ui-dashboard]

---

## 🧵 Narrative traceability: Pulse Threads & evidence manifests

Pulse Threads / narrative patterns propose **mini-stories** and “trust but verify,” where story nodes link to an `evidence_manifest` and PROV bundle.[^pulse][^evidence-manifest]

Dashboards should answer:
- Which narratives lack evidence manifests?
- Which evidence items are missing digests?
- Which narratives cite datasets not present in the catalog?
- Which narratives changed without updated evidence?

---

## 🧩 Adding a new schema (checklist)

1. 🧾 Create `your_schema_name.schema.json`
2. 🧰 Use the common envelope (or document deviations)
3. 🧪 Add **at least 2 example payloads**:
   - ✅ happy path
   - ❌ failure/edge case (e.g., missing evidence)
4. 🔗 Ensure every payload links to a `run_id` and at least one stable artifact/dataset identity
5. 🔐 If a policy gate applies, include the policy decision reference
6. ✅ Update the **Schema Inventory** table above

---

## 🗂️ Suggested folder layout (future-friendly)

```text
🧾 schemas/
 ├─ README.md
 ├─ 🧩 common/
 │   └─ envelope.schema.json
 ├─ 📜 events/
 │   └─ telemetry_event.schema.json
 ├─ 🧪 manifests/
 │   ├─ run_manifest.schema.json
 │   ├─ evidence_triplet.schema.json
 │   └─ evidence_manifest.schema.json
 ├─ 🧱 reports/
 │   ├─ graph_health_report.schema.json
 │   └─ model_drift_report.schema.json
 ├─ 🔐 governance/
 │   ├─ policy_decision.schema.json
 │   └─ governance_ledger_entry.schema.json
 └─ 🧪 examples/
     ├─ telemetry_event.ok.json
     ├─ telemetry_event.fail.json
     └─ ...
```

---

## 🧾 Example payloads (copy/paste starters)

<details>
<summary><strong>📜 Telemetry event (NDJSON line)</strong></summary>

```json
{
  "schema": "kfm.trace.telemetry_event",
  "schema_version": "1.0.0",
  "ts": "2026-01-23T17:15:12Z",
  "env": { "deployment": "dev", "git_sha": "abc123" },
  "run_id": "run_2026-01-23T17:14:58Z_8f31",
  "correlation_id": "corr_6b9a",
  "severity": "INFO",
  "event_type": "pipeline.step.complete",
  "step": { "name": "catalog.publish", "duration_ms": 1423 },
  "artifact": { "uri": "s3://kfm/audits/run_.../run_manifest.json", "digest": "sha256:..." },
  "labels": { "pipeline": "intake", "dataset_id": "kfm.dataset.ks.usgs_gauges" }
}
```
</details>

<details>
<summary><strong>🧪 Run manifest (determinism + hashing)</strong></summary>

```json
{
  "schema": "kfm.trace.run_manifest",
  "schema_version": "1.0.0",
  "ts": "2026-01-23T17:16:00Z",
  "run_id": "run_2026-01-23T17:14:58Z_8f31",
  "idempotency_key": "sha256:9a8b...",
  "canonical_digest": "sha256:9a8b...",
  "config_hash": "sha256:4f1c...",
  "input_artifacts": [
    { "uri": "https://example.gov/data/source.zip", "digest": "sha256:1111..." }
  ],
  "output_artifacts": [
    { "uri": "s3://kfm/catalog/stac/item.json", "digest": "sha256:2222..." }
  ],
  "policy_decisions": ["pol_2026-01-23_01"],
  "prov": { "activity_id": "prov:run_8f31", "agent_id": "kfm:agent:intake_bot" }
}
```
</details>

<details>
<summary><strong>🧱 Graph health report (weekly)</strong></summary>

```json
{
  "schema": "kfm.trace.graph_health_report",
  "schema_version": "1.0.0",
  "ts": "2026-01-23T00:00:00Z",
  "run_id": "healthcheck_2026-01-23",
  "graph": { "db": "neo4j", "snapshot_digest": "sha256:aaaa..." },
  "counts": { "nodes": 124533, "edges": 851220 },
  "integrity": {
    "orphan_nodes": 12,
    "dangling_edges": 3,
    "constraint_violations": 0,
    "schema_drift": { "new_properties": ["kfm:foo"], "missing_required": [] }
  },
  "artifacts": [
    { "uri": "docs/reports/qa/graph_health/2026-01-23/summary.md", "digest": "sha256:bbbb..." },
    { "uri": "docs/reports/qa/graph_health/2026-01-23/index.csv", "digest": "sha256:cccc..." }
  ],
  "severity": "WARN"
}
```
</details>

---

## 📚 Project doc pack used (quick links)

> [!NOTE]
> The bullets below intentionally include **chat “filecite” markers** so you can open the exact uploaded source docs from this conversation.  
> If you paste this README into the repo, you can safely remove this whole `<details>` section later. ✂️

<details>
<summary><strong>📎 Sources (chat artifacts)</strong></summary>

### Core KFM system docs
-  [oai_citation:0‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`
-  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`
-  [oai_citation:2‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`
-  [oai_citation:3‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) `Document Refinement Request (Pulse Threads / Graph Health / OCI ideas)`

### Additional KFM references discovered in the pack
-  [oai_citation:4‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH) `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`
-  [oai_citation:5‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`
-  [oai_citation:6‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`

### PDF “resource libraries” (background / implementation references)
-  [oai_citation:7‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2) `AI Concepts & more.pdf`
-  [oai_citation:8‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi) `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`
-  [oai_citation:9‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6) `Various programming langurages & resources 1.pdf`
-  [oai_citation:10‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr) `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`

</details>

---

## 🧾 Evidence notes (footnotes)

[^kfm-contract]: KFM explicitly adopts **contract-first** and **provenance-first** rules; “anything that shows up in UI or Focus Mode” must be traceable, and open standards (STAC/DCAT/PROV) are called out as the backbone for metadata + lineage. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^subsystem-contracts]: The subsystem contract description highlights deterministic ETL, schema validation gates, and stable contracts that downstream UI/dashboards rely on. [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^ndjson]: Telemetry is described as an append-only JSON Lines (NDJSON) stream that can feed dashboards/audits. [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
[^run-manifest]: Run manifests are proposed as canonical JSON (e.g., `data/audits/<run_id>/run_manifest.json`) with an idempotency key and canonical digest (RFC 8785 canonicalization + hash). [oai_citation:15‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
[^evidence-triplet]: The intake spec references an evidence approach aligned with STAC/DCAT/PROV and treats provenance as non-optional for publishing and consumption. [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
[^policy-gates]: Policy is described as automated governance gates (Conftest/OPA) that can fail closed when provenance or required constraints are missing; this also includes STAC/DCAT/PROV completeness expectations. [oai_citation:18‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
[^graph-health]: Weekly graph health checks and report artifacts (e.g., `docs/reports/qa/graph_health/...`) are proposed, including checks like orphan nodes, dangling edges, and schema drift detection. [oai_citation:20‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
[^ai-trace]: The AI system overview emphasizes traceable, evidence-backed answers and linking results back to sources for transparency. [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:23‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
[^gov-ledger]: The AI system overview proposes logging outputs and decisions into an immutable governance ledger for auditability. [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
[^focus-telemetry]: The intake guide discusses QA/metrics and Focus Mode telemetry (e.g., citation coverage, drift), feeding monitoring dashboards. [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
[^ui-standard]: The UI overview calls out that visualizations should link to their source metadata and that components rely on standard schemas for extensibility.
[^ui-dashboard]: The UI overview also discusses dashboard integration (health monitoring, administrative views, “Kansas Environmental Dashboard” concept). [oai_citation:26‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
[^pulse]: Pulse Threads / conceptual attention nodes / narrative pattern detection are described as narrative + provenance constructs meant to be tracked and surfaced with verification affordances. [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:28‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
[^concepts]: Conceptual Attention Nodes / activation tracking is described as a way to surface why the system highlights certain themes (an explainability signal dashboards can aggregate). [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
[^evidence-manifest]: Evidence manifests (often YAML) are described as explicit inventories of supporting material and transformations, shown in the UI via “View Evidence,” with stable IDs/checksums and PROV links back into the graph. [oai_citation:30‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
[^oci]: Proposals include storing/managing artifacts (manifests/reports) as OCI artifacts and signing them with Cosign (supply-chain integrity). [oai_citation:31‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
[^mcp-traceability-matrix]: MCP documentation recommends a traceability matrix linking experiment IDs/features to code version, data/model versions, and result references—this folder’s schemas are designed to feed that table and keep it automatable. [oai_citation:32‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) [oai_citation:33‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)
