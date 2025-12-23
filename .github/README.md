diff --git a/.github/README.md b/.github/README.md
new file mode 100644
index 0000000..1111111
--- /dev/null
+++ b/.github/README.md
@@ -0,0 +1,349 @@
+---
+title: "KFM GitHub Automation and Governance"
+path: ".github/README.md"
+version: "v1.0.0"
+last_updated: "2025-12-22"
+status: "draft"
+doc_kind: "Guide"
+license: "CC-BY-4.0"
+
+markdown_protocol_version: "KFM-MDP v11.2.6"
+mcp_version: "MCP-DL v6.3"
+ontology_protocol_version: "KFM-ONTO v4.1.0"
+pipeline_contract_version: "KFM-PPC v11.0.0"
+stac_profile: "KFM-STAC v11.0.0"
+dcat_profile: "KFM-DCAT v11.0.0"
+prov_profile: "KFM-PROV v11.0.0"
+
+governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
+ethics_ref: "docs/governance/ETHICS.md"
+sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
+fair_category: "FAIR+CARE"
+care_label: "TBD"
+sensitivity: "public"
+classification: "open"
+jurisdiction: "US-KS"
+
+doc_uuid: "urn:kfm:doc:github:readme:v1.0.0"
+semantic_document_id: "kfm-github-readme-v1.0.0"
+event_source_id: "ledger:kfm:doc:github:readme:v1.0.0"
+commit_sha: "<latest-commit-hash>"
+
+ai_transform_permissions:
+  - "summarize"
+  - "structure_extract"
+  - "translate"
+  - "keyword_index"
+ai_transform_prohibited:
+  - "generate_policy"
+  - "infer_sensitive_locations"
+
+doc_integrity_checksum: "sha256:<calculate-and-fill>"
+---
+
+# .github — Automation, Policies, and Contribution UX
+
+## 📘 Overview
+
+### Purpose
+
+This directory is the **canonical home** for GitHub-native repository automation and contribution UX:
+
+- CI workflows (validation gates and checks)
+- Reusable actions (composite actions)
+- Workflow test inputs (“fixtures”)
+- Repo policy surface area (security policy, issue/PR templates)
+
+The intent is to make CI behavior **deterministic** and to keep the repo aligned to KFM’s canonical, contract-first pipeline ordering.
+
+### Scope
+
+In scope:
+
+- `.github/workflows/**` (CI workflows)
+- `.github/actions/**` (composite actions used by workflows)
+- `.github/**` templates and compliance files (e.g., security policy)
+
+Out of scope:
+
+- Runtime system code (`src/**`, `web/**`)
+- Data and catalogs (`data/**`)
+- Schemas and contracts (`schemas/**`, `src/server/contracts/**`)
+
+### Audience
+
+- Repo maintainers
+- Contributors editing workflows/actions/templates
+- Anyone debugging CI failures
+
+### Definitions (link to glossary)
+
+- `docs/glossary.md` (recommended)
+- **Workflow**: GitHub Actions workflow under `.github/workflows/`
+- **Composite action**: reusable action under `.github/actions/`
+- **Fixture**: deterministic, non-sensitive test input used by an action/workflow
+
+### Key artifacts (what this doc points to)
+
+- `.github/workflows/` — CI gates (schema validation, graph checks, contract tests, etc.)
+- `.github/actions/` — shared CI logic
+- `.github/actions/fixtures/` — fixtures used by CI actions (example: graph fixtures)
+
+### Definition of done (for this document)
+
+- [ ] Front-matter complete and valid
+- [ ] Clear “what goes where” for `.github/`
+- [ ] Defines how fixtures should be treated (deterministic, no secrets/PII)
+- [ ] Provides a minimal “where to look” map for debugging CI failures
+
+## 🗂️ Directory Layout
+
+### This document
+
+- **path:** `.github/README.md`
+- **role:** human-facing map of CI and GitHub-native governance
+
+### Related repository paths
+
+| Area | Canonical path | Notes |
+|---|---|---|
+| Workflows | `.github/workflows/` | CI gates and checks |
+| Composite actions | `.github/actions/` | Reusable workflow steps |
+| Action fixtures | `.github/actions/fixtures/` | Deterministic CI inputs |
+| Security policy | `.github/SECURITY.md` | Disclosure + reporting policy surface |
+| Schemas | `schemas/` | STAC/DCAT/PROV, story node, UI, telemetry schemas |
+| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Outputs validated by CI |
+| Graph | `src/graph/`, `data/graph/` | Ontology + ingest/import artifacts |
+| API contracts | `src/server/contracts/` | Contract-first boundary for API layer |
+| UI | `web/` | UI must not query Neo4j directly |
+
+### Expected file tree for this sub-area
+
+~~~text
+📁 .github/
+├── 📁 actions/
+│   ├── 📁 fixtures/
+│   │   └── 📁 graph/
+│   │       ├── 📄 README.md
+│   │       └── 📁 valid/
+│   │           └── 📄 README.md
+│   └── 📁 <action-name>/
+│       ├── 📄 action.yml
+│       └── 📄 README.md
+├── 📁 workflows/
+│   └── 📄 <workflow>.yml
+├── 📄 SECURITY.md
+├── 📄 pull_request_template.md
+└── 📁 ISSUE_TEMPLATE/
+    └── 📄 <template>.yml
+~~~
+
+## 🧭 Context
+
+### Background
+
+KFM uses CI as the contract-enforcement mechanism that keeps the repo aligned to:
+
+- one canonical home per subsystem (no “mystery duplicates”),
+- governed standards and profiles (schemas validate, contracts validate),
+- deterministic, reproducible outputs.
+
+### Assumptions
+
+- CI workflows **skip checks** when an optional root is absent, but **fail deterministically** when a referenced root exists and is invalid.
+- Workflows do not require network access for unit-level validation unless explicitly designed to do so.
+
+### Constraints / invariants
+
+Non-negotiables that CI should help preserve:
+
+1. **Canonical pipeline ordering**
+   - ETL → catalogs (STAC/DCAT/PROV) → graph → API → UI → Story Nodes → Focus Mode
+
+2. **API boundary is enforced**
+   - `web/` must never query Neo4j directly; all graph access is via `src/server/`.
+
+3. **No unsourced narrative**
+   - Published Story Nodes must be provenance-linked and validate.
+
+4. **Contracts are canonical**
+   - Schemas live in `schemas/` and API contracts under `src/server/contracts/` and must validate in CI.
+
+5. **Repo lint invariants**
+   - No YAML front-matter in code files
+   - No `README.me`
+   - No duplicate canonical homes without explicit deprecation markers
+
+## 🗺️ Diagrams
+
+### System / dataflow diagram
+
+~~~mermaid
+flowchart LR
+  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
+  B --> C[Graph<br/>Neo4j / src/graph + data/graph]
+  C --> D[APIs<br/>src/server]
+  D --> E[React/Map UI<br/>web/]
+  E --> F[Story Nodes<br/>docs/reports/story_nodes]
+  F --> G[Focus Mode]
+~~~
+
+### Optional: sequence diagram
+
+~~~mermaid
+sequenceDiagram
+  participant Dev as Contributor
+  participant GH as GitHub Actions
+  participant Repo as Repo Contents
+
+  Dev->>Repo: Push PR / commit
+  GH->>Repo: Checkout code
+  GH->>GH: Run CI gates (schemas, graph, contracts, security)
+  GH-->>Dev: Status checks + logs/artifacts
+~~~
+
+## 📦 Data & Metadata
+
+### Inputs
+
+- Git state (PR diffs, branches, tags)
+- Repository files (schemas, catalogs, code, docs)
+- Workflow configuration (YAML under `.github/workflows/`)
+
+### Outputs
+
+- Status checks (pass/fail)
+- Logs and artifacts (as configured by workflows)
+- Optional: validation reports (JSON, SARIF, etc.)
+
+### Sensitivity & redaction
+
+- Never commit secrets, access tokens, or credentials.
+- Fixtures used by CI must avoid:
+  - personal data,
+  - restricted locations,
+  - culturally sensitive knowledge (unless appropriately generalized/redacted and approved).
+
+### Quality signals
+
+- Deterministic CI runs (repeatable results for the same commit)
+- No orphan references (IDs and links resolve where required)
+- Schemas and contracts validate successfully
+
+## 🌐 STAC, DCAT & PROV Alignment
+
+CI workflows should validate catalog and provenance artifacts against schemas:
+
+### STAC
+
+- `data/stac/**` validates against `schemas/stac/**`
+
+### DCAT
+
+- `data/catalog/dcat/**` validates against `schemas/dcat/**`
+
+### PROV-O
+
+- `data/prov/**` validates against `schemas/prov/**`
+
+### Versioning
+
+- Version lineage links should be consistent across catalogs and graph representations.
+
+## 🧱 Architecture
+
+### Components
+
+- **Workflows**: `.github/workflows/**`
+- **Composite actions**: `.github/actions/**`
+- **Fixtures**: `.github/actions/fixtures/**`
+- **Compliance surface**: `.github/SECURITY.md` and templates
+
+### Interfaces / contracts
+
+CI assumes the following contract boundaries:
+
+- **Schemas** are authoritative under `schemas/`
+- **API contracts** are authoritative under `src/server/contracts/`
+- **Graph ontology/migrations** are authoritative under `src/graph/`
+
+### Extension points checklist (for future work)
+
+- [ ] Add or tighten schema validation (STAC/DCAT/PROV/story nodes/UI/telemetry)
+- [ ] Add new graph integrity checks (ontology, constraints, orphan refs)
+- [ ] Add or expand API contract tests (REST/GraphQL)
+- [ ] Add security/sovereignty scanning where applicable
+
+## 🧠 Story Node & Focus Mode Integration
+
+### How this work surfaces in Focus Mode
+
+- CI ensures Story Nodes are valid and provenance-linked so Focus Mode can safely render evidence-backed context.
+
+### Provenance-linked narrative rule
+
+- Any published narrative must trace to dataset / record / asset identifiers.
+
+### Optional structured controls
+
+~~~yaml
+# Optional example — only if a workflow/action needs structured controls.
+focus_mode:
+  require_provenance: true
+  allow_predictions: false
+~~~
+
+## 🧪 Validation & CI/CD
+
+### Validation steps
+
+- [ ] Markdown protocol checks (front-matter, required sections)
+- [ ] Schema validation (STAC/DCAT/PROV/story nodes/UI/telemetry)
+- [ ] Graph integrity checks (ontology compliance, orphan refs)
+- [ ] API contract tests
+- [ ] Security and sovereignty checks (as applicable)
+
+### Reproduction
+
+~~~bash
+# Example placeholders — replace with repo-specific commands
+# 1) validate schemas
+# 2) run unit/integration tests
+# 3) run doc lint
+~~~
+
+### Telemetry signals (if applicable)
+
+| Signal | Source | Where recorded |
+|---|---|---|
+| CI job status | GitHub Actions | Workflow logs / artifacts |
+| Validation report | Validators | Artifacts (JSON/SARIF) if enabled |
+
+## ⚖ FAIR+CARE & Governance
+
+### Review gates
+
+- Changes to CI gates, security scans, or publication workflows should be reviewed by maintainers and (where applicable) governance owners.
+
+### CARE / sovereignty considerations
+
+- Treat fixtures and test data as real releases: avoid sensitive content, generalize where required, and document approval needs.
+
+### AI usage constraints
+
+- Follow AI permissions/prohibitions in front-matter.
+- Do not introduce AI-generated outputs into published artifacts without provenance linkage and review.
+
+## 🕰️ Version History
+
+| Version | Date | Summary | Author |
+|---|---|---|---|
+| v1.0.0 | 2025-12-22 | Initial `.github/` documentation | TBD |
+
+---
+
+Footer refs:
+
+- Governance: `docs/governance/ROOT_GOVERNANCE.md`
+- Ethics: `docs/governance/ETHICS.md`
+- Sovereignty: `docs/governance/SOVEREIGNTY.md`
diff --git a/.github/actions/fixtures/graph/README.md b/.github/actions/fixtures/graph/README.md
new file mode 100644
index 0000000..1111111
--- /dev/null
+++ b/.github/actions/fixtures/graph/README.md
@@ -0,0 +1,320 @@
+---
+title: "KFM Graph Action Fixtures"
+path: ".github/actions/fixtures/graph/README.md"
+version: "v1.0.0"
+last_updated: "2025-12-22"
+status: "draft"
+doc_kind: "Guide"
+license: "CC-BY-4.0"
+
+markdown_protocol_version: "KFM-MDP v11.2.6"
+mcp_version: "MCP-DL v6.3"
+ontology_protocol_version: "KFM-ONTO v4.1.0"
+pipeline_contract_version: "KFM-PPC v11.0.0"
+stac_profile: "KFM-STAC v11.0.0"
+dcat_profile: "KFM-DCAT v11.0.0"
+prov_profile: "KFM-PROV v11.0.0"
+
+governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
+ethics_ref: "docs/governance/ETHICS.md"
+sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
+fair_category: "FAIR+CARE"
+care_label: "TBD"
+sensitivity: "public"
+classification: "open"
+jurisdiction: "US-KS"
+
+doc_uuid: "urn:kfm:doc:github:actions:fixtures:graph:readme:v1.0.0"
+semantic_document_id: "kfm-github-actions-fixtures-graph-readme-v1.0.0"
+event_source_id: "ledger:kfm:doc:github:actions:fixtures:graph:readme:v1.0.0"
+commit_sha: "<latest-commit-hash>"
+
+ai_transform_permissions:
+  - "summarize"
+  - "structure_extract"
+  - "translate"
+  - "keyword_index"
+ai_transform_prohibited:
+  - "generate_policy"
+  - "infer_sensitive_locations"
+
+doc_integrity_checksum: "sha256:<calculate-and-fill>"
+---
+
+# .github/actions/fixtures/graph — Graph Validation Fixtures
+
+## 📘 Overview
+
+### Purpose
+
+This folder contains **small, deterministic graph fixture bundles** used by GitHub Actions to validate:
+
+- graph ingest/import tooling behavior,
+- ontology/shape constraints (labels, relationship types, required properties),
+- cross-artifact linkage expectations (e.g., when nodes reference STAC/DCAT/PROV identifiers).
+
+Fixtures exist to support CI gates and to enable an end-to-end “vertical slice” test of the graph stage.
+
+### Scope
+
+In scope:
+
+- Deterministic, minimal fixture graphs used in CI
+- Synthetic or de-identified examples that are safe to publish
+
+Out of scope:
+
+- Production graph data
+- Large datasets or any fixture requiring network access
+- Sensitive locations, personal data, or culturally restricted knowledge (unless explicitly generalized/redacted and approved)
+
+### Audience
+
+- Graph/ontology maintainers
+- CI/workflow maintainers
+- Contributors adding or debugging graph validation tests
+
+### Definitions (link to glossary)
+
+- `docs/glossary.md` (recommended)
+- **Fixture bundle**: a folder containing the files needed for one graph test scenario
+- **Valid fixture**: expected to pass all graph validation and import checks
+- **Invalid fixture** (optional): expected to fail validation for a known reason (used to prevent regressions)
+
+### Key artifacts (what this doc points to)
+
+- `valid/` — fixtures that must pass validation (positive test cases)
+- (Optional) `invalid/` — fixtures that must fail validation (negative test cases)
+
+### Definition of done (for this document)
+
+- [ ] Explains what belongs in this folder (and what does not)
+- [ ] Defines safe-handling expectations (no secrets/PII, no restricted locations)
+- [ ] Provides a standard fixture-bundle structure and naming conventions
+
+## 🗂️ Directory Layout
+
+### This document
+
+- **path:** `.github/actions/fixtures/graph/README.md`
+
+### Related repository paths
+
+| Area | Canonical path | Notes |
+|---|---|---|
+| Composite actions | `.github/actions/` | Reusable steps used by workflows |
+| Workflows | `.github/workflows/` | Calls actions/fixtures during CI |
+| Graph subsystem | `src/graph/` | Ontology, migrations, constraints, loaders |
+| Graph import outputs | `data/graph/` | Import CSVs and/or Cypher scripts (canonical outputs) |
+| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Identifiers that graph nodes may reference |
+
+### Expected file tree for this sub-area
+
+~~~text
+📁 .github/actions/fixtures/graph/
+├── 📄 README.md
+└── 📁 valid/
+    ├── 📄 README.md
+    └── 📁 case-<slug>/
+        ├── 📄 README.md
+        ├── 📄 fixture.manifest.json
+        └── 📁 graph/
+            ├── 📄 <nodes>.<ext>
+            ├── 📄 <edges>.<ext>
+            └── 📄 <constraints_or_import>.<ext>
+~~~
+
+> Note: file extensions and exact filenames are intentionally flexible; they should match what the validating action expects.
+
+## 🧭 Context
+
+### Background
+
+KFM’s canonical pipeline places the graph after ETL and catalogs, and before APIs and UI. Graph fixtures are CI-friendly test inputs that help ensure graph tooling remains stable and governed.
+
+### Assumptions
+
+- Fixtures are small enough to run quickly in CI.
+- Fixtures do not require external services; any required schemas/constraints are available in-repo.
+
+### Constraints / invariants
+
+- Fixtures must be deterministic and diff-friendly (stable ordering, stable IDs).
+- Fixtures must not include secrets, PII, or restricted/culturally sensitive locations unless properly generalized/redacted and approved.
+- Fixtures should align to the ontology and schema constraints enforced by `src/graph/` tooling.
+
+### Open questions
+
+- What is the canonical fixture manifest schema (if any) for this repo?
+- Do we standardize on CSV import fixtures, Cypher import fixtures, or both?
+
+### Future extensions
+
+- Add negative fixtures (`invalid/`) for common ontology violations
+- Add fixtures that test provenance-linking fields (STAC/DCAT/PROV IDs) without requiring full catalogs
+
+## 🗺️ Diagrams
+
+### System / dataflow diagram
+
+~~~mermaid
+flowchart LR
+  A[Fixture bundle<br/>.github/actions/fixtures/graph] --> B[Graph validator/importer<br/>CI action]
+  B --> C{Expected result}
+  C -->|pass| D[Valid fixture]
+  C -->|fail| E[Invalid fixture (optional)]
+~~~
+
+### Optional: sequence diagram
+
+~~~mermaid
+sequenceDiagram
+  participant WF as Workflow
+  participant ACT as Graph Validation Action
+  participant FX as Fixture Bundle
+
+  WF->>ACT: Invoke (select fixture)
+  ACT->>FX: Load fixture files
+  ACT->>ACT: Validate / import (local)
+  ACT-->>WF: Pass/Fail + logs
+~~~
+
+## 📦 Data & Metadata
+
+### Inputs
+
+- Fixture bundle files (CSV/Cypher/JSON/etc., as expected by the action)
+- Any in-repo schemas/constraints referenced by the validating action
+
+### Outputs
+
+- CI pass/fail signal
+- Optional validation report artifacts (if enabled by the workflow)
+
+### Sensitivity & redaction
+
+- Prefer synthetic examples; avoid real names/addresses.
+- If a place must be represented, use generalized geometry or a clearly fictionalized example.
+
+### Quality signals
+
+- Fixtures remain stable across time (no nondeterministic generation)
+- Each fixture has a short README explaining the scenario and expected outcome
+- Fixture names are unique and descriptive
+
+## 🌐 STAC, DCAT & PROV Alignment
+
+### STAC
+
+- If a fixture includes references to STAC IDs, use realistic ID formats and document the mapping in the fixture README.
+
+### DCAT
+
+- If a fixture includes dataset identifiers, ensure they are stable and clearly fictional or derived from in-repo catalog artifacts.
+
+### PROV-O
+
+- If a fixture tests provenance linkage, include placeholder PROV activity IDs and document how they should be resolved.
+
+### Versioning
+
+- If fixtures encode version lineage fields, ensure predecessor/successor relationships are consistent within the fixture.
+
+## 🧱 Architecture
+
+### Components
+
+- Fixture bundles (this directory)
+- Graph validator/importer logic (composite action + graph tooling)
+- CI workflows that run the action
+
+### Interfaces / contracts
+
+- Fixture format is an internal contract between:
+  - the validating action (consumer), and
+  - fixture bundles (producer).
+
+If the fixture contract changes, update:
+
+- fixtures,
+- the action documentation,
+- and any workflow that depends on it.
+
+### Extension points checklist (for future work)
+
+- [ ] Add a fixture manifest JSON Schema under `schemas/` (if desired)
+- [ ] Add a standard “case README” template for fixture bundles
+- [ ] Add negative fixtures to prevent regressions
+
+## 🧠 Story Node & Focus Mode Integration
+
+### How this work surfaces in Focus Mode
+
+Indirect: stable graph ingest and constraints help ensure Story Nodes can reference graph entities safely.
+
+### Provenance-linked narrative rule
+
+- Any fixture that includes narrative-like text must be labeled as synthetic and must not be published as a Story Node.
+
+### Optional structured controls
+
+~~~yaml
+# Optional: if a workflow selects fixtures by label/tag.
+fixture_selector:
+  include: ["valid"]
+  exclude: ["requires_network"]
+~~~
+
+## 🧪 Validation & CI/CD
+
+### Validation steps
+
+- [ ] Fixture bundle is deterministic and small
+- [ ] Fixture contains no secrets/PII/sensitive locations
+- [ ] Fixture passes (or fails) validation as expected
+- [ ] CI logs are readable (errors point to the fixture case)
+
+### Reproduction
+
+~~~bash
+# Example placeholders — replace with repo-specific commands
+# 1) run the graph validator/importer locally against a fixture bundle
+# 2) run ontology/constraint checks
+# 3) run any fixture-specific tests
+~~~
+
+### Telemetry signals (if applicable)
+
+| Signal | Source | Where recorded |
+|---|---|---|
+| Fixture-case pass/fail | CI workflow | Workflow logs |
+| Validator report | Graph validator | Artifacts (if enabled) |
+
+## ⚖ FAIR+CARE & Governance
+
+### Review gates
+
+- Any fixture that encodes real-world sensitive content requires governance review and explicit approval.
+
+### CARE / sovereignty considerations
+
+- Prefer synthetic data and generalized locations.
+- Avoid encoding culturally restricted knowledge in fixtures unless required and approved.
+
+### AI usage constraints
+
+- If AI is used to draft fixtures, the output must be reviewed and must not contain hallucinated sources or sensitive locations.
+
+## 🕰️ Version History
+
+| Version | Date | Summary | Author |
+|---|---|---|---|
+| v1.0.0 | 2025-12-22 | Initial graph fixtures README | TBD |
+
+---
+
+Footer refs:
+
+- Governance: `docs/governance/ROOT_GOVERNANCE.md`
+- Ethics: `docs/governance/ETHICS.md`
+- Sovereignty: `docs/governance/SOVEREIGNTY.md`
diff --git a/.github/actions/fixtures/graph/valid/README.md b/.github/actions/fixtures/graph/valid/README.md
new file mode 100644
index 0000000..1111111
--- /dev/null
+++ b/.github/actions/fixtures/graph/valid/README.md
@@ -0,0 +1,318 @@
+---
+title: "KFM Valid Graph Fixtures"
+path: ".github/actions/fixtures/graph/valid/README.md"
+version: "v1.0.0"
+last_updated: "2025-12-22"
+status: "draft"
+doc_kind: "Guide"
+license: "CC-BY-4.0"
+
+markdown_protocol_version: "KFM-MDP v11.2.6"
+mcp_version: "MCP-DL v6.3"
+ontology_protocol_version: "KFM-ONTO v4.1.0"
+pipeline_contract_version: "KFM-PPC v11.0.0"
+stac_profile: "KFM-STAC v11.0.0"
+dcat_profile: "KFM-DCAT v11.0.0"
+prov_profile: "KFM-PROV v11.0.0"
+
+governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
+ethics_ref: "docs/governance/ETHICS.md"
+sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
+fair_category: "FAIR+CARE"
+care_label: "TBD"
+sensitivity: "public"
+classification: "open"
+jurisdiction: "US-KS"
+
+doc_uuid: "urn:kfm:doc:github:actions:fixtures:graph:valid:readme:v1.0.0"
+semantic_document_id: "kfm-github-actions-fixtures-graph-valid-readme-v1.0.0"
+event_source_id: "ledger:kfm:doc:github:actions:fixtures:graph:valid:readme:v1.0.0"
+commit_sha: "<latest-commit-hash>"
+
+ai_transform_permissions:
+  - "summarize"
+  - "structure_extract"
+  - "translate"
+  - "keyword_index"
+ai_transform_prohibited:
+  - "generate_policy"
+  - "infer_sensitive_locations"
+
+doc_integrity_checksum: "sha256:<calculate-and-fill>"
+---
+
+# .github/actions/fixtures/graph/valid — Fixtures That Must Pass
+
+## 📘 Overview
+
+### Purpose
+
+This folder holds **positive (passing) graph fixture bundles**. Each fixture case:
+
+- represents a minimal graph scenario,
+- conforms to the ontology/constraint expectations enforced by the graph toolchain,
+- is expected to pass validation/import in CI.
+
+These fixtures are designed to catch regressions in graph ingest tooling and ontology enforcement.
+
+### Scope
+
+In scope:
+
+- Minimal “happy path” fixtures for:
+  - allowed labels/relationship types,
+  - required properties (IDs, provenance references, etc.),
+  - import/validation mechanics.
+
+Out of scope:
+
+- Negative cases (use `../invalid/` if present)
+- Any fixture that depends on external network access
+- Any fixture encoding sensitive locations, personal data, or culturally restricted knowledge without explicit review and redaction/generalization
+
+### Audience
+
+- Graph/ontology maintainers
+- CI workflow maintainers
+- Contributors adding new validation coverage
+
+### Definitions (link to glossary)
+
+- `docs/glossary.md` (recommended)
+- **Fixture case**: a subfolder under `valid/` representing one scenario
+
+### Key artifacts (what this doc points to)
+
+- `case-<slug>/` folders (one per fixture scenario)
+- per-case `README.md` explaining:
+  - scenario intent,
+  - expected validation behavior,
+  - how the files map to the graph import format.
+
+### Definition of done (for this document)
+
+- [ ] Documents how to add a valid fixture case
+- [ ] Provides a checklist for fixture quality and safety
+- [ ] Defines expected per-case structure (README + manifest + graph files)
+
+## 🗂️ Directory Layout
+
+### This document
+
+- **path:** `.github/actions/fixtures/graph/valid/README.md`
+
+### Related repository paths
+
+| Area | Canonical path | Notes |
+|---|---|---|
+| Fixture root | `.github/actions/fixtures/graph/` | Parent README defines overall rules |
+| Graph subsystem | `src/graph/` | Ontology and constraints |
+| Graph import outputs | `data/graph/` | Canonical import artifacts (for reference) |
+| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | IDs a fixture may reference |
+
+### Expected file tree for this sub-area
+
+~~~text
+📁 .github/actions/fixtures/graph/valid/
+├── 📄 README.md
+└── 📁 case-<slug>/
+    ├── 📄 README.md
+    ├── 📄 fixture.manifest.json
+    └── 📁 graph/
+        ├── 📄 <nodes>.<ext>
+        ├── 📄 <edges>.<ext>
+        └── 📄 <constraints_or_import>.<ext>
+~~~
+
+## 🧭 Context
+
+### Background
+
+Valid fixtures are “known good” reference graphs used in CI to ensure:
+
+- ontology constraints are enforced consistently,
+- import/validation tooling remains compatible,
+- changes to graph rules don’t silently break expected behavior.
+
+### Assumptions
+
+- Fixtures are small, synthetic, and deterministic.
+- Fixture structure matches what the graph validation action expects.
+
+### Constraints / invariants
+
+- **Stable IDs:** use stable, deterministic identifiers (prefer URN-like IDs when possible).
+- **Minimality:** include only what the test needs.
+- **Safety:** no secrets/PII; avoid encoding restricted locations or culturally sensitive knowledge.
+- **Diff-friendly:** predictable ordering; avoid autogenerated timestamps unless required.
+
+### Open questions
+
+- Should all valid cases include explicit STAC/DCAT/PROV reference fields (even if stubbed), or only the ones testing linkage?
+
+### Future extensions
+
+- Add “golden” expected validation reports for each case (if the validator supports it)
+- Add a standard JSON Schema for `fixture.manifest.json`
+
+## 🗺️ Diagrams
+
+### System / dataflow diagram
+
+~~~mermaid
+flowchart LR
+  A[Valid fixture case] --> B[CI graph validation action]
+  B --> C[Expected: PASS]
+~~~
+
+### Optional: sequence diagram
+
+~~~mermaid
+sequenceDiagram
+  participant CI as CI Workflow
+  participant ACT as Graph Validation Action
+  participant CASE as Fixture Case
+
+  CI->>ACT: Select case-<slug>
+  ACT->>CASE: Load graph files
+  ACT->>ACT: Validate/import
+  ACT-->>CI: PASS + logs
+~~~
+
+## 📦 Data & Metadata
+
+### Inputs
+
+- Fixture case files (graph files + manifest + README)
+
+### Outputs
+
+- CI pass signal for the case
+- Optional: validator logs/artifacts
+
+### Sensitivity & redaction
+
+- Keep cases synthetic.
+- If referencing real places/events is unavoidable, generalize and ensure approvals per governance refs.
+
+### Quality signals
+
+- Case README explains intent and expected behavior in < 200 words
+- Manifest is present and minimal
+- Case can run in CI in seconds (not minutes)
+
+## 🌐 STAC, DCAT & PROV Alignment
+
+### STAC
+
+- If a case references STAC items, document the expected ID format and how it should be resolved.
+
+### DCAT
+
+- If a case references a dataset ID, ensure it is stable and clearly synthetic unless derived from in-repo catalogs.
+
+### PROV-O
+
+- If a case includes provenance fields, document the expected relationships and identifiers.
+
+### Versioning
+
+- If the case models lineage/versioning, ensure relationships are consistent within the case.
+
+## 🧱 Architecture
+
+### Components
+
+- Fixture case bundle (producer)
+- Graph validation/import action (consumer)
+- CI workflow orchestration
+
+### Interfaces / contracts
+
+- The fixture case must satisfy the action’s expected file naming/format contract.
+
+If the contract is changed, update:
+
+- existing cases,
+- case READMEs/manifests,
+- and the action documentation.
+
+### Extension points checklist (for future work)
+
+- [ ] Add more “happy path” cases for new ontology elements
+- [ ] Add coverage for provenance-linking fields
+- [ ] Add per-case expected output snapshots (if supported)
+
+## 🧠 Story Node & Focus Mode Integration
+
+### How this work surfaces in Focus Mode
+
+Indirect: passing graph fixtures help ensure entity IDs and relationships used by Story Nodes remain stable.
+
+### Provenance-linked narrative rule
+
+- Do not include publishable narrative content in fixtures.
+
+### Optional structured controls
+
+~~~yaml
+# Optional: per-case tags, if the action supports them.
+case_tags:
+  - "valid"
+  - "minimal"
+~~~
+
+## 🧪 Validation & CI/CD
+
+### Validation steps
+
+For any new `case-<slug>/`:
+
+- [ ] Small, deterministic, synthetic
+- [ ] No secrets/PII/sensitive locations
+- [ ] Case README included (intent + expected result)
+- [ ] Fixture passes graph validation/import in CI
+
+### Reproduction
+
+~~~bash
+# Example placeholders — replace with repo-specific commands
+# 1) run graph validation locally against a case
+# 2) run unit tests covering fixture enumeration
+~~~
+
+### Telemetry signals (if applicable)
+
+| Signal | Source | Where recorded |
+|---|---|---|
+| Case pass/fail | CI workflow | Logs |
+| Duration | CI workflow | Logs |
+
+## ⚖ FAIR+CARE & Governance
+
+### Review gates
+
+- Any fixture that encodes real-world sensitive content requires governance review.
+
+### CARE / sovereignty considerations
+
+- Use synthetic data by default.
+- Do not encode culturally restricted knowledge in fixtures unless required and approved.
+
+### AI usage constraints
+
+- AI-assisted fixture drafting must be reviewed and must not introduce hallucinated sources or sensitive details.
+
+## 🕰️ Version History
+
+| Version | Date | Summary | Author |
+|---|---|---|---|
+| v1.0.0 | 2025-12-22 | Initial valid graph fixtures README | TBD |
+
+---
+
+Footer refs:
+
+- Governance: `docs/governance/ROOT_GOVERNANCE.md`
+- Ethics: `docs/governance/ETHICS.md`
+- Sovereignty: `docs/governance/SOVEREIGNTY.md`
