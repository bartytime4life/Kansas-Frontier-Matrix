<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-flora-readme
title: configs/domains/flora/ — Governed Flora Configuration Boundary
type: readme
version: v0.4
status: draft
owners: "OWNER_TBD — Config, Flora, taxonomy/herbarium, source/rights, sensitivity/geoprivacy, cultural/stewardship, consumer, validation, policy, release, and documentation stewards"
created: 2026-07-13
updated: 2026-09-04
current_path: configs/domains/flora/README.md
owning_root: configs/
scope_id: flora
readme_profile: BOUNDARY_COMPACT
policy_label: "public; config-sublane; non-secret; non-authoritative; taxonomy-aware; specimen-aware; source-role-aware; time-aware; rights-aware; cultural-rights-aware; geoprivacy-aware; reconstruction-resistant; deny-by-default; no-live-binding; no-source-activation; no-release-authority"
truth_posture: "CONFIRMED tracked README-only config lane, accepted directory-governance adoption, review routing, and bounded validator/workflow source; PROPOSED future consumer-bound configuration; UNKNOWN config loading, runtime integration, and public operation; NEEDS VERIFICATION ownership, binding-specific authority, policy execution, and exact-head hosted checks"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  authoring_base_commit: 700570cbcf191038aa20a030174c2dd08cf93675
  main_tree: b17f061592f3da0b1903c5252bc1d12437fe3575
  flora_config_tree: 5b3781db02c96d35c3f5f10f18943e94f728a7bc
  prior_blob: 3215a5eeec3355ab3b47abaf02aa3603303c72e6
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  domain_workflow_blob: 3fe6b1ba8150960692b6b2fc764c6aa31d09565c
  public_safe_validator_blob: 17933f997f7cb1219e3057ea74bf2c077dc45386
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/flora/README.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-flora.yml
  - ../../../tools/validators/domains/flora/validate_public_safe_fixture.py
notes:
  - "Same-path documentation update only; no executable configuration, consumer, schema, policy, source, workflow, release, or public artifact changes."
  - "v0.4 replaces the July whole-domain scaffold summary with a bounded current-source ledger; it does not certify all Flora implementation."
  - "The configuration lane remains README-only, while the separate domain workflow now runs a synthetic-fixture suite and retains explicit proof/release holds."
  - "Existing v0.3 H2 navigation anchors are retained. Future configuration fields/classes below are design checklists, not adopted machine contracts."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Flora Domain Configuration

`configs/domains/flora/` holds configuration-facing guidance and, when a consumer is established, safe defaults, templates, and profile references for Flora. It does **not** own botanical truth, taxonomy, cultural authority, source admission, geoprivacy policy, evidence, review, release, or publication.

**Status:** draft v0.4 · **Tracked contents:** README only · **Consumer binding:** not established · **Review route:** `@bartytime4life`, not an accepted stewardship assignment.

