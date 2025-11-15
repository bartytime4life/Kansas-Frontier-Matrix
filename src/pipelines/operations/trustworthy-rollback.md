---
title: "🧵 Kansas Frontier Matrix — Trustworthy Rollback & STAC Reversion Playbook (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/operations/trustworthy-rollback.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-trustworthy-rollback-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧵 **Kansas Frontier Matrix — Trustworthy Rollback & STAC Reversion Playbook**  
`src/pipelines/operations/trustworthy-rollback.md`

**Purpose:**  
Define a **transactional, auditable, FAIR+CARE-aligned rollback model** for any publish touching STAC, Neo4j, tiles, indexes, or Focus Mode read models, with **zero broken links**, **no orphan derivatives**, and **full provenance**.

**Scope:**  
- STAC items, collections, and catalogs  
- Derived artifacts (tiles, rasters, vectors, tables)  
- Knowledge graph entities (Neo4j) and search indexes  
- Focus Mode read models, caches, and UI-facing materializations  

---

**Status:** `Diamond⁹ Ω / Crown∞Ω` · **Template:** `Platinum README v7.1` · **Protocol:** `KFM Markdown Output Protocol v10.3`  
**Aligned Standards:** `FAIR+CARE` · `ISO 19115` · `ISO 50001` · `ISO 14064` · `SBOM/SPDX` · `SLSA`  

</div>

---

## 🔍 At a Glance

This guide turns rollbacks into a **first-class, engineered operation**, not an emergency hack:

- Every publish is a **transaction** with a durable **write-ahead log (WAL)** and a **manifest**.  
- All downstream artifacts (tiles, indexes, Neo4j, Focus Mode caches) are **linked by lineage**, not guesswork.  
- Rollbacks operate on **links and versions**, not on fragile in-place overwrites.  
- FAIR+CARE checks are **re-run** during rollback, so we never “fail open” on sensitive data.  
- Every rollback produces its own **attestation**, **telemetry record**, and **governance trace**.

Use this document when you:

- Design new pipelines that must be **safely reversible**.  
- Implement STAC or Neo4j update jobs that can **roll forward and back**.  
- Diagnose rollbacks that created orphan artifacts or broke Focus Mode views.  
- Extend CI/CD workflows with **rollback simulations** and **SLO checks**.  

---

## 📁 Directory Layout

~~~~~text
src/
  pipelines/
    operations/
      trustworthy-rollback.md          # This playbook and architecture guide
      README.md                        # High-level ops overview (retry, rollback, hotfix)
      wal/                             # Write-ahead logs and helpers
        __init__.py
        models.py                      # WAL schemas and helpers
        storage.py                     # WAL storage abstraction (object store, DB)
      lineage/
        __init__.py
        model.py                       # Lineage graph entities and relations
        resolvers.py                   # Traverse lineage for rollback scope
      rollback/
        __init__.py
        engine.py                      # Orchestrates rollback phases
        stac_ops.py                    # STAC-specific link swaps and validations
        graph_ops.py                   # Neo4j and KG reversions
        search_ops.py                  # Search index version swaps
        cache_ops.py                   # Read-model and cache invalidation
        policy.py                      # FAIR+CARE and governance checks
      cli/
        kfm_rollback_cli.py            # Operator CLI entrypoints
      tests/
        test_wal_roundtrip.py
        test_lineage_traversal.py
        test_rollback_end_to_end.py
~~~~~

> **Note:** Concrete filenames are illustrative; align final paths and module names with `src/ARCHITECTURE.md` and `src/pipelines/geospatial/README.md` conventions.

---

## 🧠 Core Concepts

### 1. Publish Unit

The **publish unit** is the smallest entity we consider atomic for rollback:

- One or more STAC items and their parent collection updates  
- All derived artifacts directly created as part of that run  
- All read models, caches, and graph updates tied to that run  

Identified by a **`publish_id`** (globally unique) and described in a **WAL entry** and **manifest**.

### 2. Write-Ahead Transaction Log (WAL)

