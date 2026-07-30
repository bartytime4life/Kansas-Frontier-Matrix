<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/kfm-atlas-seed-cards-optimized
title: KFM Atlas Seed Cards — Optimized Carry-Forward Register
type: atlas_card_register
version: v0.6
status: draft
owners: <PLACEHOLDER — Atlas steward · Docs steward · Evidence steward · Domain stewards>
created: 2026-06-12
updated: 2026-07-29
policy_label: public
authority_class: synthesis / candidate-card register; NOT canonical doctrine
requested_path: docs/kfm_full_atlas_seed_cards.md
current_repository_home: docs/kfm_full_atlas_seed_cards.md
current_repository_home_status: CONFIRMED at main 5266ba5f2d8f39cad2d54b066d514be8ca8eb3b7; retained in place to preserve identity and avoid a parallel atlas carrier.
truth_posture: cite-or-abstain with explicit truth labels
implementation_boundary: remote main was inspected at snapshot 5266ba5f2d8f39cad2d54b066d514be8ca8eb3b7; hosted CI for this proposed change, release state, dashboards, deployments, and runtime behavior remain NEEDS VERIFICATION unless separately verified.
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/atlases/
  - docs/domains/
  - docs/intake/exploratory/new-ideas-4-14-source-map.md
  - docs/intake/exploratory/new-ideas-4-15-source-map.md
  - docs/intake/exploratory/new-ideas-4-16-source-map.md
  - docs/intake/exploratory/new-ideas-4-23-source-map.md
  - docs/intake/exploratory/new-ideas-4-25-source-map.md
  - docs/intake/exploratory/new-ideas-4-30-source-map.md
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
  - "v0.3 — adds 30 packet-local cards in 10 triads from New Ideas 4-16-26, reconciles them against the pinned remote-main snapshot, and fills cross-cutting gaps without promoting packet code or paths."
  - "v0.4 — adds 33 packet-local cards in 11 triads from New Ideas 4-30-26, focused on retrieval intent, rights drift, sampling support, distribution meaning, coverage bias, measurement reconciliation, delivery latency, asynchronous transfers, offline trust, verified rendering, and confounder-aware fitness."
  - "v0.5 — adds 30 packet-local cards in 10 triads from New Ideas 4-23-26 and New Ideas 4-25-26, focused on custody, composed-claim closure, trust-root history, replay-safe effects, obligations, reversible reconciliation, taxonomic concepts, place-name authority, survey-control provenance, and adversarial validator assurance."
  - "v0.6 — reconciles the Pass 23 source packets New Ideas 4-14-26 and New Ideas 4-15-26 against current repository evidence and adds 21 cards in 7 triads focused on bitemporal verification replay, source-conflict influence, cross-layer outcome parity, verifier portability, quality translation, runtime-proof artifact lifecycle, and interface evolution."
  - "The original draft repeated shared dependencies, tensions, open questions, and self-check text in every card. This edition deduplicates those into shared sections while preserving every card topic, class, category, source-ID set, and normalized statement."
  - "Stable IDs intentionally remain templates until PASS and ordinal allocation are supplied."
] -->

# KFM Atlas Seed Cards — Optimized Carry-Forward Register

> **Status:** Draft candidate-card register  
> **Authority:** Synthesis / candidate backlog, not canonical doctrine  
> **Input shape:** 210 card entries arranged as 70 idea/feature/programming triads
> **Core posture:** evidence-first · map-first · time-aware · cite-or-abstain · fail-closed · auditable · reversible

---

## 0. Reader note

This document optimizes the supplied KFM seed-card draft into a maintainable repository-facing register.

The source draft already used KFM truth labels and included required card fields. The main problem was maintainability: every card repeated the same dependency, tension, open-question, carry-forward, and self-check language. This edition preserves the card content but moves repeated control language into shared sections and appends only repository-reconciled packet gaps.

This is a **candidate register**, not an implementation claim. The gap passes were reconciled against remote `main@5266ba5f2d8f39cad2d54b066d514be8ca8eb3b7`, but no card here proves later repository state, hosted enforcement, release state, deployment, or runtime behavior.

---

## 1. Optimization summary

| Item | Result |
|---|---:|
| Original v0.2 card count | 96 |
| New 4-16 gap-fill cards | 30 |
| New 4-30 gap-fill cards | 33 |
| New 4-23 gap-fill cards | 15 |
| New 4-25 gap-fill cards | 15 |
| New 4-14/4-15 reconciled gap-fill cards | 21 |
| Current card count | 210 |
| Triad count | 70 |
| Idea cards | 70 |
| Feature cards | 70 |
| Programming cards | 70 |
| Stable ID posture | Template retained: `KFM-P{PASS}-{CLASS}-{NNNN}` |
| Spec hash posture | `PROPOSED` until canonical JCS + SHA-256 computation |
| Repository implementation maturity | `PARTIAL` at remote `main@5266ba5…`; hosted CI significance for this proposed change, releases, deployments, and runtime remain `NEEDS VERIFICATION` |
| Primary optimization | Deduplicated repeated control text; preserved normalized statements and source IDs |
| Current repo home | `docs/kfm_full_atlas_seed_cards.md` — **CONFIRMED** at the pinned snapshot |

---

## 2. Directory and placement posture

**Current path:** `docs/kfm_full_atlas_seed_cards.md`

**Status:** **CONFIRMED** at remote `main@5266ba5f2d8f39cad2d54b066d514be8ca8eb3b7`.

**Directory Rules basis:** this is a human-facing synthesis and candidate register, so `docs/` owns it. The existing file is updated in place to preserve document identity and stable links. It must not be copied into a second writable atlas home or placed under `schemas/`, `contracts/`, `policy/`, `release/`, `data/`, `fixtures/`, or `tests/` because it is not a machine schema, semantic contract, policy bundle, release artifact, data artifact, fixture, or test.

No move or alias is proposed by this update. A later relocation would require an independently reviewed migration with inbound-link, compatibility, correction, and rollback evidence.

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
KFM-CAND-0001 ... KFM-CAND-0210
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
- **CONFIRMED at the pinned remote-main snapshot:** KFM already contains substantial contract, schema, validator, source, policy-documentation, UI-boundary, PMTiles, STAC, receipt, release, and domain-lane surfaces. Their presence does not prove complete or hosted enforcement.
- **NEEDS VERIFICATION:** Current remote-main bytes, accepted authority for draft or proposed artifacts, required hosted checks, release state, deployments, and runtime behavior.
- **PROPOSED:** Candidate source packets sometimes contain implementation-like examples; examples are not repo proof.
- **PROPOSED:** A card may be doctrine-aligned and still not be release-ready.
- **PROPOSED:** A card may be implementation-worthy and still require rights, sensitivity, policy, and reviewer approval before exposure.

---

## 7. Shared open questions

- **NEEDS VERIFICATION:** Which workspace-present files, schemas, policies, tests, receipts, proofs, release manifests, API routes, or UI surfaces are current on remote main and actually enforce each card?
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
| `SRC-AIREF` | AI Concepts Using Python; role: AI/data/ML workflow reference. Used by 12 cards. |
| `SRC-APIREF` | Designing Great Web APIs; role: API contract and resource lifecycle reference. Used by 3 cards. |
| `SRC-ARCH` | KFM Archaeology Architecture Plan; role: archaeology lane and exact-location deny posture. Used by 6 cards. |
| `SRC-ATM` | KFM Atmosphere / Air Architecture Report; role: air/climate/smoke/EO lane blueprint. Used by 24 cards. |
| `SRC-DIR` | Directory Rules; role: placement doctrine; basis: responsibility roots, schema-home convention, lifecycle invariant, ADR/drift rules. Used by 12 cards. |
| `SRC-ENCYC` | KFM Domain and Capability Encyclopedia; role: all-domain and cross-domain capability atlas; basis: operating law and domain inventory. Used by 135 cards. |
| `SRC-FAUNA` | KFM Fauna Architecture PDF-Only Report; role: fauna domain lane and geoprivacy blueprint. Used by 21 cards. |
| `SRC-FLORA` | KFM Flora Architecture PDF-Only Implementation Blueprint; role: flora domain lane and rare-location controls. Used by 12 cards. |
| `SRC-GAI` | KFM Governed AI Extended Pro Source Ledger Report; role: provider-neutral governed AI design and finite outcomes. Used by 30 cards. |
| `SRC-GEO` | KFM Geology and Natural Resources Architecture Report; role: geology/natural resources domain lane blueprint. Used by 3 cards. |
| `SRC-GIS` | A Primer of GIS; role: geographic/cartographic representation reference. Used by 12 cards. |
| `SRC-GREEN` | Kansas Frontier Matrix Definitive Greenfield Building Plan v1.1; role: trust spine and build principles; basis: lifecycle, object families, receipts, promotion, and anti-patterns. Used by 54 cards. |
| `SRC-HAB` | KFM Habitat Architecture Implementation Blueprint; role: habitat domain lane blueprint. Used by 3 cards. |
| `SRC-HABFAUNA` | KFM Habitat + Fauna Thin-Slice Extended Pro Blueprint; role: habitat/fauna fixture-first proof slice. Used by 6 cards. |
| `SRC-HAZ` | KFM Hazards Architecture Extended Pro Blueprint; role: hazards lane and non-emergency-alerting boundary. Used by 3 cards. |
| `SRC-HYD` | KFM Hydrology Extended Pro Reference Report; role: hydrology domain lane blueprint. Used by 9 cards. |
| `SRC-MAP` | KFM MapLibre Operating Architecture, Governed UI, and AI Interaction Manual; role: map renderer boundary and trust-visible UI doctrine. Used by 30 cards. |
| `SRC-MAPMASTER` | Master MapLibre Components-Functions-Features; role: cumulative MapLibre/tile/artifact atlas; basis: tile, style, manifest, PMTiles/COG, and validation ideas. Used by 33 cards. |
| `SRC-NEW414` | New Ideas 4-14-26; role: exploratory watcher, policy, hydrology-identity, promotion, verification-history, conflict, and runtime-trust packet; identity: SHA-256 `432c5930b66fac814b21680c60015cff2eb286520ec01211bef69c0c78117f3e`, 410 pages; prior Pass 23 source `SRC-P23-003`. Used by 15 new gap-fill cards. |
| `SRC-NEW415` | New Ideas 4-15-26; role: exploratory soil, HLS/STAC, people/consent, time-aware map, runtime-proof, watcher, and contract packet; identity: SHA-256 `fb3af560b6698f41d3b75aa7bffe96be07aeb2ba2fb356219886ceda7eea2111`, 435 pages; prior Pass 23 source `SRC-P23-004`. Used by 15 new gap-fill cards. |
| `SRC-NEW416` | New Ideas 4-16-26; role: exploratory governed-ingest, baseline, anomaly, consent, temporal-map, artifact-integrity, catalog-profile, and historical-network packet; identity: SHA-256 `73e10e3c75c1f3cbbd49641b33bddfde93895b85c7562af3dbe161cf2d4c6c16`, 110 pages. Used by 30 new gap-fill cards. |
| `SRC-NEW423` | New Ideas 4-23-26; role: exploratory evidence-custody, composed-claim, signing, trust-root, event-replay, review-obligation, hydrology, ecology, and consent packet; identity: SHA-256 `76ace3bc49dbfa92aa8d48bd3bcac0871b1b1da8c91006d7ac6a318f0cacfc2d`, 652 pages. Used by 15 new gap-fill cards. |
| `SRC-NEW425` | New Ideas 4-25-26; role: exploratory biodiversity, evidence, PLSS/GLO, taxonomy, place-name, validation, AI, watcher, and consent packet; identity: SHA-256 `47983cd76db4d3c0e971c61d6259f80f32ca861091d7f65020ad94c09ce76061`, 337 pages. Used by 15 new gap-fill cards. |
| `SRC-NEW430` | New Ideas 4-30-26; role: exploratory flora/fauna intake, environmental fusion, retrieval, policy, catalog, map-artifact, offline-delivery, and validator packet; identity: SHA-256 `3d7585dd43009c14fa7ae9cec864bb0ecc84340d6fa920b67bc53cd1e7adda0b`, 289 pages. Used by 33 new gap-fill cards. |
| `SRC-NEW510` | New Ideas 5-10-26; role: PMTiles sidecar/attestation operational packet. Used by 6 cards. |
| `SRC-NEW515` | New Ideas 5-15-26; role: CDL/PLANTS material-change watcher packet. Used by 6 cards. |
| `SRC-NEW58` | New Ideas 5-8-26; role: environmental source-health and gating spec packet. Used by 6 cards. |
| `SRC-OLL` | Ollama & Ubuntu Information; role: local runtime behind governed API and model-runtime constraints. Used by 3 cards. |
| `SRC-P18` | KFM Components Pass 18; role: prior cumulative card atlas; basis: 500 cards across 14 categories and source-supported idea entries. Used by 12 cards. |
| `SRC-P20` | KFM Components Pass 20 Unified Idea Index; role: cumulative idea/category atlas; basis: 9-category and 14-category normalization, implementation boundary, expansion agenda. Used by 48 cards. |
| `SRC-PEOPLE` | KFM People, Genealogy-DNA, and Land Ownership Architecture Blueprint; role: people/DNA/land sensitivity blueprint. Used by 9 cards. |
| `SRC-PIPE` | Kansas Frontier Matrix Pipeline Living Implementation Manual v0.3; role: lifecycle and query-save-recompile loop doctrine; basis: pipeline loop, source authority ladder, public-client rule. Used by 51 cards. |
| `SRC-ROADS` | KFM Roads, Rail, and Trade Routes Architecture Plan; role: transport lane blueprint. Used by 9 cards. |
| `SRC-SETTLE` | KFM Settlements, Cities, and Infrastructure Plan; role: settlements/infrastructure lane blueprint. Used by 6 cards. |
| `SRC-SOIL` | KFM Soil Architecture Extended Pro Planning Report; role: soil domain lane blueprint. Used by 12 cards. |
| `SRC-TEMPORAL` | Developing Time-Oriented Database Applications in SQL; role: temporal database semantics reference. Used by 21 cards. |
| `SRC-UIAI` | KFM Whole-UI + Governed AI Expansion Report; role: whole-UI and governed-AI expansion plan. Used by 3 cards. |
| `SRC-URBAN` | GIS in Sustainable Urban Planning and Management; role: planning, indicators, resilience, participation reference. Used by 9 cards. |

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
| `KFM-TRIAD-033` | Material Change Classification and Non-Event Receipts | `SRC-NEW416`, `SRC-PIPE`, `SRC-P20` | `KFM-CAND-0097` | `KFM-CAND-0098` | `KFM-CAND-0099` |
| `KFM-TRIAD-034` | Identifier and Precision Lineage | `SRC-NEW416`, `SRC-FAUNA`, `SRC-SOIL`, `SRC-HYD` | `KFM-CAND-0100` | `KFM-CAND-0101` | `KFM-CAND-0102` |
| `KFM-TRIAD-035` | Correctable Environmental Event Lifecycle | `SRC-NEW416`, `SRC-ATM`, `SRC-ENCYC` | `KFM-CAND-0103` | `KFM-CAND-0104` | `KFM-CAND-0105` |
| `KFM-TRIAD-036` | Baseline Cohort and Drift Governance | `SRC-NEW416`, `SRC-ATM`, `SRC-AIREF` | `KFM-CAND-0106` | `KFM-CAND-0107` | `KFM-CAND-0108` |
| `KFM-TRIAD-037` | Corroboration Role Graph | `SRC-NEW416`, `SRC-ATM`, `SRC-ENCYC`, `SRC-GAI` | `KFM-CAND-0109` | `KFM-CAND-0110` | `KFM-CAND-0111` |
| `KFM-TRIAD-038` | Purpose-Bound Consent and Revocation Propagation | `SRC-NEW416`, `SRC-PEOPLE`, `SRC-GREEN` | `KFM-CAND-0112` | `KFM-CAND-0113` | `KFM-CAND-0114` |
| `KFM-TRIAD-039` | Governed Time-Bucket Map Playback | `SRC-NEW416`, `SRC-MAP`, `SRC-MAPMASTER`, `SRC-TEMPORAL` | `KFM-CAND-0115` | `KFM-CAND-0116` | `KFM-CAND-0117` |
| `KFM-TRIAD-040` | STAC Profile and Link-Closure Conformance | `SRC-NEW416`, `SRC-P20`, `SRC-MAPMASTER` | `KFM-CAND-0118` | `KFM-CAND-0119` | `KFM-CAND-0120` |
| `KFM-TRIAD-041` | Historical Network Uncertainty and Temporal Joins | `SRC-NEW416`, `SRC-ROADS`, `SRC-TEMPORAL`, `SRC-GIS` | `KFM-CAND-0121` | `KFM-CAND-0122` | `KFM-CAND-0123` |
| `KFM-TRIAD-042` | Purpose-Specific Hash Profiles | `SRC-NEW416`, `SRC-P20`, `SRC-GREEN` | `KFM-CAND-0124` | `KFM-CAND-0125` | `KFM-CAND-0126` |
| `KFM-TRIAD-043` | Retrieval Intent and Query Snapshot | `SRC-NEW430`, `SRC-PIPE`, `SRC-ENCYC` | `KFM-CAND-0127` | `KFM-CAND-0128` | `KFM-CAND-0129` |
| `KFM-TRIAD-044` | Source Terms Snapshot and Rights Drift | `SRC-NEW430`, `SRC-GREEN`, `SRC-PIPE` | `KFM-CAND-0130` | `KFM-CAND-0131` | `KFM-CAND-0132` |
| `KFM-TRIAD-045` | Sampling Effort and Non-Detection Support | `SRC-NEW430`, `SRC-FAUNA`, `SRC-ENCYC` | `KFM-CAND-0133` | `KFM-CAND-0134` | `KFM-CAND-0135` |
| `KFM-TRIAD-046` | Distribution Assertion and Coverage Semantics | `SRC-NEW430`, `SRC-FLORA`, `SRC-FAUNA`, `SRC-GIS` | `KFM-CAND-0136` | `KFM-CAND-0137` | `KFM-CAND-0138` |
| `KFM-TRIAD-047` | Coverage-Aware Prioritization and Exploration-Bias Control | `SRC-NEW430`, `SRC-AIREF`, `SRC-ENCYC`, `SRC-URBAN` | `KFM-CAND-0139` | `KFM-CAND-0140` | `KFM-CAND-0141` |
| `KFM-TRIAD-048` | Measurement Support and Scale Reconciliation | `SRC-NEW430`, `SRC-SOIL`, `SRC-ATM`, `SRC-HYD` | `KFM-CAND-0142` | `KFM-CAND-0143` | `KFM-CAND-0144` |
| `KFM-TRIAD-049` | Product Cadence, Delivery Latency, and Availability | `SRC-NEW430`, `SRC-PIPE`, `SRC-TEMPORAL`, `SRC-ATM` | `KFM-CAND-0145` | `KFM-CAND-0146` | `KFM-CAND-0147` |
| `KFM-TRIAD-050` | Asynchronous Transfer and Partial-State Provenance | `SRC-NEW430`, `SRC-PIPE`, `SRC-ENCYC` | `KFM-CAND-0148` | `KFM-CAND-0149` | `KFM-CAND-0150` |
| `KFM-TRIAD-051` | Offline Release Capsule and Trust Freshness | `SRC-NEW430`, `SRC-MAP`, `SRC-MAPMASTER`, `SRC-GREEN` | `KFM-CAND-0151` | `KFM-CAND-0152` | `KFM-CAND-0153` |
| `KFM-TRIAD-052` | Verified Rendering Resource Envelope | `SRC-NEW430`, `SRC-MAP`, `SRC-MAPMASTER`, `SRC-GAI` | `KFM-CAND-0154` | `KFM-CAND-0155` | `KFM-CAND-0156` |
| `KFM-TRIAD-053` | Confounder Exclusion and Observation Fitness | `SRC-NEW430`, `SRC-ATM`, `SRC-AIREF`, `SRC-ENCYC` | `KFM-CAND-0157` | `KFM-CAND-0158` | `KFM-CAND-0159` |
| `KFM-TRIAD-054` | Cross-Boundary Evidence Custody and Reconciliation | `SRC-NEW423`, `SRC-PIPE`, `SRC-GREEN`, `SRC-ENCYC` | `KFM-CAND-0160` | `KFM-CAND-0161` | `KFM-CAND-0162` |
| `KFM-TRIAD-055` | Composed Claim Dependency Closure | `SRC-NEW423`, `SRC-ENCYC`, `SRC-GAI`, `SRC-MAP` | `KFM-CAND-0163` | `KFM-CAND-0164` | `KFM-CAND-0165` |
| `KFM-TRIAD-056` | Trust-Root Lifecycle and Historical Signature Verification | `SRC-NEW423`, `SRC-GREEN`, `SRC-MAPMASTER`, `SRC-GAI` | `KFM-CAND-0166` | `KFM-CAND-0167` | `KFM-CAND-0168` |
| `KFM-TRIAD-057` | Replay-Safe Event Identity and Side-Effect Ledger | `SRC-NEW423`, `SRC-PIPE`, `SRC-GREEN`, `SRC-ENCYC` | `KFM-CAND-0169` | `KFM-CAND-0170` | `KFM-CAND-0171` |
| `KFM-TRIAD-058` | Conditional Decision Obligations and Closure | `SRC-NEW423`, `SRC-GREEN`, `SRC-ENCYC`, `SRC-GAI` | `KFM-CAND-0172` | `KFM-CAND-0173` | `KFM-CAND-0174` |
| `KFM-TRIAD-059` | Reversible Entity Reconciliation and Conflict-Preserving Dedupe | `SRC-NEW425`, `SRC-FAUNA`, `SRC-FLORA`, `SRC-ENCYC` | `KFM-CAND-0175` | `KFM-CAND-0176` | `KFM-CAND-0177` |
| `KFM-TRIAD-060` | Taxonomic Concept and Name-Usage Lineage | `SRC-NEW425`, `SRC-FLORA`, `SRC-FAUNA`, `SRC-ENCYC` | `KFM-CAND-0178` | `KFM-CAND-0179` | `KFM-CAND-0180` |
| `KFM-TRIAD-061` | Place-Name Authority and Temporal Alias Graph | `SRC-NEW425`, `SRC-SETTLE`, `SRC-ROADS`, `SRC-TEMPORAL` | `KFM-CAND-0181` | `KFM-CAND-0182` | `KFM-CAND-0183` |
| `KFM-TRIAD-062` | Survey-Control and Boundary Derivation Provenance | `SRC-NEW425`, `SRC-GIS`, `SRC-TEMPORAL`, `SRC-ENCYC` | `KFM-CAND-0184` | `KFM-CAND-0185` | `KFM-CAND-0186` |
| `KFM-TRIAD-063` | Adversarial Validator Assurance and Mutation Adequacy | `SRC-NEW425`, `SRC-GREEN`, `SRC-PIPE`, `SRC-GAI` | `KFM-CAND-0187` | `KFM-CAND-0188` | `KFM-CAND-0189` |
| `KFM-TRIAD-064` | Bitemporal Verification-State Replay | `SRC-NEW414`, `SRC-TEMPORAL`, `SRC-GREEN`, `SRC-ENCYC` | `KFM-CAND-0190` | `KFM-CAND-0191` | `KFM-CAND-0192` |
| `KFM-TRIAD-065` | Source-Conflict Topology and Influence Accounting | `SRC-NEW414`, `SRC-GAI`, `SRC-GREEN`, `SRC-ENCYC` | `KFM-CAND-0193` | `KFM-CAND-0194` | `KFM-CAND-0195` |
| `KFM-TRIAD-066` | Cross-Layer Outcome Projection and Parity | `SRC-NEW414`, `SRC-NEW415`, `SRC-GAI`, `SRC-MAP` | `KFM-CAND-0196` | `KFM-CAND-0197` | `KFM-CAND-0198` |
| `KFM-TRIAD-067` | Verifier Profile and Capability Portability | `SRC-NEW414`, `SRC-NEW415`, `SRC-GREEN`, `SRC-MAPMASTER` | `KFM-CAND-0199` | `KFM-CAND-0200` | `KFM-CAND-0201` |
| `KFM-TRIAD-068` | Source-Native Quality Translation and Health Separation | `SRC-NEW415`, `SRC-SOIL`, `SRC-ATM`, `SRC-ENCYC` | `KFM-CAND-0202` | `KFM-CAND-0203` | `KFM-CAND-0204` |
| `KFM-TRIAD-069` | Generated Runtime-Proof Artifact Lifecycle | `SRC-NEW415`, `SRC-GREEN`, `SRC-PIPE`, `SRC-ENCYC` | `KFM-CAND-0205` | `KFM-CAND-0206` | `KFM-CAND-0207` |
| `KFM-TRIAD-070` | Observed Interface Evolution and Compatibility Window | `SRC-NEW414`, `SRC-NEW415`, `SRC-PIPE`, `SRC-DIR` | `KFM-CAND-0208` | `KFM-CAND-0209` | `KFM-CAND-0210` |

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

