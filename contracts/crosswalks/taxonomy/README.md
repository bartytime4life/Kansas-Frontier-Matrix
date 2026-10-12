<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-crosswalks-taxonomy-readme
title: contracts/crosswalks/taxonomy/ — Taxonomy Crosswalk Semantic Contracts
type: readme
version: v0.2
status: draft; repository-grounded; one-proposed-executable-fixture-profile; human-review-hold; no-taxonomic-or-release-authority
owners: OWNER_TBD — Contract steward · Taxonomy steward · Flora steward · Fauna steward · Schema steward · Policy steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-09-08
policy_label: public; contracts; crosswalks; taxonomy; semantic-contracts; authority-reconciliation; evidence-aware; non-authoritative
current_path: contracts/crosswalks/taxonomy/README.md
truth_posture: CONFIRMED current directory inventory and repository bindings / PROPOSED taxonomic concept-lineage profile / UNKNOWN live taxonomy authority, accepted shared registry, source admission, policy decisions, downstream dereferencing, release, and public use
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 7f0f034236ff39eb690733bcf869ada67015a7a0
  target_blob_before_revision: 6c93a9cdd7f4fb0be997925674dc949e74ea1db7
  inspected_on: 2026-09-08
related:
  - ../README.md
  - taxonomic_concept_lineage.md
  - ../../../schemas/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage.schema.json
  - ../../../tools/validators/validate_taxonomic_concept_lineage.py
  - ../../../tests/validators/test_validate_taxonomic_concept_lineage.py
  - ../../../.github/workflows/taxonomic-concept-lineage.yml
  - ../../../data/receipts/generated/genrec-taxonomic-concept-lineage-20260805.json
  - ../../../data/receipts/generated/genrec-taxonomic-concept-lineage-contract-currentness-20260908.json
  - ../../../docs/domains/flora/CROSSWALKS.md
  - ../../../packages/domains/flora/taxonomy/README.md
  - ../../../packages/domains/flora/taxonomy_resolver/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "v0.2 reconciles the README with the current two-file directory and the existing taxonomic-concept-lineage contract, schema, validator, tests, workflow, and receipts."
  - "The declared standalone fixture root is absent; compressed synthetic vectors are embedded in the six-test validator module."
  - "Presence, passing fixtures, receipts, or a merged pull request do not create taxonomic, source, evidence, policy, review, release, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Taxonomy Crosswalk Semantic Contracts

> Directory contract for governed taxonomy crosswalk meaning: source-native name usage, versioned taxon concepts, typed concept relations, and reversible reconciliation decisions.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Inventory: verified" src="https://img.shields.io/badge/inventory-verified-blue">
  <img alt="Profile: proposed" src="https://img.shields.io/badge/profile-proposed-orange">
  <img alt="Authority: none" src="https://img.shields.io/badge/taxonomic%20authority-none-red">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-purple">
</p>

