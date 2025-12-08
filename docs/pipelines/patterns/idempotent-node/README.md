---
title: "🔁 KFM v11.2.4 — Idempotent ETL Node Pattern (WAL-Safe · Deterministic · Replay-Guaranteed)"
path: "docs/pipelines/patterns/idempotent-node/README.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Backward compatible with v11.0.x idempotent nodes"

status: "Active / Enforced"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/patterns-telemetry.json"
telemetry_schema: "schemas/telemetry/pattern-idempotent-etl-v3.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-compliant (auto-mask on for sensitive joins)"
sensitivity: "Mixed (upstream may include sensitive geospatial joins)"
classification: "Public / Internal (pipeline pattern)"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/pipelines/patterns/event-driven-deterministic-ingest.md@v11.2.4"
  - "docs/analyses/metadata/README.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:patterns:idempotent-node:readme:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "pattern-idempotent-node-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "multi-domain"
  applies_to:
    - "etl"
    - "stac"
    - "graph"
    - "provenance"
    - "telemetry"
    - "event-driven"
  impacted_modules:
    - "docs/pipelines/patterns"
    - "src/pipelines/*"
    - "data/raw/*"
    - "data/processed/*"
    - "data/stac/*"
    - "dist/provenance/*"
---

<div align="center">

# 🔁 **Idempotent ETL Node Pattern**  
### **WAL Replay · Content Hashing · Deterministic Upserts**  

`docs/pipelines/patterns/idempotent-node/README.md`

</div>

---

## 📁 Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 patterns/
        └── 📁 idempotent-node/
            📄 README.md                     # ← This file (pattern spec)
            📁 examples/
            │   📄 soil-profiles.md         # Example: soil ETL node using this pattern
            │   📄 atmo-window-node.md      # Example: atmospheric aggregation node
            └── 📁 design/
                📄 rationale.md             # Design notes, trade-offs, open questions

📁 src/
└── 📁 pipelines/
    └── 📁 patterns/
        └── 📁 idempotent_node/
            📄 compute_hash.py              # Canonical content-hash helper
            📄 wal.py                       # WAL append, query, replay helpers
            📄 checkpoint.py                # Checkpoint management utilities
            📄 transaction.py               # Idempotent upsert transaction wrapper
            📄 replay.py                    # WAL replay / recovery entrypoints
            📁 tests/
                📄 test_determinism.py      # CI determinism tests
                📄 test_wal_replay.py       # CI WAL/replay tests
                📄 test_idempotency.py      # CI idempotency & conflict tests
```

This pattern is intended as a **shared library** for all KFM ETL nodes, regardless of domain (soil, atmo, history, etc.).

---

## 🌐 Purpose

The **Idempotent ETL Node Pattern** defines a **deterministic, crash‑safe, idempotent ETL node** for the Kansas Frontier Matrix (KFM), guaranteeing:

- **Replay‑safe WAL (Write‑Ahead Logging)**  
- **Deterministic content hashing**  
- **Immutable landing‑zone ingestion**  
- **Idempotent upserts keyed by `content_hash`**  
- **Zero drift between reruns**  
- **Full lineage & FAIR+CARE compliance**

This is the **mandatory blueprint** for all ETL nodes that feed the:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → Tiles & Story Nodes → Focus Mode

spine of KFM.

---

## 🧱 High-Level Architecture

Conceptual node architecture:

```text
Immutable Landing (content-addressed)
        ↓
Deterministic Transform (e.g., DuckDB, PySpark)
        ↓
WAL Intent (PENDING → APPLIED | SKIPPED | FAILED)
        ↓
Transaction-Safe Upsert (e.g., Postgres / lakeFS / Neo4j)
        ↓
Checkpoint Update (node: last_applied_hash)
```

Each step must emit:

- **OpenLineage events** (RunEvent + IO metadata),  
- **PROV‑O entities/activities/agents**,  
- **Telemetry** (energy, CO₂e, cost, rows/bytes).

This pattern is typically embedded inside higher‑level patterns such as:

- `event-driven-deterministic-ingest.md`,  
- domain‑specific patterns (e.g., SDA async, NEXRAD watermarks).

---

## 🔐 Deterministic Content Hashing

A node MUST compute a stable `content_hash` over:

- Input manifests (paths/URIs, sizes, ETags/checksums),  
- Pipeline parameters / configuration snapshot,  
- Code fingerprint (Git commit SHA + lockfile hash, and optionally container image digest).

Example (Python):

```python
import hashlib
import json

