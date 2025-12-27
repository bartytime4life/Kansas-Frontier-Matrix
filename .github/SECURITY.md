---
title: "KFM Security Policy"
path: ".github/SECURITY.md"
version: "v1.0.1"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:github:security-policy:v1.0.1"
semantic_document_id: "kfm-security-policy-v1.0.1"
event_source_id: "ledger:kfm:doc:github:security-policy:v1.0.1"
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

> **Purpose (required):** Provide a **private, safe process** for reporting security vulnerabilities affecting Kansas Frontier Matrix (KFM), and define how maintainers triage, remediate, and coordinate disclosure across the full KFM pipeline (ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode).

**Do not open public GitHub issues for security vulnerabilities.**  
Use a private channel as described under **“Reporting a vulnerability.”**

If you believe you have found **active exploitation**, **credential exposure**, **PII exposure**, or **restricted/sensitive location disclosure**, **stop immediately** and report privately (do not continue testing; do not retain/share the data).

---

## 📘 Overview

### Purpose
This policy exists to:
- Define a **private disclosure** path for vulnerabilities and sensitive-data exposure reports.
- Ensure fixes preserve KFM’s **canonical, contract-first architecture** and governance posture:
  - **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** (non-negotiable ordering).
- Prevent harm from:
  - conventional software vulnerabilities (auth bypass, injection, XSS, SSRF, secrets leakage),
  - **data governance failures** (PII leaks, restricted location disclosure, culturally sensitive knowledge exposure),
  - and supply-chain risk (malicious builds/artifacts, dependency compromise).

### Scope

| In Scope | Out of Scope |
|---|---|
| Vulnerabilities in repository code, workflows, configs, schemas, release artifacts, and documentation that impact confidentiality/integrity/availability | General product questions / support requests |
| Exposure of sensitive or restricted content (PII, precise coordinates, culturally restricted knowledge) through catalogs/APIs/UI/narratives | Vulnerabilities in third-party services not operated by the project (unless triggered by repo misconfiguration) |
| Authn/authz, rate limiting, injection, SSRF, XSS, CSRF, secrets leakage, dependency/supply-chain risk | Social engineering, physical attacks, or issues requiring physical access |
| Security issues in Focus Mode / story rendering (unintended leakage; unsafe asset loading; narrative injection) | Denial-of-service testing without explicit written permission |
| CI/workflow misconfigurations that could expose secrets or enable malicious builds | Feature requests that do not present a security risk |

### Audience
- Primary: security researchers, maintainers, contributors.
- Secondary: data stewards / governance reviewers, operators of deployments, downstream integrators.

### Definitions
- Link: `docs/glossary.md` *(not confirmed in repo; expected by template)*

Key terms used here:
- **Vulnerability:** A weakness that can be exploited to compromise confidentiality, integrity, or availability.
- **Security incident:** Confirmed exploitation or confirmed sensitive-data exposure requiring containment and notification steps.
- **Coordinated disclosure:** Private reporting and fix coordination before public disclosure.
- **Sensitive content:** Any content restricted by governance, including PII and culturally sensitive knowledge, and any location-bearing data requiring generalization/redaction.
- **Redaction/generalization:** Transformations applied to prevent harmful disclosure (e.g., removing fields, coarsening geometry).
- **Contract boundary:** A machine-validated interface (schema/spec) that producers/consumers must obey (schemas, API specs, UI registries).
- **Provenance bundle / PROV:** Lineage artifacts that explain what inputs produced what outputs, when, and by which process/agent.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Security policy (canonical) | `.github/SECURITY.md` | Maintainers | This document |
| CI workflows | `.github/workflows/` | Maintainers | Security + contract enforcement gates (if configured) |
| Schemas registry | `schemas/` | Maintainers | STAC/DCAT/PROV/story/UI/telemetry schemas (contract-first) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Maintainers | Evidence + discovery + lineage |
| Graph layer | `src/graph/` + `data/graph/` *(if present)* | Maintainers | Ontology + ingest artifacts |
| API boundary | `src/server/` + `src/server/contracts/` | Maintainers | Redaction + access control enforcement |
| UI | `web/` | Maintainers | Map/narrative client; must not read graph directly |
| Governance references | `docs/governance/*` | Governance reviewers | Sovereignty/Ethics/CARE constraints |
| Optional deeper security docs | `docs/security/` | Maintainers | Threat model, incident playbooks (recommended) |

