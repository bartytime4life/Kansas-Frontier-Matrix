<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-src-package-readme
title: connectors/kdwp/src/kdwp/ — KDWP Greenfield Compatibility Package Scaffold
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Kansas/KDWP source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; greenfield-scaffold; compatibility-path; canonical-family-migration; product-and-role-conflict; source-admission; rights-fail-closed; sensitivity-fail-closed; no-network; no-activation; no-publication
current_path: connectors/kdwp/src/kdwp/README.md
truth_posture: CONFIRMED 0.0.0 scaffold, empty initializer, comment-only fetch/admit files, four-field local descriptor, absent proposed helper modules, and README-only local test lane / CONFLICTED package migration, product dispatch, SourceDescriptor machine authority, narrative-to-machine role mapping, and local sensitivity floor / PROPOSED future compatibility and admission contract / UNKNOWN buildability, executable tests, runtime, source activation, current access and rights, substantive CI enforcement, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 40deb4a3cab0972f0c7d38930e30c3b497408b0a
  prior_blob: bf78ca7d6f90dddbd1446226b11b1249aa6902a7
  readme_introduction_commit: da7587bbcc9a4047e3343091e89b9cc4b12cd302
related:
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../tests/README.md
  - ../../../README.md
  - ../../../kansas/README.md
  - ../../../kansas/kdwp/README.md
  - ../../../kansas/kdwp_flora/README.md
  - ../../../kansas/kdwp_ert/README.md
  - ../../../../CONTRIBUTING.md
  - ../../../../.github/CODEOWNERS
  - ../../../../.github/workflows/connector-gate.yml
  - ../../../../.github/workflows/source-descriptor-validate.yml
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../../data/registry/sources/README.md
  - ../../../../data/registry/sources/habitat/kdwp.yaml
  - ../../../../data/registry/fauna/sources/kdwp_species.yaml
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../policy/rights/README.md
  - ../../../../policy/sensitivity/README.md
  - ../../../../data/raw/habitat/kdwp/README.md
  - ../../../../release/
tags: [kfm, connectors, kdwp, kansas, package, python, greenfield, compatibility, wildlife, sinc, listed-species, fauna, flora, habitat, source-admission, source-role, rights, sensitivity, no-network, raw, quarantine, no-publication]
notes:
  - "Direct reads at base commit 40deb4a3cab0972f0c7d38930e30c3b497408b0a confirm project version 0.0.0, an empty __init__.py, comment-only fetch.py and admit.py files, and a four-field descriptor.yaml placeholder."
  - "The exact proposed helper modules descriptors.py, parse.py, normalize.py, roles.py, taxonomy.py, sensitivity.py, geometry.py, handoff.py, and errors.py were absent at the inspected base."
  - "The canonical Kansas-family coordination lane connectors/kansas/kdwp/ is present with README.md and .gitkeep, while exact pyproject.toml, src/README.md, and tests/README.md probes below it returned Not Found; no package migration is asserted."
  - "The connector-local descriptor uses deprecated minimal aliases, leaves role and rights unresolved, and asserts sensitivity_floor: public; it is not a conforming SourceDescriptor, registry record, activation decision, sensitivity clearance, or release authorization."
  - "Repository registry surfaces contain KDWP placeholders, the machine source-authority register has entries: [], rights and sensitivity policy READMEs are greenfield stubs, and connector/source-descriptor workflows execute TODO echo steps."
  - "Only this Markdown file is in scope. No code, package metadata, descriptor, registry entry, fixture, test, workflow, policy, schema, source payload, activation decision, lifecycle artifact, release object, path move, or public artifact is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Greenfield Compatibility Package Scaffold

> Repository-grounded boundary for the Python namespace at `connectors/kdwp/src/kdwp/`. The package exists, but it is a non-operational `0.0.0` scaffold inside a top-level KDWP compatibility lane. The current Kansas-family coordination lane is `connectors/kansas/kdwp/`; migration of this package, import name, and product layout has not been accepted.

**Document lifecycle:** `draft`  
**Component maturity:** `CONFIRMED` greenfield scaffold · no supported fetch, admission, lifecycle, or public behavior  
**Owner:** `OWNER_TBD`  
**Authority level:** package inside a noncanonical compatibility lane; canonical family placement is documented, but package migration and product topology are `CONFLICTED / NEEDS VERIFICATION`  
**Boundary:** no live network, no activation, no package-local authority, no direct lifecycle persistence, no release, no publication

