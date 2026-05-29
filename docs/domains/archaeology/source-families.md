<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/PLACEHOLDER-uuid
title: Archaeology — Source Families
type: standard
version: v1
status: draft
owners: <archaeology-domain-steward> + <source-steward> (PLACEHOLDER — confirm)
created: 2026-05-28
updated: 2026-05-28
policy_label: public
related: [docs/domains/archaeology/README.md, docs/domains/archaeology/pipeline-shape.md, docs/domains/archaeology/sensitivity-and-publication-posture.md, docs/domains/archaeology/cross-lane-relations.md, ai-build-operating-contract.md, directory-rules.md]
tags: [kfm, archaeology, sources, source-role, SourceDescriptor, sensitive-domain]
notes: [CONTRACT_VERSION = "3.0.0" pinned; source families CONFIRMED doctrine, rights/freshness NEEDS VERIFICATION, descriptor fields PROPOSED, repo not mounted this session]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🏺 Archaeology — Source Families

> The source families that feed the Archaeology lane, the source roles they carry, and the admission discipline that keeps an observation from being mistaken for a model — or a candidate for a confirmed site.

![status](https://img.shields.io/badge/status-draft-orange)
![policy](https://img.shields.io/badge/policy-public_doc-blue)
![sensitivity](https://img.shields.io/badge/sensitive_joins-fail_closed-critical)
![source--role](https://img.shields.io/badge/source_role-fixed_at_admission-purple)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![repo--state](https://img.shields.io/badge/rights_&_terms-NEEDS_VERIFICATION-yellow)

**Status:** `draft` · **Owners:** `<archaeology-domain-steward>` + `<source-steward>` (PLACEHOLDER) · **Updated:** 2026-05-28

> [!CAUTION]
> **Sensitive domain.** Several Archaeology source families carry exact site locations, burial, sacred, or steward-controlled content. **Sensitive joins fail closed.** No source family is admitted to a public surface without resolved rights, a fixed source role, and (where sensitivity applies) a transform receipt. Disposition is governed by `ai-build-operating-contract.md` §23.2.

---

## Quick jump

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. Source families](#3-source-families)
- [4. Source roles and the anti-collapse rule](#4-source-roles-and-the-anti-collapse-rule)
- [5. Role assignment guidance per family](#5-role-assignment-guidance-per-family)
- [6. SourceDescriptor fields](#6-sourcedescriptor-fields)
- [7. Anti-collapse failure modes](#7-anti-collapse-failure-modes)
- [8. Rights, sensitivity, and freshness](#8-rights-sensitivity-and-freshness)
- [9. Open questions register](#open-questions-register)
- [10. Open verification backlog](#open-verification-backlog)
- [11. Changelog](#changelog-v0--v1)
- [12. Definition of done](#definition-of-done)
- [Related docs](#related-docs)

---

## 1. Scope

This document inventories the **key source families** for the Archaeology / Cultural Heritage domain, the **source roles** each may carry, and the **admission discipline** (`SourceDescriptor`, role fixing, anti-collapse) that governs how those sources become evidence.

> [!NOTE]
> **Truth labels in this doc.** The eight source families are `CONFIRMED` doctrine (Atlas §15.D). The canonical source-role classes and the "role fixed at admission, never upgraded" rule are `CONFIRMED` doctrine (Atlas §24.1.1). Rights, current terms, and access methods for each specific family are `NEEDS VERIFICATION` (the Atlas itself labels them so). The `SourceDescriptor` field surface is `PROPOSED` (Atlas §24.1.3). All repo paths/schema presence are `PROPOSED` / `NEEDS VERIFICATION` (no repository mounted).

[↑ Back to top](#top)

---

## 2. Repo fit

| Aspect | Value | Status |
|---|---|---|
| Proposed path | `docs/domains/archaeology/source-families.md` | `PROPOSED` |
| Owning responsibility root | `docs/` (explains something to humans) | `CONFIRMED` rule |
| Domain segment | `archaeology` as a lane inside `docs/`, never a root | `CONFIRMED` rule |
| Source registry counterpart | `data/registry/sources/archaeology/` | `PROPOSED` |
| SourceDescriptor schema home | `schemas/contracts/v1/source/source-descriptor.json` (per Directory Rules §7.4 + ADR-0001) | `PROPOSED` / `NEEDS VERIFICATION` |
| Policy counterpart | `policy/sensitivity/archaeology/` | `PROPOSED` |
| Upstream (governs this doc) | `directory-rules.md`; `ai-build-operating-contract.md`; `[ENCY]` source doctrine | `CONFIRMED` rule / `PROPOSED` presence |

**Directory Rules basis.** A doc that *explains to humans* lives under `docs/`. The source **registry** (identity, rights, sensitivity) lives under `data/registry/` (or `data/registry/sources/<domain>/`); the **descriptor schema** lives under `schemas/`. This doc is navigational — the machine-readable `SourceDescriptor` and registry entries govern actual admission.

[↑ Back to top](#top)

---

## 3. Source families

`CONFIRMED` doctrine — Atlas §15.D. Each family may carry any of the canonical source roles **as the source requires**; the role is fixed per source at admission, not per family.

| Source family | Role (as required) | Rights / sensitivity | Freshness |
|---|---|---|---|
| State site inventory / SHPO or equivalent | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |
| Public NRHP-like listings | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |
| Field survey forms | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |
| Excavation records and provenience packets | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |
| Artifact / collection / repository records | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |
| Lab reports | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |
| Historic maps / plats / land records / newspapers | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |
| Oral history and cultural knowledge | authority / observation / context / model | rights and current terms `NEEDS VERIFICATION`; sensitive joins fail closed | source-vintage or cadence specific |

> [!WARNING]
> "Sensitive joins fail closed" is uniform across **all eight** families. A family that looks benign in isolation (e.g., historic newspapers) can expose an exact site when joined to inventory or excavation data; the join inherits the most restrictive sensitivity of either side.

[↑ Back to top](#top)

---

## 4. Source roles and the anti-collapse rule

`CONFIRMED` doctrine (Atlas §24.1.1). KFM treats **source role as a first-class identity attribute**. The role is set at admission in the `SourceDescriptor` and **preserved through every promotion** — promotion never upgrades a role.

| Role | Definition | Archaeology example | Allowed downstream |
|---|---|---|---|
| **Observed** | Direct reading or first-hand evidentiary record tied to place + time. | Ground archaeological observation; recorded find. | May feed modeled/aggregate products; never relabeled regulatory/administrative. |
| **Regulatory** | Authoritative determination by a governing body with legal/administrative force. | NRHP listing determination; SHPO eligibility ruling. | Cite as regulatory context; never an "observed" event. |
| **Modeled** | Derived product from inputs/assumptions; uncertainty preserved. | Remote-sensing / LiDAR anomaly interpretation; predictive site-sensitivity raster. | Cite with model identity + run receipt + bounds; never an observation. |
| **Aggregate** | Summary over a unit; individual fidelity lost. | Survey-coverage summary; site-density-by-county. | Cite with aggregation receipt; never a per-place record. |
| **Administrative** | Compiled agency record for administration/registration. | Land-office tract book; collection accession register. | Cite as administrative context; never collapsed with observation. |
| **Candidate** | Proposed record awaiting validation/dedup/review. | Unmerged site candidate; quarantined connector output. | Cited as candidate in WORK/QUARANTINE; **no `PUBLISHED` edge until merged**. |
| **Synthetic** | Generated by simulation/reconstruction/AI; no first-hand basis. | 3D reconstructed scene; AI-drafted summary. | Carries Reality Boundary Note + Representation Receipt; never queried as observed reality. |

> [!IMPORTANT]
> **Role is fixed at admission and never upgraded by promotion.** A `modeled` anomaly does not become `observed` because it was reviewed; a `CandidateFeature` does not become a confirmed `Archaeological Site` by moving stages. Those are separate governed transitions with their own evidence and review requirements.

[↑ Back to top](#top)

---

## 5. Role assignment guidance per family

`INFERRED` from the source-role definitions (§24.1.1) applied to the §15.D families. This is **drafting guidance**, not a fixed mapping — the actual role is set per source at admission and `NEEDS VERIFICATION` against each source's terms.

| Source family | Likely role(s) | Caution |
|---|---|---|
| State site inventory / SHPO | regulatory (eligibility rulings) **and/or** authority/administrative (inventory records) | Don't collapse a listing *determination* with an *observation* of a site. |
| Public NRHP-like listings | regulatory | A listing is a determination, not a field observation. |
| Field survey forms | observed | First-hand; feeds modeled/aggregate but is not itself a model. |
| Excavation records / provenience packets | observed | Highest-sensitivity geometry; fails closed by default. |
| Artifact / collection / repository records | administrative (accession) / observed (find context) | Collection security is sensitive; keep accession ≠ find-location. |
| Lab reports | observed (measurements) / modeled (derived estimates) | Separate a measured value from a fitted estimate. |
| Historic maps / plats / land records / newspapers | administrative / context | Historical compilation, not observation of a present site. |
| Oral history and cultural knowledge | context / authority (steward-held) | Steward-controlled; route through Indigenous/cultural §23.2 row. |

[↑ Back to top](#top)

---

## 6. SourceDescriptor fields

`PROPOSED` descriptor surface (Atlas §24.1.3) — illustrative, not authoritative. Schema home defaults to `schemas/contracts/v1/source/source-descriptor.json` per Directory Rules §7.4 and ADR-0001 unless an accepted ADR relocates it (`NEEDS VERIFICATION`: actual file presence and field names).

<details>
<summary><strong>Role-bearing SourceDescriptor fields (PROPOSED — §24.1.3)</strong></summary>

| Field | Type / vocabulary | Required? | Notes |
|---|---|---|---|
| `source_role` | enum: observed \| regulatory \| modeled \| aggregate \| administrative \| candidate \| synthetic | MUST | Set at admission. Never edited in-place; corrections produce a **new** descriptor + `CorrectionNotice`. |
| `role_authority` | string (issuing body / model identity / steward) | MUST when role ∈ {regulatory, modeled, aggregate} | Disambiguates the authoring authority for cite text. |
| `role_aggregation_unit` | geometry-scope token (county, HUC, tract, year…) | MUST when `source_role = aggregate` | Prevents geometry-scope drift on join. |
| `role_model_run_ref` | `EvidenceRef → ModelRunReceipt` | MUST when `source_role = modeled` | Pins inputs, parameters, version. |
| `role_synthetic_basis` | `{ method, inputs, reality_boundary_note_ref }` | MUST when `source_role = synthetic` | Records what is and isn't real in the carrier. |
| `role_candidate_disposition` | enum: pending \| merged \| rejected \| quarantined | MUST when `source_role = candidate` | Tracks promotion state; `PUBLISHED` edge forbidden until merged. |

</details>

`SourceDescriptor` more broadly records source identity, role, rights posture, update cadence, authority scope, sensitivity, and verification obligations. Descriptors `SHOULD` be validated before fetch, before transformation, and before publication, so source authority does not collapse into generic data availability.

[↑ Back to top](#top)

---

## 7. Anti-collapse failure modes

`CONFIRMED` doctrine (Atlas §24.1.2) — the DENY conditions most relevant to Archaeology sources:

| Collapse pattern | Denied outcome | Required guardrail |
|---|---|---|
| Modeled product (e.g., LiDAR anomaly) labeled or queried as observed site | `DENY` at publication; `ABSTAIN` at AI surface | Run receipt + uncertainty surface + role-preserving DTO field |
| Candidate record exposed on a public surface | `DENY` at trust membrane; route to `QUARANTINE` | Promotion gate; no `PUBLISHED` edge to WORK/QUARANTINE |
| Synthetic content (3D reconstruction) presented as observed reality | `DENY` publication; `HOLD` for steward review; `ABSTAIN` at AI | Reality Boundary Note; Representation Receipt; UI badge |
| Administrative compilation cited as observation | `DENY` publication of compilation as observed timeline | Source-role tag preserved; named record types |
| Aggregate (survey-coverage summary) cited as per-place truth | `DENY` join from aggregate to single record; `ABSTAIN` at AI | Aggregation receipt; geometry-scope guard |

> [!CAUTION]
> The LiDAR/remote-sensing path is the highest-risk collapse for Archaeology: an anomaly is `modeled`/`candidate`, not an `observed` site. The role-preserving DTO field and the `candidate ≠ site` guardrail must survive every transformation.

[↑ Back to top](#top)

---

## 8. Rights, sensitivity, and freshness

`CONFIRMED` doctrine / per-source `NEEDS VERIFICATION`:

- **Rights and current terms** — `NEEDS VERIFICATION` for every family. A source is not admitted until its license, terms, attribution, and access method are resolved in its `SourceDescriptor`. Rights or sovereignty status can change without notice; stale-state markers and a freshness cadence apply.
- **Sensitivity** — sensitive joins fail closed across all families; oral history and cultural knowledge route through the Indigenous/cultural §23.2 row and require steward authority.
- **Freshness** — "source-vintage or cadence specific": some families are point-in-time vintages (a 1900 plat), others have an update cadence (an active state inventory). The descriptor records which, and stale citations force `ABSTAIN` downstream.

> [!IMPORTANT]
> Rights-change detection across third-party sources is **not automated** (a known residual risk). A periodic rights/sensitivity re-evaluation is required; do not assume a once-cleared source stays cleared.

[↑ Back to top](#top)

---

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-ARCH-SRC-01 | What are the actual rights and current terms for each of the eight families? | source steward | source-by-source review |
| OQ-ARCH-SRC-02 | Does `SourceDescriptor` live at `schemas/contracts/v1/source/source-descriptor.json`, per ADR-0001? | schema steward | repo inspection / ADR confirmation |
| OQ-ARCH-SRC-03 | Which families route through the Indigenous/cultural §23.2 row by default (oral history, steward-held records)? | tribal/cultural reviewer | steward ratification |
| OQ-ARCH-SRC-04 | What is the freshness cadence and stale-out tolerance per active-inventory source? | source steward | repo inspection |

## Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Verify rights and current terms for all eight source families.
2. Verify the `SourceDescriptor` schema home and the §24.1.3 field set against the mounted repo.
3. Verify `data/registry/sources/archaeology/` exists and records source roles.
4. Verify the source-role anti-collapse validators exist (Atlas §15.K lists "candidate-not-site" as `PROPOSED`).
5. Confirm the per-family role assignment guidance (§5) against each source's terms.

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial draft of Archaeology source families | new | Synthesizes Atlas §15.D + §24.1.1–§24.1.3 source-role doctrine |
| Pinned `CONTRACT_VERSION = "3.0.0"` | clarification | Doctrine-adjacent doc requirement |

> **Backward compatibility.** New document; no prior anchors to preserve. Section anchors are stable for future revisions.

## Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (`docs/domains/archaeology/`);
- a docs steward, the archaeology domain steward, and a source/rights steward review it;
- it is linked from the archaeology lane README and the source/doctrine index;
- it does not conflict with accepted ADRs (notably ADR-0001 on the SourceDescriptor home);
- any conflict with current repo conventions is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in Section 2 is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

---

## Related docs

- `docs/domains/archaeology/README.md` — archaeology lane landing page (`PROPOSED`)
- `docs/domains/archaeology/sensitivity-and-publication-posture.md` — sibling sensitivity doc (`PROPOSED`)
- `docs/domains/archaeology/pipeline-shape.md` — sibling lifecycle doc (`PROPOSED`)
- `docs/domains/archaeology/cross-lane-relations.md` — sibling cross-lane doc (`PROPOSED`)
- `ai-build-operating-contract.md` — source-role anti-collapse, §23.2 matrix (canonical)
- `schemas/contracts/v1/source/source-descriptor.json` — SourceDescriptor schema home (`PROPOSED`, per ADR-0001)

**Last updated:** 2026-05-28 · `CONTRACT_VERSION = "3.0.0"`

[↑ Back to top](#top)
