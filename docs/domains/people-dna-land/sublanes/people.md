<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/people-dna-land/sublanes/people
title: People Sublane — People, Genealogy, DNA, and Land Ownership Domain
type: standard
version: v0.1
status: draft
owners: <People/DNA/Land domain steward — TODO>, <docs steward — TODO>, <sensitivity reviewer — TODO>
created: 2026-05-18
updated: 2026-06-06
policy_label: restricted
related:
  # NEEDS VERIFICATION — every path below is PROPOSED until checked against a mounted repo
  - docs/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/sublanes/README.md
  - docs/domains/people-dna-land/sublanes/dna/README.md
  - docs/domains/people-dna-land/sublanes/genealogy/README.md
  - docs/domains/people-dna-land/sublanes/land.md
  - directory-rules.md
  - ai-build-operating-contract.md
  - docs/standards/PROV.md
tags: [kfm, domain, people, sublane, person-assertion, identity, life-events, residence, migration]
notes:
  # CONTRACT_VERSION = "3.0.0"
  # sublanes/ path segment is PROPOSED; not in Directory Rules §12; needs ADR (OQ-PEOPLE-SUB-01).
  # FILENAME CONFLICT: this draft uses flat sublanes/people.md; a prior draft used subfolder sublanes/people/README.md. Unresolved (OQ-PEOPLE-SUB-13).
  # Living-person + DNA-derived outputs are deny-by-default; person object families owned by single [DOM-PEOPLE] bounded context.
[/KFM_META_BLOCK_V2] -->

# 👤 People Sublane

> **Person assertions, person-canonical records, name assertions, life events, residences, and migrations — modeled as assertion-first, evidence-bound, privacy-aware claims under the People/DNA/Land domain.**

