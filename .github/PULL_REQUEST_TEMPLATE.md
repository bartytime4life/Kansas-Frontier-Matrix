# 🚀 Pull Request

<!--
📄 File: .github/PULL_REQUEST_TEMPLATE.md
🗓️ Last updated: 2026-01-13
🧭 Baseline: KFM‑MDP v11.x • Master Guide v13 (draft)
-->

> [!NOTE]
> **Keep it reviewable:** 2–3 sentences + reproducible steps + evidence links for any claim-bearing change (data/models/story).

> [!IMPORTANT]
> ⛓️ **Pipeline order is absolute:** **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
> If it isn’t **machine-validated + cataloged + provenance-linked**, it isn’t publishable in KFM.

> [!IMPORTANT]
> 🧾 **Contracts over vibes:** OpenAPI, STAC/DCAT/PROV schemas, graph IDs/ontology shapes, and Story Node templates are **contracts**.  
> If a contract drifts, CI should fail **before** anything ships.

> [!IMPORTANT]
> 🧩 **One home per subsystem:** no “mystery duplicate” folders. Put things where they belong (canonical homes) or expect CI + reviewers to block it.

> [!IMPORTANT]
> 🆔 **Stable IDs are forever:** IDs must be stable across **catalogs ↔ graph ↔ APIs ↔ Story Nodes**.  
> If an ID scheme changes, treat it as a migration + breaking change.

> [!IMPORTANT]
> 🧠 **Focus Mode trust model:** Focus Mode shows **only provenance-linked content**.  
> Any AI content must be **opt‑in + labeled + constrained by evidence + sovereignty rules**.

---