### KFM-TRIAD-033 — Material Change Classification and Non-Event Receipts

**Why it matters:** PROPOSED — This card closes the gap between detecting different bytes and deciding that a source, claim, domain object, or release-significant artifact changed in a way that warrants governed work.

**Source IDs:** `SRC-NEW416`, `SRC-PIPE`, `SRC-P20`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0097` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should distinguish byte change, schema change, semantic change, source-role change, rights or sensitivity change, material domain change, and release-significant change instead of treating hash inequality as one state. |
| `KFM-CAND-0098` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | REL - Catalog Closure, Publication, Release, Rollback, Recompile | PROPOSED — KFM should let reviewers inspect the applicable materiality profile, before/after metrics, threshold evidence, decision reason, affected scope, and explicit non-material disposition without implying publication. |
| `KFM-CAND-0099` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define versioned MaterialityProfile, ChangeAssessment, and NonMaterialChangeReceipt objects whose inputs, exclusions, thresholds, policy refs, and replay context are deterministic and whose outputs cannot publish. |

**Implementation-surface note:** PROPOSED — Build the existing stable local diff helper first; feed its report into a separate materiality contract so the comparator never becomes the policy or promotion authority.

**Carry-forward state:** NEW_GAP_FILL. Remote `main@5266ba5…` confirms watcher, diff, receipt, and materiality language, but a common enforced change-assessment chain remains **NEEDS VERIFICATION**.

### KFM-TRIAD-034 — Identifier and Precision Lineage

**Why it matters:** PROPOSED — This card prevents vendor identifiers, resolved identities, approximate geometries, and public-safe derivatives from collapsing into one misleading canonical record.

**Source IDs:** `SRC-NEW416`, `SRC-FAUNA`, `SRC-SOIL`, `SRC-HYD`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0100` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should preserve every source identifier verbatim while representing crosswalk, merge, split, surrogate, and unresolved identity decisions as time-aware assertions rather than destructive rewrites. |
| `KFM-CAND-0101` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show source identity, resolved identity, effective spatial precision, uncertainty class, generalization method, and public-versus-restricted derivative lineage wherever those differences affect interpretation. |
| `KFM-CAND-0102` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should define IdentifierAssertion, CrosswalkResolution, PrecisionProfile, and PrecisionTransformReceipt objects with source IDs, validity intervals, confidence, method version, reviewer state, and supersession links. |

**Implementation-surface note:** PROPOSED — Extend existing domain identity and redaction families through one reviewed cross-cutting contract pattern; do not create a new identity root or rely on random-each-release jitter.

**Carry-forward state:** NEW_GAP_FILL. Domain-specific identity and precision surfaces are **PARTIAL** in the pinned remote-main snapshot; common cross-domain lineage remains **NEEDS VERIFICATION**.

### KFM-TRIAD-035 — Correctable Environmental Event Lifecycle

**Why it matters:** PROPOSED — This card prevents a provisional observation, anomaly candidate, corroborated event, reviewed conclusion, correction, and withdrawal from being represented as the same fact.

**Source IDs:** `SRC-NEW416`, `SRC-ATM`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0103` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model environmental observations, candidates, local events, regional events, review dispositions, corrections, retractions, and supersessions as distinct time-aware object states with no automatic upward collapse. |
| `KFM-CAND-0104` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should expose event scope, provisional status, persistence, corroboration, freshness, source roles, confidence limits, correction lineage, and finite outcome without presenting a candidate as a validated public event. |
| `KFM-CAND-0105` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define EnvironmentalObservation, EventCandidate, EnvironmentalEvent, EventReviewDisposition, and EventCorrection contracts with transition guards, evidence refs, baseline refs, policy decisions, receipts, and rollback or withdrawal links. |

**Implementation-surface note:** PROPOSED — Use synthetic atmosphere fixtures to prove `Observation -> Candidate -> Event -> Correction` anti-collapse behavior before live feeds, alerts, map layers, or publication.

**Carry-forward state:** NEW_GAP_FILL. Atmosphere source, observation, smoke, finite-outcome, correction, and release scaffolds are **PARTIAL**; the end-to-end event state machine remains **NEEDS VERIFICATION**.

### KFM-TRIAD-036 — Baseline Cohort and Drift Governance

**Why it matters:** PROPOSED — This card makes a statistical or environmental baseline inspectable as a versioned evidence artifact rather than a hidden calculation.

**Source IDs:** `SRC-NEW416`, `SRC-ATM`, `SRC-AIREF`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0106` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should treat cohort eligibility, exclusions, lookback window, seasonal window, missingness, method continuity, sensor relocation, uncertainty floor, parameter choice, and recalculation cadence as part of baseline meaning. |
| `KFM-CAND-0107` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should provide reviewer-readable baseline cards showing cohort coverage, excluded records, discontinuities, parameter versions, freshness, source roles, known blind spots, and fitness-for-use. |
| `KFM-CAND-0108` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should define BaselineManifest, CohortEligibilityReport, DiscontinuityRecord, BaselineValidationReport, and BaselineRebuildReceipt with digest-bound inputs, parameter profiles, tool versions, and correction lineage. |

**Implementation-surface note:** PROPOSED — A baseline artifact must be replayable and independently reviewable; a threshold or anomaly result must reference the exact baseline version used.

**Carry-forward state:** NEW_GAP_FILL. The workspace contains baseline and anomaly vocabulary but no accepted common baseline artifact family was established in this review.

### KFM-TRIAD-037 — Corroboration Role Graph

**Why it matters:** PROPOSED — This card prevents multiple feeds from being counted as independent confirmation when they share derivation, represent different epistemic roles, or are stale or contradictory.

**Source IDs:** `SRC-NEW416`, `SRC-ATM`, `SRC-ENCYC`, `SRC-GAI`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0109` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should represent corroboration as qualified relations among observation, regulatory, remote-sensing interpretation, forecast, simulation, contextual, and derived sources rather than as a raw source count. |
| `KFM-CAND-0110` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show which sources support, contradict, qualify, duplicate, or cannot evaluate a claim, including independence, freshness, spatial and temporal overlap, and role-specific limitations. |
| `KFM-CAND-0111` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should define CorroborationAssertion and SourceIndependenceAssessment contracts plus policy composition that fails closed on role collapse, unresolved contradictions, missing freshness, or prohibited role combinations. |

**Implementation-surface note:** PROPOSED — Corroboration may raise confidence or narrow scope, but it must not bypass identity, evidence closure, rights, sensitivity, review, release, correction, or rollback.

**Carry-forward state:** NEW_GAP_FILL. Source-role anti-collapse doctrine exists; a common machine-enforced corroboration relation remains **NEEDS VERIFICATION**.

### KFM-TRIAD-038 — Purpose-Bound Consent and Revocation Propagation

**Why it matters:** PROPOSED — This card keeps consent useful without letting it become identity proof, evidence, a license, a sensitivity downgrade, or publication authority.

**Source IDs:** `SRC-NEW416`, `SRC-PEOPLE`, `SRC-GREEN`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0112` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should bind consent to exact subject or representative authority, purpose, operation, fields, relationships, audience, retention, time, and revocation status while preserving independent evidence, rights, sensitivity, review, and release gates. |
| `KFM-CAND-0113` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should provide a consent-first review flow that previews transforms, discloses retained and sidecar fields, shows collateral-person impact, limits persistence before approval, and makes revocation and cleanup status inspectable to authorized stewards. |
| `KFM-CAND-0114` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define purpose-bound ConsentGrant, status or revocation lookup, RevocationReceipt, dependency index, CacheInvalidationReceipt, and synthetic no-network fixtures that prove the next consequential read, answer, export, tile, graph, index, and cache honors withdrawal. |

**Implementation-surface note:** PROPOSED — Cryptographic envelope, pseudonymization, token, KMS, and public-status mechanisms remain downstream choices after placement, threat model, collateral-person, key custody, retention, and revocation semantics are accepted.

**Carry-forward state:** NEW_GAP_FILL. Consent and revocation doctrine is extensive but executable placement and propagation remain explicitly **PARTIAL / NEEDS VERIFICATION**.

### KFM-TRIAD-039 — Governed Time-Bucket Map Playback

