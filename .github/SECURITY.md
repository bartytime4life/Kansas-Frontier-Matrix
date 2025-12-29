---
title: "KFM Security Policy"
path: ".github/SECURITY.md"
version: "v1.0.4"
last_updated: "2025-12-29"
status: "draft"
doc_kind: "Policy"
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

doc_uuid: "urn:kfm:doc:github:security-policy:v1.0.4"
semantic_document_id: "kfm-security-policy-v1.0.4"
event_source_id: "ledger:kfm:doc:github:security-policy:v1.0.4"
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

# KFM Security Policy

> **Purpose:** Provide a private, safe process for reporting security vulnerabilities and sensitive-content exposures affecting Kansas Frontier Matrix (KFM), and define how maintainers triage, remediate, and coordinate disclosure across the full KFM pipeline: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.

**Do not open public GitHub issues for security vulnerabilities or sensitive-content exposures.**  
Use a private channel as described under **Reporting a vulnerability**.

If you believe you have found **active exploitation**, **credential exposure**, **PII exposure**, or **restricted/sensitive location disclosure**, **stop immediately** and report privately:

- do not continue testing,
- do not retain or share the data,
- do not publish screenshots, coordinates, or logs that contain sensitive content.

---

## 🔐 Reporting quickstart

- Preferred: **GitHub Security Advisories** (private vulnerability report / draft advisory), if enabled.
- Alternate (if advisories are unavailable): **security contact email** (TBD — maintainers must publish).
- Optional encryption: **PGP key fingerprint** (TBD — maintainers must publish).
- If urgent: include **“URGENT / INCIDENT”** in the report title and state whether exploitation or sensitive-data leakage is suspected.

---

## 📘 Overview

### Purpose
This policy exists to:

- Provide a **private disclosure** path for vulnerabilities and sensitive-content exposure reports.
- Ensure fixes preserve KFM’s **contract-first** architecture and canonical ordering:
  - **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- Prevent harm from:
  - conventional software vulnerabilities (auth bypass, injection, XSS, SSRF, secrets leakage),
  - **data governance failures** (PII leaks, restricted location disclosure, culturally sensitive knowledge exposure),
  - supply-chain risk (malicious builds/artifacts, dependency compromise),
  - and narrative/AI safety failures (unsafe story rendering, prompt-injection pathways, inference-by-interaction leakage).

### Scope

| In scope | Out of scope |
|---|---|
| Vulnerabilities in repository code, workflows, configs, schemas, release artifacts, and documentation that impact confidentiality, integrity, or availability | General product questions / support requests |
| Exposure of sensitive or restricted content (PII, precise coordinates, culturally sensitive knowledge) through catalogs, APIs, UI, Story Nodes, or Focus Mode | Vulnerabilities in third-party services not operated by the project (unless triggered by repo misconfiguration) |
| Authn/authz, rate limiting, injection, SSRF, XSS, CSRF, secrets leakage, dependency/supply-chain risk | Social engineering, physical attacks, or issues requiring physical access |
| Security issues in story rendering or Focus Mode (unintended leakage, unsafe asset loading, narrative injection, prompt injection pathways) | Denial-of-service testing without explicit written permission |

### Audience
- Primary: security researchers, maintainers, contributors.
- Secondary: data stewards / governance reviewers, operators of deployments, downstream integrators.

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*

Key terms:

- **Vulnerability:** A weakness that can be exploited to compromise confidentiality, integrity, or availability.
- **Sensitive-content exposure:** Disclosure of content restricted by governance, including PII, culturally sensitive knowledge, and location-bearing data requiring generalization/redaction.
- **Security incident:** Confirmed exploitation or confirmed sensitive-content exposure requiring containment and notification steps.
- **Coordinated disclosure:** Private reporting and fix coordination before public disclosure.
- **Contract boundary:** A machine-validated interface (schema/spec) that producers/consumers must obey (schemas, API specs, UI registries).
- **Boundary artifacts:** Catalog/provenance outputs (STAC/DCAT/PROV) that form the contractual interface between pipeline stages.
- **Provenance bundle:** Lineage artifacts (PROV) that explain which inputs produced which outputs, when, and by which process/agent.