### Definition of done for this document
- [ ] Front-matter complete + `path` matches file location
- [ ] Reporting guidance is unambiguous (private first; no public exploit details)
- [ ] Sensitive-data handling rules (redaction/generalization) are explicit
- [ ] Architecture invariants stated (pipeline order; API boundary; provenance rules)
- [ ] CI/validation expectations are listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “TBD / not confirmed in repo” placeholders reviewed and resolved by maintainers

---

### Supported versions (fill-in; maintainers must confirm)
KFM support policy can vary by release cadence. Until maintainers define it explicitly:

- **Supported (recommended default):**
  - default branch (`main`)
  - most recent tagged release (**TBD — confirm release strategy**)
- **Best-effort:** older tags/snapshots may receive guidance but not patches.
- **Unsupported:** unmaintained forks or historical snapshots unless explicitly noted.

> Important: security guidance for “versions” applies to **both code** and **published artifacts** (catalogs, story nodes, derived datasets). A “fixed” codebase is not sufficient if affected artifacts remain public.

---

### Reporting a vulnerability

**Please do not open a public GitHub issue** for security-sensitive reports.

Preferred reporting path:
1. Use the repository’s **Security Advisories** workflow (private report / draft advisory), **if enabled**.
2. If advisories are not available, open a public issue **only to request a private channel**, and **do not** include exploit details, sensitive data, or PoC content.

Alternate reporting paths (only if advisories are unavailable):
- Email: **TBD — add project security contact**
- Encryption: **TBD — publish PGP key fingerprint (optional)**

#### If this is urgent (suspected active exploitation or sensitive-data leak)
- Include **“URGENT / INCIDENT”** in the report title.
- State clearly whether any of the following occurred or is likely:
  - credential/secrets exposure,
  - PII exposure,
  - restricted location or culturally sensitive knowledge exposure,
  - exploitation in a running deployment.

---

### What to include in a report (minimum)
- Summary: what is the issue and why it matters
- Affected component(s): ETL / catalogs / graph / API / UI / Story/Focus Mode / CI
- Affected paths (examples):
  - `src/pipelines/**`, `schemas/**`, `data/**` (catalogs), `src/graph/**`, `src/server/**`, `web/**`, `.github/**`
- Exact version, tag, or commit SHA tested
- Reproduction steps (minimal, safe PoC preferred)
- Expected vs actual behavior
- Impact assessment:
  - confidentiality/integrity/availability
  - whether sensitive content could be exposed (PII, restricted locations, culturally sensitive knowledge)
- Any suggested remediation (optional)

#### What not to include
- Secrets, credentials, access tokens, private keys, session cookies
- Full copies of sensitive datasets or sensitive coordinates
- Destructive payloads (irreversible deletion, ransomware-like behavior, large-scale disruption)
- Public disclosure before coordination

---

### Triage and severity (guidance; no SLA implied)

KFM treats **sensitive-data exposure** as a first-class security concern, even if “traditional exploitability” is low.

| Severity | Examples (non-exhaustive) | Typical first actions (maintainers) |
|---|---|---|
| Critical | RCE, auth bypass, mass data exfiltration, active secrets leakage; publication of restricted locations/culturally sensitive knowledge | Contain immediately: rotate secrets, disable/limit affected surface, block publication paths |
| High | Privilege escalation, SSRF to internal metadata, stored XSS, major sensitive-data exposure | Mitigate quickly; add detection; confirm scope; prepare patch |
| Medium | Reflected XSS with constraints, limited info leaks, dependency issue without clear exploit | Patch with regression tests; update dependencies; add validation gates |
| Low | Hardening opportunities, non-exploitable misconfigs, low-impact issues | Track for improvement; document mitigations |

> Governance note: if classification/sovereignty status is unclear, KFM posture is **fail closed** (treat as restricted until reviewed).

---

### Maintainer response process (high-level)
1. **Acknowledge** the report and establish a private coordination thread.
2. **Reproduce** and scope impact (code + data artifacts + deployments).
3. **Classify** severity and sensitivity (PII, restricted location/cultural knowledge).
4. **Contain** if needed (rotate secrets, disable affected endpoints, revoke tokens, restrict access).
5. **Fix** with regression coverage and contract validation.
6. **Rebuild/replace** any affected published artifacts (catalogs, graph loads, story nodes).
7. **Disclose** via coordinated advisory and release notes (timelines agreed case-by-case).
8. **Record** remediation in provenance/governance artifacts where applicable.

