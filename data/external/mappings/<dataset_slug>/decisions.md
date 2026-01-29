---
title: "DECISIONS — External Mapping: <dataset_slug>"
path: "data/external/mappings/<dataset_slug>/decisions.md"
version: "v0.1.0"
last_updated: "2026-01-29"
status: "draft"
doc_kind: "Data Mapping Decisions"
dataset_slug: "<dataset_slug>"
data_tier: "external"

# Governance + Metadata
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

# Ownership + Traceability
owner: "TBD"
reviewers: ["TBD"]
doc_uuid: "urn:kfm:data-mapping:external:<dataset_slug>:decisions:v0.1.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"

# Source (fill in)
source_name: "TBD"
source_homepage: "TBD"
source_license: "TBD"
source_access: "TBD"  # API / download URL / partner drop / etc.
source_version: "TBD" # dataset version, release date, or snapshot tag
---

![Status](https://img.shields.io/badge/status-draft-yellow)
![Tier](https://img.shields.io/badge/tier-external-blue)
![Evidence](https://img.shields.io/badge/stance-evidence--first-brightgreen)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)

# 🧾 Decisions — External Dataset Mapping: `<dataset_slug>`

> **What this file is:** an **append-only decision log** for mapping an external dataset into KFM’s governed pipeline.  
> **What “decision” means here:** any choice that affects **meaning, reproducibility, governance, or UX** (schema interpretation, CRS, time semantics, redactions, caching, etc.).  
> KFM’s pipeline ordering is **non‑negotiable**: Raw → Processed → Catalog/Prov → Database → API → UI. Any shortcut is “flawed unless proven otherwise.”:contentReference[oaicite:0]{index=0}

---

## 📘 Overview

### Purpose 🎯
Capture *why* we mapped this dataset the way we did (and what tradeoffs we accepted), in a format that supports:
- reproducible processing (“deterministic pipeline”):contentReference[oaicite:1]{index=1}
- governed publishing (metadata + lineage are required boundary artifacts):contentReference[oaicite:2]{index=2}
- fail‑closed review (no “maybe it’s fine” merges):contentReference[oaicite:3]{index=3}

### Scope ✅ / ❌
| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Field/attribute mapping into KFM contracts (schemas + catalogs) | Implementing the whole ETL (that lives in `src/pipelines/`):contentReference[oaicite:4]{index=4} |
| Spatial model decisions (geometry type, CRS transforms, simplification) | UI feature work (that lives in `web/`):contentReference[oaicite:5]{index=5} |
| Temporal semantics (valid vs transaction time; precision & uncertainty) | Narrative/story authoring (Story Nodes live elsewhere):contentReference[oaicite:6]{index=6} |
| Governance decisions (classification, redaction/generalization, access rules) | “Secret” or undocumented transforms (prohibited):contentReference[oaicite:7]{index=7} |
| External integration mode (live fetch vs cached snapshot vs hybrid) | Bypassing API governance (explicitly disallowed):contentReference[oaicite:8]{index=8} |

### Audience 👥
- **Primary:** data stewards, pipeline devs, reviewers
- **Secondary:** API/UI devs (need semantics & constraints), future contributors (need rationale)

### Definitions 📚
- **Raw:** immutable source snapshot (or immutable reference to external source), not hand-edited:contentReference[oaicite:9]{index=9}
- **Processed:** standardized output produced deterministically (idempotent, logged):contentReference[oaicite:10]{index=10}
- **Catalog artifacts:** STAC + DCAT + PROV required before “published”:contentReference[oaicite:11]{index=11}
- **Valid time:** when the thing happened (real-world time)
- **Transaction time:** when the record was observed/ingested (system time) — multiple time perspectives can introduce uncertainty; we must condense into a consistent interpretation (and document it).:contentReference[oaicite:12]{index=12}

### Key Artifacts 🔗
> Keep this table updated as files become real.

| Artifact | Expected Location | Notes |
|---|---|---|
| 🧾 Decisions log | `data/external/mappings/<dataset_slug>/decisions.md` | This file |
| 🧬 Mapping spec | `data/external/mappings/<dataset_slug>/mapping.(yml\|json\|csv)` | Column/field map + transforms (choose one format and stick to it) |
| 🧾 Data dictionary | `data/external/mappings/<dataset_slug>/dictionary.md` | Define each output field + units + enums |
| 🗺️ STAC Collection | `data/stac/collections/<collection_id>.json` | Required for geospatial assets:contentReference[oaicite:13]{index=13} |
| 🧱 STAC Item(s) | `data/stac/items/<dataset_slug>/...json` | Must point to processed assets:contentReference[oaicite:14]{index=14} |
| 🏷️ DCAT Dataset | `data/catalog/dcat/<dataset_id>.jsonld` | Discoverability + license + distributions:contentReference[oaicite:15]{index=15} |
| 🧾 PROV bundle | `data/prov/<dataset_slug>/prov.<run_id>.jsonld` | Inputs → steps → outputs, agents, params:contentReference[oaicite:16]{index=16} |
| 🧪 Validation notes | `tests/...` and/or `data/external/mappings/<dataset_slug>/validation.md` | List repeatable checks; CI will enforce rules:contentReference[oaicite:17]{index=17} |

### Definition of Done ✅
> KFM templates emphasize front-matter + required sections + repeatable validation + explicit governance notes.:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

- [ ] Front-matter complete + accurate (no removed fields; use `TBD`/`n/a` instead):contentReference[oaicite:20]{index=20}
- [ ] Decision Log has at least one concrete decision (integration mode + license)
- [ ] Mapping spec exists and references this decisions doc
- [ ] STAC + DCAT + PROV artifacts exist (or have explicit tracked TODO + owners):contentReference[oaicite:21]{index=21}
- [ ] Validation steps listed and repeatable:contentReference[oaicite:22]{index=22}
- [ ] Governance + sensitivity decisions are explicit (and reviewed if non-public):contentReference[oaicite:23]{index=23}

---

## 🗂️ Directory Layout

KFM’s governed layout explicitly supports per-domain **mappings** folders (dataset → STAC/DCAT/PROV mapping docs).:contentReference[oaicite:24]{index=24}

### This folder 📁
```text
data/external/mappings/<dataset_slug>/
├── 🧾 decisions.md                 # (this) append-only decision log
├── 🧬 mapping.yml                  # mapping spec (or .json / .csv)  ✅ choose one
├── 📚 dictionary.md                # data dictionary (fields, units, enums)
├── 🧪 validation.md                # repeatable checks + thresholds (optional but recommended)
└── 📦 samples/                     # tiny examples / schemas / snapshots (no secrets)
```

### Related repository paths 🧭
| Area | Path | What lives here |
|---|---|---|
| 🧱 Schemas | `schemas/` | JSON Schemas for STAC/DCAT/PROV/story nodes/etc.:contentReference[oaicite:25]{index=25} |
| 🛠️ Pipelines | `src/pipelines/` | ETL + transformations (domain specific):contentReference[oaicite:26]{index=26} |
| 🧾 Provenance | `data/prov/` | PROV bundles per run/dataset:contentReference[oaicite:27]{index=27} |
| 🗺️ STAC | `data/stac/` | STAC Collections/Items:contentReference[oaicite:28]{index=28} |
| 🏷️ DCAT | `data/catalog/dcat/` | DCAT outputs:contentReference[oaicite:29]{index=29} |
| 🧪 CI rules | `.github/workflows/` | Validation gates (schema, links, secrets, sensitivity scans):contentReference[oaicite:30]{index=30} |

---

## 🧭 Decision Principles (Non‑Negotiables)

### 1) Canonical pipeline ordering 🔁
Raw → Processed → Catalog/Prov → Database → API → UI — **no leapfrogging**.:contentReference[oaicite:31]{index=31}

### 2) Contract-first + deterministic ETL 📜
Schemas/contracts are first-class artifacts; transforms are idempotent, config‑driven, fully logged.:contentReference[oaicite:32]{index=32}

### 3) Fail closed governance 🧯
If a policy/check fails, KFM blocks the action; e.g., missing license → CI fails.:contentReference[oaicite:33]{index=33}

### 4) “Boundary artifacts” required before publish 🧱
A dataset is not “fully published” until it has lineage and catalogs (STAC/DCAT/PROV).:contentReference[oaicite:34]{index=34}:contentReference[oaicite:35]{index=35}

### 5) Provenance is inspectable, not vibes 🧾
PROV should record **entities (inputs/outputs), activities (process), agents (who/what)**, with parameters/notes as needed.:contentReference[oaicite:36]{index=36}  
If a dataset lacks a provenance file, it’s considered a trust red flag.:contentReference[oaicite:37]{index=37}

### 6) AI & Focus Mode: opt-in + no side-channel leaks 🤖🔒
AI hints must be opt‑in and labeled; sensitive locations must be generalized/omitted so the UI/AI can’t become a bypass channel.:contentReference[oaicite:38]{index=38}:contentReference[oaicite:39]{index=39}

### 7) Access control enforced at the API boundary 🧱🛡️
Policies (e.g., via OPA) are used to govern who can see which data; governance must not be bypassable.:contentReference[oaicite:40]{index=40}

---

## 🗒️ Decision Log (Append‑Only)

> **Rule:** add newest decisions at the top.  
> **ID format:** `DM-<dataset_slug>-0001` (Decision Map), incrementing.

| ID | Date | Decision | Status | Rationale | Owner | Evidence / Links |
|---|---|---|---|---|---|---|
| DM-<dataset_slug>-0001 | YYYY-MM-DD | Choose **integration mode** (live vs cached vs hybrid) | proposed | External integrations can keep repo lean but must manage performance & governance:contentReference[oaicite:41]{index=41} | TBD | STAC/DCAT/PROV plan |
| DM-<dataset_slug>-0002 | YYYY-MM-DD | Define **time semantics** (valid vs transaction; precision) | proposed | Multiple temporal perspectives add uncertainty; must condense + document:contentReference[oaicite:42]{index=42} | TBD | Dictionary + schema |
| DM-<dataset_slug>-0003 | YYYY-MM-DD | Define **sensitivity/classification** and redaction rules | proposed | CI scans enforce sensitive data handling + classification consistency:contentReference[oaicite:43]{index=43} | TBD | Policy doc / OPA rules |

---

## 🗺️ Mapping Decisions (Fill These Out)

### A) Source & License 📜
- **Source name:** `TBD`
- **Publisher/owner:** `TBD`
- **License:** `TBD`  
  - If license is missing/unclear → **fail closed**: do not publish.:contentReference[oaicite:44]{index=44}
- **Attribution string (exact):** `TBD`
- **Update cadence:** `TBD`
- **Source version identifier:** `TBD` (date, release tag, API version, etc.)

✅ **Decision:** Is this dataset treated as:
- [ ] **Snapshot** (pinned version) — recommended when reproducibility matters most  
- [ ] **Live external** (latest at query time) — must document drift risk + caching plan  
- [ ] **Hybrid** (live fetch + optional pin/caches for key products)

> External integrations are useful because they avoid storing multi‑GB data and can remain up‑to‑date, but must be careful about performance; optional triggers + prefetch/caching can help.:contentReference[oaicite:45]{index=45}

---

### B) Integration Mode (External ↔ KFM) 🔌

Pick one and justify:

1) **Live Fetch** 🌐  
   - Pros: always current  
   - Cons: latency + external dependency + nondeterminism  
2) **Cached Snapshot** 📦  
   - Pros: deterministic, offline-capable  
   - Cons: storage cost, must manage refresh cycle  
3) **Hybrid** 🧩  
   - Pros: both; default to cached, allow live compare  
   - Cons: complexity

