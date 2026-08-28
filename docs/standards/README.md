<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-standards-readme
title: docs/standards/ — Standards, Profiles, and Interoperability Guidance
type: readme/boundary-readme
version: v1.1
status: "active; repository-grounded; mixed-maturity"
owners:
  - "@bartytime4life"
created: 2026-05-08
updated: 2026-08-14
policy_label: repository-facing
owning_root: docs/
responsibility: "Define the human-readable standards and interoperability-guidance lane, disclose its current inventory and evidence limits, and route semantic, machine-shape, policy, validation, source, and release authority to their owning responsibility roots."
truth_posture: "CONFIRMED current path, direct-child inventory, default CODEOWNERS route, adopted Directory Rules v2, and observed child-file presence / PARTIAL child reconciliation, standards currentness, machine conformance, and consumer coverage / NEEDS VERIFICATION accountable standards stewardship, adoption state, supersession, and case-collision disposition"
evidence_snapshot: "main@cbee7add137b9738b3d123b17d41ac3d44d9745b; prior target blob cf1152d04aaf39f7dc01aa00faca211528e5ce0b; Directory Rules blob fd49a0b83e55cef52c1124281f093e263526898d; docs root README blob 1f8bac189dac1d01c1185e8b4fb8e25efd11d09f; CODEOWNERS blob dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61; 50 direct Markdown files and 2 direct child directories"
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/sources/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - contracts/README.md
  - schemas/README.md
  - policy/README.md
  - tests/README.md
  - .github/CODEOWNERS
