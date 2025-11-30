---
title: "🔄 Kansas Frontier Matrix — Auto-Update Orchestrator (kfm-auto-update.yml)"
path: "docs/architecture/ci/kfm-auto-update.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "ci-auto-update-orchestrator"
role: "auto-update-architecture"
category: "CI/CD · Automation · Governance · Telemetry"

classification: "Public Document"
sensitivity: "General"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
indigenous_rights_flag: false

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
data_steward: "KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - ".github/workflows/kfm-auto-update.yml@v11.2.2"
  - ".github/workflows/kfm-auto-update.yml@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

json_schema_ref: "../../schemas/json/kfm-auto-update-architecture-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/kfm-auto-update-architecture-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "content-alteration"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🔄 **Kansas Frontier Matrix — Auto-Update Orchestrator (kfm-auto-update.yml)**  
`docs/architecture/ci/kfm-auto-update.md`

**Purpose**  
Describe the architecture, governance hooks, lineage, and telemetry behavior of  
`.github/workflows/kfm-auto-update.yml`, which performs **scheduled, governed promotion** of  
KFM data/models from **stage → prod** under **FAIR+CARE**, **sovereignty**, and **supply-chain** controls.

</div>

---

## 📘 Overview

The **Auto-Update Orchestrator** is a **two-stage CI/CD workflow**:

1. **Stage ingest + validation (`ingest` job)**  
   - Runs the ingest agent against staging resources.  
   - Performs metadata, governance, sovereignty, and data-contract checks.  
   - Emits lineage and telemetry for the ingest run.

2. **Governed promotion to production (`promote` job)**  
   - Gated by the `ingest` job and the `prod` environment.  
   - Re-applies critical FAIR+CARE, H3, and supply-chain checks.  
   - Promotes artifacts from stage → prod and tags a release.

The entire workflow runs:

- **Daily at 03:00 UTC** on a cron trigger, and  
- On-demand via **`workflow_dispatch`** with an optional `reason` input.

---

## 🧱 Workflow Architecture

### 1. Triggers

- `schedule: 0 3 * * *` (daily auto-refresh)
- `workflow_dispatch` (manual, with optional explanation for audit)

These triggers are modeled as **prov:Activity start events**, allowing governance to distinguish:

- Regular scheduled auto-refresh  
- Explicit human-driven manual promotions  

### 2. Concurrency & Permissions

- **Concurrency group:** `kfm-auto-update`  
  - Ensures only one auto-update run is active at a time.

- **Permissions:**
  - `contents: write` (tagging and pushing tags)  
  - `id-token: write` (optional OIDC-auth to clouds)  
  - `actions: read` + `packages: read` (supply-chain context)

These permissions are the **minimum** required for orchestrated promotion and release tagging.

---

## 🧪 Ingest & Validate (Stage)

Job: `ingest`  
Environment: `stage`  

### Responsibilities

1. **Repository & runtime bootstrap**

   - Checks out `main` or relevant branch.  
   - Installs Python dependencies (locked via `requirements.txt`).  
   - Uses `PYTHON_VERSION: 3.11` consistently across jobs.

2. **Execute Ingest Agent**

   The call:

   ~~~text
   python run_agent.py --mode ingest --stage stage
   ~~~

   encapsulates:

   - pulling upstream data or model artifacts  
   - staging them into the **stage** environment  
   - applying any domain-specific transform logic required for KFM usage

3. **Validation stack**

   - **Markdown + docs:** KFM-MDP v11.2.2 rules (front-matter, headings, layout).  
   - **STAC:** KFM-STAC v11 Items/Collections validated for new/updated assets.  
   - **DCAT:** KFM-DCAT v11 dataset records updated & validated.  
   - **JSON-LD:** ontology-aligned JSON-LD (CIDOC, PROV-O, OWL-Time, GeoSPARQL).

