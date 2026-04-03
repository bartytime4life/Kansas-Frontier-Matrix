<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/REQUIRES-UUID
title: KFM Sovereignty
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: REQUIRES VERIFICATION
related: [docs/governance/README.md, docs/governance/ROOT_GOVERNANCE.md, docs/governance/ETHICS.md, policy/README.md, contracts/README.md, tests/README.md, .github/PULL_REQUEST_TEMPLATE.md]
tags: [kfm, governance, sovereignty]
notes: [Owner reflects current public `/docs/` CODEOWNERS coverage on main; UUID, dates, policy label, and any narrower file-specific ownership still need branch-local verification before merge.]
[/KFM_META_BLOCK_V2] -->

# KFM Sovereignty

Rights, stewardship, precision, and public-safe release law for KFM trust-bearing material.

> **Status:** draft standard · public `main` path, sibling docs, and `/docs/` owner coverage verified · machine enforcement and runtime emitters still need direct verification  
> **Owners:** `@bartytime4life`  
> ![Status](https://img.shields.io/badge/status-draft-orange?style=flat-square) ![Owners](https://img.shields.io/badge/owners-%40bartytime4life-1f6feb?style=flat-square) ![Branch](https://img.shields.io/badge/branch-main-24292f?style=flat-square) ![Doc](https://img.shields.io/badge/doc-sovereignty-0a7ea4?style=flat-square) ![Trust](https://img.shields.io/badge/trust-public--safe%20rules-6f42c1?style=flat-square) ![Precision](https://img.shields.io/badge/precision-conditional-b54708?style=flat-square) ![Review](https://img.shields.io/badge/review-required-f59e0b?style=flat-square) ![Repo](https://img.shields.io/badge/repo%20evidence-public%20main-lightgrey?style=flat-square)  
> **Quick jump:** [Scope](#scope) · [Verification posture](#verification-posture) · [Authority order](#authority-order-for-this-file) · [Repo fit](#repo-fit) · [Sovereignty law](#sovereignty-law) · [Truth path](#sovereignty-along-the-truth-path) · [Surface obligations](#release-and-surface-obligations) · [Lane burdens](#lane-specific-sovereignty-burdens) · [Proof objects](#typed-objects-and-proof) · [Adjacent surfaces](#adjacent-surfaces-and-handoffs) · [Known unknowns](#known-unknowns) · [Merge checklist](#merge-checklist)  
> **Repo fit:** `docs/governance/SOVEREIGNTY.md` · upstream [`./README.md`](./README.md) and [`./ROOT_GOVERNANCE.md`](./ROOT_GOVERNANCE.md) · sibling [`./ETHICS.md`](./ETHICS.md) · downstream [`../../policy/README.md`](../../policy/README.md), [`../../contracts/README.md`](../../contracts/README.md), [`../../tests/README.md`](../../tests/README.md)

> [!IMPORTANT]
> In KFM, discoverability is **not** the same as admissibility. FAIR-style discoverability helps, but it is not sufficient where care, sovereignty, privacy, exact-location risk, reuse limits, or cultural sensitivity burdens apply.

> [!NOTE]
> This file is the sovereignty-specific companion to root governance. The named sovereignty lenses below are a doctrine-preserving packaging layer; the underlying rules are more important than the labels themselves, and the labels must not be read as proof that every related schema, policy bundle, or runtime emitter already exists.

| At a glance | Working rule |
|---|---|
| Public-safe rule | Findable content is not automatically admissible or releasable |
| Authority rule | Authoritative truth stays upstream of graph/search/tile/scene/summary accelerators |
| Precision rule | Exact locations and sensitive context release only when rights and sensitivity burdens are closed |
| Runtime rule | Bounded runtime surfaces stay within `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` |
| Correction rule | Supersession, withdrawal, narrowing, and replacement stay visible |
| Mirror rule | Discovery mirrors are provenance anchors, not automatic origin authorities |

## Scope

This document defines how sovereignty works in KFM whenever a change could affect:

- rights, stewardship, or reuse posture
- exact-location exposure, geoprivacy, or culturally sensitive context
- public-safe versus generalized versus withheld release
- mirror-versus-origin authority distinctions
- runtime explanation over released evidence
- correction, withdrawal, supersession, or narrowing

Use this file to decide **how KFM should constrain exposure and meaning**.

Do not use this file to imply that a policy bundle, schema family, steward workflow, or runtime emitter already exists unless the branch under review proves it directly.

> [!WARNING]
> Sovereignty failures are usually not loud system crashes. They look like convenient overexposure, quiet authority drift, or polished prose that outruns review, rights, or sensitivity closure.

## Verification posture

| Label | Meaning in this file |
|---|---|
| **CONFIRMED** | Directly supported by March–April 2026 KFM doctrine or by current public repo evidence inspected on `main` |
| **INFERRED** | Strongly implied by repeated doctrine or adjacent repo surfaces, but not directly re-verified as mounted implementation |
| **PROPOSED** | Repo-ready wording, structure, or starter artifacts consistent with doctrine but not proven as active implementation |
| **UNKNOWN** | Not verified strongly enough in the current session to present as fact |
| **NEEDS VERIFICATION** | Owner, date, label, workflow, policy, or runtime detail that should be checked before merge |

> [!NOTE]
> Branch-local evidence outranks public `main`. If the branch under review proves a narrower or different reality, keep the doctrine and downgrade the packaging claim rather than forcing code or docs to mimic an outdated draft.

## Authority order for this file

| Priority | Source class | How this file should use it |
|---|---|---|
| **1** | Attached KFM doctrine and master architecture manuals | Anchor non-negotiable rules for truth path, trust membrane, publication, correction, and exact-location burden |
| **2** | Supporting March–April 2026 overlays | Deepen shell behavior, lane burdens, proof objects, and bounded runtime without outranking doctrine |
| **3** | Current public repo evidence on `main` | Confirm path existence, sibling governance docs, `/docs/` ownership coverage, and adjacent README surfaces |
| **4** | Official external rechecks | Use only for version-sensitive boundary facts; never let them silently override KFM law |

## Repo fit

| Item | Value |
|---|---|
| Path | `docs/governance/SOVEREIGNTY.md` |
| Action class | Revise existing governance standard on public `main`; preserve doctrine, strengthen repo fit, and tighten verification honesty |
| Role | Rights, stewardship, precision, and public-safe exposure standard for governance-significant material |
| Upstream | [`./README.md`](./README.md) · [`./ROOT_GOVERNANCE.md`](./ROOT_GOVERNANCE.md) |
| Verified sibling | [`./ETHICS.md`](./ETHICS.md) |
| Verified downstream documentation surfaces | [`../../policy/README.md`](../../policy/README.md) · [`../../contracts/README.md`](../../contracts/README.md) · [`../../tests/README.md`](../../tests/README.md) |
| Review/control-plane companion | [`../../.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md) |
| Directory owner coverage | `/docs/` currently maps to `@bartytime4life` in public `CODEOWNERS` |
| This file does **not** replace | Policy bundles, schemas, fixtures, steward workflows, runtime emitters, release proof packs, or incident runbooks |

### Current public repo signals

| Surface | What current public `main` confirms | What it does **not** confirm |
|---|---|---|
| `docs/governance/` | `README.md`, `ROOT_GOVERNANCE.md`, `ETHICS.md`, and `SOVEREIGNTY.md` are present | Additional governance surfaces beyond the visible set |
| `.github/CODEOWNERS` | Global fallback and `/docs/` ownership coverage both point to `@bartytime4life` | Narrower file-specific ownership below `/docs/` |
| `policy/`, `contracts/`, `tests/` | README surfaces exist and are linkable from governance docs | Mounted `.rego` bundles, schema inventories, fixtures, or runnable proof suites |
| `.github/workflows/` | README documentation surface exists | Checked-in workflow YAML gates, required checks, environment approvals, or rulesets |

[Back to top](#kfm-sovereignty)

## Sovereignty law

### Core determination

KFM sovereignty means that every outward-facing claim remains answerable to the same governing chain: source identity, support, time semantics, rights posture, sensitivity handling, review state, release scope, and correction lineage.

Operationally, that yields four non-negotiable consequences:

1. **Authority stays upstream.** Graphs, search indexes, tiles, scenes, summaries, exports, and model outputs may accelerate use, but they do not silently inherit canonical authority.
2. **Release is a governed state change.** A technically successful query, render, or file copy is not publication permission.
3. **Precision is conditional.** Exact coordinates, detailed site descriptions, and sensitive context are released only when policy, role, and exposure burden allow it.
4. **Explanation stays downstream of evidence.** Story, dossier, compare, and Focus surfaces may interpret released material, but they do not replace evidence, policy, or review state.

### Sovereignty lenses

The labels below are an organizing layer for repeated KFM doctrine. The **rules** are the load-bearing part.

| Sovereignty lens | Rule status | What it protects | Practical rule | Typical failure if ignored |
|---|---|---|---|---|
| Truth sovereignty | **CONFIRMED** | Canonical authority | Authoritative truth remains separate from derived projections and accelerators | Graph, search, tile, or summary layers drift into de facto truth |
| Stewardship sovereignty | **INFERRED** | Source and steward obligations | Source onboarding behaves like a contract carrying rights, sensitivity, support, and publication intent | Material moves downstream with unclear obligations or unclear steward role |
| Rights sovereignty | **CONFIRMED** | Reuse, redistribution, and care limits | No outward release without explicit rights posture and any required review | Public exposure of material with unresolved reuse or stewardship limits |
| Precision sovereignty | **CONFIRMED** | Exact coordinates and sensitive spatial context | Public-safe, generalized, withheld, or steward-only state must be explicit | Rare-species, archaeology, or oral-history sensitivity leaks through convenience layers |
| Release sovereignty | **CONFIRMED** | Governed publication state | Promotion emits review, decision, and release artifacts; deployment does not equal permission | A build or render is mistaken for a valid publication |
| Runtime sovereignty | **CONFIRMED** | Trust boundary at point of use | Public and ordinary shell surfaces read through governed APIs and evidence resolution only | UI, model runtime, or ops endpoints bypass policy and evidence controls |
| Correction sovereignty | **CONFIRMED** | Historical accountability | Supersession, narrowing, withdrawal, and replacement remain visible | Silent overwrite erases public lineage |
| Interpretive sovereignty | **CONFIRMED** | Meaning at the surface | Narrative, comparison, and AI-assisted explanation remain bounded by evidence, policy, and release state | Persuasive explanation strips uncertainty, support, or review context |

### Governing rules

#### 1. No silent authority transfer

No derived layer may quietly inherit authoritative status. That includes, at minimum, search indexes, graphs, vector stores, tiles, scenes, exports, cached summaries, retrieval layers, and model outputs.

#### 2. No sovereignty without admissibility

A resource is not admitted merely because it exists. Admission requires explicit identity, meaningful support, declared time semantics, stated method, reconstructable provenance, known rights posture, adequate validation, and review where required.

#### 3. No public sovereignty without policy closure

Every outward-facing value is a publication event. Rights, sensitivity, provenance, review state, release scope, and correction posture still apply even when a query succeeds technically.

#### 4. No precision release without burden review

If exact location, detailed description, or reconstruction context creates privacy, care, stewardship, or cultural risk, KFM must generalize, withhold, role-gate, or deny. It must not pretend that suppression means the underlying record never existed.

#### 5. No runtime sovereignty for AI

Generative assistance may retrieve, summarize, explain, compare, or draft over released scope. It may not become an uncited truth surface, a direct client path into canonical data, or a substitute for release state.

#### 6. No correction erasure

Post-release correction changes trust state visibly. It does not erase that a release, story, export, or answer has been narrowed, withdrawn, rebuilt, or superseded.

## Sovereignty along the truth path

```mermaid
flowchart LR
    A[Source edge] --> B[RAW]
    B --> C[WORK / QUARANTINE]
    C --> D[PROCESSED]
    D --> E[CATALOG / TRIPLET]
    E --> F[Decision + Review]
    F -->|public-safe unchanged| G[PUBLISHED]
    F -->|generalize| H[Generalized release]
    F -->|withhold / deny| I[Withheld or denied]

    G --> J[Governed API]
    H --> J

    G --> K[Derived delivery<br/>tiles · vectors · search · graph · scenes · exports]
    H --> K

    J --> L[Map · Timeline · Dossier · Story · Evidence Drawer · Focus]
    K --> J

    style I fill:#f8d7da,stroke:#b42318,color:#7a271a
    style H fill:#fff3cd,stroke:#b54708,color:#7a2e0e
    style G fill:#d1fadf,stroke:#027a48,color:#085d3a
```

The strongest sovereignty boundary is not raw storage versus display. It is the transition from candidate material into **catalog closure, decision, review, and release**. That is where KFM decides whether material is public-safe, generalized, withheld, or denied.

A valid negative result is still a governed result. In KFM, withholding and denial are not UX mistakes; they are often the most sovereign outcome available.

## Release and surface obligations

### Release-state handling matrix

| Requested outcome | Minimum governance requirement | Surface expectation |
|---|---|---|
| Public-safe unchanged | Rights and sensitivity clear; release artifacts emitted; review complete where required | Renderable with evidence drill-through and visible freshness/release state |
| Generalized | Exact representation unsafe but reduced-precision form approved | Surface labels generalization in place; no silent coordinate downgrade |
| Withheld / steward-only | Public release blocked but steward lane permitted | Public surface does not render protected detail; steward surface carries review context |
| Denied | Policy explicitly blocks the requested action or surface | User sees a denial state, not an unexplained absence |
| Partial | Coverage or corroboration incomplete | Surface discloses incompleteness in place |
| Stale-visible | Release still usable but beyond freshness tolerance | Surface shows stale-state cue and correction path |
| Superseded / withdrawn | Correction or replacement published | Surface preserves lineage and route to replacement |

### Trust-visible surface obligations

| Surface | Sovereignty-critical requirement |
|---|---|
| Map / Timeline | Keep time scope, freshness, and route-to-evidence visible |
| Dossier / Story | Preserve identity, dates, dependencies, evidence links, and correction state |
| Evidence Drawer | Expose bundle members, quote or preview context, transforms, and release state |
| Focus Mode | Stay scoped, cited, policy-checked, and limited to `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` |
| Export | Never outrun release scope, policy posture, or correction linkage |
| Review / Stewardship | Emit review and decision artifacts; no hidden approvals |

> [!NOTE]
> In KFM, a calm negative state is more sovereign than a fluent bluff.

## Lane-specific sovereignty burdens

Some KFM lanes carry a materially heavier sovereignty burden than others. The system should preserve those differences rather than flatten them into one publication rule.

| Lane or material family | Main sovereignty burden | Minimum public-safe posture |
|---|---|---|
| Archives, newspapers, oral histories, public memory, and heritage | Context, reuse limits, culturally sensitive material, provenance preservation | Prefer evidence-linked excerpts over decontextualized claims; never strip provenance |
| Ecology, biodiversity, flora, pollinators, wildlife, and protected areas | Rare-species exposure, geoprivacy, conservation sensitivity | Generalize, role-gate, or withhold where exact exposure creates harm |
| Archaeology and heritage 2.5D/3D | Site sensitivity, volumetric overexposure risk, 2D vs 3D burden | Use 3D only when it materially improves reasoning and still inherits the same policy and correction model |
| Land tenure, cadastral history, parcels, plats, and deeds | Legal meaning, OCR/geoparsing error risk, personal detail masking, temporal linking | Treat legal-description and parcel-history work as review-bearing lanes |
| Service areas, lifeline systems, and critical systems | Legal jurisdiction, service geography, and operational capacity are related but not identical | Preserve the distinction; avoid overclaiming service capacity from boundary data alone |
| Atmosphere, air quality, climate, EO, and scientific extension | Modeled vs observed distinction, time basis, calibration, and method visibility | Label modeled, assimilated, regulatory, and community-sensor material in place |

### Mirror and discovery caution

Discovery mirrors improve findability, but they do not replace origin authorities. A mirror may act as a provenance anchor; it is not automatically the sovereign source.

[Back to top](#kfm-sovereignty)

## Typed objects and proof

Sovereignty in KFM is carried by typed governance and release objects, not by prose alone.

| Object family | Why it matters |
|---|---|
| `SourceDescriptor` | Declares source identity, access, rights posture, sensitivity, support, and publication intent |
| `IngestReceipt` / `ValidationReport` | Prove landing and admissibility outcome before canonical trust is claimed |
| `DatasetVersion` | Carries authoritative candidate or promoted subject scope with support and time semantics |
| `CatalogClosure` / `DecisionEnvelope` / `ReviewRecord` | Make publication, rights, and review state machine-readable and auditable |
| `ReleaseManifest` / `ReleaseProofPack` | Make public-safe release explicit and reversible |
| `ProjectionBuildReceipt` | Proves derived delivery artifacts were built from known release scope |
| `EvidenceBundle` | Preserves inspectable support at the point of use |
| `RuntimeResponseEnvelope` | Makes outward runtime outcomes accountable |
| `CorrectionNotice` | Preserves visible lineage when public meaning changes |

### Runtime outcomes and surface states

Outward runtime surfaces should emit only:

- `ANSWER`
- `ABSTAIN`
- `DENY`
- `ERROR`

Trust-visible surface states should remain stable enough to test and explain:

- `promoted`
- `generalized`
- `partial`
- `stale-visible`
- `source-dependent`
- `conflicted`
- `withdrawn`
- `denied`
- `abstained`

## Adjacent surfaces and handoffs

| If the change is mainly about… | Read this first | Why |
|---|---|---|
| Root trust law, review triggers, or promotion behavior | [`./ROOT_GOVERNANCE.md`](./ROOT_GOVERNANCE.md) | Global governance law lives there; sovereignty is a focused companion, not a replacement |
| Ethical/public-consequence framing or persuasion risk | [`./ETHICS.md`](./ETHICS.md) | Ethics handles civic consequence, human impact, and interpretive responsibility beyond exposure control alone |
| Executable deny-by-default rules | [`../../policy/README.md`](../../policy/README.md) | Policy is where sovereignty must become reviewable machine behavior |
| Typed trust objects and schema families | [`../../contracts/README.md`](../../contracts/README.md) | This file names proof-object families; contract ownership lives elsewhere |
| Fixtures, validation, and negative-path proof | [`../../tests/README.md`](../../tests/README.md) | Sovereignty rules are only trustworthy if deny/generalize/withdraw paths are tested |
| Review routing and change burden capture | [`../../.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md) | Governance-significant changes should carry explicit validation, risk, rollback, and truth-posture notes |

## Known unknowns

> [!CAUTION]
> The gaps below are governance-significant. They are not minor polish items.

| Unknown / needs verification | Why it matters |
|---|---|
| Real `doc_id`, created date, updated date, and policy label | Required to make the KFM meta block trustworthy instead of decorative |
| File-specific ownership below current `/docs/` coverage | Directory ownership is public; narrower doc stewardship may still differ |
| Mounted `.rego` bundles, policy fixtures, and sovereignty-specific tests | Needed to prove this standard already has machine enforcement rather than documentation only |
| Release proof-pack implementation | Promotion, rollback, and publication proof remain conceptual until one real example is surfaced |
| Runtime response envelope and Focus negative-path emitters | Cite-or-abstain, deny, and error behavior need direct implementation proof |
| Rights and sensitivity workflows for oral history, archaeology, biodiversity, and exact-location cases | These lanes require operational steward paths before broader outward expansion |
| Branch-local link targets, glossary anchors, and any newer companion standards | Public `main` is helpful; the branch under review remains decisive |

## Merge checklist

Before merge, verify:

- [ ] `doc_id`, dates, and `policy_label` in the meta block
- [ ] file-specific owner if it differs from current `/docs/` CODEOWNERS coverage
- [ ] branch-local relative links and any newer governance companions
- [ ] whether sovereignty-related policy bundles, fixtures, or tests were added in the same change stream
- [ ] whether any lane-specific steward workflow or reason/obligation vocabulary should be linked directly
- [ ] that this document does not silently overclaim mounted enforcement, runtime emitters, or release proof

[Back to top](#kfm-sovereignty)
