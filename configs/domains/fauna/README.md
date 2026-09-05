<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-fauna-readme
title: configs/domains/fauna/ — Governed Fauna Configuration Boundary
type: readme
version: v0.4
status: draft
created: 2026-07-13
updated: 2026-09-04
current_path: configs/domains/fauna/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
owners:
  - "@bartytime4life — CODEOWNERS review route only"
  - "NEEDS VERIFICATION — config, Fauna, taxonomy, source/rights, sensitivity/geoprivacy, consumer, validation, policy, release, and documentation stewards; independent reviewer"
policy_label: "public; config-sublane; fauna; taxonomy-aware; source-role-aware; occurrence-class-aware; sensitivity-aware; geoprivacy-aware; reconstruction-resistant; rights-aware; time-aware; deny-by-default; non-secret; non-authoritative; no-live-binding; no-source-activation; no-exact-sensitive-location; no-release-authority"
truth_posture: >
  CONFIRMED exact README-only tracked subtree, parent configuration contract,
  accepted Directory Rules authority, source-first registry/capture requirements,
  CODEOWNERS routing, executable synthetic test source, and workflow-declared
  validation/proof/release boundaries / PROPOSED future consumer-bound profiles /
  UNKNOWN actual config consumers, precedence, payload validation, policy-runtime
  integration, source activation, runtime, and publication / NEEDS VERIFICATION
  accountable stewardship, independent review, exact physical RAW placement,
  registry writers, compatibility migration, and operational correction/rollback
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  initial_read_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  repin_method: "Commit comparison changes only catalog/triplet/README.md; target blob re-read unchanged. All cited repository inputs retain the inspected bytes."
  base_commit: 700570cbcf191038aa20a030174c2dd08cf93675
  main_tree: f98d5965812e9a29f55d820f9942549719930408
  fauna_config_tree: d681671c5d2cefe14d82d07b283c0ae5899a5f06
  prior_blob: 30504fabf55a008a749eb2b9199c27d0acfac3da
  tracked_blobs_in_target_directory: 1
  tree_truncated: false
  parent_readme_blob: c497e41466f3aaf934aeca4b9976a2fa8516ff21
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  source_registry_parent_blob: b5c31c7fb5334da6f74e9a850f50a208efb7c329
  raw_parent_blob: 560113c00e257725c0a440cb489510af44c13b12
  workflow_blob: ba5eb3cfcdd759fff76b3e7e7c58cba604e29b47
  smoke_test_blob: 8154761e55c01db9133f125f7cf268c2fbb8589e
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - ../README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../data/registry/sources/README.md
  - ../../../data/raw/README.md
  - ../../../.github/workflows/domain-fauna.yml
  - ../../../tests/domains/fauna/test_fauna_smoke.py
  - ../../../CONTRIBUTING.md
tags: [kfm, configs, fauna, taxonomy, source-role, sensitivity, geoprivacy, no-secrets, non-authoritative, governance]
notes:
  - "This revision changes only this README; no executable configuration or consumer is added."
  - "The July v0.3 snapshot remains Git history, not current implementation evidence. Stable document identity, creation date, and existing heading anchors are retained."
  - "Configuration stays README-only; that does not mean the entire Fauna domain is scaffold-only. Test source and workflow declarations are not execution receipts."
  - "The canonical source-registry family is resolved by accepted rules; record nesting, writer/consumer migration, and physical RAW placement are separate unresolved questions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Fauna Domain Configuration

`configs/domains/fauna/`

> Shared, non-secret configuration guidance for Fauna consumers. A profile may reference governed behavior; it cannot create animal truth, source authority, geoprivacy approval, or publication permission.

**Status:** draft `v0.4` · **Local inventory:** README only · **Runtime binding:** unverified · **Sensitive occurrences:** T4 by default.

