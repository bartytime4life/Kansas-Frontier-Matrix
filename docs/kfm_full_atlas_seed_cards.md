<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/kfm-atlas-seed-cards-optimized
title: KFM Atlas Seed Cards — Optimized Carry-Forward Register
type: atlas_card_register
version: v0.2
status: draft
owners: <PLACEHOLDER — Atlas steward · Docs steward · Evidence steward · Domain stewards>
created: 2026-06-12
updated: 2026-06-12
policy_label: public
authority_class: synthesis / candidate-card register; NOT canonical doctrine
requested_path: <UNSPECIFIED_BY_USER>
suggested_repository_home: docs/atlases/kfm-atlas-seed-cards.md
suggested_repository_home_status: PROPOSED — verify against Directory Rules, current repo docs index, and accepted ADRs before creating or moving files.
truth_posture: cite-or-abstain with explicit truth labels
implementation_boundary: current live repository state, schemas, policies, tests, release manifests, dashboards, and runtime behavior remain UNKNOWN unless verified in a mounted repo session.
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/atlases/
  - docs/domains/
tags:
  - kfm
  - atlas
  - seed-cards
  - idea-index
  - evidence
  - publication
  - maplibre
  - governed-ai
  - source-descriptor
  - release
  - rollback
notes:
  - "v0.2 — optimized from pasted seed-card draft into a compact maintainable register."
  - "The original draft repeated shared dependencies, tensions, open questions, and self-check text in every card. This edition deduplicates those into shared sections while preserving every card topic, class, category, source-ID set, and normalized statement."
  - "Stable IDs intentionally remain templates until PASS and ordinal allocation are supplied."
] -->

# KFM Atlas Seed Cards — Optimized Carry-Forward Register

> **Status:** Draft candidate-card register  
> **Authority:** Synthesis / candidate backlog, not canonical doctrine  
> **Input shape:** 96 card entries arranged as 32 idea/feature/programming triads  
> **Core posture:** evidence-first · map-first · time-aware · cite-or-abstain · fail-closed · auditable · reversible

---

## 0. Reader note

This document optimizes the supplied KFM seed-card draft into a maintainable repository-facing register.

The source draft already used KFM truth labels and included required card fields. The main problem was maintainability: every card repeated the same dependency, tension, open-question, carry-forward, and self-check language. This edition preserves the card content but moves repeated control language into shared sections.

This is a **candidate register**, not an implementation claim. No card here proves that a live repo path, schema, validator, policy, UI surface, release manifest, proof pack, or runtime behavior exists.

---

## 1. Optimization summary

| Item | Result |
|---|---:|
| Input card count | 96 |
| Triad count | 32 |
| Idea cards | 32 |
| Feature cards | 32 |
| Programming cards | 32 |
| Stable ID posture | Template retained: `KFM-P{PASS}-{CLASS}-{NNNN}` |
| Spec hash posture | `PROPOSED` until canonical JCS + SHA-256 computation |
| Repository implementation maturity | `UNKNOWN` |
| Primary optimization | Deduplicated repeated control text; preserved normalized statements and source IDs |
| Suggested repo home | `docs/atlases/kfm-atlas-seed-cards.md` — **PROPOSED** |

---

## 2. Directory and placement posture

**Requested path:** not supplied.

**Suggested home:** `docs/atlases/kfm-atlas-seed-cards.md`

**Status:** **PROPOSED**.

Rationale: this is a human-facing atlas/card register. It belongs under `docs/` unless current repo evidence or accepted ADRs define a more specific home for atlas card registers. Do not place it under `schemas/`, `contracts/`, `policy/`, `release/`, `data/`, `fixtures/`, or `tests/` because this document is not a machine schema, semantic contract, policy bundle, release artifact, data artifact, fixture, or test.

Before committing:

1. Verify the current `docs/` organization.
2. Check whether `docs/atlases/` exists.
3. Check whether an existing atlas seed-card file already exists.
4. If the target home is unclear, add a drift/open-question entry rather than creating a parallel authority home.

---

## 3. Shared truth labels

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from supplied source text, current-session artifacts, or cited doctrine. |
| **PROPOSED** | Candidate design, synthesis, implementation direction, or placement not verified as implemented. |
| **NEEDS VERIFICATION** | Checkable before implementation, source activation, publication, or operational use. |
| **UNKNOWN** | Not verified strongly enough to claim. |
| **CONFLICTED** | Sources or conventions disagree; preserve the conflict and route it to drift/ADR handling. |
| **DENY / ABSTAIN / ERROR** | Finite KFM policy/runtime outcomes, not rhetorical emphasis. |

---

## 4. Stable-ID allocation policy

The source cards use placeholder IDs:

```text
KFM-P{PASS}-IDEA-{NNNN}
KFM-P{PASS}-FEAT-{NNNN}
KFM-P{PASS}-PROG-{NNNN}
```

This edition preserves those placeholders because no pass number or ordinal assignment was supplied.

For local review only, each card also receives a noncanonical candidate key:

```text
KFM-CAND-0001 ... KFM-CAND-0096
```

When a pass is assigned, replace placeholders with deterministic pass-local IDs and compute `spec_hash` from canonicalized card JSON.

---

## 5. Shared dependencies

Unless a card explicitly narrows the requirement, every candidate card inherits these dependencies:

- **PROPOSED:** EvidenceBundle and EvidenceRef closure.
- **PROPOSED:** PolicyDecision and review-state checks.
- **PROPOSED:** ReleaseManifest or equivalent release-state record.
- **PROPOSED:** Rollback or correction reference where public exposure is possible.
- **PROPOSED:** Source-role preservation where the card depends on source evidence.
- **PROPOSED:** No public RAW / WORK / QUARANTINE exposure.
- **PROPOSED:** Directory Rules placement review before any file, schema, policy, registry, release, proof, receipt, or domain-lane path is created.
- **PROPOSED:** JSON Schema, contract validation, fixture tests, or policy checks where implementation is proposed.
- **PROPOSED:** No-network fixture tests for release-critical or policy-critical code paths.

---

## 6. Shared tensions and risks

- **PROPOSED:** Many topics are too broad for a single implementation PR and should be split into reversible proof slices.
- **NEEDS VERIFICATION:** Current mounted-repo conventions, schema homes, policy tooling, package manager, test runners, and CI gates are not verified in this register.
- **UNKNOWN:** Existing implementation maturity remains unresolved without current repo evidence.
- **PROPOSED:** Candidate source packets sometimes contain implementation-like examples; examples are not repo proof.
- **PROPOSED:** A card may be doctrine-aligned and still not be release-ready.
- **PROPOSED:** A card may be implementation-worthy and still require rights, sensitivity, policy, and reviewer approval before exposure.

---

## 7. Shared open questions

- **NEEDS VERIFICATION:** Which current repo files, schemas, policies, tests, receipts, proofs, release manifests, API routes, or UI surfaces already satisfy each card?
- **NEEDS VERIFICATION:** Which steward owns final release authority for each card family?
- **NEEDS VERIFICATION:** Which cards already exist under prior pass IDs and should be merged instead of duplicated?
- **NEEDS VERIFICATION:** Which proposed extension categories require vocabulary ratification?
- **NEEDS VERIFICATION:** Which cards require ADR support before implementation?
- **UNKNOWN:** Current repository implementation maturity for this register.

---

## 8. Source ledger

| Source ID | Description |
|---|---|

| `SRC-3DGIS` | Archaeological 3D GIS; role: 3D archaeology and field capture reference. Used by 6 cards. |
| `SRC-AGRI` | KFM Agriculture Domain Implementation Dossier Revised; role: agriculture domain lane blueprint. Used by 3 cards. |
| `SRC-AIREF` | AI Concepts Using Python; role: AI/data/ML workflow reference. Used by 3 cards. |
| `SRC-APIREF` | Designing Great Web APIs; role: API contract and resource lifecycle reference. Used by 3 cards. |
| `SRC-ARCH` | KFM Archaeology Architecture Plan; role: archaeology lane and exact-location deny posture. Used by 6 cards. |
| `SRC-ATM` | KFM Atmosphere / Air Architecture Report; role: air/climate/smoke/EO lane blueprint. Used by 3 cards. |
| `SRC-DIR` | Directory Rules; role: placement doctrine; basis: responsibility roots, schema-home convention, lifecycle invariant, ADR/drift rules. Used by 9 cards. |
| `SRC-ENCYC` | KFM Domain and Capability Encyclopedia; role: all-domain and cross-domain capability atlas; basis: operating law and domain inventory. Used by 81 cards. |
| `SRC-FAUNA` | KFM Fauna Architecture PDF-Only Report; role: fauna domain lane and geoprivacy blueprint. Used by 6 cards. |
| `SRC-FLORA` | KFM Flora Architecture PDF-Only Implementation Blueprint; role: flora domain lane and rare-location controls. Used by 3 cards. |
| `SRC-GAI` | KFM Governed AI Extended Pro Source Ledger Report; role: provider-neutral governed AI design and finite outcomes. Used by 6 cards. |
| `SRC-GEO` | KFM Geology and Natural Resources Architecture Report; role: geology/natural resources domain lane blueprint. Used by 3 cards. |
| `SRC-GIS` | A Primer of GIS; role: geographic/cartographic representation reference. Used by 3 cards. |
| `SRC-GREEN` | Kansas Frontier Matrix Definitive Greenfield Building Plan v1.1; role: trust spine and build principles; basis: lifecycle, object families, receipts, promotion, and anti-patterns. Used by 15 cards. |
| `SRC-HAB` | KFM Habitat Architecture Implementation Blueprint; role: habitat domain lane blueprint. Used by 3 cards. |
| `SRC-HABFAUNA` | KFM Habitat + Fauna Thin-Slice Extended Pro Blueprint; role: habitat/fauna fixture-first proof slice. Used by 6 cards. |
| `SRC-HAZ` | KFM Hazards Architecture Extended Pro Blueprint; role: hazards lane and non-emergency-alerting boundary. Used by 3 cards. |
| `SRC-HYD` | KFM Hydrology Extended Pro Reference Report; role: hydrology domain lane blueprint. Used by 3 cards. |
| `SRC-MAP` | KFM MapLibre Operating Architecture, Governed UI, and AI Interaction Manual; role: map renderer boundary and trust-visible UI doctrine. Used by 15 cards. |
| `SRC-MAPMASTER` | Master MapLibre Components-Functions-Features; role: cumulative MapLibre/tile/artifact atlas; basis: tile, style, manifest, PMTiles/COG, and validation ideas. Used by 15 cards. |
| `SRC-NEW510` | New Ideas 5-10-26; role: PMTiles sidecar/attestation operational packet. Used by 6 cards. |
| `SRC-NEW515` | New Ideas 5-15-26; role: CDL/PLANTS material-change watcher packet. Used by 6 cards. |
| `SRC-NEW58` | New Ideas 5-8-26; role: environmental source-health and gating spec packet. Used by 6 cards. |
| `SRC-OLL` | Ollama & Ubuntu Information; role: local runtime behind governed API and model-runtime constraints. Used by 3 cards. |
| `SRC-P18` | KFM Components Pass 18; role: prior cumulative card atlas; basis: 500 cards across 14 categories and source-supported idea entries. Used by 12 cards. |
| `SRC-P20` | KFM Components Pass 20 Unified Idea Index; role: cumulative idea/category atlas; basis: 9-category and 14-category normalization, implementation boundary, expansion agenda. Used by 39 cards. |
| `SRC-PEOPLE` | KFM People, Genealogy-DNA, and Land Ownership Architecture Blueprint; role: people/DNA/land sensitivity blueprint. Used by 6 cards. |
| `SRC-PIPE` | Kansas Frontier Matrix Pipeline Living Implementation Manual v0.3; role: lifecycle and query-save-recompile loop doctrine; basis: pipeline loop, source authority ladder, public-client rule. Used by 21 cards. |
| `SRC-ROADS` | KFM Roads, Rail, and Trade Routes Architecture Plan; role: transport lane blueprint. Used by 3 cards. |
| `SRC-SETTLE` | KFM Settlements, Cities, and Infrastructure Plan; role: settlements/infrastructure lane blueprint. Used by 3 cards. |
| `SRC-SOIL` | KFM Soil Architecture Extended Pro Planning Report; role: soil domain lane blueprint. Used by 3 cards. |
| `SRC-TEMPORAL` | Developing Time-Oriented Database Applications in SQL; role: temporal database semantics reference. Used by 3 cards. |
| `SRC-UIAI` | KFM Whole-UI + Governed AI Expansion Report; role: whole-UI and governed-AI expansion plan. Used by 3 cards. |
| `SRC-URBAN` | GIS in Sustainable Urban Planning and Management; role: planning, indicators, resilience, participation reference. Used by 6 cards. |

