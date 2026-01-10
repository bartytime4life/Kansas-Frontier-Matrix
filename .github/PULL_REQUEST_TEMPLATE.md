# 🚀 Pull Request

<!--
📄 File: .github/PULL_REQUEST_TEMPLATE.md
🗓️ Last updated: 2026-01-10
🧭 Baseline: KFM‑MDP v11.x • Master Guide v13 (draft)
-->

> [!NOTE]
> **Keep it reviewable:** 2–3 sentences + reproducible steps + evidence links for any claim-bearing change (data/models/story).

> [!IMPORTANT]
> ⛓️ **Pipeline order is absolute:** **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
> If it isn’t **machine-validated + cataloged + provenance-linked**, it isn’t publishable in KFM.

> [!IMPORTANT]
> 🧾 **Contracts over vibes:** OpenAPI, STAC/DCAT/PROV schemas, graph IDs/ontology shapes, and Story Node templates are **contracts**.  
> If a contract drifts, CI should fail before anything ships.

---

## 📌 Summary (what + why)

<!-- 1–3 sentences. Assume the reviewer is seeing this cold. -->
**Problem / context:**  

**What changed (solution):**  

**Why it matters (impact):**  

**User-visible outcome (if any):**  

**Release note (optional, 1 line):**  

---

## 🧭 Gate snapshot (fill this in)

> [!TIP]
> “Green checks” are CI’s job. This section is for **review speed**: where should a reviewer look for evidence?

| Gate / evidence | Required when… | Evidence path / link (preferred) | Notes |
|---|---|---|---|
| ✅ Lint + unit tests | always |  |  |
| ✅ Typecheck | when typed surface exists |  |  |
| 🔎 Catalog QA (STAC/DCAT quick) | touches 🗺️ `🗂️ data/**` or catalogs |  |  |
| 🧾 Metadata validate (schema/profile) | touches catalogs/schemas |  |  |
| 🧬 PROV present + complete | publishes/changes datasets, analyses, model outputs |  |  |
| 🧑‍⚖️ Policy gate (OPA/Conftest) | touches governed surfaces (data/docs/story/workflows) |  |  |
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

---

## 🧩 Scope / pipeline stage(s) touched

> [!IMPORTANT]
> Touching upstream stages affects everything downstream. If you change ETL/catalog/graph, assume UI/story/focus impact until proven otherwise.

Check all that apply:

### 📥 Sources + ETL
- [ ] 📁 `🧰 tools/` (pipelines, validators, CLI)
- [ ] 📁 `📥 data/raw/**` (new raw inputs / snapshots)
- [ ] 📁 `🧪 data/work/**` (intermediate outputs)
- [ ] 📁 `🗄️ data/processed/**` (publish-ready outputs)

### 🗂️ Catalogs + provenance (contracts)
- [ ] 📁 `🧾 data/stac/**` (STAC items/collections)
- [ ] 📁 `🗃️ data/catalog/dcat/**` (DCAT discovery layer)
- [ ] 📁 `🧬 data/prov/**` (PROV bundles)
- [ ] 📁 `🧩 schemas/**` (JSON Schemas / profiles)

### 🕸️ Graph
- [ ] 📁 `🕸️ graph/**` or `🧾 docs/ontology/**` (ontology/IDs/contracts)
- [ ] 📁 `🧾 data/graph/**` (imports/exports/manifests)

### 🔌 API boundary
- [ ] 📁 `🔌 api/**` (services, workers, policies)
- [ ] 📁 `📜 api/contracts/**` (OpenAPI/GraphQL/schema contracts)

### 🌐 UI
- [ ] 📁 `🌐 web/**` (viewer, MapLibre/WebGL, assets)

### 🎬 Story + Focus
- [ ] 📁 `🎬 docs/reports/story_nodes/**` (draft/published + assets)
- [ ] 📁 `🧠 docs/reports/focus_mode/**` (if present)

### 🤖 Control plane
- [ ] 📁 `🤖 .github/workflows/**`
- [ ] 📁 `🧩 .github/actions/**`
- [ ] 📁 `🧑‍⚖️ tools/validation/policy/**` (OPA/Rego policies)

---

## 🔗 Related issues / context

Closes: <!-- #123 -->  
Related: <!-- #456, discussion link, doc link -->  

**Optional context links**
- 🧱 Design doc / ADR:  
- 🧾 SOP / MCP protocol:  
- 🗺️ Dataset card / layer registry:  
- 🤖 Policy/gate reference:  

---

## 🧱 Design & architecture notes (contracts + clean boundaries)

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
