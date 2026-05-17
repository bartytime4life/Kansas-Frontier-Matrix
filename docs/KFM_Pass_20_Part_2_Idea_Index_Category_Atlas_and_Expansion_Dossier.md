# KFM Components Pass 20 — Unified Idea Index, Category Atlas, and Expansion Dossier

*A combined edition of two KFM Pass 20 syntheses, presented as Part I and Part II.*

---

## Reader's Note: This Is a Combined Edition

This document is a unified concatenation of two distinct Pass 20 synthesis runs. It is **not** a fresh synthesis pass that flattens them into a single category system. Each run was bounded to a different source corpus and reached a different normalization; preserving that distinction is a deliberate KFM truth-posture decision (cite-or-abstain, no silent merging of distinct evidence bases).

**Status of this wrapper:** **PROPOSED** (combined-edition structure only). The two parts carry their own internal truth labels per KFM convention; this wrapper does not retroactively change them.

### Source provenance of the two parts

| Part | Original document title | Source corpus boundary | Category system | Idea ID scheme |
|---|---|---|---|---|
| **Part I** | *KFM Components Pass 20 — Idea Index, Category Atlas, and Expansion Dossier* | 39 readable PDFs in `/mnt/data` (Phase 1 corpus) | **9** dependency-ordered categories — `GOV` · `SRC` · `EVD` · `MOD` · `POL` · `VAL` · `MAP` · `INT` · `APP` — a compression of Pass 18's 14-category surface | `KFM-IDX-<CAT>-NNN`, 72 seeded IDs (8 per category) |
| **Part II** | *KFM Components Pass 20 Part 2 — Idea Index, Category Atlas, and Expansion Dossier* | Pass 18 PDF + Pass 19 PDF (bounded two-source corpus) | **14** dependency-ordered categories — `DOC` · `REP` · `SRC` · `MOD` · `EVD` · `POL` · `VAL` · `ANA` · `FIE` · `REL` · `API` · `MAP` · `UIX` · `PLN` — retained intact from Pass 18 / Pass 19 lineage | `KFM-IDX-<CAT>-NNN` with `P19-XXX-NNN` lineage, 64+ ideas plus indexed appendix |

Both parts were prepared **2026-05-16** and both record the same operating posture: **evidence-first · map-first · time-aware · cite-or-abstain · fail-closed · policy-aware · auditable · reversible**. Both record the same current-session evidence boundary: no mounted live KFM repository, runtime, CI, dashboard, branch state, package version, or external source-currentness check was inspected, so implementation maturity, route names, DTO shapes, deployment claims, and test results remain **UNKNOWN** unless carried as doctrine.

### Why the parts are not merged at the section level

The two passes reached different but internally coherent normalization decisions over different corpora:

- **Part I compresses** Pass 18's 14-category surface into 9 categories for a master-dossier scope cap, treating prior categories as subcategories within the 9-category system.
- **Part II preserves** the 14-category dependency map intact because the bounded Pass 18 + Pass 19 corpus does not justify recompression.

Silently fusing these into a single category vocabulary would itself be a fresh synthesis act — appropriate for a later pass (and probably an ADR-bearing one), not for a "combine" operation. Reconciliation between the 9-category and 14-category views, if pursued, belongs in a future ADR that records the tradeoff explicitly.

### Reading guidance

- For broader corpus coverage with operational expansion proposals (watcher events, PMTiles attestation, sidecars, byte-range proofs, environmental probes) drawn from 39 PDFs, read **Part I**.
- For cumulative Pass 18 → Pass 19 idea normalization with an explicit `EXP-001`…`EXP-015` expansion agenda and Pass 19 → Pass 20 delta accounting, read **Part II**.
- Both parts share the same outer section skeleton: Title Page · Executive Determination · Source Synthesis Report · Structural Rationale · Master Category Map · Detailed Idea Chapters by Category · Cross-Cutting Themes · Overlaps/Contradictions/Gaps · Weakly Supported Material · Expansion Agenda · Open Questions · Appendices A/B/C. Section numbers within each part are preserved as authored.
- Idea IDs use the `KFM-IDX-<CAT>-NNN` pattern in both parts, but the `<CAT>` vocabularies differ. When citing an idea across the combined document, qualify with the part: e.g., *Part I `KFM-IDX-GOV-001`* vs. *Part II `KFM-IDX-DOC-001`*. Within a single part, the original unqualified form is sufficient.

### Shared truth label key

| Label | Meaning |
|---|---|
| **CONFIRMED** | Directly supported in the relevant pass by attached documents, working-file extraction, generated artifacts, or current-session file evidence. |
| **PROPOSED** | A synthesis, organizing interpretation, implementation direction, path, artifact, or future work item consistent with the corpus but not proven as implemented. |
| **NEEDS VERIFICATION** | Checkable before implementation, source activation, publication, or operational use, but not checked strongly enough in the pass that produced the statement. |
| **UNKNOWN** | Not supported strongly enough by the corpus or current-session evidence to be treated as established. |
| **DENY / ABSTAIN / ERROR** | Finite system outcomes or policy/runtime labels used in KFM doctrine; they are not rhetorical emphasis. |

### Open editorial questions (combined edition)

These are wrapper-level open questions, separate from each part's own Open Questions register:

1. **Category reconciliation.** Should a future pass produce a crosswalk table between Part I's 9 categories and Part II's 14 categories, or should the next pass pick one and ADR the choice? **NEEDS VERIFICATION** against current KFM ADRs.
2. **ID-namespace collision policy.** When the combined document is referenced externally, should `KFM-IDX-MOD-001 (Part I)` and `KFM-IDX-MOD-001 (Part II)` be promoted to distinct global IDs, or should one part's IDs be re-namespaced (e.g., `KFM-IDX-P1-MOD-001` / `KFM-IDX-P2-MOD-001`)? **PROPOSED** for ADR.
3. **Canonical write target.** Part I's title page references `/mnt/user-data/outputs/KFM_Pass_15_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` as its canonical Markdown write target (an older pass-name convention). This combined edition's write target should be recorded in the next ADR alongside the part-naming reconciliation. **NEEDS VERIFICATION**.
4. **Source-boundary union vs. intersection.** Part I's 39-PDF corpus is a superset of Part II's 2-PDF corpus (Pass 18 + Pass 19 appear in both). Any future merged synthesis must decide whether to treat shared sources as corroboration or as a single citation; this wrapper makes no such decision.

---


# KFM Components Pass 20 — Idea Index, Category Atlas, and Expansion Dossier

**Subtitle:** A detailed evidence-first synthesis of the attached source corpus.


## 1. Title Page

**Title:** KFM Components Pass 20 — Idea Index, Category Atlas, and Expansion Dossier

**Subtitle:** A detailed evidence-first synthesis of the attached source corpus.

**Document type:** PDF-ready master reference document, idea index, category atlas, and expansion dossier.

**Prepared:** 2026-05-16 UTC.

**Prepared for:** Kansas Frontier Matrix maintainers, source stewards, architecture reviewers, domain-lane leads, implementation planners, research editors, validation reviewers, and evidence-governance reviewers.

**Canonical Markdown write target:** `/mnt/user-data/outputs/KFM_Pass_15_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`. The requested final filename carries an older pass-name convention, but the internal title, source boundary, and working files identify this as **KFM Components Pass 20**.

**Working-state boundary:** Notes, category decisions, ID registry, and progress markers are persisted under `/mnt/user-data/outputs/_kfm_work/`. This master document is written incrementally from those working files rather than regenerated from the raw PDFs in a single pass.

**Source boundary statement:** This pass is bounded to the 39 readable PDF attachments visible in `/mnt/data` during Phase 1. The requested `/mnt/user-data/uploads` location was absent or empty in this environment, so the current-session attachments under `/mnt/data` became the Phase 1 corpus. Phase 1 found 39 PDFs, all readable, and no unreadable or quarantined PDF sources. Phase 2 compacted those sources into `_notes.md`; Phase 3 derived the category tree and seeded `_ids.tsv`; Phase 4 created this scaffold.

**Purpose statement:** This document extracts, normalizes, and develops the major ideas in the attached corpus so later KFM work can proceed from a durable idea index rather than from scattered doctrine, domain plans, pass lineage, and operational packets. It is a synthesis and expansion dossier, not a claim of current repository implementation, public release, or source activation.

**Truth posture key:**

| Label | Meaning in this document |
|---|---|
| **CONFIRMED** | Directly supported in this pass by attached documents, working-file extraction, generated artifacts, or current-session file evidence. |
| **PROPOSED** | A synthesis, organizing interpretation, implementation direction, path, artifact, or future work item consistent with the corpus but not proven as implemented. |
| **NEEDS VERIFICATION** | Checkable before implementation, source activation, publication, or operational use, but not checked strongly enough in this pass. |
| **UNKNOWN** | Not supported strongly enough by the corpus or current-session evidence, usually because no live repo, tests, runtime, logs, dashboards, branch state, source terms, or external currentness check was performed. |
| **DENY / ABSTAIN / ERROR** | Finite system outcomes or policy/runtime labels used in KFM doctrine; they are not rhetorical emphasis. |

**Citation convention:** Source support is shown through Phase 1 short tags in square brackets, for example `[Directory Rules]`, `[Greenfield Building Plan]`, and `[Pass 19]`. Working-file evidence is referenced as Phase 1, Phase 2, Phase 3, or Phase 4 state when the claim concerns this run rather than a corpus source.

**Core operating posture:** Evidence first; map first; time aware; cite or abstain; fail closed where risk matters; policy aware; auditable; reversible. Maps, tiles, graphs, AI answers, summaries, scenes, dashboards, indexes, and planning views are downstream carriers of evidence, not sovereign truth [Greenfield Building Plan] [MapLibre Operating Manual] [Pass 19].

**Current-session limitation:** No mounted live KFM repository, current CI workflow, runtime log, deployment setting, dashboard, branch protection, current external-source status, package-version check, or source-rights review was inspected during this pass. Current implementation maturity therefore remains **UNKNOWN** unless a source is clearly being used only as doctrine, lineage, or proposal.

## 2. Executive Determination

**CONFIRMED:** The corpus is about Kansas Frontier Matrix as a governed spatial evidence and publication system. Its center of gravity is not a map alone, not an AI assistant alone, not a domain-data warehouse, and not a set of disconnected implementation plans. Across the doctrine, domain blueprints, technical references, cumulative passes, and operational packets, the repeated pattern is a trust membrane: source admission, evidence resolution, policy and sensitivity review, validation, catalog/proof/receipt closure, governed release, API and map delivery, Evidence Drawer explanation, Focus Mode interpretation, correction, and rollback [Directory Rules] [Greenfield Building Plan] [Pipeline Manual] [MapLibre Operating Manual] [Pass 19].

**CONFIRMED:** The immediate lineage is cumulative. Pass 18 records a large prior idea-card synthesis and a 14-category expansion surface; Pass 19 keeps that structure while emphasizing source drift detection, environmental probes, material-change watchers, PMTiles attestation, byte-range proofs, and fail-closed publication gates [Pass 18] [Pass 19]. Pass 20 therefore does not restart the atlas from zero. It normalizes the corpus into a smaller dependency-ordered category system and develops the strongest corpus-derived ideas in prose.

**PROPOSED:** The strongest Pass 20 synthesis is that KFM's architecture should be understood as a sequence of governed transformations rather than as a set of products. Sources are admitted or refused; evidence is bundled and cited; policy allows, denies, redacts, delays, or stages exposure; validators fail closed; release manifests and proof objects make publication reversible; APIs and maps carry released truth; AI and planning support interpret rather than authorize. This is the only reading that reconciles the Directory Rules, greenfield build doctrine, pipeline loop, MapLibre operating manual, governed-AI reports, domain-lane blueprints, and operational New Ideas packets [Directory Rules] [Greenfield Building Plan] [Pipeline Manual] [Governed AI Ledger] [Master MapLibre Atlas].

**CONFIRMED / PROPOSED:** Phase 3 derived 9 top-level categories from `_notes.md`: GOV, SRC, EVD, MOD, POL, VAL, MAP, INT, and APP. This is a deliberate normalization of the broader Pass 18/Pass 19 category vocabulary, not a rejection of it. Pass 18's more granular representation, API, analysis, field, release, map, UI, and planning categories remain present inside the 9-category system as subcategories and idea entries [Pass 18] [Pass 19].

**CONFIRMED:** The corpus repeatedly warns against overclaiming implementation. Many domain-lane PDFs report no mounted repository in their own run contexts and frame their outputs as PDF-only plans, blueprints, lineage, or PR-ready proposals rather than executed patches [Hydrology] [Fauna] [Flora] [Hazards] [Archaeology Plan] [Settlements Infrastructure]. One implementation reference reports earlier connector-observed public-repo surfaces, while the Greenfield Building Plan assumes an empty start [Implementation Reference] [Greenfield Building Plan]. Pass 20 preserves that tension rather than flattening it. Current repository reality is **UNKNOWN** in this pass.

**PROPOSED:** The main actionable expansion pressure comes from three places. First, operational watchers and material-change sidecars make source change and source health testable [New Ideas 5-8] [New Ideas 5-15]. Second, PMTiles sidecars, root hashes, byte-range manifests, Bao-style proofs, and signed attestations make map artifacts more inspectable and rollback-ready [New Ideas 5-10] [Master MapLibre Atlas]. Third, repeated domain-lane reports show that hydrology, habitat/fauna, soil/agriculture/landcover, atmosphere/hazards, roads/settlements/infrastructure, archaeology, people/DNA/land, and geology can share one governed domain-lane packet while preserving domain-specific policy controls [Hydrology] [Habitat Fauna Thin Slice] [Soil] [Agriculture] [People DNA Land].

**UNKNOWN:** This pass does not know whether proposed schemas, policies, routes, layer manifests, source descriptors, validators, PMTiles attestations, CI jobs, Evidence Drawer payloads, Focus Mode envelopes, or domain-lane fixtures currently exist in the live KFM repository. Any future claim that a given path or feature is implemented must be verified against mounted repo evidence, current tests, generated receipts, release manifests, logs, dashboards, or reviewed artifacts.

**Standing assumptions for this master document:**

1. The Phase 2 notes are the compact working memory for the writing phase; the raw PDFs remain the source boundary, but the writing phase reads from `_notes.md`, `_categories.md`, and `_ids.tsv` to avoid context pressure and accidental regeneration.
2. Duplicate and near-duplicate source patterns are treated as corroboration, not as independent implementation proof.
3. Current external facts embedded in PDFs, especially source status, package versions, endpoint behavior, data cadence, and license posture, remain **NEEDS VERIFICATION** unless this pass explicitly checked them, which it did not.
4. Directory and file-path proposals remain **PROPOSED** until checked against Directory Rules, accepted ADRs, and current mounted-repo evidence [Directory Rules].
5. The document may recommend expansion paths, but public or semi-public release remains outside this writing pass and requires rights, sensitivity, validation, provenance, review, release, correction, and rollback support.

### 2.1 Executive determination table

| Determination area | Status | Result |
|---|---|---|
| Corpus center of gravity | CONFIRMED | Governed, evidence-first, map-first, time-aware spatial evidence and publication architecture. |
| Public unit of value | CONFIRMED | The inspectable claim, not a tile, graph edge, AI response, dashboard, or map layer [Greenfield Building Plan] [KFM Encyclopedia]. |
| Category system | CONFIRMED / PROPOSED | 9 dependency-ordered categories derived from Phase 2 notes and Phase 3 normalization. |
| Implementation maturity | UNKNOWN | No live repo/runtime/CI inspection in this pass. Prior repo summaries remain lineage and verification prompts. |
| Strongest near-term expansion | PROPOSED | Source watchers, PMTiles attestation, proof-bearing domain thin slices, and trust-visible API/map/UI envelopes. |
| Strongest caution | CONFIRMED | Do not treat fluent summaries, maps, raw model output, source packets, or PDF-only path plans as implementation proof. |

## 3. Source Synthesis Report

The corpus contains five major source families. The first family is the KFM doctrine and control-plane family: Directory Rules, the Greenfield Building Plan, the Pipeline Manual, the KFM Encyclopedia, the Implementation Reference, the MapLibre Operating Manual, the Whole-UI/Governed-AI report, the Governed AI Ledger, and the Ollama/Ubuntu guide. These sources govern the synthesis because they define truth posture, lifecycle law, directory placement, AI boundaries, UI trust surfaces, and publication discipline [Directory Rules] [Greenfield Building Plan] [Pipeline Manual] [KFM Encyclopedia] [MapLibre Operating Manual] [Ollama Ubuntu].

The second family is the cumulative synthesis and atlas family: Pass 18, Pass 19, and the Master MapLibre Atlas. These are not ordinary topical sources. They are prior indexing systems, baseline syntheses, and specialized idea atlases. They carry continuity, category lineage, prior idea density, and map/tile/UI object-family pressure, but they do not independently prove current implementation [Pass 18] [Pass 19] [Master MapLibre Atlas].

The third family is the domain-lane blueprint family. It covers hydrology, habitat, habitat/fauna, fauna, flora, soil, agriculture, geology/natural resources, atmosphere/air, hazards, roads/rail/trade routes, settlements/infrastructure, archaeology, and people/genealogy/DNA/land ownership. These sources are high-value because they repeat the same governed-lane skeleton while adding domain-specific risks: rare species geoprivacy, exact archaeology-site denial, living-person and DNA restrictions, infrastructure exposure, hazards that must not become emergency alerts, hydrologic source-role distinctions, and land/people assertions that must not become unsupported map labels [Hydrology] [Fauna] [Flora] [People DNA Land] [Archaeology Plan] [Hazards].

The fourth family is the technical reference family: GIS/cartography, environmental GIS, urban planning GIS, archaeological 3D GIS, advanced SQL, temporal databases, domain-driven design, Web APIs, AI/Python, and web scraping. These sources supply vocabulary, methods, and caution. Their concepts become KFM ideas only after they are normalized through KFM doctrine. A GIS tutorial, SQL concept, web API pattern, or AI model workflow is therefore not automatically a KFM implementation requirement; it becomes a **PROPOSED** KFM adaptation unless the KFM corpus already incorporates it [GIS Primer] [Temporal SQL] [DDD Reference] [Web APIs] [AI Python].

The fifth family is the Pass 20 delta-packet family: New Ideas 5-8, New Ideas 5-10, and New Ideas 5-15. These packets introduce operationally specific proposals around environmental source-health probes, tile-health thresholds, PMTiles artifact attestation, byte-range verification, and material-change watchers for CDL/PLANTS-like source packages [New Ideas 5-8] [New Ideas 5-10] [New Ideas 5-15]. Their operational specificity is valuable, but current source status, endpoint behavior, package versions, and rights details remain **NEEDS VERIFICATION** before implementation.

The recurrent ideas are consistent across the corpus. Evidence outranks generated language. Public clients use governed interfaces. Source roles matter. Maps are downstream representations. Temporal state must be explicit. Publication is a governed transition, not a file move. Sensitive exact locations fail closed. AI is interpretive, structured, bounded, and citation-validated. Domain lanes should reuse shared governance objects rather than invent parallel schema, policy, source, proof, release, or receipt homes [Directory Rules] [Greenfield Building Plan] [Governed AI Ledger] [MapLibre Operating Manual].

The corpus is strongest where it describes doctrine, responsibility boundaries, source-role separation, evidence and publication object families, map/renderer boundaries, UI trust states, local AI governance, and repeated domain-lane caution. It is thinner where it implies current operational facts: external service currentness, source rights, package versions, CDN behavior, exact public repo maturity, CI enforcement, branch protections, and runtime behavior. Those thin areas are routed to Sections 8 through 11 and to the Expansion Agenda rather than upgraded into confident claims.

Duplicate handling is important. Pass 18, Pass 19, the KFM Encyclopedia, and the Master MapLibre Atlas are cumulative and partially overlapping. Domain reports repeat no-repo caveats, schema-home ambiguity, source-registry patterns, validator-first plans, and public-safe outputs. New Ideas 5-8 and 5-10 overlap around PMTiles, sidecars, receipts, and environmental operations. Pass 20 treats those overlaps as convergence signals. They strengthen the priority of a pattern but do not multiply proof of implementation.

### 3.1 Source Inventory Notes

**CONFIRMED:** Phase 1 found 39 readable PDFs, 0 unreadable PDFs, and 39 successful first-page render checks. The table below records how each source is used in this synthesis. Length signal is page count from Phase 1, not a measure of authority.

| Short tag | Source family | Length signal | Role in Pass 20 synthesis |
|---|---|---:|---|
| [Implementation Reference] | Implementation lineage / repo-summary source | 20 | Public-repo and implementation-surface signal; treated as lineage and verification prompt, not current proof. |
| [GIS Primer] | Technical GIS/cartography reference | 321 | Representation, cartography, scale, CRS, projections, data models, map communication, and GIS analysis vocabulary. |
| [Advanced SQL] | Technical SQL reference | 112 | Analytical SQL, joins, recursive queries, windows, aggregation, and query caution for later data modeling. |
| [AI Python] | Technical AI/ML reference | 435 | AI workflow, data, supervised/unsupervised learning, model limitations, and derivative-output caution. |
| [Archaeological 3D GIS] | Technical 3D/archaeology reference | 177 | 3D GIS, field capture, surface/subsurface analysis, 2.5D versus 3D distinctions, archaeological interpretation caution. |
| [Web APIs] | Technical API reference | 45 | API-as-contract, resource ontology, HTTP lifecycle, design-first API process, and developer-facing interface discipline. |
| [Temporal SQL] | Technical temporal-database reference | 528 | Valid time, transaction time, bitemporal tables, temporal design, and time-oriented state modeling. |
| [Directory Rules] | Governing doctrine | 22 | Canonical placement rules, responsibility roots, lifecycle law, schema-home default, ADR and drift discipline. |
| [DDD Reference] | Technical domain-modeling reference | 59 | Bounded context, ubiquitous language, aggregates, repositories, domain events, context mapping, published language. |
| [ArcGIS Environmental] | Technical/environmental GIS reference | 141 | Floods, hurricanes, wildfire, vulnerability, field data, water, climate, hazards, and environmental GIS workflows. |
| [Urban GIS] | Technical/planning GIS reference | 365 | Sustainable, inclusive, resilient planning; indicators; collaborative planning; VGI; scenario and equity support. |
| [Web Scraping Java] | Technical acquisition reference | 72 | Scraper brittleness, redirects, forms, Ajax, rate limits, persistence, tests, and connector caution. |
| [Greenfield Building Plan] | Governing build doctrine | 28 | Inspectable claim, greenfield assumption, trust spine, pre-RAW events, receipts, promotion gates, catalog closure. |
| [Pipeline Manual] | Governing pipeline manual | 30 | Lifecycle, query-save-validate-compile-review-promote-recompile loop, loop records, source-ledger discipline. |
| [Agriculture] | Domain-lane blueprint | 48 | Agriculture lane, source registries, CDL/landcover adjacency, validators, catalog closure, proof and rollback patterns. |
| [Archaeology Plan] | Domain-lane blueprint | 51 | Archaeology domain, exact-location denial, cultural/steward review, candidate evidence caution, public-safe outputs. |
| [Atmosphere Air] | Domain-lane blueprint | 52 | Air, smoke, climate, EO, observed/model/regulatory distinction, source-role and knowledge-character labels. |
| [Pass 19] | Immediate prior pass | 54 | Direct baseline for Pass 20; source drift, PMTiles attestation, watchers, fail-closed operational gates. |
| [KFM Encyclopedia] | Capability encyclopedia | 82 | Broad domain/capability atlas; inspectable claim and cross-domain capability vocabulary. |
| [Fauna] | Domain-lane blueprint | 37 | Taxon/occurrence/range/habitat lane, rare-species sensitivity, public-safe derivatives, source-role constraints. |
| [Flora] | Domain-lane blueprint | 36 | Flora lane, rare-plant controls, occurrence redaction, source-role distinctions, public-safe publication. |
| [Geology Resources] | Domain-lane blueprint | 42 | Geology/resource lane, public-safe geometry, geology versus legal/resource administration distinction. |
| [Governed AI Ledger] | Governed AI architecture | 36 | AI as provider-neutral, evidence-subordinate runtime; mock adapter, citation validation, finite runtime envelopes. |
| [Habitat] | Domain-lane blueprint | 28 | Habitat patches/suitability/connectivity, schema-home uncertainty, source registry, habitat proof-lane patterns. |
| [Habitat Fauna Thin Slice] | Thin-slice blueprint | 20 | Habitat/fauna public-safe occurrence assignment proof slice; controlled fixture-first domain implementation. |
| [Hazards] | Domain-lane blueprint | 26 | Hazards lane, life-safety boundary, official alerts, historical/regulatory/operational/context source separation. |
| [Hydrology] | Domain-lane blueprint | 43 | Hydrology proof lane, HUC12, NHDPlus HR, USGS Water Data, NFHL, source descriptors, catalog/proof closure. |
| [MapLibre Operating Manual] | Map/UI operating doctrine | 22 | MapLibre as downstream 2D renderer, governed shell, Evidence Drawer, Focus Mode, map artifact boundaries. |
| [Pass 18] | Cumulative prior pass | 509 | 500-card baseline, 14-category lineage, representation/API/analysis/field/release/map/UI/planning expansion. |
| [People DNA Land] | Domain-lane blueprint | 30 | People, genealogy, DNA, land-ownership assertion-first model, living-person/DNA restrictions, temporal land assertions. |
| [Roads Rail Trade] | Domain-lane blueprint | 35 | Roads, rail, trade routes, graph projections, Indigenous/cultural mobility caution, infrastructure exposure controls. |
| [Settlements Infrastructure] | Domain-lane blueprint | 43 | Settlements/infrastructure domain, legal city/infrastructure distinctions, critical infrastructure public-safety controls. |
| [Soil] | Domain-lane blueprint | 25 | Soil lane, SSURGO/SDA/Kansas Mesonet adjacency, soil/agriculture/hydrology connections, material-change concepts. |
| [Whole UI AI] | UI and governed-AI plan | 23 | Persistent shell, Evidence Drawer, Focus Mode, review console, mock governed API, finite UI outcomes. |
| [Master MapLibre Atlas] | Specialized cumulative atlas | 554 | MapLibre/tile/style/UI/Evidence Drawer/release architecture, PMTiles/COG/GeoParquet and source-watch details. |
| [New Ideas 5-10] | Operational delta packet | 319 | PMTiles sidecars, BLAKE3/Bao, DSSE/cosign, byte-range manifests, delta-aware artifacts, validators. |
| [New Ideas 5-15] | Operational delta packet | 220 | CDL/PLANTS material-change watchers, sidecars, thresholds, proposed work records, Gate A-C validation. |
| [New Ideas 5-8] | Operational delta packet | 321 | Environmental source-health and tile-health probes, MAIAC/FIRMS/SMAP/AirNow/Mesonet gates, run receipts. |
| [Ollama Ubuntu] | Local model runtime guide | 66 | Ollama behind governed API, provider-neutral runtime, structured outputs, evidence-bounded synthesis, finite outcomes. |

**Source-use determination:** Doctrine/control-plane sources govern adaptation. Technical references supply method vocabulary. Domain blueprints supply applied lane patterns. Prior passes supply continuity. New Ideas packets supply operational proposals. None of these source families alone proves current implementation.

## 4. Structural Rationale

The category structure follows dependency order rather than file order. This is necessary because the corpus is not a linear textbook collection. It is a mixture of governing doctrine, cumulative passes, technical references, domain-lane plans, and operational proposal packets. File order would overemphasize chronology and understate the trust dependencies that make KFM coherent.

The first category, **GOV**, comes first because all other ideas depend on truth posture, source authority, directory responsibility, and implementation-evidence boundaries. Without GOV, a reader could mistake a PDF-only blueprint for a repository patch, a map artifact for a truth object, or a convenient domain folder for an approved responsibility root [Directory Rules] [Pass 18] [Pass 19].

**SRC** comes next because source admission is the first operational edge. Before evidence can be bundled, mapped, analyzed, or published, sources must be identified, classified, role-labeled, checked for rights and currentness, and routed through RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED states. The New Ideas packets sharpen this into watcher events, ETag and Last-Modified checks, source-head probes, sidecars, and material-change thresholds [Pipeline Manual] [New Ideas 5-8] [New Ideas 5-15].

**EVD** follows SRC because admitted material must become inspectable evidence before it becomes a claim. EvidenceRef-to-EvidenceBundle resolution, source ledgers, RunReceipts, PromotionReceipts, AIReceipts, spec_hash, artifact hashes, catalog records, proof objects, and signed attestations are the machinery that keeps KFM from turning summaries, tiles, or generated text into root truth [Greenfield Building Plan] [Governed AI Ledger] [New Ideas 5-10].

**MOD** comes after evidence because KFM must know what kind of thing it is representing. The GIS, temporal database, domain-driven design, SQL, and 3D GIS references all show that representation is not neutral. Scale, projection, temporal semantics, valid time, source time, transaction time, 2.5D versus 3D, domain bounded contexts, and analytical rollups all affect what a public claim can honestly mean [GIS Primer] [Temporal SQL] [DDD Reference] [Archaeological 3D GIS].

**POL** is placed before validation and publication because public consequence changes the required burden of proof. Rights, sensitivity, living-person data, DNA, rare species, archaeology, infrastructure, hazards, and cultural or steward review can require denial, redaction, generalization, staged access, delayed publication, or abstention even where data and models are otherwise technically valid [People DNA Land] [Archaeology Plan] [Fauna] [Flora] [Hazards].

**VAL** then converts claims, artifacts, source changes, and proposed releases into executable decisions. It is intentionally later than MOD and POL because validation must know what the object is and what exposure policy applies. It is intentionally earlier than MAP, INT, and APP because public APIs, map layers, AI answers, planning dashboards, and domain pilots should not become ordinary outputs until validators, policy gates, receipts, release manifests, and rollback targets exist [Greenfield Building Plan] [Pipeline Manual] [New Ideas 5-10].

**MAP** is placed late even though KFM is map-first. This is a deliberate distinction between operating surface and truth authority. The map is central to use, but downstream in governance. MapLibre, PMTiles, COGs, MVT/MLT, LayerManifest, StyleManifest, TileArtifactManifest, MapReleaseManifest, Evidence Drawer, Story Nodes, and review UI must consume released artifacts and governed envelopes; they must not reach back into RAW, WORK, QUARANTINE, canonical stores, or direct model output [MapLibre Operating Manual] [Master MapLibre Atlas] [Whole UI AI].

**INT** follows MAP because interpretation depends on the same trust membrane. Spatial analysis, machine learning, local AI, Focus Mode, indicators, and planning support can be valuable only when they remain bounded, cited, and visibly uncertain. Their assumptions, weights, source roles, and scenario status must be inspectable, especially in planning contexts where indicators can imply policy preferences [AI Python] [Urban GIS] [Ollama Ubuntu].

**APP** comes last because the domain lanes are where the shared system is applied. Hydrology, habitat/fauna, soil/agriculture, atmosphere/hazards, roads/settlements, geology, archaeology, and people/DNA/land do not need separate root-level governance systems. They need domain-specific source roles, schemas, policies, fixtures, validators, public-safe derivatives, and proof slices under the shared KFM trust structure [Hydrology] [Habitat Fauna Thin Slice] [Soil] [Agriculture] [People DNA Land].

This order also resolves a structural tension inherited from prior passes. Pass 18 used 14 categories to capture a wide expansion surface [Pass 18]. Pass 19 retained that structure as a delta baseline [Pass 19]. Pass 20 compresses the surface into 9 top-level categories to satisfy the master dossier scope cap and to make dependency order easier to inspect. The compression is not loss: API, map, UI, release, analytics, field capture, and planning remain present as subcategories and idea entries.

### 4.1 Dependency-order map

| Stage | Category | Why it appears here |
|---:|---|---|
| 1 | GOV | Establishes what counts as evidence, authority, placement, and truthful implementation language. |
| 2 | SRC | Controls what may enter the system and how source change becomes proposed work. |
| 3 | EVD | Converts admitted material into inspectable evidence, receipts, proofs, and attestations. |
| 4 | MOD | Defines representation, temporal structure, domain semantics, and analytical meaning. |
| 5 | POL | Applies rights, sensitivity, public-safety, cultural, and access constraints before exposure. |
| 6 | VAL | Tests, gates, records, denies, quarantines, promotes, corrects, rolls back, and recompiles. |
| 7 | MAP | Carries released evidence through governed APIs, map artifacts, UI, and renderer surfaces. |
| 8 | INT | Supports bounded analysis, AI, indicators, Focus Mode, and planning interpretation. |
| 9 | APP | Applies the shared system to domain lanes and proof-bearing pilots. |

## 5. Master Category Map

Phase 3 seeded 72 unique Idea IDs across 9 categories, 8 ideas per category. Status distribution in `_ids.tsv` is 51 **CONFIRMED**, 19 **PROPOSED**, and 2 **NEEDS VERIFICATION**. The category map below records the main body structure that Section 6 will develop in prose.

| Order | Code | Category | Role in the dossier | Subcategories | Seeded ideas | Status mix |
|---:|---|---|---|---|---:|---|
| 1 | GOV | Doctrine, Authority, and Responsibility Boundaries | Establishes truth posture, authority order, directory responsibility, implementation-evidence limits, and reversible change discipline. | Truth posture and finite labels; authority ladder and source-family weight; Directory responsibility roots and drift discipline; implementation boundary and repo-evidence caution; change discipline, ADRs, and reversibility. | 8 | 7 CONFIRMED; 1 PROPOSED |
| 2 | SRC | Source Intake, Lifecycle, and Material-Change Governance | Governs source admission, source roles, pre-RAW controls, watchers, material-change detection, lifecycle movement, and no-autopublish posture. | SourceDescriptor and source-role registry; connector and scraper admission; watcher events and no-autopublish posture; material-change sidecars and proposed work records; environmental/ecology probes; endpoint/license/version verification backlog. | 8 | 5 CONFIRMED; 2 PROPOSED; 1 NEEDS VERIFICATION |
| 3 | EVD | Evidence, Provenance, Receipts, Identity, and Attestation | Defines inspectable evidence objects, receipts, hashes, catalog/proof/release separation, and artifact attestation. | EvidenceRef-to-EvidenceBundle resolution; receipts and process memory; deterministic identity and hashable specifications; artifact attestation and byte-range proofs; catalog closure; citation validation and explanation payloads. | 8 | 6 CONFIRMED; 2 PROPOSED |
| 4 | MOD | Representation, Spatial-Temporal Modeling, and Domain Semantics | Normalizes how KFM represents place, time, domain objects, uncertainty, and analytical meaning. | Cartographic representation; scale/CRS/projection/precision; spatial data models and topology; temporal semantics; bounded contexts and published language; analytical structures for panels, crosswalks, hierarchies, and rollups. | 8 | 6 CONFIRMED; 2 PROPOSED |
| 5 | POL | Policy, Rights, Sensitivity, and Public Safety | Keeps rights, source terms, sensitive locations, living-person data, DNA, archaeology, infrastructure, hazards, and public-safety constraints visible. | Rights/licensing/consent; sensitive locations; living-person/genealogy/DNA/land restrictions; hazards and life-safety limits; redaction/generalization/delayed publication/staged access; PolicyDecision and finite DENY/ABSTAIN/ERROR outcomes. | 8 | 7 CONFIRMED; 1 PROPOSED |
| 6 | VAL | Validation, QA, Observability, and Release Discipline | Converts proposed claims and artifacts into validated, quarantined, denied, corrected, rolled back, or released states. | Schema/contract/fixture validation; policy-as-code and promotion gates; artifact validators; temporal/spatial/source-role integrity; observability and finite negative outcomes; release manifests, correction, rollback, non-regression, and recompile discipline. | 8 | 4 CONFIRMED; 3 PROPOSED; 1 NEEDS VERIFICATION |
| 7 | MAP | Governed API, Map Artifacts, UI, and Renderer Boundaries | Places governed APIs, MapLibre, tiles, layer/style/release manifests, Evidence Drawer, Story Nodes, and review surfaces behind the trust membrane. | Governed API and resource contracts; MapLibre renderer boundary and shell; tile/raster/vector artifacts; layer/style/tile/release manifests; Evidence Drawer/Story Nodes/review surfaces; runtime/CDN/client parity/accessibility/performance budgets. | 8 | 5 CONFIRMED; 3 PROPOSED |
| 8 | INT | Analysis, AI, Interpretation, and Planning Support | Treats spatial analysis, AI, ML, indicators, Focus Mode, scenarios, and planning support as bounded interpretation, not root truth. | Spatial analysis and indicators; ML/anomaly detection/classification/clustering; governed AI adapters and structured synthesis; Focus Mode answers and abstentions; scenario/participatory/equity/resilience planning; uncertainty, bias, and model-risk controls. | 8 | 8 CONFIRMED |
| 9 | APP | Domain Lanes, Field Capture, and Applied Knowledge Families | Consolidates domain blueprints and field/remote/3D capture patterns into applied lanes and expansion targets. | Shared domain-lane packet; water/land/ecology/environmental domains; physical and built-environment domains; human/historical/cultural/sensitive domains; field/remote-sensing/3D observation carriers; thin slices, pilots, and applied expansion pathways. | 8 | 3 CONFIRMED; 5 PROPOSED |

### 5.1 Category roles by source family

| Category | Dominant source support | Main evidence use |
|---|---|---|
| GOV | [Directory Rules], [Greenfield Building Plan], [Pipeline Manual], [Implementation Reference], [Pass 18], [Pass 19] | Governing doctrine and implementation-boundary control. |
| SRC | [Pipeline Manual], [New Ideas 5-8], [New Ideas 5-15], [Hydrology], [Agriculture], [Soil], [Atmosphere Air] | Source admission, watchers, source roles, lifecycle state, and proposed work records. |
| EVD | [Greenfield Building Plan], [Governed AI Ledger], [Ollama Ubuntu], [Master MapLibre Atlas], [New Ideas 5-10], [Pass 19] | Evidence objects, receipts, signatures, hashes, sidecars, and provenance closure. |
| MOD | [GIS Primer], [Temporal SQL], [DDD Reference], [Advanced SQL], [Archaeological 3D GIS], [Urban GIS] | Representation, temporal structure, domain semantics, analytical patterns. |
| POL | [Fauna], [Flora], [Archaeology Plan], [People DNA Land], [Hazards], [Roads Rail Trade], [Settlements Infrastructure] | Rights, sensitivity, public safety, geoprivacy, living-person/DNA, cultural and steward review. |
| VAL | [Pipeline Manual], [Greenfield Building Plan], [New Ideas 5-8], [New Ideas 5-10], [New Ideas 5-15], domain blueprints | Validator-first readiness, CI probes, release gates, observability, correction, rollback. |
| MAP | [Web APIs], [MapLibre Operating Manual], [Master MapLibre Atlas], [Whole UI AI], [Pass 18], [Pass 19] | Governed API, renderer boundaries, tile artifacts, manifests, trust-visible UI. |
| INT | [AI Python], [Advanced SQL], [ArcGIS Environmental], [Urban GIS], [Ollama Ubuntu], [Governed AI Ledger] | Bounded analysis, AI, ML, indicators, scenarios, Focus Mode, planning support. |
| APP | [Hydrology], [Habitat], [Habitat Fauna Thin Slice], [Fauna], [Flora], [Soil], [Agriculture], [Geology Resources], [Hazards], [People DNA Land] | Domain-lane synthesis, applied proof slices, field/remote/3D expansion families. |

### 5.2 Main-body allocation rule

Each category has 8 seeded Idea IDs, which fits the requested 6–12 ideas per category. Section 6 will develop these as prose entries. Secondary ideas, endpoint-specific checks, package-version claims, repeated lane variants, and implementation paths that require repo inspection are routed to Section 10 or Appendix A rather than expanding the main body beyond the cap.

## 6. Detailed Idea Chapters by Category

This section develops the seeded Idea IDs from `_ids.tsv` into prose entries. Each chapter is written from the Phase 2 notes and Phase 3 category tree, with the ID registry treated as the stability source for ID, title, category, status, and short-tag attribution. The main body keeps to the requested cap of eight entries per category. More granular source-specific variants, endpoint checks, package-version claims, and implementation-path proposals are routed later to the Expansion Agenda, Open Questions, or appendices rather than expanding the category chapters beyond their target size.

Status labels inside each entry follow the document truth posture. A CONFIRMED idea is confirmed as doctrine, source content, repeated warning, method, or synthesis basis in the attached corpus. It is not a claim that corresponding code, schema, policy, route, validator, dashboard, or runtime behavior is implemented in a live repository unless live implementation evidence is cited. PROPOSED entries identify synthesis or implementation directions supported by the corpus but not settled as implementation fact. NEEDS VERIFICATION entries identify checkable operational claims that must be verified before use.

### 6.1 GOV — Doctrine, Authority, and Responsibility Boundaries

#### 6.1.1 Category Overview

GOV is a central category. It is central not because it contains the most implementation tasks, but because it decides how all other tasks remain trustworthy. The attached corpus repeatedly shows that KFM can fail before it ever ingests a source or renders a map if it lets fluent prose, prior-pass lineage, domain enthusiasm, or proposed file paths masquerade as proof. GOV therefore establishes the working constitution for the rest of the dossier: truth labels, cite-or-abstain, responsibility-root directory rules, implementation-evidence boundaries, schema-home discipline, public trust membranes, and documentation as a control plane.

The category is CONFIRMED as a corpus-derived center of gravity. It is supported most directly by the explicit doctrine in `[Directory Rules]`, `[Greenfield Building Plan]`, and `[Pipeline Manual]`, and reinforced by the source-boundary caution in `[Pass 18]`, `[Pass 19]`, `[Governed AI Ledger]`, and `[Whole UI AI]`. It also governs how the other source families are used. A technical reference may teach a useful method, but GOV decides that KFM adoption requires evidence, policy, validation, release state, and bounded claims. A domain blueprint may propose a path, schema, or lane package, but GOV decides that current repo evidence and Directory Rules must be checked before implementation. A map or AI answer may be useful, but GOV decides that it stays downstream of evidence and review.

#### 6.1.2 Subcategories

The first GOV subcategory is truth posture and finite labels: CONFIRMED, PROPOSED, NEEDS VERIFICATION, UNKNOWN, DENY, ABSTAIN, and ERROR. These labels are not decoration; they control whether a statement can be treated as evidence, recommendation, backlog, or failure state. The second subcategory is authority and source-boundary discipline, which prevents prior pass summaries, no-repo reports, public-repo summaries, and technical references from being flattened into one undifferentiated authority. The third is responsibility-root directory governance, which treats file placement as a governance act rather than a convenience decision. The fourth is schema-home and ADR discipline, especially where `contracts/`, `schemas/`, and `schemas/contracts/v1` might otherwise drift into parallel authority. The fifth is public trust membrane doctrine: public clients, maps, UI surfaces, and model runtimes stay behind governed APIs and released artifacts. The sixth is living documentation control, where docs, registries, ADRs, source ledgers, drift registers, and progress files are part of the system's auditability.

#### 6.1.3 Individual Idea Entries

##### KFM-IDX-GOV-001 — Inspectable Claim as the Durable Public Unit

**Status and category.** CONFIRMED. Category: GOV / truth posture and public value. Source attribution: [Greenfield Building Plan] [KFM Encyclopedia] [Pass 19]. Related ideas include KFM-IDX-EVD-001, KFM-IDX-EVD-002, KFM-IDX-MAP-006, and KFM-IDX-INT-007.

**Normalized statement.** KFM's durable public unit of value is the inspectable claim: a statement whose evidence, source role, spatial and temporal scope, policy posture, review state, release state, and correction lineage can be inspected.

**Detailed explanation and why it matters.** This idea is the first GOV entry because it prevents KFM from being mistaken for a map gallery, a dashboard suite, a chatbot, a domain database, or a pile of PDFs. The corpus repeatedly says that maps, tiles, graphs, scenes, summaries, AI answers, vector indexes, and dashboards are carriers of evidence rather than sovereign truth. The inspectable claim is the object that gives those carriers meaning. A floodplain layer, a habitat assignment, a historic road corridor, a soil property map, or a Focus Mode answer is only KFM-grade when a user or reviewer can trace what is being claimed, what evidence supports it, what source role that evidence has, what policy and review controls were applied, and how the claim can be corrected or rolled back.

**Dependencies, tensions, and limits.** This idea depends on EVD evidence resolution, SRC source-role discipline, MOD spatial-temporal semantics, POL exposure controls, VAL validation and release gates, and MAP/UI surfaces that can show trust state. Its main tension is usability: ordinary users may want a simple map answer, while KFM requires enough inspectability to keep the answer honest. That tension should be handled by UI design and Evidence Drawer layering, not by removing the evidence boundary.

**Expansion directions and future work.** Future work should define a concise `InspectableClaim` acceptance checklist that can be used across domain lanes without creating a new sovereign object that duplicates EvidenceBundle or DecisionEnvelope. Open questions include whether inspectable claims should be explicit stored records, derived views over evidence and release objects, or both depending on publication significance.

##### KFM-IDX-GOV-002 — Truth Labels and Cite-or-Abstain as Operating Posture

**Status and category.** CONFIRMED. Category: GOV / truth posture. Source attribution: [Directory Rules] [Greenfield Building Plan] [Pass 18] [Pass 19]. Related ideas include KFM-IDX-EVD-003, KFM-IDX-VAL-007, KFM-IDX-POL-008, and KFM-IDX-INT-007.

**Normalized statement.** KFM should label claims by evidence strength and should cite support or abstain when support is missing, weak, inaccessible, or not appropriate for the requested exposure.

**Detailed explanation and why it matters.** Truth labels are a recurring corpus device for avoiding persuasive overclaiming. They separate direct evidence from synthesis, checkable but unverified claims, and unknowns. In this dossier, the same posture governs every idea entry: CONFIRMED means supported by the attached corpus or current working artifacts, not necessarily implemented in a live repo. PROPOSED means a synthesis or future direction consistent with the corpus. NEEDS VERIFICATION means a concrete check is required before operational use. UNKNOWN means the pass cannot establish the claim. Cite-or-abstain gives the posture teeth. A KFM answer that cannot resolve evidence should not fill the gap with model fluency, map intuition, or domain plausibility.

**Dependencies, tensions, and limits.** This idea depends on source ledgers, EvidenceBundle resolution, citation validation, finite outcome envelopes, and UI surfaces that can display abstention without making it look like failure. It also depends on editorial discipline: labels must not be used as rhetorical emphasis or ignored when inconvenient. The limitation is that truth labels require careful maintenance. A claim that was NEEDS VERIFICATION yesterday may become CONFIRMED after a source check, and a claim that was CONFIRMED in one run may be stale in another if it depends on external versions or endpoint status.

**Expansion directions and future work.** The strongest expansion path is a truth-label lint or review checklist for major docs, API payloads, and Focus Mode outputs. Suggested future work is to define when claim-level labels, section-level labels, and object-level finite outcomes are required, so the system remains readable without losing auditability.

##### KFM-IDX-GOV-003 — Responsibility-Root Directory Governance

**Status and category.** CONFIRMED. Category: GOV / directory authority and responsibility roots. Source attribution: [Directory Rules]. Related ideas include KFM-IDX-GOV-005, KFM-IDX-VAL-006, KFM-IDX-APP-006, and KFM-IDX-MAP-005.

**Normalized statement.** File location in KFM encodes ownership, governance, and lifecycle responsibility; topic alone does not justify a root folder.

**Detailed explanation and why it matters.** Directory governance appears mundane, but in KFM it is a trust control. The corpus repeatedly proposes domain lanes, schemas, validators, source registries, policies, runbooks, release artifacts, proofs, receipts, and UI surfaces. Without placement doctrine, those proposals could easily become parallel roots, duplicate schema homes, duplicate policy stores, or domain-specific authority islands. `[Directory Rules]` makes the deeper rule explicit: repo-root folders should exist only for repo-wide responsibilities such as truth, evidence, release, policy, deployable systems, lifecycle data, tests, infrastructure, runtime, or genuinely cross-domain concerns. Domain depth belongs inside lanes and responsibility roots, not in convenience buckets.

**Dependencies, tensions, and limits.** This idea depends on accepted ADRs, per-root README files, drift registers, and current repo inspection before implementation. Its major tension is that domain work often feels easier when a domain gets a new top-level folder. That convenience is exactly the drift risk KFM is trying to avoid. The limitation in this pass is that no current repo tree was inspected, so all concrete placement recommendations remain PROPOSED unless directly supported by Directory Rules as doctrine.

**Expansion directions and future work.** The next useful artifact is a path-proposal checklist for implementation agents: identify owning root, lifecycle phase, governance authority, compatibility roots, affected ADRs, and rollback/migration path before creating files. Open questions include how strictly to enforce older compatibility roots such as `ui`, `web`, `jsonschema`, `policies`, `styles`, `viewer_templates`, and `artifacts` when future repo evidence shows they exist.

##### KFM-IDX-GOV-004 — Implementation Evidence Boundary and No-Overclaim Rule

**Status and category.** CONFIRMED. Category: GOV / implementation-boundary discipline. Source attribution: [Pass 18] [Pass 19] [Governed AI Ledger] [Whole UI AI]. Related ideas include KFM-IDX-GOV-008, KFM-IDX-VAL-008, KFM-IDX-SRC-008, and KFM-IDX-MAP-001.

**Normalized statement.** KFM must distinguish doctrine, lineage, proposed architecture, generated artifacts, and current implementation proof; it must not claim repo files, runtime behavior, CI enforcement, routes, schemas, or deployment maturity without current evidence.

**Detailed explanation and why it matters.** Many attached PDFs are excellent architecture and implementation-grade planning artifacts, but many were produced in no-mounted-repo contexts. They record useful source roles, file matrices, policies, validators, fixtures, proof plans, and rollback patterns. They do not prove that those files exist in a current repository. Pass 18 and Pass 19 carry the same caution at cumulative scale. The Governed AI and Whole UI reports also bound their proposed paths and contracts because no live repo was mounted in those runs. This idea keeps KFM from converting ambition into false maturity.

**Dependencies, tensions, and limits.** The idea depends on Phase 1 inventory discipline, source-family weighting, progress logs, and a refusal to let repeated proposals count as independent implementation proof. The tension is that implementation-ready plans often use exact paths and object names so future work can proceed efficiently. Exactness can be useful and still remain PROPOSED. The limitation is that implementation evidence can exist outside this pass; the dossier should mark it UNKNOWN rather than deny it unless the current pass has inspected it.

**Expansion directions and future work.** A future implementation-verification pass should mount or inspect the target repo, record branch and dirty state, check ADRs, scan schemas/contracts/policy/tests/workflows, and emit a bounded current-state report. That report could upgrade specific GOV-adjacent claims from UNKNOWN to CONFIRMED without weakening the no-overclaim rule.

##### KFM-IDX-GOV-005 — Schema-Home and ADR Discipline

**Status and category.** CONFIRMED. Category: GOV / schema authority and change governance. Source attribution: [Directory Rules] [Implementation Reference] [Pass 19]. Related ideas include KFM-IDX-MOD-005, KFM-IDX-VAL-006, KFM-IDX-MAP-002, and KFM-IDX-APP-001.

**Normalized statement.** KFM must settle schema-home authority through Directory Rules and accepted ADRs, and must avoid parallel homes for schemas, contracts, policies, sources, registries, releases, proofs, or receipts.

**Detailed explanation and why it matters.** The corpus contains a repeated schema-home tension: some prior reports refer to `contracts/`, others to `schemas/`, and Directory Rules now state `schemas/contracts/v1/<...>` as the default convention while still requiring path verification against mounted repo evidence and accepted ADRs. This matters because schemas and contracts are not cosmetic. They define machine-readable truth surfaces, API payloads, validators, release gates, and review expectations. Parallel schema homes create quiet divergence: two files may appear to define the same object while validators, docs, and APIs disagree about which one is authoritative.

**Dependencies, tensions, and limits.** This idea depends on the directory authority order, accepted ADRs, current repo evidence, and validation gates that detect drift. It also depends on documentation discipline: ADRs must be retained when superseded, not erased. The tension is backward compatibility. If a live repo already has both `contracts/` and `schemas/`, a migration plan may be safer than abrupt deletion. The limitation is that Pass 20 cannot resolve current repo authority without live evidence.

**Expansion directions and future work.** The strongest future artifact is a schema-home verification and migration note that maps existing schema, contract, JSON Schema, OpenAPI, policy, and validator files to the accepted authority model. Suggested future work is an automated drift detector that flags duplicate definitions and requires ADR references for root or schema-home changes.

##### KFM-IDX-GOV-006 — Public Clients Stay Behind the Trust Membrane

**Status and category.** CONFIRMED. Category: GOV / public trust membrane. Source attribution: [MapLibre Operating Manual] [Whole UI AI] [Ollama Ubuntu]. Related ideas include KFM-IDX-MAP-001, KFM-IDX-MAP-006, KFM-IDX-EVD-002, KFM-IDX-POL-002, and KFM-IDX-INT-007.

**Normalized statement.** Public clients, ordinary UI surfaces, MapLibre shells, Focus Mode, and model runtimes should consume governed APIs, released artifacts, catalog records, tile services, and EvidenceBundle-backed envelopes, not canonical stores, RAW/WORK/QUARANTINE data, or direct model output.

**Detailed explanation and why it matters.** KFM is map-first and increasingly AI-aware, but the corpus insists that maps and AI remain downstream. The MapLibre manual states that MapLibre is a disciplined 2D renderer and interaction runtime, not a truth store, source registry, policy engine, citation authority, review authority, publication authority, or AI authority. The Whole UI plan and Ollama guide extend the same rule into UI and local model runtime: the public surface should receive bounded, released, policy-safe context through governed APIs and finite response envelopes. This protects the system from the most tempting shortcut: letting a convenient UI, tile URL, vector store, or local model read internal truth directly.

**Dependencies, tensions, and limits.** The idea depends on MAP resource contracts, EVD evidence resolution, POL exposure gates, VAL release checks, and finite negative outcomes such as ABSTAIN, DENY, and ERROR. Its tension is performance and developer ergonomics: direct access is often easier and faster during experiments. KFM can support internal tools and dry runs, but those cannot become the normal public path. The limitation is that exact API routes and UI components remain UNKNOWN in this pass.

**Expansion directions and future work.** Future work should define a trust-membrane acceptance test: no public client should import or fetch RAW/WORK/QUARANTINE, unpublished candidates, canonical stores, direct model endpoints, or unreviewed layer sources. A small fixture-backed governed API slice can prove the rule without requiring a full production system.

##### KFM-IDX-GOV-007 — Documentation as a Living Control Plane

**Status and category.** CONFIRMED. Category: GOV / documentation control. Source attribution: [Pipeline Manual] [Directory Rules] [KFM Encyclopedia]. Related ideas include KFM-IDX-GOV-002, KFM-IDX-SRC-001, KFM-IDX-EVD-003, KFM-IDX-VAL-006, and KFM-IDX-APP-008.

**Normalized statement.** KFM documentation is part of the governed system: it records authority, source ledgers, ADRs, registries, drift, validation posture, progress, open questions, corrections, and release decisions rather than merely explaining code after the fact.

**Detailed explanation and why it matters.** The corpus uses documents as active control surfaces. Directory Rules define placement authority. The Pipeline Manual defines lifecycle and loop doctrine. The KFM Encyclopedia maps domains, capabilities, actions, views, validation needs, and sensitive registers. Domain-lane PDFs preserve continuity, unknowns, and proposed implementation plans. In Pass 20 itself, `_inventory.md`, `_notes.md`, `_categories.md`, `_ids.tsv`, `_progress.md`, and the master Markdown file are working memory and audit artifacts. This approach makes documentation part of governance and recoverability, not a substitute for implementation proof.

**Dependencies, tensions, and limits.** The idea depends on source ledgers, progress markers, ADRs, drift registers, and truth labels. It also depends on editors not treating polished prose as evidence. The tension is document sprawl: KFM has many reports, and without ledgers and supersession discipline, documentation can become another source of ambiguity. The limitation is that docs must be tied to behavior, validators, receipts, or review state when behavior changes materially.

**Expansion directions and future work.** Suggested future work is a documentation control-plane index that records each doctrine file, domain report, pass, registry, ADR, and manual with status, authority, supersession, owner, and verification needs. This would help later writers and implementers preserve continuity without letting old PDFs silently outrank current evidence.

##### KFM-IDX-GOV-008 — Greenfield, No-Repo, and Public-Repo Sources Stay Source-Bounded

**Status and category.** PROPOSED. Category: GOV / source-boundary reconciliation. Source attribution: [Greenfield Building Plan] [Implementation Reference] [Pass 19]. Related ideas include KFM-IDX-GOV-004, KFM-IDX-VAL-008, KFM-IDX-SRC-008, and KFM-IDX-APP-008.

**Normalized statement.** KFM should reconcile greenfield plans, no-mounted-repo PDF reports, and connector-era public-repo summaries by preserving their source boundaries instead of forcing them into one false current-state narrative.

**Detailed explanation and why it matters.** This idea is PROPOSED because it is an organizing interpretation of the corpus rather than a single doctrine sentence. The Greenfield Building Plan assumes a zero-start condition so it can define a clean build strategy. Many domain reports record no mounted repo in their runs and therefore produce PDF-only implementation blueprints. `[Implementation Reference]` reports a connector-reviewed public repository with meaningful surface area. Pass 19 preserves implementation uncertainty. These can coexist if each source is read within its boundary. The greenfield plan is useful doctrine for how to build from zero. No-repo reports are useful planning and caution evidence. The public-repo summary is useful lineage and a verification prompt. None should be silently converted into current Pass 20 implementation fact.

**Dependencies, tensions, and limits.** This idea depends on GOV truth labels, EVD source ledgers, and VAL verification backlog discipline. The tension is editorial simplicity: a single maturity statement would be easier to read, but it would be less truthful. The limitation is that source-boundary reconciliation does not answer the current implementation question; it only prevents premature answers.

**Expansion directions and future work.** The next step is a dedicated implementation-evidence reconciliation pass after live repo inspection. It should compare the Greenfield plan, Directory Rules, Pass 19, Implementation Reference, and current repo tree; classify each claimed surface as present, absent, drifted, superseded, or needs migration; and emit an ADR/drift/update backlog rather than rewriting history.

### 6.2 SRC — Source Intake, Lifecycle, and Material-Change Governance

#### 6.2.1 Category Overview

SRC is a central supporting category. It governs the admission edge: how external material, source feeds, archived documents, environmental products, domain datasets, scraper outputs, and watcher observations become KFM work without becoming public truth prematurely. The corpus repeatedly describes source intake as a governed process rather than a fetch operation. A source must be identified, assigned a role, checked for rights and sensitivity, routed through lifecycle states, and converted into evidence-bearing artifacts only after validation and policy gates have something concrete to inspect [Pipeline Manual] [Greenfield Building Plan] [Hydrology].

This category is especially important because many KFM domains depend on external systems whose status, formats, terms, and update cadences can change. Hydrology may depend on USGS and FEMA sources; ecology may depend on GBIF, eBird, FIRMS, MAIAC, SMAP, Mesonet, CDL, or PLANTS; roads and settlements may depend on official or open geospatial feeds; archaeology and people/land sources may require steward review and access restrictions. SRC therefore defines the difference between observing a source, proposing work, admitting material, quarantining material, processing material, cataloging material, and publishing material [New Ideas 5-8] [New Ideas 5-15].

The main tension is speed versus governance. Watchers and source-health probes make KFM more responsive, but the corpus is clear that watchers must not become publishers. They may emit events, receipts, sidecars, and proposed work records. They may not bypass evidence, rights, sensitivity, validation, review, catalog closure, or release state.

#### 6.2.2 Subcategories

The first SRC subcategory is canonical lifecycle discipline: RAW -> WORK or QUARANTINE -> PROCESSED -> CATALOG or TRIPLET -> PUBLISHED. The second is source identity and source-role governance, where each source is allowed to support only certain kinds of claims. The third is connector and watcher admission, including pre-RAW events, no-autopublish posture, and source-head checks. The fourth is material-change governance: sidecars, stable `spec_hash`, thresholds, histograms, and PROPOSED_WORK_RECORD outboxes. The fifth is operational source-health monitoring for environmental and tile-health probes. The sixth is source currentness, endpoint, rights, license, consent, and version verification before any source or artifact can be treated as operationally safe.

#### 6.2.3 Individual Idea Entries

##### KFM-IDX-SRC-001 — Canonical Lifecycle from RAW to PUBLISHED

**Status and category.** CONFIRMED. Category: SRC / canonical lifecycle discipline. Source attribution: [Directory Rules] [Greenfield Building Plan] [Pipeline Manual] [Hydrology]. Related ideas include KFM-IDX-GOV-003, KFM-IDX-SRC-004, KFM-IDX-EVD-008, KFM-IDX-VAL-002, and KFM-IDX-MAP-001.

**Normalized statement.** KFM source material should move through a governed lifecycle - RAW to WORK or QUARANTINE to PROCESSED to CATALOG or TRIPLET to PUBLISHED - and public exposure should occur only after release gates, not by moving or copying files.

**Detailed explanation and why it matters.** The lifecycle is one of the most repeated invariants in the corpus. It prevents a source file, API payload, tile archive, domain fixture, or observed feed from becoming public truth simply because it exists. RAW preserves intake material. WORK allows processing and normalization. QUARANTINE isolates material with rights, schema, sensitivity, integrity, or source-role problems. PROCESSED records transformed outputs. CATALOG and TRIPLET provide governed metadata and graph representations. PUBLISHED is a release state, not a directory shortcut. The lifecycle creates a place for evidence, validation, policy, receipts, and rollback at each step.

**Dependencies, tensions, and limits.** This idea depends on Directory Rules, source descriptors, data lifecycle folders, validators, release manifests, and policy gates. Its tension is that external sources often arrive in formats that tempt direct publication, especially when they already look like map layers. KFM must resist that shortcut. The limitation is that actual lifecycle directories, policies, and workflows remain UNKNOWN in this pass unless supported by a specific attached document.

**Expansion directions and future work.** Future work should define lifecycle transition receipts and minimal requirements for each state. A useful first test is a fixture that enters RAW, fails one gate into QUARANTINE, then passes a corrected path into PROCESSED and CATALOG without ever becoming public until a release manifest exists. Open questions include how to handle temporary previews and whether preview layers need a separate non-public lifecycle state.

##### KFM-IDX-SRC-002 — Source Descriptor and Source-Role Registry

**Status and category.** CONFIRMED. Category: SRC / source identity and role governance. Source attribution: [Hydrology] [Fauna] [Flora] [Roads Rail Trade] [Pass 19]. Related ideas include KFM-IDX-EVD-003, KFM-IDX-MOD-008, KFM-IDX-POL-002, KFM-IDX-APP-001, and KFM-IDX-APP-006.

**Normalized statement.** Each KFM source should have an explicit descriptor and source-role registry entry that defines identity, authority, rights, update cadence, permitted claim roles, limitations, and release constraints.

**Detailed explanation and why it matters.** The domain blueprints converge on source-role discipline. A source that is useful for occurrence evidence is not necessarily a legal-status authority. A regulatory flood layer is not an observed flood event. A community-science record is not the same as a steward-reviewed sensitive occurrence. A road geometry feed is not automatically an operator, restriction, or historical corridor authority. SourceDescriptor and source-role registry concepts prevent these collapses by recording what a source is allowed to support. This is a central KFM adaptation of ordinary data cataloging: the system needs not just where a source came from, but what kind of truth it may carry.

**Dependencies, tensions, and limits.** The idea depends on SRC lifecycle, EVD source ledgers, MOD knowledge-character labels, POL rights and sensitivity gates, and VAL validators that deny unsupported source-role use. The tension is that one source may have multiple roles in different contexts. The limitation is that precise source descriptors for each live source require current rights, endpoint, and steward verification.

**Expansion directions and future work.** A strong future artifact is a registry schema that requires `source_id`, `source_role`, `authority_scope`, `rights_state`, `sensitivity_state`, `update_cadence`, `retrieval_method`, `permitted_claims`, and `not_authoritative_for`. Open questions include how to version role decisions and how to handle sources whose authority changes over time. Suggested future work is a source-role denial test: a validator should reject a claim when the cited source lacks the required role.

##### KFM-IDX-SRC-003 — Pre-RAW Events and Watcher Non-Publisher Posture

**Status and category.** CONFIRMED. Category: SRC / pre-RAW and watcher discipline. Source attribution: [Greenfield Building Plan] [Pipeline Manual] [New Ideas 5-8]. Related ideas include KFM-IDX-SRC-006, KFM-IDX-SRC-007, KFM-IDX-VAL-003, KFM-IDX-EVD-004, and KFM-IDX-GOV-006.

**Normalized statement.** Watchers and pre-RAW event handlers may observe, record, and propose work, but they must not publish or admit material into public truth without governed review, validation, and promotion.

**Detailed explanation and why it matters.** The Greenfield plan adds a pre-RAW event family, and the Pipeline Manual extends KFM through query-save-validate-compile-review-promote-recompile loops. New Ideas 5-8 makes the pattern operational by describing environmental probes for source heads, AOD, fire detections, SMAP recency, AirNow API access, and Mesonet consent. These mechanisms are valuable because they make KFM responsive to source drift and environmental change. They are risky if misunderstood. A watcher event is not an accepted source, not evidence closure, not policy approval, and not a publication decision. It is an observation that may trigger a governed process.

**Dependencies, tensions, and limits.** This idea depends on finite event envelopes, run receipts, policy denial defaults, and validators that separate observation from publication. The tension is operational pressure: a watcher may detect something that looks important, such as fire, poor air quality, or source outage. KFM still must not become an emergency alerting system or public source of unreviewed claims. The limitation is that live watcher endpoints and current data cadence were not verified in this pass.

**Expansion directions and future work.** Future work should define `WatcherEvent`, `PrefilterOutput`, and `ProposedWorkRecord` contracts with explicit `may_publish: false` posture unless promotion later approves exposure. Open questions include how quickly urgent source-health events should surface to internal reviewers. A safe first slice is a no-network fixture watcher that emits one source-head change, one ABSTAIN, and one quarantine recommendation.

##### KFM-IDX-SRC-004 — Promotion as Governed State Transition

**Status and category.** CONFIRMED. Category: SRC / promotion and lifecycle state. Source attribution: [Directory Rules] [Greenfield Building Plan] [Pipeline Manual]. Related ideas include KFM-IDX-SRC-001, KFM-IDX-EVD-004, KFM-IDX-EVD-008, KFM-IDX-VAL-002, and KFM-IDX-VAL-007.

**Normalized statement.** Promotion is a governed state transition supported by validation, policy, evidence, review, release manifest, correction path, and rollback target; it is not a file move.

**Detailed explanation and why it matters.** The corpus repeats this idea because it is easy to violate. Without governed promotion, `PUBLISHED` becomes a directory name rather than a release status. A file could be copied into a public location while source rights, sensitivity, schema validity, proof closure, catalog records, and rollback targets remain unresolved. KFM's promotion idea instead requires a state transition with evidence and process memory. It should be possible to inspect why a source artifact moved forward, which gates passed, which policy applied, who or what reviewed it, which manifest identifies the release set, and where rollback would return the system.

**Dependencies, tensions, and limits.** The idea depends on EVD receipts and proof separation, POL policy outcomes, VAL promotion gates, and MAP release manifests for public artifacts. The tension is that some data systems treat publication as deployment or file synchronization. KFM treats it as governance. The limitation is that the exact implementation of PromotionDecision, PromotionReceipt, or gates is not verified in this pass.

**Expansion directions and future work.** A first implementation target should define a promotion dry run that cannot write to public surfaces but can emit a PromotionReceipt-like record. Open questions include how to represent partial promotion, withdrawal, and supersession. Suggested future work is to create a promotion-state test matrix covering PASS, DENY, ABSTAIN, ERROR, rollback, and correction.

##### KFM-IDX-SRC-005 — Catalog Closure Before Public Release

**Status and category.** CONFIRMED. Category: SRC / catalog and publication readiness. Source attribution: [Hydrology] [Greenfield Building Plan] [Master MapLibre Atlas]. Related ideas include KFM-IDX-EVD-008, KFM-IDX-MAP-005, KFM-IDX-VAL-002, KFM-IDX-MAP-004, and KFM-IDX-APP-001.

**Normalized statement.** Public release should require catalog closure: source, evidence, provenance, artifact, policy, release, and rollback metadata must be sufficiently complete before public exposure.

**Detailed explanation and why it matters.** Domain blueprints and MapLibre materials repeatedly describe catalog, proof, receipt, and release objects as separate but coordinated. Hydrology uses catalog closure to keep water-source descriptors, observations, map layers, and proof objects aligned. The Greenfield plan frames STAC, DCAT, PROV, release manifests, and proof packs as publication prerequisites. The Master MapLibre Atlas extends the idea to tile and artifact manifests. Catalog closure ensures that public users do not receive an orphaned tile, API payload, or layer whose source identity, rights posture, digest, provenance, or rollback path is unclear.

**Dependencies, tensions, and limits.** This idea depends on EVD proof/citation objects, SRC source descriptors, VAL validators, MAP artifact manifests, and POL exposure checks. The tension is that catalog closure can look like extra paperwork when a layer appears to render correctly. But visual correctness is not release readiness. The limitation is that exact catalog profiles and release schemas remain proposed unless verified in a mounted implementation.

**Expansion directions and future work.** Future work should define a minimal catalog closure checklist for one pilot lane, ideally hydrology or PMTiles attestation. Open questions include how much catalog completeness is required for internal previews versus public release. Suggested future work is to validate a PMTiles or GeoParquet artifact against STAC/DCAT/PROV, a release manifest, and a rollback reference before making it available to MapLibre.

##### KFM-IDX-SRC-006 — Material-Change Sidecars and PROPOSED_WORK_RECORD Outbox

**Status and category.** PROPOSED. Category: SRC / material-change governance. Source attribution: [New Ideas 5-15]. Related ideas include KFM-IDX-VAL-004, KFM-IDX-EVD-005, KFM-IDX-APP-004, KFM-IDX-SRC-003, and KFM-IDX-SRC-008.

**Normalized statement.** Material-change watchers should use stable sidecars, source heads, thresholds, and proposed-work outboxes so KFM acts on meaningful source changes rather than noisy updates.

**Detailed explanation and why it matters.** New Ideas 5-15 gives a concrete pattern for USDA Cropland Data Layer and PLANTS county packages. A sidecar records source URL, ETag, Last-Modified, year, county FIPS, class histograms, classmap version, thresholds, and a stable `spec_hash`. A watcher compares sidecars and emits a PROPOSED_WORK_RECORD only when a material threshold is crossed, such as a reclassification above a relative percentage or an absolute area change. This is a strong KFM idea because it separates change detection from publication. It also prevents wasteful reprocessing when source bits change but the public or analytical claim would not materially change.

**Dependencies, tensions, and limits.** The idea depends on deterministic canonicalization, sidecar schemas, source-head collection, materiality thresholds, and outbox processing that cannot publish directly. The tension is threshold design: thresholds are policy and operational choices, not universal science. The limitation is that the watcher code in the packet is proposal material and uses stubs; it needs real data paths, rights verification, and fixtures.

**Expansion directions and future work.** A first implementation slice should use fixture counties and synthetic histograms, not live CDL. Open questions include how to tune thresholds by county size, crop class, or domain significance. Suggested future work is a validator that recomputes `spec_hash`, checks ETag/Last-Modified presence, verifies histogram units, and denies publication when a material-change record has not passed review.

##### KFM-IDX-SRC-007 — Ecology Source-Health and Tile-Health Watchers

**Status and category.** PROPOSED. Category: SRC / operational source-health probes. Source attribution: [New Ideas 5-8] [Pass 19]. Related ideas include KFM-IDX-VAL-003, KFM-IDX-APP-003, KFM-IDX-POL-002, KFM-IDX-MOD-008, and KFM-IDX-MAP-005.

**Normalized statement.** KFM can use ecology and environmental probes to watch source health and tile health, but the watcher outputs should remain policy-bound, receipt-emitting, and non-publishing.

**Detailed explanation and why it matters.** New Ideas 5-8 proposes a compact operational gating spec for environmental signals: MAIAC AOD thresholds, FIRMS fire proximity and Fire Radiative Power, SMAP recency checks, AirNow API-key status, and Mesonet license enforcement. The packet also describes recording source URL, dataset/version, request headers, ETag, Last-Modified, spatial/temporal window, derivation metrics, finite decisions, and signed run receipts. Pass 19 interprets these ideas as a source-drift and artifact-readiness delta. The normalized KFM idea is that environmental source monitoring can improve reliability and public safety posture, but it must be bounded by source roles, rights, policy, and review.

**Dependencies, tensions, and limits.** The idea depends on source descriptors, knowledge-character labels, policy profiles, run receipts, and fail-closed validators. The tension is that terms like QUARANTINE, ESCALATE, or TILE_DEGRADED may sound operationally urgent. KFM must not turn them into emergency warnings or unsupported public hazard claims. The limitation is that the current status of the referenced feeds and thresholds was not independently verified in this pass.

**Expansion directions and future work.** Future work should build a no-network probe fixture suite with canned ETag, Last-Modified, AOD, FRP, and consent cases. Open questions include whether thresholds should be per-domain policy, per-layer policy, or source-specific profiles. Suggested future work is a watcher decision envelope with explicit `not_for_life_safety` and `no_publication` fields.

##### KFM-IDX-SRC-008 — Currentness, Endpoint, Rights, and Version Reverification

**Status and category.** NEEDS VERIFICATION. Category: SRC / external and operational verification. Source attribution: [New Ideas 5-8] [New Ideas 5-10] [Pass 19]. Related ideas include KFM-IDX-GOV-004, KFM-IDX-POL-002, KFM-IDX-VAL-008, KFM-IDX-MAP-008, and KFM-IDX-APP-003.

**Normalized statement.** Any source activation, package pin, endpoint assumption, rights claim, tool-version claim, or operational watcher threshold must be reverified before operational use.

**Detailed explanation and why it matters.** The New Ideas packets contain operationally useful source and tooling observations, but many of those observations are version-sensitive. Feed status, API behavior, product cadence, license terms, package versions, PMTiles tool support, HTTP Range behavior, CDN caching, DSSE/cosign setup, and external documentation can change. Pass 19 explicitly preserves this as a limitation: current repository/runtime status and current external facts require verification. This idea is categorized as NEEDS VERIFICATION because its substance is not a design preference; it is a standing check required before KFM can safely rely on operational source behavior.

**Dependencies, tensions, and limits.** The idea depends on source descriptors, rights review, package/version lock files, CI probes, and source-ledger updates. The tension is that KFM needs current source facts to operate, but this dossier is based on PDFs and does not perform live external verification. The limitation is inherent: a static source-corpus synthesis cannot certify current external behavior after its boundary.

**Expansion directions and future work.** Future work should create a source-currentness verification backlog with owner, source URL, expected cadence, rights state, last verified date, failure behavior, and release impact. Open questions include how often high-risk sources should be rechecked and how to handle stale source descriptors. Suggested first artifact is a `SourceCurrentnessReport` fixture and validator that can fail closed when rights, version, endpoint, or source-head evidence is missing.


### 6.3 EVD — Evidence, Provenance, Receipts, Identity, and Attestation

#### 6.3.1 Category Overview

EVD is a central category. It is the machinery that lets KFM's truth posture survive contact with maps, APIs, AI, catalogs, domain lanes, and public release. The corpus repeatedly insists that evidence is not a decorative appendix. EvidenceBundle, source ledgers, receipts, proof objects, deterministic hashes, signed attestations, catalog records, release manifests, and citation validation are the structures that make an inspectable claim more than a fluent assertion or a nice-looking layer. EVD therefore sits immediately after source intake in the dependency order: after material enters the governed lifecycle, KFM must be able to say what evidence supports it, how it was transformed, who or what reviewed it, which artifact was released, and how a later correction or rollback can be anchored.

The category is CONFIRMED as a corpus-derived center of gravity. It is strongly supported by [Greenfield Building Plan], [Pipeline Manual], [Governed AI Ledger], [Ollama Ubuntu], [Pass 19], [Master MapLibre Atlas], and [New Ideas 5-10]. The newer operational packets make the evidence problem more concrete by proposing signed PMTiles sidecars, BLAKE3 roots, byte-range manifests, Bao proofs, DSSE/cosign attestations, OCI/ORAS artifact publication, and run receipts. Those implementation mechanisms remain PROPOSED unless verified in a mounted repository, but the underlying doctrine is clear: every consequential public claim needs evidence resolution, and every released artifact needs provenance strong enough to inspect, validate, correct, and roll back.

#### 6.3.2 Subcategories

The first EVD subcategory is EvidenceRef-to-EvidenceBundle resolution: a claim should resolve from reference to bundled source support before API, map, UI, export, or Focus Mode language is released. The second is source-ledger control, where the ledger is an active authority and status surface rather than a bibliography. The third is process memory: RunReceipt, PromotionReceipt, AIReceipt, validation reports, policy decisions, and rollback references explain what happened during intake, transformation, release, and interpretation. The fourth is deterministic identity, including `spec_hash`, source-head data, canonical JSON, content digests, and stable record or artifact IDs. The fifth is artifact attestation, especially for PMTiles, COGs, GeoParquet, and other public map artifacts that require root hashes, sidecars, signatures, and proof references. The sixth is separation discipline: evidence, receipts, proofs, catalogs, releases, and public claims are related objects, not interchangeable names for one file.

#### 6.3.3 Individual Idea Entries

##### KFM-IDX-EVD-001 — EvidenceBundle Outranks Generated Language and Rendered Artifacts

**Status and category.** CONFIRMED. Category: EVD / evidence authority. Source attribution: [Greenfield Building Plan] [Governed AI Ledger] [Ollama Ubuntu] [Pass 19]. Related ideas include KFM-IDX-GOV-001, KFM-IDX-GOV-006, KFM-IDX-MAP-006, and KFM-IDX-INT-007.

**Normalized statement.** EvidenceBundle is the controlling support object for consequential KFM claims; generated language, rendered maps, tiles, graphs, scenes, vector indexes, summaries, and dashboards remain derivative carriers.

**Detailed explanation and why it matters.** This idea is the evidentiary center of the KFM corpus. A map can imply certainty through color and geometry. A dashboard can imply authority through layout. A model answer can imply comprehension through fluent prose. KFM rejects all of those as root truth. EvidenceBundle is the object family that allows a claim to be inspected through source role, source identity, cited support, spatial scope, temporal scope, policy posture, review state, release state, and correction lineage. In that structure, the map and the model answer can be useful, but they must point back to evidence rather than becoming evidence by looking polished.

**Dependencies, tensions, and limits.** This idea depends on GOV truth labels, SRC source descriptors, POL exposure checks, VAL citation and release gates, and MAP/UI surfaces that can show evidence state. The main tension is that users often experience the map or answer first and the evidence second. KFM should resolve that through trust-visible design, not by weakening evidence requirements. The limit in this pass is implementation maturity: the corpus supports the doctrine, but no live EvidenceBundle resolution service or runtime evidence was inspected.

**Expansion directions and future work.** The strongest next artifact is a small EvidenceBundle fixture that can support one public-safe claim across an API payload, an Evidence Drawer display, and a Focus Mode answer. Open questions include whether EvidenceBundle should always be materialized as a stored object or sometimes generated from catalog, proof, and source records at request time.

##### KFM-IDX-EVD-002 — EvidenceRef to EvidenceBundle Resolution

**Status and category.** CONFIRMED. Category: EVD / evidence resolution. Source attribution: [Hydrology] [Hazards] [MapLibre Operating Manual] [Ollama Ubuntu]. Related ideas include KFM-IDX-GOV-006, KFM-IDX-MAP-001, KFM-IDX-MAP-006, KFM-IDX-VAL-007, and KFM-IDX-POL-007.

**Normalized statement.** A consequential KFM response should resolve EvidenceRef to EvidenceBundle before it reaches governed API output, map popups, Evidence Drawer explanations, Focus Mode synthesis, exports, or review surfaces.

**Detailed explanation and why it matters.** EvidenceRef is the pointer; EvidenceBundle is the resolved support. The distinction prevents KFM from treating a reference string, feature ID, URL, tile coordinate, or source name as sufficient evidence. Hydrology, hazards, MapLibre, and Ollama materials all converge on the same flow: a user selects or requests something, the system resolves the relevant evidence, policy and release state are checked, and only then does the public surface answer, abstain, deny, or show bounded context. This matters because the public claim surface is often several steps downstream from canonical data. A clicked feature may be a derived tile; a Focus Mode answer may summarize multiple sources; a hazard popup may involve regulatory, observed, and modeled data. Evidence resolution keeps those carriers from floating free.

**Dependencies, tensions, and limits.** The idea depends on stable feature identity, source role registry, catalog closure, policy decisions, citation validation, and UI payload contracts. Its tension is latency and complexity: resolving evidence at interaction time may be more expensive than rendering a layer. KFM should solve that with cached released EvidenceBundles or carefully scoped bundles, not by bypassing the resolution step. The limitation is that exact DTOs, endpoints, and implementation paths are UNKNOWN here.

**Expansion directions and future work.** Suggested future work is an EvidenceResolutionRecord schema and a no-network fixture showing PASS, ABSTAIN, DENY, and ERROR outcomes. Open questions include how much evidence should be bundled into a lightweight map popup versus a full Evidence Drawer record.

##### KFM-IDX-EVD-003 — Source Ledger as Active Control Surface

**Status and category.** CONFIRMED. Category: EVD / source authority and provenance. Source attribution: [Governed AI Ledger] [Pipeline Manual] [Master MapLibre Atlas]. Related ideas include KFM-IDX-GOV-002, KFM-IDX-SRC-002, KFM-IDX-SRC-008, KFM-IDX-VAL-008, and KFM-IDX-APP-003.

**Normalized statement.** KFM source ledgers should function as active control surfaces that record source identity, authority, status, limitations, and permitted use, not merely as bibliographies.

**Detailed explanation and why it matters.** The corpus repeatedly uses source ledgers to stop authority collapse. A document can be doctrine, lineage, exploratory input, technical reference, operational observation, source candidate, prior-pass baseline, or current-session evidence. Those roles matter. A technical reference may support a method but not prove KFM implementation. A prior no-repo report may preserve a proposed architecture but not prove current files. A New Ideas packet may propose useful watcher thresholds but not verify current endpoint behavior. A source ledger that records these distinctions becomes part of the governance membrane. It tells maintainers what a source can support, what it cannot prove, and what needs verification before use.

**Dependencies, tensions, and limits.** This idea depends on GOV truth labels, SRC source-role registries, POL rights checks, and VAL currentness verification. Its tension is maintenance overhead: ledgers must be updated as sources are accepted, superseded, deprecated, or restricted. The limitation is that ledgers in the PDF corpus may themselves be historical; current external source state still requires fresh verification.

**Expansion directions and future work.** Future work should define a minimal SourceLedgerRecord with authority role, source family, rights state, sensitivity posture, last verification date, verification owner, and current use status. Open questions include how to reconcile document-level source ledgers with machine source descriptors and how to represent sources that support doctrine but not implementation.

##### KFM-IDX-EVD-004 — RunReceipt, PromotionReceipt, and AIReceipt as Process Memory

**Status and category.** CONFIRMED. Category: EVD / receipts and process memory. Source attribution: [Greenfield Building Plan] [Pipeline Manual] [Governed AI Ledger]. Related ideas include KFM-IDX-SRC-004, KFM-IDX-VAL-003, KFM-IDX-VAL-007, KFM-IDX-INT-007, and KFM-IDX-MAP-006.

**Normalized statement.** KFM receipts should record the process by which evidence, artifacts, promotions, and AI responses were produced, checked, denied, released, or rolled back.

**Detailed explanation and why it matters.** Receipts are not the evidence itself; they are process memory. RunReceipt records what a run did, with what inputs, configuration, source heads, hashes, and outcomes. PromotionReceipt records whether a candidate release passed the required gates and what rollback target exists. AIReceipt records model-runtime participation, evidence scope, citation validation, and finite outcome without making model output authoritative. The corpus treats these receipts as necessary because KFM is not only concerned with the final claim. It must be possible to inspect how the claim or artifact came to exist, which controls were applied, and which failure state was chosen when controls failed.

**Dependencies, tensions, and limits.** This idea depends on deterministic identity, validation gates, policy decisions, release manifests, and no-direct-model-client behavior. Its tension is conceptual separation: a receipt can prove that a process ran and what it reported, but it does not by itself prove that the underlying claim is true or safe to publish. The limitation is that specific receipt schemas, signing recipes, and CI jobs remain proposed unless verified in a real checkout.

**Expansion directions and future work.** A first receipt implementation should be deliberately small: a no-network run receipt for a fixture validator, a promotion dry-run receipt, and an AI mock-response receipt. Open questions include how receipts are retained, whether they are public, and which receipts must be signed or included in release proof packs.

##### KFM-IDX-EVD-005 — Deterministic Identity and spec_hash

**Status and category.** CONFIRMED. Category: EVD / deterministic identity. Source attribution: [Greenfield Building Plan] [Pipeline Manual] [New Ideas 5-15]. Related ideas include KFM-IDX-SRC-006, KFM-IDX-VAL-004, KFM-IDX-MAP-004, KFM-IDX-MAP-008, and KFM-IDX-MOD-003.

**Normalized statement.** KFM should use deterministic identity, canonicalized specifications, and stable hashes such as `spec_hash` to make source changes, transformations, validation, and release artifacts reproducible.

**Detailed explanation and why it matters.** Deterministic identity is what lets KFM recognize whether a change is meaningful, reproducible, or safely comparable. The corpus uses `spec_hash` as a control point for watcher events, loop records, PMTiles sidecars, source sidecars, and run receipts. New Ideas 5-15 gives a concrete example: canonical JSON for a county CDL sidecar is hashed after excluding the prior hash value, and that stable hash anchors whether a sidecar state has changed. The broader idea applies across KFM: source descriptors, tile artifacts, release manifests, evidence bundles, and validation reports should not depend on incidental formatting, unordered fields, mutable tags, or unstated tool flags.

**Dependencies, tensions, and limits.** This idea depends on canonicalization rules, field ordering, unit normalization, source-head recording, and stable version identifiers. Its tension is granularity: too coarse a hash hides meaningful change; too fine a hash triggers churn over irrelevant differences. The limitation is that hashing methods vary across proposed packets, with SHA256, BLAKE3, root hashes, and Merkle-style manifests all appearing as candidate mechanisms. Implementation must choose deliberately.

**Expansion directions and future work.** Suggested future work is a canonicalization and hashing profile that distinguishes specification hash, source-head hash, artifact digest, feature identity hash, and receipt hash. Open questions include when canonical JSON is sufficient, when content-addressed artifact storage is needed, and when cryptographic signing is required.

##### KFM-IDX-EVD-006 — Signed Attestations and Provenance References

**Status and category.** PROPOSED. Category: EVD / attestation and provenance. Source attribution: [Greenfield Building Plan] [New Ideas 5-10] [Master MapLibre Atlas]. Related ideas include KFM-IDX-EVD-004, KFM-IDX-EVD-007, KFM-IDX-VAL-005, KFM-IDX-MAP-008, and KFM-IDX-SRC-005.

**Normalized statement.** KFM public artifacts should be accompanied, where significance justifies it, by signed attestations and provenance references that identify what was built, from what inputs, by what process, under what policy, and with what digest.

**Detailed explanation and why it matters.** The Greenfield plan and MapLibre atlas both push KFM toward proof-bearing publication. New Ideas 5-10 turns that pressure into an operational pattern: sidecar predicates, DSSE/cosign signatures, provenance references, run receipt references, tool/license notes, and artifact hashes. The normalized idea is not that every internal draft needs heavy signing. It is that released or consequential artifacts should carry enough attestation for downstream clients, reviewers, and rollback systems to verify that the artifact is the one KFM intended to publish. For map artifacts, this is especially important because a tile archive can be visually persuasive while detached from source evidence.

**Dependencies, tensions, and limits.** This idea depends on artifact digests, source ledger references, receipt references, signature key management, validation gates, and release manifests. The tension is proportionality: overly complex attestation can slow early pilots, while weak attestation undermines auditability. The limitation is that tool choices, signature infrastructure, key trust chains, and library licenses are all NEEDS VERIFICATION before implementation.

**Expansion directions and future work.** A sensible first artifact is a signed predicate for a synthetic PMTiles or GeoParquet fixture, not a production artifact. Open questions include which artifact classes require signatures, how keys are governed, how expired or compromised keys are handled, and whether clients verify signatures directly or rely on server-side release validation.

##### KFM-IDX-EVD-007 — PMTiles Sidecar and Byte-Range Proof Evidence Carrier

**Status and category.** PROPOSED. Category: EVD / artifact proof and map delivery. Source attribution: [New Ideas 5-10] [Master MapLibre Atlas]. Related ideas include KFM-IDX-MAP-004, KFM-IDX-MAP-008, KFM-IDX-VAL-005, KFM-IDX-EVD-006, and KFM-IDX-SRC-005.

**Normalized statement.** PMTiles archives can become verifiable map artifacts when paired with sidecars that record root hashes, target spec hashes, byte-range manifests, range hashes, proof references, provenance, and signatures.

**Detailed explanation and why it matters.** PMTiles are attractive because they allow efficient single-file, HTTP-range-optimized map delivery. The corpus also identifies operational risks: in-place overwrites, cache and Range quirks, native versus web client differences, lack of native atomic patch semantics, and the danger of treating a rendered tile as proof. New Ideas 5-10 proposes a KFM answer: each `.pmtiles` file receives a sidecar with schema version, filename, `spec_hash`, `root_hash`, size, patch/base hash when applicable, byte-range manifest, range hashes, Bao proof references, and build/provenance references. The map artifact becomes not just a file to serve, but a verifiable carrier connected to receipts and release controls.

**Dependencies, tensions, and limits.** This idea depends on deterministic PMTiles builds, byte-range indexing, BLAKE3 or chosen root hashing, Bao or equivalent proof tooling, DSSE/cosign or equivalent signing, and validation gates. Its tension is cost: full byte-range proof coverage may be too much for early work, while sample-only coverage may not support strong client verification. The limitation is that the packet's code and schema are proposed and tool/license facts need verification.

**Expansion directions and future work.** The first implementation should cover a tiny fixture PMTiles archive with a few manifest entries and invalid-case tests. Open questions include whether proof verification belongs in the client, the governed API, CI only, or all three for different release classes.

##### KFM-IDX-EVD-008 — Evidence, Receipts, Proofs, Catalogs, and Claims Stay Separate

**Status and category.** CONFIRMED. Category: EVD / object-family separation. Source attribution: [Greenfield Building Plan] [Pipeline Manual] [Pass 19]. Related ideas include KFM-IDX-GOV-001, KFM-IDX-SRC-005, KFM-IDX-MAP-005, KFM-IDX-VAL-002, and KFM-IDX-POL-008.

**Normalized statement.** KFM must keep evidence, receipts, proof objects, catalog records, release manifests, policy decisions, and public claims as related but distinct object families.

**Detailed explanation and why it matters.** The corpus repeatedly warns against collapsing carriers and controls. Evidence supports a claim. A receipt records process. A proof object verifies integrity or provenance. A catalog record describes assets and distributions. A release manifest identifies a published set. A policy decision controls exposure. A public claim states something to a user. These objects should be linked, but they must not be treated as aliases. If a receipt becomes evidence, process success can be mistaken for truth. If a catalog record becomes a release decision, metadata completeness can be mistaken for publication approval. If a tile becomes a claim, rendering can be mistaken for authority.

**Dependencies, tensions, and limits.** This idea depends on a clear object model, contracts or schemas, validators, and review practices. Its main tension is simplicity: combining objects can look efficient during prototyping. KFM doctrine favors inspectability and reversibility over convenient collapse. The limitation is that the exact implementation structure remains unknown, and object boundaries must be adapted to actual repo conventions when available.

**Expansion directions and future work.** Suggested future work is an object-family map showing which objects can reference each other and which cannot substitute for each other. Open questions include how to expose this separation to users without overwhelming them, and how to prevent implementation shortcuts from merging proof, catalog, and release authority.

### 6.4 MOD — Representation, Spatial-Temporal Modeling, and Domain Semantics

#### 6.4.1 Category Overview

MOD is a central-supporting category. It is central because KFM is map-first and time-aware; it is supporting because representation and modeling decisions must serve evidence, policy, validation, and publication rather than becoming independent authority. The technical references in the corpus make one point with unusual consistency: geographic information, maps, temporal databases, 3D GIS, domain models, and analytical SQL are constructed forms of representation. They help people understand the world, but they also simplify, omit, transform, classify, symbolize, aggregate, and interpret. KFM therefore cannot treat a layer, geometry, date column, parcel, taxon, route, indicator, model output, or 3D scene as self-explanatory.

The category is supported by [GIS Primer], [Temporal SQL], [DDD Reference], [Advanced SQL], [Archaeological 3D GIS], [ArcGIS Environmental], [Urban GIS], and the KFM domain blueprints. MOD normalizes the semantic commitments that evidence and public claims depend on: scale, CRS, projection, precision, raster/vector/network/field model, temporal meaning, valid versus transaction time, bounded context, source role, assertion type, observed/modelled/regulatory/interpretive knowledge character, and 2.5D versus full 3D representation. Its practical purpose is to keep KFM from publishing flattened labels where assertion-bound, time-aware, source-role-aware objects are required.

#### 6.4.2 Subcategories

The first MOD subcategory is cartographic and geographic representation: maps and GIS layers are purpose-built representations, not the world itself. The second is scale, CRS, projection, symbol, precision, and fitness-for-use. The third is spatial model choice: raster, vector, network, field, topology, remote-sensing surface, 2.5D model, and 3D model. The fourth is temporal modeling: valid time, observed time, source time, retrieval time, release time, correction time, transaction time, and bitemporal views. The fifth is domain semantics and bounded context, using published language so hydrology, fauna, land ownership, archaeology, hazards, and infrastructure do not collapse into generic features. The sixth is assertion discipline: records should state what is claimed and from which source role, not silently convert evidence, hypotheses, labels, and interpretations into canonical truth.

#### 6.4.3 Individual Idea Entries

##### KFM-IDX-MOD-001 — Maps and GIS Layers as Representations Rather Than the World

**Status and category.** CONFIRMED. Category: MOD / geographic representation. Source attribution: [GIS Primer] [Pass 18]. Related ideas include KFM-IDX-GOV-001, KFM-IDX-EVD-001, KFM-IDX-MAP-003, KFM-IDX-INT-001, and KFM-IDX-POL-001.

**Normalized statement.** KFM should treat maps and GIS layers as representations that make choices, omissions, simplifications, exaggerations, and conventions visible enough for users to understand what a layer can and cannot claim.

**Detailed explanation and why it matters.** The GIS reference corpus is explicit that a map is not a window onto the world. It is a constructed communication surface that selects features, chooses symbols, imposes scale, transforms locations, and communicates a purpose. Pass 18 translates this into KFM doctrine by treating representation as a governed claim surface. This matters because KFM's public users will often encounter a claim visually: a flood zone, a corridor, a habitat patch, a rare-species generalization, a geologic unit, or a historic overlay. If the layer hides representational choices, users may over-read its precision or authority.

**Dependencies, tensions, and limits.** This idea depends on source attribution, EvidenceBundle resolution, layer manifests, fit-for-use metadata, and UI states that can show uncertainty and limitations. The tension is that map clarity often requires simplification, while evidence integrity requires acknowledging what was simplified. The limit is that KFM cannot make every representational choice visible in the main map view; it needs layered disclosure through legends, Evidence Drawer content, and review metadata.

**Expansion directions and future work.** Future work should define a representation metadata profile for public layers: purpose, audience, scale range, source role, geometry type, symbol meaning, precision, temporal scope, and limitations. Open questions include how to prevent visually simple maps from implying more certainty than the evidence supports.

##### KFM-IDX-MOD-002 — Scale, CRS, Projection, Symbol, and Fitness-for-Use Decisions

**Status and category.** CONFIRMED. Category: MOD / spatial reference and map fitness. Source attribution: [GIS Primer] [MapLibre Operating Manual]. Related ideas include KFM-IDX-MAP-003, KFM-IDX-MAP-005, KFM-IDX-VAL-006, KFM-IDX-EVD-005, and KFM-IDX-INT-001.

**Normalized statement.** KFM should treat scale, coordinate reference systems, projections, symbols, precision, and fitness-for-use as explicit metadata and validation concerns rather than hidden renderer assumptions.

**Detailed explanation and why it matters.** The GIS Primer emphasizes that coordinate systems, projections, symbols, color, and scale affect communication and analysis. The MapLibre operating materials reinforce that the renderer is downstream of trust and should not silently become the place where meaning is invented. In KFM, a geometry's apparent precision can exceed its evidence. A symbol may imply a categorical certainty that is only a model classification. A projected or simplified geometry may be suitable for statewide visualization but not parcel-scale interpretation. Fitness-for-use language is the bridge between a useful map and an honest claim.

**Dependencies, tensions, and limits.** This idea depends on layer manifests, source descriptors, catalog metadata, geometry simplification records, scale-dependent styling, and validation checks for CRS and precision. Its tension is that users often ask practical questions without knowing what scale or projection they are depending on. KFM should expose constraints at the point of use without making maps unreadable. The limitation is that technical details can become overwhelming unless organized into clear layer metadata and Evidence Drawer sections.

**Expansion directions and future work.** Suggested future work is a fitness-for-use acceptance checklist for each public layer class. Open questions include whether KFM should deny certain operations, such as fine-scale measurement or parcel-like interpretation, when a layer's source scale or geometry generalization does not support them.

##### KFM-IDX-MOD-003 — Valid, Source, Retrieval, Release, and Correction Time Separation

**Status and category.** CONFIRMED. Category: MOD / temporal semantics. Source attribution: [Temporal SQL] [Greenfield Building Plan] [Pipeline Manual]. Related ideas include KFM-IDX-EVD-004, KFM-IDX-SRC-006, KFM-IDX-VAL-003, KFM-IDX-MAP-005, and KFM-IDX-APP-004.

**Normalized statement.** KFM should keep materially different temporal dimensions distinct, including valid time, observed time, source time, retrieval time, release time, correction time, and where needed transaction time.

**Detailed explanation and why it matters.** Temporal SQL materials warn that time-varying data are not handled safely by adding an ordinary date column. KFM's corpus extends that warning across source intake, publication, correction, rollback, and public interpretation. A soil observation's observed time is not the same as the time the source was retrieved. A hazard warning's issue time is not the same as its expiry or KFM release time. A historic land assertion's valid time may differ from the archive record date. A correction time records when KFM changed a prior claim, not when the underlying event occurred. If these are collapsed, reports can become inconsistent, stale data can look current, and rollback can become ambiguous.

**Dependencies, tensions, and limits.** This idea depends on schemas that name temporal fields precisely, validators for missing or conflicting time values, source descriptors with update cadence, and UI labels for stale or corrected material. The tension is complexity: multiple time fields can feel heavy for simple records. The limitation is that not every domain requires every temporal dimension, but KFM should define which dimensions are material per lane.

**Expansion directions and future work.** Future work should create a temporal-support matrix by domain and object family. Open questions include which public payloads must show release time, source time, and correction time, and when internal transaction time is sufficient for audit but not public display.

##### KFM-IDX-MOD-004 — Bitemporal and Time-Oriented State Modeling

**Status and category.** CONFIRMED. Category: MOD / time-oriented database design. Source attribution: [Temporal SQL] [Implementation Reference]. Related ideas include KFM-IDX-MOD-003, KFM-IDX-APP-008, KFM-IDX-VAL-006, KFM-IDX-SRC-004, and KFM-IDX-EVD-008.

**Normalized statement.** KFM should use time-oriented and, where necessary, bitemporal modeling for observations, releases, corrections, geography versions, crosswalks, and historical analytical panels.

**Detailed explanation and why it matters.** The Temporal SQL reference describes valid-time, transaction-time, and bitemporal tables, along with the complications they introduce for keys, constraints, queries, modifications, and reporting. The Implementation Reference translates this into KFM's frontier-demography and economy direction: county-year panels, geography versions, population observations, economic observations, agriculture observations, access observations, stable crosswalks, and uncertainty classes. A bitemporal posture matters because KFM often needs to ask two questions at once: what was true or claimed for a historical period, and what did KFM know, publish, correct, or supersede at a later time?

**Dependencies, tensions, and limits.** This idea depends on temporal keys, non-overlap constraints, versioned geography, release manifests, and correction lineage. The tension is that bitemporal design can be heavier than early pilots need. KFM should apply it where consequences justify it, especially public release, historical reconstruction, and corrected claims. The limitation is that this pass does not inspect actual database schema or migration files.

**Expansion directions and future work.** A practical first artifact is a small temporal fixture for a county-year frontier panel or hydrology observation history, with examples of current-state, prior-state, and corrected-state queries. Open questions include how to represent uncertain historical periods and how to align geometry versioning with observation validity.

##### KFM-IDX-MOD-005 — Bounded Contexts and Ubiquitous Language for Domain Lanes

**Status and category.** PROPOSED. Category: MOD / domain semantics. Source attribution: [DDD Reference] [Implementation Reference]. Related ideas include KFM-IDX-GOV-003, KFM-IDX-SRC-002, KFM-IDX-POL-008, KFM-IDX-APP-006, and KFM-IDX-APP-007.

**Normalized statement.** KFM domain lanes should be modeled as bounded contexts with explicit published language, source-role registries, and anticorruption boundaries for external sources.

**Detailed explanation and why it matters.** The DDD reference provides a vocabulary for keeping domain meaning stable: domain, model, ubiquitous language, bounded context, published language, context map, anticorruption layer, responsibility layers, and knowledge level. KFM needs this because its domain lanes use words that can be deceptively similar across sources. A settlement, census place, municipality, townsite, mission, fort, and infrastructure node are not interchangeable. A rail alignment is not an operator. An assessor row is not title truth. A taxonomic occurrence is not legal conservation status. A regulatory flood zone is not observed inundation. Bounded contexts help KFM preserve these distinctions and publish language that reviewers, implementers, and users can inspect.

**Dependencies, tensions, and limits.** This idea depends on source-role registries, schema names, domain documentation, API resource modeling, and review practices. The tension is that domain boundaries can fragment the system if they are too isolated. KFM should use shared governance objects while keeping domain semantics precise. The limitation is that applying DDD to KFM is a synthesis direction, not a confirmed implementation.

**Expansion directions and future work.** Future work should produce a context map for the major domain lanes and shared governance objects. Open questions include which terms should be globally shared and which should remain lane-specific published language.

##### KFM-IDX-MOD-006 — Assertion-First Domain Records Over Flattened Labels

**Status and category.** PROPOSED. Category: MOD / assertion modeling. Source attribution: [People DNA Land] [Archaeology Plan] [Implementation Reference]. Related ideas include KFM-IDX-POL-003, KFM-IDX-POL-004, KFM-IDX-APP-007, KFM-IDX-EVD-002, and KFM-IDX-GOV-001.

**Normalized statement.** Sensitive and historically complex KFM domains should model assertions with evidence, source role, temporal scope, confidence, and review state rather than flattening them into labels on maps or canonical records.

**Detailed explanation and why it matters.** The People/Genealogy-DNA/Land blueprint is explicit: person assertions stay separate from canonical person records; relationship hypotheses remain hypotheses; assessor and tax records are not title truth; parcel geometry is not title boundary proof. The Archaeology plan similarly warns that remote-sensing anomalies, 3D models, and interpreted features are not confirmed sites without review. The Implementation Reference extends the same principle to frontier analytical records. The normalized idea is assertion-first modeling. A record should say what is being asserted, by whom or by which source, under what evidence and temporal scope, with what confidence and policy posture.

**Dependencies, tensions, and limits.** This idea depends on EvidenceBundle links, source-role registries, policy profiles, temporal modeling, and review surfaces. Its tension is user expectation: public users may want simple labels such as owner, site, road, or settlement. KFM should provide clear summaries only after preserving assertion structure internally. The limitation is that exact assertion schema shapes remain proposed.

**Expansion directions and future work.** Suggested future work is a generic AssertionRecord pattern tested in one sensitive lane and one non-sensitive lane. Open questions include how to express confidence without overstating probability and how to display competing assertions in the Evidence Drawer.

##### KFM-IDX-MOD-007 — Raster, Vector, Network, Field, 2.5D, and 3D Distinctions

**Status and category.** CONFIRMED. Category: MOD / spatial data models and dimensionality. Source attribution: [GIS Primer] [Archaeological 3D GIS] [ArcGIS Environmental]. Related ideas include KFM-IDX-MAP-004, KFM-IDX-INT-004, KFM-IDX-INT-005, KFM-IDX-POL-004, and KFM-IDX-APP-005.

**Normalized statement.** KFM should distinguish raster, vector, network, field, remote-sensing surface, 2.5D, full 3D, and volumetric representations because they support different claims and different risks.

**Detailed explanation and why it matters.** The GIS Primer covers core spatial data models and transformations. ArcGIS environmental materials demonstrate practical uses across hazards, social vulnerability, field data, water resources, and climate scenarios. Archaeological 3D GIS adds an especially important distinction: 2.5D and full 3D are not interchangeable. A 2.5D surface may not represent vertical faces or multiple elevations at the same x/y position; a full 3D model can support visibility, volume, stratigraphic, or excavation questions that a 2D or 2.5D layer cannot. In KFM, these choices affect evidence claims, public safety, sensitivity, storage, rendering, and validation.

**Dependencies, tensions, and limits.** This idea depends on source descriptors, acquisition metadata, model type labels, accuracy and scale statements, rendering boundaries, and policy controls. The tension is that 3D or high-resolution remote sensing can look more authoritative than it is. KFM must label acquisition-derived geometry, interpreted reconstruction, modeled surface, and public-safe generalized output separately. The limitation is that 3D runtime and storage choices are conditional and not verified in this pass.

**Expansion directions and future work.** Future work should define model-type metadata for 2D, 2.5D, 3D, and volumetric artifacts. Open questions include when 3D evidence should be public, restricted, generalized, or withheld because of archaeology, infrastructure, or sensitive-resource risk.

##### KFM-IDX-MOD-008 — Knowledge-Character Labels for Observed, Modeled, Regulatory, and Interpretive Data

**Status and category.** CONFIRMED. Category: MOD / epistemic labeling. Source attribution: [Atmosphere Air] [Hazards] [Pass 19]. Related ideas include KFM-IDX-POL-007, KFM-IDX-INT-001, KFM-IDX-APP-005, KFM-IDX-VAL-002, and KFM-IDX-MAP-006.

**Normalized statement.** KFM should label the knowledge character of each layer, record, indicator, or claim, distinguishing observed, modeled, regulatory, administrative, operational, derived, candidate, and interpretive material.

**Detailed explanation and why it matters.** Atmosphere and hazards materials make this idea especially clear. Air observations, public AQI reports, regulatory archives, model fields, smoke masks, anomaly surfaces, remote-sensing detections, disaster declarations, regulatory flood areas, operational warnings, and resilience summaries are not epistemically interchangeable. Pass 19 preserves this as a corpus-wide control. A regulatory flood zone can support a regulatory-context claim but not an observed-flood claim. A remote-sensing fire detection can support a candidate operational-context claim but not a field-confirmed event by itself. A modeled air-quality surface can support modeled context but not official health guidance unless the source role and policy allow it.

**Dependencies, tensions, and limits.** This idea depends on source roles, domain models, policy profiles, Evidence Drawer labels, and validators that prevent unsupported role substitution. The tension is that public maps often blend observed and modeled layers for usability. KFM should allow overlays but keep knowledge character visible and enforceable. The limitation is that each domain needs its own controlled label set.

**Expansion directions and future work.** Future work should define a cross-domain knowledge-character vocabulary with domain-specific extensions. Open questions include how to display mixed-character claims and how to route ambiguous material into ABSTAIN, DENY, or candidate review states.

### 6.5 POL — Policy, Rights, Sensitivity, and Public Safety

#### 6.5.1 Category Overview

POL is a central constraint category. It decides when evidence may be exposed, generalized, delayed, restricted, denied, or routed for steward review. The corpus is unusually consistent on this point: KFM is not merely an evidence system; it is a policy-aware evidence and publication system. A claim can be well sourced and still unsafe or inappropriate for public release. A location can be accurate and still require redaction. A source can be useful and still carry terms, consent limits, cultural review requirements, or living-person restrictions. A hazard layer can be informative and still not be an emergency alert system [Directory Rules] [Archaeology Plan] [Fauna] [People DNA Land] [Hazards].

POL is CONFIRMED as corpus-derived because nearly every domain lane contains a form of fail-closed exposure control. Archaeology denies exact site locations by default. Fauna and flora reports protect sensitive species locations and require geoprivacy transforms. People/genealogy/DNA/land materials restrict living-person and DNA-derived outputs. Settlements and roads reports highlight critical infrastructure and mobility-corridor exposure risks. Agriculture, atmosphere, soil, hydrology, and New Ideas packets emphasize source rights, consent, API keys, usage terms, and currentness checks. Hazards doctrine sharply separates KFM resilience and context support from life-safety alerting [New Ideas 5-8] [Settlements Infrastructure] [Roads Rail Trade].

The governing tension is that public value often comes from specificity, but public harm can also come from specificity. KFM therefore treats public exposure as a governed state, not an automatic reward for data quality. When rights, sovereignty, cultural sensitivity, living-person data, DNA/genomic data, rare species, archaeology, critical infrastructure, or precise risk locations are unclear, the corpus favors quarantine, redaction, generalization, staged access, delayed publication, denial, or abstention.

#### 6.5.2 Subcategories

The first POL subcategory is rights, license, source terms, attribution, API-key, and consent review. The second is sensitive exact-location control for archaeology, rare species, cultural sites, infrastructure, and other public-safety contexts. The third is living-person, genealogy, DNA, genomics, and land-ownership restriction posture. The fourth is cultural, Indigenous, steward, landowner, and archaeological review. The fifth is geoprivacy, redaction, generalization, delayed release, transform receipts, and public-safe derivatives. The sixth is hazards and life-safety boundary control. The seventh is domain policy profiles and finite access outcomes: ALLOW, DENY, ABSTAIN, ERROR, staged access, and role-limited exposure.

#### 6.5.3 Individual Idea Entries

##### KFM-IDX-POL-001 — Deny-by-Default for Sensitive Exact Locations

**Status and category.** CONFIRMED. Category: POL / sensitive exact-location controls. Source attribution: [Archaeology Plan] [Fauna] [Flora] [Directory Rules]. Related ideas include KFM-IDX-GOV-006, KFM-IDX-MOD-002, KFM-IDX-POL-004, KFM-IDX-POL-005, and KFM-IDX-MAP-005.

**Normalized statement.** KFM should deny public exact-location exposure by default for sensitive archaeological, biological, cultural, infrastructure, and other high-risk location classes unless evidence, rights, policy, review, and release controls explicitly allow a public-safe form.

**Detailed explanation and why it matters.** Exact coordinates can be a harm vector. The archaeology lane treats public exact site locations as denied by default because of looting risk, cultural sensitivity, private landowner privacy, burial or sacred-site concerns, and steward permissions. Fauna and flora lanes treat sensitive occurrence geometry similarly because nests, dens, roosts, hibernacula, rare plants, and protected species can be harmed by exposure. Infrastructure and transport lanes add another class of risk where exact facility, restriction, or dependency mapping may require staged access. This idea is not anti-map; it is a rule that the public map must be safe for the consequence of the domain.

**Dependencies, tensions, and limits.** The idea depends on sensitivity classifiers, source roles, steward review, policy decisions, geoprivacy transforms, release manifests, and Evidence Drawer payloads that can explain redaction without leaking the withheld location. The tension is that exactness is often valuable for researchers and reviewers. KFM can support restricted access, generalized displays, or steward-only review, but those are separate from ordinary public exposure. The limitation is that sensitivity rules can change by jurisdiction, source terms, species, site type, or steward agreement.

**Expansion directions and future work.** Future work should define a sensitive-location policy profile with required fields for sensitivity basis, public geometry class, allowed access role, transform receipt, review state, and rollback target. A first validation fixture should prove that an exact sensitive point is denied while a generalized or suppressed public-safe derivative can proceed after review.

##### KFM-IDX-POL-002 — Rights and License Verification Gate

**Status and category.** CONFIRMED. Category: POL / rights, source terms, license, and consent. Source attribution: [Directory Rules] [Agriculture] [Atmosphere Air] [New Ideas 5-8]. Related ideas include KFM-IDX-SRC-002, KFM-IDX-SRC-008, KFM-IDX-EVD-003, KFM-IDX-VAL-008, and KFM-IDX-APP-003.

**Normalized statement.** KFM should fail closed when source rights, license terms, usage restrictions, attribution duties, API-key conditions, or consent requirements are unclear or missing.

**Detailed explanation and why it matters.** The corpus repeatedly warns that availability is not permission. A dataset may be downloadable but still require attribution, written consent, API-key terms, rate limits, redistribution limits, or special release treatment. New Ideas 5-8 explicitly treats AirNow as API-key gated and Mesonet ingest as requiring posted usage-policy awareness and written consent before ingestion. Agriculture and atmosphere materials emphasize source terms, current rights, quotas, endpoint behavior, and public-release posture. Directory doctrine reinforces that source identity, rights, sensitivity, and admissibility belong to registry and policy control, not to ad hoc data use.

**Dependencies, tensions, and limits.** This idea depends on SourceDescriptor fields, rights registries, source currentness checks, policy gates, source-ledger caveats, and release validators. The tension is operational convenience: source watchers and proof slices are easier to build if rights are treated as a note rather than a gate. KFM rejects that shortcut. The limitation is that static PDFs cannot certify current rights or endpoint terms, so many source-specific rights claims remain NEEDS VERIFICATION before activation.

**Expansion directions and future work.** Future work should create a `RightsReviewRecord` or rights section within SourceDescriptor with license text or reference, attribution requirement, redistribution status, API/key condition, consent state, last verified date, and public-release effect. A validator should deny promotion when public release is requested with `rights_status` UNKNOWN or NOASSERTION.

##### KFM-IDX-POL-003 — Living-Person, DNA, and Genomic Restriction Posture

**Status and category.** CONFIRMED. Category: POL / living-person and DNA restrictions. Source attribution: [People DNA Land]. Related ideas include KFM-IDX-MOD-006, KFM-IDX-POL-002, KFM-IDX-POL-004, KFM-IDX-APP-007, and KFM-IDX-INT-007.

**Normalized statement.** KFM should restrict living-person, DNA, genomic, and DNA-derived relationship or identity outputs by default, treating them as high-sensitivity assertions rather than ordinary public knowledge.

**Detailed explanation and why it matters.** The people/genealogy/DNA/land lane is one of the clearest examples of evidence being insufficient for publication by itself. A relationship hypothesis, DNA match, lineage inference, person assertion, or land-ownership statement can affect privacy, family identity, living persons, legal interests, and cultural sensitivity. The corpus therefore proposes assertion-first handling, separate person assertions from canonical person records, DNA restricted by default, and evidence-bound relationship hypotheses. It also warns that assessor or tax records are not title truth and parcel geometry is not title boundary proof unless the source role and evidence support that claim.

**Dependencies, tensions, and limits.** This idea depends on identity resolution controls, person/living-status treatment, consent posture, evidence-role classification, policy profiles, review state, and abstention rules. The tension is that genealogy and land history are valuable public research domains, but DNA and living-person information have higher consequence than ordinary historical place names. KFM should support historical research where evidence and release controls allow it while denying or restricting living-person and DNA-derived outputs. The limitation is that this pass does not define jurisdiction-specific privacy law or production policy; those require later legal and steward review.

**Expansion directions and future work.** Future work should define a policy profile for person assertions with fields for living-person risk, DNA/genomic derivation, consent, relationship confidence, source role, public exposure class, and review authority. A first fixture should show ABSTAIN or DENY when a Focus Mode prompt asks for living-person DNA-derived identity or relationship assertions without authorized evidence and access.

##### KFM-IDX-POL-004 — Cultural, Archaeological, and Steward Review Controls

**Status and category.** CONFIRMED. Category: POL / cultural and steward review. Source attribution: [Archaeology Plan] [Roads Rail Trade] [People DNA Land]. Related ideas include KFM-IDX-POL-001, KFM-IDX-POL-003, KFM-IDX-MOD-006, KFM-IDX-APP-006, and KFM-IDX-APP-007.

**Normalized statement.** KFM should require cultural, archaeological, Indigenous, steward, or landowner review where source material, geometry, names, routes, sites, or assertions carry cultural sensitivity or controlled-access obligations.

**Detailed explanation and why it matters.** The corpus does not treat cultural sensitivity as a cosmetic disclaimer. Archaeological site data, burial or sacred-site information, oral history, treaty context, Indigenous mobility corridors, culturally significant routes, land histories, private landowner contexts, and person/genealogy assertions may require review by appropriate stewards before public exposure. Roads/rail/trade materials warn against converting oral-history, treaty, cultural, or interpretive evidence into falsely precise public geometry. Archaeology materials deny exact public locations by default and treat remote-sensing anomalies as candidate features until evidence and review support a stronger claim. People/DNA/land materials add privacy and land-interest sensitivity.

**Dependencies, tensions, and limits.** This idea depends on steward registries, review records, access roles, sensitivity labels, transform receipts, and release gates. The tension is that steward review can slow publication, but bypassing it would undermine KFM's trust posture and can create real harm. The limitation is that the attached corpus does not identify actual steward agreements, tribal review protocols, or landowner permissions; those remain UNKNOWN and must be verified before operational release.

**Expansion directions and future work.** Future work should define a `StewardReviewRecord` with reviewer role, review scope, allowed public geometry class, allowed narrative scope, expiry or revisit date, and correction path. Another useful artifact is a route/site geometry generalization rule that preserves interpretive value while preventing false precision and sensitive disclosure.

##### KFM-IDX-POL-005 — Rare Species Geoprivacy and Transform Receipts

**Status and category.** CONFIRMED. Category: POL / geoprivacy and public-safe biological derivatives. Source attribution: [Fauna] [Flora] [Habitat Fauna Thin Slice]. Related ideas include KFM-IDX-POL-001, KFM-IDX-EVD-004, KFM-IDX-VAL-002, KFM-IDX-APP-002, and KFM-IDX-MAP-005.

**Normalized statement.** KFM should protect rare species and sensitive biological occurrences through geoprivacy transforms, public-safe derivatives, and transform receipts before public map or API exposure.

**Detailed explanation and why it matters.** Fauna and flora reports converge on a public-safety rule: exact occurrence geometry for sensitive taxa can expose protected species and habitats to harm. Public value can still be delivered through generalized range maps, habitat summaries, suitability surfaces, redacted occurrence-derived products, or public-safe assignment explanations. The habitat-fauna thin slice is especially important because it aims to prove one published fauna occurrence habitat assignment while preserving evidence, policy, release manifest, layer manifest, Evidence Drawer payload, and Focus Mode behavior. The transform receipt is the object that records how sensitive source geometry became a public-safe representation.

**Dependencies, tensions, and limits.** This idea depends on taxonomic identity, legal/conservation status, occurrence evidence, sensitivity classification, transform rules, release manifests, and policy validators. The tension is that scientific detail can require precision while public release may require generalization or suppression. KFM should not erase precision inside governed review contexts, but it should not expose that precision publicly when risk is high. The limitation is that species sensitivity and legal status require current verification and steward input.

**Expansion directions and future work.** Future work should define geoprivacy transform types such as suppress, generalize to grid, generalize to watershed or county, buffer, jitter only with constraints, delayed publication, or steward-only exact access. Each transform should emit a receipt stating input class, output class, reason, policy, reviewer, and residual risk.

##### KFM-IDX-POL-006 — Critical Infrastructure and Public-Safety Exposure Controls

**Status and category.** CONFIRMED. Category: POL / infrastructure and public-safety controls. Source attribution: [Settlements Infrastructure] [Roads Rail Trade] [Hazards]. Related ideas include KFM-IDX-POL-001, KFM-IDX-POL-007, KFM-IDX-MOD-008, KFM-IDX-APP-006, and KFM-IDX-MAP-003.

**Normalized statement.** KFM should restrict, generalize, or stage exposure of critical infrastructure, transport facilities, dependencies, restrictions, and public-safety-sensitive details when precise release could create risk.

**Detailed explanation and why it matters.** Built-environment and mobility lanes expand KFM beyond environmental and historical data into systems with operational consequence. Roads, rail, depots, yards, crossings, bridges, facilities, infrastructure dependencies, service areas, condition observations, and restrictions may be important for resilience and planning, but not every precise detail belongs on a public map. Hazards materials add another public-safety boundary: KFM can support analysis, history, regulatory context, operational context, and resilience review, but it must not become an emergency alert system or expose sensitive operational details without review. Settlements/infrastructure materials similarly separate assets, networks, facilities, operators, conditions, and public-safe representations.

**Dependencies, tensions, and limits.** This idea depends on infrastructure sensitivity labels, source roles, access profiles, review states, and public-safe layer manifests. The tension is that infrastructure transparency can support planning and accountability, while excessive precision can create security or misuse risk. KFM should aim for staged access and appropriate generalization rather than blanket invisibility. The limitation is that critical-infrastructure policy must be refined with actual sources, legal requirements, and steward review.

**Expansion directions and future work.** Future work should define infrastructure exposure classes: public generalized, public exact allowed, restricted exact, steward-only, and denied. A first validator should deny public publication when a layer marks infrastructure sensitivity but lacks exposure class, reviewer, and transform receipt.

##### KFM-IDX-POL-007 — Hazards Boundary: KFM Is Not an Emergency Alert System

**Status and category.** CONFIRMED. Category: POL / hazards and life-safety limits. Source attribution: [Hazards] [ArcGIS Environmental]. Related ideas include KFM-IDX-MOD-008, KFM-IDX-SRC-006, KFM-IDX-VAL-007, KFM-IDX-INT-008, and KFM-IDX-APP-005.

**Normalized statement.** KFM may provide hazard history, regulatory context, observations, resilience analysis, and evidence-backed summaries, but it must not operate as an emergency alert or life-safety instruction system.

**Detailed explanation and why it matters.** The hazards lane is high value precisely because hazards are consequential. The ArcGIS environmental reference demonstrates how GIS can analyze flood hazard areas, hurricanes, wildfires, vulnerability, volcanic hazards, and climate scenarios. KFM can adapt such methods for evidence-backed historical and planning support. The Hazards blueprint, however, defines a firm boundary: operational warning feeds are contextual, freshness-bound, and not-for-life-safety. KFM should point users to official alert systems and guidance when they seek emergency action. It should not imply that a KFM map, Focus Mode answer, or watcher decision is an authoritative warning or instruction.

**Dependencies, tensions, and limits.** This idea depends on hazard source-role labels, freshness status, expiry times, disclaimers, EvidenceBundle resolution, finite outcomes, and UI warnings. The tension is that users may ask urgent hazard questions, and KFM may have relevant context. KFM can answer with bounded evidence and direct users to official sources, or it can abstain or deny life-safety guidance. The limitation is that operational feeds and official alert source behavior are version-sensitive and require current verification before use.

**Expansion directions and future work.** Future work should define a hazards response envelope that includes `not_emergency_alert_system`, source freshness, official-source referral, and finite outcome. A validation fixture should reject hazard outputs that omit expiry, freshness, source, and the life-safety boundary when operational context is involved.

##### KFM-IDX-POL-008 — Domain Policy Profiles and Access Roles

**Status and category.** PROPOSED. Category: POL / domain policy profiles and access control. Source attribution: [Directory Rules] [Hydrology] [Soil] [Agriculture]. Related ideas include KFM-IDX-POL-001, KFM-IDX-POL-002, KFM-IDX-VAL-002, KFM-IDX-MAP-001, and KFM-IDX-APP-001.

**Normalized statement.** KFM should define domain policy profiles and access roles that translate general doctrine into domain-specific release, redaction, review, and denial behavior.

**Detailed explanation and why it matters.** The corpus supplies shared policy doctrine, but each domain needs specific controls. Hydrology has regulatory flood context, observed water data, terrain-derived context, and public safety implications. Soil and agriculture have source terms, landcover change, Mesonet consent, crop/field-level sensitivity, and material-change watchers. Habitat, fauna, flora, archaeology, people/DNA/land, roads, settlements, hazards, and atmosphere each carry different combinations of source authority, sensitivity, rights, public consequence, and review needs. A domain policy profile would keep KFM from writing one vague policy for all domains or reinventing policies inconsistently in every lane.

**Dependencies, tensions, and limits.** This idea depends on source descriptors, knowledge-character labels, sensitivity classes, access roles, review states, and validators. The tension is standardization versus domain specificity. Too much standardization hides real differences; too much domain-specific policy creates drift. The limitation is that the corpus supports the need for profiles but does not settle the final policy language, access roles, or enforcement stack.

**Expansion directions and future work.** Future work should create a profile template with domain, source roles, knowledge characters, public-safe classes, restricted classes, required reviews, required receipts, denial conditions, and rollback expectations. Suggested pilot profiles are hydrology proof lane, habitat-fauna, archaeology, people/DNA/land, hazards, and agriculture/CDL/PLANTS watchers.


### 6.6 VAL — Validation, QA, Observability, and Release Discipline

#### 6.6.1 Category Overview

VAL is the category that keeps the corpus from becoming only doctrine and design language. It asks how KFM knows that a source descriptor parses, a sidecar recomputes, a rights gate fails closed, a PMTiles artifact has the expected digest, a watcher event is only proposing work, a model output has citations, a schema path has not drifted, and a public release has a rollback target. The corpus repeatedly treats validation as part of truth rather than a late engineering step. Validation is not merely test coverage; it is the operational expression of KFM's evidence-first, fail-closed, policy-aware posture.

The category is CONFIRMED as a corpus-derived implementation pressure. It is supported by the Greenfield plan's validation and CI gates, the Pipeline manual's query-save-validate-compile-review-promote-recompile loop, the domain blueprints' fixture-first PR sequences, New Ideas 5-8's source-health probes, New Ideas 5-10's PMTiles attestation validator concept, and New Ideas 5-15's material-change watcher gates. VAL also carries the repeated no-mounted-repo boundary: until current repo files, tests, workflows, dashboards, logs, and receipts are inspected, implementation maturity remains UNKNOWN.

VAL sits after GOV, SRC, EVD, MOD, and POL in dependency order. It validates the objects those categories define. It also protects MAP, INT, and APP from premature public exposure. In KFM, a successful validator does not make a claim true by itself, but a failed validator should block release, force quarantine, deny output, or create a verification backlog item. That asymmetry is deliberate.

#### 6.6.2 Subcategories

The first VAL subcategory is no-network fixture-first validation, which proves schema, policy, and receipt behavior before live connectors. The second is fail-closed validator behavior across schema, policy, rights, sensitivity, evidence, catalog, and release gates. The third is CI probes and source-head recording for operational sources. The fourth is material-change validation for sidecars and proposed work records. The fifth is map artifact attestation validation, especially PMTiles sidecars. The sixth is drift detection across schemas, contracts, policies, directories, and documentation. The seventh is finite outcomes and observability records. The eighth is currentness and rights reverification backlog management.

#### 6.6.3 Individual Idea Entries

##### KFM-IDX-VAL-001 — No-Network Fixture-First Validation

**Status and category.** CONFIRMED. Category: VAL / fixture-first proof. Source attribution: [Hydrology] [Pass 19] [Habitat Fauna Thin Slice]. Related ideas include KFM-IDX-SRC-001, KFM-IDX-EVD-002, KFM-IDX-APP-001, and KFM-IDX-APP-002.

**Normalized statement.** KFM should prove new lanes and trust objects with no-network fixtures before activating live connectors, public release, UI binding, or model interpretation.

**Detailed explanation and why it matters.** Many domain reports converge on the same implementation sequence: begin with source registries, schemas, validators, fixtures, policy gates, receipts, and dry-run promotion rather than live harvesting. Hydrology is repeatedly identified as a good proof lane because it can model source roles, observations, regulatory layers, catalog closure, and map delivery without immediately touching the highest sensitivity domains. The habitat-fauna thin slice similarly asks for one controlled public-safe occurrence assignment rather than broad biodiversity ingestion. No-network fixtures let KFM test trust behavior deterministically. They also prevent early source outages, credentials, rights confusion, or endpoint drift from hiding schema and policy defects.

**Dependencies, tensions, and limits.** This idea depends on representative fixture design, schema validators, policy fixtures, and receipt examples. Its tension is realism: fixtures are safe but can be too narrow. KFM should therefore design fixtures to cover positive, negative, denied, abstained, and ambiguous cases. The limitation is that passing fixture tests does not prove operational source behavior.

**Expansion directions and future work.** Future work should define a fixture taxonomy for each thin slice: valid fixture, rights-denied fixture, sensitivity-denied fixture, stale-source fixture, unresolved-EvidenceRef fixture, and rollback fixture. Suggested first artifact is a cross-lane no-network test pack for hydrology, habitat-fauna, PMTiles attestation, and governed AI.

##### KFM-IDX-VAL-002 — Validators Fail Closed on Schema, Policy, Rights, Sensitivity, and Release Violations

**Status and category.** CONFIRMED. Category: VAL / fail-closed gates. Source attribution: [Greenfield Building Plan] [New Ideas 5-10] [Archaeology Plan] [Fauna]. Related ideas include KFM-IDX-POL-001, KFM-IDX-POL-002, KFM-IDX-EVD-008, and KFM-IDX-MAP-008.

**Normalized statement.** KFM validators should fail closed when required schema fields, policy decisions, rights evidence, sensitivity posture, proof objects, or release state are missing or invalid.

**Detailed explanation and why it matters.** The fail-closed posture appears across doctrine and domain reports. Archaeology and fauna deny exact sensitive locations by default. New Ideas 5-10 denies publication when PMTiles sidecars, signatures, root hashes, patch base hashes, or proof references are missing. The Greenfield plan treats publication as a gated state transition. A validator that merely warns while letting public release continue would contradict this posture. Fail-closed validation turns uncertainty into controlled denial, quarantine, abstention, or error rather than public exposure.

**Dependencies, tensions, and limits.** This idea depends on explicit required fields and finite failure outcomes. It also depends on implementers resisting the temptation to bypass gates for convenience. The tension is operational productivity: fail-closed systems can block work when evidence is incomplete. KFM should make failure reasons precise and remediable rather than weakening the gates.

**Expansion directions and future work.** Future work should create a shared `ValidationReport` shape with status, failed gates, reasons, evidence references, remediation hints, and release impact. A useful first artifact is a validator matrix showing which missing fields cause ABSTAIN, DENY, ERROR, QUARANTINE, or NEEDS VERIFICATION.

##### KFM-IDX-VAL-003 — CI Probes with Source Heads and Run Receipts

**Status and category.** PROPOSED. Category: VAL / operational probes and observability. Source attribution: [New Ideas 5-8] [Pipeline Manual]. Related ideas include KFM-IDX-SRC-007, KFM-IDX-EVD-004, KFM-IDX-APP-003, and KFM-IDX-VAL-008.

**Normalized statement.** KFM should use CI probes that record source heads, source response metadata, run receipts, finite decisions, and policy outcomes for operationally watched feeds.

**Detailed explanation and why it matters.** New Ideas 5-8 translates source monitoring into an auditable pattern: HEAD/If-None-Match checks, ETag and Last-Modified capture, recency windows, source-specific probes, policy IDs, source license or contact evidence, and signed run receipts. The Pipeline manual supplies the broader loop architecture. CI probes are not merely uptime checks. They are evidence-producing checks that help determine whether a source has changed, gone stale, violated expectations, or requires proposed work. For KFM, the important point is that source health and tile health become recorded events rather than informal observations.

**Dependencies, tensions, and limits.** This idea depends on source descriptors, rights state, expected cadence, threshold policy, receipts, and CI configuration. It is PROPOSED because the corpus provides the pattern but this pass does not verify any live CI implementation. The tension is that operational probes can themselves become brittle if external services change. KFM should keep probe failures as evidence of a condition to review, not automatic public truth.

**Expansion directions and future work.** Future work should build a no-network mock probe harness before live source checks. The first artifact could be a `SourceProbeReceipt` fixture with SMAP, MAIAC, FIRMS, AirNow, and Mesonet examples marked as simulated, not live.

##### KFM-IDX-VAL-004 — Material-Change Watcher Validation

**Status and category.** PROPOSED. Category: VAL / material-change gates. Source attribution: [New Ideas 5-15] [Agriculture]. Related ideas include KFM-IDX-SRC-006, KFM-IDX-EVD-005, KFM-IDX-APP-004, and KFM-IDX-POL-002.

**Normalized statement.** Material-change watchers should validate sidecars, source heads, thresholds, class histograms, spec_hash recomputation, and outbox records before proposing reprocessing.

**Detailed explanation and why it matters.** New Ideas 5-15 provides a concrete watcher pattern for USDA CDL and PLANTS county packages. The watcher should compare ETag and Last-Modified values, recompute a stable spec_hash from canonical JSON, compare county class histograms, apply relative and absolute materiality thresholds, and emit a PROPOSED work record only when the change matters. Agriculture and soil reports provide the domain motivation: landcover, crop, plant, and soil layers can change, but KFM should avoid noisy reruns and should not publish automatically.

**Dependencies, tensions, and limits.** This idea depends on sidecar schemas, threshold policy, county geometry area, classmap versioning, source rights, and safe outbox handling. It is PROPOSED because implementation and live source checks remain unverified. The tension is threshold choice: a threshold that is too sensitive creates churn; a threshold that is too coarse hides material change. KFM should document thresholds as policy choices, not scientific absolutes.

**Expansion directions and future work.** Future work should create material-change validator fixtures with unchanged, nonmaterial, material, missing-source-head, and bad-spec_hash cases. A first artifact could be a CDL county sidecar schema and a proposed-work-record schema with denial of direct publication.

##### KFM-IDX-VAL-005 — PMTiles Attestation Validator

**Status and category.** PROPOSED. Category: VAL / map artifact integrity validation. Source attribution: [New Ideas 5-10] [Master MapLibre Atlas]. Related ideas include KFM-IDX-EVD-007, KFM-IDX-MAP-004, KFM-IDX-MAP-008, and KFM-IDX-EVD-006.

**Normalized statement.** KFM should validate PMTiles sidecars, root hashes, spec hashes, byte-range manifests, proof references, patch base hashes, signatures, and release references before exposing PMTiles artifacts publicly.

**Detailed explanation and why it matters.** PMTiles gives KFM a practical static map artifact format, but static delivery is not automatically governed delivery. New Ideas 5-10 identifies why validation matters: in-place overwrites, cache and Range quirks, client differences, and missing delta semantics can produce stale or unsafe public maps. A PMTiles attestation validator would check sidecar schema, full-file root hash, range hashes, Bao proof references where present, patch metadata, provenance references, signature state, and whether the artifact appears in release/cataloig records. The Master MapLibre atlas generalizes this into map artifact proof and manifest discipline.

**Dependencies, tensions, and limits.** This idea depends on deterministic PMTiles builds, sidecar generation, proof strategy, validator tooling, release manifests, and client verification expectations. It is PROPOSED because no current validator is confirmed. The tension is implementation depth: exhaustive range proof validation may be heavy for a first pass. KFM can start with schema, root hash, selected range, and release-reference checks.

**Expansion directions and future work.** The first artifact should be a tiny PMTiles sidecar validator with valid and invalid fixtures. Later work can add Bao proof validation, DSSE/cosign verification, OCI referrer checks, and client-side verification examples.

##### KFM-IDX-VAL-006 — Schema, Contract, Policy, and Directory Drift Detection

**Status and category.** CONFIRMED. Category: VAL / drift detection and governance conformance. Source attribution: [Directory Rules] [Pipeline Manual] [Pass 19]. Related ideas include KFM-IDX-GOV-003, KFM-IDX-GOV-005, KFM-IDX-EVD-003, and KFM-IDX-MAP-005.

**Normalized statement.** KFM should detect and record drift across schema homes, contract homes, policy homes, directory placement, source registries, release artifacts, and documentation authority.

**Detailed explanation and why it matters.** Directory Rules states that when the mounted repo conflicts with placement doctrine, the conflict should be recorded in a drift register rather than silently treated as canon. The Pipeline manual and Pass 19 echo the same risk in broader terms: as KFM grows, authority collisions can emerge between docs, contracts, schemas, policies, source registries, proofs, and release objects. Drift detection is therefore a validation category, not only a documentation habit. A repo can pass ordinary tests while still creating a parallel schema home or policy home that weakens governance.

**Dependencies, tensions, and limits.** This idea depends on canonical roots, ADRs, per-root README files, source registries, and current repo scans. Its tension is that actual repo state may legitimately differ from earlier doctrine. KFM should handle that through ADRs and migration notes rather than pretending the conflict does not exist. The limitation is that this pass did not inspect a live repo.

**Expansion directions and future work.** Future work should create a drift-detection checklist that can be run during implementation planning: roots present, schema home, policy home, source registry, proof/receipt/release separation, lifecycle folders, docs authority, and compatibility roots. The first artifact could be a `DRIFT_REGISTER` example entry for schema-home ambiguity.

##### KFM-IDX-VAL-007 — Finite Failure Outcomes and Observability Records

**Status and category.** CONFIRMED. Category: VAL / finite outcomes and observability. Source attribution: [Ollama Ubuntu] [Governed AI Ledger] [New Ideas 5-8]. Related ideas include KFM-IDX-GOV-002, KFM-IDX-EVD-004, KFM-IDX-INT-007, and KFM-IDX-MAP-006.

**Normalized statement.** KFM should use finite outcomes such as ANSWER, ABSTAIN, DENY, and ERROR, with observability records that explain the reason and evidence boundary.

**Detailed explanation and why it matters.** The Ollama and governed-AI reports make finite outcomes central to model integration, but the pattern applies beyond AI. A source probe can fail, a policy can deny, an EvidenceRef can be unresolved, a validator can error, a rights gate can block release, and a public request can abstain. Finite outcomes keep negative states from becoming ambiguous. They also protect the UI: a map popup, Focus Mode response, Evidence Drawer, or review console should show whether a system declined because evidence was missing, policy denied exposure, validation failed, or an internal error occurred.

**Dependencies, tensions, and limits.** This idea depends on structured runtime envelopes, validation reports, receipts, and UI state design. The tension is user experience: negative outcomes can feel frustrating. KFM should treat them as trust-visible safety states rather than hiding them or replacing them with generic text. The limitation is that finite labels must be accompanied by reasons; labels without reason fields become opaque.

**Expansion directions and future work.** Future work should define a shared `OutcomeEnvelope` or align existing envelopes so API, Focus Mode, validators, and watchers use consistent negative states. Suggested first artifact is a set of examples where similar user-facing requests produce ANSWER, ABSTAIN, DENY, and ERROR for different evidence and policy reasons.

##### KFM-IDX-VAL-008 — External Source Currentness and Rights Reverification Backlog

**Status and category.** NEEDS VERIFICATION. Category: VAL / verification backlog. Source attribution: [New Ideas 5-8] [New Ideas 5-10] [New Ideas 5-15] [Pass 19]. Related ideas include KFM-IDX-SRC-008, KFM-IDX-POL-002, KFM-IDX-EVD-003, and KFM-IDX-APP-003.

**Normalized statement.** KFM needs a maintained backlog for rechecking external source currentness, package versions, endpoint behavior, rights, source terms, tool status, and operational assumptions.

**Detailed explanation and why it matters.** The New Ideas packets are rich with operational proposals, but they also show why a static dossier cannot certify current facts. Data platforms, PMTiles tooling, feed status, Earth observation products, MapLibre releases, AirNow keys, Mesonet policy, CDL packages, PLANTS package behavior, and source endpoint metadata can change. Pass 19 explicitly marks implementation and current external facts as unresolved without current checks. A verification backlog turns that uncertainty into managed work rather than hidden risk.

**Dependencies, tensions, and limits.** This idea depends on source ledgers, owner assignments, review cadence, release impact labels, and fail-closed behavior when verification is stale. It is labeled NEEDS VERIFICATION because the backlog items are checkable but not checked in this pass. The tension is workload: currentness checking can become endless. KFM should prioritize by release consequence and source volatility.

**Expansion directions and future work.** Future work should create a `VerificationBacklog` table with item, source, risk, last verified, required evidence, owner, release impact, and next action. The first artifact could focus on five high-signal items: Mesonet consent, PMTiles toolchain version, MapLibre target version, CDL source package status, and AirNow API access terms.


### 6.7 MAP — Governed API, Map Artifacts, UI, and Renderer Boundaries

#### 6.7.1 Category Overview

MAP is a central delivery category. It is where KFM becomes usable as a map-first system, but only after the trust path has already constrained what can be rendered, queried, explained, or interpreted. The category joins four source families: Web API design, MapLibre operating doctrine, Master MapLibre atlas artifact governance, and whole-UI/governed-AI planning. The result is a disciplined boundary: public clients and normal UI surfaces use governed APIs, released artifacts, catalog records, tile services, EvidenceBundle resolution, and release manifests. They do not read RAW, WORK, QUARANTINE, canonical stores, unpublished candidates, direct model output, or unreviewed source feeds.

MAP is CONFIRMED as a corpus-derived category, but many of its implementation details remain PROPOSED or UNKNOWN. The corpus confirms MapLibre's role as a disciplined 2D renderer and interaction runtime, not a truth store. It confirms the importance of Evidence Drawer and Focus Mode as trust-visible surfaces. It confirms that API design should use contracts, resource ontology, HTTP semantics, and developer-readable documentation. It also proposes deeper artifact governance through LayerManifest, StyleManifest, TileArtifactManifest, MapReleaseManifest, PMTiles attestation, STAC/DCAT/PROV mappings, and client-side verification. This chapter normalizes those ideas without claiming that current repo routes or UI components exist.

The key MAP rule is that rendering is downstream of trust. A beautiful map can still be wrong, unsafe, stale, or unsupported. A governed map is not merely a layer stack; it is a claim surface with evidence, policy, validation, release, correction, and rollback state visible enough to support responsible use.

#### 6.7.2 Subcategories

The first MAP subcategory is governed API as trust membrane. The second is resource ontology and HTTP contract design. The third is renderer boundary, with MapLibre as downstream 2D shell. The fourth is map artifact family: PMTiles, COGs, GeoParquet, MVT/MLT, TileJSON, styles, and derived public products. The fifth is manifest discipline: layer, style, tile artifact, and map release manifests. The sixth is Evidence Drawer and Focus Mode as trust-visible UI. The seventh is Story Nodes and review surfaces. The eighth is client or CI verification of released map artifacts.

#### 6.7.3 Individual Idea Entries

##### KFM-IDX-MAP-001 — Governed API as Trust Membrane

**Status and category.** CONFIRMED. Category: MAP / API boundary and trust membrane. Source attribution: [Web APIs] [Whole UI AI] [Governed AI Ledger] [MapLibre Operating Manual]. Related ideas include KFM-IDX-GOV-006, KFM-IDX-EVD-002, KFM-IDX-POL-008, and KFM-IDX-INT-007.

**Normalized statement.** KFM's governed API should act as the trust membrane between public clients and evidence, policy, release, model, map, and catalog systems.

**Detailed explanation and why it matters.** The Web APIs reference frames APIs as contracts between software and developers. KFM extends that concept into governance. The governed API is not merely a data access layer; it is where EvidenceRef resolution, policy posture, release state, review state, finite outcomes, and citation validation can be enforced before a public UI or model surface responds. The Whole UI/AI and MapLibre manuals repeatedly reject direct public access to canonical stores, unpublished candidate data, raw model output, or internal lifecycle directories. A governed API lets KFM provide useful public behavior while preserving the trust membrane.

**Dependencies, tensions, and limits.** This idea depends on contracts, DTOs, evidence resolution, policy checks, release manifests, and negative outcomes. The tension is developer convenience: direct data access is often faster to build. KFM should favor governed interfaces even in early slices, using fixtures and mock APIs when necessary. The limitation is that this pass does not verify current route names, frameworks, or implementation maturity.

**Expansion directions and future work.** Future work should define the smallest governed API fixture for a clicked map feature resolving to EvidenceBundle, Evidence Drawer payload, and finite Focus Mode outcome. Suggested first artifact is a mock governed API contract with no direct source or model access.

##### KFM-IDX-MAP-002 — Resource Ontology and HTTP Contract Discipline

**Status and category.** CONFIRMED. Category: MAP / API design and resource contracts. Source attribution: [Web APIs] [Pass 18]. Related ideas include KFM-IDX-MAP-001, KFM-IDX-MOD-005, KFM-IDX-VAL-006, and KFM-IDX-EVD-008.

**Normalized statement.** KFM APIs should be designed around explicit resources, lifecycles, relationships, HTTP semantics, response codes, documentation, and prototypes rather than ad hoc endpoints.

**Detailed explanation and why it matters.** The Web APIs reference emphasizes design-first API work: resource ontology, URLs through relationships, HTTP verbs mapped to lifecycle actions, response codes, documentation, prototyping, and developer experience. Pass 18 integrates API design into KFM's governed architecture. For KFM, resource ontology is a trust issue because resources such as SourceDescriptor, EvidenceBundle, DecisionEnvelope, ReleaseManifest, LayerManifest, Claim, Review, Correction, and Receipt have different roles. If an API flattens them into generic layer or answer endpoints, users and developers lose the distinctions that make KFM auditable.

**Dependencies, tensions, and limits.** This idea depends on MOD bounded contexts and EVD object-family separation. The tension is that KFM has many object families, and not all need public resources. The API should expose governed public resources and review resources without making internal lifecycle stores public. The limitation is current implementation evidence: route names and DTOs remain UNKNOWN until repo inspection.

**Expansion directions and future work.** Future work should create a resource ontology map showing public, restricted, internal, and derived resources. A suggested first artifact is an OpenAPI-like contract for evidence resolution, layer metadata, and finite Focus Mode responses.

##### KFM-IDX-MAP-003 — MapLibre as Downstream 2D Renderer

**Status and category.** CONFIRMED. Category: MAP / renderer boundary. Source attribution: [MapLibre Operating Manual] [Master MapLibre Atlas]. Related ideas include KFM-IDX-GOV-006, KFM-IDX-MOD-001, KFM-IDX-EVD-001, and KFM-IDX-INT-001.

**Normalized statement.** MapLibre should serve as KFM's disciplined downstream 2D renderer and interaction runtime, not as a canonical store, policy authority, citation authority, release authority, or AI authority.

**Detailed explanation and why it matters.** The MapLibre operating manual states the rule directly: the renderer is downstream of trust, never upstream of it. The Master MapLibre atlas extends the same rule across tiles, styles, PMTiles, MVT/MLT, COGs, popups, Story Nodes, 3D scenes, graph projections, and AI answers. MapLibre can render released artifacts, manage camera and interaction state, let users select features, and return context to governed services. It cannot decide what is true, safe, current, reviewed, or publishable. This distinction is essential because map libraries are powerful enough to make any layer look authoritative.

**Dependencies, tensions, and limits.** This idea depends on governed APIs, layer manifests, public-safe artifact generation, Evidence Drawer integration, and release state. The tension is that MapLibre UI implementation may be the most visible part of KFM, while the trust machinery is less visible. The system should make trust state visible in the map shell without letting the shell become the truth source.

**Expansion directions and future work.** Future work should define MapLibre adapter boundaries: what data the renderer may receive, what events it may emit, what it must never fetch, and how it displays stale, denied, restricted, or unresolved states. A first artifact could be a layer-click proof where MapLibre only sends a feature candidate to the governed API.

##### KFM-IDX-MAP-004 — Tiles, PMTiles, COGs, GeoParquet, and MVT/MLT as Rebuildable Artifacts

**Status and category.** CONFIRMED. Category: MAP / map artifact family. Source attribution: [Master MapLibre Atlas] [MapLibre Operating Manual] [New Ideas 5-10]. Related ideas include KFM-IDX-EVD-007, KFM-IDX-VAL-005, KFM-IDX-MOD-007, and KFM-IDX-MAP-008.

**Normalized statement.** Tiles, PMTiles, COGs, GeoParquet files, MVT/MLT tiles, style JSON, and related map products should be treated as rebuildable artifacts rather than canonical truth.

**Detailed explanation and why it matters.** The Master MapLibre atlas repeatedly identifies map artifacts as downstream carriers. New Ideas 5-10 adds operational detail for PMTiles: single-file HTTP Range archives are efficient, but they need versioned filenames, sidecars, root hashes, range proofs, and cache-aware release behavior. The MapLibre manual separates renderer, style, tile strategy, delivery, evidence, and AI. Together, these sources make a durable point: KFM can use modern map artifact formats aggressively, but those artifacts must remain reproducible derivatives of evidence, catalog, policy, and release decisions.

**Dependencies, tensions, and limits.** This idea depends on deterministic build inputs, artifact manifests, catalog records, receipts, and validators. The tension is performance: static artifacts are appealing because they are fast and scalable, but performance does not confer authority. The limitation is that different artifact formats need different validation and metadata.

**Expansion directions and future work.** Future work should create an artifact registry that lists each format, allowed use, required provenance, required validation, cache behavior, and release class. A first artifact could be a PMTiles plus STAC/DCAT/PROV fixture tied to a MapReleaseManifest.

##### KFM-IDX-MAP-005 — Layer, Style, TileArtifact, and MapRelease Manifests

**Status and category.** PROPOSED. Category: MAP / manifest discipline. Source attribution: [Master MapLibre Atlas] [MapLibre Operating Manual]. Related ideas include KFM-IDX-EVD-008, KFM-IDX-VAL-006, KFM-IDX-MAP-004, and KFM-IDX-MAP-008.

**Normalized statement.** KFM should use manifests for layers, styles, tile artifacts, and map releases so map delivery is traceable, validated, and reversible.

**Detailed explanation and why it matters.** The MapLibre atlas contains a repeated object vocabulary around LayerManifest, StyleManifest, TileArtifactManifest, and MapReleaseManifest. The MapLibre manual also calls for contract surfaces and object-family mapping. Manifests are useful because they prevent a public map from being assembled out of undocumented URLs, hand-coded style snippets, or stale layer assumptions. A layer manifest can record source role, evidence reference, geometry type, policy label, allowed zoom, freshness, and limitations. A tile artifact manifest can record input digest, build tool, version, flags, output hash, and catalog references. A map release manifest can tie together the public map state and rollback target.

**Dependencies, tensions, and limits.** This idea depends on stable schemas, validators, release discipline, and UI integration. It is PROPOSED because the corpus supplies the pattern but not current implementation proof. The tension is manifest sprawl. KFM should keep manifests distinct but linked, with minimum required fields per release class.

**Expansion directions and future work.** Future work should create a minimal manifest wave for one proof lane. Suggested first artifact is a hydrology LayerManifest, TileArtifactManifest, and MapReleaseManifest with validation fixtures and a rollback example.

##### KFM-IDX-MAP-006 — Evidence Drawer and Focus Mode as Trust-Visible Surfaces

**Status and category.** CONFIRMED. Category: MAP / trust-visible UI. Source attribution: [MapLibre Operating Manual] [Whole UI AI] [Ollama Ubuntu]. Related ideas include KFM-IDX-EVD-001, KFM-IDX-EVD-002, KFM-IDX-INT-007, and KFM-IDX-VAL-007.

**Normalized statement.** Evidence Drawer and Focus Mode should expose evidence, policy, review, release, citation, and finite-outcome state rather than acting as ordinary popups or unconstrained chat.

**Detailed explanation and why it matters.** The MapLibre and Whole UI/AI reports treat the UI as part of KFM's trust model. Evidence Drawer is the surface where users inspect support, source role, policy posture, limitations, and release state. Focus Mode is an interpretive surface that can synthesize only over admissible released evidence and should return finite outcomes such as ANSWER, ABSTAIN, DENY, or ERROR. The Ollama guide reinforces that local or private model runtimes belong behind governed APIs after evidence and policy checks. These surfaces make KFM usable without hiding the evidence chain.

**Dependencies, tensions, and limits.** This idea depends on EvidenceBundle resolution, runtime envelopes, citation validation, policy decisions, and UI state design. The tension is that users may expect a simple chatbot or popup. KFM should make the trust controls natural rather than optional. The limitation is that exact component names and app paths remain UNKNOWN without repo inspection.

**Expansion directions and future work.** Future work should define a shared Evidence Drawer payload contract and Focus Mode response envelope. The first artifact could be a mock layer click that opens a drawer and produces an abstaining Focus Mode answer when evidence is insufficient.

##### KFM-IDX-MAP-007 — Story Nodes and Review Surfaces

**Status and category.** PROPOSED. Category: MAP / narrative and review UI. Source attribution: [Whole UI AI] [Master MapLibre Atlas]. Related ideas include KFM-IDX-MAP-006, KFM-IDX-POL-004, KFM-IDX-INT-008, and KFM-IDX-APP-007.

**Normalized statement.** Story Nodes and review surfaces should present narrative, map, evidence, sensitivity, and correction context through governed payloads rather than unreviewed storytelling or direct source access.

**Detailed explanation and why it matters.** KFM's corpus includes public-facing ambitions: map-first exploration, story panels, review consoles, planning support, and evidence-rich explanation. The Whole UI/AI report proposes StoryManifest, review console, and persistent shell concepts. The MapLibre atlas adds Story Node governance and historic overlay ideas. These are valuable because not all KFM users will inspect raw evidence objects; some will learn through guided narratives. But narrative is risky if it outruns evidence, hides uncertainty, or exposes sensitive material. Story Nodes should therefore be release-aware, evidence-bound, policy-filtered, and correction-friendly.

**Dependencies, tensions, and limits.** This idea depends on EvidenceBundle resolution, release manifests, UI contracts, sensitivity rules, and review workflows. It is PROPOSED because the corpus does not verify implemented Story Node or review surfaces. The tension is editorial: a story may want coherence while evidence may be partial or contested. KFM should preserve tensions rather than flatten them.

**Expansion directions and future work.** Future work should create a Story Node fixture with map viewport, layer references, evidence references, narrative text, policy labels, review state, and correction link. Good pilots include historic corridors, public-safe archaeology, hydrology proof, or habitat-fauna assignment.

##### KFM-IDX-MAP-008 — Client Verification of Released Map Artifacts

**Status and category.** PROPOSED. Category: MAP / artifact verification at consumption boundary. Source attribution: [New Ideas 5-10] [Master MapLibre Atlas]. Related ideas include KFM-IDX-EVD-006, KFM-IDX-EVD-007, KFM-IDX-VAL-005, and KFM-IDX-MAP-004.

**Normalized statement.** KFM should support client or prefetch verification of released map artifacts using manifests, hashes, signatures, sidecars, and proof references where the release class justifies it.

**Detailed explanation and why it matters.** New Ideas 5-10 proposes a client verification flow for PMTiles: fetch the sidecar, verify its signature, locate the byte range for a tile, fetch tile bytes and proof, verify against root_hash, then decode. The Master MapLibre atlas generalizes this into a broader artifact verification posture. KFM does not need every public user to understand these mechanics, but the system benefits when CI, prefetchers, clients, or review tools can detect stale, swapped, unsigned, or mismatched artifacts. This becomes especially important when static artifacts are served through CDNs or object storage.

**Dependencies, tensions, and limits.** This idea depends on sidecar schemas, proof generation, release manifests, trusted keys, hosting behavior, and performance budgets. It is PROPOSED because implementation is unverified. The tension is cost: client-side verification can add latency and complexity. KFM should allow graduated verification: CI-only at first, prefetch verification for review, and client verification for high-risk release classes.

**Expansion directions and future work.** Future work should define verification modes by release class: no public artifact, CI digest only, prefetch digest, signed sidecar, selected byte-range proof, and full byte-range proof. A first artifact is a small PMTiles fixture with a documented verification script.


### 6.8 INT — Analysis, AI, Interpretation, and Planning Support

#### 6.8.1 Category Overview

INT is a supporting and interpretive category. It gathers analysis, machine learning, AI synthesis, field and remote-sensing interpretation, planning scenarios, indicators, and decision-support methods. The corpus does not reject analysis. It rejects unbounded interpretation presented as truth. Spatial analysis can reveal patterns, indicators can support planning, models can classify or predict, remote sensing can identify candidates, and AI can help synthesize evidence. In KFM, however, all of those outputs remain downstream of source roles, evidence resolution, representation choices, policy, validation, release state, and correction paths.

The category is CONFIRMED as corpus-derived. The GIS primer frames analysis as a way of understanding the world through geographic representation. The environmental ArcGIS text demonstrates applied hazard, vulnerability, climate, water, wildfire, field, and environmental workflows. The urban GIS text emphasizes planning support, collaborative planning, quality-of-life indicators, transport scenarios, social learning, equity, and resilience. The AI Python reference supplies AI/ML concepts and warnings about data, workflow, algorithms, and limitations. The Ollama and governed-AI reports turn those ideas into KFM-specific constraints: the model is a replaceable interpretive runtime behind governed APIs, not a truth source. Archaeological 3D GIS shows that field and 3D capture require interpretive humility.

INT is also where KFM prevents the most seductive failure mode: a sophisticated analysis, visually persuasive map, or fluent AI answer can feel more certain than its evidence permits. This category therefore keeps assumptions, uncertainty, data lineage, model limits, and citation validation in view.

#### 6.8.2 Subcategories

The first INT subcategory is spatial analysis as bounded interpretation. The second is indicators, statistics, and planning support, where assumptions and stakeholder context must be declared. The third is AI and machine learning, including model workflows, training data, evaluation, derivative outputs, and AI receipts. The fourth is field capture and remote sensing, which can produce candidate evidence but not automatically confirmed claims. The fifth is dimensional interpretation, especially 2.5D versus 3D. The sixth is web scraping and feed acquisition as drift-prone interpretation work. The seventh is bounded RAG and Focus Mode synthesis with citation validation. The eighth is participatory, equity, resilience, and scenario decision support.

#### 6.8.3 Individual Idea Entries

##### KFM-IDX-INT-001 — Spatial Analysis as Interpretation, Not Root Truth

**Status and category.** CONFIRMED. Category: INT / spatial analysis. Source attribution: [GIS Primer] [ArcGIS Environmental] [Pass 18]. Related ideas include KFM-IDX-MOD-001, KFM-IDX-MOD-002, KFM-IDX-EVD-001, and KFM-IDX-MAP-003.

**Normalized statement.** Spatial analysis in KFM should be treated as interpretation over represented evidence, not as root truth or self-validating output.

**Detailed explanation and why it matters.** GIS analysis can answer important questions about hazard exposure, environmental conditions, resource context, spatial relationships, vulnerability, landcover, movement, and settlement patterns. The environmental ArcGIS exercises demonstrate useful workflows such as flood hazard analysis, hurricane impacts, wildfire extent, social vulnerability, volcanic hazards, water resources, climate scenarios, and field data collection. KFM can adapt these patterns, but it must keep the analytical result tied to source roles, data model, assumptions, scale, time, and evidence. A buffer, overlay, enrichment, classification, zonal statistic, or hotspot result is not a new sovereign fact; it is an interpretation produced under assumptions.

**Dependencies, tensions, and limits.** This idea depends on MOD representation rules, EVD evidence objects, VAL validation, and MAP trust-visible outputs. The tension is that analysis is often the reason users come to KFM. The system should not bury analysis under bureaucracy, but it should prevent unsupported interpretations from looking authoritative. The limitation is that general GIS methods from textbooks require KFM-specific acceptance criteria before publication.

**Expansion directions and future work.** Future work should define an `AnalysisResult` profile with source inputs, method, assumptions, spatial/temporal scope, uncertainty, validation result, and release state. A first artifact could be an environmental hazard or habitat overlay that displays both result and methodological limitations in Evidence Drawer.

##### KFM-IDX-INT-002 — Indicators and Planning Support Need Declared Assumptions

**Status and category.** CONFIRMED. Category: INT / indicators and planning support. Source attribution: [Urban GIS] [Pass 18]. Related ideas include KFM-IDX-INT-008, KFM-IDX-MOD-008, KFM-IDX-APP-008, and KFM-IDX-EVD-002.

**Normalized statement.** KFM indicators and planning-support outputs should declare assumptions, source choices, weighting, scale, uncertainty, equity relevance, and decision context.

**Detailed explanation and why it matters.** The urban planning GIS source is rich with planning support: scenario analysis for low-carbon transport, collaborative planning, environmental quality under multiple deprivation, walking and built environment, social learning, public-space interaction, urban quality of life, travel perception, qualitative GIS, street quality, growth modeling, multiple-criteria cycle-route design, resettlement dynamics, transit-oriented development, water-supply preferences, flood-risk growth impacts, VGI for evacuation shelters, and equitable resettlement. These are not simple data lookups. They are decision-support structures that depend on social, political, methodological, and spatial assumptions. KFM should preserve those assumptions rather than presenting an index or scenario as objective truth.

**Dependencies, tensions, and limits.** This idea depends on source ledgers, MOD scale/representation, POL equity and public-safety considerations, VAL methodology checks, and UI explanation surfaces. The tension is that indicators are useful because they compress complexity, while compression can hide normative choices. The limitation is that KFM cannot automatically settle planning values; it can expose assumptions and evidence.

**Expansion directions and future work.** Future work should define an `IndicatorDefinition` or `ScenarioDefinition` template with inputs, weights, assumptions, stakeholders, intended use, prohibited use, update cadence, and uncertainty notes. A first artifact could be a county-year frontier or resilience indicator fixture with declared assumptions.

##### KFM-IDX-INT-003 — Machine Learning Outputs Remain Derivative

**Status and category.** CONFIRMED. Category: INT / AI and machine learning. Source attribution: [AI Python] [Governed AI Ledger] [Pass 18]. Related ideas include KFM-IDX-EVD-001, KFM-IDX-VAL-007, KFM-IDX-MOD-008, and KFM-IDX-MAP-006.

**Normalized statement.** Machine learning outputs in KFM should remain derivative interpretations tied to data, model, version, evaluation, receipts, policy, and evidence, not promoted to root truth.

**Detailed explanation and why it matters.** The AI Python reference introduces AI/ML concepts, data lifecycle, supervised and unsupervised learning, algorithms, challenges, and ethical considerations. KFM doctrine narrows those generic possibilities into a governed posture. ML can classify, cluster, predict, rank, detect anomalies, or support retrieval, but it should not become the authority for a claim without evidence and validation. A model-detected archaeological feature is a candidate. A habitat suitability prediction is a model output. A vulnerability score is an indicator. A generated explanation is a synthesis. Each needs input provenance, training or method description, evaluation, uncertainty, policy state, and citation or abstention behavior.

**Dependencies, tensions, and limits.** The idea depends on data lineage, model cards or receipts, validation reports, policy checks, and EvidenceBundle resolution. The tension is that ML outputs can scale analysis rapidly and may appear statistically authoritative. KFM must use them without letting model confidence replace source authority. The limitation is that this pass does not evaluate any specific model.

**Expansion directions and future work.** Future work should define a model-output governance profile: input evidence, model version, training data boundary, evaluation metrics, intended use, failure modes, bias/sensitivity review, and release class. A first artifact could be a synthetic classification output that is allowed as candidate evidence but denied as a confirmed claim.

##### KFM-IDX-INT-004 — Field Capture and Remote Sensing as Candidate Evidence

**Status and category.** CONFIRMED. Category: INT / field and remote-sensing interpretation. Source attribution: [ArcGIS Environmental] [Archaeological 3D GIS] [New Ideas 5-8]. Related ideas include KFM-IDX-MOD-007, KFM-IDX-MOD-008, KFM-IDX-POL-004, and KFM-IDX-APP-005.

**Normalized statement.** Field capture and remote sensing should be admitted as evidence or candidate evidence according to source role, method, accuracy, temporal scope, review state, and policy controls.

**Detailed explanation and why it matters.** Environmental GIS exercises include field data collection and remote-sensing-supported hazard and climate workflows. Archaeological 3D GIS shows how field capture, image-based modeling, laser scanning, CT, 3D GIS, and georeferenced models can transform archaeological documentation. New Ideas 5-8 brings operational environmental remote-sensing signals such as MAIAC AOD, FIRMS, and SMAP into watcher patterns. The KFM normalization is that capture does not equal confirmation. A field observation, satellite detection, smoke mask, LiDAR feature, or 3D model can support claims only when its source role, accuracy, processing, temporal state, and review are clear.

**Dependencies, tensions, and limits.** This idea depends on source descriptors, MOD representation types, EVD provenance, POL sensitivity controls, and VAL validation. The tension is that field and remote-sensing products may be among the strongest available evidence in some domains, while still being incomplete or ambiguous. The limitation is that source-specific accuracy and rights require verification.

**Expansion directions and future work.** Future work should define capture-method metadata and candidate-evidence rules for remote sensing, field notes, 3D capture, and citizen science. A first artifact could be a field-capture fixture with redaction receipt, source role, review state, and public-safe derived map artifact.

##### KFM-IDX-INT-005 — 2.5D and Full 3D Are Not Interchangeable

**Status and category.** CONFIRMED. Category: INT / 3D interpretation. Source attribution: [Archaeological 3D GIS]. Related ideas include KFM-IDX-MOD-007, KFM-IDX-MAP-004, KFM-IDX-POL-004, and KFM-IDX-APP-007.

**Normalized statement.** KFM should not treat 2.5D surfaces, full 3D models, volumetric data, reconstructions, and 3D scenes as interchangeable evidence or visualization forms.

**Detailed explanation and why it matters.** Archaeological 3D GIS provides a direct warning for KFM. A 2.5D representation can drape imagery or elevation onto a surface, but it cannot represent multiple elevation values for the same horizontal coordinate. Full 3D models, point clouds, volumetric CT data, and interpretive reconstructions support different questions and have different evidentiary status. This matters in archaeology, terrain, geology, infrastructure, settlement history, and potential future 3D/globe contexts. KFM should not adopt 3D simply because it looks impressive, and it should not flatten 3D evidence into 2D when vertical or volumetric relationships are central to the claim.

**Dependencies, tensions, and limits.** The idea depends on MOD representation metadata, MAP renderer boundaries, EVD evidence records, and POL sensitivity controls. The tension is operational: 2D MapLibre is the recommended primary renderer, while some evidence may require 3D. KFM should keep 2D as default and admit 3D conditionally when evidence burden justifies it. The limitation is that 3D tooling, performance, rights, and viewer parity remain verification needs.

**Expansion directions and future work.** Future work should define a 3D admission profile: evidence need, data type, capture method, georeferencing, uncertainty, review state, public-safe transformation, and renderer requirements. A first artifact could compare a 2.5D terrain layer and a full 3D archaeological model with prohibited inferences for each.

##### KFM-IDX-INT-006 — Web Scraping and External Feed Acquisition Need Drift Control

**Status and category.** CONFIRMED. Category: INT / acquisition and drift control. Source attribution: [Web Scraping Java] [New Ideas 5-8]. Related ideas include KFM-IDX-SRC-002, KFM-IDX-SRC-008, KFM-IDX-VAL-003, and KFM-IDX-POL-002.

**Normalized statement.** Web scraping and external feed acquisition should be treated as governed source-intake experiments with drift control, rights checks, rate limits, receipts, and quarantine defaults.

**Detailed explanation and why it matters.** The web-scraping reference describes practical scraping concerns such as redirects, missing code, broken links, Ajax pages, forms, errors, scalability, persistence, and tests. In KFM, these are not merely engineering issues. They are source-governance risks. A scraper can silently break, harvest unauthorized material, misread changed markup, miss rate limits, or produce output that looks authoritative because it is automated. New Ideas 5-8 shows a safer pattern for external feeds: source-head probes, ETag/Last-Modified capture, metrics, policy IDs, and signed run receipts. KFM should treat scraping as source admission, not a shortcut around source descriptors.

**Dependencies, tensions, and limits.** This idea depends on source descriptors, rights verification, robots and terms checks, fixture tests, error receipts, and quarantine workflows. The tension is that many useful sources may not have ideal APIs. KFM can use scraping where appropriate, but only with explicit governance. The limitation is that current source rights and endpoint behavior remain NEEDS VERIFICATION.

**Expansion directions and future work.** Future work should define a connector/scraper intake checklist covering source authority, rights, terms, robots/rate posture, drift detection, parser tests, failure receipts, and quarantine behavior. A first artifact could be a simulated HTML drift fixture that forces ABSTAIN or QUARANTINE rather than silently changing output.

##### KFM-IDX-INT-007 — Bounded AI/RAG Synthesis with Citation Validation

**Status and category.** CONFIRMED. Category: INT / governed AI and RAG. Source attribution: [Ollama Ubuntu] [Governed AI Ledger]. Related ideas include KFM-IDX-EVD-001, KFM-IDX-EVD-002, KFM-IDX-MAP-006, and KFM-IDX-VAL-007.

**Normalized statement.** AI and RAG synthesis in KFM should operate only over admissible, policy-safe, released evidence, behind a governed API, with citation validation and finite outcomes.

**Detailed explanation and why it matters.** The Ollama guide and Governed AI Ledger converge strongly: a model runtime may summarize, explain, or embed, but it must remain provider-neutral, replaceable, and subordinate to evidence and policy. It should not read RAW, WORK, QUARANTINE, canonical stores, or unpublished candidate data directly. It should not receive direct client traffic or publish raw model output. It should accept bounded context, produce structured responses, validate citations, emit runtime envelopes, and return ANSWER, ABSTAIN, DENY, or ERROR. This makes AI useful without turning generated language into evidence.

**Dependencies, tensions, and limits.** The idea depends on EvidenceBundle resolution, policy precheck/postcheck, citation validation, AIReceipt, runtime envelope, no-direct-model-client tests, and UI negative states. The tension is that AI is most attractive when it feels conversational and flexible. KFM must preserve usefulness while constraining context and output. The limitation is that this pass does not verify a live adapter or model runtime.

**Expansion directions and future work.** Future work should implement a MockAdapter proof before any real model. A first artifact should test cited answer, citation failure abstention, policy denial, missing evidence abstention, and runtime error, all using a public-safe EvidenceBundle fixture.

##### KFM-IDX-INT-008 — Participatory, Equity, and Scenario Decision Support

**Status and category.** CONFIRMED. Category: INT / planning and participation. Source attribution: [Urban GIS] [ArcGIS Environmental] [Hazards]. Related ideas include KFM-IDX-INT-002, KFM-IDX-POL-007, KFM-IDX-APP-008, and KFM-IDX-MAP-007.

**Normalized statement.** KFM planning support should include participatory, equity, resilience, and scenario context rather than presenting maps or indicators as neutral decisions.

**Detailed explanation and why it matters.** Urban GIS shows that planning support is social as well as technical. Collaborative planning, social learning, quality of life, environmental health inequalities, transport scenarios, resettlement, cycle routes, TOD, urban water supply, flood shelters, and resilience all depend on stakeholder context and normative choices. Environmental and hazards sources add risk and vulnerability contexts. KFM can be valuable as a decision-support atlas, but it must not turn indicators into decisions or maps into policy. It should expose assumptions, alternatives, equity implications, uncertainty, and evidence.

**Dependencies, tensions, and limits.** This idea depends on indicator definitions, scenario manifests, EvidenceBundle support, UI story/review surfaces, and policy disclaimers. The tension is that decision support should be actionable, but KFM must avoid overstepping into unreviewed recommendations or life-safety instructions. The limitation is that participatory processes and steward roles require real governance outside the document corpus.

**Expansion directions and future work.** Future work should define scenario and participation metadata for planning-oriented outputs: stakeholder group, assumption set, equity lens, source evidence, model method, decision status, and public limitations. A first artifact could be a resilience scenario story node that compares alternatives without declaring an unsupported policy conclusion.

### 6.9 APP — Domain Lanes, Field Capture, and Applied Knowledge Families

#### 6.9.1 Category Overview

APP is the applied-domain category. It gathers the domain lanes, field-capture patterns, and proof-slice candidates that make KFM more than a doctrine stack. The corpus contains detailed domain blueprints for hydrology, habitat, fauna, flora, soil, agriculture, geology, atmosphere, hazards, roads/rail/trade, settlements/infrastructure, archaeology, people/genealogy/DNA/land ownership, and habitat-fauna thin slicing. It also contains an implementation reference that raises a frontier-demography/economy county-year panel as a future substantive product. APP normalizes these into applied knowledge families and expansion paths.

The category is mixed-status by design. Some domain boundary ideas are CONFIRMED as repeated doctrine and source content. Specific implementation lanes remain PROPOSED unless live repo evidence, tests, receipts, manifests, or release artifacts prove them. Domain reports repeatedly state no-mounted-repo conditions, proposed file homes, and unknown runtime maturity. APP therefore preserves domain value without upgrading plans into implementation claims.

APP also prevents domain sprawl. It routes many detailed domain variants into expansion agenda items rather than expanding Section 6 beyond the main-body cap. The strongest applied pattern is not "build every lane now." It is to select proof-bearing thin slices that exercise the trust path: source descriptor, lifecycle, evidence, policy, validation, catalog closure, release manifest, map artifact, Evidence Drawer, bounded interpretation, correction, and rollback.

#### 6.9.2 Subcategories

The first APP subcategory is proof lanes, with hydrology and habitat-fauna as leading candidates. The second is ecology and environmental source watchers. The third is soil, agriculture, landcover, CDL, PLANTS, and material-change monitoring. The fourth is atmosphere and hazards, which require knowledge-character and public-safety boundaries. The fifth is transport, settlements, infrastructure, and geology, which require boundary discipline and public-safe geometry. The sixth is people, genealogy, DNA, land, and archaeology, where assertion-first modeling and sensitivity controls dominate. The seventh is field, remote, 3D, and applied capture methods. The eighth is frontier-demography and economy, a later analytic product requiring temporal, geographic, and source governance.

#### 6.9.3 Individual Idea Entries

##### KFM-IDX-APP-001 — Hydrology Proof Lane

**Status and category.** PROPOSED. Category: APP / proof lane. Source attribution: [Hydrology] [Implementation Reference] [Pass 19]. Related ideas include KFM-IDX-SRC-001, KFM-IDX-SRC-005, KFM-IDX-EVD-002, KFM-IDX-VAL-001, and KFM-IDX-MAP-005.

**Normalized statement.** Hydrology is the strongest early proof lane candidate because it can exercise KFM's lifecycle, evidence, catalog, map, API, validation, and rollback machinery with relatively clear public-source patterns.

**Detailed explanation and why it matters.** The hydrology report proposes HUC12/WBD, NHDPlus HR identity and crosswalks, USGS Water Data observation normalization, NFHL regulatory flood context, 3DEP terrain-derived context, catalog/proof closure, MapLibre layer manifests, Evidence Drawer payloads, policies, and rollback. The Implementation Reference and Pass 19 both identify hydrology or ecology as safer early proof lanes compared with high-sensitivity domains. Hydrology is valuable because it touches KFM's core identity: map-first, time-aware, evidence-first, public-claim-oriented. It can demonstrate the difference between observed water conditions, hydrologic units, regulatory flood layers, terrain context, and release artifacts.

**Dependencies, tensions, and limits.** This idea depends on source descriptors, no-network fixtures, identity crosswalks, temporal modeling, catalog closure, and public-safe layer manifests. The tension is that water data can still be operationally current or safety-relevant. KFM must avoid implying emergency status or live authority without current verification. The limitation is that implementation is PROPOSED; current connectors, tests, or release artifacts are not verified here.

**Expansion directions and future work.** A first hydrology slice should use fixtures: one HUC12, one normalized observation, one regulatory context record, one EvidenceBundle, one layer manifest, one drawer payload, and one release dry-run. Future work can add live source verification only after rights, endpoint, cadence, and policy checks are complete.

##### KFM-IDX-APP-002 — Habitat-Fauna Public-Safe Occurrence Assignment Thin Slice

**Status and category.** PROPOSED. Category: APP / ecology proof lane. Source attribution: [Habitat Fauna Thin Slice] [Habitat] [Fauna]. Related ideas include KFM-IDX-POL-005, KFM-IDX-EVD-002, KFM-IDX-VAL-001, KFM-IDX-MAP-006, and KFM-IDX-INT-004.

**Normalized statement.** A habitat-fauna thin slice should prove one public-safe occurrence-to-habitat assignment with evidence, sensitivity, release, map, drawer, and interpretation controls.

**Detailed explanation and why it matters.** The habitat-fauna thin-slice blueprint asks a precise proof question: can KFM prove one published fauna occurrence habitat assignment? Its proposed answer is a fixture-first lane using controlled public-safe occurrence data, habitat context, source role, sensitivity checks, EvidenceBundle, release manifest, layer manifest, MapLibre rendering, Evidence Drawer payload, Focus Mode outcome, and rollback. This is a strong applied idea because it combines ecological value with KFM's most important governance constraints. It also tests geoprivacy, source authority, occurrence evidence, habitat model support, and UI trust surfaces.

**Dependencies, tensions, and limits.** The idea depends on taxonomic identity, occurrence source roles, habitat classification, public-safe geometry, geoprivacy transform receipts, and validation. The tension is precision: ecological analysis often benefits from exact locations, while public maps may require generalization or suppression. The limitation is that the thin slice is PROPOSED and must not activate live GBIF, eBird, iNaturalist, KDWP, NatureServe, or similar sources without source-role and rights review.

**Expansion directions and future work.** Suggested first artifact is a synthetic fixture set with one non-sensitive occurrence and one sensitive occurrence. The non-sensitive case can produce a public-safe assignment; the sensitive case should deny exact geometry and show withheld precision in Evidence Drawer.

##### KFM-IDX-APP-003 — Ecology Source-Watcher Operational Slice

**Status and category.** PROPOSED. Category: APP / watcher proof lane. Source attribution: [New Ideas 5-8] [Pass 19]. Related ideas include KFM-IDX-SRC-007, KFM-IDX-VAL-003, KFM-IDX-EVD-004, and KFM-IDX-POL-002.

**Normalized statement.** An ecology source-watcher slice can operationalize source-head, tile-health, rights, and run-receipt discipline without publishing source-derived claims.

**Detailed explanation and why it matters.** New Ideas 5-8 proposes probes for MAIAC AOD, FIRMS fire detections, SMAP L4 soil moisture, AirNow, and Kansas Mesonet. Pass 19 treats this as one of the strongest operational deltas because it moves KFM from static doctrine toward source-drift and artifact-readiness proof. The applied idea is not that these thresholds become KFM science absolutes. It is that KFM can test source observation, source-head recording, rights/consent enforcement, finite outcomes, and receipts in a no-publication mode. That makes it a good operational slice.

**Dependencies, tensions, and limits.** The idea depends on source descriptors, fixture probes, source-head fields, DecisionEnvelope, RunReceipt, policy IDs, and explicit no-publication behavior. The tension is currentness: the packet discusses live feeds, but this dossier did not reverify them. The limitation is therefore substantial; all endpoints, terms, and thresholds remain verification items before use.

**Expansion directions and future work.** The first artifact should be no-network probe fixtures: fresh/stale source heads, missing Mesonet consent, AirNow key absent, AOD threshold breach, FIRMS threshold breach, and normal state. The output should be a proposed work or quarantine decision, never public release.

##### KFM-IDX-APP-004 — Soil, Agriculture, CDL, PLANTS, and Landcover Material-Change Lane

**Status and category.** PROPOSED. Category: APP / landcover and agricultural monitoring. Source attribution: [Soil] [Agriculture] [New Ideas 5-15]. Related ideas include KFM-IDX-SRC-006, KFM-IDX-VAL-004, KFM-IDX-EVD-005, and KFM-IDX-POL-002.

**Normalized statement.** KFM should develop soil, agriculture, CDL, PLANTS, and landcover monitoring as a material-change lane that proposes work only when source changes matter enough to reprocess.

**Detailed explanation and why it matters.** Soil and agriculture reports propose source registries, contracts, validators, policies, tests, catalog closure, proof/receipt separation, API/UI trust payloads, and rollback controls. New Ideas 5-15 adds an efficient watcher pattern for USDA CDL and PLANTS county packages. It records source URL, ETag, Last-Modified, class histograms, classmap version, thresholds, species IDs, and stable `spec_hash`, then emits a PROPOSED_WORK_RECORD only when material thresholds are crossed. This is a strong applied lane because it reduces noisy re-runs while preserving auditability and rights checks.

**Dependencies, tensions, and limits.** The idea depends on county geometry, raster histogram calculation, PLANTS package parsing, thresholds, sidecar validation, and source rights review. The tension is that agricultural and ecological change may be important even when simple area thresholds are not crossed. The limitation is that the proposed code includes stubs and example paths; live implementation needs data paths, rights checks, and fixtures.

**Expansion directions and future work.** A first artifact should validate sidecar integrity and materiality against synthetic county histograms. Future work can add STAC item emitters, PMTiles manifests, change heatmap vector tiles, drought overlays, NDVI/CDL correlation, and crop-rotation analysis after the basic watcher is governed.

##### KFM-IDX-APP-005 — Atmosphere and Hazards Knowledge-Character Separation

**Status and category.** CONFIRMED. Category: APP / atmosphere and hazards boundary. Source attribution: [Atmosphere Air] [Hazards]. Related ideas include KFM-IDX-MOD-008, KFM-IDX-POL-007, KFM-IDX-INT-004, and KFM-IDX-VAL-007.

**Normalized statement.** Atmosphere and hazards lanes require strict separation among observations, regulatory archives, public reports, model fields, remote-sensing detections, operational context, and resilience summaries.

**Detailed explanation and why it matters.** The atmosphere/air report states that air, climate, smoke, and Earth-observation layers require strict source-role and knowledge-character labeling because observations, public AQI reports, regulatory archives, model fields, smoke masks, anomaly surfaces, and fusion products are not interchangeable. The hazards blueprint adds that KFM hazards should support analysis, history, regulatory context, operational context, resilience review, map rendering, Evidence Drawer explanation, and governed AI summaries without becoming an emergency alert system. This applied family is high value but high risk because public users may treat hazard or air layers as current instructions.

**Dependencies, tensions, and limits.** The idea depends on knowledge-character labels, temporal freshness, source authority, policy disclaimers, no-life-safety posture, and Evidence Drawer explanations. The tension is that current atmospheric and hazard context can be useful for public understanding, but KFM must direct urgent life-safety needs to official sources. The limitation is that live source status and operational source rights were not verified in this pass.

**Expansion directions and future work.** Future work should create a hazards/atmosphere fixture that includes an observation, a model product, a regulatory layer, and an operational advisory, each with different public behavior. Suggested first artifact is a `not_for_life_safety` DecisionEnvelope fixture.

##### KFM-IDX-APP-006 — Roads, Rail, Trade, Settlements, Infrastructure, and Geology Boundary Discipline

**Status and category.** CONFIRMED. Category: APP / infrastructure, transport, and geology lanes. Source attribution: [Roads Rail Trade] [Settlements Infrastructure] [Geology Resources]. Related ideas include KFM-IDX-POL-006, KFM-IDX-MOD-005, KFM-IDX-MAP-003, and KFM-IDX-EVD-008.

**Normalized statement.** Transport, settlements, infrastructure, and geology/resource lanes should keep physical features, administrative status, operators, historical interpretation, restrictions, public-safe geometry, and derived graph projections distinct.

**Detailed explanation and why it matters.** The roads/rail/trade plan separates modern roads, historic roads, rail corridors, facilities, restrictions, freight corridors, Indigenous trade and mobility corridors, and graph projections. Settlements/infrastructure separates legal municipalities, census places, historic townsites, ghost towns, infrastructure assets, networks, facilities, operators, service areas, condition observations, and dependencies. Geology/resources separates bedrock, surficial geology, stratigraphy, lithology, structures, geomorphology, boreholes, geophysics, geochemistry, mineral occurrences, extraction sites, and public-safe resource layers. Across all three, the shared warning is anti-collapse: a line, label, operator, resource estimate, facility, or graph edge is not automatically a public truth claim.

**Dependencies, tensions, and limits.** The idea depends on bounded contexts, source-role registries, public-safe geometry, policy profiles, evidence resolution, and release manifests. The tension is that these domains are visually compelling and useful for historical and planning maps. KFM must preserve usability while preventing false precision, sensitive exposure, and administrative/physical confusion. The limitation is that domain reports are implementation-grade plans but not current repo proof.

**Expansion directions and future work.** Future work should define boundary matrices for each lane: physical object, legal/administrative status, operator, source authority, temporal scope, public geometry precision, and derived artifact status. A first artifact could be a transport corridor fixture with generalized public geometry and evidence-bound historical uncertainty.

##### KFM-IDX-APP-007 — People, Genealogy, DNA, Land, and Archaeology Sensitive Assertion Lanes

**Status and category.** CONFIRMED. Category: APP / sensitive assertion lanes. Source attribution: [People DNA Land] [Archaeology Plan]. Related ideas include KFM-IDX-POL-003, KFM-IDX-POL-004, KFM-IDX-MOD-006, and KFM-IDX-EVD-002.

**Normalized statement.** People, genealogy, DNA, land ownership, and archaeology lanes should be assertion-first, evidence-bound, privacy-aware, culturally sensitive, and denied or restricted by default where exact public release would create harm.

**Detailed explanation and why it matters.** The People/Genealogy/DNA/Land blueprint and Archaeology Plan define some of the strongest restrictions in the corpus. Person assertions are separate from canonical person records; DNA is restricted by default; relationship hypotheses remain hypotheses; assessor or tax records are not title truth; parcel geometry is not title boundary proof by itself; archaeological exact locations are denied by default; LiDAR, aerial, satellite, geophysical, or remote-sensing anomalies are candidate features until evidence and review support stronger claims. These lanes are high value for history and land knowledge, but they carry privacy, cultural, sovereignty, and physical-site risks.

**Dependencies, tensions, and limits.** The idea depends on assertion-first modeling, living-person classification, DNA restrictions, steward review, source roles, exact-location denial, and correction lineage. The tension is historical richness versus harm prevention. KFM can support research and public education, but not by publishing sensitive claims at unsupported precision. The limitation is that actual steward permissions, source rights, and legal review are outside this pass.

**Expansion directions and future work.** Future work should build synthetic assertion fixtures before any real sensitive data. A first artifact could show a historic land assertion, a living-person denial, a DNA-derived hypothesis denial, and an archaeological candidate feature generalized for public display.

##### KFM-IDX-APP-008 — Frontier-Demography and Economy County-Year Panel Concept

**Status and category.** PROPOSED. Category: APP / frontier-demography and analytical product. Source attribution: [Implementation Reference]. Related ideas include KFM-IDX-MOD-003, KFM-IDX-MOD-004, KFM-IDX-INT-002, and KFM-IDX-VAL-008.

**Normalized statement.** A future KFM frontier-demography/economy product should be built as a versioned county-year analytical panel with explicit frontier definitions, geography versions, observations, crosswalks, uncertainty, release manifests, and rollback cards.

**Detailed explanation and why it matters.** The Implementation Reference identifies the frontier-demography/economy lane as less mature than hydrology, ecology, and documentation-control surfaces, then proposes a substantive product: a versioned county-year frontier panel backed by FrontierDefinition, GeographyVersion, PopulationObservation, EconomicObservation, AgricultureObservation, and AccessObservation objects. This is an important applied direction because it connects KFM's name and historical frontier purpose to a buildable analytical layer. It also stresses why KFM should not be a flat spreadsheet. Frontier status depends on definitions, geography versions, time, population, economy, agriculture, access, crosswalks, uncertainty, source roles, and release state.

**Dependencies, tensions, and limits.** The idea depends on temporal modeling, versioned geography, source ledgers, reproducible joins, uncertainty classes, indicator assumptions, and release/rollback discipline. The tension is that a county-year panel looks simple to users but is semantically dense. The limitation is that the Implementation Reference is lineage and prior connector evidence; current repo maturity and live source availability are not verified here.

**Expansion directions and future work.** Future work should start with definitions, not data harvesting. A first artifact should be a `FrontierDefinition` draft and a synthetic county-year panel fixture that demonstrates geography versioning, observation source roles, and uncertainty before any public analytical claim is made.


## 7. Cross-Cutting Themes

The strongest cross-cutting theme is that KFM is a publication and evidence-governance system before it is a map, model, dashboard, or domain database. The corpus repeatedly assigns value to inspectable claims, EvidenceBundles, source roles, receipts, release manifests, policy decisions, correction paths, and rollback targets. That vocabulary appears in prior passes, domain blueprints, MapLibre manuals, governed-AI reports, and New Ideas packets. The repeated pattern is not accidental. It shows that KFM's core design pressure is trust under growth: as more sources, lanes, maps, artifacts, and interpretive tools appear, the system must preserve traceability rather than letting convenience become authority.

A second theme is that representation is itself a claim surface. GIS, cartography, 3D GIS, environmental workflows, and urban planning references all show that maps and analyses are constructed through choices of scale, projection, classification, simplification, resolution, symbolization, data model, and scenario logic. KFM doctrine turns that technical fact into governance doctrine. A layer is not only a visual object; it is a claim carrier whose fitness, source role, temporal scope, and limitations must be inspectable where material.

A third theme is temporal discipline. The corpus repeatedly distinguishes observed time, valid time, source time, retrieval time, transaction or record time, release time, and correction time. This matters for hydrology observations, hazard advisories, land ownership assertions, county-year frontier panels, source watchers, material-change records, and public releases. KFM cannot safely answer "what is true now" unless it knows which time dimension the question invokes.

A fourth theme is that public delivery surfaces are trust membranes. Governed APIs, MapLibre, Evidence Drawer, Focus Mode, Story Nodes, map artifacts, and review consoles should be downstream of source admission, evidence resolution, policy checks, validation, and release. The UI is not decoration, but it is also not sovereign truth. Its task is to make trust state visible and usable.

A fifth theme is source humility. The corpus contains official-style domain blueprints, technical textbooks, prior cumulative passes, New Ideas packets, public-repo summaries, and no-repo planning reports. The correct synthesis is not to flatten them. Doctrine governs; technical references supply methods; domain reports supply lane patterns; New Ideas packets create expansion pressure; prior passes preserve continuity; and current implementation claims require current repo, tests, logs, receipts, workflows, or generated artifact evidence.

A sixth theme is deny-by-default exposure where harm is plausible. Archaeology, rare species, living-person data, DNA/genomic material, cultural corridors, infrastructure, hazards, and source-rights uncertainty all require stronger controls than ordinary public educational layers. The corpus does not reject public knowledge. It insists that public release be appropriate to significance and risk.

A seventh theme is fixture-first proof. The best early KFM work is not broad live ingestion or polished UI. It is small, reversible, no-network proof: schemas, fixtures, validators, policies, receipts, catalog closure, release manifests, rollback references, and one public-safe explanation path. This theme appears in hydrology, habitat-fauna, governed AI, PMTiles attestation, and material-change watcher proposals.

An eighth theme is that AI and analysis are interpretive derivatives. The corpus allows bounded AI, machine learning, indicators, scenarios, spatial analysis, and planning support, but only when evidence, policy, validation, and citation controls remain in charge. Fluent generation, model output, vector search, graph projections, and summaries are useful carriers; they are never root truth.


## 8. Overlaps, Contradictions, and Gaps

The most important overlap is between source admission and evidence receipts. SRC governs how sources enter the lifecycle and how watchers propose work; EVD records what evidence and processes support later claims. These overlap because source-head metadata, ETag and Last-Modified values, source rights, spec_hash values, and run receipts can appear at the admission edge and again inside proof or release objects. The overlap is healthy if the objects remain distinct. It becomes a problem only if a source probe receipt is treated as proof that a claim is true.

A second overlap is between temporal modeling and release/correction discipline. MOD separates valid, observed, source, retrieval, release, and correction time; VAL and EVD use receipts and manifests to prove when processes ran and what release state existed. The same event may therefore appear in a domain record, a receipt, a release manifest, and a correction record. KFM needs this overlap because time-aware publication requires it, but it should avoid one generic `date` field that collapses all meanings.

A third overlap is between policy and representation. Public-safe generalization, sensitive exact-location denial, rare species geoprivacy, archaeological suppression, and infrastructure exposure controls are policy decisions expressed through representation choices. The map artifact and the policy decision must both be inspectable. The gap is that the corpus proposes many policy profiles but does not yet provide one verified cross-domain policy implementation.

A fourth overlap is between MapLibre artifact governance and API contract design. Some map surfaces can be static artifacts, while others need governed API mediation. PMTiles, COGs, GeoParquet, MVT/MLT, STAC/DCAT/PROV records, layer manifests, and Evidence Drawer payloads all sit near this boundary. The design tension is performance versus governance. Static artifacts are desirable, but only after release, integrity, and policy controls are recorded.

A fifth overlap is between analysis, AI, and planning. Spatial analysis, indicators, machine learning, Focus Mode, and scenario tools can all produce public-facing conclusions. The corpus's consistent answer is that all such outputs remain interpretive derivatives. The gap is that KFM still needs explicit acceptance criteria for when an analytical output is evidence-supported enough to publish, when it should be review-only, and when it should abstain.

The principal contradiction is not inside doctrine but between greenfield assumptions and implementation-reference lineage. The Greenfield Building Plan assumes an empty starting point, while the Implementation Reference reports prior connector-based public repository surface. This pass resolves the contradiction by source-bounding both: greenfield doctrine is useful for clean architecture; implementation-reference claims are lineage and verification prompts unless current repo evidence is inspected. Neither should be used to overclaim current implementation.

Another tension is between domain breadth and proof discipline. The corpus covers many domain lanes, but the strongest implementation advice is narrow: hydrology proof lane, habitat-fauna fixture, ecology watcher, PMTiles attestation, and governed AI mock slice. The gap is prioritization. The Expansion Agenda addresses that by routing breadth into backlog while preserving a small number of first artifacts.

The largest evidence gap remains current implementation maturity. This pass did not inspect a mounted live repo, run tests, check CI, verify current endpoints, validate source terms, or confirm runtime behavior. Therefore route names, package versions, actual schema homes, policy engine behavior, dashboards, branch protections, and deployed services remain UNKNOWN or NEEDS VERIFICATION.


## 9. Weakly Supported, Ambiguous, or Excluded Material

The first weakly supported class is current operational status. New Ideas 5-8 reports a steady operational picture across several biodiversity, observation, Earth observation, weather, and mapping feeds, but those statements are time-sensitive. They are useful as a prompt for source-currentness verification, not as durable truth in this dossier. Any operational use must recheck source status, endpoint behavior, rights, cadence, API keys, and product versions.

The second weak class is package and tool version status. MapLibre releases, PMTiles tooling, PMTiles readers, freestiler, tipmtiles, MLT support, DSSE/cosign setup, Bao proof tooling, and dependency licenses may change. This document preserves the architectural value of attestation, deterministic builds, and client verification, but it does not pin versions or certify current package state.

The third ambiguous class is repo path placement. Directory Rules provide the governing doctrine for responsibility roots and schema-home discipline, but many domain reports and New Ideas packets include proposed paths. Those paths remain PROPOSED unless checked against Directory Rules, current repo evidence, and ADRs. This dossier intentionally does not turn proposed paths into facts.

The fourth weak class is implementation maturity. Many domain PDFs are PDF-only plans created in no-mounted-repo contexts. They are valuable for lane architecture, source-role discipline, and validation planning, but they do not prove that schemas, validators, policies, APIs, UI components, workflows, tests, or dashboards exist in the current repo.

The fifth ambiguous class is external rights and redistribution. Some sources may be public, open, official, or documented; that does not settle redistribution, attribution, API-key, quota, consent, or public-release posture. KFM should deny or quarantine when rights are unclear and route such cases to SourceRightsDecision or verification backlog.

The sixth excluded class is emergency instruction. Hazards, wildfire, flood, air-quality, and operational advisory materials can support analysis and context, but KFM should not publish life-safety instructions as if it were an emergency alerting system. User-facing outputs should point to official alerting and response authorities where life-safety action is requested.

The seventh excluded class is unreviewed sensitive exact geometry. Rare species occurrences, archaeological sites, culturally sensitive corridors, living-person locations, DNA/genomic data, and critical infrastructure details should not be exposed as exact public geometry unless explicit policy, review, rights, sensitivity, and release gates permit it.

The eighth weak class is one-size-fits-all AI. The corpus supports bounded model use behind governed APIs, but not free-form public chat over arbitrary stores. Local model runtimes, embeddings, vector indexes, and RAG outputs remain derivative and must be evidence-bounded, policy-checked, citation-validated, and receipt-emitting.


## 10. Expansion Agenda

### 10.1 Research

**Hydrology source and identity research.** Priority: High. Why: Hydrology remains the strongest proof lane and needs clear source roles for WBD/HUCs, NHDPlus HR, USGS Water Data, NFHL, and terrain-derived context. Dependencies: source descriptors, rights verification, HUC fixture, temporal fields. Next step: verify current source terms and choose a minimal fixture. First artifact: Hydrology SourceRole and EvidenceBundle fixture pack.

**Source-currentness and rights research.** Priority: High. Why: multiple New Ideas packets depend on operational source and tool facts that are time-sensitive. Dependencies: source ledger, owner assignments, verification cadence. Next step: build a verification backlog covering Mesonet, AirNow, CDL, PLANTS, PMTiles tooling, and MapLibre target version. First artifact: SourceCurrentnessReport table.

**Frontier county-year source research.** Priority: Medium. Why: the frontier-demography/economy panel is a likely flagship but needs evidence and geography-version discipline before design hardens. Dependencies: geography versions, population/economy/agriculture/access source candidates, temporal modeling. Next step: identify candidate sources and uncertainty classes. First artifact: FrontierPanelSourceMemo.

### 10.2 Writing

**Object-family explanation note.** Priority: High. Why: KFM's trust depends on separating EvidenceBundle, receipts, proofs, catalogs, release manifests, policy decisions, and claims. Dependencies: EVD category entries and Directory Rules. Next step: draft a concise explanation with examples. First artifact: Trust Object Family Map.

**Public-safe map explanation guide.** Priority: Medium. Why: users need to understand why some layers are generalized, stale, denied, or evidence-bounded. Dependencies: MAP, POL, and VAL entries. Next step: write Evidence Drawer prose patterns for withheld precision, stale data, and abstention. First artifact: Evidence Drawer Language Guide.

**Domain published-language glossary.** Priority: Medium. Why: terms such as source, status, occurrence, site, model, event, and release shift meaning by domain. Dependencies: DDD-derived bounded context decisions. Next step: draft shared terms and domain-specific overrides. First artifact: PublishedLanguage seed glossary.

### 10.3 Architecture and Design

**Schema-home and responsibility-root reconciliation.** Priority: High. Why: Directory Rules require path decisions to be checked against ADRs and current repo evidence. Dependencies: repo inspection, Directory Rules, ADR review. Next step: inspect actual repo schema and contract homes. First artifact: SchemaHomeDecision or drift-register entry.

**Governed API minimal contract.** Priority: High. Why: public map, drawer, Focus Mode, and review surfaces need a governed interface before UI polish. Dependencies: EvidenceRef resolution, finite outcomes, source-policy checks. Next step: draft a no-network OpenAPI-like contract. First artifact: Mock governed API contract and fixtures.

**Map artifact manifest wave.** Priority: Medium. Why: PMTiles, COGs, GeoParquet, and styles need traceability and release linkage. Dependencies: EVD attestation, VAL validators, MAP manifest entries. Next step: define minimum fields for LayerManifest, TileArtifactManifest, and MapReleaseManifest. First artifact: manifest schema bundle with examples.

### 10.4 Implementation

**No-network hydrology proof slice.** Priority: High. Why: it proves lifecycle, evidence, catalog, release, map, and drawer behavior without broad sensitive exposure. Dependencies: source roles, fixtures, validators, policy gates, release manifest. Next step: build synthetic or public-safe fixtures. First artifact: HUC12 + observation + NFHL-context fixture pack.

**PMTiles attestation validator.** Priority: High. Why: static map artifacts are likely central to public delivery and need integrity checks. Dependencies: sidecar schema, root_hash/spec_hash, proof strategy, release gate. Next step: implement schema-only validator with negative fixtures. First artifact: pmtiles_sidecar.schema.json and validation report fixtures.

**Governed AI MockAdapter proof.** Priority: Medium. Why: model runtime should not be introduced before evidence and citation validation contracts are stable. Dependencies: EvidenceBundle fixture, citation validator, finite response envelope. Next step: create no-network MockAdapter tests. First artifact: runtime_response_envelope fixture set.

### 10.5 Domain Deepening

**Habitat-fauna public-safe occurrence assignment.** Priority: High. Why: it tests biodiversity sensitivity, geoprivacy, habitat evidence, map explanation, and Focus Mode abstention. Dependencies: synthetic occurrence, habitat evidence, transform receipt, policy profile. Next step: define one fixture record and drawer payload. First artifact: public-safe occurrence assignment proof pack.

**Soil/agriculture material-change lane.** Priority: Medium. Why: CDL and PLANTS watchers can prevent noisy reruns and prove proposed-work routing. Dependencies: sidecar schema, thresholds, county geometry, rights verification. Next step: create sidecar fixtures and materiality tests. First artifact: CDL sidecar and PROPOSED_WORK_RECORD fixture.

**Hazards/atmosphere knowledge-character lane.** Priority: Medium. Why: it exercises observed/modeled/regulatory/operational distinctions and the no-emergency-alert boundary. Dependencies: source role vocabulary, freshness state, hazard payload rules. Next step: build a mixed knowledge-character fixture set. First artifact: hazards Evidence Drawer example pack.

### 10.6 Verification Needs

**Mounted repo evidence pass.** Priority: High. Why: current implementation maturity, paths, tests, workflows, and package managers remain UNKNOWN. Dependencies: access to repo checkout or connector evidence. Next step: inspect root folders, ADRs, workflows, schema homes, policies, tests, and release objects. First artifact: RepoEvidenceReport.

**External-source rights and cadence pass.** Priority: High. Why: source activation must fail closed without rights, cadence, and endpoint facts. Dependencies: source-currentness backlog. Next step: verify priority sources and record evidence date. First artifact: SourceRightsDecision matrix.

**Package/version verification pass.** Priority: Medium. Why: map, PMTiles, AI, and attestation tooling facts are unstable. Dependencies: package manager and implementation plan. Next step: verify official versions and dependency licenses. First artifact: VersionPinReview note.

### 10.7 Missing Evidence

**Actual CI and validator behavior.** Priority: High. Why: the corpus proposes many gates but this pass did not run them. Dependencies: mounted repo and test runner. Next step: run existing baseline tests and inspect validation reports. First artifact: ValidationRunReceipt.

**Current release and rollback objects.** Priority: High. Why: publication truth requires release manifests and rollback targets. Dependencies: repo evidence. Next step: inspect release/proof/receipt/catalog folders or their equivalents. First artifact: ReleaseObjectInventory.

**Steward and reviewer assignments.** Priority: Medium. Why: sensitive domains need real review roles. Dependencies: policy profile definitions and organizational decisions. Next step: record role placeholders and unknowns. First artifact: StewardReviewBacklog.

### 10.8 Thin-Slice and Pilot Opportunities

**First pilot: hydrology Evidence Drawer proof.** Priority: High. Why: demonstrates source role, temporal observation, regulatory context, and map explanation. Dependencies: no-network fixtures, governed API contract. Next step: create click-to-drawer mock flow. First artifact: HydrologyDrawerFixture.

**Second pilot: PMTiles proof gate.** Priority: High. Why: map artifact integrity is central and testable without live sources. Dependencies: sidecar schema and validator. Next step: validate one good and three bad sidecars. First artifact: PMTilesAttestationTestPack.

**Third pilot: habitat-fauna sensitive release.** Priority: Medium. Why: shows public-safe biodiversity publication without exact sensitive geometry. Dependencies: geoprivacy policy and transform receipt. Next step: create a redacted occurrence assignment fixture. First artifact: HabitatFaunaPublicSafeReleaseFixture.

**Fourth pilot: governed AI abstention.** Priority: Medium. Why: proves that Focus Mode can refuse unsupported or policy-denied answers. Dependencies: MockAdapter and citation validator. Next step: implement answer/abstain/deny/error examples. First artifact: FocusModeFiniteOutcomeFixtures.


## 11. Open Questions and Verification Backlog

### 11.1 Evidence Questions

What minimum fields make an EvidenceBundle sufficient for ordinary public claims, sensitive-domain claims, and high-consequence releases? How should EvidenceRef resolution behave when a referenced bundle exists but is stale, restricted, superseded, or only partially supports a requested claim? Which source families require source-role subtypes beyond the current shorthand in the corpus? How should conflicting evidence bundles be represented without collapsing them into one consensus claim? What counts as enough evidence for a public map popup versus a Focus Mode answer versus a formal published claim?

### 11.2 Design Questions

Where should KFM draw the final boundary among contracts, schemas, jsonschema, policies, and compatibility roots in a live repository? Which trust-bearing objects should be stored as canonical records, and which should be derived views over evidence and release state? How should layer manifests, tile artifact manifests, release manifests, STAC/DCAT/PROV records, and Evidence Drawer payloads reference one another without becoming duplicative? Should policy profiles be domain-specific, release-class-specific, or a small shared set with domain overrides? How much evidence and limitation text should be visible by default in public UI versus available through progressive disclosure?

### 11.3 Implementation-Proof Questions

Does the current KFM repository contain the roots, ADRs, schemas, contracts, policies, tests, apps, workflows, release objects, catalog records, or proof/receipt directories described in the corpus? Which parts are implemented, draft, deprecated, or absent? Which package manager and test runner govern the web/API/validator stack? Are there existing MapLibre, PMTiles, Evidence Drawer, Focus Mode, hydrology, habitat, or governed-AI components that should be preserved rather than replaced? What baseline tests pass today, and which trust gates are actually enforced rather than documented?

### 11.4 Source-Expansion Questions

Which hydrology, ecology, agriculture, atmosphere, hazards, and frontier-demography sources can be activated under verified rights and source-role decisions? What are the current terms, cadence, version, endpoint behavior, and attribution requirements for priority sources such as WBD/HUC data, USGS water services, NFHL, CDL, PLANTS, AirNow, Mesonet, MAIAC, FIRMS, SMAP, and biodiversity occurrence sources? Which sources require written consent, API keys, steward review, delayed publication, or restricted redistribution? How often should each source be reverified, and what release impact should stale verification have?

## 12. Appendix A — Master Idea Index Table

This appendix is built from `_ids.tsv`. It preserves the stable ID, title, category, status, and source-tag registry while adding a one-sentence essence, related idea cluster, and expansion direction for later planning.

| Idea ID | Title | Category | Status | One-sentence essence | Related ideas | Expansion direction |
|---|---|---|---|---|---|---|
| KFM-IDX-GOV-001 | Inspectable Claim as the Durable Public Unit | GOV — Doctrine and authority | CONFIRMED | Establishes a governance rule for inspectable claim as the durable public unit within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-GOV-002 | Truth Labels and Cite-or-Abstain as Operating Posture | GOV — Doctrine and authority | CONFIRMED | Establishes a governance rule for truth labels and cite-or-abstain as operating posture within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-GOV-003 | Responsibility-Root Directory Governance | GOV — Doctrine and authority | CONFIRMED | Establishes a governance rule for responsibility-root directory governance within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-GOV-004 | Implementation Evidence Boundary and No-Overclaim Rule | GOV — Doctrine and authority | CONFIRMED | Establishes a governance rule for implementation evidence boundary and no-overclaim rule within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-GOV-005 | Schema-Home and ADR Discipline | GOV — Doctrine and authority | CONFIRMED | Establishes a governance rule for schema-home and adr discipline within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-GOV-006 | Public Clients Stay Behind the Trust Membrane | GOV — Doctrine and authority | CONFIRMED | Establishes a governance rule for public clients stay behind the trust membrane within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-GOV-007 | Documentation as a Living Control Plane | GOV — Doctrine and authority | CONFIRMED | Establishes a governance rule for documentation as a living control plane within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-GOV-008 | Greenfield, No-Repo, and Public-Repo Sources Stay Source-Bounded | GOV — Doctrine and authority | PROPOSED | Establishes a governance rule for greenfield, no-repo, and public-repo sources stay source-bounded within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-SRC-001; KFM-IDX-VAL-006 | Use as review doctrine for every later file, claim, and path decision. |
| KFM-IDX-SRC-001 | Canonical Lifecycle from RAW to PUBLISHED | SRC — Source lifecycle | CONFIRMED | Defines a lifecycle or source-admission rule for canonical lifecycle from raw to published within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-SRC-002 | Source Descriptor and Source-Role Registry | SRC — Source lifecycle | CONFIRMED | Defines a lifecycle or source-admission rule for source descriptor and source-role registry within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-SRC-003 | Pre-RAW Events and Watcher Non-Publisher Posture | SRC — Source lifecycle | CONFIRMED | Defines a lifecycle or source-admission rule for pre-raw events and watcher non-publisher posture within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-SRC-004 | Promotion as Governed State Transition | SRC — Source lifecycle | CONFIRMED | Defines a lifecycle or source-admission rule for promotion as governed state transition within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-SRC-005 | Catalog Closure Before Public Release | SRC — Source lifecycle | CONFIRMED | Defines a lifecycle or source-admission rule for catalog closure before public release within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-SRC-006 | Material-Change Sidecars and PROPOSED_WORK_RECORD Outbox | SRC — Source lifecycle | PROPOSED | Defines a lifecycle or source-admission rule for material-change sidecars and proposed_work_record outbox within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-SRC-007 | Ecology Source-Health and Tile-Health Watchers | SRC — Source lifecycle | PROPOSED | Defines a lifecycle or source-admission rule for ecology source-health and tile-health watchers within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-SRC-008 | Currentness, Endpoint, Rights, and Version Reverification | SRC — Source lifecycle | NEEDS VERIFICATION | Defines a lifecycle or source-admission rule for currentness, endpoint, rights, and version reverification within KFM's evidence-first architecture. | KFM-IDX-EVD-004; KFM-IDX-VAL-003; KFM-IDX-POL-002 | Convert into source descriptors, watcher fixtures, and source-currentness checks. |
| KFM-IDX-EVD-001 | EvidenceBundle Outranks Generated Language and Rendered Artifacts | EVD — Evidence and provenance | CONFIRMED | Defines an evidence/provenance mechanism for evidencebundle outranks generated language and rendered artifacts within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-EVD-002 | EvidenceRef to EvidenceBundle Resolution | EVD — Evidence and provenance | CONFIRMED | Defines an evidence/provenance mechanism for evidenceref to evidencebundle resolution within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-EVD-003 | Source Ledger as Active Control Surface | EVD — Evidence and provenance | CONFIRMED | Defines an evidence/provenance mechanism for source ledger as active control surface within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-EVD-004 | RunReceipt, PromotionReceipt, and AIReceipt as Process Memory | EVD — Evidence and provenance | CONFIRMED | Defines an evidence/provenance mechanism for runreceipt, promotionreceipt, and aireceipt as process memory within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-EVD-005 | Deterministic Identity and spec_hash | EVD — Evidence and provenance | CONFIRMED | Defines an evidence/provenance mechanism for deterministic identity and spec_hash within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-EVD-006 | Signed Attestations and Provenance References | EVD — Evidence and provenance | PROPOSED | Defines an evidence/provenance mechanism for signed attestations and provenance references within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-EVD-007 | PMTiles Sidecar and Byte-Range Proof Evidence Carrier | EVD — Evidence and provenance | PROPOSED | Defines an evidence/provenance mechanism for pmtiles sidecar and byte-range proof evidence carrier within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-EVD-008 | Evidence, Receipts, Proofs, Catalogs, and Claims Stay Separate | EVD — Evidence and provenance | CONFIRMED | Defines an evidence/provenance mechanism for evidence, receipts, proofs, catalogs, and claims stay separate within KFM's evidence-first architecture. | KFM-IDX-GOV-001; KFM-IDX-VAL-002; KFM-IDX-MAP-006 | Convert into EvidenceBundle, receipt, sidecar, proof, and manifest schemas. |
| KFM-IDX-MOD-001 | Maps and GIS Layers as Representations Rather Than the World | MOD — Representation and semantics | CONFIRMED | Defines a representation or modeling rule for maps and gis layers as representations rather than the world within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-MOD-002 | Scale, CRS, Projection, Symbol, and Fitness-for-Use Decisions | MOD — Representation and semantics | CONFIRMED | Defines a representation or modeling rule for scale, crs, projection, symbol, and fitness-for-use decisions within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-MOD-003 | Valid, Source, Retrieval, Release, and Correction Time Separation | MOD — Representation and semantics | CONFIRMED | Defines a representation or modeling rule for valid, source, retrieval, release, and correction time separation within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-MOD-004 | Bitemporal and Time-Oriented State Modeling | MOD — Representation and semantics | CONFIRMED | Defines a representation or modeling rule for bitemporal and time-oriented state modeling within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-MOD-005 | Bounded Contexts and Ubiquitous Language for Domain Lanes | MOD — Representation and semantics | PROPOSED | Defines a representation or modeling rule for bounded contexts and ubiquitous language for domain lanes within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-MOD-006 | Assertion-First Domain Records Over Flattened Labels | MOD — Representation and semantics | PROPOSED | Defines a representation or modeling rule for assertion-first domain records over flattened labels within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-MOD-007 | Raster, Vector, Network, Field, 2.5D, and 3D Distinctions | MOD — Representation and semantics | CONFIRMED | Defines a representation or modeling rule for raster, vector, network, field, 2.5d, and 3d distinctions within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-MOD-008 | Knowledge-Character Labels for Observed, Modeled, Regulatory, and Interpretive Data | MOD — Representation and semantics | CONFIRMED | Defines a representation or modeling rule for knowledge-character labels for observed, modeled, regulatory, and interpretive data within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-003; KFM-IDX-INT-001 | Convert into domain vocabularies, temporal fields, and representation metadata. |
| KFM-IDX-POL-001 | Deny-by-Default for Sensitive Exact Locations | POL — Policy and sensitivity | CONFIRMED | Defines a policy or exposure-control rule for deny-by-default for sensitive exact locations within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-POL-002 | Rights and License Verification Gate | POL — Policy and sensitivity | CONFIRMED | Defines a policy or exposure-control rule for rights and license verification gate within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-POL-003 | Living-Person, DNA, and Genomic Restriction Posture | POL — Policy and sensitivity | CONFIRMED | Defines a policy or exposure-control rule for living-person, dna, and genomic restriction posture within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-POL-004 | Cultural, Archaeological, and Steward Review Controls | POL — Policy and sensitivity | CONFIRMED | Defines a policy or exposure-control rule for cultural, archaeological, and steward review controls within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-POL-005 | Rare Species Geoprivacy and Transform Receipts | POL — Policy and sensitivity | CONFIRMED | Defines a policy or exposure-control rule for rare species geoprivacy and transform receipts within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-POL-006 | Critical Infrastructure and Public-Safety Exposure Controls | POL — Policy and sensitivity | CONFIRMED | Defines a policy or exposure-control rule for critical infrastructure and public-safety exposure controls within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-POL-007 | Hazards Boundary: KFM Is Not an Emergency Alert System | POL — Policy and sensitivity | CONFIRMED | Defines a policy or exposure-control rule for hazards boundary: kfm is not an emergency alert system within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-POL-008 | Domain Policy Profiles and Access Roles | POL — Policy and sensitivity | PROPOSED | Defines a policy or exposure-control rule for domain policy profiles and access roles within KFM's evidence-first architecture. | KFM-IDX-VAL-002; KFM-IDX-EVD-004; KFM-IDX-APP-007 | Convert into policy profiles, access roles, denials, and transform receipts. |
| KFM-IDX-VAL-001 | No-Network Fixture-First Validation | VAL — Validation and release | CONFIRMED | Defines a validation or release-control rule for no-network fixture-first validation within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-VAL-002 | Validators Fail Closed on Schema, Policy, Rights, Sensitivity, and Release Violations | VAL — Validation and release | CONFIRMED | Defines a validation or release-control rule for validators fail closed on schema, policy, rights, sensitivity, and release violations within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-VAL-003 | CI Probes with Source Heads and Run Receipts | VAL — Validation and release | PROPOSED | Defines a validation or release-control rule for ci probes with source heads and run receipts within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-VAL-004 | Material-Change Watcher Validation | VAL — Validation and release | PROPOSED | Defines a validation or release-control rule for material-change watcher validation within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-VAL-005 | PMTiles Attestation Validator | VAL — Validation and release | PROPOSED | Defines a validation or release-control rule for pmtiles attestation validator within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-VAL-006 | Schema, Contract, Policy, and Directory Drift Detection | VAL — Validation and release | CONFIRMED | Defines a validation or release-control rule for schema, contract, policy, and directory drift detection within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-VAL-007 | Finite Failure Outcomes and Observability Records | VAL — Validation and release | CONFIRMED | Defines a validation or release-control rule for finite failure outcomes and observability records within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-VAL-008 | External Source Currentness and Rights Reverification Backlog | VAL — Validation and release | NEEDS VERIFICATION | Defines a validation or release-control rule for external source currentness and rights reverification backlog within KFM's evidence-first architecture. | KFM-IDX-SRC-008; KFM-IDX-EVD-004; KFM-IDX-POL-002 | Convert into no-network tests, validators, CI probes, and failure envelopes. |
| KFM-IDX-MAP-001 | Governed API as Trust Membrane | MAP — API/map/UI delivery | CONFIRMED | Defines a governed delivery or map-surface rule for governed api as trust membrane within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-MAP-002 | Resource Ontology and HTTP Contract Discipline | MAP — API/map/UI delivery | CONFIRMED | Defines a governed delivery or map-surface rule for resource ontology and http contract discipline within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-MAP-003 | MapLibre as Downstream 2D Renderer | MAP — API/map/UI delivery | CONFIRMED | Defines a governed delivery or map-surface rule for maplibre as downstream 2d renderer within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-MAP-004 | Tiles, PMTiles, COGs, GeoParquet, and MVT/MLT as Rebuildable Artifacts | MAP — API/map/UI delivery | CONFIRMED | Defines a governed delivery or map-surface rule for tiles, pmtiles, cogs, geoparquet, and mvt/mlt as rebuildable artifacts within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-MAP-005 | Layer, Style, TileArtifact, and MapRelease Manifests | MAP — API/map/UI delivery | PROPOSED | Defines a governed delivery or map-surface rule for layer, style, tileartifact, and maprelease manifests within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-MAP-006 | Evidence Drawer and Focus Mode as Trust-Visible Surfaces | MAP — API/map/UI delivery | CONFIRMED | Defines a governed delivery or map-surface rule for evidence drawer and focus mode as trust-visible surfaces within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-MAP-007 | Story Nodes and Review Surfaces | MAP — API/map/UI delivery | PROPOSED | Defines a governed delivery or map-surface rule for story nodes and review surfaces within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-MAP-008 | Client Verification of Released Map Artifacts | MAP — API/map/UI delivery | PROPOSED | Defines a governed delivery or map-surface rule for client verification of released map artifacts within KFM's evidence-first architecture. | KFM-IDX-GOV-006; KFM-IDX-EVD-002; KFM-IDX-VAL-005 | Convert into governed API contracts, manifests, drawer payloads, and map proof gates. |
| KFM-IDX-INT-001 | Spatial Analysis as Interpretation, Not Root Truth | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for spatial analysis as interpretation, not root truth within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-INT-002 | Indicators and Planning Support Need Declared Assumptions | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for indicators and planning support need declared assumptions within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-INT-003 | Machine Learning Outputs Remain Derivative | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for machine learning outputs remain derivative within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-INT-004 | Field Capture and Remote Sensing as Candidate Evidence | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for field capture and remote sensing as candidate evidence within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-INT-005 | 2.5D and Full 3D Are Not Interchangeable | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for 2.5d and full 3d are not interchangeable within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-INT-006 | Web Scraping and External Feed Acquisition Need Drift Control | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for web scraping and external feed acquisition need drift control within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-INT-007 | Bounded AI/RAG Synthesis with Citation Validation | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for bounded ai/rag synthesis with citation validation within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-INT-008 | Participatory, Equity, and Scenario Decision Support | INT — Interpretation and planning | CONFIRMED | Defines an interpretive-use rule for participatory, equity, and scenario decision support within KFM's evidence-first architecture. | KFM-IDX-EVD-001; KFM-IDX-MAP-006; KFM-IDX-VAL-007 | Convert into bounded analysis, AI, indicator, and scenario acceptance criteria. |
| KFM-IDX-APP-001 | Hydrology Proof Lane | APP — Applied domain lanes | PROPOSED | Identifies an applied KFM lane or pilot for hydrology proof lane within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |
| KFM-IDX-APP-002 | Habitat-Fauna Public-Safe Occurrence Assignment Thin Slice | APP — Applied domain lanes | PROPOSED | Identifies an applied KFM lane or pilot for habitat-fauna public-safe occurrence assignment thin slice within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |
| KFM-IDX-APP-003 | Ecology Source-Watcher Operational Slice | APP — Applied domain lanes | PROPOSED | Identifies an applied KFM lane or pilot for ecology source-watcher operational slice within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |
| KFM-IDX-APP-004 | Soil, Agriculture, CDL, PLANTS, and Landcover Material-Change Lane | APP — Applied domain lanes | PROPOSED | Identifies an applied KFM lane or pilot for soil, agriculture, cdl, plants, and landcover material-change lane within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |
| KFM-IDX-APP-005 | Atmosphere and Hazards Knowledge-Character Separation | APP — Applied domain lanes | CONFIRMED | Identifies an applied KFM lane or pilot for atmosphere and hazards knowledge-character separation within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |
| KFM-IDX-APP-006 | Roads, Rail, Trade, Settlements, Infrastructure, and Geology Boundary Discipline | APP — Applied domain lanes | CONFIRMED | Identifies an applied KFM lane or pilot for roads, rail, trade, settlements, infrastructure, and geology boundary discipline within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |
| KFM-IDX-APP-007 | People, Genealogy, DNA, Land, and Archaeology Sensitive Assertion Lanes | APP — Applied domain lanes | CONFIRMED | Identifies an applied KFM lane or pilot for people, genealogy, dna, land, and archaeology sensitive assertion lanes within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |
| KFM-IDX-APP-008 | Frontier-Demography and Economy County-Year Panel Concept | APP — Applied domain lanes | PROPOSED | Identifies an applied KFM lane or pilot for frontier-demography and economy county-year panel concept within KFM's evidence-first architecture. | KFM-IDX-SRC-001; KFM-IDX-EVD-002; KFM-IDX-VAL-001 | Convert into small proof lanes and prioritized domain pilots. |

## 13. Appendix B — Source Contribution Matrix and Filename-to-Short-Tag Mapping

This appendix records the Phase 1 short tags used throughout the dossier. The contribution column summarizes how the source was used in synthesis; the limitation column prevents source flattening.

| Short tag | Filename | Status / length signal | Contribution | Limitation |
|---|---|---|---|---|
| [Implementation Reference] | `# Kansas Frontier Matrix Implementation Reference.pdf` | READABLE; 20 pages | Source contribution recorded in Phase 1 and synthesized in Phase 2. | Does not by itself prove current live repository behavior. |
| [GIS Primer] | `a-primer-of-gis-fundamental-geographic-and-cartographic-concepts.pdf` | READABLE; 321 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Advanced SQL] | `Advanced-SQL-Concepts.pdf` | READABLE; 112 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [AI Python] | `AI_Concepts_Using_Python.pdf` | READABLE; 435 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Archaeological 3D GIS] | `Archaeological 3D GIS.pdf` | READABLE; 177 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Web APIs] | `Designing Great Web APIs.pdf` | READABLE; 45 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Temporal SQL] | `developing-time-oriented-database-applications-in-sql.pdf` | READABLE; 528 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Directory Rules] | `Directory Rules.pdf` | READABLE; 22 pages | Governing doctrine, build posture, lifecycle law, or control-plane vocabulary. | Does not by itself prove current live repository behavior. |
| [DDD Reference] | `Domain-Driven Design Reference.pdf` | READABLE; 59 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [ArcGIS Environmental] | `Earth, Space, and Environmental Science Explorations with ArcGIS Pro ed2.pdf` | READABLE; 141 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Urban GIS] | `GIS in Sustainable Urban Planning and Management.pdf` | READABLE; 365 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Web Scraping Java] | `instant-web-scraping-with-java.pdf` | READABLE; 72 pages | Technical vocabulary and method support; KFM adoption remains governed synthesis. | Does not prove KFM implementation; adaptation requires KFM contracts and validation. |
| [Greenfield Building Plan] | `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf` | READABLE; 28 pages | Governing doctrine, build posture, lifecycle law, or control-plane vocabulary. | Does not by itself prove current live repository behavior. |
| [Pipeline Manual] | `Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf` | READABLE; 30 pages | Governing doctrine, build posture, lifecycle law, or control-plane vocabulary. | Does not by itself prove current live repository behavior. |
| [Agriculture] | `KFM_Agriculture_Domain_Implementation_Dossier_REVISED_2026-04-21.pdf` | READABLE; 48 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Archaeology Plan] | `KFM_Archaeology_Architecture_Plan_PDF_Only.pdf` | READABLE; 51 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Atmosphere Air] | `KFM_Atmosphere_Air_PDF_Only_Architecture_Report_2026-04-21.pdf` | READABLE; 52 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Pass 19] | `KFM_Components_Pass_19_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` | READABLE; 54 pages | Prior cumulative synthesis and continuity baseline; used as lineage and corroboration. | Continuity source; does not outrank original evidence or current repo proof. |
| [KFM Encyclopedia] | `kfm_encyclopedia.pdf` | READABLE; 82 pages | Governing doctrine, build posture, lifecycle law, or control-plane vocabulary. | Does not by itself prove current live repository behavior. |
| [Fauna] | `KFM_Fauna_Architecture_PDF_Only_Report.pdf` | READABLE; 37 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Flora] | `KFM_Flora_Architecture_PDF_Only_Implementation_Blueprint.pdf` | READABLE; 36 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Geology Resources] | `KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_2026-04-21.pdf` | READABLE; 42 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Governed AI Ledger] | `KFM_Governed_AI_Extended_Pro_Source_Ledger_PDF_Only_Architecture_Report_2026-04-20.pdf` | READABLE; 36 pages | Governed AI, runtime, Focus Mode, and evidence-bound response posture. | Does not by itself prove current live repository behavior. |
| [Habitat] | `kfm_habitat_architecture_pdf_only_blueprint_2026-04-21.pdf` | READABLE; 28 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Habitat Fauna Thin Slice] | `KFM_Habitat_Fauna_Thin_Slice_Extended_Pro_Blueprint.pdf` | READABLE; 20 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Hazards] | `kfm_hazards_extended_pro_pdf_only_blueprint.pdf` | READABLE; 26 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Hydrology] | `KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf` | READABLE; 43 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [MapLibre Operating Manual] | `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf` | READABLE; 22 pages | Source contribution recorded in Phase 1 and synthesized in Phase 2. | Does not by itself prove current live repository behavior. |
| [Pass 18] | `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` | READABLE; 509 pages | Prior cumulative synthesis and continuity baseline; used as lineage and corroboration. | Continuity source; does not outrank original evidence or current repo proof. |
| [People DNA Land] | `KFM_People_Genealogy_DNA_Land_Ownership_Architecture_Blueprint.pdf` | READABLE; 30 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Roads Rail Trade] | `KFM_Roads_Rail_Trade_Routes_PDF_Only_Architecture_Plan_2026-04-21.pdf` | READABLE; 35 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Settlements Infrastructure] | `kfm_settlements_infrastructure_extended_pro_plan_2026-04-21.pdf` | READABLE; 43 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Soil] | `kfm_soil_architecture_extended_pro_pdf_only_report.pdf` | READABLE; 25 pages | Domain-lane architecture, sensitivity posture, source-role patterns, and proof-slice candidates. | Planning lineage only unless current repo evidence confirms files, tests, and runtime. |
| [Whole UI AI] | `KFM_Whole_UI_Governed_AI_Expansion_Report.pdf` | READABLE; 23 pages | Governed AI, runtime, Focus Mode, and evidence-bound response posture. | Does not by itself prove current live repository behavior. |
| [Master MapLibre Atlas] | `Master MapLibre Components-Functions-Features.pdf` | READABLE; 554 pages | Prior cumulative synthesis and continuity baseline; used as lineage and corroboration. | Continuity source; does not outrank original evidence or current repo proof. |
| [New Ideas 5-10] | `New Ideas 5-10-26.pdf` | READABLE; 319 pages | Operational expansion pressure, watchers, attestation, or material-change proposals. | Version-sensitive and operationally current facts require reverification. |
| [New Ideas 5-15] | `New Ideas 5-15-26.pdf` | READABLE; 220 pages | Operational expansion pressure, watchers, attestation, or material-change proposals. | Version-sensitive and operationally current facts require reverification. |
| [New Ideas 5-8] | `New Ideas 5-8-26.pdf` | READABLE; 321 pages | Operational expansion pressure, watchers, attestation, or material-change proposals. | Version-sensitive and operationally current facts require reverification. |
| [Ollama Ubuntu] | `Ollama & Ubuntu Information.pdf` | READABLE; 66 pages | Governed AI, runtime, Focus Mode, and evidence-bound response posture. | Does not by itself prove current live repository behavior. |


## 14. Appendix C — Expansion Backlog by Priority

| Priority | Backlog item | Primary category | First artifact | Verification / rollback note |
|---|---|---|---|---|
| High | Mounted repo evidence pass | GOV / VAL | RepoEvidenceReport | Do not promote implementation claims until repo, tests, workflows, and artifacts are inspected. |
| High | Schema-home and Directory Rules reconciliation | GOV / VAL | SchemaHomeDecision or drift-register entry | If repo conflicts with doctrine, record drift or create ADR before adding files. |
| High | Hydrology proof lane | APP / SRC / EVD / MAP | HUC12 + observation + regulatory-context fixture pack | Keep no-network until source rights and endpoints are verified. |
| High | Source-currentness and rights backlog | SRC / POL / VAL | SourceCurrentnessReport | Deny activation when rights, cadence, or endpoint behavior is stale or unknown. |
| High | PMTiles attestation validator | EVD / MAP / VAL | PMTiles sidecar schema and validator fixtures | Start with schema/root-hash checks; add signatures and byte-range proofs later. |
| High | Object-family map | EVD / GOV | Trust Object Family Map | Prevent receipts, proofs, catalogs, releases, and claims from collapsing. |
| High | Habitat-fauna public-safe occurrence assignment | APP / POL | Redacted occurrence assignment fixture | Public exact geometry remains denied unless policy and review allow. |
| Medium | Governed API mock contract | MAP / INT | EvidenceRef-to-drawer mock API contract | No direct model, RAW, WORK, QUARANTINE, or canonical store access. |
| Medium | Governed AI MockAdapter proof | INT / EVD / VAL | Finite outcome and citation-validation fixtures | Keep local/Ollama or other model runtime out until adapter contract is proven. |
| Medium | CDL/PLANTS material-change watcher | SRC / APP / VAL | CDL sidecar and PROPOSED_WORK_RECORD fixtures | Watchers propose work only; publication remains gated. |
| Medium | Hazards/atmosphere knowledge-character fixture | MOD / POL / APP | Mixed observed/modeled/regulatory/operational payload pack | Include not-emergency-alert boundary and freshness states. |
| Medium | Evidence Drawer language guide | MAP / POL | Public-safe explanation patterns | Explain abstention, denial, generalized geometry, stale state, and withheld evidence. |
| Medium | Published-language glossary | MOD | Domain terms seed glossary | Use shared governance terms with domain-specific meanings where needed. |
| Medium | Frontier county-year panel concept note | APP / MOD / INT | FrontierPanelSourceMemo | Do not build flagship panel before source and geography-version proof. |
| Low | Story Node pilot | MAP / INT / POL | StoryManifest fixture | Use only governed payloads and preserve uncertainty and correction links. |
| Low | 3D / terrain admission checklist | MOD / INT / POL | 2.5D versus 3D comparison fixture | Use 3D only where evidence burden justifies it and sensitivity is handled. |
| Low | Package/version review | VAL / MAP | VersionPinReview note | Recheck official versions and licenses before pins or publication. |
| Low | Steward review backlog | POL / APP | StewardReviewBacklog | Required before culturally sensitive, archaeological, or sovereignty-relevant release. |


---

# KFM Components Pass 20 Part 2 — Idea Index, Category Atlas, and Expansion Dossier

*A detailed evidence-first synthesis of the attached source corpus.*

---

## 1. Title Page

**Title.** KFM Components Pass 20 Part 2 — Idea Index, Category Atlas, and Expansion Dossier.

**Subtitle.** A detailed evidence-first synthesis of the attached source corpus.

**Document type.** PDF-ready master reference manual; research atlas; expansion dossier.

**Date.** 2026-05-16.

**Source boundary statement.** The controlling source corpus for this document is exactly the two attached PDFs: `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (509 pages, the prior cumulative atlas with 500 persisted idea cards across 14 dependency-ordered categories) and `KFM_Components_Pass_19_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (54 pages, the prior cumulative normalization with 64 explicit ideas plus 20 indexed appendix entries, integrating three Pass 19 delta packets on environmental source-health probes, PMTiles attestation, and CDL/PLANTS source drift watchers). Their internal source ledgers — Pass 18's 40 PDFs and Pass 19's 38 PDFs — are reachable as lineage citations through the two attached documents, not as independent first-class sources here. Cumulative and duplicate sources within the two PDFs are treated as corroboration or as carry-forward lineage rather than separate ideas.

**Purpose statement.** Extract, normalize, categorize, develop, and prioritize the major ideas in the Pass 18 + Pass 19 corpus so KFM maintainers, source stewards, architecture reviewers, domain-lane leads, and implementation planners can plan later research, writing, architecture, validation, and implementation work without losing the evidence posture that the prior passes established. Pass 20 Part 2 is neither a code patch nor a publication approval; it is a durable idea index from which later work can build.

**Truth posture key.**

- **CONFIRMED** — directly supported by the two attached PDFs or by current-session artifact extraction (page counts, hashes, file presence).
- **PROPOSED** — synthesis, recommendation, design direction, or organizing interpretation consistent with the attached evidence but not settled by it alone, and not verified in an implementation.
- **NEEDS VERIFICATION** — checkable but not yet checked strongly enough in this session to act as fact; usually depends on a mounted live repository, runtime, CI dashboard, or external source page.
- **UNKNOWN** — not supported strongly enough by the corpus to be treated as established; typically current external status, tool versions, endpoint behavior, or repository implementation maturity that the corpus does not prove.

**Intended audience.** KFM maintainers; source stewards; architecture reviewers; domain-lane leads (hydrology, habitat, fauna, flora, soil, agriculture, geology, atmosphere, hazards, roads/rail/trade, settlements/infrastructure, archaeology, people/genealogy/DNA/land); implementation planners; research editors; evidence-governance reviewers.

**Current-session evidence boundary.** This pass did not inspect a mounted live KFM repository, runtime logs, CI dashboards, deployment configurations, or current external-source status pages. Implementation-layer claims — file presence, route names, DTO shapes, runtime behavior, test results, branch state, package versions, external-feed cadence and rights — remain **UNKNOWN** unless explicitly carried forward as doctrine from the attached PDFs. The two prior passes already record this boundary; Pass 20 Part 2 preserves it without inflation.

**Evidence-first | map-first | time-aware | cite-or-abstain | fail-closed | policy-aware | auditable | reversible.**

---

## Contents

1. Title Page
2. Executive Determination
3. Source Synthesis Report
4. Structural Rationale
5. Master Category Map
6. Detailed Idea Chapters by Category
7. Cross-Cutting Themes
8. Overlaps, Contradictions, and Gaps
9. Weakly Supported, Ambiguous, or Excluded Material
10. Expansion Agenda
11. Open Questions and Verification Backlog
12. Appendix A — Master Idea Index Table
13. Appendix B — Source Contribution Matrix
14. Appendix C — Expansion Backlog by Priority

---

## 2. Executive Determination

**CONFIRMED.** The Pass 18 + Pass 19 corpus is, in substance, the cumulative governance architecture of the Kansas Frontier Matrix as a governed, evidence-first, map-first, time-aware spatial knowledge and publication system. Its center of gravity is not any single map, not any single AI assistant, not any specific domain dataset, and not a conventional data warehouse. What recurs across both passes is a trust membrane composed of source admission, evidence resolution, policy and sensitivity review, validation, catalog closure, release, governed API exposure, map rendering, Evidence Drawer explanation, Focus Mode interpretation, correction, and rollback. Pass 18 documented this membrane through 500 persisted idea cards distributed across 14 dependency-ordered categories. Pass 19 abstracted those cards into 64 explicit ideas plus 20 indexed appendix entries while retaining the category structure and adding three operational packets. Pass 20 Part 2 inherits this consolidated view.

**CONFIRMED.** Pass 19 is the immediate baseline. It records a normalized atlas keyed to `P19-XXX-NNN` identifiers, with explicit lineage to Pass 18's idea-card population and to the three delta packets on environmental probes (New Ideas 5-8-26), PMTiles attestation (New Ideas 5-10-26), and CDL/PLANTS source drift watchers (New Ideas 5-15-26). Pass 20 Part 2 does not restart the atlas. It preserves the 14-category map, reuses the canonical baseline ID format `KFM-IDX-<CAT>-<NNN>` that Pass 18 cards already reference, and develops each normalized idea in fuller polished prose while keeping the cross-references intact.

**PROPOSED.** The strongest synthesis-level Pass 19 → Pass 20 delta is *operational proof pressure*. The three Pass 19 packets converged on a coherent set of next implementation moves: environmental feeds become source-health and tile-health probes with signed receipts; PMTiles become signed, hashed, byte-range-verifiable artifacts with sidecars and Bao proofs; CDL/PLANTS/SSURGO/Air feeds become material-change watcher candidates whose output enters `WORK_CANDIDATE` rather than publishing directly. Together these three packets move KFM from broad evidence doctrine toward testable source-change governance and verifiable artifact integrity. Pass 20 Part 2 sharpens this direction into a concrete expansion agenda anchored by a paired ecology-watch + PMTiles-attestation proof package.

**CONFIRMED.** The 14 categories in this dossier — `DOC`, `REP`, `SRC`, `MOD`, `EVD`, `POL`, `VAL`, `ANA`, `FIE`, `REL`, `API`, `MAP`, `UIX`, `PLN` — are derived from the corpus itself, not imposed. Pass 18 already arrived at this dependency order through Phase 4 of its build, and Pass 19 retained it intact because the new packets deepen rather than reshape the structure. Pass 20 Part 2 keeps this category map for the same reason: the new material does not invalidate the categories; it sharpens source admission, evidence, validation, release, map artifacts, and operational planning within them.

**UNKNOWN.** Current implementation maturity remains unresolved. Several attached domain reports cited inside the Pass 19 ledger were produced in no-mounted-repo contexts. One implementation reference within Pass 18's source ledger reports prior connector-based evidence of a public repository surface. Because this pass did not inspect the live repository, that public-repo report is treated as lineage and a verification prompt, not as current implementation proof. Pass 20 Part 2 follows the same evidence boundary that Pass 18 and Pass 19 already set: doctrine is asserted confidently when supported; implementation maturity, route names, DTOs, runtime behavior, deployment claims, branch state, and test results remain bounded.

**PROPOSED.** Pass 20 Part 2 is meant to function as a working atlas — a durable reference and planning document. It states the controlling source corpus, records category logic, develops the 64+ normalized ideas in prose with truth labels, captures the cross-cutting tensions and gaps, identifies weakly-supported material, and translates the merged Pass 18 + Pass 19 view into a prioritized expansion agenda with named first proofs. It is explicitly not a code patch, not a repo claim, not a publication approval, and not a substitute for live-repo conformance verification.

### 2.1 Standing assumptions

The reader should know the following assumptions, all consistent with the Pass 18 and Pass 19 evidence boundary:

1. **The corpus is two PDFs.** Citations look like `[Pass 18]` and `[Pass 19]`. Where a Pass 19 idea internally cites domain blueprints or technical references, those are reachable through Pass 19's appendix B; Pass 20 Part 2 does not promote them to first-class sources.
2. **The 14-category map is stable.** Pass 18 derived it; Pass 19 retained it; the three delta packets fit inside it; Pass 20 Part 2 retains it.
3. **`KFM-IDX-<CAT>-<NNN>` is the canonical ID format.** Pass 18 cards already link back to baseline `KFM-IDX-XXX-NNN` references; Pass 19 used a `P19-XXX-NNN` namespace as a pass-internal convention. Pass 20 Part 2 adopts `KFM-IDX-<CAT>-<NNN>` and records the `P19-XXX-NNN` lineage inside each entry's source attribution.
4. **Lineage is corroboration, not duplication.** When Pass 18 and Pass 19 both support an idea, they are listed as `[Pass 18; Pass 19]`. When only one supports it (typically because the idea entered with a Pass 19 delta packet), only that tag appears.
5. **Doctrine confidence is decoupled from implementation confidence.** Doctrine can be CONFIRMED in the corpus while implementation remains UNKNOWN. This is the core epistemic distinction the two prior passes are asking Pass 20 Part 2 to preserve.

### 2.2 Determination table

| Determination area | Status | Result |
|---|---|---|
| Corpus center of gravity | CONFIRMED | Governed, evidence-first, map-first, time-aware spatial knowledge and publication architecture. |
| Dominant idea family | CONFIRMED | Trust membrane: source admission → modeling → evidence → policy → validation → analysis → release → API → map → UI → planning. |
| Pass 18 → Pass 19 delta | CONFIRMED (lineage) | 500 idea cards normalized into 64 entries + 20 indexed appendix items; 8 cross-cutting themes expanded to 10; three delta packets integrated. |
| Pass 19 → Pass 20 Part 2 delta | PROPOSED | Adopt canonical `KFM-IDX-<CAT>-<NNN>` IDs; re-prose each idea at 250–500 words; surface latent Pass 18 detail; sequence the expansion agenda with explicit dependencies. |
| Category system | CONFIRMED | 14-category dependency order retained from Pass 18 / Pass 19. |
| Implementation claims | UNKNOWN | No current repo/runtime/CI inspection in this pass. Prior summaries remain lineage and require re-verification. |
| Best first implementation proof | PROPOSED | Paired no-network ecology watcher (CDL/PLANTS) + PMTiles sidecar validator, each fixture-first, with negative tests and `publication_denied` defaults. |

---

## 3. Source Synthesis Report

The Pass 20 Part 2 corpus is dominated by two cumulative-synthesis documents whose relationship to each other is itself the most important structural fact. Pass 18 [Pass 18] is the broad-base atlas: 509 pages, 500 persisted idea cards, 14 dependency-ordered categories, an internal source ledger of 40 PDFs, 8 cross-cutting themes, and an explicit Phase 5 schema for every idea card (stable ID, status, carry-forward state, normalized statement, detailed explanation, why-it-matters, related-ideas links, dependencies, tensions, expansion directions, open questions, future work, source attribution, and a phase self-check). Pass 19 [Pass 19] is the normalization pass: 54 pages, 64 explicit idea entries plus a 20-row indexed appendix, the same 14 categories, an expanded 10-theme cross-cutting set, an internal ledger of 38 PDFs (Pass 18's set plus the three Pass 19 delta packets), an expansion agenda EXP-001 through EXP-015, and an open-questions register. The two documents are not in tension with each other; they are stages of the same cumulative synthesis, with Pass 19 standing as Pass 18's most recent consolidation.

The relationship between the two passes can be characterized precisely. Pass 18 captured everything; Pass 19 normalized it. Pass 18's 500 cards include many EXPANDED carry-forwards linking to baseline `KFM-IDX-XXX-NNN` references, indicating that Pass 18 itself was already a re-statement of earlier passes. Pass 19's `P19-XXX-NNN` entries collapse the Pass 18 cards along thematic lines while preserving the structural distinctions Pass 18 had earned through its larger card population. This means Pass 19's entries are denser than Pass 18's cards but lose nothing essential, and Pass 20 Part 2 inherits both the breadth of Pass 18 (via Pass 19's lineage citations) and the discipline of Pass 19 (via its normalized 64-entry index).

### 3.1 Source families

Within the two attached PDFs, six source families recur. They appear here not as new first-class sources but as recurring patterns *within* the controlling Pass 18 + Pass 19 corpus.

1. **Cumulative-synthesis family.** Pass 18 itself, plus Pass 19, plus the Master MapLibre Components atlas cited inside both passes. These are prior indexing systems; they should be used as continuity baselines, not as ordinary topic sources.
2. **KFM doctrine and control-plane family.** Inside the Pass 18 / Pass 19 ledgers: Directory Rules, the Greenfield Building Plan, the Pipeline Living Implementation Manual, the Implementation Reference, the Encyclopedia, the MapLibre Operating Architecture manual, the Whole-UI / Governed-AI Expansion Report, and the Ollama/Ubuntu runtime guide. These govern *how* ideas may be adapted to KFM, not merely *what* the ideas are.
3. **Domain-lane blueprint family.** Hydrology, habitat, habitat-fauna thin slice, fauna, flora, soil, agriculture, geology, atmosphere/air, hazards, roads/rail/trade, settlements/infrastructure, archaeology, and people/genealogy/DNA/land. These are planning artifacts rather than current implementation proofs, and they cited heavily in Pass 18 and Pass 19 as both source roles and as sensitivity registries.
4. **Technical reference family.** GIS primer, environmental GIS with ArcGIS Pro, urban planning GIS, archaeological 3D GIS, Advanced SQL, temporal database design, Domain-Driven Design reference, web API design, Python AI concepts, web scraping. These supply vocabulary and methods; their content becomes PROPOSED when translated into KFM unless a KFM doctrine or domain report already adopted it.
5. **Pass 19 delta family.** The three New Ideas packets: 5-8-26 (environmental probes), 5-10-26 (PMTiles attestation), 5-15-26 (CDL/PLANTS/SSURGO/AirNow source drift). These contain the most operationally specific design pressure in the entire corpus, and they are where most Pass 19 → Pass 20 Part 2 expansion energy is concentrated.
6. **Artifact-extraction context.** File presence, page counts, and SHA-256 prefixes recorded in the Pass 18 and Pass 19 ledgers. These verify *that* the documents exist as the corpus claims, but they do not prove repo behavior, runtime status, or any external operational fact.

Within this layered structure, the most important family remains the doctrine / control-plane family. It governs how *all other* ideas can be adapted. Technical references supply vocabulary; domain blueprints supply lane-specific patterns; Pass 19 deltas supply operational pressure. None of those overrides doctrine; all of them are interpretable only through it.

### 3.2 Recurring ideas across the corpus

The Pass 18 + Pass 19 corpus is strikingly consistent on a small number of foundational claims. They appear in slightly different vocabularies across the doctrine, blueprint, and delta materials, but they converge on the same operating laws.

- **Evidence outranks generated language.** Every truth-bearing public surface — map popup, AI answer, dashboard cell, exported claim, Focus Mode synthesis — must resolve through `EvidenceRef` to a complete `EvidenceBundle` before exposure. Pass 18 establishes this as doctrine across DOC, EVD, API, MAP, UIX, and AI categories; Pass 19 reaffirms it as `P19-DOC-001` and `P19-EVD-001` and extends it into the PMTiles attestation flow.
- **Maps are downstream claim carriers, not truth stores.** MapLibre, PMTiles, COG, GeoParquet, MVT/MLT, vector indexes, and graph projections are all carriers of released artifacts; they cannot become source registries, policy authorities, or publication authorities. Pass 18 captures this through the MAP and API chapters; Pass 19 sharpens it through `P19-MAP-001` and the PMTiles operations material.
- **Source roles matter.** Regulatory archives, operational feeds, model products, imagery, community observations, occurrence aggregators, assessor records, and legal sources have non-interchangeable authority. Both passes refuse to allow `GBIF/eBird` occurrence data to stand in for legal-status authority, allow `NFHL` to stand in for observed flooding, or allow community-science observations to support public claims without review.
- **Public clients use governed interfaces, not canonical/internal stores.** RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET stores are internal; PUBLISHED artifacts are exposed only through governed APIs and released catalog records. This is the trust membrane.
- **Sensitive exact locations fail closed.** Archaeology, rare species, living-person/DNA/land, infrastructure, and steward-controlled occurrences are deny-by-default in public exposure. Generalization, suppression, staged access, and steward review are the alternatives, with transforms recorded as receipts.
- **Temporal support is first-class.** Valid time, observed time, source time, retrieval time, release time, transaction time, and correction time are distinct dimensions where material. Geography versions and class ontology versions are part of identity.
- **Release is a governed transition, not a file move.** Promotion changes release state only after gates pass; cron success and source updates are not release events.
- **Catalog, proof, and receipt objects are separate.** Catalog records describe; proof packs verify; receipts record process. None of them is truth on its own.
- **AI is interpretive.** Provider-neutral, model-replaceable, subordinate to evidence, bounded by finite outcome envelopes (`ANSWER`, `ABSTAIN`, `DENY`, `ERROR`). Focus Mode and other AI surfaces sit downstream of governed evidence flow.
- **Validation and rollback are part of truth.** Fixtures, negative tests, materiality gates, publication denial, and rollback targets are not operational afterthoughts; they are the difference between an artifact that can be trusted in public and one that cannot.

### 3.3 Strongest and weakest material

The corpus is strongest where it describes governance doctrine, responsibility boundaries, KFM object families, source-role separation, policy and sensitivity posture, map/renderer boundaries, planned domain-lane architectures, and the three operational packets' specific schemas (PMTiles sidecars, ecology watcher sidecars, environmental probe receipts). The doctrine layer is consistently CONFIRMED at the corpus level even when implementation is UNKNOWN.

The corpus is weakest where it implies current external status, package versions, live endpoint behavior, or repository presence without current verification. The New Ideas packets contain useful operational observations, but current-status statements about data feeds (GBIF, eBird, SMAP, MAIAC, FIRMS, AirNow, Mesonet), MapLibre and Cesium activity, and tool availability (Bao, cosign/DSSE, BLAKE3 implementations, freestiler-style ports) remain NEEDS VERIFICATION before any operational reliance. Many prior reports propose concrete paths; Directory Rules requires those paths to be checked against live repo conventions and ADRs before implementation.

### 3.4 Duplicate and overlap handling

Duplicates were handled as corroboration. Pass 18 and Pass 19 are cumulative passes and are treated as baselines. Domain reports cited inside each pass frequently repeat the no-repo inspection caveat and the schema-home ambiguity; that repetition strengthens the caution against overclaiming but does not create new implementation proof. The PMTiles attestation material appears in both New Ideas 5-8 and 5-10 within the Pass 19 ledger; it is normalized into one artifact-attestation idea family (`KFM-IDX-EVD-003`, `KFM-IDX-EVD-004`, `KFM-IDX-MAP-002`, `KFM-IDX-MAP-004`) rather than counted as separate doctrines. Cross-cutting themes from Pass 18 (8 themes) and Pass 19 (10 themes) overlap substantially; Pass 20 Part 2 merges them into a deduplicated 10-theme set in Section 7.

### 3.5 Source inventory notes

| Tag | Filename | Pages | Family | Hash prefix (where recorded) | Primary contribution to Pass 20 Part 2 |
|---|---|---|---|---|---|
| [Pass 18] | KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf | 509 | baseline_synthesis | (recorded internally per source) | 500 idea cards across 14 categories, 8 cross-cutting themes, 40-PDF internal source ledger, DDD-derived large-scale structure detail |
| [Pass 19] | KFM_Components_Pass_19_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf | 54 | cumulative_baseline | (recorded internally per source) | 64 normalized idea entries + 20 indexed appendix items, 10 cross-cutting themes, integration of three Pass 19 delta packets, expansion agenda EXP-001..015 |

No extraction failures. Both PDFs are text-extractable. No fonts garbled. No attachments. No embedded forms. Pass 18 was produced via pandoc/LaTeX; Pass 19 via python-docx/LibreOffice. Both render at standard 612×792 pt letter page size.

---

## 4. Structural Rationale

Pass 20 Part 2 retains the 14-category dependency order that Pass 18 derived and Pass 19 retained. The case for this structure rather than any alternative is straightforward and is made stronger by the convergence between the two prior passes.

KFM is a governed publication system. A public map layer, a governed API response, an AI explanation, a planning narrative, or an exported dataset is legitimate only after doctrine, representation, source admission, modeling, evidence, policy, validation, analysis, field/remote interpretation, catalog/release, API, and map-delivery concerns have been addressed in that order. Any ordering that puts maps before evidence, or evidence before policy, or release before validation, would reorder the trust membrane and would mismatch the structure of every domain blueprint cited in the Pass 18 / Pass 19 ledgers.

Organizing by file order, as a naive Phase 2 might do, would over-weight the accident of attachments and repeat the same domain reports one after another with little structural insight. Organizing by domain — hydrology, fauna, archaeology, roads, settlements, air, soil, agriculture — would hide the fact that all of these depend on the same trust spine and would create N parallel chapters where each one re-derives the same governance posture. Organizing by operational dependency, as Pass 18 and Pass 19 do, makes the invisible governance layers visible *before* the attractive downstream outputs (maps, AI, dashboards) appear. This is the correct epistemic ordering.

Pass 20 Part 2 keeps the 14-category map because the Pass 19 deltas did not introduce a fundamentally new category; they made several existing categories more operational. The source-drift watcher material belongs primarily to `SRC`, `VAL`, `ANA`, `REL`, and `API`. PMTiles attestation belongs primarily to `EVD`, `MAP`, `VAL`, and `REL`. Environmental source-health probes belong primarily to `SRC`, `VAL`, `ANA`, `POL`, and `MAP`. None of them claims a new top-level lane. They all instead deepen the existing lanes with concrete schemas, thresholds, fixtures, and gate conditions.

This structure also preserves the core KFM lifecycle invariant: `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`. In category terms this means: source admission and modeling appear before evidence and policy; evidence and policy before validation and release; release before API/map/UI exposure; planning only after the trust surface is visible. A category map that reversed any of these would risk inviting design that bypasses the lifecycle invariant.

---

## 5. Master Category Map

The 14 categories below are listed in dependency order. Each row records the category code, the canonical name, a short definition, why the category matters for KFM, its dominant subcategories within the corpus, and a brief role label (central, supporting, emerging, or application-layer).

| Code | Category | Short definition | Why it matters | Subcategories | Role |
|---|---|---|---|---|---|
| **DOC** | Doctrine, Truth Posture, and Responsibility Boundaries | How KFM decides what can be said, who owns a file or claim, and which surfaces may expose it. | Governs the root trust posture and which downstream ideas are admissible at all. | truth posture; responsibility roots; evidence boundary; watcher-as-non-publisher; shared governance kernel; responsibility layers | Central |
| **REP** | Geographic Representation, Scale, and Spatial Reference | How maps, geometries, projections, scale, 2D/3D views, and symbols become disciplined representations rather than neutral pictures. | Governs whether downstream artifacts can carry inspectable claims at all. | cartographic representation; scale and spatial reference; representation form separation; 3D / 2.5D humility | Central |
| **SRC** | Source Admission, Connectors, and External-Service Boundaries | How external data, APIs, watchers, packages, source descriptors, and connector behavior enter or fail to enter KFM. | Governs the intake edge where outside material first becomes accountable. | source descriptors; source-head checks; source-role registry; connectors and watchers; external service boundaries | Central |
| **MOD** | Data Modeling, Domain Semantics, Temporal Structure, and SQL | How KFM separates object families, domain contexts, time types, semantic versions, assertions, observations, and analytical tables. | Governs whether admitted material can be expressed without collapsing distinct epistemic types. | temporal structure; bounded contexts; geography versions; ontology drift; object-family separation | Central |
| **EVD** | Evidence, Provenance, Receipts, Identity, and Attestation | How `EvidenceRef`, `EvidenceBundle`, canonical hashes, receipts, signatures, and artifact proofs make claims inspectable. | Governs the inspectable substrate that every downstream public surface depends on. | EvidenceBundle closure; receipts; artifact attestation; streaming proofs; canonical hashes | Central |
| **POL** | Policy, Rights, Ethics, Sensitivity, and Public-Safety Controls | How rights, stewardship, exact-location sensitivity, source terms, cultural risk, living-person and DNA limits, and fail-closed exposure are enforced. | Governs whether and how a claim or layer can be exposed at all. | public-safe defaults; rights and consent; sensitive geometry; policy thresholds | Central |
| **VAL** | Validation, QA, Testing, Observability, and Reliability | How fixtures, negative tests, CI probes, schema gates, materiality tests, and observability keep derived products trustworthy. | Governs whether evidence and policy decisions are operational rather than ornamental. | materiality gates; CI probes; negative fixtures; publication gates; no-network dry runs | Central |
| **ANA** | Analysis, Indicators, Statistics, Machine Learning, and Model Interpretation | How indicators, thresholds, statistics, ML, environmental signals, and planning analysis remain interpretive derivatives. | Governs how analytical outputs are subordinated to evidence rather than promoted into truth. | interpretive derivatives; environmental signals; landcover drift; taxa drift; planning indicators | Supporting (large in corpus) |
| **FIE** | Field Capture, Remote Sensing, 3D, and Archaeological Interpretation | How field, drone, remote-sensing, 3D, and archaeology data are captured and interpreted with evidentiary humility. | Governs how visually persuasive 3D and remote-sensing material is prevented from becoming unqualified truth. | field capture; remote sensing; 3D archaeology; catalog normalization | Supporting / emerging |
| **REL** | Catalog Closure, Publication, Release, Rollback, and Recompile Discipline | How catalog records, release manifests, publication state, rollback targets, and recompile loops close the evidence chain. | Governs the boundary at which internal artifacts become public products. | catalog closure; promotion gates; artifact versioning; rollback; watcher lifecycle | Central |
| **API** | Governed API, Resource Ontology, HTTP, and Service Contracts | How resource contracts and finite envelopes expose governed resources while protecting canonical and internal stores. | Governs the trust membrane between clients and the system. | trust membrane; finite outcomes; design-first contracts; candidate envelopes | Central |
| **MAP** | Map Artifacts, Tiles, Raster/Vector Delivery, and Renderer Boundaries | How PMTiles, COGs, MVT/MLT, GeoParquet, styles, sidecars, CDN/Range behavior, and MapLibre delivery remain downstream carriers. | Governs whether the most visible KFM surface remains a carrier rather than an authority. | renderer boundary; PMTiles operations; artifact matrix; viewer verification; map trust states | Central |
| **UIX** | Trust-Visible UI, Evidence Drawer, Focus Mode, Story Nodes, and Review Surfaces | How the interface makes evidence, stale state, review state, policy, source, and AI boundaries visible to users. | Governs whether the user can see *why* a claim or layer is shown. | Evidence Drawer; Focus Mode; review surfaces; Story Nodes | Central (smaller) |
| **PLN** | Planning, Participation, Resilience, and Decision-Support Applications | How KFM supports planning and domain decisions without flattening evidence, equity, scenarios, or public-safety constraints. | Governs the application layer where the system meets the world it tries to support. | participatory planning; hazards/resilience; proof slices; expansion direction | Application / emerging |

### Category notes

**DOC** is central in both passes but smaller in card count than its importance suggests. Its 4–6 ideas govern everything else: cite-or-abstain, directory placement as governance boundary, truth labels as operational controls, implementation maturity as UNKNOWN without repo evidence, and (from Pass 18's DDD-derived material) the shared governance kernel and responsibility layers patterns.

**REP** is doctrinally central but appears in card form mostly through the GIS primer's communicative-representation framing and the 3D archaeology source's distinction between proper 3D models and 2.5D representations. The Pass 19 delta added geometry-version warnings (county boundary hashes) that elevate REP into a concrete operational concern.

**SRC** is one of the most operationally pressured categories in Pass 19. The three delta packets all live primarily here, since environmental probes, PMTiles intake hygiene, and CDL/PLANTS source drift are all questions about what is allowed across the intake edge.

**MOD** is the largest category in Pass 18 by absolute volume of source-supported card material because three of the most-cited references (DDD, temporal database, advanced SQL) feed it. Pass 19's normalization compressed this into 5 ideas, but the latent depth is significant.

**EVD** is the inspectable substrate. Pass 19's PMTiles attestation packet expanded EVD operationally with sidecar schemas, BLAKE3/Bao proof patterns, DSSE/cosign signing sketches, and validation gates.

**POL** is fewer ideas than its importance suggests; its 4 normalized ideas (public-safe defaults; rights as evidence; exact-location/living-person protection; thresholds as policy) appear across most domain blueprints as deny-by-default postures and as policy_id requirements.

**VAL** carries the operational weight of the trust membrane. The Pass 19 delta packets all add new VAL material: materiality gates, signed probe receipts, negative fixtures, publication denial conditions, and no-network dry runs.

**ANA** is the largest category in Pass 18 by card count (~59) because the AI Concepts source and the urban planning GIS source both feed it heavily. Pass 19 compressed this to 5 ideas with the understanding that ANA outputs remain interpretive derivatives over evidence.

**FIE** appears in both passes and is sharpened by the archaeological 3D GIS source. The Pass 19 normalization adds the field-and-remote-into-catalog-before-public-maps idea as a structural step.

**REL** carries the publication discipline and is one of the categories most reshaped by the Pass 19 PMTiles attestation delta — versioned filenames, root hashes, sidecars, and rollback targets all flow through REL.

**API** is the trust membrane. Pass 19 explicitly elevates finite outcome envelopes (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`) and `SourceIntakeRecord` as the candidate envelope for drift watchers.

**MAP** carries the renderer boundary. Pass 19 hardens it with PMTiles operations tests, the artifact matrix across COG/GeoParquet/PMTiles/STAC/DCAT/PROV, viewer verification gates, and explicit map trust states (NORMAL / STALE / DEGRADED / ESCALATE / QUARANTINE).

**UIX** carries the Evidence Drawer, Focus Mode, review surfaces, and Story Node concepts. Its card count is smaller in both passes, but each idea is structurally critical because UIX is where users either see or fail to see why a claim is presented.

**PLN** is the application/emerging layer. Pass 19 explicitly frames PLN-004 ("source-change governance plus artifact integrity is the strongest Pass 19 → Pass 20 expansion") as a planning synthesis claim, which Pass 20 Part 2 inherits as the highest-priority expansion lane.

---

## 6. Detailed Idea Chapters by Category

This section develops the major normalized ideas in full prose. Duplicate and near-duplicate material across Pass 18 and Pass 19 is merged. Each idea entry uses the requested fields, retains lineage to Pass 18 cards and Pass 19 entries through the source attribution line, and indicates status with explicit truth labels. The chapters proceed in the dependency order established in Section 4.

### 6.1 DOC — Doctrine, Truth Posture, and Responsibility Boundaries

#### Category overview

DOC is the root governance category. It contains the rules that decide what can be said, who owns a file or claim, which surfaces may expose it, and which subsequent ideas are admissible at all. It is structurally first because every later category — representation, source admission, modeling, evidence, policy, validation, analysis, field/remote interpretation, release, API, map, UI, planning — depends on doctrine being settled before its own decisions are interpretable. Although DOC has fewer ideas than ANA or REL in raw card count, its leverage on the system is among the highest. Pass 18 captured DOC through 5 idea cards in chapter 8.1 plus the cross-cutting themes that thread DOC into every other chapter; Pass 19 normalized DOC into four explicit entries plus two latent Pass 18 patterns (shared governance kernel; responsibility layers) that Pass 20 Part 2 surfaces here.

#### 6.1.1 Subcategories

- **Truth posture and public claims.** Cite-or-abstain as the controlling rule for public statements.
- **Responsibility roots and file homes.** Directory placement as governance boundary, not convenience labeling.
- **Truth labels and finite outcomes.** Status labels as operational controls rather than prose decoration.
- **Evidence boundary.** What counts as proof of implementation maturity, and what does not.
- **Shared governance kernel (latent in Pass 18).** A small explicit set of jointly-controlled governance objects shared across domain lanes.
- **Responsibility layers (latent in Pass 18).** Named layers (evidence, policy, catalog, release, API, UI, AI, operations) so cross-domain changes are evaluated against the layer they affect.

#### 6.1.2 Idea entries

##### KFM-IDX-DOC-001 — Cite-or-abstain is the controlling truth posture

**Status.** CONFIRMED. **Category/Subcategory.** DOC / Truth posture and public claims. **Lineage.** Pass 18 cross-cutting theme P18-XCT-001 and multiple DOC/EVD/API cards; Pass 19 P19-DOC-001.

**Normalized statement.** Every consequential KFM statement should either resolve to admissible evidence or abstain rather than manufacture unsupported certainty.

**Detailed explanation.** The Pass 18 + Pass 19 corpus frames KFM as an evidence-first publication system whose durable public unit is the inspectable claim. Pass 18 makes cite-or-abstain a repeated operating law across DOC, EVD, API, MAP, UIX, and AI chapters; Pass 19 reaffirms it as the first normalized DOC idea and threads it through the Evidence Drawer, Focus Mode, governed API envelopes, and PMTiles attestation gates. The rule applies to maps, AI text, dashboards, tiles, summaries, exports, and any other public surface. It does not require that every statement carry full provenance metadata in display; it requires that every consequential statement *can* be resolved through `EvidenceRef` to a complete `EvidenceBundle` when interrogated, and that statements which cannot are either withheld or marked as abstentions rather than smoothed into apparent certainty by generation pressure.

**Why it matters.** Cite-or-abstain is the firewall against persuasive but ungrounded public truth. Without it, fluent AI generation, attractive cartography, and confident dashboards will gradually substitute for the slower work of evidence resolution and policy review. With it, the system has a single rule that every public surface must answer to.

**Related ideas.** `KFM-IDX-EVD-001` (EvidenceRef → EvidenceBundle); `KFM-IDX-API-002` (finite outcome envelopes); `KFM-IDX-UIX-001` (Evidence Drawer); `KFM-IDX-UIX-002` (Focus Mode evidence-bounded).

**Dependencies.** EvidenceBundle schema; citation validator; release manifest; policy check.

**Tensions / limitations.** The corpus is rich in doctrine on this rule but repeatedly leaves implementation maturity UNKNOWN — there is no current-session proof that a runtime citation validator exists. Different claim classes also vary in what evidence is sufficient: some need source-specific citations, others can use aggregate evidence.

**Expansion directions.** Turn the rule into a runtime validator that rejects public statements lacking EvidenceRef closure. Define minimal and high-significance EvidenceBundle profiles. Build a fixture set with ANSWER / ABSTAIN / DENY / ERROR cases.

**Open questions.** Which claim classes may use aggregate evidence and which require source-specific citation? What is the abstention default in interactive UI surfaces (silence, placeholder text, "evidence pending" label)?

**Suggested future work.** Create a citation-validation fixture set tied to Focus Mode and Evidence Drawer payloads; specify the public abstention UI vocabulary.

##### KFM-IDX-DOC-002 — Directory placement is a governance boundary

**Status.** CONFIRMED. **Category/Subcategory.** DOC / Responsibility roots and file homes. **Lineage.** Pass 18 (Directory Rules cited as governing vocabulary throughout); Pass 19 P19-DOC-002.

**Normalized statement.** A file path in KFM is not a convenience label; it encodes ownership, responsibility root, lifecycle, and governance posture.

**Detailed explanation.** Directory Rules states explicitly that topic does not justify a root folder and that responsibility does. The Pass 18 ledger marks Directory Rules as governing vocabulary rather than synthesis target; Pass 19 retains that treatment. Schema-home conventions, lifecycle invariants, ADR requirements, drift handling, and the distinction between authority roots and compatibility roots are all first-class. Domain blueprints frequently propose paths inside their reports, but those paths remain PROPOSED until they have been checked against Directory Rules and live repository evidence. The rule prevents schema, policy, proof, source, release, and catalog definitions from splitting into parallel homes that silently diverge over time — the failure mode in which two competing schemas claim to define the same object family from different roots.

**Why it matters.** Directory placement is one of the most easily overlooked governance boundaries because it looks like file-system housekeeping. Treating it as governance prevents silent fragmentation of the trust membrane across competing schema homes and avoids cross-lane drift that is invisible until rollback or recompile is needed.

**Related ideas.** `KFM-IDX-REL-002` (promotion as governed state transition); `KFM-IDX-VAL-005` (no-network dry runs); `KFM-IDX-SRC-001` (SourceDescriptor); `KFM-IDX-DOC-005` (shared governance kernel).

**Dependencies.** Mounted repo inspection; ADRs for schema-home or root changes; drift register; path authority audit.

**Tensions / limitations.** Prior PDF-only domain blueprints inside the Pass 19 ledger sometimes propose different homes; one implementation reference inside the Pass 18 ledger reports a public repo while many other domain reports record no mounted repo. Until a current-session repo conformance scan is done, all proposed paths are PROPOSED.

**Expansion directions.** Turn proposed paths from Pass 19 idea entries (e.g. `tools/ingest/cdl_watch`, `tools/validators/validate_pmtiles_sidecar.py`, `data/catalog/stac/ecology/cdl`) into Directory Rules-compliant PR plans only after repo inspection.

**Open questions.** Which current repo roots are canonical versus compatibility roots? Which categories already have ADRs documenting their schema homes?

**Suggested future work.** Run EXP-009 (live repo conformance scan) before landing any PR derived from this dossier; produce a drift report mapping each proposed path to accepted / adapted / rejected.

##### KFM-IDX-DOC-003 — Truth labels are operational controls, not prose decoration

**Status.** CONFIRMED. **Category/Subcategory.** DOC / Truth labels and finite outcomes. **Lineage.** Pass 18 (truth labels woven through every card); Pass 19 P19-DOC-003.

**Normalized statement.** `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, `DENY`, `ABSTAIN`, and `ERROR` should govern behavior and exposure, not merely annotate text.

**Detailed explanation.** Pass 18 defines truth labels and finite outcome terms and uses them with discipline across all 500 cards. Pass 19 extends them into operational outputs: `SourceIntakeRecord` candidates carry a status; `DecisionEnvelope` objects carry an outcome; tile state envelopes carry `NORMAL` / `DEGRADED` / `ESCALATE` / `QUARANTINE`; PMTiles attestation gates carry `DENY` outcomes. The distinction matters because a label should determine *what the system does* — whether a claim can be rendered, reviewed, promoted, exported, or withheld — not merely *how the document reads*. A source-drift finding can be a `WORK_CANDIDATE` without being a public conclusion; an AI answer can `ABSTAIN` rather than improvise; an artifact missing a sidecar can `DENY` rather than be quietly published.

**Why it matters.** Truth labels as operational controls give the system a small, finite vocabulary in which validation, policy, release, API, and UI can agree. Without it, the same label could mean different things in prose, in code, and in the UI, and the system would lose its ability to act consistently on its own evidence posture.

**Related ideas.** `KFM-IDX-API-002` (finite outcome envelopes); `KFM-IDX-VAL-004` (publication gates deny missing proofs); `KFM-IDX-SRC-006` (CDL/PLANTS source-drift candidates).

**Dependencies.** Shared enums; schema validation; UI state mapping; policy rules; release manifest fields.

**Tensions / limitations.** Operational outcome labels and domain-state labels can be conflated if not modeled separately. `REVIEW_REQUIRED` is sometimes treated as an outcome and sometimes as a gate status; this needs to be resolved before code uses both.

**Expansion directions.** Define outcome enums distinct from domain operational states; specify the mapping from outcome to UI rendering; codify which outcomes are publishable in user-visible badges versus only in steward review consoles.

**Open questions.** How should `REVIEW_REQUIRED` differ from `ABSTAIN` in public UI? Is `STALE` an outcome or an operational state?

**Suggested future work.** Create a finite-outcome schema with a UI state-mapping table; test rendering for each outcome × user role.

##### KFM-IDX-DOC-004 — Implementation maturity remains UNKNOWN without current repo evidence

**Status.** CONFIRMED. **Category/Subcategory.** DOC / Evidence boundary. **Lineage.** Pass 18 (each card's "Implementation maturity: UNKNOWN" self-check); Pass 19 P19-DOC-004.

**Normalized statement.** Current repository maturity, route names, tests, workflows, source activations, dashboards, and runtime behavior must not be upgraded from PROPOSED to CONFIRMED without current-session implementation proof.

**Detailed explanation.** Many of the domain reports cited inside the Pass 18 and Pass 19 ledgers were produced in no-mounted-repo contexts. Their idea cards explicitly mark implementation maturity as UNKNOWN even when the doctrine they describe is confirmed by their source attribution. Pass 18 enforces this convention through a per-card phase self-check; Pass 19 retains it as a Section 8 contradiction (no-mounted-repo reports versus the prior Implementation Reference's public-repo summary). The safest synthesis is that prior repo evidence is lineage and must be re-verified in the current session. This rule is what protects Pass 20 Part 2 from inflating its own claims; it is also what makes the expansion agenda (EXP-009) coherent.

**Why it matters.** It protects KFM from false maturity claims that would make future correction harder. A claim that "the validator exists" turns into infrastructure expectations and into review behavior; if the claim is unsupported and the validator does not in fact exist, every downstream decision built on the claim is misaligned with reality.

**Related ideas.** `KFM-IDX-DOC-002` (Directory placement); `KFM-IDX-VAL-005` (no-network dry runs); `KFM-IDX-REL-004` (rollback targets).

**Dependencies.** Repo scan; tests; logs; workflow runs; release manifests; emitted receipts.

**Tensions / limitations.** The corpus contains both no-repo scans and a prior public-repo summary; this is a source-mode tension. Until a current-session conformance scan is done, both readings stand.

**Expansion directions.** Keep Pass 20 Part 2 as a synthesis and expansion dossier, not an implementation claim. Treat EXP-009 as the precondition for any PR derived from this dossier.

**Open questions.** What is the current branch, actual schema home, and CI workflow state in the live repository? Which proposed paths in Pass 19 entries already exist?

**Suggested future work.** Run EXP-009 first; produce a conformance report; treat its findings as the authoritative input to any subsequent PR plan.

##### KFM-IDX-DOC-005 — Shared governance kernel across bounded domain lanes

**Status.** PROPOSED. **Category/Subcategory.** DOC / Shared kernel. **Lineage.** Pass 18 card `KFM-P18-INV-188` (shared kernel pattern from DDD reference, page 38). Not promoted to a top-level Pass 19 entry; surfaced here because the operational pressure from Pass 19's three delta packets makes a shared kernel concrete (multiple lanes will use `SourceDescriptor`, `SourceIntakeRecord`, `DriftSummary`, `EvidenceBundle`, etc.).

**Normalized statement.** KFM should keep shared governance objects small, explicit, and jointly controlled across domain lanes rather than duplicating `EvidenceBundle`, `DecisionEnvelope`, receipts, and release objects per lane.

**Detailed explanation.** The DDD reference defines a Shared Kernel as a small subset of the domain model used by multiple bounded contexts, kept under joint stewardship and changed only by consultation. Pass 18's DOC chapter applies that pattern to KFM: hydrology, fauna, archaeology, roads, settlements, archaeology, people/DNA/land, and so on are all bounded contexts, but they share `EvidenceBundle`, `SourceDescriptor`, `PromotionDecision`, `ReleaseManifest`, and `PolicyDecision`. Pass 19's emergence of `SourceIntakeRecord`, `DriftSummary`, and the PMTiles `IntegrityEnvelope` is exactly the kind of expansion that requires the shared kernel to be explicit so each new envelope is added once and used consistently across lanes rather than re-invented per domain.

**Why it matters.** Without an explicit shared kernel, divergent lane-specific copies of the same governance object will emerge under the same name with subtly different fields, defeating the trust membrane.

**Related ideas.** `KFM-IDX-DOC-002` (Directory placement); `KFM-IDX-MOD-002` (bounded contexts); `KFM-IDX-API-001` (governed API); `KFM-IDX-API-004` (SourceIntakeRecord).

**Dependencies.** Core governance schema set; schema-home ADR; cross-domain CI; ADR process for kernel changes.

**Tensions / limitations.** A shared kernel can become too large and freeze domain lanes if it accumulates lane-specific fields. The DDD pattern explicitly warns against this.

**Expansion directions.** Define the minimum shared governance kernel (likely: `EvidenceBundle`, `EvidenceRef`, `SourceDescriptor`, `SourceIntakeRecord`, `RunReceipt`, `PromotionDecision`, `PromotionReceipt`, `ReleaseManifest`, `PolicyDecision`, `DecisionEnvelope`); require an ADR for any change.

**Open questions.** Which object families belong in the shared kernel versus lane-specific profiles? Is `DriftSummary` shared or lane-specific?

**Suggested future work.** Draft a kernel ADR; pair each kernel object with a fixture and a negative fixture.

##### KFM-IDX-DOC-006 — Responsibility layers as KFM large-scale structure

**Status.** PROPOSED. **Category/Subcategory.** DOC / Large-scale structure. **Lineage.** Pass 18 card `KFM-P18-INV-396` (Responsibility Layers pattern from DDD reference, pages 50–52). Not promoted to top-level Pass 19; surfaced here because Pass 19's expansion agenda implicitly assumes such layers exist (EXP-001 is a watcher lane; EXP-002 is an artifact-integrity lane; EXP-009 is a conformance lane).

**Normalized statement.** KFM architecture documentation should name responsibility layers — evidence, policy, catalog, release, API, UI, AI, and operations — so cross-domain changes are evaluated against the layer they affect.

**Detailed explanation.** The DDD reference identifies Responsibility Layers under large-scale structure as a way to keep a complex model navigable. Pass 18 generalizes this to KFM: even though the system has many domain lanes, every change can be characterized by which responsibility layer it touches. A PR that adds a `SourceDescriptor` field touches the SRC and EVD layers; a PR that adjusts a publication gate touches the VAL and REL layers; a PR that introduces a new map state badge touches the MAP and UIX layers. Naming the layers explicitly turns PR review into a layer-impact conversation rather than a topic-centric one. The Pass 19 expansion agenda fits this pattern naturally because each EXP item already implies a layer assignment.

**Why it matters.** It prevents topic-centric design (a "PMTiles change") from hiding which governance layer (EVD, MAP, VAL, REL) actually owns the change.

**Related ideas.** `KFM-IDX-DOC-005` (shared kernel); `KFM-IDX-DOC-002` (Directory placement); the entire 14-category map (Section 5).

**Dependencies.** Responsibility-layer enumeration; architecture register; change-impact summary template; ADR template.

**Tensions / limitations.** Layer names can become bureaucratic if not tied to decisions and tests. The risk is that PR templates require layer impact statements that nobody reads.

**Expansion directions.** Create a `responsibility_layer` field in change-impact summaries; tie it to ADR linkage and to the 14-category map.

**Open questions.** Which layers are mandatory for every KFM PR impact statement? Are the layers identical to the 14 categories or a coarser overlay?

**Suggested future work.** Draft a layer-impact template; align it with Section 5's category map.

---

### 6.2 REP — Geographic Representation, Scale, and Spatial Reference

#### Category overview

REP is the first claim-bearing layer of the trust membrane. Once doctrine is settled, the next question is whether KFM's representations — geometries, projections, scale rules, 2D/3D views, symbols, tile schemes — can carry inspectable claims at all. The GIS primer cited heavily in Pass 18 makes clear that geographic information is *communicative*: every map omits, exaggerates, generalizes, and chooses, and every map embeds choices about scale, coordinate reference system, resolution, symbology, and viewport. The 3D archaeology source extends this into volumetric representation, where the line between measured geometry and interpretive reconstruction must be visible. Pass 19 sharpened REP with the Pass 19 delta packet on county geometry hashes, which made geographic versioning a concrete intake-time concern. REP appears in both passes with a small number of high-leverage ideas.

#### 6.2.1 Subcategories

- **Cartographic representation.** The communicative nature of maps; symbols, choices, omissions.
- **Scale and spatial reference.** CRS, scale denominators, raster resolution, geometry version.
- **Representation form separation.** Raster, vector, network, field, graph, narrative — each with its own epistemic status.
- **3D and 2.5D humility.** Measured versus interpretive geometry, especially in archaeology.

#### 6.2.2 Idea entries

##### KFM-IDX-REP-001 — Representation is a governed claim surface

**Status.** CONFIRMED. **Category/Subcategory.** REP / Cartographic representation. **Lineage.** Pass 18 cross-cutting theme P18-XCT-001 and REP card cluster; Pass 19 P19-REP-001.

**Normalized statement.** Maps, symbols, projections, 3D scenes, tiles, and view states are representations with choices and omissions, so KFM should treat them as claim surfaces.

**Detailed explanation.** The GIS primer cited in the Pass 18 ledger (46 cards) explains that geographic information and maps simplify, omit, exaggerate, and communicate chosen aspects of reality. Pass 18 elevates this from a textbook observation into a KFM doctrine: representation is not neutral display. A scale denominator is a choice; a categorical color scheme is a choice; a symbol is a choice; a viewport extent is a choice. Domain reports inside the Pass 19 ledger apply the rule to hazards, archaeology, species locations, soil, hydrology, infrastructure, and settlements — each domain has cases where the choice of representation materially changes what the user reads. Pass 19 normalizes this into REP-001 and threads it through MAP, UIX, and POL.

**Why it matters.** It forces every public map layer to carry fitness-for-use, scale constraints, source role, uncertainty handling, and citation. Without it, attractive cartography becomes implicit truth claim.

**Related ideas.** `KFM-IDX-MAP-001` (renderer not truth store); `KFM-IDX-UIX-001` (Evidence Drawer); `KFM-IDX-REP-002` (scale/CRS/version as evidence properties).

**Dependencies.** Layer manifests; view manifests; scale constraints; style rules; source descriptors.

**Tensions / limitations.** The corpus contains many map-ready proposals but not always explicit fitness-for-use tests. There is also an inherent tension between informative cartographic communication and the discipline required to keep representation honest about its choices.

**Expansion directions.** Develop a representation acceptance checklist for each published layer; require fitness-for-use metadata in layer manifests.

**Open questions.** Which visual encodings become policy-significant claims (i.e. those whose interpretation affects rights, safety, or resource allocation)?

**Suggested future work.** Create a map-layer fitness-for-use template with scale, CRS, resolution, uncertainty, source role, and citation fields.

##### KFM-IDX-REP-002 — Scale, CRS, resolution, and geometry version are evidence properties

**Status.** CONFIRMED. **Category/Subcategory.** REP / Scale and spatial reference. **Lineage.** Pass 18 (multiple REP cards across GIS primer, environmental GIS, and temporal database materials); Pass 19 P19-REP-002 and the New Ideas 5-15 geometry-hash warning.

**Normalized statement.** Spatial reference, pixel area, county geometry hashes, and scale constraints must be tracked because apparent changes may be artifacts of representation rather than source reality.

**Detailed explanation.** The GIS and environmental GIS references in the Pass 18 ledger make scale, projection, resolution, raster versus vector representation, and field collection foundational to whether a comparison between two layers is even meaningful. Pass 19 adds a concrete geometry-drift warning: county boundary changes can masquerade as landcover changes unless a `county_geometry_hash` is persisted alongside class histograms. The same problem appears across hydrologic unit codes, parcels, road and rail networks, floodplain boundaries, raster grids, and tile schemes — any change in the underlying geometry can produce an apparent change in derived statistics that has nothing to do with source-reality change.

**Why it matters.** It prevents false material-change detections from triggering review work, and it protects historical comparability across releases. The CDL Watch fixture in EXP-001 is a concrete case where a missing geometry hash would have made the watcher unreliable.

**Related ideas.** `KFM-IDX-SRC-006` (CDL/PLANTS source-drift candidates); `KFM-IDX-MOD-003` (geography versions in identity); `KFM-IDX-ANA-003` (CDL histogram drift trigger).

**Dependencies.** Geometry version registry; hash calculation; projection metadata; raster resolution metadata; ontology version metadata.

**Tensions / limitations.** Changing county boundaries or class definitions can produce real numeric differences without substantive landcover change; conversely, materially-significant landcover changes can be partially masked by geometry shifts.

**Expansion directions.** Add `geometry_version_ref` and `projection_metadata` to `SourceDescriptor`, `DriftSummary`, and `SourceIntakeRecord`; build a no-network fixture that exercises both real-drift and geometry-drift cases.

**Open questions.** Which canonical county geometry version should seed county-level watchers? How should retroactive geometry changes be represented in rollback?

**Suggested future work.** Publish a geography-version fixture and a geometry-drift negative test as part of EXP-001.

##### KFM-IDX-REP-003 — Raster, vector, network, field, and graph forms must not be collapsed

**Status.** CONFIRMED. **Category/Subcategory.** REP / Representation forms. **Lineage.** Pass 18 (REP and MOD cards from GIS primer, temporal database, DDD references); Pass 19 P19-REP-003.

**Normalized statement.** KFM should keep raster surfaces, vector features, network graphs, field observations, graph projections, and narrative assertions distinct even when they appear together on a map.

**Detailed explanation.** The reference corpus distinguishes rasters, vectors, networks, fields, transformations, remote-sensing scenes, SQL tables, domain aggregates, and graph/triplet projections. Each form has its own epistemic status and its own appropriate inferences. A raster surface implies pixel-level fidelity; a vector feature implies a discrete observation; a network graph implies edge relations; a field observation implies a sampled measurement; a graph projection implies a derived reasoning surface; a narrative assertion is interpretive language. Domain reports inside the Pass 19 ledger repeatedly warn that derived tiles, graph edges, and model surfaces are *rebuildable carriers* of evidence, not canonical truth, and the AI Concepts source supplies the same caution for ML outputs.

**Why it matters.** It lets KFM use each representation form for its strengths without letting a rendering format become the source of authority. A graph triplet that summarizes a vector feature is downstream of the feature, not above it.

**Related ideas.** `KFM-IDX-MAP-003` (artifact matrix); `KFM-IDX-API-001` (governed APIs); `KFM-IDX-MOD-005` (object families distinct).

**Dependencies.** Canonical object model; graph projection rules; tile artifact manifests; knowledge-character labels.

**Tensions / limitations.** Map users may see a uniform UI despite heterogeneous epistemic status across underlying forms. The unification problem is presentational, not structural.

**Expansion directions.** Expose knowledge-character labels in layer manifests and Evidence Drawer payloads so the user can see when a layer is a derived graph projection versus an observed vector layer.

**Open questions.** How granular should source-role labels be for mixed raster/vector products? Should graph projections be a separate layer type or a property of underlying layers?

**Suggested future work.** Build a representation taxonomy registry tied to layer manifests; include `object_family` and `knowledge_character` fields in the schema.

##### KFM-IDX-REP-004 — 3D and 2.5D outputs require evidentiary humility

**Status.** CONFIRMED. **Category/Subcategory.** REP / 3D and archaeology. **Lineage.** Pass 18 (REP and FIE cards from Archaeological 3D GIS source, 43 cards); Pass 19 P19-REP-004.

**Normalized statement.** 3D models, 2.5D terrain, volume estimates, visibility analyses, and archaeological reconstructions must distinguish measured geometry from interpretation.

**Detailed explanation.** The Archaeological 3D GIS source in the Pass 18 ledger distinguishes proper 3D geometry from 2.5D representation and frames 3D models as knowledge-production tools rather than literal depictions. The Pass 19 archaeology blueprint denies exact public site locations by default and treats LiDAR anomalies, geophysical signals, and remote-sensing pattern detections as *candidate features* until reviewed. Visually compelling 3D scenes are persuasive in a way that magnifies the risk of overclaim: a reconstructed building can look as solid as a measured wall, and a hill-shaded terrain can look more precise than its underlying DEM warrants. KFM's response is to require scene manifests to flag measured-versus-interpretive geometry and to make those flags visible in the Evidence Drawer.

**Why it matters.** It prevents visually compelling 3D scenes from being mistaken for confirmed sites, precise volumes, or public truth, and it protects sensitive archaeology from looting risk.

**Related ideas.** `KFM-IDX-FIE-003` (archaeological 3D documentation vs interpretation); `KFM-IDX-POL-003` (exact-location protection); `KFM-IDX-MAP-005` (map trust states).

**Dependencies.** 3D scene manifest; review state; sensitivity policy; transform receipt; public-safe generalization.

**Tensions / limitations.** 3D visualizations are persuasive by design and may hide interpretive choices in ways that flat cartography does not. The same problem exists in 2.5D hill-shade rendering, which can suggest measurement precision that the underlying DEM does not have.

**Expansion directions.** Create scene manifests with `measured` versus `interpretive` geometry flags; suppress exact archaeological geometry in public scenes and render generalized envelopes with `suppressed_geometry: true`.

**Open questions.** How should public 3D scenes display suppressed or generalized archaeological geometry? Should viewers receive a sidebar explanation, an overlay shading, or both?

**Suggested future work.** Pilot a 3D scene Evidence Drawer payload with `measured` / `reconstructed` / `candidate` / `generalized` / `suppressed` fields.

---

---

### 6.3 SRC — Source Admission, Descriptors, Source Roles, and Connectors

#### Category overview

SRC is the intake edge of the trust membrane. Everything that becomes evidence, modeled fact, validated artifact, or published claim begins as external material that has to pass through source admission. Pass 18 captured this through cards on source descriptors, source-head metadata, source roles, connector behavior, and external-service boundaries. Pass 19 sharpened SRC with the three delta packets: New Ideas 5-8 added environmental probes; New Ideas 5-10 added PMTiles intake hygiene; New Ideas 5-15 added CDL/PLANTS/SSURGO/Air source drift watchers with `SourceDescriptor`, `SourceIntakeRecord`, and `DriftSummary` schemas. SRC is one of the most operationally pressured categories in Pass 20 Part 2.

#### 6.3.1 Subcategories

- **Source descriptors.** Identity, role, rights, cadence, endpoint, version, contact, `source_head`, sensitivity, admissibility limits.
- **Source-head checks.** HEAD, ETag, Last-Modified, content-length as low-cost change detection.
- **Source-role registry.** Occurrence aggregators vs regulatory archives vs operational feeds vs models vs imagery vs community observations vs assessor records vs legal sources.
- **Connectors and watchers.** Web acquisition, API probes, scrapers, package watchers — bounded, persisted, tested, rate-aware, rights-aware, non-publishing.
- **External-service boundaries.** What external systems may and may not do to KFM, and how their failures are surfaced.

#### 6.3.2 Idea entries

##### KFM-IDX-SRC-001 — Every admitted source needs a SourceDescriptor

**Status.** CONFIRMED. **Category/Subcategory.** SRC / Source admission. **Lineage.** Pass 18 SRC card cluster and Greenfield/Pipeline doctrine; Pass 19 P19-SRC-001 and New Ideas 5-15.

**Normalized statement.** A KFM source should enter through a descriptor that records source identity, role, rights, cadence, endpoint, version, contact, `source_head`, sensitivity, and admissibility limits.

**Detailed explanation.** The Greenfield Building Plan and Pipeline Living Implementation Manual cited in the Pass 18 ledger define source descriptors as part of the trust spine, and domain blueprints across hydrology, fauna, flora, roads, archaeology, atmosphere, soil, agriculture, and people/land each propose source registries. Pass 19's New Ideas 5-15 packet then maps watcher sidecars to `SourceDescriptor` terminology and ties them into `SourceIntakeRecord` and `DriftSummary`. The descriptor is what converts external material from anonymous data into accountable intake. It carries enough information for downstream rights review, sensitivity policy, materiality threshold lookup, and rollback target identification, without itself becoming truth — the descriptor records *that the source exists* and *how it should be treated*, not *what the source says*.

**Why it matters.** Without a descriptor, downstream evidence resolution has no stable anchor: there is no way to look up whether a claim's source has admissible rights, what role the source plays, or what its update cadence implies for freshness.

**Related ideas.** `KFM-IDX-EVD-005` (canonical hashes); `KFM-IDX-POL-002` (rights as evidence); `KFM-IDX-SRC-006` (CDL/PLANTS watchers); `KFM-IDX-API-004` (SourceIntakeRecord).

**Dependencies.** Source registry; descriptor schema; rights fields; cadence fields; source-role enumeration; sensitivity registry.

**Tensions / limitations.** New Ideas 5-15 sidecars are practical and field-tested in design but are not always complete `SourceDescriptor`s — they sometimes drop rights and contact fields. Normalization across the three Pass 19 packets is needed.

**Expansion directions.** Normalize sidecars into the `SourceDescriptor` + `SourceIntakeRecord` + `DriftSummary` family; require steward sign-off on descriptors for rights-sensitive sources before connector activation.

**Open questions.** Which descriptors need legal or steward approval before connector activation? Is the descriptor versioned independently of the source itself?

**Suggested future work.** Create `SourceDescriptor` schemas with negative fixtures for missing rights, missing `source_head`, missing contact, and missing cadence.

##### KFM-IDX-SRC-002 — HEAD, ETag, Last-Modified, and content length are intake evidence

**Status.** CONFIRMED. **Category/Subcategory.** SRC / Source-head checks. **Lineage.** Pass 18 (scraping reference + connector cards); Pass 19 P19-SRC-002 and New Ideas 5-15 sidecars.

**Normalized statement.** Fast source checks should record `source_head` metadata, but they should not substitute for substantive validation, rights review, or publication gates.

**Detailed explanation.** New Ideas 5-8, 5-10, and 5-15 packets all use HTTP HEAD / If-None-Match, ETag, Last-Modified, content length, and `spec_hash` as low-overhead watcher signals. Pass 19 warns explicitly that ETag alone is insufficient because publishers may re-publish under the same URL, and that content hashes are stronger evidence when feasible. Source-head metadata is one component of intake evidence, not a substitute for substantive validation; a HEAD success means *the URL responded*, not that *the new content is admissible*. The web-scraping source in the Pass 18 ledger reinforces this through its discussion of redirects, rate limits, and republication patterns.

**Why it matters.** It supports low-cost change detection without letting fetch success masquerade as source acceptance.

**Related ideas.** `KFM-IDX-EVD-005` (canonical hashes); `KFM-IDX-VAL-001` (material-change gates); `KFM-IDX-SRC-006` (CDL/PLANTS source-drift candidates).

**Dependencies.** HTTP metadata capture; content hash; source license; canonical descriptor hash.

**Tensions / limitations.** Some sources do not provide stable or meaningful ETags; some rotate them on every response without content change; some omit Last-Modified.

**Expansion directions.** Treat `source_head` as one evidence component among several; require content hash when feasible; for sources without stable ETag, document the fallback in the descriptor.

**Open questions.** What fallback should KFM use for sources lacking ETag and Last-Modified? Is content-length plus content-hash sufficient?

**Suggested future work.** Build `source_head` validation with missing-metadata, weak-metadata, and rotating-ETag cases.

##### KFM-IDX-SRC-003 — Source roles prevent authority collapse

**Status.** CONFIRMED. **Category/Subcategory.** SRC / Source authority. **Lineage.** Pass 18 (cross-domain SRC and POL cards); Pass 19 P19-SRC-003.

**Normalized statement.** Occurrence aggregators, regulatory archives, operational feeds, model products, imagery, community observations, assessor records, and legal sources must have distinct source roles.

**Detailed explanation.** Domain reports inside the Pass 19 ledger are unusually consistent on this point: source families are not interchangeable. Assessor and tax records are not title truth. NFHL regulatory flood-hazard zones are not observed flooding. Warning feeds are not life-safety alert systems. GBIF and eBird occurrence aggregations are context, not legal-status authority. Remote-sensing anomalies are candidates, not confirmations. Community-science observations may support context but typically require steward review before public claim. Pass 19 normalizes these into one rule: source role is a property of the source's relationship to the claim, and a mismatch between role and claim type is a deny condition rather than a quality issue.

**Why it matters.** It preserves legal, scientific, operational, and interpretive boundaries that domain experts know but generic data-handling code does not.

**Related ideas.** `KFM-IDX-POL-003` (exact-location protection); `KFM-IDX-ANA-001` (analysis as interpretive derivative); `KFM-IDX-MOD-005` (object families distinct).

**Dependencies.** Source-role registry; policy rules; `EvidenceBundle` source-role fields; per-domain role-claim matrix.

**Tensions / limitations.** A single source may play multiple roles in different claims — e.g. a state hazard archive could be regulatory context for one claim type and historical observation for another.

**Expansion directions.** Create source-role constraints and claim-type mappings; treat role-mismatch as a publication-deny condition.

**Open questions.** When can a community-science observation support public context, and when must it remain review-only?

**Suggested future work.** Build a per-domain source-role matrix (EXP-007) with explicit deny rules for authority misuse.

##### KFM-IDX-SRC-004 — Connectors and scrapers must fail safe at the intake edge

**Status.** CONFIRMED. **Category/Subcategory.** SRC / Connector behavior. **Lineage.** Pass 18 (scraping reference, 37 cards; hazards and atmosphere blueprints); Pass 19 P19-SRC-004.

**Normalized statement.** Web acquisition, scraping, API probes, and package watchers should be bounded, persisted, tested, rate-aware, rights-aware, and unable to publish directly.

**Detailed explanation.** The web-scraping reference cited in the Pass 18 ledger emphasizes redirects, rate limits, AJAX, forms, errors, robustness, persistence, and tests as part of well-behaved web acquisition. KFM doctrine extends that into connector governance: watchers and connectors emit candidate records or receipts, not public truth. Pass 19 reinforces this through the watcher-as-non-publisher invariant — the New Ideas 5-15 CDL watcher explicitly emits `SourceIntakeRecord` with `publication_state = WORK_CANDIDATE` rather than publishing layers. The same rule applies to API probes (New Ideas 5-8), PMTiles intake (New Ideas 5-10), and any future scraper or harvester.

**Why it matters.** It prevents a successful fetch from being mistaken for source acceptance, and it removes "the watcher just published it" as a possible failure mode.

**Related ideas.** `KFM-IDX-VAL-003` (negative fixtures); `KFM-IDX-POL-002` (rights as evidence); `KFM-IDX-REL-005` (watcher lifecycle).

**Dependencies.** Connector test fixtures; retry policy; rate-limit handling; source terms; quarantine path; outbox or queue for candidates.

**Tensions / limitations.** Generic web-acquisition references must be translated into KFM-specific acceptance criteria; raw scraper code from a textbook is not a connector.

**Expansion directions.** Write connector policies that separate fetch success, parse success, source acceptance, and publication into distinct outcomes.

**Open questions.** Which connector failures should emit `ERROR` versus `ABSTAIN`? What is the appropriate retry policy for each source family?

**Suggested future work.** Create a connector event envelope with `retry`, `error`, `policy_id`, and `outcome` fields.

##### KFM-IDX-SRC-005 — Environmental CI probes are source-health monitors, not scientific conclusions

**Status.** PROPOSED. **Category/Subcategory.** SRC / Source watches. **Lineage.** Pass 19 P19-SRC-005 (New Ideas 5-8 packet); domain blueprints corroborate the role separation.

**Normalized statement.** SMAP, MAIAC, FIRMS, AirNow, Mesonet, GBIF, eBird, MapLibre, and similar probes can monitor availability, freshness, and gating indicators, but their current operational claims require re-verification before use.

**Detailed explanation.** New Ideas 5-8 reports steady status for multiple feeds and proposes CI probes with signed run-receipts that record source-head metadata, derivations, decisions, policy IDs, and `spec_hash`. Because these facts are time-sensitive and not rechecked in the current session, Pass 20 Part 2 treats them as document-supported signals that need current verification before operational reliance. The probes are useful precisely *because* they are not scientific conclusions — they record what the source said when the probe ran, not what the world said. This separation between source-health and source-truth is what keeps probe outputs from leaking into public claim surfaces.

**Why it matters.** It lets KFM benefit from source-watch patterns while avoiding stale status claims and avoiding the conflation between "the feed is alive" and "the feed says something true".

**Related ideas.** `KFM-IDX-VAL-002` (environmental probes need signed receipts); `KFM-IDX-ANA-002` (AOD and FRP as tile-health gates); `KFM-IDX-POL-002` (rights and source terms).

**Dependencies.** Probe schemas; source-specific verification; credentials; usage terms; freshness thresholds.

**Tensions / limitations.** The Pass 19 packet includes links and current-status language after the model cutoff; those facts are not independently verified in this run.

**Expansion directions.** Label all source-status claims as NEEDS VERIFICATION; encode probe results as timestamped receipts with verification-date fields.

**Open questions.** Which official status pages are canonical for each source family? What is the appropriate cadence and timeout per source?

**Suggested future work.** Create a source-watch registry (EXP-003) with verification dates, recency thresholds, and rights status.

##### KFM-IDX-SRC-006 — CDL and PLANTS watchers should emit source-drift candidates only

**Status.** CONFIRMED. **Category/Subcategory.** SRC / Source drift detection. **Lineage.** Pass 19 P19-SRC-006 (New Ideas 5-15 packet); agriculture and flora blueprints corroborate.

**Normalized statement.** USDA CDL and PLANTS monitoring should detect material county-level drift and emit `SourceIntakeRecord` candidates rather than reprocessing or publishing automatically.

**Detailed explanation.** New Ideas 5-15 proposes a weekly CDL watcher with class histogram sidecars (`spec_hash`, `classmap_version`, `geometry_hash`, relative and absolute materiality thresholds), a parallel PLANTS taxa-drift watcher, and a strict governance boundary: every watcher output becomes a `SourceIntakeRecord` with `publication_state = WORK_CANDIDATE` and `promotion_required = true`, never an automatic publish. The packet provides material-change rules that go beyond raw histogram diff — net gain/loss, dominant transition, entropy change, persistence across observations — and pairs every machine diff with a markdown steward summary. This is one of the clearest expansion opportunities in the Pass 19 → Pass 20 transition: narrow, testable, doctrine-aligned, and fixture-friendly.

**Why it matters.** It is the most concrete operational expansion in the Pass 19 corpus and the most natural first proof of the full source-change governance lane.

**Related ideas.** `KFM-IDX-ANA-003` (CDL histogram drift trigger); `KFM-IDX-ANA-004` (PLANTS taxa drift); `KFM-IDX-VAL-001` (material-change gates); `KFM-IDX-REL-005` (watcher lifecycle).

**Dependencies.** County geometry fixture; thresholds; `classmap_version`; source descriptor; offline fixtures; review markdown template.

**Tensions / limitations.** Materiality thresholds are policy choices and need steward review; PLANTS data can introduce sensitive-species risk when joined to GBIF, iNaturalist, or heritage datasets.

**Expansion directions.** Build a no-network fixture-first CDL watcher (EXP-001) before any live source activation; mirror the pattern for PLANTS, SSURGO, and Air on a phased schedule.

**Open questions.** Which county set, CDL year, and class ontology should seed the first fixture? Which PLANTS taxa intersect with state-listed conservation species and require additional handling?

**Suggested future work.** Create PR-ecology-watch-0001 with watcher skeleton, schemas, fixtures, tests, and explicit `publication_denied` defaults.

### 6.4 MOD — Data Modeling, Domain Semantics, Temporal Structure, and SQL

#### Category overview

MOD is where admitted material is expressed in object families, bounded contexts, temporal structure, and SQL. The references that feed MOD most heavily inside the Pass 18 ledger are the temporal database design source (528 pages), the Domain-Driven Design reference (59 pages), and Advanced SQL Concepts (112 pages). Pass 18 produced one of its largest card populations here. Pass 19 normalized MOD into five entries that carry the structural weight: temporal structure as first-class evidence; bounded contexts; geography versions in identity; class ontology and semantic versions; object families distinct.

#### 6.4.1 Subcategories

- **Temporal structure.** Valid time, transaction time, bitemporal modeling, observed time, retrieval time, release time, correction time.
- **Bounded contexts.** Domain semantics, ubiquitous language, context maps, aggregates, repositories.
- **Geography versions.** County, HUC, parcel, road, rail, floodplain, grid, tile geometries.
- **Ontology drift.** Class IDs, taxa lists, hazard types, soil mapunits, AQI categories.
- **Object-family separation.** Assertions, observations, models, public artifacts, graph projections, AI summaries.

#### 6.4.2 Idea entries

##### KFM-IDX-MOD-001 — Temporal structure is first-class evidence

**Status.** CONFIRMED. **Category/Subcategory.** MOD / Temporal modeling. **Lineage.** Pass 18 (temporal database source, 45 cards); Pass 19 P19-MOD-001.

**Normalized statement.** Valid time, observed time, source time, retrieval time, release time, transaction time, and correction time must remain distinct where material.

**Detailed explanation.** The temporal database reference supplies valid-time, transaction-time, bitemporal, period, and temporal-key concepts. Pass 18 and Pass 19 promote these from database mechanics into a KFM invariant: time is not merely a date field. The CDL Watch packet records `retrieval_time`, source cadence, and recency windows; PMTiles sidecars record build time and release time; AI envelopes record query time and response time; correction histories record correction time relative to original assertion time. Each time dimension carries different epistemic weight, and conflating them collapses the system's ability to reason about historical state, rollback targets, and freshness.

**Why it matters.** Without explicit temporal dimensions, the system loses the ability to say what was known when, what was published when, and what was corrected when. This destroys rollback and correction lineage.

**Related ideas.** `KFM-IDX-REL-004` (rollback targets); `KFM-IDX-SRC-002` (source-head); `KFM-IDX-ANA-002` (AOD/FRP gates).

**Dependencies.** Temporal schema fields; bitemporal tables; release manifests; receipt timestamps.

**Tensions / limitations.** Temporal detail can become heavy if all domains require all time types; not every claim needs full bitemporal modeling.

**Expansion directions.** Define a minimal temporal profile per object family; treat full bitemporality as opt-in where material.

**Open questions.** Which time dimensions are mandatory for each claim category — environmental, historical, regulatory, observational?

**Suggested future work.** Build a temporal-support acceptance checklist (EXP-013) with negative fixtures for missing time dimensions.

##### KFM-IDX-MOD-002 — Bounded contexts protect domain meaning

**Status.** CONFIRMED. **Category/Subcategory.** MOD / Domain semantics. **Lineage.** Pass 18 (DDD reference, 47 cards; domain blueprints); Pass 19 P19-MOD-002.

**Normalized statement.** Hydrology, habitat, fauna, flora, soil, agriculture, geology, atmosphere, hazards, roads, settlements, archaeology, people/DNA/land, UI, and AI should remain bounded contexts with shared governance objects.

**Detailed explanation.** The DDD reference provides bounded context, ubiquitous language, aggregates, repositories, and context maps. KFM applies this to its domain lanes, which share `EvidenceBundle`, `SourceDescriptor`, `DecisionEnvelope`, catalog, proof, policy, and release objects without collapsing domain semantics. A "site" in archaeology, a "site" in hazards, and a "site" in soil are not the same object even though they share the word — bounded contexts make that distinction structural rather than rhetorical. Pass 18 captures this through ~47 cards in the MOD chapter; Pass 19 normalizes it into one principle.

**Why it matters.** It supports growth across domain lanes without producing a Big Ball of Mud where every cross-domain product re-invents the meaning of basic terms.

**Related ideas.** `KFM-IDX-SRC-003` (source roles); `KFM-IDX-API-001` (governed APIs); `KFM-IDX-DOC-005` (shared governance kernel); `KFM-IDX-PLN-003` (proof-bearing slices).

**Dependencies.** Context map; shared kernels; domain-specific schemas; governance schemas.

**Tensions / limitations.** Cross-domain products can blur boundaries, especially habitat-fauna, roads-settlements, people-land, and hazards-hydrology. Each cross-domain product needs an explicit relation-edge contract.

**Expansion directions.** Create domain-lane context maps and relation-edge rules; document the shared kernel separately from per-domain extensions.

**Open questions.** Which object families belong in shared governance versus domain-specific schemas? Where does `SourceIntakeRecord` sit?

**Suggested future work.** Write a bounded-context appendix for the first proof lane (likely ecology-watch).

##### KFM-IDX-MOD-003 — Geography versions are part of identity

**Status.** CONFIRMED. **Category/Subcategory.** MOD / Geographic versioning. **Lineage.** Pass 18 (geography-version logic across multiple categories); Pass 19 P19-MOD-003 and the CDL geometry-hash warning.

**Normalized statement.** County, HUC, parcel, road, rail, floodplain, grid, and tile geometries need version identifiers or hashes where they affect claims.

**Detailed explanation.** Pass 19 makes this concrete for CDL histograms: a county boundary change can produce an apparent landcover change without any real source-reality change unless a `county_geometry_hash` is persisted. The same problem appears across HUC boundaries (hydrology), parcel boundaries (people/land), road/rail networks (roads/rail/trade), floodplain boundaries (hazards), raster grid schemes (atmosphere), and tile schemes (map artifacts). Geography is not a fixed coordinate space; it is a versioned set of objects, and identity has to include the version.

**Why it matters.** It preserves reproducibility and comparability across releases, and it prevents source-drift watchers from emitting false positives caused by geometry refresh.

**Related ideas.** `KFM-IDX-REP-002` (scale/CRS/version as evidence); `KFM-IDX-ANA-003` (CDL histogram drift); `KFM-IDX-REL-004` (rollback targets).

**Dependencies.** `GeographyVersion` objects; geometry hashes; source descriptors; spatial-join receipts.

**Tensions / limitations.** Exact geometry may be sensitive or legally ambiguous in some domains (parcels, archaeology); geometry hash and exposure policy interact.

**Expansion directions.** Add `geometry_version_ref` to `DriftSummary`, `SourceIntakeRecord`, and layer manifests; include both the version reference and the hash so a renamed-but-unchanged geometry is detectable.

**Open questions.** How should KFM handle retroactive changes in county or HUC geometry? Should historical data be re-projected or marked as historical-geometry?

**Suggested future work.** Create one county geometry fixture with hash and one altered-geometry negative fixture (part of EXP-001).

##### KFM-IDX-MOD-004 — Class ontologies and semantic versions protect historical comparability

**Status.** CONFIRMED. **Category/Subcategory.** MOD / Semantic versioning. **Lineage.** Pass 18 (ontology references across agriculture, flora, fauna, hazards, soil, atmosphere); Pass 19 P19-MOD-004.

**Normalized statement.** Categorical source products such as CDL classes, PLANTS taxa lists, hazard types, landcover, soil map units, and AQI summaries need ontology / version references and drift checks.

**Detailed explanation.** Pass 19 warns that CDL class meanings can change between years and recommends a `classmap_version` with fail-closed behavior if class IDs changed meaning or a remapping is missing. The same pattern applies across PLANTS taxa (where USDA may update taxonomy without changing the underlying organism), SSURGO mapunits (where boundary and attribute schemas drift), hazard typologies (where federal classifications update), and AQI category definitions. Without ontology versioning, numerical continuity can mask semantic discontinuity: a chart that looks like a smooth time series can in fact be a chart of two different schemes joined without explicit remap.

**Why it matters.** It prevents numerical continuity from masking semantic discontinuity, which would silently corrupt historical comparisons and downstream indicators.

**Related ideas.** `KFM-IDX-SRC-006` (CDL/PLANTS source-drift candidates); `KFM-IDX-VAL-003` (negative fixtures); `KFM-IDX-ANA-004` (PLANTS taxa drift).

**Dependencies.** Ontology registry; remapping tables; source version; schema validation; per-source `classmap_version` lookup.

**Tensions / limitations.** Ontology maintenance can be more work than initial ingest, especially across federal data products that update on different cadences.

**Expansion directions.** Create an ontology-drift check as a validation gate; treat unmapped class IDs as deny conditions until remapped.

**Open questions.** Who owns crosswalks when source taxonomies change? Are remappings versioned per source or globally?

**Suggested future work.** Add `classmap_version` to CDL STAC items and PLANTS sidecars; build a negative fixture for unmapped class IDs.

##### KFM-IDX-MOD-005 — Assertions, observations, models, and public artifacts are different object families

**Status.** CONFIRMED. **Category/Subcategory.** MOD / Object families. **Lineage.** Pass 18 (object-family separation across cards in MOD, ANA, EVD, MAP); Pass 19 P19-MOD-005.

**Normalized statement.** An observation, a modeled derivative, a legal assertion, a public-safe tile, a graph edge, and an AI summary should not share the same truth status.

**Detailed explanation.** This distinction recurs across the corpus: regulatory flood hazard is not observed flood; an assessor record is not title truth; an occurrence point is not range truth; a model output is interpretive; a tile is a carrier; a graph edge is a derived reasoning surface; an AI summary is interpretive language. Pass 18 makes the rule explicit through cards in MOD, ANA, EVD, and MAP; Pass 19 normalizes it into MOD-005. The same KFM surface (e.g. a public map) can render multiple object families simultaneously, but the system must know which is which.

**Why it matters.** It allows KFM to publish useful composite products while retaining the provenance and epistemic status of each component.

**Related ideas.** `KFM-IDX-SRC-003` (source roles); `KFM-IDX-ANA-001` (analysis as interpretive derivative); `KFM-IDX-MAP-001` (renderer not truth store).

**Dependencies.** Object-family schemas; knowledge-character labels; `EvidenceBundle` links.

**Tensions / limitations.** Users may treat all visible layers as equally authoritative unless the UI makes distinctions clear.

**Expansion directions.** Add `object_family` and `knowledge_character` fields to layer and Evidence Drawer payloads; require these for any new public layer.

**Open questions.** Which object families are eligible for public export? Should graph projections ever be exportable as standalone data?

**Suggested future work.** Create a public-export policy keyed to `object_family`.

---

### 6.5 EVD — Evidence, Provenance, Receipts, Identity, and Attestation

#### Category overview

EVD is the inspectable substrate of the trust membrane. Without resolvable evidence, doctrine becomes prose. Pass 18 captured EVD through cards on `EvidenceRef`, `EvidenceBundle`, canonical hashes, receipts, signatures, and proof patterns. Pass 19 sharpened EVD operationally with the PMTiles attestation packet: signed sidecars with `schema_version`, `pmtiles_filename`, `spec_hash`, `root_hash`, size, delta metadata, byte-range manifest, and provenance refs; BLAKE3 for content hashing; Bao for outboard streaming proofs; DSSE / cosign for signing. Pass 20 Part 2 retains the canonical five EVD entries.

#### 6.5.1 Subcategories

- **EvidenceBundle closure.** Resolvable chain from claim to source.
- **Receipts.** Run, promotion, AI, validation, source-head receipts as process memory.
- **Artifact attestation.** Signed sidecars binding artifacts to provenance.
- **Streaming proofs.** Bao / outboard hashes for byte-range verification.
- **Canonical hashes.** Deterministic identity from canonicalized descriptors.

#### 6.5.2 Idea entries

##### KFM-IDX-EVD-001 — EvidenceRef must resolve to EvidenceBundle

**Status.** CONFIRMED. **Category/Subcategory.** EVD / Evidence closure. **Lineage.** Pass 18 (EVD card cluster); Pass 19 P19-EVD-001.

**Normalized statement.** Evidence-bearing claims should resolve through `EvidenceRef` to a complete `EvidenceBundle` before public answer, map popup, Focus Mode synthesis, or export.

**Detailed explanation.** KFM doctrine in both passes states that `EvidenceBundle` outranks generated language and that public surfaces must remain downstream of governed evidence flow. The Greenfield Building Plan, the Pipeline Living Implementation Manual, the MapLibre Operating manual, the Governed-AI manuals, and the Whole-UI Expansion Report all converge on this. `EvidenceRef` is the pointer, `EvidenceBundle` is the resolved set: claim, source descriptors, citations, supporting receipts, policy decisions, review state, and release state. Public exposure requires the bundle to be complete; an unresolved `EvidenceRef` is an abstain condition, not an attempt-to-render condition.

**Why it matters.** It supplies the inspectable substrate of every KFM public surface and gives Evidence Drawer something concrete to display.

**Related ideas.** `KFM-IDX-DOC-001` (cite-or-abstain); `KFM-IDX-UIX-001` (Evidence Drawer); `KFM-IDX-API-002` (finite outcome envelopes).

**Dependencies.** EvidenceBundle schema; resolver; citation validator; UI payload contracts.

**Tensions / limitations.** EvidenceBundle completeness criteria vary by domain and claim significance; high-significance claims need richer bundles than routine layer popups.

**Expansion directions.** Define minimal and high-significance EvidenceBundle profiles; build fixtures for both.

**Open questions.** What EvidenceBundle fields are mandatory for environmental thresholds versus historical claims versus AI answers?

**Suggested future work.** Create EvidenceBundle fixtures for a CDL drift claim and a PMTiles artifact integrity claim.

##### KFM-IDX-EVD-002 — Receipts preserve process memory without becoming truth

**Status.** CONFIRMED. **Category/Subcategory.** EVD / Receipts. **Lineage.** Pass 18 (receipts across pipeline doctrine); Pass 19 P19-EVD-002 and New Ideas 5-8/5-10 packets.

**Normalized statement.** `RunReceipt`, `PromotionReceipt`, `AIReceipt`, validation reports, and source-head receipts should record what happened, but they do not make the underlying claim true by themselves.

**Detailed explanation.** The Greenfield and Pipeline manuals treat receipts as auditable process records. New Ideas 5-8 requires signed run-receipts for environmental probes; New Ideas 5-10 references promotion and run receipts in PMTiles attestation. A receipt is the system saying "this happened at this time with these inputs and this outcome" — it is not the system saying "this is true". The distinction matters because a successful run is not a successful claim, and a promotion receipt is not source authority.

**Why it matters.** Receipts give KFM rollback and auditability without collapsing procedure into truth. They allow correction: knowing what was done, when, and why is the precondition for reversing it.

**Related ideas.** `KFM-IDX-REL-002` (promotion as state transition); `KFM-IDX-VAL-004` (publication gates); `KFM-IDX-EVD-003` (PMTiles attestation sidecars).

**Dependencies.** Receipt schemas; signatures; validation reports; release manifests.

**Tensions / limitations.** Receipts can be over-read as approval if their status is unclear; the same receipt may indicate "validation passed" without indicating "policy approved" or "release authorized".

**Expansion directions.** Separate observation, validation, promotion, and publication receipts into distinct types with distinct fields.

**Open questions.** Which receipts are public, steward-only, or internal? Should AIReceipt be public?

**Suggested future work.** Build a receipt-type registry with exposure rules per type.

##### KFM-IDX-EVD-003 — PMTiles attestation sidecars make map artifacts verifiable

**Status.** CONFIRMED. **Category/Subcategory.** EVD / Artifact attestation. **Lineage.** Pass 19 P19-EVD-003 (New Ideas 5-10 packet); Master MapLibre atlas corroborates the sidecar pattern.

**Normalized statement.** Each PMTiles artifact should have a signed sidecar that records `schema_version`, `pmtiles_filename`, `spec_hash`, `root_hash`, size, delta metadata, `byte_ranges_manifest`, and provenance refs.

**Detailed explanation.** New Ideas 5-10 supplies a detailed sidecar schema, a DSSE / cosign signing sketch, the Bao outboard proof pattern, validation gates, and a CI workflow that fails closed on missing sidecar, missing signature, missing root hash, missing `delta_base_hash`, unknown `spec_hash`, or unresolved provenance. Master MapLibre also converges on PMTiles integrity sidecars. The sidecar moves tile delivery from informal file hosting into governed artifact publication: a PMTiles file without its sidecar is not a publication candidate; a PMTiles file whose sidecar fails verification is not a publication candidate. This is exactly the kind of small, testable, fixture-friendly artifact that fits EXP-002.

**Why it matters.** It moves the most visible KFM surface — map tiles — from informal hosting to inspectable, verifiable artifact publication.

**Related ideas.** `KFM-IDX-MAP-004` (viewer verification); `KFM-IDX-REL-003` (avoid in-place overwrites); `KFM-IDX-VAL-004` (publication gates deny missing proofs).

**Dependencies.** PMTiles sidecar schema; BLAKE3 / Bao tooling; signing keys; release manifest; key trust chain.

**Tensions / limitations.** Tool versions and licenses need verification before implementation; signing tooling and key trust chain are NEEDS VERIFICATION.

**Expansion directions.** Start with a sample sidecar covering a small fixture PMTiles file; defer cryptographic verification until the toolchain is pinned.

**Open questions.** Should all tiles have byte-range proofs, or only high-risk layers at first?

**Suggested future work.** Create `tools/validators/validate_pmtiles_sidecar.py` with negative fixtures for each deny condition.

##### KFM-IDX-EVD-004 — Bao and byte-range proofs enable partial verification

**Status.** PROPOSED. **Category/Subcategory.** EVD / Range proofs. **Lineage.** Pass 19 P19-EVD-004 (New Ideas 5-10 packet); Master MapLibre atlas references streaming proof patterns.

**Normalized statement.** PMTiles clients and QA flows can verify fetched byte ranges against `root_hash` using Bao or comparable outboard proofs.

**Detailed explanation.** New Ideas 5-10 proposes generating a `.bao` outboard file and adding `bao_proof_ref` entries for tile byte ranges. The pattern enables streaming verification: a client can verify that the bytes it received correspond to a specific position in the archive without having to hash the entire archive. This is implementation guidance, not proof of an existing KFM system. The corpus does not record current Bao tooling pinning, licensing, or performance characteristics; those remain NEEDS VERIFICATION before operational reliance.

**Why it matters.** It supports streaming integrity without hashing the entire archive for every tile request, which is essential for PMTiles' Range-optimized delivery to remain trustworthy.

**Related ideas.** `KFM-IDX-MAP-002` (PMTiles Range tests); `KFM-IDX-MAP-004` (viewer verification); `KFM-IDX-VAL-004` (publication gates).

**Dependencies.** Bao toolchain; byte-range manifest; browser/server verification logic; performance benchmarks.

**Tensions / limitations.** Full client-side proof verification may be expensive or impractical in some production cases; not every browser environment can do this efficiently.

**Expansion directions.** Use QA sampled-range verification first and expand coverage as the pipeline stabilizes; consider server-mediated verification where browser cost is high.

**Open questions.** What is the performance budget for proof verification in public browsers?

**Suggested future work.** Benchmark proof verification on sample PMTiles archives before requiring it in production.

##### KFM-IDX-EVD-005 — Canonical hashes turn descriptors into stable identity

**Status.** CONFIRMED. **Category/Subcategory.** EVD / Deterministic identity. **Lineage.** Pass 18 (`spec_hash` usage); Pass 19 P19-EVD-005 with the New Ideas 5-15 canonical JSON → SHA256 method and the New Ideas 5-10 BLAKE3 recommendation.

**Normalized statement.** `spec_hash` and similar canonical hashes should be computed from canonicalized descriptors, source metadata, thresholds, classmaps, and artifact specifications.

**Detailed explanation.** Pass 18 already uses `spec_hash` language; Pass 19 makes the computation explicit. New Ideas 5-15 gives a simple canonical-JSON-plus-SHA256 method for sidecars (sort fields, normalize whitespace, hash). New Ideas 5-10 recommends BLAKE3 for artifact roots because of streaming friendliness. Different hash roles call for different algorithms: descriptor hashing values determinism and ecosystem support (SHA256 with JCS); content and root hashing values streaming and parallelism (BLAKE3); range and proof hashing values outboard verification (Bao). A hash-policy ADR is needed to make these choices explicit rather than implicit.

**Why it matters.** It makes changes auditable, deterministic, replayable, and CI-checkable.

**Related ideas.** `KFM-IDX-SRC-001` (SourceDescriptor); `KFM-IDX-SRC-002` (source-head); `KFM-IDX-MAP-004` (viewer verification).

**Dependencies.** Canonicalization method; sorted-field rules; hash-algorithm policy; schema validation.

**Tensions / limitations.** Different source families propose SHA256 or BLAKE3; the corpus has not settled a universal hash policy across all object families.

**Expansion directions.** Define hash roles: SHA256 / JCS for descriptors; BLAKE3 / Bao for streaming artifacts; explicit algorithm prefixes on every hash field.

**Open questions.** Should KFM standardize one hash algorithm per object family, or one across the system?

**Suggested future work.** Draft a hash-policy ADR (EXP-004) and validator fixtures for correct algorithm prefixes.

---

### 6.6 POL — Policy, Rights, Ethics, Sensitivity, and Public-Safety Controls

#### Category overview

POL governs whether and how a claim can be exposed at all. Pass 18 and Pass 19 are unusually consistent on POL because every domain blueprint in the ledger encountered the same recurring concerns: rights, source terms, exact-location sensitivity, cultural risk, living-person and DNA limits, archaeology, infrastructure exposure, rare species, and fail-closed defaults. Pass 19 normalizes POL into four entries that carry the load.

#### 6.6.1 Subcategories

- **Public-safe defaults.** Fail-closed when rights, sensitivity, source authority, review state, release state, or evidence closure is unclear.
- **Rights and consent.** Source rights, licenses, contacts, written permission.
- **Sensitive geometry.** Exact archaeological sites; rare species occurrences; living-person and DNA data; infrastructure-sensitive geometries; private land.
- **Policy thresholds.** AOD, FRP, CDL materiality, AQI, SSURGO mapunit thresholds as versioned policy.

#### 6.6.2 Idea entries

##### KFM-IDX-POL-001 — Public-safe by default is non-negotiable

**Status.** CONFIRMED. **Category/Subcategory.** POL / Public exposure. **Lineage.** Pass 18 (POL cards across multiple domain blueprints); Pass 19 P19-POL-001 and New Ideas 5-8 / 5-10 gates.

**Normalized statement.** Public and semi-public KFM surfaces should fail closed when rights, sensitivity, source authority, review state, release state, or evidence closure is unclear.

**Detailed explanation.** This doctrine is pervasive across domain blueprints — archaeology, people/DNA/land, fauna, flora, hazards, infrastructure, and AI. New Ideas 5-8 adds fail-closed gates for source consent (notably Mesonet, which is consent-required), and New Ideas 5-10 adds fail-closed gates for PMTiles signature failures, missing sidecars, and unverified proofs. Fail-closed is the default at the publication gate, the API gate, and the renderer gate. The user-visible consequence is that some queries return `ABSTAIN` rather than improvising an answer, and some layers do not render publicly rather than rendering with caveats.

**Why it matters.** It protects people, species, cultural resources, infrastructure, and public users from unsafe exposure that no amount of caveat text could mitigate.

**Related ideas.** `KFM-IDX-POL-003` (exact-location protection); `KFM-IDX-VAL-004` (publication gates); `KFM-IDX-REL-005` (watcher lifecycle).

**Dependencies.** Policy engine; sensitivity labels; release state; `EvidenceBundle`; user role.

**Tensions / limitations.** Fail-closed defaults can slow publication and require clear steward workflows for appeal and correction; without those workflows, fail-closed becomes a hidden tax on contributors.

**Expansion directions.** Define review queues and appeal / correction paths for denied or quarantined outputs; pair every deny with a documented reason.

**Open questions.** Who can authorize staged access for sensitive layers? What is the SLA for review of denied outputs?

**Suggested future work.** Create policy fixtures for exact-location DENY and generalized-output ALLOW (EXP-011).

##### KFM-IDX-POL-002 — Rights and source terms are evidence requirements

**Status.** CONFIRMED. **Category/Subcategory.** POL / Rights and licenses. **Lineage.** Pass 18 (rights fields across domain blueprints); Pass 19 P19-POL-002.

**Normalized statement.** Source rights, source licenses, data-use contacts, attribution, and written consent should be stored and checked before ingest or release.

**Detailed explanation.** New Ideas 5-8 explicitly says Mesonet ingest should fail closed without written consent. New Ideas 5-10 recommends storing tool and license strings in PMTiles build receipts. Domain reports in the Pass 19 ledger mark rights and source terms as NEEDS VERIFICATION for many feeds. Rights are not metadata fluff; they are evidence properties that determine admissibility. A claim derived from a source whose rights are unverified is not a publishable claim regardless of how well-modeled the rest of the pipeline is.

**Why it matters.** It keeps KFM from publishing technically valid but legally or ethically unsupported outputs.

**Related ideas.** `KFM-IDX-SRC-001` (SourceDescriptor); `KFM-IDX-EVD-002` (receipts); `KFM-IDX-VAL-002` (signed probe receipts).

**Dependencies.** License fields; source terms registry; contact records; receipt references.

**Tensions / limitations.** Some public data sources have ambiguous or changing terms; rights can be perishable.

**Expansion directions.** Add `license_text_or_contact` to run receipts and source descriptors; treat missing license as a deny condition.

**Open questions.** Which sources need direct written permission versus acceptance of public terms? Who is the named licensee for each source family?

**Suggested future work.** Build a rights-verification backlog with deny fixtures for missing license fields.

##### KFM-IDX-POL-003 — Exact-location and living-person data require special protection

**Status.** CONFIRMED. **Category/Subcategory.** POL / Sensitivity. **Lineage.** Pass 18 (POL cards across archaeology, fauna, flora, people/DNA/land, settlements/infrastructure, roads); Pass 19 P19-POL-003.

**Normalized statement.** Exact archaeological sites, rare species, steward-controlled occurrences, living-person and DNA data, infrastructure-sensitive geometries, and private-land details should be withheld, generalized, or denied unless review supports exposure.

**Detailed explanation.** The archaeology, fauna, flora, people/DNA/land, settlements/infrastructure, and roads blueprints converge on this rule. New Ideas 5-15 warns that PLANTS data can become sensitive if joined to GBIF, iNaturalist, or heritage datasets — a benign source can become sensitive through join, which means sensitivity is a property of the resulting product, not just of the original source. The Pass 18 archaeology cards explicitly deny exact public site geometry by default and require review for any exposure. The same applies to nests, dens, roosts, hibernacula, spawning sites, and other ecologically sensitive geometries. KFM's response is internal exact storage paired with public generalized products and recorded transforms.

**Why it matters.** It is one of the main reasons KFM cannot simply be a public map of all known things; precision is useful for research but dangerous in public outputs.

**Related ideas.** `KFM-IDX-SRC-003` (source roles); `KFM-IDX-MAP-005` (map trust states); `KFM-IDX-UIX-003` (review surfaces).

**Dependencies.** Sensitivity registry; geoprivacy transform receipts; access roles; review state.

**Tensions / limitations.** Map-first design intersects with exact-location denial; the solution is public-safe generalized surfaces with Evidence Drawer explanations and recorded transforms.

**Expansion directions.** Separate internal exact records from public generalized products and record transforms; treat join-induced sensitivity as a deny condition for the join product even if the inputs were individually safe.

**Open questions.** Which rare plant or animal data can be public at county level? What is the appropriate generalization radius for archaeological site centroids?

**Suggested future work.** Create geoprivacy policies with `exact`, `generalized`, `suppressed`, and `steward-only` outcomes (part of EXP-011).

##### KFM-IDX-POL-004 — Thresholds are policy controls, not universal scientific absolutes

**Status.** CONFIRMED. **Category/Subcategory.** POL / Policy thresholds. **Lineage.** Pass 19 P19-POL-004 (New Ideas 5-8 and 5-15 packets); domain blueprints corroborate.

**Normalized statement.** AOD, FRP, CDL materiality, AQI, SSURGO mapunit change, PM2.5 jumps, and other thresholds should be documented as policy choices requiring review, not treated as universal scientific truth.

**Detailed explanation.** New Ideas 5-8 explicitly says MAIAC AOD thresholds (e.g. AOD > 0.5 for `DEGRADED`, AOD > 0.8 for `QUARANTINE`) are policy, not science absolutes. The same applies to FIRMS FRP escalation thresholds, CDL materiality cutoffs, AQI category boundaries, and SSURGO mapunit area-change rules. Each threshold encodes a policy decision about how cautious or permissive the system is at a gate. Documenting thresholds with `policy_id`, `version`, `rationale`, and `steward approval` keeps the gate inspectable and tunable.

**Why it matters.** It keeps deterministic automation inspectable and adjustable rather than treated as scientific fact.

**Related ideas.** `KFM-IDX-ANA-002` (AOD/FRP gates); `KFM-IDX-VAL-001` (material-change gates); `KFM-IDX-ANA-003` (CDL histogram drift).

**Dependencies.** Threshold registry; policy ID; domain-steward review; validation fixtures.

**Tensions / limitations.** Poorly chosen thresholds can under-trigger or over-trigger work; sensitivity analysis is needed to characterize the trade-off.

**Expansion directions.** Record thresholds with `policy_id`, `version`, `rationale`, and `steward approval`; pair each threshold change with a sensitivity note.

**Open questions.** What thresholds fit Kansas counties of different size and source uncertainty?

**Suggested future work.** Create a threshold sensitivity analysis for one county and one tile set (EXP-008).

### 6.7 VAL — Validation, QA, Testing, Observability, and Reliability

#### Category overview

VAL is the operational verification category. It contains the rules and patterns by which derived products — schemas, fixtures, manifests, sidecars, drift summaries, evidence bundles, release decisions — are proven trustworthy before exposure. VAL sits between EVD and REL in the dependency order: evidence supplies the substrate, validation supplies the test discipline, release supplies the publication gate. Pass 18 spread validation logic across many chapters with a strong tilt toward testing, observability, and fail-closed posture; Pass 19 normalized it into five explicit ideas anchored on materiality, signed probes, negative fixtures, publication gates, and no-network dry runs. The Pass 19 deltas (5-8 and 5-10) push VAL toward concrete CI-shaped artifacts: signed receipts for environmental probes, sidecar validators for PMTiles, threshold sensitivity tests, and dry-run promotion gates.

#### 6.7.1 Subcategories

- **Materiality gates.** Thresholds and persistence rules that distinguish significant change from churn.
- **CI probes.** Source-health monitors that emit timestamped, signed receipts rather than ephemeral logs.
- **Negative fixtures.** Invalid fixtures proving that fail-closed actually fails.
- **Publication gates.** Promotion validators that deny missing proofs, signatures, or rights posture.
- **No-network dry runs.** Fixture-first proof lanes that exercise schemas, validators, and policy without live fetch.

#### 6.7.2 Idea entries

##### KFM-IDX-VAL-001 — Material-change gates reduce noisy reprocessing

**Status.** CONFIRMED. **Category/Subcategory.** VAL / Materiality gates. **Lineage.** Pass 19 P19-VAL-001; convergent with Pass 18 testing and observability cards.

**Normalized statement.** Source watchers should distinguish materially significant changes from routine churn using explicit thresholds, persistence rules, and structured diff summaries.

**Detailed explanation.** Pass 19's New Ideas 5-15 defines materiality for landcover and species drift with both relative and absolute thresholds: CDL county histograms should trigger review when class-share change exceeds defined relative thresholds (e.g. 1.0 percentage point shift on dominant classes, 0.25 on minor classes) or absolute hectare counts cross domain limits; PLANTS taxa drift triggers on additions/removals against a stable taxonomy version; SSURGO weekly watchers track mapunit area shift and schema drift; AirNow daily summaries flag PM2.5 jumps against rolling baselines. New Ideas 5-8 reinforces the persistence dimension: AOD and FRP signals should persist across independent observations within a 48–96 hour window before being treated as substantive rather than transient. Pass 18 corroborated the principle without naming concrete thresholds, leaving the operational sharpening to Pass 19. The point is not the specific numbers — those are policy choices under KFM-IDX-POL-004 — but that materiality is an explicit, versioned, replayable computation rather than a feeling. Materiality summaries should include net gain/loss, dominant transition, entropy, and cross-category transitions where the source product supports them, because a single absolute-delta number can obscure semantically important shifts (e.g. a county that retains its total cropland fraction but flips from corn to soybeans).

**Why it matters.** Without materiality gates, watchers become noise generators that either trigger excessive review or are silenced into uselessness. Versioned materiality keeps the system replayable: any past trigger can be reproduced from its threshold, classmap version, and source state.

**Related ideas.** `KFM-IDX-SRC-006` (CDL/PLANTS drift candidates); `KFM-IDX-ANA-003` (CDL histogram drift); `KFM-IDX-POL-004` (thresholds as policy); `KFM-IDX-VAL-003` (negative fixtures).

**Dependencies.** Threshold registry; source descriptors; checkpointed prior state; old/new histogram persistence; geometry version; classmap version.

**Tensions / limitations.** A materiality rule that only sums absolute deltas can be too blunt; transition semantics (what changed *to* what) matter. Thresholds also interact with county size — a 1% rule on a small county can be more sensitive than on a large one. The corpus does not settle a universal materiality formula and explicitly defers to domain stewards.

**Expansion directions.** Implement materiality as a function over `DriftSummary` records that produces a deterministic outcome plus a structured rationale field. Track multiple materiality dimensions side by side (absolute, relative, transition, persistence) rather than collapsing to a single scalar.

**Open questions.** What is the minimum materiality evidence needed before a steward review queue entry? Should materiality functions be per-domain or share a kernel?

**Suggested future work.** Implement `test_material_change_detects_relative_threshold` and negative cases as the first VAL fixtures; document the threshold rationale in a versioned policy registry per EXP-008.

##### KFM-IDX-VAL-002 — Environmental source probes need signed receipts

**Status.** CONFIRMED. **Category/Subcategory.** VAL / CI probes. **Lineage.** Pass 19 P19-VAL-002 (drawing on New Ideas 5-8); convergent with Pass 18 observability and EVD receipt cards.

**Normalized statement.** Source probes should record inputs, `source_head` metadata, derivations, decisions, `policy_id`, signatures, and `spec_hash` as durable receipts rather than ephemeral CI log lines.

**Detailed explanation.** New Ideas 5-8 supplies a concrete run-receipt checklist for MAIAC, FIRMS, SMAP, AirNow, and Mesonet probes: each probe run captures the URL or endpoint, response headers (ETag, Last-Modified, Content-Length, status), the probe's deterministic threshold inputs, the derivation that produced the decision (e.g. mean AOD over a tile centroid, FRP within a 5 km buffer), the finite outcome (NORMAL, DEGRADED, ESCALATE, QUARANTINE), the policy ID and version that bound the thresholds, a signature, and the canonical `spec_hash` of the probe definition. The signed receipt becomes the audit unit. CI dashboards remain useful for human triage, but they are not evidence — they cannot be re-verified, hashed, or replayed independent of the CI provider. Pass 18 corroborated this through its broader EVD doctrine on receipts as auditable process records that do not themselves constitute truth (KFM-IDX-EVD-002), and through Pass 18's emphasis on source-health observability as a first-class concern. The signed-receipt pattern is the EVD-VAL interface: VAL produces the receipts; EVD specifies their identity, signature, and schema.

**Why it matters.** Without signed receipts, source-health decisions are stored only in CI logs that can be rotated, replaced, or lost. With them, every gating decision becomes inspectable and replayable, and downstream tile state changes can be traced back to a specific probe receipt.

**Related ideas.** `KFM-IDX-SRC-005` (environmental CI probes as monitors not conclusions); `KFM-IDX-EVD-002` (receipts as process memory); `KFM-IDX-ANA-002` (AOD/FRP tile gating); `KFM-IDX-POL-004` (thresholds as policy).

**Dependencies.** Probe schemas; CI jobs; signing keys; source-terms records; credential handling; receipt store.

**Tensions / limitations.** Source-status facts in New Ideas 5-8 (which feeds were operational, which had outages) require current verification before operational reliance — they are watch prompts, not current claims. Signing toolchain decisions remain NEEDS VERIFICATION pending an ADR per EXP-004.

**Expansion directions.** Treat probes as receipts with explicit freshness and verification timestamps. Pair every probe with a deterministic decision function and a separate signed envelope.

**Open questions.** What latency thresholds are appropriate for each source family? Where should probe receipts live in the catalog — under EVD, REL, or a dedicated probe register?

**Suggested future work.** Create no-network probe fixtures with stale, missing-ETag, and unavailable-source cases (EXP-003).

##### KFM-IDX-VAL-003 — Negative fixtures are as important as valid fixtures

**Status.** CONFIRMED. **Category/Subcategory.** VAL / Negative fixtures. **Lineage.** Pass 18 (testing discipline throughout domain chapters); Pass 19 P19-VAL-003.

**Normalized statement.** KFM validators should include invalid fixtures covering missing `spec_hash`, invalid ETag, stale source date, unknown class ID, impossible hectare totals, county overflow, malformed histogram, geometry-hash mismatch, missing sidecar, bad signature, and unresolved provenance.

**Detailed explanation.** A fail-closed system is only credible if its failure paths are exercised. New Ideas 5-15 enumerates negative fixtures for the ecology watcher slice: an unchanged-county fixture (should not trigger), a material-change county fixture (should trigger), and several invalid-source cases (missing classmap, geometry mismatch, missing source descriptor) that should produce DENY or ERROR rather than silent pass. New Ideas 5-10 supplies the parallel list for PMTiles attestation: missing sidecar, invalid signature, missing Bao proof, unknown `spec_hash`, patch without `delta_base_hash`, and missing provenance refs all become DENY conditions at the publication gate. Pass 18 corroborated the principle through repeated calls for deny-by-default fixtures across sensitive domains: fauna and flora nests/dens, archaeology exact locations, people/DNA/land records, and infrastructure-sensitive geometries all need negative test cases proving the system actually refuses them. The validator registry becomes the canonical record linking every schema to both its valid and invalid fixtures.

**Why it matters.** Negative fixtures prove that fail-closed behavior actually works. They convert governance from documentation into testable invariant. The cost of missing a negative fixture is silent regression — a denied-by-design pathway that quietly starts succeeding because no test ever exercised its failure mode.

**Related ideas.** `KFM-IDX-POL-001` (public-safe by default); `KFM-IDX-EVD-003` (PMTiles attestation); `KFM-IDX-SRC-006` (CDL/PLANTS drift candidates); `KFM-IDX-VAL-004` (publication gates).

**Dependencies.** Validator scripts; fixture directory; CI workflow; policy engine; validator registry.

**Tensions / limitations.** Invalid-fixture coverage can lag behind new object families. There is also a maintenance cost: when a schema evolves, both positive and negative fixtures must move in lockstep or false-pass / false-fail regressions appear.

**Expansion directions.** Create a validator registry linking every schema to valid and invalid fixtures with explicit coverage labels. Tie fixture creation to schema PRs so a new schema cannot land without both positive and negative cases.

**Open questions.** Which test runner and schema home are canonical in the live repo? How should negative fixtures be organized — by schema, by failure mode, or by domain?

**Suggested future work.** Build the no-network fixture suite for ecology watch and PMTiles attestation before any live connector activation (EXP-001, EXP-002).

##### KFM-IDX-VAL-004 — Publication gates must deny missing proofs

**Status.** CONFIRMED. **Category/Subcategory.** VAL / Publication gates. **Lineage.** Pass 19 P19-VAL-004 (drawing on New Ideas 5-10 PMTiles attestation); convergent with Pass 18 REL doctrine on promotion as governed state transition.

**Normalized statement.** Publication should fail closed if PMTiles sidecars, signatures, Bao proofs, `root_hash`, `spec_hash`, `delta_base_hash`, rights posture, or sensitivity approval are missing.

**Detailed explanation.** New Ideas 5-10 explicitly defines DENY conditions for the PMTiles publication gate: missing sidecar, invalid signature, missing Bao proof, unknown `spec_hash`, patch artifact without a referenced `delta_base_hash`, and missing provenance refs all result in publication denial. Pass 18 corroborated the principle through its broader REL doctrine: promotion is a governed state transition, not a successful file move. The publication gate is where VAL and REL meet — validation produces the verdict, release acts on it. The gate is asymmetric by design: the cost of a missing-proof publication is corruption of the trust membrane, while the cost of a missing-proof denial is delay. Pass 19 makes that asymmetry concrete by adding cryptographic verification to the existing schema and link checks.

**Why it matters.** Without publication gates, KFM cannot keep its trust membrane intact. Files that exist on disk are not artifacts ready for public exposure; only artifacts that pass the publication gate are. The rule transforms publication from a deployment step into a verifiable governance act.

**Related ideas.** `KFM-IDX-EVD-003` (PMTiles attestation sidecars); `KFM-IDX-MAP-004` (viewer verification); `KFM-IDX-REL-002` (promotion as state transition); `KFM-IDX-VAL-003` (negative fixtures).

**Dependencies.** Release gate; sidecar validator; signature verification; policy review; key trust chain.

**Tensions / limitations.** Signature tooling and key trust chains remain NEEDS VERIFICATION — the corpus names cosign, DSSE, and BLAKE3/Bao but does not settle a specific KFM toolchain. There is also operational tension between strict gating and rapid iteration; the right answer is staged rollout (start with schema and link validation; add cryptographic verification when toolchain is pinned).

**Expansion directions.** Start with schema and link validation; layer cryptographic verification on as the toolchain ADR settles (EXP-004). Add a publication-deny dry run (EXP-010) so the gate is exercised before any real publication.

**Open questions.** What key-management model should KFM use? Which gate failures should produce DENY vs REVIEW_REQUIRED in the steward UI?

**Suggested future work.** Create PMTiles attestation gate fixtures with DENY and REVIEW_REQUIRED outcomes; prepare publication-deny dry run with intentionally incomplete PMTiles and SourceIntakeRecord objects.

##### KFM-IDX-VAL-005 — No-network dry runs are the safest first implementation proof

**Status.** PROPOSED. **Category/Subcategory.** VAL / No-network dry runs. **Lineage.** Pass 18 (recurring thin-slice and fixture-first patterns across domain chapters); Pass 19 P19-VAL-005.

**Normalized statement.** The first implementation increments should prove schemas, fixtures, validators, policy gates, and dry-run compilers without live fetch, public APIs, UI binding, or automatic promotion.

**Detailed explanation.** This pattern recurs across the Pass 18 domain blueprints and is reinforced by New Ideas 5-15: hydrology, habitat-fauna, ecology watch, and PMTiles attestation are all proposed as fixture-first proof lanes that exercise the trust membrane (schema, validator, policy, evidence, receipt, release decision) without involving live external sources, public client traffic, or automatic promotion. The no-network constraint is doing real work: it removes the risk of legal or ethical exposure from live data, eliminates the variability of external endpoints, and makes the test a property of the codebase rather than the network. A no-network PR can be reviewed, merged, and re-run identically on any branch. It also separates concerns cleanly: live activation becomes a separate, smaller PR whose verification surface is just the connector and rights review, because the schemas and validators are already proven.

**Why it matters.** No-network dry runs are the cheapest way to prove governance discipline. They let KFM establish the trust membrane before any live source is admitted, which is the only safe order given how sensitive several domain lanes are.

**Related ideas.** `KFM-IDX-DOC-004` (implementation maturity remains UNKNOWN); `KFM-IDX-SRC-006` (CDL/PLANTS drift candidates); `KFM-IDX-EVD-003` (PMTiles attestation); `KFM-IDX-PLN-003` (domain lanes as proof slices).

**Dependencies.** Fixtures; schemas; validators; CI; documentation; PR template that distinguishes no-network from live-activation increments.

**Tensions / limitations.** Dry runs cannot prove live endpoint behavior or source rights — they prove governance, not connectivity. The status is PROPOSED rather than CONFIRMED because the live-repo verification (EXP-009) has not yet established which test runner and fixture home are canonical.

**Expansion directions.** Pair no-network tests with a separate verification backlog for live activation. Adopt the no-network-first pattern as the default for every new domain lane.

**Open questions.** What is the first offline fixture set to use — CDL county 20091 or a PMTiles sample archive? Should no-network tests run on every PR or only on specific labels?

**Suggested future work.** Create a Pass 19/20 fixture-only PR package description as the standing template for thin-slice proofs.

### 6.8 ANA — Analysis, Indicators, Statistics, Machine Learning, and Model Interpretation

#### Category overview

ANA is the largest supporting category in the corpus by raw card count, but its function is constrained: every analytical output remains an interpretive derivative over evidence. Pass 18 devoted its broadest chapter to indicators, statistics, ML, and model interpretation while consistently subordinating them to EVD and POL. Pass 19 sharpens ANA in two specific directions: environmental signals (AOD, FRP) become deterministic tile-health gates when policy-bound, and source-drift summaries (CDL histograms, PLANTS taxa lists) become controlled analytical triggers rather than autonomous publication paths. The ANA chapter therefore reads as a discipline of restraint: useful indicators, calibrated thresholds, visible uncertainty, and explicit subordination to evidence and policy.

#### 6.8.1 Subcategories

- **Interpretive derivatives.** All ML, statistical, and indicator output is derived, not canonical.
- **Environmental signals.** AOD, FRP, and similar feeds gate tile health under policy thresholds.
- **Landcover drift.** CDL histogram drift as a deterministic, replayable analytical trigger.
- **Taxa drift.** PLANTS county package drift with sensitivity awareness.
- **Planning indicators.** Urban and regional planning analysis with participation and scenario context.

#### 6.8.2 Idea entries

##### KFM-IDX-ANA-001 — Analysis remains an interpretive derivative

**Status.** CONFIRMED. **Category/Subcategory.** ANA / Interpretive derivatives. **Lineage.** Pass 18 (extensive ANA chapter; doctrine that analysis is downstream of evidence and policy); Pass 19 P19-ANA-001.

**Normalized statement.** Indicators, statistics, ML models, thresholds, suitability scores, vulnerability indices, and planning scenarios should remain derived interpretations over evidence, not authoritative root claims.

**Detailed explanation.** Pass 18's analysis chapter was the largest by card count, drawing on the SQL, temporal-database, and AI technical references plus every domain blueprint that proposed indicators or models. Across all of them, KFM doctrine subordinates analytical outputs to the EvidenceBundle hierarchy: a vulnerability index is a derivative; a flood-risk score is a derivative; a habitat suitability surface is a derivative; an AI-generated summary is a derivative. The corpus treats this as central, not pedantic, because users tend to over-trust quantitative outputs and to read confident scores as facts. The mitigation is structural: every analytical output carries the indicator definition, source links, uncertainty, model card, and review state in its catalog and Evidence Drawer payloads. The user reads the number through the lens of the supporting evidence rather than around it. Pass 19 reinforces the rule by making the AI / Focus Mode boundary explicit (KFM-IDX-UIX-002): models can summarize and explain but cannot publish uncited language.

**Why it matters.** This rule keeps useful analysis available without letting prediction or summary become authoritative claim. Without it, KFM would gradually transform into a generator of confident scores that displace the slower evidence trail behind them.

**Related ideas.** `KFM-IDX-DOC-001` (cite-or-abstain); `KFM-IDX-MOD-005` (object family separation); `KFM-IDX-PLN-001` (planning support); `KFM-IDX-UIX-002` (Focus Mode evidence-bounded).

**Dependencies.** Model cards; evidence links; uncertainty fields; validation reports; review state; layer manifest extensions for indicator metadata.

**Tensions / limitations.** Users over-trust quantitative outputs; designers face pressure to show single confident numbers. The corpus does not fully settle which indicators are calibrated enough for public use.

**Expansion directions.** Display model and indicator limitations in Evidence Drawer and Focus Mode. Define an indicator manifest profile with source, formula, uncertainty, and review state.

**Open questions.** Which indicators need calibration / validation before public use? How should Evidence Drawer present uncertainty without becoming illegible?

**Suggested future work.** Create an indicator manifest profile with the required fields and pilot it on one planning indicator and one drift summary.

##### KFM-IDX-ANA-002 — AOD and FRP can gate tile health when policy-bound

**Status.** CONFIRMED. **Category/Subcategory.** ANA / Environmental signals. **Lineage.** Pass 19 P19-ANA-002 (drawing on New Ideas 5-8); not directly anticipated in Pass 18 but consistent with Pass 18 observability and POL threshold doctrine.

**Normalized statement.** MAIAC AOD and FIRMS FRP can support tile DEGRADED, ESCALATE, or QUARANTINE states when thresholds, persistence, source provenance, and policy IDs are recorded.

**Detailed explanation.** New Ideas 5-8 specifies concrete thresholds: AOD > 0.5 degrades a tile to atmospheric-haze posture; AOD > 0.8 escalates to quarantine for atmospheric layers; FRP > 0 within 5 km of a tile centroid escalates a fire-aware layer; FRP ≥ 10 MW within 5 km quarantines it. Each gate fires only when persistence rules cross (e.g. signal holds for 48–96 hours across independent observations). The output is a DecisionEnvelope tied to a `policy_id` and version, signed under VAL-002, that drives the tile's trust-visible state under MAP-005. The Pass 19 framing is careful: the thresholds are explicitly policy choices (KFM-IDX-POL-004), not scientific absolutes; the rule is a deterministic environmental gate that turns external observation into governed map state without crossing into emergency alerting (KFM-IDX-PLN-002). Pass 19 treats the underlying source-status claims (whether MAIAC/FIRMS were active in a given week) as document-supported watch prompts that need re-verification, which is why the idea ships with persistence rules and signed receipts rather than direct trust in any individual probe.

**Why it matters.** It provides a deterministic, auditable environmental gate for public map trust state without making KFM an alerting authority. The persistence requirement avoids flapping; the signed receipt makes every gating decision replayable.

**Related ideas.** `KFM-IDX-POL-004` (thresholds as policy); `KFM-IDX-VAL-002` (signed probe receipts); `KFM-IDX-MAP-005` (trust-visible map state); `KFM-IDX-PLN-002` (hazards support is not emergency alerting).

**Dependencies.** Source probes; source-status verification; DecisionEnvelope schema; signed receipts; tile centroid definition by zoom; persistence window.

**Tensions / limitations.** Thresholds are not universal science; the spatial unit (tile centroid) needs definition across mixed zoom levels. Operational source status requires live verification.

**Expansion directions.** Implement as a versioned policy profile with steward review. Treat AOD/FRP as one example of a broader environmental-signal pattern that could extend to weather, water quality, and other domains.

**Open questions.** What spatial unit defines a tile centroid for mixed zoom levels? How should persistence be tracked across timezone boundaries and partial-data windows?

**Suggested future work.** Create a no-network DecisionEnvelope fixture for QUARANTINE and DEGRADED outcomes and pair it with the threshold policy registry entry.

##### KFM-IDX-ANA-003 — CDL histogram drift is a controlled analytical trigger

**Status.** CONFIRMED. **Category/Subcategory.** ANA / Landcover drift. **Lineage.** Pass 19 P19-ANA-003 (drawing on New Ideas 5-15); convergent with Pass 18 agriculture and analysis cards.

**Normalized statement.** County-level CDL class histogram changes should trigger review only when relative or absolute materiality thresholds are crossed, semantic drift checks pass, and geometry drift checks pass.

**Detailed explanation.** New Ideas 5-15 defines the CDL drift trigger in concrete terms: each county histogram is persisted as a sidecar with `classmap_version`, `geometry_version_ref` (a hash of the county boundary used to compute the histogram), `source_descriptor_ref`, and the histogram itself. Drift is computed as the difference between successive histograms under the same classmap and geometry. The trigger fires when (a) the relative threshold rule crosses for any class, (b) the absolute hectare rule crosses, (c) dominant transitions cross the configured significance band, and (d) classmap and geometry hashes both match. If either hash mismatches, the system emits an ERROR or DENY rather than a drift conclusion — apparent change might be class-meaning drift (KFM-IDX-MOD-004) or boundary drift (KFM-IDX-REP-002), not real landcover change. The trigger output is a `DriftSummary` plus a human-readable markdown steward summary (KFM-IDX-UIX-003), wrapped in a `SourceIntakeRecord` candidate (KFM-IDX-API-004) with publication_state WORK_CANDIDATE. The pattern is replayable: any past trigger can be reproduced from the recorded threshold versions and source state.

**Why it matters.** It turns landcover monitoring into a governed, replayable analytical trigger that survives review, rollback, and recompile rather than a one-shot batch script.

**Related ideas.** `KFM-IDX-SRC-006` (CDL drift candidates); `KFM-IDX-MOD-003` (geography versions); `KFM-IDX-MOD-004` (class ontologies); `KFM-IDX-VAL-001` (material-change gates).

**Dependencies.** Raster statistics tooling; county geometry; thresholds; class ontology; source descriptor; sidecar schema.

**Tensions / limitations.** A histogram alone loses spatial-transition detail — two counties with the same class shares may have completely different spatial change patterns. Phase 2 should add pixel-level transition rasters once Phase 1 histogram drift is stable.

**Expansion directions.** Layer pixel-level transition rasters after the histogram trigger; track dominant transition types as first-class metadata in the DriftSummary.

**Open questions.** What transitions are most policy-significant for Kansas counties? How should partial-county coverage (where the source raster doesn't fully tile a county) be handled?

**Suggested future work.** Build the first county fixture for ecology-watch and produce a DriftSummary plus a `20091-summary.md` markdown steward summary as the seed reviewer artifact.

##### KFM-IDX-ANA-004 — PLANTS taxa drift is analytically useful but sensitivity-prone

**Status.** CONFIRMED. **Category/Subcategory.** ANA / Taxa drift. **Lineage.** Pass 19 P19-ANA-004 (drawing on New Ideas 5-15); convergent with Pass 18 flora and fauna sensitivity cards.

**Normalized statement.** PLANTS county package drift should track taxa additions and removals against a stable taxonomy version and intersections with governed species lists, while avoiding public exact-occurrence exposure.

**Detailed explanation.** New Ideas 5-15 mirrors the CDL sidecar pattern for PLANTS: a county package becomes a list of taxa under a recorded taxonomy version, and drift is computed as set difference between successive packages. Additions and removals become drift candidates only when (a) the taxonomy version is stable (so additions are real, not renames), (b) the intersection with state-listed and federally-listed conservation species is computed for sensitivity policy, and (c) the result is wrapped as a SourceIntakeRecord candidate. Pass 19 explicitly warns that PLANTS becomes sensitive when joined with GBIF, iNaturalist, or heritage datasets — what is a benign county species list in isolation can become a poaching map in combination. The pattern therefore inherits the fauna and flora sensitivity discipline from Pass 18: deny-by-default for exact public occurrences of rare species; generalize to county or larger; record the transform in a geoprivacy receipt; route through steward review for any output that intersects sensitive lists. The combination of analytical utility and sensitivity risk is exactly why PLANTS drift belongs in ANA (as a derived analytical trigger) rather than in a hypothetical raw-occurrence layer.

**Why it matters.** It supports biodiversity monitoring within KFM's existing fauna/flora geoprivacy posture, which is one of the system's strongest constraints. Pulling PLANTS drift into the same SourceIntakeRecord pipeline as CDL drift means the same review queue, the same sensitivity rules, and the same publication gates apply.

**Related ideas.** `KFM-IDX-POL-003` (exact-location protection); `KFM-IDX-SRC-006` (CDL/PLANTS drift candidates); `KFM-IDX-VAL-003` (negative fixtures); `KFM-IDX-MOD-004` (class/taxa ontology versioning).

**Dependencies.** PLANTS sidecar schema; taxonomy version; state and federal conservation species lists; sensitivity policy; steward review queue.

**Tensions / limitations.** Taxa list changes may reflect taxonomy updates rather than real presence/absence — separating taxonomy drift from package drift is essential. Joining PLANTS with occurrence sources introduces sensitivity risk that may not be obvious to operators.

**Expansion directions.** Track taxonomy/version drift separately from county package drift. Add explicit "join with occurrence sources is sensitive" gates wherever PLANTS feeds into a derived product.

**Open questions.** How should taxa changes intersect legal/conservation status lists from different agencies? Which join patterns require fail-closed denial?

**Suggested future work.** Create PLANTS taxa drift fixtures with both sensitive and non-sensitive cases; pair with policy fixtures from EXP-011.

##### KFM-IDX-ANA-005 — Urban and regional planning analysis needs participation and scenario context

**Status.** CONFIRMED. **Category/Subcategory.** ANA / Planning indicators. **Lineage.** Pass 18 (planning chapter and urban-planning technical reference); Pass 19 P19-ANA-005.

**Normalized statement.** Planning indicators should support scenario analysis, participation, equity, and resilience rather than presenting single authoritative answers.

**Detailed explanation.** The Pass 18 ledger drew extensively on the GIS in Sustainable Urban Planning and Management technical reference to surface a planning-analysis discipline that resists single-answer outputs. The reference covers sustainable, inclusive, compact-competitive, resilient, and collaborative city frameworks; multi-criteria analysis; quality-of-life indicators; transit-oriented development; growth and flood-risk modeling; and evacuation-shelter siting. Pass 18 placed planning analysis downstream of representation, evidence, policy, and validation; Pass 19 reaffirms that order and adds the explicit requirement that planning outputs make their scenario assumptions, stakeholder context, equity considerations, and uncertainty visible. Pass 20 Part 2 surfaces the latent Pass 18 detail that often gets abstracted away in summary: that planning analysis specifically requires participation (stakeholder identification, feedback loops, multi-criteria weighting that reflects multiple perspectives) and scenario context (the same indicator under different assumptions produces different rankings). A planning indicator that hides its assumptions is no longer planning support; it is technocratic recommendation.

**Why it matters.** Planning outputs expand KFM from data display toward decision support, which is where the system creates the most public value — but also where it carries the most political and ethical risk. Making assumptions visible is the structural defense against that risk.

**Related ideas.** `KFM-IDX-PLN-001` (planning support); `KFM-IDX-PLN-002` (hazards not emergency alerting); `KFM-IDX-REP-001` (representation as governed claim surface); `KFM-IDX-UIX-004` (Story Nodes inherit release/evidence state).

**Dependencies.** Planning scenario schema; stakeholder metadata; indicator manifest; uncertainty field; equity metadata.

**Tensions / limitations.** Planning use cases can become normative or politically charged if assumptions are hidden. Kansas frontier and rural contexts may differ from urban global examples in the reference; not every indicator transfers cleanly.

**Expansion directions.** Require scenario assumptions and equity/context notes in planning outputs. Adapt indicators to Kansas counties and rural/frontier needs explicitly.

**Open questions.** Which planning indicators transfer to Kansas counties without distortion? How should KFM represent stakeholder dissent within a published scenario?

**Suggested future work.** Create a scenario manifest fixture (EXP-014) and one public-safe planning example for a Kansas county.

### 6.9 FIE — Field Capture, Remote Sensing, 3D, and Archaeological Interpretation

#### Category overview

FIE is the corpus's supporting/emerging category for evidence that originates in observation rather than in models or catalogs. It covers field notebooks, drone captures, survey records, remote-sensing scenes, LiDAR, geophysical anomalies, and the 3D and 2.5D outputs that arise especially in archaeology. The category is supporting rather than central because most domain reports treat field and remote data as inputs to other categories (SRC, MOD, EVD, POL, ANA) rather than as a domain of governance on its own. Pass 19 nonetheless keeps FIE distinct because the corpus treats field capture and 3D interpretation as requiring their own discipline: redaction, transform receipts, candidate-versus-confirmed labeling, and STAC/DCAT/PROV normalization before any field or remote artifact reaches a public map.

The Pass 19 delta packets touch FIE indirectly: 5-8 makes remote-sensing products (MAIAC, FIRMS, SMAP, VIIRS) into source-health probes; 5-15 mentions LiDAR and aerial imagery as candidate-only inputs in the broader source-watch context. The Archaeological 3D GIS reference and the KFM archaeology blueprint converge on the strongest doctrine in this category: visually persuasive 3D outputs require evidentiary humility, and exact site geometry remains deny-by-default for public exposure.

#### 6.9.1 Subcategories

- **Field capture.** Field observations, drone runs, surveys, offline notes that need provenance and review.
- **Remote sensing.** Sentinel/SMAP/MAIAC/VIIRS/LiDAR/COG products with quality, latency, and role labels.
- **3D archaeology.** 3D and 2.5D models, measured vs interpretive geometry, candidate anomalies.
- **Catalog normalization.** STAC/DCAT/PROV staging before public map rendering.

#### 6.9.2 Idea entries

##### KFM-IDX-FIE-001 — Field capture should produce evidence, not orphan observations

**Status.** CONFIRMED. **Category/Subcategory.** FIE / Field capture. **Lineage.** Pass 19 P19-FIE-001; corroborated by Pass 18 field/capture cards and the Habitat-Fauna Thin Slice and Archaeology Architecture domain reports.

**Normalized statement.** Field observations, drone captures, survey records, and offline notes should become `EvidenceBundle`-linked records carrying source, time, geometry, rights, and review state before they influence any public surface.

**Detailed explanation.** The corpus treats field capture as a powerful evidence source that is also unusually risky: field data carries exact locations, identifiable observers, unreviewed interpretations, and sometimes private notes. Environmental GIS exercises [Pass 18] introduce Field Maps and drone workflows as standard practice; Archaeological 3D GIS treats field investigation as the substrate for 3D reconstruction and interpretation; the KFM archaeology and fauna/flora blueprints add an additional constraint that field observations enter the trust spine through descriptors, transforms, and review state rather than as raw uploads.

The normalized KFM posture is that a field observation is not yet evidence — it is a candidate that becomes evidence only when descriptor, time, geometry, rights, redaction status, and review state are recorded. The implication is operational: field tools should produce records compatible with `SourceDescriptor`, `EvidenceBundle`, and the sensitivity registry, and the catalog should keep field-origin records distinguishable from model-origin or aggregator-origin records.

**Why it matters.** Field data is high-value precisely because it carries direct observation. Treating it as orphan upload material would lose that value and expose KFM to sensitivity violations, rights ambiguities, and unreviewable claims.

**Related ideas.** `KFM-IDX-EVD-001` (EvidenceRef → EvidenceBundle closure); `KFM-IDX-SRC-001` (every source needs a descriptor); `KFM-IDX-POL-003` (exact-location and living-person sensitivity); `KFM-IDX-FIE-003` (3D archaeology documentation vs interpretation).

**Dependencies.** Field capture schema; source descriptor; review workflow; redaction policy; sensitivity registry.

**Tensions / limitations.** Field tooling in the wild often does not produce KFM-shaped records; the cost of normalization at the edge competes with the cost of normalization at intake.

**Expansion directions.** Add redaction receipts and steward review before any public release; pilot one offline field observation fixture with a public-safe transform receipt.

**Open questions.** Which field-capture fields are safe for immediate internal map preview, and which require steward review even for internal viewing?

**Suggested future work.** Create an offline field observation fixture for one habitat survey and one archaeology survey, both demonstrating descriptor closure and redaction.

##### KFM-IDX-FIE-002 — Remote sensing needs quality, latency, and source-role labeling

**Status.** CONFIRMED. **Category/Subcategory.** FIE / Remote sensing. **Lineage.** Pass 19 P19-FIE-002; reinforced by Pass 19 deltas (5-8 environmental probes); convergent with Pass 18 remote-sensing cards.

**Normalized statement.** Remote-sensing products — Sentinel, SMAP, MAIAC, VIIRS, LiDAR, COGs — should carry quality masks, latency or freshness windows, source role, processing lineage, and public-safety posture before they influence any KFM surface.

**Detailed explanation.** Pass 19's 5-8 packet [Pass 19] turns MAIAC/FIRMS/SMAP into source-health probes with thresholds, persistence rules, and signed receipts; this is fundamentally a remote-sensing discipline that says cadence, latency, and quality are not optional metadata. The KFM atmosphere, hazards, habitat, fauna, flora, soil, and geology reports use remote sensing throughout, and each distinguishes observation roles (what was measured), context roles (background information), model roles (derived products), and candidate roles (signals awaiting review).

The Archaeological 3D GIS reference adds a humility layer specifically for LiDAR and aerial imagery: anomalies are candidates until reviewed, and reconstructions are interpretive products until evidence supports them. The KFM normalization is that every remote-sensing artifact entering the system carries source role, quality flags, latency, and processing lineage, and that no remote-sensing product becomes authoritative truth merely by being recent or visually compelling.

**Why it matters.** Without quality, latency, and role labels, remote-sensing imagery can be over-interpreted by users who see a recent date and a clean visual surface and infer authoritative confirmation. Labels keep the renderer downstream of the science.

**Related ideas.** `KFM-IDX-SRC-005` (environmental CI probes); `KFM-IDX-VAL-002` (signed probe receipts); `KFM-IDX-MAP-003` (artifact matrix); `KFM-IDX-ANA-002` (AOD/FRP gating).

**Dependencies.** STAC metadata; source-head receipts; quality metrics; COG manifests; cadence policy.

**Tensions / limitations.** Some remote-sensing products have fast cadence but delayed validation, creating a window where the freshest data is also the least verified.

**Expansion directions.** Introduce PRELIMINARY or STALE states where source cadence and latency are uncertain; encode quality masks as first-class metadata.

**Open questions.** Which remote-sensing products should be public, steward-only, or review-only by default?

**Suggested future work.** Create STAC item profiles for MAIAC and CDL/COG fixtures demonstrating quality, cadence, and role labels.

##### KFM-IDX-FIE-003 — Archaeological 3D outputs separate documentation from interpretation

**Status.** CONFIRMED. **Category/Subcategory.** FIE / 3D archaeology. **Lineage.** Pass 19 P19-FIE-003; corroborated by Archaeological 3D GIS reference and KFM Archaeology Architecture Plan in Pass 18.

**Normalized statement.** 3D capture and reconstruction in archaeology should distinguish reality-based measured models, interpretive reconstructions, derived volume and visibility analyses, and candidate anomalies — and these distinctions should propagate into scene manifests and Evidence Drawer payloads.

**Detailed explanation.** Archaeological 3D GIS [Pass 18] frames 3D models as knowledge-production tools rather than visualizations, and is careful to distinguish proper 3D geometry from 2.5D representations and interpretive reconstructions from measured surfaces. The KFM archaeology blueprint sharpens this further: exact site locations are deny-by-default for public exposure, LiDAR and geophysical anomalies are candidates rather than confirmations, and reconstructions are interpretive products that must be labeled as such even when the underlying measured geometry is solid.

The KFM normalization is that every 3D scene manifest carries explicit labels — `measured`, `reconstructed`, `candidate`, `generalized`, `suppressed` — for each geometry component, and that public-facing 3D scenes never expose suppressed or generalized geometry without indicating the transform. This applies to LiDAR-derived surfaces, photogrammetric reconstructions, and any 3D output that combines measurement with interpretation.

**Why it matters.** A visually realistic 3D archaeological scene is one of the most persuasive surfaces in geospatial systems. Without separation, users will read interpretation as confirmation and loot or vandalism risk increases.

**Related ideas.** `KFM-IDX-REP-004` (3D/2.5D evidentiary humility); `KFM-IDX-POL-003` (sensitive geometry); `KFM-IDX-UIX-003` (steward summaries); `KFM-IDX-MAP-005` (map trust states).

**Dependencies.** 3D evidence provenance; review state; sensitivity policy; public-safe generalization; scene manifest schema.

**Tensions / limitations.** Even with labels, the rhetorical power of a clean 3D scene can outweigh metadata callouts; UI design must reinforce the separation.

**Expansion directions.** Pilot a 3D scene Evidence Drawer payload with measured-versus-interpreted fields; define a 3D archaeology explanation template that surfaces interpretive choices.

**Open questions.** How should Focus Mode describe uncertainty and interpretive choice in 3D archaeological scenes without overwhelming the public-facing description?

**Suggested future work.** Create a 3D archaeology scene fixture with explicit `measured` / `interpretive` flags and a corresponding drawer payload.

##### KFM-IDX-FIE-004 — Field and remote workflows normalize into catalogs before public maps

**Status.** PROPOSED. **Category/Subcategory.** FIE / Catalog normalization. **Lineage.** Pass 19 P19-FIE-004; convergent with Pass 18 STAC/DCAT/PROV doctrine and Pass 19 5-15 STAC recommendations for CDL.

**Normalized statement.** Field and remote-sensing outputs should normalize to STAC, DCAT, and PROV records — with checksums, projection metadata, source descriptors, and class ontology references — before becoming public map layers.

**Detailed explanation.** The Pass 18 catalog discipline and the Pass 19 5-15 packet [Pass 19] both treat catalog closure as the precondition for public exposure. The 5-15 packet specifically recommends representing CDL yearly bundles as STAC Items with raster assets, checksums, projection metadata, and class ontology references; the same logic extends to remote-sensing scenes and field-origin products. The KFM normalization is that field and remote outputs are not yet publishable simply because they have been captured or processed — they become publishable when catalog metadata, provenance, evidence, and policy records close consistently.

This idea is marked PROPOSED rather than CONFIRMED because the specific KFM STAC profiles for raster, vector, and field objects are not yet fixed in the corpus; the catalog discipline is doctrine, but the per-object-family profiles are still expansion work.

**Why it matters.** Catalog normalization makes field and remote products discoverable, auditable, and interoperable with the rest of the KFM trust spine. Without it, field and remote artifacts become parallel publication paths that bypass review.

**Related ideas.** `KFM-IDX-REL-001` (catalog closure); `KFM-IDX-MAP-003` (artifact matrix); `KFM-IDX-SRC-001` (every source needs a descriptor); `KFM-IDX-EVD-001` (evidence closure).

**Dependencies.** STAC item schema; checksum policy; projection metadata; source descriptor; ontology registry.

**Tensions / limitations.** Some domain products (especially 3D scenes and complex field captures) may not fit STAC cleanly and will need KFM-specific profiles.

**Expansion directions.** Define KFM STAC profiles for raster, vector, and field objects; pilot one CDL STAC item and one habitat-survey STAC item with linked provenance.

**Open questions.** Which fields are mandatory for a KFM CDL STAC item versus a field-survey STAC item, and where should the canonical profile definitions live?

**Suggested future work.** Draft `data/catalog/stac/ecology/cdl` and `data/catalog/stac/field/habitat` fixture profiles as PROPOSED pending Directory Rules review.

### 6.10 REL — Catalog Closure, Publication, Release, Rollback, and Recompile Discipline

#### Category overview

REL is the closure category. It is where validated evidence, policy decisions, artifact integrity proofs, and source descriptors come together into a published state — and, equally important, where rollback targets are preserved so that publication remains reversible. Pass 18 placed REL near the center of the dependency order: catalog closure is what turns processed material into publishable material, promotion is what changes release state, and rollback is what keeps the system honest. Pass 19 deepens REL in three operational directions: (1) PMTiles and large-artifact release discipline becomes concrete with versioned filenames, root hashes, and sidecars; (2) watcher lifecycle clarifies that source-drift detectors emit `WORK_CANDIDATE` records rather than publication; and (3) rollback targets gain explicit hash, manifest, and receipt requirements.

REL's relationship to the rest of the atlas is structural. EVD supplies the proof substrate; POL supplies the rights and sensitivity gates; VAL supplies the test discipline; REL closes the chain by binding all of them to a release manifest that determines what may be seen. API, MAP, UIX, and PLN are downstream of REL — they consume release state, they do not produce it.

#### 6.10.1 Subcategories

- **Catalog closure.** STAC/DCAT/PROV records linked to evidence, policy, proof, and release.
- **Promotion gates.** Governed state transitions, not file moves or cron success.
- **Artifact versioning.** Versioned filenames, partitions, root hashes, sidecars.
- **Rollback.** Stable manifests, receipts, downstream invalidation.
- **Watcher lifecycle.** WORK_CANDIDATE emission, not publication.

#### 6.10.2 Idea entries

##### KFM-IDX-REL-001 — Catalog closure links STAC, DCAT, PROV, release, and evidence

**Status.** CONFIRMED. **Category/Subcategory.** REL / Catalog closure. **Lineage.** Pass 19 P19-REL-001; convergent across Greenfield Building Plan, Pipeline Living Manual, Pass 18, Master MapLibre Atlas, and the Pass 19 5-10 and 5-15 deltas.

**Normalized statement.** A dataset or artifact is not publication-ready until its catalog metadata, provenance, evidence, policy, proof objects, and release records close consistently and resolve to one another.

**Detailed explanation.** Catalog closure is the corpus's strongest single doctrine in this category. The Greenfield Building Plan and Pipeline Living Manual [Pass 18] both define publication as the state in which catalog (STAC/DCAT), provenance (PROV-O), evidence (EvidenceBundle), policy (PolicyDecision), proof (RunReceipt, attestation sidecar), and release manifest records all reference each other consistently. The Pass 19 5-10 packet [Pass 19] adds PMTiles attestation sidecars to this set; the 5-15 packet adds CDL STAC items, classmap version refs, and source-drift records. The convergence is unusually clean: every Pass 19 delta points to catalog closure as the precondition for public exposure.

The normalized KFM posture is that "ready" is a closure property, not a process outcome. A pipeline can complete successfully and still produce unready output if any of the closure links is broken — missing evidence ref, missing provenance, unresolved policy, missing proof, or release manifest pointing to a phantom record.

**Why it matters.** Closure gives users and maintainers a traceable map from public artifact to source and review. Without it, the publication step becomes opaque and rollback becomes guesswork.

**Related ideas.** `KFM-IDX-EVD-001` (evidence closure); `KFM-IDX-EVD-002` (receipts); `KFM-IDX-MAP-003` (artifact matrix); `KFM-IDX-REL-002` (promotion as state transition).

**Dependencies.** Catalog records; evidence refs; release manifest; proof pack; source descriptors; policy decisions.

**Tensions / limitations.** Closure discipline can become bureaucratic if not thin-sliced; the corpus repeatedly recommends starting with minimal required fields and expanding profiles.

**Expansion directions.** Start with minimal closure requirements for PMTiles, CDL, and one public map layer; expand to full profile per artifact family.

**Open questions.** What is the minimum closure set for PMTiles, CDL, and a public map layer respectively?

**Suggested future work.** Create closure checklists for PMTiles and CDL fixtures and validate that a deliberately-incomplete artifact is denied.

##### KFM-IDX-REL-002 — Promotion is a governed state transition

**Status.** CONFIRMED. **Category/Subcategory.** REL / Promotion gates. **Lineage.** Pass 19 P19-REL-002; rooted in Directory Rules, Greenfield Building Plan, Pipeline Living Manual; reinforced by Pass 19 5-15 watcher governance.

**Normalized statement.** Promotion changes release state only after gates pass; it is not a file move, a cron success, a source update, or a model answer.

**Detailed explanation.** Directory Rules and the KFM doctrine layer [Pass 18] state the lifecycle plainly: `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`. Each transition is governed; the final transition to PUBLISHED is the most governed of all because it changes what the public sees. The Pass 19 5-15 packet [Pass 19] reinforces this by emphasizing that watchers — even successful watchers with valid sidecars and signed receipts — cannot promote; they emit candidates that enter the lifecycle from the WORK side, not from the PUBLISHED side.

The normalized KFM posture treats promotion as the moment when policy, evidence, validation, and catalog closure all bind to a `PromotionDecision` recorded with a `PromotionReceipt`. There is no implicit promotion in KFM doctrine. Cron jobs, watcher successes, validator passes, and steward approvals are all inputs to promotion; none of them is promotion itself.

**Why it matters.** This is the trust membrane between internal processing and public surfaces. If automation pressure causes promotion to leak — even by one well-meaning shortcut — the entire downstream trust posture (API, MAP, UIX) becomes ungrounded.

**Related ideas.** `KFM-IDX-DOC-002` (directory placement as governance boundary); `KFM-IDX-POL-001` (public-safe by default); `KFM-IDX-VAL-004` (publication gates); `KFM-IDX-REL-005` (watcher lifecycle).

**Dependencies.** `PromotionDecision`; `PromotionReceipt`; policy gate; release manifest; rollback target.

**Tensions / limitations.** Automation pressure can tempt teams to promote directly from successful watcher outputs; the corpus's default-deny posture is the structural defense against this temptation.

**Expansion directions.** Make `publication_denied` the default outcome for all new watcher lanes and require explicit steward action plus closure for any other outcome.

**Open questions.** Which actor can approve promotion for each domain, and how is that authority recorded in the receipt?

**Suggested future work.** Create a promotion dry-run fixture that DENIES an incomplete source-drift record and emits a useful `ValidationReport`.

##### KFM-IDX-REL-003 — Avoid in-place overwrites of PMTiles and large artifacts

**Status.** CONFIRMED. **Category/Subcategory.** REL / Artifact versioning. **Lineage.** Pass 19 P19-REL-003; rooted in Pass 19 5-10 PMTiles operational packet; reinforced by Master MapLibre Atlas.

**Normalized statement.** Large map artifacts should use versioned filenames, partitions, root hashes, sidecars, and immutable or digest-pinned references rather than in-place overwrites.

**Detailed explanation.** The Pass 19 5-10 packet [Pass 19] is unusually concrete on this point: PMTiles is an HTTP-Range-optimized single-file archive, and when a file is swapped in place, browsers and CDNs may continue to issue Range requests against stale cache entries, MapLibre clients may receive partial responses pointing into the wrong byte ranges, and native clients may crash or render corrupted tiles. The recommendation is versioned filenames (`layer.v2026-05-15.pmtiles`), digest-pinned references, root-hash sidecars, and partitions for very large archives.

The normalized KFM posture is that artifact identity includes a version or digest, and that release manifests reference artifacts by stable identifier rather than by mutable filename. Cache invalidation becomes a release problem rather than a CDN problem.

**Why it matters.** In-place overwrite is one of the few publication mistakes that produces silent failure modes — users see corrupted or stale tiles without any indication that the data has changed. Versioned artifacts make staleness visible and rollback trivial.

**Related ideas.** `KFM-IDX-MAP-002` (PMTiles Range and cache tests); `KFM-IDX-EVD-003` (PMTiles attestation sidecars); `KFM-IDX-VAL-004` (publication gates deny missing proofs).

**Dependencies.** Versioned artifact names; release manifest; cache/Range tests; rollback target.

**Tensions / limitations.** Partitioning and versioning increase artifact management complexity; the corpus does not yet settle on a partitioning unit for Kansas-scale public PMTiles.

**Expansion directions.** Define artifact naming and shard strategy by domain and zoom range; document rollback drill on a fixture PMTiles archive.

**Open questions.** What partitioning unit (county, HUC, tile pyramid) is best for Kansas-scale public PMTiles, and how does it interact with zoom-range partitioning?

**Suggested future work.** Create an artifact-release naming convention with rollback test on a small fixture archive.

##### KFM-IDX-REL-004 — Rollback targets need stable manifests and receipts

**Status.** CONFIRMED. **Category/Subcategory.** REL / Rollback. **Lineage.** Pass 19 P19-REL-004; rooted in KFM doctrine on reversibility; reinforced by Pass 19 5-10 PMTiles digest pinning and 5-15 source checkpoints.

**Normalized statement.** Every published artifact, layer, catalog record, and decision-support output should have a rollback target identified by stable manifests, hashes, version, release state, and receipts.

**Detailed explanation.** The KFM doctrine layer [Pass 18] treats reversibility as a system invariant: anything that can be published can be rolled back, and rollback must be a controlled process rather than a scramble. Pass 19's 5-10 packet [Pass 19] gives this operational form for PMTiles: digest-pinned references, root-hash sidecars, and release manifests that name a previous PUBLISHED state as the rollback target. The 5-15 packet adds source-side rollback: classmap versions, geometry hashes, and source checkpoints allow CDL-derived products to be reverted to a known prior state when downstream drift is detected.

The normalized KFM posture is that rollback is a closure property, not a recovery procedure. A release that does not name a rollback target is not a complete release.

**Why it matters.** Rollback discipline is what makes publication reversible in practice. Without stable manifests and receipts, rollback becomes an archeological exercise rather than a one-command operation.

**Related ideas.** `KFM-IDX-EVD-002` (receipts as process memory); `KFM-IDX-MOD-003` (geography versions as identity); `KFM-IDX-MAP-004` (viewer verification); `KFM-IDX-REL-003` (avoid in-place overwrites).

**Dependencies.** `ReleaseManifest`; rollback reference; artifact hashes; receipts; downstream cache invalidation.

**Tensions / limitations.** Rollback may need to retract downstream UI caches, AI response envelopes, and graph projections as well as primary artifacts; the corpus has not yet fully settled this propagation policy.

**Expansion directions.** Include downstream derivative invalidation in rollback manifests; document rollback drill for one PMTiles fixture and one CDL source record.

**Open questions.** How far should rollback propagate through tiles, graphs, Focus Mode caches, and Story Nodes?

**Suggested future work.** Create a rollback drill specification that names the propagation surface and demonstrates retraction.

##### KFM-IDX-REL-005 — Watcher output enters WORK_CANDIDATE, not PUBLISHED

**Status.** CONFIRMED. **Category/Subcategory.** REL / Watcher lifecycle. **Lineage.** Pass 19 P19-REL-005; rooted in Pass 19 5-15 CDL Watch governance; reinforced by Directory Rules lifecycle invariants.

**Normalized statement.** Source-drift detectors emit candidate records for review and processing; they must not publish layers, mutate canonical truth, or expose `RAW/WORK/QUARANTINE` payloads to public surfaces.

**Detailed explanation.** This is the watcher-as-non-publisher invariant in its REL form. The Pass 19 5-15 packet [Pass 19] states it plainly: CDL Watch and PLANTS Watch produce `SourceIntakeRecord` candidates with `publication_state: WORK_CANDIDATE`, and the lifecycle is `RAW → WORK_CANDIDATE → (review) → PROCESSED → CATALOG → PUBLISHED`. Watchers are good citizens of the lifecycle precisely because they emit records that enter from the WORK side and require explicit promotion.

The normalized KFM posture extends this to all watcher families: environmental probes, drift detectors, source-head checks, package monitors, and ontology drift checks all produce candidates, never publications. The corollary is that watcher output paths (outbox, queue, candidate directory) are not public surfaces and are not exposed through governed APIs without further promotion.

**Why it matters.** Watchers are valuable because they are cheap to run continuously. That cheapness becomes a liability if watchers can promote; the trust spine would degrade to whatever the cheapest detector emits.

**Related ideas.** `KFM-IDX-SRC-006` (CDL/PLANTS source-drift candidates); `KFM-IDX-POL-001` (public-safe by default); `KFM-IDX-VAL-001` (material-change gates); `KFM-IDX-REL-002` (promotion as state transition).

**Dependencies.** `SourceIntakeRecord` schema; outbox or queue; policy gate; no public API exposure for WORK state.

**Tensions / limitations.** Outbox paths proposed in Pass 19 snippets (such as `tools/ingest/cdl_watch/`) need Directory Rules validation and may require lifecycle-root adjustment.

**Expansion directions.** Place watcher state under governed `state/` or `checkpoint/` directories only after Directory Rules review; create an ADR if the location is ambiguous.

**Open questions.** Where should watcher state live under current repo conventions, and which actor owns the outbox-to-PROCESSED promotion?

**Suggested future work.** Create a Directory Rules-compliant ADR for watcher state placement before any watcher implementation lands.

### 6.11 API — Governed APIs, Contracts, Envelopes, and Cross-Surface Bindings

#### Category overview

API is the trust-membrane category. It contains the rules and patterns by which downstream surfaces — maps, viewers, drawers, planning support, AI flows — access KFM truth. Pass 18 establishes the doctrine that public clients and normal UI surfaces should consume governed APIs rather than canonical or internal stores; Pass 19 normalizes this into four explicit ideas around governed access, finite outcome envelopes, design-first contracts, and source intake envelopes for watcher candidates.

API sits downstream of EVD, POL, VAL, and REL: the API surface should never expose state that has not closed through evidence, policy, validation, and release gates. It sits upstream of MAP, UIX, and PLN: every map, drawer, story, and planning surface in KFM is in principle an API client, even when the implementation is co-located. This separation is what makes the trust membrane real rather than rhetorical.

#### 6.11.1 Subcategories

- **Trust membrane.** Governed APIs as the only public path to canonical truth.
- **Outcome envelopes.** Finite, governed response shapes; deny is a valid outcome.
- **Design-first contracts.** Schema and contract evolution before implementation.
- **Source intake envelopes.** `SourceIntakeRecord` and watcher candidate boundaries.

#### 6.11.2 Idea entries

##### KFM-IDX-API-001 — Governed APIs are the trust membrane, not optional plumbing

**Status.** CONFIRMED. **Category/Subcategory.** API / Trust membrane. **Lineage.** Pass 19 P19-API-001; rooted in Greenfield Building Plan, Whole-UI Governed AI Expansion Report, and Directory Rules.

**Normalized statement.** Public clients and normal UI surfaces must consume governed APIs that enforce release state, policy, evidence, and rights — never read canonical stores, raw tiles, or internal triplets directly.

**Detailed explanation.** The Greenfield Building Plan and the Whole-UI Governed AI Expansion Report [Pass 18] both treat governed APIs as the structural boundary between internal processing and public surfaces. A governed API is not merely an HTTP interface; it is the place where release state, policy decisions, evidence references, and rights posture are enforced before any payload leaves the trust spine. The Directory Rules reinforce this by drawing `ui`, `web`, and `api` as compatibility surfaces that depend on the trust roots rather than parallel publication paths.

The Pass 19 normalization extends this in two directions. First, the rule applies to AI flows as well as map and viewer flows: an AI answer is an API outcome, not a sovereign generation. Second, the rule applies even when the API and UI are co-located in the same monorepo — co-location does not erase the boundary, and the API contract is the place where the membrane is enforced.

**Why it matters.** Without a governed API membrane, every consumer becomes its own enforcement point, and the trust spine degrades to whichever consumer enforces least.

**Related ideas.** `KFM-IDX-DOC-001` (governance ahead of polish); `KFM-IDX-MAP-001` (MapLibre as renderer, not source of truth); `KFM-IDX-UIX-002` (Focus Mode evidence boundedness); `KFM-IDX-REL-002` (promotion as state transition).

**Dependencies.** API contract; release state enforcement; policy enforcement; evidence resolution; rights posture.

**Tensions / limitations.** Strict membrane enforcement can introduce latency and friction; the corpus's response is to thin-slice the membrane and cache governed outcomes rather than bypass enforcement.

**Expansion directions.** Audit every UI and AI surface for a governed-API entry point; document the exact enforcement responsibilities of each route.

**Open questions.** Which routes currently exist, which are governed in the full sense, and which are still candidate or admin-only?

**Suggested future work.** Produce a route inventory ADR with enforcement-responsibility tables for each route, marked CONFIRMED, PROPOSED, or NEEDS VERIFICATION per route.

##### KFM-IDX-API-002 — Outcome envelopes are finite, governed, and include deny

**Status.** CONFIRMED. **Category/Subcategory.** API / Outcome envelopes. **Lineage.** Pass 19 P19-API-002; rooted in Whole-UI Governed AI Expansion Report and Pipeline Living Manual.

**Normalized statement.** Governed API responses — including AI answers — should follow finite, schema-bounded envelopes that always include outcome state, evidence references, policy decision, rights posture, and explicit `denied` / `narrowed` / `bounded` outcomes alongside `granted`.

**Detailed explanation.** The Whole-UI Governed AI Expansion Report [Pass 18] introduces governed outcome envelopes as the way to keep AI fluency from substituting for evidence. Every governed response carries a bounded shape: `outcome`, `evidence_refs`, `policy_decision`, `rights_posture`, `confidence_or_scope`, and `release_state`. Deny is a first-class outcome — not an error condition — and so are `narrowed` (the system answered, but with reduced scope) and `bounded` (the system answered, but with explicit confidence or sensitivity limits).

The Pass 19 normalization adds source-drift and artifact-integrity envelopes to this pattern: a CDL drift envelope returns a `SourceIntakeRecord` reference with `publication_state: WORK_CANDIDATE`, and a PMTiles integrity envelope returns `signature_verified` and `root_hash` fields. The shape varies by surface, but the principle is constant: envelopes are finite, governed, and visibly include the deny path.

**Why it matters.** Finite envelopes are how downstream surfaces (map, drawer, planning) know when to render, what to render, and when to render nothing — without parsing free-form text or guessing at empty responses.

**Related ideas.** `KFM-IDX-DOC-005` (governed AI is interpretive, not authoritative); `KFM-IDX-POL-001` (public-safe by default); `KFM-IDX-EVD-001` (evidence closure); `KFM-IDX-UIX-001` (Evidence Drawer surfaces).

**Dependencies.** Envelope JSON schemas; outcome enum; evidence-ref resolution; policy-decision binding; rights posture vocabulary.

**Tensions / limitations.** Excessively granular envelopes can fragment the client; the corpus recommends one envelope family per surface with explicit extensions for drift, integrity, and AI flows.

**Expansion directions.** Define envelope schemas for each governed surface family — map, drawer, planning, AI, drift, integrity — and validate downstream clients against them.

**Open questions.** Which envelope fields are mandatory across all surfaces, and which are surface-specific?

**Suggested future work.** Publish envelope JSON Schemas in `data/contracts/` (PROPOSED path) with deny-case fixtures.

##### KFM-IDX-API-003 — Contracts and schemas are design-first

**Status.** CONFIRMED. **Category/Subcategory.** API / Design-first contracts. **Lineage.** Pass 19 P19-API-003; rooted in Greenfield Building Plan and Pipeline Living Manual.

**Normalized statement.** API schemas and contracts should be authored as schemas first, evolved through versioning, and validated by no-network fixtures before any implementation depends on them.

**Detailed explanation.** The Greenfield Building Plan [Pass 18] is unambiguous about contract-first design: schemas precede code, fixtures precede live data, and validators precede production traffic. The Pipeline Living Manual extends this to the whole pipeline, and the Pass 19 deltas reinforce it for source-drift records and artifact-integrity sidecars — both of which appear in the corpus as schema fragments before they appear as implementations.

The KFM normalization is that an API change is a schema change, not a code change. Versioning, deprecation, and migration are first-class concerns; breaking changes require ADRs; and every contract has at least one fixture (positive and negative) under version control.

**Why it matters.** Design-first contracts allow validation, fixture authoring, and downstream client work to proceed independently and reversibly. Code-first APIs invert this and tend to accumulate undocumented behavior.

**Related ideas.** `KFM-IDX-DOC-004` (contracts and schemas live in registries); `KFM-IDX-VAL-005` (no-network dry runs); `KFM-IDX-REL-001` (catalog closure); `KFM-IDX-API-002` (outcome envelopes).

**Dependencies.** Schema registry; fixture set; validator; ADR template; deprecation policy.

**Tensions / limitations.** Schema-first discipline slows initial implementation; the corpus argues that the cost is repaid in reversibility and clarity.

**Expansion directions.** Document a schema-evolution policy with explicit deprecation paths; require fixture coverage for both positive and negative cases.

**Open questions.** Which schema registry tooling is currently in use, and which contracts have negative-case fixtures?

**Suggested future work.** Schema-by-schema fixture audit recorded as NEEDS VERIFICATION pending live repo access.

##### KFM-IDX-API-004 — Source intake records are the watcher envelope

**Status.** CONFIRMED. **Category/Subcategory.** API / Source intake envelopes. **Lineage.** Pass 19 P19-API-004; rooted in Pass 19 5-15 CDL/PLANTS Watch packet.

**Normalized statement.** Watcher candidates should surface through a `SourceIntakeRecord`-shaped envelope that includes source URLs, fingerprints, `classmap_version`, geometry hashes, materiality reason, `publication_state: WORK_CANDIDATE`, and a steward review markdown payload.

**Detailed explanation.** The Pass 19 5-15 packet [Pass 19] introduces `SourceIntakeRecord` as the canonical envelope for source-drift candidates. It carries source URLs, fingerprints, the version of the class ontology in use (`classmap_version`), per-geometry hashes for the AOI, a structured materiality reason, the lifecycle state (`WORK_CANDIDATE` by default), and a markdown payload suitable for steward review in an Evidence Drawer or admin surface.

The KFM normalization extends this to other watchers: environmental probes, package monitors, ontology drift checks, and rights-change monitors. The pattern is consistent — emit a structured candidate envelope with enough context for human review, and never bypass that envelope to write directly into PROCESSED or PUBLISHED.

**Why it matters.** A consistent intake envelope makes watcher output reviewable, comparable, and aggregable across domains. Without it, each watcher becomes its own ad-hoc surface.

**Related ideas.** `KFM-IDX-SRC-006` (CDL/PLANTS source-drift candidates); `KFM-IDX-EVD-005` (Evidence Drawer payloads); `KFM-IDX-REL-005` (watcher lifecycle); `KFM-IDX-VAL-002` (signed probe receipts).

**Dependencies.** `SourceIntakeRecord` schema; classmap registry; fingerprint policy; geometry hash policy; steward review template.

**Tensions / limitations.** Different watcher families may need different mandatory fields; the corpus does not yet settle this fully.

**Expansion directions.** Define a `SourceIntakeRecord` core profile plus per-watcher extensions; validate candidate records with no-network fixtures.

**Open questions.** Which fields are mandatory across all watchers, and which are watcher-specific?

**Suggested future work.** Draft `data/contracts/source_intake_record.schema.json` as PROPOSED with a positive and a negative fixture pair.

### 6.12 MAP — MapLibre, PMTiles, Artifact Matrix, Viewer Verification, and Map Trust States

#### Category overview

MAP is the renderer-and-artifact category. It covers MapLibre as the public-facing rendering engine, PMTiles as the dominant artifact delivery format, COG and GeoParquet as raster and tabular co-formats, viewer-side verification of artifact integrity, and the explicit trust states that govern what a map may display. Pass 18 organized MAP as the largest reference area, with the Master MapLibre Atlas covering rendering, layer types, performance, accessibility, and operational considerations; Pass 19 normalizes this into five ideas that emphasize the renderer's downstream status and the operational integrity requirements that protect users from corrupted or stale tiles.

The Pass 19 5-10 packet [Pass 19] is the strongest single influence on this chapter. It introduces PMTiles attestation, root-hash sidecars, viewer-side verification, and digest-pinned references — all of which reinforce the doctrine that the map renderer is a consumer of governed truth, not a producer of it. The category's relationship to REL, EVD, VAL, and POL is therefore unusually tight: MAP cannot do its job correctly unless those upstream categories have closed.

#### 6.12.1 Subcategories

- **Renderer downstream.** MapLibre as renderer, not authority.
- **PMTiles operations.** Range, caching, attestation, root hashes, sidecars.
- **Artifact matrix.** COG, GeoParquet, PMTiles, STAC roles.
- **Viewer verification.** Fail-closed checks on attestation and digest.
- **Map trust states.** Granted, narrowed, denied, bounded states for layers and scenes.

#### 6.12.2 Idea entries

##### KFM-IDX-MAP-001 — MapLibre is a downstream renderer, not a source of truth

**Status.** CONFIRMED. **Category/Subcategory.** MAP / Renderer downstream. **Lineage.** Pass 19 P19-MAP-001; rooted in Master MapLibre Atlas and reinforced across all Pass 18 atlases.

**Normalized statement.** MapLibre, MapLibre GL JS, and viewer code are renderers of governed artifacts; they must not be treated as canonical truth, authoritative sources, or replacements for catalog and evidence records.

**Detailed explanation.** The Master MapLibre Atlas [Pass 18] is structured around the renderer-versus-truth distinction. MapLibre handles styling, projection, layer composition, interactivity, and performance — none of which is authority over content. The atlas covers more than fifty rendering and integration concerns, and every one of them is downstream of catalog and release decisions. The Pass 19 normalization adds that this remains true even for highly visual surfaces (3D scenes, time-aware overlays, popovers) where the rhetorical pressure to treat the map as the source is highest.

The operational consequence is that map layers are bound to governed APIs and artifact references, not to file paths or live URLs that bypass the trust spine. If a layer cannot find its governed binding, the renderer should fail closed or render a narrowed/denied state rather than render arbitrary content.

**Why it matters.** Maps are the most persuasive surface in KFM. Treating the renderer as the source would invert the trust spine — every visual would become its own authority, and evidence, policy, and release would degrade to optional metadata.

**Related ideas.** `KFM-IDX-API-001` (governed APIs as trust membrane); `KFM-IDX-MAP-004` (viewer verification fail-closed); `KFM-IDX-MAP-005` (map trust states); `KFM-IDX-REP-003` (cartography as policy choice).

**Dependencies.** Layer binding to governed API; style discipline; trust-state vocabulary.

**Tensions / limitations.** Rendering-engine features (live styling, expressions, runtime data) can blur the renderer/source boundary; the corpus's guidance is to bind all data sources to governed envelopes regardless of dynamism.

**Expansion directions.** Document a renderer-binding contract that explicitly names allowed and disallowed data sources for production maps.

**Open questions.** Which expressions and runtime patterns are acceptable in production styles versus admin or development styles?

**Suggested future work.** Author a renderer-binding policy document referenced from `KFM-IDX-MAP-004` and `KFM-IDX-API-001`.

##### KFM-IDX-MAP-002 — PMTiles needs Range, cache, and integrity tests

**Status.** CONFIRMED. **Category/Subcategory.** MAP / PMTiles operations. **Lineage.** Pass 19 P19-MAP-002; rooted in Pass 19 5-10 PMTiles operational packet.

**Normalized statement.** PMTiles delivery should be validated for HTTP Range support, cache behavior, root hash integrity, and digest-pinned references — and tests should exercise the failure modes that the format exposes, including stale Range cache and signature mismatch.

**Detailed explanation.** The Pass 19 5-10 packet [Pass 19] is unusually concrete on PMTiles operational risks. PMTiles is a single-file archive that depends on HTTP Range requests for partial reads. When a CDN does not support Range, when an origin disables Range under specific conditions, or when a file is overwritten in place while clients hold cache entries, the result can be silent corruption — pointers in the directory point into bytes that no longer belong to the requested tile. The packet recommends Range support tests, cache-behavior tests, root-hash verification, and digest-pinned references in release manifests.

The KFM normalization adds that these tests are operational artifacts: they belong in CI fixtures, they emit signed receipts when run against live origins, and their failures deny publication rather than warn. The Master MapLibre Atlas's discussion of caching and tile delivery [Pass 18] aligns with this normalization.

**Why it matters.** PMTiles failures are silent. Without operational tests, the first sign of trouble is a user-visible rendering corruption — by which point trust has already been damaged.

**Related ideas.** `KFM-IDX-EVD-003` (PMTiles attestation sidecars); `KFM-IDX-REL-003` (avoid in-place overwrites); `KFM-IDX-MAP-004` (viewer verification); `KFM-IDX-VAL-005` (no-network dry runs).

**Dependencies.** PMTiles fixture; Range-aware HTTP client; cache test harness; root-hash sidecar; release manifest.

**Tensions / limitations.** Some hosting environments do not fully support Range; the corpus recommends documenting per-environment behavior rather than assuming uniform support.

**Expansion directions.** Build a small PMTiles fixture and a Range/cache test harness as a thin slice; document per-environment Range behavior.

**Open questions.** Which Kansas-relevant hosting environments offer reliable Range, and which require origin reconfiguration?

**Suggested future work.** Land a `PR-pmtiles-ops-0001` thin slice with fixture, Range/cache tests, and signed-receipt CI.

##### KFM-IDX-MAP-003 — The COG / GeoParquet / PMTiles / STAC artifact matrix is the map's evidence shape

**Status.** CONFIRMED. **Category/Subcategory.** MAP / Artifact matrix. **Lineage.** Pass 19 P19-MAP-003; rooted in Master MapLibre Atlas and Pass 18 catalog/atlas reports.

**Normalized statement.** Public map layers should reference an explicit artifact family — COG for raster, GeoParquet for tabular, PMTiles for vector tiles, STAC for catalog — with documented role, projection, schema, and provenance.

**Detailed explanation.** The Master MapLibre Atlas [Pass 18] organizes map artifacts by family: raster (COG, georeferenced imagery), tabular (GeoParquet, CSV/Parquet exports), vector tiles (PMTiles, MVT), and catalog (STAC, DCAT). Each family carries different operational concerns — projection, indexing, tiling, partitioning, refresh cadence — and each maps to different evidence patterns. The Pass 19 5-15 packet's CDL recommendations [Pass 19] illustrate this: yearly CDL bundles are represented as STAC items with raster assets and class ontology references, distinguishing them from PMTiles-derived vector products that downstream maps may consume.

The KFM normalization is that every public map layer names its artifact family, its evidence path, and its release reference. Mixed-family layers (raster underlying with vector overlays) declare each component. This becomes the basis for renderer-side verification and for catalog closure.

**Why it matters.** Without an artifact matrix, layers become opaque to provenance — the renderer knows how to display them, but no other surface knows what they are.

**Related ideas.** `KFM-IDX-FIE-002` (remote-sensing labeling); `KFM-IDX-FIE-004` (catalog normalization); `KFM-IDX-REL-001` (catalog closure); `KFM-IDX-EVD-001` (evidence closure).

**Dependencies.** Artifact family enumeration; STAC profiles; projection metadata; schema registries.

**Tensions / limitations.** Some artifacts (3D scenes, mesh tiles, custom binaries) do not fit cleanly; the corpus's guidance is to define a KFM-specific family for them rather than to force-fit a standard.

**Expansion directions.** Author KFM artifact-family profiles for raster, vector, tabular, catalog, and scene families with examples.

**Open questions.** What is the canonical KFM family for archaeological 3D scenes, and how is it referenced from STAC?

**Suggested future work.** Draft `docs/standards/ARTIFACT_FAMILIES.md` as PROPOSED with one example per family.

##### KFM-IDX-MAP-004 — Viewer-side verification fails closed

**Status.** CONFIRMED. **Category/Subcategory.** MAP / Viewer verification. **Lineage.** Pass 19 P19-MAP-004; rooted in Pass 19 5-10 PMTiles attestation packet.

**Normalized statement.** Map viewers should verify root hashes, attestation signatures, and digest-pinned references before rendering tile content, and should fail closed (refuse to render, render a denied state, or render a narrowed substitute) when verification fails.

**Detailed explanation.** The Pass 19 5-10 packet [Pass 19] introduces viewer-side verification as the last line of defense against PMTiles corruption. Even with versioned filenames, root hashes, and signed attestations on the server side, a viewer that does not verify can still render corrupted content if the CDN or the network introduces a fault. The recommendation is that the viewer computes or checks the root hash and signature, and that a verification failure produces an explicit denied/narrowed state visible to the user rather than a silent fallback to stale or corrupted tiles.

The KFM normalization extends this beyond PMTiles to any artifact that carries an attestation sidecar: COG checksum verification, GeoParquet schema verification, and STAC item integrity checks. Fail-closed is the default; fail-open is an admin-only configuration with audit logging.

**Why it matters.** Viewer-side verification protects users from CDN faults, network corruption, and accidental in-place overwrites. Without it, server-side discipline has no enforcement at the user's eye.

**Related ideas.** `KFM-IDX-EVD-003` (PMTiles attestation sidecars); `KFM-IDX-MAP-002` (PMTiles Range/cache tests); `KFM-IDX-REL-003` (avoid in-place overwrites); `KFM-IDX-VAL-004` (publication gates).

**Dependencies.** Root-hash computation; signature verification; renderer fallback; denied-state UI.

**Tensions / limitations.** Verification adds latency on initial layer load; the corpus's guidance is to amortize verification across tile reads rather than block first render.

**Expansion directions.** Implement viewer-side verification as a renderer plugin with denied-state and narrowed-state fallbacks; document UX for verification failures.

**Open questions.** What is the denied-state UX (banner, modal, layer absence) for a verification failure on a primary public layer?

**Suggested future work.** Land a viewer-verification plugin spec with denied-state UX defined in coordination with `KFM-IDX-UIX-001`.

##### KFM-IDX-MAP-005 — Map trust states are first-class layer metadata

**Status.** CONFIRMED. **Category/Subcategory.** MAP / Map trust states. **Lineage.** Pass 19 P19-MAP-005; rooted in Whole-UI Governed AI Expansion Report and Master MapLibre Atlas.

**Normalized statement.** Every public-facing map layer, overlay, and scene should carry an explicit trust state — `granted`, `narrowed`, `bounded`, `denied`, `candidate` — visible in the renderer and recorded in release metadata.

**Detailed explanation.** The Whole-UI Governed AI Expansion Report [Pass 18] introduces explicit trust states for outcome envelopes. The Pass 19 normalization extends the same vocabulary to map layers: a layer is `granted` when fully released, `narrowed` when scope or precision has been reduced, `bounded` when confidence or freshness limits are recorded, `denied` when policy or rights prevent display, and `candidate` when the layer reflects watcher output not yet promoted. These states are not UI conveniences; they are layer metadata that the renderer consumes and the Evidence Drawer surfaces.

The operational consequence is that map composition becomes trust-aware: a public scene composed of `granted` layers may behave differently from a scene that includes a `narrowed` archaeological generalization or a `candidate` source-drift overlay. The renderer composes the states, the drawer explains them, and the catalog records them.

**Why it matters.** Without first-class trust states, users cannot tell the difference between a fully released layer and a candidate or narrowed one. The visual surface flattens trust distinctions.

**Related ideas.** `KFM-IDX-API-002` (outcome envelopes); `KFM-IDX-UIX-001` (Evidence Drawer); `KFM-IDX-POL-002` (sovereignty/sensitivity); `KFM-IDX-REL-001` (catalog closure).

**Dependencies.** Trust-state enum; layer metadata schema; renderer support; drawer payload; catalog field.

**Tensions / limitations.** Excessive state vocabulary fragments the UI; the corpus's guidance is to fix a small enum and extend by ADR.

**Expansion directions.** Fix a five-state enum (`granted`, `narrowed`, `bounded`, `denied`, `candidate`) and document composition rules for multi-layer scenes.

**Open questions.** How are mixed trust states displayed in a multi-layer scene — by worst-state, by per-layer indicator, or by a composite indicator?

**Suggested future work.** Draft a `docs/standards/MAP_TRUST_STATES.md` profile as PROPOSED with composition rules.

### 6.13 UIX — Evidence Drawer, Focus Mode, Review Surfaces, and Story Nodes

#### Category overview

UIX is the surfacing category. It covers the user-visible patterns by which evidence, policy, review state, and release state become legible: the Evidence Drawer attached to layers, popovers, and AI answers; Focus Mode for evidence-bounded exploration; steward and reviewer surfaces with structured summaries; and Story Nodes that inherit release state and rights posture from their constituent layers and evidence. Pass 18 develops these surfaces across the Whole-UI Governed AI Expansion Report, the Master MapLibre Atlas, and the storytelling chapters; Pass 19 normalizes UIX into four ideas that emphasize the mandatory presence of the drawer, the evidence-bounded nature of Focus Mode, the steward summary discipline of review surfaces, and the inherited-state property of Story Nodes.

UIX is downstream of API, REL, EVD, POL, and VAL. It is also upstream of public trust in the sense that a well-designed UIX makes the upstream discipline visible. The corpus repeatedly warns against polish that hides governance — a slick UI that omits evidence references, policy decisions, or trust-state indicators is worse than a plainer UI that exposes them.

#### 6.13.1 Subcategories

- **Evidence Drawer.** Mandatory drawer attached to layers, popovers, and AI answers.
- **Focus Mode.** Evidence-bounded, source-traceable exploration.
- **Review surfaces.** Steward and reviewer screens with structured summaries.
- **Story Nodes.** Composite narratives that inherit release state and rights posture.

#### 6.13.2 Idea entries

##### KFM-IDX-UIX-001 — Evidence Drawer is mandatory on layers, popovers, and AI answers

**Status.** CONFIRMED. **Category/Subcategory.** UIX / Evidence Drawer. **Lineage.** Pass 19 P19-UIX-001; rooted in Whole-UI Governed AI Expansion Report.

**Normalized statement.** Every public-facing surface that displays content from KFM — map layer, popover, scene, AI answer, story node — must expose an Evidence Drawer with evidence references, source descriptors, policy decision, review state, and rights posture.

**Detailed explanation.** The Whole-UI Governed AI Expansion Report [Pass 18] treats the Evidence Drawer as the universal trust surface. It is the place where governance becomes legible to the user: which sources support this claim, when were they reviewed, under what policy, with what rights posture, and at what release state. The drawer is not a decorative panel; it is a contract surface between the trust spine and the public.

The Pass 19 normalization adds three points. First, the drawer is mandatory — there is no governed surface in KFM that should ship without it. Second, the drawer payloads are versioned and bound to the underlying evidence and release records, so that a drawer cannot drift from its layer or scene. Third, the drawer includes outcome state for AI answers (granted, narrowed, bounded, denied) and trust state for layers (granted, narrowed, bounded, denied, candidate), and surfaces them with consistent vocabulary.

**Why it matters.** The drawer is what prevents polish from hiding governance. A surface without a drawer is a surface that cannot be inspected, corrected, or rolled back from the user's seat.

**Related ideas.** `KFM-IDX-EVD-005` (drawer payloads); `KFM-IDX-API-002` (outcome envelopes); `KFM-IDX-MAP-005` (map trust states); `KFM-IDX-DOC-005` (governed AI).

**Dependencies.** Drawer payload schema; evidence-ref resolution; release-state binding; rights vocabulary; review-state vocabulary.

**Tensions / limitations.** Drawers add UI weight; the corpus's guidance is to expose a compact summary with an expandable detail panel rather than to flatten the drawer for compactness.

**Expansion directions.** Define a drawer payload schema that covers map layers, popovers, AI answers, and story nodes consistently.

**Open questions.** What is the minimum mandatory drawer payload, and what fields are optional per surface?

**Suggested future work.** Draft `data/contracts/evidence_drawer_payload.schema.json` (PROPOSED path) with fixtures for each surface family.

##### KFM-IDX-UIX-002 — Focus Mode stays evidence-bounded

**Status.** CONFIRMED. **Category/Subcategory.** UIX / Focus Mode. **Lineage.** Pass 19 P19-UIX-002; rooted in Whole-UI Governed AI Expansion Report.

**Normalized statement.** Focus Mode should bound exploration to evidence-supported scope, refusing to generate, extrapolate, or summarize beyond the underlying `EvidenceBundle` set, and should indicate when scope has been narrowed or denied.

**Detailed explanation.** Focus Mode in the Whole-UI Governed AI Expansion Report [Pass 18] is a guided exploration surface that combines map context, AI explanation, and evidence references. The risk is that AI fluency in Focus Mode will produce plausible-sounding extrapolations that exceed the evidence — and because Focus Mode is visually authoritative, users will treat extrapolation as confirmation.

The Pass 19 normalization is that Focus Mode is evidence-bounded by design. Its generation surfaces consume governed outcome envelopes, its summaries are accompanied by evidence references in the drawer, and its scope is narrowed (rather than extended) when evidence is thin. Where Focus Mode would otherwise have to extrapolate, it explicitly denies or narrows — and the denied/narrowed state is visible.

**Why it matters.** Focus Mode is the surface where AI fluency and evidence discipline meet most directly. If fluency wins, the trust spine becomes ornamental. If evidence wins, Focus Mode becomes the strongest demonstration of governed AI in the system.

**Related ideas.** `KFM-IDX-DOC-005` (governed AI); `KFM-IDX-API-002` (outcome envelopes); `KFM-IDX-UIX-001` (Evidence Drawer); `KFM-IDX-EVD-001` (evidence closure).

**Dependencies.** Governed envelope; evidence resolution; narrowed/denied UX; scope vocabulary.

**Tensions / limitations.** Users may prefer fluent extrapolation over evidence-bounded answers; the corpus's response is that bounded-but-honest answers serve users better than fluent-but-untraceable answers.

**Expansion directions.** Audit Focus Mode prompts and templates against the governed envelope; expose narrowed/denied state prominently.

**Open questions.** How should Focus Mode communicate "evidence is thin" without undermining usability for valid narrow-scope answers?

**Suggested future work.** Draft a Focus Mode prompt/template policy with examples of granted, narrowed, bounded, and denied states.

##### KFM-IDX-UIX-003 — Review surfaces use steward summaries

**Status.** CONFIRMED. **Category/Subcategory.** UIX / Review surfaces. **Lineage.** Pass 19 P19-UIX-003; rooted in Whole-UI Governed AI Expansion Report and Pass 19 5-15 source-drift packet.

**Normalized statement.** Steward and reviewer surfaces should present structured `steward_review_summary` payloads — what changed, materiality reason, policy implications, rollback target, next-action options — rather than raw diffs or free-text logs.

**Detailed explanation.** The Whole-UI Governed AI Expansion Report [Pass 18] introduces steward review as a first-class flow, not an afterthought. The Pass 19 5-15 packet [Pass 19] gives this concrete shape for source drift: a `steward_review_summary` markdown payload that includes what changed, materiality reason, policy implications, rollback target, and an explicit list of next actions (promote to PROCESSED, request expansion, deny, escalate). The same shape applies to artifact-integrity reviews, rights-change reviews, and ontology-drift reviews.

The KFM normalization is that review surfaces are not log viewers — they are decision surfaces. A reviewer should be able to make a defensible decision from the summary alone, without parsing raw diffs or correlating multiple log sources. The summary is also part of the audit trail and is preserved alongside the resulting promotion or denial decision.

**Why it matters.** Structured summaries are how review scales. Without them, reviewer load grows linearly with watcher count and eventually breaks the trust spine.

**Related ideas.** `KFM-IDX-EVD-005` (drawer payloads); `KFM-IDX-SRC-006` (CDL/PLANTS candidates); `KFM-IDX-REL-002` (promotion as state transition); `KFM-IDX-POL-005` (publication denial).

**Dependencies.** Summary payload schema; review surface UI; next-action vocabulary; decision audit log.

**Tensions / limitations.** Summary discipline can flatten nuance; the corpus's guidance is to keep the structured summary as the default view with an "expand to raw" affordance.

**Expansion directions.** Define summary payload schemas per review family; standardize next-action vocabulary across families.

**Open questions.** Which next-action vocabulary spans all review surfaces, and which actions are family-specific?

**Suggested future work.** Draft a `steward_review_summary.schema.json` (PROPOSED path) covering source-drift, integrity, rights, and ontology reviews.

##### KFM-IDX-UIX-004 — Story Nodes inherit release state and rights posture

**Status.** CONFIRMED. **Category/Subcategory.** UIX / Story Nodes. **Lineage.** Pass 19 P19-UIX-004; rooted in Whole-UI Governed AI Expansion Report and Pass 18 storytelling chapters.

**Normalized statement.** Composite narrative surfaces — Story Nodes, story arcs, time tours — must inherit the worst release state and rights posture of their constituent layers, evidence, and AI outputs, and must surface this inheritance in their drawer.

**Detailed explanation.** Story Nodes are composite surfaces that combine map layers, evidence references, AI explanations, and narrative structure. Each component carries its own release state, rights posture, and trust state; the question is what the composite carries. The Whole-UI Governed AI Expansion Report [Pass 18] and Pass 19's normalization answer this with inheritance: the composite inherits the worst state of its components, so that a story node combining a fully released map layer with a candidate AI answer is treated as candidate overall.

The KFM normalization adds that inheritance is visible. The story node's drawer surfaces the inheritance chain — which component contributed which state — so that a viewer or reviewer can trace the composite back to its sources. Rollback of a constituent component requires the composite's release manifest to be updated as well.

**Why it matters.** Without inheritance, a story can be composed from mixed-trust components and presented as a single fully-released artifact, leaking lower-trust content under a high-trust surface.

**Related ideas.** `KFM-IDX-REL-001` (catalog closure); `KFM-IDX-MAP-005` (map trust states); `KFM-IDX-UIX-001` (Evidence Drawer); `KFM-IDX-REL-004` (rollback targets).

**Dependencies.** Composite manifest; inheritance rule; drawer payload; rollback propagation.

**Tensions / limitations.** Strict worst-state inheritance may make some stories impossible to publish; the corpus's guidance is to design stories that respect their constituent states rather than to relax inheritance.

**Expansion directions.** Define a composite-manifest schema with explicit inheritance rules and rollback propagation; pilot one story node with mixed-state components.

**Open questions.** How should inheritance be visualized when the worst state is candidate, and how does that interact with public exposure rules?

**Suggested future work.** Draft a `composite_manifest.schema.json` (PROPOSED path) with inheritance rules and a candidate-state example.

### 6.14 PLN — Planning Support, Hazards, Domain Lanes, and Source-Change Governance

#### Category overview

PLN is the planning-support category. It covers decision-support surfaces — hazards layering, scenario comparison, equity overlays, infrastructure planning aids — and the discipline that distinguishes planning support from operational alerting, regulatory authority, or emergency response. Pass 18 develops planning support across the hazards, infrastructure, equity, and storytelling chapters, while warning explicitly that KFM is not an emergency alerting system and not a regulatory authority. Pass 19 normalizes PLN into four ideas that emphasize participation and visible assumptions, hazards-as-context-not-alerting, domain lanes as proof-bearing slices, and the Pass 19→20 expansion as source-change governance plus artifact integrity.

PLN is the most synthesized category in the dependency order. It depends on every prior category — DOC for governance frame, REP for representation discipline, SRC for source descriptors, MOD for model boundedness, EVD for evidence closure, POL for policy posture, VAL for validation, ANA for analytical care, FIE for capture discipline, REL for release governance, API for membrane enforcement, MAP for renderer discipline, and UIX for surface legibility. A failure in any upstream category surfaces as a failure in planning support.

#### 6.14.1 Subcategories

- **Planning participation.** Equity, scenarios, participation overlays.
- **Hazards as context.** Hazards layers as context, not emergency alerting.
- **Domain lanes.** Domain-specific proof-bearing slices (habitat, archaeology, hydrology, atmosphere).
- **Source-change governance.** Pass 19→20 expansion focus: source drift and artifact integrity.

#### 6.14.2 Idea entries

##### KFM-IDX-PLN-001 — Planning support needs participation, equity, and scenario discipline

**Status.** CONFIRMED. **Category/Subcategory.** PLN / Planning participation. **Lineage.** Pass 19 P19-PLN-001; rooted in Pass 18 planning and equity chapters.

**Normalized statement.** Planning support surfaces — scenario comparison, equity overlays, infrastructure-planning aids, participatory mapping — should expose assumptions, scenario boundaries, equity dimensions, and stakeholder participation visibly, and should refuse to present scenarios as predictions.

**Detailed explanation.** Pass 18's planning chapters [Pass 18] develop planning support as a fundamentally different category from operational alerting or regulatory authority. A scenario is a structured exploration of possibilities; an equity overlay is an analytic dimension; a participatory mapping surface is a co-production tool. None of them is a prediction, and none of them is binding. The corpus repeatedly warns that decision-support surfaces that drift toward prediction or authority degrade public trust and expose KFM to misuse.

The Pass 19 normalization is that planning support should make its assumptions visible in the surface itself — not buried in documentation. A scenario surface names the time horizon, the input variables, the model boundedness, the data vintages, and the participation set. An equity overlay names the equity dimension, the data sources, the aggregation choices, and the known limitations. Visibility is the structural defense against misuse.

**Why it matters.** Planning support is the surface most likely to be quoted out of context — by media, by litigants, by decision-makers under time pressure. Visible assumptions are how the surface defends itself.

**Related ideas.** `KFM-IDX-DOC-005` (governed AI); `KFM-IDX-REP-002` (uncertainty surfacing); `KFM-IDX-MOD-002` (model boundedness); `KFM-IDX-UIX-001` (Evidence Drawer).

**Dependencies.** Scenario manifest schema; equity dimension vocabulary; participation registry; assumption surface.

**Tensions / limitations.** Visible-assumption discipline can make planning surfaces dense; the corpus's guidance is to use the drawer for full assumptions and the primary surface for summary.

**Expansion directions.** Define a `scenario_manifest.schema.json` profile and a primary-surface summary pattern; pilot one Kansas-relevant planning scenario.

**Open questions.** Which Kansas planning domain best supports a thin-slice scenario manifest pilot — hazards, infrastructure, ecology, or hydrology?

**Suggested future work.** Author a Kansas-relevant scenario manifest pilot referencing EXP-014.

##### KFM-IDX-PLN-002 — Hazards layers are context, not emergency alerting

**Status.** CONFIRMED. **Category/Subcategory.** PLN / Hazards as context. **Lineage.** Pass 19 P19-PLN-002; rooted in Pass 18 hazards chapter.

**Normalized statement.** KFM hazards layers should provide historical and contextual information for planning; they are not real-time emergency alerting, they are not regulatory determinations, and they should label themselves as such on every surface.

**Detailed explanation.** Pass 18's hazards chapter [Pass 18] makes the categorical distinction plainly: KFM contributes to risk understanding and planning by surfacing historical hazards, modeled exposure, infrastructure proximity, and policy-relevant context — but does not alert, does not warn in real time, and does not bind regulatory action. This is a structural decision rooted in capability, in legal posture, and in the trust spine: real-time alerting would require operational SLAs, regulatory determination would require legal authority, and KFM has chosen neither.

The Pass 19 normalization is that the disclaimer is not buried — it is part of the surface vocabulary. Hazards layers carry a "planning context, not alerting" label in their drawer and in their summary. Public surfaces that include hazards layers respect the same label. If KFM ever introduces something closer to operational hazard information, it does so as a separate, clearly-bounded surface with its own gates and disclaimers.

**Why it matters.** Hazard surfaces that drift toward alerting expose KFM to liability and the public to harm. The structural defense is to keep the planning/alerting distinction visible.

**Related ideas.** `KFM-IDX-DOC-003` (KFM is not regulatory/emergency); `KFM-IDX-POL-001` (public-safe by default); `KFM-IDX-MAP-005` (map trust states); `KFM-IDX-UIX-001` (Evidence Drawer).

**Dependencies.** Hazards layer manifest; surface vocabulary; disclaimer placement; trust state.

**Tensions / limitations.** Users in time pressure may want alerting behavior; the corpus's response is that pointing to NWS, FEMA, or state emergency channels is the correct service to that need.

**Expansion directions.** Document explicit referrals to official alerting authorities on hazards surfaces; standardize the "planning context, not alerting" label.

**Open questions.** Which hazards layers carry the highest misuse risk and need the most prominent labeling?

**Suggested future work.** Author a hazards labeling policy document referenced from public hazards surfaces.

##### KFM-IDX-PLN-003 — Domain lanes are proof-bearing slices

**Status.** CONFIRMED. **Category/Subcategory.** PLN / Domain lanes. **Lineage.** Pass 19 P19-PLN-003; rooted in Pass 18 domain reports (habitat, fauna, flora, archaeology, hydrology, soil, atmosphere).

**Normalized statement.** Domain expansions should ship as proof-bearing thin slices that demonstrate descriptor, evidence, policy, validation, and release closure for a small AOI before broadening — not as broad horizontal coverage.

**Detailed explanation.** The KFM domain reports [Pass 18] — habitat, fauna, flora, archaeology, hydrology, soil, atmosphere — consistently recommend thin-slice delivery: one small AOI, one descriptor, one evidence bundle, one policy decision, one validation pass, one release. The Pass 19 normalization elevates this to a category invariant: domain expansion is proof-bearing, not coverage-bearing. A new domain lane is judged by whether it demonstrates closure, not by how many counties or layers it includes.

The operational consequence is that PR templates, ADR templates, and review templates all assume a small AOI and a closed proof set. Broad coverage is earned by repeated thin slices, not asserted in the first PR.

**Why it matters.** Thin-slice proof is what keeps the trust spine intact during expansion. Broad horizontal launches typically skip closure in one or more categories — and the gap surfaces as user-visible incoherence once the surface is live.

**Related ideas.** `KFM-IDX-REL-001` (catalog closure); `KFM-IDX-VAL-005` (no-network dry runs); `KFM-IDX-EVD-001` (evidence closure); `KFM-IDX-DOC-001` (governance ahead of polish).

**Dependencies.** Thin-slice template; AOI selection; closure checklist; PR template.

**Tensions / limitations.** Thin slices are slower than broad launches; the corpus's argument is that thin slices repay the cost in reversibility, clarity, and trust.

**Expansion directions.** Document a thin-slice PR template; pilot a habitat or archaeology thin slice on a single Kansas county.

**Open questions.** Which Kansas AOI offers the right combination of evidence richness, sensitivity, and review feasibility for the next domain thin slice?

**Suggested future work.** Author a domain thin-slice PR template and one Kansas-county pilot proposal as PROPOSED.

##### KFM-IDX-PLN-004 — Pass 19→20 expansion focuses on source-change governance and artifact integrity

**Status.** CONFIRMED. **Category/Subcategory.** PLN / Source-change governance. **Lineage.** Pass 19 P19-PLN-004; rooted in Pass 19 5-8, 5-10, and 5-15 packets and Pass 19 cross-cutting synthesis.

**Normalized statement.** The expansion frontier between Pass 19 and Pass 20 is dominated by source-change governance (environmental probes, CDL/PLANTS drift, package and ontology monitors) and artifact integrity (PMTiles attestation, root hashes, viewer verification, hash policy by object family).

**Detailed explanation.** The three Pass 19 delta packets [Pass 19] — 5-8 environmental probes, 5-10 PMTiles attestation, and 5-15 CDL/PLANTS source drift — converge on two themes: how does KFM know its sources are still trustworthy, and how does KFM prove its public artifacts have not been tampered with? These themes are continuous with Pass 18 doctrine but introduce new operational artifacts: signed CI probe receipts, attestation sidecars, source-drift candidate records, classmap version registries, watcher outbox lifecycles, and hash policies by object family.

The Pass 20 expansion agenda (Section 10) is largely a translation of these themes into thin-slice work items: source-watch registry, CDL drift watcher, PMTiles attestation slice, hash policy ADR, evidence drawer payloads for drift and integrity, STAC profiles for new artifact families, domain source-role matrices, and threshold registry. The category invariant is that this expansion is governance-shaped — it strengthens existing trust spine rather than introducing parallel publication paths.

**Why it matters.** Source-change governance and artifact integrity are the two areas where Pass 18 doctrine was strongest in principle but thinnest in operational artifacts. Closing this gap is what Pass 19→20 is for.

**Related ideas.** `KFM-IDX-SRC-005` (environmental CI probes); `KFM-IDX-SRC-006` (CDL/PLANTS drift); `KFM-IDX-EVD-003` (PMTiles attestation); `KFM-IDX-EVD-004` (hash policy); `KFM-IDX-REL-001` (catalog closure).

**Dependencies.** Expansion backlog (EXP-001..015); thin-slice PR templates; ADR cadence; Directory Rules.

**Tensions / limitations.** Source-change and integrity work is operationally heavy and competes for attention with new domain coverage; the corpus's guidance is to prioritize it on the grounds that domain coverage without integrity is fragile.

**Expansion directions.** Sequence EXP-001 through EXP-015 by dependency and feasibility; land one source-watch and one integrity slice as the proof of the Pass 20 frontier.

**Open questions.** Which combination of EXP items constitutes the minimum Pass 20 declaration, and which can wait for Pass 21?

**Suggested future work.** Author a Pass 20 milestone plan that names the minimum thin-slice set and the proof-of-closure for each.

## 7. Cross-Cutting Themes

This section synthesizes the ten themes that cut across categories. Each theme appears in multiple category chapters and structures the larger argument of the atlas. The list merges Pass 18's eight cross-cutting themes with Pass 19's ten, deduplicated and renormalized into a coherent ten-theme set for Pass 20.

### 7.1 Evidence is a stateful chain, not a citation footnote

The corpus's strongest single theme is that evidence in KFM is not a citation to a source but a stateful chain that links source descriptor, evidence bundle, evidence reference, policy decision, validation result, release manifest, and rollback target. Pass 18 develops this across the Greenfield Building Plan, the Pipeline Living Manual, and the Whole-UI Governed AI Expansion Report; Pass 19 reinforces it through the CDL/PLANTS source-drift candidate envelope, the PMTiles attestation sidecar, and the steward review summary. The implication is operational: a citation that does not resolve through the chain is not evidence in KFM doctrine, and a surface that displays content without the chain is not yet governed.

This theme links DOC, SRC, EVD, POL, VAL, REL, API, and UIX. It explains why catalog closure (`KFM-IDX-REL-001`) is a closure property rather than a process outcome, why outcome envelopes (`KFM-IDX-API-002`) are finite and include deny, and why the Evidence Drawer (`KFM-IDX-UIX-001`) is mandatory on every governed surface.

### 7.2 Representation is never neutral

Pass 18's REP chapter and the recurring cartography arguments across all atlases insist that representation choices — class ontology, projection, generalization, color scheme, legend simplification, time-window aggregation — are policy choices that shape what users see. Pass 19 normalizes this in `KFM-IDX-REP-001` through `KFM-IDX-REP-005` and reinforces it through the CDL `classmap_version` discipline and the archaeology 3D measured-versus-interpretive distinction.

The implication is that style and policy share an interface: a style decision that omits a class, generalizes a geometry, or aggregates a time window has policy weight. Maps, drawers, and Focus Mode surfaces should make these choices legible, and reviewers should be able to trace why a representation looks the way it does.

This theme links REP, MAP, UIX, and POL.

### 7.3 Watchers are monitors, not publishers

Every category in which watchers appear — SRC environmental probes, SRC source-drift detectors, VAL CI probes, REL watcher lifecycle, API source intake envelopes — converges on a single invariant: watchers observe and record, they do not promote. The Pass 19 5-15 packet [Pass 19] states this plainly for CDL/PLANTS Watch (candidates enter `WORK_CANDIDATE`, never `PUBLISHED`), and the corpus extends the invariant to all watcher families.

The structural justification is that watchers are cheap to run continuously. That cheapness is a virtue only as long as it does not become an authority. The watcher-as-non-publisher rule is what keeps the trust spine from degrading to whichever detector is cheapest.

This theme links SRC, VAL, REL, API, and DOC.

### 7.4 Artifact integrity is part of publication truth

Pass 19's 5-10 packet [Pass 19] introduces PMTiles attestation, root hashes, viewer-side verification, and digest-pinned references — all of which extend KFM's "evidence chain" doctrine to the bytes that arrive at users' browsers. Pass 18 doctrine on hashes, manifests, and rollback targets is convergent but less concrete; Pass 19 makes the doctrine operational. The implication is that publication truth includes not only what was promoted but also what was actually served, and that artifact integrity is a category invariant rather than an implementation detail.

This theme links EVD, VAL, REL, MAP, and POL. It is the central theme of the Pass 20 expansion agenda (Section 10) along with source-change governance.

### 7.5 Temporal support cuts across every domain

Time is a structural concern in KFM, not a domain. The corpus is consistent that every domain — hydrology, atmosphere, soil, archaeology, fauna, flora, hazards, infrastructure — needs temporal support: time intervals, vintages, snapshot ranges, validity windows. Pass 19 normalizes this in `KFM-IDX-MOD-005` and reinforces it through CDL yearly bundles, PLANTS taxonomy versions, MAIAC daily cadence, SMAP cadence, and PMTiles versioning.

The implication is that temporal scoping is a contract surface, not a UI affordance. Tiles, layers, scenes, evidence bundles, policy decisions, and AI envelopes all reference time intervals consistently, and downstream surfaces are expected to honor them.

This theme links MOD, MAP, UIX, REL, and PLN.

### 7.6 Sensitive precision is a design risk

The fauna sensitivity posture is the strongest articulation: nests, dens, roosts, hibernacula, and spawning sites are deny-by-default for exact location, regardless of source. The corpus extends the same posture to rare-species locations, archaeological sites, sacred sites, living-person data, and certain infrastructure datasets. Pass 19 normalizes this in `KFM-IDX-POL-003` and reinforces it through Pass 19's discussion of source-role labeling and STAC profile design.

The implication is that precision is a policy decision: the system can know exact locations internally and still expose generalized geometry publicly, and the transform is part of the audit trail.

This theme links POL, FIE, REP, MAP, and UIX.

### 7.7 AI is interpretive and replaceable

The Whole-UI Governed AI Expansion Report [Pass 18] makes governed AI the explicit alternative to sovereign generation. Pass 19 normalizes this in `KFM-IDX-DOC-005`, `KFM-IDX-API-002`, and `KFM-IDX-UIX-002`. The implication is that AI in KFM is interpretive (not authoritative), evidence-bounded (not extrapolative), and replaceable (the trust spine survives a change of model, vendor, or prompt regime).

The corollary is that AI outputs travel inside governed envelopes, surface through the Evidence Drawer, and inherit the release state of their evidence. There is no "AI answer" outside this discipline.

This theme links DOC, API, UIX, EVD, and POL.

### 7.8 No-network fixtures are governance accelerators

Pass 19 repeatedly recommends that pipelines, watchers, and validators ship with fixture-first proof lanes that exercise schemas, validators, and policy without live fetch. `KFM-IDX-VAL-005` makes this explicit. The implication is that "the network is down" is a first-class test environment, not a degraded one — and that fixtures encode the contract more precisely than live data does.

The structural justification is that no-network fixtures isolate KFM's governance from upstream source instability, give CI deterministic guarantees, and accelerate ADR and PR review cycles.

This theme links VAL, SRC, EVD, REL, and API.

### 7.9 Planning support needs visible assumptions

Pass 18's planning chapters and Pass 19's `KFM-IDX-PLN-001` insist that planning support is a different surface from prediction or regulation, and that the structural defense against misuse is to make assumptions visible on the surface itself. Scenario manifests, equity dimension labels, time-horizon labels, and participation-set references all belong to the user-visible surface, not to buried documentation.

This theme links PLN, REP, MOD, UIX, and DOC.

### 7.10 Directory and schema-home discipline prevents silent fragmentation

The Directory Rules and the recurring schema-home discussions across DOC and REL chapters insist that responsibility roots are authority boundaries, not convenience buckets. A schema, contract, policy, source descriptor, registry, release record, or proof object lives in one canonical home, and parallel homes require ADR justification.

The implication is that PR placement is a governance decision. The corpus repeatedly flags proposed Pass 19 placements (such as `tools/ingest/cdl_watch/`) as NEEDS VERIFICATION pending Directory Rules review precisely because silent fragmentation is one of the most common ways for trust spines to degrade.

This theme links DOC, REL, SRC, EVD, POL, VAL, and API.

[⬆ back to top](#contents)


## 8. Overlaps, Contradictions, and Gaps

This section identifies areas where the corpus overlaps redundantly, contradicts itself, or leaves gaps relative to the doctrine it asserts. The goal is to make these visible so that Pass 20 PRs, ADRs, and documentation work address them deliberately rather than re-inheriting them.

### 8.1 Overlaps

The corpus's strongest overlaps occur between the Greenfield Building Plan, the Pipeline Living Manual, the Master MapLibre Atlas, and the Whole-UI Governed AI Expansion Report [Pass 18]. Catalog closure is restated in each, with slightly different vocabulary; promotion as a state transition appears in three of the four; the Evidence Drawer is described in two of the four; and trust states are described in three of the four. Pass 19 substantially deduplicates these by normalizing the vocabulary, but residual overlap remains in the underlying source material.

The Pass 19 deltas themselves overlap on three points: source descriptors (5-15 names them explicitly, 5-8 implies them through environmental probe records, 5-10 references them through PMTiles release manifests); evidence bundles (referenced in all three deltas); and threshold policy (5-8 thresholds for environmental probes, 5-15 thresholds for CDL drift). The Pass 20 ADR for hash policy by object family (EXP-004) and the threshold policy registry (EXP-008) are both expansion-agenda responses to these overlaps.

The 14-category map itself contains adjacent categories with deliberate overlap: VAL and ANA overlap on materiality reasoning; SRC and FIE overlap on remote-sensing inputs; MAP and UIX overlap on trust-state surfacing; REL and POL overlap on publication denial; EVD and VAL overlap on receipts. These overlaps are doctrinal rather than redundant — each category looks at the overlap from a different responsibility root.

### 8.2 Contradictions

The corpus contains few explicit contradictions, but several productive tensions deserve flagging.

**Speed versus closure.** The Pass 19 deltas implicitly assume rapid iteration on source-drift and integrity work, while the Directory Rules and the closure doctrine require careful PR placement, ADR justification, and review cycles. The Pass 19 5-15 packet [Pass 19] flags this tension explicitly by proposing watcher outbox paths under `tools/ingest/cdl_watch/` while marking the placement NEEDS VERIFICATION pending Directory Rules review.

**Breadth versus depth.** Pass 18 covers fourteen categories and many domains in considerable breadth; Pass 19 normalizes to 64 entries and recommends thin-slice depth. The breadth and depth orientations are complementary but produce friction at PR review time: a reviewer asked to assess a thin slice against a broad doctrine must do both readings simultaneously.

**Visual richness versus evidentiary humility.** The Archaeological 3D GIS reference and the Master MapLibre Atlas both develop rich visual surfaces — 3D scenes, complex symbology, time-aware overlays — while the EVD and POL doctrines require evidentiary humility on those exact surfaces. The tension is structural rather than resolvable; the corpus's response is to make humility visible in the same surface that produces the visual richness.

**Watcher autonomy versus steward authority.** Watchers are designed to run continuously and emit candidates without human input; stewards are designed to review candidates before promotion. The tension is between scale and authority. The corpus resolves it by giving watchers no authority and stewards no scalability requirement — but the resolution depends on operational discipline that may erode under pressure.

### 8.3 Gaps

Several specific gaps stand out and motivate the expansion agenda in Section 10.

**Hash policy by object family.** The corpus repeatedly references hashes (root hashes for PMTiles, geometry hashes for CDL, fingerprints for source artifacts) without naming a canonical hash policy. EXP-004 in Section 10 addresses this directly.

**STAC profiles for KFM-specific object families.** STAC is recommended as the catalog standard, but the corpus does not yet fix KFM STAC profiles for raster, vector, field-capture, 3D-scene, and source-drift artifacts. EXP-006 addresses this.

**Threshold policy registry.** Materiality thresholds appear throughout VAL and ANA chapters without a canonical registry. EXP-008 addresses this.

**Domain source-role matrices.** Each domain (atmosphere, hazards, ecology, archaeology) implies a source-role matrix (which sources are observations, which are models, which are aggregators, which are context), but the matrices are not yet explicit. EXP-007 addresses this.

**Renderer-binding contract.** `KFM-IDX-MAP-001` insists that MapLibre is a renderer rather than a source of truth, but the precise binding contract — which data sources are allowed in production styles, which expressions are acceptable, what counts as compliant — is not yet documented. The MapLibre layer registry validator (EXP-015) is the proposed response.

**Drawer payload schemas per surface.** `KFM-IDX-UIX-001` makes the Evidence Drawer mandatory, but the per-surface payload schemas (map layer, popover, AI answer, story node) are not yet authored. EXP-005 partially addresses this.

**Live repo conformance.** The most important gap is empirical: the corpus develops doctrine confidently, but the live repo has not been conformance-scanned against that doctrine in this session. EXP-009 addresses this.

[⬆ back to top](#contents)

## 9. Weakly Supported Claims

This section catalogs claims that the corpus advances without sufficient grounding in evidence or external sources. Each is marked with a status label and a brief explanation of why the claim is weakly supported relative to the rest of the corpus.

### 9.1 Specific PR paths

Several Pass 19 snippets propose specific PR paths — `tools/ingest/cdl_watch/`, `data/contracts/source_intake_record.schema.json`, `data/catalog/stac/ecology/cdl/`, `docs/standards/ARTIFACT_FAMILIES.md`. These are useful as orientation but should be treated as PROPOSED pending Directory Rules review and live repo inspection. The corpus does not in this session confirm that these paths align with current responsibility roots.

### 9.2 Implementation maturity

The corpus describes governed APIs, Evidence Drawers, Focus Mode, Story Nodes, watcher pipelines, attestation sidecars, and viewer-side verification with operational language. Without mounted repo access, tests, manifests, workflows, dashboards, or logs in this session, the implementation maturity of each is UNKNOWN. The atlas develops doctrine confidently, but readers should not infer that any specific surface is currently shipped, gated, or tested. EXP-009 (live repo conformance scan) is the structural response to this gap.

### 9.3 Per-environment Range behavior for PMTiles

`KFM-IDX-MAP-002` recommends per-environment PMTiles Range tests but does not enumerate the environments KFM expects to support, the expected Range behavior in each, or the test methodology. The recommendation is sound but the operational specifics are NEEDS VERIFICATION.

### 9.4 Sensitivity policy fixtures

`KFM-IDX-POL-003` describes deny-by-default for exact location of nests, dens, roosts, sites, and infrastructure, but the policy fixtures that exercise this behavior are PROPOSED rather than CONFIRMED. EXP-011 in Section 10 is the direct response.

### 9.5 Composite manifest inheritance rules

`KFM-IDX-UIX-004` describes Story Node inheritance of release state and rights posture from constituent components, but the inheritance rule has not been formalized in a schema. The "worst-state wins" rule is a corpus inference rather than a CONFIRMED specification.

### 9.6 Specific threshold values

VAL and ANA chapters reference materiality thresholds (per-class change percentages, AOD/FRP thresholds, persistence rules) without fixing canonical values. The thresholds in Pass 19 examples — `pct_changed_per_class >= 2%`, `tile_area_pct_changed >= 0.5%`, `persistence_days >= 2` — are illustrative rather than normative. EXP-008 (threshold policy registry) is the response.

### 9.7 AI envelope field exhaustiveness

`KFM-IDX-API-002` lists envelope fields (`outcome`, `evidence_refs`, `policy_decision`, `rights_posture`, `confidence_or_scope`, `release_state`), but the corpus does not exhaustively name the per-surface extensions. The envelope catalog is PROPOSED.

### 9.8 Rollback propagation surface

`KFM-IDX-REL-004` and the open questions in REL chapter ask how far rollback propagates through tiles, graphs, Focus Mode caches, and Story Nodes. The corpus identifies this as a question rather than answering it. The propagation surface is UNKNOWN.

[⬆ back to top](#contents)

## 10. Expansion Agenda

This section consolidates the fifteen expansion items distributed across Pass 19. Each item is presented with its priority, category alignment, dependency profile, proof-of-closure description, and risk register. The expansion agenda is the work plan for moving Pass 20 from a synthesized atlas to a series of thin-slice PRs that deliver new operational artifacts under the KFM trust spine.

The items are grouped by theme rather than priority so that dependencies are visible. Within each group the items are ordered by suggested sequence.

### 10.1 Source-change governance group

These items implement the source-drift and source-health pillars of the Pass 19→20 expansion.

**EXP-001 — CDL/PLANTS source drift watcher thin slice (High).** A fixture-first watcher for one Kansas county and one CDL year, emitting `SourceIntakeRecord` candidates with `publication_state: WORK_CANDIDATE`, signed receipts, and a `steward_review_summary` payload. Categories: SRC, VAL, REL, API, UIX. Dependencies: source descriptor schema; classmap registry; fixture set; review summary template. Proof of closure: a deliberately-mutated fixture triggers a candidate; an unchanged fixture does not; a missing-attestation case is denied. Risk: outbox placement (`tools/ingest/cdl_watch/`) is PROPOSED and needs Directory Rules review.

**EXP-003 — Source-watch registry for environmental probes (High).** A registry that lists each environmental source (MAIAC, FIRMS, SMAP, VIIRS, additional NWS/NOAA sources), its cadence, latency expectation, materiality thresholds, and signed-receipt requirements. Categories: SRC, VAL, EVD. Dependencies: source descriptor; threshold policy; signed receipt format. Proof of closure: registry validates against probe receipts and emits a consolidated source-health dashboard. Risk: threshold values are illustrative and need POL/VAL review.

**EXP-007 — Domain source-role matrices (Medium).** For each domain (atmosphere, hydrology, ecology, archaeology, hazards, infrastructure), a matrix of sources labeled by role: observation, context, model, candidate, aggregator. Categories: SRC, FIE, REL. Dependencies: domain reports; source descriptors. Proof of closure: each domain ships a matrix referenced by its layer manifests. Risk: matrix maintenance load.

### 10.2 Artifact integrity group

These items implement the PMTiles attestation, hash policy, and viewer-side verification pillars.

**EXP-002 — PMTiles attestation and sidecar validation slice (High).** A fixture PMTiles archive with a root-hash sidecar, attestation signature, and digest-pinned reference; a validator that verifies the attestation before publication; viewer-side verification that fails closed on signature mismatch. Categories: EVD, VAL, MAP, REL. Dependencies: hash policy ADR; release manifest; viewer plugin spec. Proof of closure: a deliberately-corrupted fixture is denied; a clean fixture is granted; viewer renders denied-state on signature mismatch. Risk: viewer plugin maturity unknown.

**EXP-004 — KFM hash policy ADR by object family (High).** An ADR that fixes which hash function (BLAKE3, SHA-256, content-addressing) applies to each object family (PMTiles, COG, GeoParquet, source artifacts, source descriptors, evidence bundles), and the canonicalization rule for each (JCS, raw bytes, normalized JSON). Categories: EVD, REL, POL. Dependencies: object family enumeration; canonicalization choices. Proof of closure: ADR ships with one fixture per object family. Risk: ADR breadth vs PR cadence.

**EXP-015 — MapLibre layer registry validator (High).** A validator that ensures every public-facing layer references a governed artifact (PMTiles, COG, GeoParquet, STAC) with valid trust state, evidence ref, policy decision, and release state. Categories: MAP, REL, API. Dependencies: layer registry schema; trust-state vocabulary; renderer binding contract. Proof of closure: a renderer-binding-noncompliant layer is denied at publication. Risk: renderer-binding contract is not yet fully documented.

### 10.3 Catalog closure and STAC group

**EXP-006 — STAC profile for CDL and PMTiles artifacts (Medium).** KFM-specific STAC item profiles for CDL yearly bundles (raster assets, classmap version, projection, checksum) and for PMTiles archives (vector tiles, root hash, attestation reference). Categories: REL, EVD, FIE. Dependencies: STAC base profiles; KFM extension policy. Proof of closure: one CDL STAC item and one PMTiles STAC item ship with validators. Risk: STAC extension drift.

### 10.4 Policy and threshold group

**EXP-008 — Threshold policy registry (Medium).** A canonical registry of materiality, persistence, AOD/FRP, soil moisture, ozone, and CDL drift thresholds with the policy reasoning for each. Categories: POL, VAL, ANA. Dependencies: domain reports; steward review. Proof of closure: each threshold cited in a watcher resolves through the registry. Risk: thresholds are policy choices and may need steward review per domain.

**EXP-011 — Policy fixtures for sensitive exact-location denial (High).** Fixture cases that exercise deny-by-default for nests, dens, roosts, archaeology sites, and infrastructure at exact precision, plus generalization receipts for redacted exposure. Categories: POL, FIE, MAP. Dependencies: sensitivity registry; generalization policy. Proof of closure: a high-precision request is denied; a generalized request is granted with a transform receipt. Risk: sensitivity registry coverage.

### 10.5 UI surface and drawer group

**EXP-005 — Evidence Drawer payloads for source drift and artifact integrity (Medium).** Drawer payload schemas for source-drift candidates and artifact-integrity verification, with fixtures for granted, narrowed, denied, and candidate states. Categories: UIX, EVD, API. Dependencies: drawer payload schema. Proof of closure: each state renders correctly in fixtures. Risk: drawer UI implementation maturity unknown.

### 10.6 Conformance and dry-run group

**EXP-009 — Live repo conformance scan (High).** A scan of the current KFM repository against the doctrines articulated in this atlas, producing a CONFIRMED / PROPOSED / NEEDS VERIFICATION table per category. Categories: DOC, VAL, REL, POL. Dependencies: mounted repo access; checklist per category. Proof of closure: a conformance table is published and reviewed. Risk: this item is gated by repo access in subsequent sessions.

**EXP-010 — Publication-deny dry run (Medium).** A dry-run pipeline that exercises publication denial for each gate (evidence missing, policy denied, integrity mismatch, rights unclear, review absent) and records the denial reasons. Categories: VAL, REL, POL. Dependencies: validator suite; deny case catalog. Proof of closure: each deny case produces a useful `ValidationReport` and `denied` outcome envelope. Risk: gate coverage.

**EXP-012 — Resource ontology and API lifecycle map (Medium).** A diagram and table that maps every KFM resource (source, descriptor, evidence bundle, release manifest, artifact, layer, drawer payload, AI envelope) to its lifecycle state and its governing API. Categories: DOC, API. Dependencies: resource enumeration. Proof of closure: the map ships as a reference document. Risk: completeness vs cadence.

### 10.7 Temporal and planning group

**EXP-013 — Temporal-support acceptance criteria (Medium).** A criteria document that specifies time-interval requirements for tiles, layers, evidence bundles, policy decisions, and AI envelopes; a validator that enforces them. Categories: MOD, MAP, UIX. Dependencies: temporal vocabulary; validator. Proof of closure: a deliberately-undated layer is denied. Risk: vocabulary drift.

**EXP-014 — Planning scenario manifest (Low).** A scenario manifest schema and one Kansas-relevant pilot scenario (hazards, infrastructure, ecology, or hydrology) with explicit assumptions, time horizon, equity dimensions, and participation references. Categories: PLN, REP, UIX. Dependencies: scenario schema; AOI selection. Proof of closure: scenario ships with a public-safe summary surface and drawer payload. Risk: scenario maintenance over time.

### 10.8 Priority summary

The High-priority items are EXP-001, EXP-002, EXP-003, EXP-004, EXP-009, EXP-011, and EXP-015 — seven items distributed across source-change governance, artifact integrity, conformance, and policy. The Medium-priority items are EXP-005, EXP-006, EXP-007, EXP-008, EXP-010, EXP-012, and EXP-013 — seven items distributed across catalog, policy, UI, conformance, and temporal support. EXP-014 is the only Low-priority item.

A minimal Pass 20 milestone could be defined as: EXP-001 (source drift watcher), EXP-002 (PMTiles attestation), EXP-004 (hash policy ADR), EXP-009 (live repo conformance), and one of {EXP-011, EXP-015}. This combination demonstrates closure for source change, artifact integrity, hash discipline, conformance, and either policy fixtures or renderer-binding validation.

[⬆ back to top](#contents)

## 11. Open Questions

This section consolidates the open questions identified across the atlas. Each question is grouped by category and is intended to seed ADR drafts, PR conversations, or steward review sessions. Questions marked with `(B)` are blocking for at least one expansion item; others are clarifying or scoping.

### 11.1 Governance and directory

- Where should watcher outbox state (`SourceIntakeRecord`, signed probe receipts) live under current Directory Rules conventions? `(B)` for EXP-001 and EXP-003.
- Should `docs/runbooks/fauna/` flat-or-nested convention be normalized across all runbooks, or kept per-domain?
- Should the naming discrepancy between `PROV.md` and `PROVENANCE.md` be resolved by ADR or by silent alignment? `(B)` for documentation conformance.

### 11.2 Hash and artifact integrity

- Which hash function applies to which object family — BLAKE3 for content addressing, SHA-256 for compatibility, both for different purposes? `(B)` for EXP-004.
- Which canonicalization (JCS, raw, normalized JSON) applies to each schema? `(B)` for EXP-004.
- Which Kansas-relevant hosting environments offer reliable PMTiles Range support, and which require origin reconfiguration?
- What is the partitioning unit (county, HUC, tile pyramid) for Kansas-scale public PMTiles?

### 11.3 Evidence and policy

- What is the minimum mandatory drawer payload, and which fields are surface-specific? `(B)` for EXP-005.
- Which sensitivity classes need separate generalization policies (point displacement, geometry buffering, time-window aggregation)? `(B)` for EXP-011.
- Which next-action vocabulary spans all review surfaces?
- How far should rollback propagate through tiles, graphs, Focus Mode caches, and Story Nodes?

### 11.4 Sources and validation

- Which environmental sources need the highest-cadence probes, and which can be sampled? `(B)` for EXP-003.
- Which materiality thresholds are policy choices versus operational tunings? `(B)` for EXP-008.
- Which county set, CDL year, and class ontology should seed the first CDL drift watcher fixture? `(B)` for EXP-001.
- Which PLANTS taxa intersect with state-listed conservation species and require additional handling?

### 11.5 Renderer and surface

- Which expressions and runtime patterns are acceptable in production MapLibre styles versus admin/dev styles? `(B)` for EXP-015.
- How are mixed trust states displayed in a multi-layer scene — by worst-state, per-layer indicator, or composite indicator?
- What is the denied-state UX (banner, modal, layer absence) for a verification failure on a primary public layer?

### 11.6 Planning and domain lanes

- Which Kansas planning domain best supports a thin-slice scenario manifest pilot? `(B)` for EXP-014.
- Which Kansas AOI offers the right combination of evidence richness, sensitivity, and review feasibility for the next domain thin slice?
- Which hazards layers carry the highest misuse risk and need the most prominent labeling?

### 11.7 Conformance

- Does the current KFM repository conform to the doctrines articulated in this atlas, and where does it diverge? `(B)` for EXP-009 and gated on live repo access.

[⬆ back to top](#contents)


## Appendix A — Master Idea Index Table

The table below enumerates every normalized idea entry assigned a `KFM-IDX-CAT-NNN` identifier in this atlas. Status reflects truth-labeling as of this synthesis. Lineage records whether the idea is sourced from Pass 18, Pass 19, or both. Page-anchor references are intentionally omitted in favor of category section numbers; readers should consult Section 6 for full entries.

| ID | Category | Status | Lineage | Title |
|---|---|---|---|---|
| KFM-IDX-DOC-001 | DOC | CONFIRMED | Pass 18; Pass 19 | Cite-or-abstain is the controlling truth posture |
| KFM-IDX-DOC-002 | DOC | CONFIRMED | Pass 18; Pass 19 | Directory placement is a governance boundary |
| KFM-IDX-DOC-003 | DOC | CONFIRMED | Pass 18; Pass 19 | Truth labels are operational controls |
| KFM-IDX-DOC-004 | DOC | CONFIRMED | Pass 18; Pass 19 | Implementation maturity remains UNKNOWN without current repo evidence |
| KFM-IDX-DOC-005 | DOC | PROPOSED | Pass 18 | Shared governance kernel across bounded domain lanes |
| KFM-IDX-DOC-006 | DOC | PROPOSED | Pass 18 | Responsibility layers as KFM large-scale structure |
| KFM-IDX-REP-001 | REP | CONFIRMED | Pass 18; Pass 19 | Representation is a governed claim surface |
| KFM-IDX-REP-002 | REP | CONFIRMED | Pass 18; Pass 19 | Scale, CRS, resolution, and geometry version are evidence properties |
| KFM-IDX-REP-003 | REP | CONFIRMED | Pass 18; Pass 19 | Raster, vector, network, field, and graph forms must not be collapsed |
| KFM-IDX-REP-004 | REP | CONFIRMED | Pass 18; Pass 19 | 3D and 2.5D outputs require evidentiary humility |
| KFM-IDX-SRC-001 | SRC | CONFIRMED | Pass 18; Pass 19 | Every admitted source needs a SourceDescriptor |
| KFM-IDX-SRC-002 | SRC | CONFIRMED | Pass 18; Pass 19 | HEAD, ETag, Last-Modified, and content length are intake evidence |
| KFM-IDX-SRC-003 | SRC | CONFIRMED | Pass 18; Pass 19 | Source roles prevent authority collapse |
| KFM-IDX-SRC-004 | SRC | CONFIRMED | Pass 18; Pass 19 | Connectors and scrapers must fail safe at the intake edge |
| KFM-IDX-SRC-005 | SRC | PROPOSED | Pass 19 | Environmental CI probes are source-health monitors, not scientific conclusions |
| KFM-IDX-SRC-006 | SRC | CONFIRMED | Pass 19 | CDL and PLANTS watchers should emit source-drift candidates only |
| KFM-IDX-MOD-001 | MOD | CONFIRMED | Pass 18; Pass 19 | Temporal structure is first-class evidence |
| KFM-IDX-MOD-002 | MOD | CONFIRMED | Pass 18; Pass 19 | Bounded contexts protect domain meaning |
| KFM-IDX-MOD-003 | MOD | CONFIRMED | Pass 18; Pass 19 | Geography versions are part of identity |
| KFM-IDX-MOD-004 | MOD | CONFIRMED | Pass 18; Pass 19 | Class ontologies and semantic versions protect historical comparability |
| KFM-IDX-MOD-005 | MOD | CONFIRMED | Pass 18; Pass 19 | Assertions, observations, models, and public artifacts are different object families |
| KFM-IDX-EVD-001 | EVD | CONFIRMED | Pass 18; Pass 19 | EvidenceRef must resolve to EvidenceBundle |
| KFM-IDX-EVD-002 | EVD | CONFIRMED | Pass 18; Pass 19 | Receipts preserve process memory without becoming truth |
| KFM-IDX-EVD-003 | EVD | CONFIRMED | Pass 19 | PMTiles attestation sidecars make map artifacts verifiable |
| KFM-IDX-EVD-004 | EVD | PROPOSED | Pass 19 | Bao and byte-range proofs enable partial verification |
| KFM-IDX-EVD-005 | EVD | CONFIRMED | Pass 18; Pass 19 | Canonical hashes turn descriptors into stable identity |
| KFM-IDX-POL-001 | POL | CONFIRMED | Pass 18; Pass 19 | Public-safe by default is non-negotiable |
| KFM-IDX-POL-002 | POL | CONFIRMED | Pass 18; Pass 19 | Rights and source terms are evidence requirements |
| KFM-IDX-POL-003 | POL | CONFIRMED | Pass 18; Pass 19 | Exact-location and living-person data require special protection |
| KFM-IDX-POL-004 | POL | CONFIRMED | Pass 18; Pass 19 | Thresholds are policy controls, not universal scientific absolutes |
| KFM-IDX-VAL-001 | VAL | CONFIRMED | Pass 19 | Material-change gates reduce noisy reprocessing |
| KFM-IDX-VAL-002 | VAL | CONFIRMED | Pass 19 | Environmental source probes need signed receipts |
| KFM-IDX-VAL-003 | VAL | CONFIRMED | Pass 18; Pass 19 | Negative fixtures are as important as valid fixtures |
| KFM-IDX-VAL-004 | VAL | CONFIRMED | Pass 19 | Publication gates must deny missing proofs |
| KFM-IDX-VAL-005 | VAL | PROPOSED | Pass 19 | No-network dry runs are the safest first implementation proof |
| KFM-IDX-ANA-001 | ANA | CONFIRMED | Pass 18; Pass 19 | Analysis remains an interpretive derivative |
| KFM-IDX-ANA-002 | ANA | CONFIRMED | Pass 19 | AOD and FRP can gate tile health when policy-bound |
| KFM-IDX-ANA-003 | ANA | CONFIRMED | Pass 19 | CDL histogram drift is a controlled analytical trigger |
| KFM-IDX-ANA-004 | ANA | CONFIRMED | Pass 19 | PLANTS taxa drift is analytically useful but sensitivity-prone |
| KFM-IDX-ANA-005 | ANA | CONFIRMED | Pass 18; Pass 19 | Urban and regional planning analysis needs participation and scenario context |
| KFM-IDX-FIE-001 | FIE | CONFIRMED | Pass 18; Pass 19 | Field capture should produce evidence, not orphan observations |
| KFM-IDX-FIE-002 | FIE | CONFIRMED | Pass 18; Pass 19 | Remote sensing needs quality, latency, and source-role labeling |
| KFM-IDX-FIE-003 | FIE | CONFIRMED | Pass 18; Pass 19 | Archaeological 3D outputs separate documentation from interpretation |
| KFM-IDX-FIE-004 | FIE | PROPOSED | Pass 19 | Remote and field workflows should normalize into catalogs before public maps |
| KFM-IDX-REL-001 | REL | CONFIRMED | Pass 18; Pass 19 | Catalog closure links STAC, DCAT, PROV, release, and evidence |
| KFM-IDX-REL-002 | REL | CONFIRMED | Pass 18; Pass 19 | Promotion is a governed state transition |
| KFM-IDX-REL-003 | REL | CONFIRMED | Pass 19 | Avoid in-place overwrites of PMTiles and large artifacts |
| KFM-IDX-REL-004 | REL | CONFIRMED | Pass 18; Pass 19 | Rollback targets need stable manifests and receipts |
| KFM-IDX-REL-005 | REL | CONFIRMED | Pass 19 | Watcher output enters WORK_CANDIDATE, not PUBLISHED |
| KFM-IDX-API-001 | API | CONFIRMED | Pass 18; Pass 19 | Governed APIs are trust membranes |
| KFM-IDX-API-002 | API | CONFIRMED | Pass 19 | Finite outcome envelopes replace free-form runtime status |
| KFM-IDX-API-003 | API | PROPOSED | Pass 18; Pass 19 | Design-first API contracts map resources to lifecycle |
| KFM-IDX-API-004 | API | PROPOSED | Pass 19 | SourceIntakeRecord is the proper candidate envelope for drift watchers |
| KFM-IDX-MAP-001 | MAP | CONFIRMED | Pass 18; Pass 19 | MapLibre is a downstream renderer, not a truth store |
| KFM-IDX-MAP-002 | MAP | CONFIRMED | Pass 19 | PMTiles Range and cache behavior require explicit operations tests |
| KFM-IDX-MAP-003 | MAP | CONFIRMED | Pass 18; Pass 19 | COG, GeoParquet, PMTiles, STAC, DCAT, and PROV form an artifact matrix |
| KFM-IDX-MAP-004 | MAP | PROPOSED | Pass 19 | Viewer verification should fail closed on sidecar or signature mismatch |
| KFM-IDX-MAP-005 | MAP | CONFIRMED | Pass 19 | Map states should expose stale, degraded, quarantine, and review posture |
| KFM-IDX-UIX-001 | UIX | CONFIRMED | Pass 18; Pass 19 | Evidence Drawer is a mandatory trust object |
| KFM-IDX-UIX-002 | UIX | CONFIRMED | Pass 18; Pass 19 | Focus Mode must stay evidence-bounded |
| KFM-IDX-UIX-003 | UIX | PROPOSED | Pass 19 | Review surfaces need steward-readable summaries |
| KFM-IDX-UIX-004 | UIX | PROPOSED | Pass 18; Pass 19 | Story Nodes and narrative surfaces must inherit release and evidence state |
| KFM-IDX-PLN-001 | PLN | CONFIRMED | Pass 18; Pass 19 | Planning support requires participation, equity, and scenario context |
| KFM-IDX-PLN-002 | PLN | CONFIRMED | Pass 19 | Hazards support is not emergency alerting |
| KFM-IDX-PLN-003 | PLN | CONFIRMED | Pass 18; Pass 19 | Domain lanes should be built as proof-bearing slices, not broad map layers |
| KFM-IDX-PLN-004 | PLN | PROPOSED | Pass 19 | Source-change governance plus artifact integrity is the strongest Pass 19→20 expansion |

The table contains 66 entries across 14 categories. Counts per category are: DOC 6, REP 4, SRC 6, MOD 5, EVD 5, POL 4, VAL 5, ANA 5, FIE 4, REL 5, API 4, MAP 5, UIX 4, PLN 4. Pass 18-only entries appear in DOC (DOC-005, DOC-006); Pass 19-only entries cluster in VAL, ANA, FIE, REL, API, MAP, and UIX where Pass 19's normalization introduced new operational specificity beyond Pass 18.

[⬆ back to top](#contents)

## Appendix B — Source Contribution Matrix

This matrix maps each KFM-IDX entry to its primary source contributions across the Pass 18 and Pass 19 corpus. The columns indicate where the idea draws its strongest support: P18-DR = Pass 18 domain reports (habitat, fauna, archaeology, hydrology, atmosphere, soil), P18-AT = Pass 18 architectural atlases (Greenfield Building Plan, Pipeline Living Manual, Master MapLibre Atlas, Whole-UI Governed AI Expansion Report), P18-PE = Pass 18 process/encyclopedia entries (KFM doctrine layer, Directory Rules, ADR conventions), P19-N = Pass 19 normalized entries (P19-CAT-NNN), P19-Δ = Pass 19 delta packets (5-8 environmental probes, 5-10 PMTiles attestation, 5-15 CDL/PLANTS drift).

A ● marks a strong contribution; a ○ marks a supporting reference.

### B.1 DOC / REP / SRC / MOD

| ID | P18-DR | P18-AT | P18-PE | P19-N | P19-Δ |
|---|---|---|---|---|---|
| KFM-IDX-DOC-001 | ○ | ● | ● | ● | — |
| KFM-IDX-DOC-002 | — | ● | ● | ● | ○ |
| KFM-IDX-DOC-003 | — | ● | ● | ● | — |
| KFM-IDX-DOC-004 | — | ○ | ● | ● | — |
| KFM-IDX-DOC-005 | ● | ● | ● | — | — |
| KFM-IDX-DOC-006 | ○ | ● | ● | — | — |
| KFM-IDX-REP-001 | ● | ● | ○ | ● | — |
| KFM-IDX-REP-002 | ● | ● | ○ | ● | ○ |
| KFM-IDX-REP-003 | ● | ● | — | ● | — |
| KFM-IDX-REP-004 | ● | ● | — | ● | — |
| KFM-IDX-SRC-001 | ○ | ● | ● | ● | ○ |
| KFM-IDX-SRC-002 | — | ● | ● | ● | ● |
| KFM-IDX-SRC-003 | ● | ● | ○ | ● | ● |
| KFM-IDX-SRC-004 | ○ | ● | ● | ● | ○ |
| KFM-IDX-SRC-005 | — | ○ | — | ● | ● |
| KFM-IDX-SRC-006 | — | ○ | ○ | ● | ● |
| KFM-IDX-MOD-001 | ● | ● | ○ | ● | ○ |
| KFM-IDX-MOD-002 | ● | ● | ● | ● | — |
| KFM-IDX-MOD-003 | ○ | ● | ● | ● | ○ |
| KFM-IDX-MOD-004 | ● | ● | ○ | ● | ● |
| KFM-IDX-MOD-005 | ● | ● | ○ | ● | — |

### B.2 EVD / POL / VAL / ANA

| ID | P18-DR | P18-AT | P18-PE | P19-N | P19-Δ |
|---|---|---|---|---|---|
| KFM-IDX-EVD-001 | ○ | ● | ● | ● | ○ |
| KFM-IDX-EVD-002 | — | ● | ● | ● | ● |
| KFM-IDX-EVD-003 | — | ○ | — | ● | ● |
| KFM-IDX-EVD-004 | — | ○ | — | ● | ● |
| KFM-IDX-EVD-005 | ○ | ● | ● | ● | ● |
| KFM-IDX-POL-001 | ● | ● | ● | ● | — |
| KFM-IDX-POL-002 | ● | ● | ● | ● | — |
| KFM-IDX-POL-003 | ● | ● | ○ | ● | — |
| KFM-IDX-POL-004 | ● | ● | ○ | ● | ● |
| KFM-IDX-VAL-001 | — | ○ | — | ● | ● |
| KFM-IDX-VAL-002 | — | ○ | — | ● | ● |
| KFM-IDX-VAL-003 | — | ● | ● | ● | — |
| KFM-IDX-VAL-004 | — | ● | ○ | ● | ● |
| KFM-IDX-VAL-005 | — | ● | ○ | ● | ● |
| KFM-IDX-ANA-001 | ● | ● | ○ | ● | — |
| KFM-IDX-ANA-002 | — | ○ | — | ● | ● |
| KFM-IDX-ANA-003 | — | ○ | — | ● | ● |
| KFM-IDX-ANA-004 | — | ○ | — | ● | ● |
| KFM-IDX-ANA-005 | ● | ● | — | ● | — |

### B.3 FIE / REL / API / MAP / UIX / PLN

| ID | P18-DR | P18-AT | P18-PE | P19-N | P19-Δ |
|---|---|---|---|---|---|
| KFM-IDX-FIE-001 | ● | ○ | ○ | ● | — |
| KFM-IDX-FIE-002 | ● | ● | — | ● | ● |
| KFM-IDX-FIE-003 | ● | ● | — | ● | — |
| KFM-IDX-FIE-004 | ○ | ● | ○ | ● | ● |
| KFM-IDX-REL-001 | — | ● | ● | ● | ● |
| KFM-IDX-REL-002 | — | ● | ● | ● | ● |
| KFM-IDX-REL-003 | — | ● | — | ● | ● |
| KFM-IDX-REL-004 | — | ● | ● | ● | ● |
| KFM-IDX-REL-005 | — | ● | ● | ● | ● |
| KFM-IDX-API-001 | — | ● | ● | ● | — |
| KFM-IDX-API-002 | — | ● | ○ | ● | ○ |
| KFM-IDX-API-003 | — | ● | ● | ● | — |
| KFM-IDX-API-004 | — | ○ | — | ● | ● |
| KFM-IDX-MAP-001 | — | ● | ○ | ● | — |
| KFM-IDX-MAP-002 | — | ● | — | ● | ● |
| KFM-IDX-MAP-003 | ○ | ● | ○ | ● | ○ |
| KFM-IDX-MAP-004 | — | ○ | — | ● | ● |
| KFM-IDX-MAP-005 | — | ● | ○ | ● | ○ |
| KFM-IDX-UIX-001 | — | ● | ○ | ● | — |
| KFM-IDX-UIX-002 | — | ● | — | ● | — |
| KFM-IDX-UIX-003 | — | ● | — | ● | ● |
| KFM-IDX-UIX-004 | — | ● | — | ● | — |
| KFM-IDX-PLN-001 | ● | ● | ○ | ● | — |
| KFM-IDX-PLN-002 | ● | ○ | ○ | ● | — |
| KFM-IDX-PLN-003 | ● | ● | ○ | ● | — |
| KFM-IDX-PLN-004 | — | ○ | — | ● | ● |

### B.4 Observations on the contribution matrix

The matrix reveals several patterns. First, the Pass 18 architectural atlases (P18-AT) carry the heaviest single contribution load: they appear in nearly every row of the matrix and dominate the DOC, REP, MOD, EVD, POL, REL, API, MAP, UIX, and PLN categories. This reflects the structural role of the Greenfield Building Plan, Pipeline Living Manual, Master MapLibre Atlas, and Whole-UI Governed AI Expansion Report as the corpus's primary doctrinal sources.

Second, the Pass 19 delta packets (P19-Δ) concentrate contribution in SRC, EVD, VAL, ANA, REL, MAP, and UIX — the operational categories most affected by source-drift, attestation, and watcher governance. This is the empirical signature of the Pass 19→20 expansion's emphasis on source-change governance and artifact integrity.

Third, the Pass 18 domain reports (P18-DR) contribute strongest in REP, MOD, POL, FIE, ANA, and PLN — the categories where domain-specific evidence and policy choices matter most. DOC, API, MAP, REL, and UIX show light domain-report contribution because they are cross-domain by nature.

Fourth, the Pass 18 process/encyclopedia entries (P18-PE) contribute strongest in DOC, MOD, POL, REL, and API — the governance backbone categories where Directory Rules, ADR conventions, and the KFM doctrine layer set the rules of engagement.

The matrix is intended to be useful for ADR drafting (showing which sources to cite) and for conformance scanning (showing which sources to audit against).

[⬆ back to top](#contents)

## Appendix C — Expansion Backlog by Priority

This appendix re-presents the fifteen expansion items from Section 10 organized by priority rather than by theme. It is intended as a working backlog for Pass 20 PR planning.

### C.1 High priority (7 items)

| EXP | Title | Primary categories | Proof-of-closure marker |
|---|---|---|---|
| EXP-001 | CDL/PLANTS source drift watcher thin slice | SRC, VAL, REL, API, UIX | Mutated fixture triggers candidate; clean fixture does not; missing-attestation denied |
| EXP-002 | PMTiles attestation and sidecar validation slice | EVD, VAL, MAP, REL | Corrupted fixture denied; clean fixture granted; viewer renders denied-state |
| EXP-003 | Source-watch registry for environmental probes | SRC, VAL, EVD | Registry validates probe receipts; consolidated source-health dashboard |
| EXP-004 | KFM hash policy ADR by object family | EVD, REL, POL | ADR ships with one fixture per object family |
| EXP-009 | Live repo conformance scan | DOC, VAL, REL, POL | CONFIRMED / PROPOSED / NEEDS VERIFICATION table per category |
| EXP-011 | Policy fixtures for sensitive exact-location denial | POL, FIE, MAP | High-precision request denied; generalized request granted with transform receipt |
| EXP-015 | MapLibre layer registry validator | MAP, REL, API | Renderer-binding-noncompliant layer denied at publication |

### C.2 Medium priority (7 items)

| EXP | Title | Primary categories | Proof-of-closure marker |
|---|---|---|---|
| EXP-005 | Evidence Drawer payloads for source drift and artifact integrity | UIX, EVD, API | Each state renders correctly in fixtures |
| EXP-006 | STAC profile for CDL and PMTiles artifacts | REL, EVD, FIE | One CDL STAC item and one PMTiles STAC item ship with validators |
| EXP-007 | Domain source-role matrices | SRC, FIE, REL | Each domain ships a matrix referenced by its layer manifests |
| EXP-008 | Threshold policy registry | POL, VAL, ANA | Each threshold cited in a watcher resolves through the registry |
| EXP-010 | Publication-deny dry run | VAL, REL, POL | Each deny case produces a useful `ValidationReport` and `denied` envelope |
| EXP-012 | Resource ontology and API lifecycle map | DOC, API | Map ships as a reference document |
| EXP-013 | Temporal-support acceptance criteria | MOD, MAP, UIX | A deliberately-undated layer is denied |

### C.3 Low priority (1 item)

| EXP | Title | Primary categories | Proof-of-closure marker |
|---|---|---|---|
| EXP-014 | Planning scenario manifest | PLN, REP, UIX | Scenario ships with a public-safe summary surface and drawer payload |

### C.4 Minimum Pass 20 milestone proposal

A defensible minimum Pass 20 milestone consists of: EXP-001 (source drift watcher thin slice), EXP-002 (PMTiles attestation slice), EXP-004 (hash policy ADR), EXP-009 (live repo conformance), and one of {EXP-011, EXP-015}. This combination demonstrates closure on the five themes that the Pass 19→20 expansion explicitly identifies: source-change governance, artifact integrity, hash discipline, conformance, and either policy fixtures or renderer-binding validation.

Sequencing recommendation: EXP-009 (conformance) first to establish a baseline; EXP-004 (hash policy) before EXP-002 (since attestation depends on hash policy); EXP-001 (source drift) in parallel with EXP-002 once the policy ADR has landed; EXP-011 or EXP-015 last to add the policy or renderer enforcement layer.

### C.5 Out-of-scope expansion candidates noted but not promoted

Several expansion items are referenced in the corpus but not yet elevated to the Pass 20 backlog. They include: a comprehensive AI prompt/template registry; a multi-tenant governance model; a federated catalog with external KFM-compatible nodes; a real-time alerting bridge (explicitly out of scope per `KFM-IDX-PLN-002`); and a participatory mapping intake pipeline. Each is a legitimate future direction, but none is required for Pass 20 closure under the current expansion framing. They should be revisited at Pass 21 planning.

[⬆ back to top](#contents)

---

*End of KFM Components Pass 20 Part 2 — Idea Index, Category Atlas, and Expansion Dossier.*


