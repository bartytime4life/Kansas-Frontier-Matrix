# ✅ PASS Fixtures — Policy Pack Smoke Tests

![OPA](https://img.shields.io/badge/OPA-Rego-5e2b97) ![Conftest](https://img.shields.io/badge/Conftest-Policy%20Tests-0b7285) ![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance-2f9e44) ![PROV](https://img.shields.io/badge/W3C-PROV-ef6c00) ![STAC](https://img.shields.io/badge/STAC-Cataloging-6f42c1) ![DCAT](https://img.shields.io/badge/W3C-DCAT-495057)

> [!IMPORTANT]
> Everything in `✅ fixtures/pass/` is **normative**: these are the “known-good” change-sets that **MUST** pass the Policy Pack.
> If a PASS case fails, treat it like a regression in governance, provenance, security, or artifact contracts.

---

## 🧭 What this folder is

This directory contains **PASS fixtures** used by:

📦 `mcp/dev_prov/examples/09_policy_pack_smoke_tests`

Each fixture represents a **minimal, realistic “good contribution”** that satisfies Kansas Matrix System / KFM governance rules (policy-as-code).

---

## ✅ What “PASS” means

A fixture is considered **PASS** when the policy runner produces:

- ✅ **Exit code 0** (or equivalent “success” status)
- ✅ **No `deny` outputs** (no blocking violations)
- 🟡 **Warnings allowed** only if the harness supports them and they’re either:
  - explicitly asserted, or
  - documented as non-blocking.

> [!NOTE]
> PASS fixtures are intentionally “boring”: they should be **small**, **deterministic**, and **focused**.

---

## 🧪 Run the smoke tests locally

From repo root (examples):

```bash
# Typical layout (Rego policies live under tools/validation/policy)
conftest test mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/pass \
  --policy tools/validation/policy
```

If your policy pack is kept under `api/scripts/policy/`:

```bash
conftest test mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/pass \
  --policy api/scripts/policy
```

Debug-style runs (optional):

```bash
conftest test ... --trace
opa eval -i <input.json> -d <policy_dir> "data"
```

---

## 🧱 Fixture contract (recommended)

> [!TIP]
> The harness may differ slightly — but **every fixture should make the policy decision reproducible** from the files in its folder.

Recommended per-case layout:

```text
✅ pass/
  📄 README.md  ← you are here
  📦 <case_name>/
    🧾 input.json            # What the policy engine evaluates
    📝 expected.json         # Optional: expected decision shape, warnings, etc.
    📄 README.md             # Why this case exists + which rules it exercises
    📁 files/                # Optional: repo-like file tree if your harness reads files from disk
```

### Suggested `input.json` shape (adapt to your harness)

```json
{
  "changed_files": [
    "data/contracts/example.dataset.json",
    "data/catalog/stac/example.stac-item.json",
    "data/catalog/dcat/example.dcat.json",
    "data/provenance/example.prov.jsonld"
  ],
  "context": {
    "actor": "human|agent",
    "event": "pull_request|local_run",
    "policy_pack": "v13"
  },
  "files": {
    "data/contracts/example.dataset.json": { "id": "example", "license": "CC-BY-4.0" },
    "data/catalog/stac/example.stac-item.json": { "type": "Feature", "stac_version": "1.0.0" },
    "data/catalog/dcat/example.dcat.json": { "@type": "dcat:Dataset" },
    "data/provenance/example.prov.jsonld": { "@context": "https://www.w3.org/ns/prov#" }
  }
}
```

---

## 🧩 What “good” looks like (what we keep PASS fixtures for)

These smoke tests exist to keep the project aligned with the core design pillars:

### 🔍 Provenance-first, evidence-first outputs
- Catalog entries (STAC/DCAT) are present and coherent
- Provenance (PROV) exists for derived artifacts
- AI outputs / narratives are **citation-backed**

### 🧷 Contract-first artifacts
- Dataset contracts/manifests are complete enough to drive ingestion, UI, and audits
- Outputs are deterministic / reproducible (no “hand-edited processed data”)

### 🛡️ Fail-closed governance
- Missing required metadata fails
- Unknown licenses / missing sensitivity labels fail
- Secrets / obvious credentials fail
- Unsafe publication paths fail

### 🧠 AI + UI transparency (no black boxes)
- Story/Narrative content references real datasets/entities
- UI artifacts preserve attribution and can carry credits forward on export/share
- Dev provenance is captured so “code history” links into data lineage

---

## 📚 Canonical PASS fixture categories

Use these as “buckets” when adding new passing cases:

| Category 🧩 | A PASS fixture demonstrates ✅ | Typical artifacts 📦 |
|---|---|---|
| **Dataset Intake** 📥 | License + required metadata + provenance present | Contract JSON, STAC item, DCAT dataset, PROV |
| **Pipeline Ordering** 🔁 | Later-stage artifacts aren’t introduced before earlier-stage proof | Raw → processed → catalog → graph → UI |
| **AI Output** 🧭🤖 | AI answer payload includes citations (or refuses) | Focus Mode output JSON + citation list |
| **Story Node** 🧾 | Narrative is Markdown + JSON config with references | `story.md`, `story.json`, evidence manifest |
| **Pulse Thread** 💓 | Timely narrative with evidence manifest + provenance links | Pulse JSON/MD + evidence manifest |
| **Supply Chain / OCI** 📦🔏 | Artifact references include digest + signature/attestation refs | OCI ref metadata + Cosign/in-toto pointers |
| **Dev Provenance** 🧬 | PR→PROV mapping is valid and ingestable | PR event JSON-LD (Activity/Entity/Agent) |

---

## 🧾 Minimal PASS patterns (copy/paste starter ideas)

### 1) 📥 Dataset Intake “minimum viable good”
A PASS case should include enough to satisfy governance:

- ✅ `license` present (and allowed)
- ✅ minimal spatial/temporal coverage
- ✅ STAC/DCAT + PROV created/updated together
- ✅ sensitivity label present (even if “public”)

### 2) 🧭🤖 Focus Mode answer with citations
A PASS fixture for AI outputs should demonstrate:

- ✅ explicit citation list
- ✅ governance flags surfaced (if applicable)
- ✅ refusal/uncertainty path when no evidence exists (optional PASS variant)

### 3) 🧾 Story Node content (Markdown + JSON)
A PASS story fixture should show:

- ✅ Markdown content
- ✅ JSON config referencing valid layer IDs / dataset IDs
- ✅ citations for factual claims
- ✅ no unsafe HTML injection patterns

### 4) 💓 Pulse Thread with evidence manifest
A PASS pulse fixture should show:

- ✅ “short update” narrative
- ✅ evidence manifest including dataset IDs + query params + timestamps
- ✅ provenance attached/linked so the pulse is auditable and reusable

### 5) 🧬 PR → PROV JSON-LD
A PASS dev provenance fixture should show:

- ✅ PR modeled as PROV `Activity`
- ✅ commits modeled as PROV `Entity`
- ✅ author/reviewer/CI modeled as PROV `Agent`
- ✅ valid relationships (`prov:used`, `prov:wasAssociatedWith`, etc.)

---

## ❌ Anti-patterns (belong in `../fail/`)

If you’re about to add a PASS fixture and it includes any of the below, stop — it’s probably a FAIL case:

- 🚫 dataset contract without `license`
- 🚫 derived artifacts without PROV
- 🚫 processed data changed without deterministic pipeline proof
- 🚫 secrets/credentials in JSON/YAML/env files
- 🚫 UI bypassing API boundary (e.g., direct DB access assumptions)
- 🚫 sensitive data without classification / oversight flags

---

## ➕ Adding a new PASS fixture (checklist)

- [ ] One “idea” per fixture (don’t bundle multiple behaviors)
- [ ] Minimal files required to trigger the rule(s)
- [ ] Deterministic timestamps / IDs (avoid “now()” or nondeterminism)
- [ ] Include a per-case README documenting:
  - what changed
  - why it’s considered compliant
  - what policy/rules it guards against regressing
- [ ] If you add a new policy rule, add at least:
  - 1 PASS case ✅ (this folder)
  - 1 FAIL case ❌ (`../fail/`)

---

## 🧠 Design context (project docs) 📚

<details>
<summary><strong>Why these PASS fixtures look the way they do</strong> (click to expand)</summary>

These smoke tests are shaped by the project’s design direction across:

- **Governance & policy-as-code** (OPA/Rego + Conftest; fail-closed; supply chain controls)
- **Provenance-first ingestion** (STAC/DCAT/PROV; deterministic pipelines; immutable raw evidence)
- **UI trust surfaces** (layer provenance, credits on export/share, story tooling, offline packs)
- **AI transparency** (citation-backed answers; explainability; governance flags)
- **Living atlas features** (Pulse Threads, real-time updates, community verification)
- **Dev provenance** (PR/CI events modeled as PROV so code evolution becomes queryable lineage)

Some reference PDFs are shipped as **PDF Portfolios** (bundles). If a file doesn’t render in your viewer, open it in **Adobe Reader/Acrobat**.

</details>

---

