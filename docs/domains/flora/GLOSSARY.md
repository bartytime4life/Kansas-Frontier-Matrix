<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-UUID-docs-domains-flora-glossary
title: Flora Glossary
type: standard
version: v1
status: draft
owners: TODO-flora-steward
created: TODO-YYYY-MM-DD
updated: 2026-05-07
policy_label: TODO-policy-label
related: [README.md, CURRENT_STATE.md, architecture/ARCHITECTURE.md, architecture/DATA_MODEL.md, registers/SOURCE_REGISTRY.md, operations/PIPELINES_AND_LIFECYCLE.md, governance/PUBLICATION_AND_POLICY.md, architecture/UI_AND_EVIDENCE_DRAWER.md, registers/FILE_MANIFEST.md]
tags: [kfm, flora, glossary, biodiversity, evidence, governance]
notes: [doc_id, created date, owners, and policy_label require verification against the document registry, CODEOWNERS, and policy registry before merge.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Glossary

Shared vocabulary for the KFM Flora lane: plant evidence, source-role discipline, public-safe publication, EvidenceBundle-backed claims, and governed UI behavior.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Path: docs/domains/flora](https://img.shields.io/badge/path-docs%2Fdomains%2Fflora-4c1)
![Doc: glossary](https://img.shields.io/badge/doc-glossary-blue)
![Truth: evidence-bounded](https://img.shields.io/badge/truth-evidence--bounded-2b6cb0)
![Policy: fail closed](https://img.shields.io/badge/policy-fail--closed-critical)
![Owner: TODO](https://img.shields.io/badge/owner-TODO-lightgrey)

> [!IMPORTANT]
> **Status:** draft  
> **Owners:** `TODO-flora-steward` — NEEDS VERIFICATION  
> **Path:** `docs/domains/flora/GLOSSARY.md`  
> **Purpose:** keep Flora terms stable across docs, source registries, schemas, policies, fixtures, validators, API payloads, Evidence Drawer payloads, Focus responses, release manifests, and rollback records.  
> **Quick jumps:** [How to use this glossary](#how-to-use-this-glossary) · [Repo fit](#repo-fit) · [Truth and status labels](#truth-and-status-labels) · [Lifecycle terms](#lifecycle-terms) · [Source and evidence terms](#source-and-evidence-terms) · [Flora domain terms](#flora-domain-terms) · [Sensitivity and policy terms](#sensitivity-and-policy-terms) · [Catalog, release, and rollback terms](#catalog-release-and-rollback-terms) · [UI, API, and Focus terms](#ui-api-and-focus-terms) · [Term maintenance](#term-maintenance)

> [!NOTE]
> A glossary is part of the control plane. When a term changes meaning, update the affected docs, schemas/contracts, source registry, policy rules, fixtures, validators, and payload examples instead of letting vocabulary drift.

---

## How to use this glossary

Use this file when reviewing or authoring Flora lane material. A term belongs here when it affects evidence handling, source authority, taxonomy, sensitivity, publication, public-safe geometry, UI payloads, Focus outcomes, catalog closure, receipts, proofs, or rollback.

This file does **not** make implementation claims by itself. A definition can be stable doctrine while its executable schema, route, validator, fixture, or UI component remains **UNKNOWN** until verified in the repository.

### Accepted inputs

- Terms already used in Flora documentation.
- Terms used by shared KFM doctrine that Flora must obey.
- Flora-specific profile terms needed to keep taxon, occurrence, specimen, vegetation, sensitivity, and publication language consistent.
- Terms required by source descriptors, catalog records, release manifests, EvidenceBundle payloads, DecisionEnvelope payloads, and UI review states.

### Exclusions

Do not use this glossary to store:

- Raw source data.
- Secrets, access tokens, cookies, private API keys, or controlled-access notes.
- Exact sensitive plant locations.
- Full schema definitions.
- Policy code.
- Runtime route implementations.
- Unsupported claims about current repo behavior.
- Source-provider legal interpretations not backed by source review.

[Back to top](#top)

---

## Repo fit

`docs/domains/flora/GLOSSARY.md` is a human-readable standard document inside the Flora documentation lane.

| Relationship | Path | Role |
| --- | --- | --- |
| Parent entrypoint | [`README.md`](README.md) | Domain overview and navigation surface. |
| Current-state ledger | [`CURRENT_STATE.md`](CURRENT_STATE.md) | Records what has been verified in the repository and what remains unknown. |
| Architecture | [`architecture/ARCHITECTURE.md`](architecture/ARCHITECTURE.md) | Defines Flora flow, boundaries, and invariants. |
| Data model | [`architecture/DATA_MODEL.md`](architecture/DATA_MODEL.md) | Defines object families and modeling rules. |
| Source registry guide | [`registers/SOURCE_REGISTRY.md`](registers/SOURCE_REGISTRY.md) | Defines source roles, descriptor fields, and source admission posture. |
| Lifecycle guide | [`operations/PIPELINES_AND_LIFECYCLE.md`](operations/PIPELINES_AND_LIFECYCLE.md) | Defines intake-to-publication stages and gate outcomes. |
| Publication and policy | [`governance/PUBLICATION_AND_POLICY.md`](governance/PUBLICATION_AND_POLICY.md) | Defines fail-closed publication checks and public geometry classes. |
| UI and Evidence Drawer | [`architecture/UI_AND_EVIDENCE_DRAWER.md`](architecture/UI_AND_EVIDENCE_DRAWER.md) | Defines map, drawer, and Focus behavior expectations. |
| File manifest | [`registers/FILE_MANIFEST.md`](registers/FILE_MANIFEST.md) | Tracks the Flora documentation file family. |

> [!WARNING]
> Some older or adjacent docs may reference flat companion paths such as `SOURCE_REGISTRY.md` or `DATA_MODEL.md`. Current repo evidence shows nested homes such as `registers/SOURCE_REGISTRY.md` and `architecture/DATA_MODEL.md`. Preserve compatibility notes when updating references.

[Back to top](#top)

---

## Truth and status labels

These labels describe confidence, not tone. Use the narrowest truthful label.

| Term | Definition | Flora usage |
| --- | --- | --- |
| **CONFIRMED** | Verified from current repository evidence, current-session command output, attached governing doctrine, checked artifacts, or generated outputs. | Use for file presence, documented definitions, or doctrine that was actually inspected. |
| **INFERRED** | A conservative conclusion from verified evidence, but not directly stated or implemented. | Use sparingly when a term’s placement follows from surrounding docs. |
| **PROPOSED** | A recommended term, object, path, rule, or behavior not verified as current implementation. | Use for future schemas, routes, policies, fixtures, or UI payloads. |
| **UNKNOWN** | Not verified strongly enough to treat as fact. | Use for package manager, runtime routes, branch protections, dashboards, live source terms, and CI behavior unless inspected. |
| **NEEDS VERIFICATION** | Checkable but not checked strongly enough to act on. | Use for owners, policy labels, source rights, steward approvals, schema home, API paths, and tooling. |
| **CONFLICTED** | Evidence suggests multiple possible meanings, homes, or conventions. | Use when docs and repo layout disagree or when `contracts/` versus `schemas/` authority is unresolved. |
| **ABSTAIN** | Finite outcome: evidence, scope, or support is insufficient to answer. | Focus or API should return this instead of guessing. |
| **DENY** | Finite outcome: policy disallows disclosure or action. | Used for restricted exact locations, unresolved rights, or forbidden exposure. |
| **ERROR** | Finite outcome: retrieval, validation, or runtime operation failed. | Used when the system cannot complete the governed path safely. |

[Back to top](#top)

---

## Lifecycle terms

| Term | Definition | Do not confuse with |
| --- | --- | --- |
| **RAW** | Source-native capture or controlled intake before normalization. | Public-ready data. |
| **WORK** | Transformation and quality-control space for normalization, reconciliation, and candidate production. | A publication surface. |
| **QUARANTINE** | Fail-closed holding state for unresolved rights, sensitivity, source-role, integrity, or validation issues. | Deletion or rejection without record. |
| **PROCESSED** | Normalized candidate objects that passed required processing checks but are not automatically public. | Published truth. |
| **CATALOG** | Discovery and metadata closure surface, including catalog records and provenance references. | EvidenceBundle or proof pack by itself. |
| **TRIPLET** | Graph or relationship projection derived from governed evidence. | Canonical source evidence. |
| **PUBLISHED** | Public-safe or access-scoped material released through governed state transition. | A file copy or ad hoc export. |
| **Promotion gate** | Governed checkpoint deciding whether a candidate can become a release artifact. | A shell command, file move, or UI toggle. |
| **PromotionDecision** | Recorded outcome of a promotion gate, including candidate, gates, reviewer or authority, result, and rollback target. | Runtime `ANSWER` or `DENY`. |
| **Catalog closure** | The point where catalog records, provenance, checksums, evidence references, and release references are sufficiently connected for review. | A loose bibliography. |
| **RunReceipt** | Record of a pipeline or validation run, including inputs, outputs, tool/version context, and outcome. | Release proof. |
| **TransformReceipt** | Record of a transformation such as redaction, generalization, clipping, reprojection, masking, or aggregation. | Informal note that data was changed. |
| **ValidationReport** | Structured result of schema, source-role, rights, sensitivity, provenance, geometry, and temporal checks. | Policy approval. |
| **PolicyDecision** | Policy-layer allow, deny, restrict, abstain, or obligation decision. | Validator success. |
| **Rollback target** | Prior known-good release or artifact state that can be restored or re-pointed to after error, withdrawal, or correction. | Backup copy without release context. |
| **CorrectionNotice** | Public or steward-facing record that explains a correction, supersession, withdrawal, or interpretation change. | Silent overwrite. |

[Back to top](#top)

---

## Source and evidence terms

| Term | Definition | Flora usage |
| --- | --- | --- |
| **SourceDescriptor** | Shared KFM source record describing identity, role, rights, cadence, sensitivity, access, and authority boundary. | Use as the generic source descriptor concept. |
| **FloraSourceDescriptor** | Flora-profiled descriptor for plant-related sources. | Should include plant-specific source roles, rights, spatial/temporal support, steward owner, and sensitivity posture. |
| **Source role** | Declared authority type and allowed claim usage of a source. | Required before processing or publication. Unknown role blocks promotion. |
| **Authority boundary** | The claim types a source is allowed to support. | A herbarium specimen may support occurrence evidence but not automatically legal status. |
| **Rights posture** | License, terms, redistribution, attribution, and access conditions for intended use. | Unknown rights fail closed. |
| **Sensitivity posture** | Public, restricted, generalized, redacted, steward-review, or controlled-access exposure posture. | Required before public geometry is served. |
| **EvidenceRef** | Stable pointer to evidence support. | Must resolve before consequential UI/API/Focus claims are made. |
| **EvidenceBundle** | Inspectable package of evidence references, source roles, limitations, policy posture, and support state for a claim. | Outranks generated summaries and map styling. |
| **Claim** | Evidence-bearing statement about a taxon, occurrence, specimen, status, layer, product, or public-safe artifact. | Must cite support or abstain. |
| **Inspectable claim** | Claim whose evidence, source role, spatial scope, temporal scope, policy posture, review state, release state, and correction lineage can be examined. | The public unit of value in KFM. |
| **Citation validation** | Check that claim text and evidence references actually support each other. | Needed before Focus answers or exports. |
| **Source freshness** | Recency or staleness relative to source cadence and release expectations. | Display in layer metadata, Evidence Drawer, and Focus output. |
| **Source as-of date** | Date a source statement or dataset version is valid or current as represented by the source. | Separate from retrieval and publication dates. |
| **Retrieval time** | Time KFM fetched or received a source artifact. | Not the same as observation time. |
| **Observation time** | Time a plant observation, collection, survey, or event occurred. | Not the same as ingest time. |
| **Publication time** | Time KFM released a public-safe artifact. | Not the same as source update time. |
| **Evidence limitation** | Known constraint on interpretation, such as uncertainty, incomplete coverage, scale, source role limit, or method caveat. | Should travel with the claim. |

[Back to top](#top)

---

## Flora domain terms

| Term | Definition | Flora usage |
| --- | --- | --- |
| **Flora lane** | KFM domain lane governing plant-related evidence, products, policies, and public-safe outputs. | Not a single map layer. |
| **Taxon** | A named biological classification unit such as species, subspecies, variety, genus, or family. | Use with source authority and name status. |
| **FloraTaxon** | KFM object family for normalized plant taxon identity. | Carries accepted name and crosswalk references. |
| **Accepted name** | Name selected as current or accepted within a stated taxonomic authority. | Must identify the authority or source basis. |
| **Synonym** | Alternate or historical name linked to an accepted name by a taxonomic source. | Do not treat as separate taxon unless source semantics require it. |
| **TaxonCrosswalk** | Mapping between raw source names/IDs and normalized Flora taxon IDs. | Required to keep source identity and normalized identity distinct. |
| **Unresolved taxon** | Name or ID that cannot be safely mapped to a normalized taxon. | Hold, review, or quarantine rather than guessing. |
| **Occurrence** | Source-backed indication that a plant taxon was observed, collected, reported, or otherwise recorded at a place and time. | Not automatically proof of current presence. |
| **OccurrenceEvidenceObject** | KFM object family for source-traceable plant occurrence support. | Must carry provenance, spatial/temporal support, and sensitivity posture. |
| **SpecimenRecord** | Herbarium or institutional specimen context, including catalog or collection metadata and uncertainty where available. | A specimen can support occurrence evidence but may have restricted or uncertain geometry. |
| **Voucher specimen** | Preserved or documented specimen used as evidence for identification or occurrence. | Strong evidence when provenance and identification are sound. |
| **Observation record** | Field, community, survey, or platform observation record. | Requires quality, source role, rights, sensitivity, and reviewer checks. |
| **Community observation** | Observation from community science or public reporting platforms. | Corroborative unless source-role policy says otherwise. |
| **Steward-reviewed record** | Record curated or approved by an accountable steward or qualified reviewer. | Does not automatically mean public exact release. |
| **StatusAssertion** | Jurisdiction-scoped claim about legal, conservation, invasive, native, rare, tracked, or other status. | Must carry source role and as-of date. |
| **Native status** | Claim about whether a plant is native within a defined geography and authority. | Source-dependent; do not infer from occurrence alone. |
| **Introduced status** | Claim that a plant is introduced, adventive, escaped, cultivated, or non-native under a source’s rules. | Keep distinct from invasive status. |
| **Invasive status** | Claim that a plant is invasive, noxious, regulated, or management-relevant under a defined source or authority. | Requires authority boundary and date. |
| **Rare plant** | Plant taxon or occurrence requiring special sensitivity or steward review because disclosure may cause harm or violate policy. | Exact public geometry fails closed unless explicitly approved. |
| **Range context** | Generalized spatial context describing known, expected, historical, modeled, or source-reported distribution. | Not the same as occurrence evidence. |
| **Phenology** | Timing of plant life-cycle events such as flowering, fruiting, leaf-out, senescence, or dormancy. | Must include observation or model basis. |
| **Plant community** | Vegetation grouping or ecological assemblage defined by a source classification. | Requires classification system and method. |
| **VegetationProduct** | Derived vegetation, phenology, index, classification, or model artifact. | Must carry method, uncertainty, time basis, masks, and source lineage. |
| **Vegetation index** | Remote-sensing-derived indicator such as greenness or vegetation condition. | Derived context, not direct plant occurrence truth. |
| **HabitatAssociation** | Derived relationship between flora evidence and habitat, soil, hydrology, climate, land-cover, or other covariate layers. | Keep as versioned derivative, not canonical truth. |
| **Presence claim** | Claim that a taxon is present in a defined scope. | Needs occurrence/specimen/status support and temporal bounds. |
| **Absence claim** | Claim that a taxon is absent from a defined scope. | High burden; often requires survey design evidence and should otherwise abstain. |
| **Survey effort** | Information about search intensity, method, observer, time, or coverage. | Needed to interpret absence or detection confidence. |
| **Georeference uncertainty** | Spatial uncertainty around a coordinate, locality, or mapped geometry. | Must be explicit and cannot be hidden by point precision. |
| **Coordinate precision** | Numeric precision of a coordinate. | Not the same as true spatial accuracy. |
| **Geometry support** | Evidence basis for point, polygon, range, generalized area, or aggregate geometry. | Must state whether geometry is observed, inferred, modeled, generalized, or redacted. |

[Back to top](#top)

---

## Sensitivity and policy terms

| Term | Definition | Flora usage |
| --- | --- | --- |
| **Sensitivity class** | Policy label controlling precision, exposure, review burden, and access. | Public, generalized, restricted, embargoed, or steward-review classes may apply. |
| **Geoprivacy** | Policy and technical practice of limiting precise location exposure. | Essential for rare plants and controlled records. |
| **Public-safe artifact** | Output approved for public or semi-public surfaces after validation, policy, review, catalog, release, and rollback checks. | Not equivalent to “has a map tile.” |
| **Public-safe geometry** | Geometry precision and representation approved for intended audience and risk class. | May be exact, generalized, aggregated, suppressed, or safe-stubbed. |
| **Exact geometry** | Precise point, polygon, or locality geometry. | Restricted by default for sensitive plant records. |
| **Generalized geometry** | Reduced-precision geometry suitable for public-safe display. | Requires transform receipt and clear disclosure. |
| **Redacted geometry** | Geometry with sensitive precision or attributes removed. | Must preserve enough evidence context for appropriate public explanation. |
| **Safe stub** | Public placeholder showing a restricted record exists or is withheld without disclosing sensitive detail. | Better than silently disappearing when policy allows existence disclosure. |
| **Embargo** | Time-bound restriction delaying publication or precision release. | Must include conditions and review path. |
| **Controlled access** | Access limited by terms, steward decision, role, policy, or source agreement. | Public release denied unless explicitly authorized. |
| **Steward review** | Human or institutional review required before a risky or sensitive action. | Must be recorded separately from automated validation. |
| **Fail closed** | Default to hold, deny, quarantine, or abstain when rights, sensitivity, role, or evidence is unresolved. | Core Flora publication posture. |
| **Deny condition** | A specific condition that blocks public release or disclosure. | Examples: missing rights, unknown source role, sensitive exact geometry, broken EvidenceRef. |
| **Review obligation** | Required human, steward, or policy step before promotion. | Should appear in PolicyDecision or review records. |
| **Attribution requirement** | Required credit or source statement attached to reuse or publication. | Must travel with published artifacts and exports. |

[Back to top](#top)

---

## Catalog, release, and rollback terms

| Term | Definition | Flora usage |
| --- | --- | --- |
| **ReleaseManifest** | Promotion-time inventory of published artifacts, digests, policy/review references, and rollback target. | Required before public release claims. |
| **LayerManifest** | Map-facing descriptor for a public-safe layer, including source role, freshness, review, sensitivity, evidence route, and release context. | Style is not truth; manifest carries meaning. |
| **Artifact** | Generated or stored object such as data file, layer, tile archive, catalog record, proof, receipt, or release bundle. | Use with artifact class and lifecycle state. |
| **Proof pack** | Bundle of validation, policy, catalog, receipt, manifest, and review evidence supporting a release. | Not a substitute for the source evidence itself. |
| **Receipt** | Process memory emitted by a run or transform. | Receipts support auditability but do not approve publication. |
| **STAC** | SpatioTemporal Asset Catalog metadata surface for discoverable spatial/temporal assets. | Catalog closure helper. |
| **DCAT** | Data Catalog Vocabulary surface for dataset/distribution metadata. | Interoperability helper. |
| **PROV** | Provenance model for lineage and generation relationships. | Provenance closure helper. |
| **spec_hash** | Deterministic digest of a specification, schema, descriptor, or process definition. | Helps diff, reproduce, and verify artifacts. |
| **content hash** | Digest of file or payload content. | Not the same as spec hash. |
| **Release ID** | Stable identifier for a release. | Should travel with map layers, drawer payloads, exports, and corrections. |
| **Supersession** | Replacement of an older object or release by a newer one with visible lineage. | Prefer over silent overwrite. |
| **Withdrawal** | Removal or de-publication of a release or claim due to error, rights, sensitivity, or policy. | Requires correction notice and rollback context. |
| **Rollback card** | Human-readable rollback instructions and affected surfaces for a release. | Needed before risky promotion. |

[Back to top](#top)

---

## UI, API, and Focus terms

| Term | Definition | Flora usage |
| --- | --- | --- |
| **Governed API** | API boundary that resolves evidence, applies policy, and emits finite envelopes before public UI consumption. | Flora public clients should use this, not raw source data. |
| **DecisionEnvelope** | Finite decision outcome and reason context. | Carries `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` for runtime surfaces. |
| **RuntimeResponseEnvelope** | Shared response envelope for governed runtime outputs. | Should preserve citations, policy state, evidence refs, and reason codes. |
| **Evidence Drawer** | Trust-visible UI surface showing what backs a claim. | Should show EvidenceBundle refs, source role, rights, sensitivity, freshness, review, and correction state. |
| **EvidenceDrawerPayload** | Payload powering the Evidence Drawer. | Must not be a tooltip-only summary. |
| **Focus Mode** | Evidence-bounded synthesis surface inside the governed shell. | Not a free-form botanical chatbot. |
| **FocusQueryRequest** | Request payload for a scoped Focus question. | Should include place, time, audience, release, evidence scope, and policy context. |
| **FocusQueryResponse** | Finite, citation-bearing Focus response. | Must show outcome, scope echo, evidence refs, reason codes, and audit reference. |
| **Trust cue** | Persistent signal such as source role, freshness, evidence state, rights/sensitivity, review state, or AI participation. | Should appear where meaning changes. |
| **Negative state** | Visible state explaining why content is absent, withheld, denied, stale, conflicted, or failed. | Do not hide behind empty panels. |
| **MapLibre layer** | Rendered map layer in the browser shell. | Downstream carrier of public-safe release artifacts, not source truth. |
| **Style expression** | Renderer configuration controlling appearance. | Must not silently encode business meaning or policy decisions. |
| **Popup** | Lightweight hover or click summary. | Not enough for consequential claims; use Evidence Drawer. |
| **Review surface** | Role-gated steward/reviewer interface. | Review changes must be logged and distinct from public UI behavior. |
| **Export surface** | Preview or package of outward artifacts. | Must preserve trust cues, citations, release ID, policy context, and correction state. |
| **Audit reference** | Link or identifier connecting a UI/API outcome to receipts, validation, or runtime trace. | Needed for review and correction. |

[Back to top](#top)

---

## Anti-collapse rules

These pairs must stay distinct in Flora docs and payloads.

| Do not collapse | Rule |
| --- | --- |
| Taxon identity vs occurrence evidence | A normalized taxon is not proof of presence at a place and time. |
| Occurrence vs current presence | Historical or uncertain occurrence is not automatically current presence. |
| Specimen vs observation | Both may support occurrence, but they carry different provenance and uncertainty. |
| Community observation vs official status | Community records cannot serve as legal or official status authority by default. |
| Range context vs exact occurrence | Range products are generalized or modeled context unless source evidence says otherwise. |
| Derived model vs observation truth | Vegetation models, suitability, indices, and heatmaps are derived products. |
| Coordinate precision vs location accuracy | More decimals do not mean better evidence. |
| Public map layer vs published truth | A layer is a carrier; evidence and release records carry authority. |
| Receipt vs proof | A receipt records a run; proof supports release. |
| Catalog record vs EvidenceBundle | Catalog supports discovery; EvidenceBundle supports claims. |
| Policy decision vs validator pass | Validation checks shape and constraints; policy decides admissibility and obligations. |
| Focus answer vs source evidence | Generated language remains subordinate to EvidenceBundle support. |

[Back to top](#top)

---

## Term maintenance

Update this glossary when any of the following changes:

- A Flora companion doc introduces a new trust-bearing term.
- A schema or contract adds, renames, or removes an object family.
- A source descriptor adds a new source role, rights state, cadence state, or sensitivity class.
- A policy introduces a new deny condition or review obligation.
- A UI/API payload adds a new outcome, trust cue, or negative state.
- A release, rollback, correction, or publication process changes vocabulary.
- A term is used inconsistently across docs.

### Update checklist

- [ ] Definition is short enough to scan.
- [ ] Definition states what the term is **not** when confusion is likely.
- [ ] Related companion docs are updated.
- [ ] Schema/contract names are not invented or renamed silently.
- [ ] Policy-sensitive terms include fail-closed language where needed.
- [ ] UI terms preserve Evidence Drawer and Focus boundaries.
- [ ] New public-facing terms avoid revealing restricted details.
- [ ] `registers/FILE_MANIFEST.md` still points to this glossary.
- [ ] Any flat-path references are checked against current nested repo layout.

[Back to top](#top)

---

## Appendix: compact starter glossary

<details>
<summary>Original seed terms preserved and expanded</summary>

| Seed term | Preserved definition |
| --- | --- |
| **EvidenceBundle** | Inspectable set of evidence references backing a claim. |
| **DecisionEnvelope** | Finite decision outcome and reason context. |
| **Source role** | Declared authority type and allowed claim usage of a source. |
| **Sensitivity class** | Policy label that controls precision and exposure. |
| **Public-safe artifact** | Output approved for public surfaces after policy checks. |
| **Transform receipt** | Record of geometry redaction/generalization operations. |
| **Promotion gate** | Final release decision checkpoint for publication. |
| **Quarantine** | State for records blocked by unresolved rights, sensitivity, or integrity. |
| **Rollback target** | Identified prior release that can be restored if needed. |

</details>
