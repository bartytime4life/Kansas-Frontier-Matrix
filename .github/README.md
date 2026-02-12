# `.github` — Governance, Community Health, and Automation 🧭🛡️

> [!NOTE]
> This folder holds **GitHub-specific** “community health” files and automation for the **Kansas Frontier Matrix (KFM)** repo.
> If anything in this document diverges from actual workflows/templates in the repo, **treat this README as the source to update next** (not the source of truth by itself).

---

## Quick Links

- **Open an issue** → use the templates in `.github/ISSUE_TEMPLATE/`
- **Open a PR** → follow `.github/PULL_REQUEST_TEMPLATE.md` (and the checklists below)
- **Security** → see `.github/SECURITY.md` (do **not** file vulnerabilities publicly)

---

## What Lives in `.github/`

| Path | Purpose | Notes |
|---|---|---|
| `.github/README.md` | This file | How we use GitHub for governance + operations |
| `.github/workflows/` | CI / policy gates / automation | Contract tests, linting, security scans, provenance checks |
| `.github/ISSUE_TEMPLATE/` | Issue + intake templates | Bug, feature, data intake, governance review, story node |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR “Definition of Done” | Evidence-first + checks required |
| `.github/CODEOWNERS` | Review routing | Enforces domain ownership |
| `.github/SECURITY.md` | Vulnerability reporting | Private reporting instructions |
| `.github/dependabot.yml` | Dependency update automation | Optional but recommended |
| `.github/labels.yml` | Label taxonomy (optional) | Helpful for consistent triage |

> [!TIP]
> Keep automation “boring”: **small workflows**, **clear names**, **fast feedback**, and **fail-closed** on governance gates.

---

## Governance Principles (KFM)

KFM is a governed geospatial/historical knowledge system (data → pipeline → APIs → UI/Focus Mode).  
This `.github` layer is where we translate governance into **repeatable checks**.

### Evidence-First (Non-negotiable)

Every substantive PR must include **at least one** evidence pointer:

- Dataset/catalog identifier (e.g., STAC/DCAT/PROV object ID)
- Document path (e.g., `docs/...`), schema path, or contract path
- Commit hash / release tag / artifact digest
- Test proving behavior change

> [!IMPORTANT]
> If you cannot provide evidence, label the change **“proposal”** and route it to governance review.

### FAIR + CARE + Sensitivity

Some content may be sensitive (e.g., precise locations, culturally restricted knowledge).  
When in doubt:

- **Generalize / redact** precise coordinates or sensitive attributes
- Add a **governance review** note in the PR
- Prefer “need-to-know” exposure in UI and APIs

---

## Architecture Invariants (Trust Membrane + Clean Layers)

### Trust Membrane Rule

- **Frontends and external clients never access databases directly.**
- All access must go through the **governed API layer**.

### Clean Architecture Boundaries

- **Domain**: pure entities/models (no DB/UI)
- **Use Case / Service**: workflows + business rules via interfaces
- **Integration & Interface**: ports/contracts/adapters (API boundaries)
- **Infrastructure**: storage, queues, web servers, deployment

```mermaid
flowchart TB
  subgraph Clients
    UI[React/MapLibre UI]
    Ext[External Clients]
  end

  subgraph Governed_API["Governed API Gateway (Trust Membrane)"]
    API[REST/GraphQL/API Layer]
    Policy[Policy Enforcement (OPA/Rego, etc.)]
    Audit[Audit + Provenance Logging]
  end

  subgraph DataPlane["Data Plane"]
    PG[(PostGIS/PostgreSQL)]
    Graph[(Graph DB)]
    Obj[(Object/Artifact Store)]
  end

  UI --> API
  Ext --> API
  API --> Policy
  API --> Audit
  API --> PG
  API --> Graph
  API --> Obj
```

> [!IMPORTANT]
> If a change bypasses repository interfaces to talk directly to storage, it violates the architecture.

---

## Contribution Workflow

### Issues

Use the templates. At minimum, include:

- **What happened / what you expected**
- **Reproduction steps**
- **Evidence** (logs, dataset IDs, query, provenance pointer)
- **Scope** (domain, UI, API, pipeline, docs)

