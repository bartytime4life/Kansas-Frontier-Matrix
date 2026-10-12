<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-geology-readme
title: configs/domains/geology/ — Governed Geology and Natural Resources Configuration Boundary
type: readme
version: v0.4
status: draft
owners: "NEEDS VERIFICATION — accountable Config, Geology, interpretation, natural-resources, source/rights, subsurface-sensitivity, consumer, validation, policy, release, and documentation stewards"
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; config-sublane; geology; natural-resources; non-secret; non-authoritative; consumer-bound; source-role-aware; resource-anti-collapse; sensitive-location-aware; no-live-binding; no-source-activation; no-release-authority"
current_path: configs/domains/geology/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
scope_id: geology
review_route: "@bartytime4life via /configs/ CODEOWNERS; routing is not accepted stewardship or independent approval"
truth_posture: "CONFIRMED tracked README-only configuration lane, adopted placement law, review routing, and four fixture profiles wired in the inspected workflow source / PROPOSED future consumer-bound configuration / UNKNOWN config loading, production behavior, source admission, policy execution, evidence closure, release, deployment, and publication / NEEDS VERIFICATION exact-head execution, accountable stewardship, consumer dependencies, and unresolved compatibility decisions"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  main_tree: b17f061592f3da0b1903c5252bc1d12437fe3575
  config_lane_tree: 99a4d9278d1f8bad58809e3b9b544e243d939088
  prior_blob: a63c579c397cfae9c96268f7096d0a5a208cb746
  parent_readme_blob: c497e41466f3aaf934aeca4b9976a2fa8516ff21
  root_readme_blob: a800983eac7582a84e9dd82bc7d4baf04f552ad8
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - ../README.md
  - ../../README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../data/registry/sources/geology/README.md
  - ../../../.github/workflows/domain-geology.yml
tags: [kfm, configs, geology, natural-resources, source-role, sensitivity, public-safe-geometry, rights, time, scale, datum, depth, uncertainty, governance]
notes:
  - "Same-path documentation revision. No configuration payload, consumer, contract, schema, policy, registry, test, workflow, source, release, or public artifact changes."
  - "Preserves document identity, creation date, H2 navigation anchors, and the prior safety boundaries while consolidating repeated prose."
  - "Replaces the July TODO-only workflow description with source-verified bounded fixture wiring; workflow source is not a passing execution receipt."
  - "Historical source/path conflicts remain explicit verification work, not permission to create parallel authority."
  - "Drive is read-only planning lineage; Notion is coordination. Neither proves current repository behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Geology and Natural Resources Domain Configuration

`configs/domains/geology/`

> Make configuration inspectable without turning it into geologic truth, source admission, sensitivity policy, or release authority.

**Status:** draft v0.4 · **Owning root:** `configs/` · **Local maturity:** README-only · **Consumer binding:** not established

**Navigate:** [Current evidence](#status) · [Allowed content](#what-belongs-here) · [Consumer contract](#minimum-configuration-contract) · [Resource distinctions](#geology-and-resource-claim-anti-collapse) · [Sensitivity](#sensitivity-public-safe-geometry-and-join-induced-risk) · [Validation](#validation) · [First payload](#definition-of-done-for-the-first-payload) · [Review record](#last-reviewed)

> [!IMPORTANT]
> **Two different maturity statements:** this configuration directory contains only its README at the pinned snapshot. The wider Geology lane has four bounded fixture profiles wired in the inspected workflow: resource-class anti-collapse, announcement-bounded airborne electromagnetic (AEM) campaign, public-safe geometry assessment, and production material-change assessment. Neither statement establishes a configuration loader, a live source, a geometry transform, evidence closure, or publication readiness.

> [!CAUTION]
> Exact or reconstructable private-well, subsurface, resource, infrastructure, operator/parcel, and culturally sensitive details fail closed. A setting cannot turn an occurrence into a deposit, production into reserves, an interpretation into an observation, or a map into evidence.

## Purpose

This lane inherits the [domain configuration contract](../README.md) and the [commit-safe configuration root](../../README.md). It explains the local boundary for future small defaults, templates, examples, and profile references consumed by a named Geology component.

A useful configuration answers **how an already-governed consumer is configured**, not whether a geological, resource, regulatory, operational, or ownership claim is true. Configuration maintainers, domain reviewers, consumer owners, and rights, sensitivity, validation, policy, and release reviewers should use this page alongside the [Geology documentation landing](../../../docs/domains/geology/README.md).

## Authority level

**Configuration-supporting; non-authoritative for meaning, admissibility, evidence, or release.**

| Responsibility | Owning boundary; what config may do |
|---|---|
| Placement | Accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules](../../../docs/doctrine/directory-rules.md). Section 7.2 assigns non-secret defaults and templates to `configs/`; section 16.3 supplies the `BOUNDARY_COMPACT` profile. This revision stays at the existing path. |
| Semantic meaning and identity | `contracts/` owns meaning. Select a verified versioned reference; do not settle object names, aliases, resource classes, identity equivalence, or scientific interpretation here. |
| Machine shape | `schemas/` owns shape. Reference the named consumer's verified schema; do not embed a competing schema or treat a permissive scaffold as production validation. |
| Admissibility | `policy/` owns decision rules. Reference accepted profiles; do not grant rights, lower sensitivity, approve a transform, or override a denial. |
| Sources and evidence | Source-governance and evidence owners retain their responsibilities. Configuration does not create a SourceDescriptor, admit a source, resolve an EvidenceBundle, or accept proof. |
| Release and public delivery | Release decisions and released carriers remain separate. Configuration cannot authorize promotion, map/API/export access, deployment, or publication. |

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed transition, not a file move, config toggle, commit, or workflow pass. Public clients use governed APIs and released public-safe artifacts, never internal/unreleased stores or direct model endpoints.

