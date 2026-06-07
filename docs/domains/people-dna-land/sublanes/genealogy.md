<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/people-dna-land/sublanes/genealogy
title: Genealogy Sublane — People / Genealogy / DNA / Land Ownership
type: standard
version: v1
status: draft
owners: <People-DNA-Land domain steward — TODO>, <source steward — TODO>, <sensitivity reviewer — TODO>
created: 2026-05-18
updated: 2026-06-06
policy_label: restricted
related:
  # NEEDS VERIFICATION — every path below is PROPOSED until checked against a mounted repo
  - docs/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/sublanes/README.md
  - docs/domains/people-dna-land/sublanes/people/README.md
  - docs/domains/people-dna-land/sublanes/dna/README.md
  - docs/domains/people-dna-land/sublanes/land/README.md
  - directory-rules.md
  - ai-build-operating-contract.md
  - docs/standards/PROV.md
  - docs/standards/ISO-19115.md
tags: [kfm, genealogy, people-dna-land, sublane, governance, FAIR-CARE]
notes:
  # CONTRACT_VERSION = "3.0.0"
  # sublanes/ folder convention is PROPOSED; not in Directory Rules §12; needs ADR (OQ-PEOPLE-SUB-01).
  # CONFLICTED: a standalone "genealogy" sublane vs folding genealogy into the "people" sublane is UNRESOLVED.
  #   The prior sublanes index proposed a 3-way split (people/dna/land); this doc proposes a 4-way split. Same ADR (OQ-PEOPLE-SUB-02).
  # All implementation paths are PROPOSED until verified against mounted repo evidence.
[/KFM_META_BLOCK_V2] -->

# 🌳 Genealogy Sublane — People / Genealogy / DNA / Land Ownership

> **Assertion-first, evidence-bound, privacy-aware genealogical claims** — the sublane that turns GEDCOMs, vital records, and family trees into governed, public-safe history without becoming unsourced folklore.