## 🧭 Quick nav
- [📌 Summary](#-summary-what--why)
- [✅ Repro steps](#-repro-steps)
- [🧭 Gate snapshot](#-gate-snapshot-fill-this-in)
- [🧩 Scope](#-scope--pipeline-stages-touched)
- [🧱 Design & contracts](#-design--architecture-notes-contracts--clean-boundaries)
- [🧑‍⚖️ Governance](#️-governance--policy-gate-required-when-making-claims-or-touching-governed-surfaces)
- [🧰 Domain checklists](#-domain-specific-checklists-optional-but-review-speed)

---

## 📌 Summary (what + why)

<!-- 1–3 sentences. Assume the reviewer is seeing this cold. -->
**Problem / context:**  

**What changed (solution):**  

**Why it matters (impact):**  

**User-visible outcome (if any):**  

**Release note (optional, 1 line):**  

---

## ✅ Repro steps

> [!TIP]
> Prefer “copy/paste runnable” over prose. If a reviewer can’t reproduce, they can’t approve.

**One-command repro (preferred):**
```bash
# e.g.
# make test
# make pipeline DOMAIN=hydrology RUN_ID=...
# python -m src.pipelines.<name> --config ...
```

**Inputs used (pin versions + where they live):**
- Raw input(s): `data/<domain>/raw/...` (or external reference + checksum)
- Config(s): `...`
- Seeds / randomness controls: `...`
- Runtime: `local | CI | container | cluster` (include image tag/digest if container)

**Expected output / success criteria (tight):**
- e.g., “STAC validates”, “API returns X”, “UI shows layer Y”, “story renders without unsourced claims”.

**Evidence bundle (preferred paths):**
- `reports/gates.json` (or equivalent):  
- `data/prov/<run-id>.jsonld` (or equivalent):  
- `releases/<tag or run>/build-info.json` + `checksums.sha256`:  

---

## 🧭 Gate snapshot (fill this in)

> [!TIP]
> “Green checks” are CI’s job. This section is for **review speed**: where should a reviewer look for evidence?

| Gate / evidence | Required when… | Evidence path / link (preferred) | Notes |
|---|---|---|---|
| ✅ Lint + unit tests | always |  |  |
| ✅ Typecheck | typed surface exists |  |  |
| 🔎 Data QA (schema/null/ranges/geo-validity) | touches `data/**` or pipelines |  |  |
| 🔎 Catalog QA (STAC/DCAT quick) | touches catalogs or publishable data |  |  |
| 🧾 Metadata validate (schema/profile) | touches schemas/catalog tooling |  |  |
| 🧬 PROV present + complete | publishes/changes datasets, analyses, model outputs |  |  |
| 🧩 Contract diff (API/graph/story templates) | touches any contract surface |  | link to diff / artifact |
| 🧑‍⚖️ Policy gate (OPA/Conftest) | touches governed surfaces |  |  |
| 📈 Perf evidence (p95, FPS, query plan) | touches hot paths / DB / WebGL |  |  |
| 🔐 Security scans | touches deps/auth/policies/workflows |  | CodeQL/SAST/dep scan |
| 📦 Build info + checksums | any promoted artifact / release-ish change |  |  |
| 🧾 SBOM | release lane / images |  |  |
| 🖊️ Attestation | release lane / promoted artifacts |  |  |

---

## 🎯 Type of change

- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 🧹 Refactor / cleanup (no behavior change)
- [ ] ⚡ Performance improvement
- [ ] 🔐 Security hardening
- [ ] 🗄️ Data / database change (schemas, migrations, catalog metadata)
- [ ] 🗺️ GIS / remote sensing / mapping change
- [ ] 🕸️ Graph / ontology / knowledge modeling change
- [ ] 🤖 AI/ML change (training, inference, prompts, evaluation)
- [ ] 🧪 Statistics / experimental results / analytics change
- [ ] 🧫 Scientific modeling / simulation / optimization change
- [ ] 📝 Documentation / SOP / research workflow change
- [ ] 🧰 DevOps / CI / Docker / infra change
- [ ] 💥 Breaking change (requires coordination + versioning plan)

---

## 🧭 Extension category (A–E)

> [!TIP]
> Helps reviewers apply the right mental model (and catch missing pipeline touches).

- [ ] (A) 🗺️ New data domain / dataset
- [ ] (B) 🤖 New AI-generated evidence / analysis artifact (treat as “evidence artifact”)
- [ ] (C) 🕸️ New graph entity / relationship / ontology change
- [ ] (D) 🔌 New API endpoint or service (contract-first)
- [ ] (E) 🌐 New UI layer / feature (must cite provenance in UI)

---

## 🚦 Promotion intent (important)

**Does this PR intend to promote/publish anything?**
- [ ] ❌ No (dev-only, internal refactor, docs-only, etc.)
- [ ] ✅ Yes (data/catalog/model/story/release artifact promotion)

If **Yes**, list the promotion surface(s):
- [ ] 🗺️ Dataset publish (processed assets + STAC/DCAT/PROV)
- [ ] 🕸️ Graph ingest/promote (IDs/ontology + import artifacts)
- [ ] 🔌 API deploy boundary change (contract-first)
- [ ] 🌐 UI deploy (viewer/build)
- [ ] 🎬 Story Node publish (draft → published)
- [ ] 📦 Container image publish (GHCR)
- [ ] 🏷️ Release packaging (tagged)

---

## 🧯 Risk & compatibility

**Risk level**
- [ ] 🟢 Low (localized, easy rollback)
- [ ] 🟡 Medium (touches contracts/catalogs/hot paths)
- [ ] 🔴 High (migrations, publish lanes, widespread behavior change)

**Compatibility / migration required?**
- [ ] No migration needed
- [ ] 🗄️ Data migration needed (describe below)
- [ ] 🔌 API clients may break (describe below + versioning plan)
- [ ] 🏷️ Graph schema/ontology migration needed (describe below)
- [ ] 🚩 Feature flag / staged rollout recommended

**Feature flag (if any):** `FLAG_NAME_HERE`  
**Rollback lever:** (revert PR / disable flag / rollback migration / redeploy previous image / unpublish catalog)  

**Migration notes (if any):**
- Forward plan:  
- Backfill plan:  
- Rollback plan:  
- Time/compute cost:  

---

## 🧩 Scope / pipeline stage(s) touched

> [!IMPORTANT]
> Touching upstream stages affects everything downstream. If you change ETL/catalog/graph, assume UI/story/focus impact until proven otherwise.

Check all that apply (use canonical homes first; legacy paths only if still present):

### 📥 Sources + ETL
- [ ] 📁 `src/pipelines/**` (ETL jobs / transformations)
- [ ] 📁 `tools/**` (validators, CLI utilities)
- [ ] 📁 `data/<domain>/raw/**` (new raw inputs / snapshots)
- [ ] 📁 `data/<domain>/work/**` (intermediate outputs)
- [ ] 📁 `data/<domain>/processed/**` (publish-ready outputs)

### 🗂️ Catalogs + provenance
- [ ] 📁 `data/catalog/stac/**` (STAC items/collections)
- [ ] 📁 `data/catalog/dcat/**` (DCAT discovery layer)
- [ ] 📁 `data/prov/**` (PROV bundles)
- [ ] 📁 `schemas/**` (JSON Schemas / profiles)

### 🕸️ Graph
- [ ] 📁 `src/graph/**` (ontology bindings, ingest, Cypher migrations)
- [ ] 📁 `data/graph/**` (imports/exports/manifests)

### 🔌 API boundary
- [ ] 📁 `src/server/**` (REST/GraphQL services)
- [ ] 📁 `src/server/contracts/**` (OpenAPI/GraphQL/schema contracts)
- [ ] 📁 `api/**` (legacy / transitional, if applicable)

### 🌐 UI
- [ ] 📁 `web/**` (viewer, MapLibre/WebGL, assets)

### 🎬 Story + Focus
- [ ] 📁 `docs/reports/story_nodes/**` (draft/published + assets)
- [ ] 📁 `docs/reports/focus_mode/**` (if present)

### 🧪 Methods & Computational Experiments (MCP)
- [ ] 📁 `mcp/**` (runs, experiments, notebooks, model cards)

### 📦 Releases
- [ ] 📁 `releases/**` (build-info, checksums, SBOM, attestations)

### 🤖 Control plane
- [ ] 📁 `.github/workflows/**`
- [ ] 📁 `.github/actions/**`
- [ ] 📁 `tools/validation/policy/**` (OPA/Rego policies)

---

## 🔗 Related issues / context

Closes: <!-- #123 -->  
Related: <!-- #456, discussion link, doc link -->  

**Optional context links**
- 🧱 Design doc / ADR:  
- 🧾 SOP / MCP protocol:  
- 🗺️ Dataset card / layer registry:  
- 🕸️ Ontology docs / shape constraints:  
- 🤖 Policy/gate reference:  

---

## 🧱 Design & architecture notes (contracts + clean boundaries)

> [!TIP]
> We favor layered, interface-driven boundaries: domain logic shouldn’t “know” SQL/HTTP details.

**What layer(s) changed?**
- [ ] 🧩 Domain entities / core models
- [ ] 🧠 Use cases / application services
- [ ] 🔁 Interfaces (ports)
- [ ] 🔌 Adapters (DB/web/external services)
- [ ] 🏗️ Infrastructure (frameworks, DB, cloud, containers)

**Contracts touched (list what changed)**
- 🔌 OpenAPI / GraphQL:  
- 🧾 STAC fields / extensions / item IDs:  
- 🗃️ DCAT dataset/distributions:  
- 🧬 PROV shape / run bundle expectations:  
- 🕸️ Ontology / graph IDs / relationship shapes:  
- 🎬 Story Node template / schema:  
- 🌐 UI layer registry / telemetry schema (if any):  

**Stable identifier notes (if applicable)**
- New IDs introduced:  
- Any ID migrations / redirects:  
- Back-compat story for existing IDs:  

**Reviewer focus (where to look)**
- Key files:  
- Non-obvious logic:  
- Known limitations:  

---

## 🤖 If this PR was produced by automation / agents (fill only if applicable)

> [!NOTE]
> KFM automation follows the WPE pattern (👀 Watcher → 🧠 Planner → 🛠️ Executor).  
> Automation may prepare PRs and evidence, but humans still own merge/publish decisions.

- **Automation name:** (e.g., `kfm-sim-run`, “catalog-refresh bot”, etc.)  
- **Idempotency key / run ID:**  
- **Seed + virtual time (if used):**  
- **Plan file:** `📄 plan.yml` (path)  
- **Evidence bundle output:** (folder/path)  
- **Kill-switch status at run time:** `on/off`  

Attach or link:
- [ ] `📄 plan.yml`
- [ ] `📄 reports/gates.json` (or equivalent)
- [ ] `🧬 data/prov/<run-id>.jsonld` (or equivalent)
- [ ] `📦 build-info.json` + `🔒 checksums.sha256`
- [ ] `📦 sbom.*` and `🖊️ attestations/*` (if release/publish)

---

## 🧑‍⚖️ Governance & policy gate (required when making claims or touching governed surfaces)

> [!IMPORTANT]
> If you touch **data/catalogs/story/docs/workflows**, assume policy gates apply.  
> Outputs cannot be **less restricted** than inputs (classification + sovereignty propagate).

**Max input classification touched:** `public | internal | confidential | restricted | unknown`  
**Output classification (must be ≥ strictest input):** `public | internal | confidential | restricted`  
**Redaction mode:** `strict | balanced | off (must justify)`  

**Sensitive location handling**
- [ ] Not applicable
- [ ] Applicable — generalized or redacted (describe precision tier below)

**Location precision tier (if applicable):** `exact | neighborhood | county/region | grid/index | redacted`

**Policy gate evidence**
- Report path/link:  
- Policies triggered (if known):  
  - [ ] 🧾 License allowlist
  - [ ] 🔗 URL allowlist / link safety
  - [ ] 🧬 PROV required
  - [ ] 🗂️ STAC/DCAT required fields
  - [ ] 🧭 Classification propagation
  - [ ] 🗺️ Sensitive locations
  - [ ] 🔐 Workflows least privilege
  - [ ] 📌 Actions pinning

<details>
<summary><strong>🧾 Policy pack location (for reference)</strong></summary>

```text
🛠️ tools/validation/policy/
├─ 📄 README.md
├─ 📁 rego/
│  ├─ 📁 common/
│  │  ├─ 📄 helpers.rego
│  │  ├─ 📄 license_allowlist.rego
│  │  └─ 📄 url_allowlist.rego
│  ├─ 📁 catalogs/
│  │  ├─ 📄 stac_required.rego
│  │  ├─ 📄 dcat_required.rego
│  │  ├─ 📄 prov_required.rego
│  │  └─ 📄 link_safety.rego
│  ├─ 📁 governance/
│  │  ├─ 📄 classification_propagation.rego
│  │  ├─ 📄 sensitive_locations.rego
│  │  └─ 📄 attribution.rego
│  ├─ 📁 supply_chain/
│  │  ├─ 📄 workflows_least_privilege.rego
│  │  └─ 📄 actions_pinning.rego
│  └─ 📄 bundles.rego
└─ 📁 tests/
   ├─ 📄 *_test.rego
   └─ 📁 samples/
      ├─ 📁 good/
      └─ 📁 bad/
```
</details>

---

## 🧰 Domain-specific checklists (optional, but review-speed)

> [!TIP]
> Only fill the sections that match your PR type. These are here to prevent “silent regressions” in scientific rigor, GIS correctness, performance, and trust.

<details>
<summary><strong>🗺️ GIS / Remote Sensing / Mapping checklist</strong></summary>

- [ ] CRS/Projection is explicit and correct (and consistent across assets)
- [ ] Geometry validity checks pass (self-intersections, empty geoms, invalid rings)
- [ ] Raster outputs are cloud-optimized where applicable (COG/overviews/tiling strategy)
- [ ] STAC assets include correct roles, media types, and spatial/temporal extents
- [ ] Map design sanity: legend, units, scale, labels, symbology readability (incl. colorblind safety)
- [ ] Sensitive locations: precision tier set + enforced in UI (no “zoom leak”)
- [ ] If routing/network analysis: edge costs/units documented, reproducible query or script attached

</details>

<details>
<summary><strong>🕸️ Graph / Ontology checklist</strong></summary>

- [ ] Ontology/shape change documented + migration provided (Cypher or import script)
- [ ] Stable IDs introduced (no meaning-encoded IDs unless explicitly approved)
- [ ] Relationship semantics are clear (directionality, cardinality expectations)
- [ ] No orphan node types / dangling relationships after ingest
- [ ] Query limits considered (depth, pagination, expensive traversals)
- [ ] Story Nodes reference graph entities by stable ID where applicable

</details>

<details>
<summary><strong>🔌 API contract checklist</strong></summary>

- [ ] Contract-first: OpenAPI/GraphQL updated **before** implementation drift
- [ ] Back-compat preserved (or version bump + migration notes provided)
- [ ] Pagination + filtering semantics documented (avoid unbounded responses)
- [ ] Rate limiting / abuse controls considered for public endpoints
- [ ] Security: input validation, authz checks, and error hygiene reviewed
- [ ] DB access: parameterized queries only (no string concat)

</details>

<details>
<summary><strong>🌐 UI / WebGL / Responsive checklist</strong></summary>

- [ ] Responsive behavior verified (mobile/tablet/desktop breakpoints)
- [ ] Accessibility pass (keyboard nav, labels, contrast, focus states)
- [ ] WebGL perf sanity: no obvious shader errors, memory spikes, or runaway draw calls
- [ ] Asset hygiene: images compressed appropriately; formats chosen intentionally (PNG/JPEG/WebP/GIF)
- [ ] Every layer/UI visualization links back to provenance (STAC/DCAT IDs visible via UI affordance)

</details>

<details>
<summary><strong>🎬 Story Nodes / Focus Mode checklist</strong></summary>

- [ ] Story Node follows template + is machine-ingestible
- [ ] Every claim-bearing statement has citation(s) (catalog IDs preferred)
- [ ] Fact vs interpretation is clearly separated (and labeled if AI-assisted)
- [ ] Graph entity references are stable IDs (not fragile names)
- [ ] Focus Mode: no unsourced content, no sensitive location side-channel
- [ ] AI outputs (if any): opt-in, labeled, and bounded by evidence + governance rules

</details>

<details>
<summary><strong>🧪 Statistics / Regression / Bayesian checklist</strong></summary>

- [ ] Hypothesis and design are explicit (what is being tested and why)
- [ ] Randomization / leakage risks addressed (esp. time/space leakage)
- [ ] Effect sizes + uncertainty reported (CI/credible intervals where applicable)
- [ ] Regression diagnostics done (residuals, heteroscedasticity, multicollinearity, outliers)
- [ ] Multiple comparisons / p-hacking risks considered if many tests
- [ ] Posterior predictive checks (if Bayesian) or equivalent model adequacy checks

</details>

<details>
<summary><strong>🧫 Scientific modeling / simulation / optimization checklist</strong></summary>

- [ ] Verification: numerical correctness checks / unit tests / conservation checks
- [ ] Validation: compared against measured/known data where applicable
- [ ] Sensitivity analysis performed or justified as out-of-scope
- [ ] Uncertainty quantification: what’s uncertain and how it propagates
- [ ] Solver settings + convergence criteria captured (tolerances, mesh, step sizes)
- [ ] Reproducibility: seeds, configs, and run metadata captured in PROV

</details>

<details>
<summary><strong>🗄️ Database / performance / scale checklist</strong></summary>

- [ ] Query plans captured for hot queries (and improved if regression suspected)
- [ ] Index changes explained (why, expected workload)
- [ ] Avoid `SELECT *` in production surfaces; return only needed columns
- [ ] Migrations include forward + rollback, with lock/timeout considerations
- [ ] Concurrency considerations noted (deadlocks, transaction isolation, background workers)
- [ ] p95/p99 latency and memory impact measured if performance-sensitive

</details>

<details>
<summary><strong>🔐 Security checklist</strong></summary>

- [ ] Threat model updated if introducing new exposure (endpoint, workflow, credential path)
- [ ] Secrets hygiene: no secrets committed; `.env.example` updated if needed
- [ ] Dependency changes reviewed (supply chain + licensing implications)
- [ ] Workflows pinned (actions versions) and least-privilege maintained
- [ ] Input validation and output escaping reviewed (esp. markdown/HTML rendering)

</details>

---

## 📚 Project reference shelf (optional)

<details>
<summary><strong>📚 Why these checklists exist (project library)</strong></summary>

Use this shelf when you’re unsure what “good” looks like for a given domain:

- 🧭 **KFM system invariants & structure**
  - *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation*
  - *Master Guide v13 (Draft)* + *Markdown Guide v13* + *Comprehensive Markdown Guide*

- 🧬 **Governance, ethics, sovereignty, and policy**
  - *Data Spaces* (policy + access control patterns)
  - *Introduction to Digital Humanism*
  - *On the path to AI Law’s prophecies…*
  - *Principles of Biological Autonomy* (systems thinking / agent boundaries)

- 🧪 **Scientific rigor**
  - *Scientific Modeling and Simulation (NASA-grade)*
  - *Understanding Statistics & Experimental Design*
  - *Regression Analysis with Python* + *Linear Regression slides*
  - *Graphical Data Analysis with R*
  - *Think Bayes*

- 🗺️ **GIS / mapping / remote sensing**
  - *Python Geospatial Analysis Cookbook*
  - *Making Maps (GIS design)*
  - *Cloud-Based Remote Sensing with Google Earth Engine*
  - *Archaeological 3D GIS*
  - *Mobile Mapping: Space, Cartography and the Digital*

- 🕸️ **Graphs & optimization**
  - *Spectral Geometry of Graphs*
  - *Generalized Topology Optimization for Structural Design*

- 🗄️ **Data management & performance**
  - *Database Performance at Scale*
  - *Scalable Data Management for Future Hardware*
  - *PostgreSQL Notes for Professionals*

- 🌐 **Web / UI / graphics**
  - *Responsive Web Design with HTML5 and CSS3*
  - *WebGL Programming Guide*
  - *Compressed Image File Formats (JPEG/PNG/GIF/etc.)*

- 🛡️ **Security & secure engineering**
  - *Ethical Hacking and Countermeasures*
  - *Gray Hat Python*
  - *Concurrent Real-Time & Distributed Programming in Java* (race conditions / correctness)

- 🧰 **General programming references (grab-bag)**
  - *A programming Books*, *B-C*, *D-E*, *F-H*, *I-L*, *M-N*, *O-R*, *S-T*, *U-X* (cross-language patterns, architecture, ops, tooling)

</details>

---

## ✅ Final self-check (before requesting review)

- [ ] PR summary explains **what + why** in ≤ 3 sentences
- [ ] Repro steps work from a clean checkout
- [ ] Evidence links provided for any claim-bearing change
- [ ] If publish intent: STAC/DCAT/PROV present and validated
- [ ] Contracts updated first (schemas/OpenAPI/ontology/story templates)
- [ ] Governance fields filled when touching governed surfaces