## Status

### Repository snapshot

All current-repository statements below are bounded to `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`, inspected on **2026-09-04**. Re-pin before subsequent work; the word "current" does not make this snapshot timeless.

```text
configs/domains/geology/
└── README.md    # Configuration boundary; no executable payload
```

The direct directory listing and the inspected tracked `configs/` tree establish one local blob and no child directory. They do not inventory ignored, untracked, mounted, or externally supplied configuration. No root or `configs/`-scoped `AGENTS.md` appeared in those inspected trees.

| Evidence | Bounded finding | Does not establish |
|---|---|---|
| This lane | README-only; prior blob `a63c579c397cfae9c96268f7096d0a5a208cb746`. | A parser, payload, discovery mechanism, loader, precedence rule, or direct consumer. |
| Parent README | v0.6 records a separately pinned child-lane inventory and non-authority contract. | That all child versions remain unchanged after its snapshot. |
| Directory Rules and ADR-0029 | Adopted responsibility-root law; this is an existing `configs/` domain boundary. | Acceptance of every proposed ADR or historical flat-path proposal. |
| CODEOWNERS | `/configs/` routes to `@bartytime4life`. | Accepted scientific stewardship, independent review, required approval, or completed review. |
| Wider Geology documentation | Repository-grounded v1.2 landing distinguishes mixed implementation maturity from release. | Production or public-operation evidence. |
| Geology workflow source | Four named bounded fixture profiles plus schema-link and Python startup-guard checks are wired. | A passing run on this revision or a general end-to-end geology pipeline. |

**Correction to v0.3:** the July claim that the domain workflow only echoes TODO commands is superseded by the inspected executable wiring. Do not replace that old underclaim with an overclaim that the entire Geology domain is operational.

| Profile wired in the inspected workflow | Intended bounded check | Remaining boundary |
|---|---|---|
| Resource class | Synthetic positive/negative cases keep occurrence, deposit, estimate, and related claim roles distinct. | Not a universal classification vocabulary, estimate certification, or reserve determination. |
| AEM campaign | A sparse announcement-bound candidate preserves document-reported planning separately from unknown current campaign state. | No acquisition, processing, inversion, product, or current operational evidence is created. |
| Public-safe geometry | Opaque synthetic references and metadata; rejects coordinate material and exact public geometry. A coherent generalized candidate remains `HOLD`. | No geometry transform, live-rights resolution, receipt creation, or exposure authorization. |
| Production material change | Version-pinned snapshot metadata produces `NO_CHANGE`, `REVIEW`, `HOLD`, or `ERROR`. | No live source request, source activation, lifecycle write, or publication. |

The [pinned workflow source](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/.github/workflows/domain-geology.yml) is the evidence for this wiring inventory. Its source explicitly retains broader semantics, proof, and release holds. Its always-run summary markers are not substitutes for step conclusions and exit codes.

### Truth labels applied

`CONFIRMED` identifies the inspected bytes and wiring. `PROPOSED` identifies future configuration design. `UNKNOWN` covers unobserved consumers and operational behavior. `NEEDS VERIFICATION` marks checkable ownership, execution, rights, and compatibility gaps. Historical `CONFLICTED` items must be reconciled against their current owning records, not repeated as newly verified facts.