**Decision:** `TBD`  
**Notes:** `TBD`

---

### C) Spatial Model & CRS 🌍
- **Geometry type:** `TBD` (Point/Line/Polygon/Raster/Tabular)  
- **Canonical CRS in KFM:** `TBD`  
- **Transform rules:** `TBD`
- **Precision policy:** `TBD`  
- **Generalization policy (if sensitive):** `TBD` — align with “no sensitive location leaks.”:contentReference[oaicite:46]{index=46}

**Edge case handling**
- Invalid geometries: `TBD`
- Self-intersections: `TBD`
- Multipart features: `TBD`
- Topology simplification threshold: `TBD`

---

### D) Temporal Model & Semantics 🕰️
> Time-oriented data can be represented by mapping time into a visual time dimension or into space; choose static vs dynamic representations based on the task and user needs.:contentReference[oaicite:47]{index=47}

**Input time fields (raw/external)**
- `TBD`

**KFM time fields (output)**
- `valid_start`: `TBD`
- `valid_end`: `TBD`
- `transaction_time`: `TBD` (ingest timestamp)
- `time_precision`: `TBD` (year / month / day / instant / interval)
- `time_uncertainty`: `TBD` (if applicable)

✅ **Decision checklist**
- [ ] Define **valid time** vs **transaction time**
- [ ] Decide how to resolve **conflicts** across multiple time perspectives (document it):contentReference[oaicite:48]{index=48}
- [ ] Decide whether “unknown end” becomes `null`, “open interval”, or a sentinel

