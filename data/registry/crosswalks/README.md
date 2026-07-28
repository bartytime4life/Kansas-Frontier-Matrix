<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/crosswalks/readme
name: Crosswalk Registry README
path: data/registry/crosswalks/README.md
type: data-registry-crosswalks-readme
version: v0.2.0
status: draft
owners:
  - "NEEDS VERIFICATION: registry steward"
  - "NEEDS VERIFICATION: crosswalk steward"
  - "NEEDS VERIFICATION: source and domain stewards"
  - "NEEDS VERIFICATION: contract, schema, and policy stewards"
  - "NEEDS VERIFICATION: validation, proof, and release stewards"
created: 2026-06-28
updated: 2026-07-27
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: governed-crosswalk-mapping-state
path_posture: confirmed-live-registry-lane; crosswalk-record-inventory-unknown; schema-and-validator-coverage-partial; no-public-path
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; evidence-aware; policy-aware; rights-and-sensitivity-fail-closed; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../../receipts/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/crosswalks/README.md
  - ../../../contracts/crosswalks/taxonomy/README.md
  - ../../../contracts/domains/flora/flora_taxon_crosswalk.md
  - ../../../docs/sources/catalog/CROSSWALKS.md
  - ../../../docs/domains/flora/CROSSWALKS.md
  - ../../../docs/domains/hydrology/CROSSWALK_RULES.md
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../tools/validators/hydro/check_crosswalk.py
  - ../../../tests/
  - ../../../fixtures/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - crosswalks
  - mappings
  - authority-ids
  - taxonomy
  - source-fields
  - vocabulary
  - provenance
  - evidence
  - source-role
  - policy-aware
  - correction
  - rollback
  - no-public-path
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 7863cf4cdd330e056cf22880fecc1eda9a545057
  prior_blob: 2048acd39e2acf57e6a55e2f2e3c3cb735e1c993
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  crosswalk_contracts_blob: 7dd131c6b6b5339eb6e433940d7ace169a350dbc
  inspection_date: 2026-07-27