`contracts/crosswalks/taxonomy/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Inventory](#current-directory-inventory) · [Responsibility split](#responsibility-split) · [Implemented profile](#implemented-profile) · [Doctrine](#taxonomy-crosswalk-doctrine) · [Lifecycle](#lifecycle-and-trust-boundary) · [Validation](#validation) · [Known gaps](#known-gaps) · [Evidence](#evidence-and-coordination-lineage) · [Rollback](#acceptance-and-rollback)

---

## Status

> [!IMPORTANT]
> **Directory:** `CONFIRMED` at the pinned evidence snapshot.  
> **Concrete profile:** `PROPOSED` `TaxonomicConceptLineagePacket`, with repository-present schema, validator, tests, workflow, and receipts.  
> **Human review:** pending.  
> **Authority:** none. This directory and its companions do not select a live taxonomy, admit sources, prove occurrence, decide policy, release data, or authorize publication.

The prior README said the paired schema, validator, object-level contract, and directory inventory were unverified. Direct current-main inspection now resolves those bounded questions. It does not resolve the runtime and governance gaps listed below.

## Scope

This directory owns semantic meaning and anti-collapse invariants for taxonomy crosswalks. A taxonomy crosswalk is a governed mapping claim, not a free join and not a taxonomic ruling.

It may define:

- source-native name usage and identifier preservation;
- the separation of name strings, name usages, and taxon concepts;
- authority namespace, version, treatment, provenance, and temporal context;
- typed relationships among concepts;
- finite, reversible reconciliation outcomes;
- evidence, source-role, rights, sensitivity, review, correction, and supersession expectations; and
- failure behavior when identity or authority support is insufficient.

It does not own schemas, policy code, validator code, fixtures, registry data, resolver implementations, proof objects, releases, APIs, or UI behavior.

## Current directory inventory

The pinned directory listing contains exactly two files:

| File | Status | What it establishes | Boundary |
|---|---|---|---|
| [`README.md`](README.md) | `CONFIRMED` | Directory scope, inventory, responsibility split, and review posture. | Does not validate a packet or create authority. |
| [`taxonomic_concept_lineage.md`](taxonomic_concept_lineage.md) | `PROPOSED`; executable fixture profile | Meaning and invariants for `TaxonomicConceptLineagePacket` v0.2.1. | Does not establish a live taxonomy, source admission, or release permission. |

No additional object-level contract is implied by a package README, domain narrative, schema, registry note, or proposed path.

## Responsibility split

The accepted Directory Rules, adopted by [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), keep meaning, shape, enforcement, examples, implementation, records, and release authority separate.

| Responsibility | Current repository surface | Verified posture |
|---|---|---|
| Semantic meaning | `contracts/crosswalks/taxonomy/` | This directory; one proposed concrete profile. |
| Machine shape | [`schemas/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage.schema.json`](../../../schemas/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage.schema.json) | `CONFIRMED` JSON Schema Draft 2020-12 for `TaxonomicConceptLineagePacket`; shape is not authority. |
| Semantic validation | [`tools/validators/validate_taxonomic_concept_lineage.py`](../../../tools/validators/validate_taxonomic_concept_lineage.py) | `CONFIRMED` bounded no-network validator; it checks only the local packet profile. |
| Executable examples | [`tests/validators/test_validate_taxonomic_concept_lineage.py`](../../../tests/validators/test_validate_taxonomic_concept_lineage.py) | `CONFIRMED` six deterministic tests with compressed synthetic vectors. |
| Dedicated CI | [`taxonomic-concept-lineage.yml`](../../../.github/workflows/taxonomic-concept-lineage.yml) | `CONFIRMED` path-scoped Python 3.11 workflow for the profile companions and currentness receipt. This README is not in its path filter. |
| Provenance | [retained authoring receipt](../../../data/receipts/generated/genrec-taxonomic-concept-lineage-20260805.json) and [currentness receipt](../../../data/receipts/generated/genrec-taxonomic-concept-lineage-contract-currentness-20260908.json) | `CONFIRMED` repository records; human review remains pending and the retained receipt has a documented cross-revision replay limitation. |
| Fixtures root | `fixtures/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage/` | `ABSENT` at the snapshot although declared in schema metadata; embedded test vectors are the only executable fixtures. |
| Resolver implementation | `packages/...` | Package docs are lineage/proposals, not proof of an accepted shared resolver or runtime. |
| Registry and policy | `data/registry/...`, `policy/...` | No accepted shared taxonomy authority registry or dedicated taxonomy-crosswalk policy bundle is established by this bounded slice. |
| Release and public use | `release/...`, governed consumers | Not granted or established here. |

## Accepted inputs

| Belongs in this directory | Required posture |
|---|---|
| Taxonomy crosswalk semantic contract docs | Define meaning, invariants, provenance, source-role posture, and failure behavior. |
| Authority-reconciliation semantics | Preserve authority IDs and versions without presenting a mapping as sovereign truth. |
| Synonym, accepted-name, and concept-relation semantics | Preserve source-native labels and identity lineage. |
| Reconciliation-decision semantics | Use finite outcomes, record rationale and provenance, remain reversible, and deny automatic authority creation. |
| Cross-lane taxonomy relation semantics | Preserve ownership of Flora, Fauna, occurrence, evidence, sensitivity, and release facts. |
| Compatibility, drift, correction, supersession, and rollback notes | Make conflict and recovery explicit. |

## Exclusions

| Does not belong here | Correct responsibility root |
|---|---|
| JSON Schema | `schemas/contracts/v1/...` |
| Policy decisions and release gates | `policy/...` |
| Validator code | `tools/validators/...` |
| Fixtures and tests | `fixtures/...`, `tests/...` |
| Taxonomy authority or crosswalk registry records | accepted `data/registry/...` home |
| Source descriptors and source roles | `data/registry/sources/...` and source contracts |
| Resolver or package implementation | `packages/...` |
| EvidenceBundle or proof content | `data/proofs/...` |
| Release manifests, correction state, or public admission | `release/...` and release/correction contracts |
| Public API or UI rendering | governed application, API, and UI roots after policy and release decisions |

## Implemented profile

[`taxonomic_concept_lineage.md`](taxonomic_concept_lineage.md) documents one bounded proposed packet with four record families:

| Record family | Meaning | Required separation |
|---|---|---|
| `NameUsage` | What a source and treatment called something. | `usage_id`, not `name_string`, is identity. |
| `TaxonConcept` | A version-bound circumscription. | Separate from every name string and linked to an in-packet accepted usage. |
| `ConceptRelation` | A typed, directed assertion between two concepts. | Evidence-bound, reversible in lineage, and not a merge of the source concepts. |
| `TaxonomyReconciliationDecision` | An accountable outcome under a named profile and authority-role label. | Does not mutate source records; must deny automatic resolution and remain reversible. |

The envelope includes 1–128 name usages, 1–128 taxon concepts, 0–256 concept relations, and 1–128 reconciliation decisions. Its deterministic `spec_hash` detects packet representation changes under `kfm-fixture-json-v1`; it is not a signature, evidence digest, source checksum, or authority grant.

The profile's explicit governance fields must remain false for taxonomic-authority creation, occurrence evidence, source admission, evidence closure, policy decision, review approval, release approval, and publication approval; `release_ref` must remain null.

## Taxonomy crosswalk doctrine

Taxonomy crosswalks are governed mappings. Every consequential mapping must remain inspectable as a claim.

Required posture:

- preserve the source-native name string, identifier, treatment, and version context;
- never use a name string alone as taxon identity;
- distinguish accepted, synonymic, misapplied, homonymous, unresolved, ambiguous, conflicted, rejected, and provisional states where the governing profile supports them;
- preserve source role; an authority assertion is not an observation, a regulatory record is not occurrence evidence, and an aggregate is not a per-place record;
- keep taxonomy separate from occurrence, specimen, range, conservation, rights, sensitivity, and release facts;
- attach evidence and authoring provenance without treating an opaque reference as proof that its target exists or is admitted;
- record authority and profile versions so later changes can be corrected or superseded without erasing lineage;
- fail closed when required identity, evidence, role, rights, sensitivity, or authority anchors are missing; and
- make automated acceptance impossible where the profile requires accountable review.

Drive's Flora builder reinforces the same boundary: synonymy and crosswalks must not erase source-native names or historical identity, and taxonomic identity is not occurrence. That document is read-only lineage; current repository bytes govern implementation claims.

## Semantic contract requirements

Every additional contract in this directory must state:

- the exact object families and their identity bases;
- source-native preservation and authority/version rules;
- finite outcomes and forbidden state collapses;
- evidence, provenance, source-role, temporal, rights, and sensitivity requirements;
- correction, supersession, reversibility, and rollback behavior;
- machine-schema, validator, fixture, test, workflow, and receipt paths where implemented;
- positive and negative examples, including unresolved, conflicting, denied, and review-required cases; and
- explicit non-effects for taxonomic, occurrence, source, policy, review, release, publication, and public-use authority.

## Lifecycle and trust boundary

1. Preserve source-native usage and provenance.
2. Represent version-bound concepts without equating names to identity.
3. Assert typed relations and reconciliation outcomes under a named profile.
4. Validate local shape, reference integrity, hash identity, reversibility, and non-authority assertions.
5. Route consequential or ambiguous outcomes to the applicable steward and policy gates.
6. Admit, release, correct, or supersede only through separately authorized records and workflows.

A schema-valid packet, passing validator, green workflow, generated receipt, approved code review, or merged pull request proves only its stated repository checks. None independently grants source, evidence, policy, taxonomic, review, release, deployment, publication, or public-use authority.

## Validation

### Current executable checks

The validator:

- denies symlink input, non-files, files over 1 MiB, invalid UTF-8/JSON, duplicate keys, non-finite numbers, excessive parser complexity, and non-object roots;
- checks the closed Draft 2020-12 schema and caps schema findings at 100;
- verifies the deterministic `spec_hash`;
- checks in-packet usage/concept references and rejects concept-relation self-loops;
- requires concept references for accepted/provisional decisions;
- rejects acceptance of unresolved, homonymous, or misapplied usages;
- requires reversible decisions, denies automatic resolution, and enforces separation and governance boundary fields; and
- returns machine-readable `PASS`, `FAIL`, or `ERROR` outcomes without echoing candidate values.

The dedicated test module contains six deterministic tests: a valid vector, reviewed negative codes, duplicate-key fail-closed behavior, CLI non-echo behavior, deterministic hashing, and schema validity.

From repository root, the profile's focused commands are:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_taxonomic_concept_lineage.py' \
  --verbose

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-taxonomic-concept-lineage-contract-currentness-20260908.json \
  --repo-root .
```

