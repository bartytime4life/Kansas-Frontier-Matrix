<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0030-geology-resource-character-vocabulary
title: "ADR-0030 — Geology Resource-Character Vocabulary"
type: adr
adr_id: ADR-0030
version: v1.1
status: proposed
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — Geology domain steward"
  - "OWNER_TBD — Natural Resources steward"
  - "OWNER_TBD — source and evidence steward"
  - "OWNER_TBD — contract and schema steward"
  - "OWNER_TBD — policy and sensitivity steward"
owner_status: "CODEOWNERS routes docs/adr/ and affected trust-bearing roots to @bartytime4life; accepted scientific, resource-estimate, reserve-classification, production, permit, model, source, evidence, policy, sensitivity, release, and independent-review assignments remain unverified"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Geology domain steward
  - Natural Resources steward
  - Source and evidence steward
  - Contract and schema steward
  - Resource-estimate and reserve-classification reviewer
  - Production and regulatory-data reviewer
  - Model and uncertainty reviewer
  - Policy, rights, and sensitivity reviewer
  - Validation and CI steward
  - Release and rollback steward
created: 2026-08-03
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Record the proposed minimum Geology resource-character vocabulary, its anti-collapse semantics, and the bounded graduation criteria for machine enforcement without certifying resources, admitting sources, activating policy, or authorizing release or publication."
current_path: docs/adr/ADR-0030-geology-resource-character-vocabulary.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a59c9005ca3a790846cabdcf1a160222ed73bbe4
  target_prior_blob: a4b41973fd27b851f5eca60992cb05a38e37008b
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  mineral_occurrence_contract_blob: dcf5eab9bf4fed647558d6fdc3a153c8661e034b
  resource_deposit_contract_blob: 91efc3e6aa509e7dc65b55b33bf366b437423e6f
  resource_estimate_contract_blob: 20673b0184b4e7f09c754263ab75b89f6947d9a0
  mineral_occurrence_schema_blob: d14deb401452ef703ac9b57c82f2f87df4843185
  resource_deposit_schema_blob: 8f0343623e2f873c2dac5df398aed3866d30248f
  resource_estimate_schema_blob: dca8c4081d0cbf94e61deb97345b1a7cf7d5c8fd
  geology_schema_readme_blob: beb2ee7a82ff77305f8259b554e9fe458349a123
  source_role_matrix_blob: 1143c82a5de023424509aa13d8c0fe72e2437bd1
  resource_class_fixture_readme_blob: 39500fcc3c12393fcc3ebccadab9b0fb0994c753
  resource_class_validator_blob: 821d14c3bdc44f5e7af651c343e24827279e0fd2
  resource_class_test_blob: 55ad09149480f72bd79a714f7df5fe626be19653
  production_material_change_contract_blob: 1f591a778ae1da037b27ca82d83b05b45fab4155
  geology_policy_readme_blob: 71e4a939510712346c3b80e62c47d1770e799c03
  domain_geology_workflow_blob: 74d6de5d27d7704957a89d025fdbbd2a7a01043e
  geology_source_map_blob: 028ec7c9304dbeff12697c050b3dcafe17eb550b
  geology_architecture_report_sha256: d334f43df8fd74f17115cc0f51861cf8238c9cb99d37adaf95f5e4e1655fdf51
  resource_class_pr: 1926
  adr_origin_pr: 1934
  latest_domain_geology_run: 31823429967
inspection_boundary: >
  Current-session GitHub reads over the exact target, canonical ADR inventory,
  accepted Directory Rules decision and adopted bytes, three Geology semantic
  contracts and paired schemas, Geology source-role matrix, resource-class
  fixtures/validator/tests, production material-change contract, Geology policy
  boundary, domain workflow, latest hosted Geology run, and the governed source
  map for the supplied Geology architecture report. No live mineral, resource,
  reserve, production, permit, model, property, well, borehole, source endpoint,
  policy evaluator, EvidenceBundle resolver, release environment, public client,
  or deployed runtime was exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0017-source-descriptor-admission-process.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/truth-posture.md
  - docs/domains/geology/README.md
  - docs/domains/geology/SCOPE.md
  - docs/domains/geology/OBJECT_FAMILIES.md
  - docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - docs/domains/geology/SENSITIVITY.md
  - docs/domains/geology/sublanes/natural_resources.md
  - docs/intake/exploratory/geology-natural-resources-architecture-source-map.md
  - contracts/domains/geology/MineralOccurrence.md
  - contracts/domains/geology/ResourceDeposit.md
  - contracts/domains/geology/ResourceEstimate.md
  - contracts/domains/geology/production_material_change.md
  - schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json
  - schemas/contracts/v1/domains/geology/resource_deposit.schema.json
  - schemas/contracts/v1/domains/geology/resource_estimate.schema.json
  - fixtures/domains/geology/resource_class/README.md
  - tools/validators/domains/geology/validate_resource_class_distinction.py
  - tests/domains/geology/test_source_role_anti_collapse.py
  - policy/domains/geology/README.md
  - .github/workflows/domain-geology.yml
tags: [kfm, adr, geology, natural-resources, resource-character, vocabulary, anti-collapse, source-role, object-family, classification-scheme, evidence, schema, public-safety]
notes:
  - "v1.1 is a same-path repository-grounded modernization. It preserves source and effective status as proposed; it does not accept ADR-0030."
  - "The seven-token set remains a proposed minimum vocabulary. Current executable resource-class proof is a separate three-token fixture profile, not vocabulary authority."
  - "The three paired Geology schemas remain permissive scaffolds; no shared resource-character schema exists at the evidence checkpoint."
  - "A production material-change profile now exists, but its PRODUCTION_RECORDS dataset role and watcher outcomes do not admit resource_character PRODUCTION."
  - "The latest domain-geology workflow is green for four bounded no-network profiles while proof and publish jobs retain explicit holds."
  - "No external resource/reserve classification scheme, source, real record, policy bundle, release, deployment, or publication is adopted here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0030 — Geology Resource-Character Vocabulary

