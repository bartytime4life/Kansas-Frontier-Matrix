<!--
GOVERNED ARTIFACT NOTICE
This README lives inside the KFM trust boundary: it documents non‑negotiable invariants
and how GitHub automation enforces them.
If you change meaning (not just phrasing), route through the governance review path.
-->

<div align="center">

# Kansas Frontier Matrix (KFM‑NG) — GitHub Operations & Governance Gates 🧭🗺️

**This folder is the GitHub “front door” for KFM‑NG engineering: workflows, templates, and CI gates.**  
For the system overview, start with **[README.md](../README.md)**.

<br/>

![Status](https://img.shields.io/badge/status-governed%20draft-blue)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-informational)
![Trust membrane](https://img.shields.io/badge/trust%20membrane-API%20%2B%20policy%20boundary-success)
![Policy](https://img.shields.io/badge/policy-OPA%20default%20deny-black)
![Catalogs](https://img.shields.io/badge/catalogs-STAC%20%7C%20DCAT%20%7C%20PROV-6a5acd)
![Focus Mode](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-critical)

<!-- OPTIONAL: replace ORG/REPO with real values once workflows exist -->
<!--
[![CI](https://github.com/ORG/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/ci.yml)
[![Docs](https://github.com/ORG/REPO/actions/workflows/docs.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/docs.yml)
[![Policy](https://github.com/ORG/REPO/actions/workflows/policy.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/policy.yml)
[![Data Gates](https://github.com/ORG/REPO/actions/workflows/data-gates.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/data-gates.yml)
-->

</div>

> [!IMPORTANT]
> KFM‑NG is designed around a **trust membrane** (governed API + policy boundary).  
> **UI/external clients never talk to databases.** Every request is evaluated by policy and **fails closed**.
>
> In CI terms: **if the gates cannot prove “allowed,” the change does not ship.**

---

## Table of Contents

- [What This Folder Is For](#what-this-folder-is-for)
- [Non-Negotiable Guarantees (Release Blockers)](#non-negotiable-guarantees-release-blockers)
- [What Lives in `.github/`](#what-lives-in-github)
- [CI Workflows and Gates](#ci-workflows-and-gates)
- [Running the Gates Locally](#running-the-gates-locally)
- [Governed Change Types](#governed-change-types)
- [Pull Request Checklist](#pull-request-checklist)
- [Security Notes](#security-notes)

---

## What This Folder Is For

This folder exists to make governance **enforceable**:

- CI workflows that validate **governed artifacts** (docs, Story Nodes, catalogs, policies)
- Issue/PR templates that force provenance and review discipline
- “Default deny” behavior encoded as policy tests and build gates

For the end-to-end system architecture (data → pipeline → catalogs → APIs → Focus Mode + UI), see **[README.md](../README.md)**.

---

## Non-Negotiable Guarantees (Release Blockers)

These invariants are enforced by design and must be protected by CI gates.

| Invariant | What it means | Minimum enforcement (CI/infra) |
|---|---|---|
| **Trust membrane** | UI/external clients never access databases directly; all access goes through the **governed API + policy boundary** | Network isolation + gateway + contract tests |
| **Fail-closed policy** | If policy cannot prove a request is allowed, **deny** | OPA `default deny` + regression tests |
| **Dataset promotion gates** | Only promoted datasets can serve production queries | Checksums + STAC/DCAT/PROV validation |
| **Focus Mode: cite or abstain** | Every answer returns citations + an audit reference | Output validator + policy rule |
| **Processed zone is source of truth** | Production APIs serve only validated/processed artifacts | Serving config + catalog-backed queries |

> [!WARNING]
> Any change that weakens one of the invariants above should be treated as a **release blocker** until governance review approves it.

---

## What Lives in `.github/`

```text
.github/
├── README.md                  # (this file) GitHub ops + CI gates
├── workflows/                 # GitHub Actions
│   ├── ci.yml
│   ├── docs.yml
│   ├── policy.yml
│   └── data-gates.yml
├── ISSUE_TEMPLATE/            # issue forms/templates
└── PULL_REQUEST_TEMPLATE.md   # PR checklist + governance prompts
```

> [!NOTE]
> If you are using the GitHub **organization profile README**, GitHub expects `./profile/README.md` in the special `.github` repository.  
> This file is still useful as an engineering “front door” even when not used as the org profile.

---

## CI Workflows and Gates

### Workflows (recommended mapping)

| Workflow | Primary responsibility | Typical failure means |
|---|---|---|
| `ci.yml` | Build + unit tests + formatting/lint | Code changes broke contracts or style |
| `docs.yml` | Markdown lint + link check + governed doc validation | Docs are malformed, broken links, or missing required headings |
| `policy.yml` | `opa test` + policy schema validation | Policy no longer fails closed or rules regress |
| `data-gates.yml` | Dataset promotion gates (raw → work → processed) | Missing license/sensitivity, checksum mismatch, or catalog invalid |

### Gate philosophy

- Treat **data/catalog validation** as “tests,” not “best effort.”
- Treat policy regressions as **security regressions**.
- Prefer small PRs that keep failures legible.

<details>
<summary><strong>Definition of Done for “governed CI”</strong></summary>

- [ ] Docs validators run on every PR and block merge on failure
- [ ] Policy tests run on every PR and block merge on failure
- [ ] Data gates run on every PR that touches `data/**` or `data/catalog/**`
- [ ] Governed templates are versioned and validated (Story Nodes, catalogs, contracts)
- [ ] A PR cannot merge without proving compliance (fail closed)

</details>

---

## Running the Gates Locally

> [!NOTE]
> Commands below are template-friendly. Replace with your actual Make targets once in-repo.

```bash
# Typical local checks
make lint
make test
make policy-test
make docs-validate
make data-validate
```

If you don’t have Make targets yet, align your local scripts to the workflows so CI behaves predictably.

---

## Governed Change Types

Some changes are “just code.” Others change the system’s truth surface.

### Changes that require governance review

- **Policy changes** (OPA/Rego), especially allow/deny behavior
- **Catalog schema changes** (STAC/DCAT/PROV profiles)
- **Story Node template/schema changes**
- **Evidence resolver behavior** (what counts as a citation, what must be resolvable)
- **Sensitivity handling rules** (redaction/generalization behavior)

> [!IMPORTANT]
> If a change alters **meaning**, it must be reviewed as a governed artifact change, not a routine refactor.

---

## Pull Request Checklist

- [ ] I did **not** introduce UI → DB direct access (trust membrane preserved)
- [ ] Policy still **fails closed** (OPA tests pass)
- [ ] If I touched governed artifacts, validators pass (docs/stories/catalogs/contracts)
- [ ] If I changed data, checksums + promotion gate outputs are present
- [ ] I added/updated tests appropriate to the layer (domain/usecase/integration/infrastructure)
- [ ] I documented contract changes (ADR or contract doc update)

---

## Security Notes

- Secrets must never be committed to Git.
- Workflows should use least-privilege tokens.
- Treat governance as part of security: policy + provenance + sensitivity must agree.

<div align="center">

**KFM Principle:** *If it can’t be traced, it can’t be trusted.* 🔎

</div>
