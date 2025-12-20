---
title: "🛰️ KFM — Operational Signals, Trigger Rules, QC Gates, and Provenance Attachments for Ingest Watchers"
path: "docs/data-ops/ingest-watchers/OPERATIONAL_SIGNALS_AND_GATES.md"
version: "v0.1"
last_updated: "2025-12-20"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Data-Ops & FAIR+CARE Council"
content_stability: "stable"
status: "Active / Canonical"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-ingest-watchers-operational-signals"

license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v1.0"
dcat_profile: "KFM-DCAT v1.0"
prov_profile: "KFM-PROV v1.0"
telemetry_schema: "KFM-TEL v1.2"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data-ops:ingest-watchers:operational-signals-and-gates:v11.2.6"
semantic_document_id: "kfm-ingest-watchers-operational-signals-v11.2.6"
event_source_id: "ledger:kfm:doc:data-ops:ingest-watchers:operational-signals-and-gates:v11.2.6"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 🛰️ KFM — Operational Signals, Trigger Rules, QC Gates, and Provenance Attachments for Ingest Watchers

## 📘 Overview

### Purpose
This standard defines **what an ingest watcher should observe**, **how it should decide**, and **what it must attach** so every data acceptance/rejection/quarantine event is measurable (telemetry), enforceable (QC gates + contracts), explainable (signals + rules), and reproducible (PROV lineage + immutable artifacts).

### Scope

| In Scope | Out of Scope |
|---|---|
| Signal taxonomy, gate stack, trigger rules, reason codes, provenance bundle requirements | Domain-specific scientific methods beyond “plausibility/validity bounds” (document those in domain standards) |
| Deterministic replay expectations and artifact routing | Provider-specific credentials/secrets; runtime infrastructure implementation details |
| STAC/DCAT/PROV + telemetry expectations for watcher decisions | UI rendering rules beyond provenance-linked requirements |

### Audience
- Primary: Data-Ops engineers, pipeline maintainers, ingestion/validation developers
- Secondary: Governance reviewers (FAIR+CARE), security reviewers (as applicable), dataset owners

### Definitions (link to glossary)
- Glossary: `docs/glossary.md` (if present in repo)
- Core terms used here (normative): **Signal**, **Gate**, **Trigger**, **Outcome**, **Reason Code** (defined below in the Operational Specification)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This doc | `docs/data-ops/ingest-watchers/OPERATIONAL_SIGNALS_AND_GATES.md` | Data-Ops | Canonical watcher rules + attachments |
| PROV bundle (per run) | `prov/run.jsonld` + `prov/summary.json` | Watcher | Minimum viable lineage |
| Validation artifacts | `quality/expectations.json`, `quality/validation_result.json`, `quality/metrics.json` | Watcher | Gate evidence |
| Catalog artifacts | STAC Items/Collections + DCAT Dataset/Distribution updates | Catalog stage | Publish-only unless policy says otherwise |
| Telemetry | KFM-TEL signals + logs/traces | Watcher | Gate decisions + reason codes |

### Definition of done (for this document)
- [ ] Front-matter complete + `path` matches filesystem
- [ ] Operational Specification preserved (signals, gates, triggers, provenance attachments, reason codes)
- [ ] Determinism expectations stated (idempotency key + replay)
- [ ] STAC/DCAT/PROV + telemetry obligations specified
- [ ] Validation & CI steps listed

---

## 🗂️ Directory Layout

### This document
- `docs/data-ops/ingest-watchers/OPERATIONAL_SIGNALS_AND_GATES.md`

### Related repository paths (by KFM pipeline stage)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs by domain |
| Catalogs | `data/stac/` · `data/catalog/dcat/` | STAC + DCAT outputs |
| Provenance | `data/prov/` | PROV bundles (run-level + aggregates) |
| Pipelines | `src/pipelines/` | ETL + catalog build |
| Graph | `src/graph/` | Graph build/migrations (API boundary preserved) |
| APIs | `src/server/` | Contracted access layer |
| Telemetry | `docs/telemetry/` · `schemas/telemetry/` | Observability contracts + schemas |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 data-ops/
    └── 📁 ingest-watchers/
        └── 📄 OPERATIONAL_SIGNALS_AND_GATES.md