notes:
  - "v1.1 replaces proposal-era inventory claims with a current, exact 52-entry direct-child map."
  - "The update distinguishes path presence, upstream-standard currentness, KFM adoption/profile state, implementation/validation state, and release/publication state."
  - "No child file, standard, profile, contract, schema, policy rule, source, validator, release object, runtime, or public surface is adopted, renamed, consolidated, retired, activated, or published by this README."
  - "Observed case collisions and overlapping profile families remain visible as drift and verification work; this change does not silently choose a winner."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/standards/` — Standards, Profiles, and Interoperability Guidance

`docs/standards/` is KFM's repository-facing lane for human-readable descriptions of external standards, KFM-specific profiles and mappings, interoperability guidance, and supporting trust or operational conventions.

> [!IMPORTANT]
> **A standards document is not conformance proof.** A path, profile name, version string, badge, example, validator result, receipt, pull request, or merged commit does not by itself prove that KFM has adopted an upstream standard, implements every requirement, is interoperable with a named consumer, or has released a conforming artifact.

> [!WARNING]
> **This lane has mixed maturity and unresolved naming drift.** The directory contains 50 direct Markdown files and two direct child directories at the evidence snapshot. Presence is confirmed; exhaustive semantic review, upstream-currentness review, adoption state, machine parity, consumer use, and supersession state are not.

> [!CAUTION]
> **External standards do not override KFM trust controls.** Interoperable shape or protocol compatibility never substitutes for source authority, rights, sensitivity handling, EvidenceBundle support, policy, review, release, correction, or rollback.

**Quick navigation:** [Purpose](#purpose-and-inherited-authority) · [Authority](#authority-and-negative-authority) · [Status](#status-and-evidence-boundary) · [Map](#direct-child-map) · [Start here](#start-here) · [Inventory](#current-inventory-and-navigation-groups) · [State model](#adoption-and-conformance-state-model) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Flow](#inputs-outputs-and-permitted-writers) · [Exposure](#exposure-rights-and-sensitivity) · [Storage](#mutability-retention-and-generation) · [Validation](#validation-and-negative-checks) · [Review](#ownership-review-and-escalation) · [Adjacent roots](#adjacent-responsibility-roots) · [Drift](#known-drift-and-conflicts) · [Change protocol](#change-protocol) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis-and-limitations) · [Rollback](#last-evidence-review-and-rollback) · [Summary](#status-summary)

---

<a id="purpose-and-inherited-authority"></a>

## Purpose and inherited authority

This lane inherits the [`docs/` root contract](../README.md). Its primary responsibility is to help maintainers, reviewers, source stewards, domain stewards, implementers, and external integrators understand:

- which external standard, protocol, vocabulary, format, or interoperability practice a document discusses;
- whether the document is a reference, a KFM profile, a mapping, an operational convention, or an unresolved proposal;
- which upstream specification and version the claim depends on;
- which KFM object families, lifecycle stages, domains, and public surfaces are in scope;
- where semantic meaning, machine shape, policy, fixtures, validators, source identity, evidence, and release authority live;
- what validation can and cannot prove; and
- what remains stale, conflicted, superseded, unverified, or held.

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Those rules identify `docs/standards/` as the human-readable standards-guidance lane under `docs/`. This same-path update uses the adopted `BOUNDARY_COMPACT` README profile; it does not create a new root or standards authority.

[Back to top](#top)

---

<a id="authority-and-negative-authority"></a>

## Authority and negative authority

`docs/standards/` is canonical for **human-readable standards guidance and navigation only**. Each underlying decision remains owned by the responsibility root that legitimately defines it.

| Question | Owning authority | Role of `docs/standards/` |
|---|---|---|
| Where standards guidance belongs | Adopted Directory Rules and the parent [`docs/`](../README.md) contract | Explain the lane and surface placement drift |
| What a KFM object or interface means | `contracts/` | Cite meaning; do not redefine semantic authority |
| What machine shape is valid | `schemas/` | Cite schema/profile bindings; do not host machine-shape authority |
| What is allowed, denied, held, redacted, restricted, or abstained | `policy/` plus governed review | Explain posture and obligations; do not decide admissibility |
| Whether an upstream source may be used | Source admission, rights review, `SourceDescriptor`, and source registry | Record standards relationships; do not activate sources |
| Whether an implementation actually conforms | Current code/config, validators, fixtures, tests, generated reports, and observed consumers | State the checked boundary; do not infer full conformance |
| Whether a release may publish | `release/`, evidence/proof families, policy, and authorized review | Explain prerequisites; do not approve release |
| Whether an external standard is current | The authoritative upstream issuer at a dated access point | Record the verification snapshot and currentness risk |
| This README | Human navigation, current-state disclosure, and update protocol | No contract, schema, policy, runtime, release, or publication authority |

A standards page may use normative words when it accurately reports an adopted KFM profile or an upstream requirement. The page must identify which authority makes the requirement binding. Unattributed `MUST`, `SHOULD`, or “KFM conforms” language remains a draft claim, not automatic policy.

[Back to top](#top)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

The observations below are pinned to `main@cbee7add137b9738b3d123b17d41ac3d44d9745b`. They establish tracked repository bytes and selected metadata, not upstream-standard currentness, deployed behavior, complete validator coverage, consumer interoperability, release approval, or publication.

| Surface | CONFIRMED observation | Bounded conclusion |
|---|---|---|
| This README | Prior blob `cf1152d04aaf39f7dc01aa00faca211528e5ce0b`; first path history is visible on 2026-05-08; current text still says child paths are unverified proposals | Same-path v1.1 reconciliation is warranted |
| Direct inventory | 52 direct entries: 50 Markdown files and two directories (`PROV/`, `pmtiles/`) | The current direct-child map is exactly known at the pinned revision |
| Child bodies | Selected profiles remain dated May 2026 drafts and contain proposal-era “not yet authored” or unmounted-repository language | Useful content exists, but lane-wide currency and adoption do not |
| KFM profile surfaces | STAC, provenance, sensitivity, redaction, signing, receipt, release-manifest, and map-trust documents are present | Presence does not prove adopted profile authority or machine parity |
| Upstream-reference surfaces | Catalog, geospatial, archival, semantic, biodiversity, and protocol documents are present | Upstream versions, terms, rights, errata, and currentness require file-specific verification |
| Specialized sublanes | `PROV/README.md` exists; `pmtiles/` contains `PMIDX_SPEC_V1.md` and `PMTILES_ATTESTATION_STANDARD.md` | Their relationship to same-topic root files needs explicit reconciliation |
| Review routing | Repository-default CODEOWNERS routing names `@bartytime4life`; there is no dedicated `/docs/standards/` rule | One GitHub review route is verified; accountable standards stewardship and independent review are not |
| Contracts, schemas, policy, validators, fixtures, workflows, emitted artifacts, runtime consumers, releases | Not established by this index | `UNKNOWN` unless proven by exact-revision owning-surface evidence |

### State separation

Do not collapse these independent states:

| Axis | Example |
|---|---|
| Path presence | `STAC_KFM_PROFILE.md` exists |
| Document-declared state | The file says draft, active, proposed, superseded, or another status |
| Upstream-currentness state | The cited standard/version was checked against its authoritative issuer on a dated access |
| KFM adoption state | An accepted ADR, contract, policy, or other authorized decision makes a profile binding |
| Machine-shape state | A schema exists and validates representative positive and negative fixtures |
| Implementation state | Producers and consumers emit or accept the profile at a known revision |
| Validation state | A named validator checks a bounded requirement set with stable outcomes |
| Review state | Authorized review is complete for a named version and scope |
| Release state | An immutable release includes the profile and required proofs |
| Publication state | A public-safe artifact is exposed through governed delivery |
| Correction state | Supersession, withdrawal, cache invalidation, and rollback are traceable |

A green documentation check confirms only documentation quality for the checked revision. A green schema or profile check confirms only its declared assertions. Neither proves complete interoperability or publication readiness.

[Back to top](#top)

---

<a id="direct-child-map"></a>

## Direct-child map

Directory Rules require this README to show only the directory it governs and its direct children. The map is current inventory, not a proposed target tree.

```text
docs/standards/
├── README.md                          # lane boundary, inventory, evidence limits, and change protocol
├── ARCHIVAL-STANDARDS.md              # archival interoperability guidance
├── CANONICALIZATION.md                # uppercase canonicalization guidance
├── CIDOC-CRM.md                       # cultural-heritage semantic-model guidance
├── COG.md                             # Cloud Optimized GeoTIFF guidance
├── CONSENT_TOKENS.md                  # consent-token and obligation guidance
├── DCAT.md                            # data-catalog vocabulary guidance
├── DEBOUNCE_WINDOWS.md                # change-detection debounce conventions
├── DP_BUDGETS.md                      # differential-privacy budget guidance
├── DUBLIN-CORE.md                     # Dublin Core metadata guidance
├── DUO_MAPPING.md                     # Data Use Ontology mapping guidance
├── DUO_PROFILE.md                     # KFM DUO profile guidance
├── Darwin_Core.md                     # Darwin Core guidance
├── EVIDENCE_BUNDLE.md                 # evidence-bundle documentation profile
├── FGDC-CSDGM.md                      # FGDC CSDGM metadata guidance
├── GEOPARQUET.md                      # GeoParquet guidance
├── IIIF.md                            # uppercase IIIF guidance
├── ISO-19115.md                       # ISO 19115 metadata guidance
├── MAP_TRUST_STATES.md                # trust-visible map-state vocabulary
├── MVT.md                             # Mapbox Vector Tile guidance
├── OAI-PMH.md                         # uppercase OAI-PMH guidance
├── OGC-API-TILES.md                   # OGC API - Tiles guidance
├── OPENLINEAGE_FACETS.md              # OpenLineage facet guidance
├── PMTILES.md                         # root-level PMTiles guidance
├── PROV-O.md                          # PROV-O guidance
├── PROV.md                            # PROV guidance
├── PROVENANCE.md                      # broader provenance profile guidance
├── REDACTION_DETERMINISM.md           # deterministic-redaction guidance
├── REDACTION_PROFILES.md              # named redaction-profile guidance
├── RELEASE_MANIFEST.md                # release-manifest documentation profile
├── RUN_RECEIPT.md                     # run-receipt documentation profile
├── SCHEMA-ORG.md                      # Schema.org guidance
├── SENSITIVITY_RUBRIC.md              # sensitivity classification guidance
├── SIGNING.md                         # signing and verification guidance
├── SMART_SYNC.md                      # synchronization and material-change guidance
├── STAC-DwC.md                        # STAC-Darwin Core mapping guidance
├── STAC-EO.md                         # STAC EO guidance
├── STAC.md                            # uppercase STAC guidance
├── STAC_DWC_PROFILE.md                # KFM STAC-DwC profile guidance
├── STAC_KFM_PROFILE.md                # KFM STAC profile guidance
├── STAC_KFM_TRUST_EXTENSION.md        # KFM STAC trust-extension guidance
├── TELEMETRY_MINIMUMS.md              # telemetry-minimum guidance
├── WMTS.md                            # Web Map Tile Service guidance
├── canonicalization.md                # lowercase canonicalization guidance
├── connector-rate-limits.md           # connector rate-limit guidance
├── iiif.md                            # lowercase IIIF guidance
├── oai-pmh.md                         # lowercase OAI-PMH guidance
├── snac-eac-cpf.md                    # SNAC / EAC-CPF guidance
├── stac-dwc-hybrid.md                 # lowercase STAC-DwC hybrid guidance
├── stac.md                            # lowercase STAC guidance
├── PROV/                              # nested provenance guidance; direct child details owned below
└── pmtiles/                           # specialized PMTiles standards; direct child details owned below
```

The two child directories currently contain:

- `PROV/README.md`;
- `pmtiles/PMIDX_SPEC_V1.md`; and
- `pmtiles/PMTILES_ATTESTATION_STANDARD.md`.

Those grandchildren are listed here only to explain the direct-child directory responsibilities; this README does not reproduce their deeper trees.

[Back to top](#top)

---

<a id="start-here"></a>

## Start here

| Need | Current entry point | Boundary |
|---|---|---|
| Understand this lane | [`README.md`](./README.md) | Navigation and current-state disclosure only |
| Read adopted placement law | [`directory-rules.md`](../doctrine/directory-rules.md) and accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Placement authority, not standards adoption |
| Understand semantic meaning | [`contracts/README.md`](../../contracts/README.md) | Contracts own KFM object meaning |
| Validate machine shape | [`schemas/README.md`](../../schemas/README.md) | Schemas own machine-valid shape |
| Understand allow/deny/redact/hold rules | [`policy/README.md`](../../policy/README.md) | Policy owns admissibility |
| Understand upstream source authority | [`docs/sources/README.md`](../sources/README.md) | A standard or format is not automatically a source |
| Record unresolved placement or naming conflict | [`DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) | Do not silently rename or consolidate |
| Record a checkable unresolved question | [`VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) | Verification work does not self-adopt a profile |
| Review KFM STAC guidance | [`STAC_KFM_PROFILE.md`](./STAC_KFM_PROFILE.md) | Current file declares draft; machine parity requires separate evidence |
| Review sensitive-release guidance | [`SENSITIVITY_RUBRIC.md`](./SENSITIVITY_RUBRIC.md), [`REDACTION_PROFILES.md`](./REDACTION_PROFILES.md), [`CONSENT_TOKENS.md`](./CONSENT_TOKENS.md) | Guidance is not policy approval |
| Review integrity and release support | [`SIGNING.md`](./SIGNING.md), [`RUN_RECEIPT.md`](./RUN_RECEIPT.md), [`RELEASE_MANIFEST.md`](./RELEASE_MANIFEST.md) | Documentation is not an attestation or release decision |
| Review PMTiles guidance | [`PMTILES.md`](./PMTILES.md) and [`pmtiles/`](./pmtiles/) | Root/subdirectory relationship remains under review |

[Back to top](#top)

---

<a id="current-inventory-and-navigation-groups"></a>

## Current inventory and navigation groups

The groups below are navigation aids, not adoption categories. A file can participate in more than one concern.

| Group | Observed direct surfaces | Current bounded posture |
|---|---|---|
| Catalog, metadata, and provenance | `STAC*`, `DCAT.md`, `PROV*`, `PROVENANCE.md`, `OPENLINEAGE_FACETS.md`, `DUBLIN-CORE.md`, `FGDC-CSDGM.md`, `ISO-19115.md`, `SCHEMA-ORG.md` | Paths confirmed; authority, currentness, overlap, and machine parity require file-specific review |
| Geospatial carriers and delivery protocols | `COG.md`, `GEOPARQUET.md`, `MVT.md`, `PMTILES.md`, `pmtiles/`, `WMTS.md`, `OGC-API-TILES.md` | Paths confirmed; format support and release readiness are separate claims |
| Archival and cultural interoperability | `ARCHIVAL-STANDARDS.md`, `CIDOC-CRM.md`, `IIIF.md`, `iiif.md`, `OAI-PMH.md`, `oai-pmh.md`, `snac-eac-cpf.md` | Paths confirmed; case collisions and source/version currentness remain unresolved |
| Biodiversity and data-use profiles | `Darwin_Core.md`, `STAC-DwC.md`, `STAC_DWC_PROFILE.md`, `stac-dwc-hybrid.md`, `DUO_MAPPING.md`, `DUO_PROFILE.md` | Paths confirmed; profile relationship, rights posture, and adoption require review |
| Trust, integrity, and publication support | `EVIDENCE_BUNDLE.md`, `MAP_TRUST_STATES.md`, `SIGNING.md`, `RUN_RECEIPT.md`, `RELEASE_MANIFEST.md`, `STAC_KFM_TRUST_EXTENSION.md` | Human guidance exists; canonical meaning, machine shape, policy, proof, and release authority remain elsewhere |
| Sensitivity, privacy, and redaction | `CONSENT_TOKENS.md`, `DP_BUDGETS.md`, `REDACTION_DETERMINISM.md`, `REDACTION_PROFILES.md`, `SENSITIVITY_RUBRIC.md` | Fail-closed review required; documents do not authorize sensitive-data handling |
| Operational conventions | `DEBOUNCE_WINDOWS.md`, `SMART_SYNC.md`, `TELEMETRY_MINIMUMS.md`, `connector-rate-limits.md`, `CANONICALIZATION.md`, `canonicalization.md` | Guidance exists; implementation and enforcement require exact-revision evidence |

### What the inventory does not prove

The table does not establish that:

- every file is current, adopted, non-duplicative, or correctly named;
- every upstream specification is cited at its current version;
- every KFM profile has a corresponding contract, schema, policy, fixture, validator, workflow, producer, and consumer;
- every declared validator or path still exists;
- any profile is required by branch protection or release policy;
- any release has passed the profile; or
- any public endpoint or carrier is currently exposed.

[Back to top](#top)

---

<a id="adoption-and-conformance-state-model"></a>

## Adoption and conformance state model

Every standards/profile claim should expose these dimensions separately.

| Dimension | Minimum evidence |
|---|---|
| Identity | Stable document/profile ID, exact path, version, and content digest |
| Upstream authority | Issuing organization, authoritative locator, specification/version, publication or release date, and access date |
| Scope | Object families, lifecycle stages, domains, actor classes, and public/private boundaries covered |
| KFM status | Reference-only, proposed, accepted, active, deprecated, superseded, or retired, with decision reference |
| Mapping | Explicit upstream-to-KFM fields, vocabularies, extension points, and unresolved differences |
| Semantic binding | Canonical contract references |
| Machine binding | Canonical schema/profile references and version compatibility |
| Policy binding | Rights, sensitivity, access, release, and failure outcomes |
| Validation binding | Validator, fixtures, tests, workflow, checked revision, and limitations |
| Producer/consumer evidence | Named emitters and consumers verified at a revision |
| Release binding | Manifest, proof, policy/review state, correction path, and rollback target |
| Currentness | Review trigger, upstream change/errata monitoring, and stale-state behavior |

Suggested status vocabulary for narrative records is **PROPOSED**, **ACCEPTED**, **ACTIVE**, **DEPRECATED**, **SUPERSEDED**, **RETIRED**, or **HOLD**, but an existing file's vocabulary must not be mass-normalized without checking its owning contract and consumers.

### Conformance evidence levels

| Level | Meaning |
|---|---|
| Documented | A human-readable profile or posture exists |
| Shape-tested | Representative instances validate against the declared schema/profile |
| Negative-tested | Required unsafe or invalid cases fail for expected reasons |
| Producer-verified | A named producer emits conforming output at a pinned revision |
| Consumer-verified | A named consumer accepts and correctly interprets the profile |
| Release-verified | A governed release binds profile version, proofs, policy/review state, correction, and rollback |
| Interoperability-observed | An external or independent implementation exchange was observed and recorded |

Higher levels require the lower evidence relevant to the claim, but no label here authorizes release by itself.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

Material belongs in `docs/standards/` when its primary responsibility is human-readable standards or interoperability guidance, including:

- upstream-standard summaries with authoritative source and version/currentness records;
- KFM profiles that explain how an external standard is narrowed or extended;
- mappings and crosswalks between standards and KFM object families;
- format and protocol posture, limits, and public-safe usage guidance;
- human-readable conformance checklists and failure semantics;
- trust, integrity, sensitivity, or operational conventions that are explicitly documentation profiles rather than executable authority;
- small illustrative examples whose authoritative fixtures live elsewhere; and
- migration, deprecation, or supersession notes for standards/profile documents.

A child may cite contracts, schemas, policy, fixtures, validators, source descriptors, evidence, releases, and runtime consumers. It must keep those authorities in their own roots.

[Back to top](#top)

---

<a id="what-does-not-belong-here"></a>

## What does not belong here

| Prohibited canonical content or decision | Owning authority or action |
|---|---|
| Semantic object or interface contracts | `contracts/` |
| JSON Schema, SHACL, generated types, or other machine-shape authority | `schemas/` or the adopted schema authority |
| Rego/OPA or other executable admissibility rules | `policy/` |
| Executable validators, generators, conversion tools, or migration code | `tools/`, `pipelines/`, `packages/`, or another execution root selected by role |
| Positive/negative golden fixtures and test suites | `fixtures/` and `tests/` |
| Source payloads, credentials, API keys, or source-admission decisions | Governed source and lifecycle families; secrets are never committed |
| EvidenceBundle instances, receipts, proofs, catalog records, or published carriers | Their governed `data/` accountability and lifecycle families |
| Release manifests, PromotionDecisions, correction notices, withdrawal notices, or rollback cards | `release/` |
| A copied upstream specification presented as KFM authority without rights and version controls | Link to the authoritative source; retain only licensed, reviewed excerpts where necessary |
| Direct public routes or runtime configuration | Governed applications, runtime, configuration, and released artifacts |
| Unreviewed sensitive examples or exact protected locations | Quarantine, redact, generalize, stage, delay, abstain, or deny |

> [!CAUTION]
> A long code block can silently become a second schema, policy, or fixture authority. Keep examples bounded, label them illustrative, and link to the canonical executable source.

[Back to top](#top)

---

<a id="inputs-outputs-and-permitted-writers"></a>

## Inputs, outputs, and permitted writers

### Inputs

Admissible inputs include:

- adopted doctrine and accepted ADRs;
- authoritative upstream standard, protocol, format, or vocabulary publications;
- current repository contracts, schemas, policy, fixtures, validators, tests, workflows, producers, consumers, and generated reports;
- source terms, rights, attribution, sensitivity, and redistribution decisions;
- evidence, receipts, proofs, releases, corrections, and rollback records when a conformance claim depends on them; and
- historical KFM reports and atlases as lineage, not automatic current authority.

Version-sensitive upstream facts require a dated authoritative-source check. A planning report or older profile cannot establish current external version, terms, package support, or interoperability.

### Outputs

This lane produces human-readable profiles, mappings, usage guides, currentness records, conformance expectations, deprecation notes, and navigation. Machine projections, schemas, policy, validators, fixtures, receipts, proofs, releases, and published artifacts remain separate outputs of their owning processes.

### Permitted writers

Normal writers are reviewed repository changes on feature branches. Automation may propose or synchronize text only when the canonical source, generator, edit policy, and parity check are explicit.

A writer must not use its own draft, generated receipt, passing documentation check, or pull request as proof of standards adoption, independent review, conformance, release, or publication.

[Back to top](#top)

---

<a id="exposure-rights-and-sensitivity"></a>

## Exposure, rights, and sensitivity

`docs/standards/` is repository-facing and may be publicly readable. Treat every example, locator, identifier, and quoted requirement as a potential exposure.

- Do not commit credentials, private endpoints, signed URLs, restricted source excerpts, private personal data, exact protected locations, or confidential interoperability test data.
- Record upstream copyright, license, attribution, trademark, patent, terms-of-use, and redistribution constraints where material.
- For living-person, genomic, rare-species, archaeology, infrastructure, land/title, sovereignty, cultural, tribal, or harmful-precision concerns, prefer fail-closed handling and qualified review.
- A public document may explain that redaction or denial occurs without exposing the protected payload or a sensitive reason that creates a new risk.
- Example records must be synthetic or demonstrably public-safe and must not be mistaken for released KFM data.

Standards interoperability does not waive KFM's rights, sensitivity, or public-safety obligations.

[Back to top](#top)

---

<a id="mutability-retention-and-generation"></a>

## Mutability, retention, and generation

| Property | Rule |
|---|---|
| Physical storage | Tracked Git documentation unless a child declares a governed generated or external relationship |
| Mutability | Reviewed, versioned replacement; append-only history where the profile class requires it |
| Upstream currentness | Re-review on upstream version, errata, governance, terms, or security change |
| KFM profile changes | Preserve profile identity/version and compatibility expectations; do not silently change meaning |
| Generated content | Edit the canonical source and regenerate; do not hand-edit a verified mirror |
| Deprecation | Record replacement, effective scope, consumers, compatibility window, correction path, and exit criteria |
| Retention | Preserve decision and supersession lineage even when a profile is retired |
| Deletion | Require identity, inbound-reference and consumer review, migration evidence, and Git-recoverable rollback |

A filename change can affect external links, schema identifiers, profile URIs, generated docs, imports, tests, and release references. Case-only renames are especially risky across filesystems and require explicit migration handling.

[Back to top](#top)

---

<a id="validation-and-negative-checks"></a>

## Validation and negative checks

Documentation validation is necessary but not sufficient. Use the smallest repository-native check set that covers the actual delta.

### Documentation checks

- `KFM_META_BLOCK_V2` structure and review-only document-registry comparison;
- one H1, heading order, anchors, alerts, tables, fences, and HTML;
- repository-relative paths, case, links, and fragments;
- documentation graph and stale-reference checks;
- exact direct-child inventory when this README changes;
- generated/mirror synchronization where declared; and
- secrets, rights, sensitivity, and unsafe-example review.

### Profile and conformance checks

When a child makes stronger claims, require the corresponding evidence:

- upstream specification/version/currentness verification;
- contract/schema/policy cross-reference closure;
- positive and negative fixtures;
- validator and workflow outcomes tied to an exact revision;
- producer and consumer compatibility tests;
- deterministic canonicalization or digest checks where required;
- source-rights and public-safe release checks;
- correction, withdrawal, and rollback behavior; and
- independent interoperability evidence when that claim is made.

### Negative checks

Hold or fail a change that would:

- claim “KFM conforms” without defining scope and evidence level;
- treat a documentation profile as contract, schema, policy, source, proof, or release authority;
- cite a missing, stale, superseded, or unverified upstream specification as current;
- create another writable profile for an existing topic without migration or supersession;
- hide case collisions or overlapping names;
- break stable profile IDs, anchors, links, or known consumers without compatibility handling;
- expose restricted material or harmful precision;
- hand-edit a generated target; or
- treat a passing validator as release or publication approval.

A green result must name what was checked, against which revision and profile version, and what remains outside the boundary.

[Back to top](#top)

---

<a id="ownership-review-and-escalation"></a>

## Ownership, review, and escalation

**CONFIRMED GitHub review route:** repository-default CODEOWNERS routing names `@bartytime4life`.

**NEEDS VERIFICATION:** accountable standards steward, upstream-domain experts, privacy/rights reviewers, security reviewers, catalog/provenance reviewers, release authority, and independent interoperability reviewers.

CODEOWNERS routing requests GitHub review. It is not a stewardship assignment, qualification record, approval, separation-of-duties proof, release decision, or publication authority.

Review depth should follow significance:

| Change | Minimum review concern |
|---|---|
| Typo, link, or clearer non-normative explanation | Documentation accuracy and rendering |
| Upstream version/currentness update | Authoritative source, compatibility, errata, rights, and affected mappings |
| KFM profile field or vocabulary change | Contract, schema, policy, fixtures, validators, producers, consumers, and migration |
| Canonicalization, signing, identity, or digest change | Reproducibility, backward compatibility, verification, receipts, and release lineage |
| Sensitivity, consent, redaction, or privacy change | Qualified policy/privacy/domain review and negative paths |
| Rename, split, merge, or retirement | Directory Rules, inbound references, consumers, alias/tombstone, migration, and rollback |
| Adoption or authority change | Accepted decision path and independent review appropriate to consequence |

Escalate rather than guess when authority, currentness, rights, sensitivity, profile identity, compatibility, or release significance is unclear.

[Back to top](#top)

---

<a id="adjacent-responsibility-roots"></a>

## Adjacent responsibility roots

| Surface | Relationship to this lane |
|---|---|
| [`docs/`](../README.md) | Parent human-readable governance and explanation boundary |
| [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Adopted placement law through ADR-0029 |
| [`docs/adr/`](../adr/README.md) | Decisions that adopt, amend, supersede, or retire KFM profiles |
| [`docs/sources/`](../sources/README.md) | Human source guidance and source-authority context |
| [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) | Unresolved naming, placement, authority, and parity drift |
| [`docs/registers/VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) | Checkable currentness, implementation, and consumer questions |
| [`contracts/`](../../contracts/README.md) | Semantic meaning authority |
| [`schemas/`](../../schemas/README.md) | Machine-shape authority |
| [`policy/`](../../policy/README.md) | Admissibility, rights, sensitivity, access, and release rules |
| [`fixtures/`](../../fixtures/README.md) | Representative positive and negative inputs |
| [`tests/`](../../tests/README.md) | Verification and regression evidence |
| `tools/validators/` | Executable conformance and integrity checks |
| `data/registry/` | Source, dataset, layer, rights, and sensitivity identities |
| `data/receipts/` and `data/proofs/` | Process and proof accountability objects |
| `release/` | Release, correction, withdrawal, and rollback decisions |
| Governed apps and runtime | Producers and consumers; not proven by documentation presence |