---

## 9. Triad index

| Triad | Topic | Sources | Idea | Feature | Programming |
|---|---|---|---|---|---|
| `KFM-TRIAD-001` | Inspectable Claim Operating Law | `SRC-ENCYC`, `SRC-GREEN`, `SRC-PIPE`, `SRC-P20` | `KFM-CAND-0001` | `KFM-CAND-0002` | `KFM-CAND-0003` |
| `KFM-TRIAD-002` | SourceDescriptor Admission Control | `SRC-ENCYC`, `SRC-P20`, `SRC-PIPE`, `SRC-DIR` | `KFM-CAND-0004` | `KFM-CAND-0005` | `KFM-CAND-0006` |
| `KFM-TRIAD-003` | Evidence Closure | `SRC-ENCYC`, `SRC-P20`, `SRC-GAI`, `SRC-MAP` | `KFM-CAND-0007` | `KFM-CAND-0008` | `KFM-CAND-0009` |
| `KFM-TRIAD-004` | Policy-Safe Exposure | `SRC-ENCYC`, `SRC-DIR`, `SRC-ARCH`, `SRC-FAUNA`, `SRC-PEOPLE` | `KFM-CAND-0010` | `KFM-CAND-0011` | `KFM-CAND-0012` |
| `KFM-TRIAD-005` | Time-Aware Spatial Semantics | `SRC-ENCYC`, `SRC-P18`, `SRC-TEMPORAL`, `SRC-GIS` | `KFM-CAND-0013` | `KFM-CAND-0014` | `KFM-CAND-0015` |
| `KFM-TRIAD-006` | Responsibility-Root Governance | `SRC-DIR`, `SRC-P20`, `SRC-GREEN` | `KFM-CAND-0016` | `KFM-CAND-0017` | `KFM-CAND-0018` |
| `KFM-TRIAD-007` | Validation Gate Lattice | `SRC-ENCYC`, `SRC-P20`, `SRC-PIPE`, `SRC-MAPMASTER` | `KFM-CAND-0019` | `KFM-CAND-0020` | `KFM-CAND-0021` |
| `KFM-TRIAD-008` | Receipts and Proof Objects | `SRC-GREEN`, `SRC-P20`, `SRC-MAPMASTER`, `SRC-NEW510` | `KFM-CAND-0022` | `KFM-CAND-0023` | `KFM-CAND-0024` |
| `KFM-TRIAD-009` | Governed Release State | `SRC-GREEN`, `SRC-PIPE`, `SRC-P20`, `SRC-ENCYC` | `KFM-CAND-0025` | `KFM-CAND-0026` | `KFM-CAND-0027` |
| `KFM-TRIAD-010` | Renderer-Downstream Map Law | `SRC-MAP`, `SRC-MAPMASTER`, `SRC-ENCYC`, `SRC-P18` | `KFM-CAND-0028` | `KFM-CAND-0029` | `KFM-CAND-0030` |
| `KFM-TRIAD-011` | Trust-Visible Interaction | `SRC-MAP`, `SRC-UIAI`, `SRC-ENCYC`, `SRC-P20` | `KFM-CAND-0031` | `KFM-CAND-0032` | `KFM-CAND-0033` |
| `KFM-TRIAD-012` | Evidence-Subordinate AI | `SRC-GAI`, `SRC-OLL`, `SRC-MAP`, `SRC-ENCYC` | `KFM-CAND-0034` | `KFM-CAND-0035` | `KFM-CAND-0036` |
| `KFM-TRIAD-013` | Governed Recompile Loop | `SRC-PIPE`, `SRC-P20`, `SRC-GREEN` | `KFM-CAND-0037` | `KFM-CAND-0038` | `KFM-CAND-0039` |
| `KFM-TRIAD-014` | Hydrology Proof Lane | `SRC-HYD`, `SRC-ENCYC`, `SRC-PIPE` | `KFM-CAND-0040` | `KFM-CAND-0041` | `KFM-CAND-0042` |
| `KFM-TRIAD-015` | Soil Evidence Lane | `SRC-SOIL`, `SRC-ENCYC` | `KFM-CAND-0043` | `KFM-CAND-0044` | `KFM-CAND-0045` |
| `KFM-TRIAD-016` | Habitat Evidence Lane | `SRC-HAB`, `SRC-HABFAUNA`, `SRC-ENCYC` | `KFM-CAND-0046` | `KFM-CAND-0047` | `KFM-CAND-0048` |
| `KFM-TRIAD-017` | Fauna Public-Safety Lane | `SRC-FAUNA`, `SRC-HABFAUNA`, `SRC-ENCYC` | `KFM-CAND-0049` | `KFM-CAND-0050` | `KFM-CAND-0051` |
| `KFM-TRIAD-018` | Flora Public-Safety Lane | `SRC-FLORA`, `SRC-ENCYC` | `KFM-CAND-0052` | `KFM-CAND-0053` | `KFM-CAND-0054` |
| `KFM-TRIAD-019` | Agriculture and Landcover Watchers | `SRC-AGRI`, `SRC-NEW515`, `SRC-ENCYC` | `KFM-CAND-0055` | `KFM-CAND-0056` | `KFM-CAND-0057` |
| `KFM-TRIAD-020` | Geology Resource Evidence Lane | `SRC-GEO`, `SRC-ENCYC` | `KFM-CAND-0058` | `KFM-CAND-0059` | `KFM-CAND-0060` |
| `KFM-TRIAD-021` | Atmosphere Knowledge-Character Lane | `SRC-ATM`, `SRC-NEW58`, `SRC-ENCYC` | `KFM-CAND-0061` | `KFM-CAND-0062` | `KFM-CAND-0063` |
| `KFM-TRIAD-022` | Hazards Without Emergency Alerting | `SRC-HAZ`, `SRC-ENCYC` | `KFM-CAND-0064` | `KFM-CAND-0065` | `KFM-CAND-0066` |
| `KFM-TRIAD-023` | Transport Corridor Evidence Lane | `SRC-ROADS`, `SRC-ENCYC` | `KFM-CAND-0067` | `KFM-CAND-0068` | `KFM-CAND-0069` |
| `KFM-TRIAD-024` | Settlement and Infrastructure Evidence Lane | `SRC-SETTLE`, `SRC-ENCYC` | `KFM-CAND-0070` | `KFM-CAND-0071` | `KFM-CAND-0072` |
| `KFM-TRIAD-025` | Archaeology Exact-Location Deny Lane | `SRC-ARCH`, `SRC-3DGIS`, `SRC-ENCYC` | `KFM-CAND-0073` | `KFM-CAND-0074` | `KFM-CAND-0075` |
| `KFM-TRIAD-026` | People DNA Land Safety Lane | `SRC-PEOPLE`, `SRC-ENCYC` | `KFM-CAND-0076` | `KFM-CAND-0077` | `KFM-CAND-0078` |
| `KFM-TRIAD-027` | Participatory Planning Support | `SRC-URBAN`, `SRC-ENCYC`, `SRC-P20` | `KFM-CAND-0079` | `KFM-CAND-0080` | `KFM-CAND-0081` |
| `KFM-TRIAD-028` | Field and 3D Capture Governance | `SRC-3DGIS`, `SRC-P18`, `SRC-ENCYC`, `SRC-MAPMASTER` | `KFM-CAND-0082` | `KFM-CAND-0083` | `KFM-CAND-0084` |
| `KFM-TRIAD-029` | Governed API Contract Membrane | `SRC-APIREF`, `SRC-P20`, `SRC-MAP`, `SRC-ENCYC` | `KFM-CAND-0085` | `KFM-CAND-0086` | `KFM-CAND-0087` |
| `KFM-TRIAD-030` | Interpretive Analytics Governance | `SRC-AIREF`, `SRC-P18`, `SRC-ENCYC`, `SRC-URBAN` | `KFM-CAND-0088` | `KFM-CAND-0089` | `KFM-CAND-0090` |
| `KFM-TRIAD-031` | Map Artifact Integrity | `SRC-MAPMASTER`, `SRC-NEW510`, `SRC-P20` | `KFM-CAND-0091` | `KFM-CAND-0092` | `KFM-CAND-0093` |
| `KFM-TRIAD-032` | Watcher-as-Non-Publisher | `SRC-NEW58`, `SRC-NEW515`, `SRC-PIPE`, `SRC-P20` | `KFM-CAND-0094` | `KFM-CAND-0095` | `KFM-CAND-0096` |

---