~~~

---

## 🧭 Context

### Background
KFM’s canonical pipeline ordering is preserved:
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

“Ingest watchers” live in the control-plane around ETL/cataloging: they detect upstream change/arrival, normalize/fetch, evaluate signals and gates, and then route to publish/quarantine while emitting provenance and telemetry.

### Assumptions
- Watchers run as a lightweight loop or event-driven function.
- Inputs may be late, revised, silently backfilled, or schema-drifting.
- Determinism is required: the same inputs/config produce the same outputs.

### Constraints / invariants
- Frontend consumes data via APIs (no direct graph dependency).
- Publish is only allowed after passing required QC gates and producing a provenance bundle.
- Sensitive location inference is prohibited; watchers must not “enhance” restricted location detail.

---

## 🗺️ Diagrams

### Watcher decision flow
~~~mermaid
flowchart LR
  T[Trigger: poll/event/hybrid] --> F[Fetch + normalize]
  F --> S[Measure signals]
  S --> G[Evaluate QC gates 0..7]
  G -->|PASS| P[Publish processed + catalogs]
  G -->|HOLD| R[Retry loop]
  G -->|SOFT FAIL| Q[Quarantine + diagnostics]
  G -->|DROP| D[Ignore]
  P --> A[Emit PROV + telemetry]
  Q --> A
  R --> A
  D --> A
~~~

### Catalog + provenance attachment expectations
~~~mermaid
flowchart LR
  Raw[Raw artifacts] --> Act[Watcher activity: fetch/parse/validate]
  Act --> Proc[Processed artifacts]
  Act --> Rep[Validation reports]
  Act --> Prov[PROV bundle]
  Proc --> Stac[STAC Item/Collection updates]
  Proc --> Dcat[DCAT Dataset/Distribution updates]
  Prov --> Audit[Audit/telemetry signals]
  Rep --> Audit
~~~

---

## 📎 Operational Specification (Normative)

> The sections below are normative for ingest watcher behavior and MUST be implemented or explicitly waived by a governed domain override.

## 🎯 Purpose

This document defines **what an ingest watcher should observe**, **how it should decide**, and **what it must attach** so every data acceptance/rejection/quarantine event is:
- measurable (telemetry),
- enforceable (QC gates + contracts),
- explainable (signals + rules),
- and reproducible (PROV lineage + immutable artifacts).

In KFM, an “ingest watcher” is a lightweight control-plane loop (or event-driven function) that:
1) detects change or arrival,
2) fetches/normalizes,
3) evaluates signals + gates,
4) routes to **publish** or **quarantine**,
5) emits **PROV + STAC/DCAT updates + telemetry**.

---

## 🧩 Core Concepts

### 1) Signal vs Gate vs Trigger
- **Signal**: a measured indicator (numeric, boolean, categorical) describing data, system state, or upstream conditions.
- **Gate**: a hard decision boundary (PASS / FAIL / QUARANTINE / HOLD) evaluated from one or more signals.
- **Trigger**: what causes evaluation (schedule, webhook, file arrival, API “lastUpdated”, checksum delta, upstream revision notice).

### 2) Outcomes
- **PASS → Publish** (write processed outputs, publish STAC Item/Collection updates, refresh DCAT dataset, emit PROV)
- **SOFT FAIL → Quarantine** (store raw + diagnostics, attach reason codes, open workflow issue/alert)
- **HOLD → Retry** (upstream incomplete / forecast cycle not done / rate-limit)
- **DROP → Ignore** (duplicate, known bad revision, non-authoritative mirror)

---

## 🧠 Signal Taxonomy (What to Measure)

### A) Change & Revision Signals
These prevent “silent updates” from corrupting downstream truth.

