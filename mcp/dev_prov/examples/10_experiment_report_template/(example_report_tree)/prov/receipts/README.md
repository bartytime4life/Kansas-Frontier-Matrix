# 🧾 Receipts — `prov/receipts/`

`🧬 provenance-first` `🔒 tamper-evident` `🧪 reproducible` `🧭 audit-ready`

Welcome to **Receipts** — the place where we store *verifiable evidence artifacts* that back the provenance graph (`prov/`) and the human-readable experiment report.

> If it’s not in `prov/receipts/`, it didn’t happen…  
> (…or at least: it isn’t **provable** 😉)

---

## 🎯 What belongs in `receipts/`

Receipts are **raw, machine-checkable evidence** captured during:
- 🌐 **fetching** inputs (HTTP headers, status codes, timestamps)
- 🔐 **verifying integrity** (hash lists, digests)
- 🧰 **capturing environment** (tool versions, lockfiles, runtime fingerprints)
- 🧭 **running policy gates** (validation outputs, policy decision logs)
- 🧷 **supply-chain verification** (signatures, attestations, SBOMs)
- 🗺️ **geospatial transforms** (CRS/reprojection logs, tile build configs)
- 🤖 **AI-assisted steps** (redacted prompts, model + config IDs, evaluation specs)
- 🧪 **experimental procedures** (seed logs, parameter snapshots, run manifests)

Receipts are designed so the system can answer questions like:
- “Which exact inputs produced this output?”  
- “What tool versions were used?”  
- “Can I reproduce this run byte-for-byte?”  
- “What policies were checked—and what did they decide?”  

---

## 🚫 What does *not* belong here

### ❌ Not allowed
- **Secrets** (tokens, keys, passwords), ever
- **Sensitive personal data** (unless explicitly permitted and redacted)
- “Mystery blobs” without hashes + context

### ❌ Not recommended
- **Huge artifacts** (store those in artifact storage; reference them by digest)
- Raw datasets (those live in `data/` or referenced externally by immutable ID)

> 🧯 Pro tip: Prefer **pointers + hashes** over copying large files.

---

## 🧱 Golden rules (non-negotiable)

✅ **Deterministic names:** predictable file names, stable directory structure  
✅ **Immutable mindset:** append new receipts; don’t “rewrite history”  
✅ **Everything hashed:** receipts should be listed in a checksum file  
✅ **Cross-linkable:** receipts must be referenceable from PROV + report text  
✅ **Redact aggressively:** store *proof*, not private content

---

## 📦 Recommended folder layout

Below is a suggested structure. Customize if your domain needs it, but keep the spirit: *evidence-first + navigable + machine-friendly*.

```text
prov/receipts/
├─ README.md
├─ receipts.index.json                 # 🔎 machine index of all receipt artifacts
│
├─ integrity/                          # 🔐 tamper evidence
│  ├─ checksums.sha256
│  └─ checksums.multihash.json         # optional
│
├─ fetch/                              # 🌐 network + acquisition receipts
│  ├─ <source_id>/
│  │  ├─ request.headers.txt
│  │  ├─ response.headers.txt
│  │  ├─ response.status.json
│  │  ├─ etag.txt                      # if present
│  │  └─ fetch.meta.json               # timestamps, byte counts, etc.
│  └─ ...
│
├─ env/                                # 🧰 reproducible runtime evidence
│  ├─ git_commit.txt
│  ├─ git_status.patch                 # optional (dirty diff)
│  ├─ python_version.txt
│  ├─ pip_freeze.txt
│  ├─ node_version.txt
│  ├─ package_lock.json                # optional copy
│  ├─ rustc_version.txt                # optional
│  └─ docker_image_digests.json         # optional
│
├─ run/                                # 🏃 run-level evidence
│  ├─ run_manifest.json
│  ├─ telemetry.ndjson
│  └─ timings.json
│
├─ policy/                             # 🧭 governance + validation
│  ├─ conftest.results.json
│  ├─ schema_validation.json
│  └─ gates.summary.md                 # small human-readable summary
│
├─ supply-chain/                       # 🧷 signatures + attestations
│  ├─ artifact_digests.json
│  ├─ signatures/                      # e.g., cosign outputs
│  ├─ attestations/                    # e.g., in-toto provenance
│  └─ sbom/                            # SPDX/CycloneDX, etc.
│
├─ geospatial/                         # 🗺️ geo processing evidence
│  ├─ reprojection.log
│  ├─ crs.normalization.json
│  ├─ tile_build_config.json
│  └─ tile_build.log
│
└─ ai/                                 # 🤖 AI-related receipts (redacted!)
   ├─ model_id.txt
   ├─ prompt.hashes.json               # store hashes, not raw prompts (default)
   ├─ inference_config.json
   ├─ evaluation/
   │  ├─ metricspec_id.txt
   │  └─ metrics.json
   └─ ...
```