No live data, deployment, policy-runtime, source-admission, review-enforcement, or publication audit was performed for this README revision.

## What belongs here

| Material | Conditions |
|---|---|
| Boundary documentation | Explain local responsibility, evidence, limits, review, and correction. |
| Future defaults, templates, or examples | Small, non-secret, versioned, explicitly inert until bound to a named consumer; use synthetic values or verified non-sensitive defaults. Filename patterns are proposals, not implemented payloads. |
| Profile references | Select already-governed vocabulary, parsing, time, datum, uncertainty, display, restriction, cache, or review behavior; authority stays with the referenced owner. |
| Config-specific migration notes | Describe actual key/version/consumer transitions and rollback; do not create another policy, source registry, or release home. |

A reversible inert draft can be authored with clearly labeled unresolved dependencies. It must not be presented as consumer-ready or active. Synthetic examples must not encode recognizable real wells, operators, leases, permits, samples, deposits, mines, facilities, or protected locations.

## What does not belong here

No source maps, borehole or well-log/LAS payloads, cores, samples, observations, production records, resource estimates, permits, leases, title/parcel records, or exact/reconstructable sensitive geometry. No credentials, private keys, cookies, signed URLs, confidential endpoints, workstation-specific paths, or deployment bindings.

Contracts, schemas, normative policy, source registries, EvidenceBundles, receipts, proofs, reviews, release decisions, correction notices, and lifecycle instances stay in their owning responsibility roots. Do not add bypass keys, automatic source discovery, hidden policy overrides, duplicate alias payloads, or presentation settings that conceal role, uncertainty, scale, time, or release state.

## Inputs

Before a file becomes **consumer-ready**, identify the consumer and accountable owner; filename, format, encoding, parser and version; canonical contract/schema/profile references; safe input values; load timing and precedence; finite failure behavior; positive and negative tests; and deactivation, correction, and rollback mechanisms.

For its actual use, the consumer must preserve source and object roles, identity, time, scale, units, datum, depth, uncertainty, rights, sensitivity, cross-domain ownership, evidence support, and review/release state. An input reference does not prove that the referenced decision exists, is current, or permits the requested use.

## Outputs

**Current output: documentation only.** A future validated payload may select conservative behavior for its verified consumer; it cannot mint governing decisions or advance lifecycle state.

**Exposure, mutation, and retention:** this public, versioned README and future commit-safe configuration are reviewable repository material. Accepted domain stewardship is not established by that exposure. Preserve meaningful versions, migration lineage, and rollback references in Git; do not invent a retention period, erase audit history, or copy real protected data here. Any later operational retention rule belongs to its governing contract/policy. A Git revert is not a substitute for incident handling if sensitive information was exposed.

## Scope and bounded context

### Geology-owned configuration topics

Potential consumer topics include bedrock/surficial units, lithology, geologic age, stratigraphy and correlation, contacts and structures, borehole/log/core/sample references, geophysical and geochemical support, cross-sections, hydrostratigraphy, and natural-resource/extraction/reclamation context. This list authorizes neither payload creation by discovery nor operational activation.

### Explicit non-ownership

Hydrology retains water observations and status; Soil retains horizons and soil properties; Hazards retains event and life-safety authority; Agriculture retains agricultural records; Infrastructure and Roads retain built-system claims; People/DNA/Land retains personal and ownership records; Archaeology and relevant stewards retain archaeological/cultural authority. Paleontological, cave, environmental, or regulatory questions require their actual accountable authority rather than an invented Geology permission.

Joins preserve each lane's evidence, source role, time, precision, rights, sensitivity, review, and release constraints. Hydrostratigraphic context is not a water measurement, and geology is not title, engineering-safety, or regulatory approval.

## Configuration classes

| Class | May select | Must not decide |
|---|---|---|
| Parsing and discovery | Verified parser, format version, explicit allowed filenames. | Meaning, authority, or activation by directory presence. |
| Vocabulary and roles | Versioned object/source/resource profiles. | Silent aliasing or stronger claim-class fallbacks. |
| Time, space, and measurement | Accepted freshness, unit, CRS, datum, depth, and uncertainty profiles. | Missing semantics, unsupported conversions, or apparent precision. |
| Sensitivity and rights | Accepted restriction/review/profile references. | Permission, rights clearance, generalization parameters, or lower restrictions. |
| Rendering, caching, and migration | Caveats, display order, accepted invalidation rules, compatibility windows. | Evidence/release state, hidden uncertainty, stale-data persistence, or parallel authority. |

## Minimum configuration contract