1. **Revision Marker**
- Detect upstream flags: `status=preliminary/final`, `revision_id`, `last_modified`, `etag`, `generationTime`, “processing_level”.
- If the same time interval is re-issued, treat as new revision, not duplicate.

2. **Schema Revision / Contract Drift**
- Field added/removed, type changed, enum expanded, unit changed.
- Parse headers, JSON schema, CSV columns, NetCDF vars, GeoTIFF tags, STAC extensions.

3. **Content Hash Delta**
- Stable hashing: whole-file SHA256, chunked hashes for large objects, row-group hashes for parquet.
- Hash delta without revision marker = suspicious (possible silent backfill).

4. **Backfill Window Growth**
- “New data” includes historical windows beyond policy, e.g., upstream reprocessing for last 90 days.
- Track: `min_time_changed`, `max_time_changed`, and percentage changed.

**Recommended fields:**
- `kfm.signal.revision.kind` = {upstream_flag, etag, hash_delta, backfill_detected}
- `kfm.signal.revision.severity` = {info, warn, critical}

---

### B) Completeness & Timeliness Signals
1. **Timeliness Lag**
- `lag = now - expected_arrival_time`
- Distinguish: upstream delayed vs ingestion stalled.

2. **Coverage / Expected Count**
- For sensors: expected N observations per interval.
- For tiles/grids: expected scene count, expected band list.

3. **Null Density / Missingness**
- Overall and per critical field (e.g., timestamp, geometry, pm25, discharge_cfs).

4. **Forecast Cycle Completion**
- Only publish when all required cycle members exist (e.g., `t00z` + all lead times).
- Track: partial cycle vs complete cycle.

---

### C) Validity & Conformance Signals
1. **Type & Range Validity**
- Date parseable, coords numeric, values in physical plausibility bounds.

2. **Unit & CRS / Datum Validity**
- Units present and recognized, CRS declared, vertical datum known or resolvable.

3. **Semantic Validity**
- Controlled vocabulary checks (station type codes, method codes, qualifier flags).

4. **Geospatial Validity**
- Geometry is valid, within Kansas AOI bounds (or expected domain), no self-intersections.

---

### D) Consistency & Integrity Signals
1. **Primary Key / Natural Key Uniqueness**
- No duplicates for `(station_id, timestamp)` or `(scene_id)`.

2. **Referential Integrity**
- Observation references a known station; station references known provider; asset references known collection.

3. **Time Monotonicity**
- Timestamps non-decreasing per source stream; detect resets.

4. **Cross-field Consistency**
- Example: wind direction only valid when wind speed > 0 (domain-specific).

---

### E) Statistical & Anomaly Signals (Data “Behavior”)
1. **Distribution Shift**
- PSI, KL divergence, Wasserstein distance, z-score of feature moments vs baseline.
- Use rolling baselines (7d/30d) and seasonal baselines (same month last year).

2. **Spike / Dropout / Flatline**
- Flatline: variance ~ 0 for too long.
- Dropout: missing bursts.

3. **Outlier Density**
- fraction of points outside robust bounds (MAD-based, quantile fences).

4. **Neighbor Consensus**
- Compare station to nearby stations or grid cell climatology.
- Flag if persistent deviation beyond expected microclimate envelope.

---

### F) Identity & Churn Signals (Sensors, Stations, Providers)
1. **Relocation / Coordinate Jump**
- Sudden lat/lon change beyond threshold.
- Coupled with metadata changes (address, site name) increases confidence.

2. **Device Reset / Firmware Change**
- Repeated timestamp resets, new serial number, changed reporting cadence, changed precision.

3. **Dedup / Merge Candidate**
- Two “different” stations with near-identical time series + close geometry.

---

### G) Reliability & System Health Signals
1. **Fetcher Error Rate**
- HTTP 429/5xx, timeout frequency.

2. **Upstream SLA Breach**
- consecutive late cycles.

3. **Data Corruption Indicators**
- truncation, invalid gzip, parquet footer errors.

