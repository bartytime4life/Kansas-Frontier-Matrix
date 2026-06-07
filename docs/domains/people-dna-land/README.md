<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-people-dna-land-readme
title: People, Genealogy, DNA, and Land Ownership — Domain Landing Doc
type: standard
subtype: domain-readme
version: v1.1
status: draft
owners: Docs steward; Domain steward (People/DNA/Land); Sensitivity reviewer; Rights-holder representative; Release authority
created: 2026-05-19
updated: 2026-06-07
policy_label: public-doctrine
contract_version: "3.0.0"
related:
  - docs/doctrine/directory-rules.md
  - docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md         # authored prior session (v0.1)
  - docs/domains/people-dna-land/PEOPLE_PRESERVATION_MATRIX.md  # authored prior session (v0.2)
  - docs/domains/people-dna-land/MISSING_OR_PLANNED_FILES.md    # authored prior session (v0.2)
  - docs/domains/people-dna-land/EXPANSION_PLAN.md
  - docs/domains/people-dna-land/sublanes/genealogy.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - docs/standards/PROV.md
tags: [kfm, domain, people, genealogy, dna, land, sensitive]
notes:
  - CONTRACT_VERSION pinned to 3.0.0 per ai-build-operating-contract.md.
  - Domain landing doc for the most sensitivity-loaded lane in KFM.
  - All repo-state claims are PROPOSED until verified against a mounted repository.
  - Default sensitivity posture for living-person, DNA, and private person-parcel joins is deny-by-default (T4).
  - "OPEN CONFLICT (new in v1.1): Atlas Ch. 24.13 crosswalk uses the short segment 'people' for schemas/contracts/policy-sensitivity/policy-consent roots; Directory Rules §6.1/§12 examples use 'people-dna-land' for docs/ and domains/ segments. Tracked as OQ-PDL-SEG-01; see §2.1 and §22."
[/KFM_META_BLOCK_V2] -->

# People, Genealogy, DNA, and Land Ownership

> The kinship, consent, and land-record slice of KFM — where unsourced family-tree folklore, raw DNA, vendor exports, and chain-of-title fragments meet the trust membrane. **Living-person and DNA-derived outputs are denied or restricted by default.**