These are **requirements for a future design**, not a declared schema or invented set of accepted keys.

| Concern | Required declaration or reference |
|---|---|
| Identity and responsibility | Config identity/version, `geology` scope, exact consumer, accountable owner and review route. |
| Meaning and shape | Canonical semantic contract, restrictive schema, accepted profile versions, and migration/alias mapping. |
| Parsing | Filename, media type, encoding, parser/version, duplicate-key and unknown-key handling. |
| Binding | Required/optional status, load timing, explicit discovery, reload/cache behavior, deterministic override order. |
| Scientific support | Object/source role, classification, time, method, units, scale, resolution, datum, depth, precision, and uncertainty appropriate to the consumer. |
| Governed use | Rights, sensitivity, policy, evidence, review, release, and correction references checked by their owners. |
| Failure and security | Finite reason codes, no partial unsafe application, no network by default, safe logging, and rejection of bypass settings. |
| Change and recovery | Compatible versions, deprecation window, safe disabled state, rollback target, affected-output assessment, and invalidation. |

Do not insert schema-invalid placeholders into machine-parsed files. Keep unresolved owner/profile/authority questions in documentation until the actual contract provides valid values or sentinels.

## Consumer binding, precedence, and discovery

No generic loader or precedence order is established. Bind a future file explicitly to its parser and consumer; test missing, malformed, duplicate-key, unknown-key, unsupported-version, optional-file, reload, and ambiguous-precedence cases. Fail without partial unsafe application.

A possible order such as compiled safe defaults, reviewed repository settings, reviewed deployment settings, and narrowly scoped runtime inputs remains **PROPOSED** until the named consumer specifies and tests it. Higher precedence never grants permission to weaken policy, rights, sensitivity, evidence, review, or release constraints.

Use allowlisted discovery, not "load everything under this directory." Local files, environment variables, alternate filenames, extension changes, and runtime flags must not evade the same contract. Deployment-only values are supplied through their proper controlled boundary, not committed here.

## Geology object-family boundaries

### Foundational geology

Keep `GeologicUnit`, `SurficialUnit`, `Lithology`, `GeologicAge`, `StratigraphicInterval`, structure/fault features, `CrossSection`, and `GeologyBoundaryVersion` distinct. A name match or spatial overlap does not prove correlation, equivalence, or identity.

### Subsurface references and observations

Borehole and well-log references, cores, samples, geophysical observations, and geochemical support describe different evidence. A borehole coordinate does not prove that a log, core, sample, interval, or interpretation exists.

### Natural-resource and operational context

Preserve `MineralOccurrence`, `ResourceDeposit`, `ResourceEstimate`, `ExtractionSite`, and `ReclamationRecord`, with administrative and production context explicitly separated.

### Cross-domain context

`HydrostratigraphicUnit` may provide Geology context without taking ownership of Hydrology observations.

The prior roster includes short versus `Reference`, `StructureFeature` versus `FaultStructure`, and CamelCase versus snake_case variants. This page does not normalize them. Resolve the exact accepted vocabulary, version, and identity mapping for the consumer; hold ambiguous input rather than silently aliasing or emitting duplicate objects.

## Observation, interpretation, model, and aggregate boundaries

| Evidence character | Preserve | Never upgrade to |
|---|---|---|
| Measured or observed | Method, instrument/laboratory, collection time, location support, units, uncertainty, source and corrections. | Universal or timeless truth. |
| Mapped interpretation | Map edition, author/publisher, scale, boundary confidence, method and evidence. | Direct measurement or exact subsurface fact. |
| Cross-section or model | Producing process, input evidence, version, section/volume support, assumptions, resolution, validation scope and uncertainty. | Actual observed conditions between samples, regulatory finding, or engineering suitability. |
| Aggregate | Spatial/reporting unit, period, coverage, suppression and upstream roles. | Individual site/well/operation evidence. |
| Candidate or synthetic | Unconfirmed or synthetic status and applicable review boundary. | Confirmed real-world observation or released truth. |

Rendering, ranking, interpolation, inversion, repetition, or AI generation does not strengthen the source role.

## Geology and resource-claim anti-collapse

