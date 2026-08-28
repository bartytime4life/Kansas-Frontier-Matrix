<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-hazards-glossary
title: Hazards Domain — Glossary
type: standard
version: v1
status: draft
owners: <hazards-domain-stewards-TBD>, <docs-steward-TBD>
created: 2026-06-05
updated: 2026-06-05
policy_label: public
contract_version: "3.0.0"
related:
  - ai-build-operating-contract.md
  - directory-rules.md
  - docs/domains/hazards/README.md
  - docs/domains/hazards/DATA_LIFECYCLE.md
  - docs/domains/hazards/EXPANSION_BACKLOG.md
  - docs/domains/hazards/EXPANSION_PLAN.md
  - docs/domains/hazards/FILE_SYSTEM_PLAN.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/DRIFT_REGISTER.md
tags: [kfm, hazards, glossary, ubiquitous-language, governance]
notes:
  - CONTRACT_VERSION pinned at 3.0.0 per ai-build-operating-contract.md v3.0.
  - Atlas §12.C records each Hazards term as "CONFIRMED term / PROPOSED field realization"; one-line glosses below are INFERRED from the term name plus lane doctrine, not verbatim Atlas definitions.
  - KFM Hazards is explicitly NOT an emergency alert system.
[/KFM_META_BLOCK_V2] -->

# Hazards Domain — Glossary

> The shared vocabulary of the KFM **Hazards** lane: its ubiquitous-language terms, object families, source roles, and the cross-cutting trust terms a Hazards reader needs — each labeled by how strongly it is grounded.

