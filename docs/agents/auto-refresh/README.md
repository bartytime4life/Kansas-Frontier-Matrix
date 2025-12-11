---
title: "🤖 KFM — Auto-Refresh Agent Loop (Telemetry-Driven PRs)"
path: "docs/agents/auto-refresh/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Draft / Experimental"
lifecycle: "Incubation"
review_cycle: "Monthly · FAIR+CARE Council & Reliability Engineering"
content_stability: "evolving"
status: "Active / In-Repo Canonical"

doc_kind: "Design Note"
intent: "provenance-telemetry-agent-prs"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-agents-auto-refresh-v11.2.6"
doc_uuid: "urn:kfm:doc:agents:auto-refresh:v11.2.6"
event_source_id: "ledger:docs/agents/auto-refresh/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/provenance-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/provenance-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
---

# 🤖 KFM — Auto-Refresh Agent Loop (Telemetry-Driven PRs)

## 📘 Overview

This design note describes a **governed auto-refresh agent** that:

- Monitors **commit and pipeline telemetry** (SBOMs, checksums, provenance JSON-LD, OpenLineage events).  
- Watches **upstream dataset and schema state** (STAC/DCAT versions, SDA/NOAA/NASA feeds, etc.).  
- Detects **drift** (version, checksum, schema, or governance deltas).  
- Proposes **scoped pull requests (PRs)** that:
  - Regenerate ETL manifests and STAC/DCAT/PROV lineages.  
  - Run CI validations.  
  - Attach attestations and governance notes.

This loop does **not** auto-merge; it is a **PR-suggesting agent** that keeps KFM closer to “continuously fresh and continuously reproducible” while preserving human review and FAIR+CARE controls.

The agent fits into the KFM pipeline as a **meta-layer**:

> Telemetry → Drift detection → Agent plan → Regenerated configs/metadata → PR → CI/CD → Merge → Updated ETL/STAC/DCAT/PROV → Neo4j → API/UI → Story Nodes / Focus Mode

---

## 🗂️ Directory Layout

This module lives under `docs/agents/auto-refresh/` and is paired with implementation code and telemetry schemas:

~~~text
📁 docs/
  📁 agents/
    📁 auto-refresh/
      📄 README.md                 # This file – design for telemetry-driven auto-refresh PR agent
      📄 scenarios.md              # (planned) Example drift scenarios + agent behaviors
      📄 limits-and-risks.md       # (planned) Guardrails, failure modes, and human-in-the-loop rules

📁 src/
  📁 agents/
    📁 auto_refresh/
      📄 __init__.py
      📄 loop.py                   # Main agent loop orchestration
      📄 telemetry.py              # Ingests provenance, SBOM, OpenLineage, CI metrics
      📄 drift_rules.py            # Drift detection & classification (schema, version, checksum, governance)
      📄 git_client.py             # Git operations (branching, commit, diff)
      📄 pr_client.py              # PR creation & metadata hooks
      📄 planner.py                # Turn drift events into concrete change plans
      📄 renderers.py              # Render ETL/STAC/DCAT/PROV updates and docs

📁 schemas/
  📁 telemetry/
    📄 provenance-v2.json          # Telemetry schema used by the agent (referenced above)
~~~

Any new files in `docs/agents/auto-refresh/` or `src/agents/auto_refresh/` MUST be documented here as they are added.

---

## 🧭 Context

### 1. Problem

KFM depends on many **external and internal sources**:

- External: USDA, NOAA, NASA, ESA, OpenAQ, SDA, gNATSGO, etc.  
- Internal: STAC/DCAT/PROV catalogs, ETL manifests, Neo4j schema, telemetry schemas.

When:

- upstream datasets get **new versions**,  
- schemas or contracts evolve,  
- governance rules are updated, or  
- CI telemetry flags **rising error rates**,

it becomes easy for the repo to **drift out of alignment** with reality. Manual refreshes can be slow or inconsistent.

### 2. Goal

The auto-refresh agent aims to:

- **Continuously detect drift** based on **provenance + telemetry**, not guesswork.  
- **Generate PRs**, not blind mutations:
  - Changes are always visible as diffs.  
  - CI/CD and governance checks run as usual.  
- **Document why** each PR exists (which drift signal triggered it).

This design is **Draft / Experimental** and must remain behind feature flags or sandbox branches until governed for production use.

---

## 🧱 Architecture (KFM Pipeline Fit)

### 1. Inputs

The agent consumes:

- **Telemetry streams**:
  - Provenance events (PROV-O / OpenLineage) from ETL and catalog jobs.  
  - CI metrics (success rates, error types, test coverage, time since last refresh).  
  - SBOM diffs (new dependencies, security patches).  

- **Catalog & schema state**:
  - STAC/DCAT collections and items for key domains.  
  - JSON Schemas and SHACL shapes used in validation.  
  - Governance docs and policy versions (for opt-in monitoring).  

- **Configuration**:
  - Drift rules (YAML) specifying which signals matter:
    - version drift,
    - checksum drift,
    - schema drift (breaking / non-breaking),
    - governance drift (policy changes requiring docs updates).