### Security principles
KFM treats security as **software + data + narrative**:

- **Fail closed:** if classification/sovereignty/sensitivity is unclear, treat as restricted until reviewed.
- **API boundary is mandatory:** UI must not access graph/datastores directly; all access is via contracted APIs.
- **Contracts are canonical:** schemas define structure; code must conform; CI validates.
- **Provenance is part of security:** a “fixed” codebase is insufficient if affected artifacts remain public.
- **Boundary artifacts are security surfaces:** STAC/DCAT/PROV outputs are publication interfaces and must be treated as security-relevant artifacts (no secrets, no signed URLs/tokens, no restricted coordinates in public outputs).

### Key artifacts (security-relevant)

| Artifact | Path / identifier | Primary owner | Notes |
|---|---|---|---|
| Security policy | `.github/SECURITY.md` | Maintainers | This document |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + invariants |
| Ingestion architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Maintainers | ETL + catalog-generation patterns *(see Data Intake Design doc)* |
| CI workflows | `.github/workflows/` | Maintainers | Security + contract enforcement gates |
| Schemas registry | `schemas/` | Maintainers | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) *(if present)* |
| Catalog “boundary artifacts” | `data/stac/collections/`, `data/stac/items/`, `data/catalog/dcat/`, `data/prov/` | Maintainers | Discovery + evidence + lineage; must not leak tokens or restricted coords |
| Graph layer | `src/graph/` (+ `data/graph/` if present) | Maintainers | Ontology + ingest artifacts |
| API boundary | `src/server/` | Maintainers | Auth + redaction/generalization enforcement; contracts under `src/server/contracts/**` *(if present)* |
| UI | `web/` | Maintainers | React/Map client; config validated; no direct graph access |
| Story Nodes | `docs/reports/story_nodes/` | Maintainers + reviewers | Narrative artifacts; provenance/citation requirements |
| Security runbooks | `docs/security/` | Maintainers | Threat model, incident response, supply chain integrity *(if present; recommended)* |
| Governance references | `docs/governance/*` | Governance reviewers | Sovereignty/Ethics/CARE constraints |