<!-- Badges -->
![Status: draft](https://img.shields.io/badge/status-draft-blue)
![Authority: canonical](https://img.shields.io/badge/authority-canonical-1f6feb)
![Sensitivity: T4 default](https://img.shields.io/badge/sensitivity-T4%20default-critical)
![Promotion: deny-by-default](https://img.shields.io/badge/promotion-deny--by--default-darkred)
![Doctrine: Atlas v1.1 Ch. 16](https://img.shields.io/badge/doctrine-Atlas%20v1.1%20Ch.%2016-purple)
![Segment: CONFLICTED](https://img.shields.io/badge/segment%20naming-CONFLICTED-orange)
![CONTRACT_VERSION: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![Last reviewed: 2026-06-07](https://img.shields.io/badge/last%20reviewed-2026--06--07-lightgrey)

| Field          | Value                                                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Status**     | `draft` — landing doc seeded; sublane docs and verification backlog open                                                    |
| **Owners**     | Docs steward · Domain steward (People/DNA/Land) · Sensitivity reviewer · Rights-holder representative · Release authority   |
| **Updated**    | 2026-06-07                                                                                                                  |
| **Authority**  | Canonical for the People/Genealogy/DNA/Land doctrine surface inside `docs/` *(per Directory Rules §6.1)*                    |
| **Implements** | Atlas v1.1 Ch. 16; Encyclopedia §7.14 *(section number NEEDS VERIFICATION)*; Directory Rules §6.1, §12; Pass-10 C6 (Sensitivity) & C9 (Genealogy/DNA) |

> [!IMPORTANT]
> This domain inherits the strictest defaults in KFM. Living-person fields, raw DNA segment data, private person-parcel joins, and DNA-derived hypotheses are **T4 (Denied) by default**. Promotion to any public tier requires an explicit transform, a recorded receipt, named review, and — for living persons and DNA — scoped, revocable consent. Doctrine: `[DOM-PEOPLE]`, `[ENCY]`, Atlas v1.1 Ch. 24.5.

> [!WARNING]
> **Segment-name conflict (OQ-PDL-SEG-01, new in v1.1).** Two CONFIRMED sources disagree on the domain segment. Directory Rules §6.1/§12 examples use **`people-dna-land`** (for `docs/domains/`, `policy/domains/`, `tests/domains/`, etc.); Atlas Ch. 24.13 crosswalk row 16 uses the short segment **`people`** (for `schemas/contracts/v1/people/`, `contracts/people/`, `policy/sensitivity/people/`, `policy/consent/people/`). This README uses `people-dna-land` where Directory Rules gives an explicit example, and `<segment>` for the four crosswalk-only roots, pending ADR. See [§2.1](#21-segment-naming-conflict) and [§22](#22-adrs).

---

## Mini-TOC

- [1. Scope and one-line purpose](#1-scope-and-one-line-purpose)
- [2. Authority level](#2-authority-level)
  - [2.1 Segment-naming conflict](#21-segment-naming-conflict)
- [3. Status](#3-status)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does NOT belong here](#5-what-does-not-belong-here)
- [6. Repo fit](#6-repo-fit)
- [7. Directory layout (this folder)](#7-directory-layout-this-folder)
- [8. Responsibility shape (diagram)](#8-responsibility-shape-diagram)
- [9. Ubiquitous language](#9-ubiquitous-language)
- [10. Object families](#10-object-families)
- [11. Inputs — key source families](#11-inputs--key-source-families)
- [12. Outputs and viewing products](#12-outputs-and-viewing-products)
- [13. Pipeline shape (RAW → PUBLISHED)](#13-pipeline-shape-raw--published)
- [14. Sensitivity, rights, and publication posture](#14-sensitivity-rights-and-publication-posture)
- [15. Cross-lane relations](#15-cross-lane-relations)
- [16. API, contract, and schema surfaces](#16-api-contract-and-schema-surfaces)
- [17. Validation](#17-validation)
- [18. Review burden and separation of duties](#18-review-burden-and-separation-of-duties)
- [19. Governed AI behavior](#19-governed-ai-behavior)
- [20. Publication, correction, and rollback](#20-publication-correction-and-rollback)
- [21. Open questions and verification backlog](#21-open-questions-and-verification-backlog)
- [22. ADRs](#22-adrs)
- [23. Related docs and folders](#23-related-docs-and-folders)
- [24. Appendix — extended reference](#24-appendix--extended-reference)
- [Truth labels used here](#truth-labels-used-here)

---

## 1. Scope and one-line purpose

**One-line purpose.** *(CONFIRMED doctrine / PROPOSED implementation.)* Govern assertion-first person evidence, genealogy relationships, restricted DNA evidence, land instruments, ownership intervals, chain-of-title reasoning, consent, policy decisions, review, correction, graph projection, EvidenceBundle views, and rollback for the People / Genealogy / DNA / Land Ownership lane.

The full canonical name of this domain per Atlas v1.1 Ch. 16 is **"People, Genealogy, DNA, and Land Ownership."** The folder name `people-dna-land` is the abbreviated form adopted in Directory Rules §6.1's `docs/domains/` sub-listing; both refer to the same lane. *(CONFIRMED doctrine; `docs/domains/people-dna-land/` folder name CONFIRMED in directory-rules.md §6.1. Note the schema/contract/policy-sensitivity segment is **CONFLICTED** — see [§2.1](#21-segment-naming-conflict).)*

This domain is the most ethically loaded lane in KFM. The corpus is explicit that:

- **Person assertions are evidence, not facts.** Identity is an `EvidenceBundle` view over named, time-stamped assertions; canonicalization is a derived role bounded by source role and review state. *(CONFIRMED doctrine, `[DOM-PEOPLE]` §A, §E.)*
- **DNA crosses the publication boundary only as aggregate or k-anonymized derivatives.** Raw vendor IDs, segment data, and triangulation outputs never become public. *(CONFIRMED doctrine, Pass-10 C9-03.)*
- **Assessor and tax records are not title truth.** Parcel geometry is not boundary proof without source role and evidence. *(CONFIRMED doctrine, `[DOM-PEOPLE]` §I.)*
- **Consent is revocable.** Revocation triggers tombstoning, downstream cleanup, and embargo-cache invalidation. *(CONFIRMED doctrine, Pass-10 C5-09 / C6-08; FamilySearch revocation path C9-02.)*

> [!CAUTION]
> Any reviewer who finds a person, DNA, or land artifact in a public path without supporting `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, and `ReleaseManifest` should treat that artifact as **drift** and file against `docs/registers/DRIFT_REGISTER.md` *(PROPOSED register, per Directory Rules §13)*. Default-deny promotion is a core invariant; bypasses are not normalized through use.

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 2. Authority level

**Authority class:** **Canonical** for the People/Genealogy/DNA/Land doctrine surface inside `docs/`. *(CONFIRMED per Directory Rules §6.1 — `docs/domains/people-dna-land/` is listed as a canonical sub-tree of the human-facing control plane.)*

This README **explains**. It does not define schemas (those live under `schemas/contracts/v1/<segment>/` — *PROPOSED; segment CONFLICTED*), does not define object meaning machine-readably (that lives under `contracts/<segment>/` — *PROPOSED*), does not decide allow/deny (that lives under `policy/domains/people-dna-land/` plus `policy/sensitivity/<segment>/` and `policy/consent/<segment>/` — *PROPOSED*), and does not store data (that lives under `data/<phase>/people-dna-land/` — *PROPOSED*).

> [!NOTE]
> Per Directory Rules §5/§6.1, `docs/` **explains**; `control_plane/` **indexes**; `contracts/` **defines meaning**; `schemas/` **defines shape**; `policy/` **decides admissibility**; `tests/fixtures/` **proves rules are enforceable**. This README sits in the first row of that table.

### 2.1 Segment-naming conflict

> [!WARNING]
> **CONFLICTED — resolve before any `schemas/`, `contracts/`, or `policy/sensitivity/` file in this lane is authored as canonical.** Tracked as **OQ-PDL-SEG-01** (see [§22](#22-adrs)).

| Source (CONFIRMED) | Root family | Segment | Example |
|---|---|---|---|
| **Directory Rules §6.1, §6.5, §6.6, §12** | `docs/domains/`, `policy/domains/`, `tests/domains/`, `fixtures/domains/`, `packages/domains/`, `pipelines/domains/`, `data/<phase>/` | **`people-dna-land`** | `docs/domains/people-dna-land/`, `policy/domains/people-dna-land/` |
| **Atlas Ch. 24.13 crosswalk (row 16)** | `schemas/`, `contracts/`, `policy/sensitivity/`, `policy/consent/` | **`people`** | `schemas/contracts/v1/people/`, `policy/consent/people/` |

**Resolution posture (per operating-contract source hierarchy + Directory Rules §0):** Directory Rules wins on placement where it gives an explicit example, so the `docs/domains/`, `policy/domains/`, `tests/domains/`, `fixtures/domains/`, and `data/<phase>/` segments are written **`people-dna-land`**. The four crosswalk-only roots are written **`<segment>`** and annotated, because the crosswalk says `people` while the lane convention says `people-dna-land`. No `schemas/`, `contracts/`, or `policy/sensitivity/` file is authored as canonical until the ADR lands. v1 of this README used `people-dna-land`/`domains/` for *all* roots, including the four the crosswalk assigns to `people`; v1.1 surfaces the divergence.

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 3. Status

| Item                                  | Status                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Doctrine source (Atlas v1.1 Ch. 16)   | **CONFIRMED**                                                                                     |
| Folder placement (`docs/domains/people-dna-land/`) | **CONFIRMED** (Directory Rules §6.1)                                                 |
| Segment name for `schemas/`/`contracts/`/`policy/sensitivity/` | **CONFLICTED** — `people` vs `people-dna-land` (OQ-PDL-SEG-01)               |
| Sublane convention (`sublanes/<x>.md`)| **PROPOSED** — pending ADR (see [§22](#22-adrs))                                                   |
| Schema home, contracts, policy paths  | **PROPOSED** — all segments labeled PROPOSED until mounted-repo check                              |
| Validator and CI coverage             | **NEEDS VERIFICATION** — no workflow, log, or test inspected this session                          |
| Source-family rights and currentness  | **NEEDS VERIFICATION** per source                                                                  |
| Living-person, DNA, and parcel-join lanes | **CONFIRMED doctrine** for deny-by-default / **PROPOSED implementation**                       |

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 4. What belongs here

This folder (`docs/domains/people-dna-land/`) holds **human-facing doctrine** for the People/Genealogy/DNA/Land lane. Concretely:

- A landing README (this file).
- A domain model (`PEOPLE_DOMAIN_MODEL.md`) — bounded context, identity rules, aggregates, invariants. *(CONFIRMED authored, prior session; mounted-repo presence NEEDS VERIFICATION.)*
- A preservation matrix (`PEOPLE_PRESERVATION_MATRIX.md`) — retention, tombstone, erasure duties. *(CONFIRMED authored, prior session.)*
- A file inventory (`MISSING_OR_PLANNED_FILES.md`). *(CONFIRMED authored, prior session.)*
- One Markdown file per **sublane** (genealogy, DNA, land, person identity) — *sublane folder convention PROPOSED, see [§22](#22-adrs)*.
- A domain `EXPANSION_PLAN.md` describing roadmap and thin-slice ordering. *(CONFIRMED authored, prior session.)*
- Worked-example notes (illustrative records, redaction walkthroughs) that explain the doctrine without leaking sensitive data.
- Cross-references into `contracts/`, `schemas/`, `policy/`, `tests/`, `release/`, and `runbooks/`.

> [!TIP]
> If a file you are about to add is **machine-readable**, it does not belong here. Send it to `control_plane/`, `schemas/`, `policy/`, or `contracts/` per Directory Rules §4 (Placement Protocol).

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 5. What does NOT belong here

The following **explicitly do not belong** under `docs/domains/people-dna-land/`. Segments marked `<segment>` are subject to the [§2.1 conflict](#21-segment-naming-conflict).

| Type of content                                            | Goes to instead                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Machine-readable schemas (`*.schema.json`, `*.shacl`, …)   | `schemas/contracts/v1/<segment>/` *(PROPOSED; segment CONFLICTED)*             |
| Object-meaning contracts (Markdown semantic specs)         | `contracts/<segment>/` *(PROPOSED; segment CONFLICTED)*                        |
| OPA / policy bundles (domain admissibility)                | `policy/domains/people-dna-land/` *(PROPOSED)*                                 |
| Sensitivity policy fragments                               | `policy/sensitivity/<segment>/` *(PROPOSED; segment per Atlas Ch. 24.13)*      |
| Consent-token policy fragments                             | `policy/consent/<segment>/` *(PROPOSED; segment per Atlas Ch. 24.13)*          |
| Living-person, DNA, parcel records (RAW/WORK/PUBLISHED)    | `data/<phase>/people-dna-land/` *(PROPOSED)*                                   |
| Validator and test code                                    | `tests/domains/people-dna-land/` and `tools/validators/` *(PROPOSED)*          |
| Golden / valid / invalid fixtures                          | `fixtures/domains/people-dna-land/` *(PROPOSED)*                               |
| Release manifests, rollback cards, correction notices      | `release/` *(PROPOSED)*                                                        |
| Source descriptors (per-source admission records)          | `data/registry/sources/people-dna-land/` *(PROPOSED)*                          |
| Settlements/roads/archaeology context that *cites* this lane | The owning domain's `docs/domains/<…>/` folder                               |
| Runbooks for refreshes, rollbacks, drills                  | `docs/runbooks/people-dna-land/` *(PROPOSED, subfolder convention pending ADR)* |

> [!WARNING]
> **Living-person sample data must never appear in this folder, even as an example.** Use synthetic fixtures (`fixtures/synthetic/people-dna-land/`) or census-historical (deceased, public-domain) data only. *(CONFIRMED doctrine; Pass-10 C6.)*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 6. Repo fit

Segments marked `<segment>` are subject to the [§2.1 conflict](#21-segment-naming-conflict).

| Aspect                  | Value                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This folder**         | `docs/domains/people-dna-land/`                                                                                                                    |
| **Parent**              | [`../README.md`](../README.md) — `docs/domains/` landing *(PROPOSED authoring)*                                                                    |
| **Authority root**      | `docs/` (canonical) — Directory Rules §6.1                                                                                                         |
| **Upstream doctrine**   | Atlas v1.1 Ch. 16; Encyclopedia §7.14 *(section NEEDS VERIFICATION)*; Directory Rules §6.1 & §12; Pass-10 C6, C9, C14; Unified Implementation Architecture Build Manual |
| **Sibling docs (this folder)** | [`PEOPLE_DOMAIN_MODEL.md`](PEOPLE_DOMAIN_MODEL.md) *(CONFIRMED authored)* · [`PEOPLE_PRESERVATION_MATRIX.md`](PEOPLE_PRESERVATION_MATRIX.md) *(CONFIRMED authored)* · [`MISSING_OR_PLANNED_FILES.md`](MISSING_OR_PLANNED_FILES.md) *(CONFIRMED authored)* |
| **Sublanes (children)** | [`sublanes/genealogy.md`](sublanes/genealogy.md) *(CONFIRMED authored)* · `sublanes/dna.md` *(PROPOSED)* · `sublanes/land.md` *(PROPOSED)* · `sublanes/person-identity.md` *(PROPOSED)* |
| **Roadmap**             | [`EXPANSION_PLAN.md`](EXPANSION_PLAN.md) *(CONFIRMED authored)*                                                                                    |
| **Downstream implementation** | `contracts/<segment>/…` · `schemas/contracts/v1/<segment>/…` · `policy/domains/people-dna-land/…` · `tests/domains/people-dna-land/…` · `fixtures/domains/people-dna-land/…` — **all PROPOSED** |
| **Public surface**      | `apps/governed-api/` resolvers and `apps/explorer-web/` Evidence Drawer / Focus Mode payloads — **all PROPOSED**                                   |

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 7. Directory layout (this folder)

> [!NOTE]
> Tree is **PROPOSED**. Mounted-repo verification required before any node is treated as canonical. Sublane folder convention (`sublanes/`) is not yet ratified in Directory Rules; see [§22 ADR-D-01](#22-adrs).

```text
docs/domains/people-dna-land/
├── README.md                          # this file
├── PEOPLE_DOMAIN_MODEL.md             # CONFIRMED authored — bounded context, identity, aggregates, invariants
├── PEOPLE_PRESERVATION_MATRIX.md      # CONFIRMED authored — retention, tombstone, erasure duties
├── MISSING_OR_PLANNED_FILES.md        # CONFIRMED authored — file inventory across responsibility roots
├── EXPANSION_PLAN.md                  # CONFIRMED authored — roadmap, thin-slice ordering
└── sublanes/                          # PROPOSED — convention pending ADR (see §22)
    ├── genealogy.md                   # CONFIRMED authored — kinship & life-event slice
    ├── dna.md                         # PROPOSED — DTC exports, GA4GH, consent, revocation
    ├── land.md                        # PROPOSED — patents, deeds, instruments, ownership intervals, chain-of-title
    └── person-identity.md             # PROPOSED — assertion-first identity, PersonCanonical, RelationshipAssertion
```

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 8. Responsibility shape (diagram)

The diagram below shows how this **doctrine surface** (`docs/domains/people-dna-land/`) relates to the canonical roots it explains. It is illustrative — not an implementation diagram. Segment names marked `<segment>` are subject to the [§2.1 conflict](#21-segment-naming-conflict).

```mermaid
flowchart LR
    subgraph DOCS["docs/domains/people-dna-land/  (this folder — CANONICAL doctrine)"]
        R["README.md"]
        M["PEOPLE_DOMAIN_MODEL.md"]
        PM["PEOPLE_PRESERVATION_MATRIX.md"]
        E["EXPANSION_PLAN.md"]
        SG["sublanes/genealogy.md"]
        SD["sublanes/dna.md"]
        SL["sublanes/land.md"]
        SP["sublanes/person-identity.md"]
    end

    subgraph IMPL["Implementation roots (all PROPOSED for this domain)"]
        C["contracts/&lt;segment&gt;/"]
        S["schemas/contracts/v1/&lt;segment&gt;/"]
        P["policy/domains/people-dna-land/ + policy/sensitivity/&lt;segment&gt;/ + policy/consent/&lt;segment&gt;/"]
        T["tests/domains/people-dna-land/"]
        F["fixtures/domains/people-dna-land/"]
        D["data/&lt;phase&gt;/people-dna-land/"]
        REL["release/candidates/people-dna-land/"]
    end

    subgraph PUBLIC["Public surface (governed; PROPOSED)"]
        API["apps/governed-api/ People/DNA/Land resolvers"]
        UI["apps/explorer-web/ Evidence Drawer + Focus Mode"]
    end

    R --- M
    R --- PM
    R --- E
    R --- SG
    R --- SD
    R --- SL
    R --- SP

    DOCS -. "explains" .-> IMPL
    IMPL --> REL
    REL --> API
    API --> UI

    classDef canon fill:#dbeafe,stroke:#1f6feb,stroke-width:1.5px,color:#0b1f3a
    classDef prop  fill:#fff7ed,stroke:#b45309,stroke-width:1.2px,color:#3a2a0b
    classDef pub   fill:#ecfdf5,stroke:#047857,stroke-width:1.2px,color:#053826

    class R,M,PM,E,SG canon
    class SD,SL,SP,C,S,P,T,F,D,REL prop
    class API,UI pub
```

> [!NOTE]
> The diagram is **doctrinal**, not architectural — implementation status of every node in the `Implementation` and `Public` clusters is **PROPOSED** until verified against a mounted repository.

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 9. Ubiquitous language

The terms below are the domain's stable vocabulary (Atlas v1.1 Ch. 16 §C). They are **CONFIRMED terms** with **PROPOSED field realization** — the meaning is doctrine; the exact schema fields await mounted-repo verification.

| Term                     | Meaning                                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| **Person Assertion**     | A single, source-attributed claim about a person. Identity is built **from** assertions, not asserted directly.                  |
| **PersonCanonical**      | A derived, evidence-bound canonical view of a person; never sovereign — always a projection over assertions.                     |
| **NameAssertion**        | A source-attributed claim about a person's name(s), with time validity and confidence.                                           |
| **LifeEvent**            | A typed event (birth, baptism, marriage, death, burial, immigration, etc.) bound to evidence and time.                           |
| **RelationshipAssertion** | A claim of kinship or other relationship between persons, with evidence, time validity, and confidence.                         |
| **DNA Match Evidence**   | Evidence of genetic relationship from DTC vendor or research source; **restricted by default** (T4).                            |
| **DNAKitToken**          | An opaque, non-correlatable handle for a DNA kit; raw vendor kit IDs are not logged.                                            |
| **ConsentGrant**         | A scoped, revocable authorization (e.g., GA4GH Passport, OAuth2 grant) under which restricted material may be processed.        |
| **RevocationReceipt**    | A signed record that a `ConsentGrant` has been withdrawn; triggers tombstoning and downstream cleanup.                          |
| **LandParcel**           | A parcel record from cadastral or assessor sources. **Not** authoritative for title.                                            |
| **LegalDescription**     | A textual or surveyed description (metes & bounds, PLSS, lot/block) of a parcel boundary.                                       |
| **LandInstrument**       | A legal instrument transferring or encumbering land (patent, deed, mortgage, lien, easement, lease, mineral/water/access).      |
| **Ownership Interval**   | A time-bounded interval of asserted ownership, supported by one or more `LandInstrument`s and an `EvidenceBundle`.              |
| **Chain-of-Title**       | An ordered sequence of `Ownership Interval`s with gap and overlap controls; **gaps are surfaced, not silently filled**.         |
| **Relationship Hypothesis** | A *hypothesis* derived from DNA, GEDCOM, or other evidence — explicitly not a fact. Never promoted as public truth.          |

*Doctrine source: Atlas v1.1 Ch. 16 §C; Pass-10 C9; `[DOM-PEOPLE]`, `[ENCY]`.*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 10. Object families

Per Atlas v1.1 Ch. 16 §B/§E, this domain **owns** the following object families. All carry the **CONFIRMED ownership / PROPOSED field realization** posture, and all share KFM's standard temporal model — source, observed, valid, retrieval, release, and correction times stay distinct where material *(CONFIRMED)*.

| Object family             | Default sensitivity tier *(PROPOSED, per Atlas Ch. 24.5)* | Notes                                                                              |
| ------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Person Assertion          | T0–T4 (varies; living → T4)                               | Identity built **from** assertions; never sovereign.                               |
| Person Identity Candidate | T2 (reviewer)                                             | Pre-canonical, awaiting review.                                                    |
| PersonCanonical           | T0–T4 (varies; living → T4)                               | Derived, evidence-bound; not a separate truth source.                              |
| NameAssertion             | T0–T4 (varies)                                            | Source-attributed name claim.                                                      |
| LifeEvent                 | T0–T4 (varies; living → T4)                               | Typed event with evidence and time.                                                |
| Residence Event           | T0–T4 (varies)                                            | Anchors person ↔ settlement membership.                                            |
| Migration Event           | T0–T4 (varies)                                            | Anchors person ↔ corridor / route relations to Roads/Rail.                         |
| Genealogy Relationship    | T0–T4 (varies; living → T4)                               | Kinship link; restricted when any endpoint is living.                              |
| FamilyGroup               | T0–T4 (varies)                                            | Cluster of related persons.                                                        |
| Land Ownership Assertion  | T1–T2                                                     | An ownership claim bound to a `LandInstrument` and time interval.                  |
| Deed Instrument           | T0–T1                                                     | Public record; geometry derivations are not boundary truth.                        |
| Title Instrument          | T1–T2                                                     | Title is not assessor data; assessor-as-title is denied.                           |
| Assessor Record           | T1                                                        | Cadastral / valuation snapshot — **not title**.                                    |
| TaxRecord                 | T1                                                        | Tax roll snapshot — **not title**.                                                 |
| Parcel Version            | T1                                                        | A versioned parcel geometry; not boundary proof without `LandInstrument` support.  |
| Ownership Interval        | T1–T2                                                     | Time interval of asserted ownership.                                               |
| DNA Match Evidence        | **T4** (denied by default)                                | Released only as aggregate / k-anonymized derivative; raw never republished.       |
| DNASegment                | **T4** (denied by default)                                | Raw segment data; no transform releases this to a public tier.                    |
| Relationship Hypothesis   | T2–T4 (varies; living → T4)                               | Always a hypothesis; never promoted as public truth.                              |

> [!NOTE]
> Per-object default tiers above are **INFERRED** from the Atlas Ch. 24.5.2 People rows, which enumerate explicit tiers for *living-person fields*, *raw DNA segment data*, and *private person-parcel joins* (all T4). The Atlas does not assign a separate tier to every object family individually; the ranges shown apply the living-flag / aggregation logic to each family and are PROPOSED.

*Doctrine source: Atlas v1.1 Ch. 16 §B, §E; Ch. 24.5.2 (per-domain tier matrix).*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 11. Inputs — key source families

| Source family                                                                                  | Role *(per source)*                                  | Rights / sensitivity                                                                | Currentness               |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------- |
| Vital, cemetery, burial, obituary, church, school, military, census, directory, court, probate records | authority / observation / context / model           | rights and current terms **NEEDS VERIFICATION** per source; sensitive joins fail closed | source-vintage / cadence-specific |
| GEDCOM 5.5, GEDCOM-X, GEDZip, family-tree overlays (FamilySearch et al.)                       | authority / observation / context / model           | rights and current terms **NEEDS VERIFICATION** per source; sensitive joins fail closed | source-vintage / cadence-specific |
| DNA vendor match CSV / segment / triangulation data (DTC: 23andMe, AncestryDNA, MyHeritage)    | observation / model (never authority)               | **T4 default**; consent-bound; raw never republished                                | snapshot at export time   |
| Patent, deed, mortgage, lien, easement, lease, mineral, water, access, probate instruments     | authority / observation / context                   | typically T0–T1; **rights NEEDS VERIFICATION** per recorder office                  | recording-cadence-specific |
| Assessor and tax-roll records                                                                  | observation / context (**never title authority**)   | T1; assessor-as-title is **denied** by policy                                      | annual / cyclical         |
| Plat, survey, metes & bounds, PLSS, subdivision, derived geometry                              | authority / observation / context                   | T1; geometry is **not** title-boundary proof without `LandInstrument` support      | survey-vintage-specific   |

> [!IMPORTANT]
> The 23andMe Chapter 11 filing (March 2025) is treated by the corpus as a trigger event that hardened consent and revocation requirements. The DTC vendor-loss simulation playbook is a Pass-10 C9 follow-up. *(CONFIRMED, Pass-10 C9-03 / C9-07.)*

> [!NOTE]
> The Atlas Ch. 16 §D source-role column reads "authority / observation / context / model as source role requires." The seven canonical source roles are `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic` — note that **assessor/tax records are `administrative`** and **GEDCOM/tree imports are `modeled`/`candidate`** under that enum. The role labels in this table reflect the Atlas §D wording; reconciliation with the seven-role enum is **DEFERRED — pending ADR-S-04**.

*Doctrine source: Atlas v1.1 Ch. 16 §D; Pass-10 C9.*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 12. Outputs and viewing products

*(PROPOSED viewing products; doctrine source: Atlas v1.1 Ch. 16 §G.)*

- Historical person profile maps (deceased only, evidence-bound).
- Residence / event timelines, time-aware.
- Migration paths with explicit uncertainty.
- Land parcel context with **"not title"** warning banners.
- Chain-of-title summaries with gap / overlap markers.
- Instrument timeline views.
- Restricted DNA / consent review surfaces (steward-only).
- Living-person review surfaces (reviewer-only; never public).

All viewing products inherit the cross-cutting UI doctrine *(CONFIRMED)*:

- **Evidence Drawer** with EvidenceBundle projection.
- Time-aware state and trust badges.
- Sensitivity-redacted view.
- Correction / stale-state view.
- Governed **Focus Mode** — AI never the root truth source; `AIReceipt` always recorded.

*Doctrine source: `[MAP-MASTER]`, `[GAI]`, `[UIAI]`.*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 13. Pipeline shape (RAW → PUBLISHED)

*(CONFIRMED doctrine / PROPOSED lane application.)* This domain follows KFM's lifecycle invariant — **promotion is a governed state transition, not a file move** *(Directory Rules §2.1)*.

```mermaid
flowchart LR
    RAW["RAW: immutable source capture (SourceDescriptor required)"]
    WQ["WORK / QUARANTINE: normalize schema, geometry, time, identity, evidence, rights, policy"]
    PROC["PROCESSED: validated normalized objects + receipts + public-safe candidates"]
    CAT["CATALOG / TRIPLET: EvidenceBundles + graph projections + release candidates"]
    PUB["PUBLISHED: public-safe artifacts via governed API + ReleaseManifest"]
    QUAR["QUARANTINE: holds failures with reason code"]

    RAW --> WQ
    WQ -->|"gate pass"| PROC
    WQ -->|"gate fail"| QUAR
    PROC --> CAT
    CAT --> PUB
    PUB -. "correction / rollback" .-> CAT
    QUAR -. "resolved" .-> WQ

    classDef phase fill:#eef2ff,stroke:#3730a3,stroke-width:1.2px,color:#1e1b4b
    classDef quar  fill:#fee2e2,stroke:#b91c1c,stroke-width:1.2px,color:#450a0a
    classDef pub   fill:#dcfce7,stroke:#047857,stroke-width:1.2px,color:#052e1f

    class RAW,WQ,PROC,CAT phase
    class QUAR quar
    class PUB pub
```

| Stage             | Required gate (PROPOSED implementation)                                                                                                | Status   |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| RAW               | `SourceDescriptor` exists with source role, rights, sensitivity, citation, time, and hash.                                              | PROPOSED |
| WORK / QUARANTINE | Validation and policy gate pass, **or** quarantine reason code recorded.                                                                | PROPOSED |
| PROCESSED         | `EvidenceRef`, `ValidationReport`, and digest closure exist; public-safe candidates emitted.                                            | PROPOSED |
| CATALOG / TRIPLET | Catalog and proof closure pass; `EvidenceBundle` and graph/triplet projections emitted.                                                 | PROPOSED |
| PUBLISHED         | `ReleaseManifest` issued; correction path active; rollback target named; review/policy state recorded.                                  | PROPOSED |

*Doctrine source: Atlas v1.1 Ch. 16 §H; Directory Rules §2.1 (lifecycle invariant); Atlas Ch. 24.6 (pipeline gate reference).*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 14. Sensitivity, rights, and publication posture

> [!CAUTION]
> **Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion.** *(CONFIRMED doctrine, `[ENCY]`, `[DIRRULES]`.)*

### 14.1 Tier defaults for this domain *(reproduced verbatim from Atlas Ch. 24.5.2 People rows)*

| Domain / object class                  | Default tier  | Allowed transforms (PROPOSED)                                                  | Required gates                                       |
| -------------------------------------- | ------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------- |
| People/DNA — **living-person fields**  | **T4** (denied) | Aggregation by tract or county + `AggregationReceipt` → T1                   | Consent or aggregation gate + `ReviewRecord`         |
| People/DNA — **raw DNA segment data**  | **T4** (denied) | **No transform releases this to a public tier**; T3 only under named research agreement | Named consent + `ReviewRecord` + `PolicyDecision`    |
| People/Land — **private person-parcel join** | **T4** (denied) | Generalized parcel + de-identified person → T2 only                       | `RedactionReceipt` + `ReviewRecord`                  |
| Deceased-person assertions             | T0–T1         | Standard generalization where applicable                                       | Standard release                                     |
| Land instruments (patent, deed, etc.)  | T0–T1         | Standard release; parcel-geometry not promoted as title boundary               | Standard release                                     |

### 14.2 Tier transitions

All T4 → T1/T2/T3 motions are **reversible**. Revocation of consent or agreement returns the object to T4 with a `CorrectionNotice`. Promotion to T1 (public) requires `RedactionReceipt` + `ReviewRecord`. Promotion to PUBLISHED at T0 requires `ReleaseManifest` + `ReviewRecord` + release-authority sign-off. *(CONFIRMED doctrine, Atlas Ch. 24.5.3.)*

### 14.3 Hard rules

- **Living-person and DNA-derived outputs are denied or restricted by default.** *(CONFIRMED, `[DOM-PEOPLE]` §I.)*
- **Raw kit/vendor IDs and DNA segments are not public.** *(CONFIRMED, Pass-10 C9-03.)*
- **Assessor and tax records are not title truth.** *(CONFIRMED — assessor-as-title denial is a named validator; see [§17 K6](#17-validation).)*
- **Parcel geometry is not title-boundary proof** without source role and evidence. *(CONFIRMED, `[DOM-PEOPLE]` §I.)*
- **Relationship Hypothesis** stays a hypothesis. Never promoted as fact. *(CONFIRMED, `[DOM-PEOPLE]` §B; genealogy/genomic uploads treated as consent-bound user assets, Pass-10 C9 / KFM-P15-PROG-0034 PROPOSED.)*
- **Consent is revocable.** Revocation triggers tombstones (`RevocationReceipt`), downstream cleanup, and embargo-cache invalidation. *(CONFIRMED, Pass-10 C5-09 / C6-08; C9-02.)*
- **AI never reads RAW or WORK content.** AI surfaces consume only released `EvidenceBundle`s. *(CONFIRMED, `[GAI]`; Atlas Ch. 24.5.2 Governed-AI row.)*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 15. Cross-lane relations

*(Atlas v1.1 Ch. 16 §F. All relations preserve ownership, source role, sensitivity, and EvidenceBundle support.)*

> [!NOTE]
> Atlas Ch. 16 §F names four cross-lane relations as CONFIRMED/PROPOSED: **Settlements, Roads/Rail, Archaeology, Agriculture.** The Frontier Matrix and Planetary/3D rows below are **INFERRED** from the wider Atlas (Ch. 17 §B; Ch. 24.14 object × domain matrix) — they are reasonable but are not in the §F per-domain table.

| Related lane | Relation type                                                  | Constraint                                                              | Basis |
| ------------ | -------------------------------------------------------------- | ----------------------------------------------------------------------- | ----- |
| **Settlements**                     | residence, cemetery, school, court, county, township, place    | Living-person fields fail closed.                                       | §F CONFIRMED |
| **Roads/Rail**                      | migration, access, movement                                    | Migration paths carry uncertainty; living persons fail closed.          | §F CONFIRMED |
| **Archaeology / Cultural Heritage** | historic person, land, documentary, cultural-place context     | Cultural affiliations cited with rights, sovereignty, and steward review. | §F CONFIRMED |
| **Agriculture**                     | farm, land-use, producer-adjacent context with privacy         | Private person-parcel joins denied by default.                          | §F CONFIRMED |
| **Frontier Matrix**                 | aggregated population observations feed matrix cells           | Matrix cells are analytical releases with their own evidence and rollback. | INFERRED (Ch. 17 §B) |
| **Planetary / 3D**                  | scenes may cite released domain artifacts under admission rules | Scenes are never an instruction or alert surface.                       | INFERRED (Ch. 24.14) |

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 16. API, contract, and schema surfaces

*(All entries PROPOSED; doctrine source: Atlas v1.1 Ch. 16 §J. Exact routes are UNKNOWN. Segment marked `<segment>` is subject to the [§2.1 conflict](#21-segment-naming-conflict).)*

| Endpoint or artifact                          | DTO / schema                                              | Outcomes                            | Status                                                |
| --------------------------------------------- | --------------------------------------------------------- | ----------------------------------- | ----------------------------------------------------- |
| People/DNA/Land feature/detail resolver       | `PeopleDNALandDecisionEnvelope`                           | ANSWER / ABSTAIN / DENY / ERROR     | **PROPOSED**; exact route UNKNOWN                     |
| People/DNA/Land layer-manifest resolver       | `LayerManifest` / domain layer descriptor                 | ANSWER / DENY / ERROR               | **PROPOSED**; public-safe release only                |
| People/DNA/Land Evidence Drawer payload       | `EvidenceDrawerPayload` + `EvidenceBundle` projection     | ANSWER / ABSTAIN / DENY / ERROR     | **PROPOSED**; evidence- and policy-filtered           |
| People/DNA/Land Focus Mode answer             | `Runtime Response Envelope` + `AIReceipt`                 | ANSWER / ABSTAIN / DENY / ERROR     | **PROPOSED**; AI is never root truth                  |
| Schema responsibility root                    | `schemas/contracts/v1/<segment>/`                          | finite validator outcomes           | **PROPOSED**; verify with Directory Rules and ADR-0001 |

> [!NOTE]
> The four outcomes — ANSWER / ABSTAIN / DENY / ERROR — are the **finite Outcome enum** used across all KFM decision envelopes *(CONFIRMED doctrine, Atlas Ch. 24.3)*. There is no `ACCEPTED` outcome; a passed promotion is an `ANSWER` queued per §24.3.1. Any new endpoint in this domain must return one of these four; intermediate or fuzzy outcomes are an anti-pattern.

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 17. Validation

*(All PROPOSED; doctrine source: Atlas v1.1 Ch. 16 §K. K-numbering below is a local ordering aid, not an Atlas-assigned index.)*

| K# | Validator (PROPOSED)                          | What it proves                                                                         |
| -- | --------------------------------------------- | -------------------------------------------------------------------------------------- |
| K1 | Person assertion evidence tests               | Every `Person Assertion` resolves to an `EvidenceBundle`; orphan assertions fail.      |
| K2 | GEDCOM import rights / living-flag tests      | GEDCOM imports cannot bypass living-person screening or rights checks.                 |
| K3 | DNA consent and raw-ID no-log tests           | Raw vendor kit IDs never appear in logs; consent scope is recorded per record.         |
| K4 | Revocation cleanup tests                      | `RevocationReceipt` triggers tombstoning, downstream cleanup, embargo invalidation.    |
| K5 | Legal-description and chain-of-title gap tests | Gaps and overlaps in `Ownership Interval` chains are surfaced, not silently filled.    |
| K6 | Assessor-as-title denial                      | Assessor or tax records cannot be promoted as title authority.                         |
| K7 | Graph projection safety tests                 | Triplet / graph projections do not leak sensitive joins or living-person fields.       |

> [!TIP]
> All validators in this lane should additionally exercise **negative-state cases** — DENY, ABSTAIN, and ERROR paths. A validator that only proves the happy path leaves the trust membrane unproven.

*Test home: `tests/domains/people-dna-land/` (PROPOSED). Fixture home: `fixtures/domains/people-dna-land/` (PROPOSED).*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 18. Review burden and separation of duties

*(Atlas v1.1 Ch. 24.7. CONFIRMED doctrine; named-individual assignments NEEDS VERIFICATION.)*

| Role                         | Duty in this domain                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Source steward**           | Admission and rights confirmation for vital, GEDCOM, DTC, instrument, assessor, and survey source families.    |
| **Domain steward**           | Owns contracts and validators for `Person Assertion`, `LandInstrument`, `Ownership Interval`, etc.             |
| **Sensitivity reviewer**     | Reviews redaction, generalization, withholding, and tier transitions for living-person and DNA content.       |
| **Rights-holder representative** | Confirms living-person, DNA, and culturally sensitive release decisions; required for any T4 → T3 motion. |
| **Release authority**        | Issues `ReleaseManifest`s and authorizes PUBLISHED transitions; **distinct from authorship** when materiality applies. |
| **Correction reviewer**      | Reviews `CorrectionNotice` / `RollbackCard` before they amend a PUBLISHED claim.                              |
| **AI surface steward**       | Reviews Focus Mode templates, `AIReceipt`s, and policy bindings for this domain.                              |
| **Docs steward**             | Owns this README, the ADR index, the drift register, and Atlas/supplement integrity for the lane.             |

> [!IMPORTANT]
> **Sensitive-lane release requires four roles, not two.** Per Atlas Ch. 24.7.2, a sensitive-lane release (living persons, DNA, private person-parcel joins) requires **author + sensitivity reviewer + release authority + rights-holder rep**, and the author may not also approve. Separation of duties is **maturity-dependent** (Directory Rules §2): early low-materiality doctrine work may be authored and approved by the same actor; as the public trust surface expands, separation must be enforced through tooling. The threshold itself is an open ADR (ADR-S-09).

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 19. Governed AI behavior

*(CONFIRMED doctrine / PROPOSED implementation, Atlas v1.1 Ch. 16 §L.)*

AI may:

- Summarize **released** People/DNA/Land `EvidenceBundle`s.
- Compare evidence and explain limitations.
- Draft steward-review notes and proposed corrections.

AI **must**:

- **ABSTAIN** when evidence is insufficient.
- **DENY** where policy, rights, sensitivity, or release state blocks the request.
- Emit an `AIReceipt` on every answer.

AI **must not**:

- Read RAW or WORK content directly.
- Promote a `Relationship Hypothesis` as fact.
- Synthesize living-person details, DNA inferences, or private person-parcel joins.
- Replace `EvidenceBundle` as the truth source.

*Doctrine source: `[GAI]`; Atlas Ch. 16 §L; Ch. 24.5.2 (Governed AI — RAW/WORK access denied); Ch. 24.9.2 (trust-membrane anti-patterns).*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 20. Publication, correction, and rollback

*(CONFIRMED doctrine / PROPOSED implementation, Atlas v1.1 Ch. 16 §M.)*

Publication in this domain requires, at minimum:

1. `ReleaseManifest` issued.
2. `EvidenceBundle` resolvable.
3. Validation and policy support documented.
4. `ReviewRecord` where required (always required for living-person, DNA, and private person-parcel joins).
5. Correction path active.
6. Stale-state rule honored.
7. Rollback target named.

Corrections follow the `CorrectionNotice` flow; rollbacks follow `RollbackCard`. Both are reviewed by the correction reviewer before they amend a PUBLISHED claim.

*Detailed flow: see `docs/runbooks/people-dna-land/SOURCE_REFRESH_RUNBOOK.md` (PROPOSED, not yet authored). The pattern follows the fauna runbook (`docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`; CONFIRMED authored prior session per Directory Rules §6.1.b note; mounted-repo presence NEEDS VERIFICATION).*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 21. Open questions and verification backlog

| ID        | Item                                                                                              | Evidence that would settle it                                                            | Status              |
| --------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------- |
| **OQ-PDL-SEG-01** | Segment name: `people` (Atlas Ch. 24.13) vs `people-dna-land` (DIRRULES §6.1/§12)         | ADR — carried across the domain doc set (model, matrix, inventory)                       | **CONFLICTED — BLOCKING** |
| OQ-PDL-01 | Verify living-person policy enforcement                                                           | Mounted repo files, schemas, registry entries, tests, logs, review records, manifests    | NEEDS VERIFICATION  |
| OQ-PDL-02 | Verify DNA consent / revocation enforcement                                                       | Mounted repo files + consent-token verifier + revocation cleanup tests                   | NEEDS VERIFICATION  |
| OQ-PDL-03 | Verify land-instrument chain logic and gap/overlap surfacing                                      | Mounted repo files + chain-of-title gap tests + fixtures                                  | NEEDS VERIFICATION  |
| OQ-PDL-04 | Verify geometry-role boundary logic (parcel is not title)                                          | Mounted repo files + assessor-as-title denial tests                                       | NEEDS VERIFICATION  |
| OQ-PDL-05 | Verify UI / API restricted-field no-leak behavior                                                  | Mounted repo files + tile field-allowlist tests + Evidence Drawer negative-case tests    | NEEDS VERIFICATION  |
| OQ-PDL-06 | Resolve sublane folder convention (`sublanes/`) vs flat (`docs/domains/people-dna-land/<x>.md`)   | ADR — see [§22](#22-adrs); parallel to Directory Rules OPEN-DR-02                        | OPEN                |
| OQ-PDL-07 | Resolve runbook subfolder convention for this domain (parallel to fauna's `runbooks/fauna/`)       | ADR — Directory Rules OPEN-DR-02                                                          | OPEN                |
| OQ-PDL-09 | Codify DTC-vendor compatibility matrix and vendor-loss-simulation playbook                         | `docs/runbooks/people-dna-land/DTC_VENDOR_LOSS_DRILL.md` (PROPOSED)                       | OPEN                |
| OQ-PDL-10 | Specify retention boundary: tombstone vs erasure for revoked living-person and DNA data            | Joint ADR with `docs/doctrine/lifecycle-law.md`; align with GDPR and Tribal data policies | OPEN                |
| OQ-PDL-11 | Define non-conforming GEDCOM acceptance thresholds (fail vs accept-with-warning)                   | ADR + per-source policy fragment + conformance-reporter test corpus (Pass-10 C9-01)       | OPEN                |

> [!NOTE]
> v1 numbered an item OQ-PDL-08 ("folder-name canonicalization: `people-dna-land` vs alternate longer names"). That item is **superseded by OQ-PDL-SEG-01**, which states the conflict precisely (`people` vs `people-dna-land`); the old OQ-PDL-08 row is retired to avoid two trackers for one decision.

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 22. ADRs

| ADR ID                | Topic                                                                                            | Status      |
| --------------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| **OQ-PDL-SEG-01 → ADR (proposed)** | Segment name: `people` vs `people-dna-land` for `schemas/`/`contracts/`/`policy/sensitivity/` | **PROPOSED — BLOCKING** |
| ADR-D-01 *(PROPOSED, local)* | Sublane folder convention for `docs/domains/<domain>/` (subfolder vs flat) — covers OQ-PDL-06    | PROPOSED    |
| ADR-S-04 *(corpus backlog)* | Source-role vocabulary v1 — covers the §11 role-label reconciliation                            | PROPOSED    |
| ADR-S-05 *(corpus backlog)* | Sensitivity tier scheme (T0–T4) — governs §10 and §14                                           | PROPOSED    |
| ADR-S-09 *(corpus backlog)* | Reviewer separation-of-duties threshold (tooling vs custom) — governs §18                       | PROPOSED    |
| ADR-S-14 *(corpus backlog)* | Cross-lane join policy — governs §15 private person-parcel joins                                | PROPOSED    |
| ADR-0001 *(applies; this domain inherits)* | Schema home (`schemas/contracts/v1/<…>`)                                          | CONFIRMED (per Directory Rules §0) |

> [!NOTE]
> ADR home is `docs/adr/`. Local `ADR-D-*` IDs are placeholders pending the docs steward's allocation. `ADR-S-*` IDs reference the Atlas Ch. 24.12 Master Open-ADR Backlog and are cross-referenced here rather than re-invented. v1 listed local IDs `ADR-D-02/03/04` (retention, consent-revocation, chain-of-title); those topics are tracked via OQ-PDL-10/02/03 and the corpus ADR-S backlog, so the duplicate local IDs are dropped.

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 23. Related docs and folders

*(Some link targets are PROPOSED. Where a target is not yet authored, the link points to its proposed path so the broken-link surface tells the reviewer what's missing.)*

**Inside this folder**

- [`PEOPLE_DOMAIN_MODEL.md`](PEOPLE_DOMAIN_MODEL.md) — bounded context, identity, aggregates, invariants *(CONFIRMED authored)*
- [`PEOPLE_PRESERVATION_MATRIX.md`](PEOPLE_PRESERVATION_MATRIX.md) — retention, tombstone, erasure duties *(CONFIRMED authored)*
- [`MISSING_OR_PLANNED_FILES.md`](MISSING_OR_PLANNED_FILES.md) — file inventory; source of OQ-PDL-SEG-01 *(CONFIRMED authored)*
- [`EXPANSION_PLAN.md`](EXPANSION_PLAN.md) — roadmap and thin-slice ordering *(CONFIRMED authored)*
- [`sublanes/genealogy.md`](sublanes/genealogy.md) — kinship & life-event slice *(CONFIRMED authored)*
- `sublanes/dna.md` — DTC, GA4GH, consent, revocation *(PROPOSED)*
- `sublanes/land.md` — patents, deeds, instruments, ownership intervals, chain-of-title *(PROPOSED)*
- `sublanes/person-identity.md` — assertion-first identity, `PersonCanonical`, `RelationshipAssertion` *(PROPOSED)*

**Parent and siblings**

- [`../README.md`](../README.md) — `docs/domains/` landing *(PROPOSED authoring)*
- [`../archaeology/`](../archaeology/) — cultural-context partner; sovereignty-aware *(PROPOSED authoring)*
- [`../settlements-infrastructure/`](../settlements-infrastructure/) — residence anchor *(PROPOSED authoring)*
- [`../roads-rail-trade/`](../roads-rail-trade/) — migration corridor partner *(PROPOSED authoring)*
- [`../agriculture/`](../agriculture/) — farm and land-use context *(PROPOSED authoring)*

**Doctrine and standards**

- [`../../doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement law *(CONFIRMED authored)*
- `../../doctrine/authority-ladder.md` *(PROPOSED)*
- `../../doctrine/truth-posture.md` *(PROPOSED)*
- `../../doctrine/trust-membrane.md` *(PROPOSED)*
- `../../doctrine/lifecycle-law.md` *(PROPOSED)*
- [`../../standards/PROV.md`](../../standards/PROV.md) — provenance standard *(CONFIRMED authored, prior session; naming variance vs corpus `PROVENANCE.md` → Directory Rules OPEN-DR-01)*
- `../../standards/SENSITIVITY_RUBRIC.md` *(PROPOSED in corpus, Pass-10 C6-01; not yet authored)*
- `../../standards/REDACTION_DETERMINISM.md` *(PROPOSED in corpus, Pass-10 C6-03; not yet authored)*

**Implementation siblings (canonical roots)**

- `contracts/<segment>/` *(PROPOSED; segment CONFLICTED)*
- `schemas/contracts/v1/<segment>/` *(PROPOSED; segment CONFLICTED)*
- `policy/domains/people-dna-land/`, `policy/sensitivity/<segment>/`, `policy/consent/<segment>/` *(PROPOSED)*
- `tests/domains/people-dna-land/` *(PROPOSED)*
- `fixtures/domains/people-dna-land/` *(PROPOSED)*
- `data/<phase>/people-dna-land/` *(PROPOSED)*
- `release/candidates/people-dna-land/` *(PROPOSED)*

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## 24. Appendix — extended reference

<details>
<summary><strong>A.1 — Doctrine citations used in this README</strong></summary>

| Marker          | Source                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| `[DOM-PEOPLE]`  | Domain dossier: People, Genealogy, DNA, and Land Ownership (Atlas Ch. 16)                               |
| `[ENCY]`        | KFM Encyclopedia (domain/object/source/capability spine; §7.14 section number NEEDS VERIFICATION)       |
| `[DIRRULES]`    | `docs/doctrine/directory-rules.md` (v1.3)                                                               |
| `[GAI]`         | Whole-UI Governed AI Expansion Report                                                                   |
| `[MAP-MASTER]`  | Master MapLibre Components-Functions-Features report                                                    |
| `[UIAI]`        | Whole-UI / Governed-AI cross-cutting doctrine                                                           |
| `[UNIFIED]`     | KFM Unified Implementation Architecture Build Manual                                                    |
| `[DDD]`         | Domain-Driven Design Reference (Eric Evans, 2015) — background only; KFM doctrine governs              |
| Atlas v1.1      | KFM Domains Culmination Atlas v1.1, esp. Ch. 16 (this domain), Ch. 24.5 (tiers), Ch. 24.7 (SoD), Ch. 24.13 (crosswalk) |
| Pass-10         | KFM Components Pass-10 Idea Index — esp. C6 (Sensitivity), C9 (Genealogy/Genomics), C14 (Repo Hygiene)  |

</details>

<details>
<summary><strong>A.2 — Receipt and artifact types referenced</strong></summary>

| Type                  | Role                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------ |
| `SourceDescriptor`    | Admission record for a source family (rights, sensitivity, role, citation, time, hash).   |
| `EvidenceRef`         | Pointer to the evidence backing a claim.                                                  |
| `EvidenceBundle`      | Resolvable, governed projection of evidence supporting a published claim.                  |
| `ValidationReport`    | Output of a validator on a normalized object.                                              |
| `PolicyDecision`      | Allow / Deny / Restrict / Abstain outcome of a policy check (OPA-bound).                  |
| `ReviewRecord`        | Steward / sensitivity-reviewer / rights-holder sign-off (§24.2 cross-cutting receipt).     |
| `RedactionReceipt`    | Record of a redaction / generalization transform with deterministic profile reference.    |
| `AggregationReceipt`  | Record of an aggregation transform that reaches k-anonymity for living persons.            |
| `ConsentGrant`        | Scoped, revocable authorization (GA4GH Passport, OAuth2, etc.).                            |
| `RevocationReceipt`   | Withdrawal of a `ConsentGrant`; triggers tombstoning and downstream cleanup.              |
| `ReleaseManifest`     | Signed release decision tying an artifact to its evidence, policy, and rollback target.   |
| `CorrectionNotice`    | Post-publication correction record.                                                       |
| `RollbackCard`        | Rollback decision and procedure binding to a prior published state.                        |
| `AIReceipt`           | Per-answer AI surface receipt with policy binding and EvidenceBundle reference.            |
| `RunReceipt`          | Per-pipeline-run receipt (dataset_id, fetch_time, source_url, response checksum, scope).  |

</details>

<details>
<summary><strong>A.3 — How a deceased-person assertion reaches PUBLISHED (illustrative)</strong></summary>

*(Illustrative — not a sourced exemplar. Marked PROPOSED.)*

1. **RAW** — A 1900 U.S. Census line item is captured by a source-specific connector with `SourceDescriptor` (rights: public domain; role: observation; time: enumeration date).
2. **WORK** — The line is normalized into one or more `Person Assertion`, `NameAssertion`, and `LifeEvent` objects. Place strings are anchored to GNIS; date intervals are normalized to ISO 8601.
3. **WORK/QUARANTINE** — Identity disambiguation runs; ambiguous candidates land in QUARANTINE for steward review.
4. **PROCESSED** — A validated, normalized assertion set emits with `EvidenceRef` and `ValidationReport`; digest closure passes.
5. **CATALOG / TRIPLET** — An `EvidenceBundle` is bundled with a CIDOC-CRM graph projection; a release candidate is staged.
6. **PUBLISHED** — `ReleaseManifest` is issued. The assertion becomes a layer feature in the public client, visible in the Evidence Drawer with trust badges. Correction path and rollback target are named.

At every stage, AI surfaces consume only the **released** `EvidenceBundle`. A living-person variant of this flow would terminate at WORK/QUARANTINE for review-only access, not at PUBLISHED.

</details>

<details>
<summary><strong>A.4 — Anti-patterns to watch for</strong></summary>

Aligned with Atlas Ch. 24.9.2 (trust-membrane anti-patterns) and Ch. 24.9.3 (governance-process anti-patterns).

- **Assessor-as-title.** Treating an assessor or tax (`administrative`) record as a title authority. **Denied.**
- **Parcel-as-boundary-proof.** Promoting parcel geometry as boundary truth without `LandInstrument` support. **Denied.**
- **Hypothesis-as-fact.** Publishing a `Relationship Hypothesis` (DNA, GEDCOM, or otherwise) as confirmed kinship. **Denied.**
- **Aggregation that doesn't reach k-anonymity.** Living-person aggregations below the k-threshold are not public-safe. **Denied.** [Pass-10 C6-06]
- **AI-as-truth.** Allowing a Focus Mode answer to displace the `EvidenceBundle`. **Denied.** [Atlas Ch. 24.9.2]
- **Source-role upcast.** Promoting a `modeled`/`administrative` record to `observed`/title on promotion. Role is fixed at admission. **Denied.** [Atlas Ch. 24.9.3]
- **Tombstone instead of erasure where erasure is required.** Right-to-be-forgotten obligations may require true deletion, not just tombstoning. *(See OQ-PDL-10; Pass-10 C5-09.)*
- **Standards-name drift.** Cross-references to `PROVENANCE.md` while the authored file is `PROV.md`. *(See Directory Rules OPEN-DR-01.)*

</details>

<details>
<summary><strong>A.5 — External standards this domain conforms to (where applicable)</strong></summary>

*Conformance is asserted by the corpus; mounted-repo verification of any specific binding remains NEEDS VERIFICATION.*

- **W3C PROV-O / PAV** — provenance for assertions and bundles. *(Pass-10 C8-03.)*
- **CIDOC-CRM E21 / E13** — person and assertion modeling for graph projections. *(Pass-10 C8-01.)*
- **GEDCOM 5.5 and GEDCOM-X** — genealogical interchange formats. *(Pass-10 C9-01.)*
- **GA4GH AAI, Passports, DUO, Machine-Readable Consent Guidance** — consent and access control. *(Pass-10 C9-04.)*
- **NIST SP 800-226** — differential privacy guidance for aggregates. *(Pass-10 C6-05 / C9-05.)*
- **EDPB Guidelines 01/2025** — pseudonymisation. *(Pass-10 C9-05.)*
- **ISO 19115** — geospatial metadata for parcel and instrument records *(asserted; NEEDS VERIFICATION)*.
- **FAIR + CARE** principles — overall posture.

</details>

[↑ back to top](#people-genealogy-dna-and-land-ownership)

---

## Truth labels used here

| Label                | Meaning                                                                                              |
| -------------------- | ---------------------------------------------------------------------------------------------------- |
| **CONFIRMED**        | Verified this session from attached doctrine corpus and prior-session-authored artifacts.            |
| **PROPOSED**         | Design, path, placement, or recommendation not yet verified against a mounted repository.            |
| **NEEDS VERIFICATION** | Checkable, but not yet checked strongly enough to act as fact.                                     |
| **UNKNOWN**          | Not resolvable without more evidence than this session affords.                                       |
| **INFERRED**         | Reasonably derivable from visible evidence but not directly stated.                                  |
| **CONFLICTED**       | Two CONFIRMED sources disagree (e.g., OQ-PDL-SEG-01); surfaced and tracked, not silently resolved.    |
| **EXTERNAL**         | Sourced from authoritative external research; never used for KFM-specific repo or doctrine claims.   |

> [!NOTE]
> No mounted repo, CI workflow, dashboard, or runtime log was inspected during authoring. Every path under `contracts/`, `schemas/`, `policy/`, `tests/`, `fixtures/`, `data/`, `release/`, `apps/`, and `runtime/` named here is **PROPOSED** until mounted-repo verification. Doctrine claims grounded in Atlas v1.1, Encyclopedia, Directory Rules, Pass-10, Unified Manual, MapLibre-Master, and Governed-AI sources are **CONFIRMED**.

---

**Related docs:** [`PEOPLE_DOMAIN_MODEL.md`](PEOPLE_DOMAIN_MODEL.md) · [`PEOPLE_PRESERVATION_MATRIX.md`](PEOPLE_PRESERVATION_MATRIX.md) · [`EXPANSION_PLAN.md`](EXPANSION_PLAN.md) · [`sublanes/genealogy.md`](sublanes/genealogy.md) · [`../../doctrine/directory-rules.md`](../../doctrine/directory-rules.md) · [`../../standards/PROV.md`](../../standards/PROV.md)

**Last updated:** 2026-06-07 · **Edition:** v1.1 · **CONTRACT_VERSION:** 3.0.0

[↑ back to top](#people-genealogy-dna-and-land-ownership)