**Why it matters:** PROPOSED — This card turns fast time filtering into a governed carrier contract that preserves time semantics, integrity, accessibility, and evidence continuity.

**Source IDs:** `SRC-NEW416`, `SRC-MAP`, `SRC-MAPMASTER`, `SRC-TEMPORAL`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0115` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should treat feature filters, epoch buckets, PMTiles sources, worker-prepared indexes, animation windows, and camera transitions as downstream temporal carriers rather than valid-time authority or evidence. |
| `KFM-CAND-0116` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show the active window, cadence, valid/observed/source/retrieval/release/correction time, precision, freshness, bucket identity, transition gaps, reduced-motion state, and evidence links during map playback. |
| `KFM-CAND-0117` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should define TimeBucketManifest, TemporalFilterEnvelope, bucket digest and release refs, governed worker-message schemas, swap/fallback state, and tests proving that filters and source changes preserve trust state and use accepted MapLibre adapter boundaries. |

**Implementation-surface note:** PROPOSED — Retain renderer-neutral availability semantics, but do not introduce Cesium, CZML, or a peer-renderer dependency without an accepted decision.

**Carry-forward state:** NEW_GAP_FILL. Time Banner and Story Player contracts are detailed; executable bucket manifests and playback tests remain **NEEDS VERIFICATION**.

### KFM-TRIAD-040 — STAC Profile and Link-Closure Conformance

**Why it matters:** PROPOSED — This card separates a well-shaped STAC record from a closed catalog graph, a conformant API response, and a currently reachable external asset.

**Source IDs:** `SRC-NEW416`, `SRC-P20`, `SRC-MAPMASTER`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0118` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | REL - Catalog Closure, Publication, Release, Rollback, Recompile | PROPOSED — KFM should enforce a minimal, versioned STAC profile with query-critical spatial, temporal, collection, asset-role, projection, link, and provenance references while keeping full EvidenceBundle and PROV graphs outside STAC. |
| `KFM-CAND-0119` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should provide record, collection, graph-closure, API-conformance, and availability summaries as separate reviewer states so one green check cannot imply the others. |
| `KFM-CAND-0120` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should implement deterministic no-network validators for record shape, extension discipline, query-critical fields, asset roles, and local link closure plus separate fixtures for pagination, filters, field projection, broken graphs, placeholders, and optional live availability probes. |

**Implementation-surface note:** PROPOSED — Resolve profile identifier, namespace, schema authority, placeholder disposition, and record-versus-closure ownership before introducing a blocking validator.

**Carry-forward state:** NEW_GAP_FILL. A draft STAC standard and partial catalog validators exist; accepted profile authority and complete enforcement remain **NEEDS VERIFICATION**.

### KFM-TRIAD-041 — Historical Network Uncertainty and Temporal Joins

**Why it matters:** PROPOSED — This card enables rich Kansas history exploration without turning approximate points, modern authoritative alignments, and proximity calculations into false historical certainty.

**Source IDs:** `SRC-NEW416`, `SRC-ROADS`, `SRC-TEMPORAL`, `SRC-GIS`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0121` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model historical place assertions, route-segment assertions, designated modern alignments, approximate geocodes, valid-time intervals, and proximity candidates separately, with no automatic causal or service-network inference. |
| `KFM-CAND-0122` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should let users explore post offices, settlements, and trails by time while seeing coordinate method, uncertainty geometry, route vintage, temporal overlap, distance band, source role, and interpretation caveats. |
| `KFM-CAND-0123` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define HistoricalPlaceAssertion, HistoricalRouteSegment, ProximityCandidate, TemporalSpatialJoinReceipt, and public-safe tile projection rules with synthetic fixtures for exact, approximate, non-overlapping, ambiguous, and unsupported cases. |

**Implementation-surface note:** PROPOSED — First complete source authority, rights, cadence, access, citation, and precision fields for the existing post-office and Santa Fe Trail descriptors; no live ingest or public layer is implied.

**Carry-forward state:** NEW_GAP_FILL. Greenfield descriptors exist, but source admission and uncertainty-preserving cross-layer behavior remain **PARTIAL**.

### KFM-TRIAD-042 — Purpose-Specific Hash Profiles

**Why it matters:** PROPOSED — This card prevents `spec_hash`, semantic content identity, artifact-byte integrity, receipt identity, and signature subjects from becoming an ambiguous or self-referential single digest.

**Source IDs:** `SRC-NEW416`, `SRC-P20`, `SRC-GREEN`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0124` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should name and version distinct canonicalization profiles for specification identity, semantic record content, normalized geometry, artifact bytes, receipt payloads, and signed subjects, with explicit non-equivalence. |
| `KFM-CAND-0125` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers inspect algorithm, profile version, included and excluded fields, geometry and numeric normalization, volatile-field handling, digest subject, test-vector status, and migration compatibility. |
| `KFM-CAND-0126` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define CanonicalizationProfile and HashBinding contracts plus deterministic test vectors that reject self-hashing fields, signatures inside signed subjects, unstable timestamps, unordered collections, nonfinite numbers, ambiguous CRS, and cross-profile comparisons. |

**Implementation-surface note:** PROPOSED — Hash equality proves equality only under the declared profile; it does not prove truth, authority, rights, evidence closure, policy approval, review, release, or public safety.

**Carry-forward state:** NEW_GAP_FILL. Identity ADR and contract surfaces discuss canonicalization, but accepted implementation and complete test-vector enforcement remain **NEEDS VERIFICATION**.

### KFM-TRIAD-043 — Retrieval Intent and Query Snapshot

**Why it matters:** PROPOSED — A source snapshot cannot explain what was requested, excluded, paginated, sampled, or redacted unless retrieval intent is preserved independently from both source identity and returned bytes.

**Source IDs:** `SRC-NEW430`, `SRC-PIPE`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0127` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should treat retrieval intent, normalized query predicate, geographic and temporal scope, pagination, sampling, requested fields, and result selection as versioned provenance rather than an informal note attached after ingestion. |
| `KFM-CAND-0128` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers inspect the exact source descriptor version, query scope, requested fields, filters, exclusions, page or job boundaries, redacted authentication posture, result count, and deviations between planned and executed retrieval. |
| `KFM-CAND-0129` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define RetrievalIntent, QuerySnapshot, and RetrievalReceipt contracts with deterministic parameter normalization, secret exclusion, descriptor refs, request and response digests, pagination closure, and finite incomplete or changed-query outcomes. |

**Implementation-surface note:** PROPOSED — Retrieval intent does not grant source admission, rights, claim authority, evidence closure, or release. Secret values remain outside public receipts.

**Carry-forward state:** NEW_GAP_FILL. Source descriptors and receipts preserve access and source-head facts, but no common repository-wide query-predicate artifact was established in this review.

### KFM-TRIAD-044 — Source Terms Snapshot and Rights Drift

**Why it matters:** PROPOSED — Permission to fetch is not permission to redistribute, publish, commercialize, retain, or derive; those duties can change independently of source bytes.

**Source IDs:** `SRC-NEW430`, `SRC-GREEN`, `SRC-PIPE`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0130` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | PROPOSED — KFM should preserve the exact terms, license, citation, attribution, redistribution, commercial-use, retention, access, and verification posture that governed each retrieval and should treat later terms drift as a new rights decision. |
| `KFM-CAND-0131` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should show the verified-at time, terms or license identifier, evidence reference, permitted and prohibited uses, attribution duties, downstream obligations, uncertainty, supersession, and whether existing products require hold, recomputation, withdrawal, or no action. |
| `KFM-CAND-0132` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should define SourceTermsSnapshot, RightsAssessment, and TermsChangeDecision objects plus policy tests that fail closed on missing evidence, scope mismatch, expired permission, license incompatibility, or unpropagated obligations. |

**Implementation-surface note:** PROPOSED — A terms URL or SPDX-like label is not enough when the governing text, dataset-level license, access agreement, or verification state is unresolved.

**Carry-forward state:** NEW_GAP_FILL. `SourceDescriptor.rights` is detailed and versioned, but a separately reviewable terms snapshot and downstream drift-disposition chain remain **NEEDS VERIFICATION**.

### KFM-TRIAD-045 — Sampling Effort and Non-Detection Support

**Why it matters:** PROPOSED — Presence-only observations, incomplete checklists, and opportunistic records cannot support absence or non-detection claims without a defined opportunity to detect.

**Source IDs:** `SRC-NEW430`, `SRC-FAUNA`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0133` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should bind every detection or non-detection inference to explicit sampling effort, protocol, completeness, observer or instrument opportunity, spatial and temporal support, target scope, and known detectability limits. |
| `KFM-CAND-0134` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should distinguish observed detection, supported non-detection, not sampled, incomplete effort, unknown effort, suppressed result, and stale coverage while showing effort intensity and blind spots without exposing protected observer or species locations. |
| `KFM-CAND-0135` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define SamplingEvent, DetectionOpportunity, EffortProfile, and NonDetectionAssertion contracts with pair-coherence checks, completeness flags, protocol fields, privacy transforms, and negative fixtures proving that missing or incompatible effort returns ABSTAIN or DENY. |

**Implementation-surface note:** PROPOSED — eBird EBD/SED is one motivating source pair, not the authority for a cross-domain contract. Source-specific fields must adapt into a reviewed common meaning without inventing absence.

**Carry-forward state:** NEW_GAP_FILL. eBird and fauna documentation already encode complete-checklist and effort rules; common reusable machine enforcement remains **PARTIAL / NEEDS VERIFICATION**.

### KFM-TRIAD-046 — Distribution Assertion and Coverage Semantics

**Why it matters:** PROPOSED — A county or state distribution row is a source-versioned reported status, not proof of current abundance, completeness, habitat suitability, or true absence.

**Source IDs:** `SRC-NEW430`, `SRC-FLORA`, `SRC-FAUNA`, `SRC-GIS`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0136` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model present, explicitly absent, not assessed, unknown, suppressed, disputed, stale, and out-of-scope distribution states as assertions bound to source, vocabulary, geography version, valid time, and evidence support. |
| `KFM-CAND-0137` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should map distribution status, survey or reporting coverage, source vintage, boundary version, precision, sensitivity transform, and limitations separately so blank geography is never rendered as absence and occurrence density is never rendered as abundance. |
| `KFM-CAND-0138` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define DistributionAssertion, CoverageAssessment, DistributionStatusProfile, and GeographyBinding objects with source-native status preservation, FIPS or boundary crosswalk refs, supersession, and fixtures for missing rows, changed boundaries, conflicting sources, and unsupported first-observed dates. |

**Implementation-surface note:** PROPOSED — USDA PLANTS county and state status is a motivating case. Do not synthesize `first_observed`, absence, occupancy, or abundance when the source does not provide that meaning.

**Carry-forward state:** NEW_GAP_FILL. Flora and fauna contracts preserve occurrence and non-detection distinctions, but one closed cross-domain distribution-state profile was not established.

### KFM-TRIAD-047 — Coverage-Aware Prioritization and Exploration-Bias Control

**Why it matters:** PROPOSED — Ranking counties by record density and recency can prioritize places that were already sampled heavily, creating a self-reinforcing exploration loop that looks like ecological importance.

**Source IDs:** `SRC-NEW430`, `SRC-AIREF`, `SRC-ENCYC`, `SRC-URBAN`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0139` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should separate data-richness, recency, sampling effort, source diversity, geographic coverage gaps, uncertainty reduction, sensitivity burden, steward capacity, and public value when prioritizing new work. |
| `KFM-CAND-0140` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should explain why an area was prioritized, show every score component and blind spot, compare density-led and gap-led rankings, and label the result as workflow triage rather than biodiversity richness or conservation importance. |
| `KFM-CAND-0141` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should define CoveragePriorityProfile and PriorityScorecard with versioned weights, source-role caps, missingness treatment, sensitivity and review costs, counterfactual rankings, stability checks, and receipts that cannot authorize source activation or publication. |

**Implementation-surface note:** PROPOSED — County rankings may allocate review effort, but they must not become ecological claims or suppress under-observed areas.

**Carry-forward state:** NEW_GAP_FILL. Planning and analytics governance exists, but no repository-wide guard against data-density-driven exploration bias was established.

### KFM-TRIAD-048 — Measurement Support and Scale Reconciliation

**Why it matters:** PROPOSED — A value is not comparable until parameter, unit, method, depth or height, averaging window, footprint, resolution, uncertainty, and knowledge character are aligned or explicitly held apart.

**Source IDs:** `SRC-NEW430`, `SRC-SOIL`, `SRC-ATM`, `SRC-HYD`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0142` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should bind every environmental value to a MeasurementSupport that preserves parameter, unit, instrument or model character, vertical support, temporal aggregation, spatial footprint, CRS, resolution, uncertainty, quality, and no-data semantics. |
| `KFM-CAND-0143` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show measured versus modeled versus derived character, unit and conversion, depth or level, averaging window, footprint and resolution, co-location gap, resampling method, uncertainty, and whether a comparison is valid, qualified, or unsupported. |
| `KFM-CAND-0144` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define MeasurementSupport, UnitTransformReceipt, ScaleReconciliationReport, and ComparisonFitnessDecision objects with pinned conversion and resampling profiles plus fixtures for unit, depth, time-window, footprint, resolution, and observation-versus-model mismatches. |

**Implementation-surface note:** PROPOSED — Satellite grids, stations, regulatory observations, forecasts, and models may inform one another, but co-location or resampling does not erase their source roles or support differences.

**Carry-forward state:** NEW_GAP_FILL. Soil, atmosphere, hydrology, and cross-domain validators already preserve many support fields; a common comparison and reconciliation object family remains **PARTIAL**.

### KFM-TRIAD-049 — Product Cadence, Delivery Latency, and Availability

**Why it matters:** PROPOSED — A three-hour product can arrive days later; expected cadence, generation time, publication latency, availability, retrieval, freshness, and staleness are different clocks.

**Source IDs:** `SRC-NEW430`, `SRC-PIPE`, `SRC-TEMPORAL`, `SRC-ATM`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0145` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should model observation cadence, product cadence, expected delivery window, observed availability, source revision, retrieval time, freshness window, stale threshold, and outage exception separately and version them with the source descriptor. |
| `KFM-CAND-0146` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show observed, generated, expected-available, actually available, retrieved, validated, and released times plus finite states such as on-time, expected-lag, late, stale, missing, superseded, and source-outage. |
| `KFM-CAND-0147` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define DeliveryExpectation, AvailabilityObservation, and FreshnessDecision contracts with tolerance profiles, calendar exceptions, learned observations that require review before changing policy, and synthetic fixtures distinguishing expected latency from true staleness. |

**Implementation-surface note:** PROPOSED — Packet latency figures are dated evidence to verify against official product documentation before activation; they are not timeless scheduler constants.

**Carry-forward state:** NEW_GAP_FILL. SourceDescriptor cadence and source-head semantics are strong, but a common delivery-latency and availability-window contract was not found.

### KFM-TRIAD-050 — Asynchronous Transfer and Partial-State Provenance

**Why it matters:** PROPOSED — Large provider jobs can be queued, running, expired, partially downloaded, resumed, replaced, or cancelled; collapsing those states into success or failure can duplicate or corrupt ingest.

**Source IDs:** `SRC-NEW430`, `SRC-PIPE`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0148` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should distinguish provider request identity, normalized query identity, remote job state, transfer state, local partial bytes, final artifact identity, archive expiry, retry lineage, and ingest identity for asynchronous or resumable sources. |
| `KFM-CAND-0149` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers inspect request parameters, provider job identifier, polling history, retry/backoff decisions, partial byte ranges, resume basis, expected and actual size, final digest, archive expiry, and whether downstream processing ever saw incomplete bytes. |
| `KFM-CAND-0150` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define AsyncFetchRun, TransferCheckpoint, and DownloadReceipt objects with finite requested, queued, running, succeeded, failed, cancelled, expired, partial, and quarantined states plus idempotence, checksum, resume, and no-double-ingest tests. |

**Implementation-surface note:** PROPOSED — GBIF async downloads and large eBird snapshots motivate the pattern, but provider-specific polling fields should remain adapter details.

**Carry-forward state:** NEW_GAP_FILL. Source-specific docs and pipeline tests discuss polling and resumable partial states; one common auditable transfer contract remains **NEEDS VERIFICATION**.

### KFM-TRIAD-051 — Offline Release Capsule and Trust Freshness

**Why it matters:** PROPOSED — A `.pmtiles` file alone is not an offline product, and a package verified once must not remain silently trusted after expiry, correction, withdrawal, or policy change.