---

## 🔗 How receipts connect to provenance

Receipts are **supporting evidence** for the formal provenance graph:
- **PROV Entities** → files, datasets, artifacts, manifests
- **PROV Activities** → fetch, transform, evaluate, publish
- **PROV Agents** → humans, CI bots, services, model identities

### 🧩 Linking strategy
1. Every receipt file gets a **hash** (and goes into `integrity/checksums.sha256`)
2. `receipts.index.json` becomes the **single lookup table** for tools and humans
3. PROV records reference receipts via:
   - receipt `id`
   - receipt `path`
   - receipt `sha256` (or multihash)
4. The experiment report references the same receipt IDs (no divergence)

---

## 🗂️ `receipts.index.json` (minimal schema)

Keep this file small, stable, and machine-readable.

```json
{
  "schema_version": "receipts/v1",
  "run_id": "RUN-YYYYMMDD-HHMMSSZ-XXXX",
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "items": [
    {
      "id": "fetch:source_usgs_nwis:stations",
      "kind": "http",
      "path": "fetch/source_usgs_nwis/response.headers.txt",
      "sha256": "…",
      "relates_to": {
        "prov_activity": "prov.jsonld#activity-fetch-1",
        "prov_entity": "prov.jsonld#entity-input-1"
      },
      "notes": "Headers captured for reproducible retrieval."
    }
  ]
}
```

> 🎛️ Design goal: tools can validate a run without “reading the whole report”.

---

## 🧪 Minimum receipts checklist

Use this as a baseline for any experiment run:

- [ ] 🔐 `integrity/checksums.sha256` includes *every* receipt artifact
- [ ] 🌐 Fetch receipts exist for every external download (headers + status)
- [ ] 🧰 Environment receipts include tool versions + code commit ID
- [ ] 🏃 `run/run_manifest.json` exists and is hashable
- [ ] 🧭 Policy receipts show what gates were checked (and outcomes)
- [ ] 🧷 Supply-chain receipts exist for any produced artifact (if applicable)
- [ ] 🗺️ Geo receipts exist for CRS changes / tile builds (if applicable)
- [ ] 🤖 AI receipts are **redacted** by default (hashes > raw content)

---

## 🛠️ Quick capture recipes (examples)

> These are examples; use equivalent commands for your OS/tooling.

### 🔐 Checksums
```bash
# From the report root
find prov/receipts -type f -print0 | sort -z | xargs -0 sha256sum > prov/receipts/integrity/checksums.sha256
```

### 🧰 Environment snapshot
```bash
git rev-parse HEAD > prov/receipts/env/git_commit.txt
python -V > prov/receipts/env/python_version.txt
pip freeze > prov/receipts/env/pip_freeze.txt
node -v > prov/receipts/env/node_version.txt
```

### 🌐 HTTP fetch receipts (pattern)
```bash
# Replace <URL> and output filenames as needed
curl -sS -D prov/receipts/fetch/<source_id>/response.headers.txt -o /tmp/payload.bin "<URL>"
```

---

## 📚 Project context (why this folder is so strict)

This repo’s documentation emphasizes:
- **provenance-first** ingestion, processing, publishing, and AI outputs
- **contract-first** data acceptance (no “mystery layers”)
- **policy gates** that fail closed
- **UI + AI transparency** powered by inspectable sources

Receipts are the “ground truth glue” that keeps those promises enforceable.

<details>
<summary>📦 Included project reference docs that informed this receipts design</summary>

### 🧭 Core KFM / provenance docs
- 📄 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation*
- 📄 *Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design*
- 📄 *Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖*
- 📄 *Kansas Frontier Matrix – Comprehensive UI System Overview*
- 📄 *📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide*
- 📄 *🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals*
- 📄 *Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)*
- 📄 *Additional Project Ideas*

### 🧠 Knowledge libraries (packaged as PDF portfolios)
- 📚 *AI Concepts & more* (PDF Portfolio)
- 🗺️ *Maps–GoogleMaps–VirtualWorlds–Archaeological–Computer Graphics–Geospatial–webgl* (PDF Portfolio)
- 🧮 *Data Managment–Theories–Architures–Data Science–Baysian Methods–Some Programming Ideas* (PDF Portfolio)
- 🧰 *Various programming langurages & resources 1* (PDF Portfolio)

</details>

---

## ✅ Done right, receipts unlock…

- 🧾 **Evidence you can audit**
- 🔁 **Runs you can reproduce**
- 🧬 **Provenance graphs you can query**
- 🧠 **AI answers you can trust**
- 🗺️ **Maps you can defend in peer review**

Keep it tight. Keep it verifiable. Keep the chain unbroken. 🔗✨