---

### Researcher guidelines (good-faith expectations)
- Act in good faith and avoid privacy violations or service disruption.
- Test only against systems you control or have explicit authorization to test.
- Stop immediately if you encounter unexpected sensitive data; report privately and do not retain/share it.
- Avoid automated scanning or DoS testing without written permission.
- Do not publicly disclose details until a coordinated plan is agreed.

---

## 🗂️ Directory Layout

### This document
- `path`: `.github/SECURITY.md`

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| GitHub governance & CI | `.github/` | Repo health + policy + workflows |
| CI workflows | `.github/workflows/` | CI gates for contracts, security scans, validation |
| Optional local actions | `.github/actions/` | Reusable composite actions (if present) |
| Security docs (optional deeper standards) | `docs/security/` | Threat model, incident response, supply chain notes |
| Governance | `docs/governance/` | Ethics + sovereignty + approval workflow references |
| Schemas | `schemas/` | Contract validation schemas (STAC/DCAT/PROV/story/UI/telemetry) |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog builders |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical published evidence + lineage |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology + ingest artifacts |
| API boundary | `src/server/` | Contracted access; enforce redaction/authorization |
| UI | `web/` | React/Map client; config validated; no direct graph access |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts; provenance/citation requirements |

### Expected file tree (security-related)
~~~text
📁 .github/
├── 📄 SECURITY.md
└── 📁 workflows/
    └── 📄 *.yml                      # CI gates (filenames not enumerated unless present in-repo)

📁 docs/
└── 📁 security/                      # optional (recommended)
    ├── 📄 threat_model.md
    ├── 📄 incident_response.md
    ├── 📄 supply_chain_integrity.md
    └── 📁 advisories/                # optional internal writeups (not public unless approved)
~~~

---

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system with a governed pipeline designed for auditability and harm reduction. The architecture is intentionally staged so that:
- deterministic transforms happen in ETL,
- discovery and evidence are expressed through STAC/DCAT/PROV catalogs,
- semantics are expressed in the graph,
- the API boundary enforces access control and redaction,
- the UI renders only what the API serves,
- story nodes and Focus Mode remain **provenance-linked** and governance-safe.

Security in KFM therefore includes:
- software security (code, dependencies, CI),
- data security (sensitivity classification, redaction/generalization),
- narrative safety (preventing leakage through storytelling and interaction).

### Core invariants (non-negotiable)
- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- **No UI direct-to-graph reads:** the UI must never bypass the API to query Neo4j directly.
- **Contracts are canonical:** schemas/specs define structure; code must conform; CI validates.
- **No unsourced narrative in published stories:** factual claims must be supported by evidence/citations and pass validation.
- **Governance uncertainty fails closed:** if sensitivity/sovereignty is unclear, treat as restricted until reviewed.

### Threat model snapshot (high-level)
Primary threat categories:
- **Supply chain compromise:** malicious dependency update, compromised CI signing, artifact replacement.
- **Data poisoning & malicious inputs:** hostile upstream files, crafted geospatial assets, malformed metadata.
- **Unauthorized access:** weak authn/authz, RBAC gaps, leaked credentials, insecure defaults.
- **Injection & web vulnerabilities:** SQL/Graph query injection, XSS/CSRF, SSRF, unsafe deserialization.
- **Sensitive-data leakage:** precise coordinates, metadata re-identification, “inference-by-UI” (zoom, filters).
- **Integrity loss:** tampering with catalogs, provenance, or story evidence.

### Roles (not confirmed in repo; define in governance docs)
Recommended role concepts to align with governance:
- **Maintainers:** technical triage, patching, releases.
- **Governance reviewers:** sensitivity/sovereignty decisions, approval for disclosure of sensitive impacts.
- **Incident lead (on-call):** coordinates containment and communications (role assignment TBD).