---

### E) Attribute Mapping & Normalization 🧬
**Mapping spec file:** `mapping.(yml|json|csv)` — must define:
- source_field → target_field
- type coercion rules
- unit conversions (with units recorded)
- controlled vocab / enums
- null/missing handling

**Normalization decisions**
- Strings: trim/case/folding rules `TBD`
- Units: canonical units `TBD`
- Categories: canonical enum mapping `TBD`
- Duplicate records: dedup strategy `TBD`

---

### F) Identifiers & Stable Keys 🆔
- **Primary key strategy:** `TBD`
- **Determinism requirement:** stable IDs should be derived deterministically from inputs/config so re-runs don’t reshuffle identities (supports reproducible lineage).:contentReference[oaicite:49]{index=49}
- **Cross-walks:** if source IDs change, maintain mapping table `TBD`

---

### G) Provenance & Metadata (STAC/DCAT/PROV) 🧾🗺️🏷️
Every dataset/evidence artifact needs:
- **STAC Collection + Item(s)**:contentReference[oaicite:50]{index=50}
- **DCAT dataset entry** (license, keywords, distributions):contentReference[oaicite:51]{index=51}
- **PROV bundle** (raw inputs → work → processed outputs; agents; params):contentReference[oaicite:52]{index=52}

**PROV expectations (minimum)**
- Entities: inputs/outputs (include checksums or stable references):contentReference[oaicite:53]{index=53}
- Activity: pipeline run (timestamp, script/config identifiers, parameters):contentReference[oaicite:54]{index=54}
- Agents: software + human trigger (if applicable):contentReference[oaicite:55]{index=55}

