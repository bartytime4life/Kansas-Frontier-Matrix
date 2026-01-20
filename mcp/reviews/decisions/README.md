# 🗳️ Decisions — MCP Review Records (KFM)

![MCP](https://img.shields.io/badge/MCP-Decision%20Records-blue)
![Provenance](https://img.shields.io/badge/Provenance-Required-7b1fa2)
![OPA](https://img.shields.io/badge/Policy%20Pack-OPA%20%2B%20Conftest-orange)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-2ea44f)
![Review](https://img.shields.io/badge/Reviews-PR%20Required-informational)

> [!IMPORTANT]
> KFM is a **living atlas** 🧭 that treats *code, data, narratives, and AI outputs* as **auditable evidence**.  
> If something changes **how we ingest, interpret, store, or present truth**, it deserves a Decision Record. ✅

---

## ✨ What lives here

This folder (`mcp/reviews/decisions/`) is the **canonical home** for **Decision Records (DRs)**—short, versioned documents that capture:

- **Context** 🧩 — what problem we were solving + constraints  
- **Decision** 🗳️ — what we chose and *exactly* what it means  
- **Rationale** 🧠 — why it’s the best tradeoff *for KFM*  
- **Evidence** 🔎 — experiments, benchmarks, prototypes, datasets, policy requirements  
- **Consequences** 🌊 — what changes, what breaks, what we must monitor  
- **Governance** ⚖️ — FAIR+CARE, policy gates, provenance, approvals

> [!TIP]
> Think “**architectural decision records**” (ADR), but widened to include **data governance**, **AI behavior**, **UI provenance**, **security posture**, and **community moderation**.

---

## 🧭 When you MUST write a Decision Record

Write a DR when any change is **hard to reverse** or **trust-impacting**:

### 🏗️ Architecture & platforms
- Clean-architecture boundary changes (Domain/Service/Integration/Infrastructure)
- New storage systems (relational, graph, search), messaging, caching, etc.
- Changes to API shape that the UI/pipelines depend on

### 🧾 Data intake & pipelines
- New ingestion pipeline class (OCR, scraping, ETL, streaming, simulation outputs)
- New catalog requirements (STAC/DCAT/PROV), schema/ontology shifts
- Any rule affecting **determinism**, **ordering**, or **provenance enforcement**

### 🧠 AI / Focus Mode
- Model swaps, retrieval strategy changes, prompt policy changes
- Any change to **citation**, **refusal**, **audit**, **bias/drift monitoring**
- New agent capabilities (Watcher/Planner/Executor, auto-drafting, moderation)

### 🗺️ UI/UX + storytelling
- Layer provenance UI rules, export attribution rules
- Timeline/story node format changes, offline/AR workflows
- Anything affecting user trust (“map behind the map” transparency)

### 🔐 Security / privacy / sensitivity
- Handling sensitive locations, cultural protocols, restricted data tiers
- Policy Pack rule changes, secrets handling, runtime authorization shifts

---

## 🗂️ File naming & organization

### ✅ Recommended naming
Pick one scheme and be consistent inside the repo:

- `0001-short-title.md` (classic ADR-style), **or**
- `DR-YYYYMMDD-short-title.md` (date-forward)

### 🧩 Suggested internal structure
```text
📁 mcp/
  📁 reviews/
    📁 decisions/
      📄 README.md   👈 you are here
      📄 0001-focus-mode-citations.md
      📄 0002-policy-pack-v13-enforcement.md
      📄 0003-oci-artifact-distribution.md
      📁 _archive/   🧊 superseded/deprecated decisions (optional)
```

> [!NOTE]
> “Accepted” decisions should be treated as **immutable historical facts**. If you need to change one, write a **new** DR that *supersedes* the old one.

---

## 🔁 Decision lifecycle

```mermaid
flowchart LR
  A[💡 Idea / Problem] --> B[📝 Draft DR in PR]
  B --> C{🧪 Policy Gates + Reviews}
  C -->|changes requested| B
  C -->|approved| D[✅ Accepted DR]
  D --> E[🛠️ Implementation PR(s)]
  E --> F[📈 Monitoring & Post-Review]
  F -->|unexpected outcome| G[🆕 Superseding DR]
```

---

## 🧾 Decision Record template (copy/paste)

> [!TIP]
> This mirrors KFM’s “structured docs + metadata” style and keeps decisions machine-checkable 📏.

```markdown
---
id: "DR-0000"
title: "TEMPLATE — Decision title"
path: "mcp/reviews/decisions/DR-0000-template.md"
status: "draft" # draft | proposed | accepted | implemented | superseded | deprecated
date_created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"

decision_kind: "architecture" # architecture | data | ai | ui | governance | security | community | ops
scope: ["api", "pipelines", "ui", "catalogs", "graph", "ai", "docs"] # pick what applies

# Governance & compliance
fair_category: "FAIR+CARE"
care_label: "n/a" # e.g., culturally_sensitive | restricted | public
sensitivity: "public" # public | sensitive | restricted
classification: "open" # open | internal | confidential
jurisdiction: "US"

# Traceability
supersedes: []        # list of DR ids
superseded_by: []     # filled when superseded
related_issues: []    # GH issue ids/links
related_prs: []       # GH PR links
owners: []            # responsible maintainers
reviewers_required: []# required sign-offs (roles)

# Provenance hooks (optional but encouraged)
prov_activity_id: "urn:kfm:prov:activity:TBD"
ledger_event_id: "urn:kfm:ledger:event:TBD"
commit_sha: "<filled-by-merge>"
doc_integrity_checksum: "sha256:<to-be-filled>"
license: "CC-BY-4.0"
---

# 1) 📘 Overview
**Purpose:**  
**Scope (in / out):**  
**Audience:**  
**Definitions / Acronyms:**

# 2) 🧩 Context
- What problem are we solving?
- What constraints exist? (policy, performance, budget, UX, community, data quality)
- What triggered this now?

# 3) 🗳️ Decision
State the decision in one clear paragraph.

## 3.1 ✅ Success criteria
- What does “good” look like?
- What metrics / checks prove success?

# 4) 🔀 Options considered
| Option | Pros ✅ | Cons ⚠️ | Why not chosen |
|---|---|---|---|
| A |  |  |  |
| B |  |  |  |
| C |  |  |  |

# 5) 🔎 Evidence
- Experiments (links, runs, configs)
- Datasets / sources used (STAC/DCAT/PROV refs)
- Benchmarks / user tests / prototypes
- Risk analysis

# 6) ⚖️ Governance impact (FAIR+CARE + Policy Pack)
- Which Policy Pack rules are affected?
- Any new/changed Rego policies? (Conftest)
- Sensitivity handling (obfuscation, access tiers, cultural protocols)
- Auditability (what gets logged, where, and why)

# 7) 🧱 Architecture impact
- Domain model changes
- Service workflows
- Integration boundaries (API-only access rules)
- Infrastructure dependencies

# 8) 🗺️ UI/UX impact (if applicable)
- Provenance surfaces (Layer Provenance panel, export attributions)
- Accessibility
- Timeline/story node behavior changes

# 9) 🧠 AI impact (if applicable)
- Citation/refusal behavior
- Governance ledger logging
- Bias checks & drift monitoring
- Human-in-the-loop requirements

# 10) 🚀 Rollout plan
- Steps
- Feature flags / phased release
- Backfill / migrations

# 11) 🧯 Rollback plan
- What is the safe rollback?
- What data is irreversible (if any)?

# 12) 📈 Monitoring plan
- Metrics (accuracy, citation coverage, policy violations, performance)
- Alerts & thresholds
- Post-implementation review date

# 13) 🔗 Links
- Related issues/PRs
- SOPs / runbooks / model cards / design packs
```

---

## ✅ Review lanes & required sign-offs

> [!IMPORTANT]
> KFM uses **policy-as-code** (OPA/Rego + Conftest) and a **fail-closed** posture for uncertain provenance or sensitive content. Reviews enforce that rigor. 🔒

| Decision kind | Minimum reviewers | Typical extra gates |
|---|---|---|
| 🧾 Data intake / pipelines | Data Steward + Maintainer | Provenance-first checks (STAC/DCAT/PROV), deterministic ETL verification |
| 🧠 AI / Focus Mode | AI Steward + Maintainer | Citation/refusal tests, bias checks, drift monitoring plan, governance ledger logging |
| 🗺️ UI/UX | UI Lead + Maintainer | Accessibility review, provenance visibility check, export attribution |
| 🏗️ Architecture | Architect/Lead + Maintainer | Boundary/API checks, performance envelope, deployment concerns |
| 🔐 Security / privacy | Security Reviewer + Maintainer | Sensitive geo handling, secrets scanning, authorization rules |
| 🧑‍🤝‍🧑 Community/moderation | Community Steward + Maintainer | CARE alignment, takedown/escalation workflow, audit trail |

---

## 🧪 Quality gates (what reviewers must look for)

<details>
<summary><strong>✅ Universal checklist (all decisions)</strong></summary>

- [ ] Clear **problem statement** and constraints
- [ ] Decision is **specific** (not “we’ll explore…”)
- [ ] **Alternatives** considered + honest tradeoffs
- [ ] Evidence exists (experiments, prototypes, or policy rationale)
- [ ] Includes **rollout + rollback**
- [ ] Includes **monitoring plan**
- [ ] Defines who owns it and what success means
- [ ] Links to implementation PR(s) or issue(s)

</details>

<details>
<summary><strong>🧾 Data intake checklist</strong></summary>

- [ ] STAC/DCAT/PROV updates required and included
- [ ] **Provenance-first publishing** is preserved (processed/graph changes come with PROV)
- [ ] **Pipeline ordering** is enforced (no skipping stages)
- [ ] **API boundary** preserved (UI/pipelines do not directly talk to DB/graph endpoints)
- [ ] **Deterministic ETL** (no “manual edits” to processed artifacts without pipeline evidence)
- [ ] Policy Pack updated if new rules are needed (and tests added)

</details>

<details>
<summary><strong>🧠 AI / Focus Mode checklist</strong></summary>

- [ ] Every answer is **citation-backed** (or refuses/flags uncertainty)
- [ ] Governance ledger records: sources used, approvals, policy flags
- [ ] Bias detection approach documented (what is checked + when it blocks)
- [ ] Drift monitoring documented (metrics, triggers, response playbook)
- [ ] Human-in-the-loop requirements defined for high-stakes outputs
- [ ] UI explainability hooks considered (audit panel / rationale surfaces)

</details>

<details>
<summary><strong>🗺️ UI/UX checklist</strong></summary>

- [ ] “Map behind the map” stays visible: source + license + processing summary
- [ ] Exports/shares preserve attribution & provenance
- [ ] Accessibility considerations documented
- [ ] Timeline/story behavior is deterministic and testable
- [ ] Offline packs / field mode include provenance and integrity checks

</details>

<details>
<summary><strong>🔐 Security & sensitivity checklist</strong></summary>

- [ ] Sensitive geo handling strategy (fuzzing, rounding, tiered access)
- [ ] Cultural protocol / community authority constraints respected (CARE)
- [ ] Secrets scanning & “fail closed” behavior preserved
- [ ] Runtime authorization implications covered (if applicable)
- [ ] Auditability: who can do what, and where is it logged?

</details>

---

## ⛓️ Provenance & decision audit trail

KFM treats development and governance actions as **lineage**, not just “process.”  
When possible, align decisions with:

- **GitHub PR → PROV graph integration** (PR as activity, commits as entities, contributors/reviewers as agents)  
- **Immutable governance ledger** entries for key actions (especially AI + sensitive data workflows)  
- **Policy Pack** rules as enforceable constraints (CI + optionally runtime checks)

> [!NOTE]
> A Decision Record is itself a **first-class provenance artifact**. Write it so it can be ingested into the knowledge graph later (IDs, links, status transitions, owners).

---

## 📚 Canonical project references (read before major decisions)

These are the “north star” docs for what KFM is and how it must behave:

1. **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** 📖  
2. **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design** 🏗️  
3. **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖** 🧠  
4. **Kansas Frontier Matrix – Comprehensive UI System Overview** 🗺️  
5. **📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide** 🧾  
6. **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals** 🌟  
7. **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)** 🚀  
8. **Additional Project Ideas** 🧪  
9. **AI Concepts & more (portfolio)** 🤖📦  
10. **Data Managment—Theories/Architectures/Data Science/Bayesian… (portfolio)** 🗄️📦  
11. **Maps/GoogleMaps/VirtualWorlds/Archaeological/Computer Graphics/Geospatial/WebGL (portfolio)** 🌍📦  
12. **Various programming languages & resources (portfolio)** 🧰📦  

---

## 📦 Reference library indexes (portfolios)

> [!TIP]
> These portfolios are our “technical bookshelf.” If a DR touches a topic below, cite the most relevant reference(s) in the Evidence section.

<details>
<summary><strong>🤖 AI Concepts &amp; more.pdf — embedded library index</strong></summary>

```text
1: A Developer’s Guide to Building AI Applications - English.pdf
2: A Gentle Introduction to Symbolic Computation.pdf
3: AI Foundations of Computational Agents 3rd Ed.pdf
4: Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf
5: Artificial Neural Networks Models & Applications.pdf
6: Artificial-neural-networks-an-introduction.pdf
7: Basics of Linear Algebra for machine Learning (Discover The Mathematical LLanguage of Data in Python) - Jason Brownlee.pdf
8: Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf
9: Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf.pdf
10: Deep Learning with Python.pdf
11: Foundations of Machine Learning - Foundations_of_Machine_Learning.pdf
12: Gradient Expectations - Stucture, Origins, & Synthesis Of Predictive Neural Networks.pdf
13: Introduction to Digital Humanism.pdf
14: Introduction to Machine Learning with Python - Introduction to Machine Learning with Python.pdf
15: Neural Network Architectures and Activation Functions_ A Gaussian Process Approach - 106621.pdf
16: Neural Network Toolbox User_s Guide - nnet.pdf
17: Neural Networks Using C# Succinctly - Neural_Networks_Using_C_Sharp_Succinctly.pdf
18: On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf
19: Pattern Recognition and Machine Learning.pdf
20: Principles of Biological Autonomy - book_9780262381833.pdf
21: Recurrent Neural Networks for Temporal Data Processing.pdf
22: Regression analysis using Python - slides-linear-regression.pdf
23: Volume 1 Machine Learning under Resource Constraints - Fundamentals .pdf
24: Volume 2 Machine Learning under Resource Constraints - Discovery in Physics .pdf
25: Volume 3 Machine Learning under Resource Constraints - Applications.pdf
26: artificial-intelligence-a-modern-approach.pdf
27: artificial-neural-networks-in-real-life-applications.pdf
28: deep-learning-in-python-prerequisites.pdf
29: haykin.neural-networks.3ed.2009.pdf
30: java-artificial-intelligence-made-easy-w-java-programming.pdf
31: neural networks and deep learning.pdf
32: neural-network-design.pdf
33: neural-network-learning-theoretical-foundations.pdf
34: python-machine-learning-a-crash-course-for-beginners-to-understand-machine-learning-artificial-intelligence-neural-networks-and-deep-learning-with-scikit-learn-tensorflow-and-keras.pdf
35: regression-analysis-with-python.pdf
36: understanding-machine-learning-theory-algorithms.pdf
```

</details>

<details>
<summary><strong>🗄️ Data management portfolio — embedded library index</strong></summary>

```text
1: An Introduction to Statistical Learning.pdf
2: Architecture of Advanced Numerical Analysis Systems - 978-1-4842-8853-5.pdf
3: Bayesian Methods for Hackers Probabilistic Programming and Bayesian Inference.pdf
4: Bayesian computational methods.pdf
5: Bio-Inspired Computational Algorithms & Their Applications.pdf
6: Comprehensive CI_CD Guide for Software and Data Projects.pdf
7: Data Mining Concepts & applictions.pdf
8: Data Science_ Theories, Models, Algorithms, and Analytics - DSA_Book.pdf
9: Data Spaces.pdf
10: Database Performance at Scale.pdf
11: Foundations of Machine Learning - Foundations_of_Machine_Learning.pdf
12: Genetic Programming New Approaches & Successfull Applications.pdf
13: Git Notes for Professionals - GitNotesForProfessionals.pdf
14: Gradient Expectations - Stucture, Origins, & Synthesis Of Predictive Neural Networks.pdf
15: Haskell Notes for Professionals - HaskellNotesForProfessionals.pdf
16: Hibernate Notes for Professionals - HibernateNotesForProfessionals.pdf
17: Recurrent Neural Networks for Temporal Data Processing.pdf
18: Scalable Data Management for Future Hardware.pdf
19: Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf
20: The Data Engineering Cookbook.pdf
21: The Data Lakehouse Platform For Dummies.pdf
22: The Elements of Statistical Learning.pdf
23: Theory & Practice of Cryptography & Network Security Protocols & Technologies.pdf
24: Understanding Statistics & Experimental Design.pdf
25: an-introduction-to-the-finite-element-method.pdf
26: bayes-rule-a-tutorial-introduction-to-bayesian-analysis.pdf
27: clean-architectures-in-python.pdf
28: haykin.neural-networks.3ed.2009.pdf
29: implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf
30: numerical-methods-in-engineering-with-matlab.pdf
31: think-bayes-bayesian-statistics-in-python.pdf
```

</details>

<details>
<summary><strong>🌍 Maps/WebGL portfolio — embedded library index</strong></summary>

```text
1: Archaeological 3D GIS_26_01_12_17_53_09.pdf
2: Computer Graphics using JAVA 2D & 3D.pdf
3: DesigningVirtualWorlds.pdf
4: Geographic Information System Basics - geographic-information-system-basics.pdf
5: Google Earth Engine Applications.pdf
6: Map Reading & Land Navigation.pdf
7: Spectral Geometry of Graphs.pdf
8: Understanding_Map_Projections.pdf - 710understanding_map_projections.pdf
9: geoprocessing-with-python.pdf
10: google-maps-javascript-api-cookbook.pdf
11: graphical-data-analysis-with-r.pdf
12: making-maps-a-visual-guide-to-map-design-for-gis.pdf
13: python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf
14: webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf
```

</details>

<details>
<summary><strong>🧰 Programming languages &amp; resources portfolio — embedded library index</strong></summary>

```text
1: Algorithms Notes for Professionals - AlgorithmsNotesForProfessionals.pdf
2: An Introduction to Spatial Data Analysis and Visualisation in R - An Introduction to Spatial Data Analysis in R.pdf
3: Angular 2+ Notes for Professionals - Angular2NotesForProfessionals.pdf
4: AngularJS Notes for Professionals - AngularJSNotesForProfessionals.pdf
5: Bash Notes for Professionals - BashNotesForProfessionals.pdf
6: C Notes for Professionals - CNotesForProfessionals.pdf
7: C# Notes for Professionals - CSharpNotesForProfessionals.pdf
8: C++ Notes for Professionals - CPlusPlusNotesForProfessionals.pdf
9: CSS Notes for Professionals - CSSNotesForProfessionals.pdf
10: Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf
11: Comprehensive CI_CD Guide for Software and Data Projects.pdf
12: Crafting a Compiler.pdf
13: Entity Framework Notes for Professionals - EntityFrameworkNotesForProfessionals.pdf
14: Essentials of Compilation - An Incremental Approach (python).pdf
15: Excel VBA Notes for Professionals - ExcelVBANotesForProfessionals.pdf
16: Free Android Development Book.pdf
17: Generalized Topology Optimization for Structural Design.pdf
18: HTML5 Canvas Notes for Professionals - HTML5CanvasNotesForProfessionals.pdf
19: HTML5 Notes for Professionals - HTML5NotesForProfessionals.pdf
20: Handbook Of Applied Cryptography (old).pdf
21: Introduction to Numerical Methods for Variational Problems.pdf
22: Introduction to finite element methods.pdf
23: Introduction-to-Docker.pdf
24: Java Notes for Professionals - JavaNotesForProfessionals.pdf
25: JavaScript Notes for Professionals - JavaScriptNotesForProfessionals.pdf
26: Kotlin Notes for Professionals - KotlinNotesForProfessionals.pdf
27: LaTeX Notes for Professionals - LaTeXNotesForProfessionals.pdf
28: Linux Notes for Professionals - LinuxNotesForProfessionals.pdf
29: MATLAB Notes for Professionals - MATLABNotesForProfessionals.pdf
30: MATLAB Programming for Engineers Stephen J. Chapman.pdf
31: Matlab-Modeling, Programming & Simulations.pdf
32: Microsoft SQL Server Notes for Professionals - MicrosoftSQLServerNotesForProfessionals.pdf
33: MongoDB Notes for Professionals - MongoDBNotesForProfessionals.pdf
34: MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf
35: NET Framework Notes for Professionals - DotNETFrameworkNotesForProfessionals.pdf
36: Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf
37: OCaml Practice.pdf
38: Objective-C Notes for Professionals - ObjectiveCNotesForProfessionals.pdf
39: Oracle Database Notes for Professionals - OracleDatabaseNotesForProfessionals.pdf
40: PHP Notes for Professionals - PHPNotesForProfessionals.pdf
41: Perl Notes for Professionals - PerlNotesForProfessionals.pdf
42: PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf
43: PowerShell Notes for Professionals - PowerShellNotesForProfessionals.pdf
44: Python Notes for Professionals - PythonNotesForProfessionals.pdf
45: R Notes for Professionals - RNotesForProfessionals.pdf
46: React JS Notes for Professionals - ReactJSNotesForProfessionals.pdf
47: React Native Notes for Professionals - ReactNativeNotesForProfessionals.pdf
48: Ruby Notes for Professionals - RubyNotesForProfessionals.pdf
49: Ruby on Rails Notes for Professionals - RubyOnRailsNotesForProfessionals.pdf
50: SQL Notes for Professionals - SQLNotesForProfessionals.pdf
51: ScipyLectures-simple.pdf
52: Solving Ordinary Differential Equations in Python.pdf
53: Solving PDEs in Python.pdf
54: Spring Framework Notes for Professionals - SpringFrameworkNotesForProfessionals.pdf
55: Swift Notes for Professionals - SwiftNotesForProfessionals.pdf
56: The-Data-Engineers-Guide-to-Apache-Spark.pdf
57: The-web-application-hackers-handbook-finding-and-exploiting-security-flaws.pdf
58: TypeScript Notes for Professionals - TypeScriptNotesForProfessionals.pdf
59: VBA Notes for Professionals - VBANotesForProfessionals.pdf
60: Visual Basic .NET Notes for Professionals - VisualBasic_NETNotesForProfessionals.pdf
61: Xamarin.Forms Notes for Professionals - XamarinFormsNotesForProfessionals.pdf
62: applied-data-science-with-python-and-jupyter.pdf
63: black-hat-python-python-programming-for-hackers-and-pentesters.pdf
64: flexible-software-design-systems-development-for-changing-requirements.pdf
65: iOS Developer Notes for Professionals - iOSNotesForProfessionals.pdf
66: jQuery Notes for Professionals - jQueryNotesForProfessionals.pdf
67: python-machine-learning-a-crash-course-for-beginners-to-understand-machine-learning-artificial-intelligence-neural-networks-and-deep-learning-with-scikit-learn-tensorflow-and-keras.pdf
68: responsive-web-design-with-html5-and-css3.pdf
69: software-architecture-patterns.pdf
```

</details>

---

## 🙋 FAQ

**Q: Is a DR required for every PR?**  
No. DRs are for **meaningful choices**—the kind you’d want to explain 6 months later when someone asks “why did we do this?” 🧠

**Q: Where do experiments or model cards go?**  
Use `mcp/` for methods/templates and keep experiments in the appropriate `experiments/` or `logs/` area—then link them from the DR. 🔗

**Q: How do we handle reversals?**  
Write a new DR that **supersedes** the old one, document the rollback, and link both ways. 🧊➡️🔥

---

## ✅ Done means…

A decision is “done” when:

- The DR is **accepted**
- Implementation PR(s) are merged
- Monitoring is in place (policy checks, drift checks, QA, etc.)
- We schedule a short post-review if the decision is high-impact

🧭 Keep the atlas honest.