### Open questions (must be resolved by maintainers)
| Question | Owner | Target date |
|---|---|---|
| Official security contact email/URI? | Maintainers | TBD |
| Are GitHub private Security Advisories enabled? | Maintainers | TBD |
| Do we publish a PGP key for reports? | Maintainers | TBD |
| Supported versions policy (main-only vs LTS)? | Maintainers | TBD |
| Advisory publication defaults (public vs private)? | Maintainers + Governance | TBD |
| Incident notification procedure for sensitive-data exposure? | Governance owners | TBD |

### Future extensions (recommended)
- Add `docs/security/threat_model.md` (assets, actors, trust boundaries, abuse cases)
- Add `docs/security/incident_response.md` (severity rubric, comms, postmortems)
- Add `docs/security/supply_chain_integrity.md` (SBOM/attestations/provenance index policy)
- Add CI gates for:
  - secret scanning,
  - PII/sensitive-location scanning for public outputs,
  - provenance/attestation cross-checks (if adopted).

---

## 🗺️ Diagrams

### Coordinated disclosure workflow
~~~mermaid
flowchart LR
  R[Reporter] --> C["Private reporting channel\n(Security Advisory / email)"]
  C --> T["Triage + reproduce"]
  T --> S["Severity + sensitivity classification\n(incl. governance)"]
  S --> M["Mitigation / containment\n(rotate secrets, restrict surface)"]
  M --> F["Fix + tests + contract validation"]
  F --> P["Patch release + artifact rebuilds"]
  P --> A["Advisory + coordinated disclosure"]
~~~

### Canonical pipeline + security enforcement points
~~~mermaid
flowchart TB
  A[ETL<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>src/graph + data/graph]
  C --> D[API Boundary<br/>src/server + contracts]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]

  CI[CI Gates<br/>.github/workflows] -. validates .-> A
  CI -. validates .-> B
  CI -. validates .-> C
  CI -. validates .-> D
  CI -. validates .-> E
  CI -. validates .-> F
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Handling |
|---|---|---|---|
| Vulnerability report | Advisory text / email | Reporter | Treat as sensitive until resolved |
| Secret-scanning alert | Tool output | CI / platform tooling | Rotate secrets; confirm scope |
| Dependency advisory | Advisory feed | Dependency tooling (if enabled) | Assess exploitability; patch/upgrade |
| Sensitive-data exposure report | Narrative + examples | Users/governance reviewers | Apply sovereignty + redaction immediately |
| Artifact integrity concern | Digest/attestation mismatch | CI / reviewers | Block promotion; investigate supply chain |

### Outputs

| Output | Format | Location | Notes |
|---|---|---|---|
| Patch | Code | repo | Includes tests + validation |
| Advisory | Markdown | GitHub Security Advisory (if used) | Publish per coordinated plan |
| Regression tests | Code | `tests/` | Prevent reintroduction |
| Artifact rebuilds | Data/catalog changes | `data/**` | Re-emit STAC/DCAT/PROV as needed |
| Incident note (optional) | Markdown | `docs/security/**` | Postmortem, decisions, mitigations |

### Sensitivity & redaction rules for security reports
- Do not publish exploit details or sensitive examples (especially exact locations) until:
  - remediation is complete, and
  - governance review is complete (if sensitive data involved).
- If restricted location/cultural knowledge is implicated:
  - use generalized geometry in examples,
  - omit “how to locate” instructions,
  - treat all related artifacts as high sensitivity until reviewed.

### Quality signals for security fixes
- Reproducible issue with minimal safe PoC
- Clear affected component + version/commit range
- Fix includes regression tests and validation steps
- No new secrets introduced; no new leakage pathways
- If data artifacts affected: catalogs and provenance updated consistently

### Telemetry signals (recommended; adopt in `docs/telemetry/` + `schemas/telemetry/` if configured)
| Signal | Source | Where recorded |
|---|---|---|
| `vulnerability_reported` | Reporter | Security advisory + optional telemetry |
| `vulnerability_validated` | Maintainers | Internal notes + optional telemetry |
| `security_fix_released` | Maintainers | Release notes + optional telemetry |
| `promotion_blocked` | CI gate | CI logs + optional telemetry |
| `redaction_applied` | Governance/pipeline | PROV bundle + optional telemetry |

---

## 🌐 STAC, DCAT & PROV Alignment

Security issues in KFM often affect **published artifacts**, not only source code. When a vulnerability impacts catalogs, assets, or narratives, remediation must consider catalog/provenance integrity.

