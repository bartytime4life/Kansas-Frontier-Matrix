<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-flora-readme
title: configs/domains/flora/ — Flora Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Flora steward · Sensitivity steward · Cultural/rights reviewer · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; flora; deny-by-default; sensitive-location-aware; cultural-rights-aware; source-role-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/flora/README.md
truth_posture: CONFIRMED canonical flora slug, repository-present parent config contract, repository-present Flora doctrine, exact sensitive-location denial, source-role separation, join-induced sensitivity rule, and documentation-only lane / PROPOSED future consumer-bound templates and governed profile selectors / UNKNOWN consumers, precedence, loader behavior, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, taxonomy resolver, geoprivacy parameters, cultural authority, and runtime binding
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only. It does not create, load, activate, transform, expose, or publish a Flora configuration payload."
  - "v0.2 expands the Flora-specific taxonomy, source-role, specimen/occurrence, cultural-rights, sensitive-location, join-risk, validation, correction, and rollback contract without creating a new policy, schema, registry, redaction, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Domain Configuration

`configs/domains/flora/`

> Safe-to-commit, Flora-specific configuration documentation and future consumer-bound templates. This lane does not own plant taxonomic truth, occurrence or specimen truth, cultural authority, source admission, geoprivacy, sensitivity, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Repository fit](#repository-fit) · [Inputs](#inputs) · [Outputs](#outputs) · [Configuration contract](#minimum-configuration-contract) · [Taxonomy and evidence roles](#taxonomy-specimen-occurrence-and-source-role-boundaries) · [Sensitivity and cultural rights](#sensitive-locations-cultural-rights-and-join-induced-risk) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Review](#review-burden) · [Maintenance](#maintenance) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Component maturity:** documentation boundary only  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no Flora payload, loader, consumer binding, source activation, watcher activation, geoprivacy transform, or public exposure is established by this README

> [!CAUTION]
> Exact or reconstructable rare, protected, steward-reviewed, medicinal, or culturally sensitive plant locations fail closed. Directory presence, a future configuration file, or a parsed value must never lower sensitivity, convert a specimen, model, range, candidate, or context layer into observed truth, bypass cultural or steward review, activate a source or watcher, authorize a transform, promote lifecycle state, approve release, or create KFM publication.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Flora lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should behave, but they cannot decide:

- which taxonomic authority or accepted plant name is controlling;
- whether a record is a specimen, occurrence, range, distribution model, candidate, aggregate, or cultural context;
- whether a source is authoritative, admissible, licensed, or active;
- whether cultural knowledge may be represented or redistributed;
- whether exact or generalized geometry may be exposed;
- whether a geoprivacy or redaction transform is sufficient;
- whether evidence supports a botanical claim; or
- whether an artifact may be promoted, released, or published.

This README is intended for:

- Flora domain stewards;
- configuration and developer-experience maintainers;
- taxonomy, herbarium, sensitivity, geoprivacy, cultural-rights, policy, security, and release reviewers;
- package, pipeline, app, runtime, test, watcher, and tooling owners that may consume Flora configuration; and
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Flora domain meaning | **None.** Domain doctrine remains in [`docs/domains/flora/`](../../../docs/domains/flora/README.md). |
| Plant taxonomic identity | **None.** Configuration cannot select an authority by convenience, settle a synonym conflict, or create a `FloraTaxon Crosswalk`. |
| Specimen or occurrence status | **None.** A value cannot convert a model, range, candidate, aggregate, label transcription, or contextual clue into an observed occurrence or vouchered specimen. |
| Cultural authority or consent | **None.** Configuration cannot identify the rightful cultural authority, grant consent, classify knowledge as public, or authorize redistribution. |
| Source identity, role, rights, cadence, and activation | **None.** These require applicable source registry, connector, policy, rights, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Sensitivity, geoprivacy, or redaction decision | **None.** A value may select an already-governed profile; it cannot create, weaken, or approve a sensitivity rule or transform. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority through repetition, proximity, successful parsing, operational convenience, or use by a map, watcher, dashboard, or AI surface.

[Back to top](#top)

---

## Status

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `flora` is a repository-present canonical domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Flora doctrine | **CONFIRMED repository-present** | The domain README establishes evidence-first botanical handling, exact sensitive-location denial, and source-role separation. |
| Exact sensitive-location posture | **CONFIRMED doctrine** | Rare, protected, culturally sensitive, and steward-reviewed exact locations default to generalized, withheld, staged, or denied public geometry. |
| Join-induced sensitivity | **CONFIRMED doctrine** | A resulting joined product may be more sensitive than either input and must clear the strongest applicable gates. |
| Current lane content | **README ONLY** | This lane establishes documentation, not executable configuration. |
| Consumer and loader | **UNKNOWN** | No consumer, parser, discovery mechanism, merge order, or unknown-key behavior is established here. |
| Taxonomy resolver | **NEEDS VERIFICATION** | The controlling authority and crosswalk-conflict procedure require a governed decision. |
| Source rights and cultural authority | **NEEDS VERIFICATION** | Source-specific terms, cultural permissions, and redistribution boundaries must be verified independently. |
| Geoprivacy parameters | **NEEDS VERIFICATION** | Generalization scale, withholding, jitter, delay, and tier-motion parameters must come from policy and steward review. |
| Validation and CI enforcement | **NEEDS VERIFICATION** | Expectations are documented; executable enforcement is not proven by this README. |
| Runtime, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, release, or publication. |

Directory presence must not trigger discovery, source activation, network access, watcher execution, indexing, map-layer creation, AI interpretation, geometry exposure, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, Flora-specific configuration material for a named or explicitly proposed consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this configuration boundary. | Preserve non-authority, sensitivity, rights, evidence, and release controls. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified Flora consumer. | Parseable, versioned, consumer-bound, no secrets, no live binding. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Clearly synthetic values; impossible identifiers and geometry; no automatic activation. |
| Conservative profile selectors | Select an existing hold, abstain, generalize, withhold, redact, delayed-release, or review profile. | Profile must be governed elsewhere; config cannot define the policy. |
| Public-safe display hints | Select a verified generalized display profile. | Must not contain exact protected geometry, hidden identifiers, or exposure authority. |
| Migration notes | Document a real key or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |
| Validation notes | Explain verified parse, shape, semantic, rights, sensitivity, and no-network checks. | Commands and tools must be repository-grounded. |

Synthetic examples must not resemble a real specimen, collection event, locality, population, land parcel, steward record, or culturally sensitive place closely enough to enable reconstruction.

### What does not belong here

- exact or reconstructable rare, protected, medicinal, steward-controlled, or culturally sensitive plant locations;
- real specimen labels, accession records, occurrence records, survey records, collector details, observer details, private stewardship notes, or restricted cultural knowledge;
- real herbarium downloads, community-science payloads, conservation-status payloads, source snapshots, images, or rights-restricted media metadata;
- credentials, tokens, cookies, connection strings, private endpoints, workstation paths, signed URLs, or live deployment bindings;
- settings that present a range polygon, distribution surface, habitat association, candidate, model output, aggregate, or contextual inference as an observed occurrence;
- settings that present an occurrence as a vouchered `SpecimenRecord` without supporting specimen evidence;
- settings that choose a taxonomic authority, synonym, conservation status, cultural use, or legal status without governed evidence;
- settings that lower sensitivity, suppress caveats, bypass steward or cultural review, or omit required transform and review records;
- policy, registry, schema, contract, taxonomy crosswalk, source descriptor, receipt, proof, review, consent, release, correction, or publication authority;
- lifecycle data from RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED stores; or
- auto-discovery behavior based only on directory or filename presence.

### Explicit non-ownership

This configuration lane does not own:

- habitat patches, suitability surfaces, or habitat models;
- fauna taxa, occurrences, ranges, or sensitive animal sites;
- soil, hydrology, agriculture, hazard, road, settlement, archaeology, people, DNA, land, or title truth;
- source registration, source activation, rights clearance, cultural authority, taxonomy decisions, or evidence resolution;
- geoprivacy, redaction, policy, review, release, correction, or publication decisions; or
- public APIs, map layers, Evidence Drawer payloads, watcher outputs, or generated narratives.

Cross-lane references must preserve ownership, source role, sensitivity, temporal scope, and `EvidenceBundle` support.

[Back to top](#top)

---

## Repository fit

This directory is a child of the canonical domain-configuration boundary:

```text
configs/
└── domains/
    ├── README.md
    └── flora/
        └── README.md
```

The responsibility split is:

- [`configs/`](../../README.md): repository-wide safe configuration boundary;
- [`configs/domains/`](../README.md): common rules for domain-scoped defaults and templates;
- `configs/domains/flora/`: Flora-specific configuration support;
- [`docs/domains/flora/`](../../../docs/domains/flora/README.md): Flora doctrine, ubiquitous language, source families, object families, sensitivity, lifecycle, and publication expectations;
- contracts and schemas: semantic meaning and machine-checkable shape;
- source registries and connectors: source identity, role, rights, cadence, and admission;
- policy: sensitivity, rights, admissibility, geoprivacy, and public-exposure decisions;
- tests and fixtures: deterministic proof and public-safe synthetic examples;
- receipts and proofs: transformation, validation, evidence, and integrity records;
- release surfaces: promotion, release, correction, withdrawal, and rollback decisions; and
- governed APIs and released artifacts: the ordinary public delivery path.

This README must link to those authorities after verification rather than duplicating them.

[Back to top](#top)

---

## Inputs

A future Flora configuration payload requires all of the following before it may be treated as implementation-supporting:

1. **Named consumer** — exact package, app, pipeline, watcher, service, runtime, test harness, or tool.
2. **Accepted owner** — accountable owner for the consumer and configuration.
3. **Declared format** — file type, format version, parser, and load path.
4. **Authority references** — verified contract, schema, policy, source registry, taxonomy, and domain documentation as applicable.
5. **Safe values** — synthetic placeholders or non-sensitive defaults only.
6. **Role separation** — specimen, occurrence, range, distribution model, candidate, context, aggregate, and cultural-context roles remain distinguishable.
7. **Temporal semantics** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
8. **Taxonomy posture** — authority identifiers, accepted-name behavior, synonym handling, and unresolved-crosswalk behavior are explicit.
9. **Rights and cultural review** — attribution, license, redistribution, steward restrictions, cultural authority, and consent boundaries are verified.
10. **Sensitivity posture** — exact-location, reconstruction, join-induced sensitivity, geoprivacy-profile, and public-output review are explicit.
11. **Validation path** — deterministic parsing, schema checks, semantic checks, negative cases, no-network fixtures, and expected finite outcomes.
12. **Precedence contract** — merge order, override rules, environment behavior, and unknown-key behavior are explicit.
13. **Failure behavior** — malformed, stale, missing, partial, denied, held, abstained, and error states are defined.
14. **Migration and rollback** — version transition, deactivation, correction, and prior-known-good restoration are documented.
15. **No activation by presence** — the consumer requires an explicit, reviewed binding rather than directory or filename discovery alone.

Missing evidence keeps a payload `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`; it does not become operational by successful parsing.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future configuration file may support a verified consumer by selecting already-governed behavior, such as:

- a taxonomy profile identifier;
- a source-role mapping profile;
- a public-safe generalization or withholding profile;
- a stale-state or caveat profile;
- a review-routing or hold profile;
- a no-network fixture profile; or
- a verified display-profile identifier.

A file in this directory cannot itself output or authorize:

- a `Plant Taxon`, `FloraTaxon Crosswalk`, `Flora Occurrence`, `SpecimenRecord`, `Rare Plant Record`, `RangePolygon`, `DistributionSurface`, or other Flora object;
- a `SourceDescriptor`, source activation, rights decision, cultural-authority decision, or consent record;
- a geoprivacy transform, `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, `EvidenceBundle`, or validation proof;
- a catalog entry, graph projection, vector index, tile, map layer, AI narrative, or public claim;
- a release candidate, `ReleaseManifest`, correction notice, withdrawal, rollback card, or KFM publication state.

Watchers and scheduled consumers remain non-publishers. A watcher may observe or propose work only through its separately governed contract.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file should have an adjacent or embedded, repository-approved contract covering the following fields.

| Field | Requirement |
|---|---|
| `config_id` | Stable identifier under a verified repository convention. Do not invent a random authority identifier. |
| `consumer` | Exact consuming component and supported version range. |
| `owner` | Verified accountable owner or team. |
| `format_version` | Explicit configuration format version. |
| `schema_ref` / `contract_ref` | Canonical, verified references when applicable. |
| `domain` | Must remain `flora`; it does not create domain standing. |
| `source_role_profile` | Reference to a governed role mapping; no role collapse. |
| `taxonomy_profile` | Reference to an accepted taxonomy/crosswalk policy; unresolved conflicts fail closed. |
| `temporal_profile` | Rules for source, observed, valid, retrieval, release, and correction time. |
| `sensitivity_profile` | Reference to accepted sensitivity and geoprivacy policy; no embedded exposure authority. |
| `rights_profile` | Verified attribution, redistribution, and restricted-use expectations. |
| `cultural_review_profile` | Governed review reference when cultural or medicinal knowledge may be implicated. |
| `defaults` | Conservative, public-safe defaults only. |
| `unknown_key_behavior` | Reject or explicitly hold unknown keys; never silently ignore a possible safety control. |
| `precedence` | Exact overlay and override order for the named consumer. |
| `network_posture` | No network by default for tests and examples; live access requires separate source authorization. |
| `validation` | Deterministic parse, shape, semantic, rights, sensitivity, and negative checks. |
| `failure_modes` | Finite reason-coded outcomes and safe fallback behavior. |
| `migration` | Prior version, compatibility window, deprecation, and removal criteria. |
| `rollback` | Prior known-good version and verified restoration mechanism. |

Do not add machine-parsed metadata fields until the applicable schema permits them. Put unresolved requirements in review notes rather than inserting invalid placeholders.

### Precedence and overrides

No universal precedence order is established here.

A consumer must document whether Flora configuration is combined with repository defaults, development settings, test settings, local ignored overrides, environment variables, runtime configuration, or deployment configuration. When precedence is ambiguous, the consumer must stop with `ERROR` or `HOLD`; it must not guess.

A lower-trust override must never:

- activate a source or watcher;
- change source authority or evidence role;
- choose an unreviewed taxonomy;
- reduce sensitivity or geoprivacy;
- suppress cultural or steward review;
- remove citation, caveat, rights, or freshness requirements;
- bypass quarantine, policy, validation, release, or rollback gates; or
- expose exact or reconstructable protected locations.

[Back to top](#top)

---

## Taxonomy, specimen, occurrence, and source-role boundaries

### Taxonomy

Plant taxonomic identity must remain tied to a verified authority and evidence trail.

Configuration may select a governed taxonomy or crosswalk profile for a named consumer, but it must not:

- declare one authority canonical without an accepted decision;
- silently replace accepted names, synonyms, hybrids, varieties, or subspecies;
- erase competing determinations;
- convert a label transcription into a verified determination;
- infer legal or conservation status from name similarity; or
- treat a failed crosswalk as a successful identity match.

Unresolved identity or crosswalk conflict results in `HOLD` or `ABSTAIN`, not silent normalization.

### Specimen and occurrence

A `SpecimenRecord` is vouchered evidence with accession and collection lineage. A Flora occurrence may be based on observation evidence with its own uncertainty and source role.

Configuration must not collapse:

- specimen into ordinary occurrence;
- occurrence into range;
- range into observed presence at a point;
- distribution likelihood into observed presence;
- vegetation-community context into a taxon occurrence;
- community-science observation into herbarium authority;
- historical label locality into current presence;
- invasive-treatment record into untreated occurrence; or
- a candidate or inferred location into confirmed botanical evidence.

### Source roles

Source role is claim-specific. A source may be authoritative for one assertion and contextual for another.

At minimum, future consumer configuration must keep distinct:

- taxonomic or nomenclatural authority;
- regulatory or conservation-status authority;
- specimen-backed observation;
- field or community-science observation;
- steward-controlled or restricted observation;
- corroborating evidence;
- contextual environmental information; and
- modeled, inferred, aggregated, or derived products.

Configuration must not upgrade an aggregator, model, or context source into the authority role required for a consequential claim.

### Temporal semantics

Where material, preserve:

- source publication or version time;
- collection or observation time;
- valid time;
- retrieval or ingestion time;
- release time; and
- correction or supersession time.

A historical specimen does not prove current presence. A current model does not rewrite an older observation. Stale or superseded data must remain visibly stale or superseded.

[Back to top](#top)

---

## Sensitive locations, cultural rights, and join-induced risk

### Deny-by-default location posture

Exact rare, protected, culturally sensitive, medicinal, steward-reviewed, or otherwise vulnerable plant locations are denied on ordinary public surfaces by default.

Public-safe use requires the applicable combination of:

- verified rights and source-role posture;
- steward and cultural review where applicable;
- generalized, withheld, staged, or denied geometry;
- a resolvable `EvidenceBundle`;
- an applicable `PolicyDecision`;
- a recorded transform such as a `RedactionReceipt`;
- review and release state; and
- a correction and rollback target.

The exact transform parameters belong in accepted policy and review records, not in this README or an ad hoc config value.

### Reconstruction risk

Review the resulting product for clues that may reconstruct a protected location, including:

- precise coordinates, small polygons, or high-resolution rasters;
- collector numbers, accession identifiers, locality strings, route descriptions, or landmark names;
- exact observation dates combined with photographs or phenology;
- habitat, soil, hydrology, parcel, ownership, road, trail, or infrastructure joins;
- repeated generalized points whose overlap reveals the source location;
- low-count summaries, unique taxa, or tiny population envelopes;
- cache keys, debug logs, filenames, error messages, or telemetry; and
- map zoom, hover, query, export, or tile attributes.

A benign input can become sensitive after a join. The output inherits the strongest applicable sensitivity until reviewed.

### Cultural and medicinal knowledge

Configuration cannot decide that cultural, traditional, medicinal, ceremonial, or stewardship knowledge is public.

Future consumers must:

- preserve the stated authority and provenance of cultural information;
- distinguish public published knowledge from restricted or relationship-bound knowledge;
- avoid inferring affiliation, consent, ownership, or permission;
- deny or hold ambiguous use;
- preserve attribution and restrictions; and
- route consequential use to the appropriate human review.

### Permitted profile selection

A configuration may reference an already-governed profile for:

- suppression or withholding;
- county, watershed, ecoregion, or grid generalization;
- constrained buffering or jitter;
- delayed publication;
- steward-only exact access;
- low-count suppression;
- field allowlisting; or
- review routing.

The profile identifier is not proof that the profile exists, applies, passed review, or produced a valid receipt. The consumer must resolve and validate it.

[Back to top](#top)

---

## Validation

### Documentation checks

For this README:

- one H1 is present;
- headings and quick-link anchors are coherent;
- code fences and tables are balanced;
- relative links resolve against the repository layout;
- the KFM Meta Block remains structurally consistent;
- no secrets, private endpoints, real occurrence data, or protected-location clues are present; and
- the final newline is preserved.

### Future payload checks

A future configuration payload requires deterministic checks for:

1. **Parsing** — accepted encoding, syntax, format version, and duplicate-key behavior.
2. **Shape** — canonical schema or contract validation.
3. **Consumer binding** — exact consumer, owner, parser, and supported version.
4. **Unknown keys** — rejected or held, especially for safety-relevant fields.
5. **Precedence** — deterministic merge and override order.
6. **Taxonomy** — authority identifiers, crosswalks, synonym conflicts, and unresolved identities.
7. **Source roles** — authority, observation, restricted, context, model, and derived roles do not collapse.
8. **Object roles** — specimen, occurrence, range, model, aggregate, candidate, and cultural context remain distinct.
9. **Temporal semantics** — required time kinds remain distinct and correctly ordered where applicable.
10. **Rights** — license, attribution, redistribution, access, and derivative-use requirements resolve.
11. **Cultural review** — required authority, consent, and restriction checks resolve without inference.
12. **Sensitivity** — exact-location, low-count, join-induced, and reconstruction risks fail closed.
13. **Profile resolution** — taxonomy, rights, sensitivity, display, stale-state, and review profiles exist and are applicable.
14. **Secrets and private values** — credentials, signed URLs, private paths, and sensitive identifiers are absent.
15. **No-network fixtures** — validation and negative cases do not depend on live sources.
16. **Negative cases** — malformed, unknown, stale, conflicting, held, denied, abstained, and error cases are exercised.
17. **Migration and rollback** — prior versions, deactivation, correction, and restoration are tested.
18. **No implicit activation** — file presence alone does not activate a source, watcher, layer, route, release, or publication state.

### What validation does not prove

A passing parser or schema check does not prove:

- source rights;
- cultural authority or consent;
- taxonomic correctness;
- observational truth;
- sensitivity clearance;
- evidence closure;
- release readiness;
- public safety;
- runtime consumption; or
- KFM publication.

[Back to top](#top)

---

## Failure behavior

| Condition | Expected safe disposition |
|---|---|
| Valid, authorized, non-sensitive configuration | `PASS` for internal validation; continue to ordinary governed processing. |
| Malformed file, unsupported version, or contract violation | `FAIL` or `ERROR`; do not partially apply. |
| Unknown taxon or unresolved taxonomy/crosswalk conflict | `HOLD` or `ABSTAIN`; preserve competing identities. |
| Missing source role, rights, cultural authority, policy, review, or transform authority | `HOLD`, `DENY`, or `ABSTAIN`; do not infer permission. |
| Exact sensitive occurrence or reconstructable locality requested for public use | `DENY` by default. |
| Modeled range, distribution surface, or candidate presented as observed fact | `FAIL` and `ABSTAIN`; preserve the original evidence role. |
| Specimen status asserted without voucher evidence | `FAIL` or `HOLD`; do not upgrade occurrence evidence. |
| Join creates higher sensitivity than the inputs | `HOLD` or `DENY` until the resulting product is reviewed. |
| Missing or stale evidence with no released alternative | `ABSTAIN`; do not substitute a model or cache silently. |
| Unauthorized sensitivity reduction or bypass key | `FAIL` and `DENY`; record the reason without exposing protected values. |
| Source outage or incomplete data | Preserve stale or partial state explicitly; do not fabricate completeness. |
| Consumer cannot determine precedence | `ERROR` or `HOLD`; do not merge unpredictably. |

`PASS` and `FAIL` are validator outcomes, not publication decisions. A valid config still requires evidence, policy, review, and release support for consequential outputs.

[Back to top](#top)

---

## Review burden

README changes require:

- configuration or documentation review; and
- Flora domain review.

A future payload also requires the applicable:

- named consumer owner;
- taxonomy or herbarium-data reviewer;
- source and rights reviewer;
- sensitivity and geoprivacy reviewer;
- cultural or stewardship reviewer where relevant;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer; and
- policy and release reviewer.

Do not infer acceptance from a missing reviewer rule or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Maintenance

When a Flora configuration file is added or changed:

1. identify the exact consumer and owner;
2. re-read the parent config contract and Flora doctrine;
3. verify the canonical contract, schema, policy, taxonomy, and source references;
4. preserve specimen, occurrence, range, model, candidate, and context separation;
5. preserve source-role, temporal, rights, and cultural-authority boundaries;
6. review exact-location, low-count, join-induced, reconstruction, and personal-data risk;
7. run deterministic parse, shape, semantic, negative, and no-network checks;
8. document precedence, unknown-key behavior, stale-state handling, migration, and rollback;
9. inspect the complete diff for secrets and protected clues;
10. verify remote read-back and changed paths; and
11. keep release and publication as separate governed decisions.

### Definition of done for the first payload

- [ ] A named consumer and accepted owners are verified.
- [ ] The file format, version, parser, and load path are verified.
- [ ] Canonical schema or contract references resolve.
- [ ] Taxonomy, specimen, occurrence, range, model, temporal, and source-role semantics are explicit.
- [ ] Rights, attribution, redistribution, cultural authority, and steward restrictions are reviewed.
- [ ] Sensitivity and geoprivacy parameters come from accepted policy, not the config file.
- [ ] Join-induced sensitivity and reconstruction risks are covered.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, and error cases.
- [ ] No-network tests pass.
- [ ] Secret and protected-location scans pass.
- [ ] Precedence, unknown-key, migration, deactivation, correction, and rollback behavior are tested.
- [ ] No source, watcher, public layer, release, or publication is activated by file presence.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/flora/README.md`](../../../docs/domains/flora/README.md) — Flora doctrine, source roles, sensitivity, and lifecycle posture.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved repository drift and authority conflicts.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value handling.

Future files should link to verified Flora contracts, schemas, policies, source descriptors, tests, fixtures, receipts, proofs, and release records only after those exact paths and authority relationships are confirmed.

[Back to top](#top)

---

## ADRs

No ADR is introduced by this README.

Separate governance is required for changes that would:

- add, rename, merge, or retire a canonical domain slug;
- select a canonical plant taxonomy, nomenclature authority, or crosswalk-conflict policy;
- define or alter sensitivity tiers, cultural-authority rules, or geoprivacy parameters;
- decide source rights, source-role authority, or live-source activation;
- create a parallel contract, schema, policy, registry, taxonomy, receipt, proof, or release authority;
- establish universal config discovery, precedence, or unknown-key behavior;
- authorize direct public access to internal or canonical stores; or
- change the separation among configuration, review, evidence, release, correction, and publication.

Configuration must not be used to settle those decisions indirectly.

[Back to top](#top)

---

## Rollback and correction

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request that restores the prior known-good README or configuration version. Do not force-push or rewrite shared history.

For a future payload correction:

1. disable or stop selecting the affected configuration through the verified consumer mechanism;
2. stop any watcher or scheduled consumer that depends on the faulty selection;
3. preserve the faulty version and evidence needed for review;
4. identify affected objects, joins, derivatives, caches, tiles, exports, and narratives without exposing protected locations;
5. assess whether exact or reconstructable sensitive information was exposed;
6. restore the prior known-good version;
7. re-run validation and negative cases;
8. create any required correction, redaction, withdrawal, release, or rollback records in their canonical homes; and
9. verify that no public surface continues to serve an unauthorized, stale, or reconstructable derivative.

A Git revert does not itself revoke exposed data, correct released artifacts, or establish KFM publication lineage.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**, against `main@367210cb4377c741a3c84730261bff965a102b9c`.

Review again before the first non-README payload, consumer binding, taxonomy-profile selection, cultural-review profile, sensitivity/geoprivacy-profile selection, source or watcher activation, or public-output integration.
