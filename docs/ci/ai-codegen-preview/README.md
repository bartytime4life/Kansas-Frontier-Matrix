---
title: "🤖 KFM — AI Codegen PRs with Deterministic Preview Builds & Provenance Gates"
path: "docs/ci/ai-codegen-preview/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Councils"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Reference Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "ai-codegen-prs-deterministic-preview-provenance-policy-gates"
audience:
  - "Reliability Engineering"
  - "Data Engineering"
  - "Security / Supply Chain"
  - "Catalog + Provenance Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (no secrets; provenance-safe)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Reliability Council · FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:ci:aicodegen:preview:v11.2.6"
semantic_document_id: "kfm-ci-ai-codegen-preview"
event_source_id: "ledger:docs/ci/ai-codegen-preview"
immutability_status: "version-pinned"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../releases/v11.2.6/ci-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/ci-v11.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../security/supply-chain/README.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "layout-normalization"
  - "diagram-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "fabricating provenance or approvals"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🤖 **KFM — AI Codegen PRs with Deterministic Preview Builds & Provenance Gates**
`docs/ci/ai-codegen-preview/README.md`

**Purpose**  
Define a governed pattern where an AI codegen agent proposes changes, produces a **deterministic preview build**,
emits **machine-verifiable provenance + QA artifacts**, and opens a **policy-gated PR**. KFM merges only when
lineage, QA, security, and governance attestations pass.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Deterministic-Builds-brightgreen" />
<img src="https://img.shields.io/badge/Provenance-OpenLineage%20%2B%20PROV--O-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This pattern creates a deterministic, auditable path from **AI-generated changes** to a **reviewable PR**:

- **Agent** proposes a patch bundle (seeded, logged, prompt-safe).
- **Preview build** runs in an ephemeral environment and is **bit-for-bit reproducible** (policy requirement).
- **QA** validates code + data contracts (tests + Great Expectations + schema checks).
- **Provenance** is emitted as **OpenLineage** and **PROV-O JSON-LD**, plus **SBOM** and **SLSA** attestations.
- **Policy gates** (OPA/Rego + KFM-PDC v11) block merge until all requirements pass.

**Why KFM cares**

- Reproducibility (deterministic builds)
- Accountability (OpenLineage + PROV-O)
- Safety & ethics (FAIR+CARE + sovereignty gates)
- Supply-chain integrity (SBOM + SLSA + signatures)

---

## 🗂 Directory Layout

~~~text
📁 docs/
└── 📁 ci/
    └── 📁 ai-codegen-preview/
        └── 📄 README.md                               — This reference

📁 .github/
└── 📁 workflows/
    ├── 🧾 ai_codegen_propose.yml                      — Agent run → patch bundle → PR
    ├── 🧾 ai_codegen_preview_build.yml                — Deterministic preview build (Earthly/Dagger)
    ├── 🧾 ai_codegen_qc.yml                           — Tests, lint, GE checks, telemetry
    ├── 🧾 ai_codegen_provenance.yml                   — OpenLineage + PROV-O + attestations
    └── 🧾 ai_codegen_policy_gate.yml                  — OPA gate + required PR checks

📁 schemas/
├── 📁 telemetry/
│   └── 🧾 ci-v11.json                                 — CI telemetry schema (energy, CO2e, budgets)
├── 📁 prov/
│   └── 🧾 kfm-prov-v11.json                            — PROV-O validation schema
└── 📁 lineage/
    └── 🧾 openlineage-v1.json                          — OpenLineage event schema

📁 policies/
├── 📁 opa/
│   └── 🧾 ai-codegen.rego                              — Merge gate policy
└── 📁 ge/
    └── 🧾 expectations-suite.yml                       — Data-quality expectations suite

