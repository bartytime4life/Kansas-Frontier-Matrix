---
title: "♻️ KFM v11.2.4 — Deterministic Retry Loop Pattern (Idempotent Nodes · WAL-Safe Checkpoints · Telemetry-Tuned Backoff) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/autonomy-matrix/patterns/retry-loop/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x compliant"
status: "Active / Enforced"

doc_kind: "Pattern"
intent: "retry-loop-pattern"
role: "autonomy-matrix-reliability-pattern"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/patterns-telemetry.json"
telemetry_schema: "schemas/telemetry/patterns/retry-loop-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public Document"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Reliability Pattern"
redaction_required: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Superseded when retry loop pattern v12 is adopted"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/autonomy-matrix/patterns/retry-loop/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-autonomy-matrix-patterns-retry-loop-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-autonomy-matrix-patterns-retry-loop-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:autonomy-matrix:patterns:retry-loop:v11.2.4"
semantic_document_id: "kfm-pipelines-autonomy-matrix-patterns-retry-loop-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:autonomy-matrix:patterns:retry-loop:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "🗂️ Directory Layout"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "pattern-contract-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Deterministic Pipelines × Reliability × Sustainable Intelligence"
  architecture: "Idempotent Nodes · WAL-Safe · Telemetry-Tuned"
  analysis: "Evidence-Led · Reproducible · FAIR+CARE Grounded"
  data-spec: "STAC/DCAT/PROV-Ready · Carbon-Aware"
  telemetry: "Transparent Metrics · Backoff Intelligence · WAL-Centric"
  graph: "Provenance-Rich · Retry-Safe · Lineage-Consistent"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# ♻️ **KFM v11.2.4 — Deterministic Retry Loop Pattern**  
`docs/pipelines/autonomy-matrix/patterns/retry-loop/README.md`

**Purpose:**  
Define a **governed, deterministic retry pattern** for KFM’s Autonomy Matrix that combines idempotent nodes, WAL-safe checkpoints, and telemetry-tuned backoff to reduce duplicate work, stabilize reliability, and control energy/carbon in retry-heavy pipelines.

</div>

---

## 📘 Overview

### Purpose

This pattern is a drop-in reliability primitive for KFM pipelines (especially Autonomy Matrix–controlled flows) that:

- Ensures **deterministic** retries of ETL/AI nodes.  
- Keeps nodes **idempotent** using explicit run-state contracts and keys.  
- Persists **WAL-safe** checkpoints so replay ≈ rerun.  
- Tunes **exponential backoff** using telemetry (energy, CO₂e, cost, SLO risk).  
- Reduces duplicate energy use and carbon anomalies in **P1/P2 batch** pipelines.

### Background (Plain Language)

Key terms:

- **Idempotent node** — Running the same logical work more than once produces the same materialized outputs (no duplicate rows, no drift), keyed by an `idempotency_key`.  
- **WAL (Write-Ahead Log)** — Every state change is appended to a log before commit; on crash we replay from the log to reconstruct a consistent state.  
- **Deterministic retry** — Same inputs + same configuration ⇒ same sequence of retry/backoff decisions and outputs.  
- **Telemetry-tuned backoff** — Delay between retries depends on live energy/CO₂e/cost/queue metrics, within SLO and policy constraints, using deterministic formulas.

This pattern is intended to be **config-driven** and **portable** across pipelines, not a one-off implementation.

---

## 🧭 Context

The Deterministic Retry Loop Pattern sits alongside:

- **Autonomy Matrix** — which decides *when* to run or slow/pause pipelines.  
- **Run-State Pattern** — which defines standard lifecycle states for nodes.  
- **Energy & Carbon Standards** — which define how cost/energy/CO₂e are measured and budgeted.  

This pattern is responsible for:

- Making individual nodes **safe to retry**, even under at-least-once messaging.  
- Providing **WAL-backed evidence** of what happened on each attempt.  
- Making backoff decisions **explainable** and re-playable for audits and simulations.

