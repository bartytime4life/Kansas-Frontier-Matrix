<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-readme
title: connectors/kdwp/ — KDWP Greenfield Compatibility Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KDWP source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Test steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-scaffold; compatibility-path; canonical-family-migration; product-and-role-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; no-network; no-activation; no-publication
current_path: connectors/kdwp/README.md
truth_posture: CONFIRMED repository-present 0.0.0 Python scaffold, merged v0.2 source-layout, package-boundary, and test-boundary READMEs, empty initializer, comment-only fetch/admit modules, nonconforming four-field descriptor, and documentation-only local test lane / CONFLICTED final connector path, compatibility class, package migration, product decomposition, SourceDescriptor authority, narrative-to-machine role mapping, registry activation, fixture routing, and public sensitivity floor / PROPOSED bounded compatibility and future source-admission contract / UNKNOWN buildability, executable package behavior, collected tests, runtime, live source access, current rights and terms, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  prior_blob: 7eedbe1a977174e1dd99671233d14f00fc904b36
related:
  - ../README.md
  - ./pyproject.toml
  - ./src/README.md
  - ./src/kdwp/README.md
  - ./src/kdwp/__init__.py
  - ./src/kdwp/fetch.py
  - ./src/kdwp/admit.py
  - ./src/kdwp/descriptor.yaml
  - ./tests/README.md
  - ../kansas/README.md
  - ../kansas/kdwp/README.md
  - ../kansas/kdwp_flora/README.md
  - ../kansas/kdwp_ert/README.md
  - ../kdwp_ert/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../docs/sources/catalog/kansas/kdwp.md
  - ../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../data/registry/sources/README.md
  - ../../data/registry/sources/habitat/kdwp.yaml
  - ../../data/registry/fauna/sources/kdwp_species.yaml
  - ../../control_plane/source_authority_register.yaml
  - ../../fixtures/README.md
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
  - ../../data/raw/habitat/kdwp/README.md
  - ../../release/
tags: [kfm, connectors, kdwp, kansas, wildlife, parks, sinc, listed-species, fauna, flora, habitat, python, greenfield, compatibility, source-admission, source-role, rights, sensitivity, privacy, no-network, raw, quarantine, governance]
notes:
  - "The top-level lane now contains a confirmed 0.0.0 package scaffold; the prior README's pointer-only and canonicality assertions are therefore stale and overconfident."
  - "The package, source-layout, and test-boundary READMEs are v0.2 and describe the same non-operational scaffold, invalid local descriptor, product/role conflicts, sensitive-location burden, and unresolved Kansas-family migration."
  - "The Kansas-family coordination lane connectors/kansas/kdwp/ exists and is documented as the family admission lane, but exact probes found no package scaffold beneath it in the adjacent evidence pass; no package migration is asserted."
  - "A source catalog page, directory name, local YAML, package import, pull request, merge, or green TODO-only workflow cannot create SourceDescriptor authority, rights clearance, sensitivity clearance, activation, evidence closure, or release permission."
  - "Only this Markdown file is changed. No code, package metadata, descriptor, registry entry, fixture, test, workflow, contract, schema, policy, source payload, credential, activation decision, lifecycle artifact, evidence object, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Greenfield Compatibility Connector Boundary

> Repository-grounded boundary for the source-specific lane at `connectors/kdwp/`. The path contains a real Python package scaffold, but no supported connector behavior. Existing documentation treats it as a compatibility lane relative to `connectors/kansas/kdwp/`; the exact migration and final implementation topology remain unresolved.