notes:
  - "This README preserves the existing crosswalk registry lane and updates its claims against current repository evidence."
  - "Crosswalk registry records are mapping-state records. They do not define semantic meaning, machine schema shape, policy, validator behavior, proof, catalog closure, release decisions, or public claims."
  - "Current repository evidence confirms crosswalk contracts and at least one executable Hydrology crosswalk validator, but complete registry-record, schema, fixture, test, and CI coverage remains NEEDS VERIFICATION."
  - "No concrete crosswalk registry payload inventory was established for this lane in the inspected scope."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Crosswalk Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Artifact family: registry](https://img.shields.io/badge/family-registry-0969da?style=flat-square)](#repository-fit)
[![Crosswalk rows: mapping claims](https://img.shields.io/badge/crosswalk%20rows-mapping%20claims-8250df?style=flat-square)](#crosswalk-boundary)
[![Public access: denied](https://img.shields.io/badge/public%20access-denied-b42318?style=flat-square)](#lifecycle-and-publication-boundary)
[![Truth posture: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation-and-maintenance)

> Governed registry lane for crosswalk mapping state. It records how identities, fields, names, vocabularies, and relations are mapped without turning those mappings into semantic contracts, proof, policy, release authority, or public truth.

> [!CAUTION]
> A crosswalk row is a consequential mapping claim. Missing anchors, stale authority versions, ambiguity, conflict, rights gaps, sensitivity gaps, or evidence gaps must remain visible and fail closed. Do not silently normalize uncertainty into an accepted mapping.

## Navigation

[Status](#status) · [Scope](#scope) · [Path posture](#path-posture) · [Repository fit](#repository-fit) · [Crosswalk boundary](#crosswalk-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Lifecycle](#lifecycle-and-publication-boundary) · [Validation](#validation-and-maintenance) · [Required checks](#required-checks-before-use) · [Open verification](#open-verification-items) · [Rollback](#rollback)

---

## Status

| Field | Current result |
|---|---|
| Repository path | `data/registry/crosswalks/` — **CONFIRMED** at the pinned base |
| Document lifecycle | `draft` |
| README profile | Registry-lane `BOUNDARY_COMPACT` |
| Artifact family | Crosswalk mapping-state registry |
| Semantic contract home | [`contracts/crosswalks/`](../../../contracts/crosswalks/README.md) |
| Concrete child contract evidence | [`contracts/crosswalks/taxonomy/`](../../../contracts/crosswalks/taxonomy/README.md) |
| Executable validator evidence | [`tools/validators/hydro/check_crosswalk.py`](../../../tools/validators/hydro/check_crosswalk.py) — Hydrology-specific only |
| Concrete registry record inventory | **UNKNOWN** in the inspected scope |
| Complete crosswalk schema family | **NEEDS VERIFICATION** |
| Direct public access | **DENY** |
| KFM publication effect | None |
| Accountable stewardship assignments | **NEEDS VERIFICATION** |

A file, row, valid schema instance, passing validator, catalog entry, or merged pull request does not establish mapping truth, release approval, or publication.

---

## Scope

`data/registry/crosswalks/` stores governed mapping-state records across KFM object families, source systems, authority systems, names, identifiers, fields, vocabularies, and domain lanes.

A crosswalk registry record may answer bounded questions such as:

- Which source-native identifier maps to which KFM identity, candidate identity, authority identifier, vocabulary term, field, or relation?
- Which source descriptor, authority namespace, authority version, retrieval time, review state, evidence support, and policy posture support the mapping?
- Is the mapping exact, inferred, provisional, ambiguous, conflicted, stale, deprecated, denied, superseded, or withdrawn?
- Which downstream consumers may rely on it, and which must abstain, hold, deny, or require review?
- Which correction, supersession, redaction, release, and rollback constraints apply?

This lane stores mapping state and registry-local indexes. It does not define what a crosswalk means, how its schema is shaped, whether use is allowed, whether evidence is sufficient, or whether a public release is approved.

---

## Path posture

The current path is a registry lane under the canonical `data/` responsibility root:

```text
data/registry/crosswalks/
```

Adopted Directory Rules v2 recognizes `registry` as an accountability plane under `data/`. Crosswalk mapping-state records therefore belong here rather than under a new root or inside the semantic-contract tree.

This path must not absorb:

- crosswalk semantic contracts from `contracts/crosswalks/`;
- machine schemas from `schemas/`;
- policy from `policy/`;
- validator code from `tools/`, packages, or pipelines;
- receipts, proofs, catalogs, or release decisions;
- public API, map, search, graph, export, or AI payloads.

No alternate crosswalk-registry writer or migration conflict was established in the inspected scope. Complete record inventory and machine enforcement remain unresolved.

---

## Repository fit

| Responsibility | Owning surface | Relationship to this lane |
|---|---|---|
| Registry governance | [`data/registry/README.md`](../README.md) | Parent responsibility and registry boundary |
| Crosswalk mapping state | `data/registry/crosswalks/` | Mapping records, state indexes, correction and supersession pointers |
| Source identity and role | [`data/registry/sources/`](../sources/README.md) | SourceDescriptor, rights, cadence, role, and authority inputs |
| Semantic meaning | [`contracts/crosswalks/`](../../../contracts/crosswalks/README.md) and domain contracts | Defines mapping semantics and invariants |
| Machine shape | `schemas/contracts/v1/` | Schema authority; exact crosswalk schema family needs verification |
| Policy | `policy/` | Admissibility, source-role, rights, sensitivity, and public-use decisions |
| Validator code | `tools/`, `packages/`, and `pipelines/` | Executable validation and resolution logic |
| Validation receipts | `data/receipts/` | Run-specific process memory, not registry truth |
| Evidence and proof | `data/proofs/` | EvidenceBundle, proof, citation, integrity, and review support |
| Catalog and discovery | `data/catalog/` | STAC/DCAT/PROV and catalog closure |
| Release and correction | `release/` | Promotion, correction, withdrawal, supersession, rollback, and manifest authority |
| Public consumers | Governed APIs and released artifacts | Must not read registry internals directly |

The current repository also contains domain-specific crosswalk contracts and documentation, including Flora, Fauna, Habitat, Hydrology, Atmosphere, and Settlements/Infrastructure surfaces. Those documents do not automatically create registry records here.

---

## Crosswalk boundary

| Rule | Required handling |
|---|---|
| Crosswalk row is a claim | Consequential mappings must be evidence-bound, reviewable, correctable, and rollback-aware. |
| Preserve source-native values | Keep source names, IDs, fields, vocabularies, statuses, versions, and authority namespaces. |
| Preserve both sides' identity | A crosswalk links identities; it must not silently replace one side with the other. |
| Preserve source role | Do not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, contextual, or restricted material through mapping. |
| Preserve temporal context | Record source/authority version time, retrieval time, review time, release time, and supersession time where material. |
| Preserve mapping class | Exact, equivalent, synonym, broader, narrower, inferred, ambiguous, rejected, and denied are not interchangeable. |
| Fail closed on uncertainty | Use contract-defined finite outcomes or explicit unresolved state; never coerce ambiguity into acceptance. |
| Registry is not semantic authority | Meaning remains under `contracts/`. |
| Registry is not proof or release | Evidence closure and release decisions retain separate authority homes. |
| AI and maps are downstream | Generated text, graph projections, tiles, and map proximity cannot prove a mapping. |

Outcome vocabularies vary by applicable contract and validator. This README does not invent one universal enum. Where a contract uses `ALLOW`, `DENY`, `ABSTAIN`, `ERROR`, `HOLD`, `CONFLICT`, or another finite state, preserve that surface exactly.

---

## Accepted material

This lane may contain only crosswalk registry records and registry-local support material, including:

- authority-identifier mappings;
- source-field to canonical-field mappings;
- taxonomy, name, and synonym mappings;
- vocabulary and controlled-term mappings;
- domain-to-domain relation mappings;
- public-safe derived mapping records after applicable policy and review gates;
- candidate, ambiguity, conflict, denial, stale, supersession, withdrawal, correction, and rollback state;
- pointer-only references to source descriptors, contracts, schemas, policies, evidence, receipts, proofs, catalogs, releases, corrections, and rollback objects;
- registry-local indexes that do not become proof, catalog, search, vector, graph, map, release, or generated-answer authority;
- integrity metadata for registry state where the governing contract requires it;
- README files that explain the registry boundary.

Registry records should remain compact and pointer-based. Do not embed source payloads or duplicate authority objects.

---

## Exclusions

| Do not place here | Owning surface |
|---|---|
| Raw source payloads, full extracts, restricted tables, private identifiers, tokens, or credentials | `data/raw/`, `data/work/`, `data/quarantine/`, or approved restricted storage |
| Crosswalk semantic contract documents | `contracts/crosswalks/` or domain contract lanes |
| JSON Schema or machine contract shape | `schemas/contracts/v1/` |
| Policy, rights, sensitivity, access-control, or release rules | `policy/` |
| Validator/resolver code or transformation logic | `tools/`, `packages/`, `pipelines/`, or `connectors/` |
| Fixtures and tests | `fixtures/` and `tests/` |
| Run or validation receipts | `data/receipts/` |
| EvidenceBundle, proof packs, signatures, or citation closure | `data/proofs/` |
| STAC, DCAT, PROV, catalog, or discovery records | `data/catalog/` |
| Published artifacts, layers, tiles, reports, dashboards, API payloads, graph exports, or generated answers | `data/published/` and governed delivery surfaces after release |
| Release manifests, promotion decisions, correction notices, withdrawal notices, supersession notices, or rollback cards | `release/` |
| Documentation-only crosswalk registers | `docs/` lanes such as `docs/sources/catalog/CROSSWALKS.md` |

---

## Lifecycle and publication boundary

```mermaid
flowchart LR
  S[Source and authority values] --> C[Semantic crosswalk contract]
  C --> R[Registry mapping state]
  C --> V[Schema and validator]
  S --> E[EvidenceRef / EvidenceBundle]
  R --> V
  E --> V
  V --> P[Policy and review]
  P --> K[Catalog / triplet candidate]
  K --> L[Release decision]
  L --> U[Governed public-safe consumer]
```

The diagram shows responsibility flow, not implementation maturity. Registry state does not bypass validation, evidence, policy, catalog, review, release, correction, or rollback.

| Transition | Minimum posture |
|---|---|
| Candidate mapping enters registry | Stable source/target identities, explicit mapping class, source role, authority/version context, and unresolved state visible |
| Mapping becomes dependable processed support | Applicable contract/schema validation, evidence support, conflict checks, rights/sensitivity checks, and review |
| Mapping contributes to catalog/triplet output | Provenance and catalog closure; derived relationship remains evidence-subordinate |
| Mapping reaches a public surface | Governed release, public-safe transform where needed, correction path, rollback target, and consumer caveats |

---

## Validation and maintenance

### Confirmed evidence

- The target README and path exist.
- `contracts/crosswalks/README.md` exists and defines crosswalk semantic boundaries.
- `contracts/crosswalks/taxonomy/README.md` exists.
- Multiple domain-specific crosswalk documents exist.
- `tools/validators/hydro/check_crosswalk.py` exists as executable Hydrology-specific validation evidence.

### Needs verification

- Complete child and payload inventory under `data/registry/crosswalks/`.
- A canonical crosswalk registry schema and `$id`.
- Registry-wide validators, fixtures, negative cases, and CI wiring.
- Which domain validators write or consume registry state.
- Crosswalk correction, supersession, and rollback behavior in emitted artifacts.
- Public API, MapLibre, graph, search, export, and AI consumer behavior.
- Accountable steward and reviewer assignments.

Passing a domain validator proves only its declared scope. It does not establish registry-wide conformance or public release readiness.

---

## Required checks before use

- [ ] Confirm the record belongs under `data/registry/crosswalks/`, not a contract, schema, policy, source, receipt, proof, catalog, release, or delivery root.
- [ ] Confirm stable source and target identities, namespaces, versions, and labels.
- [ ] Preserve source-native values and each participating source/domain's authority.
- [ ] Make mapping class and uncertainty explicit.
- [ ] Confirm source role is preserved and not upgraded by normalization, inference, aggregation, graph projection, mapping, AI, or release.
- [ ] Confirm authority currency, temporal scope, and stale-state behavior.
- [ ] Resolve or explicitly preserve ambiguity, conflict, denial, rights, sensitivity, and evidence gaps.
- [ ] Resolve consequential EvidenceRefs to EvidenceBundles before authoritative use.
- [ ] Confirm applicable contract, schema, policy, validator, fixture, receipt, proof, catalog, release, correction, and rollback references.
- [ ] Confirm no public client or generated-answer surface reads candidate or internal mapping rows directly.
- [ ] Confirm no credential, private identifier, restricted relationship, or harmful precision is exposed.

---

## Open verification items

| Item | Status | Required evidence |
|---|---:|---|
| Complete registry inventory | **UNKNOWN** | Pinned recursive tree and content classification |
| Canonical registry-record schema | **NEEDS VERIFICATION** | Accepted schema path, `$id`, fields, enums, compatibility policy |
| Registry-wide validator coverage | **NEEDS VERIFICATION** | Validator source, fixtures, commands, and representative runs |
| Source/target authority versioning | **NEEDS VERIFICATION** | Contract and registry examples with stale/superseded cases |
| Correction and rollback propagation | **NEEDS VERIFICATION** | Corrected mapping fixture, receipt, catalog/release delta, consumer behavior |
| Public-consumer isolation | **NEEDS VERIFICATION** | API/UI/search/graph tests denying internal or candidate registry reads |
| Steward assignments | **NEEDS VERIFICATION** | CODEOWNERS or accepted authority register |

---

## Rollback

Before merge, close the draft pull request and leave the branch unmerged.

After merge, revert the documentation commit and repeat the Markdown, link, sensitive-content, and changed-path checks. Documentation rollback must not delete or rewrite registry records, source payloads, receipts, proofs, catalogs, release objects, correction history, or published artifacts.

A future crosswalk-record correction must preserve the prior mapping state and add explicit correction or supersession lineage rather than silently overwriting history.

---

## Maintainer rule

```text
source and authority values
  -> semantic contract
  -> governed mapping-state record
  -> evidence + validation + policy + review
  -> catalog/release candidate
  -> governed public-safe consumer
```

Never collapse the chain into:

```text
similar names, IDs, fields, or geometry
  -> accepted identity or relationship
```

[Back to top](#top)