Every publish writes a single **append-only record** before any irreversible mutation:

- `publish_id`  
- `started_at`, `completed_at`, and status  
- `code_ref` (Git SHA, image digest, pipeline version)  
- `stac_items[]`, `stac_collections[]`, `asset_digests[]`  
- `derivatives[]` (tiles, rasters, tables, index segments, Neo4j subgraphs)  
- `policy_snapshot_ref` (FAIR+CARE state at publish time)  
- `sbom_ref`, `manifest_ref`  

The WAL is the **source of truth** for rollback scope. If it is incomplete, the publish must be treated as **unsafe to roll back** without manual intervention.

### 3. Lineage Graph

The **lineage graph** connects upstream sources to downstream artifacts:

- `SourceAsset` → `StacItem` → `DerivativeArtifact` → `ReadModel`

It enables:

- **Scope discovery**: find everything that depends on a given publish.  
- **Impact analysis**: show operators what will change before rollback.  
- **Integrity checks**: detect orphans and missing digests.  

The graph should be queryable from both:

- **Pipelines** (Python SDK or REST)  
- **Focus Mode** (explainability overlays and story nodes)  

### 4. Immutable Data, Mutable Links

Trustworthy rollback only works if **data is immutable** and **links are mutable**:

- Assets and derivative objects are **never overwritten**, only superseded.  
- STAC items, catalogs, and read models use **versioned links** or aliases.  
- Neo4j and indexes are managed via **versioned label sets** or **aliases**, not hard deletes.  

---

## 🧩 Data & Metadata Schemas

### WAL Record (Conceptual)

~~~~~yaml
publish_id: "pub_2025_11_14T03_15_42Z_kfm_daily_stac"
started_at: "2025-11-14T03:15:42Z"
completed_at: "2025-11-14T03:17:09Z"
status: "success" # success | partial_success | failed
code_ref:
  git_sha: "8f21b8a..."
  docker_image: "ghcr.io/kfm/pipelines:10.3.0"
  pipeline_name: "stac_daily_ingest"
stac_scope:
  items:
    - "kfm-stac:landsat:WRS2:029030:2025-11-13"
  collections:
    - "kfm-stac:landsat:WRS2"
assets:
  - logical_id: "kfm://assets/landsat/2025-11-13/029030/B04"
    digest: "sha256:..."
derivatives:
  - id: "tiles://landsat/daily/2025-11-13/029030"
    type: "tiles"
    version: "v2025_11_14T03_16_03Z"
    checksum: "sha256:..."
    depends_on:
      - "kfm-stac:landsat:WRS2:029030:2025-11-13"
  - id: "neo4j://node/basin_overlap/123456"
    type: "neo4j_subgraph"
    version: "v5"
    checksum: "sha256:..."
    depends_on:
      - "kfm-stac:landsat:WRS2:029030:2025-11-13"
policy_snapshot_ref: "governance://faircare/policies/landsat/2025-11-14T03_15_40Z"
sbom_ref: "releases/v10.3.0/sbom.spdx.json"
manifest_ref: "releases/v10.3.0/publishes/pub_2025_11_14T03_15_42Z.manifest.json"
telemetry_ref: "releases/v10.3.0/publishes/pub_2025_11_14T03_15_42Z.telemetry.json"
~~~~~

### Derivative Artifact Record (Conceptual)

~~~~~yaml
id: "tiles://landsat/daily/2025-11-13/029030"
type: "tiles" # tiles | raster | vector | table | index | neo4j_subgraph | cache
version: "v2025_11_14T03_16_03Z"
location: "s3://kfm/tiles/landsat/daily/2025-11-13/029030/v2025_11_14T03_16_03Z"
checksum: "sha256:..."
depends_on:
  - "kfm-stac:landsat:WRS2:029030:2025-11-13"
  - "kfm://assets/landsat/2025-11-13/029030/B04"
~~~~~

### Rollback Manifest (Conceptual)

