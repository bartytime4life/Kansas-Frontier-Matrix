<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/missing-or-planned-files/geology
title: Geology — Missing or Planned Files
type: standard
version: v1
status: draft
owners: <docs-steward + geology-domain-steward>  <!-- placeholder, NEEDS VERIFICATION -->
created: 2026-05-17
updated: 2026-05-17
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/domains/geology/README.md            # PROPOSED, NEEDS VERIFICATION
  - docs/registers/VERIFICATION_BACKLOG.md    # PROPOSED, NEEDS VERIFICATION
  - docs/registers/DRIFT_REGISTER.md          # PROPOSED, NEEDS VERIFICATION
tags: [kfm, geology, dom-geol, planning, inventory, missing-files]
notes:
  - Paths are PROPOSED until verified against the mounted repo.
  - Object families and source families are CONFIRMED from DOM-GEOL.
  - The four N. Verification backlog items mirror v1.1 Atlas Ch. 10.
[/KFM_META_BLOCK_V2] -->

# Geology — Missing or Planned Files

> Inventory of files the geology domain lane is **expected to host** across KFM's responsibility roots, but which are **not yet verified to exist** in the mounted repository. This is a planning and verification tracker — not authority.

<!-- Top-of-file badge row -->
![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Doc type: planning inventory](https://img.shields.io/badge/doc%20type-planning%20inventory-blue)
![Doctrine: DOM--GEOL](https://img.shields.io/badge/doctrine-DOM--GEOL-2c8a3e)
![Placement: Directory Rules §12](https://img.shields.io/badge/placement-Directory%20Rules%20%C2%A712-7b3fbf)
![Repo evidence: not mounted](https://img.shields.io/badge/repo%20evidence-not%20mounted-lightgrey)
![Truth posture: cite or abstain](https://img.shields.io/badge/truth%20posture-cite%20or%20abstain-orange)
<!-- TODO: replace once CI/build is verified --> ![CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)

| Field | Value |
|---|---|
| **Status** | draft |
| **Owners** | `<docs-steward>` + `<geology-domain-steward>` *(placeholder, NEEDS VERIFICATION)* |
| **Last updated** | 2026-05-17 |
| **Authority** | Inventory / planning artifact (not normative; subordinate to Directory Rules and DOM-GEOL) |
| **Repo evidence in this session** | **None mounted** — all path-existence claims are PROPOSED |

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. How to read this file](#2-how-to-read-this-file)
- [3. Geology lane map](#3-geology-lane-map)
- [4. Inventory by responsibility root](#4-inventory-by-responsibility-root)
  - [4.1 `docs/domains/geology/`](#41-docsdomainsgeology)
  - [4.2 `contracts/domains/geology/`](#42-contractsdomainsgeology)
  - [4.3 `schemas/contracts/v1/domains/geology/`](#43-schemascontractsv1domainsgeology)
  - [4.4 `policy/domains/geology/`](#44-policydomainsgeology)
  - [4.5 `tests/domains/geology/`](#45-testsdomainsgeology)
  - [4.6 `fixtures/domains/geology/`](#46-fixturesdomainsgeology)
  - [4.7 `packages/domains/geology/`](#47-packagesdomainsgeology)
  - [4.8 `pipelines/domains/geology/` and `pipeline_specs/geology/`](#48-pipelinesdomainsgeology-and-pipeline_specsgeology)
  - [4.9 `data/<phase>/geology/` (lifecycle)](#49-dataphasegeology-lifecycle)
  - [4.10 `data/registry/sources/geology/`](#410-dataregistrysourcesgeology)
  - [4.11 `release/candidates/geology/`](#411-releasecandidatesgeology)
- [5. Object family ↔ file crosswalk](#5-object-family--file-crosswalk)
- [6. Source family ↔ source descriptor crosswalk](#6-source-family--source-descriptor-crosswalk)
- [7. Validator / test home inventory](#7-validator--test-home-inventory)
- [8. Verification backlog](#8-verification-backlog)
- [9. Open ADRs that gate placement](#9-open-adrs-that-gate-placement)
- [10. Anti-patterns specific to geology](#10-anti-patterns-specific-to-geology)
- [11. Status snapshot & next smallest useful PR](#11-status-snapshot--next-smallest-useful-pr)
- [Related docs](#related-docs)

---

## 1. Purpose

The geology domain lane is described doctrinally by **DOM-GEOL** (Atlas Ch. 10) and placed structurally by **Directory Rules §12 — Domain Placement Law**. Together they say *what* geology owns and *where* its files belong. They do not, by themselves, say *which of those files currently exist in the repository*.

This document fills the gap. It enumerates the files the geology lane is expected to host — domain docs, contracts, schemas, policies, tests, fixtures, packages, pipelines, lifecycle data, source registry entries, and release candidates — and tracks each as **PRESENT**, **MISSING (PROPOSED to create)**, or **NEEDS VERIFICATION**. It is a planning surface, a review checklist, and a drift-prevention aid.

> [!IMPORTANT]
> This file is **inventory, not authority**. It cites doctrine; it does not create it. Where this file appears to disagree with Directory Rules, DOM-GEOL, or an accepted ADR, those higher sources win, and the conflict should be opened against `docs/registers/DRIFT_REGISTER.md` *(path PROPOSED)* per Directory Rules §2.5.

---

## 2. How to read this file

Each inventory row carries a status label. Apply the narrowest truthful label:

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified in this session from attached doctrine / Atlas / Directory Rules. Used for *doctrinal* claims, not path-existence. |
| **PRESENT** | The file is verified to exist in the mounted repo. **No row currently uses this label** — no repo is mounted in this session. |
| **MISSING (PROPOSED)** | The file is expected by Directory Rules §12 + DOM-GEOL but its existence is not verified. Default state for everything below. |
| **PARTIAL** | A neighboring or compatibility-root copy is suspected; canonical home unverified. Requires a Drift Register entry on confirmation. |
| **NEEDS VERIFICATION** | Existence is checkable with a single `ls`-equivalent action; not yet checked. |
| **UNKNOWN** | Existence cannot be resolved from available evidence and is not trivially checkable. |
| **DEFERRED** | Intentionally not created; deferral reason recorded in §11 or the relevant ADR. |

> [!NOTE]
> Throughout §4–§7, the **base path is PROPOSED** for every entry. The first reviewer with mounted-repo access SHOULD walk the inventory, mark PRESENT rows where files already exist, and open Drift Register entries for any divergence from Directory Rules.

---

## 3. Geology lane map

The geology domain is a **segment inside many responsibility roots**, never a root itself. The map below is the canonical lane shape per Directory Rules §12.

```mermaid