| Claim class | Required distinction |
|---|---|
| Occurrence | An indication or documented presence does not establish a delineated deposit, quantity, economics, permit, production, or reserve. |
| Deposit | A characterized body does not by itself establish an estimate, economic viability, recoverability, or operating permission. |
| Estimate | Preserve method, date, assumptions, standard/classification, confidence, authority, and source support; not observation or automatic reserve status. |
| Permit | Administrative application/authorization state; not physical geology, production, compliance, ownership, or reserves. |
| Production | Reported output for its period and reporting scope; not reserves, future output, title, compliance, or proof of a deposit classification. |
| Reserve | Requires its own supported classification, date, assumptions, and authority; never infer it from occurrence, deposits, permits, or production. |
| Extraction site | Site association does not prove present operation, owner, compliance, quantity, or legal status. |
| Reclamation record | A plan, status, inspection, or observation does not automatically certify completion, closure, compliance, or absence of liability. |

Do not collapse these into a generic `resource` truth field or choose a stronger class as fallback. Operator, lease, parcel, and ownership are not interchangeable. Regulatory, operational, and physical claims require distinct supporting evidence.

## Time, vintage, freshness, and correction

Keep material time kinds separate: source publication/edition; drilling, logging, survey, collection and analysis; interpretation/model creation; valid interval; permit application/issuance/amendment/suspension/expiration/revocation; production reporting period; retrieval/ingestion; release; correction/supersession/withdrawal/rollback.

Historical maps and logs retain their edition, scale, and limitations. Retrieval does not make an old source current; an announcement does not prove current campaign activity; a permit does not prove production; a model does not rewrite an observation. Preserve stale, partial, provisional, embargoed, corrected, withdrawn, and superseded states. A freshness selector cannot suppress them.

## Spatial support, scale, depth, datum, and uncertainty

### Required spatial semantics

Preserve horizontal CRS and axis order, vertical datum/elevation reference, depth reference and zero/sign convention, measured versus true vertical depth where applicable, units, dimensionality, geometry/topology, map scale, grid resolution or survey spacing, horizontal/vertical uncertainty, source versus generalized precision, and derivation method. Cross-sections also require section support and vertical exaggeration.

Geochemical or analytical consumers additionally preserve analyte, method, laboratory/instrument lineage, detection limits, and applicable confidence or quality flags. Conversion rules require supported input semantics and tests; do not guess missing units or datums.

### Non-equivalences

A map-unit polygon is not exact contact geometry; a generalized point is not its source location; a grid cell is not a point observation; a regional aggregate is not a facility; depth below ground is not elevation above datum. Zoom, extrusion, interpolation, or a smoother scene does not add accuracy or subsurface evidence.

Unknown or incompatible support produces a bounded hold, abstention, or error through the actual consumer contract, not silent coercion.

## Sensitivity, public-safe geometry, and join-induced risk

### Fail-closed material

Exact or reverse-engineerable private wells, boreholes, logs, cores, samples, geophysical/geochemical observations, exploration targets, sensitive resources, mines/quarries, processing/storage/injection/transport infrastructure, proprietary/embargoed material, and cultural/archaeological/cave/fossil context require applicable rights, sensitivity, and consequence-appropriate review.

### Public-safe outcomes

Configuration may reference an accepted withheld, suppressed, generalized, aggregated, delayed, restricted-view, or denial profile. It does not define a radius, cell size, zoom limit, jitter, buffer, delay, minimum count, sensitivity tier, or authority to expose exact data.

Public-safe use requires supported identity, rights, sensitivity, validation, provenance, integrity, transform lineage, receipts/proofs, policy, review, release state, correction, and rollback as applicable. The existing metadata-assessment profile is not a transform implementation or release decision. Hidden layers, omitted popups, low opacity, URL suppression, and client-side masking are not access controls.

### Join-induced sensitivity

Preserve the strongest applicable restriction when combining resource/well/sample records with operator, permit, lease, parcel, title, address, PLSS, imagery, route, infrastructure, or cultural context. Low-count aggregates, descriptions, cross-sections, and model extents may permit reconstruction even when one geometry is generalized.

Review the combined output, not just each input. A released input or successful transform does not automatically authorize a new join or derivative.

## Source rights, attribution, and regulatory boundaries

Retain originating publisher, source identity/version, claim-relative role, attribution, access/automation terms, redistribution/derivative/commercial limits, record restrictions, embargoes, and correction lineage. Public accessibility, a successful fetch, or a source label does not establish permission.

Keep KGS/KCC/USGS and other source-family references claim-relative: maps, regulatory filings, production compilations, catalogs, and operator reports do not acquire each other's authority. The older WWC5, MRDS, portal, endpoint, and source-vintage notes are research/lineage inputs, not current source-admission or rights determinations. Reverify source-specific facts before live use.

Unknown rights block higher-risk use; configuration cannot clear them or substitute for scientific, regulatory, ownership, or engineering review.

## Connector, source-registry, and watcher boundaries

