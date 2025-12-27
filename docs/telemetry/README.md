---
title: "KFM Telemetry — README"
path: "docs/telemetry/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:telemetry:readme:v1.0.0"
semantic_document_id: "kfm-telemetry-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:telemetry:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarization"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"
  - "identify_individual_users"
doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Telemetry — README

Telemetry is an **optional**, **schema-governed** subsystem for capturing operational, quality, and governance signals across the KFM pipeline:

**ETL → STAC/DCAT/PROV Catalogs → Graph (Neo4j) → API → UI → Story Nodes → Focus Mode**

This README defines:
- Where telemetry lives in the repo
- What telemetry is allowed to contain (and what it must never contain)
- The recommended **event envelope** shape (idempotent + schema-pinned)
- How telemetry ties to STAC/DCAT/PROV and Focus Mode
- CI/CD expectations for validating telemetry artifacts and release snapshots

## 📘 Overview

### Purpose
- Provide a single **contract-first** reference for telemetry conventions in KFM.
- Support:
  - **observability** (run success/failure, latency, throughput),
  - **governance evidence** (classification/redaction/promotion controls),
  - **release quality** (schema validation pass/fail summaries),
  - **maintenance prioritization** via *aggregate*, *non-identifying* usage signals.

### Scope
| In Scope | Out of Scope |
|---|---|
| Schema-governed events/metrics (performance, quality, governance) | Any collection of personal data (PII), user identifiers, or behavioral profiling |
| Minimal Focus Mode usage logging (story_id + timestamp) | Cross-site tracking, device fingerprinting, ad tech |
| Release-level telemetry snapshots (non-sensitive) | Operational secrets (tokens, internal URLs), raw access logs with IPs |
| Linking telemetry to STAC/DCAT/PROV IDs | Duplicating full catalogs or PROV bundles inside telemetry payloads |

### Audience
- Primary: Maintainers, pipeline/CI owners, governance reviewers
- Secondary: Domain module authors, story authors, API/UI developers

### Definitions (link to glossary)
- Link: `docs/glossary.md` (add/confirm telemetry terms there as needed)
- Terms used in this doc:
  - **Telemetry event**: a schema-validated JSON record describing a system action/signal.
  - **Telemetry snapshot**: an aggregated, versioned bundle of selected events/metrics packaged with a release.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Telemetry docs | `docs/telemetry/` | Maintainers | Human-readable contracts + signal catalog |
| Telemetry schemas | `schemas/telemetry/` | Maintainers | JSON schemas for events/metrics (semver) |
| Run logs / run manifests | `mcp/runs/` | Maintainers | Per-run artifacts; may include telemetry refs |
| Release telemetry snapshots | `releases/<version>/telemetry/` | Maintainers | Only non-sensitive, schema-validated snapshots |
| Governance policies | `docs/governance/**` | Governance | Sensitivity, CARE, review gates |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Telemetry boundaries explicitly forbid PII and user tracking
- [ ] Minimum event envelope documented with schema pinning + idempotency guidance
- [ ] Telemetry ↔ STAC/DCAT/PROV linkage expectations documented
- [ ] Validation steps listed and repeatable (schema validation + privacy scans)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/telemetry/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Telemetry docs | `docs/telemetry/` | Telemetry conventions, signal catalog, privacy notes |
| Telemetry schemas | `schemas/telemetry/` | Event/metric schemas (JSON Schema, semver) |
| Pipelines | `src/pipelines/` | ETL + catalog generation; emits run telemetry |
| Graph | `src/graph/` | Graph build/ingest; emits ingest telemetry |
| API boundary | `src/server/` (or repo-defined) | APIs + access controls; can emit aggregate request metrics |
| UI | `web/` | Focus Mode + map UI; can emit minimal usage events |
| MCP runs | `mcp/runs/` | Run manifests; telemetry refs for reproducibility |
| Releases | `releases/` | Versioned bundles incl. optional telemetry snapshot |

### Expected file tree for this sub-area
> This is the **recommended** structure. Some directories/files may not exist yet (**not confirmed in repo**).