![Status](https://img.shields.io/badge/status-draft-orange)
![Doc%20type](https://img.shields.io/badge/doc%20type-domain%20sublane-blue)
![Domain](https://img.shields.io/badge/domain-people--dna--land-7a52a7)
![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-1f7a3a)
![Sensitivity](https://img.shields.io/badge/sensitivity-living--person%20fail--closed-b30000)
![sublanes/](https://img.shields.io/badge/sublanes%2F-PROPOSED-lightgrey)
![CONTRACT_VERSION](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)

**Status:** `draft` · **Owners:** _TBD — People/DNA/Land steward; docs steward_ · **Last updated:** _2026-06-06_ · **`CONTRACT_VERSION = "3.0.0"`**

> [!IMPORTANT]
> This sublane handles **person-shaped assertions** (who someone was, what happened to them, where they lived, where they moved) — **not** DNA-derived identity, **not** land instruments or parcel chain-of-title, **not** relationship hypotheses scored from DNA matches. Those concerns live in sibling sublanes (`dna`, `genealogy`, `land`) and are referenced where they intersect.

> [!CAUTION]
> **Structural conflict — fifth variant in this tree.** This draft places the People sublane at the **flat** path `sublanes/people.md` (with flat `genealogy.md` / `dna.md` / `land.md` siblings). A prior draft placed it at the **subfolder** path `sublanes/people/README.md`. Across the five sublane docs authored so far, three things remain unresolved: whether `sublanes/` exists at all (OQ-PEOPLE-SUB-01), how many sublanes and their names (OQ-PEOPLE-SUB-02), and flat-vs-subfolder filenames (OQ-PEOPLE-SUB-13). This doc is produced as requested; the conflict is surfaced and routed to the `sublanes/` ADR, not silently resolved. [DIRRULES §12]

---

## Quick jump

- [1 · Scope](#1--scope)
- [2 · Repo fit](#2--repo-fit)
- [3 · Inputs](#3--inputs)
- [4 · Exclusions](#4--exclusions)
- [5 · Sublane structure](#5--sublane-structure)
- [6 · Ubiquitous language](#6--ubiquitous-language)
- [7 · Object families](#7--object-families)
- [8 · Source families](#8--source-families)
- [9 · Pipeline shape](#9--pipeline-shape-raw--published)
- [10 · Sensitivity, rights, and publication posture](#10--sensitivity-rights-and-publication-posture)
- [11 · Governed AI behavior](#11--governed-ai-behavior)
- [12 · Cross-sublane and cross-lane relations](#12--cross-sublane-and-cross-lane-relations)
- [13 · API, contract, and schema surfaces](#13--api-contract-and-schema-surfaces)
- [14 · Validators, tests, fixtures](#14--validators-tests-fixtures)
- [15 · Related docs](#15--related-docs)
- [16 · Open questions & verification backlog](#16--open-questions--verification-backlog)

---

## 1 · Scope

**CONFIRMED doctrine / PROPOSED implementation.** The People sublane represents people inside the Kansas Frontier Matrix (KFM) as **assertion-first, evidence-bound, privacy-aware** claims, with a strong default-deny posture for any output that touches **living persons** or that would equate a name on a record with an identified individual without supporting evidence. It owns the person-and-life-events portion of the broader People/Genealogy/DNA/Land domain and serves as upstream context for the sibling `genealogy`, `dna`, and `land` sublanes. [DOM-PEOPLE §A/§B]

**This sublane owns** (CONFIRMED terms / PROPOSED field realization, per `[DOM-PEOPLE]`):

- `Person Assertion` — a per-source claim that a person existed, with name, time, place, and source role.
- `PersonCanonical` — a curated, evidence-bound, internal-only canonical person record built from one or more `Person Assertion`s.
- `NameAssertion` — a per-source name variant tied to a person and a temporal window.
- `Person Identity Candidate` — a proposed cross-source identity link, with confidence and supporting evidence, not yet promoted to `PersonCanonical`.
- `LifeEvent` — birth, baptism, marriage, divorce, death, burial, military service, naturalization, or other life-stage events anchored to a `Person Assertion`.
- `Residence Event` — a person-anchored residence at a place over a valid-time interval.
- `Migration Event` — a person-anchored move between two places, with directionality and uncertainty.

> [!NOTE]
> `ReviewRecord` is **not** owned by this sublane. It is a cross-cutting governance receipt
> in the Atlas §24.2 receipt catalog (a steward/rights-holder/policy review of a candidate
> transition — admission, redaction, promotion, release). This sublane *triggers and
> references* `ReviewRecord`s at its promotion gates; it does not define them. [Atlas §24.2]

> [!NOTE]
> Identity resolution **scoring** is owned here; relationship-hypothesis scoring **across persons** is shared with the `genealogy` slice. Where a single hypothesis spans both (e.g., "two `Person Assertion`s are the same person AND that person is the mother of another `Person Assertion`"), the *identity* edge is resolved here and the *relationship* edge is resolved in `genealogy`. (Whether `genealogy` is a standalone sublane or folds into `people` is itself unresolved — OQ-PEOPLE-SUB-02.)

[Back to top](#-people-sublane)

---

## 2 · Repo fit

> [!WARNING]
> This document's path — `docs/domains/people-dna-land/sublanes/people.md` — is **PROPOSED**. Directory Rules §12 specifies `docs/domains/<domain>/` as the canonical doc home for a domain and lists `people-dna-land` as the domain segment. The `sublanes/` segment **is not documented** in `directory-rules.md` (it is the same class of open question as the runbook-subfolder one, §18 OPEN-DR-02) and should either be (a) ratified by an ADR amending §12 to allow a per-domain sublane segment, or (b) collapsed into `docs/domains/people-dna-land/people.md` and sibling files. Until resolved, treat this path as `PROPOSED / CONFLICTED` per §2.5.

**Domain home (CONFIRMED domain segment, PROPOSED tree):**

```text
docs/domains/people-dna-land/        # CONFIRMED segment per Directory Rules §12
├── README.md                         # PROPOSED — domain README
└── sublanes/                         # PROPOSED segment — needs ADR (OQ-PEOPLE-SUB-01)
    ├── people.md                     # THIS DOCUMENT (flat form — conflicts with prior people/README.md)
    ├── genealogy.md                  # PROPOSED sibling (flat form)
    ├── dna.md                        # PROPOSED sibling (flat form)
    └── land.md                       # PROPOSED sibling (flat form)
```

> [!CAUTION]
> The tree above shows the **flat** filename form. Prior drafts in this same tree used the
> **subfolder** form (`people/README.md`, `dna/README.md`, `genealogy/README.md`) and a flat
> `land.md` / `land_ownership.md`. A domain cannot coherently mix conventions. Resolved by the
> `sublanes/` ADR (OQ-PEOPLE-SUB-13). [DIRRULES §12]

**Upstream (this sublane consumes from):**

- `directory-rules.md` *(repo root)* — placement and lifecycle law.
- `ai-build-operating-contract.md` *(repo root)* — operating law (`CONTRACT_VERSION = "3.0.0"`).
- `docs/domains/people-dna-land/README.md` — domain-level scope, boundary, ubiquitous language. *(PROPOSED path)*

**Downstream (this sublane is referenced by):**

- `docs/domains/people-dna-land/sublanes/genealogy(.md|/README.md)` — consumes `Person Assertion`, `PersonCanonical`, `LifeEvent`. *(PROPOSED path)*
- `docs/domains/people-dna-land/sublanes/dna(.md|/README.md)` — DNA evidence is **never** allowed to mutate `PersonCanonical` directly. *(PROPOSED path)*
- `docs/domains/people-dna-land/sublanes/land(.md)` — `Land Ownership Assertion` may **reference** a `PersonCanonical`, but person↔parcel joins are restricted by sensitivity policy. *(PROPOSED path)*
- `docs/domains/settlements-infrastructure/` — residence events anchor settlement membership. *(PROPOSED path)*

[Back to top](#-people-sublane)

---

## 3 · Inputs

**CONFIRMED doctrine / PROPOSED implementation.** Inputs admitted to this sublane MUST carry a `SourceDescriptor` with explicit source role, rights, sensitivity, citation, time, and hash. Source roles use the canonical seven-role vocabulary (`observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, `synthetic`) from the Atlas §24.1 anti-collapse register. Rights status and sensitivity remain `NEEDS VERIFICATION` until reviewed; sensitive joins fail closed.

| Source family | Typical role | Examples | Status |
|---|---|---|---|
| Vital records | `authority` / `observed` | birth, death, marriage certificates (where public/legal) | NEEDS VERIFICATION for rights and current terms |
| Cemetery / burial / obituary | `authority` / `observed` | gravestone surveys, burial overlays (rights-checked), newspaper obituaries | NEEDS VERIFICATION |
| Church records | `authority` / `observed` | baptism, marriage, burial registers | NEEDS VERIFICATION |
| School / military records | `authority` / `observed` | yearbooks (public), draft registrations, service records | NEEDS VERIFICATION |
| Census records | `authority` / `observed` | U.S. decennial census schedules, state censuses | NEEDS VERIFICATION |
| Directory records | `observed` / `context` | city directories, gazetteers | NEEDS VERIFICATION |
| Court / probate records | `authority` / `observed` | wills, guardianship, probate inventories | NEEDS VERIFICATION |
| GEDCOM / GEDZip / tree overlays | `modeled` / `candidate` (hypothesis) | uploaded family trees, FamilySearch tree exports | NEEDS VERIFICATION; treated as hypothesis, never authority |

> [!CAUTION]
> **Tree overlays are not authority.** A relationship asserted in an uploaded GEDCOM is admitted as a `modeled`/`candidate`-role hypothesis and MUST link through an `EvidenceBundle` to authoritative sources before any derived public output is permitted. This is the corpus's standing warning against unsourced family folklore hardening into a "fact." [DOM-PEOPLE §D; Pass-10 C9-01]

[Back to top](#-people-sublane)

---

## 4 · Exclusions

The following are **explicitly out of scope** for this sublane. Where the boundary is close, the redirect is named.

| Excluded content | Redirect | Why |
|---|---|---|
| DNA match evidence, DNA segments, DNA kit tokens | `sublanes/dna` *(PROPOSED)* | DNA-derived identity and relationship inference are restricted by default and require a separate governance surface. |
| Relationship hypotheses scored from DNA segments | `sublanes/dna` *(PROPOSED)* | DNA-derived relationships are not equivalent to evidence-bound genealogy relationships. |
| `Genealogy Relationship`, `FamilyGroup`, `Relationship Hypothesis` | `sublanes/genealogy` *(PROPOSED)* | Relationship modeling and family-group projection sit in the genealogy slice. |
| Land instruments, deeds, titles, assessor/tax records | `sublanes/land` *(PROPOSED)* | Land governance has its own assertion-first model. Assessor/tax records are NOT title truth. |
| Parcel geometry, legal descriptions, PLSS-derived geometry | `sublanes/land` *(PROPOSED)* | Parcel geometry is a geometry version, not a title-boundary proof. |
| Settlement / municipality / census-place entities | `docs/domains/settlements-infrastructure/` *(PROPOSED)* | Places that residences refer to live in the settlements lane. |
| Archaeological cultural affiliation of named individuals | `docs/domains/archaeology/` *(PROPOSED)* | Steward-reviewed and rights-bounded; requires Archaeology governance. |
| Living-person fields exposed to the public surface | _denied by policy_ | Living-person output fails closed by default; see §10. |
| Sovereign tribal-citizenship determinations | _not owned by KFM_ | KFM does not adjudicate citizenship or enrollment. |

[Back to top](#-people-sublane)

---

## 5 · Sublane structure

The People sublane sits inside the People/DNA/Land domain and feeds the sibling slices through controlled references. It never reads downstream stores and never publishes directly to the public surface — publication is a governed state transition handled by the domain's release pipeline.

```mermaid
flowchart LR
    subgraph PDL["People / DNA / Land Domain"]
        direction LR
        subgraph PEOPLE["sublanes/people — this document"]
            PA["Person Assertion"]
            PIC["Person Identity Candidate"]
            NA["NameAssertion"]
            LE["LifeEvent"]
            RE["Residence Event"]
            ME["Migration Event"]
            PC[("PersonCanonical<br/>internal only")]
            PA --> PIC --> PC
            NA --> PA
            LE --> PA
            RE --> PA
            ME --> PA
        end
        subgraph GEN["sublanes/genealogy"]
            GR["Genealogy Relationship"]
            FG["FamilyGroup"]
            RH["Relationship Hypothesis"]
        end
        subgraph DNA["sublanes/dna — restricted"]
            DME["DNAMatchEvidence"]
            DSE["DNASegment"]
            DKT["DNAKitToken"]
        end
        subgraph LAND["sublanes/land"]
            OA["Land Ownership Assertion"]
            LI["LandInstrument"]
            LP["LandParcel"]
        end
        PC -.refers to.-> GR
        PC -.refers to.-> OA
        DME -.MAY corroborate, never mutate.-> PIC
    end

    SD[("SourceDescriptors<br/>EvidenceBundles")] --> PEOPLE
    PEOPLE -->|"public-safe derivatives only"| API["Governed API"]
    API --> UI["Public UI · Evidence Drawer · Focus Mode"]

    classDef restricted fill:#fee,stroke:#b30000,stroke-width:2px,color:#b30000;
    class DNA restricted;
    classDef thisdoc fill:#eef,stroke:#3355cc,stroke-width:2px;
    class PEOPLE thisdoc;
```

> [!NOTE]
> The diagram is **doctrinally grounded** (object families, sublane separation, governed-API trust membrane) but **path-free**. Mounted-repo verification is required before treating any specific module, route, or component name as canonical.

[Back to top](#-people-sublane)

---

## 6 · Ubiquitous language

CONFIRMED terms from the People/DNA/Land domain that the People sublane uses. Field realization is PROPOSED until verified in `contracts/domains/people-dna-land/` and `schemas/contracts/v1/domains/people-dna-land/` *(PROPOSED paths per Directory Rules §3 / §12)*.

| Term | Definition (sublane-scoped) | Status |
|---|---|---|
| **Person Assertion** | A per-source claim that a person existed, bound to source role, evidence, valid time, and release state. Never a public truth claim by itself. | CONFIRMED term / PROPOSED field |
| **PersonCanonical** | An internal-only curated record built from one or more reconciled `Person Assertion`s and a `Person Identity Candidate` resolved by steward review. Never public by default. | CONFIRMED term / PROPOSED field |
| **NameAssertion** | A per-source name variant (formal, vernacular, alias, mis-transcription) attached to a `Person Assertion` over a temporal window. | CONFIRMED term / PROPOSED field |
| **Person Identity Candidate** | A scored, evidence-linked proposal that two or more `Person Assertion`s describe the same person. Promotion to `PersonCanonical` is a governed state transition. | CONFIRMED term / PROPOSED field |
| **LifeEvent** | A bounded life-stage event (birth, marriage, death, burial, naturalization, military service, etc.) anchored to a `Person Assertion`. | CONFIRMED term / PROPOSED field |
| **Residence Event** | A `Person Assertion`-anchored residence at a place over a valid-time interval. The place is a reference into the settlements lane, not duplicated here. | CONFIRMED term / PROPOSED field |
| **Migration Event** | A `Person Assertion`-anchored move between two places with directionality and uncertainty. | CONFIRMED term / PROPOSED field |
| **ConsentGrant** _(cross-sublane)_ | A holder-controlled, machine-readable consent record referenced from this sublane when a person assertion derives from a consent-bearing source. | CONFIRMED term / PROPOSED field |
| **RevocationReceipt** _(cross-sublane)_ | A signed record that supersedes a `ConsentGrant` and triggers downstream tombstone and cache-invalidation behavior. | CONFIRMED term / PROPOSED field |
| **EvidenceBundle** _(cross-domain)_ | The governed evidentiary container any `Person Assertion`-derived public output MUST resolve to before release. | CONFIRMED doctrine |
| **DecisionEnvelope** _(cross-domain)_ | The finite-outcome runtime envelope (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`) carrying every public response about a person. | CONFIRMED doctrine |

[Back to top](#-people-sublane)

---

## 7 · Object families

**Identity rule (PROPOSED, domain-uniform).** Deterministic ID basis = `source_id + object_role + temporal_scope + normalized_digest`. The identity scheme is the domain-level proposal for stable `spec_hash`-based identity; the people sublane inherits it. Algorithm freeze and resolution path are specified at the domain or schema layer (see open questions §16).

**Temporal handling (CONFIRMED, domain-uniform).** Source time, observed time, valid time, retrieval time, release time, and correction time are kept distinct where material. Conflating these collapses provenance. [DOM-PEOPLE §E]

These families are owned by the single `[DOM-PEOPLE]` bounded context; the table reflects the *proposed* people slice, not a doctrinal sub-partition (OQ-PEOPLE-SUB-02).

| Object | Purpose (sublane-scoped) | Temporal handling | Identity status |
|---|---|---|---|
| `Person Assertion` | Per-source claim of personhood and identifying attributes. | source · observed · valid · retrieval · release · correction | PROPOSED deterministic basis |
| `PersonCanonical` | Internal-only reconciled person record. | source · observed · valid · retrieval · release · correction | PROPOSED deterministic basis |
| `NameAssertion` | Per-source name variant over a window. | source · observed · valid · retrieval · release · correction | PROPOSED deterministic basis |
| `Person Identity Candidate` | Proposed identity link between assertions. | source · observed · valid · retrieval · release · correction | PROPOSED deterministic basis |
| `LifeEvent` | Birth, marriage, death, burial, etc. | source · observed · valid · retrieval · release · correction | PROPOSED deterministic basis |
| `Residence Event` | Residence over a valid-time interval. | source · observed · valid · retrieval · release · correction | PROPOSED deterministic basis |
| `Migration Event` | Movement between two places. | source · observed · valid · retrieval · release · correction | PROPOSED deterministic basis |

> [!TIP]
> **Three-layer separation is doctrine.** A `Person Assertion` is not the same thing as a published map feature labeled with a person's name. The corpus explicitly separates: (1) **canonical human assertions** — internal-only; (2) **evidence layer** — `EvidenceBundle`-backed; (3) **publication / experience layer** — derived, policy-filtered, downstream-only. The people sublane participates in layers (1) and (2). Layer (3) is reached only through governed APIs.

<details>
<summary><strong>Worked example — illustrative only</strong></summary>

The following is **illustrative**, not extracted from a mounted source. It shows the doctrinal shape, not a verified contract.

```text
# A census enumerator records "Jno Smith, age 34, farmer, b. Ohio" in 1880.

PersonAssertion#A     <- source=US1880 census schedule (authority/observed)
NameAssertion#A1      <- "Jno Smith" linked to PersonAssertion#A
LifeEvent#A-birth     <- inferred birth ~1846, place=OH, low precision
ResidenceEvent#A-1880 <- place_ref=settlements:KS-...  valid=[1880-06-01, 1880-06-01]

# A different source - a township tax roll for 1885 - records "John Smith".

PersonAssertion#B     <- source=KS1885 tax roll (authority/observed)
NameAssertion#B1      <- "John Smith"
ResidenceEvent#B-1885 <- place_ref=settlements:KS-...  valid=[1885-..., 1885-...]

# Identity resolution proposes a link.

PersonIdentityCandidate#1
  - links: PersonAssertion#A, PersonAssertion#B
  - confidence: 0.62  (NOT promoted)
  - evidence_refs: name match, county overlap, age plausibility
  - outstanding: requires steward review (ReviewRecord)

# Until reviewed, no PersonCanonical exists. No public output joins these two.
# The Evidence Drawer shows two separate assertions and the candidate edge.
```

</details>

[Back to top](#-people-sublane)

---

## 8 · Source families

Source families are the same set listed at the domain level; the people sublane uses the subset that produces person-shaped output. Each source MUST resolve to a `SourceDescriptor` with rights, sensitivity, citation, time, and hash before any work-state processing. [DOM-PEOPLE §D]

| Source family | Role(s) | Sensitivity default | Freshness |
|---|---|---|---|
| Vital / cemetery / burial / obituary / church / school / military / census / directory / court / probate records | `authority` · `observed` · `context` · `modeled` as source role requires | Living-person fields fail closed; sensitive joins fail closed | Source-vintage or cadence specific |
| GEDCOM / GEDZip / tree overlays | `modeled` · `candidate` (hypothesis) | Living-person fields fail closed; tree-asserted relationships are hypotheses, never authority | Source-vintage |

> [!WARNING]
> **Living-person screening is the gate, not the goal.** Source admission with a living-person flag does not by itself permit public output. The gate at PROCESSED / CATALOG / PUBLISHED enforces the actual policy decision; the source-level flag only routes the assertion into the correct policy path. Living-person fields default to tier **T4**; release to T1 requires aggregation (by tract or county) plus `AggregationReceipt` and `ReviewRecord` per Atlas §24.5.3.

[Back to top](#-people-sublane)

---

## 9 · Pipeline shape (RAW → PUBLISHED)

**CONFIRMED doctrine / PROPOSED lane application.** The People sublane follows the KFM lifecycle invariant: `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a **governed state transition, not a file move** *(Directory Rules §9 lifecycle invariant)*.

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash. | `SourceDescriptor` exists. | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, and policy; hold failures in quarantine. | Validation + policy gate pass, OR quarantine reason recorded. | PROPOSED |
| **PROCESSED** | Emit validated, normalized `Person Assertion`, `LifeEvent`, `Residence Event`, `Migration Event`, `NameAssertion` objects; emit `Person Identity Candidate`s; emit public-safe candidates with living-person and sensitivity transforms applied. | `EvidenceRef`, `ValidationReport`, and digest closure exist. | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`s, graph/triplet projections (with privacy controls), and release candidates. | Catalog / proof closure passes. | PROPOSED |
| **PUBLISHED** | Serve released public-safe artifacts through the governed API and release manifests. | `ReleaseManifest`, correction path, rollback target, and review/policy state (`ReviewRecord` where required) exist. | PROPOSED |

> [!IMPORTANT]
> **Public clients never read RAW, WORK, QUARANTINE, PROCESSED, or CATALOG stores directly.** The trust membrane is enforced by reading only through governed APIs. A worker, watcher, or connector that publishes directly to `data/published/` violates the invariant (watcher-as-non-publisher). [DIRRULES; ENCY]

[Back to top](#-people-sublane)

---

## 10 · Sensitivity, rights, and publication posture

**CONFIRMED doctrine / PROPOSED enforcement.**

- **Living-person fields fail closed by default.** No public output names, locates, or relates a living person without an authorized policy decision and a steward review (`ReviewRecord`). Default tier T4; T4→T1 path is aggregation + `AggregationReceipt` + `ReviewRecord` (Atlas §24.5.3).
- **Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion.** [ENCY; DIRRULES]
- **Sensitive joins fail closed.** Person↔parcel, person↔DNA, person↔archaeology-site, and person↔court-record joins are denied by default at the public surface unless a policy decision permits them at the requested specificity.
- **Tree assertions are hypotheses.** A `Person Assertion` derived from an uploaded GEDCOM is a `modeled`/`candidate` source and cannot be promoted to a public claim without authoritative corroboration.
- **Reidentification risk applies even to dead-person data.** Spatial precision, temporal precision, relationship density, and small-community exposure all factor into the publication decision. *(The precise scoring rule is PROPOSED and remains NEEDS VERIFICATION.)*

> [!CAUTION]
> **Names in tiles are not safe by default.** The corpus's standing rule for the publication / experience layer is: **do not embed** names, exact dates of birth, GEDCOM IDs, family IDs, DNA markers, or exact burial coordinates in public tiles or layer payloads. Use opaque pointers and server-side dereference under policy.

[Back to top](#-people-sublane)

---

## 11 · Governed AI behavior

**CONFIRMED doctrine / PROPOSED implementation.** [DOM-PEOPLE §L; GAI]

| AI action | Allowed? | Condition |
|---|---|---|
| Summarize a released `EvidenceBundle` that contains person-shaped assertions | ANSWER | Bundle is PUBLISHED; sensitivity is public; non-living-person scope. |
| Compare two `Person Assertion`s in released bundles | ANSWER | Both bundles are PUBLISHED and public. |
| Draft a steward-review note on a `Person Identity Candidate` | ANSWER | Internal surface only; not a public release. |
| Infer a relationship between two persons | ABSTAIN | Relationship modeling lives in the genealogy slice; AI MUST defer there and resolve through `EvidenceBundle`. |
| Output anything about a living person | DENY | Default-deny posture per §10. |
| Output anything DNA-derived | DENY | DNA-derived inference is denied at the public surface by default. |
| Synthesize a person-shaped claim with no evidence resolution | DENY / ABSTAIN | Cite-or-abstain is doctrine; ungrounded synthesis is not an allowed outcome. |

The finite outcome set is `ANSWER` / `ABSTAIN` / `DENY` / `ERROR`. Every Focus Mode answer emits an `AIReceipt`. AI is interpretive, not the root truth source. `EvidenceBundle` outranks generated language. [Atlas §24.2 AIReceipt]

[Back to top](#-people-sublane)

---

## 12 · Cross-sublane and cross-lane relations

**CONFIRMED / PROPOSED relations (per `[DOM-PEOPLE]` §F).** Each relation must preserve ownership, source role, sensitivity, and `EvidenceBundle` support.

| This sublane | Counterpart | Relation | Constraint |
|---|---|---|---|
| `people` | `genealogy` _(slice)_ | `PersonCanonical` / `Person Assertion` is the **subject** of `Genealogy Relationship` and `FamilyGroup`. | Identity edges resolved here; relationship edges resolved in genealogy. Bidirectional references only — never mutual writes. |
| `people` | `dna` _(slice)_ | `DNAMatchEvidence` MAY **corroborate** a `Person Identity Candidate` but MUST NOT mutate `PersonCanonical` directly. | Default-deny on DNA-derived person assertions. |
| `people` | `land` _(slice)_ | `Land Ownership Assertion` references `PersonCanonical`; person↔parcel joins gated by sensitivity policy. | Assessor / tax records are NOT title truth; parcel geometry is NOT title-boundary proof. |
| `people` | Settlements / Infrastructure | `Residence Event.place_ref` and `Migration Event.{from,to}_ref` reference settlement entities. | Living-person fields fail closed across the boundary. |
| `people` | Roads / Rail | `Migration Event` may reference a corridor or route for context. | Movement context only; never a privacy bypass. |
| `people` | Archaeology / Cultural Heritage | Cultural affiliations of named individuals are **steward-reviewed and rights-bounded**. | Indigenous community context cited under sovereignty rules. |
| `people` | Agriculture | `LandParcel` context may bound field-candidate joins; **private person-parcel joins denied by default**. | Producer-adjacent context with privacy. |
| `people` | Frontier Matrix | Aggregated population observations feed matrix cells. | Matrix cells are analytical releases with their own evidence and rollback; this sublane does not edit cells. |

[Back to top](#-people-sublane)

---

## 13 · API, contract, and schema surfaces

**PROPOSED governed API surface; exact route names UNKNOWN.** Schema responsibility root is `schemas/contracts/v1/domains/people-dna-land/` per Directory Rules §3 default and ADR-0001 (schema home). Contracts root is `contracts/domains/people-dna-land/`. Per §12, these are **whole-domain** lanes — they are **not** subdivided by sublane. *All paths PROPOSED until verified.*

| Surface | DTO / Schema | Outcomes | Status |
|---|---|---|---|
| People sublane feature / detail resolver _(route TBD)_ | `PeopleSublaneDecisionEnvelope` (composes the domain `PeopleDNALandDecisionEnvelope`) | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; exact route UNKNOWN |
| People sublane layer manifest resolver | `LayerManifest` / sublane layer descriptor | `ANSWER` / `DENY` / `ERROR` | PROPOSED; public-safe release only |
| People sublane Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; evidence- and policy-filtered |
| People sublane Focus Mode answer | `RuntimeResponseEnvelope` + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; AI never root truth |
| Schema home | `schemas/contracts/v1/domains/people-dna-land/` *(PROPOSED — whole-domain, not a people/ sub-segment)* | finite validator outcomes | PROPOSED; ADR-bound |
| Contract home | `contracts/domains/people-dna-land/` *(PROPOSED — whole-domain)* | semantic Markdown for object families | PROPOSED |
| Policy home | `policy/domains/people-dna-land/` *(PROPOSED — whole-domain)* | OPA / Rego admissibility rules | PROPOSED |

> [!NOTE]
> An earlier draft proposed `…/people-dna-land/people/` sub-segments. Per §12, responsibility-root
> artifacts use the whole `people-dna-land` slug and do not subdivide by sublane; a `people/`
> sub-segment presupposes the unresolved sublane convention. Use whole-domain lanes until the
> ADR settles it. [DIRRULES §12]

[Back to top](#-people-sublane)

---

## 14 · Validators, tests, fixtures

**All PROPOSED** *(per `[DOM-PEOPLE]` §K validators/tests/fixtures list, scoped to this sublane)*. Each test exists to prove that the default-deny posture and assertion-first model survive contact with the pipeline. Validator/fixture homes use the **whole-domain** `people-dna-land` segment per §12.

| Test / fixture | What it proves | Status |
|---|---|---|
| Person-assertion evidence test | A `Person Assertion` without a resolvable `EvidenceBundle` fails the publication gate. | PROPOSED |
| GEDCOM import rights / living-flag test | Tree imports carrying a living-person flag never produce public output; rights-missing trees route to QUARANTINE. | PROPOSED |
| Identity-candidate non-promotion test | A `Person Identity Candidate` with confidence below the steward threshold never auto-promotes to `PersonCanonical`. | PROPOSED |
| Name-variant collision test | Identical name variants across sources do **not** by themselves collapse into one person. | PROPOSED |
| Residence/migration place-ref integrity test | `Residence Event` / `Migration Event` references resolve to a settlements-lane entity at the requested temporal scope, or fail closed. | PROPOSED |
| Public-tile leakage fixture | No name, exact DOB, GEDCOM ID, family ID, DNA marker, or exact burial coordinate appears in a public tile or layer payload. | PROPOSED |
| Revocation cleanup test _(cross-sublane)_ | A `RevocationReceipt` against a consent-bearing source invalidates downstream public derivatives within the published cache TTL. | PROPOSED |
| Graph projection safety test | The sublane's contribution to the graph projection does not expose denied edges via inference. | PROPOSED |

> [!NOTE]
> Fixtures should include both **positive** paths (valid published `EvidenceBundle`-backed assertions) and **negative** paths (living-person export attempts, raw-GEDCOM leakage, revoked consent, missing retention, unresolved evidence). The corpus's standing recommendation is fixture-first development for sensitive sublanes.

[Back to top](#-people-sublane)

---

## 15 · Related docs

- [`../README.md`](../README.md) — People/DNA/Land domain README *(PROPOSED path)*
- [`./README.md`](./README.md) — sublanes index *(PROPOSED layer)*
- `sublanes/genealogy(.md|/README.md)` — Genealogy sublane *(PROPOSED; filename per OQ-PEOPLE-SUB-13)*
- `sublanes/dna(.md|/README.md)` — DNA sublane *(PROPOSED)*
- `sublanes/land(.md)` — Land sublane *(PROPOSED)*
- [`directory-rules.md`](../../../../directory-rules.md) — Directory Rules (placement law §3, §12, §2.5, §18 OPEN-DR-02)
- [`ai-build-operating-contract.md`](../../../../ai-build-operating-contract.md) — operating law (`CONTRACT_VERSION = "3.0.0"`)
- [`docs/standards/PROV.md`](../../../standards/PROV.md) — provenance crosswalk
- `docs/registers/VERIFICATION_BACKLOG.md` · `docs/registers/DRIFT_REGISTER.md` — open items + drift (PROPOSED paths)
- _TODO: link to the `sublanes/` ADR (OQ-PEOPLE-SUB-01/02/13) once authored._
- _TODO: link to the People/DNA/Land schema-home ADR once authored._

[Back to top](#-people-sublane)

---

## 16 · Open questions & verification backlog

| ID | Item | Evidence that would settle it | Status |
|---|---|---|---|
| OQ-PEOPLE-SUB-01 | Does the repo use `docs/domains/people-dna-land/sublanes/` or a flat `docs/domains/people-dna-land/people.md` layout? | Mounted repo state; ADR amending Directory Rules §12. | NEEDS VERIFICATION |
| OQ-PEOPLE-SUB-02 | Is `people` a standalone sublane, and how many sublanes total (does `genealogy` fold in)? | ADR fixing sublane count and names. | CONFLICTED |
| OQ-PEOPLE-SUB-13 | Flat `people.md` vs subfolder `people/README.md` filename form across all sublanes. | Same `sublanes/` ADR. | CONFLICTED |
| OQ-PEOPLE-03 | Where do `contracts/`, `schemas/`, `policy/`, `tests/`, `fixtures/` for this domain live (whole-domain vs any sub-segment)? | Mounted repo; ADR-0001 (schema home). | NEEDS VERIFICATION |
| OQ-PEOPLE-04 | Exact governed-API route for the people feature/detail resolver. | Mounted `apps/governed-api/` routes; OpenAPI; service tests. | UNKNOWN |
| OQ-PEOPLE-05 | Steward-review threshold for promoting a `Person Identity Candidate` to `PersonCanonical`. | Policy doc or ADR; review console; CI fixtures. | NEEDS VERIFICATION |
| OQ-PEOPLE-06 | Precise reidentification-risk scoring rule (uniqueness · spatial · temporal · relationship density · small-community). | Domain policy doc; rego rules; fixtures. | NEEDS VERIFICATION |
| OQ-PEOPLE-07 | Public cache TTL for revocation-driven invalidation. | Release-manifest doc; revocation runbook; cache config. | NEEDS VERIFICATION |
| OQ-PEOPLE-08 | Confirm `ReviewRecord` is the cross-cutting receipt (Atlas §24.2) referenced here, not a sublane-owned object. | Receipt schema home (`schemas/contracts/v1/receipts/`); domain README. | NEEDS VERIFICATION |
| OQ-PEOPLE-09 | How are `RevocationReceipt`-driven tombstones materialized for `PersonCanonical` records from consent-bearing sources? | Tombstone schema; cleanup test; pipeline receipt envelope. | NEEDS VERIFICATION |
| OQ-PEOPLE-10 | Living-person determination — steward-set, age-rule-driven, or source-flag-driven? | Sensitivity policy; living-person screen tests. | NEEDS VERIFICATION |
| OQ-PEOPLE-11 | Is `PersonCanonical` ever exposed externally, even in aggregated form? | Policy decisions; release manifests; tile/layer audit. | NEEDS VERIFICATION |

> [!NOTE]
> All open questions will be filed to `docs/registers/VERIFICATION_BACKLOG.md` when this doc is published; the CONFLICTED rows additionally go to `docs/registers/DRIFT_REGISTER.md`. *(PROPOSED. [DIRRULES §2.5])*

---

### External sources

None consulted for this document. All claims derive from project knowledge (KFM Domains Atlas v1.1, Directory Rules, Unified Implementation Architecture Build Manual, Pass-10 Idea Index, and the People/DNA/Land sections of the Atlas and Encyclopedia).

---

**Last updated:** 2026-06-06 · **Doc id:** `kfm://doc/people-dna-land/sublanes/people` · **Status:** `draft` · `CONTRACT_VERSION = "3.0.0"` · [Back to top](#-people-sublane)