### Source-first connector placement

Source acquisition belongs to its reviewed source/source-family boundary under `connectors/`, not to a new domain-first implementation hierarchy. A compatibility index or historical KGS/KSGS/product alias does not justify a second client, credential store, cache, writer, or activation path.

### Source-registry topology

The [Geology source-registry README](../../../data/registry/sources/geology/README.md) still declares a parallel domain-first source lane and final-topology verification work. This revision confirms that declaration, not an exhaustive current descriptor inventory or migration-completion audit. The historical `data/registry/geology/sources/` route must not become a divergent config-controlled registry.

Use the source owner's verified identity and canonical-resolution rules. Directory existence, an alias name, or a convenient path is not authority.

### Watchers and scheduled consumers

Watchers may detect change and propose candidates, diagnostics, receipts, and review requests within their authority. They do not silently accept geology claims, activate sources, mutate canonical records, promote, or publish. No schedule, connector, network request, or watcher is enabled by this README.

## Cross-sections, 3D scenes, and renderer boundaries

Sections, profiles, block/fence diagrams, volumes, terrain, tiles, and scenes are carriers. Preserve author/process, evidence references, section/volume support, horizontal/vertical scale, exaggeration, datum/depth, method, version, uncertainty, unsupported zones, source vintage, public-safe state, and release/correction lineage.

Display configuration may control accepted styling and visible caveats; it cannot infer contacts, hide uncertainty, change claim role, or assert actual subsurface conditions. Keep synthetic/interpretive reality-boundary notes visible. Renderer selection, dependency admission, browser readiness, and public-layer release remain separate decisions; this page admits none.

## Logging, telemetry, caches, and derived indexes

Do not log protected coordinates or depth/location combinations, real well/sample/operator/parcel/lease identifiers, private endpoints, signed URLs, proprietary values, sensitive bounds/section lines, or unnecessary full policy inputs. Prefer config/consumer version, digest, profile identifiers, safe reason codes, redacted references, and cache-generation/invalidation state.

Rights changes, sensitivity escalation, correction, withdrawal, source supersession, policy change, and rollback must reach affected caches, search/vector indexes, tiles, generalized derivatives, cross-sections/scenes, exports, tracked screenshots/reports, and generated-answer caches. Logging and caching are disclosure surfaces, not exceptions to the public boundary.

## Validation

### Documentation validation

For a README-only change, verify the exact base/target blob and allowed diff; metadata identity; one H1; section/fragment compatibility; balanced fenced blocks; resolving repository destinations; absence of conflict markers, trailing whitespace, secrets, real sensitive payloads, and unsupported maturity claims. Review authority, source-role, geometry, and release language as content, not just syntax.

The revision must not label unexecuted tests, inherited checks, source listings, static badges, or workflow-summary markers as passing results. Use the [contributor contract](../../../CONTRIBUTING.md) for proportional changed-area validation and failure attribution.

### Future payload validation

Test parser/schema conformance, binding and explicit discovery, duplicate/unknown keys, deterministic precedence and reload, role/identity preservation, time/scale/unit/datum/depth semantics, rights and sensitivity references, cross-domain joins, no-network behavior, safe logging, deactivation, migration, correction, and rollback. A permissive placeholder schema cannot establish readiness.

The following **existing workflow commands are reference commands for a prepared checkout**, not a receipt that they ran during this documentation revision:

```bash
# Run from repository root after the repository-approved test dependencies exist.
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
export KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0

python -m pytest -q -p no:cacheprovider \
  tests/validators/domains/geology/test_schema_contract_doc_links.py \
  tests/domains/geology/test_public_safe_geometry.py \
  tests/domains/geology/test_production_material_change.py
python tests/domains/geology/test_source_role_anti_collapse.py --verbose
python tests/domains/geology/test_aem_campaign.py --verbose
python tools/validators/geology/public_safe_geometry/validate_public_safe_geometry.py --fixtures
```

These commands are a bounded subset of [the workflow](../../../.github/workflows/domain-geology.yml), not a substitute for its full positive/negative CLI checks, startup-guard proof, readiness inventory, or future config-specific tests. No `make geology-validate` or `make validate-geology` target is established here. The Python guard's proof does not cover dependency installation, all native extensions, non-Python processes, or operating-system-wide egress.

### Minimum negative cases

Cover resource-class upgrades; estimate-as-observation/reserve; operator-as-owner; model/interpretation/aggregate-as-observation; ambiguous aliases; malformed/unsupported/duplicate/unknown keys; unverified source role or rights; sensitive exact geometry and reconstruction joins; missing time, scale, method, datum, depth, unit or uncertainty; stale/embargoed/withdrawn/corrected input; unauthorized policy overrides; missing rollback; and failed derivative invalidation.

