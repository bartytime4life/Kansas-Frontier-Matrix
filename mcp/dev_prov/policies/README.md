# 🛡️ MCP Dev Provenance Policies (KFM)

<kbd>Policy-as-Code</kbd> <kbd>OPA/Rego</kbd> <kbd>Conftest</kbd> <kbd>Fail-Closed ✅</kbd> <kbd>FAIR + CARE</kbd> <kbd>PROV-O</kbd> <kbd>Evidence-First</kbd>

> **North Star:** *If it can’t be proven, it can’t be published.*  
> KFM is contract-first + provenance-first: “no mystery layers,” every output must trace back to cataloged sources and processing steps.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🎯 What this folder is

This directory contains **development provenance (dev_prov)** + **governance** policies for the Kansas Frontier Matrix (KFM), aligned with:

- **Evidence-first publishing** (STAC + DCAT + PROV “evidence triplet”)  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Provenance-first intake** + deterministic pipelines + immutable raw data boundaries  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **AI transparency** (Focus Mode must cite sources; refuse/flag uncertainty rather than fabricate)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **FAIR/CARE governance + sensitive-data safety rails** (classification propagation, access control, geo-obfuscation)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **MCP (Master Coder Protocol)**: reproducibility, documentation-first, experiment logs/model cards, and CI quality gates  [oai_citation:6‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:7‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)  