## 10. Card register

### KFM-TRIAD-001 — Inspectable Claim Operating Law

**Why it matters:** PROPOSED — This card matters because it preserves cite-or-abstain, the trust membrane, and governed publication as the central public truth posture.

**Source IDs:** `SRC-ENCYC`, `SRC-GREEN`, `SRC-PIPE`, `SRC-P20`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0001` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should treat the inspectable claim as the durable unit of public value across maps, tiles, graphs, AI answers, dashboards, and exports. |
| `KFM-CAND-0002` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should expose claim-level evidence, temporal scope, spatial scope, source role, policy posture, review state, release state, and correction lineage wherever a public surface makes or implies a consequential claim. |
| `KFM-CAND-0003` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should define a claim envelope contract that binds EvidenceRef, EvidenceBundle status, policy decision, release state, correction lineage, and rollback reference before publication. |

**Implementation-surface note:** PROPOSED — KFM should define a claim envelope contract that binds EvidenceRef, EvidenceBundle status, policy decision, release state, correction lineage, and rollback reference before publication.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-002 — SourceDescriptor Admission Control

**Why it matters:** PROPOSED — This card matters because it prevents external feeds, aggregators, and scraped material from becoming authority without review.

**Source IDs:** `SRC-ENCYC`, `SRC-P20`, `SRC-PIPE`, `SRC-DIR`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0004` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | PROPOSED — KFM should make source admission a governed decision that records source role, rights posture, sensitivity posture, update cadence, authority class, and permitted use before data enters the lifecycle. |
| `KFM-CAND-0005` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should give stewards a source-intake and source-health view that distinguishes admissible sources, quarantined sources, context-only sources, and denied sources. |
| `KFM-CAND-0006` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | PROPOSED — KFM should implement SourceDescriptor, SourceIntakeRecord, SourceHealthCheck, and source-role validators as controlled inputs to connectors and watchers. |

**Implementation-surface note:** PROPOSED — KFM should implement SourceDescriptor, SourceIntakeRecord, SourceHealthCheck, and source-role validators as controlled inputs to connectors and watchers.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-003 — Evidence Closure

**Why it matters:** PROPOSED — This card matters because it makes generated language and visual context subordinate to evidence instead of persuasive by default.

**Source IDs:** `SRC-ENCYC`, `SRC-P20`, `SRC-GAI`, `SRC-MAP`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0007` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should require EvidenceRef to resolve to an EvidenceBundle before a claim is answered, rendered as authoritative, exported, or promoted. |
| `KFM-CAND-0008` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should surface evidence closure, missing evidence, abstention reasons, and withheld-evidence posture in the Evidence Drawer and Focus Mode response envelope. |
| `KFM-CAND-0009` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should implement a CitationValidationReport and EvidenceResolutionReport that produce finite ANSWER, ABSTAIN, DENY, or ERROR outcomes. |

**Implementation-surface note:** PROPOSED — KFM should implement a CitationValidationReport and EvidenceResolutionReport that produce finite ANSWER, ABSTAIN, DENY, or ERROR outcomes.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-004 — Policy-Safe Exposure

**Why it matters:** PROPOSED — This card matters because it preserves public safety, steward trust, rights compliance, and reversible release discipline.

**Source IDs:** `SRC-ENCYC`, `SRC-DIR`, `SRC-ARCH`, `SRC-FAUNA`, `SRC-PEOPLE`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0010` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should fail closed when rights, sovereignty, cultural sensitivity, living-person data, DNA/genomics, rare species, archaeology, infrastructure, private land, or precise-location exposure is unclear. |
| `KFM-CAND-0011` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should present redaction, denial, generalization, staged access, stale state, and abstention as explicit trust-visible states rather than hidden implementation details. |
| `KFM-CAND-0012` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should implement policy decision contracts and fail-closed validators that block release when rights, source terms, sensitivity review, or access posture is unresolved. |

**Implementation-surface note:** PROPOSED — KFM should implement policy decision contracts and fail-closed validators that block release when rights, source terms, sensitivity review, or access posture is unresolved.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-005 — Time-Aware Spatial Semantics

**Why it matters:** PROPOSED — This card matters because it prevents users from mistaking current-state summaries, historical sequences, and nonsequenced evidence for the same claim.

**Source IDs:** `SRC-ENCYC`, `SRC-P18`, `SRC-TEMPORAL`, `SRC-GIS`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0013` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model valid time, observed time, source time, retrieval time, release time, and correction time as distinct dimensions where the distinction affects evidence or interpretation. |
| `KFM-CAND-0014` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should disclose temporal query mode, time window, geography version, uncertainty class, and fitness-for-use for public analytical and map-facing outputs. |
| `KFM-CAND-0015` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should implement temporal_scope, geography_version, query_receipt, and temporal_query_mode fields in relevant runtime and evidence contracts. |

**Implementation-surface note:** PROPOSED — KFM should implement temporal_scope, geography_version, query_receipt, and temporal_query_mode fields in relevant runtime and evidence contracts.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-006 — Responsibility-Root Governance

**Why it matters:** PROPOSED — This card matters because it avoids parallel schema homes, policy islands, duplicate release stores, and domain-root drift.

**Source IDs:** `SRC-DIR`, `SRC-P20`, `SRC-GREEN`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0016` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should treat path placement as governance because a file location encodes responsibility root, lifecycle phase, and authority boundary. |
| `KFM-CAND-0017` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should provide reviewers a path-placement checklist that marks proposed homes, required ADRs, drift risks, and rollback or migration notes. |
| `KFM-CAND-0018` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement directory-rule linting and path-proposal validation for contracts, schemas, policies, release artifacts, proofs, receipts, source registries, and domain lanes. |

**Implementation-surface note:** PROPOSED — KFM should implement directory-rule linting and path-proposal validation for contracts, schemas, policies, release artifacts, proofs, receipts, source registries, and domain lanes.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-007 — Validation Gate Lattice

**Why it matters:** PROPOSED — This card matters because it keeps promotion from becoming warning-only and makes failure states inspectable.

**Source IDs:** `SRC-ENCYC`, `SRC-P20`, `SRC-PIPE`, `SRC-MAPMASTER`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0019` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should treat validation, QA, observability, and reliability as part of publication truth rather than as post-release hygiene. |
| `KFM-CAND-0020` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should expose validation status, freshness status, source-health status, denied state, degraded state, and rollback readiness to reviewers and, where safe, public users. |
| `KFM-CAND-0021` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement no-network fixture tests, schema validators, policy validators, visual regression checks, material-change tests, and receipt completeness checks as release gates. |

**Implementation-surface note:** PROPOSED — KFM should implement no-network fixture tests, schema validators, policy validators, visual regression checks, material-change tests, and receipt completeness checks as release gates.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-008 — Receipts and Proof Objects

**Why it matters:** PROPOSED — This card matters because it supports deterministic identity, tamper-evident review, source continuity, and rollback.

**Source IDs:** `SRC-GREEN`, `SRC-P20`, `SRC-MAPMASTER`, `SRC-NEW510`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0022` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should pair receipts and proof objects so every intake, transform, catalog, map-artifact build, AI response, and release can be reconstructed and challenged. |
| `KFM-CAND-0023` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | REL - Catalog Closure, Publication, Release, Rollback, Recompile | PROPOSED — KFM should let reviewers inspect run receipts, promotion receipts, proof packs, content hashes, signature state, attestation references, and rollback targets before release. |
| `KFM-CAND-0024` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should implement RunReceipt, PromotionReceipt, MerkleManifest, DSSE or equivalent signed envelope, spec_hash, and attestation validators for release-critical actions. |

**Implementation-surface note:** PROPOSED — KFM should implement RunReceipt, PromotionReceipt, MerkleManifest, DSSE or equivalent signed envelope, spec_hash, and attestation validators for release-critical actions.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-009 — Governed Release State

**Why it matters:** PROPOSED — This card matters because it prevents publication from becoming a file copy, layer toggle, or unreviewed generated output.

**Source IDs:** `SRC-GREEN`, `SRC-PIPE`, `SRC-P20`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0025` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | REL - Catalog Closure, Publication, Release, Rollback, Recompile | PROPOSED — KFM should treat promotion as a governed state transition backed by validation, policy, review, proof, catalog, release manifest, correction path, and rollback target. |
| `KFM-CAND-0026` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | REL - Catalog Closure, Publication, Release, Rollback, Recompile | PROPOSED — KFM should provide release and correction surfaces that show what changed, why it changed, what evidence supports it, and how to roll it back or supersede it. |
| `KFM-CAND-0027` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | REL - Catalog Closure, Publication, Release, Rollback, Recompile | PROPOSED — KFM should implement PromotionDecision, ReleaseManifest, CatalogClosureReport, CorrectionNotice, WithdrawalRecord, and RollbackCard as separate but linked artifact families. |

**Implementation-surface note:** PROPOSED — KFM should implement PromotionDecision, ReleaseManifest, CatalogClosureReport, CorrectionNotice, WithdrawalRecord, and RollbackCard as separate but linked artifact families.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-010 — Renderer-Downstream Map Law

**Why it matters:** PROPOSED — This card matters because it preserves the trust membrane while still allowing fast map exploration.

**Source IDs:** `SRC-MAP`, `SRC-MAPMASTER`, `SRC-ENCYC`, `SRC-P18`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0028` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should keep MapLibre downstream of evidence, policy, review, and release state rather than letting rendered pixels, feature properties, or layer visibility become truth authority. |
| `KFM-CAND-0029` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should show released, stale, degraded, denied, context-only, generalized, and withheld states directly in map layers, popups, Evidence Drawer links, and export paths. |
| `KFM-CAND-0030` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should implement LayerManifest, StyleManifest, TileArtifactManifest, MapReleaseManifest, MapContextEnvelope, and no-direct-RAW/WORK/QUARANTINE checks for map sources. |

**Implementation-surface note:** PROPOSED — KFM should implement LayerManifest, StyleManifest, TileArtifactManifest, MapReleaseManifest, MapContextEnvelope, and no-direct-RAW/WORK/QUARANTINE checks for map sources.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-011 — Trust-Visible Interaction

**Why it matters:** PROPOSED — This card matters because it prevents polished UI from hiding uncertainty, denial, source gaps, or policy limits.