~~~text
📁 docs/
└── 📁 telemetry/
    ├── 📄 README.md
    ├── 📄 SIGNAL_CATALOG.md                 # recommended (not confirmed in repo)
    ├── 📄 PRIVACY_AND_SAFETY.md             # recommended (not confirmed in repo)
    └── 📁 examples/                         # recommended (not confirmed in repo)
        ├── 📄 focus_mode_entry.v1.json
        └── 📄 governance_redaction_applied.v1.json

📁 schemas/
└── 📁 telemetry/
    ├── 📄 event_envelope.schema.json        # recommended canonical envelope (not confirmed in repo)
    ├── 📄 focus_mode_entry.v1.schema.json   # minimal Focus Mode entry event (not confirmed in repo)
    ├── 📄 governance_signals.v1.schema.json # classification/redaction/publish signals (not confirmed in repo)
    ├── 📄 energy-v2.json                    # optional sustainability telemetry (not confirmed in repo)
    └── 📄 carbon-v2.json                    # optional sustainability telemetry (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM is contract-first and evidence-first: catalogs (STAC/DCAT) and lineage (PROV) are required for trustworthy outputs. Telemetry is an optional layer that helps answer operational/governance questions like:
- Are pipelines succeeding and how long do they take?
- Are governance controls (classification/redaction) being applied and enforced?
- How often are stories/layers used (at an aggregate level) so we can prioritize maintenance?

### Assumptions
- Telemetry is **schema-governed**: every recorded event conforms to a versioned schema.
- Telemetry is **privacy-preserving by design**: no personal data; only aggregate or technical metrics.
- Telemetry is **secondary to canonical evidence**:
  - STAC/DCAT/PROV remain the system of record for data + metadata.
  - Telemetry provides operational and compliance signals.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (**no direct graph dependency**).
- Telemetry must not introduce a side-channel that leaks sensitive locations or restricted knowledge.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical telemetry sink (file snapshots only vs. external observability backend)? | Maintainers | TBD |
| What is the retention policy for raw events vs. aggregated snapshots? | Governance + Maintainers | TBD |
| Should release telemetry snapshots be signed (and with which tooling)? | Governance + Security | TBD |
| Which events are required vs. optional for a “domain pack” to be considered complete? | Maintainers | TBD |

### Future extensions
- Add a formal, machine-readable signal registry (YAML/JSON) used by CI to enforce allowlists (not confirmed in repo).
- Add energy/carbon accounting signals during ETL/model runs (optional; schema-governed).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph KFM_Pipeline["KFM Canonical Pipeline"]
    A[ETL] --> B[STAC/DCAT/PROV Catalogs]
    B --> C[Neo4j Graph]
    C --> D[APIs]
    D --> E[React/Map UI]
    E --> F[Story Nodes]
    F --> G[Focus Mode]
  end

  subgraph Telemetry["Telemetry (optional, schema-governed)"]
    T1[Events/Metrics] --> T2[Validation (CI)]
    T2 --> T3[Run logs (mcp/runs)]
    T2 --> T4[Release snapshot (releases/<version>/telemetry)]
  end

  A -. emits .-> T1
  B -. emits .-> T1
  C -. emits .-> T1
  D -. emits .-> T1
  E -. emits .-> T1
  F -. emits .-> T1
  G -. emits .-> T1
~~~

### Optional: sequence diagram (Focus Mode entry)
~~~mermaid
sequenceDiagram
  participant UI as UI (Focus Mode)
  participant API as API
  participant Tele as Telemetry Sink

  UI->>API: GET /focus/<story_id> (or equivalent)
  API-->>UI: story content + provenance refs
  UI->>Tele: emit focus_mode_entry (story_id + occurred_at)
  Note over UI,Tele: No user identifiers; schema-validated event only
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus Mode entry signal | JSON event | `web/` client + API context | JSON Schema + privacy rules |
| Pipeline run timing | JSON event/metric | `src/pipelines/` | Schema validation + determinism checks |
| Governance actions | JSON event | pipeline/CI/governance tooling | Schema validation + review gates |
| Energy/carbon signals (optional) | JSON event/metric | pipeline/model runs | Schema validation (energy/carbon schemas) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw/per-run telemetry refs | JSON/MD | `mcp/runs/<run_id>/...` | Schema pinned per event |
| Aggregated release snapshot | JSON/CSV | `releases/<version>/telemetry/` | Snapshot schema + checksums |
| Telemetry signal catalog | Markdown | `docs/telemetry/SIGNAL_CATALOG.md` | Markdown protocol checks |
| Event schemas | JSON Schema | `schemas/telemetry/*.json` | Semver + changelog |

