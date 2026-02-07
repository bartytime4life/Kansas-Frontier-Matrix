<!-- CONTRIBUTING.md | Kansas Frontier Matrix (KFM) -->
<!-- Last updated: 2026-02-06 (America/Chicago) -->

# 🤝 Contributing to Kansas Frontier Matrix (KFM) 🌾🗺️  
### _Evidence-first. Contract-first. Governance-aware. Built to withstand scrutiny._ 🧾🧱

![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue.svg)
![Docs](https://img.shields.io/badge/docs-Markdown%20first-informational.svg)
![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%2B%20DCAT%20%2B%20PROV-7d3c98.svg)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-0aa.svg)
![Contract-first](https://img.shields.io/badge/contracts-first-success.svg)
![Trust-first](https://img.shields.io/badge/trust-first-evidence%20%2B%20contracts-success.svg)
![API](https://img.shields.io/badge/API-REST%20%2B%20GraphQL-4b9.svg)
![Geo](https://img.shields.io/badge/Geo-PostGIS%20%2B%20STAC%20%2B%20Tiles-6a5acd.svg)

**Timezone:** America/Chicago 🕰️  
**Maintainer note:** KFM is not a “just ship it” repo — it’s a **trust system**. Every merge should increase auditability. 🔍

---

## 🔗 Quick links

- 🧾 **Open an Issue**: `./.github/ISSUE_TEMPLATE/` (if present)
- 🔁 **Open a PR**: `./.github/PULL_REQUEST_TEMPLATE.md` (if present)
- 🔐 **Security**: `./SECURITY.md`
- 📄 **License**: `./LICENSE` (Apache-2.0)
- 📚 **Docs**: `./docs/`
- 🧰 **Schemas**: `./schemas/`
- 🗃️ **Data + catalogs**: `./data/`

> [!TIP]
> If you’re new: aim for **docs**, **tests**, **validators**, or a **small data QA improvement** first ✅  
> KFM rewards careful incrementalism.

---

## 🚦 Non‑negotiables

> [!IMPORTANT]
> KFM is **contract-first** ✅ + **evidence-first** 🧾  
> Contributions must respect the **non‑negotiable pipeline order**:
>
> **ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode** 🔒✅  
> _No shortcuts. No bypasses._  
> This “truth path” is core to the platform’s design. :contentReference[oaicite:0]{index=0}

### 🧭 Pipeline at a glance (trust path)
```mermaid
flowchart LR
  A[🧪 ETL / Ingest] --> B[🗂️ STAC + DCAT + PROV]
  B --> C[🕸️ Graph Build / Ontology]
  C --> D[🛡️ API Boundary + Policy]
  D --> E[🌐 UI + Visualization]
  E --> F[📚 Story Nodes]
  F --> G[🎯 Focus Mode (advisory)]
```

### 🧱 What “contract-first” means here
- **Schemas + API shapes are first-class artifacts** (reviewed like code)
- Breaking changes require **migrations + tests + docs**
- UI changes that alter meaning require **provenance surfaced in the UI** (layer metadata, citations, lineage)

### 🧾 What “evidence-first” means here
Nothing is “publishable” unless it is traceable:
- 🗂️ **STAC** (assets + spatial metadata)
- 🏷️ **DCAT** (dataset discovery + description)
- 🧬 **PROV** (lineage: inputs → activity → outputs → agents)

### 🤖 Focus Mode safety stance (non-negotiable)
- **Advisory-only** (never takes autonomous actions)
- **Closed-book runtime** (no ad-hoc browsing/tools in runtime assistant mode)
- **No citation, no answer** (uncited claims must be refused)

---

## 🧭 Table of contents

- [👋 Ways to contribute](#-ways-to-contribute)
- [🧑‍🚀 Start here](#-start-here)
- [🗂️ Repo map](#️-repo-map)
- [🚀 Dev setup](#-dev-setup)
- [🧪 Quality gates](#-quality-gates)
- [🧩 Change impact matrix](#-change-impact-matrix)
- [🗃️ Data + catalogs](#️-data--catalogs-stacdcatprov)
- [🕸️ Graph + ontology](#️-graph--ontology)
- [🛡️ APIs + contracts](#️-apis--contracts)
- [🎨 Frontend + visualization](#-frontend--visualization)
- [📚 Story Nodes + governed docs](#-story-nodes--governed-docs)
- [🤖 AI/analysis outputs as evidence](#-aianalysis-outputs-as-evidence)
- [🧭 Governance, sovereignty, sensitive data](#-governance-sovereignty-sensitive-data)
- [🔐 Security + responsible disclosure](#-security--responsible-disclosure)
- [🧾 Git workflow + PR standards](#-git-workflow--pr-standards)
- [🏷️ Issue labels + triage](#️-issue-labels--triage)
- [📚 Reference shelf](#-reference-shelf)

---

## 👋 Ways to contribute

Pick a lane that fits your time + skills — all lanes matter 🌱:

- 🐛 **Bug fixes** (logic, data QA, UI regressions, performance)
- ✨ **Features** (domain modules, new layers, export/report flows)
- 🗺️ **GIS layers & ETL** (ingest, transform, validate, publish)
- 🛰️ **Remote sensing** (indices, cloud masking QA, change detection)
- 🤖 **ML/AI** (evaluation, monitoring, uncertainty, inference integration)
- 🧬 **Modeling & simulation** (V&V, calibration, sensitivity analysis)
- 🕸️ **Graph/ontology** (entity types, relations, constraints, migrations)
- 🎨 **Frontend** (React, MapLibre/WebGL, responsive/a11y, UX polish)
- 🗄️ **Data management** (Postgres/PostGIS, migrations, indexing)
- 🔐 **Security & reliability** (hardening, policy checks, testability)
- 📚 **Documentation** (runbooks, governed docs, Story Nodes)
- 🧪 **Research artifacts** (spikes, benchmarks, trade studies)

---

## 🧑‍🚀 Start here

### ✅ The “good first PR” menu (low risk, high value)
- Add missing **tests** for an existing behavior ✅
- Tighten a **schema** (and update fixtures + docs) 🧾
- Add a **validator** script for STAC/DCAT/PROV output 🧬
- Improve a **runbook** (setup, deploy, troubleshoot) 📚
- Improve **UI a11y** (keyboard, labels, contrast, focus states) ♿

### 🧭 The “safe PR shape”
> [!TIP]
> Prefer PRs that change **one layer** at a time (A or B or C…) unless you’re explicitly shipping an end‑to‑end feature.  
> Big features should land as: **scaffold → behavior → polish** 🏎️💨

---

## 🗂️ Repo map

> [!NOTE]
> KFM aims for **one canonical home per subsystem** to avoid drift and shadow copies 🧱

### 🧭 Canonical homes (target layout)
```text
📦 repo-root/
├─ 🗃️ data/                         # raw/work/processed + catalogs (STAC/DCAT/PROV)
│  ├─ raw/                           # source inputs (treat as read-only)
│  ├─ work/                          # intermediate artifacts
│  ├─ processed/                     # publishable outputs
│  ├─ stac/                          # collections/ + items/
│  ├─ catalog/dcat/                  # DCAT (JSON-LD)
│  └─ prov/                          # PROV bundles (lineage)
├─ 📚 docs/                          # governed docs, ADRs, runbooks, narratives
│  ├─ templates/                     # universal / story node / API contract templates
│  ├─ governance/                    # ethics, sovereignty, CARE/FAIR review gates
│  ├─ architecture/                  # blueprints + ADRs
│  └─ reports/story_nodes/           # draft/ + published/ (governed narratives)
├─ 🧾 schemas/                       # JSON Schemas (stac/dcat/prov/storynodes/ui/telemetry)
├─ 🧠 src/
│  ├─ pipelines/                     # ETL + transforms + catalog writers
│  ├─ graph/                         # graph build + ontology bindings + ingest
│  └─ server/                        # API boundary + policy + redaction + contract enforcement
├─ 🌐 web/                           # React + MapLibre (+ optional Cesium)
├─ 🧪 tests/                         # unit + integration + contract + e2e tests
├─ 🧰 tools/                         # devtools, validators, scripts (if present)
├─ 🐳 docker/                        # compose, images, dev services (if present)
├─ 📦 releases/                      # signed datasets/artifacts metadata (if present)
├─ 📄 LICENSE                        # Apache-2.0
├─ 📄 SECURITY.md                    # responsible disclosure
├─ 📄 CITATION.cff                   # citation metadata
└─ 📄 CONTRIBUTING.md                # you are here 👋
```

---

## 🚀 Dev setup

> [!IMPORTANT]
> If you’re editing anything that crosses boundaries (data→graph→API→UI), prefer a Docker-backed integration run 🐳

### 🐳 Option A — Docker-first (recommended)
```bash
# 1) copy env file (if present)
cp .env.example .env

# 2) build + start
docker compose up --build

# 3) run tests (use what exists in-repo)
pytest -q
npm test
```

### 🧪 Option B — Local-first (Python + Node)

#### 1) Python (typical)
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"   # if pyproject.toml is used
```

#### 2) Node (if `web/` exists)
```bash
npm ci
# or: pnpm i / yarn
```

#### 3) Run tests
```bash
pytest
npm test
```

> [!TIP]
> For Node workflows (tooling/build/test), prefer **clean installs** (`npm ci`) for reproducibility.  
> Node setup and CLI/REPL concepts are covered in the project’s JS references. :contentReference[oaicite:1]{index=1}

---

## 🧪 Quality gates

### ✅ Baseline Definition of Done (DoD)
- ✅ Tests updated/added (unit first; integration when boundaries change)
- ✅ Determinism preserved (seeds/configs/tolerances for ML/sim)
- ✅ Catalog + provenance updated (STAC/DCAT/PROV) for publishable artifacts
- ✅ Contracts updated + validated for API/UI changes
- ✅ Docs updated (runbooks, schema notes, Story Nodes, examples)
- ✅ No secrets/PII committed
- ✅ Governance triggers handled (FAIR+CARE + sovereignty)

### 🧰 “Trust checks” by boundary (fast mental model)
| Boundary crossed | Minimum proof |
|---|---|
| 🗃️ Data → Catalog | STAC/DCAT/PROV updated + validated |
| 🗂️ Catalog → Graph | graph ingest tests + migration plan |
| 🕸️ Graph → API | contract tests + redaction/policy checks |
| 🛡️ API → UI | provenance surfaced + e2e smoke tests |
| 📚 Story → Focus | citations complete + governance review |

> [!TIP]
> If CI exists, treat it as a **merge gate**, not a suggestion. If something is flaky, fix the flake — don’t bypass it. 🧯

---

## 🧩 Change impact matrix

KFM changes usually touch multiple layers. Use this to avoid “half-changes” that break trust. 🧱🧾

| Change type | Examples | You must also update |
|---|---|---|
| **(A) Data / domain source** 🗃️ | new dataset, new imagery, new archive | STAC/DCAT/PROV, licensing, artifact/DVC pointers |
| **(B) Pipeline / ETL** 🧪 | transform change, reprojection, QA | determinism, fixtures, provenance updates |
| **(C) Graph / ontology** 🕸️ | new node/edge types, mappings | migrations, constraints, integrity checks |
| **(D) API / service** 🛡️ | new endpoint, new GraphQL field | contract-first, redaction/policy, contract tests |
| **(E) UI layer / feature** 🌐 | map overlay, story viewer, focus panel | provenance popups, CARE safeguards, e2e tests |

> [!NOTE]
> KFM is explicitly designed with a **layered architecture** and strict “truth path” enforcement (UI does not bypass API; policy gates exist at boundaries). :contentReference[oaicite:2]{index=2}

---

## 🗃️ Data + catalogs (STAC/DCAT/PROV)

This is the **trust spine** of KFM. If you add or change data, keep it traceable. 🧾🗂️

### ✅ Required data lifecycle layout
- `data/raw/<domain>/` — source inputs (read-only mindset)
- `data/work/<domain>/` — intermediate artifacts
- `data/processed/<domain>/` — publishable outputs

### ✅ Required boundary artifacts
- `data/stac/collections/` + `data/stac/items/`
- `data/catalog/dcat/` (JSON‑LD catalog entries)
- `data/prov/` (lineage bundles)

### 📦 Large files: artifacts first (avoid git bloat)
> [!IMPORTANT]
> Don’t “sneak” large binaries into git. Track them via the repo’s approved artifact/DVC/registry pattern.

If your change introduces large rasters/tiles/point clouds:
- Prefer cloud-friendly formats: **COG**, **GeoParquet**, **PMTiles**, etc. (where applicable)
- Store data as **content-addressed artifacts** (hashes/pointers) rather than committed binaries
- Consider signing/attesting artifacts if the repo uses supply-chain tooling

### 🧾 Adding a new domain module (checklist)
- [ ] Create folders: `data/raw/<domain>/`, `data/work/<domain>/`, `data/processed/<domain>/`
- [ ] Add/extend pipelines under `src/pipelines/<domain>/`
- [ ] Generate STAC/DCAT/PROV for publishable outputs
- [ ] Extend schemas under `schemas/` if you introduce new fields (no one-off keys)
- [ ] Add a runbook: `docs/data/<domain>/README.md`
- [ ] Add tests: unit + contract + (optional) integration
- [ ] Run validation in CI (schemas, catalogs, provenance)

---

## 🕸️ Graph + ontology

KFM’s graph is where “data becomes knowledge.” Treat schema/ontology edits like database migrations. 🧠➡️🕸️

### ✅ Requirements for graph changes
- **Stable IDs** for entities and relationships
- **Migration plan** (forward + rollback where feasible)
- **Integrity constraints** (avoid silent drift)
- **Fixtures** that prove expected traversals and edge cases

### 🧪 Minimum tests to add
- Invariants: symmetry, conservation, monotonicity (as applicable)
- Convergence/termination bounds (for solvers/optimizers)
- Migration verification (pre/post assertions)

---

## 🛡️ APIs + contracts

### ✅ Contract-first workflow
1) Define/update contracts first (OpenAPI / GraphQL schemas) 🧾  
2) Implement server behavior (policy + redaction included) 🛡️  
3) Add contract tests + integration tests (as needed) 🧪  
4) Update docs + examples 📚

### 🔒 Policy boundary expectations
- The **UI must not** fetch raw evidence artifacts directly
- All user-facing consumption should go through the API boundary for:
  - redaction/classification
  - audit logging
  - consistent semantics

> [!NOTE]
> Policy gate concepts (e.g., middleware enforcement) are core to the platform design. :contentReference[oaicite:3]{index=3}

---

## 🎨 Frontend + visualization

KFM UI is a trust surface: it must render meaning **and** provenance. 🗺️🧾

### ✅ UX + accessibility (a11y) baseline
- Keyboard navigation for critical flows ♿
- Labels/aria for controls and map widgets
- Don’t encode meaning by color alone (maps/charts)
- Mobile + desktop friendly layouts (responsive)

> [!TIP]
> Great UI work starts with **requirements + flows** (not code-first).  
> Use light “comps”/wireframes when changing navigation, layouts, or workflows. :contentReference[oaicite:4]{index=4}

### 🧊 WebGL + map performance hygiene
- Progressive loading (don’t block main thread)
- Test on modest hardware
- Prefer tiling strategies for large data
- Add visual regression checks when map appearance is mission-critical

### 🖼️ Images & media (docs + UI)
- Prefer appropriately compressed formats:
  - Photos → JPEG (lossy)  
  - Diagrams/flat graphics → PNG (lossless)  
- Avoid oversized assets in git; prefer artifacts when large
- Always include attribution/licensing notes for externally sourced media

(Background on tradeoffs and formats is in the internal references.) :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

---

## 📚 Story Nodes + governed docs

Story Nodes are **governed narrative artifacts**. Focus Mode is the **highest-trust view** 🎯

### ✅ Story Nodes are machine-ingestible storytelling
A valid Story Node must:
- include provenance/citations for every claim 🧾
- reference graph entities with stable IDs 🕸️
- distinguish fact vs interpretation (especially where AI assists) 🧠

### ✅ Promotion rule (Draft → Published → Focus Mode)
Drafts/notes do **not** surface in Focus Mode. Promotion exists so:
- provenance references exist
- sensitivity handling is reviewed
- rendering expectations are defined

### 📍 Suggested Story Node layout
- Templates live in `docs/templates/` (if present)
- Drafts: `docs/reports/story_nodes/draft/`
- Published: `docs/reports/story_nodes/published/<story_slug>/`

Optional “Focus controls” block:
```yaml
focus_layers:
  - "layer_id"
focus_time: "YYYY-MM-DD"
focus_center: [-98.0000, 38.0000]
```

---

## 🤖 AI/analysis outputs as evidence

KFM treats AI/analysis outputs as **datasets**, not “magic text.” 🧾🤝

If you add:
- an ML-predicted layer
- simulation output rasters
- a statistical report
- an AI-generated summary intended for users

…you must keep it **provenance-complete** and **policy-safe**.

### ✅ Evidence artifact rules
- Store publishable outputs in `data/processed/<domain-or-project>/...`
- Catalog it (STAC/DCAT as appropriate)
- Trace it in PROV (inputs, activity, parameters/seeds, agent)
- Include uncertainty, limitations, and monitoring expectations

> [!TIP]
> “Truthful uncertainty” beats confident ambiguity. If a model is weak in a region/time, say so and document it. 🧠

---

## 🧭 Governance, sovereignty, sensitive data

KFM’s governance stance is not decorative — it’s architectural. 🧱🧭

### 🌿 CARE + FAIR (together)
- FAIR helps data be reusable and discoverable
- CARE helps ensure data use is ethical and aligned with collective benefit, authority, responsibility, and ethics

### 🧑🏽‍🤝‍🧑🏽 Indigenous data considerations (high bar)
If your contribution touches Indigenous Peoples, lands, waters, treaties, or culturally sensitive knowledge:
- Avoid “deficit framing” by default
- Prefer community engagement signals (where possible)
- Treat categories, labels, and aggregates as **culturally embedded**, not neutral
- Flag ambiguity for governance review — don’t guess

This repo aligns with Indigenous Data Sovereignty and Indigenous statistics critiques that treat data as culturally embedded, not inherently neutral. :contentReference[oaicite:7]{index=7}

### 🛰️ Geospatial privacy (always treat as sensitive until proven safe)
- Location traces and sensitive sites may require generalization/redaction
- Don’t publish precise coordinates for protected resources
- When in doubt: escalate to governance review

---

## 🔐 Security + responsible disclosure

### 🚫 Hard rules
- Never commit secrets (tokens, keys, private certs)
- Don’t upload real PII into fixtures/examples
- Use `.env` locally; keep `.env.example` safe + documented

### 🛡️ Responsible disclosure
- Follow `SECURITY.md`
- Don’t post exploit details in public issues

### 🧾 Supply-chain integrity (if enabled in repo)
- Prefer pinned dependencies / lockfiles
- Use provenance/attestation tooling if present
- Keep builds reproducible (Docker-first helps)

---

## 🧾 Git workflow + PR standards

### 🌿 Branch naming
- `feature/<short-name>`
- `fix/<short-name>`
- `docs/<short-name>`
- `chore/<short-name>`
- `data/<short-name>`

### ✅ Commit messages (Conventional Commits encouraged)
- `feat: add drought-index layer registry entry`
- `fix: correct CRS handling in ETL reprojection`
- `docs: clarify Story Node promotion rules`
- `test: add contract tests for graph query endpoint`

### 🔁 PR checklist (Definition of Done)
- [ ] Linked issue (or rationale)
- [ ] Tests added/updated
- [ ] Lint/format passes
- [ ] Docs updated (if behavior changed)
- [ ] No secrets committed
- [ ] Data provenance included (if new data/layer)
- [ ] Contracts/catalogs updated (if crossing boundaries)
- [ ] Governance/FAIR+CARE review triggered if needed

### 🧠 Review rubric (what maintainers look for)
- **Trust:** can a reviewer trace outputs to sources in <5 minutes?
- **Determinism:** can CI reproduce the result?
- **Contracts:** did we break a consumer silently?
- **Governance:** did we protect sensitive data and cultural context?
- **Performance:** does it scale beyond a laptop?

---

## 🏷️ Issue labels + triage

Recommended labels (use what the repo already has):
- `bug` 🐛
- `enhancement` ✨
- `docs` 📚
- `good first issue` 🌱
- `help wanted` 🙋
- `security` 🔐
- `data` 🗂️
- `gis` 🗺️
- `ml` 🤖
- `simulation` 🧬
- `graph` 🕸️
- `contracts` 🧾

When filing issues, include:
- expected vs actual behavior
- steps to reproduce
- logs / screenshots
- environment info (OS, python/node versions, docker version)

---

## 📚 Reference shelf

> [!NOTE]
> These are internal references used to keep KFM aligned across engineering, design, governance, and data practice.  
> Please **summarize** rather than copying large excerpts.

### 🧭 Core system + architecture
- **Kansas Frontier Matrix (KFM) – Comprehensive System Documentation** :contentReference[oaicite:8]{index=8}

### 🎨 UI, UX, and web craft
- **Professional Web Design: Techniques and Templates (5th ed.)** :contentReference[oaicite:9]{index=9}  
- **Learn to Code HTML & CSS: Develop and Style Websites** :contentReference[oaicite:10]{index=10}

### 🖼️ Media formats & compression (useful for map tiles + docs assets)
- **Compressed Image File Formats: JPEG, PNG, GIF, XBM, BMP** :contentReference[oaicite:11]{index=11}

### 🧰 JavaScript/Node toolchain literacy (web + tooling)
- **Node.js (Apress reference)** :contentReference[oaicite:12]{index=12}

### 🧭 Governance + Indigenous data sovereignty
- **Indigenous Statistics: From Data Deficits to Data Sovereignty (2nd ed., 2025)** :contentReference[oaicite:13]{index=13}

---

✅ Thanks for helping build KFM — every careful boundary line, provenance link, and test makes the system more trustworthy. 🌾🧭🧾
