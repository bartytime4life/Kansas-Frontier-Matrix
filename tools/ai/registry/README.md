---
title: "KFM AI Registry — README"
path: "tools/ai/registry/README.md"
version: "v0.1.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:tools:ai:registry:readme:v0.1.0"
semantic_document_id: "kfm-tools-ai-registry-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:tools:ai:registry:readme:v0.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM AI Registry — README

## 📘 Overview

### Purpose

The **AI Registry** is the single canonical place to **declare, version, and govern** AI/ML assets used by KFM, including:

- models (LLMs, embedding models, classifiers),
- prompt packs / extraction templates,
- AI transforms (e.g., summarization, structure extraction),
- evaluation harnesses and minimum quality thresholds,
- drift/quality monitors and telemetry expectations.

This registry exists to keep KFM **contract-first** and **evidence-first**:

- **Contract-first:** AI behavior is declared in a schema-validated registry (no “mystery model changes”).
- **Evidence-first:** any AI outputs that become user-visible must be backed by provenance and (when applicable) STAC/DCAT/PROV artifacts.

### Scope

In scope:

- Registry *format* (what gets registered, required fields, versioning rules)
- Validation expectations (schema + policy gates)
- Integration points (pipelines, API boundary, Focus Mode provenance/audit)
- Governance triggers for adding/changing AI capabilities

Out of scope:

- Full cloud deployment instructions (keep ops details in dedicated runbooks if/when introduced)
- Training pipelines for custom models (handled as separate, reproducible workflows)

### Audience

- AI / data engineering maintainers
- API maintainers (who enforce registry-driven allowlists)
- Governance reviewers (who approve new AI narrative behaviors)
- Contributors adding a new AI evidence product or model integration

### Definitions (link to glossary)

- **AI asset**: any model, prompt pack, or transform component used to produce outputs (including evidence artifacts).
- **AI transform**: a bounded, named operation applied to source/evidence (e.g., `summarize`, `structure_extract`).
- **Prompt pack**: versioned prompts/templates used for extraction or summarization.
- **Model card**: a governed description of model usage, limitations, evaluation, and risks (canonical home: `mcp/`).
- **Evidence product**: AI-derived artifact treated as *evidence* (not narrative), represented in STAC/DCAT/PROV when it enters the pipeline.

> Glossary location is **not confirmed in repo**. If a glossary exists, link it here (recommended: `docs/glossary.md` or `docs/standards/GLOSSARY.md`).

### Key artifacts (what this doc points to)