**Source IDs:** `SRC-MAP`, `SRC-UIAI`, `SRC-ENCYC`, `SRC-P20`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0031` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should make the UI part of the trust model by exposing evidence, policy, review, release, stale, correction, and abstention state at the point of use. |
| `KFM-CAND-0032` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should provide Evidence Drawer, Focus Mode, Story Node, Compare, Review, Dossier, and Export affordances that never bypass governed APIs. |
| `KFM-CAND-0033` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should implement EvidenceDrawerPayload, FocusModeEnvelope, StoryManifest, ReviewHandoff, TrustStateBadge, and accessibility/performance validation surfaces. |

**Implementation-surface note:** PROPOSED — KFM should implement EvidenceDrawerPayload, FocusModeEnvelope, StoryManifest, ReviewHandoff, TrustStateBadge, and accessibility/performance validation surfaces.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-012 — Evidence-Subordinate AI

**Why it matters:** PROPOSED — This card matters because it blocks AI from becoming a hidden truth source or public bypass around evidence and policy.

**Source IDs:** `SRC-GAI`, `SRC-OLL`, `SRC-MAP`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0034` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should treat AI as interpretive and provider-neutral, with EvidenceBundle, policy decision, review state, citation validation, and finite outcomes outranking model language. |
| `KFM-CAND-0035` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should let Focus Mode answer only over released or admissible evidence context and should make ABSTAIN, DENY, and ERROR first-class outcomes. |
| `KFM-CAND-0036` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement MockAdapter-first runtime contracts, RuntimeResponseEnvelope, AIReceipt, CitationValidationReport, and no-direct-model-client checks before any live runtime adapter. |

**Implementation-surface note:** PROPOSED — KFM should implement MockAdapter-first runtime contracts, RuntimeResponseEnvelope, AIReceipt, CitationValidationReport, and no-direct-model-client checks before any live runtime adapter.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-013 — Governed Recompile Loop

**Why it matters:** PROPOSED — This card matters because it allows improvement while preserving receipts, review, policy checks, and rollback.

**Source IDs:** `SRC-PIPE`, `SRC-P20`, `SRC-GREEN`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0037` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement the incremental query-save-validate-compile-review-promote-recompile loop as a governed learning and recompilation lane, not as autonomous self-modification. |
| `KFM-CAND-0038` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should let maintainers inspect QueryRunRecord, EvidenceResolutionRecord, CandidateDelta, RecompileManifest, LoopValidationReport, LoopDecision, and rollback references. |
| `KFM-CAND-0039` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement dry-run compilers, loop-control schemas, no-autopublish policy gates, and loop fixtures before live source or model integration. |

**Implementation-surface note:** PROPOSED — KFM should implement dry-run compilers, loop-control schemas, no-autopublish policy gates, and loop fixtures before live source or model integration.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-014 — Hydrology Proof Lane

**Why it matters:** PROPOSED — This card matters because it provides a high-value proof lane while reinforcing lifecycle and evidence closure.

**Source IDs:** `SRC-HYD`, `SRC-ENCYC`, `SRC-PIPE`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0040` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should treat hydrology as a proof-bearing domain lane that distinguishes watershed identity, hydrography networks, observations, regulatory flood context, terrain-derived context, and public-safe map products. |
| `KFM-CAND-0041` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should support watershed, HUC, streamflow, flood-context, hydrograph, layer-evidence, and source-freshness views that resolve to evidence and source role. |
| `KFM-CAND-0042` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement hydrology SourceDescriptors, HUC fixtures, observation normalization, hydrograph evidence bundles, layer manifests, and validation gates before public release. |

**Implementation-surface note:** PROPOSED — KFM should implement hydrology SourceDescriptors, HUC fixtures, observation normalization, hydrograph evidence bundles, layer manifests, and validation gates before public release.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-015 — Soil Evidence Lane

**Why it matters:** PROPOSED — This card matters because it prevents soil maps and derived surfaces from being treated as unqualified ground truth.

**Source IDs:** `SRC-SOIL`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0043` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model soil surveys, map units, horizons, properties, soil-moisture context, and derived suitability products as evidence-bound objects with source-role limits. |
| `KFM-CAND-0044` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should expose soil properties, uncertainty, source date, survey lineage, cross-domain links to hydrology/agriculture, and public-safe map layers. |
| `KFM-CAND-0045` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement soil source descriptors, soil map-unit schemas, horizon/property validators, snapshot receipts, and tile/catalog artifacts with rollback targets. |

**Implementation-surface note:** PROPOSED — KFM should implement soil source descriptors, soil map-unit schemas, horizon/property validators, snapshot receipts, and tile/catalog artifacts with rollback targets.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-016 — Habitat Evidence Lane

**Why it matters:** PROPOSED — This card matters because it keeps ecological interpretation bounded by evidence, policy, and public-safe geometry.

**Source IDs:** `SRC-HAB`, `SRC-HABFAUNA`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0046` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should represent habitat patches, suitability, connectivity, restoration context, disturbance state, and habitat assignment as evidence-supported claims rather than unconstrained model outputs. |
| `KFM-CAND-0047` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should let users inspect habitat assignment evidence, model support, uncertainty class, stewardship posture, and public-safe derived maps. |
| `KFM-CAND-0048` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement habitat schemas, habitat-fauna join fixtures, model-support validators, sensitivity gates, and EvidenceDrawer payloads for habitat assignment. |

**Implementation-surface note:** PROPOSED — KFM should implement habitat schemas, habitat-fauna join fixtures, model-support validators, sensitivity gates, and EvidenceDrawer payloads for habitat assignment.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-017 — Fauna Public-Safety Lane

**Why it matters:** PROPOSED — This card matters because it reduces rare-species and sensitive-location leakage while preserving inspectable ecological evidence.

**Source IDs:** `SRC-FAUNA`, `SRC-HABFAUNA`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0049` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should distinguish taxonomy, occurrence evidence, conservation status, range, seasonal range, habitat support, disease/mortality evidence, and public-safe derivatives in the fauna lane. |
| `KFM-CAND-0050` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should expose generalized or redacted fauna layers, evidence drawer explanations, steward review state, and geoprivacy reasons where exact public exposure is unsafe. |
| `KFM-CAND-0051` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement taxon resolution, occurrence sensitivity classification, source-role constraints, generalized layer manifests, and geoprivacy validators. |

**Implementation-surface note:** PROPOSED — KFM should implement taxon resolution, occurrence sensitivity classification, source-role constraints, generalized layer manifests, and geoprivacy validators.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-018 — Flora Public-Safety Lane

**Why it matters:** PROPOSED — This card matters because it protects rare plant locations and steward-controlled evidence while preserving auditability.

**Source IDs:** `SRC-FLORA`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0052` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should manage flora observations, specimens, taxonomic identity, rare-plant controls, modeled surfaces, and public visualizations as separate evidence and release objects. |
| `KFM-CAND-0053` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should show flora evidence, taxonomic confidence, status context, redaction posture, steward review, and generalized map outputs when public exposure is permitted. |
| `KFM-CAND-0054` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement flora source descriptors, taxon identifiers, occurrence/geoprivacy schemas, sensitivity gates, and public-safe artifact validators. |

**Implementation-surface note:** PROPOSED — KFM should implement flora source descriptors, taxon identifiers, occurrence/geoprivacy schemas, sensitivity gates, and public-safe artifact validators.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-019 — Agriculture and Landcover Watchers

**Why it matters:** PROPOSED — This card matters because it reduces noisy reruns and preserves publication as a reviewed transition.

**Source IDs:** `SRC-AGRI`, `SRC-NEW515`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0055` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | PROPOSED — KFM should treat cropland, landcover, agriculture statistics, crop-class changes, and PLANTS package deltas as governed signals that propose work rather than auto-publish changes. |
| `KFM-CAND-0056` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should expose county-level material-change records, class histograms, threshold reasons, source heads, and proposed-work status to reviewers. |
| `KFM-CAND-0057` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement CDL/PLANTS sidecars, spec_hash computation, materiality thresholds, watcher events, PROPOSED_WORK_RECORD outbox artifacts, and validator gates. |

**Implementation-surface note:** PROPOSED — KFM should implement CDL/PLANTS sidecars, spec_hash computation, materiality thresholds, watcher events, PROPOSED_WORK_RECORD outbox artifacts, and validator gates.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-020 — Geology Resource Evidence Lane

**Why it matters:** PROPOSED — This card matters because it prevents physical geology, resource administration, production history, and public visualizations from collapsing into one truth layer.

**Source IDs:** `SRC-GEO`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0058` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should distinguish bedrock, surficial geology, stratigraphy, structures, geomorphology, borehole evidence, resource estimates, extraction records, and public-safe geology layers. |
| `KFM-CAND-0059` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should let users inspect geology/resource claims by source role, evidence type, spatial precision, interpretation class, release state, and cross-domain linkage. |
| `KFM-CAND-0060` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement geology SourceDescriptors, stratigraphic and lithologic object schemas, public-safe geometry rules, catalog artifacts, and validation fixtures. |

**Implementation-surface note:** PROPOSED — KFM should implement geology SourceDescriptors, stratigraphic and lithologic object schemas, public-safe geometry rules, catalog artifacts, and validation fixtures.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-021 — Atmosphere Knowledge-Character Lane

**Why it matters:** PROPOSED — This card matters because it prevents modeled, operational, regulatory, and observational layers from becoming epistemically interchangeable.

**Source IDs:** `SRC-ATM`, `SRC-NEW58`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0061` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should distinguish observations, public AQI context, regulatory archives, model fields, smoke masks, anomaly surfaces, and fusion products in the atmosphere and air lane. |
| `KFM-CAND-0062` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should show air-quality context, freshness, preliminary status, parameter meaning, source-role limits, and knowledge-character labels for map and analysis outputs. |
| `KFM-CAND-0063` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement atmosphere parameter registries, source-health probes, AOD/FIRMS/SMAP/AirNow/Mesonet decision envelopes, and fail-closed source-rights gates. |

**Implementation-surface note:** PROPOSED — KFM should implement atmosphere parameter registries, source-health probes, AOD/FIRMS/SMAP/AirNow/Mesonet decision envelopes, and fail-closed source-rights gates.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-022 — Hazards Without Emergency Alerting

**Why it matters:** PROPOSED — This card matters because it preserves public safety and prevents KFM from substituting for official emergency systems.

**Source IDs:** `SRC-HAZ`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0064` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should support hazards history, regulatory context, operational context, observations, detections, models, and resilience review without becoming an emergency alert system. |
| `KFM-CAND-0065` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should expose hazard evidence, freshness, expiry, operational-context disclaimers, source authority, and official-source routing where life-safety action is requested. |
| `KFM-CAND-0066` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement hazard source-role descriptors, event/observation/model separation, not-for-life-safety policy checks, and finite DENY/ABSTAIN behavior for unsafe requests. |

