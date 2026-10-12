<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/domains/readme
name: Domain Registry README
path: data/registry/domains/README.md
type: data-registry-domains-parent-readme
version: v0.1.0
status: draft
owners:
  - "NEEDS VERIFICATION: registry steward"
  - "NEEDS VERIFICATION: domain stewards"
  - "NEEDS VERIFICATION: contract, schema, policy, validation, and release stewards"
created: 2026-07-29
updated: 2026-07-29
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: domain-state-records
path_posture: canonical-subtype-first-parent-confirmed; boundary-readme-only; no-child-lanes-or-records; implementation-maturity-unverified
sensitivity_posture: registry-internal; no-public-path; rights-and-sensitivity-fail-closed; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../datasets/README.md
  - ../layers/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../crosswalks/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/domains/README.md
  - ../../../schemas/contracts/v1/domains/README.md
  - ../../../policy/domains/README.md
  - ../../../tests/domains/README.md
  - ../../../fixtures/domains/README.md
  - ../../../release/README.md
notes:
  - "Accepted Directory Rules v2 explicitly place domain-state registry records under data/registry/domains/."
  - "This README establishes only the parent boundary required by that placement; it does not create domain records, child lanes, a writer, or implementation maturity."
  - "No canonical domain-state object contract, schema, validator, fixture, test, producer, consumer, runtime resolver, owner assignment, retention rule, or release integration was verified for this lane in the completion pass."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Registry

> Canonical subtype-first parent for governed domain-state registry records. This boundary does not itself create a domain identity, registry record, writer, implementation, release decision, or public claim.

| Boundary field | Current value |
|---|---|
| Status | Boundary README only; record shape and implementation **NEEDS VERIFICATION** |
| Inherited parent | [`data/registry/`](../README.md) |
| Local scope ID | `data/registry/domains/` |
| Local owner | **NEEDS VERIFICATION** |
| Public access | **DENY** |

**Truth posture:** cite or abstain

> [!IMPORTANT]
> Accepted [Directory Rules v2](../../../docs/doctrine/directory-rules.md) places domain-state registry records under `data/registry/domains/`. [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) establishes that document as the writable Directory Rules authority. Canonical placement is **CONFIRMED**; emitted records, writers, consumers, and runtime behavior are not.

> [!CAUTION]
> This README authorizes no writer. Domain-first paths such as `data/registry/<domain>/` may not become independent registry writers by implication. Unknown identity, evidence, rights, sensitivity, policy, review, release, correction, or rollback state must fail closed.

## Purpose and inherited boundary

`data/registry/domains/` inherits the registry-control boundary from [`data/registry/`](../README.md). Its bounded responsibility is domain-state registry records: compact governance handles that may identify a domain and point to its applicable semantic, machine, evidence, policy, review, release, correction, and rollback authorities.

This lane is not domain truth. A path, README, registry row, valid instance, passing check, pull request, or merge cannot make a claim true, evidence-complete, rights-cleared, policy-admitted, reviewed, released, or published.

## Status and current directory map

The current tracked boundary has no domain child lane and no registry payload:

```text
data/registry/domains/
└── README.md    # this boundary contract; not a registry record
```

The tree is current and shows direct children only, as required by `DIR-README-003` and `DIR-README-004`. It must not be expanded for visual symmetry. A domain child belongs here only when repository evidence establishes at least one useful governed record and its ownership, shape, writer, validation, and lifecycle controls.

| Question | Current answer |
|---|---|
| Canonical parent placement | **CONFIRMED** by Directory Rules §12.3 |
| README profile | `BOUNDARY_COMPACT` under Directory Rules §16 |
| Domain child lanes | None created or verified in this completion pass |
| Domain-state records | None created or verified in this completion pass |
| Canonical object contract and schema | **NEEDS VERIFICATION** |
| Producer, permitted writer, and runtime resolver | **NEEDS VERIFICATION**; none authorized here |
| Concrete consumers and public API behavior | **NEEDS VERIFICATION** |
| Owner, reviewer, retention, and rollback assignments | **NEEDS VERIFICATION** |
| Publication effect | None |

## Belongs here

Only the following material may belong after its governing contract and controls are verified:

- compact domain-state registry records with stable, deterministic domain identity;
- registry-local indexes over those records;
- pointers to domain contracts, schemas, source and dataset identities, evidence, policy decisions, review state, release state, corrections, supersession, and rollback targets;
- explicit unresolved, held, denied, deprecated, corrected, withdrawn, or superseded state when the governing contract supports it;
- boundary documentation that does not claim implementation maturity.

This list defines responsibility, not present implementation. No record fields, filenames, child domains, or state vocabulary are established by this README.

## Prohibited here

