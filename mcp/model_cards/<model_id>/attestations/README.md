# 🧾 Attestations (Evidence Pack) — `<model_id>`

> **Goal:** make every model release **verifiable**, **auditable**, and **traceable** end‑to‑end (data → pipeline → artifact → UI/answers). 🔗🧬

This folder is the **attestation hub** for the model in `mcp/model_cards/<model_id>/`.

It exists so that **anyone** (maintainers, auditors, contributors) can answer:

- ✅ *What exactly is the model artifact I’m using?* (digest, version, build inputs)
- ✅ *Who/what produced it?* (CI run + maintainer sign‑off when required)
- ✅ *What governance & security checks did it pass?* (policy gates, secrets scan, safety checks)
- ✅ *What data + evaluations support it?* (datasets, metrics, known limitations)

---

## 🧭 Quick links

- [📁 Folder layout](#-folder-layout)
- [✅ Attestation matrix](#-attestation-matrix)
- [🔎 Verification recipes](#-verification-recipes)
- [🤖 Agent & CI expectations](#-agent--ci-expectations)
- [🧠 How this ties into Focus Mode + Story Nodes](#-how-this-ties-into-focus-mode--story-nodes)
- [🛡️ Governance, privacy, sensitivity](#️-governance-privacy-sensitivity)
- [🚨 Revocation & rollback](#-revocation--rollback)
- [🧾 Glossary](#-glossary)

---

## 📁 Folder layout

> Keep it boring, repeatable, and machine-checkable 😄

<details>
<summary><strong>🗂️ Recommended structure</strong></summary>

```text
mcp/model_cards/<model_id>/
├─ README.md                         # 📌 Model Card (human-facing)
├─ eval/                             # 📊 Eval reports + experiment artifacts
│  └─ <release>/...
└─ attestations/
   ├─ README.md                       # (this file)
   ├─ index.json                      # 🧾 machine-readable catalog
   ├─ slsa/                           # 🔗 build provenance (SLSA/in-toto style)
   ├─ sbom/                           # 📦 SPDX / CycloneDX
   ├─ policy/                         # 🛡️ OPA/Conftest reports (fail-closed)
   ├─ data/                           # 🧬 dataset provenance bundles (STAC/DCAT/PROV)
   ├─ security/                       # 🔐 vuln scans, secrets scans, prompt-gate outputs
   └─ human/                          # 👤 approvals / sign-off receipts
```

</details>

---

## ✅ Attestation matrix

> [!IMPORTANT]
> If a **required** row is missing for a release, treat that release as **NOT promotion‑eligible**.

| Category | What it proves | Typical format | Where | Required? |
|---|---|---:|---|:--:|
| 🔗 Build provenance | How artifact was produced (inputs, toolchain, CI run) | `*.intoto.jsonl` / `*.json` | `slsa/` | ✅ |
| 📦 SBOM | What software is inside (deps, versions) | SPDX / CycloneDX | `sbom/` | ✅ |
| 🛡️ Policy gate report | Governance checks passed (fail‑closed) | JSON / text report | `policy/` | ✅ |
| 🧬 Data provenance bundle | Which datasets were used (and their lineage) | STAC/DCAT/PROV | `data/` | ✅ (if model depends on KFM data) |
| 📊 Evaluation bundle | Performance + limitations + metric definition | Markdown + artifacts | `../eval/` | ✅ |
| 🔐 Security scan output | No secrets, acceptable vulnerabilities | JSON reports | `security/` | ✅ |
| 👤 Human approval | Maintainer + authority-to-control approvals | signed note / receipt | `human/` | ⚠️ conditional |

---

## 🧾 `index.json` (recommended)

`index.json` is the **attestation catalog**: one place for tools & humans to find evidence.

```json
{
  "model_id": "<model_id>",
  "release": "<semver-or-date>",
  "artifacts": [
    {
      "name": "model",
      "digest": "sha256:<...>",
      "oci_ref": "<optional: registry/repo@sha256:...>",
      "attestations": {
        "slsa": ["slsa/<digest>.intoto.jsonl"],
        "sbom": ["sbom/<digest>.spdx.json"],
        "policy": ["policy/<release>.conftest.json"],
        "security": ["security/<release>.scans.json"],
        "eval": ["../eval/<release>/report.md"],
        "data": ["data/<bundle_id>/prov.jsonld"]
      }
    }
  ]
}
```

---

## 🔎 Verification recipes

> These are **patterns**, not sacred commands. Prefer your installed tool’s `--help`.

### 1) ✅ Digest match
- Confirm the artifact digest referenced in the **Model Card** matches the actual file / OCI digest.
- Confirm that digest appears in `attestations/index.json`.

### 2) 🔐 Verify signatures / attestations (OCI mode)
If artifacts are stored in an **OCI registry**, signatures and attestations may exist as **OCI referrers**.

```bash
# Examples (pseudo):
cosign verify <oci_ref>
cosign verify-attestation <oci_ref> --type slsaprovenance
```

### 3) 🛡️ Verify policy gates (fail‑closed)
```bash
# Example (pseudo):
conftest test ./data ./mcp ./docs -p ./policy
```

### 4) 🧬 Verify dataset lineage
- Each dataset referenced by the model should have:
  - catalog metadata (STAC/DCAT) 📚
  - provenance (PROV) 🧬
  - sensitivity + license fields 🏷️

---

## 🤖 Agent & CI expectations

KFM’s automation patterns assume:

- **Agents can open PRs** but **must never auto‑merge** 🔒
- **Policy gates apply equally** to humans and agents ✅
- Agent actions can be **signed** (Sigstore/Cosign or equivalent) ✍️
- Agent and pipeline steps should appear in provenance as a first-class `prov:Agent` when applicable 🧬

**Nice-to-have (strongly recommended):**
- a **run manifest** per CI/pipeline run (tool versions, source URLs, record counts, errors)
- stable **hashing/canonicalization** so the run itself has a deterministic identifier (useful for “same input → same output” expectations)

---

## 🧠 How this ties into Focus Mode + Story Nodes

KFM’s AI outputs should be:

- 🧑‍⚖️ **Advisory-only** (no autonomous action)
- 📚 **Evidence-first** (source-cited claims)
- ✅ **Governance-checked** (policy enforcement before returning output)

Attestations are the *artifact-side* mirror of that same trust model:

- Focus Mode can cite **what model** produced a response (digest + release)
- the UI can surface **why a layer/claim is trusted** (source metadata + provenance)
- Story Nodes can carry **evidence manifests** (citations + checksums) that reference the same provenance bundles stored here

---

## 🛡️ Governance, privacy, sensitivity

> [!WARNING]
> Even “derived” outputs can leak sensitive information. Treat **model outputs** as publishable artifacts that may require privacy review.

Recommended controls:
- ✅ sensitivity classification tags on datasets & outputs
- ✅ geo-obfuscation/generalization when required
- ✅ query auditing / inference controls for high-risk outputs
- ✅ k-anonymity / differential-privacy-style approaches when publishing aggregates (when appropriate)
- ✅ authority-to-control approvals for culturally sensitive data

---

## 🚨 Revocation & rollback

Mistakes happen. A safe release process plans for rollback:

- Maintain **versioned artifacts** (prefer content-addressed digests)
- Maintain a **“latest” pointer** that can be repointed back to a known-good digest
- If sensitive data leaks:
  - revoke access quickly (classification flip)
  - remove/purge offending artifacts
  - record the incident + remediation as an attestation (audit trail)

---

## 🧾 Glossary

- **SLSA / in-toto**: build provenance frameworks (who built what, from what)
- **SBOM**: software bill of materials (SPDX / CycloneDX)
- **OPA / Conftest**: policy-as-code + CI enforcement
- **STAC / DCAT / PROV**: catalogs + provenance for data and processes
- **OCI Registry**: content-addressed artifact storage (models, tiles, datasets)
- **Cosign**: artifact signing & attestation tool (often paired with OCI registries)

---

## 📎 Reference library (non‑normative, but useful 📚)

This repo also carries large “library” style references (AI concepts, data management, maps/WebGL, programming resources). They inform implementation choices, but **this README is the normative spec** for what must ship in an evidence pack.

✅ If you add new reference books, consider updating your library manifest/index so contributors can discover them.