It is particularly important where:

- Work is expensive (GPU, big joins).  
- Energy/carbon budgets are tight.  
- P2 batch workloads can be shifted in time to avoid peaks.  
- Incident replay and “what if” analysis are part of SRE practice.

---

## 🧱 Architecture

### Run-State Contract (Required)

Nodes MUST expose and honor this run-state contract:

~~~text
PENDING → RUNNING → (SOFT_FAIL | HARD_FAIL | COMPLETE)

SOFT_FAIL: transient; eligible for retry per policy
HARD_FAIL: non-transient; requires operator/automation escalation
~~~

For every transition, persist (WAL entry):

- `run_id` (UUIDv7)  
- `node_id`  
- `attempt` (monotonic per `idempotency_key`)  
- `input_hash` (normalized inputs)  
- `seed` (base RNG seed)  
- `cfg_hash` (hash of config snapshot)  
- `idempotency_key` (derived from inputs + target partition)  
- `checkpoint_ref` (WAL page / object version)  
- `telemetry_snapshot` (energy_kWh, carbon_kgCO2e, cost_usd, duration_s, queue_depth, etc.)  
- `decision_proof` (machine-readable explanation for retry/backoff/escalate)

This contract MUST be compatible with any existing **Run-State Pattern** documents.

### WAL-Safe Checkpoints

Guidelines:

- **Before** any side-effect, write WAL entry `INTENT`.  
- **After** side-effect, write `COMMIT` with artifact digests and lineage edges.  
- Use **monotonic attempt numbers**; all attempts share the same `idempotency_key`.  
- Outputs must be:
  - **Content-addressed** (hash-stable artifact references).  
  - **Partition-addressed** (e.g., date/site/H3 partition keys).  

Replay behavior:

- WAL replay reconstructs `PENDING → RUNNING → ...` sequences without human intervention.  
- If the replay sees `COMPLETE` with valid digests, it **must not** recompute work.

### Exponential Backoff (Telemetry-Tuned)

Base policy (deterministic):

~~~text
delay = min(max_delay_s, base_delay_s * 2^attempt + jitter)
attempt ≤ max_attempts
~~~

Where:

- `jitter` is deterministic, derived from `jitter_seed` (no unlogged randomness).  
- `max_attempts` and delay bounds are policy-driven.

Telemetry tuning overlay:

- If `grid_intensity_gCO2/kWh` is high → prefer longer delay (within SLO).  
- If `energy_rate_usd/kWh` is at peak → prefer longer delay.  
- If `deadline_risk` increases (low buffer, high queue depth) → shorten delay within carbon/energy policy.  

All computed values and thresholds **must** be included in `decision_proof`.

### Duplicate-Work Guards

The pattern assumes **at-least-once messaging** but guarantees **exactly-once effects**:

- **Idempotency key enforcement** at queue ingress (e.g., SQS FIFO or logical de-dupe table).  
- **Artifact existence check** by digest before compute; if artifact exists, short-circuit to `COMPLETE`.  
- **Lease/lock** per `(node_id, idempotency_key)` during `RUNNING`.  
- Time-bounded leases with WAL-backed renewal to avoid deadlocks.

### Deterministic Retry Loop — Pseudocode (Reference)

~~~python
def retry_loop(node, inputs, cfg):
    run = hydrate_run_context(node, inputs, cfg)
    k = derive_idempotency_key(inputs, cfg.target_partition)

    if artifact_exists(k):  # fast idempotent exit
        wal.append(run, state="COMPLETE", reason="artifact_exists")
        return OK

    attempt = 0
    while attempt < cfg.max_attempts:
        attempt += 1
        seed_rng(run.seed, attempt)  # deterministic
        wal.append(run, state="RUNNING", attempt=attempt, intent="compute")

        try:
            checkpoint = node.preflight_checkpoint(run, k)  # WAL-safe
            out = node.compute(inputs, cfg, checkpoint)      # pure & replayable
            write_artifacts(out, k)                          # content-addressed
            wal.append(run, state="COMPLETE", artifacts=digest(out))
            return OK

        except TransientError as e:
            wal.append(run, state="SOFT_FAIL", error=str(e))
            delay = backoff_with_telemetry(run, attempt, cfg)  # deterministic fn
            sleep(delay)
            continue

        except PermanentError as e:
            wal.append(run, state="HARD_FAIL", error=str(e))
            escalate(run, policy="autonomy-matrix")
            return HARD_FAIL

    # attempts exhausted
    wal.append(run, state="HARD_FAIL", error="max_attempts_exceeded")
    escalate(run, policy="deadline-aware")
    return HARD_FAIL
