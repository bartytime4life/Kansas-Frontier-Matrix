---
title: "⏱️ KFM — Trigger & Retry Decision Matrix (Cron · Webhook · Upstream-Event)"
path: "docs/runbooks/reliability/trigger-retry-matrix.md"
version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Council · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Runbook"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

semantic_document_id: "kfm-trigger-retry-matrix"
doc_uuid: "urn:kfm:runbook:reliability:trigger-retry-matrix:v11.2.6"
event_source_id: "ledger:runbooks/reliability/trigger-retry-matrix"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "layout-normalization"
  - "a11y-adaptations"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# ⏱️ **KFM — Trigger & Retry Decision Matrix**
`docs/runbooks/reliability/trigger-retry-matrix.md`

**Purpose**  
Provide safe, governed defaults for **when KFM jobs run** and **how they retry** across trigger types  
(**cron**, **webhook**, **upstream-event**) while preserving **idempotency**, **deterministic replays**, and **auditable provenance**.

</div>

## 📘 Overview

This runbook defines actionable defaults for job scheduling and retries:

- **Triggers**
  - `cron` — scheduled execution
  - `webhook` — immediate request-driven execution
  - `upstream-event` — event-driven ingestion (object store, queue, pub/sub)
- **Goals**
  - deterministic replays
  - bounded retries and bounded failure amplification
  - consistent idempotency (no duplicate rows/files/edges)
  - machine-readable provenance (PROV-O/OpenLineage) for every run

Definitions:

- **Idempotency** means running the same job twice produces the same final state (no duplicate rows, files, or graph edges).
- **Provenance** means emitting machine-readable lineage (PROV-O/OpenLineage) for every run, including failure runs.

## 🗂️ Directory Layout

~~~text
📁 docs/
├── 📁 runbooks/                                    — Operational runbooks (governed)
│   ├── 📁 reliability/                             — Reliability policies and procedures
│   │   ├── 📄 trigger-retry-matrix.md               — Trigger & retry decision matrix (this runbook)
│   │   └── 📄 <other_reliability_runbooks>.md       — Canonical runbooks for retries, SLIs/SLOs, DLQs, etc.
│   └── 📄 README.md                                — Runbooks index
└── 📁 standards/                                   — Governance + FAIR+CARE + sovereignty policies
    ├── 📁 governance/
    ├── 📁 faircare/
    └── 📁 sovereignty/
~~~

## 🧭 Context

### Why “trigger kind” changes retry policy

Retry is not one-size-fits-all:

- **Cron** retries should be bounded to avoid overlapping scheduled runs and to prevent “retry storms” across many jobs.
- **Webhook** retries should be short-lived and conservative, because they’re often initiated by humans/agents and can include policy boundaries (auth, signatures, approvals).
- **Upstream-event** retries should be more patient and DLQ-aware, because upstream systems can be bursty and transiently unavailable.

### Universal guardrails (apply to all triggers)

- **Always define an idempotency key (IK).**
- **Never retry in tight loops.** Use backoff and jitter.
- **Do not partially publish.** If the job produces governed artifacts, use `stage → validate → promote`.
- **Emit provenance on success and failure.** Failure events are audit evidence.

## 🗺️ Diagrams

~~~mermaid
flowchart TB
  T["Trigger (cron / webhook / upstream-event)"] --> IK["Compute idempotency key (IK)"]
  IK --> G["Policy gates (auth, governance, contracts)"]
  G --> R["Run job (deterministic, replayable)"]
  R --> W["Writes (idempotent: upsert/merge, content-addressed artifacts)"]
  W --> P["Emit provenance (PROV/OpenLineage)"]
  R -->|failure| B["Retry controller (budget + backoff + jitter)"]
  B -->|exhausted| DLQ["Quarantine/DLQ + incident hooks"]
  B -->|retry| R
~~~

## 🧠 Story Node & Focus Mode Integration

Focus Mode MAY:

- summarize this runbook into operator checklists,
- extract default retry values into structured configuration suggestions,
- link jobs/runs to this runbook via `semantic_document_id`.

Focus Mode MUST NOT:

- claim a run is idempotent without an IK + dedupe/merge evidence,
- invent governance approvals,
- fabricate lineage links or policy outcomes.

## 🧪 Validation & CI/CD

### Decision Matrix (actionable defaults)

| Trigger kind | Typical use | Start condition | Retry policy (max / backoff) | Retry budget window | Idempotency key (IK) | Write strategy | Provenance & audit hooks | Notes / anti-patterns |
|---|---|---|---|---|---|---|---|---|
| **Cron (scheduled)** | Periodic ETL, ledger compaction, QA sweeps | Clock time (`0/15 * * * *`) | **6 attempts**, exponential **2^n** with **jitter**, base **30s**, cap **15m** | **6h** per run | `IK = {dataset_id, period, partition, code_sha}` | **Upsert+merge** with **content-addressed** artifacts; **stage → validate → promote** | Emit: `run.start`, `run.metrics`, `run.end`; PROV entity: input checksums, output URIs, code SHA; attach energy/carbon spans | Don’t align cron to flaky upstream drops; prefer **watermarks** over wall-clock |
| **Webhook (immediate)** | Human/agent action; small batch fixes | HTTP POST with signed context | **3 attempts**, **fixed 30s** then **2m**, then **5m** (jittered) | **30m** | `IK = {request_uuid}` (reject reuse) | **Transactional** change with **dry-run** option; require **preview diff** | Log full request envelope hash; PROV activity with actor & reason; store signature & policy checks | Never mutate without **request signature** and **policy gate** |
| **Upstream-Event** | New file/object/topic message | Objectstore/queue event | **8 attempts**, **exp 2^n** (base **15s**, cap **10m**), **DLQ** after | **24h** from first attempt | `IK = {source_uri OR message_id}` | **Exactly-once** via **dedupe ledger**; content-hash partitioning; **idempotent merges** | OpenLineage `event.ingest` with source ETag/MD5; store upstream watermark (ts/seqno) | If upstream is bursty, **coalesce** (e.g., 60s window) before fanout |

