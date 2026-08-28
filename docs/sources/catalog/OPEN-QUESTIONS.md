<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-open-questions
title: Source catalog open questions
type: register
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward · Source steward · Lane stewards>
created: 2026-05-20
updated: 2026-05-23
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/INDEX.md
  - docs/sources/catalog/NAMING.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/CROSSWALKS.md
  - docs/sources/catalog/CARE-COMPLIANCE.md
  - docs/sources/catalog/COVERAGE-MATRIX.md
  - docs/sources/catalog/GLOSSARY.md
  - docs/doctrine/directory-rules.md
  - docs/registers/DRIFT_REGISTER.md
tags: [kfm, docs, sources, catalog, register, open-questions]
notes:
  - "v0.2 — full presentation-standard pass; this register is established as the canonical numbering authority for OPEN-DSC-* identifiers in this lane."
  - "v0.2 promotes OPEN-DSC-NEW to OPEN-DSC-15 with a proper identifier."
  - "v0.2 surfaces a numbering collision: concurrent v0.2 revisions of sibling docs (IDENTITY.md, INDEX.md, NAMING.md) in this session introduced new OPEN-DSC-NN identifiers (13..25) that collide with this register's existing numbering. Reconciliation table provided in §Numbering reconciliation; sibling docs require a follow-up renumbering pass."
  - "v0.2 flags ADR-0010 (cited in OPEN-DSC-12) as NEEDS VERIFICATION — not located in the doctrine corpus this session; canonical ADR ledger uses ADR-0001 (confirmed) plus the doctrine synthesis ADR-S-NN backlog (ADR-S-01..15). Reconcile against the active ADR ledger."
  - "PROPOSED scaffold; sibling-link presence verified in a prior Claude Code session, not in this session."
[/KFM_META_BLOCK_V2] -->

# Source catalog open questions

> Canonical numbered register of unresolved questions (`OPEN-DSC-*`) for the source-catalog documentation lane.