📁 scripts/
├── 📁 agent/
│   └── 🐍 main.py                                      — Seeded agent runner (writes patch + log)
├── 📁 lineage/
│   ├── 🐍 emit_openlineage.py                          — OpenLineage event emitter
│   └── 🐍 write_prov.py                                — PROV-O bundle writer
└── 📁 supplychain/
    ├── 🧾 sbom.sh                                      — SBOM generator
    ├── 🧾 slsa_attest.sh                               — SLSA attestation generator
    └── 🧾 supplychain_verify.sh                        — Verification gate
~~~

---

## 🧭 Context

### Problem

AI codegen can increase velocity but also increases risk:

- non-deterministic builds,
- missing or incomplete provenance,
- accidental interface drift,
- supply-chain ambiguity,
- governance bypass via “small-looking” changes.

### Non-goals

- This pattern does **not** auto-merge PRs.
- This pattern does **not** waive human review for governed areas.
- This pattern does **not** permit publishing secrets, restricted knowledge, or sensitive locations.

### Core constraints (governed)

- Determinism: pinned toolchains, pinned base images, locked dependencies, stable locale/TZ, explicit seeds.
- Provenance completeness: every run produces machine-verifiable lineage artifacts.
- Policy enforcement: merge is blocked unless all checks pass (override requires signed justification).

---

## 🧱 Architecture

### Components

#### Agent (codegen proposer)

Responsibilities:

- generate patch bundle deterministically (seeded; stable toolchain),
- write an agent log capturing:
  - seed and config hash,
  - tool versions,
  - prompt reference (prompt content must be provenance-safe),
  - changed files list and diff hash.

Rules:

- prompts and intermediate artifacts MUST NOT contain secrets or PII,
- agent output is a proposal only, never a direct merge.

#### Builder (deterministic preview)

Responsibilities:

- build artifacts in an ephemeral runner with deterministic settings:
  - pinned base images,
  - locked deps (hash-pinned),
  - stable environment (locale, TZ, file ordering),
  - reproducible packaging settings.
- emit checksum manifest for produced artifacts.

Recommended engines:

- Earthly targets for reproducible builds,
- Dagger pipelines for ephemeral, portable execution graphs.

#### QA (code + data contract checks)

Responsibilities:

- unit/integration tests,
- lint and formatting checks,
- data contract validation (KFM-PDC v11),
- Great Expectations (GE) suite execution (when data artifacts exist),
- drift checks and PII scans for data outputs.

#### Provenance (OpenLineage + PROV-O + attestations)

Responsibilities:

- emit OpenLineage events keyed by:
  - commit SHA, PR id, workflow run id,
- write PROV-O JSON-LD bundle:
  - `prov:Activity` for agent, build, QA, gate,
  - `prov:Entity` for patch, artifacts, manifests, reports,
  - `prov:Agent` for AI agent and human reviewers (as applicable),
- generate SBOM and SLSA attestation for the artifact set,
- sign bundle where required (policy).

#### Policy gate (OPA/Rego + contract checks)

Responsibilities:

- evaluate merge eligibility based on:
  - provenance completeness,
  - QA pass/fail,
  - security posture (SBOM + SLSA),
  - FAIR+CARE and sovereignty gates,
  - energy/carbon thresholds and reliability budgets (if enforced).

#### PR surfacing (GitHub)

Responsibilities:

- open PR with:
  - patch bundle,
  - links/references to preview artifacts,
  - provenance and QA summaries,
  - explicit semver recommendation when interfaces change.

---

## 🗺 Diagrams

~~~mermaid
flowchart TD
  A["Trigger: workflow_dispatch or scheduler"] --> B["Agent proposes patch bundle"]
  B --> C["Open PR with proposal branch"]
  C --> D["Deterministic preview build"]
  D --> E["QA: tests, lint, contracts, GE"]
  E --> F["Emit provenance: OpenLineage + PROV-O"]
  F --> G["Supply chain: SBOM + SLSA + signature"]
  G --> H["OPA policy gate evaluates context"]
  H --> I["Merge allowed only if all gates pass"]
