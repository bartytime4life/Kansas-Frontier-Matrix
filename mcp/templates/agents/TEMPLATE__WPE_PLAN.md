---
template_id: TEMPLATE__WPE_PLAN
template_name: "Watcher–Planner–Executor (WPE) Plan"
template_version: "1.0.0"
path: "mcp/templates/agents/TEMPLATE__WPE_PLAN.md"
project: "Kansas Frontier Matrix (KFM) / Kansas-Matrix-System"
status: "template"
created_utc: "{{YYYY-MM-DDTHH:MM:SSZ}}"
owners:
  - "{{OWNER_NAME_OR_HANDLE}}"
tags:
  - mcp
  - agents
  - wpe
  - governance
  - provenance
  - policy-pack
---

# 🔭🧠🛠️ TEMPLATE__WPE_PLAN
A **safe, auditable, policy-gated** plan format for the **Watcher → Planner → Executor** (WPE) automation loop.  
Default behavior: **observe → propose → PR (no auto-merge)**, with **CI + policy gates** enforcing quality, provenance, and governance.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:1‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

| 🧩 Pattern | 🔒 Governance | 🧾 Provenance | 🔁 Determinism |
|---|---|---|---|
| Watcher → Planner → Executor | Policy Pack / OPA / “fail-closed” | STAC/DCAT/PROV + signed event record | Structured plan + idempotency keys |

> [!IMPORTANT]
> **Non‑negotiables (defaults):**
> - 🔭 **Watcher observes only** and emits an **immutable, signed event record** (no side effects).  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
> - 🧠 **Planner proposes** (plan/patch), **does not execute** changes directly.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
> - 🛠️ **Executor materializes the plan as a PR**, subject to normal branch protections, CI, and policy gates.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
> - 🧯 **Kill-switch exists** to disable all agent actions globally.  [oai_citation:6‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
> - 🧾 **Evidence-first:** no “mystery layers” / unsourced additions; narratives require citations + manifests.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:9‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🗺️ WPE lifecycle overview

```mermaid
flowchart LR
  W[Watcher 🔭\n(Observe & Record)] --> ER[Immutable Event Record 🧾\n(signed, timestamped)]
  ER --> P[Planner 🧠\n(Formulate deterministic plan)]
  P --> PL[Plan Artifact 📦\n(plan.json + risk + tests)]
  PL --> E[Executor 🛠️\n(Run deterministic pipeline + open PR)]
  E --> PR[Pull Request 🔀\n(context + provenance + artifacts)]
  PR --> CI[CI + Policy Pack ✅\n(fail closed)]
  CI --> HR[Human Review 👀]
  HR --> M[Merge ✅]
  M --> PUB[Publish/Promote 🌐\nCatalog + Graph + UI]
```

Key idea: **automation with accountability** — every action ties back to a trigger event and is reviewable.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 1) 🎯 Objective & scope

### Objective (fill)
- **Problem statement:** {{WHAT_WAS_DETECTED_OR_REQUESTED}}
- **Desired outcome / success:** {{MEASURABLE_RESULT}}
- **Non-goals:** {{WHAT_WE_ARE_NOT_DOING}}

### Impacted areas (check all that apply)
- [ ] 📥 Data intake (raw/work/processed)  
- [ ] 🧬 Provenance & catalogs (STAC/DCAT/PROV)  
- [ ] 🧠 Knowledge Graph (Neo4j / concept graph)  
- [ ] 🧱 PostGIS / tiles / summaries  
- [ ] 🌐 API layer  
- [ ] 🗺️ UI layer (Map / Timeline / Story / AR)  
- [ ] 🤖 Focus Mode / AI assistant behavior  
- [ ] 🧪 Simulation / modeling pipeline  
- [ ] 🧰 DevOps / dependencies / security  

> [!NOTE]
> KFM’s architecture is layered (data → ETL → graph/API → UI → AI), so record *which layers* are touched.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 2) 🚨 Trigger & context

