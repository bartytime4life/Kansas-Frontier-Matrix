# 🧩 docs/templates

![Docs](https://img.shields.io/badge/docs-governed-blue)
![Templates](https://img.shields.io/badge/templates-canonical-informational)
![KFM](https://img.shields.io/badge/KFM-provenance--first-success)

This folder contains **governed Markdown templates** used across the Kansas Frontier Matrix (KFM) documentation system.

KFM treats documentation as **first-class, machine-validated artifacts**. These templates exist to keep the repo consistent with KFM’s core invariants:
- **Contract-first**: schemas + API contracts are first-class and versioned.
- **Evidence-first**: provenance + catalog entries come *before* narrative interpretation.
- **Deterministic pipeline**: transformations are reproducible, logged, and stable for the same inputs.

> [!IMPORTANT]
> **Do not “freestyle” new doc formats.** Start from a template, keep required front-matter, and link claims to evidence artifacts (datasets/schemas/catalog entries) wherever applicable.

---

## 🗂️ What’s in here

```text
📁 docs/
└─ 📁 templates/                               🧩 documentation scaffolds (copy-me starters)
   ├─ 📄 README.md                              👈 you are here
   ├─ 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md          📄 universal doc template (KFM-MDP frontmatter + sections)
   ├─ 📄 TEMPLATE__STORY_NODE_V3.md              📚 Story Node template (narrative + citations + map hooks)
   └─ 📄 TEMPLATE__API_CONTRACT_EXTENSION.md     🔌 API contract extension template (types, endpoints, examples)
```

---

## 🧭 Template index

| Template | What it’s for | When to use it | Typical destination |
|---|---|---|---|
| [`TEMPLATE__KFM_UNIVERSAL_DOC.md`](./TEMPLATE__KFM_UNIVERSAL_DOC.md) | 📘 Canonical doc structure (overview/scope/audience/etc.) | Architecture docs, governance docs, domain READMEs, standards | `docs/**/…/*.md` |
| [`TEMPLATE__STORY_NODE_V3.md`](./TEMPLATE__STORY_NODE_V3.md) | 🧠 Story Nodes + Focus Mode structure | Historical narrative, interpretive reports that must be provenance-linked | `docs/reports/story_nodes/**` |
| [`TEMPLATE__API_CONTRACT_EXTENSION.md`](./TEMPLATE__API_CONTRACT_EXTENSION.md) | 🌐 API contract changes (endpoints, schema changes, compatibility) | Adding/changing endpoints, payload shape, versioning notes | near API contracts / API docs |

> [!NOTE]
> If you aren’t sure which template to use:  
> - **Docs about system behavior/contracts** → Universal Doc  
> - **Narrative that the UI/Focus Mode should render** → Story Node  
> - **API surface changes** → API Contract Extension

---

## 🚀 Quick start

### 1) Copy a template ✂️
Pick the closest template and copy it to the target location:

```bash
# Example: create a new architecture doc
cp docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md docs/architecture/my_new_doc.md
```

### 2) Fill in front-matter 🧾
Every governed doc starts with YAML front-matter.

**Rules:**
- ✅ Update `title`, `path`, `version`, `last_updated`, `status`
- ✅ Keep governance fields (use `"TBD"` or `"n/a"` — do **not** delete fields)
- ✅ Assign `doc_uuid` (stable identifier)
- ✅ Fill `commit_sha` + `doc_integrity_checksum` when your workflow supports it

<details>
<summary><strong>Checksum helpers (examples)</strong></summary>

```bash
# Linux
sha256sum docs/architecture/my_new_doc.md

# macOS
shasum -a 256 docs/architecture/my_new_doc.md
```

```powershell
# Windows PowerShell
Get-FileHash docs\architecture\my_new_doc.md -Algorithm SHA256
```
</details>

---

## 🧱 “Governed” means… (non-negotiables)

### ✅ Evidence linkage
Docs and Story Nodes should be written so both humans **and machines** can trace claims.

**Minimum expectation:**
- Every material claim links to **datasets, schemas, catalog records, or sources**.
- Processes described include **repeatable validation steps**.
- Governance / FAIR+CARE / sovereignty considerations are **explicit**.

> [!TIP]
> If a sentence would be controversial without evidence, treat it as a **claim that must be cited**.

---

## 🧠 Story Node specifics (Focus Mode ready)

Story Nodes are “machine-ingestible storytelling.” A valid Story Node should:
- include **provenance for every claim**
- reference **graph entities** via stable identifiers
- clearly separate **fact vs interpretation** (especially if AI assisted)

> [!CAUTION]
> Focus Mode is a **trust-preserving gate**. Content that’s not provenance-linked may be blocked, hidden, or flagged for governance review.

---

## 🌐 API contract extension specifics

When changing the API surface area:
- update the **contract first**
- document **backwards compatibility**
- include **test/validation expectations**
- note any **redaction/governance rules** if data is sensitive

> [!IMPORTANT]
> Contract changes are treated like schema changes: version consciously, avoid breaking consumers, and document migration paths.

---

## 🧪 Validation & CI expectations

KFM’s CI commonly enforces the following (high-level):
- YAML front-matter presence + correctness
- required section structure for governed docs
- link/reference validation (no broken internal refs)
- schema validation for structured artifacts
- contract tests for API endpoints
- security/governance scans (secrets, PII/sensitive location checks, classification consistency)

> [!NOTE]
> If your doc fails CI, it’s usually one of: missing front-matter, deleted required fields, broken links, or missing “Definition of Done” elements.

---

## 🧰 Creating / evolving templates

Templates are **governed**. Treat changes like changing a public interface.

### Rules of thumb
- ✅ Prefer **adding** fields/sections over removing them
- ✅ If change is breaking, create a **new versioned template** (e.g., `V4`) rather than mutating the older one
- ✅ Update this README’s **Template index** when adding a template
- ✅ Align with contract-first + evidence-first expectations

> [!WARNING]
> Avoid silent template churn. If a template’s meaning changes, reviewers lose trust and older docs become inconsistent.

---

## 🧾 PR checklist (docs/templates)

- [ ] Template choice matches the artifact type (doc vs story vs API contract)
- [ ] YAML front-matter complete (no missing required keys)
- [ ] No required fields deleted (use `TBD` / `n/a`)
- [ ] Claims link to evidence (datasets/schemas/catalog entries/sources)
- [ ] Governance + FAIR/CARE + sovereignty implications stated (if applicable)
- [ ] Validation steps included & repeatable (where processes are described)

---

## 🔗 Related (conceptual) anchors

While templates live here, they’re designed to align with:
- canonical pipeline ordering (**data → catalogs/prov → database → API → UI → narrative**)
- provenance-first publication patterns
- the Story Node + Focus Mode trust model

> [!TIP]
> If you’re writing something that *feels* like “policy,” “contract,” “schema,” or “evidence rules,” it probably belongs in a governed doc using the Universal Doc Template.

---
