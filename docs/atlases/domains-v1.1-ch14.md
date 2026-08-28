<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: KFM Domains v1.1 — Ch. 14 Settlements / Infrastructure
type: standard
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/atlases/domains-v1.1.md
  - docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md
  - docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md
  - docs/atlases/receipt-catalog.md
  - docs/atlases/pipeline-gate-reference.md
  - docs/doctrine/directory-rules.md
tags: [kfm, atlas, domain, settlements, infrastructure, ch14, doctrine, carrier]
notes:
  - Per-domain carrier for Atlas v1.0 Ch. 14 (Settlements / Infrastructure); the first per-chapter dossier carrier in the series.
  - Filename uses a new chapter-number-based pattern (domains-v1.1-ch14.md); the prior carrier domains-v1.1.md §12.1 proposed a kebab-domain-name pattern (settlements-infrastructure.md). The convention fork is surfaced in §16.
  - A-N template reproduced verbatim from the atlas; per-object sensitivity and §24.4.12 cross-lane edges supplied from Atlas Ch. 24.
  - Owners, doc_id, schema/policy home presence remain placeholders.
[/KFM_META_BLOCK_V2] -->

# KFM Domains v1.1 — Ch. 14 Settlements / Infrastructure

> **A per-chapter dossier carrier for Atlas v1.0 Ch. 14 — settlements, municipalities, census places, historic townsites, ghost towns, forts, missions, reservation communities, infrastructure assets, networks, facilities, service areas, operators, condition observations, dependencies, and public-safe representations.**
> Authority lives in Atlas v1.0 Ch. 14; this file routes readers into it.

<p align="center">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Authority: carrier" src="https://img.shields.io/badge/authority-carrier--only-lightgrey">
  <img alt="Doctrine anchor: Atlas v1.0 Ch. 14" src="https://img.shields.io/badge/anchor-Atlas%20v1.0%20Ch.%2014-success">
  <img alt="Dossier: DOM-SETTLE" src="https://img.shields.io/badge/dossier-%5BDOM--SETTLE%5D-informational">
  <img alt="Object families: 16" src="https://img.shields.io/badge/object%20families-16-blueviolet">
  <img alt="Source families: 8" src="https://img.shields.io/badge/source%20families-8-informational">
  <img alt="Critical-asset deny lane" src="https://img.shields.io/badge/critical%20asset-DENY%20default-critical">
</p>