### STAC (assets/items/collections)
If a vulnerability affects STAC artifacts (e.g., malicious asset, sensitive content published):
- Deprecate or replace affected Items/Assets (per KFM-STAC profile; deprecation mechanism may be profile-specific).
- Rebuild derived artifacts that reference the affected asset.
- Validate corrected STAC against project schemas.
- Ensure no signed URLs, tokens, or restricted coordinates are present in public STAC outputs.

### DCAT (dataset discovery records)
If a dataset listing requires correction after remediation:
- Update the dataset record to reflect:
  - changes in access,
  - redaction/generalization applied,
  - corrected distribution links.
- Ensure distributions do not expose restricted content.
- Ensure dataset-level provenance pointers remain valid (or are updated).

### PROV-O (lineage)
For incidents involving data corrections or redactions:
- Record remediation as provenance activity (where adopted) so downstream consumers can trace changes.
- Ensure classification propagation: **no output is less restricted than any input in its lineage**.
- If governance status is unclear, fail closed and require review before publication.

### Supply-chain provenance hooks (recommended)
If the project adopts artifact attestation and SBOM linking, provenance metadata may include:
- an artifact digest,
- a build job/run identity,
- an attestation reference,
- an SBOM reference,
- commit SHA linkage.

(See also “Validation & CI/CD” for verification patterns.)

---

## 🧱 Architecture

### Components and responsibilities

| Component | Security responsibility | Primary interface |
|---|---|---|
| ETL (`src/pipelines/`) | Treat inputs as untrusted; deterministic transforms; no secret leakage | Config + run logs |
| Catalogs (`data/stac/`, `data/catalog/dcat/`, `data/prov/`) | Schema-valid metadata; no sensitive disclosures; stable IDs | JSON + validators |
| Graph (`src/graph/`, `data/graph/`) | Integrity constraints; ingest only from governed outputs | Ingest scripts + API access |
| API boundary (`src/server/`) | **Enforce authn/authz + redaction/generalization** | REST/GraphQL contracts |
| UI (`web/`) | Safe rendering; no direct graph access; avoid inference-by-interaction | API calls only |
| Story Nodes (`docs/reports/story_nodes/`) | Provenance-linked facts; no leakage; validate references | Story validator + UI |
| Focus Mode | Provenance-linked synthesis only; respect sensitivity flags | UI + evidence bundles |

### Trust boundaries (where to be strict)
- External data sources → ETL: untrusted inputs; validate and sanitize.
- CI runner → build artifacts: protect signing, secrets, and output integrity.
- API → clients: enforce auth, rate limits, and redaction.
- Narrative rendering: treat story content and linked assets as potentially risky (XSS, leakage).

### Security controls by pipeline stage (recommended baseline)

| Stage | Common risks | Controls (recommended baseline) | Primary enforcement point |
|---|---|---|---|
| ETL | malicious files, injection via parsers, data poisoning | input validation, strict parsing, pinned dependencies, deterministic runs | `src/pipelines/**` + CI |
| Catalog build | schema drift, sensitive fields in metadata, malicious asset URLs | schema validation, leakage scans, link allowlists, checksum recording | CI + `schemas/**` |
| Graph ingest | constraint violations, provenance loss, unbounded merges | uniqueness constraints, deterministic merge keys, import validation | `src/graph/**` + tests |
| API | auth bypass, injection, SSRF, excessive data exposure | RBAC, input sanitization, query parameter allowlists, rate limiting, redaction | `src/server/**` + contract tests |
| UI | XSS, CSRF, inference-by-interaction, direct graph access | safe HTML handling, CSP, strict API usage, UI config schema validation | `web/**` + CI |
| Story/Focus | leakage through narrative, unsourced claims, unsafe asset loading | story validator, provenance requirements, redaction notices, restricted asset handling | CI + publishing workflow |

### Supply chain integrity (recommended; adopt if/when enforced)
To reduce risk of artifact tampering and “unknown-origin builds,” adopt:
- **SBOM generation** for releases/artifacts (SPDX or CycloneDX).
- **Attestation/provenance** for build outputs (SLSA-aligned where feasible).
- **Digest verification** on artifacts consumed by downstream stages.
- Avoid mutable references for critical artifacts (prefer content-addressed digests).