[Scope](#purpose) · [Current evidence](#status) · [Allowed content](#what-belongs-here) · [Consumer contract](#minimum-configuration-contract) · [Sensitivity](#sensitivity-geoprivacy-and-tier-motion) · [Sources](#connector-and-source-registry-boundaries) · [Validation](#validation) · [Rollback](#rollback-correction-supersession-and-invalidation)

> [!IMPORTANT]
> Inherit the [domain configuration contract](../README.md). This child narrows it for Fauna; it does not establish a loader, an active configuration, an approved source, or a released layer. Missing evidence, rights, sensitivity, policy, review, or release support must not become implicit permission.

> [!CAUTION]
> Exact or reconstructable sensitive occurrences, nests, dens, roosts, hibernacula, spawning/breeding sites, telemetry paths, steward-controlled records, and observer or landowner details fail closed. Hiding a popup, filtering a layer, or lowering opacity is not access control. Protected detail must be withheld or transformed before public delivery.

## Purpose

Keep the Fauna-specific configuration boundary inspectable without copying domain doctrine or policy into configuration. This directory may eventually hold genuinely shared profiles or templates for **named consumers**, covering taxonomy references, occurrence routing, monitoring, ranges, seasonality, public-safe display, freshness, and review routing.

**Directory Rules basis:** accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules](../../../docs/doctrine/directory-rules.md). Section 10.4 makes configuration follow its consumer unless genuinely shared; sections 12 and 16 keep domains inside responsibility roots and use inherited, compact boundary READMEs. A single app's settings belong with that app; declarative pipeline runs belong in `pipeline_specs/`; deployment settings belong in `infra/`; executable admissibility rules belong in `policy/`.

This is a same-path documentation update under `configs/`, not a new authority, source registry, schema, or policy home.

## Authority level

**Implementation-supporting; non-authoritative for truth and governance.**

| Concern | Configuration may do | Configuration must not do |
|---|---|---|
| Taxonomy and status | Reference a versioned, reviewed taxonomy/crosswalk/status profile. | Adjudicate identity, synonymy, merge/split decisions, legal status, or conservation status. |
| Source and evidence | Reference source identities and supported processing profiles. | Admit or activate sources, upgrade source roles, confirm an occurrence, or create evidence closure. |
| Sensitivity and rights | Select accepted policy references and conservative routing. | Change tiers, invent geoprivacy parameters, clear rights, reduce review, or approve disclosure. |
| Consumer behavior | Supply explicitly supported, validated non-secret settings. | Create discovery, precedence, network access, or runtime binding by file presence. |
| Release and public use | Reference an already-governed release/display profile. | Promote, release, publish, or authorize map/API/export/AI access. |

A parsed file, passing validator, signature, manifest name, or familiar provider name does not transfer authority to configuration.

## Status

### Repository snapshot

Evidence below is pinned to `main@700570cbcf191038aa20a030174c2dd08cf93675`, inspected on **2026-09-04**. It is not a continuously refreshed repository inventory.

| Item | Verified value |
|---|---|
| Original target blob | `30504fabf55a008a749eb2b9199c27d0acfac3da` |
| Target directory tree | `d681671c5d2cefe14d82d07b283c0ae5899a5f06` |
| Recursive target-tree result | One tracked blob; `truncated: false` |
| Parent README blob | `c497e41466f3aaf934aeca4b9976a2fa8516ff21` |
| CODEOWNERS route | `/configs/ @bartytime4life`; no narrower matching rule in the inspected file |

```text
configs/domains/fauna/
└── README.md  # Configuration boundary; no tracked payload or child directory
```

This verifies the tracked target subtree only. Ignored files, untracked workstation settings, external stores, and runtime consumers are outside that inventory.

### Evidence ledger