4. **Cost / Resource Spikes**
- unexpectedly large payload sizes, memory blowups.

---

## 🧱 QC Gates (Hard Decisions)

Below is a common gate stack that works across domains (air, hydro, geology rasters, catalogs).

### Gate 0 — Trigger Eligibility
**Goal:** only run when meaningful.
- PASS if: new revision marker OR hash delta OR new time window.
- DROP if: duplicate event (idempotency key hit).

**Idempotency key** example:
`kfm_idem = sha256(source_id + collection_id + revision_id + time_window + fetch_params)`

---

### Gate 1 — Contract & Schema Gate
**FAIL (Quarantine)** if any:
- missing required fields,
- type changes violating contract,
- unit changes without explicit revision event,
- CRS missing/invalid.

Outputs:
- `contract_diff.json`
- `schema_snapshot.json`
- `gate_1_report.json`

---

### Gate 2 — Structural Integrity Gate
**FAIL (Quarantine)** if:
- invalid file structure,
- checksum mismatch,
- cannot parse essential formats.

Outputs:
- parsing logs
- checksum report
- minimal sample extraction

---

### Gate 3 — Domain Validity Gate
**FAIL (Quarantine)** for hard physical impossibility.
Examples:
- negative precipitation,
- PM2.5 < 0 or absurdly high beyond instrument range (unless flagged exceptional + supported),
- discharge negative where not physically meaningful,
- geometry outside valid bounds for the dataset’s stated domain.

---

### Gate 4 — Completeness & Timeliness Gate
**HOLD (Retry)** if:
- forecast cycle incomplete,
- expected batch member missing,
- upstream still “preliminary” when policy demands “final”.

**SOFT FAIL (Quarantine)** if:
- persistent missingness beyond tolerance,
- too few observations in a publishing window.

---

### Gate 5 — Consistency & Dedup Gate
**SOFT FAIL (Quarantine)** if:
- duplicates exceed threshold,
- key collisions,
- referential integrity breaks.

**PASS with annotation** if:
- duplicates are expected and deterministically resolved (document rule).

---

### Gate 6 — Behavioral / Statistical Gate
**SOFT FAIL** if:
- distribution shift above threshold,
- flatline/spike patterns indicative of sensor fault,
- neighbor-consensus persistent deviations.

**PASS with flag** if:
- anomalies are plausible events and corroborated (e.g., wildfire smoke episode validated by multiple stations).

---

### Gate 7 — Publish Gate (Promotion Saga)
Only **publish** if:
- all required gates pass,
- provenance bundle created,
- STAC/DCAT updates are consistent,
- telemetry emitted,
- signatures/attestations ready (if enabled).

---

## 🧷 Trigger Rules (When to Run What)

### 1) Polling Triggers
- **Interval polling**: every 5–15 min for realtime sensors; hourly/daily for batch.
- Conditional: increase frequency during known event windows.

### 2) Event Triggers
- Object store event (new file).
- Webhook from provider (new revision).
- Message bus (forecast cycle ready).

### 3) Hybrid Trigger Pattern
- Event triggers ingestion attempt.
- Polling verifies completeness and catches missed events.

---

## 🔍 Concrete Signal → Gate Rule Examples

### Example A — “Revision Marker”
**Signals**
- `etag_changed = true`
- `last_modified_changed = true`
- `hash_changed = true`

**Rules**
- If `hash_changed=true` AND `etag_changed=false` → `Gate 0 = PASS`, but `Gate 1` gets “silent change” warning.
- If `revision_id` decreased or repeats with different hash → quarantine with reason `REVISION_INCONSISTENT`.

---

### Example B — “Sensor Churn / Firmware”
**Signals**
- `cadence_change_ratio > 2.0`
- `precision_digits_changed = true`
- `timestamp_resets_detected = true`

**Rules**
- If ≥2 signals true within 24h → `Gate 6 = SOFT FAIL` and create “sensor state transition” annotation.
- If timestamp resets persist → `Gate 3 = FAIL` (invalid time semantics).

