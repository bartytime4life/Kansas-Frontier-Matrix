<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-people-readme
title: connectors/people/ — Governed People Short-Name Compatibility Boundary
type: readme
version: v0.2
status: draft; repository-grounded; readme-only; restricted-compatibility-alias; no-active-implementation-established
owners: OWNER_TBD — Connector steward · Source steward · People/DNA/Land steward · Living-person privacy steward · Consent and revocation steward · DNA/genomic steward · Land-records steward · Rights reviewer · Sensitivity reviewer · Security steward · Data steward · Migration steward · Validation steward · CI steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-07-15
supersedes: v0.1
policy_label: restricted-doctrine; compatibility-alias; people; people-dna-land; living-person-sensitive; dna-genomic-restricted; private-person-parcel-deny-default; consent-revocation-aware; quarantine-first; no-network; no-package; no-source-tree; no-tests; no-descriptors; no-data; no-receipts; no-publication; migration-gated
current_path: connectors/people/README.md
truth_posture: CONFIRMED target README and README-only short-name lane, connectors responsibility root, fuller connectors/people-dna-land README, People/DNA/Land sensitivity profile, bounded absence of people pyproject/src/tests paths, and current repository references / PROPOSED frozen compatibility class, one-way alias resolution to connectors/people-dna-land, no-new-files enforcement, stable source identity normalization, consent/revocation reference discipline, living-person and DNA fail-closed controls, migration/tombstone procedure, CI guardrails, correction propagation, and rollback requirements / CONFLICTED final people versus people-dna-land naming disposition because no accepted ADR or migration note was verified / UNKNOWN exhaustive recursive alias-lane inventory, active SourceDescriptors, accepted source profiles, executable connector behavior, alias consumers, generated links, CI enforcement, source activation, consent authority, emitted receipts, deployment, and downstream release state / NEEDS VERIFICATION owners, accepted alias class, package/import/config compatibility, canonical source IDs, living-person classifier, consent and revocation enforcement, DNA tokenization, rights and provider terms, validator wiring, correction sweep, deactivation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 21e44bb292afe8227a08b08b47683e581e92fc5b
  prior_blob: 1de551d34bef9f9c03fe1a3b7da5f2a1e6b8356c
  related_repository_blobs:
    connectors_root_readme: bdd50032bed62ac36964c79f16cf5541b21759a6
    fuller_connector_readme: 2ab7b6677b077adba7406a42f56c1efead76dd51
    sensitivity_profile: b599188f22746a5f7b008efa3bf1c91a84713172
  direct_lane_files_confirmed:
    - connectors/people/README.md
  checked_absent_paths:
    - connectors/people/pyproject.toml
    - connectors/people/src/README.md
    - connectors/people/tests/README.md
related:
  - ../README.md
  - ../people-dna-land/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/domains/people-dna-land/README.md
  - ../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../docs/domains/people-dna-land/CANONICAL_PATHS.md
  - ../../docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - ../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - ../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../docs/sources/catalog/ftdna/README.md
  - ../../docs/sources/catalog/ahgp/README.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../schemas/contracts/v1/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../policy/consent/
  - ../../release/
notes:
  - "v0.2 replaces a brief alias note with a commit-pinned, fail-closed compatibility boundary."
  - "The bounded alias lane is README-only. It has no package metadata, source root, tests root, source descriptor family, consent store, fixture lane, receipt emitter, or release path."
  - "connectors/people-dna-land/ is the repository-present fuller connector documentation lane. Final naming disposition remains ADR or migration-note work."
  - "The alias resolves one way and must not create duplicate implementation, split source identity, weaken consent, or bypass sensitivity."
  - "Living-person data, raw DNA/genomic material, raw kit/vendor identifiers, exact sensitive locations, and private person-parcel joins fail closed."
  - "This revision changes documentation only and creates no code, activation, data, receipt, proof, policy decision, or release object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed People Short-Name Compatibility Boundary

`connectors/people/`