[Back to top](#top)

---

<a id="known-drift-and-conflicts"></a>

## Known drift and conflicts

This README records current evidence without deciding authority that belongs elsewhere.

| ID | CONFIRMED observation | Status | Required disposition |
|---|---|---|---|
| `STD-DRIFT-001` | Both `CANONICALIZATION.md` and `canonicalization.md` exist | `CONFLICTED / HOLD` | Compare identity, content, inbound links, generators, and consumers; choose migration only through reviewed authority |
| `STD-DRIFT-002` | Both `IIIF.md` and `iiif.md` exist | `CONFLICTED / HOLD` | Reconcile case-only paths with cross-filesystem migration and compatibility evidence |
| `STD-DRIFT-003` | Both `OAI-PMH.md` and `oai-pmh.md` exist | `CONFLICTED / HOLD` | Reconcile identity, content, links, and consumers |
| `STD-DRIFT-004` | Both `STAC.md` and `stac.md` exist | `CONFLICTED / HOLD` | Determine reference/profile roles before any rename or consolidation |
| `STD-DRIFT-005` | `PROV.md`, `PROV-O.md`, `PROVENANCE.md`, and `PROV/README.md` coexist | `CONFLICTED / NEEDS VERIFICATION` | Define each role, canonical relationship, supersession, and nested-lane need |
| `STD-DRIFT-006` | `PROV/README.md` and `DUO_PROFILE.md` resolve to the same blob `a4283dac33ec9f2c182a8be0cb0d23a3e1ba13e0` at the snapshot | `CONFIRMED byte identity / HOLD` | Inspect semantic intent and history; do not infer which path is wrong or delete either |
| `STD-DRIFT-007` | `STAC-DwC.md`, `STAC_DWC_PROFILE.md`, and `stac-dwc-hybrid.md` coexist | `CONFLICTED / NEEDS VERIFICATION` | Establish reference, profile, and hybrid roles or a governed consolidation plan |
| `STD-DRIFT-008` | `PMTILES.md` and `pmtiles/` both carry PMTiles-related guidance | `NEEDS VERIFICATION` | Document parent/child scope, profile identities, consumers, and edit authority |
| `STD-DRIFT-009` | `STAC_KFM_PROFILE.md` says `STAC_DWC_PROFILE.md` and `EVIDENCE_BUNDLE.md` are not yet authored, although both paths exist | `CONFIRMED stale prose` | Reconcile those statements in a file-specific follow-up against current content and authority |
| `STD-DRIFT-010` | `SENSITIVITY_RUBRIC.md` labels `REDACTION_DETERMINISM.md`, `DP_BUDGETS.md`, and `CONSENT_TOKENS.md` as not yet authored, although all paths exist | `CONFIRMED stale prose` | Reconcile file-specific links and adoption status without upgrading policy authority |
| `STD-DRIFT-011` | The prior README labels all child paths proposed/unverified despite 52 tracked direct entries | `CONFIRMED stale lane inventory` | Corrected by this same-path README update |
| `STD-DRIFT-012` | No dedicated `/docs/standards/` CODEOWNERS rule exists | `CONFIRMED routing gap / NEEDS VERIFICATION` | Decide whether default routing is sufficient; do not invent a steward identity |

These findings are not authority to rename, merge, delete, or adopt any child. Structural work requires its own evidence, migration plan, validation, and rollback.

[Back to top](#top)

---

<a id="change-protocol"></a>

## Change protocol

### Update an existing guidance document

1. Freeze the current path, document ID, status, content digest, upstream authority/version, related KFM authorities, inbound references, and known consumers.
2. Classify the change as editorial, currentness, profile-semantic, policy-significant, structural, or authority-changing.
3. Verify version-sensitive claims from the authoritative upstream issuer.
4. Reconcile contracts, schemas, policy, fixtures, validators, producers, consumers, and releases affected by the claim.
5. Preserve truth labels and explicitly state what remains unverified.
6. Run documentation and profile-specific checks.
7. Record compatibility, correction, and rollback where material.

### Add a new standards/profile document

1. Confirm the need is not served by an existing file, nested lane, generated source, compatibility path, or active proposal.
2. Identify one authority owner and the `docs/standards/` explanatory responsibility.
3. Define stable identity, upstream source, scope, KFM status, bindings, review trigger, and non-effects.
4. Add direct navigation only after path and role are verified.
5. Do not create a second contract, schema, policy, source, proof, or release home.

### Rename, consolidate, split, move, or retire

1. Return `HOLD` until identities, content differences, writers, readers, links, profile URIs, schema IDs, generators, tests, and external consumers are inventoried.
2. Obtain the decision authority required by Directory Rules and affected contracts.
3. Add the canonical target and prevent parallel writes.
4. Use dual-read/single-write or a tombstone only for verified compatibility needs.
5. Repair links, anchors, generated references, imports, fixtures, tests, workflows, manifests, and release references.
6. Prove parity and zero writers/consumers before retirement.
7. Preserve Git history, supersession facts, correction path, and rollback.

Case-only changes must be staged in a way that works across case-insensitive filesystems and does not produce two writable authorities.

[Back to top](#top)

---

<a id="open-verification-backlog"></a>

## Open verification backlog

Priority reflects documentation and trust significance, not authorization to implement.

| Priority | Item | Closure evidence |
|---|---|---|
| P0 | Determine authoritative roles and writable homes for the provenance family | Accepted decision or bounded root/profile contract; content/consumer inventory; migration and rollback if needed |
| P0 | Reconcile sensitivity, consent, redaction, and privacy documents with actual policy authority | Qualified review, canonical policy bindings, negative fixtures, validators, and release obligations |
| P1 | Resolve case-collision families without breaking links or consumers | Path/identity decision, cross-filesystem migration test, aliases/tombstones where needed, link and graph closure |
| P1 | Reconcile STAC reference/profile/DwC/trust-extension relationships | Profile map, contract/schema/policy bindings, producer/consumer tests, version/currentness record |
| P1 | Define PMTiles root/subdirectory ownership and profile identities | Parent/child contract, validators, consumers, correction and rollback |
| P1 | Repair confirmed “not yet authored” statements in selected child files | File-specific review against current paths and adoption state |
| P1 | Classify every child as reference, mapping, KFM profile, operational convention, compatibility document, or lineage | Reviewed inventory with stable IDs and non-effects |
| P1 | Verify upstream versions, locators, terms, licenses, errata, and review triggers | Dated authoritative-source ledger |
| P2 | Map every stronger conformance claim to contracts, schemas, policy, fixtures, validators, workflows, producers, and consumers | Cross-root closure matrix tied to exact revisions |
| P2 | Establish accountable standards stewardship and independent-review triggers | Verified assignments; CODEOWNERS updated only if authorized |
| P2 | Confirm document-registry and documentation-graph coverage for all child identities | Green registry/graph checks plus reviewed deltas |
| P3 | Establish external interoperability exercises for selected profiles | Reproducible exchange packet, independent consumer result, receipt, limitations, and correction path |

[Back to top](#top)

---

<a id="evidence-basis-and-limitations"></a>

## Evidence basis and limitations

### Current-session repository evidence

- `main@cbee7add137b9738b3d123b17d41ac3d44d9745b`;
- prior `docs/standards/README.md` blob `cf1152d04aaf39f7dc01aa00faca211528e5ce0b`;
- exact direct-child listing from the GitHub contents API;
- `PROV/` and `pmtiles/` child listings;
- first-path history showing the lane README on 2026-05-08;
- selected current child headers and content for STAC and sensitivity profiles;
- parent [`docs/README.md`](../README.md);
- adopted Directory Rules and accepted ADR-0029; and
- current `.github/CODEOWNERS`.

### Supplied doctrine and lineage

Attached KFM architecture, pipeline, directory-governance, MapLibre, domain, atlas, and implementation documents reinforce the responsibility-root split, evidence-first posture, public trust membrane, current-session evidence limit, and reversible-change discipline. They are source and design lineage, not substitutes for the current repository observations above.

### Not established by this update

This README does not establish:

- current upstream standard versions, endpoint behavior, licenses, terms, or security posture;
- complete child-document accuracy or adoption;
- canonical profile IDs or namespace choices;
- complete contract/schema/policy/fixture/validator coverage;
- hosted CI or branch-protection significance;
- deployed producers, consumers, APIs, maps, or AI behavior;
- standards compliance certification;
- source activation, evidence closure, rights or sensitivity clearance;
- release, deployment, promotion, or publication; or
- the correct structural disposition of any conflicting path.

[Back to top](#top)

---

<a id="last-evidence-review-and-rollback"></a>

## Last evidence review and rollback

**Evidence review:** 2026-08-14 against `main@cbee7add137b9738b3d123b17d41ac3d44d9745b`.

Re-review this README when:

- direct children are added, renamed, moved, generated, deprecated, or retired;
- an upstream standard, terms, governance, errata, or security posture changes materially;
- a KFM profile is accepted, superseded, or deprecated;
- contract, schema, policy, validator, producer, consumer, or release bindings change;
- CODEOWNERS or accountable stewardship changes;
- a case collision or overlapping profile family is resolved;
- a correction, withdrawal, rollback, or public interoperability incident occurs; or
- documentation validation coverage changes materially.

### Rollback

Before merge, close the pull request and abandon the feature branch.

After merge, revert the documentation commit or restore prior blob:

```text
cf1152d04aaf39f7dc01aa00faca211528e5ce0b
```

Then rerun documentation metadata, link, graph, stale-reference, and changed-area validation. Rollback must not rename, delete, adopt, or alter any child profile.

[Back to top](#top)

---

<a id="status-summary"></a>

## Status summary

**CONFIRMED:** same-path README modernization; adopted `docs/standards/` placement; exact 52-entry direct inventory; selected stale references; current default GitHub review route; no structural or authority transition.

**PARTIAL:** child-document reconciliation, standards/profile classification, upstream currentness, contract/schema/policy/validator binding, producer/consumer evidence, and external interoperability.

**NEEDS VERIFICATION:** accountable standards stewardship, adoption and supersession state, case-collision disposition, specialized sublane ownership, hosted exact-head checks, independent review, and public release conformance.

**NON-EFFECTS:** this README does not adopt a standard or KFM profile; define contract meaning; define machine shape; change policy; activate a source; emit evidence, receipts, proofs, catalogs, or releases; change runtime behavior; deploy; promote; publish; merge; or alter repository settings.

[Back to top](#top)