| Material | Owning surface |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, catalog, triplet, or published payloads | Applicable `data/` lifecycle lane |
| Source, dataset, layer, rights, sensitivity, or crosswalk registry records | Sibling registry families under `data/registry/` |
| Domain meaning and invariants | [`contracts/domains/`](../../../contracts/domains/README.md) or another accepted contract home |
| Machine shape | [`schemas/contracts/v1/domains/`](../../../schemas/contracts/v1/domains/README.md) or another accepted schema home |
| Admission, access, sensitivity, rights, or release policy | [`policy/domains/`](../../../policy/domains/README.md) and applicable cross-cutting policy roots |
| Fixtures, executable checks, or implementation code | [`fixtures/domains/`](../../../fixtures/domains/README.md), [`tests/domains/`](../../../tests/domains/README.md), and verified implementation roots |
| Receipts, proofs, catalogs, or release decisions | `data/receipts/`, `data/proofs/`, `data/catalog/`, and [`release/`](../../../release/README.md) |
| Secrets, restricted source bytes, harmful-precision locations, or private-person data | Approved restricted storage and access controls; never this public-repository lane |
| Public API, UI, map, search, graph, export, or generated-answer payloads | Governed interfaces and released public-safe artifacts only |

## Inputs and outputs

Potential inputs are references, not copied authorities: canonical domain identity and contracts, verified registry identities, EvidenceRefs that resolve to EvidenceBundles where claims depend on evidence, rights and sensitivity posture, policy outcomes, review state, release state, and correction or rollback references.

Potential outputs are bounded domain-state registry records and registry-local indexes for governed internal consumers. No input interface, output object, producer, consumer, API route, resolver, or runtime integration was verified in this completion pass. Public clients must not read this lane directly.

## Exposure, mutation, and retention

- **Exposure:** internal governance only; direct public access is denied.
- **Mutation:** no writer is authorized by this README. Future writes require a verified contract, schema, owner, permitted writer, validation path, evidence and policy controls, and auditable change history.
- **Topology:** subtype-first `data/registry/domains/` is canonical. A domain-first compatibility lane must remain read-only unless an accepted migration decision says otherwise.
- **Retention:** no retention schedule was verified. Do not silently overwrite or delete identity, correction, denial, withdrawal, or supersession history.
- **Correction and rollback:** future records must preserve correction and rollback targets appropriate to their significance. This README is not a rollback record.

## Validation

The boundary itself is valid only while all of these remain true:

1. The path remains under the canonical `data/registry/` responsibility root.
2. The README shows only verified direct children and does not imply unverified domain lanes or payloads.
3. No domain-first compatibility path becomes an independent writer.
4. No registry record substitutes for a contract, schema, policy decision, EvidenceBundle, review, release, correction, or rollback authority.
5. Public clients consume governed interfaces and released public-safe products, not this registry lane.
6. Unknown identity, evidence, rights, sensitivity, policy, review, release, or exposure state produces abstention, hold, quarantine, redaction, generalization, staged access, or denial rather than optimistic publication.

Before any record or child lane is added, verify at minimum: deterministic identity; canonical contract and schema authority; owner and permitted writer; producer and consumer; source-role and temporal handling; EvidenceRef resolution; rights and sensitivity posture; policy outcome; correction and rollback behavior; deterministic fixtures and no-network tests; and release/publication separation.

## Related authority surfaces

| Responsibility | Surface |
|---|---|
| Registry parent and inherited operating contract | [`data/registry/`](../README.md) |
| Source, dataset, layer, rights, sensitivity, and crosswalk state | [`sources/`](../sources/README.md), [`datasets/`](../datasets/README.md), [`layers/`](../layers/README.md), [`rights/`](../rights/README.md), [`sensitivity/`](../sensitivity/README.md), and [`crosswalks/`](../crosswalks/README.md) |
| Controlling placement doctrine | [Directory Rules v2](../../../docs/doctrine/directory-rules.md) |
| Adoption decision | [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Semantic meaning | [`contracts/domains/`](../../../contracts/domains/README.md) |
| Machine shape | [`schemas/contracts/v1/domains/`](../../../schemas/contracts/v1/domains/README.md) |
| Policy | [`policy/domains/`](../../../policy/domains/README.md) and applicable cross-cutting policy roots |
| Enforceability evidence | [`fixtures/domains/`](../../../fixtures/domains/README.md) and [`tests/domains/`](../../../tests/domains/README.md) |
| Promotion and publication decisions | [`release/`](../../../release/README.md) |

## Open verification items

- Identify and ratify the registry and domain stewards for this family.
- Resolve the canonical domain-state semantic contract, machine schema, finite states, and stable identity rules.
- Inventory intended producers, consumers, compatibility readers, and any existing out-of-lane domain-state records before authorizing a writer.
- Define deterministic validation, fixtures, tests, receipts, evidence resolution, policy checks, correction, retention, supersession, and rollback behavior.
- Verify whether any domain has sufficient grounded records and controls to justify a child lane; do not scaffold empty symmetry.
- Verify governed API or release integration before making any availability claim.

## Rollback

This change is documentation-only and creates no registry payload, child lane, writer, consumer, or runtime binding. Before merge, close the draft pull request to abandon it. After merge, use a normal revert commit to remove this README and its otherwise empty directory, restoring the prior missing-boundary state without data migration.