> README-only compatibility boundary for the short name **People**. The repository-present fuller connector documentation lane is [`connectors/people-dna-land/`](../people-dna-land/README.md). This path may explain naming and migration posture; it must not become a second connector, package, source tree, test lane, descriptor family, consent store, data lane, receipt path, proof path, or publication authority.

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: restricted compatibility alias" src="https://img.shields.io/badge/scope-restricted__compatibility__alias-blue">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="Sensitivity: deny by default" src="https://img.shields.io/badge/sensitivity-deny__by__default-critical">
  <img alt="Consent: revocation aware" src="https://img.shields.io/badge/consent-revocation__aware-critical">
  <img alt="Network behavior: none" src="https://img.shields.io/badge/network-none-critical">
  <img alt="New implementation files: denied" src="https://img.shields.io/badge/new__implementation-DENIED-red">
  <img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

> [!IMPORTANT]
> **Evidence snapshot:** `main@21e44bb292afe8227a08b08b47683e581e92fc5b`
> **Target blob before this revision:** `1de551d34bef9f9c03fe1a3b7da5f2a1e6b8356c`
> **Bounded alias-lane result:** this README only
> **Checked absent alias implementation paths:** `pyproject.toml`, `src/README.md`, and `tests/README.md`
> **Repository-present fuller connector documentation lane:** [`connectors/people-dna-land/`](../people-dna-land/README.md)
> **Activation:** an alias, link, import string, source-list entry, workflow result, consent reference, or future redirect activates nothing

> [!CAUTION]
> `people` is a short label, not a separate source family, privacy class, consent authority, identity authority, DNA authority, land-title authority, package, service, or release lane. Do not mint a second source identity or weaker policy path merely because both spellings exist.

> [!WARNING]
> Do not add connector clients, package code, tests, fixtures, credentials, provider profiles, source descriptors, consent artifacts, living-person records, DNA/genomic material, land records, downloaded data, receipts, proofs, release objects, public routes, or generated outputs under `connectors/people/`.

---

## Status and evidence boundary

`connectors/people/` is a repository-present, README-only compatibility lane. `connectors/people-dna-land/` is the fuller restricted connector documentation lane. No accepted ADR or migration note was verified that permanently declares either spelling canonical.

- **CONFIRMED:** this README exists; checked alias package, source-root, and tests-root paths do not.
- **CONFIRMED:** People/DNA/Land doctrine is deny-by-default for living-person identity, raw DNA/genomic material, raw kit/vendor identifiers, and private person-parcel joins.
- **PROPOSED:** freeze this lane as a one-way compatibility alias.
- **CONFLICTED:** final `people` versus `people-dna-land` naming remains unresolved.
- **UNKNOWN:** exhaustive inventory, active descriptors, consumers, runtime enforcement, receipts, deployment, and release state.

---

## Purpose and authority

This README prevents the short name `people` from becoming a parallel connector, source identity, consent store, policy surface, data lane, proof lane, or release path.

```text
connectors/people/
  -> compatibility explanation only
  -> connectors/people-dna-land/
  -> fuller restricted connector documentation
```

The alias may own only this README and future approved redirect or tombstone metadata. It must not own code, packages, tests, fixtures, source descriptors, consent records, living-person classifications, DNA material, genealogy data, land records, data artifacts, receipts, proofs, releases, or public surfaces.

The alias cannot activate a source, grant consent, establish identity or kinship, interpret DNA as relationship truth, determine title, close evidence, or publish.

---

## Repository fit and current inventory

```text
connectors/
├── people-dna-land/
│   └── README.md              # fuller restricted boundary
└── people/
    └── README.md              # this compatibility lane
```

Checked and not found:

```text
connectors/people/pyproject.toml
connectors/people/src/README.md
connectors/people/tests/README.md
```

