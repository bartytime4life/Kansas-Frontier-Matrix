# 🛡️ MCP Gates — Policy-as-Code & Evidence Checks (KFM DNA)

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-0b7285)
![Evidence First](https://img.shields.io/badge/Principle-Evidence--First-2f9e44)
![Policy as Code](https://img.shields.io/badge/Policy-OPA%20%7C%20Rego-364fc7)
![Fail Closed](https://img.shields.io/badge/Safety-Fail--Closed-e03131)
![Human in the Loop](https://img.shields.io/badge/Workflow-Human--in--the--Loop-f08c00)

> **One-liner:** A **Gate** is a deterministic, auditable check that blocks unsafe or unverifiable changes **until** they are made *proven* (metadata + lineage + policy compliance) ✅

---

## 🧭 What this folder is

This directory documents the **Gate subsystem** for the **MCP (Master Coder Protocol)** layer of the Kansas-Matrix-System.

Gates are the “last mile” trust boundary that ensure:

- ✅ **Nothing ships without provenance**
- ✅ **Nothing executes without policy**
- ✅ **Nothing is shown without citations / traceability**
- ✅ **Sensitive things are protected by default**
- ✅ **Automation stays reviewable and reversible**

---

## 📚 Design inputs used to shape Gates (all project files)

This README is intentionally built from **every project file** so the Gate system stays consistent with the KFM architecture, UI, AI, intake, governance, and future roadmap.

### Core KFM docs (product + architecture)
- **KFM — Comprehensive Technical Documentation** (governance, licensing, platform rigor)
- **KFM — Comprehensive Architecture, Features, and Design** (security, CI, modular services, QA)
- **KFM — AI System Overview** (Focus Mode, governance checks, prompt security, drift/bias)
- **KFM — Comprehensive UI System Overview** (provenance-first UI, offline packs, AR/3D)
- **KFM — Data Intake Technical & Design Guide** (raw immutability, deterministic ETL, STAC/DCAT/PROV)
- **KFM — Latest Ideas & Future Proposals** (agents, provenance-first CI, PR-based automation)
- **Innovative Concepts to Evolve KFM** (ethical governance, sensitive coordinates, crowdsourced verification)
- **Additional Project Ideas** (Pulse Threads, graph health checks, OCI artifacts + attestations)

### Deep reference libraries (embedded portfolio PDFs)
- **AI Concepts & more** (ML foundations → informs drift/bias gates + evaluation gates)
- **Data Management / Bayesian / Data Science portfolio** (data quality, privacy, inference-control → informs privacy gates)
- **Maps / GoogleMaps / Virtual Worlds / WebGL portfolio** (projections, 3D performance → informs geo/perf gates)
- **Programming languages & resources portfolio** (DevSecOps, CI/CD, security patterns → informs security gates)

> 🧩 **Rule:** If a design idea isn’t representable as a Gate (or backed by evidence), it’s not “real” in MCP.

---

## 🧠 Gate philosophy (non‑negotiables)

### 1) Evidence-first 🧾
A Gate should be satisfied by **evidence artifacts**, not vibes:
- `source.json` (where did it come from?)
- `run_manifest.json` (what ran, with what inputs?)
- checksums/digests (what bytes exactly?)
- STAC/DCAT/PROV triplet (what is it, where is it, how was it made?)

### 2) Fail-closed by default 🔒
If the Gate cannot determine compliance, the result is **FAIL**, not “maybe”.

### 3) Deterministic & reproducible 🎛️
Given the same inputs + configs, the Gate returns the same result.

### 4) Human-in-the-loop 🤝
Automation can propose fixes, but **humans approve** merges and **waivers**.

### 5) Surfaced everywhere 👁️
Gate status must be visible in:
- CI (merge blocking)
- Runtime (API/tool guardrails)
- UI (provenance panels, governance flags)
- Logs/Ledger (audit trail)

---

## 🧱 Gate lifecycle (Watcher → Planner → Executor)

Gates integrate cleanly with the “automation agent” model:

- 🕵️ **Watcher** detects drift/violations (new data, new deps, schema changes, failing tests)
- 🧠 **Planner** proposes a structured fix (patch, config change, metadata fill, redaction)
- 🛠️ **Executor** applies the fix **as a PR** (not a silent mutation)

> ✅ **Healthy system:** Most Gate failures become auto-generated PRs with clear evidence and a human review step.

---

## 🗺️ Where Gates run (Gate “surfaces”)

| Surface | Purpose | Typical examples |
|---|---|---|
| 🧪 **CI / PR checks** | Block merges until policy is met | schema validation, license check, graph integrity |
| 📥 **Ingestion pipeline** | Stop bad data early | raw immutability, checksum match, projection sanity |
| 🧠 **AI runtime** | Prevent hallucinations & leakage | prompt gate, citation enforcement, sensitive redaction |
| 🗺️ **UI publishing** | Prevent misleading visualization | provenance links, “no mystery layers”, AR alignment checks |
| 🎮 **Simulation output** | Ensure reproducible runs | deterministic runner, run manifests, validation rules |
| 🌐 **Federation sync** | Ensure compatibility | schema version checks, cross-region policy alignment |

---

## 🧩 Gate taxonomy (recommended packs)

Gates are grouped into **packs** so teams can run the right subset per workflow.

### Pack: `intake`
- Raw immutability
- Source + license verification
- Schema + metadata completeness
- Projection sanity checks
- Safety classification & privacy rules

### Pack: `publish`
- STAC/DCAT/PROV required
- “No mystery nodes/layers”
- Catalog QA (required fields + license)
- Story Node integrity (citations + map state config)
- UI surfacing checks

### Pack: `runtime`
- API auth + role enforcement
- Rate limit & abuse controls
- Query constraints for sensitive datasets

### Pack: `ai`
- Prompt injection defense (“Prompt Gate”)
- Citation enforcement (“no source → no answer”)
- Sensitive leakage prevention
- Drift monitoring thresholds

### Pack: `security`
- Secrets scanning
- Dependency/SBOM checks
- Artifact signing + attestations

### Pack: `geo-perf`
- Tile pyramid / caching policies
- LOD rules for 3D assets
- Offline pack constraints (size, completeness, provenance)

### Pack: `sim`
- Deterministic runner rules
- Run manifest completeness
- Verification rules & reproducibility checks

---

## 📜 Gate contract (what every Gate must implement)

A Gate must be representable as a **spec** (YAML/JSON) plus an implementation (code and/or Rego).

### ✅ Minimal required fields
```yaml
id: MCP-GATE-AI-001
name: "AI outputs must contain evidence citations"
stage: ai.runtime
severity: block   # block | warn | info
description: >
  Ensures generated answers include citations for every factual claim.
inputs:
  - type: "ai.answer"
    schema: "schemas/ai_answer.schema.json"
policy:
  type: "rego"
  entrypoint: "gates.ai.citations.deny"
evidence:
  required:
    - "gate_result.json"
    - "run_manifest.json"
auto_fix:
  supported: false
waiver:
  allowed: true
  max_days: 14
owner:
  team: "governance"
  contact: "@maintainers"
```

### ✅ Output shape (`gate_result.json`)
```json
{
  "gate_id": "MCP-GATE-AI-001",
  "status": "FAIL",
  "severity": "block",
  "summary": "Missing citations for 3 claims",
  "violations": [
    {"path": "$.claims[2]", "reason": "no citation"},
    {"path": "$.claims[5]", "reason": "no citation"},
    {"path": "$.claims[9]", "reason": "no citation"}
  ],
  "evidence": {
    "run_manifest": "artifacts/run_manifest.json",
    "inputs_digest": "sha256:...",
    "policy_version": "opa-pack@vX.Y.Z"
  },
  "timestamp": "2026-01-20T00:00:00Z"
}
```

---

## 🧰 Suggested folder layout (inside `mcp/gates/`)

```text
📦 mcp/gates/
├─ 📚 docs/
│  └─ README.md                👈 you are here
├─ 🧾 specs/
│  ├─ packs/                   # pack definitions (intake/publish/ai/etc)
│  └─ gates/                   # gate specs (yaml/json)
├─ 🧠 policies/
│  └─ rego/                    # OPA/Rego policy modules
├─ 🧪 tests/
│  ├─ fixtures/
│  └─ snapshots/
├─ 🧱 schemas/
│  ├─ stac.schema.json
│  ├─ dcat.schema.json
│  ├─ prov.schema.json
│  └─ ai_answer.schema.json
└─ 🛠️ runner/
   ├─ cli.md                   # how to run gates locally
   └─ gate_runner.(py|ts|go)   # your implementation
```

> 💡 Keep specs & policies separate so we can swap implementations (Python, TS, Go) without changing Gate definitions.

---

## ✅ Core Gate set (starter list)

Below is a “starter” set that matches KFM’s evidence-first architecture.

### 📥 Data / Intake
- **MCP-GATE-DATA-001** Raw data immutability (no in-place edits)
- **MCP-GATE-DATA-002** Checksums/digests required for all raw artifacts
- **MCP-GATE-DATA-003** Source + license metadata present & valid
- **MCP-GATE-DATA-004** Projection declared (EPSG), CRS sanity checked
- **MCP-GATE-DATA-005** Sensitivity classification required (public/sensitive/restricted)

### 🗂️ Metadata / Catalog
- **MCP-GATE-CAT-001** STAC/DCAT/PROV triplet required for publish
- **MCP-GATE-CAT-002** Schema validation (JSON Schema / SHACL where relevant)
- **MCP-GATE-CAT-003** Catalog QA (required fields, license, version tags)
- **MCP-GATE-CAT-004** Deprecation must use explicit replacement links (no silent deletes)

### 🧠 Knowledge Graph Integrity
- **MCP-GATE-GRAPH-001** No dangling edges (referential integrity)
- **MCP-GATE-GRAPH-002** No “mystery nodes” (every node links to evidence)
- **MCP-GATE-GRAPH-003** Story Nodes must link to backing datasets

### 🧠 AI / Focus Mode
- **MCP-GATE-AI-001** Every factual claim has a citation
- **MCP-GATE-AI-002** Refuse/abstain when retrieval yields no evidence
- **MCP-GATE-AI-003** Prompt Gate: sanitize inputs, prevent injection patterns
- **MCP-GATE-AI-004** Sensitive data redaction + governance flags surfaced
- **MCP-GATE-AI-005** Drift/bias monitoring thresholds recorded + alerting

### 🔐 Security / Supply Chain
- **MCP-GATE-SEC-001** Secret scanning (block commits with keys/tokens)
- **MCP-GATE-SEC-002** SBOM present for releases
- **MCP-GATE-SEC-003** Artifact signing + attestations (policy configurable)
- **MCP-GATE-SEC-004** Dependency vulnerability scanning (block critical)

### 🗺️ UI / Geo / Perf
- **MCP-GATE-GEO-001** Map layers must display provenance links (“map behind the map”)
- **MCP-GATE-GEO-002** Tile service rules (cacheability, bounds, zoom limits)
- **MCP-GATE-GEO-003** Offline pack completeness (data + metadata + provenance)
- **MCP-GATE-GEO-004** 3D assets must include LOD strategy & size limits (WebGL safety)

### 🎮 Simulation
- **MCP-GATE-SIM-001** Deterministic run manifests required
- **MCP-GATE-SIM-002** Verification checks (inputs pinned, outputs reproducible)
- **MCP-GATE-SIM-003** Governance rules for simulation outputs (sensitivity, citations)

### 🌐 Federation
- **MCP-GATE-FED-001** Schema version compatibility checks
- **MCP-GATE-FED-002** Cross-region policy parity checks (minimum baseline)

---

## 🧪 Running Gates (local + CI)

### Local run (recommended convention)
> ⚠️ Replace commands with your repo’s actual runner once implemented.

```bash
# Run a full pack against a workspace
mcp-gates run --pack intake --workspace ./data

# Run a single gate with verbose evidence output
mcp-gates run --gate MCP-GATE-CAT-001 --input ./data/processed/my_dataset
```

### CI run (recommended convention)
- PRs touching `data/**`, `docs/**`, `api/**`, `ui/**` should run targeted packs:
  - `intake` for raw/processed changes
  - `publish` for metadata + story changes
  - `ai` for prompt/templates/model config changes
  - `security` for deps/build changes

> ✅ **Merge rule:** any `severity: block` failure blocks merge.

---

## 🧯 Waivers (time‑boxed escape hatch)

Waivers exist, but they must be:
- ✅ **explicit**
- ✅ **time-boxed**
- ✅ **owned**
- ✅ **audited**
- ✅ **re-reviewed**

Recommended file:
```text
🧾 mcp/gates/waivers.yml
```

Recommended waiver fields:
```yaml
- gate_id: MCP-GATE-CAT-001
  reason: "Legacy dataset pending PROV reconstruction"
  owner: "@data-maintainers"
  expires: "2026-02-15"
  scope:
    - "data/processed/legacy/*"
```

---

## 🧷 “Gates produce artifacts” (Evidence outputs)

A Gate is not complete unless it produces artifacts that can be stored and referenced later:
- `gate_result.json`
- `run_manifest.json`
- `inputs.lock` (or digest list)
- optional: `explain.md` (human-friendly explanation)
- optional: `patch.diff` (Planner-proposed fix)

> 🧊 **Best practice:** store Gate evidence as immutable objects (e.g., OCI artifacts) so audits remain stable.

---

## 🧠 Gate authoring checklist (copy/paste)

- [ ] Define **exact invariant** (what must always be true?)
- [ ] Define **inputs** (schemas + trust boundary)
- [ ] Define **evidence** required to pass
- [ ] Choose enforcement level: `block | warn | info`
- [ ] Write policy (Rego) and/or deterministic code
- [ ] Add fixtures + tests (good/bad cases)
- [ ] Add UI surfacing requirements (where will users see it?)
- [ ] Define waiver rules (allowed? max duration? owners?)
- [ ] Document failure modes + remediation steps

---

## 🗣️ Glossary (tiny but crucial)

- **Gate:** Deterministic check that returns PASS/WARN/FAIL and emits evidence.
- **Policy Pack:** Bundle of Gate policies (OPA/Rego) versioned like code.
- **Evidence Triplet:** STAC (spatiotemporal index), DCAT (catalog discovery), PROV (lineage).
- **Provenance-first:** Every output traceable to inputs + transforms.
- **Prompt Gate:** AI input/output policy guardrail to prevent injection/leakage.
- **W‑P‑E:** Watcher → Planner → Executor automation pattern (PR-based, reviewable).

---

## 🔗 Next docs to create (recommended)

- `mcp/gates/docs/authoring.md` — How to write a Gate (examples + gotchas)
- `mcp/gates/docs/packs.md` — What each pack contains and when to run it
- `mcp/gates/docs/waivers.md` — Waiver process + audit expectations
- `mcp/gates/docs/evidence.md` — Evidence artifacts spec (run_manifest, source.json, etc.)
- `mcp/gates/docs/ui-surfacing.md` — How Gate results appear in UI/Focus Mode

---

## 🏁 Bottom line

**MCP Gates are the contract between creativity and credibility.**  
They let the system evolve rapidly (agents, new data, new stories) **without** sacrificing trust.

✅ **If it can’t be proven, it can’t ship.**  
✅ **If it’s sensitive, it’s protected by default.**  
✅ **If it’s AI-generated, it’s labeled and cited.**

---