![status](https://img.shields.io/badge/status-draft-yellow)
![domain](https://img.shields.io/badge/domain-hazards-darkred)
![type](https://img.shields.io/badge/doc--type-glossary-informational)
![boundary](https://img.shields.io/badge/boundary-NOT_an_alert_system-critical)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![policy](https://img.shields.io/badge/policy-public--safe-green)

**Status:** draft · **Owners:** `<hazards-domain-stewards-TBD>` · `<docs-steward-TBD>` · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Last updated:** 2026-06-05

> [!IMPORTANT]
> **How to read the labels in this glossary.** The Atlas records each Hazards ubiquitous-language term as **"CONFIRMED term / PROPOSED field realization"** — the *term* is canon; its *schema shape* is not yet fixed. The Atlas does **not** publish a prose definition for each term. The one-line glosses in [§3](#3-ubiquitous-language-confirmed-terms) are therefore **INFERRED** from the term name plus Hazards lane doctrine (DOM-HAZ §12; ENCY §7.10), and are marked accordingly. They explain intended meaning; they do not assert a verified field definition. *(CONFIRMED basis — Atlas §12.C; ENCY §7.10.)*

> [!CAUTION]
> **KFM is not an emergency alert system.** Several terms below name operational warning/advisory/watch material. Inside KFM these are **contextual-only** carriers, freshness-bounded, and must redirect life-safety action to NWS, FEMA, USGS, and state/local emergency authorities. No definition in this glossary licenses life-safety instruction. *(CONFIRMED — DOM-HAZ §12.I; Atlas §24.9.2.)*

---

## Table of Contents

1. [Scope & how to use](#1-scope--how-to-use)
2. [Label legend](#2-label-legend)
3. [Ubiquitous language (CONFIRMED terms)](#3-ubiquitous-language-confirmed-terms)
4. [Term → source-role crosswalk](#4-term--source-role-crosswalk)
5. [Object families](#5-object-families)
6. [Source families](#6-source-families)
7. [Cross-cutting KFM trust terms](#7-cross-cutting-kfm-trust-terms)
8. [Temporal vocabulary](#8-temporal-vocabulary)
9. [Boundary & anti-collapse terms](#9-boundary--anti-collapse-terms)
10. [Open questions](#10-open-questions)
11. [Related docs](#11-related-docs)

---

## 1. Scope & how to use

This glossary is **domain-scoped**: it defines the words the Hazards lane uses, in the meaning the Hazards bounded context gives them. Where a word is also defined globally (e.g., `EvidenceBundle`, `Promotion`), this file points to the cross-cutting definition rather than re-deciding it ([§7](#7-cross-cutting-kfm-trust-terms)).

- For the **lifecycle** behind these terms, see [`DATA_LIFECYCLE.md`](./DATA_LIFECYCLE.md).
- For **where files live**, see [`FILE_SYSTEM_PLAN.md`](./FILE_SYSTEM_PLAN.md).
- For **planned work**, see [`EXPANSION_BACKLOG.md`](./EXPANSION_BACKLOG.md) and [`EXPANSION_PLAN.md`](./EXPANSION_PLAN.md).

This file **explains** vocabulary; it does not **decide** object meaning (that is `contracts/domains/hazards/`) or shape (that is `schemas/contracts/v1/domains/hazards/`).

[↩ Back to top](#table-of-contents)

---

## 2. Label legend

| Label | Meaning in this glossary |
|---|---|
| **CONFIRMED** | Verified this session from attached KFM doctrine (Atlas v1.1, ENCY, Directory Rules, operating contract). |
| **INFERRED** | A one-line gloss derived from the canonical term name plus lane doctrine; not a verbatim Atlas definition. |
| **PROPOSED** | Field realization, schema path, or naming not yet verified in a mounted repo. |
| **CONFLICTED** | Sources disagree or a mapping is unsettled; held until ADR / drift-register resolution. |
| **NEEDS VERIFICATION** | Checkable, but not checked strongly enough to act as fact. |

> [!NOTE]
> The recurring phrase in the Atlas — *"used inside this domain with meaning constrained by source role, evidence, time, and release state"* — is the CONFIRMED guardrail attached to **every** Hazards term: a term's meaning is never free-floating; it is pinned by which source role carries it, what evidence supports it, which times apply, and whether it has been released. *(CONFIRMED — Atlas §12.C.)*

[↩ Back to top](#table-of-contents)

---

## 3. Ubiquitous language (CONFIRMED terms)

The twelve terms below are **CONFIRMED** as the Hazards ubiquitous language (Atlas §12.C). The **Term** column is canon; the **Intended meaning** column is **INFERRED** (see [§2](#2-label-legend)); the **Carrier object** links the term to a §5 object family where one applies.

| Term (CONFIRMED) | Intended meaning (INFERRED) | Typical carrier object | Canonical source role *(Atlas §24.1.1)* |
|---|---|---|---|
| `Hazard Event` | A discrete hazard occurrence treated as evidence or a released derivative within Hazards. | `HazardEvent` | `observed` |
| `historical_event_record` | A record of a hazard event that has already occurred (the event is in the past). | `HazardEvent` | `observed` |
| `operational_warning` | An issued warning carried **as context only** — never as a KFM-authored alert. | `WarningContext` | `observed` *(CONFLICTED — see [§9](#9-boundary--anti-collapse-terms) and OQ-HAZ-GL-01)* |
| `operational_advisory` | An issued advisory carried as context only. | `AdvisoryContext` | `observed` *(CONFLICTED)* |
| `operational_watch` | An issued watch carried as context only. | (advisory/watch context) | `observed` *(CONFLICTED)* |
| `administrative_declaration` | A compiled administrative record such as a disaster declaration — not an observation, not a regulation. | `DisasterDeclaration` | `administrative` |
| `regulatory_context` | An authoritative regulatory determination (e.g., an NFHL flood-zone designation) cited as context — never as observed inundation. | `FloodContext` | `regulatory` |
| `scientific_observation` | A first-hand scientific reading tied to place and time. | `HazardObservation`, `EarthquakeEvent` | `observed` |
| `remote_sensing_detection` | A remote-sensing detection (e.g., active-fire pixel) — a detection, **not** ground truth; enters as `candidate` until reviewed. | `WildfireDetection`, `SmokeContext` | `observed` *(candidate until reviewed)* |
| `modeled_derivative` | A derived product from inputs, assumptions, or fitted parameters, carrying uncertainty and a model run receipt. | `SmokeContext`, `DroughtIndicator` | `modeled` |
| `resilience_analysis` | A planning-oriented analysis derived from released evidence. | `ResilienceSummary` | `modeled` or `aggregate` |
| `unknown_unclassified` | Material whose source role is not yet classified. | (none until classified) | DENY at admission; quarantine until reviewed |

> [!WARNING]
> `unknown_unclassified` is a **fail-closed** state, not a usable role: unclassified source role is denied at admission and quarantined until a steward classifies it. *(CONFIRMED — DOM-HAZ §12.I "unknown source roles are quarantined".)*

[↩ Back to top](#table-of-contents)

---

## 4. Term → source-role crosswalk

The Hazards dossier (§12.D) describes source roles in an `authority / observation / context / model` shorthand "as the source role requires." KFM schema field values, however, use the **canonical seven-role register** (Atlas §24.1.1): `observed / regulatory / modeled / aggregate / administrative / candidate / synthetic`. This crosswalk maps the dossier shorthand onto the canonical register so the two are not confused.

| Dossier shorthand (§12.D) | Canonical role (§24.1.1) | Note |
|---|---|---|
| `observation` | `observed` | Direct reading or first-hand record. |
| `authority` | (no canonical equivalent) | `authority` is **not** a canonical source role; it is dossier narration. Disambiguate to `regulatory` (legal force) or `administrative` (compiled record). |
| `context` | (usage posture, not a role) | "Contextual-only" describes how a carrier may be used, not a source role; the carrier still takes one of the seven roles. |
| `model` | `modeled` | Carries `ModelRunReceipt`. |
| — | `aggregate` | Published summary over a unit; carries `AggregationReceipt`. |
| — | `candidate` | Awaiting review; no PUBLISHED edge until promoted. |
| — | `synthetic` | Simulated/reconstructed/AI-generated; carries `RealityBoundaryNote`. |

> [!IMPORTANT]
> Source role is **set at admission and never upgraded by promotion** (Atlas §24.1.1 reading note). A modeled smoke trajectory never becomes an observation; a regulatory flood zone never becomes an observed flood event.

[↩ Back to top](#table-of-contents)

---

## 5. Object families

The fifteen Hazards object families are **CONFIRMED** (Atlas §12.B/E; ENCY §7.10). Identity basis is **PROPOSED** (`source id + object role + temporal scope + normalized digest`); temporal handling — keeping `source`, `observed`, `valid`, `retrieval`, `release`, and `correction` times distinct where material — is **CONFIRMED** (Atlas §12.E).

<details>
<summary><strong>Hazards object families (CONFIRMED list)</strong></summary>

| Object family | One-line role (INFERRED from name + §12.E) | Lane note |
|---|---|---|
| `HazardEvent` | A hazard occurrence as evidence or released derivative. | `observed`; historical record. |
| `HazardObservation` | A direct hazard observation tied to place + time. | `observed`. |
| `WarningContext` | An operational warning carried as context only. | `issue`/`expiry`/`freshness` mandatory; contextual-only. |
| `AdvisoryContext` | An operational advisory carried as context only. | `issue`/`expiry`/`freshness` mandatory; contextual-only. |
| `DisasterDeclaration` | An administrative declaration record. | `administrative`; never an observed event timeline. |
| `FloodContext` | Regulatory flood context (NFHL partner with Hydrology). | `regulatory`; never observed inundation. |
| `WildfireDetection` | A remote-sensing or reported wildfire detection. | `candidate` by default until reviewed. |
| `SmokeContext` | A modeled smoke trajectory / mask. | `modeled`; carries `ModelRunReceipt`. |
| `DroughtIndicator` | An aggregate/modeled drought indicator. | carries `AggregationReceipt` or `ModelRunReceipt`. |
| `EarthquakeEvent` | An observed earthquake event. | `observed`. |
| `HeatColdEvent` | A heat or cold event. | observed or modeled basis. |
| `ExposureSummary` | An exposure overlay summary. | derivative; cites `EvidenceBundle`; infrastructure-precision deny-default. |
| `ResilienceSummary` | A resilience summary. | derivative; review state. |
| `HazardTimeline` | A role-aware hazard timeline. | derivative; preserves source-role tags. |
| `ImpactArea` | An impact-area geometry. | derivative; preserves source role. |

> Token-casing note: the Atlas spells two of these as single tokens — `SmokeContext` and `ImpactArea` — and renders the rest as two-word display names ("Hazard Event", "Warning Context"). KFM casing is preserved exactly as the Atlas uses it; field realization is PROPOSED.

</details>

[↩ Back to top](#table-of-contents)

---

## 6. Source families

The ten Hazards source families are **CONFIRMED** (Atlas §12.D); their per-source **rights and current terms are NEEDS VERIFICATION**, and **sensitive joins fail closed** (Atlas §12.D).

| Source family | Canonical role(s) | Note |
|---|---|---|
| NOAA Storm Events / NCEI-style records | `observed` / `aggregate` | Historical events and counts. |
| NWS API — alerts / warnings / advisories / watches | operational, contextual-only *(role CONFLICTED — see OQ-HAZ-GL-01)* | Never KFM-authored alerting. |
| FEMA Disaster Declarations / OpenFEMA | `administrative` | Declaration index, not an observed event. |
| FEMA NFHL / MSC flood hazard | `regulatory` | Flood-zone designation; not observed inundation. |
| USGS Earthquake Catalog | `observed` | Continuous + revision windows. |
| USGS Water Data *(cross-lane to Hydrology)* | `observed` | Cited as flood/drought context. |
| NOAA HMS Fire & Smoke | `modeled` / `observed` | Analysis + direct detection. |
| NASA FIRMS active fire | `observed` (`candidate` until reviewed) | Detection ≠ ground truth. |
| Drought monitors (USDM / state) | `aggregate` / `modeled` | Weekly composite. |
| Kansas / local emergency management context | `administrative` | Steward-mediated. |

[↩ Back to top](#table-of-contents)

---

## 7. Cross-cutting KFM trust terms

These terms are **CONFIRMED** but **owned globally**, not by the Hazards lane. They are listed here for the Hazards reader's convenience; the authoritative definitions live in the operating contract, the Atlas glossary, and Directory Rules §19.

| Term | Meaning (CONFIRMED — Atlas Appendix A; contract; DR §19) |
|---|---|
| `EvidenceBundle` | Resolved evidence package supporting a claim — source, scope, provenance, policy, citation, review context. |
| `EvidenceRef` | A reference that must resolve to an `EvidenceBundle` before a claim carries public authority. |
| `SourceDescriptor` | Machine-readable source identity, source role, rights, cadence, access, steward, sensitivity, release posture. |
| `PolicyDecision` | Explicit allow / deny / restrict / abstain / error decision tied to user, purpose, release class, evidence, sensitivity. |
| `RuntimeResponseEnvelope` | Governed AI/API response wrapper carrying outcome, evidence context, citations, policy state, validation result. |
| `ReleaseManifest` | Released artifact set, digests, policy posture, rollback target. |
| `CorrectionNotice` | Record that a published claim was corrected: what changed, why, what derivatives were invalidated. |
| `RollbackCard` | Record of a rollback decision and the targeted prior release. |
| `RedactionReceipt` | Record of a public-safe field or geometry transformation. |
| `ModelRunReceipt` | Pins the inputs, parameters, and version that produced a modeled value. |
| `AggregationReceipt` | Records the bin/cell aggregation applied to protect underlying records. |
| `RealityBoundaryNote` | Statement that a carrier is synthetic or reconstructed and not direct evidence. |
| `Promotion` | A governed release state transition — **not** a file move. |
| `Trust membrane` | The boundary preventing raw/unreviewed/generated/internal state from becoming public truth. Operational form: `apps/governed-api/` (CONFIRMED at commit `b6a279…`). |
| `Governed API` | Interface enforcing evidence, policy, release, finite outcomes, and audit. |

[↩ Back to top](#table-of-contents)

---

## 8. Temporal vocabulary

The Hazards lane keeps several time fields **distinct where material** — collapsing them is a temporal-role validator failure. *(CONFIRMED — Atlas §12.E; DATA_LIFECYCLE §6.3.)*

| Time field | What it marks |
|---|---|
| `event_time` | When the hazard occurred. |
| `observed_time` | When the observation was taken. |
| `issue_time` | When an issuing authority published an operational message. |
| `valid_time` | The interval over which a record is asserted to hold. |
| `expiry_time` | When operational context becomes stale by the issuing authority's rules. |
| `source_time` | The source's own vintage/timestamp. |
| `retrieval_time` | When KFM retrieved the material. |
| `release_time` | When KFM published the derived artifact. |
| `correction_time` | When a published claim was corrected. |

> [!CAUTION]
> `freshness_state` (`current` / `stale` / `expired` / `unknown`, PROPOSED enum) is computed from `expiry_time` vs the current clock. **Expired operational context cannot render as current warning state.** *(CONFIRMED rule — DOM-HAZ §12.I; see DATA_LIFECYCLE §7.)*

[↩ Back to top](#table-of-contents)

---

## 9. Boundary & anti-collapse terms

| Term | Meaning | Status |
|---|---|---|
| `not_emergency_alert_system` | Envelope/banner flag asserting that a Hazards surface is not an alert authority and must redirect life-safety action to official sources. | PROPOSED field; CONFIRMED requirement (Atlas §24.9.2) |
| `official_source_link` | Deep link to the official issuing authority, required on operational-context surfaces. | PROPOSED field; CONFIRMED requirement |
| Source-role anti-collapse | The rule that observed / regulatory / modeled / aggregate / administrative / candidate / synthetic roles are never conflated. | CONFIRMED (Atlas §24.1) |
| Regulatory-as-observed collapse | DENY condition: an NFHL regulatory polygon cited as an observed flood event. | CONFIRMED DENY (Atlas §24.1.2) |
| Warning-as-life-safety collapse | DENY condition: an operational warning treated as a KFM-authored life-safety instruction. | CONFIRMED DENY (Atlas §24.9.2) |

> [!CAUTION]
> **OQ-HAZ-GL-01 (CONFLICTED).** Mapping `operational_warning` / `advisory` / `watch` to the canonical role `observed` is **not settled**: the seven-role register has no `context` role, so "contextual-only" is a usage posture layered on a role. `observed` is defensible (the issuance is a first-hand record of what the authority said) but risks the warning-as-life-safety collapse if downstream code reads `observed` as "observed hazard." Resolution path: ADR. Shared with `EXPANSION_PLAN.md` OQ-HAZ-EP-01.

[↩ Back to top](#table-of-contents)

---

## 10. Open questions

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-HAZ-GL-01 | What canonical `source_role` do `operational_warning` / `advisory` / `watch` take, given the register has no `context` role? | Schema owner + hazards steward | ADR (shared with EXPANSION_PLAN OQ-HAZ-EP-01) |
| OQ-HAZ-GL-02 | Should the Atlas §12.D `authority / observation / context / model` shorthand be formally reconciled to the §24.1.1 register in the Hazards dossier? | Schema owner | ADR or drift entry |
| OQ-HAZ-GL-03 | Do the INFERRED one-line glosses in §3 get promoted to CONFIRMED once `contracts/domains/hazards/` materializes definitions? | Docs steward + hazards steward | Repo inspection; contract authorship |
| OQ-HAZ-GL-04 | Is a global KFM glossary the home for the cross-cutting terms in §7, with this file pointing to it (avoiding duplicate definitions)? | Docs steward | Directory Rules check; ADR-S vocabulary |

[↩ Back to top](#table-of-contents)

---

## 11. Related docs

> Sibling-doc placement under `docs/domains/hazards/` is CONFIRMED by Directory Rules §12; specific file presence is NEEDS VERIFICATION.

- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating law; `CONTRACT_VERSION = "3.0.0"` *(CONFIRMED authority)*
- [`directory-rules.md`](../../../directory-rules.md) — placement; §12 Domain Placement Law; §19 glossary *(CONFIRMED)*
- [`docs/domains/hazards/README.md`](./README.md) — Hazards lane orientation *(file presence NEEDS VERIFICATION)*
- [`docs/domains/hazards/DATA_LIFECYCLE.md`](./DATA_LIFECYCLE.md) — lifecycle, freshness, receipt matrix *(sibling doc)*
- [`docs/domains/hazards/EXPANSION_BACKLOG.md`](./EXPANSION_BACKLOG.md) — backlog; home of DRIFT-HAZ-PATH-01 *(sibling doc)*
- [`docs/domains/hazards/EXPANSION_PLAN.md`](./EXPANSION_PLAN.md) — milestone plan; OQ-HAZ-EP-01 *(sibling doc)*
- [`docs/domains/hazards/FILE_SYSTEM_PLAN.md`](./FILE_SYSTEM_PLAN.md) — placement plan *(sibling doc)*
- `contracts/domains/hazards/` — object meaning (where §3/§5 definitions become canonical) *(placement CONFIRMED §12; presence NEEDS VERIFICATION)*
- `schemas/contracts/v1/domains/hazards/` — object shape *(placement CONFIRMED per ADR-0001 + §12)*
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) — global verification register
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — drift entries (DRIFT-HAZ-PATH-01)

---

### Footer

> **Label legend:** see [§2](#2-label-legend) · **Terms:** see [§3](#3-ubiquitous-language-confirmed-terms) · **Trust terms:** see [§7](#7-cross-cutting-kfm-trust-terms) · **Open questions:** see [§10](#10-open-questions)

**Last updated:** 2026-06-05 · **Maintainers:** `<hazards-domain-stewards-TBD>`, `<docs-steward-TBD>` · **Status:** draft · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Policy label:** public

[↩ Back to top](#table-of-contents)