**Implementation-surface note:** PROPOSED — KFM should implement hazard source-role descriptors, event/observation/model separation, not-for-life-safety policy checks, and finite DENY/ABSTAIN behavior for unsafe requests.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-023 — Transport Corridor Evidence Lane

**Why it matters:** PROPOSED — This card matters because it keeps historic interpretation, administrative status, and route geometry separate but related.

**Source IDs:** `SRC-ROADS`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0067` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model modern roads, historic roads, rail corridors, trade routes, movement corridors, facilities, restrictions, and graph projections without equating geometry with authority. |
| `KFM-CAND-0068` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should let users inspect route evidence, temporal status, generalized historic geometry, operator or jurisdiction assertions, access restrictions, and public-safe corridor maps. |
| `KFM-CAND-0069` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement transport object schemas, temporal event records, graph projection manifests, sensitive-corridor generalization rules, and EvidenceDrawer payloads. |

**Implementation-surface note:** PROPOSED — KFM should implement transport object schemas, temporal event records, graph projection manifests, sensitive-corridor generalization rules, and EvidenceDrawer payloads.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-024 — Settlement and Infrastructure Evidence Lane

**Why it matters:** PROPOSED — This card matters because it prevents map labels, administrative records, infrastructure assets, and public claims from collapsing into one unreviewed layer.

**Source IDs:** `SRC-SETTLE`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0070` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model settlements, municipalities, census places, historic townsites, infrastructure assets, networks, operators, condition observations, dependencies, and public-safe representations separately. |
| `KFM-CAND-0071` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should expose settlement identity, alternative names, legal status, infrastructure condition, service areas, dependencies, sensitivity flags, and review posture. |
| `KFM-CAND-0072` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement settlement and infrastructure schemas, stable identity helpers, source descriptors, deny policies for sensitive assets, and public-safe layer manifests. |

**Implementation-surface note:** PROPOSED — KFM should implement settlement and infrastructure schemas, stable identity helpers, source descriptors, deny policies for sensitive assets, and public-safe layer manifests.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-025 — Archaeology Exact-Location Deny Lane

**Why it matters:** PROPOSED — This card matters because it reduces looting, cultural harm, and false precision while preserving evidence and review traceability.

**Source IDs:** `SRC-ARCH`, `SRC-3DGIS`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0073` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should treat archaeological records, remote-sensing anomalies, 3D interpretations, site claims, artifacts, cultural review, and public maps as governed evidence objects with exact-location denial by default. |
| `KFM-CAND-0074` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should expose reviewed generalized archaeology layers, sensitivity reasons, steward review state, evidence confidence, and interpretation limits without disclosing unsafe exact locations. |
| `KFM-CAND-0075` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement archaeology sensitivity policies, anomaly-versus-confirmed-site schemas, geoprivacy transforms, transform receipts, and public-output validators. |

**Implementation-surface note:** PROPOSED — KFM should implement archaeology sensitivity policies, anomaly-versus-confirmed-site schemas, geoprivacy transforms, transform receipts, and public-output validators.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-026 — People DNA Land Safety Lane

**Why it matters:** PROPOSED — This card matters because it prevents sensitive personal or genomic information and weak land-title inference from becoming public truth.

**Source IDs:** `SRC-PEOPLE`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0076` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should represent people assertions, relationship hypotheses, DNA-derived evidence, land ownership assertions, and parcel or assessor context as evidence-bound and policy-sensitive records. |
| `KFM-CAND-0077` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should distinguish historical research, living-person restrictions, DNA restrictions, title evidence limits, parcel geometry caveats, and relationship hypothesis confidence in public and reviewer views. |
| `KFM-CAND-0078` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement assertion-first people/land schemas, living-person and DNA denial policies, temporal land-ownership assertions, relationship evidence validators, and restricted-access payloads. |

**Implementation-surface note:** PROPOSED — KFM should implement assertion-first people/land schemas, living-person and DNA denial policies, temporal land-ownership assertions, relationship evidence validators, and restricted-access payloads.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-027 — Participatory Planning Support

**Why it matters:** PROPOSED — This card matters because it keeps planning support transparent, reviewable, and bounded by evidence and policy.

**Source IDs:** `SRC-URBAN`, `SRC-ENCYC`, `SRC-P20`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0079` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should support planning, participation, resilience, equity, scenarios, and decision support as evidence-informed interpretation rather than automatic recommendation authority. |
| `KFM-CAND-0080` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should provide scenario views, indicator dashboards, stakeholder notes, uncertainty labels, equity context, and evidence-backed planning explanations. |
| `KFM-CAND-0081` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement scenario manifests, indicator definition contracts, stakeholder-input receipts, equity/sensitivity checks, and decision-support validation reports. |

**Implementation-surface note:** PROPOSED — KFM should implement scenario manifests, indicator definition contracts, stakeholder-input receipts, equity/sensitivity checks, and decision-support validation reports.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-028 — Field and 3D Capture Governance

**Why it matters:** PROPOSED — This card matters because it prevents high-fidelity visuals from overstating certainty or exposing sensitive locations.

**Source IDs:** `SRC-3DGIS`, `SRC-P18`, `SRC-ENCYC`, `SRC-MAPMASTER`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0082` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should treat field capture, remote sensing, 3D models, LiDAR, terrain, drone data, and archaeological visualization as evidence carriers with acquisition, processing, interpretation, and sensitivity metadata. |
| `KFM-CAND-0083` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should expose acquisition method, processing lineage, interpretation status, dimensional caveats, view limits, and public-safe 2D or 3D representations. |
| `KFM-CAND-0084` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement capture receipts, 3D/remote-sensing source descriptors, model/scene manifests, georeferencing validators, and sensitivity gates for exact or high-resolution outputs. |

**Implementation-surface note:** PROPOSED — KFM should implement capture receipts, 3D/remote-sensing source descriptors, model/scene manifests, georeferencing validators, and sensitivity gates for exact or high-resolution outputs.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-029 — Governed API Contract Membrane

**Why it matters:** PROPOSED — This card matters because it keeps public clients downstream of evidence, policy, and release gates.

**Source IDs:** `SRC-APIREF`, `SRC-P20`, `SRC-MAP`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0085` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should make APIs the governed trust membrane between public surfaces and internal stores, rather than exposing canonical or lifecycle stores directly. |
| `KFM-CAND-0086` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should provide evidence-backed resource responses, finite negative outcomes, release-state filters, citation validation, and review-safe payloads for UI, map, export, and Focus Mode clients. |
| `KFM-CAND-0087` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement OpenAPI-like contracts, runtime envelopes, resource lifecycle response codes, no-raw-public-route checks, and response validators. |

**Implementation-surface note:** PROPOSED — KFM should implement OpenAPI-like contracts, runtime envelopes, resource lifecycle response codes, no-raw-public-route checks, and response validators.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-030 — Interpretive Analytics Governance

**Why it matters:** PROPOSED — This card matters because it prevents derived metrics or model fluency from replacing source evidence.

**Source IDs:** `SRC-AIREF`, `SRC-P18`, `SRC-ENCYC`, `SRC-URBAN`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0088` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should treat analytics, indicators, statistics, machine learning, and model interpretation as derived and explainable outputs that remain subordinate to evidence and policy. |
| `KFM-CAND-0089` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should disclose model inputs, assumptions, uncertainty, validation status, training or source lineage, confidence class, and interpretation limits for analytic outputs. |
| `KFM-CAND-0090` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement ModelRunReceipt, IndicatorDefinition, FeatureSetManifest, ValidationReport, and model-output policy checks before any public analytic result is published. |

**Implementation-surface note:** PROPOSED — KFM should implement ModelRunReceipt, IndicatorDefinition, FeatureSetManifest, ValidationReport, and model-output policy checks before any public analytic result is published.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-031 — Map Artifact Integrity

**Why it matters:** PROPOSED — This card matters because it prevents stale tile swaps, unverifiable map artifacts, and untraceable visual releases.

**Source IDs:** `SRC-MAPMASTER`, `SRC-NEW510`, `SRC-P20`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0091` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should treat PMTiles, COGs, GeoParquet, style JSON, and rendered previews as release artifacts whose integrity, provenance, and rollback readiness must be inspectable. |
| `KFM-CAND-0092` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should let reviewers inspect artifact root hashes, byte-range manifests, sidecars, signatures, tool versions, input digests, source ledger references, and release manifest links. |
| `KFM-CAND-0093` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should implement PMTiles/COG sidecar schemas, BLAKE3 or equivalent roots, byte-range proofs, signed attestations, artifact validators, and no-in-place-overwrite release checks. |

**Implementation-surface note:** PROPOSED — KFM should implement PMTiles/COG sidecar schemas, BLAKE3 or equivalent roots, byte-range proofs, signed attestations, artifact validators, and no-in-place-overwrite release checks.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

### KFM-TRIAD-032 — Watcher-as-Non-Publisher

**Why it matters:** PROPOSED — This card matters because it keeps source freshness actionable without turning automation into unreviewed publication.

**Source IDs:** `SRC-NEW58`, `SRC-NEW515`, `SRC-PIPE`, `SRC-P20`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0094` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | PROPOSED — KFM should let watchers detect material source changes and source-health shifts while preventing watchers from publishing or committing directly to canonical release state. |
| `KFM-CAND-0095` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should expose proposed work records, source-head diffs, threshold breaches, persistence windows, license failures, and review status to maintainers. |
| `KFM-CAND-0096` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement watcher sidecars, HEAD/ETag probes, Last-Modified capture, materiality rules, signed run receipts, proposed-work outboxes, and default-deny policy gates. |

**Implementation-surface note:** PROPOSED — KFM should implement watcher sidecars, HEAD/ETag probes, Last-Modified capture, materiality rules, signed run receipts, proposed-work outboxes, and default-deny policy gates.

**Carry-forward state:** EXPANDED. Repository implementation status remains **UNKNOWN** until mounted-repo evidence verifies files, schemas, policies, tests, workflows, releases, or runtime behavior.

---

## 11. Category distribution

| Category | Count |
|---|---:|

| PIP - Pipelines, Pipeline Specs, Validators | 25 |
| MAP - Map Surface, MapLibre, Tiles, Styling | 14 |
| MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | 9 |
| UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | 9 |
| ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | 8 |
| POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | 7 |
| DAT - Data Lifecycle, Provenance, Receipts | 6 |
| DOC - Documentation, Doctrine, Reader Surfaces | 4 |
| REL - Catalog Closure, Publication, Release, Rollback, Recompile | 4 |
| SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | 4 |
| EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | 3 |
| SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | 3 |

---

## 12. Source-use distribution

| Source ID | Card count |
|---|---:|

