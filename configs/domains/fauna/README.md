<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-fauna-readme
title: configs/domains/fauna/ — Governed Fauna Configuration Boundary
type: readme
version: v0.4
status: draft
owners:
  - "@bartytime4life — CODEOWNERS review route only"
  - "NEEDS VERIFICATION — configuration, Fauna, taxonomy, source/rights, sensitivity/geoprivacy, consumer, validation, policy, release, and independent review assignments"
created: 2026-07-13
updated: 2026-09-04
owning_root: configs/
responsibility: Shared non-secret Fauna configuration guidance; reference authority without duplicating it
current_path: configs/domains/fauna/README.md
policy_label: "public; config-sublane; fauna; non-secret; non-authoritative; no-live-binding; no-source-activation; no-exact-sensitive-location; no-release-authority"
truth_posture: >
  CONFIRMED exact tracked README-only config directory, accepted Directory Rules,
  source-first registry-family authority, CODEOWNERS routing, inspected workflow
  commands, and closed draft OccurrenceEvidence schema / PROPOSED future
  consumer-bound configuration / UNKNOWN loader, precedence, runtime use,
  source activation, policy integration, independent review, and publication /
  NEEDS VERIFICATION exact-head execution and physical writer/consumer migration
  closure; broader Fauna maturity is file-specific, not uniformly scaffold-only.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  initial_read_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  repin_basis: Exact compare to the base changed only catalog/triplet/README.md; all inspected inputs unchanged
  base_commit: 700570cbcf191038aa20a030174c2dd08cf93675
  main_tree: f98d5965812e9a29f55d820f9942549719930408
  prior_blob: 30504fabf55a008a749eb2b9199c27d0acfac3da
  inventory_scope: Exact tracked configs/domains/fauna directory; README.md only, no child directories
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - ../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/fauna/README.md
  - ../../../data/registry/sources/README.md
  - ../../../data/registry/sources/fauna/README.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-fauna.yml
  - ../../../.github/workflows/fauna-occurrence-evidence.yml
  - ../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
tags: [kfm, configs, fauna, taxonomy, source-role, occurrence, geoprivacy, rights, time, no-secrets, governance]
notes:
  - "Same-path README revision; no configuration payload, loader, schema, policy, source, workflow, or release object changes."
  - "v0.3 and its 2026-07-14 checkpoint remain Git history. v0.4 corrects blanket scaffold/TODO claims and distinguishes accepted registry-family authority from unresolved migration."
  - "Directory Rules retain their original draft label inside the exact bytes adopted by accepted ADR-0029. This README neither edits those bytes nor adopts another ADR."
  - "Shared configuration belongs in configs; app-only settings, pipeline specifications, infrastructure settings, and policy retain their own responsibility owners."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Fauna Domain Configuration

`configs/domains/fauna/` makes shared, non-secret Fauna configuration choices inspectable. It does not decide animal truth, taxonomic identity, source admission, geoprivacy, policy, review, or release.

**Status:** draft `v0.4` · **Config inventory:** README-only · **Owning root:** `configs/` · **Review route:** `@bartytime4life` via CODEOWNERS, not verified independent stewardship.