~~~

---

## 📦 Data & Metadata

### Required artifacts (minimum set)

Each PR run SHOULD produce:

- `patch.diff` (or commit set) + hash
- preview build artifact bundle + checksum manifest
- QA reports (tests, GE, schema validation)
- telemetry bundle (energy, CO2e, reliability budget)
- provenance bundle (OpenLineage + PROV-O JSON-LD)
- supply-chain bundle (SBOM + SLSA attestation + verification report)

### Example PR comment payload (truncated)

~~~json
{
  "kfm_pr_id": 2134,
  "preview": {
    "artifact_manifest_sha256": "sha256:…",
    "earthly_target": "+preview",
    "dagger_digest": "sha256:…"
  },
  "provenance": {
    "openlineage_run_id": "urn:uuid:…",
    "prov_jsonld_ref": "artifacts/prov/run-2134.jsonld",
    "slsa_attestation_ref": "artifacts/attestations/slsa.json",
    "sbom_ref": "releases/v11.2.6/sbom.spdx.json"
  },
  "qa": {
    "ge_report": "reports/ge/pr-2134.json",
    "tests_passed": true,
    "coverage": 0.87
  },
  "telemetry": {
    "energy_kwh": 0.42,
    "co2e_kg": 0.18,
    "reliability_budget": "within"
  },
  "policy_gate": {
    "opa_decision": "allow",
    "reasons": ["contracts_ok", "prov_ok", "slsa_ok", "ge_ok"]
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT preview outputs (when applicable)

If the AI proposal affects ETL/catalog code or data products, the preview build SHOULD produce:

- preview STAC Items/Collections under a sandbox output path,
- preview DCAT dataset/distributions,
- validation reports (PySTAC / stac-validator / SHACL).

These preview catalogs are treated as ephemeral evidence artifacts for the PR.

### OpenLineage and PROV-O requirements

- OpenLineage events SHOULD be emitted per workflow stage (agent, build, QA, gate).
- PROV-O bundle MUST include:
  - `prov:Activity` for each stage,
  - `prov:Entity` for patch, artifacts, reports, and manifests,
  - `prov:wasDerivedFrom` linking preview outputs to source inputs and the proposal commit,
  - `prov:used` linking activities to configs, policies, and schemas.

---

## 🧪 Validation & CI/CD

### Policy gates (merge only if all pass)

- **Contract**: KFM-PDC v11 conformance (schemas, interfaces, graph contracts where applicable).
- **Data quality**: GE suites green; drift and PII checks pass (if data artifacts exist).
- **Security**: SBOM license/CVE policy; Sig verification; SLSA level meets minimum.
- **Lineage**: OpenLineage complete; PROV-O validates against `schemas/prov/kfm-prov-v11.json`.
- **Ethics**: FAIR+CARE flags respected; sovereignty controls enforced; no restricted outputs.
- **Ops**: telemetry thresholds honored; reliability budget not violated (when enforced).

### Minimal GitHub Actions scaffold (snippets)

#### `.github/workflows/ai_codegen_propose.yml`

~~~yaml
name: "🤖 AI Codegen — Propose"
on:
  workflow_dispatch:

jobs:
  propose:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run agent (seeded)
        run: |
          python scripts/agent/main.py --seed 1337 --out patch.diff --log agent.json

      - name: Create PR (gh cli)
        run: |
          git apply patch.diff
          git checkout -b ai/proposal/${{ github.run_id }}
          git commit -am "AI proposal: ${{ github.run_id }}"
          git push -u origin ai/proposal/${{ github.run_id }}
          gh pr create \
            --title "AI Proposal ${{ github.run_id }}" \
            --body-file docs/ci/ai-codegen-preview/PR_TEMPLATE.md
~~~

#### `.github/workflows/ai_codegen_preview_build.yml`

~~~yaml
name: "🧪 AI Codegen — Preview Build"
on:
  pull_request:
    paths-ignore:
      - "docs/**"

jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deterministic preview build (Earthly/Dagger)
        run: |
          earthly --allow-privileged +preview

      - name: Generate SBOM and artifact manifest
        run: |
          ./scripts/supplychain/sbom.sh > releases/v11.2.6/sbom.spdx.json
          ./scripts/supplychain/manifest.sh artifacts/ > releases/v11.2.6/manifest.zip
~~~

#### `.github/workflows/ai_codegen_provenance.yml`

~~~yaml
name: "📜 AI Codegen — Provenance"
on:
  workflow_run:
    workflows: ["🧪 AI Codegen — Preview Build"]
    types: [completed]

jobs:
  lineage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Emit OpenLineage
        run: python scripts/lineage/emit_openlineage.py

      - name: Write PROV-O JSON-LD
        run: python scripts/lineage/write_prov.py --out artifacts/prov/run.jsonld

      - name: SLSA attestation
        run: ./scripts/supplychain/slsa_attest.sh artifacts/ > artifacts/attestations/slsa.json
~~~

#### `.github/workflows/ai_codegen_policy_gate.yml`

~~~yaml
name: "🚦 AI Codegen — Policy Gate"
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate PROV-O
        run: ajv -s schemas/prov/kfm-prov-v11.json -d artifacts/prov/run.jsonld

      - name: OPA policy decision
        run: opa eval --format=json -I -d policies/opa -i artifacts/context.json "data.kfm.allow"

      - name: Great Expectations (data quality)
        run: great_expectations checkpoint run ge/ci.yml

      - name: Supply-chain verification
        run: ./scripts/supplychain/supplychain_verify.sh releases/v11.2.6/sbom.spdx.json artifacts/attestations/slsa.json
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes

This pattern supports Story Nodes by attaching reviewable evidence artifacts:

- patch bundle and diff summary,
- preview build artifacts and checksums,
- STAC/DCAT previews (when relevant),
- provenance bundles (OpenLineage + PROV-O),
- QA and policy gate results.

Story Nodes SHOULD clearly distinguish:

- **fact**: what changed and what checks passed/failed,
- **interpretation**: impact assessment and risk narrative,
- **policy**: required approvals and any restricted-scope constraints.

### Focus Mode constraints

Focus Mode MAY summarize outcomes and link artifacts, but MUST NOT:

- claim approvals occurred,
- invent provenance or policy decisions,
- infer sensitive information not present in artifacts.

---

## ⚖ FAIR+CARE & Governance

### Governance posture (mandatory)

- AI codegen runs MUST produce PRs; they MUST NOT auto-merge governed changes.
- Any change that affects:
  - rights/licensing,
  - sovereignty labels,
  - sensitivity classification,
  - provenance requirements,
  - public-facing catalogs,
  MUST trigger escalation to stewardship review.

### Override path (restricted)

If an override is permitted by policy, it MUST be accompanied by:

- a signed justification artifact,
- an explicit scope statement,
- a provenance-preserving audit trail.

### Safety constraints

- Do not store secrets in prompts, logs, or PR artifacts.
- Do not emit restricted locations or sensitive knowledge through preview catalogs or PR comments.
- Apply sovereignty gates consistently (block on conflict; require manual review).

---

## 🕰 Version History

| Version | Date       | Notes |
|-------:|------------|------|
| v11.2.6 | 2025-12-13 | Initial governed pattern for AI codegen PRs with deterministic preview builds and provenance/policy gates. |

---

<div align="center">

🤖 **KFM — AI Codegen PRs with Deterministic Preview Builds & Provenance Gates**  
Deterministic Builds · Verifiable Lineage · Policy-Gated Merges

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[↩ Back to Index](../../README.md) ·
[📚 Data Architecture](../../architecture/README.md) ·
[🛡️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🔐 Supply-Chain Security](../../security/supply-chain/README.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