**Quick jump:** [Purpose](#1-purpose-and-role) · [A. Identity](#a-domain-identity-and-one-line-purpose) · [B. Scope](#b-scope-boundary-and-explicit-non-ownership) · [C. Language](#c-ubiquitous-language) · [D. Sources](#d-key-source-families) · [E. Objects](#e-main-object-families) · [F. Cross-lane](#f-cross-lane-relations) · [G. Viewing](#g-map-and-viewing-products) · [H. Pipeline](#h-pipeline-shape-raw--published) · [I. Sensitivity](#i-sensitivity-rights-and-publication-posture) · [J. API/Schema](#j-api-contract-and-schema-surfaces) · [K. Validators](#k-validators-tests-fixtures) · [L. Governed AI](#l-governed-ai-behavior-for-this-domain) · [M. Publication](#m-publication-correction-rollback) · [N. Verification](#n-verification-backlog-and-open-questions) · [Naming](#16-naming-convention-fork-conflicted)

> [!IMPORTANT]
> **Status:** `PROPOSED file` / `CONFIRMED doctrine` (Atlas v1.0 Ch. 14 A–N blocks) / `UNKNOWN repo implementation depth`
> **Owner:** `OWNER_TBD`
> **Proposed path:** `docs/atlases/domains-v1.1-ch14.md`
> **Filename pattern:** **chapter-number-based** (`ch14`) — diverges from the kebab-domain-name pattern proposed in `domains-v1.1.md` §12.1 (`settlements-infrastructure.md`). See §16.
> **Lane choice:** `docs/atlases/` over `docs/atlas/` — `CONFIRMED at doctrine level` per `directory-rules.md` v1.2 §6.1.
> **Truth posture:** *Atlas v1.0 Ch. 14 is doctrine.* This file is a carrier. EvidenceBundle and `[DOM-SETTLE]` dossier remain authoritative. Where this carrier paraphrases the chapter, **the chapter wins on wording**.

> [!NOTE]
> **Evidence boundary.** All A–N block content is **`CONFIRMED doctrine`** from Atlas v1.0 Ch. 14 and reproduced verbatim or near-verbatim. The per-stage `Status` in block H is `PROPOSED` in the Atlas itself. The §24.4.12 cross-lane edges owned by Settlements/Infrastructure (§F supplement), the §24.13 responsibility-root crosswalk (§14), and the §24.14 per-object sensitivity defaults (§15) are `CONFIRMED doctrine / PROPOSED supplement` per Atlas v1.1. **Repo implementation depth — `schemas/contracts/v1/settlement/`, `contracts/settlement/`, `policy/sensitivity/infrastructure/`, validators, CI gates, runtime emission paths — remains `UNKNOWN`.**

---

## 1. Purpose and role

This file is the **per-chapter dossier carrier** for Settlements / Infrastructure. It exists because:

- The previous-level carrier (`docs/atlases/domains-v1.1.md`) covers all 16 domain chapters at a single granularity. Maintainers working **on settlements/infrastructure specifically** — adding a new ghost-town record, ingesting Census TIGER, drafting a critical-infrastructure deny policy — need a focused entry that reproduces the A–N template inline.
- The Settlements/Infrastructure domain carries one of KFM's three operational "deny lanes" (critical-asset detail; the other two are Archaeology site coords and People/DNA/Land living-person fields). Surfacing this discipline at the per-domain level matters.
- The §24.1.2 anti-collapse register flags **Settlements** specifically under *"administrative compilation cited as observation"* — a domain-specific failure mode worth pinning at the per-domain level (see §15.2 of this carrier).

**This file is not authority.** Two non-collapse rules apply:

1. **Atlas Ch. 14 wins on wording.** Where this carrier paraphrases the chapter, the chapter is authoritative.
2. **`[DOM-SETTLE]` dossier is the underlying source.** Per Atlas v1.1 non-collapse rule: *"Registers and master atlases are navigational aids. EvidenceBundle and the governing dossiers remain authoritative."*

---

## A. Domain identity and one-line purpose

> **Source:** Atlas v1.0 §14.A (p. 90). `CONFIRMED doctrine / PROPOSED implementation`.

> Govern settlements, municipalities, census places, historic townsites, ghost towns, forts, missions, reservation communities, infrastructure assets, networks, facilities, service areas, operators, condition observations, dependencies, and public-safe representations. `[DOM-SETTLE] [ENCY]`

---

## B. Scope, boundary, and explicit non-ownership

> **Source:** Atlas v1.0 §14.B (p. 90). `CONFIRMED / PROPOSED`.

### B.1 This domain owns

| Object family | Atlas citation |
|---|---|
| Settlement | `[DOM-SETTLE] [ENCY]` |
| Municipality | `[DOM-SETTLE] [ENCY]` |
| CensusPlace | `[DOM-SETTLE] [ENCY]` |
| Townsite | `[DOM-SETTLE] [ENCY]` |
| GhostTown | `[DOM-SETTLE] [ENCY]` |
| Fort | `[DOM-SETTLE] [ENCY]` |
| Mission | `[DOM-SETTLE] [ENCY]` |
| ReservationCommunity | `[DOM-SETTLE] [ENCY]` |
| Infrastructure Asset | `[DOM-SETTLE] [ENCY]` |
| Network Node | `[DOM-SETTLE] [ENCY]` |
| Network Segment | `[DOM-SETTLE] [ENCY]` |
| Facility | `[DOM-SETTLE] [ENCY]` |
| Service Area | `[DOM-SETTLE] [ENCY]` |
| Operator | `[DOM-SETTLE] [ENCY]` |
| Condition Observation | `[DOM-SETTLE] [ENCY]` |
| Dependency | `[DOM-SETTLE] [ENCY]` |

### B.2 This domain explicitly does NOT own

| Boundary | What it means |
|---|---|
| **Roads/Rail** owns transport routes. | Settlement/Infrastructure may cite road/rail facilities (bridges, depots, crossings) but does not own the route. See `[DOM-ROADS]`. |
| **Hydrology** owns water evidence. | Stormwater, wastewater, drainage, floodplain context is consumed from Hydrology, never recreated. See `[DOM-HYD]`. |
| **Hazards** owns hazard events and warnings. | Critical-infrastructure resilience and exposure cite Hazards; **Settlements never asserts hazard authority**. See `[DOM-HAZ]`. |
| **People/Land** owns ownership and living-person privacy. | Settlement membership may cite residence; **living-person fields fail closed**; private parcel joins deny by default. See `[DOM-PEOPLE]`. |

---

## C. Ubiquitous language

> **Source:** Atlas v1.0 §14.C (pp. 90–91). All 12 terms `CONFIRMED term / PROPOSED field realization`.

> *Atlas template note: each term is "used inside this domain with meaning constrained by source role, evidence, time, and release state."*

| Term | Domain role |
|---|---|
| **Settlement** | Generic settled place; superset over Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity. |
| **Municipality** | Legal/administrative incorporation; carries an issuing authority. |
| **CensusPlace** | Census-defined statistical entity; not necessarily legal. |
| **Townsite** | Planned/platted townsite; historic or modern; may or may not have become a municipality. |
| **GhostTown** | Settlement no longer extant; historical evidence only; status carries explicit dissolution time. |
| **Fort** | Military/protective installation; usually historical; subject to archaeological + steward review. |
| **Mission** | Religious/cultural installation; historical context; often paired with archaeological sensitivity. |
| **ReservationCommunity** | Sovereign Indigenous community; **steward review and rights/sovereignty constraints apply**. |
| **Infrastructure Asset** | Built physical asset (pipe, line, tower, plant); **critical detail T4 default**. |
| **Network Node** | Topological junction in an infrastructure network. |
| **Network Segment** | Topological edge in an infrastructure network. |
| **Facility** | Operational asset class (water plant, substation, depot); operator-sensitive details default to restricted. |

> Each term's *"meaning constrained by source role, evidence, time, and release state"* clause is the per-term anti-collapse hook: a `Municipality` admitted as an `administrative` compilation cannot be downstream-cited as an `observed` event timeline. See §15.2.

---

## D. Key source families

> **Source:** Atlas v1.0 §14.D (p. 91). 8 source families, all carrying `authority / observation / context / model as source role requires`; rights/sensitivity `NEEDS VERIFICATION`; freshness `source-vintage or cadence specific`.

| # | Source family | Typical role(s) | Constraint |
|---|---|---|---|
| 1 | **Census TIGER / census place geography** | authority / observation / context | Rights and current terms `NEEDS VERIFICATION`; sensitive joins **fail closed**. |
| 2 | **GNIS and gazetteers** | authority / context | Same. |
| 3 | **state/local GIS / Kansas Geoportal-style sources** | authority / observation / context | Same. |
| 4 | **municipal and local legal records** | authority (legal/administrative) | Same. |
| 5 | **historical gazetteers and maps** | observation / context | Historical-source caveats; vintage-specific. |
| 6 | **infrastructure operators and providers** | observation / authority (operator) | Operator-sensitive details **default restricted**. |
| 7 | **KDOT / bridge / facility sources** | authority / observation | Crossing/bridge admissions cite Roads/Rail. |
| 8 | **FEMA / hazards / resilience sources** | observation / context | Hazards-owned; settlement cites resilience context, never asserts hazard authority. |

> **Source-role anti-collapse note** (Atlas §24.1): the role of a source is set at admission via `SourceDescriptor.source_role` and is preserved through every promotion. Promotion never upgrades `administrative` → `observed` or `regulatory` → `observed`. See §15.2.

---

## E. Main object families

> **Source:** Atlas v1.0 §14.E (pp. 92–93). All rows `CONFIRMED object-family spine / PROPOSED implementation`.
> Identity rule across the spine: *"PROPOSED deterministic basis: source id + object role + temporal scope + normalized digest."*
> Temporal handling across the spine: *"CONFIRMED source, observed, valid, retrieval, release, and correction times stay distinct where material."*

| # | Object | Purpose |
|---|---|---|
| 1 | **Settlement** | Generic settled-place evidence or released derivative. |
| 2 | **Municipality** | Legal/administrative incorporation record. |
| 3 | **CensusPlace** | Census-defined statistical place. |
| 4 | **Townsite** | Planned/platted townsite. |
| 5 | **GhostTown** | Settlement no longer extant. |
| 6 | **Fort** | Military/protective installation evidence. |
| 7 | **Mission** | Religious/cultural installation evidence. |
| 8 | **ReservationCommunity** | Sovereign Indigenous community record (sovereignty rules apply). |
| 9 | **Infrastructure Asset** | Built physical asset (T4 default for critical detail). |
| 10 | **Network Node** | Topological junction. |
| 11 | **Network Segment** | Topological edge. |
| 12 | **Facility** | Operational asset class. |
| 13 | **Service Area** | Aggregate coverage polygon. |
| 14 | **Operator** | Operating party identity (operator-sensitive). |
| 15 | **Condition Observation** | Observed asset condition with `observed_at` discipline. |
| 16 | **Dependency** | Inter-asset / inter-system dependency edge (sensitive). |

> Per Atlas §24.14, **`Infrastructure Asset (critical)`** carries `T4 default for critical detail`; `T1 for generalized footprint`. **`Settlement / Municipality / GhostTown`** carry `T0` baseline. See §15 of this carrier.

---

## F. Cross-lane relations

> **Source:** Atlas v1.0 §14.F (p. 94). 4 edges; all carry the standard constraint *"relation must preserve ownership, source role, sensitivity, and EvidenceBundle support."*

| This domain | Related lane | Relation type |
|---|---|---|
| Settlements/Infrastructure | **Roads/Rail** | depot, bridge, crossing, transport facility relation. |
| Settlements/Infrastructure | **Hazards** | exposure, resilience, warnings, declarations. |
| Settlements/Infrastructure | **Hydrology** | water, wastewater, stormwater, floodplain, drainage. |
| Settlements/Infrastructure | **People/Land** | residence, ownership, parcel, migration context with restrictions. |

### F.1 Settlements as a relation owner (Atlas §24.4.12)

> Atlas v1.1 §24.4.12 catalogs the edges where Settlements/Infrastructure is the **owning** lane. Reproduced verbatim:

| Edge owner | Consumes from owner | Relation (`CONFIRMED doctrine`) |
|---|---|---|
| Settlements / Infrastructure | **People/Land** | Settlement identity (Township, GhostTown, Townsite, Reservation Community) bounds residence and ownership context. |
| Settlements / Infrastructure | **Frontier Matrix** | Settlement status feeds settlement cells in the matrix. |
| Settlements / Infrastructure | **Hazards** | Critical-infrastructure exposure context with **default deny on public detail**. |

---

## G. Map and viewing products

> **Source:** Atlas v1.0 §14.G (p. 94). Domain viewing products `PROPOSED`; cross-cutting viewing products `CONFIRMED doctrine`.

### G.1 Domain viewing products (`PROPOSED`)

- Current settlement view
- Historic townsite view
- Legal-status-event view
- Census-place comparison
- Public-safe asset view
- Service-area aggregate view
- Dependency-summary view
- **Restricted internal review view** *(non-public; for stewards)*

### G.2 Cross-cutting viewing products (`CONFIRMED doctrine`)

Per Atlas's standard cross-cutting block (identical across all 16 domain chapters; full text in `docs/atlases/maplibre-master.md`):

> *Evidence Drawer · time-aware state · trust badges · sensitivity-redacted view · correction/stale-state view · governed Focus Mode.* `[MAP-MASTER] [GAI]`

---

## H. Pipeline shape (RAW → PUBLISHED)

> **Source:** Atlas v1.0 §14.H (pp. 94–95). `CONFIRMED doctrine / PROPOSED lane application`; the lifecycle invariant `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` is universal across all 16 domains.

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash. | `SourceDescriptor` exists. | `PROPOSED` |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, and policy; hold failures. | Validation and policy gate pass, or quarantine reason is recorded. | `PROPOSED` |
| **PROCESSED** | Emit validated normalized objects, receipts, and public-safe candidates. | `EvidenceRef`, `ValidationReport`, and digest closure exist. | `PROPOSED` |
| **CATALOG / TRIPLET** | Emit catalog records, EvidenceBundles, graph/triplet projections, and release candidates. | Catalog/proof closure passes. | `PROPOSED` |
| **PUBLISHED** | Serve released public-safe artifacts through governed APIs and manifests. | `ReleaseManifest`, correction path, rollback target, and review/policy state exist. | `PROPOSED` |

> **Universal gate detail:** lifecycle gates (Admission, Normalization, Validation, Catalog closure, Release, Correction, Rollback), required artifacts, closure rules, and reason codes are consolidated in **`docs/atlases/pipeline-gate-reference.md`** (Atlas v1.1 §24.6). The per-stage **`PROPOSED`** status above reflects the Atlas's own implementation-status posture for this domain.

---

## I. Sensitivity, rights, and publication posture

> **Source:** Atlas v1.0 §14.I (p. 95). `CONFIRMED / PROPOSED`.

> Critical infrastructure, utilities, condition observations, dependencies, operator-sensitive details, and exact facility geometry **default to restricted or review**. `[DOM-SETTLE] [ENCY]`

> [!CAUTION]
> **Deny-by-default promotion gate** *(Atlas universal callout, reproduced)*:
> *Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks public promotion**.* `[ENCY] [DIRRULES]`

### I.1 Per-object sensitivity defaults

> **Source:** Atlas v1.1 §24.14 (Object Family × Domain Reference Matrix). `PROPOSED supplement`.

| Object family | Default tier | Notes |
|---|---|---|
| `Settlement` / `Municipality` / `GhostTown` | **T0** | Public open release. |
| `CensusPlace`, `Townsite`, `Fort`, `Mission` | **T0** | Public open release; historical context. |
| `ReservationCommunity` | **T0** but with sovereignty-review path | Cultural review may restrict release of associated detail. |
| `Infrastructure Asset (critical)` | **T4 default** for critical detail; **T1** for generalized footprint | The Atlas §24.13 "critical-asset deny lane." |
| `Facility` | T0 mostly; **T2 / T4** for sensitive condition / operator detail | Per §24.14. |
| `Network Node` / `Network Segment` | T0 generalized; **T4** for restricted topology | Critical-system topology restricted. |
| `Service Area` | T0 aggregate | Aggregation receipts apply. |
| `Operator` | T1 / T2 / T4 | Operator-sensitive detail restricted. |
| `Condition Observation` | T2 / T4 | Per-asset condition is typically operator-restricted. |
| `Dependency` | **T4 default** | Inter-system dependencies are sensitive. |

> Cross-references: `RedactionReceipt`, `AggregationReceipt`, and `PolicyDecision` (the receipts that govern tier transforms) are documented in **`docs/atlases/receipt-catalog.md`** §3.

---

## J. API, contract, and schema surfaces

> **Source:** Atlas v1.0 §14.J (p. 95). `PROPOSED governed API surface; exact routes UNKNOWN`.

| Endpoint or artifact | DTO / schema | Outcomes | Status |
|---|---|---|---|
| Settlements/Infrastructure feature/detail resolver; **route TBD** | `SettlementsInfrastructureDecisionEnvelope` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | `PROPOSED governed API surface; exact route UNKNOWN`. |
| Settlements/Infrastructure layer manifest resolver | `LayerManifest` / domain layer descriptor | `ANSWER` / `DENY` / `ERROR` | `PROPOSED`; **public-safe release only**. |
| Settlements/Infrastructure Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | `PROPOSED`; evidence and policy filtered. |
| Settlements/Infrastructure Focus Mode answer | Runtime Response Envelope + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | `PROPOSED`; **AI never root truth**. |
| Schema responsibility root | `schemas/contracts/v1/` *(see §14 below for full crosswalk)* | finite validator outcomes | `PROPOSED`; verify with Directory Rules and ADR. |

> **Finite outcome envelope** for every surface: per `kfm_unified_doctrine_synthesis.md` §11, every governed gate returns from the small set `{ANSWER, ABSTAIN, DENY, ERROR, ALLOW, HOLD, PASS, FAIL}`. AI surfaces specifically return `ANSWER / ABSTAIN / DENY / ERROR` and never bypass cite-or-abstain.

---

## K. Validators, tests, fixtures

> **Source:** Atlas v1.0 §14.K (p. 95). All `PROPOSED`.

- `PROPOSED`: **Legal municipality evidence tests** — Municipality is admitted with verifiable issuing authority.
- `PROPOSED`: **census-vs-municipality distinction** — CensusPlace and Municipality are not interchangeable; admission preserves both.
- `PROPOSED`: **infrastructure topology tests** — Network Node + Network Segment topology is structurally valid.
- `PROPOSED`: **condition `observed_at` tests** — Condition Observation carries valid temporal scope.
- `PROPOSED`: **restricted geometry no-leak tests** — critical-asset exact geometry never reaches public layers.
- `PROPOSED`: **catalog/proof/release closure tests** — every PUBLISHED settlement carries `CatalogMatrix` + `EvidenceBundle` + `ReleaseManifest` + rollback target.

> Each test should pair with **deterministic fixtures** per the Atlas §24.6 closure rule that *"validators are deterministic and tied to fixtures."*

---

## L. Governed AI behavior for this domain

> **Source:** Atlas v1.0 §14.L (p. 96). `CONFIRMED doctrine / PROPOSED implementation`.

> AI may **summarize** released Settlements/Infrastructure EvidenceBundles, **compare** evidence, **explain limitations**, and **draft steward-review notes**.
> AI **must `ABSTAIN`** when evidence is insufficient.
> AI **must `DENY`** where policy, rights, sensitivity, or release state blocks the request. `[GAI] [DOM-SETTLE] [ENCY]`

Settlements/Infrastructure has specific cite-or-abstain hot spots:

| Scenario | Required posture |
|---|---|
| AI asked about a critical-infrastructure asset's exact location, condition, or dependency. | **`DENY`** with reason code (per Atlas §24.6.3: `SENSITIVITY_UNRESOLVED` or policy-decision-blocked). |
| AI asked about a ghost town's history with only candidate evidence in `WORK`. | **`ABSTAIN`** until `EvidenceBundle` resolves; never paraphrase unverified material. |
| AI asked to compare two municipalities' historical timelines using administrative compilations. | **`ANSWER` only with explicit source-role labeling** (administrative ≠ observed); see §15.2 anti-collapse. |
| AI asked about a reservation community's cultural detail. | **`ABSTAIN` or `DENY`** unless steward review and sovereignty rules permit. |

---

## M. Publication, correction, rollback

> **Source:** Atlas v1.0 §14.M (p. 96). `CONFIRMED doctrine / PROPOSED implementation`.

Settlements/Infrastructure publication requires:

1. **`ReleaseManifest`** — bound layers, styles, tile artifacts, proof pack.
2. **`EvidenceBundle`** — resolved evidence for every claim in the release.
3. **Validation/policy support** — `ValidationReport` + `PolicyDecision` for the gate.
4. **`ReviewRecord` where required** — sensitive lanes (critical infrastructure, operator-sensitive) require steward sign-off.
5. **Correction path** — `CorrectionNotice` lineage discipline (Atlas Appendix E).
6. **Stale-state rule** — public surfaces transition through `stale` / `superseded` / `withdrawn` per Atlas §24.8, never silently edited.
7. **Rollback target** — `RollbackCard` pointing to a valid prior release.

> See **`docs/atlases/pipeline-gate-reference.md`** §3 for the Release gate's universal artifact list; **`docs/atlases/receipt-catalog.md`** §3 for `ReleaseManifest`, `CorrectionNotice`, and `RollbackCard` field shapes.

---

## N. Verification backlog and open questions

> **Source:** Atlas v1.0 §14.N (p. 96). All `NEEDS VERIFICATION`.

| Item to verify | Evidence that would settle it |
|---|---|
| Verify **source rights and municipal legal-source roles**. | Mounted repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests. |
| Verify **critical infrastructure policy**. | Same. |
| Verify **public-safe layer registry**. | Same. |
| Verify **API and Focus Mode auth/policy behavior**. | Same. |

---

## 13. Anti-collapse posture for Settlements

> **Source:** Atlas v1.1 §24.1.2 (Anti-collapse failure modes — DENY conditions). `CONFIRMED doctrine`.

Settlements is one of three domains flagged for the *"administrative compilation cited as observation"* failure mode (the others are People/Land and Roads).

| Collapse pattern | Denied outcome | Required guardrail |
|---|---|---|
| **Administrative compilation cited as observation.** Example: a 1880 county incorporation record is queried as if it timestamped an observed event. | `DENY publication of compilation as observed event timeline.` | Source-role tag preserved; named `LifeEvent` / `AdminEvent` types; cite-or-abstain at AI. |

**Mitigation in this domain:**

- Every `Municipality` admission carries `source_role = administrative` with `role_authority = <issuing body>` (§D.2 verbatim).
- Every `Condition Observation` carries `source_role = observed` distinct from administrative roster admission.
- `Settlement` may carry mixed admission lineage (administrative incorporation + observed condition observations) — the per-record evidence trail must preserve both, never collapse them.

---

## 14. Responsibility root

> **Source:** Atlas v1.1 §24.13 (Atlas Section ↔ Dossier ↔ Responsibility Root Crosswalk), Ch. 14 row. `CONFIRMED doctrine; paths PROPOSED until mounted-repo verification`.

| Atlas Ch. | Domain | Source dossier | Primary responsibility root (`PROPOSED`) | Notes |
|---|---|---|---|---|
| **14** | Settlements / Infrastructure | `[DOM-SETTLE]` | `schemas/contracts/v1/settlement/` · `contracts/settlement/` · `policy/sensitivity/infrastructure/` | **"Critical-asset deny lane."** |

### 14.1 Expected lane pattern (`PROPOSED`)

Per `directory-rules.md` §12 (Domain Placement Law), the Settlements/Infrastructure domain follows the uniform lane pattern:

```text
docs/domains/settlements-infrastructure/
contracts/domains/settlements-infrastructure/
schemas/contracts/v1/settlement/         # short-name per §24.13
schemas/contracts/v1/domains/settlements-infrastructure/   # alternate per §12 lane pattern
policy/sensitivity/infrastructure/        # per §24.13
policy/domains/settlements-infrastructure/
tests/domains/settlements-infrastructure/
fixtures/domains/settlements-infrastructure/
packages/domains/settlements-infrastructure/
pipelines/domains/settlements-infrastructure/
pipeline_specs/settlements-infrastructure/
data/raw/settlements-infrastructure/
data/work/settlements-infrastructure/
data/quarantine/settlements-infrastructure/
data/processed/settlements-infrastructure/
data/catalog/domain/settlements-infrastructure/
data/published/layers/settlements-infrastructure/
data/registry/sources/settlements-infrastructure/
release/candidates/settlements-infrastructure/
```

> [!WARNING]
> **`CONFLICTED`** — short-name vs. lane-pattern conflict. Atlas §24.13 uses **`schemas/contracts/v1/settlement/`** (singular, short-name). `directory-rules.md` §12 lane pattern uses **`schemas/contracts/v1/domains/<domain>/`**. The two are not equivalent. Reconciliation is `NEEDS VERIFICATION` — likely belongs in ADR-S-01 (Schema home) or a successor.

---

## 15. Sensitivity defaults for Settlements objects

> **Source:** Atlas v1.1 §24.14 (Object Family × Domain Reference Matrix). See also §I.1 above for the per-object table.

### 15.1 Atlas §24.14 highlights for Settlements

| Object family | Owner (`CONFIRMED doctrine`) | Citing domains | Sensitivity default (`PROPOSED`) |
|---|---|---|---|
| `Settlement` / `Municipality` / `GhostTown` | Settlements | People/Land; Frontier Matrix; Archaeology. | T0 |
| `Infrastructure Asset (critical)` | Settlements/Infrastructure | Hazards (with restriction). | **T4 default** for critical detail; T1 for generalized footprint. |

### 15.2 Companion non-collapse rule

The §24.4.12 edge *"Critical-infrastructure exposure context with default deny on public detail"* (see §F.1 of this carrier) is the operational expression of the T4 default. **Hazards consumes** infrastructure-exposure context **from** Settlements; the relation **does not authorize public release of critical detail** by either lane.

---

## 16. Naming-convention fork (`CONFLICTED`)

> [!WARNING]
> **`CONFLICTED`** — this file establishes a new per-chapter naming pattern (`domains-v1.1-ch14.md`) that diverges from the kebab-domain-name pattern proposed in `docs/atlases/domains-v1.1.md` §12.1 (`settlements-infrastructure.md`). Reconciliation is `NEEDS VERIFICATION` and belongs in the proposed atlas-Markdown naming ADR (top-level carrier §11).

| Pattern | Example | Pros | Cons |
|---|---|---|---|
| **Chapter-number-based** *(this file)* | `domains-v1.1-ch14.md` | Atlas-chapter pinning is unambiguous; tolerates domain renames; chains cleanly from `domains-v1.1.md`. | Reader must know Ch. 14 = Settlements/Infrastructure (resolvable via `domains-v1.1.md` §3 chapter table). |
| **Kebab-domain-name** *(prior proposal)* | `settlements-infrastructure.md` | Self-describing; consistent with other carriers (`receipt-catalog.md`, `pipeline-gate-reference.md`, `maplibre-master.md`). | Sensitive to chapter renumbering and domain renames; requires a naming choice per domain (settlements? settlements-infrastructure? infrastructure?). |
| **Hybrid** | `domains-v1.1-ch14-settlements-infrastructure.md` | Self-describing **and** chapter-pinned. | Long; mixes conventions. |

> **Recommended resolution direction:** the atlas-Markdown naming ADR (proposed in top-level carrier §11) should decide between **chapter-number** and **kebab-domain-name** (or hybrid) and apply consistently across all 16 per-domain carriers. **This file does not make that decision.**

---

## 17. Companion carriers

| Carrier | Scope | Relationship |
|---|---|---|
| `docs/atlases/domains-v1.1.md` | All 16 domain chapters at single granularity. | **Parent carrier.** |
| `docs/atlases/kfm-domains-v1.1-pass23-32-consolidated-atlas.md` | Top-level navigation across v1.0 + v1.1 + Pass 23/32 + v1.3 overlay. | Grandparent carrier. |
| `docs/atlases/Kansas_Frontier_Matrix_-_Domains_v1_1___Pass_23_32_Consolidated_Atlas.md` | Full-text Markdown conversion. | **Authoritative on wording.** |
| `docs/atlases/receipt-catalog.md` | Atlas §24.2 (Receipt classes consumed by Settlements operations). | Cross-domain reference. |
| `docs/atlases/pipeline-gate-reference.md` | Atlas §24.6 (Gates that govern Settlements release). | Cross-domain reference. |
| `docs/atlases/maplibre-master.md` | MapLibre renderer surface (Settlements consumes for `LayerManifest`, `StyleManifest`). | Cross-domain reference. |

### 17.1 Sibling per-chapter carriers (none authored)

If the per-chapter naming pattern is adopted (§16), the sibling carriers would be: `domains-v1.1-ch3.md` (Spatial Foundation) through `domains-v1.1-ch18.md` (Planetary/3D). None are authored yet.

---

## 18. Cross-references

| Reference | Role | Status |
|---|---|---|
| **Atlas v1.0 Ch. 14 §§ A–N (pp. 90–96)** | **Primary doctrinal anchor for every block of this carrier.** | `CONFIRMED doctrine` |
| Atlas v1.1 §24.1 (Source-Role Anti-Collapse Register), §24.1.2 (anti-collapse failure modes) | §13 administrative-compilation anti-collapse. | `CONFIRMED doctrine` |
| Atlas v1.1 §24.4.12 (Edges owned by Settlements / Infrastructure) | §F.1 supplement. | `CONFIRMED doctrine` |
| Atlas v1.1 §24.13 (Crosswalk, Ch. 14 row) | §14 responsibility root. | `CONFIRMED doctrine; paths PROPOSED` |
| Atlas v1.1 §24.14 (Object Family × Domain Matrix) | §I.1 and §15 sensitivity defaults. | `CONFIRMED doctrine; defaults PROPOSED` |
| `[DOM-SETTLE]` dossier — *KFM Settlements, Cities, and Infrastructure Plan* | Underlying source dossier for the chapter. | `CONFIRMED corpus presence` |
| `KFM_Encyclopedia.md` Ch. 7 / domain expansion | Cross-corroborates dossier tag mapping. | `CONFIRMED corpus presence` |
| `directory-rules.md` §5 (responsibility roots) + §12 (Domain Placement Law) | §14.1 lane pattern. | `CONFIRMED at commit b6a279…` |
| `kfm_full_atlas_seed_cards.md` — `Settlement and Infrastructure Evidence Lane Implementation Surface` | Implementation-surface card for this domain. | `CONFIRMED corpus presence` (card is `PROPOSED implementation`) |
| `docs/atlases/domains-v1.1.md` §3 Ch. 14 row | Parent-carrier domain-table entry. | `PROPOSED file` |

---

## 19. ADR backlog

> Atlas §24.12 Open-ADR Backlog. Filtered for ADRs that materially touch this domain.

| ADR-S | Title (`PROPOSED`) | Touched by this carrier |
|---|---|---|
| **S-01** | Confirm/amend ADR-0001 (schema home `schemas/contracts/v1/<…>`). | §14 (`schemas/contracts/v1/settlement/` vs. lane pattern); §16 (CONFLICTED). |
| **S-04** | Source-role enum — canonical vocabulary, evolution rule. | §D, §13 (administrative source role discipline). |
| **S-05** | Sensitivity tier scheme T0–T4. | §I.1, §15. |
| **S-09** | Reviewer separation-of-duties threshold. | §M (Release with `ReviewRecord` for sensitive lanes). |
| **S-10** | Stale-state propagation. | §M (stale-state rule). |
| **S-12** | Connector cadence and quarantine recovery. | §D (8 source families). |
| **S-14** | Cross-lane join policy. | §F, §F.1. |
| **S-15** | Doctrine artifact lifecycle. | §16 (per-chapter carrier naming). |
| **(new, proposed)** | Atlas-Markdown naming convention under `docs/atlases/` — including the per-chapter-vs-kebab-domain fork. | §16. |

---

## 20. Verification checklist

- [ ] Confirm the target path `docs/atlases/domains-v1.1-ch14.md` does not already exist; resolve `docs/atlas/` mirror collisions.
- [ ] **Naming reconciliation (§16)**: open the atlas-Markdown naming ADR; pick chapter-number-based, kebab-domain-name, or hybrid; apply consistently across all 16 per-domain carriers.
- [ ] Confirm `OWNER_TBD` — docs steward + `[DOM-SETTLE]` dossier owner.
- [ ] Confirm `doc_id` allocation convention; do not invent UUIDs.
- [ ] Confirm every A–N block in this carrier matches Atlas v1.0 §14 verbatim or near-verbatim; flag any wording drift.
- [ ] Confirm §F cross-lane edge list matches Atlas §14.F and §24.4.12 together.
- [ ] Confirm §I.1 per-object sensitivity defaults match Atlas §24.14 row-by-row.
- [ ] Confirm §14 responsibility-root paths match Atlas §24.13 row 14 verbatim.
- [ ] **Resolve §14.1 short-name vs. lane-pattern `CONFLICTED`** (`schemas/contracts/v1/settlement/` vs. `schemas/contracts/v1/domains/settlements-infrastructure/`) via ADR-S-01 or successor.
- [ ] Confirm `policy/sensitivity/infrastructure/` exists or is tracked.
- [ ] Confirm critical-asset detail (`Infrastructure Asset`, `Dependency`, `Operator`, `Condition Observation`) is gated at admission and at every gate per §24.6.
- [ ] Confirm `Municipality` admission carries `source_role = administrative` per §13 anti-collapse posture.
- [ ] Confirm `Settlement` ↔ `Frontier Matrix` cell-feed edge (§F.1) does not bypass aggregation/cell-receipt discipline.
- [ ] Confirm AI surface (§L) returns `DENY` for critical-infrastructure detail queries with reason code per Atlas §24.6.3.
- [ ] Run `Diagram syntactic check`: no Mermaid block in this carrier; no check needed.

---

## 21. Rollback / supersession

| Condition | Action |
|---|---|
| Atlas v1.2 (or successor) amends Ch. 14 | Update A–N blocks in lock-step; preserve v1.1 row content as lineage; bump file `version`. |
| Atlas §24.4.12 edges amend Settlements ownership | Update §F.1 verbatim. |
| Atlas §24.13 amends responsibility root | Update §14 verbatim; preserve old paths as lineage. |
| Atlas §24.14 amends Settlements sensitivity defaults | Update §I.1 and §15 verbatim. |
| ADR resolves §14.1 short-name vs. lane-pattern `CONFLICTED` | Demote one path home to `SUPERSEDED`; record drift if both persist. |
| ADR resolves §16 naming-convention fork | Apply chosen convention; rename file if needed; preserve old name as compatibility alias for 30 days per `directory-rules.md` §8.3; record migration. |
| `[DOM-SETTLE]` dossier amends source families or object families | Re-author §D and §E from new dossier text; the dossier wins over this carrier. |
| `directory-rules.md` amends §12 Domain Placement Law | Update §14.1 lane pattern. |
| `KFM-P2-FEAT-0012` or related cards reclassify infrastructure handling | Update §I.1 and §L accordingly. |
| Hazards revises its alert-authority boundary | **Cannot happen via Settlements lane.** Hazards owns this; this carrier never re-asserts hazard authority. |
| This carrier is found to drift from Atlas Ch. 14 wording | Restore Atlas wording verbatim; the chapter wins. |
| This carrier is found to overclaim implementation | Demote to `PROPOSED` / `UNKNOWN`; never resolve drift by lowering the truth label. |

**Rollback target:** `ROLLBACK_TARGET_TBD` (PROPOSED: prior commit ref of this file as recorded in `release/manifests/`).

---

## 22. Source ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| **Atlas v1.0 Ch. 14 §§ A–N (pp. 90–96)** | **`CONFIRMED doctrine`** | Every A–N block of this carrier; verbatim or near-verbatim. | This carrier paraphrases; chapter wins on wording. Per-stage `Status` in block H is `PROPOSED` per the atlas. |
| Atlas v1.1 §24.1 + §24.1.2 (Source-Role Anti-Collapse + DENY conditions) | `CONFIRMED doctrine` | §13 anti-collapse posture (administrative-as-observation). | — |
| Atlas v1.1 §24.4.12 (Edges owned by Settlements/Infrastructure) | `CONFIRMED doctrine` | §F.1 supplement (People/Land, Frontier Matrix, Hazards edges). | Atlas v1.0 §14.F remains authoritative on the canonical 4-edge list (§F). |
| Atlas v1.1 §24.13 (Crosswalk, Ch. 14 row) | `CONFIRMED doctrine; paths PROPOSED` | §14 responsibility root + "Critical-asset deny lane" note. | All path-level claims are `PROPOSED` until mounted-repo verification. |
| Atlas v1.1 §24.14 (Object Family × Domain Matrix) | `CONFIRMED doctrine; defaults PROPOSED` | §I.1 per-object sensitivity defaults; §15.1 highlights. | Defaults are `PROPOSED supplement`. |
| `[DOM-SETTLE]` dossier (*KFM Settlements, Cities, and Infrastructure Plan*) | `CONFIRMED corpus presence` | Underlying source for Atlas Ch. 14 content. | Dossier wins over this carrier on wording. |
| `KFM_Encyclopedia.md` | `CONFIRMED corpus presence` | Dossier-tag mapping (`[DOM-SETTLE]`); cross-domain object-family corroboration. | Encyclopedia is corpus, not schema authority. |
| `directory-rules.md` v1.2/v1.3 §5, §12 | `CONFIRMED at commit b6a279…` | §14.1 lane pattern; `docs/atlases/` lane choice. | Path-level claims for new files remain `PROPOSED`. |
| `kfm_full_atlas_seed_cards.md` — Settlement and Infrastructure Evidence Lane Implementation Surface | `CONFIRMED corpus presence` | Implementation-surface card (PROPOSED) for this domain. | Card is `PROPOSED implementation`; not authority. |
| Parent carrier (`docs/atlases/domains-v1.1.md`) §3 Ch. 14 row | `PROPOSED file` (sibling session-authored) | §17 companion structure. | Carrier-only; defers to atlas wording. |

> **Memory is not evidence.** Every consequential claim in this file is traceable to one of the sources above, an Atlas row reproduced verbatim, or an explicit `PROPOSED` / `NEEDS VERIFICATION` / `CONFLICTED` placeholder. Where this carrier paraphrases Atlas Ch. 14 wording, the chapter wins on wording.

---

<p align="right"><a href="#kfm-domains-v11--ch-14-settlements--infrastructure">↑ Back to top</a></p>