| Evidence at the pinned commit | Supported conclusion | Not established |
|---|---|---|
| Exact target tree and [parent README](../README.md) | This config lane is README-only and inherits a non-secret, non-authoritative boundary. | A loader, consumer binding, or executable Fauna configuration. |
| [Accepted ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and adopted rules | `configs/` ownership, source-first capture identity, and canonical source-registry family are governed. | A newly authorized writer, migration, or source activation. |
| [Source-registry parent](../../../data/registry/sources/README.md) and [RAW parent](../../../data/raw/README.md) | One source identity/capture; parallel domain views are not independent authority. Exact physical RAW placement remains held. | Complete descriptor inventory or live writer/consumer integration. |
| [Fauna domain README](../../../docs/domains/fauna/README.md) | Current domain documentation describes mixed, bounded implementation rather than a greenfield lane. | Uniform maturity of every package, schema, policy, fixture, or route. |
| [Smoke-test source](../../../tests/domains/fauna/test_fauna_smoke.py) | Substantive positive/negative fixture tests and explicit network-call blocking are present in the inspected test source. | A successful test run in this documentation session or production safety. |
| [Domain workflow](../../../.github/workflows/domain-fauna.yml) | `validate-fauna` invokes two synthetic suites. Proof and release-dry-run jobs have explicit readiness holds. | A generic config validator, completed proof production, release rehearsal, or hosted exact-head success. |
| [CODEOWNERS](../../../.github/CODEOWNERS) | Review routing to `@bartytime4life`. | Accepted domain stewardship, required approval, independent review, or review completion. |

### Maturity matrix

| Capability | Truth and maturity boundary |
|---|---|
| Fauna configuration payload | **CONFIRMED absent from the inspected tracked subtree.** |
| Config discovery, precedence, schema binding, and consumer integration | **UNKNOWN.** No such behavior is established by this README. |
| Fauna fixture validation | **CONFIRMED test source and workflow wiring; execution NOT RUN in this revision session.** |
| Domain schema/policy/package coverage | **NEEDS VERIFICATION per file and consumer.** Do not generalize July placeholder observations to the entire current domain. |
| Geoprivacy enforcement and operational invalidation | **NEEDS VERIFICATION.** Doctrine and synthetic tests are not live policy-runtime proof. |
| Source admission, runtime, release, deployment, and publication | **Not established or authorized by this change.** |

The previous v0.3 assertion that `domain-fauna.yml` only echoes TODO messages is superseded by the inspected workflow. The canonical registry **family** is also no longer undecided. Unresolved record layout, writer ownership, physical storage, and migration must remain explicit.

## What belongs here

Small shared defaults, placeholder templates, synthetic examples, and profile references with a named or explicitly proposed consumer. Draft authoring may proceed with disclosed unknowns; **consumer-ready use** requires the binding and validation below.

Profile references can select already-governed taxonomy, source-role mapping, restricted/public routing, freshness, display, review, or invalidation behavior. They must not copy authoritative registry records, policy decisions, contracts, or geoprivacy logic into this directory.

Mutation is reviewable, version-controlled documentation or configuration work. Git history retains prior versions; no source-data retention schedule or permission to store restricted inputs is created here. Do not create files merely to complete a directory pattern.

## What does not belong here

Real occurrence, specimen, survey, telemetry, acoustic, eDNA, mortality, disease, rehabilitation, rescue, invasive-species, or source payloads; protected geometry or private-land joins; observer, landowner, permit-holder, researcher, or other living-person details; restricted media, EXIF, collection details, or steward notes.

Also excluded: credentials, cookies, tokens, signed URLs, private endpoints, connection strings, workstation/deployment bindings, source admission/activation decisions, canonical taxonomy or status records, inline geoprivacy radii or randomization parameters, executable policy, schemas, semantic contracts, authoritative descriptors, receipts, proofs, release decisions, correction notices, and rollback cards.

Do not add connector implementations, automatic directory discovery, or bypass settings such as `skip_review`, `allow_exact`, or `sensitive=false`. A generic `trusted`, `verified`, or `public` flag cannot replace distinct governed decisions.

## Inputs

Before operational use, identify the exact consumer and accountable owners; parser, encoding and format version; supported path and discovery mechanism; contract/schema references; accepted source, taxonomy, occurrence, time, sensitivity, rights and display profiles; no-network posture; precedence and unknown-key behavior; validation/negative cases; logging, migration, deactivation, correction and rollback behavior.

Use synthetic values that cannot be joined back to real taxa/site events, people, parcels, telemetry, facilities, or protected collections. Unknown owners and authority references stay explicit in draft documentation, not fabricated into active payloads.

## Outputs

**Current output: documentation only.** A future validated configuration can support a verified consumer; it cannot issue a `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, `EvidenceBundle`, or `ReleaseManifest` merely by naming one. Nor can it make a range, model, candidate detection, or generalized geometry into an approved occurrence or release.

Public clients use governed APIs and released, public-safe artifacts, never internal configuration as a route to RAW, WORK, QUARANTINE, unpublished candidates, canonical stores, or a direct model runtime.

## Validation

### Documentation validation

Check stable `doc_id` and creation date, one H1, valid metadata, heading/fragment continuity, balanced fences, resolving relative links, truthful source labels, and absence of secrets or protected detail. Compare the exact base/head and changed paths. Report unrun checks and retrieval limits; do not copy old green results forward.

### Existing Fauna test command

The inspected `domain-fauna.yml` declares this command, run **from a complete repository root**:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m unittest --verbose \
  tests.domains.fauna.test_fauna_smoke \
  tests.domains.fauna.test_public_safe_migration_fixture
```

**Verified as workflow source; NOT RUN during this README revision.** It validates bounded synthetic fauna fixtures, not this configuration directory, production geoprivacy, or source rights. The network environment flag is not a universal sandbox: the inspected test source explicitly patches selected network calls.

`build-proof-fauna` and `publish-dry-run-fauna` are readiness/hold checks, not working proof and release producers. A successful hold check is not an `EvidenceBundle`, release approval, or public-use authorization.

### Future payload validation

| Layer | Required behavior before consumer-ready use |
|---|---|
| Parse and shape | Deterministic encoding/parser; supported version; accepted restrictive schema. Empty-permissive scaffolds are insufficient. |
| Binding and precedence | Exact consumer/path; explicit discovery; deterministic overrides; tested missing/stale/incompatible file handling. |
| Unknown keys | Explicit and tested; unknown policy-significant keys must not become permission. |
| Domain semantics | Preserve taxonomy version, source role, observation class, time, spatial support, and uncertainty. |
| Sensitivity and rights | Resolve accepted policy/transform references; deny unsupported exposure; preserve record/media/steward restrictions. |
| Reconstruction and logging | Test joins, counts, identifiers, time, media, vector attributes, previews, logs, errors, caches and exports for disclosure. |
| Correction and rollback | Test deactivation, compatibility, invalidation, restoration, and refusal to reuse withdrawn derivatives. |

No payload-specific validation command is claimed while no payload or consumer binding is verified.

### Required negative cases

| Failure family | Minimum cases |
|---|---|
| Identity and evidence | Unknown/conflicting taxon; unversioned merge/split; duplicate event with conflicting lineage; aggregator upgraded to original authority; missing evidence. |
| Meaning and time | Model/range/habitat/candidate promoted to observation; unsupported absence inference; stale status labeled current; ambiguous or missing observation/valid time. |
| Sensitivity and rights | Restricted record sent to public profile; exact site requested; missing policy/redaction/review/release reference; unresolved rights or embargo. |
| Indirect disclosure | Small-cell counts, stable ID joins, telemetry/time linkage, EXIF/URLs, parcel/facility joins, tile attributes, logs and caches reveal withheld detail. |
| Configuration and migration | Unknown key/version, malformed input, ambiguous precedence, missing rollback, duplicate registry writer, noncanonical authority reference, invalidation failure. |

## Review burden

Request configuration/documentation and Fauna-domain review. For behavior-bearing changes, add the affected consumer, taxonomy, source/rights, sensitivity/geoprivacy, schema/contract, validation, security, policy, release and rollback reviewers; include a steward or rights-holder representative where relevant.

`@bartytime4life` is the verified **routing identity**, not proof that all those responsibilities are assigned or independent. Do not self-certify author/approver separation. Follow the current [contributor guide](../../../CONTRIBUTING.md) and applicable delivery controls; branch authoring is not ready-for-review, merge, release, or publication authority.

## Related folders

### Configuration and doctrine

Use the [parent config README](../README.md) for shared constraints, the [Fauna domain README](../../../docs/domains/fauna/README.md) for domain scope and its linked companions, and [Directory Rules](../../../docs/doctrine/directory-rules.md) with [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) for placement. The accepted ADR, not the retained `PROPOSED_FOR_ADOPTION` label inside the pinned rules bytes, establishes adoption.

### Authority and implementation-shaped surfaces

The Fauna domain index links the responsibility-owning contract, schema, policy, fixture, validator, test, runbook, lifecycle and release families. Recheck those exact owners and consumers before adding a profile; this README is not a duplicate inventory or migration authority.

For the corrected boundaries, start with the [source-registry parent](../../../data/registry/sources/README.md), [Fauna registry child](../../../data/registry/sources/fauna/README.md), [RAW parent](../../../data/raw/README.md), [domain workflow](../../../.github/workflows/domain-fauna.yml), and [smoke-test source](../../../tests/domains/fauna/test_fauna_smoke.py). Older child text cannot override the accepted rules or its current parent.

### Source and coordination lineage

| Source | Role in this revision | Limit |
|---|---|---|
| [Fauna Architecture PDF-Only Report](https://drive.google.com/file/d/1mWhhtubyaAtNuWJ3vY7nuDLx50Wig7Bj/view), 2026-04-21 | Taxonomy/occurrence/range distinctions, sensitivity, geoprivacy, source-role and continuity design. | Its no-mounted-repo finding describes that authoring session. Proposed paths, source terms, and broad build phases are not current implementation or new commissioning. |
| [Drive Directory Rules lineage](https://docs.google.com/document/d/1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs/edit) | Earlier responsibility-root rationale. | Adopted repository rules and ADR-0029 govern current placement; earlier domain-first RAW examples do not. |
| [Notion Fauna coordination](https://app.notion.com/p/3caa92021bf6811b8926dc0010d67672) | Source-first reconciliation and optional Fauna RAW-reference lineage. | Historical main/queue/scheduler observations are not current state. GitHub evidence controls implementation. |

Drive and Notion source material remained read-only during preparation of this revision. No external provider terms, live endpoints, protected records, or production source feeds were verified or retrieved.

## ADRs and drift triggers

This README creates or adopts **no ADR**. Recheck current accepted decisions before changing domain identity, taxonomy adjudication, sensitivity tiers, geoprivacy authority, source writers, schema/contract homes, public access, or release responsibilities. Do not use a configuration change to settle those decisions indirectly.

The source-registry **family** is already canonical under accepted `DIR-SOURCE-003`; the remaining work is exact record layout, writer/consumer ownership, generated-view binding and migration, not a choice between equally authoritative families. Physical RAW placement remains held. A future migration needs an explicit path decision, impact/identity mapping, validation and rollback; this README authorizes no moves or duplicate writers.

## Scope and bounded context

Keep responsibilities separate: `docs/` explains, `contracts/` defines meaning, `schemas/` defines machine shape, `policy/` governs admissibility, `data/registry/` owns identities, implementation roots run consumers, lifecycle lanes hold governed instances, and `release/` records release/correction decisions. This directory supplies shared non-secret configuration only.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed transition, not a file move or a configuration toggle. A public claim follows `EvidenceRef -> EvidenceBundle` and the applicable policy, rights, sensitivity, review, release, correction and rollback checks. Maps, tiles, graphs, indexes, scenes, summaries and AI remain downstream carriers.

## Configuration classes

All classes below are **PROPOSED profile concepts**, not implemented keys or admitted profiles.

| Class | Permitted selection | Boundary |
|---|---|---|
| Taxonomy / source role | Versioned vocabulary, crosswalk, or mapping reference. | No identity adjudication or role upgrade. |
| Occurrence / sensitivity | Restricted, hold, deny, abstain or review routing; accepted sensitivity profile. | No tier reduction or embedded policy. |
| Public-safe display / freshness | Approved field/representation profile and product-specific stale behavior. | No exact-location permission; stale remains visible. |
| Review / invalidation | Required reviewer classes and accepted invalidation behavior. | Cannot remove review or reuse withdrawn outputs. |
| Migration | Declared, bounded compatibility behavior. | No second authority or undocumented key reinterpretation. |

## Minimum configuration contract

Before a future file is consumer-ready, document or carry the following in that consumer's **accepted schema**. This is a design checklist, not a new schema or copy-paste payload.

| Information | Required meaning |
|---|---|
| `config_id`, `config_version`, `domain` | Stable configuration identity/version and canonical `fauna` scope; no aliases created by config. |
| `consumer_id`, `owner_refs`, `format_version` | Exact consumer, accountable owners and supported parser/format version. |
| `contract_ref`, `schema_ref` | Existing semantic and restrictive machine-shape authority. |
| Source, taxonomy and occurrence profile references | Reviewed source identities, versioned taxonomy/crosswalk and method/class handling. |
| Policy, sensitivity, temporal and public-safe profile references | Accepted governing behavior; no copied decisions or invented parameters. |
| `unknown_key_behavior`, `precedence`, `network_posture` | Explicit tested failure/override rules and no network by default. |
| `logging_posture`, `failure_posture` | Sanitized diagnostics and finite reason-coded outcomes. |
| `migration`, `rollback` | Deprecated-key window, deactivation, correction/invalidation, prior version and restoration path. |

## Consumer binding, precedence, and discovery

A directory or filename is not a binding. Verify explicit consumer code or declarative binding, supported version, exact file, parser, schema, precedence, unknown-key behavior, overrides, safe failure, sanitized effective-config auditing and rollback.

No universal precedence order is established here. A future consumer must document and test its own order across embedded defaults, shared profiles and deployment-specific settings. Secret references are a separate concern; secrets must not become a higher-priority policy override. Local, environment or deployment values cannot weaken sensitivity, review, source-role, evidence or release gates. Missing or invalid configuration must not be partially applied or silently open access.

## Fauna object-family boundaries

| Family | Preserve |
|---|---|
| `Taxon`, `TaxonCrosswalk`, `ConservationStatus` | Source-native identity, authority/version, synonym and merge/split lineage; jurisdiction and effective status time. |
| `OccurrenceEvidence`, `OccurrenceRestricted`, `OccurrencePublic` | Source evidence, restricted handling and released public-safe derivative are different objects/states. |
| `RangePolygon`, `SeasonalRange`, `MigrationRoute` | Spatial/temporal support and representation limits; no substitution for observed occurrence or exact telemetry. |
| `SensitiveSite`, `MonitoringEvent` | Protected-site controls and method-specific evidentiary limits. |
| `MortalityObservation`, `DiseaseObservation`, `InvasiveSpeciesRecord` | Observed/reported support, uncertainty, status authority and review limits; no unsupported diagnosis or causation. |
| `RedactionReceipt` and other trust objects | Reference existing governing evidence; configuration does not issue or validate them by naming them. |

These are retained domain concepts, not a claim that every family has an accepted schema, implemented consumer or operational release path.

## Taxonomy identity and status

Preserve original identifiers/names, the authority and vocabulary version, historical synonyms, crosswalks, unresolved conflicts and taxon merge/split history. Display labels must not overwrite source identity. A taxonomy update cannot silently rekey records; review affected caches, indexes, public carriers and cross-domain relations.

Conservation/legal status must retain its original authority, jurisdiction, effective time and supersession. It is not evidence of current presence and cannot become current merely through a cached list or aggregator.

## Source role and evidence character

Original authority, direct observation, access platform/aggregator, context, model/derivative and candidate detection must remain distinguishable. Restricted/steward access is an additional constraint, not an upgrade in factual authority. Preserve original provider, record-level rights, method, time, uncertainty and lineage through aggregation.

Do not flatten those distinctions into `trusted`, `verified`, `authoritative` or `public`. A profile may reference accepted mappings but cannot invent or normalize conflicting role vocabularies silently.

## Occurrence, monitoring, range, and candidate boundaries

Taxonomic identity is not occurrence; range, seasonal range, migration, habitat association, suitability, occupancy, density and distribution models are not direct observations. Non-detection or absence of a record is not species absence unless sampling design and evidence support that inference.

Acoustic, eDNA, telemetry, camera-trap, specimen, survey, checklist, mortality, disease and invasive records keep method-specific semantics. A score, threshold or AI output cannot confirm a candidate. Mortality/disease reports cannot establish diagnosis, prevalence, causation or public-health authority. Habitat owns habitat patches, suitability and assignments; cross-lane links do not transfer Fauna truth. Duplicate resolution preserves competing source records, uncertainty and correction lineage.

## Time, seasonality, freshness, and correction

Distinguish observation time, event interval, reporting/submission, retrieval/ingestion/processing, model issue and valid time, season/life stage, embargo expiry, source freshness, release, and correction/withdrawal/supersession time as applicable. Missing time does not default to current truth.

A status/taxonomy update, embargo expiry, source correction, policy change or release withdrawal triggers governed review of affected products. Expiry alone is not permission to disclose a previously restricted record.

## Spatial support, precision, and reconstruction risk

Retain the support type: exact restricted point/track, generalized point, cell, polygon/range, seasonal area, corridor/route, aggregate, or withheld geometry. Preserve datum/CRS and declared uncertainty where the consumer contract requires them; do not invent precision or present a generalized point as an exact observation.

Reconstruction review includes time plus observer/route history, externally joinable identifiers, media EXIF/filenames/URLs/thumbnails, rare-taxon labels, low-count cells, tile boundaries/zoom/attributes, and parcel/trail/water-body/habitat/facility/collection/landowner joins. It also includes logs, cache keys, analytics, errors, screenshots, support bundles, previews, exports and AI/search indexes. Withhold, deny, hold or apply an accepted generalization profile when safety is unresolved.

## Sensitivity, geoprivacy, and tier motion

Sensitive occurrence defaults to **T4** under Fauna doctrine. Public exact sensitive-occurrence tiles and API responses are denied. The same protection covers nests, dens, roosts, hibernacula, spawning/breeding/staging areas, telemetry clusters and steward-controlled sites.

Configuration cannot lower a tier. A public-safe T1 derivative requires the applicable accepted transform, `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, evidence closure, rights review, release, correction and rollback support. Geoprivacy parameters and approval belong in their owning policy/transform controls, not this directory. Missing, stale, unsupported or incompatible references fail closed.

Transform before public delivery, not through browser-only masking. Retain the derivative's generalization/precision caveat and auditable transform lineage without exposing restricted inputs, inversion clues or secret transform parameters.

## Source rights, attribution, and stewardship

Resolve provider/original source identity, record- and media-level licenses, terms, attribution, redistribution/derivative permissions, commercial/public-use limits, embargo/permit/steward restrictions, access quotas, supported claim families, correction/takedown contact and version/freshness before operational use.

Public accessibility is not redistribution permission. Aggregation does not erase upstream restrictions, private-person concerns, sovereignty or private-land constraints. Unknown rights remain held; a config profile cannot clear them.

## Connector and source-registry boundaries

### Connectors

Source-specific implementations belong in the accepted connector home keyed by a registered source or declared provider grouping. Do not turn the historical `connectors/fauna/` compatibility index into a second implementation hierarchy, or put fetching/authentication/rate-limit logic in configuration.

Source capture identity is **source-first**: one capture may serve multiple domains without duplicated RAW bytes. The [RAW parent](../../../data/raw/README.md) leaves exact physical placement held pending an accepted decision. An optional Fauna reference is not a mandatory hop or an authorized second payload. A connector does not publish.

### Source registry

Accepted `DIR-SOURCE-003` establishes **`data/registry/sources/`** as the canonical machine source-registry family. Existing `data/registry/sources/fauna/` is a child of that family; `data/registry/fauna/sources/` is a parallel view/compatibility candidate, not an independent writer. The older Fauna child still contains pre-adoption uncertainty; follow the adopted rules and [current parent](../../../data/registry/sources/README.md).

This resolves family authority, **not** exact descriptor filenames/nesting, accepted writer, complete source inventory, generated-view binding or consumer migration. Do not infer a new physical record layout, synchronize manual duplicates, choose a convenient divergent copy, or treat a reference as admission. Keep one governed source identity and preserve migration/correction/rollback evidence.

## Logging, telemetry, caches, and derived indexes

Minimize operational output. Never log exact or reconstructable protected geometry, private-person/permit/rehabilitation/collection details, credentials, signed URLs, restricted payload fragments, or sensitive identifiers when a generalized reason code suffices. Effective-config summaries and cache/index keys must be sanitized too.

Source-role/activation, taxonomy/crosswalk, status, sensitivity/transform, embargo, public allowlist, generalization, correction and release changes require scoped invalidation through the responsible consumer. Do not silently reuse stale or withdrawn tiles, reports, exports, graph/search/vector projections or AI summaries. These are rebuildable carriers, not canonical truth.

## Failure behavior

The dispositions below are **required design constraints**, not verified config-runtime behavior or a new shared outcome vocabulary.

| Condition | Safe disposition |
|---|---|
| Valid configuration | Continue only to the next governed check; validation success does not grant publication. |
| Malformed/unsupported input, ambiguous precedence or unknown policy-significant key | Reject or return an error; do not partially apply or fail open. |
| Unresolved identity, source, rights, time, evidence or authority | Hold, abstain or deny under the accepted consumer contract; preserve uncertainty. |
| Exact sensitive exposure, unauthorized tier reduction or bypass | Deny; emit sanitized reasons without revealing protected values. |
| Source outage, incomplete data, stale or withdrawn evidence | Preserve unavailable/partial/stale state; do not fabricate completeness or substitute model language. |
| Duplicate authority, noncanonical binding or unproven invalidation | Hold/error or deny public reuse until the responsible control resolves it. |

`PASS`/`FAIL` describe validation where supported; `HOLD` is a governed work state. Outward runtime responses retain the accepted `ANSWER | ABSTAIN | DENY | ERROR` boundary. None is a substitute for review or release records.

## Governed AI and generated language

AI may summarize released, policy-safe `EvidenceBundle` material, explain caveats, draft review notes, narrow a query or explain abstention. It must not infer hidden sites, reconstruct restricted precision, upgrade authority, adjudicate taxonomy/legal status without evidence, promote candidates, issue review/release decisions or present generated prose as evidence.

A presentation profile cannot grant the model new access. Scope and evidence resolution precede policy/rights/sensitivity/review/release checks and a cited bounded answer or abstention. Public clients must not receive a direct model-to-internal-store path.

## Migration and anti-bypass posture

Before changing a future payload, pin the actual target and consumer; inspect parents, authority references and overlap; preserve source, identity, method and restricted/public distinctions; validate positive/negative and no-network cases; review the full diff for protected clues; and document precedence, stale handling, migration, deactivation, correction, invalidation and rollback.

Do not duplicate canonical contracts/descriptors in config, create a parallel Fauna connector or contract home, claim permissive schemas prove safety, treat held workflows as producers, or smuggle bypass keys into a compatibility migration. Proposed ADRs and old source plans cannot authorize a structural change.

## Rollback, correction, supersession, and invalidation

For this README, retain the prior blob and exact change commit. Before integration, a reviewer may request a branch-local revert; closure or abandonment is a separate authorized action. After integration, use a transparent reviewed revert rather than force-resetting shared history. No automatic revert is implied by a delivery incident.

For a future config correction: deactivate through its verified consumer; retain the faulty version and review evidence; identify affected outputs without leaking protected detail; restore the last known-good version; rerun validation; rebuild/invalidate carriers; and record required correction, withdrawal and rollback objects in their owning homes. Rollback decisions belong in `release/rollback_cards/`; executed rollback/invalidation receipts belong in `data/receipts/rollback/` under adopted rules, not a new config-local proof store.

A Git revert alone does not revoke exposed data, correct released artifacts, clear caches or prove that unauthorized derivatives stopped being served.

## Definition of done for the first payload

- [ ] A real consumer, accountable owners and genuinely shared configuration need are identified; dormant draft assumptions are separated from operational use.
- [ ] Exact file, format/version, parser, discovery, restrictive schema, contract, precedence, overrides and unknown-key handling are verified and tested.
- [ ] Source, taxonomy, occurrence, status, time, spatial support, rights, sensitivity and geoprivacy references resolve without transferring authority to config.
- [ ] Synthetic positive/negative, no-network, secret/privacy and reconstruction checks cover the actual consumer; CI runs substantive checks rather than treating holds as completed production.
- [ ] Review, sanitized diagnostics, cache/index/export invalidation, migration, deactivation, correction and rollback are verified to the required scope.
- [ ] No file presence activates a source, lowers sensitivity, grants public access or replaces evidence/policy/review/release closure.

## Last reviewed

**2026-09-04**, against `main@700570cbcf191038aa20a030174c2dd08cf93675`. Revision `v0.4` preserves the prior document identity and controls, replaces obsolete workflow/maturity and registry-family claims, and consolidates inherited prose. Prior `v0.3` remains recoverable from blob `30504fabf55a008a749eb2b9199c27d0acfac3da` and Git history.

Re-review before the first non-README payload, consumer binding, schema/role/taxonomy change, source writer or physical-placement migration, sensitivity/rights change, workflow graduation, public integration or correction. Re-pin all repository claims then. This revision proves no runtime, deployment, source admission, independent approval or publication readiness.
