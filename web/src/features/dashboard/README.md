---
title: "Dashboard Feature (KFM Web UI)"
repo_path: "web/src/features/dashboard"
status: "draft"
version: "v0.1.0"
last_updated: "2026-01-15"
audience: ["frontend-devs", "design", "api-devs", "governance"]
---

# 🧭 Dashboard Feature — `web/src/features/dashboard` 📊

![Status](https://img.shields.io/badge/status-draft-orange)
![UI](https://img.shields.io/badge/ui-React-informational)
![Maps](https://img.shields.io/badge/maps-MapLibre%20%2F%20Cesium-informational)
![Principle](https://img.shields.io/badge/principle-provenance--first-blue)

> The Dashboard is KFM’s “control room” view: **a single-glance overview** of data/catalog health, recent updates, key stories, and governance signals — while staying **100% within KFM’s contract-first + provenance-first rules**.  
> Anything shown here must be **traceable**, **contracted**, and **safe to display**. :contentReference[oaicite:0]{index=0}

---

## ✨ What this is

KFM is designed as an evidence-backed “living atlas,” with a strict pipeline that moves from data → catalogs → graph → APIs → UI → stories → Focus Mode.:contentReference[oaicite:1]{index=1}  
The Dashboard is the **UI surface** where we summarize the health and “pulse” of those upstream artifacts (without bypassing them).

KFM’s frontend is described as a React SPA that pulls dynamic content from the API, with separate UI subsystems for map viewers and story content.:contentReference[oaicite:2]{index=2}  
This feature module is intended to implement a **Dashboard page + widgets** consistent with that architecture.

---

## ✅ Non‑negotiables (KFM invariants)

These rules apply to **every** Dashboard card, number, chart, and “recent activity” item:

1. **Pipeline ordering is absolute**  
   `ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode`:contentReference[oaicite:3]{index=3}

2. **API boundary rule**  
   The frontend **must never** query Neo4j directly; everything goes through the governed API layer (`src/server/`).:contentReference[oaicite:4]{index=4}

3. **Provenance first**  
   Published data must be registered (STAC/DCAT + PROV) before graph/UI use.:contentReference[oaicite:5]{index=5}  
   And anything visible in UI or Focus Mode must be traceable to cataloged sources and provable processing.:contentReference[oaicite:6]{index=6}

4. **Evidence-first narrative**  
   No unsourced narrative content (also applies to dashboard summaries that read like narrative).:contentReference[oaicite:7]{index=7}

5. **Sovereignty & classification propagation**  
   No output can be less restricted than its inputs; UI must implement safeguards (e.g., generalized/blurred sensitive locations).:contentReference[oaicite:8]{index=8}

6. **CI gates are part of “done”**  
   Contributions must pass schema/provenance/security checks; missing required artifacts fails CI.:contentReference[oaicite:9]{index=9}

---

## 🧩 Scope

### In scope ✅
- A **Dashboard route/page** that aggregates high-level system info via **contracted APIs**
- Widget cards for:
  - Catalog overview (STAC/DCAT/PROV counts, last publish)
  - Recent datasets / new items
  - Recent events / timeline highlights (summary-only)
  - Featured Story Nodes / learning paths
  - Governance + telemetry signals (redactions, blocked publications, sensitive access)
  - “Live” updates (optional): subscription/polling façade

### Out of scope ❌
- Direct database / Neo4j access
- “Mystery queries” that bypass catalog artifacts
- Uncited narrative claims inside cards
- Admin-only privileged actions unless explicitly governed by policy + contracts

---

## 🧠 Why the Dashboard exists

KFM supports diverse audiences and workflows (public exploration, museums/educators, hazard monitoring, etc.).:contentReference[oaicite:10]{index=10}  
A dashboard mode is specifically contemplated for **auto-updating** “new events” via GraphQL subscriptions/WebSockets as the platform grows toward real-time feeds.:contentReference[oaicite:11]{index=11}

---

## 🏗️ Architecture & data flow

```mermaid
flowchart LR
  subgraph Upstream["Upstream (governed)"]
    A[ETL] --> B[STAC/DCAT/PROV catalogs]
    B --> C[Neo4j graph]
  end

  subgraph Boundary["Boundary (contract-first)"]
    D[API Layer\nREST + GraphQL\nredaction + access control]
  end

  subgraph UI["Web UI (React)"]
    E[Dashboard\n(web/src/features/dashboard)]
    F[Map UI\nMapLibre / optional Cesium]
    G[Story Nodes + Focus Mode]
  end

  B --> D
  C --> D
  D --> E
  D --> F
  D --> G
```

Key: **Dashboard must consume API contracts**, never graph directly.:contentReference[oaicite:12]{index=12}

---

## 🧱 Suggested feature module layout

> This is an “expected shape” for `web/src/features/dashboard/` in a feature-first UI organization.

```text
📁 web/src/features/dashboard/
├─ 📄 README.md                👈 you are here
├─ 📄 index.ts
├─ 📄 routes.ts                (route registration / lazy entry)
├─ 📄 DashboardPage.tsx        (page shell + grid layout)
├─ 📁 components/
│  ├─ 🧩 DashboardGrid.tsx
│  ├─ 🧩 DashboardCard.tsx
│  ├─ 🧩 ProvenanceChips.tsx   (STAC/DCAT/PROV + classification)
│  └─ 🧩 EmptyState.tsx
├─ 📁 widgets/
│  ├─ 📊 CatalogSummaryWidget.tsx
│  ├─ 🗺️ MapQuickstartWidget.tsx
│  ├─ 📚 StoryHighlightsWidget.tsx
│  ├─ 🧠 FocusModeEntryWidget.tsx
│  ├─ 🛡️ GovernanceTelemetryWidget.tsx
│  └─ ⚡ LiveEventsWidget.tsx
├─ 📁 api/
│  ├─ 🔌 dashboardClient.ts     (typed API wrapper)
│  └─ 📜 contracts.md           (human-readable contract notes)
├─ 📁 hooks/
│  ├─ 🪝 useDashboardSummary.ts
│  ├─ 🪝 useLiveEvents.ts       (subscription → polling fallback)
│  └─ 🪝 useGovernanceSignals.ts
├─ 📁 types/
│  ├─ 🧾 dashboard.types.ts
│  └─ 🧾 provenance.types.ts
└─ 📁 __tests__/
   ├─ ✅ DashboardPage.test.tsx
   └─ ✅ widgets.test.tsx
```

> KFM’s documentation describes frontend subfolders like `components/`, `views/`, and map `viewers/` (MapLibre/Cesium). This feature module should “plug into” that structure without duplicating it.:contentReference[oaicite:13]{index=13}

---

## 🧱 Widget design: what each card must prove

### 1) 📦 Catalog Summary (STAC/DCAT/PROV)
**Goal:** “What’s published? What changed?”

**Must include:**
- Counts + “last published” timestamps
- Links to:
  - STAC collection(s) and/or item(s)
  - DCAT dataset record(s)
  - PROV bundle(s)

Why: Catalog artifacts are required boundary outputs in the KFM lifecycle (they’re the interface to downstream stages).:contentReference[oaicite:14]{index=14}

---

### 2) 🗺️ Map + Timeline Quickstart
**Goal:** Jump into the primary exploration UI.

- Shortcut actions: “Open Map”, “Open Timeline”, “Resume last view”
- Displays lightweight “active layers” + “current time filter” (if stored)

KFM’s UI pipeline explicitly includes a React Map UI layer (MapLibre, optional Cesium).:contentReference[oaicite:15]{index=15}

---

### 3) 📚 Story Highlights
**Goal:** Guide users into governed narratives.

Story Nodes are authored in Markdown with supporting config; frontend loads and renders them (and synchronizes map state via MapLibre/Cesium).:contentReference[oaicite:16]{index=16}

Dashboard should show:
- Featured stories (editorial)
- Recently published stories
- “In review” stories (if permitted by role/governance)

---

### 4) 🧠 Focus Mode entry
**Goal:** “Ask a question” with evidence-backed answers.

Focus Mode answers should be constrained and clearly marked as AI synthesis, with **citations** users can click through.:contentReference[oaicite:17]{index=17}  
Dashboard should avoid being a “chat page,” but can provide a guided entry point (“Ask about this county”, “Ask about current layer”).

---

### 5) 🛡️ Governance + Telemetry (compliance signals)
KFM plans “telemetry-driven governance” dashboards to monitor:
- sensitive data access
- redactions
- publication blocked by policy:contentReference[oaicite:18]{index=18}

Dashboard can include a **Governance Telemetry Widget** that:
- displays **aggregate counts + trends** (not raw sensitive logs)
- provides links to governed audit views (role-gated)
- clearly shows classification labels

---

### 6) ⚡ Live Events (optional)
KFM’s roadmap describes a dashboard mode that auto-updates with new events using subscriptions/WebSockets.:contentReference[oaicite:19]{index=19}

Design recommendation:
- Prefer **GraphQL subscription → fallback to polling**
- UI shows:
  - connection state (live / degraded / offline)
  - last refresh timestamp
  - “why you’re seeing this” provenance chip

---

## 🧾 Provenance UX contract (required)

Every dashboard card that communicates a fact must ship a small “evidence panel” pattern:

- **Source chips:** STAC / DCAT / PROV identifiers (and classification label)
- **Click-through:** open the corresponding dataset metadata or evidence viewer
- **No orphan claims:** if you can’t cite it, don’t show it

> “Anything that shows up in the UI or Focus Mode must be traceable back to cataloged sources and provable processing.”:contentReference[oaicite:20]{index=20}

---

## 🔌 API contracts & integration notes

### Contract-first workflow
If Dashboard needs new backend data:
1. Define/update the contract first (OpenAPI / GraphQL schema under contracts).:contentReference[oaicite:21]{index=21}
2. Implement on server side (with redaction rules if sensitive).:contentReference[oaicite:22]{index=22}
3. Update frontend feature to use the contract (typed client).
4. Add tests (contract + UI) so CI can gate regressions.:contentReference[oaicite:23]{index=23}

### Example API capability surface (from KFM technical docs)
KFM’s API layer is described as REST + GraphQL, with endpoints returning metadata/data (GeoJSON/tiles) and analysis calls (e.g., NDVI).:contentReference[oaicite:24]{index=24}

**Dashboard principle:** Prefer **summary endpoints** (counts, latest IDs, timestamps) over heavy dataset payloads.

---

## ⚙️ Performance & scale considerations

KFM’s longer-term scaling notes explicitly call out:
- caching in the API for frequent queries
- tile servers/CDNs for heavy raster tiles
- GraphQL subscriptions/WebSockets for real-time updates:contentReference[oaicite:25]{index=25}

Dashboard should therefore:
- ✅ cache summary responses (client + server)
- ✅ request lightweight aggregates
- ✅ avoid rendering heavy map layers directly in dashboard cards
- ✅ show “loading vs stale vs live” states clearly

### Optional: approximate/interactive analytics (advanced)
Interactive dashboards often benefit from **approximate query processing** with error estimation (e.g., bootstrap-based approaches). This is relevant for “fast insights” panels that show aggregates with uncertainty bounds (but must be transparently labeled).:contentReference[oaicite:26]{index=26}

---

## 🔒 Security & safety notes (defensive posture)

- All dashboard inputs (search, filters) must be validated/sanitized.
- Never show secrets, raw logs, or sensitive identifiers unless contracts + governance explicitly allow it.
- Ensure **classification labels propagate** into the UI so users understand restrictions.:contentReference[oaicite:27]{index=27}

---

## ✅ Testing strategy

Minimum expectations (align with CI gates):
- **Unit tests**: widgets render states (loading/empty/error), provenance chips always present
- **Contract tests**: response schema validation for summary endpoints
- **Security checks**: ensure no sensitive fields leak in dashboard payloads
- **Snapshot tests (limited)**: layout stability for the grid

CI is a required gate; missing governance/provenance compliance should fail builds.:contentReference[oaicite:28]{index=28}

---

## 🧪 “Definition of Done” checklist for a new Dashboard widget

- [ ] Has a clear purpose + user story
- [ ] Pulls data **only** through a contract-first API (no direct graph access):contentReference[oaicite:29]{index=29}
- [ ] Every factual UI element has provenance chips (STAC/DCAT/PROV)
- [ ] Respects classification & sovereignty propagation:contentReference[oaicite:30]{index=30}
- [ ] Loading / error / empty / stale states included
- [ ] Tests added
- [ ] Docs updated (this README + any contract notes)

> Tip: For UI content meant for parsing/rendering (especially evidence/citation patterns), validate the Markdown rendering expectations so it won’t break “evidence panels” or citation parsing in downstream readers (Focus Mode UIs may depend on conventions).:contentReference[oaicite:31]{index=31}

---

## 🧑‍💻 Documentation philosophy (why this README is “NASA-grade”)

This project’s research/dev protocol explicitly calls out documenting each major module (including dashboards) with responsibilities and key functions/classes — so new contributors can navigate safely across disciplines.:contentReference[oaicite:32]{index=32}

---

## 🔗 Primary project references (most relevant)

> (These are the “north star” docs that constrain what the Dashboard can do.)

- 📘 KFM Technical Documentation: :contentReference[oaicite:33]{index=33}  
- 🧾 KFM Markdown Guide v13 (pipeline + invariants + governance): :contentReference[oaicite:34]{index=34}  
- 📝 Markdown Best Practices (rendering + governance patterns): :contentReference[oaicite:35]{index=35}  
- 🧪 Research / Master Coder Protocol (module documentation expectations): :contentReference[oaicite:36]{index=36}  

---

## 📚 Project library (all project files) 🗂️

<details>
<summary><strong>Click to expand the full reference library</strong> 📦</summary>

### 🧭 Core system & architecture
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `MARKDOWN_GUIDE_v13.md.gdoc`

### 🌐 Web UI / UX / rendering
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

### 🗺️ GIS / cartography / remote sensing
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`

### 🗄️ Data systems / performance / “big queries”
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`

### 📈 Statistics / analytics / ML
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `graphical-data-analysis-with-r.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`

### 🧪 Modeling / simulation / scientific computing
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`

### 🧠 Graphs / optimization / theory (long-horizon capability)
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### ⚖️ Governance / ethics / socio-technical context
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🔒 Security & resilience (defensive references)
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🧵 Concurrency / distributed systems
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

### 📚 Programming compendiums (A→X)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

</details>

---

## 🗺️ Roadmap ideas (aligned with KFM docs)

- **Evidence panels & richer context popups** (provenance-linked, uncertainty-aware):contentReference[oaicite:37]{index=37}
- **Dashboard “live mode”** via subscriptions/WebSockets:contentReference[oaicite:38]{index=38}
- **Mobile-friendly + offline packs** (future-friendly UX direction):contentReference[oaicite:39]{index=39}

---

## 🧾 Appendix: quick quotes that drive design decisions

> “The frontend UI must never query the Neo4j graph directly…”:contentReference[oaicite:40]{index=40}  
> “Anything that shows up in the UI or Focus Mode must be traceable…”:contentReference[oaicite:41]{index=41}

---

