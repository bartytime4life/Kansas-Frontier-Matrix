---
title: "Security Tripwire Fixtures — GitHub Actions"
path: ".github/actions/fixtures/security/tripwires/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:security-tripwires-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-security-tripwires-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions-fixtures-security-tripwires-readme-v1.0.0"
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

# Security Tripwire Fixtures

This directory contains **synthetic, intentionally “bad” fixtures** used to verify that KFM’s CI **security** and **sovereignty** gates correctly detect and block unsafe patterns.

## 📘 Overview

### Purpose

- Provide a safe, documented home for **security “tripwire” test inputs** used by GitHub Actions.
- Prevent regressions: a tripwire fixture should **fail** the relevant gate deterministically.
- Ensure fixtures do not introduce real-world risk: **no real secrets, no real personal data, no real restricted locations**.

### Scope

| In scope | Out of scope |
|---|---|
| Fixtures stored under `.github/actions/fixtures/security/tripwires/` | Real credentials, keys, tokens, or access strings |
| Conventions for fixture naming, organization, and safety | Implementing scanners / policies (document those under `.github/SECURITY.md` and `docs/security/`) |
| How CI should consume fixtures for “expected fail” tests | Production security configuration or deployment hardening |

### Audience

- CI / GitHub Actions maintainers
- Security and governance maintainers
- Contributors adding or updating “security gate” checks

### Definitions

- **Security gate**: a CI check that blocks merges when security constraints are violated.
- **Sovereignty gate**: a CI check that blocks merges when CARE / sovereignty rules could be violated (for example, restricted location leakage).
- **Tripwire fixture**: a synthetic file designed to **trigger** a specific gate so we can prove the gate still works.
- **Fixture harness**: the workflow/job code that runs the gate against a fixture and asserts expected pass/fail.

See also: `docs/glossary.md` (if present).

### Key artifacts

| Artifact | Path | Role |
|---|---|---|
| This README | `.github/actions/fixtures/security/tripwires/README.md` | Conventions + safety rules |
| Security policy | `.github/SECURITY.md` | Policy-level requirements |
| Security standards | `docs/security/` | Technical standards and runbooks |
| Workflows | `.github/workflows/` | CI jobs that invoke security gates |
| Local actions | `.github/actions/` | Composite actions used by workflows |
| Fixtures root | `.github/actions/fixtures/` | Fixture data for action tests |

### Definition of done

- [ ] Each new tripwire fixture is **synthetic** and **safe to publish**.
- [ ] Each fixture maps to exactly one gate (or documents why it exercises multiple).
- [ ] A workflow/job asserts the expected outcome (typically **failure**) deterministically.
- [ ] No fixture is accidentally consumed by production code paths.
- [ ] Fixtures remain small, reviewable, and stable over time.

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/security/tripwires/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Local composite actions |
| Fixtures | `.github/actions/fixtures/` | Test inputs for actions |
| Security fixtures | `.github/actions/fixtures/security/` | Security-related fixtures (pass and fail) |
| Tripwire fixtures | `.github/actions/fixtures/security/tripwires/` | Fixtures expected to trigger gates |
| CI workflows | `.github/workflows/` | Invocation and assertions |
| Security policy and standards | `.github/SECURITY.md`, `docs/security/` | Requirements and details |

### Expected file tree for this sub-area

~~~text
📁 .github
└── 📁 actions
    └── 📁 fixtures
        └── 📁 security
            └── 📁 tripwires
                ├── 📄 README.md
                ├── 📁 <gate-family-1>
                │   └── 📄 <synthetic-tripwire-files>
                └── 📁 <gate-family-2>
                    └── 📄 <synthetic-tripwire-files>
~~~

## 🧭 Context

### Background

KFM’s CI is expected to include **security and sovereignty scanning gates** as part of its minimum checks. Tripwire fixtures exist to keep those gates honest: if a gate stops catching what it should catch, the fixture-based test should fail loudly.

### Assumptions

- Workflows use local actions under `.github/actions/` to implement at least some checks.
- Tripwire fixtures are used only by CI tests, not by runtime code paths.
- If there is a repository-wide scanner, it should not treat these fixtures as production data (use allowlists/paths, or run fixture tests in a dedicated job).

### Constraints and invariants