def compute_content_hash(inputs, params, code_sha, lockfile_hash):
    """
    inputs: sequence of {uri, size, etag|checksum}
    params: dict of configuration parameters used by this node
    """
    norm_inputs = sorted(inputs, key=lambda x: x["uri"])
    blob = json.dumps(
        {
            "inputs": norm_inputs,
            "params": params,
            "code": {"sha": code_sha, "lockfile": lockfile_hash},
        },
        sort_keys=True,
    )
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()
```

Properties:

- **Stable**: same inputs + params + code → same `content_hash`.  
- **Comprehensive**: code or config changes force new hashes.  
- **Comparable**: allows quick detection of **no‑op runs** (unchanged content).

The `content_hash` is the **primary key** for idempotency in this pattern.

---

## 📜 WAL Schema (Append‑Only)

A minimal relational WAL for ETL nodes:

```sql
create table if not exists etl_wal (
  wal_id         bigserial primary key,
  run_id         uuid        not null,
  node           text        not null,
  step           text        not null,
  payload        jsonb       not null,
  content_hash   text        not null,
  status         text        not null check (status in ('PENDING','APPLIED','SKIPPED','FAILED')),
  started_at     timestamptz not null default now(),
  applied_at     timestamptz
);
```

Guidelines:

- **Append‑only**: no record deletions; only status transitions.  
- **Intent, not effect**: WAL expresses *intent* to apply a given transform/output.  
- **Payload**:
  - Encodes everything needed to re‑run the node deterministically:
    - Input manifests,  
    - Params,  
    - Code & config IDs,  
    - Optional domain context.

---

## 📘 Checkpoint Schema

Per‑node checkpoint:

```sql
create table if not exists etl_checkpoint (
  node             text primary key,
  last_applied_hash text        not null,
  updated_at       timestamptz  not null default now()
);
```

Purpose:

- Stores the **last successfully applied `content_hash`** per node.  
- Enables quick **skip** decisions, e.g., “nothing changed since last run”.

Typical sequence:

1. Compute `content_hash`.  
2. If `content_hash == last_applied_hash` → short‑circuit to SKIPPED.  
3. Otherwise, proceed with WAL + upsert.

---

## 🧱 Target Table Pattern

For a node writing to a relational target:

```sql
create table if not exists node_output (
  content_hash text primary key,
  record       jsonb not null,
  lineage      jsonb,
  valid_from   timestamptz,
  valid_to     timestamptz
);
```

Rules:

- Rows are **immutable**; new versions are added as new `content_hash` records.  
- `valid_from` / `valid_to` can represent temporal validity or supersession windows.  
- Graph integration typically maps:
  - `node_output.content_hash` → `:Artifact { content_hash }` nodes.

Other target backends (e.g., lakeFS, object stores, Neo4j) must implement **equivalent semantics**:

- Effects keyed by `content_hash`,  
- Writable in a single atomic operation per run,  
- Discoverable via PROV/lineage.

---

## 🔁 Idempotent Upsert Transaction (Relational Example)

Canonical flow:

1. Insert WAL **PENDING** record (intent).  
2. Check if `content_hash` is already **APPLIED**.  
3. If yes → mark WAL as **SKIPPED**, return.  
4. If no → apply transform effect in **one transaction**.  
5. Mark WAL as **APPLIED** and update checkpoint.

Example (Postgres‑style pseudo‑SQL):

```sql
begin;

-- 1. Idempotency gate: has this content_hash already been applied?
select 1
from etl_wal
where content_hash = :hash
  and status = 'APPLIED'
for update;

-- 2. If exists, application logic marks SKIPPED and short-circuits (not shown here).

-- 3. Upsert effect (simplified)
insert into node_output (content_hash, record, lineage, valid_from)
select :hash, record, lineage, now()
from duckdb_stage_view
on conflict (content_hash) do nothing;

-- 4. Mark WAL entry as APPLIED
update etl_wal
set status     = 'APPLIED',
    applied_at = now()
where wal_id = :wal_id;

-- 5. Update checkpoint
insert into etl_checkpoint (node, last_applied_hash)
values (:node, :hash)
on conflict (node) do update
  set last_applied_hash = excluded.last_applied_hash,
      updated_at        = now();