### Definition of done (for this document)
- [ ] Front-matter complete and `path` matches file location
- [ ] Reporting guidance is unambiguous: private first; no public exploit details
- [ ] Sensitive-content handling rules are explicit (PII + restricted locations + cultural knowledge)
- [ ] Architecture invariants stated: canonical pipeline ordering; API boundary; provenance rules
- [ ] CI/validation expectations are listed and repeatable (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “TBD / not confirmed in repo” placeholders reviewed and resolved by maintainers

---

## 🗂️ Directory layout

### This document
- `path`: `.github/SECURITY.md`

### Related repository paths (canonical targets)

| Area | Path | What lives here |
|---|---|---|
| GitHub governance & CI | `.github/` | Repo health + policy + workflows |
| CI workflows | `.github/workflows/` | CI gates for contracts, security scans, validation |
| Governance | `docs/governance/` | Ethics + sovereignty + approval workflow references |
| Templates | `docs/templates/` | Universal / Story Node / API Contract templates |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs *(if present)* |
| Schemas | `schemas/` | Contract validation schemas *(if present)* |
| Pipelines (ETL + catalogs) | `src/pipelines/` | Deterministic ETL + catalog builders |
| Catalog outputs (“boundary artifacts”) | `data/stac/collections/`, `data/stac/items/`, `data/catalog/dcat/`, `data/prov/` | Published discovery + evidence + lineage |
| Data lifecycle staging | `data/raw/`, `data/work/`, `data/processed/` | Raw inputs → intermediates → published datasets |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology + ingest artifacts |
| API boundary | `src/server/` | Contracted access; enforce redaction/authorization |
| UI | `web/` | React/Map client; config validated; no direct graph access |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts; provenance/citation requirements |
| Experiments / runs | `mcp/` | Runs, experiments, model cards, SOPs *(if present)* |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators, QA scripts |
| Releases | `releases/` | Versioned packaged artifacts *(if used)* |

### Repo drift note (security relevance)
Some KFM design docs note that **repo drift** can create security ambiguity (duplicate subsystem homes, missing canonical roots, Story Node location mismatch). If your repo exhibits drift:

- treat it as a governance + security risk (inconsistent gates, bypassable checks),
- prefer canonical subsystem homes (API under `src/server/`, UI under `web/`),
- ensure CI gates scan the true publication paths (catalog outputs, Story Nodes, UI bundles).

### Expected file tree (minimum)

~~~text
📁 .github/
├── 📄 SECURITY.md
└── 📁 workflows/
    └── 📄 *.yml

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📁 governance/
├── 📁 templates/
├── 📁 architecture/
└── 📁 reports/
    └── 📁 story_nodes/

📁 mcp/
├── 📁 runs/
└── 📁 experiments/

📁 schemas/
📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/

📁 tests/
📁 tools/
📁 web/
📁 releases/                      # if used
~~~

---

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system with a governed pipeline designed for auditability and harm reduction. The architecture is intentionally staged so that:

- deterministic transforms happen in ETL,
- discovery, evidence, and lineage are expressed through STAC/DCAT/PROV boundary artifacts,
- semantics are expressed in the graph,
- the API boundary enforces access control and redaction/generalization,
- the UI renders only what the API serves,
- Story Nodes and Focus Mode remain provenance-linked and governance-safe.

Security in KFM therefore includes:

- software security (code, dependencies, CI),
- data security (sensitivity classification, redaction/generalization),
- narrative safety (preventing leakage through storytelling and interaction),
- and AI safety (prompt injection pathways; provenance/uncertainty requirements).

### Core invariants (non-negotiable)

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**
- **No UI direct-to-graph reads:** UI must never bypass the API to query the graph directly.
- **Boundary artifacts first:** STAC/DCAT/PROV outputs are required before publishing to the graph, APIs, UI, or narratives.
- **Contracts are canonical:** schemas/specs define structure; code must conform; CI validates.
- **No unsourced narrative in published stories:** factual claims must be supported by evidence and pass validation.
- **Governance uncertainty fails closed:** treat as restricted until reviewed.
- **Classification does not downgrade through lineage:** no output is less restricted than any input in its provenance chain.

### Threat model snapshot (categories)

- Supply chain compromise: malicious dependency update, compromised CI signing, artifact replacement.
- Data poisoning and malicious inputs: hostile upstream files, crafted geospatial assets, malformed metadata.
- Unauthorized access: weak authn/authz, RBAC gaps, leaked credentials, insecure defaults.
- Injection and web vulnerabilities: query injection, XSS/CSRF, SSRF, unsafe deserialization.
- Sensitive-content leakage: precise coordinates, metadata re-identification, inference-by-interaction.
- Integrity loss: tampering with catalogs, provenance, or story evidence.
- Prompt injection: untrusted narrative/data causing unsafe tool calls or data exfiltration via AI systems.

### Roles (recommended)

- Maintainers: technical triage, patching, releases.
- Governance reviewers: sensitivity/sovereignty decisions; approval for disclosures involving restricted impacts.
- Incident lead: coordinates containment and communications *(role assignment TBD)*.

---

## 🗺️ Diagrams

### Coordinated disclosure workflow

~~~mermaid
flowchart LR
  R[Reporter] --> C["Private reporting channel<br/>(Security Advisory / email)"]
  C --> T["Triage + reproduce"]
  T --> S["Severity + sensitivity classification<br/>(incl. governance)"]
  S --> M["Mitigation / containment<br/>(rotate secrets, restrict surface)"]
  M --> F["Fix + tests + contract validation"]
  F --> P["Patch release + artifact rebuilds"]
  P --> A["Advisory + coordinated disclosure"]
~~~

### Canonical pipeline and security enforcement points

~~~mermaid
flowchart LR
  subgraph Data
    A["Raw sources<br/>data/raw/**"] --> B["ETL + normalization<br/>src/pipelines/**"]
    B --> C["STAC Items + Collections<br/>data/stac/items/** + data/stac/collections/**"]
    C --> D["DCAT dataset views<br/>data/catalog/dcat/**"]
    C --> E["PROV lineage bundles<br/>data/prov/**"]
  end

  C --> G["Neo4j graph<br/>src/graph/**"]
  G --> H["API boundary (contracts + redaction)<br/>src/server/**"]
  H --> I["React/Map UI<br/>web/**"]
  I --> J["Story Nodes<br/>docs/reports/story_nodes/**"]
  J --> K["Focus Mode<br/>provenance-linked only"]

  CI["CI gates<br/>.github/workflows/**"] -. validates .-> B
  CI -. validates .-> C
  CI -. validates .-> D
  CI -. validates .-> E
  CI -. validates .-> G
  CI -. validates .-> H
  CI -. validates .-> I
  CI -. validates .-> J
~~~

---

## 📌 Supported versions

KFM support policy can vary by release cadence. Until maintainers define it explicitly:

- **Supported (recommended default):**
  - default branch (`main`)
  - most recent tagged release *(TBD — confirm release strategy)*
- **Best effort:** older tags/snapshots may receive guidance but not patches.
- **Unsupported:** unmaintained forks or historical snapshots unless explicitly noted.

Important:

- Security guidance applies to **code and published artifacts** (catalogs, Story Nodes, derived datasets).
- If an artifact is vulnerable or exposes restricted data, remediation requires **artifact rebuilds and replacement**, not only a code fix.

---

## 🚨 Reporting a vulnerability

**Please do not open a public GitHub issue** for security-sensitive reports.

### Preferred reporting path
1. Use the repository’s **Security Advisories** workflow (private report / draft advisory), if enabled.
2. If advisories are not available, create a minimal public issue **only to request a private channel**, and **do not** include exploit details, sensitive data, or a PoC.

### Alternate reporting paths
Use only if advisories are unavailable:

- Email: **TBD — add project security contact**
- Encryption: **TBD — publish PGP key fingerprint**

### Urgent incidents
If you suspect **active exploitation** or **sensitive-content leakage**:

- Include **“URGENT / INCIDENT”** in the subject/title.
- State clearly whether any of the following occurred or is likely:
  - credential/secrets exposure,
  - PII exposure,
  - restricted location or culturally sensitive knowledge exposure,
  - exploitation in a running deployment.

### What to include in a report
Minimum:

- Summary: what the issue is and why it matters
- Affected components: ETL / catalogs / graph / API / UI / Story / Focus Mode / CI
- Affected paths (examples): `src/pipelines/**`, `schemas/**`, `data/**`, `src/graph/**`, `src/server/**`, `web/**`, `.github/**`
- Version, tag, or commit SHA tested
- Reproduction steps (minimal and safe PoC preferred)
- Expected vs actual behavior
- Impact assessment:
  - confidentiality / integrity / availability
  - whether sensitive content could be exposed (PII, restricted locations, culturally sensitive knowledge)
- Suggested remediation (optional)

### What not to include

- Secrets, credentials, access tokens, private keys, session cookies
- Full copies of sensitive datasets or precise sensitive coordinates
- Destructive payloads or large-scale disruption instructions
- Public disclosure before coordination

### Reporter template
You can copy/paste this structure into the advisory/email:

~~~text
Title:
  [VULN] <short description>  OR  [INCIDENT] <short description>

Summary:
  <1–3 sentences>

Affected components:
  - Stage(s): <ETL | Catalogs | Graph | API | UI | Story | Focus | CI>
  - Paths: <e.g., src/server/...>

Version tested:
  - Tag/commit: <...>
  - Deployment: <self-hosted / hosted / unknown>

Steps to reproduce:
  1)
  2)
  3)