### Quick how-to (apply the defaults)

1. **Pick a trigger**
   - time-driven → **cron**
   - human/agent click → **webhook**
   - file/message arrival → **upstream-event**

2. **Set the idempotency key (IK)**
   - build IK from stable inputs (partition, source URI, message id, request UUID)
   - include `code_sha` when output correctness depends on code version

3. **Adopt the retry line**
   - use matrix values as default
   - add jitter to avoid coordinated retries

4. **Make writes idempotent**
   - object storage: write to `staging/` using content hashes; promote via a single atomic pointer update
   - DB/graph: upsert/merge keyed by business keys; track IK in a dedupe ledger
   - files: avoid overwrite-in-place; use versioned URIs

5. **Emit provenance**
   - on start/end (and on failure), emit PROV/OpenLineage with:
     - input checksums / upstream ETag/MD5
     - output URIs
     - code SHA
     - IK
     - policy gate results
     - energy/carbon spans (where required)

### CI expectations (documentation)

This runbook must remain compliant with:

- front-matter schema presence
- H1/H2 structure rules (approved H2 registry)
- footer governance links
- accessibility (heading order, list semantics)
- no secrets / no PII

## 📦 Data & Metadata

### A. Exponential backoff with jitter (pseudocode)

~~~python
import random
import time

def backoff_seconds(attempt_index: int, base_s: float, cap_s: float) -> float:
    # attempt_index starts at 0 for the first retry
    raw = base_s * (2 ** attempt_index)
    bounded = min(raw, cap_s)
    jitter = random.uniform(0.5, 1.5)
    return bounded * jitter

def retry_loop(run_once, max_attempts: int, base_s: float, cap_s: float):
    for i in range(max_attempts):
        try:
            return run_once()
        except Exception:
            if i == max_attempts - 1:
                raise
            time.sleep(backoff_seconds(i, base_s=base_s, cap_s=cap_s))
~~~

### B. Idempotency key (IK) materialization pattern

~~~text
IK rules:
- must be stable for “the same logical work”
- must change when output correctness changes (e.g., code_sha included)
- must be recorded in run logs + provenance
- must be enforced (dedupe ledger or uniqueness constraint)
~~~

Example IK fields (illustrative):

~~~text
cron IK:
  dataset_id + period + partition + code_sha

webhook IK:
  request_uuid (single-use; reject duplicates)

upstream-event IK:
  message_id OR source_uri + (etag/md5/version) + code_sha (when required)
~~~

## 🌐 STAC, DCAT & PROV Alignment

### DCAT
This runbook is a documentation dataset record candidate:

- `semantic_document_id` maps to `dct:identifier`
- the Markdown file is a `dcat:Distribution` (`mediaType: text/markdown`)

### STAC
This runbook may be represented as a non-spatial STAC Item:

- `geometry: null`
- `properties.datetime = last_updated`
- `assets.markdown.href` points to `docs/runbooks/reliability/trigger-retry-matrix.md`

### PROV-O / OpenLineage
For each job run (regardless of trigger), the run should be captured as:

- `prov:Activity` (or OpenLineage Run)
- `prov:Entity` inputs/outputs with checksums and stable URIs
- `prov:Agent` for the runner and any approving roles (when applicable)

This runbook is the plan/policy surface that can be referenced as a `prov:Plan` by activities.

## 🧱 Architecture

### Trigger wiring and idempotency boundary

- Triggers must not bypass the idempotency boundary.
- IK must be computed from the trigger payload/context and must be persisted before any side-effecting writes.

### Write strategies (canonical)

- **Content-addressed artifacts**
  - stage artifacts under deterministic paths keyed by content hash
  - promote via pointer swap / catalog update, not overwrite-in-place
- **DB/graph dedupe**
  - enforce unique keys for domain entities
  - store IK in a dedupe ledger (or a uniqueness constraint) to prevent double-apply
- **DLQ / quarantine**
  - upstream-event retries must land in DLQ/quarantine after the retry budget
  - DLQ must preserve enough context to replay deterministically (payload hash, source identifiers, code SHA)

## ⚖ FAIR+CARE & Governance

- This runbook is governed by the KFM governance, FAIR+CARE, and sovereignty standards referenced in the footer.
- Webhooks must require signature + policy gates before any mutation.
- Retry behavior must not amplify harm:
  - avoid retry storms that cause excessive upstream load
  - avoid logging sensitive payload details; store envelope hashes when needed
  - apply masking/generalization when work relates to sensitive locations or protected knowledge

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---:|---|---|
| **v11.2.6** | 2025-12-14 | `@kfm-reliability` | Initial KFM‑MDP v11.2.6 compliant trigger/retry decision matrix with idempotency and provenance defaults. |

<div align="center">

[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
