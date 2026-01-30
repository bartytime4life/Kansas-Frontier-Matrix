# 📏 KFM Standards Hub (docs/standards)

![Governance](https://img.shields.io/badge/governance-policy--as--code-6f42c1)
![Pipeline](https://img.shields.io/badge/pipeline-evidence--first-0aa)
![Docs](https://img.shields.io/badge/docs-contract--first-orange)

Welcome to **KFM’s governed standards** folder — the “rules of the road” for how data, metadata, docs, and interfaces are structured so the whole system stays **evidence-backed, traceable, and reviewable**. Standards here exist to keep the KFM pipeline consistent and enforceable across **ETL → catalogs → graph → API → UI → narratives**. 📚🧭  
(Standards are expected to be validated by CI and treated as **source-of-truth contracts**.):contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 Quick links

### 📌 Core standards (this folder)
- 📝 **Markdown authoring & workflow** → `./KFM_MARKDOWN_WORK_PROTOCOL.md`:contentReference[oaicite:2]{index=2}
- 🧱 **Repository structure** → `./KFM_REPO_STRUCTURE_STANDARD.md`:contentReference[oaicite:3]{index=3}
- 🗂️ **STAC profile** → `./KFM_STAC_PROFILE.md`:contentReference[oaicite:4]{index=4}
- 🧾 **DCAT profile** → `./KFM_DCAT_PROFILE.md`:contentReference[oaicite:5]{index=5}
- 🧬 **PROV profile** → `./KFM_PROV_PROFILE.md`:contentReference[oaicite:6]{index=6}

### 🧩 Related “governed” folders (where these standards get applied)
- 📚 Templates → `docs/templates/` (universal docs, Story Nodes, API contract changes):contentReference[oaicite:7]{index=7}
- ⚖️ Governance → `docs/governance/` (ethics, sovereignty, review gates):contentReference[oaicite:8]{index=8}
- 🗞️ Story Nodes → `docs/reports/story_nodes/` (draft vs published narratives):contentReference[oaicite:9]{index=9}

---

## ✅ What counts as a “standard” in KFM?

A **standard** is a document that defines **non-negotiable contracts** or **validation rules** for:
- 📦 **Data lifecycle & staging** (raw/work/processed)
- 🗂️ **Metadata correctness** (STAC/DCAT/PROV profiles + schemas)
- 🧠 **Evidence integrity** (no narrative without provenance-linked evidence)
- 🔒 **Sovereignty & classification propagation**
- 🧱 **Canonical subsystem homes** (one place per subsystem; avoid repo drift)

> [!IMPORTANT]
> Standards in this folder are meant to be **enforced by CI/CD** and treated like API contracts: breaking changes require deliberate versioning + review.:contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}

---

## 🧷 The non‑negotiables (print these in your brain 🧠)

### 1) Pipeline ordering is absolute 🧬➡️🗺️➡️🧠➡️🧰➡️🖥️➡️📖
KFM treats the pipeline sequence as **inviolable** — no stage may leapfrog earlier stages or bypass required boundary artifacts.:contentReference[oaicite:12]{index=12}  
A canonical ordering is explicitly emphasized in KFM design docs.:contentReference[oaicite:13]{index=13}

### 2) Provenance first (metadata before interpretation) 🧾✅
Before anything is loaded into the graph or referenced by UI/narratives, it must be:
- cataloged (STAC/DCAT),
- lineage-traced (PROV),
- schema/profile-valid.:contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}

### 3) API boundary rule 🧱
The UI must not query the graph directly; access flows through the governed API layer so redaction + policy can be enforced consistently.:contentReference[oaicite:16]{index=16}

### 4) Governance is “policy as code” ⚖️💻
KFM expects governance rules to be encoded (e.g., OPA/Rego) and enforced via CI checks and/or runtime decisions.:contentReference[oaicite:17]{index=17}

### 5) Fail closed by default 🔒
If checks fail (missing license, missing PROV, etc.), the system blocks the action rather than allowing incomplete or non-compliant content through.:contentReference[oaicite:18]{index=18}

---

## 📦 Data + metadata standards (the “boundary artifacts”)

KFM’s publishing model requires that datasets move through **staging areas** and generate required catalogs/lineage outputs at publication time.:contentReference[oaicite:19]{index=19}

### 🗃️ Required staging layout
- `data/raw/<domain>/` — immutable raw sources  
- `data/work/<domain>/` — intermediate outputs  
- `data/processed/<domain>/` — final outputs ready for downstream consumption:contentReference[oaicite:20]{index=20}

### 🧾 Required “boundary artifacts” at publication
Every dataset (and every “evidence artifact”) must be accompanied by:
- **STAC** records (collections + items)
- **DCAT** dataset entry (discovery layer)
- **PROV** activity bundle (lineage / how it was produced):contentReference[oaicite:21]{index=21}

### 🔗 Cross-layer linkage expectations (keep catalogs, graph, and stories in sync)
- STAC → points to processed assets + includes license/source attribution:contentReference[oaicite:22]{index=22}
- DCAT → links to STAC/distributions for discovery:contentReference[oaicite:23]{index=23}
- PROV → links raw → work → processed + identifies run/config/commit where applicable:contentReference[oaicite:24]{index=24}
- Graph → references catalog IDs (don’t duplicate bulky data):contentReference[oaicite:25]{index=25}

---

## 🧠 Story Nodes standards (governed narrative artifacts)

Story Nodes are expected to be **machine-ingestible narratives** whose claims are tied to evidence, typically written in Markdown and paired with structured choreography (e.g., JSON/YAML) that drives map/timeline behavior.:contentReference[oaicite:26]{index=26}:contentReference[oaicite:27]{index=27}

> [!NOTE]
> “Evidence-first narrative” means **no unsourced claims** are allowed in Story Nodes or Focus Mode; AI-generated content must be clearly identified and evidence-constrained.:contentReference[oaicite:28]{index=28}

---

## 🧱 Standards catalog (what lives here)

| Standard 📄 | Purpose 🎯 | Applies to 🧩 |
|---|---|---|
| `KFM_REPO_STRUCTURE_STANDARD.md` | One canonical home per subsystem (prevents repo drift) | Everyone touching repo layout |
| `KFM_MARKDOWN_WORK_PROTOCOL.md` | Doc authoring conventions + repeatable doc workflow | Docs, Story, Standards |
| `KFM_STAC_PROFILE.md` | KFM extensions/requirements for STAC metadata | ETL + catalog generation |
| `KFM_DCAT_PROFILE.md` | KFM DCAT requirements for dataset discovery | Catalog + portal export |
| `KFM_PROV_PROFILE.md` | KFM provenance requirements (lineage) | ETL + derived artifacts |

(These documents are referenced explicitly as standards artifacts in the Master Guide.):contentReference[oaicite:29]{index=29}

---

## 🧪 Enforcement: how standards become “real” (CI + policy)

KFM design expects:
- **Automated CI enforcement** of governance rules (e.g., missing metadata/license/provenance fails PR checks).:contentReference[oaicite:30]{index=30}
- **Runtime policy enforcement** for access control and response sanitization where needed (e.g., sensitive datasets, restricted outputs).:contentReference[oaicite:31]{index=31}

These are aligned with the broader “testing + CI must be green before merge” mindset described in the Master Coder Protocol documentation.:contentReference[oaicite:32]{index=32}

---

## 🧾 Versioning rules (standards are contracts)

### 🏷️ Repo / release versioning
The Master Guide describes semantic-style versioning expectations at the repository level (major for structural shifts, minor for compatible additions).:contentReference[oaicite:33]{index=33}

### 🧬 Dataset versioning + citation
KFM design docs emphasize that versioned snapshots matter for reuse and citation (e.g., via tags/releases and `CITATION.cff`).:contentReference[oaicite:34]{index=34}

---

## 🔁 How to change a standard (safe change control)

> [!IMPORTANT]
> Changing standards may cause **cascading breakage** (pipelines, validators, UI contracts). Treat changes like API contract changes.

### ✅ Change checklist
- [ ] **Write the intent**: what problem is this solving? (include examples + non-goals)
- [ ] **Backwards compatibility**: does this break existing metadata/docs? If yes, define migration path.
- [ ] **Validation impact**: update schemas/validators/CI rules that enforce the standard.
- [ ] **Docs alignment**: update templates + any “how-to” that depends on the changed standard.
- [ ] **Version signal**: note whether this is patch/minor/major impact.

This reflects the broader “document-first + peer review + CI gates” posture in the Master Coder Protocol documentation.:contentReference[oaicite:35]{index=35}:contentReference[oaicite:36]{index=36}

---

## 🧰 Quick “Definition of Done” for any governed doc ✅

A governed artifact should be considered “done” only when:
- ✅ Front-matter is complete and valid (template/profile compliant)  
- ✅ Claims link to datasets/schemas/sources as applicable  
- ✅ Validation steps are repeatable  
- ✅ Governance + FAIR/CARE + sovereignty implications are stated:contentReference[oaicite:37]{index=37}

---

## 📎 Appendix: Key source docs used to derive this README

- KFM Master Guide v13 (Draft) — `MARKDOWN_GUIDE_v13.md.gdoc` :contentReference[oaicite:38]{index=38}  
- Kansas Frontier Matrix — Comprehensive Technical Blueprint (PDF) :contentReference[oaicite:39]{index=39}  
- Scientific Method / Research / Master Coder Protocol Documentation (PDF) :contentReference[oaicite:40]{index=40}  

---

## 📝 Footnotes (traceability)

[^pipeline-order]: Pipeline ordering is explicitly described as inviolable in the Master Guide v13 draft.:contentReference[oaicite:41]{index=41}

[^kfm-canonical-order]: KFM design docs also emphasize a canonical “raw → processed → catalog/prov → database → API → UI” sequencing conceptually, reinforcing the same spirit of ordered boundary artifacts.:contentReference[oaicite:42]{index=42}

[^policy-as-code]: “Policy as code” + automated CI enforcement is described as a core governance approach (e.g., OPA/Rego + Conftest-like checks).:contentReference[oaicite:43]{index=43}