- Tripwire fixtures must never contain real secrets or real sensitive information.
- Fixtures must not undermine architectural boundaries.
  - Example: do not add any production code path that reads fixtures.
- CI gate behavior should be deterministic: validate if present; fail if invalid; skip if not applicable.
- Architectural rule support: do not violate core boundaries such as “UI must not connect to Neo4j directly.”

### Open questions

| Question | Owner | Target |
|---|---|---|
| Which workflow(s) validate the security and sovereignty scanning gates? | TBD | TBD |
| Does the repository-wide security scan exclude `.github/actions/fixtures/**` by design? | TBD | TBD |
| Do we maintain a fixture manifest mapping each fixture to a gate/rule ID? | TBD | TBD |

### Future extensions

- Add a `manifest.json` or `manifest.yaml` per gate family enumerating:
  - fixture file(s)
  - expected result (pass/fail)
  - rule identifier(s)
  - workflow/job name(s) that assert the behavior

## 🗺️ Diagrams

### Fixture test flow

~~~mermaid
flowchart LR
  F["Tripwire Fixture<br/>.github/actions/fixtures/security/tripwires/**"] --> A["Security Gate Action<br/>.github/actions/**"]
  A --> W["GitHub Workflow Job<br/>.github/workflows/**"]
  W --> R["Expected Result<br/>fail (tripwire hit)"]
~~~

## 📦 Data & Metadata

### Inputs

- Small synthetic fixture files (text, JSON, YAML, etc.) designed to match a specific “bad pattern”.

### Outputs

- CI job status (expected: failure for tripwires)
- Logs/artifacts that show which rule fired (recommended)

### Sensitivity and redaction

- Treat all fixtures as **public** content:
  - Use fictional names, domains, and identifiers.
  - Never include actual coordinates for restricted sites.
  - Never include real credentials, tokens, keys, or access strings.

### Quality signals

- Fixtures are minimal (small files, few lines).
- Fixture naming makes intent obvious (gate family + what it should trigger).
- Tests assert the expected behavior deterministically (no flaky timing/network dependencies).

## 🌐 STAC, DCAT & PROV Alignment

Not applicable: this directory contains CI fixtures, not KFM datasets or evidence products. (Datasets and evidence products must follow the STAC/DCAT/PROV requirements described in the Master Guide and architecture docs.)

## 🧱 Architecture

### Components

| Component | Location | Responsibility |
|---|---|---|
| Tripwire fixtures | `.github/actions/fixtures/security/tripwires/` | Synthetic inputs for “expected fail” tests |
| Gate implementation | `.github/actions/` | Code that detects and blocks unsafe patterns |
| Test harness | `.github/workflows/` | Runs gate against fixtures and asserts outcomes |
| Policy and standards | `.github/SECURITY.md`, `docs/security/` | Defines what must be blocked and why |

### Next-evolution extension points

- Add new tripwire families as new security/sovereignty gates are added.
- If a gate requires structured inputs, document the schema and keep fixtures schema-valid when applicable.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

Not applicable: tripwire fixtures are CI-only and should never be ingested as Story Nodes.

### Focus Mode rule

Tripwire fixtures indirectly support Focus Mode by helping enforce repository-wide rules that prevent unsafe or unsourced content from reaching user-facing surfaces.

## 🧪 Validation & CI/CD

### Minimum CI gates for contributions touching this area

- Markdown protocol validation (for this README)
- Security and sovereignty scanning gate tests using these fixtures
- Repo lint checks relevant to `.github/**`

### Suggested validation steps for new fixtures

- [ ] Confirm the fixture is synthetic and contains no real sensitive information.
- [ ] Confirm the workflow/job asserts the expected outcome (tripwire hit).
- [ ] Confirm the fixture does not break repository-wide checks outside the intended fixture tests.

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- Adding a new gate that changes what is considered sensitive/blocked
- Adding fixtures that simulate sensitive content categories
- Any change that could affect public-facing behavior or security posture

### Sovereignty safety

- Do not include culturally restricted knowledge, sacred site details, or precise restricted geometries in fixtures.
- If a sovereignty gate must be tested, use generalized, synthetic examples.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for security tripwire fixtures | TBD |

---

Footer refs:

- `docs/MASTER_GUIDE_v12.md`
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- `.github/SECURITY.md`
- `docs/security/`