### Trigger summary
- **Trigger type:** `{{repo_change|external_feed|schedule|telemetry_anomaly|policy_violation|user_request}}`
- **Watcher name:** `{{WATCHER_ID}}`
- **Severity:** `{{low|medium|high|critical}}`
- **First observed (UTC):** `{{YYYY-MM-DDTHH:MM:SSZ}}`
- **Idempotency key candidate:** `{{WPE_IDEMPOTENCY_KEY}}`  
  (Tip: derive from canonicalized event payload + stable IDs.)

### Primary affected entities
- Datasets: `{{dataset_ids}}`
- Domains: `{{domain_ids}}`
- Graph nodes/relations: `{{entity_ids}}`
- UI layers/story nodes: `{{layer_ids_or_story_ids}}`
- External sources: `{{source_urls_or_registry_refs}}`

### Governance classification (required)
- **Sensitivity:** `{{public|restricted|sensitive|sacred|private}}`
- **CARE/FAIR notes:** `{{care_notes}}`

> [!IMPORTANT]
> If the trigger touches **sensitive / sovereignty‑related** content, the plan must include redaction, coordinate obfuscation, or access controls before publish.  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:14‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 3) 🧾 Evidence & inputs

### Evidence pack (must list)
- [ ] Source datasets / URLs: `{{...}}`
- [ ] Checksums captured (SHA‑256 or multihash): `{{...}}`  [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Existing catalog entries (STAC/DCAT): `{{...}}`
- [ ] Existing PROV lineage references: `{{...}}`
- [ ] Relevant policy rules & expected gates: `{{...}}`

### “Evidence-first” narrative requirement (if text/story is impacted)
- [ ] Story node has citations block (3–7 refs) + **evidence manifest** file
- [ ] Evidence manifest includes checksums + precise pointers (line ranges / query params)
- [ ] Story node includes an embedded **PROV JSON‑LD snippet** linking story → sources → creation activity  [oai_citation:16‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 4) 🔭 Watcher specification

### Watcher mission
What does this watcher monitor, how often, and how does it decide “this is worth emitting an event”?

- **Watcher ID:** `{{WATCHER_ID}}`
- **Schedule:** `{{cron_or_event_driven}}`
- **Inputs observed:** `{{repo_paths|api_endpoints|feeds|registries|telemetry_files}}`
- **Detection rules:** `{{explicit_rules}}`

Examples of watcher triggers KFM expects (fill as applicable):
- Missing metadata fields (license, source, extent) on new dataset(s)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- CI regressions (coverage dropped below threshold)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Dependency/security updates (e.g., PostGIS patch available)  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Real‑time feeds updated (ETag/Last‑Modified changes, sequence drift)  [oai_citation:20‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### Watcher outputs (required)
- [ ] Immutable event record (signed + timestamped)
- [ ] Links to evidence pack (checksums, URLs, prior catalog refs)

#### Event record JSON template
```json
{
  "event_id": "{{EVENT_ID}}",
  "wpe_idempotency_key": "{{IDEMPOTENCY_KEY}}",
  "watcher": {
    "id": "{{WATCHER_ID}}",
    "version": "{{WATCHER_VERSION}}"
  },
  "observed_at_utc": "{{YYYY-MM-DDTHH:MM:SSZ}}",
  "trigger_type": "{{repo_change|external_feed|schedule|telemetry_anomaly|policy_violation|user_request}}",
  "severity": "{{low|medium|high|critical}}",
  "summary": "{{ONE_LINE_SUMMARY}}",
  "details": {
    "affected_dataset_ids": ["{{...}}"],
    "affected_paths": ["{{...}}"],
    "external_sources": ["{{...}}"],
    "evidence": [
      {
        "kind": "download",
        "uri": "{{SOURCE_URI}}",
        "sha256": "{{SHA256}}",
        "notes": "{{...}}"
      }
    ]
  },
  "signatures": {
    "method": "{{sigstore|gpg|internal}}",
    "signed_by": "{{WATCHER_IDENTITY}}",
    "signature_ref": "{{SIGNATURE_POINTER}}"
  }
}
```

> [!NOTE]
> Watcher events should be immutable, timestamped, and signed to support auditability.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 5) 🧠 Planner specification

### Planner mission
Given an event record, decide **what should be done**, under strict authority limits.

- **Planner ID:** `{{PLANNER_ID}}`
- **Inputs:** event record + current catalog/graph state + policy pack rules
- **Outputs:** deterministic plan (JSON) and/or a proposed patch *for review*  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### Authority boundaries (fill)
- **Allowed:** {{metadata_edits|catalog_updates|data_reingest|doc_updates|build_artifacts}}
- **Not allowed:** {{deletions_of_user_data|publishing_sensitive_locations|bypassing_ci|secrets}}

> [!IMPORTANT]
> Planner must never propose actions that violate policies or exceed authority; escalate to human review when needed.  [oai_citation:23‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### Risk classification (required)
- **Risk level:** `{{low|medium|high}}`
- **Reason:** `{{...}}`
- **Required approvals:** `{{none|1_maintainer|2_maintainers|domain_steward|security}}`

### Determinism rule (required)
Planner outputs a structured plan that is:
- **replayable** (same input → same plan)
- **idempotent** (safe to retry / detect duplicates)
- **machine-validated** (schema checked)

KFM supports “agent-assisted” workflows where AI can propose steps, but **deterministic code validates and executes** them.  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

#### Plan JSON template
```json
{
  "plan_id": "{{PLAN_ID}}",
  "event_id": "{{EVENT_ID}}",
  "wpe_idempotency_key": "{{IDEMPOTENCY_KEY}}",
  "planner": {
    "id": "{{PLANNER_ID}}",
    "version": "{{PLANNER_VERSION}}"
  },
  "created_at_utc": "{{YYYY-MM-DDTHH:MM:SSZ}}",
  "risk": {
    "level": "{{low|medium|high}}",
    "required_approvals": ["{{...}}"]
  },
  "policy_preflight": {
    "ruleset_version": "{{POLICY_PACK_VERSION}}",
    "expected_gates": ["{{KFM-CAT-001}}", "{{KFM-PROV-001}}", "{{KFM-CARE-001}}"],
    "waiver_needed": false,
    "waiver_ref": null
  },
  "actions": [
    {
      "type": "{{ingest_dataset|update_metadata|build_tiles|update_graph|publish_story_node|run_simulation|dependency_update}}",
      "targets": {
        "dataset_ids": ["{{...}}"],
        "paths": ["{{...}}"]
      },
      "inputs": [
        { "uri": "{{...}}", "sha256": "{{...}}" }
      ],
      "outputs_expected": [
        "data/processed/{{...}}",
        "data/catalog/stac/{{...}}",
        "data/catalog/dcat/{{...}}",
        "data/prov/{{...}}"
      ],
      "tests": [
        "{{unit_tests}}",
        "{{schema_validators}}",
        "{{policy_pack_conftest}}"
      ]
    }
  ],
  "rollback": {
    "strategy": "{{revert_pr|restore_previous_artifact|pin_previous_version}}",
    "notes": "{{...}}"
  }
}
```

---

### 🧪 Optional: scientific method protocol (for simulations / research work)
Use this when the plan includes simulation/modeling or investigative analytics.

<details>
<summary><strong>🧬 Expand: Scientific Method / MCP-aligned protocol fields</strong></summary>

- **Question / problem:** {{...}}
- **Background research:** {{what’s already known + citations}}
- **Hypothesis:** {{testable statement}}
- **Experiment / method:** {{tools, variables, setup}}
- **Data collection:** {{what will be logged, where, IDs}}
- **Analysis plan:** {{stats, viz, evaluation}}
- **Results reporting:** {{tables, artifacts, model cards}}
- **Conclusion & limitations:** {{...}}
- **Next steps:** {{...}}

This mirrors the “protocol-first” / reproducibility orientation for research workflows.  [oai_citation:25‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

</details>

---

## 6) 🛠️ Executor specification

### Executor mission
Carry out the plan **under oversight**, typically by:
- running deterministic pipeline steps
- committing generated outputs
- opening a PR with full context & provenance  
…and then **waiting for human review**.

- **Executor ID:** `{{EXECUTOR_ID}}`
- **Kill switch respected:** `{{true}}` (must check runtime flag)  [oai_citation:26‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

> [!IMPORTANT]
> Default: **Executor does not auto-merge**. The standard flow is PR → CI → human review.  [oai_citation:27‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:28‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Execution steps (fill)
1. [ ] Verify kill-switch is OFF and agent identity is authorized.
2. [ ] Fetch plan + validate JSON schema.
3. [ ] Create branch: `{{branch_name}}`
4. [ ] Run deterministic pipeline steps (no “creative” modifications).
5. [ ] Generate required catalogs & provenance (STAC/DCAT/PROV).
6. [ ] Generate **run manifest** and compute canonical digest.
7. [ ] Run test suite + policy pack (fail closed).
8. [ ] Open PR with:
   - event link
   - plan link
   - run manifest + artifacts
   - explicit risk & required approvals
9. [ ] Stop. Await human review.

### Run manifest requirement (audit trail)
Each run produces a run manifest JSON capturing who/what/when, sources, tool versions, and summary counts; canonicalize JSON (RFC 8785) and hash (SHA‑256) for stable identifiers / idempotency keys.  [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> [!NOTE]
> Run manifests can be stored under something like `data/audits/<run_id>/run_manifest.json`.  [oai_citation:30‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 7) 📦 Required outputs & repo touchpoints

### Required artifacts checklist
- [ ] 🔔 `Event Record` (immutable, signed)  
- [ ] 🧠 `Plan` (structured JSON + risk + tests)  
- [ ] 🧾 `Run Manifest` (canonical digest / idempotency)  
- [ ] 🗂️ `Catalog updates` (STAC/DCAT)  
- [ ] 🧬 `PROV` lineage record (entities, activity, agents)  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:32‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] 🧱 `Graph ingestion outputs` (CSV nodes/relationships if applicable)
- [ ] 🧪 `Test results` + policy pack reports
- [ ] 🧵 If narrative/UI: `Story node` + evidence manifest + PROV snippet  [oai_citation:33‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Suggested output tree (adapt to your repo conventions)
```text
📂 data/
  📂 audits/
    📂 {{run_id}}/
      🧾 run_manifest.json
      🧾 checksums.sha256
      🧾 policy_report.json
  📂 events/
    🔔 {{event_id}}.json
  📂 prov/
    🧬 {{prov_id}}.jsonld
  📂 raw/
    📂 {{domain}}/{{dataset}}/{{version}}/
  📂 work/
    🧪 sims/            # sandbox simulation outputs (NOT publishable)
  📂 processed/
    📦 {{domain}}/{{dataset}}/{{version}}/
  📂 catalog/
    📂 stac/
    📂 dcat/
📂 data/graph/csv/
  🧱 nodes_*.csv
  🔗 rels_*.csv
📂 ui/
  🗺️ layers/
  🧵 stories/
```

> [!IMPORTANT]
> Simulation/model outputs should live in a sandbox area first (e.g., `data/work/sims/`) and must be promoted via PR to `data/processed/` with full STAC/DCAT/PROV before being used by Graph/API/UI.  [oai_citation:34‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 8) ✅ Policy Pack & CI gates (fail closed)

KFM uses automated gates for:
- schema validation
- provenance completeness
- license / attribution presence
- sensitive-content checks
- citation/evidence requirements  
…blocking merges when they fail (“fail closed”).  [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### Policy categories (examples)
Use stable IDs and document waivers.

- `KFM-CAT-001` Catalog required (STAC/DCAT present)
- `KFM-PROV-001` PROV required (lineage + agent attribution)
- `KFM-LIC-001` License required
- `KFM-CARE-001` Sensitive / sovereignty handling required
- `KFM-EVID-001` Evidence-first narratives required

> [!NOTE]
> Policy packs can include: “Evidence for Narratives,” “Sovereignty / Classification,” “Mandatory CI Checks,” and a time-bound waiver mechanism for exceptions.  [oai_citation:37‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 9) 🧬 Provenance & catalog publishing

### Required metadata set
- **STAC** (spatial/temporal assets & collections)
- **DCAT** (dataset catalog listing)
- **PROV** (lineage: entities, activities, agents)  [oai_citation:38‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### “No mystery layers” rule
All published layers must be traceable with a data contract, provenance, and CI checks.  [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Optional: OCI artifact distribution (ORAS + cosign)
Use OCI registries to store large artifacts and attach signatures/provenance as referrers.  [oai_citation:40‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:41‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

<details>
<summary><strong>📦 Expand: OCI distribution fields (optional)</strong></summary>

- Registry ref: `{{registry}}/{{repo}}:{{tag}}`
- Media type: `application/vnd.kfm.layer.pmtiles` / `...geoparquet` / etc.
- `distribution.oci` file in catalog referencing OCI ref
- Cosign signatures + in-toto provenance attestation attached

This supports secure, reusable distribution with provenance attached.  [oai_citation:42‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

</details>

---

## 10) 🧠 Graph + 🧱 PostGIS integration notes

### Knowledge graph integration (when applicable)
- Add/update nodes & relationships during ingestion; align to known ontologies (e.g., CIDOC‑CRM, GeoSPARQL) where possible.  [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### PostGIS roles (when applicable)
- Use PostGIS for tile serving and aggregates (e.g., vector tiles), keeping UI fast.  [oai_citation:44‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Real-time streams (when applicable)
Real-time answers should still cite sources and log provenance for the specific reading used.  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 11) 🗺️ UI / Story / Focus Mode considerations

### UI transparency goals
UI should let users trace “the map behind the map” — linking visuals to source metadata and provenance.  [oai_citation:46‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### Story Nodes (if applicable)
Story Nodes combine **markdown narrative + JSON config** to drive map state (camera, layers, timeline) and should be backed by evidence manifests + PROV.  [oai_citation:47‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:48‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### AR Mode (if applicable)
AR should reuse the same data endpoints (no separate dataset), with careful filtering to avoid clutter and to respect governance.  [oai_citation:49‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### Focus Mode (if applicable)
Focus Mode should answer with citations/provenance derived from ingested data and contracts (no hidden sources).  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 12) 🧪 Optional: simulation/model promotion checklist

Use when the plan includes simulations or models.

- [ ] Results created in sandbox (`data/work/...`) first
- [ ] Inputs pinned (hashes), params captured, env pinned, seeds recorded
- [ ] Verification tests + regression tests
- [ ] Validation vs real-world data where possible
- [ ] Uncertainty quantification / sensitivity analysis where feasible
- [ ] Promote to `data/processed/` only via PR with STAC/DCAT/PROV  [oai_citation:51‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:52‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 13) 🧾 PR template (Executor output)

> Paste this into the PR description.

```markdown
## Summary
- Event: {{EVENT_ID}} (Watcher: {{WATCHER_ID}})
- Plan: {{PLAN_ID}} (Planner: {{PLANNER_ID}})
- Run: {{RUN_ID}} (Executor: {{EXECUTOR_ID}})
- Risk: {{low|medium|high}}
- Required approvals: {{...}}

## What changed
- {{bullet list}}

## Artifacts
- Run manifest: `data/audits/{{run_id}}/run_manifest.json`
- PROV: `data/prov/{{prov_id}}.jsonld`
- STAC/DCAT: `data/catalog/...`
- Evidence manifest (if narrative): `ui/stories/.../evidence/...`

## Tests / Gates
- [ ] Unit tests
- [ ] Schema validators
- [ ] Policy Pack (OPA/Conftest) — fail closed
- [ ] Security scan (if deps changed)

## Governance / CARE / Sensitivity
- Classification: {{...}}
- Redaction/obfuscation: {{...}}
- Notes: {{...}}

## Rollback
- {{strategy + steps}}
```

---

## 14) 📚 Source map (project files → template anchors)

> This section is intentionally explicit so maintainers know which project docs informed which parts of the template.

### Core KFM architecture & governance
- **WPE agents (Watcher/Planner/Executor), immutable event record, PR flow, auditability**  [oai_citation:53‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:54‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **Policy gates (schema/provenance/license/sensitive content) + fail-closed enforcement**  [oai_citation:55‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:56‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **Policy Pack rule categories + waiver mechanism (Evidence for Narratives / Sovereignty / Mandatory CI checks)**  [oai_citation:57‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Data intake, provenance, QA, telemetry
- **Agent-assisted ingestion: AI proposes steps, deterministic code validates/executes; policies apply equally to humans/agents; kill-switch; signing**  [oai_citation:58‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Ingestion gate: checksums, light validation, telemetry logging; deterministic transform & load**  [oai_citation:59‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Simulation sandbox vs promotion + reproducibility/V&V requirements**  [oai_citation:60‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Catalogs & evidence-first publishing
- **Contract-first / no mystery layers; Focus Mode citations from contracts/provenance**  [oai_citation:61‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Boundary artifact patterns (STAC/DCAT/PROV as publish requirements)**  [oai_citation:62‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Story Nodes + evidence manifests + PROV snippet linkage**  [oai_citation:63‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### UI, storytelling, AR
- **UI transparency: “map behind map” provenance linkage**  [oai_citation:64‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **AR mode reuses same data endpoints and filters layers**  [oai_citation:65‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **Innovative future direction (4D digital twins / AR + storytelling emphasis)**  [oai_citation:66‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

### FAIR/CARE & cultural sensitivity
- **Cultural protocols, TK labels, differential access, coordinate fuzzing example**  [oai_citation:67‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

### Distribution & supply chain integrity
- **Run manifest canonicalization + hashing for idempotency**  [oai_citation:68‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **OCI registry distribution with ORAS + cosign signatures/provenance referrers**  [oai_citation:69‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:70‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Real-time & streams
- **Real-time query + provenance logging; classification respected for display**  [oai_citation:71‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Supporting reference portfolios (open externally if needed)
These are PDF portfolios requiring Adobe Reader/Acrobat for best access (still part of the project reference set):
- **AI Concepts & more (portfolio)**  [oai_citation:72‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- **Maps / Google Maps / Virtual Worlds / Geospatial WebGL (portfolio)**  [oai_citation:73‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- **Various programming languages & resources (portfolio)**  [oai_citation:74‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- **Data management / architectures / Bayesian methods (portfolio)**  [oai_citation:75‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)

### Extra project references discovered in the file set (optional but useful)
- **Markdown patterns (checklists, PR templates, badges) as documentation UX**  [oai_citation:76‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz) [oai_citation:77‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- **Scientific method protocol template for research/simulation tasks**  [oai_citation:78‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- **Geospatial/Python/PostGIS cookbook (operational recipes; treat as reference only)**  [oai_citation:79‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

---

## ✅ Final sign-off checklist (fill before submitting)
- [ ] All placeholders replaced
- [ ] Risk + approvals defined
- [ ] Evidence pack complete (sources + checksums)
- [ ] Plan JSON validated
- [ ] Run manifest generated (canonical digest)
- [ ] STAC/DCAT/PROV present (or explicitly “N/A” with rationale)
- [ ] Policy Pack expected gates listed (waiver process used if needed)
- [ ] PR body includes links to Event + Plan + Run Manifest
- [ ] If UI/story affected: evidence manifest + citations block included
