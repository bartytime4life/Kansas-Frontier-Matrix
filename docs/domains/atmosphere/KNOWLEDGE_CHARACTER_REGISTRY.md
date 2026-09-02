<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/atmosphere/knowledge-character-registry
title: Atmosphere — Knowledge Character Registry
type: standard
version: v1
status: draft
owners: DOM-AIR steward + Docs steward (PLACEHOLDER — NEEDS VERIFICATION)
created: 2026-05-29
updated: 2026-05-29
policy_label: public
related:
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md  # CANONICAL prose explainer for this vocabulary
  - docs/domains/atmosphere/IDENTITY_MODEL.md         # companion — identity view
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md       # companion — placement view
  - docs/domains/atmosphere/EXPANSION_BACKLOG.md      # companion — candidate register
  - docs/doctrine/directory-rules.md                  # CONFIRMED — this project
  - docs/registers/DRIFT_REGISTER.md                  # receives the naming-collision drift entry
  - docs/adr/ADR-0001-schema-home.md                  # CONFIRMED — cited by Directory Rules
  - ai-build-operating-contract.md                    # CONFIRMED — operating contract
tags: [kfm, atmosphere, air, knowledge-character, registry, controlled-vocabulary, governance, doctrine]
notes:
  # NAMING COLLISION (CONFIRMED in this session): sibling docs reference BOTH this filename and KNOWLEDGE_CHARACTERS.md for the same vocabulary. This file does NOT duplicate the prose; it is a controlled-vocabulary registry surface that defers all explanation to KNOWLEDGE_CHARACTERS.md.
  # Creating two competing full documents would be the parallel-authority anti-pattern (Directory Rules §13.1). This stub avoids that pending the ADR / rename in OQ-REG-01.
  # The 12 terms are CONFIRMED ubiquitous language (Atlas v1.1 Ch. 11 §C); the canonical ENUM VALUES are OPEN (Atlas KFM-P1-IDEA-0051).
  # Registry home (data/registry/ vs control_plane/) is ADR-class (ADR-S-03) — this docs-lane file is the human-readable index, not the machine artifact.
  # CONTRACT_VERSION = "3.0.0" (doctrine-adjacent doc).
  # Meta Block v2 rule: no nested HTML comments inside this block; '#' annotations only.
[/KFM_META_BLOCK_V2] -->

# Atmosphere — Knowledge Character Registry

> **The controlled-vocabulary surface for Atmosphere knowledge characters.** This file is the *registry index*; the *explanation, rules, and rationale* live in the canonical companion, [`KNOWLEDGE_CHARACTERS.md`](./KNOWLEDGE_CHARACTERS.md).

