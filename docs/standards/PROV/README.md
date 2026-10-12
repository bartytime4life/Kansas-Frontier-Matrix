<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/prov-family-readme
title: docs/standards/PROV/ — W3C PROV Family Boundary
type: readme/boundary-readme
version: v1.0.0
status: active; repository-grounded; reconciliation-boundary; non-authoritative
owners:
  - "@bartytime4life — verified CODEOWNERS route; accountable provenance stewardship and independent review remain NEEDS VERIFICATION"
created: 2026-05-24
updated: 2026-08-14
policy_label: public
owning_root: docs/
scope_id: w3c-prov-family
responsibility: "Route KFM's W3C PROV guidance, disclose overlapping provenance documents and implementation boundaries, and prevent this nested lane from becoming parallel semantic, schema, policy, catalog, receipt, release, or publication authority."
truth_posture: "CONFIRMED current path, history, duplicate DUO bytes, parent standards inventory, related provenance documents, accepted Directory Rules authority, CODEOWNERS route, selected repository boundaries, and dated W3C PROV references / PROPOSED document-role convergence and future application-profile decisions / UNKNOWN complete producer, consumer, runtime, release, and public-conformance behavior / NEEDS VERIFICATION accountable stewardship, canonical semantic-profile identity, PAV binding, machine profile, validator coverage, migration, and supersession"
evidence_snapshot: "main@0abdce42ea0a41f88e86b7d97df0ebd79961e37b; target and DUO_PROFILE prior blob a4283dac33ec9f2c182a8be0cb0d23a3e1ba13e0; standards README blob a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b; PROV.md blob e69e4e9ee9a9771d0ad33aecfbb7ce91bd60867f; PROV-O.md blob 919452dbd8abe1ff1079a7235d43b211de6fae54; PROVENANCE.md blob cddd69eeb49ccc65481137e2d65dcafe1abe2ebf"
related:
  - docs/standards/README.md
  - docs/standards/PROV.md
  - docs/standards/PROV-O.md
  - docs/standards/PROVENANCE.md
  - docs/standards/OPENLINEAGE_FACETS.md
  - docs/standards/EVIDENCE_BUNDLE.md
  - docs/standards/RUN_RECEIPT.md
  - docs/standards/SIGNING.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - data/catalog/prov/README.md
  - data/prov/README.md
  - contracts/README.md
  - schemas/README.md
  - policy/README.md
  - release/README.md
tags: [kfm, standards, provenance, w3c-prov, prov-o, boundary, reconciliation, cite-or-abstain]
notes:
  - "Same-path correction: the prior body was byte-identical to docs/standards/DUO_PROFILE.md and described GA4GH DUO rather than W3C PROV."
  - "The legitimate DUO profile remains at docs/standards/DUO_PROFILE.md."
  - "This README does not select a canonical winner between PROV.md and PROV-O.md or collapse semantic and supply-chain provenance."
  - "No contract, schema, policy, validator, fixture, data, receipt, proof, release, runtime, source, deployment, or publication state changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/standards/PROV/` — W3C PROV Family Boundary

> Route readers through KFM's provenance guidance while keeping W3C semantic provenance, operational lineage, process receipts, supply-chain attestations, catalog projections, evidence, policy, and release authority distinct.

