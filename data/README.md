<!--
📌 `data/` is KFM’s canonical evidence + metadata boundary.
🗓️ Last updated: 2026-01-26
🔐 Reminder: “Published” in KFM means cataloged + provenance-linked + validated (not just “a file exists”).
📦 Note: several “reference library” PDFs are *PDF portfolios* — extract embedded docs before indexing/searching (see “Reference portfolios” below).
-->

<a id="top"></a>

# 📦 `data/` — Kansas Frontier Matrix Evidence & Metadata Hub 🧭🗺️
_The governed home of KFM’s **sources**, **evidence artifacts**, and the **boundary metadata** (STAC/DCAT/PROV) that makes everything traceable._

<p align="left">
  <img alt="KFM" src="https://img.shields.io/badge/KFM-evidence%20%2B%20metadata-2b6cb0" />
  <img alt="Ordering" src="https://img.shields.io/badge/order-ETL%E2%86%92Catalogs%E2%86%92Graph%E2%86%92API%E2%86%92UI%E2%86%92Story%E2%86%92Focus-111827" />
  <img alt="STAC" src="https://img.shields.io/badge/STAC-Collections%20%26%20Items-845ef7" />
  <img alt="DCAT" src="https://img.shields.io/badge/DCAT-JSON--LD-845ef7" />
  <img alt="PROV" src="https://img.shields.io/badge/PROV-lineage%20bundles-845ef7" />
  <img alt="GeoParquet" src="https://img.shields.io/badge/GeoParquet-columnar%20vectors-845ef7" />
  <img alt="PMTiles" src="https://img.shields.io/badge/PMTiles-offline%20%2B%20fast%20maps-845ef7" />
  <img alt="COG" src="https://img.shields.io/badge/COG-cloud%20optimized%20GeoTIFF-845ef7" />
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-local%20LLM%20runtime%20optional-000000" />
  <img alt="RAG" src="https://img.shields.io/badge/RAG-citations%20%2B%20receipts-0b7285" />
  <img alt="OCI" src="https://img.shields.io/badge/OCI-artifact%20registry%20optional-6e40c9" />
  <img alt="Sigstore" src="https://img.shields.io/badge/Sigstore-Cosign%20attestations%20optional-6e40c9" />
  <img alt="SLSA" src="https://img.shields.io/badge/SLSA%20%2B%20SBOM-supply%20chain%20rigor-6e40c9" />
  <img alt="Governance" src="https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043" />
  <img alt="Policy" src="https://img.shields.io/badge/policy-OPA%20%7C%20Conftest-0b7285" />
  <img alt="Security" src="https://img.shields.io/badge/security-hostile--inputs%20%2B%20deny--by--default-critical" />
</p>

> [!IMPORTANT]
> ✅ **Prime directive:** `data/` is the **evidence boundary**.  
> If something can be used in the UI, Story Nodes, or Focus Mode, it must be:
> **(1) cataloged (STAC/DCAT)** + **(2) lineage-linked (PROV)** + **(3) policy-checked** + **(4) reproducible**.  
> **No catalog → no graph → no API → no UI.**  
> _(KFM calls this the “evidence triplet / evidence-first publishing” posture.)_ [^kfm_expanded] [^markdown_guide] [^kfm_ai]

> [!NOTE]
> 🌐 **Data Spaces mindset:** In KFM, **metadata + IDs + provenance** are the interface.  
> Big binaries may live in stable storage / registries *only if* pointers are stable, licensed, hashed, and auditable.  
> _(We prefer content-addressed references + strong receipts over “mystery paths.”)_ [^kfm_roadmap]

---

## 🔗 Repo navigation (common)
- ⬅️ Overview: `../README.md`
- 🧬 Pipelines: `../src/pipelines/README.md` *(or `../pipelines/README.md`, if present)*
- 🚪 API boundary: `../api/README.md` *(if present)*
- 🌐 Web UI boundary: `../web/README.md` *(if present)*
- 🧪 MCP (methods + receipts): `../mcp/README.md` *(if present — **recommended** for experiments/model cards)*
- 🧩 Schemas & contracts: `../schemas/README.md` *(if present)*
- 🧰 Validators & tooling: `../tools/README.md` *(if present)*
- 🤝 Collaboration automation: `../.github/README.md` *(if present)*
- 📚 Reference library: `../docs/reference/README.md` *(recommended home for extracted portfolio docs)*

---

<details>
<summary><strong>🧭 Table of contents</strong></summary>