**Source IDs:** `SRC-NEW430`, `SRC-MAP`, `SRC-MAPMASTER`, `SRC-GREEN`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0151` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | REL - Catalog Closure, Publication, Release, Rollback, Recompile | PROPOSED — KFM should treat an offline map as a release capsule containing exact spatial artifacts, style, glyph and sprite manifests, evidence and citation summaries, policy and release refs, verification material, expiry, correction, and withdrawal behavior. |
| `KFM-CAND-0152` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show offline release identity, installed and last-verified times, coverage and limitations, expiry, stale or withdrawn state, pending update size, correction availability, evidence depth, and what functions are blocked when trust freshness cannot be renewed. |
| `KFM-CAND-0153` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should define OfflineReleaseCapsule, CacheInventory, OfflineVerificationReceipt, and correction or withdrawal delta handoffs with atomic install, interrupted update, expired trust, rollback, cache purge, and reconnect synchronization fixtures. |

**Implementation-surface note:** PROPOSED — Offline mode may expose the last verified public release with visible limits; it must never cache restricted geometry, use internal stores, or imply current status past the accepted freshness policy.

**Carry-forward state:** NEW_GAP_FILL. PMTiles, manifest, rollback, cache-invalidation, and offline-bundle concepts exist, but an end-to-end public offline capsule contract remains **PARTIAL**.

### KFM-TRIAD-052 — Verified Rendering Resource Envelope

**Why it matters:** PROPOSED — Integrity checks that exhaust memory, block interaction, or occur after decode are not a safe rendering boundary, especially on constrained devices.

**Source IDs:** `SRC-NEW430`, `SRC-MAP`, `SRC-MAPMASTER`, `SRC-GAI`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0154` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should verify released map bytes, proof structure, expected signer or trust profile, and release binding before decode or render while enforcing declared network, CPU, memory, concurrency, and interaction budgets. |
| `KFM-CAND-0155` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should expose loading, verifying, verified, degraded, stale, blocked, and failed states without flashing unverified content and should provide accessible retry, offline, lower-detail, abstention, and evidence-summary paths. |
| `KFM-CAND-0156` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should define VerifiedRenderingEnvelope and governed worker messages with chunked hashing, proof and signer checks, queue and concurrency limits, fetch/decode/hash/heap budgets, cancellation, and fixtures for corruption, truncation, replay, timeout, resource exhaustion, and worker failure. |

**Implementation-surface note:** PROPOSED — Passing signature and digest checks proves artifact authenticity and integrity under the declared profile, not evidence truth, rights, review, or publication correctness.

**Carry-forward state:** NEW_GAP_FILL. Renderer boundaries, performance budgets, and artifact verification exist separately; their fail-closed client composition remains **NEEDS VERIFICATION**.

### KFM-TRIAD-053 — Confounder Exclusion and Observation Fitness

**Why it matters:** PROPOSED — Clouds, smoke, haze, shadows, snow, sensor faults, maintenance, and method discontinuities can make a valid observation unfit for a particular analysis without making it nonexistent.

**Source IDs:** `SRC-NEW430`, `SRC-ATM`, `SRC-AIREF`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0157` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | PROPOSED — KFM should evaluate observation fitness for a declared use through versioned quality, mask, confounder, persistence, source-role, freshness, and support profiles while retaining excluded evidence and reasons for correction or reinterpretation. |
| `KFM-CAND-0158` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show the declared use, fitness state, excluded observations, quality masks, confounders, persistence support, alternative explanations, method version, affected area or interval, and whether a conclusion was narrowed, delayed, quarantined, corrected, or withdrawn. |
| `KFM-CAND-0159` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should define ObservationFitnessDecision, ContextSnapshot, and ExclusionReceipt objects with deterministic source-specific profiles and fixtures for cloud, smoke, shadow, snow, missing QA, single-observation, contradictory-context, stale-mask, and corrected-mask cases. |

**Implementation-surface note:** PROPOSED — The packet's vegetation thresholds are candidate policy inputs, not universal scientific constants. First proofs should use synthetic observations and reason codes.

**Carry-forward state:** NEW_GAP_FILL. Domain validators already preserve quality, support, source role, and mismatch reasons; one reusable, correctable fitness-for-use decision family remains **PARTIAL**.

### KFM-TRIAD-054 — Cross-Boundary Evidence Custody and Reconciliation

**Why it matters:** PROPOSED — A sender receipt alone cannot prove what a receiving lane accepted, rejected, duplicated, quarantined, or left unresolved.

**Source IDs:** `SRC-NEW423`, `SRC-PIPE`, `SRC-GREEN`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0160` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should treat every transfer across lifecycle, environment, organization, or responsibility boundaries as a custody handoff that preserves the exact offered artifact, receiving decision, accepted subset, rejected subset, duplicates, and unresolved balance. |
| `KFM-CAND-0161` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers compare sender and receiver receipts, inspect item and byte accounting, follow retries and replacements, and distinguish complete, partially accepted, quarantined, disputed, and unreconciled handoffs. |
| `KFM-CAND-0162` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define CustodyHandoff, AcceptanceRecord, and ReconciliationReport objects with digest and count conservation, idempotent retry, duplicate detection, reject reasons, timeout, correction, and closure fixtures. |

**Implementation-surface note:** PROPOSED — A custody receipt proves what was offered or observed at a boundary, not that the receiving lane validated truth, accepted rights, or authorized release.

**Carry-forward state:** NEW_GAP_FILL. Lane receipts and promotion records exist, but a common sender-to-receiver reconciliation seam remains **PARTIAL**.

### KFM-TRIAD-055 — Composed Claim Dependency Closure

**Why it matters:** PROPOSED — A public claim assembled from several evidence bundles can appear supported even when a mandatory dependency is missing, denied, contradictory, or stale.

**Source IDs:** `SRC-NEW423`, `SRC-ENCYC`, `SRC-GAI`, `SRC-MAP`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0163` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should model composed claims as dependency graphs whose required, optional, one-of, excluded, contradictory, and context-only evidence roles determine whether the whole claim is supported, qualified, abstained, denied, or erroneous. |
| `KFM-CAND-0164` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show which claim components closed, which dependencies are missing or withheld, why the conclusion was narrowed, and whether an alternative evidence path satisfied the declared claim profile. |
| `KFM-CAND-0165` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should define ComposedClaimProfile, ClaimDependency, and ClaimClosureReport contracts with cycle detection, role cardinality, freshness, policy outcome, contradiction, alternative-path, and fail-closed fixtures. |

**Implementation-surface note:** PROPOSED — Closure is evaluated against a declared claim profile; it must not invent support by silently dropping required dependencies or averaging contradictory evidence.

**Carry-forward state:** NEW_GAP_FILL. Claim envelopes and evidence closure exist, but reusable dependency-graph semantics for composed claims remain **NEEDS VERIFICATION**.

### KFM-TRIAD-056 — Trust-Root Lifecycle and Historical Signature Verification

**Why it matters:** PROPOSED — Key rotation, revocation, expiry, and trust-policy change can make a currently valid key different from the key that was valid when an artifact was signed or reviewed.

**Source IDs:** `SRC-NEW423`, `SRC-GREEN`, `SRC-MAPMASTER`, `SRC-GAI`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0166` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should version trust roots, signer roles, activation, expiry, revocation, compromise, supersession, and verification policy so current trust and historical validity are evaluated without rewriting prior evidence. |
| `KFM-CAND-0167` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers inspect signer identity, trust-profile version, signing and verification times, key status then and now, revocation or compromise reason, offline-verification posture, and any required re-sign, correction, withdrawal, or abstention. |
| `KFM-CAND-0168` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should define TrustRootRecord, SignerAuthorization, KeyStatusEvent, and HistoricalVerificationReceipt with synthetic active, rotated, expired, revoked, compromised, unknown, offline, and policy-version mismatch fixtures. |

**Implementation-surface note:** PROPOSED — Historical signature validity proves origin and integrity under the recorded trust profile; it does not prove claim truth, rights, review sufficiency, or release fitness.

**Carry-forward state:** NEW_GAP_FILL. Signing and key-rotation guidance is substantial, while accepted machine authority and historical-verification enforcement remain **PARTIAL**.

### KFM-TRIAD-057 — Replay-Safe Event Identity and Side-Effect Ledger

**Why it matters:** PROPOSED — At-least-once delivery, retries, reordered events, and worker restarts can duplicate consequential effects even when the underlying transform is deterministic.

**Source IDs:** `SRC-NEW423`, `SRC-PIPE`, `SRC-GREEN`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0169` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should separate deterministic event identity, delivery attempt, processing result, side-effect intent, effect reservation, effect completion, and replay outcome so duplicate delivery cannot silently repeat a consequential action. |
| `KFM-CAND-0170` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let operators trace an event through deliveries, retries, locks or reservations, completed effects, stale attempts, poison handling, compensations, and final finite state without interpreting retry count as work completed. |
| `KFM-CAND-0171` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define GovernedEventEnvelope, DeliveryAttempt, SideEffectIntent, and EffectLedgerEntry contracts with deterministic identity, compare-and-set reservation, idempotency scope, ordering, replay, crash recovery, compensation, and duplicate-delivery fixtures. |

**Implementation-surface note:** PROPOSED — Exactly-once claims should be avoided unless the complete transport, reservation, effect, and recovery boundary is proven; otherwise report at-least-once delivery with idempotent effects.

**Carry-forward state:** NEW_GAP_FILL. Idempotence and replay safety are widely required, but a common event-to-effect ledger remains **NEEDS VERIFICATION**.

### KFM-TRIAD-058 — Conditional Decision Obligations and Closure

**Why it matters:** PROPOSED — “Approved with obligations” is unsafe when required conditions can be lost between review, policy evaluation, transformation, and release.

**Source IDs:** `SRC-NEW423`, `SRC-GREEN`, `SRC-ENCYC`, `SRC-GAI`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0172` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should treat conditional approval as a set of versioned obligations whose application, evidence, satisfaction, waiver, expiry, violation, reopening, supersession, and correction remain explicit and fail closed for consequential transitions. |
| `KFM-CAND-0173` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should show every active obligation, responsible steward, due or expiry condition, satisfaction evidence, waiver authority, affected artifacts and releases, unmet consequences, and downstream reopening or withdrawal state. |
| `KFM-CAND-0174` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should define ConditionalDecision, ObligationRecord, and ObligationClosureDecision contracts with applicability, dependency, satisfaction evidence, waiver, expiry, re-evaluation, correction, and release-blocking negative fixtures. |

**Implementation-surface note:** PROPOSED — An obligation is not closed by a text field or reviewer assertion alone; the accepted closure profile must bind evidence and authority appropriate to its significance.

**Carry-forward state:** NEW_GAP_FILL. Review records contain obligation concepts, while end-to-end application and closure enforcement remain **PARTIAL**.

### KFM-TRIAD-059 — Reversible Entity Reconciliation and Conflict-Preserving Dedupe

**Why it matters:** PROPOSED — Automatic winner-takes-all deduplication can merge distinct entities, erase source disagreement, and make later correction impossible.

**Source IDs:** `SRC-NEW425`, `SRC-FAUNA`, `SRC-FLORA`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0175` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should preserve source-native entity assertions and treat match, non-match, merge, split, cluster, and unresolved conflict as reversible decisions supported by versioned evidence rather than destructive normalization. |
| `KFM-CAND-0176` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should let stewards compare candidate entities, inspect contributing and conflicting attributes, approve or reject matches, split prior clusters, restore source views, and see every downstream artifact affected by reconciliation changes. |
| `KFM-CAND-0177` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define MatchProposal, ReconciliationDecision, EntityCluster, and SplitDecision objects with blocking keys, feature evidence, confidence limits, authority roles, transitivity guards, reversal, correction, and false-merge fixtures. |

**Implementation-surface note:** PROPOSED — Similar names, rounded geometry, dates, or identifiers can generate candidates but must not silently decide identity or delete losing assertions.

**Carry-forward state:** NEW_GAP_FILL. Domain identity and dedupe rules exist, but a reusable reversible reconciliation family remains **PARTIAL**.

### KFM-TRIAD-060 — Taxonomic Concept and Name-Usage Lineage

**Why it matters:** PROPOSED — A scientific-name string can refer to different circumscriptions over time, while one taxon concept can accumulate synonyms, misapplications, splits, lumps, and competing treatments.

**Source IDs:** `SRC-NEW425`, `SRC-FLORA`, `SRC-FAUNA`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0178` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should separate source-native NameUsage from TaxonConcept and preserve authorship, rank, treatment, valid time, concept relation, source role, and unresolved disagreement instead of treating an accepted-name string as timeless identity. |
| `KFM-CAND-0179` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show accepted-for-use context, synonyms, homonyms, misapplied names, split and lump history, source treatments, unresolved mappings, affected occurrence or distribution claims, and the version used for a query or release. |
| `KFM-CAND-0180` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should define NameUsage, TaxonConcept, ConceptRelation, and TaxonomyReconciliationDecision contracts with source-native identifiers and synthetic synonym, homonym, split, lump, misapplication, unresolved, supersession, and reversal fixtures. |

**Implementation-surface note:** PROPOSED — A versioned reconciliation profile may select a working concept for a declared use, but it must retain the source treatments and must not imply universal taxonomic authority.

**Carry-forward state:** NEW_GAP_FILL. Flora and fauna crosswalks exist, while a common cross-domain concept and name-usage lineage remains **PARTIAL**.

### KFM-TRIAD-061 — Place-Name Authority and Temporal Alias Graph

**Why it matters:** PROPOSED — Official, variant, historical, translated, community, and disputed names can change independently of a feature's existence, geometry, legal status, or ownership.

**Source IDs:** `SRC-NEW425`, `SRC-SETTLE`, `SRC-ROADS`, `SRC-TEMPORAL`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0181` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should model place names as time-bounded, source-role-bound assertions linked to but distinct from feature identity, geometry, jurisdiction, legal status, and ownership. |
| `KFM-CAND-0182` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should support search across official, variant, historical, translated, superseded, and disputed names while disclosing source, valid time, language or community context, feature binding, ambiguity, and withheld-sensitive-name posture. |
| `KFM-CAND-0183` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should define PlaceNameAssertion, TemporalAliasEdge, FeatureNameBinding, and NameAuthorityDecision contracts with collision, homonym, rename, translation, dispute, unbound name, feature split or merge, and supersession fixtures. |

**Implementation-surface note:** PROPOSED — A GNIS or other authority record can support a name assertion; separate evidence is required for existence, geometry, boundary, ownership, legal status, or historical interpretation.

**Carry-forward state:** NEW_GAP_FILL. GNIS, historical gazetteer, and place-identity surfaces exist, but a common temporal name-authority graph remains **PARTIAL**.

### KFM-TRIAD-062 — Survey-Control and Boundary Derivation Provenance

**Why it matters:** PROPOSED — Survey records, monuments, measurements, adjustments, plats, field notes, and georeferenced images can support a boundary derivation without making that derivation exact or legally authoritative.

**Source IDs:** `SRC-NEW425`, `SRC-GIS`, `SRC-TEMPORAL`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0184` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should preserve survey observation, monument or control status, survey generation, adjustment, georeference, residual, transformation, derived geometry, valid time, source role, and legal-use limitation as distinct provenance. |
| `KFM-CAND-0185` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | MAP - Map Surface, MapLibre, Tiles, Styling | PROPOSED — KFM should show whether geometry is source-recorded, reconstructed, adjusted, georeferenced, interpolated, generalized, conflicting, or unresolved together with residuals, control status, source vintage, derivation lineage, and non-survey or non-legal-use warnings. |
| `KFM-CAND-0186` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should define SurveyObservation, ControlStatusEvent, GeoreferenceReport, BoundaryDerivation, and SurveyFitnessDecision objects with conflicting-control, lost-monument, adjustment, high-residual, datum, temporal, incomplete-record, and legal-authority abstention fixtures. |

**Implementation-surface note:** PROPOSED — PLSS, CadNSDI, GLO plats, and field notes are valuable survey-control evidence; they must not be described as a universal ground-truth lattice, spatial checksum, title record, or public-safety clearance.

**Carry-forward state:** NEW_GAP_FILL. Source-product documentation exists, while a common survey-to-derived-boundary provenance contract remains **NEEDS VERIFICATION**.

### KFM-TRIAD-063 — Adversarial Validator Assurance and Mutation Adequacy

**Why it matters:** PROPOSED — Positive fixtures, line coverage, and a green validator run do not prove that dangerous semantic changes or fail-open behavior would be detected.