**Document lifecycle:** `draft v0.2`  
**Current package maturity:** `CONFIRMED` non-operational `0.0.0` greenfield scaffold  
**Owner:** `OWNER_TBD`  
**Path posture:** repository-present; compatibility intent documented; exact class and final implementation home `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** no live network, no activation, no package-local authority, no direct lifecycle persistence, no evidence closure, no release, no publication

> [!IMPORTANT]
> The current lane contains an empty `__init__.py`, comment-only `fetch.py` and `admit.py`, and a four-field `descriptor.yaml` placeholder. These establish path and package presence—not a fetcher, parser, admission decision, quarantine implementation, lifecycle handoff, test suite, or runtime.

> [!CAUTION]
> `sensitivity_floor: public` in the package-local placeholder is not a public-safety decision. KDWP product families can involve listed status, SINC rank, sensitive ecological locations, monitoring observations, ranges, habitat or stewardship context, private-property joins, and review-tool outputs. Unknown product identity, source role, rights, sensitivity, geometry, or review state fails closed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current status](#current-status) · [Repository snapshot](#repository-snapshot) · [Path conflict](#path-and-migration-conflict) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Descriptor boundary](#descriptor-registry-and-activation-boundary) · [Product boundaries](#kdwp-product-and-source-role-boundaries) · [Sensitivity](#rights-sensitivity-privacy-and-geometry) · [Lifecycle](#lifecycle-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [Review](#review-burden) · [Evidence](#evidence-basis) · [ADRs](#adrs-and-migration) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kdwp/` is a repository-present source-specific implementation lane under the canonical `connectors/` responsibility root.

Its present purpose is to:

- expose the exact incompleteness of the current KDWP package scaffold;
- prevent placeholder files from being mistaken for an active connector;
- preserve the unresolved migration relationship between this package and the Kansas-family KDWP coordination lane;
- keep KDWP product identity and source roles from collapsing into one agency-wide feed;
- establish fail-closed requirements for rights, sensitivity, privacy, geometry, taxonomy, status, time, and review state;
- limit any future package output to caller-owned source-admission candidates;
- identify the contracts, schemas, registries, policies, fixtures, tests, and reviews that must exist before implementation or activation.

This README does not declare that the current top-level path is canonical, deprecated, legacy, redirect-only, or permanent. It also does not declare `connectors/kansas/kdwp/` to contain the executable package. Those placement and migration questions remain governed decisions.

