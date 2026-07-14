<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-habitat-readme
title: configs/domains/habitat/ — Habitat Configuration Boundary
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Config steward · Habitat steward · Sensitivity/geoprivacy steward · Consumer owner · Validation steward
created: 2026-06-16
updated: 2026-07-13
policy_label: public; config-sublane; habitat; landscape-not-species; source-role-aware; model-aware; geoprivacy-aware; deny-by-default; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/habitat/README.md
truth_posture: CONFIRMED canonical habitat slug, repository-present parent config contract, repository-present Habitat doctrine, seven source-role classes, landscape-not-species boundary, modeled-versus-regulatory anti-collapse rule, sensitive-join fail-closed posture, README plus non-semantic .gitkeep inventory, and documentation-only lane / CONFLICTED Directory-Rules segment form versus Atlas flat-form navigation / PROPOSED future consumer-bound templates and governed profile selectors / UNKNOWN consumers, precedence, loader behavior, deployment binding, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, accepted policy profiles, geoprivacy parameters, model fitness, and runtime binding
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: e223451fd0852beea79c3cfa0235e1231746dd4f
  prior_blob: 1fbe41b16962e414b2589be443e9939a7bf6d026
  lane_inventory:
    - README.md
    - .gitkeep
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../packages/domains/habitat/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains README.md and an empty .gitkeep only. The .gitkeep is non-semantic and does not establish a configuration payload, consumer, loader, or activation path."
  - "A bounded repository search for configs/domains/habitat returned this README and documentation references, but no indexed executable consumer. This is bounded evidence, not proof that no differently named or unindexed consumer exists."
  - "v0.3 preserves the strong v0.2 no-secrets, sensitivity, source-role, anti-bypass, migration, correction, and rollback controls while grounding current inventory and adding an explicit minimum per-file contract, temporal/model semantics, finite failure behavior, and definition of done."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Domain Configuration

`configs/domains/habitat/`