---

### Example C — “Forecast Cycle Completion”
**Signals**
- `cycle_members_expected = 49`
- `cycle_members_present = 47`
- `cycle_age_minutes = 18`

**Rules**
- If `present < expected` AND `cycle_age < grace_period` → `HOLD`.
- If `present < expected` AND `cycle_age >= grace_period` → quarantine `INCOMPLETE_CYCLE`.

---

### Example D — “Neighbor Consensus”
**Signals**
- `deviation_sigma = 4.5`
- `neighbors_corrob = false`
- `duration_hours = 6`

**Rules**
- If `deviation_sigma > 4` AND `duration_hours > 3` AND `neighbors_corrob=false` → quarantine as likely sensor fault.
- If neighbors corroborate → pass with “event plausible” flag.

---

## 🧾 Provenance Attachments (What Must Be Emitted)

### 1) PROV Bundle (Minimum Viable Lineage)
Every ingest attempt produces a PROV graph with:
- **Entity**: raw artifact(s), normalized table(s), derived products (rasters, parquet, geojson), validation reports
- **Activity**: fetch, parse, normalize, validate, publish
- **Agent**: watcher service identity, CI runner, human approver (if any)

Minimum relations:
- `wasGeneratedBy` (product ← activity)
- `used` (activity → inputs)
- `wasAssociatedWith` (activity ↔ agent)
- `wasDerivedFrom` (product ← input)
- `hadPlan` (activity ↔ pipeline config snapshot)

Persist as:
- `prov/run.jsonld` (or `prov/run.ttl`)
- `prov/summary.json` (human-friendly digest)

---

### 2) Validation Artifacts
For each run:
- `quality/expectations.json` (rules)
- `quality/validation_result.json` (results per expectation)
- `quality/metrics.json` (profiles: null rate, duplicates, drift stats)

---

### 3) Catalog Artifacts (STAC + DCAT)
- Update/create **STAC Item** for each asset and **STAC Collection** for grouping.
- Update **DCAT Dataset** and **Distribution** entries for discovery and governance.

---

### 4) Telemetry Artifacts
Emit consistent metrics/logs/traces for:
- run duration, bytes processed, rows/records, error classes
- gate decisions and reason codes
- drift scores, missingness, duplicates
- upstream SLA lag

---

### 5) Attestations & Integrity (Optional but Recommended)
- Produce signed build/proc provenance for artifacts (software + data processing), and attach signatures to release bundles.

---

## 🧱 Reason Codes (Standardize Your Decisions)

Define an enum used across gates, logs, and PROV annotations:

- `DUPLICATE_EVENT`
- `SCHEMA_BREAKING_CHANGE`
- `SCHEMA_NONBREAKING_CHANGE`
- `UNIT_CHANGE_UNANNOUNCED`
- `CRS_MISSING_OR_INVALID`
- `CHECKSUM_MISMATCH`
- `PARSE_ERROR`
- `PHYSICAL_IMPOSSIBILITY`
- `MISSINGNESS_EXCEEDED`
- `INCOMPLETE_CYCLE`
- `KEY_COLLISION`
- `REFERENTIAL_INTEGRITY_FAIL`
- `DISTRIBUTION_SHIFT_HIGH`
- `FLATLINE_DETECTED`
- `RELOCATION_SUSPECTED`
- `UPSTREAM_RATE_LIMIT`
- `UPSTREAM_OUTAGE`

Each reason code should have:
- severity: {info,warn,critical}
- default action: {pass,pass_with_flag,hold,quarantine,drop}
- remediation playbook pointer

---

## 🧪 Implementation Patterns (Battle-Tested)

### Pattern 1 — “Two-Track Storage”
- Always persist **raw** (immutable).
- Persist **processed** only if publish gate passes.
- Persist **quarantine** with full diagnostics and replay metadata.