**Source IDs:** `SRC-NEW425`, `SRC-GREEN`, `SRC-PIPE`, `SRC-GAI`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0187` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should assess release-critical validators and policies with adversarial semantic mutations, property checks, negative fixtures, and gap-class coverage rather than treating execution or line coverage as sufficient assurance. |
| `KFM-CAND-0188` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers inspect tested invariants, mutant classes, killed and surviving mutants, equivalent or waived rationale, untested finite outcomes, dependency and network posture, and the consequence of each assurance gap. |
| `KFM-CAND-0189` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define ValidatorAssurancePlan and MutationAssessmentReport with deterministic no-network mutants for removed required fields, inverted allow or deny, bypassed abstention, stale profile, altered authority, skipped signature check, truncated evidence, and swallowed failure. |

**Implementation-surface note:** PROPOSED — Mutation score is evidence about the tested mutant set, not a universal quality grade. Any threshold requires owner-approved significance and equivalent-mutant handling.

**Carry-forward state:** NEW_GAP_FILL. Policy and validator tests exist, while cross-cutting mutation adequacy and semantic gap reporting remain **NEEDS VERIFICATION**.

### KFM-TRIAD-064 — Bitemporal Verification-State Replay

**Why it matters:** PROPOSED — Corrections, revocations, late-arriving evidence, policy changes, and release transitions can change current verification state without changing what was known, recorded, or considered valid at an earlier time.

**Source IDs:** `SRC-NEW414`, `SRC-TEMPORAL`, `SRC-GREEN`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0190` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should represent every verification-state change with subject identity, state, reason, effective time, recorded time, predecessor, authority, evidence, policy profile, and trust profile so current and `as_of` answers remain reproducible without rewriting prior history. |
| `KFM-CAND-0191` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should let reviewers replay verification state at a declared time, distinguish late-recorded from backdated-effective events, inspect active evidence and release context, and follow supersession, correction, rollback, and revocation edges. |
| `KFM-CAND-0192` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should define VerificationStateEvent, VerificationStateGraph, AsOfVerificationQuery, and VerificationReplayReport contracts with synthetic active, late-recorded, corrected, superseded, revoked, missing-predecessor, cyclic, ambiguous, and unknown-history fixtures. |

**Implementation-surface note:** PROPOSED — Event effective time, KFM recorded time, decision time, release time, and query `as_of` time must remain distinct. Replay reports recorded knowledge under a declared profile; it does not retroactively make an earlier claim true.

**Carry-forward state:** NEW_GAP_FILL. Temporal and correction doctrine exists, while one reusable bitemporal verification-state replay contract remains **NEEDS VERIFICATION**.

### KFM-TRIAD-065 — Source-Conflict Topology and Influence Accounting

**Why it matters:** PROPOSED — Individually admissible sources can still disagree because of role, time, scale, support, precision, method, uncertainty, or revocation, and a source count or average can hide the conflict.

**Source IDs:** `SRC-NEW414`, `SRC-GAI`, `SRC-GREEN`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0193` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | PROPOSED — KFM should assess jointly used sources under a versioned comparison profile that preserves source roles and classifies their relationship as consistent, divergent, conflicting, insufficient, inapplicable, or containing revoked evidence before producing a finite result. |
| `KFM-CAND-0194` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | PROPOSED — KFM should show compared inputs, eligibility and exclusions, comparison axes, tolerance-profile identity, conflict class, uncertainty, and which sources were dominant, contributing, context-only, excluded, or non-influential in the result. |
| `KFM-CAND-0195` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should define SourceConflictProfile, SourceComparison, InfluenceLedger, and FederationDecision contracts with unit, scale, time, precision, support, source-role, missingness, revocation, threshold-boundary, order-invariance, and irreconcilable-conflict fixtures. |

**Implementation-surface note:** PROPOSED — Comparison eligibility and tolerance are declared policy/contract inputs, not hidden scientific constants. Conflict does not authorize averaging, majority voting, authority-role collapse, or publication.

**Carry-forward state:** NEW_GAP_FILL. Corroboration roles and composed-claim closure exist, while common conflict topology and source-influence accounting remain **PARTIAL**.

### KFM-TRIAD-066 — Cross-Layer Outcome Projection and Parity

**Why it matters:** PROPOSED — A valid finite outcome can be corrupted when policy, release, runtime, API, UI, export, or cache layers rename, omit, upgrade, or collapse its state and reasons.

**Source IDs:** `SRC-NEW414`, `SRC-NEW415`, `SRC-GAI`, `SRC-MAP`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0196` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | PROPOSED — KFM should preserve finite-outcome meaning and reason lineage across policy, release, runtime, API, UI, export, and cache projections through a versioned matrix of allowed transformations, permitted degradations, and prohibited upgrades. |
| `KFM-CAND-0197` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers inspect each projection step, input and output outcome, reason-code mapping, omitted fields, authorized degradation, policy/profile identity, and any parity failure before a consequential surface is trusted. |
| `KFM-CAND-0198` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define OutcomeProjectionProfile, OutcomeProjectionStep, and OutcomeParityReport contracts with synthetic ANSWER, ABSTAIN, DENY, ERROR, redacted, stale, unavailable, reason-loss, empty-success, cache, and unauthorized-upgrade fixtures. |

**Implementation-surface note:** PROPOSED — Parity does not require every layer to expose the same shape or current outcome. A later runtime may safely degrade because of freshness or revocation, but any difference must be allowed by the pinned profile and preserve its reason.

**Carry-forward state:** NEW_GAP_FILL. Finite outcomes and some lane-specific parity checks exist, while a common cross-layer projection contract remains **PARTIAL**.

### KFM-TRIAD-067 — Verifier Profile and Capability Portability

**Why it matters:** PROPOSED — CI, server, desktop, browser, and offline verifiers may support different algorithms, canonicalization profiles, trust material, revocation inputs, dependencies, network posture, and resource limits.

**Source IDs:** `SRC-NEW414`, `SRC-NEW415`, `SRC-GREEN`, `SRC-MAPMASTER`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0199` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should interpret verification only relative to an explicit verifier profile that binds supported algorithms, canonicalization, trust and revocation inputs, dependency versions, network posture, time source, and resource limits; unsupported capability must produce an explicit fail-safe result. |
| `KFM-CAND-0200` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should show verifier identity, environment class, profile and dependency versions, available and missing capabilities, trust freshness, network assumptions, resource limits, attempted checks, and whether results are portable, qualified, unsupported, or incomparable. |
| `KFM-CAND-0201` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | PROPOSED — KFM should define VerifierProfile, VerificationCapabilityClaim, VerificationAttempt, and PortabilityAssessment contracts with synthetic CI, browser, offline, unsupported-algorithm, canonicalization-mismatch, stale-trust, missing-revocation, dependency-drift, clock, network, and resource-exhaustion fixtures. |

**Implementation-surface note:** PROPOSED — Equivalent verification requires equivalent accepted inputs and semantics, not merely the same green label. Library availability or network success must not silently change truth, policy, review, or release authority.

**Carry-forward state:** NEW_GAP_FILL. Offline trust, signing, and integrity-before-render exist, while explicit verifier capability and portability assessment remain **PARTIAL**.

### KFM-TRIAD-068 — Source-Native Quality Translation and Health Separation

**Why it matters:** PROPOSED — A source-native quality code, normalized quality interpretation, station or sensor health state, and the validity or fitness of one observation answer different questions and can change independently.

**Source IDs:** `SRC-NEW415`, `SRC-SOIL`, `SRC-ATM`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0202` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | PROPOSED — KFM should preserve source-native quality vocabulary and code, vocabulary version, mapping rule and version, normalized interpretation, semantic loss, unmapped state, station or sensor health, observation validity, analytic fitness, and decision reason as separate lineage. |
| `KFM-CAND-0203` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers compare native and normalized quality, inspect mapping evidence and loss, distinguish offline or maintenance state from invalid reading and missing support, and see which declared uses admit, exclude, quarantine, deny, or abstain from the observation. |
| `KFM-CAND-0204` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define NativeQualityAssertion, QualityMappingDecision, SourceHealthEvent, ObservationValidityDecision, and ObservationFitnessDecision contracts with known, unknown, contradictory, deprecated, lossy, offline, maintenance, calibration, invalid-value, stale, missing-depth, missing-support, and valid fixtures. |

**Implementation-surface note:** PROPOSED — Normalization may make quality comparable for a declared use, but it must not erase the native assertion or upgrade source role. Operational outage must not become an environmental condition or a valid absence claim.

**Carry-forward state:** NEW_GAP_FILL. Soil and atmosphere lanes preserve many fields, while a reusable cross-domain translation and health-separation contract remains **PARTIAL**.

### KFM-TRIAD-069 — Generated Runtime-Proof Artifact Lifecycle

**Why it matters:** PROPOSED — A generated runtime response is useful comparison evidence, but committing every actual, treating a passing output as truth, or silently replacing a golden fixture creates noise and weakens review.

