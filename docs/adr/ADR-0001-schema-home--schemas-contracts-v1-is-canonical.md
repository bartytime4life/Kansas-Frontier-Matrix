<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0001-schema-home
title: ADR-0001 — Schema Home: `schemas/contracts/v1/` is Canonical
type: adr
adr_id: ADR-0001
adr_status: accepted
version: v1
status: published
owners: Architecture Steward · Schema Steward · Docs Steward
created: 2026-04-21
updated: 2026-05-09
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/architecture/contract-schema-policy-split.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - control_plane/object_family_register.yaml
  - control_plane/deprecation_register.yaml
tags: [kfm, adr, governance, schemas, contracts, directory-rules]
notes:
  - Live-repo enforcement state is NEEDS VERIFICATION per Directory Rules §18.
  - Domain schema-home ADRs (archaeology, fauna, flora, habitat, geology, atmosphere, hydrology, settlements, infrastructure, hazards, agriculture, people-dna-land) descend from this decision.
[/KFM_META_BLOCK_V2] -->

# ADR-0001 — Schema Home: `schemas/contracts/v1/` is Canonical

> The default home for **machine-checkable schemas** in KFM is `schemas/contracts/v1/<family>/...`. `contracts/` retains **semantic Markdown** only. Two homes for the same authority is the single most expensive drift in the repository, and this ADR closes that question.

<p>
  <img alt="ADR" src="https://img.shields.io/badge/ADR-0001-1f6feb?style=flat-square">
  <img alt="Status: Accepted" src="https://img.shields.io/badge/status-accepted-2ea043?style=flat-square">
  <img alt="Authority: Canonical" src="https://img.shields.io/badge/authority-canonical-8957e5?style=flat-square">
  <img alt="Schema home: schemas/contracts/v1" src="https://img.shields.io/badge/schema--home-schemas%2Fcontracts%2Fv1-0969da?style=flat-square">
  <img alt="Enforcement: NEEDS VERIFICATION" src="https://img.shields.io/badge/enforcement-NEEDS%20VERIFICATION-d29922?style=flat-square">
  <img alt="Last reviewed: 2026-05-09" src="https://img.shields.io/badge/reviewed-2026--05--09-6e7681?style=flat-square">
</p>

| Field | Value |
|---|---|
| **ADR ID** | ADR-0001 |
| **Title** | Schema Home: `schemas/contracts/v1/` is Canonical |
| **Status** | `accepted` |
| **Date proposed** | 2026-04-21 *(approximate; backfill — see §10)* |
| **Date accepted** | 2026-04-21 *(retroactive; corpus-attested anchor)* |
| **Date last reviewed** | 2026-05-09 |
| **Supersedes** | None |
| **Superseded by** | None |
| **Authoritative for** | All `*.schema.json`, `*.schema.yaml`, JSON-LD context, and equivalent machine-validation artifacts |
| **Owner** | Architecture Steward |
| **Reviewers required to amend** | Architecture Steward + Schema Steward + Docs Steward + at least one subsystem owner |
| **Conformance** | RFC 2119-style `MUST` / `MUST NOT` apply to §3 (Decision) |

**Quick jump:** [1. Context](#1-context) · [2. Forces](#2-forces) · [3. Decision](#3-decision) · [4. Consequences](#4-consequences) · [5. Alternatives](#5-alternatives-considered) · [6. Migration](#6-migration-plan) · [7. Rollback](#7-rollback-plan) · [8. Validation](#8-validation-and-enforcement) · [9. Related](#9-related-doctrine-and-adrs) · [10. Open](#10-open-questions-and-needs-verification) · [11. Appendix](#11-appendix)

---

## 1. Context

KFM separates four cooperating governance layers — **meaning** (`contracts/`), **shape** (`schemas/`), **admissibility** (`policy/`), and **proof** (`tests/`, `fixtures/`). These layers are non-collapsible by doctrine: collapsing any two is one of the named drift modes the project tries to prevent.

Across the dossier corpus, a recurring ambiguity emerged whenever a new domain — hydrology, soil, fauna, flora, habitat, geology, atmosphere, archaeology, settlements/infrastructure, hazards, agriculture, people/DNA/land — needed a place to commit its first JSON Schema:

- **Option A.** Under `contracts/<domain>/<x>.schema.json`, alongside the meaning Markdown.
- **Option B.** Under `schemas/contracts/v1/<domain>/<x>.schema.json`, in a single versioned schema authority root.
- **Option C.** Under a topic-named root such as `schemas/<domain>/...` (`schemas/occurrence_evidence/`, `schemas/soil_moisture/`, `schemas/hazards/`, etc.).

Domain blueprints repeatedly noted both Option A and Option B as `PROPOSED / CONFLICTED path | Authority level: machine contract authority pending ADR | Dependencies: ADR-0001 resolves schema home`, which is the marker this ADR is here to retire.

> [!IMPORTANT]
> Without a single answer, validators, CI, integration tests, the governed API, and downstream consumers each pick a path independently. Once two homes both look authoritative, the cost to undo grows quadratically: every test, every fixture, every reference, every CI job, every receipt that hashes a schema `$id` carries the choice forward.

## 2. Forces

The forces below shape the decision; each is grounded in repeated corpus statements rather than convenience.

| Force | What it requires |
|---|---|
| **Validator parity** | A single root that the structural validator (e.g. `scripts/validate_schemas.py`) can treat as *the* contract surface, so coverage is uniform across families. |
| **Versioned shape** | Schemas need an explicit version segment so breaking changes ship as `v2/` without mutating `v1/`. |
| **Layer separation** | `contracts/` documents *meaning*; `schemas/` mechanizes *shape*. If `.schema.json` files live in `contracts/`, the meaning/shape boundary blurs and Markdown directories become validator targets. |
| **Domain placement law** | Per Directory Rules §12, a domain `MUST NOT` become a root folder. Schemas for domain `X` belong in `schemas/contracts/v1/<X>/`, not `<X>/schemas/`. |
| **Cross-cutting reuse** | Common, runtime, evidence, release, correction, and policy schemas must share an authority root with domain schemas so cross-references (`$ref`) are stable and namespaced. |
| **Auditability** | The schema authority root is referenced by hashes, receipts, and proof packs; relocating it later requires a structural migration, not a routine move. |
| **Lineage tolerance** | Pre-existing `contracts/<domain>/<x>.schema.json` files exist as *lineage*; the rule must absorb them via migration without invalidating prior receipts. |

## 3. Decision

> [!IMPORTANT]
> **Canonical machine-schema home: `schemas/contracts/v1/<family>/...`** (RFC 2119: `MUST`).
> **`contracts/` retains semantic Markdown only** — never `.schema.json`, `.schema.yaml`, or equivalent (RFC 2119: `MUST NOT`).
> **Divergent definitions in both `schemas/` and `contracts/` are prohibited** (RFC 2119: `MUST NOT`).

### 3.1 Canonical layout

```
