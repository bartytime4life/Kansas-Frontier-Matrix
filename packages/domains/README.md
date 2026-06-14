<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-domains-readme
title: Domain Packages README
type: readme
version: v0.1
status: draft
owners:
  - <package-owner>
  - <domain-stewards>
  - <schema-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: packages/domains/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/README.md
  - packages/README.md
  - pipelines/domains/README.md
  - pipeline_specs/README.md
  - contracts/domains/
  - schemas/contracts/v1/domains/
  - policy/domains/
  - tests/packages/domains/
  - fixtures/packages/domains/
  - data/proofs/evidence_bundle/
  - release/manifests/
tags: [kfm, packages, domains, shared-library, domain-lanes, mapping-helpers, identity-normalizers, observation-parsers, adapters, governance]
notes:
  - "This README expands the short packages/domains stub into a governed shared-package contract."
  - "packages/ contains shared libraries; packages/domains/ may contain reusable per-domain helper code such as mappers, identity normalizers, observation parsers, adapters, and validation helpers."
  - "docs/domains/ explains domain scope; contracts define meaning; schemas define machine shape; policy defines admissibility; pipelines execute transformations; packages/domains provides reusable code only."
  - "Domain package helpers cannot decide domain truth, policy, evidence closure, lifecycle promotion, release, or public display by themselves."
  - "Concrete child packages, language runtime, package manifests, exports, build scripts, tests, and CI coverage remain NEEDS VERIFICATION until repository evidence proves them."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Packages