### Sensitivity & redaction
Telemetry payloads **must not** include:
- personal identifiers (names, emails, IPs, user ids),
- exact sensitive coordinates or reconstructable location traces,
- secrets (tokens, keys) or internal-only endpoints.

When telemetry references a sensitive artifact, it should reference **opaque IDs** (e.g., dataset_id, stac_item_id, prov_activity_id) rather than embedding raw content.

### Quality signals
Telemetry is intended to record (examples; extend via schema):
- pipeline performance: run duration, counts, validation results,
- governance controls: classification assigned, redaction applied, promotion blocked,
- catalog health: stac/dcat/prov validation pass/fail, publish counts,
- UI compliance signals: redaction notices shown, provenance links present.

### Minimal event envelope (recommended)
Telemetry events should follow an envelope pattern that supports idempotency, schema pinning, and governance labels.

~~~json
{
  "id": "evt_01JABCDE9YZ7KFM12345",
  "idempotency_key": "sha256:5fd8... (stable hash of deterministic tuple)",
  "type": "focus_mode_entry",
  "source": "web/focus-mode",
  "generation": "release/v13.0.0@<commit_sha>",
  "version": "1.0.0",
  "occurred_at": "2025-12-27T00:00:00Z",
  "schema": {
    "ref": "schemas/telemetry/focus_mode_entry.v1.schema.json",
    "sha256": "<schema-hash>"
  },
  "provenance": {
    "run_id": "mcp_run_<id>",
    "prov_activity_id": "prov:activity:<id>",
    "stac_item_id": "stac:item:<id>"
  },
  "labels": {
    "sensitivity": "low",
    "classification": "open",
    "jurisdiction": "US-KS"
  },
  "payload": {
    "story_id": "kfm-story:<id>"
  },
  "signatures": [
    {
      "alg": "ed25519",
      "key_id": "kfm:signing-key:<id>",
      "sig": "<base64>"
    }
  ]
}
~~~

> Notes:
> - Signing is optional unless governance/security requires it.
> - `idempotency_key` should be stable so retries are safe (put-if-absent dedup).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Telemetry should reference STAC identifiers rather than duplicating STAC JSON.
- Examples of references:
  - `stac_collection_id`
  - `stac_item_id`
  - `asset_key` / `asset_href_hash`

### DCAT
- Telemetry should reference DCAT dataset identifiers when reporting publish/validation stats:
  - `dcat_dataset_id`
  - `distribution_id` (if used)
- License/sensitivity signals should be aligned with DCAT metadata and governance rules.

### PROV-O
- Telemetry should attach lineage pointers, not full PROV payloads:
  - `prov_activity_id` for runs/transforms,
  - `prov_entity_id` for produced artifacts,
  - `prov_agent_id` for tools/owners (role-based, not personal where possible).

### Versioning
- Telemetry schemas use semver. Any breaking change requires:
  - new schema file (new major),
  - documentation updates in `docs/telemetry/`,
  - CI allowlist updates (if present).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Producers | Emit telemetry events/metrics | JSON events (schema-pinned) |
| Schema registry | Define event contracts | `schemas/telemetry/` |
| Validation | Enforce schema + safety | CI checks + scanners |
| Storage | Store raw events/snapshots | `mcp/runs/` + `releases/<version>/telemetry/` |
| Consumers | Dashboards/analysis (optional) | Aggregated, non-sensitive views |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Telemetry event envelope | `schemas/telemetry/event_envelope.schema.json` | Semver + changelog |
| Telemetry signal schemas | `schemas/telemetry/*.schema.json` | Semver; new signal = minor unless breaking |
| Release telemetry snapshot | `releases/<version>/telemetry/` | Snapshot schema pinned per release |
| Governance labels | `docs/governance/**` | Human-reviewed; changes require governance review |

### Implementation pattern (recommended; may be staged)
- Producers write to an **outbox** (transactional) and dispatch asynchronously.
- Consumers use a **dedup store** keyed by `idempotency_key` (put-if-absent).
- Observability emits aggregate metrics/spans (e.g., publish counts, retries, dedup hits, latency).

