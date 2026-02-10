# .github — Governance & Automation Control Plane for Kansas Frontier Matrix (KFM)

![Governed](https://img.shields.io/badge/Governed-Yes-blue)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-Yes-success)
![Evidence--First](https://img.shields.io/badge/Evidence--First-Required-informational)
![Fail--Closed](https://img.shields.io/badge/Governance-Fail--Closed-important)
![Trust%20Membrane](https://img.shields.io/badge/Architecture-Trust%20Membrane-8A2BE2)
![Supply%20Chain](https://img.shields.io/badge/Supply%20Chain-Guarded-critical)

> [!IMPORTANT]
> This folder is the **repo-level control plane** for KFM: contribution safety, CI gates, and policy enforcement live here.
> If a change bypasses these controls, it conflicts with KFM’s **evidence-first** and **fail-closed** design goals.

> [!NOTE]
> Some files referenced in this README may be **TBD** in your current repo snapshot (**not confirmed in repo**).
> This README defines the **intended baseline** so the repo can converge on a consistent, auditable governance posture.

---

## 📌 Quick orientation

- **If you are contributing:** start at **“Contribution Workflow”** and **“PR Gate Checklist.”**
- **If you are reviewing:** start at **“Controls Matrix”** and **“Protected Paths + CODEOWNERS.”**
- **If you are setting up repo settings:** start at **“Branch Protection / Rulesets Baseline.”**

---

## 🔎 Gap analysis → enhancements implemented in this baseline

This README started from a solid “principles + recommended files” outline. The biggest governance gaps were **enforcement specificity** and **operational clarity**. This version closes those gaps by:

- **Making “fail-closed” concrete** with a *controls matrix*, a *required-checks contract*, and an explicit *repo settings baseline*.
- **Adding supply-chain controls** beyond Dependabot: *dependency review as a required PR gate*, GitHub Actions hardening, and secret leak prevention via *push protection*.  [oai_citation:0‡GitHub Docs](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configuring-the-dependency-review-action?utm_source=chatgpt.com)
- **Separating “policy intent” from “repo reality”** using a *manifest table* that labels files as **Required / Recommended / Optional**, and marks any repo-specific values as **(not confirmed in repo)**.
- **Adding an exception (“break-glass”) path** that stays auditable instead of relying on informal bypasses.
- **Clarifying high-impact paths** and CODEOWNERS enforcement, including the GitHub branch protection option to require Code Owner review.  [oai_citation:1‡GitHub Docs](https://docs.github.com/articles/about-code-owners?utm_source=chatgpt.com)
- **Adding an issue intake control** using `ISSUE_TEMPLATE/config.yml` guidance to reduce “blank issue” drift and route sensitive reports appropriately.  [oai_citation:2‡GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository?utm_source=chatgpt.com)
- **Modernizing protections** by acknowledging GitHub **rulesets** as an alternative/complement to branch protection rules.  [oai_citation:3‡GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets?utm_source=chatgpt.com)

---

## 📘 Overview

### Purpose
KFM is designed as a governed geospatial/historical knowledge system where:

- **User-visible content is evidence-backed** (datasets, narratives, and AI answers carry provenance/citations).
- **Governance is enforced by default** (missing metadata, missing provenance, or failing checks should block merges/releases).

This `.github/` directory hosts the operational guardrails that implement that posture: PR requirements, CI workflows, security policy, and review routing.

### Scope

| In scope | Out of scope |
|---|---|
| Pull Request / Issue workflow and templates | Domain-specific narrative content (**see `docs/`**) |
| CI/CD workflows & required checks | Runtime infrastructure configuration (**handled in infra/deploy layers**) |
| Security disclosure + repo hardening policies | Dataset-specific metadata records (**see `data/` + `docs/`**) |
| CODEOWNERS and path-based review protections | End-user UI documentation (**see product docs**) |

### Audience
- **Contributors:** understand how to propose changes safely.
- **Reviewers/Maintainers:** apply consistent governance decisions.
- **Security & Data stewards:** verify policy compliance before merge/release.

### Definitions (Repo Ops)
- **Fail-closed:** if required checks/metadata are missing, the change is blocked.
- **Evidence-first:** factual claims (docs, story nodes, AI outputs) must be traceable to sources.
- **Trust membrane:** the UI never talks directly to databases; all access is governed via API.

---

## 🧩 Controls matrix

This is the “what enforces what” map. If a principle has no enforcement line, it’s a governance gap.

| Principle | What it means in KFM | Enforced by (automation) | Enforced by (human) | Fail-closed signal |
|---|---|---|---|---|
| Evidence-first | Claims trace to sources + transformations | Provenance validation workflow; doc schema checks | Data/Doc steward review | CI fails on missing required fields / citations |
| Fail-closed | Missing required artifacts blocks merge | Branch protections / rulesets + required status checks  [oai_citation:4‡GitHub Docs](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com) | Maintainers do not override except break-glass | PR cannot merge |
| Supply-chain guarded | Dependencies & actions are scrutinized | Dependabot + dependency review + code scanning  [oai_citation:5‡GitHub Docs](https://docs.github.com/en/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file?utm_source=chatgpt.com) | Security steward review | Security gate fails |
| Secret-safe | No secrets in git history | Secret scanning + push protection  [oai_citation:6‡GitHub Docs](https://docs.github.com/code-security/secret-scanning/about-secret-scanning?utm_source=chatgpt.com) | Security steward triage | Push blocked / alert raised |
| Trust membrane | UI never directly hits DB | Architectural tests (if present), API contract checks (**not confirmed in repo**) | Architecture review | Review blocks merge |

> [!IMPORTANT]
> “Fail-closed” requires **repository settings** (branch protection or rulesets) *and* **required CI checks**. A workflow existing is not enough; it must be **required**.  [oai_citation:7‡GitHub Docs](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com)

---

## 🗂️ Directory layout + governance manifest

### `.github/` (this folder)

```text
.github/
  README.md
  SECURITY.md
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  ISSUE_TEMPLATE/
    config.yml
    bug_report.yml
    feature_request.yml
    data_ingest_request.yml
    story_node_request.yml
  workflows/
    ci.yml
    docs-validation.yml
    provenance-validation.yml
    security.yml
    dependency-review.yml
    codeql.yml
    scorecard.yml
  dependabot.yml
```

### Governance manifest (Required vs Recommended)

| Path | Status | Why it exists | Owner role (recommended) |
|---|---:|---|---|
| `.github/README.md` | **Required** | Defines the repo governance baseline | Maintainers |
| `.github/SECURITY.md` | **Required** | Vulnerability intake + disclosure | Security steward |
| `.github/CODEOWNERS` | **Required** | Mandatory review routing for sensitive paths | Maintainers |
| `.github/PULL_REQUEST_TEMPLATE.md` | **Required** | Standardizes risk, provenance, and checks | Maintainers |
| `.github/ISSUE_TEMPLATE/config.yml` | Recommended | Controls issue chooser + contact links  [oai_citation:8‡GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository?utm_source=chatgpt.com) | Maintainers |
| `.github/workflows/ci.yml` | **Required** | Tests/lint/typecheck/build | Engineering lead |
| `.github/workflows/docs-validation.yml` | **Required** | Markdown + schema + link checks | Doc steward |
| `.github/workflows/provenance-validation.yml` | **Required** | Metadata/lineage gates for datasets | Data steward |
| `.github/workflows/security.yml` | **Required** | Secret scan policy checks; SAST hooks | Security steward |
| `.github/workflows/dependency-review.yml` | Recommended | Block vulnerable deps in PRs  [oai_citation:9‡GitHub Docs](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configuring-the-dependency-review-action?utm_source=chatgpt.com) | Security steward |
| `.github/workflows/codeql.yml` | Recommended | Code scanning (SAST) | Security steward |
| `.github/dependabot.yml` | Recommended | Automated dependency PRs  [oai_citation:10‡GitHub Docs](https://docs.github.com/en/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file?utm_source=chatgpt.com) | Maintainers |

> [!NOTE]
> If a **Required** item is missing, treat it as a **governance gap** and open an issue labeled `governance-gap` (label taxonomy below).

---

## 🧭 Context: KFM posture & “truth path”

KFM’s project posture is built around:

- **Provenance surfaced to users** (e.g., Focus Mode “Audit” panel + dataset info dialogs show source + transformations) (**not confirmed in repo**).
- **Narratives as governed artifacts** (Story Nodes follow a strict template and carry citations).
- **A governed “truth path” for data** (Raw → Processed → Catalog/PROV → Database → API → UI).

Repo operations should reflect those design commitments—CI and reviews are not “nice to have”; they are part of the product contract.

### Trust membrane (high level)

```mermaid
flowchart LR
  U[User] --> UI[Web UI (React/MapLibre)]
  UI --> API[Governed API Layer]
  API --> PG[(PostGIS)]
  API --> G[(Graph Store)]
  API --> S[(Search/Index)]
  API --> C[(Catalog/Metadata)]
```

### Contribution + governance flow

```mermaid
flowchart TD
  A[Contributor] --> B[Issue / Proposal]
  B --> C[PR w/ Template + Checklists]
  C --> D[CI Gates: lint/tests/security/docs/provenance]
  D -->|pass| E[CODEOWNERS Review + Governance Review if needed]
  D -->|fail| F[Block merge (fail-closed)]
  E --> G[Merge]
  G --> H[Release / Deploy Workflow (if configured)]
```

### Data “truth path” (pipeline contract)

```mermaid
flowchart LR
  R[data/raw + source manifest] --> P[data/processed]
  P --> M[Catalog: STAC/DCAT (design target)]
  M --> V[PROV lineage (design target)]
  V --> DB[(Databases)]
  DB --> API[API]
  API --> UI[UI + Focus Mode]
```

---

## 🛡️ Branch protection / rulesets baseline

KFM governance cannot be “best effort.” Use **protected branches** and/or **rulesets** to enforce merge discipline.  [oai_citation:11‡GitHub Docs](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com)

### Required settings for the default branch (baseline)

> [!IMPORTANT]
> The terms “branch protection rule” and “ruleset” both appear in GitHub’s current governance model; use what your org supports best. Rulesets explicitly support “required status checks” and other constraints for branches/tags.  [oai_citation:12‡GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets?utm_source=chatgpt.com)

**Repository settings checklist (fail-closed):**
- [ ] Require pull request before merging (**no direct pushes**)
- [ ] Require approvals (suggested: **1–2**, depending on risk)
- [ ] **Require review from Code Owners**  [oai_citation:13‡GitHub Docs](https://docs.github.com/articles/about-code-owners?utm_source=chatgpt.com)
- [ ] Require status checks to pass before merging  [oai_citation:14‡GitHub Docs](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com)
- [ ] Require branches to be up to date before merging (recommended for high-risk repos)
- [ ] Restrict who can push to protected branches (maintainers only)
- [ ] Block force pushes and deletion on protected branches  [oai_citation:15‡GitHub Docs](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com)

### Required status checks contract (names are repo-specific)

These must match your workflow/job names (**not confirmed in repo**). Example contract:

| Check name (example) | What it blocks on failure |
|---|---|
| `ci / test` | failing unit/integration/contract tests |
| `ci / lint` | lint/typecheck/format violations |
| `docs-validation` | broken links / invalid doc structure |
| `provenance-validation` | missing manifest/lineage metadata |
| `security` | secret scanning / SAST gate fails |
| `dependency-review` | vulnerable dependency introduced  [oai_citation:16‡GitHub Docs](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/customizing-your-dependency-review-action-configuration?utm_source=chatgpt.com) |

> [!TIP]
> If you adopt rulesets, GitHub’s rulesets documentation explicitly calls out “Required status checks ensure required CI tests are passing before changes can be made.”  [oai_citation:17‡GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets?utm_source=chatgpt.com)

---

## 🧰 GitHub Actions security hardening baseline

GitHub recommends applying the **principle of least privilege** to the `GITHUB_TOKEN` and granting only what each workflow/job needs.  [oai_citation:18‡GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use?utm_source=chatgpt.com)

### Mandatory workflow constraints (baseline)

- **Least privilege** for `GITHUB_TOKEN`
  - Set default workflow permissions to **read-only** for repository contents, then elevate per job as needed.  [oai_citation:19‡GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use?utm_source=chatgpt.com)
- **Pin third-party actions**
  - Pin actions to commit SHAs (supply-chain safety). *(Practice recommended; verify your org’s standard if different.)*
- **Avoid unsafe triggers**
  - Be cautious with workflows that execute untrusted code (e.g., fork PRs). Use hardened patterns and avoid privilege escalation on untrusted inputs.
- **Use OIDC for cloud deploy credentials when applicable**
  - OIDC jobs require `permissions: id-token: write` (only on deploy jobs).  [oai_citation:20‡GitHub Docs](https://docs.github.com/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services?utm_source=chatgpt.com)

---

## 🔐 Secrets, vulnerabilities, and supply-chain posture

### Secret scanning + push protection (baseline)

Secret scanning detects known secret formats in commits.  [oai_citation:21‡GitHub Docs](https://docs.github.com/code-security/secret-scanning/about-secret-scanning?utm_source=chatgpt.com)  
Push protection is designed to **prevent secrets from being pushed in the first place** and blocks the push when a secret is detected.  [oai_citation:22‡GitHub Docs](https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection?utm_source=chatgpt.com)

**Repo baseline checklist:**
- [ ] Enable secret scanning (where available)  [oai_citation:23‡GitHub Docs](https://docs.github.com/code-security/secret-scanning/about-secret-scanning?utm_source=chatgpt.com)
- [ ] Enable push protection (where available)  [oai_citation:24‡GitHub Docs](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/prevent-future-leaks/enabling-push-protection-for-your-repository?utm_source=chatgpt.com)
- [ ] Document bypass policy (break-glass only; audited) (see “Exceptions” below)

### Dependabot baseline

The `dependabot.yml` file provides fine-grained control over dependency monitoring and updates.  [oai_citation:25‡GitHub Docs](https://docs.github.com/en/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file?utm_source=chatgpt.com)

**Repo baseline checklist:**
- [ ] Enable Dependabot version updates
- [ ] Enable Dependabot security updates
- [ ] Set a sane schedule (weekly is typical; adapt to risk)
- [ ] Group updates where appropriate (reduce PR noise)

### Dependency review (recommended as a required gate)

GitHub’s **dependency review action** scans pull requests for dependency changes and can raise an error if new dependencies have known vulnerabilities.  [oai_citation:26‡GitHub Docs](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configuring-the-dependency-review-action?utm_source=chatgpt.com)

**Repo baseline checklist:**
- [ ] Add a dependency review workflow for PRs
- [ ] Mark the workflow as **required** so vulnerable deps block merges  [oai_citation:27‡GitHub Docs](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/customizing-your-dependency-review-action-configuration?utm_source=chatgpt.com)

---

## 🧾 Contribution workflow

### Issues: required metadata (baseline)

If issue templates are present, include at least:

- **Change type:** code | data | docs | story node | policy
- **Risk level:** low | medium | high
- **Provenance impact:** none | adds lineage | modifies lineage
- **Sensitivity:** public | internal | restricted
- **Requested reviewers:** suggested owners / stewards

> [!NOTE]
> GitHub supports an issue chooser configuration file (`ISSUE_TEMPLATE/config.yml`) to customize templates and contact links.  [oai_citation:28‡GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates?utm_source=chatgpt.com)

### PRs: required checklist (fail-closed intent)

PRs should declare *what* changed and *how* it stays governed.

#### PR must include

- [ ] Scope: which layers/areas changed (Domain / Service / Interface / Infra / Docs / Data)
- [ ] Tests: unit/integration/contract tests added/updated as applicable
- [ ] Provenance: datasets/docs/story nodes include citations / lineage artifacts as needed
- [ ] Security: no secrets committed; workflows follow least privilege
- [ ] Sensitivity: no restricted locations or personal data exposed; governance review requested if unsure

> [!IMPORTANT]
> For KFM, documentation and story content are not “non-code.” They are governed outputs and must be reviewable and traceable.

### Change classification (recommended)

| Change type | Minimum reviewers | Mandatory gates | Extra governance step |
|---|---:|---|---|
| Docs only | 1 | docs-validation | Doc steward if templates/standards touched |
| Code only | 1–2 | ci + security | Architecture review if trust membrane impacted |
| Data ingest / update | 2 | provenance + docs + security | Data steward + license check |
| `.github/workflows/**` | 2 | security + ci | Security steward required |
| Templates/standards | 2 | docs-validation | Governance review label required |

---

## 📦 Data & metadata contract (repo-level)

This section defines the **minimum metadata** expected in GitHub artifacts so KFM can remain auditable.

### Dataset ingest PRs (minimum expectations)

When adding a dataset, the governance model expects:

- Raw files stored as immutable snapshots under `data/raw/`
- A **source manifest (JSON/YAML)** alongside raw data:
  - `source_uri` (or citation)
  - `acquired_at` (date)
  - `license` (spdx id or equivalent; if unknown → “unknown” + governance label)
  - `checksum` (sha256 recommended)
  - `format` / `media_type`
  - `sensitivity` (public/internal/restricted)
- CI validation gates that block merge if required fields are missing (fail-closed intent)

> [!WARNING]
> If license or sensitivity is unclear: do **not** guess. Mark as **unknown** and request governance review.

---

## 🌐 STAC, DCAT & PROV alignment (design target)

KFM is designed to use standards-aligned metadata and lineage (**design target; not confirmed in repo**):

- **STAC** for geospatial items/collections
- **DCAT** for dataset catalog descriptions
- **PROV** for lineage/audit trails (how outputs were produced from inputs)

Repo operations should ensure:

- A dataset does not become UI/API-visible unless its metadata + lineage exist.
- PRs that add/modify datasets also add/modify the relevant catalog/lineage artifacts.

---

## 🧱 Architecture constraints (clean layers + trust membrane)

### Clean layers (enforced by review discipline)

| Layer | Owns | Must NOT do |
|---|---|---|
| Domain | pure entities/models | depend on DB/UI frameworks |
| Use Case / Service | workflows + business rules | talk directly to storage |
| Integration / Interface | ports/contracts + adapters | bypass interfaces to call DBs |
| Infrastructure | real DB/API/UI implementations | embed business rules meant for services |

### Trust membrane rule (non-negotiable)

- External clients and the frontend **never access databases directly**.
- All access routes through the governed API layer where permissions/provenance/business rules apply.

---

## 🧠 Story Node & Focus Mode integration (governed narratives)

Story Nodes are governed narrative documents:

- Authored in Markdown with a strict structure (Template v3, if adopted)
- Include citations for substantive claims
- Are version-controlled and validated in CI before becoming “official content”

Focus Mode is designed to:

- Display narrative content + evidence together
- Surface provenance in the UI (audit panel / info dialogs)
- Constrain AI answers to verified data with citations

> [!IMPORTANT]
> If a Story Node step makes a claim, it must have evidence. If the evidence is unclear, mark it as **not confirmed** and request governance review rather than guessing.

---

## 🧪 Validation & CI/CD (required gates baseline)

KFM’s default posture is “fail-closed.” CI should block merges when any required check fails.

### Recommended CI checks

- **Code quality:** formatting, lint, typecheck
- **Testing:** unit/integration/contract tests
- **Docs validation:** markdown lint + structure/schema validation + link checks
- **Provenance validation:** required metadata/lineage artifacts exist when datasets are changed
- **Security:** secret scanning policy, dependency checks, code scanning (SAST), container scanning (if applicable)

---

## 🧭 Protected paths + CODEOWNERS strategy

GitHub supports requiring review from Code Owners via branch protection settings.  [oai_citation:29‡GitHub Docs](https://docs.github.com/articles/about-code-owners?utm_source=chatgpt.com)

### High-impact paths (baseline)

Treat these as “high impact” areas:

- `.github/workflows/**` (CI supply chain)
- `data/raw/**` (source-of-truth evidence)
- `data/**/prov/**` (lineage/audit trail)
- `docs/templates/**` and `docs/standards/**` (governance contracts)
- `infra/**` (deployment/security posture)
- `api/**` or `server/**` (governed interface boundary; names may vary) (**not confirmed in repo**)

> [!TIP]
> If you don’t yet have GitHub teams, start with a small maintainer set and migrate to teams later. Keep owners minimal.

---

## 🏷️ Labels taxonomy (recommended)

Create labels that encode governance routing:

- `governance-gap` — missing required control/file/check
- `governance-review` — escalation needed (license unclear, sensitive content, provenance incomplete)
- `security` — vulnerabilities / secret exposure / workflow hardening
- `data-ingest` — dataset adds/updates
- `story-node` — narrative request/change
- `policy-change` — templates/standards/governance rules

---

## ⚖️ FAIR+CARE & sensitivity governance

### Sensitivity posture (safe by default)

KFM may contain culturally sensitive or vulnerable information. Repo operations should:

- Prefer **generalization/redaction** over precise sensitive disclosures
- Require governance review for restricted content
- Avoid publishing precise locations of sacred/vulnerable sites in public-facing docs

### Governance escalation triggers

Apply a governance review label when:

- Provenance is incomplete
- A dataset license is unclear
- Story content touches sensitive cultural knowledge
- A change alters templates/standards or access policy
- A change affects `.github/workflows/**` or CI supply chain

---

## 🧯 Exceptions (“break-glass”) process (auditable overrides)

> [!IMPORTANT]
> Emergency work happens. Governance still applies. The goal is not “no exceptions,” it’s **auditable exceptions**.

### When break-glass is allowed

- Active secret leak response (rotation + containment)
- Critical vulnerability patch with known exploit risk
- Production outage mitigation (if this repo deploys runtime)

### Break-glass requirements

- [ ] Open an issue labeled `break-glass` with: reason, scope, rollback plan
- [ ] PR must reference the issue
- [ ] Minimum 1 approver (Security steward for security events)
- [ ] Post-incident follow-up PR: restore normal controls + add missing tests/docs/metadata

---

## 🕰️ Version history

| Version | Date | Summary | Author | Review Notes |
|---:|---|---|---|---|
| v0.2.0 | 2026-02-10 | Added controls matrix, repo settings baseline, supply-chain gates, and break-glass workflow (baseline doc update) | @TBD | Ensure required checks match workflow job names (**not confirmed in repo**) |
| v0.1.0 | YYYY-MM-DD | Initial governed `.github/README.md` baseline for KFM repo operations | @TBD | Align with current CI + governance policies |

---

## 📎 Appendix — starter stubs (copy into separate files)

> [!NOTE]
> These are scaffolds. Treat them as governed artifacts when adopted.

<details>
<summary><strong>SECURITY.md (starter stub)</strong></summary>

```markdown
# Security Policy

## Supported Versions
- **main**: supported
- release branches/tags: (define if applicable)

## Reporting a Vulnerability
Please **do not** open a public issue for suspected vulnerabilities.

- Use GitHub’s private vulnerability reporting (if enabled), or
- Email: **security@TBD** (not confirmed)

Include:
- description + impact
- steps to reproduce
- affected paths/versions
- suggested fix (if known)

## Disclosure Process
- Triage within **TBD** business days (not confirmed)
- Patch development in private
- Coordinated disclosure after fix is released
```

</details>

<details>
<summary><strong>CODEOWNERS (starter stub)</strong></summary>

```text
# High-impact paths
.github/workflows/ @kfm-maintainers @kfm-security-stewards
.github/          @kfm-maintainers

data/raw/         @kfm-data-stewards
data/**/prov/     @kfm-data-stewards

docs/templates/   @kfm-doc-stewards @kfm-governance-stewards
docs/standards/   @kfm-doc-stewards @kfm-governance-stewards
```

</details>

<details>
<summary><strong>ISSUE_TEMPLATE/config.yml (starter stub)</strong></summary>

```yaml
blank_issues_enabled: false
contact_links:
  - name: Security vulnerability report
    url: https://github.com/<ORG>/<REPO>/security/advisories/new
    about: "Report security issues privately (preferred)."
  - name: Governance & sensitivity questions
    url: https://github.com/<ORG>/<REPO>/discussions
    about: "Ask before publishing sensitive material."
```

</details>