| `SRC-ENCYC` | 81 |
| `SRC-P20` | 39 |
| `SRC-PIPE` | 21 |
| `SRC-GREEN` | 15 |
| `SRC-MAP` | 15 |
| `SRC-MAPMASTER` | 15 |
| `SRC-P18` | 12 |
| `SRC-DIR` | 9 |
| `SRC-GAI` | 6 |
| `SRC-ARCH` | 6 |
| `SRC-FAUNA` | 6 |
| `SRC-PEOPLE` | 6 |
| `SRC-NEW510` | 6 |
| `SRC-HABFAUNA` | 6 |
| `SRC-NEW515` | 6 |
| `SRC-NEW58` | 6 |
| `SRC-3DGIS` | 6 |
| `SRC-URBAN` | 6 |
| `SRC-TEMPORAL` | 3 |
| `SRC-GIS` | 3 |
| `SRC-UIAI` | 3 |
| `SRC-OLL` | 3 |
| `SRC-HYD` | 3 |
| `SRC-SOIL` | 3 |
| `SRC-HAB` | 3 |
| `SRC-FLORA` | 3 |
| `SRC-AGRI` | 3 |
| `SRC-GEO` | 3 |
| `SRC-ATM` | 3 |
| `SRC-HAZ` | 3 |
| `SRC-ROADS` | 3 |
| `SRC-SETTLE` | 3 |
| `SRC-APIREF` | 3 |
| `SRC-AIREF` | 3 |

---

## 13. Promotion and implementation rules

A candidate card may move toward implementation only when the implementing PR identifies:

1. Owning responsibility root.
2. Affected domain lane, if any.
3. Contract home, if semantic meaning changes.
4. Schema home, if machine shape changes.
5. Policy home, if allow/deny/restrict/abstain behavior changes.
6. Fixtures and negative cases.
7. Validator or test entry point.
8. Evidence/provenance/receipt impact.
9. Release/correction/rollback impact.
10. Documentation updates.
11. Security/sensitivity review.
12. Drift-register or ADR impact.

A card must not be treated as implemented merely because its Markdown exists.

---

## 14. Recommended first implementation slices

### Slice A — Inspectable claim envelope

Use cards:

- `KFM-CAND-0001`
- `KFM-CAND-0002`
- `KFM-CAND-0003`
- `KFM-CAND-0007`
- `KFM-CAND-0008`
- `KFM-CAND-0009`

Goal: define a minimal claim envelope that binds EvidenceRef, EvidenceBundle status, PolicyDecision, release state, correction lineage, and rollback reference.

### Slice B — SourceDescriptor admission

Use cards:

- `KFM-CAND-0004`
- `KFM-CAND-0005`
- `KFM-CAND-0006`
- `KFM-CAND-0094`
- `KFM-CAND-0095`
- `KFM-CAND-0096`

Goal: prove watcher-as-non-publisher and governed source admission without live publication.

### Slice C — Map renderer trust membrane

Use cards:

- `KFM-CAND-0028`
- `KFM-CAND-0029`
- `KFM-CAND-0030`
- `KFM-CAND-0088`
- `KFM-CAND-0089`
- `KFM-CAND-0090`

Goal: prove MapLibre and map artifacts are downstream of release, evidence, policy, and manifest checks.

### Slice D — Sensitive-domain deny path

Use cards:

- `KFM-CAND-0010`
- `KFM-CAND-0011`
- `KFM-CAND-0012`
- `KFM-CAND-0073`
- `KFM-CAND-0074`
- `KFM-CAND-0075`
- `KFM-CAND-0076`
- `KFM-CAND-0077`
- `KFM-CAND-0078`

Goal: prove exact-location deny/generalization patterns for archaeology and people/DNA/land before any public map exposure.

---

## 15. Validation checklist

Before merging this register:

- [ ] Confirm the final repository path.
- [ ] Check for duplicate prior atlas-card files.
- [ ] Check whether any card already has a real pass ID.
- [ ] Decide whether proposed extension categories require vocabulary ADR.
- [ ] Run Markdown lint.
- [ ] Run link check after adding repo links.
- [ ] Verify no exact sensitive locations are included.
- [ ] Verify no raw source data is embedded.
- [ ] Verify all implementation claims remain PROPOSED or UNKNOWN unless repo evidence supports them.
- [ ] Verify all path proposals are marked PROPOSED.
- [ ] Add this file to the appropriate docs index.
- [ ] Add a drift-register entry if the repo lacks an atlas-card register home.

---

## 16. JSONL candidate manifest

This manifest is generated from the optimized card register. It is **not canonical** until pass/ordinal allocation and `spec_hash` computation are performed.