- This README: `tools/ai/registry/README.md`
- Master Guide (canonical ordering + invariants): `docs/MASTER_GUIDE_v12.md`
- v13 redesign blueprint (canonical homes + CI gates): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance / ethics / sovereignty:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/ETHICS.md`
  - `docs/governance/SOVEREIGNTY.md`

Registry files and schemas (**not confirmed in repo**, proposed canonical locations):

- Registry source:
  - `tools/ai/registry/registry.yaml`
- Registry schema:
  - `schemas/ai/registry.schema.json`
- Registry validation entrypoint:
  - `tools/ai/registry/validate.py` (or `src/pipelines/**` if treated as a pipeline step)
- Model cards / eval reports:
  - `mcp/model_cards/`
  - `mcp/evaluations/`

### Definition of done (for this document)

- [ ] Describes what the registry controls and what it does *not* control
- [ ] States non-negotiable constraints (no unsourced narrative; API boundary; provenance-first)
- [ ] Defines the minimal registry entry contract (fields + versioning)
- [ ] Defines validation expectations (schema + policy checks)
- [ ] Specifies where registry artifacts live (or flags **not confirmed in repo**)
- [ ] Includes CI validation steps and telemetry expectations

## 🗂️ Directory Layout

### This document

- Path: `tools/ai/registry/README.md`
- Owner: **TBD** (recommend assigning to “AI + Governance” maintainers)

### Related repository paths

- `tools/ai/` — operational and tooling utilities (this registry lives here)
- `mcp/` — experiments, model cards, SOPs (referenced by registry entries)
- `schemas/` — JSON Schemas and contract artifacts (registry schema belongs here)
- `src/server/` — API boundary (registry enforcement should occur here)
- `src/pipelines/` — deterministic transforms (AI evidence products must be reproducible)
- `docs/telemetry/` + `schemas/telemetry/` — telemetry definitions and validation

### Expected file tree for this sub-area

~~~text
📁 tools/
└── 🤖 ai/
    ├── 🧭 registry/
    │   ├── 📄 README.md
    │   ├── 📄 registry.yaml                # not confirmed in repo
    │   ├── 🧪 validate_registry.py         # not confirmed in repo
    │   └── 📁 examples/                    # optional; not confirmed in repo
    └── 📈 drift/                           # if present: drift monitoring tooling
~~~

## 🧭 Context

### Background

KFM uses AI to enhance discovery and assist with extraction/summarization, but it requires:

- **benchmarked quality** (tests on known examples, regression checks in CI),
- **governance oversight** for new AI capabilities (especially user-visible narrative behavior),
- **provenance-first integration** so AI outputs never become “unsourced narrative.”

The registry provides the contract surface that makes those expectations enforceable.

### Assumptions

- The system follows the canonical ordering: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- AI is treated as an *assistant* that produces **evidence products**, not authoritative claims.
- The API layer is the enforcement boundary for what the UI can access and what AI behaviors are allowed.

### Constraints / invariants

Non-negotiables for registry-driven AI behavior:

1. **No unsourced narrative**
   - Any user-visible AI text must be provenance-linked and auditable.
2. **No UI direct-to-graph reads**
   - `web/` must not query Neo4j directly; AI-related bundles flow through the API boundary.
3. **Contracts are canonical**
   - Registry must be schema-validated; API/pipelines must rely on the registry (no hard-coded “secret defaults”).
4. **No secrets in-repo**
   - The registry may reference *how* to locate secrets (e.g., environment variable names), but must never store keys/tokens.

### Open questions

- What is the minimum viable registry schema for “CI green”?
- Where is the authoritative model-card format stored (under `mcp/`)? (**not confirmed in repo**)
- Does the API expose a “registry introspection” endpoint for audit purposes? (**not confirmed in repo**)
- Should registry entries be signed (e.g., checksum + provenance bundle) before release? (**not confirmed in repo**)

### Future extensions

- Tight integration with drift tooling (`tools/ai/drift/`) so registered assets can declare drift monitors.
- Registry-driven evaluation “suites” so each model/prompt pack declares required benchmarks.
- Support for multiple runtime backends (local inference vs managed service) without changing downstream contracts.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["Registry source<br/>tools/ai/registry/registry.yaml"] --> B["Schema + policy validation<br/>schemas/ai/registry.schema.json"]
  B -->|pass| C["Registry resolver<br/>(build-time + runtime)"]
  B -->|fail| X["CI gate fails"]

  C --> D["API boundary enforcement<br/>src/server/"]
  C --> E["Pipeline transforms<br/>src/pipelines/"]

  E --> F["Evidence artifacts<br/>data/stac + data/catalog/dcat + data/prov"]
  D --> G["Focus Mode bundles<br/>(narrative + provenance + AI audit)"]
  G --> H["UI<br/>web/"]

  C --> T["Telemetry signals<br/>docs/telemetry + schemas/telemetry"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as CI
  participant Reg as AI Registry
  participant API as API Boundary
  participant UI as UI (Focus Mode)

  Dev->>Reg: Propose new registry entry (model/prompt/transform)
  CI->>Reg: Validate schema + policy gates
  CI-->>Dev: Pass/Fail + diffs

  API->>Reg: Resolve allowed transforms for request
  UI->>API: Request Focus bundle
  API-->>UI: Bundle includes AI provenance refs + citations
~~~

## 📦 Data & Metadata

### Inputs

- Registry source (YAML/JSON): declared models/prompt packs/transforms
- Model cards: `mcp/` (format and location **not confirmed in repo**)
- Evaluation fixtures / gold sets:
  - recommended: `tests/fixtures/ai/` (**not confirmed in repo**)
- Run manifests and logs:
  - recommended: `mcp/runs/` or `src/pipelines/**` manifests (**not confirmed in repo**)

### Outputs

- Resolved registry (normalized JSON) for API/pipeline consumers (**not confirmed in repo**)
- Validation reports (CI artifacts) proving:
  - schema validity,
  - policy compliance,
  - evaluation baseline compatibility.
- Provenance hooks to link AI runs to:
  - STAC assets (when AI outputs become evidence artifacts),
  - PROV activities/agents/entities.

### Sensitivity & redaction

Potentially sensitive registry content:

- prompts that could reveal sensitive inference strategies,
- references to restricted datasets or redaction rules,
- deployment endpoints.

Rules:

- Never store secrets, tokens, or credentials in the registry.
- Mark entries that touch culturally sensitive content as “review required” (see governance section).
- Explicitly prohibit transforms that infer sensitive locations.

### Quality signals

Recommended minimum quality signals for registry entries:

- benchmark metrics (precision/recall for extraction; qualitative rubric for summaries)
- regression thresholds (fail CI if performance drops unexpectedly)
- drift monitors (distribution shift alerts; output-stability checks)
- reproducibility identifiers:
  - model version / hash,
  - prompt pack version,
  - deterministic transform config hash.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

When AI produces an **evidence product** (e.g., structured extraction results, embeddings, entity link candidates):

- represent outputs as STAC Items/Assets under `data/stac/`,
- store an asset reference to the registry entry ID and transform run ID.

### DCAT

When AI outputs are treated as datasets:

- register a DCAT dataset record under `data/catalog/dcat/`,
- include license/keywords/description consistent with the evidence product’s purpose.

### PROV-O

For every AI evidence-producing run:

- record a `prov:Activity` for the transform execution,
- record a `prov:Agent` representing the model/prompt pack (linked to registry entry),
- record a `prov:Entity` for produced artifacts (STAC/DCAT outputs).

### Versioning

- Registry changes must be versioned and reviewable.
- Prefer additive changes; breaking changes require an explicit version bump and downstream contract updates.
- Deprecations should be explicit (e.g., `deprecated: true` with a replacement pointer) — schema **not confirmed in repo**.

## 🧱 Architecture

### Components

- **Registry source**: human-editable registry file(s)
- **Schema validator**: machine validation (JSON Schema) + policy checks
- **Resolver**: converts registry entries into runtime-ready configuration for:
  - pipeline transforms,
  - API allowlists.
- **Governance hooks**: tagging entries that require review/approval
- **Telemetry hooks**: emits signals on registry changes and runtime usage

### Interfaces / contracts

**Recommended minimum entry types** (schema details **not confirmed in repo**):

- `model`
- `prompt_pack`
- `transform`
- `evaluation_suite`

Example (illustrative) registry snippet:

~~~yaml
registry_version: "v1"
entries:
  - id: "urn:kfm:ai:model:llm:default"
    kind: "model"
    name: "Default LLM"
    version: "TBD"
    allowed_transforms:
      - "summarize"
      - "structure_extract"
    artifacts:
      model_card: "mcp/model_cards/TBD.md"     # not confirmed in repo
      eval_report: "mcp/evaluations/TBD.md"    # not confirmed in repo
    governance:
      review_required: true
      review_reason: "new AI narrative behaviors"
    provenance:
      prov_agent_id: "urn:kfm:agent:ai:model:llm:default"
    notes: "Never store API keys here."
~~~

### Extension points checklist (for future work)

- [ ] AI registry schema added under `schemas/ai/`
- [ ] Validator integrated into CI (fail if invalid; deterministic behavior)
- [ ] Pipelines read registry entries by stable ID (no hard-coded model choices)
- [ ] API allowlist enforced from registry (UI cannot bypass)
- [ ] Evidence products emitted to STAC/DCAT/PROV when AI outputs become evidence
- [ ] Telemetry signals recorded + schema version bump if new signals added
- [ ] Governance review gates documented and enforced for sensitive AI behaviors

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

If AI contributes to a Focus Mode bundle:

- show **which registry entry** was used (model + prompt pack versions),
- provide a **provenance panel** linking to:
  - the underlying evidence records,
  - the AI run’s PROV activity,
  - evaluation context (if relevant).

### Provenance-linked narrative rule

- Any narrative text produced/assisted by AI must have:
  - citations to evidence IDs (documents, records, STAC assets),
  - an AI audit reference (registry entry ID + run ID),
  - clear labeling when content is AI-assisted vs curator-authored.

### Optional structured controls

~~~yaml
focus_panels:
  - "narrative"
  - "provenance"
  - "ai_audit"     # not confirmed in repo
ai_audit:
  registry_entry_ids:
    - "urn:kfm:ai:model:llm:default"
  show_eval_summary: true
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Registry schema validation (JSON Schema) (**not confirmed in repo**)
- [ ] Policy checks:
  - [ ] transforms allowed/prohibited
  - [ ] no secret-like fields committed
- [ ] “Golden” evaluation regression tests for key transforms (**not confirmed in repo**)
- [ ] API contract tests if registry affects public endpoints (**not confirmed in repo**)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate the registry against its schema
# ./tools/ai/registry/validate_registry.py tools/ai/registry/registry.yaml

# 2) run AI evaluation smoke tests (small fixture set)
# pytest -q tests/ai

# 3) run markdown lint / protocol validation
# ./tools/validate_markdown_protocol.sh
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `ai_registry_change` | git + CI | `docs/telemetry/` + `schemas/telemetry/` |
| `ai_transform_invocation` | API/pipelines | `docs/telemetry/` + `schemas/telemetry/` |
| `ai_eval_regression` | CI eval harness | `docs/telemetry/` + `schemas/telemetry/` |
| `ai_drift_alert` | drift tooling | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

Registry changes that **require governance review** (recommended):

- adding a new model that generates user-visible content,
- changing prompt packs that affect narrative or extraction behavior,
- enabling new transform types (especially anything beyond the allowed list),
- changes involving culturally sensitive materials or locations.

### CARE / sovereignty considerations

- Treat culturally sensitive knowledge as requiring explicit review and access rules.
- Avoid publishing granular locations for sensitive sites unless policy allows.
- Ensure redaction rules are enforced at the API boundary and reflected in Focus Mode.

### AI usage constraints

This document’s AI permissions/prohibitions must match front-matter:

Allowed:

- `summarize`
- `structure_extract`
- `translate`
- `keyword_index`

Prohibited:

- `generate_policy`
- `infer_sensitive_locations`

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-22 | Initial README for AI registry | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
