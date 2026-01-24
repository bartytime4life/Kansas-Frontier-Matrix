# ♻️ Reusable GitHub Actions Workflows (KFM)

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-reusable%20workflows-2088FF?logo=githubactions&logoColor=white)
![Policy Pack](https://img.shields.io/badge/OPA%20%2B%20Conftest-Policy%20Pack-7B42BC)
![Provenance](https://img.shields.io/badge/W3C%20PROV--O-lineage%20everywhere-00A98F)
![FAIR%20%2B%20CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-governance%20gates-FFB000)
![Supply Chain](https://img.shields.io/badge/SBOM%20%2B%20Signing-supply%20chain%20security-111111?logo=sigstore&logoColor=white)

> [!IMPORTANT]
> This directory is KFM’s **CI/CD “pattern library”** 🧩 — small, reusable workflow building blocks that standardize:
> - 🔒 **Governance & policy-as-code** (fail-closed gates)
> - 🧬 **Provenance-first operations** (code + data lineage)
> - 🧪 **Test & validation discipline** (software + data pipelines)
> - 📦 **Supply-chain security** (SBOM / attestations / signing)
> - 🗺️ **Geospatial + knowledge graph integrity** (STAC/DCAT/PROV → PostGIS/Neo4j)
> - 🧠 **AI/Focus Mode reliability** (RAG regression + citation rules)

---

## 📦 What lives here

This folder contains **reusable workflows** triggered via `workflow_call` (not “top-level” CI pipelines).

📁 **Folder map**
```text
📦 .github/
  ⚙️ workflows/
    🧭 (caller workflows live here)
    ♻️ reusables/
      📝 README.md   👈 you are here
      🔒 reusable-policy-pack.yml
      🧬 reusable-provenance-pr.yml
      🧪 reusable-python-ci.yml
      🧪 reusable-node-ci.yml
      🗺️ reusable-stac-dcat-prov-validate.yml
      🧠 reusable-ai-eval.yml
      📦 reusable-build-sign-publish.yml
      🧱 reusable-graph-import-dryrun.yml
      🛰️ reusable-offline-pack.yml
      🧹 reusable-maintenance.yml
```

> [!TIP]
> Keep **caller workflows** in `.github/workflows/*.yml` **thin** (routing + job selection), and put the real work in these reusables.

---

## 🚀 Quickstart: calling a reusable workflow

A caller workflow can “import” a reusable like this:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  ui:
    uses: ./.github/workflows/reusables/reusable-node-ci.yml
    with:
      working-directory: ui
      node-version: "20"
    secrets: inherit

  api:
    uses: ./.github/workflows/reusables/reusable-python-ci.yml
    with:
      working-directory: api
      python-version: "3.12"
    secrets: inherit

  governance:
    uses: ./.github/workflows/reusables/reusable-policy-pack.yml
    with:
      policy_dir: api/scripts/policy
      targets: |
        data/**/*.json
        data/**/*.yaml
        docs/**/*.md
    secrets: inherit
```

---

## 🧠 KFM workflow philosophy (why these gates exist)

KFM is built around **“the map behind the map”** 🗺️ — every layer, story, and AI answer should remain traceable to its sources and transforms.

These reusables reflect a few core rules:

### 1) 🧬 Provenance-first (everything is an auditable event)
- Data + metadata updates are treated as first-class changes.
- We track and attach **run manifests**, checksums, and PROV records.
- Pull Requests can be represented as **PROV Activities**, commits as **Entities**, and authors/reviewers as **Agents** (so devops becomes queryable lineage).

### 2) 🔒 Fail-closed policy gates (policy is “just another test”)
- Governance rules are enforced automatically.
- If a license is missing, a sensitivity tag is absent, or a schema is invalid → CI fails (no “silent drift”).

### 3) 🗺️ Data ≠ code (but it’s still versioned like code)
- KFM’s pipeline expects standard metadata triplets:
  - **STAC** (spatiotemporal indexing)
  - **DCAT** (discoverability + distribution)
  - **PROV** (lineage + reproducibility)

### 4) 🧠 AI is not exempt
- Focus Mode uses **hybrid retrieval / RAG** (graph + GIS + doc search).
- Answers must remain **citation-backed** and governed (prompt-security gates, sensitivity rules, etc.).

---

## 🔁 Pipeline at a glance

```mermaid
flowchart LR
  PR[🔀 Pull Request] --> CALL[📞 Caller workflow]
  CALL --> RW[♻️ Reusable workflows]

  RW --> POL[🔒 Policy Pack (OPA/Conftest)]
  RW --> TEST[🧪 Unit/Integration/E2E]
  RW --> META[🗂 STAC/DCAT/PROV Validate]
  RW --> PROV[🧬 PROV + Run Manifest]
  RW --> BUILD[📦 Build + SBOM + Sign]

  META --> PG[(🗺️ PostGIS)]
  META --> N4J[(🧠 Neo4j)]
  BUILD --> OCI[(📦 OCI Registry)]
```

---

## 🧩 Reusable workflow catalog (recommended set)

> [!NOTE]
> File names can evolve — what matters is **consistent responsibility boundaries**. If you add/rename a reusable, update this table ✅

| Category | Reusable (suggested) | What it enforces | Typical triggers |
|---|---|---|---|
| 🔒 Governance | `reusable-policy-pack.yml` | OPA/Conftest rules, FAIR+CARE, secrets scanning, license checks, required metadata fields | PR / Push |
| 🧬 Provenance | `reusable-provenance-pr.yml` | PR → PROV JSON-LD, run manifests, canonical hashes, attach artifacts | PR / Push |
| 🧪 API CI | `reusable-python-ci.yml` | lint + tests + typecheck + coverage (FastAPI / data tooling) | PR / Push |
| 🧪 UI CI | `reusable-node-ci.yml` | lint + typecheck + tests + build (React/TS, MapLibre/Cesium UI) | PR / Push |
| 🗂 Metadata | `reusable-stac-dcat-prov-validate.yml` | schema + link validation, catalog integrity, evidence linkage | PR / Push |
| 🧱 Graph | `reusable-graph-import-dryrun.yml` | Neo4j CSV import sanity checks, stable ID validation, optional Cypher smoke tests | PR |
| 🗺️ Geodata | `reusable-geo-build.yml` | build/validate PMTiles/MBTiles/COG/GeoParquet artifacts | PR / Push |
| 🧠 AI | `reusable-ai-eval.yml` | RAG regression suite, citation rules, prompt-gate checks, drift/safety checks | PR / Nightly |
| 📦 Release | `reusable-build-sign-publish.yml` | Docker build, SBOM, signing, publish to GHCR/OCI, attach attestations | Push / Tag |
| 🛰️ Offline | `reusable-offline-pack.yml` | creates offline bundles (tiles + story nodes + minimal UI) and publishes as artifact | Release |
| 🧹 Maintenance | `reusable-maintenance.yml` | dependency updates, scheduled health checks, graph QA, doc link checks | Scheduled |

---

## 🧷 Inputs, outputs, and conventions

### ✅ Naming
- Prefer: `reusable-<domain>-<action>.yml`
  - e.g., `reusable-python-ci.yml`, `reusable-policy-pack.yml`

### 🧾 Standard inputs
Keep inputs:
- **explicit**
- **typed**
- **documented**
- stable across repos (future “Frontier Matrix” forks)

Suggested baseline inputs:
- `working-directory` (string)
- `python-version` / `node-version` (string)
- `run-tests` / `run-typecheck` / `run-lint` (bool)
- `artifact-retention-days` (number)
- `fail-on-warnings` (bool)

### 📦 Standard outputs & artifacts
Every reusable should aim to produce at least one of:
- 🧬 `run_manifest.json` (tool versions, counts, sources, inputs/outputs)
- 🧾 SBOM (SPDX/CycloneDX)
- 🔏 signing metadata (cosign attestations, if enabled)
- 🗂 validation reports (STAC/DCAT/PROV, policy failures, link checks)
- 🧱 graph import diagnostics (CSV summary, constraint checks)

---

## 🔐 Secrets, permissions, and “kill switch” patterns

### 👮 Least-privilege permissions
Default job permissions should be minimal:
- `contents: read`
- `pull-requests: write` **only** if commenting on PRs
- `id-token: write` **only** for OIDC signing / artifact attestation

### 🧯 Automation kill switch (recommended)
KFM’s automation patterns benefit from a **single, obvious kill switch** 🛑 (for agents and scheduled jobs).

Example pattern:
```yaml
if: ${{ vars.KFM_AUTOMATION_ENABLED == 'true' }}
```

Recommended variable:
- `KFM_AUTOMATION_ENABLED` → `"true"` / `"false"`

Use it for:
- scheduled workflows
- auto-PR dependency bumpers
- background indexing or graph imports

---

## 🔒 Policy Pack guidance (OPA + Conftest)

The Policy Pack is where KFM encodes governance:
- ✅ metadata required fields (STAC/DCAT/PROV)
- ✅ license allowlist (SPDX)
- ✅ CARE sensitivity flags where needed
- ✅ “no secrets in git” pattern checks (tokens/keys)
- ✅ citation + evidence manifest rules for Story Nodes
- ✅ AI output metadata rules (citations, redaction flags)

> [!IMPORTANT]
> Policy checks should be **fail-closed** by default.
> If exceptions are needed, add them via PR so the rules remain transparent and auditable.

---

## 🧬 Provenance guidance (PR lineage + run manifests)

KFM treats devops artifacts as provenance:
- PR lifecycle events can emit **PROV JSON-LD**
- pipeline runs can produce:
  - a canonicalized `run_manifest.json` (stable hash)
  - artifacts that include provenance attachments
  - optional ingestion of provenance into Neo4j

This enables questions like:
- “Which code version produced this dataset?”
- “Which PR modified the water-quality pipeline and who reviewed it?”
- “Which stories used this dataset?” (via evidence manifests)

---

## 🗺️ Geospatial & graph workflows (KFM-specific expectations)

KFM’s runtime is hybrid:
- **PostGIS** for spatial performance
- **Neo4j** for semantic relationships + lineage

Reusable workflows should support:
- 🗂 STAC/DCAT/PROV validation before any import
- 🧱 “dry-run” graph import checks (CSV shape + stable IDs)
- 🛰 offline pack building (PMTiles/MBTiles + minimal metadata + story nodes)
- 🔁 rollback friendliness (Git revert + re-sync)

---

## 🧠 AI & Focus Mode workflows (RAG, citations, safety)

Focus Mode uses:
- hybrid retrieval (graph + GIS + text)
- caching / embeddings
- strict traceability to sources

So AI workflows should include:
- ✅ retrieval regression tests (same question → same cited sources set, within tolerance)
- ✅ citation policy checks
- ✅ “prompt gate” / prompt injection hardening checks
- ✅ drift / sanity checks for embeddings/index rebuilds (nightly)

---

## 🛠️ Authoring new reusables (house rules)

When adding a reusable workflow:

1) 📝 **Document-first**
   - Add a header comment block (purpose, inputs, outputs, secrets, examples)
   - Update this `README.md`

2) 🧪 **Test it like code**
   - Include at least one caller workflow in `.github/workflows/` that uses it
   - Prove it works on PRs

3) 🔒 **Pin what matters**
   - Prefer pinned action versions
   - Capture tool versions in `run_manifest.json`

4) 📏 **Be stable across repos**
   - If KFM is forked to another region, the reusable should still be usable with minimal edits

---

## 🧭 Related KFM docs (recommended reading)

These workflows are designed to match KFM’s architecture and governance concepts:

- 🗺️ UI System (React + MapLibre/Cesium, provenance in UI, offline packs)
- 🧬 Data Intake (STAC/DCAT/PROV backbone, PostGIS + Neo4j integration, rollback)
- 🧠 AI System (Focus Mode RAG, citations, prompt security)
- 🔒 Governance & Security (Policy Packs, SBOM/signing, fail-closed posture)
- 🚀 Proposals (PR → PROV graph integration, expanded automation)
- 🧩 Idea vaults (geospatial/WebGL references, CI/CD references, language resources)

> [!TIP]
> If you’re implementing a new reusable, look for the relevant guide in `docs/` and mirror its constraints here.

---

## ✅ Checklist (PR reviewers)

Use this checklist when reviewing workflow changes:

- [ ] Does it enforce or preserve provenance (artifacts + logs + stable IDs)?
- [ ] Does it respect fail-closed governance (no silent bypass)?
- [ ] Are permissions minimal (no broad write unless required)?
- [ ] Are secrets handled via GitHub secrets/vars (never in repo)?
- [ ] Are outputs reproducible (tool versions captured)?
- [ ] Is the reusable documented + this README updated?

---

## 🧯 Troubleshooting (common gotchas)

- **Policy Pack failing unexpectedly** → run Conftest locally against the changed files; check required fields + allowlists.
- **Graph import dry-run failing** → validate stable IDs & CSV headers; check relationship cardinalities.
- **Offline pack too large** → scope inputs; build per-county/per-theme bundles; publish as OCI artifacts.
- **AI eval “drift”** → ensure embeddings/index rebuild uses pinned model/tool versions; compare against last successful baseline.

---

### 🏁 Done
If you’re new here: start by finding the caller workflow that matches your change, then trace into the reusable. ♻️
