<!-- 📄 File: mcp/incidents/runbooks/graph-neo4j.md -->

# 🚨🧩 Graph / Neo4j Runbook (KFM)

![Runbook](https://img.shields.io/badge/runbook-incident%20response-blue)
![Service](https://img.shields.io/badge/service-graph--neo4j-6f42c1)
![Tier](https://img.shields.io/badge/tier-critical-red)
![Data Backbone](https://img.shields.io/badge/metadata-STAC%2FDCAT%2FPROV-0aa)

📁 **Repo path**
```text
📁 mcp/
  📁 incidents/
    📁 runbooks/
      📄 graph-neo4j.md ✅
```

> **According to a document from 2026-01-23**, KFM’s Neo4j knowledge graph is a cornerstone of the platform’s hybrid architecture (Neo4j + PostGIS + API + UI + Focus Mode), and it’s used for relationship/context queries (including AI-driven traversals). [oai_citation:0‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🔎 Quick navigation

- [🎯 Purpose & scope](#-purpose--scope)
- [🧠 Service overview](#-service-overview)
- [📌 KFM invariants (do-not-break rules)](#-kfm-invariants-do-not-break-rules)
- [🧯 First 5 minutes triage](#-first-5-minutes-triage)
- [🧬 Graph integrity health checks](#-graph-integrity-health-checks)
- [🛠️ Common incident playbooks](#️-common-incident-playbooks)
- [💾 Backup & recovery](#-backup--recovery)
- [✅ Validation & exit criteria](#-validation--exit-criteria)
- [📚 References](#-references)

---

## 🎯 Purpose & scope

This runbook covers **incident response** for the **Neo4j-backed KFM knowledge graph**, including:

- Outages (Neo4j unavailable / connection failures)
- Severe latency / timeouts impacting API, UI, and Focus Mode
- Data integrity failures (orphans, schema drift, constraint/index issues)
- Ingestion-sync issues (graph out of sync with STAC/DCAT/PROV and/or PostGIS)
- Backup failures and emergency restore / rollback paths

**Non-goals:** Designing new schemas/ontologies or implementing new ingest pipelines (those belong in architecture & data-intake docs; this runbook references them).

---

## 🧠 Service overview

### What Neo4j does in KFM
- Neo4j stores **semantic relationships and provenance links** across people, places, events, datasets, documents, story artifacts, etc., enabling complex relationship queries. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Focus Mode can translate user questions into **graph traversals** using ontology-aligned relationships (e.g., CIDOC-CRM, OWL-Time), then combine graph results with other retrieval steps (RAG-style). [oai_citation:4‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- KFM uses a **hybrid store** approach: **PostGIS for heavy geospatial compute** and **Neo4j for semantic context**, coordinated via the API layer. [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Dependency chain (blast radius)
```mermaid
flowchart LR
  A[Data Intake Pipelines] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Graph Build/Sync]
  B --> D[PostGIS Load]
  C --> E[API Layer (REST/GraphQL)]
  D --> E
  E --> F[UI (Map + Story + Focus)]
  E --> G[Focus Mode AI Retrieval]
```

If **Neo4j** is degraded:
- **GraphQL/graph endpoints** can fail or slow (and may cascade into UI/Focus Mode). [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Geospatial map tiles/data can still work if PostGIS is healthy, but semantic features degrade (dataset/story linking, provenance traversals, concept hubs).

---

## 📌 KFM invariants (do-not-break rules)

These are **KFM-specific safety rails** you must preserve during incident response:

### 1) “API is the boundary” (no UI direct Cypher)
KFM guidance explicitly emphasizes: **UI must never query the graph directly; all access via API** to ensure redaction/permission checks and to avoid unsafe arbitrary queries. [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

✅ **Implication:** During incidents, mitigations should prioritize:
- throttling/limiting in API/GraphQL resolvers (depth/page size),
- cache or query shaping in the API,
- read-only Neo4j access for diagnostics,
- never “hotfixing” UI to talk directly to Neo4j.

### 2) Evidence-first metadata backbone
STAC/DCAT/PROV are the metadata backbone; after preparing these, the next step is loading into Neo4j and PostGIS. [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

✅ **Implication:** When data integrity looks wrong, first ask:
- “Did catalog generation succeed?”
- “Did graph sync step run with the same catalog version?”
- “Are we looking at a stale graph?”

### 3) Graph schema stability + migrations required
Graph/ontology versioning guidance: labels/relationship types should stay backwards-compatible unless a deliberate migration is performed; schema/ontology changes require migration scripts and version history updates. [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

✅ **Implication:** In an incident, **do not** “quick rename labels” or change relationship types ad-hoc.

### 4) Automated policy gates + “fail closed”
KFM includes automated policy gates (schema validation, STAC/DCAT/PROV completeness, license presence, sensitivity classification, provenance completeness) and follows “fail closed”. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

✅ **Implication:** If graph is broken because bad data slipped in, treat that as a **gate failure** and fix the gate, not only the symptom.

### 5) Graph integrity health checks are first-class CI
KFM describes institutionalized Graph Integrity Health Checks, including: ingestion lag monitoring, hub detection (top-degree nodes), property schema drift checks, and backup verification—producing artifacts and escalating certain failures as high severity. [oai_citation:14‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:15‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

✅ **Implication:** If you’re in an incident and these checks aren’t available, that’s itself a reliability gap—capture it in the postmortem.

---

## 🧯 First 5 minutes triage

### Step 0 — Confirm blast radius
- ✅ Are API graph endpoints failing? (GraphQL endpoint / graph REST endpoints)
- ✅ Is Focus Mode failing to retrieve relationships/citations?
- ✅ Is map browsing still OK? (often PostGIS-driven)

> If Focus Mode is impacted: Neo4j failures can directly reduce multi-hop context and response quality. [oai_citation:16‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### Step 1 — Basic availability checks
- **Network/connectivity**
  - Can the API reach Neo4j (Bolt)?
  - If you have direct access: can you connect with `cypher-shell`?

- **Neo4j service health**
  - Is the process/container running?
  - Are there restarts/crash loops?
  - Check logs for OOM / “out of memory” / store corruption / index rebuild loops.

### Step 2 — Identify incident class
Pick the closest bucket:

- **A. Outage:** cannot connect / connection refused / authentication failures
- **B. Performance:** p95 latency spikes, timeouts, CPU pegged, GC pressure
- **C. Integrity:** missing nodes, broken links, orphans, schema drift, failed constraints/indexes
- **D. Sync:** catalog/postgis updated but graph is stale (or vice versa)
- **E. Security/Governance:** sensitive data exposed or redaction bypass

### Step 3 — Stabilize (reduce harm)
- Prefer **degraded mode** over “random restarts”:
  - Limit GraphQL depth / cap relationship expansions (GraphQL resolvers should guard expensive queries). [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
  - Enable caching for frequently requested lookups when safe (KFM expects caching/indices for responsiveness). [oai_citation:18‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- If there’s suspected integrity corruption: **freeze writes/sync** and switch to read-only triage.

---

## 🧬 Graph integrity health checks

These checks are referenced as an early warning system and are intended to be automated (e.g., scheduled CI). [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 🚦 Minimum “incident-time” integrity checklist
Run these *before* doing invasive fixes:

- [ ] Confirm database is writable only if intended (or switch to read-only for integrity triage)
- [ ] `SHOW CONSTRAINTS` and `SHOW INDEXES` → ensure no failed/offline items
- [ ] Validate “orphan” patterns (broken lineage links)
- [ ] Check ingestion lag (minutes since last graph update)
- [ ] Detect runaway “super-hub” nodes (top-degree nodes)
- [ ] Sample schema drift on critical node types (property type/presence)
- [ ] Confirm backups are valid (backup verification is high severity) [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> 📌 **Tip:** If you don’t know label/property names, start by discovering schema:
> - `CALL db.schema.nodeTypeProperties()`
> - `CALL db.schema.visualization()`

### 🧪 Suggested Cypher snippets (adapt labels/properties to your schema)

#### 1) Node/relationship counts (trend delta)
```cypher
MATCH (n) RETURN count(n) AS nodes;
MATCH ()-[r]->() RETURN count(r) AS rels;
```
> Health checks often compare deltas between runs (e.g., detect explosions). [oai_citation:22‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

#### 2) Constraints & index status
```cypher
SHOW CONSTRAINTS;
SHOW INDEXES;
```

#### 3) Orphan detection (examples)
```cypher
// STAC-like: Items without Dataset/Collection link (adapt relationship type)
MATCH (i:Item)
WHERE NOT (i)-[:PART_OF|:IN_COLLECTION]->(:Dataset)
RETURN count(i) AS orphan_items;

// PROV-like: Activity with no USED and no WAS_GENERATED_BY links (adapt)
MATCH (a:Activity)
WHERE NOT (a)-[:USED]->()
  AND NOT ()-[:WAS_GENERATED_BY]->(a)
RETURN count(a) AS orphan_activities;
```
> Orphan checks are explicitly called out (broken lineage links). [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

#### 4) Ingestion lag (recent activity timestamp)
```cypher
// Assumes a timestamp property like ingested_at or last_seen
MATCH (n)
WHERE exists(n.ingested_at)
RETURN max(n.ingested_at) AS last_ingested_at;
```
> Ingestion lag monitoring is called out as “real-time monitoring of pipeline currency.” [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

#### 5) Top-degree nodes (hub detection)
```cypher
MATCH (n)
RETURN labels(n) AS labels, n.id AS id, size((n)--()) AS degree
ORDER BY degree DESC
LIMIT 50;
```
> Hub detection: list top nodes by degree; catch unintended “super-hub” nodes. [oai_citation:25‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

#### 6) Property schema drift (sample check)
```cypher
// Example pattern from the health check description; adjust labels and properties
MATCH (s:Sensor)
WITH s
WHERE s.pm25 IS NULL OR NOT s.pm25 =~ '^-?\\d+(\\.\\d+)?$'
RETURN count(s) AS bad_pm25;
```
> Drift checks look for wrong types / missing critical properties; threshold triggers escalation. [oai_citation:26‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🛠️ Common incident playbooks

> Use these like LEGO blocks 🧱 — pick the playbook that matches the incident bucket you identified.

### A) 🚫 Neo4j unavailable (connection refused / auth failures)

**Symptoms**
- API returns 5xx on graph queries
- `cypher-shell` can’t connect
- Neo4j process/container down or flapping

**Immediate actions**
1. Check service state (systemd/docker/k8s depending on deploy)
2. Check disk space (Neo4j can fail on low disk)
3. Check logs for:
   - out-of-memory / GC thrash
   - store corruption
   - license/enterprise feature mismatch (if applicable)
4. If crash-looping: take a snapshot of logs + config before changes.

**Likely root causes**
- Resource exhaustion (disk/memory)
- Misconfig / credential rotation mismatch
- Corrupted store or failed upgrade/migration

**Fix**
- Restore service availability first (restart after removing root cause)
- If corruption suspected: skip “restart loops” and move to **Backup & Recovery** section.

---

### B) 🐢 Severe latency / timeouts (p95 spike)

**Symptoms**
- Focus Mode answers timing out or missing relationship context
- GraphQL query timeouts
- High CPU / heap pressure

**First response**
- Identify top queries:
  - `SHOW TRANSACTIONS;` / `SHOW QUERIES;` (version-dependent)
- Kill obvious runaway queries (carefully; document query signatures)
- Reduce expensive query patterns:
  - Limit GraphQL recursion depth / require pagination (KFM expects guardrails). [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- Confirm cache strategy / enable safe caching for hot paths (KFM expects caching for responsiveness). [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Root cause suspects**
- Missing/failed indexes (check `SHOW INDEXES`)
- Super-hub nodes from ingestion bug (run hub detection) [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Schema drift causing poor selectivity
- “N+1 traversals” due to resolver changes

**Stabilization**
- Temporarily disable/limit high-cost endpoints via API feature flags (if available)
- Prefer shifting heavy counting to PostGIS (KFM: heavy counting belongs in SQL/PostGIS). [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### C) 🧩 Data integrity failure (orphans, drift, broken lineage)

**Symptoms**
- Users can’t trace provenance or relationships appear broken
- Integrity checks fail (orphans, drift thresholds exceeded)
- Missing expected edges after ingestion

**Immediate actions**
1. Freeze sync (stop further graph updates) to prevent compounding
2. Run integrity checklist (constraints, orphans, drift)
3. Identify the first bad commit/pipeline run (catalog version or run_id)

**KFM-specific guidance**
- Graph content should be derived from the metadata backbone (STAC/DCAT/PROV), then loaded into Neo4j/PostGIS. [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Graph schema stability is contractual; changes require migrations. [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Fix options**
- **Rebuild/sync from known-good metadata** (preferred)
- **Rollback to prior graph snapshot** (see rollback patterns)
- Patch ingestion/ETL (then rebuild) if it’s a recurring producer bug

---

### D) 🔁 Graph out of sync with catalogs / PostGIS

**Symptoms**
- New dataset exists in DCAT/STAC/PROV but graph nodes missing
- Graph nodes exist but API cannot find distributions/metadata
- UI shows broken links

**Immediate actions**
- Verify pipeline ordering (catalogs must be correct before graph feed) [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Confirm the graph sync step ran using the same catalog version
- Check for “hand edited CSV” drift (graph CSV should be generated, not hand edited) [oai_citation:34‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Fix**
- Re-run graph sync job for the target dataset(s)
- If sync tooling is broken, revert to last known-good version and open an issue

---

### E) 🔒 Governance / sensitive data incident (redaction bypass)

**Symptoms**
- Sensitive location precision exposed
- User can retrieve restricted attributes

**Immediate actions**
1. Treat as P0 (security & trust impact)
2. Enforce **API boundary** (UI must not access graph directly) [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
3. Disable affected endpoints / tighten resolvers / apply hotfix rules in API layer
4. Audit the query paths (query auditing is a known defensive strategy) [oai_citation:36‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

**Design context**
- KFM describes sensitivity-aware handling including generalization of location precision for privacy. [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM’s broader governance goals include culturally-aware access controls and ethical stewardship patterns (e.g., Mukurtu / TK Labels concepts). [oai_citation:38‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 💾 Backup & recovery

> Backups are explicitly considered high-severity when failing: broken backups mean real data-loss risk. [oai_citation:39‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Backup verification (recommended)
- Run a backup dump and **test restore in an isolated container** (automation-friendly). [oai_citation:40‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Store artifacts (reports + metrics) in a timestamped directory; health checks expect this pattern. [oai_citation:41‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Restore decision tree
- If the issue is **corruption** → restore known-good
- If the issue is **bad ingest** → rollback/rebuild from prior metadata snapshot
- If the issue is **schema drift** → apply migration + rebuild (don’t hand-edit live)

### Rollback pattern (KFM-aligned)
KFM intake guidance describes generating graph CSVs under `data/graph/csv/` and using bulk import for rebuild/rollback flows, with stable IDs so a previous snapshot can be re-imported. [oai_citation:42‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:43‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## ✅ Validation & exit criteria

You can close the incident when:

- ✅ Neo4j is reachable and stable (no crash loops)
- ✅ API graph endpoints are healthy and within latency targets
- ✅ Integrity checks pass (or are below warning thresholds):
  - constraints/indexes healthy
  - orphans at baseline
  - no new super-hubs
  - schema drift below threshold
- ✅ Focus Mode can retrieve and cite sources again (traceability expectation) [oai_citation:44‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- ✅ Backups are verified valid (especially if restore occurred) [oai_citation:45‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Post-incident follow-ups (must-do)
- [ ] Create/Update issues if multiple health checks failed (automation suggests escalating via tracker) [oai_citation:46‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] If root cause was ingest: add/strengthen policy gates (fail closed) [oai_citation:47‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] If schema changes were involved: write migration + version notes [oai_citation:48‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 References

### Primary KFM design docs (used in this runbook)
- KFM AI System Overview (Neo4j + Focus Mode retrieval)  [oai_citation:49‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- KFM Data Intake – Technical & Design Guide (STAC/DCAT/PROV → Neo4j/PostGIS + API boundary)  [oai_citation:50‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- KFM Comprehensive Technical Documentation (GraphQL, Neo4j semantics)  [oai_citation:51‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM Architecture, Features, and Design (policy gates, reliability concepts)  [oai_citation:53‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- MARKDOWN_GUIDE_v13 subsystem contracts (graph schema stability, migrations)  [oai_citation:54‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Additional Project Ideas (Graph Integrity Health Checks, hub detection, drift, backup verification)  [oai_citation:55‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Supporting research pack (project files)
- 🌟 Latest Ideas & Future Proposals (bulk doc ingestion into graph, operational ideas)  [oai_citation:56‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- Innovative Concepts to Evolve KFM (governance, ethics patterns)  [oai_citation:57‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- Kansas-Frontier-Matrix Open-Source Mapping Hub Design (STAC-like approach & ingestion framing)  [oai_citation:58‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
- Data Mining Concepts & Applications (query auditing concepts)  [oai_citation:59‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
- AI Concepts & more (AI/graph background pack)  [oai_citation:60‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- Data Management – Theories/Architectures (data architecture background pack)  [oai_citation:61‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- Maps / GoogleMaps / VirtualWorlds / Geospatial WebGL (map tech background pack)  [oai_citation:62‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- Various programming languages & resources (engineering reference pack)  [oai_citation:63‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- KFM UI System Overview (UI context for graph-driven features)  [oai_citation:64‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