[Status and evidence](#status) · [What belongs here](#what-belongs-here) · [Consumer binding](#consumer-binding-precedence-and-discovery) · [Sensitivity](#sensitivity-geoprivacy-cultural-rights-and-join-risk) · [Validation](#validation) · [First payload](#definition-of-done-for-the-first-payload) · [Rollback](#rollback-correction-supersession-and-invalidation)

> [!IMPORTANT]
> **README-only describes this configuration directory, not the entire Flora domain.** At the pinned snapshot, the separate `domain-flora` workflow executes a bounded synthetic-fixture test suite. Its proof-building and release-dry-run jobs remain explicit readiness holds. Neither a configuration file nor a green held job establishes botanical truth, release readiness, or safe public use. See the [evidence ledger](#evidence-ledger).

> [!CAUTION]
> Exact or reconstructable rare, protected, culturally sensitive, steward-controlled, medicinal, seed-source, or restoration-sensitive locations and knowledge fail closed for ordinary public use. Public accessibility, generalized geometry, a profile name, or an AI answer cannot substitute for rights, cultural authority, evidence, policy, review, release, correction, and rollback support.

## Purpose

Provide a reviewable boundary for **how a named consumer handles already-governed botanical material**. Inherit the [domain configuration contract](../README.md) and [configuration-root rules](../../README.md); keep Flora-specific taxonomy, specimen/occurrence, temporal, cultural-rights, and reconstruction-risk constraints here.

This page serves configuration maintainers, Flora and herbarium reviewers, consumer owners, rights and sensitivity reviewers, and contributors assessing a future payload. It is not a second Flora architecture, source registry, policy document, or executable configuration contract.

## Authority level

**Owning root: `configs/`; local scope: `flora`.** This is a same-path configuration boundary, not a new domain root or authority home.

Accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../../docs/doctrine/directory-rules.md) bytes despite their preserved internal `PROPOSED_FOR_ADOPTION` label. Responsibility-root placement, domain-as-lane scope, and the compact boundary/inheritance rules in §16 govern this page. The older Drive Directory Rules document is lineage, not an alternative writable authority.

| Responsibility | What configuration may do | What it cannot do |
|---|---|---|
| Consumer behavior | Reference a supported parser, version, load path, and conservative profile. | Invent loading, precedence, or runtime integration. |
| Meaning and shape | Reference verified contracts and schemas. | Define a second taxonomy, object contract, enum, or schema. |
| Source and evidence | Preserve accepted identifiers, roles, and evidence references. | Admit a source, upgrade evidence, or manufacture an EvidenceBundle. |
| Rights and sensitivity | Select an applicable, already-governed profile. | Grant consent, lower protections, approve a transform, or mint its receipt. |
| Release and correction | Reference authorized state and rollback instructions. | Approve review, promote, publish, or silently supersede released material. |

Keep the lifecycle intact:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed transition, not a file move, config toggle, passing test, or merge. Public clients use governed APIs and released artifacts, never internal or unreleased stores.

## Status

### Repository snapshot

The following findings are pinned to `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`, inspected on **2026-09-04**. They are not a moving claim about later `main`.

| Item | Verified value or limit |
|---|---|
| Prior README | v0.3; blob `3215a5eeec3355ab3b47abaf02aa3603303c72e6`; reviewed 2026-07-14. |
| Tracked local tree | `5b3781db02c96d35c3f5f10f18943e94f728a7bc`; exactly one README, no payload or child directory. |
| Scope of inventory | Git-tracked files only; not ignored, untracked, external, or deployed configuration. |
| Consumer, loader, precedence | **UNKNOWN / not established** by the inspected sources. |
| Stewardship | **NEEDS VERIFICATION**; CODEOWNERS is routing, not role acceptance or independent approval. |
| Exposure, mutation, retention | Public repository documentation; reviewed version-controlled edits; history retained in Git. No source-data retention or runtime-store authority. |

```text
configs/domains/flora/
└── README.md  # Configuration boundary; no executable payload
```

Pre-write reconciliation used `main@700570cbcf191038aa20a030174c2dd08cf93675`. The comparison from the inspection commit changed only `catalog/triplet/README.md`; the target and inspected authority/validation sources remained unchanged.

### Evidence ledger

All repository links in this ledger identify the same immutable inspection commit. Other relative links are navigation, not fresh implementation certificates.

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| [Tracked configuration directory][e-config-tree] | README-only local inventory. | A consumer or a whole-domain implementation inventory. |
| [Parent configuration boundary][e-parent] | Non-secret, non-authoritative domain configuration posture. | Flora-specific loading, validation, or activation. |
| [Accepted ADR-0029][e-adr] | Adoption of the pinned Directory Rules bytes and responsibility-root law. | Acceptance of other ADRs, source rights, or release. |
| [CODEOWNERS][e-owners] | `/configs/` routes to `@bartytime4life`. | Completed review, accepted stewards, required checks, or separation of duties. |
| [Public-safe fixture validator][e-validator] | Concrete code for the `flora-public-safe-fixture` synthetic profile. | Config parsing, botanical truth, real geoprivacy approval, or EvidenceBundle closure. |
| [Domain workflow][e-workflow] | `validate-flora` invokes a synthetic-fixture suite; proof and release jobs test readiness holds. | A passing run in this session, proof production, an executed release dry run, deployment, or publication. |
| [Flora domain overview][e-domain] | Botanical scope and governance guidance; its June implementation caveats remain historical. | Current maturity inferred from its `TODO` badge or proposed path examples. |

### Implementation maturity

The July statement that the entire domain workflow is **TODO-only** is superseded by the inspected workflow source. `validate-flora` checks its required artifacts and invokes `test_flora_smoke.py`. `build-proof-flora` and `publish-dry-run-flora` retain `WORKFLOW_SKIPPED_EXPLICIT` / `WORKFLOW_HOLD` states; they do not build a proof or execute a release.

This revision makes no blanket claim that all Flora schemas are empty, all fixtures are absent, all packages are implemented, or production is ready. Those statements require their own current, bounded inspection. A package version or directory count is not sufficient evidence either way.

## What belongs here

Small, commit-safe defaults, templates, synthetic examples, conservative profile references, and migration guidance for a **named consumer** belong here. A future file must explain its format, supported consumer, validation, failure behavior, exposure, and rollback.

A reference may select an approved taxonomy, sensitivity, freshness, rights, review, or display profile. It cannot redefine that profile. Examples must use synthetic identifiers and avoid real or reconstructable taxa-locality combinations, accession records, collector identities, cultural knowledge, or live service bindings.

## What does not belong here

Do not store credentials, cookies, private endpoints, signed URLs, workstation bindings, source downloads, occurrence/specimen records, herbarium labels or images, collector details, private-land clues, protected knowledge, or sensitive geometry.

Do not add contracts, schemas, policy rules, registries, lifecycle data, EvidenceBundles, receipts, proofs, manifests, review decisions, release decisions, or correction records to this lane. Do not encode bypasses such as public exact-location access, skipped review, disabled redaction, or implicit source/watcher activation.

## Inputs

A **consumer-ready** payload needs a verified consumer and owner route; declared format/version/parser; explicit load path and precedence; applicable contract/schema/profile references; synthetic or authorized values; object/source-role and time semantics; rights/cultural/sensitivity review where applicable; deterministic positive and negative tests; and a migration/rollback path.

Safe, reversible authoring is a separate stage: a clearly labeled, inert proposal or synthetic test design may be drafted while non-safety questions remain open. Missing production approvals block activation or exposure, not ordinary README authoring. Never put schema-invalid placeholders into a machine-consumed file without an accepted sentinel convention.

## Outputs

**Current output: documentation only.** Future validated configuration may support parsing, conservative routing, profile selection, stale-state handling, field allowlisting, or migration for its verified consumer.

A config artifact cannot itself create an admitted source, accepted taxon, occurrence claim, consent, transform approval, EvidenceBundle, PolicyDecision, ReviewRecord, release, or public-safe derivative. Naming these objects is not proof that they exist or apply.

## Validation

### Documentation validation

For this file, check the stable document ID and creation date, metadata syntax, one H1, heading order, retained H2 fragments, internal navigation, balanced fences, relative-link targets, UTF-8/LF formatting, final newline, and absence of protected material or credentials. Bind any result to the exact candidate bytes or commit; do not inherit a result from another README or base.

### Existing domain validation command

The inspected [domain workflow](../../../.github/workflows/domain-flora.yml) contains this command, run from a repository checkout:

```bash
python -m unittest discover \
  --start-directory tests/domains/flora \
  --pattern 'test_flora_smoke.py' \
  --verbose
```

**Scope:** a standard-library, synthetic public-safe fixture suite. It is not a Flora configuration test and is not reported as executed by this documentation revision. Its workflow source is evidence of wiring, not a test result. No dependency installation or live source access is needed to author this README.

### Future payload validation

| Check | Required proof for the named consumer |
|---|---|
| Parsing and shape | Supported format/version; duplicate keys, unknown keys, malformed input, and incompatible profiles handled explicitly. A permissive schema is not semantic proof. |
| Binding and precedence | Exact load path, load/reload timing, merge order, missing-file behavior, and local/environment overrides are deterministic and tested. |
| Botanical semantics | Taxon versions and determinations preserved; specimen, occurrence, range, model, community, candidate, and restoration roles do not collapse. |
| Rights and safety | Source/distributor roles, record/media rights, cultural authority, geoprivacy, time, join risk, and public-field restrictions survive every output path. |
| Evidence and lifecycle | Applicable references resolve; validation, policy, review, proof, release, correction, and rollback remain distinct. |
| Reversibility | Deprecated keys, deactivation, cache/index invalidation, supersession, and rollback are tested with synthetic data. |

### Required negative cases

Cover unresolved or conflicting taxa; a historical specimen presented as current presence; an unvouchered observation presented as vouchered; a range/model/habitat join presented as occurrence; distributor-origin substitution; unknown or duplicate keys; conflicting precedence; unsupported versions; and missing references.

Also cover restricted geometry or metadata, cultural/collector/landowner leakage, join-induced reconstruction, stale/embargoed/corrected/withdrawn inputs, unauthorized profile weakening, missing rollback, and failed cache invalidation. Use synthetic fixtures and no live network by default. Exact predicates and expected reason codes belong to the consumer's verified contract and tests.

Executable configuration validation is **NOT APPLICABLE** until this directory has a payload and verified consumer. Broader domain tests and hosted checks must be reported separately as run, not run, failed, skipped, or held.

## Review burden

The inspected [CODEOWNERS](../../../.github/CODEOWNERS) routes `/configs/` to `@bartytime4life`. This does not establish independent review, domain stewardship, community authority, or required-check enforcement.

README review needs configuration/documentation and Flora expertise. A payload additionally needs its consumer owner and the relevant taxonomy/herbarium, source/rights, sensitivity/geoprivacy, cultural/community, validation, security, policy, and release reviewers. Cross-domain joins require the affected lane owners; do not invent people or teams to fill these roles.

## Related folders

### Configuration and doctrine

The [parent domain README](../README.md) owns shared configuration expectations; the [root README](../../README.md) owns commit-safe configuration placement. [Directory Rules](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) control placement and adoption. The [Flora overview](../../../docs/domains/flora/README.md) supplies domain orientation, not a current implementation certificate.

### Authority and implementation-shaped surfaces

Contracts own meaning; schemas own shape; policy owns admissibility; source registries own governed source records; tests and fixtures support bounded behavior; release records own release/correction decisions. Resolve exact bindings from the owning lane before adding a payload here. Do not copy those authorities into configuration.

For the current narrow implementation claim, inspect the [fixture validator](../../../tools/validators/domains/flora/validate_public_safe_fixture.py) and [workflow](../../../.github/workflows/domain-flora.yml), not an old cross-domain tree or package-version label.

## ADRs and drift triggers

No path move, new authority home, schema decision, or policy change is introduced. Accepted ADR-0029 controls this same-path revision; an old document's references to other ADRs do not establish their acceptance.

The v0.3 README recorded source-registry ordering differences (`data/registry/sources/flora/` versus `data/registry/flora/sources/`), singular/plural release-manifest paths, contract/schema aliases, filename variants, and source-connector aliases. **These are retained as historical binding risks, not re-certified as current unresolved conflicts.** Before a consumer binds to any such path, inspect current owning READMEs, accepted ADRs, alias records, writers/consumers, and migration evidence. This update neither selects an alias nor authorizes parallel writes.

Re-review when consumers, authority references, taxonomy versions, exposure, sensitivity, source terms, ownership, validation, precedence, aliases, or release dependencies change. A structural or authority-changing choice needs its appropriate accepted decision or explicitly provisional migration proposal, not a config shortcut.

## Scope and bounded context

### In scope

Consumer-facing parsing, conservative profile references, deterministic configuration behavior, synthetic test settings, migration, and rollback for Flora-related processing.

### Out of scope

Taxonomic adjudication, source harvesting, real specimen/occurrence processing, cultural-consent decisions, transform approval, cross-domain authority transfer, live integration, release, and publication. Habitat, Fauna, Soil, Hydrology, Agriculture, Atmosphere, Hazards, Archaeology, transport/infrastructure, and People/DNA/Land retain their own records and authority; a Flora join does not absorb them.

## Configuration classes

**PROPOSED design categories, not an accepted enum:** parser profile; taxonomy/crosswalk reference; source-role reference; occurrence-processing profile; sensitivity reference; rights/cultural reference; public-display profile; freshness/correction profile; migration profile; synthetic test profile.

Choose one primary responsibility per payload unless a verified consumer requires an atomic composite. Every referenced profile must retain its owning authority and version. A friendly name such as `public_display_profile` grants no exposure permission.

## Minimum configuration contract

This is a **design checklist**, not a new semantic or machine contract. A future consumer should make the following inspectable in its accepted format:

| Information | Required distinction |
|---|---|
| Identity | Configuration ID/version and `flora` scope, distinct from source, schema, profile, consumer, and release identity. |
| Binding | Exact consumer/version range, owner, filename, parser/encoding, duplicate-key behavior, load/reload timing, and supported keys. |
| Authority references | Applicable contract/schema, taxonomy, source-role, sensitivity, rights/cultural, public-safe, and review profiles with explicit versions. |
| Behavior | Precedence, unknown-key handling, temporal semantics, network posture, finite failure behavior, and permitted outputs. |
| Evidence | Positive/negative tests, validation results, binding-specific limitations, and policy/reference-resolution checks where applicable. |
| Change handling | Deprecation window, migration, prior version, deactivation, correction, and cache/index/tile/export invalidation. |

Do not invent required machine fields, enum values, profile IDs, accepted owners, or a generic loader from this table. Contract and schema owners must ratify any machine-facing shape.

## Consumer binding, precedence, and discovery

**No consumer binding is established for this directory.** A future binding must identify the component, explicit path, supported versions, parser/schema resolution, load timing, restart/reload needs, merge order, and failure behavior. Prove it with a deterministic synthetic test before calling it active.

### Default discovery posture

No recursive discovery, wildcard loading, filename-triggered activation, inferred lexical merge order, unreviewed local inheritance, or silent less-restrictive fallback. Missing files, malformed values, duplicate keys, unknown safety-relevant keys, and incompatible profiles must not widen access. Environment variables and local overrides cannot bypass rights, sensitivity, evidence, review, or release controls.

## Flora object-family boundaries

Object names retained here are domain vocabulary, not proof of implemented schemas. Preserve the responsibilities of `PlantTaxon` and crosswalks; `SpecimenRecord`; `FloraOccurrence`; restricted and public occurrence derivatives; rare/invasive/status records; vegetation communities; surveys; phenology; ranges/models; habitat associations; and restoration records.

A public derivative is not the restricted original. Taxonomy, observation, classification, regulatory status, review, transformation, evidence, and release are separate assertions. A config cannot instantiate or approve `RedactionReceipt`, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, or release objects by writing their names.

## Taxonomy identity and nomenclature

Retain source-native names, authority and vocabulary versions, ranks, synonyms, hybrids, cultivars, provisional identifications, common/historical names, unresolved mappings, and determination history. A synonym or crosswalk is not permission to silently merge records or erase prior identifications.

Resolver choice, authority order, mapping confidence, conflicts, update cadence, and rollback remain consumer-specific verification work. An aggregator is not automatically a nomenclatural authority. A parsed label is not an accepted determination.

## Specimen, occurrence, range, model, and candidate boundaries

A specimen carries collection, institution, catalog, voucher/determination, time, rights, and locality context. An occurrence may or may not be vouchered. Neither a historical specimen nor a current designation proves current presence.

Ranges, modeled distributions, suitability, vegetation communities, checklists, imagery candidates, restoration recommendations, and habitat joins must retain their actual evidentiary role. Planned planting, completed planting, and wild occurrence remain distinct. Configuration thresholds cannot convert any of these into direct observation or assert a voucher without supporting evidence.

## Source role and evidence character

Use the vocabulary of the **actual bound contract/schema and source profile**. Do not create a parallel role enum or flatten roles into `trusted`, `verified`, `authoritative`, or `public`.

The inspected synthetic validator, for example, requires `source_role = synthetic_occurrence`. That is a profile-local test value, not an admitted source classification or a reason to rewrite another profile's role vocabulary. Preserve origin publisher, distributor, institution, record identity, method, and evidence character separately; community observation, institutional specimen evidence, regulatory records, aggregates, models, context, and candidates are not interchangeable.

## Time, phenology, freshness, and correction

Keep collection/observation/survey intervals, identification time, source version/publication time, model initialization/valid time, retrieval/processing time, embargo expiry, review/release time, and correction/withdrawal time distinct where material.

A direct phenology observation retains its method, stage, time, and uncertainty; a remotely sensed phenology or vegetation-condition product remains derived support. Neither refresh timestamps nor a new taxonomy determination erase historical state. Use verified freshness/embargo rules; never invent a universal threshold or suppress stale, partial, corrected, embargoed, or withdrawn status.

## Spatial support, precision, and reconstruction risk

Preserve point, locality, route, plot, transect, polygon, grid, county, watershed, ecoregion, range, raster, uncertainty envelope, generalized, and withheld support as applicable. Carry georeferencing uncertainty, coordinate system, source-versus-derived geometry, and transform lineage without pretending public geometry is source geometry.

### Reconstruction checks

Review coordinate-like values, tiny polygons, low-count cells, high-resolution surfaces, accession/collector identifiers, external join keys, precise dates, itineraries, localities, landmarks, parcel/road/trail joins, restoration/seed-source context, and media EXIF. Repeated time slices or overlapping generalized products can narrow a location. Review combinations, not just isolated fields.

Public output, citations, alt text, filenames, errors, logs, caches, analytics, exports, screenshots, and map feature-state can all carry reconstructable clues. If safety cannot be established, hold, deny, withhold, delay, or apply an approved generalization before delivery.

## Sensitivity, geoprivacy, cultural rights, and join risk

### Deny-by-default location posture

Exact and reconstructable sensitive botanical locations are not ordinary public layers. Applicable evidence, rights, cultural authority, sensitivity policy, review, transform receipts, release state, correction, and rollback must resolve before exposure. A source coordinate is not a public-safe coordinate.

Transform or deny sensitive content **before public delivery**. Hidden layers, omitted popups, low opacity, client-side filters, and UI-only masking do not protect data already delivered to the client. No universal jitter, grid, precision, or delay parameter is approved here.

### Cultural, traditional, and medicinal knowledge

Preserve provenance, representational authority, consent, use restrictions, context, and attribution. Publicly accessible text does not establish community consent or authorize redistribution. Do not infer affiliation, cultural ownership, stewardship, or permission; ambiguous use remains held or denied pending appropriate review.

### Join-induced sensitivity

Individually public records can become sensitive when combined. A join inherits the strongest applicable protection until the **resulting product** is reviewed. Pay particular attention to habitat/soil/parcel joins, collector itineraries, cultural-use context, seed sources, restoration sites, small counts, and repeated generalizations.

### Permitted profile references

A consumer may select an applicable, already-governed withholding, suppression, delay, staged-access, generalization, field-allowlist, or review profile. Profile resolution, applicability, execution, validation, receipts, and release are separate checks. Configuration cannot issue or approve them.

## Source rights, attribution, cultural authority, and stewardship

Retain record-level and media-specific terms alongside the original publisher, institution, distributor, attribution, permitted uses, retention limits, and restrictions. A distributor's availability or license summary does not automatically settle an originating record's rights.

Examples must not contain real herbarium labels, images, collector details, restricted knowledge, or live credentials. Unverified source terms and cultural authority remain explicit; source activation and real-data use require their own governed transition. This README verifies no current external endpoint, provider license, or automation permission.

## Connector, source-registry, and watcher boundaries

### Connectors

Source-specific implementation belongs to the owning connector responsibility, not this configuration directory. Select a reviewed source identity and explicit consumer binding, not a convenient source alias or a new domain-specific fetch hierarchy. The prior README's `connectors/flora/` compatibility warning remains a binding-review lead, not proof that all current connector aliases have been audited.

### Source registry

Configuration may reference a verified source record; it must not create, duplicate, activate, or arbitrate source registries. Resolve the historical topology risks in [ADRs and drift triggers](#adrs-and-drift-triggers) for the actual binding before use. Stable source identity must survive any reviewed alias migration.

### Watchers

Watchers are non-publishers. File presence cannot activate them. They may detect changes and propose work, but cannot silently rewrite canonical records, upgrade botanical claims, weaken sensitivity, push directly to `main`, promote lifecycle state, or publish. Configuration does not supply credentials or source-admission authority.

## Logging, telemetry, caches, and derived indexes

Document allowed log fields, access/retention, error redaction, metrics labels, cache keys and expiry, index fields, and invalidation behavior for the consumer. Keep protected locality, taxon-location combinations, collector/landowner details, cultural terms, source tokens, and transform parameters out of ordinary diagnostics.

Test propagation of rights, sensitivity, taxonomy, correction, withdrawal, and rollback changes through API payloads, tiles, GeoJSON, PMTiles, rasters, search/vector/graph indexes, browser storage, exports, reports, and AI summaries. A reverted config is not a completed correction while a derivative still exposes superseded or protected content.

## Failure behavior

| Condition | Required safe behavior for the future consumer |
|---|---|
| Malformed/duplicate/unsupported input or ambiguous precedence | Fail atomically; do not partly apply or fall back to weaker protection. |
| Unresolved taxonomy, conflicting evidence, stale or insufficient support | Preserve uncertainty and route to hold, abstention, or explicit error. |
| Missing rights, cultural authority, sensitivity review, applicable policy, or release | Hold or deny the affected use; do not infer permission. |
| Protected/reconstructable public output or an unauthorized weakening override | Deny exposure and report a safe reason without echoing protected values. |
| Evidence-role substitution or unsupported voucher/current-presence assertion | Reject the assertion and preserve the original role. |
| Invalidation or rollback cannot close | Deny further affected public use and escalate the correction. |

Validator `PASS`/`FAIL`, work-state `HOLD`/quarantine, and outward `ANSWER`/`ABSTAIN`/`DENY`/`ERROR` are different layers. Implement exact codes in the verified consumer. A parse success or passing synthetic fixture is never a publication decision.

## Governed AI and generated language

AI is interpretive. The allowed sequence is scope → evidence retrieval → `EvidenceRef` resolution to `EvidenceBundle` → rights/sensitivity/policy/review/release checks → cited, bounded answer or abstention/denial/error.

Preserve specimen, occurrence, range, model, cultural, spatial, temporal, and correction distinctions. Do not reconstruct protected locations from joins, citations, map state, or prose. `enable_ai`, `allow_exact_location`, `skip_review`, `publish`, and similar keys cannot bypass the trust membrane. Maps, tiles, indexes, graphs, scenes, summaries, and generated language are carriers, not root truth.

## Migration and anti-bypass posture

A future change must identify old/new versions, exact keys and meaning, affected consumers and profiles, compatibility window, source/watcher effects, sensitivity/rights review, validation, deactivation, correction, invalidation, and rollback.

Use a reviewed single-write authority boundary; preserve identities and required compatibility. An alias cannot become more permissive than its target. Do not create parallel contract/schema/policy/source/release homes or hide role changes, stale state, or reduced review behind a migration.

## Rollback, correction, supersession, and invalidation

For this README-only revision, the prior blob is `3215a5eeec3355ab3b47abaf02aa3603303c72e6`. An unmerged branch may be left unused; after any separately authorized merge, rollback is a reviewed revert or forward correction restoring the intended documentation without force-pushing or rewriting shared history.

For a future executable payload: deactivate selection through the verified consumer, stop affected reload/watch processes as appropriate, preserve the faulty version and audit evidence, identify affected outputs without leaking protected material, restore a known-good version, rerun relevant tests, issue required correction/withdrawal/review records, and invalidate or rebuild affected carriers.

A Git revert does not revoke already exposed information, withdraw a release, invalidate caches, or constitute a rollback receipt. Verify the governed public path and retain correction provenance.

## Definition of done for the first payload

- [ ] Exact consumer, owner route, format/version, parser, filename, load/reload path, and precedence are verified.
- [ ] Applicable contract/schema/profile references resolve without relying on an unreviewed alias or parallel authority.
- [ ] Taxonomy, evidence character, source/distributor roles, spatial/temporal meaning, uncertainty, and correction are preserved.
- [ ] Rights, cultural authority, consent, sensitivity, geoprivacy, and joined-product review are resolved for the intended use.
- [ ] Positive and negative synthetic tests prove fail-closed parsing, binding, profile resolution, public-output restrictions, and no-network behavior.
- [ ] Logs, caches, indexes, maps, exports, citations, and AI cannot expose protected clues; invalidation and rollback are tested.
- [ ] Local validation and exact-head hosted results are separately recorded, including not-run, skipped, held, and failed checks.
- [ ] File presence, tests, or review prose cannot activate sources/watchers, manufacture proof, or authorize release/publication.

These are consumer-readiness criteria. Safe inert authoring may precede them, but execution and exposure must not bypass the applicable gates.

## Last reviewed

**2026-09-04**, against `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`; currentness claims are limited to the sources in the ledger. Exact-head test execution, broader Flora implementation, deployment, public operation, and independent review remain separate verification.

**Revision continuity:** v0.4 preserves the v0.3 document identity, creation date, H2 navigation fragments, configuration boundary, botanical distinctions, sensitivity/cultural-rights controls, and correction requirements while reducing repeated whole-domain inventories. It replaces stale blanket maturity claims with bounded source evidence. It changes no consumer behavior or authority state.

**Lineage and coordination consulted:** the April 21, 2026 [*KFM Flora Architecture PDF-Only Implementation Blueprint*][e-flora-lineage], the earlier [Drive *Directory Rules*][e-directory-lineage], and the [*KFM Hourly Flora Domain Builder v1.0* Notion page][e-coordination]. Their historical repository/scheduler observations are not current implementation or activation evidence. Drive sources remain read-only; Notion is a coordination projection, not repository authority. No external source is admitted by this revision.

[Back to top](#top)

[e-config-tree]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/configs/domains/flora
[e-parent]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/configs/domains/README.md
[e-adr]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[e-owners]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/.github/CODEOWNERS
[e-validator]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/tools/validators/domains/flora/validate_public_safe_fixture.py
[e-workflow]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/.github/workflows/domain-flora.yml
[e-domain]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/bb3eb695e6068b38453ca3ded8f1394a8fdebc20/docs/domains/flora/README.md
[e-flora-lineage]: https://drive.google.com/file/d/1awNB4HbNr3X4ll0XjJnsO-AqmuO2GSfj/view
[e-directory-lineage]: https://docs.google.com/document/d/1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs/edit
[e-coordination]: https://app.notion.com/p/3caa92021bf6815db884de68502fb21f
