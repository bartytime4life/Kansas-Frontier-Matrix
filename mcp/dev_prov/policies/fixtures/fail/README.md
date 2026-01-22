# 🧪 Fail Fixtures — Dev Provenance Policy Pack (OPA/Rego + Conftest)

![OPA](https://img.shields.io/badge/OPA-Open%20Policy%20Agent-7B42BC?logo=openpolicyagent&logoColor=white)
![Conftest](https://img.shields.io/badge/Conftest-Policy%20Tests-111827)
![Rego](https://img.shields.io/badge/Rego-Policy%20as%20Code-0EA5E9)
![Fail Closed](https://img.shields.io/badge/Gate-fail--closed-DC2626)
![Provenance First](https://img.shields.io/badge/Provenance-first-10B981)

> ⚠️ **This folder is intentionally “bad.”** Everything here should **fail** policy checks.  
> It exists to prove our governance gates catch violations before anything becomes “real” in KFM.

---

## 📍 What this folder is

This directory contains **negative test fixtures** for the KFM policy pack — files that violate rules on purpose, so CI can confirm we **block** them.

Typical uses:
- ✅ Prevent regressions (a rule should *stay enforced*)
- ✅ Validate new rules (add a new fail fixture first)
- ✅ Document edge cases (why something is rejected)

---

## 🗂️ Recommended layout

```text
📦 mcp/dev_prov/policies/
┣━━ 📜 rego/                     # policy rules (*.rego)
┣━━ 🧪 fixtures/
┃   ┣━━ ✅ pass/                 # fixtures that MUST pass
┃   ┗━━ ❌ fail/                 # fixtures that MUST fail (you are here)
┃       ┣━━ 🧾 metadata/         # DCAT/STAC/contract violations
┃       ┣━━ ⛓️ provenance/        # PROV / lineage / run-manifest violations
┃       ┣━━ 🔐 security/         # secrets, tokens, unsafe URLs, etc.
┃       ┣━━ 🤖 ai/               # AI-output policies (citations, labels, etc.)
┃       ┣━━ 🧬 graph/            # graph integrity / orphan checks (if modeled as files)
┃       ┗━━ 📦 supply_chain/     # signing / OCI / artifact integrity checks
```

> If your repo layout differs, keep the **intent**: *fail fixtures are grouped by what they’re testing*.

---

## ▶️ How to run locally

From the repo root (adjust paths if needed):

```bash
# Run ONLY the fail fixtures (expect failures)
conftest test \
  -p mcp/dev_prov/policies/rego \
  mcp/dev_prov/policies/fixtures/fail

# Run pass fixtures (expect success)
conftest test \
  -p mcp/dev_prov/policies/rego \
  mcp/dev_prov/policies/fixtures/pass
```

Pro tip:
- Fail fixtures should produce **stable, readable** failure messages.
- Pass fixtures should remain **minimal** to avoid “accidental” failures.

---

## 🧩 What we typically enforce (and therefore break here)

Below is a “menu” of common policy categories. Your actual `.rego` rules define truth; fixtures prove it.

### 1) 🧾 Metadata completeness (FAIR)
Fail cases usually include:
- Missing `license` (or not an approved SPDX string)
- Missing `publisher/provider` fields
- Missing spatial/temporal coverage in STAC/DCAT-like records
- Missing dataset ID / version / classification tags

**Example filenames**
- `metadata/MISSING__license__dcat.json`
- `metadata/INVALID__spdx__stac_item.json`

---

### 2) ⛓️ Provenance & lineage (Evidence-first)
Fail cases usually include:
- Processed data changed without a matching PROV update
- PROV entity missing `wasDerivedFrom` / `used` / `wasGeneratedBy`
- Run manifests missing checksums or canonical digests
- “Orphaned” lineage nodes (e.g., activity not linked to inputs/outputs)

**Example filenames**
- `provenance/MISSING__prov_links__prov.jsonld`
- `provenance/ORPHAN__activity__prov.jsonld`
- `provenance/MISSING__checksums__run_manifest.json`

---

### 3) 🔐 Security hygiene
Fail cases usually include:
- Obvious secrets (AWS keys, JWT-like strings, private tokens)
- Disallowed external endpoints
- Unsafe config patterns (e.g., debug flags in prod configs)

**Example filenames**
- `security/SECRET__aws_key__dataset.json`
- `security/SECRET__jwt__config.yml`

---

### 4) 🤖 AI governance (Focus Mode / generated content)
Fail cases usually include:
- AI output missing citations
- Missing “AI-generated” labeling/metadata (if required)
- Output references a dataset without provenance/citation anchors

**Example filenames**
- `ai/MISSING__citations__answer.json`
- `ai/MISSING__ai_label__story_node.md`

---

### 5) 📦 Supply chain / artifact integrity
Fail cases usually include:
- Artifact references missing digest pins
- Missing signature/attestation (if required)
- OCI artifact metadata missing required referrers

**Example filenames**
- `supply_chain/MISSING__cosign_sig__artifact_ref.yml`
- `supply_chain/MISSING__digest__oci_distribution.yml`

---

## 🧠 Naming convention (strongly recommended)

Use names that explain **what should fail** and **why**:

```text
<AREA>/<STATUS>__<RULE_OR_CONCEPT>__<SHORT_CASE>.<ext>

# Examples:
metadata/MISSING__license__dcat.json
provenance/INVALID__prov_chain__prov.jsonld
security/SECRET__jwt__env.json
ai/MISSING__citations__answer.json
```

Why this works:
- 🔎 Greppable
- 📚 Self-documenting
- 🧯 Easy to map to policy IDs later

---

## 🧷 Fixture design rules (keep them sharp ✂️)

✅ **Minimize**: smallest file that reproduces the failure  
✅ **One reason to fail**: avoid multi-fail “soup” unless you’re explicitly testing bundling  
✅ **Stable failures**: don’t depend on time, randomness, or network  
✅ **Readable**: prefer short JSON/YAML with comments (where allowed)  
✅ **No real secrets**: even in fixtures — use obviously fake patterns

---

## ➕ Adding a new fail fixture (Golden Path 🏆)

1. **Pick one rule** you’re testing (or one new rule you’re introducing)
2. Create the smallest violating artifact in the right subfolder
3. Run:
   ```bash
   conftest test -p mcp/dev_prov/policies/rego mcp/dev_prov/policies/fixtures/fail
   ```
4. Confirm:
   - It fails for the expected reason
   - The error message is understandable
5. (Optional but 🔥) Add a matching **pass** fixture demonstrating the compliant version

---

## 🧯 Troubleshooting

- **“Fail fixture passed”** → a regression (or your fixture didn’t actually violate the rule)
- **“Pass fixture failed”** → your rule became stricter (or fixture needs updating)
- **Lots of failures at once** → fixture might be breaking multiple rules; simplify it

---

## 📚 Project reference library (why these rules exist)

These policy fixtures are aligned with KFM’s core principles:
- 🧾 **FAIR + CARE** governance
- ⛓️ **Provenance-first / evidence-first publishing**
- 🔐 **Fail-closed gates**
- 🤖 **AI outputs must stay citeable and auditable**
- 🗺️ **UI must surface provenance (“map behind the map”)**
- 📦 **Supply chain integrity for artifacts**

Key docs / packs in this repo’s broader library (see `/mnt/data` uploads in this project workspace):
- 📘 Kansas Frontier Matrix — Comprehensive Architecture, Features, and Design
- 📗 Kansas Frontier Matrix — AI System Overview
- 📙 Kansas Frontier Matrix — Comprehensive UI System Overview
- 📕 KFM Data Intake — Technical & Design Guide
- 💡 Innovative Concepts to Evolve KFM
- 🧠 AI Concepts & more
- 🗺️ Maps/GoogleMaps/VirtualWorlds/Archaeological/Computer Graphics/Geospatial/WebGL
- 🧰 Various programming languages & resources
- 🗄️ Data Management / Architectures / Data Science / Bayesian Methods
- 🧪 Additional Project Ideas
- 🌟 Latest Ideas & Future Proposals

---

### ✅ You’re in the right place if…
- You’re building **new policies** and want confidence they’ll be enforced
- You’re strengthening provenance/security/AI governance and need **tests that prove the gate closes**
- You’re documenting “why we reject this” with a concrete artifact

Happy breaking things (safely) 😈✨