~~~~~yaml
rollback_id: "rb_2025_11_14T06_22_01Z_pub_2025_11_14T03_15_42Z"
target_publish_id: "pub_2025_11_14T03_15_42Z_kfm_daily_stac"
requested_by: "ops:andrew.barta"
requested_at: "2025-11-14T06:21:50Z"
status: "completed" # planned | dry_run | completed | failed | cancelled
scope:
  stac_items:
    - "kfm-stac:landsat:WRS2:029030:2025-11-13"
  derivatives:
    - "tiles://landsat/daily/2025-11-13/029030"
diffs:
  - entity: "kfm-stac:landsat:WRS2:029030:2025-11-13"
    type: "stac_item_link"
    from_version: "v2025_11_14T03_15_42Z"
    to_version: "v2025_11_10T03_14_19Z"
attestations:
  - "attest://rollback/pipelines/stac_daily_ingest/2025-11-14T06_22_01Z"
policy_snapshot_ref: "governance://faircare/policies/landsat/2025-11-14T06_21_40Z"
telemetry_ref: "releases/v10.3.0/rollbacks/rb_2025_11_14T06_22_01Z.telemetry.json"
~~~~~

---

## 🔄 Rollback Execution Flow (Mermaid)

This is the **canonical, idempotent** rollback flow. Any implementation must conform to these phases.

~~~~~mermaid
flowchart TD
  RQ["Receive rollback request<br/>with target publish id"]
    --> VL["Validate publish id exists<br/>and WAL is complete"]
  VL -->|invalid or incomplete| AB["Abort<br/>require manual intervention"]
  VL -->|valid| SC["Resolve rollback scope<br/>via lineage graph"]
  SC --> DR["Dry run diff<br/>+ impact report"]
  DR --> PG["Run FAIR+CARE<br/>+ governance checks"]
  PG -->|fail| QL["Quarantine lane<br/>with masked variants"]
  PG -->|pass| EX["Execute rollback transaction"]
  EX --> LS["Swap links & aliases<br/>to previous versions"]
  LS --> RM["Rebuild read models<br/>and invalidate caches"]
  RM --> VC["Verify checksums<br/>and referential integrity"]
  VC -->|fail| RF["Rollback failed<br/>emit alerts and halt"]
  VC -->|pass| AT["Emit rollback manifest<br/>attestation and telemetry"]
~~~~~

**Key properties:**

- **Idempotent:** Running the same rollback twice is safe; no extra side-effects.  
- **Transactional:** If any post-condition fails, the pipeline must **fail closed** and not leave partial state.  
- **Observable:** Every step emits events to the telemetry pipeline referenced in front matter.  

---

## 🧭 Design Principles

1. **Rollback is a first-class operation**  
   Exposed via CLI, API, and Focus Mode internal controls (not just ad-hoc scripts).

2. **No manual edit-only rollbacks**  
   Every rollback must be traceable to a **rollback manifest** and **WAL entry**.

3. **Immutable content, mutable references**  
   Assets, tiles, and tables are never edited in place; only links and aliases move.

4. **Lineage-driven scope**  
   Scope is inferred from the lineage graph, not from wildcard path deletes.

5. **Policy re-evaluation**  
   FAIR+CARE rules and masking policies are re-run with current configuration.

6. **Graceful failure modes**  
   If rollback cannot fully restore state, it must:
   - Stop with a clear error  
   - Emit governance alerts  
   - Preserve forensic evidence (logs, manifests, metrics)

---

## 🚦 SLOs, Metrics, and Alerts

Use these **baseline SLOs** for trustworthy rollback operations:

| Metric                               | Target                        | Owner             | Notes                                       |
|--------------------------------------|-------------------------------|-------------------|---------------------------------------------|
| **Rollback MTTR** (p50)              | ≤ 10 minutes                  | Data Ops          | From request accepted to completed manifest |
| **Rollback MTTR** (p95)              | ≤ 30 minutes                  | Data Ops          | Complex multi-domain publishes              |
| **Broken STAC links after rollback** | 0                             | Pipelines Eng     | Verified by link checker                    |
| **Orphan derivative rate**           | 0 per rollback                | Pipelines Eng     | Orphans detected by lineage audit           |
| **Policy recheck latency**           | ≤ 2 minutes                   | FAIR+CARE Council | From rollback request to policy decision    |
| **Rollback job failure rate**        | < 1% per quarter              | Platform Eng      | Excludes intentional policy aborts          |
| **Telemetry completeness**           | 100% rollbacks with telemetry | Platform Eng      | Telemetry record must be present and valid  |