### Pattern 2 — “Deterministic Replay”
- Persist config snapshot + seed + dependency versions + input hashes.
- A replay must reproduce outputs bitwise if upstream inputs unchanged.

### Pattern 3 — “Soft Fail with Annotations”
Not every anomaly should block publication. Use:
- `pass_with_flag` when corroborated by context, neighbors, or external signals.
- Record the flag in STAC `properties` and DCAT `dcterms:conformsTo` / notes.

### Pattern 4 — “Budgeted Verification”
Run cheap checks always; expensive checks conditionally:
- Always: schema, parse, checksum, basic ranges.
- Conditional: drift/neighbor checks when volume threshold met or on daily rollups.

---

## 📦 Minimal Contract Template for a Watcher

A watcher contract should specify:
- data producer + endpoint(s)
- cadence + expected arrival
- schema + units + CRS
- required fields
- gate thresholds (missingness, duplicates, drift)
- quarantine routing + TTL + escalation
- publish rules (preliminary vs final)
- provenance requirements (what to attach)
- catalog requirements (STAC/DCAT mapping)

---

## 🗺️ Domain Notes (Quick Mappings)

### Air Quality (PM2.5 sensors)
High-value signals:
- flatline/spike, cadence shifts, relocation, neighbor-consensus, humidity bias flags.
Gates:
- strict timestamp integrity; quarantine for persistent sensor resets.

### Hydrology (streamflow gauges)
High-value signals:
- rating curve revision markers, provisional/final states, backfill windows, unit conversions.
Gates:
- hold if provisional policy requires final for certain products.

### Rasters / Remote Sensing
High-value signals:
- band completeness, nodata consistency, georeferencing validity, cloud-mask availability.
Gates:
- fail on missing CRS/transform; soft-fail on minor metadata warnings.

---

## ✅ Operational Checklist (Per Run)

1) Trigger captured + idempotency key computed  
2) Fetch raw + capture ETag/Last-Modified + checksum  
3) Parse + schema snapshot + contract diff  
4) Profile metrics (nulls, dupes, ranges)  
5) Drift/anomaly checks (if enabled)  
6) Gate decision + reason codes  
7) Persist raw/processed/quarantine deterministically  
8) Emit PROV bundle + validation artifacts  
9) Update STAC/DCAT (publish only)  
10) Emit telemetry + alerts if thresholds crossed  

---

## 📚 References

- PROV data model and PROV-O ontology for provenance graphs.
- Data cataloging via DCAT; geospatial asset metadata via STAC.
- Data quality checks and validation frameworks as inspiration for expectation/constraint patterns.
- OpenTelemetry conventions for consistent cross-service telemetry.

---

## 🧪 Validation & CI/CD (Project Gates)

### Validation steps
- [ ] Markdown protocol validation
- [ ] Schema validation (STAC/DCAT/PROV) for publish artifacts
- [ ] Gate decision + reason codes recorded for each run
- [ ] PROV bundle emitted for each run attempt
- [ ] Telemetry emitted with gate outcomes and error classes

### Reproduction (deterministic replay expectations)
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas (stac/dcat/prov)
# 2) run watcher unit tests
# 3) run doc lint
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates
- FAIR+CARE council review: quarterly (per `review_cycle`)
- Security council review: as applicable (new sensitive sources, new endpoints, new redaction rules)
- Historian/editor review: as applicable (when watchers affect narrative-facing evidence products)

### CARE / sovereignty considerations
- No inference of sensitive locations.
- Apply generalization/redaction rules where domain policies require it.

### AI usage constraints
- AI transforms are limited to the declared `ai_transform_permissions`.
- Prohibited: generating new policy and inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1 | 2025-12-20 | Standardized formatting to v12 Universal Doc layout; operational content preserved | TBD |

---

## 🔗 Footer

- 🔙 Back to Index: `docs/README.md`
- 🧱 Data-Ops: `docs/data-ops/README.md`
- 🛡️ Governance Charter: `docs/governance/README.md`
---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