4. **FAIR+CARE & Sovereignty**

   - `run_faircare_checks.py` ensures new or changed datasets have:
     - appropriate FAIR and CARE labels,  
     - correct sensitivity flags, licensing, and stewardship fields.  

   - `h3_masking_check.py --stage stage` ensures:
     - high-precision coordinates are not directly exposed for archaeological or tribal sites.  
     - metadata is updated to reflect generalization (H3 index resolution, etc.).

5. **Data contracts & lineage**

   - `validate_pipelines.py` enforces KFM-PDC v11 contracts:  
     - stable schemas, units, ranges, etc.  
   - `emit_lineage.py --env stage --mode ingest`:
     - emits OpenLineage events describing ingest tasks, sources, and outputs.  

6. **Telemetry**

   - `telemetry_collect.py --env stage` writes stage-level telemetry to `github-infra-telemetry.json`.  
   - Telemetry is uploaded as an artifact (`telemetry-stage`) for later aggregation.

---

## 🚀 Promote to Production (Governed)

Job: `promote`  
Needs: `ingest`  
Environment: `prod` (gated)  

### Responsibilities

1. **Gated entry**

   - `needs: ingest` ensures promotion only runs after **successful** stage ingest + validation.  
   - `environment: prod` includes environment-level approvals and optional wait timers.

2. **Final governance checks**

   - **FAIR+CARE** (`run_faircare_checks.py --env prod`) re-checks:
     - licensing, CARE labels, FAIR categories in the final promoted assets.  

   - **H3** (`h3_masking_check.py --stage prod`) ensures:
     - no regression in spatial masking between stage and prod.  

3. **Supply-chain validation**

   - `verify_supply_chain.py` ensures:
     - SBOM present + consistent with `manifest.zip`.  
     - SLSA-like attestations and signatures valid.  

4. **Promotion & tagging**

   - `promote.py --from stage --to prod`:
     - copies or reconfigures artifacts from staging locations to production.  
     - may update STAC/DCAT to point to production resources.

   - `print_version.py` + tag:
     - creates annotated tag `kfm-<ver>` using a bot identity:
       - `kfm-auto-update-bot <auto@kfm.example.org>`  
     - pushes tags back to the remote.

5. **Telemetry**

   - `telemetry_collect.py --env prod` creates a prod-level telemetry JSON.  
   - Uploaded as `telemetry-prod` artifact for governance dashboards and historical analysis.

---

## 🧩 Interaction with Other Workflows

- **`kfm-auto-update.yml`** does not replace core **PR-driven** CI; instead it:
  - Operates on a reliable branch (e.g., `main`).  
  - Uses the same validation logic in scripts as PR workflows use via composite actions.  

- Outputs from this workflow feed into:

  - `telemetry_export.yml` — to merge multiple telemetry sources.  
  - `release.yml` — to package and sign official releases that incorporate auto-updated content.  
  - Focus Mode system health narratives via Story Nodes (see `kfm-auto-update.story-node.json` below).

---

## 🧠 Story Node & Focus Mode Integration

The auto-update process is represented in Focus Mode via a **system Story Node**, enabling:

- Timeline views of auto-refresh runs.  
- Geographic and dataset context (which collections were updated).  
- Governance overlay (how many checks passed, any violations).  

See `docs/story-nodes/system/kfm-auto-update.json` in the next section.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|---------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Deep architecture doc created; added lineage, telemetry, FAIR+CARE, sovereignty, and promotion behavior sections. |
| v11.2.0 | 2025-11-27 | First inclusion of `kfm-auto-update.yml` into CI/CD documentation; described stage → prod pattern.            |
| v11.0.0 | 2025-11-18 | Initial auto-update pattern drafted as part of v11 CI/CD experiments.                                         |

---

<div align="center">

🔄 **Kansas Frontier Matrix — Auto-Update Orchestrator (kfm-auto-update.yml)**  
Provenance-First · Governance-Aware · FAIR+CARE-Aligned  

[⬅ CI/CD Master Architecture](README.md) · [⚙ GitHub Infrastructure](../README.md) · [🛡 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
