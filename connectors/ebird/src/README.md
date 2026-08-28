<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ebird-src-readme
title: connectors/ebird/src/ — eBird Connector Source Tree
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Fauna steward · Data steward · QA steward · Docs steward
created: 2026-07-10
updated: 2026-07-10
policy_label: restricted
related:
  - ../README.md
  - ./ebird/README.md
  - ../tests/README.md
  - ../../../docs/sources/catalog/ebird/README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../data/registry/sources/fauna/
  - ../../../data/raw/fauna/
  - ../../../data/quarantine/fauna/
  - ../../../data/receipts/fauna/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, ebird, src, python-package, fauna, birds, source-admission, sensitivity, quarantine, governance]
notes:
  - "connectors/ebird/src/ is the source-tree container for the eBird connector package."
  - "Source-tree code may support descriptor-gated eBird intake and raw/quarantine admission only."
  - "Imports must be side-effect free; exact sensitive occurrence data must fail closed."
  - "Actual modules, exports, dependencies, tests, fixtures, credentials, and CI behavior remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# eBird Connector Source Tree

> Python source-root boundary for governed eBird source-admission code.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: connector source tree" src="https://img.shields.io/badge/scope-connector__source__tree-blue">
  <img alt="Policy: restricted" src="https://img.shields.io/badge/policy-restricted-orange">
  <img alt="Lifecycle: raw or quarantine" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine-orange">
</p>