> [!IMPORTANT]
> `fetch.py` and `admit.py` contain comments only, `__init__.py` is empty, and `descriptor.yaml` is a nonconforming placeholder. Nothing in the inspected package fetches KDWP material, makes an admission decision, emits a candidate envelope, writes to a lifecycle root, or creates a public claim.

> [!CAUTION]
> `sensitivity_floor: public` in the connector-local placeholder is **not** a public-safety determination. KDWP products include listed-status, SINC-rank, range, monitoring, habitat, stewardship, and review outputs with different roles and sensitivity burdens. Treat the local YAML as an invalid migration placeholder, never as activation or release authority.

**Quick links:** [Purpose](#purpose) · [Current package](#current-package) · [Repository fit](#repository-fit) · [Descriptor and activation conflict](#descriptor-and-activation-conflict) · [Product and role boundaries](#kdwp-product-and-role-boundaries) · [Sensitivity boundary](#sensitivity-and-public-use-boundary) · [Inputs and outputs](#inputs-and-outputs) · [Implementation boundary](#implementation-boundary) · [Failure contract](#failure-contract) · [Validation](#validation) · [Evidence](#evidence) · [Review and rollback](#review-migration-and-rollback) · [Definition of done](#definition-of-done)

---

## Purpose

This README records what the current Python namespace is, what it demonstrably does not do, and which governance, packaging, source, policy, and validation gates must close before implementation begins.

Today the package is useful only as:

- a visible marker for the live `kdwp` scaffold;
- a fail-closed boundary around placeholder code and metadata;
- a record of the unresolved migration from the top-level compatibility lane to the Kansas-family KDWP lane;
- a product and source-role anti-collapse contract for future maintainers;
- a rollback and review input for a later package or connector migration decision.

The intended audience is connector and package maintainers, Kansas/KDWP source stewards, Fauna, Flora, and Habitat stewards, rights and sensitivity/privacy reviewers, security reviewers, test/validation stewards, and migration reviewers.

This README does not prove that the current package path should survive, that `kdwp` is the final package or source-ID slug, that one adapter should represent every KDWP product, or that any source is approved for access, admission, transformation, or release.

[Back to top](#top)

---

## Current package

Direct file reads at base commit `40deb4a3cab0972f0c7d38930e30c3b497408b0a` confirm this bounded surface:

```text
connectors/kdwp/
├── pyproject.toml                  # project kfm-connector-kdwp, version 0.0.0
├── src/
│   ├── README.md                   # stale compatibility source-layout outline
│   └── kdwp/
│       ├── README.md               # this package boundary
│       ├── __init__.py             # empty
│       ├── fetch.py                # comment-only greenfield placeholder
│       ├── admit.py                # comment-only greenfield placeholder
│       └── descriptor.yaml         # four-field greenfield placeholder
└── tests/
    └── README.md                   # test-boundary documentation only in indexed/exact probes
```

| Surface | Confirmed state | Consequence |
|---|---|---|
| [`pyproject.toml`](../../pyproject.toml) | Declares `kfm-connector-kdwp` at `0.0.0`; no build system, dependencies, Python constraint, package-discovery rule, entry point, or command is declared. | Buildability, installability, supported runtime, dependency posture, and package API are `UNKNOWN`. |
| [`__init__.py`](./__init__.py) | Empty file. | No package API or import-time behavior is implemented. |
| [`fetch.py`](./fetch.py) | Comment-only placeholder. | No transport, endpoint, authentication, retry, timeout, rate-limit, pagination, caching, or source-head behavior exists. |
| [`admit.py`](./admit.py) | Comment-only placeholder. | No descriptor resolution, validation, quarantine, admission, receipt, or handoff behavior exists. |
| [`descriptor.yaml`](./descriptor.yaml) | `name: kdwp`, `role: TBD`, `rights: TBD`, `sensitivity_floor: public`. | Incomplete and unsafe as an activation basis; not a conforming descriptor or authority record. |
| [`src/README.md`](../README.md) | States that only the source-layout README and child package README were confirmed. Direct package-file reads now disprove that inventory claim. | Treat the parent inventory as stale documentation, not current package evidence. |
| [`tests/README.md`](../../tests/README.md) | Documentation contract at the inspected path; indexed search found no executable test file. Exact probes for `test_fetch.py`, `test_admit.py`, `test_descriptor.py`, and `conftest.py` returned `Not Found`. | Package tests, discovery, coverage, and CI enforcement are absent or `UNKNOWN`. |

Exact probes for the v0.1 README's proposed helper modules—`descriptors.py`, `parse.py`, `normalize.py`, `roles.py`, `taxonomy.py`, `sensitivity.py`, `geometry.py`, `handoff.py`, and `errors.py`—returned `Not Found` at the pinned base.

This is a bounded inventory, not a recursive tree receipt. Differently named, generated, unindexed, or later-added files remain `UNKNOWN` until directly inspected at the commit under review.

[Back to top](#top)

---

## Repository fit

KFM's [`connectors/`](../../../README.md) root owns source-specific fetch, probe, packaging, and admission support. Source doctrine, registry instances, schemas, policy decisions, evidence closure, lifecycle promotion, release decisions, and public-client behavior live in their own responsibility roots.

| Surface | Observed posture | Package implication |
|---|---|---|
| [`connectors/kdwp/`](../../README.md) | Repository-present top-level `0.0.0` scaffold whose READMEs describe noncanonical compatibility posture. | Path presence does not grant canonical status, activation, or permission to expand implementation. |
| [`connectors/kansas/`](../../../kansas/README.md) | Repository-present Kansas source-family coordination lane. | Governs Kansas-family placement but not product activation or package migration. |
| [`connectors/kansas/kdwp/`](../../../kansas/kdwp/README.md) | Current KDWP source-family coordination README plus `.gitkeep`; exact probes found no `pyproject.toml`, `src/README.md`, or `tests/README.md` below it. | Canonical family placement is documented; executable package placement and migration remain unresolved. |
| [`connectors/kansas/kdwp_flora/`](../../../kansas/kdwp_flora/README.md) | Repository-present Flora/listed-species documentation lane. | Product grouping and sibling-versus-child topology remain independently governed. |
| [`connectors/kansas/kdwp_ert/`](../../../kansas/kdwp_ert/README.md) | Repository-present Ecological Review Tool documentation lane. | ERT is not evidence that this package implements ecological review or legal clearance. |
| [`docs/sources/catalog/kansas/kdwp.md`](../../../../docs/sources/catalog/kansas/kdwp.md) | Draft source-family catalog entry that says the Kansas-family connector path was already correct and documents several distinct KDWP product classes. | Human-facing source doctrine; not a descriptor, activation decision, runtime contract, or release authority. |
| KDWP registry placeholders | Repository contains a Habitat placeholder and a Fauna greenfield template, both incomplete. | No product-level registry admission or source activation is established. |

The responsibility root is not the unresolved question: source-specific implementation belongs under `connectors/`. The unresolved questions are whether this top-level package is retained as a compatibility import, how implementation moves or is recreated under `connectors/kansas/kdwp/`, which product adapters exist, which package/import/source IDs survive, and how losing paths are deprecated without breaking lineage.

A later migration can affect imports, source IDs, descriptor references, fixtures, receipts, workflows, backlinks, source-head history, correction/supersession state, and rollback. Resolve it through an accepted ADR or explicit migration plan. This README does not move, rename, delete, or ratify a path.

[Back to top](#top)

---

## Descriptor and activation conflict

[`descriptor.yaml`](./descriptor.yaml) is not a usable `SourceDescriptor`.

| Connector-local field | Current value | Current contract posture |
|---|---|---|
| `name` | `kdwp` | Not the required `source_id`; it names an agency/package umbrella rather than one governed KDWP product. Under the populated closed schema it is not a canonical field. |
| `role` | `TBD` | Deprecated migration alias; `TBD` is not an accepted source role. KDWP lists, ranks, range products, observations, habitat layers, and review outputs require product/record-specific decisions. |
| `rights` | `TBD` | Scalar placeholder where the populated schema requires a reviewed rights object. Unresolved rights fail closed. |
| `sensitivity_floor` | `public` | Deprecated migration alias and unsafe as a permissive default while product identity, record-level sensitivity, exact location, rights, review, redaction, and release state are unresolved. |

The inspected [`SourceDescriptor` contract](../../../../contracts/source/source_descriptor.md) and [populated singular-path schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) require a richer closed object: object and schema identity, stable source ID, descriptor version, source type and role, authority rank, publisher and steward, rights, sensitivity, cadence, access, citation, source-head evidence, admissibility limits, public-release posture, review state, release state, and lifecycle state.

The machine authority is also conflicted:

- the populated singular-path schema labels [`schemas/contracts/v1/sources/source_descriptor.schema.json`](../../../../schemas/contracts/v1/sources/source_descriptor.schema.json) canonical and itself legacy;
- the plural-path schema is an empty `PROPOSED` scaffold that accepts arbitrary properties and provides no meaningful validation;
- narrative source docs use role words such as `authority`, `regulatory`, `observed`, `context`, and `model`, while the populated machine schema uses values such as `authoritative_for_claim`, `regulatory_context`, `observation`, `steward_review_source`, and `model_context`;
- no accepted narrative-to-machine role mapping was found in scope.

Repository authority surfaces do not close the gap:

| Surface | Confirmed state | Consequence |
|---|---|---|
| [`data/registry/sources/habitat/kdwp.yaml`](../../../../data/registry/sources/habitat/kdwp.yaml) | Four-line `PROPOSED` placeholder generated from documentation inventory. | Not a conforming product descriptor or activation decision. |
| [`data/registry/fauna/sources/kdwp_species.yaml`](../../../../data/registry/fauna/sources/kdwp_species.yaml) | Greenfield template using legacy fields and unresolved `TBD` values. | Not evidence of rights, sensitivity, role, source head, activation, or public release. |
| [`control_plane/source_authority_register.yaml`](../../../../control_plane/source_authority_register.yaml) | `status: PROPOSED` with `entries: []`. | No KDWP source-authority or activation entry is established. |
| [Rights policy README](../../../../policy/rights/README.md) and [sensitivity policy README](../../../../policy/sensitivity/README.md) | Greenfield bundle stubs. | No executable KDWP rights, redaction, or sensitivity decision is proven. |
| [`connector-gate`](../../../../.github/workflows/connector-gate.yml) and [`source-descriptor-validate`](../../../../.github/workflows/source-descriptor-validate.yml) workflows | Pull-request workflows whose jobs currently run `echo TODO ...`. | A green run does not establish connector-boundary enforcement, descriptor validity, rights presence, or package behavior. |

Therefore:

- do not load the local YAML as registry, activation, policy, or release authority;
- do not infer public safety from `sensitivity_floor: public`;
- do not create one agency-wide descriptor or one role for all KDWP products;
- do not copy narrative role tokens into machine fields until an accepted mapping exists;
- do not place authoritative descriptors or activation decisions in this package;
- do not enable transport until product-specific descriptors, current reviews, source heads, and activation decisions exist in accepted authority surfaces;
- do not treat any descriptor as proof that source claims are true or approved for release.

[Back to top](#top)

---

## KDWP product and role boundaries

KDWP is a source family, not one homogeneous dataset. The role labels below describe current source-document meaning only; they are not approved machine enum values.

| Product or surface | Source-document role posture | Identity and support that must survive | Denied collapse |
|---|---|---|---|
| Endangered, threatened, SINC, and other listed-status artifacts | `authority` / `regulatory` | Exact issuing program, list/instrument identity, version or effective date, taxon/community identity, citation, source head, rights, and review state. | A legal or stewardship determination treated as an observation, crowd report, or unrestricted public-location grant. |
| SINC ranks and sensitivity inputs | `authority` input to downstream sensitivity review | Rank vocabulary and version, taxon/community identity, effective date, issuing program, citation, disagreement state, and review provenance. | Rank interpreted as public-release permission, exact-location permission, universal taxonomy, or proof of current local presence. |
| Range products and spatial status context | `authority` / `context` | Product/version, scale, vintage, geometry/support type, uncertainty, taxon identity, source URI, and disclaimer. | Range polygon treated as a dated occurrence, current occupancy, exact sensitive locality, or observation. |
| Survey, monitoring, mortality, and disease records | `observed` | Program and event identity, observation time, source time, retrieval time, taxon identification, observer/recorder posture where lawful, geometry, uncertainty, withholding state, and source-native identifiers. | Observation treated as legal status, complete population truth, agency-wide rank, emergency warning, or unrestricted location. |
| Habitat, natural-community, and stewardship layers | Product-specific `context` or `authority` | Product identity, stewardship role, scale, vintage, model/compilation status, geometry/support, rights, citation, and sensitivity joins. | Habitat or stewardship polygon treated as per-place species occurrence, legal clearance, or final habitat truth without downstream evidence. |
| Kansas Ecological Review Tool and related review outputs | Product-specific `context`, `model`, or steward-review surface | Tool/product version, input scope, model or rule version, review date, disclaimer, source data references, output class, and steward/reviewer state. | Tool output treated as a legal determination, permit, site-clearance certificate, complete absence finding, or public-safe exact-location authority. |
| Operational notices, hunting/fishing material, closures, or transient advisories | Operational or administrative context only when explicitly admitted | Product identity, source time, expiry, not-for-life-safety disclaimer, rights, and intended use. | KFM acting as alert authority, emergency channel, current legal advice, or replacement for official KDWP instructions. |

Required anti-collapse rules:

1. one publisher name must not produce one publisher-wide role, descriptor, cadence, rights state, or sensitivity state;
2. mixed files must be split by product or record role, or fail closed into review/quarantine;
3. regulatory/listed-status material must remain distinct from observed events;
4. a range or habitat surface must remain distinct from an occurrence record;
5. an ERT/review result must remain distinct from legal clearance and public release;
6. federal status, NatureServe rank, taxonomy-backbone, and aggregator-origin records retain their own authority and provenance rather than being relabeled as KDWP truth;
7. maps, tiles, summaries, joins, dashboards, and AI explanations remain downstream carriers, never source authority.

[Back to top](#top)

---

## Sensitivity and public-use boundary

KDWP material can contain or imply exact sensitive ecological locations, nests, dens, roosts, hibernacula, spawning sites, rare plants, natural-community locations, private-land context, individual hunter or landholder information, and sensitive facilities.

Package-level rules:

- source access or upstream public availability is not KFM rights or release clearance;
- public lists or rank labels do not make associated occurrence geometry public-safe;
- exact or withheld geometry must never be reconstructed from generalized fields, joins, logs, exceptions, caches, fixtures, or model output;
- source-native geometry, uncertainty, precision, and withholding state must be preserved for governed review without being echoed into public or developer-facing errors;
- fixtures must be synthetic, minimized, rights-cleared, and incapable of disclosing a real sensitive locality;
- `sensitivity_floor: public` in the placeholder must not flow into runtime, tests, policy, map styling, exports, or release decisions;
- redaction, generalization, withholding, embargo, and public-precision decisions belong to reviewed downstream policy and release workflows, with receipts where required;
- the package must not serve public layers, range maps, ecological-review answers, or AI summaries;
- operational notices must carry a not-for-life-safety posture and never replace official channels.

A successful fetch or parse would prove only that bytes were retrieved or interpreted. It would not prove source admission, evidence closure, public safety, legal status, release readiness, or truth.

[Back to top](#top)

---

## Inputs and outputs

### Current inputs

None. The package declares no supported function, class, command, configuration contract, endpoint, credential variable, host allowlist, fixture format, parser shape, or sink interface.

### Current outputs

None. The placeholders emit no payload, parse result, source-head observation, candidate envelope, receipt, validation report, RAW record, QUARANTINE record, evidence object, or public artifact.

### Future admissible inputs

Only after placement, descriptor, activation, rights, sensitivity, and packaging decisions are accepted, a narrow package contract may accept:

- a conforming, reviewed, product-specific `SourceDescriptor` reference;
- an explicit activation decision for fixture-only, restricted, or approved live operation;
- approved source bytes, files, archives, documents, tables, GIS exports, or transport results;
- current access configuration supplied through approved secret handling, never committed source;
- exact KDWP product/program identity and source-native identifiers;
- source-head evidence such as version, release date, checksum, `ETag`, `Last-Modified`, or documented manual identifier;
- source, observation, validity/effective, retrieval, and correction time where material;
- rights, attribution, sensitivity, geometry, withholding, and reviewer references;
- explicit run identity and caller-owned candidate-output interfaces;
- synthetic or rights-cleared fixtures for offline tests.

### Future admissible outputs

A future implementation may return, without direct persistence:

- deterministic source-head or probe results;
- parse results that preserve source-native fields and do not upgrade meaning;
- a `RAW` handoff candidate when identity, role, rights, sensitivity, source head, and activation are sufficiently resolved;
- a `QUARANTINE` handoff candidate with a structured reason when they are not;
- a process-memory retrieval, no-op, denial, or operational receipt candidate when an accepted receipt contract exists;
- a deterministic failure that omits sensitive payload data.

The package must not select release, persist directly into lifecycle roots, create an `EvidenceBundle`, emit a public geometry, or convert connector success into evidence or truth.

[Back to top](#top)

---

## Implementation boundary

### Allowed only after migration and contract decisions

- a narrow product dispatcher that preserves exact KDWP product identity;
- explicit opt-in transport behind reviewed configuration, host, credential, timeout, retry, rate-limit, and source-head controls;
- parsers for verified source-native shapes, including reviewed document/table/file/GIS variants;
- deterministic normalization that preserves source-native values, units, dates, geometry, uncertainty, rank vocabulary, and disclaimers;
- product, role, taxonomy, listed-status, rank, rights, sensitivity, geometry, time, and source-head checks;
- structured failures suitable for `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, or a `QUARANTINE` candidate;
- side-effect-free candidate-envelope construction for governed orchestration;
- offline, synthetic, minimized, negative-first fixtures and tests;
- a transparent compatibility import or redirect if an accepted migration retains this package temporarily.

### Forbidden

- network calls on import or by default;
- credentials, tokens, cookies, account data, private endpoints, or signed URLs in source, fixtures, docs, logs, exceptions, or test output;
- agency-wide default roles, rights, sensitivity, cadence, source-head, or public-release assumptions;
- authoritative `SourceDescriptor` instances, source-authority entries, policy decisions, or activation decisions inside the package;
- direct or implicit writes to RAW, QUARANTINE, receipts, WORK, PROCESSED, CATALOG, TRIPLET, proofs, release, rollback, or PUBLISHED roots;
- silent mapping from narrative source-role words into unresolved machine enums;
- treating a list, rank, range product, habitat layer, observation, or ERT result as interchangeable;
- reconstructing or exposing withheld or sensitive geometry;
- presenting ERT or other review outputs as permits, legal clearance, complete absence findings, or public-release approval;
- public maps, tiles, APIs, dashboards, exports, range products, ecological-review answers, or AI answers;
- emergency, hunting/fishing, legal, land-use, operational, or life-safety advice;
- claims of implementation, validation, activation, coverage, policy enforcement, or CI maturity without current evidence.

There is intentionally no quickstart. A runnable example would imply a supported API, source, and safety posture that do not exist.

[Back to top](#top)

---

## Failure contract

A future implementation must fail deterministically and without echoing sensitive payload content. Minimum reason families include:

- unresolved package migration, import identity, source ID, or product topology;
- missing, nonconforming, unreviewed, superseded, or inactive product descriptor;
- missing activation decision or operation not allowed by activation mode;
- unknown product, unsupported source shape, source-head mismatch, or stale source;
- unresolved role, authority, legal/listed-status context, rank vocabulary, rights, attribution, cadence, or sensitivity;
- missing taxon/community identity, observation/event identity, source URI, citation, time, geometry, uncertainty, scale, withholding state, or disclaimer;
- mixed regulatory, authority, observed, context, modeled, administrative, or review-tool material without a governed split;
- denied network posture, unapproved host, missing secret handling, or unsafe response size/type;
- attempted direct lifecycle persistence, evidence/release creation, public output, or sensitive-location exposure;
- reliance on the local `sensitivity_floor: public` placeholder.

Unknowns route to `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, or a `QUARANTINE` candidate. They never receive permissive defaults.

[Back to top](#top)

---

## Validation

No package build, install, import, or test command is documented because none is supported by the inspected project metadata.

Before implementation maturity can be claimed, evidence must cover:

1. accepted KDWP package location, import name, source-ID convention, compatibility class, and losing-path migration;
2. complete recursive package, test, fixture, workflow, and backlink inventory;
3. build backend, package discovery, supported Python versions, dependency policy, entry points, and clean install/import;
4. accepted `SourceDescriptor` schema/contract authority and narrative-to-machine role mapping;
5. product-specific conforming descriptors, source-authority records where applicable, review state, and explicit activation decisions;
6. current source access methods, product schemas, terms, attribution, redistribution, cadence, rate limits, source heads, correction, and withdrawal behavior;
7. no-network default behavior plus host, credential, timeout, retry, response-size, content-type, and payload-logging controls for opt-in transport;
8. synthetic or rights-cleared fixtures with listed-status, role, rights, sensitivity, exact-location, withholding, taxonomy, time, geometry, and malformed-input negative cases;
9. product and role anti-collapse tests for lists/ranks, ranges, observations, habitat/stewardship surfaces, and ERT/review outputs;
10. deterministic `RAW`/`QUARANTINE` candidate-envelope, idempotency, no-op, denial, and lifecycle-boundary behavior;
11. proof that package code cannot create policy, evidence, catalog, release, public map/API/UI, or AI authority;
12. substantive package-specific test discovery and CI execution, including negative coverage and failure evidence;
13. correction, supersession, invalidation, migration, deactivation, and rollback tests.

The current `connector-gate` and `source-descriptor-validate` workflows are TODO-only scaffolds. Their successful status cannot be used as evidence that the package, descriptor, rights, sensitivity, or lifecycle boundary was tested.

Documentation checks for this revision should include one H1, balanced fenced blocks, working repository-relative links, no remote badge/image dependencies, no credential-like strings, a final newline, and an exact one-file diff.

[Back to top](#top)

---

## Evidence

Evidence for this revision is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `40deb4a3cab0972f0c7d38930e30c3b497408b0a`.

| Evidence | Status | Supports | Does not support |
|---|---|---|---|
| Target README and history | `CONFIRMED` | Prior blob `bf78ca7d6f90dddbd1446226b11b1249aa6902a7`; substantive README introduced by commit `da7587bbcc9a4047e3343091e89b9cc4b12cd302`. | Runtime, source access, descriptor validity, tests, or release. |
| [`pyproject.toml`](../../pyproject.toml) | `CONFIRMED` | Project name `kfm-connector-kdwp` and version `0.0.0`. | Buildability, dependencies, Python support, installability, API, or command. |
| Exact package-file reads | `CONFIRMED` | Empty initializer; comment-only fetch/admit placeholders; four-field descriptor placeholder. | Executable behavior, parser coverage, admission, lifecycle output, or activation. |
| Exact proposed-module probes | `CONFIRMED absent at base` | The nine helper filenames proposed by v0.1 were not present. | Permanent nonexistence or absence of differently named/unindexed files. |
| [`src/README.md`](../README.md) | `CONFIRMED stale inventory` | Existing source-layout boundary language. | Current package inventory; direct file reads supersede its two-file snapshot. |
| [`tests/README.md`](../../tests/README.md) plus exact test probes | `CONFIRMED` documentation / named tests absent | Intended offline, sensitive-species-safe compatibility-test posture. | Executable tests, discovery, coverage, or CI success. |
| [`connectors/kansas/kdwp/README.md`](../../../kansas/kdwp/README.md), `.gitkeep`, and exact package-path probes | `CONFIRMED` | Kansas-family coordination lane exists; no named package scaffold was found below it. | Accepted package migration, final product layout, or runtime. |
| [`docs/sources/catalog/kansas/kdwp.md`](../../../../docs/sources/catalog/kansas/kdwp.md) | `CONFIRMED draft` | KDWP source-family/product, role, sensitivity, and canonical-family documentation. | Current endpoint behavior, rights clearance, valid machine roles, descriptor admission, or activation. |
| [`SourceDescriptor` contract](../../../../contracts/source/source_descriptor.md) and [populated singular schema](../../../../schemas/contracts/v1/source/source_descriptor.schema.json) | `CONFIRMED draft/PROPOSED` | Rich descriptor surface, deprecated aliases, closed-object and fail-closed constraints. | Accepted plural-path migration, persisted KDWP descriptors, or runtime enforcement. |
| [Plural schema](../../../../schemas/contracts/v1/sources/source_descriptor.schema.json) | `CONFIRMED empty PROPOSED scaffold` | Current schema-path conflict. | Meaningful validation or canonical migration completion. |
| KDWP registry placeholder files | `CONFIRMED` | Placeholder and greenfield-template state. | Registry admission, product identity, rights, sensitivity, source head, activation, or release. |
| [`source_authority_register.yaml`](../../../../control_plane/source_authority_register.yaml) | `CONFIRMED` | Register is `PROPOSED` and contains `entries: []`. | Any KDWP authority/activation decision. |
| Rights and sensitivity policy READMEs | `CONFIRMED` | Both are greenfield stubs. | Executable or reviewed KDWP policy. |
| Connector and descriptor workflows | `CONFIRMED TODO-only` | Workflow names and triggers exist. | Substantive connector, descriptor, rights, sensitivity, or package validation. |
| [`data/raw/habitat/kdwp/README.md`](../../../../data/raw/habitat/kdwp/README.md) | `CONFIRMED documentation` | RAW habitat lane boundary and per-product role split are documented. | Actual payloads, accepted connector output, promotion, or public release. |

Not inspected: live KDWP services or portals, current terms pages, credentials, source payloads, private or sensitive records, real exact coordinates, executable package tests, runtime logs, deployed configuration, emitted receipts, EvidenceBundles, release manifests, or public clients. Treat associated claims as `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Review, migration, and rollback

Review changes here as connector-placement, package/import identity, KDWP product identity, source-role, legal/listed-status, rights, sensitivity, privacy, exact-location, security, and lifecycle-boundary changes—even when the diff is documentation-only.

A future migration must preserve or deliberately supersede:

- Git and documentation history;
- package/import compatibility and deprecation behavior;
- product/source IDs and descriptor references;
- source-head and retrieval lineage;
- fixtures, tests, workflow discovery, and negative cases;
- receipts, candidate-envelope references, and downstream backlinks;
- rights, sensitivity, redaction, correction, withdrawal, and review state;
- rollback to the last known safe package and documentation state.

Rollback this README revision if it is used to:

- treat this package or another path as canonical without an accepted migration decision;
- activate the local descriptor or any unresolved registry placeholder;
- infer public safety from `sensitivity_floor: public`;
- claim working fetch, admission, parsing, fixtures, tests, policy, CI enforcement, or lifecycle output;
- collapse listed-status/rank, range, observation, habitat/stewardship, ERT, or operational products;
- expose sensitive ecological or private-location detail;
- present ERT/review output as legal clearance or public-release authority;
- bypass descriptor, activation, rights, sensitivity, evidence, policy, review, release, correction, or rollback gates.

Before merge, close the draft change and abandon its scoped branch if the revision is rejected. After merge, create a transparent revert of the documentation commit; do not reset, force-push, or rewrite shared history. The baseline target blob is `bf78ca7d6f90dddbd1446226b11b1249aa6902a7` at base commit `40deb4a3cab0972f0c7d38930e30c3b497408b0a`.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Current package files and `0.0.0` maturity are explicit.
- [x] Placeholder fetch, admission, descriptor, registry, policy, workflow, and test state is not overstated.
- [x] Canonical family placement and unresolved package migration are separated.
- [x] Descriptor/schema authority, role-vocabulary conflict, and default-deny result are explicit.
- [x] KDWP product, source-role, rights, sensitivity, exact-location, ERT, and public-use anti-collapse rules are explicit.
- [x] Current inputs, outputs, commands, tests, activation, lifecycle behavior, and publication are stated as absent or unknown.
- [x] Evidence limits, review burden, migration discipline, and rollback target are recorded.

### Implementation readiness

- [ ] Package-location/import/source-ID migration is accepted and losing paths are dispositioned.
- [ ] Owners and required reviewers are assigned.
- [ ] Build, install, Python-version, dependency, entry-point, and package API contracts are implemented.
- [ ] SourceDescriptor machine authority and narrative-to-machine role mapping are accepted.
- [ ] Product-specific conforming descriptors, authority/registry records, review states, and activation decisions exist.
- [ ] Current source access, schemas, terms, rights, attribution, cadence, rate limits, source heads, correction, and withdrawal are reviewed.
- [ ] Sensitive-location, private-land/living-person, geometry, uncertainty, withholding, redaction, and public-precision policy is executable.
- [ ] Product dispatch, parsing, candidate-envelope, no-op, denial, and lifecycle-boundary behavior is implemented.
- [ ] Default tests are offline, deterministic, synthetic or rights-cleared, negative-first, and CI-discovered.
- [ ] Connector/descriptor workflows execute substantive checks rather than TODO steps.
- [ ] Correction, deactivation, supersession, migration, and rollback are tested.

Until every applicable implementation-readiness item closes, keep this package inert and fail closed.

<p align="right"><a href="#top">Back to top</a></p>
