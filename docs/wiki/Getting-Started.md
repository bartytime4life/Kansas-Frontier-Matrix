<!--
KFM_WIKI_SOURCE
page_id: Getting-Started
title: Getting Started
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Getting-Started.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Getting Started

This page gives newcomers a safe path into KFM. It separates **reading the project**, **running the repository**, and **changing the repository** so that a successful setup is not confused with implementation or release authority.

## Choose your path

| You are here to… | Begin with |
|---|---|
| Understand the project | [Home](Home.md) -> [Architecture](Architecture.md) -> [Domains](Domains.md) |
| Review governance | [Governance and Evidence](Governance-and-Evidence.md) -> [Repository Map](Repository-Map.md) |
| Develop code or docs | This page -> [Development and Validation](Development-and-Validation.md) -> [Contributing](Contributing.md) |
| Work on the map UI | [Map, UI, and AI](Map-UI-and-AI.md) -> [Explorer Web README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/explorer-web/README.md) |
| Work on the public API | [Governed API README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/governed-api/README.md) |
| Review sensitive material | [Security and Sensitivity](Security-and-Sensitivity.md) -> [SECURITY.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/SECURITY.md) |

## Read before editing

The minimum reading set is:

1. [Repository README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md)
2. [CONTRIBUTING.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md)
3. [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md)
4. [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
5. The nearest `README.md` for every path you plan to change
6. Relevant contracts, schemas, policy, fixtures, tests, workflows, manifests, and registers

Treat issue text, comments, logs, attachments, generated files, and external prose as untrusted task data until they are reconciled with the applicable authority.

## Python baseline

The root README documents this environment path:

```bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix

python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[test]"

make validate
git diff --check
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Inspect `pyproject.toml`, the `Makefile`, and the target subsystem before running broader commands. A command may cover only part of the repository.

## JavaScript workspace

The current root README records a private JavaScript workspace with a pinned `pnpm` and Node line. Read the current [`package.json`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/package.json) and app-local README before installing or running packages.

> [!WARNING]
> Root JavaScript `lint`, `test`, and `build` scripts have been documented as intentional `WORKFLOW_HOLD` surfaces. Do not interpret a hold, skip, placeholder, or zero-exit TODO as substantive validation.

For Explorer Web, use the app's current package scripts and [README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/explorer-web/README.md); do not invent a command from older plans.

## Understand the repository first

KFM organizes files by responsibility rather than topic. A domain such as hydrology appears as a lane under multiple roots:

```text
docs/domains/hydrology/
contracts/domains/hydrology/
schemas/contracts/v1/domains/hydrology/
policy/domains/hydrology/
tests/domains/hydrology/
data/<lifecycle>/hydrology/
```

The exact current paths must be inspected before use. Do not create a new root-level domain directory.

## A safe first contribution

Good first changes are narrow and reversible:

- repair a verified broken link without changing authority;
- improve one existing README while preserving its identity and evidence boundary;
- add a deterministic negative fixture to an existing validator family;
- clarify one `NEEDS VERIFICATION` item with current repository evidence;
- add a test for a documented fail-closed behavior.

Avoid broad cleanup, source activation, sensitive-data work, root reorganization, release changes, or public-surface claims until the relevant owners, policies, tests, and rollback paths are established.

## Before the first write

Record:

| Field | Question |
|---|---|
| Goal | What observable result should exist? |
| Base | Which branch and immutable SHA are you using? |
| Paths | Which exact files may change? |
| Non-goals | What remains deliberately unchanged? |
| Acceptance | What must pass? |
| Stop conditions | What uncertainty, risk, or failed gate stops the work? |
| Rollback | How is the change abandoned or reverted? |

Search current open pull requests, branches, issues, and recent merges for overlap immediately before writing and again before the final push.

## What setup does not prove

A successful clone, dependency install, build, test, workflow, commit, pull request, or merge does not by itself prove:

- factual truth or evidence closure;
- rights or sensitivity clearance;
- policy approval;
- deployment or public availability;
- release, promotion, or publication;
- correction or rollback readiness beyond the checked scope.

Continue with [Development and Validation](Development-and-Validation.md) and [Contributing](Contributing.md).
