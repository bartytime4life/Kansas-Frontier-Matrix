<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-fauna-readme
title: configs/domains/fauna/ — Fauna Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Fauna steward · Sensitivity steward · Consumer owner
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; fauna; deny-by-default; geoprivacy-aware; source-role-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/fauna/README.md
truth_posture: CONFIRMED canonical fauna slug, repository-present parent config contract, repository-present Fauna doctrine, T4 sensitive-occurrence default, exact-location denial, and documentation-only lane / PROPOSED future consumer-bound templates / UNKNOWN consumers, precedence, loader behavior, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, taxonomy resolver, geoprivacy parameters, and runtime binding
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only. It does not create, load, activate, expose, or publish a Fauna configuration payload."
  - "v0.2 expands the Fauna-specific taxonomy, source-role, geoprivacy, sensitive-site, validation, correction, and rollback contract without creating a new policy, schema, registry, redaction, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Domain Configuration

`configs/domains/fauna/`

> Safe-to-commit, Fauna-specific configuration documentation and future consumer-bound templates. This lane does not own taxonomic truth, occurrence truth, source admission, geoprivacy, sensitivity, evidence, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Repository fit](#repository-fit) · [Inputs](#inputs) · [Outputs](#outputs) · [Configuration contract](#minimum-configuration-contract) · [Taxonomy and source roles](#taxonomy-occurrence-and-source-role-boundaries) · [Geoprivacy](#geoprivacy-sensitive-sites-and-public-safety) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Review](#review-burden) · [Maintenance](#maintenance) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Component maturity:** documentation boundary only  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no Fauna payload, loader, consumer binding, source activation, geoprivacy transform, or public exposure is established by this README

> [!CAUTION]
> Exact or reconstructable sensitive occurrences, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry paths, steward-controlled records, and private-person details fail closed. Directory presence, a future configuration file, or a parsed value must never lower sensitivity, convert restricted records into public records, bypass steward review, activate a source, authorize a transform, promote lifecycle state, approve release, or create KFM publication.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Fauna lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should behave, but they cannot decide:

- which taxonomy or taxon identity is controlling;
- whether an occurrence is observed, inferred, modeled, aggregated, or restricted;
- whether a source is authoritative, admissible, licensed, or active;
- whether exact or generalized geometry may be exposed;
- whether a geoprivacy transform is sufficient;
- whether evidence supports a claim; or
- whether an artifact may be promoted, released, or published.

This README is intended for:

- Fauna domain stewards;
- configuration and developer-experience maintainers;
- taxonomy, sensitivity, geoprivacy, rights, policy, security, and release reviewers;
- package, pipeline, app, runtime, test, and tooling owners that may consume Fauna configuration; and
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Fauna domain meaning | **None.** Domain doctrine remains in [`docs/domains/fauna/`](../../../docs/domains/fauna/README.md). |
| Taxonomic identity and conservation or legal status | **None.** Configuration cannot select an authority by convenience or resolve a taxonomic conflict as truth. |
| Occurrence status | **None.** A value cannot convert a model, range, candidate, aggregation, or context layer into an observed occurrence. |
| Source identity, role, rights, cadence, and activation | **None.** These require the applicable source registry, connector, policy, rights, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Sensitivity or geoprivacy decision | **None.** A value may select an already-governed profile; it cannot create, weaken, or approve a sensitivity rule or transform. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority through repetition, proximity, successful parsing, operational convenience, or use by a map or AI surface.

[Back to top](#top)

---

## Status

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `fauna` is a repository-present canonical domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Fauna doctrine | **CONFIRMED repository-present** | The domain README establishes deny-by-default sensitive-location handling and source-role separation. |
| Sensitive occurrence default | **CONFIRMED doctrine** | Exact sensitive occurrences and sensitive sites default to T4 and public exact-location release is denied. |
| Current lane content | **README ONLY** | This lane establishes documentation, not executable configuration. |
| Consumer and loader | **UNKNOWN** | No consumer, parser, discovery mechanism, merge order, or unknown-key behavior is established here. |
| Taxonomy resolver | **NEEDS VERIFICATION** | The controlling resolver and crosswalk-conflict procedure require a governed decision. |
| Geoprivacy parameters | **NEEDS VERIFICATION** | Radius, fuzzing, aggregation, withholding, and tier-motion parameters must come from policy and steward review. |
| Validation and CI enforcement | **NEEDS VERIFICATION** | Expectations are documented; executable enforcement is not proven by this README. |
| Runtime, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, release, or publication. |

Directory presence must not trigger discovery, source activation, network access, indexing, map-layer creation, AI interpretation, geometry exposure, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, Fauna-specific configuration material for a named or explicitly proposed consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define the configuration boundary. | Preserve taxonomy, source-role, geoprivacy, evidence, policy, review, and release controls. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified consumer. | Parseable, versioned, consumer-bound, synthetic, no secrets, no live binding. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Fictional identifiers and geometry; clearly non-operational; no automatic discovery. |
| Conservative review defaults | Select an existing deny, hold, abstain, redact, generalize, or steward-review profile. | Cannot reduce policy or review burden. |
| Public-safe display hints | Select a verified generalized display profile. | Must not contain protected geometry or grant exposure. |
| Migration notes | Document a real key or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |

Synthetic examples must not resemble a real occurrence, observer, nest, den, roost, hibernaculum, spawning site, migration path, telemetry track, parcel, or protected location closely enough to enable reconstruction.

### What does not belong here

- real occurrences, observations, surveys, telemetry, tracking data, eDNA records, acoustic records, mortality records, disease records, invasive-species records, or source payloads;
- exact or reconstructable nests, dens, roosts, hibernacula, spawning sites, breeding sites, migration routes, or other sensitive geometry;
- observer, researcher, volunteer, landowner, permit-holder, or other living-person information;
- rights-restricted media, media metadata, collection details, access-control detail, or steward-controlled records;
- credentials, tokens, connection strings, private endpoints, workstation paths, or live deployment bindings;
- source admission, activation, authority-role, cadence, rights, license, or redistribution decisions;
- taxonomy authority, crosswalk resolution, conservation status, legal status, or synonym adjudication;
- schemas, contracts, policy, registries, receipts, proofs, manifests, release records, correction records, or publication decisions;
- values that present modeled range, habitat suitability, candidate detections, inferred presence, or contextual joins as observed occurrence truth;
- values that allow an aggregator to stand in as legal-status or conservation authority;
- hidden bypasses for sensitivity, geoprivacy, redaction, review, deny, abstain, quarantine, or release gates; or
- auto-discovery behavior based only on directory or filename presence.

### Explicit non-ownership

This lane may reference verified outputs from other responsibility roots, but it must not redefine them. It does not own:

- habitat patches, suitability surfaces, or habitat assignment;
- plant records or plant-sensitive locations;
- water, soil, agricultural, road, land, title, or living-person truth;
- source descriptors, connector behavior, rights decisions, or source activation;
- Fauna contracts, schemas, sensitivity policy, or validation rules;
- `EvidenceBundle`, `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, release, proof, or rollback objects; or
- lifecycle records under RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED.

[Back to top](#top)

---

## Repository fit

This directory is a child of the canonical domain-configuration boundary:

```text
configs/
└── domains/
    ├── README.md
    └── fauna/
        └── README.md
```

The responsibility split is:

- [`configs/`](../../README.md): repository-wide safe configuration boundary;
- [`configs/domains/`](../README.md): common rules for domain-scoped defaults and templates;
- `configs/domains/fauna/`: Fauna-specific configuration support;
- [`docs/domains/fauna/`](../../../docs/domains/fauna/README.md): Fauna doctrine, terms, object families, source roles, sensitivity, and lifecycle expectations;
- `contracts/domains/fauna/`: semantic object meaning when verified;
- `schemas/contracts/v1/domains/fauna/`: machine-checkable shape when verified;
- `policy/domains/fauna/` and `policy/sensitivity/fauna/`: admissibility and sensitivity decisions when verified;
- `data/registry/sources/fauna/`: source identities and activation posture when verified; and
- tests, fixtures, pipelines, receipts, proofs, catalogs, release candidates, and published artifacts: their own responsibility roots.

This README must link to those authorities rather than copying their normative content into configuration.

[Back to top](#top)

---

## Inputs

A future Fauna configuration payload requires all of the following before it may be treated as consumer-ready:

1. **Named consumer** — exact package, app, pipeline, service, runtime, test harness, or tool.
2. **Declared format** — file type, format version, and canonical parser.
3. **Authority references** — verified contract, schema, policy, source registry, and domain documentation as applicable.
4. **Synthetic or non-sensitive values** — no real occurrence, location, person, telemetry, media, or source payload.
5. **Source-role model** — authority, observation, aggregator, context, model, and candidate roles remain distinguishable.
6. **Taxonomy posture** — resolver, vocabulary version, synonym behavior, unresolved conflict behavior, and update cadence are explicit.
7. **Temporal posture** — observation, event, valid, ingestion, update, expiry, and correction times are defined where applicable.
8. **Sensitivity and geoprivacy review** — protected taxa, sensitive sites, exact geometry, private joins, and reconstruction risk are reviewed.
9. **Rights review** — provider terms, attribution, redistribution, media, and steward restrictions are verified.
10. **Validation path** — deterministic parsing, schema checks, semantic checks, no-network fixtures, negative tests, and expected finite outcomes.
11. **Precedence rule** — interaction with repository defaults, environment settings, local overrides, deployment configuration, and runtime values is explicit.
12. **Rollback and correction** — prior version, deactivation, migration, correction, and rollback behavior are named.

A missing requirement leaves the payload **PROPOSED** or **NEEDS VERIFICATION**. It does not become active by convention.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future validated file may support a verified consumer by selecting conservative, already-governed behavior such as:

- a named taxonomy crosswalk profile;
- a source-role mapping profile;
- a deny, hold, abstain, quarantine, or steward-review route;
- a public-safe generalization or display profile;
- freshness and stale-state handling;
- a field allowlist for an already-approved public derivative; or
- a migration compatibility window.

A configuration output cannot:

- admit or activate a source;
- create taxonomic, occurrence, legal-status, or conservation-status truth;
- create or approve a geoprivacy transform;
- emit a valid `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, or `ReleaseManifest` merely by naming one;
- reveal a sensitive site or lower a sensitivity tier;
- write lifecycle data directly to a later phase;
- authorize a public layer, API response, map display, AI answer, release, or publication.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file should document or carry the following information in the repository-approved form.

| Field | Required meaning |
|---|---|
| Consumer | Exact component that reads the file. |
| Owner | Accountable component and domain owner; no invented team. |
| Format version | Version of the configuration shape. |
| Contract or schema reference | Canonical machine or semantic authority, when verified. |
| Domain | `fauna`; a config file cannot create a new domain alias. |
| Source roles | Allowed role vocabulary and non-collapse rules. |
| Taxonomy profile | Resolver and crosswalk profile by stable identifier, not embedded authority data. |
| Sensitivity profile | Stable reference to governed policy; not an inline policy substitute. |
| Public-safe profile | Stable reference to an approved transform or release profile. |
| Temporal semantics | Applicable times, timezone, freshness, and expiry behavior. |
| Unknown-key behavior | Reject, warn, or ignore; must be explicit and tested. |
| Precedence | Exact merge and override order for the named consumer. |
| Network posture | No network by default unless the consumer and security review explicitly authorize it. |
| Failure posture | Finite fail-closed outcomes for missing, malformed, stale, conflicting, or unauthorized input. |
| Validation | Parser, schema, semantic, sensitivity, rights, and negative-case checks. |
| Migration | Deprecated keys, compatibility window, replacement, and correction path. |
| Rollback | Prior known-good version and consumer deactivation method. |

Do not add schema-invalid placeholders to a machine-parsed file. Keep unresolved ownership or authority outside the payload until the repository supplies an approved sentinel or value.

[Back to top](#top)

---

## Taxonomy, occurrence, and source-role boundaries

Fauna configuration must preserve the distinction among meaning, evidence, source role, and display.

### Taxonomy

- A taxon identifier must retain its authority and vocabulary version.
- A synonym, crosswalk, or inferred match is not automatically a canonical identity.
- Conflicting authority taxonomies must remain visible and follow a governed conflict procedure.
- Configuration may select a verified crosswalk profile; it must not embed an unofficial replacement taxonomy.
- The controlling resolver and conflict policy remain **NEEDS VERIFICATION** until accepted repository evidence resolves them.

### Occurrence classes

- `OccurrenceEvidence` is source-bound evidence before sensitivity disposition.
- `OccurrenceRestricted` remains restricted and fails closed for public exact-location use.
- `OccurrencePublic` is a public-safe derivative after required policy, review, transformation, evidence, and release gates.
- `RangePolygon`, `SeasonalRange`, and `MigrationRoute` are scoped spatial products, not substitutes for direct occurrence evidence.
- A candidate detection, habitat model, range model, inferred presence, environmental association, or AI interpretation is not an observed occurrence.

### Source roles

| Role | Configuration-safe treatment |
|---|---|
| Authority | May be referenced only through a verified source identity and authority scope. |
| Observation | Preserves observation method, time, source, uncertainty, and sensitivity. |
| Aggregator | Preserves upstream source and record-level restrictions; cannot become legal-status authority by aggregation. |
| Context | Supports interpretation but cannot confirm occurrence, identity, or legal status. |
| Model | Remains modeled output with method, version, uncertainty, and valid scope. |
| Candidate | Remains unconfirmed and must not be promoted by a display or scoring threshold alone. |

Configuration must never collapse these roles into a generic `trusted` or `verified` flag.

[Back to top](#top)

---

## Geoprivacy, sensitive sites, and public safety

The Fauna doctrine establishes exact sensitive occurrences and sensitive sites as deny-by-default.

### Protected material

The following must be treated as restricted unless governing evidence proves a safer release posture:

- sensitive-taxon occurrence geometry;
- nests, dens, roosts, hibernacula, spawning sites, breeding sites, congregation sites, and nursery areas;
- telemetry and tracking paths;
- steward-controlled or embargoed records;
- observer and private-land details;
- vulnerable collection, rescue, rehabilitation, mortality, or disease locations; and
- attributes or combinations that allow location reconstruction.

### Tier motion

- Sensitive occurrence defaults to **T4** under the repository-present Fauna doctrine.
- Public exact sensitive-occurrence tiles are denied.
- A T4 record does not become public because a configuration value requests a lower tier.
- The doctrine describes T4-to-public movement only through governed geoprivacy or generalization plus the required `RedactionReceipt`, `ReviewRecord`, and `PolicyDecision`.
- Configuration may reference an approved transform profile after those authority surfaces exist; configuration cannot define the transform, approve it, or issue its receipts.
- Exact generalization radius, fuzzing distribution, withholding rules, aggregation thresholds, and tier-transition parameters remain **NEEDS VERIFICATION** and must not be guessed here.

### Reconstruction resistance

Validation must consider not only direct coordinates but also:

- timestamps combined with routes or observer histories;
- media EXIF or filenames;
- small-area counts or rare-taxon labels;
- parcel, facility, trail, water-body, or habitat joins;
- low zoom or tile boundaries that reveal a small source set;
- stable identifiers that can be joined to an external exact record; and
- cache, log, error, analytics, or debugging output.

When public safety cannot be established, the consumer must deny, hold, abstain, generalize through governed policy, or omit the field. It must not silently expose the value.

[Back to top](#top)

---

## Security, rights, and network posture

- Real credentials, tokens, cookies, API keys, signed URLs, private endpoints, or account identifiers must not be committed.
- A template may name an environment variable only when the consumer and repository convention verify that name.
- Rights, license, attribution, redistribution, media-use, and steward restrictions must be resolved in source authority surfaces, not inferred from public accessibility.
- Configuration must not automatically activate a live wildlife source or network call.
- No-network fixtures are the default validation surface for a new payload.
- Live-source testing, when separately authorized, must be isolated from normal deterministic tests and must not record sensitive payloads.
- Logs, errors, receipts, screenshots, support bundles, and test output must not expose protected locations or personal information.

[Back to top](#top)

---

## Validation

### Documentation validation

For this README:

- one H1 is present;
- headings are ordered and linkable;
- relative links remain inside known responsibility roots;
- the KFM metadata block retains its existing `doc_id` and `created` value;
- no real occurrence, person, media, telemetry, source, credential, or protected-location data is included; and
- doctrine, current repository state, proposals, unknowns, and verification needs remain distinct.

### Future payload validation

A future payload is not ready until applicable checks pass.

| Validation layer | Required checks |
|---|---|
| Parse | File parses under the declared format and encoding. |
| Shape | Schema or approved contract reference validates every field. |
| Consumer binding | Named consumer, supported filename, version, and load path are verified. |
| Unknown keys | Behavior is explicit and covered by negative tests. |
| Precedence | Merge and override behavior is deterministic and tested. |
| Taxonomy | Authority, vocabulary version, crosswalk, synonyms, and conflict behavior remain explicit. |
| Source roles | Authority, observation, aggregator, context, model, and candidate roles do not collapse. |
| Occurrence split | Restricted and public derivatives remain separate; modeled or range data does not become observation. |
| Sensitivity | T4 records and protected sites fail closed; policy references resolve. |
| Geoprivacy | Any selected profile is governed, versioned, reviewable, and incapable of lowering protections by local override. |
| Rights | Provider, steward, attribution, media, redistribution, and private-person constraints resolve. |
| Reconstruction | Direct and indirect protected-location clues are absent from commit-safe content and public output. |
| Temporal | Times, freshness, expiry, corrections, and seasonal scope are explicit. |
| Network | Deterministic tests use no live network; any authorized live test is separate and redacted. |
| Secrets | No credential or private endpoint is present. |
| Rollback | Prior configuration and deactivation behavior are documented and tested where applicable. |

Executable configuration validation remains **NOT APPLICABLE** while this lane contains no payload and no verified consumer.

### Negative cases

At minimum, future tests should cover:

- unknown taxon or unresolved taxonomy conflict;
- aggregator presented as legal-status authority;
- model or range product presented as an observation;
- candidate promoted without confirmation evidence;
- restricted occurrence routed to a public profile;
- missing or invalid policy, review, receipt, or release reference;
- real or reconstructable protected geometry in an example;
- observer, landowner, telemetry, or media metadata leakage;
- stale, partial, unavailable, or superseded source state;
- malformed file, unknown key, unsupported version, or ambiguous precedence; and
- missing rollback target.

[Back to top](#top)

---

## Failure behavior

A verified consumer must use finite, reason-coded, fail-closed outcomes. The exact implementation remains **PROPOSED** until code and tests confirm it.

| Condition | Expected safe disposition |
|---|---|
| Valid, authorized, non-sensitive configuration | `PASS` for internal validation; continue to ordinary governed processing. |
| Malformed file, unsupported version, or contract violation | `FAIL` or `ERROR`; do not partially apply. |
| Unknown taxonomy or unresolved crosswalk conflict | `HOLD` or `ABSTAIN`; preserve competing identities. |
| Missing source role, rights, policy, review, or transform authority | `HOLD`, `DENY`, or `ABSTAIN`; do not infer permission. |
| Exact sensitive occurrence or site requested for public use | `DENY` by default. |
| Missing or stale evidence with no released alternative | `ABSTAIN`; do not substitute a model or cache silently. |
| Unauthorized sensitivity reduction or bypass key | `FAIL` and `DENY`; record the reason without exposing sensitive values. |
| Source outage or incomplete data | Preserve stale or partial state explicitly; do not fabricate completeness. |
| Consumer cannot determine precedence | `ERROR` or `HOLD`; do not merge unpredictably. |

`PASS` and `FAIL` are validator outcomes, not publication decisions. A valid config still requires evidence, policy, review, and release support for consequential outputs.

[Back to top](#top)

---

## Review burden

README changes require:

- config or documentation review; and
- Fauna domain review.

A future payload also requires the applicable:

- named consumer owner;
- taxonomy reviewer;
- source and rights reviewer;
- sensitivity and geoprivacy reviewer;
- steward or rights-holder review where protected records are implicated;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer; and
- policy and release reviewer.

Do not infer acceptance from a missing reviewer rule or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Maintenance

When a Fauna configuration file is added or changed:

1. identify the exact consumer and owner;
2. re-read the parent config contract and Fauna doctrine;
3. verify the canonical contract, schema, policy, and source references;
4. preserve source-role and restricted/public occurrence separation;
5. review taxonomy, rights, sensitivity, geoprivacy, reconstruction, and personal-data risk;
6. run deterministic parse, shape, semantic, negative, and no-network checks;
7. document precedence, unknown-key behavior, stale-state handling, migration, and rollback;
8. inspect the complete diff for secrets and protected clues;
9. verify remote read-back and changed paths; and
10. keep release and publication as separate governed decisions.

### Definition of done for the first payload

- [ ] A named consumer and accepted owners are verified.
- [ ] The file format, version, parser, and load path are verified.
- [ ] Canonical schema or contract references resolve.
- [ ] Source-role, taxonomy, occurrence, temporal, and sensitivity semantics are explicit.
- [ ] Geoprivacy parameters come from accepted policy, not the config file.
- [ ] Rights and steward restrictions are reviewed.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, and error cases.
- [ ] No-network tests pass.
- [ ] Secret and reconstruction-risk scans pass.
- [ ] Precedence, unknown-key, migration, deactivation, correction, and rollback behavior are tested.
- [ ] No source, public layer, release, or publication is activated by file presence.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/fauna/README.md`](../../../docs/domains/fauna/README.md) — Fauna doctrine and sensitivity posture.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved repository drift and authority conflicts.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value handling.

Future files should link to verified Fauna contracts, schemas, policies, source descriptors, tests, fixtures, receipts, proofs, and release records only after those exact paths and authority relationships are confirmed.

[Back to top](#top)

---

## ADRs

No ADR is introduced by this README.

Separate governance is required for changes that would:

- add, rename, merge, or retire a canonical domain slug;
- select a canonical taxonomy resolver or crosswalk-conflict policy;
- define or alter sensitivity tiers or geoprivacy parameters;
- create a parallel contract, schema, policy, registry, receipt, proof, or release authority;
- establish universal config discovery, precedence, or unknown-key behavior;
- authorize direct public access to internal or canonical stores; or
- change the separation among configuration, review, evidence, release, and publication.

Configuration must not be used to settle those decisions indirectly.

[Back to top](#top)

---

## Rollback and correction

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request that restores the prior known-good README or configuration version. Do not force-push or rewrite shared history.

For a future payload correction:

1. disable or stop selecting the affected configuration through the verified consumer mechanism;
2. preserve the faulty version and evidence needed for review;
3. identify affected outputs and caches without exposing protected locations;
4. restore the prior known-good version;
5. re-run validation and negative cases;
6. create any required correction, redaction, withdrawal, release, or rollback records in their canonical homes; and
7. verify that no public surface continues to serve an unauthorized or reconstructable derivative.

A Git revert does not itself revoke exposed data, correct released artifacts, or establish KFM publication lineage.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**, against `main@e5686326d2c0922e4d3830e2d53390877eaa1690`.

Review again before the first non-README payload, consumer binding, taxonomy-profile selection, geoprivacy-profile selection, source activation, or public-output integration.
