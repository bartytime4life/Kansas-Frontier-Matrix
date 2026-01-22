# 🧾 Artifacts — Story Node Evidence Manifest (Example 03)

![example](https://img.shields.io/badge/example-03__story__node__evidence__manifest-2b6cb0)
![provenance](https://img.shields.io/badge/provenance-PROV%20%7C%20STAC%20%7C%20DCAT-16a34a)
![policy](https://img.shields.io/badge/policy-fail--closed%20gates-ef4444)
![ui](https://img.shields.io/badge/UI-Story%20Nodes%20%2B%20Focus%20Mode-8b5cf6)

Welcome to the **generated artifact vault** for Example 03. 🗄️✨  
This folder exists to prove (and keep proving) that a Story Node’s narrative is **evidence-first, reproducible, and auditable**.

---

## 🧭 What this folder is (and why it exists)

A **Story Node** in KFM is typically:
- **Markdown** for the narrative ✍️
- a **JSON config** that drives playback (steps, map state, timeline) 🎬🗺️

This `artifacts/` directory is the *machine-verifiable* side of the story:
- ✅ **Evidence Manifest**: every claim → a cited, cataloged source
- ✅ **Provenance (PROV)**: how inputs produced outputs (and who/what ran it)
- ✅ **Catalog hooks (STAC/DCAT)**: discovery + dataset metadata
- ✅ **Integrity**: hashes/checksums & deterministic run metadata

> Think of it as **“the map behind the map”**—but for narrative truth. 🧠🧾

---

## ⚡ Quick start (human-friendly)

1) **Open the Evidence Manifest**  
   Look for `EM-*.yaml` or `evidence_manifest.*` and scan the `claims[]` → `evidence[]` links.

2) **Verify integrity**  
   Run checksum verification if present:
   ```bash
   sha256sum -c checksums.sha256
   ```

3) **Inspect provenance**  
   Open `prov*.jsonld` (or similar) to see a chain like:
   `entities (inputs/outputs) ↔ activities (runs) ↔ agents (humans/bots)`

---

## 📁 Expected contents (tree)

> Names can vary slightly by generator version — the patterns matter. ✅

```text
📦 artifacts/
├─ 🧾 README.md                         ← you are here
├─ 🧷 EM-*.yaml / EM-*.json             ← Evidence Manifest (primary)
├─ 🧬 prov*.jsonld                      ← W3C PROV bundle (lineage)
├─ 🗂️  stac*.json                       ← STAC Item/Collection (assets)
├─ 🗃️  dcat*.jsonld                     ← DCAT Dataset/Distributions (catalog)
├─ 🔐 checksums.sha256                  ← integrity list (sha256)
├─ 🧪 policy_report*.json               ← policy gate output (optional)
├─ 🧾 run_manifest*.json                ← deterministic run metadata (optional)
└─ 🧾 receipts/                         ← request receipts, query params, logs (optional)
   ├─ http_*.json
   └─ query_*.json
```

---

## 🧷 Artifact guide (what each thing does)

| Artifact | Purpose | Who/what consumes it |
|---|---|---|
| `EM-*.yaml` / `evidence_manifest.*` | **Claim → Evidence** mapping + metadata | UI story viewer, Focus Mode, CI policy gates |
| `prov*.jsonld` | Reproducible lineage: inputs/outputs/runs/agents | Governance ledger, audits, debugging, “why” panels |
| `stac*.json` | Spatial/temporal asset metadata | Map layer tooling, asset discovery, offline packs |
| `dcat*.jsonld` | Dataset-level catalog metadata | Dataset registry, interoperability/harvesting |
| `checksums.sha256` | Tamper-evident integrity | CI, reviewers, offline distribution |
| `run_manifest*.json` | Deterministic run ID, config hash, environment hints | Re-run verification, reproducibility |
| `policy_report*.json` | “Fail closed” gate results (license/classification/citations) | Maintainers, CI |
| `receipts/*` | How evidence was fetched/derived (queries, parameters) | Auditors, “show your work” UX |

---

## 🧾 Evidence Manifest (the star of Example 03)

### 🧩 What it connects
- A Story Node’s **textual claims** (sentences/paragraphs)
- To **evidence records** (datasets, documents, queries)
- With **stable IDs** so the UI can:
  - render footnotes
  - open the evidence panel
  - block “mystery claims” 🚫

### ✅ Recommended minimum fields (per evidence item)
- `id` (stable)
- `type` (`dataset`, `document`, `query`, `image`, `map_layer`, …)
- `uri` (or catalog ID)
- `license`
- `retrieved_at`
- `digest` (sha256 preferred)
- `stac_ref` / `dcat_ref` / `prov_ref` (when applicable)
- `used_in_steps` (which story playback steps cite it)

### Example snippet (schema vibe)
```yaml
manifest_id: EM-84
story_node_id: story.ks.example-03
claims:
  - claim_id: C-001
    text: "Kansas river gauge levels rose sharply after X event."
    supports:
      - evidence_id: E-USGS-TOPEKA-2025-01-01T20
evidence:
  - evidence_id: E-USGS-TOPEKA-2025-01-01T20
    type: query
    uri: kfm://dcat/usgs-realtime-water-data
    retrieved_at: "2025-01-01T20:00:00Z"
    digest:
      alg: sha256
      value: "…"
    prov_ref: prov://activity/kfm.focus.query.2025-01-01T20
    license: "Public Domain / US Gov"
    receipts:
      - receipts/query_usgs_topeka_note.json
```

---

## 🧬 Provenance bundle (PROV / “how we got here”)

Your PROV JSON-LD should let a reviewer answer:

- **What** outputs were created?
- **From which** inputs?
- **By what** activity (pipeline run / query / transform)?
- **By whom/what** agent (human, CI, bot)?
- **When** did it happen?

> If the Evidence Manifest is “**what supports the claim**,” PROV is “**what produced the artifact**.” 🧠

---

## 🧪 Policy gates (fail-closed by design)

This folder is designed to pass automated gates such as:
- citations required for factual claims ✅
- STAC/DCAT/PROV completeness ✅
- license present ✅
- sensitivity/classification labeling ✅
- “no unsourced content” in story rendering ✅

If a required artifact is missing or inconsistent, CI should treat it as **blocked** (not “warning-only”). 🚦

---

## 🗺️ How this ties into the UI & Focus Mode

In the KFM UI:
- Story playback steps can **toggle layers**, change **timeline year**, and move the **map state**
- The story panel can show **citations**, and a **View Evidence** panel can open the manifest-backed sources
- Focus Mode should produce **AnswerWithCitations**, and those citations should align with catalog IDs and provenance links

In other words:  
**Stories and AI answers use the same trust contract** → evidence + provenance + policy. 🔁✅

---

## 🧰 Editing rules (so we don’t break the chain)

### ✅ DO
- Treat artifacts as **generated outputs** (rebuild rather than hand-edit).
- Keep raw sources immutable; only transform via config-driven steps.
- Add evidence using **stable IDs** and include digests/checksums.
- Mark sensitive content and avoid leaking restricted locations.

### ❌ DON’T
- Hand-edit produced hashes or PROV records.
- Add narrative claims without manifest-backed citations.
- Store secrets/tokens in receipts or logs.

---

## 📦 Distribution notes (big files, offline packs, and “data as code”)

For large or binary artifacts:
- prefer content-addressed storage (e.g., OCI registry workflows) and keep **pointers + metadata** here
- consider DVC for heavyweight layers/models
- always preserve links back to STAC/DCAT/PROV so nothing becomes a black box

---

## 🔗 Related project docs (deep context 🧠📚)

### Core KFM architecture & governance
- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**
- **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**
- **Additional Project Ideas.pdf** (OCI/ORAS/Cosign, deterministic pipelines, etc.)
- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**
- **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**

### UI + narrative layer
- **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**

### Reference libraries (note: PDF portfolios)
- **AI Concepts & more.pdf** *(PDF portfolio — open with Acrobat/Reader to access sub-docs)*
- **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** *(portfolio)*
- **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** *(portfolio)*
- **Various programming langurages & resources 1.pdf** *(portfolio)*

---

## 🧩 FAQ

**Q: Why is the Evidence Manifest separate from the Story Node markdown?**  
A: Markdown is for humans; the manifest is for machines, policy, and deterministic traceability. Keeping them separate makes audits and automation cleaner.

**Q: What if a claim is interpretation, not a fact?**  
A: Mark it as interpretation/analysis and still cite the supporting evidence; the UI/AI can then display “fact vs inference” clearly.

**Q: Can I delete artifacts to reduce repo size?**  
A: Prefer **pointers + checksums + provenance** over deleting truth. If size is the issue, move large binaries to DVC/OCI and keep the metadata here.

---

### ✅ North Star
> No story without sources. No data without provenance. No UI without receipts. 🧾🧬🗺️

