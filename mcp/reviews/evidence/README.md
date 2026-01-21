# 🧾 MCP Review Evidence

![Evidence First](https://img.shields.io/badge/Evidence--First-Receipts%20Required-blue)
![STAC](https://img.shields.io/badge/STAC-Spatiotemporal%20Catalog-success)
![DCAT](https://img.shields.io/badge/DCAT-Data%20Catalog-success)
![PROV](https://img.shields.io/badge/PROV--O-Lineage%20%26%20Audit-informational)
![Policy as Code](https://img.shields.io/badge/Policy%20as%20Code-OPA%20%2B%20Conftest-orange)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Governance-brightgreen)

> **Receipts-only zone 🧾**  
> If a claim, dataset, map layer, Story Node, or AI output can’t point to evidence… it **doesn’t ship**.

This folder lives at: `mcp/reviews/evidence/README.md`

---

## 📌 What this folder is

This directory stores **Evidence Packs** used during **MCP (Master Coder Protocol) reviews** for the Kansas Frontier Matrix (KFM).

An Evidence Pack is the **human- and machine-reviewable “receipt bundle”** that proves:

- ✅ where data came from
- ✅ what transformations were applied (and with what config/code)
- ✅ what catalogs were updated (**STAC / DCAT / PROV**)
- ✅ what the UI shows and why (“**map behind the map**”)
- ✅ what Focus Mode said, with **citations**
- ✅ what policy gates, tests, and governance checks were passed
- ✅ what was approved (and by whom), without losing chain of custody

---

## 🧭 Quick navigation

- [🧠 Evidence-first rules](#-evidence-first-rules)
- [📦 What counts as evidence](#-what-counts-as-evidence)
- [📁 Folder layout](#-folder-layout)
- [🏷️ Naming and immutability](#️-naming-and-immutability)
- [🧾 Evidence Manifest](#-evidence-manifest-em-yamljson)
- [🏃 Run Manifest](#-run-manifest-rm-json)
- [🔄 Review workflow](#-review-workflow)
- [✅ Review checklists](#-review-checklists)
- [🔐 Security privacy and sovereignty](#-security-privacy-and-sovereignty)
- [🩺 Recurring audits](#-recurring-audits)
- [🤝 Community verification](#-community-verification)
- [🧰 Templates](#-templates)
- [📚 Related docs](#-related-docs)

---

## 🧠 Evidence-first rules

KFM is built on three non-negotiables:

1. **Provenance-first**: every published output must be traceable to sources and steps.
2. **Determinism**: given the same inputs + config, pipelines should reproduce the same outputs.
3. **Fail-closed governance**: missing provenance, missing licenses, missing sensitivity labels, or missing citations should block publication.

> 🧩 Rule of thumb: **“If it can’t be audited, it can’t be merged.”**

---

## 📦 What counts as evidence

Evidence Packs can include any combination of:

- 📚 **Primary sources**: PDFs, scans, archives, official documents, citations, page/line locators  
- 📊 **Datasets**: dataset IDs, query URLs, STAC items/collections, DCAT records
- 🧮 **Queries & calculations**: SQL, notebooks, scripts, parameter files, outputs + hashes
- 🧾 **Catalog & lineage**: STAC / DCAT / PROV fragments or references
- 🧪 **QA evidence**: schema validation, link checks, unit tests, diff reports, graph integrity checks
- 🖼️ **UI proof**: screenshots/gifs showing before/after layers + attribution visible
- 🔐 **Security proof**: SBOMs, signatures (cosign), attestations (e.g., SLSA/in-toto), scan results
- 🧑‍⚖️ **Governance artifacts**: approvals, waivers (with expiry), council notes (when needed)

### 🚫 What does *not* belong here
- 🔑 secrets (tokens, keys, credentials)
- 🧬 raw sensitive/PII data (store **references + redacted samples**, never raw)
- 🪨 huge binaries unless absolutely necessary (use OCI artifacts; store **digests + manifests** here)

---

## 📁 Folder layout

Recommended structure (adjust as needed, but keep it review-friendly):

```text
mcp/
└─ 🧠 reviews/
   └─ 📎 evidence/
      ├─ 📄 README.md                         # 📘 How to store review evidence + required artifacts + linking conventions
      ├─ 🧩 templates/
      │  ├─ 🧩🧾 evidence_manifest.template.yaml # Template: evidence index (citations, artifacts, checksums, reviewers)
      │  └─ 🧩🧾 run_manifest.template.json      # Template: run ledger (commands, env, inputs/outputs, hashes)
      │
      └─ ✅ MCP-0001-example/                 # Example evidence bundle (one folder per review/change)
         ├─ 📝📄 summary.md                    # Human summary: what was tested, what passed/failed, and key findings
         ├─ 🧾 evidence_manifest.yaml          # Evidence index: artifacts + citations + checksums + pointers to catalogs
         ├─ 🧾 run_manifest.json               # Run manifest: exact steps to reproduce + versions + digests
         │
         ├─ 🗂️ catalogs/                      # Optional: copied snippets or references (avoid duplicating huge catalogs)
         │  ├─ 🛰️ stac/                       # STAC items/collections or pointers used as evidence
         │  ├─ 🗂️ dcat/                       # DCAT dataset/distribution snippets or pointers
         │  └─ 🧬 prov/                       # PROV bundles/snippets or pointers (lineage proof)
         │
         ├─ 📦 artifacts/                     # Supporting artifacts produced/collected during validation
         │  ├─ 🪵 logs/                       # Logs/traces (sanitize secrets/PII)
         │  ├─ 📝 reports/                    # Reports (markdown/pdf) summarizing results
         │  ├─ 📸 screenshots/                # Screenshots used to verify UI/behavior (redacted)
         │  └─ 📓 notebooks/                  # Notebook exports or links (prefer minimal, reproducible artifacts)
         │
         └─ 🔏 signatures/
            └─ 🔐 cosign/                     # Signature/attestation pointers (or exported refs) for supply-chain proofs
```

---

## 🏷️ Naming and immutability

### ✅ Naming convention (recommended)
- Evidence Pack folder: `MCP-####-short-slug/`
- Evidence manifest: `evidence_manifest.yaml` (or `EM-####.yaml`)
- Run manifest: `run_manifest.json` (or `RM-<run_id>.json`)
- PROV bundle: `prov/bundle.jsonld`

### 🧊 Immutability rules
Evidence is **append-only**.

- Don’t edit history to “fix” evidence.
- If something changes, **create a new Evidence Pack** (or add a new `rev/` inside the pack).
- Prefer **content-addressed references** (hashes/digests) wherever possible.

---

## 🧾 Evidence Manifest (EM) YAML/JSON

The **Evidence Manifest** is the machine-readable inventory of evidence supporting a change.

It should answer, quickly:

- What did you use?
- Exactly where is it?
- Exactly which part was used (page/line/query slice)?
- What did you produce?
- What claims does this support?

### ✅ Suggested fields
- `id`, `title`, `created_at`
- `scope` (MCP id, PR id, component: `data|ui|ai|story|infra`)
- `sensitivity` (classification + notes)
- `items[]` (each source/dataset/query/screenshot/etc)
- `transforms[]` (if any)
- `outputs[]` (what this change produces)
- `prov` (links to PROV bundle)
- `review` (requested reviewers, approvals)

---

## 🏃 Run Manifest (RM) JSON

The **Run Manifest** is the audit record for pipelines and automated updates (ingests, watchers, transforms).

Minimum fields (strongly recommended):

- `run_id`, `run_time`
- `idempotency_key`
- `canonical_digest` (hash of canonicalized manifest)
- `source_urls` or dataset IDs
- `tool_versions` + environment metadata
- `summary_counts` (records in/out/errors)
- `outputs` (paths/digests)

> 💡 If the pipeline is “exactly-once” or idempotent, the Run Manifest is where reviewers confirm that property.

---

## 🧬 Evidence flow

```mermaid
flowchart LR
  A[Source 📄/📊/🗺️] --> B[Raw ingest 🧊 (immutable)]
  B --> C[Deterministic pipeline ⚙️]
  C --> D[STAC/DCAT/PROV catalogs 🧾]
  D --> E[Neo4j + PostGIS 🕸️]
  E --> F[UI “map behind map” 🧭]
  E --> G[Focus Mode 🔎🤖 (citations)]
  C --> H[Run Manifest (RM) 🧾]
  F --> I[Story Node / Pulse Thread ✍️]
  I --> J[Evidence Manifest (EM) 🧾]
  J --> K[Review ✅]
```

---

## 🔄 Review workflow

1. **Intake**
   - Create Evidence Pack folder
   - Add EM (+ RM if pipelines were run)
   - Reference or include STAC/DCAT/PROV

2. **Automated policy gates**
   - Schema checks
   - License checks
   - STAC/DCAT/PROV completeness checks
   - Sensitivity / sovereignty checks
   - Citation rules (stories + AI outputs must cite sources)
   - Provenance-first publishing rules

3. **Human review**
   - Reviewers inspect EM/RM, spot-check sources
   - Re-run key steps when needed (or verify digests)

4. **Council / ethics review (when applicable)**
   - Triggered for sensitive, high-stakes, or sovereignty-governed datasets
   - Includes ethical screening + FAIR/CARE + sustainability + accessibility

5. **Approval & merge**
   - Merge happens only after both **policy gates** and **human oversight**
   - Merge is recorded via governance/provenance logs

---

## ✅ Review checklists

### 📦 Data ingestion / dataset update
- [ ] Raw inputs referenced and treated as immutable evidence
- [ ] Deterministic pipeline or documented method (no “mystery steps”)
- [ ] **STAC** collection/items present or referenced
- [ ] **DCAT** dataset/distributions present or referenced
- [ ] **PROV** bundle present or referenced
- [ ] License is explicit and compatible
- [ ] Sensitivity classification set and propagated to outputs
- [ ] Run Manifest included (RM) for automated ingestion
- [ ] Policy gates pass

### 🗺️ Story Node / Pulse Thread
- [ ] Human-readable citations block exists
- [ ] Evidence Manifest enumerates each source + locator/query slice
- [ ] PROV links story/pulse to evidence + author/AI agent
- [ ] Any AI-assisted text is labeled as such
- [ ] Each major claim maps to one or more evidence IDs

### 🔎 Focus Mode / AI change
- [ ] Change has evaluation evidence (tests / benchmarks / samples)
- [ ] Outputs include citations; unsupported answers refuse/flag uncertainty
- [ ] Governance flags handled (sensitive data rules)
- [ ] Refusal + safety tests included (where relevant)

### 🖥️ UI / map layer change
- [ ] Screenshot(s) show before/after + attribution visible
- [ ] Provenance discoverable (“map behind the map” path works)
- [ ] Tiles/artifacts referenced by digest (OCI if external)
- [ ] Accessibility checks evidenced (keyboard, screen size, contrast, etc.)

---

## 🔐 Security privacy and sovereignty

Evidence is powerful — so it must be safe.

**Always include a classification label** and apply these rules:

- **No secrets**: never store tokens/keys.
- **No raw sensitive exports**: store references, redactions, aggregates, or protected access pointers.
- **Classification must propagate**: outputs cannot be “less restricted” than their inputs.
- **Sovereignty-aware review**: culturally sensitive sites, endangered species, sacred locations, etc. need extra review and/or generalization.

> 🧯 When in doubt: **redact, aggregate, and require review**.

---

## 🩺 Recurring audits

This folder can also store **scheduled proof** that the system is healthy, e.g.:

- 🕸️ Graph integrity checks (orphan nodes, broken links, drift)
- 🧾 Metadata completeness audits
- 🔐 Signature verification spot-checks
- 📉 Sustainability / compute accountability snapshots (when tracked)

Suggested pattern:

```text
mcp/reviews/evidence/
  AUDIT-YYYY-MM/
    summary.md
    artifacts/reports/
    artifacts/logs/
    evidence_manifest.yaml
```

---

## 🤝 Community verification

Some evidence benefits from humans-in-the-loop:

- “second pair of eyes” checks on OCR excerpts
- cross-checking citizen contributions with official layers
- moderator verification badges / approval notes
- dispute resolution packets (what changed, why, and who approved)

If community verification was used, record:
- what was verified
- verification method
- verifier identity (or role)
- timestamp + decision outcome

---

## 🧰 Templates

<details>
<summary>📄 evidence_manifest.template.yaml (click to expand)</summary>

```yaml
id: EM-0000
title: "Evidence pack title"
created_at: "2026-01-20T00:00:00Z"

scope:
  mcp_id: MCP-0000
  pr: 0
  component: "data|ui|ai|story|infra"

sensitivity:
  classification: public # public|sensitive|confidential
  notes: ""

items:
  - id: EV-001
    kind: dataset # dataset|document|image|query|code|run|ui-screenshot
    title: "USGS gauge dataset"
    ref:
      dcat: "data/catalogs/dcat/usgs_gauge.jsonld"
      stac: "data/stac/collections/usgs_gauge/collection.json"
    checksum:
      algo: sha256
      value: "<sha256>"
    locator: "query: max(stage) for 1908"
    used_for:
      - claim_id: CL-001
        claim: "Peak stage in 1908 was ..."
        narrative_ref: "story_nodes/flood_1908.md#CL-001"

transforms:
  - id: TR-001
    description: "Monthly aggregation"
    run_manifest: "run_manifest.json"

outputs:
  - id: OUT-001
    kind: stac-item
    path: "data/stac/items/usgs_gauge/1908.json"

prov:
  bundle: "catalogs/prov/bundle.jsonld"

review:
  requested_reviewers: ["@maintainer"]
  approvals: []
```
</details>

<details>
<summary>⚙️ run_manifest.template.json (click to expand)</summary>

```json
{
  "run_id": "RUN-2026-01-20T00-00-00Z",
  "run_time": "2026-01-20T00:00:00Z",
  "idempotency_key": "<optional>",
  "canonical_digest": "sha256:<computed-after-canonicalization>",
  "source_urls": [],
  "tool_versions": {},
  "summary_counts": { "records_in": 0, "records_out": 0, "errors": 0 },
  "outputs": []
}
```
</details>

---

## 📚 Related docs

Within the repo (typical locations):
- 🧾 **Catalogs**: `data/stac/`, `data/catalogs/dcat/`, `data/prov/`
- ⚖️ **Policy pack**: `api/scripts/policy/` (OPA + Conftest)
- 🕸️ **Graph ingestion**: catalogs → Neo4j/PostGIS import pipeline
- ✍️ **Narratives**: `story_nodes/` (Story Nodes + Pulse Threads)
- 🔐 **Artifact distribution**: OCI registry + signing (cosign)

---

### 🧩 Final reminder

✅ Reviewers can ignore extra receipts.  
❌ Reviewers cannot approve missing receipts.

**When in doubt: add more evidence.**