> If it doesn’t have provenance, treat it as a red flag in KFM.:contentReference[oaicite:56]{index=56}

---

### H) Governance, Sensitivity & Access 🔒
**Classification:** `public | restricted | confidential | tribal_sensitive | TBD`  
**Care label:** `TBD`  
**Redaction/generalization rules:** `TBD`

**Policy enforcement**
- Access decisions must be enforced via the API layer and/or policy engine (e.g., OPA), not by UI convention.:contentReference[oaicite:57]{index=57}
- CI includes scans for secrets, PII, sensitive locations, and classification downgrades; document how we comply.:contentReference[oaicite:58]{index=58}

**Focus Mode / AI constraints**
- AI contributions opt-in + labeled (include confidence/uncertainty):contentReference[oaicite:59]{index=59}
- No sensitive location leakage; use broad regions/blurred markers if needed:contentReference[oaicite:60]{index=60}

---

### I) Performance, Caching & Determinism ⚡
**External calls**
- Expected latency budget: `TBD`
- Retry/backoff: `TBD`
- Rate limiting: `TBD`
- Cache TTL (if live): `TBD`

> External integrations should remain optional/triggered so normal operation isn’t impacted; prefetching some datasets can make them internal thereafter.:contentReference[oaicite:61]{index=61}

---

### J) UI/Visualization Implications 🗺️✨
Document any UI assumptions so we don’t accidentally build a layer the data can’t support:
- Default styling choices: `TBD`
- Time slider behavior (if temporal): `TBD`
- Multi-scale behavior (zoom thresholds): `TBD`
- Tooltip fields (safe/public): `TBD`

> Choose temporal visualization approach consciously (static vs dynamic; mapping time to time vs time to space).:contentReference[oaicite:62]{index=62}

---

## 🧪 Validation & CI Notes

KFM CI gates commonly include:
- Markdown protocol + YAML front-matter + required sections:contentReference[oaicite:63]{index=63}
- Link/reference validation:contentReference[oaicite:64]{index=64}
- JSON Schema validation (STAC/DCAT/PROV etc.):contentReference[oaicite:65]{index=65}
- Security & governance scans (secrets, PII, sensitive locations, classification consistency):contentReference[oaicite:66]{index=66}

✅ **Add repeatable validation steps here**
- [ ] `TBD` (schema validation command)
- [ ] `TBD` (sample query / sanity check)
- [ ] `TBD` (sensitivity scan outcome)

---

## 🛰️ Optional: Remote Sensing / Earth Engine Notes (If Applicable)

If this mapping uses remote sensing workflows (e.g., GEE exports), capture:
- export parameters (region, scale, bands, time filters)
- whether we used precomputed assets vs new exports
- how metadata is attached to outputs

Example principle: attaching run parameters as metadata helps preserve a record of important properties and supports tool interoperability.:contentReference[oaicite:67]{index=67}  
Performance note: prefer pre-existing computed results where possible; large areas can take much longer to export and should be approached incrementally.:contentReference[oaicite:68]{index=68}

---

## 🧩 Appendix — New Decision Template

<details>
<summary>📌 Click to expand: decision record template</summary>

```markdown
### DM-<dataset_slug>-XXXX — <short title>

- **Date:** YYYY-MM-DD
- **Status:** proposed | accepted | superseded
- **Owner:** @TBD
- **Context:** What problem are we solving?
- **Decision:** What did we choose?
- **Alternatives considered:** What else did we consider and why not?
- **Consequences:** What changes because of this?
- **Governance:** sensitivity/classification impact? policy updates needed?
- **Evidence:** links to sources, samples, tests, PRs, provenance IDs
```

</details>

---

## 🔗 References (Project Files)

- KFM blueprint (architecture, pipeline ordering, governance): :contentReference[oaicite:69]{index=69}  
- KFM v13 Markdown Guide (contracts, catalogs, CI gates, directory layout): :contentReference[oaicite:70]{index=70}  
- Visualization of Time-Oriented Data (temporal modeling/visualization): :contentReference[oaicite:71]{index=71}  
- Cloud-Based Remote Sensing with Google Earth Engine (metadata + time-series workflows): :contentReference[oaicite:72]{index=72}  


