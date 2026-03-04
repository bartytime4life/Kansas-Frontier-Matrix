<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c7f3d4d7-6d18-4e1b-8e8a-ec8d5f3ac4a1
title: Hazards Domain
type: standard
version: v1
status: draft
owners: KFM Domain Stewards (Hazards)
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related:
  - docs/domains/hazards/README.md
  - src/pipelines/autonomous/hazards-refresh/README.md
  - docs/standards/governance/ROOT-GOVERNANCE.md
  - docs/MASTER_GUIDE_v13.md
tags: [kfm, domain, hazards, governance, provenance]
notes:
  - "Domain runbook + contract surface for hazards ingestion, cataloging, and governed access."
[/KFM_META_BLOCK_V2] -->

<div align="center">

# 🌪️ Hazards Domain  
One-line purpose: **Define the governed contract for ingesting, cataloging, and serving multi-hazard event data in KFM** (storms, warnings, disaster declarations, earthquakes, wildfire/smoke).

**Path:** `docs/domains/hazards/README.md`

<img alt="Status" src="https://img.shields.io/badge/status-active%20pipeline-brightgreen" />
<img alt="Domain" src="https://img.shields.io/badge/domain-hazards-orange" />
<img alt="Governance" src="https://img.shields.io/badge/policy-default--deny%20fail--closed-red" />
<img alt="Catalog contract" src="https://img.shields.io/badge/contract-STAC%20%2B%20DCAT%20%2B%20PROV-blue" />
<img alt="License" src="https://img.shields.io/badge/license-docs%20CC--BY%204.0-lightgrey" />

</div>

---

## Impact block

- **Status:** **CONFIRMED:** Hazards ingestion is implemented via an automated refresh pipeline marked “Active / Enforced” (v11).  
- **Owners:** **UNKNOWN:** not yet pinned in this directory (add names/teams in PR).  
- **Primary pipeline:** `src/pipelines/autonomous/hazards-refresh/`  
- **Primary contract surfaces:** **CONFIRMED:** `STAC + DCAT + PROV` catalogs and a governed API boundary.
- **Non-goal:** **CONFIRMED:** KFM is **not** an operational emergency alert system.

