<!--
👋 Thanks for contributing to Kansas Frontier Matrix (KFM)!

Quick vibe check 🧭:
- KFM is **provenance-first** (“the map behind the map”) and **fails closed** by default.
- Anything that touches data/AI must keep the “truth path” intact:
  Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI  ✅
  (No bypassing the governed API layer 🚫)
-->

## 🧭 Summary
**What changed & why?**  
- **Goal:** <!-- e.g., Improve dataset search relevance / Fix tile rendering / Add new story node -->
- **User impact:** <!-- who benefits, what’s improved -->
- **Risk level:** ☐ Low ☐ Medium ☐ High  
- **Rollback plan:** <!-- how to revert safely if needed -->

---

## 🔗 Related Issues / Discussions
- Closes: #<!-- issue -->
- Related: #<!-- issue -->
- Docs / ADR / RFC: <!-- link(s) -->

---

## 🧩 Type of Change
_Check all that apply_
- ☐ 🐛 Bug fix
- ☐ ✨ Feature
- ☐ ♻️ Refactor (no behavior change)
- ☐ 🧪 Tests
- ☐ 📝 Docs / content
- ☐ 🗺️ Data addition / update
- ☐ 🏭 Pipeline / ETL
- ☐ 🤖 AI / Focus Mode
- ☐ 🔐 Security / governance policy
- ☐ 🧱 Infra / CI / tooling
- ☐ 🎨 UI/UX

---

## 📦 Scope
_Check folders impacted (helps reviewers route faster)_
- ☐ `api/` 🧠 (FastAPI backend)
- ☐ `web/` 🖥️ (React + TypeScript UI)
- ☐ `pipelines/` 🏭 (ETL / jobs / transforms)
- ☐ `data/raw/` 🧊 (immutable source snapshots)
- ☐ `data/processed/` 🧼 (cleaned/standardized outputs)
- ☐ `data/catalog/` 🗂️ (STAC/DCAT metadata)
- ☐ `data/provenance/` 🧾 (W3C PROV lineage logs)
- ☐ `docs/` 📚 (architecture, stories, guides)
- ☐ `.github/` 🧰 (templates, workflows)

---

## 🧪 Testing & Validation
**What did you run?** (paste commands + results)
- ☐ Unit tests
- ☐ Integration tests
- ☐ Lint / format
- ☐ Typecheck
- ☐ E2E (UI)
- ☐ Pipeline dry-run / sample dataset run

**Commands (examples):**
```bash
# api
# pytest
# ruff check .
# mypy .

# web
# npm test
# npm run lint
# npm run build
```

**Evidence (required):**
- Test output / CI link: <!-- paste -->
- Screenshots / recordings (for UI): <!-- paste -->

---

## 🗺️ Data & Provenance (Required for any data/story change)
> [!IMPORTANT]
> KFM is “evidence-first.” If metadata/provenance is missing, the system should **block** (“fail closed”).

### ✅ Dataset changes checklist
- ☐ Raw source snapshot added/updated in `data/raw/` (or referenced with immutable pointer)
- ☐ Processed outputs in `data/processed/` match the transformation spec
- ☐ Catalog metadata updated in `data/catalog/` (STAC items + DCAT dataset record)
- ☐ Provenance log updated/added in `data/provenance/` (W3C PROV lineage)
- ☐ **License** captured + compatible
- ☐ **Sensitivity classification** set (public/restricted/confidential)
- ☐ Checksums / manifests updated (if applicable)

### 📌 Dataset details
- **Dataset ID:** `<!-- e.g., ks_hydrology_1880 -->`
- **Temporal coverage:** <!-- start/end -->
- **Spatial coverage:** <!-- bbox / region -->
- **License:** <!-- e.g., CC-BY 4.0 / Public Domain -->
- **Sensitivity:** ☐ Public ☐ Restricted ☐ Confidential
- **Provenance file:** `data/provenance/<!-- file -->`

### 📝 Story / Narrative changes checklist (if applicable)
- ☐ Story includes clear sources (footnotes / references / `sources.json` / front matter)
- ☐ Claims are tied to citations (“No Source, No Answer” standard)
- ☐ Any sensitive cultural material flagged appropriately (CARE-aligned handling)

---

## 🤖 AI / Focus Mode (If applicable)
**What changed?**
- ☐ Prompt / policy changes
- ☐ Retrieval / embeddings
- ☐ Citation formatting / grounding
- ☐ Model config / runtime (e.g., Ollama)
- ☐ Safety filtering / refusal behavior

**Grounding requirements**
- ☐ AI responses remain citation-backed (“No Source, No Answer”)
- ☐ Refusal behavior verified when evidence is missing
- ☐ AI outputs don’t leak restricted/confidential data

**Test plan**
- Provide at least **3 example queries** with expected results + citations:
  1) Q: <!-- -->  
     Expected: <!-- -->  
     Sources used: <!-- -->
  2) Q: <!-- -->  
     Expected: <!-- -->  
     Sources used: <!-- -->
  3) Q: <!-- -->  
     Expected: <!-- -->  
     Sources used: <!-- -->

---

## 🔐 Security / Governance Impact
_Check all that apply_
- ☐ No secrets/tokens added (✅ verified)
- ☐ RBAC/permissions reviewed (least privilege)
- ☐ OPA policies updated (if relevant)
- ☐ “Fail closed” behavior preserved (missing metadata ➜ blocked)
- ☐ Audit/provenance logging still captured
- ☐ Threat model notes added (if meaningful)

**Security notes:** <!-- brief -->

---

## 🗄️ Database / Migrations (If applicable)
- ☐ Schema change
- ☐ Data migration
- ☐ Backfill job
- ☐ Index changes (tiles/search performance)

**Migration notes**
- Forward migration: <!-- steps -->
- Backward migration: <!-- steps -->
- Expected runtime: <!-- estimate -->
- Risks: <!-- -->

---

## 🎨 UI/UX Notes (If applicable)
- ☐ Screenshots attached
- ☐ Mobile/responsive checked
- ☐ Accessibility checked (keyboard nav, contrast, labels)
- ☐ Map interactions validated (layers, timeline, 2D/3D if relevant)

**Before/After:** <!-- images/links -->

---

## ⚠️ Breaking Changes
- ☐ None
- ☐ Yes (describe below)

**Breaking details**
- What breaks: <!-- -->
- Who is impacted: <!-- -->
- Migration path: <!-- -->
- Deprecation plan (if any): <!-- -->

---

## ✅ Final Checklist
- ☐ PR title is clear + scoped (e.g., `api:`, `web:`, `pipelines:`, `data:`)
- ☐ Changes are small enough to review (or split into follow-ups)
- ☐ Docs updated where needed
- ☐ Tests added/updated where needed
- ☐ Data changes include license + provenance + catalog metadata
- ☐ No direct DB access added from UI (API remains the gate 🌐)

---

<details>
<summary>🧠 Reviewer Notes (optional)</summary>

- Suggested reviewers: @<!-- -->
- Areas to focus: <!-- tricky logic, risky changes -->
- Follow-ups / TODOs: <!-- -->
</details>