[![Status: Draft](https://img.shields.io/badge/status-draft-yellow)](#) [![Type: Registry index](https://img.shields.io/badge/type-registry--index-blue)](#) [![Canonical prose: KNOWLEDGE_CHARACTERS.md](https://img.shields.io/badge/prose-KNOWLEDGE__CHARACTERS.md-informational)](./KNOWLEDGE_CHARACTERS.md) [![Enum: OPEN](https://img.shields.io/badge/enum-OPEN-critical)](#) [![Contract: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)](#) [![Last updated](https://img.shields.io/badge/last__updated-2026--05--29-lightgrey)](#)

**Status:** Draft · **Owners:** DOM-AIR steward + Docs steward *(PLACEHOLDER — NEEDS VERIFICATION)* · **Updated:** 2026-05-29 · **Contract:** `CONTRACT_VERSION = "3.0.0"`

> [!IMPORTANT]
> **This file does not duplicate `KNOWLEDGE_CHARACTERS.md`.** Across the Atmosphere lane docs, two filenames — `KNOWLEDGE_CHARACTERS.md` and `KNOWLEDGE_CHARACTER_REGISTRY.md` — refer to the **same vocabulary**. Maintaining two full prose documents would be the parallel-authority anti-pattern (Directory Rules §13.1) — competing definitions that drift apart. Per Directory Rules §2.5, the collision is surfaced as a drift entry, not silently reconciled. Until the naming ADR (see [§5 OQ-REG-01](#5-open-questions)) resolves it, **`KNOWLEDGE_CHARACTERS.md` is canonical for prose, rules, and rationale**; this file holds only the controlled-vocabulary *index* and pointers into that canon.

---

<a id="contents"></a>

## Contents

1. [Purpose and relationship to the explainer](#1-purpose-and-relationship-to-the-explainer)
2. [Controlled vocabulary index](#2-controlled-vocabulary-index)
3. [Machine-registry status](#3-machine-registry-status)
4. [Enforcement pointers](#4-enforcement-pointers)
5. [Open questions](#5-open-questions)
6. [Changelog](#6-changelog)
7. [Definition of done](#7-definition-of-done)
8. [Related docs](#8-related-docs)

---

## 1. Purpose and relationship to the explainer

This file is the **registry index** for the Atmosphere knowledge-character vocabulary: a stable, scannable list of the controlled terms, with each term pointing to its full treatment in [`KNOWLEDGE_CHARACTERS.md`](./KNOWLEDGE_CHARACTERS.md).

| Concern | Where it lives |
|---|---|
| **What the terms mean; the anti-collapse rule; rationale; lifecycle; UI exposure** | [`KNOWLEDGE_CHARACTERS.md`](./KNOWLEDGE_CHARACTERS.md) *(CANONICAL prose explainer)* |
| **The scannable term index + machine-registry status** | This file |
| **The machine-readable registry artifact (enum + guards)** | `data/registry/` or `control_plane/` *(home is ADR-class — ADR-S-03; PROPOSED — NEEDS VERIFICATION)* |
| **Validators that enforce the vocabulary** | `tools/validators/...`, exercised by `tests/domains/atmosphere/` *(PROPOSED)* |
| **Policy deny rules** | `policy/domains/atmosphere/` *(PROPOSED)* |

> [!NOTE]
> If your tooling only needs the *list of valid terms*, read [§2](#2-controlled-vocabulary-index). If you need to know *why* a term exists, what guards it requires, or how the anti-collapse rule works, follow the link to `KNOWLEDGE_CHARACTERS.md` — that prose is **not** repeated here, deliberately.

[Back to top ↑](#contents)

---

## 2. Controlled vocabulary index

The twelve Atmosphere knowledge-character terms per **Atlas v1.1 Ch. 11 §C (CONFIRMED ubiquitous language / PROPOSED field realization)**. Each carries the same doctrinal constraint: *meaning constrained by source role, evidence, time, and release state.* Full glosses, guards, and denials are in [`KNOWLEDGE_CHARACTERS.md` §4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters).

| # | Term | One-line role | Detail |
|---|---|---|---|
| 0 | `Knowledge character` *(umbrella field)* | Every object MUST carry exactly one. | [§2](./KNOWLEDGE_CHARACTERS.md#2-what-knowledge-character-means) |
| 1 | `OBSERVED_SENSOR` | Direct instrument reading. | [§4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters) |
| 2 | `PUBLIC_AQI_REPORT` | Agency AQI report — **AQI ≠ concentration**. | [§6.1](./KNOWLEDGE_CHARACTERS.md#61-the-four-explicit-atmosphere-denials-confirmed--atlas-11i-11k) |
| 3 | `REGULATORY_ARCHIVE` | Archived regulatory dataset / determination. | [§4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters) |
| 4 | `LOW_COST_SENSOR` | Community-grade reading — **caveats required for public release**. | [§6.1](./KNOWLEDGE_CHARACTERS.md#61-the-four-explicit-atmosphere-denials-confirmed--atlas-11i-11k) |
| 5 | `ATMOSPHERIC_MODEL_FIELD` | NWP / CTM / reanalysis output — **never an observation**. | [§6.1](./KNOWLEDGE_CHARACTERS.md#61-the-four-explicit-atmosphere-denials-confirmed--atlas-11i-11k) |
| 6 | `REMOTE_SENSING_MASK` | Satellite raster / mask — **AOD ≠ PM2.5**. | [§6.1](./KNOWLEDGE_CHARACTERS.md#61-the-four-explicit-atmosphere-denials-confirmed--atlas-11i-11k) |
| 7 | `CLIMATE_ANOMALY_CONTEXT` | Departure-from-baseline context — aggregate, never per-place. | [§4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters) |
| 8 | `DERIVED_FUSION` | Multi-source blend — derivative, not observation. | [§4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters) |
| 9 | `METEOROLOGICAL_CONTEXT` | Supporting meteorology. | [§4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters) |
| 10 | `ALERT_AND_ADVISORY_CONTEXT` | Advisory context — **never the official alerting authority**. | [§4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters) |
| 11 | `NETWORK_AND_SITE_CONTEXT` | Network / site metadata. | [§4](./KNOWLEDGE_CHARACTERS.md#4-the-twelve-atmosphere-knowledge-characters) |

> [!WARNING]
> **The enum is not yet canonical.** Atlas KFM-P1-IDEA-0051 records the open question *"What canonical enum values should KFM use for knowledge-character labels?"* The terms above are CONFIRMED as the Atmosphere ubiquitous language; the exact machine enum (casing, umbrella-term handling) is **OPEN** and ADR-class. Do not freeze a string enum from this index until the ADR lands.

[Back to top ↑](#contents)

---

## 3. Machine-registry status

The **machine-readable** knowledge-character registry (the artifact schemas and validators load at runtime) is **PROPOSED — NEEDS VERIFICATION**. Its proposed shape is illustrated in [`KNOWLEDGE_CHARACTERS.md` §8](./KNOWLEDGE_CHARACTERS.md#8-registry-shape-proposed).

| Aspect | Status |
|---|---|
| Registry **home** (`data/registry/` vs. `control_plane/` vs. schema-adjacent) | **OPEN** — ADR-class per Directory Rules §2.4(5); Atlas ADR-S-03. |
| Registry **enum values** | **OPEN** — Atlas KFM-P1-IDEA-0051. |
| Registry **field shape** (`required_guards`, `forbidden`, `public_release`) | **INFERRED** proposal — see explainer §8. |
| Registry **presence on disk** | **NEEDS VERIFICATION** — repo not mounted this session. |

> [!NOTE]
> This `docs/`-lane file is the human-readable index. It is **not** the machine artifact and must not be loaded by validators as one. When the machine registry lands (per ADR-S-03), this file should link to it, not embed it.

[Back to top ↑](#contents)

---

## 4. Enforcement pointers

The anti-collapse rule and its four explicit denials are defined in [`KNOWLEDGE_CHARACTERS.md` §6](./KNOWLEDGE_CHARACTERS.md#6-the-anti-collapse-rule) and enforced through the validators in [§9](./KNOWLEDGE_CHARACTERS.md#9-validators-and-deny-tests). Pointers only — no logic lives here:

- **Denials** (`aqi-as-concentration`, `aod-as-pm25`, `model-as-observed`, `low-cost-sensor-caveat`) → `policy/domains/atmosphere/` *(PROPOSED)*.
- **Validator logic** → `tools/validators/<topic>/...`, *called* by `tests/domains/atmosphere/` *(Directory Rules §13.5; PROPOSED)*.
- **UI / API / AI exposure** of knowledge character → see [`KNOWLEDGE_CHARACTERS.md` §11](./KNOWLEDGE_CHARACTERS.md#11-ui-api-and-ai-surface-exposure).

[Back to top ↑](#contents)

---

## 5. Open questions

| # | Item | Status | What would settle it |
|---|---|---|---|
| OQ-REG-01 | **Filename reconciliation** — is the canonical file `KNOWLEDGE_CHARACTERS.md` (explainer) with this as a thin index, or should one filename be retired? | **OPEN** | A rename/keep ADR + a single `docs/registers/DRIFT_REGISTER.md` entry; update all sibling-doc references. |
| OQ-REG-02 | Canonical knowledge-character **enum values**. | **OPEN** *(Atlas KFM-P1-IDEA-0051; ADR-S-04)* | Enum ADR + mounted registry. |
| OQ-REG-03 | Machine-registry **home**. | **OPEN** *(ADR-S-03)* | Placement ADR + mounted file. |
| OQ-REG-04 | Whether this index should be auto-generated from the machine registry (to prevent the two from drifting). | **PROPOSED** | Build a generator + CI check once the machine registry exists. |

> [!IMPORTANT]
> **Recommended resolution (PROPOSED).** Keep `KNOWLEDGE_CHARACTERS.md` as the single canonical prose+vocabulary doc and retire this filename, **or** keep this file strictly as an auto-generated index of the machine registry (OQ-REG-04). What should *not* persist is two hand-maintained prose documents defining the same vocabulary — that is the drift this stub is designed to prevent.

[Back to top ↑](#contents)

---

## 6. Changelog

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Created as a redirect-aware registry **index**, not a duplicate explainer | new | Sibling docs reference both filenames for one vocabulary; a second full prose doc would be parallel-authority drift (Directory Rules §13.1). |
| Deferred all prose, rules, glosses, and rationale to `KNOWLEDGE_CHARACTERS.md` | reconciliation | Single source of truth for the vocabulary; this file holds only the index + pointers. |
| Recorded the filename collision as OQ-REG-01 with a recommended resolution | reconciliation | Surface drift per Directory Rules §2.5 rather than silently picking. |

> **Backward compatibility.** New file. Satisfies references to `KNOWLEDGE_CHARACTER_REGISTRY.md` in the sibling docs without creating competing definitions.

[Back to top ↑](#contents)

---

## 7. Definition of done

This document is done enough to enter the repository when:

- the filename question (OQ-REG-01) is resolved by ADR — either this file is retired in favor of `KNOWLEDGE_CHARACTERS.md`, or it is fixed as an auto-generated index — and a single drift entry is recorded;
- it contains **no** prose that competes with or diverges from `KNOWLEDGE_CHARACTERS.md`;
- the machine-registry home (OQ-REG-03) and enum (OQ-REG-02) are settled and this index links to (or is generated from) the mounted registry;
- a DOM-AIR steward and a docs steward review it;
- the `GENERATED_RECEIPT.json` planned for this artifact is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

[Back to top ↑](#contents)

---

## 8. Related docs

- [`docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md`](./KNOWLEDGE_CHARACTERS.md) — **CANONICAL** prose explainer for this vocabulary
- [`docs/domains/atmosphere/IDENTITY_MODEL.md`](./IDENTITY_MODEL.md) — identity view; *uses* the vocabulary *(companion)*
- [`docs/domains/atmosphere/FILE_SYSTEM_PLAN.md`](./FILE_SYSTEM_PLAN.md) — placement view *(companion)*
- [`docs/domains/atmosphere/EXPANSION_BACKLOG.md`](./EXPANSION_BACKLOG.md) — candidate register *(companion)*
- [`docs/domains/atmosphere/EXPANSION_PLAN.md`](./EXPANSION_PLAN.md) — sequenced roadmap *(companion)*
- [`docs/domains/atmosphere/README.md`](./README.md) — Atmosphere lane overview *(PROPOSED)*
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Directory Rules §13.1 (parallel-home anti-pattern), §2.5 (drift handling) *(CONFIRMED)*
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — receives the OQ-REG-01 naming-collision entry *(PROPOSED)*
- [`docs/adr/ADR-0001-schema-home.md`](../../adr/ADR-0001-schema-home.md) — default schema home *(CONFIRMED)*
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating contract *(CONFIRMED — `CONTRACT_VERSION = "3.0.0"`)*

External (doctrinal) — names only; not links:

- `[DOM-AIR]` — Atmosphere / Air dossier (Atlas Ch. 11 §C)
- `[ENCY]` — Domain & Capability Encyclopedia §7.9
- `[DIRRULES]` — Directory Rules

---

**Last updated:** 2026-05-29 · **Version:** v1 (draft) · **Status:** draft · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Canonical prose:** [`KNOWLEDGE_CHARACTERS.md`](./KNOWLEDGE_CHARACTERS.md)

[Back to top ↑](#contents)