Observed result:
  <...>

Expected result:
  <...>

Impact:
  - CIA: <Confidentiality / Integrity / Availability>
  - Sensitive content: <PII | restricted location | cultural knowledge | none/unknown>

Notes:
  - Suggested fix / mitigation:
  - Any logs (redacted):
  - Preferred disclosure credit name (optional):
~~~

---

## 🧯 Triage and severity

KFM treats **sensitive-content exposure** as a first-class security concern, even if “traditional exploitability” is low.

### Severity guidance

| Severity | Examples | Typical first actions |
|---|---|---|
| Critical | RCE, auth bypass, mass data exfiltration, active secrets leakage; publication of restricted locations or culturally sensitive knowledge | Contain immediately: rotate secrets, disable/limit affected surface, block publication paths, remove/revoke exposed artifacts |
| High | Privilege escalation, SSRF to internal metadata, stored XSS, major sensitive-content exposure | Mitigate quickly; add detection; confirm scope; prepare patch and artifact rebuilds |
| Medium | Reflected XSS with constraints, limited info leaks, dependency issue without clear exploit | Patch with regression tests; update dependencies; add validation gates |
| Low | Hardening opportunities, non-exploitable misconfigs, low-impact issues | Track for improvement; document mitigations |

### Sensitivity classification rule
If sensitivity/sovereignty status is unclear, KFM posture is **fail closed**:

- treat the issue as restricted,
- limit dissemination of details,
- require governance review before publishing any postmortem/advisory that could reveal sensitive content.

---

## 🧰 Maintainer response process

High-level workflow:

1. **Acknowledge** the report and establish a private coordination thread.
2. **Reproduce** and scope impact across **code + data artifacts + deployments**.
3. **Classify** severity and sensitivity (PII, restricted location, culturally sensitive knowledge).
4. **Contain** if needed:
   - rotate secrets, revoke tokens, restrict endpoints,
   - temporarily unpublish or block affected artifacts.
5. **Fix** with tests and contract validation.
6. **Rebuild/replace** any affected published artifacts:
   - STAC/DCAT/PROV outputs,
   - graph ingest outputs,
   - Story Nodes and any caches/derived bundles.
7. **Disclose** via coordinated advisory and release notes (timelines case-by-case).
8. **Record** remediation in governance/provenance artifacts where applicable.

### Incident response (confirmed)
A confirmed incident requires additional steps:

- Preserve evidence safely (redacted logs; do not collect extra PII).
- Identify blast radius:
  - which datasets/collections/items were affected,
  - which endpoints or UI flows could expose the data,
  - whether any tokens/keys were exposed.
- Contain:
  - revoke and rotate credentials,
  - block vulnerable endpoints,
  - revoke/pull affected artifacts from publication targets.
- Recover:
  - patch and redeploy,
  - rebuild catalogs/provenance,
  - validate “no regression” via CI gates.
- Post-incident:
  - add regression tests and monitoring,
  - produce an internal postmortem (optional) and a public summary if appropriate.

### Coordinated disclosure timeline
- Default timeline: **TBD** (maintainers must define).
- If sensitive communities or restricted locations are involved, disclosure timing and detail level require governance review and may be delayed or redacted.

---

## 🤝 Researcher guidelines

Good-faith expectations:

- Test only against systems you control or have explicit authorization to test.
- Avoid privacy violations or service disruption.
- Stop immediately if you encounter unexpected sensitive content; report privately and do not retain or share it.
- Avoid automated scanning or denial-of-service testing without written permission.
- Do not publicly disclose details until a coordinated plan is agreed.

### Safe harbor
This project intends to support good-faith security research. A safe-harbor statement is **recommended** but requires maintainer review before being treated as authoritative:

