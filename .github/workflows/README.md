<a id="top"></a>

# 🧰 `.github/workflows/` — CI/CD for Kansas Frontier Matrix (KFM)

<div align="left">

<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/ci.yml/badge.svg" /></a>
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml"><img alt="CodeQL" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg" /></a>
<a href="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml"><img alt="Pages" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pages.yml/badge.svg" /></a>

<img alt="KFM-MDP" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-5865F2" />
<img alt="Master Guide" src="https://img.shields.io/badge/Master%20Guide-v13%20(draft)-f59e0b" />
<img alt="Provenance" src="https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1" />
<img alt="Policy as Code" src="https://img.shields.io/badge/policy-Conftest%20%2B%20Rego-0ea5e9" />
<img alt="Supply Chain" src="https://img.shields.io/badge/supply%20chain-SBOM%20%2B%20Attestations-111827" />
<img alt="DevSecOps" src="https://img.shields.io/badge/DevSecOps-enabled-black" />
<img alt="CI" src="https://img.shields.io/badge/CI-boring%20by%20design-success" />

</div>

> 🧭 This folder contains GitHub Actions workflows that keep KFM **buildable**, **testable**, **secure**, and **shippable** — across **pipelines → catalogs → graph → API → UI → stories → (optional) agent automation**.
>
> ✅ **North Star:** CI/CD protects *trust* (provenance + integrity + policy) first, then *speed* (caching + change-aware gates).  
> 🚦 **KFM order (don’t break it):** **ETL → Metadata (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**.

> [!IMPORTANT]
> CI is intentionally **boring** (predictable, repeatable, least‑privilege, auditable).  
> The data, stories, and models are the interesting part. 🗺️✨

---

## 📘 Overview

### 🎯 Purpose
Make it hard to accidentally ship untraceable, unsafe, or broken artifacts — and easy to ship verified, reproducible ones.

CI/CD in KFM exists to enforce:
- ✅ **contracts** (schemas + IDs + API boundaries)
- ✅ **integrity** (provenance + checksums + attestations)
- ✅ **governance** (FAIR + CARE, sensitive-location rules, licensing discipline)
- ✅ **repeatability** (deterministic runs, idempotent pipelines)
- ✅ **operational safety** (kill-switch + env-gated promotion)

### 🧩 Scope
| In scope ✅ | Out of scope ❌ |
|---|---|
| GitHub Actions workflows under `📁 .github/workflows/` | Production runbooks for cloud infra *(belongs in `docs/`)* |
| Reusable workflows (`workflow_call`) and composite actions usage | Writing OPA/Rego policy logic *(belongs in `tools/validation/policy/`)* |
| CI gate triggers, artifacts, and promotion semantics | Detailed dataset metadata requirements *(belongs in STAC/DCAT/PROV docs)* |
| Supply-chain posture (SBOM + attestations) | End-user UI docs *(belongs in `web/` or `docs/`)* |

### 👥 Audience
- **Primary:** maintainers and contributors editing workflows, validators, or release/promotion lanes  
- **Secondary:** reviewers verifying governance + supply-chain compliance, and anyone debugging CI failures

### 🧠 Definitions
- **PR lane:** fast checks required for merge (lint/tests/fast metadata/policy gates)
- **Scheduled lane:** heavier checks run on cron or manual dispatch (integration + deep schema validation)
- **Promotion:** governed publish step (env-gated, atomic, audit-friendly; *not* “copy files somewhere”)
- **Fail-closed:** if a promotion-critical rule fails, publishing must stop
- **Governed surface:** paths that can affect public trust (e.g., `data/**`, `docs/**`, `.github/**`, policy rules)

---

## 🧾 Workflow policy metadata

| Field | Value |
|---|---|
| Folder | `.github/workflows/` |
| Status | Active ✅ |
| Last updated | **2026-01-10** |
| KFM-MDP baseline | **v11.2.6** |
| Master Guide | **v13 (draft)** |
| Governance | FAIR + CARE (data + people) |
| CI philosophy | PR-fast lane + scheduled heavy lanes + env-gated promotion 🚦 |
| Runner baseline | `ubuntu-latest` (pin images for hermetic lanes) 🐧 |
| “Least privilege” | Default `permissions: { contents: read }` 🔐 |
| “PR-first promotion” | Promotion happens via **signed PRs**, not direct pushes 🧾 |

---

## ⚡ Quick links

| Action | Link |
|---|---|
| ✅ All Action runs | [GitHub Actions](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions) |
| 📦 Releases | [Releases](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases) |
| 🐛 Issues | [Issues](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues) |
| 🤝 `.github/` Collaboration hub | [`../README.md`](../README.md) |
| 🧭 Repo root overview | [`../../README.md`](../../README.md) |
| 🔐 Security policy | [`../../SECURITY.md`](../../SECURITY.md) *(or `../SECURITY.md` if canonical is inside `.github/`)* |

> [!TIP]
> If a badge 404s, that workflow file probably doesn’t exist yet.  
> This README doubles as a **spec + target shape** — update it as you implement workflows to avoid drift. 🧾✅

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [📺 Mermaid Workflow TV](#mermaid-workflow-tv)
- [🧠 CI/CD principles](#cicd-principles)
- [🧬 KFM invariants CI must enforce](#kfm-invariants-ci-must-enforce)
- [📁 What lives here](#what-lives-here)
- [🗂️ Workflow catalog](#workflow-catalog)
- [🚦 Change-aware gate matrix](#change-aware-gate-matrix)
- [🧱 Promotion gates](#promotion-gates)
- [🧑‍⚖️ Policy as code gates](#policy-as-code-gates)
- [🧯 Kill-switch](#kill-switch)
- [🤖 Agent automation lane](#agent-automation-lane)
- [🗺️ Data + catalog gates](#data--catalog-gates)
- [🕸️ Graph + semantics gates](#graph--semantics-gates)
- [🎬 Story Nodes + Focus Mode gates](#story-nodes--focus-mode-gates)
- [🧪 Integration tests](#integration-tests)
- [🌐 Web UI gates](#web-ui-gates)
- [📈 Modeling + simulation gates](#modeling--simulation-gates)
- [⚡ Performance gates](#performance-gates)
- [🔐 Security scanning](#security-scanning)
- [📦 Artifacts & traceability](#artifacts--traceability)
- [🧷 Secrets & environments](#secrets--environments)
- [🧩 Reusable workflows & composite actions](#reusable-workflows--composite-actions)
- [🛠️ Starter templates](#starter-templates)
- [🧰 Debug locally](#debug-locally)
- [🧾 Adding a new workflow checklist](#adding-a-new-workflow-checklist)
- [✅ Definition of Done (for this document)](#definition-of-done-for-this-document)

</details>

---

<a id="mermaid-workflow-tv"></a>

## 📺 Mermaid Workflow TV

A “TV guide” of how work moves through KFM CI/CD (PR fast lane → scheduled heavy lanes → env-gated publish). 📺🧪

```mermaid
flowchart TB
  subgraph PR["🧪 PR Lane (fast • required)"]
    PR1["ci.yml<br/>lint • unit • typecheck"]
    PR2["ui.yml<br/>web lint • test • build"]
    PR3["catalog-qa.yml<br/>STAC/DCAT quick gate"]
    PR4["policy-gate.yml<br/>Conftest/Rego (FAIR+CARE)"]
    PR5["docs.yml<br/>markdown/link checks (optional)"]
    PR6["actionlint.yml<br/>workflow lint (recommended)"]
  end

  subgraph SCHEDULE["🌙 Scheduled Lane (slow • trusted)"]
    N1["integration.yml<br/>PostGIS + graph + API contracts"]
    N2["stac-validate.yml<br/>full STAC schema lane"]
    N3["dcat-validate.yml<br/>DCAT lane"]
    N4["prov-validate.yml<br/>PROV lane"]
    N5["perf.yml<br/>bundle + query budgets"]
    N6["model-regression.yml<br/>metrics + reproducibility checks"]
  end

  subgraph PROMOTE["🚦 Promotion Lane (env-gated)"]
    P1["publish-catalog.yml<br/>atomic publish + catalogs"]
    P2["docker.yml<br/>build/push images (GHCR)"]
    P3["pages.yml<br/>docs/viewer deploy (optional)"]
  end

  subgraph RELEASE["🏷️ Release Lane (tags)"]
    R1["release.yml<br/>release assets + notes"]
    R2["sbom.yml<br/>SBOM generation"]
    R3["attest.yml<br/>SLSA/Sigstore attestations"]
    R4["scorecard.yml<br/>OpenSSF scorecard (optional)"]
  end

  subgraph AGENTS["🤖 Agent Lane (optional)"]
    A1["agents-watcher.yml<br/>read-only signals"]
    A2["agents-planner.yml<br/>deterministic plans"]
    A3["agents-executor.yml<br/>PR-only executor (no merge)"]
    A4["detect-validate-promote.yml<br/>ETag/changes → lanes → signed PR"]
  end

  PR1 --> SCHEDULE
  PR3 --> P1
  PR4 --> P1
  SCHEDULE --> P1
  P1 --> RELEASE
  P2 --> RELEASE
  AGENTS --> PR
