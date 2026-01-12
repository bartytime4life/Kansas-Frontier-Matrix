---
title: "📡 KFM Telemetry Standards"
path: "docs/standards/telemetry/README.md"
version: "v1.1.0"
last_updated: "2026-01-12"
status: "draft"
doc_kind: "Standard"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:standards:telemetry:readme:v1.1.0"
semantic_document_id: "kfm-standards-telemetry-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:standards:telemetry:readme:v1.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

<div align="center">

# 📡 **KFM Telemetry Standards**
`docs/standards/telemetry/README.md`

**Telemetry = Governance + Observability**  
Schema-first signals for *reproducibility, diagnostics, security auditing, and FAIR+CARE compliance*.

<img alt="Status" src="https://img.shields.io/badge/status-draft-yellow" />
<img alt="Telemetry" src="https://img.shields.io/badge/telemetry-v1.1.0-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-brightgreen" />
<img alt="Schema First" src="https://img.shields.io/badge/schema--first-required-informational" />
<img alt="OpenTelemetry" src="https://img.shields.io/badge/OpenTelemetry-aligned-5e5eea" />

</div>

> [!IMPORTANT]
> This is a **normative** standard. Keywords **MUST / SHOULD / MAY** are used in the RFC-style sense.  
> Telemetry is **operational metadata** — it is *not* evidence/truth for Story Nodes.

---

## 🧭 Quick Navigation