[![Status: Draft](https://img.shields.io/badge/status-draft-yellow)](#status)
[![Domain: People-DNA-Land](https://img.shields.io/badge/domain-people--dna--land-7e3ff2)](../README.md)
[![Sensitivity: Default-Deny on Living + DNA](https://img.shields.io/badge/sensitivity-default--deny%20living%20%2B%20DNA-d73a49)](#10-policy-and-sensitivity-posture)
[![Pipeline: RAW → PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-blue)](#9-pipeline-shape-raw--published)
[![sublanes/: PROPOSED](https://img.shields.io/badge/sublanes%2F-PROPOSED-yellow)](#2-repo-fit)
[![CONTRACT_VERSION 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)](#)
[![FAIR + CARE](https://img.shields.io/badge/principles-FAIR%20%2B%20CARE-2ea44f)](#15-fair--care-posture)

| Field            | Value                                                          |
| ---------------- | -------------------------------------------------------------- |
| **Status**       | Draft                                                          |
| **Owners**       | People-DNA-Land domain stewards · *TODO / NEEDS VERIFICATION*  |
| **Last updated** | 2026-06-06                                                     |
| **Contract**     | `CONTRACT_VERSION = "3.0.0"`                                   |
| **Parent**       | [`docs/domains/people-dna-land/README.md`](../README.md)       |
| **Sibling sublanes** | [`people/README.md`](../people/README.md) · [`dna/README.md`](../dna/README.md) · [`land/README.md`](../land/README.md) — *paths PROPOSED* |

> [!IMPORTANT]
> **CONFLICTED — does this sublane exist on its own?** The domain is titled "People,
> **Genealogy**, DNA, and Land Ownership," so a genealogy sublane is defensible. But the
> domain's *object families* (Person Assertion, Genealogy Relationship, FamilyGroup,
> LifeEvent, …) are owned by a **single** `[DOM-PEOPLE]` bounded context with **no**
> sub-partition in doctrine, and a prior `sublanes/README.md` proposed a **three-way**
> split (`people` / `dna` / `land`) that folds genealogy into `people`. This doc proposes a
> **four-way** split. The sublane *count and names* are an open ADR question
> (**OQ-PEOPLE-SUB-02**), tracked alongside the `sublanes/` convention itself
> (**OQ-PEOPLE-SUB-01**). This doc is authored as requested; the conflict is surfaced, not
> resolved. [DOM-PEOPLE §A/§B; DIRRULES §12]

---

## Quick jump

- [1. Scope and one-line purpose](#1-scope-and-one-line-purpose)
- [2. Repo fit](#2-repo-fit)
- [3. Inputs the sublane accepts](#3-inputs-the-sublane-accepts)
- [4. Exclusions and explicit non-ownership](#4-exclusions-and-explicit-non-ownership)
- [5. Sublane architecture (diagram)](#5-sublane-architecture-diagram)
- [6. Ubiquitous language](#6-ubiquitous-language)
- [7. Object families owned here](#7-object-families-owned-here)
- [8. Source families and source roles](#8-source-families-and-source-roles)
- [9. Pipeline shape (RAW → PUBLISHED)](#9-pipeline-shape-raw--published)
- [10. Policy and sensitivity posture](#10-policy-and-sensitivity-posture)
- [11. Publication: overlay pointers, not PII](#11-publication-overlay-pointers-not-pii)
- [12. Cross-lane and cross-sublane handoffs](#12-cross-lane-and-cross-sublane-handoffs)
- [13. Governed AI behavior in this sublane](#13-governed-ai-behavior-in-this-sublane)
- [14. Validators, fixtures, and CI gates](#14-validators-fixtures-and-ci-gates)
- [15. FAIR + CARE posture](#15-fair--care-posture)
- [16. Open questions and verification backlog](#16-open-questions-and-verification-backlog)
- [17. Related docs](#17-related-docs)
- [Truth labels used here](#truth-labels-used-here)

---

## 1. Scope and one-line purpose

**One-line purpose.** The Genealogy sublane governs assertion-first lineage evidence — GEDCOMs, family trees, vital records, and relationship hypotheses — under KFM's evidence-bound, privacy-aware, default-deny doctrine for living persons. *(CONFIRMED doctrine / PROPOSED implementation. [DOM-PEOPLE §A])*

The Genealogy sublane is the **kinship and life-event slice** of the broader People / Genealogy / DNA / Land Ownership domain. It is the place where unsourced family-tree folklore meets KFM's trust membrane: every relationship is an assertion with evidence and confidence, never a sovereign fact; every published view is a derivative of governed claims, never the canonical store.

> [!IMPORTANT]
> Genealogy outputs that involve **living persons** or **DNA-derived inference** are denied or restricted by default. Historical research is supported where evidence, rights, and release controls allow it; living-person and DNA-derived outputs require explicit, scoped, revocable consent. [DOM-PEOPLE §I; ENCY]

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 2. Repo fit

| Aspect            | Value                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------- |
| **This path**     | `docs/domains/people-dna-land/sublanes/genealogy/README.md` — *PROPOSED (see [OQ-PEOPLE-SUB-01](#16-open-questions-and-verification-backlog))* |
| **Authority root**| `docs/` — human-facing control plane (Directory Rules §3) — *CONFIRMED*                     |
| **Domain slug**   | `people-dna-land` — *CONFIRMED, named explicitly in Directory Rules §12*                    |
| **Parent README** | [`../README.md`](../README.md) — the People / Genealogy / DNA / Land Ownership landing doc |
| **Upstream doctrine** | Atlas v1.1 Ch. 16; ENCY; Directory Rules §12 (Domain Placement Law)                     |
| **Downstream artifacts** | Whole-domain lanes per §12 — `contracts/domains/people-dna-land/…` · `schemas/contracts/v1/domains/people-dna-land/…` · `policy/domains/people-dna-land/…` · `tests/domains/people-dna-land/…` · `fixtures/domains/people-dna-land/…` — *all PROPOSED; not subdivided by sublane* |

> [!NOTE]
> **Two layered PROPOSED questions.** (1) Directory Rules §12 confirms `docs/domains/people-dna-land/`
> as the domain home and `people-dna-land` as the slug — *CONFIRMED.* (2) The `sublanes/`
> subfolder is **not** in §12; it is the same class of open question as the runbook-subfolder
> one (§18 OPEN-DR-02) and needs an ADR before it is canonical — *PROPOSED, OQ-PEOPLE-SUB-01.*
> Per §12, responsibility-root artifacts (schemas, policy, tests, data) live in **whole-domain**
> lanes and do **not** subdivide by sublane; `sublanes/` is a documentation-only layer that
> adds no authority home. [DIRRULES §3, §12]

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 3. Inputs the sublane accepts

| Input family                                                                  | Source role                                  | Status        | Citation              |
| ----------------------------------------------------------------------------- | -------------------------------------------- | ------------- | --------------------- |
| GEDCOM 5.5 and GEDCOM-X files (uploaded `.ged`/`.gedz`/JSON-XML)              | authority / observed                         | CONFIRMED     | [DOM-PEOPLE] [ENCY] [Pass-10 C9-01] |
| FamilySearch API responses (OAuth2-scoped)                                    | observed                                     | CONFIRMED     | [Pass-10 C9-02]       |
| Vital records (birth, marriage, death) where public/legal                     | authority / observed                         | CONFIRMED     | [DOM-PEOPLE] [ENCY]   |
| Cemetery, burial, obituary, church, school, military, census, directory, court, probate records | authority / observed / context | CONFIRMED | [DOM-PEOPLE] [ENCY] |
| Tree overlays from genealogy clients and crowd platforms                      | observed / modeled (hypothesis)              | CONFIRMED     | [DOM-PEOPLE] [ENCY]   |
| Consent receipts (machine-readable, signed)                                   | governance artifact                          | PROPOSED      | [Pass-10 C6-07]       |

> [!NOTE]
> Source-role labels use the canonical seven-role vocabulary (`observed`, `regulatory`,
> `modeled`, `aggregate`, `administrative`, `candidate`, `synthetic`) from the Atlas §24.1
> anti-collapse register, rather than ad-hoc synonyms. A tree-overlay hypothesis is `modeled`
> (or `candidate` until reviewed), never `observed`. [Atlas §24.1; ADR-S-04 pending]

> [!CAUTION]
> **GEDCOM is treated as RAW only.** Never publish GEDCOM directly, never map GEDCOM identifiers directly, never expose GEDCOM identifiers in public surfaces. The lifecycle is `GEDCOM → RAW → Evidence Extraction → Governed Claims → EvidenceBundle → Policy Review → OverlayPointer → Published Runtime Envelope`. *(CONFIRMED doctrine / PROPOSED implementation. [DOM-PEOPLE; Pass-10 C9-01])*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 4. Exclusions and explicit non-ownership

Genealogy is presented here as one slice of People / Genealogy / DNA / Land Ownership. The following are explicitly **out of scope** for this sublane and live elsewhere:

| Excluded                                              | Belongs in                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------- |
| DNA match evidence, DNA segments, DTC raw genotypes   | [`sublanes/dna/README.md`](../dna/README.md) — *PROPOSED*             |
| Land ownership assertions, deeds, titles, parcel-version, chain-of-title | [`sublanes/land/README.md`](../land/README.md) — *PROPOSED* |
| Canonical person records (`PersonCanonical`) and identity resolution across all sublanes | [`sublanes/people/README.md`](../people/README.md) — *PROPOSED* |
| Settlements, cemeteries as places, schools as places, court venues       | `docs/domains/settlements-infrastructure/` *(CONFIRMED parent)*    |
| Indigenous community context, cultural sovereignty review                | `docs/domains/archaeology/` *(CONFIRMED parent)*                    |
| Spatial foundation, base layers, hydrology context                       | `docs/domains/spatial-foundation/` (and sibling natural-system domains) |

This sublane consumes context from those neighbors via governed cross-lane edges — it does not redefine them.

> [!WARNING]
> **The `people` / `genealogy` boundary is the live tension.** If the ADR settles on a
> three-way split, the kinship/life-event content here merges into the `people` sublane and
> this file becomes a redirect or is retired. If it settles on four-way, this boundary
> (genealogy owns relationships and life events; `people` owns `PersonCanonical` and identity
> resolution) holds. Do not treat either arrangement as canonical until the ADR lands.
> [OQ-PEOPLE-SUB-02]

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 5. Sublane architecture (diagram)

The diagram below shows how genealogical inputs traverse the trust membrane to become public-safe overlays. The shape is **CONFIRMED doctrine** (lifecycle invariant + trust membrane); specific arrows representing implementation are **PROPOSED**.

```mermaid
flowchart LR
  subgraph SRC["Sources — Source Role + Rights"]
    GED["GEDCOM 5.5 / GEDCOM-X<br/>uploaded files"]
    FS["FamilySearch API<br/>OAuth2 scoped"]
    VR["Vital / Cemetery / Obit /<br/>Church / Census records"]
    TREE["Tree overlays<br/>community-contributed"]
    CR["ConsentReceipt<br/>signed, machine-readable"]
  end

  subgraph LC["Lifecycle — RAW to PUBLISHED"]
    RAW[("RAW<br/>immutable capture")]
    WQ[("WORK / QUARANTINE<br/>normalize + classify")]
    PROC[("PROCESSED<br/>validated assertions")]
    CAT[("CATALOG / TRIPLET<br/>EvidenceBundle + graph")]
    PUB[("PUBLISHED<br/>governed releases only")]
  end

  subgraph GATE["Governance Gates"]
    G1{{"SourceDescriptor<br/>+ rights + sensitivity"}}
    G2{{"Validators + PolicyDecision<br/>+ Living-person screen"}}
    G3{{"EvidenceRef resolves<br/>+ ValidationReport"}}
    G4{{"Catalog closure<br/>+ EvidenceBundle"}}
    G5{{"ReleaseManifest<br/>+ ReviewRecord<br/>+ rollback target"}}
  end

  subgraph OUT["Public-Safe Outputs"]
    OP["OverlayPointer<br/>opaque, short-TTL"]
    ENV["RuntimeResponseEnvelope<br/>ANSWER / ABSTAIN / DENY / ERROR"]
    ED["Evidence Drawer<br/>citation surface"]
  end

  GED --> G1 --> RAW
  FS --> G1
  VR --> G1
  TREE --> G1
  CR -.governs.-> G2
  CR -.governs.-> G5

  RAW --> G2 --> WQ
  WQ --> G3 --> PROC
  PROC --> G4 --> CAT
  CAT --> G5 --> PUB

  PUB --> OP
  PUB --> ENV
  PUB --> ED

  classDef gate fill:#fff7e6,stroke:#d97706,color:#7c2d12;
  classDef pub  fill:#e6f4ff,stroke:#0369a1,color:#0c4a6e;
  class G1,G2,G3,G4,G5 gate
  class OP,ENV,ED pub
```

> [!NOTE]
> Public clients never read RAW, WORK, or QUARANTINE directly — that bypasses the trust membrane (Directory Rules; lifecycle invariant). All public reads flow through the governed API and resolve `EvidenceRef → EvidenceBundle` at dereference time. *(CONFIRMED doctrine.)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 6. Ubiquitous language

KFM-specific terms used in this sublane. Definitions are **CONFIRMED as terms**; field-level realization is **PROPOSED** pending schema home.

| Term                       | Definition (constrained by source role, evidence, time, release state) | Status |
| -------------------------- | ---------------------------------------------------------------------- | ------ |
| **Person Assertion**       | A claim that a person existed with given attributes, bound to its source role and evidence — never sovereign truth. | CONFIRMED term / PROPOSED field |
| **PersonCanonical**        | The deterministically-identified canonical person reference, derived from one or more assertions after identity resolution. | CONFIRMED term / PROPOSED field |
| **NameAssertion**          | A claim that a person bore a name in a given context — multiple NameAssertions per person are expected. | CONFIRMED term / PROPOSED field |
| **LifeEvent**              | An event in a person's life (birth, marriage, death, residence-start, etc.) carrying valid time, source time, and evidence. | CONFIRMED term / PROPOSED field |
| **Genealogy Relationship** (a.k.a. **RelationshipAssertion**) | An evidence-bound, confidence-scored claim of kinship between persons. Hypothesis until corroborated. | CONFIRMED term / PROPOSED field |
| **FamilyGroup**            | A bounded set of related persons, often nuclear, used for navigation and disambiguation. | CONFIRMED term / PROPOSED field |
| **Relationship Hypothesis**| A scored, evidence-weighted candidate relationship pending steward or evidence-closure decision. | CONFIRMED term / PROPOSED field |
| **Person Identity Candidate**| A pre-resolution candidate suggesting two Person Assertions may refer to the same canonical person. | CONFIRMED term / PROPOSED field |
| **ConsentGrant**           | A scoped, revocable, time-bounded authorization for processing or publication of person-linked data. | CONFIRMED term / PROPOSED field |
| **RevocationReceipt**      | The signed record of consent withdrawal, triggering downstream embargo and tombstone propagation. | CONFIRMED term / PROPOSED field |

> [!TIP]
> The terms above are the **interior** vocabulary. The exterior vocabulary (CIDOC-CRM `E21 Person`, `E5 Event`, `E13 Attribute Assignment`; PROV-O `Activity / Entity / Agent`; Schema.org `Person`) is used in graph projections and web surfaces, with `sameAs` linkage to authority IRIs (Wikidata, LCNAF, VIAF, ISNI). *(CONFIRMED. [Pass-10 C7, C8])*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 7. Object families owned here

Object families this sublane is responsible for, with identity and temporal handling. **Note:** under doctrine these object families are owned by the single `[DOM-PEOPLE]` bounded context; the table reflects this *proposed* genealogy/people partition, not a doctrinal sub-partition. [DOM-PEOPLE §E; OQ-PEOPLE-SUB-02]

| Object                       | Purpose                                                                | Identity rule (**PROPOSED**)                                 | Temporal handling (**CONFIRMED**)                                                              |
| ---------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `Person Assertion`           | Per-source claim that a person existed; evidence and confidence required. | source_id + object role + temporal scope + normalized digest | source, observed, valid, retrieval, release, and correction times stay distinct where material |
| `NameAssertion`              | A name borne by a person in a given context; multiple per person.       | source_id + object role + temporal scope + normalized digest | same                                                                                           |
| `LifeEvent`                  | Birth, marriage, death, baptism, naturalization, etc.                   | source_id + object role + temporal scope + normalized digest | same                                                                                           |
| `Residence Event`            | Person-at-place over an interval; bridges to settlements via residence relation. | source_id + object role + temporal scope + normalized digest | same                                                                                  |
| `Migration Event`            | Person-between-places event chain; carries uncertainty.                 | source_id + object role + temporal scope + normalized digest | same                                                                                           |
| `Genealogy Relationship`     | Evidence-bound, scored relationship claim.                              | source_id + object role + temporal scope + normalized digest | same                                                                                           |
| `FamilyGroup`                | Bounded set of related persons.                                         | source_id + object role + temporal scope + normalized digest | same                                                                                           |
| `Relationship Hypothesis`    | Pre-decision scored candidate relationship.                             | source_id + object role + temporal scope + normalized digest | same                                                                                           |
| `Person Identity Candidate`  | Pre-resolution merge candidate across Person Assertions.                | source_id + object role + temporal scope + normalized digest | same                                                                                           |

*(Object purposes and lifecycle handling: [DOM-PEOPLE] [ENCY], Atlas v1.1 §16 E.)*

> [!NOTE]
> Identity rules above are **PROPOSED** until ratified by ADR. The temporal-distinction rule — source / observed / valid / retrieval / release / correction times treated separately — is **CONFIRMED doctrine** and applies uniformly across object families. The split of these families between `genealogy` and `people` is **PROPOSED** (OQ-PEOPLE-SUB-02); in a three-way arrangement they all live in `people`.

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 8. Source families and source roles

| Source family                                                                                                       | Source role(s)                            | Rights / sensitivity                                                          | Freshness               | Status                  |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------- | ----------------------- | ----------------------- |
| Vital / cemetery / burial / obituary / church / school / military / census / directory / court / probate records   | authority / observed / context / modeled | rights & current terms **NEEDS VERIFICATION**; sensitive joins fail closed    | source-vintage specific | [DOM-PEOPLE] [ENCY]     |
| GEDCOM / GEDZip / tree overlays                                                                                     | authority / observed / context / modeled | rights & current terms **NEEDS VERIFICATION**; sensitive joins fail closed    | source-vintage specific | [DOM-PEOPLE] [ENCY]     |
| FamilySearch API responses                                                                                          | observed                                   | OAuth2-scoped consent; user-revocable                                          | live / cadence-bound    | [Pass-10 C9-02] CONFIRMED upstream / PROPOSED integration |
| DNA vendor match data (DTC genomic exports, segment, triangulation)                                                 | observed                                   | **default-deny**; restricted-policy required                                  | source-vintage specific | [DOM-PEOPLE] [ENCY] — *out of scope here; see [`dna/README.md`](../dna/README.md)* |

> [!WARNING]
> Rights and current terms for every source family are flagged **NEEDS VERIFICATION**. Source admission MUST NOT proceed without a resolvable `SourceDescriptor` carrying source role, authority, rights, sensitivity, cadence, and a payload/reference hash. *(CONFIRMED doctrine / PROPOSED implementation.)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 9. Pipeline shape (RAW → PUBLISHED)

The lifecycle invariant — `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` — is **CONFIRMED doctrine**. Per-stage handling for genealogy is **PROPOSED implementation**.

| Stage              | Handling                                                                                                                         | Gate                                                                                | Status   |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------- |
| **RAW**            | Capture immutable GEDCOM/API/scan payload with source role, rights, sensitivity, citation, time, hash. Create `ConsentReceipt`s. | `SourceDescriptor` exists; admission policy satisfied.                              | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema (GEDCOM 5.5 ↔ GEDCOM-X), dates (ABT/BEF/AFT/BET/CAL → ISO 8601 intervals), places (anchor to GNIS/TGN where possible), identities, evidence, rights, sensitivity. Hold failures with quarantine reason. | Validation + policy gate pass, or quarantine reason recorded.                       | PROPOSED |
| **PROCESSED**      | Emit validated normalized assertions and receipts; produce public-safe candidates after living-person screen and redaction.       | `EvidenceRef` resolves, `ValidationReport` present, digest closure verified.        | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`s, graph/triplet projections (CIDOC-CRM `E21` / `E5` / `E13`, PROV-O), release candidates. | Catalog/proof closure passes.                                                       | PROPOSED |
| **PUBLISHED**      | Serve via governed API only. Public envelopes carry `OverlayPointer`s, not PII; `EvidenceRef`s resolve to bundles at dereference time. | `ReleaseManifest`, review state where required, rollback target, correction path. | PROPOSED |

*(Lifecycle invariant: Directory Rules §9; ENCY. Stage table adapted from Atlas v1.1 §16 H.)*

> [!IMPORTANT]
> **Promotion is a governed state transition, not a file move.** A path-level move that bypasses validators, policy gates, evidence-bundle creation, catalog closure, and release-decision recording violates the lifecycle invariant regardless of which directory the bytes end up in. *(CONFIRMED doctrine. [DIRRULES §9])*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 10. Policy and sensitivity posture

### 10.1 Three-layer separation

The Genealogy sublane MUST keep three layers explicitly separate. Collapsing any pair into one is a **publication-level drift**:

1. **Canonical Human Assertions** — internal only; never public by default. Examples: Person Assertion, RelationshipAssertion, LifeEvent claim, Residence Event claim.
2. **Evidence Layer** — `EvidenceBundle`-backed, immutable lineage. Examples: census image, church record, obituary, gravestone photo, archive citation.
3. **Publication / Experience Layer** — derived and policy-filtered, downstream carrier — never sovereign truth. Examples: map overlays, timelines, story exports, graph views.

*(CONFIRMED architectural recommendation. [ENCY; Pass-10 C5/C6].)*

### 10.2 Fail-closed publication gates

The matrix below is **PROPOSED** and reflects the recommended baseline. Each row is a `MUST DENY` condition the OPA policy bundle should enforce at promotion and at dereference.

| Condition                                              | Decision |
| ------------------------------------------------------ | -------- |
| Missing `ConsentReceipt` for living-person scope       | DENY     |
| Missing retention field on `ConsentReceipt`            | DENY     |
| Unknown subject scope                                  | DENY     |
| Living person without explicit, scoped consent         | DENY     |
| Any DNA / genomic payload (handled in `dna/README.md`) | DENY     |
| Exact burial coordinates in public export              | DENY     |
| Raw GEDCOM identifiers in overlay pointer              | DENY     |
| Unresolved `EvidenceRef`                               | DENY     |
| Publication before promotion                           | DENY     |
| Revoked consent (per status-list check)                | DENY     |
| Missing `spec_hash`                                    | DENY     |
| Invalid DSSE signature on receipt                      | DENY     |

*(Fail-closed table reframed for this sublane from the corpus consent/redaction doctrine [Pass-10 C6-06..C6-08]. PROPOSED until policy bundle lands.)*

### 10.3 Reidentification Risk Score (proposed gate)

A pre-publication score evaluating uniqueness, spatial precision, temporal precision, relationship density, and small-community exposure. Outcomes:

- **ANSWER** — publish as-is
- **GENERALIZE** — coarsen geometry or time, or substitute initials / relationship labels
- **DELAY** — embargo until time-based risk diminishes
- **DENY** — withhold from public surface

This gate fits naturally into `DecisionEnvelope` semantics. *(PROPOSED. [Pass-10 C6-06].)*

> [!WARNING]
> The sensitivity rubric is **0–5** (public to highest-restricted) and applies across genealogy outputs. Per-class rubric calibration for genealogy is an **open expansion** ([Pass-10 C6-01]). Until calibration is published, default to the higher-restricted reading when in doubt. The mapping between the 0–5 rubric and the Atlas §24.5 T0–T4 tier scheme is itself unresolved (ADR-S-05).

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 11. Publication: overlay pointers, not PII

Public clients receive opaque, short-TTL pointers — never identifiers. Recommended runtime envelope shape (**PROPOSED**, illustrative, from [Pass-10 C6-08]):

```json
{
  "outcome": "ANSWER",
  "overlay_pointer": "overlay://9f2a...",
  "policy_label": "public",
  "retention": "P90D",
  "no_reidentification": true,
  "evidence_bundle_refs": [
    "kfm://evidence/..."
  ]
}
```

**Never** embed in public envelopes: names · exact dates of birth · GEDCOM IDs · family IDs · DNA markers (handled in `dna/README.md`, denied entirely from public) · exact burial coordinates.

**Always** prefer: opaque overlay pointers · server-side dereference · signed runtime envelopes (DSSE) · short TTLs · revocation-aware fetches · policy evaluation at dereference time.

This preserves rollback, revocation, and correction capability downstream. *(CONFIRMED doctrine / PROPOSED implementation.)*

<details>
<summary><strong>Verifiable Credential / SD-JWT flow (PROPOSED expansion)</strong></summary>

The corpus identifies a path toward selective-disclosure VCs (SD-JWT, BBS+) for consent: the holder presents a derived presentation containing only the fields a given overlay needs; the verifier checks the VC proof, the DSSE signature on the consent receipt pointer, and a privacy-preserving revocation status (W3C Bitstring Status List or accumulator). Any failure → DENY with reason surfaced.

Illustrative presentation shape:

```json
{
  "presentation": {
    "disclosed": { "relationship": "cousin", "lat": 38.97, "lon": -95.24 },
    "redactions": { "name": "J.D.", "dna_markers": "hashed-aggregate" }
  },
  "proofs": { "sdjwt": "...", "revocation": "good", "dsse": "valid" }
}
```

Status: **PROPOSED future expansion**. Baseline opaque-pointer model is sufficient for v1 publication. *(See [Pass-10 C9-04] for GA4GH AAI / Passports / DUO context.)*

</details>

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 12. Cross-lane and cross-sublane handoffs

Edges are **CONFIRMED doctrine**; specific schema fields realizing each edge are **PROPOSED**.

| Edge direction | Counterpart                         | Relation                                                                          | Constraint                                                              |
| -------------- | ----------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| consumes from  | `sublanes/people/` (PROPOSED)       | `PersonCanonical` identity resolution                                             | Preserves source role + evidence; never overrides Person Assertion lineage |
| consumes from  | `sublanes/dna/` (PROPOSED)          | `DNAMatchEvidence` and segment data **only via restricted-access channel**         | Default-deny; review-required; never embedded in public overlays         |
| consumes from  | `sublanes/land/` (PROPOSED)         | `Ownership Interval`, residence-parcel context                                     | Assessor/tax ≠ title truth; parcel geometry ≠ title boundary             |
| consumes from  | `docs/domains/settlements-infrastructure/` | Residence, cemetery, school, court, county, township, place relation         | Living-person fields fail closed [Atlas v1.1 §16 F]                      |
| consumes from  | `docs/domains/roads-rail-trade/`    | Migration, access, movement context                                                | Preserves ownership, source role, sensitivity, EvidenceBundle support     |
| consumes from  | `docs/domains/archaeology/`         | Indigenous community context; cultural affiliation                                 | Steward-reviewed and rights-bounded; sovereignty preserved [Atlas v1.1 §16 F] |
| emits to       | `docs/domains/frontier-matrix/`     | Aggregated population observations feeding matrix cells                            | Matrix cells are analytical releases with own evidence and rollback      |
| emits to       | Governed AI (`runtime/`)            | Released EvidenceBundles for summarization                                          | ABSTAIN when evidence insufficient; DENY where policy blocks              |

*(Edge catalog: Atlas v1.1 §16 F [DOM-PEOPLE]; Pass-10 cross-cutting themes.)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 13. Governed AI behavior in this sublane

| AI action                | Required posture                                                                                                                          | Outcome envelope                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Summarize a released `EvidenceBundle` for a historical person | Permitted; cite the bundle; bound confidence to bundle's confidence; preserve uncertainty in wording.                                | ANSWER + `evidence_refs` + citation_validation |
| Compare two `Relationship Hypothesis` candidates             | Permitted as evidence comparison only; never collapse hypothesis into fact.                                                          | ANSWER + bundle refs                          |
| Draft a steward review note                                  | Permitted; mark draft; require steward sign-off before any state transition.                                                          | ANSWER (draft) + review queue entry            |
| Infer a living-person relationship from DNA-derived evidence | **DENY**. Living-person + DNA-derived inference fails closed regardless of evidence.                                                 | DENY + reason                                  |
| Answer about a person when `EvidenceRef` is missing or unresolved | **ABSTAIN**. Cite the gap; do not synthesize.                                                                                  | ABSTAIN + gap reason                           |
| Generate a public surface (overlay, story, map label)        | Only from `PUBLISHED` releases via governed API; never directly from RAW/WORK/QUARANTINE; never bypass `OverlayPointer` discipline.   | ANSWER (governed) or DENY                     |

Every AI response in this sublane emits an `AIReceipt` with `outcome ∈ {ANSWER, ABSTAIN, DENY, ERROR}`, `evidence_refs`, `policy_decision`, and `citation_validation`. *(CONFIRMED doctrine. [DOM-PEOPLE §L; ENCY; GAI].)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 14. Validators, fixtures, and CI gates

### 14.1 Validators (PROPOSED homes)

| Validator                           | What it checks                                                                                  | PROPOSED path                                                                              |
| ----------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| GEDCOM conformance reporter         | GEDCOM 5.5 / GEDCOM-X structural validity; reports tolerated deviations and rejected records.   | `tools/validators/people-dna-land/validate_gedcom.py` *(PROPOSED)*                         |
| Consent receipt validator           | Schema validity, signature presence, retention bounds, revocation URI, no raw identifiers leaking. | `tools/validators/people-dna-land/validate_consent_receipt.py` *(PROPOSED)*             |
| Overlay pointer validator           | Opaque-only, expiry present, no PII fields, no GEDCOM refs, scope + retention labels present.    | `tools/validators/people-dna-land/validate_overlay_pointer.py` *(PROPOSED)*              |
| EvidenceRef closure check           | Every published assertion resolves to a valid, signed `EvidenceBundle`.                          | shared validator under `tools/validators/evidence/` *(PROPOSED)*                          |
| Living-person screen                | Heuristic + policy check for living-person fields; fails closed when uncertain.                  | `tools/validators/people-dna-land/screen_living_persons.py` *(PROPOSED)*                  |

> [!NOTE]
> Validator paths use the whole-domain `people-dna-land` segment, not a `genealogy` segment —
> per §12, tooling does not subdivide by sublane. A flat `tools/validators/genealogy/` home
> (used in an earlier draft) would presuppose the unresolved sublane partition. [DIRRULES §12]

### 14.2 Negative fixtures (recommended early investments)

Negative fixtures are governance assets — they prove the rules are enforceable.

| Fixture                              | Expected | PROPOSED path                                                                |
| ------------------------------------ | -------- | ---------------------------------------------------------------------------- |
| `expired_receipt.json`               | FAIL     | `fixtures/domains/people-dna-land/genealogy/negative/` *(PROPOSED)*          |
| `revoked_receipt.json`               | FAIL     | same                                                                          |
| `living_person_export.json`          | FAIL     | same                                                                          |
| `missing_retention.json`             | FAIL     | same                                                                          |
| `raw_gedcom_overlay.json`            | FAIL     | same                                                                          |
| `unresolved_evidence_ref.json`       | FAIL     | same                                                                          |
| `exact_burial_coordinates.json`      | FAIL     | same                                                                          |
| `invalid_signature.json`             | FAIL     | same                                                                          |
| `valid_public_overlay.json`          | PASS     | `fixtures/domains/people-dna-land/genealogy/positive/` *(PROPOSED)*           |

*(Negative fixture set adapted from the corpus consent/publication gates [Pass-10 C6-06..C6-08].)*

### 14.3 CI gate layers

```text
Schema Layer
  - JSON schema validity
  - required fields present
  - enum correctness

Governance Layer
  - retention bounds enforced
  - consent scope known and valid
  - revocation status checked
  - living-person restrictions honored

Publication Layer
  - no PII leakage
  - no raw GEDCOM IDs
  - generalized geometry rules satisfied
  - overlay expiry enforced

Provenance Layer
  - spec_hash present
  - DSSE signatures valid
  - EvidenceRefs resolvable
```

*(CI gate layering adapted from corpus C5/C6 governance machinery.)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 15. FAIR + CARE posture

The Genealogy sublane is one of the clearest sites where **FAIR by design, CARE in practice** applies ([Pass-10 C9-05; FAIR/CARE]). The pairing is operationalized here as:

- **Findable** — every assertion carries a stable identifier and source citation; catalog records expose discovery metadata.
- **Accessible** — released artifacts are accessible via the governed API; sensitive layers gate at dereference, not at indexing.
- **Interoperable** — graph projection uses CIDOC-CRM (`E21 Person`, `E5 Event`, `E13 Attribute Assignment`) and Schema.org Person/Event for web surfaces; authority anchoring via Wikidata QID, LCNAF, VIAF, ISNI.
- **Reusable** — clear licensing, evidence-per-claim attribution, content-addressed bundles, deterministic rebuild from receipts.

CARE gates **what can publish**, to whom, on what terms:

- **Collective Benefit** — public-safe family/history story maps serve genealogical research while preserving descendant communities' interests.
- **Authority to Control** — Indigenous community context flows through the Archaeology domain's steward review (Atlas v1.1 §16 F); living-person scope is controlled by the subject via revocable consent.
- **Responsibility** — every published assertion carries provenance back to its evidence; corrections and rollbacks propagate.
- **Ethics** — DNA, living-person, and culturally sensitive content are denied by default; publication requires explicit policy approval.

> [!TIP]
> Where FAIR and CARE appear to conflict — e.g., a request to make an asset findable when community authority requires it not be findable at all — the corpus's posture is to use an explicit *not-findable-by-policy* convention so the catalog can record absence without leaking existence. *(PROPOSED expansion. [Pass-10 C9-05].)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 16. Open questions and verification backlog

| ID    | Item                                                                                                              | Evidence that would settle it                                                                          | Status               |
| ----- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------- |
| OQ-PEOPLE-SUB-01 | Is `docs/domains/<domain>/sublanes/` a ratified convention, or should sublane docs live flat at `docs/domains/<domain>/<sublane>.md`? | ADR amending Directory Rules §12; mounted-repo evidence of either pattern. | NEEDS VERIFICATION |
| OQ-PEOPLE-SUB-02 | **Is there a standalone `genealogy` sublane (four-way split) or does genealogy fold into `people` (three-way split)?** A prior `sublanes/README.md` proposed three-way; this doc proposes four-way. | ADR fixing sublane count and names; `[DOM-PEOPLE]` is a single bounded context with no doctrinal sub-partition. | **CONFLICTED** |
| OQ-GEN-03 | When does a non-conforming GEDCOM file fail the gate vs. accept with a warning?                                   | GEDCOM conformance test corpus + threshold policy ([Pass-10 C9-01]).                                   | NEEDS VERIFICATION   |
| OQ-GEN-04 | Retention policy for FamilySearch responses after upstream consent revocation — embargo, surface, or escalate?    | FamilySearch retention policy doc; GA4GH consent revocation semantics ([Pass-10 C9-02]).               | NEEDS VERIFICATION   |
| OQ-GEN-05 | Default `k` for living-person overlays — fixed at `k=10` or scaled with population density?                       | Pilot data; policy decision ([Pass-10 C6-06]).                                                          | UNKNOWN              |
| OQ-GEN-06 | Per-domain calibration of the 0–5 sensitivity rubric for genealogy, and its mapping to the §24.5 T0–T4 tiers.     | Per-domain rubric calibration register ([Pass-10 C6-01]); ADR-S-05.                                    | NEEDS VERIFICATION   |
| OQ-GEN-07 | Schema homes — confirm `schemas/contracts/v1/domains/people-dna-land/…` structure against ADR-0001.               | Mounted-repo schemas tree; ADR-0001 reading.                                                            | NEEDS VERIFICATION   |
| OQ-GEN-08 | Owner / steward identity for the People / Genealogy / DNA / Land Ownership domain.                                 | `CODEOWNERS` / governance register entry.                                                               | NEEDS VERIFICATION   |
| OQ-GEN-09 | Consent receipt envelope: Kantara form vs. lightweight DSSE-wrapped JSON; VC/SD-JWT timing.                        | ADR — Consent Receipts as First-Class Governance Objects ([Pass-10 C6-07]).                            | NEEDS VERIFICATION   |
| OQ-GEN-10 | Authority-ladder ordering for person identifiers — Wikidata QID vs. LCNAF vs. VIAF vs. ISNI when they conflict.     | Authority-ladder formalization ([Pass-10 C7-01..04]).                                                  | NEEDS VERIFICATION   |
| OQ-GEN-11 | Tombstone format for revoked content, and propagation SLA across downstream derivatives.                            | Tombstone-format spec ([Pass-10 C5-09]); revocation-event SLA ([Pass-10 C6-08]).                        | NEEDS VERIFICATION   |
| OQ-GEN-12 | Whether `policy/consent/people/` (Atlas §24.13) or `policy/domains/people-dna-land/consent/` (DIRRULES §12) is canonical. | Mounted repo + ADR. | CONFLICTED |

> [!NOTE]
> All open questions above will be filed (or aliased) to `docs/registers/VERIFICATION_BACKLOG.md` when this doc is published. Items that propose new placements or conventions — and the two CONFLICTED rows above — will additionally appear in `docs/registers/DRIFT_REGISTER.md`. *(PROPOSED. [DIRRULES §2.5].)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## 17. Related docs

- [`../README.md`](../README.md) — People / Genealogy / DNA / Land Ownership domain landing *(PROPOSED)*
- [`../sublanes/README.md`](./README.md) — sublanes index *(PROPOSED layer)*
- [`../people/README.md`](../people/README.md) — People sublane: PersonCanonical, identity resolution *(PROPOSED)*
- [`../dna/README.md`](../dna/README.md) — DNA sublane: DNAMatchEvidence, DNASegment, restricted access *(PROPOSED)*
- [`../land/README.md`](../land/README.md) — Land sublane: deeds, titles, parcels, chain-of-title *(PROPOSED)*
- [`directory-rules.md`](../../../../../directory-rules.md) — placement law (§3, §12, §2.4, §18 OPEN-DR-02)
- [`ai-build-operating-contract.md`](../../../../../ai-build-operating-contract.md) — operating law (`CONTRACT_VERSION = "3.0.0"`)
- [`docs/standards/PROV.md`](../../../../standards/PROV.md) — provenance vocabulary profile
- [`docs/standards/ISO-19115.md`](../../../../standards/ISO-19115.md) — metadata profile
- `docs/runbooks/people-dna-land/` — operational procedures *(per-source refresh runbooks PROPOSED; subfolder convention per §18 OPEN-DR-02)*

*(All link paths in this list are relative to this doc's PROPOSED location and **will need verification** once the sublane folder convention is ratified.)*

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)

## Truth labels used here

| Label                | Meaning                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **CONFIRMED**        | Verified in this session from attached KFM doctrine documents.                                                                |
| **PROPOSED**         | Design, recommendation, file path, or placement not yet verified in implementation.                                            |
| **INFERRED**         | Reasonably derivable from visible doctrine but not directly stated for this sublane specifically.                              |
| **NEEDS VERIFICATION** | Checkable, but not yet checked in this session — typically because the repo is not mounted.                                 |
| **UNKNOWN**          | Not resolvable without additional evidence beyond this session.                                                                |
| **CONFLICTED**       | Sources disagree, or doctrine and a prior sibling doc appear inconsistent; held until an ADR or drift-register entry resolves it. |
| **EXTERNAL**         | Sourced from authoritative external research (none used in this doc).                                                          |

---

**Last updated:** 2026-06-06 · **Doc id:** `kfm://doc/people-dna-land/sublanes/genealogy` · **Status:** Draft · **Version:** v1 · `CONTRACT_VERSION = "3.0.0"`

[↑ Back to top](#-genealogy-sublane--people--genealogy--dna--land-ownership)