```jsonl

{"candidate_key":"KFM-CAND-0001","triad_id":"KFM-TRIAD-001","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Inspectable Claim Operating Law Pattern","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-GREEN","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat the inspectable claim as the durable unit of public value across maps, tiles, graphs, AI answers, dashboards, and exports.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0002","triad_id":"KFM-TRIAD-001","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Inspectable Claim Operating Law Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-GREEN","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose claim-level evidence, temporal scope, spatial scope, source role, policy posture, review state, release state, and correction lineage wherever a public surface makes or implies a consequential claim.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0003","triad_id":"KFM-TRIAD-001","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Inspectable Claim Operating Law Implementation Surface","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-GREEN","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define a claim envelope contract that binds EvidenceRef, EvidenceBundle status, policy decision, release state, correction lineage, and rollback reference before publication.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0004","triad_id":"KFM-TRIAD-002","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"SourceDescriptor Admission Control Pattern","category":"SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-PIPE","SRC-DIR"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should make source admission a governed decision that records source role, rights posture, sensitivity posture, update cadence, authority class, and permitted use before data enters the lifecycle.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0005","triad_id":"KFM-TRIAD-002","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"SourceDescriptor Admission Control Capability","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-PIPE","SRC-DIR"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should give stewards a source-intake and source-health view that distinguishes admissible sources, quarantined sources, context-only sources, and denied sources.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0006","triad_id":"KFM-TRIAD-002","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"SourceDescriptor Admission Control Implementation Surface","category":"SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-PIPE","SRC-DIR"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement SourceDescriptor, SourceIntakeRecord, SourceHealthCheck, and source-role validators as controlled inputs to connectors and watchers.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0007","triad_id":"KFM-TRIAD-003","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Evidence Closure Pattern","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should require EvidenceRef to resolve to an EvidenceBundle before a claim is answered, rendered as authoritative, exported, or promoted.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0008","triad_id":"KFM-TRIAD-003","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Evidence Closure Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should surface evidence closure, missing evidence, abstention reasons, and withheld-evidence posture in the Evidence Drawer and Focus Mode response envelope.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0009","triad_id":"KFM-TRIAD-003","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Evidence Closure Implementation Surface","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement a CitationValidationReport and EvidenceResolutionReport that produce finite ANSWER, ABSTAIN, DENY, or ERROR outcomes.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0010","triad_id":"KFM-TRIAD-004","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Policy-Safe Exposure Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-DIR","SRC-ARCH","SRC-FAUNA","SRC-PEOPLE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should fail closed when rights, sovereignty, cultural sensitivity, living-person data, DNA/genomics, rare species, archaeology, infrastructure, private land, or precise-location exposure is unclear.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0011","triad_id":"KFM-TRIAD-004","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Policy-Safe Exposure Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-DIR","SRC-ARCH","SRC-FAUNA","SRC-PEOPLE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should present redaction, denial, generalization, staged access, stale state, and abstention as explicit trust-visible states rather than hidden implementation details.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0012","triad_id":"KFM-TRIAD-004","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Policy-Safe Exposure Implementation Surface","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-DIR","SRC-ARCH","SRC-FAUNA","SRC-PEOPLE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement policy decision contracts and fail-closed validators that block release when rights, source terms, sensitivity review, or access posture is unresolved.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0013","triad_id":"KFM-TRIAD-005","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Time-Aware Spatial Semantics Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P18","SRC-TEMPORAL","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model valid time, observed time, source time, retrieval time, release time, and correction time as distinct dimensions where the distinction affects evidence or interpretation.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0014","triad_id":"KFM-TRIAD-005","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Time-Aware Spatial Semantics Capability","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P18","SRC-TEMPORAL","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should disclose temporal query mode, time window, geography version, uncertainty class, and fitness-for-use for public analytical and map-facing outputs.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0015","triad_id":"KFM-TRIAD-005","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Time-Aware Spatial Semantics Implementation Surface","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P18","SRC-TEMPORAL","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement temporal_scope, geography_version, query_receipt, and temporal_query_mode fields in relevant runtime and evidence contracts.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0016","triad_id":"KFM-TRIAD-006","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Responsibility-Root Governance Pattern","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-DIR","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat path placement as governance because a file location encodes responsibility root, lifecycle phase, and authority boundary.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0017","triad_id":"KFM-TRIAD-006","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Responsibility-Root Governance Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-DIR","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide reviewers a path-placement checklist that marks proposed homes, required ADRs, drift risks, and rollback or migration notes.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0018","triad_id":"KFM-TRIAD-006","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Responsibility-Root Governance Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-DIR","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement directory-rule linting and path-proposal validation for contracts, schemas, policies, release artifacts, proofs, receipts, source registries, and domain lanes.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0019","triad_id":"KFM-TRIAD-007","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Validation Gate Lattice Pattern","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-PIPE","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat validation, QA, observability, and reliability as part of publication truth rather than as post-release hygiene.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0020","triad_id":"KFM-TRIAD-007","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Validation Gate Lattice Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-PIPE","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose validation status, freshness status, source-health status, denied state, degraded state, and rollback readiness to reviewers and, where safe, public users.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0021","triad_id":"KFM-TRIAD-007","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Validation Gate Lattice Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ENCYC","SRC-P20","SRC-PIPE","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement no-network fixture tests, schema validators, policy validators, visual regression checks, material-change tests, and receipt completeness checks as release gates.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0022","triad_id":"KFM-TRIAD-008","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Receipts and Proof Objects Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GREEN","SRC-P20","SRC-MAPMASTER","SRC-NEW510"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should pair receipts and proof objects so every intake, transform, catalog, map-artifact build, AI response, and release can be reconstructed and challenged.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0023","triad_id":"KFM-TRIAD-008","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Receipts and Proof Objects Capability","category":"REL - Catalog Closure, Publication, Release, Rollback, Recompile","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GREEN","SRC-P20","SRC-MAPMASTER","SRC-NEW510"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect run receipts, promotion receipts, proof packs, content hashes, signature state, attestation references, and rollback targets before release.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0024","triad_id":"KFM-TRIAD-008","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Receipts and Proof Objects Implementation Surface","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GREEN","SRC-P20","SRC-MAPMASTER","SRC-NEW510"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement RunReceipt, PromotionReceipt, MerkleManifest, DSSE or equivalent signed envelope, spec_hash, and attestation validators for release-critical actions.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0025","triad_id":"KFM-TRIAD-009","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Governed Release State Pattern","category":"REL - Catalog Closure, Publication, Release, Rollback, Recompile","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GREEN","SRC-PIPE","SRC-P20","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat promotion as a governed state transition backed by validation, policy, review, proof, catalog, release manifest, correction path, and rollback target.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0026","triad_id":"KFM-TRIAD-009","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Governed Release State Capability","category":"REL - Catalog Closure, Publication, Release, Rollback, Recompile","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GREEN","SRC-PIPE","SRC-P20","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide release and correction surfaces that show what changed, why it changed, what evidence supports it, and how to roll it back or supersede it.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0027","triad_id":"KFM-TRIAD-009","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Governed Release State Implementation Surface","category":"REL - Catalog Closure, Publication, Release, Rollback, Recompile","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GREEN","SRC-PIPE","SRC-P20","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement PromotionDecision, ReleaseManifest, CatalogClosureReport, CorrectionNotice, WithdrawalRecord, and RollbackCard as separate but linked artifact families.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0028","triad_id":"KFM-TRIAD-010","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Renderer-Downstream Map Law Pattern","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAP","SRC-MAPMASTER","SRC-ENCYC","SRC-P18"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should keep MapLibre downstream of evidence, policy, review, and release state rather than letting rendered pixels, feature properties, or layer visibility become truth authority.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0029","triad_id":"KFM-TRIAD-010","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Renderer-Downstream Map Law Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAP","SRC-MAPMASTER","SRC-ENCYC","SRC-P18"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show released, stale, degraded, denied, context-only, generalized, and withheld states directly in map layers, popups, Evidence Drawer links, and export paths.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0030","triad_id":"KFM-TRIAD-010","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Renderer-Downstream Map Law Implementation Surface","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAP","SRC-MAPMASTER","SRC-ENCYC","SRC-P18"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement LayerManifest, StyleManifest, TileArtifactManifest, MapReleaseManifest, MapContextEnvelope, and no-direct-RAW/WORK/QUARANTINE checks for map sources.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0031","triad_id":"KFM-TRIAD-011","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Trust-Visible Interaction Pattern","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAP","SRC-UIAI","SRC-ENCYC","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should make the UI part of the trust model by exposing evidence, policy, review, release, stale, correction, and abstention state at the point of use.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0032","triad_id":"KFM-TRIAD-011","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Trust-Visible Interaction Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAP","SRC-UIAI","SRC-ENCYC","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide Evidence Drawer, Focus Mode, Story Node, Compare, Review, Dossier, and Export affordances that never bypass governed APIs.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0033","triad_id":"KFM-TRIAD-011","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Trust-Visible Interaction Implementation Surface","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAP","SRC-UIAI","SRC-ENCYC","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement EvidenceDrawerPayload, FocusModeEnvelope, StoryManifest, ReviewHandoff, TrustStateBadge, and accessibility/performance validation surfaces.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0034","triad_id":"KFM-TRIAD-012","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Evidence-Subordinate AI Pattern","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GAI","SRC-OLL","SRC-MAP","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat AI as interpretive and provider-neutral, with EvidenceBundle, policy decision, review state, citation validation, and finite outcomes outranking model language.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0035","triad_id":"KFM-TRIAD-012","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Evidence-Subordinate AI Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GAI","SRC-OLL","SRC-MAP","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let Focus Mode answer only over released or admissible evidence context and should make ABSTAIN, DENY, and ERROR first-class outcomes.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0036","triad_id":"KFM-TRIAD-012","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Evidence-Subordinate AI Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GAI","SRC-OLL","SRC-MAP","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement MockAdapter-first runtime contracts, RuntimeResponseEnvelope, AIReceipt, CitationValidationReport, and no-direct-model-client checks before any live runtime adapter.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0037","triad_id":"KFM-TRIAD-013","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Governed Recompile Loop Pattern","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-PIPE","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement the incremental query-save-validate-compile-review-promote-recompile loop as a governed learning and recompilation lane, not as autonomous self-modification.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0038","triad_id":"KFM-TRIAD-013","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Governed Recompile Loop Capability","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-PIPE","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let maintainers inspect QueryRunRecord, EvidenceResolutionRecord, CandidateDelta, RecompileManifest, LoopValidationReport, LoopDecision, and rollback references.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0039","triad_id":"KFM-TRIAD-013","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Governed Recompile Loop Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-PIPE","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement dry-run compilers, loop-control schemas, no-autopublish policy gates, and loop fixtures before live source or model integration.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0040","triad_id":"KFM-TRIAD-014","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Hydrology Proof Lane Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HYD","SRC-ENCYC","SRC-PIPE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat hydrology as a proof-bearing domain lane that distinguishes watershed identity, hydrography networks, observations, regulatory flood context, terrain-derived context, and public-safe map products.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0041","triad_id":"KFM-TRIAD-014","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Hydrology Proof Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HYD","SRC-ENCYC","SRC-PIPE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should support watershed, HUC, streamflow, flood-context, hydrograph, layer-evidence, and source-freshness views that resolve to evidence and source role.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0042","triad_id":"KFM-TRIAD-014","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Hydrology Proof Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HYD","SRC-ENCYC","SRC-PIPE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement hydrology SourceDescriptors, HUC fixtures, observation normalization, hydrograph evidence bundles, layer manifests, and validation gates before public release.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0043","triad_id":"KFM-TRIAD-015","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Soil Evidence Lane Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-SOIL","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model soil surveys, map units, horizons, properties, soil-moisture context, and derived suitability products as evidence-bound objects with source-role limits.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0044","triad_id":"KFM-TRIAD-015","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Soil Evidence Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-SOIL","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose soil properties, uncertainty, source date, survey lineage, cross-domain links to hydrology/agriculture, and public-safe map layers.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0045","triad_id":"KFM-TRIAD-015","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Soil Evidence Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-SOIL","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement soil source descriptors, soil map-unit schemas, horizon/property validators, snapshot receipts, and tile/catalog artifacts with rollback targets.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0046","triad_id":"KFM-TRIAD-016","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Habitat Evidence Lane Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HAB","SRC-HABFAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should represent habitat patches, suitability, connectivity, restoration context, disturbance state, and habitat assignment as evidence-supported claims rather than unconstrained model outputs.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0047","triad_id":"KFM-TRIAD-016","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Habitat Evidence Lane Capability","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HAB","SRC-HABFAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let users inspect habitat assignment evidence, model support, uncertainty class, stewardship posture, and public-safe derived maps.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0048","triad_id":"KFM-TRIAD-016","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Habitat Evidence Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HAB","SRC-HABFAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement habitat schemas, habitat-fauna join fixtures, model-support validators, sensitivity gates, and EvidenceDrawer payloads for habitat assignment.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0049","triad_id":"KFM-TRIAD-017","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Fauna Public-Safety Lane Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-FAUNA","SRC-HABFAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should distinguish taxonomy, occurrence evidence, conservation status, range, seasonal range, habitat support, disease/mortality evidence, and public-safe derivatives in the fauna lane.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0050","triad_id":"KFM-TRIAD-017","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Fauna Public-Safety Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-FAUNA","SRC-HABFAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose generalized or redacted fauna layers, evidence drawer explanations, steward review state, and geoprivacy reasons where exact public exposure is unsafe.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0051","triad_id":"KFM-TRIAD-017","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Fauna Public-Safety Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-FAUNA","SRC-HABFAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement taxon resolution, occurrence sensitivity classification, source-role constraints, generalized layer manifests, and geoprivacy validators.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0052","triad_id":"KFM-TRIAD-018","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Flora Public-Safety Lane Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-FLORA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should manage flora observations, specimens, taxonomic identity, rare-plant controls, modeled surfaces, and public visualizations as separate evidence and release objects.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0053","triad_id":"KFM-TRIAD-018","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Flora Public-Safety Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-FLORA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show flora evidence, taxonomic confidence, status context, redaction posture, steward review, and generalized map outputs when public exposure is permitted.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0054","triad_id":"KFM-TRIAD-018","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Flora Public-Safety Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-FLORA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement flora source descriptors, taxon identifiers, occurrence/geoprivacy schemas, sensitivity gates, and public-safe artifact validators.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0055","triad_id":"KFM-TRIAD-019","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Agriculture and Landcover Watchers Pattern","category":"SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-AGRI","SRC-NEW515","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat cropland, landcover, agriculture statistics, crop-class changes, and PLANTS package deltas as governed signals that propose work rather than auto-publish changes.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0056","triad_id":"KFM-TRIAD-019","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Agriculture and Landcover Watchers Capability","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-AGRI","SRC-NEW515","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose county-level material-change records, class histograms, threshold reasons, source heads, and proposed-work status to reviewers.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0057","triad_id":"KFM-TRIAD-019","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Agriculture and Landcover Watchers Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-AGRI","SRC-NEW515","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement CDL/PLANTS sidecars, spec_hash computation, materiality thresholds, watcher events, PROPOSED_WORK_RECORD outbox artifacts, and validator gates.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0058","triad_id":"KFM-TRIAD-020","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Geology Resource Evidence Lane Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GEO","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should distinguish bedrock, surficial geology, stratigraphy, structures, geomorphology, borehole evidence, resource estimates, extraction records, and public-safe geology layers.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0059","triad_id":"KFM-TRIAD-020","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Geology Resource Evidence Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GEO","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let users inspect geology/resource claims by source role, evidence type, spatial precision, interpretation class, release state, and cross-domain linkage.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0060","triad_id":"KFM-TRIAD-020","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Geology Resource Evidence Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-GEO","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement geology SourceDescriptors, stratigraphic and lithologic object schemas, public-safe geometry rules, catalog artifacts, and validation fixtures.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0061","triad_id":"KFM-TRIAD-021","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Atmosphere Knowledge-Character Lane Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ATM","SRC-NEW58","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should distinguish observations, public AQI context, regulatory archives, model fields, smoke masks, anomaly surfaces, and fusion products in the atmosphere and air lane.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0062","triad_id":"KFM-TRIAD-021","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Atmosphere Knowledge-Character Lane Capability","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ATM","SRC-NEW58","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show air-quality context, freshness, preliminary status, parameter meaning, source-role limits, and knowledge-character labels for map and analysis outputs.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0063","triad_id":"KFM-TRIAD-021","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Atmosphere Knowledge-Character Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ATM","SRC-NEW58","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement atmosphere parameter registries, source-health probes, AOD/FIRMS/SMAP/AirNow/Mesonet decision envelopes, and fail-closed source-rights gates.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0064","triad_id":"KFM-TRIAD-022","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Hazards Without Emergency Alerting Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HAZ","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should support hazards history, regulatory context, operational context, observations, detections, models, and resilience review without becoming an emergency alert system.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0065","triad_id":"KFM-TRIAD-022","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Hazards Without Emergency Alerting Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HAZ","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose hazard evidence, freshness, expiry, operational-context disclaimers, source authority, and official-source routing where life-safety action is requested.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0066","triad_id":"KFM-TRIAD-022","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Hazards Without Emergency Alerting Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-HAZ","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement hazard source-role descriptors, event/observation/model separation, not-for-life-safety policy checks, and finite DENY/ABSTAIN behavior for unsafe requests.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0067","triad_id":"KFM-TRIAD-023","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Transport Corridor Evidence Lane Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ROADS","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model modern roads, historic roads, rail corridors, trade routes, movement corridors, facilities, restrictions, and graph projections without equating geometry with authority.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0068","triad_id":"KFM-TRIAD-023","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Transport Corridor Evidence Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ROADS","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let users inspect route evidence, temporal status, generalized historic geometry, operator or jurisdiction assertions, access restrictions, and public-safe corridor maps.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0069","triad_id":"KFM-TRIAD-023","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Transport Corridor Evidence Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ROADS","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement transport object schemas, temporal event records, graph projection manifests, sensitive-corridor generalization rules, and EvidenceDrawer payloads.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0070","triad_id":"KFM-TRIAD-024","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Settlement and Infrastructure Evidence Lane Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-SETTLE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model settlements, municipalities, census places, historic townsites, infrastructure assets, networks, operators, condition observations, dependencies, and public-safe representations separately.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0071","triad_id":"KFM-TRIAD-024","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Settlement and Infrastructure Evidence Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-SETTLE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose settlement identity, alternative names, legal status, infrastructure condition, service areas, dependencies, sensitivity flags, and review posture.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0072","triad_id":"KFM-TRIAD-024","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Settlement and Infrastructure Evidence Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-SETTLE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement settlement and infrastructure schemas, stable identity helpers, source descriptors, deny policies for sensitive assets, and public-safe layer manifests.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0073","triad_id":"KFM-TRIAD-025","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Archaeology Exact-Location Deny Lane Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ARCH","SRC-3DGIS","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat archaeological records, remote-sensing anomalies, 3D interpretations, site claims, artifacts, cultural review, and public maps as governed evidence objects with exact-location denial by default.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0074","triad_id":"KFM-TRIAD-025","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Archaeology Exact-Location Deny Lane Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ARCH","SRC-3DGIS","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose reviewed generalized archaeology layers, sensitivity reasons, steward review state, evidence confidence, and interpretation limits without disclosing unsafe exact locations.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0075","triad_id":"KFM-TRIAD-025","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Archaeology Exact-Location Deny Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-ARCH","SRC-3DGIS","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement archaeology sensitivity policies, anomaly-versus-confirmed-site schemas, geoprivacy transforms, transform receipts, and public-output validators.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0076","triad_id":"KFM-TRIAD-026","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"People DNA Land Safety Lane Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-PEOPLE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should represent people assertions, relationship hypotheses, DNA-derived evidence, land ownership assertions, and parcel or assessor context as evidence-bound and policy-sensitive records.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0077","triad_id":"KFM-TRIAD-026","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"People DNA Land Safety Lane Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-PEOPLE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should distinguish historical research, living-person restrictions, DNA restrictions, title evidence limits, parcel geometry caveats, and relationship hypothesis confidence in public and reviewer views.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0078","triad_id":"KFM-TRIAD-026","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"People DNA Land Safety Lane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-PEOPLE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement assertion-first people/land schemas, living-person and DNA denial policies, temporal land-ownership assertions, relationship evidence validators, and restricted-access payloads.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0079","triad_id":"KFM-TRIAD-027","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Participatory Planning Support Pattern","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-URBAN","SRC-ENCYC","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should support planning, participation, resilience, equity, scenarios, and decision support as evidence-informed interpretation rather than automatic recommendation authority.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0080","triad_id":"KFM-TRIAD-027","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Participatory Planning Support Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-URBAN","SRC-ENCYC","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide scenario views, indicator dashboards, stakeholder notes, uncertainty labels, equity context, and evidence-backed planning explanations.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0081","triad_id":"KFM-TRIAD-027","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Participatory Planning Support Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-URBAN","SRC-ENCYC","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement scenario manifests, indicator definition contracts, stakeholder-input receipts, equity/sensitivity checks, and decision-support validation reports.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0082","triad_id":"KFM-TRIAD-028","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Field and 3D Capture Governance Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-3DGIS","SRC-P18","SRC-ENCYC","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat field capture, remote sensing, 3D models, LiDAR, terrain, drone data, and archaeological visualization as evidence carriers with acquisition, processing, interpretation, and sensitivity metadata.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0083","triad_id":"KFM-TRIAD-028","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Field and 3D Capture Governance Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-3DGIS","SRC-P18","SRC-ENCYC","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose acquisition method, processing lineage, interpretation status, dimensional caveats, view limits, and public-safe 2D or 3D representations.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0084","triad_id":"KFM-TRIAD-028","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Field and 3D Capture Governance Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-3DGIS","SRC-P18","SRC-ENCYC","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement capture receipts, 3D/remote-sensing source descriptors, model/scene manifests, georeferencing validators, and sensitivity gates for exact or high-resolution outputs.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0085","triad_id":"KFM-TRIAD-029","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Governed API Contract Membrane Pattern","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-APIREF","SRC-P20","SRC-MAP","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should make APIs the governed trust membrane between public surfaces and internal stores, rather than exposing canonical or lifecycle stores directly.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0086","triad_id":"KFM-TRIAD-029","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Governed API Contract Membrane Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-APIREF","SRC-P20","SRC-MAP","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide evidence-backed resource responses, finite negative outcomes, release-state filters, citation validation, and review-safe payloads for UI, map, export, and Focus Mode clients.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0087","triad_id":"KFM-TRIAD-029","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Governed API Contract Membrane Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-APIREF","SRC-P20","SRC-MAP","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement OpenAPI-like contracts, runtime envelopes, resource lifecycle response codes, no-raw-public-route checks, and response validators.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0088","triad_id":"KFM-TRIAD-030","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Interpretive Analytics Governance Pattern","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-AIREF","SRC-P18","SRC-ENCYC","SRC-URBAN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat analytics, indicators, statistics, machine learning, and model interpretation as derived and explainable outputs that remain subordinate to evidence and policy.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0089","triad_id":"KFM-TRIAD-030","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Interpretive Analytics Governance Capability","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-AIREF","SRC-P18","SRC-ENCYC","SRC-URBAN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should disclose model inputs, assumptions, uncertainty, validation status, training or source lineage, confidence class, and interpretation limits for analytic outputs.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0090","triad_id":"KFM-TRIAD-030","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Interpretive Analytics Governance Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-AIREF","SRC-P18","SRC-ENCYC","SRC-URBAN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement ModelRunReceipt, IndicatorDefinition, FeatureSetManifest, ValidationReport, and model-output policy checks before any public analytic result is published.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0091","triad_id":"KFM-TRIAD-031","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Map Artifact Integrity Pattern","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAPMASTER","SRC-NEW510","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat PMTiles, COGs, GeoParquet, style JSON, and rendered previews as release artifacts whose integrity, provenance, and rollback readiness must be inspectable.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0092","triad_id":"KFM-TRIAD-031","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Map Artifact Integrity Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAPMASTER","SRC-NEW510","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect artifact root hashes, byte-range manifests, sidecars, signatures, tool versions, input digests, source ledger references, and release manifest links.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0093","triad_id":"KFM-TRIAD-031","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Map Artifact Integrity Implementation Surface","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-MAPMASTER","SRC-NEW510","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement PMTiles/COG sidecar schemas, BLAKE3 or equivalent roots, byte-range proofs, signed attestations, artifact validators, and no-in-place-overwrite release checks.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0094","triad_id":"KFM-TRIAD-032","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Watcher-as-Non-Publisher Pattern","category":"SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension)","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-NEW58","SRC-NEW515","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let watchers detect material source changes and source-health shifts while preventing watchers from publishing or committing directly to canonical release state.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0095","triad_id":"KFM-TRIAD-032","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Watcher-as-Non-Publisher Capability","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-NEW58","SRC-NEW515","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose proposed work records, source-head diffs, threshold breaches, persistence windows, license failures, and review status to maintainers.","implementation_status":"UNKNOWN"}
{"candidate_key":"KFM-CAND-0096","triad_id":"KFM-TRIAD-032","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Watcher-as-Non-Publisher Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"EXPANDED","source_ids":["SRC-NEW58","SRC-NEW515","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement watcher sidecars, HEAD/ETag probes, Last-Modified capture, materiality rules, signed run receipts, proposed-work outboxes, and default-deny policy gates.","implementation_status":"UNKNOWN"}
```

