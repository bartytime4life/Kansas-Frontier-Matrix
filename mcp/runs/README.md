---
title: "MCP Runs — Run Records and Reproducibility Logbook"
path: "mcp/runs/README.md"
version: "v1.2.0"
last_updated: "2026-01-19"
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

doc_uuid: "urn:kfm:doc:mcp:runs:readme:v1.2.0"
semantic_document_id: "kfm-mcp-runs-readme-v1.2.0"
event_source_id: "ledger:kfm:doc:mcp:runs:readme:v1.2.0"
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

# MCP Runs — Run Records & Reproducibility Logbook 🧾🧪

![Status](https://img.shields.io/badge/status-draft-yellow)
![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-enabled-brightgreen)
![KFM--MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-blue)
![MCP--DL](https://img.shields.io/badge/MCP--DL-v6.3-purple)

</div>

> 🧭 **KFM rule:** If someone can’t reproduce the run from **(a)** this run record + **(b)** canonical artifacts in `data/**` + **(c)** the recorded commit/config, then the run is **not** “real” for audit/provenance purposes.  
> This is aligned with KFM’s provenance-first / evidence-first stance across intake → catalogs → graph → API → UI → narrative/AI. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 Contents

- [📘 Overview](#-overview)
- [✅ Quick Start](#-quick-start)
- [🧱 Where Runs Sit in the Canonical Pipeline](#-where-runs-sit-in-the-canonical-pipeline)
- [🗂️ Directory Layout](#️-directory-layout)
- [🆔 Run IDs and Correlation IDs](#-run-ids-and-correlation-ids)
- [📦 What Every Run Must Capture](#-what-every-run-must-capture)
- [🧾 Run Manifest (`run.yaml`) Standard](#-run-manifest-runyaml-standard)
- [🌐 STAC, DCAT, PROV Linking Rules](#-stac-dcat-prov-linking-rules)
- [🧪 Simulation Runs](#-simulation-runs)
- [🤖 AI / Focus Mode Runs](#-ai--focus-mode-runs)
- [🗺️ UI / Map Verification Runs](#️-ui--map-verification-runs)
- [🔐 Security, Sensitivity, CARE/Sovereignty](#-security-sensitivity-caresovereignty)
- [🧪 Validation, CI/CD, Policy Pack Gates](#-validation-cicd-policy-pack-gates)
- [🧯 Failures, Rollbacks, and Provenance Repair](#-failures-rollbacks-and-provenance-repair)
- [📎 Templates](#-templates)
- [🕰️ Version History](#️-version-history)
- [📚 Source Pack Used](#-source-pack-used)

---

## 📘 Overview

### Purpose 🎯
`mcp/runs/` is KFM’s **run logbook**: a human-readable + reviewable record of:

- **Intent**: what ran and why  
- **Context**: commit/config/environment and policy pack version  
- **Inputs/outputs**: stable IDs and pointers (not duplicated binaries)  
- **Evidence linkages**: STAC/DCAT/PROV/Graph/API/UI references  
- **Governance outcomes**: policy gates, redactions, and review triggers  

KFM is designed as a layered, provenance-first system where catalog metadata and lineage are “first-class,” and pipelines emit telemetry (unique run IDs, config hashes, success/failure metrics) for traceability. :contentReference[oaicite:2]{index=2}

### Scope ✅/🚫

| In Scope ✅ | Out of Scope 🚫 |
|---|---|
| Run records for ETL, catalogs, graph ingest, API contract tests, UI verification, simulation, AI evaluations. | Canonical STAC/DCAT/PROV outputs (live under `data/**`). |
| Pointers to evidence artifacts (IDs/paths/hashes) + small manifests/logs. | Large binaries, raw data dumps, duplicate processed datasets. |
| Failure records (how to reproduce + remediation plan). | Unsourced narrative conclusions (belongs in governed Story Nodes). |
| Run governance notes: policy checks, sensitivity classification, waivers. | Secrets/credentials/PII/private URLs/sensitive coordinates. |

### Audience 👥
- **Primary:** maintainers/contributors running ingestion/ETL, catalog builds, graph ingest/migrations, API contract tests, UI checks, AI runs, and simulations.  
- **Secondary:** reviewers/auditors validating provenance, reproducibility, governance compliance, and CI gates.

### Definitions 📚
- Glossary (recommended canonical home): `docs/glossary.md`  
  KFM documentation emphasizes consistent terminology (including for AI) as part of governance/standards. :contentReference[oaicite:3]{index=3}

### Key artifacts this README points to 🧩

| Artifact | Path / Identifier | Why you care |
|---|---|---|
| **Master Guide v13 (Draft)** | `docs/MASTER_GUIDE_v13.md` | Canonical pipeline ordering + invariants + governance structure. :contentReference[oaicite:4]{index=4} |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Contract-first, fail-closed policy gates, “one canonical home.” :contentReference[oaicite:5]{index=5} |
| Policy Pack (OPA + Conftest) | `tools/validation/policy/` *(example)* | Machine-enforced governance rules in CI and optionally runtime. :contentReference[oaicite:6]{index=6} |
| AI System Overview | `docs/architecture/ai-system-architecture.md` *(example)* | Focus Mode evidence bundle + governance check + telemetry. :contentReference[oaicite:7]{index=7} |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Governed documentation standard (front matter, IDs, validations). :contentReference[oaicite:8]{index=8} |

### Definition of done ✅
- [x] Front-matter complete + aligned to KFM doc patterns (FAIR+CARE metadata) :contentReference[oaicite:9]{index=9}
- [x] Clear scope boundaries (run logbook vs canonical homes)
- [x] Run record conventions (IDs, required fields, redaction rules)
- [x] Explicit linkage expectations for STAC/DCAT/PROV + graph mirroring :contentReference[oaicite:10]{index=10}
- [x] Simulation “workbench → promotion” rules included :contentReference[oaicite:11]{index=11}
- [x] Policy Pack + fail-closed governance gates referenced :contentReference[oaicite:12]{index=12}
- [ ] Optional: publish a validated schema for `run.yaml` under `schemas/telemetry/` (future)
- [ ] Optional: CLI generator for `RUN_ID/` scaffolds (future)

---

## ✅ Quick Start

### 1) Create the run folder 📁
1. Choose a `RUN_ID` (see [Run IDs](#-run-ids-and-correlation-ids)).
2. Create: `mcp/runs/<RUN_ID>/`
3. Add at minimum:
   - `README.md` (human record)
   - `run.yaml` (machine manifest)

### 2) Record the reproducibility anchors 🔩
At minimum, capture:
- `commit_sha` (+ branch/tag if helpful)
- `config_hash` (hash of the effective config)
- deterministic seeds (if any)
- stable input identifiers + hashes when feasible  
This aligns with reproducibility checklists (record parameters, commit hash, seeds, dependency versions). :contentReference[oaicite:13]{index=13}

### 3) Point to canonical artifacts (don’t copy them) 🧭
- Outputs belong in `data/**` (processed outputs, STAC/DCAT/PROV bundles).
- The run record points to them via IDs/paths/hashes.  
KFM explicitly links STAC/DCAT/PROV together and mirrors them in Neo4j for traversal. :contentReference[oaicite:14]{index=14}

### 4) Validate + (optionally) promote via PR ✅
- Run schema + policy checks (Policy Pack), link checks, secret scans, catalog schema validations.
- For simulations: run in workbench first; promote to `data/processed` only after review. :contentReference[oaicite:15]{index=15}
- If promoting: open a PR that includes the canonical artifacts + this run record (manual or W-P-E Executor). :contentReference[oaicite:16]{index=16}

---

## 🧱 Where Runs Sit in the Canonical Pipeline

KFM is a layered system that moves from ingestion and ETL, to standardized catalogs and provenance, to graph/database indexing, to API contracts, to UI, to narrative/Focus Mode—with governance and telemetry enforcing safety and reproducibility across the stack. :contentReference[oaicite:17]{index=17}

~~~mermaid
flowchart LR
  A["📥 Data Intake / ETL<br/>data/raw → data/work → data/processed"] --> B["🌐 Catalogs<br/>STAC + DCAT"]
  B --> C["🧾 Provenance<br/>PROV bundles"]
  C --> D["🧠 Knowledge Graph + Stores<br/>Neo4j + PostGIS + Search"]
  D --> E["🧩 API Boundary<br/>OpenAPI / GraphQL"]
  E --> F["🗺️ UI<br/>Map + Timeline + Story UI"]
  F --> G["🧠 Story Nodes + Focus Mode"]
  A -.-> H["⚖ Governance + Policy Pack<br/>(CI + optional runtime)"]
  G -.-> H
  A -.-> I["📈 Telemetry (Run IDs + config hashes)"]
~~~

---

## 🗂️ Directory Layout

### Canonical homes (don’t fight the system) 🧭
| Area | Canonical home | Notes |
|---|---|---|
| MCP root | `mcp/` | Experiments, SOPs, run logbook. |
| **Run logbook** | `mcp/runs/` | **Run records + small support files** (this folder). |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog builders + run mechanics. |
| Data staging | `data/raw/`, `data/work/`, `data/processed/` | Raw is immutable; work is sandbox; processed is promotable. :contentReference[oaicite:18]{index=18} |
| Catalogs + provenance | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical STAC/DCAT/PROV artifacts. :contentReference[oaicite:19]{index=19} |
| Graph | `src/graph/` (+ optional `data/graph/`) | Ontology bindings + ingest + fixtures. |
| API boundary | `src/server/` *(or `api/`)* | REST/GraphQL contracts + redaction logic. |
| UI | `web/` | Map + Focus Mode UI consuming API contracts. |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative nodes (evidence-linked). |

### Expected run folder skeleton 🧱
~~~text
📁 mcp/
└── 📁 runs/
    ├── 📄 README.md
    ├── 📁 RUN_ID/
    │   ├── 📄 README.md                # ✅ REQUIRED: human record
    │   ├── 📄 run.yaml                 # ✅ REQUIRED: machine manifest
    │   ├── 📄 checksums.sha256         # ◻ RECOMMENDED: inputs/outputs hashes
    │   ├── 📄 env.txt                  # ◻ RECOMMENDED: runtime + lockfile pointers
    │   ├── 📄 policy_eval.json         # ◻ OPTIONAL: Policy Pack / OPA eval summary
    │   ├── 📄 metrics.json             # ◻ OPTIONAL: small metrics summary
    │   ├── 📄 artifacts.md             # ◻ OPTIONAL: pointers to canonical outputs + external blobs
    │   └── 📁 logs/                    # ◻ OPTIONAL: small logs (NO secrets)
    └── 📁 _templates/
        ├── 📄 RUN_RECORD_TEMPLATE.md
        └── 📄 run.yaml.template
~~~

---

## 🆔 Run IDs and Correlation IDs

### Run ID conventions 🧷
Run IDs must be:
- unique within `mcp/runs/`
- stable enough to reference from PROV + Story Nodes
- filesystem-safe (ASCII, no spaces)

Recommended patterns:
- `YYYY-MM-DD__<area>__<slug>__<shortsha>`
- `YYYYMMDDTHHMMSSZ__<area>__<slug>__<shortsha>`

Examples:
- `2026-01-19__etl__usgs-water-refresh__a1b2c3d`
- `20260119T173012Z__ai__focus-bundle-eval__a1b2c3d`

### Correlation IDs (make it queryable) 🧠
KFM links catalogs and provenance into a traversable evidence graph (STAC/DCAT/PROV mirrored in Neo4j). :contentReference[oaicite:20]{index=20}

For each run, **prefer capturing**:

- `run_id` (folder name)
- `prov_activity_id` (a stable ID for the run as `prov:Activity`)
- `ledger_event_id` *(if governance ledger is used for the action)*
- `config_hash` (hash of the effective config)
- `policy_pack_version` + `policy_eval_id` (CI/runtime gates)
- `stac_item_ids`, `dcat_dataset_ids`, `prov_bundle_paths`

> 💡 KFM also explores mapping GitHub PRs into PROV (PR=Activity, commits=Entities, authors/reviewers=Agents) to make development history queryable lineage. :contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}

---

## 📦 What Every Run Must Capture

### Required (minimum) ✅
- **Intent**: why this run exists (question/task/change)
- **Commit SHA**: exactly what code ran
- **Effective config snapshot**: via `config_hash` + config refs
- **Inputs**: stable IDs + hashes (when feasible)
- **Outputs**: pointers to canonical artifacts in `data/**`
- **Validation status**: what passed/failed
- **Safety notes**: classification/sensitivity/redaction if relevant

This mirrors scientific-method style rigor: define problem, document methods, record data logging, present results with traceability, note limitations and next steps. :contentReference[oaicite:23]{index=23}

### Recommended quality bar ⭐
A high-quality run record:
- pins environment (container digest / lockfiles), and records seeds  
- includes a checksums file for critical inputs/outputs  
- references STAC/DCAT/PROV and links them (run ↔ catalogs ↔ lineage)  
- captures policy-gate results (“fail closed” posture)  
- is review-ready (someone else can reproduce it)

---

## 🧾 Run Manifest (`run.yaml`) Standard

KFM leans on machine-readable governance and provenance (Policy Pack + standards) rather than “tribal knowledge.” :contentReference[oaicite:24]{index=24}

### Minimal required keys ✅
- `run_id`, `run_kind`, `status`, `started_at`
- `commit_sha`
- `config` (at least a `config_hash` + reference)
- `inputs[]` + `outputs[]` (stable IDs/paths)
- `evidence` refs (STAC/DCAT/PROV if applicable)

### Recommended `run.yaml` (v13-friendly) 🧩
~~~yaml
run_id: "20260119T173012Z__etl__example__a1b2c3d"
title: "Example ETL refresh (USGS water stations)"
run_kind: "etl"          # etl | catalog | graph | api | ui | ai | simulation | validation | docs | ad_hoc
status: "success"        # success | failed | partial | cancelled
runner: "manual"         # manual | ci | agent
actor: "human:handle"    # or service principal / bot (no secrets)

timestamps:
  started_at: "2026-01-19T17:30:12Z"
  ended_at: "2026-01-19T17:46:03Z"

code:
  commit_sha: "a1b2c3d4e5f6..."
  branch: "main"
  repo_path_hint: "src/pipelines/..."  # optional pointer

config:
  config_ref: "src/pipelines/hydrology/usgs.yaml"
  config_hash: "sha256:<hash-of-effective-config>"
  deterministic: true
  random_seed: 123456   # if applicable

environment:
  container_image: "ghcr.io/kfm/pipeline:2026-01-19"
  container_digest: "sha256:<digest>"
  lockfiles:
    - "requirements.txt"
    - "package-lock.json"
  sbom_ref: "releases/sbom.spdx.json"  # if available (supply-chain best practice) :contentReference[oaicite:25]{index=25}

governance:
  policy_pack_version: "v13"
  policy_eval:
    ci_conftest: "pass"
    runtime_opa: "n/a"
  classification: "open"
  sensitivity: "public"
  care_label: "TBD"
  waivers:
    - id: "KFM-CAT-001"
      reason: "TBD"
      expires: "2026-02-01"

provenance:
  prov_activity_id: "urn:kfm:prov:activity:20260119T173012Z__etl__example__a1b2c3d"
  prov_bundle_paths:
    - "data/prov/2026/01/19/..."
  ledger_event_id: "ledger:kfm:run:20260119T173012Z__etl__example__a1b2c3d"

inputs:
  - kind: "source"
    id: "usgs:nwis"
    time_range: "2026-01-12/2026-01-19"
  - kind: "file"
    path: "data/raw/usgs/nwis/2026-01-19.csv"
    sha256: "<hash>"

outputs:
  - kind: "dataset"
    id: "kfm.ks.hydro.usgs_nwis.stations.v2026_01_19"
    classification: "open"
  - kind: "stac-item"
    path: "data/stac/items/....json"
  - kind: "dcat-dataset"
    path: "data/catalog/dcat/....jsonld"

evidence_links:
  stac:
    collections: ["kfm.ks.hydro.usgs_nwis"]
    items: ["kfm.ks.hydro.usgs_nwis.stations.2026-01-19"]
  dcat:
    datasets: ["kfm.ks.hydro.usgs_nwis.stations"]
  prov:
    activities: ["urn:kfm:prov:activity:..."]

graph:
  ingested: true
  notes: "STAC/DCAT/PROV mirrored to Neo4j nodes Dataset/Asset/Activity"  # :contentReference[oaicite:26]{index=26}

api:
  contract_version: "vX.Y.Z"
  tests: "pass"

ui:
  permalink: "TBD"  # include URL-encoded state when relevant :contentReference[oaicite:27]{index=27}

notes:
  limitations: []
  followups: []
~~~

---

## 🌐 STAC, DCAT, PROV Linking Rules

### The “Evidence Triplet” 🧾🧠🗺️
KFM intentionally links STAC (asset-level), DCAT (dataset-level), and PROV (lineage) so discovery metadata, technical metadata, and provenance remain connected—and then mirrors that evidence graph into Neo4j for traversal. :contentReference[oaicite:28]{index=28}

**Practical expectations:**
- STAC Item should carry a pointer to the producing PROV `Activity` (or version key)  
- DCAT Dataset should reference STAC and PROV locations (e.g., distribution/hasPart)  
- PROV bundle must record inputs/outputs/agents for transformations

### KFM profile extensions (examples) 🧩
KFM profiles may enforce required properties (e.g., `kfm:dataset_id`, `kfm:classification`) and add sovereignty/sensitivity extensions. :contentReference[oaicite:29]{index=29}

> ✅ **Run record rule:** If your run affects spatiotemporal assets and you can’t point to updated STAC/DCAT/PROV artifacts, the run is **not promotable** to `data/processed` or user-facing layers.

---

## 🧪 Simulation Runs

KFM treats simulations as evidence (with uncertainty), not “truth,” and requires the same rigor as other datasets—plus extra caution and V&V. :contentReference[oaicite:30]{index=30}

### Workbench vs promotion (non-negotiable) 🧰➡️🏛️
- Simulations start in `data/work/sims/` (sandbox / experimental)
- They are **not official** until reviewed and **promoted** to `data/processed` and cataloged  
- Don’t wire the UI directly to workbench outputs :contentReference[oaicite:31]{index=31}

### Promotion checklist ✅
- [ ] Stable IDs assigned  
- [ ] STAC/DCAT/PROV generated (and linked)  
- [ ] Input hashes pinned; parameters captured; environment pinned; random seeds recorded :contentReference[oaicite:32]{index=32}
- [ ] Verification tests + regression checks in place :contentReference[oaicite:33]{index=33}
- [ ] Validation approach documented (compare to real data when possible; assumptions otherwise) :contentReference[oaicite:34]{index=34}
- [ ] Uncertainty quantification + sensitivity notes included (minimum deliverables) :contentReference[oaicite:35]{index=35}
- [ ] Sensitivity + sovereignty reviewed (classification cannot be downgraded)

### W-P-E automation note 🤖
Simulation runs may be initiated by Watcher/Planner/Executor automation: Watcher detects a trigger, Planner proposes steps, Executor runs and opens a PR for promotion. :contentReference[oaicite:36]{index=36}:contentReference[oaicite:37]{index=37}

---

## 🤖 AI / Focus Mode Runs

### Evidence-first AI execution 🧠
Focus Mode is designed as: retrieve evidence → generate answer → governance check → deliver with citations; and it logs telemetry and governance records. :contentReference[oaicite:38]{index=38}

### Hard gate: citations or refuse 🚫✅
KFM policy gates require that any Focus Mode output include citations; if an answer can’t provide a source, it’s a policy violation and must refuse/fail closed. :contentReference[oaicite:39]{index=39}:contentReference[oaicite:40]{index=40}

### What to record for AI runs 🧾
In addition to standard run fields, include:
- evaluation dataset IDs (and hashes)
- metrics: accuracy + citation coverage (at minimum)
- drift monitoring notes (alerts, thresholds, remediation plan) :contentReference[oaicite:41]{index=41}
- prompt-security/prompt-gate version (if applicable) :contentReference[oaicite:42]{index=42}
- whether answers were human-edited (feedback loop)

> 🛡️ Prompt security: KFM describes “Prompt Gate” style defenses that sanitize user inputs and prevent sensitive information leakage. :contentReference[oaicite:43]{index=43}

---

## 🗺️ UI / Map Verification Runs

### Why UI runs matter 🎛️
KFM’s UI is stateful: map position/layers/filters and time ranges can be encoded in a shareable URL. This is gold for reproducibility—record the permalink in the run record. :contentReference[oaicite:44]{index=44}

### What to capture
- UI permalink (URL state)
- environment/browser version (if relevant)
- screenshots (small) or pointers to canonical artifacts
- any API endpoints/queries under test (contract version)

> 🧠 Mapping stack note: KFM’s mapping design includes converting scanned maps to georeferenced web formats (e.g., Cloud-Optimized GeoTIFFs) and serving vector overlays for a modern map UI. :contentReference[oaicite:45]{index=45}

---

## 🔐 Security, Sensitivity, CARE/Sovereignty

### Never store secrets in run records 🔥
Run folders must not contain:
- credentials, tokens, private URLs
- PII
- sensitive coordinates / restricted locations

### Sensitive-location handling 🗺️➡️⬢
KFM describes location generalization (e.g., show a hexagon/area instead of an exact point), access control, and sensitivity tagging in metadata—especially for culturally sensitive locations and endangered resources. :contentReference[oaicite:46]{index=46}

### Classification propagation (no downscoping) ⛓️
Policy rules enforce that the most restrictive classification of inputs carries through to outputs; attempts to downgrade classification/sensitivity should fail policy checks. :contentReference[oaicite:47]{index=47}

### Inference control (avoid “leaking by query”) 🧠🔍
KFM’s “no sensitive location inference” posture pairs well with established privacy approaches like query auditing / inference control (monitor queries that could reconstruct sensitive values). :contentReference[oaicite:48]{index=48}

---

## 🧪 Validation, CI/CD, Policy Pack Gates

### Policy Pack (OPA + Conftest) ⚖️
KFM codifies governance rules as policies (Rego) and enforces them in CI via Conftest; examples include:
- no dataset without license
- AI outputs must include at least one citation
- sensitive data requires review flag
- code must pass tests/lint  
…and it can optionally be used at runtime (e.g., pre-check Focus Mode output). :contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}

### Minimum CI gates (recommended) ✅
- [ ] Policy Pack evaluation (CI) — fail on deny rules :contentReference[oaicite:51]{index=51}
- [ ] STAC/DCAT/PROV schema validation (where referenced)
- [ ] Link checks (docs + catalogs)
- [ ] Secret scanning
- [ ] Unit/integration tests (where relevant)
- [ ] Markdown lint + front-matter schema checks (docs are “tested”) :contentReference[oaicite:52]{index=52}

### PR → PROV integration (optional but powerful) 🧬
KFM proposes emitting PROV JSON-LD for GitHub PR events (PR=Activity, commits=Entities, contributors=Agents) and ingesting into Neo4j for devops provenance queries. :contentReference[oaicite:53]{index=53}

---

## 🧯 Failures, Rollbacks, and Provenance Repair

KFM explicitly calls for rollback runbooks and “provenance repair” procedures—undo changes transparently while keeping lineage intact (mark retractions/rollbacks in PROV). :contentReference[oaicite:54]{index=54}

### Failure run records should include
- minimal reproduction steps (with exact commit + config)
- what gate failed (policy id if possible)
- remediation plan (fix forward, or rollback plan)
- links to PR/issues

### Emergency removal (sensitive leak) 🚨
If something sensitive slips in, guidance emphasizes immediate access revocation and an emergency procedure; treat it like a security incident and improve policy gates afterward. :contentReference[oaicite:55]{index=55}

---

## 📎 Templates

### Template: `RUN_ID/README.md` 🧾
<details>
<summary><strong>Click to expand</strong> 🧾</summary>

```markdown
# <RUN_ID> — <short title> 🧪

## Summary
- **Status:** success | failed | partial | cancelled
- **Run kind:** etl | catalog | graph | api | ui | ai | simulation | validation | docs | ad_hoc
- **Started / ended:** <timestamps>
- **Commit:** <sha> (branch/tag)
- **Config:** <path> (config_hash: sha256:...)

## Intent (problem statement)
- What question/task drove this run?
- What changed since last run?

## Inputs
- List stable dataset IDs, STAC/DCAT refs, source systems, and hashes where feasible.

## Method / Commands
- Exact commands (or CI job names), plus notes on deviations.

## Environment
- Container image + digest / lockfiles / hardware notes.

## Outputs (pointers only)
- STAC refs:
- DCAT refs:
- PROV bundle:
- Graph ingest notes:
- API/UI verification notes (permalinks, endpoints, screenshots):

## Validation & Policy Gates
- Policy Pack summary (pass/fail + notable rule IDs)
- Schema validation results
- Link check + secret scan outcomes

## Sensitivity / CARE / Sovereignty
- Classification/sensitivity tags
- Any redaction/generalization applied (no sensitive coordinates)

## Limitations & Follow-ups
- Known limitations
- Next steps + issues/PRs
```
</details>

### Template: `run.yaml` 🧩
<details>
<summary><strong>Click to expand</strong> 🧩</summary>

```yaml
run_id: "<RUN_ID>"
run_kind: "etl"
status: "success"
runner: "manual"
actor: "human:<handle>"

timestamps:
  started_at: "<ISO8601>"
  ended_at: "<ISO8601>"

code:
  commit_sha: "<sha>"
  branch: "<branch>"

config:
  config_ref: "<path>"
  config_hash: "sha256:<hash>"
  deterministic: true
  random_seed: null

environment:
  container_image: "<image>"
  container_digest: "sha256:<digest>"
  lockfiles: []

governance:
  policy_pack_version: "v13"
  policy_eval:
    ci_conftest: "pass"
    runtime_opa: "n/a"
  classification: "open"
  sensitivity: "public"
  care_label: "TBD"

provenance:
  prov_activity_id: "urn:kfm:prov:activity:<RUN_ID>"
  prov_bundle_paths: []
  ledger_event_id: "ledger:kfm:run:<RUN_ID>"

inputs: []
outputs: []
notes:
  limitations: []
  followups: []
```
</details>

---

## 🕰️ Version History

| Version | Date | Author | Change summary |
|---:|---:|---|---|
| v1.0.0 | 2025-12-22 | ChatGPT | Initial `mcp/runs/` README scaffold. |
| v1.1.0 | 2025-12-28 | ChatGPT | Tightened run ID + manifest conventions; clarified canonical pointers, redaction rules, CI expectations. |
| v1.2.0 | 2026-01-19 | ChatGPT | Integrated v13 governance: Policy Pack gates, fail-closed AI citation rules, simulation promotion model, PR→PROV linkage, security/supply-chain fields, and templates. |

---

## 📚 Source Pack Used

> These are the project documents used to align this README with KFM’s architecture, governance, and reproducibility patterns.

### Core KFM PDFs / docs ✅
- 🧱 Architecture & layers, telemetry/run IDs, governance/security: **KFM — Comprehensive Architecture, Features, and Design** :contentReference[oaicite:56]{index=56}:contentReference[oaicite:57]{index=57}
- 📥 Data intake philosophy (immutability, deterministic ETL), STAC/DCAT/PROV integration: **KFM Data Intake — Technical & Design Guide** :contentReference[oaicite:58]{index=58}:contentReference[oaicite:59]{index=59}
- 🤖 Focus Mode pipeline + governance check + telemetry: **KFM — AI System Overview** :contentReference[oaicite:60]{index=60}:contentReference[oaicite:61]{index=61}
- 🗺️ UI state + shareable URL: **KFM — Comprehensive UI System Overview** :contentReference[oaicite:62]{index=62}
- 🔐 Sensitive location policy + CARE framing: **KFM — Comprehensive Technical Documentation** :contentReference[oaicite:63]{index=63}
- 💡 PR→PROV + rollback runbooks + Policy Pack roadmap: **Latest Ideas & Future Proposals** :contentReference[oaicite:64]{index=64}:contentReference[oaicite:65]{index=65}
- 🧪 Scientific-method rigor for experiments + reproducibility checklists: **Scientific Method / Master Coder Protocol** :contentReference[oaicite:66]{index=66}:contentReference[oaicite:67]{index=67}
- 🧠 Privacy/inference control (query auditing): **Data Mining Concepts & applications** :contentReference[oaicite:68]{index=68}
- 🧾 Doc governance + citations + CI checks for Markdown: **Comprehensive Markdown Guide** :contentReference[oaicite:69]{index=69}
- 🔎 Design gaps (templates, experiments, glossary): **Design Audit — Gaps & Enhancement Opportunities** :contentReference[oaicite:70]{index=70}
- 🗺️ Open-source mapping pipeline notes (COG conversion, OCR parsing, mapping UI): **Open-Source Geospatial Historical Mapping Hub Design** :contentReference[oaicite:71]{index=71}
- 🌟 Future-facing concepts (AR, digital twin, GeoXAI, citizen validation): **Innovative Concepts to Evolve KFM** 

### Project “resource portfolio” PDFs (extract + index recommended) 📦
These files are PDF portfolios (container bundles) and may need extraction into individual docs for search/indexing:
- 📦 AI Concepts & more (portfolio) :contentReference[oaicite:73]{index=73}
- 📦 Maps / Google Maps / Virtual Worlds / Geospatial WebGL (portfolio) :contentReference[oaicite:74]{index=74}
- 📦 Various programming languages & resources (portfolio) :contentReference[oaicite:75]{index=75}
- 📦 Data management theories & Bayesian methods (portfolio) :contentReference[oaicite:76]{index=76}

### Chat filecite markers (for the attached project files) 🔖
- 🤖 AI System Overview :contentReference[oaicite:77]{index=77}
- 🗺️ UI System Overview :contentReference[oaicite:78]{index=78}
- 📥 Data Intake — Technical & Design Guide :contentReference[oaicite:79]{index=79}
- 💡 Innovative Concepts to Evolve KFM :contentReference[oaicite:80]{index=80}

---

### Footer refs 🔗
- 🧭 Master Guide: `docs/MASTER_GUIDE_v13.md`
- 🏛️ Governance: `docs/governance/ROOT_GOVERNANCE.md`
- 🧾 Ethics: `docs/governance/ETHICS.md`
- 🪶 Sovereignty: `docs/governance/SOVEREIGNTY.md`