[Back to top](#top)

---

## Authority level

**Source-specific connector scaffold only.** This folder has no independent authority over source identity, object meaning, machine shape, rights, sensitivity, lifecycle state, evidence, catalog closure, release, correction, rollback, or public delivery.

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Responsibility root | **CONFIRMED** | Source-specific fetch, probe, preservation, parsing, packaging, and admission support belongs under `connectors/`. |
| Current path | **CONFIRMED** | `connectors/kdwp/` exists and contains a Python scaffold. |
| Distribution | **CONFIRMED PLACEHOLDER** | `kfm-connector-kdwp`, version `0.0.0`; buildability and supported runtime remain unknown. |
| Package behavior | **NOT IMPLEMENTED IN NAMED MODULES** | Initializer is empty; fetch and admit modules contain comments only. |
| Local descriptor | **NONCONFORMING PLACEHOLDER** | It is not a registry record, SourceDescriptor authority, activation decision, rights decision, sensitivity decision, or release authorization. |
| Local tests | **DOCUMENTATION BOUNDARY** | The test README exists; conventional executable tests were not established in the adjacent evidence pass. |
| Compatibility class | **CONFLICTED** | Existing docs say compatibility/noncanonical, but no accepted migration record reviewed here classifies the path as legacy, deprecated, mirror, redirect, or retained implementation. |
| Final package home | **CONFLICTED** | Kansas-family coordination is documented, while the actual package currently remains here. |
| Source activation | **DENIED / NOT ESTABLISHED** | No conforming product descriptor, reviewed authority entry, source head, terms review, or activation decision was verified. |
| Public release | **NONE** | Connector or package presence cannot create a public claim, layer, API payload, summary, evidence bundle, or release. |

[Back to top](#top)

---

## Current status

### Repository snapshot

The following bounded tree is confirmed by direct repository reads and the merged adjacent v0.2 documentation:

```text
connectors/kdwp/
├── README.md                       # this parent connector boundary
├── pyproject.toml                  # project kfm-connector-kdwp, version 0.0.0
├── src/
│   ├── README.md                   # v0.2 source-layout boundary
│   └── kdwp/
│       ├── README.md               # v0.2 package scaffold boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only placeholder
│       ├── admit.py                # comment-only placeholder
│       └── descriptor.yaml         # name: kdwp; role/rights TBD; sensitivity_floor: public
└── tests/
    └── README.md                   # v0.2 negative-first test boundary
```

| Surface | Confirmed state | Consequence |
|---|---|---|
| [`pyproject.toml`](./pyproject.toml) | Project name and `0.0.0` version only. | Build backend, Python support, dependencies, discovery, entry points, and commands are `UNKNOWN`. |
| [`src/README.md`](./src/README.md) | Records the source layout and unresolved package migration. | Documentation only; does not implement behavior. |
| [`src/kdwp/README.md`](./src/kdwp/README.md) | Records package files, descriptor conflict, product boundaries, and fail-closed contract. | Documentation only; package remains non-operational. |
| [`src/kdwp/__init__.py`](./src/kdwp/__init__.py) | Empty. | No import API or import-time behavior. |
| [`src/kdwp/fetch.py`](./src/kdwp/fetch.py) | Comment-only. | No transport, endpoint, authentication, retry, timeout, pagination, rate-limit, caching, or source-head behavior. |
| [`src/kdwp/admit.py`](./src/kdwp/admit.py) | Comment-only. | No validation, finite disposition, quarantine, candidate envelope, or sink behavior. |
| [`src/kdwp/descriptor.yaml`](./src/kdwp/descriptor.yaml) | Four-field placeholder. | Invalid as source, rights, sensitivity, activation, or release authority. |
| [`tests/README.md`](./tests/README.md) | Negative-first future test contract. | Does not prove collection, passing tests, coverage, or substantive CI. |

This is not a recursive tree receipt. Differently named, generated, unindexed, or later-added files remain `UNKNOWN` until directly inspected at the commit under review.

[Back to top](#top)

---

## Path and migration conflict

Repository evidence now shows two different KDWP surfaces:

| Surface | Observed posture | Current implication |
|---|---|---|
| `connectors/kdwp/` | Repository-present Python package scaffold. | Actual implementation placeholder exists here today; presence does not establish final canonicality. |
| `connectors/kansas/kdwp/` | Kansas-family KDWP coordination README and placeholder lane. | Documents family/source admission boundaries; exact package probes in the adjacent evidence pass did not establish a package scaffold beneath it. |
| `connectors/kansas/kdwp_flora/` | Flora/listed-species documentation lane. | Product placement and relationship to the parent package remain governed. |
| `connectors/kansas/kdwp_ert/` | Ecological Review Tool documentation lane. | ERT result semantics and sibling-versus-child placement remain governed. |
| `connectors/kdwp_ert/` | Top-level ERT compatibility surface. | Adds migration pressure; does not authorize duplicate active implementations. |

The human-facing KDWP source catalog and Kansas-family README provide strong placement intent, but documentation alone is not a package migration, import decision, source-ID migration, registry decision, or accepted ADR.

A safe migration must settle together:

- winning implementation path and losing-path disposition;
- distribution and import names;
- product adapter topology;
- stable source and product IDs;
- descriptor and activation references;
- fixtures and test routing;
- workflows and source-head state;
- receipt, evidence, correction, and supersession lineage;
- consumer imports and documentation backlinks;
- deprecation schedule and rollback.

Until then, do not create a second evolving package under the Kansas-family path and do not upgrade this path to canonical authority by convention.

[Back to top](#top)

---

## What belongs here

The existing lane may contain, after accepted implementation and migration decisions:

- package and import compatibility code required by an accepted migration;
- source-specific client interfaces with explicit dependency injection;
- deterministic parsers for approved, identified KDWP product shapes;
- source-native metadata preservation;
- product and source-role dispatch;
- candidate identity and temporal normalization that does not upgrade truth status;
- geometry, CRS, uncertainty, precision, withholding, and transform metadata preservation;
- finite hold, quarantine, deny, abstain, and error outcomes using the accepted project vocabulary;
- caller-owned candidate envelopes or immutable byte/reference results;
- no-network synthetic test support that belongs beside the package under the accepted test architecture;
- compatibility warnings, deprecation adapters, and migration documentation.

Implementation must remain bounded to source-specific fetch and admission mechanics. It must not absorb downstream domain truth, policy, evidence, release, or public-delivery responsibilities.

[Back to top](#top)

---

## What does not belong here

Do not place or infer the following under this connector lane:

- canonical contracts or schemas;
- source registry or authority records;
- policy-as-code or discretionary policy decisions;
- rights or sensitivity approvals;
- production credentials, browser sessions, API keys, signed URLs, cookies, or tokens;
- bulk harvests, source archives, fixture corpora, media dumps, or sensitive ecological payloads;
- authoritative taxonomy, legal-status, range, occurrence, habitat, or stewardship truth outside declared source/product scope;
- evidence bundles, claim authority, proof packs, release manifests, promotion decisions, corrections, withdrawals, or rollback cards;
- direct writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, registry, proof, receipt, or release roots;
- public map layers, tiles, API payloads, reports, alerts, summaries, exports, or AI answers;
- life-safety, emergency-response, permit, legal-clearance, or absence determinations;
- a second independently evolving implementation at a competing path;
- generated language or models presented as source truth.

[Back to top](#top)

---

## Inputs

Future executable code may accept only explicit, caller-supplied inputs such as:

- a reviewed product-specific descriptor or stable reference to one;
- an explicit activation decision appropriate to the requested operation;
- a declared KDWP product family and source role;
- immutable response bytes, local file reference, or injected transport result;
- retrieval context containing source URI, source head, retrieval time, request identity, and safe status metadata;
- caller-supplied clock, retry, timeout, rate-limit, cache, and pagination policy;
- a temporary working directory controlled by the caller;
- reviewed taxonomy/status/rank crosswalk references;
- rights, sensitivity, geometry, and review policy references;
- an explicit sink/callback interface owned by an external orchestrator.

The package must not discover production credentials, infer an activation decision, guess a product role, or silently contact a source during import, tests, documentation builds, or ordinary validation.

[Back to top](#top)

---

## Outputs

A future connector may return only bounded, caller-owned values, for example:

- immutable fetched bytes plus safe retrieval metadata;
- a parsed source-native record preserving original fields and qualifiers;
- a normalized admission candidate with explicit product, role, identity, time, geometry, rights, and sensitivity references;
- a finite disposition such as hold, quarantine, deny, abstain, error, or accepted-for-external-handoff;
- deterministic reason codes and safe explanations;
- no-op, retry, stale, drift, and correction signals;
- a receipt candidate or evidence reference for an external orchestrator to validate and persist.

The connector does not persist lifecycle state. An accepted external orchestrator may choose a governed RAW or QUARANTINE handoff after validating the candidate. Anything beyond that remains downstream.

[Back to top](#top)

---

## Descriptor, registry, and activation boundary

The current package-local YAML is not a conforming `SourceDescriptor`.

| Local field | Current value | Fail-closed interpretation |
|---|---|---|
| `name` | `kdwp` | Agency/package umbrella, not necessarily a stable product-specific `source_id`. |
| `role` | `TBD` | Unresolved and not an accepted machine role. |
| `rights` | `TBD` | No permission, attribution, redistribution, or stored-content decision. |
| `sensitivity_floor` | `public` | Deprecated/permissive placeholder; not reviewed product- or record-level public clearance. |

Before any source access or admission behavior exists, governance must provide:

1. one accepted SourceDescriptor contract and schema authority;
2. stable product-level source IDs and descriptor versions;
3. explicit product scope, source type, role, authority, publisher, and steward;
4. reviewed rights, attribution, redistribution, disclaimer, and permitted-use posture;
5. sensitivity, privacy, exact-location, geometry, and public-transform posture;
6. cadence, access method, rate/size limits, citation, and source-head evidence;
7. admissibility limits, review state, activation state, lifecycle handoff class, and public-release posture;
8. a machine authority/control-plane entry where required;
9. validation fixtures and substantive CI.

Unknown, missing, placeholder, contradictory, draft, denied, retired, fixture-only, or unreviewed state must prevent live source access and public output.

[Back to top](#top)

---

## KDWP product and source-role boundaries

KDWP is an institutional source family, not one homogeneous feed.

| Product or record family | Candidate meaning | Prohibited collapse |
|---|---|---|
| Listed-status or legal-status records | Source-issued status within stated jurisdiction and effective time. | Not occurrence, range, habitat, survey, or proof of current presence. |
| SINC rank or sensitivity context | Source-issued conservation/sensitivity context within stated scope and review state. | Not automatic public-location clearance and not a field observation. |
| Monitoring, survey, mortality, disease, eDNA, acoustic, or telemetry observations | Agency observation evidence with method, time, qualifiers, geometry, and uncertainty. | Not legal/listed status, modeled range, habitat suitability, or population truth without downstream analysis. |
| Range or distribution products | Compilation or model with vintage, scale, method, and uncertainty. | A range polygon is not an exact occurrence or proof of presence at a selected point. |
| Habitat, natural-community, WMA, stewardship, or conservation-planning products | Administrative, modeled, observed, or planning context according to product role. | Modeled habitat, regulatory context, stewardship boundary, and observation are distinct. |
| Ecological Review Tool inputs/results | Bounded review evidence tied to submitted scope, date, rules, and disclaimer. | Not a permit, legal clearance, field survey, consultation completion, absence finding, or release approval. |
| Portal, index, or carrier records | References to upstream records or products. | Carrier does not inherit all upstream authority and does not become original evidence. |
| Generated normalizations, joins, maps, summaries, or AI text | Rebuildable derivative with traceable inputs and transforms. | Cannot mint source authority, reveal withheld material, or replace policy/review/release state. |

Mixed products must be split by product and role or held until an accepted multi-role contract proves safe handling.

[Back to top](#top)

---

## Rights, sensitivity, privacy, and geometry

### Rights

No live source access, persistence, fixture reuse, redistribution, media handling, or public output is permitted until current terms and source-steward review establish:

- access permission;
- attribution and citation requirements;
- redistribution and derivative permissions;
- disclaimer and compelled-link language;
- retention and caching limits;
- automated-access and rate-limit rules;
- treatment of attachments, images, downloads, and GIS packages;
- correction, withdrawal, and stale-state expectations.

Unknown or contradictory rights fail closed.

### Sensitivity and privacy

Default-deny or review-required material includes:

- precise locations for listed, protected, sensitive, denning, nesting, roosting, breeding, hibernating, translocated, captive, or disease-affected taxa;
- ecological review requests and results containing private parcels, project locations, contacts, access routes, internal notes, or living-person data;
- private-property, residence, infrastructure, collector, submitter, landowner, or permit-sensitive joins;
- records whose sensitivity is created or increased through cross-source combination;
- public derivatives lacking an approved generalization/redaction transform and receipt.

A permissive package default cannot lower record-level or join-induced sensitivity.

### Geometry

Every candidate must preserve or explicitly account for:

- native geometry type and source CRS/datum;
- coordinate method and derivation;
- observed, inferred, generalized, centroided, buffered, withheld, or null status;
- precision and uncertainty;
- geometry vintage and source feature identity;
- transform/generalization identity and reviewer state;
- public versus steward-only geometry separation.

False precision, undocumented centroiding, coordinate swaps, invalid ranges, missing datum where material, and reconstruction of withheld locations must fail or quarantine.

[Back to top](#top)

---

## Lifecycle boundary

```text
source edge / pre-RAW
        ↓
connector returns caller-owned bytes or admission candidate
        ↓
external governed orchestrator
        ├── DENY / ABSTAIN / ERROR / HOLD
        ├── QUARANTINE candidate
        └── RAW candidate after descriptor, activation, rights, and sensitivity gates
                ↓
WORK / QUARANTINE
                ↓
PROCESSED
                ↓
CATALOG / TRIPLET + EvidenceBundle / proof closure
                ↓
reviewed release transition
                ↓
PUBLISHED governed API / artifact / map surface
```

This connector owns only the bounded source edge. It cannot skip, merge, or authorize later stages. Promotion is a governed state transition, not a file copy, path move, commit, pull request, merge, successful fetch, or connector receipt.

[Back to top](#top)

---

## Failure contract

Incomplete, unsafe, or contradictory input must produce one finite outcome using the accepted project vocabulary.

| Semantic outcome | Use |
|---|---|
| `HOLD` | Structurally parseable candidate lacks required governance, mapping, or review state. |
| `QUARANTINE` | Candidate may be useful but cannot safely advance; reasons are recorded. |
| `DENY` | Requested access, transform, exposure, or use is prohibited. |
| `ABSTAIN` | Evidence, identity, mapping, or temporal/spatial support is insufficient for the requested interpretation. |
| `ERROR` | Deterministic contract, transport, parse, or operational failure; no permissive fallback. |

The exact enum and envelope contract remain `NEEDS VERIFICATION`. Package code must use the accepted shared contract rather than inventing an incompatible local vocabulary.

A safe failure carries stable reason codes, a non-sensitive explanation, affected gates, retry/remediation class, no partial public result, and no side effect outside caller-owned temporary state.

[Back to top](#top)

---

## Validation

Future implementation must prove at least:

- package import is side-effect-free and no-network;
- zero executable tests and unexpected skipped negative tests fail readiness review;
- descriptor shape and activation state are resolved from accepted authority surfaces;
- the current four-field placeholder is rejected;
- product family and source role are explicit and compatible;
- listed-status, observation, range, habitat, ERT, and carrier meanings do not collapse;
- upstream identity, source URI, product ID, amendment, and supersession links are preserved;
- source, observed, effective/valid, retrieval, review, release, and correction times remain distinct where material;
- source-native taxonomy/status/rank values survive unresolved mappings;
- rights, attribution, redistribution, disclaimer, and retention state fail closed;
- sensitivity, privacy, exact-location, public precision, and join-induced risk fail closed;
- geometry type, CRS/datum, derivation, precision, uncertainty, withholding, and transform metadata are preserved;
- parsing and normalization are deterministic and do not silently discard unknown values;
- network, credentials, production filesystem, lifecycle roots, registry, proof, receipt, catalog, and release writes are denied by default;
- no public map, tile, API payload, report, summary, alert, citation, evidence claim, or AI answer is emitted;
- package and path migration cannot create duplicate active implementations, descriptors, fixtures, source heads, or lineage;
- substantive CI executes real package/test commands rather than TODO-only echo steps.

### Negative decision matrix

| Condition | Required result |
|---|---|
| Missing or invalid descriptor | No source access; hold/quarantine/deny. |
| Missing, draft, denied, retired, or fixture-only activation | No live source access. |
| Unknown rights or terms | No public output; fail closed. |
| Unknown sensitivity or missing review | No public output; fail closed. |
| Unknown product family or role | Hold/quarantine; no umbrella fallback. |
| Observation treated as legal/listed status | Fail. |
| Listed-status context treated as occurrence | Fail. |
| Range or modeled habitat treated as exact occurrence | Fail. |
| ERT result treated as permit, clearance, field survey, or absence proof | Fail. |
| Taxon/status/rank mapping unresolved | Preserve source value and hold/abstain. |
| Retrieval time substituted for effective or observed time | Fail. |
| False-precision or reconstructable sensitive geometry | Fail or quarantine. |
| Sensitive join becomes less restrictive than an input | Fail. |
| Direct lifecycle, evidence, catalog, proof, registry, or release write | Fail. |
| Current or Kansas-family path declares implementation canonicality without accepted migration | Fail migration review. |
| Same controlled inputs produce different candidate or reasons | Fail determinism. |
| Green workflow runs only TODO echo steps | Do not count as implementation proof. |

[Back to top](#top)

---

## Review burden

| Reviewer role | Required focus |
|---|---|
| Connector/package maintainer | Package API, transport, parsing, side effects, determinism, dependency posture, and migration compatibility. |
| Kansas/KDWP source steward | Product inventory, source identity, current access surfaces, cadence, corrections, and source-native fields. |
| Fauna/Flora/Habitat stewards | Domain ownership, taxonomy/status semantics, observation/range/habitat distinctions, and cross-lane routing. |
| Rights reviewer | Terms, attribution, redistribution, stored payloads, media, fixtures, and public derivatives. |
| Sensitivity/privacy reviewer | Exact locations, protected taxa, private/living-person joins, public precision, ERT material, logs, and fixtures. |
| Security reviewer | Network/credential posture, retries, request logging, parsers, archives/media, dependencies, and CI artifacts. |
| Contract/schema reviewer | Accepted SourceDescriptor, candidate, receipt, and failure shapes plus migration handling. |
| Test/validation steward | Discovery, negative cases, reason codes, no-side-effect assertions, safe fixtures, and substantive CI. |
| Migration/architecture reviewer | Winning path, imports, source IDs, descriptors, consumers, deprecation, history, and rollback. |

Exact individual owners or GitHub teams remain `UNKNOWN`; do not invent assignments.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Prior `connectors/kdwp/README.md` blob | **CONFIRMED** | Previous compatibility posture and rollback target. | Current package behavior or accepted migration. |
| `pyproject.toml` | **CONFIRMED** | Distribution name and version `0.0.0`. | Buildability, dependencies, Python support, or runtime. |
| Package files | **CONFIRMED** | Empty initializer, comment-only fetch/admit modules, four-field descriptor. | Fetching, parsing, admission, or handoff behavior. |
| Merged source/package/test v0.2 READMEs | **CONFIRMED DOCUMENTATION** | Repository snapshot, conflicts, fail-closed boundaries, and proposed validation. | Executable implementation, coverage, activation, or release. |
| `connectors/kansas/kdwp/README.md` | **CONFIRMED DOCUMENTATION** | Kansas-family source admission intent and product boundaries. | Executable package migration or canonical machine authority. |
| Flora and ERT READMEs | **CONFIRMED DOCUMENTATION** | Distinct product pressure and role/sensitivity boundaries. | Final topology, source activation, or legal effect. |
| KDWP source catalog | **CONFIRMED DRAFT DOCUMENTATION** | Human-facing source-family/product context. | Current source terms, machine descriptor, or activation. |
| SourceDescriptor contract/schema surfaces | **CONFIRMED REPOSITORY SURFACES; AUTHORITY CONFLICTED** | Candidate governance fields and fail-closed obligations. | One accepted schema/validator or conforming KDWP descriptor. |
| Registry/control-plane files | **CONFIRMED PLACEHOLDERS / EMPTY AUTHORITY IN ADJACENT EVIDENCE** | Lack of established KDWP machine activation. | Source admission or public use. |
| Rights and sensitivity READMEs | **CONFIRMED GREENFIELD SURFACES** | Responsibility boundaries. | Current KDWP terms or record-level decision. |
| Connector/descriptor workflows | **CONFIRMED TODO-ONLY IN ADJACENT EVIDENCE** | Workflow scaffolding. | Package import, test collection, descriptor conformance, or enforcement. |
| Directory Rules and connector-output ADR | **CONFIRMED DOCTRINE** | Responsibility root, lifecycle, handoff, migration, and no-parallel-authority rules. | Resolution of the current path/product/schema conflicts. |

No live KDWP endpoint, payload, current terms page, credential, runtime log, deployed service, EvidenceBundle, release manifest, or public client was inspected for this documentation update.

[Back to top](#top)

---

## ADRs and migration

This README creates no ADR and resolves no migration.

An accepted ADR or explicit governed migration record is required before any change that:

- moves or duplicates the package;
- changes distribution, import, source, or product IDs;
- chooses one versus multiple product adapters;
- changes fixture/test routing;
- creates parallel descriptor, registry, policy, schema, receipt, proof, or release homes;
- retires this path or promotes it from compatibility posture;
- establishes narrative-to-machine source-role mapping;
- changes a public sensitivity or geometry default.

A documentation update may surface these conflicts; it cannot settle them by wording alone.

[Back to top](#top)

---

## Definition of done

### This documentation revision

- [x] Current package and path maturity is explicit.
- [x] The prior pointer-only inventory and overconfident canonicality language are corrected.
- [x] Source-layout, package, and test v0.2 boundaries are integrated.
- [x] Directory Rules responsibility roots and lifecycle law are preserved.
- [x] Product and source-role anti-collapse controls are explicit.
- [x] Rights, sensitivity, privacy, geometry, time, ERT, fixture, and join risks fail closed.
- [x] Inputs, outputs, failure semantics, validation, review, migration, rollback, and backlog are explicit.
- [x] No implementation or activation maturity is overclaimed.

### Connector readiness remains open

- [ ] Accepted path, package/import identity, product topology, source IDs, losing-path disposition, and migration plan.
- [ ] Accepted SourceDescriptor contract/schema/registry authority and conforming product descriptors.
- [ ] Reviewed activation decisions and source-head evidence.
- [ ] Current source access, terms, attribution, redistribution, cadence, rate/size limits, correction, and withdrawal posture.
- [ ] Safe product contracts, taxonomy/status/rank crosswalks, ERT semantics, and public geometry policies.
- [ ] Implemented package configuration, client/parser/admission interfaces, finite envelopes, and deterministic reason codes.
- [ ] Safe reviewed fixtures and executable no-network negative tests.
- [ ] Substantive CI with non-zero collection, zero-discovery failure, and demonstrated boundary failures.
- [ ] Evidence, catalog, policy, review, release, correction, and rollback closure outside the connector.

Documentation completeness does not imply connector readiness, source admission, activation, rights clearance, sensitivity clearance, evidence closure, or publication.

[Back to top](#top)

---

## Rollback

Rollback is required if this README is used to claim source authority, accepted canonicality, completed migration, executable connector behavior, source access, activation, rights or sensitivity clearance, safe exact-location exposure, lifecycle authority, evidence closure, or release readiness.

Before merge, close the draft pull request and abandon the scoped branch if the revision is rejected.

After merge, restore prior README blob:

```text
7eedbe1a977174e1dd99671233d14f00fc904b36
```

through a transparent revert commit or revert pull request, then rerun applicable documentation, link, connector-boundary, policy, and rollback checks. Do not reset, force-push, or rewrite shared history.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Complete recursive inventory of this lane and consumers | **UNKNOWN** | Mounted checkout or non-truncated tree/import receipt at reviewed commit. |
| Final connector and package home | **CONFLICTED** | Accepted ADR/migration, consumer inventory, import/source-ID plan, deprecation, and rollback. |
| Compatibility class of `connectors/kdwp/` | **CONFLICTED / NEEDS VERIFICATION** | Accepted legacy/mirror/redirect/retained decision. |
| Product-family topology | **CONFLICTED** | Accepted relationship among parent, Flora, ERT, observation, range, and habitat products. |
| SourceDescriptor schema and validator authority | **CONFLICTED** | One accepted contract/schema, migration, fixtures, validator, and CI command. |
| Narrative-to-machine source-role mapping | **CONFLICTED** | Accepted vocabulary and crosswalk. |
| Product descriptors and source-authority entries | **PLACEHOLDER / NOT ESTABLISHED** | Conforming records and reviewed authority/control-plane entries. |
| Activation decisions and source heads | **NOT ESTABLISHED** | Reviewed activation records and approved observed source-head receipts. |
| Current access surfaces and product schemas | **NEEDS VERIFICATION** | Current authoritative KDWP documentation and source-steward review. |
| Current rights, attribution, redistribution, disclaimers, and retention | **NEEDS VERIFICATION** | Current terms and signed rights review. |
| Sensitivity, privacy, public geometry, redaction, and joins | **NEEDS VERIFICATION** | Policy, transform profiles, fixtures, receipts, tests, and reviewer decisions. |
| Taxonomy, status, SINC rank, range, occurrence, habitat, and ERT semantics | **NEEDS VERIFICATION** | Product contracts, crosswalks, fixtures, and domain/source review. |
| Executable package behavior | **NOT IMPLEMENTED IN NAMED MODULES** | Code, packaging, imports, tests, and logs. |
| Substantive connector CI | **NOT ESTABLISHED** | Real workflow commands, test collection, logs, and demonstrated negative failure. |
| Owners and review routing | **UNKNOWN** | Accepted CODEOWNERS or ownership register. |
| Repository-wide promotion prerequisites | **NEEDS VERIFICATION** | Trusted workflow result and required doctrine/release artifacts. |

[Back to top](#top)

---

## Maintainer note

Do not build new authority here.

The smallest safe next implementation sequence is:

1. settle path, package, product, source-ID, descriptor, fixture, and test routing;
2. replace the local descriptor placeholder with an accepted external reference or governed migration shim;
3. add one invented invalid descriptor fixture;
4. prove import and network denial;
5. prove one deterministic fail-closed candidate with no side effects;
6. add product/role, rights, sensitivity, identity, time, geometry, and migration negatives;
7. only then consider a reviewed, opt-in source probe.

[Back to top](#top)
