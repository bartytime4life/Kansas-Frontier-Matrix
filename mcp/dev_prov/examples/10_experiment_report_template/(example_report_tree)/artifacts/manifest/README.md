# 🧾 Artifact Manifest (Dev Provenance) — `artifacts/manifest/`

![Template](https://img.shields.io/badge/template-experiment%20report-blue)
![Provenance](https://img.shields.io/badge/provenance-PROV--O-6f42c1)
![Catalog](https://img.shields.io/badge/catalog-STAC%20%7C%20DCAT-0b7285)
![Policy%20Gates](https://img.shields.io/badge/policy%20gates-OPA%20%2B%20Conftest-orange)
![Supply%20Chain](https://img.shields.io/badge/supply%20chain-cosign%20%7C%20SLSA-success)

> 🧭 **Purpose:** This folder defines the **single source of truth** for *what artifacts exist* in this experiment report, *where they live*, and *how to verify them* (checksums + lineage + licensing + sensitivity).
>
> If it’s not in the manifest, it’s not “official.” ✅

---

## ✨ What this manifest unlocks

- 🔁 **Reproducibility:** re-run the experiment and verify outputs match (hashes + run identifiers)
- 🧾 **Auditability:** answer “what produced this file?” (inputs → processing → outputs)
- 🧠 **AI-ready citations:** enable assistants (Focus Mode / report agents) to cite artifacts without guessing
- 🛡️ **Governance & safety:** enforce “fail-closed” rules (no license? no provenance? blocked.)
- 📦 **Distribution:** optionally publish artifacts via OCI-style registries (signed, versioned, portable)

---

## 📁 Folder contract

This template assumes the manifest sits beside (or references) the report’s generated outputs.

```text
(example_report_tree)/
└─ artifacts/ 🧰
   ├─ manifest/ 🧾
   │  ├─ README.md                  👈 you are here
   │  ├─ manifest.json              ✅ canonical artifact index (recommended)
   │  ├─ manifest.schema.json       🧬 JSON Schema for validation (recommended)
   │  ├─ checksums.sha256           🔐 hash list for all artifacts (recommended)
   │  ├─ prov.jsonld                🧵 W3C PROV run + derivations (optional but ideal)
   │  ├─ sbom.spdx.json             🧱 SBOM for build/runtime deps (optional)
   │  └─ attestations/              🏷️ signatures / in-toto / SLSA (optional)
   └─ ... other artifact folders ...
```

> 🧩 You can keep artifacts *anywhere* under the report tree — the manifest is the map.  
> The only rule: **the manifest must be able to resolve every artifact reference**.

---

## ✅ Non‑negotiables (template policy)

Use this checklist as your “definition of done”:

- [ ] Every artifact has a **stable ID** (`artifact_id`)
- [ ] Every artifact has a **content hash** (`sha256` or stronger)
- [ ] Every artifact declares **license**
- [ ] Every artifact declares **sensitivity / access intent** (public / internal / restricted / confidential)
- [ ] Every derived artifact links to **inputs + process/run** (PROV, run_id, or equivalent)
- [ ] If an artifact is used in a narrative/analysis, it has **citation metadata**
- [ ] Validation is **automated** (Schema + Policy Gates) and **fails closed**

---

## 🧬 Manifest format

### Canonical file
Prefer **JSON** for deterministic validation and stable signing:

- `manifest.json` ✅ canonical
- (Optional) `manifest.schema.json` 🧬
- (Optional) `prov.jsonld` 🧵

### Versioning rules
- `manifest_version` is **semver**
- Additive fields are allowed (backwards-compatible)
- Breaking schema changes require a version bump and migration notes

---

## 🧾 Recommended `manifest.json` shape (opinionated)

> This is a **template** shape: adjust fields as needed, but keep the *core invariants* (IDs, hashes, provenance).

```json
{
  "manifest_version": "1.0.0",
  "generated_at": "2026-01-22T00:00:00Z",

  "report": {
    "report_id": "exp_railroads_vs_settlement_001",
    "title": "Railroads vs Settlement (Kansas) — Experiment #001",
    "authors": ["@you"],
    "tags": ["kfm", "experiment", "geospatial", "provenance"]
  },

  "run": {
    "run_id": "run_2026_01_22__a1b2c3",
    "run_time": "2026-01-22T00:00:00Z",
    "idempotency_key": "railroads_vs_settlement__v1__seed_1337",
    "canonical_digest": "sha256:REPLACE_ME"
  },

  "environment": {
    "repo": {
      "url": "REPLACE_ME",
      "commit": "REPLACE_ME",
      "dirty": false
    },
    "runtime": {
      "os": "linux",
      "python": "3.11",
      "containers": [
        { "name": "api", "image": "REPLACE_ME", "digest": "sha256:REPLACE_ME" }
      ]
    }
  },

  "artifacts": [
    {
      "artifact_id": "dataset/railroads_1870_vector",
      "kind": "dataset",
      "role": "input",
      "path": "../../data/railroads_1870.geojson",
      "media_type": "application/geo+json",
      "sha256": "REPLACE_ME",
      "size_bytes": 123456,
      "created_at": "2026-01-22T00:00:00Z",

      "license": { "spdx": "CC-BY-4.0", "url": "REPLACE_ME" },
      "sensitivity": "public",

      "citations": [
        {
          "label": "Source dataset / archive name",
          "uri": "REPLACE_ME",
          "accessed_at": "2026-01-22"
        }
      ],

      "provenance": {
        "prov_ref": "prov.jsonld#entity_railroads_1870",
        "derived_from": []
      },

      "catalog": {
        "stac_item": "REPLACE_ME",
        "dcat_dataset": "REPLACE_ME"
      },

      "validation": {
        "schema": "REPLACE_ME",
        "policy_pack": "REPLACE_ME",
        "passed": true,
        "reports": []
      }
    },

    {
      "artifact_id": "figure/railroads_vs_settlement_heatmap",
      "kind": "figure",
      "role": "output",
      "path": "../figures/heatmap.png",
      "media_type": "image/png",
      "sha256": "REPLACE_ME",
      "size_bytes": 98765,
      "created_at": "2026-01-22T00:10:00Z",

      "license": { "spdx": "CC-BY-4.0" },
      "sensitivity": "public",

      "provenance": {
        "prov_ref": "prov.jsonld#entity_heatmap_png",
        "derived_from": ["dataset/railroads_1870_vector"]
      },

      "notes": "Generated from notebook notebooks/analysis.ipynb"
    }
  ]
}
```

---

## 🧱 Artifact record “must-have” fields

| Field | Why it exists | “Fail closed” rule |
|------|----------------|-------------------|
| `artifact_id` | Stable reference for linking & citations | Must be unique |
| `path` / `uri` | Where the artifact can be fetched | Must resolve |
| `sha256` | Integrity check & immutability anchor | Must exist for binaries |
| `license` | Legal clarity & safe reuse | Missing → block |
| `sensitivity` | Controls exposure + privacy posture | Missing → block |
| `provenance` | Explains lineage + derivations | Missing for derived outputs → block |
| `citations[]` | Human-facing source trace | Required for public-facing claims |

---

## 🔎 Linking to STAC / DCAT / PROV (recommended)

If your artifacts are geospatial or cataloged datasets, keep **standard hooks**:

- 🗺️ **STAC**: item/collection links for spatial assets (rasters, vectors, tiles, etc.)
- 🧾 **DCAT**: dataset-level catalog entry (publisher, license, update cadence, contacts)
- 🧵 **PROV**: lineage graph describing inputs → activity → outputs

> 📌 Even if you don’t publish a full catalog in this experiment template, adding these fields now makes it “drop-in compatible” with catalog-driven platforms later. 🧠

---

## 🔒 Validation & Policy Gates

Your CI (or local tooling) should validate:

1. 🧬 **Schema** (JSON Schema / Pydantic model)
2. 🧾 **Completeness** (licenses, sensitivity, provenance references present)
3. 🔐 **Integrity** (hashes match file contents)
4. 🔗 **Resolution** (paths/URIs exist and are accessible in the report tree)
5. 🧠 **Citation discipline** (anything referenced by narrative/AI has a citation entry)

> 🛑 **Policy mindset:** “If a check can’t be performed, fail closed.”

---

## 🛡️ Signing & publishing artifacts (optional, but powerful)

If you want artifacts to be portable across systems/environments:

- Publish artifacts to an **OCI-compatible registry** (like container images, but for data & reports)
- Attach:
  - 🏷️ signatures (cosign)
  - 🧱 SBOM (SPDX)
  - 🧵 PROV JSON-LD as an attestation / referrer
  - ✅ run manifest & canonical digest

This gives you: **verifiable origin**, **version history**, **easy transfers**, and **registry UIs** for browsing. 📦

---

## 🧩 Integration points (how other parts consume this)

### 🗺️ UI / map layers
Use the manifest to generate:
- layer attribution strings
- “Layer Info” panels
- export footnotes / credits

### 🧠 AI assistant (Focus Mode / report agents)
Use the manifest to:
- retrieve sources deterministically
- attach citations automatically
- refuse unsupported claims (no sources = no answer)

### 📚 Story Nodes / narratives
Use the manifest as the **citation backbone**:
- every inline citation should map to an artifact or external source entry
- CI can validate “no broken references” 🔗

### 🤖 W‑P‑E automation (optional)
A Watcher–Planner–Executor agent can:
- detect missing metadata
- propose manifest patches
- open PRs (never auto-merge) ✅

---

## 🧯 Common mistakes (and how to avoid them)

- ❌ **“We generated a file but forgot to list it.”**  
  ✅ Treat manifest updates as part of the pipeline output.

- ❌ **Hashes don’t match after re-running.**  
  ✅ Ensure deterministic outputs, record run seeds, pin tool versions.

- ❌ **No license / unclear license.**  
  ✅ Always include SPDX identifiers when possible.

- ❌ **Sensitive data leaked in “public” outputs.**  
  ✅ Use `sensitivity` + redaction/generalization + policy gates.

---

## 🧪 Nice-to-have extras (future-proofing)

- 🧾 `CHANGELOG.md` for artifact schema evolution
- 📦 “Offline pack” entries for field use (bundled tiles + story content)
- 🛰️ Support for AR-ready assets (lightweight geometry + media previews)
- 📈 Evaluation metrics artifacts (model cards, benchmarks, audit panels)

---

## 🏁 TL;DR

**The manifest is the contract.**  
It is how we keep experiments: **reproducible 🔁, auditable 🧾, trustworthy 🛡️, and AI-citeable 🧠**.