**Alerting suggestions:**

- **Critical:**
  - Broken STAC links > 0 after rollback  
  - Rollback job fails post-link swap  
  - Policy evaluation cannot be executed (missing engine, config)  

- **Warning:**
  - Orphan derivatives detected  
  - Rollback MTTR p95 breached for the last N rollbacks  
  - Telemetry record missing or invalid schema  

---

## 🧪 CI/CD Integration & Checks

### Required CI Jobs for Rollback-Capable Pipelines

1. **Schema checks**  
   Validate WAL, lineage, and rollback manifest JSON Schemas.

2. **Deterministic dry-run tests**  
   For synthetic publishes:
   - Write WAL  
   - Build lineage  
   - Run rollback **dry run** only  
   - Assert:
     - Scope discovery is deterministic  
     - No forbidden entities appear (e.g., external IDs not in lineage)

3. **End-to-end simulation**  
   In an ephemeral environment:
   - Run a sample publish  
   - Run full rollback  
   - Validate:
     - Checksums restored to previous values  
     - STAC links, Neo4j edges, and indexes consistent  

4. **Governance hooks**  
   Enforce:
   - No rollback to a publish that failed FAIR+CARE validation originally  
   - No rollback that bypasses current masking policies without explicit override  

5. **Telemetry contract tests**  
   Ensure rollback jobs:
   - Emit telemetry matching `pipelines-trustworthy-rollback-v1.json`  
   - Include `rollback_id`, `target_publish_id`, status, duration, and error summary  

---

## 🛠️ Implementation Notes & Interfaces

### 1. WAL Interface (Python Sketch)

~~~~~python
class WalStorage:
    def append(self, record: "WalRecord") -> None:
        ...

    def get(self, publish_id: str) -> "WalRecord":
        ...

    def list_for_entity(self, entity_id: str) -> list["WalRecord"]:
        ...
~~~~~

- Backed by object storage (parquet, JSON) or a small DB table.  
- Must support **idempotent append** based on `publish_id`.  

### 2. Lineage Resolver

~~~~~python
class LineageResolver:
    def scope_for_publish(self, publish_id: str) -> "RollbackScope":
        ...

class RollbackScope(NamedTuple):
    stac_items: list[str]
    collections: list[str]
    derivatives: list["DerivativeRef"]
    read_models: list["ReadModelRef"]
~~~~~

- May read from:
  - Neo4j lineage graph  
  - Parquet lineage tables  
  - Combined materialized views  

### 3. Rollback Engine

~~~~~python
class RollbackEngine:
    def dry_run(self, publish_id: str) -> "RollbackPlan":
        ...

    def execute(self, publish_id: str) -> "RollbackResult":
        ...
~~~~~

Responsibilities:

- Acquire **global or scoped lock** for the target entities.  
- Invoke domain-specific ops:
  - `stac_ops.swap_links`  
  - `graph_ops.revert_subgraph`  
  - `search_ops.swap_aliases`  
  - `cache_ops.invalidate_and_rebuild`  
- Run **policy checks** before applying changes.  

### 4. CLI Entrypoint

Example user-facing CLI:

~~~~~bash
kfm rollback plan --publish-id pub_2025_11_14T03_15_42Z
kfm rollback execute --publish-id pub_2025_11_14T03_15_42Z --reason "bad cloud mask"
kfm rollback status --rollback-id rb_2025_11_14T06_22_01Z
~~~~~

- `plan`: dry run, prints diff and risk assessment.  
- `execute`: performs rollback with appropriate safety prompts.  
- `status`: queries telemetry and manifests.  

---