**Quick nav:**  
[Scope](#scope) · [Where it fits](#where-it-fits) · [Inputs](#acceptable-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Contracts](#contracts-and-invariants) · [Source registry](#source-registry-matrix) · [DoD](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix-verification-steps-for-unknowns)

---

## Evidence labels used here

- **CONFIRMED** — grounded in existing KFM docs/pipeline notes.
- **PROPOSED** — a recommended pattern consistent with KFM standards, but not verified in this directory yet.
- **UNKNOWN** — must be verified in-repo before treating as truth.

---

## Scope

### What “Hazards” means in KFM

**CONFIRMED:** The hazards domain is a **multi-hazard event layer** intended to support map + timeline exploration and cross-domain resilience analysis (e.g., hazards linked to infrastructure, land, and population context).  
**CONFIRMED:** Hazards include both **historical** records and **near-real-time** feeds, but KFM’s intent is **evidence-first analysis** rather than alerting.

### Primary hazard classes (domain vocabulary)

- **Severe weather events** (tornadoes, hail, floods, winter storms, etc.)
- **Official warnings and alert polygons** (severe weather warning geometries)
- **Disaster declarations** (federal declarations, county tagging)
- **Seismic events** (earthquake records)
- **Wildfire and smoke evidence** (satellite detections and analyst polygons; official CAP alerts)

> IMPORTANT: **CONFIRMED:** Even if near-real-time warnings are ingested, **do not represent this domain as an emergency alerting product**. This is a research/analysis atlas with governance guardrails.

[Back to top](#-hazards-domain)

---

## Where it fits

### Repository placement

**CONFIRMED (KFM-wide):** Data moves through required stages and only becomes “published” once boundary artifacts exist (catalog triplet and provenance).  
- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/` → publication metadata in `STAC/DCAT/PROV`.

**CONFIRMED (system boundary):**
- **Frontend/UI must not access DB/storage directly**; all reads cross the **governed API + policy boundary**.
- Hazard features should always be traceable back to **catalog + provenance** objects.

### Key upstream/downstream connections

**Upstream**
- External agencies / feeds (NOAA, NWS, FEMA, USGS, satellite-derived wildfire/smoke sources)

**Core processing**
- **CONFIRMED:** Hazards refresh pipeline executes a declarative DAG (LangGraph YAML in the described design), normalizes events, builds STAC items, validates checksums, and syncs to the knowledge graph.

**Downstream**
- **CONFIRMED:** Knowledge graph (Neo4j) references catalogs; UI and Focus Mode rely on governed evidence resolution and citations.

[Back to top](#-hazards-domain)

---

## Acceptable inputs

### Data allowed in this domain

**CONFIRMED:** Multi-hazard event sources may include (at least):
- NOAA Storm Events
- NWS severe weather warnings (polygon feeds)
- FEMA disaster declarations (county tagging)
- USGS earthquake records
- Wildfire detection from satellite sources

**PROPOSED (formats):**
- GeoJSON / FlatGeobuf / GeoParquet for event geometries
- STAC Items for published event artifacts
- DCAT JSON-LD for dataset discovery
- PROV bundles or run receipts for lineage

### Minimal input metadata requirements (domain policy)

**PROPOSED (enforce in CI):**
- source name + access method (URL/API) + freshness hints (ETag/Last-Modified if available)
- license + attribution text
- geographic extent (bbox) and temporal span
- sensitivity classification (`public`, `restricted`, etc.)
- schema reference (JSON Schema or equivalent)

[Back to top](#-hazards-domain)

---

## Exclusions

### What must NOT go here

- **CONFIRMED:** Anything that turns KFM into an “alerting” or “dispatch” system.
- **PROPOSED:** Personally identifying information (PII), precise residential addresses, or victim-identifying incident details.
- **PROPOSED:** Unverified social media rumor ingestion as “truth.” (If used as *evidence*, it must be explicitly labeled and governed.)

### Where to put related-but-not-hazards things

- **Climate anomaly model outputs** → climate domain (then referenced as overlays in hazards)
- **Infrastructure layers** → infrastructure domain
- **Narratives about hazard impacts** → Story Nodes (draft/published), referencing hazard events via EvidenceRefs

[Back to top](#-hazards-domain)

---

## Directory tree

> NOTE: This tree distinguishes what is **present vs planned** to avoid implying repo state.

```text
docs/domains/hazards/
  README.md                      # (THIS FILE) Domain contract + runbook

  (PROPOSED) sources.md           # Curated list of hazard sources + licenses + attribution text
  (PROPOSED) glossary.md          # Domain vocabulary: event types, severity scales, geometry semantics
  (PROPOSED) schemas/             # Domain-specific schema extensions (must be cross-repo validated)
  (PROPOSED) qa/                  # QA playbooks: spatial sanity checks, dedupe rules, drift checks
  (PROPOSED) examples/            # Minimal STAC/DCAT/PROV examples for hazard event datasets
```

[Back to top](#-hazards-domain)

---

## Quickstart

### 1) Read the pipeline runbook (authoritative)

- `../../../src/pipelines/autonomous/hazards-refresh/README.md`

### 2) Run in sandbox mode first

```bash
# PSEUDOCODE (verify the real entrypoint in the pipeline README):
# Goal: fetch + normalize + write WORK artifacts without publishing.
kfm run --spec spec/hazards-refresh.yaml --mode sandbox --out data/work/hazards/
```

### 3) Promote only after contracts pass (triplet + policy)

```bash
# PSEUDOCODE:
# Goal: validate STAC/DCAT/PROV, enforce policy gates, then publish.
make ci.test
conftest test receipts/run_receipt.json -p policies
make hazards.publish
```

### 4) Validate you didn’t bypass the trust membrane

**CONFIRMED invariant:** UI/clients must only read hazards through governed APIs, not direct DB queries.

[Back to top](#-hazards-domain)

---

## Contracts and invariants

### Publishing contract: STAC + DCAT + PROV

**CONFIRMED (KFM-wide):** KFM treats catalogs and provenance as **contract surfaces** between pipelines and runtime.  
**PROPOSED minimum:** treat the “catalog triplet” as non-optional; missing or inconsistent pieces fail promotion.

### Data lifecycle and staging

**CONFIRMED (KFM-wide):**
- **RAW**: immutable source captures (read-only)
- **WORK**: intermediate joins/normalization, dedupe, clustering, QA
- **PROCESSED**: finalized domain outputs
- **PUBLISHED**: discoverable via catalogs (STAC/DCAT/PROV), available through governed APIs

### Governance posture

**CONFIRMED (KFM-wide):**
- default-deny, fail-closed policy enforcement
- sensitive fields must be generalized/redacted; surface CARE flags when applicable
- export paths must include license + attribution automatically

[Back to top](#-hazards-domain)

---

## Source registry matrix

> This is the “what we ingest” view. Add rows only when you can fill in license + cadence + geometry + provenance rules.

| Dataset / Feed | Hazard class | Geometry | Update cadence | License posture | Evidence |
|---|---|---:|---:|---|---|
| NOAA Storm Events Database | severe weather events | point / county / track (varies) | monthly | public domain (USG) | CONFIRMED |
| NOAA SPC Severe Weather GIS | tornado tracks, hail/wind reports | lines + points | annually | openly downloadable | CONFIRMED |
| FEMA Disaster Declarations (OpenFEMA) | declarations by county | county tagging | continual | public domain (USG) | CONFIRMED |
| NWS alerts / warnings (CAP) | warnings/advisories | polygon + text | continual | government alerts | CONFIRMED |
| USGS earthquakes | seismic events | points | UNKNOWN | UNKNOWN | UNKNOWN |
| NASA FIRMS (MODIS/VIIRS) | wildfire detections | points | within hours | UNKNOWN | CONFIRMED (cadence only) |
| NOAA HMS smoke polygons | smoke extent | polygons | daily | UNKNOWN | CONFIRMED (cadence only) |

[Back to top](#-hazards-domain)

---

## Definition of Done

### DoD: adding or updating a hazards dataset

- [ ] **Registry entry updated** (owner, license, policy label, cadence, contact)
- [ ] **RAW acquisition** is immutable with manifest + checksums
- [ ] **Processed artifacts** exist with digests and predictable paths
- [ ] **STAC + DCAT + PROV** schema-valid and cross-linked
- [ ] **Policy decisions recorded**; default-deny tests pass; generalized derivatives created if required
- [ ] **Evidence resolution works** from UI/Focus (citations resolve; denied layers fail safely)
- [ ] **Audit trail** exists (run receipt emitted; promotion decision recorded)

[Back to top](#-hazards-domain)

---

## FAQ

### Is this an emergency alert system?

**CONFIRMED:** No. Even if NWS warnings are ingested, KFM is **not** an operational alert system. Treat warnings as evidence layers for analysis and historical context.

### How do hazards relate to the knowledge graph?

**CONFIRMED:** Hazard events are represented as nodes in the knowledge graph and linked with time + geometry semantics; catalogs and provenance remain the primary trace surface.

### Can I add a new hazard feed?

**PROPOSED approach:**
1. Add it to a `sources.md` registry (license, cadence, access URL, attribution).
2. Implement ingestion in the hazards pipeline (RAW→WORK→PROCESSED).
3. Emit STAC/DCAT/PROV and run receipts.
4. Add CI policy checks (deny-by-default) and a minimal QA suite.
5. Only then promote to PUBLISHED.

[Back to top](#-hazards-domain)

---

## Appendix: verification steps for UNKNOWNs

Use this checklist to turn UNKNOWN → CONFIRMED with minimal effort:

1. **Confirm the real hazards pipeline entrypoint**
   - Open: `src/pipelines/autonomous/hazards-refresh/README.md`
   - Record: command, config/spec path, and expected output directories.

2. **Confirm the hazards output locations**
   - Search for `data/raw/hazards`, `data/work/hazards`, `data/processed/hazards`
   - Update this README’s Quickstart commands to be runnable.

3. **Confirm policy labels and obligations**
   - Identify the Rego bundle / Conftest policy pack used for dataset promotion.
   - Document any hazards-specific redaction rules (e.g., geometry generalization thresholds).

4. **Confirm API endpoints for hazards**
   - Locate the governed API contract for hazard queries.
   - Add a short “Usage” section with real endpoints + example requests (and policy-safe error behavior).

[Back to top](#-hazards-domain)