![status](https://img.shields.io/badge/status-draft%20·%20canonical%20register-yellow)
![type](https://img.shields.io/badge/type-register-blueviolet)
![open%20questions](https://img.shields.io/badge/open%20questions-15-1f6feb)
![partially%20resolved](https://img.shields.io/badge/partially%20resolved-3-green)
![numbering%20collisions](https://img.shields.io/badge/numbering%20collisions-13-red)
![reviewed](https://img.shields.io/badge/last%20reviewed-2026--05--23-green)

**Status:** scaffold (PROPOSED) · **Type:** register *(canonical numbering authority for `OPEN-DSC-*`)* · **Last reviewed:** 2026-05-23

---

## Quick jump

- [Purpose](#purpose)
- [Authority pointer](#authority-pointer)
- [Numbering reconciliation (CRITICAL)](#numbering-reconciliation-critical)
- [Status vocabulary](#status-vocabulary)
- [Register (OPEN-DSC-01..15)](#register-open-dsc-0115)
- [Cross-reference to ADR-S-NN doctrine backlog](#cross-reference-to-adr-s-nn-doctrine-backlog)
- [Maintenance rules](#maintenance-rules)
- [Related docs](#related-docs)

---

## Purpose

This register is the **canonical numbering authority** for `OPEN-DSC-*` identifiers in the `docs/sources/catalog/` lane.

> **What `OPEN-DSC-*` numbers exist? What does each one mean? What is its current status? What is the path to resolution?**

> [!IMPORTANT]
> Sibling docs in this lane (`IDENTITY.md`, `INDEX.md`, `NAMING.md`, `CROSSWALKS.md`, `CARE-COMPLIANCE.md`, `COVERAGE-MATRIX.md`, `GLOSSARY.md`) **MUST NOT** allocate new `OPEN-DSC-NN` identifiers without first checking this register. The numbering authority lives here; allocation drift is itself a drift signal *(per `directory-rules.md` §2.5)*. The Numbering reconciliation section below documents a collision that occurred in this session and proposes the fix.

Entries `OPEN-DSC-01` through `OPEN-DSC-08` are carried forward from [`README.md`](./README.md) §19. Entries `OPEN-DSC-09` through `OPEN-DSC-14` were added in the 2026-05-20 reorganization and the 2026-05-21 connector-derived family scaffold. `OPEN-DSC-15` is the former `OPEN-DSC-NEW` from v0.1, now properly numbered.

[Back to top](#quick-jump)

---

## Authority pointer

| Concern | Where authority lives | Status |
|---|---|---|
| `OPEN-DSC-*` numbering authority (this lane) | This register | **CONFIRMED — canonical** *(v0.2)* |
| Lane-wide `OPEN-DR-*` numbering | [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) §18 | **CONFIRMED root** |
| Cross-lane `ADR-S-NN` doctrine backlog | KFM Domains Atlas v1.1 §24.12 *(15 ADR-S items)*; KFM Unified Doctrine Synthesis §49 | **CONFIRMED reference** |
| Active ADR ledger | [`docs/adr/`](../../adr/) | **CONFIRMED root** *(only ADR-0001 confirmed in corpus this session)* |
| Drift register | [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) | **CONFIRMED root** *(directory-rules.md §2.5)* |
| Verification backlog | [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) | **CONFIRMED root** *(per directory-rules.md §18 OPEN-DR-04 resolution-path pattern)* |

> [!CAUTION]
> ADR-0010 is referenced in `OPEN-DSC-12` (carried from v0.1). The specific identifier `ADR-0010` was **not located** in the doctrine corpus this session. Only `ADR-0001` is confirmed in this session. The doctrine synthesis ADR backlog uses `ADR-S-NN` identifiers (ADR-S-01..15). Reconcile this reference against the active ADR ledger; if no `ADR-0010` exists, replace with the corresponding `ADR-S-NN` entry or assign a new ADR number. Flagged as `OPEN-DSC-12-NV`.

[Back to top](#quick-jump)

---

## Numbering reconciliation (CRITICAL)

> [!CAUTION]
> **A numbering collision occurred in this session.** Concurrent v0.2 revisions of sibling docs (`IDENTITY.md`, `INDEX.md`, `NAMING.md`) introduced **new `OPEN-DSC-NN` identifiers (13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25) that collide with this register's existing numbering** (OPEN-DSC-13 and OPEN-DSC-14 are already assigned to different questions in this canonical register, and OPEN-DSC-15 is the promotion of OPEN-DSC-NEW). Per `directory-rules.md` §2.5: surfaced, not smoothed.

### Resolution

This register **holds the canonical numbering**. The sibling docs MUST renumber their newly-introduced entries to start at the next free identifier after this register's current allocation. The proposed renumbering table below preserves the **semantics** of each sibling-doc question while assigning a non-colliding identifier.

| Originally introduced in | Sibling-doc identifier (collision) | Semantics (PRESERVED) | **Proposed canonical identifier** | Reconciliation action |
|---|---|---|---|---|
| IDENTITY.md v0.2 | OPEN-DSC-13 *(new in v0.2)* | Collection-id versioning policy *(Pass-10 C4-02)* | **OPEN-DSC-16** | Renumber in IDENTITY.md v0.3 |
| IDENTITY.md v0.2 | OPEN-DSC-14 *(new in v0.2)* | Item-id formula ADR | **OPEN-DSC-17** | Renumber in IDENTITY.md v0.3 |
| IDENTITY.md v0.2 | OPEN-DSC-15 *(new in v0.2)* | Canonical run-receipt schema *(Pass-10 C1-01)* | **OPEN-DSC-18** | Renumber in IDENTITY.md v0.3 |
| IDENTITY.md v0.2 | OPEN-DSC-16 *(new in v0.2)* | Per-family `promoteId` resolution | **OPEN-DSC-19** | Renumber in IDENTITY.md v0.3 |
| IDENTITY.md v0.2 | OPEN-DSC-17 *(new in v0.2)* | ADR identifier ledger reconciliation | **OPEN-DSC-20** | Renumber in IDENTITY.md v0.3 |
| IDENTITY.md v0.2 | OPEN-DSC-18 *(new in v0.2)* | `kfm:promotion_state` Collection-summary field *(Pass-10 C4-02 Open Question)* | **OPEN-DSC-21** *(also duplicates this register's OPEN-DSC-04 — fold into OPEN-DSC-04 rather than allocating new)* | Fold into OPEN-DSC-04; remove from IDENTITY.md |
| INDEX.md v0.2 | OPEN-DSC-19 *(new in v0.2)* | Product-page count automation | **OPEN-DSC-22** | Renumber in INDEX.md v0.3 |
| INDEX.md v0.2 | OPEN-DSC-20 *(new in v0.2)* | Per-family page layout convention | **OPEN-DSC-23** *(intersects this register's OPEN-DSC-02; consider folding)* | Cross-reference OPEN-DSC-02; renumber if kept distinct |
| INDEX.md v0.2 | OPEN-DSC-21 *(new in v0.2)* | Connector-lane mirror | **OPEN-DSC-24** | Renumber in INDEX.md v0.3 |
| NAMING.md v0.2 | OPEN-DSC-22 *(new in v0.2)* | Filename-pattern linter (enforcement) | **OPEN-DSC-25** | Renumber in NAMING.md v0.3 |
| NAMING.md v0.2 | OPEN-DSC-23 *(new in v0.2)* | UPPERCASE_WITH_UNDERSCORES alternative for lane-root docs | **OPEN-DSC-26** | Renumber in NAMING.md v0.3 |
| NAMING.md v0.2 | OPEN-DSC-24 *(new in v0.2)* | Hidden-support folder convention codification | **OPEN-DSC-27** | Renumber in NAMING.md v0.3 |
| NAMING.md v0.2 | OPEN-DSC-25 *(new in v0.2)* | Product slug source (canonical slug ↔ filename) | **OPEN-DSC-28** | Renumber in NAMING.md v0.3 |

> [!NOTE]
> The reconciliation is **NEEDS ACTION**, not yet executed. Two further actions follow from this:
> - **DRIFT-OQ-01** entry to be opened in [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) documenting the numbering collision and the v0.3 renumbering sweep.
> - A future `v0.3` of this register absorbs OPEN-DSC-16..28 as proper entries with full text, after the sibling docs renumber.

### Numbering rule going forward

| Rule | Statement |
|---|---|
| Allocation authority | All new `OPEN-DSC-NN` identifiers MUST be allocated **here first** (this register), then referenced from sibling docs by ID. |
| Conflict detection | A v0.x of any sibling doc introducing a new `OPEN-DSC-NN` identifier MUST cite this register's current high-water mark (currently **OPEN-DSC-15**) and propose its new entries as **OPEN-DSC-16, 17, …** in numeric order. |
| Drift surfacing | If a collision is discovered (as in this session), open a `DRIFT-OQ-NN` entry in the drift register, propose a renumbering table in this register's next version, and execute the renumbering across all affected sibling docs in coordinated PRs. |
| Promotion of `OPEN-DSC-NEW` style placeholders | Placeholder identifiers (`OPEN-DSC-NEW`, `OPEN-DSC-TBD`) MUST be promoted to a proper number within one version of this register. |

[Back to top](#quick-jump)

---

## Status vocabulary

Each entry carries one **Status** value drawn from this vocabulary.

| Status | Meaning |
|---|---|
| `OPEN` | Question is unresolved; resolution path is identified but not yet executed. |
| `PROPOSED` | A provisional resolution is documented elsewhere (e.g., in a sibling register); ratification by per-root note, Docs steward decision, or ADR is still pending. |
| `PARTIALLY RESOLVED` | Some subset of the question has been answered (often by a maintainer decision or prior-session work); remainder requires further action. |
| `NEEDS VERIFICATION` | An identifier or claim references material that should exist but has not been confirmed against the mounted repo or the active ADR ledger in this session. |
| `DEFERRED` | Question is acknowledged and deliberately postponed pending a doctrinal precondition (typically an ADR or a populated companion folder in `connectors/` or `data/registry/sources/`). |
| `UNKNOWN` | Even the resolution path is unclear; doctrine-level guidance is needed. |
| `RESOLVED` | Closed; the resolution is in effect. Resolved entries remain in this register for traceability and are flagged with the resolving ADR / per-root note / commit. |

[Back to top](#quick-jump)

---

## Register (OPEN-DSC-01..15)

### OPEN-DSC-01 — lane existence

**Question:** Should `docs/sources/catalog/` exist as a docs subfolder, or should source-catalog narrative live in `docs/sources/<family>/` directly with no intermediate `catalog/` segment?
**Status:** `PROPOSED`
**Resolution path:** Per-root note in `docs/sources/README.md`, or ADR.
**Notes:** No corpus reference contradicts the current `docs/sources/catalog/` layout this session.

### OPEN-DSC-02 — per-family page layout

**Question:** Does the per-family page list live in this lane or in `docs/sources/README.md` as a flat index? The flat-vs-nested split observed earlier (flat `<family>.md` pages vs. `README.md` §8's nested folders) has been acted on.
**Status:** `PARTIALLY RESOLVED`
**Resolution path:** ADR ratifying the realized folder layout.
**Notes:** On 2026-05-20 the lane was reorganized into per-family folders (maintainer decision), implementing `README.md` §8. An ADR should still ratify the realized folder layout and settle the `docs/sources/README.md`-index vs. lane-index question. **Intersects:** the proposed OPEN-DSC-23 *(per-family page layout convention)* from `INDEX.md` v0.2 — consider folding the two.

### OPEN-DSC-03 — provenance namespace

**Question:** Is the KFM provenance namespace prefix `kfm:` (KFM-global) or `ks-kfm:` (Kansas-scoped)?
**Status:** `UNKNOWN`
**Resolution path:** ADR pinning the namespace.
**Notes:** Pass-10 C4-01 explicitly flags this as an unresolved Open Question. Affects `kfm:provenance`, `kfm:care`, Evidence-Bundle JSON-LD interior fields, all product pages. Sweeping change. **Cross-cutting** — referenced from `IDENTITY.md`, `GLOSSARY.md`, `CROSSWALKS.md`, `CARE-COMPLIANCE.md`.

### OPEN-DSC-04 — promotion-state summary field

**Question:** Should STAC Collections carry a `kfm:promotion_state` summary field summarizing the highest zone any Item in the Collection has reached?
**Status:** `PROPOSED`
**Resolution path:** ADR, plus schema change in `schemas/contracts/v1/source/`.
**Notes:** Pass-10 C4-02 Open Question. **Folds:** the proposed OPEN-DSC-21 *(kfm:promotion_state)* from `IDENTITY.md` v0.2 — fold into this entry; no separate identifier needed.

### OPEN-DSC-05 — STAC vs DCAT disposition

**Question:** Canonical disposition between STAC and DCAT for spatiotemporal datasets that could go either way (Pass-10 C4-05). Related: does each product warrant its own STAC Collection or share one with sibling products?
**Status:** `NEEDS VERIFICATION`
**Resolution path:** Profile decision in [`PROFILES.md`](./PROFILES.md), plus verification against `data/catalog/`.
**Notes:** Pass-10 C4-02 Tensions section ("Per-domain Collection conventions" unresolved). **Cross-cutting** — referenced from `IDENTITY.md`, `CROSSWALKS.md`.

### OPEN-DSC-06 — `kfm:care` registry home + crosswalks placement

**Question:** Should `kfm:care` be proposed upstream to the STAC-extensions registry or kept KFM-local (Pass-10 C15-02)? Related: the canonical home for authored crosswalks — `docs/sources/catalog/CROSSWALKS.md` vs. `docs/standards/`.
**Status:** `UNKNOWN`
**Resolution path:** ADR.
**Notes:** `directory-rules.md` §6.1.a points at `docs/standards/` for "external standards profiles that KFM conforms to or crosswalks against" — strong but not conclusive signal toward placing authored crosswalks there. Candidate resolution: authored crosswalks live as subsidiary files under same-named standards folders *(e.g., `docs/standards/STAC/crosswalk-dcat.md`)*; this register stays in the catalog lane.

### OPEN-DSC-07 — filename casing

**Question:** Filename casing for per-family pages and lane-root docs — hyphens vs. underscores. See `directory-rules.md` §18 **OPEN-DR-04**.
**Status:** `PROPOSED` *(provisionally resolved in [`NAMING.md`](./NAMING.md) v0.2)*
**Resolution path:** Per-root note ratifying `NAMING.md` *(acceptable per OPEN-DR-04: "Resolution by per-root README in `docs/standards/README.md` is acceptable")*, or one-line ADR.
**Notes:** `NAMING.md` v0.2 documents the four PROPOSED conventions: family folders snake_case; product pages kebab-case; lane-root UPPERCASE-WITH-HYPHENS; hidden `_underscore-prefix/`. Ratification is a Docs steward decision.

### OPEN-DSC-08 — repository implementation maturity

**Question:** Repository implementation maturity for everything described in this lane.
**Status:** `PARTIALLY RESOLVED`
**Resolution path:** Ongoing verification as products materialize.
**Notes:** A mounted repo was inspected in a Claude Code session on 2026-05-20; all sibling roots checked in §7.3 scope (`connectors/`, `data/catalog/`, `data/registry/sources/`, `schemas/`, `policy/`, `contracts/`, `pipelines/`, `docs/adr/`) were CONFIRMED-PRESENT at that time. Per-product implementation maturity remains `NEEDS VERIFICATION`. **No mounted-repo evidence in this session (2026-05-23).**

### OPEN-DSC-09 — candidate families: federal agencies (first wave)

**Question:** Should NASA, USDA, EPA, DOT, and BLM be promoted to `directory-rules.md` §7.3 families with full connector and registry treatment?
**Status:** `DEFERRED`
**Resolution path:** ADR per family, gated on a `connectors/<family>/` plus `data/registry/sources/<family>/` companion.
**Notes:** Folders `blm/`, `epa/` were created in the 2026-05-20 reorganization ahead of ADR; folder existence does **not** constitute §7.3 promotion. Corpus-support evidence for NASA, EPA (Atmosphere dossier `[DOM-AIR]`) and possibly USDA (Soil dossier `[DOM-SOIL]` via NRCS) — see `INDEX.md` Group A annotations.

### OPEN-DSC-10 — candidate families: archival and genealogy

**Question:** Should the Library of Congress (LOC), FamilySearch, AHGP, and Newspapers be promoted to §7.3 families?
**Status:** `DEFERRED`
**Resolution path:** ADR per family; genealogy and archival sources additionally gated on CARE and sensitivity review.
**Notes:** Folders `loc/`, `familysearch/`, `ahgp/`, `newspapers/` were created in the 2026-05-20 reorganization ahead of ADR. Corpus support: FamilySearch (Pass-10 C9-02 — CONFIRMED OAuth2-gated genealogy upstream); LOC (Pass-10 C7 authority cluster — LCNAF). AHGP acronym expansion **NEEDS VERIFICATION**.

### OPEN-DSC-11 — candidate families: citizen-science and sensors

**Question:** Should PurpleAir, eBird, and EDDMapS be promoted to §7.3 families?
**Status:** `DEFERRED`
**Resolution path:** ADR per family; eBird and EDDMapS additionally gated on sensitive-species redaction policy.
**Notes:** Folders `ebird/`, `eddmaps/` were created in the 2026-05-20 reorganization ahead of ADR. eBird and EDDMapS both touch the sensitive-occurrence lane (Fauna `[DOM-FAUNA]` / Flora `[DOM-FLORA]`); their admission MUST traverse CARE / sensitivity review before reaching §7.3.

### OPEN-DSC-12 — candidate families: biodiversity collections and genomic

**Question:** Should iDigBio/Symbiota, NatureServe/USFWS, and direct-to-consumer (DTC) genomic sources be promoted to §7.3 families?
**Status:** `DEFERRED`
**Resolution path:** ADR per family; genomic and rare-species sources gated deny-by-default per **ADR-0010** *(`NEEDS VERIFICATION` — see OPEN-DSC-12-NV)*.
**Notes:** Folders `idigbio/`, `natureserve/`, `usfws_ecos/`, `ftdna/` were created in the 2026-05-20 reorganization ahead of ADR. Corpus support: iDigBio (Pass-10 C4-03 — CONFIRMED named biodiversity consumer alongside GBIF, Symbiota); DTC genomic (Pass-10 C9-03 — CONFIRMED, names 23andMe / Ancestry / MyHeritage / FamilyTreeDNA with strict consent and redaction).

**OPEN-DSC-12-NV** *(child)* — **ADR-0010 verification.** The specific identifier `ADR-0010` cited as the deny-by-default authority for genomic and rare-species sources was **not located** in the doctrine corpus this session. Only `ADR-0001` is confirmed; the doctrine synthesis ADR backlog uses `ADR-S-NN` identifiers (likely `ADR-S-05` sensitivity tier scheme). Reconcile against the active ADR ledger. **Status:** `NEEDS VERIFICATION`. **Resolution path:** ADR-ledger lookup; if absent, replace reference with the corresponding `ADR-S-NN` or assign a new ADR number.

### OPEN-DSC-13 — folders without a clear family classification

**Question:** `openstreetmap/` and `manual_curation/` received folders in the 2026-05-20 reorganization but do not map cleanly to a source family — OpenStreetMap is a base-map source and Manual Curation describes a process rather than a source.
**Status:** `OPEN`
**Resolution path:** Maintainer decision, then ADR, relocation, or reclassification.
**Notes:** `manual_curation` overlaps with the §7.3 family `local_upload` — both lanes appear to cover operator-curated content. Distinction unclear; one may need to fold into the other. See `INDEX.md` v0.2 DRIFT-IDX-03.

### OPEN-DSC-14 — connector-derived families (second wave)

**Question:** Should NASA, USDA, USDOT, OpenAQ, HIFLD, ISRIC, the U.S. Drought Monitor, and LANDFIRE be promoted to `directory-rules.md` §7.3 families?
**Status:** `DEFERRED`
**Resolution path:** ADR per family, gated on a populated `connectors/<family>/` plus `data/registry/sources/<family>/` companion.
**Notes:** Folders `nasa/`, `usda/`, `usdot/`, `openaq/`, `hifld/`, `isric/`, `drought_monitor/`, `landfire/` were scaffolded on 2026-05-21 from the `connectors/` inventory ahead of ADR; folder existence does **not** constitute §7.3 promotion. Product descriptions are grounded in `docs/domains/*/SOURCE_REGISTRY.md` because the connector folders are empty stubs. Corpus support varies — see `INDEX.md` Group A annotations.

### OPEN-DSC-15 — §15 README-contract field-order deviation

> *(Formerly `OPEN-DSC-NEW` in v0.1; promoted to proper number in v0.2.)*

**Question:** The `_template/SOURCE_FAMILY_TEMPLATE.md` scaffold inserts a `## Directory tree` section between `## Outputs` and `## Validation`, deviating from the §15 README-contract field order in `directory-rules.md`.
**Status:** `PROPOSED`
**Resolution path:** ADR to either (a) ratify the deviation lane-wide, or (b) relocate the directory-tree section to the lane-root `INDEX.md`.
**Notes:** Flagged by the original 2026-05-20 scaffold PR. Pending ADR, both placements are observable in active drafts.

[Back to top](#quick-jump)

---

## Cross-reference to ADR-S-NN doctrine backlog

The KFM Domains Atlas v1.1 §24.12 and KFM Unified Doctrine Synthesis §49 maintain a broader **Master Open-ADR Backlog** with 15 `ADR-S-NN` entries. Where `OPEN-DSC-*` questions correspond to backlog items, the table below records the mapping. ADR-S entries without a clear OPEN-DSC counterpart are not listed here.

| OPEN-DSC | Closest ADR-S backlog item | Why related |
|---|---|---|
| **OPEN-DSC-03** *(namespace pin)* | Not directly in ADR-S backlog | Pass-10 C4-01 Open Question; no doctrine-synthesis ADR-S entry located this session. |
| **OPEN-DSC-04** *(kfm:promotion_state field)* | `ADR-S-03` *(Receipt schema layout)* — **PARTIAL match** | Schema-change rule applies. |
| **OPEN-DSC-06** *(kfm:care registry home; crosswalks placement)* | `ADR-S-05` *(Sensitivity tier scheme)* — **partial overlap** | CARE intersects sensitivity tiers. |
| **OPEN-DSC-07** *(filename casing)* | `directory-rules.md` §18 **OPEN-DR-04** — primary anchor; no ADR-S entry | Per-root README resolution acceptable. |
| **OPEN-DSC-09..12, 14** *(candidate-family promotions)* | `ADR-S-04` *(Source-role vocabulary)* — partial; new families need source-role admission | Source-role rules govern admission. |
| **OPEN-DSC-12-NV** *(ADR-0010 verification)* | `ADR-S-05` *(Sensitivity tier scheme)* — likely correspondence | Deny-by-default for genomic and rare-species is sensitivity-tier governance. |
| **OPEN-DSC-15** *(template field-order)* | Not in ADR-S backlog | Lane-local; not doctrine-class. |

> [!NOTE]
> The corpus's `ADR-S-NN` backlog is **doctrine-class** (Atlas v1.1 §24.12); the `OPEN-DSC-*` register here is **lane-class**. A lane question may map to a doctrine question (mostly via partial overlap), but they are not the same register. Reconciling across both is part of the active ADR ledger's job.

[Back to top](#quick-jump)

---

## Maintenance rules

> [!IMPORTANT]
> Docs are part of the working system. This register MUST update when questions are introduced, when status changes, or when reconciliation occurs.

| Trigger | Action |
|---|---|
| **New `OPEN-DSC-NN` identifier needed** *(in any lane doc)* | Allocate the next free number **here first**, then reference it from the sibling doc. Update the badge count. |
| **Status change** *(OPEN → PARTIALLY RESOLVED, PROPOSED → RESOLVED, etc.)* | Update the entry's Status line; add a Notes addendum citing the resolving ADR / per-root note / commit / Docs steward decision. |
| **Identifier collision detected** *(as in this session)* | Open a `DRIFT-OQ-NN` entry in the drift register; propose a renumbering table in this register; execute coordinated PRs to renumber. |
| **ADR resolves an OPEN-DSC entry** | Flip status to `RESOLVED`; preserve the entry; cite the resolving ADR. |
| **Placeholder identifier promoted** *(e.g., `OPEN-DSC-NEW` → `OPEN-DSC-NN`)* | Bump version; record the promotion in the meta block notes. |
| **Cross-cutting question identified** *(affects multiple lanes)* | Note "Cross-cutting" in the entry; ensure mapping to ADR-S backlog if applicable. |

**Versioning.** KFM Meta Block v2 semver-lite: `v0.x` while the register has open identifier collisions or unresolved `NEEDS VERIFICATION` items; `v1.x` once collisions are reconciled and the ADR ledger is stable.

[Back to top](#quick-jump)

---

## Related docs

- [`docs/sources/catalog/README.md`](./README.md) — lane root *(§19 origin of `OPEN-DSC-01..08`)*
- [`docs/sources/catalog/INDEX.md`](./INDEX.md) — family index *(introduced OPEN-DSC-19..21 collision; reconciliation in §Numbering reconciliation)*
- [`docs/sources/catalog/IDENTITY.md`](./IDENTITY.md) — identity and namespace conventions *(introduced OPEN-DSC-13..18 collision; reconciliation in §Numbering reconciliation; references OPEN-DSC-03)*
- [`docs/sources/catalog/NAMING.md`](./NAMING.md) — naming conventions *(provisional resolution of OPEN-DSC-07; introduced OPEN-DSC-22..25 collision)*
- [`docs/sources/catalog/CROSSWALKS.md`](./CROSSWALKS.md) — crosswalks register *(references OPEN-DSC-03, OPEN-DSC-05, OPEN-DSC-06)*
- [`docs/sources/catalog/CARE-COMPLIANCE.md`](./CARE-COMPLIANCE.md) — CARE compliance *(references OPEN-DSC-03; intersects OPEN-DSC-06)*
- [`docs/sources/catalog/COVERAGE-MATRIX.md`](./COVERAGE-MATRIX.md) — coverage matrix
- [`docs/sources/catalog/GLOSSARY.md`](./GLOSSARY.md) — glossary
- [`docs/sources/catalog/PROFILES.md`](./PROFILES.md) — profiles *(PROPOSED — referenced from OPEN-DSC-05)*
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority *(§18 OPEN-DR-04 parallel anchor for OPEN-DSC-07; §2.4 ADR-required changes; §2.5 do not silently conform)*
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — drift entries *(DRIFT-OQ-01 to open for numbering-collision reconciliation; DRIFT-IDX-01..03 from INDEX.md)*
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) — verification backlog
- [`docs/adr/`](../../adr/) — active ADR ledger *(needed to resolve OPEN-DSC-12-NV)*

---

*Doc status: **draft · canonical register (v0.2)** · Last reviewed: **2026-05-23** · Provenance: revised against `directory-rules.md` §18 OPEN-DR-04, Atlas v1.1 §24.12 Master Open-ADR Backlog, KFM Unified Doctrine Synthesis §49, Pass-10 C4-01 / C4-02 / C4-03 / C4-05 / C9-02 / C9-03 / C15-02; numbering collision surfaced from concurrent in-session v0.2 revisions of IDENTITY.md / INDEX.md / NAMING.md.*

[↑ Back to top](#source-catalog-open-questions)