## 🧷 Governance, FAIR+CARE, and Risk Controls

Rollback has its own risks, especially for **sensitive heritage, ecological, or community-linked data**.

### Governance Rules

- Rollbacks touching any **heritage-related STAC collections** or **sensitive locations**:
  - Must log to the governance ledger (`ROOT-GOVERNANCE.md`).  
  - May require FAIR+CARE Council approval or post-hoc review.  

- All rollbacks:
  - Must record `requested_by`, `reason`, and `risk_level`.  
  - Must reference the **policy snapshot** used for decision-making.  

### FAIR+CARE Considerations

- **Findable:**  
  Previous versions must remain discoverable through lineage views, but **access-controlled** when necessary.

- **Accessible:**  
  Rollbacks must not silently hide data required for regulatory or community obligations; use **retired** or **superseded** states instead of hard deletes.

- **Interoperable:**  
  STAC and Neo4j representations of the same rollback must stay in sync; links in Focus Mode need to reflect rollback status.

- **Reusable:**  
  Rollback manifests, WAL entries, and telemetry must support future analysis (e.g., “Which publishes do we frequently roll back?”).

- **CARE:**  
  If a rollback removes newly added protections (e.g., masked locations), require explicit sign-off and possibly a **quarantine lane** variant instead of full revert.

---

## 📘 Examples & Playbooks

### Example 1 — Roll Back a Single STAC Publish

Scenario: A Landsat daily ingest used a bad cloud mask model and produced misleading maps.

1. Operator runs:

   ~~~~~bash
   kfm rollback plan \
     --publish-id pub_2025_11_14T03_15_42Z_kfm_daily_stac
   ~~~~~

2. Engine outputs:

   - A list of STAC items and collections affected.  
   - All tiles, index segments, and Focus Mode read models in scope.  
   - Policy assessment:
     - No heritage or community-sensitive overlays involved.  
     - No additional masking required.  

3. Operator reviews diff and executes:

   ~~~~~bash
   kfm rollback execute \
     --publish-id pub_2025_11_14T03_15_42Z_kfm_daily_stac \
     --reason "Bad cloud mask thresholds in model version v3_1"
   ~~~~~

4. Rollback engine:

   - Swaps STAC item links back to previous asset versions.  
   - Reverts Neo4j nodes and relationships linked to this publish.  
   - Swaps search index aliases and invalidates Focus Mode caches.  
   - Emits rollback manifest and telemetry.  

5. CI and telemetry:

   - Confirm broken link count is zero.  
   - Record rollback MTTR and scope.  

---

### Example 2 — Partial Publish With Orphans

Scenario: A composite eco-hydro pipeline published STAC and Neo4j changes successfully, but failed during index updates.

1. WAL shows `status: partial_success`.  

2. Rollback dry run detects:

   - Some derivatives present, some missing.  
   - Index artifacts expected by WAL are not found.  

3. Engine behavior:

   - Marks rollback as **high risk**.  
   - Requires explicit `--force` with additional governance justification.  
   - Suggests **forward fix** (re-run publish with corrected pipeline) instead of rollback.  

4. Governance:

   - FAIR+CARE Council may require investigation into missing artifacts.  
   - Root cause analysis should be linked to rollback manifest.  

---

## 🔗 Related Documents

- `docs/standards/kfm_markdown_output_protocol.md`  
- `docs/standards/markdown_rules.md`  
- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `src/ARCHITECTURE.md`  
- `src/pipelines/geospatial/README.md`  
- `docs/security/prompt-injection/README.md` (for AI-assisted rollback tooling and Focus Mode guardrails)  

---

## 📜 Version History

| Version  | Date       | Author             | Summary                                                                 |
|----------|------------|-------------------|-------------------------------------------------------------------------|
| v10.3.1 | 2025-11-14 | Platform Ops Team | Updated to KFM Markdown protocol; added telemetry field hints and clarified CI gates. |
| v10.3.0 | 2025-11-14 | System + You      | Initial trustworthy rollback playbook, WAL and lineage patterns, SLOs. |