> Note: enforcement mechanisms depend on CI/workflow configuration and are not guaranteed by this document alone.

---

## 🧠 Story Node & Focus Mode Integration

### Security constraints for narrative surfacing
Security controls must prevent Story Nodes / Focus Mode from:
- exposing restricted datasets/locations (including via “zoom to reveal” interactions),
- presenting non-provenanced claims as fact,
- bypassing API-layer redaction/authorization,
- loading untrusted remote assets unsafely.

### Provenance-linked narrative rule (hard requirement)
- Every factual claim must trace to a dataset/record/asset ID.
- Published Story Nodes must pass validation (no broken references; no policy violations).

### Recommended UI behaviors (if implemented)
- Display sensitivity/redaction notices when:
  - geometry is generalized,
  - content is withheld,
  - sources are restricted.
- Provide an audit panel view showing:
  - citations and evidence IDs,
  - catalog/provenance references,
  - any redaction applied.

### Optional structured controls (example placeholders)
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)
- [ ] Markdown protocol checks (front-matter + required sections + fences)
- [ ] Secret scanning (no tokens/keys)
- [ ] PII / sensitive-location scanning for public outputs (where applicable)
- [ ] Schema validation:
  - STAC (`data/stac/**`)
  - DCAT (`data/catalog/dcat/**`)
  - PROV (`data/prov/**`)
  - UI registries (`schemas/ui/**` + `web/**/layers/**` as applicable)
  - Story Nodes (`docs/reports/story_nodes/**`)
- [ ] Graph integrity checks (constraints, required links)
- [ ] API contract tests (OpenAPI/GraphQL + implementation tests)
- [ ] UI “no direct graph access” check (forbid Neo4j drivers/connection strings in `web/**`)

### CI expectations (if configured)
KFM CI is a **pipeline contract enforcement layer**: it should fail deterministically when contracts, provenance rules, or governance rules are violated.

Recommended security-focused gates:
- “no secrets” checks
- “no sensitive coordinates” checks for public outputs
- “no signed URLs/tokens” in catalogs/docs
- deterministic ordering + checksum presence for published artifacts (as applicable)

### Supply-chain verification patterns (optional; adopt if implemented)
If the project emits attestations and SBOM references, CI or reviewers should be able to verify:
- artifact bytes match `artifact_digest`
- attestation subject digest matches `artifact_digest`
- predicate/run metadata matches `build_job_id` and `commit_sha`
- SBOM exists and is retrievable (SPDX/CycloneDX)

### Reproduction (deterministic)
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run unit/integration tests
# 2) validate schemas (schemas/, data/stac/, data/catalog/dcat/, data/prov/)
# 3) run doc lint / markdown protocol checks
# 4) run secret scan + PII/sensitive-location scan for public outputs
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates
Security fixes require governance review when they involve:
- authentication/authorization changes,
- redaction/generalization rules,
- public-facing endpoints or UI behaviors that affect disclosure,
- any artifact that could expose restricted locations/culturally sensitive knowledge,
- any change that expands access to sensitive/restricted information.

(Approver roles are **not confirmed in repo**; align with `docs/governance/ROOT_GOVERNANCE.md`.)

### CARE / sovereignty considerations
- Identify impacted communities and apply protection rules for restricted locations and culturally sensitive knowledge.
- Prefer least-privilege access, careful redaction, and documented justification for any exposure.
- If governance status is unclear:
  - fail closed (treat as restricted),
  - require review before publication,
  - log redaction/generalization actions for transparency.

### AI usage constraints
This document’s front-matter defines:
- Allowed: summarization, structure extraction, translation, keyword indexing
- Prohibited:
  - **generate_policy** (AI must not be treated as the authority for final policy decisions),
  - **infer_sensitive_locations** (directly or indirectly).

Practical rule:
- AI can help **draft** and **organize** text, but maintainers/governance must approve:
  - severity rubrics,
  - disclosure defaults,
  - any rule that affects sensitive-data exposure.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial SECURITY.md scaffold: private reporting, response process, STAC/DCAT/PROV remediation guidance | TBD |
| v1.0.1 | 2025-12-27 | Deepened policy: aligned to KFM-MDP heading constraints; expanded triage/severity, pipeline control matrix, supply-chain integrity recommendations, and governance fail-closed posture | TBD |

---

## Footer refs (do not remove)
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