There is no executable configuration payload to validate in this lane at the snapshot. Wider Geology tests remain relevant supporting evidence but cannot prove a nonexistent config binding.

## Failure behavior

The future consumer must define and test its finite reason-coded outcomes. Do not treat the names below as a newly accepted universal enum.

| Condition | Required safe behavior |
|---|---|
| Malformed, duplicate-key, unsupported, or schema-invalid input | Reject without partial unsafe application; report the consumer's validation failure/error. |
| Ambiguous identity, alias, role, datum, units, support, or precedence | Hold or error; never guess or silently upgrade. |
| Missing rights, policy, evidence, review, or release support | Hold, deny, or abstain at the applicable transition; do not infer permission. |
| Resource-role collapse or exact restricted public geometry | Reject/deny; preserve the original role and restriction. |
| Source outage, stale/partial input, or missing evidence | Preserve limits and abstain where support is insufficient; no replacement by a model or misleading cache. |
| Correction/withdrawal cannot invalidate output | Disable affected exposure and report an error with safe diagnostics. |

Internal validation `PASS`/`FAIL`, a profile's `NO_CHANGE`/`REVIEW`/`HOLD`/`ERROR`, and runtime `ANSWER`/`ABSTAIN`/`DENY`/`ERROR` answer different questions. None is by itself a release decision.

## Review burden

[CODEOWNERS](../../../.github/CODEOWNERS) routes this path through `/configs/` to `@bartytime4life`. That is routing only. Accountable Geology/configuration stewardship, required independent approval, and completed review remain separate evidence.

A documentation change needs configuration/documentation and Geology boundary review. A consumer-bound payload additionally needs the applicable consumer, semantic/schema, stratigraphy/interpretation, source/rights, resource/regulatory, subsurface/infrastructure, public-safe geometry, validation, security, policy, and release reviewers. Cross-domain joins require their owning reviewers. Unverified role names are not invented teams or approvals.

## Governed AI and generated interpretation

The governed sequence is scope and claim role, admissible evidence, `EvidenceRef -> EvidenceBundle`, then applicable policy, rights, sensitivity, review, and release checks before a bounded cited answer or abstention. Preserve source role, edition/vintage, time, scale, units, datum, depth, method, uncertainty, and correction state.

AI may interpret admissible material and propose reviewable work. It cannot approve itself, establish geology/resource/title/compliance/engineering truth, fill unsupported observations, downgrade sensitivity, or publish. Applicable AI/citation receipts record activity; they are not evidence truth or release approval. Public AI uses the governed public path, not direct model or internal-store access.

## Migration and anti-bypass posture

Consumer keys, filenames, formats, aliases, accepted vocabulary, source routing, and release-family references require explicit compatible transitions. Record old/new identifiers and paths, decision authority, consumer impact, version/identity mapping, compatibility window, validation, correction, and rollback. Preserve single-write authority and necessary bounded compatibility reads.

Do not use configuration to settle the historical flat/domain contract/schema forms, KGS/KSGS connector aliases, source-registry dual topology, or singular/plural manifest questions. Re-read current governing ADRs and owning records for the exact affected family; historical conflict notes are neither adoption nor permission to duplicate it.

No `allow_exact_geometry`, `skip_policy`, `trust_model`, `assume_production`, `prefer_latest`, or equivalent bypass, including through local files, environment variables, aliases, or alternate filenames. Configurations cannot create direct public access to canonical/source stores.

## Rollback, correction, supersession, and invalidation

For this README-only revision, preserve the prior blob recorded in metadata. Before integration, abandon or revert the isolated branch change; if a PR exists, close it without merging when appropriate. After any later authorized integration, use a transparent revert/forward-fix PR rather than rewriting shared history.

For future operational configuration: disable the affected binding; stop only dependent processes; preserve the faulty version and incident evidence; identify affected claims, objects, joins and consumers; assess semantic misclassification and disclosure; restore the prior known-good or safe disabled state; rerun relevant positive/negative checks; and issue required correction/withdrawal/review/release/rollback records through their owners.

Invalidate and verify affected caches, indexes, tiles, sections, scenes, exports, reports, and answer caches. A Git revert alone does not retract exposed information, revoke releases, correct public claims, or establish rollback completion.

## Related folders