- **TBD — include a safe harbor clause aligned to your legal posture and hosting environment.**

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Source | Handling |
|---|---|---|---|
| Vulnerability report | Advisory text / email | Reporter | Treat as sensitive until resolved |
| Secret-scanning alert | Tool output | CI / platform tooling | Rotate secrets; confirm scope |
| Dependency advisory | Advisory feed | Dependency tooling | Assess exploitability; patch/upgrade |
| Sensitive-content exposure report | Narrative + redacted examples | Users / reviewers | Apply sovereignty + redaction immediately |
| Artifact integrity concern | Digest/attestation mismatch | CI / reviewers | Block promotion; investigate supply chain |

### Outputs

| Output | Format | Location | Notes |
|---|---|---|---|
| Patch | Code | repo | Includes tests + validation |
| Advisory | Markdown | GitHub advisory (if used) | Publish per coordinated plan |
| Regression tests | Code | `tests/` | Prevent reintroduction |
| Artifact rebuilds | Data/catalog changes | `data/**` | Re-emit STAC/DCAT/PROV as needed |
| Incident note | Markdown | `docs/security/**` | Postmortem + decisions (may be private) |

### Sensitive-content handling rules for security reports

- Do not publish exploit details or sensitive examples until:
  - remediation is complete, and
  - governance review is complete if sensitive content is involved.
- If restricted location or culturally sensitive knowledge is implicated:
  - use generalized geometry in examples,
  - omit “how to locate” instructions,
  - treat related artifacts as high sensitivity until reviewed.

### Quality signals for security fixes

- Reproducible issue with minimal safe PoC
- Clear affected component and version/commit range
- Fix includes regression tests and validation steps
- No new secrets introduced; no new disclosure pathways
- If data artifacts affected: catalogs and provenance updated consistently

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `vulnerability_reported` | Reporter | Advisory + optional telemetry |
| `vulnerability_validated` | Maintainers | Internal notes + optional telemetry |
| `security_fix_released` | Maintainers | Release notes + optional telemetry |
| `promotion_blocked` | CI gate | CI logs + optional telemetry |
| `redaction_applied` | Governance/pipeline | PROV bundle + optional telemetry |

---

## 🌐 STAC, DCAT & PROV alignment

Security issues in KFM often affect **published artifacts**, not only source code. When a vulnerability impacts catalogs, assets, or narratives, remediation must consider catalog and provenance integrity.

### STAC
If a vulnerability affects STAC artifacts:

- Deprecate or replace affected Items or Assets.
- Rebuild derived artifacts that reference the affected asset.
- Validate corrected STAC against project schemas.
- Ensure no signed URLs, tokens, or restricted coordinates are present in public STAC outputs.

### DCAT
If a dataset listing requires correction after remediation:

- Update the dataset record to reflect:
  - changes in access,
  - redaction/generalization applied,
  - corrected distribution links.
- Ensure distributions do not expose restricted content.
- Ensure dataset-level provenance pointers remain valid or are updated.

### PROV
For incidents involving data corrections or redactions:

- Record remediation as a provenance activity so downstream consumers can trace changes.
- Enforce classification propagation: **no output is less restricted than any input in its lineage**.
- If governance status is unclear, fail closed and require review before publication.

### Cross-layer linkage expectations

- Stable dataset IDs/versions should appear consistently across STAC/DCAT/PROV (and, where applicable, in the graph).
- Story Nodes and Focus Mode should reference datasets by stable IDs that resolve to catalog entries.
- Any generalization/redaction applied must be reflected consistently in:
  - processed outputs (`data/processed/**`),
  - catalogs (STAC/DCAT),
  - API responses,
  - UI rendering and audit panels.

### Versioning expectations
- New versions of affected datasets should link predecessor/successor where supported.
- The graph should mirror version lineage where applicable.
- Advisories should reference affected versions of both code and artifacts.

### Supply-chain provenance hooks (if adopted)
If the project adopts artifact attestations and SBOM linking, provenance metadata may include:

