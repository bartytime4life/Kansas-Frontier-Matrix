# 05 — GitHub PR ➜ PROV (JSON‑LD) 🧬🔀✅

![Example](https://img.shields.io/badge/example-05-blue)
![Module](https://img.shields.io/badge/module-dev__prov-6f42c1)
![MCP](https://img.shields.io/badge/MCP-tooling-0aa)
![W3C PROV](https://img.shields.io/badge/W3C-PROV--O-success)
![Format](https://img.shields.io/badge/format-JSON--LD-orange)
![Workflow](https://img.shields.io/badge/GitOps-PR%20as%20evidence-black)

Turn a GitHub Pull Request into a **W3C PROV‑O compatible** provenance record (serialized as **JSON‑LD**) so KFM can answer:

- 🧾 *“Which PR created this dataset (and who reviewed it)?”*
- 🧩 *“Which code + configs + pipelines produced these outputs?”*
- 🧭 *“Can the UI show the ‘map behind the map’ (lineage + citations)?”*

This example is the **Dev‑Provenance bridge** between everyday GitHub work and KFM’s “evidence‑first” stack.

---

## 🎯 What this example demonstrates

✅ **Extract** a PR’s facts (author, reviewers, commits, changed files, CI checks)  
✅ **Translate** them into a PROV graph (Agents / Activities / Entities + relationships)  
✅ **Serialize** to **PROV JSON‑LD** (deterministic, hashable, reviewable)  
✅ **Optionally ingest** into the KFM Knowledge Graph (e.g., Neo4j)  
✅ **Make it enforceable** in CI as “policy-as-code” (fail the PR if provenance is missing)

---

## 🧠 Why PR ➜ PROV is a “KFM‑native” move

KFM is built around a single rule:

> If it shows up in the UI or Focus Mode, it must be **traceable** back to **cataloged sources** and **provable processing**.

A GitHub PR is already an auditable unit of change. This example makes it **queryable evidence**.

---

## 📦 Outputs

Typical outputs you want from this example:

```text
mcp/dev_prov/examples/05_github_pr_to_prov/
├── ✅📄 README.md                       # 👈 you are here 📌 How to generate/validate PR→PROV links + required fields
└── 📦 out/
    ├── 🧬🧾 prov.pr_<N>.jsonld           # PR-level W3C PROV-O (JSON-LD): PR/commits/reviews → produced artifacts
    ├── 🧾🔐 run_manifest.json            # Deterministic run metadata + hashes (inputs/outputs/tool versions/checksums)
    └── 📝📄 summary.md                   # (optional) Reviewer-friendly synopsis: what changed + evidence pointers + risks
```

> 💡 In a full KFM workflow, the `prov*.jsonld` file is committed under `data/provenance/` (or referenced as an artifact referrer) and becomes part of the “evidence graph.”

---

## 🗺️ High-level flow

```mermaid
flowchart LR
  A[GitHub Pull Request] --> B[Fetch PR metadata<br/>commits, reviews, files, checks]
  B --> C[Normalize + Canonicalize<br/>stable ordering, IDs, timestamps]
  C --> D[Emit run_manifest.json<br/>inputs, env, hashes]
  C --> E[Emit PROV JSON-LD<br/>Agents/Activities/Entities]
  E --> F[(Optional) Ingest to Neo4j<br/>dev history becomes queryable lineage]
  D --> G[CI Policy Gates<br/>OPA/Conftest style checks]
  E --> G
  G --> H[Human Review + Merge ✅]
```

---

## 🧰 Tool interface contract (recommended)

Because this lives under `mcp/dev_prov/…`, the cleanest shape is a **single tool** with a stable input/output contract.

### Inputs (suggested)

| Field | Type | Required | Notes |
|------:|------|:--------:|------|
| `repo` | string | ✅ | `OWNER/REPO` |
| `pr_number` | int | ✅ | PR number |
| `include_files` | bool | ✅ | Usually `true` |
| `include_reviews` | bool | ✅ | Usually `true` |
| `include_checks` | bool | ⚠️ | CI status, workflow runs, etc. |
| `out_dir` | string | ✅ | Default `./out` |
| `validate` | bool | ✅ | Schema + sanity checks |
| `ingest_to_graph` | bool | ⚠️ | If enabled, writes to Neo4j/graph loader |
| `id_namespace` | string | ⚠️ | e.g. `urn:kfm:` |

### Outputs (suggested)

| Field | Type | Notes |
|------:|------|------|
| `prov_jsonld_path` | string | Generated PROV JSON‑LD |
| `run_manifest_path` | string | Canonical run metadata |
| `summary_path` | string | Optional reviewer synopsis |
| `prov_root_id` | string | Root Activity ID |
| `hashes` | object | SHA256 digests for determinism |

---

## 🧬 PROV mapping model

This example should produce a PROV graph where:

### PROV Agents 🧑‍💻🤖
- **PR author** → `prov:Agent`
- **Reviewers** → `prov:Agent`
- **Automation / CI runner / bot** → `prov:Agent` (softwareAgent)

### PROV Activity ⚙️
- The **Pull Request lifecycle** (or merge event) → `prov:Activity`

### PROV Entities 📄
- Commits, diffs, changed files, artifacts (build outputs), manifests → `prov:Entity`

### Key relationships 🔗
- `prov:wasAssociatedWith` (Activity ↔ Agent)
- `prov:used` (Activity → input Entities like base commit, changed files)
- `prov:wasGeneratedBy` (output Entities ← Activity)
- `prov:wasDerivedFrom` (output file entities derived from prior versions)

---

## 🧾 Naming & ID conventions

Keep IDs boring and deterministic:

- `urn:github:pr:OWNER/REPO#123`
- `urn:git:commit:<sha>`
- `urn:git:file:<path>@<sha>`
- `urn:kfm:run:<run_id>`

**Rule of thumb:** if you can’t re-generate the same IDs on a replay run, the graph won’t diff cleanly.

---

## 🧱 Determinism, hashing, and “reviewable evidence”

To make provenance *actually useful* in code review:

- ✅ JSON‑LD output should be **stable** between runs for the same PR state
- ✅ Emit a `run_manifest.json` with:
  - tool version
  - input parameters
  - GitHub API URLs queried
  - commit SHAs / PR head SHA
  - checksums for emitted files
  - idempotency key

> 🔒 Optional hardening: sign provenance artifacts (and/or attach them as referrers in an OCI registry) so the “evidence stack” has supply‑chain integrity.

---

## 🧑‍⚖️ Policy gates (how this becomes enforceable)

A minimal set of CI gates KFM-style:

- ✅ **If data/processed/** changes → must include **data/provenance/** updates
- ✅ **If new datasets** → must have STAC + DCAT + PROV
- ✅ **If AI outputs** → must include at least one citation (and be labeled)
- ✅ **No bypass**: agent PRs are treated exactly like human PRs
- ✅ **Kill-switch** exists for automation (emergency freeze)

This example’s role is to make “PR evidence” **machine-checkable**, not vibes‑based.

---

## 🧭 How this connects to KFM UI + Focus Mode

Once PR history is PROV:

- 🗺️ UI can surface “**map behind the map**”:
  - dataset → provenance → pipeline run → PR → reviewers → source citations
- 🔎 Focus Mode can answer with **backed citations** and log its own “used” entities in PROV when it queries real-time data or derived outputs.

---

## 🔐 Security & privacy notes

- 🔑 Use least-privilege GitHub tokens (read PR metadata; optionally read checks).
- 🧼 Never write secrets to provenance files.
- 🏷️ If a PR touches sensitive data or culturally restricted knowledge:
  - add classification + access rules at the metadata level
  - ensure provenance records preserve authority/consent constraints (CARE‑aware thinking)

---

## 🧯 Troubleshooting checklist

- **401/403 from GitHub** → token scopes / GitHub App permissions
- **Non-deterministic PROV output** → sort keys, canonicalize arrays, normalize timestamps
- **Graph ingest fails** → validate IDs, ensure stable node keys, avoid duplicates
- **Policy fails (expected)** → provenance is missing or doesn’t match changed artifacts

---

## 🧪 Suggested “Definition of Done” ✅

Before calling this example complete:

- [ ] Generates **valid PROV‑O JSON‑LD**
- [ ] Output is **deterministic** for a fixed PR state
- [ ] Emits a **run_manifest.json** with hashes
- [ ] Includes Agents (author/reviewers/bot), Activity (PR/merge), Entities (commits/files)
- [ ] Optional: exports a Neo4j-friendly ingest format (CSV or direct Cypher)
- [ ] Optional: CI policy gate can assert “PR evidence exists”

---

## 📚 Project references used by this example

KFM “source of truth” documents (design + architecture):

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🧱 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**
- 🧭🤖 **Kansas Frontier Matrix (KFM) – AI System Overview**
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview**
- 📥 **KFM Data Intake – Technical & Design Guide**
- 🌟 **KFM – Latest Ideas & Future Proposals**
- 💡 **Innovative Concepts to Evolve KFM**
- 🧪 **Additional Project Ideas**

Reference libraries (background bundles):

- 🤖 **AI Concepts & more** (portfolio / reading bundle)
- 🗺️ **Maps‑GoogleMaps‑VirtualWorlds‑Archaeological‑Computer Graphics‑Geospatial‑webgl** (portfolio / geospatial reading bundle)
- 🧰 **Various programming languages & resources 1** (portfolio / engineering reading bundle)
- 🗄️ **Data Management / Architectures / Bayesian Methods / Programming Ideas** (portfolio / data-systems reading bundle)