This is bounded evidence, not exhaustive recursive proof. The safe state is `README_ONLY`, `NETWORK_DISABLED`, `NO_PACKAGE`, `NO_SOURCE_TREE`, `NO_TESTS`, `NO_SOURCE_DESCRIPTORS`, `NO_CONSENT_STORE`, `NO_DATA`, `NO_RECEIPTS`, `NO_PROOFS`, and `NO_RELEASE`.

Files belong under the root that owns their responsibility: source descriptors under `data/registry/sources/`, policy under `policy/`, lifecycle data under `data/`, proofs under `data/proofs/`, and release decisions under `release/`.

---

## Compatibility and identity contract

Current proposed state: `COMPATIBILITY_ALIAS`.

A transition to redirect, tombstone, or canonical lane requires an accepted decision, owner assignment, consumer inventory, stable identity mapping, privacy and consent review, package/config compatibility analysis, negative fixtures, CI guardrails, correction, and rollback.

Repository path, connector family, package/import name, source family, SourceDescriptor, consent record, person assertion, DNA evidence token, land instrument, receipt, EvidenceBundle, and release ID are distinct identity classes. A path alias must not rewrite or collapse them.

A future resolver must normalize aliases before lookup, resolve one stable connector identity, reject conflicts, preserve submitted spelling in audit metadata, and never infer consent, living-person status, rights, or release state. Separate active descriptors differing only by spelling are forbidden.

---

## Sensitive-domain boundaries

### Living-person privacy

When living-person status is true, possible, unresolved, or not evaluated, fail closed for public or broad access. Do not infer death, infer consent from public availability, expose identifying fields, create public people-search indexes, join living people to parcels, downgrade sensitivity, or log sensitive payloads.

### Consent, revocation, and retention

Consent is not a boolean and not an alias property. Resolve subject authority, scope, purpose, audience, data classes, effective time, expiration, revocation, downstream obligations, retention/deletion conditions, review, and policy decision. Missing, expired, revoked, disputed, or out-of-scope consent routes to `DENY` or `QUARANTINE`.

Revocation must be able to deactivate intake, quarantine pending material, trigger deletion or restriction workflows, invalidate derivatives, issue corrections, withdraw access, and emit audit receipts. The alias must not cache or weaken consent state.

### DNA and genomic material

Do not place raw genotype files, DNA segments, kit/vendor identifiers, match lists, genome coordinates, health interpretations, relationship probabilities, re-identification keys, credentials, or screenshots here. DNA evidence may support a hypothesis; it does not by itself create canonical identity, confirmed kinship, legal kinship, inheritance rights, sovereignty status, or public family-tree truth.

### Land records and title

Recorded instruments are evidence of recorded transactions or claims, not automatic current ownership. Assessor and tax records are administrative, not title truth. Parcel geometry is not a legal or title boundary. Private person-parcel joins are restricted and must not become public lookup or map layers. Connectors do not issue title opinions, legal advice, surveys, or ownership guarantees.

---

## Admission, lifecycle, and finite outcomes

The alias does not define source families. Every source requires its own admitted identity, source role, rights posture, sensitivity class, living-person state, consent reference when required, retention posture, provenance, and digest.

A mature connector attempt ends in one of `ADMIT_RAW`, `QUARANTINE`, `DENY`, `NO_OP`, or `ERROR`. `ADMIT_RAW` is not validation, identity resolution, proof closure, release, or publication.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move. The alias has no direct authority in any lifecycle phase. Watchers may detect change but cannot activate sources, grant consent, determine identity, release DNA evidence, establish title, or publish.

---

## Validation and CI guardrails

Proposed negative tests must fail when the alias gains package/source/tests content, an unknown or ambiguous spelling is accepted, descriptors split by spelling, consent is missing or revoked, living-person status is unresolved but exposed, raw DNA or private joins reach public fixtures, assessor records are asserted as title truth, import causes network access, source role changes, or the alias emits a release object.

Passing documentation or repository CI does not prove production privacy, consent completeness, DNA safety, title correctness, activation, or release readiness.

---

## Migration, correction, and rollback

