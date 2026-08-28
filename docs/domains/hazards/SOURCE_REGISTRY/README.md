<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/hazards/source-registry/readme
title: Hazards Domain — Source Registry (folder index)
type: standard
version: v1
status: draft
owners: <hazards-domain-steward>, <source-registry-steward>, <rights-reviewer>, <docs-steward>   # placeholders pending owner-registry verification
created: 2026-06-05
updated: 2026-06-05
policy_label: public
contract_version: "3.0.0"   # pinned per ai-build-operating-contract.md
related:
  - docs/domains/hazards/README.md
  - docs/domains/habitat/SOURCE_REGISTRY.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/doctrine/directory-rules.md
  - schemas/contracts/v1/source/source-descriptor.json
  - data/registry/sources/hazards/
  - policy/domains/hazards/
  - policy/release/hazards/
  - ai-build-operating-contract.md
tags: [kfm, domain:hazards, source-registry, governance, admission, emergency-alert-boundary]
notes:
  - "FOLDER FORM: requested as docs/domains/hazards/SOURCE_REGISTRY/README.md — i.e. SOURCE_REGISTRY as a FOLDER with a README index, holding per-source-family entry files. This diverges from the single-file docs/domains/habitat/SOURCE_REGISTRY.md used in the Habitat lane. Both are doctrine-permitted (Directory Rules §6.1.a: same-named folder when a profile warrants splitting). The file-vs-folder inconsistency across lanes is a low-stakes drift item, tracked as OQ-HAZ-SR-01."
  - "This README is the human-facing INDEX of the SOURCE_REGISTRY/ folder; it points at per-family entry files and the machine-readable registry under data/registry/sources/hazards/. It does NOT own descriptors."
  - "EMERGENCY-ALERT BOUNDARY (hard): KFM Hazards is NEVER an emergency-alert authority and must not provide life-safety instructions. KFM used as life-safety instruction = DENY (Atlas §20.5)."
  - "Source-role labels use the CONFIRMED 7-role enum (Atlas §24.1.1); the Hazards §C knowledge-character vocabulary (operational_warning, administrative_declaration, scientific_observation, etc.) maps onto it. Per-family role assignments are PROPOSED."
  - "Rights/terms NEEDS VERIFICATION for every family. CONTRACT_VERSION = \"3.0.0\"."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ⚠️ Hazards Domain — Source Registry

> Human-facing admission and authority-control surface for the source families the **Hazards** lane may admit, quarantine, restrict, or deny. This is the **folder index** for `docs/domains/hazards/SOURCE_REGISTRY/`; per-family entry files live alongside it, and the machine-readable registry lives under `data/registry/sources/hazards/`. Not a bibliography. Not the truth store. **Not an alert system.**

<p align="center">
  <b>Admission control · Not an alert authority · Role set at admission · Sensitive joins fail closed</b>
</p>