- [🧾 Doc metadata](#-doc-metadata)
- [⚡ 60‑second rules](#-60second-rules)
- [🏁 5‑minute publish checklist](#-5minute-publish-checklist)
- [🧠 KFM pipeline snapshot](#-kfm-pipeline-snapshot)
- [🚦 Non‑negotiables](#-nonnegotiables)
- [✅ What “published” means in KFM](#-what-published-means-in-kfm)
- [🗂️ Canonical directory layout](#-canonical-directory-layout)
- [🧱 Intake Gate 0 (security + integrity)](#-intake-gate-0-security--integrity)
- [🔁 Data lifecycle](#-data-lifecycle)
- [🏷️ Metadata boundary artifacts](#-metadata-boundary-artifacts)
- [🧾 Manifests, contracts, QA receipts](#-manifests-contracts-qa-receipts)
- [🧬 Telemetry, policy decisions & run receipts](#-telemetry-policy-decisions--run-receipts)
- [🤖 AI evidence artifacts (Ollama + RAG)](#-ai-evidence-artifacts-ollama--rag)
- [🧷 IDs, versioning, naming, hashing](#-ids-versioning-naming-hashing)
- [📐 Formats & packaging rules](#-formats--packaging-rules)
- [📦 “Dual-format package” pattern (GeoParquet + PMTiles)](#-dual-format-package-pattern-geoparquet--pmtiles)
- [📚 Document knowledge base (PDFs, scans, excerpts)](#-document-knowledge-base-pdfs-scans-excerpts)
- [📦 Reference portfolios (PDF containers)](#-reference-portfolios-pdf-containers)
- [🛰️ Streaming/live feeds](#-streaminglive-feeds)
- [🧪 Validation & CI gates](#-validation--ci-gates)
- [🔐 Security, privacy, and sensitive-location safety](#-security-privacy-and-sensitive-location-safety)
- [🌐 Federation & data spaces](#-federation--data-spaces)
- [➕ Adding a new dataset / domain](#-adding-a-new-dataset--domain)
- [🧬 Releases, snapshots, and attestations](#-releases-snapshots-and-attestations)
- [📚 Project file influence map](#-project-file-influence-map)
- [📎 Evidence anchors (project files)](#-evidence-anchors-project-files)
- [🕰️ Version history](#-version-history)

</details>

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `data/README.md` |
| Status | Active ✅ |
| Doc version | **v1.6.0** |
| Last updated | **2026-01-26** |
| Audience | pipeline authors · catalog writers · validators · reviewers · API/UI integrators |
| Prime directive | **Catalogs are interfaces** (offer IDs + truthy pointers, not mystery paths). |
| Canonical ordering | **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story → Focus** |
| Default posture | fail‑closed publish gates 🚦 · hostile‑input aware 🧯 · audit‑ready 🧾 |

---

## ⚡ 60‑second rules

If you remember nothing else, remember these 👇

1. 🧾 **No triplet, no ship:** every promoted dataset emits **STAC + DCAT + PROV**. [^kfm_expanded] [^markdown_guide]
2. 🧊 **Raw is immutable:** never modify `data/raw` in place; treat it as a permanent record. [^kfm_roadmap]
3. 🔁 **Determinism wins:** same inputs + config ⇒ same outputs; re-runs are idempotent. [^kfm_arch] [^markdown_guide]
4. 🧷 **IDs are contracts:** if meaning/schema changes → bump **major** version.
5. 🔐 **Security is upstream:** hostile inputs are normal; validate and bound everything. [^kfm_tech]
6. ⚖️ **CARE/sovereignty propagates:** outputs cannot be less restricted than inputs without an audited redaction step. [^kfm_tech] [^markdown_guide]
7. 🛡️ **Policy is enforced, not vibes:** OPA/Conftest gates block violations in CI and runtime. [^kfm_ai]
8. 🧬 **Receipts-first:** runs emit telemetry + hashes + PROV + QA receipts. [^kfm_ai] [^master_coder]
9. 🧭 **UI touches only the governed API:** provenance + permissions are enforced at the boundary. [^kfm_ui] [^markdown_guide]
10. 📦 **Prefer dual-format packages:** GeoParquet (analysis) + PMTiles (UX) under one dataset ID. [^kfm_tech]
11. 🤖 **AI is evidence too:** embeddings, OCR corpora, AI-derived layers, prompt templates, and model versions are treated as **evidence artifacts** (hash + PROV + policy + catalogs). [^markdown_guide] [^kfm_ai] [^ollama]

---

## 🏁 5‑minute publish checklist

> [!IMPORTANT]
> **Publishing** = **processed evidence output + boundary artifacts + validation**.  
> Raw files alone are *never* “published” in KFM.

### ✅ Minimum bar (per dataset)
- [ ] **Intake Gate 0** passed (security + integrity) ✅  
  - [ ] `source.json` present  
  - [ ] `checksums.sha256` present  
  - [ ] `telemetry.ndjson` started *(even if tiny)*  
- [ ] Place sources under `data/raw/<domain>/<source>/...` *(read-only mindset; reprocessing anchor)*
- [ ] Generate intermediates under `data/work/<domain>/<dataset>/...` *(discardable/regeneratable)*
- [ ] Produce publishable outputs under `data/processed/<domain>/<dataset>/...`
- [ ] Create (or update) a dataset **manifest/contract** *(machine-checkable)*  
  - [ ] `data/manifests/kfm.ks.<domain>.<dataset>.v<major>.yml` *(recommended)*  
  - [ ] or `dataset.contract.json` *(supported if you prefer JSON; keep schema’d)*  
- [ ] Emit boundary artifacts (**the “evidence triplet”**)  
  - [ ] **STAC Collection** → `data/stac/collections/kfm.ks.<domain>.<dataset>.v<major>.json`
  - [ ] **STAC Item(s)** → `data/stac/items/kfm.ks.<domain>.<dataset>.<yyyymmdd>.<variant>.v<major>.json`
  - [ ] **DCAT Dataset (JSON‑LD)** → `data/catalog/dcat/kfm.ks.<domain>.<dataset>.v<major>.jsonld`
  - [ ] **PROV run bundle (JSON‑LD)** → `data/prov/<run-id>.jsonld`
- [ ] Add QA receipts: `data/qa/<domain>/<dataset>/<run-id>/...` *(bbox sanity, quicklook, validation report)*
- [ ] Run validators (local or CI) ✅ confirm schemas + links + governance checks pass

### 🤖 If AI/ML/LLM touched the artifact (required when applicable)
- [ ] Record the **model identifier** and (if possible) **digest** in QA + PROV (and in the manifest). [^kfm_ai] [^markdown_guide]
- [ ] Store a **model card** / **experiment card** (even minimal) under:
  - [ ] `mcp/<domain>/<dataset>/<run-id>/model_card.md` *(recommended)*, **or**
  - [ ] `data/qa/<domain>/<dataset>/<run-id>/model_card.md` *(if you keep everything in `data/`)* [^master_coder]
- [ ] Emit an **AI receipt** capturing: prompt template ID, retrieval set (catalog IDs), policy decision refs:
  - [ ] `data/qa/<domain>/<dataset>/<run-id>/ai_receipt.json` [^kfm_ai] [^ollama]

### 🥇 Quality tiers (helps reviewers)
| Tier | What it means | Required |
|---|---|---|
| 🥉 Bronze | Raw preserved + basic stewardship | source + terms + classification + hashes |
| 🥈 Silver | Processed output + STAC | publishable artifacts + STAC + QA note |
| 🥇 Gold | Fully governed + discoverable | STAC + DCAT + PROV + strong QA + hashes + policy pass |

### 🛡️ Optional “Gold+” (supply-chain / federation ready)
- [ ] **SLSA/SBOM** attached to the run artifacts (or referenced) [^kfm_tech]
- [ ] **Sigstore Cosign attestation** for releases (if mirrored to an artifact registry) [^kfm_roadmap]
- [ ] **OCI artifact packaging** (ORAS pattern) for distribution/federation (optional) [^kfm_roadmap]

---

## 🧠 KFM pipeline snapshot

KFM enforces strict ordering so downstream always has traceable evidence. 🧾🧬

```mermaid
flowchart LR
  subgraph Data["📦 Data & Metadata Boundary (repo + storage)"]
    A["📥 Raw sources (immutable)"] --> B["⚙️ ETL + normalization (deterministic)"]
    B --> W["🧪 QA receipts + validation"]
    B --> C["🛰️ STAC items + collections"]
    C --> D["🏷️ DCAT discovery (JSON-LD)"]
    C --> E["🧬 PROV lineage bundles"]
    B --> R["📦 (Optional) OCI artifact registry mirror\nORAS + tags/digests + Cosign"]
  end

  subgraph AI["🤖 AI lane (optional, but governed)"]
    V["🧠 Embeddings / Indexes\n(vector DB / parquet / search)"] --> L["🦙 Local LLM runtime\n(Ollama)"]
    L --> F["🧾 AI receipts\n(citations + policy checks)"]
  end

  subgraph Agents["🕵️‍♂️🤖 Automation (optional)"]
    X["Watcher"] --> Y["Planner"] --> Z["Executor"]
  end

  X -. detects .-> A
  Y -. policy checks .-> W
  Z -. runs ETL .-> B

  C --> G["🕸️ Knowledge graph (refs → catalogs)"]
  G --> H["🚪 API boundary (authZ + redaction + contracts)"]
  H --> I["🗺️ UI (MapLibre/WebGL + timeline)"]
  I --> J["🎬 Story Nodes (governed narrative)"]
  J --> K["🧠 Focus Mode (provenance-linked answers)"]

  C --> V
  E --> F
  F --> K
```

> [!NOTE]
> Watchers often use **ETag / Last-Modified** to avoid redundant downloads and to keep ingestion efficient, but every skip/decision should still be logged as telemetry. [^kfm_arch]

---

## 🚦 Non‑negotiables

- ⛓️ **Pipeline ordering is absolute:** `ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story → Focus`. [^markdown_guide]
- 🧾 **Catalogs are required interfaces:** downstream layers reference **catalog IDs**, not ad‑hoc file paths. [^kfm_expanded]
- 🔁 **Deterministic + idempotent ETL:** same inputs + config ⇒ same outputs (replay-safe). [^kfm_arch] [^markdown_guide]
- 🧷 **Stable IDs forever:** dataset IDs, collection IDs, run IDs, story IDs are long-lived contracts.
- 🔒 **Integrity is mandatory:** SHA256 hashes + manifests for publishable artifacts (at minimum processed outputs).
- 🔐 **Sovereignty/classification propagate:** outputs cannot be *less restricted* than any input without an audited redaction/generalization step. [^kfm_tech] [^markdown_guide]
- 🧯 **Hostile inputs:** GeoJSON/CSV/PDF/images/rasters from the internet are attack surfaces → validate + bound + sanitize.
- 🧠 **No unsourced narrative:** Story/Focus content must be provenance-linked; AI text must be labeled + cited. [^markdown_guide] [^kfm_ai]
- 🧊 **Git stays healthy:** commit metadata + QA receipts; keep heavy binaries in stable storage with hashed pointers (or DVC).

> [!TIP]
> **FAIR** makes data findable/accessible/interoperable/reusable.  
> **CARE** keeps it ethical and accountable.  
> **Sovereignty** ensures the right people control sensitive knowledge. 🧭

---

## ✅ What “published” means in KFM

KFM uses explicit **stages** and **contracts** so we don’t ship mystery layers.

### 🧊 Stages (data state)
- **Raw** → `data/raw/<domain>/<source>/...`  
  Source snapshot; minimally transformed; reprocessing anchor.
- **Work** → `data/work/<domain>/<dataset>/...`  
  Intermediate artifacts; not stable; may be deleted/regenerated.
- **Processed** → `data/processed/<domain>/<dataset>/...`  
  Final evidence outputs meant to be served/used downstream.
- **Published** ✅  
  Processed outputs with:
  - STAC/DCAT/PROV boundary artifacts, **and**
  - passing validations/CI gates, **and**
  - correct license/classification handling, **and**
  - stable IDs (dataset + run). [^markdown_guide]

> [!NOTE]
> **Evidence artifact rule:** analysis outputs and AI-generated artifacts (OCR corpora, predicted layers, etc.) are still “datasets” in KFM — same lifecycle, same catalogs, same PROV. [^markdown_guide]

### 🧭 Dataset “lifecycle status” (metadata state)
We recommend tracking lifecycle explicitly (in manifests + catalogs):
- `draft` → present, not promoted, may change
- `published` → meets the publish bar
- `deprecated` → still available, but replaced; keep pointers to successor
- `tombstoned` → removed from distribution (policy/legal), but provenance remains

> [!WARNING]
> If you ship a file without a STAC/DCAT/PROV trail, you ship an **orphan**.  
> Orphans do not get promoted.

---

## 🗂️ Canonical directory layout

> [!IMPORTANT]
> v13+ posture is **stage-first**: `data/{raw,work,processed}/<domain>/...`  
> Catalogs reference **processed** artifacts (or stable object-store/registry pointers). [^markdown_guide]

```text
data/
├─ 📥 raw/                                  # ✅ Required: raw source snapshots (read-only mindset; immutable evidence boundary)
│  └─ 🗂️ <domain>/
│     └─ 🌐 <source>/                       # as-downloaded bytes + checksums + intake telemetry
│
├─ 🧪 work/                                 # Recommended: intermediate transforms (regeneratable; OK to wipe/rebuild)
│  └─ 🗂️ <domain>/
│     └─ 🗃️ <dataset>/                      # normalized tables, intermediate exports, scratch
│
├─ ✅ processed/                             # ✅ Required: publishable evidence artifacts (what API/UI/graph should serve)
│  └─ 🗂️ <domain>/
│     └─ 📦 <dataset>/                      # GeoParquet/COG/PMTiles/etc. + sidecars + digests
│
├─ 🧾 sources/                               # Recommended: source manifests + fetch receipts (small, auditable files)
│  └─ 🗂️ <domain>/
│     └─ 🛰️ <source>/                       # source.json, fetch config, license notes, contacts, ETag/Last-Modified receipts
│
├─ 🛰️ stac/                                  # ✅ Required: STAC catalogs (asset index + time/run snapshots)
│  ├─ 🧾 catalog.json                        # Optional but helpful STAC root (links to collections)
│  ├─ 🗂️ collections/                        # STAC Collections (dataset-level metadata)
│  └─ 🧷 items/                               # STAC Items (run/time/version snapshots referencing assets)
│
├─ 🗂️ catalog/                               # Discovery layer (human/machine “what exists” index)
│  └─ 🗂️ dcat/                                # ✅ Required: DCAT JSON-LD dataset entries (license/access/distributions)
│     └─ ➕ (optional) vocabulary/, keywords/, orgs/, ontology/  # controlled vocab + ontology + org metadata
│
├─ 🧬 prov/                                  # ✅ Required: PROV lineage bundles (JSON-LD) linking raw→work→processed→catalog
│
├─ 🧾 manifests/                             # Recommended: dataset manifests/contracts + dictionaries
├─ 🧪 qa/                                    # Recommended: QA receipts (quicklooks, bbox checks, validation reports)
│
├─ 🤖 ai/                                    # Optional: AI artifacts (prompt templates, model cards, RAG receipts)
│  ├─ 🧩 prompts/                            # versioned prompt templates (text, JSON, YAML)
│  ├─ 🪪 model_registry/                     # model metadata (IDs, digests, capabilities, licenses)
│  └─ 🧾 receipts/                           # ai_* receipts (retrieval sets, citations, policy hashes)
│
├─ 📡 live/                                  # Optional: streaming buffers + snapshots (still cataloged + provenance-linked)
├─ 📦 packs/                                 # Optional: offline “education packs” (PMTiles + mini web app + subset of stories)
├─ 🛡️ attestations/                          # Optional: signed build/publish receipts (SLSA/Cosign refs) or verification notes
├─ 🔎 indexes/                               # Optional: search indexes (redaction-aware; never raw secrets)
│  ├─ 🔤 fulltext/                           # e.g., document excerpt indexes
│  └─ 🧠 embeddings/                         # embedding vectors / ANN indexes (treat as derived evidence artifacts)
├─ 🕸️ graph/                                 # Optional: graph import/export artifacts (prefer pointers over duplication)
│  ├─ 🧱 csv/                                 # Neo4j import CSV snapshots (node/rel tables)
│  └─ 🧠 cypher/                              # Cypher import scripts or verification queries
└─ 🙂📄 README.md                              # you are here
```

> [!NOTE]
> Some specs use `data/catalogs/*` or `data/provenance/*`. That’s fine **only if** you keep a single canonical path and alias the rest consistently.  
> Prefer stability over aesthetics.

---

## 🧱 Intake Gate 0 (security + integrity)

Before *anything* is allowed to move from “downloaded” → “raw”, run the intake gate. ✅🧯

### ✅ What Gate 0 checks
- 📄 **Source manifest exists** (`source.json`)  
- 🔒 **Hashes exist** (`checksums.sha256`) for at least:
  - the exact downloaded archive(s), or
  - the exact raw files if unarchived  
- 🧾 **Telemetry started** (`telemetry.ndjson`)  
- 🧪 **Safe extraction & scanning** (zip-bomb limits, path traversal, file allowlists)
- 🏷️ **Classification assigned** (`public/internal/restricted/...`) before anything is promoted
- ⚖️ **License/terms recorded** (or blocked pending review)
- 📦 **Portfolio detection (recommended):** if file is a PDF portfolio, flag it for extraction + sandbox handling before indexing. [^ai_portfolio] [^dm_portfolio] [^webgl_portfolio] [^eng_portfolio] [^gis_portfolio] [^langs_portfolio]

> [!CAUTION]
> If `source.json` is missing, reviewers cannot evaluate provenance.  
> If hashes are missing, we can’t detect silent corruption or tampering.

### ✅ Recommended “Gate 0+” receipts (small but powerful)
- `source.lock.json` capturing:
  - retrieval timestamp
  - URL/URI
  - HTTP headers (ETag, Last-Modified) when available
  - size, MIME type
  - auth mode used (never store secrets)
- `scan.json` capturing:
  - extraction boundaries used
  - antivirus/tool versions
  - findings (even “none”)

> [!TIP]
> Watchers can use ETag/Last-Modified to skip re-downloading unchanged artifacts, but the decision should still be logged as telemetry. 🧾 [^kfm_arch]

### 📄 `source.json` (minimal example)
```json
{
  "source_id": "kfm.source.<provider>.<name>",
  "name": "Human-readable source name",
  "owner": "Provider / archive / agency",
  "uri": "https://example.org/source",
  "retrieved_at": "2026-01-26",
  "license": {
    "spdx": "UNKNOWN",
    "terms_uri": "https://example.org/terms",
    "attribution": "If required, paste exact attribution text here"
  },
  "classification": "public",
  "notes": "Handling notes (rate limits, access policy, redaction constraints)."
}
```

### 🔒 `checksums.sha256` (format example)
```text
<sha256>  raw/<domain>/<source>/<filename.ext>
<sha256>  raw/<domain>/<source>/<archive.zip>
```

### 🧾 `telemetry.ndjson` (first lines example)
```json
{"ts":"2026-01-26T14:02:11Z","event":"intake.start","source_id":"kfm.source...","actor":"human","host":"devbox-01"}
{"ts":"2026-01-26T14:02:58Z","event":"intake.hash","path":"raw/.../archive.zip","sha256":"..."}
{"ts":"2026-01-26T14:03:21Z","event":"intake.scan.ok","tool":"clamav","notes":"no threats found"}
```

---

## 🔁 Data lifecycle

KFM supports batch and event-driven pipelines. Both remain provenance-led.

### 1) Ingestion 📥
- Scheduled pulls (known sources)
- Manual expert uploads (controlled staging + explicit terms)
- Crowd/citizen contributions (separate review lane; never auto-promoted)
- Preserve raw inputs as a reprocessing anchor.

> [!IMPORTANT]
> **Raw is a permanent record.** Pipelines should never alter files in `data/raw/`; they write new artifacts to `data/processed/` (and optionally `data/work/`). [^kfm_roadmap]

### 2) Processing 🧰
Cleaning, joins, georeferencing, derived layers, modeling, simulation outputs.

Rules of thumb:
- Prefer “compute near data” (PostGIS for spatial ops; workers for heavy ML/sim).
- Partition by what users filter on (space/time/admin boundaries).
- Keep transforms explicit and repeatable (scripts/config captured in PROV).
- If outputs come from **analysis/modeling/simulation/optimization**, publish with:
  - parameters + seeds,
  - validation/verification status (QA),
  - uncertainty notes (QA + manifest),
  - clear “not for decision-making” flags when appropriate. [^markdown_guide] [^master_coder]
- If you used **optimization under uncertainty** (robust/stochastic/chance constraints), document:
  - uncertainty set / scenario generation method,
  - risk tolerance,
  - sensitivity analysis results,
  - and what “robust” means operationally for the stakeholder. [^data_mining]

### 3) Indexing & discovery 🗂️
- STAC Items/Collectionscollections describe assets and coverage.
- DCAT describes datasets/distributions and how to obtain them.
- PROV describes how the dataset was produced and from what inputs.

### 4) Publication & serving 🌐
- Downstream layers ingest from catalogs (or catalog-driven exports).
- UI consumes governed API outputs (authZ + redaction + classification rules). [^kfm_ui] [^markdown_guide]
- New catalogs can trigger graph refresh + UI indexing.

### 5) Deprecation 🪦
- Never “silently replace” a published dataset.
- Deprecate by:
  - publishing a successor dataset version,
  - marking old one `deprecated`,
  - preserving old artifacts + hashes for audit/replay.

---

## 🏷️ Metadata boundary artifacts

> [!IMPORTANT]
> Boundary artifacts are the **interfaces** downstream layers consume.  
> Graph/API/UI/Story/Focus should reference **catalog IDs**, not ad-hoc local paths. [^markdown_guide]

### ✅ Required boundary outputs (the “evidence triplet”)
- **STAC (Collections + Items)** for spatiotemporal assets (vectors, rasters, tiles, documents, thumbnails, QA receipts).
- **DCAT dataset entry (JSON‑LD)** for discovery (title/description/license/keywords/distributions).
- **PROV lineage bundle (JSON‑LD)** capturing inputs → activities → outputs. [^kfm_expanded] [^markdown_guide]

### 🔗 Cross-layer linkage expectations (do not break)
- STAC Items link to stable assets (usually `data/processed/...` or stable object-store/registry URLs).
- DCAT links to distributions (STAC, API endpoints, and/or direct downloads where allowed).
- PROV links raw → work → processed and records run/config identifiers.
- Graph stores references to catalog IDs (avoid stuffing heavy payloads into the graph). [^kfm_ai] [^markdown_guide]

### 🧩 KFM extensions (recommended fields)
To support policy gates + Focus Mode “receipts”, add KFM-scoped fields (namespaced) in STAC/DCAT/PROV where appropriate:

- `kfm:dataset_id`
- `kfm:run_id`
- `kfm:classification`
- `kfm:license_spdx`
- `kfm:sovereignty_notes` *(when needed)*
- `kfm:quality` *(QA pointers + known limitations)*
- `kfm:ai_assisted` *(if any ML/LLM used to derive an artifact)*
- `kfm:ai_model_id` *(model ID and, if possible, digest)*
- `kfm:prompt_template_id` *(prompt contract)*
- `kfm:embedding_model_id` *(if embeddings/indexes exist)*

### 🧭 FAIR+CARE metadata (recommended)
KFM design includes ethical metadata fields (e.g., “faircare” notes capturing collective benefit, authority to control, responsibility, ethics). [^kfm_expanded] [^markdown_guide]

> [!NOTE]
> Focus Mode is only as strong as the metadata it can cite. If an artifact lacks license/classification/provenance pointers, Focus Mode must treat it as **not eligible**. [^kfm_ai]

---

## 🧾 Manifests, contracts, QA receipts

KFM treats datasets like shippable products: they need a machine-checkable contract and a human-readable QA receipt. 🎟️🧾

### ✅ Recommended per-dataset files
- `data/manifests/kfm.ks.<domain>.<dataset>.v<major>.yml`  
- `data/qa/<domain>/<dataset>/<run-id>/qa.md`  
- `data/qa/<domain>/<dataset>/<run-id>/quicklook.png` *(small)*
- `data/qa/<domain>/<dataset>/<run-id>/validation.json` *(machine-readable)*
- `data/manifests/<...>/data_dictionary.md` *(or `schema.json` — strongly recommended for analytics outputs)*

### 📄 Dataset manifest (YAML example)
```yaml
dataset_id: "kfm.ks.<domain>.<dataset>.v1"
title: "Human-readable title"
description: "What this is and what it is not."
owner: "KFM / partner org"
contacts:
  - name: "Data Steward"
    role: "steward"
    email: "steward@example.org"

classification: "public"        # public|internal|confidential|restricted
license:
  spdx: "CC-BY-4.0"
  terms_uri: "https://example.org/terms"
  attribution: "Required attribution text"

faircare:                        # optional but encouraged (human-governed)
  collective_benefit: "Who benefits?"
  authority_to_control: "Who controls use?"
  responsibility: "Responsibilities/constraints?"
  ethics: "Key ethical notes"

spatial:
  crs: "EPSG:4326"
  bbox: [-102.05, 36.99, -94.58, 40.00]
temporal:
  start: "1930-01-01"
  end: "1940-12-31"

# Optional but strongly recommended when AI/ML touched outputs
ai:
  assisted: false
  model_id: null               # e.g., "ollama:llama3.1:8b@sha256:..."
  prompt_template_id: null     # e.g., "kfm.prompt.focus.v2"
  embedding_model_id: null     # e.g., "kfm.embed.bge-small.v1"
  model_card_path: null        # e.g., "mcp/<domain>/<dataset>/<run-id>/model_card.md"
  ai_receipt_path: null        # e.g., "data/qa/<domain>/<dataset>/<run-id>/ai_receipt.json"
  citation_required: true

distributions:
  - kind: "stac_collection"
    id: "kfm.ks.<domain>.<dataset>.v1"
    path: "data/stac/collections/kfm.ks.<domain>.<dataset>.v1.json"
  - kind: "dcat_dataset"
    id: "kfm.ks.<domain>.<dataset>.v1"
    path: "data/catalog/dcat/kfm.ks.<domain>.<dataset>.v1.jsonld"

artifacts:
  processed_paths:
    - "data/processed/<domain>/<dataset>/..."
  checksums: "data/processed/<domain>/<dataset>/checksums.sha256"

qa:
  latest_run_id: "etl_20260126_140211_ab12cd3"
  receipts_path: "data/qa/<domain>/<dataset>/etl_20260126_140211_ab12cd3/"
  known_limits:
    - "Explain key limitations here (coverage gaps, accuracy bounds, etc.)"
```

### 🧾 QA receipt template (Markdown + YAML front matter)
```yaml
---
doc_uuid: "qa.kfm.ks.<domain>.<dataset>.etl_20260126_140211_ab12cd3"
dataset_id: "kfm.ks.<domain>.<dataset>.v1"
run_id: "etl_20260126_140211_ab12cd3"
classification: "public"
bbox: [-102.05, 36.99, -94.58, 40.00]
crs: "EPSG:4326"
time_coverage: ["1930-01-01", "1940-12-31"]
quicklooks:
  - "quicklook.png"
validators:
  - name: "stac.validate"
    status: "pass"
  - name: "prov.validate"
    status: "pass"
ai:                               # optional
  assisted: false
  model_id: null
  prompt_template_id: null
  retrieval_set: []              # catalog IDs used (if any)
  policy_decisions: []           # policy hash/version refs
---
# QA Receipt — <dataset>
## What changed
## Validation summary
## Visual sanity checks
## Known limitations
## Evidence pointers (STAC/DCAT/PROV IDs)
```

> [!TIP]
> Reviewers love QA receipts. They turn “trust me” into “see for yourself.” ✅

---

## 🧬 Telemetry, policy decisions & run receipts

KFM’s reproducibility posture is “receipt-first.” Every meaningful run leaves a trail. [^markdown_guide] [^master_coder]

### ✅ What should exist for a promoted run
- `run_id` (stable, audit-friendly)
- parameters/config snapshot (hashable)
- deterministic seed (when relevant)
- input hashes (at least raw archive hashes)
- output hashes (required for processed outputs)
- PROV bundle (inputs → activities → outputs)
- telemetry log (NDJSON) for “what happened”
- policy decision refs (policy hash / version) when a gate is involved [^kfm_ai]

### 🧾 Recommended telemetry event vocabulary
Keep it boring and consistent:
- `intake.*` → download/hash/scan/extract/classify
- `etl.*` → transform steps, CRS transforms, georef, resampling, simplification
- `validate.*` → schema checks, link checks, geometry checks
- `publish.*` → writing STAC/DCAT/PROV, promotion decisions, kill-switch status
- `policy.*` → OPA/Conftest decisions + rule IDs
- `redact.*` → generalization/masking steps (and approvals)
- `schema_drift.*` → planner proposals + executed migrations (if enabled)

**AI lane telemetry (if used) 🤖**
- `ai.retrieve.*` → which catalogs/IDs were retrieved
- `ai.rank.*` → ranking/reranking decisions + scores
- `ai.generate.*` → model + prompt template + parameters (no secrets)
- `ai.cite.*` → citation set used and/or blocked
- `ai.policy.*` → policy outcomes (allow/deny/redact)
- `ai.export.*` → when AI content is exported into story nodes / reports [^kfm_ai] [^markdown_guide]

### 🛡️ Provenance-first operations (supply chain posture)
KFM extends provenance beyond datasets into the build/release process:
- SLSA-style attestations and SBOMs can accompany releases (software + data). [^kfm_tech]
- Data artifacts can be mirrored into OCI registries and cryptographically signed (Sigstore Cosign). [^kfm_roadmap]
- Automation agents may sign artifacts/PRs to prove they came from approved automation paths. [^kfm_roadmap]

> [!IMPORTANT]
> If the **kill-switch** is enabled, telemetry must show it, and promotion steps must stop (or enter audit-only mode). 🧯 [^kfm_ai]

---

## 🤖 AI evidence artifacts (Ollama + RAG)

KFM supports AI assistance **only** when it’s evidence-first and auditable.

### ✅ What counts as an “AI evidence artifact”
Treat these like datasets (same publish rules):
- OCR-derived corpora (text extraction outputs)
- Embedding indexes / ANN structures (used by retrieval)
- AI-derived layers (classifications, predicted maps, extracted entities)
- Prompt templates and retrieval recipes (they shape outputs)
- AI receipts (the “why and what sources” record)

> [!IMPORTANT]
> If the UI/Story/Focus sees it, it must be:
> **cataloged (STAC/DCAT)** + **lineage-linked (PROV)** + **policy-checked** + **reproducible**. [^markdown_guide] [^kfm_ai]

### 🦙 Ollama lane (optional)
KFM’s AI infrastructure supports a **local** model runtime lane (privacy-first / offline-friendly) and treats model + runtime metadata as governed artifacts. [^ollama]

**Rules:**
- Keep **model weights** out of Git unless tiny/dev-only; store them via registry/object-store with digests.
- Record model identity (and digest if possible) in:
  - QA receipt (`ai:` block),
  - PROV activity (AI run),
  - manifest (`ai:` section). [^markdown_guide] [^master_coder]

### 📁 Suggested storage pattern (AI)
```text
data/ai/prompts/
  kfm.prompt.focus.v2.md
data/ai/model_registry/
  kfm.model.ollama.llama3_1_8b.v1.json
data/indexes/embeddings/<embedding_model>/<dataset_id>/<run_id>/
  vectors.parquet
  index.meta.json
data/qa/<domain>/<dataset>/<run_id>/
  ai_receipt.json
data/prov/<run_id>.jsonld
```

### 🧾 Minimum AI receipt (JSON) fields
```json
{
  "ai_run_id": "ai_20260126_151233_ab12cd3",
  "model_id": "ollama:llama3.1:8b@sha256:...",
  "prompt_template_id": "kfm.prompt.focus.v2",
  "embedding_model_id": "kfm.embed.bge-small.v1",
  "retrieval_set": [
    "kfm.ks.<domain>.<dataset>.v1",
    "kfm.ks.<domain>.<dataset>.<yyyymmdd>.<variant>.v1"
  ],
  "policy": {
    "pack": "kfm_policy_pack_vX",
    "decision": "allow|deny|redact",
    "reasons": ["..."]
  },
  "citations": [
    {"catalog_id":"...", "asset":"...", "sha256":"..."}
  ]
}
```

> [!TIP]
> **Design audit reminder:** “semantic layer / ontology” work dramatically improves AI retrieval quality (less schema drift, better cross-domain joins). Consider tracking ontology files as governed artifacts too. [^design_audit]

---

## 🧷 IDs, versioning, naming, hashing

Stable IDs make KFM queryable, debuggable, and safe to automate.

### ✅ Dataset IDs (recommended)
- **Dataset / Collection ID:** `kfm.ks.<domain>.<dataset>.v<major>`  
  Example: `kfm.ks.hydrology.watersheds.v1`
- **STAC Item ID:** `kfm.ks.<domain>.<dataset>.<yyyymmdd>.<variant>.v<major>`  
  Example: `kfm.ks.geology.surficial.20260101.statewide.v1`
- **Run ID:** `etl_<yyyymmdd>_<hhmmss>_<shortgitsha>`  
  Example: `etl_20260126_140211_ab12cd3`

### 🤖 Optional AI IDs
- **Prompt template ID:** `kfm.prompt.<name>.v<major>`
- **Embedding model ID:** `kfm.embed.<name>.v<major>`
- **AI run ID:** `ai_<yyyymmdd>_<hhmmss>_<shortgitsha>`

### 🧠 ID design rule (don’t regret later)
- IDs are **names**, not facts.
- Avoid encoding mutable meaning inside IDs.
- If meaning/schema changes, bump the **major version**.

### 📛 File naming (processed evidence artifacts)
Prefer routing-friendly names:
- `<domain>__<dataset>__<yyyymmdd|yyyymm>__<epsg>__<resolution>__v<major.minor>.<ext>`
- Example: `agriculture__ndvi__20250301__epsg4326__30m__v1.0.tif`

### 🔒 Hashing rule
Record **SHA256** for:
- processed outputs (**required**)
- raw inputs (**recommended**)
- configs/parameter snapshots (**recommended**)
- AI receipts + prompt templates (**recommended** when AI lane used)

Where hashes should appear:
- STAC assets (checksum fields / extension)
- PROV entity records
- dataset manifests (`data/manifests/**`)
- `checksums.sha256` alongside artifacts for quick audit

### 📦 Optional: content-addressed distribution
When distributing via registries:
- prefer digest references (`...@sha256:<digest>`) over mutable tags
- if you must use `latest`, treat it as a convenience pointer only [^kfm_roadmap]

---

## 📐 Formats & packaging rules

KFM is map-first and time-aware. Formats must support streaming, indexing, and honest representation.

### 🗺️ Vector
| Use case | Preferred | Why |
|---|---|---|
| Small inspectable overlays | GeoJSON | debuggable; interoperable |
| Analytics exchange | GeoParquet | columnar; fast filters/scans |
| UI performance | PMTiles (vector tiles) | pan/zoom performance + offline |
| Authoritative edits | PostGIS | constraints + indices + query power |

**Vector must-haves ✅**
- stable feature IDs (`kfm_id` or equivalent)
- geometry validity checks + CRS explicit
- simplification/topology documented for UI-facing layers
- schema documented (manifest + DCAT) for analytics formats

### 🛰️ Raster
| Use case | Preferred | Why |
|---|---|---|
| Web streaming | COG | range requests; pyramids |
| Analysis stacks | Zarr/NetCDF *(when appropriate)* | chunked reads; large time-series |
| Quicklook | PNG/JPEG | small previews for QA |
| Time-series | chunked partitions | scalable partial reads |

**Raster must-haves ✅**
- nodata defined + units documented
- overviews/pyramids when serving to UI
- QA quicklook at known bbox/zoom

### 🧭 CRS & projection hygiene (do not skip)
- Treat **EPSG:4326** as a *storage / interchange* CRS, not always a compute CRS.
- Many operations (distance buffers, area, rasterization) require a projected CRS in meters; reproject intentionally and document it. [^py_geo]
- Bake CRS assumptions into QA: “CRS = expected; bounds reasonable; geometries valid.”

### ⚡ Performance hygiene (maps + analytics)
- Use spatial indexes (R-tree, KD-tree/ball tree where applicable) for joins/nearest-neighbor at scale. [^py_geo]
- Partition large layers by space/time and only ship what the UI needs.

### 🧾 Documents & scans (archives)
| Use case | Preferred | Notes |
|---|---|---|
| Scanned historical maps | lossless master + georef COG | record georef method + RMS + GCP count |
| Textual archives | PDF + extracted text | treat PDFs as hostile inputs; validate |
| Image derivatives | PNG/JPEG | derivatives for UX, masters for fidelity |

### 🧊 3D & “beyond 2D” evidence
3D evidence must remain provenance-linked:
- raw scans/models in `data/raw/<domain>/...`
- view-optimized assets in `data/processed/<domain>/...` (glTF / 3D Tiles)
- cataloged in STAC as assets with **CRS + vertical datum** + QA previews

> [!TIP]
> Visualization ≠ truth. 3D assets still need provenance, QA, and policy gating.

---

## 📦 “Dual-format package” pattern (GeoParquet + PMTiles)

This pattern is a KFM favorite because it serves **both** analysis and UX.

### ✅ What it is
Publish **one dataset ID** with **two distributions**:
- **GeoParquet** → analysis, joins, statistics
- **PMTiles** → UI layers, offline packs, fast pan/zoom [^kfm_tech]

### 📁 Suggested structure
```text
data/processed/geology/surficial/
  surficial__statewide__epsg4326__v1.0.parquet
  surficial__statewide__z0-12__v1.0.pmtiles
  checksums.sha256

data/stac/items/
  kfm.ks.geology.surficial.20260101.statewide.v1.json   # assets: parquet + pmtiles + quicklook

data/catalog/dcat/
  kfm.ks.geology.surficial.v1.jsonld                    # distributions: parquet + pmtiles + api
```

### ✅ Reviewer expectations
- both distributions hash-verified
- STAC points to both assets
- QA receipt includes:
  - quicklook screenshot(s)
  - bbox sanity
  - basic attribute summary (top fields, row count)
  - simplification/tiling notes for PMTiles

> [!NOTE]
> Offline “education packs” and PWA bundles get dramatically easier when PMTiles exists. 📦📚 [^kfm_roadmap]

---

## 📚 Document knowledge base (PDFs, scans, excerpts)

KFM supports a “document knowledge base” pattern where excerpts, citations, and evidence are discoverable and map-linked. [^hub_design]

A common pattern:
- source PDFs in storage,
- extracted excerpts as structured records,
- links from excerpts to **places** (coordinates / bounding boxes), **topics**, and **timeline** anchors, enabling map + search + narrative use.

### ✅ Recommended layout (documents)
```text
data/raw/archives/<source>/pdf/
data/work/archives/<dataset>/text_extraction/
data/processed/archives/<dataset>/
  excerpts.parquet            # extracted snippets + references (no secrets; redaction-aware)
  ocr_text.ndjson             # optional raw OCR output (classification-dependent)
  thumbnails/                 # small UI previews
  checksums.sha256
```

### 🧯 Security note (documents)
- PDFs/images are hostile-input surfaces; extract in sandboxed workers.
- Record OCR tool/version and quality metrics in QA receipts.
- If documents contain PII/sensitive locations, publish only redacted/generalized derivatives.

---

## 📦 Reference portfolios (PDF containers)

Some project “reference library” files are **PDF portfolios** (containers of many embedded documents). They are useful, but must be handled intentionally.

### ✅ Portfolio rule
- Treat the portfolio itself as a raw artifact (Gate 0).
- **Extract embedded files** (in a sandbox) into a governed folder.
- Then index/cite the extracted PDFs like normal documents.

### 📁 Suggested extraction landing zone
Pick one canonical home (don’t scatter):
- `docs/reference/portfolios/<portfolio_name>/...` *(recommended for human reading)*  
  **and/or**
- `data/raw/library/portfolios/<portfolio_name>/...` *(recommended if you want it fully governed like evidence sources)*

### 🧰 Extraction workflow (example)
```bash
# Recommended: extract attachments into a dedicated folder (run in a sandbox).
mkdir -p docs/reference/portfolios/ai_concepts
cd docs/reference/portfolios/ai_concepts

# List embedded attachments (poppler tool)
pdfdetach -list "../../../AI Concepts & more.pdf"

# Extract all attachments into the current directory
pdfdetach -saveall "../../../AI Concepts & more.pdf"
```

> [!CAUTION]
> Portfolio contents still inherit licensing + classification rules.  
> Extraction does not “launder” restrictions — it simply makes the evidence *indexable*.

### 📚 Portfolios in this project (currently)
- **AI Concepts & more.pdf** (PDF portfolio) [^ai_portfolio]  
- **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** (PDF portfolio) [^dm_portfolio]  
- **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** (PDF portfolio) [^webgl_portfolio]  
- **Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf** (PDF portfolio) [^eng_portfolio]  
- **Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf** (PDF portfolio) [^gis_portfolio]  
- **Various programming langurages & resources 1.pdf** (PDF portfolio) [^langs_portfolio]  

---

## 🛰️ Streaming/live feeds

KFM supports streaming inputs **only if they remain governable**.

### ✅ Rules for live/streamed datasets
- Live data becomes “real” only when it is:
  - written to stable storage (snapshots or append logs),
  - cataloged as STAC Items (micro-batch measurements are fine),
  - lineage-linked (PROV run/activity),
  - policy checked (classification + redaction + licensing).
- Prefer micro-batch windows (e.g., 5 min / 1 hour / daily) → STAC Item per window.
- Treat feeds as hostile inputs (schema checks, bounds checks, rate-limits).

### 📁 Suggested layout (optional)
```text
data/live/<domain>/<feed>/
  buffer/                 # short-lived ingest buffers (not published)
  snapshots/              # durable snapshots (publish candidates)
  telemetry.ndjson
```

> [!CAUTION]
> “Near real-time” is a pressure multiplier. Don’t relax governance because data is fast.

---

## 🧪 Validation & CI gates

KFM expects automated validation to prevent regressions and sensitive leaks.

### ✅ Typical gates
- STAC/DCAT/PROV schema validation (KFM profiles)
- Link checks (assets exist/reachable, distributions resolve)
- Hash verification (processed outputs required)
- Classification consistency (no downgrades without audited redaction)
- Secret scanning + sensitive data scanning
- Geometry validity + CRS sanity
- Temporal indexing sanity (timeline slider depends on it) [^kfm_ui]
- Policy pack evaluation (OPA/Conftest) for:
  - required license fields,
  - CRS requirements,
  - sensitivity restrictions,
  - AI citation requirements, etc. [^kfm_ai]

**AI lane checks (if used) 🤖**
- `ai_receipt.json` exists and references catalog IDs (not raw paths)
- AI outputs are labeled as derived/AI-assisted in metadata
- Policy decisions are logged
- No “unsourced claims” allowed for Story/Focus exports [^markdown_guide] [^kfm_ai]

### 🚦 Fail-fast publish gates (common policy)
- missing PROV bundle → ❌
- broken STAC asset link → ❌
- missing license/attribution for a promoted dataset → ❌ *(or “blocked pending review”)*
- sensitive leak hit → ❌
- kill-switch enabled and PR attempts promotion → ❌/audit-only 🧯 [^kfm_ai]

### 🧰 Starter local checks (examples)
```bash
# 1) JSON sanity
find data/stac data/catalog/dcat data/prov -name "*.json*" -print0 | xargs -0 -n 1 jq empty

# 2) STAC link check (assets exist)
python tools/validation/validate_stac_links.py data/stac/items

# 3) PROV completeness (raw→work→processed)
python tools/validation/validate_prov.py data/prov

# 4) Governance scan (sensitive fields, risky URLs)
python tools/validation/scan_sensitive.py data
```

> ⭐ Keep CI fast. Put heavy geospatial validations into scheduled/nightly lanes when needed.

---

## 🔐 Security, privacy, and sensitive-location safety

### ✅ Always
- Never commit secrets.
- Treat ingestion as hostile (zip bombs, malformed files, SSRF, parser exploits).
- Keep “publish” behind policy gates (OPA/Conftest), and keep a kill-switch. [^kfm_ai] [^markdown_guide]

### 🤖 AI-specific security (if enabled)
- Treat prompts, retrieved text, and documents as **prompt-injection surfaces**.
- Log what was retrieved and what was used; never let AI bypass governance.
- Hash/version prompt templates and model IDs like any other dependency. [^kfm_ai] [^master_coder]

### 🧭 Sensitive location rule (hard)
If a dataset includes sensitive locations (culturally sensitive sites, protected resources, critical infrastructure, etc.):
- generalize precision (county/township grids, H3, jitter, or bounding boxes)
- restrict access where required
- do not publish exact coordinates unless explicitly permitted and reviewed [^kfm_tech] [^markdown_guide]

### 🕵️ Privacy-preserving data mining mindset (why this matters)
Even “non-sensitive” releases can leak information via:
- linkage attacks (joining public datasets)
- inference attacks (predicting private attributes)
- temporal differencing (comparing snapshots to reveal hidden changes)

Mitigations KFM can standardize:
- aggregation thresholds (don’t publish tiny groups)
- query auditing + inference control on sensitive slices (API layer)
- k-anonymity / l-diversity / t-closeness where appropriate (explicitly documented)
- differential privacy for high-risk aggregates (optional, clearly labeled)
- publish snapshots (not uncontrolled “diff drips”) for sensitive domains [^data_mining]

> [!IMPORTANT]
> If we can’t defend the disclosure boundary, it doesn’t ship. 🔒

---

## 🌐 Federation & data spaces

KFM is designed as a blueprint for other “Frontier Matrices.”

Target posture:
- prefer standards (STAC/DCAT/PROV) for interoperability
- expose trust signals (license, provenance, classification, QA pointers, uncertainty notes)
- enable cross-hub discovery via catalogs + shared ontology mappings
- keep sovereignty enforceable across federation boundaries
- optionally distribute artifacts via registries to support cross-instance reuse [^kfm_roadmap]

> [!NOTE]
> Federation ≠ free-for-all. Governance stays always-on.

> [!TIP]
> **Design audit nudge:** formalizing a semantic layer (controlled vocab + ontology + versioned mappings) reduces drift and improves cross-domain discovery and AI retrieval. [^design_audit]

---

## ➕ Adding a new dataset / domain

### ✅ Checklist
- [ ] Create staging folders:
  - [ ] `data/raw/<new-domain>/<source>/`
  - [ ] `data/work/<new-domain>/<dataset>/`
  - [ ] `data/processed/<new-domain>/<dataset>/`
- [ ] Run **Intake Gate 0** (source.json + hashes + telemetry + scan)
- [ ] Build deterministic pipeline (config + logging + hashes) [^markdown_guide] [^master_coder]
- [ ] Emit boundary artifacts:
  - [ ] STAC Collection + Item(s)
  - [ ] DCAT JSON‑LD entry
  - [ ] PROV run bundle
- [ ] Add dataset manifest (`data/manifests/...`) + QA receipt (`data/qa/...`)
- [ ] Validate schemas + links + governance in CI
- [ ] (Optional) Graph sync after catalogs exist
- [ ] Expose via governed API (classification + redaction)
- [ ] Add domain runbook under `docs/` *(recommended)* [^markdown_guide]

<details>
<summary><strong>🧱 Dataset skeleton (copy/paste)</strong></summary>

```text
# Intake (Gate 0)
data/raw/<domain>/<source>/source.json
data/raw/<domain>/<source>/checksums.sha256
data/raw/<domain>/<source>/telemetry.ndjson

# Evidence lifecycle (stage-first)
data/raw/<domain>/<source>/
data/work/<domain>/<dataset>/
data/processed/<domain>/<dataset>/
data/processed/<domain>/<dataset>/checksums.sha256

# Catalog boundary artifacts (versioned dataset IDs)
data/stac/collections/kfm.ks.<domain>.<dataset>.v1.json
data/stac/items/kfm.ks.<domain>.<dataset>.<yyyymmdd>.<variant>.v1.json

data/catalog/dcat/kfm.ks.<domain>.<dataset>.v1.jsonld
data/prov/etl_<yyyymmdd>_<hhmmss>_<shortgitsha>.jsonld

# QA + manifests (recommended)
data/qa/<domain>/<dataset>/etl_<...>/qa.md
data/qa/<domain>/<dataset>/etl_<...>/quicklook.png
data/manifests/kfm.ks.<domain>.<dataset>.v1.yml

# AI lane (optional)
data/qa/<domain>/<dataset>/etl_<...>/ai_receipt.json
mcp/<domain>/<dataset>/etl_<...>/model_card.md
data/indexes/embeddings/<embedding_model>/<dataset_id>/<run_id>/
```
</details>

---

## 🧬 Releases, snapshots, and attestations

When evidence artifacts graduate into distribution:
- 📦 Prefer immutable **release snapshots** (versioned IDs + immutable hashes).
- 🧾 Maintain a human-readable manifest answering:
  - what changed?
  - why?
  - which catalogs/prov define it?
- 🛡️ Where supported, publish integrity signals:
  - checksums
  - signed release artifacts / attestations (Sigstore Cosign) [^kfm_roadmap]
  - supply chain receipts (SLSA + SBOM) [^kfm_tech]

### 📦 Optional: “Data packaged as OCI” distribution lane
KFM roadmaps describe treating data like software packages:
- push a dataset bundle (GeoParquet + PMTiles + metadata) as an OCI artifact (ORAS)
- sign/attest with Cosign
- reference the digest from DCAT distributions [^kfm_roadmap]

> [!TIP]
> Treat “data releases” like software releases: version, changelog, hashes, provenance. Same discipline, same trust.

---

## 📚 Project file influence map

> ✅ This README is shaped by KFM’s core specs + the attached reference portfolios.  
> The table below reflects how those files influence `data/` rules, staging, packaging, governance, reproducibility, and AI evidence posture.

<details>
<summary><strong>📦 Expand: Influence map (project files)</strong></summary>

### 🧭 Core KFM specs (project-defining)
| Project file | How it shapes `data/` |
|---|---|
| `📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf` | Defines the **stage-first lifecycle** (`raw→work→processed`) and the **evidence triplet** requirement (STAC + DCAT + PROV). Also introduces FAIR+CARE metadata fields and deterministic ETL expectations. [^kfm_expanded] |
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` | Solidifies governance posture (FAIR/CARE + sensitive-site handling), dual-format packaging example (GeoParquet + PMTiles), and provenance-first operations with SLSA/SBOM considerations. [^kfm_tech] |
| `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf` | Provides the ingestion component model (watchers/fetchers/transformers/validators/loaders/metadata emitters) and emphasizes determinism + idempotence and ETag/Last-Modified efficiency patterns. [^kfm_arch] |
| `Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf` | Adds the “data-as-artifacts” distribution lane (OCI registry + ORAS) and cryptographic integrity (Cosign attestations), plus offline packs direction for packaging choices. [^kfm_roadmap] |
| `Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf` | Drives temporal indexing requirements (timeline slider), provenance injection into UI (via governed API), and motivates quicklooks + time slices for smooth UX. [^kfm_ui] |
| `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf` | Requires evidence-first publishing for Focus Mode; immutable AI ledger + provenance-first AI receipts; policy-as-code enforcement; sandbox posture for AI + secrets protection. [^kfm_ai] |
| `KFM AI Infrastructure – Ollama Integration Overview.pdf` | Defines the optional **local LLM runtime lane** (Ollama), plus deployment + model metadata considerations needed for reproducible AI evidence artifacts. [^ollama] |

### 🧰 Supporting project docs (templates + design blueprints)
| Project file | What it contributes |
|---|---|
| `MARKDOWN_GUIDE_v13.md.gdoc` | Reinforces canonical pipeline flow + directory conventions; codifies “evidence artifact pattern” for AI/analysis outputs (store in `data/processed`, catalog in STAC/DCAT, trace in PROV, serve via API only). [^markdown_guide] |
| `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` | Adds protocol discipline: documentation-first research practice, experiment traceability, reproducible environments, and “cards” (model/experiment/data) that map cleanly to QA receipts and MCP storage. [^master_coder] |
| `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf` | Highlights structural gaps to close (semantic layer/ontology, modularity, uncertainty quantification), influencing future-proofing for metadata, federation, and AI retrieval quality. [^design_audit] |
| `KFM- python-geospatial-analysis-cookbook.pdf` | Practical geospatial implementation guidance (CRS assumptions, reprojection needs, spatial indexing/nearest-neighbor patterns) to turn policy into working pipelines. [^py_geo] |
| `Data Mining Concepts & applictions.pdf` | Privacy-preserving data mining concepts (inference/linkage risks, k-anonymity family) and robust/stochastic optimization ideas used for uncertainty-aware modeling outputs and disclosure safety. [^data_mining] |
| `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` | Contributes the “document knowledge base” model (map-linked excerpts) and reinforces raw immutability + processed outputs for serving. [^hub_design] |

### 📚 Reference portfolios (PDF containers — extract before indexing)
| Portfolio file | What it contributes to `data/` conventions |
|---|---|
| `AI Concepts & more.pdf` *(PDF portfolio)* | AI governance, uncertainty-first posture, human-in-the-loop patterns. **Requires extraction** to access embedded docs. [^ai_portfolio] |
| `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` *(PDF portfolio)* | Data architectures + federation concepts + metadata-as-interface mindset. **Requires extraction.** [^dm_portfolio] |
| `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` *(PDF portfolio)* | CRS hygiene + 3D/WebGL constraints informing packaging + QA. **Requires extraction.** [^webgl_portfolio] |
| `Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf` *(PDF portfolio)* | Secure engineering + reproducible toolchains; compression/transport considerations; container posture. **Requires extraction.** [^eng_portfolio] |
| `Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf` *(PDF portfolio)* | GIS tool cross-compatibility; analytics workflow considerations; reproducible computation. **Requires extraction.** [^gis_portfolio] |
| `Various programming langurages & resources 1.pdf` *(PDF portfolio)* | Cross-language references; practical engineering + maintainability references. **Requires extraction.** [^langs_portfolio] |

</details>

---

## 📎 Evidence anchors (project files)

> These are the project files used to shape this `data/` policy.  
> Keep them close (or at least keep stable pointers + hashes) — KFM treats documentation and evidence as part of the system. 🧾

[^kfm_expanded]: 📚 **Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf**
[^kfm_tech]: **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
[^kfm_arch]: **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**
[^kfm_roadmap]: **Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf**
[^kfm_ui]: **Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf**
[^kfm_ai]: **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**
[^ollama]: **KFM AI Infrastructure – Ollama Integration Overview.pdf**
[^markdown_guide]: **MARKDOWN_GUIDE_v13.md.gdoc**
[^hub_design]: **Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf**
[^data_mining]: **Data Mining Concepts & applictions.pdf**
[^py_geo]: **KFM- python-geospatial-analysis-cookbook.pdf**
[^master_coder]: **Scientific Method _ Research _ Master Coder Protocol Documentation.pdf**
[^design_audit]: **Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf**

[^ai_portfolio]: **AI Concepts & more.pdf** *(PDF portfolio)*
[^dm_portfolio]: **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** *(PDF portfolio)*
[^webgl_portfolio]: **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** *(PDF portfolio)*
[^eng_portfolio]: **Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf** *(PDF portfolio)*
[^gis_portfolio]: **Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf** *(PDF portfolio)*
[^langs_portfolio]: **Various programming langurages & resources 1.pdf** *(PDF portfolio)*

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---:|---|---|---|
| v1.6.0 | 2026-01-26 | Added **AI evidence artifacts** section (Ollama lane + RAG receipts + AI telemetry), added **portfolio extraction workflow**, strengthened **CRS/projection hygiene** guidance, expanded manifests/QA to include **model cards + AI receipts**, and updated influence map to include **all project files** (including design audit + master coder protocol + cookbooks). | KFM Engineering |
| v1.5.0 | 2026-01-26 | Added **offline packs** + **attestations** optional lanes, strengthened **evidence triplet** language, clarified **policy decision logging** and **schema drift** events, aligned UI expectations (timeline/provenance injection), expanded **data-as-OCI** and **Cosign/SLSA/SBOM** posture, and added document knowledge base pattern. | KFM Engineering |
| v1.4.0 | 2026-01-19 | Added **Intake Gate 0** (source.json + checksums.sha256 + telemetry.ndjson), introduced `data/sources/` + `data/live/` optional lanes, formalized **telemetry/run receipts**, added **dual-format package pattern** (GeoParquet + PMTiles), strengthened privacy/inference safety notes, and refreshed influence map. | KFM Engineering |
| v1.3.1 | 2026-01-13 | Corrected canonical `data/` layout to v13 **stage-first** staging; expanded formats guidance (GeoParquet + 3D evidence); strengthened CI “fail-fast” publish gates; refreshed influence map. | KFM Engineering |
| v1.3.0 | 2026-01-11 | Prior iteration: lifecycle stages, STAC/DCAT/PROV boundary artifacts, dataset ID conventions, validation gates, influence map. | KFM Engineering |

<p align="right"><a href="#top">⬆️ Back to top</a></p>