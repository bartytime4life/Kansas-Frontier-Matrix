# 🧾 `dev_prov` Scripts — Developer Provenance Toolkit (MCP)

![Provenance](https://img.shields.io/badge/provenance-first%20✅-2ea44f)
![W3C PROV-O](https://img.shields.io/badge/W3C-PROV--O-2b579a)
![STAC](https://img.shields.io/badge/STAC-metadata-blue)
![DCAT](https://img.shields.io/badge/DCAT-catalog-blueviolet)
![OPA + Conftest](https://img.shields.io/badge/OPA%20%2B%20Conftest-policy--as--code-orange)
![OCI](https://img.shields.io/badge/OCI-artifacts-555)
![Sigstore Cosign](https://img.shields.io/badge/Sigstore-Cosign-6f42c1)
![Neo4j](https://img.shields.io/badge/Neo4j-graph-018bff)
![PostGIS](https://img.shields.io/badge/PostGIS-geo-2c7fb8)

> [!IMPORTANT]
> **KFM is “provenance-first.”** If a change produces or updates *data, narratives, models, or AI outputs*, the change should also ship **lineage evidence** (PROV) and **catalog metadata** (STAC/DCAT), then pass **policy gates** before promotion. ✅

---

## 📍 Where you are

This README documents the scripts living under:

- 📁 `mcp/` → Master Coder Protocol / methods / reproducible workbench 🧪  
- 📁 `dev_prov/` → developer provenance (code + data + AI + CI lineage) 🧬  
- 📁 `scripts/` → small, boring CLIs that **generate, validate, package, and publish** provenance artifacts 🧾

---

## 🧠 What these scripts are for

These scripts exist to make provenance **easy to do correctly** and **hard to skip**.

They support (at minimum):

- 🧬 **PROV lineage** for datasets, model runs, derived outputs, and AI outputs  
- 🗂️ **Catalog metadata** alignment (STAC + DCAT + references into PROV)  
- 🧾 **Run Manifests** (deterministic “what ran, what it used, what it produced”)  
- 🧾 **Evidence Manifests** (claims → citations → datasets/docs/graph entities)  
- 🧷 **Policy gates** (OPA + Conftest) for provenance-first publishing + FAIR/CARE  
- 🧪 **Graph health checks** (integrity, constraints, drift detection)  
- 📦 **OCI artifact publishing** (ORAS) + 🔏 **signing/attestation** (Cosign/SLSA)  

---

## 🗺️ Big-picture flow (how provenance moves through KFM)

```mermaid
flowchart LR
  A[data/raw 🧱] --> B[data/processed 🧼]
  B --> C[STAC/DCAT/PROV 🗂️🧬]
  C --> D[Neo4j CSV import 🧠]
  D --> E[UI layers + Story Nodes 🗺️📖]
  E --> F[Focus Mode answers 🧠💬 (with citations)]

  subgraph dev_prov_scripts[dev_prov scripts 🧾]
    S1[run_manifest 🧾] --> C
    S2[evidence_manifest 🧷] --> E
    S3[validate + policy ✅] --> C
    S4[publish_oci + sign 🔏] --> G[(OCI Registry 📦)]
  end
```

---

## 📦 Folder map (recommended structure)

> [!NOTE]
> Your repo may vary. Treat this as the **target convention** so policy + CI + humans all agree on where artifacts live.

```text
📦 mcp/dev_prov/
└─ 📁 scripts/
   ├─ 📄 README.md                      👈 you are here
   ├─ 🐍 prov_pr_to_jsonld.py            (GitHub PR → PROV-O JSON-LD)
   ├─ 🐍 make_run_manifest.py            (pipeline run manifest + digests)
   ├─ 🐍 make_evidence_manifest.py        (claims/citations pack for Story Nodes / Pulse Threads)
   ├─ 🐍 validate_prov_bundle.py          (schema + policy validation)
   ├─ 🐍 graph_health_check.py            (Neo4j integrity checks + report output)
   ├─ 🐚 oci_push.sh                     (publish artifacts via ORAS)
   ├─ 🐚 oci_sign.sh                     (cosign sign + attach attestations)
   └─ 📁 schemas/
      ├─ 📄 run_manifest.schema.json
      └─ 📄 evidence_manifest.schema.json
```

---

## 🚀 Quickstart

### 1) Prereqs (local dev)
Pick the subset you need:

- 🐍 Python (for JSON/JSON-LD generation + validation)
- 🧰 `jq` / `yq` (helpful for inspection)
- 🛡️ `conftest` (OPA policy checks)
- 📦 `oras` (OCI artifact push/pull)
- 🔏 `cosign` (sign artifacts + attach attestations)
- 🧠 Neo4j access (for graph health checks)

> [!TIP]
> Keep scripts **dependency-light**. CI should be able to run these in a minimal container.

### 2) Run a script (pattern)
From repo root:

```bash
# example pattern — update to match your actual filenames/entrypoints
python mcp/dev_prov/scripts/make_run_manifest.py --help
python mcp/dev_prov/scripts/validate_prov_bundle.py --help
```

---

## 🧩 Script contract (make every script “CI-friendly”)

All scripts in this folder should follow these rules:

1. ✅ **Deterministic output**  
   - stable ordering, no random IDs, no timestamps unless explicitly part of the contract  
2. ♻️ **Idempotent**  
   - rerunning with same inputs yields identical files (byte-for-byte if possible)  
3. 🧾 **Machine output first**  
   - write artifacts to `--out` paths  
   - human logs go to stderr  
4. 🧪 **Exit codes matter**  
   - `0` pass, `1` validation fail, `2+` runtime error  
5. 🔒 **Fail-closed**  
   - missing provenance or missing citations should be a hard error in validation mode  
6. 🧷 **Include trace hooks**  
   - link outputs to dataset IDs, run IDs, graph IDs, PR IDs, etc.

---

## 🧱 Core artifacts (contracts)

### 🧾 Run Manifest
A Run Manifest is a *deterministic ledger* of a pipeline run.

It should capture:

- 🆔 `run_id` (stable + meaningful)
- 🧩 pipeline name + version
- 🧾 inputs (URLs, dataset IDs, digests)
- 📦 outputs (paths + digests)
- 🧬 link to PROV entity/activity IDs
- 🧷 policy results (pass/fail + rule IDs)
- 🔏 signatures / attestation references (optional but recommended)

**Example (shape only):**
```json
{
  "run_id": "kfm.run.2026-02-01.purpleair.v2",
  "pipeline": {
    "name": "pipelines/purpleair_ingest",
    "version": "git:abcdef123"
  },
  "inputs": [
    {
      "type": "url",
      "uri": "https://example.gov/data.csv",
      "digest": "sha256:..."
    }
  ],
  "outputs": [
    {
      "path": "data/processed/air_quality/purpleair.parquet",
      "digest": "sha256:..."
    },
    {
      "path": "data/prov/air_quality/purpleair.prov.jsonld",
      "digest": "sha256:..."
    }
  ],
  "policy": {
    "conftest": {
      "passed": true,
      "ruleset": "tools/validation/policy/"
    }
  },
  "attestations": {
    "oci_ref": "oci://registry/org/kfm/purpleair:2026-02-01",
    "cosign": {
      "signed": true,
      "bundle_ref": "oci://...#attestation"
    }
  }
}
```

---

### 🧷 Evidence Manifest
Evidence Manifests are for **Story Nodes**, **Pulse Threads**, and anything narrative.

They should tie:

- ✍️ a claim / statement / paragraph
- 🔗 to citations (datasets, documents, graph entities)
- 🧬 to provenance context (PROV IDs + dataset IDs)
- 🧭 to sensitivity / access classification (FAIR/CARE, cultural protocols)

**Example (shape only):**
```json
{
  "story_id": "story.dust_bowl.county.douglas",
  "claims": [
    {
      "id": "c1",
      "text": "Douglas County experienced severe drought impacts in the 1930s.",
      "citations": [
        { "type": "dataset", "dataset_id": "kfm.ks.climate.drought.v1" },
        { "type": "document", "doc_id": "doc.dustbowl_report.1936" }
      ],
      "links": {
        "prov": "prov:Entity:kfm.focus.answer.123",
        "graph_entities": ["kg:County:Douglas_KS", "kg:Event:DustBowl_1930s"]
      },
      "governance": {
        "sensitivity": "public",
        "care_tags": []
      }
    }
  ]
}
```

---

### 🧬 PROV JSON-LD (W3C PROV-O)
PROV is the lineage backbone:

- **Entity** = data/artifact (dataset, file, model output, AI answer)  
- **Activity** = process (pipeline run, PR merge, AI generation step)  
- **Agent** = actor (human, bot, CI system, reviewer)  

**DevOps integration (key dev_prov idea):**
- PRs become **PROV Activities**
- commits become **PROV Entities**
- authors/reviewers become **PROV Agents**
- relationships (`prov:used`, `prov:wasAssociatedWith`, `prov:wasGeneratedBy`) connect them

---

## ✅ Validation & policy gates

These scripts should be callable in CI to enforce rules like:

- 🧱 **Pipeline ordering** (no “later-stage” artifacts without “earlier-stage” outputs)
- 🧬 **Provenance-first publishing** (data changes require matching PROV updates)
- 🧷 **Evidence rules** (AI outputs + Story Nodes must include citations)
- 🧭 **Sensitivity rules** (CARE/cultural protocol tags enforce differential access)

**Typical local check pattern:**
```bash
# update these paths to match repo structure
conftest test -p tools/validation/policy data/prov data/stac data/catalog/dcat
```

> [!TIP]
> Pair policy checks with **schema validation** (JSON Schema) and **content validation** (e.g., required fields + stable IDs).

---

## 📦 Publishing artifacts to OCI (optional but powerful)

KFM can treat provenance bundles like container artifacts:

- 📦 publish with **ORAS**
- 🔏 sign with **Cosign**
- 🧬 attach PROV JSON-LD / run manifests as referrers/attestations
- 🔐 use registry permissions for restricted datasets

**Workflow sketch:**
```bash
# push a bundle (data + metadata)
./mcp/dev_prov/scripts/oci_push.sh \
  --artifact-dir data/audits/kfm.run.2026-02-01.purpleair.v2 \
  --ref oci://registry/org/kfm/purpleair:2026-02-01

# sign + attach attestations
./mcp/dev_prov/scripts/oci_sign.sh \
  --ref oci://registry/org/kfm/purpleair:2026-02-01
```

---

## 🧠 Focus Mode + UI integration (why citations matter)

Focus Mode and the UI are designed so that:

- 💬 AI answers are **context-aware** (map layers, selected feature, timeline)  
- 🧷 Every answer includes **clickable citations** (datasets/docs/entities)  
- 🧬 Derived outputs (including AI summaries) carry PROV lineage so audits can trace “why”  

**Practical outcome:**  
If the AI can’t cite evidence, it should *refuse* rather than hallucinate. ✅

---

## 🧭 Sensitivity, CARE, and cultural protocols

Provenance is not only “where it came from” — it also includes:

- 🧭 sensitivity level (public / sensitive / restricted)
- 🪶 cultural protocols and community-defined access rules
- 🧑‍🤝‍🧑 credit to contributors and knowledge holders

Your dev_prov artifacts should carry these governance tags so:

- policy can enforce them automatically ✅  
- UI can apply redaction/obfuscation where required 🕶️  
- exports can include appropriate provenance summaries 📎  

---

## 🧰 Adding a new script (checklist)

When you add a script to this folder:

- [ ] Give it a **single responsibility** (generate *or* validate *or* publish)
- [ ] Add `--help`, `--in`, `--out`, and `--strict`
- [ ] Make outputs deterministic + idempotent ♻️
- [ ] Add a tiny fixture under `mcp/dev_prov/scripts/fixtures/` (if used)
- [ ] Add CI wiring (or document how CI calls it)
- [ ] Update the **Script Catalog** section in this README ✅

---

## 📚 Project docs this folder implements

These scripts operationalize the design described across KFM’s docs:

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**  
- 🏗️ **KFM – Comprehensive Architecture, Features, and Design**  
- 🧭🤖 **KFM – AI System Overview** (citations + PROV enforcement + policy pack)  
- 🖥️ **KFM – Comprehensive UI System Overview** (citations UX + evidence-first UI)  
- 📥 **KFM Data Intake – Technical & Design Guide** (STAC/DCAT/PROV pipeline + W-P-E)  
- 💡 **Additional Project Ideas** (OCI artifacts, run manifests, pulse ideas)  
- 🌟 **Latest Ideas & Future Proposals** (idempotency, kill-switch, supply-chain attestations)  
- 🧭 **Innovative Concepts to Evolve KFM** (sensitivity-aware governance, AR/digital twins, GeoXAI)

Reference compendiums (deep background / curated reading 📚):
- 🤖 **AI Concepts & more** (portfolio)
- 🗺️ **Maps / Google Maps / Virtual Worlds / Geospatial WebGL** (research pack)
- 🧰 **Various programming languages & resources** (portfolio)
- 🧠 **Data Management / Architectures / Data Science / Bayesian Methods** (portfolio)

> [!NOTE]
> If a PDF is a *portfolio* or not text-indexed, consider extracting the relevant sub-docs into `/docs/` as markdown over time for easier cross-linking and automation.