A migration must accept the naming decision, pin commits, inventory all consumers, classify every reference by authority type, define canonical mappings, identify sensitive references, prepare positive and negative fixtures, migrate in bounded steps, update documentation and generators, verify no duplicate authority, exercise correction and rollback, and retain a redirect or tombstone where historical references require it.

Migration must preserve provenance, descriptor lineage, consent and revocation history, sensitivity decisions, evidence references, receipts, releases, corrections, and rollback targets.

Correction triggers include wrong alias mapping, duplicate descriptors, consent errors, living-person reclassification, DNA mishandling, private join exposure, title-role collapse, stale consumers, or stale release lineage. Reverting this README does not roll back source activation, consent, data, evidence, or releases.

---

## Definition of done

- [x] README-only restricted compatibility surface identified.
- [x] Fuller lane recorded without production claims.
- [x] Checked absence of alias package/source/tests recorded.
- [x] Parallel implementation and authority prevented.
- [x] Quarantine-first, deny-by-default, consent-aware posture preserved.
- [x] Living-person, DNA, title, and private-join boundaries preserved.
- [x] Migration, correction, deactivation, and rollback defined.
- [x] No code, data, policy, or release object changed.
- [ ] Repository-native checks observed after PR creation.

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PEOPLE-ALIAS-001` | Final class of this lane? | `CONFLICTED` |
| `PEOPLE-ALIAS-002` | Is the fuller lane formally canonical? | `NEEDS VERIFICATION` |
| `PEOPLE-ALIAS-003` | Any code, config, schedule, deployment, or notebook consumers? | `UNKNOWN` |
| `PEOPLE-ALIAS-004` | Accepted package/import and machine-alias policy? | `NEEDS VERIFICATION` |
| `PEOPLE-ALIAS-005` | Accepted connector/source IDs and active descriptors? | `NEEDS VERIFICATION` |
| `PEOPLE-ALIAS-006` | Living-person classification and correction implementation? | `NEEDS VERIFICATION` |
| `PEOPLE-ALIAS-007` | Consent, expiry, revocation, retention, and deletion enforcement? | `NEEDS VERIFICATION` |
| `PEOPLE-ALIAS-008` | DNA tokenization and restricted storage controls? | `NEEDS VERIFICATION` |
| `PEOPLE-ALIAS-009` | README-only validator and generated alias registry? | `UNKNOWN` |
| `PEOPLE-ALIAS-010` | Correction sweep and rollback across data, evidence, and releases? | `NEEDS VERIFICATION` |
| `PEOPLE-ALIAS-011` | Title and parcel anti-collapse enforcement? | `NEEDS VERIFICATION` |

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| Prior target blob `1de551d3…` | `CONFIRMED` | Existing alias posture. | Final naming or implementation. |
| Connectors root `bdd50032…` | `CONFIRMED ROOT CONTRACT` | Connector authority boundary. | Source activation. |
| Fuller connector `2ab7b667…` | `CONFIRMED DOCUMENTATION` | Restricted connector posture. | Executable correctness. |
| Sensitivity profile `b599188f…` | `CONFIRMED DOCUMENTATION` | Deny-by-default controls. | Runtime enforcement. |
| Bounded path checks and repository search | `CONFIRMED BOUNDED RESULT` | README-only result and current references. | Exhaustive or external consumers. |

Current repository files, accepted contracts, tests, workflows, logs, and release records outrank planning documents for implementation behavior. The fuller People/DNA/Land connector boundary controls current guidance; this alias cannot override it.

---

## Maintainer note

Keep `connectors/people/` README-only, one-way, and maximally restrictive. Do not create a second package, source tree, tests lane, descriptor family, consent store, person-data lane, DNA lane, parcel-join lane, receipt path, proof path, or release path.

Use [`connectors/people-dna-land/`](../people-dna-land/README.md) for fuller connector documentation and the proper responsibility roots for registry, consent, policy, lifecycle data, proofs, and release decisions.

<p align="right"><a href="#top">Back to top</a></p>