~~~

---

## 📦 Data & Metadata

### Telemetry Inputs (Minimum)

The backoff and governance logic must have access to:

- `energy_kWh` (node + dependencies)  
- `grid_intensity_gCO2/kWh` (regional signal)  
- `carbon_kgCO2e` (derived from energy × intensity)  
- `energy_rate_usd/kWh`  
- `compute_unit_cost_usd` (GPU/CPU hourly cost)  
- `deadline_at`, `sla_ms`, `error_budget_remaining`  
- `queue_depth`, `arrival_rate`, `parallelism_limits`  

These metrics feed:

- `backoff_with_telemetry(...)`  
- Autonomy Matrix decision-making (resume/slow/pause/escalate)  
- Energy/carbon dashboards and reports.

### Policy Knobs (YAML, Versioned)

Pattern behavior is configured via YAML under `policies/`:

~~~yaml
retry_policy:
  max_attempts: 6
  base_delay_s: 10
  max_delay_s: 900
  jitter_seed: "<sha256(run_id)>"

telemetry_tuning:
  carbon_intensity_threshold_g_per_kWh:
    low: 250
    high: 500
  energy_price_usd_per_kWh:
    peak: 0.25
  deadline_bias:
    enabled: true
    min_deadline_buffer_s: 1800
~~~

Rules:

- Policies are **versioned** and **signed** (e.g., Sigstore).  
- Changes to backoff math or thresholds bump the pattern config version (`retry-loop-v<minor>`).  
- All policies live under:
  - `docs/pipelines/autonomy-matrix/patterns/retry-loop/policies/*.yaml`  

### Integration Points in KFM

- **Pipelines** — wrap stage executors in:
  - P2 Batch (`src/pipelines/batch/*`)  
  - Selected P0/P1 flows where deterministic replay is required.  
- **Lineage (PROV-O)** — emit:
  - `prov:used` for inputs.  
  - `prov:wasGeneratedBy` for node runs.  
  - `prov:wasDerivedFrom` for derived artifacts.  
- **STAC/DCAT** — write:
  - Item/asset checksums.  
  - `processing:attempt`, `processing:energy_kWh`, `processing:carbon_kgCO2e`.  
- **OpenTelemetry** — annotate spans with:
  - `run_id`, `attempt`, `idempotency_key`.  
  - `energy_kWh`, `carbon_kgCO2e`, `cost_usd`.

---

## 🧪 Validation & CI/CD

### What “Good” Looks Like (Acceptance Criteria)

A pipeline using this pattern is considered healthy when:

- Re-running any failed window produces **identical** artifacts and lineage IDs.  
- WAL replay reconstructs run states without manual edits.  
- Energy/carbon per period show **no “double spikes”** caused by duplicate retries.  
- Retry decisions are explainable from `decision_proof` logs alone (no tribal knowledge).  

### Ops Runbook (Short)

Typical operations:

- **Replay a run:**  
  - `kfm-replay --run <run_id>` — WAL-driven; inputs considered read-only.  
- **Quarantine a permanent failure:**  
  - Mark run `HARD_FAIL`; open a ticket or `CARE_ESCALATION` if data is sensitive.  
- **Inspect carbon anomalies:**  
  - Query `telemetry_snapshot` by `idempotency_key` window and correlate with Autonomy Matrix decisions.