| Start here | Use |
|---|---|
| [Domain configuration parent](../README.md) and [configuration root](../../README.md) | Inherited commit-safe contract and configuration ownership. |
| [Geology documentation](../../../docs/domains/geology/README.md) | Domain vocabulary, related contracts/schemas/policy/fixtures/tests, lifecycle and release navigation. |
| [Geology canonical-paths document](../../../docs/domains/geology/CANONICAL_PATHS.md) | Historical draft lane map; its no-repo/placement-uncertainty language is not current authority. Reconcile against adopted Directory Rules. |
| [Geology source registry](../../../data/registry/sources/geology/README.md) | Source-role, restricted-registry, and unresolved topology boundary; not public client data access. |
| [Geology workflow](../../../.github/workflows/domain-geology.yml) | Exact commands, fixture-profile scope, and broader proof/release holds. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopted placement authority and compatibility discipline. |
| [Contributor contract](../../../CONTRIBUTING.md) and [CODEOWNERS](../../../.github/CODEOWNERS) | Reviewable delivery, proportional validation, failure attribution, and routing. |

Related families remain in their responsibility roots: Geology semantic contracts under `contracts/`, machine shapes under `schemas/`, decision rules under `policy/`, test inputs under `fixtures/`, executable checks under `tests/` and `tools/`, lifecycle/accountability instances under `data/`, and release/correction decisions under `release/`. Follow the owning document before selecting an exact subpath; this index is not a new registry.

## ADRs and drift triggers

No ADR, root, domain slug, policy, or migration is introduced. Placement follows accepted Directory Rules section 7.2 and the existing parent boundaries; the directory map follows sections 16.3–16.4. Compatibility and migration remain subject to sections 17–18.

Re-review on a first payload or consumer; parser/precedence/unknown-key changes; accepted vocabulary or path migration; source-role/rights/sensitivity changes; new cross-domain joins; transform or exposure changes; validator/workflow/review-routing changes; and corrections, withdrawals, or rollback. Record material newly verified drift through the existing governance process rather than silently resolving it in configuration.

## Definition of done for the first payload

**Inert authoring is not activation.** A synthetic, disabled, reviewable proposal may be drafted while non-safety dependencies remain explicitly unresolved. Consumer readiness and public use require their own evidence.

- [ ] A named consumer, accountable owner, canonical references, format/parser/version, binding, discovery, precedence, and failure behavior are established.
- [ ] Applicable source/object/resource roles, identity, time, spatial/measurement support, rights, sensitivity, and cross-domain constraints are preserved without invented defaults.
- [ ] Positive and negative parsing/schema/binding/semantic/no-network/logging/migration/rollback tests run on the exact change; failures and unrun checks are reported accurately.
- [ ] Accepted policy/profile references resolve for the intended operation; public-safe parameters come from the appropriate owner, not this config.
- [ ] Deactivation, correction, invalidation, and rollback are defined and tested; no source or watcher activates by presence.
- [ ] Any live or public transition separately satisfies source admission, evidence/provenance/integrity, rights/sensitivity, policy, review, proof, release, correction, and rollback gates.

## Last reviewed

**2026-09-04**, against `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`. This edition preserves the original `doc_id`, `created` date, and prior H2 navigation anchors; it changes only this README.

**Evidence roles:** GitHub source reads establish the exact tracked lane, parent/authority bytes, routing, and bounded workflow wiring. A bounded exact-path search found no direct executable config consumer; this is not a universal loader-discovery proof. The parent index's older child-version table and commit-pinned historical source receipts remain historical snapshots, not files to rewrite simply because this child advances.

**Read-only source lineage:** [Directory Rules in Drive](https://docs.google.com/document/d/1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs/edit) supplies historical responsibility-root context; adopted GitHub bytes control placement. The [2026-04-21 Geology architecture report](https://drive.google.com/file/d/1kxONABD4knMG1HYaJR740tzZ_EBrt7Ca/view), especially sections 1–2 and 6–8, preserves scope and anti-collapse planning. Its no-mounted-repository finding belongs to that report's session and is not the current repository state. The [Notion Geology builder page](https://app.notion.com/p/3caa92021bf6811dbb8acb7ac64d0efd) supplies coordination and historical handoff, not present scheduler, implementation, approval, or release proof.

**Open verification:** accountable stewards and independent review; exact-head native test/hosted CI results; future config loader and consumer-specific schema; live source rights/admission; policy-runtime and real transform integration; current compatibility resolution for an actual affected object family; evidence/proof/release closure; and deployed correction/rollback behavior. This documentation update closes none of those operational gates by prose alone.

[Back to top](#top)