commit;
```

Implementations in `transaction.py` should:

- Wrap this logic in a robust function,  
- Handle SKIPPED/FAILED transitions cleanly,  
- Integrate telemetry and lineage recording.

---

## 🔄 WAL Replay Mode

Replay is where this pattern becomes critical.

In **replay mode**, a node:

1. Reads WAL entries (e.g., `status in ('PENDING','FAILED')`) for a given node/range.  
2. Reconstructs `payload` (inputs, params, code IDs).  
3. Re‑runs the deterministic transform (e.g., DuckDB query).  
4. Checks if `content_hash` is already **APPLIED**:
   - If yes → mark WAL as **SKIPPED** (or leave as APPLIED if already so).  
   - If no  → perform the upsert transaction as usual.

Replay must guarantee:

- **No double‑writes** (idempotency is enforced by `content_hash`).  
- **No lost intents** (all PENDING/FAILED entries are revisited until resolved).  
- **Deterministic outputs**:
  - Same inputs → same `content_hash` and same effect.

This protects against:

- Crashes and partial failures,  
- Mid‑run worker evacuation / scaling events,  
- Retrying after transient infra or upstream failures.

---

## 🧪 Determinism Requirements

A node **MUST**:

- Use **fixed random seeds** for any stochastic operations.  
- Avoid uncontrolled system clock usage in transforms:
  - Timestamps should come from run metadata, not inline `now()` calls.  
- Enforce **stable sort orders** and column ordering:
  - e.g., explicit `ORDER BY` and deterministic column lists.  
- Ensure SQL / DuckDB / Spark queries are structured for **byte‑identical outputs** when inputs are unchanged.  
- Record:
  - Code version (Git commit),  
  - Dependency lockfile hashes,  
  - Config snapshots.

CI must include:

- **Determinism tests**:
  - Run the node twice with the same fixture inputs → exactly identical outputs and `content_hash`.  
- **Replay tests**:
  - Simulate partial failures, then WAL replay → final state identical to the “clean” run.

Violations (e.g., drift across reruns) are **ship‑blocking** failures for production KFM nodes.

---

## 🧭 Governance & FAIR+CARE Compliance

This pattern is *required* for:

- All new ETL nodes entering KFM’s canonical data backbone.  
- All ingestion pipelines touching:
  - Archaeology, ecology, climate, cultural heritage, sensitive hydrology, or other CARE‑governed domains.  
- All modules emitting STAC Items that appear in:
  - Focus Mode,  
  - Public dashboards,  
  - Policy‑facing reports.

CARE implications:

- When inputs include **sensitive geospatial joins** (e.g., Tribal lands, sacred sites, endangered species habitats):
  - Apply masking / generalization (e.g., H3 coarsening, donut masking) **before** content hashing when the precise geometry cannot be exposed.  
  - Record masking decisions in PROV and audit logs.  
- Ensure that `content_hash` does not indirectly leak sensitive details when referencing restricted artifacts; use **masked URIs or grouped identifiers** when required.

All idempotent ETL node designs and implementations are subject to:

- Root governance (`docs/standards/governance/ROOT-GOVERNANCE.md`),  
- FAIR+CARE Data Governance Council review,  
- Lineage and audit checks (OpenLineage + PROV‑O),  
- Telemetry requirements (pattern‑level telemetry schema).

---

## 🔍 Relationship to Other Patterns

This pattern is a **building block** used by:

- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`  
- Domain patterns:
  - Soil (SDA async / weekly),  
  - Atmospheric (NEXRAD watermarks, HRRR aggregations),  
  - Historical and land‑use aggregation nodes.

Rules:

- Event‑driven patterns rely on idempotent node semantics for each processing step.  
- Story Node & Focus Mode correctness depends on:
  - Nodes not double‑writing,  
  - Replays not changing outputs unexpectedly,  
  - Hash‑stable versions for dataset nodes in the graph.

---

## 🧭 Version History

| Version | Date       | Author / Steward           | Summary                                                                 |
|---------|------------|---------------------------|-------------------------------------------------------------------------|
| v11.2.4 | 2025-12-07 | Reliability Engineering   | KFM-MDP v11.2.4 alignment; clarified WAL schema, determinism rules, and replay behavior. |
| v11.2.3 | 2025-11-30 | Reliability Engineering   | Reliability upgrades and lineage normalization; added checkpoint examples. |
| v11.1.x | 2025-09-15 | KFM Data Platform Team    | Initial stable release of idempotent ETL node pattern.                  |

---

<div align="center">

**Kansas Frontier Matrix (KFM v11)**  
Deterministic · Reproducible · Governed · FAIR+CARE Aligned  

[⚖️ Root Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[📊 Pattern Telemetry](../../../../releases/v11.2.4/patterns-telemetry.json) ·  
[📐 Telemetry Schema](../../../../schemas/telemetry/pattern-idempotent-etl-v3.json)

</div>