These policies are designed to run:
- ✅ in **CI** (blocking merges when “deny” rules fire)  [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- ✅ at **runtime** (API-layer enforcement; “UI does not bypass API” trust boundary)  [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- ✅ in **pipelines** (pre-publish gates before data reaches graph/UI/AI)  [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 🧱 Guiding principles (non-negotiables)

### 1) 🧾 Contract-first + provenance-first
- Every dataset has a **data contract** (metadata JSON) and must satisfy required schema before acceptance.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Anything that shows in UI or Focus Mode must be traceable to cataloged sources + provable processing.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 2) 🧪 Reproducibility is a feature (and a security control)
- Raw inputs are immutable evidence; **never overwrite raw data**.  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:14‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- Deterministic outputs where possible (seeds, pinned deps, documented environments).  [oai_citation:15‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:16‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  

### 3) 🧭 “No bypass” trust boundaries
- UI must not bypass the API; policy enforcement happens at the API boundary.  [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 4) 🧑‍🤝‍🧑 CARE + Indigenous Data Sovereignty
- Sensitive/culturally sensitive data: generalized coordinates, access control, permission-based inclusion, and classification propagation.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Cultural protocols + optional TK labeling patterns are explicitly supported as governance constraints.  [oai_citation:20‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### 5) 🤖 AI outputs must be explainable + cite evidence
- Focus Mode includes citations to exact datasets/docs/entities; refusal/uncertainty is preferred over hallucination.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- UI can surface “audit panel” style explainability and governance flags.  [oai_citation:22‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

---

## 🗂️ Expected structure

> Use this layout as the “golden path.” If your repo differs, keep the **intent** and adapt paths.

```text
mcp/
└─ 🧬 dev_prov/
   └─ ⚖️ policies/
      ├─ ✅📄 README.md                 # 👈 you are here 📌 Policy pack overview: scope, how to run, and enforcement points
      ├─ ⚖️ rego/                      # OPA/Rego rules grouped by concern (policy-as-code)
      │  ├─ 🔗 dev_prov/               # PR → PROV invariants: commit linkage, receipts, attestations, trace IDs
      │  ├─ 🧾 data_gov/               # Provenance-first: evidence triplets, licensing, sensitivity labels, required metadata
      │  ├─ 🔒 security/               # Secrets/prompt-gates/supply-chain: SBOM + SLSA-style requirements, deny unsafe outputs
      │  ├─ 🤖 ai/                     # AI output rules: citations, uncertainty labeling, refusal reasons, audit hooks
      │  └─ 🗺️ geo/                    # Geo QA: CRS validity, geometry sanity, bbox checks, spatial constraints
      ├─ 📐 schemas/                   # Schemas used by policies/tests (contracts validated in CI)
      │  ├─ 🧬 prov/                   # PROV JSON-LD structural constraints / shape checks
      │  └─ 🧾 manifests/              # Run manifests, evidence manifests, story manifests (inputs/outputs)
      ├─ 🧪 fixtures/                  # Golden fixtures for testing policies (known-pass/known-fail)
      │  ├─ ✅ pass/                   # Inputs that must pass (baseline compliant examples)
      │  └─ ❌ fail/                   # Inputs that must fail (proves deny rules work)
      ├─ ⚠️ waivers/                   # Time-bound exceptions (must be justified + reviewed + expiring)
      │  └─ ⚠️🧾 waivers.yml            # Waiver ledger: id, scope, owner, expiry, rationale, approval
      └─ 📚 docs/                      # Human-readable policy documentation (rationale, mapping, examples)
         └─ 🗂️📄 POLICY_INDEX.md       # Index of policies + rationale + links to Rego files + test coverage notes
```

---

## 🏷️ Policy IDs + naming conventions

KFM policies use **stable IDs** (so CI output stays actionable and searchable). This pattern is used across the project’s policy pack approach.  [oai_citation:23‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

| Prefix | Domain | Example IDs | What it covers |
|---|---|---:|---|
| `KFM-DEVPROV-###` | Dev provenance | `KFM-DEVPROV-010` | PR/commit/run lineage, attestations |
| `KFM-PROV-###` | Provenance | `KFM-PROV-001` | PROV required when processed data changes |
| `KFM-CAT-###` | Catalog | `KFM-CAT-001` | DCAT/STAC completeness and schema |
| `KFM-SEC-###` | Security | `KFM-SEC-001` | secret scanning / pinned digests / prompt gate |
| `KFM-SOV-###` | Sovereignty + classification | `KFM-SOV-001` | “no output less restricted than inputs” |
| `KFM-STORY-###` | Narratives | `KFM-STORY-001` | citations + AI labeling rules |
| `KFM-GEO-###` | Geospatial QA | `KFM-GEO-001` | CRS validity, geometry validity |
| `KFM-MCP-###` | MCP rigor | `KFM-MCP-001` | experiment logs / model cards / reproducibility |

---

## ✅ Baseline rules (v13-aligned)

These are the **core gates** described across KFM docs (policy pack, governance, intake, AI, and UI).  [oai_citation:25‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🚦 Data & pipeline boundary rules
- **Pipeline Ordering Rule**: `data/raw → data/work → data/processed` (no in-place edits; raw is immutable evidence).  [oai_citation:27‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **API Boundary Rule**: UI never hits DB directly; API is the gatekeeper.  [oai_citation:28‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Provenance-First Publishing Rule**: processed outputs require PROV and cannot appear without catalog evidence triplet.  [oai_citation:29‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 🧾 Evidence + story rules
- **Evidence for Narratives Rule**: story content must cite datasets/entities; AI-generated text must be labeled.  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 🧭 Sovereignty / sensitivity rules
- **Sovereignty + Classification Rule**: outputs inherit the most restrictive classification of inputs; disallow leaking sensitive coordinates/fields to public outputs.  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **Sensitive Location Policy**: exact points require explicit permission; otherwise generalize.  [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 🔐 Security + supply chain rules
- **Prompt Gate**: sanitize AI inputs and prevent accidental sensitive disclosure.  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Secrets Management**: no credentials in code; rotate/audit secrets.  [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **SBOM/SLSA requirements**: releases include SBOM; attest integrity and pin dependencies.  [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  

### 🤖 AI answer integrity rules
- **Always cite sources**; refuse/flag uncertainty when evidence is missing; “nothing is a black box.”  [oai_citation:38‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **Auditability**: allow surfacing governance flags in UI for queries.  [oai_citation:39‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### 🌍 Geospatial QA rules
- Validate geometry + CRS warnings (invalid geometries can break downstream operations).  [oai_citation:40‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

---

## 🧩 Dev provenance (PR → PROV) requirements

KFM proposals describe a **PR-to-PROV graph integration** pattern that turns PRs into PROV-O JSON-LD, and ingests into Neo4j for lineage queries.  [oai_citation:41‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Minimum invariants (recommended):**
- PR is a **prov:Activity**
- Contributors/reviewers are **prov:Agent**
- Commits and artifacts are **prov:Entity**
- PR Activity `prov:used` relevant inputs (prior artifacts, datasets, issues)
- PR Activity `prov:generated` outputs (merged commit, updated dataset contract, new run manifests)
- Merge commit is linked and must exist when a PR is merged (CI can validate invariant).  [oai_citation:42‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

> 💡 This is where `KFM-DEVPROV-*` policies live: they validate the *structure* and *completeness* of dev provenance artifacts before merge.

---

## 🧾 Run manifests (auditable execution)

KFM proposes an **immutable run manifest** that records the “full run context” and can be hashed (RFC 8785 canonicalization) for idempotency + integrity.  [oai_citation:43‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Expected pattern:**
- `data/audits/<run_id>/run_manifest.json`
- Includes inputs, output artifacts, parameters, tool versions, and a `manifest_digest`
- Digest can be used as an **idempotency key** and/or signature subject

These are ideal targets for policy checks:
- Do we have a run manifest for this output?
- Does it reference the correct source dataset(s)?
- Are classifications propagated?
- Are outputs consistent with declared processing steps?

---

## 🧠 Graph integrity & provenance health checks

KFM proposes regular **graph health checks** (like unit tests for the knowledge graph) to catch drift and integrity issues early.  [oai_citation:44‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

Suggested scheduled policies/checks:
- node/relationship deltas beyond thresholds
- broken lineage links (orphaned nodes)
- constraint/index integrity
- missing catalog/prov backreferences

---

## 🏃 Running policies

### Local
```bash
# Run all policies against all supported inputs (example)
conftest test --policy mcp/dev_prov/policies/rego --all-namespaces .

# Run only dev provenance policies (example)
conftest test --policy mcp/dev_prov/policies/rego/dev_prov --all-namespaces mcp/dev_prov
```

### CI (expected)
- CI should fail when any `deny[]` rule fires, and print stable policy IDs (e.g., `KFM-PROV-001: ...`).  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Policy checks should run alongside schema validation + QA checks, consistent with KFM intake automation philosophy.  [oai_citation:46‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## ✍️ Authoring a new policy

### 🧩 Rego skeleton (Conftest-friendly)
```rego
package kfm.devprov

deny[msg] {
  input.kind == "pr_event"
  not input.prov_jsonld
  msg := "KFM-DEVPROV-001: PR event missing PROV JSON-LD record."
}
```

### ✅ Checklist
- [ ] Pick a **stable ID** + domain prefix
- [ ] Add a short rationale (what risk does it mitigate?)
- [ ] Add **fixtures**: one `pass/` and one `fail/`
- [ ] Add tests (`opa test`) if using unit-style testing
- [ ] Ensure messaging is human-actionable (path + fix hint)

> 🔎 Tip: If you’re enforcing narrative integrity, follow the project’s “evidence for narratives” rule and require citations + AI labeling.  [oai_citation:47‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧯 Waivers (exceptions, but accountable)

The policy pack supports **time-bound waivers** stored in `waivers.yml` (or `waivers/waivers.yml`). Use waivers sparingly, with expiry + justification.  [oai_citation:48‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

Example:
```yaml
waivers:
  - id: KFM-PROV-001
    reason: "Backfill legacy dataset; PROV will be added in follow-up PR."
    expires: "2026-03-31"
    paths:
      - "data/processed/legacy/**"
    approvers:
      - "governance-council"
```

> 🧾 Waivers should be auditable and aligned with governance review flows (FAIR/CARE, ethics review, etc.).  [oai_citation:49‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧬 MCP alignment: experiments, model cards, and “documentation-first”

Because MCP emphasizes **scientific rigor + reproducibility**, the policy layer should enforce:
- **Experiment log entries** for new analyses, model training, or claims
- **Model cards** for AI models that affect user-facing behavior
- **Reproducibility checklist items** (seeds, environments, parameter logging, peer review)  [oai_citation:50‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:51‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  

This directly addresses gaps identified in design audits (e.g., missing model cards/experiment logs can undermine traceability).  [oai_citation:52‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)  

---

## 🧭 Mermaid: how policy gates fit into KFM

```mermaid
flowchart LR
  A[PR / Commit] --> B[CI: Schema + Policy Gates]
  B -->|deny[] fires| X[❌ Block Merge]
  B -->|all green| C[Merge to Main]
  C --> D[Build / Pipelines]
  D --> E[run_manifest.json + PROV JSON-LD]
  E --> F[Catalog Evidence Triplet: STAC + DCAT + PROV]
  F --> G[Graph Ingest (Neo4j) + PostGIS]
  G --> H[API (Policy enforcement + AuthZ)]
  H --> I[UI + Focus Mode (Citations + Governance flags)]
```

---

## 📚 Inputs that policies commonly evaluate

### 📦 Data & catalogs
- `data/raw/**` (immutability expectations)  [oai_citation:53‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- `data/work/**`, `data/processed/**` (pipeline ordering expectations)  [oai_citation:54‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- `data/stac/**` + `data/catalogs/**` + `data/prov/**` (evidence triplet)  [oai_citation:55‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 🧾 Provenance artifacts
- PR PROV JSON-LD (PR-to-PROV)  [oai_citation:56‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- `run_manifest.json` (audits & integrity)  [oai_citation:57‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### 🗺️ Geospatial outputs
- geometry validity / CRS sanity checks (avoid invalid geoms + CRS mistakes)  [oai_citation:58‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

---

## 🧷 References (project files used)

### 🧭 KFM core system docs
- **KFM – Comprehensive Technical Documentation**  [oai_citation:59‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:60‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **KFM – Comprehensive Architecture, Features, and Design**  [oai_citation:61‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:62‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **KFM – AI System Overview 🧭🤖**  [oai_citation:63‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **KFM – Comprehensive UI System Overview**  [oai_citation:64‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **KFM Data Intake – Technical & Design Guide**  [oai_citation:65‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:66‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### ✨ KFM proposals & innovation backlog
- **🌟 Latest Ideas & Future Proposals**  [oai_citation:67‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:68‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- **Additional Project Ideas** (graph health checks, narrative integrity, governance ledger concepts)  [oai_citation:69‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Innovative Concepts to Evolve KFM** (CARE/TK/cultural protocol patterns)  [oai_citation:70‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### 🧪 MCP / rigor / QA foundations
- **Scientific Method / Research / Master Coder Protocol Documentation**  [oai_citation:71‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:72‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- **KFM Design Audit – Gaps & Enhancement Opportunities**  [oai_citation:73‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)  
- **MARKDOWN_GUIDE_v13.md.gdoc** (policy pack structure & IDs)  [oai_citation:74‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  

### 🌍 Geo + data quality references (implementation inspiration)
- **python-geospatial-analysis-cookbook** (geometry validity / CRS warnings)  [oai_citation:75‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- **Data Mining Concepts & applications** (data quality + analytical discipline)  [oai_citation:76‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  

### 📦 Reference libraries (PDF portfolios; curated learning pool)
- **AI Concepts & more (PDF portfolio)**  [oai_citation:77‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- **Maps / Virtual Worlds / Archaeological CG / Geospatial WebGL (PDF portfolio)**  [oai_citation:78‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- **Various programming languages & resources (PDF portfolio)**  [oai_citation:79‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- **Data Management theories / architectures / Bayesian methods (PDF portfolio)**  [oai_citation:80‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  

---

## 🧷 Legacy file links (required for continuity)

These older links are intentionally preserved for cross-references in prior discussions and notes:
-  [oai_citation:81‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
-  [oai_citation:82‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
-  [oai_citation:83‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
-  [oai_citation:84‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