[![Status: repository-grounded](https://img.shields.io/badge/status-repository--grounded-d4a72c?style=flat-square)](#status-and-evidence-boundary)
[![Authority: navigation only](https://img.shields.io/badge/authority-navigation%20only-0969da?style=flat-square)](#authority-and-negative-authority)
[![Convergence: held](https://img.shields.io/badge/profile%20convergence-HELD-b42318?style=flat-square)](#open-verification-register)

> [!IMPORTANT]
> This is a **human-readable family boundary**, not the canonical KFM W3C PROV application profile. A document, valid graph, receipt, signature, passing check, pull request, or merge does not establish evidence closure, policy permission, review, release, or KFM publication.

> [!WARNING]
> Provenance can expose people, private systems, restricted sources, internal paths, exact locations, embargo state, timestamps, dependency relationships, signed URLs, or security-sensitive build details. Public-bound provenance must be minimum-necessary, policy-safe, reviewed, and release-approved.

**Quick navigation:** [Purpose](#purpose-and-inherited-parent) · [Authority](#authority-and-negative-authority) · [Status](#status-and-evidence-boundary) · [Upstream](#w3c-prov-upstream) · [Map](#repository-provenance-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Inputs/outputs](#inputs-and-outputs) · [Exposure](#exposure-mutation-and-retention) · [Validation](#validation-and-review) · [Convergence](#convergence-protocol) · [Open items](#open-verification-register) · [Rollback](#correction-rollback-and-history)

## Purpose and inherited parent

This lane inherits the [`docs/standards/` boundary](../README.md) and accepted Directory Rules authority through [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md).

Its responsibility is to:

- explain the W3C PROV family at a dated evidence point;
- route readers to existing KFM provenance surfaces;
- preserve the unresolved overlap between semantic-provenance documents;
- distinguish semantic claim provenance from operational and supply-chain provenance; and
- prevent a nested documentation lane from becoming parallel contract, schema, policy, catalog, receipt, release, or public-serving authority.

Directory Rules assign an object-family boundary the `BOUNDARY_COMPACT` README profile. This same-path correction creates no root, path migration, profile adoption, or authority transition.

## Authority and negative authority

| Question | Owning authority | This README may do |
|---|---|---|
| Where standards guidance belongs | Directory Rules and [`docs/standards/`](../README.md) | Explain placement and drift |
| What W3C PROV means | Authoritative W3C specifications | Link and summarize; never redefine |
| What KFM provenance objects mean | [`contracts/`](../../../contracts/README.md) | Route to semantic authority |
| What machine shape is valid | [`schemas/`](../../../schemas/README.md) | Route to schemas; never substitute prose |
| What is allowed, withheld, or public | [`policy/`](../../../policy/README.md) and authorized review | Explain posture; never decide |
| Where catalog-stage PROV records belong | [`data/catalog/prov/`](../../../data/catalog/prov/README.md) | Route; never store payloads here |
| What process or build occurred | [`RUN_RECEIPT.md`](../RUN_RECEIPT.md), [`SIGNING.md`](../SIGNING.md), receipts and attestations | Distinguish process evidence from claim provenance |
| Whether STAC/DCAT/PROV agree | Current contracts, schemas, validators, evidence, and accepted decisions | Report bounded status; [`ADR-0022`](../../adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) remains proposed |
| Whether an artifact may release | [`release/`](../../../release/README.md), evidence, policy, review, correction, and rollback | Explain prerequisites; never approve |
| Whether KFM conforms | Exact producers, consumers, profiles, fixtures, validators, interoperability evidence, and reviewed release scope | Cite the verified boundary or abstain |

A provenance edge explains lineage; it does not prove the underlying claim. `prov:wasGeneratedBy`, a `RunReceipt`, and a signature answer different questions and do not replace `EvidenceRef → EvidenceBundle`, source role, rights, sensitivity, policy, review, release, correction, or rollback.

## Status and evidence boundary

The following is pinned to `main@0abdce42ea0a41f88e86b7d97df0ebd79961e37b`.

| Surface | CONFIRMED observation | Bounded conclusion |
|---|---|---|
| This path | Created empty on 2026-05-24, updated on 2026-05-25 | The directory exists, but history alone does not establish its intended role |
| Prior body | Blob `a4283dac33ec9f2c182a8be0cb0d23a3e1ba13e0` is byte-identical to [`DUO_PROFILE.md`](../DUO_PROFILE.md) and declares GA4GH DUO identity and scope | Path/content mismatch; legitimate DUO content remains at its proper tracked path |
| Parent index | [`docs/standards/README.md`](../README.md) records four provenance surfaces and the PROV/DUO byte collision | Reconciliation is known work, not silently resolved here |
| Semantic guidance | [`PROV.md`](../PROV.md) and [`PROV-O.md`](../PROV-O.md) overlap materially | Canonical semantic-profile identity is **CONFLICTED / NEEDS VERIFICATION** |
| Supply-chain guidance | [`PROVENANCE.md`](../PROVENANCE.md) covers SLSA, in-toto, DSSE, cosign/Sigstore, and SPDX | Complementary build provenance; not a synonym for semantic PROV |
| Catalog and compatibility | [`data/catalog/prov/`](../../../data/catalog/prov/README.md) is the documented catalog-stage lane; [`data/prov/`](../../../data/prov/README.md) identifies itself as compatibility/routing | Neither path proves released PROV conformance |
| Review route | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) routes default review to `@bartytime4life` | Routing is not stewardship, independent review, policy, or release approval |
| Machine realization | No canonical profile, context, validator suite, producer/consumer matrix, or released PROV catalog was established by this documentation review | Implementation and interoperability remain **UNKNOWN** |

```text
docs/standards/PROV/
└── README.md    # this boundary and reconciliation guide
```

## W3C PROV upstream

Checked against official W3C material on 2026-08-14:

- namespace: `http://www.w3.org/ns/prov#`; suggested prefix: `prov`;
- PROV-DM: data model;
- PROV-O: OWL2 ontology;
- PROV-N: compact notation;
- PROV-CONSTRAINTS: constraints, inferences, and validity considerations; and
- PROV errata: correction/currentness surface.

These upstream facts do not prove KFM adoption, profile completeness, JSON-LD behavior, validator coverage, or interoperability.

## Repository provenance map

| Surface | Role | Boundary |
|---|---|---|
| [`PROV/README.md`](./README.md) | Family boundary | Navigation only |
| [`PROV.md`](../PROV.md) | Broad PROV-O/PAV guidance | Draft; overlaps `PROV-O.md` |
| [`PROV-O.md`](../PROV-O.md) | Detailed PROV-O profile guidance | Draft; overlaps `PROV.md` |
| [`PROVENANCE.md`](../PROVENANCE.md) | Supply-chain/build provenance | Separate concern |
| [`OPENLINEAGE_FACETS.md`](../OPENLINEAGE_FACETS.md) | Operational-lineage guidance | Job/event lineage is not automatically claim provenance |
| [`RUN_RECEIPT.md`](../RUN_RECEIPT.md) | Process-receipt profile | Process memory, not claim truth |
| [`EVIDENCE_BUNDLE.md`](../EVIDENCE_BUNDLE.md) | Evidence-bundle profile | Evidence and provenance are linked but distinct |
| [`SIGNING.md`](../SIGNING.md) | Signature/verification guidance | Integrity/authenticity, not semantic truth |
| [`STAC.md`](../STAC.md), [`DCAT.md`](../DCAT.md) | Catalog interoperability | Agreement requires governed closure |
| [`data/catalog/prov/`](../../../data/catalog/prov/README.md) | Catalog-stage projections | Candidate carrier; release-gated |
| [`data/prov/`](../../../data/prov/README.md) | Compatibility/routing | No new trust-bearing writes |

### Responsibility split

| Concern | Question answered | Carrier |
|---|---|---|
| Source provenance | Where did source material originate, under what role, rights, time, and retrieval state? | SourceDescriptor, intake/retrieval receipt, evidence references |
| Semantic provenance | Which entity/activity/agent relations explain a claim or derived entity? | W3C PROV profile and EvidenceBundle/catalog projection |
| Authoring/versioning | Who authored or curated which version? | Reviewed PAV or equivalent mapping |
| Operational lineage | Which job or event consumed and emitted operational resources? | OpenLineage/runtime events and receipts |
| Process receipt | What ran, with which inputs, tools, hashes, outcomes, and failures? | RunReceipt and specialized receipts |
| Supply-chain provenance | Who built an artifact, from which materials, under which attestation? | SLSA/in-toto/DSSE/cosign-style attestations |
| Catalog provenance | Which lineage projection supports discovery and catalog closure? | `data/catalog/prov/` after governed profile and validation |
| Release/correction lineage | Which release, correction, withdrawal, or rollback governs use? | Release and correction object families |
| UI/AI explanation | What trace can a user inspect for this released claim? | Governed API resolving evidence and release metadata |

## What belongs here

- This direct-child inventory and boundary.
- A reviewed family-level source ledger or no-loss comparison.
- Bounded migration, redirect, tombstone, or deprecation guidance after authority exists.
- Family-level verification and correction notes that remain documentation only.

A future child requires a distinct responsibility, not merely a related filename.

## What does not belong here

| Prohibited content | Owning surface |
|---|---|
| A third independently editable PROV application profile | Reconcile `PROV.md` and `PROV-O.md` |
| Schemas, contexts, SHACL/OWL resources, or namespace registries | [`schemas/`](../../../schemas/README.md), registry, package, or governed data lane |
| Semantic contracts | [`contracts/`](../../../contracts/README.md) |
| Policy, redaction, access, or public-minimization rules | [`policy/`](../../../policy/README.md) |
| Emitters, adapters, validators, scripts, tests, or fixtures | Owning implementation, `tools/`, `tests/`, or `fixtures/` root |
| PROV catalog payloads | [`data/catalog/prov/`](../../../data/catalog/prov/README.md) |
| New trust-bearing payloads in compatibility | Deny writes to [`data/prov/`](../../../data/prov/README.md) absent a governed migration |
| Receipts, proofs, attestations, or signatures | Their owning trust-object families |
| Release, correction, withdrawal, or rollback decisions | [`release/`](../../../release/README.md) |
| Public APIs, graphs, maps, indexes, or AI stores | Governed delivery/runtime after release |
| Secrets, private endpoints, signed URLs, or harmful-precision metadata | Approved restricted systems |

## Inputs and outputs

**Permitted inputs:** official W3C specifications and errata; accepted KFM doctrine and ADRs; exact repository history; contracts, schemas, policy, fixtures, validators, tests, reports, and consumers tied to a revision; sensitivity review; and correction/migration evidence.

**Permitted outputs:** human navigation, scope clarification, a bounded conflict register, a no-loss comparison or migration plan, truth labels, and links to owning surfaces.

**Not emitted:** PROV payloads, evidence conclusions, source admission, policy decisions, review approval, release decisions, public artifacts, or publication authority.

## Exposure, mutation, and retention

| Axis | Contract |
|---|---|
| Exposure | Public repository documentation; no restricted payload or sensitive operational detail |
| Mutation | Versioned replacement through reviewed pull requests |
| Retention | Durable documentation and Git history; preserve correction and supersession lineage |
| Public-client dependency | None; this is not a runtime or policy source |
| Deletion | HOLD until redundancy, consumers, links, history retention, and reviewed retirement are proven |

## Validation and review

For this README:

- parse `KFM_META_BLOCK_V2`;
- preserve one H1, logical headings, balanced fences, valid tables, and final newline;
- resolve every introduced repository-relative link and internal fragment;
- check official W3C references at a dated point;
- scan for unsupported adoption, conformance, CI, security, release, or publication claims;
- scan for secrets and sensitive detail;
- bind final bytes in a generated authoring receipt; and
- keep the diff to this file plus direct authoring dependencies.

A future profile change must additionally prove machine-profile bindings, positive and negative fixtures, deterministic validation, producer/consumer round trips, sensitivity tests, release/rollback evidence, and exact-scope interoperability.

The verified CODEOWNERS route is `@bartytime4life`; accountable standards, evidence, catalog, security/privacy, release, and correction stewardship remains **NEEDS VERIFICATION**.

## Convergence protocol

This README does not select a canonical winner. A future dependency-closed reconciliation should:

1. pin the three profile documents, this README, inbound links, contracts, schemas, validators, data lanes, and consumers;
2. separate semantic PROV, PAV, OpenLineage, supply-chain provenance, receipts, catalog projections, and release lineage;
3. build a no-loss matrix of unique, overlapping, stale, contradicted, and unsupported content;
4. choose one semantic-profile identity through reviewed authority, not an implicit rename;
5. preserve compatibility only for verified consumers;
6. align contracts, schemas, contexts, mappings, fixtures, validators, tests, workflows, registries, and emitters;
7. prove fail-closed behavior for missing evidence, invalid PROV, unknown namespaces, sensitive leakage, stale correction state, and unresolved receipt references;
8. migrate links and consumers without breaking stable identity; and
9. record correction and rollback evidence.

Until then, consolidation, rename, or deletion remains **HOLD**.

## Open verification register

| ID | State | Required resolution |
|---|---|---|
| `PROV-OPEN-001` | **NEEDS VERIFICATION** | Canonical semantic-profile identity: `PROV.md`, `PROV-O.md`, or reviewed synthesis |
| `PROV-OPEN-002` | **NEEDS VERIFICATION** | Whether this nested directory remains needed after convergence |
| `PROV-OPEN-003` | **NEEDS VERIFICATION** | Adopted PAV subset, currentness posture, and namespace treatment |
| `PROV-OPEN-004` | **UNKNOWN** | Authoritative contexts, schemas, SHACL/OWL resources, and namespace registry |
| `PROV-OPEN-005` | **UNKNOWN** | Current PROV producers, consumers, validators, APIs, graphs, maps, indexes, and AI uses |
| `PROV-OPEN-006` | **NEEDS VERIFICATION** | Identity-preserving OpenLineage ↔ RunReceipt ↔ PROV ↔ catalog mapping |
| `PROV-OPEN-007` | **NEEDS VERIFICATION** | Public redaction, aggregation, delay, and access rules for provenance fields |
| `PROV-OPEN-008` | **PROPOSED** | Stable KFM namespace and extension governance without redefining W3C predicates |
| `PROV-OPEN-009` | **UNKNOWN** | Writer/consumer closure for `data/prov/` migration or retirement |
| `PROV-OPEN-010` | **PROPOSED** | Finite conformance outcomes and reason codes |
| `PROV-OPEN-011` | **NEEDS VERIFICATION** | W3C errata and revision-watch procedure |
| `PROV-OPEN-012` | **NEEDS VERIFICATION** | Accountable reviewers for material profile change |

## Correction, rollback, and history

When inaccurate, pin the affected bytes and contradicting evidence, classify the correction, update the smallest responsible documentation set, preserve stable identity/anchors, refresh the authoring receipt, and record downstream implications.

Before merge, close the draft pull request and abandon the branch. After an authorized merge, revert the merge commit or restore prior blob:

```text
a4283dac33ec9f2c182a8be0cb0d23a3e1ba13e0
```

That blob is the exact DUO duplicate and is rollback history—not valid PROV-family guidance. Restoring it reopens the path/content defect.

| Date | Change | State |
|---|---|---|
| 2026-05-24 | Empty README created | **CONFIRMED** |
| 2026-05-25 | README replaced with bytes identical to `DUO_PROFILE.md` | **CONFIRMED** |
| 2026-08-14 | Same-path boundary correction and convergence register | **PROPOSED until reviewed and merged** |

No target-specific PROV content is lost: legitimate DUO content remains at [`DUO_PROFILE.md`](../DUO_PROFILE.md), history remains recoverable, and the overlapping provenance profiles remain visible.

`next_action: REVIEW_BOUNDARY_THEN_DECIDE_PROFILE_CONVERGENCE_SEPARATELY`

[Back to top](#top)