**Source IDs:** `SRC-NEW415`, `SRC-GREEN`, `SRC-PIPE`, `SRC-ENCYC`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0205` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | DAT - Data Lifecycle, Provenance, Receipts | PROPOSED — KFM should govern generated runtime-proof artifacts through explicit ephemeral, retained-for-review, promoted-golden, stale, invalidated, corrected, and deleted states while preserving runner, contract, fixture, configuration, dependency, environment, and digest identity. |
| `KFM-CAND-0206` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should let reviewers inspect actual-versus-expected differences, generation provenance, determinism and redaction posture, retention and expiry, review decision, golden-promotion rationale, affected tests, and later invalidation or correction. |
| `KFM-CAND-0207` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define RuntimeProofArtifactRecord, GoldenPromotionDecision, and ProofArtifactInvalidationNotice contracts with synthetic ephemeral, retained, promoted, rejected, nondeterministic, sensitive, stale-contract, dependency-drift, expired, invalidated, corrected, and deleted fixtures. |

**Implementation-surface note:** PROPOSED — Generated actuals should be ephemeral by default. Deliberate golden promotion makes an expected test artifact under a declared profile; it does not make the response official evidence, canonical data, or publication authority.

**Carry-forward state:** NEW_GAP_FILL. Runtime proof and golden fixtures exist, while their shared generated-artifact lifecycle remains **NEEDS VERIFICATION**.

### KFM-TRIAD-070 — Observed Interface Evolution and Compatibility Window

**Why it matters:** PROPOSED — Source interfaces evolve through undocumented drift, version change, redirects, deprecation, dual operation, and retirement, while transport metadata and sample responses provide only partial observations.

**Source IDs:** `SRC-NEW414`, `SRC-NEW415`, `SRC-PIPE`, `SRC-DIR`

| Candidate key | Class | Stable ID template | Category | Normalized statement |
|---|---|---|---|---|
| `KFM-CAND-0208` | `idea` | `KFM-P{PASS}-IDEA-{NNNN}` | SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | PROPOSED — KFM should preserve declared interface identity separately from observed behavior and govern discovery, compatibility, deprecation, dual-read, migration, rollback, consumer debt, retirement, and correction without treating URL, ETag, timestamp, redirect, or one sample as canonical identity. |
| `KFM-CAND-0209` | `feature` | `KFM-P{PASS}-FEAT-{NNNN}` | DOC - Documentation, Doctrine, Reader Surfaces | PROPOSED — KFM should show declared and observed contract/profile versions, observation evidence, changed capabilities, compatibility class, affected consumers, dual-read comparison, deprecation and sunset signals, migration decision, rollback readiness, and retirement blockers. |
| `KFM-CAND-0210` | `programming` | `KFM-P{PASS}-PROG-{NNNN}` | PIP - Pipelines, Pipeline Specs, Validators | PROPOSED — KFM should define InterfaceObservation, CompatibilityAssessment, InterfaceMigrationDecision, and InterfaceRetirementRecord contracts with synthetic unchanged, additive, breaking, redirect, undocumented, partial-sample, dual-read mismatch, rollback, consumer-blocked, retired, and reactivated fixtures. |

**Implementation-surface note:** PROPOSED — A watcher records interface evidence and may open review work; it must not silently rewrite a connector, change canonical identity, activate a replacement, retire a consumer, or publish data.

**Carry-forward state:** NEW_GAP_FILL. Source-specific deprecation and interface-drift guidance exists, while a common compatibility-window and retirement contract remains **PARTIAL**.

---

## 11. Category distribution

| Category | Count |
|---|---:|
| PIP - Pipelines, Pipeline Specs, Validators | 46 |
| UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer | 28 |
| MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL | 23 |
| MAP - Map Surface, MapLibre, Tiles, Styling | 20 |
| DOC - Documentation, Doctrine, Reader Surfaces | 19 |
| DAT - Data Lifecycle, Provenance, Receipts | 17 |
| POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension) | 15 |
| ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation | 12 |
| SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension) | 9 |
| EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain | 8 |
| REL - Catalog Closure, Publication, Release, Rollback, Recompile | 7 |
| SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension) | 6 |

---

## 12. Source-use distribution

| Source ID | Card count |
|---|---:|
| `SRC-ENCYC` | 135 |
| `SRC-GREEN` | 54 |
| `SRC-PIPE` | 51 |
| `SRC-P20` | 48 |
| `SRC-MAPMASTER` | 33 |
| `SRC-NEW430` | 33 |
| `SRC-GAI` | 30 |
| `SRC-MAP` | 30 |
| `SRC-NEW416` | 30 |
| `SRC-ATM` | 24 |
| `SRC-FAUNA` | 21 |
| `SRC-TEMPORAL` | 21 |
| `SRC-NEW414` | 15 |
| `SRC-NEW415` | 15 |
| `SRC-NEW423` | 15 |
| `SRC-NEW425` | 15 |
| `SRC-AIREF` | 12 |
| `SRC-DIR` | 12 |
| `SRC-FLORA` | 12 |
| `SRC-GIS` | 12 |
| `SRC-P18` | 12 |
| `SRC-SOIL` | 12 |
| `SRC-HYD` | 9 |
| `SRC-PEOPLE` | 9 |
| `SRC-ROADS` | 9 |
| `SRC-URBAN` | 9 |
| `SRC-3DGIS` | 6 |
| `SRC-ARCH` | 6 |
| `SRC-HABFAUNA` | 6 |
| `SRC-NEW510` | 6 |
| `SRC-NEW515` | 6 |
| `SRC-NEW58` | 6 |
| `SRC-SETTLE` | 6 |
| `SRC-AGRI` | 3 |
| `SRC-APIREF` | 3 |
| `SRC-GEO` | 3 |
| `SRC-HAB` | 3 |
| `SRC-HAZ` | 3 |
| `SRC-OLL` | 3 |
| `SRC-UIAI` | 3 |

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

### Slice E — Deterministic diff, materiality, and hash semantics

Use cards:

- `KFM-CAND-0097`
- `KFM-CAND-0098`
- `KFM-CAND-0099`
- `KFM-CAND-0124`
- `KFM-CAND-0125`
- `KFM-CAND-0126`

Goal: implement the existing stable top-level JSON-diff gap with synthetic fixtures, then define separate contract-level hash profiles and materiality decisions so byte inequality never becomes automatic promotion.

### Slice F — Correctable synthetic atmosphere event

Use cards:

- `KFM-CAND-0103`
- `KFM-CAND-0104`
- `KFM-CAND-0105`
- `KFM-CAND-0106`
- `KFM-CAND-0107`
- `KFM-CAND-0108`
- `KFM-CAND-0109`
- `KFM-CAND-0110`
- `KFM-CAND-0111`

Goal: prove, with no-network synthetic fixtures only, that observation, candidate, event, correction, baseline, and corroboration roles remain distinct and produce finite outcomes. Do not activate live feeds or publish an alert layer.

### Slice G — Governed temporal carrier

Use cards:

- `KFM-CAND-0115`
- `KFM-CAND-0116`
- `KFM-CAND-0117`
- `KFM-CAND-0118`
- `KFM-CAND-0119`
- `KFM-CAND-0120`

Goal: define a digest-bound TimeBucketManifest and deterministic offline STAC record/link-closure fixtures that preserve time kinds, release refs, evidence handoffs, accessibility, and MapLibre adapter boundaries.

### Slice H — Historical uncertainty join

Use cards:

- `KFM-CAND-0121`
- `KFM-CAND-0122`
- `KFM-CAND-0123`

Goal: use explicitly synthetic places and route segments to prove that approximate geometry, valid-time overlap, distance, and source roles produce a qualified proximity candidate rather than a historical or causal claim.

### Slice I — Retrieval and biodiversity meaning

Use cards:

- `KFM-CAND-0127` through `KFM-CAND-0138`

Goal: define retrieval intent, terms snapshots, sampling effort, non-detection, distribution state, and coverage semantics before any new USDA PLANTS, eBird, or GBIF adapter is activated. Use synthetic rows and no-network fixtures only.

### Slice J — Coverage-aware work selection

Use cards:

- `KFM-CAND-0139`
- `KFM-CAND-0140`
- `KFM-CAND-0141`

Goal: compare a density-led county ranking with a coverage-gap-led ranking and prove that the score is an inspectable work-priority aid, not a biodiversity, conservation, or publication claim.

### Slice K — Measurement, latency, and transfer state

Use cards:

- `KFM-CAND-0142` through `KFM-CAND-0150`

Goal: use synthetic grid, station, delayed-product, and interrupted-download fixtures to preserve measurement support, expected delivery latency, partial state, retries, final bytes, and finite outcomes without activating an external source.

### Slice L — Offline trust and verified rendering

Use cards:

- `KFM-CAND-0151` through `KFM-CAND-0156`

Goal: define one public-safe synthetic OfflineReleaseCapsule and prove atomic install, integrity-before-render, resource-budget failure, expiry, correction, withdrawal, reconnect synchronization, and rollback without adding a peer renderer.

### Slice M — Correctable observation fitness

Use cards:

- `KFM-CAND-0106` through `KFM-CAND-0111`
- `KFM-CAND-0157`
- `KFM-CAND-0158`
- `KFM-CAND-0159`

Goal: prove that a synthetic environmental observation can be retained as evidence yet excluded from a declared analytic use because of a pinned confounder or quality profile, with visible reasons and correction lineage.

### Slice N — Custody and replay invariants

Use cards:

- `KFM-CAND-0160` through `KFM-CAND-0162`
- `KFM-CAND-0169` through `KFM-CAND-0171`

Goal: use synthetic sender, receiver, event, delivery, and side-effect records to prove conservation, partial acceptance, duplicate delivery, crash recovery, reconciliation, and exactly one idempotent effect without activating a live pipeline or broker.

### Slice O — Composed claim and conditional obligation closure

Use cards:

- `KFM-CAND-0163` through `KFM-CAND-0165`
- `KFM-CAND-0172` through `KFM-CAND-0174`

Goal: prove that missing or denied required evidence narrows or blocks a composed claim and that a conditional review decision cannot authorize release until every applicable obligation reaches an evidence-backed finite closure.

### Slice P — Historical trust verification

Use cards:

- `KFM-CAND-0166`
- `KFM-CAND-0167`
- `KFM-CAND-0168`

Goal: use synthetic keys and trust-profile versions to distinguish currently trusted, historically valid, expired, revoked, compromised, unknown, offline, and policy-mismatched signatures without treating signature success as truth or release.

### Slice Q — Reversible identity, taxonomy, and place names

Use cards:

- `KFM-CAND-0175` through `KFM-CAND-0183`

Goal: use synthetic entities, taxonomic treatments, and place-name histories to prove match proposals, merge/split reversal, source-native assertion retention, synonym/homonym/split/lump lineage, temporal aliases, disputes, and role separation without fetching or publishing live records.

### Slice R — Survey-control provenance

Use cards:

- `KFM-CAND-0184`
- `KFM-CAND-0185`
- `KFM-CAND-0186`

Goal: bind synthetic survey observations, monument status, adjustment, georeferencing, residuals, derived geometry, and fitness limitations while proving that survey-control evidence does not become legal-boundary or ownership authority.

### Slice S — Adversarial validator assurance

Use cards:

- `KFM-CAND-0187`
- `KFM-CAND-0188`
- `KFM-CAND-0189`

Goal: run a no-network mutation proof against one accepted release-critical validator or policy and report killed, surviving, equivalent, and waived mutants by semantic gap class without inventing a universal score threshold.

### Slice T — Verification history and source conflict replay

Use cards:

- `KFM-CAND-0190` through `KFM-CAND-0195`

Goal: use synthetic verification events and source observations to replay state before and after correction/revocation, classify consistent, divergent, conflicting, insufficient, and revoked-source combinations, and prove source influence without averaging, voting, or rewriting history.

### Slice U — Outcome parity and verifier portability

Use cards:

- `KFM-CAND-0196` through `KFM-CAND-0201`

Goal: define one allowed outcome-projection matrix and one verifier-profile matrix, then catch reason loss, prohibited outcome upgrade, unsupported capability, stale trust, canonicalization mismatch, dependency drift, and resource failure without adding browser or live-signing dependencies.

### Slice V — Quality, generated proof, and interface evolution

Use cards:

- `KFM-CAND-0202` through `KFM-CAND-0210`

Goal: use synthetic quality codes, station-health events, observations, runtime actuals, golden decisions, and old/new interface descriptions to preserve native meaning, separate health from validity, govern generated proof artifacts, and prove a reversible compatibility window without activating a source.

---

## 15. Validation checklist

Before merging this register:

- [ ] Confirm the final repository path.
- [x] Check for duplicate prior atlas-card files.
- [ ] Check whether any card already has a real pass ID.
- [ ] Decide whether proposed extension categories require vocabulary ADR.
- [ ] Run Markdown lint.
- [x] Run deterministic local link and anchor checks after adding repo links.
- [x] Verify no exact sensitive locations are included.
- [x] Verify no raw source data is embedded.
- [x] Verify `SRC-NEW416` identity, digest, byte count, page count, and source-map link.
- [x] Verify `SRC-NEW414` identity, digest, byte count, page count, Pass 23 lineage, and source-map link.
- [x] Verify `SRC-NEW415` identity, digest, byte count, page count, Pass 23 lineage, and source-map link.
- [x] Verify `SRC-NEW423` identity, digest, byte count, page count, and source-map link.
- [x] Verify `SRC-NEW425` identity, digest, byte count, page count, and source-map link.
- [x] Verify `SRC-NEW430` identity, digest, byte count, page count, and source-map link.
- [x] Verify the April 16 packet's paste-ready code and generic paths are not promoted as repository authority.
- [x] Verify the April 14 packet's watcher, policy, hydrology, package, browser-verifier, signature, release, and peer-renderer code is not promoted as repository authority.
- [x] Verify the April 15 packet's soil, HLS/STAC, people/consent, route, workflow, threshold, runtime-output, and peer-renderer code is not promoted as repository authority.
- [x] Verify the April 23 packet's parallel evidence stack, key-service recipes, event actions, obligation shortcuts, and publication paths are not promoted as repository authority.
- [x] Verify the April 25 packet's loaders, authority rankings, PLSS overclaims, GNIS role collapse, policy thresholds, network installs, AI promotion, and sensitive examples are not promoted as repository authority.
- [x] Verify the April 30 packet's loaders, paths, thresholds, external-service facts, cloud examples, signatures, and UI code are not promoted as repository authority.
- [x] Verify Cesium/CZML remains excluded from implementation candidates pending accepted renderer authority.
- [x] Verify query, terms, sampling, distribution, measurement, latency, transfer, offline, rendering, and observation-fitness cards preserve evidence, policy, review, release, correction, and rollback boundaries.
- [x] Verify custody, composed claims, trust-root history, replay, obligations, reconciliation, taxonomy, place names, survey control, and validator assurance preserve independent authority and finite outcomes.
- [x] Verify sender receipt does not become receiver acceptance, signature does not become truth, duplicate delivery does not become duplicate effect, obligation text does not become closure, scientific-name string does not become concept identity, GNIS name does not become geometry or legal status, and survey control does not become title authority.
- [x] Verify current verification state does not rewrite historical `as_of` state, source count does not become consensus, permitted degradation does not become outcome upgrade, verifier availability does not become verification truth, native quality does not disappear into normalized quality, station outage does not become environmental absence, generated actual does not become golden or official truth, and transport metadata does not become interface or content identity.
- [x] Verify no missing distribution row becomes absence, no record-density score becomes ecological richness, and no successful signature becomes truth or release authority.
- [x] Verify materiality, corroboration, consent, hashing, and proximity cards preserve independent evidence, policy, review, release, correction, and rollback gates.
- [x] Verify all implementation claims remain PROPOSED or UNKNOWN unless repository evidence supports them.
- [x] Verify all path proposals are marked PROPOSED or explicitly identified as existing workspace paths.
- [x] Add this file to the appropriate docs index.
- [x] Confirm that no drift-register entry is required merely to retain and update the existing atlas register in place.

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
{"candidate_key":"KFM-CAND-0097","triad_id":"KFM-TRIAD-033","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Material Change Classification and Non-Event Receipts Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should distinguish byte change, schema change, semantic change, source-role change, rights or sensitivity change, material domain change, and release-significant change instead of treating hash inequality as one state.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0098","triad_id":"KFM-TRIAD-033","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Material Change Classification and Non-Event Receipts Capability","category":"REL - Catalog Closure, Publication, Release, Rollback, Recompile","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect the applicable materiality profile, before and after metrics, threshold evidence, decision reason, affected scope, and explicit non-material disposition without implying publication.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0099","triad_id":"KFM-TRIAD-033","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Material Change Classification and Non-Event Receipts Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-PIPE","SRC-P20"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define versioned MaterialityProfile, ChangeAssessment, and NonMaterialChangeReceipt objects whose inputs, exclusions, thresholds, policy refs, and replay context are deterministic and whose outputs cannot publish.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0100","triad_id":"KFM-TRIAD-034","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Identifier and Precision Lineage Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-FAUNA","SRC-SOIL","SRC-HYD"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should preserve every source identifier verbatim while representing crosswalk, merge, split, surrogate, and unresolved identity decisions as time-aware assertions rather than destructive rewrites.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0101","triad_id":"KFM-TRIAD-034","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Identifier and Precision Lineage Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-FAUNA","SRC-SOIL","SRC-HYD"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show source identity, resolved identity, effective spatial precision, uncertainty class, generalization method, and public-versus-restricted derivative lineage wherever those differences affect interpretation.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0102","triad_id":"KFM-TRIAD-034","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Identifier and Precision Lineage Implementation Surface","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-FAUNA","SRC-SOIL","SRC-HYD"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define IdentifierAssertion, CrosswalkResolution, PrecisionProfile, and PrecisionTransformReceipt objects with source IDs, validity intervals, confidence, method version, reviewer state, and supersession links.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0103","triad_id":"KFM-TRIAD-035","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Correctable Environmental Event Lifecycle Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model environmental observations, candidates, local events, regional events, review dispositions, corrections, retractions, and supersessions as distinct time-aware object states with no automatic upward collapse.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0104","triad_id":"KFM-TRIAD-035","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Correctable Environmental Event Lifecycle Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose event scope, provisional status, persistence, corroboration, freshness, source roles, confidence limits, correction lineage, and finite outcome without presenting a candidate as a validated public event.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0105","triad_id":"KFM-TRIAD-035","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Correctable Environmental Event Lifecycle Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define EnvironmentalObservation, EventCandidate, EnvironmentalEvent, EventReviewDisposition, and EventCorrection contracts with transition guards, evidence refs, baseline refs, policy decisions, receipts, and rollback or withdrawal links.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0106","triad_id":"KFM-TRIAD-036","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Baseline Cohort and Drift Governance Pattern","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-AIREF"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat cohort eligibility, exclusions, lookback window, seasonal window, missingness, method continuity, sensor relocation, uncertainty floor, parameter choice, and recalculation cadence as part of baseline meaning.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0107","triad_id":"KFM-TRIAD-036","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Baseline Cohort and Drift Governance Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-AIREF"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide reviewer-readable baseline cards showing cohort coverage, excluded records, discontinuities, parameter versions, freshness, source roles, known blind spots, and fitness-for-use.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0108","triad_id":"KFM-TRIAD-036","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Baseline Cohort and Drift Governance Implementation Surface","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-AIREF"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define BaselineManifest, CohortEligibilityReport, DiscontinuityRecord, BaselineValidationReport, and BaselineRebuildReceipt with digest-bound inputs, parameter profiles, tool versions, and correction lineage.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0109","triad_id":"KFM-TRIAD-037","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Corroboration Role Graph Pattern","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-ENCYC","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should represent corroboration as qualified relations among observation, regulatory, remote-sensing interpretation, forecast, simulation, contextual, and derived sources rather than as a raw source count.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0110","triad_id":"KFM-TRIAD-037","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Corroboration Role Graph Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-ENCYC","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show which sources support, contradict, qualify, duplicate, or cannot evaluate a claim, including independence, freshness, spatial and temporal overlap, and role-specific limitations.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0111","triad_id":"KFM-TRIAD-037","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Corroboration Role Graph Implementation Surface","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ATM","SRC-ENCYC","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define CorroborationAssertion and SourceIndependenceAssessment contracts plus policy composition that fails closed on role collapse, unresolved contradictions, missing freshness, or prohibited role combinations.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0112","triad_id":"KFM-TRIAD-038","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Purpose-Bound Consent and Revocation Propagation Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-PEOPLE","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should bind consent to exact subject or representative authority, purpose, operation, fields, relationships, audience, retention, time, and revocation status while preserving independent evidence, rights, sensitivity, review, and release gates.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0113","triad_id":"KFM-TRIAD-038","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Purpose-Bound Consent and Revocation Propagation Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-PEOPLE","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide a consent-first review flow that previews transforms, discloses retained and sidecar fields, shows collateral-person impact, limits persistence before approval, and makes revocation and cleanup status inspectable to authorized stewards.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0114","triad_id":"KFM-TRIAD-038","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Purpose-Bound Consent and Revocation Propagation Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-PEOPLE","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define purpose-bound ConsentGrant, status or revocation lookup, RevocationReceipt, dependency index, CacheInvalidationReceipt, and synthetic no-network fixtures that prove the next consequential read, answer, export, tile, graph, index, and cache honors withdrawal.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0115","triad_id":"KFM-TRIAD-039","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Governed Time-Bucket Map Playback Pattern","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-MAP","SRC-MAPMASTER","SRC-TEMPORAL"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat feature filters, epoch buckets, PMTiles sources, worker-prepared indexes, animation windows, and camera transitions as downstream temporal carriers rather than valid-time authority or evidence.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0116","triad_id":"KFM-TRIAD-039","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Governed Time-Bucket Map Playback Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-MAP","SRC-MAPMASTER","SRC-TEMPORAL"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show the active window, cadence, valid, observed, source, retrieval, release, and correction time, precision, freshness, bucket identity, transition gaps, reduced-motion state, and evidence links during map playback.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0117","triad_id":"KFM-TRIAD-039","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Governed Time-Bucket Map Playback Implementation Surface","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-MAP","SRC-MAPMASTER","SRC-TEMPORAL"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define TimeBucketManifest, TemporalFilterEnvelope, bucket digest and release refs, governed worker-message schemas, swap and fallback state, and tests proving that filters and source changes preserve trust state and accepted MapLibre adapter boundaries.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0118","triad_id":"KFM-TRIAD-040","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"STAC Profile and Link-Closure Conformance Pattern","category":"REL - Catalog Closure, Publication, Release, Rollback, Recompile","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-P20","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should enforce a minimal, versioned STAC profile with query-critical spatial, temporal, collection, asset-role, projection, link, and provenance references while keeping full EvidenceBundle and PROV graphs outside STAC.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0119","triad_id":"KFM-TRIAD-040","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"STAC Profile and Link-Closure Conformance Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-P20","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should provide record, collection, graph-closure, API-conformance, and availability summaries as separate reviewer states so one green check cannot imply the others.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0120","triad_id":"KFM-TRIAD-040","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"STAC Profile and Link-Closure Conformance Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-P20","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should implement deterministic no-network validators for record shape, extension discipline, query-critical fields, asset roles, and local link closure plus separate fixtures for pagination, filters, field projection, broken graphs, placeholders, and optional live availability probes.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0121","triad_id":"KFM-TRIAD-041","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Historical Network Uncertainty and Temporal Joins Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ROADS","SRC-TEMPORAL","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model historical place assertions, route-segment assertions, designated modern alignments, approximate geocodes, valid-time intervals, and proximity candidates separately, with no automatic causal or service-network inference.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0122","triad_id":"KFM-TRIAD-041","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Historical Network Uncertainty and Temporal Joins Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ROADS","SRC-TEMPORAL","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let users explore post offices, settlements, and trails by time while seeing coordinate method, uncertainty geometry, route vintage, temporal overlap, distance band, source role, and interpretation caveats.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0123","triad_id":"KFM-TRIAD-041","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Historical Network Uncertainty and Temporal Joins Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-ROADS","SRC-TEMPORAL","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define HistoricalPlaceAssertion, HistoricalRouteSegment, ProximityCandidate, TemporalSpatialJoinReceipt, and public-safe tile projection rules with synthetic fixtures for exact, approximate, non-overlapping, ambiguous, and unsupported cases.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0124","triad_id":"KFM-TRIAD-042","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Purpose-Specific Hash Profiles Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should name and version distinct canonicalization profiles for specification identity, semantic record content, normalized geometry, artifact bytes, receipt payloads, and signed subjects, with explicit non-equivalence.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0125","triad_id":"KFM-TRIAD-042","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Purpose-Specific Hash Profiles Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect algorithm, profile version, included and excluded fields, geometry and numeric normalization, volatile-field handling, digest subject, test-vector status, and migration compatibility.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0126","triad_id":"KFM-TRIAD-042","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Purpose-Specific Hash Profiles Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW416","SRC-P20","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define CanonicalizationProfile and HashBinding contracts plus deterministic test vectors that reject self-hashing fields, signatures inside signed subjects, unstable timestamps, unordered collections, nonfinite numbers, ambiguous CRS, and cross-profile comparisons.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0127","triad_id":"KFM-TRIAD-043","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Retrieval Intent and Query Snapshot Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat retrieval intent, normalized query predicate, geographic and temporal scope, pagination, sampling, requested fields, and result selection as versioned provenance rather than an informal note attached after ingestion.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0128","triad_id":"KFM-TRIAD-043","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Retrieval Intent and Query Snapshot Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect the exact source descriptor version, query scope, requested fields, filters, exclusions, page or job boundaries, redacted authentication posture, result count, and deviations between planned and executed retrieval.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0129","triad_id":"KFM-TRIAD-043","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Retrieval Intent and Query Snapshot Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define RetrievalIntent, QuerySnapshot, and RetrievalReceipt contracts with deterministic parameter normalization, secret exclusion, descriptor refs, request and response digests, pagination closure, and finite incomplete or changed-query outcomes.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0130","triad_id":"KFM-TRIAD-044","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Source Terms Snapshot and Rights Drift Pattern","category":"SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-GREEN","SRC-PIPE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should preserve the exact terms, license, citation, attribution, redistribution, commercial-use, retention, access, and verification posture that governed each retrieval and should treat later terms drift as a new rights decision.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0131","triad_id":"KFM-TRIAD-044","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Source Terms Snapshot and Rights Drift Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-GREEN","SRC-PIPE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show the verified-at time, terms or license identifier, evidence reference, permitted and prohibited uses, attribution duties, downstream obligations, uncertainty, supersession, and whether existing products require hold, recomputation, withdrawal, or no action.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0132","triad_id":"KFM-TRIAD-044","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Source Terms Snapshot and Rights Drift Implementation Surface","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-GREEN","SRC-PIPE"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define SourceTermsSnapshot, RightsAssessment, and TermsChangeDecision objects plus policy tests that fail closed on missing evidence, scope mismatch, expired permission, license incompatibility, or unpropagated obligations.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0133","triad_id":"KFM-TRIAD-045","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Sampling Effort and Non-Detection Support Pattern","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-FAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should bind every detection or non-detection inference to explicit sampling effort, protocol, completeness, observer or instrument opportunity, spatial and temporal support, target scope, and known detectability limits.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0134","triad_id":"KFM-TRIAD-045","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Sampling Effort and Non-Detection Support Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-FAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should distinguish observed detection, supported non-detection, not sampled, incomplete effort, unknown effort, suppressed result, and stale coverage while showing effort intensity and blind spots without exposing protected observer or species locations.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0135","triad_id":"KFM-TRIAD-045","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Sampling Effort and Non-Detection Support Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-FAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define SamplingEvent, DetectionOpportunity, EffortProfile, and NonDetectionAssertion contracts with pair-coherence checks, completeness flags, protocol fields, privacy transforms, and negative fixtures proving that missing or incompatible effort returns ABSTAIN or DENY.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0136","triad_id":"KFM-TRIAD-046","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Distribution Assertion and Coverage Semantics Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-FLORA","SRC-FAUNA","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model present, explicitly absent, not assessed, unknown, suppressed, disputed, stale, and out-of-scope distribution states as assertions bound to source, vocabulary, geography version, valid time, and evidence support.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0137","triad_id":"KFM-TRIAD-046","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Distribution Assertion and Coverage Semantics Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-FLORA","SRC-FAUNA","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should map distribution status, survey or reporting coverage, source vintage, boundary version, precision, sensitivity transform, and limitations separately so blank geography is never rendered as absence and occurrence density is never rendered as abundance.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0138","triad_id":"KFM-TRIAD-046","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Distribution Assertion and Coverage Semantics Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-FLORA","SRC-FAUNA","SRC-GIS"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define DistributionAssertion, CoverageAssessment, DistributionStatusProfile, and GeographyBinding objects with source-native status preservation, FIPS or boundary crosswalk refs, supersession, and fixtures for missing rows, changed boundaries, conflicting sources, and unsupported first-observed dates.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0139","triad_id":"KFM-TRIAD-047","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Coverage-Aware Prioritization and Exploration-Bias Control Pattern","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-AIREF","SRC-ENCYC","SRC-URBAN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should separate data-richness, recency, sampling effort, source diversity, geographic coverage gaps, uncertainty reduction, sensitivity burden, steward capacity, and public value when prioritizing new work.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0140","triad_id":"KFM-TRIAD-047","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Coverage-Aware Prioritization and Exploration-Bias Control Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-AIREF","SRC-ENCYC","SRC-URBAN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should explain why an area was prioritized, show every score component and blind spot, compare density-led and gap-led rankings, and label the result as workflow triage rather than biodiversity richness or conservation importance.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0141","triad_id":"KFM-TRIAD-047","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Coverage-Aware Prioritization and Exploration-Bias Control Implementation Surface","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-AIREF","SRC-ENCYC","SRC-URBAN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define CoveragePriorityProfile and PriorityScorecard with versioned weights, source-role caps, missingness treatment, sensitivity and review costs, counterfactual rankings, stability checks, and receipts that cannot authorize source activation or publication.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0142","triad_id":"KFM-TRIAD-048","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Measurement Support and Scale Reconciliation Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-SOIL","SRC-ATM","SRC-HYD"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should bind every environmental value to a MeasurementSupport that preserves parameter, unit, instrument or model character, vertical support, temporal aggregation, spatial footprint, CRS, resolution, uncertainty, quality, and no-data semantics.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0143","triad_id":"KFM-TRIAD-048","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Measurement Support and Scale Reconciliation Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-SOIL","SRC-ATM","SRC-HYD"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show measured versus modeled versus derived character, unit and conversion, depth or level, averaging window, footprint and resolution, co-location gap, resampling method, uncertainty, and whether a comparison is valid, qualified, or unsupported.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0144","triad_id":"KFM-TRIAD-048","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Measurement Support and Scale Reconciliation Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-SOIL","SRC-ATM","SRC-HYD"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define MeasurementSupport, UnitTransformReceipt, ScaleReconciliationReport, and ComparisonFitnessDecision objects with pinned conversion and resampling profiles plus fixtures for unit, depth, time-window, footprint, resolution, and observation-versus-model mismatches.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0145","triad_id":"KFM-TRIAD-049","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Product Cadence, Delivery Latency, and Availability Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-TEMPORAL","SRC-ATM"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model observation cadence, product cadence, expected delivery window, observed availability, source revision, retrieval time, freshness window, stale threshold, and outage exception separately and version them with the source descriptor.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0146","triad_id":"KFM-TRIAD-049","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Product Cadence, Delivery Latency, and Availability Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-TEMPORAL","SRC-ATM"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show observed, generated, expected-available, actually available, retrieved, validated, and released times plus finite states such as on-time, expected-lag, late, stale, missing, superseded, and source-outage.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0147","triad_id":"KFM-TRIAD-049","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Product Cadence, Delivery Latency, and Availability Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-TEMPORAL","SRC-ATM"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define DeliveryExpectation, AvailabilityObservation, and FreshnessDecision contracts with tolerance profiles, calendar exceptions, learned observations that require review before changing policy, and synthetic fixtures distinguishing expected latency from true staleness.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0148","triad_id":"KFM-TRIAD-050","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Asynchronous Transfer and Partial-State Provenance Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should distinguish provider request identity, normalized query identity, remote job state, transfer state, local partial bytes, final artifact identity, archive expiry, retry lineage, and ingest identity for asynchronous or resumable sources.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0149","triad_id":"KFM-TRIAD-050","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Asynchronous Transfer and Partial-State Provenance Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect request parameters, provider job identifier, polling history, retry and backoff decisions, partial byte ranges, resume basis, expected and actual size, final digest, archive expiry, and whether downstream processing ever saw incomplete bytes.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0150","triad_id":"KFM-TRIAD-050","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Asynchronous Transfer and Partial-State Provenance Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define AsyncFetchRun, TransferCheckpoint, and DownloadReceipt objects with finite requested, queued, running, succeeded, failed, cancelled, expired, partial, and quarantined states plus idempotence, checksum, resume, and no-double-ingest tests.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0151","triad_id":"KFM-TRIAD-051","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Offline Release Capsule and Trust Freshness Pattern","category":"REL - Catalog Closure, Publication, Release, Rollback, Recompile","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-MAP","SRC-MAPMASTER","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat an offline map as a release capsule containing exact spatial artifacts, style, glyph and sprite manifests, evidence and citation summaries, policy and release refs, verification material, expiry, correction, and withdrawal behavior.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0152","triad_id":"KFM-TRIAD-051","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Offline Release Capsule and Trust Freshness Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-MAP","SRC-MAPMASTER","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show offline release identity, installed and last-verified times, coverage and limitations, expiry, stale or withdrawn state, pending update size, correction availability, evidence depth, and what functions are blocked when trust freshness cannot be renewed.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0153","triad_id":"KFM-TRIAD-051","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Offline Release Capsule and Trust Freshness Implementation Surface","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-MAP","SRC-MAPMASTER","SRC-GREEN"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define OfflineReleaseCapsule, CacheInventory, OfflineVerificationReceipt, and correction or withdrawal delta handoffs with atomic install, interrupted update, expired trust, rollback, cache purge, and reconnect synchronization fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0154","triad_id":"KFM-TRIAD-052","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Verified Rendering Resource Envelope Pattern","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-MAP","SRC-MAPMASTER","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should verify released map bytes, proof structure, expected signer or trust profile, and release binding before decode or render while enforcing declared network, CPU, memory, concurrency, and interaction budgets.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0155","triad_id":"KFM-TRIAD-052","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Verified Rendering Resource Envelope Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-MAP","SRC-MAPMASTER","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should expose loading, verifying, verified, degraded, stale, blocked, and failed states without flashing unverified content and should provide accessible retry, offline, lower-detail, abstention, and evidence-summary paths.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0156","triad_id":"KFM-TRIAD-052","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Verified Rendering Resource Envelope Implementation Surface","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-MAP","SRC-MAPMASTER","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define VerifiedRenderingEnvelope and governed worker messages with chunked hashing, proof and signer checks, queue and concurrency limits, fetch, decode, hash, and heap budgets, cancellation, and fixtures for corruption, truncation, replay, timeout, resource exhaustion, and worker failure.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0157","triad_id":"KFM-TRIAD-053","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Confounder Exclusion and Observation Fitness Pattern","category":"ANA - Analysis, Indicators, Statistics, Machine Learning, Model Interpretation","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-ATM","SRC-AIREF","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should evaluate observation fitness for a declared use through versioned quality, mask, confounder, persistence, source-role, freshness, and support profiles while retaining excluded evidence and reasons for correction or reinterpretation.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0158","triad_id":"KFM-TRIAD-053","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Confounder Exclusion and Observation Fitness Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-ATM","SRC-AIREF","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show the declared use, fitness state, excluded observations, quality masks, confounders, persistence support, alternative explanations, method version, affected area or interval, and whether a conclusion was narrowed, delayed, quarantined, corrected, or withdrawn.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0159","triad_id":"KFM-TRIAD-053","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Confounder Exclusion and Observation Fitness Implementation Surface","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW430","SRC-ATM","SRC-AIREF","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define ObservationFitnessDecision, ContextSnapshot, and ExclusionReceipt objects with deterministic source-specific profiles and fixtures for cloud, smoke, shadow, snow, missing QA, single-observation, contradictory-context, stale-mask, and corrected-mask cases.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0160","triad_id":"KFM-TRIAD-054","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Cross-Boundary Evidence Custody and Reconciliation Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-PIPE","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat every transfer across lifecycle, environment, organization, or responsibility boundaries as a custody handoff that preserves the exact offered artifact, receiving decision, accepted subset, rejected subset, duplicates, and unresolved balance.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0161","triad_id":"KFM-TRIAD-054","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Cross-Boundary Evidence Custody and Reconciliation Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-PIPE","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers compare sender and receiver receipts, inspect item and byte accounting, follow retries and replacements, and distinguish complete, partially accepted, quarantined, disputed, and unreconciled handoffs.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0162","triad_id":"KFM-TRIAD-054","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Cross-Boundary Evidence Custody and Reconciliation Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-PIPE","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define CustodyHandoff, AcceptanceRecord, and ReconciliationReport objects with digest and count conservation, idempotent retry, duplicate detection, reject reasons, timeout, correction, and closure fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0163","triad_id":"KFM-TRIAD-055","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Composed Claim Dependency Closure Pattern","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-ENCYC","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model composed claims as dependency graphs whose required, optional, one-of, excluded, contradictory, and context-only evidence roles determine whether the whole claim is supported, qualified, abstained, denied, or erroneous.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0164","triad_id":"KFM-TRIAD-055","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Composed Claim Dependency Closure Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-ENCYC","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show which claim components closed, which dependencies are missing or withheld, why the conclusion was narrowed, and whether an alternative evidence path satisfied the declared claim profile.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0165","triad_id":"KFM-TRIAD-055","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Composed Claim Dependency Closure Implementation Surface","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-ENCYC","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define ComposedClaimProfile, ClaimDependency, and ClaimClosureReport contracts with cycle detection, role cardinality, freshness, policy outcome, contradiction, alternative-path, and fail-closed fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0166","triad_id":"KFM-TRIAD-056","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Trust-Root Lifecycle and Historical Signature Verification Pattern","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-GREEN","SRC-MAPMASTER","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should version trust roots, signer roles, activation, expiry, revocation, compromise, supersession, and verification policy so current trust and historical validity are evaluated without rewriting prior evidence.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0167","triad_id":"KFM-TRIAD-056","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Trust-Root Lifecycle and Historical Signature Verification Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-GREEN","SRC-MAPMASTER","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect signer identity, trust-profile version, signing and verification times, key status then and now, revocation or compromise reason, offline-verification posture, and any required re-sign, correction, withdrawal, or abstention.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0168","triad_id":"KFM-TRIAD-056","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Trust-Root Lifecycle and Historical Signature Verification Implementation Surface","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-GREEN","SRC-MAPMASTER","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define TrustRootRecord, SignerAuthorization, KeyStatusEvent, and HistoricalVerificationReceipt with synthetic active, rotated, expired, revoked, compromised, unknown, offline, and policy-version mismatch fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0169","triad_id":"KFM-TRIAD-057","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Replay-Safe Event Identity and Side-Effect Ledger Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-PIPE","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should separate deterministic event identity, delivery attempt, processing result, side-effect intent, effect reservation, effect completion, and replay outcome so duplicate delivery cannot silently repeat a consequential action.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0170","triad_id":"KFM-TRIAD-057","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Replay-Safe Event Identity and Side-Effect Ledger Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-PIPE","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let operators trace an event through deliveries, retries, locks or reservations, completed effects, stale attempts, poison handling, compensations, and final finite state without interpreting retry count as work completed.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0171","triad_id":"KFM-TRIAD-057","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Replay-Safe Event Identity and Side-Effect Ledger Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-PIPE","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define GovernedEventEnvelope, DeliveryAttempt, SideEffectIntent, and EffectLedgerEntry contracts with deterministic identity, compare-and-set reservation, idempotency scope, ordering, replay, crash recovery, compensation, and duplicate-delivery fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0172","triad_id":"KFM-TRIAD-058","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Conditional Decision Obligations and Closure Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-GREEN","SRC-ENCYC","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should treat conditional approval as a set of versioned obligations whose application, evidence, satisfaction, waiver, expiry, violation, reopening, supersession, and correction remain explicit and fail closed for consequential transitions.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0173","triad_id":"KFM-TRIAD-058","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Conditional Decision Obligations and Closure Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-GREEN","SRC-ENCYC","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show every active obligation, responsible steward, due or expiry condition, satisfaction evidence, waiver authority, affected artifacts and releases, unmet consequences, and downstream reopening or withdrawal state.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0174","triad_id":"KFM-TRIAD-058","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Conditional Decision Obligations and Closure Implementation Surface","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW423","SRC-GREEN","SRC-ENCYC","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define ConditionalDecision, ObligationRecord, and ObligationClosureDecision contracts with applicability, dependency, satisfaction evidence, waiver, expiry, re-evaluation, correction, and release-blocking negative fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0175","triad_id":"KFM-TRIAD-059","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Reversible Entity Reconciliation and Conflict-Preserving Dedupe Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-FAUNA","SRC-FLORA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should preserve source-native entity assertions and treat match, non-match, merge, split, cluster, and unresolved conflict as reversible decisions supported by versioned evidence rather than destructive normalization.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0176","triad_id":"KFM-TRIAD-059","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Reversible Entity Reconciliation and Conflict-Preserving Dedupe Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-FAUNA","SRC-FLORA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let stewards compare candidate entities, inspect contributing and conflicting attributes, approve or reject matches, split prior clusters, restore source views, and see every downstream artifact affected by reconciliation changes.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0177","triad_id":"KFM-TRIAD-059","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Reversible Entity Reconciliation and Conflict-Preserving Dedupe Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-FAUNA","SRC-FLORA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define MatchProposal, ReconciliationDecision, EntityCluster, and SplitDecision objects with blocking keys, feature evidence, confidence limits, authority roles, transitivity guards, reversal, correction, and false-merge fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0178","triad_id":"KFM-TRIAD-060","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Taxonomic Concept and Name-Usage Lineage Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-FLORA","SRC-FAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should separate source-native NameUsage from TaxonConcept and preserve authorship, rank, treatment, valid time, concept relation, source role, and unresolved disagreement instead of treating an accepted-name string as timeless identity.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0179","triad_id":"KFM-TRIAD-060","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Taxonomic Concept and Name-Usage Lineage Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-FLORA","SRC-FAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show accepted-for-use context, synonyms, homonyms, misapplied names, split and lump history, source treatments, unresolved mappings, affected occurrence or distribution claims, and the version used for a query or release.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0180","triad_id":"KFM-TRIAD-060","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Taxonomic Concept and Name-Usage Lineage Implementation Surface","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-FLORA","SRC-FAUNA","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define NameUsage, TaxonConcept, ConceptRelation, and TaxonomyReconciliationDecision contracts with source-native identifiers and synthetic synonym, homonym, split, lump, misapplication, unresolved, supersession, and reversal fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0181","triad_id":"KFM-TRIAD-061","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Place-Name Authority and Temporal Alias Graph Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-SETTLE","SRC-ROADS","SRC-TEMPORAL"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should model place names as time-bounded, source-role-bound assertions linked to but distinct from feature identity, geometry, jurisdiction, legal status, and ownership.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0182","triad_id":"KFM-TRIAD-061","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Place-Name Authority and Temporal Alias Graph Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-SETTLE","SRC-ROADS","SRC-TEMPORAL"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should support search across official, variant, historical, translated, superseded, and disputed names while disclosing source, valid time, language or community context, feature binding, ambiguity, and withheld-sensitive-name posture.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0183","triad_id":"KFM-TRIAD-061","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Place-Name Authority and Temporal Alias Graph Implementation Surface","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-SETTLE","SRC-ROADS","SRC-TEMPORAL"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define PlaceNameAssertion, TemporalAliasEdge, FeatureNameBinding, and NameAuthorityDecision contracts with collision, homonym, rename, translation, dispute, unbound name, feature split or merge, and supersession fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0184","triad_id":"KFM-TRIAD-062","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Survey-Control and Boundary Derivation Provenance Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-GIS","SRC-TEMPORAL","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should preserve survey observation, monument or control status, survey generation, adjustment, georeference, residual, transformation, derived geometry, valid time, source role, and legal-use limitation as distinct provenance.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0185","triad_id":"KFM-TRIAD-062","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Survey-Control and Boundary Derivation Provenance Capability","category":"MAP - Map Surface, MapLibre, Tiles, Styling","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-GIS","SRC-TEMPORAL","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show whether geometry is source-recorded, reconstructed, adjusted, georeferenced, interpolated, generalized, conflicting, or unresolved together with residuals, control status, source vintage, derivation lineage, and non-survey or non-legal-use warnings.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0186","triad_id":"KFM-TRIAD-062","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Survey-Control and Boundary Derivation Provenance Implementation Surface","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-GIS","SRC-TEMPORAL","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define SurveyObservation, ControlStatusEvent, GeoreferenceReport, BoundaryDerivation, and SurveyFitnessDecision objects with conflicting-control, lost-monument, adjustment, high-residual, datum, temporal, incomplete-record, and legal-authority abstention fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0187","triad_id":"KFM-TRIAD-063","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Adversarial Validator Assurance and Mutation Adequacy Pattern","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-GREEN","SRC-PIPE","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should assess release-critical validators and policies with adversarial semantic mutations, property checks, negative fixtures, and gap-class coverage rather than treating execution or line coverage as sufficient assurance.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0188","triad_id":"KFM-TRIAD-063","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Adversarial Validator Assurance and Mutation Adequacy Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-GREEN","SRC-PIPE","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect tested invariants, mutant classes, killed and surviving mutants, equivalent or waived rationale, untested finite outcomes, dependency and network posture, and the consequence of each assurance gap.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0189","triad_id":"KFM-TRIAD-063","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Adversarial Validator Assurance and Mutation Adequacy Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW425","SRC-GREEN","SRC-PIPE","SRC-GAI"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define ValidatorAssurancePlan and MutationAssessmentReport with deterministic no-network mutants for removed required fields, inverted allow or deny, bypassed abstention, stale profile, altered authority, skipped signature check, truncated evidence, and swallowed failure.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0190","triad_id":"KFM-TRIAD-064","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Bitemporal Verification-State Replay Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-TEMPORAL","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should represent every verification-state change with subject identity, state, reason, effective time, recorded time, predecessor, authority, evidence, policy profile, and trust profile so current and as_of answers remain reproducible without rewriting prior history.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0191","triad_id":"KFM-TRIAD-064","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Bitemporal Verification-State Replay Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-TEMPORAL","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers replay verification state at a declared time, distinguish late-recorded from backdated-effective events, inspect active evidence and release context, and follow supersession, correction, rollback, and revocation edges.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0192","triad_id":"KFM-TRIAD-064","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Bitemporal Verification-State Replay Implementation Surface","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-TEMPORAL","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define VerificationStateEvent, VerificationStateGraph, AsOfVerificationQuery, and VerificationReplayReport contracts with synthetic active, late-recorded, corrected, superseded, revoked, missing-predecessor, cyclic, ambiguous, and unknown-history fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0193","triad_id":"KFM-TRIAD-065","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Source-Conflict Topology and Influence Accounting Pattern","category":"EVD - Evidence, EvidenceBundle, EvidenceRef, Cite-or-Abstain","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-GAI","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should assess jointly used sources under a versioned comparison profile that preserves source roles and classifies their relationship as consistent, divergent, conflicting, insufficient, inapplicable, or containing revoked evidence before producing a finite result.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0194","triad_id":"KFM-TRIAD-065","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Source-Conflict Topology and Influence Accounting Capability","category":"UIX - UI / UX, Viewer Affordances, Focus Mode, EvidenceDrawer","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-GAI","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show compared inputs, eligibility and exclusions, comparison axes, tolerance-profile identity, conflict class, uncertainty, and which sources were dominant, contributing, context-only, excluded, or non-influential in the result.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0195","triad_id":"KFM-TRIAD-065","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Source-Conflict Topology and Influence Accounting Implementation Surface","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-GAI","SRC-GREEN","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define SourceConflictProfile, SourceComparison, InfluenceLedger, and FederationDecision contracts with unit, scale, time, precision, support, source-role, missingness, revocation, threshold-boundary, order-invariance, and irreconcilable-conflict fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0196","triad_id":"KFM-TRIAD-066","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Cross-Layer Outcome Projection and Parity Pattern","category":"POL - Policy, OPA, Conftest, Decisions  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should preserve finite-outcome meaning and reason lineage across policy, release, runtime, API, UI, export, and cache projections through a versioned matrix of allowed transformations, permitted degradations, and prohibited upgrades.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0197","triad_id":"KFM-TRIAD-066","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Cross-Layer Outcome Projection and Parity Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect each projection step, input and output outcome, reason-code mapping, omitted fields, authorized degradation, policy/profile identity, and any parity failure before a consequential surface is trusted.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0198","triad_id":"KFM-TRIAD-066","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Cross-Layer Outcome Projection and Parity Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-GAI","SRC-MAP"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define OutcomeProjectionProfile, OutcomeProjectionStep, and OutcomeParityReport contracts with synthetic ANSWER, ABSTAIN, DENY, ERROR, redacted, stale, unavailable, reason-loss, empty-success, cache, and unauthorized-upgrade fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0199","triad_id":"KFM-TRIAD-067","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Verifier Profile and Capability Portability Pattern","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-GREEN","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should interpret verification only relative to an explicit verifier profile that binds supported algorithms, canonicalization, trust and revocation inputs, dependency versions, network posture, time source, and resource limits; unsupported capability must produce an explicit fail-safe result.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0200","triad_id":"KFM-TRIAD-067","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Verifier Profile and Capability Portability Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-GREEN","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show verifier identity, environment class, profile and dependency versions, available and missing capabilities, trust freshness, network assumptions, resource limits, attempted checks, and whether results are portable, qualified, unsupported, or incomparable.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0201","triad_id":"KFM-TRIAD-067","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Verifier Profile and Capability Portability Implementation Surface","category":"SEC - Security, Signing, Cosign, DSSE, Rekor  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-GREEN","SRC-MAPMASTER"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define VerifierProfile, VerificationCapabilityClaim, VerificationAttempt, and PortabilityAssessment contracts with synthetic CI, browser, offline, unsupported-algorithm, canonicalization-mismatch, stale-trust, missing-revocation, dependency-drift, clock, network, and resource-exhaustion fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0202","triad_id":"KFM-TRIAD-068","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Source-Native Quality Translation and Health Separation Pattern","category":"MOD - Data Modeling, Domain Semantics, Temporal Structure, SQL","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW415","SRC-SOIL","SRC-ATM","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should preserve source-native quality vocabulary and code, vocabulary version, mapping rule and version, normalized interpretation, semantic loss, unmapped state, station or sensor health, observation validity, analytic fitness, and decision reason as separate lineage.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0203","triad_id":"KFM-TRIAD-068","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Source-Native Quality Translation and Health Separation Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW415","SRC-SOIL","SRC-ATM","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers compare native and normalized quality, inspect mapping evidence and loss, distinguish offline or maintenance state from invalid reading and missing support, and see which declared uses admit, exclude, quarantine, deny, or abstain from the observation.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0204","triad_id":"KFM-TRIAD-068","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Source-Native Quality Translation and Health Separation Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW415","SRC-SOIL","SRC-ATM","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define NativeQualityAssertion, QualityMappingDecision, SourceHealthEvent, ObservationValidityDecision, and ObservationFitnessDecision contracts with known, unknown, contradictory, deprecated, lossy, offline, maintenance, calibration, invalid-value, stale, missing-depth, missing-support, and valid fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0205","triad_id":"KFM-TRIAD-069","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Generated Runtime-Proof Artifact Lifecycle Pattern","category":"DAT - Data Lifecycle, Provenance, Receipts","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW415","SRC-GREEN","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should govern generated runtime-proof artifacts through explicit ephemeral, retained-for-review, promoted-golden, stale, invalidated, corrected, and deleted states while preserving runner, contract, fixture, configuration, dependency, environment, and digest identity.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0206","triad_id":"KFM-TRIAD-069","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Generated Runtime-Proof Artifact Lifecycle Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW415","SRC-GREEN","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should let reviewers inspect actual-versus-expected differences, generation provenance, determinism and redaction posture, retention and expiry, review decision, golden-promotion rationale, affected tests, and later invalidation or correction.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0207","triad_id":"KFM-TRIAD-069","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Generated Runtime-Proof Artifact Lifecycle Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW415","SRC-GREEN","SRC-PIPE","SRC-ENCYC"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define RuntimeProofArtifactRecord, GoldenPromotionDecision, and ProofArtifactInvalidationNotice contracts with synthetic ephemeral, retained, promoted, rejected, nondeterministic, sensitive, stale-contract, dependency-drift, expired, invalidated, corrected, and deleted fixtures.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0208","triad_id":"KFM-TRIAD-070","stable_id_template":"KFM-P{PASS}-IDEA-{NNNN}","pass":"{PASS}","class":"idea","title":"Observed Interface Evolution and Compatibility Window Pattern","category":"SRC - Source Registry, Connectors, Ingestion  (PROPOSED extension)","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-PIPE","SRC-DIR"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should preserve declared interface identity separately from observed behavior and govern discovery, compatibility, deprecation, dual-read, migration, rollback, consumer debt, retirement, and correction without treating URL, ETag, timestamp, redirect, or one sample as canonical identity.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0209","triad_id":"KFM-TRIAD-070","stable_id_template":"KFM-P{PASS}-FEAT-{NNNN}","pass":"{PASS}","class":"feature","title":"Observed Interface Evolution and Compatibility Window Capability","category":"DOC - Documentation, Doctrine, Reader Surfaces","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-PIPE","SRC-DIR"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should show declared and observed contract/profile versions, observation evidence, changed capabilities, compatibility class, affected consumers, dual-read comparison, deprecation and sunset signals, migration decision, rollback readiness, and retirement blockers.","implementation_status":"NEEDS_VERIFICATION"}
{"candidate_key":"KFM-CAND-0210","triad_id":"KFM-TRIAD-070","stable_id_template":"KFM-P{PASS}-PROG-{NNNN}","pass":"{PASS}","class":"programming","title":"Observed Interface Evolution and Compatibility Window Implementation Surface","category":"PIP - Pipelines, Pipeline Specs, Validators","status":"active","carry_forward_state":"NEW_GAP_FILL","source_ids":["SRC-NEW414","SRC-NEW415","SRC-PIPE","SRC-DIR"],"spec_hash":"PROPOSED","normalized_statement":"PROPOSED: KFM should define InterfaceObservation, CompatibilityAssessment, InterfaceMigrationDecision, and InterfaceRetirementRecord contracts with synthetic unchanged, additive, breaking, redirect, undocumented, partial-sample, dual-read mismatch, rollback, consumer-blocked, retired, and reactivated fixtures.","implementation_status":"NEEDS_VERIFICATION"}
```

