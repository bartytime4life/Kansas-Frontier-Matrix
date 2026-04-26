<!-- [KFM_META_BLOCK_V2]
doc_id: TODO: assign kfm://doc/<uuid>
title: Documentation Hub
type: standard
version: v1
status: draft
owners: TODO: verify owner
created: TODO: YYYY-MM-DD
updated: 2026-04-26
policy_label: TODO: verify policy label
related: [docs/runbooks/repository-next-steps.md, docs/runbooks/markdown-debt-backlog.md, docs/adr/]
tags: [kfm, documentation, repository-navigation, governance]
notes: [Structure date was supplied as verified on 2026-04-26; re-check the live repository tree before relying on implementation, CI, runtime, or release-state claims.]
[/KFM_META_BLOCK_V2] -->

# Documentation Hub

Operational and reference documentation for the repository, organized for evidence-bounded navigation, governance, and review.

<p align="center">
  <img alt="Status: active supplied" src="https://img.shields.io/badge/status-active--supplied-lightgrey">
  <img alt="Evidence: bounded" src="https://img.shields.io/badge/evidence-bounded-blue">
  <img alt="Policy: cite or abstain" src="https://img.shields.io/badge/policy-cite--or--abstain-orange">
  <img alt="Review: needs verification" src="https://img.shields.io/badge/review-NEEDS_VERIFICATION-lightgrey">
</p>

<p align="center">
  <a href="#scope">Scope</a> ·
  <a href="#repo-fit">Repo fit</a> ·
  <a href="#inputs">Inputs</a> ·
  <a href="#exclusions">Exclusions</a> ·
  <a href="#directory-structure">Directory structure</a> ·
  <a href="#start-here">Start here</a> ·
  <a href="#validation">Validation</a>
</p>

> [!IMPORTANT]
> This page is a documentation hub, not implementation proof. Re-check the live repository tree before using this file to make implementation, CI, runtime, deployment, route, schema, workflow, release, or test-state claims.

| Field | Value |
|---|---|
| Status | `active` from supplied documentation context; live repo status `NEEDS_VERIFICATION` |
| Owners | `TODO: verify owner` |
| Evidence mode | `Supplied structure; live repository tree not re-checked by this file` |
| Policy label | `TODO: verify policy label` |
| Repo fit | Target path: `docs/README.md` |
| Upstream | `[Repository root](../README.md)` — `NEEDS_VERIFICATION` |
| Downstream | [`adr/`](adr/), [`architecture/`](architecture/), [`domains/`](domains/), [`registers/`](registers/), [`runbooks/`](runbooks/), [`sources/`](sources/), [`standards/`](standards/) |
| Public posture | Cite-or-abstain; fail closed on unresolved rights, sensitivity, review state, or implementation evidence |

## Scope

This directory contains repository documentation that helps maintainers and contributors understand how KFM work is organized, governed, reviewed, and maintained.

Use `docs/` for human-readable guidance, including:

- architecture decision records
- system and subsystem architecture notes
- domain-lane documentation
- registers, indexes, and ledgers
- runbooks and remediation procedures
- source-facing documentation
- documentation standards and conventions

## Repo fit

`docs/` is the repository’s documentation hub. It explains repository behavior, governance expectations, review posture, source discipline, and operator workflows.

| Relationship | Path | Role |
|---|---|---|
| Parent | `../` | Repository root. |
| Hub | `docs/` | Documentation navigation and governance-facing prose. |
| Decisions | [`docs/adr/`](adr/) | Architecture-impacting decisions and authority changes. |
| Operations | [`docs/runbooks/`](runbooks/) | Execution, remediation, review, and operator procedures. |
| Standards | [`docs/standards/`](standards/) | Shared documentation conventions and writing rules. |

> [!NOTE]
> Links in this page are relative to `docs/README.md`. Verify the root README and all downstream paths before committing.

## Inputs

Documentation belongs here when it helps a maintainer, contributor, steward, reviewer, or operator understand repository intent, workflow, governance, or evidence posture.

Accepted inputs include:

| Input | Belongs here when |
|---|---|
| ADRs | A decision changes folder authority, governance rules, schema homes, major workflows, or other architecture-impacting boundaries. |
| Architecture notes | A subsystem, surface, or domain lane needs human-readable design explanation. |
| Domain docs | A KFM lane needs scope, source-role, policy, validation, release, or correction guidance. |
| Registers | A ledger, index, source map, document map, or inventory needs to remain reviewable. |
| Runbooks | A maintainer needs repeatable execution, remediation, verification, or rollback guidance. |
| Source-facing docs | A source family, intake path, or source-role rule needs explanation. |
| Standards | Documentation rules, Markdown conventions, truth labels, or review expectations need a stable home. |

## Exclusions

Do not use `docs/` as a substitute for authoritative implementation surfaces.

| Do not place here as authoritative truth | Use instead |
|---|---|
| Machine-readable schemas or contracts | `TODO: verify schema/contract home` |
| Policy-as-code rules | `TODO: verify policy home` |
| Runtime configuration | `TODO: verify config/deployment home` |
| CI workflow definitions | `TODO: verify workflow home` |
| Generated receipts, proof packs, or release artifacts | `TODO: verify receipts/proofs/release homes` |
| RAW, WORK, QUARANTINE, or unpublished source data | `TODO: verify governed data lifecycle paths` |
| Secrets, credentials, private endpoints, or tokens | Never commit to docs, fixtures, prompts, or examples. |

> [!WARNING]
> Documentation may explain contract, policy, schema, runtime, and release behavior, but it must not imply implementation maturity that has not been verified from repository files, tests, workflows, logs, manifests, generated artifacts, or runtime evidence.

## Directory structure

The structure below was supplied as verified on **2026-04-26**.

```text
docs/
├── adr/
├── architecture/
├── domains/
├── registers/
├── runbooks/
├── sources/
└── standards/
