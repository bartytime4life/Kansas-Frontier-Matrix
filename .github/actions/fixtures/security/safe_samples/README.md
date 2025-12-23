---
title: "Security Fixtures — Safe Samples"
path: ".github/actions/fixtures/security/safe_samples/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
status: "active"
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

doc_uuid: "urn:kfm:doc:fixtures:security:safe-samples:readme:v1.0.0"
semantic_document_id: "kfm-fixtures-security-safe-samples-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:fixtures:security:safe-samples:readme:v1.0.0"
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

# Security Fixtures — Safe Samples

## 📘 Overview

### Purpose

This directory contains **intentionally safe, non-sensitive fixture files** used by security-related CI checks and GitHub Actions.
These samples exist to test workflows and scanners **without** storing secrets, personal data, or restricted location information in the repository.

### Scope

| In Scope | Out of Scope |
|---|---|
| Synthetic, non-sensitive fixture files for CI/security tests | Real credentials, private keys, tokens, passwords, session cookies |
| Public, shareable examples (placeholders, redacted configs) | Any PII (names/emails tied to real people), private datasets, copyrighted source dumps |
| Small text-based samples that should pass scanners | Strings that intentionally trigger secret scanners (place those elsewhere) |

### Audience

- Primary: CI / DevOps maintainers, security reviewers
- Secondary: Contributors adding or updating fixtures used by tests

### Definitions

- **Fixture:** A file checked into the repo to support deterministic tests.
- **Safe sample:** A fixture that is *safe to publish* and should *not* be flagged as a secret or sensitive content by scanners.
- **Security gate:** A CI job that enforces security rules (secret scanning, linting, policy checks).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `.github/actions/fixtures/security/safe_samples/README.md` | TBD | Conventions + constraints |
| Safe fixture files | `.github/actions/fixtures/security/safe_samples/**` | TBD | Must remain public-safe |
| Security checks consuming fixtures | CI / GitHub Actions | TBD | Must not require real secrets |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] No secrets, private keys, credentials, or PII present in any fixture
- [ ] Fixtures are deterministic, minimal, and text-based where possible
- [ ] Security/secret scanners pass on the fixtures directory
- [ ] Any new sample is documented (add/update the “What belongs here” section)

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/security/safe_samples/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/actions/` | Local actions and their supporting fixtures |
| Security fixtures | `.github/actions/fixtures/security/` | Security-related test inputs |
| Workflows | `.github/workflows/` | CI workflows that may reference fixtures |
| Security governance | `docs/governance/` | Governance, ethics, sovereignty references |

### Suggested fixture tree

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 security/
            └── 📁 safe_samples/
                ├── 📄 README.md
                └── 📁 <add_safe_fixture_files_here>/
~~~

## 🧭 Context

### Security + sensitivity

Treat everything in this directory as **public**:
- Do **not** include real API keys, passwords, tokens, certificates, private keys, or any credential material.
- Avoid including strings that match well-known secret formats, even if “fake”.
  - Example: use placeholders like `YOUR_API_KEY_HERE`, `REPLACE_ME`, `<TOKEN>` instead of realistic-looking token strings.
- Do **not** include sensitive location coordinates or “restricted site” examples; keep any location-like examples generalized and synthetic.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Safe fixture files] --> B[Security CI job / scanner]
  B --> C[Pass: no findings]
  B --> D[Fail: unexpected findings]
  D --> E[Fix fixture content or scanner rule]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Safe fixture files | text/yaml/json/etc. | This directory | Must not match secret patterns; must be public-safe |
| Scanner configuration | repo-specific | CI / Action config | Must be deterministic |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Scan results | logs / SARIF / exit code | CI logs / artifacts | CI gate rules |

### Sensitivity & redaction

- **Required:** Fixtures must already be safe; do not rely on redaction after the fact.
- If you need an example of a sensitive field, use **obvious placeholders** (`<REDACTED>`, `REPLACE_ME`) rather than realistic token formats.

### Quality signals

- Fixtures are:
  - minimal (small file size, short content)
  - deterministic (no timestamps/random data unless explicitly fixed)
  - scanner-safe (should not trigger secret scanners or policy gates)

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Not applicable: fixtures are not geospatial catalog artifacts.

### DCAT

- Not applicable: fixtures are not published datasets.

### PROV-O

- Not applicable: fixtures are not pipeline outputs; they support CI validation only.

### Versioning

- Fixtures may change as tests evolve; keep changes small and document intent in PR descriptions.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Fixtures | Provide deterministic, safe test inputs | File paths under `safe_samples/` |
| CI workflow / action | Executes scanners and checks | GitHub Actions runner |
| Scanner / rules | Detect forbidden patterns and policy violations | Config + CLI invocation |

### Interfaces and contracts

- **Path contract:** Workflows/tests should reference fixtures by stable relative path.
- **Content contract:** Content must remain public-safe and should not intentionally trip secret scanning.
- **Naming contract:** Prefer descriptive names that communicate purpose, e.g.:
  - `config_placeholder.yaml`
  - `example_env_template.env.example`
  - `sanitized_policy_input.json`

### Extension points checklist

- [ ] Add fixture file(s) under `safe_samples/`
- [ ] Ensure content is synthetic and does not resemble real secrets
- [ ] Update this README if new categories are added
- [ ] Verify CI/security checks pass

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Not applicable: these fixtures are CI artifacts only.

### Provenance-linked narrative rule

- Not applicable.

### Optional structured controls

- Not applicable.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (if enforced for `.github/**`)
- [ ] Secret scanning / credential detection passes
- [ ] Repo policy checks pass (no PII, no restricted location leakage)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run markdown/doc lint if configured
# 2) run secret scanning / security lint locally if supported
# 3) run the action/test suite that consumes these fixtures
~~~

### Telemetry signals

- Not applicable unless your CI system records fixture coverage or scanner metrics.

## ⚖ FAIR+CARE & Governance

### Review gates

- Any additions to this directory should be reviewed by:
  - CI maintainer, and
  - Security reviewer (recommended), especially if adding new sample categories.

### CARE and sovereignty considerations

- Keep fixture content synthetic and generalized.
- Do not include culturally sensitive knowledge or precise coordinates tied to restricted places.

### AI usage constraints

- This doc allows summarization/structure extraction/translation/indexing.
- Prohibited: generating new policy from this file; inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial safe sample fixture README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