> The specific backend (files vs. OTel backend) is intentionally not fixed here; the contract is the schema-governed event envelope + validation gates.

### Extension points checklist (for future work)
- [ ] Add/confirm `schemas/telemetry/event_envelope.schema.json` and pin in docs
- [ ] Add minimal `focus_mode_entry` schema and example payload
- [ ] Add governance signal schemas (classification/redaction/publish)
- [ ] Add CI job: telemetry schema validation + PII/secret scans
- [ ] Add release packaging step: `releases/<version>/telemetry/` snapshot
- [ ] Add energy/carbon telemetry schemas and emitters (optional)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Minimum required telemetry (if enabled):
- `focus_mode_entry` event when a story is opened (**story_id + timestamp** only).

Recommended additional compliance signals (schema-governed):
- `focus_mode_redaction_notice_shown` when a redaction/generalization notice is displayed,
- `provenance_link_missing` when a required citation/provenance ref is absent (CI and/or runtime).

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Telemetry must never become a substitute for provenance; it can only point to provenance.

### Optional structured controls (example shape)
~~~yaml
focus_layers:
  - "telemetry:enabled"         # example; not confirmed in repo
focus_time: "2025-12-27"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] Telemetry schema validation (JSON Schema) for any emitted event samples
- [ ] Privacy scans (no PII; no sensitive coordinate leakage)
- [ ] Secret scanning (no keys/tokens in telemetry payloads or docs)
- [ ] Release packaging checks (if telemetry snapshot is produced)
- [ ] Governance checks (classification propagation and redaction rules, as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands.
# These commands are NOT confirmed in repo; they document intent.

# 1) Validate telemetry schemas
# <schema-validate> schemas/telemetry/

# 2) Validate sample telemetry payloads (if stored in repo)
# <schema-validate> docs/telemetry/examples/*.json

# 3) Run privacy scans (PII + sensitive locations)
# <scan-pii> docs/telemetry/ docs/telemetry/examples/
# <scan-sensitive-locations> docs/telemetry/examples/

# 4) Package telemetry snapshot for a release (tag pipeline)
# <release-build> --include-telemetry
~~~

### Telemetry signals (recommended examples)
| Signal | Source | Where recorded |
|---|---|---|
| `focus_mode_entry` (story_id, occurred_at) | UI | `docs/telemetry/` + `schemas/telemetry/` |
| `etl.<domain>.run` (duration, status) | ETL | `mcp/runs/` + optional release snapshot |
| `catalog_validation_result` (PASS/WARN/FAIL) | CI | CI logs + optional snapshot |
| `classification_assigned` (dataset_id, sensitivity, classification) | Governance gate | telemetry events (schema-governed) |
| `redaction_applied` (method, fields_removed, geometry_generalization) | ETL/curation | telemetry events (schema-governed) |
| `promotion_blocked` (reason, scan_results_ref) | CI/governance | telemetry events (schema-governed) |
| `catalog_published` (public|internal, counts, validation_status) | Release/publish | telemetry snapshot |
| `focus_mode_redaction_notice_shown` (layer_id, redaction_method) | UI | telemetry events (schema-governed) |

## ⚖ FAIR+CARE & Governance

### Review gates
Telemetry changes require review when they:
- add a new signal (new schema) or change an existing schema,
- change what telemetry is collected (especially anything that could increase sensitivity),
- introduce new external sinks or dashboards (risk of exposure),
- alter retention or aggregation rules.

### CARE / sovereignty considerations
Telemetry must not be used to infer or expose:
- protected cultural sites,
- community-sensitive locations,
- restricted knowledge flows.

If a telemetry event references a sensitive artifact, the event must:
- preserve the artifact’s classification labels,
- avoid embedding sensitive content (use ID references),
- respect “no output less restricted than any input” lineage logic.

### AI usage constraints
- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited:
  - generating new policy from telemetry,
  - inferring sensitive locations or identities from telemetry,
  - identifying individual users via telemetry event correlation.
- Any AI-driven aggregation/classification suggestions must be reviewed by humans before adoption.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial telemetry README (contracts, boundaries, validation) | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`