- 🎯 [Purpose](#-purpose)
- 🧩 [Scope](#-scope)
- 🧱 [KFM invariants telemetry must respect](#-kfm-invariants-telemetry-must-respect)
- 📁 [Directory layout](#-directory-layout)
- 🧬 [Telemetry model](#-telemetry-model)
- 🧾 [Minimum event envelope](#-minimum-event-envelope)
- 🏷️ [Naming rules](#-naming-rules)
- 🧷 [STAC/DCAT/PROV alignment](#-stacdcatprov-alignment)
- 🛡️ [Sensitivity, redaction, and sovereignty](#-sensitivity-redaction-and-sovereignty)
- ✅ [Validation & CI/CD](#-validation--cicd)
- 🩺 [Ops runbooks & SLOs](#-ops-runbooks--slos)
- 🗃️ [Event registry starter set](#-event-registry-starter-set)
- 🕰️ [Version history](#-version-history)
- 📎 [References](#-references)

---

## 🎯 Purpose

KFM telemetry standards define **how operational, security, and governance signals are**:

- ✅ **Named** (consistent event_type taxonomy)
- ✅ **Structured** (schema-first JSON envelopes)
- ✅ **Classified** (FAIR+CARE + sovereignty-safe labels)
- ✅ **Validated** (CI + runtime validators)
- ✅ **Linked** to pipeline artifacts (run IDs, dataset IDs, STAC/DCAT/PROV references)

Telemetry exists to support:

- 🔁 **Reproducibility** (run tracking, deterministic pipelines, idempotency verification)
- 🧰 **Operational diagnostics** (latency, failures, performance regressions)
- 🔐 **Security + governance auditing** (who/what/when under what access rules)
- 🌿 **Sustainability accounting** (energy + carbon signals as first-class QA outputs)

---

## 🧩 Scope

| ✅ In Scope | 🚫 Out of Scope |
|---|---|
| Event/metric taxonomy & envelope requirements | Vendor selection / specific SaaS products |
| Schema-first validation & schema versioning rules | Dashboard UX, alert thresholds (document elsewhere) |
| Classification & redaction rules for telemetry payloads | Organization-wide ethics policy authorship (governance docs own that) |
| Linkage to pipeline artifacts (run_id, dataset_id, STAC/DCAT, PROV) | Secrets management, credential rotation (security runbooks own that) |
| CI telemetry quality gates & minimum SLO reporting | Business analytics unrelated to KFM runtime/governance |

### 👥 Audience
- **Primary:** Platform / DataOps / Pipeline engineers; API/UI engineers emitting telemetry
- **Secondary:** Security reviewers; FAIR+CARE governance reviewers; domain stewards

### 📚 Definitions (glossary pointers)
- If present, see: `docs/glossary.md`
- Key terms in this standard: telemetry, event, metric, trace, log, envelope, schema_id, run_id, provenance, classification, redaction

---

## 🧱 KFM invariants telemetry must respect

Telemetry MUST not violate KFM’s “non-negotiables”:

1) **Canonical pipeline ordering (absolute):**  
`ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode`  
No stage may leapfrog/bypass prior stages’ contracts/outputs.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

2) **API boundary rule:**  
UI must never query Neo4j directly; UI telemetry must flow via the API boundary (contracted).  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

3) **Provenance-first:**  
Published artifacts must be registered in STAC/DCAT + PROV before graph/UI/story usage.  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

4) **Sovereignty & classification propagation:**  
No output artifact (including telemetry) may be less restricted than its inputs; redaction is end-to-end.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

5) **Evidence-first narrative:**  
Telemetry can *support audits*, but it does not become narrative evidence without proper catalog/provenance linkage.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📁 Directory layout

### 📄 This document
- `docs/standards/telemetry/README.md` ✅

### 🔗 Related repository paths (expected)
| Area | Path | What lives here |
|---|---|---|
| Telemetry runbooks | `docs/telemetry/` | Dashboards, SOPs, incident notes, SLOs |
| Telemetry schemas | `schemas/telemetry/` | JSON Schemas, semver’d, changelogged |
| UI schema contracts | `api/contracts/schemas/ui/` | UI event schemas (Focus Mode, map UX, etc.) |
| STAC schema contracts | `api/contracts/schemas/stac/` | STAC profile & validations for KFM |
| OpenAPI contracts | `api/contracts/openapi/` | API boundary definitions, telemetry ingestion endpoints |
| Pipelines | `src/pipelines/` | ETL + catalog jobs emitting telemetry |
| Graph | `src/graph/` | Ontology bindings, ingest/migrations, graph health telemetry |
| Server/API | `src/server/` | Ingestion endpoints, authz decisions, redaction enforcement |
| Validation tools | `tools/validation/` | Schema validators, policy gates, catalog QA |
| Provenance bundles | `data/prov/` | PROV artifacts referenced by telemetry |

### 🗂️ Expected file tree
```text
📁 docs/
└── 📁 standards/
    └── 📁 telemetry/
        └── 📄 README.md

📁 docs/
└── 📁 telemetry/
    ├── 📄 runbooks.md
    ├── 📄 slos.md
    └── 📄 incident-playbooks.md

📁 schemas/
└── 📁 telemetry/
    ├── 📄 envelope.telemetry-event.v1.schema.json
    ├── 📄 event.pipeline-run.v1.schema.json
    ├── 📄 event.api-request.v1.schema.json
    ├── 📄 event.ui-focus-mode.v1.schema.json
    └── 📄 README.md
```

---

## 🧬 Telemetry model

KFM treats telemetry as **multi-modal**:

- 🧾 **Events** (discrete facts: “policy denied”, “pipeline finished”)
- 📈 **Metrics** (counters/gauges/histograms: latency_ms, bytes_processed)
- 🧵 **Traces** (end-to-end causality across services: trace_id/span_id)
- 🪵 **Logs** (human-readable + structured, but MUST still be governable)

> [!NOTE]
> **Schema-first** is the default: events SHOULD be emitted as structured JSON that validates against `schemas/telemetry/**`.

### 🧠 Components that emit telemetry
KFM’s architecture is modular (pipeline/catalog/graph/API/UI/Focus Mode). Telemetry MUST identify **which component** emitted it and how it maps to system structure.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)

Recommended `component` values:
- `etl`, `catalog`, `prov`, `graph`, `api`, `ui`, `story`, `focus`, `agent`, `mcp`, `policy`, `ci`, `security`, `telemetry`

---

## 🧾 Minimum event envelope

All telemetry **events** MUST conform to a shared **envelope** schema (authoritative schema lives under `schemas/telemetry/`).

### ✅ Required fields (MUST)

| Field | Type | Why it exists |
|---|---|---|
| `schema_id` | string (URI) | Declares schema contract (semver’d) |
| `event_id` | string | Idempotency + deduplication |
| `event_time` | string (RFC3339) | Ordering + audit |
| `event_type` | string | Taxonomy lookup + routing |
| `severity` | enum | Filtering + incident triage |
| `component` | string | Producer identity |
| `classification` | enum | Redaction + access control decisions |
| `run_id` | string | Reproducibility linkage |

### ⭐ Strongly recommended fields (SHOULD)

| Field | Type | Notes |
|---|---|---|
| `trace` | object | trace_id/span_id to correlate across services |
| `actor` | object | hashed/abstracted identity + role (no PII) |
| `dataset` | object | dataset_id + sensitivity metadata |
| `provenance` | object | PROV activity/entity pointers |
| `artifacts` | object | commit_sha, sbom_ref, manifest_ref |
| `metrics` | object | small numeric payload; prefer metrics pipeline for heavy stats |
| `message` | string | short human-readable summary |
| `details` | object | bounded-size structured details |

---

## 🧪 Canonical event envelope (illustrative)

> [!WARNING]
> This JSON is an **illustration**. The authoritative contract MUST live in `schemas/telemetry/` and be validated in CI.

```json
{
  "schema_id": "urn:kfm:schema:telemetry:envelope:v1.0.0",
  "event_id": "01J1Y4...stable-or-uuid",
  "event_time": "2026-01-12T00:00:00Z",
  "event_type": "pipeline.run.completed",
  "severity": "info",
  "component": "etl",
  "classification": "open",
  "run_id": "run_2026-01-12T00:00:00Z_abc123",

  "trace": {
    "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
    "span_id": "00f067aa0ba902b7",
    "parent_span_id": null
  },

  "actor": {
    "actor_type": "human|service|agent",
    "actor_id_hash": "sha256:…",
    "role": "public_viewer|contributor|admin|ci_bot"
  },

  "dataset": {
    "dataset_id": "kfm.ks.topic.year_range.v3",
    "stac_item_id": "optional",
    "dcat_dataset_id": "optional",
    "sensitivity": "public|internal|confidential|restricted"
  },

  "provenance": {
    "prov_activity_id": "prov:activity:…",
    "prov_entity_ids": ["prov:entity:…"]
  },

  "artifacts": {
    "commit_sha": "<latest-commit-hash>",
    "sbom_ref": "releases/<ver>/sbom.spdx.json",
    "manifest_ref": "releases/<ver>/manifest.zip"
  },

  "metrics": {
    "duration_ms": 8421,
    "records_processed": 120034
  },

  "message": "ETL run completed successfully",
  "details": {}
}
```

---

## 🏷️ Naming rules

### `event_type` naming
Events MUST use **dot-delimited**, lower-case, stable naming:

**Format:**  
`<domain>.<subject>.<action>[.<state>]`

Examples:
- `pipeline.run.started`
- `pipeline.stage.completed`
- `catalog.stac.validation.failed`
- `api.request.completed`
- `ui.focus_mode.loaded`
- `policy.gate.denied`
- `security.authz.denied`

### `schema_id` naming
Schemas MUST be semver’d and referenced by stable URNs:

**Recommended format:**  
`urn:kfm:schema:telemetry:<name>:v<MAJOR>.<MINOR>.<PATCH>`

Examples:
- `urn:kfm:schema:telemetry:envelope:v1.0.0`
- `urn:kfm:schema:telemetry:event.ui-focus-mode:v1.0.0`
- `urn:kfm:schema:telemetry:event.policy-gate:v1.0.0`

### `dataset_id` naming (KFM convention)
When telemetry references datasets, it SHOULD use the KFM dataset naming pattern (example shown in audit):  
`kfm.ks.topic.year_range.v#`  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧷 STAC/DCAT/PROV alignment

Telemetry MUST be “cross-layer linkable” when it refers to pipeline artifacts.

### 🌐 STAC
Telemetry SHOULD reference STAC when events concern:
- STAC collection/item creation/validation
- Asset ingestion, indexing, integrity checks (broken links, missing assets)

Recommended fields:
- `dataset.stac_item_id`
- `dataset.stac_collection_id`

### 🧾 DCAT
If telemetry is published as datasets (optional future), it SHOULD have DCAT records describing:
- Owner/publisher
- Update cadence
- Access restrictions & license

### 🧬 PROV-O
Telemetry SHOULD link to provenance where available:
- `provenance.prov_activity_id` (pipeline run)
- `provenance.prov_entity_ids` (inputs/outputs)
- `artifacts.commit_sha` (code provenance)

> [!TIP]
> KFM already emphasizes “catalogs + PROV bundles as boundary artifacts.” Telemetry should reference those boundaries rather than re-encoding them.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🛡️ Sensitivity, redaction, and sovereignty

Telemetry MUST NOT become a covert channel for restricted data.

### 🚫 Prohibited content in telemetry (MUST NOT)
- Secrets: tokens, keys, credentials
- Direct PII: names, emails, phone numbers (unless explicitly governed/approved)
- Raw sensitive geometries/coordinates derived from restricted sources
- Full prompts/responses containing sensitive data (AI systems)

### ✅ Required controls
1) **Classification label is mandatory** (`classification` + optional `sensitivity` detail).  
2) **No downstream loosening of restrictions**: telemetry classification cannot be lower than the strictest input classification.  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
3) **Redaction is end-to-end**: redaction may occur in processed data, metadata, API, and UI layers.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
4) **Audit trails are expected**: emit events when sensitive data is accessed, redactions occur, or publication is blocked.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧊 Location generalization guidance (SHOULD)
If a telemetry event must reference location:
- Prefer stable IDs (STAC item IDs, graph entity IDs)
- Prefer generalized geometry (e.g., coarse H3 cell ID / bounding box / rounded coords)
- Never store exact coordinates for restricted sites

### 🧩 Actor identity (privacy-safe)
Telemetry SHOULD avoid storing direct user identifiers. A privacy-preserving pattern is to store:
- `actor_id_hash` (e.g., sha256 of a stable internal ID + salt)
- role + actor_type
- optional “context hash” for access decisions (see data spaces pattern)  [oai_citation:11‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)

---

## 🔐 Policy gates & telemetry-driven governance

KFM’s roadmap includes CI policy gates (OPA/Conftest) and governance monitoring signals. Telemetry MUST be compatible with policy enforcement patterns, including:  
- emitting `policy.gate.*` events  
- emitting `security.authz.*` events  
- emitting `catalog.validation.*` events  
 [oai_citation:12‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Recommended policy telemetry fields:
- `policy.policy_id` (versioned)
- `policy.decision` (`allow|deny`)
- `policy.reason_codes` (bounded list)
- `policy.review_required` (boolean)

---

## 🩺 Ops runbooks & SLOs

KFM treats telemetry as a **first-class QA output**, including sustainability metrics. A proposed runbook pattern is a scheduled “10-minute telemetry health check” verifying that CI runs emit OpenTelemetry traces and energy/carbon usage data; suggested minimum SLOs include **95% trace coverage** and **90% steps reporting energy usage**.  [oai_citation:14‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

### ✅ Minimum operational checks (SHOULD)
- Trace completeness for CI runs (presence of expected spans/attributes)
- Energy report presence for CI runs (where enabled)
- Schema validity rate for emitted events
- Alert on missing telemetry for critical pipelines

> [!NOTE]
> Sustainability alignment references ISO energy + carbon tracking standards as part of governance direction; implementers should treat these as “governance-aligned telemetry targets” even if the storage stack is still evolving.  [oai_citation:15‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)

---

## ✅ Validation & CI/CD

Telemetry changes MUST be testable and repeatable.

### 🔒 Required CI gates (MUST)
- JSON Schema validation for `schemas/telemetry/**`
- Contract compatibility checks for schema changes (semver rules)
- Secret scanning for telemetry fixtures/examples
- Governance checks for sensitivity leaks (policy gate)

### 🧪 Recommended CI gates (SHOULD)
- “Telemetry quality” report: schema pass-rate, missing field rate, volume anomalies
- Idempotency/dedup tests (event_id stability)
- Trace linkage tests (run_id ⇄ trace_id ⇄ prov_activity_id)

### 🧰 Example command scaffold
```bash
# examples — align with repo’s actual tooling

# 1) validate telemetry schemas
make validate-telemetry-schemas

# 2) validate sample events against schema (fixtures)
make validate-telemetry-fixtures

# 3) run policy checks (OPA/Conftest)
make policy-gate

# 4) run contract tests for API telemetry ingestion endpoints
make test-telemetry-contracts
```

---

## 🗃️ Event registry starter set

> [!TIP]
> This is a **starter registry**. The authoritative registry SHOULD be encoded as schema enums (or a schema registry doc) to enable automated validation.

### 🧱 Pipeline & catalog
| Event type | When emitted | Notes |
|---|---|---|
| `pipeline.run.started` | pipeline run begins | include run_id, commit_sha |
| `pipeline.run.completed` | run ends successfully | include duration + outputs |
| `pipeline.run.failed` | run ends with error | include bounded error codes |
| `pipeline.stage.started` | stage begins | stage_name required |
| `pipeline.stage.completed` | stage ends | include metrics |
| `catalog.stac.validation.passed` | STAC validates | link STAC IDs |
| `catalog.stac.validation.failed` | STAC fails | include schema_id + reason |
| `catalog.dcat.validation.passed` | DCAT validates | link DCAT ID |
| `catalog.dcat.validation.failed` | DCAT fails | bounded failure codes |
| `prov.bundle.written` | PROV artifact created | include prov_activity_id |

### 🧠 Graph & ontology
| Event type | When emitted | Notes |
|---|---|---|
| `graph.ingest.started` | graph ingest begins | reference prov activity |
| `graph.ingest.completed` | ingest success | nodes/edges counts |
| `graph.constraint.violated` | constraint fails | no sensitive payloads |
| `ontology.mapping.missing` | ontology mismatch | points to schema / mapping |

### 🌐 API boundary
| Event type | When emitted | Notes |
|---|---|---|
| `api.request.received` | request enters API | request_id + route |
| `api.request.completed` | request completes | status_code + latency |
| `api.redaction.applied` | redaction performed | include redaction_type |
| `security.authz.denied` | access denied | include policy_id + reason |

### 🗺️ UI + Focus Mode
| Event type | When emitted | Notes |
|---|---|---|
| `ui.app.loaded` | UI boot complete | performance timing |
| `ui.map.layer.toggled` | layer on/off | use stable layer IDs |
| `ui.focus_mode.loaded` | Focus Mode opened | include trace link |
| `ui.focus_mode.query.submitted` | query submitted | DO NOT log raw prompt if sensitive |
| `ui.focus_mode.response.rendered` | response rendered | include citation_count |
| `focus_mode_redaction_notice_shown` | withheld/generalized output shown | sovereignty audit signal  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |

### 🤖 Agents / MCP / policy
| Event type | When emitted | Notes |
|---|---|---|
| `agent.node.started` | agent node begins | include node_id |
| `agent.node.completed` | agent node ends | include outcome |
| `agent.tool.call` | tool invoked | tool_id (no secrets) |
| `agent.tool.denied` | tool blocked by governance | include policy_id |
| `mcp.request.started` | MCP request begins | include mcp_server |
| `mcp.request.completed` | MCP request ends | include duration |
| `policy.gate.denied` | CI policy gate denies | include reason codes |

### 🌿 Sustainability / energy
| Event type | When emitted | Notes |
|---|---|---|
| `sustainability.energy.report.generated` | energy report created | include step coverage |
| `sustainability.carbon.estimated` | carbon estimate produced | units required |

---

## 🧾 Examples (copy/paste friendly)

<details>
<summary><strong>✅ Example: Policy gate denial</strong> (click to expand)</summary>

```json
{
  "schema_id": "urn:kfm:schema:telemetry:event.policy-gate:v1.0.0",
  "event_id": "deny_2026-01-12_abc123",
  "event_time": "2026-01-12T03:21:09Z",
  "event_type": "policy.gate.denied",
  "severity": "warn",
  "component": "ci",
  "classification": "internal",
  "run_id": "ci_run_abc123",
  "policy": {
    "policy_id": "urn:kfm:policy:care-redaction:v2.1.0",
    "decision": "deny",
    "reason_codes": ["SENSITIVE_GEOMETRY_UNREDACTED"],
    "review_required": true
  },
  "message": "Policy gate denied promotion: sensitive geometry not redacted",
  "details": {}
}
```
</details>

<details>
<summary><strong>✅ Example: Focus Mode redaction notice</strong> (click to expand)</summary>

```json
{
  "schema_id": "urn:kfm:schema:telemetry:event.ui-focus-mode:v1.0.0",
  "event_id": "focus_redaction_notice_001",
  "event_time": "2026-01-12T10:02:44Z",
  "event_type": "focus_mode_redaction_notice_shown",
  "severity": "info",
  "component": "ui",
  "classification": "open",
  "run_id": "session_9f3c",
  "actor": { "actor_type": "human", "actor_id_hash": "sha256:…", "role": "public_viewer" },
  "message": "Focus Mode withheld precise location details due to sovereignty rules",
  "details": { "redaction_type": "geometry_generalized" }
}
```
</details>

---

## 🧠 Open questions (tracked work)

| Question | Owner | Target date |
|---|---|---|
| What is the authoritative telemetry sink pattern (OTel collector + storage)? | TBD | TBD |
| Retention rules per classification class? | Governance + Security | TBD |
| Which telemetry schemas are baseline-required under `schemas/telemetry/`? | Telemetry WG | TBD |
| Do we catalog telemetry as DCAT datasets and PROV activities? | DataOps | TBD |
| How do we standardize energy/carbon measurement collection across CI and runtime? | Platform | TBD |

---

## ✅ Producer checklist (quick compliance)

- [ ] Emits telemetry in structured JSON (schema-first)
- [ ] Includes required envelope fields (`schema_id`, `event_id`, `event_time`, `event_type`, `severity`, `component`, `classification`, `run_id`)
- [ ] Links to STAC/DCAT/PROV identifiers when relevant
- [ ] Never emits secrets/PII/sensitive coordinates
- [ ] Uses stable naming conventions for `event_type`
- [ ] Includes trace linkage (trace_id/span_id) where possible
- [ ] Emits governance signals for redaction, authz denies, policy blocks

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.0 | 2026-01-12 | Added governance-aligned taxonomy, policy gate + energy telemetry, envelope hardening, and KFM invariant alignment | TBD |
| v1.0.0 | 2025-12-20 | Initial telemetry standards README | TBD |

---

## 📎 References

Project sources used to ground this standard:

- KFM v13 master structure + invariants + telemetry-driven governance notes:  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- KFM technical architecture context (Focus Mode, pipeline, modular structure):  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)
- KFM repo audit summary (contract-first + standards alignment; dataset naming convention example):  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:20‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)
- Roadmap proposals (telemetry health check + energy/carbon SLOs; policy pack OPA/Conftest):  [oai_citation:21‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)  [oai_citation:22‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)
- Data spaces access-control hashing pattern (privacy-safe context validation):  [oai_citation:23‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq)

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
