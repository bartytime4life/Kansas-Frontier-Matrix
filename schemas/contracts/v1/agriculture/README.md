<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-agriculture-readme
title: schemas/contracts/v1/agriculture/ — Agriculture Schema Compatibility Index
type: readme; directory-readme; schema-compatibility-index; non-authoritative-router
authority_class: compatibility-index
version: v1.1
status: draft; compatibility; transitional; index-only; repository-grounded
policy_label: public
owners:
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Agriculture domain steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
updated: 2026-07-20
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2b31ccbd9ba5b3fe6772ea1b0165eca45bdfebb0
  prior_blob: 716b3fd1e73feaeba678e6800606604e7d621d16
related:
  - ../../../README.md
  - ../README.md
  - ../domains/README.md
  - ../domains/agriculture/README.md
  - ../../../../contracts/domains/agriculture/README.md
  - ../../../../fixtures/domains/agriculture/README.md
  - ../../../../tests/domains/agriculture/README.md
  - ../../../../tools/validators/domains/agriculture/README.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
tags: [kfm, schemas, contracts, v1, agriculture, compatibility, transitional, index-only, json-schema, no-parallel-authority]
notes:
  - "This directory contains only README.md and .gitkeep at the recorded evidence snapshot."
  - "Agriculture machine-schema files currently live under schemas/contracts/v1/domains/agriculture/; that lane is doctrine-aligned but remains proposed because ADR-0001 is proposed."
  - "This README is a router and drift guard. It does not make this flat lane or the domain lane accepted schema authority."
[/KFM_META_BLOCK_V2] -->

# `schemas/contracts/v1/agriculture/` — Agriculture Schema Compatibility Index

`schemas/contracts/v1/agriculture/` is an index-only compatibility lane that routes maintainers to the Agriculture domain schema surface without creating a second schema authority.

**Audience:** schema, Agriculture-domain, contract, validation, governance, and documentation maintainers.

