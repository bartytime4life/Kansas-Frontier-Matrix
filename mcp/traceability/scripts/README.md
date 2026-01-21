---
title: "MCP Traceability Scripts"
path: "mcp/traceability/scripts/README.md"
version: "v0.1.0"
last_updated: "2026-01-21"
status: "active"
doc_kind: "README"
license: "CC-BY-4.0"
markdown_protocol_version: "1.0"
kfm_principles:
  - "provenance-first"
  - "contract-first"
  - "fail-closed policy gates"
---

# 🧾 MCP Traceability Scripts

![MCP](https://img.shields.io/badge/MCP-master%20coder%20protocol-8A2BE2)
![Traceability](https://img.shields.io/badge/traceability-evidence--first-blue)
![Provenance](https://img.shields.io/badge/provenance-enforced-brightgreen)
![STAC](https://img.shields.io/badge/metadata-STAC-orange)
![DCAT](https://img.shields.io/badge/metadata-DCAT-informational)
![PROV-O](https://img.shields.io/badge/metadata-PROV--O-yellow)
![OPA](https://img.shields.io/badge/policy-OPA%2FConftest-lightgrey)
![Supply%20Chain](https://img.shields.io/badge/supply%20chain-cosign%20%2B%20oras-black)

> **Chain-of-custody tooling** for Kansas Frontier Matrix (KFM): run manifests ➜ STAC/DCAT/PROV ➜ policy gates ➜ signatures ➜ publishable artifacts.  
> Goal: **no mystery layers** 🕵️‍♂️🚫 and **every insight comes with a footnote** 🧷⛓️.

> [!IMPORTANT]
> **Fail-closed by default** 🚦: if we can’t validate or prove provenance, it **doesn’t ship**.

---

## 🧭 Quick Navigation

- [🎯 What “traceability” means in KFM](#-what-traceability-means-in-kfm)
- [📦 What these scripts produce](#-what-these-scripts-produce)
- [🗂️ Folder layout](#️-folder-layout)
- [⚡ Quickstart](#-quickstart)
- [🔁 End-to-end workflows](#-end-to-end-workflows)
- [🧾 Run Manifest format](#-run-manifest-format)
- [🧬 STAC + DCAT + PROV wiring](#-stac--dcat--prov-wiring)
- [🚦 Policy gates](#-policy-gates)
- [🔏 Signing + OCI publishing](#-signing--oci-publishing)
- [🕸️ Graph registration + health checks](#️-graph-registration--health-checks)
- [🧠 AI traceability (Focus Mode + agents)](#-ai-traceability-focus-mode--agents)
- [🗺️ Geospatial helpers](#️-geospatial-helpers)
- [🧫 Privacy + sensitivity checks](#-privacy--sensitivity-checks)
- [📚 Source docs used to build this README](#-source-docs-used-to-build-this-readme)

---

## 🎯 What “traceability” means in KFM

Traceability is the **end-to-end proof trail** that links any KFM output back to:

- 📥 **Inputs** (source URLs, archives, sensor feeds, documents, etc.)
- 🧪 **Processing** (what ran, when, with which parameters and tool versions)
- 🧾 **Evidence metadata** (STAC/DCAT/PROV triplet)
- 🏷️ **Governance** (license, sensitivity classification, FAIR+CARE/CARE flags)
- 👤🤖 **Actors** (human contributor, bot, Watcher–Planner–Executor agent, Focus Mode invocation)
- 🔏 **Integrity** (canonical hashes, signatures, immutable governance ledger entry)

This aligns with KFM’s contract-first approach (metadata “data contracts” as source of truth), plus strict provenance/citation expectations for anything shown in the UI or AI assistant. 🧱⛓️

---

## 📦 What these scripts produce

Most workflows produce a **Trace Bundle** (think: “evidence backpack” 🎒) with:

- 🧾 `run_manifest.json` (canonicalized + hashed; idempotency key)
- 🧬 `prov.jsonld` (lineage; `prov:Entity`, `prov:Activity`, `prov:Agent`)
- 🛰️ STAC Items/Collections (`stac_item.json`, `collection.json`, assets)
- 🗃️ DCAT dataset record (`dcat_dataset.jsonld`)
- 🧷 `evidence_manifest.yaml` (for Story Nodes / Pulse Threads / AI outputs)
- ✅ validation + policy reports (schema, license, sensitivity, provenance completeness)
- 🔏 signatures + attestations (Cosign) + optional SBOM
- 📦 optional OCI publishing metadata (ORAS media types, digest pinning)

---

## 🗂️ Folder layout

> [!NOTE]
> This folder is the **scripts layer** for MCP traceability. If your repo uses a centralized CLI (e.g., `tools/cli.py`), treat these scripts as the implementation targets behind that CLI.

```text
📦 mcp/traceability/
└─ 📁 scripts/
   ├─ 📄 README.md
   ├─ 🐍 run_manifest.py                # create + hash run manifests (RFC 8785 canonical JSON)
   ├─ 🐍 emit_prov.py                   # build PROV-O JSON-LD from run + pipeline metadata
   ├─ 🐍 emit_stac.py                   # generate STAC Item/Collection + assets
   ├─ 🐍 emit_dcat.py                   # generate DCAT record + link to STAC/PROV
   ├─ 🐍 validate_bundle.py             # schema/spatial/license/provenance completeness checks
   ├─ 🐍 policy_gate.py                 # conftest/OPA runner wrapper (fail-closed)
   ├─ 🐍 graph_register.py              # mirror triplet into Neo4j (datasets/assets/activities)
   ├─ 🐍 graph_health_check.py          # scheduled integrity report (orphans, missing edges, drift)
   ├─ 🐍 evidence_manifest.py           # citations/evidence manifests for stories + AI outputs
   ├─ 🐍 ai_receipt.py                  # Focus Mode / agent action receipts + ledger payloads
   ├─ 🐍 privacy_scan.py                # optional: k-anonymity/l-diversity/t-closeness checks
   ├─ 🐚 sign_bundle.sh                 # cosign sign/verify artifacts (optional keyless)
   ├─ 🐚 publish_oci.sh                 # oras push/pull + attach provenance (optional)
   └─ 🧰 extract_pdf_portfolio.sh        # helper: unpack PDF portfolios in /mnt/data (optional)
```

> [!TIP]
> If your repo already has these scripts elsewhere, use this README as the **contract** for what each command must guarantee (inputs, outputs, exit codes, side effects).

---

## ⚡ Quickstart

### ✅ Prereqs

- 🐍 Python 3.11+ (recommended for deterministic tooling + JSON schema validation)
- 🧰 `jq` / `yq` (optional but convenient)
- 🚦 `conftest` + OPA (policy-as-code gates)
- 🔏 `cosign` + 📦 `oras` (optional, for supply-chain + OCI artifact distribution)
- 🕸️ Neo4j client (optional, for graph registration + health checks)
- 🗺️ GDAL / `ogr2ogr` (optional, for geospatial ingest helpers)

### 🔧 Environment variables (common)

```bash
# Core
export KFM_ENV=dev
export KFM_ACTOR="user:yourname"              # or agent:KFM_Bot / service:ci

# Storage / catalogs
export KFM_DATA_DIR="./data"

# Graph / DB (optional)
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASS="password"
export POSTGIS_DSN="postgresql://user:pass@localhost:5432/kfm"

# Policy
export KFM_POLICY_DIR="./mcp/traceability/policy"

# OCI publish (optional)
export OCI_REGISTRY="ghcr.io/your-org/kfm"
export OCI_REPO="trace-bundles"
```

---

## 🔁 End-to-end workflows

### 1) 📥 Dataset pipeline run → Trace Bundle (run manifest + triplet + gates)

**Intent:** Deterministic, idempotent pipelines that produce catalog-ready assets (e.g., GeoParquet/COGs/tiles), plus metadata and provenance.

```mermaid
flowchart LR
  A[📥 Source Data] --> B[🧪 Ingest/Transform]
  B --> C[🧾 Run Manifest<br/>RFC 8785 + SHA-256]
  C --> D[🧬 Emit STAC/DCAT/PROV]
  D --> E[🚦 Validate + Policy Gates<br/>(fail-closed)]
  E -->|pass| F[🔏 Sign (Cosign)]
  F --> G[📦 Publish (ORAS → OCI)]
  G --> H[🕸️ Register in Graph]
  E -->|fail| X[🛑 Block Merge/Publish]
```

**Typical command sequence (example):**
```bash
python run_manifest.py   --config pipelines/population/config.yaml --out data/audits/
python emit_stac.py      --run data/audits/<run_id>/run_manifest.json --out data/catalog/
python emit_dcat.py      --run data/audits/<run_id>/run_manifest.json --out data/catalog/
python emit_prov.py      --run data/audits/<run_id>/run_manifest.json --out data/provenance/

python validate_bundle.py --run data/audits/<run_id>/run_manifest.json
python policy_gate.py     --inputs data/catalog/ data/provenance/

# Optional supply-chain
./sign_bundle.sh          data/audits/<run_id>/
./publish_oci.sh          data/audits/<run_id>/ --registry "$OCI_REGISTRY" --repo "$OCI_REPO"
```

---

### 2) 📝 Story Node / 🫀 Pulse Thread → Evidence Manifest + provenance hooks

Story outputs must remain **evidence-first**: citations and an evidence manifest that preserves raw references (dataset IDs, query params, timestamps, etc.).

```mermaid
flowchart LR
  S[📝 Narrative Content<br/>(Markdown/JSON)] --> M[📎 evidence_manifest.yaml]
  M --> V[✅ Validate citations<br/>exist + resolvable]
  V --> P[🔗 PROV snippet<br/>prov:Entity derivedFrom]
  P --> G[🕸️ Graph links<br/>Story/Pulse → Datasets/Places]
  G --> UI[🧭 UI playback + provenance panel]
```

**Example:**
```bash
python evidence_manifest.py \
  --story docs/stories/dust_bowl.md \
  --out data/audits/<run_id>/evidence_manifest.yaml \
  --mode story-node

python validate_bundle.py --evidence data/audits/<run_id>/evidence_manifest.yaml
```

---

### 3) 🧠 Focus Mode answer → receipt + governance ledger payload

Focus Mode answers are treated as **first-class artifacts**:
- they must include citations,
- they can be represented as derived entities with PROV links,
- they are logged to an immutable governance ledger with compliance metadata.

**Example:**
```bash
python ai_receipt.py \
  --question "How has drought impacted Kansas agriculture in the last decade?" \
  --context ./ui_state.json \
  --citations ./citations.json \
  --concepts drought,agriculture \
  --out data/audits/<run_id>/ai_answer_receipt.json
```

---

### 4) 🕸️ Weekly graph health check (QA)

A scheduled job runs health checks via Cypher to catch:
- orphan nodes,
- missing lineage edges,
- broken references to catalog assets,
- stale/expired metadata.

**Example:**
```bash
python graph_health_check.py \
  --neo4j "$NEO4J_URI" \
  --out docs/reports/qa/graph_health/
```

---

## 🧾 Run Manifest format

KFM’s ingestion patterns emphasize:
- deterministic/idempotent runs,
- JSON canonicalization (RFC 8785),
- SHA-256 digest stored back into the manifest (self-fingerprinting),
- manifests saved under `data/audits/<run_id>/run_manifest.json`.

### Minimal example (shape, not exact schema)

```json
{
  "run_id": "2026-01-21T03:14:15Z__population_county_1860_2020__v1",
  "run_time": "2026-01-21T03:14:15Z",
  "actor": "user:yourname",
  "pipeline": {
    "name": "population_county_1860_2020",
    "version": "1.0.0",
    "config_path": "pipelines/population/config.yaml"
  },
  "inputs": [
    {
      "role": "source_csv",
      "uri": "https://example.gov/census.csv",
      "retrieved_at": "2026-01-21T03:10:01Z",
      "sha256": "..."
    }
  ],
  "outputs": [
    {
      "role": "processed_table",
      "path": "data/processed/population_county_1860_2020.parquet",
      "sha256": "..."
    },
    {
      "role": "catalog_entry",
      "path": "data/catalog/datasets/population_county_1860_2020.json",
      "sha256": "..."
    }
  ],
  "tool_versions": {
    "python": "3.11.7",
    "gdal": "3.8.0"
  },
  "summary_counts": {
    "records_in": 123456,
    "records_out": 123456,
    "errors": 0
  },

  "canonical_digest": "sha256:<computed-after-RFC8785-canonicalization>",
  "idempotency_key": "sha256:<usually-same-as-canonical_digest>"
}
```

> [!TIP]
> The manifest digest doubles as an **activity identifier** that can be referenced in PROV and mirrored into Neo4j for exact “what produced this?” queries.

---

## 🧬 STAC + DCAT + PROV wiring

KFM uses a **triplet approach** (STAC + DCAT + PROV) and links them together:

- STAC can carry a PROV activity reference (or a version field that maps back to PROV).
- DCAT can point to STAC and PROV through distributions/relations.
- Neo4j mirrors the same evidence graph with nodes and edges (Dataset, Asset, Activity/Run, etc.).

> [!NOTE]
> Profiles matter: expect KFM-flavored profiles for STAC/DCAT/PROV (e.g., `kfm:dataset_id`, `kfm:classification`, sovereignty/sensitivity extensions, agent roles).

---

## 🚦 Policy gates

Policy gates should run at checkpoints (ingestion, AI inference, content publication) and enforce at minimum:

- ✅ schema validation
- ✅ STAC/DCAT/PROV completeness
- ✅ license presence (no data without known license)
- ✅ sensitivity classification (and correct handling)
- ✅ provenance completeness (inputs + processing declared)
- ✅ **citations required for AI outputs** (refuse if unsourced)

> [!IMPORTANT]
> Philosophy: **fail closed** 🚫✅. If it can’t be proven compliant, it’s blocked.

### Conftest runner (example)

```bash
conftest test data/catalog/ data/provenance/ \
  --policy "$KFM_POLICY_DIR" \
  --output table
```

### Common “must-have” rules 🔒

- 🚫 **Secrets scanning** (API keys/JWT patterns in JSON/YAML)
- 🏷️ **License allowlist** (SPDX strings)
- 🧭 **Required fields** (providers, spatial/temporal, attribution)
- 🪶 **Indigenous data sovereignty flags** when applicable

---

## 🔏 Signing + OCI publishing

KFM’s traceability flow supports publishing bundles to an OCI registry:

- publish via **ORAS** (`oras push ...`) with typed media
- link the OCI artifact back into metadata (`distribution.oci` in STAC/DCAT)
- sign artifacts with **Cosign**
- optionally attach SBOM + provenance attestations

### Example ORAS push (pattern)

```bash
oras push "$OCI_REGISTRY/$OCI_REPO:run-<run_id>" \
  --manifest-config /dev/null:application/vnd.oci.empty.v1+json \
  data/audits/<run_id>/run_manifest.json:application/vnd.kfm.runmanifest+json \
  data/provenance/<run_id>.prov.jsonld:application/ld+json \
  data/catalog/datasets/<dataset_id>.stac.json:application/json \
  data/catalog/datasets/<dataset_id>.dcat.jsonld:application/ld+json
```

### Cosign sign/verify (pattern)

```bash
cosign sign "$OCI_REGISTRY/$OCI_REPO:run-<run_id>"
cosign verify "$OCI_REGISTRY/$OCI_REPO:run-<run_id>"
```

> [!TIP]
> Policy can require “all artifacts must be signed by approved identity” before use.

---

## 🕸️ Graph registration + health checks

### Graph registration

The trace bundle should register:

- `Dataset` node (DCAT-ish)
- `Asset` nodes (STAC-ish)
- `Activity/Run` nodes (PROV-ish)
- `Agent` nodes (human / bot / CI / Focus Mode / W-P-E agents)

…and wire edges:
- `prov:used`, `prov:generated`, `prov:wasDerivedFrom`
- dataset→asset membership
- story/pulse→dataset/place references

### Graph health (scheduled QA)

A weekly report should cover:

- 🧩 missing links (dataset without prov activity; asset without dataset; story without evidence manifest)
- 🧟 orphans (nodes with no inbound/outbound relationships)
- 🧪 stale metadata (missing checksums, missing licenses, missing sensitivity labels)
- 🔁 drift (unexpected schema changes; policy failures)

Outputs should land in something like:
```text
docs/reports/qa/graph_health/graph_health_YYYYMMDD.md
docs/reports/qa/graph_health/graph_health_YYYYMMDD.json
```

---

## 🧠 AI traceability (Focus Mode + agents)

### Focus Mode receipts 🧾🤖

The AI layer should produce machine-readable receipts that capture:

- the question + UI context (bbox/time/layers)
- citations (dataset IDs, graph nodes, document IDs)
- concept nodes used (Conceptual Attention Nodes)
- policy checks applied (citation coverage, sensitivity redactions)
- governance ledger payload (append-only signed record)

**Example receipt shape (minimal):**
```json
{
  "answer_id": "ai:focusmode:2026-01-21T03:22:01Z:abcd1234",
  "question": "What does this drought index layer show?",
  "ui_context": {
    "bbox": [-101.2, 36.8, -94.6, 40.0],
    "time": {"start": "2015-01-01", "end": "2025-12-31"},
    "active_layers": ["usdm_drought_index_v2"]
  },
  "citations": [
    {"kind": "dataset", "kfm_id": "dataset:usdm_drought_index_v2", "locator": "stac:...#asset:..."}
  ],
  "concepts": ["concept:drought", "concept:agriculture"],
  "policy": {
    "citation_required": true,
    "citation_coverage": 1.0,
    "sensitivity_redactions_applied": false
  },
  "prov": {
    "entity": "prov:Entity:ai_answer",
    "wasDerivedFrom": ["prov:Entity:dataset:usdm_drought_index_v2"],
    "activity": "prov:Activity:focusmode_inference",
    "agent": "prov:Agent:focusmode_v1"
  },
  "ledger_ref": "govledger:sha256:..."
}
```

### Watcher–Planner–Executor agents 🕵️➡️🧠➡️⚙️

For automation, traceability scripts must also support:

- Watcher detection events (what changed / what triggered)
- Planner proposals (what will be done; why; required approvals)
- Executor actions (what actually ran; outputs; manifests; policy results)

> [!NOTE]
> Treat agent actions like pipelines: **manifested, validated, signed (optional), and attributable**.

---

## 🗺️ Geospatial helpers

KFM commonly uses:

- 🧱 **GeoParquet** for large vector datasets
- 🛰️ **COGs** (Cloud-Optimized GeoTIFF) for rasters
- 🧩 tiles / offline packs (e.g., PMTiles/MBTiles patterns)
- 🗃️ PostGIS for spatial DB workflows (optional)

### Import helper patterns (PostGIS)

```bash
# Example pattern (choose your preferred toolchain)
shp2pgsql -s 4326 -I input.shp public.my_layer | psql "$POSTGIS_DSN"

# Or GDAL:
ogr2ogr -f "PostgreSQL" "PG:$POSTGIS_DSN" input.shp -nln public.my_layer
```

> [!TIP]
> If you generate tiles / offline packs, treat them as artifacts too: checksum + STAC asset entry + PROV lineage + license + signatures (optional).

---

## 🧫 Privacy + sensitivity checks

Optional (but recommended when handling sensitive data):

- 🧍‍♀️ k-anonymity / l-diversity / t-closeness checks
- 🧾 query auditing patterns (track access + transformations)
- 🔐 classification enforcement (public/internal/restricted)

These checks should produce:
- a machine-readable report
- a policy gate result (pass/fail)
- provenance hooks showing transformations/redactions applied

---

## 📚 Source docs used to build this README

### Core KFM design + governance
- 📘 KFM Comprehensive Technical Documentation :contentReference[oaicite:0]{index=0}
- 🏗️ KFM Comprehensive Architecture, Features, and Design :contentReference[oaicite:1]{index=1}
- 🧭🤖 KFM AI System Overview :contentReference[oaicite:2]{index=2}
- 🧩 UI System Overview (Provenance panels, “map behind the map”) :contentReference[oaicite:3]{index=3}
- 📚 Data Intake – Technical & Design Guide (STAC/DCAT/PROV, evidence manifests) :contentReference[oaicite:4]{index=4}
- 🌟 Latest Ideas & Future Proposals (reproducible research + model outputs as traceable data) :contentReference[oaicite:5]{index=5}
- 💡 Innovative Concepts to Evolve KFM :contentReference[oaicite:6]{index=6}
- 🧠 Additional Project Ideas (run manifests, policy-as-code, OCI publishing, Conceptual Attention Nodes) :contentReference[oaicite:7]{index=7}

### Reference libraries (PDF portfolios)
- 🧠 AI Concepts & more (portfolio) :contentReference[oaicite:8]{index=8}
- 🗃️ Data Management / Architectures / Data Science / Bayesian Methods (portfolio) :contentReference[oaicite:9]{index=9}
- 🗺️ Maps + Google Maps + Virtual Worlds + Archaeological CG + Geospatial WebGL (portfolio) :contentReference[oaicite:10]{index=10}
- 🧰 Various programming languages & resources (portfolio) :contentReference[oaicite:11]{index=11}

---

## ✅ Contributing a new script (checklist)

> [!TIP]
> The fastest way to “do traceability right” is to treat scripts like pipeline contracts: stable outputs + strict validation.

- [ ] Script has `--help` and non-zero exit on failure 🧯
- [ ] Emits or references a `run_manifest.json` 🧾
- [ ] Produces (or updates) STAC/DCAT/PROV artifacts 🧬
- [ ] Runs validation + policy gates (fail-closed) 🚦
- [ ] Writes outputs into deterministic locations (`data/audits/`, `data/provenance/`, `data/catalog/`) 📂
- [ ] If publishing, pins digests + signs artifacts (optional but preferred) 🔏
- [ ] Adds/updates schema + policy tests ✅
- [ ] Updates this README (add the script + example usage) 📝