### 2. Core Loop

Conceptual pseudocode:

~~~text
while True:
  drift_events = detect_drift_from_telemetry_and_catalogs()
  plans = plan_changes_from_drift(drift_events)
  for plan in plans:
    branch = git_client.create_branch(plan)
    renderers.apply_plan_to_repo(plan, branch)
    git_client.open_pr_with_metadata(branch, plan)
  sleep(config.scan_interval)
~~~

Key steps:

1. **Detect drift**: query telemetry + catalogs, apply rules.  
2. **Plan change**: choose actions (refresh manifests, bump versions, regenerate PROV bundles, update docs).  
3. **Render changes**: edit ETL configs, STAC/DCAT JSON, PROV JSON-LD, or docs in a deterministic way.  
4. **Open PR**: attach provenance, telemetry snapshots, and governance context.

### 3. Boundaries & Guardrails

The agent MUST:

- Only operate on **config/metadata/docs**, not raw data or graph content directly.  
- Never push directly to `main` or any protected branch.  
- Respect **code owners** and governance:
  - Assign appropriate reviewers.
  - Tag PRs with domain labels (e.g., `domain:soil`, `domain:air-quality`).
- Provide a clear “off switch” (feature flags or config) for each domain.

---

## 📦 Data & Metadata

### 1. Telemetry Schema (provenance-v2.json)

The `provenance-v2.json` telemetry schema (referenced in front-matter) describes:

- Drift signals:
  - `kind` (`version`, `checksum`, `schema`, `governance`, `telemetry-anomaly`).  
  - `source` (dataset ID, STAC Collection ID, telemetry stream ID).  
  - `severity` and `confidence`.  
- Context:
  - `old_value`, `new_value`, and diff snippets.
  - Time window of observed drift.  
- Agent actions:
  - `plan_id`, `planned_changes`, `target_paths[]`.

The agent MUST log:

- One record per drift detection.  
- One record per plan applied.  
- A linkage between plan IDs and resulting PR numbers.

### 2. Provenance & Attestations

Each agent-generated PR MUST include:

- A pointer to a **PROV bundle** describing:
  - Inputs: telemetry snapshots, catalog entries, configuration.  
  - Activity: “auto-refresh-planning@version” and “auto-refresh-apply@version”.  
  - Agents: the auto-refresh service and human reviewers.

- Attestations (SLSA/DSSE where applicable) capturing:
  - Which code version and config were used.  
  - Which CI workflows validated the PR.  
  - SBOM references for updated components.

---

## ⚖ FAIR+CARE & Governance

Even though this is a tooling/automation feature, FAIR+CARE and sovereignty still apply:

- **FAIR**:
  - Changes must be explainable, with machine-readable provenance.  
  - Agent-generated PRs must link to the underlying drift signals (telemetry, catalogs).  

- **CARE**:
  - Agent MUST NOT:
    - Expand data exposure or loosen access control without explicit governance approval.  
    - Introduce new public datasets without human review of sensitivity, sovereignty, and license.  
  - For **Indigenous or sensitive domains**, the agent:
    - May detect drift, but PR templates must explicitly flag “requires Indigenous/sovereignty review” where appropriate.  
    - Must never override redaction or access levels.

- **Human in the loop**:
  - No auto-merge on agent PRs.  
  - Governance and domain owners retain final say on whether a refresh is accepted.

---

## 🧪 Validation & CI/CD

The auto-refresh agent is deeply tied to CI/CD and must:

- Be tested in **sandbox environments** (separate repos or branches) before operating on canonical KFM.  
- Pass standard KFM checks:
  - `markdown-lint`, `schema-lint`, `metadata-check` for any doc changes.  
  - STAC/DCAT/PROV validators for catalog changes.  
  - Domain-specific test suites (e.g., soil, air quality, hydrology) for config changes.

Agent-specific tests SHOULD include:

- **Unit tests**:
  - Drift detection rules (expected vs unexpected drift).  
  - Plan generation for common scenarios (e.g., new STAC version, SDA schema change).  

- **Integration tests**:
  - End-to-end “drift → PR” flow in a sandbox repo.  
  - Handling of conflicting PRs (agent backs off when humans are mid-change).  

- **Safety tests**:
  - Ensure the agent never:
    - Bypasses code owners.  
    - Touches disallowed directories (e.g., secret stores, raw restricted datasets).  
    - Removes or downgrades governance metadata.

CI workflows for this agent should live in `.github/workflows/agents-auto-refresh.yml` (or similar), and may be triggered:

- Periodically (cron).  
- After key pipeline jobs complete.  
- Manually (for experiments and debugging).

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                 |
|----------:|-----------:|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | Initial design note for telemetry-driven auto-refresh PR agent; defined architecture, telemetry schema linkage, guardrails, and CI expectations. |

---

<div align="center">

🤖 **KFM — Auto-Refresh Agent Loop (Telemetry-Driven PRs)**  
Reproducibility · Provenance · Governance-Aware Automation  

[📘 Docs Root](../../README.md) · [🧩 Agents Index](../README.md) · [🛡 Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>