> [!IMPORTANT]
> Do not add machine schemas to this flat lane. The current Directory Rules place domain-specific machine shape under `schemas/contracts/v1/domains/<domain>/`, while [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is still `proposed`. Until that decision and any migration are closed, treat [`../domains/agriculture/`](../domains/agriculture/README.md) as the proposed domain lane and this directory as a compatibility pointer only.

[Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does NOT belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence ledger](#evidence-ledger) · [Open verification](#open-verification) · [Rollback](#rollback)

## Purpose

This directory preserves discoverability for the older flat Agriculture schema path while preventing it from evolving independently.

It exists to:

- point readers and legacy references toward the proposed Agriculture domain schema lane;
- record the flat-path versus domain-path relationship;
- expose material schema, contract, fixture, validator, and CI maturity gaps;
- support a future ADR-backed migration, deprecation, or alias decision; and
- prevent documentation from upgrading permissive schema scaffolds into implementation, policy, evidence, or release claims.

This README documents repository state. It is not a JSON Schema, semantic contract, schema registry, migration manifest, policy decision, validation report, receipt, proof, release record, or publication authority.

## Authority level

**Compatibility / transitional / index-only.** The `schemas/` root owns machine-checkable shape. This flat lane owns no schema family and must not become a parallel Agriculture schema home.

The placement basis is:

1. [Directory Rules](../../../../docs/architecture/directory-rules.md) assign machine shape to `schemas/` and apply the domain lane pattern `schemas/contracts/v1/domains/<domain>/` to Agriculture.
2. [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) proposes `schemas/contracts/v1/` as the machine-schema home and `schemas/contracts/v1/domains/<domain>/` for domain-specific schemas.
3. [`schemas/README.md`](../../../README.md) preserves the meaning/shape/policy/proof split and warns against parallel authority.
4. The current repository contains this flat directory as a README-and-`.gitkeep` compatibility lane and contains Agriculture schema files in [`../domains/agriculture/`](../domains/agriculture/README.md).

The target path is therefore **CONFIRMED present**, but its long-term disposition remains **NEEDS VERIFICATION**. The proposed domain lane is not upgraded to accepted authority by this README.

## Status

### Compatibility status

| Concern | Current state | Evidence posture |
|---|---|---|
| Flat directory | `README.md` plus `.gitkeep`; no machine schema files | **CONFIRMED** at `main@2b31ccbd9ba5b3fe6772ea1b0165eca45bdfebb0` |
| Lane class | Compatibility / transitional / index-only | **PROPOSED classification**, consistent with the prior README and Directory Rules anti-drift posture |
| Proposed domain lane | `schemas/contracts/v1/domains/agriculture/` exists | **CONFIRMED path / PROPOSED authority** |
| ADR status | ADR-0001 is `proposed`, not accepted | **CONFIRMED** from the ADR metadata and status block |
| Migration or deprecation decision | No accepted decision was verified for this flat lane | **NEEDS VERIFICATION** |
| Generated or mirrored status | No generator, synchronization command, or mirror notice was found for this README | **UNKNOWN** beyond the inspected paths; treat as manually maintained |
| Public or release authority | None | **CONFIRMED boundary** |

### Repository fit

```text
schemas/
└── contracts/
    └── v1/
        ├── agriculture/
        │   ├── .gitkeep
        │   └── README.md                    # this compatibility index
        └── domains/
            └── agriculture/
                ├── README.md                # proposed domain schema index
                ├── *.schema.json            # 19 direct schema scaffolds at the snapshot
                ├── hydrology-ext/README.md  # extension-placement question remains open
                └── receipts/README.md       # receipt-schema placement remains open
```

### Bounded domain-schema snapshot

The direct Agriculture domain lane contains 19 `*.schema.json` files at the recorded base commit. All declare JSON Schema Draft 2020-12, all have distinct `$id` values within that bounded set, all carry `x-kfm.status: PROPOSED`, and all permit unspecified properties.

| Shape group | Files | Observed structure | Interpretation |
|---|---|---|---|
| Empty-property scaffolds | `aggregation_receipt`, `agriculture_decision_envelope`, `agriculture_feature_dto`, `crop_observation` | No declared properties or required fields; `additionalProperties: true` | **PROPOSED scaffold**; not a meaningful payload contract |
| ID-only scaffolds | `catalog_matrix`, `correction_notice`, `decision_envelope`, `domain_feature_identity`, `domain_layer_descriptor`, `domain_observation`, `domain_validation_report`, `evidence_bundle`, `evidence_drawer_payload`, `layer_manifest`, `promotion_decision`, `release_manifest`, `rollback_card`, `run_receipt`, `source_state_hash` | Requires `id`; exposes only `id`, `spec_hash`, and `version`; `additionalProperties: true` | **PROPOSED minimal scaffold**; not field-complete domain validation |

The bounded inventory also exposes these conflicts and gaps:

- `$id` uses two namespaces: four `kfm://schemas/...` identifiers and fifteen `https://schemas.kfm.local/...` identifiers. Namespace authority is **NEEDS VERIFICATION**.
- Four schema-declared contract paths exist exactly. Fifteen exact targets are absent; one absent target, `aggregation_receipt.md`, has a hyphenated semantic-contract counterpart at [`contracts/domains/agriculture/aggregation-receipt.md`](../../../../contracts/domains/agriculture/aggregation-receipt.md).
- None of the fifteen schema-declared family fixture directories exists. The Agriculture fixture root contains documentation and placeholders, not those declared fixture families.
- Two schema-declared validator paths exist, but both are four-line `NotImplementedError` placeholders. Two additional Agriculture validator files in the same lane are also placeholders; no field-level Agriculture validator was established.
- [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml) parses all schema JSON, checks Draft 2020-12 meta-schema validity, and requires unique canonical-v1 `$id` values. Its configured aggregate fixture validators cover six shared families, not the Agriculture schemas listed here.
- [`domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) reports explicit readiness holds. A green held job is not Agriculture schema, evidence, policy, release, or runtime proof.
- The proposed domain-lane README currently describes only one known schema, while the pinned tree contains 19. Treat that README inventory as stale until it is regenerated and reviewed.

No item above establishes source truth, semantic completeness, EvidenceBundle closure, policy approval, rights or sensitivity clearance, runtime use, release readiness, or publication.

## What belongs here

- `README.md` as the compatibility router and drift guard.
- `.gitkeep` while the compatibility directory must remain addressable.
- A short, reviewed migration, deprecation, or mirror notice when an accepted decision requires one.
- Stable links to the proposed domain schema lane, semantic contracts, fixtures, validators, tests, workflows, ADRs, and drift records.
- Evidence-bounded status notes that clearly distinguish path presence, schema shape, validation coverage, and release state.

Any additional file must keep this lane non-authoritative and must identify its canonical source, synchronization rule, owner, sunset or review trigger, and rollback path.

## What does NOT belong here

- `*.schema.json`, JSON-LD contexts, or other machine-shape definitions.
- Hand-maintained or generated copies of schemas from `../domains/agriculture/`.
- Semantic contract prose or object-family definitions.
- Policy rules, rights decisions, sensitivity decisions, redaction rules, or release decisions.
- Valid, invalid, golden, live-source, or production payloads.
- Validator or runtime implementation.
- Schema registry records, source registry records, EvidenceBundles, proofs, receipts, catalogs, manifests, or lifecycle data.
- Public API, map, UI, Focus Mode, export, search, graph, or model-runtime behavior.
- Claims that schema presence, JSON validity, a green workflow, a commit, or a pull request proves correctness or publication.

## Inputs

Changes to this index must be grounded in the smallest sufficient evidence set:

- current [Directory Rules](../../../../docs/architecture/directory-rules.md) and any accepted amending ADR;
- [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) and its current lifecycle state;
- the exact flat-lane and proposed domain-lane tree at a pinned commit;
- machine schema metadata, including `$schema`, `$id`, `required`, `properties`, `additionalProperties`, and `x-kfm` pointers;
- paired semantic contracts under [`contracts/domains/agriculture/`](../../../../contracts/domains/agriculture/README.md);
- fixtures, validators, tests, workflows, schema-registry records, migrations, and drift entries that actually exist; and
- policy, evidence, review, release, correction, and rollback records only when a claim depends on them.

Lineage documents and proposed paths may guide review, but they do not prove implementation. Memory and README prose do not upgrade a schema or integration claim to **CONFIRMED**.

## Outputs

This lane emits no runtime or lifecycle object.

Its only supported outputs are:

- a human-readable routing index;
- a compatibility classification;
- a bounded snapshot of observed drift and maturity;
- review and validation instructions; and
- pointers for a future ADR-backed migration or deprecation.

It does not emit schemas, generated mirrors, registry entries, validation reports, policy decisions, evidence, receipts, proofs, catalogs, release records, published artifacts, or public responses.

## Validation

### Documentation checks

For this README:

- verify one H1, consecutive heading levels, balanced fences, readable tables, and a final newline;
- verify every repository-relative link against the resulting branch;
- confirm the KFM Meta Block markers are balanced and the preserved `doc_id` remains unique;
- confirm the flat lane still contains no machine schema files;
- compare the pinned domain-schema inventory and maturity claims with the actual JSON files;
- scan for credentials, restricted payloads, private identities, or exact sensitive locations; and
- inspect the complete base-to-head diff for unrelated changes.

### Repository checks and their limits

| Check | What it establishes | What it does not establish |
|---|---|---|
| JSON parsing of `schemas/contracts/v1/domains/agriculture/*.schema.json` | The inspected files are syntactically valid JSON | Semantic completeness or admissibility |
| Draft 2020-12 meta-schema check | The inspected schema documents are legal Draft 2020-12 schemas | Useful Agriculture constraints, fixtures, or runtime enforcement |
| Unique `$id` check in [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml) | No duplicate `$id` exists in the workflow's canonical-v1 scan when the job passes | Accepted namespace, stable identity, or registry activation |
| `make schemas` | The configured aggregate validator runner completes | Agriculture-specific schema validation; the configured families are shared source/evidence/runtime families |
| `python -m pytest -q tests/schemas tests/contracts` | The repository-owned schema/contract suite passes within its collected scope | Agriculture-domain test coverage unless those tests are collected there |
| [`domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) | Documented Agriculture boundaries and explicit readiness holds remain consistent | Executable Agriculture validation, proof, release readiness, or publication |

Do not promote this lane, remove it, add schemas to it, or call the domain lane active solely because generic schema validation passes.

## Review burden

[`.github/CODEOWNERS`](../../../../.github/CODEOWNERS) routes all `/schemas/` changes to `@bartytime4life`. That is review routing, not proof that independent schema, Agriculture, contract, validation, policy, or release review occurred.

Before approving a change here, reviewers must confirm:

- [ ] the flat lane remains compatibility/index-only;
- [ ] no schema definition or divergent mirror was added;
- [ ] the Directory Rules and ADR-0001 status are represented accurately;
- [ ] schema counts, `$id` namespaces, contract pointers, fixture roots, validator paths, and CI claims match the pinned tree;
- [ ] unresolved schema-home, receipt-family, extension-lane, and naming conflicts remain visible;
- [ ] schema validity is not presented as evidence, policy permission, release approval, or publication;
- [ ] public clients remain downstream of governed interfaces and released artifacts;
- [ ] the generated-work receipt is valid and remains pending human review until an authorized reviewer acts; and
- [ ] rollback restores the prior blob without rewriting shared history.

A migration, deprecation, schema-home change, or new parallel definition requires the appropriate schema, Agriculture-domain, contract, validation, migration, and governance review in addition to GitHub code-owner routing.

## Related folders

| Path | Relationship | Current posture |
|---|---|---|
| [`../../../README.md`](../../../README.md) | Schema responsibility root | **CONFIRMED root boundary** |
| [`../README.md`](../README.md) | v1 schema-family index | **CONFIRMED / mixed maturity** |
| [`../domains/README.md`](../domains/README.md) | Parent domain-schema index | **CONFIRMED file / proposed lane model** |
| [`../domains/agriculture/`](../domains/agriculture/README.md) | Agriculture machine-shape lane and direct schema files | **CONFIRMED path / PROPOSED authority / stale README inventory** |
| [`../domains/agriculture/hydrology-ext/`](../domains/agriculture/hydrology-ext/README.md) | Agriculture-Hydrology extension index | **NEEDS VERIFICATION / cross-domain placement-sensitive** |
| [`../domains/agriculture/receipts/`](../domains/agriculture/receipts/README.md) | Agriculture receipt-schema index | **NEEDS VERIFICATION / receipt-family placement-sensitive** |
| [`../../../../contracts/domains/agriculture/`](../../../../contracts/domains/agriculture/README.md) | Agriculture semantic contracts | **CONFIRMED path / partial pairing** |
| [`../../../../fixtures/domains/agriculture/`](../../../../fixtures/domains/agriculture/README.md) | Agriculture fixture index | **CONFIRMED documentation / declared schema-family fixtures absent** |
| [`../../../../tests/domains/agriculture/`](../../../../tests/domains/agriculture/README.md) | Agriculture enforceability boundary | **CONFIRMED documentation / executable coverage unestablished** |
| [`../../../../tools/validators/domains/agriculture/`](../../../../tools/validators/domains/agriculture/README.md) | Agriculture edge-validator lane | **CONFIRMED files / placeholder implementations** |
| [`../../../../policy/domains/agriculture/`](../../../../policy/domains/agriculture/README.md) | Agriculture policy boundary | **Separate authority; not changed here** |
| [`../../../../release/agriculture/`](../../../../release/agriculture/README.md) | Agriculture release orientation | **Separate authority; blocked/held posture** |

## ADRs

### ADR-0001 — schema home

[ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) proposes:

- `schemas/contracts/v1/` for machine-checkable schemas;
- `schemas/contracts/v1/domains/<domain>/` for domain-specific schemas;
- `contracts/` for semantic meaning; and
- no divergent machine definitions across `schemas/` and `contracts/`.

Its current status is `proposed`. This README follows its anti-drift direction without claiming the decision is accepted.

### Unresolved lane decision

No accepted ADR or migration record was verified that classifies `schemas/contracts/v1/agriculture/` as a permanent alias, generated mirror, deprecated path, or removable directory. Until that decision exists:

1. keep this lane index-only;
2. place no schema files here;
3. do not silently redirect or delete the path;
4. record any migration mapping and downstream consumer impact; and
5. preserve rollback to the prior path state.

The inspected [`DRIFT_REGISTER.md`](../../../../docs/registers/DRIFT_REGISTER.md) does not yet contain an Agriculture flat-versus-domain schema-lane entry. Add one when a migration or deprecation decision enters scope; this documentation-only revision does not create that decision.

## Last reviewed

| Field | Value |
|---|---|
| Review date | 2026-07-20 |
| Repository snapshot | `bartytime4life/Kansas-Frontier-Matrix` `main@2b31ccbd9ba5b3fe6772ea1b0165eca45bdfebb0` |
| Flat-lane prior blob | `716b3fd1e73feaeba678e6800606604e7d621d16` |
| Review state | Draft compatibility-index revision; human review pending |
| Next review trigger | ADR-0001 status change; flat-lane migration/deprecation decision; Agriculture schema inventory change; `$id` namespace decision; contract/fixture/validator/test activation; child-lane placement decision; or schema workflow change |

## Evidence ledger

| Evidence | Observation supported | Truth status | Does not prove |
|---|---|---|---|
| `schemas/contracts/v1/agriculture/` at the pinned commit | Directory contains `README.md` and `.gitkeep`, with no schema definitions | **CONFIRMED** | Long-term alias policy |
| [`Directory Rules`](../../../../docs/architecture/directory-rules.md) | `schemas/` owns machine shape; domains belong inside responsibility roots | **CONFIRMED doctrine / specific placement subject to stated limits** | Accepted ADR-0001 or implementation completeness |
| [ADR-0001](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed schema-home and domain-lane decision | **CONFIRMED text / PROPOSED decision** | Accepted governance state |
| [`../domains/agriculture/`](../domains/agriculture/README.md) plus direct schema JSON | Nineteen direct, permissive, `PROPOSED` schema scaffolds and two child indexes exist | **CONFIRMED bounded inventory** | Semantic completeness, fixture closure, validator enforcement, or runtime use |
| [`contracts/domains/agriculture/`](../../../../contracts/domains/agriculture/README.md) | Four exact schema-declared contract targets and one hyphenated counterpart exist | **CONFIRMED bounded inventory** | Complete contract pairing |
| [`fixtures/domains/agriculture/`](../../../../fixtures/domains/agriculture/README.md) | Agriculture fixture documentation exists; schema-declared family roots are absent | **CONFIRMED bounded inventory** | Complete recursive fixture or test coverage outside inspected scope |
| Agriculture validator scripts and READMEs | Four per-domain Agriculture validator filenames are `NotImplementedError` placeholders | **CONFIRMED** | Future validator design or activation |
| [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml) | Generic schema JSON, meta-schema, identity, configured-fixture, and shared schema/contract checks | **CONFIRMED workflow definition** | A passing run for this branch or Agriculture-specific conformance |
| [`domain-agriculture.yml`](../../../../.github/workflows/domain-agriculture.yml) | Read-only readiness checks and explicit holds | **CONFIRMED workflow definition** | Agriculture validation, proof, release, or publication |

## Open verification

- [ ] Decide whether this flat lane is a permanent compatibility alias, temporary transition, deprecated path, or removal candidate.
- [ ] Accept, revise, supersede, or reject ADR-0001 through authorized review.
- [ ] Add or link the Agriculture flat-versus-domain lane decision in the drift and migration records.
- [ ] Reconcile the proposed domain-lane README with the 19-file schema inventory.
- [ ] Resolve the two `$id` namespace patterns and register accepted identities.
- [ ] Resolve `aggregation-receipt.md` versus `aggregation_receipt.md` without silently changing object identity.
- [ ] Decide whether receipt schemas belong in the Agriculture domain root, its `receipts/` child, or the shared receipt family.
- [ ] Decide whether `hydrology-ext/` is an Agriculture-owned extension or a cross-domain schema concern.
- [ ] Complete semantic contracts or explicitly profile shared contracts for every Agriculture schema.
- [ ] Add deterministic valid and invalid fixtures for accepted Agriculture schema families.
- [ ] Replace placeholder validators with reviewed implementations and wire targeted tests.
- [ ] Confirm schema registry, policy, evidence, release, correction, and rollback integration before promoting any schema beyond scaffold status.

## Rollback

Before merge, rollback means closing or abandoning the draft pull request; deleting the review branch is a separate cleanup action.

After merge, create a transparent revert of the implementation or merge commit, restoring prior blob `716b3fd1e73feaeba678e6800606604e7d621d16`, then re-run the same Markdown, link, schema-structure, and remote-diff checks. Do not force-push or rewrite shared history.

## Changelog

### v1.1 — 2026-07-20

- Reclassified the flat path as a bounded compatibility/transitional index rather than a candidate schema home.
- Added a pinned repository evidence snapshot and current two-file flat-lane inventory.
- Recorded the 19-file proposed domain-schema inventory, permissive scaffold shapes, split `$id` namespaces, partial contract pairing, absent declared fixture roots, placeholder validators, and CI limits.
- Added the Directory Rules README contract sections, review burden, evidence ledger, open verification, and transparent rollback.
- Preserved the existing `doc_id`, Agriculture routing purpose, no-parallel-authority rule, compatibility boundary, review checklist intent, and unresolved migration posture.

---

**Compatibility rule:** keep this lane pointer-only until an accepted decision and verified migration establish a different role.