- artifact digest,
- build job/run identity,
- attestation reference,
- SBOM reference,
- commit SHA linkage.

---

## 🧱 Architecture

### Components and responsibilities

| Component | Security responsibility | Primary interface |
|---|---|---|
| ETL (`src/pipelines/`) | Treat inputs as untrusted; deterministic transforms; no secret leakage | Config + run logs |
| Catalogs (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`) | Schema-valid metadata; no sensitive disclosure; stable IDs | JSON + validators |
| Graph (`src/graph/`) | Integrity constraints; ingest only from governed outputs | Ingest scripts + API access |
| API boundary (`src/server/`) | Enforce authn/authz plus redaction/generalization | REST/GraphQL contracts |
| UI (`web/`) | Safe rendering; no direct graph access; avoid inference-by-interaction | API calls only |
| Story Nodes (`docs/reports/story_nodes/`) | Provenance-linked facts; no leakage; validate references | Story validator + UI |
| Focus Mode | Provenance-linked synthesis only; respect sensitivity flags; AI opt-in rules | UI + evidence bundles |

### Interfaces and contracts

| Contract surface | Canonical artifact | Validation expectation |
|---|---|---|
| Schemas | `schemas/**` | JSON schema validation in CI |
| STAC outputs | `data/stac/**` | STAC profile validation in CI |
| DCAT outputs | `data/catalog/dcat/**` | DCAT profile validation in CI |
| PROV outputs | `data/prov/**` | PROV profile validation in CI |
| API contracts | `src/server/**` + docs | Contract tests + schema linting |
| UI registries | `web/**` | Schema-validated config; no direct graph access |
| Story Nodes | `docs/reports/story_nodes/**` | Template + provenance + citation validation |

### Trust boundaries

- External data sources → ETL: untrusted inputs; validate and sanitize.
- CI runner → build artifacts: protect signing, secrets, and output integrity.
- API → clients: enforce auth, rate limits, and redaction.
- Narrative rendering: treat story content and linked assets as potentially risky.

### Security controls by pipeline stage

| Stage | Common risks | Baseline controls | Primary enforcement |
|---|---|---|---|
| ETL | malicious files, parser vulnerabilities, data poisoning | input validation, strict parsing, pinned deps, deterministic runs | `src/pipelines/**` + CI |
| Catalog build | schema drift, sensitive fields, malicious asset URLs | schema validation, leakage scans, URL allowlists, checksum recording | CI + `schemas/**` |
| Graph ingest | constraint violations, provenance loss, unbounded merges | uniqueness constraints, deterministic merge keys, import validation | `src/graph/**` + tests |
| API | auth bypass, injection, SSRF, excessive exposure | RBAC, input sanitization, allowlists, rate limiting, redaction | `src/server/**` + contract tests |
| UI | XSS, CSRF, inference-by-interaction | safe rendering, CSP, strict API use, config validation | `web/**` + CI |
| Story and Focus | leakage, unsourced claims, unsafe assets, prompt injection | story validator, provenance requirements, redaction notices, restricted asset handling | CI + publish workflow |

### Supply chain integrity (recommended)

- SBOM generation for releases/artifacts (SPDX or CycloneDX).
- Build attestations/provenance for release outputs (SLSA-aligned).
- Digest verification on artifacts consumed by downstream stages.
- Avoid mutable references for critical artifacts (prefer content-addressed digests).

---

## 🧠 Story Node & Focus Mode integration

### Narrative security constraints
Security controls must prevent Story Nodes / Focus Mode from:

- exposing restricted datasets/locations (including via “zoom to reveal” interactions),
- presenting non-provenanced claims as fact,
- bypassing API-layer redaction/authorization,
- loading untrusted remote assets unsafely,
- enabling prompt injection that triggers unsafe tool calls or data exfiltration.

### Provenance-linked narrative rule
- Every factual claim must trace to a dataset/record/asset ID.
- Published Story Nodes must pass validation:
  - no broken references,
  - no policy violations,
  - citations/provenance present,
  - separation of fact vs inference vs hypothesis where applicable.

### Predictive or AI-generated content rule
- AI content must be opt-in.
- AI outputs must carry uncertainty/confidence metadata and must not be presented as sourced fact.
- AI must not infer or reveal sensitive locations.

### Recommended UI behaviors (if implemented)
- Show sensitivity/redaction notices when geometry is generalized or content is withheld.
- Provide an audit panel with:
  - citations and evidence IDs,
  - catalog/provenance references,
  - redaction indicators.

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)
- [ ] Markdown protocol checks (front-matter + required sections + fences)
- [ ] Link/reference checks (no orphan pointers)
- [ ] Secret scanning
- [ ] PII and sensitive-location scanning for public outputs
- [ ] Classification propagation checks where labels exist
- [ ] Schema validation:
  - [ ] STAC (`data/stac/**`)
  - [ ] DCAT (`data/catalog/dcat/**`)
  - [ ] PROV (`data/prov/**`)
  - [ ] UI registries (`web/**`) *(if present)*
  - [ ] Story Nodes (`docs/reports/story_nodes/**`) *(if present)*
  - [ ] Telemetry schemas (`schemas/telemetry/**`) *(if present)*
- [ ] Graph integrity checks (constraints, required links)
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] UI boundary enforcement (forbid Neo4j drivers/connection strings in `web/**`)

### CI expectations
CI is a pipeline contract enforcement layer: it should fail deterministically when contracts, provenance rules, or governance rules are violated.

Recommended security-focused gates:

- no secrets checks
- no sensitive coordinates checks for public outputs
- no signed URLs/tokens in catalogs/docs
- deterministic ordering and checksum presence for published artifacts where applicable
- provenance/attestation checks where adopted

### Reproduction

~~~bash
# Placeholders — replace with repo-specific commands
# 1) run unit/integration tests
# 2) validate schemas (schemas/, data/stac/, data/catalog/dcat/, data/prov/)
# 3) run doc lint / markdown protocol checks
# 4) run secret scan + PII/sensitive-location scan for public outputs
~~~

---

## ⚖ FAIR+CARE & governance

### Review gates
Security fixes require governance review when they involve:

- authn/authz or access controls,
- redaction/generalization rules,
- public-facing endpoints or UI behaviors that affect disclosure,
- any artifact that could expose restricted locations or culturally sensitive knowledge,
- changes in classification of data or outputs.

### CARE and sovereignty considerations
- Identify impacted communities and apply protection rules for restricted locations and culturally sensitive knowledge.
- Prefer least-privilege access, careful redaction, and documented justification for any exposure.
- If governance status is unclear:
  - fail closed,
  - require review before publication,
  - record redaction/generalization actions for transparency.

### AI usage constraints
This document’s front-matter defines:

- Allowed: summarization, structure extraction, translation, keyword indexing
- Prohibited:
  - generate_policy
  - infer_sensitive_locations

Practical rule:
- AI can help draft and organize text, but maintainers/governance must approve any rule that affects disclosure, redaction, or sensitive community impacts.

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial SECURITY.md scaffold: private reporting, response process, STAC/DCAT/PROV remediation guidance | TBD |
| v1.0.1 | 2025-12-27 | Expanded triage/severity, control matrix, and governance fail-closed posture | TBD |
| v1.0.2 | 2025-12-27 | Template-aligned upgrade: added reporting quickstart, incident response, contracts table, AI/prompt-injection considerations, and clarified artifact rebuild requirements | TBD |
| v1.0.3 | 2025-12-28 | Universal-template alignment pass: normalized headings, canonical paths, repo-drift guardrails, and CI gate checklist wording | TBD |
| v1.0.4 | 2025-12-29 | Architecture-sync pass: aligned directory layout + pipeline diagram to canonical repo top-levels and “boundary artifacts” language; tightened invariants and validation gates | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Ingestion architecture: `docs/architecture/KFM_INGEST_ARCHITECTURE.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