> Safe-to-commit, Habitat-specific configuration documentation and future consumer-bound templates. This lane does not own habitat truth, species truth, source admission, policy, geoprivacy, evidence, lifecycle state, release, or publication.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Repository fit](#repository-fit) · [Inputs](#inputs) · [Outputs](#outputs) · [File contract](#minimum-configuration-contract) · [Consumer binding](#consumer-binding-precedence-and-discovery) · [Semantic guardrails](#habitat-semantic-and-source-role-guardrails) · [Sensitivity](#sensitivity-geoprivacy-and-join-induced-risk) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Review](#review-burden) · [Maintenance](#maintenance-and-safe-change-pattern) · [Migration](#migration-and-anti-bypass-posture) · [Done](#definition-of-done-for-the-first-payload) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Rollback](#rollback-and-correction) · [Language](#safe-language-rules)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.3`  
> **Observed lane maturity:** `README.md` plus a non-semantic empty `.gitkeep`; no executable Habitat configuration payload is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no Habitat payload, loader, consumer binding, source activation, model execution, public-safe transform, map exposure, release, or publication is established by this README

> [!CAUTION]
> Habitat owns landscape, not species. A modeled suitability surface is not a regulatory critical-habitat designation, a habitat patch is not a species occurrence, and a configuration value is not a policy or release decision. Exact or reconstructable sensitive habitat and occurrence-linked context fails closed.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Habitat lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should behave, but they cannot decide:

- whether a landscape feature is an observation, regulatory designation, modeled product, aggregate, administrative record, candidate, or synthetic fixture;
- whether a habitat patch, ecological system, suitability surface, corridor, restoration opportunity, or stewardship zone is true;
- whether a Fauna or Flora occurrence may be joined to Habitat or publicly exposed;
- whether a source is authoritative, admissible, licensed, or active;
- whether a geometry is public-safe;
- whether a model is fit for a particular use;
- whether evidence supports a claim; or
- whether an artifact may be promoted, released, or published.

This README is intended for:

- Habitat domain stewards;
- configuration and developer-experience maintainers;
- source-role, model, sensitivity, geoprivacy, rights, policy, security, and release reviewers;
- package, pipeline, app, runtime, test, watcher, connector, and tooling owners that may consume Habitat configuration; and
- reviewers checking Directory Rules placement and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Habitat domain meaning | **None.** Domain doctrine remains in [`docs/domains/habitat/`](../../../docs/domains/habitat/README.md). |
| Habitat object meaning | **None.** `HabitatPatch`, `SuitabilityModel`, `Corridor`, and related semantics belong to verified contracts. |
| Species occurrence or taxonomic truth | **None.** Fauna and Flora own their respective occurrences and taxa. Habitat may use governed context joins only. |
| Regulatory designation | **None.** Configuration cannot create, alter, or imply a critical-habitat or other regulatory designation. |
| Model or observation truth | **None.** Configuration cannot convert modeled, candidate, aggregate, administrative, or synthetic material into observed or regulatory truth. |
| Source identity, role, rights, cadence, and activation | **None.** These require the applicable source registry, connector, policy, rights, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Sensitivity or geoprivacy decision | **None.** A value may select an already-governed profile; it cannot create, weaken, or approve a sensitivity rule or transform. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority through repetition, proximity, successful parsing, operational convenience, or use by a map, dashboard, model, watcher, search index, Evidence Drawer, Focus Mode, or AI surface.

[Back to top](#top)

---

## Status

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `e223451fd0852beea79c3cfa0235e1231746dd4f` |
| Prior README blob | `1fbe41b16962e414b2589be443e9939a7bf6d026` |
| Current verified lane files | `README.md`, empty `.gitkeep` |

### Maturity matrix

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `habitat` is a repository-present canonical domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this path as a non-secret, non-authoritative configuration sublane. |
| Habitat doctrine | **CONFIRMED repository-present** | The domain README establishes landscape-not-species ownership, seven source roles, model/regulatory anti-collapse, and sensitive-join controls. |
| Current lane inventory | **CONFIRMED — README + `.gitkeep`** | The empty `.gitkeep` has no semantic or runtime effect. No executable payload is established. |
| Indexed executable consumer | **NOT FOUND IN BOUNDED SEARCH** | A repository search returned this README and documentation references, not executable consumption. Differently named or unindexed consumers remain `UNKNOWN`. |
| Consumer and loader | **UNKNOWN** | No parser, auto-discovery mechanism, merge order, precedence, or unknown-key behavior is established here. |
| Source-role vocabulary | **CONFIRMED doctrine** | `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic` remain distinct. |
| Path form | **CONFLICTED / GOVERNED BY DIRECTORY RULES FOR THIS README** | Directory Rules uses the domain-segment form; an Atlas flat-form crosswalk remains a drift candidate. Configuration must not create both. |
| Source rights and terms | **NEEDS VERIFICATION** | Source-specific rights, attribution, redistribution, cadence, and access limits require verified source records. |
| Geoprivacy parameters | **NEEDS VERIFICATION** | Generalization, suppression, jitter, delay, aggregation, and restricted-view parameters must come from policy and steward review. |
| Model fitness and thresholds | **NEEDS VERIFICATION** | A threshold may configure a verified model; it cannot establish model validity or intended-use fitness. |
| Validation and CI enforcement | **NEEDS VERIFICATION** | Expectations are documented; substantive executable enforcement is not proven by this README. |
| Runtime, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, release, or publication. |

Directory presence must not trigger discovery, source activation, network access, model execution, indexing, geometry transformation, tile generation, map-layer creation, AI interpretation, lifecycle promotion, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only safe, non-secret, Habitat-specific configuration material for a named or explicitly proposed consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this configuration boundary. | Preserve non-authority, source-role, sensitivity, evidence, and release controls. |
| `.gitkeep` | Preserve a directory in Git when otherwise empty. | Non-semantic; never treated as configuration or activation evidence. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified Habitat consumer. | Parseable, versioned, consumer-bound, no secrets, no live binding. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Clearly synthetic values; impossible identifiers and geometry; no automatic activation. |
| Conservative review defaults | Select an existing hold, abstain, restrict, generalize, redact, or review profile. | Cannot weaken policy, source rights, evidence, or release burden. |
| Public-safe display profile selectors | Select an already-governed generalized display profile. | Cannot contain exact protected geometry or authorize exposure. |
| Model presentation hints | Configure labels, uncertainty display, version visibility, or caveat rendering. | Must not change source role, evidence status, or model fitness. |
| Migration notes | Document a real key, version, consumer, or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |
| Validation notes | Describe verified checks and expected finite outcomes. | Commands and workflows must resolve or remain labeled `PROPOSED` / `NEEDS VERIFICATION`. |

Synthetic examples must not resemble real sensitive habitat, occurrence locations, stewardship areas, private parcels, restoration sites, protected areas, critical assets, or low-count populations closely enough to support reconstruction.

### What does not belong here

- real Habitat source records, observations, ecological-system payloads, suitability outputs, corridors, restoration candidates, or lifecycle data;
- exact or reconstructable sensitive habitat, occurrence-linked habitat, rare-species context, breeding, nesting, denning, roosting, spawning, refuge, stewardship, restoration, protected-area, or private-land details;
- real Fauna or Flora occurrences, taxonomic records, specimens, or protected-location clues;
- credentials, tokens, private keys, cookies, signed URLs, private endpoints, workstation paths, internal deployment bindings, or environment-specific secrets;
- settings that label modeled habitat as regulatory critical habitat;
- settings that label suitability, connectivity, corridor, restoration, or candidate products as observations;
- settings that treat administrative stewardship or ownership context as habitat truth or land-title truth;
- settings that rely on map style filters, hidden fields, opacity, or client-side zoom alone to protect sensitive geometry;
- source admission, activation, cadence, rights, redistribution, or source-role decisions;
- schemas, contracts, policy, registries, receipts, proofs, evidence bundles, release records, correction notices, or publication decisions;
- package code, pipeline logic, connector code, watcher code, runtime adapters, infrastructure definitions, generated artifacts, caches, exports, screenshots, or reports.

### Explicit non-ownership

This lane does not own:

- animal taxa or occurrences — **Fauna**;
- plant taxa, specimens, or occurrences — **Flora**;
- soil objects — **Soil**;
- water observations or hydrologic truth — **Hydrology**;
- crop and field truth — **Agriculture**;
- hazard event and risk truth — **Hazards**;
- ownership, title, parcel, or living-person truth — **People/DNA/Land**;
- source registration, contract meaning, schema shape, policy, lifecycle objects, trust artifacts, release decisions, or public routes.

[Back to top](#top)

---

## Repository fit

```text
configs/
└── domains/
    ├── README.md
    └── habitat/
        ├── README.md
        └── .gitkeep
```

The responsibility split is:

- [`configs/`](../../README.md): repository-wide safe, non-secret configuration boundary;
- [`configs/domains/`](../README.md): common rules for domain-scoped defaults and templates;
- `configs/domains/habitat/`: Habitat-specific configuration support;
- [`docs/domains/habitat/`](../../../docs/domains/habitat/README.md): Habitat doctrine, ownership, object families, source roles, sensitivity, and lifecycle expectations;
- [`packages/domains/habitat/`](../../../packages/domains/habitat/README.md): proposed reusable implementation helpers, not configuration authority;
- contracts, schemas, policy, registries, connectors, pipelines, tests, fixtures, lifecycle data, receipts, proofs, catalogs, release records, and public applications: their own responsibility roots.

### Path-form conflict

Directory Rules uses domain segments such as:

```text
contracts/domains/habitat/
schemas/contracts/v1/domains/habitat/
policy/domains/habitat/
```

An Atlas navigation crosswalk also uses flatter forms. This README follows the Directory Rules segment form for links and placement. It does not create aliases, duplicate homes, or dual-write behavior. Final drift resolution remains an ADR or register concern.

[Back to top](#top)

---

## Inputs

A future Habitat configuration payload requires all of the following before it may be treated as implementation-supporting:

1. **Named consumer** — exact package, pipeline, app, runtime, connector, watcher, test harness, or tool.
2. **Declared format** — file type, format version, parser, and supported encoding.
3. **Verified authority references** — applicable contract, schema, policy, source registry, and Habitat doctrine.
4. **Source-role model** — explicit use of `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic` where relevant.
5. **Object and product class** — whether the consumer handles `HabitatPatch`, `LandCoverObservation`, `EcologicalSystem`, `SuitabilityModel`, `ConnectivityEdge`, `Corridor`, `Restoration Opportunity`, `StewardshipZone`, or another verified class.
6. **Spatial semantics** — CRS, resolution, scale, support, uncertainty, geometry class, and internal-versus-public-safe representation.
7. **Temporal semantics** — source, observed, valid/effective, snapshot, retrieval, run, release, expiry, supersession, and correction times where material.
8. **Rights and sensitivity review** — source terms, redistribution, geoprivacy, occurrence joins, private-land risk, low-count risk, and residual reconstruction risk.
9. **Model semantics** — model version, method, covariates, training or calibration context, intended use, limitations, and uncertainty display when modeled outputs are involved.
10. **Synthetic examples** — no real source records, sensitive geometry, people, parcels, or operational bindings.
11. **Deterministic validation** — parse, shape, semantic, negative, no-network, and stable-output checks.
12. **Precedence and unknown-key behavior** — explicit merge order, duplicate handling, override policy, and fail-closed behavior.
13. **Rollback and deactivation** — known-good prior version, disable path, migration behavior, and affected-output review.
14. **Accepted owners and reviewers** — consumer, Habitat, validation, rights/sensitivity, policy, security, and release roles as applicable.

A filename, path, or successful parse does not satisfy these requirements.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future file may provide validated input to a verified consumer. It cannot itself:

- admit or activate a source;
- execute a model;
- create a Habitat object;
- convert a source role;
- determine model fitness;
- establish public-safe geometry;
- create a geoprivacy or redaction receipt;
- promote lifecycle state;
- create an `EvidenceBundle`;
- approve a map layer, API response, or AI answer;
- authorize release or publication.

A consumer may emit a parse result, validation report, candidate record, or finite failure outcome in its own canonical responsibility lane. Those outputs do not belong here merely because the consumer read a file from this directory.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file should document these fields in the file itself or an adjacent verified manifest:

| Field | Requirement |
|---|---|
| `config_id` | Stable identifier that does not imply source, policy, or release authority. |
| `config_version` | Explicit version suitable for migration and rollback. |
| `format_version` | Version of the file shape or parser contract. |
| `intended_consumer` | Exact package, pipeline, app, runtime, connector, watcher, test, or tool. |
| `consumer_owner` | Accountable owner or `OWNER_TBD` with blocked activation. |
| `load_path` | Explicit discovery or invocation mechanism; never directory-presence inference. |
| `precedence` | Order relative to defaults, domain, dev, test, local, environment, deployment, and runtime settings. |
| `unknown_key_behavior` | Prefer reject; any ignore behavior must be intentional, tested, and documented. |
| `schema_ref` | Verified machine-shape authority, where applicable. |
| `contract_ref` | Verified semantic authority, where applicable. |
| `policy_refs` | Governing sensitivity, source-role, rights, model-use, and release profiles. |
| `source_role_profile` | Accepted role or role set; cannot upgrade source authority. |
| `spatial_profile` | CRS, scale, support, uncertainty, and public-safe geometry profile reference. |
| `temporal_profile` | Time-kind and freshness semantics. |
| `model_profile` | Model/version/method/fitness reference when modeled products are involved. |
| `sensitivity_profile` | Reference to a governed profile; not an inline redefinition. |
| `example_posture` | `synthetic`, `template`, or another explicit non-operational class. |
| `network_posture` | No-network by default for validation; live access separately governed. |
| `validation` | Commands, tests, negative cases, and expected outcomes. |
| `deactivation` | How the consumer stops selecting the file. |
| `rollback` | Prior known-good version and restoration procedure. |
| `status` | `PROPOSED`, `ACTIVE` only with evidence, `DEPRECATED`, `DISABLED`, or another governed finite state. |

Missing required metadata must produce `HOLD`, `FAIL`, `ERROR`, `ABSTAIN`, or `DENY` as appropriate. It must not trigger best-effort activation.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

No universal Habitat configuration loader is established by this README.

A verified consumer binding must identify:

- the exact file path;
- the parser and supported format version;
- whether loading is explicit, command-line, environment-selected, deployment-selected, or test-only;
- the precedence order;
- behavior for missing, duplicate, malformed, stale, unsupported, or unknown values;
- whether reload is supported and how partial application is prevented;
- deactivation and rollback behavior;
- logging and redaction rules;
- tests proving directory presence alone does not activate the file.

### Safe precedence posture

Until a consumer proves otherwise:

1. no file in this lane is automatically loaded;
2. no filename has implicit priority;
3. local or deployment overrides do not become repository truth;
4. unknown keys fail closed;
5. conflicting values do not merge unpredictably;
6. missing sensitivity, source-role, model, rights, or release context blocks consequential behavior;
7. configuration cannot override policy or release decisions.

[Back to top](#top)

---

## Habitat semantic and source-role guardrails

### Canonical source-role classes

The Habitat doctrine fixes seven source-role classes:

```text
observed | regulatory | modeled | aggregate | administrative | candidate | synthetic
```

A downstream product may have a different role from an input only when it is created as a new, separately identified, evidence-backed product. Configuration must never relabel a record in place to gain stronger authority.

### Anti-collapse matrix

| Claim or product | Must not be collapsed into | Required configuration posture |
|---|---|---|
| Regulatory critical habitat | Modeled habitat, occurrence points, range maps, stewardship zones | Preserve regulatory source, effective date, designation scope, and authority limits. |
| Modeled habitat or suitability | Regulatory designation or observed occurrence | Label as modeled; expose model version, method, uncertainty, support scale, and limitations. |
| Land-cover observation | Habitat quality, species presence, legal designation | Preserve observation class and time; derived products receive their own identity and role. |
| Habitat patch | Fauna or Flora occurrence | Preserve cross-lane ownership; occurrence context remains a governed join. |
| Connectivity edge or corridor | Observed movement route, legal corridor, or occurrence | Preserve method, resistance assumptions, temporal scope, and uncertainty. |
| Restoration opportunity | Approved project, funded action, completed restoration, or legal commitment | Label as candidate/model output unless separate evidence establishes another status. |
| Stewardship zone | Ownership, title, access right, regulatory designation, or habitat truth | Treat as administrative context with rights and effective dates. |
| Aggregate landscape summary | Exact local occurrence or absence proof | Preserve aggregation support and low-count protections. |
| Candidate feature | Confirmed Habitat object | Require review, evidence, and validation before any status transition. |
| Synthetic fixture | Observed reality | Keep obvious synthetic identifiers and block production/public use. |

### Cross-lane ownership

Habitat may join to Fauna, Flora, Soil, Hydrology, Hazards, Agriculture, and People/Land context. Every join must preserve:

- original domain ownership;
- source role;
- rights and attribution;
- sensitivity tier or restriction state;
- time semantics;
- evidence references;
- uncertainty and method limitations;
- release state.

A join does not transfer authority to Habitat.

[Back to top](#top)

---

## Spatial, temporal, and model semantics

### Spatial semantics

A future configuration must not use unlabeled numbers such as `250`, `10`, or `0.8` where the meaning depends on units, CRS, resolution, scale, support, or confidence.

Spatial settings require:

- named CRS or verified profile reference;
- units;
- source resolution and effective support;
- geometry class;
- positional uncertainty;
- internal versus public-safe representation;
- scale/zoom applicability;
- residual reconstruction risk;
- policy reference for any generalization or suppression.

### Temporal semantics

Keep distinct where material:

- source publication or snapshot time;
- observed time;
- regulatory effective and expiry times;
- model initialization and valid times;
- retrieval time;
- run time;
- release time;
- supersession time;
- correction time.

A single `timestamp` must not silently collapse these meanings.

### Model semantics

Configuration may select a verified model profile. It cannot establish that the model is correct, calibrated, current, or fit for public use.

Modeled Habitat settings should reference:

- model and version;
- input and covariate versions;
- training/calibration scope where applicable;
- intended use and prohibited uses;
- threshold meaning;
- uncertainty representation;
- geographic and temporal applicability;
- known limitations;
- evidence and release references for public derivatives.

[Back to top](#top)

---

## Sensitivity, geoprivacy, and join-induced risk

Sensitive Habitat handling is fail closed.

### Protected contexts

Examples include:

- occurrence-linked sensitive habitat;
- rare-species habitat context;
- breeding, nesting, denning, roosting, spawning, refuge, or hibernation context;
- precise stewardship or conservation-priority areas;
- private-land, access, management, restoration, or protected-resource detail;
- low-count or small-area summaries;
- repeated-query or differencing risks;
- source combinations that reveal more than either input alone.

### Required posture

- Configuration may select an accepted sensitivity or public-safe geometry profile; it must not define an ad hoc bypass.
- Exact internal and public-safe geometry must remain separate.
- Transform parameters come from policy and steward review, not convenience values in an example file.
- Generalization, suppression, constrained jitter, aggregation, delayed publication, or steward-only access must be recorded by the canonical transform/receipt process.
- Style filters, field omission in a popup, client-side zoom limits, opacity, or hidden layers are not geoprivacy controls.
- Sensitive geometry must be transformed or denied **before** tiles, exports, indexes, caches, screenshots, or public DTOs are generated.
- Join sensitivity is assessed on the resulting product. The result must inherit at least the strongest applicable restriction and may require a stricter posture.
- Missing or ambiguous sensitivity context produces `HOLD`, `DENY`, or `ABSTAIN`.

### Low-count and differencing protection

A generalized output may still be reconstructable when:

- only one or a few records contribute;
- successive releases differ by a single feature;
- a small polygon intersects a known property or protected area;
- multiple public layers can be combined to recover exact context;
- a time series reveals arrival, removal, or management activity.

Configuration cannot waive these risks through a low zoom, coarse style, or generic `public: true` flag.

[Back to top](#top)

---

## Secret and live-binding rules

Every committed file must be safe to review publicly.

- Use obvious placeholders such as `<HABITAT_SOURCE_ID>`, `<POLICY_PROFILE_ID>`, `<LOCAL_ONLY_PATH>`, or `<REPLACE_WITH_LOCAL_VALUE>`.
- Never commit credentials, tokens, private keys, certificates, cookies, signed URLs, or service-account material.
- Never commit private hostnames, private IPs, internal dashboards, live database URLs, or confidential deployment values.
- Never commit personal workstation paths or usernames.
- Never commit exact sensitive locations or reconstructable clues.
- Do not put real operational source identifiers into a template when the identifier itself is sensitive or activation-significant.
- Prefer references by name to an approved secret or deployment system.
- If a value may be secret, private, live, or sensitive, remove it, replace it with a placeholder, and document the verified local/deployment injection path.

[Back to top](#top)

---

## Validation

### README validation

- KFM metadata block is balanced and current.
- One H1 is present.
- Headings and internal links resolve.
- Relative repository links resolve where paths are claimed present.
- Code fences and tables are structurally valid.
- Final newline is present.
- Evidence labels do not overstate implementation maturity.

### Future payload validation

| Gate | Required checks | Failure posture |
|---|---|---|
| Inventory and placement | File is under the correct config lane and is not an authority-bearing artifact. | `FAIL`; move or reject. |
| Parse and format | Deterministic parser, supported version, duplicate-key handling, encoding, final newline. | `FAIL` / `ERROR`; no partial application. |
| Shape | Verified schema or closed validator where applicable; unknown keys handled explicitly. | `FAIL` / `HOLD`. |
| Consumer binding | Named consumer, owner, load path, precedence, and deactivation are proven. | `HOLD`; do not activate. |
| Source role | Seven-role class is explicit and no role upgrade occurs. | `FAIL` / `DENY`. |
| Habitat semantics | Modeled/regulatory/observed/aggregate/administrative/candidate/synthetic classes remain distinct. | `FAIL` / `DENY`. |
| Cross-lane ownership | Fauna, Flora, Soil, Hydrology, Hazards, Agriculture, and People/Land truth remains owned by those lanes. | `FAIL` / `HOLD`. |
| Model semantics | Model/version/method/threshold/uncertainty/intended use are explicit. | `HOLD` / `ABSTAIN`. |
| Spatial semantics | CRS, units, resolution, support, geometry class, uncertainty, and scale are explicit. | `FAIL` / `HOLD`. |
| Temporal semantics | Relevant time kinds remain separate; stale and superseded state is visible. | `FAIL` / `ABSTAIN`. |
| Rights and attribution | Source terms, redistribution, attribution, and access limits resolve. | `HOLD` / `DENY`. |
| Sensitivity and geoprivacy | No exact or reconstructable sensitive detail; governed profile refs resolve. | `DENY` / `FAIL`. |
| Join-induced risk | Combined output is reassessed for sensitivity, low count, and reconstruction. | `HOLD` / `DENY`. |
| Secrets and live bindings | No credentials, private endpoints, personal paths, or deployment secrets. | `FAIL`; rotate/revoke if exposed. |
| No-network behavior | Fixtures and validation run without live source access by default. | `FAIL` / `ERROR`. |
| Negative cases | Missing evidence, ambiguous roles, invalid model profile, exact-location request, stale source, unknown key, and precedence conflict are exercised. | Required before activation. |
| Determinism | Same config and fixtures produce stable results and digests. | `FAIL`. |
| Migration and rollback | Prior version, deactivation, correction, and rollback are tested. | `HOLD`. |
| Public-path isolation | Apps and public clients do not read this directory directly. | `DENY` / `FAIL`. |

A syntactically valid file is not necessarily semantically safe, policy-allowed, evidence-supported, or release-ready.

[Back to top](#top)

---

## Failure behavior

| Condition | Expected safe disposition |
|---|---|
| Valid, authorized, non-sensitive configuration | `PASS` for internal validation; continue to ordinary governed processing. |
| Malformed file, unsupported version, duplicate key, or contract violation | `FAIL` or `ERROR`; do not partially apply. |
| Unknown key or unknown precedence | `ERROR` or `HOLD`; do not merge unpredictably. |
| Missing consumer, owner, schema, contract, or policy reference | `HOLD`; do not activate. |
| Unresolved source role or role-upgrade attempt | `FAIL`, `HOLD`, or `DENY`. |
| Modeled product presented as regulatory critical habitat or observation | `FAIL` and `DENY`. |
| Habitat product presented as species occurrence truth | `FAIL` and `DENY`. |
| Missing model fitness, method, threshold meaning, or uncertainty | `HOLD` or `ABSTAIN`. |
| Missing rights, sensitivity, review, evidence, or release state | `HOLD`, `DENY`, or `ABSTAIN`. |
| Exact or reconstructable sensitive context requested for public use | `DENY` by default. |
| Stale, superseded, partial, or missing data | Preserve the state explicitly; `ABSTAIN` when no released alternative exists. |
| Source outage | Do not fabricate freshness or completeness; use a reason-coded stale/partial state. |
| Consumer cannot determine a safe rollback | `HOLD` or `ERROR`. |
| Secret or private endpoint detected | `FAIL`; remove and rotate/revoke as required. |

`PASS` and `FAIL` are validator outcomes, not publication decisions. Public or AI surfaces use governed finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` only after evidence, policy, and release checks.

[Back to top](#top)

---

## Review burden

README changes require:

- configuration or documentation review; and
- Habitat domain review.

A future payload also requires the applicable:

- named consumer owner;
- source and rights reviewer;
- model/method reviewer;
- sensitivity and geoprivacy reviewer;
- Fauna or Flora steward when occurrence or species context is joined;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer;
- policy and release reviewer.

Do not infer acceptance from a missing reviewer rule or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Maintenance and safe change pattern

When a Habitat configuration file is added or changed:

1. identify the exact consumer and owner;
2. re-read the parent config contract and Habitat doctrine;
3. verify the canonical contract, schema, policy, registry, and model references;
4. preserve the seven source roles and landscape-not-species boundary;
5. verify model/regulatory/observed distinctions;
6. review rights, sensitivity, geoprivacy, low-count, join, private-land, and reconstruction risk;
7. verify spatial, temporal, model, uncertainty, and stale-state semantics;
8. run deterministic parse, shape, semantic, negative, and no-network checks;
9. document precedence, unknown-key behavior, migration, deactivation, correction, and rollback;
10. inspect the complete diff for secrets, live bindings, exact locations, and protected clues;
11. verify remote read-back and changed paths; and
12. keep evidence, review, release, and publication as separate governed decisions.

### Change-budget discipline

A configuration PR should not silently add or alter:

- source activation;
- contracts or schemas;
- sensitivity policy;
- model algorithms or thresholds whose meaning is not already governed;
- connectors or network behavior;
- lifecycle data;
- receipts or proofs;
- release decisions;
- public routes or map layers.

Those changes require their own scoped implementation and review surfaces.

[Back to top](#top)

---

## Migration and anti-bypass posture

If misplaced material is found here:

1. do not treat it as authoritative merely because it is committed;
2. classify it as safe config, secret/live binding, contract, schema, policy, registry, source data, package code, pipeline code, runtime/infra, lifecycle object, trust artifact, release record, public artifact, generated output, or sensitive detail;
3. remove or quarantine credentials, live bindings, and exact protected context immediately; rotate or revoke exposed credentials as required;
4. move machine shape to `schemas/`;
5. move semantic meaning to `contracts/`;
6. move policy and geoprivacy rules to `policy/`;
7. move source identity and activation state to registry/connector governance;
8. move implementation to packages, pipelines, connectors, runtime, apps, tools, or infrastructure as appropriate;
9. move lifecycle, catalog, receipt, proof, and published material to canonical `data/` lanes;
10. move release, correction, withdrawal, supersession, and rollback decisions to `release/`;
11. preserve provenance, consumer impact, migration reason, and rollback instructions;
12. create a drift or correction record when the misplaced material was consumed.

### Anti-bypass matrix

| Bypass risk | Required response |
|---|---|
| Config treated as policy authority | Reject; policy remains authoritative. |
| Config duplicates contract or schema | Move meaning/shape to the canonical root and keep only references here. |
| Directory presence activates a source or model | Reject; require explicit verified binding. |
| Config contains exact sensitive context | Remove, assess exposure, and route through sensitivity/correction governance. |
| Client-side style hides protected geometry | Reject; transform or deny before public artifact generation. |
| Config writes catalog, receipt, proof, or release records | Reject and move to canonical trust/release homes. |
| Public client reads this directory | Reject; public access must cross the governed API and released artifacts. |
| Watcher publishes from config | Reject; watchers may propose candidates and receipts only. |
| Model threshold presented as truth | Reject; preserve method, version, intended use, and uncertainty. |

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] A named consumer and accepted owners are verified.
- [ ] The file format, version, parser, and explicit load path are verified.
- [ ] Canonical schema, contract, policy, registry, and doctrine references resolve.
- [ ] Precedence, duplicate-key, missing-file, and unknown-key behavior are documented and tested.
- [ ] The seven source-role classes remain explicit and non-interchangeable.
- [ ] Modeled habitat cannot be labeled or queried as regulatory critical habitat or observation.
- [ ] Habitat remains landscape, not Fauna or Flora occurrence truth.
- [ ] Spatial, temporal, model, uncertainty, stale-state, and supersession semantics are explicit.
- [ ] Rights, attribution, and redistribution terms are reviewed.
- [ ] Sensitivity and public-safe geometry parameters come from accepted policy profiles, not ad hoc config values.
- [ ] Join-induced sensitivity, low counts, differencing, private-land, and reconstruction risks are tested.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, stale, partial, and error cases.
- [ ] No-network tests pass.
- [ ] Secret, private-endpoint, personal-path, and protected-context scans pass.
- [ ] Migration, deactivation, correction, and rollback behavior are tested.
- [ ] No source, model, public layer, API route, release, or publication is activated by file presence.
- [ ] Repository-native checks are substantive or their scaffold limitations are stated explicitly.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat doctrine, source-role vocabulary, object families, sensitivity, and lifecycle posture.
- [`../../../packages/domains/habitat/README.md`](../../../packages/domains/habitat/README.md) — proposed reusable Habitat implementation-helper boundary.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane and sensitivity register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved path and authority drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value handling.

Future files should link to verified Habitat contracts, schemas, policies, source descriptors, models, tests, fixtures, receipts, proofs, and release records only after those exact paths and authority relationships are confirmed.

[Back to top](#top)

---

## ADRs and drift triggers

No ADR is introduced by this README.

Separate governance is required for changes that would:

- add, rename, merge, or retire a canonical domain slug;
- change Habitat ownership or the landscape-not-species boundary;
- change the seven source-role vocabulary or permit role upgrades;
- equate modeled habitat with regulatory critical habitat or occurrence truth;
- select or change canonical Habitat object names;
- resolve segment-versus-flat lane paths;
- define or alter sensitivity tiers, geoprivacy parameters, low-count rules, or public-safe geometry policy;
- decide source rights, source authority, or live-source activation;
- establish universal config discovery, precedence, or unknown-key behavior;
- create a parallel contract, schema, policy, registry, receipt, proof, or release authority;
- authorize direct public access to internal or canonical stores;
- change model fitness, regulatory interpretation, promotion gates, or release separation; or
- introduce a direct public route to configuration material.

Configuration must not be used to settle these decisions indirectly.

[Back to top](#top)

---

## Rollback and correction

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request that restores the prior known-good README or configuration version. Do not force-push or rewrite shared history.

For a future payload correction:

1. disable or stop selecting the affected configuration through the verified consumer mechanism;
2. stop any connector, watcher, model, renderer, scheduled process, or public-output workflow that depends on the faulty selection;
3. preserve the faulty version and evidence needed for review;
4. identify affected objects, joins, model runs, candidates, caches, tiles, indexes, exports, screenshots, and narratives without exposing protected locations;
5. assess whether source roles, ownership, regulatory/model distinctions, model fitness, or evidence status were collapsed;
6. assess whether exact or reconstructable sensitive information was exposed;
7. restore the prior known-good version or safe disabled state;
8. re-run validation and negative cases;
9. create any required correction, redaction, withdrawal, release, or rollback records in their canonical homes; and
10. verify that no public surface continues to serve an unauthorized, stale, misclassified, or reconstructable derivative.

A Git revert does not itself revoke exposed data, correct released artifacts, reverse a regulatory or model claim, or establish KFM publication lineage.

[Back to top](#top)

---

## Safe language rules

Use language such as:

- “safe Habitat configuration template for a named consumer”;
- “intended consumer — `NEEDS VERIFICATION`”;
- “synthetic placeholder”;
- “modeled Habitat profile, not regulatory designation”;
- “public-safe display profile selector, subject to policy and release review”;
- “configuration aid, not authority”;
- “README-only lane plus non-semantic `.gitkeep`”;
- “bounded search found no indexed executable consumer.”

Avoid unsupported claims such as:

- “the Habitat pipeline uses this config”;
- “this file activates the source or model”;
- “this config is validated by CI” when the workflow is only scaffolding;
- “this setting authorizes public display”;
- “this threshold proves habitat presence”;
- “this layer is critical habitat” when the source is modeled;
- “this config replaces policy”;
- “this folder contains the complete operational Habitat configuration.”

[Back to top](#top)

---

## Last reviewed

**2026-07-13**, against `main@e223451fd0852beea79c3cfa0235e1231746dd4f`.

Review again before the first non-README payload, consumer binding, loader or precedence decision, source-role profile, model profile, sensitivity/geoprivacy profile, source or model activation, or public-output integration.

<details>
<summary>Appendix A — no-loss preservation note</summary>

The v0.2 README established a strong Habitat configuration boundary covering no-secrets rules, sensitive-Habitat and geoprivacy posture, source-role controls, consumer/validator expectations, anti-bypass behavior, migration, correction, rollback, and safe language. v0.3 preserves those controls while replacing stale inventory uncertainty with a bounded repository snapshot, explicitly classifying `.gitkeep` as non-semantic, adding the minimum per-file contract, strengthening modeled-versus-regulatory and landscape-versus-species distinctions, adding spatial/temporal/model semantics, join-induced and low-count risk, finite failure behavior, and a concrete first-payload definition of done.

</details>