### Security & Supply Chain

To keep the pattern supply-chain safe:

- Sign policy files (e.g., with Sigstore).  
- Pin containers and dependencies via SBOM digests.  
- Deny unpinned images at CI/CD gates.  
- Validate pattern code against:
  - `security-advisory-check` (where relevant).  
  - Static analysis rules for dynamic execution (no ungoverned `eval` in backoff logic).

### Versioning & Governance

- Any change to:
  - Backoff formulas.  
  - Telemetry thresholds.  
  - State machine semantics.  
  must be captured as:
  - Pattern version bump (`retry-loop-vX.Y`).  
  - Policy YAML version bump.  
  - Dashboard before/after diff (energy/carbon and duplicate work metrics).

- Observability dashboards should show:
  - Baseline vs. pattern-enabled periods.  
  - Incident windows with and without telemetry-tuned backoff.

---

## 🗂️ Directory Layout

Authoritative retry-loop subtree:

~~~text
docs/pipelines/autonomy-matrix/patterns/retry-loop/
├─ README.md                     # This file (pattern definition)
├─ policies/
│  ├─ default.yaml               # Default retry policy
│  └─ p2-batch-reporting.yaml    # Tuned policy for P2 batch reporting
├─ examples/
│  ├─ p2-batch-reporting/
│  │  ├─ scenario-deadline-catchup.md
│  │  ├─ scenario-monthly-carbon-cap.md
│  │  └─ scenario-offhours-slowdown.md
│  └─ p0-storm-nowcast/
│     ├─ scenario-carbon-clamp.md
│     ├─ scenario-care-escalation.md
│     └─ scenario-thrash-control.md
└─ specs/
   ├─ wal-checkpointing.md       # Detailed WAL integration
   └─ idempotency-contract.md    # Shared idempotency semantics across KFM
~~~

### Related Standards & Patterns

- `../../../patterns/README.md` (Pipelines Patterns Index)  
- `../../../patterns/run-state/README.md` (Run-State Pattern v11.2.x)  
- `../../../../standards/energy/README.md` (Energy Standards Index v11.2.4)  
- `../../../../standards/telemetry/` (Energy, carbon, cost schemas)  
- `../../../../standards/provenance/prov-o.md` (Lineage standard)  
- `../../../messaging/sqs-fifo-dedup/README.md` (Ingress de-dupe)

---

## ⚖ FAIR+CARE & Governance

This pattern supports FAIR+CARE by:

- **Findable & Reusable** — Run histories and retry decisions are indexed in the WAL and telemetry, with stable identifiers.  
- **Responsible Energy/Carbon Use** — Telemetry-tuned backoff avoids unnecessary duplicate work and peak-energy retry storms.  
- **Risk & Sovereignty** — For heritage or sensitive datasets, retries are still deterministic, traceable, and governed, reducing the chance of silent data corruption during recovery.  

Governance hooks:

- Pattern usage in pipelines should be reviewed during:
  - **Reliability reviews** (SLO design, incident postmortems).  
  - **Sustainability reviews** (energy/carbon budgets).  
- Any pipeline classified as `Sensitive` or with `indigenous_rights_flag: true` in its metadata should have:
  - Additional human review on **HARD_FAIL** runs.  
  - Explicit notes in policy YAML about CARE-aware behavior.

---

## 🕰️ Version History

| Version   | Date       | Notes                                                                                             |
|----------:|------------|---------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial governed release for KFM v11.2.4; formalized WAL-safe retry loop, telemetry-tuned backoff, and P2/P0 scenario examples. |

---

<div align="center">

♻️ **KFM v11.2.4 — Deterministic Retry Loop Pattern**  
Deterministic ETL · WAL-Safe Checkpoints · Telemetry-Tuned Backoff  

[📘 Pipelines Index](../../../README.md) · [🧠 Autonomy Matrix](../../README.md) · [⚖ Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>