---

## 17. Changelog

| Version | Date | Change |
|---|---:|---|
| v0.6 | 2026-07-29 | Reconciled the prior Pass 23 sources `New Ideas 4-14-26` and `New Ideas 4-15-26` against the pinned remote-main snapshot and added 21 gap-fill cards in 7 triads covering bitemporal verification replay, source-conflict influence, cross-layer outcome parity, verifier portability, source-native quality translation and health separation, generated runtime-proof artifact lifecycle, and observed interface evolution. |
| v0.5 | 2026-07-29 | Reconciled `New Ideas 4-23-26` and `New Ideas 4-25-26` against the pinned remote-main snapshot and added 30 gap-fill cards in 10 triads covering cross-boundary custody, composed-claim closure, trust-root history, replay-safe effects, conditional obligations, reversible reconciliation, taxonomic concepts, temporal place-name authority, survey-control provenance, and adversarial validator assurance. |
| v0.4 | 2026-07-29 | Reconciled `New Ideas 4-30-26` against the pinned remote-main snapshot and added 33 gap-fill cards in 11 triads covering retrieval intent, source terms drift, sampling support, distribution meaning, coverage bias, measurement reconciliation, delivery latency, asynchronous transfer state, offline trust, verified rendering, and confounder-aware observation fitness. |
| v0.3 | 2026-07-29 | Reconciled `New Ideas 4-16-26` against the pinned remote-main snapshot and added 30 gap-fill cards in 10 triads covering materiality, precision lineage, correctable environmental events, baseline governance, corroboration roles, purpose-bound consent, governed playback, STAC conformance, historical uncertainty, and hash profiles. |
| v0.2 | 2026-06-12 | Optimized pasted seed-card draft into deduplicated triad register with source ledger, shared controls, category/source distributions, candidate keys, implementation slices, and JSONL manifest. |
| v0.1 | unknown | Original pasted seed-card draft with 96 repeated card entries and placeholder pass/ordinal IDs. |

---

## 18. Footer

```yaml
kfm_footer:
  document: "KFM Atlas Seed Cards — Optimized Carry-Forward Register"
  version: "v0.6"
  status: "draft"
  authority_class: "candidate-card register / synthesis; not canonical doctrine"
  requested_path: "docs/kfm_full_atlas_seed_cards.md"
  current_repository_home: "docs/kfm_full_atlas_seed_cards.md"
  current_repository_home_status: "CONFIRMED at main 5266ba5f2d8f39cad2d54b066d514be8ca8eb3b7; retained in place"
  card_count: 210
  triad_count: 70
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