**Start here:** [Status](#status) · [Permitted content](#what-belongs-here) · [Consumer binding](#consumer-binding-precedence-and-discovery) · [Source boundaries](#connector-and-source-registry-boundaries) · [Validation](#validation) · [First payload](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> The configuration lane remains README-only; the broader Fauna domain does **not** remain uniformly placeholder-only. Inspected workflow sources invoke bounded synthetic tests, and the OccurrenceEvidence schema has a closed draft shape. Neither observation proves a configuration loader, a passing run, accepted policy, live source use, or public readiness.

> [!CAUTION]
> Sensitive occurrences default to **T4** under Fauna doctrine. Exact or reconstructable nests, dens, roosts, hibernacula, spawning/breeding sites, telemetry paths, private-land clues, and observer or steward details fail closed. Hiding a layer or popup is not redaction. Configuration cannot lower sensitivity or grant exposure.

## Purpose

This is the contributor-facing boundary for shared Fauna defaults, templates, examples, and profile references. It inherits the [parent domain-configuration contract](../README.md) rather than creating another domain architecture or authority register.

A useful configuration file identifies the consumer, configurable behavior, authority references, validation, failure handling, and rollback. Directory completeness alone is not a reason to add a payload.

## Authority level

**Implementation-supporting; non-authoritative for evidence and governance.** Placement follows [Directory Rules](../../../docs/doctrine/directory-rules.md) §10.4 and §12, as adopted by [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

Configuration follows its consumer unless genuinely shared. App-only settings belong with the app; declarative run definitions belong in `pipeline_specs/`; deployment settings belong in `infra/`; admissibility rules belong in `policy/`; secrets remain outside Git. This existing shared lane is not a license to centralize every Fauna-related setting.

| Responsibility | Configuration may do | Configuration cannot do |
|---|---|---|
| Consumer behavior | Select a supported, validated profile for an explicitly bound consumer | Establish a loader or precedence rule by filename alone |
| Meaning and shape | Reference semantic contracts and machine schemas | Create a competing contract or schema authority |
| Taxonomy and evidence | Reference reviewed identities and evidence | Adjudicate synonyms, confirm occurrences, or manufacture evidence |
| Sources and rights | Reference canonical source identity and reviewed permissions | Admit/activate a source or upgrade its role or rights |
| Sensitivity and policy | Reference an accepted policy/transform profile | Define geoprivacy parameters, approve a transform, or weaken controls |
| Review and release | Carry references needed by the consumer | Substitute for review, promotion, release, correction, or publication |

A valid configuration is not a valid claim, approved source, public-safe derivative, or release.

## Status

### Repository snapshot

| Field | Inspected value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Evidence base | `main@700570cbcf191038aa20a030174c2dd08cf93675` |
| Main tree | `f98d5965812e9a29f55d820f9942549719930408` |
| Prior target blob | `30504fabf55a008a749eb2b9199c27d0acfac3da` |
| Exact tracked config directory | One file, `README.md`; no child directories |
| Scope not observed | Ignored, untracked, generated-outside-Git, workstation, or external configuration |

```text
configs/domains/fauna/
└── README.md
```

This snapshot is immutable evidence, not a promise that `main` will remain unchanged. Parent and companion documents retain their own dated checkpoints; those internal dates are not upgraded by reading their current bytes.

### Evidence ledger

| Inspected source | Bounded finding | Limit |
|---|---|---|
| [Parent configuration README](../README.md), `v0.6` | Non-secret, non-authoritative shared domain configuration boundary | No generic discovery, loading, or precedence implementation established |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Exact rules bytes adopted; responsibility and source-first identity rules apply | The rules' internal draft label is retained; no new adoption or migration occurs here |
| [Fauna domain README](../../../docs/domains/fauna/README.md), `v1.2.3` | Mixed maturity, sensitive-location controls, optional Fauna RAW reference, and bounded implementation navigation | Its historical counts and prior test results are not new execution evidence |
| [Source registry parent](../../../data/registry/sources/README.md), `v1.2` | `data/registry/sources/` is the canonical source-registry family | Exact writer, authoritative record inventory, consumer migration, and physical RAW placement remain unresolved |
| [domain-fauna workflow](../../../.github/workflows/domain-fauna.yml), blob `ba5eb3cfcdd759fff76b3e7e7c58cba604e29b47` | Validation invokes two standard-library synthetic suites; proof and release-dry-run jobs explicitly check held boundaries | It is not TODO-only; a successful hold check still produces no proof or release |
| [OccurrenceEvidence workflow](../../../.github/workflows/fauna-occurrence-evidence.yml), blob `faae7732e4cafe7f997bc367dc67ba5c61f8dd06` | Declares focused tests, fixture replay, and generated-receipt validation | Workflow source is not evidence those commands passed on this revision |
| [OccurrenceEvidence schema](../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json), blob `55bfdf896627443281e41ef2761024bddedc7828` | Draft object schema declares required fields and `additionalProperties: false` | Not a Fauna configuration schema, operational acceptance, or proof that every Fauna schema is restrictive |
| [CODEOWNERS](../../../.github/CODEOWNERS), blob `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | `/configs/` routes to `@bartytime4life`; no narrower Fauna-config pattern in these bytes | Routing is not accepted stewardship, required approval, or independent review |

### Maturity matrix

| Capability | Status at this review |
|---|---|
| Tracked configuration payload | **Absent in this exact config directory** |
| Loader, direct consumer, precedence, config schema binding | **UNKNOWN / not established by this review** |
| Broader Fauna validation | **CONFIRMED source-level bounded implementation; maturity remains file-specific** |
| Exact-head test results and hosted enforcement | **NEEDS VERIFICATION; not established by workflow inspection** |
| Taxonomy resolver, accepted geoprivacy policy and runtime integration | **NEEDS VERIFICATION** |
| Live source admission, release, deployment, publication | **Not authorized or established by this README** |

The July `v0.3` blanket statements about empty schemas, placeholder fixtures, and TODO-only validation are superseded by this bounded ledger. Uninspected packages, policies, fixtures, and release surfaces are not thereby declared complete.

## What belongs here

Small shared settings or inactive authoring examples with an explicit consumer justification may belong here: placeholder-only `*.template.yaml` files; tiny synthetic YAML/JSON/TOML examples; references to accepted taxonomy, source-role, sensitivity, display, freshness, or review profiles; and config-specific migration/validation notes.

Examples must be unmistakably synthetic and must not provide plausible reconstruction clues for real taxa occurrences, sites, people, collections, telemetry, or properties. File extensions and profile names are examples, not discovered payloads or a new schema.

Safe reversible drafting may proceed with clearly labeled non-critical unknowns. **Consumer-ready use** requires the binding and validation gates below; source activation and publication remain separate transitions.

## What does not belong here

Do not commit source payloads, real occurrences or surveys, specimens/media, acoustic/eDNA records, mortality/disease records, telemetry, protected geometry, observer/landowner information, private endpoints, credentials, cookies, signed URLs, or workstation/deployment bindings here.

Do not duplicate schemas, semantic contracts, source registries, taxonomic authority tables, executable policy, geoprivacy parameters, receipts, proofs, release manifests, or correction records. Do not embed source clients or a second connector hierarchy.

Reject bypasses such as `skip_review`, `allow_exact`, or an unqualified `trusted`/`public` flag that substitutes for separate evidence, rights, sensitivity, review, and release decisions. UI masking cannot make restricted input suitable for this directory.

## Inputs

Before a payload is treated as consumer-ready, identify its consumer and accountable review assignments; format/version/parser; canonical contract and restrictive schema; referenced source/policy profiles; permitted configurable fields; effective precedence and unknown-key behavior; no-network test boundary; and correction/deactivation/rollback path.

Domain-sensitive inputs must separately preserve taxonomy, source role, occurrence class, observation method, spatial support, temporal meaning, rights, sensitivity, and review state. Missing evidence remains explicit; it does not become a permissive default.

## Outputs

Current output is documentation only. A future consumer-bound file may select already-governed behavior; it cannot issue a `PolicyDecision`, `RedactionReceipt`, `ReviewRecord`, `EvidenceBundle`, or `ReleaseManifest` by naming one.

Public clients consume governed APIs and released public-safe artifacts, never this directory as a truth store or a shortcut to RAW, WORK, QUARANTINE, internal stores, or a model endpoint.

## Validation

### Documentation validation

For a README-only change, check the complete diff, stable metadata identity, one H1, heading/fragment compatibility, resolving relative links, UTF-8 and whitespace hygiene, truth labels, and absence of sensitive examples or authority-changing wording. Re-pin target bytes and overlap before writing; verify the remote blob and single-file scope afterward.

Record commands, exact base/head, results, limitations, and rollback in the branch/PR handoff. Structural document checks do not prove domain runtime behavior. Never report inherited or unrun checks as passing.

### Future payload validation

Require deterministic parsing; a consumer-specific restrictive schema; semantic validation; explicit loading and precedence; tested unknown-key rejection for authority-affecting or unsupported keys; no unsafe overrides; and redacted diagnostics. Profile references must resolve without fetching live data merely because configuration exists.

Check taxonomy identity, source-role preservation, occurrence/model separation, time and spatial support, rights, sensitivity, reconstruction risk, and cache invalidation. Exercise the actual parser and consumer, not just an example schema. Configuration-payload validation is **not applicable to this revision**, which adds no payload.

The inspected `domain-fauna.yml` invokes the following bounded suite. This is a repository command reference, **not a claim of execution in this documentation update**, and it does not validate a future config loader. Run it from a prepared repository root:

```sh
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m unittest --verbose \
  tests.domains.fauna.test_fauna_smoke \
  tests.domains.fauna.test_public_safe_migration_fixture
```

### Required negative cases

| Case | Required boundary |
|---|---|
| Unknown taxon, synonym conflict, merge/split, or stale status | Preserve uncertainty and versioned identity; do not silently rekey or confirm presence |
| Aggregator promoted to authority; model/range/candidate promoted to observation | Reject the unsupported claim or role change |
| Missing rights, evidence, policy, review, transform, or release support | Hold, deny, or abstain; no implicit permission |
| Exact sensitive geometry or reconstruction through time, IDs, counts, media, tiles, or joins | Deny exposure before delivery, including caches and logs |
| Malformed file, unsupported version/key, conflicting precedence, partial application | Fail closed and preserve a known-safe configuration |
| Duplicate registry identity, noncanonical writer, or implicit source fetch | Reject the bypass; retain one source-first identity |
| Withdrawn source/release, changed taxonomy/policy, or failed invalidation | Stop stale public reuse; require correction and rebuilding |
| Missing deactivation or rollback target | Do not graduate the payload to operational use |

## Review burden

The verified GitHub route is `@bartytime4life` through `/configs/`. Configuration and Fauna review remain required; accepted stewardship and independent approval are not inferred from that route.

A payload also needs the applicable consumer, taxonomy, source/rights, sensitivity/geoprivacy, schema, validation, security, policy, and release/correction reviewers. Where protected records are implicated, include the relevant steward or rights-holder authority. Documentation authors cannot self-grant these roles.

## Related folders

### Configuration and doctrine

Use the [parent README](../README.md) for shared configuration rules, [Fauna domain README](../../../docs/domains/fauna/README.md) for domain navigation, and [adopted Directory Rules](../../../docs/doctrine/directory-rules.md) with [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) for placement.

### Authority and implementation-shaped surfaces

The [source registry parent](../../../data/registry/sources/README.md) controls the family boundary. The [Fauna registry child](../../../data/registry/sources/fauna/README.md) remains a useful historical navigation surface, but its older unresolved-canonical-family language must not override the adopted rules or parent correction.

The [OccurrenceEvidence schema](../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json), [focused workflow](../../../.github/workflows/fauna-occurrence-evidence.yml), and [domain workflow](../../../.github/workflows/domain-fauna.yml) show specific implementation boundaries, not a general Fauna readiness certificate. Refer to domain navigation for other contracts, policies, validators, fixtures, and release-related lanes; reverify each before use.

## ADRs and drift triggers

No new ADR, root, writer, schema, or policy is introduced. Apply accepted authority before changing ownership, a domain slug, a canonical schema or registry family, a compatibility path, source identity, sensitivity, public exposure, or release semantics.

**Resolved authority:** the source-registry family is `data/registry/sources/`. **Unresolved implementation:** exact record organization, writer/consumer binding, generated-view migration, physical RAW placement, and published-carrier convergence. A same-file README correction does not settle those migrations.

An ordinary inactive template inside an established responsibility does not automatically require a new ADR. A parallel authority, topology migration, policy change, or new exposure path does require the applicable decision, impact review, validation, and rollback.

## Scope and bounded context

Configuration references the owning responsibilities; it does not absorb them:

```text
human domain guidance      -> docs/
semantic meaning           -> contracts/
machine-checkable shape    -> schemas/
admissibility rules        -> policy/
source identity            -> data/registry/sources/
source acquisition         -> connectors/ (source-first)
lifecycle instances        -> governed data/ lanes
release decisions          -> release/
shared non-secret settings -> configs/
```

This is an authority map, not an inventory or permission to scaffold every lane. Preserve `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`; promotion is a governed transition, not a file move.

## Configuration classes

**PROPOSED design categories, not implemented keys:** taxonomy/crosswalk profile selection; source-role mapping references; restricted/public-derivative routing; sensitivity profile references; public-safe display allowlists; freshness and review routing; cache invalidation; and time-bounded migration support.

Select accepted profiles by stable reference. Do not copy their authority content, invent an accepted resolver, or place geoprivacy radii, randomization distributions, tier-transition logic, or transform code in this lane.

## Minimum configuration contract

The following is a **PROPOSED review checklist**, not a machine schema or requirement to add unused fields. A future consumer defines and validates the exact shape in the proper authority homes.

| Conceptual fields | Required meaning |
|---|---|
| `config_id`, `config_version`, `domain`, `format_version` | Stable identity, supported shape/version, and explicit `fauna` scope |
| `consumer_id`, `owner_refs` | Exact binding and accountable assignments; no invented owners |
| `contract_ref`, `schema_ref` | Controlling semantics and machine shape; no duplicated authority |
| `policy_profile_refs`, `source_registry_refs` | Versioned authority references preserving canonical identity |
| Taxonomy, source-role, occurrence, sensitivity, temporal, public-safe profile references | Explicit decisions supplied elsewhere, not approval by configuration |
| `unknown_key_behavior`, `precedence`, `network_posture` | Tested effective configuration; no implicit discovery, network access, or unsafe overrides |
| `logging_posture`, `failure_posture` | Minimized diagnostics and finite fail-closed outcomes |
| `migration`, `rollback` | Compatibility window, deactivation, correction, invalidation, and prior known-safe version |

## Consumer binding, precedence, and discovery

No loader is established here. Do not auto-discover this directory from its name or interpret a committed file as active.

A binding must identify the exact consumer/code or declarative registration, supported file/version, parser, schema, load timing, error handling, and deactivation path. Document effective precedence for defaults, shared config, environment/local overrides, and deployment configuration; there is **no universal precedence order established by this README**.

Secret resolution remains separate and must never serialize secrets into the repository or effective-config logs. Overrides cannot reduce sensitivity, change source authority, remove required review, or expose unreleased material. Unsupported authority-affecting keys fail closed rather than being silently ignored.

## Fauna object-family boundaries

These are domain review concepts, not a claim that every family is implemented or accepted.

| Family | Boundary to preserve |
|---|---|
| `Taxon`, `TaxonCrosswalk`, `ConservationStatus` | Identity, synonym/crosswalk assertions, and jurisdiction/time-bound status remain separate from presence |
| `OccurrenceEvidence`, `OccurrenceRestricted`, `OccurrencePublic` | Source evidence, restricted material, and public-safe derivatives retain distinct lifecycle and access meaning |
| `RangePolygon`, `SeasonalRange`, `MigrationRoute` | Range/model/seasonal support is not direct occurrence or precise telemetry |
| `SensitiveSite`, `MonitoringEvent` | Sensitive-site exposure and method-specific monitoring require their own evidence and review |
| `MortalityObservation`, `DiseaseObservation`, `InvasiveSpeciesRecord` | A report does not establish cause, diagnosis, prevalence, legal designation, or a confirmed invasion |
| `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, `EvidenceBundle` | Different accountability/evidence families; none is interchangeable with configuration or release approval |

## Taxonomy identity and status

Preserve source-native taxon identifiers and names, reviewed authority/vocabulary versions, synonyms, unresolved conflicts, and merge/split lineage. Display labels do not replace identifiers. A taxonomy change must not silently rekey records or erase historical interpretations.

Conservation and legal status retain source, jurisdiction, effective time, and supersession. Status is not occurrence evidence. Taxonomy/status changes require review of affected relations, caches, indexes, tiles, and reports.

## Source role and evidence character

Keep original provider/authority, access platform, method, and claim support distinct. An aggregator does not inherit original-source authority; community observation is not automatically specimen, agency, or regulatory authority. Model, aggregate, contextual, candidate, and synthetic support retain their own limitations.

These descriptions are not a replacement `source_role` enum. The inspected OccurrenceEvidence draft schema carries a concrete vocabulary; any consumer mapping must follow its actual governing contract/schema without relabeling authority. Access restrictions and rights are separate axes, not observation roles.

## Occurrence, monitoring, range, and candidate boundaries

Range, habitat association, suitability, density, occupancy, and distribution models do not substitute for direct occurrence evidence. Acoustic, eDNA, camera, specimen, checklist, survey, telemetry, mortality, disease, and invasive-species records retain method-specific uncertainty.

Non-detection is not absence unless sampling design and evidence support that inference. Scores, thresholds, model probabilities, and generated language cannot confirm a candidate by themselves. Duplicate resolution preserves lineage and uncertainty; public counts require small-cell and rare-taxon disclosure review. Habitat owns habitat patches/suitability; a cross-lane assignment does not transfer Fauna truth authority.

## Time, seasonality, freshness, and correction

Separate observation time, event interval, reporting time, retrieval/processing time, model issue/valid time, seasonal/life-stage scope, source freshness, embargo, release, and correction/withdrawal time. Do not replace them with one apparently current timestamp.

Ambiguous or stale support remains visible. Embargo expiry alone does not authorize release. Taxonomy, status, source, policy, or release changes trigger review and scoped invalidation rather than silent reuse.

## Spatial support, precision, and reconstruction risk

Distinguish restricted exact points/tracks, generalized points, cells, polygons/ranges, corridors, aggregates, and withheld geometry. Preserve method and precision labels; generalized display is not exact location or release approval.

Review reconstruction through timestamps plus observer/route histories; externally joinable IDs; media EXIF, thumbnails, names and URLs; rare labels and small counts; tile attributes, boundaries and zoom; parcel/trail/water/habitat/facility joins; and logs, analytics, screenshots, exports, or support bundles. Where safety is unresolved, withhold, generalize through accepted authority, quarantine, or deny before delivery.

## Sensitivity, geoprivacy, and tier motion

Sensitive occurrences and sites default to **T4** under Fauna doctrine. A public-safe **T1 derivative** requires accepted geoprivacy/generalization controls, `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, admissible evidence, and separate release/correction/rollback support. The restricted original remains restricted; this is not a config-driven downgrade.

Configuration references an accepted profile, never its approval. Parameters belong with policy/transform authority, not here. Missing, stale, unsupported, or conflicting profile references fail closed. Public lineage must support auditing without leaking restricted inputs or reconstruction-enabling transform details.

## Source rights, attribution, and stewardship

Resolve provider and original-record identity, applicable record/media terms, attribution, redistribution and derivative permissions, public/commercial-use restrictions, retention, embargo, permits, steward authority, permitted claim families, automation/rate limits, correction contacts, and freshness before operational use.

Public accessibility is not redistribution permission. Aggregation does not erase upstream restrictions. This revision verifies no provider license, endpoint, authorization, or live dataset and admits no source.

## Connector and source-registry boundaries

### Connectors

Accepted rules are source-first: acquisition belongs under `connectors/` using the canonical source ID or declared provider grouping. `connectors/fauna/` remains a compatibility/navigation concept, not permission for another source-client hierarchy. Domain normalization belongs with its accepted pipeline/package responsibility.

Maintain one source-first RAW capture identity. As the current Fauna domain README explains, `data/raw/fauna/` may be an **optional compatibility/reference** to that capture, not a mandatory hop or accepted payload writer. Exact physical capture placement remains **HOLD / NEEDS VERIFICATION**. Route through governed sensitivity handling without duplicating RAW bytes; a connector does not publish.

### Source registry

`DIR-SOURCE-001` through `DIR-SOURCE-004` and the [registry parent](../../../data/registry/sources/README.md) establish `data/registry/sources/` as the canonical family. Existing `data/registry/sources/fauna/` and `data/registry/fauna/sources/` views do not have equal independent-write authority.

Do not choose the convenient copy, duplicate a SourceDescriptor, or infer an accepted `sources/<domain>/<source_id>` writer from directory shape. Domain-first records may be governed generated/compatibility views; actual binding is not proven here. Migration needs writer/consumer inventory, identity crosswalk, accepted placement, view contract, validation, and rollback. Older child wording that leaves the canonical family undecided is drift, not a reason to reopen the accepted family decision.

## Logging, telemetry, caches, and derived indexes

Minimize diagnostics; never expose protected geometry, source payload fragments, sensitive identifiers, person/landowner/permit/facility details, credentials, or signed locators in logs, cache keys, previews, analytics, errors, or support bundles.

Source/rights changes, taxonomy/crosswalk versions, status, policy/transform profiles, embargo, field allowlists, generalization, and correction/withdrawal/release changes require scoped invalidation. Search/vector/graph indexes, tiles, reports, and AI summaries remain rebuildable derivatives, not truth. Failed invalidation must not leave unauthorized material silently available.

## Failure behavior

Exact consumer reason codes remain **PROPOSED** until implemented and tested. Keep three different outcomes separate:

| Layer | Boundary |
|---|---|
| Validation | Internal `PASS`/`FAIL` or error means a bounded check result, not permission to expose data |
| Work disposition | `HOLD`, quarantine, remediation, or denial preserves unresolved obligations |
| Governed response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` follows the actual runtime contract and admissible evidence |

Malformed configuration must not partially apply. Missing evidence must not fall back silently to stale caches or a model. Unresolved taxonomy, rights, precedence, policy, or conflicting registry identity must not become permission. A successful explicit workflow hold is not a successful proof build or release dry-run.

## Governed AI and generated language

Keep the sequence: scope -> evidence -> `EvidenceRef` -> `EvidenceBundle` -> rights/sensitivity/policy/review/release checks -> cited bounded answer or abstention/denial/error.

AI may explain released evidence and uncertainty or draft review notes. It cannot reconstruct protected sites, upgrade source authority, settle taxonomy/legal status without support, convert a range/model/candidate into occurrence, or decide redaction, review, or release. A configuration profile cannot grant a model new evidence or access authority.

## Migration and anti-bypass posture

Pin exact base/target bytes, identify the consumer and owning root, inspect accepted authority and overlapping work, then author the smallest reversible change. Separate changed-area evidence from unrelated inherited failures. Preserve existing identities and fragment links when updating documentation.

A future payload change also needs parser/schema and negative tests, source/taxonomy/time/rights/sensitivity review, deterministic precedence, minimized effective-config auditing, and deactivation/invalidation/rollback. Do not copy authority objects into config, create another registry writer, weaken validation, or treat fixture success as live readiness.

No code, schema, policy, validator, workflow, registry, or runtime behavior changes in this revision, so this README is the affected documentation surface; companion historical checkpoints are not rewritten.

## Rollback, correction, supersession, and invalidation

For this documentation-only revision, preserve the prior blob and branch/commit evidence. Before merge, the isolated change can be abandoned through the authorized review process. After merge, a separately reviewed revert restores the prior file without force-pushing or rewriting shared history; nothing here requests an automatic revert.

For a future payload, disable the affected selection, preserve the faulty version and audit evidence, identify downstream effects without exposing protected data, restore the known-safe version, rerun validation, and invalidate/rebuild caches and carriers. Record required correction, withdrawal, release, and rollback objects in their owning homes.

A Git revert does not revoke disclosed data, invalidate external caches, correct released artifacts, or replace auditable publication lineage.

## Definition of done for the first payload

- [ ] A real shared consumer need, exact binding, accountable assignments, and correct responsibility home are established.
- [ ] Format, version, parser, restrictive schema, semantics, allowed keys, precedence, and safe failure are tested.
- [ ] Profile references preserve taxonomy, source role, occurrence class, time, spatial support, rights, and sensitivity without duplicating authority.
- [ ] Synthetic valid/invalid/held/denied cases exercise the actual consumer with no live source retrieval.
- [ ] Sensitive-data, secret, reconstruction, media, logging, cache, tile, export, and cross-lane risks are reviewed.
- [ ] One canonical source identity survives compatibility views; no implicit discovery or activation is introduced.
- [ ] Deactivation, migration, correction, supersession, invalidation, and rollback are verified.
- [ ] Actual changed-area results, unrun checks, inherited failures, and independent review limitations are recorded at exact revisions.
- [ ] Source admission, transformation approval, evidence closure, release, and publication remain separate governed gates.

## Last reviewed

**2026-09-04**, using GitHub evidence at `main@700570cbcf191038aa20a030174c2dd08cf93675`. Configuration inventory is exact for the tracked directory; broader implementation inspection is bounded to the named sources above.

**Lineage:** `v0.3` (2026-07-14, `main@b04e9b4a576557ec8cf2f48f6cbe45fd07fbec7a`) is retained in Git history. The read-only [Fauna architecture PDF](https://drive.google.com/file/d/1mWhhtubyaAtNuWJ3vY7nuDLx50Wig7Bj/view), native Drive [Directory Rules](https://docs.google.com/document/d/1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs/edit), and [Notion Fauna coordination page](https://app.notion.com/p/3caa92021bf6811b8926dc0010d67672) informed this review. Their proposed paths, old no-repository findings, and schedule/status snapshots are lineage, not current implementation or activation authority.

Reverify before the first payload, consumer binding, profile selection, source/RAW migration, geoprivacy change, or public-output integration. No source artifact was edited; no merge, release, deployment, promotion, publication, or settings change is authorized.

[Back to top](#top)