> Shared library root for per-domain KFM helper code: mapping helpers, identity normalizers, observation parsers, crosswalk adapters, DTO/type adapters, and validation utilities. This root supports domain apps, pipelines, tests, and tools, but it is not domain doctrine, schema authority, contract authority, policy authority, lifecycle data, executable pipeline logic, evidence closure, or release approval.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-shared%20library-0a7ea4)
![domains](https://img.shields.io/badge/domain%20doctrine-docs%2Fdomains%2F-d62728)
![pipelines](https://img.shields.io/badge/executable-pipelines%2Fdomains%2F-d62728)

**Status:** Draft  
**Path:** `packages/domains/README.md`  
**Responsibility root:** `packages/` — shared libraries used by apps, workers, pipelines, and tools  
**Domain doctrine root:** `docs/domains/` — human-facing domain scope, status, and verification index  
**Executable domain-pipeline root:** `pipelines/domains/`  
**Declarative domain-pipeline-spec root:** `pipeline_specs/`  
**Contract/schema/policy roots:** `contracts/domains/`, `schemas/contracts/v1/domains/`, and `policy/domains/`  
**Placement posture:** `packages/domains/` may host reusable domain helper code only when it remains subordinate to doctrine, contracts, schemas, policy, lifecycle, evidence, and release authority.  
**Public posture:** no public API, no direct lifecycle-store reads for public clients, no policy decision, no EvidenceBundle fabrication, no release approval, and no domain truth authority.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Domain package responsibility boundary](#3-domain-package-responsibility-boundary)
- [4. Package anti-collapse rules](#4-package-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Package scope](#7-package-scope)
- [8. Domain slug posture](#8-domain-slug-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal package contract shape](#12-minimal-package-contract-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`packages/domains/` is a shared-library lane for reusable domain-specific code that is not itself an executable pipeline, API server, schema home, policy home, or data lifecycle home.

It may support:

- per-domain mapping helpers;
- source-to-domain adapter helpers;
- identity normalization utilities;
- observation parsers;
- domain DTO or type adapters generated from canonical schemas;
- crosswalk helpers that preserve source-role boundaries;
- fixture builders for package tests;
- validation adapters that call canonical schemas without replacing them;
- shared helper modules used by apps, pipelines, workers, and tools.

It does **not** define domain meaning, decide policy, create EvidenceBundles, promote lifecycle data, publish artifacts, or approve release.

Short rule:

```text
packages/domains/              = reusable domain helper libraries
docs/domains/                  = human-facing domain doctrine and indexes
contracts/domains/             = domain object meaning
schemas/contracts/v1/domains/  = domain machine shape
policy/domains/                = domain policy/admissibility
pipelines/domains/             = executable domain transformations
pipeline_specs/                = declarative run configuration
data/                          = lifecycle state, receipts, proofs, catalog/triplets, artifacts
release/                       = release decisions and rollback/correction control
```

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `packages/`? | This root owns shared libraries used by apps, workers, pipelines, and tools. | CONFIRMED root contract |
| Why `domains/` under packages? | Domain helper code can be shared without becoming domain doctrine, pipeline logic, or data storage. | CONFIRMED stub intent / NEEDS VERIFICATION for implementation |
| Is this domain doctrine? | No. Human-facing domain doctrine and indexes belong under `docs/domains/`. | CONFIRMED boundary posture |
| Is this executable domain pipeline logic? | No. Executable domain pipeline logic belongs under `pipelines/domains/`. | CONFIRMED boundary posture |
| Can this define schemas or contracts? | No. It may consume generated types, but schema and contract authority stay in their roots. | CONFIRMED authority separation |
| Can this decide policy, evidence, or release? | No. It may preserve refs and validation results only. | CONFIRMED policy/evidence/release separation |

> [!IMPORTANT]
> Domain helper code can normalize and translate. It cannot make a claim true, decide that source material is admissible, bypass policy, publish an artifact, or replace EvidenceBundle closure.

[⬆ Back to top](#top)

---

## 3. Domain package responsibility boundary

Allowed direction:

```text
domain app / pipeline / worker / test
  -> packages/domains/<domain> helper
  -> normalized identifiers, parsed observations, mapped DTOs, validation inputs, or safe fixture objects
  -> governed pipeline/API/tool handles lifecycle, policy, evidence, and release where authorized
```

Blocked direction:

```text
packages/domains/<domain> helper
  -> direct RAW / WORK / QUARANTINE / PROCESSED / PUBLISHED writes
  -> domain truth decision
  -> policy decision
  -> EvidenceBundle creation
  -> catalog truth
  -> release approval
  -> public trust membrane bypass
```

The package should favor pure, deterministic, side-effect-minimal helpers. Any future IO capability must be explicit, bounded, test-covered, reviewable, and owned by an executable app, pipeline, worker, or tool lane.

[⬆ Back to top](#top)

---

## 4. Package anti-collapse rules

Disallowed collapses:

```text
shared package -> domain doctrine
helper function -> domain truth
normalizer -> identity authority
parser -> observation truth
crosswalk -> source authority
DTO adapter -> schema authority
type alias -> contract authority
validation helper -> validation pass
successful package test -> lifecycle promotion
release ref helper -> release approval
public helper -> governed API bypass
```

Required separations:

- shared domain helper code stays under `packages/domains/`;
- domain doctrine stays under `docs/domains/`;
- domain meaning stays under `contracts/domains/`;
- domain schemas stay under `schemas/contracts/v1/domains/`;
- domain policy stays under `policy/domains/` and sensitivity/source policy roots;
- executable domain transformations stay under `pipelines/domains/`;
- declarative run profiles stay under `pipeline_specs/`;
- lifecycle records and receipts stay under `data/`;
- EvidenceBundles stay under proof homes;
- release decisions stay under `release/`;
- public clients consume governed API envelopes and released artifacts, not package internals.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include:

- per-domain helper libraries;
- mapping helpers between source fields and domain DTOs;
- identity normalization utilities that preserve provenance and uncertainty;
- observation parsing utilities that preserve source role, source time, valid time, and limitations;
- crosswalk helpers that preserve native values and do not overwrite source classifications;
- schema-generated adapters with generation provenance;
- deterministic id helper utilities when policy and schema allow;
- safe fixture builders and mock helpers for package tests;
- compatibility helpers for domain helper migrations.

A good placement test:

> If the file is reusable domain helper code that remains subordinate to contracts, schemas, policy, lifecycle, evidence, and release controls, it may belong here. If it decides truth, runs a pipeline, reads/writes lifecycle data, or defines object meaning, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain doctrine and scope docs | `docs/domains/<domain>/` |
| Domain object contracts | `contracts/domains/<domain>/` |
| Domain schemas | `schemas/contracts/v1/domains/<domain>/` |
| Domain policy decisions/rules | `policy/domains/<domain>/` and accepted policy roots |
| Executable domain pipelines | `pipelines/domains/<domain>/` |
| Declarative pipeline specs | `pipeline_specs/<domain>/` |
| Source descriptors | `data/registry/sources/<domain>/` |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Runtime receipts | `data/receipts/` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API routes | `apps/governed-api/` |
| UI-only rendering components | `apps/explorer-web/` or accepted UI package roots |
| Package tests | `tests/packages/domains/` |
| Package fixtures | `fixtures/packages/domains/` unless package-local convention is accepted |

[⬆ Back to top](#top)

---

## 7. Package scope

`packages/domains/` may support code for KFM domain lanes such as:

- Agriculture;
- Air and Atmosphere;
- Archaeology;
- Fauna;
- Flora;
- Geology;
- Habitat;
- Hazards;
- Hydrology;
- People / DNA / Land;
- Roads / Rail / Trade;
- Settlements / Infrastructure;
- Soil.

Domain helper modules must preserve each domain's sensitivity and source-role boundaries. Examples include rare-species redaction posture, archaeology exact-location denial, People/DNA/Land privacy gates, Roads/Rail/Trade access/legal-route separation, Soil support-type separation, and Settlements/Infrastructure legal/operational-status separation.

[⬆ Back to top](#top)

---

## 8. Domain slug posture

Canonical domain slugs should mirror the accepted domain-lane register and responsibility roots. Current doctrine identifies these domain slugs:

```text
hydrology
soil
fauna
flora
habitat
geology
atmosphere
roads-rail-trade
settlements-infrastructure
archaeology
hazards
agriculture
people-dna-land
```

Alias or compatibility lanes such as `air`, `people`, or `settlement` must not become parallel authorities without ADR and migration notes.

[⬆ Back to top](#top)

---

## 9. Required gates

Before any domain helper package is used by production callers, it should have:

1. **Placement gate** — domain slug and package path aligned with accepted domain-lane posture.
2. **Schema gate** — generated or hand-written adapters reconciled with canonical schemas.
3. **Contract gate** — helper behavior does not redefine object meaning.
4. **Source-role gate** — helpers preserve source roles, provenance, and limitations.
5. **Lifecycle gate** — no hidden lifecycle reads/writes or promotions.
6. **Policy gate** — no helper decides sensitivity, rights, or admissibility outcomes.
7. **Evidence gate** — no helper creates EvidenceBundles or fabricates refs.
8. **Release gate** — no helper approves release or public display.
9. **Fixture gate** — no-network tests and synthetic/sanitized fixtures.
10. **Review gate** — affected domain steward, package owner, schema steward, evidence steward, and policy steward review for trust-bearing changes.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
packages/domains/
├── README.md
├── agriculture/                  # PROPOSED
├── air/                          # PROPOSED alias/compatibility if retained
├── archaeology/                  # PROPOSED
├── atmosphere/                   # PROPOSED
├── fauna/                        # PROPOSED
├── flora/                        # PROPOSED
├── geology/                      # PROPOSED
├── habitat/                      # PROPOSED
├── hazards/                      # PROPOSED
├── hydrology/                    # PROPOSED
├── people-dna-land/              # PROPOSED
├── roads-rail-trade/             # PROPOSED
├── settlements-infrastructure/   # PROPOSED
└── soil/                         # PROPOSED
```

Child package shape is language/runtime dependent and remains `NEEDS VERIFICATION`. Do not add parallel slug homes or generated output folders without package manifest evidence, generation provenance, tests, and a migration note.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Package source | `packages/domains/<domain>/` | Shared helper source only. |
| Domain doctrine | `docs/domains/<domain>/` | Scope and human-facing control plane. |
| Domain contracts | `contracts/domains/<domain>/` | Object meaning authority. |
| Domain schemas | `schemas/contracts/v1/domains/<domain>/` | Machine shape authority. |
| Domain policy | `policy/domains/<domain>/` | Admissibility/exposure authority. |
| Executable domain pipeline | `pipelines/domains/<domain>/` | Runs transformations. |
| Declarative domain spec | `pipeline_specs/<domain>/` | Configures pipeline runs. |
| Lifecycle data | `data/<phase>/<domain>/` | Not written by helpers as hidden behavior. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced, not fabricated. |
| Release refs | `release/` | Referenced, not approved. |
| Tests | `tests/packages/domains/` | Package validation. |
| Fixtures | `fixtures/packages/domains/` | No-network package fixtures. |

[⬆ Back to top](#top)

---

## 12. Minimal package contract shape

```yaml
package_id: kfm.packages.domains
status: draft
authority: shared_library_root
not_authority_for:
  - domain_doctrine
  - object_contract
  - schema_home
  - policy_decision
  - lifecycle_write
  - evidence_bundle
  - release_decision
allowed_responsibilities:
  - mapping helpers
  - identity normalizers
  - observation parsers
  - crosswalk adapters
  - schema-bound adapters
  - safe fixture builders
required_invariants:
  no_hidden_lifecycle_writes: true
  no_policy_bypass: true
  no_evidence_fabrication: true
  no_release_approval: true
  helper_output_is_not_truth: true
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/packages/domains/
├── test_domain_package_boundaries.py        # PROPOSED
├── test_slug_alignment.py                   # PROPOSED
├── test_helpers_do_not_define_contracts.py  # PROPOSED
├── test_helpers_do_not_decide_policy.py     # PROPOSED
├── test_no_hidden_lifecycle_writes.py       # PROPOSED
├── test_evidence_refs_preserved.py          # PROPOSED
├── test_release_refs_not_approved.py        # PROPOSED
├── test_generated_types_match_schema.py     # PROPOSED
└── test_root_boundary.py                    # PROPOSED
```

Fixture material should live in `fixtures/packages/domains/` unless a package-local fixture convention is explicitly accepted. Fixtures should be synthetic or sanitized and must not contain sensitive exact-location, private-person, DNA/genomic, restricted-infrastructure, or other controlled material unless the fixture policy explicitly permits it.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- expands the short `packages/domains/README.md` stub;
- identifies `packages/domains/` as shared per-domain helper-code space;
- preserves docs, contracts, schemas, policy, pipelines, pipeline specs, data, evidence, and release roots as separate authorities;
- blocks domain helpers from becoming doctrine, schema, contract, policy, lifecycle, evidence, release, or public-trust authority;
- defines expected package scope, slug posture, root boundaries, tests, fixtures, and open questions.

Future package files are done only when they are schema-aligned, test-covered, steward-reviewed, deterministic where practical, and unable to bypass domain doctrine, lifecycle, evidence, policy, and release controls.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PKG-DOMAINS-001` | Which domain helper child packages currently exist and which are planned? | NEEDS VERIFICATION |
| `PKG-DOMAINS-002` | Which language/runtime owns `packages/domains/` child packages? | UNKNOWN |
| `PKG-DOMAINS-003` | Which package manifest controls this root, if any? | UNKNOWN |
| `PKG-DOMAINS-004` | Should alias lanes such as `air`, `people`, or `settlement` exist under packages/domains? | NEEDS VERIFICATION / ADR |
| `PKG-DOMAINS-005` | Which CI workflow validates domain helper packages? | UNKNOWN |
| `PKG-DOMAINS-006` | Should generated domain adapters live here, under generated-code roots, or beside schemas? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this root helper-focused and subordinate to domain governance. Do not add domain doctrine, source descriptors, schema authority, contract authority, policy decisions, lifecycle writers, EvidenceBundle writers, release decisions, public API routes, UI behavior, sensitive raw examples, or generated truth claims here.