---

## 17. Changelog

| Version | Date | Change |
|---|---:|---|
| v0.2 | 2026-06-12 | Optimized pasted seed-card draft into deduplicated triad register with source ledger, shared controls, category/source distributions, candidate keys, implementation slices, and JSONL manifest. |
| v0.1 | unknown | Original pasted seed-card draft with 96 repeated card entries and placeholder pass/ordinal IDs. |

---

## 18. Footer

```yaml
kfm_footer:
  document: "KFM Atlas Seed Cards — Optimized Carry-Forward Register"
  version: "v0.2"
  status: "draft"
  authority_class: "candidate-card register / synthesis; not canonical doctrine"
  requested_path: null
  suggested_repository_home: "docs/atlases/kfm-atlas-seed-cards.md"
  suggested_repository_home_status: "PROPOSED"
  card_count: 96
  triad_count: 32
  implementation_claims: "UNKNOWN unless separately verified"
  stable_id_policy: "placeholder IDs retained until PASS and ordinal assignment"
  spec_hash_policy: "pending canonical JCS + SHA-256 computation"
  review_required:
    - "Atlas steward"
    - "Docs steward"
    - "Evidence steward"
    - "Domain steward for affected lane"
    - "Policy steward for sensitivity/release-impacting cards"
```

**Authority reminder:** This register does not supersede KFM doctrine, Directory Rules, accepted ADRs, contracts, schemas, policy, release manifests, proof objects, or verified repository evidence.