> [!NOTE]
> A README-only change does not trigger `taxonomic-concept-lineage.yml` because this path is outside that workflow's filter. Reviewers must treat the workflow result on the unchanged profile companions as inherited evidence, not an exact-head execution caused by this documentation edit.

### Documentation checks for this README

- confirm the current directory contains only the two inventoried files;
- resolve every relative repository link at the pinned base;
- verify the named schema, validator, six-test module, workflow, and two receipts are present;
- confirm the standalone fixture root is absent rather than silently claiming fixture completeness;
- confirm the dedicated workflow does not include this README in its trigger paths; and
- compare the pull-request head to its exact base and verify this is a one-file documentation diff.

## Known gaps

The current profile does not establish or enforce:

- a standalone fixture directory wired into the workflow and receipts;
- an accepted live taxonomy authority, shared canonical taxonomy registry, or shared runtime resolver;
- live-source retrieval, source admission, external-reference dereferencing, or evidence closure;
- rights, sensitivity, conservation, source-role, policy, steward-review, promotion, release, or publication decisions;
- uniqueness of every semantic identifier, relation identifier, or decision identifier beyond the exact checks documented by the validator;
- cycle detection, transitive consistency, or contradiction detection across concept relations;
- split/lump-specific evidence rules beyond nonempty evidence references;
- downstream dereferencing of `taxonomic_concept_lineage_ref` in the PLANTS taxa-drift assessment family;
- single-revision replay of the retained 2026-08-05 receipt, whose documented authoring-time and later-refreshed bindings span revisions; or
- owners and final release authority, which remain `OWNER_TBD` / `UNKNOWN`.