`connectors/ebird/src/`

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Authority boundary](#authority-boundary) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Import safety](#import-safety) · [Sensitivity posture](#sensitivity-posture) · [Validation](#validation) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Scope

`connectors/ebird/src/` is the Python source-tree container for the eBird connector package.

Code below this tree may support descriptor-gated source requests, metadata preservation, content digests, bounded parsing, sensitivity routing, and raw/quarantine admission envelopes. It must not become avian truth, fauna doctrine, taxonomy authority, policy authority, schema authority, source-registry authority, catalog/triplet authority, proof closure, release authority, publication authority, fixture authority, or generated-report storage.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Source-tree path:** `connectors/ebird/src/`  
> **Truth posture:** path and package README are `CONFIRMED`; package discovery, modules, imports, exports, dependencies, tests, fixtures, credentials, endpoints, and CI execution remain `UNKNOWN / NEEDS VERIFICATION`.

## Repo fit

```text
connectors/
└── ebird/
    ├── README.md
    ├── src/
    │   ├── README.md
    │   └── ebird/
    │       └── README.md
    └── tests/
        └── README.md
```

Related responsibility roots:

```text
docs/sources/catalog/ebird/  # eBird source-family and product documentation
docs/domains/fauna/          # fauna doctrine and domain guidance
data/registry/sources/fauna/ # SourceDescriptors and activation state
data/raw/fauna/              # admitted raw/staged outputs
data/quarantine/fauna/       # held or sensitive material requiring review
data/receipts/fauna/         # process and validation receipts
policy/sensitivity/          # sensitivity and release rules
release/                     # release, correction, and rollback decisions
```

> [!NOTE]
> These paths are responsibility boundaries. Their current contents, enforcement, and runtime integration remain `NEEDS VERIFICATION` unless directly inspected.

## Authority boundary

```text
connectors/ebird/src/
├── package source tree
├── package folders
├── package-local documentation
└── importable connector code

ALLOWED HANDOFFS:
  data/raw/fauna/
  data/quarantine/fauna/
  receipt inputs for downstream receipt writers

NOT HERE:
  source descriptors as authority
  fauna doctrine
  taxonomy authority
  policy decisions
  processed records
  catalog or triplet writers
  EvidenceBundle closure
  release or publication decisions
  public-ready exact occurrence outputs
  fixtures as authority
  generated reports
```

## Accepted contents

| Accepted item | Example | Required posture |
|---|---|---|
| Package directory | `ebird/` | Must remain connector implementation code only |
| Package-local documentation | package README | Must not claim runtime behavior unless verified |
| Endpoint adapters | API, EBD, SED request helpers | Must be SourceDescriptor-linked and configurable |
| Metadata parsers | checklist, observation, taxonomy, product metadata | Must preserve product family and source limitations |
| Admission helpers | digest, timestamps, output envelope | Must target raw/quarantine only |
| Sensitivity routing helpers | restricted-location or review flags | Must fail closed and must not publish/generalize autonomously |
| Test support helpers | fake clients or small deterministic builders | Must not become fixture authority |

## Exclusions

| Do not store here | Correct home |
|---|---|
| SourceDescriptors or activation records | `data/registry/sources/fauna/` |
| Raw or quarantine payloads | `data/raw/fauna/`, `data/quarantine/fauna/` |
| Processed occurrence, checklist, taxonomy, or range records | downstream processing lanes |
| Catalog or triplet records | governed catalog/triplet stages |
| EvidenceBundles or proof packs | `data/proofs/` or verified proof homes |
| Release, correction, or rollback decisions | `release/` |
| Sensitivity or publication policy | `policy/` and governed policy homes |
| Machine schemas | `schemas/contracts/v1/` |
| Human contracts and semantic authority | `contracts/` |
| Canonical fixtures | accepted fixture roots |
| Generated test or QA reports | `artifacts/` |

## Import safety

Importing code below `connectors/ebird/src/` must not:

- call eBird services;
- read credentials or environment secrets;
- write files or lifecycle objects;
- initialize network clients with live side effects;
- mutate source activation state;
- emit logs containing exact sensitive locations, observer identifiers, tokens, or private metadata;
- publish, generalize, promote, or release records.

Configuration, credentials, SourceDescriptors, clients, clocks, and output writers should be injected at runtime through explicit interfaces.

## Source and product-family posture

Implementation must keep eBird product families distinct:

- API responses are not interchangeable with EBD or SED extracts;
- observations are not range, occupancy, abundance, or population truth;
- checklist metadata is not proof of observer identity, access rights, or complete detection;
- taxonomy inputs are versioned crosswalk inputs, not autonomous taxonomic authority;
- hotspot or region summaries are derived context, not exact occurrence evidence;
- absence from a response is not proof of biological absence;
- historical and current records must preserve their own temporal scope.

Preserve, when available:

- SourceDescriptor ID and activation state;
- product family and access mode;
- source locator or request fingerprint;
- retrieval time and source/observation/checklist time;
- taxonomy identifiers and taxonomy version;
- content digest;
- source role and limitations;
- rights and access posture;
- sensitivity and review flags;
- quarantine reason and bounded outcome.

## Sensitivity posture

> [!CAUTION]
> Exact occurrence data for sensitive species, nests, roosts, breeding sites, private land, or observer-linked records must fail closed. This source tree must not emit public-ready exact locations or bypass policy, redaction, generalization, review, or release controls.

Package code should return explicit bounded outcomes such as:

| Outcome | Meaning |
|---|---|
| `admit_raw` | Candidate is eligible for raw admission with preserved metadata |
| `quarantine` | Rights, sensitivity, integrity, schema, or review issue requires hold |
| `deny` | Source activation, policy, rights, or safety conditions prohibit intake |
| `no_change` | Retrieved content is unchanged from the governed prior state |
| `rate_limited` | Upstream limit prevented completion without unsafe retry behavior |
| `skipped` | A documented precondition was not met |
| `error` | Execution failed and produced no trusted admission result |

## Validation

Before relying on this source tree, verify:

- [ ] package discovery and import path are correct;
- [ ] imports are side-effect free;
- [ ] public exports are documented or intentionally absent;
- [ ] SourceDescriptor and activation checks are enforced;
- [ ] credentials, endpoints, timeouts, retries, pagination, and rate limits are configurable;
- [ ] API, EBD, SED, taxonomy, and derived products remain distinguishable;
- [ ] exact sensitive coordinates and observer/private metadata fail closed;
- [ ] output writers can target only raw/quarantine admission lanes;
- [ ] no-network tests cover metadata preservation and bounded failure outcomes;
- [ ] downstream stages—not this source tree—own processing, evidence closure, release, and publication;
- [ ] CI invokes the relevant tests or explicitly documents exclusion.

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `connectors/ebird/README.md` | `CONFIRMED` | Connector purpose, product families, sensitivity posture, raw/quarantine boundary | Does not prove implementation or activation |
| `connectors/ebird/src/ebird/README.md` | `CONFIRMED` | Package-level boundary and import-safety expectations | Does not prove modules or runtime behavior |
| `connectors/ebird/pyproject.toml` | `CONFIRMED` | Greenfield package name/version | Does not prove discovery, dependencies, build, tests, or installation |
| Current source-tree inventory | `UNKNOWN` | Actual modules and exports | Requires recursive repository inspection |
| Tests, fixtures, CI, runtime receipts | `NEEDS VERIFICATION` | Enforceability and behavior | Not verified in this update |

## Safe change pattern

1. Confirm the change belongs to the eBird connector source tree.
2. Confirm imports remain side-effect free.
3. Confirm SourceDescriptor, product-family, rights, time, taxonomy, and sensitivity metadata remain preserved.
4. Confirm exact sensitive location and observer/private metadata cannot leak through outputs, logs, errors, or fixtures.
5. Confirm the change cannot write processed, catalog, triplet, proof, release, or published objects.
6. Add or update offline tests and document any unverified live-service behavior.
7. Update adjacent package and connector documentation when the boundary changes.

## Rollback

Rollback is required when a change:

- introduces import-time network, credential, filesystem, or lifecycle side effects;
- bypasses SourceDescriptor activation or sensitivity review;
- leaks exact sensitive locations or private/observer metadata;
- collapses product families or strengthens source authority without evidence;
- writes outside raw/quarantine admission boundaries;
- claims runtime, test, or release maturity without proof.

Rollback target for this creation: prior placeholder blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual source-tree contents are inventoried.
- [ ] Package layout, discovery, dependencies, imports, and public exports are documented.
- [ ] SourceDescriptor IDs and product-family activation are verified.
- [ ] Imports are proven side-effect free.
- [ ] Sensitive-location and observer/private-data handling is proven fail-closed.
- [ ] Offline tests cover metadata, digests, product-family separation, and bounded outcomes.
- [ ] Outputs are proven to enter only raw/quarantine admission lanes.
- [ ] No source-family, fauna, taxonomy, policy, schema, catalog, triplet, proof, release, publication, fixture, or report authority lives here.
- [ ] CI and runtime behavior are verified or explicitly marked `NEEDS VERIFICATION`.

## Status summary

`connectors/ebird/src/` is the eBird connector Python source-root only. It supports descriptor-gated intake and raw/quarantine admission; it is not source-family truth, fauna truth, taxonomy authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, fixture authority, or generated-report storage.

<p align="right"><a href="#top">Back to top</a></p>