> **Proposed decision.** KFM should use a small, closed `resource_character`
> vocabulary to state what kind of Geology or Natural Resources claim a record
> represents, while keeping object identity, source role, source-native
> classification, evidence, policy, sensitivity, release, and correction as
> separate axes.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR identity: confirmed](https://img.shields.io/badge/ADR--0030-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Fixture proof: three characters](https://img.shields.io/badge/fixture%20proof-three%20characters-0969da?style=flat-square)](#bounded-resource-class-proof)
[![Shared schema: absent](https://img.shields.io/badge/shared%20schema-ABSENT-b42318?style=flat-square)](#schema-and-contract-status)
[![Policy: evaluator unbound](https://img.shields.io/badge/policy-evaluator%20unbound-6e7781?style=flat-square)](#policy-evidence-and-release-boundary)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity, acceptance, and implementation are separate facts.** The canonical
> ADR index uniquely assigns `ADR-0030` to this file and records both source and
> effective status as `proposed`. The accepted Directory Rules decision confirms
> that `docs/adr/` owns the human decision record. Neither fact accepts the
> vocabulary, hardens a schema, admits a source, certifies a resource, or grants
> release authority.

> [!CAUTION]
> **The current executable profile is narrower than this proposal.** The frozen
> `kfm-geology-resource-class-fixture-v1` profile accepts only
> `MINERAL_OCCURRENCE`, `RESOURCE_DEPOSIT`, and `RESOURCE_ESTIMATE`. It rejects
> reserve, production, permit, modeled-potential, direct-observation, and
> sensitive-location collapse. That is substantive fixture behavior, not a
> canonical seven-token vocabulary.

> [!WARNING]
> **Recognizing a word is not admitting an object family.** `RESERVE`,
> `PRODUCTION`, `PERMIT`, and `MODELED_POTENTIAL` remain proposed vocabulary
> members without accepted Geology object-family contracts or schemas. They
> cannot be inserted into one of the three existing schemas merely because this
> ADR names them.

> [!NOTE]
> **Current Geology CI is green but bounded.** The latest inspected
> `domain-geology` run completed the resource-class, AEM campaign, public-safe
> geometry, and production material-change checks successfully. Its proof and
> publish-dry-run jobs intentionally record holds. A green workflow does not
> establish vocabulary acceptance, live-source truth, policy evaluation,
> EvidenceBundle closure, resource or reserve validity, or publication.

**Quick navigation:** [Status](#status) · [Evidence boundary](#evidence-boundary) · [Repository evidence](#current-repository-evidence) · [Context](#context) · [Decision](#decision) · [Vocabulary](#vocabulary-semantics) · [Anti-collapse](#anti-collapse-rules) · [Source roles](#source-role-and-object-family-boundaries) · [Evidence](#stewardship-and-evidence-requirements) · [Implementation](#current-implementation-maturity) · [Conflicts](#conflict-and-hold-register) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Authority](#authority-and-publication-boundary) · [Rollback](#rollback-and-supersession) · [Verification](#verification-checklist) · [Open work](#open-questions) · [References](#references) · [No-loss ledger](#appendix-a--no-loss-reconciliation-ledger)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0030` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0030-geology-resource-character-vocabulary.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` — non-binding |
| **Decision class** | Cross-contract Geology/Natural Resources claim-character vocabulary and anti-collapse semantics |
| **Proposed token set** | Seven exact tokens; see [Decision](#decision) |
| **Current executable posture** | Three-token synthetic fixture profile plus separate bounded Geology assessment profiles |
| **Current schema posture** | Three permissive object schemas; no shared `resource_character` schema |
| **Current policy posture** | Geology policy source exists as scaffolding; evaluator, bundle, and governed consumer remain unbound |
| **Evidence checkpoint** | `main@a59c9005ca3a790846cabdcf1a160222ed73bbe4` |
| **Implementation effect of this revision** | Documentation only |
| **Publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Acceptance versus implementation graduation

Two independent state transitions must remain visible:

1. **ADR acceptance** would approve the seven-token vocabulary and normative
   anti-collapse semantics.
2. **Implementation graduation** would require accepted contract/schema
   ownership, a shared vocabulary schema, compatibility fixtures, deterministic
   validators, source and evidence closure, policy mapping, consumer behavior,
   review, correction, and rollback evidence.

An accepted ADR without the implementation gates would be governing doctrine,
not proof that real records are valid. Conversely, fixture tests, schema
validation, a workflow pass, a commit, a pull request, or a merge cannot accept
this ADR.

### Governing placement authority

Accepted [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the exact Directory Rules v2 bytes at
[`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). For this
decision family, that authority split is:

| Responsibility | Owning surface |
|---|---|
| Human architectural decision | `docs/adr/` |
| Domain and source-role explanation | `docs/domains/geology/` |
| Semantic object meaning | `contracts/domains/geology/` |
| Machine-checkable shape | `schemas/contracts/v1/domains/geology/` |
| Admissibility and exposure | `policy/domains/geology/` and shared policy surfaces |
| Source identity and authority limits | `data/registry/sources/geology/` |
| Synthetic replay | `fixtures/` |
| Validation mechanics | `tools/validators/` and `tests/` |
| Release, correction, and rollback | `release/` and owning accountability families |

This same-path update changes no responsibility boundary and creates no parallel
schema, policy, source, evidence, receipt, proof, or release authority.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded in current repository evidence at
`main@a59c9005ca3a790846cabdcf1a160222ed73bbe4`.

### Truth labels

| Label | Meaning in this ADR |
|---|---|
| **CONFIRMED** | Verified from current repository bytes, hosted checks, merged PR records, or exact readback |
| **PROPOSED** | Decision, vocabulary, path, mapping, obligation, or implementation target not accepted or operationally proved |
| **NEEDS VERIFICATION** | A concrete owner, source, mapping, schema, consumer, or behavior remains to be checked |
| **UNKNOWN** | The inspected surfaces do not support a stronger conclusion |
| **CONFLICTED** | Two repository surfaces make incompatible naming, membership, or authority claims |
| **HELD** | The current system intentionally blocks graduation or release while prerequisites remain open |

### Inspected surfaces

- the complete current ADR and canonical ADR index;
- accepted ADR-0029 and the exact adopted Directory Rules bytes;
- `MineralOccurrence`, `ResourceDeposit`, and `ResourceEstimate` semantic contracts;
- their three paired JSON Schema files;
- the Geology schema README and contract-lane README;
- the Geology source-role matrix;
- the frozen resource-class fixture README, validator, and focused tests;
- the `ProductionMaterialChange` contract;
- the Geology policy boundary;
- the `domain-geology` workflow and its latest hosted run;
- the governed source map for the supplied Geology architecture report;
- merged PRs #1926 and #1934.

### What this evidence cannot prove

This revision does not prove:

- ADR-0030 is accepted;
- any source is admitted, current, complete, accurate, licensed, or public-safe;
- any real occurrence, deposit, estimate, reserve, production record, permit, or
  modeled potential is valid;
- the seven-token set is scientifically or legally complete;
- an external reporting or reserve-classification scheme is adopted;
- the four unadmitted characters have canonical object families;
- the three current schemas enforce resource-character semantics;
- a policy evaluator selects or enforces these distinctions;
- EvidenceRefs resolve to EvidenceBundles for real resource claims;
- public APIs, maps, exports, graph projections, or AI surfaces expose the
  vocabulary safely;
- proof, release, deployment, or publication occurred.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current status | Safe conclusion |
|---|---:|---|
| ADR identity and index row | **CONFIRMED** | Exact path exists; source and effective status remain `proposed` |
| Directory Rules placement | **CONFIRMED accepted through ADR-0029** | Same-path `docs/adr/` placement is governed; no semantic acceptance follows |
| `MineralOccurrence` contract | **CONFIRMED draft / substantive** | Defines reported presence and explicitly excludes deposit, estimate, reserve, permit, production, and ownership implications |
| `ResourceDeposit` contract | **CONFIRMED draft / substantive** | Defines a named or delineated body and excludes estimate, reserve, permit, production, ownership, and operation implications |
| `ResourceEstimate` contract | **CONFIRMED draft / substantive** | Defines a modeled or compiled quantity/classification claim and excludes direct observation and reserve-by-default |
| Three paired object schemas | **CONFIRMED permissive scaffolds** | Each has empty `properties`, `additionalProperties: true`, and no resource-character enforcement |
| Shared resource-character schema | **ABSENT at checkpoint** | No `resource_character.schema.json` exists in the Geology schema lane |
| Contract-pointer casing | **CONFLICTED** | Three lower-case `x-kfm.contract_doc` pointers do not resolve to the tracked PascalCase contracts |
| Geology schema README | **CONFIRMED stale inventory** | It says no concrete Geology schemas were confirmed even though the lane now contains many schema files |
| Geology source-role matrix | **CONFIRMED draft** | Seven source roles and fail-closed collapse rules are documented; matrix defaults and naming remain non-binding |
| Resource-class fixture profile | **CONFIRMED substantive / synthetic** | Three exact character/object-family pairings and eight exact negative cases are enforced without network access |
| Resource-class validator/test | **CONFIRMED deterministic** | Closed shapes, bounded arrays, stable findings, duplicate-key rejection, no-value echo, and no-network behavior are tested |
| Production material-change profile | **CONFIRMED separate bounded profile** | Compares production snapshot metadata using `PRODUCTION_RECORDS`; it does not admit the `PRODUCTION` resource character |
| Geology public-safe geometry profile | **CONFIRMED separate bounded profile** | Tests geometry-declaration safety; it does not classify resource character or authorize exposure |
| Geology policy lane | **CONFIRMED scaffolding / evaluator unbound** | Intent and defaults exist, but no accepted bundle, evaluator, authenticated decision emitter, or governed consumer is established |
| Latest `domain-geology` run | **CONFIRMED success with holds** | Four bounded validation profiles ran; proof and publish jobs remained explicit readiness holds |
| Evidence, proof, release, publication | **NOT ESTABLISHED** | No current surface makes this vocabulary a released or public truth authority |

### Material corrections from v0.1

- Pins the ADR to the current repository and canonical 34-record ADR index.
- Records ADR-0029 as the accepted placement authority without implying that
  ADR-0030 is accepted.
- Corrects the change-history reference from “pending” to merged PR #1934.
- Records the current substantive three-character fixture proof instead of
  describing it only through its origin PR.
- Records the newer production material-change and public-safe geometry profiles
  without collapsing either into vocabulary admission.
- Records the latest successful `domain-geology` run while preserving its proof
  and publish holds.
- Confirms that the three paired schemas remain permissive and that the shared
  vocabulary schema is still absent.
- Records the Geology policy lane as evaluator-unbound rather than implying
  policy enforcement.
- Keeps source admission, external classification schemes, scientific/legal
  authority, real data, public clients, release, and publication unverified.

[Back to top](#top)

---

<a id="context"></a>

## Context

Natural-resource records are especially vulnerable to semantic inflation. A
reported material presence can be mislabeled as a deposit; a deposit can be
presented as a quantified resource; a modeled estimate can be presented as a
reserve; a permit or production record can be treated as proof of physical
geology, ownership, current operation, or economic viability.

KFM already carries four distinct concepts that must not be collapsed:

```text
what kind of claim?              -> resource_character
which semantic record owns it?   -> object_family
how was supporting knowledge made? -> source_role
which source-native scheme applies? -> classification_scheme_ref
```

A fifth axis—policy/release state—decides whether a governed operation may use
or expose the record. It is not derivable from any of the four semantic axes.

### Current bounded implementation

Merged PR #1926 turned one narrow profile into executable fixture proof. It
accepts only:

| `resource_character` | `object_family` | Profile-local `source_role` | Bounded claim |
|---|---|---|---|
| `MINERAL_OCCURRENCE` | `MineralOccurrence` | `observed` | Reported presence only |
| `RESOURCE_DEPOSIT` | `ResourceDeposit` | `aggregate` | Delineated-body context only |
| `RESOURCE_ESTIMATE` | `ResourceEstimate` | `modeled` | Modeled quantity with scheme, method, date, confidence, and assumptions |

Those source-role pairings are frozen fixture values, not universal rules. The
current source-role matrix permits more nuanced evidence roles and requires a
SourceDescriptor to carry the binding source role and authority limits.

### Why a decision is still needed

Without a reviewed shared vocabulary:

- schemas may introduce incompatible token spellings;
- consumers may infer stronger truth from filenames, free text, or source roles;
- `reserve_estimate` may be mistaken for accepted reserve status;
- `PRODUCTION_RECORDS` may be mistaken for a physical resource character;
- modeled prospectivity may be converted into deposit truth;
- permit or production context may be joined into resource truth without
  preserving evidence and time;
- public clients may expose a semantic label without the source, evidence,
  sensitivity, review, and release state needed to interpret it.

The ADR therefore defines a proposed semantic boundary before machine
enforcement expands.

[Back to top](#top)

---

<a id="decision"></a>

## Decision

If accepted, KFM SHALL apply the following rules to Geology and Natural
Resources records that carry a normalized resource-character claim.

### D1 — `resource_character` is a first-class claim-character field

`resource_character` states what kind of resource-related claim the record
represents. It does not state who produced the evidence, which contract owns the
record, whether an external classification is valid, or whether the record may
be released.

### D2 — The minimum set is closed and exact

The accepted field would use exactly:

```text
MINERAL_OCCURRENCE
RESOURCE_DEPOSIT
RESOURCE_ESTIMATE
RESERVE
PRODUCTION
PERMIT
MODELED_POTENTIAL
```

Unknown tokens fail closed. Adding, renaming, merging, or changing the meaning
of a token requires a reviewed contract/schema change and an ADR amendment or
successor when the decision changes materially.

### D3 — Four semantic axes remain orthogonal

| Axis | Question answered | Example |
|---|---|---|
| `resource_character` | What kind of claim is represented? | `RESOURCE_ESTIMATE` |
| `object_family` | Which semantic contract owns the record? | `ResourceEstimate` |
| `source_role` | How was the supporting knowledge produced? | `modeled` |
| `classification_scheme_ref` | Which source-native scientific, economic, or legal scheme defines the source label? | Versioned scheme reference |

Policy decision, sensitivity posture, review state, and release state remain
additional independent axes.

### D4 — Vocabulary recognition is not object-family admission

The vocabulary may recognize all seven characters while only the first three
have current draft semantic object families. Until separately accepted
contracts and schemas exist, `RESERVE`, `PRODUCTION`, `PERMIT`, and
`MODELED_POTENTIAL` remain unadmitted for the three current object schemas.

### D5 — Character may not be inferred from weak signals

A producer or consumer MUST NOT infer `resource_character` solely from:

- `source_role`;
- filename or path;
- UI label or map style;
- source-native free text;
- commodity name;
- a linked record;
- a workflow outcome;
- a production watcher disposition;
- model confidence; or
- an AI-generated summary.

### D6 — Source-native meaning is preserved

Normalization MUST retain the source-native label, source record identity,
classification scheme and edition, mapping version, effective time, and
limitations. The normalized token must not erase a more precise source
classification or manufacture one where the source is ambiguous.

### D7 — Relationships do not collapse identity

Occurrence, deposit, estimate, reserve, production, permit, modeled-potential,
extraction, reclamation, ownership, and facility records may reference one
another only through explicit, evidence-bound, time-aware relations. A relation
does not make two records the same object or transfer authority from one to
another.

### D8 — The vocabulary grants no policy or publication state

No `resource_character` value may by itself establish:

- source admission;
- evidence sufficiency;
- rights or redistribution permission;
- sensitivity or public-safe precision;
- review approval;
- economic or legal status;
- policy allow;
- promotion eligibility;
- release; or
- publication.

### Non-goals

This ADR does not:

- accept itself;
- certify resources or reserves;
- adopt an external resource/reserve reporting standard;
- define a commodity taxonomy;
- decide permit validity, compliance, ownership, title, or operation status;
- create source descriptors or retrieve real records;
- define every Geology object family;
- activate policy;
- choose public DTO fields;
- authorize a map, API, graph, export, or AI response;
- create proof, release, deployment, or publication state.

[Back to top](#top)

---

<a id="vocabulary-semantics"></a>

## Vocabulary semantics

| Character | Minimum proposed meaning | Current object-family admission | Must not imply |
|---|---|---|---|
| `MINERAL_OCCURRENCE` | Reported mineral, commodity, or material presence at a source-supported place or area | `MineralOccurrence` draft contract; fixture-positive | Deposit identity, quantity, reserve, economic viability, permit, production, ownership, or public exposure |
| `RESOURCE_DEPOSIT` | Named, delineated, or source-characterized body treated as a deposit | `ResourceDeposit` draft contract; fixture-positive | Quantity, reserve, economics, permit, production, title, ownership, or operation |
| `RESOURCE_ESTIMATE` | Modeled, compiled, classified, or aggregated quantity/classification claim under explicit method and assumptions | `ResourceEstimate` draft contract; fixture-positive | Direct observation, deposit identity, reserve by default, production, permit, economic viability, or release |
| `RESERVE` | Explicit source-classified reserve assertion under a cited scheme, effective date, assumptions, and qualified review | **Unadmitted** | Estimate, deposit, occurrence, production, permit, ownership, or KFM certification |
| `PRODUCTION` | Time-bounded reported production record from an appropriate administrative, regulatory, or observed evidence chain | **Unadmitted**; current material-change profile is process-only | Deposit, reserve, estimate, permit validity, current operation, ownership, or physical-geology truth |
| `PERMIT` | Issuer- and jurisdiction-bound regulatory authorization record with source-native status and effective interval | **Unadmitted** | Resource existence, extraction, production, ownership, reserve, compliance, or current operation |
| `MODELED_POTENTIAL` | Model-derived prospectivity, favorability, or potential with versioned inputs, method, uncertainty, and limitations | **Unadmitted** | Occurrence, deposit, estimate quantity, reserve, permit, production, or economic viability |

### Boundary examples

| Input statement or object | Correct posture |
|---|---|
| A field or compiled source reports mineral presence | Candidate `MINERAL_OCCURRENCE`, subject to source/evidence review |
| A source delineates a named resource body | Candidate `RESOURCE_DEPOSIT`, not an estimate or reserve |
| A source publishes a quantity under explicit method and classification | Candidate `RESOURCE_ESTIMATE`, unless explicit accepted reserve evidence supports a separate reserve record |
| A permit exists for a site | `PERMIT` context only; it does not prove deposit, production, ownership, or compliance |
| A production table changes month-to-month | Production process evidence; not deposit, estimate, reserve, or permit proof |
| A model highlights favorable geology | `MODELED_POTENTIAL`; not occurrence or deposit truth |
| A source uses the label `reserve_estimate` | Preserve the source label and scheme; do not normalize to `RESERVE` without the reserve evidence floor |
| An AI summary calls an estimate “proven reserves” | Reject or abstain; generated wording cannot upgrade character |

[Back to top](#top)

---

<a id="anti-collapse-rules"></a>

## Anti-collapse rules

If accepted, implementations MUST enforce these invariants.

1. A record carries exactly one normalized `resource_character`.
2. Unknown, missing, multiple, or unsupported values fail closed.
3. `MINERAL_OCCURRENCE` is not `RESOURCE_DEPOSIT`.
4. `RESOURCE_DEPOSIT` is not `RESOURCE_ESTIMATE`.
5. `RESOURCE_ESTIMATE` is not `RESERVE` by default.
6. `MODELED_POTENTIAL` is not occurrence, deposit, estimate quantity, or reserve.
7. `PERMIT` is regulatory context, not physical-geology or production proof.
8. `PRODUCTION` is time-bounded production evidence, not deposit, estimate,
   reserve, permit validity, ownership, or current-operation proof.
9. `source_role: observed` does not create an occurrence automatically.
10. `source_role: modeled` does not create an estimate or potential automatically.
11. Aggregate and administrative records do not become per-place observed truth.
12. A public-safe geometry declaration does not establish resource character.
13. A workflow outcome, validator pass, receipt, or release path does not
    establish scientific, economic, legal, or regulatory truth.
14. A cross-character link must preserve both identities, evidence, time,
    sensitivity, and correction lineage.
15. Public eligibility remains a separate governed decision.

### Deterministic classification order

A future normalizer should proceed in this order:

1. validate object shape and source identity;
2. resolve source-native label and classification scheme;
3. verify source role and authority limits;
4. resolve evidence and temporal scope;
5. determine whether one exact normalized character is supported;
6. preserve ambiguity as review or abstention rather than guessing;
7. apply policy, sensitivity, review, and release gates separately;
8. emit the governed record or finite negative outcome.

This ordering is a proposed semantic rule. The repository does not yet establish
a canonical normalizer that performs it end to end.

[Back to top](#top)

---

<a id="source-role-and-object-family-boundaries"></a>

## Source-role and object-family boundaries

### Source role is evidence character, not resource character

The current draft Geology source-role matrix names seven roles:

```text
observed
regulatory
modeled
aggregate
administrative
candidate
synthetic
```

Those values answer how knowledge was produced or held. They do not answer
whether the record is an occurrence, deposit, estimate, reserve, production,
permit, or modeled potential.

| Example | `source_role` | Possible `resource_character` | Required caution |
|---|---|---|---|
| Field observation of material | `observed` | `MINERAL_OCCURRENCE` | Observation still requires reviewed occurrence identity |
| Compiled deposit inventory | `aggregate` or `administrative` | `RESOURCE_DEPOSIT` | Preserve compilation and aggregation limits |
| Model-derived quantified estimate | `modeled` | `RESOURCE_ESTIMATE` | Scheme, method, date, confidence, and assumptions required |
| Regulatory permit register | `regulatory` or `administrative` | `PERMIT` | Permit does not prove geology, extraction, or compliance |
| Production reporting table | `regulatory`, `administrative`, or another reviewed role | `PRODUCTION` | Reporting grain and time remain explicit |
| Prospectivity model | `modeled` | `MODELED_POTENTIAL` | Potential does not become occurrence or deposit |
| Synthetic demonstration fixture | `synthetic` | Fixture-scoped only | Cannot support a real-world resource claim |

The matrix is draft and its cell defaults are not accepted by this ADR. The
binding source role for real records must come from an admitted
`SourceDescriptor`.

### Object family owns meaning

`object_family` answers which semantic contract owns the record. The first
three proposed pairings are:

| `resource_character` | Current draft `object_family` |
|---|---|
| `MINERAL_OCCURRENCE` | `MineralOccurrence` |
| `RESOURCE_DEPOSIT` | `ResourceDeposit` |
| `RESOURCE_ESTIMATE` | `ResourceEstimate` |

No current accepted pairing exists for the other four characters. Reusing one
of the three object families to bypass that gap is prohibited.

### Production material-change is not character admission

The repository now contains a proposed
`ProductionMaterialChange` comparison contract. It uses:

```text
dataset_role = PRODUCTION_RECORDS
outcome = NO_CHANGE | REVIEW | HOLD | ERROR
```

That object compares metadata for two version-pinned production snapshots. It
does not carry or admit `resource_character: PRODUCTION`, validate production
rows, establish deposit or reserve truth, or authorize release. Its existence
therefore strengthens anti-collapse evidence without closing ADR-0030's
production-ownership question.

### Public-safe geometry is a separate gate

The Geology public-safe geometry assessment checks whether a public projection
declaration is generalized, withheld, denied, evidence-linked, and free of
coordinate material. It does not determine whether the underlying claim is an
occurrence, deposit, estimate, reserve, production record, permit, or modeled
potential. Both gates may apply to one future record, but neither substitutes
for the other.

[Back to top](#top)

---

<a id="schema-and-contract-status"></a>

## Schema and contract status

### Semantic contracts

The three current contracts are substantive but remain draft:

| Contract | Current meaning | Resource-character relationship |
|---|---|---|
| [`MineralOccurrence`](../../contracts/domains/geology/MineralOccurrence.md) | Reported presence | Proposed one-to-one pairing with `MINERAL_OCCURRENCE` |
| [`ResourceDeposit`](../../contracts/domains/geology/ResourceDeposit.md) | Named or delineated body | Proposed one-to-one pairing with `RESOURCE_DEPOSIT` |
| [`ResourceEstimate`](../../contracts/domains/geology/ResourceEstimate.md) | Modeled or compiled quantity/classification claim | Proposed one-to-one pairing with `RESOURCE_ESTIMATE` |

Each contract also carries broader field proposals, sensitivity posture, and
anti-collapse guidance. None is an accepted source, scientific certification,
policy decision, or release record.

### Machine schemas

The paired schemas currently share the same limits:

| Schema | Current field enforcement | Contract pointer |
|---|---|---|
| `mineral_occurrence.schema.json` | Empty `properties`; `additionalProperties: true` | Lower-case path that does not resolve to tracked PascalCase contract |
| `resource_deposit.schema.json` | Empty `properties`; `additionalProperties: true` | Lower-case path that does not resolve to tracked PascalCase contract |
| `resource_estimate.schema.json` | Empty `properties`; `additionalProperties: true` | Lower-case path that does not resolve to tracked PascalCase contract |

No shared `resource_character.schema.json` exists at the evidence checkpoint.
The Geology schema README also retains a stale claim that no concrete Geology
schemas were confirmed. That README drift is documentation debt, not evidence
that the schema files are absent.

### Proposed first schema ratchet

Only after this ADR is accepted, the smallest dependency-closed implementation
should:

1. add a shared schema fragment at the Directory-Rules-aligned Geology schema
   lane with exactly the seven tokens;
2. correct the three contract pointers to the tracked contract paths;
3. minimally require `object_family`, `resource_character`, `source_role`,
   `source_descriptor_ref`, and non-empty `evidence_refs`;
4. bind the first three schemas to exact object-family/resource-character pairs;
5. retain `additionalProperties: true` for the first compatibility ratchet unless
   a separately reviewed closed-shape migration is ready;
6. add positive, unknown-token, cross-family, and anti-collapse fixtures;
7. validate through the repository's accepted schema and Geology checks; and
8. leave sources, policy, lifecycle data, APIs, release, and publication
   untouched.

The four unadmitted characters belong in the shared enum and negative
compatibility tests only during that first ratchet.

[Back to top](#top)

---

<a id="bounded-resource-class-proof"></a>

## Bounded resource-class proof

The frozen fixture profile is a substantive implementation surface with a
deliberately narrow authority boundary.

### Confirmed behavior

- three explicit valid fixtures;
- eight explicit invalid fixtures with sorted finding-code sidecars;
- exact object-family/character/profile checks;
- missing, unknown, and multiple-character rejection;
- reserve, permit, production, modeled-potential, observation, and location
  collapse rejection;
- estimate classification, method, date, confidence, and assumption support;
- closed fixture shapes and deterministic finding order;
- bounded file size, evidence refs, limitations, and assumption refs;
- duplicate-key and non-finite JSON rejection;
- no untrusted value echo in findings;
- explicit network denial in tests and CI.

### Authority limit

A passing profile proves only that synthetic inputs satisfy or violate the
frozen profile as expected. It does not prove:

- the seven-token vocabulary is accepted;
- the three fixture source-role pairings are universal;
- the schemas enforce the profile;
- a real source or classification scheme is admitted;
- a resource claim is scientifically, economically, legally, or regulatorily
  valid;
- policy, evidence, review, release, or public-safety gates close.

Historical fixture meanings must remain stable. Future vocabulary tests should
extend the profile through a versioned successor or clearly separated
compatibility suite rather than silently changing current positive or negative
polarity.

[Back to top](#top)

---

<a id="stewardship-and-evidence-requirements"></a>

## Stewardship and evidence requirements

### Stewardship floor

| Responsibility | Required reviewed authority |
|---|---|
| Token stability and compatibility | Architecture and schema stewards |
| Occurrence and deposit meaning | Geology and Natural Resources stewards |
| Estimate methods and source classifications | Natural Resources plus identified estimate-method/classification reviewer |
| Reserve admission | Identified reserve-classification reviewer plus source, evidence, and Natural Resources review |
| Production admission | Future production/regulatory-data owner plus source and evidence review |
| Permit admission | Future regulatory/legal owner plus source and evidence review |
| Modeled-potential admission | Model/uncertainty owner plus Geology and Natural Resources review |
| Source identity, authority limits, rights, and freshness | Source steward through admitted SourceDescriptor evidence |
| Evidence resolution and correction lineage | Evidence steward |
| Exact or harmful-precision geometry | Policy and sensitivity review |
| Release, correction, and rollback | Existing release/accountability owners |

Every role above remains `OWNER_TBD` or `NEEDS VERIFICATION` unless a current
accepted record assigns it. CODEOWNERS routing is review routing, not scientific,
economic, legal, source, evidence, policy, or release authority.

### Common evidence floor

Any future admitted resource-character record must carry or resolve:

- `source_descriptor_ref`;
- `source_record_ref`;
- preserved source role and authority limits;
- non-empty EvidenceRefs and EvidenceBundle closure before consequential use;
- source-native label and normalized mapping;
- classification scheme and edition where applicable;
- source/assertion, retrieval, valid/effective, release, and correction times as
  applicable;
- rights, attribution, redistribution, and sensitivity posture;
- commodity/material context and source-native terminology;
- geometry or aggregation posture, uncertainty, and precision;
- correction, supersession, withdrawal, and stale-state lineage.

This floor does not admit a source or make a record public.

### Character-specific evidence

| Character | Additional minimum evidence before admission |
|---|---|
| `MINERAL_OCCURRENCE` | Reported commodity/material, observation or compilation basis, place/area and precision, source/observed time where supported, uncertainty, and occurrence identity |
| `RESOURCE_DEPOSIT` | Deposit identity/name, delineation or characterization basis, commodity set, geometry fingerprint, temporal validity, and explicit links to supporting occurrences or observations |
| `RESOURCE_ESTIMATE` | Source classification and scheme, method/model, estimate date, aggregation unit, quantity and units when present, confidence, assumptions, and estimate identity |
| `RESERVE` | Explicit reserve label, reporting scheme and edition, effective date, method, technical/economic assumptions, qualified review, and lineage to supporting estimates; no KFM certification inferred |
| `PRODUCTION` | Reporting period, quantity and units, reporting grain/site/facility/well context, issuer, source revision, and correction lineage |
| `PERMIT` | Issuer, jurisdiction, permit identifier, regulated scope, source-native status, effective interval, and update/correction lineage |
| `MODELED_POTENTIAL` | Model/run identities, input and specification hashes, method/version, effective date, uncertainty, limitations, and model/reality-boundary accountability |

When a required owner, source, scheme, evidence chain, time, rights state,
sensitivity posture, or classification mapping is unresolved, admission remains
held or the governed operation abstains.

[Back to top](#top)

---

<a id="current-implementation-maturity"></a>

## Current implementation maturity

| Level | Description | Current evidence |
|---|---|---|
| **M0 — vocabulary proposal** | Seven tokens and anti-collapse rules documented | **CONFIRMED proposed** |
| **M1 — bounded fixture proof** | Synthetic positive/negative behavior for three characters | **CONFIRMED** |
| **M2 — shared machine vocabulary** | Shared enum plus minimally hardened three object schemas | **NOT ESTABLISHED** |
| **M3 — semantic admission** | Accepted owners, source mappings, evidence floor, policy reasons, and correction rules | **NOT ESTABLISHED** |
| **M4 — governed consumers** | Pipelines, APIs, graph/UI/AI projections preserve all axes and fail closed | **NOT ESTABLISHED** |
| **M5 — reviewed public operation** | Released public-safe records, receipts, telemetry, correction propagation, and rollback evidence | **UNKNOWN / NOT ESTABLISHED** |

### Present safe claim

> KFM currently has a proposed seven-token Geology resource-character decision,
> substantive draft contracts for occurrence, deposit, and estimate, and a
> deterministic three-character synthetic anti-collapse profile. The repository
> does not yet establish a shared vocabulary schema, accepted four-character
> object ownership, active policy evaluation, live source/evidence closure,
> governed public consumers, or released resource claims.

The evidence does not support “the seven-token vocabulary is canonical,”
“production is admitted because a production watcher exists,” “the schemas
enforce anti-collapse,” “policy is active,” “real resource data is validated,”
or “a green Geology workflow proves release readiness.”

[Back to top](#top)

---

<a id="conflict-and-hold-register"></a>

## Conflict and hold register

| ID | Status | Conflict or hold | Safe interim posture |
|---|---|---|---|
| `RCHAR-01` | **HOLD** | ADR remains proposed | Preserve seven-token proposal; do not harden dependent authority as accepted |
| `RCHAR-02` | **ABSENT** | Shared `resource_character` schema does not exist | Keep canonical vocabulary claims in this ADR only as proposed |
| `RCHAR-03` | **HOLD** | Three object schemas remain empty permissive scaffolds | Do not claim field enforcement or admit real records through shape alone |
| `RCHAR-04` | **CONFLICTED** | Lower-case schema pointers versus PascalCase tracked contracts | Correct through one reviewed schema migration; do not create duplicate contract files |
| `RCHAR-05` | **STALE** | Geology schema README says no concrete schemas were confirmed | Update separately or with the schema ratchet; do not use the stale inventory as current tree truth |
| `RCHAR-06` | **HOLD** | `RESERVE`, `PRODUCTION`, `PERMIT`, and `MODELED_POTENTIAL` lack accepted object-family ownership | Keep them vocabulary-recognized and schema-unadmitted |
| `RCHAR-07` | **PROPOSED** | Source-role matrix is draft and contains inferred defaults/naming drift | Treat admitted SourceDescriptor as future binding authority |
| `RCHAR-08` | **HOLD** | Geology policy evaluator, bundle, and consumer are unbound | No policy-enforcement claim; fail closed at integration |
| `RCHAR-09` | **NEEDS VERIFICATION** | External source schemes, editions, mappings, and rights | Preserve source-native labels; adopt no universal scheme here |
| `RCHAR-10` | **NEEDS VERIFICATION** | Named scientific, estimate, reserve, production, permit, model, and release stewards | Missing assignments block admission |
| `RCHAR-11` | **OPEN** | Public DTO exposure of `resource_character` is undecided | Expose no raw semantic label without evidence, sensitivity, and release review |
| `RCHAR-12` | **HOLD** | Proof and publish-dry-run Geology jobs intentionally report readiness holds | Do not infer release from successful workflow conclusions |

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

### Phase 0 — Preserve the proposal boundary

- keep source and effective ADR status `proposed`;
- preserve the exact seven tokens and three-token fixture compatibility;
- correct stale documentation claims without changing semantic authority;
- keep policy, source activation, lifecycle writes, release, and publication out
  of documentation-only work.

### Phase 1 — Review the decision

- identify the required owners and independent reviewers;
- review the seven-token minimum and anti-collapse rules;
- review the distinction between vocabulary recognition and object admission;
- review external-scheme preservation and mapping requirements;
- transition this ADR and the canonical index together only through explicit
  accepted review.

### Phase 2 — Minimal schema ratchet

Implement the bounded schema slice described in
[Schema and contract status](#schema-and-contract-status):

- one shared seven-token schema fragment;
- three corrected contract pointers;
- five minimum required fields;
- three exact character/object-family constants;
- versioned positive and negative compatibility fixtures;
- focused no-network validation;
- documentation and generated-authoring provenance updates.

### Phase 3 — Character-specific ownership

For each of `RESERVE`, `PRODUCTION`, `PERMIT`, and `MODELED_POTENTIAL`:

- select the owning semantic contract and responsibility lane;
- identify qualified reviewers;
- admit source families and classification schemes separately;
- define time, identity, correction, and evidence semantics;
- define sensitivity and public-safe projection requirements;
- add fixtures and validators before consumers.

This phase may determine that one or more characters belong to an adjacent
domain contract with a Geology projection rather than a Geology-owned object.
That choice requires explicit mapping, not duplication.

### Phase 4 — Policy and evidence integration

- define accepted policy inputs, reasons, and obligations;
- ensure missing/ambiguous character support abstains or holds rather than
  defaulting to allow;
- resolve EvidenceRefs to EvidenceBundles before consequential claims;
- preserve source role, source-native classification, and character in decision
  and accountability records;
- test rights, sensitivity, stale-state, correction, and withdrawal behavior.

### Phase 5 — Governed consumers

- normalize only reviewed exact mappings;
- keep pipelines no-network in unit tests and fixture-first during admission;
- define API, graph, map, export, and Focus projection behavior;
- prevent public clients from reading canonical/internal stores;
- preserve safe explanations without exposing restricted geometry or source
  details;
- add replay, correction, cache invalidation, rollback, and compatibility tests.

### Phase 6 — Reviewed operation

- prove source admission and evidence closure for one public-safe fixture-backed
  source family;
- produce accepted decision, review, receipt, proof, release, correction, and
  rollback objects;
- verify client behavior and safe telemetry;
- retain the ability to withdraw or supersede character mappings without
  rewriting immutable source records.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

ADR-0030 should remain `proposed` until equivalent evidence closes every
applicable gate.

### Governance and ownership

- [ ] Architecture, Geology, Natural Resources, source, evidence, contract,
      schema, policy, sensitivity, validation, release, and docs reviews are
      recorded.
- [ ] Estimate-method, reserve-classification, production, permit, and model
      reviewer roles are identified or their admissions remain explicitly held.
- [ ] The ADR and canonical index carry matching reviewed status.
- [ ] Independent review or a documented bootstrap exception is recorded.

### Vocabulary semantics

- [ ] The seven tokens are reviewed as claim character, not source role,
      object-family identity, external classification, or release status.
- [ ] Minimum meanings and non-implications are accepted.
- [ ] Unknown and ambiguous mappings fail closed.
- [ ] Source-native labels and schemes remain preserved.
- [ ] Cross-character relations cannot transfer identity or authority.

### Contract and schema

- [ ] One shared seven-token schema fragment exists at the accepted schema home.
- [ ] The three existing contract pointers resolve to tracked contracts.
- [ ] The first three schemas bind exact object-family/character pairs.
- [ ] Compatibility and negative fixtures cover unknown tokens and every
      load-bearing collapse.
- [ ] The four unadmitted characters remain rejected by the three current object
      schemas.
- [ ] Schema and contract versioning/migration behavior is documented.

### Source, evidence, and policy

- [ ] SourceDescriptor and EvidenceBundle dependencies are machine-checkable.
- [ ] External schemes and editions are admitted individually with rights and
      authority limits.
- [ ] Policy mapping distinguishes unsupported, prohibited, and operational
      failure states.
- [ ] Sensitive geometry and harmful joins fail closed.
- [ ] Correction, supersession, stale-state, withdrawal, and rollback semantics
      are tested.

### Behavioral proof

- [ ] Current three-character fixture polarity remains stable.
- [ ] New fixtures are deterministic, synthetic, bounded, and no-network.
- [ ] Tests reject filename, role, free-text, workflow, and AI-based inference.
- [ ] Production material-change outcomes remain process outcomes, not character
      admission.
- [ ] Public-safe geometry assessment remains separate from character
      classification.
- [ ] Repository-native schema, Geology, validator, docs, and receipt checks pass
      on the exact review head.

### Governed consumers and release

- [ ] Pipelines and adapters preserve every semantic axis.
- [ ] Public clients consume governed projections only.
- [ ] UI/AI surfaces distinguish source role, claim character, uncertainty,
      sensitivity, and release state where permitted.
- [ ] Release cannot follow from character, schema, fixture, validator, workflow,
      or path alone.
- [ ] Correction and withdrawal propagate through APIs, maps, indexes, exports,
      and caches.
- [ ] No acceptance check itself releases or publishes data.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Gives contracts, schemas, validators, and consumers one reviewable
  anti-collapse vocabulary.
- Keeps occurrence, deposit, estimate, reserve, production, permit, and modeled
  potential semantically distinct.
- Keeps source role, object identity, source-native classification, and release
  state independent.
- Preserves the current three-character fixture profile as a stable compatibility
  baseline.
- Allows unknown or unsupported mappings to fail closed deterministically.
- Makes later correction and supersession of mappings auditable.

### Costs

- Four vocabulary members remain intentionally unadmitted until ownership and
  evidence dependencies close.
- Contract/schema casing drift requires a separate reviewed migration.
- External classification schemes require per-edition source and rights review.
- Consumers must carry more context than one convenient “resource class” field.
- Public-safe geometry, policy, evidence, and release remain separate gates.
- Specialized scientific, economic, regulatory, and model review is required.

### Tradeoff

KFM accepts slower semantic admission and more explicit object boundaries in
exchange for reducing false resource certainty, regulatory inflation, sensitive
location exposure, and irreversible data-model drift.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Use `source_role` as resource class | Rejected: evidence-production character is not claim character |
| Keep the vocabulary fixture-local forever | Rejected as the target state: schemas and consumers need reviewed shared names |
| Treat `reserve_estimate` as `RESERVE` automatically | Rejected: source label, scheme, assumptions, and qualified review are required |
| Treat modeled potential as a deposit subtype | Rejected: model output cannot establish a physical deposit |
| Treat permit or production as proof of deposit/operation | Rejected: regulatory/administrative context does not create physical or legal conclusions |
| Create seven complete object schemas immediately | Rejected for the first ratchet: four characters lack accepted ownership and source/evidence semantics |
| Adopt one external reporting standard as universal KFM authority | Deferred: schemes remain versioned source-native references until individually reviewed |
| Infer character from contract filename | Rejected: path and spelling are not semantic evidence |
| Expose one free-text `resource_class` field | Rejected: free text prevents deterministic anti-collapse checks and migration |
| Collapse character and release eligibility | Rejected: semantic identity cannot grant policy or publication state |

[Back to top](#top)

---

<a id="policy-evidence-and-release-boundary"></a>

## Policy, evidence, and release boundary

A complete governed flow should remain:

```text
source record
  -> admitted SourceDescriptor and preserved source role
  -> EvidenceRef resolution and source-native classification
  -> reviewed resource-character mapping
  -> owning semantic object and machine validation
  -> policy / rights / sensitivity / review checks
  -> correction-aware accountability records
  -> release decision and public-safe projection
  -> governed API / map / export / AI interpretation
```

Current repository evidence establishes only selected draft contracts, synthetic
fixtures, validators/tests, and readiness workflows. It does not establish the
middle or final authority transitions.

### Finite failure posture

This ADR does not redefine the repository's accepted or proposed runtime outcome
contracts. A future integration should preserve at least these distinctions:

| Condition | Safe disposition |
|---|---|
| Character support unresolved or ambiguous | `ABSTAIN`, `HOLD`, or review-required outcome under the owning contract |
| Explicit policy, rights, sensitivity, or release prohibition | `DENY` |
| Validator, schema, integrity, source, or evaluator machinery failure | `ERROR` |
| Character and all required evidence/policy/release support close | Governed `ANSWER` or operation-specific allow; never publication by inference |

Reason codes, obligations, and public explanations must be owned by accepted
policy/runtime contracts, not invented ad hoc in this ADR.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

| Responsibility | Authority home | Effect of this ADR |
|---|---|---|
| Architecture decision | `docs/adr/` | Records the proposal only |
| Domain meaning | Geology doctrine and semantic contracts | Informs token meanings; remains draft where marked |
| Machine shape | Geology schema lane | No schema changed by this revision |
| Source admission | Source registry and source policy | No source admitted |
| Evidence closure | EvidenceRef/EvidenceBundle authorities | No evidence resolved |
| Policy and sensitivity | `policy/` plus accepted runtime | No policy activated |
| Validation | fixtures, validators, tests, workflows | Existing bounded proof is described, not widened |
| Review and accountability | review/receipt/proof families | No human review or proof created by prose |
| Release and rollback | `release/` and accountability roots | No release or rollback state changed |
| Public clients | Governed APIs and released artifacts | No route, DTO, layer, export, or AI behavior changed |

### Invariants

1. A token does not certify a resource.
2. A schema pass does not resolve evidence.
3. A fixture does not admit a source.
4. A validator does not make policy.
5. A workflow success does not make proof or release.
6. A permit or production record does not become physical-geology truth.
7. A model does not become occurrence or deposit evidence by confidence alone.
8. A public-safe geometry declaration does not grant release.
9. An `ANSWER` does not publish by itself.
10. Historical source labels, decisions, receipts, and corrections remain
    append-only and traceable.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation rollback

This revision is documentation-only. Before merge, close the pull request and
abandon the branch. After merge, use a reviewed revert or restore prior target
blob `a4b41973fd27b851f5eca60992cb05a38e37008b`. No source, schema, data,
runtime, release, cache, or public artifact requires restoration.

### Decision supersession

If ADR-0030 is later accepted and then replaced:

1. author a successor ADR;
2. record reciprocal supersession links;
3. preserve this record;
4. version the vocabulary and affected schemas;
5. retain source-native labels and historical mappings;
6. provide exact compatibility and migration fixtures;
7. preserve decisions, receipts, and corrections;
8. update consumers and public projections through governed migration;
9. test rollback and replay before retiring aliases.

### Implementation rollback

Any later schema or consumer implementation must carry its own rollback plan.
Rollback must not:

- rewrite immutable source records;
- silently relabel historical characters;
- convert unknown mappings to a stronger character;
- delete prior decisions or receipts;
- expose restricted geometry;
- default to release or public display.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

| Check | Result at this revision |
|---|---|
| ADR identity and exact path | **CONFIRMED** |
| Source metadata | **CONFIRMED proposed** |
| Effective decision status | **CONFIRMED proposed** |
| Same-path Directory Rules placement | **CONFIRMED** |
| Exact seven-token proposed set | **CONFIRMED in ADR** |
| Three substantive draft contracts | **CONFIRMED** |
| Three paired schemas | **CONFIRMED permissive scaffolds** |
| Shared vocabulary schema | **ABSENT** |
| Contract-pointer casing | **CONFLICTED** |
| Three-character fixture profile | **CONFIRMED substantive** |
| Eight exact negative resource-class fixtures | **CONFIRMED** |
| Deterministic no-network validator/tests | **CONFIRMED** |
| Production material-change profile | **CONFIRMED separate process profile** |
| Public-safe geometry profile | **CONFIRMED separate assessment profile** |
| Geology policy evaluator/bundle/consumer | **NOT ESTABLISHED** |
| Latest `domain-geology` run | **CONFIRMED success with proof/release holds** |
| Live source or real record validation | **NOT PERFORMED / NOT AUTHORIZED** |
| EvidenceBundle closure | **NOT ESTABLISHED** |
| Public API/UI/AI behavior | **NOT ESTABLISHED** |
| Local documentation source checks for this edit | **PASS in authoring session** |
| Hosted exact-head checks | **PENDING after pull-request creation** |
| Human review | **PENDING** |
| Release, deployment, publication | **NOT CLAIMED** |

Repository and hosted evidence support bounded implementation claims only. They
do not substitute for scientific, legal, economic, source, evidence, policy,
review, release, or production-system verification.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open questions

1. Which accepted owner reviews reserve-classification mappings and reporting
   schemes?
2. Which semantic contract and responsibility lane own production records?
3. Which semantic contract and responsibility lane own permit status and history?
4. Does modeled potential need a Geology-owned object family, or a shared
   model-output contract with a Geology projection?
5. Which external resource/reserve schemes and editions may be admitted, under
   what rights and mapping rules?
6. Should the current PascalCase contract paths remain canonical, and what
   compatibility treatment is required for lower-case schema pointers?
7. Which source-role/resource-character pairings are universally invalid beyond
   the minimum anti-collapse rules?
8. Should public DTOs expose `resource_character` directly or only a
   public-safe projection with evidence and limitation labels?
9. Which reason codes and obligations belong to unsupported or ambiguous
   character mappings?
10. How should historical mapping corrections propagate through graph, catalog,
    API, map, export, and AI caches?
11. Which Geology schema README update should accompany the first schema ratchet?
12. What is the smallest public-safe source family that can prove the complete
    character/evidence/policy/release path without exposing sensitive resource
    locations?

[Back to top](#top)

---

<a id="references"></a>

## References

### Governing and adjacent decisions

- [ADR operating contract](./README.md)
- [Canonical ADR index](./INDEX.md)
- [ADR-0017 — Source Descriptor Admission Process](./ADR-0017-source-descriptor-admission-process.md)
- [ADR-0020 — Abstain Is a First-Class Decision](./ADR-0020-abstain-is-a-first-class-decision.md)
- [ADR-0024 — Steward Separation of Duties for Release](./ADR-0024-steward-separation-of-duties-for-release.md)
- [ADR-0025 — Public Client Never Reads Canonical or Internal Stores](./ADR-0025-public-client-never-reads-canonical-internal-stores.md)
- [ADR-0029 — Adopt Directory Governance Standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)

### Geology semantics and source posture

- [Geology domain README](../domains/geology/README.md)
- [Geology scope](../domains/geology/SCOPE.md)
- [Geology object families](../domains/geology/OBJECT_FAMILIES.md)
- [Geology source-role matrix](../domains/geology/SOURCE_ROLE_MATRIX.md)
- [Geology sensitivity](../domains/geology/SENSITIVITY.md)
- [Natural Resources sublane](../domains/geology/sublanes/natural_resources.md)
- [Governed source map for the supplied Geology architecture report](../intake/exploratory/geology-natural-resources-architecture-source-map.md)

### Contracts, schemas, fixtures, and validation

- [`MineralOccurrence` contract](../../contracts/domains/geology/MineralOccurrence.md)
- [`ResourceDeposit` contract](../../contracts/domains/geology/ResourceDeposit.md)
- [`ResourceEstimate` contract](../../contracts/domains/geology/ResourceEstimate.md)
- [`ProductionMaterialChange` contract](../../contracts/domains/geology/production_material_change.md)
- [Mineral occurrence schema scaffold](../../schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json)
- [Resource deposit schema scaffold](../../schemas/contracts/v1/domains/geology/resource_deposit.schema.json)
- [Resource estimate schema scaffold](../../schemas/contracts/v1/domains/geology/resource_estimate.schema.json)
- [Geology schema index](../../schemas/contracts/v1/domains/geology/README.md)
- [Resource-class fixture profile](../../fixtures/domains/geology/resource_class/README.md)
- [Resource-class validator](../../tools/validators/domains/geology/validate_resource_class_distinction.py)
- [Resource-class tests](../../tests/domains/geology/test_source_role_anti_collapse.py)
- [Geology policy boundary](../../policy/domains/geology/README.md)
- [Geology workflow](../../.github/workflows/domain-geology.yml)

### Pull-request lineage

- [PR #1926 — bounded Geology resource-class validator](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1926)
- [PR #1934 — initial ADR-0030 proposal](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1934)

[Back to top](#top)

---

<a id="appendix-a--no-loss-reconciliation-ledger"></a>

## Appendix A — No-loss reconciliation ledger

| v0.1 material | v1.1 disposition |
|---|---|
| Proposal and non-binding posture | Preserved and strengthened in status/evidence boundaries |
| Seven-token minimum | Preserved exactly |
| Four orthogonal axes | Preserved as D3 and expanded with policy/release separation |
| Minimum meanings and non-implications | Preserved in the vocabulary table |
| Nine anti-collapse rules | Preserved and expanded to current repository profiles |
| Stewardship table | Preserved with OWNER_TBD/NEEDS VERIFICATION discipline |
| Common source-evidence floor | Preserved and clarified |
| Character-specific evidence | Preserved |
| Three-contract and three-schema compatibility | Preserved and updated against current bytes |
| PR #1926 fixture profile | Preserved and updated as current substantive implementation evidence |
| Existing local class labels | Preserved in boundary examples and open mapping rules |
| No stored-record migration | Preserved |
| Smallest schema-hardening slice | Preserved and expanded into the convergence plan |
| Positive/negative consequences | Preserved |
| Alternatives | Preserved and expanded |
| References | Preserved and updated |
| Proposal/acceptance/schema phases | Preserved and expanded to policy/consumer/release phases |
| Documentation and decision rollback | Preserved |
| Open questions | Preserved and expanded |
| Acceptance gates | Preserved and expanded |
| Non-effects | Preserved across non-goals and authority boundary |
| Change history | Corrected to merged PR #1934 |

No v0.1 semantic decision is silently deleted. This revision changes evidence
classification, current-state accuracy, navigation, governance clarity, and
implementation maturity only.

## Change history

| Date | Version | Status | Change | PR |
|---|---|---|---|---|
| 2026-08-03 | `v0.1` | proposed | Initial minimum vocabulary, stewardship, compatibility, and schema-hardening proposal | [#1934](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1934) |
| 2026-08-14 | `v1.1` | proposed | Same-path repository reconciliation against current contracts, schemas, bounded Geology profiles, policy posture, workflow evidence, and accepted Directory Rules; decision status unchanged | pending review |

## Last reviewed

**2026-08-14** — repository-grounded review against
`main@a59c9005ca3a790846cabdcf1a160222ed73bbe4`.

Review again when:

- ADR-0030 changes status;
- a shared resource-character schema lands;
- one of the three current schemas becomes field-enforcing;
- a contract-pointer casing migration occurs;
- reserve, production, permit, or modeled-potential ownership is accepted;
- a source-native reporting scheme is admitted;
- Geology policy becomes executable;
- public DTO, API, map, graph, export, or AI behavior is implemented;
- evidence, proof, release, correction, or rollback behavior changes;
- the frozen resource-class fixture profile is versioned or superseded;
- six months pass without review.

[Back to top](#top)