![status](https://img.shields.io/badge/status-draft-orange)
![domain](https://img.shields.io/badge/domain-hazards-B71C1C)
![role](https://img.shields.io/badge/role-source_registry_index-lightgrey)
![boundary](https://img.shields.io/badge/emergency--alert-NEVER_an_authority-critical)
![rights](https://img.shields.io/badge/rights-NEEDS_VERIFICATION-orange)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)
![meta](https://img.shields.io/badge/meta-KFM__v2-lightgrey)
<!-- TODO: replace static badges with CI-driven Shields endpoints once owners + registry are verified (NEEDS VERIFICATION). -->

**Status:** draft &middot; **Owners:** hazards steward · source-registry steward · rights reviewer · docs steward *(placeholders)* &middot; **Contract:** `CONTRACT_VERSION = "3.0.0"` &middot; **Last updated:** 2026-06-05

> [!WARNING]
> **KFM Hazards is not an emergency-alert system.** It governs *historical* hazard events, warnings/advisories/watches **as context**, disaster declarations, regulatory hazard areas, scientific observations, remote sensing, models, and resilience summaries. It MUST NOT provide life-safety instructions or be presented as an alert authority. KFM used as a life-safety instruction is a `DENY` at the emergency-alert boundary. **(CONFIRMED — Atlas §20.5; Hazards dossier §B; §24.4.10.)**

> [!IMPORTANT]
> **This README is an index, not the registry of record.** The authoritative `SourceDescriptor` records are append-only under `data/registry/sources/hazards/`. This file indexes the `SOURCE_REGISTRY/` folder's per-family entries and explains how Hazards admits each source. If this index and a descriptor disagree, the **descriptor wins** — open a `DRIFT_REGISTER` entry.

---

## Contents

1. [Purpose & the folder-index form](#1-purpose--the-folder-index-form)
2. [The emergency-alert boundary](#2-the-emergency-alert-boundary)
3. [Repo fit and authority](#3-repo-fit-and-authority)
4. [Folder layout](#4-folder-layout)
5. [Source-role vocabulary](#5-source-role-vocabulary)
6. [Hazards source families](#6-hazards-source-families)
7. [Warning / advisory / watch — context, never instruction](#7-warning--advisory--watch--context-never-instruction)
8. [Sensitivity & rights posture](#8-sensitivity--rights-posture)
9. [Admission lifecycle](#9-admission-lifecycle)
10. [Schema, policy, and validator surfaces](#10-schema-policy-and-validator-surfaces)
11. [Open questions register](#11-open-questions-register)
12. [Open verification backlog](#12-open-verification-backlog)
13. [Changelog & definition of done](#13-changelog--definition-of-done)
14. [Related docs](#14-related-docs)

---

## 1. Purpose & the folder-index form

This document is the **Hazards domain's** source registry index. It records which source families the Hazards lane may consider, the role each is allowed to play, the rights/sensitivity/freshness posture each carries, the admission state of each, and the pointer to the per-family entry file and the machine-readable descriptor.

It is laid out as a **folder with a README index** (`SOURCE_REGISTRY/README.md`) rather than a single file. That choice is doctrine-permitted: Directory Rules §6.1.a allows a same-named folder when a profile is large enough to warrant splitting into subsidiary files (per-family entries, crosswalks, version pins). The Hazards lane has eight source families across several distinct authority types, so per-family entry files under one folder index are a reasonable shape.

> [!NOTE]
> **File-vs-folder divergence (OQ-HAZ-SR-01).** The Habitat lane used a single-file `docs/domains/habitat/SOURCE_REGISTRY.md`; this lane uses a `SOURCE_REGISTRY/` folder with a README. Both are valid, but the cross-lane inconsistency should be reconciled by a per-root README or ADR so domain lanes are predictable. Low-stakes drift — flagged, not silently split. **(CONFIRMED that both forms are permitted; PROPOSED which is canonical per-lane.)**

[⬆ back to top](#top)

---

## 2. The emergency-alert boundary

The single hardest rule in this lane, stated before anything else operational.

> [!WARNING]
> **KFM is never an emergency-alert authority.** The Hazards lane admits NWS warnings/advisories/watches and FEMA declarations as **historical or contextual** records — `Warning Context`, `Advisory Context`, `Disaster Declaration` — never as live instructions. No Hazards surface, layer, popup, or Focus-Mode answer may tell a person what to do for their safety. KFM used as a life-safety instruction is a `DENY`. **(CONFIRMED — Atlas §20.5 emergency-alert boundary; Hazards dossier §B non-ownership; §24.4.10 "Hazard event context is cited; KFM is never an alert authority.")**

This boundary shapes the whole registry: a source's *operational* warning content is admitted as `Warning Context` (a record that a warning was issued), not as an actionable alert. The registry records the boundary on every family that carries operational content (NWS, Kansas/local emergency context).

[⬆ back to top](#top)

---

## 3. Repo fit and authority

| Aspect | Value | Status |
|---|---|---|
| This file | `docs/domains/hazards/SOURCE_REGISTRY/README.md` (folder index) | **PROPOSED** — Directory Rules §12 + §6.1.a same-named-folder. |
| Per-family entry files | `docs/domains/hazards/SOURCE_REGISTRY/<family>.md` | **PROPOSED** (see §4). |
| Responsibility root | `docs/` (human-facing control plane) | CONFIRMED — Directory Rules §5. |
| Machine-readable registry home | `data/registry/sources/hazards/` | **PROPOSED** — Directory Rules §12; path form `sources/hazards/` vs `hazards/` open. |
| Descriptor schema home | `schemas/contracts/v1/source/source-descriptor.json` | **PROPOSED** — Directory Rules §7.4 / ADR-0001; NEEDS VERIFICATION. |
| Policy gates | `policy/domains/hazards/`; release gate `policy/release/hazards/` | **PROPOSED** — Directory Rules §12; §24.13 assigns Hazards a `policy/release/hazards/` lane. |
| Connector home | `connectors/<vendor>/` with `data/raw/hazards/<source_id>/<run_id>/` output | CONFIRMED pattern — Directory Rules §7.3. |
| Authority over published artifacts | **None.** Registry is not the truth store, publication authority, policy authority, or alert authority. | CONFIRMED doctrine — Directory Rules §11; Atlas §24.1.3, §20.5. |

[⬆ back to top](#top)

---

## 4. Folder layout

The `SOURCE_REGISTRY/` folder is indexed by this README; per-family entries are subsidiary files.

```text
docs/domains/hazards/SOURCE_REGISTRY/
├── README.md                       # ← this index
├── noaa-storm-events.md            # per-family entry (PROPOSED)
├── nws-alerts.md                   # per-family entry (PROPOSED) — Warning/Advisory/Watch Context
├── fema-disaster-declarations.md   # per-family entry (PROPOSED)
├── fema-nfhl-msc.md                # per-family entry (PROPOSED) — flood hazard context
├── usgs-earthquake-catalog.md      # per-family entry (PROPOSED)
├── noaa-hms-fire-smoke.md          # per-family entry (PROPOSED)
├── nasa-firms-active-fire.md       # per-family entry (PROPOSED)
└── kansas-local-emergency.md       # per-family entry (PROPOSED)
```

> [!NOTE]
> Per-family entry files are **PROPOSED** and not yet authored. Each would follow the registry-entry template (role, authority, endpoint, rights, sensitivity, cadence, source-head policy, activation state, descriptor pointer) and resolve to a `SourceDescriptor` under `data/registry/sources/hazards/`. The filename casing within the folder (`noaa-storm-events.md`) is itself part of OQ-HAZ-SR-01.

[⬆ back to top](#top)

---

## 5. Source-role vocabulary

The Hazards lane uses the project-wide **CONFIRMED 7-role enum** (`observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`). The Hazards dossier §C also defines a richer **knowledge-character vocabulary** that maps onto those roles — this is how the lane distinguishes a warning from a declaration from a model.

| Hazards §C knowledge character | Maps to 7-role | Example |
|---|---|---|
| `scientific_observation` | `observed` | USGS earthquake reading; storm-event observation. |
| `remote_sensing_detection` | `observed` | NASA FIRMS active-fire detection; NOAA HMS smoke. |
| `operational_warning` / `operational_advisory` / `operational_watch` | `regulatory` *(operational issuance, context only)* | NWS warning/advisory/watch — admitted as **Context**, never instruction. |
| `administrative_declaration` | `administrative` | FEMA disaster declaration. |
| `regulatory_context` | `regulatory` | FEMA NFHL flood-hazard regulatory zone. |
| `modeled_derivative` | `modeled` | Modeled hazard/exposure surface; requires `ModelRunReceipt` + uncertainty. |
| `resilience_analysis` | `modeled` / `aggregate` | Exposure/resilience summary. |
| `unknown_unclassified` | `candidate` | Pending intake not yet classified. |

> [!CAUTION]
> **Hazards-specific anti-pattern.** An `operational_warning` admitted as `Warning Context` must **not** be re-surfaced as a live alert (emergency-alert boundary `DENY`). A `regulatory_context` NFHL zone must **not** be cited as `observed` inundation — that is the Hydrology lane's hard line too ("NFHL regulatory context is not observed inundation"). A `modeled_derivative` must **not** be framed as observation. **(CONFIRMED — Atlas §24.1.2 anti-collapse; §20.5; Hydrology dossier §B.)**

[⬆ back to top](#top)

---

## 6. Hazards source families

> [!NOTE]
> Each row is a **declared family**, not an admission decision. Active admission requires a `SourceDescriptor` plus a `SourceActivationDecision`. Rights, endpoints, version, and current cadence are **NEEDS VERIFICATION** for every family. The "Atlas role" placeholder ("authority / observation / context / model as source role requires") is reproduced from §D as the thing to verify; the canonical role is from the 7-role enum (§5).

| # | Source family | Knowledge character → role (PROPOSED) | Hazards use | Entry file (PROPOSED) | Status |
|---|---|---|---|---|---|
| 6.1 | **NOAA Storm Events / NCEI** | `scientific_observation` → `observed` | Historical hazard-event record. | `noaa-storm-events.md` | CONFIRMED listing / PROPOSED activation |
| 6.2 | **NWS alerts / warnings / advisories / watches** | `operational_warning/advisory/watch` → `regulatory` *(Context only)* | `Warning Context` / `Advisory Context` — **never** live alert. | `nws-alerts.md` | CONFIRMED listing / PROPOSED activation |
| 6.3 | **FEMA Disaster Declarations / OpenFEMA** | `administrative_declaration` → `administrative` | `Disaster Declaration` records. | `fema-disaster-declarations.md` | CONFIRMED listing / PROPOSED activation |
| 6.4 | **FEMA NFHL / MSC flood hazard** | `regulatory_context` → `regulatory` | `Flood Context` — **not** observed inundation. | `fema-nfhl-msc.md` | CONFIRMED listing / PROPOSED activation |
| 6.5 | **USGS Earthquake Catalog** | `scientific_observation` → `observed` | `Earthquake Event` records. | `usgs-earthquake-catalog.md` | CONFIRMED listing / PROPOSED activation |
| 6.6 | **NOAA HMS Fire and Smoke** | `remote_sensing_detection` → `observed` | `Wildfire Detection` / `SmokeContext`. | `noaa-hms-fire-smoke.md` | CONFIRMED listing / PROPOSED activation |
| 6.7 | **NASA FIRMS active fire** | `remote_sensing_detection` → `observed` | `Wildfire Detection`. | `nasa-firms-active-fire.md` | CONFIRMED listing / PROPOSED activation |
| 6.8 | **Kansas / local emergency context** | per product → `regulatory` / `administrative` | Local hazard/emergency **context**, never instruction. | `kansas-local-emergency.md` | CONFIRMED listing / PROPOSED activation |

*All families are drawn from the Hazards dossier §D. Rights and current terms for every family are **NEEDS VERIFICATION**; sensitive joins fail closed; freshness is source-vintage or cadence specific.*

[⬆ back to top](#top)

---

## 7. Warning / advisory / watch — context, never instruction

The lane's operational sources (NWS, Kansas/local emergency context) carry content that *looks* like an alert. The registry's job is to admit them as **records of issuance**, not as actionable alerts.

| Admitted as | What it means | What it is NOT |
|---|---|---|
| `Warning Context` | A record that a warning was issued at a time/place. | A live instruction to take shelter / evacuate. |
| `Advisory Context` | A record that an advisory was issued. | A current recommendation from KFM. |
| `Operational Watch` | A record that a watch was in effect. | A KFM-issued watch. |

> [!WARNING]
> If a Hazards surface would tell a person what to do for safety, or present KFM as the source of a live alert, the answer is `DENY` and the surface is mis-scoped. Direct users to the official authority (NWS, local emergency management) — KFM cites that an authority issued something; it never substitutes for it. **(CONFIRMED — Atlas §20.5; Hazards dossier §B.)**

[⬆ back to top](#top)

---

## 8. Sensitivity & rights posture

Hazards data is mostly public, but the lane carries two real sensitivity surfaces and a universal fail-closed posture.

| Surface | Posture | Note |
|---|---|---|
| Critical-infrastructure exposure (Settlements join) | **Deny-by-default on public detail** | Settlements/Infrastructure owns the critical-asset deny lane; Hazards consumes exposure context with default deny on public detail (§24.4.12). |
| Living-person / private-parcel impact joins | Fail closed | People/Land controls apply on any join. |
| Operational alert content | Emergency-alert boundary `DENY` | §2, §7. |
| All families | Rights/terms NEEDS VERIFICATION; sensitive joins fail closed | Gate B + Gate C before activation. |

> [!CAUTION]
> This index states **no exact coordinates, access tokens, critical-asset detail, or restricted-source-derived fields.** Where a join touches critical infrastructure or private parcels, the gate and generalization live in `policy/` and the relevant lane's sensitivity doc. **(Sensitive-domain content discipline.)**

[⬆ back to top](#top)

---

## 9. Admission lifecycle

CONFIRMED doctrine for source admission (Unified Manual §3.6):

1. **Create or update** a `SourceDescriptor` for the candidate family/instance.
2. **Review** declared role (7-role enum + §C knowledge character), rights, sensitivity, cadence, access — **and the emergency-alert boundary** for operational sources.
3. **Issue a `SourceActivationDecision`**: `allowed` / `restricted` / `denied` / `needs-review`.
4. **Hold connectors inactive** until activation, fixtures, validators, and policy gates exist.
5. **Record** the descriptor pointer and decision under `data/registry/sources/hazards/`, and link it from the per-family entry file.

Promotion of source material is never a file move — it is a recorded decision backed by an `EvidenceBundle`, validation, and policy support. **(CONFIRMED — Directory Rules §3; Encyclopedia Appendix E.)**

[⬆ back to top](#top)

---

## 10. Schema, policy, and validator surfaces

| Surface | Proposed home | Status |
|---|---|---|
| `SourceDescriptor` schema | `schemas/contracts/v1/source/source-descriptor.json` | PROPOSED / NEEDS VERIFICATION |
| `SourceActivationDecision` schema | `schemas/contracts/v1/source/source-activation-decision.json` | PROPOSED / NEEDS VERIFICATION |
| Hazards admissibility policy | `policy/domains/hazards/` | PROPOSED |
| Hazards release gate | `policy/release/hazards/` | PROPOSED — §24.13 assigns this lane |
| Emergency-alert-boundary validator | `tools/validators/domains/hazards/` | PROPOSED — deny KFM-as-alert / life-safety-instruction |
| Source-role / anti-collapse validators | `tools/validators/source_descriptor/`, `.../domains/hazards/` | PROPOSED |
| Machine-readable registry | `data/registry/sources/hazards/` | PROPOSED |

### Validator coverage expected (PROPOSED)

- Source-descriptor schema validation (missing rights, missing source-head, missing cadence).
- **Emergency-alert-boundary denial test** — deny any surface that presents KFM as an alert authority or emits a life-safety instruction.
- NFHL-as-observed-inundation denial test (consistent with Hydrology).
- Operational-warning-as-live-alert denial test.
- `modeled_derivative`-as-observed denial test.
- No-network fixture coverage and dry-run watcher receipts.

[⬆ back to top](#top)

---

## 11. Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-HAZ-SR-01 | Folder form (`SOURCE_REGISTRY/README.md`, this lane) vs single file (`SOURCE_REGISTRY.md`, Habitat lane) — which is canonical per domain? | Directory steward + docs steward | Per-root README in `docs/domains/`; ADR (Directory Rules §6.1.a). |
| OQ-HAZ-SR-02 | Per-family entry-file naming/casing within the folder (`noaa-storm-events.md` vs `NOAA_STORM_EVENTS.md`). | Docs steward | Same per-root README. |
| OQ-HAZ-SR-03 | Confirm per-family role assignments (§6) and the §C-character → 7-role mapping against admitted descriptors. | Source steward | Registry inspection. |
| OQ-HAZ-SR-04 | Rights/terms for each family (all NEEDS VERIFICATION). | Rights reviewer | RightsReviewRecord per family; Gate B. |
| OQ-HAZ-SR-05 | Exact emergency-alert-boundary validator behavior and fixtures. | Hazards steward + policy steward | `policy/domains/hazards/` + validator design. |
| OQ-HAZ-SR-06 | Registry path form (`data/registry/sources/hazards/` vs `data/registry/hazards/`). | Directory steward | Per-root README. |
| OQ-HAZ-SR-07 | Whether Kansas/local emergency context is one family or several per-product descriptors. | Source steward | Per-product descriptors. |

[⬆ back to top](#top)

---

## 12. Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Folder-vs-file convention (OQ-HAZ-SR-01) and entry-file naming (OQ-HAZ-SR-02).
2. Presence/contents of `data/registry/sources/hazards/` descriptors and the eight per-family entry files.
3. Rights/terms for all eight families (Gate B).
4. Per-family role assignments and the §C-character → 7-role mapping (OQ-HAZ-SR-03).
5. Emergency-alert-boundary validator and fixtures (OQ-HAZ-SR-05).
6. `policy/release/hazards/` and `policy/domains/hazards/` presence.
7. NFHL-as-observed and operational-warning-as-live-alert denial fixtures.
8. Registry path form (OQ-HAZ-SR-06) and the Hazards-lane path-form conflict (Directory Rules §12 vs Atlas §24.13 flat).

[⬆ back to top](#top)

---

## 13. Changelog & definition of done

### 13.1 Changelog

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial Hazards source-registry **folder index**. | new | First Hazards-lane source doc; folder form per the requested path. |
| Built the folder-index form (`SOURCE_REGISTRY/README.md`) per Directory Rules §6.1.a; flagged the file-vs-folder divergence from Habitat as OQ-HAZ-SR-01. | reconciliation | Both forms are permitted; the cross-lane inconsistency is surfaced, not silently introduced. |
| Led with the emergency-alert boundary (§2, §7) as the lane's hard `DENY`. | clarification | Atlas §20.5 / dossier §B — KFM is never an alert authority. |
| Mapped the Hazards §C knowledge-character vocabulary onto the CONFIRMED 7-role enum (§5). | clarification | Distinguishes warning/declaration/observation/model without forking the enum. |
| Listed the eight §D families with PROPOSED roles and per-family entry-file pointers (§4, §6). | gap closure | Establishes the folder's contents and the admission surface. |
| Pinned `CONTRACT_VERSION = "3.0.0"`; no exact coordinates / tokens / critical-asset detail. | housekeeping / safety | Doctrine-adjacent + sensitive-join discipline. |

> **Backward compatibility.** New document — no prior anchors. Sibling to the Habitat `SOURCE_REGISTRY.md`; the file-vs-folder convention must be reconciled (OQ-HAZ-SR-01).

### 13.2 Definition of done

This index is done enough to enter the repository when:

- the folder-vs-file convention (OQ-HAZ-SR-01) is resolved or noted in `docs/registers/DRIFT_REGISTER.md`, and the Habitat/Hazards lanes are made consistent;
- the eight per-family entry files exist (or are clearly marked PROPOSED) and resolve to descriptors;
- the hazards domain steward, source-registry steward, rights reviewer, and docs steward review it; a policy steward signs off on the emergency-alert-boundary section;
- per-family role assignments are confirmed against admitted descriptors;
- rights/terms (Gate B) are resolved or each unresolved family is marked NEEDS VERIFICATION and not asserted as admitted;
- it remains an index — confirmed at review that it stores no descriptor and presents no live alert or life-safety instruction;
- the `GENERATED_RECEIPT.json` planned in the PR is wired into CI with `contract_version: "3.0.0"`;
- future changes follow the operating contract's §37 lifecycle.

[⬆ back to top](#top)

---

## 14. Related docs

**All targets PROPOSED until confirmed against a mounted repo; path form follows Directory Rules §12.**

- [`docs/domains/hazards/README.md`](../README.md) — Hazards lane orientation *(PROPOSED — NEEDS VERIFICATION)*.
- `docs/domains/hazards/SOURCE_REGISTRY/<family>.md` — per-family entry files *(PROPOSED, §4)*.
- [`docs/domains/habitat/SOURCE_REGISTRY.md`](../../habitat/SOURCE_REGISTRY.md) — sibling lane's single-file registry (the file-vs-folder comparison).
- [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../../sources/SOURCE_DESCRIPTOR_STANDARD.md) — project-wide descriptor standard *(PROPOSED)*.
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — §5/§6.1.a/§7.3/§7.4/§11/§12.
- `schemas/contracts/v1/source/source-descriptor.json` — descriptor schema *(PROPOSED home; NEEDS VERIFICATION)*.
- `policy/domains/hazards/` and `policy/release/hazards/` — Hazards admissibility + release policy *(PROPOSED)*.
- `data/registry/sources/hazards/` — machine-readable hazards source registry *(PROPOSED)*.
- [`ai-build-operating-contract.md`](../../../../ai-build-operating-contract.md) — §20.5 emergency-alert boundary; canonical operating contract (`CONTRACT_VERSION = "3.0.0"`).

---

**Last updated:** 2026-06-05 &middot; **Status:** draft &middot; **Contract:** `CONTRACT_VERSION = "3.0.0"` &middot; **Role:** source-registry folder index &middot; **Hard boundary:** KFM is never an emergency-alert authority &middot; **Citation short-names:** [DOM-HAZ], [DOM-HYD], [DOM-SETTLE], [ENCY], [DIRRULES], [GAI]

[⬆ back to top](#top)