### Pull Requests

All PRs should be small, reviewable, and reversible.

```mermaid
flowchart LR
  A[Branch] --> B[PR Opened]
  B --> C[CI: Lint + Tests]
  C --> D[CI: Governance Gates]
  D --> E[Review + Approvals]
  E --> F[Merge]
  F --> G[Release/Publish (if applicable)]
```

---

## CI Quality Gates (Recommended Baseline)

> [!NOTE]
> Exact workflow filenames vary by repo. Keep the *intent* stable even if implementation changes.

| Gate | What it Protects | Typical Failure Mode | Fix |
|---|---|---|---|
| Format/Lint | Consistency, fast review | Style drift | Run formatter + lint |
| Unit/Integration Tests | Behavioral correctness | Regression | Add/repair tests |
| Contract/API Checks | Trust membrane + API stability | Breaking schema | Update contract + versioning |
| Docs Lint/Link Check | CI-ready docs | Broken anchors/links | Fix references |
| License/CARE Checks | Legal/ethical governance | Unknown license | Add metadata + review |
| Security Scans | Supply chain + code safety | Vulnerable deps | Patch/bump deps |
| Provenance Checks | Traceability/audit | Missing IDs/digests | Add provenance index pointers |

---

## PR Definition of Done ✅

### Required (All PRs)

- [ ] Linked issue (or explain why not)
- [ ] Clear scope (Domain / Use Case / Integration / Infra / UI)
- [ ] Tests added/updated (or “no test needed” justification)
- [ ] Docs updated (if behavior/contract changes)
- [ ] No secrets committed (keys, tokens, credentials)
- [ ] Governance notes included if sensitive data is involved
- [ ] All required CI checks pass

### If You Touch Data Pipelines

- [ ] Data license confirmed + recorded
- [ ] Deterministic IDs/digests preserved
- [ ] QA/validation artifacts generated
- [ ] Provenance updated (inputs → transforms → outputs)
- [ ] Rollback plan documented

---

## Label Taxonomy (Suggested)

| Label | Meaning | Typical Owner |
|---|---|---|
| `domain:*` | Domain model/spec changes | Domain owner |
| `pipeline:*` | Ingestion/transforms/catalog | Data engineering |
| `api:*` | API contracts and services | API team |
| `ui:*` | React/Map UI/Focus Mode | UI team |
| `governance` | Needs policy review | Governance group |
| `security` | Security-relevant | Security owner |
| `docs` | Documentation-only | Docs owner |

---

## Security

> [!WARNING]
> **Do not** disclose vulnerabilities in public issues/PRs.

- Follow `.github/SECURITY.md` for reporting
- Treat credentials as compromised if exposed
- Rotate keys and invalidate tokens immediately (maintainers)

---

## Expected Repository Layout (Informational)

> [!NOTE]
> This is a **typical** KFM-style monorepo layout. Confirm against the actual repo and adjust.

```text
.github/
  workflows/
  ISSUE_TEMPLATE/
  PULL_REQUEST_TEMPLATE.md
docs/
src/
web/
data/
```

---

## Maintainers: Keep This Folder Healthy

- Prefer **explicit workflow names** and stable check IDs (so branch protection remains consistent)
- Keep “policy-as-code” rules versioned and reviewed
- Regularly prune stale templates/labels
- Document any “break glass” procedures (incident response, rollback)

<details>
<summary><strong>Maintainer Checklist (Quarterly)</strong></summary>

- [ ] Review CI runtime + flakiness
- [ ] Update dependency automation (Dependabot/Renovate)
- [ ] Revisit label taxonomy + CODEOWNERS
- [ ] Audit security reporting instructions
- [ ] Validate docs link-check remains green
- [ ] Ensure governance gates still match policy

</details>

---

## Reference Pointers (Project Docs)

- KFM architecture and governance docs (see `docs/` and root project guides)
- Documentation formatting and CI expectations (see docs style guide materials)

> [!TIP]
> Keep this `.github/README.md` short and operational. Put deeper system design in `docs/` and keep links stable.