Close any executable gap with the smallest dependency-complete change across contract, schema, validator, fixtures, tests, workflow paths, and receipts as applicable. Do not expand this directory README into a parallel authority home.

## Evidence and coordination lineage

| Source | Status | Supports | Limit |
|---|---|---|---|
| GitHub `main@7f0f034236ff39eb690733bcf869ada67015a7a0` and direct path inspection | `CONFIRMED` implementation evidence | Exact two-file directory, current companion paths, workflow filter, absent fixture root, and prior README blob. | Repository presence and merge history do not grant taxonomic or release authority. |
| [`taxonomic_concept_lineage.md`](taxonomic_concept_lineage.md) and its currentness receipt | `PROPOSED` profile / `CONFIRMED` repository records | Exact packet meaning, checks, gaps, provenance, and review hold. | Fixture-scoped representation only; opaque refs are not dereferenced. |
| [Flora crosswalk doctrine](../../../docs/domains/flora/CROSSWALKS.md) | `CONFIRMED` doctrine / implementation claims remain scoped | Governed mappings, source-role anti-collapse, evidence, provenance, sensitivity, and fail-closed posture. | Flora-specific narrative is not shared-runtime proof. |
| [Drive: KFM Hourly Flora Domain Builder v1.0](https://docs.google.com/document/d/1SdZMLyyPbzywH4KUmEpuPsRic8_rFyQrIowns45vVfU/edit?usp=drivesdk) | read-only lineage | Taxonomy/occurrence separation and preservation of source-native names and historical identity. | Subordinate to repository evidence; not approval or implementation authority. |
| [Notion: KFM Hourly Flora Domain Builder v1.0](https://app.notion.com/p/3caa92021bf6815db884de68502fb21f) | unverified coordination context | Current domain ownership and non-collapse coordination. | Not implementation, review, policy, or release authority. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `CONFIRMED` adopted placement governance | Responsibility-root split and lifecycle discipline. | Placement governance does not make a taxonomy decision. |

GitHub is implementation authority. Drive provides read-only lineage, and Notion provides coordination context. Conflicts resolve to current repository evidence and accepted governance; unresolved source or taxonomy truth remains visible and fail-closed.

## Definition of done

- [x] Current directory inventory is verified.
- [x] The concrete object-level contract and paired schema are linked.
- [x] The bounded validator, six-test module, workflow, and receipts are linked and described without expanding their authority.
- [x] The absent standalone fixture root and the README workflow-trigger gap are explicit.
- [ ] Owners and review/release authorities are confirmed.
- [ ] Standalone fixtures are added and wired, or the schema metadata is deliberately revised through a dependency-complete change.
- [ ] An accepted shared taxonomy registry/resolver boundary and source-admission process are established.
- [ ] Policy gates for source role, rights, sensitivity, consequential reconciliation, and public release are linked and tested.
- [ ] Downstream consumers dereference the lineage packet under explicit compatibility and failure rules.
- [ ] Correction, supersession, and release behavior are exercised with repository-present fixtures.

## Acceptance and rollback

Accept this README change only if review confirms:

- the diff is documentation-only and confined to this file;
- every repository-present claim resolves at the exact base/head;
- the proposed profile and its non-authority boundary are preserved;
- the missing fixture root and workflow-trigger limitation remain visible; and
- independent review occurs through the repository's normal review route.

Before merge, rollback is closing the pull request and deleting its branch. After an authorized merge, rollback is a normal revert of this documentation commit. The pre-change target is blob `6c93a9cdd7f4fb0be997925674dc949e74ea1db7` on `main@7f0f034236ff39eb690733bcf869ada67015a7a0`.

---

`contracts/crosswalks/taxonomy/` defines taxonomy-crosswalk meaning. It is not a live authority, schema root, policy engine, validator package, fixture store, registry, resolver implementation, proof root, release surface, public API/UI, or permission to turn a taxon name into supported truth.

<p align="right"><a href="#top">Back to top</a></p>
