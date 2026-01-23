---
title: "DevOps Provenance Schemas 🛠️ (dev_prov/devops)"
path: "mcp/dev_prov/schemas/devops/README.md"
version: "v0.1.0"
last_updated: "2026-01-22"
status: "draft"
doc_kind: "Schema README"
schema_pack: "devops"
provenance_profile: "KFM PROV Mapping (W3C PROV-aligned)"
license: "CC-BY-4.0"
---

# 🛠️ DevOps Provenance Schemas (mcp/dev_prov/schemas/devops)

<kbd>JSON Schema</kbd> <kbd>PROV-O mapping</kbd> <kbd>OPA / Conftest</kbd> <kbd>OCI Artifacts</kbd> <kbd>Evidence-first</kbd> <kbd>FAIR+CARE aware</kbd>

A **schema pack** for capturing **DevOps + DataOps + MLOps provenance** across the Kansas Frontier Matrix (KFM) platform — so builds, deployments, pipeline runs, policy decisions, rollbacks, and health checks become **auditable graph facts** instead of tribal knowledge. 🧭

> 🔎 KFM is designed to treat *data like code*: versioned, reviewable, reproducible, and governed — with provenance and policy embedded end-to-end.  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:1‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧭 Quick Navigation

- [What this pack is for](#-what-this-pack-is-for)
- [Where it plugs into KFM](#-where-it-plugs-into-kfm)
- [📁 Directory layout](#-directory-layout)
- [🧩 Schema inventory](#-schema-inventory)
- [📦 Event taxonomy](#-event-taxonomy)
- [✉️ Base event envelope](#️-base-event-envelope)
- [🧬 PROV mapping](#-prov-mapping)
- [🛡️ Policy-as-code events](#️-policy-as-code-events)
- [📦 OCI artifact & supply-chain events](#-oci-artifact--supply-chain-events)
- [🚀 Deployment & rollback events](#-deployment--rollback-events)
- [📈 Ops / health / incident events](#-ops--health--incident-events)
- [🧭 FAIR+CARE, sensitivity, and “don’t log harm”](#-faircare-sensitivity-and-dont-log-harm)
- [✅ Validation & tests](#-validation--tests)
- [🔁 Versioning rules](#-versioning-rules)
- [✅ Definition of Done](#-definition-of-done)
- [📚 Sources](#-sources)

---

## 🎯 What this pack is for

This schema pack standardizes **DevOps telemetry as structured events** so that:

- ✅ CI/CD runs are **traceable** to commits/PRs and reproducible contexts  
- ✅ Policy decisions (OPA / Conftest) are captured as **machine-checkable governance evidence**  
- ✅ Artifacts (tiles, GeoParquet, COGs, API images, offline packs) are **content-addressed and signed**  
- ✅ Deployments are **audited**, with rollbacks recorded as first-class events  
- ✅ Ops routines (graph health checks, backups, migrations) are **visible + reviewable**  
- ✅ KFM’s UI can surface provenance & governance “tooltips” and admin dashboards safely  
  (e.g., sensitivity warnings + generalized locations)  [oai_citation:2‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 🧩 Where it plugs into KFM

KFM is a modular geospatial + knowledge-graph platform (Python/FastAPI + PostGIS + Neo4j + React/TypeScript + MapLibre + Cesium). That stack implies multiple operational surfaces that need consistent provenance capture.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Typical event emitters include:

- 🧪 **GitHub Actions** CI workflows (tests, lint, type-check, CodeQL, catalog QA)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 🧠 **AI Watcher–Planner–Executor agents** that open PRs, propose changes, and respect policy gates  [oai_citation:6‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🧱 **Data intake & pipeline runners** (ingest → validate → transform → publish) with NDJSON run logs  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 📦 **Artifact publishers** pushing PMTiles/GeoParquet/COGs or container images into an OCI registry via ORAS + signing via Cosign  [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- 🚀 **CD systems** (Docker → Registry → Kubernetes/Helm/Terraform) with rollback support  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 🗺️ **Map delivery + UI releases** (timeline slider MVP, 4D mapping, offline packs, high-performance tiling)  [oai_citation:10‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 📌 Design principles

These schemas follow KFM’s “provenance-first” philosophy:

1. **Append-only events** 📜  
   Don’t mutate history. Emit a new event when state changes (deploy failed → emit failure event).

2. **Deterministic identifiers** 🧾  
   Prefer stable IDs derived from canonical data (e.g., RFC 8785 canonical JSON + sha256) when possible.  
   This matches KFM’s emphasis on reproducibility and traceability across runs.  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

3. **Minimal-but-sufficient payloads** 🎯  
   Events should contain enough to reproduce & audit, not everything (no giant logs inside events).

4. **Zero secrets / no sensitive coordinates in logs** 🔒  
   Capture references (hashes, artifact refs) rather than raw sensitive content.  
   KFM explicitly treats sensitive data carefully (generalization, access control, classification).  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

5. **Policy outcomes are first-class** 🧠⚖️  
   If a pipeline is blocked, the *reason* must be structured (rule id, pack version, inputs).

---

## 📁 Directory layout

> This README documents the schema **contract** for DevOps provenance events.

```text
📁 mcp/
  📁 dev_prov/
    📁 schemas/
      📁 devops/
        📄 README.md  👈 you are here
        📄 devops.event.schema.json
        📄 devops.pipeline_run.schema.json
        📄 devops.policy_evaluation.schema.json
        📄 devops.artifact.schema.json
        📄 devops.deployment.schema.json
        📄 devops.incident.schema.json
        📄 devops.health_check.schema.json
        📄 devops.ml_event.schema.json   (optional / when MLOps is enabled)
        📁 examples/
          📄 pipeline_run.completed.ndjson
          📄 policy.evaluated.ndjson
          📄 artifact.published.ndjson
          📄 deploy.completed.ndjson
```

> 🧠 Note: File names are **recommended defaults**. If your repo already uses a different naming convention, mirror it — but keep the *event contract* consistent.

---

## 🧩 Schema inventory

| Schema | Purpose | Typical emitter |
|---|---|---|
| `devops.event` | Base envelope shared by all DevOps events | all emitters |
| `devops.pipeline_run` | Pipeline run lifecycle + step summaries | CI, pipeline runners |
| `devops.policy_evaluation` | OPA/Conftest decisions + violations | policy gate job |
| `devops.artifact` | Built/published/signed/scanned artifact events | artifact publisher |
| `devops.deployment` | Deploy/rollback events, env targets | CD / GitOps |
| `devops.health_check` | Scheduled checks (graph health, backups, integrity) | cron / ops runner |
| `devops.incident` | Incident + postmortem provenance | ops / maintainers |
| `devops.ml_event` | Model training/eval/drift/promote | MLOps runner |

---

## 📦 Event taxonomy

Event types are strings with a stable namespace:

```text
devops.<domain>.<action>
```

Examples:

- `devops.pipeline_run.started`
- `devops.pipeline_run.completed`
- `devops.policy.evaluated`
- `devops.policy.denied`
- `devops.artifact.published`
- `devops.artifact.signed`
- `devops.deploy.completed`
- `devops.rollback.executed`
- `devops.health_check.completed`
- `devops.incident.created`
- `devops.ml.model_trained` (optional)

> ✅ Tip: Keep a **closed set** of event types in schema enums to prevent drift.

---

## ✉️ Base event envelope

All DevOps events MUST validate against the base envelope.  
Event-specific payload goes into `data`.

### Required fields (recommended)

- `schema_id` (string): e.g., `kfm.devops.event@v0.1.0`
- `event_id` (string): ULID/UUID
- `event_type` (string): from taxonomy
- `ts` (string): ISO 8601 timestamp
- `actor` (object): human/agent/service identity
- `source` (object): repo/ref/commit + tooling source
- `correlation` (object): run_id + trace ids that tie steps together
- `env` (object): `ci` / `staging` / `prod` + region/cluster
- `classification` (object): sensitivity + CARE label + license expectations
- `data` (object): event-specific

### Canonical example (JSON)

```json
{
  "schema_id": "kfm.devops.event@v0.1.0",
  "event_id": "01J2K0GJQ0QG8Q7S1XQ2B4KZ2A",
  "event_type": "devops.pipeline_run.completed",
  "ts": "2026-01-22T18:04:12Z",

  "actor": {
    "actor_type": "service",
    "actor_id": "github_actions",
    "display_name": "GitHub Actions"
  },

  "source": {
    "scm": "git",
    "repo": "Kansas-Frontier-Matrix",
    "ref": "main",
    "commit_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "pr_number": 123
  },

  "correlation": {
    "run_id": "kfm-run-20260122-1800Z-00042",
    "parent_run_id": null,
    "trace_id": "trace-2f8e3c",
    "span_id": "span-9b1a"
  },

  "env": {
    "stage": "ci",
    "region": "local",
    "runtime": "linux-x64"
  },

  "integrity": {
    "canonicalization": "rfc8785",
    "payload_hash": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "inputs_hash": "sha256:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
    "outputs_hash": "sha256:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
  },

  "refs": {
    "artifact_ref": null,
    "prov_ref": null,
    "sbom_ref": null,
    "attestation_ref": null
  },

  "classification": {
    "sensitivity": "public",
    "care_label": "Public",
    "license_hint": "CC-BY-4.0",
    "contains_pii": false
  },

  "data": {
    "status": "success",
    "duration_ms": 94123,
    "summary": {
      "tests_passed": true,
      "lint_passed": true,
      "policy_passed": true
    }
  }
}
```

---

## 🧾 NDJSON run logging (preferred storage format)

KFM pipelines commonly benefit from line-delimited JSON telemetry (`.ndjson`) that is **easy to stream, diff, and ingest** into graph systems. The intake design explicitly describes NDJSON run logs with hashes and artifact/prov references.  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

Example (each line = one event):

```ndjson
{"ts":"2026-01-22T18:00:01Z","event_type":"devops.pipeline_run.started","correlation":{"run_id":"kfm-run-20260122-1800Z-00042"},"data":{"pipeline":"catalog_qa","stage":"start"}}
{"ts":"2026-01-22T18:03:10Z","event_type":"devops.policy.evaluated","correlation":{"run_id":"kfm-run-20260122-1800Z-00042"},"data":{"decision":"allow","violations":[]}}
{"ts":"2026-01-22T18:04:12Z","event_type":"devops.pipeline_run.completed","correlation":{"run_id":"kfm-run-20260122-1800Z-00042"},"data":{"status":"success","duration_ms":94123}}
```

---

## 🧬 PROV mapping

KFM maps development and pipeline actions into a PROV-shaped graph (Activities, Entities, Agents) so audits can answer:

- “Which pipeline run generated this artifact?”
- “Which commits (Entities) were used by this run (Activity)?”
- “Which bot/human (Agent) approved and merged it?”

This aligns with KFM’s explicit GitHub PR → PROV Activity mapping concept and Neo4j ingestion plan.  [oai_citation:15‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### Mapping table

| DevOps concept | PROV concept | Where it shows up |
|---|---|---|
| Pipeline run | `prov:Activity` | `devops.pipeline_run.*` |
| Build artifact / PMTiles / GeoParquet / image | `prov:Entity` | `devops.artifact.*` |
| Commit / PR merge | `prov:Entity` | `devops.git.*` (optional) |
| Maintainer / contributor / bot / CI runner | `prov:Agent` | `actor.*` |
| “used” relationship | `prov:used` | `integrity.inputs_hash`, `refs.*` |
| “generated” relationship | `prov:wasGeneratedBy` | `artifact_ref` + `run_id` |

---

## 🛡️ Policy-as-code events

KFM’s governance approach includes policy-as-code (OPA) gates, fail-closed behavior, and explicit denial messages for violations — including provenance integrity (“processed data changed without matching PROV update”) and sensitive data handling.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### `devops.policy.evaluated` (recommended fields)

- `policy_pack_id` (string) — e.g., `kfm-policy-pack`
- `policy_pack_version` (string)
- `engine` (enum) — `opa`
- `decision` (enum) — `allow | deny | warn`
- `violations[]` — structured objects:
  - `rule_id` (string) e.g., `KFM-PROV-001`
  - `severity` (enum) `low|medium|high|critical`
  - `message` (string)
  - `evidence_refs[]` (optional) — pointers/hashes, not raw secrets

Example:

```json
{
  "event_type": "devops.policy.evaluated",
  "data": {
    "engine": "opa",
    "policy_pack_id": "kfm-policy-pack",
    "policy_pack_version": "v1.4.2",
    "decision": "deny",
    "violations": [
      {
        "rule_id": "KFM-PROV-001",
        "severity": "high",
        "message": "Processed data changed without matching PROV update.",
        "evidence_refs": ["sha256:ee..."]
      }
    ]
  }
}
```

> 💡 Keep violation messages short, stable, and searchable. Put verbose logs in build artifacts, not the event.

---

## 📦 OCI artifact & supply-chain events

KFM explicitly explores OCI registries (via ORAS) for non-container artifacts like PMTiles/GeoParquet/COGs, with Cosign signing and attached provenance/SBOM attestations — enabling strong integrity, reproducibility, and rollback by digest.  [oai_citation:18‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Artifact references (`artifact_ref`)

Use an OCI digest reference (kept as a string). Store it in events **only as a reference**:

```text
oci:<registry>/<namespace>/<name>@sha256:<digest>
```

(Keep this value in code/log blocks, not prose.)

### `devops.artifact.published` (recommended fields)

- `artifact_kind` — `pmtiles | geoparquet | cog | docker_image | offline_pack | prov_jsonld | sbom`
- `media_type` — e.g., `application/vnd.pmtiles`
- `digest` — `sha256:<...>`
- `tags[]` — e.g., `["20260122", "v0.13.0"]`
- `signature_ref` — Cosign signature ref
- `sbom_ref` — SBOM artifact ref
- `attestation_ref` — in-toto / provenance attestation ref
- `provenance_ref` — PROV JSON-LD ref (if stored separately)

### Offline packs 🧳 (field alignment)

KFM’s “offline pack” idea (downloadable bundles for regions, exhibits, low-connectivity use) should be represented as an artifact kind (`offline_pack`) with explicit contents manifest + checksums.  [oai_citation:20‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🚀 Deployment & rollback events

KFM’s architecture supports containerized deployment and rollback, and KFM’s intake/ops design explicitly discusses rollback patterns (Git revert, graph re-import, kill-switch for automation).  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### `devops.deploy.completed` (recommended fields)

- `deploy_target` (object):
  - `platform`: `kubernetes | vm | static_site`
  - `cluster` / `namespace` / `service`
- `artifact_ref` (string): what was deployed
- `config_ref` (string): config hash or IaC commit hash
- `status` (enum): `success|failed`
- `rollback_plan_ref` (optional): pointer to rollback instructions

### `devops.rollback.executed` (recommended fields)

- `rollback_reason` (string)
- `from_artifact_ref` / `to_artifact_ref`
- `method` (enum): `git_revert | digest_pin | helm_rollback | db_restore`
- `operator` (actor): human or automation

---

## 📈 Ops / health / incident events

Operational routines should be represented as structured events so that reliability work becomes queryable:

- `devops.health_check.completed`  
- `devops.backup.completed` / `devops.restore.completed`  
- `devops.migration.applied`  
- `devops.incident.created` / `devops.incident.resolved`  

> 🧩 This directly supports “system health and integrity for maintainers and auditors” as described in KFM’s architecture.  [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧭 FAIR+CARE, sensitivity, and “don’t log harm”

KFM treats data sensitivity as a first-class concern — including location generalization, access control, tagging, and CARE-aligned stewardship for Indigenous/community-controlled data.  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:25‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

### Minimum required classification fields

- `sensitivity`: `public | internal | restricted`
- `care_label`: free text (e.g., `Restricted · Tribal Sensitive`)
- `contains_pii`: boolean
- `notes` (optional): short explanation

### Logging rules (practical)

✅ log:
- hashes
- artifact digests
- policy rule ids
- run ids and statuses

❌ don’t log:
- secrets
- raw access tokens
- raw PII
- precise coordinates of sensitive sites

> 🗺️ The UI itself may display generalized shapes (e.g., hex areas instead of exact points) when sensitivity requires it — DevOps logs must respect the same principle.  [oai_citation:26‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## ✅ Validation & tests

Recommended validation strategy:

- **Schema validation** in CI (fail-closed)  
- **Example fixtures** in `examples/` validated in CI  
- **Policy checks** (OPA/Conftest) that verify:
  - event type enums are not drifting
  - required fields exist
  - hashes are present where mandated
  - prohibited fields (secrets) are absent

KFM’s broader CI/CD approach includes GitHub Actions pipelines that block merges on failure, with tests, linting, type checking, security scans, and “catalog QA” style checks.  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🔁 Versioning rules

- **Patch** (`v0.1.1`): docs/examples, clarification, no schema changes
- **Minor** (`v0.2.0`): backward-compatible additions (new optional fields, new event types if not enum-locked)
- **Major** (`v1.0.0`): breaking changes (renames, required fields changed, type changes)

✅ Always:
- keep `schema_id` explicit (includes version)
- keep old schema files for historical validation
- provide a migration note when bumping major

---

## ✅ Definition of Done

Before merging a schema change:

- [ ] JSON Schema validates (locally + CI)
- [ ] `examples/*.ndjson` fixtures validate
- [ ] Event taxonomy updated (no orphan event types)
- [ ] PROV mapping updated (if new entity/activity/agent concepts introduced)
- [ ] OPA policy pack updated if governance requirements changed
- [ ] No sensitive data leaked (spot-check payloads)
- [ ] Version bumped appropriately
- [ ] README updated (this file)

---

## 📚 Sources

These project files inform the DevOps schema requirements and conventions:

- KFM architecture, tech stack, CI/CD expectations  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- KFM technical documentation (governance, sensitivity, SOP direction)  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM AI system overview (agent workflows, PR → PROV mapping, policy awareness)  [oai_citation:30‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- KFM UI system overview (provenance surfacing + sensitivity UX)  [oai_citation:31‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- KFM data intake guide (provenance-first intake, NDJSON telemetry, policy gates, rollback patterns)  [oai_citation:32‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Innovative concepts (CARE, cultural protocols, sensitivity-aware handling)  [oai_citation:33‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- Additional project ideas (OCI + ORAS + Cosign + provenance attachments)  [oai_citation:34‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Latest ideas & future proposals (offline packs, PMTiles + GeoParquet dual packaging, timeline infra)  [oai_citation:35‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- AI Concepts & more (reference library for AI lifecycle context)  [oai_citation:36‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- Maps / Virtual Worlds / WebGL portfolio (reference library for geospatial + WebGL ops constraints)  [oai_citation:37‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- Programming languages & resources portfolio (multi-language ecosystem reference)  [oai_citation:38‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- Data management / Bayesian / CI-CD portfolio (data architecture & reproducibility reference)  [oai_citation:39‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
